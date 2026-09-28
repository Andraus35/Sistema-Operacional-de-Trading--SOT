# BL-016 — Encaminhamento do MC-SKL-001 (Camada de Skills) após fechamento de I-001

| Campo | Valor |
|---|---|
| Documento | BL-016-MC-SKL-001-encaminhamento |
| **Tipo** | **Análise/encaminhamento de backlog (RMR-001 §4 — tratamento de item `ATIVADO`).** NÃO é abertura de Spec, NÃO é Dossiê de Pesquisa formal (RULE-ECC-02), NÃO abre SPEC-025, NÃO fecha o critério de corte D-vs-P (CONS-01 — isso é matéria do Dossiê de abertura da SPEC-025). NÃO homologa. |
| Autor | Especificador SOT (souza.merchan@gmail.com — identificação de autoria) |
| Data | 2026-09-28 |
| Gatilho que ativou | `decisao:I-001 resolvida` (DHR-I001-001, 2026-09-28) |
| Item | BL-016 — MC-SKL-001 (`reference/camadas/CAMADAS SKILLS.MD`), ref. externa não-normativa (DHR-MC-SKL-001, K-MAN-19) |
| Decisor | **Andraus** (promoção/absorção de item e qualquer fechamento de critério — CONS-01, INV-09) |
| Fontes | `governance/DHR-I001-001_...md`; `governance/BRIEFING-DECISAO-I-001.md`; `reference/camadas/CAMADAS SKILLS.MD` (MC-SKL-001 §5/§21/§24/§27/§28); `governance/CONFLICT-MAP.md` (K-MAN-19); `governance/RULES.md` (RULE-MECH-01..04, RULE-MM-01..07); `backlog/RMR-001_Painel_Backlog.md` (BL-016); `AGENTS.md` §6 |

> **Status epistemológico (TRACE-06).** A direção de I-001 (Opção C) e o texto do MC-SKL-001 são `[FATO NORMATIVO]` / `[FONTE]` verificados. A classificação D-vs-P das 95 SKL-SPEC é `[INFERÊNCIA]` preliminar — **não decisão**. A proposta de estado do BL-016 (§6) é `[PROPOSTA]`. Nenhuma linha aqui fecha decisão aberta, abre/renumera slot (INV-07/RULE-ECC-01) ou substitui o `CATALOGO-OFICIAL.md` (INV-09). MC-SKL-001 permanece **referência externa não-normativa** (X-01) — nada aqui o torna baseline.

---

## 1. R-ARCH — resolvido pela direção C (não se decide de novo; aplica-se)

**Confirmação por escrito.** A pergunta arquitetural do R-ARCH ("Skill é agente ou é competência usada por um agente?") **já está respondida** pela direção homologada de I-001 (DHR-I001-001, Opção C — híbrido por Classe):

- **[FATO NORMATIVO]** Competências **Classe D** (determinísticas, certificáveis, reutilizáveis) formalizam-se como **Skill separada** (unidade formal com identidade/versão/escopo/contrato de I/O — MC-SKL-001 §8/§15).
- **[FATO NORMATIVO]** Competências **Classe P** (julgamento qualitativo — leitura estrutural Elliott, narrativa institucional SMC) permanecem **comportamento interno do agente**; não viram "Skill" separada certificável.
- **[FATO NORMATIVO]** A Opção C **não colapsa** Skill em agente nem o inverso — é exatamente o que o R-ARCH pedia (Skill ≠ agente especialista; MC-SKL-001 §37/"Ponto arquitetural"). O agente continua sendo o integrador cognitivo que **usa** uma ou várias Skills.
- **[FATO NORMATIVO]** **CC-01 intocada** — a hierarquia Elliott → Fibonacci → Fractal → SMC → ICT e "ICT não cria hipótese" não são objeto de I-001 nem deste encaminhamento (DHR-I001-001 §1; BRIEFING §restrição inviolável; K-MAN-19 "prevalecem CC-01/hierarquia/RULE-EW-SM-ICT").

