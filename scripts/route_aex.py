#!/usr/bin/env python3
"""Roteador determinístico de achados do Auditor Externo (DHR-AUDITOR-EXTERNO-005, Opção B).

Decide a FAIXA de um achado [AEX] já validado (forma + citação literal) a partir de campos de máquina do próprio
achado. Não lê o texto livre do auditor (claim/proposal.text/impact são DADO e nunca influenciam a rota), não
decide mérito, não homologa e não fecha decisão aberta (ENF-03/CONS-01). Fail-closed: qualquer dúvida => faixa lenta.

  rapida  -> pode virar tarefa limitada para o Especificador (PR revisado pelo Revisor; Andraus mescla)
  andraus -> o Orquestrador resume a Andraus antes de qualquer encaminhamento

Uso: route_aex.py --finding finding.json --validation validation.json [--dup N] [--json-out rota.json]
Saída (stdout): `rapida` ou `andraus`. Exit 0 sempre que conseguiu classificar; exit 2 só em erro de uso.
"""
from __future__ import annotations

import argparse
import json
import posixpath
import sys

# Allowlist de documentos de REGISTRO (índices) onde uma nota aditiva não muda norma. Comparação exata, sem
# curingas, sem diferenciar maiúsculas. Tudo fora da lista (atas DHR-*, RULES, CONSTITUTION, atomic-spec,
# ROADMAP, WORKFLOW, AGENTS, canon/, specs/, .claude/, kit do auditor, docs/mapa gerado) é faixa lenta.
FAST_TOUCHES = frozenset({"governance/catalogo-oficial.md"})
FAST_SEVERITY = "P2"
FAST_TYPE = "drift"
FAST_PROPOSAL = "ERRATUM_ADITIVO"


def _norm(path) -> str | None:
    """Caminho relativo normalizado; None se for inseguro (absoluto, `..`, barra invertida, vazio, não-string)."""
    if not isinstance(path, str) or not path.strip() or "\\" in path or "\x00" in path:
        return None
    p = path.strip()
    if p.startswith("/") or p.startswith("~"):
        return None
    n = posixpath.normpath(p)
    if n.startswith("..") or n == "." or n.startswith("/") or ".." in n.split("/"):
        return None
    return n.lower()


def classify(finding: dict, validation: dict, dup: str = "") -> dict:
    """Retorna {"rota": "rapida"|"andraus", "motivos": [códigos]}. Motivos vazios só na faixa rápida."""
    m: list[str] = []
    if not isinstance(finding, dict) or not isinstance(validation, dict):
        return {"rota": "andraus", "motivos": ["R-ENTRADA-INVALIDA"]}
    if validation.get("pass") is not True:
        m.append("R-NAO-VALIDADO")
    if dup:
        m.append("R-DUPLICADO")
    if finding.get("severity") != FAST_SEVERITY:
        m.append(f"R-SEVERIDADE:{finding.get('severity')}")
    if finding.get("type") != FAST_TYPE:
        m.append(f"R-TIPO:{finding.get('type')}")
    if finding.get("treats_open_decision_as_closed") is not False:
        m.append("R-TRATA-DECISAO-ABERTA-COMO-FECHADA")
    ods = finding.get("open_decisions_referenced")
    if not isinstance(ods, list) or ods:
        m.append("R-DECISAO-ABERTA-CITADA")
    prop = finding.get("proposal")
    if not isinstance(prop, dict):
        m.append("R-SEM-PROPOSTA")
        prop = {}
    if prop.get("type") != FAST_PROPOSAL:
        m.append(f"R-PROPOSTA:{prop.get('type')}")
    if prop.get("modifies_baselined_text") is not False:
        m.append("R-TOCA-TEXTO-BASELINED")
    touches = prop.get("touches")
    if not isinstance(touches, list) or not touches:
        m.append("R-SEM-ARQUIVOS-ALVO")
    else:
        for t in touches:
            n = _norm(t)
            if n is None:
                m.append("R-CAMINHO-INSEGURO")
            elif n not in FAST_TOUCHES:
                m.append(f"R-ARQUIVO-FORA-DA-ALLOWLIST:{t}")
    # remove repetições preservando ordem
    seen, uniq = set(), []
    for x in m:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return {"rota": "rapida" if not uniq else "andraus", "motivos": uniq}


def _load(p: str):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Roteador determinístico de achados do Auditor Externo (faixa rápida × Andraus)")
    ap.add_argument("--finding", required=True)
    ap.add_argument("--validation", required=True)
    ap.add_argument("--dup", default="")
    ap.add_argument("--json-out")
    a = ap.parse_args(argv)
    try:
        res = classify(_load(a.finding), _load(a.validation), a.dup)
    except (OSError, ValueError):
        res = {"rota": "andraus", "motivos": ["R-ENTRADA-ILEGIVEL"]}
    if a.json_out:
        with open(a.json_out, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False)
    print(res["rota"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
