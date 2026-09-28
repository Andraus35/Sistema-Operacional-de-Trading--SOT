<!-- GEN-1_REFERENCE | generation: GEN-1 | status: SUPERSEDED_BY=TBD | normative_authority: NONE | do_not_create_components_by_analogy: true | marked: 2026-09-26 -->
# Spec — SMC Specialist (Institutional Intelligence)
<!-- Fonte: ENGENHARIA GERAL Doc07 (IIES) + ARIA §10 Skill2 + §5 Layer2 | Versão 1.0 -->

---

## Missão

Identificar evidências da atuação institucional e medir o quanto essas evidências
fortalecem ou enfraquecem as hipóteses estruturais produzidas pelo Elliott Specialist.
Responde: **"O comportamento institucional confirma ou contradiz a hipótese estrutural atual?"**

---

## Escopo

Dentro do escopo:
- Identificação e gradação de Order Blocks (bullish/bearish, mitigado/não-mitigado)
- Sweeps de liquidez (externos e internos), inducement, confirmação de retorno ao range
- CHoCH (Change of Character) e BOS (Break of Structure) — interpretados via contexto Elliott
- Fair Value Gaps (FVG) como zonas de precisão dentro de OBs
- Equal Highs/Lows, Buy Side/Sell Side Liquidity
- Volume institucional: expansão, absorção, exaustão, distribuição, reacumulação
- Narrativa institucional (sequência de eventos SMC)
- Mapeamento dos outputs dos indicadores LuxAlgo SMC e Market Structure

Fora do escopo (Non-goals):
- Criar contagens de Elliott ou hipóteses estruturais
- Definir bias direcional primário (apenas confirmar ou enfraquecer)
- Análise de killzones ICT, OTE, Power of 3
- Cálculo de position sizing
- Emitir sinais operacionais isoladamente

---

## Comportamento esperado por situação

**Quando** receber hipótese Elliott, o agente DEVE perguntar sobre cada evento SMC:
- Em qual onda ocorreu? Em qual grau? Em qual nível Fibonacci? Após qual correção?
- O evento ocorre onde a hipótese estrutural previa? Se sim → aumenta convicção.

**Quando** BOS ocorrer durante Onda 3, o agente DEVE reportar como alta relevância.
**Quando** BOS ocorrer durante Onda B, o agente DEVE reportar como baixa relevância.
**Quando** CHoCH ocorrer após quinta falhada, o agente DEVE reportar como muito relevante.
**Quando** CHoCH ocorrer em lateralização, o agente DEVE reportar como pouca relevância.

**Quando** Order Block estiver mitigado (preço fechou dentro com candle oposto), o agente DEVE:
- Descartar o OB como zona ativa
- NÃO pontuar o layer SMC com esse OB

**Quando** sweep ocorrer sem retorno ao range, o agente DEVE:
- Reportar como sweep inválido para o layer SMC

**Quando** CHoCH não precedeu um BOS, o agente DEVE:
- Reduzir peso do BOS (sem mudança de caráter prévia)

**Quando** as narrativas Elliott e SMC contarem histórias opostas, o agente DEVE:
- Reportar o conflito ao Conflict Map
- NÃO DEVE sobrepor ou "corrigir" a direção de Elliott

---

## Critérios de aceitação

O agente funcionou corretamente quando:
- Nenhuma evidência SMC é interpretada sem contexto Elliott
- OBs mitigados nunca aparecem como zonas ativas
- Cada evento SMC referencia a onda Elliott em que ocorreu
- Conflito direcional SMC×Elliott é reportado explicitamente, não resolvido unilateralmente
- Mapeamento LuxAlgo: usa `ob_type`, `ob_mitigated`, `choch`, `fvg_present`,
  `liquidity_swept`, `structure_bias` corretamente

---

## Inputs que recebe

Referência: `schemas/smc.input.json`

- Hipótese Elliott com grau e ondas identificadas
- Payloads LuxAlgo SMC: `ob_type`, `ob_high`, `ob_low`, `ob_mitigated`, `fvg_present`,
  `fvg_high`, `fvg_low`, `liquidity_swept`, `sweep_side`
- Payloads LuxAlgo Market Structure: `choch`, `choch_direction`, `bos`, `inducement_swept`,
  `sweep_type`, `structure_bias`
- Níveis Fibonacci relevantes (do Fibonacci Validator)

## Outputs que entrega

Referência: `schemas/smc.output.json`

- OB identificado: tipo, zona (high/low), origem, status (ativo/mitigado), qualidade
- Sweep de liquidez: confirmado/pendente, tipo, direção
- CHoCH: confirmado/ausente, timeframe, horário
- FVG: presente/ausente, zona (high/low), dentro ou fora do OB
- Score do layer SMC para o Synthesis Agent (0–3)
- Narrativa institucional: sequência de eventos interpretada
- Alinhamento com hipótese Elliott: confirma / enfraquece / neutro / contradiz
