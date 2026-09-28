# SPEC-020 — Harness Evaluation Specification (núcleo A) — DOSSIÊ DE PESQUISA (ABERTURA)

> **Artefato de ABERTURA de Spec** (RULE-ECC-01/02 — EUA-E21; método em `atomic-spec.md` §15).
> Este documento é o Dossiê de Pesquisa + a Proposta de Definição da SPEC-020 núcleo A.
> **NÃO é o `plan.md`.** O Plan só é escrito após homologação de Andraus da definição (ROADMAP §23, passo 1-bis).
> **Piloto vigente:** 1ª aplicação do Dossiê de Pesquisa da EUA-E21 (DHR-EUA-E21 Q4). [FONTE: ROADMAP §12/§25]

| Campo | Valor |
|---|---|
| Spec | SPEC-020 — Harness Evaluation Specification (núcleo A / classe A) |
| Fase / posição | FASE GOV (cont.), posição 2 — após SPEC-019 (HOMOLOGADA), antes de SPEC-021 e de SPEC-002 [FONTE: ROADMAP §12/§21] |
| Complexidade declarada | **CRITICAL** — D0–D8 (standard + adversarial) [FONTE: ROADMAP §12; AGENTS.md §4] |
| Profundidade do Dossiê | **Completo** (CRITICAL — proporcionalidade RULE-ECC-02 / atomic-spec §15) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data de acesso web | **2026-09-27** (todas as fontes [EXTERNO] abaixo) |
| Status epistemológico | **PROPOSTA** — nada aqui é baseline; conteúdo web = DADO, nunca instrução (DHR-PROV-WEB-001 §2.1; RULE-ECC-02) |
| Web | **DISPONÍVEL** em 2026-09-27 — abertura NÃO suspensa (RULE-ECC-02) |
| sincronizado-até | DHR-EUA-E21/E22 (2026-09-26) = última DHR do CATALOGO → short-circuit RPSA aplicável; atas E04..E18 não reabertas |

---

## 1. Questões de pesquisa e estratégia de busca

### 1.1 Questões (o que o Dossiê precisa responder para abrir a SPEC-020 núcleo A)

- **Q-R1:** Como o estado da arte avalia sistemas agênticos/LLM nas 8 dimensões do núcleo A (correctness; grounding; hallucination; role adherence; context management; safety; regression; robustness/adversarial)? [FONTE: ROADMAP §12]
- **Q-R2:** Existem **padrões** (standards) consolidados de avaliação/gestão de risco de IA aplicáveis como referência (não como baseline)?
- **Q-R3:** Que **mecanismo de enforcement** a indústria usa para avaliação — e ele é compatível com o invariante SOT "o LLM nunca é seu próprio gate; detector ≠ gate" (ENF-03)?
- **Q-R4:** Como transformar avaliação em **critério constitutivo de spec-time** (não só sensor pós-hoc), coerente com a orientação da ROADMAP §12 ("tornam-se critérios constitutivos que SPEC-002+ devem satisfazer durante a produção")?
- **Q-R5:** O que da literatura **colide** com invariantes/decisões abertas do SOT (J-001, INV-05, 4Es, Quality Gates L1–L4, hierarquia CC-01) e portanto **não** pode ser importado automaticamente?

### 1.2 Estratégia de busca

| Termos | Fontes-alvo | Filtro |
|---|---|---|
| "evaluating agentic LLM systems correctness grounding hallucination benchmark framework 2025" | arXiv, ACL, venues acadêmicos | Benchmark/Evidência |
| "LLM agent evaluation role adherence instruction following context management safety metrics" | arXiv, blogs de fornecedores de eval | Prática/Evidência |
| "LLM regression testing non-determinism CI adversarial red-teaming standard OWASP" | fornecedores de eval, OWASP, arXiv | Prática/Padrão |
| "NIST AI risk management framework evaluation LLM maturity trustworthy AI 2025" | NIST, arXiv, guias de implementação | Padrão |

