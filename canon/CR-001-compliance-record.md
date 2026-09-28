# CR-001 — Compliance Record Specification (consolidado, Cap.6-8)
<!-- Fonte: DOCUMENTOS INICIAIS/04_Compliance_Record_CR-001. BASELINED parcial (Cap.1-6) conforme Catálogo. -->

---

# CR-001 — Capítulo 6
## Governança do Compliance Register
### Baseline 1.0 — CONGELADO ✅ (Doc.13 Final)

**Nota de método:** este documento foi construído por extração literal dos ADR-032 a ADR-045 e suas revisões, tal como submetidos e auditados nesta conversa — não por regeneração de texto. Cada elemento (CP, CRR, T) traz sua origem entre colchetes. Isso rompe o padrão de regressão observado entre Obs.16 e Obs.23: não há reescrita, apenas montagem.

---

## 6.1 Objetivo

Este capítulo estabelece as regras de governança, autoridade, preservação, consulta e manutenção do Compliance Register — o artefato canônico responsável pela preservação formal dos ComplianceRecords produzidos por processos auditáveis. `[ADR-032; Doc.9 §6.1]`

O Compliance Register não executa auditorias, não produz julgamentos de conformidade, não interpreta conformidade e não determina ações corretivas. `[ADR-032, ADR-042, ADR-044]`

## 6.2 Escopo

Este capítulo define: natureza do Compliance Register; responsabilidades permitidas e proibidas; regras de autoridade; preservação histórica; relação com ComplianceRecords; relação com NCRs; relação com NCRStatusEvents; invariantes estruturais; princípios derivados; testes de integridade.

Não define: execução de auditorias; criação ou fechamento de NCRs; interpretação de conformidade; determinação operacional de status vigente. Esses comportamentos pertencem a outros capítulos do CR-001. `[Doc.9 §6.2; Doc.12 §6.2]`

## 6.3 Classificação PPQ-001

| Campo | Valor |
|---|---|
| GES Level | GES-1 |
| What | Governança do Compliance Register |
| Why | Garantir preservação histórica auditável, autoridade única, rastreabilidade |
| Who | Governança, Auditores Autorizados, Consumidores Autorizados |
| Where | Ecossistema ORYX / Camada de Compliance |
| When | Sempre que ComplianceRecords forem registrados, consultados ou preservados |
| How | Regras canônicas CRR, CP e testes definidos neste capítulo |
| How Much | Baixo custo arquitetural |

`[ADR-032–045 consolidado]`

---

## 6.4 Definição Normativa

O Compliance Register é o repositório canônico responsável pela preservação e disponibilização dos ComplianceRecords reconhecidos pela Governança. `[ADR-032]`

- O Register não interpreta conteúdo. `[ADR-044]`
- O Register não produz conformidade nem julgamentos. `[ADR-032, ADR-044]`
- O Register não executa processos operacionais. `[ADR-040]`
- O Register não possui lifecycle operacional. `[ADR-040]`

---

## 6.5 Unicidade e Autoridade

Existe exatamente um Compliance Register Canônico reconhecido pela Governança. `[ADR-037, CRR10]`

> **Nota de correção C6-01:** a redação normativa preliminar (Doc.9) introduziu o qualificador "para cada domínio governado" em §6.5/CRR10, reabrindo implicitamente o Modelo B (múltiplos Registers), já descartado pelo Teste de Adoção do ADR-037. Esse qualificador foi removido (Obs.12) e não é reintroduzido aqui.

### Invariantes — Bloco Unicidade/Autoridade

| CRR | Texto | Origem |
|---|---|---|
| CRR10 | Existe exatamente um Compliance Register Canônico. | ADR-037 |
| CRR11 | Visões derivadas não constituem Compliance Registers. | ADR-037 |
| CRR12 | Visões derivadas não possuem autoridade sobre registros canônicos. | ADR-037 |
| CRR13 | Todo ComplianceRecord possui exatamente um Register de Autoridade: o Compliance Register Global. | ADR-037 (absorve CRR1) |
| CRR21 | A Governança é a única autoridade do Compliance Register. | ADR-041 |
| CRR22 | Auditores não governam o Compliance Register. | ADR-041 |

**CRR1** (histórico): *"Todo ComplianceRecord deve pertencer a exatamente um Compliance Register."* — `SUPERSEDED por CRR13` (Doc.5, Obs.5). Mantido aqui apenas como nota de rastreabilidade; não constitui invariante ativa.

---

## 6.6 Estrutura Canônica

```
ComplianceRegister
├─ register_id
├─ register_name
├─ version
└─ created_at
```
`[ADR-039 REV.2, ratificado no Doc.12 §6.6 — estrutura final após reversão de authority/records[]]`

**Semântica dos campos:**
- `register_id` — identidade imutável.
- `register_name` — identificação humana.
- `version` — representa exclusivamente a versão estrutural do schema do Register. Não representa estado operacional, lifecycle ou revisão de instância. `[ADR-039 REV.2, resolução da Obs.3]`
- `created_at` — data de criação do Register.

**Relações não persistidas:** relações entre ComplianceRegister e ComplianceRecords (e NCRStatusEvents) são derivadas do ecossistema e não constituem atributos armazenados do artefato Register. `[ADR-039 REV.1, Obs.6]`

**Campos proibidos:** `status`, `lifecycle_state`, `operational_state`, `current_state`. `[ADR-039 REV.2, C6-03]`

| CRR | Texto | Origem |
|---|---|---|
| CRR17 | register_id é imutável. | ADR-039 |
| CRR18 | O reconhecimento do Register Canônico é responsabilidade exclusiva da Governança. | ADR-039, revisado (Obs.6b — texto original "não podem existir dois Registers canônicos ativos" foi reescrito para remover o termo "ativos", por redundância com CRR10) |
| CRR19 | O Compliance Register não transita estados operacionais. | ADR-040 |
| CRR20 | O Compliance Register não participa de workflows. | ADR-040 |

> **Correção Obs.24 (autoauditoria):** CRR19/CRR20 estavam ausentes do corpo desta seção na primeira versão do Doc.13 — apareciam apenas na tabela De-Para (§6.16), sem o texto formal da invariante. Corrigido nesta revisão.

---

## 6.7 Preservação de ComplianceRecords

O Compliance Register preserva ComplianceRecords. A preservação é append-only: `[ADR-033]`

```
ADD      → permitido
UPDATE   → proibido
DELETE   → proibido
REPLACE  → proibido
```

| CRR | Texto | Origem |
|---|---|---|
| CRR2 | O Compliance Register não altera ComplianceRecords. | ADR-032 |
| CRR3 | ComplianceRecords não podem ser removidos. | ADR-033 |
| CRR4 | ComplianceRecords não podem ser substituídos. | ADR-033 (restaurado — Obs.20) |
| CRR8 | Nenhuma auditoria posterior remove auditoria anterior. | ADR-036 |
| CRR9 | Histórico completo deve permanecer disponível. | ADR-036 |
| CRR23 | ComplianceRecords são produzidos antes do Register. | ADR-042 |
| CRR24 | O Register não executa atividades de auditoria. | ADR-042 |

