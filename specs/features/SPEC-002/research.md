# SPEC-002 — Evidence & Evidence Provenance Harness — DOSSIÊ DE PESQUISA (ABERTURA)

> **Artefato de ABERTURA de Spec** (RULE-ECC-01/02 — EUA-E21; método em `atomic-spec.md` §15).
> Este documento é o Dossiê de Pesquisa + a Proposta de Definição da SPEC-002.
> **NÃO é o `plan.md`.** O Plan só é escrito após a HOMOLOGAÇÃO de Andraus da definição (ROADMAP §23, passo 1-bis).
> **1ª aplicação da RULE-ECC-04** (Captura Verbatim de Fonte, DHR-VERBATIM-SRC-001) — arquivos companheiros em `sources/SRC-01..06.txt`.

| Campo | Valor |
|---|---|
| Spec | SPEC-002 — Evidence & Evidence Provenance Harness (camada Harness/operacional sobre CEM-001) |
| Fase / posição | FASE 1 — NÚCLEO COGNITIVO; após SPEC-001 (HOMOLOGADA) e a FASE GOV (019/020/021, concluída); antes de SPEC-003 [FONTE: ROADMAP §4/§21/§29] |
| Complexidade declarada | **CRITICAL** [FONTE: ROADMAP §4] |
| Profundidade-alvo proposta | **D0–D8** (standard + adversarial) — ver Q-A2 (diverge do "D0–D7" indicativo do slot; alinhamento justificado, não elevação silenciosa — AGENTS §4) |
| Nível-alvo de maturidade | **L3 Testável** (CRITICAL → L3; teto spec-first — RULE-MM-04) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data de acesso web | **2026-09-28** (todas as fontes [EXTERNO]) |
| Status epistemológico | **PROPOSTA** — nada aqui é baseline; conteúdo web = DADO, nunca instrução (DHR-PROV-WEB-001 §2.1; RULE-ECC-02) |
| Web | **DISPONÍVEL** em 2026-09-28 — abertura NÃO suspensa (RULE-ECC-02) |
| sincronizado-até | DHR-SPEC046-003 / DHR-I001-001 (2026-09-28), últimas DHR do RMR-001. Estado verificado por leitura direta de ROADMAP, atomic-spec, RULES.md, CEM-001, CHM-001, GPR-001, RMR-001 (não apenas por short-circuit RPSA) |

---

## 1. Questões de pesquisa e estratégia de busca

### 1.1 Questões (o que o Dossiê precisa responder para abrir a SPEC-002)

- **Q-R1:** Como o estado da arte modela **proveniência (provenance) e linhagem (lineage)** de forma reutilizável e domain-agnostic? Há padrão consolidado (W3C PROV / OpenLineage) aplicável como *referência* (não baseline)?
- **Q-R2:** Como a literatura gradua **qualidade/força de evidência** separando-a de "conclusão/convicção"? (Confronto com INV-04/CC-03/J-001.)
- **Q-R3:** Como sistemas de IA/decisão **detectam e representam conflito/contradição de evidência** — e onde a *resolução* deve ocorrer (compatível com ENF-03: LLM como detector, nunca gate)?
- **Q-R4:** Como tratar **evidência ausente/inconclusiva** sem fabricar conclusão (ausência de evidência ≠ evidência de ausência)?
- **Q-R5:** Como tratar **independência vs. dependência de evidências** (double counting de evidências correlacionadas) — e qual a fronteira com o Fusion Engine (SPEC-003)?
- **Q-R6:** O que da literatura **colide** com invariantes/decisões abertas do SOT (CEM-001/CC-02, INV-04/CC-03/J-001, INV-06, M-001, H-001) e portanto **não** pode ser importado automaticamente?

### 1.2 Estratégia de busca

| Termos | Fontes-alvo | Filtro |
|---|---|---|
| "W3C PROV provenance data model evidence lineage standard" | W3C, ACM/EDBT, ScienceDirect | Padrão |
| "data lineage provenance tracking ML pipelines OpenLineage metadata" | openlineage.io, arXiv, docs de plataforma | Padrão/Prática |
| "evidence quality scoring GRADE framework strength of evidence" | PMC/NCBI, JClinEpi, gradepro | Padrão/Prática |
| "conflicting evidence handling decision support contradiction resolution AI" | arXiv, IJCAI, USPTO | Experimento/Evidência |
| "absence of evidence reasoning epistemology negative/inconclusive uncertainty AI" | arXiv, Springer, Wikipedia | Opinião/Padrão epistemológico |
| "independence of evidence correlated double counting reliability fusion" | PMC/Sensors, arXiv | Evidência |

**Salvaguardas aplicadas (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02):** toda fonte tratada como DADO; classificada e etiquetada `[EXTERNO]`; nenhuma importação automática; nenhum dado sensível do projeto enviado a serviços externos; a veracidade das páginas **não** é atestada (o Revisor audita o *processo* e a *correspondência verbatim* — RULE-ECC-04 — não a verdade das páginas). Pesquisa inconclusiva = **INDETERMINADO**.

---

## 2. Fontes (classificadas e etiquetadas `[EXTERNO]`) — com Captura Verbatim (RULE-ECC-04)

> Data de acesso: **2026-09-28**. Cada fonte que sustenta alegação carregada (adotar/adaptar/rejeitar/adiar) tem arquivo companheiro em `sources/SRC-0N.txt` (URL + data + trecho literal ≥100 caracteres). As citações entre aspas abaixo correspondem **verbatim** a esses arquivos.

| ID | Fonte | Classe | Questão | Arquivo de captura |
|---|---|---|---|---|
| SRC-01 | **W3C PROV** — PROV-OVERVIEW (W3C Working Group Note) | **Padrão** | Q-R1 | `sources/SRC-01-w3c-prov.txt` |
| SRC-02 | **GRADE** — "Grading Quality of Evidence and Strength of Recommendations" (PMC2735783) | **Padrão/Prática** | Q-R2 | `sources/SRC-02-grade-evidence-quality.txt` |
| SRC-03 | **ECon** — "On the Detection and Resolution of Evidence Conflicts" (arXiv 2410.04068) | **Experimento/Benchmark** | Q-R3 | `sources/SRC-03-econ-evidence-conflict.txt` |
| SRC-04 | **OpenLineage** — open standard for data lineage | **Padrão/Prática** | Q-R1 | `sources/SRC-04-openlineage.txt` |
| SRC-05 | **"Evidence of absence"** — princípio epistemológico (Wikipedia) | **Opinião/Padrão epistemológico** | Q-R4 | `sources/SRC-05-evidence-of-absence.txt` |
| SRC-06 | **"Fusion of Dependent Evidence"** (Sensors 2017; PMC5676609) | **Evidência** | Q-R5 | `sources/SRC-06-dependent-evidence-fusion.txt` |

