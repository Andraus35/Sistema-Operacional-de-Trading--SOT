# DHR-RPSA-001 — Ata — Automação determinística dos carimbos RPSA e sincronização dos agentes

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-05 |
| Status | **ORDEM DIRETA DE ANDRAUS** (chat, 2026-10-05: "tratar agora e automatizar deterministicamente os carimbos"). Executa o *Agent-Sync* pendente e automatiza a manutenção do carimbo `sincronizado-até` (RPSA, DHR-EUA-E16 §4.3). |
| Compatibilidade | **Patch** (ferramenta de Controlador + sincronização de carimbos; nenhuma BASpec, regra, método ou decisão aberta alterada) |
| Regime | Aditivo (INV-07): livro-razão append-only; nenhuma ata anterior editada. |

## 1. Problema `[FATO]`
O carimbo `sincronizado-até` de `especificador.md` e `revisor.md` estava em `DHR-ERRATA-001`, atrás de três atas posteriores, e `last_sync_catalog_date` estava em 2026-09-26. A comparação "com a última DHR em escopo no CATALOGO" (EUA-E16 §4.3) não era determinística: a ordem textual do CATALOGO não é cronológica e "em escopo" é um julgamento (§4.1) que não ficava registrado.

## 2. Decisões `[FATO: ordem direta de Andraus, 2026-10-05]`
1. **Livro-razão append-only** `governance/rpsa-ledger.json`: toda DHR posterior ao carimbo-base é **classificada** (em escopo? Agent-Sync: `fonte-unica` | `propagado` | `pendente`; motivo). O julgamento de escopo permanece **humano e registrado**; o script não o decide.
2. **`scripts/check_rpsa.py`:** confere (R1–R5), alinha os carimbos de forma idempotente (`--write`) e classifica uma DHR nova lendo a Data da própria ata (`--register`). Testes em `tests/test_rpsa.py`.
3. **CI:** passo **informativo** `check_rpsa.py` (mesma régua de introdução gradual do `check_doc_sync`) e passo **bloqueante** apenas para os **testes** da ferramenta.
4. **Classificação inicial** das DHRs posteriores ao carimbo-base (registrada no livro-razão, **sujeita a reclassificação por Andraus**): ver §3.
5. **Skill:** `.claude/skills/SKILL.md` alinhada à matriz emendada (Knowledge Graph → CRITICAL · D0–D7), conforme o acompanhamento de DHR-SPEC006-PEND-001 §3.
6. **Propagação mínima aos agentes:** o comentário do carimbo, que mandava comparar "com a última DHR em escopo no CATALOGO-OFICIAL", passa a apontar o livro-razão e o script (única mudança embutida; `sync: propagado` nesta ata).

## 3. Classificação inicial `[INFERÊNCIA do orquestrador — a ratificar por Andraus]`
| DHR | Em escopo (§4.1)? | Agent-Sync | Motivo resumido |
|---|---|---|---|
| DHR-AUDIT-SPEC001-001 | sim | fonte-unica | toca fluxo (validador de Specs bloqueante no CI) e declaração global no CATALOGO; agentes referenciam CATALOGO/AGENTS; checklist embutido inalterado |
| DHR-AUDITOR-EXTERNO-001 | sim | fonte-unica | institui piloto de papel externo e composição do consenso; não altera checklist embutido; o Revisor atua sob demanda do Orquestrador; reavaliar na homologação definitiva do papel |
| DHR-SPEC006-PEND-001 | sim | fonte-unica | emenda à matriz do atomic-spec §3 e estado do BL-029; os agentes leem o atomic-spec e o RMR-001 por referência |
| DHR-RPSA-001 | sim | propagado | altera o mecanismo do carimbo; comentário do carimbo atualizado nos dois agentes |

## 4. Como usar daqui em diante (Controlador)
`python scripts/check_rpsa.py --register DHR-… --scope sim|nao --sync fonte-unica|propagado|pendente --motivo "…"` — acrescenta a classificação e alinha os carimbos. `python scripts/check_rpsa.py` confere. Item em escopo com sync `pendente` é achado de gate (EUA-E16 §4.5).

## 5. O que esta ata NÃO faz `[FATO]`
Não homologa Spec nem a abertura da SPEC-006; não fecha decisão aberta (H-001, G-001, M-001, J-001, N-001, K-001, C-001, WF-D03, ECC-03-001, SPEC-038-DATASRC-001, SPEC-045-RUNTIME-001); não altera `canon/*` nem o método. O CI da ferramenta é **informativo** até Andraus decidir promovê-lo.

## 6. Registro
- [x] Esta ata · [x] `governance/rpsa-ledger.json` · [x] `scripts/check_rpsa.py` + `tests/test_rpsa.py` · [x] passo no CI · [x] carimbos de `especificador.md`/`revisor.md` · [x] `.claude/skills/SKILL.md` · [x] `build_map.py` + `--check`.

---

**Andraus** *(ordem direta em chat, 2026-10-05)*
