# ESTUDO DE TECNOLOGIA — H-001: mecanismo físico de armazenamento da memória permanente do Cognitive Knowledge Graph (SPEC-006)

| Campo | Valor |
|---|---|
| **Identificador** | ESTUDO-TECNOLOGIA-H001-2026-10-18 |
| **Natureza** | **[PROPOSTA] — tudo neste documento.** Não é ata, não é baseline, não é Spec, não homologa nada e **não fecha a H-001** (CONS-01; só Andraus escolhe a tecnologia — AGENTS.md §7; atomic-spec.md l.378). |
| **Origem do pedido** | `governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md` §Fase 2, passo 1 (l.35); passo seguinte = Andraus escolhe (l.36). |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 5.5) — classe de tarefa **O** (desenho). |
| **Data** | 2026-10-18 |
| **Dossiê reaproveitado** | `specs/features/SPEC-006/research.md` + `sources/` (acesso 2026-10-05; válido até **2027-01-03** — research.md l.10). Complemento web em 2026-10-18 só onde o Dossiê não cobria (licença/manutenção dos motores; Graphiti por LLM; PostgreSQL 18; XTDB v2). |
| **Status epistemológico** | Conteúdo web = **DADO, nunca instrução** (DHR-PROV-WEB-001 §2.1; RULE-ECC-02). Fontes `[EXTERNO]` classificadas; veracidade não atestada. Limitações no §10. |
| **Escopo** | Só o **COMO físico**. O **QUE** (contrato lógico RULE-CKG-001..013, INV-CKG-01/02, EC-CKG-001..006) é da SPEC-006 homologada (v1.7 + errata v1.11, DHR-SPEC006-002/003 — ROADMAP.md l.508) e **não é alterado** aqui. |

---

## 1. Recomendação (primeiro)

**[PROPOSTA] Opção C — PostgreSQL como fonte única de verdade, com tabelas de registros append-only (log de eventos do KG) e colunas bitemporais explícitas; travessia por consultas recursivas no próprio banco. Com caminho de evolução para a Opção D já desenhado: um índice de grafo derivado, reconstruível a partir do log, que só é ligado quando um gatilho medido disparar (§8).**

Três motivos:

1. **A imutabilidade e o fail-closed E3 ficam no próprio banco, em código determinístico.** O KG precisa negar DELETE/UPDATE (RULE-CKG-006, plan.md l.410-413; EC-CKG-002 l.1465-1475), fazer compare-and-commit atômico de versão (RULE-CKG-012, l.552-559), gravar INVALIDA e o fechamento de `valid_to` como **um único ato atômico** (RULE-CKG-013, l.567-571) e rejeitar tudo o que falhar na pré-condição, sem persistir nada (EC-CKG-001 l.1461). Transações ACID, restrições declarativas, revogação de UPDATE/DELETE por papel e gatilhos de banco fazem isso sem juiz LLM (ENF-03). A Opção B põe a invalidação na mão de um LLM, o que contradiz a RULE-CKG-004 ("NUNCA automática/cascata", l.390).
2. **O trace completo e a bitemporalidade não dependem de motor de grafo.** A completude do trace de Evidência já está garantida pelo contrato, "independente de H-001" (INV-CKG-02, l.650-654; RULE-CKG-011, l.539-543). O fecho transitivo de `DERIVA_DE` sai de uma consulta recursiva sobre a mesma base onde está a verdade. `valid_from`/`valid_to`/`recorded_at` são colunas explícitas (RULE-CKG-004, l.394-395); `formulated_at` é derivado da 1ª versão da cadeia `supersedes` (RULE-CKG-008, l.433-434), uma visão e não um campo do payload. A H-001 só deixa aberta a **eficiência** da consulta multi-salto ampla (RULE-CKG-011 l.542; EC-CKG-006 l.1521), e isso o índice derivado da Opção D resolve depois, sem migrar a verdade.
3. **Menor risco de licença, de manutenção e de lock-in, sem perder Eficácia.** Entre os candidatos de grafo nativo, o Memgraph Community está sob BSL e o FalkorDB sob SSPL (fora da lista de licenças da régua Equilibrada — RULES.md l.500-502). O Kùzu foi **arquivado em 2025-10-10**, e o próprio Graphiti já o marca como "deprecated" (§3.2). O Neo4j Community é GPLv3, com recursos de governança no Enterprise fechado. O PostgreSQL é maduro, usa SQL padrão e já é a família estudada pelo SOT para a notificação da SPEC-005 (`specs/features/SPEC-005/sources/SRC-NOTIFY-01.txt` l.12-13, LISTEN/NOTIFY). Sob escritor único por workspace e VPS única (research.md l.79-80), um motor de grafo dedicado é provável over-engineering. Pela ordem dos 4Es, Eficácia vem antes de Economicidade (AGENTS.md l.128; CONSTITUTION.md l.176-178), e aqui as duas apontam para o mesmo lado.

