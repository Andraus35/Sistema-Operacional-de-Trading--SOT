#!/usr/bin/env python3
"""
merge_ready.py — detector DETERMINÍSTICO de "já é possível e seguro mesclar" (DHR-MERGE-001; ordem de Andraus, 2026-10-30).

Uso:  python scripts/merge_ready.py [--json]      (exit 0 = PRONTO; exit 1 = não pronto; exit 2 = indeterminado)

Critérios (TODOS objetivos, lidos de git local + API REST do GitHub via `gh api`; GraphQL não está disponível em sessões Claude Code):
  1. existe PR ABERTO cuja cabeça é o ramo atual, base = ramo padrão, não-rascunho;
  2. `mergeable_state == "clean"` (sem conflito; revisões/regras de proteção satisfeitas);
  3. a cabeça do PR == `git rev-parse HEAD` (nada local sem empurrar) e a árvore de trabalho está limpa;
  4. ≥ 1 check-run no commit da cabeça e TODOS concluídos com success/neutral/skipped (nenhum pendente, nenhum falho).
Informativo (não bloqueia): arquivos do PR que o CODEOWNERS reserva a Andraus — só ele aprova/mescla.
É Detector (ENF-03): NUNCA mescla, nunca aprova, nunca decide. Qualquer erro de rede/API => INDETERMINADO (não afirma "pronto").
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OK_CHECK = {"success", "neutral", "skipped"}


def sh(args, cwd=ROOT, timeout=20):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def gh_api(path, timeout=20):
    rc, out, err = sh(["gh", "api", path], timeout=timeout)
    if rc != 0:
        raise RuntimeError(f"gh api {path}: {err or out}"[:300])
    return json.loads(out)


def repo_slug(url):
    m = re.search(r"[/:]([^/:]+)/([^/]+?)(?:\.git)?/?$", url or "")
    return f"{m.group(1)}/{m.group(2)}" if m else None


def owners_paths(root=ROOT):
    """Caminhos que o CODEOWNERS reserva (linha `caminho  @dono`). Sem arquivo => []."""
    try:
        txt = (Path(root) / ".github" / "CODEOWNERS").read_text(encoding="utf-8")
    except OSError:
        return []
    return [ln.split()[0].lstrip("/") for ln in txt.splitlines() if ln.strip() and not ln.lstrip().startswith("#") and len(ln.split()) >= 2]


def avaliar(info):
    """Função pura. info: dict com pr (dict|None), head_local, sujo(bool), checks(list), arquivos(list), donos(list).
    -> (estado, motivos, extra)  estado em {'PRONTO','NAO_PRONTO'}."""
    pr = info.get("pr")
    mot = []
    if not pr:
        return "NAO_PRONTO", ["não há PR aberto para o ramo atual"], {}
    if pr.get("draft"):
        mot.append("PR em rascunho")
    if pr.get("mergeable_state") != "clean":
        mot.append(f"estado de mesclagem '{pr.get('mergeable_state')}' (precisa ser 'clean': conflito, revisão pendente ou checks obrigatórios)")
    if pr.get("head_sha") != info.get("head_local"):
        mot.append("a cabeça do PR difere do HEAD local (há commit sem empurrar ou PR desatualizado)")
    if info.get("sujo"):
        mot.append("árvore de trabalho com mudanças não commitadas")
    checks = info.get("checks") or []
    if not checks:
        mot.append("nenhum check-run no commit da cabeça (CI ainda não rodou)")
    for c in checks:
        if c.get("status") != "completed":
            mot.append(f"check '{c.get('name')}' ainda não terminou ({c.get('status')})")
        elif c.get("conclusion") not in OK_CHECK:
            mot.append(f"check '{c.get('name')}' terminou '{c.get('conclusion')}'")
    donos = info.get("donos") or []
    tocados = sorted({a for a in (info.get("arquivos") or []) for d in donos if a == d or (d.endswith("/") and a.startswith(d))})
    extra = {"numero": pr.get("number"), "cabeca": pr.get("head_sha"), "url": pr.get("html_url"), "titulo": pr.get("title"), "arquivos_de_andraus": tocados,
             "arquivos_total": len(info.get("arquivos") or [])}
    return ("NAO_PRONTO" if mot else "PRONTO"), mot, extra


def coletar(root=ROOT, api=gh_api, runner=sh):
    rc, ramo, _ = runner(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=root)
    rc2, head, _ = runner(["git", "rev-parse", "HEAD"], cwd=root)
    rc3, url, _ = runner(["git", "remote", "get-url", "origin"], cwd=root)
    slug = repo_slug(url)
    if rc or rc2 or rc3 or not slug or ramo in ("", "HEAD"):
        raise RuntimeError("repositório/ramo não identificável")
    dono = slug.split("/")[0]
    _, status, _ = runner(["git", "status", "--porcelain"], cwd=root)
    lista = api(f"repos/{slug}/pulls?state=open&head={dono}:{ramo}&per_page=5")
    if not lista:
        return {"pr": None, "head_local": head, "sujo": bool(status)}
    num = lista[0]["number"]
    pr = api(f"repos/{slug}/pulls/{num}")
    sha = pr["head"]["sha"]
    checks = api(f"repos/{slug}/commits/{sha}/check-runs?per_page=100").get("check_runs", [])
    arquivos = [f["filename"] for f in api(f"repos/{slug}/pulls/{num}/files?per_page=100")]
    return {
        "pr": {"number": num, "draft": pr.get("draft"), "mergeable_state": pr.get("mergeable_state"), "head_sha": sha,
               "html_url": pr.get("html_url"), "title": pr.get("title"), "base": pr["base"]["ref"]},
        "head_local": head, "sujo": bool(status),
        "checks": [{"name": c.get("name"), "status": c.get("status"), "conclusion": c.get("conclusion")} for c in checks],
        "arquivos": arquivos, "donos": owners_paths(root),
    }


def main(argv):
    como_json = "--json" in argv
    try:
        estado, motivos, extra = avaliar(coletar())
    except Exception as e:  # fail-safe: indeterminado nunca afirma "pronto"
        saida = {"estado": "INDETERMINADO", "motivos": [str(e)[:300]], "extra": {}}
        print(json.dumps(saida, ensure_ascii=False) if como_json else f"INDETERMINADO: {saida['motivos'][0]}")
        return 2
    saida = {"estado": estado, "motivos": motivos, "extra": extra}
    if como_json:
        print(json.dumps(saida, ensure_ascii=False))
    else:
        print(f"{estado}" + (": " + "; ".join(motivos) if motivos else f" — PR #{extra.get('numero')} {extra.get('url')}"))
        if extra.get("arquivos_de_andraus"):
            print("Toca arquivos reservados a Andraus (CODEOWNERS): " + ", ".join(extra["arquivos_de_andraus"]))
    return 0 if estado == "PRONTO" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
