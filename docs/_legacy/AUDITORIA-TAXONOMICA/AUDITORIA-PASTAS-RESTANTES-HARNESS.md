# Auditoria taxonômica das pastas restantes do SOT-Harness

**Data:** 2026-09-25  
**Escopo:** todas as pastas do repositório ainda não cobertas pelas auditorias específicas de [`canon/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon) e [`governance/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance).  
**Relatório:** somente achados e sugestões. Não é baseline, Spec, emenda ou autorização de implementação.  
**Restrição observada:** nenhum arquivo existente foi alterado; foi criada somente esta pasta e este Markdown.

## 1. Pastas verificadas

| Pasta | Papel observado | Classificação predominante |
|---|---|---|
| [`docs/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs) | fundamentos, arranque, legado e diagnósticos | `REFERENCE`, `LEGACY`, `AUDIT` |
| [`specs/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/specs) | Specs de primeira geração e features homologadas | `SPEC`, com coexistência de gerações |
| [`schemas/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/schemas) | contratos JSON de I/O | `SCHEMA`, alguns de primeira geração |
| [`rag/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/rag) | bases de conhecimento para agentes | `RAG`, material de referência operacional |
| [`reference/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/reference) | camadas, contratos mestres e risco proposto | `REFERENCE`, `PROPOSAL` |
| [`RETOMADA/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/RETOMADA) | guia geral de harness | `REFERENCE`, generalista |
| [`backlog/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/backlog) | itens diferidos e gatilhos | `GOVERNANCE_SUPPORT`, `BACKLOG` |
| [`.claude/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.claude) | agentes, comandos, skills e avaliações | `HARNESS_TOOLING` |
| [`.clinerules/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.clinerules) | regras de operação de RAG, schemas e Specs | `INSTRUCTION_LAYER` |
| [`scripts/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/scripts) | gates e validadores | `ENFORCEMENT_TOOLING` |
| [`tests/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/tests) | lint e validação de schemas | `FEEDBACK_TOOLING` |
| [`.github/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.github) | CI | `FEEDBACK/CI` |
| [`UPGRADES/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/UPGRADES) | artefatos auxiliares de análise | `EVALUATION_ARTIFACT` |
| [`claude-code-setup-audit/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/claude-code-setup-audit) | auditorias de plugins/memória/setup | `ENVIRONMENT_AUDIT` |
| [`.agents/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.agents) | lock/configuração de skills | `ENVIRONMENT_METADATA` |

Também foram consideradas as pastas internas dessas árvores. Arquivos de raiz como [`README.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/README.md), [`AGENTS.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/AGENTS.md), [`GLOSSARIO.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/GLOSSARIO.md), [`ROADMAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ROADMAP.md) e [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md) foram usados como referência, não como alvo desta auditoria de pastas.

## 2. Conclusão executiva

O repositório possui boa separação física, mas a separação semântica ainda não é suficiente para um agente. A mesma ideia aparece em camadas com papéis diferentes:

- uma regra pode existir na Constituição, no RAG, no schema, na Spec de primeira geração e num script;
- uma proposta pode ser lida como runtime;
- um schema pode impor comportamento que a decisão humana marcou como piloto;
- uma ferramenta pode bloquear edição de texto, mas não garantir a semântica completa do harness;
- um resultado de avaliação pode parecer uma norma;
- um artefato de setup pode ser confundido com componente do SOT.

O problema transversal é a ausência de um **contrato de status, autoridade e sucessão aplicável a todas as pastas**.

### Riscos de maior impacto

1. [`README.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/README.md) está atrasado em relação ao Roadmap e ao Catálogo.
2. `specs/`, `schemas/` e `rag/` ainda formam um conjunto de primeira geração com score 0–9, TMP e responsabilidades antigas.
3. Os schemas validam forma, mas não implementam vários gates semânticos constitucionais.
4. O lint atual só percorre arquivos Markdown diretamente em `specs/`, ignorando `specs/features/`.
5. RAG não possui mecanismo formal visível de invalidar chunks superseded.
6. `reference/` contém propostas de risco detalhadas que podem ser confundidas com baseline.
7. `.claude/` contém instruções com carimbos de sincronização divergentes das atas recentes.
8. Os relatórios de avaliação e setup não têm fronteira explícita entre evidência, recomendação e autoridade.

