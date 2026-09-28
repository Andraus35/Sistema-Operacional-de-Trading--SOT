# RAG — Synthesis Agent Knowledge Base
<!-- 12 chunks | Fonte: ENGENHARIA GERAL Doc06 (CES) + Doc09 (MOES) + ARIA §5 §11 + CEE-001 -->
<!-- Correções Andraus 2026-09-14: R:R → 1:3 (Q-004); 70%/7-9 = Fase Piloto (Q-002); Framework 3E → 4Es (Q-009). Conviction Vector já em 8 dimensões (Q-008). -->
<!-- RAG-METADATA (2026-09-26 — Alinhamento Taxonômico):
  rag_status: ACTIVE_PILOT
  authority: ATOMIC-SPEC > RAG (em conflito, ATOMIC-SPEC prevalece — Andraus 2026-09-26)
  score_0_9_status: PILOT — Score 0-9 mantido como filtro paralelo (Andraus 2026-09-26); NÃO substitui Conviction Vector 8D
  conviction_thresholds: ≥70% (Fase Piloto, Q-002); score ≥7/9 (Fase Piloto, Q-002)
  superseded_chunks: [CHUNK-SY-007 ref. score_estrutural ≥60% — SUPERSEDED por Q-002/Q-008; norma vigente = convicção ≥70%]
  do_not_use_if: chunk contém threshold 60% ou 75% → aplicar COR-GPR-002/003 (ver GPR-001-EMENDA-001)
  open_decisions: [J-001 — fórmula/pesos definitivos do Conviction Vector; PILOT até CCM-001]
  last_verified: 2026-09-26
-->

---

## CHUNK-SY-001
---
chunk_id: SY-001
agente: SynthesisAgent
topico: missao_fundamental_arbitro_final
prioridade: critica
quando_consultar: sempre_que_iniciar_sintese
---
**Missão do Synthesis Agent (Árbitro Final)**
O Synthesis Agent é o árbitro final do SOT. Recebe os outputs dos 4 especialistas e produz a decisão operacional definitiva. A pergunta que responde é: "Dados todos os inputs, existe uma oportunidade com qualidade suficiente para operar?"

NÃO faz análise direta de mercado. NÃO verifica dados de preço. NÃO resolve conflitos favorecendo qualquer camada metodológica exceto Elliott. É o integrador — não o analista.

---

## CHUNK-SY-002
---
chunk_id: SY-002
agente: SynthesisAgent
topico: score_matrix_0_9
prioridade: critica
quando_consultar: ao_calcular_score_total
---
**Score Matrix 0-9**
O score total é a soma dos scores dos 3 layers operacionais:

| Layer | Máximo | Contribuição |
|---|---|---|
| Elliott Specialist | 3 pts | Estrutura + regime + fractalidade |
| SMC Specialist | 3 pts | Confirmação institucional |
| ICT Specialist | 3 pts | Condições de execução |
| **Total** | **9 pts** | Soma direta |

**Condição mínima para sinal:** score_total ≥ 7/9 + convicção_global ≥ 70% + R:R ≥ 1:3 + sem conflito direcional. (Limiares 7/9 e 70% = Fase Piloto, recalibráveis — Q-002; R:R = 1:3 — Q-004.)

Score ICT = 0 bloqueia o sinal independente da soma Elliott + SMC.

---

## CHUNK-SY-003
---
chunk_id: SY-003
agente: SynthesisAgent
topico: conviction_vector_multidimensional
prioridade: critica
quando_consultar: ao_calcular_convicao_global
---
**Conviction Vector — 8 dimensões**
A convicção global NÃO é soma simples. É um vetor multidimensional com independência ponderada:

| Dimensão | Fonte | Descrição |
|---|---|---|
| estrutural | Elliott | Qualidade da contagem de ondas |
| geometrica | Fibonacci | Proporções validadas |
| fractal | Elliott + Fibonacci | Coerência entre timeframes |
| institucional | SMC | Confirmação do comportamento institucional |
| operacional | ICT | Condições de execução presentes |
| temporal | ICT | Killzone ativa, timing adequado |
| volume | SMC | Contexto de volume institucional |
| historico | pattern_memory | Performance histórica do setup |

Evidências causalmente correlacionadas (ex: BOS e CHoCH sequenciados) contam como uma, não como duas. Independência é requisito para somar.

