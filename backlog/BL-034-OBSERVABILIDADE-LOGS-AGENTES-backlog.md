# BL-034 — Observabilidade e logs de agentes (master externo) — intake de backlog

> **NATUREZA DESTE DOCUMENTO.** Intake de backlog (RMR-001): **NÃO** é Dossiê de Pesquisa (RULE-ECC-02), **NÃO** abre Spec, **NÃO** é baseline e **NÃO** fecha decisão aberta. O painel vivo é `backlog/RMR-001_Painel_Backlog.md` (em divergência, o painel prevalece).

| Campo | Valor |
|---|---|
| ID | BL-034 |
| Título | Observabilidade e logs de agentes (master externo) — logs estruturados, traces, eventos de invariante/política, estados de resultado, regressão a partir de falhas |
| Tipo | Módulo diferido |
| Estado | **Em espera** |
| Gatilho de Ativação | `spec:SPEC-040 em redação` ∨ `spec:SPEC-041 em redação` |
| Origem | `reference/externo/Uso de Logs por Agentes de IA.MD` (Master Document externo, NÃO-normativo); registro direto de Andraus, 2026-10-03 |
| Afeta | SPEC-040 (Cognitive Observability) · SPEC-041 (Audit & Decision Reconstruction, D9) · SPEC-042 (Runtime Guardrails) · SPEC-038/039 (contrato de ferramenta, Provenance) · SPEC-018 (aprendizado) · SPEC-022 (teste adversarial) · SPEC-020 (avaliação, baselined — não reescrita) · BL-015 · BL-017 |
| Decisor | **Andraus** |

## 1. O que o master oferece (insumo, não decisão)
Run/trace/span com correlação; contrato de logging MUST/SHOULD/MAY; estados de resultado `REQUESTED → AUTHORIZED → STARTED → SUCCEEDED/FAILED/REJECTED/TIMEOUT/UNKNOWN` (intenção ≠ ação, INV-05); eventos de violação de invariante e de política; Detector ≠ Gate (ENF-03); versões de harness/prompt/skill/política/ferramenta; falha → taxonomia → caso de regressão; avaliação determinística antes de LLM-as-judge; "Log ≠ Memória".

## 2. Onde cai no ROADMAP (referência não-normativa já anotada)
SPEC-018 · SPEC-022 · SPEC-038 · SPEC-039 · **SPEC-040 (fonte primária)** · SPEC-041 · SPEC-042.

## 3. Tensões a resolver no Dossiê de abertura (não assumir)
1. **§49 do master × SPEC-041:** "não registrar cadeia de pensamento" × "reconstruir exatamente por que o SOT decidiu" (D9). Decidir se decisão operacional + evidências + política basta.
2. **Conteúdo opt-in / referência+hash (§10/§11) × auditoria** das Observações que sustentaram um sinal (liga a BL-033).
3. **Campo `confidence` do evento de decisão ≠ Conviction Vector** (INV-04; J-001 aberta).
4. **Referências a "AXL / Estrategista → Analista → Controlador"** são o pipeline AXL, não o Especificador/Revisor do SOT.
5. **Escada de maturidade do master (5 níveis) ≠ escada L0–L4 da SPEC-021** — não misturar.
6. "DO NOT LOG" (§72) trata do que gerar, não de apagar o que existe — não conflita com INV-07.

## 4. Ação ao ativar
No Dossiê de abertura da SPEC-040/041: usar o master como fonte de requisitos; propor número, fronteira e decomposição (RULE-ECC-01/02); resolver as tensões do §3; reconciliar com `ROADMAP.md` §18 (`Evento → Evidência → Hipótese → Conviction → Decisão → Missão → Resultado → Aprendizado`).

**Não fechado:** J-001, N-001, M-001, H-001, ECC-03-001, D-001..D-027 (MASTER Market Data).
