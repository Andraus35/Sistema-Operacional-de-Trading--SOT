#!/usr/bin/env python3
"""submit_finding.py — posta UM achado validado como Issue [AEX] (caixa de entrada do Orquestrador; canal decidido por Andraus, 2026-10-05).

[PROPOSTA — NÃO HOMOLOGADO] Padrão = DRY-RUN (só imprime). Para postar: --post. Recusa se: validação FALHAR,
evidence.json ausente/de outro commit, ou credencial tiver push/admin. Token em SOT_AUDITOR_TOKEN (nunca argv).
O auditor NÃO escreve em arquivo do repositório; a Issue é o único canal de saída.
"""
import argparse, json, os, subprocess, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-dir", required=True); ap.add_argument("--finding", required=True)
    ap.add_argument("--evidence", required=True); ap.add_argument("--slug", default="Andraus35/Sistema-Operacional-de-Trading--SOT")
    ap.add_argument("--post", action="store_true")
    a = ap.parse_args()
    rep = os.path.join(os.path.dirname(os.path.abspath(a.finding)), "validation.json")
    rc = subprocess.run([sys.executable, os.path.join(HERE, "validate_finding.py"), "--repo", a.repo_dir,
                         "--finding", a.finding, "--json-out", rep]).returncode
    if rc != 0: print("ABORTADO: achado não passou na validação determinística."); return 1
    f = json.load(open(a.finding, encoding="utf-8")); ev = json.load(open(a.evidence, encoding="utf-8"))
    if ev.get("repo_commit") != f["baseline_commit"]:
        print("ABORTADO: evidence.json é de outro commit que o do achado."); return 1
    red = [g["name"] for g in ev["gates"] if g["exit_code"] != 0 and not g["informative"]]
    body = (f"**{f['severity']} · {f['type']}** — baseline `{f['baseline_commit']}`\n\n{f['claim']}\n\n"
            f"### Proposta (DADO — não é ordem)\n`{f['proposal']['type']}` · modifica texto baselined: "
            f"{f['proposal']['modifies_baselined_text']}\n\n{f['proposal']['text']}\n\n"
            f"### Evidência literal\n" + "\n".join(f"- `{e['path']}:{e['line_start']}-{e['line_end']}` — “{e['quote']}”" for e in f["evidence"]) +
            f"\n\n### Gates determinísticos no commit auditado\nVermelhos (não informativos): {red or 'nenhum'}\n\n"
            f"### Achado (JSON canônico)\n```json\n{json.dumps(f, ensure_ascii=False, indent=2)}\n```\n\n"
            f"---\n_Auditor externo (somente leitura). Validador determinístico: PASS = forma/ancoragem, não mérito. "
            f"Destinatário único: Orquestrador interno._")
    title = f"[AEX] {f['id']} {f['severity']} — {f['title']}"
    if not a.post:
        print("DRY-RUN\nTÍTULO:", title, "\n\n" + body); return 0
    tok = os.environ.get("SOT_AUDITOR_TOKEN")
    if not tok: print("ABORTADO: defina SOT_AUDITOR_TOKEN"); return 2
    if subprocess.run([sys.executable, os.path.join(HERE, "verify_access.py"), "--repo", a.slug]).returncode != 0:
        print("ABORTADO: credencial não é somente-leitura."); return 1
    rq = urllib.request.Request(f"https://api.github.com/repos/{a.slug}/issues", method="POST",
                                data=json.dumps({"title": title, "body": body}).encode(),
                                headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                                         "User-Agent": "sot-auditor-externo", "Content-Type": "application/json"})
    try: r = json.load(urllib.request.urlopen(rq, timeout=30))
    except urllib.error.HTTPError as e: print(f"FALHOU: HTTP {e.code}"); return 1
    print("Issue criada:", r["html_url"]); return 0


if __name__ == "__main__":
    sys.exit(main())
