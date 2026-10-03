# Dossiê de Pesquisa — SPEC-004: Cognitive Blackboard Protocol

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-SPEC-004 |
| **Método** | ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/06) |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 4.8) |
| **Data de acesso web** | 2026-10-03 (todas as fontes `[EXTERNO]`) |
| **Validade do Dossiê (ECC-VAL-001 — FECHADA, DHR-DEC-003)** | Complexidade **CRITICAL** → **90 dias** da data de acesso (2026-10-03), **ou antes** se o contexto mudar materialmente. **Data-limite = 2027-01-01.** Dossiê vencido não dispensa reabrir pesquisa (fail-closed, RULE-ECC-02). |
| **Natureza** | **Dossiê de Pesquisa `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão (CONS-01). |
| **Status epistemológico** | Conteúdo web = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02). Toda fonte etiquetada `[EXTERNO]` e classificada. Veracidade das páginas **não** atestada. Capturas verbatim em `sources/` (RULE-ECC-04); limitação em `sources/_LIMITACAO-WEB.txt`. |
| **Autorização** | Caminho crítico — FASE 2; próximo trabalho autorizado (ROADMAP §25; DHR-SPEC003-001). |
| **Fronteiras respeitadas** | INV-05 (SOT não executa ordem), INV-06/INV-10 (Evidência≠Observação; CEM-001 idioma canônico), INV-07 (versionamento monotônico), INV-09 (sem baseline informal). Não redefine CHM-001/CEM-001/CCM-001 (CC-02). Event Bus = SPEC-005; Knowledge Graph = SPEC-006; estado persistente por agente (G-001) = SPEC-009. |

> **Aviso de método (RULE-MET-01 — sem bajulação, sem fabricação).** A busca web retornou **várias fontes com identificadores arXiv implausíveis/futuros** (2605.*/2606.*/2607.*/2608.*/2609.*). Foram **descartadas** por não verificáveis e risco de fabricação (`sources/_LIMITACAO-WEB.txt`). Só foram mantidas fontes verificáveis (W3C PROV; arXiv 2507.01701; documentação técnica; páginas GitHub). Nenhum padrão externo foi importado automaticamente; cada achado é confrontado com a arquitetura SOT antes de qualquer proposta.

---

## 1. Questões e estratégia de busca

**Questões (derivadas do título do slot ROADMAP §5 + M-001 + fronteiras):**
- Q1. O que o estado da arte define como **arquitetura blackboard** / memória de trabalho compartilhada de sistemas multiagente (componentes, controle, publicação/leitura)?
- Q2. Como modelar **estados e ciclo de vida** de objetos publicados que **não são hipótese** (Evidência, Missão, Convicção, Observação) — o núcleo de **M-001**?
- Q3. Como o estado da arte trata **concorrência, ordenação e idempotência** de escrita em estado compartilhado?
- Q4. Como se modela **proveniência/lineage** de objetos num estado compartilhado (para auditabilidade/reconstrução — D9)?
- Q5. Como se garante **append-only / versionamento monotônico / replay** (reconstrução histórica) — já invariante do SOT (RULE-BB-004/INV-07)?
- Q6. Que **repositórios seguros e bem avaliados** (RULE-ECC-06) exemplificam boas práticas de estado compartilhado concorrente, memória de agentes e proveniência?

**Estratégia:** WebSearch para mapear o campo (blackboard multiagente; memória compartilhada de LLM; idempotência/OCC; W3C PROV; event sourcing); WebFetch para capturar verbatim fontes-padrão (W3C PROV, abstract arXiv) e para auditar estaticamente páginas de repositórios GitHub (stars/licença/commit/arquivado — **nada instalado/executado**). Fontes classificadas `[EXTERNO]`; capturas em `sources/*.txt` (RULE-ECC-04/06).

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Papel |
|---|---|---|---|
| SRC-BB-01 | arXiv 2507.01701 "LLM Multi-Agent Systems Based on Blackboard Architecture" + confluent/tetrate | Experimento/Evidência + Prática | Modelo blackboard, controle, publicação/consenso (Q1) |
| SRC-PROV-01 | W3C PROV-DM (Recommendation) | **Padrão** | Vocabulário de proveniência entity/activity/agent (Q4) |
| SRC-ES-01 | Event Sourcing & CQRS (mia-platform, techinterview) | Prática | Append-only, replay, auditabilidade (Q5) |
| SRC-CONC-01 | Idempotência / Optimistic Concurrency (algomaster, event-driven.io, risingwave) | Prática | Concorrência, ordenação, idempotência (Q3) |
| SRC-MEM-01 | Memória em MAS de LLM (survey; governed shared memory) | Opinião/Evidência | Topologia de memória compartilhada, governança de escrita (Q1/Q2) |
| REPO-yjs | github.com/yjs/yjs | Prática (repo elegível) | Convergência de estado concorrente (Q3/Q6) |
| REPO-automerge | github.com/automerge/automerge | Prática (repo elegível) | CRDT JSON concorrente, merge automático (Q3/Q6) |
| REPO-mem0 | github.com/mem0ai/mem0 | Prática (repo elegível) | Ciclo de vida de objeto de memória ADD/UPDATE/DELETE/NOOP (Q2/Q6) |

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

### 3.1 Arquitetura blackboard (Q1) — **ADOTAR o enquadramento (já é canônico no SOT)**
[EXTERNO, SRC-BB-01] *"agents with various roles can share all the information and others' messages during the whole problem-solving process"*; *"agents that will take actions are selected based on the current content of the blackboard"*; *"No agent owns the blackboard or controls execution order."* O SOT **já** adota esse padrão: RULE-BB-001 (comunicação exclusivamente via Blackboard), RULE-BB-005 (Orchestrator só coordena, nunca analisa). **Adotar** como confirmação externa do desenho vigente; a camada Harness da SPEC-004 formaliza **o protocolo** (o quê/quando/ordem/versão de publicação), não reinventa o padrão. **Rejeitar** a parte "controle seleciona agentes/consenso" como mecanismo de orquestração — isso é **SPEC-008 (Manager)**, não o Blackboard (fronteira explícita §6).

### 3.2 Estados de objetos NÃO-hipótese (Q2 / M-001) — **ADAPTAR; decisão permanece ABERTA (CONS-01)**
[EXTERNO, SRC-MEM-01] memória tratada como *"evolving state ... where each memory object carries creation timestamps, supersession references, contradiction markers, and provenance metadata"*; [EXTERNO, REPO-mem0] pipeline que *"selects among ADD, UPDATE, DELETE, and NOOP operations"*. **Tensão com o SOT:** DELETE/UPDATE destrutivos **violam** RULE-BB-004/INV-07 (append-only; SUPERSEDED, nunca deletado). **Adaptar, não adotar:** o ciclo de vida de Evidência/Missão/Observação no Blackboard do SOT deve ser **append-only com supersessão** (projeção do estilo UPDATE→nova versão; DELETE→ARCHIVED/SUPERSEDED), alinhado a CEM-001 (ciclo de vida da Evidência, Cap.4) e CHM-001 (estados da hipótese — que o Blackboard **não** redefine, RULE-BB-003). **M-001 (estados do Blackboard para objetos não-hipótese) PERMANECE ABERTA** — este Dossiê levanta opções, **não fecha** (ver §5). [PROPOSTA] para o Plan: reusar/projetar o ciclo do CEM-001 em vez de criar enum novo.

### 3.3 Concorrência, ordenação, idempotência (Q3) — **ADOTAR optimistic concurrency + idempotency key; ADIAR CRDT**
[EXTERNO, SRC-CONC-01] *"Optimistic Concurrency ... only accept updates if the stream/record version in the database is the same as the expected one"*; *"Idempotency ensures each transaction processes exactly once, even during retries or failures ... unique transaction identifiers"*; *"events may be delivered out of order"*. [EXTERNO, REPO-yjs/REPO-automerge] CRDTs garantem que *"all data replicas eventually converge to the same state"* sem conflito. **Comparação SOT:** RULE-BB-002 já restringe escrita (um escritor por workspace) — isso **reduz** a necessidade de merge concorrente multi-escritor (caso de uso central de CRDT). **Adotar:** versionamento otimista (rejeitar escrita com versão esperada divergente) + chave de idempotência por publicação (retry seguro). **Adiar CRDT (yjs/automerge):** poderoso para co-edição multi-escritor, mas provavelmente **over-engineering** sob RULE-BB-002 (workspace de escritor único); registrado como opção caso surja escrita verdadeiramente concorrente no mesmo workspace. Decisão de mecanismo é do Plan (D4/D5) — não se fecha aqui.

### 3.4 Proveniência / lineage (Q4) — **ADAPTAR o vocabulário W3C PROV ao Lineage do CEM-001 (não substituir)**
[EXTERNO, SRC-PROV-01] *"Provenance is information about entities, activities, and people involved in producing a piece of data ... to form assessments about its quality, reliability or trustworthiness"*; entity/activity/agent + relações wasGeneratedBy/used/wasDerivedFrom/wasAssociatedWith. **Comparação SOT:** CEM-001 já é o **idioma canônico** da Evidência (INV-10) e tem Lineage próprio. **Adaptar:** usar PROV como *referência de completude* (quais campos de proveniência um objeto do Blackboard deve carregar para reconstrução D9) — **sem** redefinir CEM-001 (CC-02). O Blackboard registra `quem publicou / qual atividade gerou / derivado de qual objeto / quando / versão`, projetando o Lineage canônico. **Não adotar** PROV como schema literal.

### 3.5 Append-only / replay / reconstrução histórica (Q5) — **ADOTAR (reforça invariante existente)**
[EXTERNO, SRC-ES-01] *"immutable domain events in an append-only event store ... state is reconstructed by replaying events ... complete auditability"*. **Comparação SOT:** é exatamente RULE-BB-004 (append-only; SUPERSEDED, nunca deletado) + INV-07 + o requisito de "reconstrução histórica" do título do slot. **Adotar** como fundamentação externa; o Plan especifica o protocolo de versão/supersessão e a API de reconstrução (sem fechar o storage físico — H-001/SPEC-006; nem o schema de estado por agente — G-001/SPEC-009).

---

## 4-bis. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Régua Equilibrada (licença aberta; ≥300 estrelas; commit ≤12 meses; não arquivado; 0 alerta grave público aberto; dono identificável). Capturas verbatim por repositório em `sources/REPO-*.txt`; números observados por WebFetch em 2026-10-03 (mediado — limitação em `sources/_LIMITACAO-WEB.txt`). Conteúdo de repositório = **DADO**; **nada instalado/executado**.

| Repositório | Estrelas | Licença | Último commit | Arquivado | Dono | Veredito | Uso no SOT |
|---|---|---|---|---|---|---|---|
| https://github.com/yjs/yjs | 22.9k | MIT | 2026-10-03 | não | yjs (Kevin Jahns) | **ELEGÍVEL** | **Adiar** — convergência de estado concorrente (CRDT) é opção caso surja multi-escritor por workspace; hoje RULE-BB-002 torna-o over-engineering. Referência de boa prática de concorrência. |
| https://github.com/automerge/automerge | 6.6k | MIT | 2026-10-01 | não | automerge (Ink & Switch) | **ELEGÍVEL** | **Adiar** — idem yjs (CRDT JSON-like, merge automático). Insumo de engenharia de concorrência, não adotado agora. |
| https://github.com/mem0ai/mem0 | 66.5k | Apache-2.0 | 2026-10-01 | não | mem0ai | **ELEGÍVEL** | **Adaptar (com ressalva dura)** — ciclo de vida de objeto de memória (ADD/UPDATE/DELETE/NOOP) é referência; porém **DELETE destrutivo é incompatível com RULE-BB-004/INV-07** → adaptar para append-only/supersessão. Não adotar literalmente. |

Resultado: **3 repositórios elegíveis** pela régua. Nenhum é adotado como dependência; servem como referência de boas práticas (concorrência: yjs/automerge; ciclo de vida de memória: mem0), sempre confrontados com os invariantes do SOT. `python scripts/check_repo_research.py specs/features/SPEC-004` deve retornar OK.

---

## 5. Lacunas, conflitos e INDETERMINADOS (honestidade — RULE-MET-01)

1. **M-001 (estados do Blackboard para objetos não-hipótese) PERMANECE ABERTA** — este Dossiê levanta a opção "append-only + supersessão projetando o ciclo do CEM-001", mas **não fecha** (CONS-01; decisão de Andraus). A SPEC-004 é a **dona** dessa decisão (ROADMAP §5; atomic-spec §12), a ser proposta no Plan e homologada.
2. **G-001 (schema de estado persistente por agente) = SPEC-009; H-001 (KG grafo real vs. memória) = SPEC-006** — a SPEC-004 referencia o storage **sem** fechá-lo (fronteira §6). BL-003 (persistência física) ativa `spec:SPEC-004 em redação`.
3. **CRDT (yjs/automerge) = INDETERMINADO quanto à necessidade** — depende de haver escrita multi-escritor no mesmo workspace, hoje vedada por RULE-BB-002. Não presumir necessidade; adiado.
4. **Alertas de segurança privados dos repositórios = INDETERMINADO** (Dependabot privado não observável); registrado o proxy público "0 grave aberto" (`sources/_LIMITACAO-WEB.txt`).
5. **Fontes web com IDs arXiv implausíveis descartadas** — ver aviso de método e `_LIMITACAO-WEB.txt`. Veracidade das páginas mantidas não é atestada (DADO).
6. **BL-029 (proveniência: `computed_by`/`gate_record`) — dona = SPEC-004 (DHR-DEC-003)** e **BL-002 (método de observação de falso-DENY do Blackboard) — encaminhado à SPEC-004 (DHR-DEC-003)**: ambos ativam `spec:SPEC-004 em redação` e são requisitos a **endereçar no Plan**, não a fechar nesta abertura.

---

## 6. Escopo/quantidade resultantes, fronteiras e re-apontamento de gatilhos

### 6.1 Escopo e quantidade (detalhe em `ABERTURA.md`)
**1 Spec** (SPEC-004), número preservado (slot não dividido/renumerado — RULE-ECC-01), complexidade **CRITICAL**, profundidade **D0–D7** (pinada no ROADMAP §5 e consistente com atomic-spec §3 "Blackboard Protocol CRITICAL D0–D7"). Cobre a capacidade "Cognitive Blackboard Protocol" do ROADMAP §26 (memória de trabalho: objetos/versões/estados/namespaces/lifecycle/concorrência/ordenação/idempotência/proveniência/permissões/reconstrução), **sem** absorver transporte de eventos (SPEC-005) nem memória permanente (SPEC-006).

### 6.2 Fronteiras explícitas (NÃO absorver)
- **SPEC-004 (este slot):** Blackboard como **memória de trabalho**; contrato de objeto publicado (versão/estado/namespace/proveniência/permissão); protocolo de publicação/leitura/atualização/supersessão/expiração/invalidação; concorrência/ordenação/idempotência; reconstrução histórica (append-only).
- **SPEC-005 (Event Bus):** transporte de mudanças; envelope/subscrição/TTL/correlation/causation/retry/replay/dead-letter. Princípio: *"Blackboard guarda estado; Event Bus transporta mudanças."* — **não absorver**.
- **SPEC-006 (Knowledge Graph):** memória **permanente**; ontologia/relações. *"Blackboard é memória de trabalho; KG é memória permanente."* — **não absorver**. H-001 aqui.
- **SPEC-009 (Cognitive State & Persistence):** schema de estado persistente **por agente** (G-001) — **não absorver**.
- **CHM-001/CEM-001/CCM-001 (baselined):** o Blackboard **armazena/versiona/publica** hipótese, evidência e convicção **sem redefinir** seus contratos nem a máquina de estados da hipótese (RULE-BB-003; CC-02). INV-06/INV-10 preservados (Evidência≠Observação; idioma canônico).
- **INV-05:** o Blackboard não executa ordem; é memória de análise.

### 6.3 Re-apontamento de gatilhos RMR-001 (EUA-E21/RULE-ECC-01)
Número/slot **preservado** → nenhum re-apontamento de gatilho `spec:` necessário. A **abertura** conta como "em redação" (precedente BL-004 na SPEC-003; BL-031 na SPEC-038), portanto dispara ao entrar em redação (Plan):
- **BL-003** (`spec:SPEC-004 em redação`) → ativará: especificar o storage (Blackboard) referenciado pelo slot da SPEC-001. **Encaminhamento no Plan**, não nesta abertura.
- **BL-029** (`spec:SPEC-014 ∨ spec:SPEC-004 em redação`; **dona = SPEC-004**, DHR-DEC-003) → proveniência `computed_by`/`gate_record` do objeto no Blackboard (M-001). **Endereçar no Plan.**
- **BL-002** (Absorvido; encaminhado à SPEC-004 por DHR-DEC-003) → requisito de **observabilidade do Blackboard** (método de observação de falso-DENY do gate E3). **Endereçar no Plan.**
- **BL-011** (MC-EXP-001, ref. externa) — afeta SPEC-004, mas gatilho é `spec:SPEC-006/009` → **não dispara** aqui; fonte de requisitos futura.
- **BL-010** (MC-RAG-001) — gatilho `spec:SPEC-007` → não dispara.
- **Promoção `ATIVADO`/encaminhamento é do gate (passo 11-bis) e de Andraus** — o Especificador **não** promove (CONS-01). ATIVADOS pendentes atuais (BL-012, BL-017) são independentes desta abertura.

### 6.4 Referências em Specs BASELINED a SPEC-004 (item 6 do §15) — erratum aditivo?
Referências baselined ao slot SPEC-004 encontradas: SPEC-001 (storage físico diferido a "SPEC-004/006"), SPEC-038 (storage de Observação "M-001/H-001 abertas → SPEC-004/006"). Ambas **apontam para o número como slot futuro**; número **preservado** → **nenhum erratum aditivo de re-apontamento necessário** (padrão ERRATUM-SPEC019-001 não se aplica). Nenhuma Spec baselined é reescrita (INV-09).

---

## 7. Determinação de incidência de RULE-ECC-05 (Pesquisa Multi-Lente)

**Determinação: RULE-ECC-05 NÃO INCIDE sobre a SPEC-004** [PROPOSTA — a confirmar pelo Revisor]. Fundamento (mesmo critério do Adendo 8-A da SPEC-038):
1. A SPEC-004 **não define nem toca comportamento de agente analítico, do Conviction/Fusion Engine, do Manager ou do Risk Agent.** É **infraestrutura de memória de trabalho/comunicação** — armazena/versiona/publica objetos sem criar hipótese, interpretar evidência, agregar convicção, sintetizar ou avaliar risco.
2. É **análoga às Specs de meta-harness explicitamente excluídas** pela regra (SPEC-002/019/020/021 "e análogas … não tocam comportamento de trading").
3. Mesmo não incidindo, por prudência o Dossiê **confirma conformidade com WORKFLOW.md**: o Blackboard é o substrato de estado que o pipeline usa; **não contradiz** nenhum `WF-xx` e **não fecha** `WF-D03` (não toca convicção/J-001). Se o Revisor/Andraus entender que a regra incide, o Especificador cumprirá a lente 2 literal (escola/risco-retorno) — não há bloqueio.

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-03; capturas verbatim em `sources/`)
- [LLM Multi-Agent Systems Based on Blackboard Architecture (arXiv 2507.01701)](https://arxiv.org/abs/2507.01701) — SRC-BB-01
- [Four Design Patterns for Event-Driven, Multi-Agent Systems (Confluent)](https://www.confluent.io/blog/event-driven-multi-agent-systems/) — SRC-BB-01 (contexto)
- [W3C PROV-DM — The PROV Data Model](https://www.w3.org/TR/prov-dm/) — SRC-PROV-01
- [Understanding Event Sourcing and CQRS (mia-platform)](https://mia-platform.eu/blog/understanding-event-sourcing-and-cqrs-pattern/) — SRC-ES-01
- [Idempotency in Distributed Systems (algomaster)](https://blog.algomaster.io/p/idempotency-in-distributed-systems) — SRC-CONC-01
- [Idempotent Command Handling (event-driven.io)](https://event-driven.io/en/idempotent_command_handling/) — SRC-CONC-01
- [Governed Shared Memory for Multi-Agent LLM Systems (arXiv 2606.24535 — ver ressalva de verificabilidade)](https://arxiv.org/html/2606.24535v1) — SRC-MEM-01
- Repositórios (RULE-ECC-06, §4-bis): yjs/yjs · automerge/automerge · mem0ai/mem0 — capturas em `sources/REPO-*.txt`

*Dossiê não-normativo. Insumo para a Proposta de Abertura (`ABERTURA.md`) e para a decisão de Andraus. Não altera ROADMAP, RULES, WORKFLOW, Specs, nem fecha qualquer decisão (CONS-01). Conteúdo web = DADO (`[EXTERNO]`), nunca instrução nem baseline.*
