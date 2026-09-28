# Alinhamento de Taxonomia e Workflow do SOT

<!--
Status: [PROPOSTA] de consolidação documental
Autoridade: ROADMAP.md + ATOMIC-SPEC.md + GLOSSARIO.md + governance/
Escopo: especificação de agentes, harness e workflows; não implementação de software
-->

## 1. Finalidade e autoridade

Este documento é o índice de alinhamento para `docs/fundamentos`. Ele resolve a
ambiguidade causada pela migração de uma documentação histórica de produto/software
para um Harness Cognitivo spec-driven.

A autoridade é, nesta ordem:

1. decisões homologadas e emendas homologadas;
2. `governance/`;
3. modelos canônicos baselined em `canon/`;
4. [ROADMAP.md](../../ROADMAP.md);
5. [ATOMIC-SPEC.md](../../ATOMIC-SPEC.md);
6. este documento;
7. fundamentos históricos, propostas e auditorias.

Quando houver conflito, o texto histórico não é corrigido silenciosamente: ele é
classificado como legado e a decisão vigente é registrada aqui ou no documento
normativo apropriado.

## 2. Mudança de paradigma

### 2.1 O que o SOT especifica

O SOT especifica:

- agentes cognitivos especializados;
- engines determinísticos ou semideterminísticos;
- protocolos de Blackboard/Event Bus quando homologados;
- artefatos cognitivos e contratos de entrada/saída;
- estados, transições, gates, evidências, hipóteses e decisões;
- workflows de análise, verificação, governança e evolução;
- BASpecs D0–D9, cenários e casos adversariais.

### 2.2 O que não é objeto desta fase

Não fazem parte desta fase:

- criação de aplicação, API, banco de dados ou servidor;
- escolha de stack (`FastAPI`, `SQLite`, webhook, Telegram, Playwright etc.);
- implementação de bot de execução;
- deploy, monitoramento de infraestrutura ou integração operacional;
- tratar um plano de software histórico como autorização de construção.

Esses elementos, quando aparecerem nos fundamentos, devem ser lidos como
**[FONTE] histórica** ou **[INFERÊNCIA]**, nunca como requisito vigente.

## 3. Taxonomia canônica

### 3.1 Camadas funcionais do harness

| Camada | Função | Exemplos canônicos |
|---|---|---|
| F.1 Feedforward | Orienta e previne | Constituição, RULES, CONFLICT-MAP |
| F.2 Guardrails | Bloqueia efeito inválido em tempo real | gates e salvaguardas |
| F.3 Feedback | Detecta falha depois da produção | lint, schemas, validações |
| F.4 Evaluation | Mede a qualidade do harness | harness-eval, harness-score |

Detector não é gate: somente um mecanismo com autoridade sobre o efeito pode
bloqueá-lo.

### 3.2 Componentes cognitivos

| Classe | Termos vigentes | Responsabilidade |
|---|---|---|
| Agente | Elliott Specialist | Cria a hipótese PRIMARY e produz evidência estrutural |
| Agente | Fibonacci Validator | Produz validação geométrica e SUB quando aplicável |
| Agente | SMC Specialist | Produz evidência institucional e SUB quando aplicável |
| Agente | ICT Specialist | Avalia execução/timing; não cria hipótese |
| Agente | Synthesis Agent | Arbitra a decisão de síntese e produz TMP interno |
| Engine | Fusion Engine | Funde evidências em Evidência DERIVED |
| Engine | Conviction Engine | Calcula o Conviction Vector de 8 dimensões |
| Substrato | Blackboard / Event Bus | Coordenação e estado, conforme a Spec autorizada |
| Camada futura | Risk Agent | Recebe TMP e pertence ao escopo de risco, não ao runtime já implementado |

`Structural Agent`, `Institutional Agent` e `Execution Agent` são nomes
históricos/legados. O mapeamento de leitura é, respectivamente,
`Elliott Specialist`, `SMC Specialist` e `ICT Specialist`; não são componentes
adicionais.

`Master Agent`, `Master Orchestrator`, `Decision Orchestrator`, `Mission Engine`
e `Cognitive Scheduler` não são componentes canônicos homologados. Podem aparecer
em fontes históricas, mas não devem ser criados como novos agentes por analogia.
Uma função de coordenação só pode ser especificada por uma Spec autorizada.

### 3.3 Artefatos e fronteiras

