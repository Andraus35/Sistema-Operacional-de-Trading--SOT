# SPEC-002 — Evidence & Evidence Provenance Harness

| Campo | Valor |
|---|---|
| ID | SPEC-002 — Evidence & Evidence Provenance Harness (camada Harness/operacional sobre CEM-001) |
| Versão | 1.0 (candidata) |
| Status | **CANDIDATA — em revisão** (não homologada; homologação é ato de Andraus) |
| Fonte | ROADMAP §4/§21/§29; `research.md` (Dossiê de abertura HOMOLOGADO por Andraus 2026-09-28, §6-bis; RULE-ECC-01/02/04); atomic-spec **v1.5** |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §4; research.md Q-A1] |
| Profundidade-alvo | **D0–D8** (standard + adversarial) [FONTE: research.md Q-A2 homologado; AGENTS.md §4] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 1 — NÚCLEO COGNITIVO; após SPEC-001 (BASELINE) e a FASE GOV (019/020/021, concluída); antes de SPEC-003 [FONTE: ROADMAP §21/§29] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3; teto spec-first (RULE-MM-04/05; gate normativo E3) [FONTE: research.md §5.8(3)] |
| Método | atomic-spec.md **v1.5** (RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET incorporadas; CC-11/CC-12; RULE-MECH-01; RULE-PD-01; RULE-ECC-04; RULE-MM) [FONTE: research.md Q-A5 homologado] |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-09-28 |
| Abertura | Dossiê de Pesquisa HOMOLOGADO por Andraus (research.md §6-bis, 2026-09-28) — Plan iniciado no mesmo dia, dentro da validade do Dossiê (ECC-VAL-001, Q-A6) |

Status: **HOMOLOGADA — BASELINE** (Andraus, 2026-09-28, DHR-SPEC002-001; compat. Minor). Complexidade: CRITICAL. Profundidade-alvo: D0–D8 (standard + adversarial). Conviction Vector: fórmula/pesos/limiares definitivos = **J-001 em aberto** — não fechados aqui. [FONTE: ROADMAP §4; AGENTS.md §4; INV-03]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-09-28 | Entrega candidata inicial. Camada Harness/operacional sobre CEM-001. D0–D8, atomic-spec v1.5. Primeira Spec sob CC-11 (Classe/Mecanismo por BASpec) e RULE-MM (nível-alvo L3). |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; research.md §5.10; RMR-001]

- **RULE-REG-001** (registro físico das 11 famílias cognitivas em `RULES.md`) — gatilho `spec:SPEC-002 em redação`: **DISPAROU na abertura** e foi **HOMOLOGADO por Andraus** junto da definição (research.md §6-bis, Q-A4). As 11 famílias RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET estão fisicamente em `governance/RULES.md` (DHR-REG-001) e o `atomic-spec.md` foi consolidado em **v1.5**. Efeito colateral saneador: os 4 marcadores `[DECISÃO NECESSÁRIA: RULE-REG-001]` em `RULES.md` são resolvidos por esse registro. **Item tratado — não pendente neste gate.** [FONTE: research.md §5.9; RULES.md cabeçalho DHR-REG-001]
- **BL-012** (MC-COG-001 — consolidação cognitiva; gatilho `spec:SPEC-002 homologada`): **NÃO dispara nesta redação** — dispara na **homologação** da SPEC-002. Registrado como **IMINENTE**: no gate de homologação, o MC-COG-001 deve ser tratado (mapear COG-SPEC contra N8–N17; ACHADO R-05/COL-COG-01: usar estados **CHM-001/CEM-001**, nunca os estados §7 do MC-COG; proteger CC-02). Não é ação desta redação e **não bloqueia** o Plan. [FONTE: MEMORY MC-COG-001; RMR-001 BL-012]
- **BL-002** (sintaxe do gatilho registrado no RMR-001: `spec:SPEC-003 homologada` ∨ `decisao:J-001 resolvida` — **J-001 segue em aberto/pendente**, esta citação é só a sintaxe do gatilho, não uma afirmação de fechamento), **BL-003** (`spec:SPEC-004 em redação`), **BL-004** (`spec:SPEC-003 em redação`), **BL-017** (`spec:SPEC-007/014/038 em redação`): **não disparam** (SPEC-002 não é gatilho). [FONTE: RMR-001]
- **BL-024** (CACHING SOT; pré-condição `evento:abertura da SPEC-002`): a pré-condição foi satisfeita na abertura; já **Absorvido** (SPEC-046). Sem ação pendente. [FONTE: research.md §5.10]
- **BL-008** já `Absorvido` (auditoria retroativa da SPEC-001 concluída) — independente desta redação. [FONTE: RMR-001 BL-008]
- Nenhum item fica `ATIVADO` pendente sem encaminhamento por esta redação. O passo 11-bis pleno ocorre na homologação da SPEC-002.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** a SPEC-002 é camada operacional sobre a **Evidência** (objeto neutro de domínio — CEM-001 Princípio 1); não computa análise técnica, não cria hipótese, não inverte a hierarquia. A tipificação de qualidade e o `Domain` da Evidência são **encapsulados no produtor** (CEM-001 Cap.2); a camada de evidência não julga mercado. CC-01 não é tocada. [INFERÊNCIA a partir de CEM-001 Cap.2; INV-01]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** a SPEC-002 **constrói SOBRE** o CEM-001 (BASELINE, DHR-TAX-001) — estrutura, campos, ciclo de vida, linhagem, eventos e governança do objeto Evidência **permanecem intocados**; a Spec especifica apenas o *como opera* (produção, publicação, provenance operacional, qualidade operacional, conflito, tipologia, aging, ciclo de vida operacional). CHM-001 é referenciado apenas na fronteira a jusante (não redefinido). CCM-001 permanece **pendente (SPEC-003)** — nenhum limiar ligado a convicção é fixado. [FONTE: CEM-001; CHM-001; CONST-01; research.md §3.1/§3.4]
- [x] **CC-03 — Conviction Vector:** dimensionalidade=8 permanece **fechada**; fórmula/pesos/limiares definitivos = **J-001 em aberto/pendente** — [DECISÃO NECESSÁRIA]. A SPEC-002 **não** parametriza convicção; `Evidence Strength` permanece peso **local do produtor** (CEM-001 Cap.3), jamais promovido a Convicção (INV-04). Nenhuma escala numérica de qualidade→convicção é adotada. [FONTE: INV-03/INV-04; J-001 pendente; research.md CONFLITO-2]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. INV-04 (custo/força local nunca vira Convicção) é **reforçado** por RULE-EH-003. Salvaguardas de Sinal (§11) não são tocadas (a camada de evidência é a montante do sinal). [FONTE: INV-04; CEE-001 §10/§11]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D8 (ROADMAP §4; AGENTS.md §4).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan (plan.md), não Engineering Card. Os campos §59 e a cadeia §60 tornam-se obrigatórios quando as Tasks/Engineering Cards forem produzidas (BUILD adiado — atomic-spec §14). Omissão justificada. [FONTE: atomic-spec §8.1/§14]
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem provida por ROADMAP §4 → Dossiê (research.md, homologado) → esta Spec.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED preenchidos com ID+versão (RULE-HD-04); REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Eixo VERTICAL (RULE-HV) avaliado e declarado não aplicável (herança é sobre modelo canônico, não decomposição pai→filha de macro-spec) — ver nota na seção de Herança. [FONTE: EUA-E04 §8.3; RULE-HD-02/03/04; RULE-HV]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI):** aplicado — distinção explícita FATO NORMATIVO / FATO ARQUITETURAL / PROPOSTA / INFERÊNCIA / EXTERNO; fontes web tratadas como DADO ([EXTERNO], research.md), nunca baseline; nenhuma hipótese tratada como fato; INDETERMINADO usado onde há incerteza material (GAP-2 fusão de dependentes; ausência de evidência); sem falsa precisão (nenhuma escala numérica de qualidade). [FONTE: RULE-EPI-01..03; research.md §4]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM):** N/A material — o domínio é infraestrutura cognitiva de Evidência (neutro de escola). Termos externos concorrentes (provenance vs lineage; "quality" GRADE vs "strength" CEM) são **declarados e delimitados** (RULE-SEM-01/04): "Evidence Strength" é termo canônico do CEM-001 e **não é redefinido**; "qualidade" externa (GRADE) entra só como referência de método, não substitui o termo canônico. [FONTE: RULE-SEM-01/04; CEM-001 Cap.3; research.md §3.2]
- [x] **CC-11 — Classe/Mecanismo por BASpec com efeito (RULE-MECH-01):** **INCIDE** — a SPEC-002 cita RULE-MECH-01 e é "SPEC-002 em diante". Cada BASpec com efeito declara sua Classe (D/H/P/C) com critério 4Es; Classes H/P declaram bounded loop + critério de parada; Classes H/C declaram gate de saída determinístico. Ver §10.6 aplicado em D3. Declaração por BASpec, nunca por Spec inteira (SES-001 §50). [FONTE: RULE-MECH-01..04; atomic-spec §9/§10.6]
- [x] **CC-12 — Princípios de Domínio `PD-xx` (RULE-PD-01):** **N/A — não incide.** A SPEC-002 é camada Harness/operacional **domain-agnostic** sobre o CEM-001 (CEM-001 Princípio 1 Neutralidade; Cap.2 Neutralidade de Domínio) — **não define escopo de especialidade de mercado** (Elliott/SMC/ICT). Mesmo padrão N/A de SPEC-019/020/021 (governança/meta-harness). `PD-xx` serão declarados pelas Specs analíticas SPEC-010..014. GPR-001 §2.7 permanece vazio até lá. N/A homologado por Andraus (research.md §6-bis, Q-A3) — registrado explicitamente, não supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7; research.md §5.8(2)/§6-bis]

