#!/usr/bin/env python3
"""
validate_spec_sot.py — Gate Determinístico de Estrutura (SOT)

Implementa ENF-03 (Detector ≠ Gate): este script é o gate determinístico.
O LLM nunca é seu próprio gate. Exit-code decide, não o julgamento do modelo.

Exit 0 → estrutura válida  → Revisor prossegue com protocolo semântico
Exit 1 → estrutura inválida → NÃO CONFORME Crítica imediata (sem análise semântica)

Uso:
    python scripts/validate_spec_sot.py specs/features/SPEC-001/plan.md

Fonte normativa:
    GRE-001 v2.2 · HRE-001 v2.2 · EUA-E02 v1.2 · ENF-01…08
    Decisão de alinhamento: Andraus, 2026-09-14
"""

import sys
import re
import inspect
from pathlib import Path

# Robustez de saída: consoles Windows (cp1252) não codificam os emojis ✅/❌.
# Força UTF-8 no stdout/stderr (sem alterar a lógica dos checks nem o exit-code).
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# ─────────────────────────────────────────────
# CONFIGURAÇÃO DOS CHECKS ESTRUTURAIS
# ─────────────────────────────────────────────

CHECKS = []


def check(name: str, source: str):
    """Decorador para registrar um check estrutural com nome e fonte normativa."""
    def decorator(fn):
        CHECKS.append({"name": name, "source": source, "fn": fn})
        return fn
    return decorator


# ─────────────────────────────────────────────
# CHECKS — cada um retorna (bool, str)
# True = passa | False = falha (com mensagem)
# ─────────────────────────────────────────────

@check(
    name="[STRUCT-01] Cabeçalho obrigatório presente",
    source="PEP-001 §10 / GRE-001 CONST-01"
)
def check_header(content: str):
    """Verifica presença dos campos mínimos do cabeçalho da Spec."""
    # Suporta tanto formato "Campo: Valor" quanto tabela markdown "| Campo | Valor |"
    required = [
        (
            "Complexidade (CRITICAL/HIGH/MEDIUM/LOW)",
            r"complexidade\s*[\|:=]?\s*(CRITICAL|HIGH|MEDIUM|LOW)"
        ),
        (
            "Profundidade-alvo (D<n>)",
            r"profundidade.?alvo\s*[\|:=]?\s*D\d"
        ),
    ]
    missing = []
    for label, pattern in required:
        if not re.search(pattern, content, re.IGNORECASE):
            missing.append(label)
    if missing:
        return False, f"Campos obrigatórios ausentes no cabeçalho: {missing}"
    return True, ""


@check(
    name="[STRUCT-02] Constitution Check presente e preenchido",
    source="SDD-001 §4 / PEP-001 §7 / GRE-001 CONST-01"
)
def check_constitution(content: str):
    """Verifica presença do bloco Constitution Check com pelo menos 4 dos 5 itens."""
    if not re.search(r"constitution\s+check", content, re.IGNORECASE):
        return False, "Bloco 'Constitution Check' não encontrado."
    # Verifica menção à hierarquia Elliott
    if not re.search(r"elliott", content, re.IGNORECASE):
        return False, "Constitution Check não menciona a hierarquia Elliott→...→ICT."
    # Verifica tratamento do Conviction Vector como pendente
    conviction_ok = re.search(r"conviction.{0,60}(pendente|J-001|não.{0,10}fechado|aberto)", content, re.IGNORECASE)
    if not conviction_ok:
        return False, (
            "Constitution Check não declara Conviction Vector como pendente (J-001). "
            "Violação de INV-03: fórmula/pesos/limiares não podem ser fechados."
        )
    return True, ""


