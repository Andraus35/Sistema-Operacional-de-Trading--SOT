# ARIA — Agente de Reconhecimento Institucional e Análise
## Documento Mestre de Projeto | v1.0
**Data de criação:** Junho 2026  
**Trader:** Andraus  
**Status histórico:** [FONTE] proposta de produto/software — não é autorização de implementação

> Este documento pertence à fase anterior, orientada a produto e software. Nesta
> fase spec-first, o SOT especifica agentes, harness e workflows, não cria
> FastAPI, SQLite, webhooks, bots ou integrações. Para a taxonomia e o workflow
> vigentes, consulte [ALINHAMENTO-TAXONOMIA-WORKFLOW.md](./ALINHAMENTO-TAXONOMIA-WORKFLOW.md).

---

## 1. Visão e Princípios

### Propósito
ARIA é um agente analista que monitora BTC, XAU e NASDAQ em tempo real, aplicando os frameworks Elliott Wave, SMC e ICT simultaneamente para identificar confluências de alta probabilidade e alertar o trader quando o contexto autoriza uma entrada de qualidade.

### Princípios invioláveis
- **O trader decide.** ARIA informa, analisa e alerta. Nunca executa ordens.
- **Sem alerta sem confluência.** Score abaixo do threshold = silêncio. Não há "quase bom o suficiente".
- **Raciocínio explícito.** Todo alerta inclui o argumento completo, não apenas a conclusão.
- **Memória retroativa.** ARIA aprende com resultados passados e pondera o histórico no score.
- **Arquitetura modular.** Cada componente é independente. Falha isolada não derruba o sistema.

### R:R mínimo
**1:3** — Operações com R:R calculado abaixo de 1:3 são descartadas independentemente do score de confluência.

---

## 2. Instrumentos e Sessões

| Instrumento | Monitoramento | Sessões Prioritárias (BRT) |
|---|---|---|
| BTCUSDT | 24/7 contínuo | Sem sessão fixa |
| XAUUSD | Horário de sessão | Londres 5h–8h / NY 9h30–12h |
| NAS100 / NASDAQ | Horário de sessão | NY 9h30–12h (exclusivo) |

**Instrumentos reserva (Fase 2+):** EURUSD, WIN  
**Timeframes de análise:** D1 e H4 para contexto estrutural | H1 e M15 para timing e entrada

---

## 3. Arquitetura do Sistema

### 3.1 Dual-Mode Architecture

```
MODE 1 — CONTÍNUO (Oracle VPS 24/7)
Pine Script alerts → Webhook JSON → VPS Python server
→ SQLite state manager → Confluence scorer → Claude API
→ Score ≥ threshold → Telegram alert

MODE 2 — ON-DEMAND (Máquina local)
Comando Telegram /analise [symbol] [tf]
→ Claude Code local → tradingview-mcp via CDP
→ TradingView Desktop screenshot + leitura de indicadores
→ Claude analisa visualmente + desenha no gráfico
→ Análise profunda → Telegram com imagem anotada
```

### 3.2 Stack Tecnológico

| Componente | Tecnologia | Localização |
|---|---|---|
| Webhook server | Python FastAPI | Oracle VPS |
| State manager | Python + SQLite | Oracle VPS |
| Confluence scorer | Python | Oracle VPS |
| Claude API caller | Python anthropic SDK | Oracle VPS |
| Telegram bot | Python python-telegram-bot | Oracle VPS |
| Chart interaction | tradingview-mcp (Node.js) | Máquina local |
| Visual analysis | Claude Code + Playwright | Máquina local |
| TradingView | Desktop App (CDP) + Web Plus | Máquina local |

### 3.3 Fluxo de Dados