| Artefato | Papel vigente |
|---|---|
| Hipótese PRIMARY | Hipótese direcional criada exclusivamente pelo Elliott Specialist |
| Hipótese SUB | Sub-hipótese de SMC/Fibonacci, com `parent_id`; ICT não cria hipótese |
| Evidência | Observação objetiva produzida por agente |
| Evidência DERIVED | Resultado do Fusion Engine |
| Conviction Vector | Vetor de 8 dimensões; fórmula/pesos definitivos permanecem em J-001 |
| TMP | Handoff interno da Síntese para a camada Risk |
| Signal Package | Único artefato de fronteira SOT → Bot Trade Finance |

O SOT não executa ordens. `TMP` e `Signal Package` não são sinônimos.

### 3.4 Termos que não devem ser usados como substitutos

- `score 0–9` não substitui o Conviction Vector;
- `confiança`, `convicção`, `score` e `evidência` não são sinônimos;
- `agente`, `engine`, `skill`, `gate`, `detector` e `artefato` são classes distintas;
- `Blackboard` e `Event Bus` não são automaticamente o mesmo objeto;
- estado do agente não é estado da hipótese.

## 4. Workflow canônico

### 4.1 Workflow de especificação (vigente agora)

```text
Ler ROADMAP.md + ATOMIC-SPEC.md
  → confirmar Spec autorizada e decisões abertas
  → pesquisar fontes e baselines
  → SPECIFY: BASpecs, D0–D3, rastreabilidade
  → DESIGN: D4–D6, schemas e Enforcement Contract quando aplicável
  → TASKS: cenários D7 e adversariais D8 quando exigidos
  → VERIFY: schemas, lint, harness-eval e harness-score
  → Revisor independente
  → Homologação de Andraus
  → registrar baseline
  → iniciar próxima Spec autorizada
```

`BUILD` de software está adiado. O verificador da skill é feedback e não substitui
Revisor ou homologação.

### 4.2 Workflow cognitivo de análise (alvo a especificar)

```text
Orquestração autorizada detecta contexto
  → Elliott Specialist produz/atualiza hipótese PRIMARY
  → Fibonacci Validator valida geometria, se acionado
  → SMC Specialist produz evidência institucional/SUB, se acionado
  → ICT Specialist avalia condições operacionais, se acionado
  → Fusion Engine produz Evidência DERIVED
  → Conviction Engine calcula Conviction Vector
  → Synthesis Agent arbitra
  → somente com score ≥ 7/9, convicção ≥ 70%, R:R ≥ 1:3 e sem conflito
  → produz TMP interno; Signal Package somente na fronteira autorizada
```

Este fluxo é uma **[PROPOSTA] operacional derivada** do baseline. A ordem exata,
estados persistentes, schemas e autoridade de coordenação só se tornam normativos
nas Specs correspondentes. Não criar um “Master Agent” para preencher essa lacuna.

### 4.3 Workflow de evolução do harness

```text
observar falha ou lacuna
  → registrar evidência sem apagar histórico
  → abrir proposta/decisão necessária
  → atualizar Spec ou regra pela cadeia Especificador → Revisor → Andraus
  → validar impacto em schemas, dependências e decisões abertas
  → homologar e versionar monotonicamente
```

## 5. Classificação dos fundamentos históricos

| Arquivo | Classificação | Regra de leitura |
|---|---|---|
| `KERNEL-V2.md` | [FONTE] histórica / [PROPOSTA] | catálogo de ideias; não autoriza implementação |
| `ENGENHARIA-GERAL.md` | [FONTE] histórica / [PROPOSTA] | narrativa arquitetural; aplicar este alinhamento |
| `ARIA-plano-mestre.md` | [FONTE] histórica de produto/software | não é plano de execução vigente |
| `AUDITORIA-ideias-nao-implementadas.md` | [FONTE] diagnóstica | backlog de perguntas; não norma |
| arquivos do Inquérito SOT | [FONTE] de auditoria | evidência de inconsistências; não baseline |

Os arquivos permanecem para rastreabilidade. Nenhuma proposta neles altera
silenciosamente o baseline.

## 6. Decisões que continuam abertas

Este alinhamento não fecha decisões reservadas a Andraus, incluindo J-001, G-001,
H-001, I-001, K-001, M-001 e N-001. Onde a documentação histórica exigir uma
escolha sobre essas questões, marcar **[DECISÃO NECESSÁRIA]** e encaminhar para a
Spec/decisão indicada no [ROADMAP.md](../../ROADMAP.md).

## 7. Critério de aceitação documental

Um fundamento está alinhado quando:

- identifica explicitamente seu status epistemológico;
- não apresenta software como trabalho vigente;
- usa a taxonomia da seção 3 ou marca o termo como legado;
- separa workflow de especificação, workflow cognitivo e evolução;
- distingue TMP de Signal Package;
- não fecha decisão aberta por inferência;
- aponta para este documento e para as fontes de autoridade.

