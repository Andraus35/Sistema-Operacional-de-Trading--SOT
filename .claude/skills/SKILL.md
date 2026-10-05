---
name: sot-harness-spec
description: >
  Referência mestre para especificação e validação do Harness Cognitivo SOT.
  Use quando: especificar um agente novo, aprofundar um spec existente,
  validar harness files para completude, conformidade constitucional e
  maturidade estrutural. Integra GEH-001 (arquitetura de agentes) e
  BASpec/D0-D9 (metodologia de especificação). Contém Quality Gates L1-L4,
  sequência de sprints e bloqueadores de decisão.
---

# SOT Harness — Referência Mestre de Especificação

<!-- Fontes: GEH-001 (Guia Agente Especificações e Harness) + Unidade Atômica SOT v1.0 -->
<!-- Hierarquia de autoridade: decisões homologadas → docs baselined → Kernel →
     Engenharia Geral → modelos canônicos → spec Harness → TLC Spec Driven →
     pesquisa externa → inferências do agente -->

---

## Parte 1 — Princípios de Arquitetura [GEH-001]

### 1.1 Os 4Es — Hierarquia inviolável de governança

```
0. Conformidade / invariantes do domínio   → pré-condição absoluta
1. Eficácia      → o resultado está correto? (medido contra spec/invariantes)
2. Efetividade   → gera valor real no tempo certo? (inclui latência)
3. Eficiência    → menor recurso por execução (subordinado a 1 e 2)
4. Economicidade → menor custo unitário de provisionamento de 3
```

**Máximas invioláveis:**
- "Eficiência sem Eficácia é desperdício disfarçado de economia."
- "Economicidade que compromete Eficiência vira falsa economia."
- "Nenhuma otimização de custo pode subir o degrau da hierarquia."
- "Um modelo mais rápido que gera análise incorreta é pior que um modelo lento que gera análise correta." [CEE-001]

### 1.2 Taxonomia ETCLOVG — Anatomia do harness

| Camada | Nome | O que cobre |
|---|---|---|
| E | Execution Environment | Sandbox, permissões, liveness |
| T | Tool Interface & Protocol | Function-calling, MCP, seleção de ferramentas |
| C | Context & Memory Management | Curto/médio/longo prazo, KV-cache |
| L | Lifecycle & Orchestration | Controle de fluxo, coordenação, pipelines |
| O | Observability | Tracing, custo, sinais de confiabilidade |
| V | Verification | Avaliação, atribuição de falha, testes |
| G | Governance | Permissões, audit trail, gates de aprovação |

**Princípio C (contexto):** contexto é recurso escasso. Dê ao modelo exatamente a
informação certa em cada passo — posição importa tanto quanto presença.

**Princípio T (ferramentas):** "menos ferramentas, porém melhores". Se você não
consegue explicar quando uma ferramenta se aplica, o modelo também não conseguirá.

### 1.3 Centralizar vs. Descentralizar

**Default: centralizar.** Um fluxo único, linear, com contexto compartilhado
resolve a maioria dos problemas sem o custo de 4-15× tokens dos sistemas multiagentes.

**Os 3 (e apenas 3) gatilhos legítimos para descentralizar:**

1. **Proteção de contexto** — subtarefa gera >1.000 tokens irrelevantes para o
   orquestrador E tem critério de extração claro (só a conclusão precisa voltar)
2. **Paralelização de facetas independentes** — domínios ou fontes distintas,
   genuinamente isoláveis, para leitura/análise em paralelo
3. **Especialização de ferramentas/persona** — >20 ferramentas, ou conjuntos
   conflitantes que degradariam uns aos outros

**O que NUNCA descentralizar:**
- Decisões de design que dependem de contexto compartilhado
- Tarefas de escrita/integração cujos resultados precisam de costura coerente
- Consenso, autoridade e declaração de decisão final
- Síntese final e arbitragem de conflitos

**Heurística leitura × escrita:**
```
Leitura / exploração / análise  →  descentralizável
Escrita / decisão / síntese / consenso  →  SEMPRE centralizado
```