**Disciplinas cognitivas N8–N17 incidentes (RULES.md v1.5):** RULE-EPI (hipótese≠fato; INDETERMINADO — tratamento de ausência/inconclusiva), RULE-CAU-01 (afirmação causal exige mecanismo — usada na detecção de (in)dependência: relação causal entre evidências não se afirma por correlação/co-ocorrência), RULE-MET-01 (não-fabricação — não afirmar independência não verificada nem validação não realizada), RULE-UNC-01..03 (incerteza localizada, não convertida em probabilidade sem base), RULE-PRB-02 (não quantificar sem base — tipificação qualitativa), RULE-DEC-01 (a camada de evidência detecta/representa; não decide nem executa), RULE-SEM-01/04 (termo canônico CEM não redefinido). INDETERMINADO usado onde há incerteza material.

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-002

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - Objeto canônico: CEM-001 (BASELINE, DHR-TAX-001) — Canonical Evidence Model:
      • Cap.3 (contrato: Identidade/Origem/Conteúdo Cognitivo/Rastreabilidade; Evidence Strength
        0.0–1.0 = peso LOCAL do produtor, ≠ Convicção; Producer Type AGENT/ENGINE;
        Evidence Origin Type PRIMARY(só AGENT)/DERIVED(só ENGINE); Lineage: []=PRIMARY,
        obrigatória=DERIVED)
      • Cap.4 (ciclo de vida: ACTIVE→SUPERSEDED/INVALIDATED/ARCHIVED; transições proibidas;
        Status = único campo mutável pós-publicação; avaliação de impacto de invalidação; não-cascata)
      • Cap.5 (linhagem; Cognitive Trace Reconstruction = capacidade do Knowledge Graph;
        Cognitive Depth = métrica derivada)
      • Cap.6 (papéis PRODUCER/CONSUMER/REPOSITORY; eventos Evidence Created/Superseded/
        Invalidated/Archived propagados via EC-COG-005)
      • Cap.7/8 (governança GMC-001; conformidade/certificação)
  - Fronteira a jusante: CHM-001 (BASELINE) — objeto Hipótese; SPEC-001 v1.1 (BASELINE) —
      fronteira Fonte→Dado→Evidência→Hipótese e Registry como serviço lógico (padrão espelhado)
  - Método: atomic-spec.md v1.5 (BASpec, D0–D9, EARS, Enforcement E0–E3/F.1–F.4, TRACE-06,
      Quality Gates L1–L4 §7, Classe/Mecanismo §10.6, RULE-MM §maturidade)
  - Governança do Harness: SPEC-019 v1.0 (BASELINE) — RULE-HG-01..08, RULE-HV-01..04
  - Avaliação/Maturidade: SPEC-020 v1.0 (BASELINE) — 9 lentes/RULE-EV-01..07 (avaliação de spec-time);
      SPEC-021 v1.0 (BASELINE) — RULE-MM-01..07 (escada de maturidade por-Spec; nível-alvo L3)
  - Enforcement: ENF-01..08 — com ênfase em ENF-03 (Detector ≠ Gate; LLM nunca é seu próprio gate)
  - Invariantes: INV-04 (custo/força local fora do Conviction Vector), INV-06 (Evidência≠Observação),
      INV-07 (versionamento monotônico), INV-09 (sem baseline informal), INV-10 (CEM-001 = idioma)
  - Regras existentes: RULE-004 (evidências causalmente relacionadas contadas como uma),
      RULE-BB-002/004 (publicação em workspace próprio; append-only), RULE-MET-01, RULE-EPI-01..03,
      RULE-CAU-01, RULE-UNC-01..03, RULE-PRB-02, RULE-SEM-01/04, RULE-DEC-01
  - Princípios/4Es: CEE-001 §12 (Conformidade > Eficácia > Efetividade > Eficiência > Economicidade)

ADDED (delta local — o que esta spec acrescenta):
  - Evidence Registry como serviço lógico (alocação de ID, versionamento monotônico operacional,
    índice de estado ativo, API de consulta/reconstrução histórica) — espelho operacional do
    Hypothesis Registry (SPEC-001)
  - Protocolo operacional de produção/publicação de Evidência (D6) referenciando o contrato CEM-001
  - Camada operacional de provenance (rastreabilidade produtor→fonte→dado→evidência; ferramenta/Skill
    que produziu; INV-06 como gate de publicação)
  - Uso operacional de qualidade/força (tipificação qualitativa; guard anti-promoção a Convicção)
  - Representação operacional de (in)dependência entre evidências (anti-double-counting) — só o atributo
  - Tipologia operacional favorável/contra/inconclusiva/AUSENTE (ausência ≠ evidência de ausência)
  - Detecção e REGISTRO de conflito de evidência (nunca resolução — fronteira SPEC-003/014)
  - Temporalidade/aging operacional (representação de staleness; peso temporal adiado a J-001)
  - Ciclo de vida operacional e protocolo de avaliação de impacto de invalidação (referenciando CEM-001)
  - Declaração de Classe/Mecanismo por BASpec (CC-11) — primeira Spec sob RULE-MECH-01
  - Enforcement Contracts dos atos com efeito (EC-EH-001..005)

MODIFIED (especialização de regra herdada):
  - RULE-004 (evidências causalmente relacionadas = uma só) — a SPEC-002 ESTENDE seu alcance
    operacional: representa o atributo de (in)dependência e obriga honestidade metacognitiva
    (RULE-MET-01) sobre independência não verificada, SEM alterar o texto de RULE-004 nem antecipar
    a MECÂNICA de desconto (que é da SPEC-003). Extensão de cobertura, não de significado.

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal / obrigação-a-obrigação** sobre **modelos canônicos e método** (EUA-E04 §8.3). O eixo **VERTICAL** (RULE-HV-01..04, conservação-como-conjunto pai→filha macro-harness) foi avaliado e **não se aplica**: a SPEC-002 não é decomposição *micro* de uma *macro-spec* — ela deriva de modelos canônicos (CC-08), não de uma macro-spec da FASE GOV. A regra ESCRITA de conservação-como-conjunto vertical será redigida junto da SPEC-019/SPEC-019-derivadas; aqui não é invocada. [INFERÊNCIA — a confirmar pelo Revisor]

---

## D0 — Missão (Intenção)

A SPEC-002 especifica **como o SOT produz, publica, versiona, rastreia (provenance), qualifica, relaciona e encerra Evidências Cognitivas em operação** — a camada Harness/operacional sobre o **CEM-001** (BASELINE, não redefinido). Garante: rastreabilidade **Fonte→Dado→Evidência**; representação explícita de evidência **favorável / contra / inconclusiva / AUSENTE**; e **detecção e registro** (nunca resolução silenciosa) de **conflito** e de **(in)dependência** entre evidências — com **gate determinístico** e o LLM apenas como **detector** (ENF-03). [FONTE: ROADMAP §4; research.md §5.2]

A camada opera do lado da **Evidência**: produção/publicação, provenance operacional, qualidade/força operacional (local, ≠ Convicção), independência (representação), tipologia, conflito (detecção/registro), temporalidade/aging e ciclo de vida operacional. Constrói SOBRE o CEM-001 no mesmo padrão em que a SPEC-001 constrói sobre o CHM-001. [FONTE: research.md §3.1; ROADMAP §101]

**O que a Missão NÃO é (fronteira):**
- Não redefine CEM-001 (estrutura, campos, ciclo de vida, linhagem, eventos, governança) nem CHM-001 → **CC-02/CONST-01**.
- Não computa **fusão** de evidências nem produz evidência DERIVED → **SPEC-003 (Fusion Engine)**.
- Não calcula convicção nem fixa limiar numérico → **SPEC-003 / J-001 / CCM-001**.
- Não fecha **estados do Blackboard** para objetos não-hipótese → **M-001 / SPEC-004** (aberta).
- Não define **storage físico** de evidência (Blackboard/KG) nem Cognitive Trace Reconstruction → **SPEC-004 / SPEC-006 / H-001**.
- Não **resolve** conflito de evidência → **SPEC-003 / SPEC-014**.

**Status epistemológico:** a SPEC-002 é FATO ARQUITETURAL candidato a baseline. CEM-001, CHM-001, SPEC-001 v1.1, SPEC-019/020/021, atomic-spec v1.5, INV-*, ENF-*, RULES v1.5 são FATO NORMATIVO. Fontes externas (research.md §2, SRC-01..06) são [EXTERNO] — DADO, nunca baseline; documentado ≠ homologado (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | **Evidence Registry** como serviço lógico: alocação de ID, versionamento monotônico operacional, índice de estado ativo, API de consulta/reconstrução histórica (storage físico → SPEC-004/006) | ROADMAP §4; research.md §5.3(1) |
| S2 | **Protocolo de produção/publicação** de Evidência (D6) referenciando o contrato CEM-001; fronteira produtor PRIMARY (Agente) vs DERIVED (Fusion Engine — só contrato de fronteira) | CEM-001 Cap.2/Cap.6; research.md §5.3(2) |
| S3 | **Camada operacional de provenance**: produtor→fonte→dado→evidência; ferramenta/Skill que produziu; INV-06 como gate | CEM-001 Cap.4/Cap.5; INV-06; research.md §5.3(3) |
| S4 | **Qualidade/força operacional**: uso de `Evidence Strength` (local) SEM promoção a Convicção (INV-04); tipificação qualitativa (adaptada de GRADE) | CEM-001 Cap.3; INV-04; research.md §5.3(4) |
| S5 | **(In)dependência** como atributo operacional representado (anti-double-counting — RULE-004); mecânica de desconto/fusão adiada (SPEC-003) | RULE-004; research.md §5.3(5) |
| S6 | **Tipologia**: favorável / contra / inconclusiva / **AUSENTE** — representação distinta (ausência ≠ evidência de ausência) | RULE-EPI/UNC/MET; research.md §5.3(6) |
| S7 | **Detecção e registro de conflito** de evidência (PB-09) — nunca resolução | ENF-03; research.md §5.3(7) |
| S8 | **Temporalidade/aging operacional** (representação de staleness; peso temporal → J-001) | CEM-001 Cap.3; research.md §5.3(8) |
| S9 | **Ciclo de vida operacional** (ACTIVE→SUPERSEDED→INVALIDATED→ARCHIVED) e protocolo de avaliação de impacto de invalidação referenciando CEM-001 Cap.4/Cap.5 | CEM-001 Cap.4/Cap.5; research.md §5.3(9) |
| S10 | **Protocolo de publicação no Blackboard** para Evidência (D6) — referenciando M-001 como decisão aberta (não fecha estados) | RULE-BB-002/004; M-001; research.md §5.3(10) |
| S11 | **Enforcement Contracts** dos atos com efeito: piso **E2** (Evidência/Agente); **E3** onde há commit crítico/irreversível (invalidação de ciclo de vida) | ENF-01/02; atomic-spec §10.2 |
| S12 | **Auditabilidade (D9 por referência)**: o que a camada deve suportar para reconstrução (P13), delegando Cognitive Trace Reconstruction ao KG (SPEC-006) | CONSTITUTION P13; CEM-001 Cap.5 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Redefinir CEM-001 (estrutura/campos/ciclo/linhagem/eventos/governança) ou CHM-001 | CEM-001 / CHM-001 (BASELINE) | CC-02/CONST-01 |
| Fórmula/mecânica de **fusão** de evidências e cálculo de evidência DERIVED | **SPEC-003** (Fusion Engine) | Só o contrato de fronteira PRIMARY/DERIVED é declarado aqui |
| Conviction Vector / convicção a partir de evidência; qualquer limiar numérico | **SPEC-003 / J-001 / CCM-001** | J-001 aberto — [DECISÃO NECESSÁRIA]; INV-04 |
| **Estados do Blackboard** para objetos não-hipótese | **M-001 / SPEC-004** | M-001 em aberto — pendente; não fechar (CONS-01) |
| **Storage físico** de evidência e Cognitive Trace Reconstruction | **SPEC-004 / SPEC-006 / H-001** | Infraestrutura; H-001 em aberto — pendente |
| RAG / evidence candidate a partir de retrieval | **SPEC-007** | Fase 3 |
| Estrutura da hipótese e transição a jusante | **CHM-001 / SPEC-001** | Já especificado; a SPEC-002 opera do lado da Evidência |
| **Resolução** de conflito de evidência | **SPEC-003 / SPEC-014** | ENF-03: a camada de evidência detecta/registra, não resolve |
| Adotar modelo externo de provenance (W3C PROV/OpenLineage) ou escala numérica GRADE como baseline | — | Rejeitados como baseline (research.md §4 CONFLITO-2/3); só referência de método |

---

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide.** A SPEC-002 não define escopo de especialidade de mercado; é camada Harness/operacional **domain-agnostic** sobre o CEM-001 (neutro de domínio por construção — CEM-001 Princípio 1). Nenhum `PD-xx` é proposto (CC-12 = N/A homologado, research.md §6-bis Q-A3). Registrado explicitamente para o Revisor — não é supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7]

