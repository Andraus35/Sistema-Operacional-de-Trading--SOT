#!/usr/bin/env python3
"""check_rpsa.py — carimbo `sincronizado-até` dos agentes (RPSA, EUA-E16) de forma DETERMINÍSTICA.

RPSA (DHR-EUA-E16 §4.3): o carimbo de `.claude/agents/{especificador,revisor}.md` deve corresponder à
**última DHR em escopo dos agentes** (§4.1). A ordem textual do CATALOGO não é confiável, e "em escopo" é
um julgamento — por isso a fonte de verdade é um **livro-razão append-only** (`governance/rpsa-ledger.json`):
cada DHR posterior ao carimbo-base é CLASSIFICADA (em escopo ou não, com motivo, e como o Agent-Sync foi
resolvido). O script não decide o julgamento: ele o exige registrado e depois mantém os carimbos em sincronia.

Papel (ENF-03): DETECTOR + escritor de carimbos. Não homologa, não fecha decisão aberta, não promove item.

Uso:
  python scripts/check_rpsa.py                      # confere (exit 0 ok · 1 divergência)
  python scripts/check_rpsa.py --json               # saída estruturada
  python scripts/check_rpsa.py --write              # alinha carimbos dos agentes ao livro-razão (idempotente)
  python scripts/check_rpsa.py --register DHR-X --scope sim|nao --sync fonte-unica|propagado|pendente \\
                               --motivo "..."       # classifica uma DHR (lê a Data da própria ata) e alinha os carimbos
  python scripts/check_rpsa.py --root <dir>         # raiz alternativa (testes)

Regras checadas:
  R1  cada DHR do livro-razão existe em governance/ e as Datas não regridem;
  R2  toda DHR em governance/ fora de `pre_baseline` e do livro-razão é NÃO CLASSIFICADA (divergência);
  R3  nenhuma entrada em escopo com sync `pendente` (gate bloqueante §4.5);
  R4  carimbo de cada agente == última entrada em escopo resolvida (ou `baseline_stamp`);
  R5  `last_sync_catalog_date` de cada agente == Data da DHR do carimbo.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
LEDGER_REL = "governance/rpsa-ledger.json"
AGENTS_REL = [".claude/agents/especificador.md", ".claude/agents/revisor.md"]
DHR_ID = re.compile(r"^DHR-[A-Za-z0-9][A-Za-z0-9._-]*$")
STAMP_RE = re.compile(r"^(sincronizado-até:\s*)(DHR-[A-Za-z0-9][A-Za-z0-9._-]*)", re.M)
DATE_RE = re.compile(r"^(last_sync_catalog_date:\s*)(\d{4}-\d{2}-\d{2})", re.M)
DATA_ROW = re.compile(r"^\|\s*Data\s*\|\s*(\d{4}-\d{2}-\d{2})", re.M)
SYNC_VALUES = {"fonte-unica", "propagado", "pendente"}


def dhr_id_of(path: Path) -> str:
    return path.name.split("_", 1)[0].removesuffix(".md")


def dhr_files(root: Path) -> dict[str, Path]:
    return {dhr_id_of(p): p for p in sorted((root / "governance").glob("DHR-*.md"))}


def dhr_date(path: Path) -> str | None:
    m = DATA_ROW.search(path.read_text(encoding="utf-8"))
    return m.group(1) if m else None


def load_ledger(root: Path) -> dict:
    return json.loads((root / LEDGER_REL).read_text(encoding="utf-8"))


def save_ledger(root: Path, led: dict) -> None:
    (root / LEDGER_REL).write_text(json.dumps(led, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def expected_stamp(led: dict) -> str:
    resolved = [e for e in led["entries"] if e["em_escopo"] and e["sync"] != "pendente"]
    return resolved[-1]["id"] if resolved else led["baseline_stamp"]


def stamp_date(root: Path, led: dict, stamp: str, files: dict[str, Path]) -> str | None:
    for e in led["entries"]:
        if e["id"] == stamp:
            return e["data"]
    return dhr_date(files[stamp]) if stamp in files else None


def check(root: Path) -> list[dict]:
    achados: list[dict] = []
    add = lambda regra, msg: achados.append({"regra": regra, "msg": msg})
    led = load_ledger(root)
    files = dhr_files(root)
    known = set(led.get("pre_baseline", [])) | {led["baseline_stamp"]} | {e["id"] for e in led["entries"]}

    prev = None
    seen = set()
    for e in led["entries"]:
        if e["id"] in seen:
            add("R1", f"{e['id']} duplicada no livro-razão")
        seen.add(e["id"])
        if e["id"] not in files:
            add("R1", f"{e['id']} está no livro-razão mas não há governance/{e['id']}_*.md")
        elif dhr_date(files[e["id"]]) != e["data"]:
            add("R1", f"{e['id']}: Data do livro-razão ({e['data']}) ≠ Data da ata ({dhr_date(files[e['id']])})")
        if prev and e["data"] < prev:
            add("R1", f"{e['id']}: Data {e['data']} anterior à da entrada anterior ({prev}) — ordem do livro-razão regride")
        prev = e["data"]
        if e["sync"] not in SYNC_VALUES:
            add("R1", f"{e['id']}: sync inválido '{e['sync']}'")
        if e["em_escopo"] and e["sync"] == "pendente":
            add("R3", f"{e['id']}: Agent-Sync PENDENTE (gate §4.5 — a próxima Spec não inicia com sincronização em aberto)")

    for i in sorted(set(files) - known):
        add("R2", f"{i} NÃO CLASSIFICADA: registre com --register (em escopo? sync? motivo) — RPSA §4.1")

    want = expected_stamp(led)
    want_date = stamp_date(root, led, want, files)
    for rel in AGENTS_REL:
        p = root / rel
        if not p.exists():
            add("R4", f"{rel} ausente")
            continue
        txt = p.read_text(encoding="utf-8")
        m, d = STAMP_RE.search(txt), DATE_RE.search(txt)
        if not m:
            add("R4", f"{rel}: sem linha `sincronizado-até: DHR-…`")
        elif m.group(2) != want:
            add("R4", f"{rel}: carimbo {m.group(2)} ≠ esperado {want} (última DHR em escopo resolvida)")
        if not d:
            add("R5", f"{rel}: sem linha `last_sync_catalog_date:`")
        elif want_date and d.group(2) != want_date:
            add("R5", f"{rel}: last_sync_catalog_date {d.group(2)} ≠ Data da DHR do carimbo ({want_date})")
    return achados


def write(root: Path) -> list[str]:
    led = load_ledger(root)
    files = dhr_files(root)
    want = expected_stamp(led)
    want_date = stamp_date(root, led, want, files)
    mudou = []
    for rel in AGENTS_REL:
        p = root / rel
        txt = p.read_text(encoding="utf-8")
        novo = STAMP_RE.sub(lambda m: m.group(1) + want, txt, count=1)
        if want_date:
            novo = DATE_RE.sub(lambda m: m.group(1) + want_date, novo, count=1)
        if novo != txt:
            p.write_text(novo, encoding="utf-8")
            mudou.append(rel)
    return mudou


def register(root: Path, dhr: str, escopo: bool, sync: str, motivo: str) -> None:
    if not DHR_ID.match(dhr):
        raise SystemExit(f"ERRO: id inválido '{dhr}'")
    if sync not in SYNC_VALUES:
        raise SystemExit(f"ERRO: --sync deve ser um de {sorted(SYNC_VALUES)}")
    if not motivo.strip():
        raise SystemExit("ERRO: --motivo é obrigatório (o julgamento de escopo precisa de justificativa)")
    led = load_ledger(root)
    files = dhr_files(root)
    if dhr not in files:
        raise SystemExit(f"ERRO: não existe governance/{dhr}_*.md")
    if dhr in {e["id"] for e in led["entries"]} | set(led.get("pre_baseline", [])) | {led["baseline_stamp"]}:
        raise SystemExit(f"ERRO: {dhr} já está classificada (livro-razão é append-only; corrija por nova ata)")
    data = dhr_date(files[dhr])
    if not data:
        raise SystemExit(f"ERRO: a ata {dhr} não tem linha `| Data | AAAA-MM-DD |`")
    if led["entries"] and data < led["entries"][-1]["data"]:
        raise SystemExit(f"ERRO: Data {data} anterior à última entrada ({led['entries'][-1]['data']})")
    led["entries"].append({"id": dhr, "data": data, "em_escopo": escopo, "sync": sync, "motivo": motivo.strip()})
    save_ledger(root, led)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="RPSA — carimbos dos agentes (determinístico)")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--register")
    ap.add_argument("--scope", choices=["sim", "nao"])
    ap.add_argument("--sync", default="fonte-unica")
    ap.add_argument("--motivo", default="")
    a = ap.parse_args(argv[1:])
    root = Path(a.root).resolve()

    if a.register:
        if not a.scope:
            raise SystemExit("ERRO: --register exige --scope sim|nao")
        register(root, a.register, a.scope == "sim", a.sync, a.motivo)
        print(f"registrada: {a.register} (em escopo: {a.scope}; sync: {a.sync})")
        a.write = True
    if a.write:
        mudou = write(root)
        print("carimbos alinhados:", ", ".join(mudou) if mudou else "nenhuma mudança (já em sincronia)")

    achados = check(root)
    if a.json:
        print(json.dumps({"ok": not achados, "achados": achados}, ensure_ascii=False, indent=2))
    else:
        for x in achados:
            print(f"  [{x['regra']}] {x['msg']}")
        print(f"RPSA: {'OK — carimbos em sincronia' if not achados else str(len(achados)) + ' divergência(s)'}")
        print("Detector (ENF-03): não homologa nem fecha decisão aberta. exit 0 ≠ CONFORME ≠ homologação.")
    return 0 if not achados else 1


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except BrokenPipeError:  # saída canalizada para head/less: não é erro da ferramenta
        try:
            sys.stdout.close()
        except Exception:
            pass
        sys.exit(0)
