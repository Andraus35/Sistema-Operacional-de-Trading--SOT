#!/usr/bin/env python3
"""historico_do_diff.py — tabela "texto anterior" do HISTORICO.md gerada do diff git entre duas versões (proposta P14(b); Detector/gerador).

Problema (retrospectiva SPEC-008; ledger C06): o histórico `[antes]` copiado à mão infla o plan e falha (no Plan da SPEC-008, o R2-m10
achou o HISTORICO incompleto e a recuperação precisou do `git diff`). O agente NÃO escreve o texto anterior à mão: o Orquestrador roda
este script e cola a tabela; o Especificador só preenche a coluna "Motivo". Somente leitura (só escreve o --out, se dado).
Não decide o que é achado: lista TODA linha removida/trocada, ancorada ao bloco (cabeçalho `##…####` ou definição `RULE-/INV-…:`).

Uso:
  python scripts/historico_do_diff.py <plan.md> --base <git-ref|arquivo> [--out HISTORICO-trecho.md] [--max 700] [--json]
Saída: tabela markdown `| Local | Texto anterior | Texto novo | Motivo |` (Motivo = `(preencher)`), um linha por trecho trocado ou removido,
mais um resumo (n trechos; n linhas removidas). `--max` limita o texto por célula (0 = sem truncar; truncado leva marca `[…truncado; ver git]`).
Detector (ENF-03): não corrige nem fecha decisão (CONS-01). Limite: granularidade de linha; reflow de parágrafo aparece como troca.
"""
import argparse
import difflib
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
_HEAD = re.compile(r"^(#{2,4})\s+(.*?)\s*$")
_DEF = re.compile(r"^[\s>*|`-]*\**((?:RULE|INV)-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*)\**\s*:")


def ler_base(base, alvo):
    p = Path(base)
    if p.is_file():
        return p.read_text(encoding="utf-8", errors="replace")
    r = subprocess.run(["git", "show", f"{base}:{Path(alvo).as_posix()}"], cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit(f"base ilegível: {base} ({r.stderr.strip()[:200]})")
    return r.stdout


def ancoras(linhas):
    """Para cada índice de linha, o rótulo do bloco (última definição RULE/INV ou cabeçalho até ali)."""
    cur, out = "cabeçalho", []
    for ln in linhas:
        m = _HEAD.match(ln)
        if m:
            cur = m.group(2)[:80]
        else:
            d = _DEF.match(ln)
            if d:
                cur = d.group(1)
        out.append(cur)
    return out


def _cel(txt, mx):
    t = " ⏎ ".join(x.strip() for x in txt if x.strip()).replace("|", "\\|")
    if mx and len(t) > mx:
        t = t[:mx].rstrip() + " […truncado; ver git]"
    return t or "—"


def trechos(base_txt, novo_txt, mx=700):
    a, b = base_txt.splitlines(), novo_txt.splitlines()
    anc_a, anc_b = ancoras(a), ancoras(b)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op in ("replace", "delete"):
            local = anc_a[i1] if i1 < len(anc_a) else "fim"
            out.append({"local": local, "linhas_base": f"{i1 + 1}-{i2}", "removidas": i2 - i1,
                        "anterior": _cel(a[i1:i2], mx), "novo": _cel(b[j1:j2], mx) if op == "replace" else "(removido)"})
    return out


def tabela(ts):
    ls = ["| Local | Texto anterior (base) | Texto novo | Motivo |", "|---|---|---|---|"]
    for t in ts:
        ls.append(f"| {t['local']} (l. base {t['linhas_base']}) | {t['anterior']} | {t['novo']} | (preencher) |")
    return "\n".join(ls) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("alvo")
    ap.add_argument("--base", required=True)
    ap.add_argument("--out")
    ap.add_argument("--max", type=int, default=700)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    novo = Path(a.alvo).read_text(encoding="utf-8", errors="replace")
    ts = trechos(ler_base(a.base, a.alvo), novo, a.max)
    n = sum(t["removidas"] for t in ts)
    if a.json:
        print(json.dumps(ts, ensure_ascii=False, indent=2))
        return 0
    corpo = tabela(ts)
    if a.out:
        Path(a.out).write_text(corpo, encoding="utf-8")
    print(corpo)
    print(f"resumo: {len(ts)} trecho(s) trocado(s)/removido(s); {n} linha(s) removida(s)/trocada(s) da base (Detector; o Motivo é do Especificador).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
