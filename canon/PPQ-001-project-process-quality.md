# PPQ-001 — Especificação de Gestão de Projetos, Processos e Qualidade

**Framework de Ciência da Administração aplicado ao ORYX AGENT — e guia de prompts para o Estrategista**

| Campo | Valor |
|---|---|
| Versão | 1.2 (Congelada — Baseline) |
| Status | **CONGELADO por consenso explícito de Andraus** |
| Camada | Governança (Layer 1) — documento transversal, referenciado por todo novo prompt/documento produzido pelo Estrategista |
| Metodologia de projeto adotada | Híbrida — formaliza o pipeline já emergente (Sandbox → Backtest → Forward Test → Homologação) como Stage-Gate |
| Profundidade de BPM adotada | Leve e pragmático — sem notação BPMN completa |
| Escopo de PDCA/5W2H | Três camadas: Skill/Agente, Documento de Arquitetura, Missão Operacional |
| Diretriz mestra | Rigor proporcional e adaptativo à execução por IA — §3 |
| Peso de governança | Calibrado por risco — §10, reaproveitando os 4 Níveis do GES |

---

## 0. Perfil Confirmado do Projeto

Confirmado por Andraus em consenso de congelamento:

1. Projeto solo, com capital próprio — sem sócios ou investidores formais neste momento.
2. Sem prazo rígido — ritmo orientado por qualidade e correção arquitetural, agora balanceado com o dial de agilidade do §10.
3. Equipe = Andraus (decisor final) + Estrategista (GPT) + Analista (esta IA) + Controlador (registro). Nenhuma equipe técnica humana adicional neste momento.
4. Estágio atual = arquitetura/pré-piloto — nenhuma Skill em operação com capital real ainda.

Se o perfil do projeto mudar no futuro (ex: entrada de sócio, equipe técnica, ou início de operação com capital real), o RACI do §4.3 e o dial de burocracia do §10 devem ser revisados — não o restante do documento.

---

## 1. Missão

O PPQ-001 traduz três corpos de conhecimento da ciência da administração — Gestão de Projetos, Gestão de Processos e Gestão da Qualidade — em regras práticas e templates de prompt, para que **toda** documentação futura do ORYX (produzida pelo Estrategista, auditada pelo Analista, registrada pelo Controlador) nasça já estruturada segundo essas disciplinas, em vez de precisar de retrofit depois.

Este documento não cria uma nova burocracia paralela à arquitetura já congelada — ele **nomeia formalmente**, com vocabulário de gestão reconhecido, processos que o ORYX já pratica intuitivamente (GES, Mission Engine, ciclo de vida de documentos), e preenche as lacunas onde a disciplina de gestão ainda não foi aplicada.

---

## 2. Filosofia — Por que Gestão Formal em um Projeto Solo

Projetos solo tendem a pular gestão formal porque "não há ninguém para reportar". Isso é um erro em dois pontos específicos do ORYX:

- Você já opera com **duas IAs em papéis distintos** (Estrategista/Analista) mais um repositório de consenso (Controlador) — isso já é uma estrutura organizacional, mesmo sendo pequena. Sem PM/BPM/Qualidade formalizados, cada IA reinventa seu próprio padrão de trabalho a cada prompt.
- O ORYX vai operar com **capital real e decisões automatizadas** (Bot Trade Finance). Isso eleva o padrão de rigor esperado de "projeto pessoal" para "sistema de missão crítica" — e sistemas de missão crítica são exatamente o domínio onde PDCA, 5W2H e Stage-Gate foram desenhados para funcionar.

Princípio central:

> **Gestão formal não serve para controlar pessoas que você não tem. Serve para dar às suas IAs um contrato de trabalho comum — para que Estrategista, Analista e Controlador falem a mesma língua de processo, não apenas a mesma língua de mercado.**

---

## 3. Diretriz Mestra — Rigor Proporcional e Adaptativo à Execução por IA

Esta é a diretriz que rege a aplicação de todas as demais seções deste documento e, por extensão, de todo o projeto ORYX: busca-se o que há de melhor em ciência de arquitetura, gestão de projetos, processos e qualidade — sem comprometer custo, tempo ou flexibilidade além do que o risco da decisão realmente justifica.

### 3.1 Princípio

