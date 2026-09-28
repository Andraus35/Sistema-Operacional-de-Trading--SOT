# GMC-001 — Canonical Models Governance Specification
## Versão Consolidada Pós-Auditoria — Baseline 1.0
**Status:** CONGELADO por consenso de Andraus
**Projeto:** ORYX AGENT | **Camada:** Governança (Layer 1)

---

## Capítulo 1 — Política de Governança dos Modelos Canônicos

### Documento
GMC-001 — Canonical Models Governance Specification

### Categoria
Governança Arquitetural do SOT

### Código
GMC-001

### Missão
Estabelecer as diretrizes, princípios e critérios para criação, evolução, versionamento e descontinuação dos Modelos Canônicos utilizados pela arquitetura do SOT.

Esta política garante que a camada de Modelos Canônicos permaneça coesa, enxuta, reutilizável e alinhada aos princípios de governança da arquitetura.

### Objetivo
Garantir que novos Modelos Canônicos sejam criados apenas quando representarem contratos cognitivos universais necessários ao funcionamento do ecossistema do SOT. Evitar a proliferação de modelos redundantes, específicos ou de baixo reaproveitamento.

### Escopo
Esta política aplica-se a: todos os Modelos Canônicos existentes, futuras propostas de novos Modelos Canônicos, processos de revisão desses modelos e governança do Kernel Cognitivo.

### Definição de Modelo Canônico
Um Modelo Canônico é um contrato arquitetural que define a representação padronizada de um conceito cognitivo compartilhado entre múltiplos agentes ou componentes do SOT. Ele não pertence a um agente específico. Ele pertence à arquitetura.

### Princípios Fundamentais

**Princípio 1 — Universalidade**
Todo Modelo Canônico deverá representar um conceito válido para todo o ecossistema do SOT. Modelos específicos de um único agente não deverão ser promovidos à categoria de Modelo Canônico.

**Princípio 2 — Neutralidade**
O modelo deverá ser independente de qualquer disciplina especializada. Não poderá conter regras específicas de Elliott, ICT, SMC, macroeconomia ou qualquer outro domínio.

**Princípio 3 — Reutilização**
O modelo deverá ser consumido por múltiplos agentes ou componentes. Se um conceito for utilizado exclusivamente por um único agente, ele deverá permanecer na especificação desse agente.

**Princípio 4 — Baixo Acoplamento**
A existência do Modelo Canônico deverá reduzir o acoplamento entre componentes da arquitetura. Sua criação nunca deverá aumentar dependências desnecessárias.

**Princípio 5 — Governança Centralizada**
Toda evolução de um Modelo Canônico deverá ocorrer por meio do processo formal de governança da arquitetura do SOT. Nenhum agente poderá alterar autonomamente um Modelo Canônico.

### Critérios Obrigatórios para Criação

Um novo Modelo Canônico somente poderá ser criado quando atender simultaneamente aos seguintes critérios:

- **Critério 1 — Contrato Compartilhado:** representar um contrato utilizado por diversos agentes ou componentes.
- **Critério 2 — Independência Funcional:** possuir significado próprio, independentemente do agente que o produz ou consome.
- **Critério 3 — Reutilização Arquitetural:** eliminar duplicidade de representação entre componentes.
- **Critério 4 — Ciclo de Vida Próprio:** possuir estados, evolução ou governança independentes.
- **Critério 5 — Valor Arquitetural:** sua criação deverá simplificar a arquitetura ou aumentar sua consistência. Modelos criados apenas para organização documental não atendem este critério.

### Critérios para Não Criação

Um Modelo Canônico não deverá ser criado quando: representar apenas conceitos internos de um agente; existir apenas para organização da documentação; duplicar responsabilidades já existentes; não possuir consumidores múltiplos; não agregar valor arquitetural mensurável.

### Processo de Aprovação

Toda proposta deverá passar pelas seguintes etapas: (1) Identificação da necessidade; (2) Avaliação dos critérios obrigatórios; (3) Análise de impacto arquitetural; (4) Aprovação da governança do SOT; (5) Criação da especificação oficial; (6) Inclusão no Catálogo Oficial de Modelos Canônicos.