@check(
    name="[STRUCT-03] Etiquetagem de fonte presente",
    source="PEP-001 §6 / TRACE-06 / GRE-001 TRACE-01"
)
def check_etiquetagem(content: str):
    """Verifica presença de pelo menos uma etiqueta de fonte."""
    tags = [r"\[FONTE\]", r"\[INFERÊNCIA\]", r"\[PROPOSTA\]",
            r"\[DECISÃO NECESSÁRIA\]", r"\[EXTERNO\]"]
    found = any(re.search(t, content, re.IGNORECASE) for t in tags)
    if not found:
        return False, (
            "Nenhuma etiqueta de fonte encontrada "
            "([FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO]). "
            "Etiquetagem é obrigatória (TRACE-06)."
        )
    return True, ""


@check(
    name="[STRUCT-04] Critérios de Aceitação em EARS",
    source="GRE-001 ECON-01 / PEP-001 §5"
)
def check_ears(content: str):
    """Verifica presença de ao menos um critério em notação EARS."""
    # Padrão: "Quando <condição>, o componente DEVE <resposta>" ou variações
    ears_patterns = [
        r"quando\s+.{5,},\s+.{0,30}(deve|deverá|shall|must)",
        r"while\s+.{5,},\s+.{0,30}(shall|must|deve)",
        r"if\s+.{5,},\s+.{0,30}(shall|must|deve)",
    ]
    found = any(re.search(p, content, re.IGNORECASE) for p in ears_patterns)
    if not found:
        return False, (
            "Nenhum critério de aceitação em notação EARS encontrado. "
            "Use 'Quando <condição>, o componente DEVE <resposta>'."
        )
    return True, ""


@check(
    name="[STRUCT-05] BASpec com campos obrigatórios",
    source="Unidade Atômica v1.2 / GRE-001 BASPEC-01"
)
def check_baspec(content: str):
    """Verifica presença dos campos QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR em ao menos uma BASpec."""
    # Se não há BASpec, verifica se a complexidade é LOW (onde pode ser opcional)
    has_baspec_section = re.search(r"(BASpec|BA\s*Spec|Behavioral\s*Spec)", content, re.IGNORECASE)
    if not has_baspec_section:
        # Verifica se é complexidade LOW (onde BASpec pode ser implícita no EARS)
        is_low = re.search(r"complexidade\s*[:=]?\s*LOW", content, re.IGNORECASE)
        if is_low:
            return True, ""  # LOW pode ter BASpec implícita no EARS
        return False, (
            "Nenhuma BASpec encontrada. Para MEDIUM/HIGH/CRITICAL, "
            "BASpecs com QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR são obrigatórias."
        )
    # Verifica campos obrigatórios
    required_fields = ["QUANDO", "ENTÃO", "PORQUE", "REFERÊNCIA", "VERIFICADO POR"]
    missing = [f for f in required_fields if not re.search(f, content, re.IGNORECASE)]
    if missing:
        return False, f"BASpec incompleta. Campos ausentes: {missing}. (Unidade Atômica v1.2)"
    return True, ""


@check(
    name="[STRUCT-06] Enforcement Contract presente em comportamento com efeito",
    source="ENF-01 / EUA-E02 v1.2 / GRE-001 §3.10"
)
def check_enforcement(content: str):
    """
    Verifica se há Enforcement Contract quando a Spec descreve comportamento com efeito.
    Heurística: se menciona Blackboard, Event Bus, KG, publicação, emissão ou commit,
    deve ter Enforcement Contract com os 8 campos.
    """
    efeito_patterns = [
        r"blackboard", r"event\s*bus", r"knowledge\s*graph",
        r"publica[çc]", r"emite", r"commit", r"persiste", r"grava"
    ]
    tem_efeito = any(re.search(p, content, re.IGNORECASE) for p in efeito_patterns)
    if not tem_efeito:
        return True, ""  # Sem efeito detectado — check não se aplica

    # Verifica campos do Enforcement Contract
    ec_fields = ["CAPABILITY", "EFFECT", "PRECOND", "POSTCOND",
                 "POLICY", "LEVEL", "FAILURE-MODE", "EVIDENCE"]
    missing = [f for f in ec_fields if not re.search(f, content, re.IGNORECASE)]
    if missing:
        return False, (
            f"Comportamento com efeito detectado mas Enforcement Contract incompleto. "
            f"Campos ausentes: {missing}. (ENF-01)"
        )
    return True, ""