## 3. Achados por pasta

## 3.1 `docs/`

### TAX-DOC-001 — `docs/` mistura referência, arranque, legado e diagnóstico

**Severidade:** HIGH  
**Evidência:** [`docs/fundamentos/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs/fundamentos), [`docs/arranque/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs/arranque) e [`docs/_legacy/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs/_legacy) possuem convenções diferentes; alguns arquivos são pareceres, outros são fontes históricas, outros são planos de produto.

**Risco:** “documentação no repositório” pode ser lida como “norma vigente”.

**Sugestão:** acrescentar em todos os documentos um cabeçalho mínimo:

```text
document_class: REFERENCE | AUDIT | LEGACY | HOMOLOGATION_RECORD | PROPOSAL
normative_authority: NONE | GOVERNANCE/<file> | ROADMAP | ATOMIC-SPEC
status: ...
superseded_by: ...
```

Não mover ou apagar arquivos congelados sem decisão de hygiene.

### TAX-DOC-002 — `docs/fundamentos/` ainda é fonte semântica para regras já migradas

**Severidade:** HIGH  
**Evidência:** [`ARIA-plano-mestre.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs/fundamentos/ARIA-plano-mestre.md), [`ENGENHARIA-GERAL.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs/fundamentos/ENGENHARIA-GERAL.md) e [`KERNEL-V2.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs/fundamentos/KERNEL-V2.md) contêm stack, score, agentes e runtime de uma geração anterior, embora continuem referenciados por Rules, CEE, SAS, schemas e RAG.

**Risco:** a governança diz que esses documentos são referência/legado, mas os contratos derivados ainda apontam para eles como fonte normativa.

**Sugestão:** distinguir em cada citação:

- `[FONTE HISTÓRICA]` — origem da ideia;
- `[ÂNCORA VIGENTE]` — Constituição/Rules/Canon/Spec;
- `[COMPATIBILIDADE]` — trecho ainda aproveitado;
- `[SUPERSEDIDO]` — trecho não aplicável.

### TAX-DOC-003 — documentos de arranque não distinguem decisão, parecer e estado operacional

**Severidade:** MEDIUM  
**Evidência:** [`docs/arranque/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs/arranque) reúne questionário, respostas, pareceres, auditorias e atas, que possuem autoridades diferentes.

**Risco:** um parecer diagnóstico pode ser interpretado como decisão homologada; uma resposta pode ser lida como regra sem a ata correspondente.

**Sugestão:** cada documento de arranque deve declarar `input`, `decision_status`, `authority_record` e `downstream_effect`.

### TAX-DOC-004 — `docs/_legacy/` está fisicamente separado, mas ainda é referenciado por agentes e fluxos

**Severidade:** MEDIUM  
**Evidência:** [`docs/_legacy/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/docs/_legacy) contém prompts, snapshots e rascunhos; a existência do diretório é correta, mas não há garantia uniforme de que referências o tratem como não normativo.

**Sugestão:** usar um marcador único no início de cada arquivo:

`LEGACY — consulta histórica; não usar para derivar invariantes, Specs ou schemas.`

## 3.2 `specs/`

### TAX-SPEC-001 — coexistem Specs de primeira geração e Specs de feature/harness

**Severidade:** CRITICAL  
**Evidência:** [`specs/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/specs) contém `elliott-wave.spec.md`, `fibonacci.spec.md`, `smc.spec.md`, `ict.spec.md` e `synthesis.spec.md`, mas também `features/SPEC-001/` e `features/SPEC-019/`. O README afirma que os cinco agentes são referência e serão substituídos pelas SPEC-010…014.

**Risco:** um agente pode tratar `synthesis.spec.md` como a Spec vigente de Synthesis, embora ela própria diga que será substituída pela SPEC-014.

**Sugestão:** aplicar classificação por geração:

| Geração | Uso |
|---|---|
| `GEN-1_REFERENCE` | Specs soltas de agentes; não autorizam runtime |
| `FEATURE_SPEC` | `features/SPEC-00x/plan.md` e `checks.md` |
| `HOMOLOGATED_BASELINE` | somente quando Catálogo/DHR confirmarem |
| `SUPERSEDED` | preservada para rastreabilidade |

### TAX-SPEC-002 — a Spec de Synthesis ainda calcula Conviction apesar da separação Q-007

**Severidade:** CRITICAL  
**Evidência:** [`synthesis.spec.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/specs/synthesis.spec.md) declara que calcula convicção global, enquanto o cabeçalho reconhece que `Conviction Engine` é separado e que a arbitragem ficará para SPEC-014.

