# SPEC-021 — Harness Score / Maturity Model

| Campo | Valor |
|---|---|
| ID | SPEC-021 — Harness Score / Maturity Model (escada de maturidade canônica por-Spec) |
| Versão | 1.0 (candidata) |
| Status | **HOMOLOGADA — BASELINE** (Andraus, 2026-09-28, DHR-SPEC021-001; compat. Minor). |
| Fonte | ROADMAP §12/§21/§25; `research.md` (Dossiê de abertura HOMOLOGADO 2026-09-28, §7-bis); atomic-spec v1.4 §7; RULE-ECC-01/02 |
| Complexidade | **HIGH** |
| Profundidade-alvo | **D0–D7** (standard) |
| Profile (Claude Code) | standard (HIGH) — §7-bis aplicado (obrigatório HIGH), fornece ≥1 caso adversarial (D8) |
| Posição no caminho crítico | FASE GOV (cont.), posição 3 — após SPEC-020 núcleo A (HOMOLOGADA), antes de SPEC-002 [FONTE: ROADMAP §12/§21] |
| Nível de maturidade-alvo (desta Spec) | **L3 Testável** — D5 + ≥3 cenários D7 + ≥1 adversarial D8 + revisão independente [FONTE: atomic-spec §7] |
| Método | atomic-spec.md **v1.4** (v1.5 não homologada; DHR-EUA-E17 §3 fixa v1.4 para a FASE GOV) |
| Regime normativo citado | **RULE-ECC-01/02** (Especificação Emergente), **RULE-MECH-01..04** (Classe/Mecanismo — incide, Q-A5), **RULE-HG-06** (Constitution Check como gate) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-09-28 |
| Abertura | Dossiê de Pesquisa homologado por Andraus em **2026-09-28** (research.md §7-bis; RULE-ECC-01/02) — Plan iniciado no mesmo dia, dentro da validade do Dossiê (ECC-VAL-001, Q-A6: 30 dias / início do Plan) |

Status: **HOMOLOGADA — BASELINE** (Andraus, 2026-09-28, DHR-SPEC021-001; compat. Minor). Complexidade: HIGH. Profundidade-alvo: D0–D7 (standard). [FONTE: ROADMAP §12; AGENTS.md §4]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-09-28 | Entrega candidata inicial. Escada de maturidade canônica por-Spec L0–L4 (Q-A2). Gate normativo E3 (Q-A3). Classe por BASpec (RULE-MECH-01/CC-11). D0–D7 + §7-bis. |

---

## Nota de gate (passo 11-bis / RMR-001) — itens verificados nesta redação

[FONTE: RMR-001 §6; ROADMAP §23 passo 11-bis]

O início da redação deste Plan **não dispara** nenhum gatilho novo de ativação registrado no RMR-001 (não há item com gatilho `spec:SPEC-021 em redação`). Estado dos itens relevantes:

- **BL-020** — "Reavaliar acesso web só-leitura do Revisor" — `ATIVADO` desde 2026-09-27 (gatilho `spec:SPEC-020 homologada`, DHR-SPEC020-001). Encaminhamento **pendente de decisão de Andraus**; é **independente desta abertura** e **não bloqueia** a SPEC-021. Registrado. [FONTE: RMR-001 §6 BL-020]
- **BL-021** — "Adaptar ferramental à EUA-E21" — **Absorvido** (2026-09-27, DHR-SPEC020-001). O check determinístico `[STRUCT-11] Dossiê de Pesquisa presente` (`validate_spec_sot.py`) incide sobre Specs que citam RULE-ECC-01/02 — a SPEC-021 as cita; `research.md` está presente na pasta. Sem ação nova. [FONTE: RMR-001 §6 BL-021]
- **BL-017** — "Fechamento das dimensões classe B da SPEC-020" — gatilho `spec:SPEC-007/014/038 em redação`: **NÃO inclui SPEC-021** → não dispara; permanece `Proposto`. Classe B permanece DIFERIDA (Non-goal). [FONTE: RMR-001 §6 BL-017]
- **BL-008** — auditoria retroativa da SPEC-001 — segue `ATIVADO`, independente desta redação. [FONTE: RMR-001 §6 BL-008]
- **BL-022 / BL-023** (PRINC-BID-001 / CLASSE-MECH-001) — **Absorvidos** (2026-09-27); RULE-PD-01..03 e RULE-MECH-01..04 já vigentes e incidem sobre esta Spec (ver Constitution Check CC-11/CC-12).

Nenhum item `ATIVADO` fica sem encaminhamento por conta desta redação. [INFERÊNCIA — coerente com RMR-001 §4]

---

## Constitution Check (CC-01..CC-12 — atomic-spec §10.5 + emendas EUA-E04..E14 / CLASSE-MECH-001 / PRINC-BID-001)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** a SPEC-021 é meta-harness de **medição de maturidade de specs**; não computa análise técnica de mercado nem inverte a hierarquia. Ao contrário, o critério de nível L1+ **consome** o resultado da lente `role adherence` da SPEC-020 (que protege a hierarquia). A maturidade **protege** CC-01; não o toca. [INFERÊNCIA]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** nenhuma parte redefine modelo canônico. Também **não redefine** as escadas herdadas: as Quality Gates L1–L4 (atomic-spec §7) são reusadas como **tabela de critérios**; a escada GPR-001 §11 (L0–L5) permanece **eixo diferente e intocado** (maturidade do SOT como sistema agêntico inteiro — ver Non-goals e nota de escopo em GPR-001 §11/atomic-spec §7, editadas por Andraus em 2026-09-28). CCM-001 permanece **pendente (SPEC-003)** — nenhum limiar numérico ligado à convicção é fixado. [FONTE: atomic-spec §7 nota; GPR-001 §11 nota; CONST-01]
- [x] **CC-03 — Conviction Vector:** dimensionalidade=8 permanece **fechada**; fórmula/pesos/limiares = **J-001 (aberto/pendente)**. A SPEC-021 define níveis **ordinais qualitativos** (presença/verificação de D-levels e lentes) e **não** fixa qualquer limiar numérico de aprovação ligado a convicção — adiado a **J-001/CCM-001 (SPEC-003)** (Q-A4). [FONTE: INV-03; J-001 pendente]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. Custo não entra em nada análogo a convicção; o cálculo de nível é sobre presença/verificação de critérios, não sobre custo. Economicidade (4Es) nunca rebaixa a proteção do gate E3. [FONTE: INV-04; CEE-001 §10/§11]
- [x] **CC-05 — Complexidade declarada:** **HIGH, D0–D7** (ROADMAP §12; AGENTS.md §4). Maturidade-alvo desta Spec = L3.
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card. Os campos §59 e a cadeia §60 tornam-se obrigatórios quando as Tasks/Engineering Cards forem produzidas (BUILD adiado — atomic-spec §14). Omissão justificada. [FONTE: atomic-spec §8.1]
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem provida pela cadeia ROADMAP §12 → Dossiê (research.md §7-bis, homologado) → esta Spec.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED preenchidos com ID+versão; REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Eixo **VERTICAL (RULE-HV)** avaliado e declarado **não aplicável** (SPEC-021 é meta-harness **irmão** de SPEC-019/SPEC-020 na FASE GOV, não decomposição pai→filha) — ver nota na seção de Herança. [FONTE: EUA-E04 §8.3; RULE-HD-04; RULE-HV]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI, INDETERMINADO, INV-EPI):** aplicado — distinção FATO NORMATIVO / FATO ARQUITETURAL / PROPOSTA / INFERÊNCIA / EXTERNO explícita (ver Etiquetagem). Fontes web tratadas como DADO ([EXTERNO], research.md), nunca baseline; nenhuma hipótese tratada como fato; GAP-1 (gaming/Goodhart) e GAP-2 (limiares) mantidos como **INDETERMINADO**; sem falsa precisão numérica. [FONTE: RULE-EPI; research.md §4]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM):** **N/A** — o domínio é medição de maturidade de processo de especificação; sem terminologia concorrente por escola de análise técnica de mercado. Onde termos externos colidem (CMMI/SPICE "staged/continuous", "Dark Factory"/L5 vendor, LLM-as-Judge), a colisão é registrada e o rótulo **rejeitado como baseline** (research.md §3.2/§4), não adotado. [FONTE: RULE-SEM; research.md §4]
- [x] **CC-11 — Classe/Mecanismo por BASpec (RULE-MECH-01, §10.6):** **INCIDE** (Q-A5; SPEC-021 ≥ SPEC-002, não está na lista de não-retroação SPEC-001/019/020). A SPEC-021 **cita RULE-MECH-01 no próprio texto** (ver D2/D3) e **declara a Classe (D/H/P/C) em cada BASpec com efeito**, com critério 4Es (RULE-MECH-02) e bounded loop + gate de saída onde H/C (RULE-MECH-03). Nenhuma Classe C em BASpec de risco baixo. [FONTE: RULES.md RULE-MECH-01..04; atomic-spec §10.6; research.md §6.1]
- [x] **CC-12 — Princípios de Domínio (RULE-PD-01, §10.7):** **N/A justificado** — a SPEC-021 é **meta-harness de maturidade**, não define escopo de especialidade de **domínio de mercado** (não é Elliott/Fibonacci/SMC/ICT/estrutural). O atomic-spec §10.7 **nomeia explicitamente a SPEC-021** como exemplo de meta-harness que tipicamente não declara `PD-xx`. Nenhum `PD-xx` proposto. Consistente com o tratamento de CC-10 na SPEC-020 (N/A justificado). [FONTE: atomic-spec §10.7; RULE-PD-01; research.md §6.2; SPEC-020/plan.md CC-10]

