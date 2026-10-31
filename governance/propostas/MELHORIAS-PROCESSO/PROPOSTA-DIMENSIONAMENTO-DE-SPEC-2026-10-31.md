# Proposta — dimensionamento de Spec: critério medido para "uma Spec ou várias"

> **Não normativo. PROPOSTA** (AGENTS.md §12 passo 5). Nada aqui é regra, mecanismo ou baseline até ordem expressa de Andraus. Não fecha nem abre decisão (CONS-01). Origem: pedido de Andraus no chat, 2026-10-31 ("tivemos problemas para revisar Specs muito grandes; precisamos de um método melhor").

## 1. Achado da auditoria
Hoje **não há critério medido**. O método (`atomic-spec.md` §15, `RULE-ECC-01/02`) fixa *quem* decide (Especificador propõe após Dossiê; Andraus homologa antes do Plan) e *quando* (na abertura), mas não *como*. O Dossiê só exige registrar "escopo/quantidade resultantes". A única regra de tamanho é `.claude/agents/especificador.md:135`: "A Spec deve caber em uma sessão de revisão — se não couber, divida" — sem medida e avaliada pelo próprio autor.

A ABERTURA da SPEC-007 (linha 64) cita "atomic-spec §5" para esse argumento; o §5 trata de taxonomia de harness e a expressão não existe no `atomic-spec.md` (erro de citação, C07).

## 2. Evidência (medida em 2026-10-31, `specs/features/*/plan.md`)
Contagem de BASpecs = cabeçalhos com "BASpec" (aproximação; **corrige** a contagem de 75 dada no chat, que contava todas as linhas com "BASpec-").

| Spec | Linhas do Plan | BASpecs (cabeçalhos) | Rodadas de Plan (retrospectiva) |
|---|---|---|---|
| SPEC-019 | 749 | 9 | — |
| SPEC-020 | 730 | 10 | — |
| SPEC-021 | 806 | 9 | — |
| SPEC-046 | 893 | 11 | — |
| SPEC-002 | 955 | 11 | — |
| SPEC-038 | 947 | 16 | — |
| SPEC-005 | 1.091 | 13 | — |
| SPEC-003 | 1.202 | 14 | — |
| SPEC-004 | 1.325 | 15 | — |
| SPEC-006 | 1.735 | 14 | — |
| SPEC-048 | 1.935 | 13 | 5 |
| SPEC-007 | 3.851 | 16 | 6 (Médias 9→5→5→2→1→0; divisão no meio do Plan) |

Leitura: o número de BASpecs varia pouco (9–16); o que explode é o **volume por BASpec** e os anexos de "texto anterior preservado". Por isso o teto deve medir **linhas efetivas**, não só BASpecs.

## 3. Proposta (cada item é separável)
1. **Estimativa na abertura.** O Dossiê/ABERTURA passa a declarar: nº de BASpecs candidatas (títulos), nº de capacidades do ROADMAP cobertas e linhas previstas do Plan. Sem a estimativa, a proposta de "quantidade = 1" é incompleta.
2. **Teto provisório (a calibrar).** Alerta em 1.000 linhas efetivas de Plan e teto em 1.500, excluindo anexos de texto anterior preservado (INV-07), que passam a arquivo à parte. Acima do teto, divisão obrigatória, proposta a Andraus antes do Plan. Valores **sem calibração**: vêm só da tabela acima.
3. **Regra de corte.** Dividir por **fronteira de contrato** (o que o pedaço consome e produz), nunca por fase nem por tipo de tarefa (GEH-001: handoffs e overhead). Cada pedaço deve ser revisável de forma independente.
4. **Gate determinístico.** Novo check em `validate_spec_sot.py` (ex.: `[STRUCT-xx]`) que reprova Plan acima do teto antes do Revisor. Substitui a cláusula de divisão auto-avaliada. Informativo no início (mesma régua de introdução gradual de `check_refs.py`); bloqueante só por ordem de Andraus.
5. **Decomposição confirmada antes do Plan.** Se a estimativa passar de 80% do teto, o Plan só começa após Andraus confirmar a decomposição (evita refazer escopo no meio, como na SPEC-007).
6. **Fidelidade do texto anterior.** Mover "texto anterior preservado" para arquivo à parte com hash, reduzindo o Plan e o ruído nos detectores (ponto fraco 4 do relatório de 2026-10-24).

## 4. O que é preciso para aplicar (só por Andraus)
- Texto: nova regra (ex.: `RULE-ECC-07`) em `governance/RULES.md`; ajuste em `atomic-spec.md` §15 e em `especificador.md:135`; correção da citação na ABERTURA da SPEC-007 (por erratum).
- Mecanismo: check em `validate_spec_sot.py` + entrada em `governance/MECANISMOS.json` no mesmo PR (COE-14); selo `GATE-MANIFEST.sha256` se o script estiver no manifesto.
- Passo prévio recomendado: **calibrar** os tetos medindo tamanho × rodadas até CONFORME nas Specs já revisadas (o `loop_ledger.py` já tem as rodadas por Spec).

## 5. Riscos
- Teto mal calibrado vira divisão artificial. Mitigação: começar informativo e ajustar com dados.
- Dividir aumenta referências cruzadas e erratas de re-apontamento (custo já visto na SPEC-007/048). Mitigação: item 3 (fronteira de contrato) e item 5.
