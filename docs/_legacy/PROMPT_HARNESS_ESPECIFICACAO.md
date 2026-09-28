# Prompt — Elaboração do Harness de Especificação do Sistema SOT

> Cole no Claude Code Desktop apontando para a pasta do projeto de trading.
> 
> Objetivo: construir um harness de especificação — um processo estruturado
> que analisa a documentação existente, extrai o que é tecnicamente útil,
> e o transforma em especificações no formato correto para qualquer sistema
> agentico (Claude Code, OpenAI Agents, LangGraph, CrewAI, AutoGen etc).
>
> O produto final não é o sistema de trading em si.
> É a especificação técnica completa que permite construí-lo corretamente.

---

## CONTEXTO — O QUE EXISTE E O QUE SE QUER

### O que existe em disco

Uma coleção de documentos de engenharia do sistema SOT (Sistema de Operações
e Tendências) para análise de Bitcoin com múltiplos agentes especialistas:

- `ENGENHARIA_GERAL.pdf` — filosofia, princípios arquiteturais, hierarquia
  metodológica (Elliott → Fibonacci → SMC → ICT), modelo cognitivo
- `KERNEL_V2_docx.pdf` — domínios arquiteturais, Engineering Cards, Design
  Patterns cognitivos, mapa de dependências
- `CEE-001_Versao_Consolidada.md` — economia cognitiva, roteamento por
  complexidade, framework 3E (Eficácia, Eficiência, Efetividade)
- `GMC-001_Versao_Consolidada.md` — governança de modelos canônicos,
  estrutura de papéis (Estrategista/Analista/Controlador)
- `PPQ-001_Versao_Consolidada-1.md` — gestão de projetos, RACI, Stage-Gate,
  critérios de qualidade
- `SDD-001_Versao_Consolidada.md` — protocolo Spec-Driven Development,
  separação Spec/Plan/Tasks, Constitution Check
- `ARIA_Plano_Mestre.md` — especificação operacional do sistema: scoring
  matrix, schemas de webhook TradingView, position sizing, killzones ICT,
  templates de alerta — o documento mais operacionalmente útil do conjunto

### O que se quer produzir

Um **harness de especificação** com 6 saídas formais:

1. **SPEC principal** — descrição comportamental completa de cada agente
   (o quê faz, não como faz), escrita em linguagem que qualquer LLM entende
   sem ambiguidade

2. **SCHEMAS de I/O** — contratos JSON formais de input e output de cada
   agente, incluindo campos obrigatórios, tipos, enums e validações

3. **RAG por agente** — base de conhecimento específica de cada especialista,
   estruturada para retrieval: chunks temáticos com metadados, ordenados por
   prioridade de consulta

4. **RULES** — conjunto de regras negativas e positivas em formato de
   assertions verificáveis (o que SEMPRE acontece, o que NUNCA acontece)

5. **CONFLICT MAP** — mapa explícito de todos os conflitos possíveis entre
   agentes e a regra de resolução de cada um

6. **CONSTITUTION** — arquivo único que qualquer framework agentico lê como
   ponto de entrada: hierarquia, princípios invioláveis, sequência de execução

---

## PARTE 1 — INVENTÁRIO E CLASSIFICAÇÃO

### Tarefa 1.1 — Ler todos os documentos

Leia cada documento usando as ferramentas disponíveis. Para PDFs, use
`pdftotext`. Para MDs, leia diretamente. Não assuma o conteúdo — leia.

### Tarefa 1.2 — Classificar cada trecho encontrado

Para cada seção de cada documento, classifique em uma das categorias:

```
CATEGORIA SP — Spec-level (comportamento, princípios, filosofia)
  → vai para SPEC principal e CONSTITUTION
  → exemplos: hierarquia metodológica, modelo de detetive, convicção vs score

CATEGORIA SC — Schema-level (estrutura de dados, campos, contratos)
  → vai para SCHEMAS de I/O
  → exemplos: campos do payload TradingView, estrutura do alerta, scoring matrix

CATEGORIA RG — RAG-level (conhecimento técnico de domínio)
  → vai para base RAG de cada agente
  → exemplos: regras de Elliott, níveis Fibonacci por onda, killzones ICT,
    tipos de Order Block válidos, condições de FVG

CATEGORIA RL — Rules-level (assertions verificáveis)
  → vai para RULES
  → exemplos: "Onda 4 nunca invade Onda 1", "ICT nunca opera sem Elliott",
    "convicção global < 70% bloqueia sinal"

CATEGORIA CF — Conflict-level (conflitos e resoluções)
  → vai para CONFLICT MAP
  → exemplos: Elliott bearish vs SMC bullish, Fibonacci invalida contagem

CATEGORIA GO — Governance-only (processo interno, burocracia administrativa)
  → DESCARTAR para o harness de especificação
  → exemplos: RACI, Stage-Gate, versionamento de documentos, fluxo de aprovação
    de Engineering Cards, critérios de aceitação de documentos
```

