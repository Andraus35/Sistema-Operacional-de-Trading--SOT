# RAG — ICT Specialist Knowledge Base
<!-- 12 chunks | Fonte: ENGENHARIA GERAL Doc08 (IEIES) + ARIA §10 Skill3 + §5 Layer3 -->
<!-- Q-004 (Andraus 2026-09-14): R:R mínimo = 1:3 (risco:retorno) = 3:1 (retorno:risco) = R:R numérico ≥ 3.0. Substitui o antigo "2:1". -->

---

## CHUNK-ICT-001
```yaml
chunk_id: ICT-001
agente: ICTSpecialist
topico: missao_fundamental_e_regra_de_inatividade
prioridade: critica
quando_consultar: sempre_que_iniciar_analise_ict
```
**Missão do ICT Specialist + Regra de Inatividade**
O ICT Specialist localiza o ponto de execução de maior eficiência para hipóteses PREVIAMENTE aprovadas. A pergunta que responde é: "Se existe trade, onde entrar com o menor risco possível?"

**Regra de Inatividade (constitucional):**
O ICT Specialist PERMANECE INATIVO enquanto não houver hipótese estrutural aprovada com convicção suficiente. Não descobre oportunidades. Não analisa o mercado autonomamente. Ativado APENAS quando o Conviction Engine aprova uma hipótese.

Esta regra é inviolável — não há exceção.

---

## CHUNK-ICT-002
```yaml
chunk_id: ICT-002
agente: ICTSpecialist
topico: power_of_three_amd
prioridade: alta
quando_consultar: ao_analisar_movimentos_intra_sessao
```
**Power of 3 (AMD): Accumulation, Manipulation, Distribution**
O padrão AMD descreve o ciclo intra-sessão típico do mercado institucional:

1. **Accumulation**: fase inicial da sessão, acumulação em range estreito. Volume baixo.
2. **Manipulation (Judas Swing)**: movimento falso contra o bias da sessão para varrer liquidez. Armadilha de varejo.
3. **Distribution**: movimento real na direção do bias, após sweep da liquidez.

Identificar corretamente a fase M (Manipulation/Judas Swing) é o diferencial da execução ICT: o ponto de reversão do Judas é frequentemente o OTE perfeito para entrada.

---

## CHUNK-ICT-003
```yaml
chunk_id: ICT-003
agente: ICTSpecialist
topico: killzones_horarios_brt
prioridade: critica
quando_consultar: ao_verificar_horario_de_killzone
```
**Killzones — horários em BRT (Brasília)**

| Killzone          | Horário BRT     | Características                              |
|-------------------|-----------------|----------------------------------------------|
| London Open       | 05:00 – 08:00   | Alta liquidez, Judas Swing frequente         |
| New York Open     | 09:30 – 12:00   | Maior volume do dia, tendência forte         |
| New York Afternoon| 14:00 – 16:00   | Segunda oportunidade NY, volume decrescente  |
| Asia Session      | 22:00 – 01:00   | Menor liquidez, range estreito               |

Fora de killzone: score ICT reduz em 1 ponto. Não bloqueia execução se estrutura for excelente (≥ 8/9 nos outros layers).

Nota: Horários mudam 1h com horário de verão dos EUA (verificar calendário).

---

## CHUNK-ICT-004
```yaml
chunk_id: ICT-004
agente: ICTSpecialist
topico: judas_swing_identificacao
prioridade: alta
quando_consultar: ao_identificar_movimento_falso_em_killzone
```
**Judas Swing — identificação e uso**
O Judas Swing é o movimento falso contra o bias da sessão que ocorre tipicamente no início de killzone (London Open ou NY Open).

**Sinais de identificação:**
- Spike rápido contra o bias da sessão em killzone
- Varre liquidez de uma das extremidades do range Asian ou previous session
- Reverte com velocidade e vela de rejeição forte
- Volume na rejeição maior que no spike

