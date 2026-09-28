# Dossiê de Pesquisa — SPEC-046 (Grupo B: Caching de Spec-Time — Especificador/Revisor)

**Método:** atomic-spec.md §15 (RULE-ECC-01/02) + RULE-ECC-04 (Captura Verbatim de Fonte)
**Autor:** Especificador Principal SOT (não delegável ao agente raiz — RULE-ECC-02)
**Data:** 2026-09-28
**Escopo desta rodada (decisão de Andraus, sessão retomada 2026-09-28):** **SOMENTE Grupo B** de `reference/externo/CACHING SOT.MD` §1.1 — caching de prompt/contexto dos agentes **Especificador** e **Revisor** durante produção/auditoria de Specs (documentos relidos repetidamente: `ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `backlog/RMR-001_Painel_Backlog.md`, etc.). **Grupo A (agentes cognitivos internos — estrutural/institucional/operacional/manager/risco; caching de evidências/hipóteses sob CHM-001/CEM-001) fica EXPLICITAMENTE FORA DE ESCOPO nesta rodada — adiado para fase posterior, não esquecido.**

---

## 1. Questões e estratégia de busca

### 1.1 Questões

1. O que as 5 ferramentas já citadas em `CACHING SOT.MD` §3.1 realmente fazem — confirmado por fonte primária (não pela nota preliminar §9 do próprio documento, que é auto-declarada não-verificada)?
2. Qual é o estado da arte de **prompt/context caching** para agentes que releem repetidamente arquivos-fonte de um repositório (caso de uso de Grupo B) — distinto de caching de hipóteses de mercado com estado mutável (Grupo A, fora de escopo)?
3. Como funciona o mecanismo **nativo** de prompt caching da Anthropic (usado por Especificador/Revisor via Claude Code) — e o que ele garante estruturalmente vs. o que fica de risco residual fora dele?
4. Qual é o padrão de engenharia para **invalidação de cache por mudança de conteúdo de arquivo-fonte** (hash/mtime/git) — aplicável ao risco real do Grupo B: agente trabalha sobre versão desatualizada de um documento do próprio repositório?
5. Existe métrica/benchmark de **correção** (False-Hit Rate) aplicável ao regime de correspondência exata (Grupo B) ou essa métrica é específica de cache semântico (Grupo A)?

### 1.2 Estratégia de busca

Termos usados: `audit-prompt-caching sernote`, `cache-audit ussumant Claude Code`, `prompt-cache-skills OnlyTerp`, `CacheEval BudEcosystem false hit rate`, `semantic-cache-bench Akshitha024`, `Claude prompt caching cache breakpoint TTL invalidation`, `cache invalidation file content hash mtime git`, `RAG cache invalidation stale document versioning`. Ferramentas: WebSearch (busca) + WebFetch (captura verbatim de página real). Data de acesso de todas as fontes: **2026-09-28**.

---

## 2. Fontes classificadas [EXTERNO]

| ID | Fonte | Tipo | URL | Verbatim |
|---|---|---|---|---|
| SRC-01 | audit-prompt-caching (sernote) | Prática (auditoria estática) | github.com/sernote/audit-prompt-caching | `sources/SRC-01-audit-prompt-caching.txt` |
| SRC-02 | cache-audit (ussumant) | Prática (auditoria de 6 regras, Claude Code) | github.com/ussumant/cache-audit | `sources/SRC-02-cache-audit.txt` |
| SRC-03 | prompt-cache-skills (OnlyTerp) | Prática (implementação/correção automática) | github.com/OnlyTerp/prompt-cache-skills | `sources/SRC-03-prompt-cache-skills.txt` |
| SRC-04 | CacheEval (BudEcosystem) | Benchmark (correção — False-Hit Rate) | github.com/BudEcosystem/CacheEval | `sources/SRC-04-cacheeval.txt` |
| SRC-05 | semantic-cache-bench (Akshitha024) | Benchmark (desempenho — hit rate/custo/latência) | github.com/Akshitha024/semantic-cache-bench | `sources/SRC-05-semantic-cache-bench.txt` |
| SRC-06 | Documentação oficial Anthropic — Prompt Caching | Padrão (especificação de mecanismo nativo do provedor) | platform.claude.com/docs/en/build-with-claude/prompt-caching | `sources/SRC-06-anthropic-prompt-caching-docs.txt` |
| SRC-07 | "Cache Invalidation for AI" — TianPan.co | Prática (padrão de engenharia, RAG/documentos mutáveis) | tianpan.co/blog/2026-04-20-cache-invalidation-ai-semantic-rag | `sources/SRC-07-cache-invalidation-content-hash-rag.txt` |

Todas as fontes confirmadas por **fetch real** (WebFetch) nesta sessão — nenhuma foi presumida a partir da nota preliminar §9 de `CACHING SOT.MD` (essa nota é [PROPOSTA]/[INFERÊNCIA], não Dossiê — ela própria o declara, linha 263-265 do documento).

---

## 3. Achados por fonte e comparação com a arquitetura SOT

### SRC-01 — audit-prompt-caching (sernote)
**Achado confirmado:** ferramenta de auditoria **estática** — "It does not capture live traffic by itself." Opera sobre telemetria fornecida (payloads, traces, métricas de uso do provedor). Sua análise de "estabilidade de prefixo" é sobre **posição/ordem** de blocos no prompt (mover conteúdo variável para depois do conteúdo estável), não sobre versionamento de conteúdo de arquivo-fonte.
**Comparação SOT:** aplicável como auditoria complementar de *como* o Especificador/Revisor estruturam seus prompts (ex.: ordem de leitura ROADMAP→atomic-spec→RULES antes de conteúdo variável de sessão), mas **não resolve** o risco central do Grupo B (documento-fonte mudou entre leituras).
**Recomendação:** **adaptar** — usar como checklist de estruturação de prompt (F.3 Feedback), não como mecanismo de invalidação.

### SRC-02 — cache-audit (ussumant)
**Achado confirmado:** Skill específica do Claude Code, audita 6 regras nativas (ordenação, injeção de mensagem, estabilidade de ferramentas, troca de modelo, tamanho de conteúdo dinâmico, fork safety). Trecho literal (`sources/SRC-02-cache-audit.txt`): "1. Ordering — Dynamic data (timestamps, git status) in the system prompt / 2. Message injection — Editing the system prompt mid-session instead of using <system-reminder> tags". Nenhuma das 6 regras trata de staleness de conteúdo de arquivo do repositório.
**Comparação SOT:** as 6 regras são diretamente aplicáveis à operação **de sessão** do Especificador/Revisor no Claude Code (ex.: RULE 2 "message injection" reforça o uso de `<system-reminder>` em vez de editar o prompt de sistema em voo — já é a prática do harness SOT, ver system-reminders deste próprio ambiente). Não endereça o risco de conteúdo desatualizado de `ROADMAP.md`/`RULES.md`.
**Recomendação:** **adaptar** — auditoria complementar de higiene de sessão (F.3), fora do Enforcement Contract principal desta Spec.

### SRC-03 — prompt-cache-skills (OnlyTerp)
**Achado confirmado:** ferramenta de **correção automática** — aplica patches/diffs ao harness do agente ("lands the diff") após verificação de compatibilidade, sem exigir explicitamente confirmação humana antes de aplicar.
**Comparação SOT:** risco direto de colisão com **ENF-03** (LLM não é seu próprio gate; Detector ≠ Gate) e **INV-09** (sem baseline informal) se aplicada sem revisão humana explícita — o SOT não permite que um mecanismo automatizado altere configuração do próprio harness de especificação sem homologação (mesmo princípio que já levou à rejeição do acesso web do Revisor em BL-020/DHR-VERBATIM-SRC-001, por razão análoga: não misturar detector com gate).
**Recomendação:** **rejeitar a aplicação automática**; **adaptar** apenas o princípio de "correção com etapa de verificação" (a "Verify section" citada) como inspiração para um script determinístico que **relata** desalinhamento (nunca corrige sozinho) — coerente com o padrão já em uso em `scripts/check_doc_sync.py`/`scripts/backlog_triggers.py` (Detector, não Gate).

### SRC-04 — CacheEval (BudEcosystem)
**Achado confirmado:** benchmark de **correção semântica** — mede False-Hit Rate (FHR) em cache com correspondência por similaridade (embeddings), não em cache de correspondência exata. Trecho literal (`sources/SRC-04-cacheeval.txt`): "GPTCache's realistic default has a 68% false-hit rate — and 96% on adversarial pairs".
**Comparação SOT:** este é o risco do **Grupo A** (cache semântico de hipóteses/evidências — fora de escopo desta abertura). O Grupo B, conforme desenhado nesta proposta (§ EC-SPEC046-01 da Proposta de Abertura), usa **correspondência exata por hash de conteúdo**, não similaridade semântica — portanto a métrica FHR de CacheEval não se aplica diretamente ao mecanismo proposto para o Grupo B (correspondência exata não tem "quase-duplicatas"; ou o hash bate, ou não bate).
**Recomendação:** **adiar** — CacheEval é altamente relevante quando o Grupo A for aberto (cache de hipóteses por similaridade semântica seria exatamente o cenário que essa ferramenta mede); **não aplicável ao desenho de correspondência exata do Grupo B**.

### SRC-05 — semantic-cache-bench (Akshitha024)
**Achado confirmado:** benchmark de **desempenho** (hit rate, custo, latência, evictions) comparando ausência de cache, "Exact LRU" e cache semântico (FAISS/HNSW) em 12.000 consultas sintéticas. Trecho literal (`sources/SRC-05-semantic-cache-bench.txt`): "No Cache (baseline): 0% hit rate, baseline costs; Exact LRU: 15.3% hit rate, matches only identical queries; FAISS Semantic (HNSW): 71.4% hit rate, catches near-duplicates via cosine similarity" — não transferível numericamente ao padrão de releitura de documentos do SOT (cargas de trabalho muito diferentes: poucas dezenas de documentos-fonte relidos com alta frequência, não milhares de queries distintas).
**Comparação SOT:** o regime "Exact LRU"/correspondência exata do benchmark é o mais próximo do mecanismo proposto para o Grupo B, mas os números **não são utilizáveis como baseline** sem re-execução no ambiente real do SOT (o próprio `CACHING SOT.MD` §7 já alertava para isso — "os resultados são específicos à carga e à configuração do projeto").
**Recomendação:** **adaptar** — usar a metodologia (comparar baseline-sem-cache vs. candidata em hit rate/custo/latência) como molde do futuro Track de benchmark (D7/D8 da Spec formal), não os números.

### SRC-06 — Documentação oficial Anthropic (Prompt Caching)
**Achado confirmado — DECISIVO para o Enforcement Contract:** o cache nativo é keyed por **hash cumulativo de prefixo** em cada `cache_control` breakpoint. "Changing any block at or before the breakpoint produces a different hash on the next request" — ou seja, qualquer alteração de conteúdo em um bloco marcado invalida a entrada de cache **automaticamente** (produz um MISS, não um HIT com conteúdo velho). "Exact matching: Cache hits require 100% identical prompt segments." TTL padrão = 5 minutos (renovado a cada uso); TTL de 1h disponível.
**Comparação SOT:** este achado **reduz o escopo do risco real do Grupo B**. O mecanismo nativo da Anthropic já é fail-safe quanto a "servir bytes antigos de um bloco que mudou **dentro da mesma requisição/mesmo bloco**". O risco residual real não está no cache HTTP do provedor — está **um nível acima**: o Especificador/Revisor **lê um arquivo uma vez no início do turno/sessão e mantém esse conteúdo em contexto**; se o arquivo-fonte for alterado no repositório **entre** a leitura e o uso da informação (por outro agente, por Andraus, por um hook), o cache do provedor é irrelevante — o problema é de **re-leitura**, não de invalidação HTTP.
**Recomendação:** **adotar** o entendimento do mecanismo como base de risco (não há ação de "adotar a ferramenta" — é a plataforma já em uso), e **redirecionar o Enforcement Contract desta Spec** para o nível correto do problema: precondição de leitura fresca de arquivo-fonte antes de uma alegação carregada, não configuração de `cache_control`.

### SRC-07 — "Cache Invalidation for AI" (TianPan.co)
**Achado confirmado:** padrão de engenharia recomendado para sistemas onde "a resposta pode mudar": **chave de cache = hash do conteúdo do documento-fonte** (não apenas timestamp/ID) + **rastreamento de dependência** documento→resultado-cacheado, com invalidação **por evento de escrita**, não por TTL cego. Cita falha real de um sistema jurídico que servia contrato desatualizado porque "the retrieval cache was keyed on query embeddings, not document IDs, so there was no clean invalidation path."
**Comparação SOT:** é o padrão de **maior aderência direta** ao Grupo B — os documentos-fonte do SOT (`ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `backlog/RMR-001_Painel_Backlog.md`) são exatamente o tipo de "documento mutável, versão importa" que este padrão endereça. O SOT já possui um mecanismo análogo de dependência/detector-não-gate em `scripts/check_doc_sync.py` (drift de sincronização) e `scripts/build_map.py --check` (defasagem do mapa) — reforça que o padrão já é familiar à arquitetura do harness.
**Recomendação:** **adotar** (adaptado) — usar hash de conteúdo (ex.: SHA-256) + mtime/git como precondição de validade de qualquer conteúdo de arquivo-fonte mantido "em cache" (em contexto ou em qualquer estrutura auxiliar) pelo Especificador/Revisor. Ver Enforcement Contract EC-SPEC046-01 na Proposta de Abertura.

