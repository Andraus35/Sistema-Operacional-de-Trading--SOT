#!/usr/bin/env python3
"""fato_locais.py — tabela FATO -> LOCAIS e conferência de listas de linhas (proposta P7; informativo).

Problema (retrospectivas SPEC-006/020/048/049; ledger C01 e C07): o mesmo fato (ID, limiar, nome) aparece em vários
locais de um Plan; a correção acerta um e deixa outros, ou a lista de linhas escrita à mão omite ocorrências.
Este detector só LÊ e informa. Detector (ENF-03): não corrige, não decide, não fecha decisão aberta (CONS-01).

Uso:
  python scripts/fato_locais.py <doc.md> <fato> [<fato> ...] [--em <outro.md> ...] [--base <ref-git>]
      tabela fato -> arquivo:linhas (fato literal; prefixo `re:` = expressão regular)
      --base REF  compara com a versão do doc em REF: para cada fato diz quantas linhas com o fato MUDARAM e quantas
                  ficaram IGUAIS (mudou + igual = possível propagação parcial)
  python scripts/fato_locais.py --conferir <lista.md> <doc.md>
      lê tabela markdown `| fato | linhas |` (linhas como `12, 40-42, 77`) e confere contra o doc: linhas OMITIDAS
      (o fato ocorre ali e a lista não tem) e linhas SOBRANDO (a lista cita, mas o fato não ocorre ali)
  --strict   exit 1 se houver omissão, linha sobrando ou propagação parcial (padrão: sempre exit 0 — informativo)
  --json     saída estruturada

Limite honesto: acha ocorrências de TEXTO; não entende sinônimos nem valores reescritos ("90 dias" x "noventa").
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent


def compilar(fato):
    if fato.startswith("re:"):
        return re.compile(fato[3:])
    return re.compile(re.escape(fato))


def ler(path):
    return Path(path).read_text(encoding="utf-8", errors="replace").split("\n")


def ocorrencias(linhas, fato):
    rx = compilar(fato)
    return [i for i, ln in enumerate(linhas, 1) if rx.search(ln)]


def comprimir(nums):
    """[1,2,3,7] -> '1-3, 7'"""
    out, i = [], 0
    nums = sorted(set(nums))
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if i == j else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ", ".join(out)


def expandir(texto):
    """'12, 40-42, 77' -> {12,40,41,42,77}; ignora lixo."""
    nums = set()
    for parte in re.split(r"[,;\s]+", texto.strip()):
        m = re.fullmatch(r"(\d+)(?:\s*[-–]\s*(\d+))?", parte)
        if not m:
            continue
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        if 0 < a <= b <= a + 100000:
            nums.update(range(a, b + 1))
    return nums


def git_show(ref, path):
    try:
        rel = Path(path).resolve().relative_to(ROOT).as_posix()
        r = subprocess.run(["git", "show", f"{ref}:{rel}"], capture_output=True, text=True, encoding="utf-8",
                           cwd=ROOT, timeout=30)
        return r.stdout.split("\n") if r.returncode == 0 else None
    except Exception:
        return None


def tabela(docs, fatos, base=None):
    """-> lista de dicts {fato, arquivo, linhas, parcial?}"""
    res = []
    for fato in fatos:
        for d in docs:
            linhas = ler(d)
            occ = ocorrencias(linhas, fato)
            item = {"fato": fato, "arquivo": str(d), "linhas": occ}
            if base and Path(d) == Path(docs[0]):
                antigo = git_show(base, d)
                if antigo is None:
                    item["base"] = "indisponivel"
                else:
                    ant = {a.strip() for a in antigo}
                    mudou = [n for n in occ if linhas[n - 1].strip() not in ant]
                    igual = [n for n in occ if linhas[n - 1].strip() in ant]
                    item.update(mudou=mudou, igual=igual, parcial=bool(mudou and igual))
            res.append(item)
    return res


def conferir(lista, doc):
    """lista: arquivo md com tabela `| fato | linhas |`. -> lista de dicts por fato."""
    linhas_doc = ler(doc)
    out = []
    todas = ler(lista)
    sep = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
    for i, ln in enumerate(todas):
        if not ln.strip().startswith("|") or sep.match(ln):
            continue
        if i + 1 < len(todas) and sep.match(todas[i + 1]):   # linha logo antes do separador = cabeçalho da tabela
            continue
        cel = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cel) < 2:
            continue
        fato, declaradas = cel[0].strip("` "), cel[1]
        if not fato:
            continue
        reais = set(ocorrencias(linhas_doc, fato))
        decl = expandir(declaradas)
        out.append({"fato": fato, "omitidas": sorted(reais - decl), "sobrando": sorted(decl - reais),
                    "reais": sorted(reais), "declaradas": sorted(decl)})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="fato -> locais (informativo)")
    ap.add_argument("args", nargs="*")
    ap.add_argument("--em", nargs="*", default=[])
    ap.add_argument("--base")
    ap.add_argument("--conferir", metavar="LISTA")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    problema = False

    if a.conferir:
        if len(a.args) != 1:
            ap.error("--conferir <lista.md> <doc.md>")
        res = conferir(a.conferir, a.args[0])
        if a.json:
            print(json.dumps(res, ensure_ascii=False, indent=2))
        else:
            print("CONFERÊNCIA lista × documento (informativo — Detector ≠ Gate)")
            for r in res:
                bad = r["omitidas"] or r["sobrando"]
                problema |= bool(bad)
                print(f"- {r['fato']}: {'OK' if not bad else 'DIVERGE'}"
                      + (f" · OMITIDAS {comprimir(r['omitidas'])}" if r["omitidas"] else "")
                      + (f" · SOBRANDO {comprimir(r['sobrando'])}" if r["sobrando"] else ""))
            if not res:
                print("(nenhuma linha de tabela `| fato | linhas |` encontrada)")
    else:
        if len(a.args) < 2:
            ap.error("<doc.md> <fato> [<fato> ...]")
        doc, fatos = a.args[0], a.args[1:]
        res = tabela([doc] + a.em, fatos, a.base)
        if a.json:
            print(json.dumps(res, ensure_ascii=False, indent=2))
        else:
            print("| fato | arquivo | nº | linhas |" + (" mudou/igual |" if a.base else ""))
            print("|---|---|---|---|" + ("---|" if a.base else ""))
            for r in res:
                extra = ""
                if a.base and "mudou" in r:
                    extra = f" {len(r['mudou'])}/{len(r['igual'])}" + (" ⚠ PROPAGAÇÃO PARCIAL?" if r["parcial"] else "") + " |"
                    problema |= r["parcial"]
                elif a.base:
                    extra = " base indisponível |"
                print(f"| `{r['fato']}` | {r['arquivo']} | {len(r['linhas'])} | {comprimir(r['linhas']) or '—'} |{extra}")
    print("\nLEMBRETE: detector informativo. exit 0 ≠ CONFORME ≠ homologação; o Revisor audita, Andraus decide.")
    return 1 if (a.strict and problema) else 0


if __name__ == "__main__":
    sys.exit(main())
