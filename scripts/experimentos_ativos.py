#!/usr/bin/env python3
"""experimentos_ativos.py — garante que EXPERIMENTOS e REGRAS aprovados por Andraus para um Plan entrem nos pedidos aos agentes
construtores, DETERMINISTICAMENTE (DHR-PROCESSO-EXPERIMENTOS-001, ordem de Andraus 2026-11-14).

Falha que previne: Andraus aprovou (DHR-RETRO-003, P10) um experimento "para o PRÓXIMO Plan que mandar abrir"; o Plan da SPEC-008 abriu e
o Orquestrador não o incluiu nos pedidos das rodadas R1/R2 — a regra dependia de lembrança. Agora o registro versionado
`governance/EXPERIMENTOS-ATIVOS.json` é lido por um hook PreToolUse (Agent|SendMessage) que NEGA o pedido ao Especificador/Revisor sobre o
Plan de uma Spec no escopo de um experimento ativo quando:
  1. o pedido não traz a cláusula `EXPERIMENTO: <id>` (linha própria) — a mensagem de negação traz o texto das regras a colar;
  2. (pedido ao Revisor) a rodada seguinte ultrapassa `teto_rodadas_revisao` (rodadas = pareceres existentes da linha "SPEC-nnn PLAN" + 1)
     e `escalado_por_andraus` é falso => escalar a Andraus (ele decide; registrar em ata e marcar o campo);
  3. (pedido ao Revisor) da rodada `hash_a_partir_da_rodada` em diante falta `SHA256-ALVO: <64 hex>`.
Escopo: {"tipo":"spec","specs":[...]} ou {"tipo":"proximo-plan","apos":"AAAA-MM-DD"} (vale para o 1º Plan em redação até ser vinculado;
`--ci` falha se existir Plan em redação e o experimento "próximo Plan" ainda não tem `vinculado_a`).
Detector/trava de forma (ENF-03): não julga o mérito, nunca decide por Andraus, nunca fecha decisão aberta (CONS-01). Falha de leitura => libera
(fail-open), exceto a negação por regra explícita acima.

Uso:
  (sem argumentos)        hook PreToolUse: lê o evento em stdin e emite permissionDecision deny quando a regra nega.
  --ci                    exit 1 se o registro é inválido ou se há experimento "próximo Plan" não vinculado com Plan em redação.
  --listar                imprime os experimentos ativos.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent
REGISTRO = "governance/EXPERIMENTOS-ATIVOS.json"
CAMPOS = {"id", "descricao", "ata", "estado", "escopo", "marcador"}


def _campo(texto, nome):
    ach = re.findall(rf"^[ \t]*{nome}:[ \t]*(\S.*?)[ \t]*$", texto or "", re.M)
    return ach[0] if len(set(ach)) == 1 else None


def ler_registro(root):
    return json.loads((Path(root) / REGISTRO).read_text(encoding="utf-8"))


def validar(reg):
    """Lista de problemas do registro (vazia = válido)."""
    erros = []
    if not isinstance(reg.get("experimentos"), list):
        return ["registro sem lista `experimentos`"]
    ids = set()
    for e in reg["experimentos"]:
        falta = CAMPOS - set(e)
        if falta:
            erros.append(f"{e.get('id', '?')}: campos ausentes {sorted(falta)}")
            continue
        if e["id"] in ids:
            erros.append(f"{e['id']}: id duplicado")
        ids.add(e["id"])
        if not e["marcador"].startswith("EXPERIMENTO:") or e["id"] not in e["marcador"]:
            erros.append(f"{e['id']}: marcador deve ser `EXPERIMENTO: {e['id']}`")
        if e["estado"] not in ("ativo", "encerrado"):
            erros.append(f"{e['id']}: estado inválido")
        esc = e["escopo"]
        if esc.get("tipo") == "spec":
            if not esc.get("specs") or not all(re.fullmatch(r"SPEC-\d{3}", x) for x in esc["specs"]):
                erros.append(f"{e['id']}: escopo spec sem lista válida de SPEC-nnn")
        elif esc.get("tipo") == "proximo-plan":
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(esc.get("apos", ""))):
                erros.append(f"{e['id']}: escopo proximo-plan sem `apos` AAAA-MM-DD")
        else:
            erros.append(f"{e['id']}: escopo.tipo desconhecido")
        for k in ("teto_rodadas_revisao", "hash_a_partir_da_rodada"):
            if k in e and not (isinstance(e[k], int) and e[k] >= 1):
                erros.append(f"{e['id']}: {k} deve ser inteiro >= 1")
    return erros


def _rodadas_plan(root, spec):
    """nº de pareceres de revisão do Plan da Spec (maior rodada da linha 'SPEC-nnn PLAN')."""
    import loop_ledger
    linhas = loop_ledger.coletar(Path(root))
    rodadas = linhas.get(f"{spec} PLAN", {})
    return max(rodadas) if rodadas else 0


def _plans_em_redacao(root):
    """Specs com parecer de Plan e SEM aprovação final (Plan homologado como BASELINE)."""
    import avaliacao_spec
    import loop_ledger
    aprovadas = avaliacao_spec.aprovadas(Path(root))
    return sorted({k.split()[0] for k in loop_ledger.coletar(Path(root)) if k.endswith(" PLAN")} - set(aprovadas))


def _aplica(exp, spec, root):
    if exp["estado"] != "ativo":
        return False
    esc = exp["escopo"]
    if esc["tipo"] == "spec":
        return spec in esc["specs"]
    vinc = exp.get("vinculado_a")
    if vinc:
        return spec == vinc
    return spec in _plans_em_redacao(root) or not (Path(root) / "specs" / "features" / spec / "plan.md").exists()


def _tipo_agente(entrada):
    prompt = str(entrada.get("prompt") or entrada.get("message") or "")
    agente = str(entrada.get("subagent_type") or "").lower()
    classe = (_campo(prompt, "CLASSE-TAREFA") or "").upper()
    if "revisor" in agente or classe.startswith("S"):
        return "revisor", prompt
    if "especificador" in agente or classe == "O":
        return "especificador", prompt
    return None, prompt


def decidir(entrada, root=ROOT):
    """-> None (libera) ou o motivo da negação."""
    tipo, prompt = _tipo_agente(entrada)
    if not tipo:
        return None
    alvo = _campo(prompt, "ALVO") or ""
    m = re.search(r"SPEC-\d{3}", alvo) or re.search(r"SPEC-\d{3}", prompt)
    if not m or not re.search(r"plan\.md|\bPlan\b", prompt):
        return None                                   # não é pedido sobre o Plan de uma Spec
    spec = m.group(0)
    try:
        reg = ler_registro(root)
    except (OSError, ValueError):
        return None                                   # sem registro legível: fail-open
    motivos = []
    for exp in reg.get("experimentos", []):
        if not _aplica(exp, spec, root):
            continue
        if exp["marcador"] not in prompt.splitlines() and not re.search(rf"^[ \t]*{re.escape(exp['marcador'])}\b", prompt, re.M):
            motivos.append(f"o pedido sobre o Plan da {spec} não traz a cláusula `{exp['marcador']}` (linha própria). "
                           f"Regras do experimento {exp['id']} ({exp['ata']}): {exp['descricao']}")
            continue
        if tipo == "revisor":
            n = _rodadas_plan(root, spec)
            proxima = n + 1
            teto = exp.get("teto_rodadas_revisao")
            if teto and proxima > teto and not exp.get("escalado_por_andraus"):
                motivos.append(f"TETO de {teto} rodadas de revisão do Plan da {spec} atingido (há {n} parecer(es); este pedido seria a rodada {proxima}). "
                               f"Experimento {exp['id']}: escalar a Andraus (decisão dele; registrar em ata e marcar `escalado_por_andraus` no registro).")
            h = exp.get("hash_a_partir_da_rodada")
            if h and proxima >= h and not re.search(r"^[ \t]*SHA256-ALVO:[ \t]*`?[0-9a-fA-F]{64}", prompt, re.M):
                motivos.append(f"experimento {exp['id']}: da rodada {h} em diante o pedido ao Revisor exige `SHA256-ALVO: <64 hex>` (este seria a rodada {proxima}).")
    return " | ".join(motivos) if motivos else None


def ci(root=ROOT):
    problemas = []
    try:
        reg = ler_registro(root)
    except (OSError, ValueError) as e:
        return [f"registro ilegível: {e}"]
    problemas += validar(reg)
    em_redacao = _plans_em_redacao(root)
    for exp in reg.get("experimentos", []):
        if exp["estado"] == "ativo" and exp["escopo"].get("tipo") == "proximo-plan" and not exp.get("vinculado_a") and em_redacao:
            problemas.append(f"{exp['id']}: aprovado para o 'próximo Plan' e há Plan em redação ({', '.join(em_redacao)}) sem `vinculado_a` — "
                             "vincule o experimento ao Plan (registro + ata) e inclua a cláusula nos pedidos.")
    return problemas


def hook():
    try:
        ev = json.loads(sys.stdin.read() or "{}")
        if ev.get("tool_name") not in ("Agent", "Task", "SendMessage"):
            return 0
        motivo = decidir(ev.get("tool_input") or {})
        if motivo:
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                     "permissionDecisionReason": "EXPERIMENTOS ATIVOS (DHR-PROCESSO-EXPERIMENTOS-001) — " + motivo}}, ensure_ascii=False))
    except Exception:
        pass
    return 0


def main(argv):
    if len(argv) < 2:
        return hook()
    if argv[1] == "--ci":
        p = ci()
        for x in p:
            print("EXPERIMENTOS:", x)
        if not p:
            print("Experimentos ativos: registro válido e sem Plan em redação não vinculado.")
        return 1 if p else 0
    if argv[1] == "--listar":
        for e in ler_registro(ROOT)["experimentos"]:
            print(f"{e['id']} [{e['estado']}] escopo={json.dumps(e['escopo'], ensure_ascii=False)} ata={e['ata']}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
