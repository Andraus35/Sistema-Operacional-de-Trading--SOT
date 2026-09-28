# RAG — SMC Specialist Knowledge Base
<!-- 12 chunks | Fonte: ENGENHARIA GERAL Doc07 (IIES) + ARIA §10 Skill2 + §5 Layer2 -->

---

## CHUNK-SM-001
```yaml
chunk_id: SM-001
agente: SMCSpecialist
topico: missao_fundamental
prioridade: critica
quando_consultar: sempre_que_iniciar_analise_smc
```
**Missão do SMC Specialist**
O SMC Specialist identifica evidências da atuação institucional e mede o quanto essas evidências fortalecem ou enfraquecem as hipóteses estruturais produzidas pelo Elliott Specialist. NUNCA opera em isolamento — todo evento SMC é interpretado no contexto Elliott. A pergunta que responde é: "O comportamento institucional confirma ou contradiz a hipótese estrutural atual?"

---

## CHUNK-SM-002
```yaml
chunk_id: SM-002
agente: SMCSpecialist
topico: order_block_definicao_e_qualidade
prioridade: critica
quando_consultar: ao_identificar_e_qualificar_order_blocks
```
**Order Blocks — definição, identificação e qualidade**
Um Order Block (OB) é a última vela (ou conjunto de velas) antes de um movimento impulsivo significativo. Representa zona de atuação institucional.

**Qualidade por contexto Elliott:**
- OB criado durante Onda 3 descendente → alta qualidade (zona de distribuição institucional)
- OB criado no início de Onda 1/3 → alta qualidade (acumulação institucional)
- OB criado durante Onda B → baixa qualidade (movimento corretivo, não institucional)
- OB criado durante lateralização → qualidade baixa-média

**Regra crítica:** OB mitigado = descartado. OB é mitigado quando o preço fechou dentro da zona com um candle de direção oposta. OB mitigado nunca aparece como zona ativa.

---

## CHUNK-SM-003
```yaml
chunk_id: SM-003
agente: SMCSpecialist
topico: bos_choch_interpretacao_contextual
prioridade: critica
quando_consultar: ao_interpretar_bos_e_choch
```
**BOS e CHoCH — interpretação sempre contextual**

**BOS (Break of Structure):**
- Durante Onda 3: alta relevância — confirma impulso institucional
- Durante Onda B: baixa relevância — movimento corretivo, não tendencial
- BOS sem CHoCH prévio: peso reduzido (sem mudança de caráter antes da quebra)

**CHoCH (Change of Character):**
- Após quinta falhada: muito relevante — sinaliza possível reversão
- Em lateralização: baixa relevância — mercado sem direção
- CHoCH que precede BOS: alta relevância combinada

**Regra:** Nenhum BOS ou CHoCH é interpretado fora do contexto Elliott. A mesma quebra de estrutura tem significados opostos em Onda 3 vs Onda B.

---

## CHUNK-SM-004
```yaml
chunk_id: SM-004
agente: SMCSpecialist
topico: liquidez_tipos_e_validade
prioridade: alta
quando_consultar: ao_avaliar_sweeps_de_liquidez
```
**Tipos de liquidez e validação de sweeps**

| Tipo                | Localização                          | Característica                      |
|---------------------|--------------------------------------|-------------------------------------|
| Buy Side Liquidity  | Acima de equal highs / swing highs   | Alvo para movimento bearish         |
| Sell Side Liquidity | Abaixo de equal lows / swing lows    | Alvo para movimento bullish         |
| Internal Liquidity  | Dentro do range (FVGs, OBs internos) | Alvos de curto prazo                |
| External Liquidity  | Além dos extremos do range           | Alvos de longo prazo                |

**Validação do sweep:**
- Sweep válido = preço varre a liquidez e RETORNA ao range com fechamento interno
- Sweep inválido = preço varre mas não retorna (continuação, não reversão)
- Sweep inválido NÃO pontua o layer SMC

---

## CHUNK-SM-005
```yaml
chunk_id: SM-005
agente: SMCSpecialist
topico: fair_value_gap
prioridade: alta
quando_consultar: ao_identificar_e_usar_fvgs
```
**Fair Value Gaps (FVG) — identificação e uso**
Um FVG é um gap de três velas onde a segunda vela cria um espaço não preenchido entre a sombra superior da primeira e a sombra inferior da terceira (bullish FVG) ou vice-versa (bearish FVG).

**Uso no SOT:**
- FVG dentro de um OB = zona de precisão de entrada (aumenta qualidade do OB)
- FVG isolado = zona de suporte/resistência de menor qualidade
- FVG mitigado (preenchido pelo preço) = zona invalidada para entrada

O FVG é passado ao ICT Specialist para cálculo de OTE e ponto de entrada preciso.

---

## CHUNK-SM-006
```yaml
chunk_id: SM-006
agente: SMCSpecialist
topico: narrativa_institucional
prioridade: alta
quando_consultar: ao_construir_narrativa_smc
```
**Construção da narrativa institucional**
A narrativa institucional é uma sequência de eventos SMC interpretada em contexto Elliott. Exemplo de narrativa válida:
> "Em H4 (grau Intermediate), após Onda 4 do Elliott, o preço varreu liquidez sell-side (equal lows), retornou ao range com CHoCH bullish, criando um OB bullish não-mitigado na zona de 61.8% Fibonacci. BOS bullish subsequente confirma início de Onda 5. Alinhamento com hipótese Elliott = CONFIRMS."