**Risco:** uma nova implementação ou avaliação pode duplicar o cálculo ou fundir Conviction e Synthesis.

**Sugestão:** marcar as seções de cálculo como `SUPERSEDED/REFERENCE` e apontar para a futura SPEC-003/CCM-001; manter no artefato de referência somente a responsabilidade de arbitragem autorizada.

### TAX-SPEC-003 — estados, thresholds e ações de primeira geração não estão separados do contrato atual

**Severidade:** HIGH  
**Evidência:** as Specs soltas descrevem estados de agente, score e respostas operacionais; as features usam BASpec/D0–D9 e decisões abertas.

**Risco:** estado de agente vira estado de hipótese; limiar piloto vira invariante definitivo; “descartar silenciosamente” entra em conflito com auditabilidade.

**Sugestão:** declarar namespace e status para cada regra:

`AGENT_STATE`, `HYPOTHESIS_STATE`, `GATE_STATE`, `PILOT_THRESHOLD`, `NORMATIVE_INVARIANT`.

### TAX-SPEC-004 — os validadores de spec não abrangem toda a árvore de features

**Severidade:** HIGH  
**Evidência:** [`tests/lint-specs.js`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/tests/lint-specs.js) lê apenas os arquivos diretamente dentro de `specs/`, enquanto as Specs de features ficam em `specs/features/SPEC-001` e `SPEC-019`.

**Risco:** uma feature pode não ser lintada pelo comando que promete validar as Specs.

**Sugestão:** o lint deve percorrer recursivamente somente os padrões autorizados e distinguir `plan.md`, `checks.md` e Specs de referência. A mudança precisa ser proposta como tooling, com teste de regressão.

## 3.3 `schemas/`

### TAX-SCHEMA-001 — schema de Synthesis mantém score operacional paralelo ao Conviction Vector

**Severidade:** CRITICAL  
**Evidência:** [`synthesis.output.json`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/schemas/synthesis.output.json) exige `score_total` 0–9, `convicção_global` e `conviction_vector` 8D; o score soma Elliott + SMC + ICT e não inclui Fibonacci.

**Risco:** três métricas coexistem sem contrato explícito de precedência: score, percentual e vetor.

**Sugestão:** documentar no schema, ou em CCM/CDM futuro, a relação formal:

- score = filtro piloto independente ou derivação?
- percentual = projeção agregada ou medida distinta?
- vetor = objeto cognitivo canônico?
- qual divergência bloqueia?

Até a decisão J-001, evitar converter o schema em fórmula definitiva.

### TAX-SCHEMA-002 — schema aceita forma válida sem garantir invariantes de negócio

**Severidade:** HIGH  
**Evidência:** o schema de saída permite `COMPRA`/`VENDA` por enum e descreve condições no texto, mas não exige condicionalmente `invalidação_explícita`, `risk_reward >= 3`, ausência de conflito ou score mínimo. `required` também não exige vários campos necessários para um sinal.

**Risco:** `npm test` pode passar com um payload formalmente válido, mas constitucionalmente inválido.

**Sugestão:** separar:

1. schema estrutural JSON;
2. validação semântica de sinal;
3. gate de enforcement.

Não embutir todas as regras em JSON Schema sem decidir o contrato; criar testes negativos para cada salvaguarda vigente.

### TAX-SCHEMA-003 — inputs exigem quatro especialistas, enquanto o fluxo constitucional inclui Fractal como camada

**Severidade:** HIGH  
**Evidência:** [`synthesis.input.json`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/schemas/synthesis.input.json) exige Elliott, Fibonacci, SMC e ICT, mas a Constituição inclui Elliott → Fibonacci → Fractal → SMC → ICT e o output possui dimensão fractal.