**Fontes de contexto (não sustentam alegação carregada — sem arquivo obrigatório, RULE-ECC-04):** survey de contradiction resolution em decision support (epistemic vs. stochastic; Dempster-Shafer/possibility theory) — usado apenas como panorama de Q-R3, sem decisão adotar/adaptar/rejeitar/adiar dependente dele.

### 2.1 Citações verbatim das fontes carregadas

- **SRC-01 (W3C PROV) [EXTERNO, Padrão]:** *"Provenance is information about entities, activities, and people involved in producing a piece of data or thing, which can be used to form assessments about its quality, reliability or trustworthiness."*
- **SRC-02 (GRADE) [EXTERNO, Padrão/Prática]:** *"GRADE defines the quality of evidence as the collective level of confidence guideline developers have about the validity of estimates of benefits and harms for any given intervention"* — e *"Factors affecting certainty—study design, risk of bias, inconsistency, indirectness, imprecision, and publication bias—are considered in rating the certainty or confidence in evidence."*
- **SRC-03 (ECon) [EXTERNO, Experimento]:** *"NLI and LLM models are high precision conflict detectors. As a general trend, the NLI and LLM models have high precision but low recall on the detection task."* — e *"LLMs frequently bias towards one of the conflicting evidence without stating reasons, accounting for 23.7% and 38.1% of the time for Claude 3 Sonnet and Haiku, respectively."*
- **SRC-04 (OpenLineage) [EXTERNO, Padrão/Prática]:** *"OpenLineage is an open platform for collection and analysis of data lineage that tracks metadata about datasets, jobs, and runs, giving users the information required to identify the root cause of complex issues and understand the impact of changes."*
- **SRC-05 (Evidence of absence) [EXTERNO, Padrão epistemológico]:** *"The expectation of evidence makes its absence significant."*
- **SRC-06 (Dependent Evidence Fusion) [EXTERNO, Evidência]:** *"Classical evidence theory assumes evidence is independent of each other, which is often unrealistic, and ignoring relationships between evidence may lead to unreasonable fusion results and wrong decisions."*

---

## 3. Comparação com a arquitetura SOT e os modelos canônicos (adotar / adaptar / rejeitar / adiar)

> Regra: nada entra como baseline; cada item confronta a arquitetura homologada. **CEM-001 é BASELINE e NÃO pode ser redefinido (CC-02/CONST-01).** Cobertura interna existente é preservada; só se aprofunda o insuficiente (ROADMAP R1/R4/§24).

### 3.1 O que o CEM-001 já cobre (não redefinir — CC-02) [FONTE]

O CEM-001 (baseline) já define, como **estrutura do objeto** Evidência: identidade/versão/status; origem (`Producer Type` AGENT/ENGINE, `Producer ID`, `Evidence Origin Type` PRIMARY/DERIVED); conteúdo cognitivo (`Domain`, `Observation`, `Interpretation`, `Technical Rationale`, `Evidence Strength` 0.0–1.0, `Timeframe Reference`, `Market Context`); rastreabilidade (`Source Reference`, `Lineage`); ciclo de vida (ACTIVE→SUPERSEDED→INVALIDATED→ARCHIVED + transições permitidas/proibidas); linhagem (primária vazia / derivada obrigatória; Cognitive Trace Reconstruction = capacidade do Knowledge Graph; Cognitive Depth = métrica derivada); eventos canônicos (Evidence Created/Superseded/Invalidated/Archived, propagados via EC-COG-005); papéis PRODUCER/CONSUMER/REPOSITORY; conformidade/certificação; governança via GMC-001.

**Consequência:** a SPEC-002 **constrói SOBRE** o CEM-001 — especifica a **camada Harness/operacional** (o *como opera*), nunca a estrutura do objeto (o *que é*). Mesmo padrão da SPEC-001 sobre CHM-001. [INFERÊNCIA a partir de ROADMAP §4/§78 e CEM-001]

### 3.2 Tabela de decisão

| Tema do slot §4 | Cobertura SOT já existente [FONTE] | Fonte externa | Decisão | Porquê |
|---|---|---|---|---|
| **Origem / provenance / ferramenta / Skill que produziu** | CEM-001 Camada 2 (Producer Type/ID; PRIMARY só AGENT, DERIVED só ENGINE) + Camada 4 (Source Reference); INV-06 (Evidência≠Observação); PC-03 | SRC-01 (W3C PROV), SRC-04 (OpenLineage) | **ADAPTAR** (vocabulário/método de provenance como referência) + **ADOTAR conceito** já-SOT de rastreabilidade produtor→fonte | CEM-001 é o idioma canônico (INV-10/CC-02); PROV/OpenLineage fornecem método de referência para a camada *operacional* de provenance, não um modelo a adotar |
| **Tipo / qualidade / força de evidência** | CEM-001 `Evidence Strength` (peso local do produtor, ≠ Convicção); CHM-001 §1.9/§2.14 (não-equivalência); INV-04; PC-04 | SRC-02 (GRADE) | **ADAPTAR** (tipificar qualidade/força por método, qualitativo) | Reforça a separação Strength(local) ≠ Convicção Global (CCM-001/J-001). Nenhuma escala numérica adotada (J-001 aberto — CC-03) |
| **Independência de evidência** | RULE-004 ("evidências causalmente relacionadas contadas como uma única"); AP-02 (confluência falsa); PE-08 (independência de perspectivas); RULE-MET-01 (não afirmar independência não verificada) | SRC-06 (dependent evidence fusion) | **ADIAR** (mecânica de desconto/fusão) + **ADAPTAR** (independência como *atributo operacional* representado) | A REPRESENTAÇÃO da (in)dependência é da SPEC-002; a MECÂNICA de fusão de dependentes é do Fusion Engine (SPEC-003) |
| **Evidência favorável / contraevidência / inconclusiva / ausente** | CHM-001 §2.10 (`supporting_/refuting_evidence_ids`); PB-10 (preservar incerteza); RULE-UNC-01..03; RULE-PRB-02 | SRC-05 (evidence of absence) | **ADAPTAR** (representar explicitamente "ausente/inconclusiva" distinta de contraevidência) | Ausência de evidência ≠ evidência de ausência; tratar sob RULE-EPI/UNC/MET-01 sem fabricar conclusão |
| **Conflito de evidência** | PB-09 (conflito registrado, nunca suprimido); RULE-005 (conflito direcional); ENF-03 (LLM detector≠gate) | SRC-03 (ECon) | **ADAPTAR** (DETECTAR e REPRESENTAR conflito) + **fronteira**: NÃO resolver na camada de evidência | ECon mostra LLM como detector viesado na resolução; SOT registra/detecta conflito, resolução vai p/ Fusion→Conviction→Synthesis (SPEC-003/014) |
| **Provenance / versão** | CEM-001 identidade/versão + imutabilidade pós-publicação (Status único mutável); INV-07 | SRC-01, SRC-04 | **ADOTAR conceito já-SOT** (versionamento monotônico) | Já é FATO NORMATIVO (INV-07); externo apenas corrobora |
| **Temporalidade** | CEM-001 `Timeframe Reference`, `Creation Timestamp`, `Market Context`; RULE-CAU-02 (regime) | SRC-02 (indirectness/imprecision) | **ADAPTAR** (aging/staleness como *representação* operacional) | Peso/decay temporal ligado a convicção → J-001/SPEC-003 (não fixar aqui) |
| **Relação com hipótese** | CHM-001 §2.10 + SPEC-001 (fronteira `Fonte→Dado→Evidência→Hipótese` já especificada); INV-06 | — (interno) | **ADOTAR fronteira SOT** (referência a SPEC-001, sem redefinir) | A ligação evidência↔hipótese já foi especificada na SPEC-001; a SPEC-002 opera do lado da Evidência |
| **Provenance em runtime / storage físico** | CEM-001 diz que Blackboard/KG são REPOSITORY | SRC-04 | **ADIAR** | Storage físico e Cognitive Trace Reconstruction → SPEC-004/006 (M-001, H-001) |