---

## D2 — Regras

> **Etiqueta:** as RULE-EH-* abaixo são **[PROPOSTA]** — tornam-se normativas apenas na homologação de Andraus + registro no `RULES.md` pelo Controlador (RULE-HG-02). Até lá, não são invocáveis como FATO NORMATIVO. As RULE/INV/ENF citadas como fundamento (CEM-001, INV-04/06/07/10, ENF-03, RULE-004, RULE-EPI/CAU/MET/UNC/PRB, RULE-BB-002/004) **já existem** e são FATO NORMATIVO (RULES.md v1.5).

```
RULE-EH-001: Somente produtores autorizados pelo CEM-001 publicam Evidência: AGENT produz PRIMARY;
             Fusion Engine (ENGINE) produz DERIVED. Skill produz OBSERVAÇÃO, nunca Evidência.
             Publicação por produtor não autorizado é rejeitada (fail-closed).
             [Fonte: CEM-001 Cap.2/Cap.6; INV-06]  [PROPOSTA]

RULE-EH-002: Toda Evidência publicada DEVE satisfazer integralmente o contrato do CEM-001 Cap.3
             (Identidade + Origem + Conteúdo Cognitivo + Rastreabilidade completos; Lineage=[] p/ PRIMARY,
             obrigatória p/ DERIVED; PRIMARY⇒AGENT, DERIVED⇒ENGINE). Publicação incompleta é rejeitada.
             [Fonte: CEM-001 Cap.3; INV-10]  [PROPOSTA]

RULE-EH-003: Evidence Strength é peso LOCAL do produtor; NÃO DEVE ser agregado nem promovido a
             Convicção (INV-04). Qualidade é tipificada QUALITATIVAMENTE; nenhuma escala numérica
             de qualidade ligada a convicção é fixada (J-001 aberto).
             [Fonte: CEM-001 Cap.3; INV-04; J-001; RULE-PRB-02]  [PROPOSTA]

RULE-EH-004: Cada Evidência DEVE ter sua tipologia representada distintamente — favorável / contra /
             inconclusiva / AUSENTE. Ausência de evidência NÃO DEVE ser convertida em evidência de
             ausência nem em conclusão; trata-se sob RULE-EPI/UNC/MET (INDETERMINADO quando aplicável).
             [Fonte: RULE-EPI-01; RULE-UNC-03; RULE-MET-01]  [PROPOSTA]

RULE-EH-005: (In)dependência entre evidências é ATRIBUTO representado, não resolvido. O sistema NÃO DEVE
             afirmar independência que não verificou (RULE-MET-01); dependência causal não se afirma por
             mera co-ocorrência/correlação (RULE-CAU-01). A MECÂNICA de desconto/fusão é da SPEC-003.
             [Fonte: RULE-004; RULE-MET-01; RULE-CAU-01]  [PROPOSTA]

RULE-EH-006: Conflito entre evidências DEVE ser DETECTADO e REGISTRADO, nunca resolvido silenciosamente
             na camada de evidência. O LLM é DETECTOR, não gate (ENF-03); a resolução pertence a
             Fusion→Conviction→Synthesis (SPEC-003/014). Conflito registrado nunca é suprimido.
             [Fonte: ENF-03; RULE-MET-01; PB-09]  [PROPOSTA]

RULE-EH-007: O ciclo de vida operacional segue o CEM-001 Cap.4 (ACTIVE→SUPERSEDED/INVALIDATED/ARCHIVED;
             transições proibidas rejeitadas; Status é o único campo mutável). A invalidação propaga o
             evento Evidence Invalidated (EC-COG-005) e inicia avaliação de impacto SEM cascata automática.
             [Fonte: CEM-001 Cap.4/Cap.5; INV-07]  [PROPOSTA]

RULE-EH-008: Versionamento é monotônico e a Evidência é imutável após publicação (Status excetuado);
             evolução cria nova Evidência e transita a anterior para SUPERSEDED. Nada é deletado.
             [Fonte: CEM-001 Cap.4; INV-07; RULE-BB-004]  [PROPOSTA]
```

---

## Critérios de Aceitação (EARS)

1. Quando um AGENT autorizado solicita a publicação de uma Evidência PRIMARY completa (contrato CEM-001 Cap.3), o Evidence Harness DEVE alocar `evidence_id`, versão inicial e publicar em estado ACTIVE.
2. Quando uma Skill (produtor de Observação) tenta publicar uma Evidência, o Evidence Harness DEVE rejeitar a operação (INV-06), pois Observação ≠ Evidência.
3. Quando uma Evidência é submetida sem uma das quatro camadas obrigatórias do CEM-001 (ou com Lineage incoerente com o Origin Type), o Evidence Harness DEVE rejeitar a publicação (fail-closed).
4. Quando um consumidor tenta agregar `Evidence Strength` como convicção, o Evidence Harness DEVE rejeitar a promoção (INV-04) e manter Strength como peso local.
5. Quando uma Evidência é registrada, o Evidence Harness DEVE representar sua tipologia (favorável/contra/inconclusiva/AUSENTE) de forma distinta; e NÃO DEVE converter AUSENTE em conclusão.
6. Quando duas evidências apresentam conteúdo conflitante, o Evidence Harness DEVE detectar e registrar o conflito, mas NÃO DEVE resolvê-lo (resolução → SPEC-003/014).
7. Quando o detector de (in)dependência não consegue verificar independência, o Evidence Harness DEVE declarar a limitação (RULE-MET-01), NÃO DEVE afirmar independência.
8. Quando uma Evidência transita para INVALIDATED, o Evidence Harness DEVE propagar o evento Evidence Invalidated e iniciar avaliação de impacto SEM cascata automática sobre derivadas.
9. Quando um agente tenta uma transição proibida do ciclo de vida (ex.: INVALIDATED→ACTIVE), o Evidence Harness DEVE rejeitar a operação e preservar o objeto (INV-07).

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec com efeito declara o bloco **CLASSE/MECANISMO** (§10.6). Classe D = determinístico; C = constitutivo (é o próprio gate); H = híbrido (LLM + gate de saída determinístico + bounded loop); P = probabilístico com gate (julgamento + critério de parada).

### BASpec-EH-001 — Alocação de ID e versionamento monotônico (Evidence Registry)

```
BASpec-EH-001:
  QUANDO:       Um produtor autorizado submete uma Evidência nova ou uma nova versão de Evidência existente
  ENTÃO:        Evidence Registry aloca evidence_id único e imutável (versão inicial) OU incrementa a
                versão preservando a anterior (previous_version_id), de forma monotônica e append-only
  PORQUE:       Identidade única e versionamento monotônico são invariantes do objeto (CEM-001 Cap.3/Cap.4; INV-07)
  REFERÊNCIA:   CEM-001 Cap.3/Cap.4; INV-07; RULE-EH-001; RULE-EH-008
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : geração/registro por regra (ID único; sequência de versão monotônica); sem julgamento
    CRITÉRIO 4Es: Eficácia — identidade e histórico corretos são pré-condição de toda rastreabilidade;
                  determinismo garante reprodutibilidade da reconstrução (P13)
  VERIFICADO POR:
    DADO        Evidência EV nova de um AGENT autorizado, sem versão anterior
    QUANDO      o Registry processa a submissão
    ENTÃO       retorna evidence_id != null, version = 1, previous_version_id = null
    VERIFICAÇÃO ev.evidence_id != null; ev.version == 1
```

### BASpec-EH-002 — Gate de conformidade CEM-001 na publicação

```
BASpec-EH-002:
  QUANDO:       Uma Evidência é submetida para publicação no Blackboard
  ENTÃO:        O Harness verifica o contrato CEM-001 Cap.3 (4 camadas completas; PRIMARY⇒AGENT;
                DERIVED⇒ENGINE; Lineage=[] p/ PRIMARY e obrigatória p/ DERIVED); se qualquer condição
                falha, REJEITA a publicação (fail-closed) com código específico e nenhuma Evidência é publicada
  PORQUE:       Nenhuma Evidência fora do contrato canônico pode circular (CEM-001 Cap.3; INV-10)
  REFERÊNCIA:   CEM-001 Cap.3/Cap.6; INV-10; RULE-EH-002
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : enforcement determinístico de conformidade de contrato; é o próprio gate de publicação
    GATE DE SAÍDA: checagem determinística de presença/coerência dos campos do CEM-001 Cap.3
    CRITÉRIO 4Es: Conformidade > Eficácia — contrato canônico é inviolável; risco alto (integridade do idioma)
  VERIFICADO POR:
    DADO        Evidência PRIMARY sem campo Technical Rationale
    QUANDO      o gate de conformidade é aplicado
    ENTÃO       publicação REJEITADA, código "CEM_CONTRACT_INCOMPLETE"; nada publicado
    VERIFICAÇÃO response.error_code == "CEM_CONTRACT_INCOMPLETE"; Blackboard.evidence_count inalterado
```

