# SPEC-020 — Harness Evaluation Specification (núcleo A)

| Campo | Valor |
|---|---|
| ID | SPEC-020 — Harness Evaluation Specification (núcleo A / classe A + 9ª lente principiológica) |
| Versão | 1.0 (candidata) |
| Status | **HOMOLOGADA — BASELINE** (Andraus, 2026-09-27, DHR-SPEC020-001; compat. Minor) |
| Fonte | ROADMAP §12/§21/§25; `research.md` (Dossiê de abertura homologado 2026-09-27, §8); atomic-spec v1.4 |
| Complexidade | **CRITICAL** |
| Profundidade-alvo | **D0–D8** (standard + adversarial) |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE GOV (cont.), posição 2 — após SPEC-019 (HOMOLOGADA), antes de SPEC-021 e de SPEC-002 [FONTE: ROADMAP §12/§21] |
| Nível de maturidade-alvo | L3 (Testável) — D5 + ≥3 cenários D7 + ≥1 adversarial D8 + revisão independente [FONTE: atomic-spec §7] |
| Método | atomic-spec.md **v1.4** (v1.5 não homologada; DHR-EUA-E17 §3 fixa v1.4 para a FASE GOV) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-09-27 |
| Abertura | Dossiê de Pesquisa homologado por Andraus em 2026-09-27 (research.md §8; RULE-ECC-01/02) — Plan iniciado no mesmo dia, dentro da validade do Dossiê (ECC-VAL-001, Q-A6) |
| Incidente resolvido na homologação | **SPEC-020-PRINC-001** (consistência principiológica GPR-001 §15 como critério constitutivo verificável) — efetiva-se **na homologação desta Spec** (não fechada aqui — CONS-01) |

Status: **HOMOLOGADA — BASELINE** (Andraus, 2026-09-27, DHR-SPEC020-001; compat. Minor). Complexidade: CRITICAL. Profundidade-alvo: D0–D8 (standard + adversarial). [FONTE: ROADMAP §12; AGENTS.md §4]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-09-27 | Entrega candidata inicial. Núcleo A (8 lentes classe A) + 9ª lente principiológica (Q-A2). D0–D8. |

---

## Nota de gate (passo 11-bis / RMR-001) — item ATIVADO por esta redação

[FONTE: RMR-001 §6 BL-021; ROADMAP §23 passo 11-bis]

O **início da redação deste Plan** dispara o Gatilho de Ativação de **BL-021 — "Adaptar o ferramental à EUA-E21"** (`spec:SPEC-020 em redação`). Tratamento nesta entrega:

- **BL-021** propõe adaptar 4 scripts (`check_refs.py`, `backlog_triggers.py`, `build_map.py`, `validate_spec_sot.py`) à Especificação Emergente. É item de **tooling/processo**, não altera o conteúdo desta Spec. **Encaminhamento:** registrado como `ATIVADO`; cada sub-item "exige aprovação própria" (RMR-001 §6 BL-021) — não é ação desta Spec e **não bloqueia** a redação do Plan. O gate fecha limpo quanto a BL-021 desde que este tratamento seja registrado. [INFERÊNCIA — coerente com RMR-001 §4]
- **BL-017** (dimensões classe B da SPEC-020) — gatilho `spec:SPEC-007/014/038 em redação`: **NÃO inclui SPEC-020** → **não dispara**; permanece `Proposto`. Promoção é decisão de Andraus (RMR-001 §5), não desta Spec. Classe B permanece DIFERIDA (Q-A5). [FONTE: RMR-001 §6 BL-017]
- **BL-020** (acesso web só-leitura do Revisor) — gatilho `spec:SPEC-020 homologada`: **não disparado** (só na homologação). Registrado. [FONTE: RMR-001 §6 BL-020]
- **BL-008** segue `ATIVADO` (auditoria retroativa da SPEC-001) — independente desta redação. [FONTE: RMR-001 §6 BL-008]

---

## Constitution Check (CC-01..CC-10 — atomic-spec §10.5 + EUA-E04..E14)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** a SPEC-020 é meta-harness de **avaliação de processo de especificação**; não computa análise técnica nem inverte a hierarquia. Ao contrário, a lente **role adherence (L-ROLE)** e a lente **principiológica (L-PRIN, via PC-01/GPR-001 §15)** têm como função **verificar** que specs-filhas (SPEC-002+) preservam a hierarquia Elliott→ICT. A avaliação **protege** CC-01, não o toca. [INFERÊNCIA]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** nenhuma lente redefine modelo canônico. Grounding/correctness usam CEM-001 como idioma da Evidência (INV-10) **sem alterá-lo**; CCM-001 permanece **pendente (SPEC-003)** — nenhum limiar numérico ligado à convicção é fixado aqui. [FONTE: INV-10; CONST-01; research.md §3.3]
- [x] **CC-03 — Conviction Vector:** dimensionalidade=8 permanece **fechada**; Conviction Vector: fórmula/pesos/limiares = J-001 (aberto/pendente). A SPEC-020 **não** parametriza convicção; qualquer limiar numérico de aprovação ligado a convicção é adiado a **J-001/CCM-001 (SPEC-003)** — a Spec é qualitativa (Q-A4). [FONTE: INV-03; J-001 pendente]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. A lente **safety (L-SAFE)** trata as 5+5 Salvaguardas como **invioláveis e prevalentes** sobre qualquer catálogo externo (OWASP/NIST) — que entram apenas como referência subordinada. Custo não entra no Conviction Vector (INV-04). [FONTE: INV-04; CEE-001 §10/§11]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D8 (ROADMAP §12; AGENTS.md §4).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan (plan.md), não Engineering Card. Os campos §59 e a cadeia §60 tornam-se obrigatórios quando as Tasks/Engineering Cards forem produzidas (BUILD adiado — atomic-spec §14). Omissão justificada. [FONTE: atomic-spec §8.1]
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem provida pela cadeia ROADMAP §12 → Dossiê (research.md §8, homologado) → esta Spec.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED preenchidos com ID+versão; REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Eixo **VERTICAL (RULE-HV)** avaliado e declarado **não aplicável** (SPEC-020 é meta-harness irmão de SPEC-019 na FASE GOV, não decomposição pai→filha) — ver nota na seção de Herança. [FONTE: EUA-E04 §8.3; RULE-HD-04]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI, INDETERMINADO, INV-EPI):** aplicado — distinção explícita FATO NORMATIVO / FATO ARQUITETURAL / PROPOSTA / INFERÊNCIA / EXTERNO. Fontes web tratadas como DADO ([EXTERNO], research.md), nunca baseline; nenhuma hipótese tratada como fato; GAP-1 (illusion of compliance) e GAP-2 (limiares) mantidos como **INDETERMINADO**; sem falsa precisão. [FONTE: RULE-EPI; research.md §4]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM):** N/A — o domínio é avaliação de processo de especificação; sem terminologia concorrente por escola de análise técnica. Onde termos externos de eval colidem (LLM-as-Judge, ladders de maturidade), a colisão é registrada e o rótulo **rejeitado** (research.md §4), não adotado. [FONTE: RULE-SEM; research.md §4]

**Disciplinas cognitivas N8–N17 incidentes:** RULE-EPI (hipótese≠fato; INDETERMINADO), RULE-MET-01 (não-fabricação — nenhuma métrica/fonte inventada), RULE-DEC (decisão≠execução — a avaliação **detecta e reporta**; a homologação de spec-filha é de Andraus), RULE-CAU (nenhuma afirmação causal forte sem mecanismo), RULE-UNC (incerteza localizada, não contaminante). INDETERMINADO usado onde há incerteza material.

