> **ARQUIVADO (INV-07) — versão 2.0, superseded por `WORKFLOW.md` v2.1. Não normativo.**

# WORKFLOW — Setup Operacional Canônico do SOT

| Campo | Valor |
|---|---|
| **Versão vigente** | **2.0** |
| **Autor / autoridade** | **Andraus** — declaração soberana do setup operacional (decisão de 2026-10-01) |
| **Fonte** | Declaração de Andraus, 2026-09-29 (DHR-ECC05-001, transcrição fiel — RCN-001) + decisões de Andraus de 2026-10-01 sobre o Dossiê `reference/PESQUISA-WORKFLOW-TRADING-2026-10-01.md` (registro fiel em `reference/RESPOSTAS-WORKFLOW-2026-10-01.md`). Nome anterior: RUNTIME-WORKFLOW-SOT (v1.0, em `reference/`). |
| **Posição** | Raiz do repositório. Referenciado por `AGENTS.md`. |

## Regras de uso e de manutenção (leia antes de citar ou editar)

1. **Autoridade.** Fonte primária do *setup operacional* (como o SOT é usado em runtime). Toda Spec que toque o pipeline (agentes Estrutural/Institucional/Operacional, Manager, Risk Agent, Conviction/Fusion) deve **conformar-se** a ele; divergência = achado do Revisor, resolvida por Andraus (nunca pela Spec). **Não** substitui os modelos canônicos (CEM-001/CHM-001/CCM-001…), a hierarquia constitucional (AGENTS.md §6) nem o ADR-MANAGER-001.
2. **Citação estável.** O resto do repositório cita **só por ID** (`WF-xx`, `WF-Dxx`, `WF-Kxx`…) e por "versão vigente" — nunca por linha ou posição. IDs **nunca são reutilizados nem renumerados**; item removido vira `[REVOGADO em vX.Y]`, não some.
3. **Edição.** Só Andraus altera o conteúdo. Cada edição: (a) incrementa a versão (Maior = muda/remove passo; Menor = acrescenta/esclarece), (b) acrescenta linha ao Changelog, (c) arquiva a versão anterior em `docs/_legacy/` (nome `WORKFLOW-v<versão>.md`, INV-07).
4. **Decisões pendentes** ficam em `WF-Dxx`. Nenhuma `WF-Dxx` aberta pode aparecer como fechada em qualquer entrega (CONS-01); ao fechar vira `FECHADA` com data — não é apagada.
5. **Status epistemológico:** declaração de Andraus = [FONTE]. Valores vindos da pesquisa web = [EXTERNO] (dado, nunca baseline). Mapeamentos a termos do repositório = [INFERÊNCIA] até confirmação.
6. **Marcadores de revisão.** Item com `[REVISAR · BL-026]` é **editável por Andraus** e foi deixado com valor-padrão provisório; o backlog BL-026 (RMR-001) o recoloca em pauta quando uma Spec que o consome entrar em redação. Valor `[REVISAR]` **não é baseline** — Specs o tratam como parâmetro configurável, nunca como constante.

## Pipeline declarado