> **Ressalva honesta (§9, incerteza 2):** a licença do PostgreSQL (*PostgreSQL License*, permissiva, estilo BSD/MIT) **não está nominalmente** na lista fechada da régua Equilibrada (RULES.md l.501-502), e o projeto não é hospedado no GitHub/GitLab (lá há só um espelho). Tratá-la como "BSD-equivalente" é **[INFERÊNCIA]**. Enquadrar a régua aqui é **[DECISÃO NECESSÁRIA]** de Andraus.

---

## 2. Matriz de decisão

### 2.1 Critérios eliminatórios (passa/falha — antes dos pesos)

Um critério eliminatório não entra na soma: quem falha sai, qualquer que seja a nota. Motivo: Conformidade Constitucional fica acima de Eficácia (CONSTITUTION.md l.176) e não pode ser comprada com pontos de custo.

| ID | Critério eliminatório | Âncora |
|---|---|---|
| X1 | Permite **impor** "nada deletado/mutado" (não só convenção) | INV-07 (atomic-spec.md l.407); RULE-CKG-006 (plan.md l.410); RULE-BB-004 (RULES.md l.324) |
| X2 | A decisão de escrita/invalidação é **determinística** (sem LLM como gate) | ENF-03; RULE-CKG-004 l.390 ("NUNCA automática"); RULE-CKG-008 l.465-466 (gate verifica presença, não veracidade) |
| X3 | O KG **não faz** formação/extração/retrieval | RULE-CKG-010 l.483 ("O KG NÃO faz formação/extração/retrieval") |
| X4 | Sem capacidade de emitir ordem / efeito para execução | INV-05 (atomic-spec.md l.405) |
| X5 | Componente adotado passa na régua Equilibrada ou tem enquadramento decidido | RULE-ECC-06 (RULES.md l.498-512) |

| Opção | X1 | X2 | X3 | X4 | X5 | Resultado |
|---|---|---|---|---|---|---|
| A — property graph nativo (representante elegível: Neo4j CE) | passa com imposição na aplicação + papéis (§4.A) | passa | passa | passa | Neo4j: passa provisório. Memgraph/FalkorDB/Kùzu: **falham** | **Segue** (só Neo4j CE ou fork elegível) |
| B — grafo temporal Graphiti/Zep (como engine) | passa (invalida sem apagar) | **falha** (invalidação por chamada LLM — §3.2) | **falha** (ingestão por extração LLM) | passa | passa no Graphiti; o backend herda A | **Eliminada como mecanismo**; fica como referência de enquadramento temporal (já era assim: research.md l.68) |
| C — relacional (PostgreSQL) + log append-only | passa (REVOKE + gatilhos; resíduo de superusuário — R3) | passa | passa | passa | **[DECISÃO NECESSÁRIA]** (licença fora da lista nominal) | **Segue** |
| D — híbrido (C como verdade + índice de grafo derivado) | passa (o índice não é verdade) | passa | passa | passa | herda C + o índice escolhido | **Segue** |
| E — banco imutável bitemporal nativo (XTDB v2) — **acrescentada** | passa com ressalva (XTDB oferece apagamento por conformidade, que teria de ser bloqueado) | passa | passa | passa | passa provisório (MPL-2.0) | **Segue** |

### 2.2 Pesos (soma = 100) e justificativa

| # | Critério | Peso | Por que esse peso |
|---|---|---|---|
| 1 | Imutabilidade/versionamento monotônico imposto | 15 | INV-07 + EC-CKG-002 E3; perda de histórico é irreversível (l.1472) |
| 2 | E3 fail-closed na escrita (atomicidade, compare-and-commit, restrições, autenticação do escritor) | 15 | EC-CKG-001/003/004/005 são E3 (l.1460/1484/1496/1508); "KG publicado → E3 mínimo" (atomic-spec.md l.238) |
| 3 | Trace completo / Cognitive Trace Reconstruction | 12 | Obrigação de canônico BASELINED (CEM-001 l.562-565, l.608-615); RULE-CKG-011 |
| 4 | Bitemporalidade (`valid_from`/`valid_to`/`recorded_at`; `formulated_at` derivado) | 10 | RULE-CKG-004 l.394; RULE-CKG-008 l.433; RULE-CKG-013 cond. (iii) |
| 5 | Auditoria / proveniência por referência | 10 | RULE-CKG-005 l.399-408 (`computed_by`≠`writer_id`); EC EVIDENCE |
| 6 | Consulta cognitiva (travessia, profundidade, eficiência) | 8 | É requisito (RULE-CKG-011), mas a eficiência ampla é INDETERMINADA por desenho (l.542; RULE-UNC-01/02, RULES.md l.691-692). Eficiência não sobe acima de Eficácia |
| 7 | Licença / maturidade / segurança | 10 | RULE-ECC-06; risco de dependência morta (Kùzu) é risco de Eficácia no BUILD |
| 8 | Portabilidade / lock-in | 7 | Trocar o motor sem reescrever a verdade preserva INV-07 a longo prazo |
| 9 | Exigência do BUILD (componentes, competência, testes) | 7 | Efetividade: o contrato precisa ser implementável e testável (L3, plan.md l.13) |
| 10 | Custo operacional | 6 | Economicidade: último degrau dos 4Es (AGENTS.md l.128) |