**Checklist de topologia (gate obrigatório antes de qualquer decomposição):**
- [ ] O fluxo centralizado resolve? Se sim, NÃO adicione agentes
- [ ] Se contexto estoura, tentei compressor antes de fragmentar?
- [ ] Pelo menos 1 dos 3 gatilhos é satisfeito?
- [ ] As fronteiras são de contexto, não de fase?
- [ ] Toda escrita/decisão/síntese/consenso permanece centralizada?
- [ ] Há critério de aceitação claro para subagente verificador?

### 1.4 Padrão de ativação preguiçosa (lazy por evidência)

Para o SOT: não despertar etapas profundas sem evidência que as justifique.

```
Sinal detectado pelo Orchestrator
  → ativa Elliott Specialist (análise estrutural básica)
     → se convicção estrutural ≥ limiar → ativa Fibonacci Validator
        → se geometria confirma → ativa SMC Specialist
           → se estrutural+institucional convergem → ativa ICT Specialist
              → se condições de execução presentes → ativa Synthesis Agent
                 → se score≥7 + conv≥70% + R:R≥1:3 → gera TMP
```
*(score 7/9 e conv 70% = Fase Piloto, recalibráveis — Q-002; R:R = 1:3 — Q-004.)*

Isso materializa o CEE-001 Framework 4Es: eficiência/economicidade como consequência de eficácia,
nunca como atalho.

---

## Parte 2 — Metodologia de Especificação [UNIDADE-ATÔMICA-SOT]

### 2.1 Unidade atômica: BASpec (Behavioral Assertion Specification)

A BASpec é a unidade mínima indivisível de especificação do harness cognitivo SOT.
Ela torna o EARS notation plenamente rastreável e testável.

```
BASpec-[ID]:
  QUANDO: <condição observável e verificável>
  ENTÃO:  <comportamento específico e mensurável>
  PORQUE: <princípio ou regra que justifica>
  REFERÊNCIA: <RULE-XX, CONSTITUTION.md §Y, fonte>
  VERIFICADO POR: <cenário de teste com input e expected output>
```

**Exemplo canônico (BASpec-EW-001):**
```
BASpec-EW-001:
  QUANDO: Onda 3 medida resultar em comprimento < comprimento da Onda 1
  ENTÃO:  o agente DEVE descartar a contagem E reiniciar análise com
          novo conjunto de hipóteses E publicar motivo no Blackboard
          workspace "Observations"
  PORQUE: Regra imutável de Elliott — Onda 3 nunca é a mais curta
  REFERÊNCIA: RULE-EW-006, CONSTITUTION.md §Hierarquia metodológica
  VERIFICADO POR:
    DADO: onda1_length=100, onda3_length=80
    QUANDO: validar_contagem(w1=100, w3=80)
    ENTÃO: resultado = {status: DESCARTADO, motivo: "W3_SHORTER_THAN_W1",
           new_hypotheses: [...]}
```

**Regras de boa formação:**
- Cobre UMA condição observável (não múltiplas)
- Produz UM comportamento mensurável
- Mapeia para ≤2 RULES do RULES.md
- Testável com um único cenário input/output

### 2.2 Modelo de profundidade D0-D9

Escala adaptativa: o rigor deve ser proporcional ao impacto [PPQ-001].

| Nível | Nome | Pergunta respondida | Formato | Obrigatório para |
|---|---|---|---|---|
| D0 | Intenção | "O que este componente faz?" | Parágrafo 2-3 frases | Todos |
| D1 | Escopo | "O que está dentro e fora?" | Lista escopo + antiescopo | Todos |
| D2 | Regra nominal | "Que restrições existem?" | RULE-XX em EARS puro | Todos |
| D3 | Comportamental | "Em que situações age como?" | BASpec sem VERIFICADO POR | Agentes e motores |
| D4 | Algoritmo | "Exatamente como calcula?" | Fórmula, pseudocódigo, exemplos numéricos | Componentes det./semi-det. |
| D5 | Estado | "Quais estados e transições?" | Máquina de estados (tabela/diagrama) | Agentes stateful (P08) |
| D6 | Protocolo | "Em que ordem publica no Blackboard?" | Sequência com dependências | Todos os agentes |
| D7 | Teste | "Dado X, espera-se Y?" | BASpec completo com VERIFICADO POR | HIGH e CRITICAL |
| D8 | Adversarial | "O que deve ser rejeitado?" | Casos de falha esperada | CRITICAL |
| D9 | Auditoria | "Como reconstituir a decisão?" | Log schema + cadeia causal | Sistema completo (P13) |

