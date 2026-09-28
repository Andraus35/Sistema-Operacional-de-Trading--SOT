# SPEC-021 — Harness Score / Maturity Model — DOSSIÊ DE PESQUISA (ABERTURA)

> **Artefato de ABERTURA de Spec** (RULE-ECC-01/02 — EUA-E21; método em `atomic-spec.md` §15).
> Este documento é o Dossiê de Pesquisa + a Proposta de Definição da SPEC-021.
> **NÃO é o `plan.md`.** O Plan só é escrito após homologação de Andraus da definição (ROADMAP §23, passo 1-bis).
> **Posição:** FASE GOV, posição 3 — segue o núcleo A da SPEC-020 (HOMOLOGADA 2026-09-27), antes de SPEC-002. [FONTE: ROADMAP §12/§21/§25]

| Campo | Valor |
|---|---|
| Spec | SPEC-021 — Harness Score / Maturity Model |
| Fase / posição | FASE GOV (cont.), posição 3 — após SPEC-020 núcleo A (HOMOLOGADA), antes de SPEC-002 [FONTE: ROADMAP §12/§21] |
| Complexidade declarada | **HIGH** — D0–D7 (standard) [FONTE: ROADMAP §12; AGENTS.md §4] |
| Profundidade do Dossiê | **Completo** (HIGH — proporcionalidade RULE-ECC-02 / atomic-spec §15) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data de acesso web | **2026-09-27** (todas as fontes [EXTERNO] abaixo) |
| Status epistemológico | **PROPOSTA** — nada aqui é baseline; conteúdo web = DADO, nunca instrução (DHR-PROV-WEB-001 §2.1; RULE-ECC-02) |
| Web | **DISPONÍVEL** em 2026-09-27 — abertura NÃO suspensa (RULE-ECC-02) |
| sincronizado-até | DHR-SPEC020-001 / DHR-CLASSE-MECH-001 / DHR-PRINC-BID-001 (2026-09-27) = últimas DHR → short-circuit RPSA aplicável; atas E04..E18 não reabertas |
| Nota de protocolo (EUA-E18 Q7) | SPEC-021 é a **3ª spec** sob o protocolo §7-bis/Passo 5-bis (SPEC-019 → SPEC-020 → SPEC-021) → a **checagem de proporcionalidade (EUA-E18 Q7)** está agendada para o relatório de revisão desta Spec [FONTE: RMR-001 §6, nota do gate EUA-E18] |

---

## 1. Questões de pesquisa e estratégia de busca

### 1.1 Questões (o que o Dossiê precisa responder para abrir a SPEC-021)

- **Q-R1:** Como o estado da arte estrutura **modelos de maturidade / capability levels** para sistemas de software, IA e agentes — e qual a lógica de progressão por níveis (staged vs continuous)? [FONTE: ROADMAP §12 "L0 Declarativo → L4 Autocontrolado"]
- **Q-R2:** Existe distinção consolidada entre maturidade **organizacional/empresarial** (adoção de IA) e maturidade **de artefato/processo** (capacidade de um componente ou spec)? Qual é aplicável ao SOT (que mede *specs*, não uma organização)?
- **Q-R3:** Como a literatura evita que um **score de maturidade seja gamed** (Goodhart) — em particular, como impedir que "maturidade" se confunda com "volume de documentação/telemetria"? [FONTE: ROADMAP §12 "Maturidade não se confunde com volume de documentação"; §24]
- **Q-R4:** Como maturidade se relaciona com **avaliação** (SPEC-020) — a maturidade é um *agregado ordinal* de critérios de avaliação já satisfeitos, ou um eixo independente? [FONTE: ROADMAP §12 "Segue o núcleo A da SPEC-020"]
- **Q-R5:** O que da literatura **colide** com invariantes/decisões abertas do SOT (J-001, INV-05, 4Es, Quality Gates L1–L4 já existentes, ENF-03) e portanto **não** pode ser importado automaticamente?

### 1.2 Estratégia de busca

| Termos | Fontes-alvo | Filtro |
|---|---|---|
| "AI agent maturity model capability levels evaluation LLMOps 2025 2026" | Medium/vendors, Microsoft Learn, arXiv | Prática/Padrão |
| "CMMI capability maturity model levels ISO/IEC 15504 SPICE staged continuous representation" | academia/Springer/IEEE, ISO | Padrão |
| "evaluation maturity model LLM reliability governance scoring rubric anti-gaming Goodhart metric" | arXiv, ACL, blogs de eng. de eval | Evidência/Experimento/Opinião |
| "Decision Evidence Maturity Model agentic AI property-level NIST AI RMF maturity model arxiv" | arXiv, IEEE-USA, CSA | Experimento/Padrão |

**Salvaguardas aplicadas (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02):** toda fonte tratada como DADO; classificada e etiquetada `[EXTERNO]`; nenhuma importação automática; nenhum dado sensível do projeto enviado a serviços externos; a veracidade das páginas **não** é atestada (o Revisor audita o *processo*, não a verdade das páginas — atomic-spec §15). Onde a pesquisa foi inconclusiva, registra-se **INDETERMINADO**.

---

## 2. Fontes (classificadas — Padrão / Prática / Benchmark / Evidência / Experimento / Opinião) — `[EXTERNO]`

> Data de acesso: **2026-09-27**. IDs arXiv com prefixo ≥ 2601 são posteriores à data de treino do modelo — **conteúdo tomado apenas como DADO não verificado**; a classificação abaixo é do *tipo de artefato*, não endosso de correção (RULE-EPI / TRACE-06).