> **O ORYX busca o que há de melhor em ciência de administração e arquitetura — mas nunca por adesão automática à "melhor prática" abstrata. Toda prática só é adotada quando comprovadamente melhora o resultado real, sem comprometer custo, tempo ou flexibilidade além do que o risco da decisão justifica.**

Isto não é permissão para relaxar rigor — é a mesma lógica que já fundamenta o Framework 3E do CEE-001 (Eficácia, Eficiência, Efetividade) e o dial de burocracia do §10 deste documento, elevada aqui a princípio explícito que os une e os antecede. Onde houver conflito de interpretação entre esta diretriz e qualquer outra seção deste documento, esta seção prevalece.

### 3.2 Particularidades da Execução por IA que Mudam a Ciência de Administração Clássica

A gestão de projetos, processos e qualidade nasceu para coordenar equipes humanas. O ORYX é executado por Agentes de IA (Estrategista, Analista, e futuramente os Agentes especializados de produção). Isso muda o que "melhor prática" significa em pelo menos cinco pontos:

1. **Custo escala com tokens, não com horas-homem.** Gestão de custo clássica (PMBOK) assume folha de pagamento; o ORYX usa o modelo do CEE-001 (roteamento por classe de modelo, cache, limiares de Fase Piloto) como substituto direto — aplicar um modelo de custo de projeto tradicional sem essa adaptação não faz sentido.
2. **Velocidade de iteração é medida em sessões, não em sprints de semanas.** O time-box do §10.2 (1 a 3 sessões para Nível 2) já reflete isso — cronogramas em dias/semanas, típicos de PM clássico, não se aplicam diretamente quando a "equipe" não dorme, mas isso não é desculpa para pular validação.
3. **IA não hesita nem sinaliza incerteza espontaneamente.** Equipes humanas costumam levantar a mão quando estão inseguras; um Agente de IA, por padrão, produz respostas com confiança aparente uniforme. Por isso o 5W2H (§7) e os Critérios de Aceitação explícitos não são "documentação a mais" — são o mecanismo que força a exposição de lacunas que não apareceriam sozinhas.
4. **Memória não é automática entre sessões.** Uma equipe humana retém contexto tácito; um Agente de IA só retém o que está formalmente registrado (Blackboard, Knowledge Graph, documentos congelados). O custo de *não documentar* é mais alto no ORYX do que seria em um time humano — mas documentar além do necessário também tem custo real de tokens, sem ganho de retenção adicional.
5. **Auditoria substitui supervisão comportamental.** Gestão de qualidade clássica inclui gestão de desempenho de pessoas (motivação, treinamento, avaliação). Isso não se aplica a Agentes de IA. O controle correto é auditoria de saída (o Analista audita o resultado produzido), não gestão do processo de trabalho interno do Agente.

### 3.3 Teste de Adoção — Antes de Incorporar Qualquer Nova Prática de Gestão

Nenhuma prática de PM, BPM ou Qualidade deve ser adotada no ORYX apenas por estar consagrada na literatura. Antes de incorporar qualquer prática nova — sugerida pelo Estrategista, encontrada em pesquisa, ou proposta por Andraus — ela deve passar neste teste de três perguntas:

```
1. Risco  → Essa prática reduz um risco real e específico deste projeto
             (não um risco genérico de "projetos de IA em geral")?
2. Custo  → O custo de adotá-la (tokens, sessões, complexidade de prompt)
             cabe no time-box do nível de governança correspondente (§10.2)?
3. Flex   → Ela preserva a capacidade de mudar de direção rapidamente,
             ou trava decisões que ainda podem precisar mudar?
```

Se a prática falhar em qualquer uma das três perguntas, ela deve ser simplificada até passar, ou descartada. Isso não é diluição de qualidade — é seleção disciplinada. Exemplo já aplicado neste próprio documento: notação BPMN completa falhou no teste de Custo para o tamanho atual do projeto — por isso o §5 usa um template leve de 6 campos, não BPMN.

---

## 4. Gestão de Projetos — Stage-Gate Híbrido

### 4.1 Reconhecimento do que já existe

O ORYX já usa, sem nomear formalmente, um modelo de **Stage-Gate** (também chamado *Phase-Gate*, clássico em gestão de projetos de P&D e engenharia):

```
Sandbox → Backtest → Forward Test → Comparação → Homologação → Produção → Monitoramento
```

