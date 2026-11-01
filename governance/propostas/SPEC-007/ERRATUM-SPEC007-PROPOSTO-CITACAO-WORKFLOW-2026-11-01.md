# ERRATUM-SPEC007-PROPOSTO — citação de versão antiga do `WORKFLOW.md` (Patch, editorial). PROPOSTA

> **NADA APLICADO.** Preparado a pedido de Andraus (AskUserQuestion, 2026-11-01: "Preparar a proposta"). Baseline só muda por erratum homologado por ele. Número e nome são **propostos**. Não fecha decisão aberta (CONS-01). Não é parecer do Revisor nem homologação.

| Campo | Valor |
|---|---|
| Alvo | `specs/features/SPEC-007/plan.md` (Plan reduzido v2.3, BASELINE, DHR-SPEC007-005) |
| Natureza | **Patch, editorial, LOW.** Troca 1 citação de versão por "versão vigente"; sem comportamento, regra, BASpec, EARS, EC, estado nem schema |
| Origem | `python scripts/check_doc_sync.py` (regra D6d): WARN fixo `plan.md:2650` — cita a versão 1.2 do `WORKFLOW.md`, mas a versão vigente é a do cabeçalho do `WORKFLOW.md`. Aparece em todo SessionStart e no CI |
| Por que só por erratum | O Plan é baseline homologado (HANDOFF §8; AGENTS §10) |

## 1. A mudança (literal)
Âncora por texto exato, linha 2650 (a linha é única no arquivo; conferido em 2026-11-01):

- **Antes:** o título "Conformidade com o `WORKFLOW.md`" seguido de `(v1.2) — última frase`.
- **Depois:** o mesmo título seguido de `(versão vigente) — última frase`.
- **Âncora única:** o trecho literal `(v1.2) — última frase` (aparece uma vez no arquivo).

O texto "(v1.2)" fica preservado **neste erratum** e no git (INV-07). `AGENTS.md` já manda citar `WORKFLOW.md` "só por ID".

## 2. Verificação proposta (antes de homologar)
1. `grep -n "(v1.2) — última frase" specs/features/SPEC-007/plan.md` → só a linha 2650.
2. Depois: `python scripts/check_doc_sync.py` → **0 WARN**; `python scripts/validate_spec_sot.py specs/features/SPEC-007/plan.md` → mesmo resultado de antes (exit 0; STRUCT não depende dessa linha); `check_refs`, mapa.
3. Selo/ata: ata `DHR-SPEC007-…` curta com a ordem de Andraus citada e `RPSA-escopo: nao`; `check_rpsa --register`.

## 3. Pontos para Andraus
- **Rito:** por ser Patch LOW de uma linha, proponho **sem rodada do Revisor** (a verificação da seção 2 é determinística). Se ele preferir o rito completo, o custo medido de um erratum anterior foi alto para um ganho de 1 aviso. Decisão dele.
- **Alternativa sem erratum:** aceitar o WARN como histórico (INFO). Exigiria mudar o detector `check_doc_sync` (arquivo no selo) para tratar Plans baseline como congelados: **mais invasivo que a errata**; não recomendo.
- **Limite:** esta errata não toca nenhuma outra pendência da SPEC-007 (assinatura, DHR-SPEC007-007).