| ID | Passo (declaração de Andraus; ajustes de 2026-10-01 indicados) |
|---|---|
| **WF-01** | **Pré-condição.** Antes da abertura da Killzone: sistema ligado; usuário aponta **Time Frame** e **tipo de Trading** (position / swing / day) — o par de TFs/tripla vem de WF-T01 (editável por missão). A missão pode ser **assistida** ou **pré-programada** (WF-K04). |
| **WF-02** | **Fase 1 — Contexto estrutural.** **Agente Estrutural** (Elliott — mapeia a `Structural Agent` do ADR-MANAGER-001) observa estrutura de ondas → marca → trata Evidência → forma Hipótese → forma Convicção → entrega análise+convicção. |
| **WF-03** | **Fase 1 — Confirmação institucional (condicional).** Se o Agente Estrutural apontar oportunidade: dispara **Agente Institucional** (SMC — mapeia a `Institutional Agent`), que repete o mesmo ciclo e entrega. |
| **WF-04** | **Fase 1 — Síntese de contexto (Manager, Fase 1/Dispatch do ADR-MANAGER-001).** Manager Agent forma a **convicção macro de contexto** (WF-C01). Se conclusiva: registra um **alarme-gatilho de preço** (WF-A01) — nível a ser ativado (ou não) somente após a abertura da Killzone. |
| **WF-05** | **Ativação (Killzone).** Se o alarme-gatilho ativa dentro da Killzone: dispara **Agente Operacional** (= **ICT**, `confluence-ict` → `Operational Agent`, single TF — ex. M5; ADR-CONFLUENCE-001-v3), num **Time Frame de entrada diferente do TF de contexto** e **alinhado** à hipótese de contexto (WF-T02). Produz o **setup operacional** (entrada/stop/alvo/invalidação operacional) atrelado à hipótese de contexto por `parent_id` — **não cria hipótese** (INV-02) — e entrega ao Manager. |
| **WF-06** | **Fase 2 — Síntese global (Manager, Fase 2/Conviction do ADR-MANAGER-001).** Manager forma **convicção global** (WF-C01), decide se envia, e monta o pacote de **risco-retorno**. |
| **WF-07** | **Gate de Risco.** Envia ao **Agente de Risco** (família RISK-SPEC, BL-018), que analisa e decide se envia — ou não — o sinal ao **Bot Trade Finance** externo, com os dados de entrada. |

## Regras operacionais (decisões de Andraus, 2026-10-01)

### Killzone, relógio e missão

| ID | Regra |
|---|---|
| **WF-K01** | **Killzones são as definidas pelo ICT**, expressas no **relógio de Nova York** (`America/New_York`, que já aplica o horário de verão). Tabela padrão em WF-R02 (editável). Valem para os três ativos (BTC inclusive — não há gatilho de volatilidade substituto). |
| **WF-K02** | **Pré-aviso.** Sempre **1h antes da abertura** de cada Killzone, o **Manager** (controle rigoroso de horário, determinístico — ENF-03) aciona o SOT pedindo as orientações da missão (WF-01). Dono do abrir/fechar = Manager/Scheduler (SPEC-008/015), não os agentes analíticos. |
| **WF-K03** | **Fuso.** O SOT **identifica o fuso da máquina** para exibir e agendar; o cálculo das Killzones é feito em `America/New_York` e convertido ao fuso detectado. Janela **fixa** (não adaptativa). |
| **WF-K04** | **Missão pré-programada (madrugada).** Andraus agenda a missão antes (ativo, tipo de trading, TFs, Killzone). O Manager roda o ciclo sozinho até o **Signal Package** e o deixa em **fila para revisão**. O SOT nunca executa (INV-05). Premissa: sem checkpoint humano formal enquanto o journal/HITL estiver adiado (WF-J01). |

### Time frames e alinhamento

| ID | Regra |
|---|---|
| **WF-T01** | **Tabela de TFs por tipo de trading — editável.** Tripla **contexto / confirmação / entrada**, razão ~4:1–6:1 entre TFs; valores padrão em WF-R01; Andraus pode sobrescrever por missão. |
| **WF-T02** | **Alinhamento obrigatório.** O disparo operacional (WF-05) só vale se a direção do setup (TF de entrada) alinhar com a hipótese de contexto (TF alto); desalinhamento = sem entrada (reforça INV-01). |

### Alarme-gatilho (WF-04)

| ID | Regra |
|---|---|
| **WF-A01** | **Objeto do alarme:** nível · direção · condição de disparo · validade/expiração · nível de invalidação · condição de cancelamento · `parent_id` da hipótese-origem. É gatilho de **análise**, nunca ordem (INV-05). |
| **WF-A02** | **Estados (FSM determinística, gate não-LLM — ENF-03):** `IDLE → ARMED → TRIGGERED → {CONSUMED \| EXPIRED \| CANCELLED}`. Disparo só válido dentro da Killzone. |
| **WF-A03** | **Morte do alarme:** expira por **prazo** e é **cancelado automaticamente** se a hipótese-origem passa a `SUPERSEDED`/`REFUTED` (CHM-001). |

### Convicção, confluência e dimensões