**Nota de consolidação:** CRR25 e CRR26 (ADR-043, texto original: *"Nenhum ComplianceRecord pode ser removido do histórico canônico"* / *"O histórico completo é preservado pelo Register"*) foram consolidadas por decisão do Estrategista (ADR-043 REV.1) como reforço redacional de CRR3, CRR8 e CRR9, deixando de ser invariantes independentes. Mantidas aqui apenas como referência histórica — **não devem ser reapresentadas como invariantes ativas**.

---

## 6.8 Fonte de Verdade

O Compliance Register é a única fonte de verdade para ComplianceRecords preservados. Visões, caches, relatórios e representações derivadas não substituem o Register Canônico. `[ADR-038]`

| CRR | Texto | Origem |
|---|---|---|
| CRR15 | O Compliance Register prevalece sobre qualquer representação derivada. | ADR-038 |
| CRR16 | Representações derivadas são descartáveis. | ADR-038 |

> **Correção Obs.22:** versões anteriores da consolidação (Doc.9–12) introduziram um item numerado **CRR14** (com o mesmo conteúdo do CRR15 original) e deslocaram/reformularam CRR15/16 sem ADR que autorizasse a renumeração. Não existe CRR14 em nenhum ADR original (Doc.4, ADR-038 define apenas CRR15 e CRR16). **CRR14 é retirado nesta versão, sem substituto** — os dois invariantes de ADR-038 voltam a ser CRR15 e CRR16, com seus textos originais.

---

## 6.9 Preservação Histórica

A preservação histórica é obrigatória, cumulativa e não pode ser reduzida, reescrita ou consolidada por substituição. `[ADR-036]`

---

## 6.10 Não Interpretação

O Compliance Register não interpreta conformidade, não calcula status e não executa inferências. `[ADR-034, ADR-044]`

| CRR | Texto | Origem |
|---|---|---|
| CRR5 | O Compliance Register não armazena status vigente. | ADR-034 |
| CRR6 | Status vigente não é propriedade persistida do Compliance Register. | ADR-035 |
| CRR7 | Status vigente não é propriedade persistida do ComplianceRecord. | ADR-035 |

**Nota de consolidação:** CRR27 e CRR28 (ADR-044, texto original: *"O Register não produz interpretações de conformidade"* / *"Toda interpretação é responsabilidade do consumidor"*) foram consolidadas (ADR-044 REV.1) como reforço redacional de CRR5. Mantidas aqui apenas como referência histórica — **não devem ser reapresentadas como invariantes ativas**.

### Determinação de Status Vigente

O status vigente é uma interpretação derivada, produzida por consumidores autorizados a partir de `audited_at` e `document_id`, seguindo a Convenção de Status Vigente do Capítulo 3: maior `audited_at` prevalece; `auditor_type` não altera precedência (conforme AI11). `[ADR-035]`

Nenhum campo persistido pode representar permanentemente o status vigente.

---

## 6.11 Separação Register × NCR

A preservação de ComplianceRecords não produz NCRs automaticamente. A abertura de NCR permanece responsabilidade exclusiva da Governança. `[C6-04, correção da Obs.16]`

| CRR | Texto | Origem |
|---|---|---|
| CRR33 | A preservação de ComplianceRecords não cria NCRs automaticamente. | C6-04 |
| CRR34 | A abertura de NCR exige decisão explícita da Governança. | C6-04 |

*(CRR31 e CRR32 permanecem reservados/não utilizados nesta versão.)*

---

## 6.12 Preservação de NCRStatusEvents

O artefato `NCRStatusEvent` já foi definido e congelado no CR-001 Capítulo 2, Baseline 1.0 (NI1–NI5, NP1–NP6, ADR-015). Este capítulo **não redefine** sua estrutura, semântica ou lifecycle — apenas estabelece sua preservação referencial no Compliance Register. `[ADR-045 REV.1]`

| CRR | Texto | Origem |
|---|---|---|
| CRR29 | Todo NCRStatusEvent registrado deve ser preservado no Compliance Register. | ADR-045 REV.1 |
| CRR30 | A preservação de NCRStatusEvents não altera a definição do artefato estabelecida no Capítulo 2. | ADR-045 REV.1 |

> Os números CRR29/CRR30 são exclusivos deste ADR e não podem ser reutilizados para outro conteúdo (esta foi a causa raiz da Obs.16).

---

## 6.13 Princípios Arquiteturais

| CP | Texto | Origem |
|---|---|---|
| CP18 | Registro Não Julga — o Register preserva; consumidores interpretam. | ADR-032–036 |
| CP19 | Histórico Imutável — nada é removido. | ADR-032–036 |
| CP20 | Consulta Não É Armazenamento — status vigente é derivado. | ADR-032–036 |
| CP21 | Coexistência Temporal — auditorias divergentes coexistem (ex.: 2025 COMPLIANT e 2026 NON_COMPLIANT, ambas válidas). | ADR-032–036 |
| CP22 | Fonte Única de Verdade — um Register, múltiplas consultas. | ADR-037–040 |
| CP23 | Derivações Não Governam — views servem, Register governa. | ADR-037–040 |
| CP24 | Identidade Permanente — Register é único e identificável. | ADR-037–040 |
| CP25 | Estrutura Não Opera — Register existe; processos acontecem ao seu redor. | ADR-037–040 |
| CP26 | Governança Governa — autoridade pertence à Governança. | ADR-041–044 |
| CP27 | Registro Não Produz — auditor produz, Register preserva. | ADR-041–044 |
| CP28 | Preservação Integral — nada se perde, tudo permanece. | ADR-041–044 |
| CP29 | Armazenamento Não Interpreta — Register armazena, consumidor interpreta. | ADR-041–044 |

---

## 6.14 Testes de Integridade

**Renumeração definitiva** (resolve a colisão identificada na Obs.23: os testes T58–T67 nas versões Doc.9–12 do capítulo não correspondiam ao conteúdo original de nenhum ADR sob esses números). A partir desta versão, a numeração de testes segue estritamente a ordem de origem:

### Fundação — ADR-033 a ADR-036 (T58–T63)

| T | Texto | Resultado esperado |
|---|---|---|
| T58 | Remover ComplianceRecord. | REPROVADO |
| T59 | Substituir ComplianceRecord. | REPROVADO |
| T60 | Register armazena status vigente. | REPROVADO |
| T61 | Consumidor calcula status vigente. | APROVADO |
| T62 | Duas auditorias divergentes coexistem. | APROVADO |
| T63 | Auditoria nova remove auditoria antiga. | REPROVADO |

### ADR-037 a ADR-040 (T64–T69)

| T | Texto | Resultado esperado |
|---|---|---|
| T64 | Dois Registers Canônicos Ativos. | REPROVADO |
| T65 | Dashboard prevalece sobre Register. | REPROVADO |
| T66 | View modifica registro canônico. | REPROVADO |
| T67 | Register possui workflow operacional. | REPROVADO |
| T68 | ComplianceRecord sem Register Canônico. | REPROVADO |
| T69 | Consumidor consulta View Derivada somente leitura. | APROVADO |

### ADR-041 a ADR-044 (T70–T74)

