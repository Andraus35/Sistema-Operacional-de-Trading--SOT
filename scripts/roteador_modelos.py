#!/usr/bin/env python3
"""
roteador_modelos.py — roteador DETERMINÍSTICO de modelo por tarefa (hook PreToolUse/Agent; DHR-ROTEAMENTO-003).

Implementa em código as regras R1/R2/R4/R12 da Matriz de Roteamento Meta (proposta AUDITORIA-ROTEAMENTO-MODELOS §7) e a regra D1 da
DHR-ROTEAMENTO-001: ao invocar o Agent, o CÓDIGO confere `subagent_type` + `model`/`effort` por invocação contra a tabela abaixo.
  R-AC   Especificador SOT e Revisor SOT: modelo só pelo frontmatter — `model`/`effort` por invocação => NEGA.
  R-GATE tarefa de gate/revisão/parecer/homologação com modelo de baixo custo (haiku) => NEGA (ENF-03: Haiku nunca é gate).
  R-N4   tarefa soberana (homologar, fechar/abrir decisão) delegada a modelo de baixo custo => NEGA.
  R-ALLOW `model` por invocação só dentro de MODELOS_PERMITIDOS; subagente auxiliar sem `model` herda o da sessão (permitido).
Tabela estática e versionada (R1); sem roteador aprendido. Detector/regra de forma, não julga o mérito (ENF-03). Falha => libera
(fail-open). Telemetria mínima (R8): uma linha JSON por invocação em <tmp>/sot-roteador/uso.jsonl (dado de estado, não normativo).
"""
import json
import re
import sys
import tempfile
import time
from pathlib import Path

AGENTES_CONSTRUCAO_FIXOS = re.compile(r"(especificador|revisor)\s*sot", re.I)
MODELOS_PERMITIDOS = re.compile(r"^(opus|sonnet|haiku|fable|claude-(opus|sonnet|haiku|fable)-[\w.-]+)$", re.I)
BAIXO_CUSTO = re.compile(r"haiku", re.I)
TAREFA_GATE = re.compile(r"\b(gate|revisor_gate|parecer|revis[aã]o|revisar|auditar|auditoria|conformidade|conforme|valida[cç][aã]o de spec)\b", re.I)
TAREFA_SOBERANA = re.compile(r"\b(homolog\w*|fechar decis[aã]o|abrir decis[aã]o|baseline)\b", re.I)


def decidir(entrada):
    """-> (decisao, motivo) com decisao em {'permitir','negar'}."""
    tipo = str(entrada.get("subagent_type") or "")
    modelo = entrada.get("model")
    esforco = entrada.get("effort")
    texto = " ".join(str(entrada.get(k) or "") for k in ("description", "prompt"))
    if AGENTES_CONSTRUCAO_FIXOS.search(tipo):
        if modelo or esforco:
            return "negar", (f"R-AC: '{tipo}' roda no modelo do frontmatter; `model`/`effort` por invocação são proibidos (DHR-ROTEAMENTO-001 D1/D6; "
                             "mudar modelo = ata de Andraus + edição do frontmatter).")
        return "permitir", "R-AC: sem parâmetro de modelo"
    if not modelo:
        return "permitir", "herda o modelo da sessão"
    if not MODELOS_PERMITIDOS.match(str(modelo)):
        return "negar", f"R-ALLOW: modelo '{modelo}' fora da tabela permitida (opus|sonnet|haiku|fable|claude-*)."
    if BAIXO_CUSTO.search(str(modelo)) and TAREFA_GATE.search(texto):
        return "negar", "R-GATE: tarefa de gate/revisão/parecer não pode rodar em Haiku (ENF-03; MRM R4). Use código (revisor_gate) ou o Revisor titular."
    if BAIXO_CUSTO.search(str(modelo)) and TAREFA_SOBERANA.search(texto):
        return "negar", "R-N4: tarefa soberana (homologação/decisão/baseline) não é delegável a modelo de baixo custo."
    return "permitir", "dentro da tabela"


def registrar(entrada, decisao, motivo):
    try:
        d = Path(tempfile.gettempdir()) / "sot-roteador"
        d.mkdir(parents=True, exist_ok=True)
        with open(d / "uso.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"t": int(time.time()), "tipo": entrada.get("subagent_type"), "model": entrada.get("model"),
                                "effort": entrada.get("effort"), "decisao": decisao, "motivo": motivo}, ensure_ascii=False) + "\n")
    except OSError:
        pass


def main():
    try:
        ev = json.loads(sys.stdin.read() or "{}")
        if ev.get("tool_name") not in (None, "Agent", "Task"):
            return 0
        entrada = ev.get("tool_input") or {}
        decisao, motivo = decidir(entrada)
        registrar(entrada, decisao, motivo)
    except Exception:
        return 0
    if decisao == "negar":
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                 "permissionDecisionReason": "ROTEADOR DE MODELOS (DHR-ROTEAMENTO-003) — " + motivo}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