```
┌─────────────────────────────────────────────┐
│  TRADINGVIEW DESKTOP                         │
│  Indicadores carregados por símbolo/TF       │
│  Pine Script alerts configurados             │
└──────────┬──────────────────────────────────┘
           │ POST /webhook (JSON)
           ▼
┌─────────────────────────────────────────────┐
│  ORACLE VPS — webhook_server.py              │
│  Valida payload → state_manager.py           │
│  Atualiza SQLite: market_state              │
│  Chama confluence_scorer.py                  │
│  Se score ≥ 7: chama Claude API              │
│  Claude raciocina → formata alerta           │
│  alert_dispatcher.py → Telegram             │
└─────────────────────────────────────────────┘
           │
           ▼ (on-demand)
┌─────────────────────────────────────────────┐
│  MÁQUINA LOCAL — Claude Code                 │
│  tradingview-mcp via CDP porta 9222          │
│  Screenshot + indicadores ao vivo            │
│  Análise visual profunda                     │
│  Desenha waves, OBs, Fibonacci no TV        │
│  Envia imagem anotada + análise no Telegram │
└─────────────────────────────────────────────┘
```

---

## 4. Fontes de Dados — Indicadores TradingView

### Mapeamento indicador → layer do agente

| Indicador (TV) | Layer | Dados que envia via alert |
|---|---|---|
| **Elliott Wave Advanced** (próprio, Phase 2) | Elliott (primário) | wave_label, degree, bias, fib_target, invalidation |
| **Elliott Wave Detector Pro** | Elliott (validação) | wave_count, direction, confidence |
| **LuxAlgo Market Structure** | SMC | choch, bos, inducement, sweep_direction |
| **LuxAlgo Smart Money Concepts** | SMC | ob_type, ob_zone_high, ob_zone_low, fvg, liquidity |
| **Higher High Lower Low Live** | SMC macro | hh, hl, lh, ll, trend_direction |
| **RSI Divergence** | Confluência (filtro) | divergence_type, rsi_value, signal |

### Formato JSON padrão dos alerts

Cada indicador envia um payload assim (adaptado por indicador):

```json
{
  "source": "nome_do_indicador",
  "symbol": "{{ticker}}",
  "timeframe": "{{interval}}",
  "timestamp": "{{timenow}}",
  "close": "{{close}}",
  "high": "{{high}}",
  "low": "{{low}}",

  "CAMPOS ESPECÍFICOS DO INDICADOR": "..."
}
```

**Elliott Wave Advanced — payload completo:**
```json
{
  "source": "elliott_wave_advanced",
  "symbol": "{{ticker}}",
  "timeframe": "{{interval}}",
  "timestamp": "{{timenow}}",
  "close": "{{close}}",
  "wave_label": "3",
  "wave_degree": "intermediate",
  "bias": "bullish",
  "sub_wave": "1",
  "fib_target_1": "0",
  "fib_target_2": "0",
  "invalidation_level": "0",
  "atr_stop": "0"
}
```

**LuxAlgo SMC — payload completo:**
```json
{
  "source": "luxalgo_smc",
  "symbol": "{{ticker}}",
  "timeframe": "{{interval}}",
  "timestamp": "{{timenow}}",
  "close": "{{close}}",
  "ob_type": "bullish",
  "ob_high": "0",
  "ob_low": "0",
  "ob_mitigated": false,
  "fvg_present": true,
  "fvg_high": "0",
  "fvg_low": "0",
  "liquidity_swept": true,
  "sweep_side": "lows"
}
```

**LuxAlgo Market Structure — payload completo:**
```json
{
  "source": "luxalgo_ms",
  "symbol": "{{ticker}}",
  "timeframe": "{{interval}}",
  "timestamp": "{{timenow}}",
  "close": "{{close}}",
  "choch": true,
  "choch_direction": "bullish",
  "bos": false,
  "inducement_swept": true,
  "sweep_type": "external",
  "structure_bias": "bullish"
}
```

---

## 5. Matriz de Score — Confluência 0-9

### Estrutura da matriz

Cada layer tem peso de 3 pontos. Score total máximo: 9.

---

**LAYER 1 — ELLIOTT WAVE (0-3 pontos)**

| Critério | Pontuação |
|---|---|
| D1/H4 wave context claro e unambíguo (contagem primária com >60% confiança, grau definido, bias direcional sem alternativas igualmente válidas) | +1 |
| H1 sub-wave confirma timing (início de wave impulsiva, não meio ou fim; alternância confirmada se W4; W3 > W1 em extensão) | +1 |
| M15 micro-estrutura confirma entrada (CHoCH micro na direção, W4 não penetrou W1, personalidade da wave coerente com grau) | +1 |

