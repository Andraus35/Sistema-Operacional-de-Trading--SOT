#!/usr/bin/env python3
"""
build_map.py — BL-019: mapa de grafo do projeto para leitura rápida.

Gera, a partir do grafo de referências (scripts/check_refs.py) e do estado do backlog
(scripts/backlog_triggers.py), um mapa NÃO-NORMATIVO e REGENERÁVEL do repositório:

    docs/mapa/MAPA-PROJETO.md      visão navegável (camadas, hubs, cadeia de Specs, órfãos)
    docs/mapa/mapa-projeto.json    grafo completo (documentos, IDs, arestas) p/ máquina

Uso:
    python scripts/build_map.py                # (re)gera o mapa
    python scripts/build_map.py --check        # exit 1 se o mapa commitado está desatualizado
    python scripts/build_map.py --out DIR      # diretório de saída alternativo

Restrições (BL-019): INV-09 — o mapa não é baseline; não substitui o CATALOGO-OFICIAL
(locator autoritativo); CONS-01 — não fecha decisão aberta; sem dependência externa;
seguro descartar e regenerar. O digest cobre o CONTEÚDO dos documentos (não a data).
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_refs as cr  # noqa: E402
import backlog_triggers as bt  # noqa: E402

ROOT = cr.ROOT
AREA_DESC = {
    "raiz": "entradas: ROADMAP, atomic-spec, AGENTS, GLOSSARIO, README",
    "governance": "autoridade normativa: Constituição, RULES, CATALOGO, atas DHR, emendas EUA",
    "canon": "modelos canônicos BASELINED (CHM/CEM/CEE/GMC/SDD/PPQ/SAS/CR)",
    "specs": "Specs por feature (plan.md + checks.md) e specs de agente",
    "backlog": "RMR-001 e backlogs (gatilhos de ativação)",
    "reference": "referências externas não-normativas (camadas, master contracts)",
    "docs": "documentação histórica e de arranque (não essencial à operação)",
    "rag": "chunks de conhecimento por agente",
    "RETOMADA": "material de retomada (GEH-001)",
    ".claude": "agentes e skills do Claude Code",
    ".clinerules": "regras Cline",
}
ENTRY_POINTS = {"README.md", "AGENTS.md"}
STALE_MARKER = ".stale"  # escrito por scripts/map-sync.js quando não consegue regenerar o mapa
DEF_PRIORITY = ["governance/RULES.md", "governance/CONSTITUTION.md", "governance/CONFLICT-MAP.md", "atomic-spec.md"]


def area_of(path: str) -> str:
    return path.split("/")[0] if "/" in path else "raiz"


def title_of(text: str, path: str) -> str:
    for ln in text.split("\n")[:40]:
        if ln.startswith("# "):
            return ln[2:].strip()
    return Path(path).stem


def doc_key(path: str):
    m = re.match(r"^([A-Z][A-Za-z]*(?:-[A-Za-z]+)*-\d{3})", Path(path).name)
    return m.group(1) if m else None


def esc(s: str) -> str:
    return s.replace("|", "\\|")


def _digest_of(text: dict) -> str:
    digest_src = "\n".join(f"{p}:{hashlib.sha256(text[p].encode('utf-8')).hexdigest()}" for p in sorted(text))
    return hashlib.sha256(digest_src.encode("utf-8")).hexdigest()


def quick_digest() -> str:
    """Digest do CONTEÚDO dos documentos SEM montar o mapa (≈0,03 s contra ≈11 s do build completo).
    Mesma fórmula do build(): permite que `--check` compare o hash antes de qualquer trabalho caro."""
    return _digest_of({cr.rel(p): cr.read(p) for p in cr.list_docs()})


def build():
    docs, reg, findings, edges, counts = cr.analyze()
    paths = [cr.rel(p) for p in docs]
    text = {cr.rel(p): cr.read(p) for p in docs}

    digest = _digest_of(text)

    # --- onde cada ID é definido -------------------------------------------------
    def_doc = {}
    corpus = [p for p in paths if cr.DEF_CORPUS.match(p)]
    corpus.sort(key=lambda p: (DEF_PRIORITY.index(p) if p in DEF_PRIORITY else 99, p))
    for p in corpus:
        for kind in ("RULE", "INV"):
            for m in cr.TOKEN[kind].finditer(text[p]):
                def_doc.setdefault(m.group(0), p)

    gov = ROOT / "governance"
    dhr_file = {f.name.split("_")[0]: cr.rel(f) for f in gov.glob("DHR-*.md")} if gov.exists() else {}
    eua_file = {}
    for f in (gov.glob("EUA-E*.md") if gov.exists() else []):
        m = re.match(r"EUA-E(\d{2}[a-z]?)", f.name)
        if m:
            eua_file[m.group(1)] = cr.rel(f)
    rmr = "backlog/RMR-001_Painel_Backlog.md"

    def defined_in(tok: str):
        if tok.startswith("SPEC-"):
            plan = f"specs/features/{tok}/plan.md"
            return plan if plan in paths else ("ROADMAP.md" if "ROADMAP.md" in paths else None)
        if tok.startswith("BL-"):
            return rmr if rmr in paths else None
        if tok.startswith("DHR-"):
            for stem, f in dhr_file.items():
                if stem == tok or stem.startswith(tok + "-") or tok.startswith(stem + "-"):
                    return f
            return None
        if tok.startswith("EUA-E"):  # ata homologada (DHR) tem precedência sobre a proposta
            return dhr_file.get("DHR-" + tok) or eua_file.get(tok[5:])
        if tok in def_doc:
            return def_doc[tok]
        for d, p in def_doc.items():  # família (RULE-HG → RULE-HG-01)
            if d.startswith(tok + "-"):
                return p
        return None

    # --- arestas doc→doc + refs por ID ------------------------------------------
    doc_edges = set()
    id_refs = defaultdict(set)
    for e in edges:
        if e["type"] == "path":
            if e["to"] in text and e["from"] != e["to"]:
                doc_edges.add((e["from"], e["to"], "path"))
        else:
            id_refs[e["to"]].add(e["from"])
            tgt = defined_in(e["to"])
            if tgt and tgt != e["from"]:
                doc_edges.add((e["from"], tgt, "id"))

    # o documento que DEFINE o ID não conta como quem o cita (evita inflar hubs)
    id_refs = {t: s - {defined_in(t)} for t, s in id_refs.items()}

    inbound, outbound = defaultdict(set), defaultdict(set)
    for a, b, _ in doc_edges:
        outbound[a].add(b)
        inbound[b].add(a)
    # menção pela chave do próprio arquivo (ex.: CHM-001, MC-COG-001)
    for p in paths:
        k = doc_key(p)
        if not k:
            continue
        rx = re.compile(r"(?<![\w-])" + re.escape(k) + r"(?![\w])")
        for q in paths:
            if q != p and rx.search(text[q]):
                inbound[p].add(q)

    info = []
    for p in sorted(paths):
        info.append({"path": p, "area": area_of(p), "title": title_of(text[p], p),
                     "in": len(inbound[p]), "out": len(outbound[p])})

    return {
        "docs": docs, "paths": paths, "info": info, "digest": digest, "counts": dict(counts),
        "doc_edges": sorted(doc_edges), "id_refs": id_refs, "defined_in": defined_in,
        "inbound": inbound, "reg": reg,
    }


def short(path: str) -> str:
    """Rótulo curto; nomes genéricos (plan.md, checks.md) ganham o diretório-pai."""
    parts = path.split("/")
    return "/".join(parts[-2:]) if parts[-1] in ("plan.md", "checks.md") else parts[-1]


def link(path: str, label: str = None) -> str:
    return f"[{esc(label or path)}](../../{quote(path)})"


def render_md(m, date: str) -> str:
    info, inbound = m["info"], m["inbound"]
    by_area = defaultdict(list)
    for i in info:
        by_area[i["area"]].append(i)

    facts = bt.Facts(ROOT)
    rep = bt.build_report(ROOT) if (ROOT / "backlog" / "RMR-001_Painel_Backlog.md").exists() else None
    L = []
    L.append("# MAPA DO PROJETO — SOT Harness")
    L.append("")
    L.append("> **NÃO-NORMATIVO e REGENERÁVEL** (BL-019). Não é baseline (INV-09), não substitui o "
             "[CATALOGO-OFICIAL](../../governance/CATALOGO-OFICIAL.md) — que segue como locator autoritativo — e "
             "não fecha decisão aberta (CONS-01). Em conflito, vale o documento de origem.")
    L.append(">")
    L.append("> Regenerar: `python scripts/build_map.py` · Verificar defasagem: `python scripts/build_map.py --check`")
    L.append("")
    L.append(f"Gerado em **{date}** · digest `{m['digest'][:16]}` · **{len(info)}** documentos · "
             f"**{len(m['doc_edges'])}** arestas doc→doc · fontes: `scripts/check_refs.py`, `scripts/backlog_triggers.py`")
    L.append("")

    # 1. Camadas
    L.append("## 1. Camadas (por diretório)")
    L.append("")
    L.append("| Área | Docs | Função | Mais referenciados |")
    L.append("|---|---:|---|---|")
    order = ["raiz", "governance", "canon", "specs", "backlog", "reference", "rag", ".claude", "docs", "RETOMADA", ".clinerules"]
    for a in sorted(by_area, key=lambda x: order.index(x) if x in order else 99):
        top = sorted(by_area[a], key=lambda i: (-i["in"], i["path"]))[:3]
        tops = " · ".join(link(t["path"], short(t["path"])) + f" ({t['in']})" for t in top if t["in"])
        L.append(f"| **{a}** | {len(by_area[a])} | {esc(AREA_DESC.get(a, ''))} | {tops} |")
    L.append("")

    # 2. Dependências entre camadas (mermaid)
    agg = Counter()
    for a, b, _ in m["doc_edges"]:
        if area_of(a) != area_of(b):
            agg[(area_of(a), area_of(b))] += 1
    L.append("## 2. Dependências entre camadas")
    L.append("")
    L.append("Seta A → B = documentos de A referenciam documentos de B (só pares com ≥ 8 referências).")
    L.append("")
    L.append("```mermaid")
    L.append("flowchart LR")
    for (a, b), n in sorted(agg.items(), key=lambda kv: -kv[1]):
        if n >= 8:
            na, nb = re.sub(r"\W", "_", a), re.sub(r"\W", "_", b)
            L.append(f'  {na}["{a}"] -->|{n}| {nb}["{b}"]')
    L.append("```")
    L.append("")

    # 3. Hubs de ID
    L.append("## 3. Hubs — IDs mais referenciados")
    L.append("")
    L.append("| ID | Documentos que citam | Definido em |")
    L.append("|---|---:|---|")
    for tok, srcs in sorted(m["id_refs"].items(), key=lambda kv: (-len(kv[1]), kv[0]))[:25]:
        d = m["defined_in"](tok)
        L.append(f"| `{tok}` | {len(srcs)} | {link(d) if d else '—'} |")
    L.append("")

    # 4. Cadeia de Specs
    L.append("## 4. Cadeia de Specs")
    L.append("")
    L.append("| Spec | Estado | Plano | Docs que citam |")
    L.append("|---|---|---|---:|")
    for n in sorted(m["reg"].specs):
        tok = f"SPEC-{n}"
        if n in facts.homolog:
            st = "**Homologada**"
        elif n in facts.drafting:
            st = "Em redação"
        else:
            st = "Indicativa (não aberta)"  # EUA-E21/RULE-ECC-01: slot não é compromisso de escopo
        plan = f"specs/features/{tok}/plan.md"
        L.append(f"| `{tok}` | {st} | {link(plan) if n in facts.drafting else '—'} | {len(m['id_refs'].get(tok, ()))} |")
    L.append("")

    # 5. Backlog e integridade
    L.append("## 5. Backlog e integridade")
    L.append("")
    if rep:
        L.append(f"- **Backlog (RMR-001):** ATIVADOS = {', '.join(i['id'] for i in rep['ativados']) or 'nenhum'} · "
                 f"disparados sem registro = {len(rep['disparados_sem_registro'])} · "
                 f"verificação manual = {len(rep['manual'])} itens (`python scripts/backlog_triggers.py`).")
    c = m["counts"]
    L.append(f"- **Referências (check_refs):** ERRO={c.get('ERRO', 0)} · WARN={c.get('WARN', 0)} · "
             f"INFO={c.get('INFO', 0)} (históricos congelados) — `python scripts/check_refs.py`.")
    L.append("")

    # 6. Órfãos
    orphans = [i for i in info if i["in"] == 0 and Path(i["path"]).name not in ENTRY_POINTS
               and i["area"] not in ("docs",)]
    L.append("## 6. Documentos sem referência de entrada")
    L.append("")
    L.append("Nenhum outro documento cita por caminho, por ID resolvido ou pela chave do arquivo "
             "(ex.: `CHM-001`). Só arquivos `.md` são varridos: referências vindas de CI, JSON ou schemas não contam. "
             "Candidatos a revisão de higiene (RPIR) — **não** significa lixo.")
    L.append("")
    for i in orphans:
        L.append(f"- {link(i['path'])} — {esc(i['title'])}")
    if not orphans:
        L.append("- (nenhum)")
    L.append("")

    # 7. Índice completo
    L.append("## 7. Índice de documentos")
    L.append("")
    L.append("`←` = documentos que o citam · `→` = documentos que ele cita.")
    for a in sorted(by_area, key=lambda x: order.index(x) if x in order else 99):
        L.append("")
        L.append(f"### {a}")
        L.append("")
        L.append("| Documento | Título | ← | → |")
        L.append("|---|---|---:|---:|")
        for i in by_area[a]:
            t = i["title"] if len(i["title"]) <= 80 else i["title"][:77] + "..."
            L.append(f"| {link(i['path'], short(i['path']))} | {esc(t)} | {i['in']} | {i['out']} |")
    L.append("")
    return "\n".join(L)


def render_json(m, date: str) -> str:
    ids = []
    for tok, srcs in sorted(m["id_refs"].items()):
        ids.append({"id": tok, "defined_in": m["defined_in"](tok), "cited_by": len(srcs)})
    return json.dumps({
        "meta": {"generated": date, "digest": m["digest"], "normative": False,
                 "note": "NÃO-NORMATIVO; regenerável (BL-019)"},
        "docs": m["info"], "ids": ids,
        "edges": [{"from": a, "to": b, "type": t} for a, b, t in m["doc_edges"]],
    }, ensure_ascii=False, indent=1)


def atomic_write(path: Path, content: str):
    """Escreve via arquivo temporário + replace: hooks concorrentes não deixam mapa pela metade."""
    tmp = path.with_name(path.name + f".{os.getpid()}.tmp")
    tmp.write_text(content, encoding="utf-8")
    for attempt in range(5):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:  # Windows: destino momentaneamente aberto por outro processo
            time.sleep(0.1 * (attempt + 1))
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--out", default=str(ROOT / "docs" / "mapa"))
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    args = ap.parse_args()
    out = Path(args.out)

    js = out / "mapa-projeto.json"

    stale = out / STALE_MARKER
    if args.check:
        # caminho rápido: o hash decide sozinho; o mapa completo NÃO é montado só para comparar (11 s → ≈0,3 s)
        if stale.exists():
            print("Mapa marcado como DEFASADO (o hook não conseguiu regenerá-lo, ex.: Python ausente) — "
                  "rode: python scripts/build_map.py")
            sys.exit(1)
        if not js.exists():
            print("Mapa ausente — rode: python scripts/build_map.py")
            sys.exit(2)
        old = json.loads(js.read_text(encoding="utf-8"))["meta"]["digest"]
        if old != quick_digest():
            print("Mapa DESATUALIZADO (documentos mudaram) — rode: python scripts/build_map.py")
            sys.exit(1)
        print("Mapa em dia.")
        sys.exit(0)

    m = build()
    out.mkdir(parents=True, exist_ok=True)
    atomic_write(out / "MAPA-PROJETO.md", render_md(m, args.date))
    atomic_write(js, render_json(m, args.date))
    if stale.exists():
        stale.unlink()  # regenerado com sucesso: o marcador de defasagem deixa de valer
    print(f"Mapa gerado em {out}: {len(m['info'])} documentos, {len(m['doc_edges'])} arestas, "
          f"digest {m['digest'][:16]}")


if __name__ == "__main__":
    main()