---

## 4. Lacunas e conflitos (a pesquisa NÃO fecha decisão aberta — CONS-01)

- **Nenhuma das 5 ferramentas do benchmark original (§3.1 de `CACHING SOT.MD`) resolve, isoladamente, o risco central do Grupo B** (staleness de arquivo-fonte relido pelo agente) — confirma o próprio achado do documento-fonte (§4 da matriz: "Verificar validade temporal de dados... Insuficiente — Harness específico do SOT"), agora estendido ao domínio spec-time.
- **CacheEval (SRC-04) e semantic-cache-bench (SRC-05) medem regimes de cache SEMÂNTICO/aproximado** — o desenho proposto para o Grupo B (correspondência exata por hash) não passa pelos mesmos riscos que essas ferramentas medem. Isso não as torna inúteis — ficam **adiadas** para quando o Grupo A (cache de hipóteses, onde similaridade semântica é plausivelmente necessária) for aberto.
- **Não há benchmark real do padrão hash-de-conteúdo + dependência (SRC-07) aplicado a um harness de especificação como o SOT** — é um padrão de engenharia geral (RAG/documentos mutáveis), não uma ferramenta pronta para acoplar. A Spec formal (Plan, gate seguinte) precisará desenhar o mecanismo de captura de hash (provavelmente via `scripts/`), não importar uma ferramenta.
- **Validade/prazo do Dossiê:** decisão aberta **ECC-VAL-001** (ainda não resolvida por Andraus) — este Dossiê fica sujeito a essa decisão futura como qualquer outro.
- **[DECISÃO NECESSÁRIA]** — se a Spec formal deve reutilizar `scripts/check_doc_sync.py` (já existe, já detecta drift de decisões/RULE/estado) como veículo do mecanismo de hash-de-conteúdo, ou se precisa de um script novo dedicado a "freshness de leitura por agente". Não resolvido neste Dossiê — proposto como primeira pergunta de design do Plan (gate seguinte, após homologação desta abertura).