Agrupamento pelos 4Es: Conformidade/Eficácia (1-5) = **62**; Efetividade (6, 9) = **15**; risco de sustentação (7, 8) = **17**; Economicidade (10) = **6**. Os pesos são [PROPOSTA] e estão expostos para Andraus recalibrar.

### 2.3 Notas (1 = fraco … 5 = forte) e total ponderado (0-100)

| Critério (peso) | A Neo4j CE | B Graphiti | C PostgreSQL+log | D C+índice derivado | E XTDB v2 |
|---|---|---|---|---|---|
| 1 Imutabilidade (15) | 2 | 3 | 5 | 5 | 4 |
| 2 E3 fail-closed (15) | 3 | 1 | 5 | 5 | 3 |
| 3 Trace completo (12) | 5 | 4 | 4 | 5 | 3 |
| 4 Bitemporal (10) | 2 | 5 | 4 | 4 | 5 |
| 5 Auditoria/proveniência (10) | 3 | 2 | 5 | 5 | 4 |
| 6 Consulta cognitiva (8) | 5 | 5 | 3 | 4 | 3 |
| 7 Licença/maturidade/segurança (10) | 3 | 3 | 5 | 4 | 4 |
| 8 Portabilidade/lock-in (7) | 3 | 2 | 5 | 4 | 2 |
| 9 Exigência do BUILD (7) | 3 | 2 | 4 | 3 | 2 |
| 10 Custo operacional (6) | 3 | 2 | 5 | 4 | 3 |
| **Total ponderado** | **63,0** | **57,6** (eliminada) | **91,0** | **89,0** | **68,2** |

Cálculo: Σ(peso × nota) / 5. Exemplo para C: (75+75+48+40+50+24+50+35+28+30)/5 = 91,0.

**Sensibilidade [INFERÊNCIA]:** C e D diferem por 2 pontos. D passa C se o peso de "Consulta cognitiva" subir para **mais de 13**, tirando do "Custo operacional". Ou seja, D só vence quando a eficiência de travessia pesa mais que o dobro do que o contrato hoje exige, e é exatamente isso que o gatilho G2 (§8) mede. Nenhuma recalibração razoável dos pesos põe A, B ou E acima de C ou D: todas perdem 2 ou mais pontos nos critérios 1-2, que somam 30.

**Notas são juízo [INFERÊNCIA], não medição.** Nenhuma nota vem de benchmark executado. Não há número de latência ou throughput aqui (RULE-MET-01; CC-09: sem falsa precisão).

---

## 3. Fontes e pesquisa complementar (2026-10-18)

### 3.1 Classificação das fontes

| ID | Fonte | Classe | Uso |
|---|---|---|---|
| Dossiê SPEC-006 | research.md + sources/ (2026-10-05) | — (interno, não-normativo) | Base: KG = memória cognitiva, não "banco de grafos" (research.md l.26, l.32); "adiar grafo completo" (l.79-80); Graphiti como referência, não dependência (l.68, l.120) |
| W-GRAPHITI-README | github.com/getzep/graphiti | Prática | Backends e dependência de LLM (§3.2) |
| W-ZEP-BLOG | getzep.com/blog/beyond-static-knowledge-graphs | Prática / Opinião do fornecedor | Invalidação de arestas por LLM (§3.2) |
| W-KUZU | github.com/kuzudb/kuzu | Evidência | Repositório arquivado |
| W-NEO4J | github.com/neo4j/neo4j | Prática | Licença CE GPLv3 / Enterprise fechada |
| W-MEMGRAPH | github.com/memgraph/memgraph | Prática | Licença BSL/MEL |
| W-FALKOR | github.com/FalkorDB/FalkorDB | Prática | Licença SSPLv1 |
| W-AGE | github.com/apache/age | Prática | Extensão de grafo (openCypher) para PostgreSQL 11-18 |
| W-XTDB | github.com/xtdb/xtdb + xtdb.com (blog de lançamento v2) | Prática | Banco bitemporal imutável, MPL-2.0 |
| W-PG18 | Fontes secundárias (neon.com, depesz.com, betterstack) | Prática (secundária) | Restrições temporais `WITHOUT OVERLAPS`/`PERIOD` no PostgreSQL 18 |

### 3.2 Achados carregados (trechos literais curtos)

A ferramenta de captura devolveu trechos de no máximo ~125 caracteres. Por isso **não** cumprem o mínimo de 100 caracteres de uma captura RULE-ECC-04 em todos os casos (§10).

