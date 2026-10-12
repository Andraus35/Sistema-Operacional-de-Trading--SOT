# DHR-AUDITOR-EXTERNO-013 — Ata — Novas verificações determinísticas (Classe D) no gate do Revisor e correção de negação no STRUCT-10

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-12 |
| Status | **PROPOSTA de código, aprovada em chat por Andraus (2026-10-12: "Propor as verificações")**; a assinatura é o merge do PR. Muda scripts de gate, não texto de agente. Não fecha nem abre decisão. |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert`. Os três detectores novos são **informativos** (não bloqueiam); a única mudança em gate bloqueante é a correção de negação no STRUCT-10 (reduz falso positivo; a afirmação positiva "X fechada" continua reprovando). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Altera scripts de gate (revisor_gate.py, validate_spec_sot.py) e testes; nenhum texto de arquivo de agente e alterado. |

## 1. Origem `[FATO]`
Medição do Revisor SOT na SPEC-006 (Plan v1.0 e v1.1, 2026-10-11/12; relatório do Orquestrador em `scratchpad`, não versionado). O Revisor deu CONFORME condicional nas duas rodadas (4 Menores cada); um revisor de controle independente deu NÃO CONFORME (22 e 27 achados) e o Orquestrador confirmou no repositório 13+ desses achados, sem falso alarme. Vários eram do tipo **detectável por código**.

## 2. O que muda `[FATO]`
1. `scripts/validate_spec_sot.py` — STRUCT-10 (`_afirma_fechamento`): negação/condicional adjacente a "fechada" ("H-001 não fechada", "antes de H-001 fechada", "enquanto H-001 resolvida") **não** conta como afirmação de fechamento. Foi o motivo da reprovação (falso positivo) do Plan v1.0 da SPEC-006. "H-001 fechada", "H-001 está fechada", "H-001 foi resolvida" continuam reprovando. Testes: `tests/test_struct10.py` (+4).
2. `scripts/revisor_gate.py` — três detectores **D informativos** (aparecem no JSON de evidências do Revisor):
   - `campos_atribuidos_baseline`: campo `snake_case` atribuído (mesma linha) a modelo canônico/SPEC cujo arquivo **não o contém** (ex.: `lineage_ref` atribuído ao CEM-001). Linhas [PROPOSTA]/local/novo são isentas.
   - `estado_backlog`: estado de `BL-nnn` citado em documento **CANDIDATO** que difere do painel `backlog/RMR-001` (ex.: BL-029 citado ATIVADO; painel = Em espera). Specs homologadas são excluídas (estado histórico, INV-07).
   - `refs_variantes`: variante com sufixo (`T04-neg`, `ADV-X-06-neg`) nunca definida como item.
   Testes: `tests/test_revisor_gate.py` (+4).

## 3. Evidência `[FATO]`
- Sobre o Plan v1.0 da SPEC-006: STRUCT-10 deixa de reprovar; `estado_backlog` acusa BL-029 (linha 42). Sobre o v1.1: `campos_atribuidos_baseline` acusa `lineage_ref` (linha 78) e `refs_variantes` acusa `T04-neg` (linha 1143). Todos correspondem a defeitos confirmados.
- Falso alarme medido: varredura de todos os `plan.md`/`checks.md` em `specs/features/*` — `campos_atribuidos_baseline` 0, `refs_variantes` 0, `estado_backlog` 0 nos documentos homologados (sem a restrição a CANDIDATO tinha 29 achados históricos, por isso a restrição). `validate_spec_sot.py` continua `exit 0` em todos os plans homologados.
- 54 testes Python do gate/MCP/invariantes/STRUCT-10 passam; `npm test` 11/11; `npm run lint` sem regressão.

## 4. Limites `[FATO]`
Os detectores cobrem forma/existência/consistência verificável; **não substituem o Revisor** (Classe P). `campos_atribuidos_baseline` depende de cue textual ("é do", "atribuído ao"…) e pode ter falso negativo; amostra de uma Spec (indício, não prova). Não foram medidos contra defeitos novos sorteados.

## 5. Reversão `[PROPOSTA]`
`git revert` do commit deste PR. Nenhum carimbo RPSA muda (escopo não).

## 6. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.**

## 7. Registro
- [x] Esta ata · [x] `scripts/revisor_gate.py` · [x] `scripts/validate_spec_sot.py` · [x] testes · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] merge (assinatura) · [ ] `AGENTS.md` §8 (nota dos detectores — exige autorização de Andraus)

---

**Andraus** — *aprovação em chat, 2026-10-12; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