**Risco:** o agente não sabe se Fractal é output independente, subfunção de Elliott/Fibonacci ou cálculo interno.

**Sugestão:** manter o schema atual como `GEN-1_REFERENCE` e registrar a lacuna como decisão não resolvida. Não adicionar `fractal_output` até existir decisão/Spec.

### TAX-SCHEMA-004 — contratos de risco e Signal Package ainda não têm separação física clara

**Severidade:** HIGH  
**Evidência:** `synthesis.output.json` inclui sizing, alavancagem e risco, embora o Risk Agent seja futuro e TMP seja interno após EUA-E19a.

**Risco:** Synthesis pode ser interpretado como Risk Agent ou produtor do pacote de fronteira.

**Sugestão:** distinguir schemas por artefato:

- `synthesis.output` — decisão/snapshot interno;
- `tmp.internal` — handoff interno;
- `risk.decision` — futuro;
- `signal-package.frontier` — futuro e separado.

## 3.4 `rag/`

### TAX-RAG-001 — RAG reproduz regras antigas e novas sem metadado de vigência

**Severidade:** CRITICAL  
**Evidência:** [`synthesis.knowledge.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/rag/synthesis.knowledge.md) contém score 0–9, calcula TMP e descreve “decisão operacional definitiva”, apesar de registrar Q-007/Q-008/Q-009 no cabeçalho.

**Risco:** o agente recupera chunks antigos como instrução vigente; o cabeçalho de correção não altera o texto dos chunks.

**Sugestão:** cada chunk deve possuir `status`, `authority`, `effective_from`, `supersedes`, `source_kind` e `do_not_use_if`. Chunks superseded não devem entrar na recuperação padrão.

### TAX-RAG-002 — RAG mistura conhecimento, política e algoritmo

**Severidade:** HIGH  
**Evidência:** os arquivos de RAG contêm missões, score, thresholds, estados, passos, saídas e regras de bloqueio no mesmo formato.

**Risco:** um prompt pode tratar uma explicação de domínio como regra de enforcement, ou uma heurística como contrato.

**Sugestão:** separar tipos de chunk:

`DOMAIN_KNOWLEDGE`, `NORMATIVE_RULE`, `PROCEDURE`, `EXAMPLE`, `LEGACY`, `EVALUATION_NOTE`.

Somente `NORMATIVE_RULE` referenciado por fonte vigente pode orientar gate.

### TAX-RAG-003 — não há evidência de validação de consistência RAG contra Catálogo

**Severidade:** HIGH  
**Evidência:** existem scripts de avaliação em [`.claude/skills/harness-eval/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.claude/skills/harness-eval), mas a estrutura observada mede correctness/usefulness/agreement e não demonstra um gate que bloqueie chunks com status antigo, 4D ou TMP de fronteira.

**Sugestão:** criar futuramente uma checagem de drift RAG:

1. extrair termos/versionamentos;
2. comparar com GLOSSARIO, Rules, Catálogo e decisões abertas;
3. classificar conflito;
4. bloquear somente quando houver autoridade explícita para bloqueio.

## 3.5 `reference/`

### TAX-REF-001 — referências externas estão bem sinalizadas, mas podem ser importadas como norma por downstreams

**Severidade:** HIGH  
**Evidência:** [`reference/camadas/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/reference/camadas) contém camadas e Master Contracts detalhados; [`CATALOGO-OFICIAL.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/CATALOGO-OFICIAL.md) declara que são não normativos.

**Risco:** o conteúdo normativo e os nomes de camadas parecem prontos para implementação; um agente pode promover um `Master Contract` sem homologação.

**Sugestão:** incluir uma instrução uniforme no cabeçalho e no início de cada chunk:

`REFERENCE ONLY — não criar RULE, schema, componente ou invariante a partir deste arquivo sem DHR.`

### TAX-REF-002 — SOT-RISK-MASTER-001 detalha Risk Agent antes da família RISK-SPEC

