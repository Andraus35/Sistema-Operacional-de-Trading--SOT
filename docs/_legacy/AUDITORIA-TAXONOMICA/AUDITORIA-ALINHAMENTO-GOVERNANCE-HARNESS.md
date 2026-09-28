# Auditoria de alinhamento da governança ao Harness Cognitivo

**Data:** 2026-09-25  
**Escopo:** diretório [`governance/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance), confrontado com [`ROADMAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ROADMAP.md), [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md), o relatório do diretório [`canon/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/AUDITORIA-ALINHAMENTO-CANON-HARNESS.md) e os anexos do `INQUÉRITO SOT`.  
**Natureza:** relatório local de achados e sugestões. Não é norma, não é emenda, não fecha decisões abertas e não altera nenhum arquivo de governança existente.

## 1. Conclusão executiva

O diretório `governance/` já contém uma estrutura madura de autoridade, homologação, atas, emendas, regras, conflito e higiene documental. O problema principal é de **sincronização e classificação**, não de ausência de governança.

Há quatro camadas misturadas:

1. autoridade normativa vigente;
2. atos de homologação e histórico de decisões;
3. propostas já homologadas, mas preservadas com nome `_PROPOSTA`;
4. resíduos da arquitetura anterior de software/runtime.

O risco operacional é alto porque um agente pode encontrar, no mesmo diretório:

- uma decisão homologada e a proposta que a originou;
- uma regra atual e sua fonte histórica obsoleta;
- um status contraditório no Catálogo;
- um termo de runtime antigo apresentado como componente constitucional;
- um documento baseline que ainda contém invariantes pré-Q-008, pré-Q-009 ou pré-E19a.

**Recomendação geral:** preservar integralmente o histórico conforme INV-07, mas adicionar uma camada de metadados de autoridade, sucessão e vigência. A governança deve distinguir claramente “registro do ato”, “texto vigente” e “fonte histórica”.

## 2. Autoridade usada para a leitura

Foi aplicada a seguinte precedência:

1. decisões humanas homologadas e DHRs;
2. Constituição, Rules, Conflict Map e Catálogo Oficial;
3. [`ROADMAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ROADMAP.md) e [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md);
4. modelos canônicos e Specs homologadas;
5. propostas, referências e documentos históricos.

Uma proposta com status homologado não foi tratada como nova autoridade independente: ela é o veículo histórico da decisão, enquanto a vigência deve ser lida no DHR, no Catálogo e nos loci incorporados.

## 3. Achados críticos de sincronização e autoridade

### GOV-001 — O Catálogo Oficial apresenta dois próximos passos incompatíveis

**Severidade:** CRITICAL  
**Evidência:**

