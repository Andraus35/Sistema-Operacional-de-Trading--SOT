# RAG — Fibonacci Validator Knowledge Base
<!-- 12 chunks | Fonte: ENGENHARIA GERAL Doc04 §14 + Doc05 (FCES) + ARIA §10 Skill1 -->

---

## CHUNK-FB-001
```yaml
chunk_id: FB-001
agente: FibonacciValidator
topico: missao_fundamental
prioridade: critica
quando_consultar: sempre_que_iniciar_validacao
```
**Missão do Fibonacci Validator**
O Fibonacci Validator NÃO cria hipóteses Elliott. Recebe hipóteses já construídas e valida se as proporções geométricas de preço e tempo são coerentes com as relações de Fibonacci esperadas para cada tipo de onda. A pergunta que responde é: "A geometria de Fibonacci confirma ou rejeita esta hipótese de Elliott?"

---

## CHUNK-FB-002
```yaml
chunk_id: FB-002
agente: FibonacciValidator
topico: ratios_por_onda
prioridade: critica
quando_consultar: ao_validar_cada_onda_especifica
```
**Ratios Fibonacci esperados por tipo de onda**

| Onda | Relação com | Ratios esperados              | Notas                         |
|------|-------------|-------------------------------|-------------------------------|
| 2    | Onda 1      | 50%, 61.8%, 76.4%             | Nunca 100%+                   |
| 3    | Onda 1      | 161.8%, 261.8%, 423.6%        | Extensão. 161.8% = mínimo     |
| 4    | Onda 3      | 38.2%, 50%                    | Raramente 61.8% sem sobreposição |
| 5    | Onda 1      | 100% (igualdade), 61.8%       | Ou projeção ABCD              |
| A    | Onda anterior | Variável                   | Depende do tipo de correção   |
| B    | Onda A      | 50%, 61.8%, 76.4%, 85.4%      | Nunca > 100% em zigzag puro   |
| C    | Onda A      | 100%, 123.6%, 161.8%          | Extensão em flats e combinadas|

Tolerância aceitável: ±2% do nível esperado.

---

## CHUNK-FB-003
```yaml
chunk_id: FB-003
agente: FibonacciValidator
topico: ote_definicao
prioridade: alta
quando_consultar: ao_calcular_ote_para_ict
```
**OTE — Optimal Trade Entry (definição ICT via Fibonacci)**
O OTE é a zona entre 61.8% e 78.6% do dealing range da sessão ativa. Representa a zona de máxima eficiência de entrada dentro de um OB institucional — onde o preço corrige profundamente antes de retomar o impulso.

**Cálculo:**
- OTE_low = range_high - (range_high - range_low) × 0.786
- OTE_high = range_high - (range_high - range_low) × 0.618
- (Inverte para trade bearish)

O OTE é calculado APENAS quando o dealing range da sessão está estabelecido. Nunca usar OTE em mercado sem range definido.

---

## CHUNK-FB-004
```yaml
chunk_id: FB-004
agente: FibonacciValidator
topico: confluencia_multi_timeframe
prioridade: alta
quando_consultar: ao_identificar_zonas_de_alta_qualidade
```
**Confluência de Fibonacci multi-timeframe**
Uma zona de confluência é formada quando múltiplos timeframes convergem no mesmo nível de Fibonacci (tolerância: ±0.5% do preço). Quanto mais timeframes convergem, maior a qualidade da zona.

Níveis de qualidade:
- **Alta (high)**: 3+ timeframes convergindo (ex: D1 + H4 + H1 no mesmo nível 61.8%)
- **Média (medium)**: 2 timeframes
- **Baixa (low)**: único timeframe ou estimativa

Zonas de confluência multi-TF alimentam diretamente o SMC Specialist como contexto para avaliar Order Blocks.

---

## CHUNK-FB-005
```yaml
chunk_id: FB-005
agente: FibonacciValidator
topico: conflito_geometrico_protocolo
prioridade: critica
quando_consultar: quando_proporcoes_violam_hipotese
```
**Protocolo de conflito geométrico**
Quando as proporções observadas violam a hipótese principal:
1. Reportar conflito com detalhe: qual onda violou, qual ratio foi esperado, qual foi observado
2. NÃO descartar a hipótese unilateralmente — reporta ao Elliott Specialist
3. Verificar se as proporções se encaixam melhor na hipótese alternativa
4. Se `fits_alternative_better = true` → sinalizar ao Synthesis Agent

Conflito geométrico NÃO = invalidação estrutural. É informação para o Elliott Specialist revisar.

---

## CHUNK-FB-006
```yaml
chunk_id: FB-006
agente: FibonacciValidator
topico: extensoes_projecoes
prioridade: alta
quando_consultar: ao_calcular_alvos_de_ondas_futuras
```
**Extensões e projeções Fibonacci para alvos**

Alvos de Onda 3 (mais importantes):
- 161.8% de Onda 1 = alvo mínimo frequente
- 261.8% = alvo de extensão moderada
- 423.6% = alvo de extensão máxima (mercados muito fortes)

