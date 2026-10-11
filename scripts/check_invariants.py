#!/usr/bin/env python3
"""
check_invariants.py — detector de VALORES e ORDEM das regras fixas do SOT em textos de Spec (DHR-AUDITOR-EXTERNO-008, R2).

Somente leitura. Complementa o validate_spec_sot.py, que confere a FORMA da Spec e a decisão aberta tratada como
fechada (STRUCT-07/10) mas não confere os VALORES: R:R, score, convicção, número de dimensões, hierarquia, estados
da hipótese, ordem dos 4Es e validade do Dossiê. Cada constante abaixo cita sua fonte (AGENTS.md); tests/test_check_invariants.py
verifica que a fonte ainda diz o mesmo (alarme de deriva) — o linter NÃO é segunda fonte da verdade.

Detector ≠ Gate (ENF-03): informativo, nunca bloqueia, nunca decide, nunca homologa. Falso alarme e falso negativo são
possíveis (análise por linha); quem julga é o Revisor, quem decide é Andraus.

Uso:
    python scripts/check_invariants.py arquivo.md [outro.md ...]
    python scripts/check_invariants.py                # specs/features/*/plan.md
    python scripts/check_invariants.py --strict ...   # exit 1 se houver achado (padrão: exit 0)
"""
import argparse
import glob
import re
import sys
from pathlib import Path

# ---- constantes e fontes (a fonte é verificada por teste contra o AGENTS.md) --------------------------------------
RR_MIN = 3.0                                                    # AGENTS.md §6 item 5: R:R mínimo 1:3 (≥ 3.0)
CONVICCAO_PILOTO = 70                                           # AGENTS.md §6 item 6: convicção ≥ 70% (Fase Piloto)
SCORE_PILOTO = 7                                                # AGENTS.md §6 item 6: score ≥ 7/9 (Fase Piloto)
DIMENSOES = 8                                                   # AGENTS.md §6 item 7: Conviction Vector = 8 dimensões
HIERARQUIA = ["Elliott", "Fibonacci", "Fractal", "SMC", "ICT"]  # AGENTS.md §6 item 1
ESTADOS = ["EMERGENT", "CANDIDATE", "ACTIVE", "DOMINANT", "SUPERSEDED", "REFUTED", "ARCHIVED"]   # AGENTS.md §6 item 3 (CHM-001)
ESTADOS_DESCONTINUADOS = ["PROPOSED", "VALIDATED"]              # RULE-BB-003 descontinuada (AGENTS.md §6 item 3)
QUATRO_ES = ["Conformidade", "Eficácia", "Efetividade", "Eficiência", "Economicidade"]            # AGENTS.md §6 item 11
DOSSIE_DIAS = {"LOW": 180, "MEDIUM": 120, "HIGH": 90, "CRITICAL": 90}                             # AGENTS.md §7 (ECC-VAL-001)
NUMEROS = {"sete": 7, "oito": 8, "nove": 9, "dez": 10, "seis": 6, "cinco": 5, "quatro": 4}

# Trechos do AGENTS.md que sustentam as constantes (conferidos por teste; normalizados sem espaços repetidos)
FONTES_AGENTS = {
    "R:R": "R:R mínimo 1:3",
    "convicção/score": "Convicção ≥ 70% e score ≥ 7/9",
    "dimensões": "8 dimensões",
    "hierarquia": "Elliott → Fibonacci → Fractal → SMC → ICT",
    "estados": "EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→ARCHIVED",
    "4Es": "Conformidade > Eficácia > Efetividade > Eficiência > Economicidade",
    "dossiê": "LOW 180 / MEDIUM 120 / HIGH-CRITICAL 90",
}

# linha que apenas CITA o valor errado como exemplo/histórico não é achado
EXCECAO = re.compile(r"descontinu|supersedid[oa]|superseded (?:por|by)|legad|exemplo|erro conhecido|COR-[A-Z]+-\d+|corrig", re.I)
NUM = r"(\d+(?:[.,]\d+)?)"


def _f(x):
    return float(x.replace(",", "."))


