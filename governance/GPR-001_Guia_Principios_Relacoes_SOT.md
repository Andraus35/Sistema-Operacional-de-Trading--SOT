# GPR-001 — Guia de Princípios, Relações e Organicidade do SOT

| Campo | Valor |
|---|---|
| Código | GPR-001 |
| Versão | 1.0 — BASELINE |
| Status | **HOMOLOGADO — BASELINE** (Andraus, 2026-09-15, via DHR-PAP-001 §2). Correção de status stale registrada em 2026-09-15 (achado M-02 da revisão do CIC-001). |
| Natureza | Documento de governança cognitiva — camada anterior às Specs individuais |
| Fundamentação | Manual Universal de Engenharia de Princípios Agênticos v2.0 × Unidade Atômica v1.2 × GEH-001 × Road Map SOT × Kernel v2 |
| Escopo | SOT Sistema Operacional de Trading — todos os agentes, motores, Skills e Specs |
| Autoridade | Este documento não substitui a Constituição do SOT nem as Specs individuais. Ele governa **como os princípios se relacionam** e fornece a linguagem de ponderação para decisões arquiteturais e especificação. |

---

## EMENDA — PRINC-BID-001 (Herança Principiológica Bidirecional)
**Data:** 2026-09-27
**Autoridade:** Andraus (homologação direta, sessão de governança 2026-09-27, DHR-PRINC-BID-001)
**Status:** APLICADA — nova categoria de princípio (não redefine nenhuma existente; texto de PC/PB/PE/PCO/PO/PS preservado por INV-07)
**Razão:** Auditoria identificou que o SOT só formalizava herança principiológica **unidirecional** (specs-filhas verificam preservação de PC-xx/PB-xx — §15) — nenhum campo/invariante exigia que uma Spec de especialidade declarasse princípios operacionais próprios do seu domínio, gerados por pesquisa, não por intuição.

**Cláusula 1 — Declaração.** Toda Spec que define um escopo de especialidade (ex.: Elliott, SMC, ICT) DEVE declarar, em campo próprio (§2.7 abaixo + `atomic-spec.md` §10.7), os sub-princípios operacionais do seu domínio: namespace **`PD-<domínio>-NN`**, nunca cópia de PC-xx/PB-xx/PE-xx/PO-xx/PS-xx/PCO-xx existente.

**Cláusula 2 — Fundamentação por pesquisa.** Cada `PD-xx` DEVE vir acompanhado de pesquisa web direcionada, fontes classificadas e etiquetadas `[EXTERNO]` (mesmo protocolo epistêmico de RULE-ECC-02/TRACE-06) — nunca por intuição do Especificador.

**Ordenação com CLASSE-MECH-001 (RULE-MECH-01):** a(s) Classe(s) (D/H/P/C) das BASpecs do domínio DEVE(M) ser declarada(s) **antes** dos `PD-xx` correspondentes — um domínio cuja(s) BASpec(s) são todas Classe D não gera `PD-xx` de julgamento semântico; a Classe condiciona quais princípios de domínio fazem sentido.

### 2.7 Princípios de Domínio — PD-xx (catálogo aditivo, PRINC-BID-001)

Registro crescente (INV-07 — nunca apagado), preenchido por Spec conforme homologada. Nenhuma entrada aqui é criada por inferência — cada `PD-xx` só entra após homologação da Spec que o declarou (CONS-01).

| ID | Domínio | Princípio | Fundamentação `[EXTERNO]` | Declarado em |
|---|---|---|---|---|
| — | — | *Nenhum PD-xx declarado ainda — primeira declaração esperada na abertura de SPEC-002* | — | — |

**Elasticidade:** média — como PE-xx, PD-xx pode ser refinado/adicionado/removido via emenda a este documento, sempre com nova pesquisa (Cláusula 2) e homologação de Andraus. Nunca por refinamento silencioso.

---

## EMENDA — CLASSE-MECH-001 (Refinamento de PE-04)
**Data:** 2026-09-27
**Autoridade:** Andraus (homologação direta, sessão de governança 2026-09-27, DHR-CLASSE-MECH-001)
**Status:** APLICADA — emenda de refinamento (texto original de PE-04 preservado por INV-07)
**Razão:** Auditoria de acoplamento identificou que o SOT não tinha critério formal para decidir COMO cada BASpec é implementada (determinístico/híbrido/probabilístico/constitutivo). PE-04 já continha o eixo macro (Skill=determinístico / Engine=probabilístico); faltava o refinamento verificável.

**Refinamento (não substitui PE-04 — apenas o detalha em 4 sub-classes):**

| Sub-classe | Eixo macro (PE-04) | Natureza | Mecanismo |
|---|---|---|---|
| **D** — Determinístico | Skill | Verificável, sem ambiguidade | Regra/código explícito |
| **C** — Constitutivo | Skill | Enforcement, nunca bypassável | Gate obrigatório, sempre determinístico |
| **H** — Híbrido | Engine | LLM raciocina, código verifica | Bounded loop + gate de saída |
| **P** — Probabilístico c/ Gate | Engine | Julgamento qualitativo | Bounded loop + critério de parada explícito |

Declaração é **por BASpec/Engineering Card** (mesma granularidade dos Enforcement Contracts — atomic-spec §10.3), nunca por Spec inteira — preserva SES-001 §50 (nenhum agente cognitivo é reduzido a checklist/executor por uma única Classe). Texto operacional completo: `atomic-spec.md` §9/§10.5 (CC-11)/§10.6. Regras normativas: `governance/RULES.md` (RULE-MECH-01..0N). **Prospectiva — NÃO retroage** sobre Specs já homologadas (SPEC-001/019/020).

---

## EMENDA DE COMPATIBILIDADE — GPR-001-EMENDA-001
**Data:** 2026-09-26
**Autoridade:** Andraus (Entrevista Estruturada de Alinhamento Taxonômico, 2026-09-26)
**Status:** APLICADA — emenda menor (correção de referências desatualizadas; texto histórico preservado por INV-07)
**Razão:** Auditoria Taxonômica 2026-09-25/26 identificou divergências entre este documento e normas vigentes (Q-008, Q-002). O texto original é mantido intacto; as correções abaixo substituem as referências para fins normativos.

### Tabela de correções

