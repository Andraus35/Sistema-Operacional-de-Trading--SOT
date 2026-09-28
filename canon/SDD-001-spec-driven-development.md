# SDD-001 — Protocolo de Spec-Driven Development do ORYX AGENT

**Adaptação da ciência do GitHub Spec Kit à arquitetura já congelada — documento de uso obrigatório para Estrategista, Analista e Controlador**

| Campo | Valor |
|---|---|
| Versão | 1.1 (Congelada — Baseline) |
| Status | **CONGELADO por consenso direto de Andraus** |
| Camada | Governança (Layer 1) — documento operacional, referenciado por PPQ-001 e GES |
| Dependências | PPQ-001 (Baseline 1.2), GES (Doc. 12), CEE-001, CR-001 |
| Referência externa | GitHub Spec Kit (constitution → specify → plan → tasks → implement); práticas de mercado 2025-2026 |

---

## 0. Contexto e Vínculo

### 0.1 Nota de processo

Este documento foi redigido nesta mesma sessão que normalmente exerce o papel de Analista — não pelo Estrategista, como o fluxo padrão do PPQ-001 (§4.3 RACI) prevê. Isso foi uma exceção registrada, não um novo padrão: o rascunho e a auditoria não foram feitos por partes independentes. **Andraus optou por consenso direto, ciente dessa condição**, em vez de exigir revisão independente do Estrategista antes de congelar. Isso está dentro da autoridade do RACI (§4.3 do PPQ-001 — Andraus é sempre o Aprovador final), mas fica registrado aqui para que qualquer auditoria futura entenda por que este documento não passou pela dupla checagem padrão.

### 0.2 Por que este documento existe

A auditoria anterior mostrou que o ORYX já tem a **camada de governança** do Spec-Driven Development (Constituição via GES, agente auditor separado via Analista, registro de evidência via CR-001) — mas não tem, ainda, a **camada operacional**: artefatos formalmente separados de Spec/Plan/Tasks, um gate de checagem constitucional explícito por proposta, e uma regra clara de qual lado (spec ou execução) cede quando os dois divergem.

O SDD-001 fecha essa lacuna, reaproveitando o que já existe em vez de recriar.

---

## 1. Missão

Trazer o ORYX AGENT ao mesmo nível de estruturação técnica que projetos profissionais adotando Spec-Driven Development (GitHub Spec Kit e equivalentes) praticam em 2026 — sem importar burocracia desnecessária, seguindo a Diretriz Mestra do PPQ-001 §3 (rigor proporcional, testado pelo Teste de Adoção §3.3).

Isso significa: todo componente novo do ORYX (Skill, Agente, Documento de arquitetura) passa a nascer com três artefatos formalmente distintos — **Spec** (o quê), **Plan** (como) e **Tasks** (unidades atômicas rastreáveis) — em vez de um único documento que mistura os três níveis, como acontecia até aqui.

---

## 2. Filosofia — Por que Separar Spec, Plan e Tasks

Até agora, os documentos ORYX (CEM-001, GMC-001, CEE-001, PPQ-001) misturam, num único arquivo, a definição do comportamento esperado (Missão, Filosofia, Princípios) com a arquitetura técnica (Corpo técnico) e os critérios de aceite. Isso funcionou até aqui porque cada documento é grande e único. Mas quebra em dois pontos que o SDD resolve diretamente:

- **Revisão fica mais difícil quanto mais a spec e o plano técnico estão misturados** — um revisor de comportamento (ex: Andraus validando se a ideia está certa) precisa ler decisões de arquitetura técnica que não são da sua alçada para aprovar o "o quê".
- **Quando a implementação diverge, não fica claro se o problema é comportamental (a spec) ou técnico (o plano)** — misturar os dois num documento só dificulta isolar a causa.

Princípio central:

> **A Spec descreve o comportamento esperado, sem nenhum detalhe de implementação. O Plan traduz a Spec em arquitetura técnica. As Tasks decompõem o Plan em unidades que podem ser homologadas e rastreadas isoladamente. Nenhuma etapa pula a anterior.**

### 2.1 Nível de Maturidade Adotado: Spec-Anchored

A literatura de SDD reconhece três níveis de rigor: *spec-first* (spec como guia informal), *spec-anchored* (spec como gate de governança formal, com checkpoints de aprovação humana) e *spec-as-source* (spec como único artefato versionado; código é descartável e regenerado a cada vez). O ORYX adota explicitamente **spec-anchored** — não o extremo *spec-as-source*.

Justificativa: o ORYX opera com capital real, exige trilha de auditoria (CR-001) e aprovação humana explícita antes de qualquer mudança de Nível 1/2 (PPQ-001 §10.2) — exatamente o perfil onde a literatura recomenda spec-anchored, reservando spec-as-source para times que podem descartar e regenerar código livremente sem risco regulatório ou financeiro. Isso não é uma limitação — é a escolha correta para o risco deste projeto, e deve ser revisitada apenas se o perfil de risco mudar (PPQ-001 §0).

