#!/usr/bin/env python3
"""fsm_check.py — confere a tabela de estados (D5) contra os cenários e adversariais do Plan (proposta P16; informativo).

Problema (retrospectiva SPEC-008; ledger C10): transição sem linha, falha sem estado, guarda inalcançável; a "simulação da D4.2"
era feita à mão e falhou 3 rodadas. Este detector só LÊ e informa. Detector (ENF-03): não corrige, não decide, não fecha decisão
aberta (CONS-01). Convenção de tabela legível por máquina: ver `governance/propostas/MELHORIAS-PROCESSO/CONVENCAO-TABELA-FSM.md`.

Uso:
  python scripts/fsm_check.py <plan.md> [--efeitos "despacha=DISPATCH_PUBLISH_FAILED,invoca=MACRO_ERROR"] [--aciclico]
                                        [--strict] [--json]

Tabela D5 = primeira tabela markdown cujo cabeçalho tem as colunas `ID`, `Estado`, `Evento`, `Próximo` (e, opcional, `Ação`,
`Código`). Tokens entre crases e em MAIÚSCULAS contam como estado/evento/código; `—`/`qualquer`/`ENC` não são estados.

Verificações:
  (i)   citação `fsm_row`/`Fnn` de cenário (`### Cenário-…`) ou adversarial (`### ADV-…`) cujo ID não existe na tabela;
        evento MAIÚSCULO citado em cenário/ADV que não é evento da tabela nem aparece fora de cenário/ADV;
        código (`PREFIXO_…`, prefixo = o mais comum dos códigos da tabela) citado em cenário/ADV sem linha na tabela e sem
        declaração fora de cenário/ADV
  (ii)  linha cujo estado de origem é inalcançável a partir do início (via `Próximo`); com --aciclico, ciclos entre estados
  (iii) com --efeitos `verbo=EVENTO_DE_FALHA`: linha cuja Ação contém o verbo e que não tem, em nenhuma linha da tabela, o evento
        de falha correspondente (efeito com falha possível sem linha de falha)
  (iv)  linhas da tabela nunca citadas por nenhum cenário/ADV (informativo: possível cobertura faltando)
Limite honesto: acha TEXTO e estrutura; não entende guarda semântica nem sinônimos; falso positivo em evento/código só-de-cenário
é esperado e é por isso que o detector é informativo.
"""
import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

_CRASES = re.compile(r"`([^`]+)`")
_ID_LINHA = re.compile(r"\bF\d+[a-z]?\b")
_TOK_EVENTO = re.compile(r"\b[A-Z][A-Z0-9]{2,}(?:_[A-Z0-9]+)+\b")
_NAO_ESTADO = {"QUALQUER", "ENC", "FINAL"}


def _norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def _celulas(linha):
    return [c.strip() for c in linha.strip().strip("|").split("|")]


def achar_tabela(texto):
    """Devolve (colunas, linhas) da primeira tabela com ID/Estado/Evento/Próximo, ou (None, [])."""
    ls = texto.splitlines()
    for i, ln in enumerate(ls):
        if not ln.lstrip().startswith("|"):
            continue
        cab = [_norm(c) for c in _celulas(ln)]
        if not {"id", "estado", "evento", "proximo"} <= {c.split(" ")[0] for c in cab}:
            continue
        idx = {}
        for k, c in enumerate(cab):
            idx.setdefault(c.split(" ")[0], k)
        linhas, j = [], i + 2  # pula o separador
        while j < len(ls) and ls[j].lstrip().startswith("|"):
            cel = _celulas(ls[j])
            if len(cel) >= len(cab):
                linhas.append({"n": j + 1, "id": cel[idx["id"]].strip("`* "), "estado": cel[idx["estado"]],
                               "evento": cel[idx["evento"]], "proximo": cel[idx["proximo"]],
                               "acao": cel[idx["acao"]] if "acao" in idx else "",
                               "codigo": cel[idx["codigo"]] if "codigo" in idx else ""})
            j += 1
        return idx, linhas
    return None, []


def _tokens_crase(celula, so_maiuscula=True):
    out = []
    for t in _CRASES.findall(celula):
        t = re.split(r"[(\s]", t.strip())[0]
        if re.fullmatch(r"[A-ZÁÉÍÓÚÂÊÔÇÃ][A-ZÁÉÍÓÚÂÊÔÇÃ0-9_]*", t) or not so_maiuscula:
            out.append(t)
    return out


def estados_de(celula):
    return [t for t in _tokens_crase(celula) if t not in _NAO_ESTADO]


def eventos_de(celula):
    return [t for t in _tokens_crase(celula) if "_" in t or len(t) > 3]


def codigos_de(celula):
    return [t for t in _tokens_crase(celula) if "_" in t]


def _blocos_cenario(texto):
    """[(titulo, linha_inicial, [linhas])] das seções `### Cenário-…` e `### ADV-…`."""
    ls, out, cur = texto.splitlines(), [], None
    for i, ln in enumerate(ls, 1):
        if re.match(r"^#{2,4}\s+", ln):
            if cur:
                out.append(cur)
            cur = (ln, i, []) if re.match(r"^#{3,4}\s+(Cenário|ADV)-", ln) else None
        elif cur:
            cur[2].append(ln)
    if cur:
        out.append(cur)
    return out


def _texto_fora(texto, blocos):
    drop = set()
    for _t, ini, corpo in blocos:
        drop.update(range(ini, ini + len(corpo) + 1))
    return "\n".join(ln for i, ln in enumerate(texto.splitlines(), 1) if i not in drop)


