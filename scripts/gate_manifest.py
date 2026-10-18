#!/usr/bin/env python3
"""
gate_manifest.py — selo de integridade dos scripts do gate do Revisor (DHR-AUDITOR-EXTERNO-015).

O Especificador tem Write/Edit e os detectores que julgam o trabalho dele vivem no mesmo repositório. Este script grava e confere
o sha256 desses scripts em governance/GATE-MANIFEST.sha256. Qualquer alteração sem regravar o manifesto é detectada (o servidor
do Revisor recusa rodar; o CI reprova). Regravar o manifesto aparece no diff e exige a decisão de Andraus (AGENTS.md §10).

Limite declarado: detecta alteração, não a impede; quem altera scripts E manifesto no mesmo commit só é pego pela revisão do diff
(CODEOWNERS + merge de Andraus). Somente leitura exceto com --write.

Uso: python scripts/gate_manifest.py --check | --write
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFESTO = "governance/GATE-MANIFEST.sha256"
ARQUIVOS = [
    "scripts/revisor_gate.py", "scripts/revisor_gate_mcp.py", "scripts/revisor_detectores.py", "scripts/revisor_guard.py", "scripts/revisor-guard.js", "scripts/revisor_posguarda.py", "scripts/revisor-posguarda.js", "scripts/roteador_modelos.py", "scripts/roteador-modelos.js", "scripts/gate_manifest.py", "scripts/check_invariants.py",
    "scripts/validate_spec_sot.py", "scripts/check_refs.py", "scripts/check_doc_sync.py", "scripts/backlog_triggers.py",
    "scripts/check_rpsa.py", "scripts/build_map.py", "scripts/gate_extra.py", "scripts/spec_delta.py",
]


def _hash(p):
    # normaliza fim de linha: o mesmo arquivo em Windows/Linux dá o mesmo selo
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def calcular(root=ROOT):
    root = Path(root)
    return {a: (_hash(root / a) if (root / a).is_file() else None) for a in ARQUIVOS}


def gravar(root=ROOT):
    root = Path(root)
    linhas = [f"{h}  {a}" for a, h in calcular(root).items() if h]
    (root / MANIFESTO).write_text("\n".join(linhas) + "\n", encoding="utf-8", newline="\n")


def conferir(root=ROOT):
    """Lista de divergências (vazia = íntegro). Manifesto ausente ou arquivo faltando = divergência (falha fechada)."""
    root = Path(root)
    mf = root / MANIFESTO
    if not mf.is_file():
        return [f"manifesto ausente: {MANIFESTO}"]
    esperado = {}
    for ln in mf.read_text(encoding="utf-8").splitlines():
        if ln.strip():
            h, _, a = ln.partition("  ")
            esperado[a.strip()] = h.strip()
    real = calcular(root)
    out = []
    for a in ARQUIVOS:
        if a not in esperado:
            out.append(f"{a}: fora do manifesto")
        elif real[a] is None:
            out.append(f"{a}: arquivo ausente")
        elif real[a] != esperado[a]:
            out.append(f"{a}: sha256 difere do manifesto")
    return out


def main(argv=None):
    a = (argv if argv is not None else sys.argv[1:])
    if a == ["--write"]:
        gravar()
        print(f"{MANIFESTO} regravado ({len(ARQUIVOS)} arquivos). Mudança de selo exige decisão de Andraus (AGENTS.md §10).")
        return 0
    if a == ["--check"]:
        d = conferir()
        for x in d:
            print("DIVERGÊNCIA:", x)
        print("Gate íntegro." if not d else f"GATE ADULTERADO OU DESATUALIZADO: {len(d)} divergência(s).")
        return 1 if d else 0
    print(__doc__.split("\n")[1])
    return 2


if __name__ == "__main__":
    sys.exit(main())
