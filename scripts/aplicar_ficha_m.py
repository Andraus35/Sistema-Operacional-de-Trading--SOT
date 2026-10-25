#!/usr/bin/env python3
"""aplicar_ficha_m.py — correção DETERMINÍSTICA de achados MENORES mecânicos pelo Orquestrador (classe M; DHR-ROTEAMENTO-006).

O Revisor entrega, no parecer, um bloco `<!-- FICHA-M {json} -->` (ou um arquivo .json) com os Menores mecânicos:
  {"achados":[{"id","sev":"MENOR","arquivo","antigo","novo","condicao"}]}
Este script IDENTIFICA o que é mecânico, CORRIGE por substituição exata de texto (âncora = o texto `antigo`, não o número da linha:
imune à deriva de linhas) e VERIFICA que só as linhas previstas mudaram. O que não for mecânico não é tocado e sai listado
como ESCALA ao Especificador (classe O). Nunca corrige Média/Crítica nem altera semântica (RULE: o Orquestrador não cria
regra/campo/ID/mecanismo). Atômico: qualquer falha na verificação restaura os arquivos.

Critérios por achado (todos objetivos): sev == MENOR · arquivo dentro do repositório · `antigo` ocorre EXATAMENTE 1 vez no arquivo ·
`novo` != `antigo` e mesmo número de linhas · `condicao` não vazia · `novo` não introduz ID normativo (RULE|INV|ENF|STRUCT|CKG|WF|DHR|EUA)
inexistente em `antigo` · arquivo sem edições não commitadas de outro agente (quando em git) · lote ≤ 10 linhas e ≤ 2 arquivos.

Uso:
  python scripts/aplicar_ficha_m.py <parecer.md|ficha.json> [--dry] [--saida FICHA.json]
Saída: JSON {aplicados, escalados[{id,motivo}], arquivos}; exit 0 = todos os mecânicos aplicados/verificados; exit 1 = há ESCALA
(os escalados vão ao Especificador) ou falha de verificação (nada foi alterado). Detector/rotina de forma (ENF-03): não julga mérito.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roteador_modelos as R  # noqa: E402  (constantes e _cria_algo; arquivo selado, só lido)

ROOT = Path(__file__).resolve().parent.parent
BLOCO = re.compile(r"<!--\s*FICHA-M\s*(.*?)-->", re.S)


def carregar(caminho):
    p = Path(caminho)
    txt = p.read_text(encoding="utf-8")
    if p.suffix.lower() == ".json":
        return json.loads(txt).get("achados") or []
    m = BLOCO.search(txt)
    if not m:
        return []
    return json.loads(m.group(1)).get("achados") or []


def _sujo(root, arq):
    """True se o arquivo tem edições não commitadas (quando em git); fora do git => False."""
    try:
        dentro = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
        if dentro.returncode != 0 or Path(dentro.stdout.strip()).resolve() != Path(root).resolve():
            return False
        r = subprocess.run(["git", "-C", str(root), "diff", "--quiet", "HEAD", "--", arq], capture_output=True)
        return r.returncode == 1
    except OSError:
        return False


def avaliar(a, root):
    """-> None se o achado é mecânico aplicável, ou o motivo da ESCALA."""
    if str(a.get("sev", "")).upper() != "MENOR":
        return "severidade não é MENOR (Média/Crítica nunca é corrigida pelo Orquestrador)"
    arq, antigo, novo = a.get("arquivo"), a.get("antigo"), a.get("novo")
    if not isinstance(arq, str) or not arq.strip():
        return "arquivo ausente"
    p = (Path(root) / arq).resolve()
    try:
        p.relative_to(Path(root).resolve())
    except ValueError:
        return "arquivo fora do repositório"
    if not p.is_file():
        return "arquivo inexistente"
    if not isinstance(antigo, str) or not antigo or not isinstance(novo, str) or novo == antigo:
        return "antigo/novo ausentes ou iguais"
    if not str(a.get("condicao") or "").strip():
        return "condição verificável ausente"
    if len(antigo.splitlines()) != len(novo.splitlines()):
        return "substituição muda o número de linhas (inserção/remoção não é mecânica)"
    if R._cria_algo(a):
        return "cria regra/campo/mecanismo/ID normativo novo"
    n = p.read_text(encoding="utf-8").count(antigo)
    if n != 1:
        return f"texto antigo ocorre {n} vez(es) no arquivo (exige exatamente 1)"
    return None


def aplicar(achados, root=ROOT, dry=False):
    root = Path(root)
    aplic, escal = [], []
    for a in achados:
        motivo = avaliar(a, root)
        if motivo is None and _sujo(root, a["arquivo"]):
            motivo = "arquivo com edições não commitadas (outro agente editando); aplicar só com a árvore limpa"
        (escal.append({"id": a.get("id"), "motivo": motivo}) if motivo else aplic.append(a))
    # tetos do lote (excedente escala ao Especificador)
    ok, arqs, linhas = [], set(), 0
    for a in aplic:
        n = max(1, len(a["antigo"].splitlines()))
        novo_arqs = arqs | {a["arquivo"]}
        if len(novo_arqs) > R.MAX_ARQUIVOS_M or linhas + n > R.MAX_LINHAS_M:
            escal.append({"id": a.get("id"), "motivo": "lote M acima do teto (10 linhas / 2 arquivos): excedente vai ao Especificador"})
            continue
        ok.append(a)
        arqs, linhas = novo_arqs, linhas + n
    if dry or not ok:
        return {"aplicados": [a["id"] for a in ok] if not dry else [], "previstos": [a["id"] for a in ok], "escalados": escal,
                "arquivos": sorted(arqs)}, ok, {}
    originais = {}
    try:
        for a in ok:
            p = Path(root) / a["arquivo"]
            originais.setdefault(a["arquivo"], p.read_text(encoding="utf-8"))
        novos = dict(originais)
        esperadas = {}
        for a in ok:
            txt = novos[a["arquivo"]]
            if txt.count(a["antigo"]) != 1:
                raise ValueError(f"{a['id']}: texto antigo deixou de ser único após outra substituição do lote")
            ini = txt.index(a["antigo"])
            lin = txt.count("\n", 0, ini) + 1
            esperadas.setdefault(a["arquivo"], set()).update(range(lin, lin + max(1, len(a["antigo"].splitlines()))))
            novos[a["arquivo"]] = txt.replace(a["antigo"], a["novo"], 1)
        for arq, txt in novos.items():
            (Path(root) / arq).write_text(txt, encoding="utf-8")
        # verificação: só as linhas previstas mudaram e o texto novo está lá
        for arq, txt in novos.items():
            a_l, b_l = originais[arq].splitlines(), txt.splitlines()
            if len(a_l) != len(b_l):
                raise ValueError(f"{arq}: número de linhas mudou")
            mudou = {i + 1 for i, (x, y) in enumerate(zip(a_l, b_l)) if x != y}
            if not mudou <= esperadas[arq] or not mudou:
                raise ValueError(f"{arq}: linhas alteradas fora do previsto: {sorted(mudou - esperadas[arq])[:10]}")
        for a in ok:
            if a["novo"] not in novos[a["arquivo"]]:
                raise ValueError(f"{a['id']}: texto novo não encontrado após a aplicação")
    except Exception as e:  # atômico: restaura tudo
        for arq, txt in originais.items():
            (Path(root) / arq).write_text(txt, encoding="utf-8")
        return {"aplicados": [], "escalados": escal + [{"id": a.get("id"), "motivo": f"verificação falhou: {e}"} for a in ok],
                "arquivos": []}, [], originais
    return {"aplicados": [a["id"] for a in ok], "escalados": escal, "arquivos": sorted(arqs)}, ok, originais


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("fonte")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--saida")
    ap.add_argument("--root", default=str(ROOT))
    a = ap.parse_args(argv)
    achados = carregar(a.fonte)
    if not achados:
        print(json.dumps({"aplicados": [], "escalados": [], "arquivos": [], "nota": "nenhuma FICHA-M no parecer"}, ensure_ascii=False))
        return 0
    rel, ok, _ = aplicar(achados, a.root, a.dry)
    if a.saida and ok:
        Path(a.saida).write_text(json.dumps({"achados": ok}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(rel, ensure_ascii=False, indent=1))
    return 1 if rel["escalados"] else 0


if __name__ == "__main__":
    sys.exit(main())
