# Dossiê de Pesquisa — SPEC-046 (companion — convenção de nome do gate determinístico)

**Nota de proveniência:** o Dossiê de Pesquisa **autoral e homologado** desta Spec é `specs/features/SPEC-046/DOSSIE-PESQUISA.md` (homologado junto da abertura — DHR-SPEC046-001, 2026-09-28, junto de `PROPOSTA-ABERTURA.md`). Este arquivo `research.md` existe **apenas** para satisfazer a convenção de nome de arquivo que `scripts/validate_spec_sot.py` (check `[STRUCT-11] Dossiê de Pesquisa presente`) procura na mesma pasta de uma Spec que cita `RULE-ECC-01/02` — o script busca literalmente `research.md`. Não há dois Dossiês distintos: este arquivo é um espelho/companion do conteúdo homologado, não um documento concorrente. Em caso de qualquer divergência textual entre os dois (não deveria haver), `DOSSIE-PESQUISA.md` prevalece, por ser o nome citado explicitamente em `DHR-SPEC046-001`.

---

## Dossiê de Pesquisa — resumo executivo (ver `DOSSIE-PESQUISA.md` para o texto completo homologado)

**Escopo:** SOMENTE Grupo B (caching de spec-time, Especificador/Revisor) — Grupo A explicitamente fora de escopo, adiado (decisão de Andraus, 2026-09-28).

**Fontes classificadas `[EXTERNO]` (7, todas com captura verbatim em `sources/SRC-01..07-*.txt`, RULE-ECC-04):**

| ID | Fonte | Tipo | Recomendação |
|---|---|---|---|
| SRC-01 | audit-prompt-caching (sernote) | Prática | adaptar |
| SRC-02 | cache-audit (ussumant) | Prática | adaptar |
| SRC-03 | prompt-cache-skills (OnlyTerp) | Prática | rejeitar (aplicação automática) / adaptar (princípio de verificação) |
| SRC-04 | CacheEval (BudEcosystem) | Benchmark (False-Hit Rate) | adiar (mede cache semântico — Grupo A) |
| SRC-05 | semantic-cache-bench (Akshitha024) | Benchmark (desempenho) | adaptar (metodologia, não números) |
| SRC-06 | Documentação oficial Anthropic — Prompt Caching | Padrão | adotar (entendimento do mecanismo nativo — redireciona o risco real) |
| SRC-07 | "Cache Invalidation for AI" — TianPan.co | Prática | adotar (adaptado — base do EC-SPEC046-01) |

**Achado decisivo (SRC-06):** o cache nativo da Anthropic é keyed por hash cumulativo de prefixo — qualquer alteração em um bloco marcado invalida a entrada automaticamente (MISS, nunca HIT com conteúdo velho). O risco real do Grupo B não está nesse mecanismo — está um nível acima: a cópia em **contexto de sessão** de um documento-fonte pode ficar desatualizada se o arquivo mudar no repositório entre a leitura e o uso.

**Achado de maior aderência (SRC-07):** padrão de chave de cache = hash de conteúdo do documento-fonte + rastreamento de dependência, com invalidação por evento de escrita — base do Enforcement Contract EC-SPEC046-01 (`plan.md`).

**Lacunas/conflitos (CONS-01 — não fecham decisão aberta):** nenhuma das 5 ferramentas resolve isoladamente o risco central do Grupo B; CacheEval/semantic-cache-bench medem regime semântico (não aplicável ao desenho de correspondência exata do Grupo B); veículo técnico de implementação (script novo vs. `scripts/check_doc_sync.py` estendido) permanece `[DECISÃO NECESSÁRIA]`, não resolvido neste Dossiê nem no Plan.

**Texto completo, questões de pesquisa, estratégia de busca, achados por fonte com comparação explícita adotar/adaptar/rejeitar/adiar, e proposta de re-apontamento de gatilhos do RMR-001:** ver `specs/features/SPEC-046/DOSSIE-PESQUISA.md` (documento homologado, DHR-SPEC046-001).
