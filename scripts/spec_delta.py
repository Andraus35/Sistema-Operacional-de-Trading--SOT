#!/usr/bin/env python3
"""
spec_delta.py — cache por HASH da revisão (proposta da auditoria de custo, 2026-10-17; SPEC-046/BL-024 como motivação).

Compara DUAS versões de um plan.md por BLOCO (seção `##`/`###`/`####`, e cada definição `RULE-X-NNN:`/`INV-X:`), pelo sha256 do texto
com espaços colapsados. Entrega ao Revisor **só o que mudou** (mais as fontes canônicas citadas com o hash de cada arquivo), em vez de
reler as 1.700 linhas a cada rodada. Somente leitura. Detector ≠ Gate (ENF-03): diz O QUE mudou, não se está certo.

Uso:
  python scripts/spec_delta.py <plan.md> --base <git-ref|arquivo>   # base = versão já revisada (ex.: HEAD~3, um commit, ou um arquivo .md)
  python scripts/spec_delta.py <plan.md> --base HEAD~1 --json
  python scripts/spec_delta.py <plan.md> --fontes                    # só o inventário de fontes citadas com sha256 (cache de leitura)
Chave do bloco: ID inicial (`BASpec-CKG-010`, `EC-CKG-001`, `Cenário-CKG-T09`, `ADV-CKG-21`, `RULE-CKG-008`) ou o título normalizado.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_HEAD = re.compile(r"^(#{2,4})\s+(.*?)\s*$")
_ID = re.compile(r"^((?:BASpec|EC|ADV|Cen[áa]rio)-[A-Za-z]+(?:-T)?-?\d+|(?:INV|RULE)-[A-Z0-9-]+)")
_DEF = re.compile(r"^[\s>*|`-]*\**((?:RULE|INV)-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*)\**\s*:")


def _h(s):
    return hashlib.sha256(re.sub(r"\s+", " ", s).strip().encode("utf-8")).hexdigest()


def blocos(texto):
    """{chave: sha256}. Seções por cabeçalho + cada definição de RULE/INV (granularidade fina dentro de blocos grandes)."""
    out, cur, buf = {}, "cabeçalho", []
    def fecha():
        if buf:
            out[cur] = _h("\n".join(buf))
    for ln in texto.splitlines():
        m = _HEAD.match(ln)
        if m:
            fecha()
            t = m.group(2)
            k = _ID.match(t)
            cur = k.group(1) if k else re.sub(r"[^\w§.-]+", "-", t.lower())[:60]
            while cur in out:  # títulos repetidos
                cur += "'"
            buf = [ln]
        else:
            buf.append(ln)
    fecha()
    # definições de regra (RULE-X-NNN:) até a próxima definição ou linha em branco dupla
    lines, i = texto.splitlines(), 0
    while i < len(lines):
        m = _DEF.match(lines[i])
        if m:
            j = i + 1
            while j < len(lines) and not _DEF.match(lines[j]) and lines[j].strip() != "" and not _HEAD.match(lines[j]):
                j += 1
            out.setdefault("def:" + m.group(1), _h("\n".join(lines[i:j])))
            i = j
        else:
            i += 1
    return out


def ler_base(base, plan):
    p = Path(base)
    if p.is_file():
        return p.read_text(encoding="utf-8", errors="replace")
    rel = Path(plan).resolve().relative_to(ROOT).as_posix()
    r = subprocess.run(["git", "show", f"{base}:{rel}"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit(f"base '{base}' não encontrada ({r.stderr.strip()[:120]})")
    return r.stdout


def delta(base_txt, novo_txt):
    a, b = blocos(base_txt), blocos(novo_txt)
    return {
        "adicionados": sorted(set(b) - set(a)),
        "removidos": sorted(set(a) - set(b)),
        "alterados": sorted(k for k in set(a) & set(b) if a[k] != b[k]),
        "inalterados": sum(1 for k in set(a) & set(b) if a[k] == b[k]),
        "total_base": len(a), "total_atual": len(b),
    }


_CIT = re.compile(r"\b(CEM-001|CHM-001|CCM-001|CEE-001|SAS-001|CONSTITUTION|RULES|atomic-spec|RMR-001|SPEC-0\d\d)\b")


def fontes(texto, root=ROOT):
    """Arquivos de baseline citados + sha256 (12 hex): se o hash não mudou desde o último parecer, a releitura é desnecessária."""
    import gate_extra
    achados = {}
    for nome in sorted(set(_CIT.findall(texto))):
        f = gate_extra._arquivo(nome, root)
        if f and f.is_file():
            achados[f.relative_to(root).as_posix()] = hashlib.sha256(f.read_bytes()).hexdigest()[:12]
    return achados


def main(argv=None):
    sys.path.insert(0, str(ROOT / "scripts"))
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--base")
    ap.add_argument("--fontes", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    novo = Path(a.plan).read_text(encoding="utf-8", errors="replace")
    res = {"documento": a.plan, "documento_sha256": hashlib.sha256(novo.encode("utf-8")).hexdigest()}
    if a.base:
        res["delta"] = delta(ler_base(a.base, a.plan), novo)
    res["fontes_sha256"] = fontes(novo)
    if a.json or not a.base:
        if a.fontes and not a.json:
            for f, h in res["fontes_sha256"].items():
                print(f"{h}  {f}")
        else:
            print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0
    d = res["delta"]
    print(f"DELTA {a.plan} vs {a.base}: {len(d['alterados'])} alterados · {len(d['adicionados'])} adicionados · "
          f"{len(d['removidos'])} removidos · {d['inalterados']} inalterados (de {d['total_atual']} blocos)")
    for rot in ("alterados", "adicionados", "removidos"):
        if d[rot]:
            print(f"  {rot}: " + ", ".join(d[rot]))
    print(f"  fontes citadas (sha256 de 12): {len(res['fontes_sha256'])} — use --fontes para listar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