| T | Texto | Resultado esperado |
|---|---|---|
| T70 | Auditor altera estrutura do Register. | REPROVADO |
| T71 | Register gera ComplianceRecord. | REPROVADO |
| T72 | ComplianceRecord removido do histórico. | REPROVADO |
| T73 | Register calcula status vigente. | REPROVADO |
| T74 | Governança altera schema do Register. | APROVADO |

### ADR-045 REV.1 (T75–T76)

| T | Texto | Resultado esperado |
|---|---|---|
| T75 | Capítulo 6 redefine campos do NCRStatusEvent. | REPROVADO |
| T76 | Capítulo 6 referencia NCRStatusEvent existente e apenas define sua preservação. | APROVADO |

---

## 6.15 Teste de Adoção

Nenhuma prática nova é introduzida nesta consolidação. O capítulo materializa decisões já aprovadas em ADR-032 a ADR-045.

| Critério | Resultado |
|---|---|
| Risco | Baixo |
| Custo | Baixo |
| Flexibilidade | Alta |
| Decisão | Aprovado |

---

## 6.16 Tabela De-Para Final (CP · CRR · T)

| Bloco | CP | CRR vigentes | CRR consolidadas/superseded | T |
|---|---|---|---|---|
| ADR-032 | CP18 | CRR2 | CRR1 → superseded por CRR13 | — |
| ADR-033 | CP19 | CRR3, CRR4 | — | T58, T59 |
| ADR-034 | CP20 | CRR5 | — | T60 |
| ADR-035 | — | CRR6, CRR7 | — | T61 |
| ADR-036 | CP21 | CRR8, CRR9 | — | T62, T63 |
| ADR-037 | CP22 | CRR10, CRR11, CRR12, CRR13 | — | T64, T68 |
| ADR-038 | CP23 | CRR15, CRR16 | (CRR14 retirado — não autorizado) | T65 |
| ADR-039 | CP24 | CRR17, CRR18 | — | — |
| ADR-040 | CP25 | CRR19, CRR20 | — | T66, T67 |
| ADR-041 | CP26 | CRR21, CRR22 | — | T70 |
| ADR-042 | CP27 | CRR23, CRR24 | — | T71 |
| ADR-043 | CP28 | — | CRR25, CRR26 → consolidadas em CRR3/8/9 | T72 |
| ADR-044 | CP29 | — | CRR27, CRR28 → consolidadas em CRR5 | T73 |
| ADR-045 REV.1 | — | CRR29, CRR30 | — | T75, T76 |
| C6-04 | — | CRR33, CRR34 | — | — |
| Reservado | — | — | CRR31, CRR32 (não utilizados nesta versão) | — |

**Nota de leitura:** T69 e T74 já estão corretamente atribuídos nas linhas ADR-037/ADR-041 acima (não são itens à parte).

**Verificação de integridade:** CP18–CP29 = 12/12 presentes no corpo do texto (corrigido — Obs.24). CRR2–CRR34 = todos rastreados (vigente, consolidada ou reservada). T58–T76 = 19/19 sem colisão. CRR14 confirmado ausente e sem substituto (Obs.22, resolvida). Textos conferidos contra os ADR-fonte originais, não contra consolidações intermediárias (Doc.9–12), que continham drift adicional não detectado anteriormente (Obs.25).

---

## 6.17 Resultado Normativo

O Compliance Register é um artefato canônico de preservação. Ele preserva ComplianceRecords e referências a NCRStatusEvents, mantém histórico permanente e fornece fonte única de verdade. Ele não audita, não interpreta, não julga, não cria ou encerra NCRs, e não executa processos operacionais.

---

**Status:** CONGELADO — Baseline 1.0

**Declaração de Consenso:** consenso declarado por Andraus (Decisor Final), em 12 de julho de 2026, em resposta direta à proposta de congelamento apresentada pelo Analista, após parecer técnico CONFORME emitido nesta sessão de auditoria.

**Nota de processo:** conforme Regra 4 do Analista (nunca declara consenso — apenas emite parecer técnico), esta declaração de congelamento reflete a decisão do Decisor Final, não uma conclusão autônoma da IA. O parecer técnico que fundamenta esta decisão está registrado na trilha de auditoria desta conversa (Obs.1 a Obs.25).

Construído por extração literal; nenhum conteúdo foi gerado a partir de memória ou paráfrase.

---

# CR-001 — Capítulo 7
## Compatibilidade, Evolução e Governança de Mudanças
### Baseline 1.0 — Doc.14 (Montagem Mecânica por Extração Literal da MIC7)

**Nota de método:** este documento foi construído por extração literal da MIC7 (fonte de verdade única, mantida ao vivo desde ADR-046), não por regeneração de texto — mesmo método usado no Doc.13 (Capítulo 6). Cada elemento traz sua origem entre colchetes.

**Marco de origem:** M7-002 — escopo declarado integralmente atendido por ADR-046 a ADR-049. Nenhum novo ADR foi proposto para este capítulo após o encerramento da fundação.

---

## 7.1 Objetivo

Este capítulo estabelece as regras de compatibilidade retroativa, governança de mudanças arquiteturais, versionamento de artefatos normativos e classificação de impacto entre baselines do ecossistema ORYX.

Ele responde a quatro perguntas estruturais necessárias para que o sistema evolua sem perder integridade:

1. Como artefatos congelados permanecem válidos frente a novas versões? `[ADR-046]`
2. Quem possui autoridade para propor, auditar, registrar e aprovar mudanças? `[ADR-047]`
3. Como um identificador normativo evolui ao longo do tempo sem perder rastreabilidade? `[ADR-048]`
4. Quando uma mudança exige nova versão de baseline, e de que tipo? `[ADR-049]`

## 7.2 Escopo

Este capítulo define: compatibilidade retroativa; separação de papéis na governança de mudanças; gatilho formal de registro na MIC; modelo de estados de identificador e de capítulo; classificação Patch/Minor/Major de mudanças; e a Regra Anti-Colisão aplicada a todos os níveis de compatibilidade.

Não define: gestão de exceções arquiteturais, revogação formal de ADRs, ou política de depreciação — esses temas foram avaliados (M7-002) como pertencentes a um domínio distinto ("tratamento de desvios do fluxo normal") e permanecem candidatos a um Capítulo 8 dedicado, ainda não iniciado.

## 7.3 Classificação PPQ-001

| Campo | Valor |
|---|---|
| GES Level | GES-1 |
| What | Compatibilidade, Evolução e Governança de Mudanças do CR-001 |
| Why | Garantir que o sistema evolua sem quebrar artefatos congelados, sem ambiguidade de autoridade e com rastreabilidade completa |
| Who | Estrategista, Analista, Controlador, Decisor Final |
| Where | Todos os artefatos normativos do ORYX |
| When | Sempre que uma mudança arquitetural for proposta, revisada ou classificada |
| How | ADR-046 a ADR-049, consolidados nesta redação normativa |
| How Much | Baixo custo arquitetural |

---

## 7.4 Compatibilidade Retroativa `[ADR-046 REV.1]`

