#!/usr/bin/env python3
"""verify_access.py — falha (fail-closed) se a credencial do auditor tiver poder além de leitura/Issues.

[PROPOSTA — NÃO HOMOLOGADO] Token em SOT_AUDITOR_TOKEN (nunca por argumento). Não imprime o token.
Uso: python verify_access.py [--repo Andraus35/Sistema-Operacional-de-Trading--SOT]
"""
import argparse, json, os, sys, urllib.request, urllib.error


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", default="Andraus35/Sistema-Operacional-de-Trading--SOT")
    ap.add_argument("--confirmo-escopo", action="store_true", help="declaro ter conferido o escopo do token no GitHub (token do dono)")
    a = ap.parse_args(); tok = os.environ.get("SOT_AUDITOR_TOKEN")
    if not tok: print("FAIL: defina SOT_AUDITOR_TOKEN"); return 2
    rq = urllib.request.Request(f"https://api.github.com/repos/{a.repo}",
                                headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                                         "User-Agent": "sot-auditor-externo"})
    try: d = json.load(urllib.request.urlopen(rq, timeout=30))
    except urllib.error.HTTPError as e: print(f"FAIL: HTTP {e.code} (token sem acesso ao repositório?)"); return 1
    p = d.get("permissions", {}); bad = [k for k in ("admin", "maintain", "push") if p.get(k)]
    print(f"repo={d['full_name']} private={d['private']} pull={p.get('pull')} triage={p.get('triage')} push={p.get('push')}")
    if not p.get("pull"): print("FAIL: sem leitura"); return 1
    if bad:
        # Token do próprio dono (DHR-AUDITOR-EXTERNO-001, emenda de acesso 2026-10-05): `permissions` reflete o PAPEL do usuário,
        # não o escopo do token, e NÃO existe sonda confiável do escopo (duas tentativas contra a API real deram falso positivo:
        # POST vazio -> 422; POST de blob válido -> 201 mesmo com Contents Read-only na tela do GitHub). O escopo é declarado
        # e conferido no GitHub (Settings > Developer settings > Fine-grained tokens). Fail-closed: sem --confirmo-escopo, FAIL.
        if not a.confirmo_escopo:
            print(f"INDETERMINADO: papel do dono ({', '.join(bad)}); o escopo do token não é verificável pela API. "
                  "Confira no GitHub (Contents=Read-only, Issues=Read and write, Metadata=Read-only, só este repositório) "
                  "e rode de novo com --confirmo-escopo."); return 1
        print("INFO: escopo do token CONFIRMADO MANUALMENTE (não verificado pela API).")
    if not d.get("has_issues"): print("FAIL: Issues desabilitadas no repositório"); return 1
    print("PASS: leitura; escopo conforme declarado. (Escopo Issues:write do token não é verificável aqui; confirme na criação do token.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
