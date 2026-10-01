# DHR-WF-002 — Ata de Homologação — WORKFLOW.md v2.0 (decisões sobre o Dossiê de pesquisa de trading)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Respostas de Andraus (chat, 2026-10-01) às sugestões S-01..S-24 — `reference/RESPOSTAS-WORKFLOW-2026-10-01.md`; Dossiê `reference/PESQUISA-WORKFLOW-TRADING-2026-10-01.md` ([EXTERNO], não-normativo) |
| Data | 2026-10-01 |
| Status | **HOMOLOGADA — vigência imediata** (por instrução direta de Andraus em chat) |
| Compatibilidade | Maior no WORKFLOW.md (v1.1 → v2.0); Minor para o restante do repositório (citações por ID) |

---

## 1. Decisão

1. **`WORKFLOW.md` v2.0 vigente** (v1.1 arquivada em `docs/_legacy/WORKFLOW-v1.1.md`). Conteúdo: regras operacionais WF-K (Killzone/relógio/missão), WF-T (TFs/alinhamento), WF-A (alarme), WF-C (convicção/confluência/order flow/regime), WF-F (falhas/FSM), WF-P (ativos/calibração), WF-V (validação), WF-X (risco), WF-J01 (adiado à SPEC-018).
2. **Decisões fechadas por Andraus:** **WF-D01** (Killzone = janelas ICT em `America/New_York`, fixa, pré-aviso do Manager 1h antes, fuso da máquina detectado, missão pré-programada com fila de revisão); **WF-D02** (alarme: objeto de 7 campos, FSM, expiração + cancelamento por refutação); **WF-D04** (ICT = Agente Operacional; setup operacional, não hipótese — INV-02).
3. **WF-D03 permanece ABERTA (residual).** Andraus declarou a direção (um Conviction Vector 8D, duas leituras), mas **não** fechou fórmula/pesos/limiares (J-001), nº de invocações 1x/2x (SPEC-003 Q-A5) nem a dimensão do regime (SPEC-003). `WORKFLOW-SOT-001` (ROADMAP) reduzida a este resíduo.
4. **Valores editáveis `[REVISAR · BL-026]`:** WF-R01 (TFs por tipo), WF-R02 (horários das Killzones — [EXTERNO], fontes divergem), WF-R03 (Killzones por ativo). **BL-026** (RMR-001, `Em espera`; gatilho `spec:SPEC-008 em redação ∨ spec:SPEC-010..015 em redação`) recoloca em pauta quando uma Spec que os consome entrar em redação.
5. **Premissas registradas:** overtrading é do Bot Trade Finance (WF-X04); journal/HITL adiados à SPEC-018 (WF-J01).

## 2. Não decidido (CONS-01)

J-001, N-001, SPEC-003 Q-A5, dimensão do regime, WF-D03. Nenhuma outra decisão aberta foi fechada. **SPEC-003 permanece congelada** (candidata v1.0, sem alteração de mérito); reconciliação por delta (Q-A5/WF-C01, WF-C03, WF-C04) é o próximo passo do Especificador.

## 3. Registro do Controlador (efeitos aplicados — 2026-10-01)

- [x] `WORKFLOW.md` v2.0; `docs/_legacy/WORKFLOW-v1.1.md`.
- [x] `ROADMAP.md` — WORKFLOW-SOT-001 reduzida ao resíduo WF-D03.
- [x] `backlog/RMR-001_Painel_Backlog.md` — BL-026 (`Em espera`).
- [x] `governance/CATALOGO-OFICIAL.md` — linha da ata; `reference/RESPOSTAS-WORKFLOW-2026-10-01.md`.
- [x] Mapa, referências cruzadas, doc-sync revalidados.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