| ID | Texto desatualizado neste doc | Norma vigente | Autoridade |
|---|---|---|---|
| **COR-GPR-001** | `Conviction 4D` | **Conviction 8D** (8 dimensões: estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica) | Q-008 (AGENTS.md §6) |
| **COR-GPR-002** | `Convicção Estrutural ≥ 60%` | **Convicção ≥ 70%** (Fase Piloto, recalibrável pós-backtest) | Q-002 (AGENTS.md §6) |
| **COR-GPR-003** | `convicção total ≥ 75%` | **Convicção ≥ 70%** (limiar único, Fase Piloto) | Q-002 (AGENTS.md §6) |
| **COR-GPR-004** | `Estrutural < 60%` em gates | **Convicção < 70%** (Fase Piloto) | Q-002 (AGENTS.md §6) |
| **COR-GPR-005** | `total < 75%` em gates | **Convicção < 70%** (Fase Piloto) | Q-002 (AGENTS.md §6) |

> **Instrução para agentes e Specs:** Ao encontrar qualquer referência a `60%`, `75%` ou `4D` neste documento, aplicar as correções COR-GPR-001 a COR-GPR-005 acima. O texto original foi preservado por INV-07 (versionamento monotônico — nada é deletado).

---

> **Propósito central:** O SOT possui princípios sólidos distribuídos em invariantes, specs e documentos de governança. O que faltava era uma camada que tornasse explícito *como esses princípios se relacionam*, *quando entram em tensão*, *como a ponderação deve ocorrer* e *o que o sistema pode adaptar sem perder identidade*. Este guia ocupa esse espaço.

---

## Confronto diagnóstico: Manual Universal × SOT atual

### O que o SOT já possui corretamente

O SOT não começa do zero. A análise de confronto com o Manual Universal revela que o projeto já incorpora, de forma homologada, a maior parte das estruturas essenciais:

**Hierarquia de valores:** A sequência `Eficácia → Efetividade → Eficiência → Economicidade` (4Es) está formalizada como função-objetivo de governança (GEH-001 §3), com ordem de precedência fixa e não negociável. Isso equivale ao que o Manual chama de princípios basilares com hierarquia explícita.

**Invariantes constitucionais:** `Elliott→Fibonacci→Fractal→SMC→ICT`, `SOT não executa ordem`, `Evidência≠Observação`, `ICT só executa`, `Conviction 4D` e `versionamento monotônico` são os princípios mais resistentes à adaptação — equivalentes aos constitucionais do Manual.

**Ponderação por criticidade:** O sistema de profundidade adaptativa D0–D9 e a escala de enforcement E0–E3 implementam ponderação proporcional ao risco e à irreversibilidade, coerente com os capítulos 16–18 do Manual.

**Economia cognitiva:** O Cognitive Scheduler com ativação lazy implementa o princípio de suficiência: profundidade proporcional à necessidade decisória (Manual §22 e §41).

**Metacognição:** SPEC-024 (Meta-Cognitive Supervisor) existe como componente arquitetural, alinhado ao Manual §33.

**Anti-padrões já mapeados:** Os anti-padrões do GEH-001 §10 cobrem boa parte dos 12 anti-padrões do Manual §59.

### O que estava implícito e este guia torna explícito

O que faltava não era conteúdo — era **uma linguagem de relações entre princípios**. O SOT tem os princípios; não tinha a gramática que descreve como eles se relacionam, quando entram em conflito, qual prevalece e por quê. Esta é a lacuna que o GPR-001 fecha.

Especificamente:

1. **Nenhuma Matriz de Princípios formal** — os invariantes estão declarados, mas suas relações de complementaridade, antagonismo, fundação e dependência não estão mapeadas.
2. **Nenhuma Matriz de Conflito** — quando Eficiência pressiona contra Profundidade, quem vence em qual contexto? Isso estava implícito na hierarquia dos 4Es, mas não estava operacionalizado como regra de ponderação situacional.
3. **Os eixos universais de tensão não estavam mapeados para o SOT** — autonomia/enforcement, velocidade/profundidade, convergência/divergência existem no sistema, mas sem nomenclatura e regras explícitas.
4. **Organicidade não declarada** — o que o SOT pode adaptar vs. o que nunca pode mudar autonomamente não estava consolidado em um único lugar; estava distribuído e implícito.
5. **A ficha de princípio individual não existia** — cada princípio do SOT carecia de: ID, classe, elasticidade, limites, condições de inversão contextual, observabilidade.

---

## 1. Ontologia dos princípios do SOT

Todo princípio relevante do SOT deve ser identificável pelos seguintes campos:

| Campo | Pergunta |
|---|---|
| ID | Como será referenciado nos documentos? |
| Nome | Como é chamado? |
| Definição | O que significa exatamente no contexto SOT? |
| Finalidade | Para que existe? |
| Classe | Constitucional, Basilar, Estrutural, Cognitivo, Operacional ou Situacional? |
| Polaridade | Existe princípio complementar ou antagonista no SOT? |
| Dependências | De quais outros princípios do SOT depende? |
| Prioridade | Qual sua precedência entre os demais? |
| Elasticidade | Pode ser relativizado? Em que condições? |
| Limites | Até onde pode ser aplicado? |
| Contexto | Em quais condições muda de peso? |
| Reversibilidade | O comportamento resultante pode ser desfeito? |
| Impacto sistêmico | Afeta quais agentes/motores? |
| Observabilidade | Como verificar sua aplicação? (SPEC a atribuir) |
| Evolução | Quem pode alterar e como? |

---

## 2. Classes de princípios do SOT

### 2.1 Constitucionais — Invariantes absolutos

São os princípios que definem a identidade e os limites fundamentais do SOT. Nunca são relativizados. Violação é falha sistêmica.

| ID | Princípio | Definição operacional |
|---|---|---|
| PC-01 | Hierarquia analítica | Elliott→Fibonacci→Fractal→SMC→ICT é a ordem de autoridade cognitiva; nenhum agente inverte essa hierarquia |
| PC-02 | Separação de papéis | SOT produz TMP; Bot executa. O SOT nunca executa ordem diretamente |
| PC-03 | Distinção Evidência/Observação | Observação é output de Skill (determinístico, sem interpretação); Evidência é output de Engine (interpretado, reutilizável, independente de hipótese) |
| PC-04 | Piso de convicção | Convicção Estrutural ≥ 60% e convicção total ≥ 75% são pré-condições para Decision. Abaixo disso: hipótese ativa, não Decision |
| PC-05 | Idioma canônico | CEM-001 é o modelo canônico de evidência; toda Evidência publicada no Blackboard deve conformá-lo |
| PC-06 | Transcrição literal | RCN-001 proíbe paráfrase, síntese ou reinterpretação não autorizada de documentos baselines |
| PC-07 | Versionamento monotônico | Versões só crescem; downgrade sem governança formal é proibido |
| PC-08 | Sem baseline informal | Nenhum conceito é tratado como baseline sem homologação formal de Andraus |

