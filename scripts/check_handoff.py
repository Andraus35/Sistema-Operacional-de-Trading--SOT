#!/usr/bin/env python3
"""
check_handoff.py — detector de defasagem/integridade do HANDOFF.md (PCC-001, Fase 2).

Somente leitura. Mesmo molde de scripts/check_doc_sync.py: extrai fatos objetivos do
próprio repositório (git, ROADMAP, governance/) e cruza com o handoff. Detector ≠ Gate
(ENF-03): nunca escreve o handoff, nunca fecha decisão aberta (CONS-01), nunca
registra homologação.

Checagens (ID = PCC-001 §5.1):
    HO-01  frontmatter completo e seções 1..11 presentes                       → ERRO
    HO-02  base_commit existe e é ancestral de HEAD                            → ERRO
    HO-03  staleness: arquivos mudaram depois do último commit que tocou o
           HANDOFF.md sem novo handoff (ignora HANDOFF.md, docs/handoffs/,
           docs/mapa/ e commits "RPSA:" automáticos)                           → WARN
    HO-04  cadeia: `previous` arquivado em docs/handoffs/ e idêntico à versão
           que o handoff atual substituiu                                      → ERRO
    HO-05  mais de 150 linhas                                                  → WARN
    HO-06  DHR citada sem ata em governance/ ; decisão ABERTA do ROADMAP
           escrita como fechada/decidida na mesma linha                        → ERRO
    HO-07  spec_autorizada não menciona a Spec da linha "Próximo trabalho
           autorizado" do ROADMAP (ROADMAP prevalece)                          → WARN
    HO-08  padrão de segredo/credencial                                        → ERRO
    HO-09  linguagem de homologação/baseline sem ID DHR na mesma linha         → WARN
    HO-11  anexo de tarefa (DHR-PCC-003): `anexo:` do handoff aponta arquivo inexistente ou o anexo
           tem frontmatter incompleto / status fora de ATIVO|CONSUMIDO                       → ERRO
    HO-12  anexo ATIVO não citado pelo handoff, mais de um ATIVO, ou anexo CONSUMIDO ainda
           citado pelo handoff                                                                → WARN
    HO-13  anexo com mais de 80 linhas                                                        → WARN
    HO-14  anexo cita DHR sem ata, trata decisão ABERTA como fechada ou tem segredo           → ERRO
    HO-15  anexo copia linha longa (≥120 car.) do HANDOFF/ROADMAP/atas (aponte, não copie)    → WARN
    HO-10  pendência com `[PRAZO: AAAA-MM-DD]` vencida (hoje ≥ data): reaparece em TODA
           abertura de sessão (hook SessionStart) até a linha ser resolvida ou reagendada → WARN

Uso:
    python scripts/check_handoff.py               # relatório; exit 1 se houver ERRO
    python scripts/check_handoff.py --strict      # WARN também falha
    python scripts/check_handoff.py --json
    python scripts/check_handoff.py --root DIR    # raiz alternativa (testes)

exit 0 ≠ CONFORME ≠ homologação.
"""

import argparse
import datetime
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

sys.path.insert(0, str(Path(__file__).resolve().parent))

REQUIRED_KEYS = ["handoff_id", "previous", "data", "branch", "base_commit",
                 "spec_autorizada", "fase", "autor"]
MAX_LINES = 150
SECRET = re.compile(
    r"(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:api[_-]?key|token|secret|password)\s*[:=]\s*\S{8,})", re.I)
CLOSED_WORDS = re.compile(r"FECHAD|DECIDID|RESOLVID", re.I)
HOMOLOG_WORDS = re.compile(r"\b(foi|ficou|fica|está|estão|é|são|agora)\s+(homologad[oa]s?|baseline[d]?)\b", re.I)
DHR = re.compile(r"\bDHR-[A-Z0-9]+(?:-[A-Z0-9]+)*\b")
PRAZO = re.compile(r"\[PRAZO:\s*(\d{4}-\d{2}-\d{2})\]")
IGNORED_PREFIXES = ("HANDOFF.md", "docs/handoffs/", "docs/mapa/")
ANEXO_KEYS = ["tipo", "anexo_id", "tarefa", "serve_handoff", "base_commit", "status"]
ANEXO_STATUS = ("ATIVO", "CONSUMIDO")
ANEXO_MAX_LINES = 80
ANEXO_MIN_COPY = 120
ANEXO_DIRS = ("governance/propostas", "docs/handoffs/anexos")


def git(root, *args):
    try:
        r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
    except OSError:
        return None
    return r.stdout if r.returncode == 0 else None