Baselines congeladas permanecem semanticamente válidas após a introdução de novas versões arquiteturais. `[CP30]`

**Cláusula de escopo (CE1):** o princípio de Compatibilidade Retroativa aplica-se exclusivamente a identificadores registrados na MIC com status `Vigente`. Identificadores de ADRs em fase de auditoria (REV.1, REV.2, REV.N) permanecem revisáveis até o registro formal pelo Controlador — este é o mecanismo que permitiu as correções legítimas ocorridas durante a fundação deste próprio capítulo (ver §7.9).

| CRR | Texto |
|---|---|
| CRR35 | Baselines Congeladas Permanecem Válidas — nenhuma nova versão pode invalidar uma baseline previamente congelada. |
| CRR36 | Significados Vigentes São Imutáveis — nenhum identificador registrado na MIC com status Vigente pode receber significado diferente em versão posterior. |
| CRR37 | Correção Não É Redefinição — a revisão de um ADR ainda não registrado como Vigente na MIC constitui correção arquitetural legítima, não redefinição semântica. |
| CRR38 | Compatibilidade É Obrigatória — toda mudança arquitetural deve declarar explicitamente seu impacto sobre compatibilidade retroativa. |

---

## 7.5 Governança de Mudanças Arquiteturais `[ADR-047 REV.1]`

Toda mudança arquitetural relevante percorre um fluxo formal de proposta, auditoria, decisão e registro antes de adquirir status normativo. `[CP31]`

### Separação de Papéis

| Papel | Responsabilidade | Autoridade de Aprovação |
|---|---|---|
| Estrategista | Propor ADRs, elaborar soluções, produzir consolidações, responder observações | Não |
| Analista | Auditoria independente, parecer técnico, identificação de inconsistências | Não |
| Controlador | Manutenção da MIC, registro de baselines, preservação histórica | Não |
| Decisor Final | Declarar consenso, aprovar congelamentos, aceitar riscos residuais | **Sim — exclusiva** |

| CRR | Texto |
|---|---|
| CRR39 | Toda Mudança Relevante Exige ADR. |
| CRR40 | Papéis São Separados — Estrategista propõe, Analista audita, Controlador registra, Decisor Final aprova. |
| CRR41 | Registro na MIC Possui Gatilho Formal — ocorre exclusivamente com parecer técnico sem observações críticas pendentes + decisão do Decisor Final; declarações intermediárias de ACCEPTED seguidas de REV.X não acionam registro. |
| CRR42 | Aprovação Pertence ao Decisor Final. |
| CRR43 | Registro Oficial Pertence ao Controlador. |
| CRR44 | Equivalência Formal de Governança — o termo "Governança", usado nos Capítulos 1–6 para representar autoridade de aprovação, reconhecimento ou homologação, equivale ao papel de Decisor Final definido neste capítulo. Esta cláusula é interpretativa: não altera o conteúdo normativo dos capítulos anteriores. |

---

## 7.6 Versionamento Arquitetural `[ADR-048 REV.2]`

Toda evolução normativa deve preservar a capacidade de reconstruir integralmente qualquer estado histórico previamente aprovado. `[CP32]`

### Modelo Normativo de Estados

O versionamento opera em duas dimensões independentes, que não devem ser interpretadas como substitutas entre si:

**Dimensão A — Estado do Identificador** (ADR, CP, CRR, T):
```
Draft → Proposed → Accepted → Vigente → {Deprecated | Superseded | Consolidated}
```

**Dimensão B — Estado do Capítulo/Baseline:**
```
Em Construção → Congelado
```
*(Termo oficial: "Congelado". "Frozen" é mantido apenas como sinônimo histórico, não deve ser usado em novos documentos.)*

Um identificador permanece `Vigente` mesmo quando o capítulo ao qual pertence se torna `Congelado` — as duas dimensões coexistem sem se substituir.

| CRR | Texto |
|---|---|
| CRR45 | Todo identificador normativo deve possuir estado explícito de ciclo de vida (Dimensão A). O estado pertence ao identificador individual. |
| CRR46 | Revisões Não Eliminam Histórico — uma revisão substitui vigência operacional, não elimina existência histórica. |
| CRR47 | Baselines Congeladas Permanecem Recuperáveis — toda baseline aprovada permanece disponível para consulta, auditoria e reconstrução histórica. |
| CRR48 | Depreciação Não Implica Remoção — artefatos Deprecated/Superseded/Consolidated permanecem rastreáveis no histórico oficial. |
| CRR49 | Congelamento Não Altera Vigência — o congelamento de um capítulo/baseline não modifica automaticamente o estado dos identificadores nele contidos. |
| CRR50 | Estados de Identificador e Capítulo São Independentes — dimensões distintas, não substitutas entre si. |
| CRR51 | Versionamento Explícito — toda alteração de identificador normativo após publicação inicial deve possuir nomenclatura de versão explícita (ex.: REV.1, REV.2, Baseline 1.0/2.0). Ausência constitui violação de governança documental. |

---

## 7.7 Compatibilidade de Baselines `[ADR-049 REV.2]`

O nível de compatibilidade de uma mudança determina o nível de evolução permitido para a baseline correspondente. `[CP33]`

### Classificação

| Nível | Definição | Efeito na Baseline |
|---|---|---|
| **Patch** | Correções exclusivamente editoriais (ortografia, formatação, referências cruzadas, notas sem efeito normativo) | Não altera a versão |
| **Minor** | Mudanças compatíveis que adicionam comportamento sem invalidar comportamento anterior | Incremento Minor (ex.: 1.0 → 1.1) |
| **Major** | Mudanças que removem, invalidam ou alteram comportamento normativo vigente | Nova baseline major (ex.: 1.0 → 2.0) |

**Cláusula de escopo (CE2):** este ADR não cria exceção a CRR36. Mudanças Major alteram comportamento vigente **exclusivamente por sucessão** — criação de identificadores novos que sucedem os anteriores, marcando-os `Superseded`/`Deprecated`/`Consolidated` conforme CRR48. A redefinição direta do texto de um identificador `Vigente` permanece proibida por CRR36 em qualquer nível de compatibilidade, inclusive Major.

| CRR | Texto |
|---|---|
| CRR52 | Mudanças Patch Não Alteram Baseline. |
| CRR53 | Mudanças Minor Geram Evolução Compatível. |
| CRR54 | Mudanças Major Geram Nova Baseline — operando exclusivamente por criação de identificadores sucessores (CRR48); redefinição direta de identificador Vigente permanece proibida por CRR36 em qualquer nível. |
| CRR55 | Compatibilidade Retroativa Obrigatória — mudanças Minor devem preservar a validade dos identificadores Vigentes existentes; complementa CP30, não permite redefinição. |
| CRR56 | Quebra de Compatibilidade Deve Ser Declarada — nenhuma mudança incompatível pode ser introduzida implicitamente; deve ser explicitamente declarada como Major. |

> **Nota de consolidação (Obs.C7-12, resolvida nesta redação):** o CRR57 original (*"Mudança Major Opera por Sucessão"*) sobrepunha-se integralmente ao conteúdo já incorporado em CRR54 acima. Consolidado em CRR54; não reapresentado como invariante independente, seguindo o mesmo padrão de Single Source of Truth aplicado no Capítulo 6 (CRR25–28).