---

## 5. Escopo/quantidade resultantes e proposta de re-apontamento de gatilhos do RMR-001

**Escopo resultante desta rodada:** 1 (uma) Spec cobrindo exclusivamente o Grupo B (spec-time, Especificador/Revisor). Grupo A **não** é aberto nesta rodada — ver justificativa de faseamento na Proposta de Abertura, §"Faseamento explícito A vs. B".

**Capacidades cobertas (RULE-ECC-01 — "capacidade exigida sem Spec ao fim de uma fase = achado de gate", `governance/RULES.md:426-436`):** "caching de prompt/contexto para agentes de spec-time" — capacidade nova, não constava da lista de capacidades exigidas do ROADMAP §26 (que é derivada dos títulos dos slots de domínio 002-045); é adjacente, em natureza, à FASE GOV (019/020/021 — governança do próprio harness), não à Trilha B de domínio de trading.

**Re-apontamento de gatilhos do RMR-001 (§3 do RMR-001):** o item **BL-024** tem hoje gatilho `evento:abertura da SPEC-002` (pré-condição a validar ANTES de SPEC-002 abrir). Esta abertura (SPEC-046) **satisfaz e supera** essa pré-condição para o Grupo B especificamente — as ações de validação (1)-(3) do BL-024 já estavam concluídas antes desta sessão; a ação (4) (precondição CHM-001 verificável) permanece **explicitamente fora de escopo** para esta rodada (aplica-se só ao Grupo A). Proposta de re-apontamento: **BL-024 mantém seu gatilho original** (ele é sobre a validação pré-SPEC-002 como um todo, ambos os grupos), mas esta abertura de SPEC-046 deve ser **registrada como nova linha aditiva** no RMR-001 (não substitui BL-024), com o encaminhamento específico do Grupo B. O Controlador/Andraus decide o registro formal no gate (ROADMAP §23 passo 11-bis).