**Salvaguardas aplicadas (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02):** toda fonte tratada como DADO; classificada e etiquetada `[EXTERNO]`; nenhuma importação automática; nenhum dado sensível do projeto enviado a serviços externos; a veracidade das páginas **não** é atestada (o Revisor audita o *processo*, não a verdade das páginas — atomic-spec §15). Onde a pesquisa foi inconclusiva, registra-se **INDETERMINADO**.

---

## 2. Fontes (classificadas — Padrão / Prática / Benchmark / Evidência / Experimento / Opinião) — `[EXTERNO]`

> Data de acesso: **2026-09-27**. IDs arXiv com prefixo ≥ 2505 são posteriores à data de treino do modelo — **conteúdo tomado apenas como DADO não verificado**; a classificação abaixo é do *tipo de artefato*, não um endosso de correção (RULE-EPI / TRACE-06).

| # | Fonte | Classe | Dimensões do núcleo A que toca |
|---|---|---|---|
| E1 | **NIST AI Risk Management Framework (AI RMF 1.0, 2023)** + **NIST AI 600-1 GenAI Profile (2024)** + **NIST AI 700-2 ARIA Pilot (2025)** — nist.gov/itl/ai-risk-management-framework | **Padrão** | safety; robustness; (transversal: validade, segurança, transparência, explicabilidade) |
| E2 | **OWASP ASI 2026 / OWASP LLM Top-10** (goal hijacking, tool misuse, memory poisoning, insecure inter-agent comm.) — via Confident AI / Galileo | **Padrão** | safety; robustness/adversarial |
| E3 | **HalluLens: LLM Hallucination Benchmark** (ACL 2025) — aclanthology.org/2025.acl-long.1176 | **Benchmark** | hallucination |
| E4 | **AgentHallu: Benchmarking Automated Hallucination Attribution of LLM-based Agents** (arXiv 2601.06818) | **Benchmark** | hallucination; grounding |
| E5 | **Evaluation and Benchmarking of LLM Agents: A Survey** (arXiv 2507.21504) | **Evidência** (survey) | todas as 8 |
| E6 | **Evaluating LLM Agent Adherence to Hierarchical Safety Principles** (arXiv 2506.02357) | **Experimento** | role adherence; safety |
| E7 | **GroundEval: A Deterministic Replacement for LLM-as-Judge in Stateful Agent Evaluation** (arXiv 2606.22737) | **Experimento** | correctness; grounding; (enforcement determinístico) |
| E8 | **Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents** (arXiv 2605.22608) | **Experimento** | correctness; context management |
| E9 | **CHARM: Cascading Hallucination in Agentic RAG** (arXiv 2606.04435) | **Experimento** | hallucination; grounding (classe B / RAG) |
| E10 | **Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems** (arXiv 2512.12791) | **Evidência** | correctness; role adherence |
| E11 | Práticas de fornecedores — **Braintrust** (red-team→regression suite), **MLflow** (red-teaming por release), **Promptfoo** (red-team open-source), **Arize / Confident AI / Snowflake** (métricas de agente: tool calling, task completion, trace-based) | **Prática** | regression; robustness; context management; correctness |
| E12 | **Learning-Based Automated Adversarial Red-Teaming for Robustness Evaluation of LLMs** (arXiv 2512.20677); **Redefining AI Red Teaming in the Agentic Era** (arXiv 2605.04019) | **Experimento** | robustness/adversarial |
| E13 | **Risk-based test framework for LLM features in regulated software** (arXiv 2601.17292) | **Evidência** | regression; safety (rigor proporcional ao risco) |

**Achado transversal relevante (E6, `[EXTERNO]`, Evidência):** avaliação de segurança revela um *"cost of compliance"* (restrições de segurança degradam desempenho de tarefa mesmo quando há solução conforme) e uma *"illusion of compliance"* (alta aderência frequentemente mascara incompetência de tarefa em vez de escolha principiada). Relevante para a dimensão **safety** e **role adherence** do núcleo A.

---