**O que permanece explicitamente ABERTO (CONS-01):** o **critério de corte exato** entre o que é Classe D isolável como Skill e o que não é. Isso **não** se decide aqui — é matéria do Dossiê de Pesquisa na abertura formal da SPEC-025 (RULE-ECC-01/02). Este documento apenas **aplica a direção** e produz um mapa **preliminar** para instruir aquele Dossiê.

**Reaproveitamento normativo (por que C é verificável).** O eixo de corte D-vs-P **não é novo** — reusa a taxonomia já homologada **CLASSE-MECH-001 / RULE-MECH-01..04** (`atomic-spec.md` §10.6). `atomic-spec.md` já observa que "um domínio só-Classe-D não gera `PD-xx` de julgamento semântico": Classe D e julgamento qualitativo são naturezas distintas. Uma Skill Classe D é, por definição, unidade determinística com gate de saída verificável (ENF-03 / RULE-MECH-03) — candidata natural a Skill formal certificável; uma Classe P é difícil de "certificar" isoladamente e cabe dentro do agente.

---

## 2. Mapa preliminar SKL-SPEC-001..095 contra a direção C `[INFERÊNCIA]`

> **Ressalva de honestidade (RULE-MET-01).** As 95 SKL-SPEC de MC-SKL-001 §24 são **modelos-de-especificação da própria plataforma de Skills** (o maquinário: "Skill Capability Contract", "Skill Identity Model", "Skill Harness"…), **não** as competências de domínio (Fibonacci, Elliott, FVG…). Portanto há **dois níveis** de classificação, e é desonesto fundir os dois:
> - **Nível-plataforma (as 95 SKL-SPEC):** classifico se o *modelo* descreve estrutura/contrato **verificável determinístico** (→ maquinário que a plataforma formaliza) ou governa **julgamento qualitativo** (→ descreve comportamento cognitivo do agente, não maquinário certificável isolado).
> - **Nível-domínio (as competências reais Elliott/Fib/SMC/ICT):** é *aqui* que a direção C decide "vira Skill formal (D) vs. fica no agente (P)". Este nível **não está enumerado** em MC-SKL-001 e é o núcleo do Dossiê da SPEC-025.
>
> O mapa abaixo é do **nível-plataforma** (o que o item BL-016 pede — "mapear SKL-SPEC-001..095"), com uma síntese do nível-domínio ao final. Tudo `[INFERÊNCIA]` preliminar; a decisão final é do Dossiê da SPEC-025.

| Grupo (MC-SKL-001 §24) | SKL-SPEC | Predominância `[INFERÊNCIA]` | Racional |
|---|---|---|---|
| FUNDAMENTOS | 001–010 | **D** (~10/10) | Contratos/esquemas estruturais (identidade, escopo, estado, versão, proveniência) — verificáveis por sensor determinístico (§25). Maquinário-núcleo da plataforma. |
| COMPETÊNCIA | 011–020 | **Misto, lean P** (~4D/6P) | Model/Boundary/Applicability/Depth = estruturais (D); Method/Heuristic/Procedure/Domain-Pattern/Specialization carregam interpretação (P). |
| CONTEXTO | 021–028 | **Misto, lean P** (~3D/5P) | Contract/Completeness/Temporal-Validity estruturais (D); Sufficiency/Relevance/Regime/Degradation/Recovery = julgamento (P). |
| RAG | 029–036 | **Misto, lean D** (~5D/3P) | Contract/Requirement/Retrieval/Packet-Consumption estruturais (D); Sufficiency/Conflict-Handling/Gap-Escalation = julgamento (P). |
| COGNIÇÃO | 037–046 | **P** (~2D/8P) | Hipótese/alternativa/interpretação/inferência/contraevidência/incerteza/calibração/limitation-reasoning = julgamento qualitativo. Só o Contract (037) é estrutural. Núcleo do comportamento-de-agente. |
| MULTI-SKILL | 047–055 | **Misto, lean P** (~4D/5P) | Selection/Coordination/Composition/Redundancy têm roteamento determinístico (D); Conflict/Comparison/Synthesis = julgamento (P). |
| EXPERIÊNCIA | 056–060 | **P** (~1D/4P) | Contract estrutural (D); historical/regime/similar/contrasting performance = interpretação contextual (P). |
| LEARNING | 061–068 | **Misto** (~4D/4P) | Contract/Performance-Measurement/Drift/Regression = estatístico-determinístico (D); Improvement-Hypothesis/Experimentation/Calibration/Learning-Candidate = julgamento (P). Calibração → R-05 (CCM-001/J-001). |
| GOVERNANÇA | 069–076 | **D** (~7D/1P) | Change/Impact classification, approval, promotion, rollback, deprecation, exception = fluxo procedural/estrutural verificável (D). Exception carrega julgamento (P). |
| OUTPUT | 077–083 | **D** (~6D/1P) | Esquemas de reporting (evidence/confidence/uncertainty/limitation/conflict/provenance) — estrutura verificável (D). |
| HARNESS | 084–095 | **D** (~9D/3P) | Deterministic-Sensors/Behavioral/Boundary/Regression/Benchmark/Economicity/Observability/Version-Validation/Failure-Detection = verificáveis (D); Inferential-Sensors/Adversarial = julgamento (P). |