### Evolução dos Modelos Canônicos

Todo Modelo Canônico deverá: possuir versionamento; preservar compatibilidade sempre que possível; documentar alterações; manter histórico de evolução. Mudanças incompatíveis deverão ser tratadas como nova versão arquitetural.

### Estado dos Modelos Canônicos

O conjunto vigente de Modelos Canônicos aprovados é definido exclusivamente pelo Catálogo Oficial de Modelos Canônicos. O GMC-001 não mantém listas normativas de modelos específicos, preservando o Catálogo Oficial como fonte única de verdade para o estado da arquitetura.

### Independência entre Modelos Canônicos

Nenhum Modelo Canônico possui autoridade normativa sobre outro Modelo Canônico. Modelos Canônicos podem utilizar conceitos definidos por outros modelos, mas não podem modificar, governar ou redefinir contratos que não lhes pertencem. A coordenação entre modelos, resolução de conflitos e harmonização arquitetural pertencem exclusivamente ao GMC-001.

### Critérios de Aceitação

Esta política será considerada conforme quando: impedir a criação indiscriminada de Modelos Canônicos; garantir que cada Modelo Canônico represente um contrato universal; preservar a simplicidade e a consistência da arquitetura; assegurar governança e evolução controlada da camada de Modelos Canônicos.

---

## Capítulo 2 — Estrutura de Governança e Autoridades Arquiteturais

### Objetivo do Capítulo
Definir a estrutura formal de governança responsável pela criação, evolução, aprovação, auditoria, homologação e manutenção dos Modelos Canônicos do ecossistema ORYX/SOT.

### Princípio Fundamental
A governança dos Modelos Canônicos deve ser centralizada, rastreável e auditável. Nenhum Modelo Canônico pode evoluir sem passar pela estrutura formal de governança definida pelo GMC-001.

### Estrutura de Governança
A governança dos Modelos Canônicos é composta por papéis arquiteturais especializados. Esses papéis não representam componentes do sistema — representam funções de governança.

**Papel: Estrategista**
Missão: projetar e evoluir a arquitetura conceitual dos Modelos Canônicos.
Responsabilidades: elaborar especificações; propor novos modelos; propor alterações; responder às auditorias; incorporar correções; manter coerência arquitetural entre modelos; elaborar análises de impacto.
Limitação: não possui autoridade para aprovar suas próprias propostas.

**Papel: Analista**
Missão: realizar auditoria independente das especificações arquiteturais.
Responsabilidades: verificar consistência interna; verificar consistência cruzada; identificar conflitos; avaliar aderência ao GMC-001; emitir parecer técnico; classificar observações (Crítica/Média/Menor).
Limitação: não aprova modelos. Apenas recomenda aprovação, correção ou rejeição.

**Papel: Controlador**
Missão: atuar como autoridade formal de registro arquitetural.
Responsabilidades: homologar modelos aprovados; registrar versões oficiais; manter o Catálogo Oficial; registrar congelamentos; registrar descontinuações; preservar histórico.
Autoridade: constitui a autoridade formal de homologação arquitetural do ecossistema ORYX/SOT.
Limitação: não executa auditorias.

**Papel: Usuário (Autoridade de Validação Estratégica)**
O Usuário constitui uma extensão formal da estrutura de governança. Os papéis arquiteturais fundamentais permanecem Estrategista, Analista e Controlador. O processo de governança reconhece adicionalmente o Usuário como autoridade de validação estratégica.
Responsabilidades: validar consenso arquitetural; aprovar congelamento de baselines; solicitar reabertura de documentos; arbitrar divergências não resolvidas entre Estrategista e Analista.
Limitação: não substitui auditoria técnica, homologação documental ou manutenção do Catálogo.

### Processo de Governança

```
Estrategista → Analista → Correções → Analista → Aprovação Técnica
    → Usuário (consenso) → Controlador (homologação) → Catálogo Oficial
```

### Iniciação Formal de Propostas
Uma proposta de Modelo Canônico passa a existir formalmente quando: recebe um código provisório; possui escopo arquitetural definido; é registrada em estado DRAFT. Ideias, discussões ou análises preliminares anteriores a esse registro não constituem propostas formais.

