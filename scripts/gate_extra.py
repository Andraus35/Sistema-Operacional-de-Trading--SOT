#!/usr/bin/env python3
"""
gate_extra.py — detectores D adicionais do gate do Revisor (auditoria independente da SPEC-006, 2026-10-13).

Origem: governance/propostas/AUDITORIA-INDEPENDENTE-SPEC006/RELATORIO.md §6/§7 (propostas P0-3, P0-4, P1-6, P1-7, P1-8, P0-2).
11 de 12 mutações que deveriam reprovar passavam como PASSOU_D; cada função abaixo fecha uma classe delas. Somente leitura.
Detector ≠ Gate (ENF-03): o código decide forma/valor/existência; o Revisor decide sentido. Exit 0 ≠ CONFORME ≠ homologação.

Funções (cada uma devolve [(linha, mensagem)]):
  citacoes_arquivo_linha  `CEM-001 l.608-615`, `SPEC-004 RULE-CBP-007 l.264-270`, `RMR-001 l.136 (BL-029)`: arquivo resolve, linha existe
                          e, quando há ID citado junto, o ID é DEFINIDO no intervalo (não apenas mencionado).
  contagens_declaradas    "13 BASpecs", "6 EC", "17 cenários", "22 adversariais" (fora do changelog) × cabeçalhos reais.
  piso_enforcement        Spec do Knowledge Graph: EC de escrita/publicação/commit com LEVEL < E3 (atomic-spec §10.2).
  decisoes_abertas_fechadas  ID de decisão aberta (lido do Status do plan) com palavra de fechamento NA MESMA ORAÇÃO, sem negação/pendência.
  invariantes_estritos    ICT cria hipótese / custo-confiança no Conviction Vector, sem a isenção por `INV-nn` ou `≠`.
  assertivas_checks       `assert-present:"x"` / `assert-absent:"x"` das linhas "Corrigido" do checks.md executadas contra o plan.md.
  teto_de_veredito        teto do veredito do Revisor (revisor.md §3/§8): decisão aberta que bloqueia a Spec ⇒ "CONFORME condicional".
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------------------------------------------- util
_FECHA = re.compile(r"\b(fechad[ao]s?|resolvid[ao]s?|decidid[ao]s?|homologad[ao]s?|encerrad[ao]s?)\b", re.I)
_NEG_LOCAL = re.compile(
    r"\b(n[ãa]o|nunca|jamais|nem|sem|ainda|permanece\w*|segue\w*|continu\w*|aberta|abertas|pendente|pendentes|"
    r"exceto|at[ée] que|quando|rejeit\w*|proíbe|proibid\w*|vedad\w*)\b|"
    r"\[DECIS[ÃA]O NECESS[ÁA]RIA\]|DADO|ADV-|cen[áa]rio|≠",
    re.I)
_ID_DECISAO = re.compile(r"\b(?:[A-Z]{1,6}-\d{2}-\d{3}|[A-Z]{1,6}(?:-[A-Z][A-Z0-9]*)*-(?:D\d{2}|\d{3}))\b")


def _ler(p):
    try:
        return Path(p).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def _norm(s):
    return re.sub(r"\s+", " ", s)


def _eh_candidato(texto):
    """Documento ainda não baseline: Status contém CANDIDATO ou ERRATA ... PROPOSTA. (Bloqueio só incide aí — INV-07.)"""
    m = re.search(r"^\|\s*Status\s*\|([^\n]*)", texto, re.M)
    if not m:
        return False
    s = m.group(1)
    return bool(re.search(r"CANDIDAT", s, re.I) or re.search(r"ERRATA[^|]{0,80}PROPOSTA", s, re.I))


# ----------------------------------------------------------------------------------------------- citações arquivo:linha
_DOC_ARQ = {
    "CEM-001": "canon/CEM-001*.md", "CHM-001": "canon/CHM-001*.md", "CCM-001": "canon/CCM-001*.md",
    "CEE-001": "canon/CEE-001*.md", "SAS-001": "canon/SAS-001*.md",
    "CONSTITUTION": "governance/CONSTITUTION.md", "RULES": "governance/RULES.md",
    "atomic-spec": "atomic-spec.md", "RMR-001": "backlog/RMR-001_Painel_Backlog.md",
}
_PREFIXO_REGRA = {"CBP": "SPEC-004", "CEB": "SPEC-005", "HH": "SPEC-001", "CKG": "SPEC-006",
                  "CAU": "RULES", "ONT": "RULES", "EPI": "RULES", "SEM": "RULES", "BB": "RULES", "MECH": "RULES"}

_RANGES = r"l\.\d+(?:-\d+)?(?:\s*[/,]\s*(?:l\.)?\d+(?:-\d+)?)*"
_CIT_DOC = re.compile(
    r"(?P<doc>CEM-001|CHM-001|CCM-001|CEE-001|SAS-001|CONSTITUTION|RULES(?:\.md)?|atomic-spec(?:\.md)?|RMR-001|SPEC-0\d\d(?:/plan\.md)?)"
    r"(?:\s*§[\d.]+)?\s+(?:\((?:[^)]{0,40})\)\s*)?(?P<rng>" + _RANGES + r")"
    r"(?:\s*\(\s*(?P<par>(?:BL|DHR)-[A-Z0-9-]+)\s*\))?")
_CIT_ID = re.compile(
    r"(?P<id>(?:RULE|INV)-[A-Z]+-\d{2,3})(?P<mais>(?:/[A-Z]{3,4}-\d{3})*)\s+(?P<rng>" + _RANGES + r")")


def _arquivo(doc, root):
    doc = re.sub(r"\.md$", "", doc)
    if doc.startswith("SPEC-"):
        doc = doc.split("/")[0]
        return Path(root) / "specs" / "features" / doc / "plan.md"
    pat = _DOC_ARQ.get(doc)
    if not pat:
        return None
    c = sorted(Path(root).glob(pat))
    return c[0] if c else None


def _intervalos(rng):
    out = []
    for a, b in re.findall(r"(\d+)(?:-(\d+))?", rng.replace("l.", "")):
        a = int(a)
        out.append((a, int(b) if b else a))
    return out


def _define(linha, ident):
    """ident é DEFINIDO na linha (início após marcação markdown) — não apenas mencionado."""
    s = re.sub(r"^[\s#>*|`\-]+", "", linha)
    return s.startswith(ident) and not re.match(re.escape(ident) + r"-?\d", s)


def citacoes_arquivo_linha(texto, root=ROOT):
    achados, cache = [], {}

    def linhas(p):
        if p not in cache:
            t = _ler(p)
            cache[p] = t.splitlines() if t is not None else None
        return cache[p]

    for i, linha in enumerate(texto.splitlines(), 1):
        for m in _CIT_DOC.finditer(linha):
            arq = _arquivo(m.group("doc"), root)
            if not arq or not arq.is_file():
                continue
            L = linhas(arq)
            for a, b in _intervalos(m.group("rng")):
                if a < 1 or b > len(L) or a > b:
                    achados.append((i, f"{m.group('doc')} l.{a}-{b}: fora do arquivo ({len(L)} linhas)"))
                    continue
                par = m.group("par")
                if par and not any(par in L[k] for k in range(max(0, a - 2), min(len(L), b + 1))):
                    achados.append((i, f"{m.group('doc')} l.{a}-{b} ({par}): o ID não está no intervalo citado"))
        for m in _CIT_ID.finditer(linha):
            ident = m.group("id")
            pref = ident.split("-")[1]
            doc = _PREFIXO_REGRA.get(pref)
            ctx = linha[max(0, m.start() - 40):m.start()]
            mm = list(re.finditer(r"SPEC-0\d\d", ctx))
            if mm:
                doc = mm[-1].group(0)
            if not doc:
                continue
            arq = _arquivo(doc, root)
            if not arq or not arq.is_file():
                continue
            L = linhas(arq)
            for a, b in _intervalos(m.group("rng"))[:1]:  # só o 1º intervalo pertence a este ID
                if a < 1 or b > len(L) or a > b:
                    achados.append((i, f"{ident} l.{a}-{b}: fora do arquivo {arq.name} ({len(L)} linhas)"))
                elif not any(_define(L[k], ident) for k in range(max(0, a - 11), b)):  # a regra pode ser citada em qualquer ponto do seu bloco (≤10 linhas após a definição)
                    achados.append((i, f"{ident} l.{a}-{b}: {ident} não é DEFINIDO nesse intervalo de {arq.name}"))
    return achados


# --------------------------------------------------------------------------------------------------------- contagens
_CONTA = [
    ("BASpec", re.compile(r"^#{2,4}\s*BASpec-[A-Z]+-\d+", re.M), re.compile(r"\b(\d+)\s+BASpecs?\b")),
    ("EC", re.compile(r"^#{2,4}\s*EC-[A-Z]+-\d+", re.M), re.compile(r"(?<![\w-])(\d+)\s+(?:EC|Enforcement Contracts?|ECs)(?![\w-])")),
    ("cenário", re.compile(r"^#{2,4}\s*Cen[áa]rio-[A-Z]+-T\d+", re.M), re.compile(r"\b(\d+)\s+cen[áa]rios\s*\(T01", re.I)),  # só a forma "N cenários (T01..Tnn)" (outras Specs numeram diferente)
    ("ADV", re.compile(r"^#{2,4}\s*ADV-[A-Z]+-\d+", re.M), re.compile(r"\b(\d+)\s+(?:adversariais|ADV)\b", re.I)),
]


def contagens_declaradas(texto):
    reais = {nome: len(h.findall(texto)) for nome, h, _d in _CONTA}
    achados = []
    for i, linha in enumerate(texto.splitlines(), 1):
        if re.match(r"^\|\s*\d+\.\d+\s*\|", linha):  # histórico de versões: contagens de versões antigas
            continue
        for nome, _h, dec in _CONTA:
            if reais[nome] == 0:
                continue
            for m in dec.finditer(linha):
                if int(m.group(1)) != reais[nome]:
                    achados.append((i, f"declara {m.group(1)} {nome}, mas há {reais[nome]} cabeçalhos"))
    return achados


# --------------------------------------------------------------------------------------------------------- enforcement
_EC_ESCRITA = re.compile(r"escrita|write|publica|commit|grava|admiss", re.I)
_EC_LEITURA = re.compile(r"consulta|leitura|read-only|somente leitura", re.I)


def piso_enforcement(texto):
    """Spec do Knowledge Graph: EC de escrita/publicação com LEVEL < E3 (atomic-spec §10.2: KG publicado → E3 mínimo)."""
    if not re.search(r"Knowledge Graph", texto[:1500]):
        return []
    achados = []
    blocos = list(re.finditer(r"^###\s*(EC-[A-Z]+-\d+)\b[^\n]*\n(.*?)(?=^###\s|\Z)", texto, re.M | re.S))
    for b in blocos:
        titulo = texto[b.start():texto.index("\n", b.start())]
        lv = re.search(r"^LEVEL\s*:\s*(E\d)", b.group(2), re.M)
        if not lv:
            continue
        if _EC_ESCRITA.search(titulo) and not _EC_LEITURA.search(titulo) and lv.group(1) < "E3":
            ln = texto[:b.start()].count("\n") + 1
            achados.append((ln, f"{b.group(1)} é escrita/publicação no KG com LEVEL {lv.group(1)} (< E3)"))
    return achados


# ------------------------------------------------------------------------------------- campos por BASpec / por EC (P1-6)
_CAMPOS_BASPEC = ["QUANDO", "ENTÃO", "PORQUE", "REFER[ÊE]NCIA", "VERIFICADO POR"]
_CAMPOS_EC = ["CAPABILITY", "EFFECT", "PRECOND", "POSTCOND", "LEVEL"]


def campos_por_bloco(texto):
    """STRUCT-05/06 eram globais (o campo em QUALQUER lugar bastava). Aqui: cada `### BASpec-*` precisa dos 5 campos e cada
    `### EC-*` dos campos de contrato, DENTRO do próprio bloco (até o próximo `### `)."""
    achados = []
    for rx, campos, nome in ((r"^###\s*(BASpec-[A-Z]+-\d+)", _CAMPOS_BASPEC, "BASpec"), (r"^###\s*(EC-[A-Z]+-\d+)", _CAMPOS_EC, "EC")):
        for m in re.finditer(rx + r"[^\n]*\n(.*?)(?=^###\s|^##\s|\Z)", texto, re.M | re.S):
            corpo = m.group(2)
            falta = [c for c in campos if not re.search(r"^[ \t]*" + c + r"\b|\b" + c + r"\s*:", corpo, re.M | re.I)]
            if falta:
                ln = texto[:m.start()].count("\n") + 1
                achados.append((ln, f"{m.group(1)} sem {', '.join(c.replace('[ÊE]', 'Ê') for c in falta)} no próprio bloco"))
    return achados


# ---------------------------------------------------------------------------------------------- decisões abertas fechadas
def ids_abertos_do_status(texto):
    m = re.search(r"^\|\s*Status\s*\|([^\n]*)", texto, re.M)
    if not m:
        return set()
    s = m.group(1)
    return {x for x in _ID_DECISAO.findall(s) if re.search(r"\d", x) and not x.startswith(("DHR-", "SPEC-", "BL-", "RULE-", "INV-", "EUA-"))}


def decisoes_abertas_fechadas(texto, extras=()):
    abertos = ids_abertos_do_status(texto) | set(extras)
    achados = []
    for i, linha in enumerate(texto.splitlines(), 1):
        if re.match(r"^\|\s*(Status|\d+\.\d+)\s*\|", linha):  # cabeçalho/histórico já dizem "permanece/NÃO fecha"
            continue
        for oracao in re.split(r"(?<=[.;!?])\s+|\s[—–]\s", linha):
            for did in abertos:
                if re.search(r"(?<![A-Za-z0-9-])" + re.escape(did) + r"(?![A-Za-z0-9-])", oracao) and _FECHA.search(oracao) and not _NEG_LOCAL.search(oracao):
                    achados.append((i, f"{did} aparece com palavra de fechamento sem negação/pendência na mesma oração"))
    return achados


# ------------------------------------------------------------------------------------------------ invariantes estritos
_ESTRITOS = [
    ("INV-02", re.compile(r"\bICT\b.{0,50}\b(cria|criam|gera|geram|abre)\b.{0,40}(sub-?)?hip[óo]teses?", re.I), "ICT não cria hipótese (AGENTS §6 item 2)"),
    ("INV-04", re.compile(r"\b(custo|confian[çc]a)\b.{0,60}(alimenta\w*|entra\w*|comp[õo]e|integra\w*).{0,40}(Conviction Vector|vetor)", re.I), "custo/confiança não entram no Conviction Vector (AGENTS §6 item 8)"),
    ("INV-04", re.compile(r"CAUSA.{0,40}(conviction|Conviction Vector).{0,20}(PERMITID\w*|permitid\w*)", re.I), "nenhuma aresta para conviction (INV-04)"),
]
_NEGA_ESTRITA = re.compile(r"\b(n[ãa]o|nunca|jamais|nem|sem|proíbe|proibid\w*|vedad\w*|rejeit\w*|viola\w*|ADV-\w+|DADO|cen[áa]rio)\b", re.I)


def invariantes_estritos(texto):
    achados = []
    for i, linha in enumerate(texto.splitlines(), 1):
        for inv, rx, desc in _ESTRITOS:
            if rx.search(linha) and not _NEGA_ESTRITA.search(linha):
                achados.append((i, f"{inv}: {desc}"))
    return achados


# --------------------------------------------------------------------------------------------- assertivas do checks.md
_ASSERT = re.compile(r'assert-(present|absent):"([^"\n]{2,200})"(?:\s+em\s+(plan|checks)\.md)?')


def assertivas_checks(checks_texto, plan_texto):
    """Executa as assertivas do checks.md. Texto normalizado (espaços colapsados) para tolerar quebra de linha."""
    achados = []
    plan_n, checks_n = _norm(plan_texto), _norm(checks_texto)
    for i, linha in enumerate(checks_texto.splitlines(), 1):
        for m in _ASSERT.finditer(linha):
            tipo, alvo, onde = m.group(1), _norm(m.group(2)), m.group(3) or "plan"
            if not re.search(r"\w", alvo):  # `assert-absent:"..."` literal = descrição do formato, não assertiva
                continue
            base = checks_n if onde == "checks" else plan_n
            n = len(re.findall(re.escape(alvo), base))
            if onde == "checks":  # a própria assertiva contém o texto: não conta
                n -= sum(1 for q in _ASSERT.finditer(checks_texto) if _norm(q.group(2)) == alvo)
            if tipo == "present" and n < 1:
                achados.append((i, f'assert-present:"{alvo}" FALHOU: não há ocorrência em {onde}.md'))
            if tipo == "absent" and n > 0:
                achados.append((i, f'assert-absent:"{alvo}" FALHOU: há {n} ocorrência(s) em {onde}.md'))
    return achados


def corrigidos_sem_assertiva(checks_texto):
    """Linhas de tabela marcadas Corrigido/Resolvido sem assertiva executável (informativo)."""
    out = []
    for i, linha in enumerate(checks_texto.splitlines(), 1):
        if linha.startswith("|") and re.search(r"\*\*(Corrigido|Resolvido)", linha) and not _ASSERT.search(linha):
            out.append((i, "marcado Corrigido/Resolvido sem assertiva executável (`assert-present|absent:\"...\"`)"))
    return out


# ---------------------------------------------------------------------------------------------------- teto de veredito
def teto_de_veredito(spec_id, texto_plan, root=ROOT, gate_executado_pelo_revisor=False):
    """
    revisor.md §3: gate ausente na sessão do Revisor ⇒ "no máximo CONFORME condicional".
    revisor.md §8 (tabela de decisões abertas): Spec cuja decisão aberta 'Bloqueia' ela ⇒ "no máximo CONFORME condicional".
    Devolve (teto, [motivos]). teto ∈ {"CONFORME", "CONFORME condicional"}.
    """
    motivos = []
    if not gate_executado_pelo_revisor:
        motivos.append("gate determinístico não executado DENTRO da sessão do Revisor (revisor.md §3: no máximo CONFORME condicional)")
    rv = _ler(Path(root) / ".claude" / "agents" / "revisor.md") or ""
    sec = rv[rv.find("## 8. Decisões abertas"):] if "## 8. Decisões abertas" in rv else ""
    for ln in sec.splitlines():
        m = re.match(r"^\|\s*(?!~~)([A-Z]-\d{3})\s*\|[^|]*\|\s*([^|]*)\|", ln)
        if m and spec_id and spec_id in m.group(2):
            did = m.group(1)
            if re.search(rf"\b{did}\b[^|\n]*\b(ABERTA|aberta)\b", texto_plan) or did in ids_abertos_do_status(texto_plan):
                motivos.append(f"{did} ABERTA e bloqueia {spec_id} (revisor.md §8: no máximo CONFORME condicional)")
    return ("CONFORME condicional" if motivos else "CONFORME"), motivos
