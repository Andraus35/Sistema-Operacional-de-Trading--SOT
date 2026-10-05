# Dossiê de Pesquisa — SPEC-005: Cognitive Event Bus (slot ROADMAP §5, FASE 2)

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-SPEC-005 |
| **Método** | ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06) |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 4.8) |
| **Data de acesso web** | 2026-10-04 (todas as fontes `[EXTERNO]`) |
| **Complexidade proposta** | **HIGH** (ROADMAP §5 pina P0 — HIGH; ver §6.1 e ABERTURA §1). Dossiê em profundidade proporcional HIGH (atomic-spec §15). |
| **Validade do Dossiê (ECC-VAL-001 — FECHADA, DHR-DEC-003)** | HIGH → **90 dias** da data de acesso (2026-10-04), ou antes se o contexto mudar materialmente. **Data-limite = 2027-01-02.** Dossiê vencido não dispensa reabrir pesquisa (fail-closed, RULE-ECC-02). |
| **Natureza** | **Dossiê de Pesquisa `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão (CONS-01). |
| **Status epistemológico** | Conteúdo web = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02). Toda fonte etiquetada `[EXTERNO]` e classificada; veracidade das páginas **não** atestada. Capturas verbatim em `sources/` (RULE-ECC-04); limitação em `sources/_LIMITACAO-WEB.txt`. |
| **Autorização** | Caminho crítico — FASE 2; próxima na sequência após a SPEC-004 homologada (ROADMAP §21/§25; DHR-SPEC004-003). Abertura autorizada por Andraus (chat, 2026-10-04: "Abrir SPEC-005 reenquadrada"). |
| **Fronteiras respeitadas** | INV-05 (SOT não executa ordem), INV-06/INV-10 (Evidência≠Observação; CEM-001 idioma canônico), INV-07 (versionamento monotônico), INV-09 (sem baseline informal). Não redefine CHM-001/CEM-001/CCM-001 nem **SPEC-004** (CC-02/CONST-01). Blackboard = SPEC-004 (baselined); Knowledge Graph = SPEC-006; estado persistente por agente (G-001) = SPEC-009. |

> **Aviso de método (RULE-MET-01 — sem bajulação, sem fabricação).** A busca web retornou de novo **IDs arXiv implausíveis/futuros** (ex.: 2607.02448) — **descartados** por não verificáveis (risco de fabricação; `sources/_LIMITACAO-WEB.txt`). Distinguo explicitamente trechos **verbatim via WebFetch** (base de alegações carregadas) de **sumários de WebSearch** (DADO de contexto, não garantidos verbatim). Nenhum padrão externo foi importado automaticamente; cada achado é confrontado com a arquitetura SOT antes de qualquer proposta.

---

## 0. Auditoria de entrada (dado a verificar — resultado da verificação do Especificador)

O orquestrador forneceu uma auditoria documental. **Verifiquei cada âncora no repositório** (resultado abaixo); é `[FONTE]` interna, não baseline nova.

| Âncora da auditoria | Verificação | Resultado |
|---|---|---|
| (a) Origem = ideia de engenharia de software | `docs/fundamentos/KERNEL-V2.md` l.1829-1859 ("Cognitive Event Bus (CEB)… distribuir eventos sem que os módulos fiquem verificando continuamente… reduz uso de CPU na VPS, diminui latência, melhora escalabilidade… 'sistema nervoso'") · `ENGENHARIA-GERAL.md` Doc 13 l.4794-4805 ("Data Contracts & Event Bus… Nenhum agente conversa diretamente com outro. Toda comunicação ocorre através de contratos padronizados publicados no Event Bus") · `AUDITORIA-ideias-nao-implementadas.md` l.2823 ("O Event Bus equivale ao barramento do sistema") | **CONFIRMADO.** Event Bus nasce como **proposta de engenharia** (evolução sugerida, não requisito homologado). `[FONTE]`, status FATO ARQUITETURAL (não baseline). |
| (b) EVENT-BUS-001 órfã | `governance/ADR-MANAGER-001` l.201 ("EVENT-BUS-001 \| Event Bus: existe? Como se distingue do Blackboard? \| Aberta") + l.148/191 (GOV-007 PARCIAL) · `governance/DHR-ADR-HOC003` l.121/145 (lista EVENT-BUS-001 como aberta) · **ausente** das listas de decisões abertas do AGENTS §7 e do ROADMAP §7 | **CONFIRMADO — decisão órfã.** Encaminhamento proposto em §8 (não fecho — CONS-01). |
| (c) Conflito de linhagem | Doc 13 ("tudo via Event Bus") × `governance/RULES.md` l.308 **RULE-BB-001** ("Comunicação entre agentes EXCLUSIVAMENTE via Blackboard Cognitivo") | **CONFIRMADO — tensão real.** Tratada em §3.1/§3.6. WORKFLOW (WF-F02 FSM determinística; WF-02..07; WF-A01..A03; WF-K04) citado só por ID; não contradito; WF-D03 não fechada. |
| (d) Sobreposição com SPEC-004 v1.2 (BASELINE) | `specs/features/SPEC-004/plan.md` entrega log append-only com seq por workspace, replay, expiração, idempotência, `supersedes`/`derived_from`, `schema_version`, identidade autenticada (DHR-SPEC004-002/003) | **CONFIRMADO.** Mapa de cobertura × lacuna em §4. |
| (e) Necessidades reais a preservar | WF-A03 (cancelar alarme quando hipótese→SUPERSEDED/REFUTED) · `canon/CEM-001` l.717-727 (eventos de ciclo de vida da Evidência propagados pela "infraestrutura oficial… EC-COG-005 — Cognitive Event Bus"; "O CEM não define o comportamento interno dessa infraestrutura") · `governance/GPR-001` passo 11 l.456-457 ("Blackboard → Event Bus → Bot Trade Finance") · SPEC-001 EARS 8 (`plan.md` l.159 "emitir evento 'Hypothesis.Created' no Event Bus"; l.367) e l.75 (transporte delegado à SPEC-005; `SAS-001 §6.7`) · `CONSTITUTION.md` l.235 (EC-COG-005) | **CONFIRMADO.** Slot NÃO removido/renumerado (INV-07/CONST-01); reenquadramento só por proposta a Andraus. |

**Conclusão da auditoria:** o slot SPEC-005 é **real e referenciado por baselines/canônicos** (CEM-001, SPEC-001, GPR-001, CONSTITUTION, WORKFLOW implícito). O que está em aberto não é *se* há um mecanismo de propagação de eventos, mas **qual a sua forma** (broker durável completo vs. camada fina de notificação sobre o log já existente da SPEC-004) e **como se distingue do Blackboard** (EVENT-BUS-001).

---

## 1. Questões e estratégia de busca

**Questões (derivadas do título do slot §5 + conflito de linhagem + sobreposição SPEC-004 + EVENT-BUS-001):**
- Q1. Como o estado da arte propaga **notificação de mudança** sobre um **log append-only já existente** sem introduzir um broker durável paralelo (outbox, CDC/log-tailing, change feed, cursor de leitura)?
- Q2. Como o **event sourcing** trata projeções/consumidores reagindo ao log (catch-up subscription, cursor, idempotência) — e isso é compatível com o log append-only da SPEC-004?
- Q3. **Quando um message broker é over-engineering** em processo único / escritor único por workspace (RULE-BB-002)?
- Q4. Como a **arquitetura blackboard** separa o quadro (estado) do componente de **controle/notificação** (transporte de mudanças) — a fronteira SPEC-004 × SPEC-005?
- Q5. Como se **orquestram agentes LLM** sem message broker (estado compartilhado + execução dirigida por grafo/FSM)? É coerente com o WORKFLOW do SOT (FSM WF-F02, agentes invocados por fase)?
- Q6. Que **repositórios seguros e bem avaliados** (RULE-ECC-06) exemplificam essas práticas?

**Estratégia:** WebSearch para mapear o campo (outbox vs CDC; event sourcing/catch-up; broker over-engineering; blackboard+notificação; orquestração LLM sem broker; LISTEN/NOTIFY+cursor); WebFetch para capturar **verbatim** as fontes-base e auditar estaticamente páginas de repositório (stars/licença/arquivado — **nada instalado/executado**). Fontes classificadas `[EXTERNO]`; capturas em `sources/*.txt` (RULE-ECC-04/06).

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Papel |
|---|---|---|---|
| SRC-OUTBOX-01 | microservices.io — Transactional Outbox (Chris Richardson) | **Padrão** | Separar persistência de estado da propagação (Q1) |
| SRC-ES-01 | techinterview.org — Event Sourcing/CQRS, projeções, read models | Prática | Consumidores projetam sobre o log via cursor/catch-up (Q2) |
| SRC-NOTIFY-01 | centrifugal.dev — outbox + CDC + LISTEN/NOTIFY | Prática | Notificação (push) é otimização sobre o log durável (Q1/Q3) |
| SRC-BROKER-01 | milanjovanovic.tech — Modular Monolith Communication | Opinião/Prática | Broker adiciona complexidade; in-process quando basta (Q3) |
| SRC-BB-01 | confluent.io / openlayer.com / arXiv 2507.01701 | Prática + Experimento | Controle notifica agentes; quadro ≠ controle (Q4) |
| SRC-LLM-01 | LangGraph (langchain-ai) docs/README | Prática | Orquestração multiagente por estado compartilhado, sem broker (Q5) |
| REPO-debezium | github.com/debezium/debezium | Prática (repo elegível) | CDC: ler o log e propagar sem polling do produtor (Q1/Q6) |
| REPO-langgraph | github.com/langchain-ai/langgraph | Prática (repo elegível) | Estado compartilhado + grafo determinístico (Q5/Q6) |
| REPO-postgresql-event-sourcing | github.com/eugene-khyst/postgresql-event-sourcing | **NÃO ELEGÍVEL (arquivado)** | Registrado; não adotado (Q2/Q6) |

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

### 3.1 Blackboard × controle/notificação (Q4) — **ADOTAR o enquadramento (confirma a fronteira SPEC-004↔SPEC-005)**
[EXTERNO, SRC-BB-01 — verbatim via WebFetch de openlayer.com, acesso 2026-10-04] *"No agent owns the blackboard or controls execution order. A control component watches for state changes and notifies interested agents, but doesn't direct their actions."* O SOT já separa quadro (SPEC-004, baselined) de controle (Manager — SPEC-008, RULE-BB-005). **Adotar** o enquadramento: a SPEC-005 é a **notificação de mudanças** sobre o quadro, não um segundo armazém de estado — princípio do próprio slot: *"Blackboard guarda estado. Event Bus transporta mudanças."* (ROADMAP §5). **Rejeitar** a leitura de que o Event Bus "dirige" agentes (isso é orquestração = Manager) e a leitura de "assinante autônomo 24/7" (ver §3.5/§7: no SOT os agentes são invocados por fase).

### 3.2 Notificação de mudança sobre log append-only (Q1) — **ADOTAR outbox/change-feed como modelo; a SPEC-004 já é o "outbox"**
[EXTERNO, SRC-OUTBOX-01] *"The solution is for the service that sends the message to first store the message in the database as part of the transaction that updates the business entities. A separate process then sends the messages to the message broker."* **Comparação SOT:** a SPEC-004 **já** persiste o objeto atomicamente no log append-only com `seq` por workspace, `supersedes`/`derived_from` e identidade autenticada — isto é, **o estado já está durável**. **Adotar** o modelo em que a propagação é um *processo separado que lê o log já comprometido*; a SPEC-005 ocupa o papel do "separate process" — **não** precisa reintroduzir durabilidade (o log é a fonte de verdade). `[INFERÊNCIA]` de engenharia: isso favorece **camada fina de notificação com cursor** (Opção A, §ABERTURA) em vez de broker durável paralelo (que duplicaria a durabilidade já garantida pela SPEC-004).

### 3.3 Event sourcing / catch-up subscription / cursor (Q2) — **ADOTAR o modelo de consumidor-com-cursor (reforça SPEC-004)**
[EXTERNO, SRC-ES-01] *"An event store is an append-only log of domain events... the database contains the event log, not the current state rows."* e *"A projection consumes the event stream and builds a read-optimized view... Multiple projections can consume the same event stream for different purposes."* **Comparação SOT:** idêntico ao que a SPEC-004 entrega (replay do log por `seq`). **Adotar:** consumidores (agentes/Skills/Risk/Bot-feedback) reagem ao log via **cursor de leitura** (último `seq` processado) + **idempotência** (chave por evento). Isso dá "notificação de mudança" **sem** armazém novo. **Não fechar** o mecanismo físico (push vs. poll) aqui — é matéria do Plan (D4/D5).

### 3.4 LISTEN/NOTIFY — push é otimização, não fonte de verdade (Q1/Q3) — **ADAPTAR: notificação é best-effort sobre o log durável**
[EXTERNO, SRC-NOTIFY-01] *"When you make database changes, you open a transaction, make the required changes, and write an event into a special outbox table."* e *"Centrifugo supports LISTEN/NOTIFY mechanism of PostgreSQL to be notified about new data in the outbox table."* [DADO não-verificado, dev.to 404] a notificação *"is an optimization rather than a complete alternative to polling"* e *"can drop messages"*. **Comparação SOT:** reforça que o **push de evento é entrega best-effort/otimização**; a **durabilidade e a ordem ficam no log append-only** (SPEC-004, RULE-BB-004/INV-07). **Adaptar:** a SPEC-005 pode especificar notificação push, mas a **reconstrução/recuperação** sempre volta ao cursor sobre o log — fail-safe. Non-goal de garantir durabilidade própria no transporte (seria duplicar a SPEC-004).

### 3.5 Orquestração de agentes LLM sem broker (Q5) — **ADIAR broker completo; alinhar ao WORKFLOW (FSM dirigida pelo Manager)**
[EXTERNO, SRC-LLM-01] LangGraph *"uses a direct state-based approach rather than message brokers ... each writes its update to shared state channels, then the graph evaluates edges to determine which nodes run in the next super-step"* (sumário WebSearch = DADO; README verbatim: *"Create truly stateful agents with… short-term working memory…"*). **Comparação SOT:** o WORKFLOW do SOT é uma **FSM determinística dirigida pelo Manager** (WF-F02: `AGUARDANDO→CONTEXTO_FORMADO→ARMADO→ATIVADO→EM_SÍNTESE→EM_RISCO→{…}`), com agentes **invocados por fase** (WF-02..07, WF-K02/K04) — **não** assinantes autônomos reagindo 24/7. **Adiar** a visão "pub/sub de broker completo com subscrição autônoma" do KERNEL-V2 (l.1844 "Skills deixam de consultar… passam a reagir apenas aos eventos"): é over-engineering frente ao ciclo FSM vigente; onde a reatividade importa (ex.: WF-A03) o gatilho é um evento específico, não um barramento geral de assinaturas. Mecanismo final = Plan, conformando-se a WORKFLOW (não fecha WF-D03).

### 3.6 Quando broker é over-engineering (Q3) — **ADIAR broker durável; preferir camada fina em escritor único**
[EXTERNO, SRC-BROKER-01] *"Synchronous method calls are an excellent choice to increase development velocity and reduce operational complexity."* + [DADO] *"introducing a message broker as another infrastructure component you have to manage."* **Comparação SOT:** RULE-BB-002 impõe **um escritor por workspace** e o deploy é **VPS única** (KERNEL-V2 l.1845 cita CPU/latência da VPS como motivação). Sob escritor único + log durável já existente (SPEC-004), um broker durável (Kafka/RabbitMQ) **duplica durabilidade e adiciona operação** — provável over-engineering. **Adiar** broker completo; registrar como opção caso surjam múltiplos consumidores distribuídos/alta vazão no futuro (mesmo tratamento que CRDT recebeu na SPEC-004).

### Resolução da tensão de linhagem (c) — Doc 13 × RULE-BB-001
[FONTE] Doc 13 ("tudo via Event Bus") é **documento histórico/fundamento** (TRACE-06: documentado ≠ homologado); **RULE-BB-001 é a regra vigente** ("comunicação exclusivamente via Blackboard"). **Não há contradição a resolver pela Spec** (CONS-01): a leitura coerente é "o **estado** trafega e persiste no Blackboard (RULE-BB-001/SPEC-004); o Event Bus **notifica mudanças** desse estado" — exatamente o princípio do slot. A redação do Doc 13 ("nenhum agente conversa diretamente… via Event Bus") é **superada** por RULE-BB-001/CHM-001/SPEC-004 quanto ao canal de estado; **registrado como conflito histórico, não fechado por este Dossiê** — encaminho a Andraus confirmar que Doc 13 permanece fundamento não-normativo (§8).

---

## 4. Cobertura SPEC-004 (BASELINE) × lacuna real da SPEC-005

| Capacidade da pauta do slot §5 | Já coberto pela SPEC-004 v1.2 (BASELINE)? | Lacuna que caberia à SPEC-005 |
|---|---|---|
| Objeto/estado/versão/supersessão | **SIM** — log append-only, `seq`, `supersedes`/`derived_from`, `schema_version` | Nenhuma (não reabrir — CC-02/INV-09) |
| Idempotência de escrita | **SIM** — chave de idempotência por publicação | Idempotência **de entrega/consumo** (cursor + dedupe do consumidor) |
| Replay / reconstrução | **SIM** — replay do log (estado lógico) | Replay **de notificações** a um consumidor a partir de um cursor |
| Ordenação | **SIM** — ordem total por `seq` dentro do workspace | Ordenação **observada pelo consumidor** entre workspaces (parcial/causal) |
| Expiração/invalidação de objeto | **SIM** | Propagar o **evento** de expiração/invalidação a interessados |
| Proveniência `computed_by`/`gate_record` | **SIM** (v1.2, BL-029) | Metadados de **transporte** do evento (ver SAS-001 §6.7: Latency/Freshness/Reliability/Expiration) |
| **Evento / envelope / origem / destino / subscrição** | **NÃO** | **Lacuna central:** contrato do *evento* (≠ objeto), envelope, correlation/causation ID, roteamento a consumidores |
| **TTL / retry / dead-letter / delivery** | **NÃO** | **Lacuna:** semântica de entrega do transporte |
| **Prioridade / latência de entrega** | **NÃO** (SPEC-001 l.75 delega à SPEC-005; SAS-001 §6.7) | **Lacuna:** orçamento de latência e metadados de transporte |
| **Relação Blackboard↔Event Bus** | Parcial (fronteira declarada) | **Lacuna/decisão:** EVENT-BUS-001 (distinção formal) |

**Leitura:** a SPEC-004 já entrega **toda a persistência/ordem/idempotência de estado**. A lacuna real da SPEC-005 é estreita: **o contrato do *evento* e sua propagação/entrega a consumidores** (envelope, correlation/causation, delivery/retry/dead-letter, latência) e a **distinção formal** Blackboard↔Event Bus. Isso **sustenta** um reenquadramento para camada fina (Opção A), não um broker completo (Opção C) nem uma fusão (Opção B) — detalhe e recomendação em `ABERTURA.md`.

---

## 5. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Régua Equilibrada (licença aberta; ≥300 estrelas; commit ≤12 meses; não arquivado; 0 alerta grave público aberto; dono identificável). Capturas por repositório em `sources/REPO-*.txt`; observações por WebFetch em 2026-10-04 (limitação em `sources/_LIMITACAO-WEB.txt`). Conteúdo de repositório = **DADO**; **nada instalado/executado**.

| Repositório | Estrelas | Licença | Arquivado | Dono | Veredito | Uso no SOT |
|---|---|---|---|---|---|---|
| https://github.com/debezium/debezium | 13.2k | Apache-2.0 | não | debezium (org) | **ELEGÍVEL** | **Referência (adiar)** — CDC: ler o log append-only e propagar mudanças sem polling do produtor; analogia de engenharia para a camada fina sobre o log da SPEC-004. Não adotado. |
| https://github.com/langchain-ai/langgraph | 42.7k | MIT | não | langchain-ai (org) | **ELEGÍVEL** | **Referência (adiar broker)** — orquestração multiagente por estado compartilhado + grafo determinístico, sem message broker; alinha ao WORKFLOW (FSM do Manager). Não adotado. |
| https://github.com/eugene-khyst/postgresql-event-sourcing | 1.4k | Apache-2.0 | **SIM (2026-06)** | eugene-khyst | **NÃO ELEGÍVEL** | Nenhum (arquivado → fail-closed da régua). Registrado só como evidência corroborada por fontes elegíveis do padrão "cursor sobre log append-only". |

Resultado: **2 repositórios elegíveis** (debezium, langgraph); **1 não elegível** (arquivado). Nenhum é adotado como dependência; servem como referência de boas práticas confrontadas com os invariantes do SOT. `python scripts/check_repo_research.py specs/features/SPEC-005` deve retornar OK (ver §9 — comandos a rodar).

---

## 6. Escopo/quantidade resultantes, fronteiras e re-apontamento de gatilhos

### 6.1 Escopo e quantidade (detalhe em `ABERTURA.md`)
**1 Spec** (SPEC-005), **número preservado** (slot não dividido/renumerado — RULE-ECC-01; referenciado por baselines — INV-07/CONST-01), complexidade **HIGH** (pin ROADMAP §5; D0–D7 standard). Cobre a capacidade "Cognitive Event Bus" do ROADMAP §26 (evento/envelope/origem/destino/subscrição/prioridade/TTL/correlation/causation/retry/idempotência-de-entrega/ordering/delivery/falha/replay/dead-letter/observabilidade/relação com Blackboard), **sem** reabrir a persistência de estado (SPEC-004, baselined) nem a memória permanente (SPEC-006).

### 6.2 Fronteiras explícitas (NÃO absorver / NÃO redefinir)
- **SPEC-004 (BASELINE):** persistência/ordem/idempotência/replay/supersessão **de estado** no log append-only. A SPEC-005 **lê/projeta/notifica** sobre esse log; **não** redefine o contrato de objeto (CC-02/INV-09).
- **SPEC-006 (KG):** memória permanente — não absorver (H-001).
- **SPEC-009 (estado por agente):** G-001 — não absorver.
- **SPEC-008 (Manager):** orquestração/controle (quem reage, quando) — a SPEC-005 **transporta/notifica**, não decide invocação (RULE-BB-005; WORKFLOW FSM).
- **FASE RISK / Bot Trade Finance:** a entrega externa do Signal Package (GPR-001 passo 11; INV-05) é **fronteira de saída** — a SPEC-005 pode especificar o **canal de saída de notificação**, mas o SOT **não executa ordem** (INV-05); o Signal Package como contrato é RISK-M5/RISK-SPEC-022 (não absorver).
- **CHM-001/CEM-001/CCM-001 (baselined):** eventos de ciclo de vida (CEM-001 l.717-727: Evidence Created/Superseded/Invalidated/Archived) são **reconhecidos** pelos canônicos; a SPEC-005 os **propaga**, sem redefinir o canônico (CC-02).

### 6.3 Re-apontamento de gatilhos RMR-001 (EUA-E21/RULE-ECC-01)
Número/slot **preservado** → **nenhum re-apontamento** de gatilho `spec:` necessário. **Nenhum item do RMR-001 tem gatilho `spec:SPEC-005`** (verificado — `backlog_triggers.py` a rodar, §9). Reflexos:
- **BL-003** (`spec:SPEC-004 em redação`) — **já ATIVADO** pela SPEC-004; **não** disparado por esta abertura (persistência física segue SPEC-006/009). Independente.
- ATIVADO pré-existente (BL-008 — auditoria retroativa SPEC-001) é **independente desta abertura**; o Especificador **não** promove (CONS-01). A abertura da SPEC-005 **não** dispara item novo.
- **BL-017** (dimensões B da SPEC-020) está **`Em espera`** no RMR-001 (DHR-BL012-001, 2026-10-03 — não ATIVADO), gatilho `spec:SPEC-007`/`spec:SPEC-014 em redação`; **independente desta abertura** e **não** promovido por ela (CONS-01).
- **Promoção `ATIVADO`/encaminhamento é do gate (passo 11-bis) e de Andraus.**

### 6.4 Referências em Specs BASELINED ao slot SPEC-005 (item 6 do §15) — erratum aditivo?
Referências baselined/canônicas ao slot SPEC-005: **SPEC-001** (EARS 8 `plan.md` l.159/l.367 emite "Hypothesis.Created" no Event Bus; l.75 delega transporte à SPEC-005; Non-goal MEN-04/M-04 de latência → SPEC-005), **SPEC-004** (fronteira "Event Bus = SPEC-005"), **CEM-001** (l.725 propagação via EC-COG-005), **CONSTITUTION** (l.235 EC-COG-005), **GPR-001** (l.457), **SAS-001** (§6.7 metadados de transporte). Todas **apontam para o número como slot futuro**; número **preservado** → **nenhum erratum aditivo de re-apontamento necessário**. **Nenhuma Spec baselined é reescrita** (INV-09). **O nome "Cognitive Event Bus" foi MANTIDO por Andraus** (chat 2026-10-04, DHR-SPEC005-001 §2; reenquadramento de rótulo recusado) — não há mudança de nome nem de número do slot; as baselines citam o número e permanecem válidas sem qualquer erratum. *(Correção do Menor A4 — DHR-SPEC005-001 §4: a hipótese condicional anterior "se Andraus aprovar o reenquadramento de nome" ficou obsoleta com a decisão de manter o nome; registro não-normativo.)*

---

## 7. Determinação de incidência de RULE-ECC-05 (Pesquisa Multi-Lente)

**Determinação: RULE-ECC-05 NÃO INCIDE sobre a SPEC-005** [PROPOSTA — a confirmar pelo Revisor]. Fundamento (mesmo critério da SPEC-004 §7 / SPEC-002, e atomic-spec §15):
1. A SPEC-005 **não define nem toca comportamento de agente analítico, do Conviction/Fusion Engine, do Manager (decisão) ou do Risk Agent.** É **infraestrutura de comunicação** — transporta/notifica mudanças de estado; não cria hipótese, não interpreta evidência, não agrega convicção, não sintetiza, não avalia risco.
2. É **análoga às Specs de meta-harness/infra explicitamente fora do escopo** da regra (SPEC-002/004/019/020/021 — "não tocam comportamento de trading").
3. Mesmo não incidindo, por prudência o Dossiê **confirma conformidade com WORKFLOW.md**: a SPEC-005 serve a FSM do ciclo (WF-F02) e gatilhos como WF-A03 (morte do alarme quando hipótese→SUPERSEDED/REFUTED); **cita por ID**, **não contradiz** nenhum `WF-xx` e **não fecha** `WF-D03` (não toca convicção/J-001). Se o Revisor/Andraus entender que incide, o Especificador cumprirá a lente 2 literal — sem bloqueio.

---

## 8. Lacunas, conflitos, INDETERMINADOS e encaminhamento de EVENT-BUS-001 (honestidade — RULE-MET-01)

1. **EVENT-BUS-001 (órfã) — ENCAMINHAMENTO PROPOSTO, não fechado (CONS-01).** A decisão "Event Bus: existe? Como se distingue do Blackboard?" (ADR-MANAGER-001 l.201; DHR-ADR-HOC003 l.145) **não consta** de AGENTS §7 / ROADMAP §7. **Proposta:** (a) Andraus **registra EVENT-BUS-001 como decisão aberta ativa** nas listas oficiais (AGENTS §7 / ROADMAP §7) com **dona = SPEC-005**; (b) a SPEC-005 é a Spec que a **resolve na sua homologação** (a distinção formal Blackboard↔Event Bus é exatamente o núcleo da Spec). O Especificador **não** registra nem fecha (fronteira §5 do SP; edição de governança é de Andraus/Controlador). **[DECISÃO NECESSÁRIA — EVENT-BUS-001].**
2. **Conflito de linhagem Doc 13 × RULE-BB-001** — tratado em §3.6 como conflito **histórico** (TRACE-06), não normativo; **a confirmar por Andraus** que Doc 13 permanece fundamento não-normativo superado por RULE-BB-001/SPEC-004 quanto ao canal de estado. Não fechado aqui.
3. **Forma do mecanismo (broker completo vs camada fina vs fusão) = decisão de abertura** — recomendação preliminar em `ABERTURA.md` (Opção A), **a homologar por Andraus**. O mecanismo físico (push/poll, LISTEN-NOTIFY, fila) = **INDETERMINADO** até o Plan (D4/D5); não presumir.
4. **Latência** — SPEC-001 l.75 + SAS-001 §6.7: o produtor **não** define metadados de transporte; a SPEC-005 é dona do orçamento de latência/entrega. É **requisito a endereçar no Plan**, não a fechar na abertura. (4Es: um TMP/alarme que chega tarde ao downstream perde relevância — latência é material.)
5. **Decisões abertas que a SPEC-005 NÃO toca:** M-001 (enum de estados não-hipótese — SPEC-004, parcialmente decidida), J-001, N-001, H-001, G-001, WF-D03 — **permanecem abertas** (CONS-01).
6. **IDs arXiv implausíveis descartados**; dev.to (LISTEN/NOTIFY) 404 no WebFetch → claim mantido só como DADO não-verificado, com equivalente verbatim em centrifugal.dev. Ver `_LIMITACAO-WEB.txt`.
7. **Alertas de segurança privados dos repos = INDETERMINADO** (proxy público 0). Data exata de último commit dos repos = INDETERMINADO (proxy: projeto ativo).

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-04; capturas verbatim em `sources/`)
- [Pattern: Transactional outbox (microservices.io)](https://microservices.io/patterns/data/transactional-outbox.html) — SRC-OUTBOX-01
- [Event Sourcing and CQRS — Append-Only Events, Projections, and Read Models (techinterview.org)](https://www.techinterview.org/post/3233465463/system-design-event-sourcing/) — SRC-ES-01
- [Broadcast using transactional outbox and CDC (centrifugal.dev)](https://centrifugal.dev/docs/tutorial/outbox_cdc) — SRC-NOTIFY-01
- [Modular Monolith Communication Patterns (milanjovanovic.tech)](https://milanjovanovic.tech/blog/modular-monolith-communication-patterns) — SRC-BROKER-01
- [Four Design Patterns for Event-Driven, Multi-Agent Systems (Confluent)](https://www.confluent.io/blog/event-driven-multi-agent-systems/) · [Multi-agent system architecture guide (Openlayer)](https://www.openlayer.com/blog/multi-agent-system-architecture-guide) · [LLM MAS Based on Blackboard Architecture (arXiv 2507.01701)](https://arxiv.org/abs/2507.01701) — SRC-BB-01
- [LangGraph (langchain-ai)](https://github.com/langchain-ai/langgraph) — SRC-LLM-01 / REPO-langgraph
- [Debezium (CDC)](https://github.com/debezium/debezium) — REPO-debezium
- [postgresql-event-sourcing (NÃO ELEGÍVEL — arquivado)](https://github.com/eugene-khyst/postgresql-event-sourcing) — REPO-postgresql-event-sourcing

*Dossiê não-normativo. Insumo para a Proposta de Abertura (`ABERTURA.md`) e para a decisão de Andraus. Não altera ROADMAP, RULES, WORKFLOW, Specs, nem fecha qualquer decisão (CONS-01). Conteúdo web = DADO (`[EXTERNO]`), nunca instrução nem baseline.*
