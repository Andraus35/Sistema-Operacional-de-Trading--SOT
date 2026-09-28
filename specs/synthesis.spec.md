<!-- GEN-1_REFERENCE | generation: GEN-1 | status: SUPERSEDED_BY=SPEC-014 | normative_authority: NONE | do_not_create_components_by_analogy: true | marked: 2026-09-26 -->
# Spec — Synthesis Agent (Árbitro Final)
<!-- Fonte: ENGENHARIA GERAL Doc06 (CES) + Doc09 (MOES) + ARIA §10 Skill4 + §5 + §7 | Versão 1.1 -->
<!-- Q-007: Conviction Engine é SEPARADO (Fusion→Conviction→Synthesis) — o cálculo de convicção migra p/ SPEC-003; aqui permanece a arbitragem. Q-008: Conviction Vector = 8 dimensões. Q-004: R:R 1:3. Q-002: 70%/7-9 = Fase Piloto. Artefato de 1ª geração — será substituído pela SPEC-014. -->

---

## Missão

Receber os outputs de todos os especialistas, calcular a convicção global multidimensional,
arbitrar conflitos entre metodologias e emitir o sinal operacional final com formato
padronizado. Árbitro — não analista.
Responde: **"Há edge suficiente? Qual é a decisão?"**

---

## Escopo

Dentro do escopo:
- Agregação das convicções por dimensão — **8 dimensões (Q-008)**: estrutural, geométrica, fractal, institucional,
  operacional, temporal, volume, histórica
- Arbitragem de conflitos Elliott×SMC, Elliott×Fibonacci
- Aplicação de regras de convicção mínima (≥ 70% — Fase Piloto, recalibrável, Q-002)
- Aplicação de regra de R:R mínimo (≥ 1:3 — Q-004)
- Verificação de pontuação mínima por layer (ICT ≥ 1/3 obrigatório)
- Cálculo de position sizing sugerido
- Formatação do alerta Telegram (Mode 1 contínuo + Mode 2 on-demand)
- Geração do Trading Mission Package (TMP)
- Consulta ao pattern_memory (histórico de setups similares)

Fora do escopo (Non-goals):
- Análise direta de mercado (Elliott, SMC, Fibonacci, ICT)
- Alterar outputs dos especialistas
- Emitir sinal sem convicção ≥ 70% (limiar de Fase Piloto — Q-002)
- Emitir sinal com conflito direcional aberto Elliott×SMC

---

## Comportamento esperado por situação

**Quando** receber todos os 4 outputs dos especialistas, o agente DEVE:
1. Verificar se há conflito direcional Elliott×SMC → se sim, output = NEUTRO
2. Calcular score agregado: Elliott (0–3) + SMC (0–3) + ICT (0–3) = 0–9
3. Verificar pontuação mínima ICT (≥ 1/3 obrigatório)
4. Calcular convicção multidimensional (não soma — ponderação por independência)
5. Verificar convicção global ≥ 70% (Fase Piloto — Q-002)
6. Verificar R:R calculado ≥ 1:3 (Q-004)
7. Emitir sinal ou reportar motivo para não emissão

**Quando** score ≥ 7/9 + R:R ≥ 1:3 + convicção ≥ 70% + sem conflito (limiares de score/convicção = Fase Piloto — Q-002):
- Emitir sinal COMPRA ou VENDA com alerta formatado

**Quando** score 5–6/9:
- Log interno apenas — sem alerta

**Quando** score < 5/9:
- Descartar silenciosamente

**Quando** R:R calculado < 1:3 (mesmo com score 9/9):
- SEM sinal. Registra no log como "score alto, R:R insuficiente"

**Quando** ICT score = 0/3:
- SEM sinal operacional, independente da soma total

**Quando** ambiguidade Elliott > 30% (duas contagens quase igualmente válidas):
- DEVE apresentar contagem alternativa no alerta
- NÃO DEVE suprimir a alternativa mesmo com score alto

---

## Critérios de aceitação

O agente funcionou corretamente quando:
- Nenhum sinal emitido com convicção < 70%
- Nenhum sinal emitido com R:R < 1:3
- Nenhum sinal emitido com conflito direcional Elliott×SMC
- Todo sinal inclui: bias, scores, entry_zone, stop, targets, R:R, invalidador, sizing
- Todo sinal declara o nível de invalidação explicitamente
- Alternativa apresentada quando probabilidade > 30%
- Score e Conviction Vector presentes em todo output

---

## Inputs que recebe

Referência: `schemas/synthesis.input.json`

- Output do Elliott Specialist (hipótese, bias, convicção, score 0–3, invalidador)
- Output do Fibonacci Validator (confirmação, confluência, OTE, convicção geométrica)
- Output do SMC Specialist (OB, sweep, CHoCH, FVG, score 0–3, alinhamento)
- Output do ICT Specialist (plano operacional, score 0–3, killzone, R:R)
- Capital de referência e risco base
- Histórico de pattern_memory (acerto por setup similar)

## Outputs que entrega

Referência: `schemas/synthesis.output.json`

- sinal: COMPRA / VENDA / NEUTRO / AGUARDAR_SETUP
- convicção_global: 0–100%
- score_total: 0–9
- conviction_vector: {estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica} (8 dimensões — Q-008)
- entry_zone: low, high
- stop_level: preço + motivo
- target_1: preço (1:1.5)
- target_2: preço (1:3)
- target_3: preço (extensão 1.618)
- risk_reward: calculado
- sizing_sugerido: tamanho + alavancagem
- invalidação_explícita: condição que invalida o sinal
- contagem_alternativa: se probabilidade > 30%
- razão_sem_sinal: se sinal = NEUTRO ou AGUARDAR_SETUP
- alerta_telegram: string formatada completa