**Checklist de consistência principiológica (GPR-001 §15) — incorporado como lente L-PRIN (SPEC-020-PRINC-001):** ver BASpec-EV-009 e a seção "Lente 9". A SPEC-020 **operacionaliza** o checklist §15, hoje declarativo (L0–L1), como critério verificável de spec-time. [FONTE: GPR-001 §15; ROADMAP §12]

---

## Herança / Delta (§8.3 — EUA-E04)

```
HERANÇA / DELTA — SPEC-020

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO):
  - Método: atomic-spec.md v1.4 (BASpec, D0–D9, Enforcement E0–E3, F.1–F.4, EARS, TRACE-06,
            Quality Gates L1–L4 §7, taxonomia de Harness F.1–F.4 §5)
  - Governança do Harness: SPEC-019 v1.0 (BASELINE) — em particular:
      • RULE-HG-06 (Constitution Check CC-01..CC-10 como gate obrigatório ANTES do Plan e da
        homologação) — a SPEC-020 ACOPLA suas lentes a este gate já existente
      • RULE-HG-03 (parecer CONFORME ≠ vigência; só Andraus homologa) — decisão≠execução
      • RULE-HG-02/ENF-05 (policies não auto-aprovadas)
  - Hypothesis Harness: SPEC-001 v1.1 (BASELINE) — a dimensão "hypothesis consistency" já é
      fechável (SPEC-001 homologada); usada como âncora da lente correctness/role adherence
      quando a spec-filha manipula hipótese (CHM-001)
  - Princípios: GPR-001 v1.0 (BASELINE) — §15 (checklist de consistência principiológica);
      PC-01..PC-08 (constitucionais); PB-01..PB-10; hierarquia 4Es
  - Enforcement: ENF-01..08 — com ênfase em ENF-03 (Detector ≠ Gate; LLM nunca é seu próprio gate)
  - Invariantes: INV-05 (SOT não executa; produz Signal Package/TMP interno),
      INV-07 (versionamento monotônico), INV-09 (sem baseline informal), INV-10 (CEM-001 idioma),
      INV-04 (custo fora do Conviction Vector)
  - Modelos canônicos (idioma, não redefinidos): CEM-001 (Evidência), CHM-001 (Hipótese)

ADDED (delta local — o que esta spec acrescenta):
  - 9 lentes constitutivas de avaliação de spec-time (L-CORR, L-GRND, L-HALL, L-ROLE, L-CTX,
    L-SAFE, L-REGR, L-ROBU + L-PRIN principiológica) como critérios VERIFICÁVEIS
  - Acoplamento das lentes ao Constitution Check / checks.md como gate de spec-time (SPEC-002+)
  - Método de avaliação por lente: detector (semântico/LLM) vs gate (determinístico) — ENF-03
  - Disciplina de regressão: achado adversarial → caso versionado (INV-07)
  - Operacionalização do GPR-001 §15 (declarativo → verificável): SPEC-020-PRINC-001
  - Enforcement Contracts dos atos de avaliação com efeito de gate (EC-EV-001..004)

MODIFIED (especialização de regra herdada):
  - RULE-HG-06 (Constitution Check como gate) — ESTENDIDA em conteúdo: as 9 lentes tornam-se
    itens avaliáveis acoplados ao mesmo gate, sem alterar o texto de RULE-HG-06 nem criar
    autoridade nova. (A extensão é de cobertura de itens; a mecânica de gate é reutilizada.)

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal / obrigação-a-obrigação** (EUA-E04 §8.3). O **eixo VERTICAL** (RULE-HV-01..04, conservação-como-conjunto pai→filha) foi avaliado e **não se aplica**: a SPEC-020 não é decomposição *micro* de um *macro* SPEC-019 — ambas são meta-harnesses **irmãos** da FASE GOV (SPEC-019 governa *como* specs mudam; SPEC-020 avalia *se* specs satisfazem critérios). Declarar herança vertical seria confundir os eixos (o cenário ADV-HV-07 da própria SPEC-019 alerta contra isso). A dependência de SPEC-019 é por **acoplamento de contrato** (gate RULE-HG-06), não por conservação vertical. [INFERÊNCIA — a confirmar pelo Revisor]

---

## D0 — Missão (Intenção)

A SPEC-020 especifica **como o SOT Harness de Especificação é avaliado** na dimensão constitutiva (classe A): define, para cada uma das **9 lentes** — correctness, grounding, hallucination, role adherence, context management, safety, regression, robustness/adversarial (como método) e **principle consistency** (GPR-001 §15) — **o critério verificável de spec-time** que toda Spec de componente (SPEC-002+) DEVE satisfazer **durante a produção**, com **gate determinístico** e o LLM apenas como **detector** (ENF-03). [FONTE: ROADMAP §12; research.md §5.2]

A avaliação é um **meta-harness** (F.4 Evaluation da taxonomia atomic-spec §5): mede a qualidade das próprias Specs. Materializa a orientação da ROADMAP §12 — as lentes "tornam-se critérios constitutivos que SPEC-002+ devem satisfazer durante a produção (não apenas sensores posteriores)".

**O que a Missão NÃO é (fronteira):**
- Não é modelo de **maturidade** L0–L4 por spec → **SPEC-021**. [FONTE: ROADMAP §12]
- Não fecha as dimensões **classe B** (RAG faithfulness / tool correctness / decision traceability) → **SPEC-007/038/014 (BL-017)**. [FONTE: ROADMAP §12; RMR-001 BL-017]
- Não fixa limiar numérico dependente de convicção → **J-001 / CCM-001 (SPEC-003)**. [FONTE: J-001]
- Não especifica **tooling de avaliação de runtime** → fase de implementação; SPEC-045-RUNTIME-001 permanece decisão aberta separada, **não antecipada** (Q-A3). [FONTE: ROADMAP §20/§22]
- Não redefine CEM/CHM/CCM/CDM/CNM (CC-02) nem a hierarquia (CC-01).

**Status epistemológico:** a SPEC-020 é FATO ARQUITETURAL candidato a baseline. atomic-spec v1.4, SPEC-019 v1.0, SPEC-001 v1.1, GPR-001 v1.0, INV-*, ENF-* são FATO NORMATIVO. Fontes externas de eval (research.md §2) são [EXTERNO] — DADO, nunca baseline; documentado ≠ homologado (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | Definição verificável das **9 lentes** (8 classe A + principiológica) como critérios constitutivos (EARS + BASpec) | ROADMAP §12; research.md §5.3 |
| S2 | **Acoplamento ao Constitution Check / `checks.md`** — como cada lente vira item de gate de spec-time para SPEC-002+ | Q-A3; RULE-HG-06; research.md §3.2 |
| S3 | **Método de avaliação** por lente: detector (semântico/LLM) vs gate (determinístico); trajetória/trace como alvo | ENF-03; research.md §3.1 |
| S4 | **Método adversarial/robustez** (como avaliar), articulado com D8 e §7-bis/Passo 5-bis, sem duplicar SPEC-022 | research.md §3 (robustness) |
| S5 | **Disciplina de regressão**: converter achado adversarial em caso versionado (INV-07), articulada com F.3/CI, sem escrever código | INV-07; research.md §3 (regression) |
| S6 | **Incorporação de SPEC-020-PRINC-001** — operacionalizar GPR-001 §15 (declarativo→verificável) como 9ª lente | ROADMAP §12; Q-A2 |
| S7 | **Enforcement Contracts** dos atos de avaliação com efeito de gate (E2/E3 conforme criticidade) | ENF-01; atomic-spec §10 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Modelo de maturidade L0–L4 por spec | **SPEC-021** | Segue o núcleo A; maturidade ≠ avaliação constitutiva [FONTE: ROADMAP §12] |
| Dimensões **classe B** (RAG faithfulness / tool correctness / decision traceability) | **SPEC-007 / 038 / 014** (BL-017) | DIFERIDAS por EUA-E17 + BL-017; não fechadas antes do componente-alvo (CONS-01) [FONTE: ROADMAP §12] |
| Limiares numéricos dependentes de convicção | **J-001 / CCM-001 (SPEC-003)** | J-001 aberto — [DECISÃO NECESSÁRIA]; Spec qualitativa (Q-A4) |
| Tooling de avaliação de **runtime** / execução | Fase de implementação; SPEC-045-RUNTIME-001 | Fase spec-first (ROADMAP §22); decisão aberta separada, não antecipada (Q-A3) |
| Produzir os **casos** de teste cognitivo/adversarial integrado | **SPEC-022** | SPEC-020 fixa o *método* de avaliar robustez; SPEC-022 produz os casos |
| Redefinir CEM/CHM/CCM/CDM/CNM ou a hierarquia | CEM/CHM/... ; PC-01 | CONST-01 / CC-01 / CC-02 |
| Adotar rótulos/ladders externos (NIST janelas, OWASP como norma, LLM-as-Judge-gate) | — | Rejeitados como baseline (research.md §4 CONFLITO-1/2/3) |

---

## D2 — Regras

> **Etiqueta:** as RULE-EV-* abaixo são **[PROPOSTA]** — tornam-se normativas apenas na homologação de Andraus + registro no RULES.md pelo Controlador (nova seção "Regras de Avaliação do Harness (RULE-EV)"). Até lá, não são invocáveis como FATO NORMATIVO (RULE-HG-02). As RULE/INV/ENF citadas como fundamento (ENF-03, RULE-HG-06, INV-07, RULE-EPI, RULE-MET-01, GPR-001 §15) **já existem** e são FATO NORMATIVO.
>
> **Nota pós-homologação (aditiva — INV-07, não altera o texto acima):** RULE-EV-01..07 foram registradas por escrito em `governance/RULES.md` §"Regras de Avaliação do Harness (RULE-EV)" em 2026-09-28, completando a obrigação de RULE-HG-02 (a etiqueta [PROPOSTA] acima descreve o estado no momento da homologação desta Spec, 2026-09-27, e é preservada como registro histórico).

```
RULE-EV-01: Toda Spec de componente (SPEC-002+) DEVE ser avaliada, ANTES da homologação, pelas 9
            lentes constitutivas (correctness, grounding, hallucination, role adherence,
            context management, safety, regression, robustness/adversarial, principle consistency),
            acopladas ao Constitution Check / checks.md como gate de spec-time.
            [Fonte: ROADMAP §12; RULE-HG-06; research.md §3.2]  [PROPOSTA]