---

## CHUNK-SY-004
---
chunk_id: SY-004
agente: SynthesisAgent
topico: processo_decisao_7_passos
prioridade: alta
quando_consultar: ao_executar_processo_de_sintese
---
**Processo de decisão — 7 passos sequenciais**
1. Verificar guards constitucionais: ICT score, directional_conflict, R:R, convicção — qualquer bloqueio → NEUTRO ou AGUARDAR
2. Calcular score_total (Elliott + SMC + ICT)
3. Calcular conviction_vector (8 dimensões)
4. Comparar Dupla Narrativa (Estrutural × Institucional)
5. Se score ≥ 7 E convicção ≥ 70% E R:R ≥ 1:3: preparar sinal COMPRA/VENDA
6. Verificar alternativas: há hipótese alternativa com prob > 30%? → incluir em contagem_alternativa
7. Gerar TMP (Trading Mission Package) se sinal operacional emitido

---

## CHUNK-SY-005
---
chunk_id: SY-005
agente: SynthesisAgent
topico: estados_de_sinal
prioridade: critica
quando_consultar: ao_definir_estado_do_sinal
---
**Estados de sinal possíveis**

| Estado | Condição | Ação |
|---|---|---|
| COMPRA | score ≥ 7 + conv ≥ 70% + R:R ≥ 1:3 + sem conflito + ICT ≥ 1 + bias bullish | Gerar TMP bullish |
| VENDA | Idem com bias bearish | Gerar TMP bearish |
| NEUTRO | directional_conflict = true OU score < 5 OU convicção < 50% | Aguardar resolução |
| AGUARDAR_SETUP | Estrutura identificada mas condições incompletas | Monitorar |

NEUTRO ≠ AGUARDAR_SETUP. NEUTRO = conflito presente. AGUARDAR = setup bom mas timing ruim.

---

## CHUNK-SY-006
---
chunk_id: SY-006
agente: SynthesisAgent
topico: dupla_narrativa_comparacao
prioridade: alta
quando_consultar: ao_comparar_narrativas_estrutural_e_institucional
---
**Comparação da Dupla Narrativa**
O Synthesis Agent recebe dois inputs narrativos:
1. **Narrativa Estrutural** (Elliott + Fibonacci + Fractal): "O que o mercado está construindo?"
2. **Narrativa Institucional** (SMC): "Como os institucionais estão construindo isso?"

Critérios de avaliação:
- Narrativas convergentes → convicção elevada, sinal possível
- Narrativas paralelas (não conflitantes, independentes) → convicção moderada
- Narrativas divergentes com direções opostas → `directional_conflict = true` → NEUTRO obrigatório
- SMC neutro (sem evidência) → não conta como divergência, apenas como ausência de confirmação

---

## CHUNK-SY-007
---
chunk_id: SY-007
agente: SynthesisAgent
topico: trading_mission_package_tmp
prioridade: alta
quando_consultar: ao_gerar_tmp
---
**Trading Mission Package (TMP)**
O TMP é o **artefato interno** de passagem da Síntese para a camada de risco (Síntese → Risk Agent) — snapshot da decisão de síntese. **NÃO é mais o artefato de fronteira** do sistema: a fronteira SOT → Bot Trade Finance passou a ser o **Signal Package** (EUA-E19a/DHR-EUA-E19a, Andraus 2026-09-22; termo fundacional restaurado). O TMP entregue pela Síntese tem os campos obrigatórios abaixo:

- sinal: COMPRA | VENDA
- ativo: BTC | XAU | NASDAQ
- entry_zone: {min, max} em preço
- stop_level: preço do stop estrutural (invalidador)
- target_1, target_2, target_3: alvos progressivos
- risk_reward: calculado com stop e target_1
- sizing_sugerido: % do capital baseado em Kelly/risco
- invalidação_explícita: condição que cancela o trade
- contagem_alternativa: hipótese concorrente se prob > 30%
- alerta_telegram: string formatada para o canal

O TMP é gerado APENAS quando sinal = COMPRA ou VENDA.

---