- Na tabela de duas trilhas do [`CATALOGO-OFICIAL.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/CATALOGO-OFICIAL.md), a Trilha B informa “Próximo artefato: SPEC-002”.
- Mais adiante, o mesmo Catálogo informa que, após DHR-EUA-E17, o próximo da Trilha B é `SPEC-019`, seguido de `SPEC-020` núcleo A e `SPEC-021`.
- [`DHR-EUA-E17`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/DHR-EUA-E17_Ata_Homologacao_Reposicionamento_Specs_Governanca_Harness.md) e [`EUA-E17`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/EUA-E17_Reposicionamento_Specs_Governanca_Harness_PROPOSTA.md) registram que a FASE GOV precede SPEC-002.

**Risco:** o Catálogo, que é o Single Source of Truth, pode autorizar duas Specs diferentes.

**Sugestão:** manter apenas um campo vivo de “próximo artefato por trilha”, gerado ou atualizado junto com cada DHR. Referências históricas devem ser marcadas como `snapshot anterior`, nunca permanecer em tabela operacional sem data de corte.

### GOV-002 — CEM-001 tem status contraditório entre Catálogo e cânone

**Severidade:** CRITICAL  
**Evidência:**

- [`CATALOGO-OFICIAL.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/CATALOGO-OFICIAL.md) classifica CEM-001 como `BASELINED`.
- [`CEM-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/CEM-001-canonical-evidence-model.md) ainda declara `Candidato a baseline oficial`.
- O próprio Catálogo afirma ser a fonte oficial de estado e baseline.

**Risco:** um agente pode tratar o CEM como não vinculante, ou entender que existem duas versões de autoridade.

**Sugestão:** escolher um único estado vigente no cabeçalho do arquivo e incluir referência explícita ao DHR/Q-001 que o suporta. Caso o texto ainda não esteja integralmente homologado, o Catálogo deve refletir essa limitação em vez de usar `BASELINED`.

### GOV-003 — Propostas homologadas continuam com identidade visual de proposta

**Severidade:** HIGH  
**Evidência:** vários arquivos `EUA-E04...E19a_PROPOSTA.md` registram `Status epistemológico: HOMOLOGADA`, mas conservam `_PROPOSTA` no nome. A própria [`EUA-E17`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/EUA-E17_Reposicionamento_Specs_Governanca_Harness_PROPOSTA.md) explica que o filename é preservado por convenção.

**Risco:** ferramentas, agentes ou leitores podem classificar pelo nome do arquivo e ignorar o status homologado; o inverso também é possível.

**Sugestão:** não renomear retroativamente sem plano de compatibilidade. Adicionar um front matter uniforme com `kind: amendment`, `lifecycle: homologated`, `supersedes`, `homologated_by`, `effective_from` e `source_dhr`. O Catálogo deve ser a rota preferencial para saber o status.

### GOV-004 — A governança não diferencia suficientemente ato, norma vigente e veículo histórico

**Severidade:** HIGH  
**Evidência:** o diretório reúne `DHR-*`, `EUA-*`, normas vivas, atas, inventário, backlog e referências externas no mesmo nível físico. O Catálogo registra que a separação de pastas (`governance/emendas/`, `governance/atas/`) foi diferida.

**Risco:** o agente lê uma ata ou proposta como se fosse o texto normativo atual, ou interpreta uma decisão histórica como regra operacional completa.

**Sugestão:** introduzir classificação obrigatória por documento:

| Classe | Função |
|---|---|
| `NORMATIVE_BASELINE` | texto vigente |
| `HOMOLOGATION_RECORD` | prova do ato de homologação |
| `AMENDMENT_VEHICLE` | proposta/emenda que transporta alteração |
| `AUDIT_REGISTER` | inventário, conflito ou higiene |
| `REFERENCE_NON_NORMATIVE` | fonte consultiva |
| `LEGACY` | histórico superseded |

Essa classificação pode ser feita em cabeçalhos sem mover os arquivos congelados.

## 4. Achados de taxonomia e migração para harness

### GOV-005 — A Constituição ainda apresenta runtime de software como arquitetura constitucional

**Severidade:** CRITICAL  
**Evidência:** [`CONSTITUTION.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/CONSTITUTION.md) inclui no fluxo:

`TradingView → Data Acquisition → Market Digital Twin → Mission Engine → Master Orchestrator → especialistas`.

Também afirma que `Master Orchestrator` coordena e que `Mission Engine` inicia toda análise.

**Risco:** o texto constitucional transforma componentes legados/propostos em invariantes, embora o baseline atual seja spec-first e o runtime cognitivo ainda esteja sendo especificado por fases.

**Sugestão:** separar no documento:

- invariantes constitucionais do harness;
- pipeline conceitual de objetos cognitivos;
- arquitetura runtime futura, condicionada às Specs;
- exemplos históricos de produto.

Até homologação específica, `Master Orchestrator` e `Mission Engine` devem ser marcados como `REFERENCE/UNRESOLVED`, não como componentes constitucionais.

### GOV-006 — RULES.md usa “Orchestrator” sem identidade taxonômica estável