**Agregado nível-plataforma `[INFERÊNCIA]`:** ~**55/95 ≈ 58% predominância D** (maquinário estrutural/contratos/harness que a plataforma enxuta formaliza) e ~**40/95 ≈ 42% predominância P** (modelos que descrevem julgamento cognitivo — melhor endereçados como comportamento-de-agente/lentes de cognição do que como certificação isolada). Grupos COGNIÇÃO e EXPERIÊNCIA são os polos-P; FUNDAMENTOS, GOVERNANÇA, OUTPUT e HARNESS são os polos-D.

**Leitura para a direção C.** Sob a Opção C, a **plataforma SPEC-025 enxuta** deve concentrar-se no bloco-D (contratos, identidade, estado, versão, output-schema, harness determinístico, governança) — o "esqueleto certificável" comum a qualquer Skill formal. O bloco-P (cognição/experiência/inferência) descreve o que o **agente** faz com a Skill e reconcilia-se com a camada cognitiva já normativa (N8–N17 / MC-COG BL-012), **não** exige uma plataforma de certificação isolada por competência. Isso reduz o risco de sobre-especificação que o BRIEFING-DECISAO-I-001 §2 (Opção A) apontava.

**Nível-domínio (síntese, `[INFERÊNCIA]`).** As competências reais candidatas a **Skill formal (D)**: cálculo de retração/extensão Fibonacci, detecção regrada de FVG/Order Block/liquidez, cálculo de R:R, verificação de killzone/tempo ICT — determinísticas, reutilizáveis entre agentes. As que **ficam no agente (P)**: contagem/leitura estrutural Elliott, narrativa institucional SMC, juízo de convicção. Isto é **preliminar** e é precisamente o que o Dossiê da SPEC-025 fechará.

---

## 3. Aplicação dos tratamentos de colisão (K-MAN-19), à luz da direção C

Todos os tratamentos abaixo já estavam **diferidos à ativação** (K-MAN-19). Aplicam-se agora como **orientação de encaminhamento** — nenhum vira norma sem SPEC-025 homologada.

- **R-01 — G-gates (G0–G13, §28) ↔ escada de maturidade L0–L4.** Os 14 Quality Gates da camada Skills são **gates LOCAIS**, não um sistema de gate global paralelo; mapeiam-se sobre a escada canônica **RULE-MM-01..07** (L0–L4 por-Spec). **Sob C:** o pacote G0–G13 completo só se aplica a **Skills formais Classe D** (que têm harness/certificação próprios); competências **Classe P internas ao agente** são governadas pelo harness do agente (lentes SPEC-020 / RULE-MM), **não** por um harness de Skill separado. Isso evita duplicar maquinário de certificação onde não há unidade certificável isolada.