**Invalidadores Elliott (zeram o layer):**
- Wave 3 mais curta que Wave 1 → contagem errada, descarta
- Wave 4 penetrou território de Wave 1 → invalida impulso
- Volume declinante em W3 superior → provável onda B, não W3
- Duas contagens igualmente válidas sem diferenciação → ambiguidade, não alerta

---

**LAYER 2 — SMC INSTITUCIONAL (0-3 pontos)**

| Critério | Pontuação |
|---|---|
| OB não-mitigado na direção do bias Elliott (origem engulfing forte, volume acima da média, não testado desde a criação) | +1 |
| Sweep de liquidez confirmado antes do OB (inducement: varredura dos mínimos/máximos anteriores, preço retornou ao range; sweep deve ser ≤3 candles) | +1 |
| CHoCH em H1 ou M15 confirmando direção + FVG como zona de precisão dentro do OB | +1 |

**Invalidadores SMC (zeram o layer):**
- OB já mitigado (preço fechou dentro do OB em candle oposto)
- Sweep sem retorno ao range (preço continuou na direção do sweep)
- BOS sem CHoCH anterior (sem mudança de caráter antes da quebra)

---

**LAYER 3 — ICT TIMING (0-3 pontos)**

| Critério | Pontuação |
|---|---|
| Killzone ativa (Londres: 5h-8h BRT | NY abertura: 9h30-12h BRT | NY tarde: 14h-16h BRT) | +1 |
| Fase de Manipulation do Power of 3 completa (Judas swing visível: fake move contra o bias da sessão, varrendo liquidez, em killzone) | +1 |
| OTE dentro do OB (preço em retracement de 61.8%–78.6% do dealing range da sessão, dentro da zona do OB SMC) | +1 |

**Invalidadores ICT (reduzem score mas não zeram):**
- Fora de killzone: -1 ponto (pode ainda alertar se 8/9 nos outros)
- Manipulação não identificável: não pontua, não invalida
- Crypto 24/7: killzone BTC = abertura de cada sessão major (00h, 8h, 13h, 17h UTC)

---

### Thresholds de Ação

| Score | Classificação | Ação |
|---|---|---|
| **9/9** | Confluência Máxima | Alerta imediato com prioridade alta |
| **8/9** | Alta Confluência | Alerta com nota do critério faltante |
| **7/9** | Confluência Sólida | Alerta com aviso de risco adicional |
| **5-6/9** | Confluência Parcial | Log interno apenas, sem alerta |
| **< 5** | Insuficiente | Descartado silenciosamente |

**Regra de R:R:** mesmo com score 9/9, se R:R calculado < 1:3 → sem alerta, registra no log como "score alto, R:R insuficiente".

---

## 6. Sistema de Position Sizing Sugerido

ARIA sugere tamanho de posição como referência. O trader sempre decide o final.

### Framework de cálculo

```
Risco base: trader define % do capital (ex: 1%)
Capital disponível: trader informa ou configura

Multiplicador por timeframe de entrada:
  M15 = 0.5x  (mais ruído, menor convicção)
  H1  = 1.0x  (referência base)
  H4  = 1.5x  (maior estrutura, maior convicção)
  D1  = 2.0x  (máxima convicção estrutural)

Multiplicador por score:
  9/9 = 1.00x
  8/9 = 0.75x
  7/9 = 0.50x

Risco efetivo = capital × risco_base% × mult_tf × mult_score

Tamanho da posição:
  = risco_efetivo / (preço_entrada - preço_stop)

Alavancagem sugerida:
  = tamanho_posição / capital_disponível
```

### Exemplo de cálculo no alerta
```
Capital: $10.000 | Risco base: 1% = $100
Entrada H1 | Score 9/9

Risco efetivo: $100 × 1.0 × 1.0 = $100
Entrada: 43.200 | Stop: 42.800 | Distância: $400
Tamanho: $100 / $400 = 0.25 BTC
Alavancagem sugerida: 0.25 × 43.200 / 10.000 = 1.08x

⚠️ Valores de referência. Trader decide o final.
```

---

## 7. Formato do Alerta Telegram