**Uso operacional:**
- O ponto de reversão do Judas = candidato a entry zone dentro do OTE
- Judas confirmado + OTE + FVG = condição de entrada de alta qualidade
- Judas ausente: declarar explicitamente "Judas não identificado" com justificativa

---

## CHUNK-ICT-005
```yaml
chunk_id: ICT-005
agente: ICTSpecialist
topico: ote_calculo_execucao
prioridade: critica
quando_consultar: ao_calcular_zona_de_entrada_ote
```
**OTE (Optimal Trade Entry) — cálculo e aplicação ICT**
O OTE é a zona entre 61.8% e 78.6% do dealing range da sessão. É o ponto onde o preço corrige profundamente DENTRO de um OB antes do impulso real.

**Regra fundamental:** OTE NUNCA é usado isoladamente. Exige confluência:
✓ OTE + OB ativo (SMC) + hipótese Elliott aprovada = entrada de qualidade máxima
✓ OTE + FVG dentro do OB = refinamento de precisão
✗ OTE sozinho = sem valor preditivo

**Verificação em andamento:**
Se `current_price_in_ote = true` + killzone ativa + OB ativo + Judas identificado → condição IDEAL de entrada.

---

## CHUNK-ICT-006
```yaml
chunk_id: ICT-006
agente: ICTSpecialist
topico: mss_market_structure_shift_m5
prioridade: alta
quando_consultar: ao_identificar_gatilho_de_confirmacao
```
**MSS (Market Structure Shift) em M5 — gatilho de confirmação**
O MSS em M5 é o gatilho de confirmação para entrada ICT. Representa a mudança de estrutura de mercado no menor grau utilizado pelo SOT.

**MSS bullish:** novo Higher High em M5 após sequência de Lower Lows
**MSS bearish:** novo Lower Low em M5 após sequência de Higher Highs

**Sequência ideal de entrada:**
1. Hipótese Elliott aprovada (bullish)
2. OB bullish ativo identificado pelo SMC Specialist
3. Judas Swing bearish em London Open
4. Preço retorna ao OTE dentro do OB
5. **MSS bullish em M5 confirma** → entrada executada

Sem MSS, a entrada é prematura. MSS é o "gatilho de pull" da operação.

---

## CHUNK-ICT-007
```yaml
chunk_id: ICT-007
agente: ICTSpecialist
topico: stop_loss_estrutural
prioridade: critica
quando_consultar: ao_definir_nivel_de_stop
```
**Stop Loss Estrutural — princípio ICT**
O stop loss no SOT NUNCA é apenas um limitador de prejuízo. É um invalidador estrutural — o preço no qual a leitura da hipótese se torna incorreta.

**Definição do stop:**
- Deve ser abaixo do nível que invalida a hipótese Elliott (ex: abaixo do início da Onda 2)
- Pode ser abaixo da base do OB (se OB for invalidado antes do movimento esperado)
- Nunca stop arbitrário em ATR sem referência estrutural

**Consequência:** um stop grande pode inviabilizar o trade (R:R abaixo do mínimo 1:3). Neste caso, bloquear a execução e aguardar melhor ponto — não reduzir o stop artificialmente.

---

## CHUNK-ICT-008
```yaml
chunk_id: ICT-008
agente: ICTSpecialist
topico: rr_minimo_e_bloqueios
prioridade: critica
quando_consultar: ao_avaliar_viabilidade_do_trade
```
**R:R mínimo e condições de bloqueio**

**R:R mínimo:** 1:3 (risco:retorno; = 3:1 retorno:risco; R:R numérico ≥ 3.0) — absoluto, sem exceção. Mesmo com score 9/9 e convicção 100%, se R:R < 1:3, o trade não é executado. (Q-004)

**Condições de bloqueio obrigatórias (6):**
1. Hipótese estrutural não aprovada → INATIVO
2. R:R calculado < 1:3 com stop estrutural
3. Narrativa estrutural ou institucional instável/conflitante
4. OB alvo já mitigado
5. Killzone encerrada e não há outra até o próximo ciclo
6. ICT score = 0/3 (nenhuma condição ICT satisfeita)