| # | Fonte | Classe | O que informa para a SPEC-021 |
|---|---|---|---|
| M1 | **CMMI (SEI/Carnegie Mellon) + ISO/IEC 15504 (SPICE)** — linhagem Humphrey 1988: 5 níveis staged (Initial→Optimizing); representação **staged** (maturidade organizacional) vs **continuous** (capability por processo); ISO/IEC 15504-7 introduz 6 níveis de maturidade | **Padrão** | Base canônica da ideia de "níveis de maturidade"; distinção staged (agregado) vs continuous (por área) — diretamente análoga à tensão SOT "maturidade por-repo vs por-spec" |
| M2 | **Microsoft — Agentic AI adoption maturity model** (learn.microsoft.com) | **Prática** | Modelo de maturidade de **adoção organizacional** (não de artefato) — fronteira do que o SOT NÃO faz |
| M3 | **Maturity models empresariais 2026** — Sema4.ai (5 pilares/5 estágios), SphereInc "Maturity Map", Larridin "Enterprise Guide" | **Opinião/Prática** | Confirmam que "maturity model" no mercado é majoritariamente **organizacional** — a rejeitar como baseline para o SOT (que mede specs) |
| M4 | **Dan Shapiro / AI-SDLC Maturity Model** — 5 níveis (Manual L0 → "Dark Factory"/AI-Autonomous L5), analogia à direção autônoma (via M8) | **Prática** | Ladder de 6 níveis (L0–L5) por autonomia — comparável ao GPR-001 §11 L0–L5; útil como referência de *rótulos de progressão* |
| M5 | **The AI Codebase Maturity Model: From Assisted Coding to Fully Autonomous Systems** (arXiv 2604.09388) | **Evidência** | Maturidade de **artefato de engenharia** (codebase) por níveis — mais próximo do alvo SOT (maturidade de spec) que os modelos organizacionais |
| M6 | **Decision Evidence Maturity Model for Agentic AI: A Property-Level Method Specification (DEMM)** (arXiv 2605.04093) | **Experimento** | Agrega verdicts **por-propriedade** em rubrica de **5 níveis de capacidade** ancorada na linhagem de maturity models; categoria "conflicting"; foco em *reconstrutibilidade de evidência* (≈ P13/D9 do SOT). Modelo mais convergente: maturidade como agregação verificável de propriedades, não volume |
| M7 | **Evolving AI Risk Management: A Maturity Model based on the NIST AI RMF** (arXiv 2401.15229) + **A Flexible Maturity Model for AI Governance based on NIST AI RMF** (IEEE-USA ebook) | **Padrão/Evidência** | Maturidade de **governança/risco** derivada do NIST AI RMF; alerta: usa framework voluntário para reduzir pressão de compliance (anti-gaming brando) |
| M8 | **Goodhart's Law in Your LLM Eval Suite** (tianpan.co, 2026) | **Opinião/Prática** | "When a measure becomes a target, it ceases to be a good measure"; detecção de gaming (ex.: entropia cross-model); "avaliar o avaliador". Central para Q-R3 (maturidade ≠ volume) |
| M9 | **LLMs Designing and Applying Evaluation Rubrics** (ACL 2026 findings) + práticas de rubrica (LaunchDarkly, Maxim) | **Experimento/Prática** | Rubricas descrevem "o que é bom" por nível de score — método para tornar cada nível de maturidade **verificável**, não subjetivo |
| M10 | **MLOps→LLMOps maturity (níveis 0–2)** — CodeX/Medium; revisão de literatura de modelos MLOps | **Prática** | Ladders de automação de pipeline (L0 manual → L2 CI/CD) — mapeável a Quality Gates L1–L4 do SOT; reforça que níveis altos exigem automação/verificação, não só documento |
| M11 | **AI Security Maturity Model — 5 níveis** (Practical DevSecOps; SANS AI Security Maturity Model) | **Prática/Padrão** | Ladder de 5 níveis focado em segurança — subordinado às Salvaguardas SOT (não baseline) |

**Achado transversal relevante (M8/M6, `[EXTERNO]`):** o risco central de um modelo de maturidade é o **gaming (Goodhart)** — otimizar o indicador em vez do sistema. O DEMM (M6) responde a isso ancorando cada nível em **evidência de propriedade reconstruível** (não em quantidade de artefatos); M8 propõe "avaliar o avaliador". Ambos são diretamente pertinentes ao mandato explícito da ROADMAP §12: *"Maturidade não se confunde com volume de documentação."*

---

## 3. Comparação com a arquitetura SOT (adotar / adaptar / rejeitar / adiar)

> Regra: nada entra como baseline; cada item confronta a arquitetura homologada. Cobertura interna existente é **preservada**; só se aprofunda o insuficiente (ROADMAP R1/§24).

### 3.1 Cobertura SOT já existente [FONTE] — a SPEC-021 constrói SOBRE, não redefine

