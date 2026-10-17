#!/usr/bin/env python3
"""
revisor_detectores.py — detectores D adicionais do gate do Revisor (DHR-AUDITOR-EXTERNO-017).

Cada detector é código puro, somente leitura, sem rede e sem shell, e devolve lista de (linha, mensagem) — ou de strings para
os que comparam duas versões. Nascem da medição do Revisor em Spec real com defeitos plantados (2026-10-17): o gate de código
achou 0 de 14. Detector ≠ Gate (ENF-03): levanta candidatos objetivos; quem julga o sentido é o Revisor.
Calibração: tests/test_revisor_detectores.py roda cada detector nos Plans homologados (falso alarme conhecido = lista fixa)
e nas mutações determinísticas (cada detector tem de achar a sua).
"""
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- 1. mapeamento complexidade→nível/profundidade contraditório ---------------------------------------------------
_MAPA = re.compile(r"\b(LOW|MEDIUM|HIGH|CRITICAL)\b\s*(?:→|->)\s*(L[0-4])\b")
NIVEL_ALVO_CANONICO = {"LOW": "L1", "MEDIUM": "L2", "HIGH": "L3", "CRITICAL": "L3"}   # RULE-MM-04 (RULES.md)


def mapeamento_conflitante(texto):
    """Mesma complexidade mapeada para níveis diferentes no mesmo documento, ou fora do canônico RULE-MM-04."""
    vistos, out = {}, []
    for i, ln in enumerate(texto.splitlines(), 1):
        for k, v in _MAPA.findall(ln):
            vistos.setdefault(k, {}).setdefault(v, []).append(i)
    for k, vs in vistos.items():
        if len(vs) > 1:
            minoria = min(vs.items(), key=lambda kv: len(kv[1]))
            out.append((minoria[1][0], f"{k}→ mapeado para {sorted(vs)} no mesmo documento (minoria: {minoria[0]})"))
        for v, linhas in vs.items():
            if v != NIVEL_ALVO_CANONICO[k] and len(vs) == 1:
                out.append((linhas[0], f"{k}→{v} difere do canônico {k}→{NIVEL_ALVO_CANONICO[k]} (RULE-MM-04)"))
    return out


# --- 2. identificador de norma acima do máximo registrado ----------------------------------------------------------
def _max_registro(arquivo, prefixo, root):
    f = Path(root) / arquivo
    if not f.is_file():
        return None
    nums = [int(m.group(1)) for m in re.finditer(r"^\|\s*" + prefixo + r"-(\d{2})\s*\|", f.read_text(encoding="utf-8", errors="replace"), re.M)]
    return max(nums) if nums else None


def id_norma_inexistente(texto, root=ROOT):
    """ENFnn / INVnn acima do último registrado na tabela do atomic-spec; CC-nn acima de 12. Citação inventada (alucinação documental)."""
    lim = {"ENF": _max_registro("atomic-spec.md", "ENF", root), "INV": _max_registro("atomic-spec.md", "INV", root), "CC": 12}
    out = []
    for i, ln in enumerate(texto.splitlines(), 1):
        for pre, n in re.findall(r"(?<![\w-])(ENF|INV|CC)-(\d{2})\b(?!\s*\.\.|\s*[–-]\s*\d)", ln):
            if lim[pre] is not None and int(n) > lim[pre]:
                out.append((i, f"{pre}-{n} não existe (máximo registrado: {pre}-{lim[pre]:02d})"))
    return out


