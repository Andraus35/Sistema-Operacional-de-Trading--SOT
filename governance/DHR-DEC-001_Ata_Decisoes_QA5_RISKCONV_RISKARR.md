# DHR-DEC-001 — Ata de Decisões — Q-A5, RISK-CONV-001, RISK-ARR-LOC-001, DIV code-block

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Respostas diretas de Andraus (chat, 2026-10-01) a perguntas do Especificador sobre decisões abertas de convicção/risco e higiene de anotações DIV |
| Data | 2026-10-01 |
| Status | **HOMOLOGADA — vigência imediata** (por instrução direta de Andraus em chat) |
| Compatibilidade | Minor no repositório (citações por ID). `WORKFLOW.md` v2.0 → v2.1 (Menor — acréscimo WF-X05 + esclarecimento WF-C01); SPEC-003 v1.2 → v1.3 (delta de propagação, sem renumerar BASpecs). |
| Não fecha | Nenhuma decisão aberta além das listadas em §1. J-001, N-001, M-001, SPEC-015-SCOPE, WF-D03 (residual), Q-A9, D-RISK-SP-001 e CDM-001 permanecem **ABERTAS** (§2). |

---

## 1. Decisões fechadas por Andraus (2026-10-01)

### 1.1 Q-A5 — número de invocações do mecanismo de Conviction Vector — **FECHADA**
O Manager invoca o **mecanismo de cálculo do Conviction Vector 2x por ciclo**:
- **Macro** (Fase 1, Dispatch): dimensões disponíveis **estrutural + institucional** → forma a convicção macro de contexto e **registra o alarme-gatilho de preço** (WF-04/WF-A01).
- **Global** (Fase 2, Conviction): **+ operacional** → decide o envio (WF-06).

É **um único Conviction Vector 8D, duas leituras** (WF-C01). A **invocação** pertence ao **Manager** (SPEC-008 Fase 1 / SPEC-014 Fase 2); a **SPEC-003** fornece o **mecanismo**, não a invocação. Registrado em `WORKFLOW.md` v2.1 (WF-C01). **J-001** (fórmula/pesos/limiares definitivos) permanece aberta — Q-A5 fecha apenas o **número de invocações**, não a calibração.

### 1.2 RISK-CONV-001 — "convicção de risco" vs Conviction Vector — **FECHADA**
A antiga "convicção de risco" é **renomeada para "avaliação de risco"** — **escala própria do Risk Agent** (família RISK-SPEC). A avaliação de risco **NUNCA soma, pondera nem retroalimenta o Conviction Vector 8D** (INV-04; fluxo unidirecional convicção → risco, WF-X03). Registrada em `WORKFLOW.md` v2.1 (novo **WF-X05**). O detalhamento operacional continua pertencendo a **RISK-SPEC-010** (FASE RISK), que agora apenas **implementa** a decisão já tomada aqui — não a reabre.

### 1.3 RISK-ARR-LOC-001 — localização do D-ARR-001 — **FECHADA**
O **D-ARR-001** é declarado **AUSENTE do repositório**. A verdade vigente do Risk Agent é a composição: **EUA-E19a** (Signal Package / fronteira / TMP interno) + **INV-RISK-*** + **BL-018** + **FASE RISK (EUA-E20)**. Se o arquivo `D-ARR-001` vier a aparecer, entra por **RPIR/HOD-001** (triagem de intake) — **não** é fonte normativa hoje e não reabre esta decisão por si só.

### 1.4 Higiene DIV — comentários em bloco de código — **aplicada**
Os comentários **DIV-CEE-04** (`canon/CEE-001`, diagrama `InferenceContextEnvelope` §6.1) e **DIV-PPQ-05** (`canon/PPQ-001`, exemplo de prompt §8.4) foram **movidos para FORA do respectivo bloco de código** (imediatamente acima da cerca), porque comentário HTML dentro de bloco de código renderiza como texto literal. **Texto normativo/histórico intacto** (CONST-01/INV-07). `DHR-DIV-001` recebeu nota de ajuste.

---

## 2. Permanecem ABERTAS (CONS-01 — não fechadas por este ato)

| Decisão | Motivo de permanecer aberta |
|---|---|
| **J-001** | Fórmula/pesos/limiares **definitivos** do Conviction Vector — só após backtest; Q-A5 fecha apenas o nº de invocações, não a calibração. |
| **N-001** | Pesos por ativo — Andraus: **manter até o backtest**. |
| **M-001** | Estados do Blackboard para objetos não-hipótese — resolve na **abertura da SPEC-004**. |
| **SPEC-015-SCOPE** | Fronteira/decomposição do Manager (ADR-MANAGER-001 §7) — **manter aberta**. |
| **WF-D03** (residual) | Direção macro×global declarada (WF-C01) e nº de invocações já fixado (2x, Q-A5); resíduo = fórmula/pesos/limiares (J-001) + dimensão do regime (WF-C04/Q-A9). Permanece **ABERTA**. |
| **Q-A9** | Em qual das 8 dimensões entra o regime (WF-C04) — **a cargo da SPEC-003** (fonte de dados: `research-Q-A9-regime.md`, não-normativo). |
| **D-RISK-SP-001** | Signal Package / FASE RISK — abre com RISK-SPEC-022. |
| **CDM-001** | Canonical Decision Model — pendente de redação (FASE 6/RDR). |

**RISK-CONV-001** aparece como "permanece aberta" na instrução original apenas para contraste — está **FECHADA** por §1.2 acima.

---

## 3. Efeitos de propagação (aplicados pelo Especificador, 2026-10-01)

- [x] `WORKFLOW.md` → **v2.1**; `docs/_legacy/WORKFLOW-v2.0.md` (ARQUIVADO). WF-C01 esclarecido (2x), **WF-X05** novo, WF-D03 ABERTA (residual atualizado), changelog.
- [x] `ROADMAP.md` — RISK-CONV-001 e RISK-ARR-LOC-001 movidas de "Decisões abertas ativas" para "Decisões FECHADAS"; Q-A5 registrada como fechada; §10-bis (FASE RISK) e WORKFLOW-SOT-001/WF-D03 atualizados.
- [x] `AGENTS.md` §7 — RISK-CONV-001/RISK-ARR-LOC-001 removidas das ativas e registradas como fechadas.
- [x] `governance/CATALOGO-OFICIAL.md` — linha da ata DHR-DEC-001 + listas de decisões.
- [x] `backlog/BL-018-RISK-AGENT-backlog.md` e `backlog/RMR-001_Painel_Backlog.md` — RISK-CONV-001 fecha em RISK-SPEC-010 → agora decidida (sem promover estado indevidamente; gate 11-bis).
- [x] `docs/MATRIZ-WORKFLOW-SPEC.md` — WF-C01 / WF-X05 / WF-D03.
- [x] `specs/features/SPEC-003/{plan,checks,research}.md` — **v1.3 candidata**: Q-A5 passa a dado de entrada herdado de WF-C01 (invocação 2x decidida; a Spec NÃO a implementa).
- [x] `canon/CEE-001` / `canon/PPQ-001` — DIV-CEE-04 / DIV-PPQ-05 movidos para fora do code-block; `DHR-DIV-001` com nota de ajuste.
- [x] `.claude/agents/{especificador,revisor}.md` — `sincronizado-até: DHR-DEC-001` + SYNC-DATE 2026-10-01.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