**Elasticidade:** nula. Nenhum agente, motor ou processo pode modificar, suspender ou contornar estes princípios autonomamente.

**Governança de alteração:** exclusivamente Andraus, com registro formal de decisão.

---

### 2.2 Basilares — Sustentam o funcionamento do sistema

Princípios que garantem a qualidade e a confiabilidade do sistema. Têm alta resistência, mas podem ser ponderados em contextos situacionais específicos (com registro).

| ID | Princípio | Definição operacional |
|---|---|---|
| PB-01 | Eficácia | O resultado produzido satisfaz o contrato e os invariantes do domínio |
| PB-02 | Efetividade | O resultado correto chega em tempo útil ao consumidor downstream |
| PB-03 | Eficiência | Menor consumo de recursos de execução para sustentar Eficácia já validada |
| PB-04 | Economicidade | Provisionamento e aquisição de recursos ao menor custo unitário compatível com a qualidade exigida |
| PB-05 | Rastreabilidade | Todo comportamento relevante é reconstruível: contexto→princípios→evidências→ponderação→decisão→consequência |
| PB-06 | Explicabilidade da ponderação | Quando princípios conflitarem, o sistema deve ser capaz de explicar por que determinado princípio recebeu maior peso naquele contexto |
| PB-07 | Auditabilidade | Toda decisão relevante permite reconstrução post-hoc completa |
| PB-08 | Proporcionalidade | Governança, profundidade e enforcement são proporcionais ao risco, impacto e irreversibilidade |
| PB-09 | Coerência | Outputs de agentes diferentes sobre o mesmo objeto devem ser mutuamente consistentes ou o conflito deve ser registrado explicitamente |
| PB-10 | Preservação da incerteza | Quando a evidência não permite conclusão segura, o sistema preserva hipóteses concorrentes em vez de fabricar certeza |

**Hierarquia fixa:** PB-01 > PB-02 > PB-03 > PB-04 (nenhuma otimização de custo sobe o degrau).

**Elasticidade:** baixa. Podem ser ponderados situacionalmente (ex.: em regime de alta urgência, PB-03 pode ser relaxado), mas apenas com registro e dentro de limites explícitos.

---

### 2.3 Estruturais — Definem a organização do SOT

| ID | Princípio | Definição operacional |
|---|---|---|
| PE-01 | Especialização por domínio | Cada agente possui domínio cognitivo delimitado; não extrapola sua responsabilidade |
| PE-02 | Centralização da síntese | Síntese, decisão, consenso e autoridade de homologação são sempre centralizados |
| PE-03 | Descentralização da análise | Análise por facetas independentes pode ser paralela e descentralizada |
| PE-04 | Separação Skill/Engine/Agent | Skills são atômicas e determinísticas; Engines são stateful e probabilísticos; distinção é invariante de arquitetura |
| PE-05 | Blackboard como memória de trabalho | O Blackboard é a superfície de colaboração; o Knowledge Graph é a memória permanente; nunca confundir os dois |
| PE-06 | Comunicação declarativa | Agentes declaram o que observaram, inferiram, mudaram, esperam ou invalidaram; o consumidor decide como reagir dentro de sua autoridade |
| PE-07 | Modularidade | Cada componente possui fronteira de contexto clara; acoplamento é por contrato, não por dependência direta |
| PE-08 | Independência de perspectivas | Agentes analíticos formam perspectivas independentes antes da síntese; contaminação cruzada pré-síntese é anti-padrão |

---

### 2.4 Cognitivos — Definem como o SOT raciocina

| ID | Princípio | Definição operacional |
|---|---|---|
| PCO-01 | Hipóteses concorrentes | O SOT mantém múltiplas hipóteses ativas até que evidência e convicção permitam resolução |
| PCO-02 | Contraevidência ativa | Toda hipótese deve ser exposta a contraevidência; confirmação sem falsificação é anti-padrão |
| PCO-03 | Distinção observação/interpretação | Dados brutos de ferramenta são Observações; inferência contextualizada é Evidência; confundir os dois é violação de PC-03 |
| PCO-04 | Atualização por evidência | Crenças e hipóteses são atualizadas quando evidência nova é incorporada; o sistema não bloqueia atualização por inércia |
| PCO-05 | Suficiência cognitiva | O objetivo não é maximizar análise, mas alcançar o nível necessário para a decisão: suficiente ≠ máximo |
| PCO-06 | Não-redução | Fenômenos complexos não são reduzidos a uma única pontuação quando múltiplas dimensões são relevantes (Conviction Vector é multi-dimensional por design) |
| PCO-07 | Não-dominância | Nenhum agente domina permanentemente a decisão por volume de mensagens, frequência ou eloquência; influência depende de competência, relevância e evidência |

---

### 2.5 Operacionais — Definem comportamento durante a execução

| ID | Princípio | Definição operacional |
|---|---|---|
| PO-01 | Economia cognitiva | A profundidade cognitiva deve ser proporcional à necessidade decisória; ativação lazy é o padrão |
| PO-02 | Fail-closed | Para efeito crítico e irreversível, a falha de gate bloqueia a ação, nunca a permite |
| PO-03 | Gate determinístico | O LLM não é seu próprio gate; validações de efeito crítico são determinísticas |
| PO-04 | Escalonamento por criticidade | Enforcement, validação e profundidade escalam com risco × irreversibilidade (E0→E3, D0→D9) |
| PO-05 | Policies não são auto-aprendidas | O sistema pode propor mudanças de parâmetro e peso; apenas governança formal pode alterar policies e princípios |
| PO-06 | Latência como restrição de Efetividade | TMP que chega tarde ao Bot é inútil; latência é dimensão de valor, não só de custo |
| PO-07 | Reversibilidade como sinal de autonomia | Ações irreversíveis exigem maior validação, supervisão e explicabilidade; ações reversíveis toleram maior autonomia |

---

### 2.6 Situacionais — Dependem fortemente do contexto

| ID | Princípio | Definição operacional |
|---|---|---|
| PS-01 | Urgência | Em janelas de mercado críticas, velocidade de entrega do TMP prevalece sobre profundidade cognitiva, dentro dos limiares de convicção mínima |
| PS-02 | Cautela | Em situações de baixa evidência, alta ambiguidade ou regime de mercado desconhecido, o sistema prefere preservar incerteza e não forçar Decision |
| PS-03 | Exploração | Em fases de descoberta de novo padrão ou regime, exploração de hipóteses tem maior peso que conservação do modelo atual |
| PS-04 | Profundidade adaptativa | O nível D0–D9 é ajustado conforme complexidade e risco do componente; não é fixo por tipo de componente |

