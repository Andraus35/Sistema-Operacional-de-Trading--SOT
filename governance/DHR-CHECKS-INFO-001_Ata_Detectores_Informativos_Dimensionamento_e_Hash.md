# DHR-CHECKS-INFO-001 — Ata de Decisão — Detectores informativos: dimensionamento de Spec (RULE-ECC-07) e SHA256-ALVO (delta por hash)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Revisor SOT / Controlador |
| Ref | Resposta de Andraus (chat, 2026-10-31, AskUserQuestion): "Checks informativos (Recomendado)" · `DHR-DIMENSIONAMENTO-001` · `DHR-DELTA-HASH-001` |
| Data | 2026-10-31 |
| Status | **DECISÃO REGISTRADA** (decisão direta de Andraus em chat; AGENTS.md §10). Aditiva (INV-07); reversível por `git revert`. |
| Compatibilidade | Patch (novo detector informativo; não altera método, agentes nem arquivo selado). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Novo script detector e passo de CI; não altera texto de agente de construção nem método. |

## 1. Decisão `[FATO]`
`scripts/check_dimensionamento.py` (novo, não selado) passa a existir como **Detector informativo** (exit 0 sempre; passo `continue-on-error` no CI):
1. **RULE-ECC-07:** linhas do corpo do `plan.md` (antes do primeiro `## Anexo`) contra os tetos — confirmação > 1.600, alerta 1.900, teto 2.000. Vale **desde a SPEC-049**; Specs anteriores aparecem só como INFO (histórico).
2. **DHR-DELTA-HASH-001:** parecer do Revisor datado de **2026-11-01 em diante**, rodada ≥ 2 e por delta, sem `SHA256-ALVO:` declarado = WARN. (Pareceres de 2026-10-31 são anteriores à regra.)
Registrado em `MECANISMOS.json` (`det.check-dimensionamento`); teste `tests/test_check_dimensionamento.py` em CI.

## 2. Ressalvas `[FATO]`
- **Não é gate.** Não bloqueia merge nem Spec; promoção a bloqueante só por ordem de Andraus.
- O hook de roteamento e o `validate_spec_sot.py` (selados) **não** foram alterados; o `[STRUCT-xx]` do teto segue **não instituído**.
- Estado atual: 13 Specs em INFO histórico (maior corpo: SPEC-007 com 1.949; SPEC-048 com 1.935); 0 WARN.
- Nenhuma decisão aberta foi fechada (CONS-01); nenhuma leitura do Revisor foi cortada (4Es).

## 3. Registro
- [x] Esta ata · [x] `scripts/check_dimensionamento.py` + teste · [x] `MECANISMOS.json` · [x] CI (informativo) · [ ] merge (assinatura)