| Ativo interno | Papel | Relação com a SPEC-021 |
|---|---|---|
| **Quality Gates L1–L4** (atomic-spec §7): L1 Operacional · L2 Guiado · L3 Testável · L4 Expert | Gate de qualidade por profundidade (D-levels + revisão) | Já é uma **escada de maturidade de spec** parcial — a SPEC-021 a reconcilia/eleva a modelo normativo por-spec |
| **GPR-001 §11** (L0–L5): L0 Declarativo · L1 Especificado · L2 Guiado · L3 Testável · L4 Autocontrolado · L5 Evolutivo governado | Critério de maturidade do SOT **como sistema agêntico** (estimado hoje entre L0–L1) | Fonte da linguagem L0–L5; hoje é **critério declarativo** — a SPEC-021 o torna verificável por-spec |
| **ROADMAP §12/§21 (texto da SPEC-021):** L0 Declarativo → L1 Especificado → L2 Guiado → **L3 Verificado** → L4 Autocontrolado | Escada de 5 níveis (L0–L4) prometida para a SPEC-021 | Alvo direto — mas há **conflito de rótulos/aridade** com as duas escadas acima (ver CONFLITO-1) |
| **`harness-score`** (`npx harness-score`; F.4 Evaluation, atomic-spec §5/§7) | Maturidade **repo-global** (hoje) | ROADMAP §12: SPEC-021 "torna o harness-score normativo **por spec** (não só repo-global)" |
| **SPEC-020 núcleo A** (9 lentes constitutivas, BASELINE) | Avaliação constitutiva de spec-time (F.4) | Insumo direto: a maturidade de uma spec é função de *quais lentes/D-levels ela satisfaz* (Q-R4) |
| **P13 / D9 / SPEC-041** (reconstrutibilidade/auditoria) | Rastreabilidade da decisão | Âncora para níveis altos de maturidade (verificável ≥ documentado) |

### 3.2 Decisões adotar/adaptar/rejeitar/adiar

| Tópico externo | Decisão | Porquê |
|---|---|---|
| **Ideia de níveis staged/continuous (M1 CMMI/SPICE)** | **ADAPTAR** (conceito) | A distinção *staged (agregado)* vs *continuous (por processo/spec)* modela exatamente "repo-global vs por-spec" (ROADMAP §12). Adotar a **lógica**, rejeitar os rótulos/estruturas específicas (INV-09) |
| **Maturidade organizacional/empresarial (M2/M3/M7 org-level)** | **REJEITAR como baseline** | O SOT mede **specs/artefatos**, não uma organização; modelos org-level (pilares de talento/cultura/estratégia) estão fora do escopo (ver Non-goals). Podem entrar só como referência histórica |
| **Maturidade de artefato de engenharia (M5 codebase, M10 MLOps L0–L2)** | **ADAPTAR** | Convergente com "maturidade por spec"; a lógica "nível alto exige automação/verificação, não só documento" reforça o mandato anti-volume |
| **DEMM — agregação por-propriedade em rubrica de níveis (M6)** | **ADAPTAR (conceito, não implementação)** | Convergente com o SOT: maturidade = agregação **verificável** de propriedades satisfeitas (≈ D-levels + lentes SPEC-020), com categoria "conflicting" (≈ INDETERMINADO). Reforça reconstrutibilidade (P13). Ferramental/adapters do DEMM = runtime → **ADIAR** |
| **Rubricas por nível (M9)** | **ADOTAR (como método)** | Rubrica que descreve "o que é bom" por nível torna cada nível **verificável**, alinhado ao EARS/`VERIFICADO POR` e a ENF-03 (gate determinístico) |
| **Anti-Goodhart / avaliar o avaliador (M8)** | **ADOTAR (como princípio de desenho)** | Materializa a exigência da ROADMAP §12 ("maturidade ≠ volume de documentação"). Método: nível ancorado em evidência verificável, nunca em contagem de artefatos |
| **Autonomia como eixo de maturidade (M4 "Dark Factory"/L5)** | **ADAPTAR com cautela** | O nível mais alto do SOT (L4 Autocontrolado / L5 Evolutivo governado — GPR §11) é **governado** (learning propõe, governança decide — ENF-05); rejeitar qualquer noção de autonomia que dispense o trio/Andraus (INV-09, ENF-05) |
| **Ferramental/telemetria de maturidade de runtime (M6 adapters, M10 pipelines)** | **ADIAR** | Fase spec-first (ROADMAP §22); tooling de runtime = SPEC-045-RUNTIME-001 (decisão aberta separada, não antecipada) |
| **Rótulos/aridade de escadas externas (5 níveis CMMI, 6 níveis SPICE, L0–L5 vendor)** | **REJEITAR como baseline** | Mesma classe de colisão dos Master Contracts (K-MAN — G-gates/ladders externos rejeitados); a escada canônica do SOT é decisão interna (Q-A2), nunca importada |

### 3.3 Modelos canônicos — fronteiras (CC-01/CC-02)

- Nenhum item ADOTADO redefine CEM/CHM/CCM/CDM/CNM (CC-02) nem toca a hierarquia Elliott→ICT (CC-01). A SPEC-021 é **meta-harness de avaliação de maturidade de specs** — não computa análise técnica. **CCM-001 permanece pendente (SPEC-003)**; nenhum limiar numérico ligado à convicção é fixado (J-001 aberto).

---

## 4. Lacunas, conflitos e INDETERMINADOS (NÃO fecham decisão aberta — CONS-01)