@check(
    name="[STRUCT-07] Conviction Vector não fechado (INV-03 / J-001)",
    source="INV-03 / CONS-01 / GRE-001 §3.1"
)
def check_conviction_nao_fechado(content: str):
    """
    Verifica que o Conviction Vector não é usado como invariante fechado.
    Qualquer declaração de limiares numéricos (60%, 75%) sem marcação como
    pendente/decisão aberta é violação de INV-03.
    """
    # Padrão: menção a limiares sem marcação de pendência
    limiar_patterns = [
        r"estrutural\s*[≥>=]\s*60",
        r"total\s*[≥>=]\s*75",
        r"conviction\s*.{0,30}(60|75)\s*%",
    ]
    for pattern in limiar_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            # Verifica se está marcado como pendente/decisão aberta próximo ao match
            start = max(0, match.start() - 200)
            end = min(len(content), match.end() + 200)
            context = content[start:end]
            pendente = re.search(
                r"(pendente|J-001|decisão\s+aberta|não.{0,10}fechado|\[DECISÃO NECESSÁRIA\])",
                context,
                re.IGNORECASE
            )
            if not pendente:
                return False, (
                    f"Limiar do Conviction Vector declarado como fechado (trecho: '{match.group()}'). "
                    f"J-001 está em aberto — fórmula/pesos/limiares NÃO podem ser invariante fechado (INV-03/CONS-01)."
                )
    return True, ""


@check(
    name="[STRUCT-08] Status epistemológico presente (documentado ≠ homologado)",
    source="TRACE-06 / PEP-001 §5"
)
def check_status_epistemologico(content: str):
    """Verifica presença de ao menos um marcador de status epistemológico."""
    status_markers = [
        r"FATO NORMATIVO",
        r"FATO ARQUITETURAL",
        r"documentado\s*[≠!=]\s*homologado",
        r"documentado ≠",
        r"\[DECISÃO NECESSÁRIA\]",
    ]
    found = any(re.search(m, content, re.IGNORECASE) for m in status_markers)
    if not found:
        return False, (
            "Nenhum marcador de status epistemológico encontrado. "
            "Obrigatório distinguir FATO NORMATIVO / FATO ARQUITETURAL / PROPOSTA / INFERÊNCIA / DECISÃO NECESSÁRIA "
            "(TRACE-06: documentado ≠ homologado)."
        )
    return True, ""


@check(
    name="[STRUCT-09] Complexidade compatível com profundidade-alvo",
    source="Unidade Atômica v1.2 §D / AGENTS.md §3"
)
def check_profundidade_compativel(content: str):
    """Verifica que a profundidade declarada é compatível com a complexidade."""
    complexidade = re.search(r"complexidade\s*[:=]?\s*(CRITICAL|HIGH|MEDIUM|LOW)", content, re.IGNORECASE)
    profundidade = re.search(r"profundidade.?alvo\s*[:=]?\s*D(\d+)", content, re.IGNORECASE)
    if not complexidade or not profundidade:
        return True, ""  # STRUCT-01 já cobre ausência — não duplicar

    comp = complexidade.group(1).upper()
    prof = int(profundidade.group(1))

    pisos = {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0}
    tetos = {"LOW": 3, "MEDIUM": 5, "HIGH": 7, "CRITICAL": 8}

    if prof > tetos[comp]:
        return False, (
            f"Profundidade D{prof} excede o teto para {comp} (teto = D{tetos[comp]}). "
            f"Profile deve ser pinado, não elevado em silêncio (AGENTS.md §3)."
        )
    return True, ""


_PENDENCIA = re.compile(
    r"(aberta|pendente|bloqueador|não.{0,10}baselined|\[DECISÃO NECESSÁRIA\]|em.{0,10}aberto)",
    re.IGNORECASE,
)