### Aprovação Arquitetural
Um Modelo Canônico somente poderá ser encaminhado ao Controlador quando: todos os capítulos obrigatórios estiverem concluídos; não existirem inconsistências críticas abertas; todas as auditorias obrigatórias estiverem concluídas; existir consenso arquitetural registrado.

A Aprovação Técnica ocorre quando o Analista emite parecer positivo sem inconsistências bloqueantes abertas. Esse parecer autoriza a transição do Modelo Canônico para o estado APPROVED e seu encaminhamento ao Controlador para homologação.

### Homologação
A homologação transforma uma especificação em ativo arquitetural oficial. Após homologação: o modelo torna-se parte do Catálogo Oficial; passa a possuir versão oficial; torna-se referência normativa para a arquitetura.

### Estados de Governança

| Estado | Significado |
|---|---|
| DRAFT | Em elaboração |
| UNDER_REVIEW | Em auditoria |
| APPROVED | Aprovado tecnicamente — estado transitório entre aprovação técnica e homologação pelo Controlador |
| BASELINED | Homologado e congelado |
| DEPRECATED | Em processo de descontinuação |
| RETIRED | Retirado oficialmente |
| REJECTED | Proposta encerrada sem aprovação |

**Regra do estado APPROVED:** É um estado transitório. Todo modelo APPROVED deverá ser encaminhado ao Controlador para homologação ou ter sua aprovação revogada mediante justificativa formal registrada. Nenhum modelo deverá permanecer indefinidamente em estado APPROVED.

**Estado REJECTED:** Preserva histórico da proposta, justificativas da rejeição e rastreabilidade do processo decisório. Uma proposta rejeitada poderá originar nova proposta futura, porém esta deverá iniciar novo ciclo de governança.

### Catálogo Oficial

O Catálogo Oficial constitui a única fonte autorizada para consulta dos Modelos Canônicos vigentes. O catálogo deverá registrar: código do modelo; nome oficial; versão vigente; **baseline vigente**; status atual; histórico resumido.

### Independência dos Papéis
Nenhum papel possui autoridade absoluta. O sistema opera por segregação de responsabilidades: Estrategista propõe; Analista audita; Usuário valida consenso; Controlador homologa.

### Descontinuação de Modelos
Um Modelo Canônico poderá entrar em processo formal de descontinuação quando tornar-se obsoleto, for substituído por versão incompatível, perder valor arquitetural, ou for absorvido por outro modelo. A descontinuação deverá preservar histórico e rastreabilidade. O procedimento detalhado será definido em capítulo específico.

### Coordenação entre Modelos
O GMC-001 não atua como componente operacional. Sua função é definir regras de coordenação. A aplicação dessas regras ocorre através dos papéis de governança definidos neste capítulo.

### Critérios de Aceitação
Este capítulo será considerado conforme quando: existir autoridade formal para homologação; existir separação clara entre proposta, auditoria e homologação; existir mecanismo oficial para manutenção do Catálogo; existir definição dos estados de governança; existir processo formal para evolução dos Modelos Canônicos.

---

## Capítulo 3 — Evolução, Versionamento e Compatibilidade dos Modelos Canônicos

### Objetivo
Definir as regras que governam a evolução dos Modelos Canônicos ao longo do tempo, garantindo estabilidade arquitetural, compatibilidade controlada e preservação da interoperabilidade do ecossistema ORYX/SOT.

### Princípio Fundamental
Modelos Canônicos são contratos arquiteturais compartilhados. Toda evolução deve preservar a confiança dos componentes que dependem desses contratos. Mudanças não controladas são consideradas risco arquitetural.

### Princípio da Estabilidade Evolutiva
Uma vez homologado e incorporado ao Catálogo Oficial, um Modelo Canônico passa a constituir parte da baseline arquitetural do ecossistema. A evolução deve privilegiar: estabilidade; previsibilidade; compatibilidade; rastreabilidade; simplicidade.

