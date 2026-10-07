#!/usr/bin/env python3
"""validate_finding.py — validador DETERMINÍSTICO de achado do Auditor Externo (SOT).

[PROPOSTA — NÃO HOMOLOGADO] Detector (ENF-03): checa forma e ancoragem; NÃO julga mérito,
NÃO homologa e NÃO é gate do processo. PASS = achado bem formado e verificável por string-match;
não significa que o achado esteja certo.

Uso: python validate_finding.py --repo <clone> --finding finding.json [--json-out report.json]
Exit 0 = PASS · 1 = FAIL · 2 = erro de uso. Somente biblioteca padrão. Somente leitura (git show/cat-file).
"""
import argparse, json, re, subprocess, sys

SEV = {"P0", "P1", "P2"}
TIPO = {"invariante", "salvaguarda", "CONS-01", "CONST-01", "rastreabilidade", "enforcement", "EARS/BASpec",
        "dossie/pesquisa", "seguranca", "drift", "editorial", "outro"}
PROP = {"ERRATUM_ADITIVO", "EMENDA_PONTUAL", "NOTA", "SEM_MUDANCA"}
ID_RE = re.compile(r"^AEX-\d{8}-\d{3}$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
MIN_QUOTE = 20
# IDs normativos do SOT (prefixo-NÚMERO/SIGLA): RULE-ECC-04, INV-09, CC-08, ENF-03, DHR-…, EUA-E21, SPEC-006, WF-D03 etc.
ID_TOKEN = re.compile(r"\b(?:RULE|INV|CC|ENF|DHR|EUA|ADR|BL|SPEC|WF|RISK|GRE|HRE|PN|CONS|CONST)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b")
MAX_RULE_TOKENS = 10
# comandos de reprodução permitidos: só leitura (1º token ou par de tokens)
ALLOWED = [("git", "show"), ("git", "grep"), ("git", "cat-file"), ("git", "log"), ("git", "diff"),
           ("grep",), ("python", "scripts/validate_spec_sot.py"), ("python", "scripts/check_refs.py"),
           ("python", "scripts/check_doc_sync.py"), ("python", "scripts/build_map.py"),
           ("python", "scripts/check_repo_research.py"), ("npm", "run", "lint"), ("npm", "test")]
META = re.compile(r"[;&|`$<>\n]")
CLOSED_CLAIM = re.compile(r"\b(J-001|N-001|M-001|H-001|G-001|I-001|K-001|C-001|WF-D03|ECC-03-001)\b[^.\n]{0,60}"
                          r"\b(resolvid[ao]|fechad[ao]|decidid[ao]|closed|resolved)\b", re.I)


def git(repo, *args):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    return r.returncode, r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--finding", required=True)
    ap.add_argument("--json-out")
    a = ap.parse_args()
    err, warn = [], []
    try:
        f = json.load(open(a.finding, encoding="utf-8"))
    except Exception as e:
        print(f"FAIL: JSON inválido ({e})"); return 2

    def need(obj, key, typ, where):
        if key not in obj or not isinstance(obj[key], typ) or (typ is str and not obj[key].strip()):
            err.append(f"E-FORMA {where}.{key}: ausente ou tipo inválido"); return None
        return obj[key]

    if f.get("schema_version") != "1.0": err.append("E-FORMA schema_version deve ser '1.0'")
    fid = need(f, "id", str, "finding")
    if fid and not ID_RE.match(fid): err.append("E-ID id deve casar AEX-AAAAMMDD-NNN")
    sev = need(f, "severity", str, "finding")
    if sev and sev not in SEV: err.append("E-ENUM severity ∈ P0|P1|P2")
    tp = need(f, "type", str, "finding")
    if tp and tp not in TIPO: err.append(f"E-ENUM type ∈ {sorted(TIPO)}")
    title = need(f, "title", str, "finding")
    if title and len(title) > 120: err.append("E-FORMA title ≤ 120 caracteres")
    claim = need(f, "claim", str, "finding")
    for k in ("rule_source", "impact", "what_does_not_change"):
        need(f, k, str, "finding")
    if claim and len(claim) > 2000: err.append("E-FORMA claim ≤ 2000 caracteres")

    # baseline: HEAD do clone, árvore limpa
    sha = need(f, "baseline_commit", str, "finding")
    rc, head = git(a.repo, "rev-parse", "HEAD"); head = head.strip()
    if rc != 0: print("FAIL: --repo não é repositório git"); return 2
    if sha and not SHA_RE.match(sha): err.append("E-BASELINE baseline_commit deve ter 40 hex")
    elif sha and sha != head: err.append(f"E-BASELINE baseline_commit {sha[:8]} ≠ HEAD do clone {head[:8]}")
    if git(a.repo, "status", "--porcelain")[1].strip():
        err.append("E-ARVORE árvore de trabalho não está limpa (auditoria é somente leitura)")
    sha = head  # âncoras verificadas no commit real

    # PN2 (anti-alucinação de regra): todo ID normativo citado em rule_source deve EXISTIR no commit auditado. Texto livre sem ID é
    # permitido (liberdade cognitiva); só regra INVENTADA é barrada. Detector de forma/ancoragem — não julga se a regra se aplica.
    rs = f.get("rule_source")
    if isinstance(rs, str):
        toks = list(dict.fromkeys(ID_TOKEN.findall(rs)))
        if len(toks) > MAX_RULE_TOKENS:
            err.append(f"E-RULESRC rule_source cita {len(toks)} IDs normativos (máx. {MAX_RULE_TOKENS}); cite só os que fundamentam o achado")
            toks = toks[:MAX_RULE_TOKENS]
        for t in toks:
            if git(a.repo, "grep", "-q", "-F", "-e", t, sha)[0] != 0:
                err.append(f"E-RULESRC rule_source cita '{t}', que NÃO existe no commit auditado (regra inventada?)")

    # evidência literal
    ev = f.get("evidence")
    if not isinstance(ev, list) or not ev:
        err.append("E-EVID evidence[] obrigatório (≥1): achado sem citação literal é descartado")
        ev = []
    for i, e in enumerate(ev):
        w = f"evidence[{i}]"
        p = e.get("path") if isinstance(e, dict) else None
        ls, le, q = (e.get(k) for k in ("line_start", "line_end", "quote")) if isinstance(e, dict) else (None,) * 3
        if not (isinstance(p, str) and p and not p.startswith("/") and ".." not in p.split("/")):
            err.append(f"E-EVID {w}.path inválido"); continue
        if git(a.repo, "cat-file", "-e", f"{sha}:{p}")[0] != 0:
            err.append(f"E-EVID {w}.path não existe no commit: {p}"); continue
        if not (isinstance(ls, int) and isinstance(le, int) and 1 <= ls <= le):
            err.append(f"E-EVID {w}.line_start/line_end inválidos"); continue
        if not (isinstance(q, str) and len(q) >= MIN_QUOTE):
            err.append(f"E-EVID {w}.quote deve ter ≥ {MIN_QUOTE} caracteres literais"); continue
        lines = git(a.repo, "show", f"{sha}:{p}")[1].replace("\r\n", "\n").split("\n")
        if le > len(lines):
            err.append(f"E-EVID {w}: line_end {le} > tamanho do arquivo ({len(lines)})"); continue
        trecho = "\n".join(lines[ls - 1:le])
        if q.replace("\r\n", "\n") not in trecho:
            err.append(f"E-QUOTE {w}: citação NÃO encontrada literalmente em {p}:{ls}-{le}")

    # proposta
    pr = f.get("proposal")
    if not isinstance(pr, dict):
        err.append("E-PROP proposal{} obrigatório")
    else:
        pt = need(pr, "type", str, "proposal")
        if pt and pt not in PROP: err.append(f"E-ENUM proposal.type ∈ {sorted(PROP)}")
        need(pr, "text", str, "proposal")
        mb = pr.get("modifies_baselined_text")
        if not isinstance(mb, bool): err.append("E-PROP proposal.modifies_baselined_text (bool) obrigatório")
        elif mb and pt not in ("ERRATUM_ADITIVO", "EMENDA_PONTUAL"):
            err.append("E-INV09 texto baselined só por ERRATUM_ADITIVO ou EMENDA_PONTUAL (nunca edição direta)")
        for t in pr.get("touches", []) if isinstance(pr.get("touches", []), list) else []:
            if isinstance(t, str) and (t.startswith("canon/") or t.startswith("./canon/")):
                err.append(f"E-CONST01 proposta não pode alterar canon/: {t} (registrar como pendência para Andraus)")
        if CLOSED_CLAIM.search((pr.get("text") or "") + " " + (claim or "")):
            warn.append("W-CONS01 texto parece tratar decisão aberta como resolvida — conferir (CONS-01)")

    # postura: a diretiva citada deve ser a VIGENTE no commit auditado (Orquestrador é a única autoridade de postura)
    dv = need(f, "directive_version", str, "finding")
    rc2, dtxt = git(a.repo, "show", f"{sha}:governance/propostas/AUDITOR-EXTERNO/DIRETIVAS-AO-AUDITOR.md")
    if rc2 != 0:
        err.append("E-DIRETIVA arquivo de diretivas ausente no commit auditado")
    else:
        vig = [m.group(1) for m in re.finditer(r"^## (DIR-\d{3})\s*\n+Status:\s*VIGENTE", dtxt, re.M)]
        if not vig: err.append("E-DIRETIVA nenhuma diretiva VIGENTE no commit auditado")
        elif dv and dv != vig[-1]: err.append(f"E-DIRETIVA directive_version {dv} ≠ vigente {vig[-1]}")

    # decisões abertas e estado S/I/P
    if f.get("treats_open_decision_as_closed") is not False:
        err.append("E-CONS01 treats_open_decision_as_closed deve ser false (decisão aberta nunca vira invariante)")
    if not isinstance(f.get("open_decisions_referenced"), list):
        err.append("E-FORMA open_decisions_referenced[] obrigatório (pode ser vazio)")
    st = f.get("status_sip")
    if not (isinstance(st, dict) and all(isinstance(st.get(k), bool) for k in ("specified", "implemented", "proven"))):
        err.append("E-SIP status_sip{specified,implemented,proven} (bool) obrigatório")
    elif (st["implemented"] or st["proven"]) and not f.get("gate_evidence_ref"):
        err.append("E-SIP implemented/proven=true exige gate_evidence_ref (declarado ≠ verificável ≠ executável)")

    # reprodução (somente leitura)
    for i, c in enumerate(f.get("reproduce", []) if isinstance(f.get("reproduce", []), list) else []):
        toks = c.split() if isinstance(c, str) else []
        ok = isinstance(c, str) and not META.search(c) and any(tuple(toks[:len(p)]) == p for p in ALLOWED)
        if not ok: err.append(f"E-REPRO reproduce[{i}] fora da lista de comandos somente-leitura: {c!r}")

    au = f.get("author")
    if not (isinstance(au, dict) and all(isinstance(au.get(k), str) and au[k].strip() for k in ("model", "date"))):
        err.append("E-FORMA author{model,date} obrigatório (reprodutibilidade)")

    rep = {"pass": not err, "finding_id": fid, "head": head, "errors": err, "warnings": warn}
    if a.json_out: json.dump(rep, open(a.json_out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(("PASS" if not err else "FAIL") + f" — {fid} @ {head[:8]}")
    for x in err: print("  ✗", x)
    for x in warn: print("  !", x)
    print("Lembrete: PASS = forma e ancoragem; NÃO é parecer de mérito, nem homologação.")
    return 0 if not err else 1


if __name__ == "__main__":
    sys.exit(main())