Uma narrativa incompleta (apenas "BOS identificado" sem contexto) é insuficiente.

---

## CHUNK-SM-007
```yaml
chunk_id: SM-007
agente: SMCSpecialist
topico: dupla_narrativa
prioridade: critica
quando_consultar: ao_publicar_output_para_synthesis
```
**Dupla Narrativa — princípio fundamental (Doc07)**
O output SMC deve incluir sempre a Dupla Narrativa:
1. **Narrativa Estrutural (Elliott)**: o que a estrutura de ondas diz
2. **Narrativa Institucional (SMC)**: o que o comportamento institucional diz

Quando as duas convergem → `elliott_alignment = "confirms"`
Quando as duas divergem → `directional_conflict = true` → Synthesis Agent emite NEUTRO

A comparação das duas narrativas pelo Synthesis Agent é o que diferencia o SOT de análise técnica comum.

---

## CHUNK-SM-008
```yaml
chunk_id: SM-008
agente: SMCSpecialist
topico: score_smc_layer
prioridade: alta
quando_consultar: ao_calcular_score_para_synthesis
```
**Cálculo do score SMC (0–3) para o Synthesis Agent**
- **0**: sem evidência institucional válida, ou directional_conflict = true
- **1**: evidência fraca (OB mitigado / sweep inválido / CHoCH sem contexto claro)
- **2**: evidência moderada alinhada ao Elliott (OB ativo + sweep válido OU CHoCH+BOS alinhados)
- **3**: evidência forte + múltiplas confluências SMC alinhadas ao Elliott (OB ativo + FVG + sweep válido + CHoCH+BOS sequenciados corretamente)

Score 3/3 exige que os eventos SMC ocorram nas ondas Elliott esperadas (ex: OB na zona de Onda 4, BOS na Onda 3).

---

## CHUNK-SM-009
```yaml
chunk_id: SM-009
agente: SMCSpecialist
topico: mapeamento_luxalgo
prioridade: alta
quando_consultar: ao_processar_payloads_luxalgo
```
**Mapeamento de campos LuxAlgo para conceitos SOT**

| Campo LuxAlgo         | Conceito SOT                | Regra de uso                              |
|-----------------------|-----------------------------|-------------------------------------------|
| `ob_type`             | Tipo do OB                  | bullish/bearish/none                      |
| `ob_mitigated`        | OB mitigado?                | true → descartar, não pontuar             |
| `choch`               | CHoCH confirmado?           | true → verificar contexto Elliott         |
| `fvg_present`         | FVG presente no OB?         | true → aumenta qualidade do OB            |
| `liquidity_swept`     | Sweep de liquidez?          | true → verificar retorno ao range         |
| `sweep_type`          | Tipo de liquidez varrida    | external = mais relevante                 |
| `structure_bias`      | Bias estrutural LuxAlgo     | SUBORDINADO ao bias Elliott               |

O campo `structure_bias` do LuxAlgo NUNCA sobrepõe ou corrige o bias Elliott. É evidência adicional.

---

## CHUNK-SM-010
```yaml
chunk_id: SM-010
agente: SMCSpecialist
topico: conflito_direcional_protocolo
prioridade: critica
quando_consultar: quando_smc_contradiz_elliott
```
**Protocolo de conflito direcional SMC × Elliott**
Quando `directional_conflict = true` (SMC aponta direção oposta ao Elliott):
1. O SMC Specialist reporta o conflito ao Conflict Map — não resolve unilateralmente
2. NÃO sobrepõe ou "corrige" a direção de Elliott
3. A Dupla Narrativa declara explicitamente a divergência
4. O Synthesis Agent recebe `directional_conflict = true` e emite NEUTRO
5. NUNCA emitir sinal operacional com conflito direcional aberto

Isso decorre do Princípio da Hierarquia: Elliott é o mapa, SMC confirma.

---

## CHUNK-SM-011
```yaml
chunk_id: SM-011
agente: SMCSpecialist
topico: contexto_volume_institucional
prioridade: media
quando_consultar: ao_avaliar_contexto_de_volume
```
**Volume institucional como contexto SMC**
O SMC Specialist observa padrões de volume para contextualizar atividade institucional:
- **Expansão de volume**: confirma deslocamento genuíno (impulso institucional)
- **Absorção**: grande volume sem movimento de preço = acumulação/distribuição
- **Exaustão**: volume decrescente com preço ainda subindo = fim de movimento
- **Reacumulação**: volume baixo em correção rasa = institucional mantendo posição

Volume expansivo em direção contrária ao OB = possível mitigação iminente.

---

## CHUNK-SM-012
```yaml
chunk_id: SM-012
agente: SMCSpecialist
topico: antiescopo_absoluto
prioridade: critica
quando_consultar: ao_verificar_limites_de_responsabilidade
```
**O que o SMC Specialist NUNCA faz**
- Criar contagens de Elliott ou hipóteses estruturais → Elliott Specialist
- Definir bias direcional primário → Elliott Specialist
- Identificar killzones, OTE, Power of 3, Judas Swing → ICT Specialist
- Calcular position sizing → ICT Specialist e Synthesis Agent
- Emitir sinais operacionais isoladamente → Synthesis Agent
- Sobrepor bias Elliott com bias SMC → violação constitucional