def parse(text):
    """(frontmatter dict, corpo). Frontmatter = bloco '---' inicial, 'chave: valor'."""
    fm, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for ln in m.group(1).split("\n"):
            k, sep, v = ln.partition(":")
            if sep:
                fm[k.strip()] = v.strip()
        body = text[m.end():]
    return fm, body


def analyze(root: Path, today=None):
    f = []  # (sev, id, msg)
    hp = root / "HANDOFF.md"
    if not hp.exists():
        return [("ERRO", "HO-01", "HANDOFF.md ausente na raiz")], None
    text = hp.read_text(encoding="utf-8", errors="replace")
    fm, body = parse(text)
    lines = text.split("\n")

    # HO-01
    miss = [k for k in REQUIRED_KEYS if not fm.get(k)]
    if miss:
        f.append(("ERRO", "HO-01", f"frontmatter sem campo(s): {', '.join(miss)}"))
    secs = {int(n) for n in re.findall(r"^## (\d+)\.", body, re.M)}
    absent = [str(n) for n in range(1, 12) if n not in secs]
    if absent:
        f.append(("ERRO", "HO-01", f"seção(ões) ausente(s): {', '.join(absent)}"))

    # HO-05
    if len(lines) > MAX_LINES:
        f.append(("WARN", "HO-05", f"{len(lines)} linhas (> {MAX_LINES}); mover excedente para o arquivo"))

    # HO-02 / HO-03 / HO-04 (precisam de git)
    in_git = git(root, "rev-parse", "--git-dir") is not None
    last = None
    if not in_git:
        f.append(("INFO", "HO-02", "fora de repositório git: checagens HO-02/03/04 puladas"))
    else:
        base = fm.get("base_commit", "")
        if base and git(root, "cat-file", "-e", f"{base}^{{commit}}") is None:
            f.append(("ERRO", "HO-02", f"base_commit {base} não existe no histórico"))
        elif base:
            r = subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", base, "HEAD"])
            if r.returncode != 0:
                f.append(("ERRO", "HO-02", f"base_commit {base} não é ancestral de HEAD"))
        last_out = git(root, "log", "-1", "--format=%H", "--", "HANDOFF.md")
        last = last_out.strip() if last_out else None
        # HO-03
        if last:
            out = git(root, "log", "--no-merges", "--name-only", "--format=@@%s", f"{last}..HEAD")
            if out is not None:
                changed, skip = set(), False
                for ln in out.split("\n"):
                    if ln.startswith("@@"):
                        skip = ln[2:].startswith("RPSA:")
                    elif ln.strip() and not skip and not ln.startswith(IGNORED_PREFIXES):
                        changed.add(ln.strip())
                if changed:
                    f.append(("WARN", "HO-03",
                              f"{len(changed)} arquivo(s) mudaram depois do último commit do HANDOFF.md "
                              f"sem novo handoff (ex.: {sorted(changed)[0]})"))
        # HO-04
        prev = fm.get("previous", "")
        if prev and prev.lower() != "null":
            arch = root / "docs" / "handoffs" / f"{prev}.md"
            if not arch.exists():
                f.append(("ERRO", "HO-04", f"previous {prev} não arquivado em docs/handoffs/"))
            else:
                head = git(root, "show", "HEAD:HANDOFF.md")
                if head is not None and head != text:
                    ref = head  # handoff reescrito e ainda não commitado: o substituído é o de HEAD
                elif last and git(root, "rev-parse", f"{last}^") is not None:
                    ref = git(root, "show", f"{last}^:HANDOFF.md")
                else:
                    ref = None
                if ref is not None:
                    ref_id = parse(ref)[0].get("handoff_id")
                    if ref_id != prev:
                        f.append(("ERRO", "HO-04", f"previous={prev} mas o handoff substituído é {ref_id}"))
                    elif arch.read_text(encoding="utf-8", errors="replace") != ref:
                        f.append(("ERRO", "HO-04", f"{arch.name} difere do handoff que substituiu (arquivo deve ser cópia exata)"))

    # HO-06
    gov = root / "governance"
    names = [p.name for p in gov.glob("DHR-*")] if gov.exists() else []
    cat = (gov / "CATALOGO-OFICIAL.md").read_text(encoding="utf-8", errors="replace") if (gov / "CATALOGO-OFICIAL.md").exists() else ""
    for d in sorted(set(DHR.findall(body))):
        if not any(n.startswith(d + "_") or n == d + ".md" for n in names) and d not in cat:
            f.append(("ERRO", "HO-06", f"{d} citada sem ata em governance/ nem registro no CATALOGO"))
    open_ids = set()
    try:
        from check_doc_sync import Facts
        open_ids = set(Facts(root).decisions_open)
    except Exception:
        pass
    for i, ln in enumerate(lines, 1):
        if CLOSED_WORDS.search(ln) and not re.search(r"ABERT", ln, re.I):
            for oid in open_ids:
                if re.search(rf"(?<![A-Za-z0-9-]){re.escape(oid)}(?![A-Za-z0-9-])", ln):
                    f.append(("ERRO", "HO-06", f"L{i}: decisão ABERTA {oid} escrita como fechada/decidida (CONS-01)"))

    # HO-07
    road = (root / "ROADMAP.md")
    if road.exists() and fm.get("spec_autorizada"):
        for ln in road.read_text(encoding="utf-8", errors="replace").split("\n"):
            if re.match(r"\|\s*Próximo trabalho autorizado\s*\|", ln):
                m = re.search(r"SPEC-\d{3}", ln)
                if m and m.group(0) not in fm["spec_autorizada"]:
                    f.append(("WARN", "HO-07",
                              f"spec_autorizada='{fm['spec_autorizada'][:40]}' difere do ROADMAP ({m.group(0)}); ROADMAP prevalece"))
                break

    # HO-08
    for i, ln in enumerate(lines, 1):
        if SECRET.search(ln):
            f.append(("ERRO", "HO-08", f"L{i}: possível segredo/credencial"))

    # HO-09
    for i, ln in enumerate(lines, 1):
        if HOMOLOG_WORDS.search(ln) and not DHR.search(ln) and not re.search(r"pendente|aguard|não|nao|sem |nunca", ln, re.I):
            f.append(("WARN", "HO-09", f"L{i}: linguagem de homologação/baseline sem ID DHR na linha"))

    # HO-10 — lembretes datados: não depende de memória de sessão; o hook SessionStart mostra o WARN
    hoje = today or datetime.date.today()
    for i, ln in enumerate(lines, 1):
        for m in PRAZO.finditer(ln):
            try:
                d = datetime.date.fromisoformat(m.group(1))
            except ValueError:
                f.append(("WARN", "HO-10", f"L{i}: [PRAZO: {m.group(1)}] com data inválida"))
                continue
            if hoje >= d:
                txt = PRAZO.sub("", ln).strip(" -*")[:110]
                f.append(("WARN", "HO-10", f"L{i}: pendência vencida em {d.isoformat()} — {txt}"))
    f.extend(analyze_anexos(root, fm, open_ids, names, cat, in_git))
    return f, fm