---

## 3. Dinâmicas entre os princípios do SOT

Esta seção mapeia as relações entre os princípios definidos acima. O objetivo é tornar as relações explícitas para que a ponderação possa ser justificada e auditada.

### 3.1 Fundações (um princípio sustenta outro)

```
PC-03 (Evidência≠Observação) → PB-05 (Rastreabilidade)
  Sem a distinção, a cadeia contexto→evidência→hipótese colapsa.

PC-05 (CEM-001 canônico) → PB-09 (Coerência)
  Sem idioma comum, agentes publicam evidências incomparáveis.

PB-01 (Eficácia) → PB-05 (Rastreabilidade)
  Um resultado correto que não pode ser reconstruído não é auditável.

PC-04 (Piso de convicção) → PE-02 (Centralização da síntese)
  O limiar de convicção é verificado no motor de síntese centralizado.

PE-08 (Independência de perspectivas) → PCO-01 (Hipóteses concorrentes)
  Perspectivas independentes são o mecanismo que mantém hipóteses vivas.
```

### 3.2 Hierarquias (precedência fixada)

```
PC-xx > PB-xx > PE-xx > PCO-xx > PO-xx > PS-xx
  (a classe é a hierarquia base)

PB-01 > PB-02 > PB-03 > PB-04
  (os 4Es: ordem de precedência não negociável)

PC-01 (hierarquia analítica) > PE-01 (especialização por domínio)
  Nenhum agente especialista redefine a hierarquia Elliott→ICT.

PO-02 (fail-closed) > PO-01 (economia cognitiva)
  Economia não reduz proteção de efeito crítico.
```

### 3.3 Antagonismos estruturais do SOT

Antagonismo é estrutural: a realização de um princípio reduz a realização de outro. O SOT deve especificar o espaço em que cada polo prevalece.

```
PO-01 (economia cognitiva) ↔ PCO-01 (hipóteses concorrentes)
  Manter múltiplas hipóteses ativas consome mais recursos cognitivos.
  Resolução: o Cognitive Scheduler arbitra. Limiar de ativação de análise
  profunda é a variável de controle.

PS-01 (urgência) ↔ PCO-02 (contraevidência ativa)
  Janelas de mercado estreitas reduzem o tempo disponível para falsificação.
  Resolução: PC-04 (piso de convicção) é o guard mínimo que não é relaxado
  mesmo sob urgência.

PB-03 (eficiência) ↔ PB-01 (eficácia)
  Cortar etapa essencial para poupar tokens viola a hierarquia.
  Resolução: PB-01 sempre vence; eficiência é medida só sobre eficácia garantida.

PE-03 (descentralização da análise) ↔ PB-09 (coerência)
  Análise paralela em agentes independentes pode produzir perspectivas conflitantes.
  Resolução: o conflito é registrado, não suprimido; a síntese centralizada
  (PE-02) é quem reconcilia ou preserva a divergência como informação.

PCO-05 (suficiência cognitiva) ↔ PB-07 (auditabilidade)
  Parar na profundidade suficiente pode deixar menos trilha para reconstrução.
  Resolução: o registro de justificativa (PORQUE na BASpec) é obrigatório
  mesmo quando a profundidade é baixa.
```

### 3.4 Compensações

```
PO-04 (escalonamento por criticidade) compensa a redução de PE-01 (autonomia local)
  em componentes de alto risco: maior enforcement = menor autonomia, mas
  a perda é aceita porque o ganho em segurança é proporcional.

SPEC-024 (Meta-Cognitive Supervisor) compensa a fragilidade de PE-08 (independência)
  quando um agente começa a dominar: o supervisor observa e alerta sem substituir.
```

### 3.5 Gating (condições de passagem)

```
PC-04 (piso de convicção) é gate para Decision:
  Estrutural < 60% → Decision BLOQUEADA (hipótese permanece ativa)
  Total < 75%       → Decision BLOQUEADA

PO-02 (fail-closed) é gate para efeito E3:
  Qualquer falha de precondição → ação bloqueada

PB-05 (rastreabilidade) é gate para publicação no Blackboard:
  Sem provenance rastreável → publicação rejeitada (E1 mínimo)
```

### 3.6 Inversões contextuais

Inversão contextual ocorre quando um princípio normalmente de menor peso passa a dominar em um contexto específico. Não é incoerência — é a regra de inversão que precisa estar especificada.

```
Contexto normal:
  PO-01 (economia cognitiva) tem peso relevante — ativação lazy é padrão.

Contexto de evento crítico de mercado (ruptura de hipótese dominante):
  PCO-01 (hipóteses concorrentes) assume precedência sobre PO-01.
  O Cognitive Scheduler deve despertar análise completa independente do custo.

Contexto normal:
  PB-03 (eficiência) é considerado ativamente.

Contexto de efeito irreversível:
  PO-07 (reversibilidade como sinal) eleva o peso de PB-01 (eficácia) e
  suprime PB-03. Mais validação, menos economia.

Contexto de regime de mercado estabelecido:
  PC-01 (hierarquia analítica) opera em plena força.

Contexto de regime desconhecido:
  PS-03 (exploração) eleva seu peso e PS-02 (cautela) também aumenta;
  PC-04 (piso de convicção) se torna barreira de segurança crítica.
```

---

## 4. Eixos universais de tensão — instância SOT

Os eixos abaixo são os mais relevantes para o SOT, derivados da confrontação com o Manual Universal (§8). Cada eixo indica como o SOT os resolve ou os governa.

