# SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine

| Campo | Valor |
|---|---|
| ID | SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine (redige o **CCM-001**, canônico pendente) |
| Versão | 1.3 (candidata) |
| Status | **CANDIDATA — em revisão** (não homologada; homologação é ato de Andraus) |
| Fonte | ROADMAP §4/§21/§143; `research.md` (Dossiê de abertura HOMOLOGADO por Andraus 2026-10-01, §6-bis + §8 nota de delta v1.1; RULE-ECC-01/02/04/05); atomic-spec **v1.5**; `WORKFLOW.md` (versão vigente — reconciliação v1.1, conformidade RULE-ECC-05 lente 3) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §4/§143; research.md Q-A1/Q-A2; atomic-spec §3 "Conviction Engine = CRITICAL"] |
| Profundidade-alvo | **D0–D8** (standard + adversarial) [FONTE: research.md Q-A2 homologado; AGENTS.md §4] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 1 — NÚCLEO COGNITIVO; após SPEC-001/002 (BASELINE) e a FASE GOV (019/020/021, concluída); antes de SPEC-004 [FONTE: ROADMAP §21/§143] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3; teto spec-first (RULE-MM-04/05; gate normativo E3) [FONTE: research.md §5.8(4)] |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01; RULE-PD-01 (N/A); RULE-ECC-04; **RULE-ECC-05 (1ª aplicação num Plan)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — gates constitutivos (C) + agregação determinística (D) + julgamento com gate (H/P); declaração normativa é por BASpec |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-01 |
| Abertura | Dossiê de Pesquisa HOMOLOGADO por Andraus (research.md §6-bis, 2026-10-01) — Plan iniciado no mesmo dia, dentro da validade do Dossiê (ECC-VAL-001 pendente; precedente 30 dias/início do Plan, Q-A7) |

Complexidade: CRITICAL. Profundidade-alvo: D0–D8 (standard + adversarial). Conviction Vector: definitivos pendentes (J-001/N-001 em aberto); dimensionalidade=8 fechada; limiares-piloto ≥70% / 7-9 interinos.

Status epistemológico de cabeçalho: a SPEC-003 **redige o CCM-001** (Canonical Conviction Model), canônico **pendente** (não protegido por CONST-01 — ROADMAP §79), respeitando os canônicos vizinhos **CEM-001/CHM-001** (BASELINE, não redefinidos — CC-02). Conviction Vector: **dimensionalidade = 8 fechada** (Questionário v1); **limiares-piloto ≥70% / 7-9 = FATO NORMATIVO interino** (Questionário v1, recalibrável pós-backtest); **fórmula/pesos/limiares definitivos = J-001 em aberto**; **pesos por ativo definitivos = N-001 em aberto** — [DECISÃO NECESSÁRIA]. [FONTE: INV-03; AGENTS.md §6; research.md §6-bis Q-A4]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.3 | 2026-10-01 | **Delta de propagação DHR-DEC-001 (decisão direta de Andraus em chat).** Resolve **Q-A5**: o número de invocações do mecanismo de Conviction Vector **passa a FECHADO — 2x por ciclo** (macro na Fase 1: estrutural+institucional → registra o alarme; global na Fase 2: +operacional → decide o envio), **declarado em `WORKFLOW.md` WF-C01 (versão vigente)**. Para a SPEC-003 isso é **dado de entrada herdado de WF-C01**: a Spec **dá o mecanismo** de convicção sobre subconjunto/vetor-completo e **NÃO é dona da invocação** — a invocação é do **Manager Fase 1 (SPEC-008) / Fase 2 (SPEC-014)**. **Sem renumerar BASpecs e sem mudança de mérito de EARS/Enforcement/Classe.** Ajustados: Nota de gate, CC-03/CC-10, Non-goals, S5, Conformidade WF-C01, RULE-CF-010, fluxo D6, BASpec-CF-010, ADV-CF-12, §7-bis CF-010, lista final. **`WF-D03` permanece ABERTA (residual)**: J-001/N-001 (fórmula/pesos/limiares) e **Q-A9** (dimensão do regime, a cargo desta Spec) — Q-A5 **sai** do resíduo da WF-D03. M-001 segue aberta. |
| 1.0 | 2026-10-01 | Entrega candidata inicial. Redige o CCM-001 + Evidence Fusion Engine + Conviction Engine + Conviction Vector 8D. D0–D8, atomic-spec v1.5. 1ª aplicação de RULE-ECC-05 refletida num Plan (decisões adotar/adaptar/rejeitar/adiar do Dossiê incorporadas nas BASpecs/Non-goals). |
| 1.2 | 2026-10-01 | **Delta de propagação DHR-ARQ-001 (unificação Manager/Conviction).** Resolve **CONFLITO-1 / CC-10**: a acepção de "Conviction Engine" deixa de ser **(a)** "componente SEPARADO do Kernel" e passa a **mecanismo de fusão + cálculo do Conviction Vector 8D (Classe D/H do CCM-001) INVOCADO pelo Manager Agent — Fase 2 (Conviction)** — propagando ADR-MANAGER-001 (HOMOLOGADO) e CEM-001 DIV-CEM-4. Nenhum agente/componente "Conviction Engine" independente é criado. B-001 FECHADA (Q-007) e **parcialmente SUPERSEDIDA** na parte "componente separado" (INV-07 — não apagada); preservada a separação **lógica** de etapas (Fusão→cálculo do Conviction Vector→síntese). **Sem mudança de mérito das BASpecs/EARS/Enforcement/Classe; BASpecs NÃO renumeradas** (os três mecanismos cobertos — Fusão, Conviction Vector, gate — permanecem; muda o *framing* de "componente separado" para "mecanismo invocado pelo Manager Fase 2"). **WF-D03 permanece ABERTA** (J-001/N-001/Q-A5/Q-A9). Atualiza o cabeçalho de status, CC-10, a Declaração de acepção semântica e a Missão (D0). |
| 1.1 | 2026-10-01 | **Delta de reconciliação ao `WORKFLOW.md` (versão vigente).** Sem mudança de mérito das BASpecs/EARS/Enforcement/Classe. (1) Reclassifica a fronteira: `WF-D01` (Killzone), `WF-D02` (alarme-gatilho) e `WF-D04` (papel do ICT) agora **FECHADAS** por Andraus na `WORKFLOW.md` (versão vigente) — a SPEC-003 continua **não** as especificando (são do Manager/Scheduler — SPEC-008/015 — e dos agentes SPEC-010..014), mas deixam de ser tratadas como pontos abertos de `WORKFLOW-SOT-001`; **`WF-D03` permanece ABERTA (residual)**: J-001, N-001, nº de invocações 1x/2x (Q-A5) e **dimensão do regime** (WF-C04, novo **Q-A9**). (2) Incorpora por ID, mecanismo-apenas: `WF-C01` (macro×global = um vetor, duas leituras → CF-010), `WF-C02` (confluência por independência → CF-002), `WF-C03` (order flow → dimensão de volume, INDETERMINADO → CF-007), `WF-C04` (regime = dimensão de convicção → RULE-CF-003/Q-A9), `WF-X03`/INV-04 (risco não retroalimenta convicção → CF-008/CF-011), `WF-A01` (parent_id/hipótese-origem = contrato de entrada consumido → CF-001/CF-013), `WF-V02` (rótulo de evidência por escola, preservado na reconstrução → CF-011/D9), `WF-P02`/N-001 (parâmetros por ativo = gancho → CF-009). (3) Atualiza CC-10/acepção semântica à direção de `WF-C01`, a conformidade RULE-ECC-05 lente (3), Herança/Delta (CC-08), Nota de gate e Etiquetagem. Registra **Q-A9** (dimensão do regime, WF-C04). BASpecs **não renumeradas**. |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; research.md §5.9; RMR-001]

- **BL-004** (Fórmula/pesos/limiares do Conviction Vector; gatilho `spec:SPEC-003 em redação`): **DISPAROU na abertura** → **ATIVADO** e **Absorvido** pela SPEC-003 (research.md §6-bis / correção A-01). O item descreve exatamente o trabalho desta Spec (redigir CCM-001; fechar o **mecanismo** de J-001/N-001). O **fechamento** de J-001/N-001 quanto a valores definitivos é pós-backtest (não nesta Spec — CONS-01); aqui fecha apenas estrutura/método + limiares-piloto interinos (Q-A4). **Item tratado — não pendente neste gate.** [FONTE: RMR-001 BL-004; research.md §5.9]
- **BL-012** (MC-COG-001; gatilho `spec:SPEC-002 homologada`): permanece **`ATIVADO`**, **independente desta Spec** — tratado separadamente por Andraus (research.md §6-bis correção A-01). Não bloqueia a SPEC-003 e não é absorvido por ela; registrado para visibilidade do gate. [FONTE: RMR-001 BL-012; MEMORY MC-COG-001]
- **BL-002** (Falso-DENY observável, ENF-07; gatilho `spec:SPEC-003 homologada` ∨ `decisao:J-001 resolvida` — **J-001 segue em aberto/pendente**, esta é só a sintaxe do gatilho): **não dispara na redação**; **IMINENTE** — dispara na **homologação** da SPEC-003. O método de observação de falso-DENY do gate E3 (CF-012) já é esboçado em EC-CF-006/ENF-07; limiar amostral = gap de enforcement aberto. [FONTE: RMR-001 BL-002]
- **BL-003** (`spec:SPEC-004 em redação`), **BL-017** (`spec:SPEC-007/014/038 em redação`): **não disparam** (SPEC-003 não é gatilho). [FONTE: RMR-001]
- Nenhum item fica `ATIVADO` pendente **sem encaminhamento** por esta redação (BL-004 absorvido/tratado; BL-012 encaminhado a Andraus; BL-002 IMINENTE). O passo 11-bis pleno ocorre na homologação da SPEC-003.
- **Reconciliação `WORKFLOW-SOT-001` (DHR-WF-002, versão vigente da `WORKFLOW.md`) [FONTE]:** a decisão aberta `WORKFLOW-SOT-001` deixou de ser quádrupla — `WF-D01` (Killzone), `WF-D02` (alarme-gatilho) e `WF-D04` (papel do ICT) estão **FECHADAS** por Andraus; permanece **ABERTA só `WF-D03`** (residual): relação convicção-macro/global ↔ Conviction Vector 8D (direção declarada em `WF-C01`; **o nº de invocações passou a FECHADO — 2x por ciclo — por Andraus [WF-C01, Q-A5, DHR-DEC-001, 2026-10-01]**; resíduo aberto = fórmula/pesos/limiares = J-001 e dimensão do regime = WF-C04/Q-A9). A SPEC-003 continua **não** especificando Killzone/alarme/ICT (Manager/Scheduler SPEC-008/015 e agentes SPEC-010..014), **não** é dona da invocação 2x (é do Manager Fase 1/2 — SPEC-008/014) e **não** fecha `WF-D03` (CONS-01). Nenhuma `WF-Dxx` aberta é tratada como fechada nesta entrega. [FONTE: ROADMAP §32; WORKFLOW.md WF-D01/D02/D03/D04 versão vigente]

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** a agregação do Conviction Vector é **NÃO-compensatória** onde a hierarquia exige — a dimensão **estrutural (Elliott)** tem precedência e **veto direcional** (RULE-SY-001); dimensões inferiores (geométrica/fractal/institucional/operacional) **confirmam ou enfraquecem, nunca sobrepõem** a superior (INV-01/RULE-008). Rejeita-se explicitamente agregação compensatória pura (TOPSIS) e "votos" simétricos (SRC-05/SRC-06 [EXTERNO]) por violarem CC-01 — ver §D2/BASpec-CF-005/CF-006. [FONTE: INV-01; RULE-SY-001; RULE-008; research.md §3.1 CONFLITO-2]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** a SPEC-003 **constrói SOBRE** CEM-001 (entrada da fusão; Fusion Engine = único ENGINE PRODUCER de evidência DERIVED) e **respeita** CHM-001 (Separação Tríplice; Hypothesis Confidence intocada). **CCM-001 é o produto redigido** — canônico **pendente**, não protegido por CONST-01 (ROADMAP §79) — e é escrito sob GMC-001 respeitando as fronteiras dos vizinhos. CEM-001 e CHM-001 **não** são redefinidos. [FONTE: CEM-001 Cap.2/3/5/6; CHM-001 §1.9/§2.14; ROADMAP §79; CC-02]
- [x] **CC-03 — Conviction Vector:** **dimensionalidade = 8 fechada** (Questionário v1; não reaberta). **Limiares-piloto ≥70% / 7-9 = FATO NORMATIVO interino** (Questionário v1, recalibrável pós-backtest). **Fórmula/pesos/limiares definitivos = J-001 em aberto/pendente**; **pesos por ativo definitivos = N-001 em aberto/pendente** — [DECISÃO NECESSÁRIA]; a Spec fecha **estrutura/método/mecanismo**, não os valores definitivos (Q-A4). Nenhum valor definitivo é tratado como fechado (INV-03/CONS-01). [FONTE: INV-03; J-001 pendente; N-001 pendente; research.md §6-bis Q-A4]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada; as 5 Salvaguardas de Sinal (§11) são **preservadas** pelo gate CF-012 (invalidação explícita; score ≥7/9; conflito direcional→NEUTRO; convicção ≥70%; R:R 1:3 — este último **referenciado como fronteira a jusante**, pertence ao Risk Agent/Synthesis). INV-04 (custo/sizing nunca na convicção) é **reforçado** por CF-011/EC-CF-005. [FONTE: CEE-001 §10/§11; RULE-CEE-004; INV-04]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D8 (ROADMAP §4/§143; research.md Q-A1/Q-A2).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card. Os campos §59 e a cadeia §60 tornam-se obrigatórios quando as Tasks/Engineering Cards forem produzidas (BUILD adiado — atomic-spec §14). Omissão justificada. [FONTE: atomic-spec §8.1/§14]
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem provida por ROADMAP §4/§143 → Dossiê (research.md, homologado) → esta Spec.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED preenchidos com ID+versão (RULE-HD-04); REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Eixo VERTICAL (RULE-HV) avaliado e declarado não aplicável (herança sobre modelos canônicos vizinhos, não decomposição pai→filha de macro-spec) — ver nota na seção de Herança. [FONTE: EUA-E04 §8.3; RULE-HD-02/03/04; RULE-HV]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI):** aplicado — distinção FATO NORMATIVO / FATO ARQUITETURAL / PROPOSTA / INFERÊNCIA / EXTERNO; fontes web tratadas como DADO ([EXTERNO], research.md §2), nunca baseline; nenhuma hipótese tratada como fato; **INDETERMINADO** usado onde há incerteza material (ausência/contraevidência; (in)dependência não verificável; robustez insuficiente); **sem falsa precisão** — nenhuma escala/limiar numérico definitivo de convicção fixado (J-001). [FONTE: RULE-EPI-01..03; RULE-PRB-02; research.md §4]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM-01):** **INCIDE e RESOLVIDO (delta v1.2 / DHR-ARQ-001).** O termo **"Conviction Engine"** tinha **acepção concorrente** (CONFLITO-1): (a) motor autônomo separado do Kernel (ROADMAP/B-001); (b) Fase 2 do Manager Agent (CEM-001 notas DIV-CEM-4/ADR-MANAGER-001; `WORKFLOW.md` WF-04/WF-06, que atribuem ao **Manager** o ato de *formar* a convicção macro/global em runtime). **Por instrução direta de Andraus (DHR-ARQ-001, 2026-10-01), a SPEC-003 adota a acepção (b):** "Conviction Engine" é **mecanismo de fusão + cálculo do Conviction Vector 8D (Classe D/H do CCM-001) INVOCADO pelo Manager Agent — Fase 2 (Conviction)** — **não** um agente/componente separado. B-001 (Q-007) fica **parcialmente SUPERSEDIDA** na parte "componente separado" (INV-07 — não apagada), preservando a separação **lógica** de etapas (Fusão→cálculo do Conviction Vector→síntese). Isto **resolve** o CONFLITO-1 (deixa de ser reconciliação pendente (a)↔(b)); o que **permanece aberto** em `WORKFLOW-SOT-001`/WF-D03 é apenas J-001/N-001 e a dimensão do regime (Q-A9) — **não** a taxonomia do componente nem o nº de invocações (**Q-A5 FECHADA — 2x por ciclo — por Andraus [WF-C01, DHR-DEC-001]**; a invocação é do Manager Fase 1/2, a SPEC-003 só fornece o mecanismo). A direção macro×global declarada em `WF-C01` segue consistente com CF-010; `WF-C01` não fecha J-001. Termos canônicos (Evidence Strength, Hypothesis Confidence, Global Conviction) **não são redefinidos** (RULE-SEM-04). Ver §"Declaração de acepção semântica". [FONTE: RULE-SEM-01/04; ADR-MANAGER-001 §2.1/§2.3; CEM-001 DIV-CEM-4; DHR-ARQ-001; WORKFLOW.md WF-C01/WF-04/WF-06 versão vigente; research.md §3.3/§4 CONFLITO-1]
- [x] **CC-11 — Classe/Mecanismo por BASpec com efeito (RULE-MECH-01):** **INCIDE** — a SPEC-003 cita RULE-MECH-01 e é "SPEC-002 em diante". Cada BASpec com efeito declara sua Classe (D/H/P/C) com critério 4Es; Classes H/P declaram bounded loop + critério de parada; Classes H/C declaram gate de saída determinístico. Declaração por BASpec, nunca por Spec inteira (SES-001 §50). Ver §D3. [FONTE: RULE-MECH-01..04; atomic-spec §9/§10.6]
- [x] **CC-12 — Princípios de Domínio `PD-xx` (RULE-PD-01):** **N/A — não incide** (homologado Q-A3). O Conviction/Fusion Engine é **infraestrutura de agregação transversal e domain-agnostic** — agrega convicções produzidas pelas escolas (Elliott/SMC/ICT), mas **não é** uma escola analítica. Mesmo padrão N/A de SPEC-002. Os `PD-xx` serão declarados pelas Specs analíticas SPEC-010..014. GPR-001 §2.7 permanece sem `PD-xx` de convicção. N/A **homologado por Andraus** (research.md §6-bis Q-A3) — registrado explicitamente, não supressão silenciosa. Nuance honesta (RULE-MET-01): RULE-ECC-05 incidir **não** implica RULE-PD-01 incidir — gatilhos distintos (ECC-05 = toca comportamento de trading; PD-01 = define escopo de especialidade). [FONTE: RULE-PD-01; atomic-spec §10.7; research.md §5.8(3)/§6-bis]