### Autoridade sobre Classificações de Evolução
As categorias de evolução definidas neste capítulo constituem a classificação oficial e universal para todos os Modelos Canônicos governados pelo GMC-001. Modelos Canônicos individuais poderão referenciar essas categorias para fins explicativos, mas não deverão manter definições normativas independentes que entrem em conflito com esta especificação. Em caso de divergência, prevalece a definição estabelecida pelo GMC-001.

### Classificação das Alterações

**Categoria A — Extensão**
Alteração que amplia capacidades sem modificar a estrutura do contrato.
Exemplos: inclusão de novos valores em Governed Enumerations; inclusão de novos estados previamente previstos.
Características: não altera consumidores existentes; não altera produtores existentes; compatibilidade integral preservada.

**Categoria B — Ampliação Estrutural Compatível**
Alteração que expande o contrato mantendo compatibilidade.
Exemplos: novo campo opcional; novo relacionamento opcional.
Características: consumidores e produtores existentes continuam operando; adaptação opcional.
**Regra de compatibilidade:** Uma Ampliação Estrutural somente será classificada como Categoria B quando preservar compatibilidade com produtores e consumidores existentes. Novos campos adicionados ao contrato deverão ser opcionais para implementações existentes.
**Reclassificação automática para Categoria C:** Uma proposta será automaticamente classificada como Categoria C quando: introduzir campo obrigatório; exigir alteração em produtores existentes; exigir alteração em consumidores existentes; modificar comportamento previamente válido.

**Categoria C — Alteração Incompatível**
Alteração que rompe contratos previamente válidos.
Exemplos: remoção de campo obrigatório; alteração semântica de elemento existente; mudança que exige adaptação de consumidores existentes.
Características: compatibilidade rompida; exige nova versão principal.

### Política de Versionamento

Formato canônico: `MAJOR.MINOR`

- Versão MINOR: incrementada para Categoria A e Categoria B.
- Versão MAJOR: incrementada para Categoria C.

### Compatibilidade Retroativa

A compatibilidade retroativa constitui objetivo prioritário da governança. Toda proposta deverá demonstrar explicitamente: impacto em produtores; impacto em consumidores; impacto em repositórios; impacto em modelos dependentes. Na ausência dessa demonstração, a proposta não poderá avançar para avaliação.

### Análise de Impacto Obrigatória

Toda alteração proposta deverá conter avaliação formal de impacto respondendo: (1) Quais componentes serão afetados? (2) Quais modelos serão afetados? (3) Há quebra de compatibilidade? (4) Existe alternativa menos invasiva? (5) A alteração simplifica ou aumenta complexidade?

A Análise de Impacto constitui requisito obrigatório da proposta de alteração. Sua elaboração é responsabilidade do Estrategista. A verificação de completude, consistência e precisão da análise é responsabilidade do Analista durante o processo de auditoria.

### Coexistência de Versões

Versões distintas de um mesmo Modelo Canônico poderão coexistir temporariamente durante processos de migração arquitetural. Entretanto: apenas uma versão poderá possuir status BASELINE; versões anteriores permanecem registradas no Catálogo; versões substituídas permanecem auditáveis.

### Política de Depreciação

**Elemento Deprecated:** elemento oficialmente marcado para remoção futura. Continua válido, continua suportado, permanece documentado, não deve ser utilizado em novas implementações.

Toda depreciação deverá: ser registrada no histórico oficial; indicar justificativa; indicar versão de marcação; indicar versão prevista para remoção.

**Prazo mínimo:** nenhum elemento poderá ser removido antes de uma nova versão MAJOR subsequente.

### Substituição de Modelos Canônicos

A substituição de um Modelo Canônico por outro poderá ocorrer quando: o modelo existente tornar-se arquiteturalmente inadequado; houver sobreposição irreconciliável de responsabilidades; uma nova abordagem arquitetural for formalmente aprovada. Toda substituição deverá preservar rastreabilidade histórica entre o modelo substituído e seu sucessor. O processo formal de substituição de Modelos Canônicos será definido em capítulo específico do GMC-001.

### Descontinuação de Modelos Canônicos