RULE-EV-02: A avaliação de cada lente DEVE separar DETECTOR de GATE: componente semântico/LLM atua
            como DETECTOR (sinal); o GATE é determinístico e/ou a homologação de Andraus.
            O LLM NUNCA é o gate de aprovação de uma Spec.
            [Fonte: ENF-03; atomic-spec §5/§10.1]  [PROPOSTA]

RULE-EV-03: A lente hallucination é DETECTOR, não gate autônomo: um sinal de alucinação alimenta o
            Revisor/gate determinístico, nunca aprova nem reprova sozinho por juízo de LLM.
            [Fonte: ENF-03; RULE-MET-01; research.md §3 (hallucination)]  [PROPOSTA]

RULE-EV-04: Achado adversarial (D8 / §7-bis / Passo 5-bis) que revele falha constitutiva DEVE ser
            convertido em caso de regressão VERSIONADO e preservado (nunca deletado).
            [Fonte: INV-07; research.md §3 (regression)]  [PROPOSTA]

RULE-EV-05: Nenhuma lente DEVE fixar limiar numérico de aprovação dependente de convicção; tais
            limiares permanecem em J-001/CCM-001 (SPEC-003). Avaliação é qualitativa até J-001.
            [Fonte: J-001; INV-03; CONS-01; Q-A4]  [PROPOSTA]

RULE-EV-06: A lente principle consistency (SPEC-020-PRINC-001) DEVE aplicar o checklist do GPR-001 §15
            como itens verificáveis; contradição com princípio PC-xx = reprovação; conflito com PB-xx
            DEVE ser registrado e justificado (explicabilidade da ponderação, PB-06).
            [Fonte: GPR-001 §14/§15; ROADMAP §12; Q-A2]  [PROPOSTA]

RULE-EV-07: As Salvaguardas Constitucionais (CEE-001 §10/§11) e os invariantes PC-xx PREVALECEM sobre
            qualquer catálogo/benchmark externo (OWASP/NIST/etc.); referência externa é subordinada e
            nunca baseline.
            [Fonte: INV-04; CEE-001; research.md §3 (safety), §4]  [PROPOSTA]
```

---

## Critérios de Aceitação (EARS)

1. Quando uma Spec de componente (SPEC-002+) é submetida à homologação sem avaliação pelas 9 lentes constitutivas, o Harness Evaluation DEVE bloquear a elegibilidade à homologação.
2. Quando um detector semântico (LLM) sinaliza uma violação, o Harness Evaluation NÃO DEVE tratar esse sinal como gate de aprovação — a decisão DEVE permanecer no gate determinístico e/ou em Andraus.
3. Quando uma afirmação de uma Spec-filha não está ancorada em Evidência/fonte rastreável (grounding), o Harness Evaluation DEVE marcar a lente grounding como reprovada.
4. Quando uma Spec-filha atribui a um agente uma responsabilidade fora do seu domínio hierárquico (ex.: ICT criando hipótese estrutural), o Harness Evaluation DEVE reprovar a lente role adherence.
5. Quando um achado adversarial revela falha constitutiva, o Harness Evaluation DEVE exigir a conversão do achado em caso de regressão versionado, preservado (INV-07).
6. Quando uma Spec-filha contradiz um princípio constitucional PC-xx (GPR-001 §15), o Harness Evaluation DEVE reprovar a lente principle consistency.
7. Quando uma lente tenta fixar um limiar numérico de aprovação dependente de convicção, o Harness Evaluation DEVE rejeitar o fechamento e manter o critério qualitativo (J-001 aberto).
8. Quando um catálogo externo (OWASP/NIST) conflita com uma Salvaguarda Constitucional, o Harness Evaluation DEVE fazer prevalecer a Salvaguarda e tratar a referência externa como subordinada.
9. Quando uma Spec-filha declara alta aderência a princípios de segurança mas não demonstra competência de tarefa (illusion of compliance), o Harness Evaluation DEVE registrar a lente safety como INDETERMINADO e encaminhar ao método adversarial.

---

## D3 — Comportamento (BASpecs — as 9 lentes constitutivas)

### BASpec-EV-001 — Lente 1: Correctness

```
BASpec-EV-001:
  QUANDO:       Uma Spec-filha (SPEC-002+) é avaliada quanto a correctness
  ENTÃO:        Harness Evaluation exige que cada comportamento tenha VERIFICADO POR mensurável
                (cenário DADO/QUANDO/ENTÃO com output concreto) e trace reconstruível (P13);
                ausência de critério verificável = reprovação da lente
  PORQUE:       Correção só é avaliável se o comportamento é verificável, não apenas declarativo
                (atomic-spec §1 P13; Quality Gates L3)
  REFERÊNCIA:   RULE-EV-01; atomic-spec §1/§7; [EXTERNO] research.md E5/E7/E8/E10
  VERIFICADO POR:
    DADO        Spec-filha com BASpec sem campo VERIFICADO POR
    QUANDO      Harness Evaluation aplica a lente correctness
    ENTÃO       lente = REPROVADA, código "CORRECTNESS_NOT_VERIFIABLE"
    VERIFICAÇÃO relatório aponta a BASpec sem cenário; gate de spec-time não passa