**Disciplinas cognitivas N8–N17 incidentes (RULES.md v1.5):** RULE-EPI (hipótese≠fato; INDETERMINADO), RULE-CAU-01 (afirmação causal exige mecanismo — usada na fusão de dependentes: dependência causal entre evidências não se afirma por co-ocorrência/correlação), RULE-MET-01 (não-fabricação — não afirmar convicção/independência/robustez não verificadas), RULE-UNC-01..03 (incerteza localizada, não convertida em probabilidade sem base — RULE-UNC-03 remete quantificação ao nó Probabilística/Conviction Engine), RULE-PRB-01/02 (não quantificar sem base; RULE-PRB-01 nota que o Conviction Vector tem contrato próprio = CCM-001/J-001), RULE-DEC-01 (o Conviction Engine produz convicção/insumo decisional, **não executa** nem dimensiona risco), RULE-SEM-01/04 (acepção de "Conviction Engine" declarada; termos canônicos não redefinidos). INDETERMINADO usado onde há incerteza material.

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-003

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - Objeto canônico vizinho (entrada): CEM-001 (BASELINE, DHR-TAX-001) — Canonical Evidence Model:
      • Cap.2/Cap.6 (Fusion Engine = único ENGINE PRODUCER de evidência DERIVED; consome apenas ACTIVE;
        papéis PRODUCER/CONSUMER; Multi-Role Compliance)
      • Cap.3 (Evidence Strength 0.0–1.0 = peso LOCAL do produtor, ≠ Convicção; Domain; Market Context;
        Timeframe Reference)
      • Cap.4/Cap.5 (ciclo de vida; avaliação de impacto de invalidação iniciada pelo Fusion Engine,
        sem cascata automática; Lineage; Cognitive Depth = métrica derivada; Cognitive Trace Reconstruction
        = capacidade do Knowledge Graph)
      • Cap.6 (eventos Evidence Created/Invalidated via EC-COG-005)
  - Objeto canônico vizinho (fronteira): CHM-001 (BASELINE) — Separação Tríplice (§1.9) e Princípio da Não
      Equivalência (§2.14): Evidence Confidence (CEM) × Hypothesis Confidence (CHM) × Global Conviction (CCM);
      "Global Conviction definida pelo futuro CCM-001" (§2.14); CHM-001 não calcula Convicção Global; o CCM-001
      não redefine Confidence de Hipótese
  - Camada a montante: SPEC-001 v1.1 (BASELINE) — slot de convicção referenciado pela hipótese;
      SPEC-002 (BASELINE, DHR-SPEC002-001) — evidência operacional ACTIVE, provenance, tipologia
      (favorável/contra/inconclusiva/AUSENTE), (in)dependência representada (anti-double-counting), conflito
      DETECTADO/REGISTRADO (nunca resolvido) — insumos que a SPEC-003 consome
  - Setup operacional (fronteira soberana, NÃO redefinida): WORKFLOW.md (versão vigente, DHR-WF-002) —
      a SPEC-003 conforma-se por ID (mecanismo-apenas): WF-C01 (macro×global = um vetor, duas leituras),
      WF-C02 (confluência por independência), WF-C03 (order flow → dimensão de volume, INDETERMINADO),
      WF-C04 (regime = dimensão, não gate; dimensão-alvo = Q-A9), WF-X03 (fluxo unidirecional convicção→risco),
      WF-A01 (parent_id/hipótese-origem consumido, não produzido), WF-V02 (rótulo de evidência por escola
      preservado), WF-P02 (parâmetros por ativo = mecanismo → N-001). WF-D01/D02/D04 FECHADAS (fora de escopo
      — Manager/Scheduler SPEC-008/015 e agentes); WF-D03 ABERTA (residual) — não fechada aqui (CONS-01)
  - Método: atomic-spec.md v1.5 (BASpec, D0–D9, EARS, Enforcement E0–E3/F.1–F.4, TRACE-06, Quality Gates
      L1–L4 §7, Classe/Mecanismo §10.6, RULE-MM §maturidade)
  - Governança/Avaliação/Maturidade: SPEC-019 v1.0 (RULE-HG-01..08, RULE-HV-01..04); SPEC-020 v1.0
      (9 lentes/RULE-EV-01..07; RULE-EV-05 = avaliação qualitativa até J-001); SPEC-021 v1.0 (RULE-MM-01..07;
      nível-alvo L3; RULE-MM-06 = sem limiar numérico dependente de convicção)
  - Enforcement: ENF-01..08 (ênfase ENF-03 Detector≠Gate; ENF-04 fail-closed; ENF-07 falso-DENY no E3)
  - Invariantes: INV-01 (hierarquia), INV-03 (dimensionalidade=8; definitivos=J-001), INV-04 (custo fora
      do Conviction Vector), INV-05 (SOT não executa; produz insumo decisional), INV-06 (Evidência≠Observação),
      INV-07 (versionamento monotônico), INV-09 (sem baseline informal), INV-10 (CEM-001 = idioma)
  - Regras existentes: RULE-002 (ICT sem hipótese estrutural aprovada pelo Conviction Engine → inativo),
      RULE-003 (convicção global <70% → sem sinal; Fase Piloto), RULE-004 (evidências causalmente
      relacionadas = uma), RULE-005 (conflito direcional Elliott×SMC → inválido), RULE-008 (camada inferior
      não invalida superior), RULE-010 (toda alteração de convicção rastreável), RULE-SY-001 (Elliott veto;
      conflito Elliott×SMC → NEUTRO), RULE-SY-003 (sem sinal <70%; Fase Piloto), RULE-CEE-004 (5 Salvaguardas
      de Sinal), RULE-BB-002/004, RULE-GMC-001..005 (governança do CCM-001), RULE-EPI/CAU/MET/UNC/PRB/DEC/SEM
  - Princípios/4Es: GPR-001 PC-04 (piso de convicção — guard mínimo), PCO-06 (não-redução — Conviction Vector
      multidimensional por design), PB-06 (explicabilidade da ponderação), PB-08 (proporcionalidade),
      PB-09 (coerência/registro de conflito), PE-08 (independência de perspectivas); CEE-001 §12
      (Conformidade > Eficácia > Efetividade > Eficiência > Economicidade)

ADDED (delta local — o que esta spec acrescenta):
  - CCM-001 (Canonical Conviction Model): contrato canônico da Convicção Global (identidade, campos do
    Conviction Vector 8D, imutabilidade/versionamento, Separação Tríplice, governança GMC-001)
  - Evidence Fusion Engine (contrato operacional): consumo de ACTIVE, produção de DERIVED, mecânica de
    desconto anti-double-counting (calibração → J-001), avaliação de impacto de invalidação, Cognitive Depth
  - Conviction Engine (contrato operacional): normalização por dimensão, agregação NÃO-compensatória
    com precedência estrutural, tratamento de ausência/contraevidência/conflito/incerteza, robustez/
    sensibilidade/estabilidade/aging, convicção sobre subconjunto (macro) e vetor completo (global)
  - Gate Convicção→Decisão (CF-012, E3): piso ≥70% / 7-9 (interino), conflito direcional → NEUTRO
  - Guards: Separação Tríplice (CF-011) e INV-04 (CF-011/EC-CF-005)
  - Declaração de Classe/Mecanismo por BASpec (CC-11); Enforcement Contracts (EC-CF-001..006)

MODIFIED (especialização de regra herdada):
  - RULE-004 (evidências causalmente relacionadas = uma) — a SPEC-003 fornece a MECÂNICA de fusão/desconto
    que a SPEC-002 apenas representava como atributo. Extensão operacional do alcance, SEM alterar o texto de
    RULE-004 e SEM fixar a calibração numérica do desconto (→ J-001). Extensão de cobertura, não de significado
    (RULE-HD-02 respeitada).

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal / obrigação-a-obrigação** sobre **modelos canônicos e método** (EUA-E04 §8.3). O eixo **VERTICAL** (RULE-HV-01..04, conservação-como-conjunto pai→filha macro-harness) foi avaliado e **não se aplica**: a SPEC-003 não é decomposição *micro* de uma *macro-spec* — deriva de modelos canônicos vizinhos (CC-08), não de uma macro-spec. A regra ESCRITA de conservação-como-conjunto vertical será redigida junto da SPEC-019/derivadas; aqui não é invocada. [INFERÊNCIA — a confirmar pelo Revisor]

---

## Declaração de acepção semântica (RULE-SEM-01 — CC-10)

> **Termo:** "Conviction Engine". **Acepção adotada por esta Spec (delta v1.2 / DHR-ARQ-001, 2026-10-01):** **(b)** "Conviction Engine" é **mecanismo** (rótulo legado de arquitetura-para-código) — **mecanismo de fusão + cálculo do Conviction Vector 8D, Classe D/H do CCM-001 — INVOCADO pelo Manager Agent — Fase 2 (Conviction)** (ADR-MANAGER-001 §2.1/§2.3; CEM-001 notas DIV-CEM-4; `WORKFLOW.md` WF-04/WF-06). **Não** se cria agente/componente "Conviction Engine" independente. **Acepção legada, registrada e SUPERSEDIDA-em-parte (INV-07):** **(a)** componente **SEPARADO** do Kernel na topologia Fusion→Conviction→Synthesis (B-001, Questionário v1). Por instrução direta de Andraus, **(a) está parcialmente supersedida por (b)** na parte "componente/agente separado" — o que B-001 preserva é a separação **lógica** de etapas/mecanismos (Fusão→cálculo do Conviction Vector→síntese), agora invocadas pelo Manager Fase 2. A mudança é de **framing** (como o termo é lido), não de mérito das BASpecs (os três mecanismos cobertos permanecem; BASpecs não renumeradas). `WF-C01` declara a direção macro×global (um vetor, duas leituras) sem decidir 1x/2x (Q-A5) nem J-001. CONFLITO-1 **resolvido**; não é mais reconciliação pendente. (RULE-SEM-01; PB-09 conflito registrado e agora dirimido por Andraus.) [FONTE: ADR-MANAGER-001 §2.1/§2.3; CEM-001 DIV-CEM-4; DHR-ARQ-001; WORKFLOW.md WF-C01/WF-04/WF-06 versão vigente; RULE-SEM-01; research.md §3.3/§4 CONFLITO-1]

---

## Conformidade com o `WORKFLOW.md` (RULE-ECC-05 — lente 3; atomic-spec v1.5 = confronto E conformidade)

> **Autoridade:** o `WORKFLOW.md` (versão vigente) é fonte soberana do setup operacional; a SPEC-003 **conforma-se** a ele e **não** o edita; divergência seria achado do Revisor, resolvida por Andraus. A SPEC-003 **não fecha nenhuma `WF-Dxx` aberta**.

**IDs `WF-xx` tocados por esta Spec (mecanismo-apenas, sem invadir Manager/Risk/J-001):**