**Checklist de consistência principiológica (GPR-001 §15):** PC-01 (hierarquia) preservada (protegida, não tocada); PC-02 (SOT não executa) reforçada (maturidade **detecta/atribui nível**, não executa — INV-05/RULE-DEC); PC-04 (piso de convicção) não tocado (níveis qualitativos, sem limiar de convicção — J-001 aberto); 4Es na ordem (Conformidade>Eficácia>...; Economicidade não rebaixa o gate E3); rastreabilidade PB-05 e explicabilidade PB-06 (cada atribuição de nível registra o critério satisfeito/não satisfeito); PB-10 (preservação da incerteza) honrada por INDETERMINADO. Item CLASSE-MECH-001 do §15: cada BASpec com efeito declara Classe (CC-11). Item PRINC-BID-001 do §15: N/A (meta-harness, CC-12).

**Disciplinas cognitivas N8–N17 incidentes:** RULE-EPI (hipótese≠fato; INDETERMINADO em GAP-1/2), RULE-MET-01 (não-fabricação — nenhuma métrica anti-gaming definitiva inventada), RULE-DEC (decisão≠execução — a maturidade **atribui e reporta**; a homologação da Spec-filha é de Andraus), RULE-CAU (nenhuma afirmação causal forte sem mecanismo), RULE-UNC (incerteza localizada, não contaminante).

---

## Herança / Delta (§8.3 — EUA-E04)

```
HERANÇA / DELTA — SPEC-021

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO):
  - Método: atomic-spec.md v1.4 — em particular:
      • Quality Gates L1–L4 (§7): tabela de critérios reusada como substrato de cada nível
        (L1 Operacional / L2 Guiado / L3 Testável / L4 Expert) — SEM redefinir a tabela
      • Profundidade D0–D9 (§2); complexidade↔profundidade (§3); EARS (§4); F.1–F.4 (§5);
        Enforcement E0–E3 (§10); TRACE-06 (§11); CLASSE-MECH-001 (§9/§10.6)
  - Governança do Harness: SPEC-019 v1.0 (BASELINE) — em particular:
      • RULE-HG-06 (Constitution Check como gate obrigatório ANTES do Plan e da homologação) —
        a SPEC-021 ACOPLA o gate de maturidade a este gate já existente
      • RULE-HG-03 (parecer CONFORME ≠ vigência; só Andraus homologa) — decisão≠execução
      • RULE-HG-08 (todo ato de governança produz registro DHR auditável)
      • RULE-HV-01..04 (Herança Vertical) — avaliada; eixo VERTICAL declarado não aplicável (nota abaixo)
  - Avaliação do Harness: SPEC-020 v1.0 (BASELINE) — 9 lentes constitutivas (RULE-EV-01..07):
      a maturidade AGREGA (ordinalmente) os critérios das lentes já avaliados; NÃO redefine
      nem duplica as 9 lentes (relação maturidade×avaliação — Q-R4)
  - Princípios: GPR-001 v1.0 (BASELINE) — §11 (escada L0–L5 = EIXO DIFERENTE, não substituído);
      PC-01..PC-08; PB 4Es (PB-01>PB-02>PB-03>PB-04); PE-04 (refinado por CLASSE-MECH-001); §15
  - Enforcement: ENF-01..08 — com ênfase em ENF-03 (Detector ≠ Gate; LLM nunca é seu próprio gate)
  - Invariantes: INV-03 (Conviction 8D fechada; limiares definitivos = J-001 aberto),
      INV-05 (SOT não executa; produz Signal Package/TMP interno),
      INV-07 (versionamento monotônico), INV-09 (sem baseline informal)

ADDED (delta local — o que esta spec acrescenta):
  - Escada de maturidade CANÔNICA por-Spec de 5 níveis: L0 Declarativo → L1 Especificado →
    L2 Guiado → L3 Testável → L4 Autocontrolado (rótulo L3 = "Testável", harmonizado — Q-A2)
  - Regra determinística de ATRIBUIÇÃO de nível por spec, ancorada em presença + verificação de
    D-levels e lentes SPEC-020 (não em volume de documentação — anti-gaming)
  - Progressão STAGED (cumulativa): um nível só é atingido se todos os inferiores o forem
  - Nível-alvo por complexidade (LOW→L1 · MEDIUM→L2 · HIGH/CRITICAL→L3) como declaração verificável
  - GATE NORMATIVO E3 (Q-A3): Spec-filha abaixo do nível-alvo declarado = inelegível à homologação
  - Detector de gaming (Goodhart) como SINAL, nunca gate (ENF-03)
  - `harness-score` normativo POR SPEC (staged) coexistindo com o score repo-global (continuous)
  - Enforcement Contracts dos atos de atribuição/gate de maturidade (EC-HS-001..003)
  - Declaração de Classe (D/H/P/C) por BASpec com efeito (RULE-MECH-01/CC-11)

MODIFIED (especialização de regra herdada):
  - RULE-HG-06 (Constitution Check como gate) — ESTENDIDA em conteúdo: a atribuição de nível de
    maturidade torna-se item avaliável acoplado ao mesmo gate, sem alterar o texto de RULE-HG-06
    nem criar autoridade nova. (Extensão de itens; a mecânica de gate é reutilizada.)
  - Quality Gates L1–L4 (atomic-spec §7) — NÃO modificadas: reusadas como tabela de critérios
    (a nota de reconciliação em §7 foi inserida por Andraus em 2026-09-28, não por esta Spec)

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal / obrigação-a-obrigação** (EUA-E04 §8.3). O **eixo VERTICAL** (RULE-HV-01..04, conservação-como-conjunto pai→filha) foi avaliado e **não se aplica**: a SPEC-021 não é decomposição *micro* de um *macro* SPEC-019/SPEC-020 — as três são meta-harnesses **irmãos** da FASE GOV (SPEC-019 governa *como* specs mudam; SPEC-020 avalia *se* specs satisfazem critérios; SPEC-021 mede *quão maduras* as specs estão). Declarar herança vertical confundiria os eixos (o cenário ADV-HV-07 da própria SPEC-019 alerta contra isso, e a SPEC-020 já adotou este mesmo entendimento). A dependência de SPEC-019/SPEC-020 é por **acoplamento de contrato** (gate RULE-HG-06; consumo das lentes RULE-EV), não por conservação vertical. [INFERÊNCIA — a confirmar pelo Revisor]

---

## D0 — Missão (Intenção)

A SPEC-021 especifica **como a maturidade de cada Spec do SOT Harness é medida e atribuída**. Define: (1) uma **escada de maturidade canônica única por-Spec** de 5 níveis — `L0 Declarativo → L1 Especificado → L2 Guiado → L3 Testável → L4 Autocontrolado` — reconciliando as escadas internas divergentes (CONFLITO-1) sem redefinir Quality Gates L1–L4 nem a escada GPR-001 §11; (2) a **regra determinística de atribuição de nível** por spec, função de **quais D-levels e quais lentes da SPEC-020 a spec de fato satisfaz e verifica** — nunca do volume de documentação (anti-gaming); (3) o **gate normativo** que condiciona a elegibilidade da Spec-filha à homologação ao seu nível-alvo declarado, com **gate determinístico** e o LLM apenas como **detector** (ENF-03). Torna o `harness-score` **normativo por spec** (staged), não só repo-global (continuous). [FONTE: ROADMAP §12/§21; research.md §5.2; Q-A2/Q-A3]

A maturidade é um **meta-harness** (F.4 Evaluation da taxonomia atomic-spec §5): mede a qualidade das próprias Specs. Materializa a orientação da ROADMAP §12 — "torna o harness-score normativo por spec" e "maturidade não se confunde com volume de documentação".

**O que a Missão NÃO é (fronteira):**
- Não é a **avaliação constitutiva** (9 lentes) → **SPEC-020** (BASELINE). A maturidade **consome** o resultado das lentes; não as redefine. [FONTE: ROADMAP §12]
- Não redefine a escada **GPR-001 §11 (L0–L5)** — eixo diferente (maturidade do SOT como sistema agêntico inteiro). [FONTE: GPR-001 §11 nota; Q-A2]
- Não fixa limiar numérico dependente de convicção → **J-001 / CCM-001 (SPEC-003)** (Q-A4). [FONTE: J-001]
- Não especifica **tooling/telemetria de maturidade de runtime** → fase de implementação; SPEC-045-RUNTIME-001 permanece decisão aberta separada, **não antecipada**. [FONTE: ROADMAP §20/§22]
- Não fecha as dimensões **classe B** da SPEC-020 (BL-017) nem redefine CEM/CHM/CCM/CDM/CNM (CC-02) ou a hierarquia (CC-01).

**Status epistemológico:** a SPEC-021 é FATO ARQUITETURAL candidato a baseline. atomic-spec v1.4, SPEC-019 v1.0, SPEC-020 v1.0, GPR-001 v1.0, INV-*, ENF-*, RULE-MECH-01..04 são FATO NORMATIVO. Fontes externas de maturity models (research.md §2) são [EXTERNO] — DADO, nunca baseline; documentado ≠ homologado (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | **Escada canônica única por-Spec** L0–L4 (nomes + critério objetivo por nível), reconciliando CONFLITO-1 | ROADMAP §12; Q-A2; research.md §3.1/§4 |
| S2 | **Regra determinística de atribuição de nível** por spec (presença + verificação de D-levels e lentes SPEC-020), ordinal e qualitativa | Q-A4; research.md §3.2; INV-03 |
| S3 | **Progressão staged** (cumulativa): nível N exige todos os níveis < N satisfeitos | research.md §3.2 (M1 staged); [EXTERNO] M1 |
| S4 | **Nível-alvo por complexidade** (LOW→L1, MEDIUM→L2, HIGH/CRITICAL→L3) como declaração verificável | atomic-spec §4/§7; AGENTS.md §4 |
| S5 | **Gate normativo E3**: Spec-filha abaixo do nível-alvo declarado = inelegível à homologação | Q-A3; RULE-HG-06; ENF-03/04 |
| S6 | **Anti-gaming** (Goodhart): nível ancorado em evidência verificável; detector de inflação de documentação = SINAL, nunca gate | research.md §3.2/§4 GAP-1; ENF-03; RULE-MET-01 |
| S7 | **`harness-score` normativo por spec** (staged) coexistindo com o score repo-global (continuous) | ROADMAP §12; research.md §3.2 (M1) |
| S8 | **Relação maturidade × avaliação (SPEC-020)**: maturidade agrega ordinalmente os critérios das lentes, sem duplicá-las | research.md §3.1 (Q-R4) |
| S9 | **Enforcement Contracts** dos atos de atribuição/gate de maturidade (E2/E3) + **Classe por BASpec** (RULE-MECH-01) | atomic-spec §10; RULE-MECH-01; Q-A5 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Redefinir as 9 lentes da SPEC-020 | **SPEC-020** (BASELINE) | Maturidade **consome** as lentes; não as redefine (CC-02 análogo) [FONTE: ROADMAP §12] |
| Fechar dimensões **classe B** da SPEC-020 | **SPEC-007/038/014** (BL-017) | DIFERIDAS; não antecipadas (CONS-01) [FONTE: RMR-001 BL-017] |
| Limiares numéricos dependentes de convicção | **J-001 / CCM-001 (SPEC-003)** | J-001 aberto — maturidade é ordinal/qualitativa (GAP-2, Q-A4) |
| Redefinir a escada **GPR-001 §11 (L0–L5)** | **GPR-001** (BASELINE) | Eixo diferente (SOT como sistema inteiro); coexiste sem fusão (CC-02; Q-A2) [FONTE: GPR-001 §11 nota] |
| Redefinir **Quality Gates L1–L4** (atomic-spec §7) ou a hierarquia | atomic-spec §7 ; PC-01 | Constrói SOBRE / reusa como tabela de critérios; reconcilia sem apagar (INV-07) |
| Maturidade **organizacional/empresarial** (pilares estratégia/talento/cultura) | — (fora do SOT) | SOT mede specs, não organização (CONFLITO-2); rejeitado como baseline [EXTERNO] |
| **Tooling/telemetria de maturidade de runtime** | Fase de implementação; SPEC-045-RUNTIME-001 | Fase spec-first (ROADMAP §22); decisão aberta separada, não antecipada |
| Meta-Cognitive Supervisor / auditoria D9 completa (critério de L4 em runtime) | **SPEC-024 / SPEC-041** | L4 referencia esses componentes; não os especifica aqui |
| Adotar rótulos/ladders externos (CMMI/SPICE, NIST janelas, vendor L0–L5, LLM-as-Judge-gate) como baseline | — | Rejeitados (INV-09); referência subordinada apenas (research.md §4) |

---

## D2 — Regras

> **Etiqueta:** as RULE-MM-* abaixo são **[PROPOSTA]** — tornam-se normativas apenas na homologação de Andraus + registro no RULES.md pelo Controlador (nova seção "Regras de Maturidade do Harness (RULE-MM)"). Até lá, não são invocáveis como FATO NORMATIVO (RULE-HG-02). As RULE/INV/ENF citadas como fundamento (**RULE-MECH-01..04**, ENF-03/04, RULE-HG-06, RULE-EV-01..07, INV-03/07, RULE-MET-01) **já existem** e são FATO NORMATIVO.

```
RULE-MM-01: A maturidade de toda Spec do SOT DEVE ser medida na ESCADA CANÔNICA POR-SPEC de 5 níveis:
            L0 Declarativo → L1 Especificado → L2 Guiado → L3 Testável → L4 Autocontrolado.
            Os critérios objetivos de cada nível são os das Quality Gates atomic-spec §7 (L1–L4),
            com L0 abaixo da Quality Gate L1. Esta escada NÃO redefine as Quality Gates nem a
            escada GPR-001 §11 (L0–L5, eixo do sistema inteiro).
            [Fonte: ROADMAP §12; atomic-spec §7; GPR-001 §11 nota; Q-A2]  [PROPOSTA]