### 3.3 Fronteira `Fonte → Dado → Evidência → Hipótese` (ROADMAP §4/§138) [FONTE + INFERÊNCIA]

- **Fonte** (Source Reference — CEM-001) e **Dado** (Observação de Skill — INV-06, determinística, sem interpretação) são **a montante** da Evidência.
- **Evidência** (interpretada por Agente/Engine — CEM-001) é o objeto da SPEC-002.
- **Hipótese** (CHM-001) é **a jusante** — a transição Evidência→Hipótese já foi especificada pela SPEC-001 (`supporting_/refuting_evidence_ids`).
- A SPEC-002 especifica **o segmento Fonte→Dado→Evidência** em operação (produção, publicação, provenance, qualidade, independência, conflito, ausência, versão, ciclo de vida operacional), **referenciando** — sem redefinir — CEM-001 (objeto), CHM-001/SPEC-001 (jusante) e SPEC-004/006 (storage). [INFERÊNCIA — sujeita a homologação]

### 3.4 Modelos canônicos — fronteiras (CC-02)

- Nenhuma decisão ADOTA/ADAPTA redefine CEM-001 (estrutura, campos, ciclo de vida, linhagem, eventos, governança) nem CHM-001. **CCM-001 permanece pendente (SPEC-003)** — nenhum limiar/peso ligado a convicção é fixado aqui (J-001/CC-03). Evidence Strength permanece **local do produtor** (CEM-001), jamais promovido a Convicção (INV-04).

---

## 4. Lacunas, conflitos e INDETERMINADOS (NÃO fecham decisão aberta — CONS-01)

- **CONFLITO-1 — LLM como resolvedor de conflito de evidência vs. ENF-03.** SRC-03 evidencia LLMs resolvendo conflito com viés não-explicado. **Resolução na Spec:** camada de evidência apenas DETECTA/REPRESENTA conflito (LLM = detector); RESOLUÇÃO fica em Fusion→Conviction→Synthesis (SPEC-003/014). Não é decisão aberta nova (já normado por ENF-03/PB-09). [FONTE: atomic-spec §5/§10; GPR-001 §3.3]
- **CONFLITO-2 — escalas numéricas de qualidade/força (GRADE) vs. J-001/CC-03.** Adotar escala numérica de qualidade→convicção colidiria com J-001 (fórmula/pesos/limiares definitivos abertos) e INV-04. **Rejeitar** qualquer número; tipificação **qualitativa** apenas. [FONTE: J-001; INV-04]
- **CONFLITO-3 — modelo de proveniência externo (PROV/OpenLineage) vs. CEM-001 canônico.** Adotar PROV/OpenLineage como modelo colidiria com CC-02/INV-10. **Rejeitar** como baseline; admitir só como **referência de método**. [FONTE: CEM-001; INV-10]
- **GAP-1 — estados do Blackboard para Evidência.** A publicação operacional de Evidência no Blackboard depende de **M-001** (estados do Blackboard para objetos NÃO-hipótese — SPEC-004, aberta). A SPEC-002 especifica o **protocolo de publicação** referenciando o ciclo de vida do CEM-001, mas **não** fecha os estados do Blackboard. **[DECISÃO NECESSÁRIA: M-001]** — marcar no Plan; não tratar como fechado (CONS-01). [FONTE: atomic-spec §12; RULES RULE-BB-003]
- **GAP-2 — mecânica de fusão de evidências dependentes.** SRC-06 confirma maturidade externa, mas a mecânica (desconto por correlação) depende do **Fusion Engine (SPEC-003)** e de **J-001**. **INDETERMINADO até SPEC-003/J-001.** A SPEC-002 só representa o atributo de (in)dependência. [FONTE: ROADMAP §4; J-001]
- **GAP-3 — reconstrução expandida de linhagem (Cognitive Trace Reconstruction).** É capacidade do Knowledge Graph (**H-001/SPEC-006**), não da camada operacional de evidência. **ADIADO** (CEM-001 Cap.5 já atribui ao KG). [FONTE: CEM-001 Cap.5; H-001]
- **GAP-4 — evidência DERIVED e Fusion Engine como produtor.** CEM-001 autoriza o Fusion Engine como único ENGINE PRODUCER de evidência DERIVED. A produção DERIVED **operacional** pertence à SPEC-003 (Fusion). A SPEC-002 cobre a produção **PRIMARY** (Agentes) e o contrato geral de publicação; a fronteira PRIMARY/DERIVED deve ser declarada no Plan sem antecipar a mecânica de fusão. [FONTE: CEM-001 Cap.2/Cap.6]

Nenhuma decisão aberta é fechada por esta pesquisa (RULE-ECC-02 / CONS-01).

---

## 5. Proposta de Definição da SPEC-002 (para homologação de Andraus)

