#!/usr/bin/env python3
"""
check_refs.py — verificador de integridade de referências cruzadas do SOT.

Somente leitura. Detecta (a) IDs citados que nunca são definidos (SPEC/BL/DHR/EUA/RULE/INV)
e (b) caminhos de arquivo citados que não existem. Opcionalmente exporta o grafo de
referências (--graph) — semente do "mapa do projeto" (backlog).

Uso:
    python scripts/check_refs.py                 # relatório; exit 1 se houver ERRO
    python scripts/check_refs.py --strict        # WARN também falha
    python scripts/check_refs.py --info          # inclui achados INFO (históricos)
    python scripts/check_refs.py --graph out.json

Severidades
    ERRO  referência quebrada em documento VIVO (normativo em vigor)
    WARN  referência quebrada em documento não-normativo/em elaboração, ou caminho movido
    INFO  referência quebrada em documento CONGELADO (atas DHR, propostas EUA) — INV-07:
          não se reescreve; o CATALOGO-OFICIAL resolve localização. Nunca falha o gate.

Este script NÃO é gate de conformidade (exit 0 ≠ CONFORME ≠ homologação) e não fecha
decisão aberta (CONS-01): apenas aponta referências sem alvo.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE = re.compile(
    r"(^|/)(node_modules|\.git|UPGRADES|_legacy)(/|$)|harness-eval/runs/|^docs/mapa/"  # docs/mapa = saída gerada
)
# Congelados: atas e propostas (INV-07) — nunca reescritos.
FROZEN = re.compile(r"(^|/)governance/(DHR-|EUA-|HOD-|MAN-|PP-|PE-)|^docs/")
# Marcadores de referência prospectiva (alvo ainda a criar) — não é erro.
FORWARD = re.compile(r"(será|serão|futur|próxim|proposta|pendente|reservad|planejad|a ser |candidat|diferid|normatizad|e\.g\.|ex\.:|exemplo|for example|sem lastro)", re.I)
# Placeholders de ID (INV-GAP-nnn, SPEC-xxx): padrão, não referência.
PLACEHOLDER = re.compile(r"^-(?:nnn|NNN|xxx?|XXX?|##+|n+)\b")

# Fontes de definição para RULE-* / INV-*
DEF_CORPUS = re.compile(
    r"^(governance/(RULES|CONSTITUTION|CONFLICT-MAP|GPR-001[^/]*|SES-001[^/]*)\.md"
    r"|atomic-spec\.md|ROADMAP\.md|canon/[^/]+\.md|GLOSSARIO\.md"
    r"|specs/[^/]+\.spec\.md|specs/features/[^/]+/plan\.md)$"
)

TOKEN = {
    "SPEC": re.compile(r"(?<![\w-])SPEC-(\d{3})(?![\w-])"),
    "BL": re.compile(r"(?<![\w-])BL-(\d{3})(?![\w-])"),
    "DHR": re.compile(r"(?<![\w-])DHR-[A-Z0-9]+(?:-[A-Za-z0-9]+)*"),
    "EUA": re.compile(r"(?<![\w-])EUA-E(\d{2}[a-z]?)(?![\w])"),
    "RULE": re.compile(r"(?<![\w-])RULE-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*"),
    "INV": re.compile(r"(?<![\w-])INV-[A-Z0-9]+(?:-[A-Z0-9]+)*"),
}
PATH_EXT = r"(?:md|MD|json|py|js|yml|yaml)"
BACKTICK = re.compile(r"`([^`\n]{3,160})`")
MDLINK = re.compile(r"\]\(([^)\s]{3,200})\)")
PATHLIKE = re.compile(r"^[\w./ %\-ÁÉÍÓÚÂÊÔÃÕÇáéíóúâêôãõç]+\." + PATH_EXT + r"$")


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def list_docs():
    out = []
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() == ".md":
            r = rel(p)
            if not EXCLUDE.search(r):
                out.append(p)
    return sorted(out)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def strip_fences(text: str) -> str:
    """Remove blocos ``` (exemplos/diagramas) para não gerar referências espúrias."""
    # preserva a contagem de linhas para que os números reportados batam com o arquivo
    return re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)


class Registry:
    """Conjuntos de IDs definidos, extraídos de fontes objetivas."""

    def __init__(self, docs):
        self.docs = docs
        # existência de arquivo inclui UPGRADES/_legacy (só não são varridos como documento)
        self.all_files = {rel(p) for p in ROOT.rglob("*")
                          if p.is_file() and not re.search(r"(^|/)(node_modules|\.git)(/|$)", rel(p))}
        self.basenames = defaultdict(set)
        for f in self.all_files:
            self.basenames[Path(f).name.lower()].add(f)

        gov = ROOT / "governance"
        self.dhr_stems = {p.name.split("_")[0] for p in gov.glob("DHR-*.md")} if gov.exists() else set()
        self.eua = set()
        if gov.exists():
            for p in gov.glob("EUA-E*.md"):
                m = re.match(r"EUA-E(\d{2}[a-z]?)", p.name)
                if m:
                    self.eua.add(m.group(1))

        # EUA também é definida por cabeçalho de ata DHR / atomic-spec (ex.: EUA-E01..E03 sem proposta própria)
        for p in (list(gov.glob("DHR-*.md")) if gov.exists() else []) + [ROOT / "atomic-spec.md"]:
            if p.exists():
                head = "\n".join(read(p).split("\n")[:20])
                self.eua |= set(re.findall(r"EUA-E(\d{2}[a-z]?)", head))

        # EUA anunciada como futura por ata/proposta de governança (ex.: EUA-E20 na DHR-EUA-E19a)
        # — alvo planejado, não referência quebrada.
        if gov.exists():
            for p in gov.glob("*.md"):
                for ln in read(p).split("\n"):
                    if FORWARD.search(ln):
                        self.eua |= set(re.findall(r"EUA-E(\d{2}[a-z]?)", ln))

        self.specs = set()
        feats = ROOT / "specs" / "features"
        if feats.exists():
            self.specs |= {d.name.split("-", 1)[1][:3] for d in feats.iterdir() if d.name.startswith("SPEC-")}
        road = ROOT / "ROADMAP.md"
        if road.exists():
            self.specs |= set(re.findall(r"^#{2,4}\s*SPEC-(\d{3})\b", read(road), re.M))
            # o ROADMAP é a autoridade da sequência: qualquer SPEC-### nele está declarada
            self.specs |= set(re.findall(r"(?<![\w-])SPEC-(\d{3})(?![\w-])", read(road)))

        self.bls = set()
        rmr = ROOT / "backlog" / "RMR-001_Painel_Backlog.md"
        if rmr.exists():
            self.bls |= set(re.findall(r"\|\s*\*\*BL-(\d{3})\*\*", read(rmr)))
        for p in (ROOT / "backlog").glob("BL-*.md") if (ROOT / "backlog").exists() else []:
            m = re.match(r"BL-(\d{3})", p.name)
            if m:
                self.bls.add(m.group(1))

        self.rules, self.invs = set(), set()
        for p in docs:
            if DEF_CORPUS.match(rel(p)):
                t = read(p)
                self.rules |= {m.group(0) for m in TOKEN["RULE"].finditer(t)}
                self.invs |= {m.group(0) for m in TOKEN["INV"].finditer(t)}

    @staticmethod
    def _family_ok(tok: str, defined: set) -> bool:
        """RULE-HG ("família") é válido se existir RULE-HG-01; RULE-X-01 se X-01 ou prefixo definido."""
        if tok in defined:
            return True
        return any(d.startswith(tok + "-") for d in defined)

    def defined(self, kind: str, m: re.Match) -> bool:
        tok = m.group(0)
        if kind == "SPEC":
            return m.group(1) in self.specs
        if kind == "BL":
            return m.group(1) in self.bls
        if kind == "EUA":
            return m.group(1) in self.eua
        if kind == "DHR":
            return any(s == tok or s.startswith(tok + "-") or tok.startswith(s + "-") for s in self.dhr_stems)
        if kind == "RULE":
            return self._family_ok(tok, self.rules)
        if kind == "INV":
            return self._family_ok(tok, self.invs)
        return True


def classify_severity(path: str, kind: str) -> str:
    if FROZEN.search(path) or "PROPOSTA" in path:
        return "INFO"
    if path.startswith("reference/"):
        return "INFO"  # referências externas: namespaces locais próprios (I-EXP, INV-EPI...)
    if kind in ("RULE", "INV"):
        return "WARN"  # pode ser regra proposta ainda não homologada
    if path.startswith(("rag/", "RETOMADA/")):
        return "WARN"
    return "ERRO"


def resolve_path(src: Path, raw: str, reg: Registry):
    """Retorna (estado, alvo): 'ok' | 'moved' | 'missing'."""
    t = unquote(raw.split("#")[0])
    t = re.sub(r":\d+(?:[-–]\d+)?(?:,\s*\d+)*$", "", t).strip()
    if re.match(r"^(node|python3?|npm|npx)\s", t):  # comando: o alvo é o último argumento
        t = t.split()[-1]
    if not PATHLIKE.match(t) or "..." in t or (t.startswith(".") and not t.startswith(("./", "../"))):
        return None, None
    bare = "/" not in t  # nome sem diretório = atalho de citação, não caminho
    cand = [t, (src.parent / t).relative_to(ROOT).as_posix() if (src.parent / t).resolve().is_relative_to(ROOT) else t]
    for c in cand:
        if c in reg.all_files:
            return "ok", c
    tt = t.lstrip("./")
    if not bare:  # sufixo: "SPEC-001/plan.md" ~ "specs/features/SPEC-001/plan.md"
        for f in sorted(reg.all_files):
            if f.endswith("/" + tt):
                return "ok", f
    hits = reg.basenames.get(Path(t).name.lower())
    if hits:
        return ("ok", sorted(hits)[0]) if bare else ("moved", sorted(hits)[0])
    return ("missing_bare" if bare else "missing"), None


def analyze():
    """Varre o repositório. Retorna (docs, registry, achados_dedup, arestas, contagens)."""
    docs = list_docs()
    reg = Registry(docs)
    findings = []  # (sev, file, line, msg)
    edges = []

    for p in docs:
        r = rel(p)
        raw = read(p)
        text = strip_fences(raw)
        # linhas originais para reportar nº de linha aproximado
        lines = text.split("\n")
        for i, line in enumerate(lines, 1):
            for kind, rx in TOKEN.items():
                for m in rx.finditer(line):
                    tok = m.group(0)
                    if PLACEHOLDER.match(line[m.end():m.end() + 5]):
                        continue
                    if kind == "SPEC" and not (ROOT / "ROADMAP.md").exists():
                        continue
                    if reg.defined(kind, m):
                        edges.append({"from": r, "to": tok, "type": "id"})
                    else:
                        sev = "INFO" if FORWARD.search(line) else classify_severity(r, kind)
                        findings.append((sev, r, i, f"{kind} sem definição: {tok}"))
            for rx in (BACKTICK, MDLINK):
                for m in rx.finditer(line):
                    state, target = resolve_path(p, m.group(1), reg)
                    if state == "ok":
                        edges.append({"from": r, "to": target, "type": "path"})
                    elif state == "moved":
                        sev = "INFO" if FROZEN.search(r) else "WARN"
                        edges.append({"from": r, "to": target, "type": "path"})
                        findings.append((sev, r, i, f"caminho desatualizado: {m.group(1)} → existe em {target}"))
                    elif state == "missing_bare":
                        findings.append(("INFO", r, i, f"nome sem diretório e sem alvo: {m.group(1)}"))
                    elif state == "missing":
                        soft = r.startswith(("reference/", "rag/", "RETOMADA/")) or "PROPOSTA" in r
                        sev = "INFO" if (FROZEN.search(r) or FORWARD.search(line)) else ("WARN" if soft else "ERRO")
                        findings.append((sev, r, i, f"caminho inexistente: {m.group(1)}"))

    # deduplica (arquivo, msg)
    seen, uniq = set(), []
    for f in findings:
        k = (f[0], f[1], f[3])
        if k not in seen:
            seen.add(k)
            uniq.append(f)

    counts = defaultdict(int)
    for f in uniq:
        counts[f[0]] += 1
    return docs, reg, uniq, edges, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--info", action="store_true")
    ap.add_argument("--graph", metavar="OUT.json")
    args = ap.parse_args()

    docs, reg, uniq, edges, counts = analyze()

    order = {"ERRO": 0, "WARN": 1, "INFO": 2}
    shown = [f for f in sorted(uniq, key=lambda x: (order[x[0]], x[1], x[2])) if args.info or f[0] != "INFO"]
    print("=" * 60)
    print("VERIFICADOR DE REFERÊNCIAS — check_refs.py")
    print(f"Documentos: {len(docs)} · arestas resolvidas: {len(edges)}")
    print(f"IDs definidos: SPEC={len(reg.specs)} BL={len(reg.bls)} DHR={len(reg.dhr_stems)} "
          f"EUA={len(reg.eua)} RULE={len(reg.rules)} INV={len(reg.invs)}")
    print("=" * 60)
    for sev, f, ln, msg in shown:
        print(f"[{sev}] {f}:{ln} — {msg}")
    print("-" * 60)
    print(f"ERRO={counts['ERRO']} WARN={counts['WARN']} INFO={counts['INFO']}"
          + ("" if args.info else "  (use --info para ver os históricos)"))
    print("LEMBRETE: gate auxiliar. exit 0 ≠ CONFORME ≠ homologação.")

    if args.graph:
        nodes = sorted({e["from"] for e in edges} | {e["to"] for e in edges})
        Path(args.graph).write_text(
            json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        print(f"Grafo escrito em {args.graph} ({len(nodes)} nós, {len(edges)} arestas)")

    fail = counts["ERRO"] > 0 or (args.strict and counts["WARN"] > 0)
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