### BASpec-EH-003 — INV-06: Observação de Skill não é Evidência

```
BASpec-EH-003:
  QUANDO:       Uma Skill (produtor stateless de Observação) tenta publicar um objeto como Evidência
  ENTÃO:        O Harness REJEITA a operação (fail-closed) com código "SKILL_NOT_EVIDENCE_PRODUCER";
                Observação não é promovida a Evidência
  PORQUE:       Evidência (Agente/Engine, interpretada) ≠ Observação (Skill, determinística) — INV-06
  REFERÊNCIA:   INV-06; CEM-001 Cap.2; RULE-EH-001
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico sobre producer_type/producer_id ∈ AUTHORIZED_EVIDENCE_PRODUCERS
    GATE DE SAÍDA: verificação binária de autorização de produtor (é o gate)
    CRITÉRIO 4Es: Conformidade > Eficácia — proteger a fronteira Observação/Evidência (INV-06)
  VERIFICADO POR:
    DADO        Skill "fibo-levels" tenta publicar objeto como Evidência
    QUANDO      o gate de produtor é aplicado
    ENTÃO       operação REJEITADA, código "SKILL_NOT_EVIDENCE_PRODUCER"
    VERIFICAÇÃO response.error_code == "SKILL_NOT_EVIDENCE_PRODUCER"
```

### BASpec-EH-004 — Provenance operacional (produtor→fonte→dado→evidência)

```
BASpec-EH-004:
  QUANDO:       Uma Evidência é publicada
  ENTÃO:        O Harness exige provenance operacional completa: producer_type/producer_id,
                Source Reference (origem informacional), ferramenta/Skill que gerou a Observação de base
                e Lineage coerente com o Origin Type; provenance incompleta = rejeição (fail-closed)
  PORQUE:       Rastreabilidade Fonte→Dado→Evidência é obrigatória (CEM-001 Cap.4/Cap.5; P13)
  REFERÊNCIA:   CEM-001 Cap.4/Cap.5; CONSTITUTION P13; RULE-EH-002
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de presença/coerência de provenance
    GATE DE SAÍDA: verificação de Source Reference + producer + Lineage (é o gate)
    CRITÉRIO 4Es: Eficácia — provenance é pré-condição da auditabilidade (P13) e da avaliação de impacto
  VERIFICADO POR:
    DADO        Evidência DERIVED com Lineage vazia
    QUANDO      o gate de provenance é aplicado
    ENTÃO       publicação REJEITADA, código "PROVENANCE_INCOMPLETE" (DERIVED exige Lineage)
    VERIFICAÇÃO response.error_code == "PROVENANCE_INCOMPLETE"
```

### BASpec-EH-005 — Guard anti-promoção de Strength a Convicção (INV-04)

```
BASpec-EH-005:
  QUANDO:       Um consumidor ou processo tenta usar Evidence Strength como (ou agregá-lo em) Convicção
  ENTÃO:        O Harness REJEITA a promoção (fail-closed) com código "STRENGTH_IS_NOT_CONVICTION";
                Strength permanece peso local; a qualidade é tipificada qualitativamente
  PORQUE:       Custo/força local NUNCA entram no Conviction Vector; Convicção pertence ao CCM-001/SPEC-003 (INV-04; J-001)
  REFERÊNCIA:   INV-04; CEM-001 Cap.3; J-001; RULE-EH-003
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que barra promoção Strength→Convicção
    GATE DE SAÍDA: verificação de que nenhum campo de convicção é derivado de Strength nesta camada
    CRITÉRIO 4Es: Conformidade > Eficácia — INV-04 é inviolável; não antecipar J-001
  VERIFICADO POR:
    DADO        consumidor tenta computar conviction_dimension a partir de Evidence Strength
    QUANDO      o guard é aplicado
    ENTÃO       operação REJEITADA, código "STRENGTH_IS_NOT_CONVICTION"
    VERIFICAÇÃO response.error_code == "STRENGTH_IS_NOT_CONVICTION"
```

### BASpec-EH-006 — Detector de (in)dependência entre evidências (anti-double-counting)

```
BASpec-EH-006:
  QUANDO:       Duas ou mais evidências candidatas apresentam relação potencial de dependência (mesma
                fonte/dado, linhagem compartilhada, co-ocorrência)
  ENTÃO:        O Harness executa um detector que REPRESENTA o atributo de (in)dependência (independent |
                dependent | undetermined); quando não consegue verificar independência, marca "undetermined"
                e declara a limitação — NÃO afirma independência; NÃO aplica desconto (mecânica → SPEC-003)
  PORQUE:       Evidências causalmente relacionadas devem contar como uma (RULE-004); não fabricar
                independência não verificada (RULE-MET-01); dependência causal não se afirma por correlação (RULE-CAU-01)
  REFERÊNCIA:   RULE-004; RULE-MET-01; RULE-CAU-01; RULE-EH-005
  CLASSE/MECANISMO:
    CLASSE      : P (Probabilístico com Gate)
    MECANISMO   : detector (heurístico + apoio semântico/LLM) que produz o atributo; ENF-03 (detector≠gate)
    BOUNDED LOOP: uma passada por par de evidências candidatas; sem re-tentativa recursiva; encerra em
                  "undetermined" quando a evidência discriminante é insuficiente (RULE-INQ-03) — sem retry infinito
    CRITÉRIO 4Es: Eficácia — evitar double counting protege a qualidade da fusão a jusante; honestidade
                  (Conformidade) prevalece sobre completar o atributo
  VERIFICADO POR:
    DADO        EV-1 e EV-2 derivadas da mesma Observação de fonte única, sem discriminante de independência
    QUANDO      o detector de (in)dependência roda
    ENTÃO       atributo = "undetermined"; limitação registrada; nenhuma afirmação de independência
    VERIFICAÇÃO relationship_attribute == "undetermined"; independence_claimed == false
```

### BASpec-EH-007 — Tipologia favorável/contra/inconclusiva/AUSENTE

```
BASpec-EH-007:
  QUANDO:       Uma Evidência é registrada em relação a uma questão/hipótese-alvo referenciada
  ENTÃO:        O Harness representa distintamente a tipologia (favorável | contra | inconclusiva |
                AUSENTE); AUSENTE (evidência esperada e não encontrada) é representada como categoria
                própria e NÃO é convertida em conclusão nem em "evidência de ausência"
  PORQUE:       Ausência de evidência ≠ evidência de ausência; preservar incerteza (RULE-EPI/UNC/MET);
                inconclusiva ≠ contra
  REFERÊNCIA:   RULE-EPI-01; RULE-UNC-03; RULE-MET-01; RULE-EH-004
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : classificação semântica (LLM) da relação evidência↔questão + gate determinístico que
                  garante representação nas 4 categorias distintas e barra conversão de AUSENTE em conclusão
    BOUNDED LOOP: classificação em passo único por evidência; sem re-tentativa; INDETERMINADO se ambígua
    GATE DE SAÍDA: verificação determinística de que a categoria pertence ao enum e AUSENTE não vira conclusão
    CRITÉRIO 4Es: Eficácia — distinguir AUSENTE/inconclusiva preserva a integridade epistêmica a jusante
  VERIFICADO POR:
    DADO        questão espera evidência institucional de sweep e nenhuma é encontrada no timeframe
    QUANDO      o Harness classifica a tipologia
    ENTÃO       typology = "AUSENTE"; nenhuma conclusão "não houve manipulação" é derivada
    VERIFICAÇÃO typology == "AUSENTE"; derived_conclusion_from_absence == false
```

### BASpec-EH-008 — Detecção e registro de conflito (nunca resolução)

```
BASpec-EH-008:
  QUANDO:       Duas evidências ACTIVE apresentam interpretações materialmente conflitantes
  ENTÃO:        O Harness DETECTA e REGISTRA o conflito (conflict_record com as evidências envolvidas),
                sinaliza-o como insumo para Fusion/Conviction/Synthesis, e NÃO o resolve; o conflito
                registrado nunca é suprimido
  PORQUE:       Conflito é registrado e nunca suprimido (PB-09); LLM é detector viesado na resolução
                (SRC-03 [EXTERNO]) — resolução pertence à SPEC-003/014 (ENF-03)
  REFERÊNCIA:   ENF-03; RULE-MET-01; PB-09; RULE-EH-006; [EXTERNO] research.md SRC-03
  CLASSE/MECANISMO:
    CLASSE      : P (Probabilístico com Gate)
    MECANISMO   : detector (semântico/LLM) de conflito → sinal; gate determinístico apenas registra e
                  encaminha; ENF-03 (o LLM nunca resolve/aprova o conflito)
    BOUNDED LOOP: uma avaliação por par de evidências; encerra registrando o conflito; sem loop de resolução
    CRITÉRIO 4Es: Conformidade > Eficácia — não resolver na camada errada (ENF-03) prevalece sobre "fechar" o conflito
  VERIFICADO POR:
    DADO        EV-A (bullish, institucional) e EV-B (bearish, institucional), ambas ACTIVE
    QUANDO      o detector de conflito roda
    ENTÃO       conflict_record criado; status = "REGISTERED_UNRESOLVED"; nenhuma resolução aplicada
    VERIFICAÇÃO conflict.status == "REGISTERED_UNRESOLVED"; resolved_by_evidence_layer == false
```

### BASpec-EH-009 — Temporalidade/aging operacional (staleness)