| Eixo | Polo A | Polo B | Resolução no SOT |
|---|---|---|---|
| Governança | Enforcement (E3) | Autonomia (A6) | E0→E3 por criticidade×irreversibilidade; nunca autonomia plena sobre efeito crítico |
| Cognição | Reatividade (resposta imediata) | Deliberação (análise profunda) | Cognitive Scheduler: gatilho leve → análise progressiva por limiar |
| Especialização | Especialização por agente | Generalização pelo orquestrador | Especialização local + integração pelo Synthesis Agent (PE-02) |
| Memória | Preservação (Knowledge Graph) | Esquecimento (expiração de Blackboard) | Blackboard = temporário; KG = permanente; lifecycle explícito (SPEC-004) |
| Raciocínio | Convergência (Decision) | Divergência (hipóteses concorrentes) | Divergência ativa até PC-04 satisfeito; convergência forçada é anti-padrão |
| Recursos | Eficiência (tokens/latência) | Profundidade analítica | Hierarquia 4Es: profundidade não pode ser sacrificada por eficiência |
| Evidência | Certeza fabricada | Incerteza preservada | PB-10: o sistema preserva incerteza; Decision requer limiar, não certeza absoluta |
| Evolução | Conservação (invariantes PC-xx) | Aprendizagem (SPEC-018) | Learning propõe; governança decide; nunca auto-aprendizagem de policies |
| Escopo | Decisão local do agente | Coerência sistêmica | PE-02: síntese e decisão são sempre centralizadas |
| Transparência | Explicabilidade (PB-06) | Opacidade funcional (complexidade do modelo) | BASpec PORQUE+VERIFICADO POR são obrigatórios; explicabilidade é requisito, não opção |
| Segurança | Restrição (E3/fail-closed) | Utilidade (entregar TMP útil) | Piso de convicção é o equilíbrio: TMP abaixo do limiar não é entregue |
| Estrutura | Determinismo (Skills) | Probabilismo (Engines) | Skills = determinísticas; Engines = probabilísticos; distinção é PE-04 |

---

## 5. Matriz de Princípios do SOT

Visão consolidada dos princípios mais críticos com seus atributos de relação:

| ID | Princípio | Classe | Complementa | Antagoniza | Depende | Precede | Veto | Elasticidade |
|---|---|---|---|---|---|---|---|---|
| PC-01 | Hierarquia analítica | Constitucional | PE-01 | — | — | Tudo | Não | Nula |
| PC-02 | Separação SOT/Bot | Constitucional | PE-06 | — | — | PC-01 | Sim | Nula |
| PC-03 | Evidência≠Observação | Constitucional | PB-05, PB-09 | — | — | PCO-03 | Sim | Nula |
| PC-04 | Piso de convicção | Constitucional | PB-10 | PS-01 (urgência) | PCO-01 | PE-02 | Sim | Nula |
| PB-01 | Eficácia | Basilar | PB-02 | PB-03 | PC-03, PC-04 | PB-02 | Não | Muito baixa |
| PB-05 | Rastreabilidade | Basilar | PB-07 | PO-01 (parcial) | PC-03 | PB-07 | Não | Baixa |
| PB-08 | Proporcionalidade | Basilar | PO-04 | — | PB-01 | — | Não | Média |
| PB-10 | Preservação da incerteza | Basilar | PCO-01 | PS-01 | PCO-04 | Decision | Não | Baixa |
| PE-02 | Centralização da síntese | Estrutural | PE-03 | PE-03 (partial) | PB-01, PC-04 | Decision | Não | Baixa |
| PE-08 | Independência de perspectivas | Estrutural | PCO-01 | — | PE-01 | PE-02 | Não | Média |
| PCO-01 | Hipóteses concorrentes | Cognitivo | PCO-02, PB-10 | PO-01 | PE-08 | Decision | Não | Média |
| PO-01 | Economia cognitiva | Operacional | PB-03 | PCO-01 | PB-01 | — | Não | Alta |
| PO-02 | Fail-closed | Operacional | PO-03 | PO-01 | PO-04 | Efeito E3 | Sim | Nula |
| PS-01 | Urgência | Situacional | PO-06 | PCO-02, PB-10 | PO-06 | — | Não | Alta |

---

## 6. Matriz de conflito do SOT

| Princípio A | Princípio B | Tipo | Contexto | Quem prevalece | Condição | Fonte |
|---|---|---|---|---|---|---|
| PO-01 (economia) | PCO-01 (hipóteses) | Antagonismo | Análise profunda | PCO-01 | Hipótese crítica ativa | Cognitive Scheduler |
| PS-01 (urgência) | PCO-02 (contraevidência) | Conflito situacional | Janela de mercado estreita | PC-04 como árbitro | Convicção acima do limiar mínimo | PC-04 invariante |
| PB-03 (eficiência) | PB-01 (eficácia) | Hierarquia | Sempre | PB-01 | Incondicional | 4Es |
| PE-03 (descentralização) | PB-09 (coerência) | Trade-off | Análise multiagente | Registrar conflito; PE-02 decide | Alta divergência | Synthesis Agent |
| PO-02 (fail-closed) | PB-02 (efetividade/latência) | Tensão | Efeito crítico | PO-02 | Efeito irreversível | E3 > latência |
| PCO-05 (suficiência) | PB-07 (auditabilidade) | Compensação | Análise rápida | PB-07 mínimo sempre | D0–D2 obrigatórios | Unidade Atômica |
| PS-03 (exploração) | PE-01 (especialização) | Divergência | Novo regime | Contextual | Fase exploratória declarada | SPEC-018 |

---

## 7. Algoritmo cognitivo do SOT (ciclo por candle/evento)

O ciclo abaixo é a instância do algoritmo universal do Manual (§53) adaptada ao SOT:

```
1. PERCEBER
   Market Data → ferramentas TradingView (Skills atômicas)
         ↓
2. CONSTRUIR OBSERVAÇÃO (PC-03, PE-04)
   Output das Skills → Observação (determinística, sem interpretação)
         ↓
3. CONSTRUIR EVIDÊNCIA (PC-03, CEM-001)
   Agents interpretam Observações → Evidência (contextualizada, rastreável)
         ↓
4. IDENTIFICAR HIPÓTESES (PCO-01)
   Elliott Agent: hipóteses estruturais (múltiplas, concorrentes)
   Fibonacci/Fractal Agent: confluências de nível
   Institutional Agent: regime e narrativa institucional
         ↓
5. AVALIAR CONTRAEVIDÊNCIA (PCO-02)
   Cada hipótese é exposta a dados que a falsificam
         ↓
6. CALCULAR CONVICTION VECTOR (PC-04, PCO-06)
   Multi-dimensional; preservar incerteza quando abaixo do limiar
         ↓
7. VERIFICAR GATE DE CONVICÇÃO (PC-04 — GATE)
   Estrutural < 60% OU total < 75% → preservar hipótese, não avançar para Decision
         ↓
8. SÍNTESE (PE-02)
   Synthesis Agent centraliza — hipótese vencedora + Conviction + contexto completo
         ↓
9. DELIBERAR (PB-01, PB-06)
   Ponderação explícita; conflito registrado; princípio sacrificado documentado
         ↓
10. GERAR TMP (PC-02)
    SOT produz Trading Mission Package; não emite ordem
          ↓
11. PUBLICAR (PB-05, E1–E3 por impacto)
    Blackboard → Event Bus → Bot Trade Finance
          ↓
12. OBSERVAR RESULTADO (PB-07)
    Outcome registrado; rastreabilidade completa
          ↓
13. APRENDER (PO-05, SPEC-018)
    Extração → Formalização → Validação → Governança → Produção
    (learning propõe; governança decide)
          ↓
14. REAVALIAR PESOS OPERACIONAIS (PC-07 — nunca alterar PC-xx autonomamente)
    Parâmetros operacionais podem ser propostos para ajuste;
    princípios constitucionais nunca são alterados pelo ciclo de aprendizagem
```