```

### BASpec-EV-002 — Lente 2: Grounding

```
BASpec-EV-002:
  QUANDO:       Uma afirmação de uma Spec-filha assere fato de mercado/estrutura/decisão
  ENTÃO:        Harness Evaluation exige âncora rastreável (Evidência CEM-001 / fonte / RULE);
                afirmação sem âncora = reprovação da lente grounding
  PORQUE:       Toda afirmação deve ser ancorada (cadeia Fonte→Dado→Evidência→Hipótese; RULE-EPI);
                CEM-001 é o idioma da Evidência (INV-10) — não redefinido
  REFERÊNCIA:   RULE-EV-01; RULE-EPI; INV-10; [EXTERNO] research.md E4/E7/E9
  VERIFICADO POR:
    DADO        Spec-filha afirma "X é institucional" sem Evidência/fonte
    QUANDO      Harness Evaluation aplica a lente grounding
    ENTÃO       lente = REPROVADA, código "UNGROUNDED_CLAIM"
    VERIFICAÇÃO afirmação sem âncora identificada; gate não passa
```

### BASpec-EV-003 — Lente 3: Hallucination (DETECTOR, não gate)

```
BASpec-EV-003:
  QUANDO:       Uma Spec-filha referencia artefato/decisão/RULE/fonte
  ENTÃO:        Harness Evaluation roda DETECTOR de não-existência (referência inexistente, artefato
                inventado, falsa precisão); o sinal alimenta o gate determinístico/Revisor — nunca
                aprova/reprova por juízo de LLM isolado
  PORQUE:       Não-fabricação é obrigatória (RULE-MET-01); Detector ≠ Gate (ENF-03)
  REFERÊNCIA:   RULE-EV-03; RULE-MET-01; ENF-03; [EXTERNO] research.md E3/E4/E9
  VERIFICADO POR:
    DADO        Spec-filha cita "RULE-XYZ" inexistente no RULES.md
    QUANDO      o detector de alucinação sinaliza a referência
    ENTÃO       sinal registrado; gate determinístico (existência no RULES.md) reprova
    VERIFICAÇÃO o veredito vem do gate determinístico, não do LLM; sinal é insumo, não decisão
```

### BASpec-EV-004 — Lente 4: Role adherence

```
BASpec-EV-004:
  QUANDO:       Uma Spec-filha atribui responsabilidade a um agente/componente
  ENTÃO:        Harness Evaluation verifica aderência à hierarquia (Elliott→Fibonacci→Fractal→SMC→ICT)
                e ao escopo por agente; atribuição fora do domínio (ex.: ICT criando hipótese) = reprovação
  PORQUE:       PC-01/CC-01 são invariantes; princípio de topo sobrepõe instrução de tarefa
                (aderência hierárquica sob conflito)
  REFERÊNCIA:   RULE-EV-01; CC-01; RULE-ICT-007; [EXTERNO] research.md E6/E10
  VERIFICADO POR:
    DADO        Spec-filha do ICT que cria hipótese estrutural
    QUANDO      Harness Evaluation aplica a lente role adherence
    ENTÃO       lente = REPROVADA, código "ROLE_HIERARCHY_VIOLATION"
    VERIFICAÇÃO violação de CC-01 identificada; gate não passa
```

### BASpec-EV-005 — Lente 5: Context management

```
BASpec-EV-005:
  QUANDO:       Uma Spec-filha descreve uso de contexto/estado ao longo de uma trajetória cognitiva
  ENTÃO:        Harness Evaluation avalia integridade de contexto sobre a TRAJETÓRIA (não só ponto):
                sem perda/contaminação/duplicação silenciosa de contexto entre etapas
  PORQUE:       Avaliação sobre a trajetória de contexto é critério de integridade; SPEC-043 detalha
                o slot downstream (só o critério é fixado aqui)
  REFERÊNCIA:   RULE-EV-01; RULE-CEE-003; [EXTERNO] research.md E5/E8/E11
  VERIFICADO POR:
    DADO        Spec-filha que reusa estado obsoleto sem revalidação
    QUANDO      Harness Evaluation aplica a lente context management
    ENTÃO       lente = REPROVADA, código "CONTEXT_INTEGRITY_BREACH"
    VERIFICAÇÃO ponto de contaminação/obsolescência identificado na trajetória
```

### BASpec-EV-006 — Lente 6: Safety

```
BASpec-EV-006:
  QUANDO:       Uma Spec-filha descreve comportamento com efeito ou exposição a ameaça
  ENTÃO:        Harness Evaluation verifica que as 5+5 Salvaguardas (CEE-001 §10/§11) e os PC-xx são
                respeitados e PREVALECEM sobre catálogos externos; alta aderência sem competência de
                tarefa (illusion of compliance) => registrar INDETERMINADO e encaminhar ao adversarial
  PORQUE:       Salvaguardas invioláveis prevalecem (RULE-EV-07); a literatura alerta para
                "illusion of compliance" (E6) — não mascarar incompetência por aderência formal
  REFERÊNCIA:   RULE-EV-07; CEE-001 §10/§11; INV-04; [EXTERNO] research.md E1/E2/E6
  VERIFICADO POR:
    DADO        Spec-filha que atende formalmente a safety mas não demonstra competência de tarefa
    QUANDO      Harness Evaluation aplica a lente safety
    ENTÃO       lente = INDETERMINADO, código "COMPLIANCE_ILLUSION_SUSPECT"; encaminha ao adversarial
    VERIFICAÇÃO estado INDETERMINADO registrado; caso enviado a D8 (não força PASS/FAIL)
```

### BASpec-EV-007 — Lente 7: Regression

```
BASpec-EV-007:
  QUANDO:       Um achado adversarial revela falha constitutiva numa Spec-filha
  ENTÃO:        Harness Evaluation exige conversão do achado em caso de regressão VERSIONADO,
                referenciável em checks.md/CI, preservado (nunca deletado)
  PORQUE:       Casos de regressão preservam a memória de falhas (INV-07); casa com o pipeline
                D8→checks.md→CI (F.3 Feedback)
  REFERÊNCIA:   RULE-EV-04; INV-07; atomic-spec §5 (F.3); [EXTERNO] research.md E11/E13
  VERIFICADO POR:
    DADO        Achado adversarial ADV-XX numa Spec-filha, sem caso de regressão correspondente
    QUANDO      Harness Evaluation aplica a lente regression
    ENTÃO       lente = REPROVADA, código "REGRESSION_CASE_MISSING"
    VERIFICAÇÃO ausência do caso versionado identificada; exige registro antes de avançar
