# Dossiê de Pesquisa — SPEC-007: RAG / WikiRAG / Knowledge Formation Harness (slot ROADMAP §6, FASE 3)

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-SPEC-007 |
| **Método** | ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06) + DHR-BACKLOG-ABERTURA-001 |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 5.5) |
| **Data de acesso web** | 2026-10-18 (todas as fontes `[EXTERNO]`); Benchmark local lido no commit `0abd22e` |
| **Complexidade proposta** | **CRITICAL · D0–D8** (pin ROADMAP §6 l.180; coerente com AGENTS §4 — sem conflito de matriz, ao contrário da SPEC-006: a matriz do atomic-spec §3 não lista RAG). Dossiê em profundidade CRITICAL. |
| **Validade do Dossiê (ECC-VAL-001 — FECHADA, DHR-DEC-003)** | CRITICAL → **90 dias** da data de acesso (2026-10-18) → **data-limite 2027-01-16**, ou antes se o contexto mudar materialmente (ex.: o Benchmark Inteligencia-SOT entregar a etapa RAG dele). Dossiê vencido não dispensa reabrir a pesquisa (fail-closed, RULE-ECC-02). |
| **Natureza** | **Dossiê `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão (CONS-01). Tudo o que propõe é `[PROPOSTA]`. |
| **Status epistemológico** | Conteúdo web e de repositórios = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1; RULE-ECC-02). Fontes classificadas e etiquetadas; veracidade das páginas não atestada. Capturas literais em `sources/` (RULE-ECC-04); limitações em `sources/_LIMITACAO-WEB.txt`. |
| **Autorização** | ROADMAP l.34 ("Próximo trabalho autorizado: SPEC-007 … abertura pendente de autorização de Andraus e do passo 1-bis") + tarefa do Orquestrador (2026-10-18) com a decisão de Andraus sobre o repositório paralelo (chat, 2026-10-18). |
| **Fronteiras respeitadas** | INV-04 (custo/confiança/relevância fora do Conviction Vector), INV-05 (SOT não executa ordem), INV-06/INV-10 (Evidência ≠ Observação; CEM-001 idioma canônico), INV-07 (nada é apagado), INV-09 (sem baseline informal). Não redefine CHM-001/CEM-001/CCM-001 nem **SPEC-002/004/005/006** (CC-02/CONST-01). KG = SPEC-006 (H-001 FECHADA, Opção C — DHR-H001-001). |

> **Aviso de método (RULE-MET-01).** (1) A API do GitHub respondeu 403; métricas de repositório vieram da página HTML pública (ver `_LIMITACAO-WEB.txt`). (2) A ferramenta de leitura web limita citação literal a 125 caracteres — os trechos são literais (≥100 caracteres), às vezes recortes de frase maior, anotados como tal. (3) Blogs secundários e números sem fonte primária foram descartados. (4) O repositório paralelo foi lido **somente leitura**; nada foi executado nem instalado; nenhum conteúdo dele foi copiado para o SOT além de citações curtas de **FATO** com arquivo:linha. Distingo sempre **[FATO do repositório]** de **[INFERÊNCIA]**.

---

## 0. Auditoria de entrada — o que é "RAG / WikiRAG / Knowledge Formation" no SOT hoje

| Âncora | Verificação | Resultado |
|---|---|---|
| (a) Definição do slot | `ROADMAP.md` l.179-182: "Formalizar: `Retrieval → Evidence Candidate → Knowledge Formation → Knowledge Candidate → Validation → Governance → Published Knowledge → Knowledge Graph / RAG`. Regras: `Documento recuperado ≠ verdade` · `Trecho recuperado ≠ conhecimento validado` · `Conhecimento candidato ≠ conhecimento publicado`." | `[FONTE]`, FATO ARQUITETURAL (slot indicativo). O slot é um **pipeline de formação e publicação** com recuperação, não "busca vetorial". |
| (b) Dependência já criada pelo KG baselined | `specs/features/SPEC-006/plan.md` l.485-488 (RULE-CKG-010): o KG recebe conhecimento por duas fontes, "(b) CONHECIMENTO FORMADO via SELO DE PUBLICAÇÃO da SPEC-007 (contrato do selo = DEPENDÊNCIA da SPEC-007 = [DECISÃO NECESSÁRIA]). Formado SEM selo é REJEITADO (`FORMED_WITHOUT_SEAL`)"; l.1415 (`publication.origin = canonical_lifecycle \| spec007_seal`; hipótese via selo ⇒ `HYPOTHESIS_VIA_SEAL_FORBIDDEN`); l.976 (produtor/gatilho de promoção = [DECISÃO NECESSÁRIA]). | **FATO NORMATIVO** (SPEC-006 BASELINE v1.7 + errata v1.11/v1.12 — DHR-SPEC006-002/003/004). A SPEC-007 **deve entregar o contrato do selo** sem redefinir RULE-CKG-010 (CC-02). |
| (c) Outras Specs baselined que apontam para a SPEC-007 | `SPEC-002/plan.md` l.170 e l.848 ("evidence candidate a partir de retrieval → SPEC-007"); `SPEC-003/plan.md` l.1080; `SPEC-020/plan.md` l.116/144/720/728 (RAG faithfulness ↔ SPEC-007); `SPEC-021/plan.md` l.160/762. | **FATO NORMATIVO.** Número e capacidade do slot são referenciados → preservar número e nome (INV-07). |
| (d) Fonte de requisitos já admitida | `backlog/RMR-001` BL-010 (MC-RAG-001, `Em espera`; "aplicação absorve o item na abertura de SPEC-007"); `reference/camadas/MC-RAG-001_Master_Contract_Camada_RAG.md` (46 RAG-SPEC; diz "Status: Baseline de especificação" l.6 — **não** é baseline do SOT: é referência externa classificada, K-MAN-14); `governance/CONFLICT-MAP.md` l.139-142 (COL-RAG-01..04). | MC-RAG-001 = **referência externa** (TRACE-06: documentado ≠ homologado). Colisões já homologadas (DHR-BL010-011-012-001). |
| (e) Conhecimento curado pré-existente | `rag/*.knowledge.md` (5 arquivos GEN-1: elliott-wave, fibonacci, smc, ict, synthesis), chunks com metadados (`chunk_id`, `agente`, `prioridade`, `quando_consultar`) — ex.: `rag/smc.knowledge.md` l.1-15. | `[FONTE]` GEN-1, **não** formado nem selado por pipeline. É, de fato, um "wiki curado à mão" sem proveniência formal → tensão a decidir (§10, Q-ABERTURA-6). |
| (f) Sobreposição com slots futuros | `ROADMAP.md` l.246-247 (SPEC-018 "Learning & Knowledge Formation Governance… Resolve K-001"), l.370-371 (SPEC-043 contexto: compressão, contexto obsoleto/contaminado), l.373-374 (SPEC-044 alucinação: afirmação sem fonte, conflito com fonte). | **Conflito de fronteira a declarar** (não a resolver em silêncio): "Knowledge Formation" aparece em SPEC-007 **e** SPEC-018; "contexto" em MC-RAG-001 Grupo D **e** SPEC-043; "fidelidade" em BL-017 **e** SPEC-044. Proposta de corte em §6/§8. |
| (g) "WikiRAG" | O termo só aparece no título do slot (ROADMAP l.179) e em registros que o repetem; **nenhum documento do SOT o define**. | **Lacuna terminológica** (CC-10/RULE-SEM). Interpretação proposta em §3.8 (a decidir por Andraus — Q-ABERTURA-3). |

**Conclusão.** A SPEC-007 é o **pipeline governado que transforma fonte em conhecimento publicado e devolve evidência citável aos agentes**: aquisição com proveniência → formação de candidato → validação → **selo de publicação** (o contrato do qual a SPEC-006 já depende) → recuperação com citação obrigatória → pacote de evidência → avaliação de fidelidade. Ela **não** é o KG (SPEC-006), **não** é o Blackboard (SPEC-004), **não** é o aprendizado/governança de runtime (SPEC-018/K-001) e **não** é a gestão de janela de contexto (SPEC-043).

---

## 1. Questões e estratégia de busca

- **Q1.** Qual o estado da arte de **chunking e recuperação** (lexical × semântica × híbrida; reranking)? Quando vale o custo?
- **Q2.** Como a **recuperação adaptativa** (recuperar só quando necessário) é feita e limitada?
- **Q3.** Como garantir **citação obrigatória e resolvível** (atribuição) na resposta?
- **Q4.** Como **medir fidelidade (faithfulness)** de RAG — e separá-la da qualidade da recuperação? (BL-017 / ROADMAP l.291: "RAG faithfulness (fecha em SPEC-007)".)
- **Q5.** Que riscos de **segurança** são próprios do RAG (envenenamento, injeção indireta)?
- **Q6.** O que significa "**WikiRAG**" no estado da arte (conhecimento compilado vs. recuperado)?
- **Q7.** Como tratar **atualização, obsolescência e esquecimento** sem violar INV-07?
- **Q8.** Que **repositórios seguros e bem avaliados** (RULE-ECC-06) exemplificam essas práticas?
- **Q9.** O que o **Benchmark Inteligencia-SOT** (decisão de Andraus, 2026-10-18) entrega que seja objeto do SOT Harness?

**Estratégia:** WebSearch para mapear o campo; WebFetch para capturar trechos literais de fontes primárias (arXiv, Anthropic, OWASP, gist de Karpathy) e páginas públicas de repositórios (estrelas/licença/arquivamento/último commit). Leitura local, somente leitura, do clone do Benchmark (`/home/user/andraus35/inteligencia-sot`, commit `0abd22e`). Nenhum dado sensível do SOT enviado em consultas.

**Termos de busca usados (acesso 2026-10-18) — correção A-09 (parecer do Revisor, 2026-10-19):**
- WebSearch: `Karpathy "LLM Wiki" pattern knowledge base compiled by LLM instead of RAG`; `gist.github.com karpathy llm-wiki`; `RAG faithfulness evaluation groundedness hallucination benchmark 2025 claim-level citation verification`.
- WebFetch direto (fonte primária conhecida, sem busca): `arxiv.org/abs/2309.15217`, `/2305.14627`, `/2310.11511`, `/2307.03172`, `/2505.04847`; `anthropic.com/news/contextual-retrieval`; `genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/`; `gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`.
- Repositórios (página HTML + página de commits do `main`; API 403): `vibrantlabsai/ragas`, `deepset-ai/haystack`, `truera/trulens`, `princeton-nlp/ALCE`, `Andraus35/Inteligencia-SOT`.
- Benchmark local (Grep/Glob/Read, somente leitura): padrões `(?i)chunk|retriev|recupera|embedding|faithful|citaç`, `RAG|corpus|SOT`; leitura de README, NOTICE, ROADMAP, AGENTS, `docs/governanca/*`, `documento-ativo.json` e dos relatórios de gate/OCR/revisor/contexto citados em §5.

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Papel |
|---|---|---|---|
| SRC-RAGAS-01 | arXiv 2309.15217 — Ragas (avaliação de RAG sem referência) | Benchmark + Prática | Q4 — avaliação de RAG sem referência humana; a leitura "fidelidade ≠ relevância como métricas separadas" é `[INFERÊNCIA]` (o trecho capturado não a afirma — correção A-04) *[texto anterior — INV-07 (correção N-08): "Q4 — dimensões de avaliação (fidelidade ≠ relevância)"]* |
| SRC-FAITHJUDGE-01 | arXiv 2505.04847 — Benchmarking LLM Faithfulness in RAG (2025) | Benchmark + Evidência | Q4 — recuperar certo não garante resposta fiel |
| SRC-ALCE-01 | arXiv 2305.14627 — ALCE (texto com citações) | Benchmark + Evidência | Q3 — citação como requisito verificável |
| SRC-CTXRET-01 | Anthropic — Contextual Retrieval (2024) | Prática + Experimento (do fornecedor) | Q1 — híbrida + reranking + chunk contextualizado |
| SRC-SELFRAG-01 | arXiv 2310.11511 — Self-RAG | Experimento + Prática | Q2 — recuperação sob demanda |
| SRC-LITM-01 | arXiv 2307.03172 — Lost in the Middle | Evidência + Experimento | Q1/Q4 — posição da evidência no contexto |
| SRC-OWASP-LLM08-01 | OWASP LLM08:2025 Vector and Embedding Weaknesses | Padrão (de facto) + Prática | Q5 — superfície de ataque do RAG |
| SRC-LLMWIKI-01 | Karpathy — gist "llm-wiki.md" (abr/2026) | Opinião + Prática emergente | Q6/Q7 — wiki compilado sobre fontes imutáveis |
| REPO-ragas / REPO-haystack / REPO-trulens | repositórios elegíveis (§4) | Prática | Q4/Q1/Q8 |
| REPO-ALCE / REPO-inteligencia-sot | repositórios **NÃO ELEGÍVEIS** (§4) | — (registrados, não adotados) | transparência da régua |

Fonte interna de requisitos (não `[EXTERNO]`): MC-RAG-001 (BL-010, referência externa classificada — K-MAN-14).

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

### 3.1 Formação ≠ publicação (Q1/Q9) — **ADOTAR como invariante do slot (já é do SOT)**
`[INFERÊNCIA]` — sem fonte `[EXTERNO]` própria neste item (correção A-10): o estado da arte e o próprio SOT convergem: a fonte não é conhecimento. *[texto anterior — INV-07: "O estado da arte e o próprio SOT convergem: a fonte não é conhecimento." sem etiqueta]* MC-RAG-001 §5 (l.188-192) proíbe o caminho "`Source → LLM → Knowledge Published`" e RAG-P04 (l.79-80) diz que a formação produz Knowledge Candidate e a publicação depende de validação e governança. Isso **é** a regra do ROADMAP l.182. **Comparação SOT:** o selo de publicação é o ponto onde a SPEC-007 encontra a SPEC-006 (RULE-CKG-010 caminho b). **Adotar** "formado ≠ publicado" como invariante; **adaptar** os estados do Knowledge Candidate como estados **locais** da SPEC-007 (COL-RAG-03), sem fechar **M-001** (estados do Blackboard para objetos não-hipótese — ABERTA). `[INFERÊNCIA]`: o selo tem efeito permanente (alimenta memória que nunca apaga — INV-07) → **E3 fail-closed**.

### 3.2 Chunking + recuperação híbrida + reranking (Q1) — **ADAPTAR como opção de estratégia; não fixar motor nem números**
[EXTERNO, SRC-CTXRET-01 — verbatim] *"Specifically, we found that Reranked Contextual Embedding and Contextual BM25 reduced the top-20-chunk retrieval failure rate"* e *"traditional RAG solutions remove context when encoding information"*. **Comparação SOT:** sustenta (i) chunk que **carrega contexto da sua origem** (alinha a "Trecho recuperado ≠ conhecimento validado" — o trecho precisa saber de onde veio), (ii) recuperação **híbrida** (lexical + semântica) e (iii) **reranking** como filtro. **Adaptar** como **estratégias declaradas com condição de uso** (MC-RAG-001 RAG-SPEC-013/014, l.461-477); o motor (índice, embeddings, reranker) é BUILD — neutralidade tecnológica (RAG-P12). Os percentuais são de experimento do fornecedor em corpus próprio: **não** viram meta nem limiar (CC-09). Ranking **não** pode depender só de similaridade (RAG-SPEC-017 l.495) — converge com RULE-004 (evidências da mesma origem contam como uma).

### 3.3 Recuperação adaptativa (Q2) — **ADAPTAR como laço limitado; REJEITAR autocrítica do modelo como gate**
[EXTERNO, SRC-SELFRAG-01 — verbatim] *"Our framework trains a single arbitrary LM that adaptively retrieves passages on-demand, and generates and reflects"*. **Comparação SOT:** recuperar só com justificativa (MC-RAG-001 §10, l.356-365) é eficiência legítima. **Adaptar** como laço com **limite e critério de parada** (Classe H, RULE-MECH-03; MC-RAG-001 RAG-SPEC-027 "novas chamadas devem possuir justificativa e limite"). **Rejeitar** que a "reflexão" do próprio modelo seja o gate: o gate de saída é do harness, determinístico quando possível (ENF-03). O orçamento é do Manager (SPEC-008), não do RAG (RAG-SPEC-015 l.479-485 — o roteador não aumenta o orçamento).

### 3.4 Citação obrigatória e resolvível (Q3) — **ADOTAR como requisito verificável do Evidence Packet**
[EXTERNO, SRC-ALCE-01 — verbatim] *"In this work, our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability"*. **Comparação SOT:** casa com RAG-P01 (proveniência obrigatória), com CEM-001 (Lineage) e com SPEC-002 (proveniência da evidência). **Adotar**: todo item do pacote de evidência cita um trecho **resolvível** (fonte + versão/hash + localizador). A checagem "a citação resolve?" é **Classe D** (determinística) e roda **antes** de qualquer juízo por modelo. O repositório do ALCE é NÃO ELEGÍVEL (§4) — usa-se só o paper.

### 3.5 Fidelidade (RAG faithfulness) (Q4) — **ADAPTAR a definição; fechar a dimensão B da SPEC-020 na homologação da SPEC-007**
[EXTERNO, SRC-RAGAS-01 — verbatim] *"We introduce Ragas (Retrieval Augmented Generation Assessment), a framework for reference-free evaluation of Retrieval"*. [EXTERNO, SRC-FAITHJUDGE-01 — verbatim] *"still frequently introduce unsupported information or contradictions even when provided with relevant context."* [EXTERNO, REPO-trulens — verbatim] *"Read more about the core concepts behind TruLens including Metrics, the RAG Triad, and Honest, Harmless and Helpful Evals."* **Comparação SOT:** `[INFERÊNCIA]` (correção A-04 — os trechos capturados sustentam só que a avaliação dispensa referência humana e que recuperar o contexto certo não garante resposta fiel; a separação em métricas distintas e a medição por afirmação são leitura minha, não afirmação literal das capturas): o campo separa **qualidade da recuperação** de **fidelidade do uso do trecho**; mede fidelidade **por afirmação** contra o trecho citado. *[texto anterior — INV-07: a mesma frase sem a etiqueta `[INFERÊNCIA]`]* Proposta `[PROPOSTA]` de definição em duas sub-medidas:
- **F1 — fidelidade de formação:** o Knowledge Candidate não introduz afirmação inexistente na fonte sem marcação (MC-RAG-001 RAG-SPEC-009 l.432-435); preserva modalidade ("pode" ≠ "vai"), negação, condição e quantidade; não converte associação em causa (RULE-EPI-02, RULE-CAU).
- **F2 — fidelidade do pacote de evidência:** cada afirmação da síntese mínima do pacote tem suporte no trecho que cita; contraevidência e lacunas aparecem (RAG-P08/P09).
Método: **D primeiro** (citação resolve, trecho existe, números/sinais literais preservados) e **H depois** (juízo por modelo com gate de saída e limite). **Limiares = INDETERMINADO** até calibração com amostra (sem falsa precisão — CC-09); nenhum número externo é importado. O fechamento formal é **emenda pontual à SPEC-020** no mesmo padrão do ERRATUM-SPEC020-001 (número a atribuir na homologação) — **não** se fecha antes (CONS-01; BL-017).

### 3.6 Posição e tamanho do contexto (Q1/Q4) — **ADIAR à SPEC-043; a SPEC-007 só declara a interface**
[EXTERNO, SRC-LITM-01 — verbatim] *"we observe that performance is often highest when relevant information occurs at the beginning or end of the input context"*. **Comparação SOT:** orçamento, empacotamento, compressão, "context rot" e "lost-in-the-middle" (MC-RAG-001 Grupo D, RAG-SPEC-021..025) são exatamente o tema da **SPEC-043** (ROADMAP l.370-371). **Adiar** para lá. A SPEC-007 **declara** só o que entrega: estimativa de tamanho do pacote e marcação de **evidência crítica** que não pode ser descartada por compressão/posição (RAG-P07). Sem isso, duplicaria a SPEC-043.

### 3.7 Segurança do RAG (Q5) — **ADOTAR: texto recuperado é dado, nunca instrução; fonte classificada antes da formação**
[EXTERNO, SRC-OWASP-LLM08-01 — verbatim] *"Vectors and embeddings vulnerabilities present significant security risks in systems utilizing Retrieval Augmented Generation"* e *"Data poisoning can occur intentionally by malicious actors (Ref #5, #6, #7) or unintentionally."* **Comparação SOT:** converge com DHR-PROV-WEB-001 §2.1 (conteúdo = dado) e com a classificação de fonte (MC-RAG-001 RAG-SPEC-004). **Adotar** como requisitos: (i) instrução embutida em fonte nunca muda o comportamento; (ii) fonte sem classificação não entra na formação; (iii) a publicação só ocorre sob selo (envenenamento não chega ao KG sem passar pela validação). A detecção de alucinação **sistêmica** fica com a SPEC-044. **Mecanismo da garantia (correção A-11):** *detectar* injeção em texto é probabilístico; por isso a regra (i) só pode ser Classe C/fail-closed se a garantia vier da **arquitetura**, não da detecção: `[PROPOSTA]` (a) a etapa de formação roda **sem ferramentas e sem efeitos** (só lê a fonte e devolve um candidato; não escreve, não chama ferramenta, não publica); (b) o **único** caminho para efeito permanente é o selo (gate não-LLM, E3). Assim, uma instrução embutida **não vira efeito** (essa é a garantia arquitetural); ela ainda pode produzir um candidato contaminado, que o selo **DEVE** barrar — e isso **não** é garantido pela arquitetura: depende da autoridade e da independência do juiz (Q-ABERTURA-8), pois o hash prova identidade e não qualidade, e um juiz por modelo lê o mesmo texto injetado (ver §10 item 1-bis). O Plan declara esse mecanismo por BASpec. *[texto anterior — INV-07 (correção N-03): "Assim, uma instrução embutida pode no máximo produzir um candidato ruim — que o selo barra."]*

### 3.8 "WikiRAG" (Q6) — **ADAPTAR como VISÃO do conhecimento publicado; REJEITAR wiki escrito pelo modelo como autoridade**
[EXTERNO, SRC-LLMWIKI-01 — verbatim] *"Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki"*; fontes brutas *"immutable — the LLM reads from them but never modifies them"*; varredura de *"contradictions between pages, stale claims that newer sources have superseded"*. **Comparação SOT:** a ideia útil é **compilar** o conhecimento uma vez (páginas por conceito, com citações às fontes imutáveis) em vez de re-derivar a cada consulta — ganho de Eficiência e de consistência. Mas no padrão original o **modelo escreve e mantém** o wiki: isso é "`Source → LLM → Knowledge Published`", proibido no SOT. **Proposta `[PROPOSTA]`:** "WikiRAG" = **visão compilada e legível do conhecimento já publicado sob selo** (página = projeção de itens publicados + citações), **reconstruível** a partir do publicado e **sem autoridade própria** (a verdade permanente é o KG — SPEC-006; RAG-SPEC-012 l.452-455 "sem transferir autoridade semântica para a tecnologia"). A varredura de contradição/obsolescência **detecta e registra** (Detector ≠ Gate — ENF-03); a resolução é da governança (RULE-CKG-013 da SPEC-006; SPEC-018). Os `rag/*.knowledge.md` GEN-1 (§0 e) são o antecessor natural dessa visão — mas hoje não têm proveniência formal. **Decisão de Andraus** (Q-ABERTURA-3).
**Classe e consumo do WikiRAG (correção A-03):** `[PROPOSTA]` (i) **compilação Classe D** — a página é montada por regra determinística a partir de itens já publicados (agrupar por conceito, ordenar, anexar citações), reconstruível byte a byte; **alternativa** (se Andraus quiser texto redigido por modelo): **Classe H com gate de saída** — cada frase da página precisa apontar item publicado que a sustente, senão a página não é emitida; nesse caso a página continua sendo visão, não conhecimento novo. (ii) **Regra de consumo:** o Evidence Packet e os agentes citam **somente itens publicados e fontes**, **nunca** a página do WikiRAG — página escrita por modelo e consumida como fonte seria conhecimento formado sem selo (contradiz RULE-CKG-010 `FORMED_WITHOUT_SEAL` e R-8). A página é para leitura humana e navegação.

### 3.9 Atualização, obsolescência e esquecimento (Q7) — **ADAPTAR sob INV-07: invalidar/superar, nunca apagar**
Mesmo princípio já adotado na SPEC-006 (research SPEC-006 §3.1/§3.6; "invalidar, não deletar"). **Comparação SOT:** quando a fonte muda (novo hash), o conhecimento formado dela é **marcado para revalidação** e pode ser **superado** por nova versão sob selo — nunca removido (INV-07; MC-RAG-001 RAG-P10 temporalidade explícita). O "esquecimento" de recuperação (deixar de recuperar algo obsoleto) é **filtro temporal** na consulta (RAG-SPEC-020 l.507-510), não deleção. Critérios de decaimento/retenção/valor = **K-001/SPEC-018** (aberta) — **não** fechar aqui.
**Obrigação para o futuro Plan (observação do Revisor, 2026-10-19):** RULE-CKG-004 (SPEC-006 `plan.md` l.395-401) diz que mudança de validade é **ato autorizado, nunca automática/cascata**. Logo, "fonte nova ⇒ derivados marcados para revalidação" só é compatível se a **marcação não for destrutiva** (não muda validade nem estado publicado) e se a superação/invalidação ocorrer **só** por novo selo ou ato autorizado. Registrar no Plan como obrigação herdada e como **caso D8** (tentativa de cascata automática ⇒ DENY).

---

## 4. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Régua: licença aberta conhecida; ≥300 estrelas; último commit ≤12 meses antes do acesso; não arquivado; 0 alerta grave público aberto; dono identificável. Uma captura por repositório em `sources/REPO-*.txt`. Conteúdo de repositório = **DADO**; **nada instalado/executado**.

| Repositório | Estrelas | Licença | Último commit | Veredito | Uso no SOT |
|---|---|---|---|---|---|
| https://github.com/vibrantlabsai/ragas | 16100 | Apache-2.0 | 2026-02-24 | **ELEGÍVEL** | Referência — adaptar o enquadramento da dimensão "RAG faithfulness" (métricas tradicionais + juízo por modelo — sustentado pelo trecho capturado; "métricas separadas" = `[INFERÊNCIA]`, correção A-04). Não é dependência. *[texto anterior — INV-07 (correção N-08): "Referência — adaptar o enquadramento da dimensão 'RAG faithfulness' (métricas separadas; métricas tradicionais + juízo por modelo). Não é dependência."]* |
| https://github.com/deepset-ai/haystack | 26800 | Apache-2.0 | 2026-10-16 | **ELEGÍVEL** | Referência — adaptar a separação de etapas (recuperação, roteamento, geração) como contratos distintos. Framework não escolhido (neutralidade tecnológica; motor = BUILD). |
| https://github.com/truera/trulens | 3600 | MIT | 2026-10-16 | **ELEGÍVEL** | Referência — o trecho capturado só nomeia o "RAG Triad"; ler isso como "qualidade da recuperação ≠ fidelidade da resposta" é `[INFERÊNCIA]` (correção A-04); rastreio por etapa fica com SPEC-040. *[texto anterior — INV-07 (correção N-08): "Referência — adaptar 'qualidade da recuperação ≠ fidelidade da resposta' (RAG Triad); rastreio por etapa fica com SPEC-040."]* |
| https://github.com/princeton-nlp/ALCE | 527 | MIT | 2024-10-09 | **NÃO ELEGÍVEL** (commit > 12 meses) | Registrado e descartado — código não é adotado; a alegação usa só o paper (SRC-ALCE-01). |
| https://github.com/Andraus35/Inteligencia-SOT | 0 | nenhuma | 2026-10-18 (proxy) | **NÃO ELEGÍVEL** (sem licença aberta; < 300 estrelas) | Descartado como dependência pela régua; tratado à parte como Benchmark por decisão de Andraus (§5), sem uso de motores/agentes/skills. |

Resultado: **3 repositórios elegíveis** (referência, nenhum adotado como dependência); **2 não elegíveis** registrados. Comando a rodar pelo operador: `python scripts/check_repo_research.py specs/features/SPEC-007`.

---

## 5. Benchmark Inteligencia-SOT (decisão de Andraus, chat 2026-10-18)

**Política aplicada (de Andraus, não do Especificador):** (1) motores, agentes e skills do projeto paralelo **NÃO** são usados no SOT — são **referência registrada como BENCHMARK**; (2) entregas efetivas que sejam objeto do SOT Harness são **analisadas** quanto a uso/integração, no todo ou em parte; (3) vale a estrutura do SOT, com **soberania** dos motores, agentes e controles do SOT. **Registro:** decisão registrada na ata **`governance/DHR-BENCH-INTEL-001_Ata_Inteligencia-SOT_como_Benchmark.md`** (D1–D6; D7 = correção do `AGENTS.md` §7; D8 = re-apontagem de COL-EXP-05). *[texto anterior — INV-07 (correção N-01): "Registro: Andraus mandou registrar em ata essa decisão (chat, 2026-10-19); a ata é criada pelo Orquestrador — citada aqui como 'DHR-BENCH-INTEL-001'." — e antes: a decisão constava só do chat de 2026-10-18 e do HANDOFF]*

### 5.1 O que o repositório é — [FATO do repositório] × [INFERÊNCIA] (commit `0abd22e`)
- **[FATO]** "O objetivo é traduzir documentos e preparar uma base RAG com fontes rastreáveis." (`inteligencia-sot@0abd22e:README.md:7`). Documento ativo: "Evidence-Based Technical Analysis, inglês → português do Brasil" (`inteligencia-sot@0abd22e:README.md:11`; `inteligencia-sot@0abd22e:rag/traducao/documento-ativo.json:3-4`, `document_id` com ISBN 0470008741).
- **[FATO]** A etapa RAG **não está implementada**: "LangChain, LangGraph, indexação e integração ao SOT não estão implementados" (`inteligencia-sot@0abd22e:README.md:35`); contratos de RAG são "candidatos à futura especificação/implementação" (`inteligencia-sot@0abd22e:docs/governanca/CONTRATOS.md:3`); a Etapa 2 é "Posterior à entrega/revisão da tradução, sem implementação nesta rodada" (`inteligencia-sot@0abd22e:ROADMAP.md:116`); RAG-ESCOPO está `aberto`, dependente de T8 (`inteligencia-sot@0abd22e:ROADMAP.md:30`).
- **[FATO]** O projeto se declara separado do SOT: "O projeto nasce separado do SOT e não importa sua governança." (`inteligencia-sot@0abd22e:rag/traducao/MASTER-PROJETO-TRADUCAO.md:3`); "decisões anteriores do SOT não aprovam regras deste projeto" (`inteligencia-sot@0abd22e:docs/governanca/POLITICA.md:37`); integração ao SOT está fora da implantação (`inteligencia-sot@0abd22e:docs/governanca/DECISOES.md:18-19`).
- **[FATO]** Licença: "Nenhuma licença geral de reutilização foi escolhida ou acrescentada nesta correção. Acesso público não equivale a concessão de licença." (`inteligencia-sot@0abd22e:NOTICE.md:4-5`); "nenhum direito sobre o livro ou autorização de publicação desses dados é concedido" (`inteligencia-sot@0abd22e:NOTICE.md:9-11`); componentes vendorizados têm licenças próprias (`inteligencia-sot@0abd22e:NOTICE.md:6-7`).
- **[FATO]** Estado do material: `pilot_approved: false`, `gold_reference_approved: false`, `corpus_approved: false` (`inteligencia-sot@0abd22e:rag/traducao/documento-ativo.json:53-55`); revisão humana competente da fonte **bloqueada** — "Nenhum revisor humano competente designado" (`inteligencia-sot@0abd22e:ROADMAP.md:22`).
- **[INFERÊNCIA]** O ISBN 0470008741 corresponde ao livro *Evidence-Based Technical Analysis* (D. Aronson, Wiley) — obra de terceiro sobre teste estatístico de regras de análise técnica e viés de mineração de dados; tema **pertinente** ao SOT (backtest/calibração — BL-032, WF-V01, RULE-CTF-01). O repositório não nomeia o autor; a atribuição é minha.
- **[INFERÊNCIA]** A "entrega efetiva" do paralelo hoje é **governança e controles determinísticos de uma etapa de preparação documental (tradução/OCR)** + **desenho** (não runtime) de contratos de RAG. Não há índice, recuperação nem avaliação de RAG executáveis para comparar.

### 5.2 Tabela item × objeto do SOT Harness × potencial

Legenda de potencial: **usar** · **integrar em parte** · **só referência** · **descartar**. "Integrar em parte" aqui significa sempre **reescrever pelo SOT, no idioma e nos contratos do SOT** (CC-02, soberania) — nunca copiar texto/código (licença).

| # | Item [FATO, arquivo:linha @0abd22e] | Objeto do SOT Harness? | Potencial | Condição (licença · soberania · E3/fail-closed) | Risco |
|---|---|---|---|---|---|
| B1 | Separação aquisição → transformação → revisão → **liberação ao corpus**, com aprovação por documento/lote vinculada ao hash (`inteligencia-sot@0abd22e:docs/governanca/POLITICA.md:31` IG-09; `inteligencia-sot@0abd22e:docs/governanca/CONTRATOS.md:5-11`) | **Sim** — mesma cadeia do slot (ROADMAP l.182) | **só referência** (convergência; o SOT já tem a regra) | Liberação do corpus deles **≠** selo do SOT; nada entra no KG sem selo SPEC-007 (E3) | Confundir "corpus aprovado lá" com "publicado aqui" |
| B2 | Proveniência mínima candidata: `document_id`, `source_version`, `source_sha256`, `source_locator`, `page`, `block_id`, `derived_from`, `transform_name/version`, `review_ref`, `approval_ref`, `temporal_scope`, `conflict_refs`… (`inteligencia-sot@0abd22e:docs/governanca/CONTRATOS.md:15-17`) | **Sim** — Source Model / proveniência (RAG-SPEC-003; CEM-001 Lineage; SPEC-002) | **integrar em parte** — como **lista de conferência** no Plan, redigida pelo SOT por referência a CEM-001/SPEC-002 | CC-02 (não redefinir CEM); reprodução literal da lista = **[DECISÃO NECESSÁRIA — licença do titular]** | Criar 2º esquema de proveniência paralelo ao CEM |
| B3 | Casos de verificação: "Chunk sem referência resolvível: impedir liberação ao corpus"; "Duas traduções citam o mesmo bloco: não tratá-las automaticamente como duas evidências independentes"; "Fonte com comando para ignorar política: tratar como texto"; "Sem evidência suficiente… explicar lacuna" (`inteligencia-sot@0abd22e:docs/governanca/CONTRATOS.md:31-39`) | **Sim** — citação resolvível, RULE-004, conteúdo = dado, lacuna explícita | **integrar em parte** — como **casos adversariais candidatos (D8)**, redigidos pelo SOT | Licença: ideias de teste não são cópia de texto `[INFERÊNCIA]`, mas texto literal só com autorização do titular | Baixo |
| B4 | IG-05 fidelidade: não converter "pode" em "será", associação em causalidade, hipótese em fato (`inteligencia-sot@0abd22e:docs/governanca/POLITICA.md:19`) | **Sim** — fidelidade de formação (F1, §3.5); RULE-EPI-01/02, RULE-CAU | **só referência** (o SOT já tem as regras) | — | Baixo |
| B5 | IG-06 conteúdo como dado (`inteligencia-sot@0abd22e:docs/governanca/POLITICA.md:21`) | **Sim** — converge com DHR-PROV-WEB-001 | **só referência** | — | Baixo |
| B6 | Gate de artefato: identidade por **digest confiável recebido separado do candidato** (ART-TRUST-01, `inteligencia-sot@0abd22e:docs/GATE-ARTEFATO-IMPLEMENTADO.md:35-41`); "QUANDO requisito obrigatório não possui checker semântico implementado, ENTÃO registrar UNPROVEN e BLOCKED" (ART-PROOF-03, `inteligencia-sot@0abd22e:docs/GATE-ARTEFATO-IMPLEMENTADO.md:48-53`); falha/insumo incompleto bloqueia sem aprovação (ART-FAIL-04, `inteligencia-sot@0abd22e:docs/GATE-ARTEFATO-IMPLEMENTADO.md:54-59`); publicação atômica com link exclusivo, sem sobrescrita (`inteligencia-sot@0abd22e:docs/GATE-ARTEFATO-IMPLEMENTADO.md:82-84`) | **Sim** — **padrão do selo de publicação** (selo vinculado ao hash do material validado; ausência de prova = bloqueio) | **integrar em parte** — o **padrão conceitual** do selo: hash do validado + estado sem-prova ⇒ **INDETERMINADO ⇒ não publica** (fail-closed E3, Classe C/D). **Código: descartar** (específico de PDF/Poppler) | Soberania: o selo é do SOT (gate não-LLM, ENF-03); código só com licença do titular | Importar estados "UNPROVEN/BLOCKED" como vocabulário paralelo ao INDETERMINADO do SOT (CC-10) |
| B7 | Contrato OCR: original → raster → regiões → **observação bruta** preservada antes do candidato; relatórios com `semantic_fidelity_proven=false`, `reviewer_authenticated=false` (`inteligencia-sot@0abd22e:docs/CONTRATO-OCR-IMPLEMENTADO.md:51-57` e `:98-108`) | **Parcial** — aquisição/parsing de documento escaneado (RAG-SPEC-005/006); honestidade de limites (RULE-MET-01) | **só referência** (princípio "bruto preservado antes do derivado"); **código/OCR: descartar** | — | Especificar OCR na SPEC-007 (fora de escopo; é BUILD de adaptador de fonte) |
| B8 | Revisor adversarial híbrido: canal **D** (recalcula números, sinais, ordem, fórmulas) + canal **P** com nove eixos — "negação, condições, modalidade, quantidades, associações, omissões, terminologia, visual e instruções hostis tratadas como dados"; combinação só *clear* se D passar e P for *clear* (`inteligencia-sot@0abd22e:docs/REVISOR-ADVERSARIAL-HIBRIDO-2026-10-13.md:12-22`) | **Sim** — método de avaliação de **fidelidade** (F1/F2) e casamento com Classe D + H/P com gate de saída | **integrar em parte** — os eixos como **taxonomia candidata de falhas de fidelidade**, confrontada com SPEC-020/022/044 no Plan; o agente/skill deles **não** é usado | Soberania: avaliadores do SOT (Revisor/gates); nada de "auditor" externo no fluxo | Taxonomia de tradução não cobrir falhas de RAG (ex.: citação a trecho errado) |
| B9 | Exportação Markdown determinística MD-01..07: recusa por hash divergente, ID repetido, tabela/fórmula não representada; MD-06 "Não inferir fidelidade da tradução" (`inteligencia-sot@0abd22e:docs/retomada/MARKDOWN-SPEC.md:16-40`) | **Parcial** — normalização/unidade semântica com identidade (RAG-SPEC-006/007) | **só referência** | — | Baixo |
| B10 | Roteiro RAG R1–R5: "Citações resolvíveis, ausência de suporte declarada, conflitos com versões/fontes"; "Não escolher verdade entre fontes conflitantes por inferência" (`inteligencia-sot@0abd22e:ROADMAP.md:119-129`); "mostrar versões e conflitos com citações, sem escolher verdade por inferência" (`inteligencia-sot@0abd22e:docs/governanca/DECISOES.md:13-14`) | **Sim** — RAG-P08 (contradição explícita), citação obrigatória | **só referência** (convergência; desenho, não entrega) | — | Baixo |
| B11 | CTX-01: contexto por hash/cache, recibo antes de efeito, gateway de escrita, simetria documental (`inteligencia-sot@0abd22e:docs/CONTEXTO-SPEC.md:6-24`) — "memória entre sessões" | **Sim, mas NÃO da SPEC-007** — spec-time → SPEC-046 (baseline) / PCC-001 (HANDOFF); runtime → SPEC-009 (G-001) / SPEC-043 | **só referência** (para evolução da SPEC-046/PCC; fora deste slot) | — | Puxar memória de sessão para dentro do RAG |
| B12 | Guarda de publicação Git `publicar.sh` (`inteligencia-sot@0abd22e:README.md:39-43`) | **Não do SOT runtime** — tooling de repositório (o SOT tem CI/hooks próprios) | **descartar** para a SPEC-007 | — | — |
| B13 | Pipeline de tradução (citações desagregadas — correção A-05): 3 papéis coordenador/tradutor/auditor (`inteligencia-sot@0abd22e:AGENTS.md:116-120`, bloco `roles` *[antes: `:114-118` — corrigido, N-09]*); avaliação WMT/MQM (`inteligencia-sot@0abd22e:README.md:20-21`) e diagnóstico WMT24++ com Marian (`inteligencia-sot@0abd22e:README.md:46-48`); OCR Tesseract (`inteligencia-sot@0abd22e:ROADMAP.md:71`) e Poppler (`inteligencia-sot@0abd22e:docs/GATE-ARTEFATO-IMPLEMENTADO.md:25-26`); skills `translation-*` (`inteligencia-sot@0abd22e:rag/traducao/.agents/skills/translation-{coordinator,translator,quality,auditor}/SKILL.md`); Harness Score L4 de Paladini (`inteligencia-sot@0abd22e:AGENTS.md:70`), vendorizado e pinado (`inteligencia-sot@0abd22e:docs/HARNESS-QUALIDADE.md:4`) *[citação anterior — INV-07: "(`AGENTS.md` fatos `roles`), … (`inteligencia-sot@0abd22e:AGENTS.md:66-72`)" agregada]* | **Não** — só do projeto de tradução | **descartar** (política de Andraus: motores/agentes/skills não usados) | Licenças de terceiros vendorizados não se estendem (`inteligencia-sot@0abd22e:NOTICE.md:6-7`) | — |
| B14 | **O livro traduzido** como fonte para o corpus do SOT (`inteligencia-sot@0abd22e:rag/traducao/documento-ativo.json:3-4`; `corpus_approved: false` `:55`; `document_data_publication_allowed: false` `:60`) | **Sim, como DADO de entrada** (fonte candidata), não como harness | **usar** como **fonte candidata** — **só** depois de: (i) definido se Andraus tem/obterá autorização do titular dos direitos da obra (terceiro) ou se o uso fica restrito a uso privado, e se o corpus pode ou não ir a provedor externo de embeddings/LLM — o próprio Benchmark separa aprovação do corpus de transmissão externa (`inteligencia-sot@0abd22e:ROADMAP.md:128`; `inteligencia-sot@0abd22e:docs/governanca/POLITICA.md:33`) *[texto anterior — INV-07: "(i) direito de uso da obra de terceiro decidido"]*; (ii) revisão humana da tradução; (iii) entrada pela aquisição da SPEC-007 (classificação, proveniência, formação, validação, selo) | **[DECISÃO NECESSÁRIA — direitos autorais de terceiro + uso privado]**; tradução **≠** fonte original (proveniência deve apontar o original e a transformação) | Tratar tradução não revisada como verdade; risco jurídico de reprodução |

**O que do Benchmark é, de fato, objeto do SOT Harness:** B1–B6, B8 e B10 (formação governada, proveniência, citação/independência, fidelidade, selo vinculado a hash com fail-closed, conflito explícito); B7/B9 parcialmente (aquisição/normalização); B11 é objeto do SOT, mas de **outras** Specs; B14 é **insumo de dados**, não mecanismo. **Só da tradução:** B12, B13.

### 5.3 Integração possível (interface, não mecanismo) — `[PROPOSTA]`
Se Andraus quiser ligar os dois projetos, a interface natural é **uma fonte externa** na etapa de aquisição da SPEC-007: o "manifesto de corpus liberado" deles (`inteligencia-sot@0abd22e:docs/governanca/CONTRATOS.md:9`) entraria no SOT como **fonte classificada** (com hash e cadeia de transformação), **nunca** como conhecimento publicado. A aprovação de corpus deles (IG-09) **não** substitui validação nem selo do SOT. Nenhum agente, skill ou motor deles roda dentro do SOT.

---

## 6. Cobertura por canônicos/Specs BASELINED × lacuna real da SPEC-007 × o que pertence a outros

| Capacidade | Já coberto? | Lacuna da SPEC-007 / dono |
|---|---|---|
| Proveniência de evidência (`computed_by`, `gate_record`, Lineage) | **SIM** — CEM-001; SPEC-002 (BASELINE); SPEC-004 v1.2 | Proveniência da **fonte e do trecho** (Source Model) **por referência** a CEM/SPEC-002 — não redefinir |
| Evidência candidata a partir de retrieval | **Atribuído** à SPEC-007 por SPEC-002 l.170/848 e SPEC-003 l.1080 | **Lacuna central:** como um trecho recuperado vira *Evidence Candidate* entregue ao agente — o agente é quem produz a **Evidência** (CEM-001; INV-06) |
| Memória de trabalho / objetos de trabalho | **SIM** — SPEC-004 (Blackboard) | Knowledge Candidate como objeto de trabalho: **estados = [DECISÃO NECESSÁRIA] por tocar M-001 (ABERTA)** |
| Notificação de mudança | **SIM** — SPEC-005 | Nenhuma — a SPEC-007 **emite/consome** eventos (publicação, revalidação), não redefine transporte |
| Memória permanente, admissão, imutabilidade, contradição | **SIM** — SPEC-006 (RULE-CKG-001..013; H-001 FECHADA — PostgreSQL só-inserção bitemporal, DHR-H001-001) | **Lacuna central:** **contrato do selo** (RULE-CKG-010 b) — a SPEC-007 o entrega; **não** redefine o KG, o contrato CKG, a admissão por tipo, nem o mecanismo físico |
| Formação → Knowledge Candidate → Validação → Selo | **NÃO** | **Lacuna central** da SPEC-007 |
| Recuperação (estratégias, híbrida, temporal, contraditória) + Evidence Packet com citação | **NÃO** | **Lacuna central** da SPEC-007 (consulta ao KG = read-only, RULE-CKG-011) |
| RAG faithfulness (dimensão B da SPEC-020) | **DIFERIDA** — BL-017 | **Lacuna central**; fecha por emenda pontual à SPEC-020 na homologação |
| Orçamento/empacotamento/compressão/rot de contexto | **NÃO** | **SPEC-043** (slot) — fora da SPEC-007 |
| Alucinação sistêmica (afirmação sem fonte em qualquer saída) | **NÃO** | **SPEC-044** (slot) — a SPEC-007 cobre só a fidelidade **do RAG** |
| Aprendizado com feedback de recuperação; governança de runtime; ciclo de evolução P12 | **NÃO** | **SPEC-018 / K-001 (ABERTA)** — a SPEC-007 só registra feedback rastreável; não se autoaltera (RAG-P13) |
| Estado persistente por agente; continuidade entre sessões em runtime | **NÃO** | **SPEC-009 / G-001 (ABERTA)** |
| Episódios/experiência (EXPERIENTIAL) | **NÃO** | **SPEC-017** (Pattern Memory) + SPEC-009; RAG-P11 (experiência ≠ regra) declarado; dup. EXP-SPEC-021 ↔ RAG-SPEC-018 (COL-EXP-05) — **re-apontado à SPEC-007 por decisão de Andraus (chat, 2026-10-19; DHR-BENCH-INTEL-001 D8)**; `CONFLICT-MAP.md:147` (hoje "ADIAR (SPEC-006/009)") será atualizado pelo Orquestrador após a homologação da abertura (ABERTURA §11): o Plan da SPEC-007 **deve tratar** a reconciliação COL-EXP-05; proposta de tratamento: independência de **evidência** na SPEC-007 (RAG-SPEC-018, conforme RULE-004/COL-RAG-04), independência de **experiência** com SPEC-009/017 *[texto anterior — INV-07: "independência de evidência fica na SPEC-007 (…); independência de experiência fica com SPEC-009/017" como fronteira, sem re-apontamento]* |
| Orçamento de recursos da consulta | **NÃO** | **SPEC-008** (Manager — orquestração); o RAG não aumenta orçamento |

**Invariantes de fronteira (reafirmados, não reabertos):** **INV-04** — escore de relevância/recuperação e "confiança" do pacote **não** são Convicção e **nunca** entram no Conviction Vector; custo de recuperação idem. **INV-05** — o RAG entrega evidência e contexto, **não** conclusões nem decisões (RAG-SPEC-030 l.565-568); não executa nada. **INV-07** — publicado nunca é apagado; superado/invalidado preserva histórico. **CC-02** — CEM/CHM/CCM e SPEC-002/004/005/006 intocados.

**Permanecem abertas (CONS-01):** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03 (residual), ECC-03-001, SPEC-045-RUNTIME-001, **CKG-STRUCT-ORIGIN-001** (BL-035), produtor/gatilho de promoção trabalho→permanente (SPEC-006 l.976). *[texto anterior — INV-07: a lista incluía "RULE-REG-001" entre "SPEC-045-RUNTIME-001" e "CKG-STRUCT-ORIGIN-001"; retirada por correção A-01 — `ROADMAP.md:37` registra RULE-REG-001 **FECHADA** (Andraus, 2026-09-28, DHR-REG-001)]*
**Nota (A-01, resolvida — correção N-01):** por ordem de Andraus, o `AGENTS.md` §7 foi corrigido e registra RULE-REG-001 **FECHADA** (`AGENTS.md:137`; ata DHR-BENCH-INTEL-001, D7). *[texto anterior — INV-07: "Nota de divergência (pendência de Andraus — A-01): `AGENTS.md` §7 ainda descreve RULE-REG-001 como aberta; o ROADMAP prevalece (o próprio AGENTS §7 manda seguir o ROADMAP em divergência). Corrigir o AGENTS.md é decisão de Andraus (AGENTS §10) — ainda **não** decidida; o Especificador não edita esse arquivo."]*

---

## 7. Mapeamento de MC-RAG-001 (BL-010) por grupo → destino proposto

| Grupo MC-RAG-001 | RAG-SPEC | Destino proposto | Tratamento de colisão |
|---|---|---|---|
| A — Fundamentos | 001-007 (capacidade, request, source model, classificação, aquisição, parsing, unidade semântica) | **SPEC-007** (contratos); parsing/OCR concretos = BUILD de adaptador | COL-RAG-03: I-RAG/RAG-P como **locais** |
| B — Formação | 008-011 (candidato, fidelidade, impacto, publicação) | **SPEC-007** (núcleo) | 4Es na ordem do SOT (COL-RAG-02 — rejeitar ordem do §1 do MC-RAG) |
| B — Projeção no KG | 012 | **SPEC-006** (já baselined) — a SPEC-007 só entrega o **selo** | CC-02 |
| C — Recuperação | 013-014, 016-020 | **SPEC-007** | 018 conforme RULE-004 (COL-RAG-04) |
| C — Recurso | 015 (Scheduler/RAG) | **SPEC-008** (orçamento) — interface declarada na SPEC-007 | — |
| D — Contexto | 021-025 | **SPEC-043** | — |
| D — Lacuna/suficiência/laço/pacote | 026-029 | **SPEC-007** | laço = Classe H com limite |
| E — Integração | 030-031 | **SPEC-007** (interface com CEM/KG por referência) | INV-05; CC-02 |
| E — Experiência / Aprendizado | 032-033 | **SPEC-009/017** / **SPEC-018** | RAG-P11/P13 declarados |
| F — Feedback | 034 (registro rastreável) | **SPEC-007** (só registro) | — |
| F — Aprendizado/regressão | 035-036 | **SPEC-018** (aprendizado) / **SPEC-022** (regressão) | — |
| Harness/Gates/Métricas | 037; G0–G8 | Avaliação na **SPEC-007** + SPEC-020; **G-gates rejeitados** como taxonomia global → gates locais | COL-RAG-01 |
| Segurança / Benchmark / Versionamento | 045 / 043-044 / 042 | **SPEC-007** (segurança e versionamento do pipeline); benchmark de economicidade = BUILD | INV-04 |
| Quality Gates | 038 | **SPEC-007** como **gates locais** (nunca taxonomia G0–G8 global) | COL-RAG-01 |
| Métricas | 039 (RAG Metrics Model) | **SPEC-007** — só a **definição** das métricas do próprio RAG (incl. F1/F2), **sem limiares** (INDETERMINADO); integração na avaliação do harness = SPEC-020 | CC-09; INV-04 (métrica/custo ≠ convicção) |
| Taxonomia de falhas | 040 (RAG Failure Taxonomy) | **SPEC-007** (taxonomia local de falhas do pipeline, insumo B8) + casos de regressão → **SPEC-022** | — |
| Observabilidade | 041 (RAG Observability Contract) | **SPEC-040** (Cognitive Observability); a SPEC-007 só declara os eventos/campos que emite | Detector ≠ Gate (ENF-03) |
| Ciclo de vida | 046 (RAG Lifecycle) | **SPEC-007** (ciclo de vida do candidato e do pipeline, estados locais sem reusar nomes do CHM-001; sem fechar M-001) | CC-02; CC-10 |

*(Linhas 038-041 e 046 acrescentadas por correção A-06 — parecer do Revisor, 2026-10-19; fonte: `reference/camadas/MC-RAG-001_Master_Contract_Camada_RAG.md` l.1109-1117.)*

---

## 8. Escopo, quantidade, decomposição e re-apontamento

### 8.1 Opções de decomposição (detalhe e recomendação em `ABERTURA.md` §3-§4)
- **(A) Uma Spec "tudo de MC-RAG-001"** (46 itens, inclusive contexto e aprendizado) — **rejeitada**: invade SPEC-043/018/044 e não cabe numa sessão de revisão.
- **(B) Uma Spec núcleo — RECOMENDADA:** SPEC-007 = aquisição com proveniência + formação + validação + **selo** + recuperação com citação + pacote de evidência + fidelidade (F1/F2) + segurança; contexto → SPEC-043; aprendizado → SPEC-018; alucinação sistêmica → SPEC-044. Com **cláusula de divisão** se o Plan não couber numa revisão.
- **(C) Duas Specs agora:** SPEC-007 (formação + selo) + Spec nova (recuperação + pacote), número só na abertura dela (o SPEC-047 está reservado — ROADMAP l.538). Custo: **erratum aditivo de re-apontamento** em Specs baselined que hoje mandam "retrieval → SPEC-007" (SPEC-002 l.170/848; SPEC-003 l.1080; SPEC-006 l.299/341/1594) e divisão da dimensão faithfulness entre duas Specs — o que também exige re-apontar as referências "RAG faithfulness → SPEC-007" em **SPEC-020** `plan.md` l.116/144/720/728 e **SPEC-021** `plan.md` l.160/762 (correção A-12; só pesa se Andraus escolher a C).

Critérios: Eficácia (entregar o selo que a SPEC-006 espera **e** a recuperação que os agentes vão consumir), Efetividade (sem duplicar SPEC-043/044/018), Eficiência (uma revisão por Spec), Economicidade (evitar errata em baselines). (B) atende os quatro; (C) só se o Plan de (B) não couber.

### 8.2 Re-apontamento de gatilhos e referências baselined (item 5 e 6 do §15)
- Sob (B): número e nome **preservados** → **nenhum** re-apontamento de gatilho `spec:` e **nenhum** erratum em Spec baselined.
- Sob (C): re-apontar **BL-017** (parte "answer/packet faithfulness") e propor erratum aditivo às referências listadas em 8.1 — **não** executado aqui.

### 8.3 Itens do RMR-001 vinculados por regra (DHR-BACKLOG-ABERTURA-001) — **o Especificador não promove**
Pela regra (gatilho com alternativa `spec:SPEC-007 em redação`), ficam vinculados: **BL-010**, **BL-017** e **BL-035**. **Conflito registrado:** ROADMAP l.34 cita só "BL-010 e BL-035"; o gatilho do **BL-017** (`spec:SPEC-007 em redação ∨ spec:SPEC-014 em redação`) também casa com a regra do `backlog_triggers.py --abertura` (l.203-233). Recomendo tratar os três; confirmar rodando `python scripts/backlog_triggers.py --abertura SPEC-007`. Disposições **propostas** (a declarar no Plan) em `ABERTURA.md` §8. **BL-011** (gatilho `milestone:` e `spec:SPEC-006/009`) **não** vincula por regra, mas está em estado **`ATIVADO`** (`backlog/RMR-001_Painel_Backlog.md:118`, Andraus, 2026-10-17, DHR-BACKLOG-001; a SPEC-006 deu `Disposição: PARCIAL` e adiou COL-EXP-05 "→ SPEC-007/009"). **Decisão de Andraus (chat, 2026-10-19; registrada em DHR-BENCH-INTEL-001 D8):** **re-apontar o resíduo COL-EXP-05 para a SPEC-007**; o item **segue `ATIVADO`** (não virou `Absorvido` — isso é só de Andraus). Consequência: o Plan da SPEC-007 **deve tratar** COL-EXP-05 (ver §6). *[texto anterior — INV-07: "seu resíduo COL-EXP-05 é tratado em §6 como fronteira." — omitia o estado ATIVADO; correção A-08]*

---

## 9. Incidência de RULE-ECC-05 (Pesquisa Multi-Lente) e de CC-12

**RULE-ECC-05 — NÃO INCIDE** `[PROPOSTA — a confirmar pelo Revisor]`. A SPEC-007 não define comportamento de agente analítico, Conviction/Fusion, Manager ou Risk: entrega evidência citável e conhecimento publicado, agnóstica de escola (mesma determinação das SPEC-004/005/006). Conformidade prudencial com `WORKFLOW.md` v2.1: o documento **não** menciona RAG/conhecimento (busca sem ocorrências de "RAG", "conhecimento", "Knowledge"); a SPEC-007 não contradiz nenhum `WF-xx` e não fecha `WF-Dxx`. Se no Plan a recuperação tocar a formação de contexto de uma fase do Manager, o `WF-xx` será citado por ID. **Ressalva honesta:** o *conteúdo* do corpus é de domínio (ex.: livro B14); isso não torna a Spec de especialidade — o pipeline trata qualquer escola como dado.
**CC-12 (RULE-PD-01) — NÃO INCIDE:** não é Spec de especialidade; nenhum `PD-xx` proposto.

---

## 10. Lacunas, conflitos e INDETERMINADOS (RULE-MET-01)

1. **Contrato do selo de publicação** — dependência aberta da SPEC-006 (l.487, l.1670). A SPEC-007 o especifica; quem é o **produtor/gatilho de promoção** de objetos **canônicos** (caminho a) segue **[DECISÃO NECESSÁRIA]** (SPEC-006 l.976; proposta SPEC-018/K-001). `[PROPOSTA]`: a SPEC-007 é a produtora só do conhecimento **formado** (caminho b).
1-bis. **Autoridade e independência do selo (correção A-02)** — falta decidir **quem emite** o selo (identidade autenticada; allowlist de emissores — a SPEC-006 deixa "quem mantém a allowlist de escritores" em [DECISÃO NECESSÁRIA], `plan.md` l.482, K-001/SPEC-018), se há **aprovação humana por lote** (como o IG-09 do Benchmark, `inteligencia-sot@0abd22e:docs/governanca/POLITICA.md:31`), se o **juiz de fidelidade (Classe H) é independente** do modelo que formou o candidato, e o **conteúdo mínimo** do selo (hash do validado + emissor autenticado + referência ao registro de validação). Sem isso, o mesmo modelo poderia propor e validar (risco ENF-03). **Limite honesto:** o vínculo ao hash prova **identidade** do material, não a **qualidade** da validação. Toca **K-001/SPEC-018 (abertas)** sem fechá-las. **[DECISÃO NECESSÁRIA]** — Q-ABERTURA-8.
1-ter. **Homônimo `CANDIDATE` (correção A-07)** — "Knowledge Candidate"/"Evidence Candidate" (objetos do pipeline) ≠ estado `CANDIDATE` da hipótese (`canon/CHM-001-canonical-hypothesis-model.md` l.329/332). Os estados locais do pipeline **não** reutilizam nomes de estado do CHM-001 (CC-10/CC-02).
2. **Estados do Knowledge Candidate × M-001** — se o candidato vive no Blackboard, seus estados tocam M-001 (ABERTA). **[DECISÃO NECESSÁRIA]**; proposta: estados locais declarados como `[PROPOSTA]`, sem fechar M-001.
3. **"WikiRAG" sem definição no SOT** — interpretação proposta em §3.8; **[DECISÃO NECESSÁRIA]** (Q-ABERTURA-3).
4. **`rag/*.knowledge.md` GEN-1** — conhecimento curado sem proveniência formal nem selo; não pode ser tratado como publicado sem passar pelo pipeline; também não pode ser apagado (INV-07). **[DECISÃO NECESSÁRIA]** (Q-ABERTURA-6).
5. **Fronteira com SPEC-018** ("Knowledge Formation" nos dois títulos) — proposta: SPEC-007 = **pipeline e selo** (spec do mecanismo); SPEC-018 = **governança/aprendizado de runtime** (quem aprova o quê, ciclo P12, K-001). A confirmar por Andraus.
6. **Fronteira com SPEC-043/044** — proposta em §3.6/§6; a confirmar.
7. **Limiares de fidelidade** = **INDETERMINADO** até calibração com amostra; nenhum número externo vira meta.
8. **Benchmark** — sem RAG executável para comparar (§5.1); a comparação é de **governança e controles**, não de desempenho. Licença ausente: qualquer reuso literal de código/texto = **[DECISÃO NECESSÁRIA — titular]**. Direitos sobre o livro (obra de terceiro) = **[DECISÃO NECESSÁRIA]**.
9. **Divergência ROADMAP l.34 × regra de vinculação** (BL-017) — §8.3.
10. **Métricas de repositório** = página pública (API 403); alertas de segurança = INDETERMINADO (registrado como 0). `_LIMITACAO-WEB.txt`.

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-18; capturas em `sources/`)
- [Ragas: Automated Evaluation of Retrieval Augmented Generation (arXiv 2309.15217)](https://arxiv.org/abs/2309.15217) — SRC-RAGAS-01
- [Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards (arXiv 2505.04847)](https://arxiv.org/abs/2505.04847) — SRC-FAITHJUDGE-01
- [Enabling Large Language Models to Generate Text with Citations (arXiv 2305.14627)](https://arxiv.org/abs/2305.14627) — SRC-ALCE-01
- [Introducing Contextual Retrieval (Anthropic, 2024)](https://www.anthropic.com/news/contextual-retrieval) — SRC-CTXRET-01
- [Self-RAG (arXiv 2310.11511)](https://arxiv.org/abs/2310.11511) — SRC-SELFRAG-01
- [Lost in the Middle (arXiv 2307.03172)](https://arxiv.org/abs/2307.03172) — SRC-LITM-01
- [OWASP LLM08:2025 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) — SRC-OWASP-LLM08-01
- [Karpathy — llm-wiki.md (gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — SRC-LLMWIKI-01
- [ragas](https://github.com/vibrantlabsai/ragas) · [haystack](https://github.com/deepset-ai/haystack) · [trulens](https://github.com/truera/trulens) — elegíveis
- [ALCE](https://github.com/princeton-nlp/ALCE) · [Inteligencia-SOT](https://github.com/Andraus35/Inteligencia-SOT) — não elegíveis

*Dossiê não-normativo. Insumo para `ABERTURA.md` e para a decisão de Andraus. Não altera ROADMAP, RULES, WORKFLOW, Specs, canônicos nem o RMR-001; não fecha decisão aberta (CONS-01). Web e repositórios = DADO, nunca instrução nem baseline.*