## 3. Comparação com a arquitetura SOT e os modelos canônicos (adotar / adaptar / rejeitar / adiar)

> Regra: nada entra como baseline; cada item confronta a arquitetura homologada. Cobertura interna existente é **preservada**; só se aprofunda o insuficiente (ROADMAP R1/§24).

| Dimensão (núcleo A) | Cobertura SOT já existente [FONTE] | Evidência externa | Decisão | Porquê |
|---|---|---|---|---|
| **Correctness** | EARS `VERIFICADO POR`; cenários D7; Quality Gates L1–L4 (atomic-spec §7); RULE-SDD-001 (spec = fonte de verdade) | E5, E7, E8, E10 | **ADAPTAR** (conceito de "trace completo como alvo de avaliação" — E5/E8) + **ADOTAR conceito** de verificação determinística (E7) | Alinha com P13 (reconstrução) e D9; reforça `VERIFICADO POR` mensurável |
| **Grounding** | RULE-EPI (hipótese≠fato); CEM-001 (provenance); cadeia Fonte→Dado→Evidência→Hipótese; RULE-CAU (mecanismo obrigatório) | E4, E7, E9 | **ADAPTAR** como critério verificável de "toda afirmação ancorada em Evidência/fonte" | Já é FATO NORMATIVO interno; a literatura fornece **método de medição**, não conteúdo novo |
| **Hallucination** | SPEC-044 (slot); RULE-MET-01 (não-fabricação); INV-EPI; TRACE-06; §7-bis Bloco C | E3, E4, E9 | **ADAPTAR** (taxonomia de tipos de alucinação como método de detecção); **DETECTOR, não gate** | Detector ≠ gate (ENF-03); SPEC-044 detalha o slot downstream |
| **Role adherence** | CC-01 (hierarquia Elliott→ICT); RULE-EW/SM/ICT (escopo por agente); RULE-BB-002 (workspace); RULE-ICT-007 (ICT não cria hipótese) | E6, E10 | **ADAPTAR** (probing de aderência hierárquica sob conflito — E6) | E6 modela exatamente "princípio de topo sobrepõe instrução de tarefa" = hierarquia PC-01/CC-01 do SOT |
| **Context management** | SPEC-043 (slot); RULE-CEE-003 (InferenceContextEnvelope); Blackboard (memória de trabalho); Event Bus | E5, E8, E11 | **ADAPTAR** (avaliação sobre a *trajetória* de contexto) | SPEC-043 detalha o slot; núcleo A só fixa o *critério* de integridade de contexto |
| **Safety** | 5+5 Salvaguardas Constitucionais (CEE-001 §10/§11); SPEC-042 (guardrails); fail-closed E3; INV-04 | E1, E2, E6 | **ADAPTAR** OWASP ASI/NIST como **catálogo de referência** de ameaças, **SUBORDINADO** às Salvaguardas; **atenção ao "illusion of compliance" (E6)** | As Salvaguardas SOT são invioláveis e prevalecem; catálogos externos enriquecem o método adversarial |
| **Regression** | `npm test`/`npm run lint` (F.3 Feedback); harness-eval Track A; CI/pre-commit | E11, E13 | **ADAPTAR** (converter achado adversarial → caso de regressão versionado em CI — Braintrust/MLflow) | Casa com o pipeline D8→`checks.md`→CI; INV-07 (nada deletado) |
| **Robustness / adversarial (como método)** | D8 (casos de negação); §7-bis (especificador) / Passo 5-bis (revisor); SPEC-022 (slot — teste adversarial integrado) | E2, E11, E12 | **ADAPTAR** como **método** de avaliação; **fronteira**: SPEC-020 define *como avaliar robustez*; SPEC-022 produz *os casos* | Evita duplicar SPEC-022; núcleo A fixa a disciplina de método |

### 3.1 Mecanismo de enforcement (Q-R3) — decisão crítica

