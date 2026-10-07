#!/usr/bin/env python3
"""auditor_bot.py — bot DETERMINÍSTICO que atende pedidos [AEX-REQ] com o Codex em modo somente-leitura (piloto).

[PROPOSTA — NÃO HOMOLOGADO] Desenho (docs: PROPOSTA-AUTOMACAO-B e ata DHR-AUDITOR-EXTERNO-003):
  - roda por agendador (systemd timer) DEPOIS de `~/.sot-audit/sync_auditor.sh` (âncora fora do repositório) sair com exit 0;
  - sem pedido pendente: termina sem chamar o modelo;
  - com pedido: prepara o commit auditado (setup_auditor.sh) e as evidências (run_gates.py), roda `codex exec` em
    sandbox READ-ONLY, SEM o token do GitHub no ambiente do modelo, e recebe só um bloco JSON de achados (DADO);
  - quem valida e publica é este código: preenche os campos de máquina, confere vazamento de segredos, valida cada achado
    (validate_finding via submit_finding), posta os que passam e dá o ACK com o veredito consultivo.
O modelo nunca escreve, nunca tem rede e nunca recebe token de escrita. Nenhuma decisão aqui: tudo é DADO para o Orquestrador.

Uso:  auditor_bot.py [--dry-run] [--request N]
  --dry-run   faz tudo, exceto postar achados e dar ACK (imprime o que faria)
Saída: 0 = nada a fazer ou atendido · 2 = bloqueio (registrado como nota no pedido, no máx. 1x por motivo).
Ambiente (todos opcionais): SOT_AUDIT_STATE, SOT_AUDIT_HOME, SOT_CODEX_CMD, SOT_SETUP_CMD, SOT_GATES_CMD, SOT_BOT_MAX_RUNS,
SOT_BOT_MAX_ATTEMPTS, SOT_CODEX_TIMEOUT, SOT_CODEX_MODEL_LABEL; SOT_AUDITOR_TOKEN, SOT_CONFIRMO_ESCOPO=1 (declaração de Andraus).
"""
import argparse, datetime, fcntl, json, os, re, shlex, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import poll_requests as pr  # noqa: E402  (mesmo kit, coberto pelo MANIFEST aprovado)
import loop_tools as lt     # noqa: E402

STATE = os.environ.get("SOT_AUDIT_STATE", os.path.expanduser("~/.sot-audit"))
WORK = os.environ.get("SOT_AUDIT_HOME", os.path.expanduser("~/sot-audit"))
CODEX = shlex.split(os.environ.get("SOT_CODEX_CMD", "codex"))
SETUP = shlex.split(os.environ.get("SOT_SETUP_CMD", f"bash {shlex.quote(os.path.join(HERE, 'setup_auditor.sh'))}"))
GATES = shlex.split(os.environ.get("SOT_GATES_CMD", f"{shlex.quote(sys.executable)} {shlex.quote(os.path.join(HERE, 'run_gates.py'))}"))
MAX_RUNS = int(os.environ.get("SOT_BOT_MAX_RUNS", "6"))          # chamadas ao modelo por dia (UTC)
MAX_ATTEMPTS = int(os.environ.get("SOT_BOT_MAX_ATTEMPTS", "2"))  # tentativas por pedido
TIMEOUT = int(os.environ.get("SOT_CODEX_TIMEOUT", "1800"))
MODEL_LABEL = os.environ.get("SOT_CODEX_MODEL_LABEL", "codex exec (modelo padrão do CLI instalado)")
MAX_FINDINGS = 10
VERDICTS = {"OK", "COM_RESSALVAS", "NAO_OK"}
TOKEN_RE = re.compile(r"(gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,})")


def log(msg):
    print(f"[{datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}] {msg}", flush=True)


def today():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")


def iso_today():
    return datetime.datetime.now(datetime.timezone.utc).date().isoformat()


def _read_json(path, default):
    try: return json.load(open(path, encoding="utf-8"))
    except Exception: return default


def _write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(obj, open(path, "w", encoding="utf-8"))


def redact(text, secrets):
    for s in secrets:
        if s: text = text.replace(s, "[REDIGIDO]")
    return TOKEN_RE.sub("[REDIGIDO]", text)