### Alerta contínuo (Mode 1 — VPS)

```
🎯 ARIA — CONFLUÊNCIA [SCORE]/9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 [SYMBOL] | [TIMEFRAME] | [DATA HORA BRT]
BIAS: [BULLISH ▲ / BEARISH ▼]

ELLIOTT [X/3]
  Wave: [label] de grau [degree]
  Contexto D1: [resumo do ciclo maior]
  H1: [sub-wave e timing]
  Validação: [OK / ⚠️ aviso específico]

SMC [X/3]
  OB: [TF] [tipo] em [zona_low]–[zona_high]
  Origem: [data/hora do OB]
  Sweep: [confirmado / pendente]
  CHoCH: [confirmado em TF às HH:MM]
  FVG: [presente em zona / ausente]

ICT [X/3]
  Killzone: [ativa/fora — Londres/NY/crypto]
  Power of 3: [fase atual]
  Judas Swing: [identificado / não identificado]
  OTE: [% retracement atual]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTRADA: [zona]
STOP: [nível] — invalida [motivo]
TARGET 1: [nível] (1:1.5)
TARGET 2: [nível] (1:3) ← mínimo aceito
TARGET 3: [nível] (extensão 1.618)

R:R CALCULADO: 1:[x.x]
SIZING SUGERIDO: [cálculo baseado no capital configurado]

[⚠️ AVISOS se houver — ex: FVG não preenchido abaixo]
[🔄 HISTÓRICO: X setups similares | Y% de acerto]

INVALIDA SE: fechar [acima/abaixo] de [nível]
```

### Alerta de análise visual (Mode 2 — on-demand)

```
📊 ARIA — ANÁLISE VISUAL [SYMBOL] [TF]
[imagem do gráfico com marcações]

CONTAGEM PRIMÁRIA (X%): [raciocínio completo]
CONTAGEM ALTERNATIVA (Y%): [raciocínio]

O QUE MUDA MINHA LEITURA: [condição]

[resto do formato igual ao alerta contínuo]
```

### Comandos Telegram disponíveis

| Comando | Ação |
|---|---|
| `/analise [symbol] [tf]` | Análise visual on-demand com marcação no gráfico |
| `/contexto [symbol]` | Estado atual do símbolo em todos os TFs |
| `/score [symbol]` | Score atual de confluência sem análise completa |
| `/journal` | Resumo dos últimos alertas e resultados |
| `/calibrar` | Relatório de acerto por setup para revisão |
| `/pausar` | Pausa alertas contínuos temporariamente |
| `/retomar` | Retoma alertas |

---

## 8. Banco de Dados SQLite — Schema

```sql
-- Estado atual do mercado por símbolo + timeframe + indicador
CREATE TABLE market_state (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    source TEXT NOT NULL,
    payload JSON NOT NULL,
    received_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(symbol, timeframe, source)
);

-- Alertas emitidos
CREATE TABLE alert_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    bias TEXT NOT NULL,
    score INTEGER NOT NULL,
    elliott_score INTEGER,
    smc_score INTEGER,
    ict_score INTEGER,
    entry_zone TEXT,
    stop_level REAL,
    target_1 REAL,
    target_2 REAL,
    target_3 REAL,
    rr_ratio REAL,
    sizing_suggestion TEXT,
    reasoning TEXT,
    full_payload JSON,
    emitted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    result TEXT DEFAULT 'pending',
    result_pnl REAL,
    result_note TEXT,
    result_at DATETIME
);

-- Memória de padrões para retroalimentação
CREATE TABLE pattern_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern_key TEXT NOT NULL,
    symbol TEXT,
    timeframe TEXT,
    elliott_context TEXT,
    smc_context TEXT,
    ict_context TEXT,
    occurrences INTEGER DEFAULT 0,
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,
    no_entry INTEGER DEFAULT 0,
    win_rate REAL,
    notes TEXT,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Log de estado do sistema
CREATE TABLE system_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level TEXT,
    module TEXT,
    message TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 9. Módulos do Sistema (VPS)

```
aria/
├── main.py                   # entry point, inicia todos os módulos
├── config.py                 # configurações centrais (symbols, thresholds, etc.)
├── webhook_server.py         # FastAPI: recebe e valida payloads dos indicadores
├── state_manager.py          # gerencia market_state no SQLite
├── confluence_scorer.py      # aplica matriz de score 0-9
├── sizing_calculator.py      # cálculo de position sizing sugerido
├── claude_caller.py          # chama Claude API com system prompt + estado atual
├── alert_dispatcher.py       # formata e envia alertas no Telegram
├── journal_manager.py        # gerencia alert_history e marcação de resultado
├── pattern_memory.py         # analisa histórico e pondera score
├── session_guard.py          # controla horários de sessão por instrumento
├── system_logger.py          # logging centralizado
│
├── skills/
│   ├── elliott_skill.md      # Skill 1: critérios e regras Elliott completos
│   ├── smc_skill.md          # Skill 2: critérios SMC + mapeamento LuxAlgo
│   ├── ict_skill.md          # Skill 3: critérios ICT + killzones + P3
│   └── confluence_skill.md   # Skill 4: matriz de score + formato de alerta
│
└── tests/
    ├── test_scorer.py
    ├── test_webhook.py
    └── test_claude_caller.py