# --- 3. contagem declarada ≠ itens listados ------------------------------------------------------------------------
def contagem_declarada(texto):
    """'Critérios em EARS (N)' = itens numerados 'Quando…' da seção de critérios; 'N cenários adversariais' = ADV definidos;
    'N BASpecs' acima do total de BASpecs definidos (impossível)."""
    out, linhas = [], texto.splitlines()
    ears = 0
    em = False
    for ln in linhas:
        if re.match(r"^#{1,3}\s*Crit[ée]rios de Aceita", ln):
            em = True
            continue
        if em and re.match(r"^#{1,3}\s", ln):
            break
        if em and re.match(r"^\s*\d+[.)]\s*(?:\*\*)?Quando\b", ln):
            ears += 1
    adv = len({m.group(1) for m in re.finditer(r"^#{2,4}\s*(ADV-[A-Z]+-\d+)\b", texto, re.M)})
    bas = len({m.group(1) for m in re.finditer(r"^#{2,4}\s*(BASpec-[A-Z]+-\d+)\b", texto, re.M)})
    for i, ln in enumerate(linhas, 1):
        for m in re.finditer(r"Crit[ée]rios em EARS\s*\((\d+)\)", ln):
            if ears and int(m.group(1)) != ears:
                out.append((i, f"declara {m.group(1)} critérios EARS; a seção lista {ears}"))
        for m in re.finditer(r"\b(\d+)\s+cen[aá]rios adversariais", ln):
            if adv and int(m.group(1)) != adv:
                out.append((i, f"declara {m.group(1)} cenários adversariais; há {adv} definidos"))
        for m in re.finditer(r"\b(\d+)\s+BASpecs\b", ln):
            if bas and int(m.group(1)) > bas:
                out.append((i, f"declara {m.group(1)} BASpecs; há {bas} definidas"))
    return out


# --- 4. nome de Spec incoerente com o ROADMAP ----------------------------------------------------------------------
_STOP = {"de", "do", "da", "e", "the", "of", "and", "a", "o", "harness", "agent", "para", "com", "em"}


def _nomes_roadmap(root):
    f = Path(root) / "ROADMAP.md"
    if not f.is_file():
        return {}
    return {m.group(1): m.group(2) for m in re.finditer(r"^###\s+SPEC-(\d{3})\s+[—-]\s+(.+)$", f.read_text(encoding="utf-8", errors="replace"), re.M)}


def _tokens(s):
    return {t for t in re.findall(r"[a-zà-ú0-9]{3,}", s.lower()) if t not in _STOP}


def spec_nome_incoerente(texto, root=ROOT):
    """'SPEC-NNN (Nome Próprio)' em que o nome casa melhor com OUTRO slot do ROADMAP do que com o NNN citado."""
    nomes, out = _nomes_roadmap(root), []
    toks = {k: _tokens(v) for k, v in nomes.items()}
    for i, ln in enumerate(texto.splitlines(), 1):
        for m in re.finditer(r"SPEC-(\d{3})\**\s*\(([A-Z][A-Za-z&' ]{5,60})\)", ln):
            n, nome = m.group(1), m.group(2)
            t = _tokens(nome)
            if n not in toks or len(nome.split()) < 2 or not t:
                continue
            pont = {k: len(t & v) / len(t) for k, v in toks.items()}
            melhor = max(pont, key=pont.get)
            if melhor != n and pont[melhor] >= 0.6 and pont[melhor] > pont.get(n, 0):
                out.append((i, f"SPEC-{n} chamada '{nome}'; esse nome é o do SPEC-{melhor} no ROADMAP ('{nomes[melhor][:50]}')"))
    return out


# --- 5. valor que a Spec atribui a uma fonte ≠ valor da fonte ------------------------------------------------------
def valor_fonte(texto, root=ROOT):
    """'≥N cenários D7' atribuído ao atomic-spec §7 deve ser o valor da tabela L3 do próprio atomic-spec."""
    f = Path(root) / "atomic-spec.md"
    m = re.search(r"L3 Testável\s*\|[^|\n]*?≥\s*(\d+)\s+cen[aá]rios D7", f.read_text(encoding="utf-8", errors="replace")) if f.is_file() else None
    if not m:
        return []
    esperado, out = int(m.group(1)), []
    for i, ln in enumerate(texto.splitlines(), 1):
        for g in re.finditer(r"≥\s*(\d+)\s+cen[aá]rios D7", ln):
            if int(g.group(1)) != esperado and "atomic-spec" in ln:
                out.append((i, f"'≥{g.group(1)} cenários D7' atribuído ao atomic-spec; a tabela L3 diz ≥{esperado}"))
    return out


