#!/usr/bin/env python3
"""
revisor_gate.py — GATE FUNDIDO (Classe D) do Revisor SOT (DHR-AUDITOR-EXTERNO-009, fase F1).

Funde e amplia os detectores determinísticos existentes numa bateria fixa, para uma Spec (ou documento):
  D bloqueante   validate_spec_sot.py (estrutura) · baselines presentes na raiz · IDs de modelos canônicos que não existem
  D informativo  check_invariants.py (valores e ordem) · check_refs.py · check_doc_sync.py · backlog_triggers.py (ATIVADO)
                 check_rpsa.py · build_map.py --check
                 campos_atribuidos_baseline (campo `x` atribuído a baseline que não o contém) · estado_backlog (estado de BL-nnn
                 citado ≠ RMR-001) · refs_variantes (T04-neg / ADV-X-NN-sufixo sem definição) — achados da medição da SPEC-006
  H sinais       candidatos por palavra-chave a violação de invariante de SENTIDO (AGENTS.md §6/§7): o código levanta,
                 o Revisor CONFIRMA. Nunca bloqueiam. Têm falso alarme e falso negativo por construção.
Classe P (julgamento de sentido, adversarial, epistêmico) NÃO está aqui: é do Revisor (atomic-spec §10.6).

Detector ≠ Gate (ENF-03): o código decide forma/valor/existência (D); o Revisor decide sentido (P). Somente leitura:
nenhum detector escreve na árvore (build_map só com --check). Exit 1 = falha em item D bloqueante; 0 = nenhum D bloqueante
falhou (≠ CONFORME ≠ homologação).

Uso: python scripts/revisor_gate.py <plan.md|doc.md> [--json] [--out evidence.json] [--rapido]
  --rapido  pula os detectores do repositório inteiro (refs/sync/backlog/rpsa/mapa), roda só os que dependem do documento.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_invariants  # noqa: E402

BASELINES = ["ROADMAP.md", "atomic-spec.md", "governance/RULES.md"]            # Passo 0 (núcleo sempre obrigatório)
ID_CANONICO = re.compile(r"(?<![A-Za-z]-)(?<!/)\b(CHM|CEM|CCM|CEE|GMC|SDD|PPQ|SAS|CR)-(\d{3})\b")  # modelos canônicos (AGENTS.md §6 item 12); (?<!X-) ignora RULE-CEE-003

# negação OU contexto que DESCREVE o comportamento proibido (caso adversarial, cenário de teste, citação da própria regra)
NEGA = re.compile(r"\b(n[ãa]o|nada|nunca|jamais|sem|proíbe|proibid\w*|vedad\w*|apenas notifica|fora d[oae]s?|viola\w*|rejeitad\w*|adversari\w*|ADV-\w+|DADO|cen[áa]rio|INV-\d{2})\b|≠", re.I)

# H — sinais por palavra-chave. Fonte de cada um: AGENTS.md §6/§7 (invariante ou decisão fechada). (código, regex, fonte)
SINAIS_H = [
    ("H-ORDEM", re.compile(r"\bSOT\b.{0,50}\b(executa|envia|opera|coloca)\b.{0,40}\b(ordem|ordens)\b", re.I), "AGENTS.md §6 item 9 (SOT não executa ordem)"),
    ("H-ICT-HIPOTESE", re.compile(r"\bICT\b.{0,50}\b(cria|criam|gera|geram|abre)\b.{0,40}hip[óo]teses?", re.I), "AGENTS.md §6 item 2 (ICT não cria hipótese)"),
    ("H-CUSTO-VETOR", re.compile(r"\bcusto\b.{0,70}(Conviction Vector|vetor).{0,40}|(Conviction Vector|vetor).{0,70}\bcusto\b", re.I), "AGENTS.md §6 item 8 (custo nunca entra no vetor)"),
    ("H-REMOCAO", re.compile(r"hip[óo]teses?.{0,60}\b(removid\w*|apagad\w*|deletad\w*|exclu[ií]d\w*)\b|\b(removid\w*|apagad\w*|deletad\w*)\b.{0,50}hip[óo]teses?", re.I), "AGENTS.md §6 item 10 (nada é deletado)"),
    ("H-PARENT-ID", re.compile(r"sub-?hip[óo]teses?.{0,60}\bsem\s+(necessidade\s+de\s+)?`?parent_id`?", re.I), "AGENTS.md §6 item 2 (sub-hipóteses com parent_id)"),
    ("H-EVENTBUS", re.compile(r"Event Bus.{0,50}fonte de verdade|Blackboard.{0,40}apenas replica", re.I), "AGENTS.md §7 EVENT-BUS-001 (Blackboard guarda a verdade)"),
    ("H-REGIME-GATE", re.compile(r"regime[^.]{0,40}\b(é|como|tratad\w+ como)\s+(um\s+)?(gate|veto)\b|regime[^.]{0,30}\bveta\b", re.I), "AGENTS.md §7 Q-A9 (regime é dimensão temporal, não gate/veto)"),
    ("H-SYNTH-SEPARADO", re.compile(r"Synthesis Agent.{0,60}\b(separado|permanece)\b", re.I), "AGENTS.md §6 item 9 / §7 B-001+ADR-MANAGER-001 (Synthesis absorvido pelo Manager)"),
    ("H-VETOR-1X", re.compile(r"(Conviction Vector|vetor).{0,80}\b(uma [úu]nica vez|apenas uma vez)\b", re.I), "AGENTS.md §7 Q-A5 (invocado 2x por ciclo)"),
    ("H-REFUTED-SINAL", re.compile(r"REFUTED.{0,60}\b(gera|pode gerar|emite|produz)\b.{0,15}sinal", re.I), "AGENTS.md §6 item 3 (CHM-001: REFUTED é terminal)"),
]


def checar_baselines(root=ROOT):
    return [b for b in BASELINES if not (Path(root) / b).is_file()]


def ids_canonicos_existentes(root=ROOT):
    return {m.group(0) for p in (Path(root) / "canon").glob("*.md") for m in [ID_CANONICO.match(p.name)] if m}


def checar_ids_canonicos(texto, root=ROOT):
    """IDs de modelo canônico citados que não existem em canon/ (alucinação documental — Passo 4)."""
    existentes = ids_canonicos_existentes(root)
    achados = []
    for i, linha in enumerate(texto.splitlines(), 1):
        for m in ID_CANONICO.finditer(linha):
            if m.group(0) not in existentes:
                achados.append((i, m.group(0)))
    return achados


# --- detectores D informativos (achados da medição do Revisor na SPEC-006, 2026-10-12) -------------------------------
_BASE_ID = r"(?:CEM|CHM|CCM|CEE|GMC|SDD|PPQ|SAS|CR)-\d{3}|SPEC-0\d{2}"
_ATRIB = re.compile(r"`([a-z][a-z0-9]*_[a-z0-9_]+)`[^`\n]{0,40}?\b(?:é|são|do|da|de|vem\s+d[oa]|atribu[ií]d[oa]\s+(?:ao|à)|pertence\s+ao)\s+(?:o\s+|a\s+)?(" + _BASE_ID + r")\b")
_ATRIB_ISENTA = re.compile(r"\[PROPOSTA\]|proposta|\blocal\b|\bnovo\b|renome|n[ãa]o existe|inexistente|0 ocorr", re.I)


def _arquivo_baseline(bid, root):
    root = Path(root)
    if bid.startswith("SPEC-"):
        p = root / "specs" / "features" / bid / "plan.md"
        return p if p.is_file() else None
    c = sorted((root / "canon").glob(bid + "*.md"))
    return c[0] if c else None


def campos_atribuidos_baseline(texto, root=ROOT):
    """Campo `snake_case` atribuído (na mesma linha) a um baseline (modelo canônico ou SPEC) cujo arquivo NÃO contém o campo.
    Candidato a [FONTE] inventada (RULE-HD-04/RULE-MET-01). Linhas marcadas [PROPOSTA]/local/novo são isentas."""
    cache, achados = {}, []
    for i, linha in enumerate(texto.splitlines(), 1):
        if _ATRIB_ISENTA.search(linha):
            continue
        for m in _ATRIB.finditer(linha):
            campo, bid = m.group(1), m.group(2)
            if bid not in cache:
                f = _arquivo_baseline(bid, root)
                cache[bid] = f.read_text(encoding="utf-8", errors="replace") if f else None
            if cache[bid] is not None and campo not in cache[bid]:
                achados.append((i, campo, bid))
    return achados


_ESTADO_RE = re.compile(r"(BL-\d{3})\b[^.\n]{0,80}?\b(ATIVADO|Em espera|Absorvido|Descartado|Diferido)\b")
_ESTADO_ISENTA = re.compile(r"~~|riscad|\bn[ãa]o\b|\bNÃO\b|\bsem\b|promov|antes|anterior|gatilho|devolvid", re.I)


def estados_backlog(root=ROOT):
    """{BL-nnn: estado vigente} do painel backlog/RMR-001 (1º termo em negrito da coluna Estado)."""
    f = Path(root) / "backlog" / "RMR-001_Painel_Backlog.md"
    if not f.is_file():
        return {}
    out = {}
    for linha in f.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"\|\s*\*\*(BL-\d{3})\*\*\s*\|", linha)
        if not m:
            continue
        cel = linha.split("|")
        if len(cel) > 7:
            e = re.search(r"\*\*([^*]+)\*\*", cel[7]) or re.match(r"\s*(\S+(?: \S+)?)", cel[7])
            if e:
                out[m.group(1)] = e.group(1).strip()
    return out


_CANDIDATO = re.compile(r"^\|\s*Status\s*\|[^\n]*CANDIDAT", re.M | re.I)


def estado_backlog(texto, root=ROOT):
    """Estado de BL-nnn citado no documento que difere do painel RMR-001 (negações/histórico isentos).
    Só incide em documento CANDIDATO (linha Status): em Spec homologada o estado escrito é o do momento da homologação e
    não pode ser reescrito (INV-07) — divergência histórica ali não é defeito."""
    if not _CANDIDATO.search(texto):
        return []
    reais, achados = estados_backlog(root), []
    for i, linha in enumerate(texto.splitlines(), 1):
        for m in _ESTADO_RE.finditer(linha):
            bl, citado = m.group(1), m.group(2)
            trecho = linha[m.start():m.end()]
            if bl in reais and citado.lower() != reais[bl].lower() and not _ESTADO_ISENTA.search(trecho):
                achados.append((i, bl, citado, reais[bl]))
    return achados


_VARIANTE = re.compile(r"\b((?:T\d{2}|ADV-[A-Z]+-\d{2}|EC-[A-Z]+-\d{3})-[a-z]+)\b")


def refs_variantes(texto):
    """Referência a variante com sufixo (T04-neg, ADV-X-06-neg) que nunca é definida como item (início de linha/cabeçalho)."""
    definidos = {m.group(1) for ln in texto.splitlines() for m in [re.match(r"^[\s#>*|-]*\**((?:T\d{2}|ADV-[A-Z]+-\d{2}|EC-[A-Z]+-\d{3})-[a-z]+)\b", ln)] if m}
    achados = []
    for i, linha in enumerate(texto.splitlines(), 1):
        for m in _VARIANTE.finditer(linha):
            if m.group(1) not in definidos:
                achados.append((i, m.group(1)))
    return achados


def sinais_h(texto):
    out = []
    for i, linha in enumerate(texto.splitlines(), 1):
        for cod, rx, fonte in SINAIS_H:
            if rx.search(linha) and (cod == "H-PARENT-ID" or not NEGA.search(linha)):
                out.append({"codigo": cod, "linha": i, "trecho": linha.strip()[:160], "fonte": fonte})
    return out


def _run(nome, cmd, classe, bloqueante, cwd=ROOT):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        saida = (p.stdout or "") + (p.stderr or "")
        return {"nome": nome, "classe": classe, "bloqueante": bloqueante, "exit_code": p.returncode,
                "output_sha256": hashlib.sha256(saida.encode("utf-8")).hexdigest(), "tail": [l for l in saida.splitlines() if l.strip()][-4:]}
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return {"nome": nome, "classe": classe, "bloqueante": bloqueante, "exit_code": 127,
                "output_sha256": hashlib.sha256(b"").hexdigest(), "tail": [f"indisponível: {type(e).__name__}"]}


def rodar(doc, rapido=False, root=ROOT):
    root = Path(root)
    docp = Path(doc)
    rel = str(docp.resolve().relative_to(root.resolve())).replace("\\", "/") if docp.resolve().is_relative_to(root.resolve()) else str(docp)
    texto = docp.read_text(encoding="utf-8", errors="replace")
    py = sys.executable
    itens = []

    faltam = checar_baselines(root)
    itens.append({"nome": "baselines_na_raiz", "classe": "D", "bloqueante": True, "exit_code": 1 if faltam else 0,
                  "output_sha256": "", "tail": [f"ausentes: {faltam}" if faltam else "ROADMAP.md, atomic-spec.md, governance/RULES.md presentes"]})
    ids = checar_ids_canonicos(texto, root)
    itens.append({"nome": "ids_canonicos_existem", "classe": "D", "bloqueante": True, "exit_code": 1 if ids else 0,
                  "output_sha256": "", "tail": [f"linha {l}: {i} não existe em canon/" for l, i in ids[:6]] or ["todos os IDs de modelo canônico citados existem"]})
    if rel.startswith("specs/features/") and rel.endswith("/plan.md"):
        itens.append(_run("validate_spec_sot", [py, "scripts/validate_spec_sot.py", rel], "D", True, root))
    else:
        itens.append({"nome": "validate_spec_sot", "classe": "D", "bloqueante": False, "exit_code": 0, "output_sha256": "",
                      "tail": ["NÃO APLICÁVEL: documento fora de specs/features/<SPEC>/plan.md (sem gate de estrutura)"]})
    inv = [f"{rel}:{ln} [{c}] {m}" for ln, c, m, _f in check_invariants.checar_texto(texto)]
    itens.append({"nome": "check_invariants", "classe": "D", "bloqueante": False, "exit_code": 1 if inv else 0,
                  "output_sha256": "", "tail": inv[:8] or ["nenhum desvio de valor/ordem"]})
    for nome, achados, fmt in (
        ("campos_atribuidos_baseline", campos_atribuidos_baseline(texto, root),
         lambda a: f"{rel}:{a[0]} campo `{a[1]}` atribuído a {a[2]}, que não o contém"),
        ("estado_backlog", estado_backlog(texto, root),
         lambda a: f"{rel}:{a[0]} {a[1]} citado como {a[2]}; painel RMR-001 = {a[3]}"),
        ("refs_variantes", refs_variantes(texto),
         lambda a: f"{rel}:{a[0]} variante '{a[1]}' nunca definida como item"),
    ):
        det = [fmt(a) for a in achados]
        itens.append({"nome": nome, "classe": "D", "bloqueante": False, "exit_code": 1 if det else 0,
                      "output_sha256": "", "tail": det[:6] or ["nenhum achado"], "detalhes": det})
    if not rapido:
        itens.append(_run("check_refs", [py, "scripts/check_refs.py"], "D", False, root))
        itens.append(_run("check_doc_sync", [py, "scripts/check_doc_sync.py"], "D", False, root))
        itens.append(_run("backlog_triggers", [py, "scripts/backlog_triggers.py"], "D", False, root))
        itens.append(_run("check_rpsa", [py, "scripts/check_rpsa.py"], "D", False, root))
        itens.append(_run("build_map_check", [py, "scripts/build_map.py", "--check"], "D", False, root))
    sinais = sinais_h(texto)
    for s in sinais:
        s["ref"] = f"{rel}:{s['linha']}"                      # arquivo:linha completo (o Revisor cita assim)
    for g in itens:
        if g["nome"] == "check_invariants":
            g["detalhes"] = inv                               # lista completa (a saída humana mostra só as primeiras)
        if g["nome"] == "ids_canonicos_existem":
            g["detalhes"] = [f"{rel}:{ln} {i} não existe em canon/" for ln, i in ids]
    reprovado = any(i["bloqueante"] and i["exit_code"] != 0 for i in itens)
    return {"schema_version": "2.0", "documento": rel, "gates": itens, "sinais_H": sinais,
            "veredito_D": "REPROVADO_D (NÃO CONFORME Crítica automática)" if reprovado else "PASSOU_D (≠ CONFORME ≠ homologação)",
            "nota": "Classe P (sentido, adversarial, epistêmico) não é coberta: é julgamento do Revisor."}, reprovado


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("doc")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--rapido", action="store_true")
    a = ap.parse_args(argv)
    ev, reprovado = rodar(a.doc, a.rapido)
    if a.out:
        Path(a.out).write_text(json.dumps(ev, ensure_ascii=False, indent=2), encoding="utf-8")
    if a.json:
        print(json.dumps(ev, ensure_ascii=False, indent=2))
    else:
        print(f"GATE FUNDIDO (Classe D) — {ev['documento']}")
        for g in ev["gates"]:
            marca = "OK " if g["exit_code"] == 0 else ("RED" if g["bloqueante"] else "AVISO")
            print(f"  {marca:5} [{g['classe']}{'*' if g['bloqueante'] else ' '}] {g['nome']}: {g['tail'][-1] if g['tail'] and g['nome'] in ('validate_spec_sot','check_refs','check_doc_sync','backlog_triggers','check_rpsa','build_map_check') else (g['tail'][0] if g['tail'] else '')}")
        print(f"  SINAIS H (candidatos — o Revisor confirma): {len(ev['sinais_H'])}")
        for s in ev["sinais_H"][:10]:
            print(f"    linha {s['linha']} [{s['codigo']}] {s['trecho']}")
        print(f"VEREDITO D: {ev['veredito_D']}")
        print("(*) = bloqueante. Classe P fica com o Revisor.")
    return 1 if reprovado else 0


if __name__ == "__main__":
    sys.exit(main())