Alvos de Onda 5:
- Igualdade com Onda 1: mais comum
- 61.8% de Onda 1: truncamento
- Projeção ABC: C = A em extensão

Alvos de Onda C (correção):
- 100% de Onda A: o mais comum
- 161.8% de Onda A: overshooting em mercados voláteis

---

## CHUNK-FB-007
```yaml
chunk_id: FB-007
agente: FibonacciValidator
topico: simetria_temporal
prioridade: media
quando_consultar: ao_analisar_proporcionalidade_temporal
```
**Simetria temporal como validação adicional**
Além das proporções de preço, o Fibonacci Validator pode observar:
- Onda 4 frequentemente dura proporção similar à Onda 2 em tempo
- Onda 5 frequentemente é proporcional à Onda 1 em tempo
- Correções ABC: C tende a durar proporção de A × 1.0 ou 1.618

A simetria temporal é corroborante, não determinante. Não invalida hipótese se ausente.

---

## CHUNK-FB-008
```yaml
chunk_id: FB-008
agente: FibonacciValidator
topico: score_geometrico
prioridade: alta
quando_consultar: ao_calcular_convicção_geometrica
```
**Cálculo da convicção geométrica (0–100%)**
A convicção geométrica é calculada com base no número e qualidade das proporções validadas:

- Cada onda validada dentro da tolerância: +15–20 pontos
- Confluência multi-TF no nível: +15 pontos bônus
- Validação do OTE dentro do OB: +10 pontos bônus
- Conflito em onda importante (3, 4): -30 pontos
- Conflito em onda menos crítica (5, B): -15 pontos
- Status inconclusivo (pivôs insuficientes): máximo 40%

Convicção geométrica alimenta a dimensão `geometrica` do Conviction Vector do Synthesis Agent.

---

## CHUNK-FB-009
```yaml
chunk_id: FB-009
agente: FibonacciValidator
topico: antiescopo_absoluto
prioridade: critica
quando_consultar: ao_verificar_limites_de_responsabilidade
```
**O que o Fibonacci Validator NUNCA faz**
- Criar contagens Elliott próprias → responsabilidade do Elliott Specialist
- Definir bias direcional → responsabilidade do Elliott Specialist
- Identificar OBs, CHoCH, BOS → responsabilidade do SMC Specialist
- Calcular killzones ou Power of 3 → responsabilidade do ICT Specialist
- Emitir sinal operacional → responsabilidade do Synthesis Agent
- Decidir invalidação estrutural → reporta ao Elliott Specialist, não decide sozinho

---

## CHUNK-FB-010
```yaml
chunk_id: FB-010
agente: FibonacciValidator
topico: canais_de_elliott
prioridade: media
quando_consultar: ao_validar_canais_e_projecoes_geometricas
```
**Canais de Elliott e proporcionalidade geométrica**
Os canais de Elliott são uma forma de validação geométrica adicional:
1. Canal básico: linha conectando início da Onda 1 ao final da Onda 2, paralela passando pelo final da Onda 1
2. Canal ajustado: após Onda 3 conhecida, reconectar usando finais de Onda 2 e 4
3. Onda 5 frequentemente atinge o canal superior (ou fica aquém = truncamento)

A proporcionalidade do canal confirma a hipótese estrutural sem depender de pivôs exatos.

---

## CHUNK-FB-011
```yaml
chunk_id: FB-011
agente: FibonacciValidator
topico: retracao_vs_extensao_vs_projecao
prioridade: media
quando_consultar: ao_distinguir_tipos_de_medicao_fibonacci
```
**Distinção entre retração, extensão e projeção**
- **Retração**: medida dentro do movimento anterior (ex: Onda 2 retrai Onda 1)
  - Fórmula: 1 - ratio (50% de retração = mercado retrocede 50% do movimento anterior)
- **Extensão**: medida além do movimento anterior (ex: Onda 3 estende Onda 1)
  - Fórmula: ratio × comprimento da onda de referência adicionado ao início
- **Projeção**: estima movimento futuro baseado em distância de onda anterior diferente
  - Ex: Onda C projetada como 100% de Onda A começando do final de Onda B

Confundir retração com extensão é erro crítico de cálculo.

---

## CHUNK-FB-012
```yaml
chunk_id: FB-012
agente: FibonacciValidator
topico: comportamento_quando_pivots_insuficientes
prioridade: alta
quando_consultar: quando_analise_em_formacao_sem_pivots_confirmados
```
**Comportamento com pivôs insuficientes**
Quando a onda em andamento ainda não terminou (pivô final desconhecido):
- Status = `inconclusive` para essa onda específica
- Calcular PROJEÇÃO ao invés de validação
- Declarar explicitamente que o pivô é projetado, não confirmado
- Convicção geométrica máxima = 40% para ondas incompletas
- Não bloquear o pipeline — reportar o que foi validado até agora

Pivôs projetados são estimativas úteis para o ICT Specialist calcular zonas-alvo.