Cada seta é um **gate** (portão de decisão) — nada avança sem aprovação explícita. Isso já é Stage-Gate. O que falta é vocabulário de gestão de projeto ao redor dele: escopo, cronograma por fase, gestão de risco, e stakeholders — hoje implícitos, precisam ficar explícitos em todo novo documento.

### 4.2 Mapeamento PMBOK → estruturas ORYX (sem criar nada novo)

| Área de conhecimento (PMBOK) | Onde já existe no ORYX | O que falta formalizar |
|---|---|---|
| Escopo | Missão (Mission Engine), Constituição de 4 níveis (GES) | Todo novo documento/Skill deve declarar explicitamente "está dentro" ou "está fora" de escopo — hoje é implícito |
| Cronograma | Pipeline Sandbox→Backtest→Forward Test→Homologação | Não precisa de datas fixas (sem prazo rígido, premissa §0.2) — mas precisa de **critério de saída** por fase (quando uma fase é considerada concluída) |
| Risco | Salvaguardas Constitucionais espalhadas nos documentos (CEE-001, GES) | Consolidar um registro de riscos por documento/Skill — ver template §8.2 |
| Qualidade | GES (5 validações), agora 6 com CEE-001 | Já maduro — este PPQ-001 não duplica, apenas referencia |
| Stakeholders | Andraus (decisor), Estrategista, Analista, Controlador | Nunca formalizado como RACI — ver §4.3 |
| Comunicação | Blackboard (entre agentes), chats separados (entre papéis humanos/IA) | Já resolvido pela arquitetura — nada a fazer aqui |
| Integração | Master Orchestrator | Já resolvido — nada a fazer aqui |

### 4.3 RACI mínimo (leve, 4 papéis)

| Atividade | Andraus | Estrategista | Analista | Controlador |
|---|---|---|---|---|
| Propor novo documento/Skill/mudança | Consultado | **Responsável** | Informado | Informado |
| Auditar conformidade arquitetural | Informado | Informado | **Responsável** | Informado |
| Declarar consenso | **Aprovador** | Informado | Informado | Informado |
| Registrar e versionar | Informado | Informado | Informado | **Responsável** |

Isso não é burocracia nova — é a governança de 3 papéis que você já usa, apenas nomeada em RACI para que cada prompt ao Estrategista já saiba seu papel (Responsável por propor, nunca por aprovar).

---

## 5. Gestão de Processos (BPM Leve)

### 5.1 Padrão mínimo de representação de processo

Nada de BPMN completo (teste de Custo, §3.3). Todo processo novo documentado no ORYX — seja um fluxo de Skill, um fluxo de missão, ou um fluxo de governança — deve responder seis campos, sempre nesta ordem:

```
Gatilho     → o que inicia o processo (evento, decisão, agendamento)
Entradas    → o que o processo consome (dados, documentos, decisões anteriores)
Etapas      → sequência mínima de passos (setas simples, como já é praticado)
Saídas      → o que o processo produz
Responsável → qual Agente/Skill/papel executa
Exceções    → o que acontece quando o processo falha ou é abortado
```

Isso já é, na prática, o estilo que os documentos ENGENHARIA_GERAL usam ("Fechou D1 ↓ Nova quebra estrutural ↓ Structural desperta") — o PPQ-001 apenas obriga que os seis campos estejam sempre presentes, para que nenhum processo novo fique incompleto por omissão.

### 5.2 Quando NÃO formalizar um processo

Para manter a leveza pedida: processos que ocorrem uma única vez, ou que são puramente exploratórios (ex: uma sessão de brainstorm de ideias, como a AUDITORIA_DE_IDEIAS), não precisam do template de 6 campos. O template se aplica a processos **recorrentes** — algo que vai acontecer mais de uma vez na vida do sistema.

---

## 6. Gestão da Qualidade — PDCA em Três Camadas

Cada camada usa o mesmo ciclo PDCA, mas mapeado sobre estruturas que já existem — não se inventa um PDCA genérico, ele é encaixado no que o ORYX já faz.

### 6.1 Camada 1 — Skill/Agente (já mais madura, via GES)

| PDCA | Corresponde a (GES + CEE-001) |
|---|---|
| **P**lan | Formulação da ideia + 5W2H obrigatório (§7.1) + entrada em Sandbox |
| **D**o | Backtest + Forward Test |
| **C**heck | Comparação com baseline + as 6 Validações (GES + Validação Econômica do CEE-001) |
| **A**ct | Homologação (padroniza e propaga) ou Rejeição/Rollback (descarta e documenta o motivo) |