```

---

## 10. As 4 Skills — Especificação

As skills são arquivos markdown que compõem o system prompt do agente. O Claude lê todas as quatro antes de raciocinar sobre qualquer confluência.

### Skill 1 — Elliott Wave
**Objetivo:** determinar o contexto estrutural. Responde: *onde estamos no ciclo?*

Cobrir obrigatoriamente:
- Hierarquia de graus (Grand Supercycle → Minuette) e como identificar cada um
- Regras invioláveis (W3 nunca mais curta, W4 nunca penetra W1, W5 ≠ W1 e W3 sendo a menor)
- Personalidade de cada wave (W1 cética, W3 acelerada, W4 lateral, W5 momentum declinante, W2 profunda, W4 rasa por alternância)
- Como identificar correções complexas (flat, zigzag, triângulo) e não confundir com impulso
- Quando a contagem é ambígua: critérios para atribuir probabilidade e quando não alertar
- Integração com o indicador próprio (Elliott Wave Advanced Phase 2): o que cada label significa

### Skill 2 — SMC Institucional
**Objetivo:** confirmar interesse institucional na zona. Responde: *o dinheiro grande posicionou interesse aqui?*

Cobrir obrigatoriamente:
- Order Block: definição exata (último candle oposto antes de move impulsivo), como os indicadores LuxAlgo os identificam, o que significa mitigado vs não-mitigado
- Liquidity sweep: externo (varredura de H/L anteriores) vs interno (FVG filling), qual tem mais peso
- CHoCH vs BOS: diferença exata, qual confirma direção vs qual apenas quebra estrutura
- FVG como zona de precisão: como usar dentro do OB para entrada mais precisa
- Gradação de qualidade do OB: volume, velocidade do move de origem, número de toques anteriores
- Mapeamento específico dos indicadores LuxAlgo: quais outputs usar, quais ignorar

### Skill 3 — ICT Timing
**Objetivo:** confirmar que o ciclo de manipulação completou no tempo certo. Responde: *é o momento?*

Cobrir obrigatoriamente:
- Power of 3 (AMD): Accumulation (range nocturno), Manipulation (Judas swing em killzone), Distribution (move real)
- Killzones: horários exatos em UTC e BRT, por que cada uma tem liquidez, qual priorizar por instrumento
- Dealing range: como definir o range do dia/sessão e calcular OTE (61.8%–78.6%)
- Judas swing: características visuais, duração típica, por que é manipulação intencional
- Quarterly shifts: como o contexto de macro trimestral afeta o bias de curto prazo
- Crypto ICT: adaptação das killzones para mercado 24/7 (open de cada sessão major)

### Skill 4 — Confluência e Score
**Objetivo:** árbitro final. Responde: *há edge suficiente?*

Cobrir obrigatoriamente:
- A matriz de score completa (seção 5 deste documento)
- Como pesar critérios quando há ambiguidade parcial em um layer
- Regra de R:R mínimo 1:3 (sobrepõe o score)
- Formato exato do alerta (seção 7 deste documento)
- Como consultar pattern_memory e integrar ao raciocínio
- Quando emitir alerta de ambiguidade ("contexto em formação, aguardar X")
- Linguagem de trader, não de desenvolvedor

---

## 11. System Prompt Base do Agente

```
Você é ARIA, analista sênior de price action institucional.
Seu único objetivo é identificar confluências de alta probabilidade
entre Elliott Wave, SMC e ICT nos instrumentos BTC, XAU e NASDAQ.