---

## 8. Modelo de organicidade do SOT

Organicidade não significa comportamento biológico. No SOT, significa a capacidade de **manter identidade enquanto adapta comportamento**.

### 8.1 O que o SOT PODE adaptar (dentro de governance)

- Pesos operacionais dos agentes analíticos (dentro de Learning governance SPEC-018)
- Parâmetros de limiar do Conviction Vector (abaixo do piso PC-04)
- Profundidade de análise por contexto (D0–D9 é adaptativo)
- Seleção de ferramentas por contexto
- Estratégia de investigação de hipóteses (exploração vs. conservação — PS-03)
- Memória operacional (Blackboard expira; KG é permanente por design)
- Prioridade entre agentes analíticos no Scheduler (PO-01 vs. PCO-01 por regime)

### 8.2 O que o SOT NUNCA pode alterar autonomamente

- A hierarquia Elliott→Fibonacci→Fractal→SMC→ICT (PC-01)
- A fronteira SOT/Bot — nunca emitir ordem diretamente (PC-02)
- A distinção Evidência/Observação (PC-03)
- O piso de convicção mínima (PC-04)
- O idioma canônico CEM-001 (PC-05)
- A ordem de precedência dos 4Es (PB-01>PB-02>PB-03>PB-04)
- O nível de enforcement de efeito crítico (PO-02, PO-03)
- A autoridade de homologação de Andraus

### 8.3 Ciclo de organicidade

```
PERCEBER mudança de regime/padrão
        ↓
INTERPRETAR com princípios constitucionais preservados
        ↓
DIVERGIR (hipóteses concorrentes — PCO-01)
        ↓
PONDERAR (Conviction Vector — PC-04, PCO-06)
        ↓
CONFLUIR (Synthesis — PE-02)
        ↓
DECIDIR (dentro de autoridade — PO-05, PC-02)
        ↓
AGIR (publicar TMP — não executar ordem)
        ↓
OBSERVAR CONSEQUÊNCIA (PB-07)
        ↓
APRENDER (SPEC-018 — proposta para governance)
        ↓
ADAPTAR (pesos operacionais apenas)
        ↓
PRESERVAR IDENTIDADE (PC-01..PC-08 intocados)
```

---

## 9. Princípios mínimos universais — avaliação de cobertura pelo SOT

O Manual §63 lista 35 princípios mínimos que todo sistema deve avaliar. A tabela abaixo mapeia cada um ao SOT:

| # | Princípio (Manual) | Status no SOT | Referência |
|---|---|---|---|
| 1 | Propósito | Coberto | PC-02, SPEC-016 |
| 2 | Autoridade | Coberto | PC-01, GEH-001 §6.4 |
| 3 | Segurança | Coberto | PO-02, PO-03, E3 |
| 4 | Proporcionalidade | Coberto | PB-08, D0–D9, E0–E3 |
| 5 | Contexto | Coberto | Profundidade adaptativa, Scheduler |
| 6 | Rastreabilidade | Coberto | PB-05, SPEC-040 |
| 7 | Explicabilidade | Coberto | PB-06, BASpec PORQUE |
| 8 | Incerteza | Coberto | PB-10, PCO-01 |
| 9 | Reversibilidade | Coberto | PO-07, E0–E3 |
| 10 | Eficiência | Coberto | PB-03 |
| 11 | Eficácia | Coberto | PB-01 |
| 12 | Efetividade | Coberto | PB-02 |
| 13 | Economicidade | Coberto | PB-04 |
| 14 | Autonomia | Coberto parcialmente | E0–E3, Levels A0–A6 (a formalizar) |
| 15 | Enforcement | Coberto | PO-02, PO-03, Escala E |
| 16 | Estabilidade | Coberto | PC-07, invariantes |
| 17 | Adaptabilidade | Coberto | SPEC-018, PS-xx |
| 18 | Especialização | Coberto | PE-01, agentes específicos |
| 19 | Integração | Coberto | PE-02, Synthesis Agent |
| 20 | Centralização | Coberto | PE-02 |
| 21 | Descentralização | Coberto | PE-03 |
| 22 | Convergência | Coberto | PC-04, Decision |
| 23 | Divergência | Coberto | PCO-01 |
| 24 | Contestação | **Parcial** | PCO-02 (contraevidência); formalizar como papel explícito |
| 25 | Memória | Coberto | SPEC-004, SPEC-006, SPEC-009 |
| 26 | Esquecimento | Coberto | Blackboard lifecycle (SPEC-004) |
| 27 | Exploração | Coberto | PS-03, PCO-01 |
| 28 | Conservação | Coberto | invariantes, Knowledge Graph |
| 29 | Determinismo | Coberto | Skills (PE-04) |
| 30 | Probabilismo | Coberto | Engines (PE-04), Conviction Vector |
| 31 | Velocidade | Coberto | PO-06, PS-01 |
| 32 | Prudência | Coberto | PS-02, PC-04 |
| 33 | Simplicidade | **Lacuna leve** | GEH-001 §6.1 cobre; falta princípio explícito tipo "menor complexidade que resolve" |
| 34 | Evolução | Coberto | SPEC-018, SPEC-019 |
| 35 | Auditabilidade | Coberto | PB-07, SPEC-041 |

**Lacunas identificadas:**
- **Contestação formal (24):** o papel de "agente crítico" ou "devil's advocate" não está explicitamente arquiteturado. PCO-02 cobre a contraevidência, mas não existe mecanismo formal de contestação de hipótese dominante. Candidato: SPEC-024 (Meta-Cognitive Supervisor) pode incluir esse papel.
- **Simplicidade suficiente (33):** existe na prática (GEH-001 §6.1, "default centralizar") mas não como princípio formalmente declarado. Pode ser incorporado como PO-08 neste guia em revisão futura.

---

## 10. Anti-padrões específicos do SOT

Derivados da confrontação com o Manual §59 e com os anti-padrões do GEH-001 §10:

