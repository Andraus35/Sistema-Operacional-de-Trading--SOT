#!/usr/bin/env python3
"""medir_leituras.py — artefato de PROPOSTA (nao e mecanismo, nao roda no CI): conta, nas transcricoes de subagentes de UMA sessao,
quanto de cada arquivo-nucleo foi lido (Read inteiro/parcial ou Grep) e quantos bytes de resultado cada agente consumiu.
Uso: python medir_leituras.py <pasta com agent-*.jsonl e agent-*.meta.json>. Somente leitura. Limite: so ve resultados de ferramentas,
nao o prompt injetado; tokens = bytes/4 (estimativa)."""
import glob, json, os, sys
ALVOS = {"RMR-001": "backlog/RMR-001_Painel_Backlog.md", "ROADMAP": "ROADMAP.md", "atomic-spec": "atomic-spec.md", "RULES": "governance/RULES.md",
         "CATALOGO": "governance/CATALOGO-OFICIAL.md", "MECANISMOS": "governance/MECANISMOS.json"}
def texto(c): return c if isinstance(c, str) else "".join(x.get("text", "") for x in (c or []) if isinstance(x, dict))
def main(pasta):
    for f in sorted(glob.glob(os.path.join(pasta, "agent-*.jsonl"))):
        mf = f.replace(".jsonl", ".meta.json"); meta = json.load(open(mf)) if os.path.exists(mf) else {}
        usos, lidos, total, n = {}, {}, 0, 0
        for l in open(f, encoding="utf-8"):
            if not l.strip(): continue
            c = (json.loads(l).get("message") or {}).get("content")
            if not isinstance(c, list): continue
            for b in c:
                if b.get("type") == "tool_use": usos[b["id"]] = (b["name"], b.get("input", {})); n += 1
                elif b.get("type") == "tool_result":
                    nome, inp = usos.get(b.get("tool_use_id"), (None, {})); t = texto(b.get("content")); total += len(t)
                    for k, p in ALVOS.items():
                        if nome in ("Read", "Grep") and p in json.dumps(inp):
                            lidos.setdefault(k, []).append((nome, len(t), bool(inp.get("offset") or inp.get("limit"))))
        print(f"{os.path.basename(f)[6:14]} {meta.get('agentType', '?'):18s} ferramentas={n:3d} resultados={total:7d}B (~{total // 4} tok)")
        for k, v in lidos.items():
            print(f"    {k:11s} " + "; ".join(f"{a}{'(parcial)' if p and a == 'Read' else ''}:{b}B" for a, b, p in v[:6]))
if __name__ == "__main__": main(sys.argv[1] if len(sys.argv) > 1 else ".")
