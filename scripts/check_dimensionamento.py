#!/usr/bin/env python3
"""
check_dimensionamento.py — detectores INFORMATIVOS de dimensionamento de Spec e de delta por hash (DHR-CHECKS-INFO-001).

1. RULE-ECC-07 (DHR-DIMENSIONAMENTO-001): linhas do CORPO normativo do plan.md (antes do primeiro `## Anexo`) vs. tetos
   (confirmação > 1.600 · alerta 1.900 · teto 2.000). Prospectiva desde a SPEC-049: Specs anteriores são só INFO (histórico).
2. DHR-DELTA-HASH-001: parecer do Revisor de data >= 2026-11-01, rodada >= 2 e por delta, sem `SHA256-ALVO:` declarado = WARN.

Somente leitura. Detector ≠ Gate (ENF-03): exit 0 sempre; nunca bloqueia, nunca decide, nunca homologa. Quem julga é o Revisor,
quem decide é Andraus. Promoção a bloqueante só por ordem de Andraus.

Uso:
    python scripts/check_dimensionamento.py            # todas as Specs e pareceres
    python scripts/check_dimensionamento.py --root DIR # raiz alternativa (testes)
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import loop_ledger  # noqa: E402

CONFIRMA, ALERTA, TETO = 1600, 1900, 2000
PRIMEIRA_SPEC_PROSPECTIVA = 49
DATA_DELTA_HASH = "2026-11-01"  # a regra foi decidida em 2026-10-31; pareceres desse dia são anteriores a ela


def classificar(corpo, numero):
    """(nivel, texto). Nível INFO para Spec anterior à vigência; WARN só quando aplicável."""
    if numero < PRIMEIRA_SPEC_PROSPECTIVA:
        return "INFO", f"corpo {corpo} linhas (histórico; RULE-ECC-07 vale desde a SPEC-{PRIMEIRA_SPEC_PROSPECTIVA:03d})"
    if corpo > TETO:
        return "WARN", f"corpo {corpo} > teto {TETO}: divisão deve ser proposta a Andraus ANTES do Plan"
    if corpo > ALERTA:
        return "WARN", f"corpo {corpo} > alerta {ALERTA} (teto {TETO})"
    if corpo > CONFIRMA:
        return "INFO", f"corpo {corpo} > {CONFIRMA}: confirmar a decomposição com Andraus antes do Plan"
    return "OK", f"corpo {corpo} linhas"


def checar_planos(root):
    achados = []
    for plan in sorted((Path(root) / "specs" / "features").glob("SPEC-*/plan.md")):
        spec = plan.parent.name
        n = int(re.search(r"(\d+)", spec).group(1))
        t = loop_ledger.tamanho_plan(root, spec)
        if not t:
            continue
        nivel, txt = classificar(t[1], n)
        achados.append((nivel, spec, txt))
    return achados


def checar_hash(root):
    achados = []
    for f in sorted((Path(root) / "governance").rglob("PARECER*.md")):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", f.name)
        if not m or m.group(1) < DATA_DELTA_HASH:
            continue
        _, rodada = loop_ledger.linha_trabalho(f.relative_to(root))
        modo, sha, _ = loop_ledger.metadados_rodada(f.read_text(encoding="utf-8", errors="replace"))
        if rodada >= 2 and modo.startswith("delta") and sha in ("ausente", "não conferido"):
            achados.append(("WARN", f.name, f"rodada R{rodada} por delta sem SHA256-ALVO declarado (revisor.md §3-bis item 7)"))
    return achados


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--root", default=str(ROOT))
    a = ap.parse_args(argv)
    achados = checar_planos(a.root) + checar_hash(a.root)
    print("=" * 60)
    print("DIMENSIONAMENTO / DELTA POR HASH — detectores informativos")
    print("=" * 60)
    for nivel, alvo, txt in achados:
        print(f"[{nivel}] {alvo} — {txt}")
    w = sum(1 for x in achados if x[0] == "WARN")
    print("-" * 60)
    print(f"ERRO=0 WARN={w} INFO={sum(1 for x in achados if x[0] == 'INFO')} OK={sum(1 for x in achados if x[0] == 'OK')}")
    print("Somente leitura — Detector (ENF-03): não bloqueia, não decide.")
    print("LEMBRETE: exit 0 ≠ CONFORME ≠ homologação.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