RULE-MM-02: A atribuição de nível DEVE ser DETERMINÍSTICA e ancorada em PRESENÇA + VERIFICAÇÃO de
            D-levels e de lentes da SPEC-020, NUNCA em volume de documentação. O detector semântico
            (LLM) que sinaliza gaming/inflação é DETECTOR (sinal); o veredito de nível é do gate
            determinístico e/ou de Andraus (ENF-03).
            [Fonte: ENF-03; RULE-MET-01; research.md §3.2/§4 GAP-1]  [PROPOSTA]

RULE-MM-03: A progressão é STAGED (cumulativa): o nível N só é atribuído se todos os níveis inferiores
            a N estiverem satisfeitos. Saltar nível é proibido.
            [Fonte: research.md §3.2 (M1 staged); INV-03 (ordinal)]  [PROPOSTA]

RULE-MM-04: Toda Spec DEVE declarar seu NÍVEL-ALVO por complexidade (LOW→L1, MEDIUM→L2,
            HIGH/CRITICAL→L3). Nível-alvo acima do atingível no spec-time (L4 exige auditoria D9 +
            backtest de comportamento + aprovação registrada de Andraus — atomic-spec §7 L4) só é
            reivindicável na fase de implementação; no spec-first o teto é L3.
            [Fonte: atomic-spec §4/§7; AGENTS.md §4; ROADMAP §22]  [PROPOSTA]

RULE-MM-05: Uma Spec-filha cujo nível ATINGIDO é inferior ao seu NÍVEL-ALVO declarado é INELEGÍVEL à
            homologação (gate normativo, efeito E3). Fail-closed: ambiguidade sobre o nível atingido
            ⇒ não aprova.
            [Fonte: ROADMAP §12 ("normativo por spec"); Q-A3; RULE-HG-06; ENF-04]  [PROPOSTA]

RULE-MM-06: Nenhum nível DEVE fixar limiar numérico de aprovação dependente de convicção; níveis são
            ordinais qualitativos. Tais limiares permanecem em J-001/CCM-001 (SPEC-003).
            [Fonte: J-001; INV-03; CONS-01; Q-A4]  [PROPOSTA]

RULE-MM-07: O `harness-score` por-spec (staged) NÃO substitui o score repo-global (continuous);
            ambos coexistem. A maturidade por-spec AGREGA ordinalmente os critérios das lentes da
            SPEC-020 já avaliados, sem redefinir nem duplicar as 9 lentes.
            [Fonte: ROADMAP §12; research.md §3.1/§3.2; SPEC-020 RULE-EV-01]  [PROPOSTA]
```

---

## Critérios de Aceitação (EARS)

1. Quando uma Spec-filha é submetida à homologação com nível de maturidade atingido inferior ao seu nível-alvo declarado, o Harness Score DEVE bloquear a elegibilidade à homologação (gate E3).
2. Quando um detector semântico (LLM) sinaliza possível gaming (inflação de documentação para reivindicar nível superior), o Harness Score NÃO DEVE tratar esse sinal como gate — o veredito de nível DEVE permanecer no gate determinístico e/ou em Andraus.
3. Quando uma Spec reivindica um nível N sem satisfazer os critérios de um nível inferior a N, o Harness Score DEVE recusar a atribuição de N (progressão staged).
4. Quando uma tabela de atribuição tenta fixar um limiar numérico de aprovação dependente de convicção, o Harness Score DEVE rejeitar o fechamento e manter o critério ordinal qualitativo (J-001 aberto).
5. Quando uma Spec satisfaz D0–D3 + schema válido + RULES rastreadas mas não possui D4/protocolo, o Harness Score DEVE atribuir nível L1 (não L2).
6. Quando uma Spec HIGH/CRITICAL não possui ≥3 cenários D7 + ≥1 adversarial D8 + revisão independente, o Harness Score DEVE recusar a atribuição de L3.
7. Quando uma proposta tenta usar a escada por-Spec para redefinir a escada GPR-001 §11 (L0–L5) ou as Quality Gates L1–L4, o Harness Score DEVE rejeitar a redefinição (CC-02 / eixos distintos).
8. Quando o volume de documentação de uma Spec aumenta sem aumento de D-levels/lentes verificados, o Harness Score NÃO DEVE elevar o nível de maturidade.

---

## D3 — Comportamento (BASpecs com Classe/Mecanismo — RULE-MECH-01/CC-11)

> Toda BASpec abaixo com efeito de gate/atribuição declara sua **Classe (D/H/P/C)** (RULE-MECH-01), o **Mecanismo**, o **critério 4Es** (RULE-MECH-02) e — onde H/C — **bounded loop** e **gate de saída** (RULE-MECH-03).

### BASpec-HS-001 — Definição dos critérios objetivos de cada nível (L0–L4)

```
BASpec-HS-001:
  QUANDO:       Uma Spec-filha é medida quanto à maturidade
  ENTÃO:        Harness Score mapeia cada nível a um critério objetivo:
                L0 Declarativo = D0–D1 presentes (intenção/escopo como texto, sem verificação);
                L1 Especificado = Quality Gate L1 (D0–D3 + schema válido + RULES rastreadas);
                L2 Guiado = Quality Gate L2 (D4 fórmula+exemplo ONDE há regra determinística numérica,
                  senão N/A justificado + protocolo D6 + conflitos mapeados);
                L3 Testável = Quality Gate L3 (D5 estados + ≥3 cenários D7 + ≥1 adversarial D8 +
                  revisão independente);
                L4 Autocontrolado = Quality Gate L4 (D9 auditoria + backtest de comportamento (P12) +
                  aprovação registrada de Andraus)
  PORQUE:       Reconciliação homologada (Q-A2): a escada por-Spec reusa as Quality Gates §7 como
                tabela de critérios; nível ≠ volume (anti-gaming)
  REFERÊNCIA:   RULE-MM-01; atomic-spec §7; ROADMAP §12
  CLASSE:       D (Determinístico)
  MECANISMO:    Regra/código explícito: verifica presença/verificação dos artefatos por nível
  CRITÉRIO 4Es: Eficácia — o critério de nível deve ser inequívoco e verificável; determinismo elimina
                ambiguidade (não há retry nem julgamento aberto)
  VERIFICADO POR:
    DADO        Spec-filha com D0–D3 + schema válido + RULES rastreadas, sem D4/D5/D7/D8
    QUANDO      Harness Score mapeia critérios
    ENTÃO       critérios de L1 satisfeitos; critérios de L2+ não satisfeitos
    VERIFICAÇÃO relatório lista, por nível, artefato exigido × presente/verificado