- **CONFLITO-1 — três escadas de maturidade internas divergentes.** O SOT já carrega **três** escadas parcialmente incompatíveis: (a) **Quality Gates L1–L4** (L1 Operacional/L2 Guiado/**L3 Testável**/L4 Expert — atomic-spec §7); (b) **GPR-001 §11 L0–L5** (L0 Declarativo…**L3 Testável**…L4 Autocontrolado/L5 Evolutivo governado); (c) **ROADMAP §12/§21 texto da SPEC-021** (L0 Declarativo→L1 Especificado→L2 Guiado→**L3 Verificado**→L4 Autocontrolado). Há divergência de **aridade** (4 vs 6 vs 5 níveis) e de **rótulo do L3** ("Testável" vs "Verificado"). **A SPEC-021 é exatamente o lugar de reconciliar isso** — mas a escolha da escada canônica é **[DECISÃO NECESSÁRIA]** de Andraus (Q-A2). Esta pesquisa **não** a fecha (CONS-01). [FONTE: atomic-spec §7; GPR-001 §11; ROADMAP §12/§21]
- **CONFLITO-2 — "maturity model" externo é majoritariamente organizacional.** M2/M3/M7 medem organizações; o SOT mede specs. Importar pilares org-level (estratégia/talento/cultura) seria erro de escopo. **Rejeitar como baseline**; adaptar apenas a *lógica de níveis* de M1/M5/M6. [FONTE: INV-09; ROADMAP §24]
- **CONFLITO-3 — LLM-as-Judge / score automático como gate.** Prática de mercado (M9) usa LLM-as-judge para pontuar; o SOT proíbe LLM como gate (ENF-03). **Resolução na Spec:** o cálculo de nível de maturidade é **gate determinístico** (quais D-levels/lentes estão de fato presentes e verificados); o LLM é, no máximo, detector. Já normado por ENF-03 — não é decisão aberta nova. [FONTE: ENF-03; SPEC-020 RULE-EV-02]
- **GAP-1 — gaming/Goodhart (maturidade ≠ volume).** Como **garantir** que um nível alto não é obtido por inflar documentação/telemetria é **problema aberto na literatura** (M8) — parcialmente endereçado por "evidência de propriedade" (M6), sem solução fechada. Para o SOT: registrar como risco a tratar no desenho da Spec (ancorar nível em evidência verificável), sem inventar métrica anti-gaming definitiva. **INDETERMINADO** (não fabricar métrica — RULE-MET-01). [EXTERNO/INFERÊNCIA]
- **GAP-2 — limiares numéricos.** Qualquer *threshold* numérico de aprovação ligado a convicção/score depende de **J-001** (aberto). A SPEC-021 define **níveis ordinais qualitativos** (por presença/verificação de D-levels e lentes), **não** limiares numéricos dependentes de convicção. **INDETERMINADO até J-001/CCM-001 (SPEC-003).** [FONTE: J-001; INV-03; CONS-01]
- **GAP-3 — normativo vs consultivo.** ROADMAP §12 diz "torna o harness-score **normativo** por spec". Se a maturidade vira **gate** (bloqueia homologação abaixo de nível-alvo) ou permanece **score consultivo** (informa, não bloqueia) é **[DECISÃO NECESSÁRIA]** (Q-A3) — impacta o nível de Enforcement (E2 vs E3). Esta pesquisa não a fecha (CONS-01).

Nenhuma decisão aberta é fechada por esta pesquisa (RULE-ECC-02 / CONS-01).

---

## 5. Proposta de Definição da SPEC-021 (para homologação de Andraus)

### 5.1 Número, quantidade, decomposição — [PROPOSTA]

- **Número:** **SPEC-021** (slot mantido; número monotônico, não reutilizado — RULE-ECC-01).
- **Quantidade:** **1 (uma) Spec** — não decomposta.
  - *Porquê:* o modelo de maturidade é um **artefato único e coeso** (uma escada + regra de atribuição de nível + acoplamento ao gate); decompor fragmentaria um único meta-harness sem ganho de atomicidade (ROADMAP §24 — não maximizar quantidade de documentos).
- **Complexidade:** **HIGH · D0–D7 · maturidade-alvo L3** (Testável: D5 + ≥3 cenários D7 + ≥1 adversarial D8 + revisão independente — atomic-spec §7). [FONTE: ROADMAP §12; AGENTS.md §4]
  - *Nota:* HIGH → D0–D7 (standard). O D8 adversarial não é piso obrigatório para HIGH, mas **será aplicado** (§7-bis é obrigatório para HIGH/CRITICAL — especificador.md §7-bis) e alimenta a maturidade-alvo L3 ("≥1 adversarial D8").

### 5.2 Missão (comportamental, sem implementação) — [PROPOSTA]

Especificar **como a maturidade de cada Spec do SOT Harness é medida e atribuída**: definir uma **escada de maturidade canônica única** (reconciliando Quality Gates L1–L4, GPR-001 §11 L0–L5 e a escada L0–L4 da ROADMAP §12 — sujeito a Q-A2), a **regra verificável de atribuição de nível** por spec (função de quais D-levels e quais lentes da SPEC-020 a spec de fato satisfaz e verifica — não do volume de documentação), e o **acoplamento ao gate de spec-time**, com **gate determinístico** e o LLM apenas como detector (ENF-03). Torna o `harness-score` **normativo por spec**, não só repo-global.

### 5.3 Escopo (dentro) — [PROPOSTA]

1. **Escada de maturidade canônica única** (níveis, nomes, critério objetivo de cada nível) — reconciliando as três escadas internas (CONFLITO-1). [sujeito a Q-A2]
2. **Regra de atribuição de nível por spec** — determinística, ancorada em evidência verificável (D-levels presentes + lentes SPEC-020 em PASS/REGRESSED), **anti-gaming** (nível ≠ contagem de documentos — GAP-1). [EARS + BASpec]
3. **Acoplamento ao gate de spec-time** (RULE-HG-06 / Constitution Check) — como o nível de maturidade condiciona (ou informa) a elegibilidade à homologação. [sujeito a Q-A3]
4. **`harness-score` normativo por spec** — o critério que torna o score por-spec (não só repo-global), reutilizando a distinção staged/continuous (M1). [FONTE: ROADMAP §12]
5. **Relação maturidade × avaliação (SPEC-020)** — maturidade como agregação ordinal dos critérios já avaliados; sem duplicar as 9 lentes.
6. **Método adversarial/robustez** do próprio modelo de maturidade (D8 + §7-bis/Passo 5-bis), incluindo casos de gaming.
7. **Enforcement Contracts** dos atos de atribuição/gate de maturidade (E2/E3 conforme Q-A3).
8. **Declaração de Classe por BASpec com efeito** (RULE-MECH-01/CC-11 — ver §6, ponto de atenção).

