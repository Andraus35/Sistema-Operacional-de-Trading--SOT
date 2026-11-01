#!/usr/bin/env python3
"""lint_autoprecheck.py — P-B: Autopré-check legível por máquina (PROPOSTA; não instalado; informativo).

O autor/Orquestrador preenche `specs/features/<SPEC>/autoprecheck.md`: tabela `| AP-xx | [x] | evidência |`.
  - item tipo D  : `[x]` exige evidência `PE:<id>[,<id>]` com os ids do catálogo; confere no pre-entrega.json (status OK; achado
                   informativo exige `justificado: <texto>=15+ chars`; bloqueante vermelho = reprova).
  - item ATESTADO: `[x]` exige âncora `arquivo:linha «trecho literal»` (trecho >= ancora_min_chars) que o script confere na linha.
  - `N/A` exige `motivo: ...` (15+ chars) e só vale se o item não se aplica ao contexto.
  - `[ ]` ou item do catálogo ausente = reprova. pre-entrega.json com plan_sha256 diferente do plan.md atual = reprova.
Detector ≠ Gate (ENF-03): confere FORMA e ÂNCORA, nunca o sentido. Um ATESTADO bem ancorado continua sendo auto-atestação; o
ganho é dizer ao Revisor ONDE ele tem de olhar. Somente leitura (escreve só com --template --out).

Uso: python lint_autoprecheck.py specs/features/SPEC-nnn [--pre-entrega pre-entrega.json] [--contexto abertura,trading,especialidade,alta]
     python lint_autoprecheck.py specs/features/SPEC-nnn --template --pre-entrega pre-entrega.json [--contexto ...] [--out autoprecheck.md]
"""
import argparse, hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAT = json.loads((HERE / "autoprecheck_catalogo.json").read_text(encoding="utf-8"))
LINHA = re.compile(r"^\s*\|\s*(AP-[A-Z0-9]+)\s*\|\s*(\[x\]|\[ \]|N/A)\s*\|\s*(.*?)\s*\|?\s*$")
ANCORA = re.compile(r"(?P<arq>[\w./\\-]+\.\w+):(?P<ln>\d+)\s*[«\"“](?P<tr>.+?)[»\"”]", re.S)


def aplica(item, ctx):
    return item["aplica"] == "sempre" or item["aplica"] in ctx


def _pe_status(pe, pid):
    for v in pe.get("verificacoes", []):
        if v["id"] == pid:
            return v
    return None


def conferir(spec_dir, root, ctx, pe):
    probs, sd = [], Path(spec_dir)
    arq = root / sd / "autoprecheck.md"
    if not arq.exists():
        return [f"autoprecheck.md ausente em {sd} (nenhum item do Autopré-check tem rastro)"]
    linhas = {}
    for ln in arq.read_text(encoding="utf-8").splitlines():
        m = LINHA.match(ln)
        if m:
            linhas[m.group(1)] = (m.group(2), m.group(3))
    plan = root / sd / "plan.md"
    if pe is not None and plan.exists():
        if pe.get("plan_sha256") != hashlib.sha256(plan.read_bytes()).hexdigest():
            probs.append("pre-entrega.json é de outra versão do plan.md (plan_sha256 diverge) — rode o pré-gate de novo")
    for it in CAT["itens"]:
        i = it["id"]
        if i not in linhas:
            if aplica(it, ctx): probs.append(f"{i}: item do catálogo ausente do autoprecheck.md")
            continue
        est, ev = linhas[i]
        if est == "N/A":
            if aplica(it, ctx): probs.append(f"{i}: marcado N/A mas se aplica ao contexto {sorted(ctx)}")
            elif not re.search(r"motivo:\s*\S.{14,}", ev): probs.append(f"{i}: N/A sem `motivo:` de 15+ caracteres")
            continue
        if est == "[ ]":
            probs.append(f"{i}: não marcado ([ ]) — {it['texto'][:60]}"); continue
        if it["tipo"] == "D":
            ids = re.findall(r"PE:([\w.,]+)", ev); ids = [x for g in ids for x in g.split(",") if x]
            if not ids: probs.append(f"{i}: item D [x] sem evidência `PE:<id>`"); continue
            for need in it["pe"]:
                if need not in ids: probs.append(f"{i}: evidência não cita `{need}` (exigido pelo catálogo)")
            if pe is not None:
                for pid in ids:
                    v = _pe_status(pe, pid)
                    if v is None: probs.append(f"{i}: `{pid}` não consta do pre-entrega.json")
                    elif v["tipo"] == "bloqueante" and v["status"] != "OK": probs.append(f"{i}: `{pid}` bloqueante VERMELHO")
                    elif v["status"] not in ("OK",) and not re.search(r"justificado:\s*\S.{14,}", ev):
                        probs.append(f"{i}: `{pid}` com achado ({v['status']}) sem `justificado:` de 15+ caracteres")
        else:
            m = ANCORA.search(ev)
            if not m: probs.append(f"{i}: ATESTADO [x] sem âncora `arquivo:linha «trecho»`"); continue
            tr = " ".join(m.group("tr").split())
            if len(tr) < CAT["ancora_min_chars"]: probs.append(f"{i}: trecho da âncora com {len(tr)} < {CAT['ancora_min_chars']} caracteres"); continue
            alvo = root / m.group("arq")
            if not alvo.exists(): probs.append(f"{i}: âncora aponta arquivo inexistente {m.group('arq')}"); continue
            L = alvo.read_text(encoding="utf-8", errors="replace").splitlines(); n = int(m.group("ln"))
            if n < 1 or n > len(L) or tr not in " ".join(L[n - 1].split()):
                probs.append(f"{i}: trecho não consta (literalmente) em {m.group('arq')}:{n}")
    return probs


def template(spec_dir, ctx, pe):
    out = ["# Autopré-check (rascunho gerado; preencha as âncoras dos itens ATESTADO)", "", "| item | estado | evidência |", "|---|---|---|"]
    for it in CAT["itens"]:
        if not aplica(it, ctx):
            out.append(f"| {it['id']} | N/A | motivo: fora do contexto {it['aplica']} |"); continue
        if it["tipo"] == "D":
            ok = pe is not None and all((_pe_status(pe, p) or {}).get("status") == "OK" for p in it["pe"])
            out.append(f"| {it['id']} | {'[x]' if ok else '[ ]'} | PE:{','.join(it['pe'])} |")
        else:
            out.append(f"| {it['id']} | [ ] | arquivo:linha «trecho literal >= {CAT['ancora_min_chars']} caracteres» — {it['texto'][:50]} |")
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("spec_dir"); ap.add_argument("--root", default=str(HERE.parents[3]))
    ap.add_argument("--pre-entrega"); ap.add_argument("--contexto", default=""); ap.add_argument("--template", action="store_true"); ap.add_argument("--out")
    a = ap.parse_args(argv); root = Path(a.root); ctx = {c for c in a.contexto.split(",") if c}
    pe = json.loads(Path(a.pre_entrega).read_text(encoding="utf-8")) if a.pre_entrega else None
    if a.template:
        t = template(a.spec_dir, ctx, pe)
        (Path(a.out).write_text(t, encoding="utf-8") if a.out else print(t)); return 0
    probs = conferir(a.spec_dir, root, ctx, pe)
    for p in probs: print("RED", p)
    print(f"{len(probs)} problema(s). Detector (ENF-03): confere forma e âncora, não o sentido. exit 0 ≠ CONFORME ≠ homologação.")
    return 1 if probs else 0


if __name__ == "__main__":
    sys.exit(main())