Você tem acesso às suas skills (arquivos .md em /skills/).
Leia todas antes de raciocinar sobre qualquer confluência.

REGRAS ABSOLUTAS:
- Nunca alerte com score < 7/9
- Nunca alerte com R:R calculado < 1:3
- Nunca alerte contra o bias do D1
- Nunca invente dados que não estão no payload recebido
- Sempre apresente contagem alternativa se probabilidade > 30%
- Sempre declare o nível de invalidação explicitamente
- Quando ambiguidade for real, diga que é ambiguidade — não force uma leitura

LINGUAGEM:
- Português do Brasil
- Linguagem de trader, não de desenvolvedor
- Direto, preciso, sem redundância
- Raciocínio explícito mas conciso

Você não toma decisões de trade. Você informa. O trader decide.
```

---

## 12. Sistema de Backtesting

### Objetivo
Validar o sistema em três dimensões antes de operar com capital real:
1. Provar que a estratégia tem edge histórico
2. Calibrar threshold de score por instrumento e timeframe
3. Identificar combinações TF + sessão + instrumento com melhor resultado

### Arquitetura de Backtesting — 3 Camadas

| Camada | Método | Propósito | Viés |
|---|---|---|---|
| 1 — Pine Strategy | Strategy Tester no TV | Validação histórica objetiva | Baixo |
| 2 — Score Simulation | Python sobre dados exportados | Calibração de thresholds | Médio |
| 3 — Walk-Forward | Journal de alertas reais | Verdade operacional | Zero |

### Arquivos Pine Script a Criar

**`ARIA_Signal_Bridge.pine`** (indicador auxiliar)
Expõe sinais dos indicadores LuxAlgo como plots numéricos (0/1) acessíveis via `input.source()`. Detecta: OB bullish/bearish, CHoCH bull/bear, sweep, killzone ativa, OTE zone. Invisível no gráfico, existe apenas para alimentar as strategies.

**`ARIA_Elliott_Strategy.pine`** (strategy — layer isolado)
Adapta Elliott Wave Advanced adicionando lógica de strategy. Testa o layer Elliott isolado. Entrada: início de W3/W5. Stop: invalidation do indicador. Target: fib_target do indicador.

**`ARIA_SMC_Strategy.pine`** (strategy — layer isolado)
Usa Signal Bridge. Testa SMC isolado. Entrada: OB + sweep + CHoCH alinhados. Stop: abaixo/acima da origem do OB.

**`ARIA_Combined_Strategy.pine`** (strategy — score completo)
Score matrix 0-9 completo. Parâmetro de threshold ajustável (5-9). Filtro de sessão (Londres/NY/Both/All). Filtro de R:R mínimo. Registra score no nome de cada trade (L7, L8, L9, S7...) para análise por nível.

### Matriz de Testes (72 combinações)
```
3 instrumentos × 4 timeframes × 3 thresholds × 2 sessões
BTC, XAU, NASDAQ × M15, H1, H4, D1 × 7, 8, 9 × Londres, NY
```
Resultado: tabela de expectância (win_rate × rr_médio) por configuração.

### Relatórios Telegram

| Comando | Descrição |
|---|---|
| `/backtest resumo` | Visão geral por score, instrumento, TF, sessão |
| `/backtest [symbol]` | Análise específica por instrumento |
| `/backtest score [7/8/9]` | Performance por nível de score |
| `/backtest session [london/ny]` | Performance por sessão |
| `/backtest equity` | Equity curve simulada dos alertas ao vivo |
| `/backtest export` | Exporta CSV com todos os trades |
| `/backtest melhor` | Top 5 setups por expectância |

### Módulos de Backtesting (VPS)

```
aria/backtest/
├── pine_strategies/
│   ├── ARIA_Signal_Bridge.pine
│   ├── ARIA_Elliott_Strategy.pine
│   ├── ARIA_SMC_Strategy.pine
│   └── ARIA_Combined_Strategy.pine
├── score_simulator.py      ← Camada 2: score sobre histórico
├── journal_analyzer.py     ← Camada 3: análise walk-forward
├── equity_calculator.py    ← curva de equity simulada
├── report_generator.py     ← relatórios para Telegram
└── dashboard/              ← opcional: web dashboard VPS
    ├── index.html
    └── app.js