```

### BASpec-EV-008 — Lente 8: Robustness / adversarial (como método)

```
BASpec-EV-008:
  QUANDO:       Uma Spec-filha HIGH/CRITICAL é avaliada quanto a robustez
  ENTÃO:        Harness Evaluation exige que o método adversarial (D8 + §7-bis do Especificador +
                Passo 5-bis do Revisor) tenha sido aplicado — casos de negação por BASpec crítica;
                a SPEC-020 fixa o MÉTODO de avaliar robustez, não os casos (SPEC-022 os produz)
  PORQUE:       Robustez é disciplina de método (casos de negação); evita duplicar SPEC-022
  REFERÊNCIA:   RULE-EV-01; atomic-spec §2 (D8); especificador §7-bis; [EXTERNO] research.md E2/E11/E12
  VERIFICADO POR:
    DADO        Spec-filha CRITICAL sem seção D8/§7-bis preenchida
    QUANDO      Harness Evaluation aplica a lente robustness
    ENTÃO       lente = REPROVADA, código "ADVERSARIAL_METHOD_ABSENT"
    VERIFICAÇÃO ausência de método adversarial identificada; gate não passa
```

### BASpec-EV-009 — Lente 9: Principle consistency (SPEC-020-PRINC-001)

```
BASpec-EV-009:
  QUANDO:       Uma Spec-filha é avaliada quanto a consistência principiológica
  ENTÃO:        Harness Evaluation aplica o checklist do GPR-001 §15 como itens verificáveis;
                contradição com princípio PC-xx = REPROVAÇÃO; conflito com PB-xx = registrar e
                justificar a ponderação (PB-06); operacionaliza precedência/conflito (GPR-001 §3.2/§6)
  PORQUE:       O GPR-001 §15 hoje é declarativo (L0–L1); SPEC-020-PRINC-001 o torna critério
                constitutivo verificável de spec-time
  REFERÊNCIA:   RULE-EV-06; GPR-001 §14/§15/§6; ROADMAP §12 (SPEC-020-PRINC-001)
  VERIFICADO POR:
    DADO        Spec-filha cujo comportamento contradiz PC-02 (SOT não executa ordem)
    QUANDO      Harness Evaluation aplica a lente principle consistency
    ENTÃO       lente = REPROVADA, código "PRINCIPLE_CONTRADICTION (PC-02)"
    VERIFICAÇÃO item do checklist §15 marcado como violado; gate não passa
```

---

## D4 — Algoritmo

**N/A como fórmula numérica.** A avaliação constitutiva é **qualitativa** (Q-A4): não há regra determinística numérica de agregação de "score de avaliação" — fixá-la dependeria de limiares ligados a convicção (J-001, aberto — RULE-EV-05). O que existe é um **procedimento** determinístico de aplicação de lentes (ver D6 — Protocolo). A omissão de D4 numérico é **justificada**: introduzir escore numérico agora violaria CONS-01/INV-03. [FONTE: J-001; atomic-spec §2 (D4 "onde há regra determinística real")]

---

## D5 — Máquina de estados da avaliação de uma lente

A avaliação de cada lente sobre uma Spec-filha percorre estados explícitos:

| Estado | Significado |
|---|---|
| NOT_EVALUATED | Lente ainda não aplicada à Spec-filha |
| DETECTED | Detector (semântico/LLM) produziu sinal — **insumo, não veredito** (ENF-03) |
| PASS | Gate determinístico/Revisor confirmou conformidade da lente |
| FAIL | Gate determinístico/Revisor confirmou não-conformidade (reprovação) |
| INDETERMINADO | Incerteza material (ex.: illusion of compliance) — não força PASS/FAIL; encaminha ao adversarial |
| REGRESSED | Achado convertido em caso de regressão versionado (INV-07) |

### Transições

```
NOT_EVALUATED -> DETECTED        (detector semântico roda; sinal produzido)
DETECTED       -> PASS           (gate determinístico/Revisor confirma conformidade)
DETECTED       -> FAIL           (gate determinístico/Revisor confirma violação)
DETECTED       -> INDETERMINADO  (incerteza material; encaminha a D8/adversarial)
INDETERMINADO  -> PASS | FAIL     (após avaliação adversarial resolver a incerteza)
FAIL           -> REGRESSED       (achado versionado como caso de regressão — RULE-EV-04)
```

**Invariante de estado (ENF-03):** o estado nunca transita de DETECTED direto a PASS/FAIL **por juízo do LLM** — a transição é do gate determinístico e/ou da homologação de Andraus. DETECTED é sinal, não decisão.

---

## D6 — Protocolo de avaliação (acoplamento ao Constitution Check / checks.md)

Sequência canônica de avaliação de uma Spec-filha (SPEC-002+) — acoplada ao gate de spec-time da SPEC-019 (RULE-HG-06):

```
1. Especificador redige a Spec-filha (plan.md) + checks.md; aplica §7-bis (HIGH/CRITICAL).
2. As 9 lentes (L-CORR..L-PRIN) são avaliadas como itens de checks.md / Constitution Check estendido.
3. Para cada lente: DETECTOR semântico (LLM) roda → produz sinal (estado DETECTED).
4. GATE determinístico aplica os checks estruturais/objetivos (existência de RULE, presença de
   VERIFICADO POR, existência de artefato, presença de D8/§7-bis, checklist GPR-001 §15) → PASS/FAIL.