A descontinuação: não implica remoção histórica; não implica perda de auditabilidade; não implica exclusão do Catálogo. Status permitido: DEPRECATED ou RETIRED, conforme definido pelos capítulos subsequentes.

### Coordenação entre Modelos

Quando uma alteração em um Modelo Canônico impactar outro Modelo Canônico, a governança deverá coordenar a evolução de forma consistente. O GMC-001 define as regras de coordenação arquitetural. Não executa coordenação operacional como componente ativo do sistema. A execução do processo pertence às instâncias de governança definidas nos capítulos posteriores.

### Critérios de Aceitação

Este capítulo será considerado conforme quando: toda alteração possuir classificação formal; todo modelo possuir versionamento explícito; compatibilidade for analisada antes da aprovação; coexistência de versões estiver disciplinada; depreciações forem controladas; substituições forem rastreáveis; descontinuações preservarem histórico; a baseline vigente puder ser identificada de forma inequívoca.

---

## Capítulo 4 — Catálogo Oficial de Modelos Canônicos

### Objetivo do Capítulo
Definir a estrutura, responsabilidades, regras de operação e critérios de integridade do Catálogo Oficial de Modelos Canônicos do ecossistema ORYX/SOT.

### Princípio Fundamental
Todo Modelo Canônico oficialmente reconhecido pela arquitetura deverá estar registrado no Catálogo Oficial. Nenhum modelo possui existência arquitetural oficial fora do Catálogo.

### Natureza do Catálogo
O Catálogo Oficial é um registro arquitetural. Ele não substitui: a documentação técnica dos modelos; as especificações dos modelos; os processos de governança. Sua função é registrar oficialmente o estado dos Modelos Canônicos aprovados.

### Single Source of Truth

**Regra de Prevalência:** O Catálogo Oficial constitui a fonte autoritativa para informações de: estado; versão; baseline vigente; situação de aprovação; situação de descontinuação. Em caso de divergência documental relacionada a essas informações, prevalece o Catálogo Oficial. O conteúdo normativo de cada Modelo Canônico permanece autoridade exclusiva sobre sua própria especificação técnica. O Catálogo não substitui nem altera o conteúdo normativo dos Modelos Canônicos. Sua função é exclusivamente registrar seu estado oficial na arquitetura.

### Responsabilidade de Manutenção
A manutenção do Catálogo é responsabilidade exclusiva do Controlador. Somente o Controlador poderá: registrar novos modelos; registrar novas versões; registrar homologações; registrar baselines; registrar depreciações; registrar aposentadorias (RETIRED).

### Estrutura Mínima de Registro

| Campo | Obrigatório |
|---|---|
| Código | Sim |
| Nome Oficial | Sim |
| Categoria | Sim |
| Versão Vigente | Sim |
| Baseline Vigente | Sim |
| Status Atual | Sim |
| Data de Registro | Sim |

**Campo Categoria:** Categoria arquitetural do Modelo Canônico. Governed Enumeration sob GMC-001. Valores atualmente aprovados: EVIDENCE_MODEL, GOVERNANCE_MODEL. Novas categorias poderão ser adicionadas mediante processo formal de governança.

### Identificador Canônico

Formato recomendado: `<DOMÍNIO>-<NÚMERO>` (ex: CEM-001, GMC-001, CHM-001). O identificador é permanente e não poderá ser reutilizado.

### Estados Oficiais do Catálogo

| Estado | Significado |
|---|---|
| DRAFT | Em elaboração |
| UNDER_REVIEW | Em auditoria |
| APPROVED | Aprovado tecnicamente |
| BASELINED | Homologado oficialmente |
| SUPERSEDED | Substituído por versão posterior |
| DEPRECATED | Em processo de descontinuação |
| RETIRED | Retirado oficialmente |
| REJECTED | Encerrado sem aprovação |

**Nota Normativa — Estado SUPERSEDED:** O estado SUPERSEDED constitui um estado exclusivo do Catálogo Oficial de Modelos Canônicos. Sua finalidade é representar que determinada versão foi substituída por uma versão posterior do mesmo Modelo Canônico. SUPERSEDED não constitui estado de governança arquitetural do ciclo de vida definido no Capítulo 2. Os estados de governança permanecem exclusivamente: DRAFT, UNDER_REVIEW, APPROVED, BASELINED, DEPRECATED, RETIRED, REJECTED. O estado SUPERSEDED existe apenas para fins de rastreabilidade de versões dentro do Catálogo Oficial.