### 6.2 Camada 2 — Documento de Arquitetura (parcialmente formal, formalizado agora)

| PDCA | Corresponde a (fluxo de 3 papéis) |
|---|---|
| **P**lan | Estrategista redige documento candidato, com 5W2H de justificativa (§7.2) |
| **D**o | Documento circula — Analista realiza auditoria de conformidade |
| **C**heck | Comparação contra documentos congelados + Critérios de Aceitação explícitos (padrão já usado no CEE-001 §12) |
| **A**ct | Andraus declara consenso → Controlador congela versão, **ou** documento retorna ao Estrategista com apontamentos (novo ciclo Plan) |

### 6.3 Camada 3 — Missão Operacional (Mission Engine já existe, mapeamento novo)

| PDCA | Corresponde a (Mission Engine, ENGENHARIA GERAL Doc. 09) |
|---|---|
| **P**lan | Missão Criada + Planejada (com submissões Elliott/Fibonacci/Fractal/SMC/ICT) |
| **D**o | Missão Delegada + Executada |
| **C**heck | Missão Validada (Conviction Engine avalia coerência) |
| **A**ct | Missão Consolidada + Encerrada — resultado alimenta o Learning Agent (aprendizado formal do ciclo) |

**Observação importante:** a Camada 3 já é, estruturalmente, um PDCA — só faltava o nome. Não requer mudança de arquitetura, apenas o reconhecimento de que o "Aprendizado" do Learning Agent é literalmente o **Act** do ciclo anterior alimentando o **Plan** do próximo.

---

## 7. 5W2H — Template Obrigatório

5W2H é o formulário de entrada do **Plan** em qualquer uma das três camadas. Nenhuma proposta — de Skill, de documento, ou de mudança de roteamento (CEE-001 §9) — deve ser aceita para análise sem responder as sete perguntas.

### 7.1 Template — Nova Skill/Agente ou Mudança Técnica

```
What (O quê)      → Qual capacidade está sendo criada/alterada?
Why (Por quê)     → Qual lacuna ou problema real ela resolve? (nunca "porque seria legal ter")
Where (Onde)      → Em qual Agente/camada da arquitetura ela vive?
When (Quando)     → Em que fase do pipeline entra? Tem dependência de outra Skill?
Who (Quem)        → Qual Agente é o responsável funcional por ela?
How (Como)        → Qual algoritmo/lógica/fonte teórica ela usa?
How much (Quanto) → Custo estimado (CEE-001 §5 roteamento) e critério de sucesso mensurável
```

### 7.2 Template — Novo Documento de Arquitetura

```
What      → O que este documento especifica que nenhum outro documento já cobre?
Why       → Que decisão, ambiguidade ou lacuna ele resolve?
Where     → Em qual camada (Governança/Modelos/Kernel/Agentes/Skills) ele se encaixa?
When      → É pré-requisito de quê? O que está bloqueado até ele existir?
Who       → Quem audita (Analista) e quem aprova consenso (Andraus)?
How       → Qual estrutura ele segue (padrão dos documentos já congelados)?
How much  → Impacto em documentos existentes (padrão CEE-001 §13 "Impacto em documentos existentes")
```

---

## 8. Prompts-Guia para o Estrategista

Blocos de prompt prontos, para colar na conversa com o Estrategista (GPT), garantindo que PM + BPM + Qualidade + a Diretriz Mestra (§3) já venham embutidos na resposta, em vez de precisar ser cobrados depois pelo Analista.

### 8.1 Prompt-padrão: solicitar nova Skill/Agente

```
Você é o Estrategista do ORYX AGENT. Antes de propor a especificação técnica
completa desta Skill/Agente, preencha o 5W2H (What/Why/Where/When/Who/How/
How much) conforme o padrão PPQ-001 §7.1.

Em seguida, declare explicitamente:
1. Em qual Tipo Cognitivo (I–V) esta Skill se enquadra e qual classe de modelo
   você recomenda (CEE-001 §5) — com justificativa, não apenas a escolha.
2. Quais das 6 validações do pipeline GES+CEE-001 você antecipa que serão
   mais críticas para esta Skill, e por quê.
3. Um registro de risco mínimo: o que pode dar errado, e qual salvaguarda
   constitucional (GES Nível 1, CEE-001 §10) protege contra isso.
4. Que esta proposta passou pelo Teste de Adoção (PPQ-001 §3.3) se estiver
   introduzindo alguma prática de gestão nova, não apenas técnica de mercado.

Só depois disso, escreva a especificação técnica completa da Skill.
```