**Severidade:** CRITICAL  
**Evidência:** [`SOT-RISK-MASTER-001_Consolidado.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/reference/SOT-RISK-MASTER-001_Consolidado.md) é explicitamente `[PROPOSTA]`, mas define pipeline, RDR, Risk Harness, invariantes de risco e responsabilidade de emissão de Signal Package.

**Risco:** a riqueza do documento pode superar a autoridade real e antecipar decisões abertas `RISK-ARR-LOC-001`, `RISK-CONV-001` e `D-RISK-SP-001`.

**Sugestão:** dividir, quando autorizado, em:

- registro de decisões humanas já tomadas;
- proposta de arquitetura;
- questões abertas;
- futura RISK-SPEC;
- contrato do Signal Package.

Enquanto isso, manter o documento fora de qualquer índice de runtime.

### TAX-REF-003 — nomes de camada competem com F.1–F.4, D0–D9 e Quality Gates

**Severidade:** MEDIUM  
**Evidência:** as camadas externas possuem níveis, nós e classificações próprias; [`CONFLICT-MAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/CONFLICT-MAP.md) registra rejeições de rótulos concorrentes.

**Sugestão:** todo documento em `reference/camadas/` deve incluir tabela “rótulos locais não canônicos” e correspondência, quando autorizada, com F.1–F.4, D0–D9 e L1–L4.

## 3.6 `RETOMADA/`

### TAX-RET-001 — GEH-001 é generalista, mas é usado como fundamento específico do SOT

**Severidade:** HIGH  
**Evidência:** [`GEH-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md) declara escopo independente de domínio, enquanto GPR/PPQ/PAP o usam como fundamentação do SOT.

**Risco:** exemplos generalistas ou recomendações externas ganham status de requisito específico de trading.

**Sugestão:** distinguir `framework transportável` de `instanciação SOT`; toda regra importada deve apontar para a decisão/Spec que a especializou.

### TAX-RET-002 — GEH-001 contém padrões de orquestração que podem reintroduzir taxonomia antiga

**Severidade:** MEDIUM  
**Sugestão:** marcar padrões como `PATTERN`, não como componentes; nunca resolver `Master Orchestrator`, `Scheduler` ou `Mission Engine` apenas por analogia com GEH-001.

## 3.7 `backlog/`

### TAX-BLK-001 — RMR-001 contém modelo de estado claro, mas seu status é “PROPOSTA” apesar de estar no Catálogo como baseline

**Severidade:** CRITICAL  
**Evidência:** [`RMR-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/backlog/RMR-001_Painel_Backlog.md) declara `HOMOLOGADO — BASELINE` no cabeçalho e, logo depois, `Status epistemológico: este painel é PROPOSTA`.

**Risco:** o mecanismo que controla ativação de backlog pode ser tratado como não vinculante ou como autoridade concorrente.

**Sugestão:** separar `document status` de `item epistemic status`: o painel pode ser baseline enquanto cada item continua `[INFERÊNCIA]`, `[FATO]`, `PROPOSTO`, `EM ESPERA` ou `ATIVADO`.

### TAX-BLK-002 — gatilhos de backlog podem parecer runtime

**Severidade:** HIGH  
**Evidência:** RMR-001 usa “o sistema informa”, mas também esclarece que não há runtime e que o informe é garantido por gates.

**Sugestão:** renomear conceitualmente para `process gate surfacing` até existir automação; o script BL-006 deve ser ferramenta de governança, não componente cognitivo.

### TAX-BLK-003 — BL-018 descreve Risk Agent antes de sua autorização

**Severidade:** HIGH  
**Sugestão:** manter BL-018 claramente `FUTURE_COMPONENT/PROPOSAL`, com um único campo de gatilho e sem duplicar decisões de `reference/SOT-RISK-MASTER-001`.

## 3.8 `.claude/`

### TAX-CLAUDE-001 — carimbos de sincronização dos agentes estão divergentes

**Severidade:** CRITICAL  
**Evidência:** [`especificador.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.claude/agents/especificador.md) declara `sincronizado-até: DHR-PROV-WEB-001`, mas inclui comentários sobre EUA-E17/E18/E19; [`revisor.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.claude/agents/revisor.md) declara `sincronizado-até: DHR-EUA-E19`; a ata DHR-EUA-E19a é posterior e o Catálogo registra efeitos adicionais.