| ID | Regra |
|---|---|
| **WF-C01** | **Convicção macro × global = um único Conviction Vector 8D, duas leituras:** macro = subconjunto disponível na Fase 1 (estrutural+institucional); global = vetor com +operacional na Fase 2. **Direção declarada por Andraus; fórmula, pesos, limiares e número de invocações (1x/2x) NÃO são fechados aqui** (J-001, SPEC-003 Q-A5, WF-D03). |
| **WF-C02** | **Confluência vale por independência dos sinais, não por contagem** (anti double-counting). Princípio aqui; mecânica do desconto → SPEC-002/003; calibração = J-001. |
| **WF-C03** | **Order flow (CVD/delta/absorção)** alimenta a **dimensão de volume**; onde o dado falta ou é ruim = **INDETERMINADO** (nunca zero ou fabricado). Disponibilidade por ativo é declarada, não presumida. |
| **WF-C04** | **Regime** (tendência/range/alta volatilidade) é **dimensão de convicção, não gate.** Em qual das 8 dimensões entra: **deixado para a SPEC-003** (dimensionalidade=8 fechada). |

### Falhas e estados do ciclo

| ID | Regra |
|---|---|
| **WF-F01** | **Seis ramos de falha explícitos:** (1) sem oportunidade (WF-02/03) → encerra o ciclo; (2) discordância Estrutural×Institucional → NEUTRO (AGENTS §6.4); (3) sem confirmação operacional (WF-05) → reset do alarme; (4) veto de risco (WF-07) → sem sinal; (5) alarme expirado → reset; (6) reentrada após stop → sinalizada pelo SOT (limite de overtrading é do Bot Trade Finance — WF-X04). |
| **WF-F02** | **FSM do ciclo inteiro (determinística, auditável):** `AGUARDANDO → CONTEXTO_FORMADO → ARMADO → ATIVADO → EM_SÍNTESE → EM_RISCO → {SINAL_ENVIADO \| RECUSADO \| EXPIRADO}`. O gate nunca é LLM (ENF-03). Contrato aqui; implementação no Plan do Manager (SPEC-015). |

### Ativos, calibração e validação

| ID | Regra |
|---|---|
| **WF-P01** | **BTC, XAU e NASDAQ podem operar em paralelo.** O `INV-RISK-HEAT` deve ser medido **com correlação** (BTC×NASDAQ correlacionados), cálculo no Risk Agent (RISK-SPEC). |
| **WF-P02** | **Parâmetros por ativo** (Killzones aplicáveis, TFs, limiares de volume, pesos) são **mecanismo parametrizável**; valores → N-001/backtest (não fechados). |
| **WF-V01** | Ao codificar regras de Elliott/SMC/ICT, exigir **walk-forward + Deflated Sharpe/PBO por regra** (requisito herdado pela implementação). |
| **WF-V02** | **Rótulo de qualidade de evidência por escola** visível no raciocínio (Elliott: regras falseáveis/contagem subjetiva; Fibonacci: só em confluência; SMC/ICT: fraca/anedótica; order flow: dependente de dado). Evidência fraca ≠ inútil. |

### Risco (insumos ao Risk Agent — escopo RISK-SPEC)

| ID | Regra |
|---|---|
| **WF-X01** | **Expectância** (f de win-rate e R:R) é a métrica-raiz de avaliação; **R:R mínimo 1:3 permanece piso soberano** (INV-RISK-RR, AGENTS §6.5). |
| **WF-X02** | **Sizing pela distância do stop** (risco fixo por trade); Kelly adiado. Sizing ≠ convicção (INV-04). |
| **WF-X03** | **Fluxo unidirecional** convicção (WF-06) → risco (WF-07); o risco **nunca** retroalimenta a convicção (INV-04). |
| **WF-X04** | **Prevenção de overtrading é do Bot Trade Finance** (externo); fora do escopo do SOT. |

### Adiado

| ID | Item | Destino |
|---|---|---|
| **WF-J01** | Decision journal imutável (veredito do sistema × decisão humana) e checkpoint humano antes da fronteira | SPEC-018 |

## Valores editáveis marcados para revisão `[REVISAR · BL-026]`