| WF-xx | Conteúdo (resumo) | Como a SPEC-003 se conforma | Onde |
|---|---|---|---|
| **WF-C01** | Convicção macro × global = um Conviction Vector 8D, duas leituras (macro = subconjunto Fase 1; global = +operacional); direção declarada, 1x/2x e fórmula não fechados | O CCM-001 computa convicção sobre **subconjunto** (macro) e **vetor completo** (global) pelo **mesmo** contrato; a invocação **2x** está **decidida** (WF-C01/Q-A5, DHR-DEC-001) e é do Manager (SPEC-008/014) — a Spec **não a implementa**; fórmula = J-001 (aberta) | CF-010; RULE-CF-010; CC-10 |
| **WF-C02** | Confluência vale por **independência**, não por contagem (anti double-counting) | Fusão conta evidências causalmente relacionadas como **uma**; não afirma independência não verificada; calibração do desconto → J-001 | CF-002; RULE-CF-002 |
| **WF-C03** | Order flow (CVD/delta/absorção) → **dimensão de volume**; dado faltante/ruim = **INDETERMINADO** (nunca zero/fabricado) | Dimensão sem evidência suficiente → **INDETERMINADO**, incerteza localizada, sem número fabricado | CF-007; RULE-CF-006 |
| **WF-C04** | **Regime** (tendência/range/alta vol.) é **dimensão de convicção, não gate**; em qual das 8 dimensões entra = **deixado para a SPEC-003** | Regime tratado como **dimensão** (não gate); **em qual das 8 dimensões** é **[DECISÃO NECESSÁRIA: Q-A9]** — proposta de opções + recomendação para Andraus; **não decidido aqui** | RULE-CF-003 (nota); Q-A9 |
| **WF-X03** / INV-04 | Fluxo unidirecional convicção→risco; risco **nunca** retroalimenta a convicção | Custo/sizing/alavancagem/R:R **nunca** entram no Conviction Vector; guard fail-closed | CF-008; CF-011; EC-CF-004 |
| **WF-A01** | Objeto do alarme traz `parent_id` da hipótese-origem (gatilho de análise, nunca ordem — INV-05) | A convicção referencia a hipótese-origem (`hypothesis_ref`, não redefinida — Separação Tríplice); o **objeto alarme** e seu `parent_id` são **do Manager** (WF-A01), consumidos, não produzidos pela SPEC-003 | CF-013; CCM-001 (Origem); INV-05 |
| **WF-V02** | Rótulo de **qualidade de evidência por escola** visível no raciocínio | O rótulo por escola (produzido na SPEC-002/agentes) é **preservado na reconstrução/linhagem** da fusão, não sobrescrito; evidência fraca ≠ descartada | CF-011; D9; RULE-CF-011 |
| **WF-P02** / N-001 | Parâmetros por ativo (pesos, limiares de volume) = mecanismo parametrizável; valores → N-001/backtest | O CCM-001 **suporta** pesos por ativo como **mecanismo**; valores definitivos = **N-001 (aberto)** | CF-009; RULE-CF-003 |

**Verificação da lente (3):** (i) todos os `WF-xx` citados **existem** na `WORKFLOW.md` (versão vigente); (ii) **nenhum** é contraditado — a SPEC-003 implementa o mecanismo que cada WF pressupõe, respeitando INV-01/04/05; (iii) **nenhuma `WF-Dxx` aberta é tratada como fechada**: `WF-D03` permanece aberta no resíduo J-001/N-001/WF-C04-Q-A9 (o nº de invocações **saiu** do resíduo — **Q-A5 FECHADA, 2x, por Andraus [WF-C01/DHR-DEC-001]**, invocação do Manager); `WF-D01/D02/D04` **já estavam fechadas** por Andraus e **não** são especificadas aqui (Manager/Scheduler e agentes). [FONTE: WORKFLOW.md versão vigente; RULE-ECC-05; ROADMAP §32; DHR-WF-001/002]

---

## D0 — Missão (Intenção)

A SPEC-003 especifica **como o SOT funde evidências independentes e dependentes em evidência derivada (CEM-001) e agrega a convicção em um Conviction Vector de 8 dimensões — explicável, robusto e auditável — redigindo o CCM-001 (Canonical Conviction Model) como contrato canônico da Convicção Global**, preservando: a **Separação Tríplice** (Evidence Strength × Hypothesis Confidence × Global Conviction — nenhum contamina o outro); a **hierarquia analítica inviolável** (estrutural/Elliott precede e veta; agregação **não-compensatória**); as **Salvaguardas de Sinal** (CEE-001 §11); e a fronteira **INV-04** (custo/dimensionamento NUNCA entram na convicção). Entrega o vetor de convicção ao **Synthesis Agent (SPEC-014)** — **sem executar decisão, sem emitir sinal e sem dimensionar risco**. [FONTE: ROADMAP §4/§143; research.md §5.2]

Os três **mecanismos** cobertos (não agentes autônomos — DHR-ARQ-001; B-001 parcialmente SUPERSEDIDA na parte "componente separado"): **(1) Evidence Fusion Engine** (único ENGINE PRODUCER de evidência DERIVED — CEM-001 Cap.2/6; mecanismo determinístico); **(2) Conviction Engine** — **mecanismo (Classe D/H do CCM-001) invocado pelo Manager Agent — Fase 2 (Conviction)** que calcula o Conviction Vector 8D; **(3) CCM-001** (contrato canônico redigido). A **síntese/decisão** fica a jusante (Manager Agent — Fase 2 / SPEC-014/SPEC-015, fora do escopo desta Spec). A unificação do Manager (fronteira SPEC-008×SPEC-015) **não é fechada aqui** (proposta EUA-E23; CONS-01). [FONTE: research.md §0/§5.1 Opção A homologada; ADR-MANAGER-001; DHR-ARQ-001]

**O que a Missão NÃO é (fronteira):**
- Não redefine CEM-001 nem CHM-001 (estrutura, campos, ciclo de vida, linhagem, Separação Tríplice) → **CC-02/CONST-01**.
- Não fecha os **valores/pesos definitivos** de fórmula/limiares (J-001) nem pesos por ativo (N-001) — fixa **estrutura/método/mecanismo + limiares-piloto interinos**; definitivos são pós-backtest → **J-001 / N-001 (pendentes)**.
- Não faz **Síntese / árbitro / TMP / Signal Package** → **SPEC-014 / Risk Agent**.
- Não faz **position sizing, alavancagem, R:R, Portfolio Heat, Kelly** → **Risk Agent / RISK-SPEC** (INV-04; SRC-03/04 [EXTERNO] adiados).
- Não **resolve** conflito de evidência de forma nova (a SPEC-002 já detecta/registra; aqui é **consumido** como insumo da fusão/agregação) — a resolução direcional vive na agregação não-compensatória e no gate, não como reinvenção da detecção.
- Não fecha **estados do Blackboard** para objetos não-hipótese (publicação do Conviction Vector) → **M-001 / SPEC-004 (pendente)**.
- Não **implementa nem é dona** da invocação do motor — o número de invocações está **DECIDIDO por Andraus: 2x por ciclo** (macro Fase 1 / global Fase 2; WF-C01, Q-A5 FECHADA, DHR-DEC-001) e a invocação é do **Manager** (SPEC-008 Fase 1 / SPEC-014 Fase 2). A SPEC-003 só fornece o **mecanismo** de convicção sobre subconjunto/vetor-completo; a direção macro×global é declarada em WF-C01.
- Não especifica **Killzone (WF-D01), alarme-gatilho (WF-D02) nem onde o ICT entra (WF-D04)** — **FECHADOS por Andraus** na `WORKFLOW.md` (versão vigente) e de responsabilidade do **Manager/Scheduler (SPEC-008/015)** e dos **agentes (SPEC-010..014)**, não do Conviction/Fusion Engine.
- Não decide **em qual das 8 dimensões entra o regime** (WF-C04) → **[DECISÃO NECESSÁRIA: Q-A9]** — a Spec propõe opções com recomendação; a decisão é de Andraus.