### 2.3 Calibração por complexidade SOT

| Componente | Complexidade | Profundidade mínima |
|---|---|---|
| Conviction Engine | **CRITICAL** | D0-D8 |
| Elliott Specialist | **CRITICAL** | D0-D8 |
| Blackboard Protocol | **CRITICAL** | D0-D7 |
| Synthesis Agent | **HIGH** | D0-D7 |
| SMC Specialist | **HIGH** | D0-D6 |
| Event Bus (EC-COG-005) | **HIGH** | D0-D6 |
| ICT Specialist | **MEDIUM** | D0-D5 |
| Fibonacci Validator | **MEDIUM** | D0-D5 |
| Knowledge Graph (EC-COG-003) | **CRITICAL** | D0-D7 |
| Pattern Memory | **MEDIUM** | D0-D4 |
| Learning Governance (P12) | **LOW** | D0-D3 |

### 2.4 As 5 gramáticas normativas

**G1 — Normativa (D2):** para regras
```
RULE-XX: <sujeito> DEVE/NÃO DEVE/PODE <ação>
         [Fonte: documento §seção]
```

**G2 — Comportamental (D3):** para specs situacionais (EARS)
```
**Quando** <condição observável>, o agente DEVE <resposta>
```

**G3 — Operacional (D4):** para algoritmos
```
ALGORITMO: <nome>
  ENTRADA: <variáveis tipadas>
  PROCESSO:
    1. <passo com fórmula explícita>
    2. <passo com fórmula explícita>
  SAÍDA: <variável tipada + range válido>
  EXEMPLO: entrada={...} → saída={...}
```

**G4 — Cognitiva (D5):** para máquinas de estados
```
Estado: <NOME_ESTADO>
  → Transição para <OUTRO_ESTADO> quando <condição>
  → Emite <publicação_blackboard> ao entrar
  → Aguarda <evento> antes de transitar
```

**G5 — Avaliativa (D7):** para cenários de teste (Gherkin adaptado)
```
DADO: <estado inicial com valores concretos>
QUANDO: <evento ou input específico>
ENTÃO: <expected output com valores concretos>
VERIFICAÇÃO: campo_x = valor_esperado
```

### 2.5 Template mestre de spec

```markdown
# Spec — [Nome do Componente]
<!-- Fonte: [documentos fonte] | Versão: [X.Y] | Profundidade: D[nível] -->
<!-- Complexidade: CRITICAL | HIGH | MEDIUM | LOW -->

## Missão (D0) [OBRIGATÓRIO]
[2-3 frases. Qual pergunta este componente responde?]

## Escopo (D1) [OBRIGATÓRIO]
### Dentro do escopo
- [item]
### Fora do escopo (Non-goals)
- [item]

## Regras aplicáveis (D2) [OBRIGATÓRIO]
- RULE-XX: [texto resumido] [Fonte: §]

## Comportamento situacional (D3) [OBRIGATÓRIO]
**Quando** [condição observável], o agente DEVE:
- [ação 1]
- [ação 2]

## Algoritmo (D4) [OBRIGATÓRIO para HIGH/CRITICAL]
### Algoritmo: [nome]
**Entrada:** [variáveis tipadas]
**Processo:**
  1. [passo com fórmula]
**Saída:** [variável tipada + range]
**Exemplo:** entrada={...} → saída={...}

## Estados (D5) [OBRIGATÓRIO para agentes com P08]
| Estado | Descrição | Entra quando | Sai quando | Publica no Blackboard |
|---|---|---|---|---|
| IDLE | ... | ... | ... | nada |
| ANALYZING | ... | ... | ... | workspace/Observations |

## Protocolo de Blackboard (D6) [OBRIGATÓRIO para agentes]
Sequência de publicação:
1. [condição] → publica em [workspace] → mensagem: [schema]
Dependências: [aguarda workspace/X ter estado Y]

## Cenários de teste (D7) [OBRIGATÓRIO para HIGH/CRITICAL]
### Cenário [ID]-[nome]
**DADO:** [estado inicial com valores concretos]
**QUANDO:** [evento ou input]
**ENTÃO:** [expected output com valores concretos]
**VERIFICAÇÃO:** campo_x = valor_esperado

## Casos adversariais (D8) [OBRIGATÓRIO para CRITICAL]
### Adversarial [ID]-[nome]
**DADO:** [estado que deve ser rejeitado]
**QUANDO:** [evento]
**ENTÃO:** sistema DEVE rejeitar com: [erro específico]

## Auditabilidade (D9) [OPCIONAL — somente sistema completo]
[Como reconstituir esta decisão 48h depois]

## I/O
- Input: `schemas/[nome].input.json`
- Output: `schemas/[nome].output.json`
```