| ID | Tabela (valor-padrão provisório) |
|---|---|
| **WF-R01** | **TFs por tipo** (contexto / confirmação / entrada): position = Semanal-Diário / H4 / — · swing = Diário / H4 / H1 · day = H4 / H1 / M15. Heurística de varejo [EXTERNO]; o Operacional do WF-05 é single-TF (ex. M5) — **reconciliar entrada M5 × tabela** na revisão. |
| **WF-R02** | **Killzones ICT em horário de Nova York** [EXTERNO — fontes divergem; só Londres é consenso]: Asian 20:00–24:00 · London 02:00–05:00 · NY AM 07:00–10:00 · London Close 10:00–12:00 · NY PM 13:30–16:00. Janelas Silver Bullet (1h) variam por fonte e não são adotadas ainda. |
| **WF-R03** | **Quais Killzones valem por ativo** (WF-P02): padrão provisório = todas para os três ativos; refinar (ex.: NASDAQ → NY AM/PM; XAU → London/NY) na revisão. |

## Termos e pontos de decisão (CONS-01 — decisões de Andraus)

| ID | Ponto | Estado |
|---|---|---|
| **WF-D01** | Killzone como mecanismo formal | **FECHADA** (Andraus, 2026-10-01): WF-K01..K04; tabelas em WF-R02/R03 editáveis. |
| **WF-D02** | Alarme-gatilho de preço como mecanismo formal | **FECHADA** (Andraus, 2026-10-01): WF-A01..A03. |
| **WF-D03** | Convicção macro × global × Conviction Vector 8D / J-001 | **ABERTA (residual)** — direção declarada em WF-C01 (um vetor, duas leituras); fórmula/pesos/limiares (J-001), número de invocações 1x/2x (SPEC-003 Q-A5) e dimensão do regime (WF-C04) seguem abertos. |
| **WF-D04** | Papel do ICT no pipeline | **FECHADA** (Andraus, 2026-10-01): ICT = Agente Operacional (WF-05); produz setup operacional, não hipótese (INV-02). |
| **WF-M01** | Agente Estrutural ↔ `Structural Agent` (Elliott) | [INFERÊNCIA] — confirmar SPEC-010 |
| **WF-M02** | Agente Institucional ↔ `Institutional Agent` (SMC) | [INFERÊNCIA] — confirmar SPEC-011/012 |
| **WF-M03** | Agente Operacional ↔ `Operational Agent` (ICT, single TF) | ADR-CONFLUENCE-001-v3 confirma `confluence-ict` → Operacional; detalhe SPEC-013/014 |

## Citado por (manter coerente ao editar)

`AGENTS.md` · `atomic-spec.md` (RULE-ECC-05) · `governance/RULES.md` (RULE-ECC-05) · `ROADMAP.md` (WORKFLOW-SOT-001) · `governance/CATALOGO-OFICIAL.md` · `backlog/RMR-001_Painel_Backlog.md` (BL-026) · `.claude/agents/{especificador,revisor}.md` · `specs/features/SPEC-003/{research,plan,checks}.md`. Atas `DHR-*` são registro histórico imutável e mantêm o nome antigo.

## Changelog

| Versão | Data | Mudança |
|---|---|---|
| 2.0 | 2026-10-01 | **Maior.** Incorpora as decisões de Andraus sobre o Dossiê de pesquisa (24 sugestões): regras operacionais WF-K/T/A/C/F/P/V/X/J; WF-05 passa a nomear o Operacional como ICT e a produzir "setup operacional" (não "hipótese" — INV-02); fecha WF-D01, WF-D02, WF-D04; WF-D03 permanece aberta (residual J-001/SPEC-003); valores editáveis marcados `[REVISAR · BL-026]` (WF-R01..R03). Passos WF-01..07 mantêm IDs; v1.1 arquivada em `docs/_legacy/WORKFLOW-v1.1.md`. |
| 1.1 | 2026-10-01 | Movido para a raiz como `WORKFLOW.md`; IDs estáveis WF-01..07, WF-D01..04, WF-M01..03; regras de manutenção. Conteúdo dos passos inalterado. |
| 1.0 | 2026-09-29 | Captura original (DHR-ECC05-001), RUNTIME-WORKFLOW-SOT (em `reference/`); arquivada em `docs/_legacy/`. |
