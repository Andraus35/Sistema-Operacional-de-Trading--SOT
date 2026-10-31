#!/usr/bin/env python3
"""
equiv_conservacao.py — prova de conservação ao enxugar um documento quente (PROPOSTA; não instalado).

Regra: toda linha NÃO VAZIA do ORIGINAL deve existir (texto normalizado, multiconjunto) no ENXUTO ou no ARQUIVO MORTO.
Linhas novas no enxuto/arquivo são permitidas (ponteiros). Detector (ENF-03): não decide o que pode ser enxugado.
Uso: equiv_conservacao.py <original> <enxuto> <arquivo_morto> [--json]
Saída: exit 0 = conservado; exit 1 = linhas perdidas (lista com a linha mais parecida, para pegar número alterado).
"""
import difflib
import re
import sys
from collections import Counter
from pathlib import Path


def norm(l):
    return re.sub(r"\s+", " ", l.replace("\r", "")).strip()


def linhas(p):
    return [norm(l) for l in Path(p).read_text(encoding="utf-8").split("\n") if norm(l)]


def verificar(original, enxuto, morto):
    pool = Counter(linhas(enxuto)) + Counter(linhas(morto))
    perdidas = []
    for l in linhas(original):
        if pool[l] > 0:
            pool[l] -= 1
        else:
            perdidas.append(l)
    cands = list(pool.elements())
    out = []
    for l in perdidas:
        m = difflib.get_close_matches(l, cands, n=1, cutoff=0.8) if len(l) < 3000 else []
        out.append((l, m[0] if m else None))
    return out


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    perdidas = verificar(*argv[1:4])
    if not perdidas:
        print("CONSERVADO: toda linha do original existe no enxuto ou no arquivo morto.")
        return 0
    print(f"PERDA: {len(perdidas)} linha(s) do original ausente(s):")
    for l, m in perdidas[:20]:
        print("  -", l[:140] + ("…" if len(l) > 140 else ""))
        if m:
            print("    parecida (valor alterado?):", m[:140] + ("…" if len(m) > 140 else ""))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