def prefixo_codigos(linhas):
    c = Counter()
    for r in linhas:
        for t in codigos_de(r["codigo"]):
            c[t.split("_")[0]] += 1
    return c.most_common(1)[0][0] if c else None


def verificar(texto, efeitos=None, aciclico=False):
    """Devolve {'tabela_linhas': n, 'achados': [{'verif','msg','linha'}...]}."""
    idx, linhas = achar_tabela(texto)
    ach = []
    if not linhas:
        return {"tabela_linhas": 0, "achados": [{"verif": "tabela", "linha": 0,
                "msg": "nenhuma tabela com colunas ID/Estado/Evento/Próximo encontrada (convenção de máquina ausente)"}]}
    ids = {r["id"] for r in linhas}
    eventos = {e for r in linhas for e in eventos_de(r["evento"])}
    codigos = {c for r in linhas for c in codigos_de(r["codigo"])}
    prefixo = prefixo_codigos(linhas)
    blocos = _blocos_cenario(texto)
    fora = _texto_fora(texto, blocos)
    citados = set()
    # (i) citações dos cenários/ADV
    for titulo, ini, corpo in blocos:
        nome = re.sub(r"^#+\s+", "", titulo).split("—")[0].strip()
        for k, ln in enumerate(corpo, ini + 1):
            if "fsm_row" in ln or re.search(r"\bF\d+[a-z]?\b", ln):
                for f in _ID_LINHA.findall(ln):
                    citados.add(f)
                    if f not in ids and ("fsm_row" in ln or f.startswith("F")):
                        ach.append({"verif": "i", "linha": k, "msg": f"{nome}: cita linha {f} que não existe na tabela de estados"})
            for t in set(_TOK_EVENTO.findall(ln)):
                if prefixo and t.startswith(prefixo + "_"):
                    if t not in codigos and t not in fora:
                        ach.append({"verif": "i", "linha": k, "msg": f"{nome}: código {t} sem linha na tabela e sem declaração fora de cenário/ADV"})
                elif t.endswith(("_FIRED", "_FAILED", "_ERROR", "_EXCEEDED", "_RESULT", "_COMMAND", "_TRIGGERED", "_EXPIRED", "_CANCELLED", "_ARMED")):
                    if t not in eventos and t not in fora:
                        ach.append({"verif": "i", "linha": k, "msg": f"{nome}: evento {t} não é evento da tabela de estados"})
    # (ii) alcançabilidade
    destinos = {}
    for r in linhas:
        for o in estados_de(r["estado"]) or []:
            destinos.setdefault(o, set())
            destinos[o].update(estados_de(r["proximo"]))
    inicio = {s for r in linhas if re.match(r"^\s*(—|-|\(sem|qualquer)", r["estado"]) or not estados_de(r["estado"])
              for s in estados_de(r["proximo"])}
    alcanc, fila = set(inicio), list(inicio)
    while fila:
        s = fila.pop()
        for d in destinos.get(s, ()):
            if d not in alcanc:
                alcanc.add(d)
                fila.append(d)
    conhecidos = {d for r in linhas for d in estados_de(r["proximo"])}  # só vira "estado" quem é destino de alguma linha
    for r in linhas:
        for o in estados_de(r["estado"]):
            if o in conhecidos and o not in alcanc:
                ach.append({"verif": "ii", "linha": r["n"], "msg": f"{r['id']}: estado de origem `{o}` inalcançável a partir do início"})
    if aciclico:
        cor = {}

        def dfs(s, pilha):
            cor[s] = 1
            for d in destinos.get(s, ()):
                if d == s:
                    continue
                if cor.get(d) == 1:
                    ach.append({"verif": "ii", "linha": 0, "msg": "ciclo entre estados: " + " → ".join(pilha + [s, d])})
                elif d not in cor:
                    dfs(d, pilha + [s])
            cor[s] = 2
        for s in list(destinos):
            if s not in cor:
                dfs(s, [])
    # (iii) efeito com falha possível
    for verbo, falha in (efeitos or {}).items():
        tem = falha in eventos or any(falha in r["evento"] for r in linhas)
        for r in linhas:
            if _norm(verbo) in _norm(r["acao"]) and not tem:
                ach.append({"verif": "iii", "linha": r["n"], "msg": f"{r['id']}: ação '{verbo}' sem linha para o evento de falha {falha}"})
    # (iv) linhas nunca citadas
    for r in linhas:
        if r["id"] not in citados and _ID_LINHA.fullmatch(r["id"] or ""):
            ach.append({"verif": "iv", "linha": r["n"], "msg": f"{r['id']}: nenhum cenário/ADV cita esta linha (informativo)"})
    return {"tabela_linhas": len(linhas), "achados": ach}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("plan")
    ap.add_argument("--efeitos", default="", help="verbo=EVENTO_DE_FALHA,... (config do Plan)")
    ap.add_argument("--aciclico", action="store_true")
    ap.add_argument("--strict", action="store_true", help="exit 1 se houver achado de (i)/(ii)/(iii) (padrão: exit 0)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    ef = dict(p.split("=", 1) for p in a.efeitos.split(",") if "=" in p)
    res = verificar(Path(a.plan).read_text(encoding="utf-8", errors="replace"), ef, a.aciclico)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"fsm_check: {res['tabela_linhas']} linha(s) na tabela de estados")
        for x in res["achados"]:
            print(f"[{x['verif']}] L{x['linha']}: {x['msg']}")
        print(f"achados: {len(res['achados'])} (Detector informativo; exit 0 ≠ CONFORME ≠ homologação)")
    graves = [x for x in res["achados"] if x["verif"] in ("i", "ii", "iii", "tabela")]
    return 1 if (a.strict and graves) else 0


if __name__ == "__main__":
    sys.exit(main())