def note(issue, text, key, secrets, dry):
    """Comenta no pedido SEM marcador de ACK, no máximo 1x por (pedido, motivo)."""
    f = os.path.join(STATE, "notified.json"); n = _read_json(f, {})
    k = f"{issue}:{key}"
    if n.get(k): log(f"(nota já registrada: {k})"); return
    body = redact(f"Bot do auditor externo — **{text}**\n\n_Nota automática (dado ao Orquestrador); não é veredito nem ACK._", secrets)
    if dry: log(f"[dry-run] nota em #{issue}: {text}"); return
    try:
        pr.call(f"/repos/{pr.SLUG}/issues/{issue}/comments", "POST", {"body": body})
        n[k] = True; _write_json(f, n)
    except SystemExit:
        log("não foi possível registrar a nota (HTTP)")


def counter(name, delta=0):
    f = os.path.join(STATE, f"{name}-{today()}.count"); v = int(_read_json(f, 0)) + delta
    if delta: _write_json(f, v)
    return v


def attempts(issue, delta=0):
    f = os.path.join(STATE, "attempts.json"); a = _read_json(f, {}); k = str(issue)
    if delta: a[k] = a.get(k, 0) + delta; _write_json(f, a)
    return a.get(k, 0)


def secrets_list():
    out = []
    tok = os.environ.get("SOT_AUDITOR_TOKEN")
    if tok: out.append(tok)
    def walk(o):
        if isinstance(o, dict): [walk(v) for v in o.values()]
        elif isinstance(o, list): [walk(v) for v in o]
        elif isinstance(o, str) and len(o) >= 20: out.append(o)
    codex_home = os.path.join(STATE, "codex-home")
    for root, _, files in os.walk(codex_home):
        for fn in files:
            if fn == "auth.json": walk(_read_json(os.path.join(root, fn), {}))
    return out


def sh(cmd, env, cwd=None, timeout=None, stdin=None):
    return subprocess.run(cmd, cwd=cwd, env=env, input=stdin, capture_output=True, text=True, timeout=timeout)


def vigente_dir(repo):
    try: txt = open(os.path.join(repo, "governance/propostas/AUDITOR-EXTERNO/DIRETIVAS-AO-AUDITOR.md"), encoding="utf-8").read()
    except OSError: return None
    vig = re.findall(r"^## (DIR-\d{3})\s*\n+Status:\s*VIGENTE", txt, re.M)
    return vig[-1] if vig else None


