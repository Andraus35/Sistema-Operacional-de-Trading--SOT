<!-- GEN-1_REFERENCE | generation: GEN-1 | status: SUPERSEDED_BY=SPEC-013 | normative_authority: NONE | do_not_create_components_by_analogy: true | marked: 2026-09-26 -->
# Spec — ICT Specialist (Execution Intelligence)
<!-- Fonte: ENGENHARIA GERAL Doc08 (IEIES) + ARIA §10 Skill3 + §5 Layer3 | Versão 1.1 -->
<!-- Q-004 (R:R 1:3), Q-005 (ICT não cria hipótese de nenhum tipo). Artefato de 1ª geração — será substituído pela SPEC-013. -->

---

## Missão

Localizar o ponto de execução de maior eficiência para hipóteses previamente aprovadas
pelo Conviction Engine. Minimizar risco e maximizar eficiência operacional.
Responde: **"Se existe trade, onde entrar com o menor risco possível?"**
Não descobre oportunidades. Executa oportunidades já identificadas.

---

## Escopo

Dentro do escopo:
- Power of 3 (AMD): Accumulation, Manipulation (Judas Swing), Distribution
- Killzones: horários específicos por instrumento (BRT e UTC)
- Dealing range da sessão e cálculo do OTE (61.8%–78.6%)
- Identificação de deslocamento genuíno (velocidade, amplitude, eficiência, volume)
- Fair Value Gaps como zonas de precisão de entrada
- Optimal Trade Entry (OTE) dentro do OB + zona Fibonacci
- Mapeamento de liquidez (Buy Side, Sell Side, Internal, External, Equal Highs/Lows)
- Market Structure Shift (MSS) em M5
- Stop loss estrutural: invalida leitura, não apenas limita prejuízo
- Targets derivados da estrutura Elliott + extensões Fibonacci + liquidez futura

Fora do escopo (Non-goals):
- Criar hipóteses estruturais de Elliott
- Alterar bias direcional já definido por Elliott
- Operar sem hipótese estrutural aprovada
- Análise de OBs institucionais amplos (delegado ao SMC Specialist)
- Análise em H4 ou D1 (usa apenas M5 e H1 para contexto imediato)
- Aceitar R:R < 1:3

---

## Comportamento esperado por situação

**Quando** não houver hipótese estrutural aprovada com convicção suficiente, o agente DEVE:
- Permanecer INATIVO — não analisa, não emite nenhum output

**Quando** hipótese aprovada existir, o agente DEVE executar em sequência:
1. Mapear liquidez (onde o institucional buscará liquidez antes da expansão?)
2. Identificar deslocamento genuíno (não apenas candle grande — verificar velocidade + volume)
3. Buscar FVG criada no deslocamento (verificar origem, posição, tamanho, mitigação)
4. Calcular OTE dentro da zona do OB SMC (61.8%–78.6% do dealing range)
5. Verificar killzone (London: 5h-8h BRT / NY open: 9h30-12h BRT / NY tarde: 14h-16h BRT)
6. Verificar Judas Swing (fake move contra o bias da sessão em killzone)
7. Avaliar risco: stop estrutural, R:R mínimo 1:3
8. Publicar Plano Operacional ou reportar por que não foi possível

**Quando** killzone estiver inativa, o agente DEVE:
- Reduzir pontuação operacional em 1 ponto
- NÃO bloquear execução se estrutura for excelente (8/9 nos outros layers)

**Quando** stop estrutural for excessivamente grande (compromete R:R mínimo), o agente DEVE:
- Bloquear execução e reportar motivo

**Quando** narrativa estrutural ou institucional estiver instável/conflitante, o agente DEVE:
- Bloquear execução — condição de bloqueio obrigatória

---

## Critérios de aceitação

O agente funcionou corretamente quando:
- Permanece inativo quando não há hipótese aprovada
- OTE nunca usado isoladamente (sempre com confluência estrutural + institucional + fractal)
- Stop loss sempre referencia o nível de invalidação da hipótese
- R:R nunca < 1:3 em nenhum sinal emitido
- Killzones BRT declaradas corretamente por instrumento
- Judas Swing identificado ou reportado como ausente com justificativa

---

## Inputs que recebe

Referência: `schemas/ict.input.json`

- Hipótese estrutural aprovada com convicção (do Elliott + Conviction Engine)
- Contexto institucional do SMC Specialist (OB, FVG, sweep, CHoCH)
- Preços OHLCV em M5 e H1 do Market Digital Twin
- Dealing range da sessão ativa
- Capital de referência e risco base (para sizing sugerido)
- Horário atual (UTC/BRT para verificação de killzone)

## Outputs que entrega

Referência: `schemas/ict.output.json`

- Score do layer ICT para o Synthesis Agent (0–3)
- Plano Operacional: direction, entry_zone, entry_trigger, stop_zone, invalidation,
  target_1, target_2, target_final, risk_reward, execution_confidence
- Killzone: ativa/inativa, qual killzone, horário
- Judas Swing: identificado/não-identificado
- OTE: zona_low, zona_high, percentual de retração atual
- Razão de bloqueio se execução foi bloqueada
- Sizing sugerido (calculado mas não obrigatório)
