#!/usr/bin/env python3
"""loop_tools.py — lógica DETERMINÍSTICA e testável do loop de auditoria externa (usada pelo workflow).

[PROPOSTA — NÃO HOMOLOGADO] Nenhum LLM aqui. Entrada de Issue é DADO não confiável: nunca vai para shell.
Subcomandos:
  extract      --body-file F --out finding.json      extrai o 1º bloco ```json da Issue (limite 100 KB)
  meta         --finding finding.json                imprime baseline_commit (40 hex) ou erro
  fingerprint  --finding finding.json                impressão digital p/ deduplicar (caminho+linha+citação+tipo)
  request-body --pr N --sha SHA --files-file F --round R [--kind auditoria|re-auditoria] [--refs "1,2"]
  comment-body --report validation.json --fp FP [--dup N]
Exit 0 ok · 1 erro de dado · 2 uso.
"""
import argparse, hashlib, json, re, sys

MAX_BODY = 100_000
MAX_ROUNDS = 3        # rodadas de pedido por PR
MAX_OPEN_AEX = 25     # fila máxima de Issues [AEX] abertas (freio contra ping-pong)
FENCE = re.compile(r"```json\s*\n(.*?)\n```", re.S)
SHA = re.compile(r"^[0-9a-f]{40}$")


def cmd_extract(a):
    body = open(a.body_file, encoding="utf-8").read()
    if len(body.encode()) > MAX_BODY: print("ERRO: corpo da Issue excede 100 KB"); return 1
    m = FENCE.search(body)
    if not m: print("ERRO: nenhum bloco ```json encontrado no corpo"); return 1
    try: d = json.loads(m.group(1))
    except Exception as e: print(f"ERRO: JSON inválido ({e})"); return 1
    if not isinstance(d, dict): print("ERRO: JSON deve ser objeto"); return 1
    json.dump(d, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2); return 0


def _load(p):
    return json.load(open(p, encoding="utf-8"))


def cmd_meta(a):
    s = _load(a.finding).get("baseline_commit", "")
    if not (isinstance(s, str) and SHA.match(s)): print("ERRO: baseline_commit inválido"); return 1
    print(s); return 0


def fingerprint(f):
    ev = (f.get("evidence") or [{}])[0]
    q = re.sub(r"\s+", " ", str(ev.get("quote", ""))).strip()
    raw = "|".join([str(ev.get("path", "")), str(ev.get("line_start", "")), q, str((f.get("proposal") or {}).get("type", ""))])
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def cmd_fingerprint(a):
    print(fingerprint(_load(a.finding))); return 0


def cmd_request_body(a):
    if not SHA.match(a.sha): print("ERRO: sha inválido"); return 1
    files = [l.strip() for l in open(a.files_file, encoding="utf-8") if l.strip()]
    files = [x for x in files if not x.startswith("docs/mapa/")]  # saída gerada, fora do escopo de auditoria
    refs = [r.strip() for r in (a.refs or "").split(",") if r.strip().isdigit()]
    lista = "\n".join(f"- `{x}`" for x in files[:200]) or "- (nenhum arquivo auditável)"
    extra = f"\n\n**Achados em tratamento (Issues):** {', '.join('#'+r for r in refs)}" if refs else ""
    print(f"""<!-- aex-req pr={a.pr} sha={a.sha} round={a.round} kind={a.kind} -->
**Pedido de {a.kind} externa** — PR #{a.pr} · rodada {a.round}/{MAX_ROUNDS}

- Commit a auditar (fixe-o): `{a.sha}`
- Escopo (arquivos alterados, sem `docs/mapa/`):
{lista}{extra}

**Como atender (auditor externo, somente leitura):** `kit/poll_requests.py --prepare` → `kit/setup_auditor.sh {a.sha}` → `kit/run_gates.py` → audite → `kit/validate_finding.py` → `kit/submit_finding.py --post` → `kit/poll_requests.py --ack <nº desta Issue>`.

**Destinatário único: Orquestrador interno.** O auditor externo (em nuvem) lê a diretiva vigente (`DIRETIVAS-AO-AUDITOR.md`) e faz `git pull`/clone **somente deste commit**. Não menciona nem se reporta a terceiros.

_Gerado por workflow determinístico (nenhum LLM). Achado é **dado a verificar** pelo Orquestrador, que consulta Andraus e aciona Revisor/Especificador._""")
    return 0


def cmd_comment_body(a):
    r = _load(a.report)
    if a.dup:
        print(f"**DUPLICADO** de #{a.dup} (mesma citação/linha/tipo). Rotulado `aex-duplicado`; não entra em nova triagem.\n\n"
              f"<!-- aex-fp:{a.fp} -->"); return 0
    ok = r.get("pass")
    linhas = "\n".join(f"- {e}" for e in r.get("errors", [])) or "- (nenhum)"
    avis = "\n".join(f"- {w}" for w in r.get("warnings", []))
    bloco_avisos = ("Avisos:\n" + avis + "\n") if avis else ""
    veredito = "PASS" if ok else "FAIL"
    if ok:
        rodape = ("PASS = forma e ancoragem (citação literal no commit). **Não** é parecer de mérito nem homologação. "
                  "Próximo: o **Orquestrador** tria o achado, consulta Andraus e aciona o Revisor SOT (string-match), e registra a disposição "
                  "(`CONFIRMADO` · `PARCIAL` · `DESCARTADO` · `DUPLICADO`).")
    else:
        rodape = "Achado inválido: o auditor deve corrigir e postar **novo** achado (Issues não são editadas)."
    head = str(r.get("head", ""))[:12]
    print(f"**Validação determinística: {veredito}** @ `{head}` · achado `{r.get('finding_id')}`\n\n"
          f"Erros:\n{linhas}\n{bloco_avisos}\n{rodape}\n\n<!-- aex-fp:{a.fp} -->")
    return 0


def main():
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="c", required=True)
    e = sp.add_parser("extract"); e.add_argument("--body-file", required=True); e.add_argument("--out", required=True)
    for n in ("meta", "fingerprint"): sp.add_parser(n).add_argument("--finding", required=True)
    r = sp.add_parser("request-body")
    for k in ("pr", "sha", "files-file", "round"): r.add_argument(f"--{k}", required=True)
    r.add_argument("--kind", default="auditoria", choices=["auditoria", "re-auditoria"]); r.add_argument("--refs", default="")
    c = sp.add_parser("comment-body"); c.add_argument("--report", required=True); c.add_argument("--fp", required=True); c.add_argument("--dup")
    a = ap.parse_args()
    return {"extract": cmd_extract, "meta": cmd_meta, "fingerprint": cmd_fingerprint,
            "request-body": cmd_request_body, "comment-body": cmd_comment_body}[a.c](a)


if __name__ == "__main__":
    sys.exit(main())
