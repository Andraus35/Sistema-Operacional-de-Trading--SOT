# RAG — Elliott Wave Specialist Knowledge Base
<!-- 15 chunks | Fonte: ENGENHARIA GERAL Doc04 (ECES) + Doc01 (SOT Constitution) + SAS-001 -->

---

## CHUNK-EW-001
```yaml
chunk_id: EW-001
agente: ElliottWaveSpecialist
topico: missao_fundamental
prioridade: critica
quando_consultar: sempre_que_iniciar_analise
```
**Missão do Elliott Specialist**
O Elliott Wave Specialist constrói e mantém um "Modelo Estrutural Vivo" do mercado. Não procura entradas. Não procura sinais. Procura a melhor explicação estrutural para o comportamento de preço atual. A pergunta que responde é: "Qual estrutura de Elliott explica melhor o comportamento atual?" Cada hipótese é uma narrativa explicativa, não uma previsão determinística.

---

## CHUNK-EW-002
```yaml
chunk_id: EW-002
agente: ElliottWaveSpecialist
topico: tres_regras_imutaveis
prioridade: critica
quando_consultar: ao_validar_qualquer_contagem
```
**As 3 Regras Imutáveis de Elliott (nunca violadas)**
1. **Onda 3 nunca é a mais curta** das ondas de impulso (1, 3, 5). Se Onda 3 for mais curta que Onda 1 → descartar contagem imediatamente.
2. **Onda 2 nunca penetra o início da Onda 1** (nunca retrai mais de 100% da Onda 1). Se isso ocorrer → estrutura não é um impulso.
3. **Onda 4 nunca penetra o território de preço da Onda 1** em impulsos normais (exceto diagonais). Se penetrar → considerar diagonal ou estrutura corretiva.

---

## CHUNK-EW-003
```yaml
chunk_id: EW-003
agente: ElliottWaveSpecialist
topico: processo_analitico_cinco_passos
prioridade: alta
quando_consultar: ao_processar_novos_dados_de_mercado
```
**Processo Analítico em 5 Etapas (Doc04 §5)**
1. **Observar**: identificar regime de mercado (tendencial/corretivo/lateral) ANTES da contagem
2. **Segmentar**: localizar grandes pivôs → estrutura principal → subestrutura → microestrutura
3. **Construir**: gerar hipótese principal + mínimo 1 hipótese alternativa
4. **Validar**: verificar as 3 regras imutáveis + proporções Fibonacci
5. **Projetar**: calcular alvos de ondas futuras + definir invalidadores
A análise é SEMPRE top-down: S1 → D1 → H4 → H1 → M5. Nunca começa pelo M5.

---

## CHUNK-EW-004
```yaml
chunk_id: EW-004
agente: ElliottWaveSpecialist
topico: hierarquia_graus_timeframes
prioridade: alta
quando_consultar: ao_classificar_graus_ondas
```
**Hierarquia oficial de graus e timeframes (SOT)**

| Grau         | Timeframe | Duração típica      |
|------------- |-----------|---------------------|
| Supercycle   | S1/Mensal | Décadas             |
| Cycle        | S1/Semanal| Anos                |
| Primary      | D1        | Meses               |
| Intermediate | H4        | Semanas             |
| Minor        | H1        | Dias                |
| Minute       | M5        | Horas               |
| Minuette     | M1        | Minutos             |

Regra de alinhamento: a onda em M5 é subestrutura da onda em H1, que é subestrutura da onda em H4 etc.

---

## CHUNK-EW-005
```yaml
chunk_id: EW-005
agente: ElliottWaveSpecialist
topico: regras_ondas_especificas
prioridade: alta
quando_consultar: ao_identificar_tipo_de_onda
```
**Regras por tipo de onda**
- **Onda 1**: frequentemente confundida com correção. Volume deve aumentar na segunda metade.
- **Onda 2**: retrai profundamente (50%–76.4%), nunca passa de 100% da Onda 1.
- **Onda 3**: mais longa e forte das ondas de impulso. Volume expansivo. Extensão mínima 161.8% da Onda 1.
- **Onda 4**: retrai 38.2%–50% da Onda 3. Nunca entra no território de preço da Onda 1. Frequentemente lateral/complexa.
- **Onda 5**: pode ser igual à Onda 1 ou 61.8% dela. Volume frequentemente menor que Onda 3. Pode truncar em mercados muito fortes.
- **Ondas A-B-C**: estruturas corretivas. Onda B não deve passar de 100% da Onda A em ziguezague.

