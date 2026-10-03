#!/usr/bin/env python3
"""Gate determinístico da RULE-ECC-06 — Pesquisa em repositórios seguros e bem avaliados.

Andraus (chat, 2026-10-03, DHR-ECC06-001): o Dossiê de Pesquisa de toda Spec nova passa a
exigir pesquisa de melhores práticas em repositórios (GitHub/GitLab) APENAS dos que forem
"seguros e de melhor avaliação" pela régua EQUILIBRADA abaixo. O que NÃO atende é descartado e
registrado como NÃO ELEGÍVEL (nunca adotado/adaptado). Se nenhum atender, o Dossiê registra
"nenhum repositório elegível" — resultado válido (pesquisa inconclusiva = INDETERMINADO).

O script confere a ESTRUTURA e a RÉGUA sobre as capturas companheiras
(specs/features/SPEC-0NN/sources/REPO-*.txt). Ele NÃO verifica a veracidade dos números
(sem web — mesmo mandato do Revisor, ENF-03): os números vêm da captura mediada pelo
Especificador (RULE-ECC-04) e o Revisor audita por string. É Gate estrutural, não CONFORME.

Formato da captura (sources/REPO-<id>.txt), uma por repositório citado:
    Repositório: https://github.com/owner/repo
    Plataforma: GitHub | GitLab
    Data de acesso: AAAA-MM-DD
    Estrelas: 1234
    Licença: MIT
    Último commit: AAAA-MM-DD
    Arquivado: não
    Alertas de segurança graves abertos: 0
    Dono: owner (pessoa/organização identificável)
    Veredito de elegibilidade: ELEGÍVEL | NÃO ELEGÍVEL
    Trecho literal: "..." (≥100 caracteres, RULE-ECC-04)

Uso:
    python scripts/check_repo_research.py specs/features/SPEC-004     # uma pasta de Spec
    python scripts/check_repo_research.py --all                        # todas (menos grandfathered)
Exit 0 = ok · 1 = reprovado.
"""
from __future__ import annotations

import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Specs anteriores à RULE-ECC-06 (prospectiva — INV-07, sem reescrita retroativa).
GRANDFATHERED = {
    "SPEC-001", "SPEC-002", "SPEC-003", "SPEC-019", "SPEC-020", "SPEC-021",
    "SPEC-038", "SPEC-046",
}

# Régua EQUILIBRADA (Andraus, 2026-10-03).
MIN_STARS = 300
MAX_COMMIT_AGE_DAYS = 365
OPEN_LICENSES = {
    "MIT", "APACHE-2.0", "BSD-2-CLAUSE", "BSD-3-CLAUSE", "ISC", "MPL-2.0",
    "LGPL-2.1", "LGPL-3.0", "GPL-2.0", "GPL-3.0", "AGPL-3.0", "UNLICENSE", "CC0-1.0",
}

REPO_URL = re.compile(
    r"https?://(?:www\.)?(github\.com|gitlab\.com)/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", re.I
)
SECTION_HEAD = re.compile(r"^(#{1,6})\s+.*pesquisa\s+em\s+reposit[óo]rios", re.I | re.M)
NONE_ELIGIBLE = re.compile(r"nenhum\s+reposit[óo]rio\s+(eleg[íi]vel|atende)", re.I)
ADOPT = re.compile(r"\b(adotar|adaptar)\b", re.I)

FIELD_PATTERNS = {
    "url": r"^Reposit[óo]rio\s*:\s*(\S+)",
    "plataforma": r"^Plataforma\s*:\s*(.+)",
    "acesso": r"^Data de acesso\s*:\s*(\d{4}-\d{2}-\d{2})",
    "estrelas": r"^(?:Estrelas|Stars)\s*:\s*([\d.,]+)",
    "licenca": r"^(?:Licen[çc]a|License)\s*:\s*(.+)",
    "ultimo_commit": r"^(?:[ÚU]ltimo commit|Last commit)\s*:\s*(\d{4}-\d{2}-\d{2})",
    "arquivado": r"^(?:Arquivado|Archived)\s*:\s*(.+)",
    "alertas": r"^Alertas de seguran[çc]a graves abertos\s*:\s*(\d+)",
    "dono": r"^(?:Dono|Owner)\s*:\s*(.+)",
    "veredito": r"^Veredito de elegibilidade\s*:\s*(.+)",
}


def norm_url(url: str) -> str:
    m = REPO_URL.search(url.strip())
    if not m:
        return url.strip().lower()
    host, owner, repo = m.group(1).lower(), m.group(2).lower(), m.group(3).lower()
    repo = re.sub(r"\.git$", "", repo).rstrip(".")
    return f"{host}/{owner}/{repo}"


def parse_capture(text: str) -> dict:
    meta: dict = {}
    for key, pat in FIELD_PATTERNS.items():
        m = re.search(pat, text, re.I | re.M)
        if m:
            meta[key] = m.group(1).strip()
    return meta