### 5.4 Fora do escopo (Non-goals) — [PROPOSTA]

| Item | Pertence a | Justificativa |
|---|---|---|
| Redefinir as 9 lentes da SPEC-020 | **SPEC-020** (BASELINE) | Maturidade **consome** as lentes; não as redefine (CC-02 análogo) |
| Fechar dimensões **classe B** da SPEC-020 | **SPEC-007/038/014** (BL-017) | Diferidas; não antecipadas (CONS-01) |
| Limiares numéricos dependentes de convicção | **J-001 / CCM-001 (SPEC-003)** | J-001 aberto — maturidade é ordinal/qualitativa (GAP-2) |
| Maturidade **organizacional/empresarial** (pilares de estratégia/talento/cultura) | — (fora do SOT) | SOT mede specs, não organização (CONFLITO-2); rejeitado como baseline |
| **Tooling de runtime** / telemetria de maturidade em execução | Fase de implementação; SPEC-045-RUNTIME-001 | Fase spec-first (ROADMAP §22); decisão aberta separada, não antecipada |
| Meta-Cognitive Supervisor / auditoria D9 completa | **SPEC-024 / SPEC-041** | Níveis altos referenciam esses componentes; não os especificam aqui |
| Redefinir Quality Gates L1–L4 ou a hierarquia | atomic-spec §7 ; PC-01 | Constrói SOBRE; reconcilia sem apagar (INV-07) |
| Adotar rótulos/ladders externos (CMMI/SPICE/NIST janelas/vendor L0–L5) como baseline | — | Rejeitados (INV-09); referência subordinada apenas |

### 5.5 Capacidades §26 cobertas

- Cobre integralmente a capacidade **"SPEC-021 — Harness Score / Maturity Model"** (ROADMAP §26). Nenhuma capacidade da FASE GOV fica descoberta ao fim desta Spec: SPEC-019 (governança) ✅ + SPEC-020 núcleo A (avaliação) ✅ + SPEC-021 (maturidade) fecham a FASE GOV; classe B da SPEC-020 permanece **declaradamente diferida** (BL-017 — não é achado de gate: diferida por decisão homologada EUA-E17). [FONTE: ROADMAP §12/§21/§26]

### 5.6 Herança prevista (a declarar no Plan — CC-08 / RULE-HV) — [PROPOSTA]

- **INHERITS:** atomic-spec.md **v1.4** (BASpec, D0–D7, Enforcement E0–E3, F.1–F.4, EARS, TRACE-06, **Quality Gates L1–L4 §7**); **SPEC-019 v1.0 baseline** (RULE-HG-06 Constitution Check como gate; RULE-HG-03 CONFORME≠vigência; RULE-HG-02/ENF-05 policies não auto-aprovadas); **SPEC-020 v1.0 baseline** (9 lentes / RULE-EV-01..07 — maturidade agrega os critérios das lentes); **GPR-001 v1.0** (§11 escada L0–L5; PE-04 refinado por CLASSE-MECH-001; 4Es); ENF-01..08 (ênfase ENF-03 Detector≠Gate); INV-05/07/09.
- **Eixo VERTICAL (RULE-HV):** avaliar no Plan. Hipótese preliminar [INFERÊNCIA]: SPEC-021 é **irmã** de SPEC-019/SPEC-020 na FASE GOV (meta-harnesses), não decomposição *micro* de um *macro* — provável **não-aplicação** da conservação-como-conjunto vertical, como já se decidiu para a SPEC-020 (plan.md §Herança). A confirmar no Plan.
- **Método da FASE GOV = atomic-spec v1.4** (v1.5 não homologada) [FONTE: DHR-EUA-E17 §3].

### 5.7 Re-apontamento de gatilhos RMR-001 e passo 11-bis

- **Nenhum re-apontamento necessário:** o slot SPEC-021 é **mantido** (não dividido/fundido/renumerado/descartado) — RULE-ECC-01 não exige re-apontamento. [FONTE: RMR-001 §3]
- **Heads-up para o gate da abertura/início do Plan:**
  - **BL-021** (adaptar ferramental à EUA-E21) — já **Absorvido** (2026-09-27, DHR-SPEC020-001); o check `[STRUCT-11] Dossiê de Pesquisa presente` do `validate_spec_sot.py` incide sobre Specs que citam RULE-ECC-01/02 — a SPEC-021 as citará. Sem ação nova.
  - **BL-020** (acesso web só-leitura do Revisor) — **`ATIVADO`** desde a homologação da SPEC-020 (2026-09-27), encaminhamento pendente de decisão de Andraus — **independente desta abertura** (não bloqueia); registrado.
  - **BL-017** (classe B da SPEC-020) — gatilho `spec:SPEC-007/014/038 em redação`: **NÃO inclui SPEC-021** → não dispara; permanece `Proposto`. Classe B permanece DIFERIDA.
  - **BL-008** segue `ATIVADO` (auditoria retroativa da SPEC-001) — independente desta abertura.
  - **BL-022/BL-023** (PRINC-BID-001 / CLASSE-MECH-001) — **Absorvidos** (2026-09-27); suas RULE (RULE-PD-*, RULE-MECH-*) já vigentes e incidem sobre esta abertura (ver §6).

