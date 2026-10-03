# DHR-DEC-004 — Ata de Decisões — BL-017, SPEC-038-DATASRC-001, MASTER Market Data (BL-033), sincronização RPSA

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Respostas diretas de Andraus (chat, 2026-10-03) após a homologação da abertura da SPEC-038 (DHR-SPEC038-001); leitura de `reference/externo/MASTER — MARKET DATA, ORDER FLOW E INTEGRAÇÃO TRADINGVIEW.MD` |
| Data | 2026-10-03 |
| Status | **HOMOLOGADA — vigência imediata** (instrução direta de Andraus em chat) |
| Compatibilidade | Minor. Nenhum modelo canônico baselined tocado (CONST-01); nenhuma Spec baselined reescrita (INV-09). |
| Não fecha | J-001, N-001, M-001, H-001, WF-D03 (residual), ECC-03-001 e as **D-001..D-027** do MASTER (§1.3). |

---

## 1. Decisões de Andraus (2026-10-03)

### 1.1 BL-017 — **PROMOVIDO a ATIVADO**
O gatilho `spec:SPEC-038 em redação` disparou. A emenda pontual à SPEC-020 que fecha a dimensão B **"tool correctness ↔ SPEC-038"** continua **somente na homologação da SPEC-038** (não agora — CONS-01). As demais dimensões B (RAG faithfulness ↔ SPEC-007; decision traceability ↔ SPEC-014) permanecem diferidas.

### 1.2 SPEC-038-DATASRC-001 — **DECIDIDA neste recorte**
Andraus: **TradingView também como fonte de decisão**, lido à luz do MASTER (§6/§19/§56) como **"uma das fontes"**:
- o canal TradingView (CDP, perfil de DHR-DEC-003 §1.1; **risco de Termos de Uso assumido por Andraus**) entra como fonte **via adapter** (`TradingViewAdapter`), **nunca como fonte única da verdade** e nunca substituindo um feed L2/L3;
- o dado de qualquer fonte é **Observação** e só vira Evidência pela governança da SPEC-002 (INV-06; "Provider ≠ Evidence", MASTER §5);
- o **provedor de dados de máquina** (order flow, futuros, BTC multi-exchange) **NÃO é escolhido** aqui: fica para o Discovery/benchmark do MASTER. Databento/Kaiko/CoinDesk/APIs de exchange permanecem **opções**, não decisões (MASTER §56).
Esta ata **não afirma conformidade jurídica** com os Termos de Uso do TradingView, que vedam uso não-display e "algorithmic decision-making" (SRC-TOS-01); o risco é de Andraus.

### 1.3 MASTER — Market Data, Order Flow e Integração TradingView — **NOVO BL-033 (Em espera)**
Registrado como **BL-033** com proposta de **capacidade/slot indicativo** "Market Data & Order Flow" — **sem número de Spec atribuído agora** (RULE-ECC-01/02: número, quantidade e fronteira definidos na abertura, após Dossiê e homologação). A SPEC-038 permanece restrita ao **contrato de ferramenta**, que o MASTER reutiliza. As decisões abertas **D-001..D-027** do MASTER (instrumentos BTC/NQ/XAU, nível L1/L2/L3, footprint, agregação, orçamento, tokens etc.) **permanecem ABERTAS**. O MASTER é **referência externa NÃO-NORMATIVA** (status DISCOVERY / DECISION REQUIRED).

### 1.4 Sincronização RPSA dos agentes — **AUTORIZADA**
Andraus autorizou a sincronização do carimbo `sincronizado-até` e do resumo de DHR em `.claude/agents/especificador.md` e `.claude/agents/revisor.md` até **DHR-DEC-004** (edição aditiva; papel, ferramentas e regras inalterados). Registrado como emenda de Andraus (RPSA/EUA-E16).

---

## 2. Permanecem ABERTAS (CONS-01)
**J-001 · N-001 · M-001 · H-001 · WF-D03 (residual) · ECC-03-001 · D-001..D-027 (MASTER) · escolha do provedor de dados de máquina.** `Em espera`: BL-001, BL-003, BL-010, BL-011, BL-013, BL-015, BL-016, BL-018, BL-026, BL-027..BL-030, BL-032, BL-033. **ATIVADO:** BL-012 (tratamento do delta) e BL-017.

## 3. Registros consequentes
`backlog/RMR-001_Painel_Backlog.md` (BL-017 ATIVADO; BL-033; nota) · `ROADMAP.md` e `governance/CATALOGO-OFICIAL.md` e `AGENTS.md` §7 (DATASRC-001 decidida neste recorte) · `specs/features/SPEC-038/ABERTURA.md` (adendo aditivo — a abertura já homologada não é reescrita) · `.claude/agents/{especificador,revisor}.md` (carimbo).
