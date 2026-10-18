#!/usr/bin/env python3
"""
check_branches.py — detector de ramos órfãos (informativo; Detector ≠ Gate, ENF-03; DHR-ROTEAMENTO-003 Emenda 1 / P3 de Andraus).

Compara os ramos remotos (refs/remotes/origin/*) com origin/main:
  BR-01 [WARN] ramo À FRENTE da main (commits próprios) cujo nome NÃO é citado em HANDOFF.md -> trabalho possivelmente esquecido.
  BR-02 [INFO] ramo totalmente contido na main (0 commits próprios) -> apagável (ligar "apagar ramo após o merge" no GitHub).
O ramo atual e a main são ignorados. Somente leitura: nunca apaga ramo, nunca fecha PR. Sem origin/main local, só avisa.
Saída: linhas "[WARN] BR-01 ..." e "ERRO=0 WARN=n INFO=m". Exit 0 sempre (informativo).
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRINCIPAL = "origin/main"


def _git(root, *args):
    r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return r.returncode, r.stdout.strip()


def analisar(root=ROOT, handoff_texto=None):
    """-> (achados[(nivel, id, msg)], aviso|None)."""
    root = Path(root)
    rc, _ = _git(root, "rev-parse", "--verify", "--quiet", PRINCIPAL)
    if rc != 0:
        return [], f"{PRINCIPAL} indisponível localmente (git fetch origin main); nada conferido."
    if handoff_texto is None:
        h = root / "HANDOFF.md"
        handoff_texto = h.read_text(encoding="utf-8") if h.is_file() else ""
    _, atual = _git(root, "rev-parse", "--abbrev-ref", "HEAD")
    _, refs = _git(root, "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin")
    achados = []
    for ref in sorted(r for r in refs.splitlines() if r):
        nome = ref[len("origin/"):] if ref.startswith("origin/") else ref
        if nome in ("HEAD", "main", atual) or ref == "origin":
            continue
        rc, n = _git(root, "rev-list", "--count", f"{PRINCIPAL}..{ref}")
        if rc != 0 or not n.isdigit():
            continue
        if int(n) == 0:
            achados.append(("INFO", "BR-02", f"{nome} — contido na main (0 commits próprios): apagável"))
        elif not re.search(re.escape(nome), handoff_texto):
            achados.append(("WARN", "BR-01", f"{nome} — {n} commit(s) à frente da main e não citado em HANDOFF.md (órfão?)"))
    return achados, None


def main(argv):
    achados, aviso = analisar()
    if aviso:
        print(f"[INFO] BR-00 {aviso}")
    for nivel, ident, msg in achados:
        print(f"[{nivel}] {ident} {msg}")
    print("-" * 60)
    print(f"ERRO=0 WARN={sum(a[0] == 'WARN' for a in achados)} INFO={sum(a[0] == 'INFO' for a in achados)}")
    print("Somente leitura — Detector (ENF-03): não apaga ramo nem fecha PR.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