def _ordem(linha, termos, ignorar_case=False):
    """Posições de cada termo na linha, em ordem de aparição (só os presentes)."""
    flags = re.I if ignorar_case else 0
    achados = []
    for t in termos:
        m = re.search(r"\b" + re.escape(t) + r"\b", linha, flags)
        if m:
            achados.append((m.start(), t))
    return [t for _, t in sorted(achados)]


def _corrente(linha, termos, seta, minimo):
    """Maior corrente contínua 'T1 seta T2 seta T3…' com termos da lista (na ordem em que aparecem), se tiver ≥ minimo."""
    alt = "|".join(re.escape(t) for t in termos)
    best = []
    for m in re.finditer(r"\b(?:%s)\b(?:\s*(?:%s)\s*\b(?:%s)\b)+" % (alt, seta, alt), linha):
        cadeia = re.findall(r"\b(?:%s)\b" % alt, m.group(0))
        if len(cadeia) > len(best):
            best = cadeia
    return best if len(best) >= minimo else []


def _fora_de_ordem(visto, canonico):
    idx = [canonico.index(t) for t in visto]
    return idx != sorted(idx)


def checar_linha(linha):
    """Retorna lista de (codigo, mensagem, fonte) para uma linha de texto."""
    out = []
    if EXCECAO.search(linha):
        return out

    # R:R mínimo
    if re.search(r"R:R", linha):
        for m in re.finditer(r"1\s*:\s*" + NUM, linha):
            if _f(m.group(1)) < RR_MIN:
                out.append(("INV-RR", f"R:R 1:{m.group(1)} abaixo do mínimo 1:3 (≥ 3.0)", "AGENTS.md §6 item 5"))
        for m in re.finditer(r"(?:inferior a|abaixo de|mínimo|minimo|≥|>=)\s*" + NUM, linha):
            v = _f(m.group(1))
            if v < RR_MIN and not re.match(r"1\s*:", linha[m.start(1):]):
                out.append(("INV-RR", f"R:R mínimo {m.group(1)} abaixo de 3.0", "AGENTS.md §6 item 5"))
        if re.search(r"R:R[^|\n]*\|\s*" + NUM + r"\s*(\||$)", linha):                       # linha de tabela "R:R mínimo | 2.5"
            v = _f(re.search(r"R:R[^|\n]*\|\s*" + NUM, linha).group(1))
            if v < RR_MIN:
                out.append(("INV-RR", f"R:R mínimo {v:g} (tabela) abaixo de 3.0", "AGENTS.md §6 item 5"))

    # score mínimo
    for m in re.finditer(r"score[^.\n|]{0,30}?(\d)\s*/\s*9", linha, re.I):
        if re.search(r"≥|>=|m[ií]nimo", linha) and int(m.group(1)) < SCORE_PILOTO:
            out.append(("INV-SCORE", f"score mínimo {m.group(1)}/9 diverge do limiar de Fase Piloto 7/9", "AGENTS.md §6 item 6"))

    # convicção mínima
    if re.search(r"convic[çc][ãa]o", linha, re.I) and not re.search(r"maturidade|bias", linha, re.I):
        for m in re.finditer(r"(?:≥|>=|m[ií]nim\w*(?:\s+de)?|limiar(?:\s+de)?)\s*" + NUM + r"\s*%", linha, re.I):
            if _f(m.group(1)) != CONVICCAO_PILOTO:
                out.append(("INV-CONVICCAO", f"convicção mínima {m.group(1)}% diverge do limiar de Fase Piloto 70%", "AGENTS.md §6 item 6"))

    # dimensões do Conviction Vector
    for m in re.finditer(r"\b(\d+|" + "|".join(NUMEROS) + r")\s+dimens", linha, re.I):
        n = int(m.group(1)) if m.group(1).isdigit() else NUMEROS[m.group(1).lower()]
        if n != DIMENSOES and re.search(r"vetor|conviction", linha, re.I):
            out.append(("INV-DIM", f"{n} dimensões no vetor; o canônico tem {DIMENSOES}", "AGENTS.md §6 item 7"))
    if re.search(r"estrutural", linha, re.I) and re.search(r"geom[ée]trica", linha, re.I) and re.search(r"\bcusto\b", linha, re.I):
        out.append(("INV-DIM", "'custo' listado entre as dimensões do vetor (custo nunca entra: INV-04)", "AGENTS.md §6 item 8"))

    # hierarquia de camadas
    vis = _corrente(linha, HIERARQUIA, r"→|->", 3)
    if vis and _fora_de_ordem(vis, HIERARQUIA):
        out.append(("INV-HIER", f"hierarquia fora de ordem: {' → '.join(vis)}", "AGENTS.md §6 item 1"))
    m = re.search(r"\b(\w+)\s+camadas", linha, re.I)
    if m and set(HIERARQUIA) <= set(re.findall(r"Elliott|Fibonacci|Fractal|SMC|ICT", linha)):
        n = NUMEROS.get(m.group(1).lower(), int(m.group(1)) if m.group(1).isdigit() else None)
        if n is not None and n != len(HIERARQUIA):
            out.append(("INV-HIER", f"{n} camadas declaradas; são {len(HIERARQUIA)}", "AGENTS.md §6 item 1"))

    # estados da hipótese
    for e in ESTADOS_DESCONTINUADOS:
        if re.search(r"\b" + e + r"\b", linha) and re.search(r"→|estado", linha, re.I):
            out.append(("INV-ESTADO", f"estado {e} é da RULE-BB-003 descontinuada (use os 7 estados do CHM-001)", "AGENTS.md §6 item 3"))
    ve = _corrente(linha, ESTADOS, r"→|->", 4)
    if ve and _fora_de_ordem(ve, ESTADOS):
        out.append(("INV-ESTADO", f"estados do CHM-001 fora de ordem: {' → '.join(ve)}", "AGENTS.md §6 item 3"))
    m = re.search(r"\b(\w+)\s+estados\b", linha, re.I)
    if m and len(_ordem(linha, ESTADOS)) >= 4:
        n = NUMEROS.get(m.group(1).lower(), int(m.group(1)) if m.group(1).isdigit() else None)
        if n is not None and n != len(ESTADOS):
            out.append(("INV-ESTADO", f"{n} estados declarados; o CHM-001 tem {len(ESTADOS)}", "AGENTS.md §6 item 3"))

    # ordem dos 4Es
    v4 = _corrente(linha, QUATRO_ES, r">", 3)
    if v4 and _fora_de_ordem(v4, QUATRO_ES):
        out.append(("INV-4ES", f"ordem dos 4Es invertida: {' > '.join(v4)}", "AGENTS.md §6 item 11"))

    # validade do Dossiê por complexidade
    if re.search(r"dossi", linha, re.I):
        cx = set(re.findall(r"\b(LOW|MEDIUM|HIGH|CRITICAL)\b", linha))
        dias = re.findall(r"(\d+)\s*dias", linha)
        if len(cx) == 1 and len(dias) == 1:
            c, d = next(iter(cx)), int(dias[0])
            if d != DOSSIE_DIAS[c]:
                out.append(("INV-DOSSIE", f"validade do Dossiê {c} = {d} dias; o canônico é {DOSSIE_DIAS[c]}", "AGENTS.md §7 (ECC-VAL-001)"))
    return out


def checar_texto(texto):
    achados = []
    for i, linha in enumerate(texto.splitlines(), 1):
        for cod, msg, fonte in checar_linha(linha):
            achados.append((i, cod, msg, fonte))
    return achados


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("arquivos", nargs="*")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args(argv)
    arquivos = a.arquivos or sorted(glob.glob("specs/features/*/plan.md"))
    total = 0
    for arq in arquivos:
        p = Path(arq)
        if not p.is_file():
            print(f"{arq}: arquivo não encontrado")
            continue
        for linha, cod, msg, fonte in checar_texto(p.read_text(encoding="utf-8", errors="replace")):
            print(f"{arq}:{linha} [{cod}] {msg} (fonte: {fonte})")
            total += 1
    print(f"ACHADOS={total} em {len(arquivos)} arquivo(s)")
    print("LEMBRETE: detector informativo. exit 0 ≠ CONFORME ≠ homologação; o Revisor audita, Andraus decide.")
    return 1 if (a.strict and total) else 0


if __name__ == "__main__":
    sys.exit(main())