def build_prompt(req, repo, dv):
    tpl = open(os.path.join(HERE, "PROMPT-AUDITOR-CI.md"), encoding="utf-8").read()
    files = "\n".join(f"  - `{f}`" for f in req["files"]) or "  - (nenhum arquivo auditável)"
    return (tpl.replace("{{SHA}}", req["sha"]).replace("{{DATE}}", iso_today())
               .replace("{{FILES}}", files).replace("{{DIRETIVA}}", dv or "DIR-???"))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--request", type=int)
    a = ap.parse_args(); dry = a.dry_run
    os.makedirs(STATE, exist_ok=True); os.chmod(STATE, 0o700)
    lock = open(os.path.join(STATE, "bot.lock"), "w")
    try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError: log("outra execução em andamento; saindo"); return 0
    if not os.environ.get("SOT_AUDITOR_TOKEN"): log("BLOQUEADO: SOT_AUDITOR_TOKEN ausente"); return 2
    secrets = secrets_list()

    try: p = pr.pending()
    except SystemExit: log("BLOQUEADO: falha ao consultar pedidos (API)"); return 2
    if a.request: p = [x for x in p if x["issue"] == a.request]
    if not p: log("Sem pedidos pendentes."); return 0
    req = p[0]; n = req["issue"]
    log(f"Pedido #{n} (PR #{req['pr']}) @ {req['sha'][:8]}, rodada {req['round']}")

    approved = ""
    try: approved = open(os.path.join(STATE, "approved_manifest.sha256")).read().strip()
    except OSError: pass
    if req["manifest"] and approved and req["manifest"] != approved:
        log("Pedido com manifesto diferente do aprovado (pedido desatualizado); ignorado.");
        note(n, "BLOQUEADO: pedido gerado com outro manifesto do kit que o aprovado neste bot (pedido desatualizado)", "manifesto", secrets, dry); return 2
    seen_f = os.path.join(STATE, "dryrun-seen.json"); seen = _read_json(seen_f, {}); seen_k = f"{n}:{req['sha']}"
    if dry and not a.request and seen.get(seen_k):
        log(f"Dry-run de #{n} @ {req['sha'][:8]} já foi feito; sem nova chamada ao modelo (use --request {n} para repetir)."); return 0
    if attempts(n) >= MAX_ATTEMPTS:
        log(f"Tentativas esgotadas para #{n}."); note(n, f"BLOQUEADO: {MAX_ATTEMPTS} tentativas esgotadas (decisão humana necessária)", "tentativas", secrets, dry); return 2
    if counter("runs") >= MAX_RUNS:
        log("Limite diário de chamadas ao modelo atingido."); return 0

    env = dict(os.environ, SOT_AUDIT_HOME=WORK, SOT_CONFIRMO_ESCOPO=os.environ.get("SOT_CONFIRMO_ESCOPO", ""))
    repo = os.path.join(WORK, "repo"); evidence = os.path.join(WORK, "evidence.json")
    r = sh(SETUP + [req["sha"]], env, timeout=1800)
    if r.returncode != 0:
        log("setup falhou:\n" + redact((r.stdout + r.stderr)[-800:], secrets))
        note(n, "BLOQUEADO: preparo do commit auditado/calibração falhou (setup_auditor)", "setup", secrets, dry); return 2
    r = sh(GATES + ["--repo", repo, "--out", evidence], env, timeout=1800)
    if r.returncode != 0 or not os.path.exists(evidence):
        log("gates falharam:\n" + redact((r.stdout + r.stderr)[-800:], secrets))
        note(n, "BLOQUEADO: execução dos gates determinísticos falhou (run_gates)", "gates", secrets, dry); return 2
    head = sh(["git", "-C", repo, "rev-parse", "HEAD"], env).stdout.strip()
    if head != req["sha"]:
        log(f"HEAD do clone {head[:8]} ≠ SHA do pedido {req['sha'][:8]}"); note(n, "BLOQUEADO: commit preparado difere do pedido", "head", secrets, dry); return 2
    dv = vigente_dir(repo)
    if not dv: note(n, "BLOQUEADO: nenhuma diretiva VIGENTE no commit auditado", "diretiva", secrets, dry); return 2

    # --- modelo: read-only, sem rede (sandbox), SEM token do GitHub no ambiente
    cenv = {k: v for k, v in os.environ.items() if not k.startswith(("SOT_", "GIT_CONFIG", "GITHUB_", "GH_"))}
    cenv["CODEX_HOME"] = os.path.join(STATE, "codex-home"); cenv["HOME"] = os.environ.get("HOME", STATE)
    out_file = os.path.join(WORK, "codex-last-message.txt")
    if os.path.exists(out_file): os.remove(out_file)
    counter("runs", 1)
    if not dry: attempts(n, 1)   # dry-run não gasta tentativas do pedido
    cmd = CODEX + ["exec", "--sandbox", "read-only", "--ephemeral", "--skip-git-repo-check", "--ignore-user-config",
                   "--ignore-rules", "--cd", repo, "-o", out_file, "-"]
    log("Chamando o modelo (read-only, sem token no ambiente)...")
    try: r = sh(cmd, cenv, cwd=repo, timeout=TIMEOUT, stdin=build_prompt(req, repo, dv))
    except subprocess.TimeoutExpired:
        note(n, f"BLOQUEADO: o modelo excedeu {TIMEOUT}s", "timeout", secrets, dry); return 2
    except FileNotFoundError:
        note(n, "BLOQUEADO: comando do Codex não encontrado no bot", "codex-ausente", secrets, dry); return 2
    raw = open(out_file, encoding="utf-8").read() if os.path.exists(out_file) else (r.stdout or "")
    if r.returncode != 0 and not raw.strip():
        log("codex exec falhou:\n" + redact((r.stderr or "")[-800:], secrets))
        note(n, "BLOQUEADO: o Codex terminou com erro e sem resposta", "codex-erro", secrets, dry); return 2

    # --- vazamento: nenhuma saída que contenha segredo é usada ou publicada
    if any(s and s in raw for s in secrets) or TOKEN_RE.search(raw):
        if not dry: attempts(n, MAX_ATTEMPTS)  # trava novas tentativas (só fora do dry-run)
        log("SEGURANÇA: a saída do modelo contém algo parecido com segredo; descartada.")
        note(n, "BLOQUEADO (segurança): a saída do modelo continha material parecido com segredo e foi descartada; revisar e rotacionar credenciais", "vazamento", secrets, dry); return 2

    m = lt.FENCE.search(raw)
    try: data = json.loads(m.group(1)) if m and len(raw.encode()) <= lt.MAX_BODY else None
    except Exception: data = None
    if not (isinstance(data, dict) and data.get("veredito") in VERDICTS and isinstance(data.get("achados"), list)):
        log("saída fora do formato esperado")
        note(n, "BLOQUEADO: a saída do modelo não seguiu o formato (bloco JSON com veredito e achados)", "formato", secrets, dry); return 2

    lim = data.get("limitacao")   # o modelo declarou que NÃO conseguiu auditar (ex.: sandbox sem leitura) -> sem ACK nem achados
    if isinstance(lim, str) and re.search(r"INDETERMINADO|auditoria n[ãa]o realizada", lim, re.I):
        log("o modelo declarou a auditoria como não realizada: " + redact(lim[:300], secrets))
        note(n, "BLOQUEADO: o modelo declarou que não conseguiu realizar a auditoria (limitação de leitura/ambiente); sem ACK. Ver o log do bot", "indeterminado", secrets, dry); return 2

    posted = discarded = 0
    valid_sev = []   # gravidades dos achados que PASSARAM na validação (base do veredito derivado)
    for raw_f in data["achados"][:MAX_FINDINGS]:
        if not isinstance(raw_f, dict): discarded += 1; continue
        seq = counter("ids", 1)
        f = dict(raw_f)
        f.update({"schema_version": "1.0", "id": f"AEX-{today()}-{seq:03d}", "baseline_commit": req["sha"],
                  "author": {"model": MODEL_LABEL, "date": iso_today()},
                  "directive_version": dv, "gate_evidence_ref": None})
        f.setdefault("treats_open_decision_as_closed", False)
        fdir = os.path.join(WORK, "findings"); os.makedirs(fdir, exist_ok=True)
        fpath = os.path.join(fdir, f"{f['id']}.json"); json.dump(f, open(fpath, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        sub = [sys.executable, os.path.join(HERE, "submit_finding.py"), "--repo-dir", repo, "--finding", fpath, "--evidence", evidence, "--slug", pr.SLUG]
        if not dry: sub.append("--post")
        r = sh(sub, env, timeout=300)
        tail = redact((r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else "", secrets)
        if r.returncode == 0: posted += 1; valid_sev.append(f.get("severity")); log(f"achado {f['id']}: {'DRY-RUN ok' if dry else 'POSTADO'} — {tail}")
        else: discarded += 1; log(f"achado {f['id']}: DESCARTADO — {tail}")
    # Veredito = função DETERMINÍSTICA dos achados válidos (ENF-03: o LLM não é o próprio gate); o do modelo é só dado comparado.
    if posted == 0 and discarded > 0:   # decisão de Andraus: tudo descartado => bloquear, sem nota nem ACK (evita OK por derivação vazia)
        log(f"BLOQUEIO: o modelo apontou {discarded} problema(s) e todos foram descartados na validação; sem nota.")
        note(n, f"BLOQUEADO: o modelo apontou {discarded} problema(s), mas nenhum passou na validação determinística (forma/citação); sem nota nem ACK. Nova tentativa dentro do limite", "tudo-descartado", secrets, dry); return 2
    model_verdict = data["veredito"]
    verdict = lt.derive_verdict(valid_sev)
    log(f"Resumo: postados={posted} descartados={discarded} veredito={verdict} (modelo: {model_verdict})")
    if dry:
        seen[seen_k] = True; _write_json(seen_f, seen); log("[dry-run] sem ACK."); return 0
    diverg = (f" Veredito do modelo: {model_verdict} — **diverge** do calculado pelo código a partir dos achados válidos (registrado como dado)."
              if model_verdict != verdict else f" Veredito do modelo: {model_verdict} (coincide com o calculado).")
    pr.call(f"/repos/{pr.SLUG}/issues/{n}/comments", "POST",
            {"body": f"<!-- aex-ack -->\nAuditor externo (bot): pedido atendido. **Veredito consultivo: {verdict}** (calculado por código a partir dos achados válidos; "
                     f"dado ao Orquestrador; não é homologação). Achados postados: {posted} · descartados na autoverificação: {discarded}.{diverg}"})
    log(f"ACK em #{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