---

## CHUNK-EW-006
```yaml
chunk_id: EW-006
agente: ElliottWaveSpecialist
topico: hipoteses_multiplas_obrigatorias
prioridade: critica
quando_consultar: ao_publicar_analise_no_blackboard
```
**Regra das hipóteses múltiplas obrigatórias (P02 + P03)**
O Elliott Specialist NUNCA publica apenas uma hipótese. Sempre produz:
- Hipótese Principal: maior convicção, declarada explicitamente em %
- Hipótese Alternativa (mínimo 1): com condição de ativação explícita
- Condição de resolução: que evento de mercado promoveria a alternativa a principal?

Quando duas contagens têm convicção próxima (diferença < 15%), reportar como ambiguidade explícita com bias = "ambiguous". Nunca forçar uma leitura.

---

## CHUNK-EW-007
```yaml
chunk_id: EW-007
agente: ElliottWaveSpecialist
topico: estados_cognitivos_do_agente
prioridade: media
quando_consultar: ao_reportar_estado_no_blackboard
```
**Estados cognitivos do agente (Doc02 ADS)**
O agente percorre estes estados em ordem: INACTIVE → OBSERVING → INVESTIGATING → HYPOTHESIS_BUILDING → VALIDATING → MONITORING → REVISING → CONFIRMED → INVALIDATED

- **CONFIRMED**: hipótese se desenvolvendo conforme previsto
- **REVISING**: nova evidência exige revisão mas não invalida
- **INVALIDATED**: regra imutável violada ou invalidador atingido → reinicia com novo conjunto de hipóteses

O estado é publicado no Blackboard junto com cada output.

---

## CHUNK-EW-008
```yaml
chunk_id: EW-008
agente: ElliottWaveSpecialist
topico: regime_de_mercado
prioridade: alta
quando_consultar: antes_de_iniciar_qualquer_contagem
```
**Identificação de regime antes da contagem (Doc04 §5-1)**
O regime é determinado ANTES de qualquer contagem e nunca é alterado pela contagem.

| Regime       | Características                                      |
|------------- |------------------------------------------------------|
| trending_up  | HH/HL progressivos, volume expansivo em impulsos     |
| trending_down| LL/LH progressivos, volume expansivo em impulsos     |
| corrective   | Estrutura ABC, zigzague, flat, triangle              |
| lateral      | Sem direção clara, range definido                    |
| compression  | Amplitude diminuindo, triângulo convergente          |
| expansion    | Amplitude aumentando, saída iminente de range        |

Regime lateral: a análise é fundamentalmente diferente. Veja CHUNK-EW-015.

---

## CHUNK-EW-009
```yaml
chunk_id: EW-009
agente: ElliottWaveSpecialist
topico: invalidadores_por_tipo_de_onda
prioridade: critica
quando_consultar: ao_definir_nivel_de_invalidacao
```
**Invalidadores canônicos por contagem**
- Impulso bullish: fechamento abaixo do início da Onda 1
- Impulso bearish: fechamento acima do início da Onda 1
- Onda 3 em andamento: fechamento abaixo do final da Onda 2 (invalida todo o impulso)
- Onda 4 em andamento: penetração no território de preço da Onda 1 (invalida → considerar diagonal)
- Correção ABC: superação do início da Onda A em 100% invalida o ABC como correção simples
- Diagonal: penetração do início = invalida a diagonal

Todo output deve incluir o invalidador com preço exato.

---

## CHUNK-EW-010
```yaml
chunk_id: EW-010
agente: ElliottWaveSpecialist
topico: score_elliott_layer
prioridade: alta
quando_consultar: ao_calcular_score_para_synthesis
```
**Cálculo do score Elliott (0–3) para o Synthesis Agent**
- **0**: estrutura ambígua sem direção clara, ou regra imutável violada
- **1**: estrutura identificada em apenas 1-2 timeframes, convicção 30–50%
- **2**: estrutura clara em 3+ timeframes, hipótese principal com convicção 50–70%
- **3**: estrutura forte com confluência top-down (S1 ao H1 alinhados), hipótese principal > 70%, sem ambiguidade crítica