**Risco:** o agente não sabe se o carimbo é apenas última sincronização textual, última DHR lida ou versão normativa aplicada.

**Sugestão:** substituir um carimbo único por:

`last_sync_dhr`, `last_sync_catalog_date`, `required_sources`, `runtime_policy_version`.

### TAX-CLAUDE-002 — instruções de agentes misturam mandato, processo e referência histórica

**Severidade:** HIGH  
**Evidência:** os prompts contêm regras operacionais, explicações, nomes de versões, referências a propostas e instruções de leitura.

**Risco:** uma nota histórica dentro do prompt pode adquirir força de instrução; uma instrução de processo pode ser confundida com regra constitucional.

**Sugestão:** separar seções com marcadores:

`MANDATE`, `MUST_READ`, `PROCESS_GATE`, `NON_NORMATIVE_CONTEXT`, `CURRENT_SYNC`.

### TAX-CLAUDE-003 — avaliações em `harness-eval/runs/` não são claramente separadas de autoridade

**Severidade:** MEDIUM  
**Sugestão:** marcar todos os resultados como `EVALUATION_ARTIFACT`, com dataset, versão do harness, commit/digest, status de reprodução e relação com eventual gate F.3/F.4.

## 3.9 `.clinerules/`

### TAX-CLINE-001 — regras de RAG, schemas e Specs duplicam autoridade fora de governance

**Severidade:** HIGH  
**Evidência:** [`sot-rag.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.clinerules/sot-rag.md), [`sot-schemas.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.clinerules/sot-schemas.md) e [`sot-specs.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.clinerules/sot-specs.md) orientam comportamento de ferramenta.

**Risco:** uma regra operacional local pode divergir de RULES/ATOMIC-SPEC e ser aplicada como autoridade equivalente.

**Sugestão:** cada regra deve declarar `enforcement_class` e sua fonte; `.clinerules` pode orientar ferramenta, mas não criar invariante.

## 3.10 `scripts/`, `tests/` e `.github/`

### TAX-TOOL-001 — detector, gate e teste não estão explicitamente separados

**Severidade:** HIGH  
**Evidência:** [`scripts/gate-check.js`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/scripts/gate-check.js) bloqueia alguns padrões textuais; [`tests/lint-specs.js`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/tests/lint-specs.js) faz lint; [`tests/validate-schemas.js`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/tests/validate-schemas.js) valida JSON; [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md) define Detector ≠ Gate.

**Risco:** passar no detector pode ser interpretado como conformidade semântica ou homologação.

**Sugestão:** toda saída deve declarar:

`tool_role: DETECTOR | GATE | FEEDBACK | EVALUATION`  
`authority: ...`  
`scope: ...`  
`does_not_prove: ...`

### TAX-TOOL-002 — `gate-check.js` depende de regex estreita

**Severidade:** MEDIUM  
**Evidência:** o gate procura frases literais como “ICT pode criar hipótese”, R:R permissivo e SMC sobrepondo Elliott.

**Risco:** variações linguísticas passam pelo detector; textos historicamente inválidos podem não ser identificados.

**Sugestão:** manter regex como sensor barato, mas complementar com vocabulário controlado, IDs de regra e testes de mutação. Não chamar o regex de verificador completo.

### TAX-TOOL-003 — CI pode validar somente a geração de primeira linha

**Severidade:** HIGH  
**Evidência:** o lint de Specs lê apenas o diretório imediato; a árvore `features/` não é coberta por esse script.

**Sugestão:** revisar o workflow em [`.github/workflows/ci.yml`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.github/workflows/ci.yml) para indicar explicitamente quais famílias são validadas e quais são referência. Adicionar uma etapa específica para `features/SPEC-*`.

## 3.11 `UPGRADES/`

### TAX-UPG-001 — grafo de conhecimento é snapshot estrutural, não fonte semântica

**Severidade:** MEDIUM  
**Evidência:** [`meta.json`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/UPGRADES/understand-anything-graph/meta.json) registra digest, contagem de arquivos e timestamp; o `knowledge-graph.json` é derivado.

**Risco:** um agente pode usar o grafo como representação atual quando o repositório mudou.

**Sugestão:** inserir `derived_only: true`, `source_digest`, `generated_at`, `not_authority: true` e política de invalidação após alteração.

## 3.12 `claude-code-setup-audit/`

### TAX-SETUP-001 — auditorias de plugin/memória estão fora do domínio normativo, mas tratam riscos de governança relevantes

**Severidade:** HIGH  
**Evidência:** [`findings.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/claude-code-setup-audit/2026-09-25T08-50-27-189/findings.md) conclui que memória persistente externa é compatível, mas requer política de privacidade/retenção.