**Status epistemológico:** a SPEC-003 é FATO ARQUITETURAL candidato a baseline; o CCM-001 por ela redigido é [PROPOSTA] até homologação. CEM-001, CHM-001, SPEC-001/002/019/020/021, atomic-spec v1.5, INV-*, ENF-*, RULES v1.5 são FATO NORMATIVO. Fontes externas (research.md §2, SRC-01..07) são [EXTERNO] — DADO, nunca baseline; documentado ≠ homologado (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | **CCM-001 (Canonical Conviction Model):** contrato canônico da Convicção Global — identidade, campos do Conviction Vector 8D, imutabilidade/versionamento, Separação Tríplice, governança GMC-001 | CHM-001 §1.9/§2.14; GMC-001; research.md §5.3(1) |
| S2 | **Evidence Fusion Engine:** consumo de evidência ACTIVE (CEM-001), produção de DERIVED (único ENGINE PRODUCER), mecânica de desconto anti-double-counting (calibração→J-001), avaliação de impacto de invalidação, Cognitive Depth | CEM-001 Cap.2/4/5/6; RULE-004; research.md §5.3(2) |
| S3 | **Conviction Engine / Conviction Vector 8D:** escalas, normalização por dimensão, pesos (mecanismo; valores→J-001/N-001), independência/correlação, ausência/contraevidência/conflito/consenso, robustez/sensibilidade/aging/estabilidade, agregação, limites, incerteza, cálculo da convicção global, explicabilidade (PB-06) | ROADMAP §143; GPR-001 PCO-06/PB-06; research.md §5.3(3) |
| S4 | **Preservação da hierarquia e Salvaguardas:** agregação **NÃO-compensatória** (estrutural precede/veta; conflito direcional→NEUTRO; gates de sinal); Elliott-veto (RULE-SY-001) | INV-01; RULE-005/SY-001; CEE-001 §11; research.md §5.3(4) |
| S5 | **Convicção macro vs. global (mecanismo):** o CCM-001 suporta convicção sobre **subconjunto** de dimensões (macro: estrutural+institucional) e sobre o **vetor completo** (global: +operacional) — o mecanismo. A invocação **2x por ciclo** está **decidida** (WF-C01/Q-A5, DHR-DEC-001) e é do **Manager** (SPEC-008 Fase 1 / SPEC-014 Fase 2); a Spec fornece o mecanismo, **não** a invocação | WORKFLOW.md WF-C01/WF-04/WF-06; research.md §5.3(5)/§5.7 |
| S6 | **Limiares-piloto interinos** ≥70% / 7-9 como FATO NORMATIVO interino (Questionário v1); gate Convicção→Decisão | AGENTS.md §6; RULE-003/SY-003/CEE-004; research.md §6-bis Q-A4 |
| S7 | **Enforcement Contracts** dos atos com efeito: piso **E2** (Evidência/Engine); **E3** no gate Convicção→Decisão (crítico/irreversível; fail-closed; ENF-07 falso-DENY) | ENF-01/02/04/07; atomic-spec §10.2; research.md §5.3(6) |
| S8 | **Classe/Mecanismo por BASpec** (CC-11) e **Auditabilidade (D9 por referência)** para reconstrução da convicção (P13; RULE-010) | RULE-MECH-01; CONSTITUTION P13; RULE-010; research.md §5.3(7) |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Redefinir CEM-001 (estrutura/campos/ciclo/linhagem/eventos/governança) ou CHM-001 (Separação Tríplice, Confidence) | CEM-001 / CHM-001 (BASELINE) | CC-02/CONST-01 |
| **Valores/pesos definitivos** de fórmula/limiares e pesos por ativo | **J-001 / N-001 (pendentes)** — pós-backtest | A Spec fixa estrutura/método/mecanismo + limiares-piloto; definitivos são [DECISÃO NECESSÁRIA] (Q-A4) |
| **Synthesis Agent / árbitro / TMP / Signal Package** | **SPEC-014 / Risk Agent** | A jusante do Conviction Engine (B-001) |
| **Position sizing / alavancagem / R:R / Portfolio Heat / Kelly** | **Risk Agent / RISK-SPEC** | INV-04; SRC-03/04 [EXTERNO] ADIADOS; convicção ≠ sizing/custo |
| **Resolução** (detecção/registro) de conflito de evidência | **SPEC-002 (já faz)** | A SPEC-003 **consome** o conflito registrado; a agregação não-compensatória e o gate tratam o conflito **direcional** para a convicção, não reinventam a detecção |
| **Estados do Blackboard** para objetos não-hipótese (publicação do Conviction Vector) | **M-001 / SPEC-004 (pendente)** | M-001 em aberto — não fechar (CONS-01) |
| **Storage físico / Knowledge Graph / Cognitive Trace Reconstruction** | **SPEC-004 / SPEC-006 / H-001 (pendente)** | Infraestrutura |
| **Killzone (WF-D01), alarme-gatilho (WF-D02), papel do ICT (WF-D04)** | **Manager/Scheduler (SPEC-008/015) e agentes (SPEC-010..014)** | **FECHADOS** por Andraus na `WORKFLOW.md` (versão vigente); fora do escopo do Conviction/Fusion Engine — a SPEC-003 não os especifica |
| **Invocação do motor (nº de vezes) e dimensão do regime (WF-C04)** | **Manager Fase 1/2 (SPEC-008/014)** para a invocação **2x já decidida** (WF-C01/Q-A5, DHR-DEC-001) · **SPEC-003** decide a dimensão do regime (Q-A9) usando `research-Q-A9-regime.md` | A invocação 2x é **dado herdado de WF-C01** (a Spec só dá o mecanismo, CF-010, não a implementa); a dimensão do regime segue **[DECISÃO NECESSÁRIA: Q-A9]** a cargo desta Spec; WF-D03 **ABERTA (residual)** = J-001/N-001/Q-A9 (CONS-01) |
| Adotar framework externo (Dempster-Shafer, Bayes/BMA, TOPSIS, confluência ponderada) como **baseline** | — | Rejeitados como baseline (research.md §4 CONFLITO-2/3); só referência de método; o contrato canônico é o CCM-001 |

---

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide** (homologado Q-A3). O Conviction/Fusion Engine é **infraestrutura de agregação transversal e domain-agnostic** — não define escopo de especialidade de mercado (Elliott/SMC/ICT). Nenhum `PD-xx` é proposto (CC-12 = N/A homologado, research.md §6-bis Q-A3). Registrado explicitamente para o Revisor — não é supressão silenciosa. Nuance honesta (RULE-MET-01): RULE-ECC-05 incidir não arrasta RULE-PD-01 (gatilhos distintos). [FONTE: RULE-PD-01; atomic-spec §10.7; research.md §5.8(3)]

---

## D2 — Regras

> **Etiqueta:** as RULE-CF-* e o CCM-001 abaixo são **[PROPOSTA]** — tornam-se normativos apenas na homologação de Andraus + registro pelo Controlador (RULE-HG-02). Até lá, não são invocáveis como FATO NORMATIVO. As RULE/INV/ENF citadas como fundamento (CEM-001, CHM-001, INV-01/03/04/05/06/07/10, ENF-03/04/07, RULE-002/003/004/005/008/010, RULE-SY-001/003, RULE-CEE-004, RULE-GMC-*, RULE-EPI/CAU/MET/UNC/PRB/DEC/SEM, GPR-001 PC-04/PCO-06/PB-06) **já existem** e são FATO NORMATIVO (RULES.md v1.5 / atomic-spec v1.5 / GPR-001).

```
RULE-CF-001: O Evidence Fusion Engine é o ÚNICO ENGINE PRODUCER autorizado a produzir evidência DERIVED;
             consome apenas evidência ACTIVE (CEM-001 Cap.4/6). Fusão produzida por produtor não
             autorizado, ou a partir de evidência não-ACTIVE, é rejeitada (fail-closed).
             [Fonte: CEM-001 Cap.2/4/6; INV-06]  [PROPOSTA]

RULE-CF-002: A fusão de evidências DEVE respeitar a (in)dependência representada pela SPEC-002: evidências
             causalmente relacionadas contam como UMA (anti-double-counting). O Fusion Engine NÃO DEVE
             afirmar independência que não verificou (RULE-MET-01) nem inferir dependência causal por mera
             co-ocorrência/correlação (RULE-CAU-01). A CALIBRAÇÃO numérica do desconto é J-001 (não fixada).
             [Fonte: RULE-004; RULE-MET-01; RULE-CAU-01; J-001]  [PROPOSTA]

RULE-CF-003: O Conviction Vector tem EXATAMENTE 8 dimensões (estrutural, geométrica, fractal, institucional,
             operacional, temporal, volume, histórica — Questionário v1); NÃO DEVE ser colapsado em pontuação única
             quando múltiplas dimensões são relevantes (PCO-06 não-redução). Dimensionalidade é fechada;
             fórmula/pesos/limiares definitivos são J-001/N-001 (não fixados).
             [Fonte: INV-03; GPR-001 PCO-06; J-001; N-001]  [PROPOSTA]

RULE-CF-004: Cada dimensão DEVE ser normalizada para uma escala comum ANTES da agregação, preservando a
             modalidade/nuance material (RULE-SEM-03) e sem introduzir falsa precisão (RULE-PRB-02). O método
             de normalização é determinístico e explicável (PB-06); a escala/parâmetros definitivos são J-001.
             [Fonte: GPR-001 PB-06; RULE-SEM-03; RULE-PRB-02; J-001]  [PROPOSTA]

RULE-CF-005: A agregação do Conviction Vector é NÃO-COMPENSATÓRIA onde a hierarquia exige: a dimensão
             estrutural (Elliott) tem precedência e veto; dimensões inferiores confirmam/enfraquecem, NUNCA
             sobrepõem a superior (INV-01/RULE-008). Agregação puramente compensatória (TOPSIS) e "votos"
             simétricos (SRC-05/SRC-06 [EXTERNO]) são REJEITADOS como baseline.
             [Fonte: INV-01; RULE-008; RULE-SY-001; research.md §3.1 CONFLITO-2]  [PROPOSTA]

RULE-CF-006: Ausência de evidência, contraevidência e conflito DEVEM ser tratados sem fabricar convicção:
             ausência ≠ evidência de ausência; incerteza material → INDETERMINADO (não forçar PASS/FAIL nem
             número). Conflito direcional Elliott×SMC → saída NEUTRA (RULE-005/SY-001).
             [Fonte: RULE-EPI-01; RULE-UNC-03; RULE-MET-01; RULE-005; RULE-SY-001]  [PROPOSTA]

RULE-CF-007: A Separação Tríplice é inviolável: Evidence Strength (CEM, peso local), Hypothesis Confidence
             (CHM) e Global Conviction (CCM) NÃO DEVEM contaminar-se. O CCM-001 calcula a Global Conviction e
             NÃO redefine Confidence de hipótese nem Evidence Strength.
             [Fonte: CHM-001 §1.9/§2.14; INV-10]  [PROPOSTA]

RULE-CF-008: Custo/latência/dimensionamento/alavancagem NUNCA entram no Conviction Vector (INV-04).
             Convicção ≠ Score ≠ sizing. Sizing/risco-retorno (Kelly, R-multiple) são do Risk Agent (a jusante).
             [Fonte: INV-04; CEE-001 §10 Salv.4; SRC-03/04 [EXTERNO] ADIADOS]  [PROPOSTA]

RULE-CF-009: O gate Convicção→Decisão aplica os limiares-piloto interinos (convicção global ≥ 70%;
             score ≥ 7/9) como FATO NORMATIVO interino (Questionário v1, recalibrável pós-backtest), além de conflito
             direcional → NEUTRO. Os limiares definitivos são J-001 (não fixados). O gate é determinístico;
             o LLM é detector, nunca o gate (ENF-03).
             [Fonte: RULE-003/SY-003; RULE-CEE-004; ENF-03; J-001]  [PROPOSTA]

RULE-CF-010: O CCM-001 DEVE suportar convicção computada sobre SUBCONJUNTO de dimensões (macro) e sobre o
             VETOR COMPLETO (global) — o mecanismo. O NÚMERO de invocações está FECHADO em 2x por ciclo
             (macro Fase 1 / global Fase 2; WF-C01, Q-A5, DHR-DEC-001); essa invocação é do Manager
             (SPEC-008 Fase 1 / SPEC-014 Fase 2) e NÃO é implementada por esta Spec — o CCM-001 apenas provê
             o mecanismo invocável.
             [Fonte: WORKFLOW.md WF-C01/WF-04/WF-06; DHR-DEC-001; research.md §5.7]  [PROPOSTA]

RULE-CF-011: Toda convicção publicada DEVE ser rastreável e reconstruível (RULE-010; P13): dimensões de
             entrada, normalização, pesos aplicados, regra de agregação, conflitos, robustez/sensibilidade e
             resultado. Explicabilidade da ponderação é requisito, não opção (PB-06).
             [Fonte: RULE-010; CONSTITUTION P13; GPR-001 PB-06]  [PROPOSTA]

RULE-CF-012: O CCM-001 é modelo canônico e segue a governança GMC-001 (universal BTC/XAU/NASDAQ, neutro,
             reutilizável, baixo acoplamento; alteração por fluxo Estrategista→Analista→Controlador).
             [Fonte: RULE-GMC-001..005; GMC-001]  [PROPOSTA]
```

> **Nota WF-C04 — regime como DIMENSÃO, não gate [DECISÃO NECESSÁRIA: Q-A9]:** a `WORKFLOW.md` (versão vigente, WF-C04) declara que o **regime** (tendência/range/alta volatilidade) é **dimensão de convicção, não gate**, e **deixa para a SPEC-003** definir **em qual das 8 dimensões (fechadas)** ele entra. A SPEC-003 **conforma-se** ao princípio (regime não é gate — não cria 9ª dimensão, INV-03) mas **não decide** a dimensão-alvo: é **[DECISÃO NECESSÁRIA]** registrada em **Q-A9** (research.md §8 + dossiê dedicado `research-Q-A9-regime.md`, não-normativo, aprofundamento por pesquisa de trading — 2026-10-01), com opções e recomendação para Andraus (Opção A=temporal recomendada; C=estrutural rejeitada por contaminar o veto INV-01). Até a decisão, o mapeamento do regime a uma das 8 dimensões é **INDETERMINADO** (CONS-01; não fabricar). [FONTE: WORKFLOW.md WF-C04 versão vigente; INV-03; RULE-CF-003; Q-A9; research-Q-A9-regime.md] **Decisão de Andraus (chat, 2026-10-01):** Q-A9 **permanece ABERTA e fica a cargo da SPEC-003** (a Spec decide em qual das 8 dimensões entra o regime), usando `research-Q-A9-regime.md` (não-normativo, [EXTERNO]) como **fonte de dados**; a recomendação do dossiê (temporal) é insumo, não decisão.

---

## Critérios de Aceitação (EARS)

1. Quando o Fusion Engine recebe evidências ACTIVE para fundir, o Fusion Engine DEVE produzir evidência DERIVED com Lineage preenchida (CEM-001 Cap.5) e NÃO DEVE consumir evidência não-ACTIVE.
2. Quando duas evidências candidatas têm relação de dependência representada pela SPEC-002, o Fusion Engine DEVE contá-las como uma (anti-double-counting) e NÃO DEVE afirmar independência não verificada.
3. Quando o Conviction Engine agrega as dimensões, o Conviction Engine DEVE normalizar cada dimensão para escala comum antes de agregar e DEVE preservar as 8 dimensões (não colapsar — PCO-06).
4. Quando a dimensão estrutural é fraca ou conflitante, o Conviction Engine NÃO DEVE compensá-la com dimensões inferiores (agregação não-compensatória; estrutural precede/veta).
5. Quando há conflito direcional Elliott×SMC, o Conviction Engine DEVE produzir resultado que força saída NEUTRA no gate (RULE-005/SY-001).
6. Quando uma dimensão não tem evidência suficiente, o Conviction Engine DEVE marcar INDETERMINADO para aquela dimensão e NÃO DEVE fabricar valor numérico.
7. Quando um processo tenta derivar convicção a partir de custo/sizing ou de Evidence Strength diretamente, o Conviction Engine DEVE rejeitar (INV-04 / Separação Tríplice).
8. Quando a convicção global e o score atingem os limiares-piloto (≥70% / 7-9) sem conflito direcional, o gate Convicção→Decisão DEVE habilitar o encaminhamento ao Synthesis; caso contrário DEVE bloquear (fail-closed).
9. Quando a convicção é publicada, o Conviction Engine DEVE registrar a reconstrução completa (dimensões, normalização, pesos, agregação, conflito, robustez) para auditoria (P13/RULE-010).
10. Quando uma evidência ancestral é invalidada, o Fusion Engine DEVE iniciar avaliação de impacto sobre as derivadas SEM cascata automática (CEM-001 Cap.4/5).

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec com efeito declara o bloco **CLASSE/MECANISMO** (§10.6). Classe D = determinístico; C = constitutivo (é o próprio gate); H = híbrido (LLM + gate de saída determinístico + bounded loop); P = probabilístico com gate (julgamento + critério de parada).

### BASpec-CF-001 — Fusion Engine: produção de evidência DERIVED (único ENGINE PRODUCER)

```
BASpec-CF-001:
  QUANDO:       O Fusion Engine recebe duas ou mais evidências ACTIVE para fundir
  ENTÃO:        Produz uma evidência DERIVED (Producer Type=ENGINE, Origin Type=DERIVED) com Lineage
                contendo os ancestrais diretos; evidência não-ACTIVE é rejeitada; produtor não autorizado
                é rejeitado (fail-closed)
  PORQUE:       O Fusion Engine é o único ENGINE PRODUCER e consome apenas ACTIVE (CEM-001 Cap.2/4/6; INV-06)
  REFERÊNCIA:   CEM-001 Cap.2/4/6; INV-06; RULE-CF-001
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de autorização de produtor + estado ACTIVE + coerência de Lineage
    GATE DE SAÍDA: verificação binária (producer∈autorizados ∧ ancestrais ACTIVE ∧ Lineage≠[])
    CRITÉRIO 4Es: Conformidade > Eficácia — proteger o contrato CEM-001 (DERIVED só ENGINE; só ACTIVE)
  VERIFICADO POR:
    DADO        EV-A e EV-B ACTIVE submetidas ao Fusion Engine
    QUANDO      a fusão é processada
    ENTÃO       EV-C DERIVED criada; Lineage == [EV-A, EV-B]; origin_type == "DERIVED"
    VERIFICAÇÃO ev_c.origin_type == "DERIVED"; ev_c.lineage == ["EV-A","EV-B"]
```

### BASpec-CF-002 — Fusão anti-double-counting de evidências dependentes

```
BASpec-CF-002:
  QUANDO:       O Fusion Engine funde evidências com relação de (in)dependência representada pela SPEC-002
  ENTÃO:        Evidências causalmente relacionadas são contadas como UMA (desconto de dependência); quando
                a independência não foi verificada, marca "undetermined" e declara a limitação — NÃO afirma
                independência; a CALIBRAÇÃO numérica do desconto NÃO é fixada (J-001)
  PORQUE:       Evidências causalmente relacionadas = uma (RULE-004); não fabricar independência (RULE-MET-01);
                dependência causal não se afirma por correlação (RULE-CAU-01); confluência vale por
                independência, não por contagem (WF-C02); calibração → J-001
  REFERÊNCIA:   RULE-004; RULE-MET-01; RULE-CAU-01; RULE-CF-002; WF-C02; J-001
  CLASSE/MECANISMO:
    CLASSE      : P (Probabilístico com Gate)
    MECANISMO   : julgamento (apoio semântico/LLM) sobre o atributo de dependência herdado da SPEC-002 →
                  aplica desconto estrutural; ENF-03 (detector≠gate — o veredito de contagem é determinístico)
    BOUNDED LOOP: uma passada por conjunto de evidências dependentes; encerra em "undetermined" quando o
                  discriminante é insuficiente (RULE-INQ-03); sem retry infinito
    CRITÉRIO 4Es: Eficácia — evitar double counting protege a qualidade da convicção; honestidade
                  (Conformidade) prevalece sobre "completar" o atributo
  VERIFICADO POR:
    DADO        EV-1 e EV-2 derivadas da mesma fonte única, atributo "dependent" (SPEC-002)
    QUANDO      o Fusion Engine funde
    ENTÃO       contribuição contada como 1 (não 2); independence_claimed == false
    VERIFICAÇÃO effective_count == 1; independence_claimed == false
```

### BASpec-CF-003 — Avaliação de impacto de invalidação sobre derivadas (não-cascata)

```
BASpec-CF-003:
  QUANDO:       Uma evidência ancestral na Lineage de uma evidência DERIVED é invalidada (Evidence Invalidated)
  ENTÃO:        O Fusion Engine inicia avaliação de impacto sobre as derivadas relacionadas SEM cascata
                automática; a decisão de manter/substituir/invalidar segue regras de linhagem; o objeto é
                preservado (INV-07)
  PORQUE:       Invalidação não implica cascata automática (CEM-001 Cap.4/5); o Fusion Engine é o responsável
                por iniciar a avaliação de impacto
  REFERÊNCIA:   CEM-001 Cap.4/Cap.5; INV-07; RULE-CF-001
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que barra cascata automática + dispara processo de avaliação de impacto
    GATE DE SAÍDA: verificação de que nenhuma invalidação em massa foi aplicada automaticamente
    CRITÉRIO 4Es: Conformidade > Eficácia — preservar não-cascata e histórico (INV-07)
  VERIFICADO POR:
    DADO        EV-ancestral invalidada, com EV-DERIVED dependente
    QUANDO      o evento Evidence Invalidated é processado
    ENTÃO       avaliação de impacto iniciada; auto_cascade_applied == false
    VERIFICAÇÃO impact_evaluation_started == true; auto_cascade_applied == false
```

### BASpec-CF-004 — Normalização por dimensão (escala comum)

```
BASpec-CF-004:
  QUANDO:       O Conviction Engine recebe as contribuições por dimensão (das 8 dimensões)
  ENTÃO:        Normaliza cada dimensão para uma escala comum antes de agregar, preservando modalidade/nuance
                (RULE-SEM-03); NÃO introduz precisão numérica sem base (RULE-PRB-02); os parâmetros de escala
                definitivos NÃO são fixados (J-001)
  PORQUE:       Agregar dimensões heterogêneas exige normalização explicável (PB-06); sem falsa precisão (J-001)
  REFERÊNCIA:   GPR-001 PB-06; RULE-SEM-03; RULE-PRB-02; RULE-CF-004; J-001
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : transformação determinística por dimensão para escala comum (método explicável); sem julgamento
    CRITÉRIO 4Es: Eficácia — normalização correta é pré-condição de agregação válida; determinismo garante P13
  VERIFICADO POR:
    DADO        contribuições em escalas distintas por dimensão
    QUANDO      a normalização roda
    ENTÃO       cada dimensão em escala comum; mapeamento reconstruível; nenhum valor definitivo de J-001 assumido
    VERIFICAÇÃO all(dim.normalized in common_scale); reconstruction_available == true
```

### BASpec-CF-005 — Agregação NÃO-compensatória (rejeita compensação pura)

```
BASpec-CF-005:
  QUANDO:       O Conviction Engine agrega as 8 dimensões normalizadas em convicção
  ENTÃO:        Aplica agregação NÃO-compensatória: dimensões inferiores NÃO podem compensar fraqueza/conflito
                da dimensão estrutural; rejeita agregação puramente compensatória (TOPSIS) e "votos" simétricos
                (SRC-05/SRC-06 [EXTERNO]); preserva as 8 dimensões (não colapsa — PCO-06)
  PORQUE:       Hierarquia inviolável: estrutural precede; inferior não sobrepõe superior (INV-01/RULE-008);
                compensação pura violaria CC-01 (research.md CONFLITO-2)
  REFERÊNCIA:   INV-01; RULE-008; GPR-001 PCO-06; RULE-CF-005; [EXTERNO] research.md SRC-05/SRC-06
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : agregação por regra estrutural-primeiro (determinística) + julgamento qualitativo das
                  interações entre dimensões; gate de saída determinístico que rejeita compensação da estrutural
    BOUNDED LOOP: uma passada de agregação por vetor; sem re-tentativa recursiva; INDETERMINADO se irredutível
    GATE DE SAÍDA: verificação de que nenhuma dimensão inferior elevou a convicção acima do que a estrutural permite
    CRITÉRIO 4Es: Conformidade > Eficácia — preservar hierarquia prevalece sobre "maximizar" o score
  VERIFICADO POR:
    DADO        estrutural fraca/baixa e institucional+operacional altas
    QUANDO      a agregação não-compensatória roda
    ENTÃO       convicção global limitada pela estrutural; compensação rejeitada
    VERIFICAÇÃO compensated_by_lower_dims == false; structural_precedence_preserved == true
```

### BASpec-CF-006 — Precedência/veto estrutural e conflito direcional → NEUTRO

```
BASpec-CF-006:
  QUANDO:       Há conflito direcional entre a dimensão estrutural (Elliott) e a institucional (SMC)
  ENTÃO:        O Conviction Engine produz um resultado que força saída NEUTRA no gate (Elliott-veto);
                NÃO resolve o conflito favorecendo SMC sobre Elliott
  PORQUE:       Elliott tem veto sobre direção; conflito Elliott×SMC → NEUTRO (RULE-005/SY-001/SY-002)
  REFERÊNCIA:   RULE-005; RULE-SY-001; RULE-SY-002; RULE-CF-006
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de veto estrutural (directional_conflict ⇒ NEUTRO)
    GATE DE SAÍDA: verificação binária (conflito direcional ⇒ saída NEUTRA obrigatória)
    CRITÉRIO 4Es: Conformidade > Eficácia — Salvaguarda de Sinal inviolável (CEE-001 §11 item 3)
  VERIFICADO POR:
    DADO        estrutural bullish e institucional bearish (directional_conflict=true)
    QUANDO      o gate de veto roda
    ENTÃO       saída = NEUTRO; conflito não resolvido a favor de SMC
    VERIFICAÇÃO output == "NEUTRO"; resolved_in_favor_of_smc == false
```

### BASpec-CF-007 — Ausência/contraevidência/incerteza → INDETERMINADO (não fabricar convicção)

```
BASpec-CF-007:
  QUANDO:       Uma dimensão do Conviction Vector não possui evidência suficiente, ou há contraevidência não
                resolvida, ou a incerteza é material
  ENTÃO:        O Conviction Engine marca aquela dimensão como INDETERMINADO e localiza a incerteza
                (RULE-MET-02); NÃO fabrica valor numérico; NÃO converte ausência em evidência de ausência
  PORQUE:       Ausência ≠ evidência de ausência; incerteza material → INDETERMINADO (RULE-EPI/UNC/MET);
                não quantificar sem base (RULE-PRB-02); order flow (CVD/delta/absorção) alimenta a dimensão
                de volume e, quando o dado falta/é ruim, é INDETERMINADO — nunca zero/fabricado (WF-C03)
  REFERÊNCIA:   RULE-EPI-01; RULE-UNC-01/03; RULE-MET-01/02; RULE-PRB-02; RULE-CF-006; WF-C03
  CLASSE/MECANISMO:
    CLASSE      : P (Probabilístico com Gate)
    MECANISMO   : julgamento (apoio semântico) sobre suficiência de evidência por dimensão → INDETERMINADO;
                  gate determinístico barra conversão de ausência em conclusão e número fabricado
    BOUNDED LOOP: avaliação única por dimensão; encerra em INDETERMINADO quando insuficiente (RULE-INQ-03)
    CRITÉRIO 4Es: Conformidade > Eficácia — honestidade epistêmica prevalece sobre "completar" o vetor
  VERIFICADO POR:
    DADO        dimensão volume sem evidência observável no timeframe
    QUANDO      o Conviction Engine avalia a dimensão
    ENTÃO       dimensão = INDETERMINADO; incerteza localizada; sem número fabricado; sem conclusão de ausência
    VERIFICAÇÃO dim_volume == "INDETERMINADO"; fabricated_value == false; absence_as_conclusion == false
```

### BASpec-CF-008 — Robustez / sensibilidade / estabilidade com explicabilidade

```
BASpec-CF-008:
  QUANDO:       A convicção global é calculada
  ENTÃO:        O Conviction Engine representa robustez/sensibilidade/estabilidade do resultado (quanto o
                resultado muda se pesos/dimensões variam — SRC-07 [EXTERNO] adaptado) como atributos explícitos
                e explicáveis (PB-06); a MÉTRICA definitiva de robustez NÃO é fixada (J-001)
  PORQUE:       Robustez/sensibilidade são propriedades explícitas da agregação (PB-06/PB-08); métrica
                definitiva → J-001 (research.md §3.1)
  REFERÊNCIA:   GPR-001 PB-06/PB-08; RULE-CF-011; J-001; [EXTERNO] research.md SRC-07
  CLASSE/MECANISMO:
    CLASSE      : P (Probabilístico com Gate)
    MECANISMO   : análise de sensibilidade (perturbação de pesos/dimensões) + julgamento qualitativo de
                  estabilidade; gate de saída opcional (resultado qualitativo/ordinal, não binário)
    BOUNDED LOOP: conjunto finito de perturbações declarado; encerra após o conjunto; sem varredura infinita
    CRITÉRIO 4Es: Efetividade — convicção robusta é mais útil a jusante; explicabilidade (Conformidade/PB-06)
  VERIFICADO POR:
    DADO        um vetor de convicção próximo do limiar-piloto
    QUANDO      a análise de sensibilidade roda sobre o conjunto declarado de perturbações
    ENTÃO       atributo de robustez/estabilidade representado e explicável; sem métrica numérica definitiva
    VERIFICAÇÃO robustness_attribute != null; explanation_available == true; definitive_metric_fixed == false
```

### BASpec-CF-009 — Aging e pesos por ativo (mecanismo; J-001/N-001 abertos)

```
BASpec-CF-009:
  QUANDO:       O Conviction Engine pondera dimensões por ativo (BTC/XAU/NASDAQ) e por idade da evidência
  ENTÃO:        Aplica o MECANISMO de pesos por ativo e de aging (decaimento temporal) que o CCM-001 suporta;
                os VALORES/pesos por ativo e o peso/decay temporal definitivos NÃO são fixados (N-001/J-001)
  PORQUE:       O CCM-001 deve suportar pesos por ativo (universalidade GMC-001) e aging; parâmetros por ativo
                são mecanismo parametrizável (WF-P02); valores → N-001/J-001 pós-backtest (research.md GAP-N)
  REFERÊNCIA:   RULE-GMC-001; CEM-001 Cap.3 (Timeframe Reference); RULE-CF-003; WF-P02; N-001; J-001
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : aplicação determinística de uma tabela de pesos (parametrizável) e função de aging; sem julgamento
    CRITÉRIO 4Es: Eficiência — mecanismo barato e reprodutível; Conformidade preserva J-001/N-001 (não antecipa valores)
  VERIFICADO POR:
    DADO        o mesmo vetor para BTC e para NASDAQ, com placeholders de pesos por ativo
    QUANDO      o mecanismo de pesos por ativo roda
    ENTÃO       o mecanismo aceita pesos por ativo sem fixar valores definitivos; aging aplicado como função
    VERIFICAÇÃO per_asset_weighting_supported == true; definitive_weights_fixed == false
```

### BASpec-CF-010 — Convicção sobre subconjunto (macro) e vetor completo (global)

```
BASpec-CF-010:
  QUANDO:       O consumidor (Manager/Scheduler) solicita convicção sobre um subconjunto de dimensões (macro:
                estrutural+institucional) ou sobre o vetor completo (global: +operacional)
  ENTÃO:        O CCM-001 computa a convicção sobre o conjunto de dimensões informado, usando o MESMO motor e
                contrato; a invocação é 2x por ciclo (decidida por Andraus — WF-C01/Q-A5) e é do Manager
                (SPEC-008 Fase 1 / SPEC-014 Fase 2) — esta Spec NÃO a implementa
  PORQUE:       O workflow usa convicção macro (Fase 1) e global (Fase 2) como UM vetor 8D em duas leituras —
                direção declarada por Andraus (WF-C01); a invocação 2x está FECHADA (Q-A5, DHR-DEC-001) e é do
                Manager, não da SPEC-003 (research.md §5.7; WF-C01)
  REFERÊNCIA:   WORKFLOW.md WF-C01/WF-04/WF-06; WORKFLOW-SOT-001; RULE-CF-010
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : o motor aceita o conjunto de dimensões como parâmetro; computa sobre o subconjunto informado
    CRITÉRIO 4Es: Efetividade — um único contrato consistente para macro e global; Conformidade não fixa invocação
  VERIFICADO POR:
    DADO        solicitação de convicção macro (estrutural+institucional) e, depois, global (vetor completo)
    QUANDO      o motor computa cada uma
    ENTÃO       ambas computadas pelo mesmo contrato; número de invocações não fixado pela Spec
    VERIFICAÇÃO macro_subset_supported == true; full_vector_supported == true; invocation_count_fixed == false
```

### BASpec-CF-011 — Guard Separação Tríplice + INV-04 (convicção ≠ strength ≠ custo/sizing)

```
BASpec-CF-011:
  QUANDO:       Um processo tenta derivar Global Conviction diretamente de Evidence Strength, de Hypothesis
                Confidence, ou de custo/sizing/alavancagem
  ENTÃO:        O Conviction Engine REJEITA a operação (fail-closed): Evidence Strength permanece peso local;
                Hypothesis Confidence permanece do CHM; custo/sizing nunca entram na convicção (INV-04)
  PORQUE:       Separação Tríplice inviolável (CHM-001 §1.9/§2.14); custo nunca no Conviction Vector (INV-04);
                fluxo unidirecional convicção→risco — o risco NUNCA retroalimenta a convicção (WF-X03/INV-04)
  REFERÊNCIA:   CHM-001 §1.9/§2.14; INV-04; INV-10; WF-X03; RULE-CF-007/008
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que barra contaminação entre os três níveis e a entrada de custo/sizing
    GATE DE SAÍDA: verificação de que nenhum campo de convicção foi derivado de Strength/Confidence/custo
    CRITÉRIO 4Es: Conformidade > Eficácia — INV-04 e Separação Tríplice são invioláveis
  VERIFICADO POR:
    DADO        processo tenta mapear Evidence Strength=0.8 (ou custo) em uma dimensão de convicção
    QUANDO      o guard roda
    ENTÃO       operação REJEITADA, código "CONVICTION_CONTAMINATION_FORBIDDEN"; nada contaminado
    VERIFICAÇÃO response.error_code == "CONVICTION_CONTAMINATION_FORBIDDEN"
```

### BASpec-CF-012 — Gate Convicção→Decisão (piso interino; conflito direcional → NEUTRO) [E3]

```
BASpec-CF-012:
  QUANDO:       A convicção global está calculada e é avaliada para habilitar o encaminhamento ao Synthesis
  ENTÃO:        O gate determinístico habilita o encaminhamento SOMENTE se (convicção global ≥ 70%) E
                (score ≥ 7/9) E (sem conflito direcional); caso contrário BLOQUEIA (fail-closed). Os limiares
                ≥70%/7-9 são FATO NORMATIVO interino (Questionário v1); os definitivos são J-001 (não fixados)
  PORQUE:       Salvaguardas de Sinal invioláveis (CEE-001 §11): convicção ≥70%, score 7/9, conflito→NEUTRO —
                limiares de Fase Piloto; gate determinístico, LLM nunca é o gate (ENF-03); efeito irreversível/
                crítico habilita Decision (ENF-04)
  REFERÊNCIA:   RULE-003/SY-003; RULE-CEE-004; RULE-005; ENF-03/04; J-001; RULE-CF-009
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico (comparação de limiares interinos + checagem de conflito direcional);
                  é o próprio gate; LLM pode ser detector, nunca o gate (ENF-03)
    GATE DE SAÍDA: verificação binária (≥70% ∧ ≥7/9 ∧ ¬directional_conflict) ⇒ habilita; senão bloqueia
    CRITÉRIO 4Es: Conformidade > Eficácia — o gate é a barreira de segurança crítica (PC-04); fail-closed
  VERIFICADO POR:
    DADO        convicção global 68% (abaixo do piloto ≥70%)
    QUANDO      o gate Convicção→Decisão roda
    ENTÃO       encaminhamento BLOQUEADO (fail-closed); nenhuma habilitação de Decision
    VERIFICAÇÃO gate_passed == false; decision_enabled == false
```

### BASpec-CF-013 — Publicação do Conviction Vector no Blackboard (M-001 aberta)

```
BASpec-CF-013:
  QUANDO:       O Conviction Vector 8D é calculado e deve ser disponibilizado a consumidores a jusante
  ENTÃO:        O Conviction Engine publica o vetor no workspace de sua responsabilidade (RULE-BB-002),
                append-only (RULE-BB-004), com reconstrução completa anexada (P13/RULE-010); os ESTADOS do
                Blackboard para este objeto não-hipótese referenciam M-001 (aberta) — NÃO são fixados aqui
  PORQUE:       Publicação em workspace próprio (RULE-BB-002/004); rastreabilidade (RULE-010/P13); a convicção
                referencia a hipótese-origem (hypothesis_ref) cujo `parent_id` é objeto do alarme do Manager
                (WF-A01, consumido, não produzido aqui — INV-05); estados de objeto não-hipótese = M-001
                (SPEC-004, aberta — CONS-01)
  REFERÊNCIA:   RULE-BB-002/004; RULE-010; CONSTITUTION P13; WF-A01; INV-05; M-001; RULE-CF-011
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de publicação (workspace próprio; append-only; reconstrução anexada);
                  não fixa estados do Blackboard (referencia M-001)
    GATE DE SAÍDA: verificação de workspace correto + append-only + reconstrução presente
    CRITÉRIO 4Es: Conformidade > Eficácia — publicação íntegra e auditável; não antecipar M-001
  VERIFICADO POR:
    DADO        Conviction Vector calculado, com reconstrução completa
    QUANDO      a publicação roda
    ENTÃO       vetor publicado append-only no workspace próprio; reconstrução anexada; estados = M-001 (aberta)
    VERIFICAÇÃO published_append_only == true; reconstruction_attached == true; blackboard_states_fixed == false
```

---

## D4 — Algoritmo

**Parcialmente N/A como fórmula numérica definitiva.** A estrutura/método da agregação é especificada (normalização por dimensão → agregação não-compensatória estrutural-primeiro → gate de limiares interinos), mas as **fórmulas/pesos/limiares definitivos** dependem de **J-001/N-001** (pós-backtest; BUILD/VERIFY adiados — ROADMAP §22; RULE-MM-06/RULE-EV-05). Fixá-los agora violaria INV-03/CONS-01.

Mecânicas **determinísticas reais** especificáveis sem J-001 (D4 "onde há regra determinística real" — atomic-spec §2):
- **Normalização (CF-004):** transformação por dimensão para escala comum — método determinístico e reconstruível; parâmetros de escala definitivos = J-001.
- **Veto estrutural (CF-006):** `directional_conflict(Elliott, SMC) == true ⇒ saída NEUTRA` — regra binária, sem parâmetro.
- **Gate (CF-012):** `habilita ⇔ (conv_global ≥ 0.70) ∧ (score ≥ 7/9) ∧ (¬directional_conflict)` — os limiares são os interinos homologados (Questionário v1), recalibráveis; definitivos = J-001.
- **Aging/pesos (CF-009):** forma funcional parametrizável (pesos por ativo como tabela; aging como função do Timeframe Reference), com **valores em aberto** (N-001/J-001).

A agregação não-compensatória completa (forma exata, pesos, limiares) é **[DECISÃO NECESSÁRIA: J-001/N-001]** — a Spec fixa o **método/mecanismo**, não os números. [FONTE: J-001 pendente; N-001 pendente; atomic-spec §2; research.md GAP-J/GAP-N]

---

## D5 — Máquina de estados (ciclo da convicção; CEM-001 Cap.4 para a evidência — não redefinido)

A **evidência** (entrada/saída da fusão) segue o ciclo de vida do **CEM-001 Cap.4** (ACTIVE→SUPERSEDED/INVALIDATED/ARCHIVED; transições proibidas; Status único campo mutável; não-cascata) — **não redefinido** pela SPEC-003.

O **objeto Conviction Vector** (produto do CCM-001) tem um ciclo operacional mínimo [PROPOSTA]:

| Estado | Descrição | Transições |
|---|---|---|
| COMPUTED | Vetor calculado, ainda não avaliado pelo gate | → GATED |
| GATED_PASS | Passou o gate Convicção→Decisão (≥70%/7-9, sem conflito) | → SUPERSEDED (por recálculo) |
| GATED_BLOCK | Bloqueado pelo gate (fail-closed) | → SUPERSEDED (por recálculo) |
| SUPERSEDED | Substituído por novo cálculo (versionamento monotônico — INV-07) | terminal operacional |

> **Fronteira M-001 [DECISÃO NECESSÁRIA — aberta]:** os **estados do Blackboard** para este objeto não-hipótese dependem de **M-001** (SPEC-004, aberta). O ciclo acima é o **ciclo do objeto convicção** (recálculo/versão), NÃO os estados do Blackboard — estes não são fixados aqui (CONS-01; Q-A8). [FONTE: M-001; RULE-BB-003; research.md GAP-M]

---

## D6 — Protocolo de publicação no Blackboard

### Workspace e produtores [FONTE: RULE-BB-002; CEM-001 Cap.6]

| Produtor | Publica |
|---|---|
| Fusion Engine (ENGINE) | Evidência DERIVED (workspace de Evidência) |
| Conviction Engine | Conviction Vector 8D (workspace de Convicção) |

### Sequência (pipeline B-001: Fusion → Conviction → [Synthesis, SPEC-014])

1. **Consumo:** Conviction Engine lê evidência ACTIVE (própria + DERIVED do Fusion Engine) e Hypothesis Confidence (CHM) — **sem contaminar** (Separação Tríplice, CF-011).
2. **Fusão (Fusion Engine):** produz DERIVED (CF-001); aplica anti-double-counting (CF-002); avaliação de impacto de invalidação quando aplicável (CF-003).
3. **Normalização (CF-004)** por dimensão.
4. **Agregação não-compensatória (CF-005)** com precedência estrutural; veto direcional → NEUTRO (CF-006).
5. **Tratamento de ausência/incerteza (CF-007)** → INDETERMINADO por dimensão quando aplicável.
6. **Robustez/sensibilidade (CF-008)**; aging/pesos por ativo (CF-009, mecanismo).
7. **Convicção macro (subconjunto) ou global (vetor completo)** conforme solicitado (CF-010).
8. **Guards** Separação Tríplice/INV-04 (CF-011) ao longo do cálculo.
9. **Gate Convicção→Decisão (CF-012, E3):** habilita/bloqueia (fail-closed).
10. **Publicação (CF-013):** vetor + reconstrução completa (P13/RULE-010), append-only; estados do Blackboard = **M-001 (aberta)**.
11. **Encaminhamento:** ao **Synthesis Agent (SPEC-014)** — fora do escopo.

> **Nota de invocação [Q-A5 FECHADA — Andraus, DHR-DEC-001]:** o número de invocações do motor está **decidido: 2x por ciclo** (macro na Fase 1; global na Fase 2 — WF-C01) e é do **Manager** (SPEC-008 Fase 1 / SPEC-014 Fase 2). A Spec só fornece o mecanismo (CF-010), **não** implementa a invocação. O resíduo aberto de WF-D03 é J-001/N-001 e a dimensão do regime (Q-A9). [FONTE: WORKFLOW.md WF-C01; DHR-DEC-001]

---

## D7 — Cenários de Teste

### Cenário-CF-T01 — Fusão válida produz DERIVED
```
DADO        EV-A e EV-B ACTIVE submetidas ao Fusion Engine
QUANDO      a fusão roda
ENTÃO       EV-C DERIVED criada; Lineage=[EV-A,EV-B]; origin_type="DERIVED"
VERIFICAÇÃO ev_c.origin_type == "DERIVED"; ev_c.lineage == ["EV-A","EV-B"]
```

### Cenário-CF-T02 — Anti-double-counting de dependentes
```
DADO        EV-1 e EV-2 de fonte única, atributo "dependent" (SPEC-002)
QUANDO      o Fusion Engine funde
ENTÃO       contribuição efetiva = 1; independência não afirmada
VERIFICAÇÃO effective_count == 1; independence_claimed == false
```

### Cenário-CF-T03 — Agregação não-compensatória (estrutural fraca limita a convicção)
```
DADO        estrutural baixa; institucional+operacional altas
QUANDO      a agregação roda
ENTÃO       convicção limitada pela estrutural; compensação rejeitada
VERIFICAÇÃO compensated_by_lower_dims == false
```

### Cenário-CF-T04 — Conflito direcional → NEUTRO
```
DADO        estrutural bullish, institucional bearish (directional_conflict=true)
QUANDO      o gate de veto roda
ENTÃO       saída = NEUTRO
VERIFICAÇÃO output == "NEUTRO"; resolved_in_favor_of_smc == false
```

### Cenário-CF-T05 — Dimensão sem evidência → INDETERMINADO
```
DADO        dimensão volume sem evidência observável
QUANDO      o Conviction Engine avalia
ENTÃO       dim_volume = INDETERMINADO; sem número fabricado; sem conclusão de ausência
VERIFICAÇÃO dim_volume == "INDETERMINADO"; fabricated_value == false
```

### Cenário-CF-T06 — INV-04 / Separação Tríplice (strength/custo não vira convicção)
```
DADO        processo tenta mapear Evidence Strength (ou custo) em dimensão de convicção
QUANDO      o guard CF-011 roda
ENTÃO       rejeição "CONVICTION_CONTAMINATION_FORBIDDEN"
VERIFICAÇÃO response.error_code == "CONVICTION_CONTAMINATION_FORBIDDEN"
```

### Cenário-CF-T07 — Gate bloqueia abaixo do piloto (fail-closed)
```
DADO        convicção global 68% (< piloto 70%)
QUANDO      o gate CF-012 roda
ENTÃO       encaminhamento bloqueado; Decision não habilitada
VERIFICAÇÃO gate_passed == false; decision_enabled == false
```

### Cenário-CF-T08 — Convicção macro e global pelo mesmo contrato
```
DADO        solicitação macro (estrutural+institucional) e global (vetor completo)
QUANDO      o motor computa cada uma
ENTÃO       ambas pelo mesmo contrato; invocação não fixada pela Spec
VERIFICAÇÃO macro_subset_supported == true; full_vector_supported == true; invocation_count_fixed == false
```

---

## D8 — Cenários Adversariais [casos de negação — CRITICAL]

Princípio transversal: **fail-closed** — em qualquer ambiguidade sobre autorização, contaminação, hierarquia, limiar ou irreversibilidade, o motor NÃO funde / NÃO agrega compensatoriamente / NÃO habilita Decision / NÃO fixa decisão aberta, e retorna código específico ou INDETERMINADO.

### ADV-CF-01 — Produtor não autorizado produz DERIVED (viola CEM-001) (consolida CF-001/T01)
**DADO:** um AGENT (ou Skill) tenta produzir evidência DERIVED, ou o Fusion Engine funde evidência não-ACTIVE
**QUANDO:** o gate de produtor/estado roda
**ENTÃO:** rejeitar `DERIVED_PRODUCER_OR_STATE_INVALID`; nada produzido
**PORQUE:** só o Fusion Engine (ENGINE) produz DERIVED e só de ACTIVE (CEM-001 Cap.2/4/6; RULE-CF-001)
**VERIFICAÇÃO:** error_code == "DERIVED_PRODUCER_OR_STATE_INVALID"

### ADV-CF-02 — Double-counting de dependentes / independência fabricada (viola RULE-004/MET-01) (consolida CF-002/T02)
**DADO:** evidências dependentes sem discriminante de independência
**QUANDO:** a fusão roda
**ENTÃO:** contar como 1; atributo "undetermined"; NÃO afirmar independência; desconto numérico não fabricado (J-001)
**PORQUE:** evidências causalmente relacionadas = uma (RULE-004); não fabricar independência (RULE-MET-01; RULE-CAU-01)
**VERIFICAÇÃO:** effective_count == 1; independence_claimed == false

### ADV-CF-03 — Agregação compensatória pura / votos simétricos (viola CC-01) (consolida CF-005/T03)
**DADO:** proposta de agregar as 8 dimensões por TOPSIS/soma ponderada simétrica, deixando institucional+operacional compensarem estrutural fraca
**QUANDO:** a agregação é avaliada
**ENTÃO:** rejeitar `COMPENSATORY_AGGREGATION_FORBIDDEN`; aplicar não-compensatória com precedência estrutural
**PORQUE:** hierarquia inviolável; inferior não sobrepõe superior (INV-01/RULE-008); SRC-05/SRC-06 [EXTERNO] só referência, não baseline
**VERIFICAÇÃO:** compensated_by_lower_dims == false; structural_precedence_preserved == true

### ADV-CF-04 — Conflito direcional resolvido a favor de SMC (viola RULE-SY-002) (consolida CF-006/T04)
**DADO:** conflito direcional Elliott×SMC
**QUANDO:** a agregação/gate processa a direção
**ENTÃO:** saída NEUTRO; rejeitar qualquer resolução a favor de SMC (`DIRECTIONAL_CONFLICT_MUST_BE_NEUTRAL`)
**PORQUE:** Elliott veta; conflito Elliott×SMC → NEUTRO (RULE-005/SY-001/SY-002)
**VERIFICAÇÃO:** output == "NEUTRO"; resolved_in_favor_of_smc == false

### ADV-CF-05 — Convicção fabricada sob ausência/incerteza (viola RULE-EPI/MET) (consolida CF-007/T05)
**DADO:** dimensão sem evidência suficiente
**QUANDO:** o Conviction Engine avalia
**ENTÃO:** INDETERMINADO + incerteza localizada; rejeitar número fabricado e conversão de ausência em conclusão (`FABRICATED_CONVICTION_FORBIDDEN`)
**PORQUE:** ausência ≠ evidência de ausência; não quantificar sem base (RULE-EPI-01; RULE-UNC-03; RULE-PRB-02; RULE-MET-01)
**VERIFICAÇÃO:** fabricated_value == false; absence_as_conclusion == false

### ADV-CF-06 — Contaminação da Separação Tríplice / INV-04 (consolida CF-011/T06)
**DADO:** tentativa de derivar convicção de Evidence Strength, Hypothesis Confidence ou custo/sizing
**QUANDO:** o guard CF-011 roda
**ENTÃO:** rejeitar `CONVICTION_CONTAMINATION_FORBIDDEN`; níveis preservados; custo fora da convicção
**PORQUE:** Separação Tríplice (CHM-001 §1.9/§2.14) e INV-04 invioláveis
**VERIFICAÇÃO:** response.error_code == "CONVICTION_CONTAMINATION_FORBIDDEN"

### ADV-CF-07 — Gate habilita Decision abaixo do piloto (viola CEE-001 §11) (consolida CF-012/T07)
**DADO:** convicção global < 70% ou score < 7/9 ou conflito direcional
**QUANDO:** o gate CF-012 roda
**ENTÃO:** bloquear (fail-closed); rejeitar habilitação (`CONVICTION_GATE_BLOCKED`); limiar interino não relaxado
**PORQUE:** Salvaguardas de Sinal invioláveis (CEE-001 §11; RULE-003/SY-003/CEE-004); PC-04 guard mínimo
**VERIFICAÇÃO:** gate_passed == false; decision_enabled == false

### ADV-CF-08 — LLM age como gate de aprovação da convicção (viola ENF-03)
**DADO:** proposta de o componente semântico/LLM "aprovar" a convicção ou resolver o conflito direcional
**QUANDO:** o gate é processado
**ENTÃO:** rejeitar `LLM_IS_NOT_GATE`; o veredito do gate é determinístico; LLM apenas detector
**PORQUE:** o LLM nunca é seu próprio gate (ENF-03; RULE-CF-009)
**VERIFICAÇÃO:** gate_decided_by == "deterministic"; llm_as_gate == false

### ADV-CF-09 — Fixar valores definitivos de J-001/N-001 (viola CONS-01)
**DADO:** tentativa de fixar, nesta Spec, fórmula/pesos/limiares definitivos ou pesos por ativo definitivos
**QUANDO:** o CCM-001 é redigido
**ENTÃO:** rejeitar `OPEN_DECISION_CANNOT_BE_CLOSED`; só estrutura/método/mecanismo + limiares-piloto interinos
**PORQUE:** J-001/N-001 abertos — não fechar (CONS-01; Q-A4); definitivos pós-backtest
**VERIFICAÇÃO:** j001_definitive_values_fixed == false; n001_definitive_values_fixed == false

### ADV-CF-10 — Cascata automática de invalidação (viola não-cascata) (consolida CF-003)
**DADO:** evidência ancestral invalidada
**QUANDO:** o Fusion Engine processa o evento
**ENTÃO:** rejeitar cascata automática (`AUTO_CASCADE_FORBIDDEN`); iniciar avaliação de impacto; preservar histórico
**PORQUE:** invalidação não implica cascata automática (CEM-001 Cap.4/5; INV-07; RULE-CF-001)
**VERIFICAÇÃO:** auto_cascade_applied == false; impact_evaluation_started == true

### ADV-CF-11 — Colapsar o vetor 8D em pontuação única (viola PCO-06)
**DADO:** proposta de reduzir o Conviction Vector a um único número descartando as 8 dimensões
**QUANDO:** a agregação/publicação roda
**ENTÃO:** rejeitar `DIMENSIONALITY_REDUCTION_FORBIDDEN`; preservar as 8 dimensões e a reconstrução
**PORQUE:** não-redução quando múltiplas dimensões são relevantes (PCO-06; INV-03 dimensionalidade=8)
**VERIFICAÇÃO:** dimensions_preserved == 8; collapsed_to_scalar == false

### ADV-CF-12 — Implementar/ser dona da invocação do motor, fixar dimensão do regime ou estados do Blackboard (invade Manager / Q-A9 / M-001)
**DADO:** tentativa de a SPEC-003 **implementar/possuir** a invocação do motor (que é do Manager), de fixar **a dimensão das 8 em que o regime entra (WF-C04/Q-A9)**, ou os estados do Blackboard para a convicção
**QUANDO:** o mecanismo macro/global (CF-010), o mapeamento do regime (RULE-CF-003/Q-A9) ou a publicação (CF-013) é definido
**ENTÃO:** rejeitar `OUT_OF_SCOPE_MANAGER_OR_M001`; a invocação **2x** está decidida por Andraus (WF-C01/Q-A5) mas é do **Manager** (SPEC-008/014), não implementada aqui; a dimensão do regime (Q-A9) e os estados do Blackboard (M-001) seguem abertos
**PORQUE:** invocação = Manager (2x já decidida — Q-A5/WF-C01/DHR-DEC-001 — mas não é desta Spec); dimensão do regime = decisão de Andraus (Q-A9, WF-C04); estados do Blackboard = M-001 (Q-A8) — não fechar o que segue aberto (CONS-01)
**VERIFICAÇÃO:** invocation_implemented_here == false; regime_dimension_fixed == false; blackboard_states_fixed == false

> **Cobertura:** 12 cenários adversariais (mínimo CRITICAL = ≥1; cobrem casos de negação de todas as BASpecs com efeito e das fronteiras abertas J-001/N-001/M-001/WORKFLOW-SOT-001). Mapeiam para EC-CF-001..006 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada ato DEVE ser reconstruível (P13/RULE-010): entrada (evidências ACTIVE + Hypothesis Confidence + **rótulo de qualidade de evidência por escola** preservado, não sobrescrito — WF-V02), fusão (DERIVED + Lineage + desconto de dependência), normalização por dimensão, pesos aplicados, regra de agregação (não-compensatória; veto estrutural), dimensões INDETERMINADO, conflitos consumidos, robustez/sensibilidade, resultado do gate (pass/block + limiares usados), publicação (vetor + reconstrução). A **reconstrução expandida de linhagem** (Cognitive Trace Reconstruction) e o **storage físico** pertencem ao **Knowledge Graph (SPEC-006 / H-001 pendente)** — aqui ficam **por referência** (coerente com alvo D0–D8; CEM-001 Cap.5). [FONTE: CONSTITUTION P13; RULE-010; CEM-001 Cap.5; H-001 pendente]

---

## CCM-001 (Canonical Conviction Model) — esqueleto do contrato redigido [PROPOSTA]

> Produto central da SPEC-003. Redigido sob GMC-001 (RULE-GMC-001..005), respeitando a Separação Tríplice (CHM-001 §1.9/§2.14) e o CEM-001. **Estrutura/método; valores definitivos = J-001/N-001 (abertos).**

| Camada | Conteúdo | Fronteira |
|---|---|---|
| Identidade | `conviction_id`, `version`, `previous_version_id`, `creation_timestamp`, `status` (COMPUTED/GATED_PASS/GATED_BLOCK/SUPERSEDED) | Imutável pós-publicação exceto `status` (padrão CEM-001 Cap.4) |
| Origem | `producer_id` = Conviction Engine; `source_evidence_ids` (ACTIVE/DERIVED consumidas); `hypothesis_ref` (Hypothesis Confidence lido, não redefinido) | Separação Tríplice (CF-011) |
| Conviction Vector 8D | `{estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica}` — cada dimensão: valor normalizado \| INDETERMINADO | Dimensionalidade=8 fechada (Questionário v1); valores/pesos = J-001/N-001 |
| Agregação | `aggregation_method` (não-compensatória, estrutural-primeiro), `global_conviction`, `score`, `directional_conflict`, `robustness`, `sensitivity` | Fórmula/pesos/limiares definitivos = J-001 |
| Gate | `gate_result` (pass/block), `thresholds_used` (piloto ≥70%/7-9 interino) | Limiares definitivos = J-001 |
| Rastreabilidade | `reconstruction` (dimensões→normalização→pesos→agregação→gate), `per_asset_weights_ref` (N-001) | P13/RULE-010; N-001 aberto |
| Governança | GMC-001 (universal/neutro/reutilizável/baixo acoplamento) | RULE-GMC-001..005 |

---

## I/O Schemas (lógicos — referência; não redefinem CEM-001/CHM-001)

### Objeto Conviction Vector (CCM-001 — produto desta Spec)
```json
{
  "conviction_id": "CV-2026-10-01-001",
  "version": 1,
  "previous_version_id": null,
  "creation_timestamp": "2026-10-01T12:00:00Z",
  "status": "COMPUTED | GATED_PASS | GATED_BLOCK | SUPERSEDED",
  "producer_id": "conviction_engine",
  "source_evidence_ids": ["EV-A", "EV-C(DERIVED)"],
  "hypothesis_ref": "HY-...",
  "conviction_vector": {
    "estrutural": "0.0-1.0 | INDETERMINADO",
    "geometrica": "0.0-1.0 | INDETERMINADO",
    "fractal": "0.0-1.0 | INDETERMINADO",
    "institucional": "0.0-1.0 | INDETERMINADO",
    "operacional": "0.0-1.0 | INDETERMINADO",
    "temporal": "0.0-1.0 | INDETERMINADO",
    "volume": "0.0-1.0 | INDETERMINADO",
    "historica": "0.0-1.0 | INDETERMINADO"
  },
  "aggregation_method": "non_compensatory_structural_first",
  "global_conviction": "0.0-1.0 (valores definitivos = J-001)",
  "score": "n/9",
  "directional_conflict": false,
  "robustness": "qualitativo/ordinal (métrica definitiva = J-001)",
  "gate_result": "PASS | BLOCK",
  "thresholds_used": { "conviction_min": "0.70 (piloto interino)", "score_min": "7/9 (piloto interino)" },
  "per_asset_weights_ref": "N-001 (aberto)",
  "reconstruction": { "...": "dimensões→normalização→pesos→agregação→gate" }
}
```
> `conviction_vector` tem exatamente 8 dimensões (Questionário v1). `global_conviction`, pesos e limiares têm **valores definitivos em J-001/N-001** (abertos). Nenhum campo deriva de custo/sizing (INV-04) nem redefine Evidence Strength/Hypothesis Confidence (Separação Tríplice).

---

## Enforcement Contracts

### EC-CF-001 — Fusão (produção de DERIVED; gate de produtor/estado)
```
CAPABILITY   : Produzir evidência DERIVED a partir de evidência ACTIVE
EFFECT       : Publicação de Evidence DERIVED no workspace de Evidência; evento Evidence Created (EC-COG-005)
PRECOND      : (producer == Fusion Engine/ENGINE) AND (todas as ancestrais ACTIVE) AND (Lineage coerente)
POSTCOND     : DERIVED publicada; Lineage íntegra; anti-double-counting aplicado; nada promovido a convicção
POLICY       : RULE-CF-001/002; CEM-001 Cap.2/4/6; INV-06; RULE-004
LEVEL        : E2 (Operacional — Engine; estado compartilhado alterado)
FAILURE-MODE : Fail-closed — rejeitar fusão; código específico; nada publicado; log
EVIDENCE     : Log de fusão (ancestrais, desconto de dependência); evento Evidence Created
```

### EC-CF-002 — Avaliação de impacto de invalidação (não-cascata)
```
CAPABILITY   : Iniciar avaliação de impacto sobre derivadas quando ancestral é invalidada
EFFECT       : Processo de avaliação de impacto; nenhuma invalidação automática em massa
PRECOND      : (evento Evidence Invalidated recebido) AND (não aplicar cascata automática)
POSTCOND     : avaliação iniciada; objeto preservado (INV-07); decisão por regras de linhagem
POLICY       : RULE-CF-003; CEM-001 Cap.4/5; INV-07
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — cascata automática rejeitada; histórico preservado
EVIDENCE     : impact_evaluation_record; ausência de auto-cascata
```

### EC-CF-003 — Agregação não-compensatória + tratamento de incerteza (Detector ≠ Gate)
```
CAPABILITY   : Agregar as 8 dimensões (não-compensatória) e tratar ausência/contraevidência/incerteza
EFFECT       : Produz o Conviction Vector 8D (insumo); nenhuma decisão/execução
PRECOND      : (normalização feita) AND (precedência estrutural preservada) AND (bounded loop com parada) AND
               (LLM só como detector — ENF-03)
POSTCOND     : vetor 8D preservado; dimensões sem base = INDETERMINADO; compensação pura rejeitada
POLICY       : RULE-CF-004/005/006; INV-01; RULE-008; GPR-001 PCO-06; RULE-EPI/UNC/MET/PRB
LEVEL        : E2 (Operacional — produz insumo; sem efeito normativo próprio)
FAILURE-MODE : Fail-closed — irredutível/ambíguo ⇒ INDETERMINADO; compensação da estrutural ⇒ rejeição
EVIDENCE     : reconstrução da agregação; log de dimensões INDETERMINADO; rejeição de compensação
```

### EC-CF-004 — Guard Separação Tríplice + INV-04
```
CAPABILITY   : Impedir contaminação entre Evidence Strength / Hypothesis Confidence / Global Conviction e
               a entrada de custo/sizing na convicção
EFFECT       : Bloqueia derivação de convicção a partir de Strength/Confidence/custo
PRECOND      : (tentativa de contaminação detectada)
POSTCOND     : níveis preservados; custo fora da convicção (INV-04)
POLICY       : RULE-CF-007/008; CHM-001 §1.9/§2.14; INV-04; INV-10
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — rejeitar; código "CONVICTION_CONTAMINATION_FORBIDDEN"
EVIDENCE     : log da tentativa barrada; ausência de campo de convicção derivado de Strength/custo
```

### EC-CF-005 — Gate Convicção→Decisão (commit crítico irreversível) [E3]
```
CAPABILITY   : Habilitar ou bloquear o encaminhamento da convicção para a Decisão (Synthesis)
EFFECT       : Habilitação de Decision (efeito crítico/irreversível a jusante) ou bloqueio
PRECOND      : (conv_global ≥ 0.70 piloto) AND (score ≥ 7/9 piloto) AND (¬directional_conflict) AND
               (gate determinístico — LLM nunca é o gate, ENF-03)
POSTCOND     : habilita só se todas as pré-condições; senão bloqueia (fail-closed); limiar interino não relaxado
POLICY       : RULE-CF-009; RULE-003/SY-003; RULE-CEE-004; RULE-005; GPR-001 PC-04; ENF-03/04; J-001
LEVEL        : E3 (Crítico — habilita Decision; irreversível a jusante)
FAILURE-MODE : Fail-closed — ambiguidade/abaixo do piloto ⇒ bloquear; nenhuma habilitação; log
EVIDENCE     : gate_record (limiares usados, resultado); evento; método de observação de falso-DENY
             + ENF-07: amostragem de convicções válidas bloqueadas por engano (limiar amostral = gap aberto)
```

### EC-CF-006 — Publicação do Conviction Vector (workspace próprio; M-001 aberta)
```
CAPABILITY   : Publicar o Conviction Vector 8D com reconstrução completa
EFFECT       : Publicação append-only no workspace de Convicção; evento de convicção publicada
PRECOND      : (workspace próprio — RULE-BB-002) AND (append-only — RULE-BB-004) AND (reconstrução anexada) AND
               (estados do Blackboard NÃO fixados — M-001 aberta)
POSTCOND     : vetor publicado; reconstrução íntegra (P13/RULE-010); nada deletado (INV-07)
POLICY       : RULE-CF-011; RULE-BB-002/004; RULE-010; CONSTITUTION P13; M-001
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — workspace alheio / sem reconstrução ⇒ rejeitar publicação
EVIDENCE     : log de publicação; reconstrução anexada; referência explícita a M-001 (aberta)
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
Pipeline cognitivo de 2 motores (B-001): **Fusion Engine** (produz evidência DERIVED — CEM-001) → **Conviction Engine** (calcula o Conviction Vector 8D sob o CCM-001). Combina gates constitutivos determinísticos (Classe C: produtor/estado, veto estrutural, Separação Tríplice/INV-04, gate Convicção→Decisão, publicação), cálculo determinístico (Classe D: normalização, aging/pesos-mecanismo, macro/global) e julgamento com gate (Classe H/P: anti-double-counting, agregação não-compensatória, ausência/incerteza, robustez). Não executa; produz convicção para consumo a jusante (Synthesis/SPEC-014). [FONTE: CEM-001; CHM-001; atomic-spec §9/§10.6; research.md §0]

### Roteamento de modelo (CEE-001 §5)
Gates constitutivos/determinísticos (C/D) não requerem LLM. Os julgamentos (H/P — anti-double-counting, agregação não-compensatória, ausência/incerteza, robustez) usam apoio semântico: Tipo III (julgamento especialista) → **Sonnet** como detector; Tipo IV–V (conflito multi-narrativa/agregação complexa) → **Opus reservado** apenas como detector, **nunca como gate** (ENF-03). Roteamento definitivo por Engineering Card (BUILD adiado). [FONTE: CEE-001 §5/RULE-CEE-002; ENF-03]

### Dependências técnicas
CEM-001 (BASELINE) · CHM-001 (BASELINE) · SPEC-001 v1.1 (BASELINE) · SPEC-002 (BASELINE, DHR-SPEC002-001) · SPEC-019/020/021 v1.0 (BASELINE) · atomic-spec v1.5 · RULES.md v1.5 (INV-*, ENF-*, RULE-002/003/004/005/008/010, RULE-SY-*, RULE-CEE-004, RULE-GMC-*, RULE-BB-*, RULE-EPI/CAU/MET/UNC/PRB/DEC/SEM) · GPR-001 (PC-04/PCO-06/PB-06) · CEE-001 v2.0 · EC-COG-005 (Event Bus — contrato → SPEC-005) · WORKFLOW.md (confronto RULE-ECC-05). Referências externas [EXTERNO], não-baseline: research.md §2 (SRC-01..07).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Agregação compensatória compensa estrutural fraca (fere CC-01) | RULE-CF-005; ADV-CF-03; EC-CF-003; rejeição de TOPSIS/votos (SRC-05/06) |
| Conflito direcional resolvido a favor de SMC (fere RULE-SY-002) | RULE-CF-006; ADV-CF-04; CF-012 |
| Strength/custo/Confidence viram convicção (fere INV-04/Separação Tríplice) | RULE-CF-007/008; ADV-CF-06; EC-CF-004 |
| Convicção fabricada sob ausência (fere RULE-EPI/MET) | RULE-CF-006; ADV-CF-05; EC-CF-003 |
| Gate habilita abaixo do piloto (fere CEE-001 §11) | RULE-CF-009; ADV-CF-07; EC-CF-005 (E3, fail-closed) |
| LLM age como gate (fere ENF-03) | ENF-03; ADV-CF-08; EC-CF-003/005 (detector≠gate) |
| Fixar J-001/N-001 definitivos (fere CONS-01) | Non-goal; ADV-CF-09; CC-03; D4 valores em aberto |
| Colapsar o vetor 8D (fere PCO-06) | RULE-CF-003; ADV-CF-11 |
| Double-counting / independência fabricada | RULE-CF-002; ADV-CF-02; RULE-MET-01/CAU-01 |
| Cascata automática de invalidação | RULE-CF-001; ADV-CF-10; EC-CF-002 |
| Implementar/ser dona da invocação do motor (é do Manager; 2x já decidida — Q-A5/WF-C01) ou fixar estados do Blackboard (M-001) | Non-goal; ADV-CF-12; CF-010/CF-013 |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz o schema lógico do Conviction Vector (CCM-001) e esqueleto do contrato; nenhum schema canônico do CEM-001/CHM-001 alterado.
- **RAG:** nenhum; a camada não escreve no KG/RAG (evidence candidate a partir de retrieval → SPEC-007).
- **Skills:** nenhuma Skill afetada; INV-06 preservado (Skill produz Observação, não Evidência/Convicção).
- **Testes:** adiciona `checks.md` (verificação de spec); a mecânica numérica de agregação fica para BUILD pós-J-001.
- **Modelos dependentes:** CEM-001/CHM-001/SPEC-001/002 não alterados (construção SOBRE); CCM-001 é novo canônico [PROPOSTA].
- **Compatibilidade:** **Minor** — adiciona o CCM-001 + camada Fusion/Conviction sobre canônicos existentes, sem invalidar comportamento vigente; nenhuma RULE existente redefinida (RULE-004 estendida em cobertura, não em texto).

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07) e a Classe por BASpec (CC-11). A calibração numérica (J-001/N-001) é condição de BUILD (backtest), não de homologação da Spec.

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — pergunta adversarial por BASpec com efeito (cobertura TOTAL — CRITICAL, 13 BASpecs):**

- **CF-001 (fusão DERIVED, C):** se errada → produtor não autorizado/evidência não-ACTIVE vira DERIVED → observável por `origin_type`/`producer` inválido publicado; verificável por consumidor independente. Negação: ADV-CF-01. QUANDO-sim-mas-ENTÃO-não: evidência ACTIVE que vira SUPERSEDED durante a fusão → rejeitar.
- **CF-002 (anti-double-counting, P):** se errada → dependentes contadas em dobro / independência fabricada → observável por `effective_count`>1 ou `independence_claimed=true` sem discriminante; verificável. Negação: ADV-CF-02. QUANDO-sim-mas-ENTÃO-não: co-ocorrência ≠ dependência causal (RULE-CAU-01) → "undetermined", não "dependent".
- **CF-003 (impacto invalidação, C):** se errada → cascata automática → observável por derivadas invalidadas em massa; verificável. Negação: ADV-CF-10.
- **CF-004 (normalização, D):** se errada → dimensões agregadas em escalas distintas → observável por reconstrução inconsistente; verificável. Negação: cobertura em EC-CF-003 (reconstrução); sem falsa precisão (J-001).
- **CF-005 (agregação não-compensatória, H):** se errada → inferior compensa estrutural → observável por `compensated_by_lower_dims=true`; verificável. Negação: ADV-CF-03. QUANDO-sim-mas-ENTÃO-não: dimensões altas não elevam convicção acima do que a estrutural permite.
- **CF-006 (veto estrutural/conflito, C):** se errada → conflito resolvido a favor de SMC → observável por `output≠NEUTRO` sob conflito; verificável. Negação: ADV-CF-04.
- **CF-007 (ausência/incerteza, P):** se errada → convicção fabricada → observável por valor numérico em dimensão sem evidência; verificável. Negação: ADV-CF-05. QUANDO-sim-mas-ENTÃO-não: ausência não vira conclusão.
- **CF-008 (robustez, P):** se errada → robustez afirmada sem análise ou métrica numérica definitiva fabricada → observável por `definitive_metric_fixed=true` ou ausência de explicação; verificável. Negação: guard J-001; EC-CF-003.
- **CF-009 (aging/pesos, D):** se errada → valores definitivos de pesos por ativo fixados → observável por `definitive_weights_fixed=true`; verificável. Negação: ADV-CF-09 (N-001 aberto).
- **CF-010 (macro/global, D):** se errada → a Spec implementa/possui a invocação do motor (que é do Manager) → observável por `invocation_implemented_here=true`; verificável. A invocação 2x está decidida por Andraus (Q-A5/WF-C01) mas pertence ao Manager (SPEC-008/014). Negação: ADV-CF-12.
- **CF-011 (Separação Tríplice/INV-04, C):** se errada → strength/custo vira convicção → observável por campo de convicção derivado de Strength/custo; verificável. Negação: ADV-CF-06.
- **CF-012 (gate Convicção→Decisão, C/E3):** se errada → Decision habilitada abaixo do piloto ou LLM como gate → observável por `decision_enabled=true` sob <70%/7-9 ou `llm_as_gate=true`; verificável. Negação: ADV-CF-07, ADV-CF-08.
- **CF-013 (publicação, C):** se errada → publicação em workspace alheio / sem reconstrução / estados do Blackboard fixados → observável por workspace inválido ou `blackboard_states_fixed=true`; verificável. Negação: ADV-CF-12.

Todas as 13 BASpecs com efeito têm ENTÃO verificável por observador independente e caso de negação em D8. Nenhuma restou como [DECISÃO NECESSÁRIA] por falta de verificabilidade (as decisões abertas J-001/N-001/M-001/WORKFLOW-SOT-001 são fronteiras explícitas, não falhas de verificabilidade das BASpecs).

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista CEM-001 (Cap.2/3/4/5/6), CHM-001 (§1.9/§2.14), SPEC-001 v1.1, SPEC-002, SPEC-019/020/021 v1.0, atomic-spec v1.5, ENF-01..08, INV-01/03/04/05/06/07/09/10, RULE-002/003/004/005/008/010, RULE-SY-*, RULE-CEE-004, RULE-GMC-*, GPR-001 PC-04/PCO-06/PB-06 (ID+versão — RULE-HD-04). Evidência de satisfação por obrigação herdada:
- CEM-001 Cap.2/6 (Fusion = único ENGINE PRODUCER) → CF-001/EC-CF-001.
- CEM-001 Cap.4/5 (invalidação/não-cascata; Lineage) → CF-003/EC-CF-002; CF-001 (Lineage).
- CHM-001 §1.9/§2.14 (Separação Tríplice) → CF-007/CF-011/EC-CF-004.
- INV-01/RULE-008/RULE-SY-001 (hierarquia/veto) → CF-005/CF-006/EC-CF-003.
- INV-03/PCO-06 (dimensionalidade=8; não-redução) → CF-003(rule)/ADV-CF-11.
- INV-04 (custo fora da convicção) → CF-008(rule)/CF-011/EC-CF-004.
- RULE-004/MET-01/CAU-01 (dependentes=uma; não fabricar) → CF-002.
- RULE-003/SY-003/CEE-004 (limiares piloto; salvaguardas) → CF-009(rule)/CF-012/EC-CF-005.
- ENF-03 (detector≠gate) → CF-009/CF-012/ADV-CF-08.
- RULE-010/P13 (rastreabilidade) → CF-011/CF-013/D9.
- SPEC-002 (conflito/(in)dependência representados) → consumidos por CF-002/CF-006.
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (o único MODIFIED estende RULE-004 em cobertura, sem alterar texto — RULE-HD-02). **Eixo VERTICAL (RULE-HV) declarado não aplicável** (herança sobre canônicos vizinhos, não decomposição pai→filha de macro-spec).

**Bloco C — epistêmico (RULE-EPI/CAU/PRB):** nenhuma afirmação causal forte sem mecanismo (dependência entre evidências por RULE-CAU-01: co-ocorrência ≠ causa → "undetermined"); nenhuma hipótese tratada como fato (SRC-01..07 = [EXTERNO]/DADO; nenhum método externo importado como baseline); INDETERMINADO usado em ausência/contraevidência/robustez insuficiente/(in)dependência não verificável; **nenhuma probabilidade/precisão numérica definitiva** declarada (limiares são interinos piloto Questionário v1; definitivos = J-001; RULE-PRB-01 nota contrato próprio do Conviction Vector; RULE-UNC-03 remete quantificação a este nó, mas sob J-001 aberto — mecanismo, não valores).

**Bloco D — reforço de escopo:** a Spec **produz convicção/insumo decisional** (fusão/agregação/gate), **não executa** ordem, **não emite sinal**, **não dimensiona risco** — INV-05/RULE-DEC-01 reconfirmados (§7). Nenhuma BASpec cruza a fronteira SOT→execução downstream nem invade Synthesis (SPEC-014)/Risk Agent. Dependências de decisão de Andraus (homologação; efetivação de RULE-CF/CCM-001) marcadas [PROPOSTA]; J-001, N-001, M-001, WORKFLOW-SOT-001 marcadas [DECISÃO NECESSÁRIA]/abertas, não fechadas.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001; CHM-001; SPEC-001 v1.1; SPEC-002; SPEC-019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5; RULES v1.5; GPR-001; CEE-001 v2.0 (INV-*, ENF-*, RULE-*, PC-04/PCO-06/PB-06) | [FONTE] | FATO NORMATIVO |
| Limiares-piloto ≥70% / 7-9 | [FONTE] | FATO NORMATIVO **interino** (Questionário v1, recalibrável pós-backtest) |
| CCM-001; RULE-CF-001..012; BASpec-CF-001..013; EC-CF-001..006 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Fontes SRC-01..07 (Bayes/DS, agregação, Kelly, convicção×confiança, confluência, TOPSIS, sensibilidade) | [EXTERNO] | Referência de método — DADO, nunca baseline (research.md §2) |
| Acepção "Conviction Engine" = componente separado (a) | [DECISÃO NECESSÁRIA] (reconciliação) | Acepção declarada (RULE-SEM-01); reconciliação (a)↔(b) = WORKFLOW-SOT-001 |
| Fórmula/pesos/limiares **definitivos** do Conviction Vector | [DECISÃO NECESSÁRIA] | **J-001 — EM ABERTO/pendente — não fechar** |
| Pesos por ativo **definitivos** (BTC/XAU/NASDAQ) | [DECISÃO NECESSÁRIA] | **N-001 — EM ABERTO/pendente — não fechar** |
| Estados do Blackboard para o Conviction Vector | [DECISÃO NECESSÁRIA] | **M-001 — EM ABERTO/pendente (SPEC-004)** |
| Número de invocações (macro 1x / global 2x) + dimensão do regime (WF-C04/Q-A9) | [DECISÃO NECESSÁRIA] | **WORKFLOW-SOT-001/WF-D03 — EM ABERTO/pendente (invocação = Manager/Scheduler; dimensão do regime = Andraus/Q-A9)** |
| Killzone (WF-D01), alarme-gatilho (WF-D02), papel do ICT (WF-D04) | [FONTE] | **FECHADOS por Andraus (WORKFLOW.md versão vigente); fora do escopo da SPEC-003 (Manager/Scheduler SPEC-008/015 + agentes)** |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-003 confirmada como próximo autorizado (§4/§30/§143); FASE 1, após SPEC-001/002 e FASE GOV.
[x] atomic-spec.md lido: método v1.5 confirmado (CC-11/CC-12; RULE-MECH-01; RULE-ECC-04/05; RULE-MM; §15 Dossiê).
[x] Nenhum invariante congelado violado (INV-01..10 + INV-RISK). INV-01/03/04/05/06/07/10 reforçados.
[x] Constitution Check CC-01..CC-12 preenchido (N/A justificados CC-06/07/12; CC-10/CC-11 INCIDEM e aplicados).
[x] Disciplinas N8–N17: RULE-EPI (INDETERMINADO/ausência), RULE-CAU-01 (dependência), RULE-MET-01 (não-fabricação), RULE-UNC/PRB (qualitativo; sem falsa precisão), RULE-DEC-01 (produz≠executa), RULE-SEM-01 (acepção declarada).
[x] Referências externas SRC-01..07 [EXTERNO] classificadas (research.md §2); rótulos externos (DS/Bayes/TOPSIS/Kelly) NÃO adotados como baseline; verbatim capturado (RULE-ECC-04, sources/).
[x] RULE-ECC-05 (3 lentes) refletida no Plan: Arquitetura (§3.1), Escola/risco-retorno (§3.2 — Kelly ADIADO ao Risk Agent), confronto WORKFLOW.md (§3.3 — macro/global, motor 1x/2x aberto) — decisões adotar/adaptar/rejeitar/adiar incorporadas em BASpecs/Non-goals.
[x] Spec sem implementação (BUILD adiado); Plan derivado; Tasks adiadas (spec-first).
[x] Critérios em EARS (10); BASpecs completas (CF-001..013) com Classe declarada (CC-11); RULEs citadas existentes vs propostas (RULE-CF/CCM-001 [PROPOSTA]) etiquetadas.
[x] Profundidade D0–D8 atingida (D5 ciclo convicção + CEM-001 Cap.4; D6 protocolo pipeline B-001; D7 x8; D8 adversarial x12; D9 por referência).
[x] Enforcement Contract em todo ato com efeito (EC-CF-001..006); piso E2; E3 no gate Convicção→Decisão irreversível; fail-closed; ENF-07 amostral declarado no E3.
[x] Status epistemológico aplicado (FATO NORMATIVO / interino / PROPOSTA / EXTERNO / DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: J-001, N-001, M-001, WORKFLOW-SOT-001 permanecem abertas (só mecanismo/estrutura + limiares-piloto); B-001/dimensionalidade=8 FECHADAS (não reabertas); nenhuma decisão aberta usada como invariante fechado.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos registrados (research.md §4 CONFLITO-1/2/3/4; GAP-J/N/M/WORKFLOW) — não resolvidos em silêncio.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE/EC fabricada como vigente; sem baseline informal.
[x] 4Es na ordem; Conformidade > Eficácia (INV-01/04 e ENF-03 prevalecem). Latência N/A (camada spec-time; consumidor a jusante é SPEC-014).
[x] Dependências a montante homologadas (CEM-001/CHM-001/SPEC-001/002/019/020/021/atomic-spec v1.5/RULES v1.5/GPR-001/CEE-001); não downstream de bloqueador aberto (J-001/N-001 são de calibração/BUILD, não bloqueiam a estrutura/método qualitativa).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); Bloco A cobre TODAS as 13 BASpecs com efeito — obrigatório CRITICAL.
[x] CC-11/§10.6: Classe por BASpec com efeito, com critério 4Es; H/P com bounded loop; H/C com gate de saída.
[x] Abertura (RULE-ECC-01/02/04/05): Dossiê presente e HOMOLOGADO (research.md §6-bis); verbatim em sources/SRC-01..07.txt; escopo/quantidade/número homologados (Opção A).
[x] Passo 11-bis: BL-004 ATIVADO/absorvido/tratado; BL-012 ATIVADO independente (Andraus); BL-002 IMINENTE (homologação); demais não disparam.
[ ] Gate determinístico (validate_spec_sot.py) e build_map.py --check: reportado ao caller (execução no ambiente pai).
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] / abertas nesta Spec (não fechadas — CONS-01):
- **J-001** — fórmula/pesos/limiares **definitivos** do Conviction Vector (inclui calibração do desconto de dependência, peso/decay de aging, métrica de robustez); a Spec fixa estrutura/método + limiares-piloto interinos, **não** os definitivos.
- **N-001** — pesos por ativo **definitivos** (BTC/XAU/NASDAQ); a Spec especifica o **mecanismo**, não os valores.
- **M-001** — estados do Blackboard para objetos não-hipótese (Conviction Vector); referenciada como aberta; fecha em SPEC-004.
- **WORKFLOW-SOT-001** — número de invocações (macro 1x / global 2x), Killzone, alarme-gatilho, onde ICT entra; reconciliação da acepção "Conviction Engine" (a)↔(b); a Spec só fornece o mecanismo; decisão do Manager/Scheduler.

Carregado do Dossiê para o Revisor:
- research.md §6-bis: 1 achado Menor não-bloqueante do parecer do Revisor sobre o research.md (A-01, linguagem sobre BL-012) — já corrigido no Dossiê e refletido na Nota de gate acima.
- B-001 e dimensionalidade=8 FECHADAS (não reabertas); CEM-001/CHM-001 não redefinidos (CC-02).