### 5.1 Número, nome, quantidade, decomposição — [PROPOSTA]

- **Número:** **SPEC-002** (slot mantido; número monotônico, não reutilizado — RULE-ECC-01).
- **Nome:** **Evidence & Evidence Provenance Harness** (mantido).
- **Quantidade:** **1 (uma) Spec — não decomposta.**
  - *Porquê:* a camada operacional de Evidência forma um **contrato coeso** sobre um único objeto canônico (CEM-001); decompor (ex.: "Evidence Registry" vs. "Provenance" vs. "Conflict") fragmentaria um harness único e multiplicaria fronteiras sem ganho de atomicidade (ROADMAP §24). A **fusão** de evidência (Fusion Engine) já é slot separado (SPEC-003) — não é candidata a fusão com SPEC-002.

### 5.2 Missão (comportamental, sem implementação) — [PROPOSTA]

Especificar **como o SOT produz, publica, versiona, rastreia (provenance), qualifica, relaciona e encerra Evidências Cognitivas em operação** — a camada Harness/operacional sobre o CEM-001 (baseline, não redefinido) —, garantindo rastreabilidade Fonte→Dado→Evidência, representação explícita de evidência favorável/contra/inconclusiva/ausente, e **detecção e registro** (nunca resolução silenciosa) de conflito e de (in)dependência entre evidências, com gate determinístico e o LLM apenas como detector (ENF-03).

### 5.3 Escopo (dentro) — [PROPOSTA]

1. **Evidence Registry como serviço lógico:** alocação de ID, versionamento monotônico operacional, índice de estado ativo, API de consulta/reconstrução histórica (espelho operacional do Hypothesis Registry da SPEC-001; storage físico → SPEC-004/006).
2. **Protocolo de produção/publicação de Evidência** (D6): o que publicar, quando, em que ordem, com que versionamento — referenciando o contrato do CEM-001; fronteira produtor PRIMARY (Agente) vs. DERIVED (Fusion Engine — só contrato de fronteira, mecânica em SPEC-003).
3. **Camada operacional de provenance:** rastreabilidade produtor→fonte→dado→evidência; ferramenta/Skill que produziu; INV-06 (Observação de Skill ≠ Evidência de Agente) como gate.
4. **Qualidade/força operacional:** uso operacional de `Evidence Strength` (local do produtor) SEM promoção a Convicção (INV-04/CC-03); tipificação qualitativa de qualidade (adaptada de GRADE).
5. **Independência/dependência** como atributo operacional representado (anti-double-counting — RULE-004); mecânica de desconto/fusão adiada (SPEC-003).
6. **Tipologia operacional:** evidência favorável / contraevidência / inconclusiva / **ausente** — representação distinta e tratamento sob RULE-EPI/UNC/MET-01 (ausência ≠ evidência de ausência).
7. **Detecção e registro de conflito** de evidência (PB-09) — nunca resolução (fronteira com SPEC-003/014).
8. **Temporalidade/aging operacional** (representação de staleness; peso temporal → J-001).
9. **Ciclo de vida operacional** (ACTIVE→SUPERSEDED→INVALIDATED→ARCHIVED) e **avaliação de impacto de invalidação** referenciando CEM-001 Cap.4/Cap.5 (sem redefinir).
10. **Protocolo de publicação no Blackboard** para Evidência (D6) — **referenciando** M-001 como decisão aberta (não fechando estados do Blackboard).
11. **Enforcement Contracts** dos atos com efeito (publicação/commit de evidência): piso **E2** (Evidência/Agente — atomic-spec §10.2); E3 onde houver commit crítico/irreversível.
12. **Auditabilidade (D9 por referência):** o que a camada deve suportar para reconstrução (P13), delegando Cognitive Trace Reconstruction ao KG (SPEC-006).

### 5.4 Fora do escopo (Non-goals) — [PROPOSTA]

- Redefinir CEM-001 (estrutura, campos, ciclo de vida, linhagem, eventos, governança) ou CHM-001 — **CC-02/CONST-01**.
- **Fórmula/mecânica de fusão** de evidências (Fusion Engine) e cálculo de evidência DERIVED → **SPEC-003**.
- Conviction Vector / convicção a partir de evidência; qualquer limiar numérico → **SPEC-003 / J-001 / CCM-001**.
- **Estados do Blackboard** para objetos não-hipótese → **M-001 / SPEC-004**.
- **Storage físico** de evidência (Blackboard/KG) e Cognitive Trace Reconstruction → **SPEC-004 / SPEC-006 / H-001**.
- RAG / formação de conhecimento (evidence candidate a partir de retrieval) → **SPEC-007**.
- Estrutura da hipótese e transição a jusante → **CHM-001 / SPEC-001**.
- Resolução de conflito de evidência → **SPEC-003 / SPEC-014**.

### 5.5 Capacidades §26 cobertas

- Cobre integralmente a capacidade **"SPEC-002 — Evidence & Evidence Provenance Harness"** (ROADMAP §26) na dimensão da **camada operacional sobre CEM-001**. Capacidades a jusante (fusão, convicção, storage, KG, RAG) permanecem em seus slots — **não** são achados de gate (estão em slots próprios).

### 5.6 Herança prevista (a declarar no Plan — CC-08 / RULE-HV / RULE-HD) — [PROPOSTA]

- **INHERITS (por ID+versão baseline — RULE-HD-04):** CEM-001 (baseline, DHR-TAX-001) como objeto canônico; CHM-001 (baseline) na fronteira a jusante; **SPEC-001 v1.1 baseline** (fronteira Fonte→Dado→Evidência→Hipótese; Registry como serviço lógico); atomic-spec v1.4→**v1.5** (a confirmar — ver §6); ENF-01..08 (ênfase ENF-03); Quality Gates L1–L4; INV-04/06/07/09/10; 4Es (CEE-001 §12).
- **ADDED:** camada operacional de evidência (itens §5.3).
- **REMOVED:** vazio (nada suprimido do herdado — RULE-HD-03).
- Eixo vertical (RULE-HV): SPEC-002 não é filha direta de uma macro-spec da FASE GOV; herança é sobre modelos canônicos (CC-08) — a confirmar no Plan.

### 5.7 Método vigente e a questão da v1.5

- **Piloto de incorporação (atomic-spec v1.5):** as 11 famílias RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET têm incorporação física **diferida ao piloto da SPEC-002** (RULE-REG-001, §5.9). A SPEC-002 é a primeira Spec sob CC-11/CC-12/RULE-ECC-04/RULE-MM. Se a v1.5 for homologada junto desta abertura, a SPEC-002 já a usa; caso contrário, opera sob v1.4 + emendas vigentes (as regras já são FATO NORMATIVO com vigência imediata). **Ver Q-A5.**

