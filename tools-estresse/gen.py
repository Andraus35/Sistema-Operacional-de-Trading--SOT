"""Gerador do teste de estresse (Auditor Externo x Revisor interno).

Cada <<ID|correto|defeituoso>> em base/*.md e um "slot". Para cada documento, a
SEMENTE secreta sorteia quais slots recebem a versao defeituosa; os demais ficam
corretos e funcionam como iscas limpas. Defeitos extras de Andraus entram por
--extra (JSON) e ficam no gabarito marcados origem=andraus.

Uso:
  python gen.py --clean --out limpo                      # tudo correto (para Andraus escrever os extras)
  python gen.py --seed <segredo> --out saida --key key.json [--extra extras.json] [--n 10]
"""
import argparse, hashlib, json, random, re, sys
from pathlib import Path

SLOT = re.compile(r"<<([A-Z]+-\d+)\|([^|]*?)\|([^|]*?)>>")
HERE = Path(__file__).parent


def render(text, bad_ids):
    out, pos, slots = [], 0, []
    cur = 0
    for m in SLOT.finditer(text):
        out.append(text[pos:m.start()])
        cur += len(text[pos:m.start()])
        sid, ok, bad = m.group(1), m.group(2), m.group(3)
        use_bad = sid in bad_ids
        chosen = bad if use_bad else ok
        slots.append({"id": sid, "class": sid.split("-")[0], "ok": ok, "bad": bad,
                      "defect": use_bad, "start": cur, "text": chosen})
        out.append(chosen)
        cur += len(chosen)
        pos = m.end()
    out.append(text[pos:])
    rendered = "".join(out)
    for s in slots:
        s["line"] = rendered.count("\n", 0, s["start"]) + 1
    return rendered, slots


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed")
    ap.add_argument("--clean", action="store_true")
    ap.add_argument("--out", required=True)
    ap.add_argument("--key", default="key.json")
    ap.add_argument("--extra")
    ap.add_argument("--n", type=int, default=10, help="defeitos de slot por documento")
    a = ap.parse_args()
    if not a.clean and not a.seed:
        sys.exit("informe --seed (ou --clean)")
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    key = {"defects": [], "decoys": []}
    rendered_docs = {}
    for f in sorted((HERE / "base").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        ids = [m.group(1) for m in SLOT.finditer(text)]
        bad = set()
        if not a.clean:
            bad = set(random.Random(f"{a.seed}:{f.name}").sample(ids, min(a.n, len(ids))))
        rendered_docs[f.name], slots = render(text, bad)
        for s in slots:
            rec = {"id": s["id"], "class": s["class"], "file": f.name, "line": s["line"],
                   "ok": s["ok"], "bad": s["bad"], "origem": "gerador"}
            (key["defects"] if s["defect"] else key["decoys"]).append(rec)
    if a.extra:
        for e in json.loads(Path(a.extra).read_text(encoding="utf-8")):
            doc = rendered_docs[e["file"]]
            if "\n" in e["replace"] or doc.count(e["find"]) != 1:
                sys.exit(f"extra {e['id']}: 'find' deve ocorrer exatamente 1 vez e 'replace' nao pode ter quebra de linha")
            i = doc.index(e["find"])
            rendered_docs[e["file"]] = doc[:i] + e["replace"] + doc[i + len(e["find"]):]
            line = rendered_docs[e["file"]].count("\n", 0, i) + 1
            key["defects"].append({"id": e["id"], "class": e.get("class", "SEM"), "file": e["file"],
                                   "line": line, "ok": e["find"], "bad": e["replace"], "origem": "andraus"})
    for name, doc in rendered_docs.items():
        (out / name).write_text(doc, encoding="utf-8", newline="\n")
    if not a.clean:
        kp = Path(a.key)
        kp.write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf-8")
        print("defeitos:", len(key["defects"]), "| iscas limpas:", len(key["decoys"]))
        print("sha256 do gabarito:", hashlib.sha256(kp.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
