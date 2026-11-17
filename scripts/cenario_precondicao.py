#!/usr/bin/env python3
"""cenario_precondicao.py — todo cenário de teste cita pré-condição/fixture DECLARADA (proposta P17(b); informativo).

Problema (retrospectivas SPEC-007/008; ledger C03): cenário sem pré-condição, ou que usa um nome de fixture (M0, S1, H1…) que nenhuma seção
declara, não é executável na construção. Este detector só LÊ e informa. Detector (ENF-03): não corrige, não decide, não fecha decisão
aberta (CONS-01).

Uso:
  python scripts/cenario_precondicao.py <plan.md> [--strict] [--json]

Convenção: cenário = seção `### Cenário-…`; a pré-condição é a linha `DADO` (ou `GIVEN`) do bloco; fixture = seção `## Fixture …` do Plan
(nomes como `M0`, `E1`, `S1`, `A1`: letra maiúscula + dígitos, em negrito/crase/texto). Verificações:
  (a) cenário sem linha `DADO`;
  (b) `DADO` vazio ou só com marcação sem nome (informativo);
  (c) `DADO` com nome de fixture (`[A-Z]\\d{1,2}`) NÃO declarado na seção Fixture e NÃO definido no próprio DADO (`X = …`/`X:`);
  (d) Plan com cenários e sem nenhuma seção `## Fixture` (informativo).
`T\\d+` (cenário) e `F\\d+` (linha da D5) são referências, não fixtures. Sem seção Fixture só (d) vale.
Limite honesto: acha NOMES; não entende se o valor da fixture basta para a asserção. Nome só-de-DADO (ex.: `H4`) é aceito se o
DADO o define ("S1 trocado por…" define-se como variação de S1 declarado, não como nome novo).
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

_NOME = re.compile(r"(?<![A-Za-z0-9_])([A-Z]\d{1,2})(?![A-Za-z0-9_])")
_HEAD = re.compile(r"^(#{2,4})\s+(.*?)\s*$")


def secoes(texto):
    out, cur = [], None
    for i, ln in enumerate(texto.splitlines(), 1):
        m = _HEAD.match(ln)
        if m:
            if cur:
                out.append(cur)
            cur = (m.group(1), m.group(2), i, [])
        elif cur:
            cur[3].append(ln)
    if cur:
        out.append(cur)
    return out


def fixtures_declaradas(secs):
    nomes = set()
    for nivel, tit, _i, corpo in secs:
        if tit.lower().startswith("fixture"):
            nomes.update(_NOME.findall(tit))
            nomes.update(_NOME.findall("\n".join(corpo)))
    return nomes


def dado_de(corpo):
    """Texto do DADO (linha `DADO ...` + continuações indentadas até o próximo rótulo)."""
    out, dentro = [], False
    for ln in corpo:
        m = re.match(r"^\s*(DADO|GIVEN)\b\s*(.*)$", ln)
        if m:
            dentro = True
            out.append(m.group(2))
        elif dentro and re.match(r"^\s*(QUANDO|WHEN|ENTÃO|ENTAO|THEN|VERIFICAÇÃO|VERIFICACAO)\b", ln):
            break
        elif dentro and (ln.startswith("```") or not ln.strip()):
            break
        elif dentro:
            out.append(ln.strip())
    return " ".join(out).strip() if dentro else None


def verificar(texto):
    secs = secoes(texto)
    decl = fixtures_declaradas(secs)
    ach, n_cen = [], 0
    for nivel, tit, ini, corpo in secs:
        if not re.match(r"^(Cenário|Cenario)-", tit):
            continue
        n_cen += 1
        nome = tit.split("—")[0].strip()
        dado = dado_de(corpo)
        if dado is None:
            ach.append({"verif": "a", "linha": ini, "msg": f"{nome}: sem linha DADO (pré-condição não declarada)"})
            continue
        if not _NOME.search(dado) and not re.search(r"fixture", dado, re.I) and len(dado) < 6:
            ach.append({"verif": "b", "linha": ini, "msg": f"{nome}: DADO sem nome de fixture nem pré-condição legível ('{dado}')"})
        definidos = set(re.findall(r"(?<![A-Za-z0-9_])([A-Z]\d{1,2})\s*(?:=|:)", dado))
        # T01/F09 = referência a outro cenário / linha da D5, não nome de fixture; sem seção Fixture só vale (d)
        refs = {n for n in _NOME.findall(dado) if n[0] in "TF"}
        for n in sorted(set(_NOME.findall(dado)) - decl - definidos - refs) if decl else []:
            ach.append({"verif": "c", "linha": ini, "msg": f"{nome}: DADO usa `{n}` que nenhuma seção Fixture declara (nem o próprio DADO define)"})
    if n_cen and not decl:
        ach.append({"verif": "d", "linha": 0, "msg": f"{n_cen} cenário(s) e nenhuma seção `## Fixture` com nomes declarados"})
    return {"cenarios": n_cen, "fixtures": sorted(decl), "achados": ach}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("plan")
    ap.add_argument("--strict", action="store_true", help="exit 1 se houver achado (a) ou (c) (padrão: exit 0)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    r = verificar(Path(a.plan).read_text(encoding="utf-8", errors="replace"))
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(f"cenario_precondicao: {r['cenarios']} cenário(s); fixtures declaradas: {', '.join(r['fixtures']) or '—'}")
        for x in r["achados"]:
            print(f"[{x['verif']}] L{x['linha']}: {x['msg']}")
        print(f"achados: {len(r['achados'])} (Detector informativo; exit 0 ≠ CONFORME ≠ homologação)")
    return 1 if (a.strict and any(x["verif"] in ("a", "c") for x in r["achados"])) else 0


if __name__ == "__main__":
    sys.exit(main())
