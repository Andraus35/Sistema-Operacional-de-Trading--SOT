# DHR-DOCSYNC-003 — Ata de Decisão — Detector de sincronização casa ID inteiro; AGENTS.md §7 corrige SPEC-020-PRINC-001

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador |
| Ref | Respostas de Andraus (chat, 2026-10-30, AskUserQuestion): "Corrigir o AGENTS.md §7" e "Corrigir o detector" · achado M-1 e observação O-1 do parecer R1 do ERRATUM-SPEC020-002 (`governance/propostas/SPEC-020/PARECER-REVISOR-ERRATUM-SPEC020-002-R1-2026-10-30.md`) · `ROADMAP.md` "Decisões FECHADAS" · `DHR-SPEC020-001` · `AGENTS.md` §7 · `DHR-COESAO-005` |
| Data | 2026-10-30 |
| Status | **DECISÃO REGISTRADA** (decisão direta de Andraus em chat; AGENTS.md §10). Toca `AGENTS.md` e arquivo selado (`scripts/check_doc_sync.py`) **por ordem expressa dele**. |
| Compatibilidade | Patch |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Correção de dado em texto de projeto e de detector: não altera texto de agente de construção nem método. |

## 1. Decisões de Andraus `[FATO]`
| # | Decisão |
|---|---|
| a | `AGENTS.md` §7: SPEC-020-PRINC-001 deixa de aparecer como aberta; entra riscada com **FECHADA** (fonte: `ROADMAP.md` "Decisões FECHADAS" e §12; `DHR-SPEC020-001`), texto anterior preservado (INV-07). **Não fecha decisão alguma**: apenas alinha o AGENTS.md ao ROADMAP, que já a fechou na homologação da SPEC-020 (2026-09-27). |
| b | `scripts/check_doc_sync.py` (D1): o ID de decisão só casa quando é **inteiro** (limite de palavra por `(?<![A-Za-z0-9-])`…`(?![A-Za-z0-9-])`), e examina todas as ocorrências da linha. Corrige o falso positivo "C-001" dentro de "SPEC-020-PRINC-001". Teste novo em `tests/test_check_doc_sync.py`. |

## 2. Selo `[FATO]`
`governance/GATE-MANIFEST.sha256` regravado (`gate_manifest.py --write`) **só** para refletir `scripts/check_doc_sync.py`, por ordem expressa de Andraus (item b). Nenhum outro script do gate foi alterado.

## 3. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001. Nenhuma foi fechada por esta ata (SPEC-020-PRINC-001 já estava fechada no ROADMAP).

## 4. Registro
- [x] Esta ata · [x] AGENTS.md §7 · [x] detector + teste · [x] selo · [ ] merge (assinatura)