```

### BASpec-HS-002 — Atribuição determinística do nível atingido

```
BASpec-HS-002:
  QUANDO:       Os critérios de nível (HS-001) foram avaliados sobre uma Spec-filha
  ENTÃO:        Harness Score atribui o nível ATINGIDO = o maior N cujos critérios (e os de todos os
                níveis < N) estão presentes E verificados; a atribuição é registrada com o critério
                satisfeito/não satisfeito de cada nível (rastreável — PB-05)
  PORQUE:       Maturidade é agregação verificável de critérios, não contagem de artefatos (anti-Goodhart);
                atribuição rastreável sustenta explicabilidade (PB-06)
  REFERÊNCIA:   RULE-MM-02; RULE-MM-03; ENF-03; [EXTERNO] research.md M6 (DEMM), M1
  CLASSE:       D (Determinístico)
  MECANISMO:    Regra/código: max{N | ∀ k≤N: critérios(k) presentes∧verificados}; sem julgamento de LLM
  CRITÉRIO 4Es: Eficácia — a atribuição correta do nível prevalece; determinismo garante reprodutibilidade
  VERIFICADO POR:
    DADO        Spec-filha com L1 e L2 satisfeitos, L3 não satisfeito (falta D8)
    QUANDO      Harness Score atribui o nível
    ENTÃO       nível atingido = L2 (não L3 — staged)
    VERIFICAÇÃO registro mostra L1✔ L2✔ L3✘ (motivo: D8 ausente); nível = L2
```

### BASpec-HS-003 — Progressão staged (proibição de salto de nível)

```
BASpec-HS-003:
  QUANDO:       Uma Spec reivindica (ou uma rotina tenta atribuir) nível N sem satisfazer um nível < N
  ENTÃO:        Harness Score recusa a atribuição de N e reporta o nível inferior faltante
  PORQUE:       Progressão de maturidade é cumulativa (staged) — a integridade da escada exige que
                níveis altos pressuponham os inferiores
  REFERÊNCIA:   RULE-MM-03; [EXTERNO] research.md M1 (staged)
  CLASSE:       D (Determinístico)
  MECANISMO:    Regra/código: se ∃ k<N com critérios(k) não satisfeitos ⇒ atribuição de N recusada
  CRITÉRIO 4Es: Eficácia — impedir nível inflado (salto) preserva o significado do nível
  VERIFICADO POR:
    DADO        Spec com D5+D7+D8 (aparência de L3) mas sem RULES rastreadas (L1 falho)
    QUANDO      Harness Score avalia a progressão
    ENTÃO       L3 recusado; nível atingido reportado = L0 (L1 faltante)
    VERIFICAÇÃO registro aponta L1✘ como bloqueio da progressão
```

### BASpec-HS-004 — Nível-alvo por complexidade

```
BASpec-HS-004:
  QUANDO:       Uma Spec-filha declara sua complexidade (LOW/MEDIUM/HIGH/CRITICAL)
  ENTÃO:        Harness Score deriva o NÍVEL-ALVO: LOW→L1, MEDIUM→L2, HIGH→L3, CRITICAL→L3
                (teto spec-time = L3; L4 exige backtest/D9/Andraus na implementação — RULE-MM-04)
  PORQUE:       O nível-alvo deve ser proporcional à criticidade (PB-08); complexidade↔profundidade
                é a fonte homologada (atomic-spec §4/§7)
  REFERÊNCIA:   RULE-MM-04; atomic-spec §4/§7; AGENTS.md §4
  CLASSE:       D (Determinístico)
  MECANISMO:    Regra/código: tabela complexidade→nível-alvo
  CRITÉRIO 4Es: Efetividade — o alvo certo evita exigir profundidade desproporcional (Economicidade
                não rebaixa o alvo mínimo de Eficácia)
  VERIFICADO POR:
    DADO        Spec-filha declarada HIGH
    QUANDO      Harness Score deriva o nível-alvo
    ENTÃO       nível-alvo = L3
    VERIFICAÇÃO tabela complexidade→alvo aplicada; alvo registrado
```

### BASpec-HS-005 — Gate normativo (inelegibilidade abaixo do nível-alvo) — E3

```
BASpec-HS-005:
  QUANDO:       Uma Spec-filha é submetida à homologação com nível atingido < nível-alvo declarado
  ENTÃO:        Harness Score bloqueia a elegibilidade à homologação (gate normativo E3), acoplado ao
                Constitution Check / RULE-HG-06; fail-closed em ambiguidade sobre o nível atingido
  PORQUE:       ROADMAP §12 torna a maturidade "normativa por spec" (Q-A3); abaixo do alvo, a Spec não
                está madura o suficiente para virar baseline (INV-09)
  REFERÊNCIA:   RULE-MM-05; RULE-HG-06; ENF-04; ROADMAP §12; Q-A3
  CLASSE:       C (Constitutivo — enforcement, gate obrigatório nunca bypassável)
  MECANISMO:    Gate determinístico: nível_atingido ≥ nível_alvo ? elegível : inelegível
  CRITÉRIO 4Es: Conformidade/Eficácia — o gate protege a integridade da baseline; Economicidade nunca
                o rebaixa (E3)
  GATE DE SAÍDA: comparação determinística nível_atingido vs nível_alvo (é o próprio gate)
  VERIFICADO POR:
    DADO        Spec-filha HIGH (alvo L3) com nível atingido L2
    QUANDO      Harness Score aplica o gate normativo
    ENTÃO       elegibilidade = BLOQUEADA, código "MATURITY_BELOW_TARGET (L2<L3)"
    VERIFICAÇÃO gate não passa; Spec-filha permanece inelegível até atingir L3
```

### BASpec-HS-006 — Anti-gaming (detector de volume, não gate) — Goodhart

```
BASpec-HS-006:
  QUANDO:       Uma Spec-filha ganha volume de documentação sem aumento de D-levels/lentes verificados
  ENTÃO:        Harness Score NÃO eleva o nível (o cálculo ignora volume); um detector semântico (LLM)
                PODE sinalizar suspeita de gaming como INSUMO ao Revisor/gate determinístico — nunca
                aprova/reprova nível por juízo de LLM isolado
  PORQUE:       "When a measure becomes a target, it ceases to be a good measure" (Goodhart) — o nível
                deve refletir capacidade verificável, não quantidade; Detector ≠ Gate (ENF-03)
  REFERÊNCIA:   RULE-MM-02; ENF-03; RULE-MET-01; [EXTERNO] research.md M8 (Goodhart), M6 (DEMM)
  CLASSE:       H (Híbrido — LLM detecta suspeita de gaming; código verifica os critérios substantivos)
  MECANISMO:    LLM sinaliza (DETECTED); gate determinístico recomputa o nível por presença+verificação
  CRITÉRIO 4Es: Eficácia — evitar nível fabricado é integridade da medida; o detector acelera (Eficiência)
                sem decidir
  BOUNDED LOOP: o detector roda uma vez por submissão de Spec-filha (sem retry infinito); um re-run só
                ocorre em nova versão da Spec-filha (INV-07)
  GATE DE SAÍDA: recomputo determinístico do nível (BASpec-HS-002) — o sinal do LLM não altera o nível
  VERIFICADO POR:
    DADO        Spec-filha com 3x mais texto e os mesmos D-levels/lentes verificados
    QUANDO      Harness Score recomputa o nível
    ENTÃO       nível inalterado; sinal de gaming (se houver) registrado como insumo, não veredito
    VERIFICAÇÃO log mostra DETECTED (gaming?) distinto do nível atribuído pelo gate determinístico