---

## 3. Os Três Artefatos Obrigatórios

### 3.1 Spec — O Quê (comportamento, sem implementação)

Mapeamento sobre a estrutura já usada: a Spec corresponde às seções **Missão + Filosofia + Princípios + Critérios de Aceitação** que os documentos ORYX já produzem — agora isoladas como artefato próprio, revisável sem precisar entender arquitetura técnica.

```
SPEC — Template

## Missão
[O que este componente faz, em linguagem comportamental, sem menção a
algoritmo, modelo de IA, ou estrutura de dados]

## Escopo
Dentro do escopo: [...]
Fora do escopo (Non-goals): [...]

## Comportamento Esperado
[Descrição do que o componente deve fazer, com casos de uso e casos de
borda — equivalente a user stories + edge cases do Spec Kit]

## Critérios de Aceitação (notação EARS)
[Cada critério escrito no formato: "Quando <gatilho/condição>, o
componente DEVE <resposta esperada>." Ex: "Quando o Structural Agent
detectar quebra de estrutura em H4, DEVE emitir Evidência no formato
EC-COG-002 em até 1 ciclo." Isso torna o critério verificável por
qualquer leitor — humano ou IA — sem ambiguidade de interpretação,
e sem custo adicional real, já que é apenas uma forma mais precisa de
escrever o que já seria escrito de qualquer forma.]

## 5W2H de Justificativa
[Template PPQ-001 §7.1 ou §7.2, conforme o tipo de componente]
```

A Spec **não** contém: nome de modelo de IA, algoritmo específico, estrutura de dados, fluxo de chamadas entre Agentes. Isso é papel do Plan.

### 3.2 Plan — Como (arquitetura técnica)

Corresponde ao que os documentos ORYX já chamam de "Corpo técnico". Formalizado como artefato distinto:

```
PLAN — Template

## Arquitetura
[Como o componente é construído — algoritmos, fontes teóricas
(Elliott/Fibonacci/SMC/ICT), estrutura de dados, contratos com CEM/CHM/CCM/CDM]

## Roteamento de Modelo
[Tipo Cognitivo I-V e classe de modelo recomendada — CEE-001 §5]

## Dependências Técnicas
[Quais outros componentes/documentos este Plan pressupõe]

## Riscos Técnicos e Salvaguardas
[O que pode falhar tecnicamente, e qual Salvaguarda Constitucional protege]

## Impacto em Cache/Custo
[Se aplicável — CEE-001 §6, InferenceContextEnvelope]
```

O Plan é sempre derivado de uma Spec já aprovada — nunca escrito antes ou em paralelo.

### 3.3 Tasks — Unidades Atômicas Rastreáveis

Corresponde aos **Engineering Cards** já usados no KERNEL V2 — formalizados aqui como o terceiro artefato obrigatório, não apenas um item de backlog solto.

```
TASKS — Template

## Lista de Tasks derivadas deste Plan
| ID (Engineering Card) | Descrição | Critério de Aceite individual | Nível GES (PPQ-001 §10.2) |
|---|---|---|---|
| ... | ... | ... | ... |

## Regra de Rastreabilidade
Toda Task deve apontar para a Spec e o Plan que a originaram. Nenhuma
Task existe sem uma Spec aprovada por trás dela — Tasks órfãs (sem Spec)
são automaticamente Nível 3 ou inferior (PPQ-001 §10.2), nunca Nível 1 ou 2.
```

---

## 4. Constitution Check — Gate Obrigatório

Toda Spec nova, antes de avançar para o Plan, passa por uma checagem explícita contra a Constituição já congelada (GES Nível 1) — o mesmo mecanismo que o Spec Kit formaliza como primeiro passo de qualquer projeto.

```
CONSTITUTION CHECK — Checklist obrigatório (Analista)

[ ] A Spec respeita a hierarquia analítica Elliott→Fibonacci→Fractal→SMC→ICT?
[ ] A Spec não redefine nenhum Modelo Canônico (CEM/CHM/CCM/CDM/CNM)?
[ ] Se envolve Convicção, respeita o Conviction Vector **8D** (convicção ≥ 70%, score ≥ 7/9 — Fase Piloto, Q-008/Q-002)? <!-- [LEGADO/SUPERSEDED 2026-09-26] texto original: "4D (Estrutural≥60%+...≥75% total)" — substituído por emenda de compatibilidade SDD-001-EMENDA-001 (Alinhamento Taxonômico); norma: Q-008 (8D) + Q-002 (70% Fase Piloto). Histórico preservado por INV-07. -->
[ ] A Spec não viola nenhuma Salvaguarda Constitucional (CEE-001 §10, GES Nível 1)?
[ ] A Spec declara em qual dos 4 Níveis do GES ela se enquadra (PPQ-001 §10.2)?

Se qualquer item falhar: a Spec é rejeitada ANTES do Plan ser escrito —
nunca depois. Corrigir um Plan que nasceu de uma Spec inconstitucional
é retrabalho evitável.
```