---

## Parte 3 — Etiquetagem obrigatória

Todo conteúdo novo produzido por agentes deve usar as etiquetas:

| Etiqueta | Significado |
|---|---|
| **[FONTE]** | Extraído diretamente de documento do projeto |
| **[INFERÊNCIA]** | Derivado por análise — pode estar errado |
| **[PROPOSTA]** | Novo conteúdo — requer homologação |
| **[DECISÃO NECESSÁRIA]** | Conflito ou lacuna — PARAR e reportar |
| **[EXTERNO]** | TLC Spec Driven, harness-score, pesquisa externa |

**Regra de conflito:** quando houver conflito entre fontes, NÃO resolver
silenciosamente. Registrar o conflito, explicar o impacto, marcar como
[DECISÃO NECESSÁRIA] e aguardar instrução.

---

## Parte 4 — Quality Gates L1-L4

### Gate L1 — Operacional (pré-requisito para qualquer implementação)

| Gate | Critério | Ferramenta |
|---|---|---|
| D0-PRESENT | Missão clara em ≤3 frases | lint-specs.js |
| D1-PRESENT | Antiescopo declarado explicitamente | lint-specs.js |
| D2-TRACED | Toda RULE tem fonte documentada | RULES.md review |
| D3-EARS | ≥3 situações em BASpec/EARS | lint-specs.js |
| SCHEMA-VALID | Schema JSON válido Draft-07 | validate-schemas.js |

### Gate L2 — Guiado (pré-requisito para integração entre agentes)

| Gate | Critério | Ferramenta |
|---|---|---|
| D4-ALGO | Algoritmos determinísticos com fórmula | review manual |
| D4-EXAMPLE | Exemplo numérico por algoritmo | review manual |
| CONFLICT-COVERED | Conflitos mapeados no CONFLICT-MAP.md | review |
| BLACKBOARD-PROTOCOL | Sequência de publicação no Blackboard definida | review manual |
| TRACK-A-CLEAN | 0 broken no harness-eval Track A | harness-eval |

### Gate L3 — Testável (pré-requisito para produção)

| Gate | Critério | Ferramenta |
|---|---|---|
| D5-STATE | State machine completa para agentes stateful (P08) | review manual |
| D7-SCENARIOS | ≥3 cenários DADO/QUANDO/ENTÃO com valores concretos | harness-eval |
| D8-ADVERSARIAL | ≥2 casos de falha esperada | harness-eval |
| REVIEW-INDEP | Revisão por revisor diferente do autor | processo |
| SCORE-L3 | harness-score ≥ L3 | harness-score |

### Gate L4 — Expert (pré-requisito para autonomia completa)

| Gate | Critério | Ferramenta |
|---|---|---|
| D9-AUDIT | Reconstrução de decisão pós-hoc possível | review manual |
| SENSORS-60 | Sensors dimension ≥ 60% no harness-score | harness-score |
| FULL-COVERAGE | Todas as colunas da Matriz de Cobertura preenchidas | coverage matrix |
| P12-COMPLETE | Ciclo P12 completo (backtest + sandbox + aprovação) | processo |

---

## Parte 5 — Decisões necessárias (BLOQUEANTES)

