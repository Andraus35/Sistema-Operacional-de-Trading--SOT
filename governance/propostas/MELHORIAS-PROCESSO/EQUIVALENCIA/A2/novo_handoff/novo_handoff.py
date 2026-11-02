#!/usr/bin/env python3
"""novo_handoff.py — PROPOSTA (não instalada). Faz os passos MECÂNICOS de trocar o HANDOFF.md (AGENTS.md §11).

Faz, de forma atômica (tudo ou nada): (1) copia o HANDOFF.md atual, byte a byte, para docs/handoffs/HO-<id>.md;
(2) troca `handoff_id` (número +1), `previous` (= id antigo), `data` e `base_commit`; (3) aplica as trocas de texto pedidas
com --trocar 'ANTIGO=>NOVO' e FALHA ALTO se alguma âncora não existir exatamente uma vez (acaba o `replace` silencioso).
Não decide conteúdo, não registra homologação, não fecha decisão aberta (CONS-01). Detector/utilitário (ENF-03).

Uso: python novo_handoff.py [--root R] [--data AAAA-MM-DD] [--base HASH] [--trocar 'A=>B' ...] [--ramo NOME]
Saída: exit 0 ok · 2 recusado (nada foi escrito).
"""
from __future__ import annotations
import argparse, datetime, re, subprocess, sys
from pathlib import Path

ID_RE = re.compile(r"^(HO-\d{4}-\d{2}-\d{2}-)(\d+)$")


def _fm_get(text: str, key: str) -> str | None:
    m = re.search(rf"^{key}:[ \t]*(.*)$", text.split("\n---", 2)[0] if text.startswith("---") else "", re.M)
    return m.group(1).strip() if m else None


def planejar(root: Path, data: str, base: str | None, trocas: list[str], ramo: str | None):
    """Devolve (novo_texto, id_antigo, id_novo, destino_da_copia) ou levanta SystemExit(2) sem escrever nada."""
    h = root / "HANDOFF.md"
    if not h.exists():
        raise SystemExit("RECUSADO: HANDOFF.md ausente")
    texto = h.read_text(encoding="utf-8")
    if not texto.startswith("---\n"):
        raise SystemExit("RECUSADO: HANDOFF.md sem frontmatter")
    antigo = _fm_get(texto, "handoff_id")
    m = ID_RE.match(antigo or "")
    if not m:
        raise SystemExit(f"RECUSADO: handoff_id inválido: {antigo!r}")
    prefixo_data = re.sub(r"\d{4}-\d{2}-\d{2}", data, m.group(1))
    novo = f"{prefixo_data}{int(m.group(2)) + 1:0{len(m.group(2))}d}"
    destino = root / "docs" / "handoffs" / (f"ramo-{ramo}" if ramo else "") / f"{antigo}.md"
    if destino.exists() and destino.read_text(encoding="utf-8") != texto:
        raise SystemExit(f"RECUSADO: {destino.relative_to(root)} já existe e DIFERE do handoff atual (cadeia colidiu; use --ramo)")
    out = texto
    for campo, valor in (("handoff_id", novo), ("previous", antigo), ("data", data)) + ((("base_commit", base),) if base else ()):
        out, n = re.subn(rf"^({campo}:)[ \t]*.*$", rf"\g<1> {valor}", out, count=1, flags=re.M)
        if n != 1:
            raise SystemExit(f"RECUSADO: campo `{campo}` ausente no frontmatter")
    for par in trocas:
        if "=>" not in par:
            raise SystemExit(f"RECUSADO: --trocar mal formado (use 'ANTIGO=>NOVO'): {par!r}")
        a, b = par.split("=>", 1)
        c = out.count(a)
        if c != 1:
            raise SystemExit(f"RECUSADO: âncora encontrada {c}x (esperado 1x): {a[:60]!r}")
        out = out.replace(a, b, 1)
    return out, antigo, novo, destino


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--data", default=datetime.date.today().isoformat())
    ap.add_argument("--base")
    ap.add_argument("--trocar", action="append", default=[])
    ap.add_argument("--ramo")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    base = a.base
    if base is None:
        r = subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"], capture_output=True, text=True)
        base = r.stdout.strip() or None
    try:
        out, antigo, novo, destino = planejar(root, a.data, base, a.trocar, a.ramo)
    except SystemExit as e:
        print(e, file=sys.stderr)
        return 2
    destino.parent.mkdir(parents=True, exist_ok=True)
    texto = (root / "HANDOFF.md").read_text(encoding="utf-8")
    if not destino.exists():
        destino.write_text(texto, encoding="utf-8")
    (root / "HANDOFF.md").write_text(out, encoding="utf-8")
    print(f"{antigo} -> {novo}; cópia em {destino.relative_to(root)}. Rode: python scripts/build_map.py && python scripts/check_handoff.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