---

## 7.8 Testes de Integridade

### ADR-046 (T77–T81)

| T | Texto | Resultado esperado |
|---|---|---|
| T77 | Nova versão invalida baseline anterior. | REPROVADO |
| T78 | ADR em revisão (REV.X) corrige identificador antes do registro na MIC. | APROVADO |
| T79 | Identificador Vigente na MIC recebe novo significado. | REPROVADO |
| T80 | Nova funcionalidade é adicionada por identificador novo. | APROVADO |
| T81 | Mudança declara compatibilidade com versões anteriores. | APROVADO |

### ADR-047 (T82–T86)

| T | Texto | Resultado esperado |
|---|---|---|
| T82 | Mudança arquitetural sem ADR. | REPROVADO |
| T83 | Mesmo agente propõe e audita a própria mudança. | REPROVADO |
| T84 | ADR ACCEPTED com observação crítica pendente é registrado na MIC. | REPROVADO |
| T85 | Decisor Final aprova baseline após parecer conforme. | APROVADO |
| T86 | Controlador atualiza MIC após aprovação formal. | APROVADO |

### ADR-048 (T87–T92)

| T | Texto | Resultado esperado |
|---|---|---|
| T87 | Revisão elimina histórico anterior. | REPROVADO |
| T88 | Baseline congelada permanece auditável. | APROVADO |
| T89 | Artefato Deprecated continua rastreável. | APROVADO |
| T90 | Identificador alterado após publicação sem nomenclatura explícita de versão. | REPROVADO |
| T91 | Capítulo Congelado contém identificador Vigente. | APROVADO |
| T92 | Congelamento altera automaticamente o estado dos identificadores internos. | REPROVADO |

### ADR-049 (T93–T98)

| T | Texto | Resultado esperado |
|---|---|---|
| T93 | Correção ortográfica altera a versão da baseline. | REPROVADO |
| T94 | Ampliação compatível gera evolução Minor. | APROVADO |
| T95 | Remoção de comportamento vigente mantém a mesma baseline. | REPROVADO |
| T96 | Mudança incompatível gera nova baseline major. | APROVADO |
| T97 | Mudança incompatível sem declaração explícita. | REPROVADO |
| T98 | Mudança Major redefine diretamente o texto de identificador Vigente. | REPROVADO |

---

## 7.9 Teste de Adoção

Nenhuma prática nova é introduzida nesta consolidação. O capítulo materializa decisões já aprovadas em ADR-046 a ADR-049, formalizando um comportamento que já havia sido praticado com sucesso durante a fundação do Capítulo 6 (revisões REV.X antes do congelamento — ADR-039, ADR-043, ADR-044, ADR-045).

| Critério | Resultado |
|---|---|
| Risco | Baixo |
| Custo | Baixo |
| Flexibilidade | Alta |
| Decisão | Aprovado |

---

## 7.10 Tabela De-Para Final

| Bloco | CP | CRR vigentes | CRR consolidadas | T |
|---|---|---|---|---|
| ADR-046 REV.1 | CP30 | CRR35, CRR36, CRR37, CRR38 | — | T77–T81 |
| ADR-047 REV.1 | CP31 | CRR39, CRR40, CRR41, CRR42, CRR43, CRR44 | — | T82–T86 |
| ADR-048 REV.2 | CP32 | CRR45, CRR46, CRR47, CRR48, CRR49, CRR50, CRR51 | — | T87–T92 |
| ADR-049 REV.2 | CP33 | CRR52, CRR53, CRR54, CRR55, CRR56 | CRR57 → consolidado em CRR54 | T93–T98 |
| Reservado (herdado Cap.6) | — | — | CRR31, CRR32 (não utilizados) | — |

**Verificação de integridade:** CP30–33 = 4/4 presentes. CRR35–56 = todas rastreadas (Vigente ou consolidada); CRR57 consolidada em CRR54, não reapresentada como independente. T77–T98 = 22/22 sem colisão. Nenhum identificador redefinido após registro como Vigente.

---

## 7.11 Resultado Normativo

Este capítulo estabelece que o ecossistema ORYX evolui por **extensão e sucessão controladas**, nunca por redefinição retroativa de identificadores já registrados como `Vigente`. Toda mudança arquitetural é classificada (Patch/Minor/Major), governada por papéis formalmente separados, e só produz efeito normativo após registro pelo Controlador — nunca antes.

O capítulo não trata de exceções, revogações ou depreciações programáticas — esses temas foram deliberadamente excluídos do escopo (M7-002) e permanecem candidatos a um Capítulo 8 dedicado.

---

**Status:** candidato a Baseline 1.0 — pronto para auditoria formal final e declaração de consenso.
Construído por extração literal da MIC7; nenhum conteúdo foi gerado a partir de memória ou paráfrase.

---

# CR-001 — Capítulo 8
## Gestão de Exceções e Casos Extraordinários
### Fundação Encerrada (M8-002) — aguardando Auditoria de Cobertura final e consenso de Andraus (Doc.15)

**Nota de método:** este documento foi construído pelo Controlador por extração literal da MIC8 (fonte de verdade única, mantida ao vivo desde ADR-050), não por regeneração de texto — mesmo método usado nos Doc.13 (Capítulo 6) e Doc.14 (Capítulo 7). Cada elemento traz sua origem entre colchetes.

**Marco de origem:** M8-001 — abertura formal com numeração global herdada do Capítulo 7. **Marco de encerramento da fundação:** M8-002 — terceira verificação de completude (Mecanismo 3) concluiu que não há lacuna crítica remanescente.

---

## 8.1 Objetivo

Este capítulo estabelece as regras de gestão de exceções arquiteturais, resolução formal de conflitos entre normas simultaneamente Vigentes, revogação e substituição de identificadores, compatibilidade entre baselines congeladas como entidades navegáveis, e política de depreciação normativa — incluindo tanto os critérios de candidatura quanto a decisão formal de transição.

Ele responde a seis perguntas estruturais que o Capítulo 7 deliberadamente deixou fora de escopo (M7-002, §7.2):

1. Como o sistema trata desvios temporários e justificados do fluxo normal? `[ADR-050]`
2. O que acontece quando duas normas simultaneamente Vigentes produzem decisões incompatíveis? `[ADR-050, ADR-054]`
3. Como um identificador deixa de ser válido de forma explícita e rastreável? `[ADR-051]`
4. Como uma baseline congelada permanece navegável e auditável mesmo após ser sucedida? `[ADR-052]`
5. Quando e como uma norma pode ser candidata à depreciação? `[ADR-053]`
6. Quem decide formalmente a transição de uma candidatura para o estado Deprecated? `[ADR-055]`

## 8.2 Escopo

Este capítulo define: gestão formal de exceções com prazo obrigatório; escalonamento e resolução de conflitos normativos; revogação explícita com preservação de histórico; o estado `Substituída` para baselines (Dimensão B); critérios objetivos de candidatura à depreciação; e o processo de decisão formal que transiciona uma candidatura para `Deprecated` (Dimensão A, CRR48).