```

### BASpec-HS-007 — Rejeição de limiar numérico dependente de convicção

```
BASpec-HS-007:
  QUANDO:       Uma tabela/rotina de atribuição tenta fixar aprovação de nível por limiar numérico
                dependente de convicção (ex.: "L3 se convicção-de-maturidade ≥ N%")
  ENTÃO:        Harness Score rejeita o fechamento e mantém o critério ordinal qualitativo
  PORQUE:       J-001 (fórmula/pesos/limiares definitivos do Conviction Vector) está em aberto; nenhum
                limiar de convicção pode virar invariante fechado (INV-03/CONS-01)
  REFERÊNCIA:   RULE-MM-06; J-001; INV-03; CONS-01; Q-A4
  CLASSE:       C (Constitutivo — enforcement de fronteira com decisão aberta)
  MECANISMO:    Gate determinístico: presença de limiar numérico ligado a convicção ⇒ rejeição
  CRITÉRIO 4Es: Conformidade — respeitar a decisão aberta J-001 prevalece sobre qualquer conveniência
  GATE DE SAÍDA: verificação determinística de ausência de limiar de convicção (é o próprio gate)
  VERIFICADO POR:
    DADO        proposta de "aprovar L3 se convicção-de-maturidade ≥ 80%"
    QUANDO      Harness Score aplica RULE-MM-06
    ENTÃO       fechamento rejeitado; critério mantido ordinal (J-001 aberto)
    VERIFICAÇÃO nenhum limiar numérico de convicção fixado; CONS-01 preservado
```

### BASpec-HS-008 — Coexistência harness-score por-spec (staged) × repo-global (continuous)

```
BASpec-HS-008:
  QUANDO:       O `harness-score` é computado
  ENTÃO:        Harness Score produz um nível de maturidade POR SPEC (staged) que NÃO substitui o score
                repo-global (continuous); a maturidade por-spec agrega ordinalmente os critérios das
                lentes da SPEC-020 já avaliados, sem redefinir nem duplicar as 9 lentes
  PORQUE:       ROADMAP §12 pede "harness-score normativo por spec"; a distinção staged/continuous (M1)
                modela "por-spec vs repo-global"; a maturidade consome a avaliação (SPEC-020), não a refaz
  REFERÊNCIA:   RULE-MM-07; SPEC-020 RULE-EV-01; ROADMAP §12; [EXTERNO] research.md M1
  CLASSE:       D (Determinístico)
  MECANISMO:    Regra/código: score por-spec = f(níveis atingidos por spec); score repo-global mantido
  CRITÉRIO 4Es: Efetividade — o score por-spec chega ao gate de cada Spec no momento útil (spec-time)
  VERIFICADO POR:
    DADO        repositório com N specs, cada uma com nível por-spec
    QUANDO      Harness Score é computado
    ENTÃO       nível por-spec presente para cada spec; score repo-global preservado (coexistem)
    VERIFICAÇÃO ambos os scores presentes; nenhum redefine as lentes SPEC-020
```

---

## D4 — Algoritmo

**D4 numérico N/A justificado.** A atribuição de nível é **ordinal e qualitativa** (Q-A4): não há fórmula numérica de agregação de "score de maturidade" — fixá-la dependeria de limiares ligados a convicção (J-001 aberto — RULE-MM-06). O que existe é uma **regra determinística não-numérica** (BASpec-HS-002/HS-003), especificada no formato ALGORITMO abaixo sem números:

```
ALGORITMO: atribuir_nivel_maturidade
ENTRADA:   Spec-filha S; resultados de presença/verificação de D-levels de S; resultados das lentes
           da SPEC-020 sobre S (PASS/FAIL/INDETERMINADO)
PROCESSO:  1. Para cada nível k em [L0, L1, L2, L3, L4]: satisfeito(k) := todos os critérios objetivos
              de k (BASpec-HS-001) presentes E verificados (não por volume).
           2. nível_atingido := maior N tal que satisfeito(k) para todo k ≤ N (staged — HS-003).
           3. Volume de documentação NÃO entra em satisfeito(k) (anti-gaming — HS-006).
           4. Nenhum limiar numérico dependente de convicção é usado (HS-007).
SAÍDA:     nível_atingido ∈ {L0,L1,L2,L3,L4} (ordinal) + registro por-nível do critério satisfeito/faltante
EXEMPLO (ordinal, sem número): S HIGH com D0–D3+schema+RULES (L1✔), D6 protocolo+conflitos (L2✔),
           D5+3×D7+1×D8+revisão (L3✔), sem D9/backtest/Andraus (L4✘) ⇒ nível_atingido = L3
```

**Nota de reconciliação [PROPOSTA]:** o critério "D4 (fórmula+exemplo)" da Quality Gate L2 (atomic-spec §7) é **condicional** — só se aplica a componentes com regra determinística **numérica** real (atomic-spec §2: D4 obrigatório para "Determinísticos/semi"). Onde o componente legitimamente não tem regra numérica (como esta própria Spec e meta-harnesses), D4-numérico é **N/A justificado** e a evidência de L2 é o **protocolo determinístico (D6) + conflitos mapeados**. Isto não redefine as Quality Gates; explicita como a atribuição de nível trata D-levels N/A (não penaliza N/A justificado; penaliza omissão não justificada). [PROPOSTA — a confirmar pelo Revisor/Andraus]

---

## D5 — Máquina de estados da atribuição de maturidade de uma Spec-filha

| Estado | Significado |
|---|---|
| NOT_SCORED | Maturidade ainda não medida para a Spec-filha |
| DETECTED | Detector semântico (LLM) produziu sinal (ex.: suspeita de gaming) — **insumo, não veredito** (ENF-03) |
| LEVELED | Gate determinístico atribuiu o nível atingido (L0–L4) |
| ELIGIBLE | nível atingido ≥ nível-alvo → elegível à homologação |
| BLOCKED | nível atingido < nível-alvo → inelegível (gate normativo E3, fail-closed) |
| INDETERMINADO | Incerteza material sobre um critério (ex.: lente SPEC-020 em INDETERMINADO) — não força nível; encaminha ao adversarial/Revisor |

### Transições

```
NOT_SCORED    -> DETECTED       (detector semântico roda; sinal produzido — opcional)
NOT_SCORED    -> LEVELED        (gate determinístico atribui nível sem sinal de detector)
DETECTED      -> LEVELED        (gate determinístico atribui nível; sinal do LLM é insumo, não veredito)
LEVELED       -> ELIGIBLE       (nível atingido ≥ nível-alvo)
LEVELED       -> BLOCKED        (nível atingido < nível-alvo — E3, fail-closed)
LEVELED       -> INDETERMINADO  (critério material incerto; encaminha ao Revisor/adversarial)
INDETERMINADO -> LEVELED        (após resolução da incerteza; nunca aprovado por LLM isolado)
```

**Invariante de estado (ENF-03):** nunca há transição DETECTED → ELIGIBLE/BLOCKED **por juízo do LLM** — a atribuição de nível e a decisão de elegibilidade são do gate determinístico e/ou da homologação de Andraus. DETECTED é sinal, não decisão.

---

## D6 — Protocolo de atribuição (acoplamento ao Constitution Check / RULE-HG-06)

Sequência canônica de medição de maturidade de uma Spec-filha — acoplada ao gate de spec-time da SPEC-019 (RULE-HG-06) e ao resultado da avaliação da SPEC-020:

```
1. Especificador redige a Spec-filha (plan.md) + checks.md; declara complexidade e nível-alvo.
2. A SPEC-020 avalia as 9 lentes (resultado PASS/FAIL/INDETERMINADO) — insumo à maturidade.
3. Harness Score verifica, por nível (L0..L4), presença + verificação dos critérios (BASpec-HS-001):
   - L0: D0–D1 presentes;   - L1: Quality Gate L1;   - L2: Quality Gate L2 (D4 numérico N/A justif. permitido);
   - L3: Quality Gate L3 (D5 + ≥3 D7 + ≥1 D8 + revisão independente);   - L4: Quality Gate L4 (D9+backtest+Andraus).