def _ids_fechados_roadmap(roadmap: Path) -> set:
    """
    IDs de decisão que o ROADMAP declara FECHADAS (linha '| Decisões FECHADAS |').
    Só o 1º ID de cada segmento ' · ' conta — IDs citados como referência no meio do
    texto (ex.: 'runtime → SPEC-018/K-001') NÃO são decisões fechadas.
    """
    try:
        texto = roadmap.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return set()
    for linha in texto.splitlines():
        if re.match(r"\|\s*Decisões FECHADAS\s*\|", linha):
            fechados = set()
            for segmento in linha.split("·"):
                m = re.search(r"\b([A-Z]-\d{3})\b", segmento)
                if m:
                    fechados.add(m.group(1))
            return fechados
    return set()


def _afirma_fechamento(content: str, pos: int, did: str) -> bool:
    """Ocorrência que ATRIBUI fechamento ao ID (janela curta, mesma sentença/célula)."""
    palavra = r"(fechad[oa]s?|resolvid[oa]s?|homologad[oa]s?|closed|resolved)"
    fim = pos + len(did)
    antes = content[max(0, pos - 40):pos]
    depois = content[fim:fim + 40]
    # corta na fronteira de sentença/célula para não atravessar contextos
    antes = re.split(r"[.\n|;]", antes)[-1]
    depois = re.split(r"[.\n|;]", depois)[0]
    return bool(re.search(palavra, antes, re.I) or re.search(palavra, depois, re.I))


@check(
    name="[STRUCT-10] Decisões Abertas não contaminam como invariantes",
    source="CONS-01 / PEP-001 §6"
)
def check_cons01(content: str, roadmap: Path = None):
    """
    Verifica que itens listados como Decisões Abertas (J-001, B-001 etc.)
    não aparecem em outras seções como fatos fechados.

    Regras por ID:
      1. ID que o ROADMAP declara FECHADO (ex.: L-001, B-001) pode ser citado livremente.
      2. Ocorrência com marca de pendência num raio de 200 chars: ok.
      3. Ocorrência SEM marca local é aceita como mera referência SOMENTE se (a) o ID é
         declarado pendente em outro ponto do documento E (b) a ocorrência não atribui
         fechamento ao ID (fechado/resolvido/homologado colado ao ID).
      4. Caso contrário: violação. ID nunca declarado pendente, ou com afirmação
         local de fechamento, continua reprovando (CONS-01 preservado).
    """
    decisoes = re.findall(r"\b([A-Z]-\d{3})\b", content)
    if not decisoes:
        return True, ""

    if roadmap is None:
        roadmap = Path(__file__).resolve().parent.parent / "ROADMAP.md"
    fechados = _ids_fechados_roadmap(roadmap)

    unique = set(decisoes)
    violations = []
    for did in unique:
        if did in fechados:
            continue
        # Localização com fronteira de palavra (sem \b, "M-001" casava dentro de
        # CHM-001/CEM-001/CCM-001/CDM-001/CNM-001 → falsos positivos).
        ocorrencias = [m.start() for m in re.finditer(r"\b" + re.escape(did) + r"\b", content)]
        marcadas = []
        for pos in ocorrencias:
            context = content[max(0, pos - 200):min(len(content), pos + 200)]
            marcadas.append(bool(_PENDENCIA.search(context)))
        declarado_pendente = any(marcadas)
        for pos, marcada in zip(ocorrencias, marcadas):
            if marcada:
                continue
            if declarado_pendente and not _afirma_fechamento(content, pos, did):
                continue  # referência solta a decisão declarada pendente no documento
            violations.append(did)
            break  # Uma violação por ID é suficiente para reportar

    if violations:
        return False, (
            f"IDs de Decisão Aberta {sorted(violations)} encontrados sem marcação de pendência em contexto próximo. "
            f"CONS-01: nenhuma decisão aberta pode aparecer como invariante fechado."
        )
    return True, ""


