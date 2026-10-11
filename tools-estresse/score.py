"""Confere as respostas do Revisor e do Auditor contra o gabarito (key.json).

Cada resposta e tratada como texto (JSON ou texto livre): um defeito conta como
ACHADO se a resposta citar "arquivo:linha" a ate --tol linhas dele, ou citar o
trecho defeituoso literal. Isca limpa tocada = possivel falso alarme.

O relatorio na tela traz so numeros agregados (nao revela o gabarito).
O detalhe vai para --detail (arquivo que so Andraus abre).

Uso:
  python score.py --key key.json --run revisor1=r1.txt --run revisor2=r2.txt --run revisor3=r3.txt \
                  --run auditor1=a1.json --run auditor2=a2.json --run auditor3=a3.json --detail detalhe.json
"""
import argparse, json, re
from collections import defaultdict
from pathlib import Path


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def touched(rec, blob, tol, refs):
    """True se a resposta cita o item por trecho literal ou por arquivo:linha."""
    # trechos curtos ("8", "NEUTRO", "v1.0") aparecem em qualquer lugar: so contam por arquivo:linha
    lits = [rec["bad"], rec["ok"]]
    if any(len(norm(t)) >= 12 and norm(t) in blob for t in lits):
        return True
    return any(f == rec["file"].lower() and lo - tol <= rec["line"] <= hi + tol for f, lo, hi in refs)


def refs_of(raw):
    """Citacoes arquivo+linhas: texto livre (arq.md:12 ou 12-14) e JSON do auditor (evidence[].path/line_start/line_end)."""
    out = []
    for m in re.finditer(r"(spec-ex-[abc]\.md)\W{0,3}(?:linhas?|l\.?|line)?\s*[:#]?\s*(\d+)(?:\s*[-–]\s*(\d+))?", raw, re.I):
        lo = int(m.group(2))
        out.append((m.group(1).lower(), lo, int(m.group(3) or lo)))
    try:
        data = json.loads(raw)
    except ValueError:
        return out
    stack = [data]
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            p, ls = x.get("path") or x.get("file"), x.get("line_start", x.get("line"))
            if isinstance(p, str) and isinstance(ls, int):
                out.append((Path(p).name.lower(), ls, x.get("line_end") if isinstance(x.get("line_end"), int) else ls))
            stack.extend(x.values())
        elif isinstance(x, list):
            stack.extend(x)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True)
    ap.add_argument("--run", action="append", required=True, help="rotulo=arquivo")
    ap.add_argument("--tol", type=int, default=0)
    ap.add_argument("--detail")
    a = ap.parse_args()
    key = json.loads(Path(a.key).read_text(encoding="utf-8"))
    D, C = key["defects"], key["decoys"]
    found, falsa = {}, {}
    for r in a.run:
        label, path = r.split("=", 1)
        raw = Path(path).read_text(encoding="utf-8")
        blob = norm(raw)
        refs = refs_of(raw)
        found[label] = {d["id"] for d in D if touched(d, blob, a.tol, refs)}
        falsa[label] = {c["id"] for c in C if touched(c, blob, a.tol, refs)}
    cls = defaultdict(int)
    for d in D:
        cls[d["class"]] += 1
    groups = defaultdict(list)
    for label in found:
        groups[re.sub(r"\d+$", "", label)].append(label)
    print(f"Gabarito: {len(D)} defeitos ({sum(d['origem']=='andraus' for d in D)} de Andraus), {len(C)} iscas limpas")
    for label in found:
        by = defaultdict(int)
        for d in D:
            if d["id"] in found[label]:
                by[d["class"]] += 1
        parts = ", ".join(f"{k} {by[k]}/{cls[k]}" for k in sorted(cls))
        print(f"{label}: {len(found[label])}/{len(D)} defeitos ({parts}) | iscas tocadas: {len(falsa[label])}/{len(C)}")
    union = {g: set().union(*(found[l] for l in ls)) for g, ls in groups.items()}
    for g, u in union.items():
        print(f"{g} (uniao das rodadas): {len(u)}/{len(D)}")
    gs = sorted(union)
    if len(gs) == 2:
        x, y = gs
        print(f"Valor marginal: {y} acha {len(union[y]-union[x])} que {x} nao achou; {x} acha {len(union[x]-union[y])} que {y} nao achou; ambos {len(union[x]&union[y])}; nenhum {len(D)-len(union[x]|union[y])}")
    if a.detail:
        det = {"defeitos": [{**d, "achado_por": [l for l in found if d["id"] in found[l]]} for d in D],
               "iscas_tocadas": [{**c, "tocada_por": [l for l in falsa if c["id"] in falsa[l]]} for c in C if any(c["id"] in falsa[l] for l in falsa)]}
        Path(a.detail).write_text(json.dumps(det, ensure_ascii=False, indent=1), encoding="utf-8")
        print("Detalhe gravado em", a.detail, "(so Andraus abre)")


if __name__ == "__main__":
    main()