4. Detector semântico (LLM) opcional sinaliza suspeita de gaming (volume) → estado DETECTED (insumo).
5. GATE determinístico atribui nível_atingido = maior N cumulativo (staged) → estado LEVELED.
6. Compara nível_atingido vs nível-alvo: ≥ → ELIGIBLE; < → BLOCKED (E3, fail-closed).
7. Critério material incerto (ex.: lente em INDETERMINADO) → INDETERMINADO; encaminha ao Revisor/adversarial.
8. Revisor (GRE-001/HRE-001) audita a atribuição como parte do parecer (detector, não gate).
9. Andraus homologa a Spec-filha (única autoridade de vigência — RULE-HG-03). A maturidade NÃO homologa.
```

O acoplamento **não cria autoridade nova**: reutiliza o gate RULE-HG-06 (Constitution Check antes do Plan e da homologação), estendendo os **itens** avaliados com o gate de maturidade. [FONTE: RULE-HG-06; Q-A3]

---

## D7 — Cenários de Teste

### Cenário-HS-T01 — L1 atribuído, L2 recusado por falta de protocolo

```
DADO        Spec-filha com D0–D3 + schema válido + RULES rastreadas, sem protocolo D6/conflitos
QUANDO      Harness Score atribui o nível
ENTÃO       nível atingido = L1 (L2 recusado)
VERIFICAÇÃO registro mostra L1✔ L2✘ (protocolo/conflitos ausentes)
```

### Cenário-HS-T02 — Gate normativo bloqueia HIGH abaixo do alvo

```
DADO        Spec-filha HIGH (nível-alvo L3) com nível atingido L2 (falta ≥1 adversarial D8)
QUANDO      Harness Score aplica o gate normativo (E3)
ENTÃO       elegibilidade = BLOCKED, "MATURITY_BELOW_TARGET (L2<L3)"
VERIFICAÇÃO gate não passa; Spec-filha inelegível à homologação
```

### Cenário-HS-T03 — Volume não eleva o nível (anti-gaming)

```
DADO        Spec-filha com documentação triplicada e os mesmos D-levels/lentes verificados
QUANDO      Harness Score recomputa o nível
ENTÃO       nível inalterado; sinal de gaming (se houver) registrado como insumo (DETECTED), não veredito
VERIFICAÇÃO log distingue DETECTED do nível atribuído pelo gate determinístico (ENF-03)
```

### Cenário-HS-T04 — Salto de nível recusado (staged)

```
DADO        Spec com D5+D7+D8 (aparência de L3) mas sem RULES rastreadas (L1 falho)
QUANDO      Harness Score avalia a progressão
ENTÃO       L3 recusado; nível atingido = L0 (L1 faltante)
VERIFICAÇÃO registro aponta L1✘ como bloqueio (RULE-MM-03)
```

### Cenário-HS-T05 — Limiar de convicção rejeitado

```
DADO        proposta de "aprovar L3 se convicção-de-maturidade ≥ 80%"
QUANDO      Harness Score aplica RULE-MM-06
ENTÃO       fechamento rejeitado; critério mantido ordinal (J-001 aberto)
VERIFICAÇÃO nenhum limiar numérico ligado a convicção fixado; CONS-01 preservado
```

---

## D8 — Cenários Adversariais [casos de negação — reforço §7-bis / maturidade-alvo L3]

Princípio transversal: **fail-closed** — em qualquer ambiguidade sobre o nível atingido ou sobre a autoridade do veredito, o Harness Score NÃO aprova a Spec-filha e retorna estado/código específico.

### ADV-HS-01 — Gaming por volume de documentação
**DADO:** Spec-filha infla documentação para reivindicar L3 sem novos D-levels/lentes verificados
**QUANDO:** o nível é computado
**ENTÃO:** nível não elevado (`VOLUME_NOT_MATURITY`); sinal de gaming = insumo, não veredito
**PORQUE:** maturidade ≠ volume (Goodhart — ROADMAP §12; research.md M8); RULE-MM-02
**VERIFICAÇÃO:** recomputo determinístico ignora volume; nível inalterado

### ADV-HS-02 — LLM-as-Judge usado como gate de nível
**DADO:** proposta de deixar o detector LLM atribuir/aprovar o nível de maturidade
**QUANDO:** a atribuição é configurada
**ENTÃO:** rejeitar (fail-closed) `LLM_JUDGE_AS_GATE_FORBIDDEN`; LLM permanece detector; gate determinístico/Andraus decide
**PORQUE:** Detector ≠ Gate; o LLM nunca é seu próprio gate (ENF-03; RULE-MM-02)
**VERIFICAÇÃO:** configuração recusada; nível atribuído pelo gate determinístico

### ADV-HS-03 — Salto de nível (L3 sem L1/L2)
**DADO:** rotina tenta atribuir L3 a uma Spec sem satisfazer L1/L2
**QUANDO:** a progressão é avaliada
**ENTÃO:** rejeitar `STAGED_VIOLATION`; nível atingido = maior N cumulativo válido
**PORQUE:** progressão staged (RULE-MM-03; research.md M1)
**VERIFICAÇÃO:** nível reportado respeita a cumulatividade

### ADV-HS-04 — Limiar numérico de convicção embutido no nível
**DADO:** tentativa de fixar aprovação de nível por limiar dependente de convicção
**QUANDO:** RULE-MM-06 é aplicada
**ENTÃO:** rejeitar `CONVICTION_THRESHOLD_LOCKED_FORBIDDEN`; manter ordinal (J-001 aberto)
**PORQUE:** J-001 em aberto; limiares definitivos não podem ser invariante fechado (INV-03/CONS-01)
**VERIFICAÇÃO:** nenhum limiar de convicção fixado; J-001 preservado como aberto

### ADV-HS-05 — Escada por-Spec contrabandeada para redefinir GPR-001 §11 ou Quality Gates
**DADO:** proposta de usar a escada por-Spec (L0–L4) para redefinir a escada GPR-001 §11 (L0–L5) ou as Quality Gates L1–L4
**QUANDO:** o escopo é avaliado
**ENTÃO:** rejeitar `SCALE_REDEFINITION_FORBIDDEN`; a escada por-Spec coexiste como eixo distinto; §11 e §7 intocados
**PORQUE:** eixos diferentes (Q-A2); CC-02; INV-07 (não apagar/redefinir baseline)
**VERIFICAÇÃO:** GPR-001 §11 e Quality Gates §7 preservados; escadas coexistem

### ADV-HS-06 — Maturidade tenta redefinir/duplicar as 9 lentes da SPEC-020
**DADO:** proposta de a maturidade reescrever critérios das lentes (ex.: refazer role adherence)
**QUANDO:** a relação maturidade×avaliação é definida
**ENTÃO:** rejeitar `LENS_REDEFINITION_FORBIDDEN`; maturidade AGREGA os resultados das lentes, não as redefine
**PORQUE:** SPEC-020 é BASELINE (CC-02 análogo); RULE-MM-07
**VERIFICAÇÃO:** nenhuma lente redefinida; maturidade consome PASS/FAIL/INDETERMINADO das lentes

### ADV-HS-07 — Spec abaixo do alvo homologada apesar do gate
**DADO:** tentativa de homologar Spec-filha HIGH com nível atingido L2 (< alvo L3)
**QUANDO:** o gate normativo é aplicado
**ENTÃO:** fail-closed `MATURITY_BELOW_TARGET`; permanece inelegível; homologação recusada
**PORQUE:** gate normativo E3 (Q-A3; RULE-MM-05; ENF-04); a maturidade não homologa — só Andraus (RULE-HG-03)
**VERIFICAÇÃO:** elegibilidade bloqueada até o alvo ser atingido; nenhuma homologação decorre da maturidade

### ADV-HS-08 — Nível-alvo rebaixado por pressão de Economicidade
**DADO:** proposta de rebaixar o nível-alvo de uma Spec CRITICAL para "poupar esforço"
**QUANDO:** o nível-alvo é derivado
**ENTÃO:** rejeitar `TARGET_DOWNGRADE_FORBIDDEN`; alvo permanece proporcional à complexidade
**PORQUE:** 4Es — Economicidade nunca rebaixa Eficácia/Conformidade (PB-01>PB-04; RULE-MM-04)
**VERIFICAÇÃO:** nível-alvo mantido pela tabela complexidade→alvo; rebaixamento silencioso recusado

> **Cobertura:** 8 cenários adversariais (excede o mínimo de ≥1 para HIGH; alimenta a maturidade-alvo L3 e o §7-bis). Casos de negação das BASpecs e das fronteiras homologadas.

---

## D9 — Auditabilidade (por referência)

Cada atribuição de maturidade DEVE ser reconstruível: entrada (Spec-filha + versão), critérios por nível (presente/verificado/faltante), nível atingido, nível-alvo, veredito de elegibilidade e autoridade do veredito (gate determinístico/Revisor/Andraus), sinal de detector (se houve), código de achado. Reconstrução completa (D9) pertence a **SPEC-041** (Cognitive Audit); aqui fica **por referência** (coerente com alvo D0–D7). O critério L4 da própria escada (auditoria D9 + backtest) só é atingível na fase de implementação (RULE-MM-04). [FONTE: atomic-spec §2 (D9); CONSTITUTION P13]

---

## I/O Schemas (lógicos)

### Resultado de maturidade de uma Spec-filha — schema lógico

```json
{
  "spec_filha": "SPEC-0xx vX.Y",
  "complexidade": "LOW | MEDIUM | HIGH | CRITICAL",
  "nivel_alvo": "L1 | L2 | L3",
  "criterios_por_nivel": {
    "L0": {"satisfeito": true,  "faltante": null},
    "L1": {"satisfeito": true,  "faltante": null},
    "L2": {"satisfeito": true,  "faltante": null},
    "L3": {"satisfeito": false, "faltante": "≥1 adversarial D8 ausente"},
    "L4": {"satisfeito": false, "faltante": "D9+backtest+Andraus (implementação)"}
  },
  "nivel_atingido": "L2",
  "estado": "NOT_SCORED | DETECTED | LEVELED | ELIGIBLE | BLOCKED | INDETERMINADO",
  "elegivel_homologacao": false,
  "detector_signal": "<suspeita de gaming — insumo, não veredito>",
  "veredito_por": "gate_deterministico | revisor | andraus",
  "codigo_achado": "MATURITY_BELOW_TARGET | VOLUME_NOT_MATURITY | STAGED_VIOLATION | ...",
  "preserva_historico": true
}
```

---

## Enforcement Contracts

### EC-HS-001 — Atribuição de nível de maturidade a uma Spec-filha

```
CAPABILITY   : Computar e registrar o nível de maturidade atingido (L0–L4) de uma Spec-filha, por
               presença+verificação de D-levels e lentes SPEC-020 (gate determinístico)
EFFECT       : Publica o nível atingido no relatório/checks.md (insumo do gate de spec-time)
PRECOND      : (critérios por nível avaliados por HS-001) AND (progressão staged aplicada — HS-003) AND
               (volume de documentação NÃO usado — HS-006) AND (detector semântico apenas como sinal — ENF-03)