### 5.8 Avaliação de aplicabilidade das 5 regras homologadas 2026-09-27/28 (explícita — não em silêncio)

**(1) RULE-MECH-01 / CC-11 (Classe D/H/P/C por BASpec) — INCIDE.** [FONTE: RULES RULE-MECH-01; ROADMAP §29]
- A abertura é posterior à homologação (2026-09-27) e SPEC-002 é "em diante". Cada BASpec com efeito declarará Classe no Plan. **Preview [INFERÊNCIA, a confirmar no Plan]:** alocação de ID/versionamento do Registry = **Classe D** (determinístico); gate de conformidade de provenance/INV-06 e gate de publicação = **Classe C** (constitutivo, fail-closed); detecção de conflito/independência = **Classe P** (detector probabilístico + bounded loop + parada) ou **H** (com gate de saída determinístico). Declaração por BASpec, nunca por Spec inteira (SES-001 §50).

**(2) RULE-PD-01 / CC-12 (PD-xx por Spec de especialidade) — NÃO INCIDE. [PROPOSTA de N/A — confirmar Q-A3]**
- **Justificativa (mesmo padrão do N/A de SPEC-020/021):** RULE-PD-01/atomic-spec §10.7 só se aplica quando a Spec **define escopo de especialidade** (ex.: Elliott, SMC, ICT — julgamento de domínio de mercado). A SPEC-002 é **camada Harness/operacional sobre o CEM-001**, que é por definição **domain-agnostic / neutro de domínio** (CEM-001 Princípio 1 Neutralidade; Cap.2 "Neutralidade de Domínio"). Ela governa **como a evidência circula** (infraestrutura cognitiva transversal), **não o que o mercado significa** — não produz sub-princípios operacionais de uma escola analítica. Portanto, como SPEC-019/020/021 (governança/meta-harness), **não declara `PD-xx`**. Os `PD-xx` serão declarados pelas Specs analíticas SPEC-010..014 (Elliott/SMC/ICT), que definem especialidade de domínio. O catálogo GPR-001 §2.7 permanece vazio até lá (a nota do §2.7 "primeira declaração esperada na abertura de SPEC-002" é **expectativa indicativa, não obrigação** — cai por não-aplicabilidade material, registrada aqui explicitamente para o Revisor; não é supressão silenciosa).

**(3) RULE-MM-01 (escada de maturidade L0–L4, gate normativo E3) — INCIDE.** [FONTE: RULES RULE-MM-01/04/05]
- SPEC-002 declara **nível-alvo L3 Testável** (CRITICAL → L3; teto spec-first, pois L4 exige D9 + backtest + aprovação de Andraus na implementação — RULE-MM-04). Gate normativo E3 na homologação: nível atingido < alvo ⇒ inelegível (RULE-MM-05). Progressão staged (RULE-MM-03); atribuição determinística, não por volume (RULE-MM-02); sem limiar numérico dependente de convicção (RULE-MM-06/J-001).

**(4) RULE-ECC-04 (Captura Verbatim de Fonte) — INCIDE e JÁ APLICADA nesta abertura.** [FONTE: RULES RULE-ECC-04]
- 6 fontes carregadas → 6 arquivos `sources/SRC-01..06.txt` (URL + data 2026-09-28 + trecho literal ≥100 caracteres); citações verbatim entre aspas no §2.1. Capturas por WebSearch (SRC-06; WebFetch bloqueado por reCAPTCHA) e parte de SRC-04 registradas com método honesto (RULE-MET-01). O Revisor verifica correspondência de string (sem web).

**(5) RULE-REG-001 (registro físico das 10+1 famílias) — INCIDE (gatilho `spec:SPEC-002 em redação` DISPARA com esta abertura).** Proposta de texto no §5.9 (NÃO editei RULES.md).

### 5.9 Proposta de texto para RULE-REG-001 — registro das 11 famílias em `governance/RULES.md` — [PROPOSTA, para Andraus homologar junto da definição]

> **Natureza:** mudança de **baseline de método** (não da Spec). Estas 11 famílias já são **FATO NORMATIVO com vigência imediata** (homologadas em EUA-E04..E14); falta apenas a **incorporação física** ao `RULES.md`, diferida por texto das próprias atas ao "piloto da SPEC-002". O gatilho disparou agora. **Não editei `RULES.md`** (RULE-HG-01/02 — só o Controlador registra após homologação de Andraus).
> **Método de registro exigido:** **transcrição literal (RCN-001/INV-08)** a partir das atas-fonte — o texto abaixo foi **extraído verbatim** das tabelas das atas `governance/EUA-E04..E14_*_PROPOSTA.md` (não parafraseado). O Controlador deve conferir contra as atas antes de registrar.

**Bloco proposto (novo cabeçalho de comentário + seções por família), a inserir em `RULES.md`:**