def _d(s: str) -> date | None:
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def evaluate(meta: dict) -> tuple[bool, list[str]]:
    """Aplica a régua equilibrada. Retorna (elegível, motivos de reprovação)."""
    why: list[str] = []
    missing = [k for k in ("url", "acesso", "estrelas", "licenca", "ultimo_commit",
                           "arquivado", "alertas", "dono") if k not in meta]
    if missing:
        return False, [f"campo(s) ausente(s) na captura: {', '.join(missing)}"]
    try:
        stars = int(re.sub(r"[.,]", "", meta["estrelas"]))
    except ValueError:
        stars = -1
    if stars < MIN_STARS:
        why.append(f"estrelas {meta['estrelas']} < {MIN_STARS}")
    lic = meta["licenca"].strip().upper().replace(" ", "-")
    if lic not in OPEN_LICENSES:
        why.append(f"licença '{meta['licenca']}' fora da lista de licenças abertas conhecidas")
    acc, last = _d(meta["acesso"]), _d(meta["ultimo_commit"])
    if not acc or not last:
        why.append("data de acesso/último commit inválida (AAAA-MM-DD)")
    elif (acc - last).days > MAX_COMMIT_AGE_DAYS:
        why.append(f"último commit há {(acc - last).days} dias (> {MAX_COMMIT_AGE_DAYS})")
    if not re.match(r"^(n[ãa]o|no|false)\b", meta["arquivado"].strip(), re.I):
        why.append("repositório arquivado")
    if int(meta["alertas"]) != 0:
        why.append(f"{meta['alertas']} alerta(s) de segurança grave(s) aberto(s)")
    if len(meta["dono"].strip()) < 2:
        why.append("dono não identificável")
    return (not why), why


def _section(text: str) -> str | None:
    m = SECTION_HEAD.search(text)
    if not m:
        return None
    level = len(m.group(1))
    rest = text[m.end():]
    nxt = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    return text[m.start(): m.end() + (nxt.start() if nxt else len(rest))]


def check_spec_folder(folder: Path) -> tuple[bool, str]:
    research = folder / "research.md"
    if not research.exists():
        return False, "research.md (Dossiê de Pesquisa) ausente"
    text = research.read_text(encoding="utf-8", errors="replace")
    sec = _section(text)
    if sec is None:
        return False, (
            "RULE-ECC-06: o Dossiê não tem a seção 'Pesquisa em repositórios' "
            "(GitHub/GitLab — só repositórios seguros e bem avaliados; régua equilibrada)."
        )
    urls = {}
    for m in REPO_URL.finditer(sec):
        urls.setdefault(norm_url(m.group(0)), m.group(0))
    captures: dict[str, tuple[Path, dict]] = {}
    for f in sorted((folder / "sources").glob("REPO-*.txt")) if (folder / "sources").exists() else []:
        meta = parse_capture(f.read_text(encoding="utf-8", errors="replace"))
        if "url" in meta:
            captures[norm_url(meta["url"])] = (f, meta)

    errors: list[str] = []
    eligible_count = 0
    verdicts: dict[str, bool] = {}
    for key, raw in urls.items():
        if key not in captures:
            errors.append(f"{raw}: sem captura sources/REPO-*.txt (RULE-ECC-04/06)")
            continue
        f, meta = captures[key]
        ok, why = evaluate(meta)
        verdicts[key] = ok
        declared = meta.get("veredito", "").strip().upper().replace("Í", "I")
        declared_ok = declared.startswith("ELEGIVEL")
        declared_bad = declared.startswith("NAO ELEGIVEL") or declared.startswith("NÃO ELEGIVEL")
        if not (declared_ok or declared_bad):
            errors.append(f"{f.name}: 'Veredito de elegibilidade' ausente ou inválido")
        elif declared_ok != ok:
            errors.append(
                f"{f.name}: veredito declarado ({'ELEGÍVEL' if declared_ok else 'NÃO ELEGÍVEL'}) "
                f"diverge da régua ({'ELEGÍVEL' if ok else 'NÃO ELEGÍVEL: ' + '; '.join(why)})"
            )
        if ok:
            eligible_count += 1
    # Repositório não elegível jamais é adotado/adaptado.
    for line in sec.splitlines():
        for m in REPO_URL.finditer(line):
            key = norm_url(m.group(0))
            if verdicts.get(key) is False and ADOPT.search(line) and not re.search(
                r"n[ãa]o\s+(adotar|adaptar)|descart|n[ãa]o\s+eleg", line, re.I
            ):
                errors.append(f"{m.group(0)}: NÃO ELEGÍVEL pela régua, mas a linha adota/adapta")
    if eligible_count == 0 and not NONE_ELIGIBLE.search(sec):
        errors.append(
            "nenhum repositório elegível citado e a seção não declara 'nenhum repositório "
            "elegível' (resultado válido, mas precisa ser explícito)"
        )
    if errors:
        return False, " | ".join(errors)
    return True, ""


def spec_folders() -> list[Path]:
    base = ROOT / "specs" / "features"
    return sorted(p for p in base.glob("SPEC-*") if p.is_dir() and p.name not in GRANDFATHERED)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 1
    targets = spec_folders() if argv[1] == "--all" else [Path(a) for a in argv[1:]]
    bad = 0
    print("VERIFICADOR RULE-ECC-06 — pesquisa em repositórios seguros e bem avaliados")
    for t in targets:
        if t.name in GRANDFATHERED:
            print(f"  [skip] {t.name} (anterior à RULE-ECC-06 — grandfathered)")
            continue
        ok, msg = check_spec_folder(t)
        print(f"  [{'OK' if ok else 'FAIL'}] {t.name}" + ("" if ok else f" — {msg}"))
        bad += 0 if ok else 1
    print(f"ERRO={bad}")
    print("LEMBRETE: gate estrutural; não verifica a veracidade dos números (sem web — ENF-03). exit 0 ≠ CONFORME.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