### 8.2 Prompt-padrão: solicitar novo documento de arquitetura

```
Você é o Estrategista do ORYX AGENT. Antes de redigir o documento completo,
preencha o 5W2H de justificativa (PPQ-001 §7.2).

Declare também:
1. Escopo: o que este documento cobre e o que explicitamente NÃO cobre
   (PPQ-001 §4.2 — área de Escopo).
2. Impacto: quais documentos já congelados ou candidatos precisam ser
   revisados por causa deste novo documento.
3. Critérios de Aceitação: liste, ao final do documento, as condições
   objetivas e verificáveis sob as quais este documento passa de
   "especificação" para "implementado" (padrão já usado no CEE-001 §12).

Estruture o documento seguindo o padrão dos documentos já congelados
(Missão → Filosofia → Princípios → Corpo técnico → Critérios de Aceitação
→ Status), com linguagem direta e frases curtas, como nos documentos
ENGENHARIA_GERAL já aprovados.
```

### 8.3 Prompt-padrão: revisão periódica (Check + Act do PDCA)

```
Você é o Estrategista do ORYX AGENT. Esta é uma revisão periódica do
componente [Skill/Agente/Documento X], camada [1/2/3 do PPQ-001 §6].

Compare o desempenho/uso real observado contra os critérios de sucesso
definidos no 5W2H original (How much).

Responda:
1. O componente ainda cumpre sua missão original sem desvio? (Check)
2. Alguma das métricas do CEE-001 §7 (se aplicável) está fora do limiar
   de Fase Piloto?
3. Recomendação: manter, ajustar (novo ciclo Plan) ou descontinuar —
   com justificativa, nunca sem ela.

Não implemente a recomendação — apenas proponha. A decisão segue o
fluxo de Autoridade de Homologação (CEE-001 §9).
```

### 8.4 Prompt-padrão: nova Missão operacional (referência, não documentação)

```
Você é o Estrategista/Master Orchestrator do ORYX AGENT. Ao formular
uma nova Missão, estruture-a com 5W2H reduzido:

What  → hipótese a validar/refutar
Why   → prioridade (PPQ-001 mapeamento Mission Engine, evento gatilho)
Where → ativo e grau fractal (S1/D1/H4/H1/M5)
When  → janela temporal esperada e dependências de outras missões
Who   → quais Agentes/Skills são convocados (submissões)
How   → ordem metodológica: Elliott → Fibonacci → Fractal → SMC → ICT
How much → risco (2% base, R:R mínimo 1:3) e custo estimado de inferência
```

---

## 9. Papel de Cada Ator Nesta Camada

- **Estrategista** — usa os prompts do §8 como estrutura de entrada obrigatória para qualquer proposta. Responsável pelo Plan e pelo Do.
- **Analista (este chat)** — audita se o 5W2H foi de fato respondido (não apenas presente pro forma), se o escopo declarado é coerente com a arquitetura congelada, se os Critérios de Aceitação são objetivamente verificáveis, e se a proposta passa no Teste de Adoção (§3.3) quando aplicável. Responsável pelo Check.
- **Andraus** — declara consenso (Act de decisão) e pode, a qualquer momento, considerar uma resposta do Estrategista incompleta se o 5W2H estiver superficial — isso não é falha de conteúdo técnico, é falha de processo, e deve ser devolvida antes mesmo da auditoria do Analista.
- **Controlador** — não valida conteúdo. Verifica apenas se a estrutura (5W2H presente, Critérios de Aceitação presentes, RACI respeitado) está completa antes de registrar.

---

## 10. Calibração de Peso de Governança — Burocracia vs. Agilidade

Esta seção é a aplicação prática da Diretriz Mestra (§3) — ela responde diretamente à necessidade de equilibrar controle com velocidade, dentro de um prazo razoável para o tamanho real do projeto.

### 10.1 Princípio

> **O peso do processo deve ser proporcional ao risco e à irreversibilidade da decisão — nunca ao tamanho do documento gerado ou ao entusiasmo do momento.**