5. Incerteza material (ex.: illusion of compliance) → INDETERMINADO; encaminha ao adversarial (D8).
6. Achado de FAIL adversarial → caso de regressão versionado (REGRESSED; RULE-EV-04; INV-07).
7. Revisor (GRE-001/HRE-001) audita o resultado das lentes como parte do parecer (detector, não gate).
8. Andraus homologa a Spec-filha (única autoridade de vigência — RULE-HG-03). A avaliação NÃO homologa.
```

O acoplamento **não cria autoridade nova**: reutiliza o gate RULE-HG-06 (Constitution Check antes do Plan e da homologação), estendendo os **itens** avaliados. [FONTE: RULE-HG-06; Q-A3]

---

## D7 — Cenários de Teste

### Cenário-EV-T01 — Detector não é gate (ENF-03)

```
DADO        detector semântico sinaliza possível alucinação numa Spec-filha
QUANDO      o resultado da avaliação é computado
ENTÃO       o veredito PASS/FAIL vem do gate determinístico/Revisor, não do LLM
VERIFICAÇÃO log mostra estado DETECTED → (gate determinístico) → FAIL; LLM não decidiu
```

### Cenário-EV-T02 — Role adherence bloqueia ICT criando hipótese

```
DADO        Spec-filha do ICT que cria hipótese estrutural
QUANDO      Harness Evaluation aplica a lente role adherence
ENTÃO       lente = FAIL, "ROLE_HIERARCHY_VIOLATION" (CC-01 / RULE-ICT-007)
VERIFICAÇÃO gate de spec-time não passa; violação de hierarquia registrada
```

### Cenário-EV-T03 — Achado adversarial vira regressão versionada

```
DADO        achado adversarial ADV-X revela falha constitutiva; sem caso de regressão
QUANDO      Harness Evaluation aplica a lente regression
ENTÃO       exige caso versionado; estado FAIL → REGRESSED após registro (INV-07)
VERIFICAÇÃO caso de regressão presente em checks.md/CI; nada deletado
```

### Cenário-EV-T04 — Principle consistency reprova contradição com PC-xx

```
DADO        Spec-filha cujo comportamento contradiz PC-02 (SOT não executa ordem)
QUANDO      Harness Evaluation aplica a lente principle consistency (GPR-001 §15)
ENTÃO       lente = FAIL, "PRINCIPLE_CONTRADICTION (PC-02)"
VERIFICAÇÃO item do checklist §15 marcado violado; gate não passa
```

### Cenário-EV-T05 — Limiar numérico dependente de convicção é rejeitado

```
DADO        Spec-filha tenta fixar "aprovação se convicção-de-avaliação ≥ N%"
QUANDO      Harness Evaluation aplica RULE-EV-05
ENTÃO       fechamento rejeitado; critério mantido qualitativo (J-001 aberto)
VERIFICAÇÃO nenhum limiar numérico ligado a convicção fixado; CONS-01 preservado
```

---

## D8 — Cenários Adversariais [casos de negação — CRITICAL]

Princípio transversal: **fail-closed** — em qualquer ambiguidade sobre autoridade de veredito, o Harness Evaluation NÃO aprova a Spec-filha e retorna estado/código específico.

### ADV-EV-01 — LLM-as-Judge usado como gate de aprovação
**DADO:** proposta de usar o detector LLM como portão de aprovação de uma Spec-filha
**QUANDO:** a avaliação é configurada
**ENTÃO:** rejeitar (fail-closed) `LLM_JUDGE_AS_GATE_FORBIDDEN`; LLM permanece detector; gate determinístico/Andraus decide
**PORQUE:** Detector ≠ Gate; o LLM nunca é seu próprio gate (ENF-03; RULE-EV-02)
**VERIFICAÇÃO:** configuração recusada; veredito atribuído a gate determinístico/Revisor/Andraus

### ADV-EV-02 — Illusion of compliance (aderência mascara incompetência)
**DADO:** Spec-filha com alta aderência formal a safety e baixa competência de tarefa
**QUANDO:** a lente safety é aplicada
**ENTÃO:** estado INDETERMINADO `COMPLIANCE_ILLUSION_SUSPECT`; encaminha ao adversarial; não força PASS
**PORQUE:** "illusion of compliance" é problema aberto (E6, INDETERMINADO — GAP-1); não fabricar métrica (RULE-MET-01)
**VERIFICAÇÃO:** INDETERMINADO registrado; caso enviado a D8; nenhuma aprovação automática

### ADV-EV-03 — Catálogo externo tenta sobrepor Salvaguarda Constitucional
**DADO:** regra OWASP/NIST que conflita com uma Salvaguarda CEE-001 §11
**QUANDO:** a lente safety pondera as fontes
**ENTÃO:** Salvaguarda PREVALECE; catálogo externo tratado como subordinado (`EXTERNAL_SUBORDINATE`)
**PORQUE:** Salvaguardas invioláveis; referência externa nunca é baseline (RULE-EV-07; INV-04; research.md §4)
**VERIFICAÇÃO:** decisão registra prevalência da Salvaguarda; rótulo externo não adotado

### ADV-EV-04 — Ladder de maturidade externo contrabandeado para o núcleo A
**DADO:** proposta de usar janelas NIST / ladder de fornecedor como critério da SPEC-020
**QUANDO:** a avaliação é definida
**ENTÃO:** rejeitar `MATURITY_OUT_OF_SCOPE`; maturidade pertence à SPEC-021, não ao núcleo A
**PORQUE:** colisão com Quality Gates L1–L4/harness-score/GPR L0–L5 (research.md §4 CONFLITO-2); rótulos rejeitados
**VERIFICAÇÃO:** critério de maturidade não entra no núcleo A; encaminhado a SPEC-021

### ADV-EV-05 — "Task completion" imposto como métrica primária
**DADO:** proposta de avaliar Spec-filha por conclusão de tarefa/execução bem-sucedida
**QUANDO:** a lente correctness é definida
**ENTÃO:** rejeitar `EXECUTION_METRIC_FORBIDDEN`; adaptar para "qualidade de análise/decisão"
**PORQUE:** SOT não executa (INV-05/PC-02) e prioriza Conformidade > Eficácia (4Es); research.md §4 CONFLITO-3
**VERIFICAÇÃO:** métrica de execução recusada; critério ancorado em qualidade de análise

### ADV-EV-06 — Dimensão classe B tratada como fechada antes do componente-alvo
**DADO:** tentativa de fechar RAG faithfulness / tool correctness / decision traceability na SPEC-020
**QUANDO:** o escopo é avaliado
**ENTÃO:** rejeitar `CLASS_B_PREMATURE`; classe B permanece DIFERIDA (SPEC-007/038/014; BL-017)
**PORQUE:** CONS-01 — dimensões B não fechadas antes do componente-alvo (ROADMAP §12; Q-A5)
**VERIFICAÇÃO:** classe B não fechada; BL-017 intocado

### ADV-EV-07 — Limiar numérico de convicção embutido na avaliação
**DADO:** tentativa de fixar limiar numérico de aprovação dependente de convicção
**QUANDO:** RULE-EV-05 é aplicada
**ENTÃO:** rejeitar `CONVICTION_THRESHOLD_LOCKED_FORBIDDEN`; manter qualitativo (J-001 aberto)
**PORQUE:** J-001 em aberto; fórmula/pesos/limiares não podem ser invariante fechado (INV-03/CONS-01)
**VERIFICAÇÃO:** nenhum limiar de convicção fixado; J-001 preservado como aberto

> **Cobertura:** 7 cenários adversariais (mínimo para CRITICAL cumprido; casos de negação das lentes e das fronteiras homologadas).

---

## D9 — Auditabilidade (por referência)

Cada avaliação de lente DEVE ser reconstruível: entrada (Spec-filha + versão), lente, estado (DETECTED/PASS/FAIL/INDETERMINADO/REGRESSED), veredito e autoridade do veredito (gate determinístico/Revisor/Andraus), código de achado. Reconstrução completa (D9) pertence a **SPEC-041** (Cognitive Audit); aqui fica **por referência** (coerente com alvo D0–D8). [FONTE: atomic-spec §2 (D9); CONSTITUTION P13]

---

## I/O Schemas (lógicos)

### Resultado de avaliação de lente — schema lógico
```json
{
  "spec_filha": "SPEC-0xx vX.Y",
  "lente": "correctness | grounding | hallucination | role_adherence | context_management | safety | regression | robustness | principle_consistency",
  "estado": "NOT_EVALUATED | DETECTED | PASS | FAIL | INDETERMINADO | REGRESSED",
  "detector_signal": "<sinal semântico — insumo, não veredito>",
  "veredito_por": "gate_deterministico | revisor | andraus",
  "codigo_achado": "<ex.: ROLE_HIERARCHY_VIOLATION | UNGROUNDED_CLAIM | ...>",
  "caso_regressao_ref": "<id do caso versionado, se REGRESSED>",
  "preserva_historico": true
}
```

---

## Enforcement Contracts

### EC-EV-001 — Aplicação das 9 lentes como gate de spec-time

```
CAPABILITY   : Avaliar uma Spec-filha (SPEC-002+) pelas 9 lentes e condicionar sua elegibilidade
               à homologação (gate de spec-time acoplado ao Constitution Check / RULE-HG-06)
EFFECT       : Bloqueia a elegibilidade à homologação da Spec-filha quando uma lente crítica FALHA
               (efeito sobre o processo de governança — publicação do veredito em checks.md/gate)
PRECOND      : (as 9 lentes foram aplicadas) AND (gate determinístico executado) AND
               (detector semântico usado apenas como sinal, não como veredito — ENF-03)
POSTCOND     : Spec-filha só elegível a homologação se nenhuma lente crítica está em FAIL;
               INDETERMINADO encaminhado ao adversarial; nada é homologado pela avaliação
