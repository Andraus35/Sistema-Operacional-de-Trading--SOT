#!/usr/bin/env python3
"""collect_repo_meta.py — M6: coleta metadados OBJETIVOS de um repositório pela API PÚBLICA do GitHub e gera um RASCUNHO de captura REPO-*.txt.

[PROPOSTA — NÃO HOMOLOGADO] Origem: governance/propostas/PESQUISA-ESPECIFICADOR/PROPOSTA-MELHORIA-PESQUISA.md (M6), "pacote equilibrado"
escolhido por Andraus (chat, 2026-10-06). Converte "NÃO CONFIRMADA por falta de acesso" em dado real (a SPEC-006 já provou o método com `pushed_at`).

É AUXILIAR, não gate (ENF-03): NÃO decide elegibilidade (RULE-ECC-06 é conferida por scripts/check_repo_research.py sobre a captura).
  - Só lê a API PÚBLICA: NUNCA envia token/credencial (nem o que houver no ambiente) — repositório privado = HTTP 404 = INDETERMINADO.
  - Resposta da API = DADO (nunca instrução). Registra o CAMPO-FONTE de cada número.
  - `Alertas de segurança graves abertos` é gravado como INDETERMINADO: a API pública não expõe alertas do Dependabot. Registrar "0" quando o
    dado é desconhecido (precedente SPEC-006: "registrado conservadoramente como 0") NÃO é conservador. Como a captura sai com esse campo não
    numérico, `check_repo_research.py` a trata como incompleta (fail-closed) até Andraus decidir o método — decisão registrada na PROPOSTA.
  - GitLab: fora do escopo desta versão (INDETERMINADO).

Uso:
    python scripts/collect_repo_meta.py owner/repo                 # imprime o rascunho
    python scripts/collect_repo_meta.py https://github.com/owner/repo --out specs/features/SPEC-0NN/sources/REPO-nome.txt
    python scripts/collect_repo_meta.py owner/repo --api-base http://127.0.0.1:PORTA --today AAAA-MM-DD   # (testes)
Exit 0 = rascunho gerado · 2 = não foi possível (privado/inexistente/GitLab/rede) — INDETERMINADO, nada é inventado.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_repo_research import MAX_COMMIT_AGE_DAYS, MIN_STARS, OPEN_LICENSES  # noqa: E402  (mesma régua, fonte única)

GITHUB = re.compile(r"^(?:https?://(?:www\.)?github\.com/)?([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?/?$", re.I)
GITLAB = re.compile(r"gitlab\.com", re.I)


def fetch(api_base: str, owner: str, repo: str, timeout: int = 20) -> dict:
    rq = urllib.request.Request(f"{api_base.rstrip('/')}/repos/{owner}/{repo}",
                                headers={"Accept": "application/vnd.github+json", "User-Agent": "sot-collect-repo-meta"})   # SEM Authorization
    with urllib.request.urlopen(rq, timeout=timeout) as r:
        data = json.load(r)
    if not isinstance(data, dict):
        raise ValueError("resposta da API não é um objeto JSON")
    return data


def build_capture(d: dict, api_base: str, today: date) -> str:
    owner_login = str((d.get("owner") or {}).get("login") or "").strip()
    owner_type = str((d.get("owner") or {}).get("type") or "").strip()
    lic = (d.get("license") or {}).get("spdx_id")
    stars = d.get("stargazers_count")
    pushed = str(d.get("pushed_at") or "")
    last = pushed[:10] if re.match(r"^\d{4}-\d{2}-\d{2}", pushed) else "INDETERMINADO"
    arch = d.get("archived")
    url = str(d.get("html_url") or "")
    desc = " ".join(str(d.get("description") or "").split())
    full = str(d.get("full_name") or "")

    # pré-avaliação MECÂNICA dos critérios verificáveis (não é veredito): mesma régua de check_repo_research.py
    notes = []
    notes.append(f"estrelas {stars} {'>=' if isinstance(stars, int) and stars >= MIN_STARS else '<'} {MIN_STARS}" if isinstance(stars, int) else "estrelas INDETERMINADO")
    lic_ok = isinstance(lic, str) and lic.strip().upper().replace(" ", "-") in OPEN_LICENSES
    notes.append(f"licença {lic or 'INDETERMINADO'} {'na lista de abertas' if lic_ok else 'FORA da lista de abertas conhecidas (ou NOASSERTION)'}")
    try:
        age = (today - datetime.strptime(last, "%Y-%m-%d").date()).days
        notes.append(f"último push há {age} dias ({'<=' if age <= MAX_COMMIT_AGE_DAYS else '>'} {MAX_COMMIT_AGE_DAYS})")
    except ValueError:
        notes.append("último push INDETERMINADO")
    notes.append("arquivado: " + ("sim" if arch is True else "não" if arch is False else "INDETERMINADO"))
    notes.append("alertas de segurança graves: INDETERMINADO (API pública não os expõe)")

    lines = [
        f"Repositório: {url}",
        "Plataforma: GitHub",
        f"URL: {url}",
        f"Data de acesso: {today.isoformat()}",
        f"Origem: API pública do GitHub (GET {api_base.rstrip('/')}/repos/{full}) em {today.isoformat()}; sem credencial; "
        "campos lidos: stargazers_count, license.spdx_id, pushed_at, archived, owner.login/type, description.",
        f"Estrelas: {stars if isinstance(stars, int) else 'INDETERMINADO'}   (campo stargazers_count)",
        f"Licença: {lic or 'INDETERMINADO'}   (campo license.spdx_id)",
        f"Último commit: {last}   (proxy: campo pushed_at = {pushed or 'ausente'}; data do último push observável, não necessariamente do último commit do branch default)",
        f"Arquivado: {'sim' if arch is True else 'não' if arch is False else 'INDETERMINADO'}   (campo archived)",
        "Alertas de segurança graves abertos: INDETERMINADO   (a API pública não expõe alertas do Dependabot; NÃO registrar 0 por suposição — "
        "decisão de método pendente de Andraus, RULE-ECC-06)",
        f"Dono: {owner_login or 'INDETERMINADO'} ({owner_type or 'tipo não informado'}{' — identificável' if owner_login else ''})",
        "Veredito de elegibilidade: PENDENTE — rascunho do coletor; o Especificador aplica a régua RULE-ECC-06 e check_repo_research.py a confere",
        "Pré-avaliação mecânica (NÃO é veredito): " + "; ".join(notes),
        "",
    ]
    if desc:
        lines += [f'Trecho literal (verbatim — campo "description" da API pública do GitHub, acesso {today.isoformat()}):', f'"{desc}"', ""]
    else:
        lines += ["Trecho literal: INDETERMINADO (a API não trouxe `description`); capture um trecho verbatim da página, se for citar.", ""]
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("repo", help="owner/repo ou URL https://github.com/owner/repo")
    ap.add_argument("--api-base", default="https://api.github.com")
    ap.add_argument("--today", default=None, help="AAAA-MM-DD (padrão: hoje; para testes)")
    ap.add_argument("--out", default=None, help="grava o rascunho neste arquivo (não sobrescreve existente)")
    a = ap.parse_args(argv)
    if GITLAB.search(a.repo):
        print("INDETERMINADO: GitLab fora do escopo desta versão do coletor (só GitHub).", file=sys.stderr); return 2
    m = GITHUB.match(a.repo.strip())
    if not m:
        print(f"INDETERMINADO: não reconheço '{a.repo}' como owner/repo do GitHub.", file=sys.stderr); return 2
    today = datetime.strptime(a.today, "%Y-%m-%d").date() if a.today else date.today()
    try:
        d = fetch(a.api_base, m.group(1), m.group(2))
    except urllib.error.HTTPError as e:
        print(f"INDETERMINADO: a API respondeu HTTP {e.code} (repositório privado/inexistente ou limite de taxa); nada foi inventado.", file=sys.stderr); return 2
    except (urllib.error.URLError, ValueError, OSError) as e:
        print(f"INDETERMINADO: não foi possível consultar a API ({type(e).__name__}); nada foi inventado.", file=sys.stderr); return 2
    text = build_capture(d, a.api_base, today)
    if a.out:
        out = Path(a.out)
        if out.exists():
            print(f"ABORTADO: {out} já existe (capturas não são sobrescritas — INV-07).", file=sys.stderr); return 2
        out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text, encoding="utf-8")
        print(f"rascunho gravado em {out}")
    else:
        print(text)
    print("LEMBRETE: rascunho, não veredito. Alertas = INDETERMINADO; exit 0 ≠ CONFORME ≠ homologação.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