---

## 6. Resolução do ponto de atenção — RULE-MECH-01 (incide) × RULE-PD-01 (não incide)

> **[DECISÃO NECESSÁRIA de escopo submetida a Andraus, com proposta fundamentada — Q-A5.]** O Especificador propõe a resolução abaixo e a justifica; a confirmação é de Andraus.

### 6.1 RULE-MECH-01 / CC-11 — **INCIDE sobre a SPEC-021** [PROPOSTA — INCIDÊNCIA]

**Texto normativo:** RULE-MECH-01 aplica-se a "Toda BASpec com efeito, em Spec que cita RULE-MECH-01 no próprio texto (**SPEC-002 em diante** — não retroage sobre SPEC-001/019/020, INV-07)". [FONTE: RULES.md RULE-MECH-01; atomic-spec §10.5 CC-11]

**Análise:**
- **Critério numérico:** SPEC-021 ≥ SPEC-002 → dentro de "SPEC-002 em diante". ✔
- **Critério de exclusão:** a lista de não-retroação é **SPEC-001/019/020** (specs já homologadas ANTES da emenda). SPEC-021 **não** está na lista. ✔
- **Critério temporal (intenção "prospectiva"):** a emenda CLASSE-MECH-001 foi homologada em **2026-09-27**; a SPEC-021 está sendo **aberta em 2026-09-27**, ou seja, **após** a homologação (mesmo dia, mas a abertura é ato posterior à homologação registrada em DHR-CLASSE-MECH-001). "Prospectiva" = incide sobre specs abertas depois da vigência; SPEC-021 qualifica. ✔
- **Subtileza do mesmo-dia:** a coincidência de data **não** cria retroação — a homologação precede a abertura na ordem dos atos (a SPEC-021 sequer estava aberta quando a emenda foi homologada). Aplicar a disciplina é, ademais, **conservador** (fail-safe): declarar Classe não pode violar nenhum invariante; **omiti-la** numa spec elegível seria NÃO CONFORME Crítica (RULE-MECH-04). [INFERÊNCIA]

**Conclusão proposta:** **RULE-MECH-01 INCIDE.** O `plan.md` da SPEC-021:
- **citará RULE-MECH-01 no próprio texto** (condição de ativação de CC-11);
- **declarará a Classe (D/H/P/C) em cada BASpec com efeito** (§10.6 atomic-spec), com **critério 4Es** explícito (RULE-MECH-02) e **bounded loop + gate de saída** onde H/P (RULE-MECH-03);
- Classes prováveis [INFERÊNCIA, a fixar no Plan por BASpec]: a **atribuição de nível de maturidade** tende a **Classe D/H** (regra determinística sobre presença/verificação de D-levels e lentes; onde houver julgamento qualitativo residual, H com gate de saída); o **enforcement de "não reivindicar nível acima da evidência"** (anti-gaming) tende a **Classe C** (constitutivo — gate obrigatório), *se* o nível de risco justificar (RULE-MECH-02: Classe C em risco baixo = violação de Economicidade). CC-11 verificado por BASpec.

### 6.2 RULE-PD-01 / CC-12 — **NÃO INCIDE sobre a SPEC-021** [PROPOSTA — NÃO-INCIDÊNCIA, justificada]

**Texto normativo:** RULE-PD-01 aplica-se a "Toda Spec que define um **escopo de especialidade** (ex.: Elliott, SMC, ICT)". O atomic-spec §10.7 é explícito: *"Specs de governança/meta-harness (ex.: SPEC-019, **SPEC-020, SPEC-021**) tipicamente não declaram `PD-xx`."* [FONTE: atomic-spec §10.7; RULES.md RULE-PD-01; GPR-001 §2.7 Cláusula 1]

**Análise:**
- A SPEC-021 é **meta-harness** (modelo de maturidade de specs — F.4 Evaluation), **não** define escopo de especialidade de **domínio de mercado** (não é Elliott/Fibonacci/SMC/ICT/estrutural). Não gera sub-princípios operacionais de leitura de mercado.
- `PD-xx` existe para capturar princípios de **domínio de análise técnica** fundamentados em pesquisa `[EXTERNO]` de mercado — inaplicável a um modelo de maturidade.
- Precedência RULE-MECH-01 → RULE-PD-01 (Classe antes de PD): mesmo que se cogitasse, as BASpecs da SPEC-021 não são de julgamento semântico de domínio de mercado — não geram `PD-xx` (GPR-001 §2.7, ordenação).

**Conclusão proposta:** **RULE-PD-01 NÃO INCIDE.** No Constitution Check do `plan.md`, **CC-12 = N/A com justificativa explícita** (não mera omissão): *"SPEC-021 é meta-harness de maturidade, não define escopo de especialidade de domínio de mercado; atomic-spec §10.7 nomeia a SPEC-021 como exemplo de meta-harness que tipicamente não declara `PD-xx`. Nenhum `PD-xx` proposto."* Consistente com o tratamento de CC-10 na SPEC-020 (N/A justificado). [FONTE: atomic-spec §10.7; SPEC-020/plan.md CC-10]

---

## 7. Perguntas que Andraus precisa decidir (homologação da definição)

