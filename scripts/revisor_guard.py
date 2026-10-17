#!/usr/bin/env python3
"""
revisor_guard.py — guarda determinística do fim do Revisor SOT (hook SubagentStop; DHR-AUDITOR-EXTERNO-017).

O hook recebe no stdin o JSON do evento (agent_type, agent_transcript_path, last_assistant_message, stop_hook_active, cwd). Quando
o subagente é o Revisor e vai encerrar, o CÓDIGO confere, sem depender de o modelo lembrar:
  G1  o núcleo do Passo 0 foi ABERTO nesta sessão (ROADMAP.md, atomic-spec.md, RULES.md, RMR-001) — o Revisor vinha declarando
      "não verificado" em vez de abrir;
  G2  o gate de código (revisor_gate) foi rodado pelo HARNESS sobre o artefato revisado e o resultado consta do parecer — assim o
      gate participa mesmo quando a ferramenta MCP não carrega (pasta não confiável / nuvem);
  G3  cada citação arquivo:linha do parecer existe e, quando há trecho entre aspas/crases, o trecho está perto da linha citada.
Violação => exit 2 com a lista no stderr: o Revisor continua e corrige (uma única vez: com stop_hook_active=true libera, para não
travar). Falha do próprio script => exit 0 (nunca derruba a sessão). Detector ≠ Gate (ENF-03): confere FORMA e EXISTÊNCIA; o sentido
do parecer continua sendo do Revisor, a homologação de Andraus.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

NUCLEO = [("ROADMAP.md", "ROADMAP.md"), ("atomic-spec.md", "atomic-spec.md"), ("RULES.md", "governance/RULES.md"), ("RMR-001", "backlog/RMR-001")]
_CIT = re.compile(r"([\w./\\-]+\.(?:md|json|py|js|yml|txt))\s*[:#]\s*(\d{1,5})(?:\s*[-–]\s*(\d{1,5}))?")
_TRECHO = re.compile(r"[`\"“]([^`\"”\n]{20,200})[`\"”]")


def _strs(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from _strs(v)
    elif isinstance(x, list):
        for v in x:
            yield from _strs(v)


def ler_transcript(path):
    """(prompt_inicial, [strings de entradas de ferramentas de leitura])."""
    prompt, usos = "", []
    try:
        linhas = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return prompt, usos
    for ln in linhas:
        try:
            o = json.loads(ln)
        except ValueError:
            continue
        msg = o.get("message") or {}
        cont = msg.get("content")
        if o.get("type") == "user" and not prompt:
            prompt = " ".join(_strs(cont))
        if o.get("type") == "assistant" and isinstance(cont, list):
            for b in cont:
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") in ("Read", "Grep", "mcp__sot-revisor-gate__revisor_gate"):
                    usos.append(" ".join(_strs(b.get("input"))))
    return prompt, usos


def fontes_nao_abertas(usos):
    return [rotulo for chave, rotulo in NUCLEO if not any(chave in u for u in usos)]


def alvo_da_revisao(prompt):
    """Caminho do plan.md (ou documento .md) citado no pedido, se existir."""
    for m in re.finditer(r"(/[\w./-]+\.md|specs/features/SPEC-\d{3}/plan\.md)", prompt):
        p = Path(m.group(1))
        p = p if p.is_absolute() else ROOT / p
        if p.is_file() and p.name == "plan.md":
            return p
    for m in re.finditer(r"(/[\w./-]+\.md)", prompt):
        p = Path(m.group(1))
        if p.is_file():
            return p
    return None


def rodar_gate(alvo):
    import revisor_gate
    ev, _ = revisor_gate.rodar(alvo, rapido=False, root=ROOT)
    linhas = [f"VEREDITO D: {ev['veredito_D']}"]
    for g in ev["gates"]:
        if g["exit_code"] != 0:
            for d in (g.get("detalhes") or g.get("tail") or [])[:4]:
                linhas.append(f"  [{g['nome']}] {d}")
    linhas.append(f"  sinais H: {len(ev['sinais_H'])}")
    return ev, linhas


def _norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def _resolver(nome, dirs):
    p = Path(nome)
    cands = [p] if p.is_absolute() else [ROOT / p] + [d / p for d in dirs]
    for c in cands:
        if c.is_file():
            return c
    base = p.name
    achados = [c for d in [ROOT] + dirs for c in Path(d).rglob(base) if ".git" not in c.parts and "node_modules" not in c.parts] if base else []
    return achados[0] if len(achados) == 1 else None


def conferir_citacoes(texto, dirs):
    """Falhas de citação arquivo:linha[+trecho]. Citação cujo arquivo não se resolve só falha se tiver diretório (parece caminho)."""
    falhas, vistos = [], set()
    for m in _CIT.finditer(texto):
        nome, lo = m.group(1), int(m.group(2))
        hi = int(m.group(3) or lo)
        chave = (nome, lo, hi)
        if chave in vistos:
            continue
        vistos.add(chave)
        arq = _resolver(nome, dirs)
        if arq is None:
            if "/" in nome:
                falhas.append(f"{nome}:{lo} — arquivo não encontrado")
            continue
        linhas = arq.read_text(encoding="utf-8", errors="replace").splitlines()
        if lo > len(linhas):
            falhas.append(f"{nome}:{lo} — o arquivo tem só {len(linhas)} linhas")
            continue
        t = _TRECHO.search(texto, m.end(), m.end() + 260)
        if not t:
            continue
        trecho = _norm(t.group(1).rstrip(". …"))[:60]
        if len(trecho) < 15:
            continue
        janela = _norm(" ".join(linhas[max(0, lo - 4):hi + 3]))
        if trecho in janela:
            continue
        todo = _norm(" ".join(linhas))
        if trecho in todo:
            falhas.append(f"{nome}:{lo} — o trecho citado existe, mas em outra linha")
        else:
            falhas.append(f"{nome}:{lo} — o trecho citado não está no arquivo: «{t.group(1)[:60]}»")
    return falhas[:12]


def avaliar(evento):
    """-> lista de mensagens de violação (vazia = liberar)."""
    if not re.search(r"revisor", str(evento.get("agent_type", "")), re.I):
        return []
    if evento.get("stop_hook_active"):
        return []
    prompt, usos = ler_transcript(evento.get("agent_transcript_path", ""))
    final = str(evento.get("last_assistant_message", ""))
    msgs = []
    faltam = fontes_nao_abertas(usos)
    if faltam:
        msgs.append("G1 — núcleo do Passo 0 NÃO aberto nesta sessão: " + ", ".join(faltam) +
                    ". Abra-os (Read/Grep) e confira as afirmações do artefato que dependem deles (M1/M4); só declare 'não verificado' o que de fato não conseguir abrir.")
    alvo = alvo_da_revisao(prompt)
    dirs = [alvo.parent] if alvo else []
    if alvo:
        try:
            ev, linhas = rodar_gate(alvo)
            if "VEREDITO D" not in final or "NÃO VERIFICADO" in final.upper():
                msgs.append("G2 — o gate de código foi rodado pelo harness sobre " + str(alvo) + " (não depende da sua ferramenta). Incorpore ao parecer, "
                            "na seção 3, e confirme/descarte cada achado com arquivo:linha:\n" + "\n".join(linhas))
        except Exception as e:                       # o gate quebrado não derruba o Revisor
            msgs.append(f"G2 — o gate do harness falhou ({type(e).__name__}); declare GATE NÃO VERIFICADO.")
    bad = conferir_citacoes(final, dirs)
    if bad:
        msgs.append("G3 — citações do parecer que não conferem (corrija ou retire; sem evidência não há achado):\n  " + "\n  ".join(bad))
    return msgs


def main():
    try:
        evento = json.loads(sys.stdin.read() or "{}")
        msgs = avaliar(evento)
    except Exception:
        return 0
    if msgs:
        sys.stderr.write("GUARDA DO REVISOR (DHR-AUDITOR-EXTERNO-017) — antes de encerrar:\n" + "\n".join(msgs) + "\n")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