**Risco:** o resultado pode ser entendido como autorização de instalação ou como parte nativa do harness.

**Sugestão:** classificar como `ENVIRONMENT_AUDIT`, declarar que não altera a SSoT do SOT e criar, se desejado, uma política separada de retenção, privacidade e não autoridade da memória.

### TAX-SETUP-002 — snapshots de setup não têm vínculo formal com versão do harness

**Severidade:** MEDIUM  
**Sugestão:** cada auditoria deve indicar `repo_digest`, `tooling_version`, `environment_scope`, `reproducibility` e `non_normative: true`.

## 3.13 `.agents/`

### TAX-AGENTMETA-001 — metadata de skills é ambiente, não contrato do SOT

**Severidade:** LOW  
**Evidência:** [`.agents/.skill-lock.json`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.agents/.skill-lock.json) registra dependências/configuração de skills.

**Sugestão:** explicitar `environment_metadata: true` e impedir que o arquivo seja usado como fonte de autoridade arquitetural.

## 4. Achados transversais entre pastas

### TAX-X-001 — ausência de um vocabulário de status universal

**Severidade:** CRITICAL  
`BASELINED`, `HOMOLOGADO`, `CANDIDATO`, `PROPOSTA`, `REFERENCE`, `LEGACY`, `SUPERSEDED`, `FUTURE` e `[INFERÊNCIA]` aparecem em documentos e formatos diferentes. Não existe uma tabela universal que diga se são status de documento, item, decisão, regra, componente, chunk ou avaliação.

**Sugestão:** publicar uma taxonomia de lifecycle:

| Dimensão | Valores sugeridos |
|---|---|
| documento | `DRAFT`, `CANDIDATE`, `HOMOLOGATED`, `BASELINED`, `SUPERSEDED`, `LEGACY` |
| decisão | `OPEN`, `RESOLVED`, `DEFERRED`, `REJECTED` |
| componente | `PROPOSED`, `AUTHORIZED`, `FUTURE`, `ACTIVE`, `RETIRED` |
| evidência | `OBSERVED`, `DERIVED`, `AUDIT_RESULT` |
| avaliação | `RUN`, `REPRODUCIBLE`, `NON_REPRODUCIBLE`, `REFERENCE` |

### TAX-X-002 — falta de ligação máquina-legível entre autoridade e derivados

**Severidade:** HIGH  
**Sugestão:** todo schema, RAG chunk, Spec, script e prompt deve apontar para:

`authority_id`, `authority_version`, `source_kind`, `effective_from`, `supersedes`, `open_decisions`.

### TAX-X-003 — migração para Harness Cognitivo ainda é parcial

**Severidade:** CRITICAL  
O fluxo físico já é spec-first, mas os artefatos derivados continuam orientados a produto:

`Synthesis → score → sizing → TMP/alerta`

em vez de separar:

`evidência → hipótese → fusion → conviction → síntese → handoff interno → pacote de fronteira futuro`.

**Sugestão:** tratar todo artefato de primeira geração como compatibilidade, não como runtime autorizado, até que a família de Specs correspondente seja homologada.

### TAX-X-004 — ferramentas validam sintaxe melhor que semântica

**Severidade:** HIGH  
JSON Schema, lint, regex gate, CI e harness-eval cobrem superfícies diferentes, mas não existe uma matriz única que declare qual ferramenta prova qual requisito.

**Sugestão:** criar uma matriz de enforcement:

