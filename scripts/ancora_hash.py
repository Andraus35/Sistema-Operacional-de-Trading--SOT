#!/usr/bin/env python3
"""ancora_hash.py — citação por IDENTIFICADOR + hash curto do bloco, em vez de número de linha (proposta P14(a); informativo).

Problema (retrospectiva SPEC-008; ledger C07): citar "plan.md l.473" deriva a cada edição do Plan. A âncora `ID#hhhh` (ex.: `RULE-MDC-005#a1f3`)
não deriva com a posição e ainda denuncia que o TEXTO da regra mudou depois da citação (hhhh = 4 primeiros hex do sha256 do bloco, o MESMO
hash por bloco do `spec_delta.py`). Este detector só LÊ e informa. Detector (ENF-03): não corrige, não decide, não fecha decisão aberta (CONS-01).

Uso:
  python scripts/ancora_hash.py hash <plan.md> <ID> [<ID> ...]        # imprime `ID#hhhh` do bloco ATUAL
  python scripts/ancora_hash.py conferir <doc.md> <plan.md> [--strict] [--json]
      lê as âncoras `ID#hhhh` de <doc.md> e confere com o <plan.md>: OK · DEFASADA (o bloco mudou) · INEXISTENTE (o ID não é bloco do plan)
Chave do bloco: definição `RULE-/INV-…:` (`def:ID`) ou seção `##…####` que começa com o ID (BASpec-/EC-/ADV-/Cenário-).
Limite honesto: o hash cobre o texto do próprio bloco (espaços colapsados); mudança numa regra CITADA por ele não o altera; a âncora diz que
o bloco mudou, não se a citação ainda é válida (isso é do Revisor). Não toca `check_refs.py` (selado): a integração à régua de referências é decisão à parte.
"""
import argparse
import json
import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
import spec_delta  # noqa: E402

ANCORA = re.compile(r"\b((?:RULE|INV)-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*|(?:BASpec|EC|ADV)-[A-Z]+-\d+|Cen[áa]rio-[A-Z]+-T\d+)#([0-9a-f]{4})\b")


def hashes(plan_txt):
    """{ID: hhhh} para todo bloco identificável do plan (def: tem precedência sobre seção)."""
    b = spec_delta.blocos(plan_txt)
    out = {}
    for k, h in b.items():
        if k.startswith("def:"):
            out[k[4:]] = h[:4]
    for k, h in b.items():
        if not k.startswith("def:") and re.match(r"^(?:RULE|INV|BASpec|EC|ADV|Cen[áa]rio)-", k):
            out.setdefault(k.rstrip("'"), h[:4])
    return out


def conferir(doc_txt, plan_txt):
    h = hashes(plan_txt)
    res = []
    for i, ln in enumerate(doc_txt.splitlines(), 1):
        for m in ANCORA.finditer(ln):
            ident, hh = m.group(1), m.group(2)
            atual = h.get(ident)
            st = "INEXISTENTE" if atual is None else ("OK" if atual == hh else "DEFASADA")
            res.append({"linha": i, "id": ident, "hash_citado": hh, "hash_atual": atual, "estado": st})
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    sub = ap.add_subparsers(dest="cmd", required=True)
    a1 = sub.add_parser("hash")
    a1.add_argument("plan")
    a1.add_argument("ids", nargs="+")
    a2 = sub.add_parser("conferir")
    a2.add_argument("doc")
    a2.add_argument("plan")
    a2.add_argument("--strict", action="store_true")
    a2.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    plan = Path(a.plan).read_text(encoding="utf-8", errors="replace")
    if a.cmd == "hash":
        h = hashes(plan)
        rc = 0
        for i in a.ids:
            if i in h:
                print(f"{i}#{h[i]}")
            else:
                print(f"{i}: não é bloco identificável do plan", file=sys.stderr)
                rc = 1
        return rc
    res = conferir(Path(a.doc).read_text(encoding="utf-8", errors="replace"), plan)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        for r in res:
            extra = "" if r["estado"] == "OK" else f" (citado #{r['hash_citado']}, atual #{r['hash_atual']})"
            print(f"L{r['linha']}: {r['id']}#{r['hash_citado']} — {r['estado']}{extra}")
        ruins = [r for r in res if r["estado"] != "OK"]
        print(f"{len(res)} âncora(s); {len(ruins)} defasada(s)/inexistente(s) (Detector informativo; exit 0 ≠ CONFORME ≠ homologação)")
    return 1 if (a.strict and any(r["estado"] != "OK" for r in res)) else 0


if __name__ == "__main__":
    sys.exit(main())
