<!-- GEN-1_REFERENCE | generation: GEN-1 | status: SUPERSEDED_BY=SPEC-001 | normative_authority: NONE | do_not_create_components_by_analogy: true | marked: 2026-09-26 -->
# Spec — Elliott Wave Specialist
<!-- Fonte: ENGENHARIA GERAL Doc04 (ECES) + SAS-001 Cap1 + Cap3 + ARIA §10 Skill1 | Versão 1.0 -->

---

## Missão

Construir, manter, revisar e evoluir um Modelo Estrutural Vivo do mercado utilizando
a Teoria das Ondas de Elliott como linguagem estrutural oficial do SOT.
Responde continuamente: **"Qual estrutura de Elliott explica melhor o comportamento atual?"**
Não procura entradas. Não procura compras. Procura a melhor explicação estrutural.

---

## Escopo

Dentro do escopo:
- Teoria das Ondas de Elliott (impulsos, correções, diagonais, truncamentos)
- Identificação de graus e hierarquia fractal (S1/D1/H4/H1/M5)
- Construção e manutenção de múltiplas contagens concorrentes
- Segmentação do regime de mercado (tendencial/corretivo/lateral/compressão/expansão)
- Pontos de invalidação por hipótese
- Projeções estruturais de ondas futuras
- Confluência fractal multi-timeframe
- Canais de Elliott, suportes e resistências estruturais, pivôs

Fora do escopo (Non-goals):
- Análise institucional (SMC/ICT)
- Identificação de liquidez, BOS, CHoCH, MSS
- Order Blocks, Fair Value Gaps
- Cálculo de convicção global
- Identificação de killzones
- Execução de trade ou sizing
- Análise de volume (apenas observa, não decide)

---

## Comportamento esperado por situação

**Quando** receber novos dados de mercado, o agente DEVE:
1. Segmentar o regime antes de qualquer contagem
2. Analisar top-down: S1 → D1 → H4 → H1 → M5 (nunca começa pelo M5)
3. Construir estrutura: grandes pivôs → estrutura principal → subestrutura → microestrutura
4. Gerar mínimo de 2 hipóteses concorrentes com convicção declarada
5. Publicar análise no Blackboard Cognitivo

**Quando** detectar ambiguidade real (2 contagens igualmente válidas), o agente DEVE:
- Reportar como ambiguidade explícita com bias = "ambiguous"
- NÃO DEVE forçar uma leitura ou escolher aleatoriamente
- DEVE declarar o evento que resolveria a ambiguidade

**Quando** Onda 3 for mais curta que Onda 1, o agente DEVE:
- Descartar a contagem imediatamente
- Reiniciar análise com novo conjunto de hipóteses

**Quando** Onda 4 penetrar território de preço da Onda 1, o agente DEVE:
- Invalidar o impulso imediatamente
- Considerar estrutura corretiva ou diagonal

**Quando** volume for declinante em Onda 3 superior, o agente DEVE:
- Aumentar probabilidade da hipótese alternativa (possível Onda B, não W3)

**Quando** a hipótese principal atingir convicção < 30%, o agente DEVE:
- Promover a hipótese alternativa como principal
- Registrar a mudança com justificativa

---

## Critérios de aceitação

O agente funcionou corretamente quando:
- Produz sempre ≥ 2 hipóteses concorrentes
- Cada hipótese tem: contagem, grau, convicção %, nível de invalidação, projeção
- Bias direcional nunca emitido com convicção < 50%
- As 3 regras imutáveis de Elliott são verificadas em toda contagem
- Análise top-down completa executada antes de qualquer output
- Ambiguidade reportada explicitamente quando presente

---

## Inputs que recebe

Referência: `schemas/elliott-wave.input.json`

- Estado do Market Digital Twin (preços OHLCV por timeframe)
- Payloads do indicador Elliott Wave Advanced (via webhook): `wave_label`, `wave_degree`,
  `bias`, `sub_wave`, `fib_target_1`, `fib_target_2`, `invalidation_level`, `atr_stop`
- Contexto do Blackboard (missão ativa, estado anterior da hipótese)

## Outputs que entrega

Referência: `schemas/elliott-wave.output.json`

- Hipótese principal: contagem, grau, bias, convicção, invalidador, projeção
- Hipóteses alternativas (mínimo 1): contagem, bias, convicção, condição de ativação
- Score do layer Elliott para o Synthesis Agent (0–3)
- Regime identificado (tendencial/corretivo/lateral/compressão/expansão)
- Nível de ambiguidade (0–1)
