import json, re, subprocess, sys
repo = "Andraus35/Sistema-Operacional-de-Trading--SOT"
out, nums = sys.argv[1], [int(n) for n in sys.argv[2:]]
res = []
for n in nums:
    body = subprocess.run(["gh", "issue", "view", str(n), "--repo", repo, "--json", "body", "--jq", ".body"],
                          capture_output=True, text=True, encoding="utf-8").stdout
    m = re.search(r"```json\s*(\{.*?\})\s*```", body, re.S)
    if m:
        f = json.loads(m.group(1))
        res.append({"issue": n, "evidence": f.get("evidence", [])})
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(out, "achados:", len(res), "evidencias:", sum(len(r["evidence"]) for r in res))