POLICY       : RULE-EV-01/02; RULE-HG-06; ENF-03; INV-09
LEVEL        : E3 (Crítico — condiciona efeito normativo de governança sobre a Spec-filha)
FAILURE-MODE : Fail-closed — ambiguidade sobre autoridade de veredito ⇒ não aprova; Spec-filha
               permanece inelegível; log de rejeição
EVIDENCE     : Relatório por lente (schema I/O); entrada em checks.md; parecer do Revisor
             + método de observação de falso-DENY: amostragem de Specs-filhas reprovadas por
               "lente FAIL" que de fato satisfaziam o critério (limiar = gap aberto, ENF-07)
```

### EC-EV-002 — Detector semântico (LLM) como sinal, nunca gate

```
CAPABILITY   : Produzir sinal semântico de violação (alucinação, grounding, aderência) via LLM
EFFECT       : Emite sinal (estado DETECTED) que alimenta o gate determinístico/Revisor
PRECOND      : (o sinal é rotulado como insumo, não veredito) AND (existe gate determinístico a jusante)
POSTCOND     : Nenhuma aprovação/reprovação decorre isoladamente do LLM (ENF-03)
POLICY       : RULE-EV-02/03; ENF-03; RULE-MET-01
LEVEL        : E2 (Operacional — produz estado/insumo; sem efeito normativo próprio)
FAILURE-MODE : Fail-closed — se não houver gate determinístico a jusante, o sinal NÃO produz veredito
EVIDENCE     : Log de estado DETECTED distinto do veredito PASS/FAIL; rastreabilidade detector→gate
```

### EC-EV-003 — Conversão de achado adversarial em regressão versionada

```
CAPABILITY   : Registrar achado constitutivo como caso de regressão versionado
EFFECT       : Cria caso de regressão referenciável (checks.md/CI), preservado
PRECOND      : (achado adversarial de FAIL) AND (caso versionado com ID monotônico)
POSTCOND     : Caso de regressão preservado; estado da lente = REGRESSED; nada deletado (INV-07)
POLICY       : RULE-EV-04; INV-07
LEVEL        : E2 (Operacional — estado/preservação; sem efeito normativo de vigência)
FAILURE-MODE : Fail-closed — sem caso versionado registrado, a lente regression permanece FAIL
EVIDENCE     : Caso de regressão em checks.md/CI; histórico intacto (INV-07)
```

### EC-EV-004 — Gate de consistência principiológica (SPEC-020-PRINC-001)

```
CAPABILITY   : Verificar a Spec-filha contra o checklist GPR-001 §15 (precedência/conflito de princípios)
EFFECT       : Bloqueia elegibilidade à homologação quando há contradição com princípio PC-xx
PRECOND      : (checklist §15 aplicado item a item) AND (conflitos PB-xx registrados e justificados — PB-06)
POSTCOND     : Contradição com PC-xx ⇒ FAIL; conflito PB-xx ⇒ registrado com ponderação explicável
POLICY       : RULE-EV-06; GPR-001 §14/§15/§6; ENF-03
LEVEL        : E3 (Crítico — condiciona efeito normativo; princípios constitucionais)
FAILURE-MODE : Fail-closed — contradição PC-xx não resolvida ⇒ Spec-filha inelegível
EVIDENCE     : Checklist §15 preenchido por Spec-filha; registro de conflito PB-xx + ponderação
             + método de observação de falso-DENY amostral (ENF-07 — gap aberto)
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
O Harness Evaluation (núcleo A) é um **meta-harness de avaliação spec-time** (F.4 Evaluation, atomic-spec §5), executado durante a produção de cada Spec-filha por: Especificador (aplica lentes em checks.md), gate determinístico (`validate_spec_sot.py` estendido — via BL-021, sujeito a aprovação própria), Revisor (audita as lentes, detector), Andraus (homologa). Não é componente cognitivo de runtime. [FONTE: atomic-spec §5; Q-A3]

### Roteamento de modelo (CEE-001 §5 / EUA-E19)
**N/A como chamada de LLM de runtime** — a SPEC-020 não descreve agente cognitivo que roteia por Tipo I–V. Onde o detector semântico é apoiado por LLM, é **detector**, não gate (ENF-03); o roteamento dos agentes de processo é governado por suas configs (EUA-E19), fora do escopo. [FONTE: EUA-E19; ENF-03]

### Dependências técnicas
atomic-spec v1.4 · SPEC-019 v1.0 (RULE-HG-06 gate) · SPEC-001 v1.1 (hypothesis consistency) · GPR-001 v1.0 (§15) · RULES.md v1.1 (ENF-*, RULE-HG-*, RULE-ICT-007) · CEE-001 v2.0 (§10/§11) · CEM-001/CHM-001 (idioma). Referências externas [EXTERNO], não-baseline: research.md §2 (E1–E13).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| LLM-as-Judge vira gate (colisão ENF-03) | RULE-EV-02/03; ENF-03; ADV-EV-01; EC-EV-002 fail-closed |
| Fixar limiar de convicção (fere J-001) | RULE-EV-05; ADV-EV-07; CONS-01 |
| Classe B tratada como fechada | Non-goal explícito; ADV-EV-06; BL-017 intocado |
| Catálogo externo sobrepõe Salvaguarda | RULE-EV-07; ADV-EV-03; INV-04 |
| Maturidade contrabandeada ao núcleo A | Non-goal; ADV-EV-04; SPEC-021 |
| Illusion of compliance mascarar incompetência | BASpec-EV-006 INDETERMINADO; ADV-EV-02; GAP-1 |
| Antecipar SPEC-045-RUNTIME-001 | Non-goal; tooling de runtime fora de escopo (Q-A3) |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz schema lógico "resultado de avaliação de lente" (I/O acima); nenhum schema de runtime alterado.
- **RAG:** nenhum; a avaliação não escreve no KG/RAG.
- **Skills:** nenhuma Skill afetada.
- **Testes:** adiciona itens de lente ao `checks.md` de cada Spec-filha; propõe extensão de `validate_spec_sot.py` (via BL-021, aprovação própria).
- **Modelos dependentes:** SPEC-019/SPEC-001/GPR-001 não alterados (construção SOBRE / acoplamento).
- **Compatibilidade:** **Minor** — adiciona comportamento (RULE-EV + lentes) acoplado ao gate existente RULE-HG-06, sem invalidar comportamento vigente; nenhuma RULE existente redefinida.

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07).

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — pergunta adversarial por BASpec CRITICAL/HIGH (as 9 lentes):**
- **EV-003 (hallucination):** se errada, observável = LLM aprovando/reprovando sozinho → detectável pela ausência de estado DETECTED distinto do veredito. ENTÃO verificável por observador independente (log detector→gate). Negação: ADV-EV-01. Condição QUANDO-satisfeito-mas-ENTÃO-não-deve: detector sinaliza mas a referência de fato existe → gate determinístico confirma PASS (tratado: veredito é do gate, não do detector).
- **EV-004 (role adherence):** se errada, observável = ICT criando hipótese homologado → detectável por violação de CC-01/RULE-ICT-007. Negação: ADV-EV-05 + Cenário-EV-T02.
- **EV-006 (safety):** se errada, observável = aderência formal mascarando incompetência → INDETERMINADO em vez de PASS forçado. Negação: ADV-EV-02 (illusion of compliance).
- **EV-009 (principle consistency):** se errada, observável = Spec-filha contradizendo PC-xx e sendo aprovada → detectável pelo checklist §15. Negação: Cenário-EV-T04 + ADV (PC-02).
- **EV-007 (regression):** se errada, observável = achado adversarial perdido (não versionado) → detectável por ausência do caso em checks.md. Negação: Cenário-EV-T03; INV-07 impede deleção.

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista atomic-spec v1.4, SPEC-019 v1.0, SPEC-001 v1.1, GPR-001 v1.0, ENF-01..08, INV-04/05/07/09/10, CEM/CHM (ID+versão — RULE-HD-04). Evidência de satisfação por obrigação herdada: RULE-EV-02/03 ancora a ENF-03; RULE-EV-04 ancora a INV-07; RULE-EV-01/D6 ancora a RULE-HG-06 (gate); RULE-EV-06 ancora a GPR-001 §15; RULE-EV-07 ancora a INV-04/CEE-001; a lente role adherence ancora a CC-01/RULE-ICT-007; grounding ancora a INV-10/CEM-001. Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (MODIFIED apenas estende os *itens* do gate RULE-HG-06, sem alterar seu texto). **Eixo VERTICAL (RULE-HV) declarado não aplicável** (SPEC-020 é irmã, não filha de SPEC-019) — evita a confusão que o próprio ADV-HV-07 da SPEC-019 alerta.