```
BASpec-EH-009:
  QUANDO:       Uma Evidência ACTIVE é consultada após decorrido tempo desde seu Creation Timestamp
  ENTÃO:        O Harness representa o staleness operacional (idade relativa ao Timeframe Reference) como
                atributo derivado; NÃO fixa peso/decay numérico ligado a convicção (adiado a J-001)
  PORQUE:       Aging é representação operacional; o peso/decay temporal na convicção pertence a J-001/SPEC-003 (RULE-PRB-02)
  REFERÊNCIA:   CEM-001 Cap.3 (Timeframe Reference/Creation Timestamp); J-001; RULE-PRB-02; RULE-EH-003
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : cálculo determinístico de idade relativa (timestamp × Timeframe Reference) → atributo qualitativo/ordinal
    CRITÉRIO 4Es: Eficiência — representação barata e reprodutível; sem antecipar J-001 (Conformidade preserva CC-03)
  VERIFICADO POR:
    DADO        Evidência com Timeframe Reference = H1 criada há muitas barras H1
    QUANDO      o cálculo de staleness roda
    ENTÃO       staleness_flag setado (ordinal: fresh/aging/stale); nenhum peso numérico de convicção atribuído
    VERIFICAÇÃO staleness computed == true; conviction_weight_assigned == false
```

### BASpec-EH-010 — Transição de ciclo de vida e avaliação de impacto de invalidação

```
BASpec-EH-010:
  QUANDO:       Uma Evidência ACTIVE é submetida a uma transição de estado (SUPERSEDED/INVALIDATED/ARCHIVED)
  ENTÃO:        O Harness valida a transição contra o grafo do CEM-001 Cap.4 (transições proibidas
                rejeitadas — fail-closed); se INVALIDATED, propaga o evento Evidence Invalidated (EC-COG-005)
                e inicia avaliação de impacto sobre derivadas SEM cascata automática; o objeto é preservado (INV-07)
  PORQUE:       Ciclo de vida e não-cascata são do CEM-001 Cap.4/Cap.5; transição irreversível exige gate crítico (INV-07)
  REFERÊNCIA:   CEM-001 Cap.4/Cap.5; INV-07; RULE-EH-007; RULE-EH-008
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de transição (grafo canônico) + emissão de evento; é o próprio gate
    GATE DE SAÍDA: verificação binária de que a transição pertence ao grafo permitido do CEM-001 Cap.4
    CRITÉRIO 4Es: Conformidade > Eficácia — transição de estado é irreversível (INVALIDATED→ACTIVE proibida); risco alto
  VERIFICADO POR:
    DADO        Evidência EV em INVALIDATED
    QUANDO      agente tenta transicionar EV para ACTIVE
    ENTÃO       transição REJEITADA, código "LIFECYCLE_TRANSITION_FORBIDDEN"; EV preservada
    VERIFICAÇÃO response.error_code == "LIFECYCLE_TRANSITION_FORBIDDEN"; Blackboard.contains(EV) == true
```

---

## D4 — Algoritmo

**Majoritariamente N/A como fórmula numérica.** A camada é constitutiva/representacional e **qualitativa**: fixar escores numéricos (qualidade, peso de aging, desconto de dependência) dependeria de limiares ligados a convicção — **J-001, em aberto** (RULE-EH-003; INV-03/CONS-01). A única mecânica determinística real é a de **BASpec-EH-001** (alocação de ID/versão monotônica) e **BASpec-EH-009** (idade relativa = função de `Creation Timestamp` e `Timeframe Reference`), ambas sem fórmula de convicção. A omissão de D4 numérico de qualidade/desconto é **justificada** (atomic-spec §2: D4 "onde há regra determinística real"; a mecânica de desconto/fusão é da SPEC-003). [FONTE: J-001; atomic-spec §2; research.md GAP-2]

---

## D5 — Máquina de estados do ciclo de vida da Evidência (CEM-001 Cap.4 — não redefinido)

A máquina de estados da Evidência é a do **CEM-001 Cap.4** — a SPEC-002 **não redefine**; apenas opera sobre ela. Diferente da hipótese (CHM-001, 7 estados), a Evidência **nasce em ACTIVE** (estado padrão) — não há EMERGENT/CANDIDATE.

| Estado | Descrição | Elegível p/ inferência/fusão? |
|---|---|---|
| ACTIVE | Estado padrão; válida e disponível | **Sim** |
| SUPERSEDED | Substituída por versão mais recente; auditável | Não |
| INVALIDATED | Incorreta/não representativa; preserva histórico de erro | Não |
| ARCHIVED | Fora da camada operacional; consulta histórica | Não |

### Grafo de transições permitidas [FONTE: CEM-001 Cap.4]

```
ACTIVE      -> SUPERSEDED | INVALIDATED | ARCHIVED
SUPERSEDED  -> ARCHIVED
INVALIDATED -> ARCHIVED
```

### Transições proibidas (rejeitadas — fail-closed) [FONTE: CEM-001 Cap.4]

```
INVALIDATED -> ACTIVE
ARCHIVED    -> ACTIVE
SUPERSEDED  -> ACTIVE
```

**Não-cascata [FONTE: CEM-001 Cap.4/Cap.5]:** a invalidação de uma Evidência ancestral **não** invalida automaticamente as derivadas — o Fusion Engine inicia avaliação de impacto; a decisão de manter/substituir/invalidar segue as regras de linhagem. A avaliação de impacto sobre hipóteses/convicções/decisões pertence aos respectivos modelos (CHM/CCM/CDM), não à SPEC-002.

---

## D6 — Protocolo de publicação no Blackboard

### Workspace e produtores [FONTE: RULE-BB-002; CEM-001 Cap.6]

Evidências são publicadas no workspace de Evidência do Blackboard Cognitivo, apenas por produtores autorizados no workspace de sua responsabilidade (RULE-BB-002).

| Produtor | Origin Type | Publica |
|---|---|---|
| AGENT (Structural, Institutional, Macro, Sentiment, Risk, Context, Operational) | PRIMARY | Evidência |
| Fusion Engine (ENGINE) | DERIVED | Evidência (mecânica → SPEC-003) |
| Skill | — | Observação (NÃO Evidência — INV-06) |

### Sequência de publicação

1. **Submissão:** produtor submete Evidência candidata.
2. **Gate de produtor (EH-001/EH-003):** producer autorizado? Skill = rejeição (INV-06).
3. **Gate de contrato (EH-002):** 4 camadas CEM-001 Cap.3 completas; PRIMARY⇒AGENT/DERIVED⇒ENGINE; Lineage coerente.
4. **Gate de provenance (EH-004):** Source Reference + producer + Lineage.
5. **Alocação (EH-001):** Evidence Registry aloca `evidence_id`, `version=1` (ou `n+1`).
6. **Publicação:** objeto publicado em estado ACTIVE (append-only — RULE-BB-004).
7. **Evento:** Evidence Created emitido (EC-COG-005).
8. **Representação operacional:** tipologia (EH-007), (in)dependência (EH-006), staleness (EH-009), conflito (EH-008) computados como atributos/registros — detectores, não gates (ENF-03).

> **Fronteira M-001 [DECISÃO NECESSÁRIA — em aberto]:** os **estados do Blackboard** para objetos NÃO-hipótese (Evidência) dependem de **M-001** (SPEC-004, aberta). Este protocolo referencia o **ciclo de vida do objeto** (CEM-001 Cap.4) e a mecânica de publicação, mas **não fecha** os estados do Blackboard — isso pertence à SPEC-004 (M-001 pendente). Homologado como aberta (research.md §6-bis, Q-A7). [FONTE: M-001; RULE-BB-003; research.md GAP-1]

---

## D7 — Cenários de Teste

### Cenário-EH-T01 — Publicação válida de Evidência PRIMARY por AGENT
```
DADO        Structural Agent com Evidência PRIMARY completa (CEM-001 Cap.3), Source Reference = Market Data
QUANDO      submete ao Evidence Harness
ENTÃO       evidence_id alocado; version = 1; estado = ACTIVE; evento Evidence Created emitido
VERIFICAÇÃO ev.evidence_id != null; ev.status == "ACTIVE"; ev.origin_type == "PRIMARY"
```

### Cenário-EH-T02 — Skill bloqueada como produtora de Evidência (INV-06)
```
DADO        Skill stateless "confluence-elliott" tenta publicar objeto como Evidência
QUANDO      o gate de produtor é aplicado
ENTÃO       rejeição, código "SKILL_NOT_EVIDENCE_PRODUCER"; nada publicado
VERIFICAÇÃO response.error_code == "SKILL_NOT_EVIDENCE_PRODUCER"
```

### Cenário-EH-T03 — Contrato CEM incompleto rejeitado
```
DADO        Evidência PRIMARY sem Interpretation
QUANDO      o gate de contrato (EH-002) é aplicado
ENTÃO       rejeição, código "CEM_CONTRACT_INCOMPLETE"
VERIFICAÇÃO response.error_code == "CEM_CONTRACT_INCOMPLETE"; evidence_count inalterado
```

### Cenário-EH-T04 — Strength não vira Convicção (INV-04)
```
DADO        processo tenta agregar Evidence Strength=0.8 em uma dimensão de convicção
QUANDO      o guard EH-005 é aplicado
ENTÃO       rejeição, código "STRENGTH_IS_NOT_CONVICTION"; Strength permanece local
VERIFICAÇÃO response.error_code == "STRENGTH_IS_NOT_CONVICTION"
```

### Cenário-EH-T05 — Conflito detectado e registrado, não resolvido
```
DADO        EV-A (bullish) e EV-B (bearish) institucionais, ambas ACTIVE
QUANDO      o detector de conflito (EH-008) roda
ENTÃO       conflict_record status = "REGISTERED_UNRESOLVED"; sem resolução na camada de evidência
VERIFICAÇÃO conflict.status == "REGISTERED_UNRESOLVED"; resolved_by_evidence_layer == false
```

### Cenário-EH-T06 — Ausência representada, não convertida em conclusão
```
DADO        questão espera evidência de sweep; nenhuma encontrada
QUANDO      o Harness classifica a tipologia (EH-007)
ENTÃO       typology = "AUSENTE"; nenhuma conclusão de ausência derivada
VERIFICAÇÃO typology == "AUSENTE"; derived_conclusion_from_absence == false
```

### Cenário-EH-T07 — Transição de ciclo de vida proibida rejeitada (INV-07)
```
DADO        Evidência em INVALIDATED
QUANDO      agente tenta transicionar para ACTIVE
ENTÃO       rejeição, código "LIFECYCLE_TRANSITION_FORBIDDEN"; objeto preservado
VERIFICAÇÃO response.error_code == "LIFECYCLE_TRANSITION_FORBIDDEN"; Blackboard.contains(EV) == true
```

