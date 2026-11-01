# DHR-SPEC007-008 — Ata — Erratum editorial da SPEC-007 (citação de versão do `WORKFLOW.md`)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT |
| Ref | `governance/propostas/SPEC-007/ERRATUM-SPEC007-PROPOSTO-CITACAO-WORKFLOW-2026-11-01.md` · alvo `specs/features/SPEC-007/plan.md` (BASELINE v2.3, DHR-SPEC007-005) |
| Data | 2026-11-01 |
| Status | **ERRATUM HOMOLOGADO (Patch, editorial, LOW) e APLICADO no ramo; mescla do PR só por ordem de Andraus.** Decisão de Andraus no chat, 2026-11-01, por AskUserQuestion: "Preparar a proposta"; rito "Sem Revisor, verificação determinística"; "Homologar e aplicar". |
| Compatibilidade | Patch editorial; não toca comportamento, regra, BASpec, EARS, EC, estado nem schema. Não fecha decisão aberta (CONS-01). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Troca editorial de uma citação de versao no Plan da SPEC-007; nao altera texto de agente nem metodo. |

## 1. O que mudou (literal)
Em `plan.md` (título "Conformidade com o `WORKFLOW.md`", linha 2650): `(v1.2) — última frase` passou a `(versão vigente) — última frase`. O texto antigo fica preservado nesta ata e no git (INV-07).

## 2. Verificação (determinística, sem rodada do Revisor, por escolha de Andraus)
`check_doc_sync`: o aviso de `plan.md:2650` desapareceu (0 WARN). `validate_spec_sot.py specs/features/SPEC-007/plan.md`: mesmo resultado de antes (exit 0). Os demais gates constam do PR.

## 3. Limite
Não substitui parecer do Revisor nem homologa mais nada da SPEC-007. A pendência de assinatura criptográfica (DHR-SPEC007-007) continua aberta.
