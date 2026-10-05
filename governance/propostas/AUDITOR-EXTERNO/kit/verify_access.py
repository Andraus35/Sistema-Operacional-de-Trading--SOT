#!/usr/bin/env python3
"""verify_access.py — falha (fail-closed) se a credencial do auditor tiver poder além de leitura/Issues.

[PROPOSTA — NÃO HOMOLOGADO] Token em SOT_AUDITOR_TOKEN (nunca por argumento). Não imprime o token.
Uso: python verify_access.py [--repo Andraus35/Sistema-Operacional-de-Trading--SOT]
"""
import argparse, json, os, sys, urllib.request, urllib.error


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", default="Andraus35/Sistema-Operacional-de-Trading--SOT")
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
        # Token do próprio dono (DHR-AUDITOR-EXTERNO-001 §acesso, 2026-10-05): `permissions` reflete o PAPEL do usuário, não o
        # escopo do token. Sonda não-mutante: POST git/blobs com corpo vazio -> 403 = token sem Contents:write (PASS);
        # 422/201 = escrita autorizada (FAIL).
        pr = urllib.request.Request(f"https://api.github.com/repos/{a.repo}/git/blobs", data=b"{}", method="POST",
                                    headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                                             "User-Agent": "sot-auditor-externo", "Content-Type": "application/json"})
        try:
            urllib.request.urlopen(pr, timeout=30); code = 201
        except urllib.error.HTTPError as e: code = e.code
        if code in (403, 404):
            print(f"INFO: papel do dono ({', '.join(bad)}), mas a sonda de escrita foi negada (HTTP {code}) — token sem Contents:write.")
        else:
            print(f"FAIL: credencial com poder de escrita (sonda HTTP {code}; papel: {', '.join(bad)}). Recrie o token só com Contents:Read + Issues:Read/Write."); return 1
    if not d.get("has_issues"): print("FAIL: Issues desabilitadas no repositório"); return 1
    print("PASS: leitura + sem escrita de código. (Escopo Issues:write do token não é verificável aqui; confirme na criação do token.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
