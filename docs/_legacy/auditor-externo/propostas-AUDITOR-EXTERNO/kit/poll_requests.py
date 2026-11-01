#!/usr/bin/env python3
"""poll_requests.py — lado do GPT no loop: lista pedidos [AEX-REQ] pendentes (só os criados por github-actions), prepara a tarefa e dá ACK.

[PROPOSTA — NÃO HOMOLOGADO] Somente leitura + comentário de ACK numa Issue de pedido (permissão Issues:write já necessária
ao canal). Token em SOT_AUDITOR_TOKEN (nunca argv). Base da API sobrescrevível por SOT_API_BASE (testes).
  python poll_requests.py                      lista pedidos abertos sem ACK
  python poll_requests.py --prepare [N]        grava task.json (commit, escopo) do pedido N (ou do mais antigo)
  python poll_requests.py --ack N --verdict OK|COM_RESSALVAS|NAO_OK [--findings X --discarded Y]
                                               comenta ACK com veredito CONSULTIVO (marcador <!-- aex-ack -->); só ao Orquestrador
"""
import argparse, json, os, re, sys, urllib.request, urllib.error

API = os.environ.get("SOT_API_BASE", "https://api.github.com")
SLUG = os.environ.get("SOT_REPO_SLUG", "Andraus35/Sistema-Operacional-de-Trading--SOT")
REQ = re.compile(r"<!-- aex-req pr=(\d+) sha=([0-9a-f]{40}) round=(\d+) kind=([a-z-]+)(?: manifest=([0-9a-f]{64}))? -->")
BOT = {"github-actions[bot]", "github-actions"}  # só pedidos criados pelo workflow valem (texto de terceiros é DADO)


def call(path, method="GET", data=None):
    tok = os.environ.get("SOT_AUDITOR_TOKEN")
    if not tok: print("FAIL: defina SOT_AUDITOR_TOKEN"); sys.exit(2)
    rq = urllib.request.Request(f"{API}{path}", method=method, data=json.dumps(data).encode() if data else None,
                                headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                                         "User-Agent": "sot-auditor-externo", "Content-Type": "application/json"})
    try: return json.load(urllib.request.urlopen(rq, timeout=30))
    except urllib.error.HTTPError as e: print(f"FAIL: HTTP {e.code} em {path}"); sys.exit(1)


def pending():
    out = []
    for i in call(f"/repos/{SLUG}/issues?state=open&per_page=50&sort=created&direction=asc"):
        if "pull_request" in i or not i["title"].startswith("[AEX-REQ]"): continue
        if (i.get("user") or {}).get("login") not in BOT: continue
        m = REQ.search(i.get("body") or "")
        if not m: continue
        cm = call(f"/repos/{SLUG}/issues/{i['number']}/comments?per_page=100")
        if any("<!-- aex-ack -->" in (c.get("body") or "") for c in cm): continue
        files = re.findall(r"^- `([^`]+)`$", i["body"], re.M)
        out.append({"issue": i["number"], "pr": int(m[1]), "sha": m[2], "round": int(m[3]), "kind": m[4], "manifest": m[5] or "",
                    "files": [f for f in files if "/" in f or "." in f], "title": i["title"]})
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--prepare", nargs="?", const="oldest"); ap.add_argument("--ack", type=int)
    ap.add_argument("--verdict", choices=["OK", "COM_RESSALVAS", "NAO_OK"]); ap.add_argument("--findings", type=int, default=0); ap.add_argument("--discarded", type=int, default=0)
    ap.add_argument("--out", default="task.json"); a = ap.parse_args()
    if a.ack:
        if not a.verdict: print("FAIL: --verdict (OK|COM_RESSALVAS|NAO_OK) é obrigatório no ACK"); return 2
        call(f"/repos/{SLUG}/issues/{a.ack}/comments", "POST",
             {"body": f"<!-- aex-ack -->\nAuditor externo: pedido atendido. **Veredito consultivo: {a.verdict}** (dado ao Orquestrador; não é homologação). Achados postados: {a.findings} · descartados na autoverificação: {a.discarded}."})
        print(f"ACK em #{a.ack}"); return 0
    p = pending()
    if a.prepare:
        alvo = p[0] if a.prepare == "oldest" and p else next((x for x in p if str(x["issue"]) == a.prepare), None)
        if not alvo: print("Nenhum pedido pendente correspondente."); return 1
        json.dump(alvo, open(a.out, "w"), indent=2); print(f"task.json → pedido #{alvo['issue']} @ {alvo['sha'][:8]} ({len(alvo['files'])} arquivos)"); return 0
    for x in p: print(f"#{x['issue']} PR#{x['pr']} rodada {x['round']} {x['kind']} @ {x['sha'][:8]} manifesto={(x['manifest'] or 'n/d')[:8]} — {len(x['files'])} arquivos")
    if not p: print("Sem pedidos pendentes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