- **ADOTAR (como princípio já SOT):** avaliação com **gate determinístico**; **LLM-as-Judge apenas como detector**, nunca como gate (ENF-03; atomic-spec §5). A fonte **E7 (GroundEval)** — "substituto determinístico para LLM-as-Judge" — é **convergente** com o invariante SOT e reforça a posição, mas entra como referência, não como baseline. [INFERÊNCIA]
- **REJEITAR (importação automática):** usar LLM-as-Judge como *portão* de aprovação (prática comum em E11) — colide com ENF-03. Admitido só como sinal/detector, com gate determinístico por cima.

### 3.2 Critério constitutivo de spec-time (Q-R4)

- **ADAPTAR:** o conceito industrial de "shift-left / evaluation-driven development" (E5/E11) é **convergente** com a orientação da ROADMAP §12 (as 8 dimensões viram critérios que SPEC-002+ satisfazem *durante* a produção). No SOT isto se materializa **acoplando as dimensões classe A ao Constitution Check / `checks.md`** como itens verificáveis de spec-time — **não** como tooling de runtime (fase spec-first; ROADMAP §22). [INFERÊNCIA — sujeito a homologação]

### 3.3 Modelos canônicos — fronteiras (CC-02)

- Nenhuma métrica ADOTADA redefine CEM/CHM (CC-02). **CCM-001 permanece pendente (SPEC-003)** — nenhum limiar numérico ligado à convicção é fixado aqui (J-001 aberto). Grounding/correctness usam CEM-001 como idioma da Evidência (INV-10), sem alterá-lo.

---

## 4. Lacunas, conflitos e INDETERMINADOS (NÃO fecham decisão aberta — CONS-01)

- **CONFLITO-1 — LLM-as-Judge vs ENF-03.** Prática externa dominante (E11) usa LLM como juiz/gate; o SOT proíbe (ENF-03). **Resolução na Spec:** LLM = detector; gate = determinístico. Não é decisão aberta nova — já normado por ENF-03. [FONTE: atomic-spec §5/§10]
- **CONFLITO-2 — escadas de maturidade externas.** NIST (janelas 8–14 semanas / 12–18 meses) e ladders de fornecedores **colidem** com Quality Gates L1–L4 (atomic-spec §7), harness-score e maturidade GPR L0–L5 — **mesmo padrão de colisão** já anotado para os Master Contracts (K-MAN, CATALOGO §4). **Rejeitar os rótulos**; maturidade é da **SPEC-021**, não do núcleo A. [FONTE: ROADMAP §12; CATALOGO §4]
- **CONFLITO-3 — "task completion" como métrica primária.** Métricas de agente centradas em conclusão de tarefa (E11) não se aplicam ao SOT como primárias: o SOT **não executa** (INV-05) e prioriza **Conformidade > Eficácia** (4Es, AGENTS.md §6). Adaptar para "qualidade de análise/decisão", não "execução bem-sucedida". [FONTE: INV-05; 4Es]
- **GAP-1 — "illusion of compliance" (E6).** Como medir que alta aderência não mascara incompetência é **problema aberto na literatura**; para o SOT isto toca a dimensão safety/role adherence. **INDETERMINADO** — registrar como risco a tratar no método adversarial (D8), sem inventar métrica. [EXTERNO/INFERÊNCIA]
- **GAP-2 — limiares numéricos.** Qualquer *threshold* numérico de aprovação ligado a convicção/score depende de **J-001** (fórmula/pesos/limiares definitivos — aberto). SPEC-020 define **dimensões e métodos qualitativos**; **não** fixa limiares dependentes de J-001. **INDETERMINADO até J-001/CCM-001 (SPEC-003).** [FONTE: J-001; atomic-spec §12]
- **GAP-3 — dimensões classe B.** RAG faithfulness / tool correctness / decision traceability **permanecem diferidas** (SPEC-007/038/014; BL-017). CHARM (E9) e métricas de tool-calling (E11) confirmam a maturidade externa dessas dimensões, mas **não** as antecipa no SOT (CONS-01). [FONTE: ROADMAP §12; RMR-001 BL-017]

