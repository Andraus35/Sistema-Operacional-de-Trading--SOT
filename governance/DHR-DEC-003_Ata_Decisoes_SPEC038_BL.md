# DHR-DEC-003 — Ata de Decisões — SPEC-038 (TVMCP-001), BL-002/012/027/028/029/030/031/032, ECC-VAL-001, ECC-03-001

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Respostas diretas de Andraus (chat, 2026-10-03) a perguntas sobre decisões abertas e itens do RMR-001 |
| Data | 2026-10-03 |
| Status | **HOMOLOGADA — vigência imediata** (por instrução direta de Andraus em chat) |
| Compatibilidade | Minor no repositório (citações por ID). Nenhuma Spec baselined reescrita (INV-09). |
| Não fecha | J-001, N-001, M-001, H-001, WF-D03 (residual), **SPEC-038-DATASRC-001**, ECC-03-001 — ver §2. |

---

## 1. Decisões de Andraus (2026-10-03)

### 1.1 SPEC-038-TVMCP-001 (BL-031) — veredito sobre canais TradingView — **DECIDIDA**
Andraus escolheu **aceitar o canal CDP (família `tradingview-mcp`) como PERFIL EXPLORATÓRIO**, supervisionado por humano. Condições que acompanham a decisão (do Dossiê e do tutorial `reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md` §1/§9):
- o dado do canal é **Observação**, nunca Evidência nem baseline (INV-06/CEM-001); nunca gera nem envia ordem (INV-05; `replay_trade` proibido);
- operações que alteram gráfico/conta (`draw_*`, `indicator_add`, `alert_create`, `pine_set_source`, encerrar o app) só com confirmação explícita;
- barra em formação = INDETERMINADO; proveniência por leitura; fail-closed; saída de ferramenta = dado não-confiável;
- **o risco de Termos de Uso do TradingView (uso display-only; "algorithmic decision-making" vedado; suspensão de conta sem aviso) permanece e é ASSUMIDO por Andraus.** Esta ata não é parecer jurídico nem torna o canal fonte de decisão do SOT;
- as demais candidatas (6 de terceiros) seguem **não adotadas** na proposta do Dossiê; o **MCP oficial** do TradingView permanece como canal a reavaliar quando houver resposta do TradingView.
O Especificador deve **reescrever o veredito de `ABERTURA.md` §4** conforme esta decisão (a proposta anterior era "rejeitar a família CDP"). **BL-031 → Absorvido** (encaminhado à SPEC-038).

### 1.2 BL-032 — dona do backtest/calibração — **DECIDIDA**
**Ampliar a SPEC-018** (ciclo Extração→Formalização→Validação→Backtest→Stress→Sandbox→Aprovação) com as etapas de backtest/calibração sob WF-V01 e RULE-CTF-01. Gatilho preservado (`spec:SPEC-018 em redação`). Não cria slot novo. J-001/N-001 seguem abertas (valores definitivos pós-backtest).

### 1.3 BL-028 — Salvaguarda de Sinal 1 — **DONA = SPEC-014** (Manager — Convicção & Síntese)
Materialização como precondição verificável. Gatilho existente (`spec:SPEC-014 em redação`).

### 1.4 BL-002 — falso-DENY observável — **ABSORVIDO na SPEC-004**
Requisito de observabilidade do Blackboard/proveniência, tratado na abertura da SPEC-004.

### 1.5 BL-012 — MC-COG-001 — **ENCAMINHAMENTO: reavaliar só o delta**
Mapear o delta útil (schemas §6/§19, integração §18); rejeitar os estados §7 que conflitam com CHM-001 (R-05); não re-especificar o já normativo (~80%). Permanece ATIVADO até o tratamento.

### 1.6 BL-027 — score de setup / Score 0–9 PILOT — **DONA = SPEC-014**, com insumo de calibração do BL-032 (SPEC-018).

### 1.7 BL-029 — "LLM propõe, harness recomputa" — **DONA = SPEC-004** (Blackboard); a SPEC-014 apenas consome.

### 1.8 BL-030 — PEP/PDP e campo ENFORCER — **DIVIDIDO**: **método** (campo ENFORCER no template de Enforcement Contract) por emenda ao `atomic-spec.md` §10; **runtime** (PEP/PDP) → SPEC-018/K-001.

### 1.9 ECC-VAL-001 — validade do Dossiê de Pesquisa — **FECHADA**
Prazo **por complexidade**: LOW 180 dias · MEDIUM 120 dias · HIGH/CRITICAL 90 dias, contados da data de acesso das fontes; **ou antes**, se o contexto mudar materialmente (nova versão de fonte, de Termos de Uso ou de decisão sobre o objeto). Dossiê vencido não dispensa a Spec de reabrir pesquisa (fail-closed, RULE-ECC-02). Os números podem ser ajustados por Andraus (emenda aditiva). Prospectivo: incide sobre Dossiês a partir desta data; não invalida Dossiês de Specs já homologadas.

### 1.10 ECC-03-001 — escopo da RULE-ECC-03 — **MANTIDA RESERVADA**
Sem escopo definido; RULE-ECC-03 continua RESERVADA e não vinculante (RULE-HG-02). **ECC-03-001 permanece aberta.**

---

## 2. Permanecem ABERTAS (CONS-01)

| Decisão | Motivo |
|---|---|
| **SPEC-038-DATASRC-001** | Andraus: "aguardar TradingView" — fonte de dados de decisão (OHLCV/indicadores) depende da resposta do TradingView sobre uso não-display via MCP e da latência. |
| **J-001 / N-001 / M-001 / H-001 / WF-D03 (residual)** | Inalteradas. |
| **ECC-03-001** | Ver §1.10. |
| BL-001, BL-003, BL-010, BL-011, BL-013, BL-015, BL-016, BL-017, BL-018, BL-026 | `Em espera` — gatilhos próprios ainda não disparados; não decididos nesta ata. |

## 3. Registros consequentes
`backlog/RMR-001_Painel_Backlog.md` (estados/donas de BL-002/012/027/028/029/030/031/032) · `ROADMAP.md` (linhas de decisões) · `AGENTS.md` §7 · `atomic-spec.md` §15 e `governance/RULES.md` (ECC-VAL-001). Nenhum modelo canônico baseline tocado (CONST-01).