- **R-02b — Skill Depth LEVEL 0–5 (§21) locais.** Os níveis de profundidade de invocação (LEVEL 0 NÃO-NECESSÁRIA … LEVEL 5 INVESTIGAÇÃO) são **rótulos LOCAIS** da camada Skills; **não** se confundem nem substituem os profiles de complexidade do SOT (LOW/MEDIUM/HIGH/CRITICAL ↔ D0–D8, AGENTS.md §4) nem a escada L0–L4. **Sob C:** LEVEL 0–5 descreve profundidade de **acionamento em runtime** de uma Skill formal Classe D; é dimensão de proporcionalidade/Economicidade (SKL-P22/§33), não de maturidade de spec. Mantido local; reconciliação numérica final no Dossiê da SPEC-025.

- **R-03 — I-SKL-01..20 (§27) e SKL-P01..24 (§5) locais.** Invariantes e princípios da camada são **LOCAIS** e **ancoram** nos canônicos, sem criar globais novos: I-SKL-04 (hipótese≠fato) ancora RULE-EPI-01/CC-09; I-SKL-05/19 (contraevidência/UNKNOWN) ancoram RULE-MET-01/INDETERMINADO; I-SKL-07 (experiência≠regra) ancora INV-07/RULE-CAU-01; I-SKL-12 (não substitui cognição) ancora MC-COG/R-ARCH; I-SKL-13/15 (Governança/Learning sem autoautoridade) ancoram INV-09/I-GOV-13/I-LRN-12. **Sob C:** essas obrigações valem para Skills formais D; para competências P internas, já são cobertas pelas RULE cognitivas vigentes (N8–N17) do próprio agente — sem dupla contagem.

- **R-05 — calibração de confiança → CCM-001/J-001.** SKL-SPEC-044 (Confidence Calibration) e SKL-SPEC-065 (Skill Calibration) **NÃO** fecham nem calibram o Conviction Vector 8D — J-001 permanece **aberto**; qualquer confidence de Skill é métrica local, roteada ao futuro CCM-001/Conviction Engine (INV-03/J-001). **Sob C:** reforça-se que uma Skill (D **ou** P) nunca cria autoridade de score próprio (SKL-P05 competência≠autoridade; INV-04 custo fora do Vector). Fronteira J-001/CC-02 preservada.

- **X-01 — status.** MC-SKL-001 declara "MASTER SPECIFICATION"/"MASTER CONTRACT BASELINE" (§0/§41) — **sem efeito normativo** (INV-09). Continua **referência externa não-normativa**; este encaminhamento não o promove.

- **X-02 — rótulos/estados.** Os estados da Skill §23 (DEFINED→VALIDATED→…→ARCHIVED) e §35 (ciclo de vida) são **ciclo do artefato-Skill**, objeto distinto — **não** conflitam com CHM-001 (hipótese) e mapeiam-se sobre versionamento/DHR/RMR-001 (INV-07). Namespaces G/LEVEL/I-SKL/SKL-P **não** adotados como rótulos globais do SOT. Reconciliação de nomes fica para a redação da SPEC-025.

**Fronteiras confirmadas conformes (mantidas de K-MAN-19):** CC-02 (Skill não redefine CEM/CHM/CCM/CDM/CNM), INV-05 (Skill não decide/executa — produz insumo para a cognição; SOT não executa ordem), CC-01 (hierarquia intocada).

---

## 4. Consequência para a fila de Specs `[INFERÊNCIA]`

- **SPEC-025** (plataforma de Skills / "Resolve I-001") passa a ter **direção estável**: plataforma **enxuta** centrada no bloco-D (esqueleto certificável) + critério de corte D-vs-domínio a fechar no Dossiê. Não é aberta por este ato.
- **SPEC-026..037** (as 12 Skills analíticas, Bloco R da auditoria) **continuam dependendo dos agentes SPEC-010..014** e **não** são adiantáveis (BRIEFING §4). A direção C não as destrava sozinha.
- **Sliver Bloco S de SPEC-025** (template/plataforma) sobe a **candidato a Dossiê antecipado** (modelo SPEC-046), per DHR-I001-001 §2.5 — **decisão de abrir permanece de Andraus, em ato separado**. Este encaminhamento não a solicita.
- **SPEC-002 permanece o próximo trabalho autorizado** pela ordem regular (inalterada).