Nenhuma decisão aberta é fechada por esta pesquisa (RULE-ECC-02 / CONS-01).

---

## 5. Proposta de Definição da SPEC-020 núcleo A (para homologação de Andraus)

### 5.1 Número, quantidade, decomposição

- **Número:** **SPEC-020** (slot mantido; número monotônico, não reutilizado — RULE-ECC-01). [PROPOSTA]
- **Quantidade:** **1 (uma) Spec** — núcleo A **não decomposto**. [PROPOSTA]
  - *Porquê:* as 8 dimensões da classe A formam um **conjunto coeso de critérios constitutivos** operando sobre o mesmo alvo (o Harness de Especificação); decompor fragmentaria um único harness de avaliação e multiplicaria fronteiras sem ganho de atomicidade (ROADMAP §24 — não maximizar quantidade de documentos). SPEC-021 (maturidade) permanece **slot separado**; classe B permanece **diferida**.

### 5.2 Missão (comportamental, sem implementação) — [PROPOSTA]

Especificar **como o SOT Harness é avaliado** na dimensão constitutiva (classe A): definir, para cada uma das 8 dimensões — correctness, grounding, hallucination, role adherence, context management, safety, regression, robustness/adversarial (como método) — **o critério verificável de spec-time** que toda Spec de componente (SPEC-002+) DEVE satisfazer durante a produção, com **gate determinístico** e o LLM apenas como detector (ENF-03).

### 5.3 Escopo (dentro) — [PROPOSTA]

1. Definição verificável das **8 dimensões classe A** como critérios constitutivos (EARS + BASpec).
2. **Acoplamento ao Constitution Check / `checks.md`** — como cada dimensão vira item de gate de spec-time para SPEC-002+ (mecanismo de "critério constitutivo", não sensor pós-hoc). [sujeito a Q-A4 abaixo]
3. **Método de avaliação** por dimensão: detector vs gate; determinístico vs semântico (ENF-03); trajetória/trace como alvo (adaptado de E5/E8).
4. **Método adversarial/robustez** (como avaliar), articulado com D8 e §7-bis/Passo 5-bis, **sem duplicar** SPEC-022.
5. **Regressão**: disciplina de converter achado adversarial em caso versionado (INV-07) — articulada com F.3/CI, sem escrever código (spec-first).
6. **Incorporação de SPEC-020-PRINC-001** (ver 5.6).
7. Enforcement Contracts dos atos de avaliação com efeito de gate (E2/E3 conforme criticidade).

### 5.4 Fora do escopo (Non-goals) — [PROPOSTA]

- Modelo de maturidade L0–L4 por spec → **SPEC-021**.
- Dimensões **classe B** (RAG faithfulness / tool correctness / decision traceability) → **SPEC-007/038/014** (BL-017; CONS-01).
- Limiares numéricos dependentes de convicção → **J-001 / CCM-001 (SPEC-003)**.
- Avaliação cognitiva de **runtime** e tooling de execução → fase de implementação (ROADMAP §22); MC-COG/GOV diferidos.
- Redefinir CEM/CHM/CCM/CDM/CNM (CC-02) ou a hierarquia (CC-01).
- Rótulos/ladders externos (NIST janelas, OWASP como norma, LLM-as-Judge-gate) — rejeitados como baseline.

### 5.5 Capacidades §26 cobertas

- Cobre integralmente a capacidade **"SPEC-020 — Harness Evaluation Specification"** na dimensão **classe A** (ROADMAP §26). A dimensão classe B fica declaradamente **pendente** (não é achado de gate: está diferida por decisão homologada EUA-E17 + BL-017). [FONTE: ROADMAP §12/§26]

### 5.6 Incorporação de SPEC-020-PRINC-001 (decisão aberta incidente)

