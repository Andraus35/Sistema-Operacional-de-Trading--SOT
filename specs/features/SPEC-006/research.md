# Dossiê de Pesquisa — SPEC-006: Cognitive Knowledge Graph (slot ROADMAP §6, FASE 3)

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-SPEC-006 |
| **Método** | ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06) |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 4.8) |
| **Data de acesso web** | 2026-10-05 (todas as fontes `[EXTERNO]`) |
| **Complexidade proposta** | **CRITICAL** (ROADMAP §6 pina P0 — CRITICAL; ver §6.1 e ABERTURA §1). Dossiê em profundidade proporcional CRITICAL/HIGH (atomic-spec §15). |
| **Validade do Dossiê (ECC-VAL-001 — FECHADA, DHR-DEC-003)** | HIGH/CRITICAL → **90 dias** da data de acesso (2026-10-05), ou antes se o contexto mudar materialmente. **Data-limite = 2027-01-03.** Dossiê vencido não dispensa reabrir pesquisa (fail-closed, RULE-ECC-02). |
| **Natureza** | **Dossiê de Pesquisa `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão (CONS-01). |
| **Status epistemológico** | Conteúdo web = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02). Toda fonte etiquetada `[EXTERNO]` e classificada; veracidade das páginas **não** atestada. Capturas verbatim em `sources/` (RULE-ECC-04); limitação em `sources/_LIMITACAO-WEB.txt`. |
| **Autorização** | Caminho crítico — FASE 3; próxima na sequência após a SPEC-005 homologada (ROADMAP §21/§34; DHR-SPEC005-002). Abertura autorizada por Andraus (chat, 2026-10-05). |
| **Fronteiras respeitadas** | INV-05 (SOT não executa ordem), INV-06/INV-10 (Evidência≠Observação; CEM-001 idioma canônico), INV-07 (versionamento monotônico), INV-09 (sem baseline informal). Não redefine CHM-001/CEM-001/CCM-001 nem **SPEC-004/SPEC-005** (CC-02/CONST-01). Blackboard = SPEC-004 (baselined; memória de trabalho); Event Bus = SPEC-005 (baselined; notificação); RAG/Knowledge Formation = SPEC-007; estado persistente por agente (G-001) = SPEC-009. |

> **Aviso de método (RULE-MET-01 — sem bajulação, sem fabricação).** A busca web retornou **vários IDs arXiv implausíveis/futuros** (2608.*, 2606.*, 2604.*, 2601.*, 2512.*, 2511.*) — **descartados** por não-verificáveis (risco de fabricação; `sources/_LIMITACAO-WEB.txt`). Mantida como fonte acadêmica verificável **apenas** arXiv 2501.13956 (Zep, jan/2025), aberta por WebFetch e capturada verbatim. Distingo explicitamente trechos **verbatim via WebFetch** (base de alegações carregadas) de **sumários de WebSearch** (DADO de contexto). Nenhum padrão externo foi importado automaticamente; cada achado é confrontado com a arquitetura SOT antes de qualquer proposta.

---

## 0. Auditoria de entrada — "Knowledge Graph": ideia de engenharia de software ou memória cognitiva permanente?

O orquestrador pediu a mesma auditoria de conceito legado feita para o Event Bus (SPEC-005): verificar se "Knowledge Graph" nasce como **grafo de propriedades / banco de grafos** (ideia inicial de software) ou como **memória permanente cognitiva** (padrões, hipóteses resolvidas, lições). **Verifiquei cada âncora no repositório** (resultado abaixo); é `[FONTE]` interna, não baseline nova.

| Âncora da auditoria | Verificação | Resultado |
|---|---|---|
| (a) Origem conceitual | `docs/fundamentos/KERNEL-V2.md` l.1101-1104 ("Até agora falamos várias vezes em Knowledge Graph, mas nunca definimos exatamente o que ele é. Na minha opinião, ele **não deve ser um banco de dados**. Ele deve ser o **Modelo Cognitivo Permanente** do SOT.") + l.1154 ("representação semântica permanente do conhecimento do SOT, conectando evidências, hipóteses, narrativas, missões, aprendizados e ativos através de relações explícitas e auditáveis") · `ENGENHARIA-GERAL.md` l.3539-3548 (KGS "memória semântica oficial… conhecimento estruturado… não documentos") · `AUDITORIA-ideias-nao-implementadas.md` l.2825 ("O Knowledge Graph atua como sistema de arquivos semânticos") | **CONFIRMADO — é memória permanente cognitiva, NÃO banco de grafos.** O próprio documento-fonte **rejeita** a leitura "banco de dados". `[FONTE]`, status FATO ARQUITETURAL (não baseline). O **mecanismo físico** (grafo real vs. estrutura em memória) é **exatamente H-001 — ABERTA**. |
| (b) Separação Blackboard × KG | `KERNEL-V2.md` l.1456-1467 ("Blackboard ↓ Memória de trabalho. CKG ↓ Memória permanente. **Nunca misturar.**") e l.1576-1586 ("Blackboard: temporário/vivo/dinâmico/mutável. Knowledge Graph: permanente/histórico/consolidado. **Jamais misturar.**") | **CONFIRMADO.** Fronteira SPEC-004 (trabalho) × SPEC-006 (permanente) é constitutiva e já declarada no ROADMAP §5/§6. Mapa de cobertura em §4. |
| (c) Separação KG × Ontologia | `KERNEL-V2.md` l.1488-1507 ("Cognitive Ontology… O Knowledge Graph responde 'o que aconteceu?' e 'como os elementos se relacionam?'. A Ontologia Cognitiva responde 'o que cada conceito significa?' e 'quais relações são permitidas?'… a gramática do conhecimento") | **CONFIRMADO — tensão de escopo.** A pauta do §6 lista "ontologia" como item da SPEC-006; o fundamento histórico sugeria componente separado (CO). Tratado em §3.6/§6 (ontologia como camada DENTRO da SPEC-006, enxuta; não criar componente novo sem Andraus). |
| (d) Dependências já canônicas | `canon/CEM-001` l.608-615 ("Responsabilidades do Knowledge Graph: preservar toda a linhagem; preservar todas as versões; preservar todos os estados; fornecer *Cognitive Trace Reconstruction* completa… permitir navegação completa da cadeia cognitiva") + l.494 ("Knowledge Graph \| Todos os estados (preservação permanente)") + l.563-565 · `canon/SAS-001` §6.12 l.923 e l.163 ("consultado quando necessário… Não é pré-requisito obrigatório") · `CONSTITUTION.md` l.233 (EC-COG-003 "Memória relacional de padrões") · `CEE-001` l.111 (métrica de calibração entra no KG) | **CONFIRMADO.** O KG **já tem responsabilidades atribuídas por modelos canônicos BASELINED** — a SPEC-006 constrói **sobre** elas (não redefine — CC-02). Mapa em §4. |
| (e) Resolve H-001 | `atomic-spec.md` §12 (H-001 "Knowledge Graph: grafo real ou estrutura em memória?" — SPEC-006) · ROADMAP §6 ("Resolve H-001") · AGENTS §7 (H-001 ativa) | **CONFIRMADO — H-001 é o mecanismo FÍSICO.** A SPEC-006 pode fechar o **contrato cognitivo** (ontologia, entidades, relações, lifecycle, consulta, governança de escrita) sem fechar o **mecanismo físico** — este é H-001 e **só Andraus fecha** (§8). |

**Conclusão da auditoria.** "Knowledge Graph" no SOT **não** é a ideia de software "banco de grafos/property graph" — é a **memória semântica permanente cognitiva** (padrões, hipóteses resolvidas, evidências, narrativas, missões, aprendizados e suas relações auditáveis). O documento-fonte original **explicitamente rejeita** "banco de dados" e o posiciona como "Modelo Cognitivo Permanente". O que está em aberto **não é se** há memória permanente (há — referenciada por CEM-001/SAS-001/CONSTITUTION baselined), mas **(i)** qual a forma do contrato cognitivo (camada fina sobre o log/registros já existentes vs. grafo completo próprio) e **(ii)** o **mecanismo físico de armazenamento = H-001 (ABERTA — só Andraus)**.

---

## 1. Questões e estratégia de busca

**Questões (derivadas da pauta do §6 + auditoria de conceito legado + H-001 + fronteira com SPEC-004/007/009):**
- Q1. Como o estado da arte representa **memória de longo prazo de agentes LLM** como grafo de conhecimento (entidades + relações + proveniência), e como isso difere de recuperação RAG?
- Q2. Como **knowledge graphs temporais / bitemporais** tratam temporalidade, versionamento e "fato que deixou de ser verdade" (validade no tempo, invalidar vs. deletar)?
- Q3. Qual é o modelo de **provenance** consolidado (W3C PROV: entidades/atividades/agentes) e o que dele é pertinente a uma memória cognitiva auditável?
- Q4. Como o campo trata **consolidação e esquecimento controlado** (lifecycle do conhecimento; crescimento ilimitado da memória)?
- Q5. **GraphRAG vs. memória estruturada:** quando o grafo agrega valor sobre vetor/documento, e quando é over-engineering?
- Q6. Que **repositórios seguros e bem avaliados** (RULE-ECC-06) exemplificam essas práticas?

**Estratégia:** WebSearch para mapear o campo (KG temporal/bitemporal; memória de agente; provenance; forgetting; GraphRAG vs memória); WebFetch para capturar **verbatim** as fontes-base (arXiv Zep, W3C PROV, atlan) e auditar estaticamente páginas/metadados de repositório via **API pública do GitHub** (stars/licença/arquivado/pushed_at — **nada instalado/executado**). Fontes classificadas `[EXTERNO]`; capturas em `sources/*.txt` (RULE-ECC-04/06). IDs arXiv futuros/implausíveis **descartados** (honestidade RULE-MET-01).

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Papel |
|---|---|---|---|
| SRC-ZEP-01 | arXiv 2501.13956 — "Zep: A Temporal Knowledge Graph Architecture for Agent Memory" | **Benchmark** + Prática | KG temporal como memória de agente, relações históricas (Q1/Q2) |
| SRC-PROV-01 | W3C PROV-OVERVIEW (Working Group Note, 2013) | **Padrão** | Modelo de provenance: entidades/atividades/agentes (Q3) |
| SRC-MEMVSKG-01 | atlan — "AI Memory vs RAG vs Knowledge Graph" | Opinião/Prática | Distinção KG (relações, multi-salto) × RAG (documentos) (Q1/Q5) |
| SRC-FORGET-01 | Sumários WebSearch — forgetting/crescimento ilimitado em memória-grafo | Opinião/Experimento (**DADO, não verbatim**) | Consolidação/esquecimento controlado; grafo nem sempre supera vetor (Q4/Q5) |
| REPO-graphiti | github.com/getzep/graphiti | Prática (repo elegível) | KG bitemporal: janela de validade, invalidar≠deletar (Q2/Q6) |
| REPO-graphrag | github.com/microsoft/graphrag | Prática (repo elegível) | Extração de grafo de texto → retrieval (fronteira SPEC-007) (Q5/Q6) |
| REPO-cognee | github.com/topoteretes/cognee | Prática (repo elegível) | Plataforma de memória de agente em grafo (Q1/Q6) |
| REPO-mem0 | github.com/mem0ai/mem0 | Prática (repo elegível) | Camada de memória que persiste/consolida entre sessões (Q1/Q6) |

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

### 3.1 KG temporal como memória de longo prazo (Q1/Q2) — **ADAPTAR o enquadramento temporal; CONVERGE com INV-07**
[EXTERNO, SRC-ZEP-01 — verbatim via WebFetch do abstract, acesso 2026-10-05] *"Zep addresses this fundamental limitation through its core component Graphiti -- a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships."* [EXTERNO, REPO-graphiti — verbatim via WebFetch do README] *"Facts have validity windows. When information changes, old facts are invalidated — not deleted. Query what's true now, or what was true at any point in time."* **Comparação SOT:** "invalidar, não deletar" + "janela de validade" **converge** com **INV-07** (versionamento monotônico — refutado/arquivado nunca é deletado) e com **CEM-001** (l.602 "A invalidação não implica remoção") e com a máquina de estados do **CHM-001** (SUPERSEDED/REFUTED/ARCHIVED preservados). **Adaptar** o conceito de **temporalidade/validade** como propriedade das relações do KG; **rejeitar** a importação da engine Graphiti (é dependência externa; o mecanismo físico é H-001). `[INFERÊNCIA]`: o SOT já tem a semântica temporal nos canônicos — a SPEC-006 a **expressa no contrato do KG**, não a inventa.

### 3.2 Provenance (Q3) — **ADAPTAR o princípio do W3C PROV; não adotar o vocabulário RDF/OWL**
[EXTERNO, SRC-PROV-01 — verbatim via WebFetch, acesso 2026-10-05] *"Provenance is information about entities, activities, and people involved in producing a piece of data or thing, which can be used to form assessments about its quality, reliability or trustworthiness."* **Comparação SOT:** o **princípio** (proveniência = quem/o quê/como produziu, para avaliar confiabilidade) já é expresso internamente por **CEM-001** (Lineage, `computed_by`, `gate_record`) e **SPEC-004 v1.2** (proveniência com `gate_id`/`gate_version`/identidade autenticada — BL-029). **Adaptar** o princípio como requisito de que **toda entidade/relação do KG carregue proveniência**; **rejeitar** a adoção do vocabulário RDF/OWL do PROV (não é idioma do SOT — INV-10: CEM-001 é o idioma canônico da Evidência). A proveniência no KG **referencia** os contratos canônicos, não os redefine (CC-02).

### 3.3 Integração sem recomputar o grafo inteiro (Q2) — **ADOTAR o princípio incremental; alinha a append-only da SPEC-004**
[EXTERNO, REPO-graphiti — verbatim via WebFetch do README] *"New data integrates immediately without batch recomputation. The graph evolves in real-time as episodes are ingested."* **Comparação SOT:** alinha ao log **append-only** da SPEC-004 (o estado já chega consolidado e versionado); a memória permanente **cresce incrementalmente** a partir de conhecimento já validado, sem reprocessar todo o histórico. **Adotar** o princípio de **integração incremental** como requisito não-funcional do KG; o **mecanismo** (índice, materialização) fica no Plan (D4/D5) e no limite de H-001. **Não fechar** mecanismo físico aqui.

### 3.4 KG × RAG (Q1/Q5) — **ADOTAR a distinção (confirma fronteira SPEC-006 ↔ SPEC-007)**
[EXTERNO, SRC-MEMVSKG-01 — verbatim via WebFetch, acesso 2026-10-05] *"Knowledge graph stores entities and their explicit relationships for structured, multi-hop reasoning. Depth-first, relationship-oriented."* e *"RAG retrieves relevant document chunks at query time from an external index. Stateless, breadth-first, document-oriented. The standard starting point for enterprise AI."* [EXTERNO, REPO-graphrag — verbatim via WebFetch do README] *"The GraphRAG project is a data pipeline and transformation suite that is designed to extract meaningful, structured data from unstructured text using the power of LLMs."* **Comparação SOT:** confirma a **fronteira do ROADMAP**: a **SPEC-006 (KG)** é a **memória permanente de conhecimento já validado e suas relações** (raciocínio relacional/multi-salto); o **pipeline de extração/formação de conhecimento a partir de texto + retrieval é a SPEC-007 (RAG/Knowledge Formation)**. **Adotar** a distinção; **rejeitar** absorver o pipeline GraphRAG dentro da SPEC-006 (seria invadir a SPEC-007 e violar "documento recuperado ≠ conhecimento validado" do §6/§7 do ROADMAP). `Documento recuperado → Evidência candidata → Conhecimento validado → KG` é a direção; o KG recebe o conhecimento **já publicado**.

### 3.5 Quando o grafo vale o custo (Q5) — **ADIAR grafo completo; preferir camada fina sobre registros já existentes em escritor único/VPS**
[EXTERNO, SRC-MEMVSKG-01 — verbatim via WebFetch] *"your queries require multi-hop reasoning: tracing relationships across entities rather than matching document similarity"* [EXTERNO, SRC-FORGET-01 — DADO, sumário de WebSearch, NÃO verbatim] o campo registra que representar memória como grafo "does not uniformly improve retrieval over a flat vector store" e que métodos de memória-grafo "largely leave unbounded growth of the memory store unaddressed". **Comparação SOT:** sob **escritor único por workspace** (RULE-BB-002), **VPS única** e **log durável já existente** (SPEC-004), um banco de grafos completo é **provável over-engineering** se o ganho de raciocínio multi-salto não for exercido. **Adiar** o grafo-engine completo; **recomendar** (ABERTURA Opção A) uma **camada de memória permanente sobre os registros/log já existentes**, com consulta cognitiva e governança de escrita, deixando o **mecanismo físico INDETERMINADO = H-001**. Mesmo tratamento que CRDT recebeu na SPEC-004 e o broker na SPEC-005 (registrar e adiar, não apagar — INV-07).

### 3.6 Consolidação, esquecimento e ontologia (Q2/Q4) — **ADAPTAR com cautela; ontologia enxuta DENTRO da SPEC-006; esquecimento sob governança**
[EXTERNO, SRC-FORGET-01 — DADO, sumário de WebSearch, NÃO verbatim] o campo começa a tratar "forgetting module that controls the lifecycle of stored information". **Comparação SOT:** "esquecimento" no SOT **não pode** significar deleção (INV-07) — só pode ser **arquivamento/rebaixamento de relevância sob governança** (consistente com CHM-001 ARCHIVED e com a imutabilidade reforçada pelo BL-011/MC-EXP-001, que REFORÇA RULE-BB-004/INV-07). **Adaptar**: lifecycle do conhecimento = transições de estado versionadas, nunca remoção. **Ontologia** (KERNEL-V2 l.1488-1507): a pauta do §6 a lista como item da SPEC-006; o fundamento histórico sugeria um componente "Cognitive Ontology" separado. **Recomendação:** tratar a ontologia como **camada enxuta DENTRO da SPEC-006** (tipos de entidade/relação permitidos + regras de integridade), **sem criar componente novo** — a decisão de componente separado seria arquitetural e **é de Andraus** (registrado em §8, não fechado).

### Resolução da tensão de linhagem — KG "banco de grafos" × KG "memória cognitiva"
[FONTE] O fundamento original (KERNEL-V2 l.1103) **já resolve** a tensão a favor de "memória cognitiva permanente" e **contra** "banco de dados". Não há contradição normativa a resolver pela Spec (CONS-01): a leitura coerente é "o KG é a **representação semântica permanente** do conhecimento validado e suas relações auditáveis; o **mecanismo físico** (grafo real, estrutura em memória, tabelas+índice relacional) é uma decisão de engenharia **deliberadamente aberta = H-001**". Registrado como enquadramento histórico coerente, **não fechado** por este Dossiê.

---

## 4. Cobertura por canônicos/Specs BASELINED × lacuna real da SPEC-006

| Capacidade da pauta do slot §6 | Já coberto por canônico/Spec BASELINED? | Lacuna que caberia à SPEC-006 |
|---|---|---|
| Versionamento / preservação de versões | **SIM** — CHM-001 (versionamento append-only, máquina de estados); CEM-001 l.612 ("preservar todas as versões"); SPEC-004 (`schema_version`, `supersedes`) | Expor versões **como relações navegáveis** no KG permanente |
| Linhagem / proveniência | **SIM** — CEM-001 Lineage + l.608-615 (responsabilidades do KG); SPEC-004 v1.2 proveniência (`gate_id`/identidade) | **Contrato do KG** que armazena e navega a linhagem (Cognitive Trace Reconstruction — CEM l.563) |
| Estados / ciclo de vida de objetos | **SIM** — CHM-001 (hipótese), CEM-001 l.494 ("todos os estados — preservação permanente") | Lifecycle **do nó/relação do KG** (permanente/temporário, arquivamento) |
| Reconstrução da cadeia cognitiva | **SIM (como responsabilidade atribuída)** — CEM-001 l.563-565 ("capacidade do Knowledge Graph… Cognitive Trace Reconstruction") | **Especificar** essa capacidade como comportamento verificável do KG |
| Memória de trabalho / objetos ACTIVE | **SIM** — SPEC-004 (Blackboard) | Nenhuma — não reabrir (CC-02/INV-09); KG só recebe conhecimento **permanente** |
| Notificação de mudança | **SIM** — SPEC-005 (Event Bus) | Nenhuma — o KG **consome/emite** eventos de ciclo de vida, não redefine o transporte |
| **Ontologia (tipos/relações permitidas)** | **NÃO** (canônicos definem objetos, não a gramática do grafo) | **Lacuna central:** ontologia enxuta — tipos de entidade/relação e regras de integridade |
| **Entidades e relações do grafo** (CONFIRMA/REFUTA/DEPENDE_DE/HERDA/PERTENCE_A/INVALIDA…) | **NÃO** (ENGENHARIA-GERAL l.3588-3662 é fundamento histórico, não baseline) | **Lacuna central:** catálogo de tipos de nó e de relação (estrutural/institucional/hipótese/evidência/missão/aprendizado) |
| **Temporalidade / validade no tempo das relações** | **Parcial** (CHM/CEM têm estados; não "validade bitemporal") | **Lacuna:** temporalidade das relações (quando uma relação passou a/deixou de valer) |
| **Confiança / relações estatísticas** | **NÃO** (confidence de evidência ≠ confiança de relação do KG) | **Lacuna:** confiança de relação; **cuidado:** confiança ≠ Convicção (INV-04); não tocar J-001/N-001 |
| **Similaridade / causalidade / hierarquia** | **Parcial** — RULE-CAU (causal, EUA-E09) exige mecanismo | **Lacuna:** relações de similaridade/causalidade/hierarquia **respeitando RULE-CAU** (mecanismo obrigatório, não pós-hoc) |
| **Consulta cognitiva** | **NÃO** | **Lacuna:** contrato de consulta semântica (perguntas de padrão/similaridade/histórico — KERNEL-V2 l.1440-1449) |
| **Governança de escrita** | **Parcial** — SPEC-019 (governança spec-time), RULE-BB-* | **Lacuna:** quem escreve no KG, com que gate (E2/E3), imutabilidade (INV-07) |
| **Conhecimento permanente vs. temporário** | **SIM (princípio)** — KERNEL-V2 l.1456-1467 | Operacionalizar o critério de promoção trabalho→permanente (fronteira com SPEC-007/SPEC-018) |
| **Mecanismo físico de armazenamento** | **NÃO — H-001 ABERTA** | **NÃO fechar** — decisão de Andraus (§8) |

**Leitura:** os canônicos BASELINED (CHM-001, CEM-001) já **atribuem responsabilidades ao KG** (linhagem, versões, estados, Cognitive Trace Reconstruction) e as Specs de FASE 2 (SPEC-004 trabalho, SPEC-005 notificação) já cobrem **memória de trabalho e transporte**. A lacuna real da SPEC-006 é o **contrato cognitivo da memória permanente**: ontologia enxuta, catálogo de entidades/relações, temporalidade/validade, confiança de relação (≠ Convicção), consulta cognitiva e governança de escrita — **sem** fechar o **mecanismo físico (H-001)** e **sem** invadir a formação de conhecimento/RAG (SPEC-007). Isso **sustenta** a Opção A (camada fina de memória permanente sobre registros/log existentes, mecanismo físico INDETERMINADO) — detalhe e recomendação em `ABERTURA.md`.

---

## 5. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Régua Equilibrada (licença aberta; ≥300 estrelas; commit ≤12 meses; não arquivado; 0 alerta grave público aberto; dono identificável). Capturas por repositório em `sources/REPO-*.txt`; metadados por **WebFetch da API pública do GitHub** em 2026-10-05 (limitação em `sources/_LIMITACAO-WEB.txt`). Conteúdo de repositório = **DADO**; **nada instalado/executado**.

| Repositório | Estrelas | Licença | Arquivado | Dono | Veredito | Uso no SOT |
|---|---|---|---|---|---|---|
| https://github.com/getzep/graphiti | 31444 | Apache-2.0 | não | getzep | **ELEGÍVEL** | **Referência (adaptar enquadramento; adiar engine)** — KG bitemporal: "janela de validade"/"invalidar, não deletar" converge com INV-07 e CEM-001; mecanismo físico = H-001. Não adotado como dependência. |
| https://github.com/microsoft/graphrag | 36225 | MIT | não | microsoft | **ELEGÍVEL** | **Referência (adiar; fronteira SPEC-007)** — extração de grafo de texto + retrieval é pipeline de RAG/Knowledge Formation (SPEC-007), não a memória permanente (SPEC-006). Não adotado. |
| https://github.com/topoteretes/cognee | 31373 | Apache-2.0 | não | topoteretes | **ELEGÍVEL** | **Referência (adiar)** — plataforma de memória de agente em grafo; corrobora a camada memória permanente ≠ trabalho. Não adotado; mecanismo físico = H-001. |
| https://github.com/mem0ai/mem0 | 66586 | Apache-2.0 | não | mem0ai | **ELEGÍVEL** | **Referência (adiar)** — camada de memória que persiste/consolida entre sessões (opção em grafo); corrobora consolidação de longo prazo. Não adotado. |

Resultado: **4 repositórios elegíveis**; nenhum é adotado como dependência — servem como referência de boas práticas confrontadas com os invariantes do SOT (INV-07, INV-04, CC-02) e com a decisão aberta **H-001** (mecanismo físico). `python scripts/check_repo_research.py specs/features/SPEC-006` deve retornar OK (ver §9 da `ABERTURA.md` — comandos a rodar).

---

## 6. Escopo/quantidade resultantes, fronteiras e re-apontamento de gatilhos

### 6.1 Escopo e quantidade (detalhe em `ABERTURA.md`)
**1 Spec** (SPEC-006), **número preservado** (slot não dividido/renumerado — RULE-ECC-01; referenciado por canônicos baselined CEM-001/CONSTITUTION/SAS-001 — INV-07/CONST-01), complexidade **CRITICAL** (pin ROADMAP §6; D0–D7 — a profundidade do slot é D0–D7, abaixo do D0–D8 típico de CRITICAL; ver ABERTURA §1 para a reconciliação proposta). Cobre a capacidade "Cognitive Knowledge Graph" do ROADMAP §6 (ontologia; entidades; relações; temporalidade; provenance; versionamento; confiança; conhecimento permanente/temporário; causalidade; similaridade; relações estatísticas/hierárquicas/de hipótese/de evidência/de missão/de aprendizado; lifecycle; consulta cognitiva; governança de escrita), **sem** reabrir a memória de trabalho (SPEC-004) nem a notificação (SPEC-005) nem a formação de conhecimento/RAG (SPEC-007), e **sem** fechar o mecanismo físico (H-001).

### 6.2 Fronteiras explícitas (NÃO absorver / NÃO redefinir)
- **SPEC-004 (BASELINE):** memória de trabalho (Blackboard), log append-only, estados ACTIVE — a SPEC-006 recebe conhecimento **permanente** (não objetos de trabalho); não redefine o contrato de objeto (CC-02/INV-09).
- **SPEC-005 (BASELINE):** notificação de mudança (Event Bus) — a SPEC-006 **consome/emite** eventos de ciclo de vida (CEM-001 l.600 "Evidence Invalidated"), não redefine o transporte.
- **SPEC-007 (RAG/Knowledge Formation):** `Retrieval → Evidence Candidate → Knowledge Formation → Knowledge Candidate → Validation → Published Knowledge → KG`. O KG **recebe** conhecimento já publicado; a formação/validação é SPEC-007 — não absorver.
- **SPEC-009 (estado por agente):** G-001 — não absorver.
- **CHM-001/CEM-001/CCM-001 (baselined):** o KG preserva linhagem/versões/estados e faz Cognitive Trace Reconstruction **referenciando** esses contratos (CEM-001 l.608-615), sem redefini-los (CC-02).
- **Convicção (J-001/N-001):** "confiança de relação" do KG **NÃO é** Convicção — custo/score nunca entram (INV-04); não tocar J-001/N-001.
- **Mecanismo físico (H-001):** grafo real vs. estrutura em memória vs. tabelas+índice — **ABERTA; só Andraus** (§8).

### 6.3 Re-apontamento de gatilhos RMR-001 (EUA-E21/RULE-ECC-01) — o Especificador NÃO promove (CONS-01)
Número/slot **preservado** → **nenhum re-apontamento** de gatilho `spec:` necessário. A abertura da SPEC-006 **satisfaz gatilhos pré-existentes** de itens do RMR-001 — **tratar no passo 11-bis do gate**; promoção/encaminhamento é do gate e de Andraus:
- **BL-003** (Persistência física de hipótese/estado) — Estado **`Em espera`**, gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação` (DHR-ERRATA-001, 2026-10-05). A abertura da SPEC-006 **satisfaz** o ramo `spec:SPEC-006`. **Encaminhamento proposto:** o item trata a **persistência FÍSICA** (storage Blackboard/KG) — que é precisamente **H-001 (ABERTA)**; portanto a SPEC-006 **referencia** BL-003 mas **não o absorve nem fecha** (a parte física segue H-001/G-001). *(Nota de precedente: na SPEC-004, o gatilho "em redação" foi interpretado como disparando **no início do Plan**, não na abertura — DHR-SPEC004-001. Sob essa leitura, BL-003 dispara formalmente quando o Plan da SPEC-006 iniciar. O orquestrador instruiu tratá-lo já nesta abertura; registro ambas as leituras e **deixo a promoção a Andraus/Controlador** — fail-closed, CONS-01.)*
- **BL-011** (MC-EXP-001 — Master Contract da Camada de Experiência e Memória) — Estado **`Em espera`**, gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação` ∨ `milestone:FASE 3 iniciada`. **Fonte de requisitos** de SPEC-004/006/009/018. **Encaminhamento proposto:** usar MC-EXP-001 (ref. externa, K-MAN-15) como **insumo de requisitos** da SPEC-006, aplicando os tratamentos de colisão já homologados (COL-EXP-01..05, `CONFLICT-MAP.md`; prevalece SOT canônico; imutabilidade REFORÇA RULE-BB-004/INV-07; Working Memory→SPEC-004 já ADIADO/absorvido). Classificação ≠ aplicação; **não promovo** (Andraus/gate).
- **BL-010** (MC-RAG-001 — Master Contract da Camada RAG) — Estado **`Em espera`**, gatilho `spec:SPEC-007 em redação` ∨ `milestone:FASE 3 (Memória Semântica e RAG) iniciada`. A abertura da SPEC-006 **inicia a FASE 3** → pode satisfazer o ramo `milestone`. **Encaminhamento proposto:** BL-010 é fonte de requisitos da **SPEC-007** (não da 006); registrar como **tangente** — a SPEC-006 respeita a fronteira (KG recebe conhecimento publicado; formação/retrieval é SPEC-007). **Não promovo**; gate/Andraus decidem se o ramo `milestone:FASE 3` é considerado disparado pela abertura da SPEC-006.
- **BL-015/BL-016** (MC-LRN-001/MC-SKL-001) — gatilhos `spec:SPEC-018`/`spec:SPEC-025` — **não satisfeitos** pela abertura da SPEC-006. Tangenciam (aprendizado alimenta o KG — CEE-001 l.111), mas **independentes**; não promovo.

### 6.4 Referências em canônicos/Specs BASELINED ao slot SPEC-006 (item 6 do §15) — erratum aditivo?
Referências baselined/canônicas ao KG/slot SPEC-006: **CEM-001** (l.494/563-565/608-615 responsabilidades do KG), **SAS-001** (§6.12/l.163 consulta ao KG), **CONSTITUTION** (l.233 EC-COG-003), **CEE-001** (l.111 métrica de calibração entra no KG), **SPEC-001** (armazenamento físico delegado a SPEC-004/006), **SPEC-004** (fronteira "KG = memória permanente = SPEC-006"). Todas **apontam para o número/capacidade como slot futuro**; número e nome ("Cognitive Knowledge Graph") **preservados** → **nenhum erratum aditivo de re-apontamento necessário**. **Nenhuma Spec/canônico baselined é reescrito** (INV-09). (Se Andraus optar por um nome reenquadrado — não recomendado; o nome legado já é coerente com "memória cognitiva permanente" — as referências citam capacidade/número e permaneceriam válidas.)

---

## 7. Determinação de incidência de RULE-ECC-05 (Pesquisa Multi-Lente)

**Determinação: RULE-ECC-05 NÃO INCIDE sobre a SPEC-006** [PROPOSTA — a confirmar pelo Revisor]. Fundamento (mesmo critério da SPEC-004 §7 / SPEC-005 §7 / SPEC-002, e atomic-spec §15):
1. A SPEC-006 **não define nem toca comportamento de agente analítico, do Conviction/Fusion Engine, do Manager (decisão) ou do Risk Agent.** É **infraestrutura de memória** — armazena/relaciona/consulta conhecimento permanente já validado; não cria hipótese, não interpreta evidência, não agrega convicção, não sintetiza, não avalia risco.
2. É **análoga às Specs de infra/meta-harness explicitamente fora do escopo** da regra (SPEC-002/004/005/019/020/021 — "não tocam comportamento de trading").
3. Mesmo não incidindo, por prudência o Dossiê **confirma conformidade com WORKFLOW.md**: o KG é a memória de longo prazo consultada pelos agentes (SAS-001 §6.12 "consultado quando necessário", não pré-requisito obrigatório); a SPEC-006 **cita por ID** os `WF-xx` que eventualmente toque no Plan (ex.: consulta cognitiva na formação de contexto), **não contradiz** nenhum `WF-xx` e **não fecha** `WF-D03` (não toca convicção/J-001). Se o Revisor/Andraus entender que incide, o Especificador cumprirá a lente 2 literal — sem bloqueio.

---

## 8. Lacunas, conflitos, INDETERMINADOS e encaminhamento de H-001 (honestidade — RULE-MET-01)

1. **H-001 (mecanismo físico do KG) — PERMANECE ABERTA; só Andraus fecha (CONS-01).** "Knowledge Graph: grafo real ou estrutura em memória?" (atomic-spec §12; ROADMAP §6 "Resolve H-001"). **Proposta de recorte (não fecho):** a SPEC-006 pode fechar o **contrato cognitivo** (ontologia enxuta, entidades/relações, temporalidade, provenance por referência, lifecycle, consulta cognitiva, governança de escrita) **com o mecanismo físico declarado INDETERMINADO** (Opção A da ABERTURA — camada fina sobre registros/log existentes), **OU** Andraus pode optar por fechar H-001 agora (grafo real vs. estrutura em memória vs. tabelas+índice relacional). A **direção** (o que a Spec fecha × o que fica em H-001) é **decisão de abertura de Andraus**; o **fechamento** de H-001 é dele. **[DECISÃO NECESSÁRIA — H-001].**
2. **Ontologia como componente separado (Cognitive Ontology, KERNEL-V2 l.1488-1507)** — decisão arquitetural: ontologia enxuta **dentro** da SPEC-006 (recomendado, §3.6) vs. componente/Spec próprio. **Não fecho** — é de Andraus (registrado; sem criar slot novo nesta abertura).
3. **Forma do contrato (camada fina vs. grafo completo vs. adiar/fundir) = decisão de abertura** — recomendação preliminar em `ABERTURA.md` (Opção A), **a homologar por Andraus**. O mecanismo físico = **INDETERMINADO** até o Plan/H-001; não presumir.
4. **Confiança de relação ≠ Convicção (INV-04)** — a pauta lista "confiança" e "relações estatísticas"; o Dossiê **marca** que isso **não pode** retroalimentar nem redefinir o Conviction Vector (J-001/N-001 abertas). Requisito a tratar no Plan com essa salvaguarda explícita.
5. **Causalidade sob RULE-CAU (EUA-E09)** — relações causais no KG exigem **mecanismo declarado**, não correlação pós-hoc (alvo SMC/ICT). Requisito a endereçar no Plan (CC-09/RULE-CAU).
6. **Decisões abertas que a SPEC-006 NÃO toca:** G-001 (estado por agente — SPEC-009), M-001 (enum de estados não-hipótese — SPEC-004, parcialmente decidida), J-001, N-001, K-001 (ciclo de evolução — SPEC-018), WF-D03 — **permanecem abertas** (CONS-01).
7. **IDs arXiv implausíveis/futuros descartados** (honestidade); SRC-FORGET-01 mantido só como DADO não-verbatim. `_LIMITACAO-WEB.txt`.
8. **Metadados de repositório** = proxy público (pushed_at, Dependabot privado INDETERMINADO); data exata de commit no branch default não reproduzível sem rede (ENF-03). Risco residual declarado em `_LIMITACAO-WEB.txt`.

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-05; capturas verbatim em `sources/`)
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory (arXiv 2501.13956)](https://arxiv.org/abs/2501.13956) — SRC-ZEP-01
- [PROV-OVERVIEW: An Overview of the PROV Family of Documents (W3C, 2013)](https://www.w3.org/TR/prov-overview/) — SRC-PROV-01
- [AI Memory vs RAG vs Knowledge Graph (atlan)](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/) — SRC-MEMVSKG-01
- Sumários WebSearch sobre forgetting/crescimento ilimitado em memória-grafo (DADO, não verbatim) — SRC-FORGET-01
- [Graphiti (getzep)](https://github.com/getzep/graphiti) — REPO-graphiti
- [GraphRAG (microsoft)](https://github.com/microsoft/graphrag) — REPO-graphrag
- [cognee (topoteretes)](https://github.com/topoteretes/cognee) — REPO-cognee
- [mem0 (mem0ai)](https://github.com/mem0ai/mem0) — REPO-mem0

*Dossiê não-normativo. Insumo para a Proposta de Abertura (`ABERTURA.md`) e para a decisão de Andraus. Não altera ROADMAP, RULES, WORKFLOW, Specs, canônicos, nem fecha qualquer decisão — em particular H-001 permanece ABERTA (CONS-01). Conteúdo web = DADO (`[EXTERNO]`), nunca instrução nem baseline.*