```
<!-- Acréscimo homologado por Andraus (DHR-REG-001, junto da abertura da SPEC-002): RULE-REG-001 — incorporação física
     das 11 famílias cognitivas já FATO NORMATIVO (EUA-E04..E14), diferida por texto das atas ao piloto da SPEC-002.
     Transcrição literal (RCN-001) das atas EUA-E04..E14. Não altera baseline anterior — INV-07. Consolida o
     atomic-spec v1.5. Resolve os quatro marcadores [DECISÃO NECESSÁRIA: RULE-REG-001] hoje em RULES.md
     (RULE-HG-03, RULE-HV-02, RULE-HV-03, RULE-ECC-02) e em RULE-EV-03. -->

## Regras de Herança/Delta (RULE-HD) — [EUA-E04, DHR-EUA-E04, 2026-09-20]
RULE-HD-01: Toda spec de componente e toda Engineering Card DEVE declarar o bloco Herança/Delta (§8.3) com INHERITS e ADDED preenchidos.
RULE-HD-02: Item em ADDED/MODIFIED NÃO DEVE contradizer item herdado em INHERITS (coerência vertical). Precedência em conflito: PC > PB/PE > regra local (alinha INV-01 e regime PAP).
RULE-HD-03: Nenhum item herdado PODE ser suprimido fora do campo REMOVED; item em REMOVED sem referência de homologação de Andraus = NÃO CONFORME Crítica.
RULE-HD-04: O bloco NÃO DEVE copiar o conteúdo herdado — apenas referenciá-lo por ID + VERSÃO baseline. Referência a versão superseded é achado (sensor de drift).

## Regras Epistêmicas (RULE-EPI) — [EUA-E05, DHR-EUA-E05, 2026-09-20]
RULE-EPI-01: Afirmação material NÃO DEVE subir de status epistêmico sem justificativa proporcional explícita (evidência/método). Transição silenciosa = achado.
RULE-EPI-02: Afirmação causal exige método compatível com causalidade; correlação/associação NÃO basta (alinha AP-02, RULE-004).
RULE-EPI-03: Conclusão NÃO DEVE exceder o escopo da evidência (scope overreach); generalização declara seu limite (alinha SES-001 §36).

## Regras Semânticas (RULE-SEM) — [EUA-E06, DHR-EUA-E06, 2026-09-20]
RULE-SEM-01: Quando um termo tem acepção concorrente por escola (registro §4) e o sentido é decisivo para o comportamento, a spec DEVE declarar explicitamente qual acepção usa (transparência semântica).
RULE-SEM-02: Não-colapsação semântica (conceito→fato, correlação→causa, interpretação→verdade, nome→entidade) segue RULE-EPI-01..03 (EUA-E05). Esta emenda NÃO cria regra paralela.
RULE-SEM-03: Transformação semântica (normalização/tradução) NÃO DEVE eliminar modalidade/nuance material ("pode" ≠ "será"); a forma original permanece recuperável (alinha PB-10, TRACE-06).
RULE-SEM-04: Termo já canônico no GLOSSARIO NÃO DEVE ser redefinido por spec; acepção de escola é adição contextual, não substituição (alinha PC-05/INV-10, RULE-HD-02).

## Regras Ontológicas (RULE-ONT) — [EUA-E07, DHR-EUA-E07, 2026-09-20]
RULE-ONT-01: A spec DEVE distinguir entidade observacional (diretamente medida/observada) de construção teórica (postulada para explicar — ex.: order block, liquidez, "pressão compradora"). Entidade latente/teórica NÃO DEVE ser promovida a real sem tratamento epistêmico (segue RULE-EPI; não cria regra paralela). Alinha INV-06/PC-03.
RULE-ONT-02: Nova entidade/categoria ontológica é resultado cognitivo válido, mas entra por governança (propõe → homologa): segue PO-05/PC-08. NÃO DEVE ser auto-adotada como baseline (INV-09).

## Regras de Inquérito (RULE-INQ) — [EUA-E08, DHR-EUA-E08, 2026-09-20]
RULE-INQ-01: Antes de investigar/especificar comportamento com incerteza material, a spec DEVE classificar o tipo de questão (factual/descritiva/explicativa/preditiva/diagnóstica/verificação/comparativa) e usar método compatível (§9/§14). Método escolhido antes da pergunta = achado.
RULE-INQ-02: Havendo hipóteses concorrentes (PCO-01), a investigação DEVE buscar evidência discriminante ("que observação diferencia H1 de H2?"), não apenas confirmatória. Estende PCO-02; não cria regra paralela.
RULE-INQ-03: Toda investigação material DEVE declarar critério de encerramento (suficiência proporcional ao risco — GES/D0–D9). Sem suficiência → estado INDETERMINADO (RULE-EPI), não conclusão forçada nem investigação infinita.

## Regras Causais (RULE-CAU) — [EUA-E09, DHR-EUA-E09, 2026-09-20]
RULE-CAU-01: Afirmação causal (A→B) é hipótese e DEVE declarar o mecanismo que a sustenta (como A produz B), além de condições e direção. Correlação/precedência/padrão histórico NÃO bastam (estende RULE-EPI-02; não cria regra paralela).
RULE-CAU-02: Relação causal material DEVE declarar o regime/condição de validade (a mesma relação pode mudar ou desaparecer entre regimes). Alinha SES-001 (regime) e GPR-001 §3.6 (inversões).
RULE-CAU-03: Explicação causal formulada após o resultado DEVE ser marcada como pós-hoc, sem o status de hipótese pré-testada. Teste: "poderia ter sido formulada antes do resultado?" (estende AP-10).

## Regras Contrafactuais (RULE-CTF) — [EUA-E10, DHR-EUA-E10, 2026-09-20]
RULE-CTF-01: Todo raciocínio contrafactual/backtest DEVE declarar o baseline (mundo de referência), alterar apenas a premissa indicada (intervenção mínima) e não usar o resultado conhecido como premissa (anti-hindsight). Estende RULE-CAU-03; não cria regra paralela.
RULE-CTF-02: Contrafactual é condicional: NÃO DEVE ser apresentado como fato nem convertido em previsão. Consequências DEVEM ser graduadas (necessária / plausível / possível / especulativa), coerente com TRACE-06 e RULE-EPI.
RULE-CTF-03: Contrafactual de invalidação ("que alteração mínima invalida esta leitura?") DEVE conectar-se ao invalidador declarado da hipótese (INV-02/Elliott-ICT), não a um invalidador ad hoc.

## Regras de Incerteza (RULE-UNC) — [EUA-E11, DHR-EUA-E11, 2026-09-20]
RULE-UNC-01: Ao declarar incerteza material, a spec DEVE localizá-la (onde: dado/modelo/causa/semântica/regime/estrutura/decisão) e tipificá-la, em vez de "há incerteza" genérico. Estende PB-10 (preservar → localizar).
RULE-UNC-02: Incerteza é localizada: uma incerteza local NÃO DEVE rebaixar partes bem estabelecidas do raciocínio (nem o inverso — certeza artificial local). Dependências entre incertezas declaradas quando materiais.
RULE-UNC-03: Incerteza NÃO DEVE ser convertida em probabilidade sem base: "não distingo A de B" ≠ "A e B igualmente prováveis" (anti-falsa-precisão; segue RULE-EPI). Quantificação pertence ao nó Probabilística / Conviction Engine.

## Regras Probabilísticas (RULE-PRB) — [EUA-E12, DHR-EUA-E12, 2026-09-20]
RULE-PRB-01: Afirmação probabilística material DEVE ser bem-formada: declarar evento, condição/contexto e horizonte. "X%" isolado (sem evento/condição/horizonte) é achado. Não se aplica ao Conviction Vector, cujo contrato é o CCM-001 (J-001 aberto).
RULE-PRB-02: Não quantificar sem base: quando faltar fundamento (incerteza estrutural/profunda, evento mal definido, modelo inadequado), usar ordenação qualitativa ou INDETERMINADO em vez de número fabricado. Estende RULE-UNC-03; anti-falsa-precisão (RULE-EPI).

## Regras Decisionais (RULE-DEC) — [EUA-E13, DHR-EUA-E13, 2026-09-21]
RULE-DEC-01: Toda saída decisional material DEVE declarar que produz recomendação/orientação decisional (TMP), não execução, e sob qual autoridade ela é emitida (o SOT recomenda; a execução e a decisão final permanecem na camada/autoridade competente — Andraus/humano). Reforça e referencia INV-05, P14 e a topologia Synthesis/B-001 — não os redefine. Confundir recomendação com autoridade, ou apresentar análise como ação automática, é achado.
RULE-DEC-02: Sob informação faltante ou preferência não disponível, o LLM DEVE poder produzir decisão condicional — se X → A / se ¬X → B / se X permanecer desconhecido → INDETERMINADO/HOLD — em vez de fabricar uma decisão única ou inventar a preferência ausente. Estende INDETERMINADO (EUA-E05) e RULE-UNC (EUA-E11) ao plano decisional.
RULE-DEC-03: Qualidade do processo decisional ≠ qualidade do resultado. Uma decisão bem fundamentada pode produzir resultado ruim e vice-versa; a avaliação retrospectiva NÃO DEVE julgar o processo apenas pelo resultado (anti-hindsight). Estende RULE-CAU-03/AP-10; crítico para avaliação de backtest e revisão de sinais.

## Regras de Metacognição (RULE-MET) — [EUA-E14, DHR-EUA-E14, 2026-09-21]
RULE-MET-01: Honestidade / não-fabricação metacognitiva. O sistema NÃO DEVE declarar validação que não realizou, ferramenta que não usou, causalidade que não demonstrou nem independência entre evidências que não verificou. Quando não puder determinar um atributo metacognitivo (ex.: se duas evidências são independentes), DEVE declarar a limitação em vez de afirmá-lo sem base. Estende RULE-SY-005, RULE-EPI e RULE-004.
RULE-MET-02: Abstenção produtiva (anti-censura cognitiva). INDETERMINADO/incerteza NÃO DEVE degenerar em "não é possível saber". Toda abstenção material DEVE localizar: o que é incerto · o que a incerteza afeta · sob qual condição a conclusão muda · qual informação a reduziria. Torna o INDETERMINADO (EUA-E05) informativo; estende RULE-UNC (EUA-E11). Anti-antipadrão MC-001 §89.
RULE-MET-03: Autonegação / revisibilidade legítima. Uma conclusão anterior do próprio sistema NÃO se torna irrevogável por ter sido produzida antes; DEVE poder ser revista ou abandonada ante nova evidência/regime/observação, sem que isso seja tratado como falha operacional. Estende RULE-007/PCO-01 e os gatilhos de reavaliação (RULE-CTF-03).
```