O score 3/3 exige confirmação de fractal em pelo menos 4 dos 5 graus hierárquicos.

---

## CHUNK-EW-011
```yaml
chunk_id: EW-011
agente: ElliottWaveSpecialist
topico: relacao_com_volume
prioridade: media
quando_consultar: ao_diferenciar_onda_3_de_onda_B
```
**Volume como sinal confirmatório (não decisivo)**
- Volume crescente em impulso = confirma hipótese impulsiva
- Volume declinante em possível Onda 3: aumentar probabilidade da hipótese alternativa (pode ser Onda B)
- Volume em Onda 4: frequentemente menor — normal
- Volume na Onda 5: comparar com Onda 3. Divergência de volume (5 menor) = possível truncamento ou fim do ciclo

O agente OBSERVA o volume mas não decide baseado somente nele. É evidência corroborante, não determinante.

---

## CHUNK-EW-012
```yaml
chunk_id: EW-012
agente: ElliottWaveSpecialist
topico: tipos_de_correcoes_permitidos
prioridade: media
quando_consultar: ao_identificar_estrutura_corretiva
```
**Tipos de correções reconhecidos pelo SOT**
- **Ziguezague (ABC)**: A impulso, B contra, C impulso. O mais comum.
- **Flat (ABC)**: A 3 ondas, B quase ao início de A, C ao final de A. Frequente em Onda 4.
- **Triângulo (ABCDE)**: 5 ondas em compressão. Geralmente Onda 4 ou Onda B de ziguezague.
- **Double three / Triple three**: correções complexas encadeadas. Ambiguidade alta — declarar explicitamente.
- **Diagonal leading/ending**: 5 ondas com sobreposição permitida. Comum no início ou fim de movimento.

Correções complexas exigem declaração explícita de ambiguidade e evento resolutório.

---

## CHUNK-EW-013
```yaml
chunk_id: EW-013
agente: ElliottWaveSpecialist
topico: nivel_de_ambiguidade
prioridade: alta
quando_consultar: ao_declarar_ambiguidade
```
**Protocolo de ambiguidade (P03 — Múltiplas Hipóteses)**
Quando `ambiguity_level > 0.3` (duas contagens com probabilidade próxima):
1. NUNCA forçar uma leitura ou escolher aleatoriamente
2. Declarar explicitamente `bias = "ambiguous"`
3. Descrever ambas as contagens com suas convicções
4. Declarar o evento resolutório: "Se [evento X], hipótese A prevalece; se [evento Y], hipótese B prevalece"
5. O Synthesis Agent emitirá NEUTRO se a hipótese principal estiver ambígua acima do limiar

---

## CHUNK-EW-014
```yaml
chunk_id: EW-014
agente: ElliottWaveSpecialist
topico: antiescopo_absoluto
prioridade: critica
quando_consultar: ao_verificar_limites_de_responsabilidade
```
**O que o Elliott Specialist NUNCA faz (SAS-001 antiescopo)**
- Identificar OBs, CHoCH, BOS, FVG, Liquidity sweeps → responsabilidade do SMC Specialist
- Calcular convicção global → responsabilidade do Synthesis Agent
- Identificar killzones, OTE, Power of 3 → responsabilidade do ICT Specialist
- Validar proporções Fibonacci → responsabilidade do Fibonacci Validator
- Emitir sinal operacional → responsabilidade do Synthesis Agent
- Analisar volume de forma decisiva → observa, não decide

---

## CHUNK-EW-015
```yaml
chunk_id: EW-015
agente: ElliottWaveSpecialist
topico: mercado_lateral
prioridade: media
quando_consultar: quando_regime_for_lateral
```
**Comportamento em mercado lateral (regime = lateral)**
Em lateralização, a análise de Elliott é conservativa:
- Prioridade: identificar limites do range (suporte e resistência estruturais)
- Não tentar forçar contagem impulsiva em range
- Identificar se é triângulo (compressão com saída iminente) ou flat (correção simples)
- Score máximo Elliott em lateral: 2/3 (raramente 3/3 sem confluência clara)
- Aguardar saída do range com confirmação antes de propor hipótese impulsiva
- O Synthesis Agent emitirá AGUARDAR_SETUP em lateral sem direção confirmada