Produza a tabela de classificação:

| Documento | Seção/Trecho | Categoria | Destino |
|---|---|---|---|
| ENGENHARIA_GERAL | Hierarquia Elliott→Fibonacci→SMC→ICT | SP | CONSTITUTION |
| ENGENHARIA_GERAL | Modelo do detetive (refutação vs confirmação) | SP | SPEC |
| ... | ... | ... | ... |

**Tudo que cair em GO não aparece mais no harness.**

---

## PARTE 2 — PRODUZIR AS 6 SAÍDAS

### Saída 1 — CONSTITUTION.md

O arquivo que qualquer framework lê primeiro. Máximo de 200 linhas.
Deve conter apenas o que é universal para TODOS os agentes do sistema.

Estrutura obrigatória:

```markdown
# SOT Constitution — Sistema de Operações e Tendências

## Missão do sistema
[Uma frase. O que o sistema faz e para quem.]

## Hierarquia metodológica inviolável
[A sequência exata com o papel de cada metodologia.
Extraído de ENGENHARIA_GERAL.]

## Princípios cognitivos universais
[Cada princípio em uma linha, como assertion.
Ex: "O sistema mantém múltiplas hipóteses concorrentes — nunca uma única."]

## Sequência de execução dos agentes
[Ordem obrigatória com o que cada agente recebe e entrega.]

## O que nenhum agente faz
[Assertions negativas universais. O que é estruturalmente impossível.]

## Definições canônicas
[Glossário mínimo: convicção, hipótese, evidência, bias, invalidador.
Baseado em ENGENHARIA_GERAL e KERNEL_V2.]
```

---

### Saída 2 — SPECS/ (um arquivo por agente)

Produza `specs/[nome-agente].spec.md` para cada agente:
- `elliott-wave.spec.md`
- `fibonacci.spec.md`
- `smc.spec.md`
- `ict.spec.md`
- `synthesis.spec.md`

Cada spec usa este template (baseado em SDD-001 §3.1):

```markdown
# Spec — [Nome do Agente]

## Missão
[O que este agente faz, em linguagem comportamental.
SEM mencionar modelos de IA, algoritmos ou estruturas de dados.]

## Escopo
Dentro do escopo:
- [lista]

Fora do escopo (Non-goals):
- [lista — especialmente o que o agente vizinho faz]

## Comportamento esperado por situação
[Casos de uso e casos de borda em notação EARS:
"Quando <condição>, o agente DEVE <resposta>."
"Quando <condição>, o agente NÃO DEVE <resposta>."]

## Critérios de aceitação
[Condições verificáveis de que o agente funcionou corretamente.
Em notação EARS.]

## Inputs que recebe
[O que este agente precisa para funcionar — referenciando Saída 3 (schemas).]

## Outputs que entrega
[O que este agente produz — referenciando Saída 3 (schemas).]
```

---

### Saída 3 — SCHEMAS/ (JSON Schema por agente)

Produza `schemas/[nome-agente].input.json` e `schemas/[nome-agente].output.json`
para cada agente.

Para cada schema, extraia campos de:
- `ARIA_Plano_Mestre.md` — payloads TradingView, formato de alerta, campos operacionais
- `ENGENHARIA_GERAL` — campos cognitivos (convicção, hipótese, bias)
- `KERNEL_V2` — contratos do Cognitive Core

Formato JSON Schema Draft-07. Campos obrigatórios marcados em `required`.
Enums para valores discretos. `description` em português em cada campo.