Em vez de criar uma nova escala de risco, o PPQ-001 reaproveita os **4 Níveis da Constituição do Conhecimento já congelados no GES (Documento 12, MLS Doc. 11)** — eles já são, na prática, uma escala de risco. Isso evita ter duas hierarquias de importância competindo entre si.

### 10.2 O dial de burocracia (reaproveitando os 4 Níveis do GES)

| Nível GES | O que é | Peso de processo | Time-box alvo |
|---|---|---|---|
| **Nível 1 — Constituição** | Elliott, Fibonacci, SMC, ICT, Kernel Cognitivo, Conviction Engine | Máximo: 5W2H completo (§7.2) + Stage-Gate completo (§4.1) + consenso explícito de Andraus + registro no CONTROLADOR | Sem prazo-alvo — é o único nível onde correção deve sempre vencer velocidade |
| **Nível 2 — Framework Oficial** | Skills, Agentes, Engines, documentos de arquitetura vertical (SAS, IIES etc.) | Padrão: 5W2H (§7.1) + pipeline completo + auditoria do Analista obrigatória | **1 a 3 sessões de trabalho** da proposta ao consenso — ver regra de corte em §10.3 |
| **Nível 3 — Conhecimento Certificado** | PDFs, indicadores TradingView, Pine Scripts, estudos externos | Fast-track: pipeline de certificação já existente (Leitura → Engenharia Reversa → Validação → Sandbox → Certificação), sem 5W2H completo, sem novo documento de arquitetura | **1 sessão** — se exceder isso, provavelmente é Nível 2 disfarçado |
| **Nível 4 — Aprendizado Operacional** | Calibrações, memória de ativos, estatísticas de campanha | Nenhuma burocracia — adapta automaticamente dentro dos limites já definidos; apenas logado; revisão só no Check periódico da Camada 3 (§6.3) | Nenhum — é o próprio ciclo operacional contínuo |

### 10.3 Regra do Corte de Escopo (Right-Sizing)

Se uma proposta de Nível 2 ultrapassa o time-box de 3 sessões sem chegar a consenso, isso não é sinal de que o assunto é difícil — é sinal de que **o escopo está grande demais para uma única proposta**. A ação correta não é acelerar a auditoria, é dividir a proposta em sub-propostas menores, cada uma com seu próprio 5W2H. Exatamente o que aconteceu, na prática, quando o CEE-001 foi de "documento com 4 pendências abertas" para "documento fechado" — cada pendência resolvida como uma unidade de trabalho separada, não uma renegociação do documento inteiro.

### 10.4 Fast-track explícito para mudanças triviais

Nem toda alteração precisa de ciclo. Correções editoriais, ajuste de exemplo, correção de erro de digitação, ou pequenos ajustes de parâmetro **dentro de limites já homologados** (ex: ajustar o time-box de §10.2 em si) não entram no pipeline — apenas exigem sinal do Analista de que a mudança é de fato trivial, registrado inline, sem novo ciclo de documento.

Critério objetivo para "trivial": a mudança não altera nenhum Critério de Aceitação existente, não move um componente entre classes de modelo (CEE-001 §5), e não afeta nenhuma Salvaguarda Constitucional. Se qualquer uma dessas três condições for violada, a mudança não é trivial — vai para Nível 2.

### 10.5 Ritmo do backlog total (dimensionamento do projeto)

O SOT/ORYX tem um backlog estimado de **310 a 330 Engineering Cards** (KERNEL V2, SES). Isso é grande o suficiente para que tentar aplicar o Stage-Gate completo (Nível 1/2) a cada card, sequencialmente, seria incompatível com qualquer prazo razoável — mesmo sem deadline externo.

Duas alavancas de agilidade, ambas já sugeridas na sua própria documentação e agora formalizadas como política:

1. **Priorização P0 primeiro, com peso total; o resto, por herança de padrão.** Os componentes P0 (fundacionais — Kernel, Cognitive Core) justificam o peso máximo do Nível 1/2. Uma vez que um **SOT Design Pattern** (conceito já levantado no KERNEL V2) for validado uma vez, Engineering Cards subsequentes que apenas aplicam o mesmo padrão a um domínio diferente (ex: mais uma Skill de evidência, seguindo o padrão já certificado da Trend Skill) podem tramitar como Nível 3 fast-track — o padrão já foi litigado, não precisa ser rejulgado a cada aplicação.
2. **Lotes (batches), não unidades.** Cards do mesmo domínio e do mesmo Tipo Cognitivo (CEE-001 §5) podem ser propostos, auditados e homologados em lote, com um único 5W2H cobrindo o lote e critérios de aceitação individuais por card dentro dele — desde que nenhum deles seja Nível 1.