---

## 5. Proposta de estado do BL-016 `[PROPOSTA]` (Andraus decide)

**Recomendo: BL-016 → `Em espera` (re-diferido), NÃO `Absorvido`.** Justificativa:

1. **A "Ação ao ativar" foi cumprida** por este documento: R-ARCH aplicado (§1), SKL-SPEC-001..095 mapeadas contra C (§2), R-01/R-02b/R-03/R-05/X-01/X-02 aplicados (§3), classificação ref. externa + K-MAN-19 já registrados. O encaminhamento que o `ATIVADO` exigia está **feito** — não há pendência de análise que justifique manter `ATIVADO` (cuja semântica é "requer ação no próximo gate"; a ação foi tomada).
2. **Mas `Absorvido` seria prematuro.** `Absorvido` = "implementado/incorporado; aponta para o artefato que o absorveu". O artefato que absorve BL-016 é a **SPEC-025** (o item é, por definição, "fonte de requisitos de SPEC-025"), que **não existe ainda**. O corte D-vs-P e a extensão da plataforma permanecem **abertos (CONS-01)**. Declarar Absorvido agora afirmaria uma incorporação que não ocorreu.
3. **Precedente coerente.** É o mesmo tratamento dos irmãos de família (BL-010..015): admitidos, analisados, permanecem `Em espera` até a Spec-alvo entrar em redação. O gatilho remanescente natural é **`spec:SPEC-025 em redação`** (a 1ª condição do gatilho composto original; a 2ª — `decisao:I-001 resolvida` — já disparou e foi tratada). Sugiro **re-apontar o gatilho** para `spec:SPEC-025 em redação` (registro aditivo, INV-07 — gatilho original preservado), conssignando este documento como o tratamento da condição já disparada.

**Alternativa (se Andraus optar por adiantar o sliver S):** manter `ATIVADO` com encaminhamento adicional "abrir Dossiê antecipado do núcleo-S da SPEC-025 como linha paralela (modelo SPEC-046)". Essa é decisão separada de Andraus (DHR-I001-001 §2.5) — não a recomendo por padrão, mas registro-a como caminho legítimo.

**Não recomendo `Descartado`** (o item tem valor futuro claro como fonte de requisitos da SPEC-025).

---

## 6. Notas de conformidade

- Documento de **encaminhamento de backlog** (RMR-001 §4/§5) — **não** fecha decisão, **não** abre Spec, **não** homologa, **não** renumera slot, **não** substitui o `CATALOGO-OFICIAL.md` (CONS-01, INV-07, INV-09, RULE-ECC-01).
- **CC-01** tratada como restrição inviolável, nunca objeto (DHR-I001-001 §1).
- **MC-SKL-001 = referência externa não-normativa** (X-01, K-MAN-19) — citado como fonte de requisitos/achado, nunca baseline.
- Classificação D-vs-P das 95 SKL-SPEC é `[INFERÊNCIA]` preliminar; fechamento é do **Dossiê de Pesquisa da SPEC-025** (RULE-ECC-01/02), com captura verbatim RULE-ECC-04, quando/se Andraus autorizar a abertura.
- Nenhuma decisão aberta tocada (J-001, K-001, I-001-corte, etc.). Nenhuma fonte `[EXTERNO]`/web usada — todas as âncoras são internas.

---

*Encaminhamento BL-016 — Especificador SOT, 2026-09-28. NÃO-normativo (INV-09). Insumo para o gate/decisão de Andraus sobre o estado do item e sobre a eventual abertura do sliver S da SPEC-025.*