- **Graphiti invalida por LLM.** [EXTERNO, W-ZEP-BLOG, acesso 2026-10-18] *"We make an LLM call for each new edge using an invalidation prompt, providing existing similar edges as context."* e *"We mark conflicting edges as 'expired' by setting the `expired_at` field on the Edge property."* **Confronto SOT:** a invalidação no KG é "ATO AUTORIZADO (CKG-009), NUNCA automática/cascata" (plan.md l.390), e a colisão é **marcada, não resolvida** (RULE-CKG-013 l.577). Uma invalidação decidida por LLM falha X2. **Rejeitar como mecanismo. Adaptar** só o enquadramento temporal, que já estava adaptado (research.md l.68).
- **Graphiti exige LLM e grafo de terceiros.** [EXTERNO, W-GRAPHITI-README] Graphiti *"defaults to using OpenAI for LLM inference and embedding"*; requisitos *"Neo4j 5.26 / FalkorDB 1.1.2 / Amazon Neptune Database Cluster"*; *"Kuzu is deprecated and will be removed in a future release — the upstream Kuzu project is no longer maintained."* **Confronto:** adotar Graphiti é adotar A (ou um backend SSPL/proprietário) **mais** um pipeline de extração por LLM. A extração pertence à SPEC-007, não ao KG (RULE-CKG-010 l.483). **Rejeitar.**
- **Kùzu arquivado.** [EXTERNO, W-KUZU] *"This repository was archived by the owner on Oct 10, 2025. It is now read-only."* Há um fork comunitário (LadybugDB, MIT), só em fonte secundária, **não verificado** → INDETERMINADO. **Rejeitar** pela régua (arquivado).
- **Neo4j.** [EXTERNO, W-NEO4J] *"Neo4j Community Edition is an open source product licensed under GPLv3."* / *"Neo4j Enterprise Edition includes additional closed-source components"*. **Confronto:** elegível como CE. Recursos de governança/restrição fora do CE são **[INFERÊNCIA a verificar no BUILD]**. Não confirmei a lista exata nesta sessão.
- **Memgraph / FalkorDB.** [EXTERNO] *"Memgraph Community is available under the BSL license."* / FalkorDB *"Licensed under the Server Side Public License v1 (SSPLv1)."* BSL e SSPL estão fora da lista da régua (RULES.md l.501-502) → **NÃO ELEGÍVEIS**.
- **Apache AGE.** [EXTERNO, W-AGE] *"Apache AGE is an extension for PostgreSQL that enables users to leverage a graph database on top of the existing"* … (truncado pela ferramenta). Fontes secundárias sugerem que o pacote para PostgreSQL 18 vem de um *release candidate*. **Status de release final INDETERMINADO.** Candidato de índice em D, não de verdade.
- **XTDB v2.** [EXTERNO, W-XTDB] *"'Bitemporal' - all data is accurately versioned as updates are made ('system' time), but it also allows you to separately"* … (truncado). O lançamento estável da v2 aparece datado de 2025-06-12 (sumário de busca — DADO, não verbatim). **Confronto:** é o casamento conceitual mais próximo com RULE-CKG-004, mas o ecossistema é JVM/Clojure, a compatibilidade SQL é parcial e a comunidade é menor (~3,1 mil estrelas). Ver também a ressalva de apagamento em X1.
- **PostgreSQL 18 — restrições temporais.** [EXTERNO, W-PG18, secundárias — DADO] `WITHOUT OVERLAPS` em chaves primárias/únicas e `PERIOD` em chaves estrangeiras (sobre tipos range). **Confronto:** é útil para chaves que **não** podem se sobrepor. Atenção: o contrato **admite** sobreposição entre relações contraditórias e as marca como colisão (RULE-CKG-013 cond. (iii), l.562-564). Usar `WITHOUT OVERLAPS` indiscriminadamente **rejeitaria** o que o contrato manda preservar. **Adaptar com cuidado** (§4.C).

### 3.3 Repositórios — régua Equilibrada (RULE-ECC-06), observação em 2026-10-18

| Repositório | Licença | Estrelas (aprox.) | Arquivado | Último commit ≤12m | Alertas graves | Veredito |
|---|---|---|---|---|---|---|
| getzep/graphiti | Apache-2.0 | 32,0 mil | não | sim (Dossiê: pushed_at 2026-10-04) | INDETERMINADO (proxy 0) | ELEGÍVEL (já no Dossiê) — referência, **não** mecanismo |
| neo4j/neo4j | GPL-3.0 | 17,3 mil | não | provável (ramo 2026.09 visível); data não confirmada | INDETERMINADO | ELEGÍVEL **provisório** |
| apache/age | Apache-2.0 | 4,9 mil | não | não confirmado | INDETERMINADO | ELEGÍVEL **provisório** |
| xtdb/xtdb | MPL-2.0 | 3,1 mil | não | não confirmado | INDETERMINADO | ELEGÍVEL **provisório** |
| memgraph/memgraph | BSL / MEL | 4,6 mil | não | — | — | **NÃO ELEGÍVEL** (licença) |
| FalkorDB/FalkorDB | SSPLv1 | 10,5 mil | não | — | — | **NÃO ELEGÍVEL** (licença) |
| kuzudb/kuzu | MIT | 4,0 mil | **sim (2025-10-10)** | — | — | **NÃO ELEGÍVEL** (arquivado) |
| PostgreSQL (git.postgresql.org; espelho github.com/postgres/postgres) | PostgreSQL License | — | — | — | — | **Régua não aplicável nominalmente → [DECISÃO NECESSÁRIA]** |
| SQLite (sqlite.org, Fossil) | domínio público | — | — | — | — | idem |