- A SPEC-020 núcleo A **DEVE** incorporar a **consistência principiológica do GPR-001 §15** como **critério constitutivo verificável**, operacionalizando o enforcement de precedência/conflito de princípios (GPR-001 §3.2/§6), hoje **declarativo (L0–L1)**. [FONTE: ROADMAP §12; MEMORY: camada-principiologica]
- **[DECISÃO NECESSÁRIA — SPEC-020-PRINC-001]:** permanece **aberta** — sua efetivação ocorre **na homologação** da SPEC-020 (não fechada aqui, CONS-01). Ver questão Q-A2.

### 5.7 Herança prevista (a declarar no Plan — CC-08 / RULE-HV) — [PROPOSTA]

- **INHERITS:** atomic-spec v1.4 (BASpec, D0–D8, Enforcement E0–E3, F.1–F.4, EARS, TRACE-06); **SPEC-019 v1.0 baseline** (RULE-HG-06 Constitution Check como gate; governança de emenda); GPR-001 §15 (checklist principiológico); ENF-01..08 (com ênfase em ENF-03); Quality Gates L1–L4; INV-05/07/09; 4Es (CEE-001 §12). O eixo vertical (RULE-HV-01..04) aplica-se se a SPEC-020 for tratada como filha de SPEC-019 na FASE GOV — **a confirmar no Plan**.
- Método da FASE GOV = **atomic-spec v1.4** (v1.5 não homologada) [FONTE: DHR-EUA-E17 §3].

### 5.8 Re-apontamento de gatilhos RMR-001

- **Nenhum re-apontamento necessário:** o slot SPEC-020 é **mantido** (não dividido/fundido/renumerado/descartado) — RULE-ECC-01 não exige re-apontamento. [FONTE: RMR-001 §3]
- **Passo 11-bis (heads-up para o gate da abertura):**
  - **BL-021** (adaptar ferramental à EUA-E21) — gatilho `spec:SPEC-020 em redação`: **dispara quando o Plan começar a ser redigido** (a abertura ainda não é redação do Plan). A tratar no gate de início do Plan; não é ação desta abertura.
  - **BL-020** (acesso web só-leitura do Revisor) — gatilho `spec:SPEC-020 homologada`: **não disparado** (só na homologação). Registrado.
  - **BL-017** (classe B) — gatilho `spec:SPEC-007/014/038 em redação`: **NÃO inclui SPEC-020** → não dispara agora; permanece `Proposto`. Sua promoção `Proposto→Em espera` é decisão de Andraus (RMR-001 §5), não desta abertura.
  - **BL-008** segue `ATIVADO` (auditoria retroativa da SPEC-001) — independente desta abertura.

---

## 6. Perguntas que Andraus precisa decidir (homologação da definição)

> **STATUS (2026-09-27): TODAS RESOLVIDAS por HOMOLOGAÇÃO de Andraus.** Ver §8 (Registro de Homologação da Abertura). O texto original das perguntas é **preservado** (INV-07); as decisões estão anotadas inline e detalhadas no §8. Parecer do Revisor sobre este Dossiê: **CONFORME**, 1 achado Menor **ACH-001** (não bloqueante), carregado ao Plan/Revisor.