POSTCOND     : Nível atingido registrado com o critério satisfeito/faltante de cada nível (rastreável);
               nada é homologado pela atribuição
POLICY       : RULE-MM-01/02/03; RULE-EV-01 (consome lentes); ENF-03; INV-09
LEVEL        : E3 (Crítico — condiciona efeito normativo de governança sobre a Spec-filha)
FAILURE-MODE : Fail-closed — ambiguidade sobre o nível atingido ⇒ estado INDETERMINADO / não eleva;
               Spec-filha não ganha nível sem evidência verificada
EVIDENCE     : Relatório por nível (schema I/O); entrada em checks.md; parecer do Revisor
             + método de observação de falso-DENY: amostragem de Specs cujo nível foi subestimado por
               critério de fato satisfeito (limiar = gap aberto, ENF-07)
```

### EC-HS-002 — Gate normativo de maturidade (inelegibilidade abaixo do alvo)

```
CAPABILITY   : Condicionar a elegibilidade da Spec-filha à homologação ao seu nível-alvo declarado
EFFECT       : Bloqueia a elegibilidade à homologação quando nível_atingido < nível_alvo (efeito sobre
               a governança — publicação do veredito de bloqueio em checks.md/gate)
PRECOND      : (nível atingido computado — EC-HS-001) AND (nível-alvo derivado da complexidade — HS-004)
POSTCOND     : Spec-filha elegível somente se nível_atingido ≥ nível_alvo; caso contrário BLOCKED;
               nada é homologado pelo gate (só Andraus homologa — RULE-HG-03)
POLICY       : RULE-MM-04/05; RULE-HG-06; ENF-04; ROADMAP §12; Q-A3
LEVEL        : E3 (Crítico — gate normativo; abaixo do alvo bloqueia a baseline)
FAILURE-MODE : Fail-closed — ambiguidade sobre o alvo ou o nível atingido ⇒ inelegível; log de rejeição
EVIDENCE     : Registro do par (nível_atingido, nível_alvo) + veredito de elegibilidade; parecer do Revisor
             + método de observação de falso-DENY amostral (ENF-07 — gap aberto)
```

### EC-HS-003 — Detector de gaming (LLM) como sinal, nunca gate

```
CAPABILITY   : Produzir sinal semântico de suspeita de gaming (inflação de documentação) via LLM
EFFECT       : Emite sinal (estado DETECTED) que alimenta o Revisor/gate determinístico
PRECOND      : (o sinal é rotulado como insumo, não veredito) AND (existe gate determinístico a jusante — HS-002)
POSTCOND     : Nenhuma atribuição/elevação de nível decorre isoladamente do LLM (ENF-03)
POLICY       : RULE-MM-02; ENF-03; RULE-MET-01
LEVEL        : E2 (Operacional — produz estado/insumo; sem efeito normativo próprio)
FAILURE-MODE : Fail-closed — sem gate determinístico a jusante, o sinal NÃO altera o nível
EVIDENCE     : Log de estado DETECTED distinto do nível atribuído; rastreabilidade detector→gate
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
O Harness Score / Maturity Model é um **meta-harness de maturidade spec-time** (F.4 Evaluation, atomic-spec §5), executado durante a produção de cada Spec-filha por: Especificador (declara complexidade/nível-alvo), SPEC-020 (fornece resultado das lentes), gate determinístico (atribui nível; aplica o gate normativo), Revisor (audita a atribuição, detector), Andraus (homologa). Não é componente cognitivo de runtime. [FONTE: atomic-spec §5; Q-A3]

### Roteamento de modelo (CEE-001 §5 / EUA-E19)
**N/A como chamada de LLM de runtime** — a SPEC-021 não descreve agente cognitivo que roteia por Tipo I–V. Onde o detector de gaming é apoiado por LLM, é **detector**, não gate (ENF-03). [FONTE: EUA-E19; ENF-03]

### Dependências técnicas
atomic-spec v1.4 (Quality Gates §7; D0–D9; CLASSE-MECH §9/§10.6) · SPEC-019 v1.0 (RULE-HG-06 gate; RULE-HG-03) · SPEC-020 v1.0 (9 lentes / RULE-EV-01..07) · GPR-001 v1.0 (§11 eixo diferente; PE-04; 4Es) · RULES.md (ENF-*, RULE-HG-*, RULE-MECH-01..04) · INV-03/05/07/09. Referências externas [EXTERNO], não-baseline: research.md §2 (M1–M11).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Maturidade vira "contagem de documentos" (Goodhart) | RULE-MM-02; BASpec-HS-006; ADV-HS-01; recomputo determinístico |
| LLM-as-Judge vira gate de nível (colisão ENF-03) | RULE-MM-02; EC-HS-003 fail-closed; ADV-HS-02 |
| Fixar limiar de convicção (fere J-001) | RULE-MM-06; BASpec-HS-007; ADV-HS-04; CONS-01 |
| Redefinir GPR-001 §11 ou Quality Gates | Non-goal; ADV-HS-05; CC-02; nota de escopo (GPR §11 / atomic §7) |
| Redefinir/duplicar as 9 lentes da SPEC-020 | Non-goal; ADV-HS-06; RULE-MM-07 |
| Salto de nível (nível inflado) | RULE-MM-03; ADV-HS-03; staged |
| Rebaixar nível-alvo por Economicidade | RULE-MM-04; ADV-HS-08; 4Es (PB-01>PB-04) |
| Antecipar SPEC-045-RUNTIME-001 / tooling de runtime | Non-goal; fora de escopo (Q-A3/ROADMAP §22) |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz schema lógico "resultado de maturidade de spec" (I/O acima); nenhum schema de runtime alterado.
- **RAG:** nenhum; a maturidade não escreve no KG/RAG.
- **Skills:** nenhuma Skill afetada.
- **Testes:** adiciona item de maturidade ao gate de spec-time de cada Spec-filha (via checks.md); propõe extensão futura de `validate_spec_sot.py`/`harness-score` (tooling; aprovação própria, fora do escopo desta Spec).
- **Modelos dependentes:** SPEC-019/SPEC-020/GPR-001/atomic-spec §7 não alterados (construção SOBRE / acoplamento; a nota de reconciliação em §7 e GPR §11 foi inserida por Andraus, não por esta Spec).
- **Compatibilidade:** **Minor** — adiciona comportamento (RULE-MM + escada + gate) acoplado ao gate existente RULE-HG-06, sem invalidar comportamento vigente; nenhuma RULE existente redefinida.

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07) e declaram Classe por Card (RULE-MECH-01).

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório HIGH)

> SPEC-021 é a **3ª spec** sob o protocolo §7-bis/Passo 5-bis (SPEC-019 → SPEC-020 → SPEC-021). Todos os blocos preenchidos sem economizar, para facilitar a checagem de proporcionalidade (EUA-E18 Q7) que o Revisor conduzirá no relatório desta Spec.

**Bloco A — pergunta adversarial por BASpec HIGH (as BASpecs com efeito):**
- **HS-001 (critérios de nível):** se errada, observável = uma Spec sem D8 recebendo L3 → detectável por comparação artefato-exigido×presente. ENTÃO verificável por observador independente (relatório por nível). Condição QUANDO-satisfeito-mas-ENTÃO-não-deve: um D-level presente-porém-não-verificado (ex.: cenário D7 sem VERIFICADO POR concreto) → tratado: "presente E verificado" exige verificação, não só presença.
- **HS-002 (atribuição determinística):** se errada, observável = nível dependente de julgamento de LLM → detectável pela ausência de estado DETECTED distinto do nível (log). Negação: ADV-HS-02.
- **HS-003 (staged):** se errada, observável = L3 atribuído sobre L1 falho → detectável pela cumulatividade. Negação: ADV-HS-03 + Cenário-HS-T04.
- **HS-005 (gate normativo E3):** se errada, observável = Spec abaixo do alvo homologada → detectável pelo par (atingido<alvo) sem bloqueio. Negação: ADV-HS-07. Condição QUANDO-satisfeito-mas-ENTÃO-não-deve: nível_atingido = nível_alvo (igual) → deve ELIGIBLE (não bloquear); tratado: comparação é "≥", não ">".
- **HS-006 (anti-gaming):** se errada, observável = nível subindo com volume e mesmos D-levels → detectável por recomputo determinístico. Negação: ADV-HS-01 + Cenário-HS-T03.
- **HS-007 (rejeição de limiar de convicção):** se errada, observável = limiar numérico ligado a convicção fixado → viola J-001/CONS-01. Negação: ADV-HS-04 + Cenário-HS-T05.
- **HS-008 (coexistência de scores):** se errada, observável = score por-spec substituindo o repo-global ou redefinindo lentes → detectável pela ausência de um dos scores / lente alterada. Negação: ADV-HS-06.

