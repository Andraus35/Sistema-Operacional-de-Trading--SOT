# PESQUISA — Estado da Arte para Evolução do WORKFLOW Operacional do SOT

| Campo | Valor |
|---|---|
| **Identificador** | PESQUISA-WORKFLOW-TRADING-2026-10-01 |
| **Versão** | 1.0 |
| **Data de acesso web** | 2026-10-01 (todas as fontes `[EXTERNO]`) |
| **Autor** | Especificador Principal (Claude Code, Opus 4.8) |
| **Natureza** | **Dossiê de Pesquisa `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão. |
| **Status epistemológico** | Conteúdo web = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02). Toda fonte etiquetada `[EXTERNO]` e classificada. A veracidade das páginas **não** é atestada. |
| **Destino** | `reference/` (padrão não-normativo). Insumo para Andraus evoluir o `WORKFLOW.md` (v1.1) e suas decisões abertas. |
| **Decisões que permanecem ABERTAS** | `WORKFLOW-SOT-001` e `WF-D01..WF-D04` **seguem abertas** — este documento **sugere**, Andraus **decide** (CONS-01). |
| **Fronteiras respeitadas** | AGENTS.md §6 (não-negociáveis); INV-01 (hierarquia), INV-02 (ICT não cria hipótese), INV-04 (custo fora da convicção), INV-05 (SOT não executa). Risco/sizing/Kelly = escopo RISK-SPEC (adiado). |

> **Aviso de método (RULE-MET-01 — sem bajulação).** Grande parte do material de varejo sobre ICT/SMC/Elliott é **prática ou folclore**, não evidência. Onde a base empírica é fraca ou a escola é **não-falseável**, isto está declarado explicitamente na Seção B e nas sugestões. A qualidade da evidência foi separada de sua popularidade.

---

## A. Sumário executivo

O `WORKFLOW.md` (versão vigente à época da pesquisa: 1.1) declara fielmente o pipeline de 7 passos de Andraus (WF-01..07) e mantém honestamente 4 pontos sem mecanismo formal (WF-D01 Killzone, WF-D02 alarme-gatilho, WF-D03 convicção macro × global, WF-D04 papel do ICT). A pesquisa de estado da arte mostra que **os quatro pontos têm literatura e padrões maduros o suficiente para serem parametrizados** — a maior parte do que falta é **decisão de parametrização de Andraus**, não invenção de mecanismo.

Cinco achados estruturais dominam o dossiê:

1. **Killzone é um conceito de janela temporal que precisa ser parametrizado por ativo** — BTC é 24/7 (killzone de sessão é mais fraca), XAU e NASDAQ têm sessões/abertura cash claras. O erro de implementação mais comum e barato de evitar é o **drift de horário por horário de verão (DST)** — a janela em UTC se move 1h nas viradas. [EXTERNO]
2. **O "alarme-gatilho de preço" é um padrão clássico de ordem condicional / máquina de estados "armed"** (alert → armed → triggered → expired/cancelled), com análogos diretos em corretoras (conditional orders, OCO/OTOCO, GTC com expiração). O ponto crítico para o SOT é **amarrar o cancelamento do alarme à refutação da hipótese** (CHM-001 SUPERSEDED/REFUTED), não só a preço/tempo. [EXTERNO + FONTE]
3. **A análise top-down multi-timeframe é padrão consolidado**, com razões típicas de 4:1–6:1 entre TFs e um mapeamento limpo contexto/confirmação/entrada por tipo de trading (position/swing/day). Isso dá base concreta para WF-01 (apontar TF e tipo) e para a regra WF-05 ("TF de entrada diferente do TF de contexto"). [EXTERNO]
4. **Confluência não vale por quantidade e sim por independência dos sinais** — contar Elliott+Fibonacci+SMC+ICT como 4 confirmações quando medem a mesma coisa é **double-counting**, um viés que infla convicção falsamente. Isto reforça princípios SOT já existentes (PE-08 independência, AP-02 confluência falsa, PCO-06 não-redução) e tem implicação direta na convicção das Fases 1 e 2. [EXTERNO + FONTE]
5. **ICT encaixa-se naturalmente como camada de timing/refinamento de entrada** (OTE 62–79%, killzone, varredura de liquidez do Power-of-3), exatamente no WF-05 (Agente Operacional), **sem violar INV-02** (ICT não cria hipótese). A evidência empírica mecânica do ICT é fraca; a discricionária é melhor — o que recomenda usá-lo como refinamento condicionado, não como gerador de sinal autônomo. [EXTERNO + FONTE]

Hierarquia de evidência resumida: **Elliott** (regras duras falseáveis, mas rotulagem subjetiva); **Fibonacci** (fraco isolado, útil só em confluência); **SMC/ICT** (majoritariamente prática/anedótica, evidência mecânica fraca, melhora com discricionariedade); **Order Flow** (mecanismo plausível, mas dependente de qualidade de dados por ativo); **MTF / pipeline / walk-forward / expectância** (base metodológica forte).

---

## B. Achados por escola e tema, com qualidade de evidência

> Escala: **Forte** (estudo acadêmico/replicável) · **Moderada** (consenso metodológico amplo, pouca refutação) · **Fraca** (backtests mistos, sem verificação independente) · **Anedótica** (folclore de varejo / proprietário / não-falseável).

### B.1 Elliott Wave — evidência **Fraca a Moderada** (regras duras falseáveis; rotulagem subjetiva)
- Três regras invioláveis e **falseáveis em tempo real**: onda 2 não retrai >100% da onda 1; onda 3 nunca é a mais curta; onda 4 não entra no território da onda 1. Elas dão **níveis de invalidação objetivos** — raros em análise discricionária. [EXTERNO]
- Diretrizes (não leis): alternância, igualdade — ajudam a escolher entre contagens válidas, nunca sobrepõem as regras. [EXTERNO]
- Crítica central: **sem taxa de acerto publicada e verificada independentemente**; rotulagem é subjetiva — dois analistas competentes produzem contagens válidas diferentes do mesmo gráfico e ambos "acertam" relabelando a posteriori. [EXTERNO]
- *Implicação SOT:* coerente com Elliott como criador de hipótese primária (INV-01/Q-005), **desde que** a contagem alternativa e o nível de invalidação sejam registrados explicitamente (favorece versionamento monotônico CHM-001).
- Fontes: [cwcount — Elliott rules](https://cwcount.com/education/elliott-wave-principle-rules/), [LuxAlgo — Elliott pattern rules](https://www.luxalgo.com/blog/elliott-wave-theory-pattern-rules-simplified/), [Ironclad Research](https://www.ironcladresearch.com/learn/technical-analysis/elliott-wave-theory)

### B.2 Fibonacci — evidência **Fraca isolado / Moderada em confluência**
- Estudo acadêmico multi-mercado: comportamento de preço em zonas Fibonacci **não difere estatisticamente** de zonas não-Fibonacci. Batchelor & Ramyar (2006): sem poder "mágico" nos níveis. [EXTERNO]
- Porém: **clusters de medições independentes** convergindo no mesmo preço elevam a probabilidade de reação; a confluência (com S/R, estrutura, médias) é o que agrega valor. [EXTERNO]
- *Implicação SOT:* coerente com Fibonacci como **validador geométrico** (não criador de contagem) e com a exigência de confluência por independência (ver S-13).
- Fontes: [ScienceDirect — automatic Fibonacci evaluation](https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495), [The Bull — confluence matters more than ratios](https://thebull.com.au/technical-analysis/fibonacci-retracement-guide/), [Fibonacci clusters](https://forextraininggroup.com/using-fibonacci-clusters-to-increase-your-trading-odds/)

### B.3 SMC — evidência **Fraca a Anedótica** (melhora com backtest de regras objetivas)
- BOS/CHoCH/MSS (estrutura), Order Block, FVG, varredura de liquidez — componentes bem descritos e replicáveis como regra, porém a validação séria depende de **regras objetivas + backtest em dados reais**; a aplicação discricionária tende a "ver padrões no retrovisor". [EXTERNO]
- Setups empilhados (múltiplas confluências) relatam win-rate maior que confluência única — **mas a fonte alerta que o diferencial é o backtest**, não o empilhamento em si. [EXTERNO]
- *Implicação SOT:* coerente com SMC como sub-hipótese institucional (INV-01); o ganho real exige codificação objetiva + walk-forward (ver S-20).
- Fontes: [Backtrex — SMC guide 2026](https://backtrex.com/en/blog/what-is-smart-money-concepts-trading), [TradingWyckoff — SMC complete](https://tradingwyckoff.com/en/smart-money-concepts/)

### B.4 ICT — evidência **Fraca a Anedótica** (proprietário, parcialmente não-falseável)
- Killzones (janelas de sessão), OTE (zona de retração 62–79%), Power-of-3 / AMD (acumulação→manipulação→distribuição), Silver Bullet — conceitos de **Michael Huddleston (Inner Circle Trader)**, majoritariamente **proprietários e anedóticos**. [EXTERNO]
- Teste mecânico independente: bot ICT totalmente mecânico (sweeps+MSS+FVG) terminou **−15,1R / win-rate 29,6% / profit factor 0,81** em 1 ano; o **mesmo** framework com julgamento discricionário de um analista terminou **+27,6R / 40,4%** em 2 meses — sugere que **o edge, se existe, está na discricionariedade, não na mecânica**. [EXTERNO] *(Atenção: 2 meses é amostra pequena — evidência Fraca para ambos os lados; RULE-MET-01.)*
- AMD no daily mapeia a sessões: acumulação=Ásia, manipulação=abertura Londres (varre um lado do range asiático), distribuição=NY. [EXTERNO]
- *Implicação SOT:* usar ICT como **timing/refinamento** (WF-05), nunca como gerador de hipótese (INV-02); tratar reivindicações não-falseáveis com ceticismo documentado.
- Fontes: [offbeatforex — ICT backtest com IA](https://offbeatforex.com/is-ict-strategy-profitable/), [litefinance — killzones](https://www.litefinance.org/blog/for-beginners/trading-strategies/ict-killzones/), [fluxcharts — Power of Three](https://www.fluxcharts.com/articles/trading-strategies/ict-strategies/ict-power-of-three), [theinnercircletraders — PO3](https://www.theinnercircletraders.com/ict-power-of-3/)

### B.5 Order Flow — evidência **Moderada (mecanismo plausível) / limitada por dados**
- Delta (compra−venda agressiva por nível/barra), CVD (delta acumulado), absorção (limite grande refilado contra ordens a mercado no DOM), footprint, imbalance — ferramentas de microestrutura reais. [EXTERNO]
- **Aplicabilidade por ativo é desigual:** futuros são os dados mais limpos (CME/Eurex centralizado); BTC tem os books mais profundos do cripto (order flow "mais limpo" do setor), mas **perp flow é guiado por alavancagem e rápido**, spot é mais lento/"real"; cripto é **exchange-specific** (CVD reflete a venue). Ações variam com qualidade do Level 2. [EXTERNO]
- *Implicação SOT:* order flow é candidato natural à **dimensão de volume** do Conviction Vector 8D — porém com **ressalva explícita de disponibilidade/qualidade de dados por ativo** (BTC spot vs perp, XAU, NASDAQ). Não há garantia de dados de footprint retail para todos os ativos.
- Fontes: [ATAS — CVD guide](https://atas.net/volume-analysis/basics-of-volume-analysis/cvd-pro/), [markettrace — order flow crypto perps](https://markettrace.ai/blog/order-flow-trading), [traderprofesional — BTC order flow](https://traderprofesional.com/en/bitcoin-order-flow/)

### B.6 Multi-Timeframe top-down — evidência **Moderada (consenso metodológico)**
- Razão típica **4:1 a 6:1** entre níveis de TF. Exemplos padrão: swing = diário (viés) / 4h (setup) / 1h (entrada); day = 4h (contexto) / 1h (setup) / 15m (execução); "Triple Screen" exige confirmação de 3 TFs. [EXTERNO]
- *Implicação SOT:* dá base concreta para WF-01 (TF + tipo) e para WF-05 ("TF de entrada diferente do contexto"). Ver S-06/S-07.
- Fontes: [hoclamtrader — MTF framework](https://hoclamtrader.com/en/multi-timeframe-analysis-complete-guide/), [Signal Pilot — MTF confirmation](https://blog.signalpilot.io/articles/multi-timeframe-confirmation/), [traze — timeframes](https://traze.com/academy/advanced-strategies-forex-brokers/multiple-timeframe-analysis-methods-strategies/)

### B.7 Pipeline de decisão em camadas / máquina de estados — evidência **Forte (engenharia)**
- Pipeline canônico: **market data → signal → risk → order management → execution**, fluxo unidirecional, cada componente com uma só função. [EXTERNO]
- Sequência de avaliação: **regime filter → setup → trigger**; "regime é o filtro de contexto mais importante — todo sinal significa algo diferente dependendo do regime". [EXTERNO]
- **O núcleo do Order Management é uma máquina de estados determinística; sem ela, edge-cases criam "posições fantasma"**. Pré-trade risk checks: limites de posição, P&L diário, sanity de preço, rate limiting, allowlist de instrumento. [EXTERNO]
- *Implicação SOT:* corrobora a separação sinal/risco já no workflow (WF-06 síntese vs WF-07 risco) e recomenda máquina de estados explícita para o ciclo de setup (ver S-12).
- Fontes: [NexusFi — trading system architecture](https://nexusfi.com/a/automation/trading-system-architecture), [mbrenndoerfer — quant architecture](https://mbrenndoerfer.com/writing/quant-trading-system-architecture-infrastructure)

### B.8 Confluência / independência de sinais — evidência **Moderada (importa de multicolinearidade)**
- "Confluência escala com **independência**, não com contagem"; setups com 5+ fatores tendem a **underperformar** 2–4 fatores independentes; indicadores que concordam >85–90% do tempo medem informação sobreposta. [EXTERNO]
- Sinais independentes vêm de **fontes de dados diferentes**: estrutura de preço, momentum, volume, tempo/sessão. [EXTERNO]
- *Implicação SOT:* reforça PE-08/AP-02/PCO-06 e a hierarquia não-compensatória; ver S-13. Order flow (volume) e killzone (tempo/sessão) são as dimensões **mais independentes** de Elliott/SMC (estrutura).
- Fontes: [metatradingclub — stacking independent signals](https://www.metatradingclub.com/confluence-in-trading/), [draconic — why signals mislead](https://draconic.ai/blog/confluence-trading-independent-signals), [traderssecondbrain — how many factors](https://traderssecondbrain.com/guides/setup-confluence-factors)

### B.9 Ordens condicionais / alarme-armed — evidência **Forte (prática de mercado)**
- Ordem condicional: executa só quando critérios (preço/tempo/outra-ordem) são atendidos. Padrões OCO (um cancela o outro) e OTOCO (um dispara OCO). GTC com expiração até 180 dias; "defina expiração em cada alerta na criação; o que você não renovar conscientemente deve morrer sozinho". [EXTERNO]
- "Cenários mais complexos exigem controlar e rastrear **estados** (flags/valores que sinalizam condições)." [EXTERNO]
- *Implicação SOT:* o WF-D02 (alarme-gatilho) é exatamente este padrão; ver S-03/S-04/S-05.
- Fontes: [Fidelity — conditional orders](https://www.fidelity.com/learning-center/trading-investing/trading/conditional-order-types), [IBKR — conditional orders](https://www.interactivebrokers.com/campus/trading-lessons/conditional-orders/), [quantopia — conditional order best practices](https://www.quantopia.net/blog/conditional-order-meaning-overview-examples/), [TradingView — alerts](https://www.tradingview.com/pine-script-docs/faq/alerts/)

### B.10 Backtest / anti-overfitting — evidência **Forte (metodologia)**
- Walk-forward é o padrão de validação (re-otimização em janelas rolantes, OOS repetido). **Insuficiente sozinho** sob múltiplos testes: usar **Deflated Sharpe Ratio** (corrige viés de seleção), **PBO via CSCV** (probabilidade de overfitting), Combinatorial Purged CV. Estratégias sobreajustadas **sistematicamente underperformam** fora da amostra. [EXTERNO]
- *Implicação SOT:* qualquer codificação das regras discricionárias de Elliott/SMC/ICT exige walk-forward + correção de múltiplos testes, com **evidência por regra** (coerente com SES-001 §35 validação empírica). Ver S-20.
- Fontes: [Wikipedia — walk forward optimization](https://en.wikipedia.org/wiki/Walk_forward_optimization), [arXiv 2512.12924 — walk-forward microstructure](https://arxiv.org/pdf/2512.12924), [QuantInsti — walk-forward](https://blog.quantinsti.com/walk-forward-optimization-introduction/)

### B.11 Risco-retorno / expectância — evidência **Forte (identidade matemática)**
- **Não existe R:R mínimo universal**; o que importa é a **expectância = f(win-rate, payoff)**. Win-rate de breakeven: 1:2 → 33,3%; 1:3 → 25%. Expectância positiva sse `win-rate × RR > (1 − win-rate)`. Sizing profissional: 1–2% fixo por trade; **a distância do stop determina o tamanho**, não o contrário. [EXTERNO]
- *Implicação SOT (apenas insumo):* o `INV-RISK-RR` (R:R ≥ 1:3) é **decisão soberana de Andraus** (AGENTS §6.5) e **não** é contestado aqui; a literatura apenas contextualiza que 1:3 implica tolerar win-rate ≥ 25% para breakeven. **Sizing/Kelly = escopo RISK-SPEC (adiado)** — não entra no Conviction Vector (INV-04). Ver S-22/S-23.
- Fontes: [backtrex — RR & expectancy](https://backtrex.com/en/blog/risk-reward-ratio-trading-expectancy-relationship), [tradingwithrayner — RR ratio](https://www.tradingwithrayner.com/risk-reward-ratio/)

### B.12 Multi-ativo / correlação / heat — evidência **Forte (dados de correlação)**
- BTC–NASDAQ: correlação 30d ~**0,88** (risco-off conjunto); BTC–ouro: baixa/variável/por vezes negativa; em crises de liquidez, correlações convergem a ~1,0 (tudo cai junto). [EXTERNO]
- *Implicação SOT:* operar BTC+NASDAQ em paralelo **não é diversificação** — é quase a mesma aposta; o `INV-RISK-HEAT` (≤15%) precisa ser **medido com correlação**, não por soma ingênua de riscos independentes. Escopo primário = Risk Agent, mas o workflow precisa decidir 1-ativo vs N-ativos. Ver S-16.
- Fontes: [onedayadvisor — BTC-Nasdaq 0.88](https://www.onedayadvisor.com/2025/01/bitcoin-nasdaq-correlation-correlation.html), [spark.money — BTC correlation](https://www.spark.money/tools/bitcoin-correlation-calculator), [WGC — gold optimal weight](https://www.gold.org/goldhub/gold-focus/2025/05/you-asked-we-answered-golds-optimal-portfolio-weight-higher-correlated)

### B.13 Human-in-the-loop / auditabilidade — evidência **Moderada (prática emergente)**
- Trilha de auditoria imutável por etapa: `request → ai_reasoning → policy_evaluation → decision → human_review → final_action`; registro que preserva **o que a IA disse vs. o que o humano decidiu** (a resolução nunca sobrescreve o veredito da máquina). HITL = humano aprova antes da execução. [EXTERNO]
- *Implicação SOT:* alinhado a P13 (reconstrução), D9 (auditoria), INV-07 (monotônico) e ao papel de Andraus como decisor. Ver S-18/S-19.
- Fontes: [arXiv 2608.28596 — evidence-traceable HITL](https://arxiv.org/pdf/2608.28596), [SAP — HITL approval/escalation/audit](https://community.sap.com/t5/artificial-intelligence-blogs-posts/human-in-the-loop-sap-agents-approval-escalation-and-audit-series-2-part-5/ba-p/14372994)

---

## C. Sugestões (S-01..S-24) — ordenadas por impacto

> Cada sugestão: **proposta · justificativa · evidência+fonte · riscos/limites · conflito possível com AGENTS §6 · opções (recomendada marcada ✅)**. Nenhuma fecha decisão — todas pedem decisão de Andraus.

### — Bloco I: WF-D01 Killzone —

#### S-01 — Parametrizar a Killzone **por ativo** (BTC 24/7 · XAU · NASDAQ cash open) — `WF-D01` / `WF-05`
- **Proposta:** definir a Killzone como janela temporal **por ativo**: NASDAQ ancorada à abertura cash (e, opcionalmente, à primeira hora NY); XAU às sobreposições Londres/NY; BTC, por ser 24/7, usar killzones de sessão como filtro **fraco** (ou substituí-las por gatilhos de volatilidade/volume, já que a premissa de "sessão" é menos válida).
- **Justificativa:** killzone é conceito de janela de alta atividade; sua eficácia "pode ser menor para ativos ilíquidos/locais" e é mais sólida em FX/ouro; BTC 24/7 enfraquece a lógica de sessão. [EXTERNO, Fraca/Anedótica — B.4]
- **Evidência:** [litefinance — killzones](https://www.litefinance.org/blog/for-beginners/trading-strategies/ict-killzones/), [offbeatforex](https://offbeatforex.com/is-ict-strategy-profitable/)
- **Riscos/limites:** evidência ICT é fraca; não tratar killzone como edge por si — é filtro de *quando olhar*, não de *o que fazer*.
- **Conflito AGENTS §6:** nenhum (não toca hierarquia nem convicção). Relaciona-se a N-001 (parâmetros por ativo).
- **Opções:** (a) ✅ killzone parametrizada por ativo, com BTC usando gatilho de volatilidade em vez de sessão; (b) killzone única por sessão igual para os 3 ativos; (c) sem killzone formal (gatilho sempre armado) — menos seletivo.

#### S-02 — Killzone: janela **fixa vs adaptativa**, dono do abrir/fechar, e **guard anti-DST** — `WF-D01` / `WF-04`→`WF-05`
- **Proposta:** declarar quem abre/fecha a Killzone (candidato: **Manager/Scheduler — SPEC-008/015**, não o agente analítico), se a janela é fixa (horário) ou adaptativa (volatilidade/volume realizados), e **obrigar cálculo em UTC com correção automática de horário de verão**.
- **Justificativa:** "razão comum de falha das killzones: traders derivam no horário sem perceber — a janela UTC se move 1h nas viradas de DST." [EXTERNO, Anedótica→prática — B.4]
- **Evidência:** [litefinance — DST drift](https://www.litefinance.org/blog/for-beginners/trading-strategies/ict-killzones/)
- **Riscos/limites:** janela adaptativa adiciona complexidade e exige dados de volatilidade em tempo real.
- **Conflito AGENTS §6:** nenhum.
- **Opções:** (a) ✅ fixa por horário **com guard DST** + dono = Manager/Scheduler; (b) adaptativa por volatilidade; (c) híbrida (fixa com extensão adaptativa).

### — Bloco II: WF-D02 Alarme-gatilho de preço —

#### S-03 — Estrutura canônica do **alarme-gatilho** (nível · direção · validade/expiração · invalidação · cancelamento) — `WF-D02` / `WF-04`
- **Proposta:** especificar o alarme-gatilho como objeto com campos mínimos: `nível`, `direção`, `condição de disparo`, `validade/expiração`, `nível de invalidação`, `condição de cancelamento`, `hipótese-origem (parent_id)`. Saída da Fase 1 do Manager; pré-condição da Fase 2.
- **Justificativa:** padrão consolidado de ordem condicional (trigger price/tempo/outra-ordem + expiração). [EXTERNO, Forte — B.9]
- **Evidência:** [IBKR conditional orders](https://www.interactivebrokers.com/campus/trading-lessons/conditional-orders/), [Fidelity](https://www.fidelity.com/learning-center/trading-investing/trading/conditional-order-types)
- **Riscos/limites:** não confundir alarme (interno, SOT) com ordem (externa, Bot Trade Finance) — INV-05.
- **Conflito AGENTS §6:** nenhum, desde que o alarme **não execute** (INV-05) — é gatilho de *análise*, não de ordem.
- **Opções:** (a) ✅ objeto com os 7 campos acima; (b) mínimo (nível+direção+expiração); (c) manter informal (status quo) — não recomendado (bloqueia Specs do Manager).

#### S-04 — Padrão **"armed state" / máquina de estados** do alarme (alert→armed→triggered→expired/cancelled) — `WF-D02` / `WF-04`→`WF-05`
- **Proposta:** modelar o alarme como FSM determinística: `IDLE → ARMED` (quando convicção macro conclusiva registra o nível) `→ TRIGGERED` (preço atinge o nível **dentro** da Killzone) `→ {CONSUMED | EXPIRED | CANCELLED}`. Disparo só válido após abertura da Killzone (coerente com WF-04/WF-05).
- **Justificativa:** "cenários complexos exigem rastrear estados (flags)"; ordens compostas OCO/OTOCO são FSMs de fato. Máquina de estados determinística evita "posições/estados fantasma". [EXTERNO, Forte — B.9/B.7]
- **Evidência:** [quantopia — conditional order states](https://www.quantopia.net/blog/conditional-order-meaning-overview-examples/), [NexusFi — deterministic state machine](https://nexusfi.com/a/automation/trading-system-architecture)
- **Riscos/limites:** a FSM é mecanismo (HOW) — pertence ao Plan do Manager (SPEC-015), não ao WORKFLOW.md; aqui é o *contrato* de estados.
- **Conflito AGENTS §6:** nenhum. ENF-03: o gate de disparo deve ser determinístico (não LLM).
- **Opções:** (a) ✅ FSM explícita de 4–5 estados; (b) flag binária armed/not-armed; (c) sem estado formal.

#### S-05 — **Expiração automática + cancelamento por refutação da hipótese** — `WF-D02` / integra CHM-001
- **Proposta:** todo alarme nasce com expiração (GTC-like com prazo) **e** é cancelado automaticamente se a hipótese-origem transita para `SUPERSEDED`/`REFUTED` (CHM-001). "O que não for renovado conscientemente morre sozinho."
- **Justificativa:** higiene de ordens condicionais + consistência epistêmica (não disparar sobre hipótese morta). [EXTERNO Forte — B.9] + [FONTE: CHM-001 estados; INV-07].
- **Evidência:** [TradingView — set expiry at creation](https://www.tradingview.com/pine-script-docs/faq/alerts/), [FONTE] AGENTS §6.3 estados CHM-001
- **Riscos/limites:** exige o alarme carregar `parent_id` da hipótese (liga a G-001/estado persistente).
- **Conflito AGENTS §6:** nenhum — reforça o versionamento monotônico (INV-07) e os estados canônicos (§6.3).
- **Opções:** (a) ✅ expiração temporal **e** cancelamento por refutação; (b) só expiração temporal; (c) só cancelamento manual.

### — Bloco III: WF-D03 convicção macro × global / multi-timeframe —

#### S-06 — Formalizar **razões de timeframe por tipo de trading** (position/swing/day) em WF-01 — `WF-D03` / `WF-01`
- **Proposta:** ao apontar "tipo de Trading" (WF-01), o operador fixa uma tripla **contexto / confirmação / entrada** com razão 4:1–6:1. Ex.: position = S/D/H4; swing = D/H4/H1; day = H4/H1/M15. (M5 de WF-05 encaixa como entrada para day/scalp.)
- **Justificativa:** padrão MTF consolidado; "Triple Screen" exige 3 TFs alinhados. [EXTERNO, Moderada — B.6]
- **Evidência:** [hoclamtrader — ratios](https://hoclamtrader.com/en/multi-timeframe-analysis-complete-guide/), [traze](https://traze.com/academy/advanced-strategies-forex-brokers/multiple-timeframe-analysis-methods-strategies/)
- **Riscos/limites:** razões são heurística de varejo (não lei); servem de default, recalibrável por backtest/ativo.
- **Conflito AGENTS §6:** nenhum.
- **Opções:** (a) ✅ tabela de triplas por tipo como default recalibrável; (b) só contexto+entrada (par); (c) deixar livre ao operador por missão.

#### S-07 — Regra de **alinhamento entre TF de contexto e TF de entrada** (WF-05) — `WF-D03` / `WF-05`
- **Proposta:** tornar explícito que o disparo operacional (WF-05) só é válido se a direção da entrada (TF baixo) **alinhar** com a hipótese de contexto (TF alto); divergência → sem entrada (candidato a ramo de falha, S-11).
- **Justificativa:** top-down "garante trades em harmonia com o movimento maior, não contra ele"; Triple Screen exige alinhamento. [EXTERNO, Moderada — B.6]
- **Evidência:** [Signal Pilot — stop fighting the trend](https://blog.signalpilot.io/articles/multi-timeframe-confirmation/)
- **Riscos/limites:** "alinhamento" precisa de definição operacional (ex.: direção da onda Elliott do contexto == direção do setup).
- **Conflito AGENTS §6:** nenhum — reforça INV-01 (camada inferior não sobrepõe superior).
- **Opções:** (a) ✅ alinhamento obrigatório contexto↔entrada; (b) alinhamento como peso (não veto); (c) sem regra explícita.

#### S-08 — Posicionar **convicção macro (contexto) × convicção global (entrada)** como duas leituras do mesmo vetor — `WF-D03` / `WF-04`+`WF-06`
- **Proposta:** registrar a hipótese arquitetural (a confirmar em SPEC-003) de que convicção macro = Conviction Vector 8D sobre o **subconjunto** de dimensões disponíveis na Fase 1 (estrutural+institucional) e convicção global = **mesmo** vetor com +operacional na Fase 2. **NÃO fechar** — é exatamente WF-D03 + SPEC-003 Q-A5 (motor 1x/2x).
- **Justificativa:** coerência com PCO-06 (não-redução) e dimensionalidade fechada=8; o Dossiê de abertura da SPEC-003 já levanta e mantém aberta esta questão (interpretação a vs b). [FONTE: SPEC-003/research §5.7, §3.3; GPR-001 PCO-06]
- **Evidência:** [FONTE] SPEC-003/research.md §5.7; [EXTERNO] confluência por independência (B.8) sustenta somar dimensões independentes.
- **Riscos/limites:** **DECISÃO ABERTA (WF-D03 + J-001 + SPEC-003 Q-A5)** — não decidir aqui.
- **Conflito AGENTS §6:** tocar J-001/limiares como fechados violaria CONS-01/INV-03 — por isso fica como leitura proposta, não norma.
- **Opções:** (a) ✅ um vetor, duas leituras (subconjunto Fase 1 / completo Fase 2) — mais coeso; (b) dois objetos de convicção distintos com pesos/limiares por fase; (c) manter em aberto sem direção até SPEC-003.

### — Bloco IV: WF-D04 papel do ICT —

#### S-09 — ICT como **timing/refinamento de entrada**, nunca criador de hipótese — `WF-D04` / `WF-05`
- **Proposta:** declarar que ICT atua no **refinamento operacional** (OTE 62–79% da perna, killzone, varredura de liquidez do PO3) sobre a hipótese já criada por Elliott (primária) e sub-hipótese SMC — consistente com INV-02.
- **Justificativa:** OTE é zona de retração 62–79%; PO3 (manipulação) descreve o sweep que precede a distribuição — ambos são **timing**, não tese direcional. Evidência mecânica fraca recomenda uso condicionado, não autônomo. [EXTERNO, Fraca/Anedótica — B.4]
- **Evidência:** [fluxcharts — PO3/OTE](https://www.fluxcharts.com/articles/trading-strategies/ict-strategies/ict-power-of-three), [offbeatforex — discrição > mecânica](https://offbeatforex.com/is-ict-strategy-profitable/)
- **Riscos/limites:** parte do ICT é **não-falseável/proprietária** — adotar só os elementos operacionais objetivos (OTE, killzone, sweep), com ceticismo documentado.
- **Conflito AGENTS §6:** **respeita** INV-02 (ICT só executa); violaria se ICT gerasse hipótese.
- **Opções:** (a) ✅ ICT = camada de timing/refino no WF-05; (b) ICT como uma dimensão a mais de convicção operacional (sem timing dedicado); (c) ICT opcional/desligável por ativo.

#### S-10 — **Ponto de entrada do ICT no pipeline**: dentro do Agente Operacional (WF-05) — `WF-D04` / `WF-05`
- **Proposta:** situar o ICT Specialist como competência **dentro** do Agente Operacional (M5/TF de entrada), após o alarme disparar, para refinar entrada/stop/alvo/invalidação operacional — mapeável a INV-02 ("ICT executa entrada/timing/stop/targets/invalidação operacional").
- **Justificativa:** o pipeline declarado já tem Operacional no WF-05; ICT como timing encaixa sem criar novo passo. AMD mapeia manipulação→abertura Londres, distribuição→NY, reforçando dependência da Killzone. [EXTERNO — B.4] + [FONTE: INV-02].
- **Evidência:** [theinnercircletraders — PO3/AMD por sessão](https://www.theinnercircletraders.com/ict-power-of-3/)
- **Riscos/limites:** relaciona-se a I-001 (FECHADA: híbrido por Classe) e SPEC-025 (Skill≠agente) — detalhe de "como" fica para essas Specs.
- **Conflito AGENTS §6:** nenhum (respeita INV-01/INV-02).
- **Opções:** (a) ✅ ICT dentro do Agente Operacional no WF-05; (b) ICT como agente/skill separado invocado no WF-05; (c) manter ICT ausente do pipeline até SPEC-013/014.

### — Bloco V: Ramos de falha e máquina de estados do ciclo —

#### S-11 — **Ramos de falha explícitos** do pipeline (sem oportunidade · discordância · não-confirmação · veto de risco · expiração/reset · reentrada) — todos os WF
- **Proposta:** declarar explicitamente, em cada passo, a saída negativa: WF-02/03 sem oportunidade → encerra ciclo; WF-03/04 discordância Estrutural×Institucional → NEUTRO (coerente com §6.4 conflito direcional); WF-05 sem confirmação operacional → reset do alarme; WF-07 veto de risco → sem sinal; alarme expira → reset; condição de reentrada após stop.
- **Justificativa:** sistemas robustos modelam estados e caminhos negativos; "edge-cases sem FSM criam posições fantasma". [EXTERNO, Forte — B.7]
- **Evidência:** [NexusFi — state machine / edge cases](https://nexusfi.com/a/automation/trading-system-architecture)
- **Riscos/limites:** reentrada precisa de regra anti-overtrading (limite por ciclo/sessão).
- **Conflito AGENTS §6:** "discordância direcional → NEUTRO" alinha com §6.4; veto de risco alinha com WF-07/INV-05.
- **Opções:** (a) ✅ 6 ramos de falha explícitos no workflow; (b) só os 3 críticos (discordância, não-confirmação, veto); (c) tratar caso-a-caso nas Specs.

#### S-12 — **Máquina de estados do ciclo de setup inteiro** (determinística, auditável) — cross WF-01..07
- **Proposta:** além do alarme (S-04), modelar o ciclo completo como FSM: `AGUARDANDO_CONTEXTO → CONTEXTO_FORMADO → ARMADO → ATIVADO(Killzone) → EM_SÍNTESE → EM_RISCO → {SINAL_ENVIADO | RECUSADO | EXPIRADO}`. Transições determinísticas; LLM nunca é o próprio gate (ENF-03).
- **Justificativa:** FSM determinística é "o núcleo de qualquer OMS"; evita estados fantasma; dá base de auditoria (D9). [EXTERNO, Forte — B.7]
- **Evidência:** [NexusFi](https://nexusfi.com/a/automation/trading-system-architecture), [mbrenndoerfer](https://mbrenndoerfer.com/writing/quant-trading-system-architecture-infrastructure)
- **Riscos/limites:** é mecanismo do Manager (SPEC-015) — o WORKFLOW.md declara os estados; o Plan implementa.
- **Conflito AGENTS §6:** reforça ENF-03 (gate determinístico) e P13/D9.
- **Opções:** (a) ✅ FSM completa do ciclo declarada no WORKFLOW; (b) só estados de alarme (S-04) + ramos (S-11); (c) adiar para SPEC-015.

### — Bloco VI: Qualidade de confluência e dimensão de volume —

#### S-13 — Confluência por **independência**, não por contagem (anti double-counting) — `WF-02`/`WF-03`/`WF-06`
- **Proposta:** ao formar convicção (Fases 1 e 2), tratar Elliott (estrutura), Fibonacci (geometria), SMC (institucional), ICT (timing), Order Flow (volume), Killzone (tempo) como fontes de **independência variável**; descontar confirmações redundantes (Fib e Elliott medem parte da mesma coisa estrutural).
- **Justificativa:** "confluência escala com independência, não contagem"; 5+ fatores correlacionados underperformam 2–4 independentes; >85–90% de concordância = informação sobreposta. [EXTERNO, Moderada — B.8]
- **Evidência:** [metatradingclub](https://www.metatradingclub.com/confluence-in-trading/), [draconic](https://draconic.ai/blog/confluence-trading-independent-signals)
- **Riscos/limites:** a **mecânica de desconto** é da SPEC-002/003 (GAP-FUSION-DEP); aqui é o *princípio*, não a calibração (J-001).
- **Conflito AGENTS §6:** **reforça** PE-08/AP-02/PCO-06 e a agregação não-compensatória (CONFLITO-2 do SPEC-003). Calibração = J-001 (aberta).
- **Opções:** (a) ✅ adotar independência como princípio de confluência (remetendo mecânica à SPEC-002/003); (b) só documentar como alerta de viés; (c) não tratar (risco de convicção inflada).

#### S-14 — **Order flow (volume/agressão)** como dimensão de volume do Conviction Vector, com ressalva de dados por ativo — `WF-05`/`WF-06`
- **Proposta:** candidatar CVD/delta/absorção à **dimensão de volume** (das 8 do Conviction Vector), declarando explicitamente a **disponibilidade/qualidade de dados por ativo** (BTC spot vs perp venue-specific; XAU/NASDAQ via futuros = dado mais limpo). Onde o dado não existe/é ruim → dimensão `INDETERMINADO`, não zero.
- **Justificativa:** order flow é a fonte mais **independente** de estrutura/geometria; mecanismo plausível, mas "cripto é exchange-specific; perp é alavancado/rápido". [EXTERNO, Moderada — B.5]
- **Evidência:** [markettrace — order flow perps](https://markettrace.ai/blog/order-flow-trading), [traderprofesional — BTC spot vs perp CVD](https://traderprofesional.com/en/bitcoin-order-flow/)
- **Riscos/limites:** não há garantia de footprint de varejo para todos os ativos; não fabricar a dimensão (RULE-UNC/PRB/MET).
- **Conflito AGENTS §6:** nenhum; respeita INV-03 (dimensionalidade=8) e RULE-UNC (INDETERMINADO válido).
- **Opções:** (a) ✅ order flow = dimensão de volume com `INDETERMINADO` quando dado falta; (b) order flow só para BTC; (c) não usar order flow (dimensão de volume por outra proxy).

### — Bloco VII: Multi-ativo, regime e calibração por ativo —

#### S-15 — **Filtro de regime** como gate antes do setup/trigger — `WF-02` (ou novo passo pré-WF-02)
- **Proposta:** inserir, antes da Fase 1, um filtro de regime (tendência/range/alta-vol) que condiciona se o ciclo prossegue — "regime é o filtro de contexto mais importante; todo sinal significa algo diferente por regime".
- **Justificativa:** sequência canônica regime→setup→trigger; regime muda o significado do sinal. [EXTERNO, Forte — B.7]
- **Evidência:** [NexusFi — regime filter](https://nexusfi.com/a/automation/trading-system-architecture)
- **Riscos/limites:** adiciona dependência de classificação de regime (relaciona-se a SES-001 §33 "regime"); risco de over-filtering.
- **Conflito AGENTS §6:** nenhum; complementa Elliott (que já carrega noção de fase de mercado).
- **Opções:** (a) ✅ filtro de regime explícito pré-Fase 1; (b) regime como dimensão de convicção (não gate); (c) sem filtro de regime dedicado.

#### S-16 — **Um ativo vs multi-ativo em paralelo** + heat ciente de correlação — `WF-06`/`WF-07` (primário Risk Agent)
- **Proposta:** decidir se o SOT opera 1 ativo por vez ou BTC/XAU/NASDAQ em paralelo; se paralelo, o `INV-RISK-HEAT` (≤15%) deve ser medido **com correlação** (BTC+NASDAQ ~0,88 ≈ aposta dobrada), não por soma de riscos independentes.
- **Justificativa:** correlações altas e convergentes em crise; "portfólio com Nasdaq+BTC é menos diversificado do que parece". [EXTERNO, Forte — B.12]
- **Evidência:** [onedayadvisor — 0.88](https://www.onedayadvisor.com/2025/01/bitcoin-nasdaq-correlation-correlation.html), [WGC — correlated environment](https://www.gold.org/goldhub/gold-focus/2025/05/you-asked-we-answered-golds-optimal-portfolio-weight-higher-correlated)
- **Riscos/limites:** cálculo de heat correlacionado é **escopo do Risk Agent (RISK-SPEC, adiado)**; aqui é insumo + decisão de paralelismo no workflow.
- **Conflito AGENTS §6:** INV-04 (custo fora da convicção) preservado — heat é de risco, não de convicção; INV-RISK-HEAT é de Andraus.
- **Opções:** (a) ✅ definir paralelismo no workflow + heat correlacionado remetido ao Risk Agent; (b) 1 ativo por vez (simples, sem heat de carteira); (c) N-ativos com heat por soma ingênua (não recomendado — subestima risco).

#### S-17 — **Calibração de parâmetros por ativo** (ganchos N-001) — `WF-01` / transversal
- **Proposta:** declarar que killzone, razões de TF, limiares de volume e pesos de convicção podem variar por ativo (BTC/XAU/NASDAQ), criando o "gancho" para N-001 sem fechar os valores (pós-backtest).
- **Justificativa:** eficácia de killzone/order flow varia por ativo; correlações e microestrutura diferem. [EXTERNO, Moderada — B.4/B.5/B.12]
- **Evidência:** [litefinance](https://www.litefinance.org/blog/for-beginners/trading-strategies/ict-killzones/), [traderprofesional](https://traderprofesional.com/en/bitcoin-order-flow/)
- **Riscos/limites:** **N-001 é DECISÃO ABERTA** (pesos por ativo, pós-backtest) — não fechar valores aqui (CONS-01).
- **Conflito AGENTS §6:** tocar valores de N-001/J-001 como fechados violaria INV-03/CONS-01 — por isso só o *mecanismo*.
- **Opções:** (a) ✅ parametrização por ativo como mecanismo (valores → N-001/backtest); (b) parâmetros globais iguais para os 3 ativos; (c) adiar integralmente a SPEC-003/RISK.

### — Bloco VIII: Auditabilidade, HITL e validação —

#### S-18 — **Trilha de auditoria / decision journal** do ciclo (o que o SOT recomendou × o que Andraus decidiu) — transversal (D9/P13/INV-07)
- **Proposta:** cada ciclo registra, imutavelmente, as transições de estado, convicções (macro e global), hipóteses e suas refutações, e — quando houver intervenção — **o veredito do sistema vs. a decisão humana**, sem sobrescrever o primeiro.
- **Justificativa:** trilha `request→reasoning→policy→decision→human_review→final_action`; "a resolução nunca sobrescreve o veredito da máquina". [EXTERNO, Moderada — B.13]
- **Evidência:** [arXiv 2608.28596](https://arxiv.org/pdf/2608.28596), [SAP HITL audit](https://community.sap.com/t5/artificial-intelligence-blogs-posts/human-in-the-loop-sap-agents-approval-escalation-and-audit-series-2-part-5/ba-p/14372994)
- **Riscos/limites:** liga-se a G-001 (estado persistente) e SPEC-018 (K-001).
- **Conflito AGENTS §6:** reforça INV-07 (monotônico) e P13 (reconstrução).
- **Opções:** (a) ✅ decision journal imutável por ciclo; (b) só log de estados (sem veredito-vs-decisão); (c) adiar à SPEC-018.

#### S-19 — **Human-in-the-loop** como checkpoint explícito (Andraus/operador) — `WF-06`/`WF-07`
- **Proposta:** declarar explicitamente onde há aprovação humana antes de o Signal Package cruzar a fronteira (WF-07 → Bot Trade Finance), coerente com INV-05 (SOT não executa) e com o papel de Andraus como decisor.
- **Justificativa:** HITL = humano aprova antes da execução; serve de primitiva de auditoria. [EXTERNO, Moderada — B.13]
- **Evidência:** [SAP HITL](https://community.sap.com/t5/artificial-intelligence-blogs-posts/human-in-the-loop-sap-agents-approval-escalation-and-audit-series-2-part-5/ba-p/14372994)
- **Riscos/limites:** grau de automação é decisão de Andraus; HITL pode ser opcional por tipo de trading.
- **Conflito AGENTS §6:** reforça INV-05; não cria execução automática.
- **Opções:** (a) ✅ checkpoint HITL explícito antes da fronteira; (b) HITL só acima de certo risco/convicção; (c) totalmente automatizado até o Bot (sem HITL).

#### S-20 — **Walk-forward + correção de múltiplos testes** para codificar regras discricionárias — transversal (SES-001 §35)
- **Proposta:** condicionar a eventual codificação das regras de Elliott/SMC/ICT a validação walk-forward + Deflated Sharpe / PBO (CSCV), com **evidência por regra** registrada (não por sistema inteiro).
- **Justificativa:** walk-forward é padrão, mas insuficiente sob múltiplos testes; estratégias sobreajustadas sistematicamente underperformam. [EXTERNO, Forte — B.10]
- **Evidência:** [arXiv 2512.12924](https://arxiv.org/pdf/2512.12924), [QuantInsti](https://blog.quantinsti.com/walk-forward-optimization-introduction/)
- **Riscos/limites:** é fase de implementação (BUILD/VERIFY adiados — spec-first); aqui é o *requisito* a herdar.
- **Conflito AGENTS §6:** alinha com SES-001 §35 (validação empírica) e PE-04/Classe (D/H/P/C).
- **Opções:** (a) ✅ exigir walk-forward+DSR/PBO por regra na implementação; (b) só walk-forward simples; (c) validação qualitativa/discricionária (não recomendado).

#### S-21 — **Rotulagem honesta de qualidade de evidência por escola** no setup — transversal (RULE-MET-01)
- **Proposta:** registrar, junto de cada escola no pipeline, sua qualidade de evidência (Elliott: regras falseáveis / contagem subjetiva; Fibonacci: só em confluência; SMC/ICT: fraca-anedótica; Order Flow: moderada/dependente de dados), para evitar excesso de confiança e falsa precisão.
- **Justificativa:** honestidade epistêmica anti-bajulação; evita tratar folclore como evidência (RULE-MET-01/EPI). Teste mecânico de ICT negativo vs discricionário positivo mostra fragilidade da base. [EXTERNO, variado — B.1–B.5]
- **Evidência:** [offbeatforex](https://offbeatforex.com/is-ict-strategy-profitable/), [ScienceDirect Fibonacci](https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495)
- **Riscos/limites:** não confundir "evidência fraca" com "inútil" — fraca pode ter valor em confluência/timing.
- **Conflito AGENTS §6:** reforça CC-09 (status epistêmico) e RULE-MET-01.
- **Opções:** (a) ✅ rótulo de qualidade por escola, visível no raciocínio; (b) só documentar no dossiê (não no runtime); (c) não rotular.

### — Bloco IX: Risco-retorno (apenas insumo — escopo RISK-SPEC) —

#### S-22 — **Expectância como métrica-raiz**, R:R 1:3 como piso soberano (não contestado) — `WF-07` (insumo Risk)
- **Proposta:** registrar, como insumo para o Risk Agent, que a métrica que governa lucratividade é a **expectância = f(win-rate, R:R)**, e que 1:3 (INV-RISK-RR, decisão de Andraus) implica tolerar win-rate ≥ 25% para breakeven. Sem propor mudar o piso.
- **Justificativa:** "não existe R:R mínimo universal; o que importa é expectância"; breakeven 1:3 = 25%. [EXTERNO, Forte — B.11]
- **Evidência:** [backtrex — RR & expectancy](https://backtrex.com/en/blog/risk-reward-ratio-trading-expectancy-relationship)
- **Riscos/limites:** **não** reabrir INV-RISK-RR (soberano, §6.5); apenas contextualizar.
- **Conflito AGENTS §6:** manter 1:3 como está; medir expectância é do Risk Agent (RISK-SPEC).
- **Opções:** (a) ✅ adotar expectância como métrica de avaliação do Risk Agent, mantendo 1:3 como piso; (b) manter só R:R como métrica; (c) adiar integralmente ao RISK-SPEC.

#### S-23 — **Sizing pela distância do stop** (1–2% fixo) como insumo ao Risk Agent — `WF-07` (insumo Risk)
- **Proposta:** registrar o padrão "a distância do stop determina o tamanho (risco fixo 1–2%/trade)" como insumo ao Risk Agent / `INV-RISK-LEV` (threshold em aberto, m-002). Kelly permanece **adiado**.
- **Justificativa:** sizing profissional padrão; stop define tamanho, não o contrário. [EXTERNO, Forte — B.11]
- **Evidência:** [tradingwithrayner — RR/sizing](https://www.tradingwithrayner.com/risk-reward-ratio/)
- **Riscos/limites:** **escopo RISK-SPEC**; INV-04 proíbe custo/sizing na convicção — manter separado.
- **Conflito AGENTS §6:** respeita INV-04 (sizing ≠ convicção); m-002 (threshold de alavancagem) permanece aberto.
- **Opções:** (a) ✅ registrar como insumo ao Risk Agent (Kelly adiado); (b) adiar tudo ao RISK-SPEC sem registro; (c) fixar % agora (não recomendado — prematuro).

#### S-24 — **Reforçar separação sinal ↔ risco** com fluxo unidirecional (WF-06→WF-07) — `WF-06`/`WF-07`
- **Proposta:** declarar explicitamente que WF-06 (síntese/convicção) e WF-07 (risco) são componentes com **uma função cada** e fluxo unidirecional; o risco **não** retroalimenta a convicção (INV-04).
- **Justificativa:** pipeline canônico = fluxo unidirecional, componentes com função única; separação risk engine ↔ signal engine. [EXTERNO, Forte — B.7]
- **Evidência:** [NexusFi](https://nexusfi.com/a/automation/trading-system-architecture), [mbrenndoerfer](https://mbrenndoerfer.com/writing/quant-trading-system-architecture-infrastructure)
- **Riscos/limites:** já parcialmente implícito no workflow; é formalização.
- **Conflito AGENTS §6:** reforça INV-04 e INV-05.
- **Opções:** (a) ✅ formalizar fluxo unidirecional e separação; (b) manter implícito; (c) permitir feedback risco→convicção (viola INV-04 — rejeitado).

---

## D. O que o SOT já tem normativo (NÃO precisa decidir — não reabrir)

| Tema | Norma vigente SOT | Não reabrir porque |
|---|---|---|
| Hierarquia analítica | Elliott→Fibonacci→Fractal→SMC→ICT (INV-01/CC-01) | Decisão homologada (§6.1) |
| ICT não cria hipótese | INV-02 / Q-005 | Homologado — S-09/S-10 **respeitam** |
| Conflito direcional → NEUTRO | AGENTS §6.4 | Já normativo — S-11 apenas o referencia |
| R:R ≥ 1:3 | INV-RISK-RR / §6.5 | Soberano de Andraus — S-22 não contesta |
| Convicção ≥70% e score ≥7/9 | §6.6 (Fase Piloto, recalibrável) | Interino homologado |
| Conviction Vector = 8 dimensões | INV-03 / Q-008 | Dimensionalidade **fechada** |
| Custo/sizing fora da convicção | INV-04 | Homologado — S-14/S-16/S-23 respeitam |
| SOT não executa; Signal Package na fronteira; TMP interno | INV-05 / EUA-E19a | Homologado — S-03/S-19 respeitam |
| Evidência ≠ Observação | INV-06 | Homologado |
| Versionamento monotônico | INV-07 | Homologado — S-05/S-18 reforçam |
| LLM nunca é seu próprio gate | ENF-03 | Homologado — S-04/S-12 respeitam |
| Portfolio Heat ≤15% | INV-RISK-HEAT | Instituído (EUA-E19a) — S-16 só refina medição |
| Confluência falsa / independência / não-redução | PE-08 / AP-02 / PCO-06 | Já principiológico — S-13 reforça |

## E. Lacunas e INDETERMINADOS (honestidade — RULE-MET-01)

1. **Base empírica fraca de ICT/SMC/Elliott/Fibonacci isolados.** Nenhuma escola tem taxa de acerto publicada e verificada independentemente; Fibonacci isolado não difere estatisticamente de níveis aleatórios; ICT mecânico foi negativo em teste de 1 ano. O valor, se existe, está em **confluência independente + timing + discricionariedade** — não em cada escola isolada. **INDETERMINADO** se o edge sobrevive à codificação (depende de walk-forward — S-20). [EXTERNO — B.1/B.2/B.4]
2. **Amostras pequenas** nos testes "positivos" (ICT discricionário: 2 meses). Não confiar em resultados de amostra curta para nenhum dos lados.
3. **Disponibilidade de order flow por ativo** não está garantida (BTC perp vs spot, XAU, NASDAQ) — a dimensão de volume pode ficar `INDETERMINADO` em alguns ativos (S-14).
4. **Relação convicção macro × global ↔ Conviction Vector 8D** (WF-D03) é genuinamente aberta e entrelaçada com **J-001** e **SPEC-003 Q-A5 (motor 1x/2x)** — este dossiê **não** a resolve.
5. **Terminologia "Conviction Engine"** tem acepção concorrente (motor separado vs. Fase 2 do Manager) — ver SPEC-003 CONFLITO-1 / Q-A6; não reconciliada aqui.
6. **Pesos por ativo (N-001), fórmula/limiares definitivos (J-001), threshold de alavancagem (m-002), localização do ARR (RISK-ARR-LOC-001)** permanecem abertos — nenhuma sugestão os fecha (CONS-01).
7. Este dossiê **não auditou a veracidade das páginas citadas** (mandato de pesquisa, não de verificação factual); tratá-las como DADO.

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-01)

- [cwcount — Elliott Wave rules](https://cwcount.com/education/elliott-wave-principle-rules/)
- [LuxAlgo — Elliott pattern rules](https://www.luxalgo.com/blog/elliott-wave-theory-pattern-rules-simplified/)
- [Ironclad Research — Elliott Wave](https://www.ironcladresearch.com/learn/technical-analysis/elliott-wave-theory)
- [ScienceDirect — automatic Fibonacci evaluation (empirical)](https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495)
- [The Bull — Fibonacci confluence](https://thebull.com.au/technical-analysis/fibonacci-retracement-guide/)
- [Forex Training Group — Fibonacci clusters](https://forextraininggroup.com/using-fibonacci-clusters-to-increase-your-trading-odds/)
- [Backtrex — SMC guide 2026](https://backtrex.com/en/blog/what-is-smart-money-concepts-trading)
- [TradingWyckoff — SMC complete](https://tradingwyckoff.com/en/smart-money-concepts/)
- [offbeatforex — ICT backtest com IA](https://offbeatforex.com/is-ict-strategy-profitable/)
- [LiteFinance — ICT killzones](https://www.litefinance.org/blog/for-beginners/trading-strategies/ict-killzones/)
- [FluxCharts — ICT Power of Three](https://www.fluxcharts.com/articles/trading-strategies/ict-strategies/ict-power-of-three)
- [The Inner Circle Traders — PO3/AMD](https://www.theinnercircletraders.com/ict-power-of-3/)
- [ATAS — CVD guide](https://atas.net/volume-analysis/basics-of-volume-analysis/cvd-pro/)
- [MarketTrace — order flow crypto perps](https://markettrace.ai/blog/order-flow-trading)
- [Trader Profesional — BTC order flow (spot vs perp)](https://traderprofesional.com/en/bitcoin-order-flow/)
- [hoclamtrader — MTF framework](https://hoclamtrader.com/en/multi-timeframe-analysis-complete-guide/)
- [Signal Pilot — MTF confirmation](https://blog.signalpilot.io/articles/multi-timeframe-confirmation/)
- [traze — timeframes](https://traze.com/academy/advanced-strategies-forex-brokers/multiple-timeframe-analysis-methods-strategies/)
- [NexusFi — trading system architecture](https://nexusfi.com/a/automation/trading-system-architecture)
- [mbrenndoerfer — quant architecture](https://mbrenndoerfer.com/writing/quant-trading-system-architecture-infrastructure)
- [metatradingclub — stacking independent signals](https://www.metatradingclub.com/confluence-in-trading/)
- [draconic — confluence independent signals](https://draconic.ai/blog/confluence-trading-independent-signals)
- [traderssecondbrain — setup confluence factors](https://traderssecondbrain.com/guides/setup-confluence-factors)
- [Fidelity — conditional order types](https://www.fidelity.com/learning-center/trading-investing/trading/conditional-order-types)
- [Interactive Brokers — conditional orders](https://www.interactivebrokers.com/campus/trading-lessons/conditional-orders/)
- [quantopia — conditional order best practices](https://www.quantopia.net/blog/conditional-order-meaning-overview-examples/)
- [TradingView — alerts](https://www.tradingview.com/pine-script-docs/faq/alerts/)
- [Wikipedia — walk forward optimization](https://en.wikipedia.org/wiki/Walk_forward_optimization)
- [arXiv 2512.12924 — walk-forward microstructure](https://arxiv.org/pdf/2512.12924)
- [QuantInsti — walk-forward](https://blog.quantinsti.com/walk-forward-optimization-introduction/)
- [backtrex — RR & expectancy](https://backtrex.com/en/blog/risk-reward-ratio-trading-expectancy-relationship)
- [tradingwithrayner — RR ratio & sizing](https://www.tradingwithrayner.com/risk-reward-ratio/)
- [onedayadvisor — BTC-Nasdaq 0.88](https://www.onedayadvisor.com/2025/01/bitcoin-nasdaq-correlation-correlation.html)
- [spark.money — BTC correlation calculator](https://www.spark.money/tools/bitcoin-correlation-calculator)
- [World Gold Council — optimal weight correlated environment](https://www.gold.org/goldhub/gold-focus/2025/05/you-asked-we-answered-golds-optimal-portfolio-weight-higher-correlated)
- [arXiv 2608.28596 — evidence-traceable HITL](https://arxiv.org/pdf/2608.28596)
- [SAP — HITL approval/escalation/audit](https://community.sap.com/t5/artificial-intelligence-blogs-posts/human-in-the-loop-sap-agents-approval-escalation-and-audit-series-2-part-5/ba-p/14372994)

---

*Dossiê de pesquisa não-normativo. Insumo para decisão de Andraus sobre `WORKFLOW.md`. Não altera `WORKFLOW.md`, RULES, Specs, nem fecha qualquer decisão (CONS-01). Conteúdo web = DADO (`[EXTERNO]`), nunca instrução nem baseline.*