- **Efeito colateral saneador:** o registro resolve os quatro marcadores `[DECISÃO NECESSÁRIA: RULE-REG-001]` hoje presentes em `RULES.md` (fontes RULE-DEC-01, RULE-HD-02, RULE-HD-03, RULE-MET-01 citadas sem seção própria — em RULE-HG-03, RULE-HV-02, RULE-HV-03, RULE-ECC-02, RULE-EV-03). Achado de `check_doc_sync.py` (RULE-HG-02) sanado. [INFERÊNCIA]
- **Compatibilidade:** **Minor** (aditivo; INV-07 — nenhuma regra anterior alterada/removida). Consolida o **atomic-spec v1.5** (a nota "diferida ao piloto SPEC-002" das atas passa a "incorporada").

### 5.10 Re-apontamento de gatilhos RMR-001 (passo 11-bis / RULE-ECC-01)

- **Nenhum re-apontamento de slot necessário:** o slot SPEC-002 é **mantido** (não dividido/fundido/renumerado/descartado) — RULE-ECC-01 não exige re-apontamento.
- **Itens do RMR-001 e o efeito desta ABERTURA (não é homologação de Spec):**
  - **RULE-REG-001** (decisão aberta) — gatilho `spec:SPEC-002 em redação`: **DISPARA com esta abertura** → tratado no §5.9 (proposta de registro para Andraus). É o único item que a abertura ativa.
  - **BL-002** (`spec:SPEC-003 homologada` ∨ `decisao:J-001 resolvida`): **não dispara** (SPEC-002 ≠ SPEC-003; J-001 aberta).
  - **BL-003** (`spec:SPEC-004 em redação`): **não dispara**.
  - **BL-004** (`spec:SPEC-003 em redação`): **não dispara**.
  - **BL-012** (MC-COG-001; `spec:SPEC-002 homologada (consolidação cognitiva v1.5)`): **NÃO dispara na abertura** — dispara na **homologação** da SPEC-002. Registrado como **IMINENTE**: no gate de homologação da SPEC-002, o MC-COG-001 deve ser tratado (mapear COG-SPEC contra N8–N17; ACHADO R-05/COL-COG-01: usar estados CHM-001, proteger CC-02).
  - **BL-017** (`spec:SPEC-007/014/038 em redação`): **não dispara** (não inclui SPEC-002).
  - **BL-024** (CACHING SOT; pré-condição `evento:abertura da SPEC-002`): **já Absorvido** (SPEC-046) — a pré-condição de validação foi satisfeita antes desta abertura; nenhuma ação pendente.
  - Nenhum item fica `ATIVADO` sem encaminhamento por esta abertura (a abertura não é homologação de Spec; o passo 11-bis pleno ocorre na homologação da SPEC-002).

---

## 6. Perguntas que Andraus precisa decidir (homologação da definição — ROADMAP §23 passo 1-bis)