Quando um agente encontrar qualquer uma destas questões abertas, DEVE parar,
marcar como **[DECISÃO NECESSÁRIA]** e aguardar instrução. Nunca resolver autonomamente.

| ID | Questão | Impacto se resolvida incorretamente |
|---|---|---|
| **J-001** | Fórmula exata do Conviction Vector | Bloqueia toda implementação de qualidade de sinal |
| ~~**B-001**~~ | **FECHADA (Q-007)** + parcialmente SUPERSEDIDA por ADR-MANAGER-001 (DHR-ARQ-001, 2026-10-01): não é mais pergunta aberta. "Conviction Engine" = mecanismo (Classe D/H do CCM-001) invocado pelo Manager Agent — Fase 2; separação lógica de etapas preservada; dim.=8 | Resolvida — não bloqueia |
| **G-001** | Schema do estado persistente por agente | Determina InferenceContextEnvelope e cache |
| **H-001** | Knowledge Graph: grafo real ou estrutura de dados? | Determina toda a spec EC-COG-003 |
| **I-001** | Skills são unidades formais separadas dos Engines? | Determina granularidade de specs e testes |
| **K-001** | Ciclo P12: quem, critérios e artefatos por etapa? | Determina como o sistema aprende e evolui |
| **L-001** | Processo de governança do próprio harness? | Determina como specs são propostas/aprovadas |

---

## Parte 6 — Sequência recomendada de sprints

### Sprint 1 — P0 Blockers (especificar primeiro)

| Ação | Componente | Profundidade | Motivo |
|---|---|---|---|
| Decidir fórmula Conviction Vector (J-001) | Conviction Engine | D4 | GAP-003 — bloqueia qualidade de todo sinal |
| Criar schema Blackboard message | Blackboard | D4+D6 | GAP-007 — bloqueia protocolos inter-agente |
| ~~Resolver B-001 (CE vs. SA)~~ — **RESOLVIDA** (Q-007 + DHR-ARQ-001): Conviction Engine = mecanismo invocado pelo Manager Fase 2 | Manager Agent — Fase 2 (SPEC-015) / mecanismo CCM-001 (SPEC-003) | — | Não é mais pendência estrutural |

### Sprint 2 — P1 Agentes críticos

| Ação | Componente | Profundidade | Motivo |
|---|---|---|---|
| State machine Elliott Specialist | Elliott | D5 | Estado mais complexo: multi-timeframe histórico |
| Protocolo Blackboard Elliott | Elliott | D6 | Primeiro na cadeia — define padrão para outros |
| Algoritmo Synthesis Agent (D4) | Synthesis | D4 | Expande CHUNK-SY-004 para fórmula formal |
| ≥3 test scenarios por agente crítico | Elliott, Synthesis, SMC | D7 | Habilitam harness-eval Track B/C |

### Sprint 3 — P2 Infraestrutura cognitiva

| Ação | Componente | Profundidade | Motivo |
|---|---|---|---|
| Event Bus schema (EC-COG-005) | Event Bus | D0-D6 | GAP-006 — coordenação de agentes |
| Pattern Memory schema formal | Pattern Memory | D0-D4 | Dimensão histórica da convicção |
| State machines ICT, SMC | ICT, SMC | D5 | Completude operacional |

### Sprint 4 — P3 Maturidade

| Ação | Componente | Profundidade | Motivo |
|---|---|---|---|
| Knowledge Graph spec (EC-COG-003) | KG | D0-D5 | Memória relacional de longo prazo |
| Casos adversariais D8 | Elliott, Synthesis | D8 | L4 harness-score |
| Learning Governance workflow (P12) | Processo | D3 | Formaliza o ciclo de evolução |
| Sensores CI (eslint, tsconfig, prettier) | CI | — | Sensors ≥ 60% → L3 harness-score |

---

## Parte 7 — Validação do harness (PRESERVADO)

### Trigger de validação

Use os passos abaixo quando:
- Um spec file em specs/ for modificado
- Um schema file em schemas/ for modificado
- Um RAG file em rag/ for modificado
- Antes de qualquer commit ou PR afetando harness files
- Ao completar qualquer Sprint acima

### Passos de validação