**Severidade:** HIGH  
**Evidência:** [`RULES.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/RULES.md) contém regra segundo a qual “o Orchestrator apenas coordena via Blackboard”, mas a Constituição usa `Master Orchestrator`, os anexos levantam `Cognitive Orchestrator` e `Decision Orchestrator`, e não existe uma declaração única que resolva a relação entre eles.

**Risco:** a regra pode ser aplicada a componentes diferentes, com escopos e poderes distintos.

**Sugestão:** parametrizar a regra por ID de componente autorizado ou usar um termo genérico explicitamente taxonômico, como `COORDINATION_COMPONENT`. O nome concreto só deve entrar após Spec/decisão que defina identidade, entradas, saídas e autoridade.

### GOV-007 — Blackboard, Event Bus e Orchestrator aparecem próximos, mas com fronteiras incompletas

**Severidade:** HIGH  
**Evidência:** Constituição, Rules, CEE-001 e SES-001 usam Blackboard, Cognitive Event Bus, Scheduler e Orchestrator; a governança define algumas regras de Blackboard, mas não apresenta uma tabela única de responsabilidades.

**Risco:** um agente pode publicar estado no Event Bus, usar Blackboard como transporte, ou atribuir coordenação ao repositório de estado.

**Sugestão:** incluir uma matriz normativa:

| Componente | Tipo | Faz | Não faz |
|---|---|---|---|
| Blackboard | `STATE_REPOSITORY` | persiste/publica estado cognitivo append-only | não coordena nem analisa |
| Event Bus | `EVENT_BUS` | transporta eventos/gatilhos | não é fonte de verdade de estado |
| Scheduler | `SCHEDULER` | decide quando despertar trabalho autorizado | não cria hipótese nem decide |
| Orchestrator | `ORCHESTRATOR` | coordena componentes autorizados | não interpreta mercado, salvo decisão explícita |

### GOV-008 — Risk Agent está simultaneamente futuro, consumidor e etapa do pipeline

**Severidade:** HIGH  
**Evidência:**

- A Constituição e [`DHR-EUA-E19a`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/DHR-EUA-E19a_Ata_Homologacao_Restauracao_Signal_Package.md) tratam a camada de risco como futura.
- A mesma Constituição já coloca TMP entre Synthesis e Risk Agent.
- O Catálogo mantém decisões abertas `RISK-ARR-LOC-001`, `RISK-CONV-001` e outras.

**Risco:** o pipeline parece operacionalmente completo, embora a família RISK-SPEC ainda não esteja autorizada como runtime atual.

**Sugestão:** rotular a etapa como `FUTURE HANDOFF` no diagrama e declarar que o único contrato vigente nesta fase é semântico: TMP é interno; Signal Package é fronteira. Não atribuir ao Risk Agent comportamento não especificado.

## 5. Achados de inconsistência normativa

### GOV-009 — GPR-001 preserva invariantes anteriores às decisões atuais

**Severidade:** CRITICAL  
**Evidência:** [`GPR-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/GPR-001_Guia_Principios_Relacoes_SOT.md) ainda contém:

- `Conviction 4D`;
- convicção estrutural ≥ 60% e total ≥ 75%;
- `SOT produz TMP` como princípio;
- hierarquia de 4Es sem `Conformidade` na seção diagnóstica.

Isso diverge de:

- Constituição P02/P14;
- Q-002, Q-008 e Q-009;
- EUA-E19a;
- [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md);
- [`ROADMAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ROADMAP.md).

**Risco:** GPR-001 é baseline de governança e é usado pelos gates PAP/CIC; portanto, os resíduos podem contaminar Specs novas mesmo quando Constituição e Rules estão atualizadas.

**Sugestão:** emitir uma emenda de compatibilidade ao GPR-001, preservando o texto histórico em registro de versão e marcando os pontos como `SUPERSEDED`. Não tratar o CIC como suficiente para corrigir semântica: o inventário registra conformidade, mas não substitui a atualização do documento fonte.

### GOV-010 — Regras de transição e estados de hipótese/agente não estão suficientemente separados

**Severidade:** HIGH  
**Evidência:** RULES usa estados como `INACTIVE`; Constituição usa estados canônicos CHM-001 para hipóteses; o Catálogo e atas registram estados de governança do harness. Esses namespaces não estão consolidados numa tabela de escopo.

**Risco:** um estado operacional de agente pode ser interpretado como estado epistêmico de hipótese ou como maturidade de documento.

**Sugestão:** prefixar ou qualificar estados por máquina:

- `HYPOTHESIS.ACTIVE`;
- `AGENT.OBSERVING`;
- `DOCUMENT.HOMOLOGATED`;
- `GATE.INDETERMINATE`;
- `BACKLOG.WAITING`.

A transição entre máquinas deve ser especificada, não inferida por igualdade textual.

### GOV-011 — CONFLICT-MAP é robusto como histórico, mas acumula instruções negativas e namespaces concorrentes

**Severidade:** MEDIUM  
**Evidência:** [`CONFLICT-MAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/CONFLICT-MAP.md) acumula emendas E04–E14, rótulos rejeitados, níveis conflitantes, nós MAN e regras de não adoção.