Exemplo mínimo para `synthesis.output.json`:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "title": "SynthesisOutput",
  "type": "object",
  "required": ["sinal", "convicção_global", "narrativa"],
  "properties": {
    "sinal": {
      "type": "string",
      "enum": ["COMPRA", "VENDA", "NEUTRO", "AGUARDAR_SETUP"],
      "description": "Decisão operacional do sistema"
    },
    "convicção_global": {
      "type": "number",
      "minimum": 0,
      "maximum": 100,
      "description": "Convicção agregada. Sinal operacional requer >= 70."
    }
  }
}
```

---

### Saída 4 — RAG/ (base de conhecimento por agente)

Produza `rag/[nome-agente].knowledge.md` para cada agente especialista
(não para o synthesis — ele arbittra, não tem domínio próprio).

Cada arquivo RAG é uma base de conhecimento estruturada para retrieval.
**Não é um prompt. É uma biblioteca que o agente consulta.**

Estrutura de cada chunk RAG:

```markdown
---
chunk_id: [agente]-[topico]-[numero]
agente: [nome]
topico: [categoria do conhecimento]
prioridade: alta | média | baixa
quando_consultar: [situação que ativa este chunk]
---

[Conteúdo técnico específico do domínio.
Extraído dos PDFs e MDs. Sem paráfrase quando a precisão importa.]
```

Exemplos de chunks para `rag/elliott-wave.knowledge.md`:

```markdown
---
chunk_id: elliott-regras-basicas-001
agente: elliott-specialist
topico: regras-imutaveis
prioridade: alta
quando_consultar: sempre — toda análise de ondas
---

Regras de Elliott que nunca podem ser violadas:
1. Onda 2 nunca retorna além do início da Onda 1
2. Onda 3 nunca é a mais curta entre ondas 1, 3 e 5
3. Onda 4 nunca entra no território de preço da Onda 1

Se qualquer regra for violada, a contagem está errada.
A contagem deve ser descartada e reiniciada.
```

```markdown
---
chunk_id: elliott-fibonacci-relacoes-001
agente: elliott-specialist
topico: proporcoes-fibonacci
prioridade: alta
quando_consultar: ao validar extensão ou retração de qualquer onda
---

Relações Fibonacci esperadas por tipo de onda:
- Onda 2: retração de 50%, 61.8% ou 76.4% da Onda 1
- Onda 3: extensão de 161.8%, 261.8% ou 423.6% da Onda 1
- Onda 4: retração de 38.2% ou 50% da Onda 3
- Onda 5: igualdade com Onda 1 ou 61.8% dela
[extraído de ARIA_Plano_Mestre.md §X e ENGENHARIA_GERAL §Y]
```

Para cada agente, produza mínimo de 10 chunks cobrindo:
- Regras imutáveis do domínio
- Casos especiais e exceções
- Condições de invalidação
- Relações com outros agentes
- Comportamento em condições adversas (mercado lateral, alta volatilidade)

---

### Saída 5 — RULES.md (assertions verificáveis)

Um único arquivo com todas as regras do sistema em formato assertion.

Estrutura:

```markdown
# Rules — Sistema SOT

## Regras universais (violação = falha do sistema)

RULE-001: Elliott DEVE ser consultado antes de qualquer outro especialista
RULE-002: ICT NÃO DEVE emitir setup sem confirmação de Elliott
RULE-003: Convicção global < 70 NÃO DEVE produzir sinal COMPRA ou VENDA
RULE-004: Evidências causalmente relacionadas DEVEM ser contadas como uma
RULE-005: Sinal COMPRA ou VENDA com conflito direcional aberto é INVÁLIDO

## Regras por agente

### Elliott Specialist
RULE-EW-001: DEVE manter mínimo de 2 hipóteses concorrentes enquanto mercado não decidir
RULE-EW-002: NÃO DEVE emitir bias com convicção < 60%
[...]

### Fibonacci Specialist
RULE-FB-001: NÃO DEVE criar contagens Elliott — apenas validar as recebidas
[...]

### SMC Specialist
RULE-SM-001: NÃO DEVE considerar Order Block mitigado como zona ativa
RULE-SM-002: NÃO DEVE sobrepor decisão de Elliott com leitura SMC
[...]

### ICT Specialist
RULE-ICT-001: NÃO DEVE operar sem killzone ativa sem registrar risco elevado
RULE-ICT-002: NÃO DEVE aceitar RR < 2:1
[...]

### Synthesis Agent
RULE-SY-001: Elliott tem veto sobre direção — conflito Elliott×SMC = NEUTRO
RULE-SY-002: NÃO DEVE resolver conflito favorecendo SMC sobre Elliott
[...]