def _is_anexo(text):
    fm, _ = parse(text)
    return fm.get("tipo") == "anexo-de-tarefa"


def find_anexos(root: Path):
    """Arquivos .md com frontmatter `tipo: anexo-de-tarefa` em governance/propostas e docs/handoffs/anexos."""
    out = []
    for d in ANEXO_DIRS:
        base = root / d
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.md")):
            try:
                head = p.read_text(encoding="utf-8", errors="replace")[:800]
            except OSError:
                continue
            if _is_anexo(head + "\n"):
                out.append(p)
    return out


def analyze_anexos(root, hfm, open_ids, dhr_names, cat, in_git):
    """Anexo de tarefa (DHR-PCC-003): extensão do HANDOFF, no máximo um ATIVO, só ponteiros. Detector, não Gate (ENF-03)."""
    f = []
    cited = (hfm or {}).get("anexo", "")
    cited = "" if cited.lower() in ("", "null", "nenhum") else cited
    all_anexos = find_anexos(root)
    rel = lambda p: p.relative_to(root).as_posix()
    ativos = []
    for p in all_anexos:
        afm, _ = parse(p.read_text(encoding="utf-8", errors="replace"))
        if afm.get("status") == "ATIVO":
            ativos.append(rel(p))
    if len(ativos) > 1:
        f.append(("WARN", "HO-12", f"{len(ativos)} anexos ATIVO ao mesmo tempo (máximo 1): {', '.join(ativos)}"))
    for a in ativos:
        if a != cited:
            f.append(("WARN", "HO-12", f"anexo ATIVO {a} não é citado pelo campo `anexo:` do handoff (órfão/ambíguo)"))
    if not cited:
        return f
    ap = root / cited
    if not ap.exists():
        f.append(("ERRO", "HO-11", f"`anexo: {cited}` aponta arquivo inexistente"))
        return f
    atext = ap.read_text(encoding="utf-8", errors="replace")
    afm, abody = parse(atext)
    alines = atext.split("\n")
    miss = [k for k in ANEXO_KEYS if not afm.get(k)]
    if miss:
        f.append(("ERRO", "HO-11", f"anexo {cited}: frontmatter sem campo(s) {', '.join(miss)}"))
    if afm.get("tipo") and afm.get("tipo") != "anexo-de-tarefa":
        f.append(("ERRO", "HO-11", f"anexo {cited}: tipo='{afm.get('tipo')}' (esperado anexo-de-tarefa)"))
    if afm.get("status") and afm["status"] not in ANEXO_STATUS:
        f.append(("ERRO", "HO-11", f"anexo {cited}: status='{afm['status']}' fora de {'|'.join(ANEXO_STATUS)}"))
    if afm.get("status") == "CONSUMIDO":
        f.append(("WARN", "HO-12", f"anexo {cited} está CONSUMIDO mas o handoff ainda o cita: arquive em docs/handoffs/anexos/ e limpe `anexo:`"))
    if in_git and afm.get("base_commit"):
        b = afm["base_commit"]
        if git(root, "cat-file", "-e", f"{b}^{{commit}}") is None:
            f.append(("WARN", "HO-11", f"anexo {cited}: base_commit {b} não existe no histórico"))
    if len(alines) > ANEXO_MAX_LINES:
        f.append(("WARN", "HO-13", f"anexo {cited}: {len(alines)} linhas (> {ANEXO_MAX_LINES}); só ponteiros, sem copiar"))
    for d in sorted(set(DHR.findall(abody))):
        if not any(n.startswith(d + "_") or n == d + ".md" for n in dhr_names) and d not in cat:
            f.append(("ERRO", "HO-14", f"anexo {cited}: {d} citada sem ata em governance/ nem registro no CATALOGO"))
    for i, ln in enumerate(alines, 1):
        if CLOSED_WORDS.search(ln) and not re.search(r"ABERT", ln, re.I):
            for oid in open_ids:
                if re.search(rf"(?<![A-Za-z0-9-]){re.escape(oid)}(?![A-Za-z0-9-])", ln):
                    f.append(("ERRO", "HO-14", f"anexo {cited} L{i}: decisão ABERTA {oid} escrita como fechada/decidida (CONS-01)"))
        if SECRET.search(ln):
            f.append(("ERRO", "HO-14", f"anexo {cited} L{i}: possível segredo/credencial"))
    # HO-15 — "aponte, não copie" (PCC-001): linha longa repetida literalmente em fonte de verdade
    fontes = {}
    for src in [root / "HANDOFF.md", root / "ROADMAP.md", *sorted((root / "governance").glob("DHR-*.md"))]:
        try:
            fontes[src.name] = src.read_text(encoding="utf-8", errors="replace")
        except OSError:
            pass
    for i, ln in enumerate(alines, 1):
        t = ln.strip(" -*>|\t")
        if len(t) >= ANEXO_MIN_COPY:
            for nome, txt in fontes.items():
                if t in txt:
                    f.append(("WARN", "HO-15", f"anexo {cited} L{i}: linha longa copiada de {nome} (aponte por ID/linha, não copie)"))
                    break
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--hoje", default=None, help="AAAA-MM-DD (testes); padrão: data do sistema")
    a = ap.parse_args()
    findings, fm = analyze(Path(a.root), datetime.date.fromisoformat(a.hoje) if a.hoje else None)
    order = {"ERRO": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda x: (order[x[0]], x[1]))
    counts = {k: sum(1 for x in findings if x[0] == k) for k in order}
    if a.json:
        print(json.dumps({"handoff_id": (fm or {}).get("handoff_id"),
                          "achados": [{"severidade": s, "id": i, "mensagem": m} for s, i, m in findings],
                          "contagens": counts}, ensure_ascii=False, indent=1))
    else:
        print("=" * 60)
        print(f"VERIFICADOR DE HANDOFF — check_handoff.py ({(fm or {}).get('handoff_id', 'sem handoff')})")
        print("=" * 60)
        for s, i, m in findings:
            print(f"[{s}] {i} — {m}")
        print("-" * 60)
        print(f"ERRO={counts['ERRO']} WARN={counts['WARN']} INFO={counts['INFO']}")
        print("Somente leitura — Detector (ENF-03): não escreve o handoff, não fecha decisão (CONS-01).")
        print("LEMBRETE: exit 0 ≠ CONFORME ≠ homologação.")
    sys.exit(1 if counts["ERRO"] or (a.strict and counts["WARN"]) else 0)


if __name__ == "__main__":
    main()