- **Q-A1 (escopo/quantidade):** Aprova **SPEC-021 como 1 Spec HIGH (D0–D7, maturidade-alvo L3), não decomposta** (§5.1–5.4)? [DECISÃO NECESSÁRIA]
- **Q-A2 (escada canônica — CONFLITO-1):** Qual escada de maturidade a SPEC-021 fixa como **única canônica**? Opções: **(i)** adotar a linguagem **GPR-001 §11 L0–L5** (6 níveis, mais completa, inclui "L5 Evolutivo governado") e mapear Quality Gates L1–L4 dentro dela; **(ii)** adotar a escada **L0–L4** do texto da ROADMAP §12 (5 níveis) e tratar "L5 Evolutivo governado" como fora do alvo; **(iii)** outra reconciliação. Inclui resolver o **rótulo do L3** ("Testável" vs "Verificado"). O Especificador **não** decide (CONS-01). *(Proposta de trabalho, não vinculante: (i) L0–L5 do GPR-001 como espinha, absorvendo Quality Gates L1–L4 e renomeando/alinhando L3 — por ser a mais rica e já homologada em GPR-001.)* [DECISÃO NECESSÁRIA]
- **Q-A3 (normativo vs consultivo — GAP-3):** A maturidade por-spec é **gate normativo** (bloqueia elegibilidade à homologação abaixo do nível-alvo declarado, efeito **E3**) ou **score consultivo** (informa o Revisor/Andraus, efeito **E2**)? ROADMAP §12 diz "normativo por spec" — confirmar a força e o nível de Enforcement. [DECISÃO NECESSÁRIA]
- **Q-A4 (limiares/J-001):** Confirma que a SPEC-021 usa **níveis ordinais qualitativos** (presença/verificação de D-levels + lentes), **adiando** qualquer limiar numérico dependente de convicção a **J-001/CCM-001 (SPEC-003)** — mantendo GAP-2 aberto (CONS-01)? [DECISÃO NECESSÁRIA]
- **Q-A5 (ponto de atenção — Classe/PD):** Confirma a resolução do §6 — **RULE-MECH-01/CC-11 INCIDE** (Classe D/H/P/C por BASpec com efeito) e **RULE-PD-01/CC-12 = N/A justificado** (meta-harness, não especialidade de mercado)? [DECISÃO NECESSÁRIA]
- **Q-A6 (ECC-VAL-001):** Validade deste Dossiê (data de acesso 2026-09-27) — propõe-se, por analogia à SPEC-020 (Q-A6), **30 dias corridos OU início da redação do Plan, o que ocorrer primeiro**, escopo **apenas esta Spec** (ECC-VAL-001 permanece aberta como regra geral). Confirma? [DECISÃO NECESSÁRIA]
- **Q-A7 (EUA-E18 Q7 — procedimental):** A SPEC-021 é a **3ª spec** sob o protocolo §7-bis/Passo 5-bis; a nota do gate EUA-E18 agenda para ela a **checagem de proporcionalidade** do protocolo. Confirma que essa checagem será conduzida no relatório de revisão da SPEC-021? [DECISÃO NECESSÁRIA — procedimental]

Decisões que **permanecem ABERTAS** independentemente desta abertura (CONS-01): J-001; SPEC-045-RUNTIME-001; RISK-ARR-LOC-001; RISK-CONV-001; ECC-VAL-001 (regra geral); ECC-03-001; classe B da SPEC-020 (BL-017).

---

## 7-bis. Registro de Homologação da Definição de Abertura (Andraus, 2026-09-28)

Todas as 7 perguntas RESOLVIDAS por Andraus. Parecer do Revisor sobre este Dossiê: **CONFORME** (1 achado Menor A-01, fontes pós-treino, não bloqueante).

- **Q-A1 — RESOLVIDA:** Aprovado. 1 Spec HIGH, D0–D7, não decomposta.
- **Q-A2 — RESOLVIDA (diferente da proposta de trabalho §7):** a escada canônica **por-Spec é a do ROADMAP §12/§21** (`L0 Declarativo → L1 Especificado → L2 Guiado → L3 Testável → L4 Autocontrolado`, 5 níveis) — **não** a do GPR-001 §11 como espinha. Razão: é literalmente o que a SPEC-021 foi comissionada a formalizar (ROADMAP §21: "torna o harness-score normativo por spec"). Reconciliação aplicada: (a) rótulo do L3 harmonizado para "Testável" no ROADMAP §12 (era "Verificado"); (b) Quality Gates L1–L4 (atomic-spec §7) passam a ser a **tabela de critérios** por trás de cada nível desta escada, não escada concorrente; (c) GPR-001 §11 (L0–L5) permanece **eixo diferente e não substituído** — maturidade do SOT como sistema agêntico inteiro, escopo explicitado em nota própria. Editado: `ROADMAP.md` (§12 SPEC-021), `governance/GPR-001_...md` (§11, nota de escopo), `atomic-spec.md` (§7, nota de escopo).
- **Q-A3 — RESOLVIDA:** Normativo, nível **E3** — abaixo do nível-alvo declarado bloqueia elegibilidade à homologação.
- **Q-A4 — RESOLVIDA:** Confirmado. Níveis ordinais qualitativos; limiares numéricos ligados a convicção permanecem adiados a J-001/CCM-001.
- **Q-A5 — RESOLVIDA:** Confirmado. RULE-MECH-01/CC-11 incide sobre a SPEC-021 (Classe D/H/P/C por BASpec com efeito, a citar no Plan); RULE-PD-01/CC-12 = N/A justificado (meta-harness, sem domínio de especialidade de mercado).
- **Q-A6 — RESOLVIDA:** Confirmado. Validade do Dossiê = 30 dias corridos OU início do Plan (o que ocorrer primeiro) — escopo só esta Spec; Plan inicia hoje (2026-09-28), dentro da validade.
- **Q-A7 — RESOLVIDA:** Confirmado. Checagem de proporcionalidade EUA-E18 Q7 será conduzida no relatório de revisão semântica do Plan desta Spec (3ª sob o protocolo §7-bis/Passo 5-bis).

