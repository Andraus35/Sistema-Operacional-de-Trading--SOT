<!-- GEN-1_REFERENCE | generation: GEN-1 | status: SUPERSEDED_BY=SPEC-002 | normative_authority: NONE | do_not_create_components_by_analogy: true | marked: 2026-09-26 -->
# Spec — Fibonacci Validator
<!-- Fonte: ENGENHARIA GERAL Doc04 §14 + Doc05 + ARIA §10 Skill1 | Versão 1.0 -->

---

## Missão

Validar geometricamente as hipóteses estruturais produzidas pelo Elliott Specialist,
medindo se as proporções de preço e tempo são coerentes com as relações de Fibonacci
esperadas para cada tipo de onda.
Responde: **"A geometria de Fibonacci confirma ou rejeita esta hipótese de Elliott?"**

---

## Escopo

Dentro do escopo:
- Validação de retrações, extensões e projeções de Fibonacci por tipo de onda
- Confluência de níveis entre múltiplos timeframes (H1 + H4 + D1 convergindo)
- Identificação do OTE (Optimal Trade Entry): zona 61.8%–78.6% do dealing range
- Canais de Elliott e proporcionalidade geométrica entre ondas
- Simetria estrutural e projeção de alvos por Fibonacci

Fora do escopo (Non-goals):
- Criar contagens de Elliott
- Gerar sinais operacionais isoladamente
- Análise de liquidez, BOS, CHoCH, OBs
- Definir bias direcional

---

## Comportamento esperado por situação

**Quando** receber hipótese Elliott, o agente DEVE verificar:
- Onda 2: retração 50%, 61.8% ou 76.4% da Onda 1
- Onda 3: extensão 161.8%, 261.8% ou 423.6% da Onda 1
- Onda 4: retração 38.2% ou 50% da Onda 3
- Onda 5: igualdade com Onda 1 ou 61.8% dela

**Quando** as proporções confirmarem a hipótese principal, o agente DEVE:
- Aumentar convicção geométrica da hipótese
- Reportar os níveis específicos confirmados

**Quando** as proporções violarem a hipótese principal, o agente DEVE:
- Reportar conflito geométrico com detalhes (qual nível violou, qual foi observado)
- NÃO DEVE descartar a hipótese sozinho — reporta ao Elliott Specialist
- Verificar se as proporções se encaixam melhor na hipótese alternativa

**Quando** múltiplos timeframes convergirem no mesmo nível de Fibonacci, o agente DEVE:
- Reportar confluência de zona (alta qualidade de suporte/resistência)
- Incluir a zona no output de nível chave

---

## Critérios de aceitação

O agente funcionou corretamente quando:
- Não cria contagens Elliott próprias
- Cada validação referencia explicitamente qual onda está sendo validada
- Conflitos geométricos são reportados sem descartar hipóteses unilateralmente
- OTE é calculado corretamente para o dealing range da sessão quando solicitado

---

## Inputs que recebe

Referência: `schemas/fibonacci.input.json`

- Hipótese Elliott com pivôs identificados (início/fim de cada onda)
- Preços OHLCV do Market Digital Twin por timeframe
- Dealing range da sessão corrente

## Outputs que entrega

Referência: `schemas/fibonacci.output.json`

- Status de validação por hipótese: confirmado / conflito / inconclusivo
- Níveis Fibonacci relevantes identificados (zona, tipo, timeframe de origem)
- Confluência de níveis (lista de zonas onde múltiplos TFs convergem)
- OTE se calculável: zona_low, zona_high (61.8%–78.6% do dealing range)
- Alvos projetados por onda (extensões e projeções)
- Score de convicção geométrica (0–100%)