## Regras de mercado lateral

RULE-LAT-001: Sem hipótese Elliott com convicção > 50% = sistema retorna NEUTRO
RULE-LAT-002: Range > 5 candles Daily = todos agentes retornam AGUARDAR_SETUP
```

---

### Saída 6 — CONFLICT-MAP.md

Mapa exaustivo de todos os conflitos possíveis entre agentes e resolução.

Estrutura:

```markdown
# Conflict Map — Sistema SOT

## Conflitos direcionais

| Situação | Elliott | SMC | Fibonacci | Resolução | Autoridade |
|----------|---------|-----|-----------|-----------|------------|
| Divergência direcional E×S | Bullish | Bearish | — | NEUTRO | Elliott (veto) |
| Fibonacci invalida Elliott | — | — | Invalida contagem | Elliott recontar | Fibonacci |
| SMC CHoCH contra Elliott | Bullish | CHoCH down | — | Registra conflito, não bloqueia | Synthesis |

## Conflitos de timing

| Situação | ICT | Resolução |
|----------|-----|-----------|
| Setup válido fora de killzone | AGUARDAR_SETUP | ICT registra risco elevado |
| Killzone ativa sem setup | AGUARDAR_SETUP | ICT aguarda displacement |

## Conflitos de convicção

| Situação | Resolução |
|----------|-----------|
| Convicção global entre 60-70 | AGUARDAR_SETUP — não bloqueia, não sinaliza |
| Convicção global < 60 | NEUTRO |
| Hipótese única Elliott com convicção > 80 + tudo alinhado | COMPRA/VENDA válido |

## O que é impossível por definição

- Sinal COMPRA ou VENDA com convicção global < 70: impossível
- ICT emitindo setup com Elliott em NEUTRO: impossível
- SMC sobrepondo direção Elliott: impossível
- Duas evidências causalmente relacionadas contando como independentes: impossível
```

---

## PARTE 3 — VALIDAÇÃO CRUZADA

Após produzir as 6 saídas, execute a validação:

### 3.1 Todo comportamento descrito em SPEC tem schema correspondente?

Para cada campo mencionado nas SPECs, verificar se existe no SCHEMA.
Campos mencionados sem schema = gap a completar.

### 3.2 Todo chunk RAG tem ao menos uma RULE associada?

O conhecimento do RAG deve se traduzir em regras verificáveis.
RAG sem RULE correspondente = conhecimento não enforçado.

### 3.3 Todo conflito no CONFLICT-MAP está coberto por uma RULE?

Conflito sem RULE = resolução não automática = decisão humana necessária.
Listar os que ficaram sem cobertura de RULE.

### 3.4 A CONSTITUTION cobre todos os princípios das SPECs?

Nenhum princípio que aparece em uma SPEC deve estar ausente da CONSTITUTION.

---

## PARTE 4 — RELATÓRIO FINAL

Produza `HARNESS-REPORT.md` com:

### 4.1 O que foi aproveitado de cada documento

| Documento | Categorias encontradas | % aproveitado | % descartado |
|-----------|----------------------|---------------|--------------|

### 4.2 Gaps identificados

O que estava nos documentos mas não havia especificação suficiente para
transformar em SPEC, SCHEMA ou RULE. Lista com recomendação de onde buscar.

### 4.3 O que precisa ser especificado ainda

Componentes do sistema que os documentos mencionam mas não detalham
o suficiente para produzir spec de qualidade. Exemplos prováveis:
- Detalhes do RAG de cada agente (como o agente consulta o RAG)
- Formato de persistência do modelo interno de mercado
- Protocolo de atualização incremental do Knowledge Graph
- Regras de aprendizado comportamental por ativo

### 4.4 Próximos passos recomendados

Em ordem de prioridade: o que especificar primeiro para o sistema ser
implementável mais rapidamente.

---

## REGRAS DE EXECUÇÃO

- Ler cada documento antes de classificar — não assumir conteúdo pelo título
- Cada chunk RAG deve citar o documento e seção de origem
- Cada RULE deve ser verificável: ou é verdade ou é falsa — sem ambiguidade
- Se um trecho for ambíguo demais para virar RULE, vai para RAG
- Não inventar comportamento não descrito nos documentos — registrar como gap
- Ao terminar cada Parte, reportar antes de avançar para a próxima
- Ao terminar tudo, aguardar instrução de Andraus