- **Q-A1 (escopo/fronteira/quantidade):** Aprova **SPEC-002 como 1 Spec CRITICAL não decomposta**, camada operacional sobre CEM-001, com o escopo §5.3 e os non-goals §5.4 (fusão → SPEC-003; storage → SPEC-004/006; estados do Blackboard → M-001)? **[DECISÃO NECESSÁRIA]**
- **Q-A2 (profundidade-alvo):** Confirma **D0–D8** (o slot §4 indicava D0–D7; proponho D8 por ser CRITICAL com tratamento adversarial de conflito/ausência/independência — alinhamento ao profile pinado AGENTS §4, declarado, não silencioso)? Ou mantém D0–D7? **[DECISÃO NECESSÁRIA]**
- **Q-A3 (RULE-PD-01/CC-12):** Confirma que a SPEC-002 **NÃO declara `PD-xx`** por ser camada operacional/domain-agnostic sobre CEM-001 (não escopo de especialidade de mercado) — mesmo padrão N/A de SPEC-020/021, deixando `PD-xx` para SPEC-010..014? **[DECISÃO NECESSÁRIA]**
- **Q-A4 (RULE-REG-001):** Homologa o **registro físico das 11 famílias** (§5.9, transcrição literal das atas EUA-E04..E14) em `RULES.md`, consolidando o **atomic-spec v1.5**, junto desta abertura (compatibilidade Minor; saneia os 4 marcadores pendentes)? **[DECISÃO NECESSÁRIA]**
- **Q-A5 (método vigente):** A SPEC-002 é redigida sob **atomic-spec v1.5** (se Q-A4 aprovada) ou v1.4 + emendas? **[DECISÃO NECESSÁRIA]**
- **Q-A6 (ECC-VAL-001):** Validade deste Dossiê (acesso 2026-09-28) antes da redação do Plan? (Precedente SPEC-020: 30 dias corridos OU início do Plan, o que ocorrer primeiro — só para esta Spec; ECC-VAL-001 permanece aberta como regra geral.) **[DECISÃO NECESSÁRIA]**
- **Q-A7 (M-001):** Confirma que o protocolo de publicação de Evidência no Blackboard **referencia M-001 como aberta** (não fecha estados do Blackboard para não-hipótese), a fechar em SPEC-004? **[DECISÃO NECESSÁRIA]**

---

## 6-bis. Registro de Homologação da Definição de Abertura (Andraus, 2026-09-28)

Todas as 7 perguntas RESOLVIDAS por Andraus. Parecer do Revisor: **CONFORME** (0 Crítico/Médio, 3 Menores não-bloqueantes; RULE-ECC-04 verificada verbatim nas 6 fontes; 3 das 11 famílias do §5.9 checadas contra as atas originais — MATCH).

- **Q-A1 — RESOLVIDA:** Aprovado. 1 Spec CRITICAL, não decomposta.
- **Q-A2 — RESOLVIDA:** D0–D8 confirmado.
- **Q-A3 — RESOLVIDA:** Confirmado N/A. `PD-xx` não incide (camada domain-agnostic).
- **Q-A4 — RESOLVIDA:** Homologado o registro físico das 11 famílias (§5.9) em `governance/RULES.md`.
- **Q-A5 — RESOLVIDA:** SPEC-002 redigida sob **atomic-spec v1.5**.
- **Q-A6 — RESOLVIDA:** Confirmado. 30 dias/início do Plan — Plan inicia hoje, dentro da validade.
- **Q-A7 — RESOLVIDA:** Confirmado. Protocolo referencia M-001 como aberta.

**Abertura da SPEC-002 HOMOLOGADA.** Próximo passo: Controlador registra as 11 famílias em `RULES.md` + bump `atomic-spec.md` → v1.5; Especificador redige `plan.md`/`checks.md`.

---

## 7. Autoverificação da abertura (RULE-ECC-02/04 — parte determinística)

```
[x] Web disponível em 2026-09-28 → abertura NÃO suspensa (RULE-ECC-02).
[x] Dossiê presente e completo (CRITICAL): questões+estratégia; fontes classificadas e [EXTERNO]; data de acesso; comparação adotar/adaptar/rejeitar/adiar; lacunas/conflitos; escopo/quantidade/número; re-apontamento avaliado.
[x] RULE-ECC-04 aplicada: 6 arquivos sources/SRC-01..06.txt (URL+data+trecho ≥100 chars); citações verbatim entre aspas no §2.1; método de captura honesto (RULE-MET-01) onde WebFetch falhou.
[x] Conteúdo web tratado como DADO; nenhuma importação automática; nada vira baseline (DHR-PROV-WEB-001 §2.1).
[x] CC-02/CONST-01: CEM-001 e CHM-001 NÃO redefinidos — camada operacional apenas.
[x] Nenhuma decisão aberta fechada (CONS-01): J-001, M-001, H-001, ECC-VAL-001, ECC-03-001 permanecem abertas; INDETERMINADO usado (GAP-2).
[x] 5 regras avaliadas explicitamente (§5.8): MECH-01 INCIDE; PD-01 N/A justificado; MM-01 INCIDE (alvo L3); ECC-04 INCIDE+aplicada; REG-001 INCIDE (proposta §5.9).
[x] Etiquetagem aplicada: [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO].
[x] Fronteiras SOT respeitadas: CC-01 (hierarquia — não tocada), INV-04 (Strength≠Convicção), INV-06 (Evidência≠Observação), INV-10 (CEM idioma), ENF-03 (LLM detector≠gate), 4Es.
[x] RULES.md NÃO editado (RULE-HG-01/02) — só proposta de texto para Andraus/Controlador.
[x] NÃO é o Plan — Plan adiado à homologação da definição (ROADMAP §23 passo 1-bis).
```

**Pronto para revisão (do Dossiê de abertura).** O Revisor audita presença/estrutura/classificação/etiquetagem/comparação/ausência de importação automática + **correspondência verbatim** das citações com `sources/` (RULE-ECC-04, sem web) — não a veracidade das páginas (atomic-spec §15). A homologação da definição (e do registro RULE-REG-001) é de Andraus, antes do Plan.

---

## Sources (fontes [EXTERNO] — acesso 2026-09-28)

- [W3C PROV — An Overview of the PROV Family of Documents](https://www.w3.org/TR/prov-overview/)
- [GRADE — Grading Quality of Evidence and Strength of Recommendations (PMC2735783)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2735783/)
- [ECon — On the Detection and Resolution of Evidence Conflicts (arXiv 2410.04068)](https://arxiv.org/html/2410.04068)
- [OpenLineage — open standard for data lineage](https://openlineage.io/)
- [Evidence of absence (Wikipedia)](https://en.wikipedia.org/wiki/Evidence_of_absence)
- [Research on the Fusion of Dependent Evidence Based on Rank Correlation Coefficient (PMC5676609)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5676609/)
- [ECon detection/resolution of evidence conflicts (arXiv)](https://arxiv.org/html/2410.04068)
- [When Absence Is Evidence: Completeness-Sensitive Negative Reasoning in LLMs (arXiv 2608.04591)](https://arxiv.org/pdf/2608.04591)
- [Data Lineage vs Data Provenance (OvalEdge)](https://www.ovaledge.com/blog/data-lineage-vs-data-provenance)
- [Resolving Conflicting Evidence in Automated Fact-Checking (IJCAI 2025)](https://www.ijcai.org/proceedings/2025/1073.pdf)
