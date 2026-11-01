import subprocess, re, json, sys, os, shutil, tempfile
REPO = sys.argv[1]; N = int(sys.argv[2]); OUT = sys.argv[3]
DET = {"check_refs": ["scripts/check_refs.py"], "check_doc_sync": ["scripts/check_doc_sync.py"],
       "check_coesao": ["scripts/check_coesao.py"], "check_invariants": ["scripts/check_invariants.py"],
       "check_handoff": ["scripts/check_handoff.py"], "check_rpsa": ["scripts/check_rpsa.py"],
       "gate_manifest": ["scripts/gate_manifest.py", "--check"]}
g = lambda *a, cwd=REPO: subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True).stdout.strip()
commits = g("rev-list", "--first-parent", f"-n{N}", "origin/main").split()
rows = []
for c in reversed(commits):
    wt = tempfile.mkdtemp(prefix="wt-")
    subprocess.run(["git", "worktree", "add", "--detach", "-f", wt, c], cwd=REPO, capture_output=True)
    row = {"commit": c[:7], "data": g("log", "-1", "--format=%cs", c)}
    for name, cmd in DET.items():
        if not os.path.exists(os.path.join(wt, cmd[0])):
            row[name] = "ausente"; continue
        try:
            p = subprocess.run([sys.executable, "-B", *cmd], cwd=wt, capture_output=True, text=True, timeout=120)
            out = (p.stdout or "") + (p.stderr or "")
            m = re.search(r"ERRO=(\d+) WARN=(\d+)(?: INFO=(\d+))?", out)
            row[name] = f"E{m.group(1)}W{m.group(2)}" if m else f"exit{p.returncode}"
        except subprocess.TimeoutExpired:
            row[name] = "timeout"
    subprocess.run(["git", "worktree", "remove", "--force", wt], cwd=REPO, capture_output=True)
    rows.append(row)
    json.dump(rows, open(OUT, "w"), ensure_ascii=False, indent=1)
print("fim", len(rows))
