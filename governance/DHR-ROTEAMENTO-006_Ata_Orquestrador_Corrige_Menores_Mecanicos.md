# DHR-ROTEAMENTO-006 — Ata de Decisão — O Orquestrador identifica e corrige deterministicamente os Menores mecânicos (supera a DHR-ROTEAMENTO-005)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT / Controlador |
| Ref | Esclarecimento de Andraus (chat, 2026-10-25): "Quis dizer que os achados menores devem ser identificados e corrigidos deterministicamente pelo orquestrador" · `DHR-ROTEAMENTO-003` (classe M) · `DHR-ROTEAMENTO-004` (R-AC5/R-AC6) · `DHR-ROTEAMENTO-005` (SUPERADA) · `DHR-LOOP-001` (passo 0) · `AGENTS.md` §12 |
| Data | 2026-10-25 |
| Status | **REGRA DE PROCESSO ADOTADA** (decisão direta de Andraus em chat; AGENTS.md §10). Não toca arquivo selado. |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Regra operacional do Orquestrador: não altera texto de agente de construção nem método. |

## 1. Decisão de Andraus `[FATO]`
Achados **Menores mecânicos** do Revisor são **identificados e corrigidos de forma determinística pelo Orquestrador**, para evitar rodadas caras de agente. Média/Crítica e qualquer julgamento semântico seguem com o Especificador.

## 2. Erro de interpretação reconhecido `[FATO]`
A `DHR-ROTEAMENTO-005` registrou o contrário ("Orquestrador não corrige Menores") por leitura equivocada de uma frase de Andraus. Fica **SUPERADA** por esta ata (texto preservado, INV-07). A correção das 6 linhas da R3 da SPEC-048 pelo Orquestrador **estava conforme** esta regra; a "Nota de desvio" de `RETROSPECTIVAS.md` é retratada.

## 3. Mecanismo `[FATO]`
- O Revisor entrega os Menores mecânicos no parecer em bloco `<!-- FICHA-M {"achados":[{"id","sev":"MENOR","arquivo","antigo","novo","condicao"}]} -->`.
- `python scripts/aplicar_ficha_m.py <parecer.md|ficha.json> [--dry]`: aplica por substituição exata de texto (âncora = texto, não linha), exige `antigo` único, mesmo número de linhas, condição verificável, nenhum ID/regra/campo novo, árvore limpa no arquivo, teto 10 linhas/2 arquivos; verifica que só as linhas previstas mudaram; atômico. O que não for mecânico sai como ESCALA ao Especificador (exit 1).
- Hook R-AC5/R-AC6 (DHR-ROTEAMENTO-004) permanece: ordem ao Especificador exige `FICHA:` cobrindo todos os achados e M já aplicada. Nenhuma mudança em arquivo selado.

## 4. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção · mecanismo da autenticação (BUILD). Nenhuma foi fechada.

## 5. Registro
- [x] Esta ata · [x] AGENTS.md §12 passo 0 · [x] `scripts/aplicar_ficha_m.py` + `tests/test_aplicar_ficha_m.py` · [x] MECANISMOS/CI · [x] RETROSPECTIVAS (retratação) · [ ] merge (assinatura)

---

**Andraus** — *esclarecimento em chat, 2026-10-25; registro pelo Orquestrador.*