Todas as sete perguntas respondidas com âncora de fonte; nenhuma BASpec ficou como [DECISÃO NECESSÁRIA] por indefinição adversarial.

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista atomic-spec v1.4 (Quality Gates §7, D0–D9, ENF, CLASSE-MECH), SPEC-019 v1.0 (RULE-HG-06/03/08, RULE-HV), SPEC-020 v1.0 (RULE-EV-01..07 / 9 lentes), GPR-001 v1.0 (§11, PC/PB/PE-04, §15), ENF-01..08, INV-03/05/07/09 (ID+versão — RULE-HD-04). Evidência de satisfação por obrigação herdada: RULE-MM-01 ancora as Quality Gates §7 (reusadas, não redefinidas); RULE-MM-02/HS-006/EC-HS-003 ancoram ENF-03 (Detector≠Gate); RULE-MM-05/EC-HS-002 ancoram RULE-HG-06 (gate) e ENF-04 (fail-closed); RULE-MM-06/HS-007 ancoram INV-03/J-001 (não fixar limiar); RULE-MM-07/HS-008 ancoram SPEC-020 RULE-EV-01 (consome lentes, não redefine); HS-002 registro rastreável ancora PB-05; a nota de eixos distintos ancora GPR-001 §11 (não redefinido). Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (MODIFIED apenas estende os *itens* do gate RULE-HG-06, sem alterar seu texto). **Eixo VERTICAL (RULE-HV) declarado não aplicável** (SPEC-021 é irmã, não filha de SPEC-019/SPEC-020) — coerente com o precedente da SPEC-020 e o alerta ADV-HV-07 da SPEC-019.

**Bloco C — epistêmico (RULE-EPI/CAU/PRB):** nenhuma afirmação causal forte sem mecanismo (a maturidade descreve critérios de atribuição, não causalidade de mercado); nenhuma hipótese tratada como fato (fontes externas [EXTERNO] = DADO, nunca baseline); **INDETERMINADO** usado onde há incerteza material (GAP-1 gaming/Goodhart sem solução fechada; GAP-2 limiares numéricos → J-001) em vez de forçar PASS/FAIL; nenhuma probabilidade/precisão numérica declarada sem base (D4 numérico N/A justificado; níveis ordinais qualitativos — RULE-MM-06). Nenhuma métrica anti-gaming definitiva foi fabricada (RULE-MET-01) — o anti-gaming é ancorado em "presença+verificação, não volume", não numa fórmula inventada.

**Bloco D — reforço de escopo:** a SPEC-021 produz **atribuição/medição de maturidade** (detecção + veredito de elegibilidade), não executa runtime nem emite ordem — INV-05/PC-02/RULE-DEC reconfirmados (§7). Nenhuma BASpec cruza a fronteira SOT→execução downstream. Dependências de decisão de Andraus (homologação de Spec-filha; a própria homologação desta Spec) marcadas como decisão de homologação, não como fato consumado; J-001 e classe B (BL-017) marcados [DECISÃO NECESSÁRIA]/DIFERIDO, não fechados.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| atomic-spec v1.4 (Quality Gates §7); ENF-01..08; INV-03/05/07/09; RULE-MECH-01..04 | [FONTE] | FATO NORMATIVO |
| SPEC-019 v1.0 (RULE-HG-06/03/08); SPEC-020 v1.0 (RULE-EV-01..07); GPR-001 v1.0 (§11/§15) | [FONTE] | FATO NORMATIVO (baseline) |
| Escada canônica L0–L4; RULE-MM-01..07; EC-HS-001..003; BASpec-HS-001..008 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Nota de reconciliação D4 numérico N/A (tratamento de D-levels N/A na atribuição) | [PROPOSTA] | Requer confirmação do Revisor/Andraus |
| Resoluções Q-A1..Q-A7 (research.md §7-bis) | [FONTE] | FATO NORMATIVO (homologadas por Andraus 2026-09-28) |
| Fontes de maturity models M1–M11 (CMMI/SPICE, NIST, DEMM, Goodhart, etc.) | [EXTERNO] | Referência — DADO, nunca baseline (research.md §2) |
| J-001 (limiares definitivos) | [DECISÃO NECESSÁRIA] | Aberto — não tocado (RULE-MM-06) |
| Classe B da SPEC-020 (RAG faithfulness/tool correctness/decision traceability) | [FONTE] | DIFERIDA (BL-017) — não fechada |
| SPEC-045-RUNTIME-001 (tooling de maturidade de runtime) | [DECISÃO NECESSÁRIA] | Aberta separada — não antecipada |
| GAP-1 (gaming/Goodhart); GAP-2 (limiares) | [INFERÊNCIA/EXTERNO] | INDETERMINADO (não fabricar métrica) |

---

## Decisões abertas incidentes (CONS-01 — não fechar sem Andraus)

- **J-001** — fórmula/pesos/limiares definitivos do Conviction Vector — permanece **aberto/pendente**; a maturidade é ordinal/qualitativa e **não** fixa limiar de convicção (RULE-MM-06). [DECISÃO NECESSÁRIA]
- **Classe B da SPEC-020** (BL-017) — **DIFERIDA**; fecha em SPEC-007/038/014; não antecipada.
- **SPEC-045-RUNTIME-001** — caminho/tooling de leitura e telemetria em runtime — **aberta separada**; não antecipada por esta Spec.
- **ECC-VAL-001** (validade geral do Dossiê) — resolvida **só para esta Spec** (Q-A6: 30 dias / início do Plan); regra geral permanece **aberta**.
- **ECC-03-001** (escopo da RULE-ECC-03) — **aberta**; não tocada.

Nenhuma decisão aberta é usada como invariante fechado (CONS-01).

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-021 confirmada como próximo autorizado (§12/§21/§25); FASE GOV posição 3.
[x] atomic-spec.md lido: método v1.4 confirmado (Quality Gates §7 nota de reconciliação; §9/§10.6 CLASSE-MECH; §15).
[x] Nenhum invariante congelado violado (INV-01..10). INV-05 reforçado (maturidade ≠ execução, RULE-DEC).
[x] Constitution Check CC-01..CC-12 preenchido (CC-06/07 N/A justificados; CC-10 N/A justificado; CC-11 INCIDE; CC-12 N/A justificado — meta-harness).
[x] Disciplinas N8–N17: RULE-EPI (INDETERMINADO em GAP-1/2), RULE-MET-01 (não-fabricação de métrica anti-gaming), RULE-DEC (atribuição≠homologação), RULE-CAU/UNC.
[x] Referências externas [EXTERNO] classificadas (research.md §2); rótulos rejeitados (CMMI/SPICE/vendor/LLM-as-Judge-gate) não adotados como baseline; nada vira baseline.
[x] Spec sem implementação; Plan derivado; Tasks adiadas (spec-first).
[x] Critérios em EARS (8); BASpecs completas (HS-001..008) com Classe declarada (CC-11); RULEs citadas existentes (ENF-03/04, RULE-HG-06, RULE-MECH-01..04, RULE-EV-01, INV-*) × propostas (RULE-MM) claramente etiquetadas.
[x] Profundidade D0–D7 atingida (D5 estados; D6 protocolo; D7 cenários x5; D8 adversarial x8 [reforço §7-bis]; D9 por referência). Teto HIGH = D7 respeitado (D8 via §7-bis, não elevação de profile).
[x] Enforcement Contract em todo ato com efeito (EC-HS-001..003); níveis E2/E3; fail-closed; ENF-07 amostral declarado nos E3.
[x] Classe/Mecanismo (RULE-MECH-01): cada BASpec com efeito declara Classe (D/H/C) + critério 4Es + bounded loop/gate de saída onde H/C; nenhuma Classe C em risco baixo (HS-005/HS-007 são E3).
[x] Princípios de Domínio (RULE-PD-01): N/A justificado (meta-harness — CC-12); nenhum PD-xx proposto.
[x] Status epistemológico aplicado (FATO NORMATIVO vs PROPOSTA vs EXTERNO vs DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: J-001 aberta (não fixada); classe B DIFERIDA; SPEC-045-RUNTIME-001 aberta; ECC-VAL-001 regra geral aberta; nenhuma decisão aberta usada como invariante.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos registrados (research.md §4 CONFLITO-1/2/3; GAP-1/2) — não resolvidos em silêncio.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE/EC fabricada como vigente; sem baseline informal.
[x] 4Es na ordem; Conformidade > Eficácia (gate E3 não rebaixado por Economicidade). Latência N/A (maturidade spec-time).
[x] Dependências a montante homologadas (atomic-spec/SPEC-019/SPEC-020/GPR-001/RULES); não downstream de bloqueador aberto (J-001 é adiado, não bloqueia a escada qualitativa).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D) — obrigatório HIGH; 3ª spec sob o protocolo (proporcionalidade Q7 → relatório do Revisor).
[x] Abertura (RULE-ECC-01/02): Dossiê presente e HOMOLOGADO (research.md §7-bis, 2026-09-28); escopo/quantidade/número definidos e homologados; Spec não iniciada só por posição — abertura cumprida.
[x] Passo 11-bis: nenhum gatilho novo disparado; BL-020 ATIVADO (independente, pendente Andraus); BL-017 não dispara; BL-008 independente; BL-021/022/023 Absorvidos (RULE já vigentes).
[ ] Gate determinístico (validate_spec_sot.py) e build_map.py: a rodar no ambiente pai (sem Bash Python confirmado aqui) — reportado ao caller.
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] em aberto nesta Spec (não fechadas — CONS-01): **J-001** (limiares definitivos do Conviction Vector); **classe B** da SPEC-020 (BL-017); **SPEC-045-RUNTIME-001** (tooling de runtime); **ECC-VAL-001** como regra geral; **ECC-03-001**. A homologação plena da SPEC-021 (escada canônica L0–L4 + gate normativo E3 + RULE-MM-01..07) é ato de Andraus, após parecer do Revisor.

**Errata aditiva (2026-10-31, DHR-REAPONT-001):** classe B, RAG faithfulness: F1 → SPEC-007, F2 → SPEC-048 (DIFERIDA) (nota N-E) — ver `governance/ERRATUM-REAPONT-001_Re-apontamento_SPEC-007_para_SPEC-048.md`, nota(s) indicada(s). Texto acima não alterado (INV-09).
