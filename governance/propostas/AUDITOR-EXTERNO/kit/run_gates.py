#!/usr/bin/env python3
"""run_gates.py — executa os gates DETERMINÍSTICOS existentes do SOT e grava evidence.json.

[PROPOSTA — NÃO HOMOLOGADO] O LLM nunca é o próprio gate (ENF-03): os gates são os scripts do repositório;
este runner só os executa, registra commit, exit codes e hash da saída. Somente leitura: falha se a árvore
de trabalho mudar. Uso: python run_gates.py --repo <clone> --out evidence.json
"""
import argparse, glob, hashlib, json, os, platform, subprocess, sys, datetime

INFORMATIVOS = {"check_refs", "check_doc_sync", "backlog_triggers"}  # espelham 'informative' do ci.yml


def run(repo, name, cmd, env):
    p = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, env=env)
    out = (p.stdout or "") + (p.stderr or "")
    return {"name": name, "cmd": " ".join(cmd), "exit_code": p.returncode,
            "informative": name.split(":")[0] in INFORMATIVOS,
            "output_sha256": hashlib.sha256(out.encode()).hexdigest(),
            "tail": out.strip().splitlines()[-4:]}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", required=True); ap.add_argument("--out", default="evidence.json")
    a = ap.parse_args(); repo = os.path.abspath(a.repo)
    g = lambda *x: subprocess.run(["git", "-C", repo, *x], capture_output=True, text=True).stdout.strip()
    head = g("rev-parse", "HEAD")
    if g("status", "--porcelain"): print("FAIL: árvore de trabalho suja antes dos gates"); return 2
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    py = sys.executable
    gates = [("npm_test", ["npm", "test"]), ("npm_lint", ["npm", "run", "lint"]),
             ("check_refs", [py, "scripts/check_refs.py"]), ("check_doc_sync", [py, "scripts/check_doc_sync.py"]),
             ("build_map_check", [py, "scripts/build_map.py", "--check"]),
             ("check_repo_research", [py, "scripts/check_repo_research.py", "--all"])]
    for plan in sorted(glob.glob(os.path.join(repo, "specs/features/*/plan.md"))):
        rel = os.path.relpath(plan, repo)
        gates.append((f"validate_spec_sot:{rel.split('/')[2]}", [py, "scripts/validate_spec_sot.py", rel]))
    res = [run(repo, n, c, env) for n, c in gates]
    if g("status", "--porcelain"): print("FAIL: os gates alteraram a árvore (auditoria deve ser somente leitura)"); return 2
    ev = {"schema_version": "1.0", "repo_commit": head, "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "python": platform.python_version(), "gates": res,
          "nota": "exit_code 0 em gate informativo/estrutural ≠ CONFORME ≠ homologação (SPECIFIED ≠ IMPLEMENTED ≠ PROVEN)"}
    json.dump(ev, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    for r in res: print(f"{'OK ' if r['exit_code']==0 else 'RED'} {r['name']}{' (informativo)' if r['informative'] else ''}")
    print(f"evidence.json @ {head[:8]} → {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