### Regra de Baseline
Para cada Modelo Canônico poderá existir apenas uma versão em estado BASELINED simultaneamente.

### Histórico Permanente
O Catálogo deverá preservar permanentemente: versões anteriores; homologações; substituições; depreciações; aposentadorias; rejeições. Nenhum registro poderá ser removido.

### Registro de Evoluções
Toda evolução homologada deverá registrar: versão anterior; versão nova; categoria da alteração (A, B ou C); data da homologação.

### Registro de Substituições e Descontinuação
Quando um Modelo Canônico for substituído por outro, o Catálogo deverá registrar: modelo substituído; modelo sucessor; justificativa resumida; data da substituição. Quando um modelo entrar em processo de descontinuação: data da depreciação; justificativa resumida; versão afetada; previsão de retirada, quando aplicável.

### Integridade do Catálogo
O Catálogo deverá garantir: unicidade de identificadores; rastreabilidade histórica; consistência de versões; consistência de estados; preservação permanente dos registros.

### Consulta ao Catálogo
Qualquer processo de governança deverá utilizar o Catálogo como referência oficial antes de: propor novos modelos; propor alterações; iniciar auditorias; registrar homologações.

### Critérios de Aceitação
Este capítulo será considerado conforme quando: existir uma única fonte oficial de consulta; todo Modelo Canônico possuir registro identificável; todo histórico permanecer preservado; existir rastreabilidade de versões, substituições e descontinuações; a baseline vigente puder ser identificada sem ambiguidade.

---

## Capítulo 5 — Governança de Propostas, Auditorias e Aprovações

### Objetivo do Capítulo
Definir como propostas relacionadas aos Modelos Canônicos são submetidas, auditadas, aprovadas, rejeitadas e registradas dentro da governança arquitetural do ecossistema ORYX/SOT. Este capítulo transforma os princípios definidos nos capítulos anteriores em um fluxo operacional verificável.

### Princípio Fundamental
Nenhuma alteração em um Modelo Canônico produz efeitos arquiteturais antes de completar o processo formal de governança definido pelo GMC-001.

### Escopo de Governança
O processo aplica-se a: criação de novos Modelos Canônicos; evolução de modelos existentes; substituição de modelos; depreciação de modelos; retirada (retirement) de modelos; mudanças de baseline.

### Princípio da Segregação de Responsabilidades
A governança utiliza separação explícita de responsabilidades para reduzir vieses e aumentar a qualidade arquitetural. Nenhum papel executa simultaneamente proposição, auditoria e registro final.

### Autoridade de Validação Estratégica
O Usuário constitui uma extensão formal da estrutura de governança definida no Capítulo 2. Os papéis arquiteturais fundamentais permanecem Estrategista, Analista e Controlador. O processo de governança reconhece adicionalmente o Usuário como Autoridade de Validação Estratégica, responsável por: validar consenso arquitetural; aprovar congelamento de baselines; solicitar reabertura de documentos; arbitrar divergências não resolvidas entre Estrategista e Analista. O Usuário não substitui auditoria técnica, homologação documental ou manutenção do Catálogo.

### Fluxo Canônico de Governança

```
Estrategista → Analista → Usuário → Controlador
```

### Etapa 1 — Proposição
A proposta deverá conter obrigatoriamente: objetivo; justificativa arquitetural; impacto esperado; análise de impacto (responsabilidade do Estrategista); classificação da alteração (A, B ou C quando aplicável). Propostas incompletas não avançam para auditoria.

### Etapa 2 — Auditoria

O Analista deverá avaliar: conformidade com GMC-001; coerência interna; coerência com outros Modelos Canônicos; aderência aos princípios arquiteturais; riscos de compatibilidade.

**Resultados de auditoria:**

