#!/usr/bin/env python3
"""detectores_novos.py — protótipos C-1 e C-2 da auditoria do Especificador (PROPOSTA; não instalado; informativo).

C-1a  códigos_sem_definicao: código `PREFIXO_NOME` usado no texto mas nunca definido como 1ª célula de linha de tabela
      (e, inversamente, definido e nunca usado fora da definição).
C-1b  recusa_sem_codigo: linha normativa com verbo de recusa/fail-closed sem nenhum código nem remissão a tabela de códigos.
C-2   token_antigo_presente: tokens (IDs, códigos, números) retirados de linhas alteradas entre BASE e NOVO que ainda ocorrem
      no corpo vivo do NOVO ou nos arquivos irmãos (checks/research/ABERTURA). Exclui changelog/histórico (INV-07).
Detector ≠ Gate (ENF-03): levanta candidatos; quem julga o sentido é o Revisor. Somente leitura, sem rede, sem shell.
"""
import difflib, re

COD = re.compile(r"\b[A-Z]{2,}(?:_[A-Z0-9]{2,}){1,}\b")
DEF = re.compile(r"^\s*\|\s*`?(" + COD.pattern + r")`?\s*[|(/]")
HIST = re.compile(r"^\s*\|\s*\d+\.\d+(?:\.\d+)?\s*\|\s*20\d\d-\d\d-\d\d")      # linha de changelog `| 1.1 | 2026-..`
RECUSA = re.compile(r"\b(recusa|recusar|recusad[ao]|n[ãa]o emite|n[ãa]o compila|fail-closed|rejeita|rejeitar)\b", re.I)
EARS = re.compile(r"\b(DEVE|N[ÃA]O DEVE|Quando|Se )\b")
TOK = re.compile(r"\b(?:[A-Z]{2,}(?:[-_][A-Z0-9]+)+(?:-\d+)?|[A-Z]{2,}-\d+|\d{1,3}(?:\.\d{3})+|\d+[.,]\d+|\d{3,})\b")


def _vivo(texto):
    """linhas do corpo vivo: antes do primeiro `## Anexo`, sem changelog."""
    out = []
    for i, ln in enumerate(texto.splitlines(), 1):
        if re.match(r"^##\s+Anexo", ln):
            break
        if not HIST.match(ln):
            out.append((i, ln))
    return out


def regiao_codigos(texto):
    """linhas de TABELA sob cabeçalho que fala de códigos (ex.: `### D3.1 — Vocabulário unificado de códigos`)."""
    reg, dentro, nivel = [], False, 0
    for i, ln in enumerate(texto.splitlines(), 1):
        m = re.match(r"^(#{1,6})\s+(.*)", ln)
        if m:
            if re.search(r"c[óo]digos?|vocabul[áa]rio", m.group(2), re.I):
                dentro, nivel = True, len(m.group(1))
            elif dentro and len(m.group(1)) <= nivel:
                dentro = False
        elif dentro and ln.lstrip().startswith("|") and not HIST.match(ln):
            reg.append((i, ln))
    return reg


def codigos_sem_definicao(texto):
    definidos = {c for _, ln in regiao_codigos(texto) for c in COD.findall(ln)}
    pref = {c.split("_")[0] for c in definidos}          # só as famílias de prefixo que a tabela já usa (enums ficam fora)
    usos = {}
    for i, ln in _vivo(texto):
        for c in COD.findall(ln):
            usos.setdefault(c, []).append(i)
    return [(ls[0], f"código {c} usado ({len(ls)}x) e ausente da tabela de códigos") for c, ls in sorted(usos.items())
            if c not in definidos and c.split("_")[0] in pref and not c.startswith(("INV_", "RULE_", "CC_"))] if definidos else []


def recusa_sem_codigo(texto):
    ach = []
    for i, ln in _vivo(texto):
        if RECUSA.search(ln) and EARS.search(ln) and not COD.search(ln) and not re.search(r"D3\.1|tabela de c[óo]digos|c[óo]digo", ln, re.I):
            ach.append((i, "recusa/fail-closed sem código nem remissão à tabela de códigos: " + ln.strip()[:110]))
    return ach


def _tokens(s):
    return set(TOK.findall(s))


def _forma(tok):
    return re.sub(r"[A-Z]+", "A", re.sub(r"\d+", "9", tok))


def token_antigo_presente(base, novo, irmaos=None):
    """C-2 (renomeação): numa linha alterada, um token foi TROCADO por outro de mesma forma (1 sai, 1 entra); acusa onde o
    token antigo ainda ocorre no corpo vivo do NOVO ou nos arquivos irmãos. irmaos: {nome: texto}. -> [(0, msg)]"""
    a, b = base.splitlines(), novo.splitlines()
    pares = {}
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != "replace":
            continue
        for old, new in zip(a[i1:i2], b[j1:j2]):
            if HIST.match(old):
                continue
            sai, entra = _tokens(old) - _tokens(new), _tokens(new) - _tokens(old)
            if len(sai) == 1 and len(entra) == 1:
                x, y = next(iter(sai)), next(iter(entra))
                if _forma(x) == _forma(y):
                    pares.setdefault(x, (y, old.strip()[:70]))
    ach = []
    for x, (y, ctx) in sorted(pares.items()):
        pat = r"(?<![\w.])" + re.escape(x) + r"(?![\w])"
        locais = [f"plan.md:{i}" for i, ln in _vivo(novo) if re.search(pat, ln)]
        locais += [f"{n}:{i}" for n, tx in (irmaos or {}).items() for i, ln in enumerate(tx.splitlines(), 1)
                   if not HIST.match(ln) and re.search(pat, ln)]
        if locais:
            ach.append((0, f"'{x}' foi trocado por '{y}' (em «{ctx}») mas ainda ocorre em {len(locais)} local(is): {', '.join(locais[:5])}"))
    return ach


# ---------------------------------------------------------------------------------------------------- C-4
ID_PROPRIO = re.compile(r"\b(?:RULE|BASpec|EC|ADV|INV)-([A-Z]{2,5})-(\d+[A-Za-z]?)\b")
OK_MARCA = re.compile(r"✔|\bPASS\b|✅")


def checks_ancorado(checks_texto, plan_texto):
    """C-4 (versão ESTREITA): linha ✔/PASS do checks.md cita ID da PRÓPRIA família da Spec (a família mais frequente de
    `RULE|BASpec|EC|ADV|INV-<FAM>-nnn` DEFINIDA no Plan) que NÃO existe no Plan. Ignora ENF/CC/STRUCT (método), placeholders
    `0NN` e IDs de outra família (herança). Versão larga ('✔ sem âncora') foi medida e DESCARTADA: 455 alarmes em baselines."""
    fam = {}
    for f, _ in ID_PROPRIO.findall(plan_texto):
        fam[f] = fam.get(f, 0) + 1
    if not fam:
        return []
    propria = max(fam, key=fam.get)
    existentes = set(re.findall(r"\b(?:RULE|BASpec|EC|ADV|INV)-" + propria + r"-\d+[A-Za-z]?\b", plan_texto))
    ach = []
    for i, ln in enumerate(checks_texto.splitlines(), 1):
        if not ln.lstrip().startswith("|") or not OK_MARCA.search(ln):
            continue
        for m in re.finditer(r"\b(?:RULE|BASpec|EC|ADV|INV)-" + propria + r"-\d+[A-Za-z]?\b", ln):
            if m.group(0) not in existentes:
                ach.append((i, f"âncora {m.group(0)} (família {propria}) citada num ✔ do checks.md não existe no Plan"))
    return ach