Isso formaliza, com checklist, o que o Analista já faz intuitivamente — mas agora como etapa obrigatória e explícita, não apenas como parte de uma auditoria geral no fim do processo.

---

## 5. Regra da Spec Viva (Living Spec)

Quando a operação real (Missão, backtest, ou NCR do CR-001) revelar uma divergência entre o que a Spec descreve e o que o sistema realmente faz, a regra de desempate é fixa:

```
1. Por padrão, a SPEC é a fonte de verdade — o Plan/Tasks/implementação
   é corrigido para voltar a atender a Spec (isso é só um bug comum).

2. A SPEC só é considerada errada quando o Analista, auditando a
   divergência, concluir que o comportamento real revelou uma lacuna
   ou erro na própria Spec — não apenas um desvio de execução.

3. Se a Spec estiver errada: ela é atualizada PRIMEIRO, e só depois o
   Plan/Tasks são ajustados para seguir a nova versão. Nunca o
   contrário (nunca ajustar a implementação e deixar a Spec desatualizada).

4. Toda atualização de Spec já aprovada segue o mesmo Nível de
   governança (PPQ-001 §10.2) que ela tinha originalmente — uma Spec
   de Nível 1 continua exigindo consenso de Andraus para mudar,
   mesmo que a mudança pareça pequena.
```

Isso se conecta diretamente ao lifecycle NCR já congelado no CR-001 Cap.2 (OPEN→VERIFIED→CLOSED) — uma NCR que revela divergência Spec×Execução é, por definição, um gatilho para este processo.

---

## 6. Estrutura de Organização dos Artefatos

Sem exigir um repositório de código (o ORYX ainda não tem implementação), o CONTROLADOR passa a organizar seu repositório de arquitetura aprovada seguindo esta convenção lógica, para que Spec/Plan/Tasks de cada componente fiquem sempre agrupados e rastreáveis:

```
/arquitetura-aprovada/
  /<nome-do-componente>/
    spec.md          ← Missão, Escopo, Comportamento, Critérios de Aceitação
    plan.md           ← Arquitetura técnica, roteamento, dependências
    tasks.md          ← Engineering Cards derivados, com rastreabilidade
    constitution-check.md  ← Checklist do §4, preenchido e assinado pelo Analista
    historico-versoes.md   ← Mesmo padrão já usado (CEE-001 §14, PPQ-001 §13)
```

Documentos que hoje já existem como arquivo único (CEM-001, GMC-001, SAS-001 Cap.1) **não precisam ser retroativamente divididos** — isso violaria o Teste de Adoção (PPQ-001 §3.3, critério Custo). A convenção vale a partir de agora, para componentes novos ou para capítulos ainda não escritos (ex: CR-001 Cap.7, SAS-001 Cap.2 em diante).

---

## 7. Papéis e Responsabilidades

| Papel | Responsabilidade sob o SDD-001 |
|---|---|
| **Estrategista** | Escreve a Spec primeiro, sozinha, sem Plan. Só escreve o Plan depois que a Spec passou pelo Constitution Check (§4). Só decompõe em Tasks depois que o Plan foi auditado. Nunca entrega os três artefatos juntos de uma vez, exceto para componentes Nível 3/4 (fast-track, PPQ-001 §10.2), onde a separação formal não é exigida. |
| **Analista (este chat)** | Aplica o Constitution Check (§4) antes de qualquer Plan ser aceito. Audita a rastreabilidade Spec→Plan→Tasks (§3.3). Decide, em caso de divergência (§5), se o erro é da Spec ou da execução. |
| **Controlador** | Organiza o repositório conforme §6. Garante que nenhuma Task seja registrada sem Spec e Plan associados. Mantém o histórico de versões de cada artefato separadamente. |
| **Andraus** | Aprova a Spec (comportamento) e o Plan (arquitetura) como decisões potencialmente distintas — pode aprovar uma Spec e pedir revisão do Plan sem reabrir a Spec, o que hoje não é possível porque os dois estão misturados no mesmo documento. |

---

## 8. Fluxo Completo (mapeado ao pipeline ORYX já existente)

```
Constitution (GES Nível 1, já congelado)
        ↓
Specify  → Spec (§3.1) → Constitution Check (§4) → aprovação de Andraus
        ↓
Plan     → Plan (§3.2) → auditoria técnica do Analista → aprovação de Andraus
        ↓
Tasks    → Tasks (§3.3, Engineering Cards) → registrado pelo Controlador
        ↓
Implement → Sandbox → Backtest → Forward Test → Homologação (GES + CEE-001 §8)
        ↓
Validate  → Missão real → CR-001 (NCR se houver divergência) → Regra da Spec Viva (§5)
```

