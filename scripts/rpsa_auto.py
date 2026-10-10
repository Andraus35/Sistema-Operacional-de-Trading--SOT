#!/usr/bin/env python3
"""rpsa_auto.py — registro AUTOMÁTICO da classificação RPSA após a aprovação de Andraus (DHR-RPSA-002).

Problema: o livro-razão RPSA (`governance/rpsa-ledger.json`) exige que cada DHR nova seja classificada (em escopo dos
agentes ou não; EUA-E16 §4.1). Até aqui a classificação era uma inferência do Orquestrador "a ratificar por Andraus",
o que gerava uma rodada manual extra a cada ata.

Solução: a **própria ata declara** a classificação em linhas da tabela de cabeçalho; o **merge da ata por Andraus é a
ratificação**. Após o merge, este script registra a declaração no livro-razão — sem julgar mérito. O julgamento de
escopo continua sendo da ata (humano/Orquestrador, aprovado por Andraus); o código só (a) lê a declaração, (b) valida a
forma, (c) BARRA contradições óbvias com os arquivos que o próprio merge alterou e (d) registra, de forma idempotente.

Linhas na tabela de cabeçalho da ata (uma célula por linha):
  | RPSA-escopo | sim ou nao |
  | RPSA-sync   | fonte-unica | propagado | pendente |
  | RPSA-motivo | justificativa (>= 20 caracteres) |

Estados por DHR ainda não classificada:
  registrar          declaração válida e sem contradição -> será registrada (com --apply)
  sem-declaracao     ata sem as linhas RPSA-* -> segue NÃO CLASSIFICADA (R2 do check_rpsa); precisa de humano
  declaracao-invalida forma errada (valores fora do enum, motivo curto, escopo=nao com sync!=fonte-unica)
  conflito           contradição com os arquivos alterados (ver motivos) -> NÃO registra; precisa de humano

Contradições barradas (conservadoras, fail-closed):
  C1  escopo=nao mas o merge alterou atomic-spec.md, governance/RULES.md ou governance/CONSTITUTION.md
      (método/INV/CC/RULE — §4.1 — são, por definição, escopo dos agentes)
  C2  sync=propagado mas o merge não alterou .claude/agents/*.md (nada foi propagado)
  C3  escopo=nao mas o merge alterou .claude/agents/*.md (qualquer alteração em agente exige decisão humana)

Papel (ENF-03): escritor determinístico do livro-razão. NÃO homologa, NÃO fecha decisão aberta, NÃO reescreve entradas
(append-only, INV-07). Texto livre da ata nunca é executado nem interpolado em shell.

Uso:
  python scripts/rpsa_auto.py --changed-file changed.txt            # só planeja (stdout JSON)
  python scripts/rpsa_auto.py --changed-file changed.txt --apply    # registra as `registrar` e alinha carimbos
  python scripts/rpsa_auto.py --root <dir> ...                      # raiz alternativa (testes)
Saída: JSON {"plano":[...], "registradas":[...], "pendentes":[...]} ; exit 0 se não há pendência humana, 1 caso contrário.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_rpsa as rp  # noqa: E402

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
ROW = re.compile(r"^\|\s*(RPSA-escopo|RPSA-sync|RPSA-motivo)\s*\|\s*(.*?)\s*\|\s*$", re.M)
HARD_SCOPE = ("atomic-spec.md", "governance/rules.md", "governance/constitution.md")
AGENT_PREFIX = ".claude/agents/"
MIN_MOTIVO = 20


def parse_declaration(text: str) -> dict:
    """Extrai {escopo, sync, motivo} da ata; chaves ausentes ficam fora. Usa só a PRIMEIRA ocorrência de cada linha."""
    d: dict = {}
    for m in ROW.finditer(text):
        k = m.group(1).split("-", 1)[1]
        d.setdefault(k, m.group(2).strip())
    return d


def _norm_paths(changed: list[str]) -> list[str]:
    out = []
    for p in changed:
        p = (p or "").strip().replace("\\", "/")
        while p.startswith("./"):
            p = p[2:]
        p = p.lstrip("/")
        if p:
            out.append(p.lower())
    return out


def evaluate(decl: dict, changed: list[str]) -> dict:
    """Valida a declaração e confronta com os arquivos alterados. Retorna {estado, motivos, entrada?}."""
    if not decl:
        return {"estado": "sem-declaracao", "motivos": ["ata sem linhas RPSA-escopo/RPSA-sync/RPSA-motivo"]}
    erros = []
    esc = decl.get("escopo", "").lower()
    sync = decl.get("sync", "").lower()
    motivo = decl.get("motivo", "").strip()
    if esc not in ("sim", "nao"):
        erros.append("RPSA-escopo deve ser `sim` ou `nao`")
    if sync not in rp.SYNC_VALUES:
        erros.append(f"RPSA-sync deve ser um de {sorted(rp.SYNC_VALUES)}")
    if len(motivo) < MIN_MOTIVO:
        erros.append(f"RPSA-motivo curto demais (< {MIN_MOTIVO} caracteres)")
    if esc == "nao" and sync in rp.SYNC_VALUES and sync != "fonte-unica":
        erros.append("fora de escopo só pode ter sync `fonte-unica`")
    if erros:
        return {"estado": "declaracao-invalida", "motivos": erros}
    ch = _norm_paths(changed)
    tocou_hard = [p for p in ch if p in HARD_SCOPE]
    tocou_agente = [p for p in ch if p.startswith(AGENT_PREFIX) and p.endswith(".md")]
    conf = []
    if esc == "nao" and tocou_hard:
        conf.append(f"C1: declarado fora de escopo, mas o merge alterou {', '.join(sorted(set(tocou_hard)))}")
    if esc == "nao" and tocou_agente:
        conf.append(f"C3: declarado fora de escopo, mas o merge alterou {', '.join(sorted(set(tocou_agente)))}")
    if sync == "propagado" and not tocou_agente:
        conf.append("C2: sync `propagado` declarado, mas o merge não alterou .claude/agents/*.md")
    if conf:
        return {"estado": "conflito", "motivos": conf}
    return {"estado": "registrar", "motivos": [],
            "entrada": {"em_escopo": esc == "sim", "sync": sync, "motivo": motivo}}


def pendentes(root: Path) -> list[tuple[str, Path]]:
    led = rp.load_ledger(root)
    known = set(led.get("pre_baseline", [])) | {led["baseline_stamp"]} | {e["id"] for e in led["entries"]}
    res = [(i, p) for i, p in rp.dhr_files(root).items() if i not in known]
    # ordem cronológica (o livro-razão não aceita data regressiva); id desempata
    return sorted(res, key=lambda t: (rp.dhr_date(t[1]) or "9999-99-99", t[0]))


def plan(root: Path, changed: list[str]) -> list[dict]:
    out = []
    for i, p in pendentes(root):
        ev = evaluate(parse_declaration(p.read_text(encoding="utf-8")), changed)
        out.append({"dhr": i, **ev})
    return out


def apply(root: Path, pl: list[dict]) -> list[str]:
    feitas = []
    for item in pl:
        if item["estado"] != "registrar":
            continue
        e = item["entrada"]
        rp.register(root, item["dhr"], e["em_escopo"], e["sync"], e["motivo"])
        feitas.append(item["dhr"])
    if feitas:
        rp.write(root)  # alinha carimbos dos agentes ao livro-razão (idempotente)
    return feitas


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Registro automático da classificação RPSA declarada na ata (DHR-RPSA-002)")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--changed-file", required=True, help="arquivo com um caminho alterado por linha (diff do merge)")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    changed = Path(a.changed_file).read_text(encoding="utf-8").splitlines()
    pl = plan(root, changed)
    feitas = apply(root, pl) if a.apply else []
    pend = [x for x in pl if x["estado"] != "registrar"]
    print(json.dumps({"plano": pl, "registradas": feitas, "pendentes": [x["dhr"] for x in pend]}, ensure_ascii=False, indent=2))
    return 0 if not pend else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