**Abertura da SPEC-021 HOMOLOGADA.** Próximo passo: redação do `plan.md` + `checks.md` pelo Especificador, incorporando as resoluções acima.

---

## 8. Autoverificação da abertura (RULE-ECC-02 — parte determinística)

```
[x] Web disponível em 2026-09-27 → abertura NÃO suspensa (RULE-ECC-02).
[x] Dossiê presente e completo (HIGH): questões+estratégia; fontes classificadas e [EXTERNO]; data de acesso; comparação adotar/adaptar/rejeitar/adiar; lacunas/conflitos; escopo/quantidade/número; re-apontamento avaliado.
[x] Conteúdo web tratado como DADO; nenhuma importação automática; nada vira baseline (DHR-PROV-WEB-001 §2.1).
[x] Nenhuma decisão aberta fechada (CONS-01): J-001, escada canônica (Q-A2), normativo/consultivo (Q-A3, GAP-3), ECC-VAL-001, classe B (BL-017) permanecem abertas; INDETERMINADO usado (GAP-1/GAP-2).
[x] Etiquetagem aplicada: [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO].
[x] Fronteiras SOT respeitadas: CC-01 (hierarquia intocada), CC-02 (canônicos), INV-05 (não executa), ENF-03 (LLM≠gate), 4Es, Quality Gates L1–L4 (construir sobre, não redefinir).
[x] Ponto de atenção resolvido e justificado: RULE-MECH-01/CC-11 INCIDE (§6.1); RULE-PD-01/CC-12 = N/A justificado (§6.2).
[x] Passo 11-bis avaliado: BL-020 ATIVADO (independente, pendente Andraus); BL-017 não incidente; BL-008 independente; BL-021/022/023 Absorvidos (RULE já vigentes).
[x] NÃO é o Plan — Plan adiado à homologação da definição (ROADMAP §23 passo 1-bis).
```

**Pronto para revisão (do Dossiê de abertura).** O Revisor audita presença/estrutura/classificação/etiquetagem/comparação/ausência de importação automática — não a veracidade das páginas (atomic-spec §15). A homologação da definição é de Andraus, antes do Plan.

---

## Sources (fontes [EXTERNO] — acesso 2026-09-27)

- [AI in 2026: Predictions Mapped to the Agentic AI Maturity Model (A. Arsanjani, Medium)](https://dr-arsanjani.medium.com/ai-in-2026-predictions-mapped-to-the-agentic-ai-maturity-model-c6f851a40ef5)
- [AI Security Maturity Model: 5 Levels Explained 2026 (Practical DevSecOps)](https://www.practical-devsecops.com/ai-security-maturity-model/)
- [SANS Institute — AI Security Maturity Model](https://www.sans.org/press/announcements/ai-security-maturity-model-close-gap-between-enterprise-ai-adoption-governance)
- [Master the AI Maturity Model for 2026 (Sema4.ai)](https://sema4.ai/blog/ai-maturity-model-2026/)
- [Enterprise AI Agents in 2026: The Maturity Map (SphereInc)](https://www.sphereinc.com/blogs/ai-agents-maturity)
- [AI Maturity: The Complete Enterprise Guide 2026 (Larridin)](https://larridin.com/solutions/ai-maturity-the-complete-enterprise-guide-2026)
- [Introduction to the Agentic AI adoption maturity model (Microsoft Learn)](https://learn.microsoft.com/en-us/agents/adoption-maturity-model/)
- [The AI Codebase Maturity Model (arXiv 2604.09388)](https://arxiv.org/pdf/2604.09388)
- [Decision Evidence Maturity Model for Agentic AI (arXiv 2605.04093)](https://arxiv.org/abs/2605.04093)
- [Evolving AI Risk Management: A Maturity Model based on the NIST AI RMF (arXiv 2401.15229)](https://arxiv.org/pdf/2401.15229)
- [A Flexible Maturity Model for AI Governance based on the NIST AI RMF (IEEE-USA)](https://ieeeusa.org/assets/shop/ebooks/Flexible-Maturity-Model-for-AI-Governance.pdf)
- [Goodhart's Law in Your LLM Eval Suite (TianPan.co, 2026)](https://tianpan.co/blog/2026/04/14/goodharts-law-in-your-llm-eval-suite)
- [LLMs Designing and Applying Evaluation Rubrics (ACL 2026 Findings)](https://aclanthology.org/2026.findings-eacl.335.pdf)
- [LLM Evaluation: Tutorial & Best Practices (LaunchDarkly)](https://launchdarkly.com/blog/llm-evaluation/)
- [MLOps in 2026: From MLflow to LLMOps (CodeX / Medium)](https://medium.com/codex/mlops-in-2026-from-mlflow-to-llmops-the-complete-guide-to-shipping-ai-in-production-0024955b70c4)
- [The ISO/IEC 15504 Measurement Framework for Process Capability and CMMI (academia.edu)](https://www.academia.edu/54295518/The_ISO_IEC_15504_Measurement_Framework_for_Process_Capability_and_CMMI)
- [High Levels of Process Capability in CMMI and ISO/IEC 15504 (SpringerLink)](https://link.springer.com/chapter/10.1007/978-3-642-21233-8_20)
- [CMMI Vs SPICE (Visure Solutions)](https://visuresolutions.com/alm-guide/cmmi-vs-spice/)
```
