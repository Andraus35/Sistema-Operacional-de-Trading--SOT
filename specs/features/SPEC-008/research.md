# Dossiê de Pesquisa — SPEC-008: Manager — Orquestração Mecânica (Fase 1 + serviços de tempo) (slot ROADMAP §7, FASE 4)

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-SPEC-008 |
| **Método** | ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06/07) + DHR-BACKLOG-ABERTURA-001 |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 5.5) |
| **Data de acesso web** | 2026-11-07 (todas as fontes `[EXTERNO]` e repositórios) |
| **Complexidade** | **PROPOSTA — a confirmar por Andraus** (ABERTURA §1, P-1/P-2). O slot traz "P0 — CRITICAL · D0–D8" (`ROADMAP.md` §7, SPEC-008). Dossiê feito em profundidade CRITICAL (cobre todas as opções). |
| **Validade do Dossiê (ECC-VAL-001 — FECHADA, DHR-DEC-003)** | Acesso 2026-11-07. **HIGH ou CRITICAL → 90 dias → validade 2027-02-05** (vale para as duas peças da proposta de divisão — ABERTURA §3). Cai antes se o contexto mudar materialmente (ex.: Andraus editar WF-R01..R03 ou WF-F02 no `WORKFLOW.md`; abertura da SPEC-009 fixar o esquema de estado — G-001; decisão sobre M-001). Dossiê vencido não dispensa reabrir a pesquisa (fail-closed, RULE-ECC-02). |
| **Natureza** | **Dossiê `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão (CONS-01). Tudo o que propõe é `[PROPOSTA]`. |
| **Status epistemológico** | Conteúdo web e de repositórios = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1; RULE-ECC-02). Fontes classificadas e etiquetadas; veracidade das páginas não atestada. Capturas literais em `sources/` (RULE-ECC-04); limitações em `sources/_LIMITACAO-WEB.txt`. |
| **Autorização** | Ordem do Orquestrador por decisão de Andraus (chat, 2026-11-07): "SPEC-008 Manager Fase 1" como próxima Spec a abrir; ETAPA DE ABERTURA — Dossiê + proposta de abertura; **sem** `plan.md`/`checks.md`. |
| **Fronteiras respeitadas** | INV-01 (hierarquia Elliott→Fibonacci→Fractal→SMC→ICT), INV-02 (ICT não cria hipótese), INV-04 (custo nunca no Conviction Vector), INV-05 (SOT não executa ordem), INV-07 (nada apagado), INV-09 (sem baseline informal). Não redefine CHM-001/CEM-001/CCM-001/CEE-001 (CC-02). `WORKFLOW.md` v2.1 citado só por ID. |

> **Aviso de método (RULE-MET-01).** (1) Métricas de repositório vieram da página HTML pública; alertas de segurança = INDETERMINADO, registrados como 0 pelo critério das Specs anteriores. (2) A ferramenta de leitura web limita a citação literal a cerca de 125 caracteres — trechos são literais (≥100 caracteres), às vezes recorte de frase maior, anotados como tal. (3) Pesquisa sobre horário de pregão/feriados foi **inconclusiva** (página oficial indisponível) — nenhuma alegação carregada (§6). (4) Sem Bash: os gates (`backlog_triggers --abertura`, `check_repo_research`, `build_map`, `check_refs`) são do Orquestrador (ABERTURA §12). (5) O Benchmark Inteligencia-SOT **não** foi lido. Distingo **[FONTE]** (documento do SOT) de **[INFERÊNCIA]** e de **[EXTERNO]**.

---

## 0. Auditoria de entrada — o que é a SPEC-008 no SOT hoje

| Âncora | Verificação (lida em 2026-11-07) | Resultado |
|---|---|---|
| (a) Slot | `ROADMAP.md` §7: "Decidir: quem pensa; quando; por que; em que ordem; com qual profundidade; com qual orçamento; quais Skills despertar/não despertar; quando interromper/aguardar/escalar/encerrar. Incorpora ativação progressiva/lazy orchestration; dispatch/grafo de dependências; relógio/Killzone; alarme FSM; FSM do ciclo; orçamento." | `[FONTE]`, FATO ARQUITETURAL — slot **indicativo, não aberto** (tabela do §26: "Indicativo — não aberta"). |
| (b) Origem da forma atual | DHR-EUA-E23 §2 item 1: SPEC-008 = "Manager — Orquestração Mecânica", Fase 1 + serviços de tempo, Classe predominante D/C (orientativa); item 3: "número, fronteira e decomposição final de cada uma das três Specs só se fixam na abertura"; "A decomposição pode ainda ser revista (dividir/fundir — INV-07) na abertura". | **FATO NORMATIVO** (direção). Esta abertura **pode** propor divisão. |
| (c) Ator único | ADR-MANAGER-001 §2.2: "O Manager Agent é o único componente de orquestração do SOT"; §2.5: "Fase 1 — Dispatch | Mecânico/determinístico | Resolve grafo de dependências; sem julgamento analítico"; "Manager Agent não é um agente analítico. Não analisa mercado." | **FATO NORMATIVO.** Fase 1 sem modelo de linguagem decidindo (Classe D/C). |
| (d) "Manager Contract" | DHR-EUA-E23 §2 item 2: "Cria-se, quando da abertura, um documento de contrato comum (não um agente novo) — pai de herança vertical (RULE-HV) das três Specs". Busca por "Manager Contract" (2026-11-07): só aparece em atas, ROADMAP, GLOSSARIO, MATRIZ e agentes — **o documento não existe**. | **Lacuna** — esta é a 1ª das 3 Specs do Manager a abrir. Onde e quando nasce o contrato = **P-4** (ABERTURA). |
| (e) Setup soberano | `WORKFLOW.md` v2.1: WF-02/03/04/05, WF-K01..K04, WF-T01/T02, WF-A01..A03, WF-F01/F02, WF-P01/P02, WF-R01..R03 (`[REVISAR · BL-026]`), WF-C01, WF-X04, WF-J01, WF-D03 (ABERTA). | **FATO NORMATIVO** (declaração de Andraus). Conformidade obrigatória (DHR-WF-001). Ver §5 (lente 3). |
| (f) Invocação macro | RULE-CF-010 (SPEC-003, BASELINE): "essa invocação é do Manager (SPEC-008 Fase 1 / SPEC-014 Fase 2) e NÃO é implementada por esta Spec"; Q-A5 FECHADA (DHR-DEC-001): 2x por ciclo. | **FATO NORMATIVO.** A SPEC-008 **invoca** a leitura macro; **não** calcula o vetor. |
| (g) Economia | CEE-001 v2.0 §10 Salvaguarda 2: "O Scheduler nunca pode suprimir a execução de um agente por motivo de custo quando houver evento estruturalmente relevante."; §9.3: "Mudanças emergenciais de custo (ex: pico de gasto inesperado) podem pausar um componente via Scheduler (kill-switch operacional), mas não podem alterar permanentemente sua classe de modelo"; Salvaguarda 1/5 (roteamento só pelo fluxo do §9). | **FATO NORMATIVO** (canon BASELINED). Orçamento da SPEC-008 **não** pode pular agente com evento estrutural relevante. Tensão §10 S2 × §9.3 registrada (§6, CF-4). *[antes: "(§6, C-4)" — prefixo trocado por R1-m02; conteúdo de R1-m01 preservado]* |
| (h) Inversão #1 | `governance/CONFLICT-MAP.md` §"Inversões contextuais", tabela linha #1 (HOMOLOGADO 2026-09-20): trigger "Ruptura de hipótese dominante"; efeito "Cognitive Scheduler desperta análise completa independente do custo". Nota de integração do mesmo documento (etiquetada lá como `[INFERÊNCIA]`): "Inversão #1 referencia o Cognitive Scheduler (SPEC-008, pendente); a mecânica de ativação será especificada nessa Spec." | **Linha #1 da tabela = FATO NORMATIVO** (homologada). **Nota de integração = INFERÊNCIA** (a própria fonte a etiqueta assim): que a mecânica seja escrita **na SPEC-008** é leitura, não norma — esta abertura **propõe** assumi-la (`[PROPOSTA]`, ABERTURA S4). Evento que dispara: ver ABERTURA S4 e §6 L-8. *[antes: célula única "**FATO NORMATIVO** (obrigação a cumprir aqui)", que promovia a nota `[INFERÊNCIA]` a norma — corrigido por R1-m06]* |
| (i) Quem já aponta para cá | SPEC-003 (Killzone/alarme "Manager/Scheduler SPEC-008/015"; invocação macro), SPEC-004/005 (orquestração "quem reage, quando" = SPEC-008; RULE-BB-005), SPEC-007/048 (orçamento e latência da consulta, `max_retrieval_rounds` = "orçamento da SPEC-008"). | `[FONTE]` (Specs BASELINE). Obrigações de interface que a SPEC-008 herda — ver ABERTURA §2, §8 e §10. **Varredura completa da SPEC-003** (plan/research/checks, linha a linha) em §8.3 (R1-M02). SPEC-006 **não** cita a SPEC-008 (Grep 2026-11-07); entra como montante indireto (ABERTURA §10, R1-m07). |
| (j) Coordenação só via quadro | RULE-BB-001 ("Comunicação entre agentes EXCLUSIVAMENTE via Blackboard Cognitivo"); RULE-BB-005 ("O Orchestrator APENAS coordena via Blackboard. NUNCA analisa diretamente."). | **FATO NORMATIVO.** Despacho = publicação/aviso via quadro e barramento (SPEC-004/005), nunca chamada direta de agente a agente. |
| (k) Backlog vinculado por regra | Gatilho `spec:SPEC-008 em redação` em BL-026, BL-043, BL-044, BL-045, BL-046 (RMR-001; confirmado pelo Orquestrador com `backlog_triggers.py --abertura SPEC-008`). | Disposições propostas em §8.4 e ABERTURA §9. |

**Conclusão.** A SPEC-008 é a **parte mecânica** do Manager: dado um pedido de ciclo (ativo, tipo de trading, tempos gráficos, Killzone — WF-01), ela decide **quem roda, em que ordem, quando, com que teto e quando parar**, sem analisar mercado: despacha o Estrutural, despacha o Institucional só se houver oportunidade, pede a leitura macro ao mecanismo da SPEC-003, arma o alarme-gatilho, abre e fecha a janela da Killzone no relógio de Nova York, dispara o Operacional só com alarme dentro da janela, conduz a máquina de estados do ciclo e entrega à Fase 2 (SPEC-014). Tudo regra fixa (Classe D), com uma trava constitutiva (Classe C): o Manager nunca analisa, nunca cria hipótese, nunca emite ordem.

---

## 1. Questões e estratégia de busca

- **Q1.** Orquestrador de agentes: quando usar fluxo de caminho fixo e quando deixar o modelo decidir? (lente Arquitetura)
- **Q2.** Despacho com grafo de dependências: como garantir ordem correta, sem ciclo, e não misturar "ordem" com "conteúdo"?
- **Q3.** Máquinas de estados de ciclo/alarme: que práticas tornam a FSM verificável (estados finais, transições fechadas)?
- **Q4.** Ciclo longo (madrugada, reinício da máquina): como retomar sem refazer nem divergir?
- **Q5.** Orçamento e limites: como impor teto de passos/voltas sem silêncio e sem cortar análise necessária?
- **Q6.** Relógio e fuso: como calcular janela em `America/New_York` com horário de verão, e o que registrar?
- **Q7.** Escola (ICT): o que a comunidade chama de Killzone, em que relógio, e onde as fontes divergem? (lente Escola)
- **Q8.** Que **repositórios seguros e bem avaliados** (RULE-ECC-06) exemplificam despacho por grafo, FSM e execução durável?
- **Q9.** Conformidade com o `WORKFLOW.md` (lente 3): que `WF-xx` a SPEC-008 toca e onde há conflito de dono?

**Estratégia:** WebFetch direto de fontes primárias conhecidas (documentação oficial, W3C, blogs de engenharia de fornecedores) para capturar trechos literais; páginas públicas de repositórios e de commits para a régua; uma busca web (WebSearch) para mapear fontes de Killzone. Sem envio de dado do projeto. Endereços (acesso 2026-11-07):
- `anthropic.com/engineering/building-effective-agents`; `anthropic.com/engineering/multi-agent-research-system`; `microsoft.com/en-us/research/articles/magentic-one-…`.
- `w3.org/TR/scxml/`; `docs.temporal.io/workflows`; `airflow.apache.org/…/core-concepts/dags.html`; `airflow.apache.org/…/authoring-and-scheduling/timezone.html`; `en.wikipedia.org/wiki/Topological_sorting`.
- `openai.github.io/openai-agents-python/running_agents/`; `docs.langchain.com/oss/python/langgraph/graph-api`; `martinfowler.com/bliki/CircuitBreaker.html`.
- `docs.python.org/3/library/zoneinfo.html`; `luxalgo.com/library/concept/killzones/`; `backtrex.com/en/blog/ict-kill-zone-times-sessions`.
- Tentativas sem resultado (nada atribuído): `langchain-ai.github.io/langgraph/concepts/durable_execution/` (só redireciona); `docs.langchain.com/…/durable-execution` (sem definição literal); `cmegroup.com/trading-hours.html` (HTTP 503); `forums.babypips.com/…` (HTTP 403).
- Repositórios (página + commits do branch padrão): `langchain-ai/langgraph`, `temporalio/temporal`, `apache/airflow`, `statelyai/xstate`, `pytransitions/transitions`.
- Leitura interna (somente leitura): ROADMAP (cabeçalho, estado, §7, §9, §21, §23, decisões); atomic-spec §15; AGENTS.md; WORKFLOW.md v2.1; ADR-MANAGER-001; EUA-E23 v2 + DHR-EUA-E23; CEE-001 v2.0 §7/§9/§10; RULES.md (RULE-BB-001..005, RULE-CEE-001..004, RULE-ECC-01..07, RULE-HV-01..04, RULE-MECH-01..04, RULE-DEC-01/02, RULE-MET-01/02, RULE-UNC-01..03, RULE-ICT-001/003); CONFLICT-MAP (timing ICT; Inversões); SPEC-003 plan (RULE-CF-010, CF-010, CF-013, WF-C01); SPEC-004/005/007/048 (referências à SPEC-008); MATRIZ-WORKFLOW-SPEC (não-normativa); RMR-001 (BL-026, BL-043..046); SPEC-049 ABERTURA/research (modelo de forma); `scripts/check_repo_research.py` (régua).

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Papel |
|---|---|---|---|
| SRC-ANTH-AGENTS-01 | Anthropic — Building effective agents | Prática + Opinião (fornecedor) | Q1 — fluxo fixo × agente |
| SRC-ANTH-MULTI-01 | Anthropic — Multi-agent research system | Experimento (relato) + Prática | Q1/Q4/Q5 — regra de esforço; despacho síncrono; retomar |
| SRC-MAGONE-01 | Microsoft Research — Magentic-One | Experimento + Prática | Q1 — contraste (orquestrador que replaneja por modelo) |
| SRC-AIRFLOW-DAG-01 | Apache Airflow — Dags | Prática | Q2 — grafo cuida da ordem, não do conteúdo |
| SRC-TOPO-01 | Wikipedia — Topological sorting | Padrão (de facto, algoritmo clássico) | Q2 — ordem por dependência; sem ciclo |
| SRC-SCXML-01 | W3C — SCXML | Padrão (Recomendação W3C) | Q3 — FSM com estados finais |
| SRC-TEMPORAL-01 | Temporal — Workflows | Prática | Q4 — execução durável; reexecução determinística |
| SRC-OAI-MAXTURNS-01 | OpenAI Agents SDK — Running agents | Prática | Q5 — teto de voltas com erro explícito |
| SRC-LGRAPH-RECUR-01 | LangGraph — Graph API | Prática | Q5 — teto de passos; passos discretos |
| SRC-CB-01 | Fowler — CircuitBreaker | Prática + Opinião (especialista) | Q5 — parar de chamar após falhas |
| SRC-ZONEINFO-01 | Python — zoneinfo | Padrão (doc. oficial; banco IANA) | Q6 — fuso IANA; hora ambígua |
| SRC-AIRFLOW-TZ-01 | Apache Airflow — Time zones | Prática | Q6 — UTC interno; agenda local com horário de verão |
| SRC-KZ-LUX-01 | LuxAlgo — Killzones | Prática (convenção de varejo) + Opinião | Q7 — horários em NY; janela asiática divergente |
| SRC-KZ-BTX-01 | Backtrex — Kill zone times | Opinião + Prática (varejo) | Q7 — NY AM divergente; tabela em UTC fixo |
| REPO-langgraph / REPO-temporal / REPO-airflow / REPO-xstate | repositórios **elegíveis** (§4) | Prática | Q8 |
| REPO-transitions | repositório **NÃO ELEGÍVEL** (§4) | — (registrado, descartado) | transparência da régua |

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

### 3.1 Fluxo fixo × agente que decide o próprio caminho (Q1) — **ADOTAR fluxo fixo na Fase 1; REJEITAR orquestrador que replaneja por modelo**
A prática separa dois tipos: "When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks," e "Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage," (SRC-ANTH-AGENTS-01). O SOT já decidiu de que lado a Fase 1 fica: ADR-MANAGER-001 §2.5 ("Mecânico/determinístico … sem julgamento analítico") e WF-K02/WF-A02/WF-F02 ("gate não-LLM — ENF-03"). **ADOTAR:** a Fase 1 é fluxo de caminho fixo — Classe D em toda decisão de ordem, tempo, teto e transição. **REJEITAR** o padrão em que o orquestrador "self-reflects" e replaneja: "At each step of its plan, the Orchestrator creates a Progress Ledger where it self-reflects on task progress" (SRC-MAGONE-01) — isso poria julgamento de modelo dentro do despacho, contra o ADR. **ADAPTAR** só a ideia de "If the Orchestrator finds that progress is not being made for enough steps, it can update the Task Ledger" (SRC-MAGONE-01) como **contador determinístico de passos sem progresso** que encerra ou escala o ciclo (§3.5). Julgamento leve (tipo de missão; arbitragem) fica nas Fases 0/2 (SPEC-015/014). `[PROPOSTA]`

### 3.2 Despacho por grafo de dependências (Q2) — **ADOTAR "ordem ≠ conteúdo" e "sem ciclo"; ADAPTAR a ordem à hierarquia e à condição**
"The Dag itself doesn’t care about what is happening inside the tasks; it is merely concerned with how to execute them" (SRC-AIRFLOW-DAG-01) — é o mesmo princípio da RULE-BB-005 (o orquestrador só coordena). "The canonical application of topological sorting is in scheduling a sequence of jobs or tasks based on their dependencies." e "A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic" (SRC-TOPO-01). **ADOTAR:** (1) grafo de despacho declarado como **dado versionado**, recusado se tiver ciclo; (2) ordem derivada das dependências; (3) desempate por regra fixa. **ADAPTAR:** no SOT a ordem entre escolas **não** é livre — é a hierarquia constitucional (INV-01/CC-01) e o pipeline WF-02→WF-03→WF-04→WF-05; e há **arestas condicionais** (Institucional só se o Estrutural apontar oportunidade — WF-03; Operacional só com alarme disparado dentro da Killzone — WF-05/WF-A02). Isso é a "ativação progressiva" do slot: o próximo agente só acorda se a condição anterior for satisfeita. **Mapa nível a nível de INV-01 (R1-M01):** Elliott → nó Estrutural (WF-02); **Fibonacci → sem nó** no pipeline do WORKFLOW; **Fractal → sem nó**; SMC → nó Institucional (WF-03); ICT → nó Operacional (WF-05). `[FONTE]` ROADMAP §8 tem o slot **SPEC-011 — Fibonacci & Fractal Confluence Harness** ("dependência da hipótese estrutural"); AGENTS.md §3.2 lista o **Fibonacci Validator** entre os Agentes de Trading e §6.2 diz que "SMC/Fibonacci criam sub-hipóteses com `parent_id`"; WF-V02 cita Fibonacci "só em confluência"; a MATRIZ (não-normativa) põe a SPEC-011 como coadjuvante de WF-03. Nenhuma fonte diz se o Fibonacci/Fractal é **etapa despachada pelo Manager** ou **parte interna do Estrutural**. Lacuna WORKFLOW × hierarquia registrada (§6 CF-8) e levada a Andraus (ABERTURA P-11); o grafo como **dado versionado** acomoda qualquer das respostas sem reescrever a Spec. `[INFERÊNCIA]` *[antes: o parágrafo terminava em "…se a condição anterior for satisfeita." sem mapear Fibonacci/Fractal]* **Despacho síncrono por etapa** é o que a prática relata hoje: "Currently, our lead agents execute subagents synchronously, waiting for each set of subagents to complete before proceeding." (SRC-ANTH-MULTI-01) — **ADOTAR** para o ciclo de um ativo (cada etapa espera a publicação da anterior no quadro); paralelismo só **entre** ativos/missões (WF-P01), cada um com seu ciclo isolado. `[PROPOSTA]`

### 3.3 Máquinas de estados verificáveis (Q3) — **ADAPTAR (tabela de transições fechada); REJEITAR a notação**
"SCXML provides a generic state-machine based execution environment based on CCXML and Harel State Tables." (SRC-SCXML-01); o padrão trata estados finais explicitamente ("When a state machine enters a <final> substate of a compound state, the parent state remains active, but the event"). **ADAPTAR:** as duas FSMs **já decididas por Andraus** — alarme (WF-A02: `IDLE → ARMED → TRIGGERED → {CONSUMED | EXPIRED | CANCELLED}`) e ciclo (WF-F02: `AGUARDANDO → … → {SINAL_ENVIADO | RECUSADO | EXPIRADO}`) — escritas como **tabela fechada** (estado × evento → próximo estado; par não listado = recusado e registrado), estados finais sem saída, e os seis ramos de falha (WF-F01) como transições nomeadas **onde mapeiam em transição listada** (ver conferência abaixo). **REJEITAR** adotar SCXML/statecharts como formato (BUILD; ROADMAP §22). **Não** se cria estado novo nem se renomeia estado do WORKFLOW (soberano). **Conferência dos ramos contra as FSMs (R1-M05):** WF-F01 ramos 3 ("sem confirmação operacional → reset do alarme") e 5 ("alarme expirado → reset") falam em **"reset"**, mas a FSM fechada WF-A02 (`IDLE → ARMED → TRIGGERED → {CONSUMED | EXPIRED | CANCELLED}`) **não tem transição de volta** de um estado final, e a WF-F02 é sequência sem aresta de retorno (`ATIVADO → ARMADO` não está escrita). "Reset" não mapeia para nenhuma transição listada ⇒ **ambiguidade do WORKFLOW**, registrada (§6 CF-7) e levada a Andraus (ABERTURA P-12). Também não está escrito para qual estado final de WF-F02 vão os ramos 1 e 2 (`RECUSADO` ou `EXPIRADO`) — incluído na mesma pergunta. Nenhum estado nem transição é criado aqui. `[INFERÊNCIA]`

### 3.4 Ciclo que sobrevive a queda (Q4) — **ADAPTAR (retomar do registro; tempo como fato registrado); ADIAR o mecanismo à SPEC-009**
"Temporal Workflows are resilient. They can run—and keep running—for years, even if the underlying infrastructure fails." e "If those values changed, the Workflow could take a different path and fail to match the recorded history." (SRC-TEMPORAL-01); "When errors occur, we can't just restart from the beginning: restarts are expensive and frustrating for users." (SRC-ANTH-MULTI-01). **ADAPTAR:** (1) toda transição de ciclo e de alarme gravada em **registro só-inserção** (INV-07) antes de produzir efeito; (2) o instante usado em cada decisão de tempo entra **como fato registrado** — a reexecução lê o registro, não o relógio; (3) após reinício, o ciclo retoma do último estado registrado; alarme cujo prazo venceu durante a queda vai a `EXPIRED` (nunca dispara atrasado). **ADIAR:** esquema e mecanismo de persistência = SPEC-009 (**G-001 ABERTA**). **Lacuna de ordem:** a SPEC-009 vem **depois** da SPEC-008 no caminho crítico — a SPEC-008 declara o requisito; quem o satisfaz é a SPEC-009 (P-6). `[PROPOSTA]`

### 3.5 Orçamento, tetos e parada (Q5) — **ADAPTAR teto com estado explícito; REJEITAR corte por custo de etapa obrigatória**
A prática usa teto que, ao estourar, gera estado explícito: "If we exceed the `max_turns` passed, we raise a MaxTurnsExceeded exception. Pass `max_turns=None` to disable this turn limit." (SRC-OAI-MAXTURNS-01); "The recursion limit caps how many super-steps one run may execute. When the limit is exceeded, LangGraph raises" (SRC-LGRAPH-RECUR-01); para falhas repetidas, "Once the failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit breaker return" (SRC-CB-01); e regra de esforço escrita: "Agents struggle to judge appropriate effort for different tasks, so we embedded scaling rules in the prompts." (SRC-ANTH-MULTI-01). **ADAPTAR:** (1) teto de passos por ciclo, teto de voltas por agente (o laço interno de cada agente H/P é dele — RULE-MECH-03 — mas o **teto** que ele recebe vem do Manager, como a SPEC-007/048 já pediram para `max_retrieval_rounds`), teto de falhas seguidas por agente/ferramenta; estouro ⇒ estado nomeado + registro + aviso, nunca silêncio; (2) "profundidade" por **tabela fixa** (tipo de missão × etapa → teto), não por julgamento do modelo; (3) valores = **parâmetros INDETERMINADOS** (CC-09; sem número inventado). **REJEITAR:** a opção de desligar o teto (`max_turns=None`) — laço sem teto é proibido (RULE-MECH-03); e qualquer corte **por custo** de etapa com evento estruturalmente relevante (CEE-001 §10 S2) — o orçamento **avisa e escala**, não pula o Estrutural. **ADOTAR** a Inversão #1 (CONFLICT-MAP): ruptura de hipótese dominante ⇒ análise completa independente do custo — disparada por **evento publicado** (transição `DOMINANT → REFUTED` ou `DOMINANT → SUPERSEDED` da hipótese, CHM-001 l.753-754, publicada no quadro e avisada pelo barramento), nunca por julgamento do Manager (ABERTURA S4; lacuna L-8 se o evento não existir). *[antes: "…ruptura de hipótese dominante ⇒ análise completa independente do custo." sem fonte de evento — R1-m05]* **Custo nunca entra no Conviction Vector** (INV-04): o orçamento vive em espaço próprio. A tensão "kill-switch por custo" (CEE-001 §9.3) × S2 vai a Andraus (P-7). `[PROPOSTA]`

### 3.6 Relógio, fuso e horário de verão (Q6) — **ADOTAR banco IANA e relógio de NY (já FATO NORMATIVO); ADAPTAR "UTC no registro"**
"The zoneinfo module provides a concrete time zone implementation to support the IANA time zone database as originally specified in PEP 615." e a regra da hora ambígua: "During offset transitions which induce ambiguous times (such as a daylight saving time to standard time transition), the offset from before the transition is used when fold=0, and the offset after the transition is used when fold=1, for example:" (SRC-ZONEINFO-01). "Support for time zones is enabled by default. Airflow stores datetime information in UTC internally and in the database." e "Time zone aware Dags that use cron schedules respect daylight savings time. For example, a Dag with a start date" (SRC-AIRFLOW-TZ-01). **ADOTAR** (confirma WF-K01/WF-K03, não cria): janela calculada em `America/New_York` pelo banco de fusos; o fuso da máquina só para exibir e agendar. **ADAPTAR:** instantes gravados em referência única (UTC) no registro; a janela local se desloca contra o UTC na troca de horário — comportamento **correto**. **Casos de teste obrigatórios** (D7/D8): hora inexistente (ida do horário de verão), hora ambígua (volta), janela que cruza meia-noite (Asian 20:00–24:00), máquina em fuso diferente do de NY, relógio da máquina adiantado/atrasado. Fonte de tempo confiável e tolerância de desvio = **INDETERMINADO** (BUILD; P-9). `[PROPOSTA]`

### 3.7 Escola ICT — Killzone (Q7, lente 2) — **ADOTAR o relógio de NY; ADIAR os horários a Andraus (BL-026)**
As fontes confirmam o relógio de NY e a maior parte da tabela padrão: "London open 2:00–5:00 am, New York AM 7:00–10:00 am, London close 10:00 am–12:00 pm, and New York PM 1:30–4:00 pm." (SRC-KZ-LUX-01) — igual a WF-R02. **Divergem** em duas janelas: asiática — "The standard set, conventionally quoted in New York time, is the Asian killzone (roughly 8:00–10:00 pm)," (SRC-KZ-LUX-01) × WF-R02 20:00–24:00; NY AM — "the Asian session (20:00-00:00 ET), the London session (02:00-05:00 ET), the New York morning session (08:30-11:00 ET)" (SRC-KZ-BTX-01) × WF-R02 07:00–10:00. E há quem publique em UTC fixo: "the Asia kill zone (01:00-05:00 UTC), the London kill zone (07:00-10:00 UTC), the New York AM kill zone" (SRC-KZ-BTX-01) — tabela que **se desloca** contra NY na troca de horário, o que confirma WF-K01. **ADOTAR:** WF-K01 (relógio de NY). **ADIAR:** os valores são **parâmetros editáveis por Andraus** (WF-R02/R03, `[REVISAR · BL-026]`) — esta abertura recoloca a pauta (P-10), sem escolher horário. Convenções de varejo, sem autoridade de mercado (Opinião/Prática). Nenhum horário vira constante. `[PROPOSTA]`

### 3.8 Risco-retorno — **não se aplica à Fase 1**
R:R ≥ 1:3, sizing e avaliação de risco são do Risk Agent (WF-07, WF-X01..X05; FASE RISK) e o pacote risco-retorno é da Fase 2 (WF-06). A Fase 1 **não** calcula nem filtra por R:R. Lente "risco-retorno" registrada como **não pertinente** ao componente (RULE-ECC-05 pede a escola "pertinente"). `[INFERÊNCIA]`

---

## 4. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Régua: licença aberta conhecida; ≥300 estrelas; último commit ≤12 meses antes do acesso; não arquivado; 0 alerta grave público aberto; dono identificável. Uma captura por repositório em `sources/REPO-*.txt`. Conteúdo de repositório = **DADO**; **nada instalado/executado**.

| Repositório | Estrelas | Licença | Último commit | Veredito | Uso no SOT |
|---|---|---|---|---|---|
| https://github.com/langchain-ai/langgraph | 44600 | MIT | 2026-11-06 | **ELEGÍVEL** | Referência — grafo de estados com teto de passos e estado salvo para retomar; não é dependência. |
| https://github.com/temporalio/temporal | 24200 | MIT | 2026-11-06 | **ELEGÍVEL** | Referência — execução durável, temporizador registrado como evento, reexecução determinística; não é dependência. |
| https://github.com/apache/airflow | 47400 | Apache-2.0 | 2026-11-07 | **ELEGÍVEL** | Referência — grafo acíclico de tarefas; agenda ciente de fuso; UTC interno; não é dependência. |
| https://github.com/statelyai/xstate | 30400 | MIT | 2026-11-03 | **ELEGÍVEL** | Referência — máquina de estados com transições e eventos explícitos; não é dependência. |
| https://github.com/pytransitions/transitions | 6600 | MIT | 2025-09-09 | **NÃO ELEGÍVEL** (commit > 12 meses: 424 dias) | Registrado e descartado — nada aproveitado do repositório. |

Resultado: **4 repositórios elegíveis** (referência; **nenhum** escolhido como motor — BUILD); **1 não elegível** registrado. Comando a rodar pelo Orquestrador: `python scripts/check_repo_research.py specs/features/SPEC-008` e `--all`.

---

## 5. Pesquisa Multi-Lente (RULE-ECC-05) — **incide** (toca o Manager)

| Lente | Onde | Resultado |
|---|---|---|
| 1. Arquitetura | §3.1–§3.6 | Fluxo fixo; grafo sem ciclo; FSM fechada; execução durável; tetos explícitos; relógio IANA. |
| 2. Escola | §3.7 (ICT — Killzone); hierarquia de escolas = INV-01 (norma interna, não pesquisa); §3.8 (risco-retorno não pertinente) | Relógio de NY confirmado; horários divergentes vão a Andraus (BL-026). |
| 3. `WORKFLOW.md` v2.1 | tabela abaixo (refeita após a proposta de divisão — R1-M03) | Conformidade item a item; 5 pontos de dono a confirmar (CONF-1..CONF-5 da ABERTURA) e 2 ambiguidades/lacunas (CF-7 reset; CF-8 Fibonacci/Fractal); WF-D03 **não** tocada. *[antes: "4 pontos de dono a confirmar (C-1..C-4 da ABERTURA)"]* |

**Confronto e conformidade com o `WORKFLOW.md` (citação só por ID):**

| ID | O que diz (resumo) | Como a SPEC-008 se conforma | Observação |
|---|---|---|---|
| WF-01 | Pré-condição: TF + tipo; missão assistida/pré-programada | **Consome** como pedido de ciclo; não decide tipo de missão (Fase 0 = SPEC-015) | Interface com SPEC-015 (ABERTURA §2) |
| WF-02 / WF-03 | Estrutural; Institucional **condicional** | Despacho em ordem; Institucional só se o Estrutural apontar oportunidade (aresta condicional) | "oportunidade" = campo publicado pelo agente, não julgamento do Manager (`[INFERÊNCIA]`; P-8). **Fibonacci/Fractal (INV-01) sem passo no pipeline** → CF-8 / P-11 |
| WF-04 | Manager forma convicção macro; se conclusiva, registra alarme | Invoca a leitura macro (RULE-CF-010) e aplica **gate D** "conclusiva?" com limiar **parâmetro** | Limiar macro **não existe** em norma → P-5 (adiar; J-001/N-001) |
| WF-05 | Operacional (ICT) só após alarme na Killzone; TF de entrada ≠ TF de contexto | Despacha o Operacional só em `TRIGGERED` dentro da janela | ICT não cria hipótese (INV-02) |
| WF-K01..K03 | Killzones ICT no relógio de NY; pré-aviso 1h antes; fuso da máquina só exibe | Serviço de tempo determinístico (na Spec de Tempo, se a divisão for aceita) | Valores em WF-R02/R03 (BL-026). **WF-K02 nomeia o dono por número: "Dono do abrir/fechar = Manager/Scheduler (SPEC-008/015)"** — com a divisão, abrir/fechar vai à Spec de Tempo ⇒ divergência de número (o ator continua o Manager) → CF-6 / CONF-5 (Andraus) |
| WF-K04 | Missão pré-programada; ciclo sozinho até o Signal Package; fila para revisão | Conduz a Fase 1 sem checkpoint humano; para na fronteira da Fase 2 | Premissa WF-J01 (HITL adiado) |
| WF-T01 / WF-T02 | Tabela de TFs editável; alinhamento obrigatório | Consome TFs do pedido; **dono do teste de alinhamento** a confirmar (CONF-4 da ABERTURA) | WF-R01: reconciliar M5 × tabela (BL-026). MATRIZ (não-normativa) põe WF-T02 na SPEC-013 — ver CONF-4 |
| WF-A01..A03 | Objeto, FSM e morte do alarme | Proposta de dono = SPEC-008 (ou a peça de tempo — ABERTURA §3) | Campos do alarme vêm da hipótese, não do Manager (P-8). "Reset" de WF-F01 não mapeia em WF-A02 → CF-7 / P-12 |
| WF-F01 / WF-F02 | Seis ramos de falha; FSM do ciclo — "implementação no Plan do Manager (SPEC-015)" | Proposta: **dono por transição** (ABERTURA §2, tabela WF-F02): SPEC-008 até `EM_SÍNTESE`; SPEC-014 a partir dela; RISK-SPEC em `EM_RISCO` | **Conflito de dono com três lados** (WF-F02 "SPEC-015" × ROADMAP §7/DHR-EUA-E23 "SPEC-008" × EUA-E23 PROPOSTA l.115 "SPEC-014") → CF-1 / CONF-1 (Andraus) *[antes: "Proposta: FSM do ciclo **conduzida** pela SPEC-008 · Conflito de dono WF-F02 × ROADMAP §7/DHR-EUA-E23 → C-1 (Andraus)" — R1-M04]* |
| WF-P01 / WF-P02 | Ativos em paralelo; parâmetros por ativo | Um ciclo por ativo/missão, isolados; parâmetros por ativo versionados | Heat/correlação = RISK-SPEC (fora) |
| WF-C01 | Um vetor, duas leituras; 2x por ciclo | Faz a **1ª** invocação (macro) | WF-D03 (fórmula/pesos) **ABERTA** — não tocada |
| WF-X04 | Overtrading é do Bot Trade Finance | Fora | — |
| WF-J01 | Journal/HITL adiado (SPEC-018) | Fora | Premissa de WF-K04 |

**Divergência registrada (não resolvida):** RULE-ICT-003 (`governance/RULES.md`: "Entrada fora de killzone: DEVE reportar convicção operacional reduzida. NÃO DEVE bloquear execução se outros layers pontuarem alto o suficiente.") × WF-A02 ("Disparo só válido dentro da Killzone") e WF-05. Pelo WORKFLOW (soberano — DHR-WF-001) o Operacional só é despachado com alarme dentro da janela; a regra de 2026-09 descreve outro caminho. Divergência = achado a Andraus (CONF-3 da ABERTURA; §6 CF-3); a SPEC-008 se conforma ao WORKFLOW e **não** reescreve a RULE. *[antes: "(C-3 da ABERTURA)"]*

**Lente 3 refeita após a divisão (R1-M03) — busca por número de Spec (Grep, 2026-11-07):**
- `WORKFLOW.md`: "SPEC-008" aparece em **WF-K02** ("Dono do abrir/fechar = Manager/Scheduler (SPEC-008/015)") e em **WF-C01** ("A invocação 2x é do Manager (SPEC-008 Fase 1 / SPEC-014 Fase 2)"); "SPEC-015" aparece em **WF-K02** e em **WF-F02** ("implementação no Plan do Manager (SPEC-015)"). Com a divisão: WF-C01 **fica** na SPEC-008 (invocação macro); WF-K02 passa à Spec de Tempo → **CF-6**; WF-F02 já era conflito → **CF-1**.
- `docs/MATRIZ-WORKFLOW-SPEC.md` (**NÃO-NORMATIVA, regenerável** — cabeçalho da própria matriz): põe "SPEC-008 (Scheduler)" como dona de WF-K01, WF-K02, WF-K03, WF-A02, WF-A03, WF-R02, WF-R03, e "SPEC-008/SPEC-015" de WF-A01, WF-D01, WF-D02; põe a **SPEC-015** como dona de WF-04, WF-F01 e WF-F02 (SPEC-008 coadjuvante) e a **SPEC-013** de WF-T02. Com a divisão, as linhas WF-K01..K03, WF-A01..A03, WF-R02/R03 e WF-D01/D02 passariam à Spec de Tempo; WF-04/WF-F01/WF-F02/WF-T02 já divergem da proposta (CONF-1/CONF-2/CONF-4). A matriz **não** é editada pelo Especificador: é regenerada pelo Orquestrador após a homologação (ABERTURA §12).

---

## 6. Lacunas, conflitos e INDETERMINADOS (RULE-MET-01 / RULE-MET-02)

| # | Item | Estado | Encaminhamento |
|---|---|---|---|
| L-1 | "Manager Contract" (pai RULE-HV) não existe | Lacuna | P-4 |
| L-2 | Limiar da convicção macro "conclusiva" (WF-04) sem valor em norma; os limiares-piloto (≥70%, 7/9) são de **sinal** | INDETERMINADO — não inventar | P-5 (adiar a J-001/N-001; gate D com parâmetro; INDETERMINADO ⇒ não arma) |
| L-3 | Persistência do estado do ciclo/alarme (G-001 ABERTA; SPEC-009 vem depois) | Lacuna de ordem | P-6 |
| L-4 | Estados de objeto não-hipótese no quadro (M-001 ABERTA) — pedido de despacho/alarme publicados no quadro? | Aberta | P-6: estados de FSM ficam no registro da SPEC-008, **não** como estado de objeto do quadro |
| L-5 | Fonte do preço que dispara o alarme (Observação de Skill/provedor; BL-033 Market Data não aberta) | INDETERMINADO | Requisito de interface; provedor = Market Data/SPEC-038 (DHR-DEC-004) |
| L-6 | Calendário de pregão/feriado (NASDAQ futuro com pausa diária; XAU; BTC 24/7) — pesquisa inconclusiva | INDETERMINADO | Parâmetro por ativo (WF-P02/N-001); P-9 |
| L-7 | Valores de tetos/orçamento (passos, voltas, tempo por etapa, prazo do alarme) | INDETERMINADO | Parâmetros a calibrar; nunca número inventado (CC-09) |
| L-8 | Evento publicado que dispara a Inversão #1: leitura proposta = transição `DOMINANT → REFUTED`/`DOMINANT → SUPERSEDED` (CHM-001 l.753-754) publicada no quadro (SPEC-004) e avisada pelo barramento (SPEC-005); nome exato do evento não conferido nesta abertura | `[INFERÊNCIA]` — a conferir no Plan | Se não houver evento publicado, a Inversão #1 não é cumprível por regra fixa ⇒ volta a Andraus (ABERTURA S4) |
| CF-1 | Dono da FSM do ciclo — **três lados**: WF-F02 diz "Plan do Manager (SPEC-015)"; ROADMAP §7 e DHR-EUA-E23 §2 põem "FSM do ciclo" na SPEC-008; EUA-E23 PROPOSTA (l.113 e l.115) lista WF-F02 **também** sob a SPEC-014. A fronteira SPEC-008×SPEC-014 corta a FSM em `EM_SÍNTESE` | Conflito documental | Proposta: dono **por transição** (ABERTURA §2, tabela WF-F02); Andraus decide (CONF-1); WORKFLOW só Andraus edita. *[antes: "C-1 \| Dono da FSM do ciclo: WF-F02 diz 'Plan do Manager (SPEC-015)'; ROADMAP §7 e DHR-EUA-E23 põem 'FSM do ciclo' na SPEC-008 \| Conflito documental \| Andraus (C-1 da ABERTURA)…" — R1-M04/R1-m02]* |
| CF-2 | Dono da invocação macro: RULE-CF-010 "SPEC-008 Fase 1"; EUA-E23 §4 lista WF-04 entre os tocados pela SPEC-014 | Conflito documental leve | Proposta: invocação + gate D na SPEC-008; arbitragem na SPEC-014 (CONF-2) *[antes: C-2]* |
| CF-3 | RULE-ICT-003 × WF-A02/WF-05 | Divergência | Andraus (§5; CONF-3) *[antes: C-3]* |
| CF-4 | CEE-001 §9.3 (kill-switch por custo) × §10 S2 (nunca suprimir por custo com evento relevante) | Tensão no canon | P-7 (não reescrever canon — CONST-01) *[antes: C-4]* |
| CF-5 | SPEC-023 "Cognitive Orchestrator" (slot) × ADR-MANAGER-001 §2.2 ("único componente de orquestração") | Possível dupla posse futura | Registrado; não tratado aqui (fora; quando SPEC-023 abrir) *[antes: C-5]* |
| CF-6 | WF-K02 nomeia o dono do abrir/fechar da Killzone por número ("Manager/Scheduler (SPEC-008/015)"); a divisão proposta (ABERTURA §3) põe abrir/fechar na Spec de Tempo. O **ator** segue o Manager (ADR §2.2); muda só o documento | Conflito documental (criado pela proposta de divisão) | Andraus (CONF-5); WORKFLOW só Andraus edita; MATRIZ regenerada pelo Orquestrador |
| CF-7 | "Reset do alarme" (WF-F01 ramos 3 e 5) sem transição correspondente na FSM fechada WF-A02 (nem aresta de volta em WF-F02); destino final dos ramos 1 e 2 em WF-F02 não escrito | Ambiguidade do WORKFLOW | Andraus (P-12); nenhum estado novo criado |
| CF-8 | Hierarquia INV-01 (Elliott → **Fibonacci → Fractal** → SMC → ICT) × pipeline WF-02..WF-05 (só Estrutural, Institucional, Operacional): Fibonacci/Fractal (slot SPEC-011) sem posição no despacho | Lacuna WORKFLOW × hierarquia | Andraus (P-11) |

**Prefixos de ID (R1-m02):** neste Dossiê `L-n` = lacuna e `CF-n` = conflito/divergência; na ABERTURA `P-n` = pergunta e `CONF-n` = confirmação a Andraus. Até a R1 os conflitos daqui e as confirmações da ABERTURA usavam ambos `C-n` (homônimos, sentidos diferentes).

**Nada disto é fechado pela pesquisa** (CONS-01). Abertas tocadas: J-001, N-001, G-001, M-001, WF-D03 (só para dizer que não toca), SPEC-015-SCOPE (fronteira com a Fase 0), C-001 (redação EARS). Não tocadas: K-001, SPEC-045-RUNTIME-001, ECC-03-001.

---

## 7. Cobertura × lacuna × dono

| Capacidade do slot (ROADMAP §7) | Coberta pela proposta? | Dono proposto |
|---|---|---|
| quem pensa; em que ordem; quais despertar | Sim — grafo de despacho + arestas condicionais | SPEC-008 |
| quando; relógio/Killzone | Sim | SPEC-008 **ou** peça de tempo (ABERTURA §3, P-2); com divisão, WF-K02 diverge no número (CF-6) |
| por que | Sim — cada despacho registra a regra e o evento que o causaram (D9) | SPEC-008 |
| com qual profundidade / orçamento | Sim — tabela fixa de tetos (valores INDETERMINADOS) | SPEC-008 |
| quando interromper/aguardar/escalar/encerrar | Sim — estados e ramos WF-F01; escalada a Andraus registrada | SPEC-008 |
| ativação progressiva/lazy | Sim — arestas condicionais; Inversão #1 | SPEC-008 |
| alarme FSM | Sim | SPEC-008 **ou** peça de tempo (P-2) |
| FSM do ciclo | Sim, até `EM_SÍNTESE`, condicionado a CF-1/CONF-1 | SPEC-008 até `EM_SÍNTESE`; SPEC-014 e RISK-SPEC depois (proposta por transição) *[antes: "Sim, condicionado a C-1 \| SPEC-008 (proposta)"]* |
| ordem pela hierarquia completa (INV-01) | Parcial — Fibonacci/Fractal sem posição | Andraus (P-11; CF-8) |
| Skills despertar/não despertar | Parcial — só como nós do grafo; formalização de Skill = SPEC-025 (I-001 fechada; corte exato adiado) | SPEC-025 |
| estado persistente | Não — requisito à SPEC-009 | SPEC-009 (G-001) |
| tipo de missão, portfólio, Plano B | Não | SPEC-015 |
| arbitragem, convicção global, TMP | Não | SPEC-014 / SPEC-016 |

---

## 8. Escopo, quantidade, decomposição e re-apontamento

### 8.1 Peso
O slot pede CRITICAL D0–D8. A parte de **despacho e ciclo** tem os casos em que D8 adversarial rende: concorrência entre ativos, aviso duplicado ou fora de ordem do barramento, reinício no meio do ciclo, tentativa de pular etapa por custo, alarme disparando fora da janela. **Recomendo manter CRITICAL D0–D8 nela.** A parte de **relógio e alarme** é função pura de tempo, sem efeito externo e sem modelo; os casos difíceis (horário de verão, meia-noite, prazo vencido na queda) cabem como cenários negativos de D7. **Recomendo HIGH D0–D7** se for peça separada (alternativa: CRITICAL). Decisão de Andraus (P-1/P-2).

### 8.2 Quantidade e dimensionamento (RULE-ECC-07)
BASpecs candidatas: ~19–20 (lista na ABERTURA §3). Estimativa em Spec única **passa do teto de 2.000 linhas** na conta central (≈2.499) e na densidade alta (≈3.220); na densidade baixa (≈1.900) **atinge** o alerta de 1.900 (derivação na ABERTURA §3) ⇒ *[antes: "na conta central (≈2.547)… na densidade baixa (≈1.900) encosta no alerta" — central refeita sem a errata, que não existe sem divisão (R1-m04)]* a RULE-ECC-07 **exige** propor a divisão a Andraus **antes do Plan**, por fronteira de contrato. Proposta: **duas Specs** — (1) **SPEC-008 — Manager — Despacho e Ciclo (Fase 1)**; (2) **slot novo "Manager — Relógio, Killzone e Alarme-gatilho"** (número proposto **SPEC-050**, o próximo livre — a decidir por Andraus). Alternativas registradas: Spec única (acima do teto — só se Andraus decidir assim, ciente da RULE-ECC-07); três peças (sobrecusto fixo triplicado). Na ABERTURA a segunda peça é chamada "Spec de Tempo" até Andraus decidir o número.

### 8.3 Re-apontamento em Specs baselined (atomic-spec §15 item 6)
- **Sem divisão:** nenhuma errata — todas as referências já apontam à SPEC-008.
- **Com a divisão proposta:** as referências a **Killzone/alarme** passam à peça de tempo por **nota aditiva de re-apontamento** (padrão ERRATUM-REAPONT-001), sem reescrever a SPEC-003 (INV-09). Referências a **invocação macro/orquestração/orçamento/latência** (SPEC-003 invocação; SPEC-004/005/007/048) **ficam** na SPEC-008. *[antes: "…`SPEC-003/plan.md` l.46 e l.224 ('Manager/Scheduler (SPEC-008…') — nota aditiva… Lista exata a reconferir por Grep no Plan." — lista por amostra, R1-M02]*

**Varredura exaustiva (R1-M02)** — Grep de `SPEC-008|SPEC-015|Scheduler` em `specs/features/SPEC-003/{plan,research,checks}.md`, 2026-11-07. Disposição: **RE** = re-apontar Killzone/alarme à Spec de Tempo pela nota (se a divisão for aceita); **FICA** = continua certo (invocação macro da SPEC-008, nome de decisão aberta, ou sem número de Spec); **HIST** = histórico de versão/rodada — nunca editado (INV-07), a nota o cita para leitura correta.

| Arquivo:linha | Assunto | Disposição |
|---|---|---|
| plan.md:28 | changelog v1.5 — "SPEC-015-SCOPE" (decisão aberta) | FICA |
| plan.md:29 | changelog v1.4 — "SPEC-015-SCOPE" | FICA |
| plan.md:30 | changelog v1.3 — invocação "Manager Fase 1 (SPEC-008)" | HIST (e invocação: FICA) |
| plan.md:33 | changelog v1.1 — Killzone/alarme/ICT "Manager/Scheduler — SPEC-008/015" | HIST |
| plan.md:46 | Nota de gate — Killzone/alarme/ICT "(Manager/Scheduler SPEC-008/015…)" **e** invocação "(SPEC-008/014)" | RE (parte Killzone/alarme); FICA (invocação) |
| plan.md:98 | bloco de conformidade WF — "WF-D01/D02/D04 … Manager/Scheduler SPEC-008/015" | RE |
| plan.md:164 | WF-C01 — invocação "Manager (SPEC-008/014)" | FICA |
| plan.md:173 | "Manager/Scheduler e agentes" (sem número) | FICA |
| plan.md:181 | Fase 2 "SPEC-014/SPEC-015"; "fronteira SPEC-008×SPEC-015" (EUA-E23) | FICA |
| plan.md:190 | Non-goal — invocação "(SPEC-008 Fase 1 / SPEC-014 Fase 2)" | FICA |
| plan.md:191 | Non-goal — Killzone/alarme/ICT "Manager/Scheduler (SPEC-008/015)" | RE |
| plan.md:208 | S5 — invocação | FICA |
| plan.md:224 | tabela de fronteira — Killzone/alarme/ICT "Manager/Scheduler (SPEC-008/015)" | RE |
| plan.md:225 | tabela de fronteira — invocação "(SPEC-008/014)" | FICA |
| plan.md:299 | RULE-CF-010 — invocação | FICA |
| plan.md:568 | BASpec CF-010 — "consumidor (Manager/Scheduler)" (sem número) | FICA |
| plan.md:572 | BASpec CF-010 — invocação | FICA |
| plan.md:718 | invocação | FICA |
| plan.md:884 | ADV — invocação "(SPEC-008/014)" | FICA |
| plan.md:1104 | §7-bis CF-010 — invocação | FICA |
| plan.md:1147 | etiquetagem — invocação | FICA |
| plan.md:1149 | etiquetagem — Killzone/alarme/ICT "Manager/Scheduler SPEC-008/015" | RE |
| plan.md:1190 | lista final — "Manager/Scheduler" (sem número), invocação | FICA |
| research.md:129 | Killzone e alarme "(Manager/Scheduler — SPEC-008/015)" | RE |
| research.md:183 | Killzone, alarme, 1x/2x, ICT "(Manager/Scheduler — SPEC-008/015)" | RE (parte Killzone/alarme) |
| research.md:204 | "Manager/Scheduler" (sem número), invocação | FICA |
| research.md:245 | "Manager/Scheduler" (sem número), invocação — pergunta histórica Q-A5 | FICA |
| research.md:260 | invocação "(SPEC-008 Fase 1 / SPEC-014 Fase 2)" | FICA |
| research.md:300 | WF-D01 Killzone "Manager/Scheduler (SPEC-008/015)" | RE |
| research.md:301 | WF-D02 alarme "Manager (SPEC-008/015)" | RE |
| research.md:331 | gatilho de BL-026 "`spec:SPEC-008 em redação`" (citação do RMR-001) | FICA (o gatilho é re-apontado no RMR-001, não aqui) |
| research.md:347 | "SPEC-015-SCOPE" | FICA |
| checks.md:17 | "SPEC-015-SCOPE" | FICA |
| checks.md:32 | "SPEC-015-SCOPE" | FICA |
| checks.md:40 | rodada — invocação "Manager Fase 1 (SPEC-008)" | HIST (e invocação: FICA) |
| checks.md:54 | rodada — "Unificação do Manager (SPEC-008×SPEC-015)" | HIST |
| checks.md:63 | rodada — WF-D01/D02/D04 "Manager/Scheduler SPEC-008/015" | HIST |

Total: 37 linhas (plan 23 · research 9 · checks 5); **RE = 9** (plan 46, 98, 191, 224, 1149; research 129, 183, 300, 301); HIST = 5 (plan 30, 33; checks 40, 54, 63); FICA = 23. Fora da SPEC-003, a mesma busca casando "SPEC-008" com Killzone/alarme/relógio/WF-K/WF-A achou só referências a **orçamento/latência** (SPEC-048 plan l.342 e l.1131, research l.123 — FICA) e documentos não-Spec (WORKFLOW WF-K02 → CF-6; MATRIZ → regenerada; atas e propostas → registro histórico, não editados).

**Regra de busca proposta para a ata** (padrão DHR-SPEC048-001 Q-7, `[PROPOSTA]`): "a errata re-aponta à Spec de Tempo toda ocorrência de `SPEC-008` (inclusive na forma `SPEC-008/015` ou junto de `Manager/Scheduler`) que esteja **junto de Killzone, alarme/alarme-gatilho, relógio, WF-K0x, WF-A0x, WF-D01 ou WF-D02**, em Spec baselined (`plan.md`/`research.md`/`checks.md`) ou errata homologada; ocorrências junto de invocação/convicção macro, orçamento, latência ou dispatch **ficam**; **tabelas de histórico de versões e registros de rodada não são editados** (INV-07) — a nota os lista como lidos sob a errata." A busca é refeita no momento de escrever a errata (a tabela acima é a foto de 2026-11-07).

### 8.4 Itens do RMR-001 e gatilhos (DHR-BACKLOG-ABERTURA-001) — **o Especificador não promove**
Vinculados por regra: BL-026, BL-043, BL-044, BL-045, BL-046. Disposições propostas na ABERTURA §9. Re-apontamento proposto **só** se a divisão for aceita: gatilho de BL-026 ganha `∨ spec:<número da Spec de Tempo> em redação` (aditivo; Killzone/alarme vão para lá). BL-043..046 (processo dos Construtores) **ficam** no gatilho da SPEC-008, como Andraus mandou ("backlog da próxima Spec").

---

## 9. Incidência de RULE-ECC-05 (Multi-Lente) e de CC-12

- **RULE-ECC-05: incide** (toca o Manager) — três lentes em §5.
- **CC-12 / RULE-PD-01: não incide.** O Manager **não** é Spec de especialidade de escola (ADR-MANAGER-001 §2.5: "Não possui skills de análise técnica"). Nenhum `PD-xx` proposto. A Killzone é parâmetro de tempo consumido, não princípio de escola redigido aqui. `[INFERÊNCIA]` — o Revisor pode contestar.

---

## Sources (fontes `[EXTERNO]` — acesso 2026-11-07; capturas em `sources/`)

- [Building effective agents — Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [How we built our multi-agent research system — Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Magentic-One — Microsoft Research](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/)
- [Dags — Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)
- [Time zones — Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timezone.html)
- [Topological sorting — Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)
- [SCXML — W3C](https://www.w3.org/TR/scxml/)
- [Workflows — Temporal](https://docs.temporal.io/workflows)
- [Running agents — OpenAI Agents SDK](https://openai.github.io/openai-agents-python/running_agents/)
- [Graph API — LangGraph](https://docs.langchain.com/oss/python/langgraph/graph-api)
- [CircuitBreaker — Martin Fowler](https://martinfowler.com/bliki/CircuitBreaker.html)
- [zoneinfo — Python docs](https://docs.python.org/3/library/zoneinfo.html)
- [Killzones — LuxAlgo](https://www.luxalgo.com/library/concept/killzones/)
- [ICT Kill Zone Times — Backtrex](https://backtrex.com/en/blog/ict-kill-zone-times-sessions)
- Repositórios: ver §4.