---

## D8 — Cenários Adversariais [casos de negação — CRITICAL]

Princípio transversal: **fail-closed** — em qualquer ambiguidade sobre autorização, contrato, autoridade de resolução ou irreversibilidade, o Harness NÃO publica/NÃO promove/NÃO transiciona e retorna código específico.

### ADV-EH-01 — Skill publica Evidência (viola INV-06) (consolida EH-003 / T02)
**DADO:** Skill stateless tenta publicar Observação como Evidência
**QUANDO:** o gate de produtor roda
**ENTÃO:** rejeitar `SKILL_NOT_EVIDENCE_PRODUCER`; nada publicado
**PORQUE:** Observação ≠ Evidência (INV-06; RULE-EH-001)
**VERIFICAÇÃO:** error_code == "SKILL_NOT_EVIDENCE_PRODUCER"; evidence_count inalterado

### ADV-EH-02 — AGENT tenta publicar DERIVED / ENGINE tenta publicar PRIMARY
**DADO:** um AGENT tenta publicar Evidência DERIVED (ou o Fusion Engine tenta PRIMARY)
**QUANDO:** o gate de contrato (Origin Type × Producer Type) roda
**ENTÃO:** rejeitar `ORIGIN_PRODUCER_MISMATCH`; nada publicado
**PORQUE:** PRIMARY só AGENT; DERIVED só ENGINE (CEM-001 Cap.3; RULE-EH-002)
**VERIFICAÇÃO:** error_code == "ORIGIN_PRODUCER_MISMATCH"

### ADV-EH-03 — Evidence Strength promovido a Convicção (viola INV-04) (consolida EH-005 / T04)
**DADO:** processo deriva convicção diretamente de Evidence Strength
**QUANDO:** o guard EH-005 roda
**ENTÃO:** rejeitar `STRENGTH_IS_NOT_CONVICTION`; Strength permanece local; J-001 não antecipado
**PORQUE:** custo/força local nunca entram no Conviction Vector (INV-04; J-001)
**VERIFICAÇÃO:** error_code == "STRENGTH_IS_NOT_CONVICTION"

### ADV-EH-04 — Camada de evidência resolve conflito (viola ENF-03)
**DADO:** proposta de o detector LLM escolher a evidência "vencedora" e descartar a outra
**QUANDO:** o conflito é processado
**ENTÃO:** rejeitar `CONFLICT_RESOLUTION_OUT_OF_LAYER`; conflito apenas registrado; encaminha a SPEC-003/014
**PORQUE:** LLM é detector viesado na resolução (SRC-03 [EXTERNO]); Detector ≠ Gate (ENF-03; RULE-EH-006)
**VERIFICAÇÃO:** conflict.status == "REGISTERED_UNRESOLVED"; resolved_by_evidence_layer == false

### ADV-EH-05 — Independência não verificada afirmada (viola RULE-MET-01)
**DADO:** duas evidências de fonte comum sem discriminante de independência
**QUANDO:** o detector EH-006 encerra sem verificar independência
**ENTÃO:** atributo = "undetermined" + limitação declarada; NÃO afirmar independência; NÃO aplicar desconto
**PORQUE:** não fabricar independência não verificada (RULE-MET-01; RULE-004); mecânica de desconto → SPEC-003
**VERIFICAÇÃO:** independence_claimed == false; relationship_attribute == "undetermined"

### ADV-EH-06 — Ausência de evidência tratada como evidência de ausência (viola RULE-EPI)
**DADO:** nenhuma evidência encontrada para uma questão esperada
**QUANDO:** a tipologia é classificada (EH-007)
**ENTÃO:** typology = "AUSENTE"; rejeitar qualquer conclusão "prova que não ocorreu" (`ABSENCE_AS_CONCLUSION_FORBIDDEN`)
**PORQUE:** ausência de evidência ≠ evidência de ausência (RULE-EPI-01; RULE-UNC-03; RULE-EH-004)
**VERIFICAÇÃO:** derived_conclusion_from_absence == false

### ADV-EH-07 — Transição de ciclo de vida irreversível revertida (viola INV-07) (consolida EH-010 / T07)
**DADO:** Evidência em INVALIDATED/ARCHIVED/SUPERSEDED
**QUANDO:** agente tenta retornar a ACTIVE ou deletar/reescrever o objeto
**ENTÃO:** rejeitar `LIFECYCLE_TRANSITION_FORBIDDEN` / `EVIDENCE_HISTORY_IMMUTABLE`; objeto e histórico preservados
**PORQUE:** transições proibidas e imutabilidade pós-publicação (CEM-001 Cap.4; INV-07; RULE-EH-007/008)
**VERIFICAÇÃO:** error_code ∈ {"LIFECYCLE_TRANSITION_FORBIDDEN","EVIDENCE_HISTORY_IMMUTABLE"}; Blackboard.contains(EV) == true

### ADV-EH-08 — Invalidação com cascata automática sobre derivadas (viola não-cascata)
**DADO:** uma Evidência ancestral é invalidada
**QUANDO:** o sistema tenta invalidar automaticamente todas as derivadas
**ENTÃO:** rejeitar cascata automática (`AUTO_CASCADE_FORBIDDEN`); emitir Evidence Invalidated + iniciar avaliação de impacto
**PORQUE:** invalidação não implica cascata automática (CEM-001 Cap.4/Cap.5; RULE-EH-007)
**VERIFICAÇÃO:** auto_cascade_applied == false; impact_evaluation_started == true

### ADV-EH-09 — Fechar estados do Blackboard para não-hipótese (viola CONS-01 / M-001)
**DADO:** tentativa de fixar, nesta Spec, os estados do Blackboard para Evidência (objeto não-hipótese)
**QUANDO:** o protocolo de publicação é definido
**ENTÃO:** rejeitar `M001_STATES_OUT_OF_SCOPE`; referenciar M-001 como aberta; fechar → SPEC-004
**PORQUE:** M-001 em aberto — não fechar (CONS-01; research.md GAP-1; Q-A7)
**VERIFICAÇÃO:** blackboard_states_for_evidence não fixados; M-001 permanece aberta

### ADV-EH-10 — Antecipar mecânica de fusão/DERIVED (invade SPEC-003)
**DADO:** tentativa de computar evidência DERIVED (fusão/desconto de dependentes) nesta camada
**QUANDO:** o escopo é avaliado
**ENTÃO:** rejeitar `FUSION_MECHANICS_OUT_OF_SCOPE`; só o contrato de fronteira PRIMARY/DERIVED é declarado
**PORQUE:** a mecânica de fusão é do Fusion Engine (SPEC-003); J-001 aberto (research.md GAP-2/GAP-4)
**VERIFICAÇÃO:** derived_computed_here == false; SPEC-003 referenciada

> **Cobertura:** 10 cenários adversariais (mínimo para CRITICAL = ≥2; cobrem casos de negação de todas as BASpecs com efeito e das fronteiras homologadas). Todos mapeiam para EC-EH-001..005 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada ato da camada de evidência DEVE ser reconstruível (P13): entrada (Evidência + versão), gates aplicados (produtor/contrato/provenance), resultado (publicado/rejeitado + código), atributos derivados (tipologia, (in)dependência, staleness), conflitos registrados, transições de ciclo de vida (from→to + motivo + timestamp) e eventos emitidos (EC-COG-005). A **reconstrução expandida de linhagem** (Cognitive Trace Reconstruction) e o **storage físico** pertencem ao **Knowledge Graph (SPEC-006 / H-001)** — aqui ficam **por referência** (coerente com alvo D0–D8 e com CEM-001 Cap.5). [FONTE: CONSTITUTION P13; CEM-001 Cap.5; H-001 pendente]

---

## Evidence Registry (Serviço Lógico)

Espelho operacional do Hypothesis Registry (SPEC-001). Serviço lógico (não banco de dados):

| Função | Descrição |
|---|---|
| Alocação de ID | Gera `evidence_id` único e imutável (CEM-001 Cap.3) |
| Versionamento | Linhagem monotônica de versões (INV-07); imutabilidade pós-publicação |
| Índice de estado | Catálogo por `status` (ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED) |
| API de consulta | Busca por ID, estado, produtor, domínio, origem (PRIMARY/DERIVED), lineage |
| Reconstrução histórica | Suporta P13; delega Cognitive Trace Reconstruction ao KG (SPEC-006) |

**Armazenamento físico:** o Registry **não define onde** as Evidências são armazenadas (Blackboard vs KG) — pertence a SPEC-004/006. É interface lógica sobre o repositório físico. [FONTE: CEM-001 Cap.6; research.md GAP-3]

---

## I/O Schemas (lógicos — referência; não redefinem o CEM-001)

### Objeto Evidence (CEM-001 + atributos operacionais desta camada)
```json
{
  "evidence_id": "EV-2026-09-28-001",
  "evidence_version": 1,
  "previous_version_id": null,
  "creation_timestamp": "2026-09-28T10:30:00Z",
  "status": "ACTIVE | SUPERSEDED | INVALIDATED | ARCHIVED",
  "producer_type": "AGENT | ENGINE",
  "producer_id": "structural_agent",
  "evidence_origin_type": "PRIMARY | DERIVED",
  "domain": "STRUCTURAL | INSTITUTIONAL | MACRO | SENTIMENT | RISK | CONTEXT",
  "observation": "…", "interpretation": "…", "technical_rationale": "…",
  "evidence_strength": 0.72,
  "timeframe_reference": "H1",
  "market_context": "RANGE",
  "source_reference": "Market Data",
  "lineage": [],
  "_operational": {
    "producing_tool_or_skill": "confluence-elliott",
    "typology": "favorável | contra | inconclusiva | AUSENTE",
    "relationship_attribute": "independent | dependent | undetermined",
    "independence_claimed": false,
    "staleness_flag": "fresh | aging | stale",
    "conflict_refs": []
  }
}
```
> Os campos fora de `_operational` são do **CEM-001 (não redefinidos)**. O bloco `_operational` é a **camada operacional** desta Spec — atributos derivados/representados, nenhum promovido a Convicção (INV-04).

### Registro de conflito — schema lógico
```json
{
  "conflict_id": "CF-2026-09-28-001",
  "evidence_ids": ["EV-A", "EV-B"],
  "detected_by": "semantic_detector",
  "status": "REGISTERED_UNRESOLVED",
  "resolved_by_evidence_layer": false,
  "forwarded_to": "SPEC-003/SPEC-014"
}
```