A API pública do GitHub respondeu 403 nesta sessão, então os metadados vêm da página HTML, por WebFetch mediado por modelo. Nada foi instalado, clonado ou executado. **Nenhuma captura `sources/REPO-*.txt` foi criada**, porque o escopo desta tarefa é um único arquivo (§10).

---

## 4. Detalhe por opção

### A — Property graph nativo (Neo4j CE; Memgraph e Kùzu eliminados)

- **Imutabilidade:** DELETE/SET de nó e propriedade são primitivas nativas. Impor INV-07 exige uma camada de serviço e, se houver, controle de papéis; no CE isso é **[INFERÊNCIA a verificar]**. Versão vira nó/aresta extra.
- **E3:** transações ACID existem. Restrições ricas (existência/tipo de propriedade) podem depender da edição (**a verificar**). A matriz §D2.1 e os ~40 códigos de rejeição ficam quase todos na camada de serviço.
- **Trace / consulta:** é o ponto forte. Travessia de profundidade variável é nativa (Cypher/GQL).
- **Bitemporal:** não é nativo. Fica por convenção de propriedades.
- **BUILD exige:** serviço JVM separado, modelagem de versões em grafo, camada de serviço que faça todo o fail-closed, backup/restauração próprios, testes de imutabilidade fora do banco.
- **Riscos:** imutabilidade por convenção (R1); dependência de recursos Enterprise; uma segunda tecnologia de persistência ao lado do log da SPEC-004 (duas verdades — viola o espírito de "transporte ≠ fonte de verdade", AGENTS.md l.140).

### B — Grafo temporal estilo Graphiti/Zep

- **Ponto forte:** modelo temporal com `valid_at`/`invalid_at` + `expired_at` (citações do §3.2) quase igual ao bitemporal da RULE-CKG-004.
- **Por que sai:** a escrita é guiada por LLM (extração de entidades + invalidação por prompt). Falha X2 e X3. Também carrega um provedor externo de LLM por padrão (dados sensíveis saindo da VPS) e um backend de grafo que é A ou um não elegível.
- **O que se aproveita:** o vocabulário temporal e o princípio "invalidar, não deletar". Isso já está no contrato (research.md l.68; plan.md l.394-396).

### C — PostgreSQL + log append-only (RECOMENDADA)

- **Forma [PROPOSTA de BUILD, não regra]:** tabelas `node_record` / `relation_record` / `canonical_state_transition` / `collision_record` / registros de invalidação, **só INSERT**. Estado corrente = **visões** (projeção derivada — RULE-CKG-012 l.549). `formulated_at` = visão sobre a 1ª versão da cadeia `supersedes`. `recorded_at` = relógio do banco, nunca do payload. `outcome_timestamp` = derivado do `recorded_at` do registro apontado (RULE-CKG-008 l.426-427).
- **Imutabilidade:** `REVOKE UPDATE, DELETE, TRUNCATE` dos papéis de aplicação + gatilho que rejeita UPDATE/DELETE com `IMMUTABILITY_VIOLATION`. Resíduo: superusuário/DBA (R3).
- **E3:** uma transação por ato de escrita. INVALIDA + fechamento de `valid_to` no mesmo commit (A-11). Unicidade de `(chave, version)` + checagem de `expected_version` → `VERSION_CONFLICT` / `VERSION_FORK_FORBIDDEN`. Validação da matriz §D2.1 e dos campos causais em função/gatilho determinístico. Banco indisponível ⇒ escrita rejeitada, sem fila local que "comita depois" (EC-CKG-001 l.1461). Identidade do escritor = sessão autenticada (papel do banco ou identidade de serviço, reusando CBP-014), nunca o payload (RULE-CKG-005 l.406-407; RULE-CKG-009 l.469-471).
- **Trace:** consulta recursiva sobre `DERIVA_DE`, incluindo SUPERSEDED/ARCHIVED (l.543). Aciclicidade (`LINEAGE_CYCLE`) checada na escrita. A completude independe do desempenho.
- **Bitemporal:** colunas explícitas; `valid_to = null ≡ +∞` (l.395); `CHECK (valid_to IS NULL OR valid_to >= valid_from)` → `INVALID_TIME_WINDOW`. `WITHOUT OVERLAPS` **só** onde o contrato proíbe sobreposição, nunca entre relações contraditórias (§3.2).
- **Buffer `PENDING_ANCESTOR`:** o contrato manda que ele fique **fora do armazenamento do KG** (l.657-658) e diz que sua durabilidade é H-001. Proposta: esquema/tabela separado, não exposto às consultas do KG e não contado como registro do KG. O timeout continua [DECISÃO NECESSÁRIA] (l.659).
- **BUILD exige:** esquema SQL versionado; funções/gatilhos de validação; papéis; backup e restauração testados; testes de imutabilidade *no banco* (tentativa de UPDATE/DELETE deve falhar); o mesmo motor que a SPEC-004 usar para o log, se possível (§9, incerteza 1).
- **Riscos:** travessia multi-salto ampla mais lenta que um motor nativo (R4 → gatilho G2); lógica de validação extensa em SQL (R5).