# --- 6. DHR citado junto de item do backlog ≠ DHR do painel --------------------------------------------------------
def dhr_backlog(texto, root=ROOT):
    """'BL-nnn ... (data, DHR-X)' em que DHR-X não consta na linha do painel RMR-001 daquele item."""
    f = Path(root) / "backlog" / "RMR-001_Painel_Backlog.md"
    if not f.is_file():
        return []
    painel = {}
    for ln in f.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"\|\s*\*\*(BL-\d{3})\*\*\s*\|", ln)
        if m:
            painel[m.group(1)] = set(re.findall(r"DHR-[A-Z0-9-]+", ln))
    out = []
    for i, ln in enumerate(texto.splitlines(), 1):
        for m in re.finditer(r"(BL-\d{3})\b[^.\n]{0,90}?\((\d{4}-\d{2}-\d{2}),\s*(DHR-[A-Z0-9-]+)\)", ln):
            dhrs = painel.get(m.group(1))
            if dhrs and m.group(3) not in dhrs:
                out.append((i, f"{m.group(1)} citado com {m.group(3)}; painel RMR-001 cita {sorted(dhrs)}"))
    return out


# --- 7. o que mudou entre duas versões do mesmo Plan -------------------------------------------------------------
_NORMA = re.compile(r"\b(?:RULE-[A-Z]+-\d+|ENF-\d{2}|INV-\d{2}|CC-\d{2}|BL-\d{3}|DHR-[A-Z0-9-]+|WF-[A-Z]?\d+|SPEC-\d{3}|ADR-[A-Z0-9-]+|(?:GPR|SES|PPQ|SAS|CEM|CHM|CCM|CEE|GMC|SDD|CR)-\d{3}|atomic-spec)\b")
_VALOR = re.compile(r"[≥≤<>]\s*\d+(?:[.,]\d+)?%?|\b\d+(?:[.,]\d+)?\s*%|\bE[0-3]\b|\bL[0-4]\b|\bD[0-9]\b")


def comparar_versoes(antigo, novo):
    """Mudanças normativas que o autor precisa justificar: referências removidas/acrescentadas, valores trocados,
    pendência ([ ]) marcada como feita ([x]), referência da linha [FONTE] trocada. Lista de strings (sem linha única)."""
    out = []
    ca, cn = Counter(_NORMA.findall(antigo)), Counter(_NORMA.findall(novo))
    for k in sorted(set(ca) | set(cn)):
        if cn[k] < ca[k]:
            out.append(f"referência reduzida: {k} ({ca[k]}→{cn[k]})")
        elif cn[k] > ca[k]:
            out.append(f"referência acrescentada: {k} ({ca[k]}→{cn[k]})")
    la, ln_ = antigo.splitlines(), novo.splitlines()
    if len(la) == len(ln_):
        for i, (a, b) in enumerate(zip(la, ln_), 1):
            if a == b:
                continue
            if re.match(r"\s*\[ \]", a) and re.match(r"\s*\[[xX]\]", b):
                out.append(f"linha {i}: pendência [ ] marcada como feita [x]")
            va, vb = sorted(_VALOR.findall(a)), sorted(_VALOR.findall(b))
            if va != vb:
                out.append(f"linha {i}: valores {va} → {vb}")
            fa, fb = re.findall(r"\[FONTE[^\]]*\]", a), re.findall(r"\[FONTE[^\]]*\]", b)
            if fa != fb and (fa or fb):
                out.append(f"linha {i}: fonte {fa} → {fb}")
    return out