@check(
    name="[STRUCT-11] Dossiê de Pesquisa presente (RULE-ECC-01/02)",
    source="atomic-spec.md §15 / EUA-E21 / RULE-ECC-02"
)
def check_dossie_pesquisa(content: str, filepath: Path = None):
    """
    Parte determinística da RULE-ECC-02: toda Spec aberta sob o regime de
    Especificação Emergente (EUA-E21 — a Spec cita RULE-ECC-01/02 no próprio texto,
    tipicamente no campo 'Fonte'/'Abertura' do cabeçalho) deve ter um Dossiê de
    Pesquisa companheiro (research.md, mesma pasta) com a seção reconhecível.

    Specs anteriores à EUA-E21 (ex.: SPEC-001, SPEC-019) não citam RULE-ECC-01/02
    e portanto não são alcançadas por este check — não há reescrita retroativa (INV-07).
    """
    if not re.search(r"RULE-ECC-0[12]", content):
        return True, ""  # Spec fora do regime EUA-E21 — check não incide (não retroage)
    if filepath is None:
        return True, ""  # sem caminho de arquivo (ex.: chamada direta em teste) — não aplicável
    research = filepath.parent / "research.md"
    if not research.exists():
        return False, (
            "Spec cita RULE-ECC-01/02 (Especificação Emergente) mas não há research.md "
            "(Dossiê de Pesquisa) na mesma pasta. Fail-closed por RULE-ECC-02 / atomic-spec §15."
        )
    try:
        rtxt = research.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return False, f"research.md presente mas ilegível: {e}"
    if not re.search(r"Doss(iê|ie) de Pesquisa", rtxt, re.IGNORECASE):
        return False, (
            "research.md presente mas não contém seção 'Dossiê de Pesquisa' identificável "
            "(RULE-ECC-02: presença, estrutura, classificação, etiquetagem [EXTERNO])."
        )
    return True, ""


# ─────────────────────────────────────────────
# ENGINE DE EXECUÇÃO
# ─────────────────────────────────────────────

def run_checks(filepath: Path) -> int:
    """Executa todos os checks e retorna exit code (0=pass, 1=fail)."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {filepath}")
        return 1
    except Exception as e:
        print(f"[ERRO] Falha ao ler arquivo: {e}")
        return 1

    print(f"\n{'='*60}")
    print(f"GATE DETERMINÍSTICO — validate_spec_sot.py")
    print(f"Arquivo: {filepath}")
    print(f"Fonte: GRE-001 v2.2 · HRE-001 v2.2 · EUA-E02 v1.2 · ENF-03")
    print(f"{'='*60}\n")

    failures = []

    for chk in CHECKS:
        params = inspect.signature(chk["fn"]).parameters
        ok, msg = chk["fn"](content, filepath=filepath) if "filepath" in params else chk["fn"](content)
        status = "✅ PASS" if ok else "❌ FAIL"
        print(f"{status}  {chk['name']}")
        print(f"       Fonte: {chk['source']}")
        if not ok:
            print(f"       Motivo: {msg}")
            failures.append({"check": chk["name"], "source": chk["source"], "msg": msg})
        print()

    print(f"{'='*60}")
    if failures:
        print(f"RESULTADO: FAIL — {len(failures)} check(s) falharam de {len(CHECKS)}")
        print()
        print("ACHADOS (NÃO CONFORME Crítica — sem análise semântica):")
        for i, f in enumerate(failures, 1):
            print(f"  [{i}] {f['check']}")
            print(f"       Fonte: {f['source']}")
            print(f"       {f['msg']}")
            print()
        print("Ação: devolver ao Especificador. Não prosseguir com revisão semântica.")
        print(f"{'='*60}\n")
        return 1
    else:
        print(f"RESULTADO: PASS — todos os {len(CHECKS)} checks estruturais aprovados")
        print()
        print("Próximo passo: Revisor prossegue com protocolo semântico (GRE-001/HRE-001).")
        print("LEMBRETE: exit 0 ≠ CONFORME ≠ homologação. Gate estrutural apenas (ENF-03).")
        print(f"{'='*60}\n")
        return 0


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/validate_spec_sot.py <caminho/para/plan.md>")
        print("Exemplo: python scripts/validate_spec_sot.py specs/features/SPEC-001/plan.md")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    exit_code = run_checks(filepath)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