**Bloco C — epistêmico (RULE-EPI/CAU/PRB):** nenhuma afirmação causal forte sem mecanismo (as lentes descrevem critérios, não causalidade de mercado); nenhuma hipótese tratada como fato (fontes externas [EXTERNO] = DADO); INDETERMINADO usado (GAP-1 illusion of compliance; GAP-2 limiares) em vez de forçar PASS/FAIL; nenhuma probabilidade/precisão numérica declarada sem base (D4 numérico N/A justificado; J-001 aberto).

**Bloco D — reforço de escopo:** a Spec produz **avaliação** (detecção/veredito de conformidade), não executa runtime nem emite ordem — INV-05/PC-02/RULE-DEC reconfirmados (§7). Nenhuma lente cruza a fronteira SOT→execução downstream (a lente correctness rejeita "task completion/execução" — ADV-EV-05). Dependências de Andraus (SPEC-020-PRINC-001; homologação de Spec-filha) marcadas como decisão de homologação, não como fato consumado; J-001 e classe B marcados [DECISÃO NECESSÁRIA]/DIFERIDO, não fechados.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| atomic-spec v1.4; ENF-01..08; INV-04/05/07/09/10 | [FONTE] | FATO NORMATIVO |
| SPEC-019 v1.0 (RULE-HG-06 gate); SPEC-001 v1.1; GPR-001 v1.0 (§15) | [FONTE] | FATO NORMATIVO (baseline) |
| CEE-001 §10/§11; CEM-001; CHM-001 | [FONTE] | FATO NORMATIVO (baseline) |
| 9 lentes; RULE-EV-01..07; EC-EV-001..004 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| SPEC-020-PRINC-001 (operacionalização §15) | [DECISÃO NECESSÁRIA] | Efetiva-se na homologação da SPEC-020 (não fechada aqui — CONS-01) |
| Fontes de eval E1–E13 (NIST, OWASP, arXiv, fornecedores) | [EXTERNO] | Referência — DADO, nunca baseline (research.md §2) |
| J-001 (limiares definitivos) | [DECISÃO NECESSÁRIA] | Aberto — não tocado (RULE-EV-05) |
| Classe B (RAG faithfulness/tool correctness/decision traceability) | [FONTE] | DIFERIDA (BL-017) — não fechada |
| GAP-1 (illusion of compliance); GAP-2 (limiares) | [INFERÊNCIA/EXTERNO] | INDETERMINADO (não fabricar métrica) |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-020 núcleo A confirmada como próximo autorizado (§12/§21/§25); FASE GOV posição 2.
[x] atomic-spec.md lido: método v1.4 confirmado (v1.5 não homologada; DHR-EUA-E17 §3).
[x] Nenhum invariante congelado violado (INV-01..10). INV-05 reforçado (avaliação ≠ execução, RULE-DEC).
[x] Constitution Check CC-01..CC-10 preenchido (N/A justificados em CC-06/07/10).
[x] Disciplinas N8–N17: RULE-EPI (INDETERMINADO em GAP-1/2), RULE-MET-01 (não-fabricação), RULE-DEC (detecção≠homologação), RULE-CAU/UNC.
[x] Referências externas [EXTERNO] classificadas (research.md §2); rótulos rejeitados (LLM-as-Judge-gate, ladders NIST/OWASP) não adotados; nada vira baseline.
[x] Spec sem implementação; Plan derivado; Tasks adiadas (spec-first).
[x] Critérios em EARS (9); BASpecs completas (EV-001..009, as 9 lentes); RULEs citadas existentes (ENF-03, RULE-HG-06, RULE-ICT-007, INV-*) x propostas (RULE-EV) claramente etiquetadas.
[x] Profundidade D0–D8 atingida (D5 estados; D6 protocolo; D7 cenários x5; D8 adversarial x7; D9 por referência).
[x] Enforcement Contract em todo ato com efeito (EC-EV-001..004); níveis E2/E3; fail-closed; ENF-07 amostral declarado nos E3.
[x] Status epistemológico aplicado (FATO NORMATIVO vs PROPOSTA vs EXTERNO vs DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: J-001 permanece aberta (não fixada); SPEC-020-PRINC-001 permanece aberta (efetiva na homologação); classe B DIFERIDA; nenhuma decisão aberta usada como invariante.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos registrados (research.md §4 CONFLITO-1/2/3; GAP-1/2) — não resolvidos em silêncio.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE/EC fabricada como vigente; sem baseline informal.
[x] 4Es na ordem; Conformidade > Eficácia (safety/PC-xx prevalecem sobre eval externo). Latência N/A (avaliação spec-time).
[x] Dependências a montante homologadas (atomic-spec/SPEC-019/SPEC-001/GPR-001/RULES/CEE-001); não downstream de bloqueador aberto (J-001 é adiado, não bloqueia o núcleo qualitativo).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D) — obrigatório CRITICAL.
[x] Abertura (RULE-ECC-01/02): Dossiê presente e HOMOLOGADO (research.md §8, 2026-09-27); escopo/quantidade/número definidos e homologados; Spec não iniciada só por posição — abertura cumprida.
[x] Passo 11-bis: BL-021 ATIVADO (spec:SPEC-020 em redação) tratado (nota de gate; tooling, aprovação própria); BL-017 não dispara; BL-020 não dispara; BL-008 independente.
[ ] Gate determinístico (validate_spec_sot.py) e build_map.py: a rodar no ambiente pai (sem Bash Python confirmado aqui) — reportado ao caller.
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] em aberto nesta Spec (não fechadas — CONS-01):
- **SPEC-020-PRINC-001** — operacionalização do GPR-001 §15 como lente L-PRIN; **efetiva-se na homologação da SPEC-020** (Q-A2 homologou a forma "9ª lente própria"; a efetivação é da homologação, não desta redação).
- **J-001** — permanece **aberto/pendente**; limiares definitivos do Conviction Vector; a Spec é qualitativa e **não** os fixa (RULE-EV-05).
- **Classe B** (RAG faithfulness / tool correctness / decision traceability) — DIFERIDA (BL-017); fecha em SPEC-007/038/014.
- **ECC-VAL-001** como **regra geral** — resolvida só para esta Spec (Q-A6: 30 dias / início do Plan); regra geral permanece aberta.

Carregado do Dossiê para o Revisor:
- **ACH-001** — achado Menor não bloqueante do parecer do Revisor sobre o research.md (registrado em research.md §6/§8); a ser reconfirmado/tratado pelo Revisor na auditoria desta entrega.
