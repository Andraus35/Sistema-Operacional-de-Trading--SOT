# ERRATUM-SPEC005-001 — Estado do BL-008: `Absorvido`, não `ATIVADO` — erratum ADITIVO

| Campo | Valor |
|---|---|
| Spec/documentos afetados | SPEC-005 v1.0 (HOMOLOGADA — BASELINE, DHR-SPEC005-002) — `plan.md` l.39, `checks.md` (§ itens de backlog), `ABERTURA.md` §9, `research.md` §6.3; ata DHR-SPEC005-001/002 — **não reescritos** (INV-09); erratum aditivo. |
| Fundamento | Conferência no painel `backlog/RMR-001_Painel_Backlog.md` (l.107): **BL-008 = `Absorvido`** (Mapa de Auditoria da SPEC-001 HOMOLOGADO em 2026-09-28, DHR-BL008-001; SPEC-001 v1.1 não reescrita). A menção "BL-008 segue ATIVADO" vinha de uma nota histórica anterior à absorção (passo 11-bis da EUA-E22, 2026-09-26) e foi repetida, sem conferir o estado vigente, nos documentos da SPEC-005 e em notas do orquestrador. |
| Ordem | Andraus (chat, 2026-10-05, "resolver"). |
| Data | 2026-10-05 |
| Compatibilidade | **Patch** (correção de fato de estado; nenhum comportamento ou regra alterado). |

## Texto do erratum
Onde os documentos da SPEC-005 listam **BL-008 como `ATIVADO`** ("auditoria retroativa da SPEC-001" pendente), ler: **BL-008 = `Absorvido`** (DHR-BL008-001, 2026-09-28). **Itens `ATIVADO` reais após a homologação da SPEC-005:** apenas **BL-003** (persistência física) e **BL-029** (proveniência — camada Blackboard materializada na SPEC-004; consumidor→SPEC-014, boundary→SPEC-018/045 pendentes). O restante da conclusão da SPEC-005 (nenhum item com gatilho `spec:SPEC-005`) permanece correto.

## O que NÃO muda (CONS-01)
Nenhuma BASpec, regra ou decisão aberta alterada; EVENT-BUS-001 segue **FECHADA** (DHR-SPEC005-002); J-001, N-001, M-001, H-001, G-001, WF-D03, ECC-03-001 abertas.