Não define: novos mecanismos de urgência paralelos ao dial de governança do PPQ-001 §3; sistemas de registro paralelos a CRR63; nem redefinição de qualquer identificador Vigente herdado dos Capítulos 6 e 7.

## 8.3 Classificação PPQ-001

| Campo | Valor |
|---|---|
| GES Level | GES-1 |
| What | Gestão de Exceções e Casos Extraordinários do CR-001 |
| Why | Permitir desvios legítimos e temporários do fluxo normal, resolver conflitos normativos e encerrar o ciclo de vida de identificadores (revogação, depreciação) sem comprometer rastreabilidade ou Anti-Colisão |
| Who | Estrategista, Analista, Controlador, Decisor Final |
| Where | Todos os artefatos normativos do ORYX regidos pelo CR-001 |
| When | Sempre que uma exceção, conflito, revogação, sucessão de baseline ou depreciação for proposta |
| How | ADR-050 a ADR-055, consolidados nesta redação normativa |
| How Much | Baixo custo arquitetural |

---

## 8.4 Gestão de Exceções `[ADR-050 REV.1]`

Toda exceção arquitetural deve possuir justificativa explícita, duração definida, autoridade responsável e rastreabilidade completa. Não existem exceções implícitas. `[CP34]`

| CRR | Texto |
|---|---|
| CRR58 | Exceção Não É Revogação — uma exceção autoriza desvio temporário, não altera permanentemente a norma original. |
| CRR59 | Exceção Deve Possuir Prazo — toda exceção deve possuir condição de encerramento explícita; exceções permanentes são proibidas. |
| CRR60 | Conflito Entre Normas Vigentes Deve Ser Escalado — quando duas normas simultaneamente Vigentes produzirem decisões incompatíveis para o mesmo caso, o conflito deve ser escalado à Governança antes da execução. |
| CRR61 | Emergência Não Suspende Anti-Colisão — correções emergenciais continuam sujeitas a CRR36, CRR48 e CRR54; urgência acelera o processo decisório, não autoriza redefinição direta de identificador Vigente. |
| CRR62 | Exceções Utilizam o Dial de Burocracia Existente — situações emergenciais usam os níveis acelerados já definidos em PPQ-001 §3; proibido criar mecanismo paralelo de urgência. |

**CE1:** este ADR não cria exceções a CP30, CRR36 ou CRR54. Identificadores Vigentes permanecem protegidos mesmo sob regime de exceção.

**Nota de processo:** ADR-050 foi auditado pelo Analista desconsiderando um bloco de veredicto pré-escrito recebido junto da proposta original — evidência de que a salvaguarda anti-autoavaliação do Mecanismo 3 opera na prática, não apenas em princípio.

---

## 8.5 Revogação e Substituição `[ADR-051 REV.2]`

A remoção de validade normativa de um identificador não elimina sua rastreabilidade histórica. `[CP35]`

| CRR | Texto |
|---|---|
| CRR63 | Revogação Deve Ser Explícita — nenhum identificador perde validade por abandono, omissão ou desuso; exige ato formal registrado. |
| CRR64 | Revogação Não Autoriza Reutilização — identificadores revogados não podem receber novo significado; proteção histórica permanece indefinidamente. |
| CRR65 | Substituição Deve Referenciar Antecessor — todo identificador sucessor deve declarar explicitamente qual identificador substitui. |
| CRR66 | Cadeia de Sucessão Deve Ser Rastreável — histórico de sucessões reconstruível sem depender de memória de sessões anteriores. |
| CRR67 | Revogação Sem Substituto É Permitida — norma pode ser revogada sem sucessor quando o comportamento correspondente deixar de existir. |
| CRR68 | Revogado é Estado Terminal Próprio — quarto valor do enum de Dimensão A (CRR45), distinto de Deprecated/Superseded/Consolidated. Estado único mesmo com sucessor; existência de sucessor verificável via CRR65, não por marcação dupla. |

**Cláusulas (CE1–CE4):** CE1 — Revogação não excepciona Anti-Colisão; IDs revogados seguem protegidos por CRR36. CE2 — Revogação não substitui sucessão; havendo sucessor, CRR48 permanece obrigatório. CE3 — `Revogado` é extensão compatível do modelo de estados (CRR45), não redefinição. CE4 — Alcance temporal de CRR36 cobre qualquer ID que já foi Vigente, independente do status atual.

**Nota de processo:** ADR-051 foi o primeiro ciclo completo sob SDD-001 (Spec → Constitution Check → Plan → Tasks) no ecossistema ORYX, processado sem perda de rastreabilidade.

---

## 8.6 Compatibilidade entre Baselines Congeladas `[ADR-052 REV.2]`

Baselines congeladas coexistentes permanecem identificáveis, navegáveis e auditáveis independentemente da existência de versões posteriores. `[CP36]`

**Cláusula de escopo (CE5):** este ADR resolve um problema distinto do Capítulo 7/ADR-049. ADR-049/CRR52-57 trata de compatibilidade de **conteúdo** de identificador (Dimensão A — Superseded/Patch/Minor/Major). ADR-052/CRR69-74 trata de navegabilidade e sucessão de **baselines inteiras como entidades** (Dimensão B — Congelado/Substituída). `Superseded` (Dimensão A) e `Substituída` (Dimensão B) são conceitos independentes; nenhum implica o outro automaticamente.

| CRR | Texto |
|---|---|
| CRR69 | Baseline Congelada Não É Substituída Automaticamente — permanece válida para consulta/auditoria até declaração normativa explícita em contrário. |
| CRR70 | Introdução do Estado de Baseline "Substituída" — Dimensão B passa a admitir Em Construção → Congelado → Substituída. Não redefine os estados existentes. |
| CRR71 | Substituição de Baseline Não Implica Remoção — baseline substituída permanece integralmente acessível. |
| CRR72 | Relação de Sucessão Entre Baselines Deve Ser Explícita — toda baseline Substituída referencia a sucessora; toda sucessora declara qual substitui. |
| CRR73 | Navegação Entre Baselines Deve Ser Bidirecional. |
| CRR74 | Baselines Devem Possuir Intervalo de Vigência Determinável — data de congelamento + data de substituição (quando existir). Sem data de substituição, permanece no estado Congelado. |

**Cláusulas (CE1–CE5):** CE1 — não redefine estados existentes de Dimensão B, só adiciona Substituída. CE2 — aplica CRR50 (independência entre dimensões), não a modifica. CE3 — Substituída não excepciona CRR48. CE4 — determinação point-in-time via CRR74, usando o estado Congelado como referência. CE5 — ver cláusula de escopo acima.

---

## 8.7 Política de Depreciação Normativa `[ADR-053 REV.1]`

A classificação de uma norma como candidata à depreciação deve ser fundamentada por critérios explícitos e verificáveis, não por julgamento arbitrário. `[CP37]`

**Cláusula de escopo (CE1):** este ADR não altera o significado de `Deprecated` já definido por CRR48 (Cap.7). Define exclusivamente os critérios de **candidatura** — a decisão formal que efetiva a transição de estado é tratada separadamente em §8.9 (ADR-055).

