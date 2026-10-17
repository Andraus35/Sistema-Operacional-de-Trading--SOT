#!/usr/bin/env python3
"""
check_coesao.py — detector de COESÃO do harness (auditoria de 2026-10-17; achados D1..D6, O1..O7).

Somente leitura. Mesmo molde de check_handoff.py / check_doc_sync.py: extrai fatos objetivos do
próprio repositório (settings.json, CI, tests/, scripts/, AGENTS.md, agentes, CODEOWNERS, manifesto,
git) e cruza entre si. Procura o que a auditoria achou à mão: mecanismo registrado que não existe,
teste que o CI não roda, "proteção" que é no-op, citação de ata inexistente, nome de arquivo com
caixa errada, tabela do AGENTS.md diferente do arquivo do agente, selo sem dono, skill solta,
config ociosa, status contraditório entre workflow e norma, pendência de merge já resolvida.
Detector ≠ Gate (ENF-03): não corrige, não fecha decisão aberta (CONS-01), não homologa.

Checagens:
    COE-01  hook de settings.json/pre-commit aponta script inexistente                        → ERRO
            script de scripts/ sem uso (hook, CI, pre-commit, outro script, teste)            → WARN
    COE-02  teste (tests/test_*.py, tests/test-*.js) que o CI não executa                     → ERRO
    COE-03  entrada do pre-commit que lê payload de hook do Claude Code (stdin) → no-op       → WARN
    COE-04  ata DHR-* citada em scripts/.claude/.github sem arquivo em governance/            → ERRO
    COE-05  caminho citado com CAIXA diferente do arquivo real (quebra em Linux)              → ERRO
    COE-06  Tools da tabela do AGENTS.md ≠ `tools:` do arquivo do agente                       → WARN
    COE-07  arquivo selado em GATE-MANIFEST.sha256 sem linha em CODEOWNERS                    → WARN
    COE-08  skill solta (.claude/skills/*.md) ou pasta de skill sem SKILL.md                  → WARN
    COE-09  config de lint/format sem a ferramenta em package.json/CI/pre-commit              → INFO
    COE-10  workflow "INERTE/NÃO HOMOLOGADO" cujo tema o AGENTS.md descreve sem dizê-lo       → WARN
    COE-11  ata ainda "PROPOSTA — vira vigente só com o merge" que já está em origin/main     → INFO
    COE-12  HANDOFF espera merge de ata que já está em origin/main                            → WARN
    COE-13  README declara "Spec autorizada" (duplica o ROADMAP)                              → WARN
    COE-14  governance/MECANISMOS.json (registro de mecanismos) × realidade, nos dois sentidos:
            forma pelo schema, item sem arquivo, arquivo sem item, estado ≠ ativo sem nota,
            ata inexistente, workflow INERTE registrado como ativo   → WARN (registro PROPOSTA) / ERRO (VIGENTE)

Uso:
    python scripts/check_coesao.py               # relatório; exit 1 se houver ERRO
    python scripts/check_coesao.py --strict      # WARN também falha
    python scripts/check_coesao.py --json
    python scripts/check_coesao.py --matriz      # tabela script × (hook, CI, teste, selo, dono, AGENTS §8)
    python scripts/check_coesao.py --root DIR    # raiz alternativa (testes)

exit 0 ≠ CONFORME ≠ homologação.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

DHR = re.compile(r"\bDHR-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d+[a-z]?\b|\bDHR-[A-Z0-9]+(?:-[A-Z0-9]+)*\b")
PATH_TOKEN = re.compile(r"(?<![\w./-])((?:[\w.-]+/)*[\w.-]+\.(?:md|py|js|json|yml|yaml|sha256))(?![\w/-])")
BASE_TOOLS = ("Read", "Write", "Edit", "MultiEdit", "Grep", "Glob", "Bash", "WebSearch", "WebFetch")
SKIP_DIRS = {".git", "node_modules", "docs", "__pycache__"}


class Ctx:
    def __init__(self, root: Path):
        self.root = root
        self.findings = []

    def add(self, cid, level, msg, where=""):
        self.findings.append({"id": cid, "nivel": level, "onde": where, "msg": msg})

    def read(self, rel):
        p = self.root / rel
        try:
            return p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""

    def git(self, *args):
        try:
            r = subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
            return r.returncode, r.stdout
        except OSError:
            return 127, ""

    def on_default_branch(self, rel):
        """True/False se o arquivo existe em origin/main; None se não há origin/main (sem git)."""
        rc, _ = self.git("rev-parse", "--verify", "-q", "origin/main")
        if rc != 0:
            return None
        rc, _ = self.git("cat-file", "-e", f"origin/main:{rel}")
        return rc == 0


def frontmatter_tools(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    tools, on = [], False
    for ln in m.group(1).splitlines():
        if re.match(r"^tools:\s*$", ln):
            on = True
            continue
        if on:
            t = re.match(r"^\s+-\s+(\S+)", ln)
            if t:
                tools.append(t.group(1))
            elif ln.strip() and not ln.lstrip().startswith("#"):
                on = False
    return tools


def ci_text(ctx):
    out = ""
    for p in sorted((ctx.root / ".github" / "workflows").glob("*.yml")):
        out += p.read_text(encoding="utf-8", errors="replace") + "\n"
    return out


def npm_scripts(ctx):
    try:
        return json.loads(ctx.read("package.json")).get("scripts", {})
    except ValueError:
        return {}


def executed_by_ci(ctx):
    """Texto efetivamente executado pelo CI: ci.yml + o corpo dos `npm run X`/`npm test` que ele chama."""
    ci = ci_text(ctx)
    scripts = npm_scripts(ctx)
    extra = ""
    for name in re.findall(r"npm run ([\w:-]+)", ci):
        extra += " " + scripts.get(name, "")
    if re.search(r"npm (?:run )?test\b", ci):
        extra += " " + scripts.get("test", "")
    return ci + extra, ("unittest discover" in ci or "unittest discover" in extra)


def check_hooks_and_scripts(ctx):
    settings = ctx.read(".claude/settings.json")
    precommit = ctx.read(".pre-commit-config.yaml")
    ci = ci_text(ctx)
    refs = {}
    for m in re.finditer(r"scripts/([\w.-]+\.(?:js|py))", settings + "\n" + precommit):
        refs[m.group(1)] = True
        if not (ctx.root / "scripts" / m.group(1)).exists():
            ctx.add("COE-01", "ERRO", f"hook aponta para scripts/{m.group(1)}, que não existe", "settings.json/pre-commit")
    corpus = settings + precommit + ci + ctx.read("package.json")
    for sub in ("scripts", "tests"):
        for p in (ctx.root / sub).glob("*"):
            if p.suffix in (".py", ".js") and p.name != Path(__file__).name:
                corpus += "\n" + p.read_text(encoding="utf-8", errors="replace")
    for p in sorted((ctx.root / "scripts").glob("*")):
        if p.suffix not in (".py", ".js"):
            continue
        used = len(re.findall(re.escape(p.name), corpus)) + len(re.findall(re.escape(p.stem), corpus))
        own = len(re.findall(re.escape(p.name), p.read_text(encoding="utf-8", errors="replace")))
        if used - own <= 0:
            ctx.add("COE-01", "WARN", f"scripts/{p.name} não é usado por hook, CI, pre-commit, teste nem outro script", f"scripts/{p.name}")


def check_tests_in_ci(ctx):
    ran, discover = executed_by_ci(ctx)
    for p in sorted((ctx.root / "tests").glob("*")):
        if not re.match(r"test[_-].*\.(py|js)$", p.name):
            continue
        if p.name in ran or (discover and p.suffix == ".py"):
            continue
        # tests/test-*.js e validate-schemas/lint-specs rodam via npm scripts; já expandidos em `ran`
        ctx.add("COE-02", "ERRO", f"tests/{p.name} não é executado pelo CI", f"tests/{p.name}")


def check_precommit_noop(ctx):
    pc = ctx.read(".pre-commit-config.yaml")
    for m in re.finditer(r"entry:\s*node\s+(scripts/[\w.-]+\.js)", pc):
        body = ctx.read(m.group(1))
        if "readToolInput" in body:
            ctx.add("COE-03", "WARN",
                    f"{m.group(1)} lê o payload de hook do Claude Code (stdin) e o pre-commit não o fornece: roda como no-op (exit 0)",
                    ".pre-commit-config.yaml")


def check_dhr_citations(ctx):
    existing = {p.name.split("_")[0] for p in (ctx.root / "governance").glob("DHR-*.md")}
    targets = []
    for sub, pats in (("scripts", ("*.py", "*.js")), (".claude", ("*.md", "*.json")), (".github", ("*.yml", "CODEOWNERS"))):
        for pat in pats:
            targets += list((ctx.root / sub).rglob(pat))
    seen = set()
    for p in sorted(set(targets)):
        if "__pycache__" in p.parts or "runs" in p.parts:   # saídas arquivadas da skill harness-eval
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        for m in DHR.finditer(txt):
            ident = m.group(0)
            if ident in existing or (ident, p) in seen:
                continue
            # prefixo de família citado sem número final não é citação de ata única
            if not re.search(r"-\d+[a-z]?$", ident):
                continue
            seen.add((ident, p))
            ctx.add("COE-04", "ERRO", f"{ident} é citada, mas não há governance/{ident}_*.md", str(p.relative_to(ctx.root)))


def real_case(ctx, token):
    """Se `token` não existe com esta caixa mas existe com outra, devolve o nome real."""
    rel = Path(token)
    if (ctx.root / rel).exists():
        return None
    base = ctx.root / rel.parent
    if not base.is_dir():
        return None
    for q in base.iterdir():
        if q.name.lower() == rel.name.lower() and q.name != rel.name:
            return str((rel.parent / q.name).as_posix()).lstrip("./")
    return None


def check_case_drift(ctx):
    files = [ctx.root / n for n in ("README.md", "AGENTS.md", "GLOSSARIO.md")]
    files += sorted((ctx.root / ".claude" / "agents").glob("*.md")) + sorted((ctx.root / ".claude" / "commands").glob("*.md"))
    files += sorted((ctx.root / ".claude" / "skills").glob("*.md")) + sorted((ctx.root / ".clinerules").glob("*.md"))
    for p in files:
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        reported = set()
        for m in PATH_TOKEN.finditer(txt):
            tok = m.group(1)
            if tok in reported or tok.startswith(("http", "docs/")):
                continue
            real = real_case(ctx, tok)
            if real:
                reported.add(tok)
                ctx.add("COE-05", "ERRO", f"cita `{tok}`, mas o arquivo é `{real}` (caixa diferente; quebra em Linux)",
                        str(p.relative_to(ctx.root)))


def agents_table_tools(ctx):
    txt = ctx.read("AGENTS.md")
    rows = {}
    for ln in txt.splitlines():
        m = re.match(r"\|\s*`(\.claude/agents/[\w.-]+\.md)`\s*\|[^|]*\|([^|]*)\|", ln)
        if m:
            rows[m.group(1)] = (set(t for t in BASE_TOOLS if re.search(rf"\b{t}\b", m.group(2))), m.group(2))
    return rows


def check_agents_vs_table(ctx):
    for rel, (listed, cell) in agents_table_tools(ctx).items():
        tools = frontmatter_tools(ctx.read(rel))
        if tools is None:
            continue
        real = {t for t in tools if t in BASE_TOOLS}
        mcp = [t for t in tools if t.startswith("mcp__") and t.split("__")[-1] not in cell]
        extra = sorted(real - listed)
        if extra or mcp:
            ctx.add("COE-06", "WARN",
                    "frontmatter tem ferramentas que a tabela do AGENTS.md §3 não lista: " + ", ".join(extra + mcp),
                    rel)
        missing = sorted(listed - real)
        if missing:
            ctx.add("COE-06", "WARN", f"tabela do AGENTS.md §3 lista {', '.join(missing)}, ausente(s) no frontmatter", rel)


def check_codeowners(ctx):
    owners = ctx.read(".github/CODEOWNERS")
    for ln in ctx.read("governance/GATE-MANIFEST.sha256").splitlines():
        parts = ln.split()
        if len(parts) >= 2 and f"/{parts[-1]}" not in owners:
            ctx.add("COE-07", "WARN", f"{parts[-1]} está no selo mas não tem dono em CODEOWNERS", ".github/CODEOWNERS")


def check_skills(ctx):
    sk = ctx.root / ".claude" / "skills"
    if not sk.is_dir():
        return
    for p in sorted(sk.iterdir()):
        if p.is_file() and p.suffix == ".md":
            ctx.add("COE-08", "WARN", f"{p.name} solto em .claude/skills/ (skill precisa de pasta própria com SKILL.md; fora disso não é carregada)",
                    f".claude/skills/{p.name}")
        elif p.is_dir() and not (p / "SKILL.md").exists():
            ctx.add("COE-08", "WARN", f"pasta de skill sem SKILL.md: {p.name}", f".claude/skills/{p.name}")


def check_idle_configs(ctx):
    used = ctx.read("package.json") + ci_text(ctx) + ctx.read(".pre-commit-config.yaml")
    for cfg, tool in ((".eslintrc.json", "eslint"), (".prettierrc", "prettier")):
        if (ctx.root / cfg).exists() and tool not in used.lower():
            ctx.add("COE-09", "INFO", f"{cfg} existe, mas {tool} não é chamado por package.json, CI nem pre-commit", cfg)


def check_workflow_status(ctx):
    agents = ctx.read("AGENTS.md")
    for p in sorted((ctx.root / ".github" / "workflows").glob("*.yml")):
        txt = p.read_text(encoding="utf-8", errors="replace")
        head = "\n".join(txt.splitlines()[:25])
        if not re.search(r"INERTE|NÃO HOMOLOGADO", head):
            continue
        m = re.search(r"^name:\s*(.+)$", txt, re.M)
        key = re.split(r"\s*\(", m.group(1).strip())[0] if m else ""
        # seção do AGENTS.md (de "## …" a "## …") em que o tema aparece; o estado precisa estar DITO ali
        sec = next((s for s in re.split(r"(?m)^## ", agents) if key and re.search(re.escape(key), s.split("\n", 1)[0], re.I)), "")
        if sec and not re.search(r"inerte|paus|desligad|desativ", sec, re.I):
            ctx.add("COE-10", "WARN",
                    f"workflow '{key}' se declara INERTE/NÃO HOMOLOGADO, mas o AGENTS.md o descreve sem dizer que está inerte/pausado",
                    str(p.relative_to(ctx.root)))


def check_proposta_residual(ctx):
    for p in sorted((ctx.root / "governance").glob("DHR-*.md")):
        head = "\n".join(p.read_text(encoding="utf-8", errors="replace").splitlines()[:14])
        if re.search(r"Status\s*\|\s*\*\*PROPOSTA — vira vigente só com o merge", head):
            if ctx.on_default_branch(f"governance/{p.name}"):
                ctx.add("COE-11", "INFO", "Status textual ainda 'PROPOSTA — vira vigente só com o merge', mas a ata já está na main",
                        f"governance/{p.name}")


def check_handoff_pending(ctx):
    for i, ln in enumerate(ctx.read("HANDOFF.md").splitlines(), 1):
        # só linhas que ESPERAM merge ("Andraus mescla", "Merge da/das …", "PR aberto"); relato histórico não conta
        if not re.search(r"Andraus mescla|^\W*Merge d[ao]s?\b|PR aberto|aguard\w+ (o )?merge", ln, re.I):
            continue
        if re.search(r"\bjá\b", ln, re.I):
            continue
        for ident in set(DHR.findall(ln)):
            hits = list((ctx.root / "governance").glob(f"{ident}_*.md"))
            if hits and ctx.on_default_branch(f"governance/{hits[0].name}"):
                ctx.add("COE-12", "WARN", f"HANDOFF espera merge de {ident}, mas a ata já está em origin/main", f"HANDOFF.md:{i}")


def check_readme_spec(ctx):
    for i, ln in enumerate(ctx.read("README.md").splitlines(), 1):
        if re.search(r"autorizad\w*[^\n]{0,60}SPEC-\d+", ln, re.I):
            ctx.add("COE-13", "WARN", "README declara a Spec autorizada (duplica o ROADMAP; vira defasagem). Aponte para ROADMAP/HANDOFF",
                    f"README.md:{i}")


def check_registry(ctx):
    """COE-14 — o registro é a fonte única de ESTADO dos mecanismos; aqui ele é confrontado com o repositório."""
    raw = ctx.read("governance/MECANISMOS.json")
    if not raw:
        return
    try:
        reg = json.loads(raw)
        schema = json.loads(ctx.read("governance/MECANISMOS.schema.json") or "{}")
    except ValueError as e:
        ctx.add("COE-14", "ERRO", f"JSON inválido: {e}", "governance/MECANISMOS.json")
        return
    lvl = "ERRO" if reg.get("status_do_registro") == "VIGENTE" else "WARN"
    where = "governance/MECANISMOS.json"
    item_schema = schema.get("properties", {}).get("mecanismos", {}).get("items", {})
    props = item_schema.get("properties", {})
    ids, files = set(), set()
    for i, m in enumerate(reg.get("mecanismos", [])):
        tag = m.get("id", f"#{i}") if isinstance(m, dict) else f"#{i}"
        if not isinstance(m, dict):
            ctx.add("COE-14", lvl, f"item {tag} não é objeto", where)
            continue
        for k in item_schema.get("required", []):
            if k not in m:
                ctx.add("COE-14", lvl, f"{tag}: campo obrigatório ausente: {k}", where)
        for k, v in m.items():
            spec = props.get(k)
            if spec is None:
                ctx.add("COE-14", lvl, f"{tag}: campo fora do schema: {k}", where)
                continue
            if "enum" in spec and v not in spec["enum"]:
                ctx.add("COE-14", lvl, f"{tag}: {k}={v!r} fora do enum {spec['enum']}", where)
            if "pattern" in spec and not re.search(spec["pattern"], str(v)):
                ctx.add("COE-14", lvl, f"{tag}: {k}={v!r} não casa o padrão do schema", where)
        if tag in ids:
            ctx.add("COE-14", lvl, f"id repetido: {tag}", where)
        ids.add(tag)
        arq = m.get("arquivo", "")
        files.add(arq)
        if arq and not (ctx.root / arq).exists():
            ctx.add("COE-14", lvl, f"{tag}: arquivo registrado não existe: {arq}", where)
        if m.get("estado", "ativo") != "ativo" and not str(m.get("nota", "")).strip():
            ctx.add("COE-14", lvl, f"{tag}: estado {m.get('estado')} exige 'nota' dizendo por quê", where)
        ata = m.get("ata")
        if ata and not list((ctx.root / "governance").glob(f"{ata}_*.md")):
            ctx.add("COE-14", lvl, f"{tag}: ata {ata} não existe em governance/", where)
        if arq.endswith(".yml") and m.get("estado") == "ativo":
            head = "\n".join(ctx.read(arq).splitlines()[:25])
            if re.search(r"INERTE|NÃO HOMOLOGADO", head) and str(m.get("verificado_em", "")).startswith("inferido"):
                ctx.add("COE-14", lvl, f"{tag}: workflow se declara INERTE/NÃO HOMOLOGADO (chave de desligamento) e o registro diz 'ativo' sem comprovar que a chave está ligada", where)
    existing = []
    for sub, pats in (("scripts", ("*.py", "*.js")), (".github/workflows", ("*.yml",)), (".claude/agents", ("*.md",))):
        for pat in pats:
            existing += [p for p in sorted((ctx.root / sub).glob(pat)) if p.is_file()]
    skills = ctx.root / ".claude" / "skills"
    if skills.is_dir():
        existing += [p for p in sorted(skills.glob("*.md"))]
    for cfg in (".pre-commit-config.yaml", ".eslintrc.json", ".prettierrc"):
        if (ctx.root / cfg).exists():
            existing.append(ctx.root / cfg)
    for p in existing:
        rel = str(p.relative_to(ctx.root)).replace("\\", "/")
        if rel not in files:
            ctx.add("COE-14", lvl, f"{rel} existe no repositório e não está no registro de mecanismos", where)


def matriz(ctx):
    settings = ctx.read(".claude/settings.json")
    pc = ctx.read(".pre-commit-config.yaml")
    ran, discover = executed_by_ci(ctx)
    ci = ci_text(ctx)
    manifest = ctx.read("governance/GATE-MANIFEST.sha256")
    owners = ctx.read(".github/CODEOWNERS")
    agents = ctx.read("AGENTS.md")
    tests = "".join(p.read_text(encoding="utf-8", errors="replace") for p in (ctx.root / "tests").glob("*") if p.is_file())
    rows = ["| script | hook | pre-commit | CI | teste | selo | dono | AGENTS |", "|---|---|---|---|---|---|---|---|"]
    yn = lambda b: "sim" if b else "—"
    for p in sorted((ctx.root / "scripts").glob("*")):
        if p.suffix not in (".py", ".js"):
            continue
        n = p.name
        rows.append(f"| {n} | {yn(n in settings)} | {yn(n in pc)} | {yn(n in ci or n in ran)} | {yn(n in tests or p.stem in tests)} "
                    f"| {yn(f'scripts/{n}' in manifest)} | {yn(f'/scripts/{n}' in owners)} | {yn(n in agents)} |")
    return "\n".join(rows)


CHECKS = (check_hooks_and_scripts, check_tests_in_ci, check_precommit_noop, check_dhr_citations, check_case_drift,
          check_agents_vs_table, check_codeowners, check_skills, check_idle_configs, check_workflow_status,
          check_proposta_residual, check_handoff_pending, check_readme_spec, check_registry)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Detector de coesão do harness (somente leitura)")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--matriz", action="store_true")
    a = ap.parse_args(argv)
    ctx = Ctx(Path(a.root))
    if a.matriz:
        print(matriz(ctx))
        return 0
    for chk in CHECKS:
        chk(ctx)
    n = {k: sum(1 for f in ctx.findings if f["nivel"] == k) for k in ("ERRO", "WARN", "INFO")}
    if a.json:
        print(json.dumps({"contagem": n, "achados": ctx.findings}, ensure_ascii=False, indent=2))
    else:
        print("=" * 60 + "\nDETECTOR DE COESÃO — check_coesao.py\n" + "=" * 60)
        for f in ctx.findings:
            print(f"[{f['nivel']}] {f['id']} {f['onde']} — {f['msg']}")
        print("-" * 60 + f"\nERRO={n['ERRO']} WARN={n['WARN']} INFO={n['INFO']}")
        print("Somente leitura — Detector (ENF-03): não corrige, não fecha decisão (CONS-01).")
        print("LEMBRETE: detector informativo. exit 0 ≠ CONFORME ≠ homologação.")
    return 1 if n["ERRO"] or (a.strict and n["WARN"]) else 0


if __name__ == "__main__":
    sys.exit(main())