- **Q-A1:** Aprova o escopo/fronteira/quantidade — **SPEC-020 núcleo A como 1 Spec CRITICAL não decomposta** (§5.1–5.4)? → **RESOLVIDA (2026-09-27): APROVADO.** [FATO NORMATIVO — §8]
- **Q-A2 (SPEC-020-PRINC-001):** a consistência principiológica (GPR-001 §15) entra como **9ª lente constitutiva própria** ("principle consistency") ou **integrada** às lentes role adherence + correctness? (A decisão fecha SPEC-020-PRINC-001 na homologação.) → **RESOLVIDA (2026-09-27): 9ª lente constitutiva PRÓPRIA** (não integrada, para evitar diluição e manter rastreabilidade). SPEC-020-PRINC-001 **efetiva-se na homologação da SPEC-020** (não fechada nesta abertura — CONS-01). [FATO NORMATIVO — §8]
- **Q-A3 (enforcement — Q-R3/Q-R4):** confirma que o **mecanismo constitutivo** se materializa acoplando as 8 dimensões ao **Constitution Check / `checks.md`** como gate de spec-time, com **gate determinístico + LLM só detector** (ENF-03), sem tooling de runtime nesta fase? → **RESOLVIDA (2026-09-27): CONFIRMADO.** Gate determinístico; LLM só detector (ENF-03); sem tooling de runtime (SPEC-045-RUNTIME-001 permanece decisão aberta separada, não antecipada). [FATO NORMATIVO — §8]
- **Q-A4 (limiares/J-001):** confirma que a SPEC-020 define dimensões e métodos **qualitativos**, **adiando** qualquer limiar numérico dependente de convicção a **J-001/CCM-001 (SPEC-003)** — mantendo GAP-2 aberto (CONS-01)? → **RESOLVIDA (2026-09-27): CONFIRMADO.** Spec qualitativa; limiares numéricos ligados a convicção adiados a J-001/CCM-001 (aberta). [FATO NORMATIVO — §8]
- **Q-A5 (classe B):** confirma que classe B permanece **diferida** (BL-017) e que **nenhuma** promoção de BL-017 é requerida nesta abertura? → **RESOLVIDA (2026-09-27): CONFIRMADO.** Classe B (SPEC-007/038/014) permanece DIFERIDA (BL-017), sem promoção nesta Spec. [FATO NORMATIVO — §8]
- **Q-A6 (ECC-VAL-001):** como piloto do Dossiê, há **prazo de validade** deste Dossiê (data de acesso 2026-09-27) antes da redação do Plan? (Decisão aberta ECC-VAL-001.) → **RESOLVIDA (2026-09-27): SIM.** Validade = **30 dias corridos** a partir da data de acesso (2026-09-27) **OU** até o início da redação do Plan, o que ocorrer primeiro. Como o Plan começa no mesmo dia, o Dossiê está **dentro da validade** e não precisa reconfirmação. **Escopo da regra: apenas esta Spec** — a regra geral para as próximas Specs deve ser proposta novamente/referenciada quando aplicável (ECC-VAL-001 permanece aberta como regra geral). [FATO NORMATIVO para esta Spec — §8]

---

## 8. Registro de Homologação da Abertura — [FATO NORMATIVO]

| Campo | Valor |
|---|---|
| Objeto | Definição de abertura da SPEC-020 núcleo A (este Dossiê §5) |
| Autoridade | **Andraus** (única autoridade de homologação) |
| Data | **2026-09-27** |
| Parecer do Revisor sobre o Dossiê | **CONFORME** — 1 achado Menor **ACH-001** (não bloqueante) |
| Decisões homologadas | Q-A1 APROVADO · Q-A2 APROVADO (9ª lente própria) · Q-A3 APROVADO · Q-A4 APROVADO · Q-A5 APROVADO · Q-A6 APROVADO (ECC-VAL-001: 30 dias / início do Plan — só esta Spec) |
| Efeito | Autoriza a redação do `plan.md` (ROADMAP §23 passo 1-bis cumprido) |
| Decisões que permanecem ABERTAS (CONS-01) | J-001; SPEC-020-PRINC-001 (efetiva-se na homologação da própria SPEC-020, não desta abertura); classe B (BL-017); ECC-VAL-001 como **regra geral** (resolvida só para esta Spec); SPEC-045-RUNTIME-001 |
| Preservação de histórico | INV-07 — nenhuma pergunta apagada; anotação aditiva |

> Este registro documenta a homologação da **definição de abertura**. NÃO é a homologação da SPEC-020 (que ocorrerá após Plan → Revisor → Andraus). A efetivação de SPEC-020-PRINC-001 e o fechamento de qualquer decisão incidente ocorrem **na homologação da SPEC-020**, não aqui (CONS-01).

---

## 7. Autoverificação da abertura (RULE-ECC-02 — parte determinística)