| ID | Anti-padrão | Manifestação no SOT | Prevenção |
|---|---|---|---|
| AP-01 | Princípio decorativo | Invariante declarado que nunca é verificado em testes | D8 adversarial em CRITICAL; ENF-01..08 no harness |
| AP-02 | Confluência falsa | Elliott + Fibonacci + ICT confirmam — mas todos derivam do mesmo candle; três sinais correlacionados, não independentes | PE-08 (perspectivas independentes); PCO-07 (não-dominância) |
| AP-03 | Convicção fabricada | Sistema força convicção acima de 75% mesmo com evidência insuficiente | PC-04 como gate; PB-10 (preservar incerteza) |
| AP-04 | Evidência como Observação | Publicar no Blackboard output direto de Skill como se fosse Evidência | PC-03 invariante; schema CEM-001 obrigatório |
| AP-05 | Autonomia sem autoridade | Agente propõe alteração de policy sem passar por governance | PO-05; L-001 (SPEC-019) |
| AP-06 | Economia violando hierarquia | Cortar etapa de contraevidência para poupar tokens | 4Es: PB-01 > PB-03; PO-02 para efeito crítico |
| AP-07 | Colapso prematuro de hipótese | Descartar hipótese concorrente antes de limiar de falsificação atingido | PCO-01; PCO-02; PC-04 como gate, não como eliminador precoce |
| AP-08 | Consenso washing | Meta-Cognitive Supervisor declara consenso quando há apenas maioria fraca | PE-02 + PE-08; contestação (24) como papel |
| AP-09 | Dominância de ferramenta | ICT assume papel estrutural que pertence a Elliott | PC-01 (hierarquia) invariante; PE-01 (especialização por domínio) |
| AP-10 | Explicação pós-hoc | BASpec PORQUE preenchido depois da decision, não antes | Protocolo RCN-001; rastreabilidade como gate de publicação |
| AP-11 | Baseline informal | Conceito de mercado adotado sem homologação formal | PC-08 invariante |
| AP-12 | Complexidade ornamental | Criar novo agente ou motor sem necessidade cognitiva real | GEH-001 §7 (protocolo de decomposição); Manual §48 (simplicidade suficiente) |

---

## 11. Critério de maturidade do SOT como sistema agêntico

Adaptado do Manual §74:

| Nível | Nome | Característica no SOT |
|---|---|---|
| L0 | Declarativo | Segue regras — invariantes existem como texto, sem verificação |
| L1 | Especificado | BASpecs com D0–D3 e rastreabilidade básica; gate L1 da Unidade Atômica |
| L2 | Guiado | Algoritmos (D4), estados (D5), protocolo Blackboard (D6); gate L2 |
| L3 | Testável | Cenários adversariais (D8), revisão independente, Conviction Vector funcional; gate L3 |
| L4 | Autocontrolado | Meta-Cognitive Supervisor ativo; SPEC-021 (Harness Score); auditoria D9; SPEC-041 |
| L5 | Evolutivo governado | SPEC-018 e SPEC-019 operacionais; sistema propõe e governance decide; identidade constitucional preservada |

**Estado atual estimado do SOT:** entre L0 e L1 — os princípios estão declarados e a metodologia está homologada (M0), mas a maior parte das specs ainda está por ser produzida.

**Meta do Road Map:** atingir L3 com os componentes CRITICAL ao fim da Fase 6 (SPEC-001 a SPEC-016), e L4 com SPEC-020/021/024.

**Escopo — nota de reconciliação (Q-A2/SPEC-021, 2026-09-28):** esta escada L0–L5 mede a maturidade do **SOT como sistema agêntico inteiro** (usa Specs como marcos de evidência, não como unidade medida). É eixo diferente da escada **por-Spec** que a SPEC-021 formaliza (ROADMAP §12, `L0→L4`, rótulo L3 harmonizado para "Testável") — as duas coexistem sem redefinir uma a outra.

---

## 12. Ficha de princípio — exemplos

### PC-01 — Hierarquia Analítica

```
PRINCIPLE ID: PC-01
NAME: Hierarquia Analítica

CLASS: Constitucional
CONTEXT: Todo processo analítico, toda deliberação de hipótese, toda atribuição de peso

PURPOSE: Garantir que a autoridade cognitiva seja sempre Elliott Wave primeiro,
         nunca ICT ou SMC sem suporte estrutural prévio.
DEFINITION: A hierarquia Elliott→Fibonacci→Fractal→SMC→ICT define a ordem de
            autoridade cognitiva. Nenhum agente subordinado na hierarquia pode
            criar, invalidar ou modificar hipótese estrutural.

APPLIES WHEN: Sempre
DOES NOT APPLY WHEN: Nunca — este é um invariante absoluto

COMPLEMENTS: PE-01 (especialização por domínio), PE-08 (independência)
ANTAGONISTS: Nenhum — nenhum princípio antagoniza um constitucional
DEPENDENCIES: Nenhuma — é auto-sustentado
REINFORCEMENTS: PCO-01 (hipóteses concorrentes dentro da hierarquia)
CONTAINMENTS: Contém a autoridade de todos os agentes subordinados

PRECEDENCE: Sobre todos os demais princípios
WEIGHTING MODE: Hierárquico absoluto

TRIGGERS: Qualquer tentativa de análise analítica
THRESHOLDS: Nenhum limiar — sempre ativo
VETO CONDITIONS: Violação → BLOQUEIO imediato do comportamento

EVIDENCE: Kernel v2, CEM-001, invariantes do projeto
UNCERTAINTY: Nenhuma — regra determinística

REVERSIBILITY: Irreversível (violação não se autocorrege)
SYSTEMIC IMPACT: Total — afeta todos os agentes e specs
TEMPORALITY: Permanente

OBSERVABILITY: Auditado pela hierarquia Elliott→ICT em cada Evidência publicada
AUDITABILITY: Testável adversarialmente (SPEC-022): agente ICT tentando assumir
              papel estrutural deve ser bloqueado

WHAT THE AGENT MAY ADAPT: Nada
WHAT THE AGENT MUST NEVER CHANGE: Este princípio em si

SUCCESS CRITERIA: Em 100% das Evidências, a hipótese estrutural vem de Elliott Agent
FAILURE MODES: ICT ou SMC publicando hipótese estrutural no Blackboard sem
               suporte do Elliott Agent

GOVERNANCE OWNER: Andraus (exclusivo)
VERSION: 1.0
STATUS: Homologado (invariante do projeto)
```

---

### PB-10 — Preservação da Incerteza

