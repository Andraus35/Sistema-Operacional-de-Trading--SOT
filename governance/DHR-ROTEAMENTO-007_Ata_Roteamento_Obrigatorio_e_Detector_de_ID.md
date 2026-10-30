# DHR-ROTEAMENTO-007 — Ata de Decisão — Roteamento de modelo obrigatório por hook, M classificada na 1ª rodada e detector de ID

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-30), após a verificação de conduta em `governance/aprendizado/RETROSPECTIVAS.md` (propostas a/b/c) · `DHR-ROTEAMENTO-003/004/006` · `DHR-COESAO-005` (MECANISMOS.json) |
| Data | 2026-10-30 |
| Status | **REGRA DE PROCESSO ADOTADA** (decisão direta de Andraus em chat: as 3 propostas, na íntegra; AGENTS.md §10). Toca arquivo selado (`scripts/roteador_modelos.py`): selo regravado **por ordem expressa dele** (§3). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Regra operacional do Orquestrador/hook: não altera texto de agente de construção nem método. |

## 1. Decisões de Andraus `[FATO]`
| # | Decisão |
|---|---|
| a | **Detector `_cria_algo`** ignora ID normativo que o arquivo-alvo já contém (ID existente não é "novo"). Corrige os falsos positivos A6b/B3a/N3 da errata SPEC-006. |
| b | **O Orquestrador passa `model` + `CLASSE-TAREFA` em cada chamada** ao Revisor/Especificador e **classifica os achados mecânicos já na 1ª rodada** (rodar `aplicar_ficha_m.py` e depois `roteador_modelos.py esqueleto`, que marca `aplicado_m`). |
| c | **Obrigatório por hook (R-AC7):** invocação de Especificador SOT / Revisor SOT sem `model` + `CLASSE-TAREFA` válidos é NEGADA (antes o frontmatter era o fallback silencioso). |

Tabela vigente: S1/S2 → sonnet · S3 (revisão integral de Spec CRITICAL) → opus · O → opus · M → Orquestrador (sem agente).

## 2. Mecanismo `[FATO]`
`scripts/roteador_modelos.py`: `_cria_algo(a, root)` · natureza `aplicado_m` (= classe M já aplicada; `esqueleto` a detecta pelo texto novo presente e antigo ausente) · R-AC7 em `_decidir_ac`. `scripts/aplicar_ficha_m.py` passa `root` ao detector. `governance/MECANISMOS.json` atualizado no mesmo PR (COE-14). 49 testes do roteador + 10 do aplicador no CI.

## 3. Selo `[FATO]`
`governance/GATE-MANIFEST.sha256` regravado (`gate_manifest.py --write`) **só** para refletir `scripts/roteador_modelos.py`, **por ordem expressa de Andraus (item c)**; nenhum outro script do gate foi alterado. Precedente: `DHR-ROTEAMENTO-004`.

## 4. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001. Nenhuma foi fechada.

## 5. Registro
- [x] Esta ata · [x] código + testes · [x] MECANISMOS.json · [x] selo · [ ] merge (assinatura)