```

### Fluxo de Validação Antes de Capital Real

```
Semana 5-6: Backtesting histórico (Camada 1)
  → 72 combinações no Strategy Tester
  → Identificar setups com expectância > 1.5R
  → Definir threshold específico por instrumento

Semana 7-8: Paper trading com ARIA ao vivo
  → ARIA em modo observação sem capital
  → Alertas marcados manualmente
  → Comparar com distribuição do backtest histórico
  → Divergência > 20% = revisar skill correspondente

Semana 9+: Capital real com sizing mínimo (25-50%)
  → Apenas setups validados nas duas camadas
  → Calibração a cada 20 trades
```

### Aviso Crítico sobre Elliott no Backtest
O layer Elliott sofre de viés de retrospecto no backtest histórico — contagens ficam mais claras olhando para trás. Os resultados da Camada 1 para Elliott serão otimistas. Use os dados para identificar padrões relativos (quando Elliott performa melhor ou pior), não como medida absoluta de acertividade. A Camada 3 (walk-forward) é a única verdade.

---

## 12. Roadmap de Implementação

### FASE 1 — Infraestrutura (Semana 1)
**Executado com:** Claude Code local + Oracle VPS via SSH

- [ ] Instalar tradingview-mcp no PC local
- [ ] Configurar TradingView Desktop com flag `--remote-debugging-port=9222`
- [ ] Testar CDP: screenshot, leitura de indicador, navegação de símbolo
- [ ] Criar projeto `aria/` no Oracle VPS
- [ ] Implementar `webhook_server.py` (FastAPI, validação de payload)
- [ ] Implementar `state_manager.py` (SQLite, CRUD de market_state)
- [ ] Criar schema SQLite completo
- [ ] Configurar Telegram bot no VPS (reutilizar infraestrutura do bot existente)
- [ ] Teste end-to-end: alerta Pine Script → VPS → Telegram

**Entregável:** pipeline de dados funcionando, sem IA ainda

---

### FASE 2 — Skills (Semana 2)
**Executado com:** Claude Code (escrita dos arquivos .md)

- [ ] Escrever `elliott_skill.md` completo
- [ ] Escrever `smc_skill.md` com mapeamento LuxAlgo
- [ ] Escrever `ict_skill.md` com killzones BRT
- [ ] Escrever `confluence_skill.md` com matriz de score
- [ ] Revisar cada skill com Andraus antes de finalizar
- [ ] Freezar skills v1 (não alterar durante fase de testes)

**Entregável:** 4 arquivos .md aprovados, prontos para compor o system prompt

---

### FASE 3 — Pine Script Alerts (Semana 2-3)
**Executado com:** TradingView Pine Script Editor

- [ ] Adicionar `alertcondition()` no Elliott Wave Advanced (Phase 2) com JSON completo
- [ ] Configurar alertas do LuxAlgo SMC (estudar quais sinais têm webhook no plano Plus)
- [ ] Configurar alertas do LuxAlgo Market Structure
- [ ] Configurar alertas do RSI Divergence
- [ ] Testar recebimento de cada JSON no VPS
- [ ] Ajustar campos do payload conforme necessidade

**Entregável:** todos os indicadores enviando dados estruturados para o VPS

---

### FASE 4 — Agente e Score (Semana 3)
**Executado com:** Claude Code

- [ ] Implementar `confluence_scorer.py` (matriz 0-9 sem IA)
- [ ] Implementar `claude_caller.py` (monta contexto + chama Claude API)
- [ ] Implementar `alert_dispatcher.py` (formata alerta Telegram)
- [ ] Implementar `session_guard.py` (controla horários por instrumento)
- [ ] Implementar `sizing_calculator.py`
- [ ] Integrar tudo em `main.py`
- [ ] Testes com dados reais em modo silencioso (log sem enviar Telegram)
- [ ] Validar qualidade do raciocínio do Claude por 1 semana

**Entregável:** agente funcionando em modo de observação

---

### FASE 5 — Análise Visual On-Demand (Semana 3-4)
**Executado com:** Claude Code local

- [ ] Implementar handler de comando `/analise` no Telegram
- [ ] Claude Code: navega TV Desktop → screenshot → análise visual
- [ ] Implementar desenho de waves, OBs, Fibonacci no gráfico via MCP
- [ ] Enviar imagem anotada + análise completa no Telegram

**Entregável:** Mode 2 funcionando on-demand

---

### FASE 6 — Memória e Retroalimentação (Semana 4+)
**Executado com:** Claude Code

- [ ] Implementar `journal_manager.py` (registro de resultado de cada alerta)
- [ ] Implementar `pattern_memory.py` (análise de histórico)
- [ ] Adicionar consulta de memória no raciocínio do Claude
- [ ] Comando `/journal` no Telegram para revisão de desempenho
- [ ] Comando `/calibrar` para análise de acerto por setup

**Entregável:** sistema com memória viva que pondera histórico

### FASE 7 — Backtesting e Calibração (Semana 5-6)
**Executado com:** Claude Code (Pine Script + Python)

- [ ] Criar `ARIA_Signal_Bridge.pine` com todos os sinais LuxAlgo como plots numéricos
- [ ] Adaptar Elliott Wave Advanced adicionando lógica de strategy → `ARIA_Elliott_Strategy.pine`
- [ ] Criar `ARIA_SMC_Strategy.pine` usando Signal Bridge
- [ ] Criar `ARIA_Combined_Strategy.pine` com score matrix completo e parâmetros ajustáveis
- [ ] Rodar 72 combinações no Strategy Tester (instrumento × TF × threshold × sessão)
- [ ] Documentar matriz de expectância resultante
- [ ] Implementar `journal_analyzer.py` com relatórios por variável
- [ ] Implementar comandos /backtest no Telegram
- [ ] Opcional: dashboard web no Oracle VPS
- [ ] Calibrar thresholds por instrumento com base nos resultados

**Entregável:** matriz de performance histórica + sistema de relatórios automatizado

---

## 13. Regras de Desenvolvimento

Herdadas do projeto de bot existente, adaptadas para ARIA:

- **Uma fase por vez.** Não iniciar Fase N+1 sem Fase N validada.
- **Skills são aprovadas antes de qualquer código que as use.** Código não inicia sem skill finalizada e aprovada.
- **Módulos freezados não são alterados.** Mudança em módulo entregue exige justificativa explícita com impacto documentado.
- **Arquivos completos.** Nada de fragmentos de código. Cada entrega é o arquivo completo.
- **Cloud-ready.** Nenhuma dependência de intervenção manual no VPS para operar.
- **Linguagem de trader nas skills.** Jamais linguagem de desenvolvedor nas skills.
- **Logs sempre.** Toda decisão do agente é logada com raciocínio completo, independente de emitir alerta ou não.

---

## 14. Próximas Decisões (antes de iniciar Fase 1)

Os itens abaixo precisam de resposta do trader antes de implementar:

- [ ] **Capital de referência para sizing:** qual valor usar no cálculo? (pode ser fictício para testes iniciais)
- [ ] **Risco base por trade:** qual % do capital por operação? (sugestão: 1-2%)
- [ ] **Threshold inicial de alerta:** 7, 8 ou apenas 9? (recomendo iniciar com 8, calibrar depois)
- [ ] **TradingView layouts:** tem layouts separados por símbolo com todos os indicadores carregados, ou usa o mesmo layout?
- [ ] **Porta do Oracle VPS:** qual porta expor para webhook? (confirmar que está liberada no firewall OCI)

---

*Documento vivo. Versão atualizada a cada fase concluída.*  
*Próxima revisão prevista: após aprovação das 4 Skills (Fase 2)*