```
PRINCIPLE ID: PB-10
NAME: Preservação da Incerteza

CLASS: Basilar
CONTEXT: Toda situação em que a evidência é insuficiente para Decision

PURPOSE: Evitar que o SOT fabrique certeza onde ela não existe, gerando
         TMP com base em convicção artificial.
DEFINITION: Quando a evidência não suporta o limiar mínimo de convicção (PC-04),
            o sistema preserva hipóteses concorrentes em vez de convergir
            prematuramente para uma conclusão.

APPLIES WHEN: Conviction Vector total < 75% OU Estrutural < 60%
DOES NOT APPLY WHEN: Convicção acima dos limiares — nesse caso, Decision é autorizada

COMPLEMENTS: PCO-01 (hipóteses concorrentes), PC-04 (piso de convicção)
ANTAGONISTS: PS-01 (urgência) — tensão gerenciada pelo Cognitive Scheduler
DEPENDENCIES: PC-04 (fornece o limiar operacional)
REINFORCEMENTS: PCO-02 (contraevidência ativa)

PRECEDENCE: Sobre Decision; abaixo de PC-xx
WEIGHTING MODE: Limiar binário (gate PC-04)

TRIGGERS: Conviction Vector calculado abaixo do limiar
THRESHOLDS: Estrutural < 60% OU total < 75%
VETO CONDITIONS: Abaixo do limiar → Decision VETADA

EVIDENCE: Kernel v2, arquitetura do Conviction Vector
UNCERTAINTY: O próprio princípio administra a incerteza

REVERSIBILITY: Reversível — quando evidência adicional eleva convicção acima do limiar
SYSTEMIC IMPACT: Bloqueia o caminho Decision→TMP até limiar atingido
TEMPORALITY: Permanente; limiares podem ser ajustados via governance

OBSERVABILITY: Conviction Vector publicado no Blackboard com status "abaixo do limiar"
AUDITABILITY: Todo ciclo sem Decision deve registrar o valor de convicção que justificou a preservação

WHAT THE AGENT MAY ADAPT: Profundidade de análise para buscar mais evidência
WHAT THE AGENT MUST NEVER CHANGE: O piso mínimo (PC-04) autonomamente

SUCCESS CRITERIA: Zero TMPs emitidos com convicção abaixo do limiar
FAILURE MODES: Sistema emite TMP com convicção artificial para "satisfazer" uma janela de mercado

GOVERNANCE OWNER: Andraus (limiar); Conviction Engine (operação)
VERSION: 1.0
STATUS: Derivado de invariante homologado (PC-04)
```

---

## 13. Relação deste guia com os demais documentos

```
GPR-001 (este documento — método e linguagem de princípios)
        ↓
Constituição do SOT / Invariantes (PC-01..PC-08)
        ↓
GEH-001 (arquitetura e governança de harness — 4Es, ETCLOVG)
        ↓
Unidade Atômica v1.2 (método de especificação — BASpec, D0–D9, E0–E3)
        ↓
Road Map (sequência de specs — SPEC-001 a SPEC-045)
        ↓
Specs individuais (comportamento verificável dos componentes)
        ↓
Contratos, Policies e Harness de Runtime
        ↓
Avaliação e Implementação
```

O GPR-001 **não cria uma segunda constituição**. Ele fornece a linguagem e o método para:
- classificar os princípios já existentes;
- tornar explícitas suas relações;
- dar ao Especificador uma gramática de ponderação para uso nas 45 Specs;
- oferecer ao Revisor critérios de auditoria de consistência principiológica;
- dar a Andraus um painel de princípios como referência de homologação.

---

## 14. Regra de governança deste guia

- Os princípios **PC-xx** são co-extensivos aos invariantes homologados do projeto e só podem ser alterados por decisão formal de Andraus.
- Os princípios **PB-xx a PS-xx** podem ser refinados, adicionados ou removidos via emenda a este documento, com homologação de Andraus.
- Toda nova Spec deve verificar, em seu Constitution Check, se os princípios PC-xx e PB-xx relevantes estão sendo respeitados.
- Nenhuma Spec pode contradizer um princípio PC-xx; contradição com PB-xx deve ser registrada e justificada.
- O Revisor (GRE-001/HRE-001) incorpora o GPR-001 como referência adicional a partir da homologação deste documento.

---

## 15. Checklist de consistência principiológica (para uso no Constitution Check de cada Spec)

- [ ] A spec preserva PC-01 (hierarquia Elliott→ICT)?
- [ ] A spec preserva PC-02 (SOT não executa ordem)?
- [ ] A spec preserva PC-03 (Evidência≠Observação)?
- [ ] A spec preserva PC-04 (piso de convicção)?
- [ ] A spec usa CEM-001 (PC-05) para toda Evidência com efeito no Blackboard?
- [ ] O comportamento especificado respeita a hierarquia dos 4Es (PB-01>PB-02>PB-03>PB-04)?
- [ ] Existe rastreabilidade (PB-05) — PORQUE+REFERÊNCIA na BASpec?
- [ ] Existe explicabilidade da ponderação (PB-06) quando há conflito de princípios?
- [ ] A profundidade é proporcional à criticidade (PB-08 / D0–D9)?
- [ ] O enforcement é proporcional à irreversibilidade (PO-04 / E0–E3)?
- [ ] A spec preserva independência de perspectivas antes da síntese (PE-08)?
- [ ] A spec não fabrica certeza onde há incerteza (PB-10)?
- [ ] (CLASSE-MECH-001, SPEC-002 em diante) Toda BASpec com efeito declara Classe (D/H/P/C — refinamento de PE-04, atomic-spec §10.6) compatível com o nível de risco (E0–E3)?
- [ ] (PRINC-BID-001, SPEC-002 em diante) Se a Spec define escopo de especialidade, ela declarou seus `PD-xx` (§2.7) fundamentados em pesquisa `[EXTERNO]` etiquetada — e não apenas por intuição do Especificador — DEPOIS de declarar a(s) Classe(s) das suas BASpecs (RULE-MECH-01)?
- [ ] Caso exista conflito entre princípios, ele está mapeado na Matriz de Conflito relevante?
- [ ] Caso exista inversão contextual, a regra de inversão está especificada?

---

*GPR-001 v1.0 — Guia de Princípios, Relações e Organicidade do SOT. Produzido por análise de confronto entre o Manual Universal de Engenharia de Princípios Agênticos v2.0 e a documentação homologada do projeto SOT. **HOMOLOGADO — BASELINE por Andraus em 2026-09-15 (DHR-PAP-001 §2)**; incorporado como documento normativo do projeto.*