---

## Enforcement Contracts

### EC-EH-001 — Publicação de Evidência (gate de produtor + contrato + provenance)

```
CAPABILITY   : Publicar uma Evidência no Blackboard (workspace de Evidência)
EFFECT       : Publicação de objeto Evidence em estado ACTIVE; evento Evidence Created (EC-COG-005)
PRECOND      : (producer ∈ AUTHORIZED_EVIDENCE_PRODUCERS) AND (Skill NÃO é produtor — INV-06) AND
               (contrato CEM-001 Cap.3 completo) AND (PRIMARY⇒AGENT, DERIVED⇒ENGINE) AND
               (provenance completa: Source Reference + producer + Lineage coerente)
POSTCOND     : Evidence publicada com evidence_id/version alocados; provenance íntegra; nada promovido a Convicção
POLICY       : RULE-EH-001/002/004; INV-06; INV-10; CEM-001 Cap.3/Cap.6
LEVEL        : E2 (Operacional — piso Evidência/Agente; estado compartilhado alterado)
FAILURE-MODE : Fail-closed — rejeitar publicação; código específico; nenhuma Evidência publicada; log
EVIDENCE     : Log de publicação (producer_id, evidence_id, timestamp); evento Evidence Created
```

### EC-EH-002 — Guard INV-04 (Evidence Strength ≠ Convicção)

```
CAPABILITY   : Impedir a promoção/agregação de Evidence Strength em Convicção nesta camada
EFFECT       : Bloqueia derivação de convicção a partir de Strength (barreira operacional)
PRECOND      : (tentativa de mapear Strength → dimensão/valor de convicção detectada)
POSTCOND     : Strength permanece peso local; nenhuma convicção derivada aqui (J-001/SPEC-003)
POLICY       : RULE-EH-003; INV-04; J-001
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — rejeitar promoção; código "STRENGTH_IS_NOT_CONVICTION"
EVIDENCE     : Log da tentativa barrada; ausência de campo de convicção derivado de Strength
```

### EC-EH-003 — Detecção/registro de (in)dependência e conflito (Detector ≠ Gate)

```
CAPABILITY   : Produzir o atributo de (in)dependência e registrar conflito entre evidências
EFFECT       : Emite atributo/registro (insumo) para Fusion/Conviction/Synthesis; nenhuma resolução
PRECOND      : (sinal semântico/heurístico rotulado como insumo, não veredito) AND
               (existe camada de resolução a jusante — SPEC-003/014) AND (bounded loop com parada)
POSTCOND     : atributo/registro criados; independência não verificada ⇒ "undetermined" + limitação;
               conflito ⇒ "REGISTERED_UNRESOLVED"; nada resolvido na camada de evidência
POLICY       : RULE-EH-005/006; ENF-03; RULE-MET-01; RULE-CAU-01; RULE-004
LEVEL        : E2 (Operacional — produz insumo; sem efeito normativo próprio)
FAILURE-MODE : Fail-closed — sem camada de resolução a jusante, o sinal NÃO vira veredito/resolução
EVIDENCE     : Log detector→registro distinto de qualquer resolução; conflict_record preservado
```

### EC-EH-004 — Representação de tipologia e aging (ausência ≠ conclusão)

```
CAPABILITY   : Representar tipologia (favorável/contra/inconclusiva/AUSENTE) e staleness
EFFECT       : Grava atributos operacionais no objeto Evidence (bloco _operational)
PRECOND      : (classificação em passo único; enum válido) AND (AUSENTE não convertida em conclusão) AND
               (nenhum peso numérico de convicção atribuído ao aging — J-001)
POSTCOND     : tipologia/staleness representados; derived_conclusion_from_absence == false
POLICY       : RULE-EH-004; RULE-EPI-01; RULE-UNC-03; RULE-PRB-02; J-001
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — ambiguidade ⇒ INDETERMINADO; conversão de AUSENTE ⇒ rejeição
EVIDENCE     : Bloco _operational preenchido; log da classificação; flag de não-conversão de ausência
```

### EC-EH-005 — Transição de ciclo de vida / invalidação (commit crítico irreversível)