Quando bloqueado, o agente publica `execution_blocked = true` e `blocking_reason` detalhado.

---

## CHUNK-ICT-009
```yaml
chunk_id: ICT-009
agente: ICTSpecialist
topico: score_ict_layer
prioridade: alta
quando_consultar: ao_calcular_score_para_synthesis
```
**Cálculo do score ICT (0–3) para o Synthesis Agent**
- **0**: agente INATIVO (sem hipótese aprovada) ou todas as condições de bloqueio ativas
- **1**: condições parciais (R:R ≥ 1:3 mínimo, mas sem killzone ativa E sem Judas identificado)
- **2**: boas condições (OTE dentro de OB + R:R ≥ 1:3 + killzone ativa OU MSS em M5)
- **3**: condições ótimas: OTE dentro de OB + FVG + killzone ativa + Judas identificado + MSS em M5 + R:R ≥ 1:4 (retorno:risco 4:1)

Score 0 do ICT = nenhum sinal operacional possível, independente da soma Elliott + SMC.

---

## CHUNK-ICT-010
```yaml
chunk_id: ICT-010
agente: ICTSpecialist
topico: processo_sequencial_de_analise
prioridade: alta
quando_consultar: ao_executar_analise_ict_completa
```
**Processo sequencial completo do ICT Specialist (8 passos)**
1. Mapear liquidez: onde o institucional buscará liquidez antes da expansão?
2. Identificar deslocamento genuíno: velocidade + amplitude + volume (não apenas candle grande)
3. Buscar FVG criada no deslocamento: verificar origem, posição, tamanho, mitigação
4. Calcular OTE dentro da zona do OB SMC (61.8–78.6% do dealing range)
5. Verificar killzone: qual killzone ativa? Horário BRT correto?
6. Verificar Judas Swing: houve movimento falso contra o bias no início da killzone?
7. Avaliar risco: stop estrutural definido → calcular R:R → ≥ 1:3?
8. Publicar Plano Operacional OU reportar motivo de bloqueio

Cada etapa é sequencial — não pular etapas mesmo que a anterior pareça óbvia.

---

## CHUNK-ICT-011
```yaml
chunk_id: ICT-011
agente: ICTSpecialist
topico: targets_estruturais
prioridade: alta
quando_consultar: ao_definir_alvos_da_operacao
```
**Definição de targets baseada em estrutura + Fibonacci + liquidez**
Os targets do ICT Specialist não são arbitrários — derivam de:

1. **Target 1**: zona de liquidez mais próxima (equal highs/lows, FVG não preenchido, PDH/PDL)
2. **Target 2**: projeção Fibonacci de Onda 5 ou extensão 1.618 de Onda 1
3. **Target final (extensão)**: liquidez externa máxima + extensão 2.618 Fibonacci

Hierarquia de qualidade: liquidez estrutural > Fibonacci projetado > estimativa ATR

Todo target deve ter o método de cálculo declarado no output (`method` field obrigatório).

---

## CHUNK-ICT-012
```yaml
chunk_id: ICT-012
agente: ICTSpecialist
topico: antiescopo_absoluto
prioridade: critica
quando_consultar: ao_verificar_limites_de_responsabilidade
```
**O que o ICT Specialist NUNCA faz**
- Criar hipóteses estruturais Elliott → Elliott Specialist
- Alterar bias direcional já definido por Elliott → Elliott Specialist
- Operar sem hipótese estrutural aprovada → permanecer INATIVO
- Analisar OBs institucionais amplos → SMC Specialist
- Analisar em H4 ou D1 → usa apenas M5 e H1 para execução
- Aceitar R:R < 1:3 → condição de bloqueio absoluta
- Emitir sinal sem ICT score ≥ 1 → Synthesis Agent recebe score 0 = sem sinal