## CHUNK-SY-008
---
chunk_id: SY-008
agente: SynthesisAgent
topico: formato_alerta_telegram
prioridade: media
quando_consultar: ao_formatar_alerta_telegram
---
**Formato do alerta Telegram**
```
🎯 [COMPRA|VENDA] [ATIVO]
📊 Score: X/9 | Convicção: X%
📍 Entrada: X.XX – X.XX
🛑 Stop: X.XX (invalidador: [condição])
🎯 T1: X.XX | T2: X.XX | T3: X.XX
⚡ R:R: X.X:1
📐 Hipótese: [contagem Elliott resumida]
🏦 Institucional: [resumo SMC 1 linha]
⚠️ Alternativa: [se prob > 30%]
```

NUNCA emitir alerta sem todos os campos preenchidos. NUNCA usar emojis fora do padrão.

---

## CHUNK-SY-009
---
chunk_id: SY-009
agente: SynthesisAgent
topico: inference_context_envelope
prioridade: alta
quando_consultar: ao_preparar_chamada_llm
---
**InferenceContextEnvelope — protocolo obrigatório (CEE-001)**
Toda chamada LLM do Synthesis Agent DEVE usar o InferenceContextEnvelope:

```json
{
  "stable_prefix": {
    "constitution": "...",
    "rules": "...",
    "methodology": "..."
  },
  "variable_payload": {
    "elliott_output": {...},
    "fibonacci_output": {...},
    "smc_output": {...},
    "ict_output": {...},
    "capital_context": {...}
  },
  "cache_control": {
    "stable_prefix_ttl": 3600,
    "variable_payload_ttl": 0
  }
}
```

O stable_prefix contém a Constituição e Regras — imutáveis por sessão, aptos para cache.
O variable_payload contém os outputs dos agentes — mudam a cada candle, nunca cacheados.

---

## CHUNK-SY-010
---
chunk_id: SY-010
agente: SynthesisAgent
topico: pattern_memory_historico
prioridade: media
quando_consultar: ao_ponderar_componente_historico_da_convicao
---
**Pattern Memory — dimensão histórica da convicção**
A dimensão `historico` do Conviction Vector usa o `pattern_memory` para ajustar convicção baseado em performance histórica do setup específico.

Campos relevantes:
- `win_rate`: taxa de acerto do setup (ex: W4_ZIGZAG_RETRACAO_OB)
- `avg_rr`: R:R médio histórico
- `sample_size`: amostra (mínimo 10 trades para ser relevante)

Com sample_size < 10: dimensão histórica = neutro (50%), não penaliza nem bonifica.
Com win_rate < 40%: dimensão histórica = negativa (-10% convicção)
Com win_rate > 65%: dimensão histórica = positiva (+10% convicção)

---

## CHUNK-SY-011
---
chunk_id: SY-011
agente: SynthesisAgent
topico: regras_framework_4es
prioridade: alta
quando_consultar: ao_avaliar_trade_off_eficacia_eficiencia
---
**Framework 4Es aplicado ao Synthesis Agent** (Q-009)
O Synthesis Agent opera segundo a hierarquia 4Es (CEE-001 v2.0):

1. **Eficácia**: análise correta (seguir constituição, hierarquia, regras) — sempre primeiro
2. **Efetividade**: resultado que funciona no mercado real, no tempo certo (inclui latência)
3. **Eficiência**: custo computacional, latência, tokens por execução
4. **Economicidade**: menor custo unitário de provisionamento (classe de modelo, cache) — por último; nunca acima de Eficácia

Um sinal rápido que viola as regras é pior que um sinal lento que as segue.
Uma decisão eficiente que sacrifica eficácia viola a constituição.

---

## CHUNK-SY-012
---
chunk_id: SY-012
agente: SynthesisAgent
topico: antiescopo_absoluto
prioridade: critica
quando_consultar: ao_verificar_limites_de_responsabilidade
---
**O que o Synthesis Agent NUNCA faz**
- Analisar diretamente dados de mercado (preço, volume, candles) → agentes especialistas
- Resolver conflito direcional favorecendo SMC sobre Elliott → hierarquia inviolável
- Emitir COMPRA ou VENDA com convicção < 70% → RULE-SY-003
- Emitir sinal com directional_conflict = true → RULE-SY-001
- Emitir sinal com ICT score = 0 → RULE-SY-008
- Emitir sinal com R:R < 1:3 → RULE-CEE-004 salvaguarda 5 (CEE-001 §11)
- Emitir sinal sem nível de invalidação declarado → RULE-SY-007
- Ignorar hipótese alternativa com probabilidade > 30% → RULE-SY-006