| CRR | Texto |
|---|---|
| CRR75 | Candidatura Exige Critério Objetivo — norma só pode ser proposta para depreciação atendendo a pelo menos um de: (a) sucessor que cubra sua finalidade, (b) não recomendada para novos usos, (c) fora de processos operacionais ativos, (d) permanece só por necessidade histórica/rastreabilidade. |
| CRR76 | Justificativa Obrigatória — toda proposta deve registrar quais critérios de CRR75 a motivaram; ausência invalida a proposta. Registro usa o mesmo mecanismo formal de CRR63, não constitui sistema independente. |
| CRR77 | Proteção de Necessidade Operacional — nenhuma norma pode ser candidata à depreciação enquanto necessária para processos vigentes. |
| CRR78 | Critérios de Avaliação São Auditáveis — critérios que justificaram a candidatura permanecem consultáveis; rastreabilidade formal provida por CRR63. |
| CRR79 | Depreciação Não Implica Revogação — candidatura/aprovação para depreciação não altera o significado de Deprecated (CRR48) nem constitui revogação normativa (ADR-051). |

**Cláusulas (CE1–CE3):** CE1 — ver cláusula de escopo acima. CE2 — compatibilidade com ADR-051; reutiliza CRR63, sem sistema paralelo de registro. CE3 — compatibilidade com CRR36; depreciação não autoriza reutilização de identificadores protegidos.

---

## 8.8 Encerramento Formal de Conflitos e Exceções `[ADR-054 REV.1]`

Todo conflito escalado por CRR60 e toda exceção aberta sob ADR-050 devem possuir conclusão formal rastreável; nenhum estado pode permanecer indefinidamente sem resultado documentado. `[CP38]`

**Origem:** identificado pela primeira verificação de completude do capítulo (M8-002, primeira rodada) — CRR60 e CRR59 definiam gatilhos sem processo terminal explícito.

| CRR | Texto |
|---|---|
| CRR80 | Resolução Formal Obrigatória de Conflitos — conflito escalado por CRR60 deve resultar em decisão formal emitida pela autoridade de CRR42; não redefine autoridade decisória. |
| CRR81 | Registro de Resolução Utiliza CRR63 — exclusivamente; não constitui sistema de registro independente. |
| CRR82 | Resultado da Resolução Deve Produzir Artefato — novo ADR, interpretação formal, sucessão, revogação ou confirmação formal de inexistência de conflito; nenhum conflito encerra sem artefato. |
| CRR83 | Alterações Normativas Devem Reutilizar Processos Vigentes — depreciação via CRR75-79; revogação via CRR63-68; sucessão via CRR65; baselines via CRR69-74. Não autoriza atalhos nem substitui etapas obrigatórias. |
| CRR84 | Prazo de Resolução Baseado no Dial de Governança — segue PPQ-001 §3 (Níveis 1-4); reutiliza mecanismo Vigente, sem sistema paralelo de urgência. |
| CRR85 | Encerramento Formal de Exceções — condição de CRR59 atingida exige ato formal de encerramento via CRR63; não se encerra por mero decurso administrativo. |
| CRR86 | Cadeia de Decisão Integralmente Reconstruível — todo registro sob CRR81/CRR85 identifica gatilho original, autoridade responsável (CRR42), decisão produzida, artefato resultante e referência formal de registro (CRR63). |

**Cláusulas (CE1–CE5):** CE1 — compatível com ADR-050, complementa CRR59/60. CE2 — compatível com ADR-051, usa CRR63. CE3 — compatível com ADR-052, não altera Dimensão B. CE4 — compatível com ADR-053, não altera critérios de candidatura. CE5 — compatível com CRR42, CRR86 serve reconstrução histórica, não redefine competência decisória.

---

## 8.9 Decisão Formal de Depreciação `[ADR-055]`

Candidatura à depreciação só produz alteração de estado após decisão formal da autoridade competente e registro auditável correspondente. `[CP39]`

**Origem:** identificado pela segunda verificação de completude — CRR75-79 (critérios de candidatura) não possuíam amarração explícita a uma autoridade de decisão (CRR42), deixando em aberto quem formaliza a transição para `Deprecated`.

**Nota de processo:** o Plan original propunha CP38 para este ADR; corrigido para CP39 antes do registro, pois CP38 já pertencia ao ADR-054 (Obs.C8-27) — a Regra Anti-Colisão operando corretamente antes do registro chegar ao Controlador.

| CRR | Texto |
|---|---|
| CRR87 | Aprovação Formal Obrigatória — candidatura sob CRR75-79 deve ser submetida à autoridade de CRR42 antes de qualquer transição para Deprecated; candidatura por si só não altera estado. |
| CRR88 | Registro da Decisão — aprovação ou rejeição usa exclusivamente CRR63; identifica candidatura, autoridade, decisão e resultado. |
| CRR89 | Resultado da Aprovação — identificador transita para Deprecated usando exclusivamente o significado de CRR48; nenhuma alteração adicional de significado. |
| CRR90 | Resultado da Rejeição — identificador permanece no estado anterior, sem alteração normativa; candidatura permanece rastreável. |
| CRR91 | Prazo para Deliberação — reutiliza o mecanismo de CRR84 e o dial de PPQ-001 §3; candidatura não pode permanecer indefinidamente sem decisão. |
| CRR92 | Cadeia Reconstruível de Depreciação — critérios (CRR75-79), autoridade (CRR42), registro (CRR63), decisão e resultado, todos reconstruíveis. |

**Cláusulas (CE1–CE4):** CE1 — compatibilidade com CRR48; CRR89 não redefine Deprecated. CE2 — compatibilidade com CRR42; CRR87 apenas aplica autoridade já existente. CE3 — compatibilidade com CRR63; CRR88/CRR92 reutilizam exclusivamente. CE4 — compatibilidade com ADR-053; candidatura (§8.7) ≠ decisão (§8.9).

**Fechamento formal:** a cadeia `CRR75→76→77→CRR42(CRR87)→CRR63(CRR88)→CRR48(CRR89)` está completa — depreciação com processo terminal simétrico ao de revogação (§8.5) e resolução de conflitos (§8.8).

---

## 8.10 Testes de Integridade

### ADR-050 (T99–T104)

| T | Texto | Resultado esperado |
|---|---|---|
| T99 | Exceção sem justificativa formal. | REPROVADO |
| T100 | Exceção sem prazo de encerramento. | REPROVADO |
| T101 | Conflito entre normas Vigentes executado sem escalonamento. | REPROVADO |
| T102 | Correção emergencial cria identificador novo e marca o anterior como Superseded. | APROVADO |
| T103 | Correção emergencial reescreve diretamente identificador Vigente. | REPROVADO |
| T104 | Situação urgente utiliza Nível 3 ou 4 do PPQ-001 para acelerar aprovação. | APROVADO |

### ADR-051 (T105–T111)