Nenhuma etapa nova foi inventada — o SDD-001 nomeia e formaliza rastreabilidade entre etapas que já existiam soltas.

---

## 9. Right-Sizing — Quando Não Separar os Três Artefatos

Consistente com a Diretriz Mestra (PPQ-001 §3) e o dial de burocracia (PPQ-001 §10.2):

- **Nível 1 e 2** (Constituição e Framework Oficial): separação obrigatória em Spec/Plan/Tasks, com Constitution Check formal.
- **Nível 3** (Conhecimento Certificado — PDFs, indicadores, Pine Scripts): não exige a separação — o pipeline de certificação já existente cumpre o mesmo papel de forma mais leve.
- **Nível 4** (Aprendizado Operacional): não se aplica — não há Spec para uma calibração automática.

Se separar os três artefatos para um item Nível 3/4 estiver consumindo mais esforço do que o próprio item vale, isso é, por definição, o Sinal de Burocracia Excessiva (PPQ-001 §10.6) — pare e reclassifique.

### 9.1 Salvaguarda contra "Vibe Specifying"

O risco simétrico ao de pular a Spec é escrevê-la grande demais para ser revisada de verdade — uma "montanha de markdown" que Andraus aprova por cansaço, não por convicção. Regra objetiva:

> **Se uma Spec não cabe em uma única sessão de revisão por Andraus, ela está grande demais — não porque o limite seja arbitrário, mas porque uma Spec que ninguém revisa de verdade não protege contra nada.**

Quando isso acontecer, a ação correta é a mesma Regra do Corte de Escopo já definida (PPQ-001 §10.3): dividir a Spec em unidades menores, cada uma com seu próprio Constitution Check, em vez de pedir aprovação de um documento longo demais para ser lido com atenção.

---

## 10. Critérios de Aceitação

O SDD-001 será considerado implementado quando:

1. Todo componente novo Nível 1/2 (PPQ-001 §10.2) nascer com Spec e Plan como artefatos formalmente distintos, não misturados num único documento.
2. O Analista aplicar o Constitution Check (§4) antes de aprovar qualquer Plan, com registro explícito do checklist preenchido.
3. Toda Task registrada pelo Controlador apontar rastreavelmente para sua Spec e Plan de origem.
4. Ao menos um caso real de divergência Spec×Execução tiver passado pela Regra da Spec Viva (§5), validando que o processo funciona na prática, não só na teoria.
5. Nenhum documento retroativo já congelado tiver sido forçosamente dividido em Spec/Plan/Tasks — a convenção vale só para o que vem daqui para frente.
6. Critérios de Aceitação de novas Specs estiverem escritos em notação EARS (§3.1), não em prosa livre.
7. Nenhuma Spec tiver sido aprovada sem caber em uma única sessão de revisão de Andraus (§9.1 — salvaguarda contra Vibe Specifying).

---

## 11. Registro para o CONTROLADOR

| Campo | Valor |
|---|---|
| ID do Documento | SDD-001 |
| Nome | Protocolo de Spec-Driven Development do ORYX AGENT |
| Tipo | Documento de Governança (Layer 1) — operacional, transversal |
| Dependências | PPQ-001 (Baseline 1.2), GES (Doc. 12), CEE-001, CR-001 |
| Status | **CONGELADO — Baseline 1.1** — consenso direto de Andraus, ciente da nota de processo §0.1 |
| Prioridade | P1 — aplicar a partir do próximo componente novo proposto (ex: CR-001 Cap.7 ou próxima Skill), não retroativamente |

---

## 12. Histórico de Versões

| Versão | Status | Mudança |
|---|---|---|
| 1.0 | Candidata | Primeira versão — adapta os artefatos do GitHub Spec Kit (Constitution/Spec/Plan/Tasks/Implement) à arquitetura ORYX já existente, sem criar processo paralelo. Redigido pelo Analista, com nota de processo em §0.1 |
| 1.1 | Candidata | Adicionados três refinamentos para paridade real com a prática de ponta 2026: §2.1 declara nível de maturidade adotado (Spec-Anchored, não Spec-as-Source, com justificativa de risco); §3.1 adota notação EARS nos Critérios de Aceitação; §9.1 adiciona salvaguarda contra "Vibe Specifying" (Spec grande demais para revisão real cabe na Regra do Corte de Escopo) |
| 1.1 | **Congelada — Baseline** | Consenso direto de Andraus, com ciência explícita da nota de processo §0.1 (rascunho e auditoria não feitos por partes independentes nesta versão) |

---

*Fim do Documento SDD-001 — Baseline 1.1 (Congelado)*