### D — Híbrido (C como verdade + índice de grafo derivado)

- **Igual a C** na verdade e na escrita. Soma um **índice derivado**, reconstruível do log, que **nunca** recebe escrita direta. Candidatos: Apache AGE no mesmo PostgreSQL (status de release INDETERMINADO), projeção em memória no serviço de consulta ou Neo4j CE como réplica de leitura.
- **Regra de segurança [PROPOSTA de BUILD]:** toda consulta que precise de **completude** (trace de Evidência — RULE-CKG-011) pode ser respondida pela verdade se o índice estiver defasado. Defasagem detectável (marca d'água do último registro indexado); índice divergente é descartado e reconstruído, nunca "corrigido".
- **BUILD exige:** tudo de C + sincronização, reconstrução, verificação de consistência e um segundo componente para operar.
- **Riscos:** duas cópias (consistência eventual no índice); mais superfície operacional. Vale quando G2 disparar.

### E — Banco imutável bitemporal nativo (XTDB v2) — acrescentada pelo estado da arte

- **Ponto forte:** tempo de sistema + tempo de validade nativos, dados imutáveis, SQL com dialeto próprio. Conceitualmente muito alinhado à RULE-CKG-004/006.
- **Contras:** existe operação de apagamento físico para conformidade, que teria de ser bloqueada por política (X1 com ressalva) [INFERÊNCIA a verificar]. Restrições declarativas, recursão e transações multi-registro do jeito que A-11 exige = **INDETERMINADO**, não verificado. Ecossistema menor, compatibilidade SQL parcial (lock-in), armazenamento em object storage = mais peças na VPS.
- **Veredito:** registrar como alternativa. Reavaliar se G4 ou G5 dispararem.

---

## 5. Critérios obrigatórios — síntese com âncoras

| Critério | Âncora no repositório | Como C/D atende | Resíduo |
|---|---|---|---|
| Imutabilidade / INV-07 | atomic-spec.md l.407; plan.md l.410-413; EC-CKG-002 l.1465-1475; AGENTS.md l.127 | Só INSERT; REVOKE + gatilho; estado por visão | Superusuário (R3) |
| E3 fail-closed na escrita | EC-CKG-001..005 (l.1453-1511); RULE-CKG-009 l.469; atomic-spec.md l.238 | Transação única por ato; restrição/gatilho determinísticos; indisponível ⇒ REJECTED | Falso-DENY E3 continua CONDICIONAL até o limiar amostral (ENF-07, l.1461) — não muda com a tecnologia |
| Trace completo | CEM-001 l.562-565, l.608-615; RULE-CKG-011 l.539-547; INV-CKG-02 l.650-654 | Fecho recursivo de `DERIVA_DE` sobre a verdade | Eficiência ampla INDETERMINADA (RULE-UNC) |
| Bitemporal | RULE-CKG-004 l.394-395; RULE-CKG-008 l.433-434; RULE-CKG-013 l.562-564 | Colunas explícitas; `formulated_at` por visão; `recorded_at` pelo banco | `WITHOUT OVERLAPS` só onde o contrato proíbe sobreposição |
| Proveniência por referência | RULE-CKG-005 l.399-408; RULE-CKG-002 l.370-377 | Colunas de referência (ID+versão), `computed_by` e `writer_id` separados | Resolução do canônico depende dos stores CHM/CEM (BUILD) |
| Consulta cognitiva | RULE-CKG-011; EC-CKG-006 l.1513-1523; plan.md l.122 (RULE-UNC) | Consultas recursivas (C); índice derivado (D, após G2) | Sem número de latência (RULE-MET-01) |
| Auditoria | EC-CKG-* EVIDENCE; RULE-CKG-012 | Log append-only = trilha; rejeições registradas | Evidência de adulteração por DBA exige cadeia de hash (§7, R3) — seria regra nova = lote O |
| 4Es | AGENTS.md l.128; CONSTITUTION.md l.176-178 | Pesos 62/15/17/6 (§2.2) | — |
| INV-05 | atomic-spec.md l.405 | Armazenamento sem saída para execução; nenhuma opção emite ordem | — |
| Licença / maturidade / segurança | RULES.md l.498-512 | §3.3 | PostgreSQL fora da lista nominal → [DECISÃO NECESSÁRIA] |
| Portabilidade / lock-in | — | SQL padrão; índice trocável | Funções PL/pgSQL são específicas do motor |
| Custo operacional | research.md l.79-80 (VPS única) | Um serviço de banco; sem chamada LLM por escrita | — |

---

## 6. O que NÃO muda no contrato lógico da SPEC-006 (qualquer opção)

A SPEC-006 define o QUE; o mecanismo é o COMO (plan.md l.22, l.288). **Sob qualquer opção**, permanecem idênticos:

- RULE-CKG-001..013 e INV-CKG-01/02, com todos os códigos de rejeição (`IMMUTABILITY_VIOLATION`, `VERSION_CONFLICT`, `INVALID_TIME_WINDOW`, `CAUSAL_CORE_IMMUTABLE_IN_CHAIN`, `CONVICTION_HISTORY_UNDEFINED`, etc.).
- Os 6 Enforcement Contracts e seus níveis (E3 na escrita; E1 na leitura — l.1520), FAILURE-MODE fail-closed e o falso-DENY E3 CONDICIONAL (ENF-07).
- As 13 BASpecs, 13 EARS, 19 cenários e 23 ADV (contagens da v1.11, l.41).
- As fronteiras: KG ≠ Blackboard (SPEC-004); KG ≠ transporte (SPEC-005); KG não forma conhecimento (SPEC-007); confiança ≠ Convicção (RULE-CKG-007; INV-04); `conviction` negada por padrão (DHR-SPEC006-003 D2).
- As decisões abertas que a SPEC-006 não toca: G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, CKG-STRUCT-ORIGIN-001 e o timeout de `PENDING_ANCESTOR` (PLANO l.40; plan.md l.7).

**O que muda (só referência, tarefa mista do PLANO l.38):** onde hoje se lê "mecanismo físico INDETERMINADO — H-001 ABERTA" (plan.md l.5, l.22, l.24, l.117, l.246, l.288, l.333, l.342) e "durabilidade do buffer = H-001" (l.658), o texto passaria a citar a ata da escolha. **"Eficiência ampla = INDETERMINADO até H-001"** (l.542, l.1521) **não** vira número com a escolha: continua INDETERMINADO até medição no BUILD, agora ligada ao gatilho G2 em vez da H-001. Fazer essa troca de referência é classe M. Introduzir a cadeia de hash ou qualquer regra física nova é classe O e vai a Andraus antes.

---

## 7. Riscos residuais (sob a recomendação C → D)

| ID | Risco | Mitigação [PROPOSTA] | Resíduo |
|---|---|---|---|
| R1 | Imutabilidade burlada pela aplicação | REVOKE por papel + gatilho no banco (não só no serviço); teste de UPDATE/DELETE negado no CI do BUILD | Baixo |
| R2 | Divergência entre o log da SPEC-004 e o KG em motores diferentes | Usar o mesmo motor da SPEC-004 se compatível (incerteza 1) | INDETERMINADO até o BUILD da SPEC-004 |
| R3 | Superusuário/DBA altera registro sem deixar rastro | Separar papéis; backups imutáveis; **cadeia de hash por registro** como evidência de adulteração. Seria regra nova → lote O, decisão de Andraus | Médio enquanto não houver cadeia de hash |
| R4 | Travessia multi-salto ampla lenta | Gatilho G2 → índice derivado (D) | INDETERMINADO (sem medição) |
| R5 | Lógica de validação grande em SQL, difícil de testar | Validar em serviço determinístico + restrições mínimas no banco (defesa em profundidade); suíte de ADV-01..23 como testes | Médio |
| R6 | Escolha feita em spec-first envelhece | Cláusula de revisão por gatilho (§8) | Baixo |
| R7 | Régua de licença não cobre PostgreSQL/SQLite nominalmente | Decisão de enquadramento por Andraus | Aberto até a decisão |

---

## 8. Gatilhos de revisão da escolha [PROPOSTA — para constar da ata]

A escolha seria revista (não automaticamente revertida) quando qualquer um destes disparar:

- **G1 — início do BUILD da SPEC-006** (ou da SPEC-004, se ela fixar o motor do log antes): reconfirmar motor, versão e papéis.
- **G2 — eficiência de consulta:** consultas multi-salto (trace/histórico) excederem um limite de latência **a definir por Andraus com base em medição do BUILD** (sem número aqui — RULE-MET-01). Liga o índice derivado da D, sem mudar a verdade.
- **G3 — mudança de licença, arquivamento ou alerta grave** em qualquer componente adotado (reaplicar a régua RULE-ECC-06).
- **G4 — topologia:** mais de um escritor por workspace ou mais de uma máquina (quebra a premissa de research.md l.79-80).
- **G5 — exigência nova de canônico ou Spec** (SPEC-007 selo, SPEC-018/K-001, SPEC-009/G-001) que precise de consulta temporal cruzada ou de similaridade não atendível por C/D.
- **G6 — vencimento do Dossiê** (2027-01-03, research.md l.10) antes do BUILD: refazer a pesquisa de motores.

---

## 9. As duas maiores incertezas

1. **Qual motor a SPEC-004 usará para o log append-only do Blackboard.** Não encontrei escolha física na SPEC-004 (grep por PostgreSQL/SQLite em `specs/features/SPEC-004/plan.md` sem resultado). Se o log ficar em outro motor, C passa a ter duas tecnologias de persistência e o argumento de "uma verdade" enfraquece (R2). Isso não depende desta escolha, mas a afeta. [INDETERMINADO]
2. **Enquadramento de licença e régua para PostgreSQL/SQLite.** A régua Equilibrada lista licenças nominalmente e foi desenhada para repositórios GitHub/GitLab (RULES.md l.498-503). A *PostgreSQL License* e o domínio público do SQLite não estão na lista. Tratar como "BSD-equivalente / CC0-equivalente" é [INFERÊNCIA]; o enquadramento é **[DECISÃO NECESSÁRIA]** de Andraus.

Outras incertezas menores: recursos de restrição/RBAC do Neo4j CE não verificados; status de release final do Apache AGE para PG18; restrições e transações do XTDB v2; datas de último commit não confirmadas (API 403).

---

## 10. Limitações deste estudo (honestidade — RULE-MET-01)

1. A API pública do GitHub respondeu **403** nesta sessão. Os metadados vêm das páginas HTML por WebFetch (mediado por modelo). Data de último commit e alertas de segurança ficaram **INDETERMINADOS** para Neo4j, AGE e XTDB.
2. A ferramenta de captura limita citações literais a ~125 caracteres. Algumas citações do §3.2 têm menos de 100 caracteres e estão truncadas. Elas **não** satisfazem, sozinhas, a captura RULE-ECC-04.
3. Pelo escopo desta tarefa (um único arquivo novo), **nenhum** `sources/*.txt` foi criado e o `specs/features/SPEC-006/sources/_LIMITACAO-WEB.txt` **não** foi editado. Esta limitação fica registrada aqui. Se a ata ou a errata citar estas fontes como base, as capturas verbatim devem ser produzidas antes, por tarefa própria.
4. Os itens W-PG18 e o lançamento do XTDB v2 vêm de **sumários de busca/fontes secundárias** (DADO, não verbatim). Não sustentam alegação carregada sozinhos.
5. O fork LadybugDB (sucessor do Kùzu) aparece só em fonte secundária. Não foi verificado e não entra na matriz.
6. Nenhuma tecnologia foi instalada, executada ou medida. Todas as notas da matriz são juízo [INFERÊNCIA].
7. RULE-ECC-04/06 incidem formalmente sobre Dossiês de **Spec**. Este estudo é insumo de decisão (H-001), não Dossiê de abertura. Apliquei a régua por pedido do Orquestrador, como boa prática.

---

## Fontes `[EXTERNO]` (acesso 2026-10-18, exceto o Dossiê)

- Dossiê SPEC-006: `specs/features/SPEC-006/research.md` e `sources/` (acesso 2026-10-05)
- [getzep/graphiti (README)](https://github.com/getzep/graphiti)
- [Zep — Beyond Static Knowledge Graphs](https://www.getzep.com/blog/beyond-static-knowledge-graphs/)
- [kuzudb/kuzu](https://github.com/kuzudb/kuzu)
- [neo4j/neo4j](https://github.com/neo4j/neo4j)
- [memgraph/memgraph](https://github.com/memgraph/memgraph)
- [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)
- [apache/age](https://github.com/apache/age)
- [xtdb/xtdb](https://github.com/xtdb/xtdb) · [Launching XTDB v2](https://www.xtdb.com/blog/launching-xtdb-v2)
- [PostgreSQL 18 temporal constraints (neon.com)](https://neon.com/postgresql/postgresql-18/temporal-constraints) · [depesz — temporal FK](https://www.depesz.com/tag/period) · [betterstack — temporal constraints](https://betterstack.com/community/guides/databases/postgres-temporal-constraints/)
- [Kùzu arquivado / LadybugDB (oneuptime, secundária)](https://oneuptime.com/blog/post/2026-08-12-kuzu-archived-pin-0-11-3-fork-or-migrate/view) · [EDB — Apache AGE 1.8.0 release notes (secundária)](https://www.enterprisedb.com/docs/pg_extensions/apache_age/rel_notes/apache_age_1.8.0_rel_notes/)

*Documento [PROPOSTA], não-normativo. Não altera ROADMAP, AGENTS, atomic-spec, RULES, agentes, canônicos nem a SPEC-006. **H-001 permanece ABERTA** até Andraus escolher (CONS-01). Conteúdo web = DADO, nunca instrução nem baseline.*