**Risco:** a preservação histórica pode tornar difícil localizar a regra atualmente vigente, principalmente quando um agente lê um comentário de colisão sem consultar o locus sucessor.

**Sugestão:** manter o histórico, mas acrescentar em cada bloco:

`STATUS ATUAL → vigente/superseded/diferido`  
`LOCI VIGENTE → arquivo/seção`  
`NÃO É FONTE DE REGRA → se o bloco for somente diagnóstico`.

## 6. Achados de workflow do harness

### GOV-012 — PAP/CIC/RMR criam uma segunda trilha correta, mas sua interface com a Trilha B precisa de um contrato operacional único

**Severidade:** HIGH  
**Evidência:** o Catálogo define Trilha A principiólogica e Trilha B de Specs, com PAP Bloco 6, VPD, CIC e RMR como interface. Porém, o ROADMAP e o ATOMIC-SPEC continuam sendo os pontos de entrada obrigatórios para o Especificador/Revisor.

**Risco:** um agente pode iniciar uma Spec pelo RMR/PAP sem consultar o Roadmap/Atomic-Spec, ou tratar o inventário de princípios como autorização da Spec.

**Sugestão:** declarar uma sequência obrigatória única:

`ROADMAP/ATOMIC-SPEC → PAP/CIC/RMR applicability → pesquisa → Spec → Revisor → Andraus → Catálogo/DHR`.

PAP/CIC/RMR devem ser gates de conformidade e rastreabilidade; não substituem a autorização sequencial do Roadmap.

### GOV-013 — “vigência imediata” e “incorporação editorial diferida” exigem um mecanismo de leitura efetiva

**Severidade:** HIGH  
**Evidência:** DHRs como EUA-E04–E19a registram decisões com vigência imediata, enquanto a incorporação física ao `atomic-spec`, GLOSSARIO ou outros loci fica diferida.

**Risco:** durante o intervalo, a autoridade normativa está no DHR, mas o agente que lê apenas o locus de execução encontra texto antigo.

**Sugestão:** toda emenda com incorporação diferida deve conter um bloco máquina-legível:

```text
effective_status: ACTIVE
materialized_status: PENDING
read_authority: DHR-EUA-EXX
target_loci: ...
```

Enquanto `materialized_status` for `PENDING`, o Catálogo deve indicar o DHR como fonte de leitura obrigatória.

### GOV-014 — A governança contém código de versionamento e estados, mas não uma matriz consolidada de sucessão

**Severidade:** MEDIUM  
**Evidência:** INV-07 exige preservação e sucessão; CATALOGO registra superseded; DHRs apontam para loci; porém não há tabela única `artefato anterior → sucessor → escopo alterado → compatibilidade`.

**Risco:** o agente preserva todos os documentos, mas não sabe qual trecho substitui qual requisito.

**Sugestão:** criar um registro de sucessão no Catálogo ou no GMC-001 com quatro campos mínimos:

`predecessor`, `successor`, `delta`, `compatibility`.

## 7. Matriz de termos governados