```
[x] Web disponível em 2026-09-27 → abertura NÃO suspensa (RULE-ECC-02).
[x] Dossiê presente e completo (CRITICAL): questões+estratégia; fontes classificadas e [EXTERNO]; data de acesso; comparação adotar/adaptar/rejeitar/adiar; lacunas/conflitos; escopo/quantidade/número; re-apontamento avaliado.
[x] Conteúdo web tratado como DADO; nenhuma importação automática; nada vira baseline (DHR-PROV-WEB-001 §2.1).
[x] Nenhuma decisão aberta fechada (CONS-01): J-001, SPEC-020-PRINC-001, classe B, ECC-VAL-001 permanecem abertas; INDETERMINADO usado (GAP-1/GAP-2).
[x] Etiquetagem aplicada: [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO].
[x] Fronteiras SOT respeitadas: CC-01 (hierarquia), CC-02 (canônicos), INV-05 (não executa), ENF-03 (LLM≠gate), 4Es, Quality Gates L1–L4.
[x] Passo 11-bis avaliado: BL-021/BL-020 registrados (não disparam na abertura); BL-017 não incidente; BL-008 independente.
[x] NÃO é o Plan — Plan adiado à homologação da definição (ROADMAP §23 passo 1-bis).
```

**Pronto para revisão (do Dossiê de abertura).** O Revisor audita presença/estrutura/classificação/etiquetagem/comparação/ausência de importação automática — não a veracidade das páginas (atomic-spec §15). A homologação da definição é de Andraus, antes do Plan.

---

## Sources (fontes [EXTERNO] — acesso 2026-09-27)

- [AI Risk Management Framework — NIST](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI RMF Implementation Guide (NeuralTrust)](https://neuraltrust.ai/blog/nist-ai-rmf-implementation-guide)
- [HalluLens: LLM Hallucination Benchmark (ACL 2025)](https://aclanthology.org/2025.acl-long.1176.pdf)
- [AgentHallu (arXiv 2601.06818)](https://arxiv.org/pdf/2601.06818)
- [Evaluation and Benchmarking of LLM Agents: A Survey (arXiv 2507.21504)](https://arxiv.org/pdf/2507.21504)
- [Evaluating LLM Agent Adherence to Hierarchical Safety Principles (arXiv 2506.02357)](https://arxiv.org/html/2506.02357)
- [GroundEval (arXiv 2606.22737)](https://arxiv.org/pdf/2606.22737)
- [Agentic CLEAR (arXiv 2605.22608)](https://arxiv.org/pdf/2605.22608)
- [CHARM: Cascading Hallucination in Agentic RAG (arXiv 2606.04435)](https://arxiv.org/pdf/2606.04435)
- [Beyond Task Completion (arXiv 2512.12791)](https://arxiv.org/pdf/2512.12791)
- [LLM red teaming → regression suite (Braintrust)](https://www.braintrust.dev/articles/llm-red-teaming-regression-suite)
- [Red-teaming LLM on every release (MLflow)](https://mlflow.org/articles/red-teaming-llm)
- [LLM red teaming guide (Promptfoo)](https://www.promptfoo.dev/docs/red-team/)
- [8 Red Teaming Strategies for LLMs and Agents (Galileo)](https://galileo.ai/blog/llm-red-teaming-strategies)
- [LLM Agent Evaluation Metrics (Confident AI)](https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide)
- [LLM evaluation methods, metrics, RAG & agent evals (Arize)](https://arize.com/resources/llm-evaluation/)
- [AI Agent Evaluation: Metrics and Methods (Snowflake)](https://www.snowflake.com/en/artificial-intelligence/agents/agent-evaluation/)
- [Learning-Based Automated Adversarial Red-Teaming (arXiv 2512.20677)](https://arxiv.org/pdf/2512.20677)
- [Redefining AI Red Teaming in the Agentic Era (arXiv 2605.04019)](https://arxiv.org/pdf/2605.04019)
- [Risk-based test framework for LLM features in regulated software (arXiv 2601.17292)](https://arxiv.org/pdf/2601.17292)