1. **Validar JSON schemas**: `node tests/validate-schemas.js` — todos os schemas devem passar
2. **Lint specs**: `node tests/lint-specs.js` — todos os 5 specs devem passar EARS + sections
3. **Verificar pipeline cross-agente:**
   - elliott-wave.output campos referenciados em fibonacci.input
   - fibonacci.output campos referenciados em smc.input
   - smc.output + todos os outputs referenciados em synthesis.input
   - ict.input `approved_hypothesis` permite null (ICT INACTIVE state)
4. **Verificar guards constitucionais:** para cada spec:
   - ICT spec: regra INACTIVE como primeiro comportamento
   - Synthesis spec: 4 condições de sinal presentes (score≥7, R:R≥1:3, conviction≥70%, sem conflito) — 7/9 e 70% = Fase Piloto (Q-002)
   - Nenhum agente de camada inferior sobrepõe camada superior
5. **Rodar harness-score**: `npx harness-score` — manter L2 ou superior

### Critérios de PASS

- Todos os JSON schemas: JSON válido, têm $schema/$id/title/type, output schemas têm campo score
- Todos os specs: têm seções Missão/Escopo/Comportamento/Critérios e notação EARS
- Harness score: L2 mínimo (85+ pontos na versão atual)
- Harness-eval Track A: 0 broken

---

## Parte 8 — Matriz de cobertura atual (referência)

Estado em 2026-09-09 (harness-score L2, 85/108):

| Componente | D2 Norm | D3 EARS | D4 Algo | D5 Estado | D6 Proto | D7 Teste | D8 Adv |
|---|---|---|---|---|---|---|---|
| Elliott Specialist | ✓ | ✓ | △ | ✗ | ✗ | ✗ | ✗ |
| Fibonacci Validator | ✓ | ✓ | △ | N/A | ✗ | ✗ | ✗ |
| SMC Specialist | ✓ | ✓ | △ | ✗ | ✗ | ✗ | ✗ |
| ICT Specialist | ✓ | ✓ | △ | N/A | ✗ | ✗ | ✗ |
| Synthesis Agent | ✓ | ✓ | **✗** | ✗ | ✗ | ✗ | ✗ |
| Conviction Engine | △ | △ | **✗** | ✗ | N/A | ✗ | ✗ |
| Blackboard Protocol | △ | △ | ✗ | ✗ | **✗** | ✗ | ✗ |
| Event Bus | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Knowledge Graph | ✗ | ✗ | ✗ | N/A | ✗ | ✗ | ✗ |
| Pattern Memory | △ | ✗ | ✗ | N/A | N/A | ✗ | ✗ |

✓ completo | △ parcial | ✗ ausente | N/A não aplicável | **✗** crítico ausente

---

## Parte 9 — Critério de "pronto" por nível

### L1 — Pronto para desenvolvimento
- [ ] Missão clara em ≤3 frases (D0)
- [ ] Antiescopo declarado explicitamente (D1)
- [ ] ≥3 situações em BASpec/EARS (D3)
- [ ] Toda RULE referenciada existe em RULES.md
- [ ] Schema de I/O referenciado e validado
- [ ] `lint-specs.js` PASS + `validate-schemas.js` PASS

### L2 — Pronto para integração
- [ ] Todos os algoritmos determinísticos têm fórmula (D4)
- [ ] Exemplo numérico por algoritmo
- [ ] Protocolo de Blackboard definido (D6)
- [ ] Conflitos mapeados no CONFLICT-MAP.md
- [ ] harness-eval Track A: 0 broken

### L3 — Pronto para produção
- [ ] State machine completa para componentes stateful (D5)
- [ ] ≥3 cenários de teste com input/output concreto (D7)
- [ ] ≥1 caso adversarial (D8)
- [ ] Revisão independente (revisor ≠ autor)
- [ ] harness-score: componente contribui para L3

### L4 — Pronto para autonomia
- [ ] ≥2 casos adversariais (D8)
- [ ] Auditabilidade spec'd (D9)
- [ ] Ciclo P12 completo (backtest + sandbox + aprovação)
- [ ] Aprovação de Andraus registrada como "decisão homologada"