| T | Texto | Resultado esperado |
|---|---|---|
| T105 | Revogação formal registrada. | APROVADO |
| T106 | Norma abandonada sem ato formal. | REPROVADO |
| T107 | Identificador revogado reutilizado. | REPROVADO |
| T108 | Substituição sem referência ao antecessor. | REPROVADO |
| T109 | Revogação sem sucessor porque comportamento deixou de existir. | APROVADO |
| T110 | Identificador Vigente formalmente revogado (Vigente → Revogado). | APROVADO |
| T111 | Identificador já Vigente, revogado, com tentativa de reutilização com significado diferente. | REPROVADO |

### ADR-052 (T112–T122)

| T | Texto | Resultado esperado |
|---|---|---|
| T112 | Baseline Congelada continua consultável após nova baseline criada. | APROVADO |
| T113 | Baseline Substituída mantém histórico. | APROVADO |
| T114 | Relação de sucessão é bidirecional. | APROVADO |
| T115 | Determinação histórica point-in-time via CRR74. | APROVADO |
| T116 | Independência entre Dimensões (CRR50). | APROVADO |
| T117 | Ausência de data de substituição — baseline permanece Congelado. | APROVADO |
| T118 | Substituição implícita (sem declaração). | REPROVADO |
| T119 | Remoção de baseline Substituída. | REPROVADO |
| T120 | Sucessora não declarada. | REPROVADO |
| T121 | Sucessão unidirecional. | REPROVADO |
| T122 | Baseline sem metadado de vigência. | REPROVADO |

### ADR-053 (T123–T132)

| T | Texto | Resultado esperado |
|---|---|---|
| T123 | Critério objetivo presente (norma sem uso operacional). | APROVADO |
| T124 | Critério objetivo ausente. | REPROVADO |
| T125 | Justificativa registrada. | APROVADO |
| T126 | Justificativa ausente. | REPROVADO |
| T127 | Norma ainda necessária. | REPROVADO |
| T128 | Norma sem uso operacional. | APROVADO |
| T129 | Auditoria recupera critérios. | APROVADO |
| T130 | Critérios não recuperáveis. | REPROVADO |
| T131 | Deprecated não é revogado. | APROVADO |
| T132 | Depreciação tentando revogar. | REPROVADO |

### ADR-054 (T133–T146)

| T | Texto | Resultado esperado |
|---|---|---|
| T133 | Conflito escalado gera decisão formal sob CRR42. | APROVADO |
| T134 | Conflito escalado sem decisão. | REPROVADO |
| T135 | Registro usando CRR63. | APROVADO |
| T136 | Registro paralelo, fora de CRR63. | REPROVADO |
| T137 | Resolução produz artefato formal. | APROVADO |
| T138 | Encerramento sem artefato. | REPROVADO |
| T139 | Uso correto dos processos vigentes completos. | APROVADO |
| T140 | Mecanismo alternativo/atalho criado. | REPROVADO |
| T141 | Resolução dentro do prazo do nível de governança. | APROVADO |
| T142 | Prazo excedido. | REPROVADO |
| T143 | Exceção encerrada formalmente. | APROVADO |
| T144 | Exceção sem encerramento formal. | REPROVADO |
| T145 | Cadeia completa reconstruível (gatilho+autoridade+decisão+artefato+registro). | APROVADO |
| T146 | Cadeia incompleta (falta autoridade, gatilho ou artefato). | REPROVADO |

### ADR-055 (T147–T156)

| T | Texto | Resultado esperado |
|---|---|---|
| T147 | Aprovação produz transição para Deprecated. | APROVADO |
| T148 | Depreciação sem aprovação formal. | REPROVADO |
| T149 | Registro completo de aprovação (autoridade+decisão+resultado). | APROVADO |
| T150 | Decisão sem registro formal. | REPROVADO |
| T151 | Rejeição preserva estado anterior. | APROVADO |
| T152 | Rejeição altera estado indevidamente. | REPROVADO |
| T153 | Prazo de deliberação respeitado (CRR84). | APROVADO |
| T154 | Prazo expirado sem deliberação. | REPROVADO |
| T155 | Cadeia completa reconstruível. | APROVADO |
| T156 | Cadeia incompleta. | REPROVADO |

---

## 8.11 Teste de Adoção

Nenhuma prática nova de processo é introduzida nesta consolidação. O capítulo materializa decisões já aprovadas em ADR-050 a ADR-055, formalizando o mesmo padrão de fundação-antes-de-consolidação já validado nos Capítulos 6 e 7.

| Critério | Resultado |
|---|---|
| Risco | Baixo |
| Custo | Baixo |
| Flexibilidade | Alta |
| Decisão | Aprovado |

---

## 8.12 Tabela De-Para Final

| Bloco | CP | CRR vigentes | CRR consolidadas/reservadas | T |
|---|---|---|---|---|
| ADR-050 REV.1 | CP34 | CRR58, CRR59, CRR60, CRR61, CRR62 | — | T99–T104 |
| ADR-051 REV.2 | CP35 | CRR63, CRR64, CRR65, CRR66, CRR67, CRR68 | — | T105–T111 |
| ADR-052 REV.2 | CP36 | CRR69, CRR70, CRR71, CRR72, CRR73, CRR74 | — | T112–T122 |
| ADR-053 REV.1 | CP37 | CRR75, CRR76, CRR77, CRR78, CRR79 | — | T123–T132 |
| ADR-054 REV.1 | CP38 | CRR80, CRR81, CRR82, CRR83, CRR84, CRR85, CRR86 | — | T133–T146 |
| ADR-055 | CP39 | CRR87, CRR88, CRR89, CRR90, CRR91, CRR92 | — | T147–T156 |
| Reservado (herdado Cap.6) | — | — | CRR31, CRR32 (não utilizados) | — |

**Verificação de integridade:** CP34–39 = 6/6 presentes. CRR58–92 = 35/35 rastreadas, todas Vigentes, sem consolidação neste capítulo. T99–156 = 58/58 sem colisão. Nenhum identificador redefinido após registro como Vigente. Reconciliação idêntica à MIC8 mantida pelo Controlador.

---

## 8.13 Resultado Normativo

Este capítulo estabelece que desvios do fluxo normal — exceções, conflitos, revogações, sucessão de baselines e depreciação — são sempre governados, nunca implícitos: toda exceção tem prazo e encerramento formal; todo conflito tem resolução obrigatória e produz artefato; toda revogação é explícita e preserva histórico; toda baseline substituída permanece navegável; e toda depreciação exige tanto critério objetivo de candidatura quanto decisão formal de autoridade antes de produzir efeito.

Nenhum mecanismo paralelo aos já existentes (CRR42, CRR63, PPQ-001 §3) foi criado — todo o capítulo opera por reutilização e extensão compatível dos processos vigentes desde os Capítulos 1 a 7.

---

**Status:** Fundação Encerrada (M8-002) — **este documento ainda não é CONGELADO.** Falta: (1) Auditoria de Cobertura final desta redação específica pelo Analista (Mecanismo 3, aplicado ao texto consolidado, não apenas à MIC), (2) declaração de consenso de Andraus referenciando este documento.

**Nota de processo:** construído pelo Controlador por extração literal da MIC8; nenhum conteúdo foi gerado a partir de memória, paráfrase ou regeneração de texto. Devolvido ao Analista para Auditoria de Cobertura antes de qualquer declaração de consenso.