### 10.6 Sinal de Burocracia Excessiva

Heurística prática para o próprio Andraus usar, sem precisar de métrica formal: **se o tempo gasto em processo (5W2H + auditoria + ciclos de consenso) para um item específico supera o tempo gasto no trabalho técnico daquele mesmo item, isso é um sinal de alerta.** Não significa abandonar o processo — significa que aquele item provavelmente foi classificado no nível de governança errado, e deve ser reclassificado (geralmente para baixo, usando §10.2) antes de continuar. Este é, na prática, o Teste de Adoção (§3.3) aplicado retroativamente a um processo já em curso.

---

## 11. Critérios de Aceitação

O PPQ-001 será considerado implementado quando:

1. Todo novo prompt de solicitação de documento/Skill ao Estrategista usar um dos templates do §8.
2. O Analista incluir, em toda auditoria, uma verificação explícita de presença e qualidade do 5W2H, e do Teste de Adoção (§3.3) quando aplicável — não apenas conformidade técnica.
3. Os três mapeamentos de PDCA (§6.1–6.3) estiverem referenciados nos documentos correspondentes (GES para Camada 1, processo de consenso para Camada 2, Mission Engine para Camada 3) na próxima revisão desses documentos.
4. O RACI do §4.3 não tiver sido violado — nenhum papel aprovando fora de sua função.
5. Toda proposta nova declarar explicitamente em qual dos 4 Níveis do §10.2 ela se enquadra, antes de entrar em qualquer pipeline.
6. Nenhuma proposta de Nível 2 tiver ultrapassado o time-box de 3 sessões sem acionar a Regra do Corte de Escopo (§10.3).
7. Nenhuma nova prática de gestão (PM, BPM ou Qualidade) tiver sido incorporada ao projeto sem passar pelo Teste de Adoção (§3.3).

---

## 12. Status e Registro para o CONTROLADOR

| Campo | Valor |
|---|---|
| ID do Documento | PPQ-001 |
| Nome | Especificação de Gestão de Projetos, Processos e Qualidade |
| Tipo | Documento de Governança (Layer 1) — transversal, meta-processual |
| Dependências | GES (Doc. 12), CEE-001, Mission Engine (Doc. 09), MLS (Doc. 11 — 4 Níveis da Constituição do Conhecimento) |
| Status | **CONGELADO — Baseline 1.2** — consenso explícito de Andraus |
| Prioridade | P1 — orienta a partir de agora todo prompt de solicitação de documento/Skill ao Estrategista, incluindo a próxima auditoria (SAS-001 Cap.2) |

---

## 13. Histórico de Versões

| Versão | Status | Mudança |
|---|---|---|
| 1.0 | Candidata | Primeira consolidação — PM/BPM/PDCA/5W2H mapeados sobre estruturas existentes, templates de prompt para o Estrategista |
| 1.1 | Candidata | Adicionado §9 (então) — Calibração de Peso de Governança: dial de burocracia reaproveitando os 4 Níveis do GES, time-boxes por nível, Regra do Corte de Escopo, fast-track para mudanças triviais, dimensionamento do backlog (~320 Engineering Cards) e heurística de "Sinal de Burocracia Excessiva" |
| 1.1 | Congelada — Baseline | Premissas de perfil (§0) confirmadas por Andraus. Consenso explícito declarado |
| 1.2 | **Congelada — Baseline** | Adicionada §3 — Diretriz Mestra: Rigor Proporcional e Adaptativo à Execução por IA. Formaliza o princípio de equilíbrio entre conformidade com melhores práticas/ciência de arquitetura e flexibilidade/custo/tempo, com as 5 particularidades de execução por IA (§3.2) e o Teste de Adoção de 3 perguntas (§3.3). Demais seções renumeradas (antigas §3–§12 tornam-se §4–§13). Adicionado por diretriz direta de Andraus |

---

*Fim do Documento PPQ-001 — Baseline 1.2 (Congelado)*