| Resultado | Significado |
|---|---|
| CONFORME | Apto para aprovação |
| CONFORME COM OBSERVAÇÕES | Ajustes recomendados |
| NÃO CONFORME | Bloqueado |

### Classificação das Observações de Auditoria

A classificação das observações constitui responsabilidade exclusiva do Analista e integra formalmente o parecer técnico.

**Crítica:** impede aprovação; quebra arquitetural, conflito normativo, inconsistência estrutural, violação de princípios fundamentais. Resultado mínimo: NÃO CONFORME.

**Média:** não impede aprovação, mas exige correção antes do congelamento. Resultado típico: CONFORME COM OBSERVAÇÕES.

**Menor:** melhoria recomendada sem impacto arquitetural relevante. Pode coexistir com CONFORME ou CONFORME COM OBSERVAÇÕES.

**Divergências de Classificação:** caso exista discordância entre Estrategista e Analista sobre a classificação atribuída, o parecer técnico do Analista permanece válido; a divergência poderá ser submetida ao Usuário para validação estratégica; a decisão do Usuário encerra a divergência para aquele ciclo de governança.

### Transições de Estado após Auditoria

| Resultado da Auditoria | Estado Resultante no Catálogo |
|---|---|
| CONFORME | APPROVED |
| CONFORME COM OBSERVAÇÕES | UNDER_REVIEW |
| NÃO CONFORME | DRAFT |

O retorno a DRAFT deverá registrar: data; justificativa; observações bloqueantes.

### Etapa 3 — Consenso
Após auditoria, o Usuário poderá: aprovar; solicitar ajustes; solicitar nova auditoria; encerrar a proposta. O consenso encerra a fase técnica.

### Etapa 4 — Registro Oficial
Após consenso: o Controlador deverá registrar: decisão; versão; estado; baseline (quando aplicável); histórico da decisão. Somente após o registro a decisão torna-se oficial.

### Regra de Congelamento
Um documento é considerado congelado quando: recebeu parecer conforme; recebeu consenso do Usuário; foi registrado pelo Controlador. Antes disso permanece em elaboração.

### Regra de Baseline
Um documento congelado poderá ou não tornar-se baseline. A condição de baseline exige registro explícito no Catálogo Oficial.

### Estado Inicial de Documentos Reabertos
Quando um documento for formalmente reaberto: inicia-se novo ciclo de governança; preserva-se integralmente o histórico anterior; o documento retorna ao estado DRAFT.

Transições:
```
BASELINED → DRAFT
APPROVED → DRAFT
DEPRECATED → DRAFT
```

A reabertura não altera versões anteriores, registros históricos, decisões registradas ou estados previamente homologados. O baseline anteriormente vigente permanece preservado no Catálogo até a homologação de uma nova versão. Quando nova versão for homologada: baseline anterior → SUPERSEDED; nova versão → BASELINED.

### Registro de Backlog Arquitetural
Observações não bloqueantes poderão ser registradas como backlog arquitetural. O backlog: não altera a baseline vigente; não cria obrigação imediata de revisão; preserva rastreabilidade de melhorias futuras.

### Critério de Independência
A aprovação de um Modelo Canônico não implica aprovação automática de outro. Cada modelo deverá percorrer seu próprio processo de governança.

### Critério de Auditabilidade
Todo processo deverá permitir reconstrução posterior de: proposta original; auditorias realizadas; correções incorporadas; decisão final; registro oficial.

### Critérios de Aceitação
Este capítulo será considerado conforme quando: existir fluxo formal de governança; existir segregação de responsabilidades; auditorias forem obrigatórias; aprovações forem rastreáveis; congelamentos forem verificáveis; registros oficiais forem obrigatórios; decisões puderem ser reconstruídas posteriormente.

---

## Registro de Congelamento

| Campo | Valor |
|---|---|
| Documento | GMC-001 — Canonical Models Governance Specification |
| Versão | Baseline 1.0 |
| Status | CONGELADO por consenso de Andraus |
| Capítulos | 5 (completo) |
| Modelo Canônico único aprovado atualmente | CEM-001 Baseline 1.0 |
| Categoria no Catálogo | GOVERNANCE_MODEL |