| Requisito | Detector | Gate | Feedback | Avaliação | Autoridade |
|---|---|---|---|---|---|
| JSON válido | validate-schemas | CI, se configurado | sim | não | schema |
| BASpec | lint/validator | Revisor | sim | não | ATOMIC-SPEC |
| ICT não cria hipótese | gate-check + Revisor | gate autorizado | sim | sim | Constituição/Rules |
| Conviction 8D | schema + auditoria | futuro gate semântico | sim | sim | Q-008/GLOSSARIO |
| TMP vs Signal Package | vocabulário/RAG audit | futuro gate | sim | sim | EUA-E19a |

## 5. Matriz final de classificação das pastas

| Pasta | Status recomendado | Pode criar norma? | Pode bloquear? | Ação principal |
|---|---|---:|---:|---|
| `docs/` | referência/legado/auditoria | não | não | marcar status e fontes |
| `specs/` | Specs autorizadas + referência GEN-1 | somente via homologação | Revisor/validator conforme contrato | separar gerações |
| `schemas/` | contratos estruturais | não sozinho | validator/gate autorizado | separar semântica |
| `rag/` | conhecimento recuperável | não | não, salvo ferramenta autorizada | versionar chunks |
| `reference/` | proposta/referência | não | não | bloquear promoção implícita |
| `RETOMADA/` | guia generalista | não | não | separar framework de instanciação |
| `backlog/` | rastreabilidade | não | gate pode apontar pendência | separar painel e itens |
| `.claude/` | harness tooling/papéis | não | ferramentas definidas | sincronizar carimbos |
| `.clinerules/` | instrução local | não | ferramenta pode aplicar escopo local | apontar autoridade |
| `scripts/` | enforcement tooling | não | somente scripts designados | declarar papel |
| `tests/` | feedback | não | CI pode bloquear qualidade técnica | cobrir subpastas |
| `.github/` | CI | não | workflow | declarar superfície |
| `UPGRADES/` | snapshot derivado | não | não | marcar não autoridade |
| `claude-code-setup-audit/` | auditoria ambiental | não | não | separar de baseline |
| `.agents/` | metadata ambiental | não | não | não usar como norma |

## 6. Perguntas que exigem decisão humana

1. As Specs soltas da primeira geração devem permanecer em `specs/` com alias controlado ou ser movidas para uma área `reference/legacy`?
2. O score 0–9 continuará como filtro piloto independente do Conviction Vector ou será substituído por decisão do CCM-001?
3. Fractal terá output próprio, será subfunção de outro especialista ou permanecerá como dimensão calculada?
4. O RAG de primeira geração será reescrito, versionado por chunks superseded ou congelado como histórico?
5. Os schemas atuais continuam sendo contratos de referência ou devem ser marcados como não autorizados para runtime?
6. Deve existir uma política formal de memória externa para o setup Claude Code?
7. O lint deve validar recursivamente todas as features ou somente os arquivos canônicos de primeira geração?
8. Qual artefato será o contrato formal futuro do `Signal Package`?

O relatório não responde essas perguntas por inferência.

## 7. Ordem sugerida de alinhamento

1. Publicar taxonomia universal de status e classes de documento.
2. Corrigir o README e índices vivos para refletir a autoridade atual.
3. Marcar Specs/RAG/schemas de primeira geração como `GEN-1_REFERENCE`.
4. Separar schema estrutural de gate semântico.
5. Criar metadados de vigência e sucessão para RAG e prompts.
6. Corrigir cobertura recursiva de lint/CI, se homologado.
7. Isolar Risk Agent e Signal Package como futuro até RISK-SPEC.
8. Formalizar a matriz de enforcement e a política de memória ambiental.
9. Só depois iniciar reescrita ou substituição de artefatos derivados.

## 8. Regra de preservação

Nenhum achado autoriza apagar, renomear ou reescrever arquivos existentes. A migração deve usar:

- aliases controlados;
- status explícito;
- sucessão documentada;
- ponteiros de autoridade;
- preservação de snapshots;
- emendas homologadas;
- distinção entre detecção, gate, feedback e avaliação.

**Resultado:** as pastas restantes já podem ser alinhadas ao Harness Cognitivo sem destruição documental. O próximo passo correto é uma camada transversal de taxonomia e metadados, seguida por emendas específicas apenas onde uma autoridade humana confirmar a mudança.
