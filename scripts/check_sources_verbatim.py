#!/usr/bin/env python3
"""check_sources_verbatim.py — Detector determinístico de captura verbatim do Dossiê de Pesquisa (M1 + M2 + M8).

[PROPOSTA — NÃO HOMOLOGADO] Origem: governance/propostas/PESQUISA-ESPECIFICADOR/PROPOSTA-MELHORIA-PESQUISA.md (M1, M2, M8),
escolha "pacote equilibrado" de Andraus (chat, 2026-10-06). É DETECTOR (ENF-03): aponta candidatos a achado; NÃO decide,
NÃO homologa, NÃO é gate. Não usa web. Não verifica a veracidade das páginas (mesmo mandato do Revisor): só que o que está
entre « » existe LITERALMENTE nas capturas `sources/<ID>.txt` da mesma pasta (RULE-ECC-04).

Unidade de verificação = pasta que contém `sources/*.txt`; os documentos `.md` dessa pasta-pai são os Dossiês/Propostas.
  M1  toda citação « » deve existir como substring literal (espaços colapsados) em algum sources/*.txt da unidade.
      Elipse (`...` ou `…`) dentro de « »: CADA lado precisa existir como substring literal.
      Fora das capturas, aceita-se (INFO) trecho que exista em algum arquivo de texto do repositório (citação INTERNA, [FATO]).
      Trechos < --min caracteres não são conferidos (INFO).                                                  → ERRO se não existe.
  M2  citação « » na mesma linha de um rótulo `não-capturado` (conteúdo de sumário de busca ≠ página) → AVISO:
      só o que foi capturado verbatim pode ir entre aspas.                                                    → WARN.
  M8  cada captura precisa de `Data de acesso: AAAA-MM-DD` dentro da janela (--window dias; padrão 90 = HIGH/CRITICAL,
      ECC-VAL-001/DHR-DEC-003, usada só como parâmetro).                                                      → WARN.

Uso:
    python scripts/check_sources_verbatim.py                     # todas as unidades do repositório (informativo)
    python scripts/check_sources_verbatim.py PASTA [PASTA...]    # só estas unidades (a PASTA contém sources/)
    python scripts/check_sources_verbatim.py --json              # saída para máquina
    python scripts/check_sources_verbatim.py --root DIR --today AAAA-MM-DD --window N --min N   # (testes)
Exit 0 = nenhum ERRO · 1 = há ERRO (WARN/INFO não reprovam; use --strict para WARN também). exit 0 ≠ CONFORME ≠ homologação.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
QUOTE = re.compile(r"«(.+?)»", re.S)
ELLIPSIS = re.compile(r"\.\.\.|…")
ACCESS = re.compile(r"^Data de acesso\s*:\s*(\d{4}-\d{2}-\d{2})", re.I | re.M)
NOT_CAPTURED = re.compile(r"n[ãa]o[- ]capturad", re.I)
NEAR_BEFORE, NEAR_AFTER = 45, 25   # M2: rótulo 'não-capturado' imediatamente antes/depois da citação
# Specs/unidades anteriores à ECC-VAL-001/RULE-ECC-06 (INV-07: sem reescrita retroativa) — mesmo conjunto de check_repo_research.py.
GRANDFATHERED = {"SPEC-001", "SPEC-002", "SPEC-003", "SPEC-019", "SPEC-020", "SPEC-021", "SPEC-038", "SPEC-046"}
SKIP_DIRS = {".git", "node_modules", ".pytest_cache", "__pycache__", "docs"}   # docs/ = mapa gerado/legado (INV-07)
TEXT_EXT = {".md", ".py", ".js", ".yml", ".yaml", ".json", ".txt", ".sh", ".toml"}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def find_units(root: Path, only: list[Path] | None):
    if only:
        return [p for p in only if (p / "sources").is_dir()]
    out = []
    for d in sorted(root.rglob("sources")):
        if d.is_dir() and not (set(d.relative_to(root).parts) & SKIP_DIRS) and any(d.glob("*.txt")):
            out.append(d.parent)
    return out


def repo_text(root: Path, exclude: set[Path]) -> str:
    """Texto normalizado dos arquivos do repositório que NÃO são documentos de pesquisa (para aceitar citação INTERNA como INFO).

    Os .md das pastas com sources/ (Dossiês/Propostas sob verificação) ficam FORA do corpus: senão toda citação se
    'encontraria' no próprio documento (ou num irmão) e nenhuma citação inventada seria detectada."""
    parts = []
    for p in root.rglob("*"):
        if (p.is_file() and p.suffix.lower() in TEXT_EXT and p.resolve() not in exclude
                and not (set(p.relative_to(root).parts) & SKIP_DIRS)):
            try:
                parts.append(read(p))
            except OSError:
                pass
    return norm("\n".join(parts))


def check_unit(unit: Path, root: Path, today: date, window: int, minlen: int, get_repo_text):
    findings = []   # (severidade, arquivo, linha, mensagem)
    rel = lambda p: str(p.relative_to(root)).replace("\\", "/") if root in p.parents or p == root else str(p)
    caps = sorted((unit / "sources").glob("*.txt"))
    cap_text = norm("\n".join(read(c) for c in caps))

    # M8 — data de acesso (notas "_*.txt" não são capturas; Specs anteriores à regra viram INFO)
    old = unit.name in GRANDFATHERED
    sev8 = "INFO" if old else "WARN"
    for c in [c for c in caps if not c.name.startswith("_")]:
        m = ACCESS.search(read(c))
        if not m:
            findings.append((sev8, rel(c), 1, "M8: captura sem 'Data de acesso: AAAA-MM-DD' (ECC-VAL-001 não verificável)"))
            continue
        try:
            d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            findings.append((sev8, rel(c), 1, f"M8: data de acesso inválida '{m.group(1)}'"))
            continue
        age = (today - d).days
        if age < 0:
            findings.append((sev8, rel(c), 1, f"M8: data de acesso {d} está no futuro"))
        elif age > window:
            findings.append((sev8, rel(c), 1, f"M8: captura de {d} tem {age} dias (> janela de {window}; ECC-VAL-001)"))

    # M1 + M2 — citações nos .md da unidade
    for md in sorted(unit.glob("*.md")):
        text = read(md)
        for m in QUOTE.finditer(text):
            if not norm(m.group(1)):   # '« »' vazio = o próprio símbolo citado no texto, não uma citação
                continue
            line = text.count("\n", 0, m.start()) + 1
            near = text[max(0, m.start() - NEAR_BEFORE):m.start()] + " " + text[m.end():m.end() + NEAR_AFTER]
            if NOT_CAPTURED.search(near):
                findings.append(("WARN", rel(md), line, "M2: citação entre « » colada a rótulo 'não-capturado' — "
                                 "sumário de busca não é a página; só captura verbatim vai entre aspas"))
            sides = [norm(x) for x in ELLIPSIS.split(m.group(1))]
            for side in [s for s in sides if s]:
                if len(side) < minlen:
                    findings.append(("INFO", rel(md), line, f"M1: trecho curto (<{minlen}) não conferido: «{side[:40]}»"))
                elif side in cap_text:
                    continue
                elif side in get_repo_text(unit):
                    findings.append(("INFO", rel(md), line, f"M1: citação INTERNA do repositório (não é fonte externa): «{side[:60]}…»"))
                else:
                    findings.append(("ERRO", rel(md), line, f"M1: citação NÃO encontrada em sources/ nem no repositório: «{side[:80]}…» (RULE-ECC-04)"))
    return findings


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--today", default=None, help="AAAA-MM-DD (padrão: hoje; para testes)")
    ap.add_argument("--window", type=int, default=90)
    ap.add_argument("--min", dest="minlen", type=int, default=15)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    today = datetime.strptime(a.today, "%Y-%m-%d").date() if a.today else date.today()
    only = [Path(p) if Path(p).is_absolute() else root / p for p in a.paths] or None
    units = find_units(root, only)
    cache = {}
    # corpus interno por unidade: exclui só os .md da PRÓPRIA unidade (o documento citante e seus irmãos), senão toda citação
    # se "encontraria" no próprio texto; citar documento de OUTRA unidade (ex.: uma diretiva) continua sendo citação interna.
    get_repo = lambda unit: cache.setdefault(unit, repo_text(root, {md.resolve() for md in unit.glob("*.md")}))
    findings = []
    for u in units:
        findings += check_unit(u, root, today, a.window, a.minlen, get_repo)
    order = {"ERRO": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda f: (order[f[0]], f[1], f[2]))
    counts = {k: sum(1 for f in findings if f[0] == k) for k in order}
    if a.json:
        print(json.dumps({"unidades": [str(u.relative_to(root)).replace("\\", "/") for u in units],
                          "achados": [{"severidade": s, "arquivo": f, "linha": l, "mensagem": m} for s, f, l, m in findings],
                          "contagens": counts}, ensure_ascii=False, indent=1))
    else:
        print("=" * 60); print("check_sources_verbatim — captura verbatim do Dossiê (M1/M2/M8)"); print(f"Unidades: {len(units)}"); print("=" * 60)
        for s, f, l, m in findings:
            if s != "INFO":
                print(f"[{s}] {f}:{l} — {m}")
        print("-" * 60); print(f"ERRO={counts['ERRO']} WARN={counts['WARN']} INFO={counts['INFO']}  (INFO: use --json para ver)")
        print("LEMBRETE: Detector (ENF-03); não verifica a veracidade das páginas; exit 0 ≠ CONFORME ≠ homologação.")
    return 1 if counts["ERRO"] or (a.strict and counts["WARN"]) else 0


if __name__ == "__main__":
    sys.exit(main())