```
CAPABILITY   : Transicionar o estado da Evidência (SUPERSEDED/INVALIDATED/ARCHIVED)
EFFECT       : Alteração de Status em objeto compartilhado; evento Evidence Invalidated/Superseded/Archived;
               início de avaliação de impacto sobre derivadas
PRECOND      : (transição ∈ grafo CEM-001 Cap.4) AND (não é transição proibida) AND (objeto preservado — INV-07)
POSTCOND     : Status atualizado; evento emitido; avaliação de impacto iniciada SEM cascata automática;
               histórico íntegro (nada deletado)
POLICY       : RULE-EH-007/008; CEM-001 Cap.4/Cap.5; INV-07
LEVEL        : E3 (Crítico — transição irreversível: INVALIDATED/ARCHIVED/SUPERSEDED → ACTIVE proibida)
FAILURE-MODE : Fail-closed — transição proibida/ambígua ⇒ rejeitar; estado e objeto inalterados; log
EVIDENCE     : transition_record (from/to/motivo/timestamp); evento EC-COG-005
             + método de observação de falso-DENY: amostragem de transições válidas rejeitadas por
               engano (limiar = gap aberto, ENF-07)
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
O Evidence & Evidence Provenance Harness é a **camada operacional cognitiva** sobre o objeto Evidência (CEM-001). Combina gates constitutivos determinísticos (Classe C: contrato, produtor, INV-04, INV-06, ciclo de vida), serviço lógico determinístico (Classe D: Registry, aging) e detectores probabilísticos com gate (Classe P/H: (in)dependência, conflito, tipologia). Não é executor; produz e mantém Evidência para consumo a jusante (Fusion/Conviction/Synthesis). [FONTE: CEM-001; atomic-spec §9/§10.6]

### Roteamento de modelo (CEE-001 §5)
Os **gates constitutivos/determinísticos** (Classe C/D) não requerem LLM. Os **detectores** (Classe P/H — (in)dependência, conflito, tipologia) usam apoio semântico: complexidade cognitiva Tipo III (julgamento especialista) → **Sonnet** como detector; Tipo IV–V (conflito multi-narrativa) → **Opus reservado** apenas como detector, **nunca como gate** (ENF-03; SRC-03 alerta para viés do LLM na resolução). Roteamento definitivo por Engineering Card (BUILD adiado). [FONTE: CEE-001 §5/RULE-CEE-002; ENF-03]

### Dependências técnicas
CEM-001 (BASELINE) · CHM-001 (BASELINE, fronteira) · SPEC-001 v1.1 (BASELINE, padrão Registry/fronteira) · SPEC-019/020/021 v1.0 (BASELINE, governança/avaliação/maturidade) · atomic-spec v1.5 · RULES.md v1.5 (INV-*, ENF-*, RULE-004, RULE-EPI/CAU/MET/UNC/PRB, RULE-BB-*) · CEE-001 v2.0 · EC-COG-005 (Event Bus — contrato → SPEC-005). Referências externas [EXTERNO], não-baseline: research.md §2 (SRC-01..06).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| LLM resolve conflito (colisão ENF-03; viés SRC-03) | RULE-EH-006; ENF-03; ADV-EH-04; EC-EH-003 fail-closed |
| Strength promovido a Convicção (fere INV-04/J-001) | RULE-EH-003; ADV-EH-03; EC-EH-002 |
| Skill publicada como Evidência (fere INV-06) | RULE-EH-001; ADV-EH-01; EC-EH-001 |
| Ausência tratada como prova de ausência | RULE-EH-004; ADV-EH-06; EC-EH-004 |
| Independência não verificada afirmada | RULE-EH-005; RULE-MET-01; ADV-EH-05 |
| Cascata automática de invalidação | RULE-EH-007; ADV-EH-08; EC-EH-005 (não-cascata) |
| Fixar estados do Blackboard (M-001) | Non-goal; ADV-EH-09; referência a M-001 aberta |
| Antecipar mecânica de fusão (SPEC-003) | Non-goal; ADV-EH-10; só contrato de fronteira PRIMARY/DERIVED |
| Fixar limiar de convicção (fere J-001) | RULE-EH-003; CC-03; CONS-01; D4 numérico N/A justificado |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz schemas lógicos "Evidence + _operational" e "conflict_record" (I/O acima); nenhum schema canônico do CEM-001 alterado.
- **RAG:** nenhum; a camada não escreve no KG/RAG (evidence candidate a partir de retrieval → SPEC-007).
- **Skills:** nenhuma Skill afetada; INV-06 reforça a fronteira Skill/Evidência.
- **Testes:** adiciona `checks.md` (verificação de spec) e propõe (via BL-021, aprovação própria) extensão do `validate_spec_sot.py` para o check "Classe declarada por BASpec".
- **Modelos dependentes:** CEM-001/CHM-001/SPEC-001 não alterados (construção SOBRE).
- **Compatibilidade:** **Minor** — adiciona a camada operacional (RULE-EH + BASpecs + EC) sobre o CEM-001, sem invalidar comportamento vigente; nenhuma RULE existente redefinida.

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07) e a Classe declarada por BASpec (CC-11).

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — pergunta adversarial por BASpec com efeito (cobertura TOTAL — CRITICAL):**

- **EH-001 (alocação ID/versão, D):** se errada → IDs colidem ou versão regride → observável por duplicidade de `evidence_id` ou `version` não-monotônica; verificável por observador independente (índice do Registry). Negação: ADV-EH-07 (imutabilidade). Condição QUANDO-sim-mas-ENTÃO-não: resubmissão idêntica não deve gerar novo ID — tratado como nova versão só se o produtor declara refino.
- **EH-002 (gate de contrato, C):** se errada → Evidência incompleta circula → observável por consumidor que falha ao ler campo ausente; verificável (checagem de contrato). Negação: ADV-EH-02, Cenário-EH-T03.
- **EH-003 (INV-06 gate, C):** se errada → Observação de Skill vira Evidência → observável por producer_type inválido publicado; verificável. Negação: ADV-EH-01, Cenário-EH-T02.
- **EH-004 (provenance, C):** se errada → Evidência sem rastro → observável por Source Reference/Lineage vazios num objeto publicado; verificável (P13 quebra). Negação: ADV-EH-02 (mismatch); gate de provenance.
- **EH-005 (INV-04 guard, C):** se errada → Strength vira convicção → observável por campo de convicção derivado de Strength nesta camada; verificável. Negação: ADV-EH-03, Cenário-EH-T04.
- **EH-006 ((in)dependência, P):** se errada → independência não verificada afirmada → observável por `independence_claimed==true` sem discriminante; verificável. Negação: ADV-EH-05. Condição QUANDO-sim-mas-ENTÃO-não: co-ocorrência não implica dependência causal (RULE-CAU-01) → "undetermined", não "dependent".
- **EH-007 (tipologia/ausência, H):** se errada → AUSENTE convertida em conclusão → observável por `derived_conclusion_from_absence==true`; verificável. Negação: ADV-EH-06, Cenário-EH-T06.
- **EH-008 (conflito, P):** se errada → conflito resolvido/suprimido na camada errada → observável por `resolved_by_evidence_layer==true` ou conflito ausente do registro; verificável. Negação: ADV-EH-04, Cenário-EH-T05.
- **EH-009 (aging, D):** se errada → peso numérico de convicção atribuído ao aging → observável por `conviction_weight_assigned==true`; verificável. Negação: guard J-001 (CC-03); RULE-EH-003.
- **EH-010 (ciclo de vida, C):** se errada → transição proibida aceita ou cascata automática → observável por `status` inválido ou derivadas invalidadas em massa; verificável. Negação: ADV-EH-07, ADV-EH-08, Cenário-EH-T07.

Todas as BASpecs com efeito têm ENTÃO verificável por observador independente e caso de negação em D8. Nenhuma restou como [DECISÃO NECESSÁRIA] por falta de verificabilidade.

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista CEM-001 (Cap.3/4/5/6), CHM-001, SPEC-001 v1.1, SPEC-019/020/021 v1.0, atomic-spec v1.5, ENF-01..08, INV-04/06/07/09/10, RULE-004, RULE-BB-002/004 (ID+versão — RULE-HD-04). Evidência de satisfação por obrigação herdada:
- CEM-001 Cap.3 (contrato) → EH-002/EH-004 (gate de contrato/provenance).
- CEM-001 Cap.4 (ciclo de vida, transições proibidas, não-cascata) → EH-010 + D5 + EC-EH-005.
- CEM-001 Cap.3 (Strength local) + INV-04 → EH-005/EC-EH-002.
- INV-06 (Evidência≠Observação) → EH-003/EC-EH-001.
- INV-07 (monotônico/imutável) → EH-001/EH-008(rule)/EH-010; ADV-EH-07.
- INV-10 (CEM idioma) → EH-002; I/O não redefine campos do CEM.
- RULE-004 (dependentes = uma) → EH-006 (representação; mecânica adiada a SPEC-003 — RULE-HD-02 respeitada: extensão de cobertura, não contradição).
- RULE-EPI/UNC/MET/CAU/PRB → EH-006/EH-007 (ausência, independência, não-fabricação).
- ENF-03 → EH-006/EH-008 (detector≠gate).
- SPEC-001 padrão Registry → Evidence Registry (espelho).
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (o único MODIFIED estende RULE-004 sem alterar seu texto — RULE-HD-02). **Eixo VERTICAL (RULE-HV) declarado não aplicável** (herança sobre modelo canônico, não decomposição pai→filha de macro-spec).

**Bloco C — epistêmico (RULE-EPI/CAU/PRB):** nenhuma afirmação causal forte sem mecanismo (dependência entre evidências tratada por RULE-CAU-01: co-ocorrência ≠ causa → "undetermined"); nenhuma hipótese tratada como fato (fontes SRC-01..06 = [EXTERNO]/DADO); INDETERMINADO usado em (in)dependência não verificável e em ausência/inconclusiva em vez de forçar conclusão; nenhuma probabilidade/precisão numérica declarada sem base (D4 numérico de qualidade/desconto N/A justificado; J-001 aberto; tipificação qualitativa — RULE-PRB-02).

**Bloco D — reforço de escopo:** a Spec **produz e mantém Evidência** (detecção/representação/gate), **não executa** ordem nem emite sinal — INV-05/RULE-DEC-01 reconfirmados (§7). Nenhuma BASpec cruza a fronteira SOT→execução downstream nem resolve conflito/convicção (fronteira SPEC-003/014). Dependências de decisão de Andraus (homologação; efetivação de RULE-EH) marcadas [PROPOSTA]; J-001, M-001, H-001 marcadas [DECISÃO NECESSÁRIA]/aberta, não fechadas.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001 (contrato/ciclo/linhagem/eventos/governança) | [FONTE] | FATO NORMATIVO (BASELINE) |
| CHM-001; SPEC-001 v1.1; SPEC-019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5; RULES v1.5 (INV-*, ENF-*, RULE-004, RULE-EPI/CAU/MET/UNC/PRB, RULE-BB-*) | [FONTE] | FATO NORMATIVO |
| RULE-EH-001..008; BASpec-EH-001..010; EC-EH-001..005; I/O `_operational` | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Fontes SRC-01..06 (W3C PROV, GRADE, ECon, OpenLineage, Evidence of absence, Dependent Fusion) | [EXTERNO] | Referência de método — DADO, nunca baseline (research.md §2) |
| Evidence Registry (serviço lógico) | [INFERÊNCIA] | FATO ARQUITETURAL |
| Formato de evidence_id | [PROPOSTA] | Ajustável sem impacto normativo |
| J-001 (fórmula/pesos/limiares/aging na convicção) | [DECISÃO NECESSÁRIA] | EM ABERTO — pendente — não fechar |
| M-001 (estados do Blackboard p/ Evidência) | [DECISÃO NECESSÁRIA] | EM ABERTO — pendente (SPEC-004) |
| H-001 (KG: storage/Cognitive Trace Reconstruction) | [DECISÃO NECESSÁRIA] | EM ABERTO — pendente (SPEC-006) |
| Mecânica de fusão / evidência DERIVED | [FONTE] | DIFERIDA a SPEC-003 (não fechada) |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-002 confirmada como próximo autorizado (§29); FASE 1, após FASE GOV concluída.
[x] atomic-spec.md lido: método v1.5 confirmado (RULE-REG-001/DHR-REG-001; CC-11/CC-12; RULE-MECH-01; RULE-MM).
[x] Nenhum invariante congelado violado (INV-01..10 + INV-RISK). INV-04/INV-06/INV-07/INV-10 reforçados.
[x] Constitution Check CC-01..CC-12 preenchido (N/A justificados em CC-06/07/10/12; CC-11 INCIDE e aplicada).
[x] Disciplinas N8–N17: RULE-EPI (INDETERMINADO/ausência), RULE-CAU-01 (independência), RULE-MET-01 (não-fabricação), RULE-UNC/PRB (qualitativo), RULE-DEC-01 (detecta≠executa), RULE-SEM (termo CEM não redefinido).
[x] Referências externas SRC-01..06 [EXTERNO] classificadas (research.md §2); rótulos externos (PROV/OpenLineage/GRADE) NÃO adotados como baseline; verbatim capturado (RULE-ECC-04, sources/).
[x] Spec sem implementação; Plan derivado; Tasks adiadas (spec-first).
[x] Critérios em EARS (9); BASpecs completas (EH-001..010) com Classe declarada (CC-11); RULEs citadas existentes vs propostas (RULE-EH [PROPOSTA]) claramente etiquetadas.
[x] Profundidade D0–D8 atingida (D5 estados CEM-001; D6 protocolo; D7 x7; D8 adversarial x10; D9 por referência).
[x] Enforcement Contract em todo ato com efeito (EC-EH-001..005); piso E2; E3 na invalidação irreversível; fail-closed; ENF-07 amostral declarado no E3.
[x] Status epistemológico aplicado (FATO NORMATIVO vs PROPOSTA vs EXTERNO vs DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: J-001, M-001, H-001 permanecem abertas (não fixadas); mecânica de fusão DIFERIDA; nenhuma decisão aberta usada como invariante.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos registrados (research.md §4 CONFLITO-1/2/3; GAP-1..4) — não resolvidos em silêncio.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE/EC fabricada como vigente; sem baseline informal.
[x] 4Es na ordem; Conformidade > Eficácia (INV-04/06 e ENF-03 prevalecem). Latência N/A (camada spec-time; consumidor a jusante é SPEC-003).
[x] Dependências a montante homologadas (CEM-001/CHM-001/SPEC-001/019/020/021/atomic-spec v1.5/RULES v1.5/CEE-001); não downstream de bloqueador aberto (J-001 é adiado, não bloqueia a camada operacional qualitativa).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); Bloco A cobre TODAS as 10 BASpecs com efeito (não repetir o achado de cobertura incompleta da SPEC-020) — obrigatório CRITICAL.
[x] CC-11/§10.6: Classe declarada por BASpec com efeito, com critério 4Es; H/P com bounded loop; H/C com gate de saída.
[x] Abertura (RULE-ECC-01/02/04): Dossiê presente e HOMOLOGADO (research.md §6-bis); RULE-ECC-04 verbatim em sources/SRC-01..06.txt; escopo/quantidade/número homologados.
[x] Passo 11-bis: RULE-REG-001 tratado (homologado na abertura); BL-012 IMINENTE (homologação); demais não disparam.
[ ] Gate determinístico (validate_spec_sot.py) e build_map.py --check: a rodar/confirmar no ambiente pai — reportado ao caller.
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] / abertas nesta Spec (não fechadas — CONS-01):
- **J-001** — fórmula/pesos/limiares definitivos do Conviction Vector (inclui peso/decay de aging e desconto de dependência); a Spec é qualitativa e **não** os fixa.
- **M-001** — estados do Blackboard para objetos não-hipótese (Evidência); referenciada como aberta; fecha em SPEC-004.
- **H-001** — Knowledge Graph (storage físico / Cognitive Trace Reconstruction); referenciada como aberta; fecha em SPEC-006.
- Mecânica de **fusão** / evidência DERIVED — DIFERIDA a SPEC-003 (só o contrato de fronteira aqui).

Carregado do Dossiê para o Revisor:
- research.md §6-bis: 3 achados Menores não-bloqueantes do parecer do Revisor sobre o research.md — a reconfirmar/tratar na auditoria desta entrega.
- BL-012 (MC-COG-001) IMINENTE na homologação (mapear COG-SPEC × N8–N17; usar estados CEM-001/CHM-001).