| Termo | Classificação recomendada | Estado atual |
|---|---|---|
| Constitution | `NORMATIVE_BASELINE` | vigente, mas com resíduos de runtime |
| Rules | `NORMATIVE_BASELINE` | vigente; precisa qualificar `Orchestrator` |
| Conflict Map | `AUDIT_REGISTER` + regras indexadas | vigente com histórico acumulado |
| Catalog | `GOVERNANCE_COMPONENT` / SSoT | fonte de estado; possui contradição de próximo passo |
| DHR | `HOMOLOGATION_RECORD` | prova do ato, não substituto automático do texto consolidado |
| EUA | `AMENDMENT_VEHICLE` | algumas homologadas apesar do sufixo `_PROPOSTA` |
| GPR-001 | `NORMATIVE_BASELINE` | baseline com resíduos semânticos antigos |
| PAP-001 | `GOVERNANCE_COMPONENT` | gate de adesão; não autoriza sozinho a ordem de Specs |
| CIC-001 | `AUDIT_REGISTER` | inventário de conformidade; não substitui fonte normativa |
| RMR-001 | `GOVERNANCE_COMPONENT` | backlog/gatilho; não substitui ROADMAP |
| RCH-001 | `AUDIT_REGISTER` | histórico de ciclos de higiene |
| Master Orchestrator | `LEGACY/UNRESOLVED` | não assumir como componente canônico |
| Mission Engine | `LEGACY/UNRESOLVED` | separar missão de investigação e runtime futuro |
| Decision Orchestrator | `LEGACY/UNRESOLVED` | posição atual não resolvida |
| Risk Agent | `FUTURE_COMPONENT` | não operacionalizar antes de RISK-SPEC |
| TMP | `ARTIFACT_INTERNAL` | handoff interno Synthesis → Risk Agent |
| Signal Package | `ARTIFACT_FRONTIER` | saída de fronteira para Bot Trade Finance |

## 8. Decisões que não devem ser inferidas

Os seguintes pontos precisam de decisão ou emenda explícita:

1. O `Master Orchestrator` da Constituição é um componente vigente ou apenas legado?
2. `Mission Engine` será especificado como missão cognitiva, scheduler de runtime ou ambos?
3. `Orchestrator` em RULES é alias de Master Orchestrator ou categoria genérica?
4. GPR-001 deve ser corrigido prospectivamente ou superseded por um novo guia?
5. O status `BASELINED` do CEM-001 deve prevalecer sobre “Candidato a baseline oficial” no arquivo canônico?
6. Propostas homologadas continuarão com sufixo `_PROPOSTA` ou receberão metadata obrigatória?
7. A tabela de “próximo artefato” será mantida manualmente ou derivada do Roadmap/DHR?
8. A incorporação diferida de uma emenda deve bloquear a leitura dos loci antigos ou apenas redirecioná-la ao DHR?

Nenhuma dessas decisões deve ser fechada pelo relatório.

## 9. Ordem sugerida de correção futura

1. Corrigir a fonte operacional do próximo passo no Catálogo.
2. Resolver o status CEM-001 no Catálogo e no cabeçalho do cânone.
3. Emitir emenda de compatibilidade para GPR-001.
4. Classificar metadados de todos os documentos de governança.
5. Separar, na Constituição, invariantes do harness de pipeline runtime futuro.
6. Publicar a matriz Agent/Engine/Scheduler/Event Bus/Blackboard/Artifact.
7. Criar matriz de sucessão e de materialização de emendas.
8. Só depois revisar a nomenclatura de orquestração e missão.

## 10. Regra de não destruição

Este relatório recomenda alinhamento por sucessão, classificação e redirecionamento, não apagamento:

- DHRs continuam como prova histórica;
- propostas continuam preservadas;
- regras superseded continuam auditáveis;
- termos antigos recebem classificação explícita;
- texto vigente deve apontar para sua autoridade;
- nenhum documento de `governance/` deve ser alterado apenas com base neste relatório.

**Resultado:** a governança pode sustentar o Harness Cognitivo com segurança, desde que a próxima etapa seja de reconciliação de status, taxonomia e sucessão — e não de criação de novos invariantes por leitura implícita dos documentos legados.
