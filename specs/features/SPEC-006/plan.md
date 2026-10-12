# SPEC-006 — Cognitive Knowledge Graph

| Campo | Valor |
|---|---|
| ID | SPEC-006 — Cognitive Knowledge Graph (contrato cognitivo da **memória semântica permanente** do SOT — ontologia enxuta + entidades/relações tipadas + temporalidade + proveniência por referência + lifecycle + confiança de relação + consulta cognitiva + governança de escrita; **mecanismo físico de armazenamento INDETERMINADO — H-001 ABERTA**) |
| Versão | 1.5 (candidato a BASELINE) |
| Status | **CANDIDATO — aguarda verificação de spec (checks.md), gate determinístico, parecer do Revisor e homologação de Andraus.** NÃO é baseline (INV-09). Abertura HOMOLOGADA: DHR-SPEC006-001 (2026-10-11). As RULE-CKG-* e o contrato de nó/relação são **[PROPOSTA]** até homologação. **H-001 (mecanismo físico do KG) permanece ABERTA — este Plan NÃO a fecha** (CONS-01; só Andraus). M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 seguem ABERTAS. |
| Fonte | ROADMAP §6 (FASE 3); `specs/features/SPEC-006/ABERTURA.md` + `research.md` + `sources/` (Dossiê — RULE-ECC-01/02/04/06; validade CRITICAL 90 dias, limite 2027-01-03); DHR-SPEC006-001; atomic-spec **v1.5** (§3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7); `governance/RULES.md` (RULE-BB-004, RULE-CAU-01/02/03, RULE-MECH-01, RULE-HD-02/03/04, RULE-ONT-01/02); `canon/CEM-001` (Responsabilidades do KG l.608-615), `canon/CHM-001`, `canon/CCM-001`, `canon/CEE-001` l.111, `canon/SAS-001` §6.12; `WORKFLOW.md` (conformidade, não editada) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §6; atomic-spec §3 (emenda SPEC006-MATRIZ) "Knowledge Graph \| CRITICAL \| D0–D7"; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profundidade-alvo | **D0–D7 + D8 adversarial focado** nos pontos sensíveis (imutabilidade INV-07, confiança ≠ Convicção INV-04, causalidade pós-hoc RULE-CAU, colisão, governança de escrita), sem elevar o profile em silêncio [FONTE: ROADMAP §6; AGENTS.md §4; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 3 — MEMÓRIA SEMÂNTICA E RAG; próxima após SPEC-005 (BASELINE v1.0, DHR-SPEC005-002). Opera **sobre** conhecimento já validado/publicado; formação/retrieval é SPEC-007 (não absorvida) [FONTE: ROADMAP §6/§21] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3 teto spec-first; gate normativo E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01 (Classe por BASpec); RULE-PD-01/CC-12 **(N/A — infraestrutura de memória, agnóstica de escola)**; RULE-ECC-04/06; RULE-ECC-05 **(N/A)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — **D** (ontologia/catálogo, temporalidade, versionamento, consulta, trace) + **C** (governança de escrita, imutabilidade INV-07, proveniência, confiança≠Convicção INV-04, fronteira) + **H** (similaridade/causalidade com gate de saída — RULE-CAU); declaração **por BASpec** (SES-001 §50) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-12 |
| Abertura | Dossiê HOMOLOGADO por Andraus (DHR-SPEC006-001, `research.md`); Plan dentro da validade do Dossiê (CRITICAL → 90 dias; limite 2027-01-03; ECC-VAL-001 FECHADA, DHR-DEC-003) |

Complexidade: CRITICAL. Profundidade-alvo: D0–D7 + D8 adversarial focado (standard + adversarial).

**Princípio fundador (transversal):** **MEMÓRIA PERMANENTE ≠ MEMÓRIA DE TRABALHO.** *"Blackboard ↓ memória de trabalho. Knowledge Graph ↓ memória permanente. Nunca misturar."* (KERNEL-V2; ROADMAP §5/§6). O KG é a **representação semântica permanente do conhecimento já validado e suas relações auditáveis** — não é "banco de grafos" (research.md §0) e não é memória de trabalho (SPEC-004). Este Plan define **o QUE** (contrato cognitivo), com o **mecanismo físico INDETERMINADO = H-001 (ABERTA)** — decisão de engenharia de Andraus, não fechada aqui. [FONTE: ROADMAP §6; DHR-SPEC006-001 Q-ABERTURA-3; research.md §0/§8]

**Status epistemológico de cabeçalho:** a SPEC-006 é a **camada Harness/operacional da memória permanente** sobre responsabilidades que os canônicos BASELINED já atribuem ao KG (CEM-001 l.608-615; l.494; l.562-565 Cognitive Trace Reconstruction; CONSTITUTION l.233 EC-COG-003; SAS-001 §6.12; CEE-001 l.111). **NÃO redefine** CHM-001/CEM-001/CCM-001, nem reabre SPEC-004/SPEC-005 (**CC-02/CONST-01/INV-09**). **H-001** permanece **ABERTA**. [FONTE: ROADMAP §6/§7; atomic-spec §12; DHR-SPEC006-001 §3]

### Histórico de versões

| Versão | Data | Alterações (1 linha) |
|---|---|---|
| 1.0 | 2026-10-11 | Entrega candidata inicial (Opção A; mecanismo físico INDETERMINADO = H-001). 13 BASpecs, 6 EC, 13 EARS, 11 cenários, 10 adversariais. |
| 1.1 | 2026-10-12 | Rodada 2: STRUCT-10; §7-bis Bloco C; escrita → E3; duas fontes sob governança única; DERIVA_DE; matriz de integridade; estado = projeção derivada. 13 cenários, 15 ADV. |
| 1.2 | 2026-10-12 | Rodada 3: HERDA cross-escola; `provenance_ref.lineage`; `canonical_status`+transição; admissão [DECISÃO NECESSÁRIA]; INV-CKG-02; §D2.2 colisão; bitemporal. 14 cenários, 16 ADV, INV-CKG-01/02. |
| 1.3 | 2026-10-12 | Rodada 4: T01 corrigido + T15; campo único `school`+`hierarchy_role`; `gate_record` condicional; colisão §D2.2; admissão por estado. 15 cenários, 18 ADV. |
| 1.4 | 2026-10-12 | Rodada 5 (9 Maiores + 8 Menores): proveniência condicional; admissão por estado-por-tipo [PROPOSTA]; `to_node==conviction` proibido; `posthoc_flag` determinístico; versionamento sem fork; §D3.1. 16 cenários, 21 ADV. |
| 1.5 | 2026-10-12 | **Rodada 6 — CONSOLIDAÇÃO + 6 Maiores + Menores.** Regra definida UMA vez (RULE-CKG/BASpec, fonte única); EARS/D4/D6/EC/T/ADV/Herança/checks só referenciam por ID. M-01 preservação "a partir da admissão" (MODIFIED) + conviction {COMPUTED,GATED_PASS,GATED_BLOCK,SUPERSEDED}; M-02 aciclicidade invertida; M-03 trace completo só p/ Evidência (hipótese [PROPOSTA]); M-04 outcome_ref/outcome_timestamp obrigatórios (ou no_outcome); M-05 `computed_by`(produtor autenticado)≠`writer_id`(committer); M-06 `school` de structure + natural_key completo; Menores m-02..m-12. Contagem preservada: 13 BASpecs, 6 EC, 13 EARS, 16 cenários, 21 ADV, INV-CKG-01/02. |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; DHR-SPEC006-001 §3/§4; DHR-SPEC006-PEND-001; ABERTURA §8/§9; RMR-001 l.128 (BL-029) / l.192 (DHR-SPEC006-PEND-001)]

- **Nenhum item do RMR-001 tem gatilho `spec:SPEC-006` homologado isoladamente.** O início da redação **satisfaz ramos de gatilho** de itens pré-existentes — **tratado como reflexo; promoção/encaminhamento é do gate e de Andraus** (o Especificador NÃO promove — CONS-01).
- **BL-003** (persistência física de hipótese/estado) — `Em espera`, gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação`. A parte **física** do BL-003 **É** H-001 (ABERTA) / G-001 (ABERTA) → a SPEC-006 **referencia**, **não absorve** (CONS-01). Precedente SPEC-004: "em redação" = disparo no início do Plan — registro e deixo a promoção a Andraus (fail-closed).
- **BL-011** (MC-EXP-001) — `Em espera`, gatilho inclui `spec:SPEC-006 em redação`. **Fonte de requisitos**; usar como insumo sob COL-EXP-01..05 (CONFLICT-MAP; prevalece SOT canônico). Classificação ≠ aplicação; **não promovo**.
- **BL-010** (MC-RAG-001) — `Em espera`, gatilho `spec:SPEC-007 em redação` ∨ `milestone:FASE 3 iniciada`. BL-010 é fonte da **SPEC-007** → **tangente**; a SPEC-006 respeita a fronteira. **Não promovo**.
- **BL-029** (proveniência) — **`Em espera`** (DHR-SPEC006-PEND-001; gatilho `spec:SPEC-014`/`SPEC-018`/`SPEC-045`; o gatilho `spec:SPEC-004` foi CONSUMIDO). **Independente desta Spec** — não absorvido nem promovido. [FONTE: RMR-001 l.128 / l.192]
- O passo 11-bis pleno ocorre na homologação do Plan.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o KG é **infraestrutura de memória agnóstica de escola** — armazena conhecimento de qualquer camada (inclusive `HERDA`/`HIERARQUIA_DE`) **sem** alterar a hierarquia nem a autoridade de criação (Elliott cria a primária; ICT não cria — INV-01/INV-02). O KG espelha a hierarquia como relações; não a redefine, interpreta ou decide. [FONTE: INV-01/INV-02; ROADMAP §6]
- [x] **CC-02 — Não redefine Modelo Canônico baselined nem SPEC-004/005:** o KG **preserva** linhagem/versões/estados e faz *Cognitive Trace Reconstruction* **referenciando** os contratos canônicos (CEM-001 l.608-615; l.562-565) — entidades **referenciadas por ID+versão, nunca redefinidas**. CDM-001/CNM-001 pendentes não acionam CONST-01. [FONTE: CC-02; CEM-001; SPEC-004/005 BASELINE]
- [x] **CC-03 — Conviction Vector:** o KG **não computa** convicção; a **"confiança de relação"** é escala própria e **NÃO é** o Conviction Vector; dimensionalidade=8 (fechada) intocada; fórmula/pesos/limiares definitivos **pendentes (J-001 ABERTA)**; **nenhum limiar de convicção é declarado**. [FONTE: INV-03; J-001 ABERTA; N-001 ABERTA]
- [x] **CC-04 — Salvaguardas (CEE-001 §10/§11):** nenhuma violada. O KG não emite sinal, não dimensiona risco, não aplica gates de sinal. **INV-04** (leitura fiel, atomic-spec l.404): o CUSTO nunca entra no Conviction Vector; "Convicção ≠ Score" é cláusula-identidade distinta. A confiança de relação nunca retroalimenta o Conviction Vector (ver RULE-CKG-007). [FONTE: CEE-001 §10/§11; INV-04]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D7 + D8 adversarial focado.
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A** — o artefato é Spec/Plan; §59/§60 tornam-se obrigatórios nas Tasks/Cards (BUILD adiado — atomic-spec §14). Omissão justificada.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A (idem CC-06); rastreabilidade: ROADMAP §6 → Dossiê (research.md, HOMOLOGADO DHR-SPEC006-001) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente; INHERITS/ADDED/MODIFIED com ID+versão (RULE-HD-04); REMOVED vazio; MODIFIED (preservação de estados especializada a "a partir da admissão") não contradiz o herdado (RULE-HD-02). Eixo VERTICAL (RULE-HV) avaliado e não aplicável. [FONTE: EUA-E04; RULE-HD-02/03/04]
- [x] **CC-09 — Epistemic Check (RULE-EPI):** mecanismo físico = **INDETERMINADO (H-001 ABERTA)**, não fato; relações causais exigem mecanismo + regime + marcador pós-hoc (RULE-CAU-01/02/03); sem falsa precisão em "confiança de relação" (sem número até calibração); fontes web = DADO [EXTERNO]. [FONTE: RULE-EPI-01..03; RULE-CAU; research.md §8]
- [x] **CC-10 — Terminologia concorrente (RULE-SEM-01):** tratada (ver "Declaração de acepção semântica"): "conhecimento permanente" vs "memória de trabalho" vs "documento recuperado" vs "Observação" (INV-06); "confiança de relação" vs "Convicção"; "esquecimento" = arquivamento versionado; estados do KG vs estados canônicos homônimos. Nenhum termo canônico redefinido (RULE-SEM-04). [FONTE: RULE-SEM-01/04; INV-06; GLOSSARIO]
- [x] **CC-11 — Classe/Mecanismo por BASpec (RULE-MECH-01):** cada BASpec com efeito declara Classe (D/C/H) com critério 4Es; C/H declaram gate de saída determinístico; H declara bounded loop + parada (CKG-008). Por BASpec, nunca por Spec inteira (SES-001 §50). Ver §D3. [FONTE: RULE-MECH-01..04; atomic-spec §9/§10.6]
- [x] **CC-12 — Princípios de Domínio `PD-xx` (RULE-PD-01):** **N/A** (DHR-SPEC006-001 §2; ABERTURA §6; research.md §7). Infraestrutura agnóstica de escola. Registrado, não supressão silenciosa. [FONTE: RULE-PD-01; §10.7]

**Disciplinas N8–N17 incidentes (RULES.md v1.5):** RULE-EPI (H-001≠fato), RULE-CAU-01/02/03 (CKG-008), RULE-MET-01 (não-fabricação), RULE-UNC-01..03 (incerteza localizada sobre eficiência de consulta ampla enquanto H-001 ABERTA — não sobre a completude do trace de Evidência), RULE-SEM-01/04, RULE-ONT-01/02, RULE-DEC-01 (o KG armazena/relaciona/consulta, não decide nem executa — INV-05). INDETERMINADO onde há incerteza material. (Detalhe no §7-bis Bloco C.)

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-006

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - canon/CEM-001 (BASELINE) — Responsabilidades do KG (l.608-615): preservar linhagem; preservar TODAS as versões;
    preservar os estados (ver MODIFIED: especializado a "a partir da admissão"); Cognitive Trace Reconstruction
    COMPLETA da Evidência a partir das relações de Lineage (l.562-565); navegação da cadeia cognitiva (l.494; l.699).
    Proveniência: o campo LOCAL `provenance_ref.lineage` [PROPOSTA] REFERENCIA o campo `Lineage` (CEM-001 Cap.5;
    l.351/539-554) / `derived_from[]` (SPEC-004) — NÃO existe `lineage_ref` no CEM-001. Estados da Evidência =
    ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED (l.258-262 — a Evidência NÃO tem REFUTED). Transições proibidas l.473-475
    (INVALIDATED/ARCHIVED/SUPERSEDED → ACTIVE). O KG CUMPRE; NÃO redefine o CEM (CC-02/INV-10)
  - canon/CHM-001 (BASELINE) — máquina de estados da HIPÓTESE (EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→
    ARCHIVED) e versionamento append-only; o KG ARMAZENA hipóteses por referência, preservando os estados ADMITIDOS;
    REFUTED/SUPERSEDED/ARCHIVED são do CHM (hipótese). NÃO cria nem transiciona estado de hipótese (isso é SPEC-001/CHM-001)
  - canon/CCM-001 (BASELINE) — objeto Conviction Vector 8D; estados do objeto conviction = COMPUTED/GATED_PASS/
    GATED_BLOCK/SUPERSEDED (l.58/78); o KG pode armazenar o valor como propriedade de nó (por referência), mas a
    "confiança de relação" é escala PRÓPRIA e NUNCA é o Conviction Vector (INV-04)
  - specs/features/SPEC-004 v1.2 (BASELINE — DHR-SPEC004-003) — memória de TRABALHO (Blackboard); append-only REAL:
    supersessão = PROJEÇÃO DERIVADA (registro histórico NUNCA mutado; sucessora carrega `supersedes`; INV-CBP-01,
    RULE-CBP-003); versionamento OTIMISTA compare-and-commit (RULE-CBP-004 l.239-246: expected_version obrigatório na
    ATUALIZAÇÃO, EXPECTED_VERSION_REQUIRED l.243-245; criação não exige); proveniência `computed_by`/`gate_record`/
    identidade autenticada (RULE-CBP-007 l.543-558; RULE-CBP-014 l.311-319). O KG é memória PERMANENTE, distinta
    ("Nunca misturar"); HERDA a mecânica append-only e a identidade autenticada por referência; NÃO redefine (CC-02/INV-09)
  - specs/features/SPEC-005 v1.0 (BASELINE — DHR-SPEC005-002) — notificação de mudança (Event Bus); **[INFERÊNCIA]** o
    KG pode CONSUMIR eventos de ciclo de vida só como GATILHO de avaliação autorizada (CKG-009), nunca invalidação
    automática (CEM-001 l.602). O tipo `Evidence.Invalidated` É canônico (CEM-001 l.600/722) e a SPEC-005 o TRANSPORTA
    (plan l.88/l.859); a SPEC-005 **não define** o consumidor nem o contrato de consumo pelo KG = **[DECISÃO NECESSÁRIA]**;
    a SPEC-005 fonta do LOG do Blackboard e NÃO escreve no KG (l.242/l.971). EMISSÃO de eventos pelo KG = [DECISÃO NECESSÁRIA]
  - canon/CEE-001 (BASELINE) l.111 — a métrica de calibração do roteamento "entra no KG"; o KG ARMAZENA como nó (por
    referência), ISOLADA do Conviction Vector (INV-04); não a computa
  - canon/SAS-001 §6.12 (l.923-924) — o Structural Agent atua EXCLUSIVAMENTE como PRODUTOR; registra relações; NÃO
    redefine ontologias/taxonomias. **Escopo FATO NORMATIVO = o Structural Agent.** A EXTENSÃO dessa fronteira a OUTROS
    produtores do KG é **[INFERÊNCIA]/[PROPOSTA]** desta Spec (não é cláusula do SAS-001) — proposta de governança
    uniforme, a homologar. (l.163 EC-COG-003: KG "consultado quando necessário… não é pré-requisito obrigatório")
  - governance/CONSTITUTION.md l.233 (EC-COG-003) — âncora constitucional; conformar-se, não reescrever (INV-09)
  - governance/RULES.md: RULE-BB-004 (append-only; SUPERSEDED, nunca deletados — l.323) REFORÇADO como imutabilidade
    permanente (INV-07); RULE-CAU-01 (mecanismo — l.680), RULE-CAU-02 (regime — l.681), RULE-CAU-03 (pós-hoc — l.682)
    incidem sobre CAUSA (CKG-008); RULE-ONT-01/02 (status ontológico; ontologia extensível por governança — l.671)
  - Método: atomic-spec.md v1.5 (BASpec, D0–D9, EARS, Enforcement E0–E3 — §10.2 "KG publicado → E3 mínimo", TRACE-06,
    Quality Gates, Classe/Mecanismo §10.6, RULE-MM; §3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7)
  - Governança/Avaliação/Maturidade: SPEC-019 v1.0 (RULE-HG/HV — governança spec-time). **[INFERÊNCIA]** alterar a
    ONTOLOGIA seria ato de governança análogo (RULE-HG) — a SPEC-019 **não** cita "ontologia" literalmente; runtime =
    K-001 [DECISÃO NECESSÁRIA]. SPEC-020 v1.0 (9 lentes); SPEC-021 v1.0 (RULE-MM; nível-alvo L3; gate E3)
  - Enforcement: ENF-01..08 (ENF-03 Detector≠Gate; ENF-04 fail-closed; ENF-07 falso-DENY no E3)
  - Invariantes: INV-04 (CUSTO nunca no Conviction Vector; Convicção≠Score — atomic-spec l.404) — a proibição de a
    CONFIANÇA entrar na convicção é regra LOCAL [PROPOSTA] (CKG-007), NÃO cláusula de INV-04; INV-05 (não executa),
    INV-06 (Evidência≠Observação), INV-07 (versionamento monotônico), INV-09 (sem baseline informal), INV-10 (CEM-001
    idioma canônico da Evidência)
  - Setup operacional (fronteira soberana, NÃO redefinida): WORKFLOW.md — o KG é a memória de longo prazo consultada na
    formação de contexto; cita por ID os WF-xx que toque, NÃO contradiz nenhum e NÃO fecha WF-D03

ADDED (delta local — ver "Cobertura × lacuna"):
  - Ontologia ENXUTA + MATRIZ de integridade (tipo × origem/destino × direcionalidade/simetria) — a "gramática do
    conhecimento"; rejeita violação (RULE-CKG-001; §D2.1)
  - Catálogo de ENTIDADES (nós) por referência aos canônicos (inclui `observation` — INV-06) (RULE-CKG-002)
  - Catálogo de RELAÇÕES tipadas: CONFIRMA, REFUTA, DEPENDE_DE, HERDA, PERTENCE_A, INVALIDA, ORIGINA, DERIVA_DE (aresta
    de Lineage), SIMILAR_A (simétrica), CAUSA (sob RULE-CAU), HIERARQUIA_DE, ESTATISTICA_DE (RULE-CKG-003)
  - TEMPORALIDADE BITEMPORAL: `valid_from`/`valid_to` + `recorded_at`; invalidação por NOVO registro (RULE-CKG-004)
  - PROVENIÊNCIA obrigatória CONDICIONAL (espelha SPEC-004 CBP-007) (RULE-CKG-005)
  - IMUTABILIDADE / append-only permanente; estado = PROJEÇÃO DERIVADA; "esquecimento" = arquivamento versionado (RULE-CKG-006)
  - CONFIANÇA de relação — escala PRÓPRIA, ≠ Convicção (RULE-CKG-007)
  - Similaridade/causalidade com juízo + gate de saída (RULE-CKG-008)
  - GOVERNANÇA de escrita (E3); produtor registra mas NÃO redefine ontologia (RULE-CKG-009)
  - FRONTEIRA de entrada em DUAS fontes sob UMA governança (RULE-CKG-010)
  - CONSULTA cognitiva (read-only) + Cognitive Trace Reconstruction COMPLETA da Evidência (RULE-CKG-011)
  - LIFECYCLE do nó/relação (estado = projeção derivada) (RULE-CKG-012)
  - DETECÇÃO/registro de COLISÃO de relações (RULE-CKG-013)
  - Declaração de Classe/Mecanismo por BASpec (CC-11); Enforcement Contracts (EC-CKG-001..006)
  - [PROPOSTA de recorte] contrato cognitivo FECHÁVEL com mecanismo físico INDETERMINADO — NÃO fecha H-001 (Andraus)

MODIFIED (especialização de regra herdada — RULE-HD-02):
  - RULE-BB-004 (append-only do Blackboard) é REFORÇADA, não alterada, como imutabilidade PERMANENTE do KG (INV-07);
    texto/significado inalterados
  - **[M-01] A responsabilidade CEM-001 l.494 "preservar os estados" é ESPECIALIZADA no KG para "preservar TODOS os
    estados A PARTIR DA ADMISSÃO (ACTIVE em diante)".** EMERGENT/CANDIDATE são memória de TRABALHO (SPEC-004 — "nunca
    misturar"), NUNCA admitidos no KG permanente (RULE-CKG-010); sua preservação cabe à SPEC-004, não ao KG. É
    especialização de ALCANCE, não contradição (RULE-HD-02): nenhum estado de objeto ADMITIDO é perdido. O histórico de
    transições do KG começa na admissão; EMERGENT/CANDIDATE não aparecem em `canonical_state_transition_record` do KG.

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco é herança **horizontal / obrigação-a-obrigação** sobre
> canônicos, SPEC-004/005 e regras (EUA-E04 §8.3). O eixo **VERTICAL** (RULE-HV, conservação-como-conjunto pai→filha) foi
> avaliado e **não se aplica**: a SPEC-006 deriva de canônicos/Specs vizinhas/regras, não é decomposição *micro* de uma
> *macro-spec*. [INFERÊNCIA — a confirmar pelo Revisor]

### Cobertura × lacuna (canônicos / SPEC-004 / SPEC-005) — não duplicar (CC-02/INV-09)

| Capacidade | Coberta por canônico/Spec? (arquivo:linha) | Tratamento na SPEC-006 |
|---|---|---|
| Preservar linhagem/versões/estados **dos objetos admitidos**; Trace completo da Evidência | SIM — CEM-001 l.494/608-615; l.562-565 | ESPECIFICAR verificável (CKG-010/011); referencia CEM (ver MODIFIED M-01) |
| Máquina de estados da hipótese | SIM — CHM-001 | HERDADA — armazena por referência; não transiciona |
| Append-only REAL (supersessão = projeção derivada) | SIM — SPEC-004 v1.2 (INV-CBP-01) | HERDADA a mecânica (CKG-004/006/012) |
| Versionamento compare-and-commit (expected_version) | SIM — SPEC-004 RULE-CBP-004 l.239-246 | HERDADA e aplicada ao KG (CKG-012) |
| Memória de TRABALHO / objetos EMERGENT/CANDIDATE | SIM — SPEC-004 v1.2 | FRONTEIRA — não admitidos no KG (CC-02/INV-09) |
| Notificação/transporte de mudança | SIM — SPEC-005 v1.0 | FRONTEIRA — [INFERÊNCIA]/[DECISÃO NECESSÁRIA] consumo; emissão = [DECISÃO NECESSÁRIA] |
| Proveniência (`Lineage`/`gate_record`/`derived_from[]`) | SIM — CEM-001 Cap.5; SPEC-004 v1.2 | REFERÊNCIA obrigatória (CKG-005); campo local [PROPOSTA] |
| **Ontologia + matriz de integridade** | NÃO | LACUNA CENTRAL — ADDED (CKG-001) |
| **Catálogo de entidades/relações (+DERIVA_DE, observation)** | NÃO | LACUNA CENTRAL — ADDED (CKG-002/003) |
| **Temporalidade bitemporal das relações** | Parcial (estados, não validade de relação) | LACUNA — ADDED (CKG-004) |
| **Confiança de relação (≠ Convicção)** | NÃO | LACUNA — ADDED (CKG-007) |
| **Similaridade/causalidade (RULE-CAU)** | Parcial | LACUNA — ADDED (CKG-008) |
| **Consulta cognitiva** | NÃO | LACUNA — ADDED (CKG-011) |
| **Governança de escrita + da ontologia** | Parcial — SAS-001 §6.12; SPEC-019 | LACUNA — ADDED (CKG-009; E3) |
| **Lifecycle do nó/relação do KG** | Parcial | LACUNA — ADDED (CKG-012) |
| **Mecanismo físico de armazenamento** | NÃO — H-001 ABERTA | NÃO fechar — Andraus (INDETERMINADO) |

---

## Declaração de acepção semântica (RULE-SEM-01 — CC-10)

> **Termo 1:** "Conhecimento permanente" (KG) = conhecimento já validado/publicado + relações auditáveis. **≠ "memória
> de trabalho"** (Blackboard — SPEC-004). *"Nunca misturar."*
> **Termo 2:** "confiança de relação" (KG) = escala PRÓPRIA. **≠ "Convicção"** (CCM-001). NUNCA retroalimenta o Conviction
> Vector (INV-04 = o CUSTO nunca entra; "Convicção ≠ Score" é cláusula-identidade distinta — atomic-spec l.404).
> **Termo 3:** "esquecimento"/"forgetting" = **arquivamento versionado**, **NUNCA deleção** (INV-07).
> **Termo 4:** "documento recuperado" (RAG — SPEC-007) ≠ "conhecimento validado" (KG). **"Observação"** (Skill — INV-06;
> `observation`) ≠ "Evidência" (`evidence`): tipos de nó distintos (CKG-001).
> [FONTE: RULE-SEM-01/04; INV-04/06/07; GLOSSARIO; KERNEL-V2; SPEC-004/005/007]

---

## Conformidade com o `WORKFLOW.md` (RULE-ECC-05 — determinação de NÃO-incidência)

> **RULE-ECC-05 NÃO INCIDE** sobre a SPEC-006 [FONTE: DHR-SPEC006-001 §2; ABERTURA §1/§6; research.md §7]: não define nem
> toca comportamento de agente analítico, Conviction/Fusion, Manager ou Risk Agent — é infraestrutura de memória (como
> SPEC-002/004/005/019/020/021). Por prudência confirma-se conformidade: o KG é consultado "quando necessário" (SAS-001
> §6.12/l.163). Cita WF-xx só por ID, **não contradiz** nenhum e **não fecha** WF-D03 (ABERTA).

---

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide** (DHR-SPEC006-001 §2; ABERTURA §6; research.md §7). Infraestrutura agnóstica de escola. Nenhum
`PD-xx` proposto (CC-12 = N/A). Registrado — não é supressão silenciosa. [FONTE: RULE-PD-01; §10.7]

---

## D0 — Missão (Intenção)

A SPEC-006 especifica **como o SOT preserva, relaciona e consulta o conhecimento permanente já validado** — o **contrato
cognitivo da memória semântica permanente**: ontologia enxuta + matriz de integridade, catálogo de entidades (incl.
`observation` — INV-06) e relações tipadas (incl. `DERIVA_DE`, `SIMILAR_A`, `CAUSA` sob RULE-CAU), temporalidade
bitemporal, proveniência condicional, imutabilidade append-only ("esquecimento" = arquivamento versionado — INV-07),
confiança de relação (≠ Convicção — INV-04), governança de escrita (E3), fronteira de entrada (canônicos via ciclo de
vida + conhecimento formado via selo SPEC-007 [DECISÃO NECESSÁRIA]), consulta cognitiva e **Cognitive Trace
Reconstruction COMPLETA da Evidência** (CEM-001 l.608-615) — preservando **memória permanente ≠ trabalho** e deixando o
**mecanismo físico INDETERMINADO (H-001 ABERTA)**: define-se **o QUE**, não **o COMO**. [FONTE: ROADMAP §6; CEM-001
l.608-615; CHM-001; SAS-001 §6.12; DHR-SPEC006-001; research.md §4]

**O que a Missão NÃO é (fronteira):**
- Não é **memória de trabalho** → **SPEC-004 (BASELINE)**. *"Nunca misturar."*
- Não **transporta/notifica** → **SPEC-005 (BASELINE)**; consumo de evento pelo KG = [INFERÊNCIA]/[DECISÃO NECESSÁRIA]; emissão pelo KG = [DECISÃO NECESSÁRIA].
- Não **forma conhecimento** / não faz retrieval → **SPEC-007**; recebe conhecimento **publicado**.
- Não define **estado persistente por agente** → **SPEC-009**; **G-001 (ABERTA)**.
- Não especifica o **ciclo de evolução (P12)** → **SPEC-018**; **K-001 (ABERTA)**.
- Não **computa** convicção → **SPEC-003/CCM-001**; **J-001/N-001 (ABERTAS)**.
- Não **redefine** CHM-001/CEM-001/CCM-001 nem SPEC-004/005 → **CC-02/CONST-01/INV-09**.
- Não **escolhe o mecanismo físico** → **H-001 (ABERTA — só Andraus)**; INDETERMINADO.
- Não **decide** nem **executa** ordem → INV-05/RULE-DEC-01.

**Status epistemológico:** RULE-CKG-* e o contrato de nó/relação são **[PROPOSTA]** até homologação. CEM-001, CHM-001,
CCM-001, CEE-001, SAS-001, SPEC-004 v1.2, SPEC-005 v1.0, SPEC-001/019/020/021, RULE-BB-004, RULE-CAU-01/02/03, RULE-ONT-01/02,
atomic-spec v1.5, INV-*, ENF-* são FATO NORMATIVO. Fontes externas (research.md §2) são [EXTERNO] — DADO, nunca baseline (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Regra (fonte única) |
|---|---|---|
| S1 | Ontologia enxuta + matriz de integridade; rejeita violação | RULE-CKG-001; §D2.1 |
| S2 | Entidades (nós) por referência aos canônicos (incl. `observation` — INV-06); nós de construção teórica carregam `ontological_status` ∈ {observational, theoretical} (RULE-ONT-01) | RULE-CKG-002; S-catálogo |
| S3 | Relações tipadas (incl. DERIVA_DE de Lineage; SIMILAR_A simétrica; CAUSA) | RULE-CKG-003; §D2.1 |
| S4 | Temporalidade bitemporal das relações (`valid_from`/`valid_to`/`recorded_at`) | RULE-CKG-004 |
| S5 | Proveniência obrigatória CONDICIONAL (espelha SPEC-004 CBP-007) | RULE-CKG-005 |
| S6 | Imutabilidade / append-only permanente; estado = projeção derivada | RULE-CKG-006 |
| S7 | Confiança de relação — escala própria, ≠ Convicção | RULE-CKG-007 |
| S8 | Similaridade/causalidade com juízo + gate de saída (RULE-CAU) | RULE-CKG-008 |
| S9 | Governança de escrita (E3) + da ontologia; produtor não redefine ontologia (SAS-001 §6.12 — escopo Structural Agent; extensão a outros produtores = [INFERÊNCIA]) | RULE-CKG-009 |
| S10 | Fronteira de entrada (duas fontes, uma governança); admissão por estado admissível POR TIPO [PROPOSTA] (exclui EMERGENT/CANDIDATE); gatilho/produtor de promoção = [DECISÃO NECESSÁRIA] | RULE-CKG-010 |
| S11 | Consulta cognitiva (read-only) + Trace completo da Evidência (hipótese = [PROPOSTA]) | RULE-CKG-011 |
| S12 | Lifecycle do nó/relação; estado derivado; nunca remoção | RULE-CKG-012 |
| S13 | Detecção/registro de colisão; não resolve em silêncio | RULE-CKG-013; §D2.2 |
| S14 | Conhecimento permanente × temporário (ROADMAP §6): "temporário" = com janela de validade (`valid_to`) ou `relevance` rebaixada — nunca deletado. O **critério de promoção trabalho→permanente** NÃO é fechado aqui; atribuí-lo à SPEC-018/K-001 é PROPOSTA submetida a Andraus = **[DECISÃO NECESSÁRIA]** | ROADMAP §6; K-001 (ABERTA) |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Mecanismo físico de armazenamento | **H-001 (ABERTA — só Andraus)** | INDETERMINADO |
| Memória de trabalho / objetos EMERGENT/CANDIDATE | **SPEC-004 (BASELINE)** | "Nunca misturar"; CC-02/INV-09 |
| Notificação/transporte; emissão de evento pelo KG | **SPEC-005 (BASELINE)** | consumo = [INFERÊNCIA]/[DECISÃO NECESSÁRIA]; emissão = [DECISÃO NECESSÁRIA] |
| Formação de conhecimento / retrieval | **SPEC-007** | recebe conhecimento publicado |
| Estado persistente por agente | **SPEC-009** — **G-001 (ABERTA)** | persistência por agente |
| Ciclo de evolução (P12) | **SPEC-018** — **K-001 (ABERTA)** | governança de aprendizado |
| Redefinir CHM/CEM/CCM/SPEC-004/005 | canônicos/baseline | CC-02/CONST-01/INV-09 |
| Fórmula/pesos/limiares de convicção | **SPEC-003/CCM-001; J-001/N-001 (ABERTAS)** | INV-03/INV-04 |
| Componente "Cognitive Ontology" separado | — (ontologia DENTRO da SPEC-006) | DHR-SPEC006-001 Q-ABERTURA-4; criar componente é de Andraus |
| Escolher tecnologia de banco de grafos | **H-001 (ABERTA)** | fora do mandato; Andraus |

---

## D2 — Regras (FONTE ÚNICA de cada obrigação normativa)

> **Etiqueta:** RULE-CKG-* e o contrato de nó/relação são **[PROPOSTA]** — normativos só na homologação de Andraus +
> registro do Controlador (RULE-HG-02). As RULE/INV/ENF citadas como fundamento (CEM-001, CHM-001, CCM-001, RULE-BB-004,
> RULE-CAU-01/02/03, RULE-ONT-01/02, INV-04/05/06/07/09/10, ENF-03/04/07, SAS-001 §6.12, SPEC-004 INV-CBP-01/CBP-004/007/014)
> **já existem** e são FATO NORMATIVO. **Cada regra é definida AQUI uma única vez; EARS, D4, D6, EC, D7, D8, Herança e
> checks.md apenas a REFERENCIAM por ID e acrescentam o que é próprio (cenário, dado, contrato).**

```
RULE-CKG-001: Todo nó/relação escrito DEVE pertencer à ONTOLOGIA permitida (tipo ∈ catálogo) e satisfazer a MATRIZ DE
              INTEGRIDADE §D2.1 (origem/destino, direcionalidade, simetria por tipo). REGRA DE NÓ: `hypothesis.school ≠ ICT`
              (ICT não cria hipótese — INV-02/RULE-HH-004); HERDA só liga SUB a PAI `hierarchy_role=PRIMARY` (RULE-HH-003).
              Violação é REJEITADA (fail-closed). A ontologia é ENXUTA e vive DENTRO da SPEC-006. O KG ESPELHA os vínculos
              já criados pelos agentes; NÃO decide a autoridade de criação (CC-01).
              [Fonte: KERNEL-V2 l.1488-1507; DHR-SPEC006-001 Q-ABERTURA-4; INV-02; SPEC-001 RULE-HH-003 l.104/RULE-HH-004 l.108]  [PROPOSTA]

RULE-CKG-002: Toda ENTIDADE que corresponde a objeto canônico (hypothesis/CHM-001, evidence/CEM-001, conviction/CCM-001)
              DEVE referenciá-lo por ID+versão — NUNCA redefinir contrato/campos/estados (CC-02/INV-10). Um nó `observation`
              (Skill — INV-06) NÃO pode ser rotulado `evidence`. O KG grava `canonical_status` (snapshot do Status — único
              campo mutável, CEM-001 l.264) e, a cada mudança, um registro `canonical_state_transition` (estado/timestamp/
              origem/justificativa — CEM-001 l.428), VALIDANDO a transição contra a tabela do TIPO (CHM; CEM — ACTIVE/
              SUPERSEDED/INVALIDATED/ARCHIVED, SEM REFUTED): transições PROIBIDAS (CEM-001 l.473-475: INVALIDATED/ARCHIVED/
              SUPERSEDED → ACTIVE) são REJEITADAS (`FORBIDDEN_CANONICAL_TRANSITION`); reativação de estado terminal é VETADA.
              [Fonte: CEM-001 l.264/428/468-475; CHM-001; CCM-001; CC-02; INV-06; INV-10]  [PROPOSTA]

RULE-CKG-003: Toda RELAÇÃO DEVE ser tipada, armazenada DIRECIONADA (origem→destino) e carregar proveniência (CKG-005). A
              simetria (ex.: SIMILAR_A) é propriedade SEMÂNTICA da consulta (A~B ⇔ B~A), não ausência de direção. Admitir
              um `evidence` DERIVED EXIGE materializar uma aresta `DERIVA_DE` por ancestral do seu Lineage (fail-closed se
              algum ancestral não estiver referenciado/presente — INV-CKG-02). **ACICLICIDADE [M-02]:** a aresta DERIVA_DE
              não pode fechar ciclo — REJEITA (`LINEAGE_CYCLE`) se a ORIGEM já é alcançável a PARTIR do DESTINO seguindo
              DERIVA_DE (i.e., o destino já descende da origem; adicionar a aresta tornaria a origem descendente do que já
              é seu descendente). Contradição não é silenciada (CKG-013).
              [Fonte: ROADMAP §6; research.md §4/§8; INV-07; CEM-001 l.565]  [PROPOSTA]

RULE-CKG-004: A mudança de validade de uma relação é ATO AUTORIZADO (CKG-009), NUNCA automática/cascata (CEM-001 l.602; o
              impacto sobre hipóteses/convicções é de CHM/CCM — l.503/606; CHM-001 l.672-676). NÃO muta o registro
              existente: grava NOVO registro (invalidação/sucessão) com `recorded_at` e, quando aplicável, `valid_to`
              (`targets_record_id`=R0 referenciado, DISTINTO de `supersedes`). A validade corrente é PROJEÇÃO DERIVADA.
              **Bitemporal:** valid-time (`valid_from`/`valid_to`) + transaction-time (`recorded_at`). Rejeita janela
              inválida `valid_to < valid_from` (`INVALID_TIME_WINDOW`). Convenção: `valid_to = null` ≡ +∞ (vigente).
              Invalidar ≠ deletar (INV-07; espelha SPEC-004 INV-CBP-01).
              [Fonte: research.md §3.1; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.503; CHM-001 l.672-676]  [PROPOSTA]

RULE-CKG-005: Nenhuma entidade/relação existe sem PROVENIÊNCIA, espelhando a condicionalidade de SPEC-004 RULE-CBP-007
              (l.543-558): (a) `computed_by` — identidade AUTENTICADA do PRODUTOR/PROPONENTE (RULE-CBP-014 l.311-319) —
              SEMPRE obrigatório; (b) `gate_record` SÓ quando o objeto resulta de gate; (c) `provenance_ref.lineage`/
              `derived_from` SÓ quando DERIVADO. Para `asset`/`timeframe`/`regime`/`observation` e hipóteses PRIMARY,
              `lineage=[]` é legítimo (NÃO force gate_record/lineage fabricado — RULE-MET-01). Escrita sem a proveniência
              EXIGÍVEL é REJEITADA (`PROVENANCE_MISSING`; subcódigo `COMPUTED_BY_MISSING`). `provenance_ref.lineage`
              [PROPOSTA] referencia `Lineage` (CEM-001 Cap.5)/`derived_from[]` (SPEC-004) — não há `lineage_ref` no CEM-001.
              **Identidade [M-05]:** `computed_by` (produtor autenticado) é DISTINTO de `writer_id` (identidade autenticada
              do COMMITTER — runtime ou serviço do KG); ambos autenticados, não oriundos do payload (ver D6/contrato).
              [Fonte: CEM-001 Cap.5; SPEC-004 RULE-CBP-007 l.543-558/CBP-014 l.311-319; research.md §3.2]  [PROPOSTA]

RULE-CKG-006: O KG é APPEND-ONLY PERMANENTE (INV-07; reforça RULE-BB-004; espelha SPEC-004 INV-CBP-01): nenhum registro é
              DELETADO nem MUTADO (`IMMUTABILITY_VIOLATION`). "Esquecimento"/consolidação = ARQUIVAMENTO versionado (novo
              registro — CKG-012). Estado corrente = PROJEÇÃO DERIVADA; toda transição reconstruível (P13).
              [Fonte: INV-07; RULE-BB-004 (RULES.md l.323); SPEC-004 INV-CBP-01; research.md §3.6]  [PROPOSTA]

RULE-CKG-007: A CONFIANÇA de relação é escala PRÓPRIA do KG, em NAMESPACE próprio, e NÃO É a Convicção (CCM-001). O KG NÃO
              a escreve/devolve em campos do objeto de convicção, e **NÃO escreve NENHUMA aresta cujo
              `to_node.node_type == conviction`** — predicado VERIFICÁVEL por tipo de destino: proíbe CAUSA→conviction e
              ESTATISTICA_DE→conviction de QUALQUER origem e fecha o contorno por 2 SALTOS (`EDGE_TO_CONVICTION_FORBIDDEN`).
              INV-04 (atomic-spec l.404) proíbe CUSTO no Conviction Vector; a convicção é computada SÓ pela SPEC-003/CCM-001
              (extensão LOCAL [PROPOSTA], não cláusula de INV-04). Que o cálculo de convicção não a consuma é requisito à
              SPEC-003 / [DECISÃO NECESSÁRIA]. A escala de confiança é PARÂMETRO a calibrar (INDETERMINADO; não toca J-001/N-001).
              [Fonte: INV-04 (custo); CCM-001; SPEC-003; RULE-MET-01; research.md §4]  [PROPOSTA]

RULE-CKG-008: Toda relação CAUSA DEVE declarar MECANISMO+DIREÇÃO+CONDIÇÕES (RULE-CAU-01), REGIME (RULE-CAU-02) e
              `posthoc_flag` BOOLEANO obrigatório (RULE-CAU-03); correlação/precedência não bastam. **Desfecho [M-04]:**
              DEVE referenciar o desfecho — `outcome_ref` + `outcome_timestamp` obrigatórios; quando não há desfecho, exige
              declaração explícita `no_outcome=true` + justificativa (sem desfecho ⇒ `posthoc_flag=false` e nenhuma regra
              temporal incide). **Regra determinística:** se `recorded_at` > `outcome_timestamp`, então `posthoc_flag` DEVE
              ser `true` (`POSTHOC_FLAG_REQUIRED`). Faltando qualquer campo (incl. `outcome_ref` sem `no_outcome`): rejeita
              (`CAUSAL_FIELDS_MISSING`; subcódigos `POSTHOC_FLAG_REQUIRED`/`OUTCOME_REF_MISSING`). SIMILAR_A proposta por
              juízo exige `similarity_basis`. Classe H: bounded loop (parada) + gate de saída determinístico que verifica a
              PRESENÇA dos campos e a regra de carimbo (não a veracidade — ENF-03).
              [Fonte: RULE-CAU-01/02/03 (RULES.md l.680-682); research.md §8]  [PROPOSTA]

RULE-CKG-009: A escrita permanente é GOVERNADA e E3 (atomic-spec §10.2 "KG publicado → E3 mínimo"), fail-closed: só
              ESCRITORES AUTORIZADOS escrevem, com identidade AUTENTICADA pelo runtime (reusa SPEC-004 CBP-014 — não define
              auth nova); FALHA da autenticação ⇒ NÃO-AUTORIZADO (`WRITE_UNAUTHORIZED`; subcódigo `AUTH_UNAVAILABLE`). O
              produtor registra relações mas NÃO redefine a ONTOLOGIA/TAXONOMIA (`ONTOLOGY_REDEFINITION_FORBIDDEN`). **A
              fronteira "produtor registra, não redefine ontologia" é FATO NORMATIVO só para o Structural Agent (SAS-001
              §6.12); sua extensão a OUTROS produtores é [INFERÊNCIA]/[PROPOSTA] desta Spec.** Alteração da ONTOLOGIA é ato
              de GOVERNANÇA (spec-time análogo a RULE-HG/SPEC-019 — [INFERÊNCIA]; runtime K-001 [DECISÃO NECESSÁRIA]),
              prospectiva e backward-compatible (INV-07); migração de `schema_version` = [DECISÃO NECESSÁRIA]. Quem mantém a
              allowlist de escritores e quem hospeda o juízo CKG-008 = [DECISÃO NECESSÁRIA] (runtime; K-001/SPEC-018).
              [Fonte: SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; SPEC-019 RULE-HG; ENF-03/04]  [PROPOSTA]

RULE-CKG-010: O KG recebe conhecimento por DUAS fontes sob a MESMA governança (CKG-009): (a) OBJETOS CANÔNICOS e suas
              transições via CICLO DE VIDA canônico (já validados por SPEC-001/002/003); (b) CONHECIMENTO FORMADO via SELO
              DE PUBLICAÇÃO da SPEC-007 (contrato do selo = DEPENDÊNCIA da SPEC-007 = [DECISÃO NECESSÁRIA]). Formado SEM
              selo é REJEITADO (`FORMED_WITHOUT_SEAL`). O KG NÃO faz formação/extração/retrieval. **Critério de admissão
              do caminho (a) — gate verificável POR TIPO [PROPOSTA]:** admite só objeto cujo `canonical_status` ∈ conjunto
              admissível do TIPO — **hypothesis (CHM-001)** ∈ {ACTIVE, DOMINANT, SUPERSEDED, REFUTED, ARCHIVED}; **evidence
              (CEM-001 l.258-262)** ∈ {ACTIVE, SUPERSEDED, INVALIDATED, ARCHIVED}; **conviction (CCM-001 l.58/78)** ∈
              {COMPUTED, GATED_PASS, GATED_BLOCK, SUPERSEDED} — **EXCLUINDO EMERGENT/CANDIDATE** (ainda TRABALHO — SPEC-004).
              Fora do conjunto: `CANONICAL_STATUS_NOT_ADMISSIBLE`. **[M-01]** Os estados A PARTIR DA ADMISSÃO são preservados
              (CEM-001 l.494, especializado em MODIFIED); EMERGENT/CANDIDATE nunca são admitidos nem registrados no histórico
              do KG. O PRODUTOR e o GATILHO/EVENTO de promoção trabalho→permanente permanecem **[DECISÃO NECESSÁRIA]** (a
              SPEC-005 não escreve no KG — plan l.971; atribuir à SPEC-018/K-001 é proposta a Andraus, não homologada).
              [Fonte: ROADMAP §6/§7; CEM-001 l.258-262/l.494; CHM-001; CCM-001 l.58/78; research.md §3.4]  [PROPOSTA]

RULE-CKG-011: O KG DEVE oferecer CONSULTA cognitiva read-only (padrão/similaridade/causalidade/histórico/multi-salto) sem
              alterar estado. **Cognitive Trace Reconstruction COMPLETA é obrigação GARANTIDA apenas para a EVIDÊNCIA
              [M-03]**, navegando as arestas `DERIVA_DE` (evidence→evidence) — completude assegurada por INV-CKG-02 (aresta
              obrigatória por ancestral + aciclicidade) e NÃO rebaixada por H-001 (só a EFICIÊNCIA de consultas multi-salto
              amplas fica INDETERMINADA). O trace ignora o filtro de validade (ancestral SUPERSEDED/ARCHIVED permanece —
              CEM-001 l.602). O **trace de HIPÓTESE** (via ORIGINA/HERDA/DEPENDE_DE) é oferecido como **[PROPOSTA] best-effort,
              SEM alegação de completude** (INV-CKG-02 não cobre essas arestas — não há gate de aresta obrigatória nem de
              aciclicidade para HERDA/DEPENDE_DE nesta versão; estender é trabalho futuro).
              [Fonte: CEM-001 l.608-615/l.562-565/l.612-614/l.602; SAS-001 §6.12/l.163; research.md §3.4]  [PROPOSTA]

RULE-CKG-012: O estado (ACTIVE_KNOWLEDGE / SUPERSEDED / INVALIDATED_IN_TIME / ARCHIVED) é PROJEÇÃO DERIVADA (não campo
              mutado). Critérios: SUPERSEDED = existe sucessora com `supersedes` (conteúdo corrigido); INVALIDATED_IN_TIME =
              invalidação com `valid_to` sem sucessora de conteúdo; ARCHIVED = arquivamento sob gate E3 (CKG-009). Correção/
              reativação = NOVO registro, nunca mutação (INV-07). **Versionamento (INV-07) — gate de escrita, DENY se
              violado (espelha SPEC-004 RULE-CBP-004 l.239-246):** uma ATUALIZAÇÃO/sucessora só é aceita se `supersedes`
              aponta p/ a ÚLTIMA versão corrente da chave E `version == anterior+1` E `expected_version` == versão corrente
              no commit (compare-and-commit atômico); `expected_version` é OBRIGATÓRIO na atualização (ausente ⇒
              `EXPECTED_VERSION_MISMATCH`; criação inicial não exige — CBP-004 l.243-246). Proibido FORK (2ª sucessora da
              mesma versão ⇒ `VERSION_FORK_FORBIDDEN`). Dedupe: mesma chave natural sem `supersedes` divergente ⇒ DENY;
              reescrita idêntica = no-op.
              [Fonte: CHM-001; INV-07; SPEC-004 INV-CBP-01 / RULE-CBP-004 l.239-246; research.md §3.6]  [PROPOSTA]

RULE-CKG-013: Colisão sse duas relações (i) formam PAR CONTRADITÓRIO da tabela §D2.2, (ii) têm ESCOPO coincidente DO PAR
              (CONFIRMA×REFUTA: mesmos `from_node`/`to_node`; INVALIDA×alvo: `INVALIDA.target_relation_id == r2.relation_id`),
              (iii) janelas de validade se SOBREPÕEM e (iv) AMBAS NÃO-SUPERSEDED. Então o KG DETECTA e grava um
              `collision_record` COM IDENTIDADE/PROVENIÊNCIA PRÓPRIAS (`collision_id`/`version`/`computed_by`=`writer_id`=
              SERVIÇO do KG sob capability de detecção/`recorded_at`; E3) referenciando ambas (preservadas); NUNCA
              sobrescreve em silêncio. Fora dessas condições NÃO há colisão. A RESOLUÇÃO é de SPEC-007/SPEC-018 ou governança
              — o KG só detecta e registra.
              [Fonte: INV-07; §D2.2; research.md §8; fronteira SPEC-007/SPEC-018]  [PROPOSTA]
```

### D2.1 — Matriz de integridade da ontologia (RULE-CKG-001) [PROPOSTA]

> **`school`/`hierarchy_role` DERIVADOS da proveniência canônica, NÃO auto-declarados [F-04/M-06]:** resolvidos do
> `producer_id`/`producer_type` do objeto canônico referenciado (CHM-001 l.361; SPEC-001 l.187/203/214; allowlist
> `AUTHORIZED_PRODUCERS` SPEC-001 l.524) — não de atributo do payload (CBP-014). `school` = escola do produtor
> (Elliott/SMC/Fibonacci/ICT); `hierarchy_role` ∈ {PRIMARY, SUB}. **Para `structure` (M-06):** `school` é derivado do
> `producer_id` do registro do agente (ex.: SAS/Structural Agent — SAS-001 §6.12) que PUBLICA a structure, por
> referência — nunca do payload. O KG **espelha**, NÃO decide, a autoridade (CC-01). Regra de nó: `hypothesis.school ≠ ICT`
> (INV-02/RULE-HH-004 — SPEC-001 l.108/l.515-520). HERDA sub→pai ENTRE escolas é NORMAL (SPEC-001 RULE-HH-003 l.104;
> CHM-001 `parent_hypothesis_id` l.165/415; CONSTITUTION l.193); HERDA valida só `pai.hierarchy_role=PRIMARY`.

| Relação | Origem (node_type) | Destino (node_type) | Direcional | Simétrica (consulta) |
|---|---|---|---|---|
| CONFIRMA | **evidence** (NÃO observation — CONSTITUTION l.191; INV-06) | hypothesis | sim | não |
| REFUTA | **evidence** (NÃO observation) | hypothesis | sim | não |
| DEPENDE_DE | hypothesis, mission | hypothesis, evidence | sim | não |
| HERDA | hypothesis (`hierarchy_role=SUB`) | hypothesis (**PAI = PRIMARY** — RULE-HH-003); entre escolas permitido | sim | não |
| PERTENCE_A | hypothesis, evidence, structure, observation | asset, timeframe, regime, mission | sim | não |
| INVALIDA | evidence, learning | evidence, relation (via `target_relation_id`) | sim | não |
| ORIGINA | structure/hypothesis cujo `school` (derivado do produtor — M-06) ∈ {Elliott, SMC, Fibonacci} — **nunca ICT** (INV-02) | hypothesis | sim | não |
| DERIVA_DE | evidence (DERIVED) | evidence (ancestral) | sim | não — aresta de Lineage; base do trace (CKG-011); obrigatória por ancestral (INV-CKG-02) |
| SIMILAR_A | qualquer **exceto conviction** (m-07) | mesmo node_type **exceto conviction** | sim (armazenada) | **sim** (A~B ⇔ B~A) |
| CAUSA | qualquer | qualquer — **destino `conviction` PROIBIDO (QUALQUER origem; predicado `to_node.node_type==conviction`; INV-04)** | sim | não — exige mechanism+direction+conditions+regime + `posthoc_flag` (CKG-008) |
| HIERARQUIA_DE | structure, timeframe | structure, timeframe | sim | não |
| ESTATISTICA_DE | learning | hypothesis, structure, asset | sim | não |

> **DERIVA_DE × proveniência:** `DERIVA_DE` é RELAÇÃO navegável (aresta de Lineage entre nós), consumida pela Trace
> Reconstruction (ordem = ancestralidade — CEM-001 l.567-577). `provenance_ref.lineage` é CAMPO de proveniência do
> registro (referencia `Lineage`/`derived_from[]`) — não é aresta navegável. Coexistem.

> **INV-CKG-01 (Memória permanente imutável) [PROPOSTA]:** nenhum registro é deletado/mutado; estado = projeção derivada;
> consolidação = arquivamento versionado; toda entidade/relação carrega proveniência e é reconstruível. Reforça — não
> redefine — RULE-BB-004/INV-07/SPEC-004 INV-CBP-01, no eixo permanente.

> **INV-CKG-02 (Completude e aciclicidade da linhagem da EVIDÊNCIA) [PROPOSTA]:** admitir um `evidence` DERIVED EXIGE
> uma aresta `DERIVA_DE` para CADA ancestral do seu `Lineage` (CEM-001 l.565) — fail-closed se algum ausente (CKG-003);
> o grafo DERIVA_DE é ACÍCLICO (M-02); o trace ignora validade (ancestral invalidado permanece — CEM-001 l.602). Garante
> a COMPLETUDE do trace de EVIDÊNCIA (CEM-001 l.612-614), independente de H-001. **NÃO cobre o trace de hipótese** (que é
> [PROPOSTA] best-effort — CKG-011). **Ordem de admissão (evita deadlock):** o derivado só é admitido depois de (ou com)
> os ancestrais; enquanto um ancestral não for admitido, o derivado AGUARDA (`PENDING_ANCESTOR`, transitório em buffer de
> admissão FORA do armazenamento — não é registro do KG; durabilidade do buffer = H-001). Não falha-para-sempre.

### D2.2 — Tabela de contradição e escopo de colisão (RULE-CKG-013) [PROPOSTA]

**Escopo — depende do par:** CONFIRMA×REFUTA = mesmos `from_node`/`to_node`; INVALIDA×alvo = `INVALIDA.target_relation_id
== r2.relation_id`. **Condições (todas):** (i) par ∈ tabela; (ii) escopo coincidente; (iii) sobreposição temporal
(interseção de `[valid_from, valid_to)` não vazia, com `valid_to=null`≡+∞); (iv) ambas NÃO-SUPERSEDED.

| Tipo A | Tipo B (contradiz A) | Escopo do par | Simétrico? | Observação |
|---|---|---|---|---|
| CONFIRMA | REFUTA | mesmos `from_node`/`to_node` | **sim** | mesma hipótese afirmada e negada ao mesmo tempo |
| INVALIDA | relação-alvo `r2` | `INVALIDA.target_relation_id == r2.relation_id` | não | INVALIDA vigente sobre relação-alvo não-SUPERSEDED |

> Pares NÃO listados não são contradição estrutural. **NÃO colidem:** (a) `from_node` diferentes; (b) validades disjuntas;
> (c) uma SUPERSEDED. A resolução é de SPEC-007/SPEC-018 ou governança. Tabela ENXUTA, extensível por governança (RULE-ONT-02).

---

## Critérios de Aceitação (EARS)

> Cada EARS referencia a regra-fonte (D2) por ID; não reescreve a regra.

1. (CKG-001) Quando um nó/relação é submetido para escrita, o KG DEVE escrevê-lo só se o tipo ∈ ontologia e a matriz §D2.1 é satisfeita, e DEVE rejeitar (fail-closed) violação de tipo/integridade.
2. (CKG-002) Quando um nó corresponde a objeto canônico, o KG DEVE referenciá-lo por ID+versão e NÃO DEVE redefinir contrato/campos/estados; DEVE validar cada `canonical_state_transition` contra a tabela do tipo e rejeitar transição proibida/reativação de estado terminal; `observation` NÃO DEVE ser rotulado `evidence`.
3. (CKG-003) Quando uma relação é escrita, o KG DEVE exigir tipo, direção e proveniência; para `evidence` DERIVED DEVE exigir `DERIVA_DE` por ancestral e DEVE rejeitar aresta que feche ciclo na linhagem.
4. (CKG-004) Quando a validade de uma relação muda, o KG DEVE gravar NOVO registro de invalidação/sucessão, DEVE rejeitar janela `valid_to < valid_from`, e NÃO DEVE mutar nem deletar o registro existente.
5. (CKG-005) Quando qualquer escrita é tentada, o KG DEVE exigir `computed_by` (produtor autenticado) sempre, `gate_record` se há gate e `lineage` se derivado, e DEVE rejeitá-la sem a proveniência exigível.
6. (CKG-006) Quando um "esquecimento"/consolidação é solicitado, o KG DEVE arquivar/rebaixar por novo registro versionado, e NÃO DEVE remover nem mutar registro histórico.
7. (CKG-007) Quando uma confiança de relação é registrada ou lida, o KG DEVE mantê-la em namespace próprio e NÃO DEVE escrevê-la/devolvê-la em campos do objeto de convicção, nem escrever QUALQUER aresta `to_node.node_type == conviction` (direta ou por 2 saltos).
8. (CKG-008) Quando uma relação causal é proposta, o KG DEVE exigir mechanism+direction+conditions+regime, `posthoc_flag` booleano, `outcome_ref`+`outcome_timestamp` (ou `no_outcome=true`+justificativa), DEVE forçar `posthoc_flag=true` quando `recorded_at` > `outcome_timestamp`, e DEVE rejeitar causal sem esses campos; SIMILAR_A por juízo DEVE carregar `similarity_basis`.
9. (CKG-009) Quando uma escrita permanente é tentada, o KG DEVE aceitá-la (E3) apenas de escritor autorizado/autenticado (falha de auth ⇒ não-autorizado), e NÃO DEVE permitir que o produtor redefina ontologia/taxonomia.
10. (CKG-010) Quando conhecimento formado sem selo é submetido, o KG DEVE rejeitá-lo; objetos canônicos entram só quando `canonical_status` ∈ conjunto admissível do tipo (exclui EMERGENT/CANDIDATE), preservando os estados a partir da admissão.
11. (CKG-011) Quando um consumidor consulta o KG, o KG DEVE responder read-only; para a EVIDÊNCIA DEVE reconstruir a cadeia COMPLETA; para hipótese oferece trace best-effort [PROPOSTA]; NÃO DEVE alterar estado na consulta.
12. (CKG-012) Quando um nó/relação transita (SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED) ou é atualizado, o KG DEVE representar por novo registro com `expected_version` coincidente (sem FORK) preservando o histórico, e NÃO DEVE remover nem mutar a versão anterior.
13. (CKG-013) Quando duas relações contraditórias coincidem no escopo e validade, o KG DEVE detectar e registrar a colisão preservando ambas, e NÃO DEVE sobrescrever/apagar uma em silêncio.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec REFERENCIA a regra-fonte (D2) por ID e acrescenta só QUANDO/ENTÃO/VERIFICADO POR. D = determinístico; C =
> constitutivo (é o gate); H = híbrido (juízo + gate de saída + bounded loop). Escrita permanente = **E3** (atomic-spec
> §10.2); consulta = E1; guard confiança×convicção = **E3**.

### D3.1 — Vocabulário unificado de `rejected_reason`

> Códigos padronizados; subcódigos especializam um código-pai. **Convenção pai/sub:** o gate PODE retornar o código-pai
> OU um subcódigo mais específico — ambos são válidos e equivalentes para efeito de rejeição (ex.: T01 usa
> `ORIGINA_ICT_FORBIDDEN`; CKG-001/ADV-17 usam `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`; ambos ∈ `ONTOLOGY_INTEGRITY_VIOLATION`).
> **Todo código usado em qualquer BASpec/T/ADV consta desta tabela (m-04).**

| Código-pai | Subcódigos | BASpec/uso |
|---|---|---|
| `ONTOLOGY_INTEGRITY_VIOLATION` | `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`, `ORIGINA_ICT_FORBIDDEN`, `RELATION_TYPE_INVALID`, `SIMILAR_A_TYPE_MISMATCH` | CKG-001/003; T01/T03; ADV-12/17 |
| `OBSERVATION_IS_NOT_EVIDENCE` | — | CKG-002; T02; ADV-11 |
| `FORBIDDEN_CANONICAL_TRANSITION` | — | CKG-002; T09; ADV-11 |
| `PROVENANCE_MISSING` | `COMPUTED_BY_MISSING` | CKG-005; T14; ADV-06 |
| `CAUSAL_FIELDS_MISSING` | `POSTHOC_FLAG_REQUIRED`, `OUTCOME_REF_MISSING` | CKG-008; T07/T16; ADV-04 |
| `CONFIDENCE_IS_NOT_CONVICTION` | `EDGE_TO_CONVICTION_FORBIDDEN` | CKG-007; T06; ADV-03/05 |
| `WRITE_UNAUTHORIZED` | `AUTH_UNAVAILABLE`, `ONTOLOGY_REDEFINITION_FORBIDDEN` | CKG-009; T08; ADV-07 |
| `IMMUTABILITY_VIOLATION` | `PHYSICAL_DELETE_FORBIDDEN`, `RECORD_UPDATE_FORBIDDEN`, `VERSION_FORK_FORBIDDEN`, `EXPECTED_VERSION_MISMATCH` | CKG-006/012; T05/T13; ADV-01/13/15/19 |
| `INVALID_TIME_WINDOW` | — | CKG-004; T04; ADV-13 |
| `ADMISSION_REJECTED` | `FORMED_WITHOUT_SEAL`, `CANONICAL_STATUS_NOT_ADMISSIBLE` | CKG-010; T09; ADV-21 |
| `LINEAGE_INCOMPLETE` | `DERIVA_DE_EDGE_MISSING`, `LINEAGE_CYCLE` | CKG-003/011; ADV-16/20 |
| `SCOPE_OR_OPEN_DECISION_VIOLATION` | `OUT_OF_SCOPE_FORMATION`, `OPEN_DECISION_H001`, `OUT_OF_SCOPE_OR_OPEN_DECISION` | fronteiras; ADV-08/09/10 |

### BASpec-CKG-001 — Ontologia enxuta + matriz de integridade (ver RULE-CKG-001)
```
BASpec-CKG-001:
  QUANDO:       Um nó/relação é submetido para escrita
  ENTÃO:        Aplica RULE-CKG-001 — escreve só se tipo ∈ ontologia ∧ matriz §D2.1 satisfeita (incl. regra de nó
                `hypothesis.school ≠ ICT` e HERDA.pai=PRIMARY); violação rejeitada (fail-closed). Espelha vínculos criados
                pelos agentes; não decide autoridade (CC-01)
  PORQUE:       Sem gramática enxuta + integridade, a memória permanente acumula conhecimento incoerente (research.md §8 R-8)
  REFERÊNCIA:   RULE-CKG-001; §D2.1; INV-02; RULE-HH-003/004 (SPEC-001 l.104/108)
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico (tipo ∈ catálogo ∧ par origem/destino ∈ matriz ∧ direção/simetria ∧ hypothesis.school≠ICT ∧ HERDA.pai=PRIMARY)
    GATE DE SAÍDA: verificação da matriz §D2.1 + regras de nó
    CRITÉRIO 4Es: Conformidade > Eficácia — coerência da ontologia é inviolável
  VERIFICADO POR:
    DADO        um `hypothesis` cujo `school` derivado do produtor == ICT
    QUANDO      o gate de integridade roda
    ENTÃO       escrita rejeitada; nada persistido (contraste positivo: HERDA SMC-SUB → Elliott-PRIMARY é VÁLIDA — T15)
    VERIFICAÇÃO written == false; rejected_reason == "HYPOTHESIS_SCHOOL_ICT_FORBIDDEN" (∈ ONTOLOGY_INTEGRITY_VIOLATION)
```

### BASpec-CKG-002 — Entidade por referência ao canônico (ver RULE-CKG-002)
```
BASpec-CKG-002:
  QUANDO:       Um nó corresponde a objeto canônico (hypothesis/evidence/conviction) ou é uma observation
  ENTÃO:        Aplica RULE-CKG-002 — referencia por ID+versão, grava `canonical_status` + registro
                `canonical_state_transition` validado contra a tabela do tipo (CHM; CEM sem REFUTED); transição proibida
                (CEM-001 l.473-475) ou reativação de estado terminal é REJEITADA; `observation` não é rotulado `evidence`
  PORQUE:       Redefinir canônico viola CC-02/CONST-01; Status é o único campo mutável (CEM-001 l.264); reativar terminal
                viola a integridade histórica (l.468-475); Observação≠Evidência (INV-06); idioma canônico do objeto (INV-10)
  REFERÊNCIA:   RULE-CKG-002; CC-02; CC-10; CEM-001 l.264/428/468-475/494; INV-06; INV-10
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : referência (canonical_id@version) + snapshot + transição validada contra a tabela do tipo; rótulo validado (INV-06)
    CRITÉRIO 4Es: Eficácia — integridade referencial + preservação de estados + não-reativação de terminal
  VERIFICADO POR:
    DADO        (a) um observation rotulado evidence; (b) uma transição INVALIDATED→ACTIVE de evidence
    QUANDO      o nó/transição é escrito
    ENTÃO       (a) rejeitado (tipos distintos); (b) rejeitada (transição proibida; reativação vetada)
    VERIFICAÇÃO observation_labeled_evidence == false; rejected_reason ∈ {"OBSERVATION_IS_NOT_EVIDENCE","FORBIDDEN_CANONICAL_TRANSITION"}
```

### BASpec-CKG-003 — Relação tipada, direcionada, com proveniência e linhagem acíclica (ver RULE-CKG-003)
```
BASpec-CKG-003:
  QUANDO:       Uma relação entre dois nós é escrita
  ENTÃO:        Aplica RULE-CKG-003 — exige tipo/direção/proveniência; `evidence` DERIVED exige `DERIVA_DE` por ancestral
                (INV-CKG-02); **rejeita aresta DERIVA_DE que feche ciclo — se a ORIGEM já é alcançável a partir do DESTINO
                [M-02]**; SIMILAR_A é simétrica só na consulta; contradição não silenciada (CKG-013)
  PORQUE:       Relação sem tipo/direção/proveniência não é auditável (P13); sem a aresta por ancestral o trace completo da
                Evidência (CKG-011/CEM-001 l.612-614) não seria garantido; linhagem cíclica nunca termina
  REFERÊNCIA:   RULE-CKG-003/005; INV-CKG-02; CEM-001 l.565
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : validação (tipo ∈ catálogo ∧ direção ∧ proveniência ∧ ACICLICIDADE: rejeita se origem alcançável a partir do destino via DERIVA_DE)
    GATE DE SAÍDA: verificação (tipo ∧ direção ∧ proveniência ∧ ¬cria_ciclo)
    CRITÉRIO 4Es: Eficácia — relações auditáveis e navegáveis; linhagem acíclica (trace termina)
  VERIFICADO POR:
    DADO        (a) relação sem tipo do catálogo; (b) aresta DERIVA_DE cuja origem já é alcançável a partir do destino (fecharia ciclo)
    QUANDO      a validação roda
    ENTÃO       (a) rejeitada `RELATION_TYPE_INVALID`; (b) rejeitada `LINEAGE_CYCLE`
    VERIFICAÇÃO relation_written == false; lineage_acyclic == true
```

### BASpec-CKG-004 — Temporalidade bitemporal (ver RULE-CKG-004)
```
BASpec-CKG-004:
  QUANDO:       Um ato AUTORIZADO (CKG-009) determina que a validade de uma relação mudou — nunca invalidação automática/cascata (CEM-001 l.602)
  ENTÃO:        Aplica RULE-CKG-004 — grava NOVO registro de invalidação (`recorded_at`/`valid_to`/`targets_record_id`=R0),
                R0 intacto; rejeita `valid_to < valid_from` (`INVALID_TIME_WINDOW`); validade corrente = projeção derivada;
                consulta responde por valid-time e transaction-time
  PORQUE:       Invalidar por novo registro preserva a reconstrução (INV-07); só ato autorizado respeita "não-cascata" (CEM-001 l.602); janela com fim antes do início é incoerente
  REFERÊNCIA:   RULE-CKG-004/009; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.503
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : novo registro de invalidação (valid_to/recorded_at/targets_record_id); rejeita valid_to<valid_from; estado por projeção; sem mutação
    CRITÉRIO 4Es: Eficácia — nenhuma verdade histórica perdida nem reescrita
  VERIFICADO POR:
    DADO        relação criada em T0 (R0), informação muda em T1; e, à parte, tentativa com valid_to < valid_from
    QUANDO      a atualização é processada
    ENTÃO       R0 intacto; novo registro com valid_to=T1; consulta "em T0" válida, "agora" não; janela inválida rejeitada
    VERIFICAÇÃO existing_record_mutated == false; existing_record_deleted == false; historical_query_consistent == true; invalid_time_window_rejected == true
```

### BASpec-CKG-005 — Proveniência obrigatória CONDICIONAL (ver RULE-CKG-005)
```
BASpec-CKG-005:
  QUANDO:       Qualquer nó/relação é escrito
  ENTÃO:        Aplica RULE-CKG-005 — `computed_by` (produtor autenticado) SEMPRE; `gate_record` só se há gate; `lineage`
                só se derivado (`[]` legítimo para PRIMARY/asset/timeframe/regime/observation); escrita sem a proveniência
                exigível é rejeitada; **`computed_by` (produtor) ≠ `writer_id` (committer) [M-05]**
  PORQUE:       Conhecimento sem origem autenticada não é reconstruível (P13); exigir gate_record/lineage de quem não tem gate/ancestral fabricaria dado (RULE-MET-01) e contrariaria CBP-007
  REFERÊNCIA:   RULE-CKG-005; SPEC-004 RULE-CBP-007 l.543-558/CBP-014 l.311-319; CEM-001 Cap.5
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico — computed_by presente ∧ [gate ⇒ gate_record] ∧ [derivado ⇒ lineage não-vazio]
    GATE DE SAÍDA: verificação da proveniência condicional
    CRITÉRIO 4Es: Conformidade > Eficácia — identidade autenticada inviolável; sem fabricar proveniência (RULE-MET-01)
  VERIFICADO POR:
    DADO        (a) nó PRIMARY sem gate/ancestral, com computed_by; (b) nó sem computed_by
    QUANDO      o gate de escrita roda
    ENTÃO       (a) aceito (lineage=[] legítimo, sem gate_record); (b) rejeitado
    VERIFICAÇÃO case_a_written == true; case_a_lineage_empty_ok == true; case_b_written == false; case_b_reason == "COMPUTED_BY_MISSING"
```

### BASpec-CKG-006 — Imutabilidade / append-only permanente (ver RULE-CKG-006) [INV-CKG-01]
```
BASpec-CKG-006:
  QUANDO:       Uma deleção/mutação de registro é tentada (inclusive disfarçada de "esquecimento")
  ENTÃO:        Aplica RULE-CKG-006 — recusa (fail-closed); "esquecimento" só por novo registro de arquivamento versionado (CKG-012); histórico sempre preservado
  PORQUE:       Memória permanente nunca apaga nem reescreve — quebraria a reconstrução (P13) e INV-07/RULE-BB-004/INV-CBP-01
  REFERÊNCIA:   RULE-CKG-006; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate que proíbe DELETE físico e UPDATE de registro; só novos registros
    GATE DE SAÍDA: verificação (operação ∉ {DELETE, UPDATE de registro} ; histórico preservado)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda/não-reescrita acima de economia de espaço
  VERIFICADO POR:
    DADO        tentativa de deletar/reescrever um registro arquivado
    QUANDO      o gate roda
    ENTÃO       negado (fail-closed); registro íntegro e reconstruível
    VERIFICAÇÃO physical_delete == false; record_mutated == false; history_preserved == true
```

### BASpec-CKG-007 — Confiança de relação em namespace próprio (ver RULE-CKG-007)
```
BASpec-CKG-007:
  QUANDO:       Uma confiança de relação é registrada ou lida
  ENTÃO:        Aplica RULE-CKG-007 — `relation_confidence` em namespace próprio; não exposta em campo do objeto de
                convicção (nem em consulta); nenhuma aresta `to_node.node_type == conviction` (direta ou por 2 saltos)
  PORQUE:       INV-04 proíbe CUSTO no Conviction Vector; convicção é computada só pela SPEC-003/CCM-001; condicionar a "custo/confiança" era contornável — proíbe-se por TIPO DE DESTINO
  REFERÊNCIA:   RULE-CKG-007; INV-04 (custo); CCM-001; SPEC-003
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : guard determinístico — confiança em namespace do KG; ¬∃ aresta `to_node==conviction`
    GATE DE SAÍDA: verificação (confiança ∉ campos de convicção ∧ ¬∃ aresta to_node==conviction)
    CRITÉRIO 4Es: Conformidade > Eficácia — INV-04 inviolável
  VERIFICADO POR:
    DADO        (a) CAUSA(calibration_metric→conviction); (b) 2 saltos CAUSA(metric→hypothesis)+CAUSA(hypothesis→conviction); (c) ESTATISTICA_DE(learning→conviction)
    QUANDO      o gate de escrita roda
    ENTÃO       a aresta com destino conviction de cada caso é rejeitada; confiança fica em namespace próprio
    VERIFICAÇÃO confidence_exposed_in_conviction_object == false; any_edge_to_conviction_written == false; two_hop_to_conviction_blocked == true
```
> Que o CÁLCULO de convicção (SPEC-003/CCM-001; J-001 ABERTA) não consuma a confiança é requisito endereçado à SPEC-003 / [DECISÃO NECESSÁRIA] — fora do controle do KG. [INFERÊNCIA]

### BASpec-CKG-008 — Relação causal exige mecanismo+regime+desfecho+pós-hoc (ver RULE-CKG-008)
```
BASpec-CKG-008:
  QUANDO:       Um juízo propõe uma relação CAUSA ou SIMILAR_A
  ENTÃO:        Aplica RULE-CKG-008 — CAUSA exige mechanism+direction+conditions+regime, `posthoc_flag` booleano,
                `outcome_ref`+`outcome_timestamp` (ou `no_outcome=true`+justificativa) [M-04]; força `posthoc_flag=true`
                quando `recorded_at` > `outcome_timestamp`; faltando qualquer campo rejeita. SIMILAR_A por juízo exige
                `similarity_basis`. Gate verifica PRESENÇA e a regra de carimbo, não veracidade (ENF-03)
  PORQUE:       Correlação não é causalidade (CAU-01); regime muda a relação (CAU-02); explicação pós-resultado é viés se não marcada (CAU-03); sem desfecho referenciado o marcador pós-hoc era contornável
  REFERÊNCIA:   RULE-CKG-008; RULE-CAU-01/02/03
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : juízo (apoio semântico) PROPÕE; gate determinístico verifica presença dos campos e a regra temporal
    BOUNDED LOOP: nº máx. de tentativas por par de nós; sem retry infinito (CAUSA e SIMILAR_A)
    GATE DE SAÍDA: verificação (CAUSA ⇒ mechanism ∧ direction ∧ conditions ∧ regime ∧ posthoc_flag ∧ (outcome_ref+outcome_timestamp ∨ no_outcome) ∧ [recorded_at>outcome_timestamp ⇒ posthoc_flag==true]; SIMILAR_A ⇒ similarity_basis)
    CRITÉRIO 4Es: Eficácia (causalidade válida) > Eficiência; LLM é detector, nunca gate (ENF-03)
  VERIFICADO POR:
    DADO        (a) CAUSA sem mechanism/regime; (b) CAUSA com recorded_at > outcome_timestamp e posthoc_flag=false; (c) CAUSA sem outcome_ref e sem no_outcome
    QUANDO      o gate de saída roda
    ENTÃO       (a) `CAUSAL_FIELDS_MISSING`; (b) `POSTHOC_FLAG_REQUIRED`; (c) `OUTCOME_REF_MISSING`
    VERIFICAÇÃO causal_written == false; posthoc_rule_enforced == true; outcome_ref_required == true
```

### BASpec-CKG-009 — Governança de escrita E3 (ver RULE-CKG-009) [E3]
```
BASpec-CKG-009:
  QUANDO:       Uma escrita permanente é tentada
  ENTÃO:        Aplica RULE-CKG-009 — (E3, fail-closed) aceita só de escritor AUTORIZADO com identidade AUTENTICADA pelo
                runtime (reusa SPEC-004); falha de auth ⇒ não-autorizado; produtor registra mas NÃO redefine ontologia/taxonomia
  PORQUE:       Escrita permanente é commit crítico/irreversível (E3 — atomic-spec §10.2); autorização não depende do payload e não falha-aberto
  REFERÊNCIA:   RULE-CKG-009; SAS-001 §6.12 (escopo Structural Agent; extensão = [INFERÊNCIA]); SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate E3 de autorização por identidade autenticada + escopo (registrar ≠ redefinir ontologia); LLM não é gate
    GATE DE SAÍDA: verificação (escritor ∈ autorizados ∧ auth OK ∧ operação ∉ {redefinir ontologia}); auth indisponível ⇒ DENY
    CRITÉRIO 4Es: Conformidade > Eficácia — escrita só sob autorização é inviolável (ENF-04)
  VERIFICADO POR:
    DADO        uma escrita cuja verificação de identidade da SPEC-004 está indisponível/falha
    QUANDO      o gate E3 roda
    ENTÃO       negada (fail-closed; tratada como não-autorizada); falso-DENY amostrado (ENF-07)
    VERIFICAÇÃO write_allowed == false; fail_closed == true; treated_as_unauthorized == true
```

### BASpec-CKG-010 — Fronteira de entrada (ver RULE-CKG-010)
```
BASpec-CKG-010:
  QUANDO:       Conhecimento é submetido ao KG
  ENTÃO:        Aplica RULE-CKG-010 — admite (a) canônicos cujo `canonical_status` ∈ conjunto admissível do tipo (exclui
                EMERGENT/CANDIDATE), gravando `canonical_status`+transições (preserva estados A PARTIR DA ADMISSÃO — M-01),
                e (b) formado com selo SPEC-007; formado sem selo rejeitado; o KG não forma/retrieval
  PORQUE:       "Documento recuperado ≠ validado ≠ publicado"; formação é SPEC-007; o canonical_ref@version sozinho não carrega Status (CEM-001 l.264) — exige canonical_status+transições
  REFERÊNCIA:   RULE-CKG-010; ROADMAP §6/§7; CEM-001 l.258-262/l.264/l.494; CCM-001 l.58/78
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : (b) gate (selo SPEC-007 presente); (a) gate POR TIPO (`canonical_status` ∈ conjunto admissível) — ambos verificáveis, fail-closed
    GATE DE SAÍDA: verificação (selo presente) / (canonical_status ∈ conjunto admissível do tipo)
    CRITÉRIO 4Es: Conformidade > Eficácia — não contaminar com não-validado; não perder estado canônico (dos admitidos)
  VERIFICADO POR:
    DADO        (a) conhecimento formado SEM selo; (b) hypothesis com canonical_status=EMERGENT (ainda trabalho)
    QUANDO      o gate de fronteira roda
    ENTÃO       (a) rejeitado `FORMED_WITHOUT_SEAL`; (b) rejeitada `CANONICAL_STATUS_NOT_ADMISSIBLE`
    VERIFICAÇÃO formed_without_seal_accepted == false; emergent_hypothesis_admitted == false
```
> **Produtor/gatilho de promoção = [DECISÃO NECESSÁRIA]** (a SPEC-005 não escreve no KG — plan l.971; atribuir à SPEC-018/K-001 (ABERTA) é proposta a Andraus, não homologada — distinto do critério de ESTADO, que é verificável). `PENDING_ANCESTOR` é estado de BUFFER de admissão, não registro do KG (durabilidade = H-001 ABERTA). [PROPOSTA]

### BASpec-CKG-011 — Consulta read-only + Trace completo da Evidência (ver RULE-CKG-011)
```
BASpec-CKG-011:
  QUANDO:       Um consumidor consulta o KG ou pede a reconstrução da cadeia cognitiva de uma EVIDÊNCIA
  ENTÃO:        Aplica RULE-CKG-011 — responde read-only; para EVIDÊNCIA retorna a cadeia COMPLETA (fecho transitivo de
                `DERIVA_DE`; garantida por INV-CKG-02; inclui ancestrais SUPERSEDED/ARCHIVED — CEM-001 l.602); **o trace de
                HIPÓTESE (ORIGINA/HERDA/DEPENDE_DE) é best-effort [PROPOSTA], sem alegação de completude [M-03]**; não altera estado
  PORQUE:       Reconstrução completa da Evidência é responsabilidade canônica (CEM-001 l.562-565/l.699); consulta não muta
  REFERÊNCIA:   RULE-CKG-011; INV-CKG-02; CEM-001 l.608-615/l.612-614/l.602; SAS-001 §6.12
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : travessia determinística de `DERIVA_DE` (evidence) até o fecho transitivo, inclui SUPERSEDED/ARCHIVED; hipótese = best-effort; read-only
    CRITÉRIO 4Es: Eficácia (reconstrução completa da Evidência) > Eficiência (eficiência de consulta ampla = H-001)
  VERIFICADO POR:
    DADO        Evidence-E deriva de D; D de C; C de A e B (3 saltos), com C em SUPERSEDED
    QUANDO      pede-se Trace Reconstruction de Evidence-E
    ENTÃO       retorna o fecho completo [A,B,C,D] (C permanece mesmo SUPERSEDED); nenhum estado alterado
    VERIFICAÇÃO trace == ["A","B","C","D"]; trace_complete == true; superseded_ancestor_retained == true; state_mutated_by_query == false
```

### BASpec-CKG-012 — Lifecycle do nó/relação (ver RULE-CKG-012)
```
BASpec-CKG-012:
  QUANDO:       Um nó/relação é substituído, invalidado no tempo, rebaixado, ou atualizado
  ENTÃO:        Aplica RULE-CKG-012 — grava NOVO registro: SUPERSEDED (sucessora com `supersedes`); INVALIDATED_IN_TIME
                (`valid_to` sem sucessora); ARCHIVED (`relevance` sob gate E3). Atualização exige `expected_version`
                coincidente (sem FORK — `VERSION_FORK_FORBIDDEN`/`EXPECTED_VERSION_MISMATCH`); estado = projeção derivada; nada removido/mutado
  PORQUE:       Conhecimento permanente opera por lifecycle versionado, não por deleção/mutação (INV-07; INV-CBP-01); sem ordem total não há estado inequívoco
  REFERÊNCIA:   RULE-CKG-012; CHM-001; INV-07; SPEC-004 INV-CBP-01 / RULE-CBP-004 l.239-246
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : transições append-only (novo registro aponta p/ anterior por supersedes; compare-and-commit); estado por projeção
    CRITÉRIO 4Es: Eficácia — reconstrução íntegra do histórico
  VERIFICADO POR:
    DADO        um nó ACTIVE_KNOWLEDGE cujo conteúdo é corrigido; e uma 2ª sucessora da mesma versão (fork)
    QUANDO      a correção/fork roda
    ENTÃO       nova versão com supersedes→anterior (anterior íntegra); a 2ª sucessora é negada (sem fork)
    VERIFICAÇÃO old_version_preserved == true; old_version_mutated == false; supersedes_link_present == true; version_fork == false
```

### BASpec-CKG-013 — Colisão de relações (ver RULE-CKG-013)
```
BASpec-CKG-013:
  QUANDO:       Duas relações satisfazem as 4 condições de colisão (§D2.2)
  ENTÃO:        Aplica RULE-CKG-013 — DETECTA e grava `collision_record` com identidade/proveniência próprias
                (`collision_id`/`version`/`computed_by`=`writer_id`=serviço do KG/`recorded_at`; E3) referenciando ambas
                (preservadas); não sobrescreve; relações fora das 4 condições não geram colisão; resolução = SPEC-007/SPEC-018/governança
  PORQUE:       Preservar a contradição auditável respeita INV-07; resolver em silêncio perderia conhecimento (viés de confirmação); escopo evita falso-positivo
  REFERÊNCIA:   RULE-CKG-013; §D2.2; INV-07; fronteira SPEC-007/SPEC-018
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : detecção determinística (par ∈ §D2.2 ∧ escopo_do_par ∧ overlap(valid) ∧ ¬superseded(ambas)) ⇒ grava collision_record; proíbe sobrescrita silenciosa
    GATE DE SAÍDA: verificação (4 condições ⇒ collision_record com collision_id/computed_by/writer_id ∧ ambas preservadas; senão sem colisão)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda de conhecimento e auditabilidade da contradição
  VERIFICADO POR:
    DADO        CONFIRMA(A→B) vigente e REFUTA(A→B) nova com validade sobreposta (mesmos A,B)
    QUANDO      a escrita roda
    ENTÃO       ambas preservadas; collision_record gravado; nenhuma apagada; resolução não decidida pelo KG
    VERIFICAÇÃO both_relations_present == true; collision_logged == true; silent_overwrite == false
```

---

## D4 — Algoritmo

Mecânicas determinísticas (a lógica, não a tecnologia; mecanismo físico = **H-001 ABERTA**). Referenciam as regras D2.

- **Integridade (CKG-001):** aceitar sse tipo ∈ catálogo ∧ (origem.node_type, destino.node_type) ∈ matriz[tipo] ∧ direção/simetria conformes (§D2.1). Nó hypothesis: `school`/`hierarchy_role` DERIVADOS do `producer_id`/`producer_type` do canônico (structure: do produtor que a publica — M-06); `aceitar sse ¬(hypothesis ∧ school=ICT)`; `HERDA ⇒ pai.hierarchy_role=PRIMARY`.
- **Validade bitemporal (CKG-004):** criação grava `R0{creation, valid_from, recorded_at}`; mudança grava `R1{invalidation, targets_record_id=R0, valid_to, recorded_at}`; R0 nunca mutado. Rejeita `valid_to < valid_from`. `valid_to=null`≡+∞. valid-time: `válida_em(T) = ∃ creation com valid_from≤T ∧ ¬∃ invalidation aplicável com valid_to≤T`; transaction-time: conjunto com `recorded_at≤R`.
- **Imutabilidade / estado derivado + PRECEDÊNCIA (CKG-006/012):** `DELETE/UPDATE de registro ⇒ negado`. Estado(x) por precedência: (1) SUPERSEDED sse ∃ sucessora `supersedes=x`; senão (2) INVALIDATED_IN_TIME sse ∃ invalidation `targets_record_id=x` sem sucessora; senão (3) ARCHIVED sse ∃ archival vigente; senão (4) ACTIVE_KNOWLEDGE.
- **Trace Reconstruction (CKG-011):** `trace(x)` = fecho transitivo de `DERIVA_DE` a partir de x para **evidence** — COMPLETO (garantido por INV-CKG-02; ignora validade, inclui SUPERSEDED/ARCHIVED — CEM-001 l.602); ordem = ancestralidade (CEM-001 l.567-577). **Para hipótese** (ORIGINA/HERDA/DEPENDE_DE) = best-effort [PROPOSTA], sem garantia de completude [M-03]. Completude (Evidência) é obrigação; eficiência de travessia ampla = H-001.
- **Versionamento/dedupe (CKG-012):** atualização aceita sse `supersedes`=última ∧ `version`=anterior+1 ∧ `expected_version`=corrente (compare-and-commit — SPEC-004 CBP-004 l.239-246); ausência de expected_version na atualização ⇒ `EXPECTED_VERSION_MISMATCH`; 2ª sucessora da mesma versão ⇒ `VERSION_FORK_FORBIDDEN`. **Chave natural (não-canônico):** `(node_type, natural_key)` para asset/timeframe/regime/narrative/observation/learning/**structure/mission/calibration_metric** (M-06 — lista completa); canônico: `(node_type, canonical_ref)`; relação: `(relation_type, from_node, to_node, valid_from)`. Reescrita idêntica = no-op; divergente sem supersedes ⇒ DENY.
- **Gate causal (CKG-008):** `CAUSA ⇒ {mechanism, direction, conditions, regime} ≠ ∅ ∧ posthoc_flag booleano ∧ (outcome_ref ∧ outcome_timestamp) ∨ no_outcome=true+justificativa ∧ [recorded_at>outcome_timestamp ⇒ posthoc_flag=true]`; `SIMILAR_A ⇒ similarity_basis`. Juízo bounded. Verifica PRESENÇA e carimbo, não veracidade (ENF-03).
- **Confiança (CKG-007):** `confidence ∈ escala própria (PARÂMETRO a calibrar — INDETERMINADO)`; proibido em campo de convicção e `¬∃ aresta e : e.to_node.node_type==conviction` (direta ou multi-salto; INV-04).
- **Colisão (CKG-013/§D2.2):** `colide(r1,r2) sse (r1.type,r2.type)∈§D2.2 ∧ escopo_do_par ∧ overlap([r1.valid_from,r1.valid_to),[r2.valid_from,r2.valid_to)) ∧ ¬superseded(ambas)`, com `escopo_do_par` = (CONFIRMA×REFUTA: from/to iguais) ∨ (INVALIDA×alvo: `r1.target_relation_id==r2.relation_id`). Se colide ⇒ grava collision_record (E3); senão não.

Nenhuma fórmula computa convicção; nenhum limiar de convicção nem escala numérica de confiança fixado (RULE-MET-01). [FONTE: atomic-spec §2; CEM-001 Cap.5; SPEC-004 INV-CBP-01; research.md §3.1/§4]

---

## D5 — Máquina de estados (lifecycle do nó/relação — estado = projeção derivada)

> **Fronteira (CC-02/CC-10):** lifecycle do **conhecimento no KG permanente**, separado da máquina da **hipótese**
> (CHM-001) e do **estado no Blackboard** (SPEC-004). `knowledge_state` NÃO é campo mutado — é PROJEÇÃO DERIVADA (espelha
> SPEC-004 INV-CBP-01). Os estados do KG são HOMÔNIMOS mas ≠ estados canônicos: SUPERSEDED/ARCHIVED/**REFUTED** são do
> **CHM** (hipótese); a Evidência tem ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED, **sem REFUTED** (CEM-001 l.258-262 — m-03).
> O Status canônico é rastreado à parte, em `canonical_status` + `canonical_state_transition` (CKG-002/010) — CC-10.

| Estado (derivado) | Definição (projeção) | Origem |
|---|---|---|
| ACTIVE_KNOWLEDGE | criação vigente, sem sucessora/invalidação/arquivamento aplicável | criação |
| SUPERSEDED | existe sucessora com `supersedes` (conteúdo corrigido) | CKG-012 |
| INVALIDATED_IN_TIME | invalidação com `valid_to` SEM sucessora (o mundo mudou) | CKG-004/012 |
| ARCHIVED | arquivamento vigente (`relevance` sob gate E3) | CKG-012 |

> **Transitórios (NÃO persistidos):** `CANDIDATE_WRITE` (sob gates), `REJECTED` (falhou), `PENDING_ANCESTOR` (aguarda
> ancestral) são do fluxo/buffer de admissão — nada persistido quando rejeitado. Correção/reativação = NOVO registro.
> Mecanismo físico = **INDETERMINADO (H-001 ABERTA)**; Opção B (banco de grafos) registrada e ADIADA (research.md §3.5).
> [FONTE: RULE-CKG-006/012; SPEC-004 INV-CBP-01; DHR-SPEC006-001 §3]

---

## D6 — Protocolo de escrita/consulta (sobre conhecimento publicado)

- Conhecimento entra por **duas fontes sob a mesma governança (CKG-009/010)**: (a) canônicos via ciclo de vida; (b) formado com selo SPEC-007 (contrato = [DECISÃO NECESSÁRIA]).
- O **produtor** registra relações mas não redefine ontologia (SAS-001 §6.12 — **FATO NORMATIVO só p/ Structural Agent; extensão = [INFERÊNCIA]** — m-02); escrita E3 sob identidade autenticada (SPEC-004); falha de auth ⇒ não-autorizado.

> **Capacidade × papel [PROPOSTA], moldada na SPEC-004 l.329-348.** **QUEM pode o quê** proposto aqui; a **allowlist
> concreta** de escritores = **[DECISÃO NECESSÁRIA]** (runtime; K-001/SPEC-018). **Identidade [M-05]:** `computed_by` = o
> PRODUTOR autenticado (quem propõe); `writer_id` = o COMMITTER autenticado (runtime; ou serviço do KG p/
> collision/transição) — valores DISTINTOS; nenhum depende do payload (CBP-014).
>
> | Capacidade | Agente (produtor) | Runtime | Serviço do KG | Governança (Andraus) |
> |---|---|---|---|---|
> | Propor nó/relação (= `computed_by`) | PERMIT (proposta, identidade autenticada) | — | — | — |
> | Commit permanente E3 (= `writer_id`) | **DENY** | PERMIT (autentica produtor; executa commit) | — | — |
> | Escrever `collision_record`/`canonical_state_transition`/`archival` (`computed_by`=`writer_id`=serviço) | **DENY** | PERMIT (executa) | PERMIT (DETECTA/compõe sob capability explícita) | — |
> | Redefinir ONTOLOGIA/taxonomia | **DENY** (SAS-001 §6.12) | **DENY** | **DENY** | PERMIT (spec-time SPEC-019; runtime K-001 [DECISÃO NECESSÁRIA]) |
> | Consultar (read-only) | PERMIT | PERMIT | PERMIT | PERMIT |
>
> `computed_by` e `writer_id` sempre AUTENTICADOS; nenhuma capacidade depende do payload. [PROPOSTA]

- **[INFERÊNCIA]/[DECISÃO NECESSÁRIA]** — eventual **consumo** de eventos pelo KG serve só de **gatilho** para avaliação autorizada (CKG-009), **nunca** invalidação automática (CEM-001 l.602). `Evidence.Invalidated` é canônico (CEM-001 l.600/722) e a SPEC-005 o **transporta** (plan l.88/l.859); o **consumidor/contrato de consumo pelo KG** = **[DECISÃO NECESSÁRIA]**. **Emissão pelo KG NÃO é afirmada** (SPEC-005 fonta do log do Blackboard; emissão = [DECISÃO NECESSÁRIA]).
- A **consulta** é read-only e opcional/não-bloqueante (SAS-001 §6.12/EC-COG-003).

### Sequência de escrita (um nó/relação)
1. **Submissão** (canônico via ciclo de vida, ou formado via SPEC-007).
2. **Fronteira (CKG-010):** canônico só se `canonical_status` ∈ conjunto admissível do tipo (exclui EMERGENT/CANDIDATE); formado exige selo ⇒ senão `REJECTED`.
3. **Autorização E3 (CKG-009):** escritor autorizado + identidade autenticada; produtor não redefine ontologia ⇒ senão `REJECTED`.
4. **Ontologia/integridade (CKG-001):** tipo ∈ catálogo ∧ matriz §D2.1 ⇒ senão `REJECTED`.
5. **Proveniência (CKG-005):** `computed_by` (produtor) presente ∧ [gate ⇒ gate_record] ∧ [derivado ⇒ lineage] ⇒ senão `REJECTED`.
6. **Causalidade (CKG-008, se CAUSA):** mechanism+direction+conditions+regime+posthoc_flag+outcome(ou no_outcome) ⇒ senão `REJECTED`.
7. **Colisão (CKG-013):** se forma par contraditório no escopo §D2.2 com validade sobreposta e ambas não-SUPERSEDED, grava `collision_record` (não sobrescreve).
8. **Escrita append-only (CKG-006/012):** novo registro; substituição ⇒ sucessora com `supersedes`+`expected_version` (sem fork); DELETE/UPDATE proibido.
9. **Temporalidade (CKG-004):** relações carregam `valid_from`/`valid_to`/`recorded_at`; invalidação é ato AUTORIZADO (novo registro), não cascata (CEM-001 l.602).

> **Nota de fronteira:** memória de **trabalho**/versão = SPEC-004; **notificação** = SPEC-005; **formação** = SPEC-007.
> A SPEC-006 só **preserva, relaciona e consulta** o conhecimento permanente. [FONTE: ROADMAP §5/§6/§7]

---

## D7 — Cenários de Teste (16 — T01..T16)

### Cenário-CKG-T01 — ORIGINA com origem ICT → rejeição (matriz §D2.1 / CKG-001)
```
DADO        uma relação ORIGINA cuja origem tem `school` derivado do produtor = ICT (ICT nunca origina — INV-02/RULE-HH-004; SPEC-001 l.108/l.515-520)
QUANDO      o gate de integridade (§D2.1) roda
ENTÃO       escrita rejeitada; nada persistido
VERIFICAÇÃO written == false; rejected_reason == "ORIGINA_ICT_FORBIDDEN" (∈ ONTOLOGY_INTEGRITY_VIOLATION — §D3.1)
```

### Cenário-CKG-T15 — HERDA SMC-SUB → Elliott-PRIMARY (positivo; entre escolas é VÁLIDO)
```
DADO        hipótese SUB (produtor SMC, SUB) com parent_id → hipótese PAI (produtor Elliott, PRIMARY)
QUANDO      a relação HERDA é escrita
ENTÃO       aceita (entre escolas permitido — RULE-HH-003; HERDA valida só pai=PRIMARY); nada rejeitado
VERIFICAÇÃO relation_written == true; cross_school_herda_allowed == true; parent_hierarchy_role == "PRIMARY"
```

### Cenário-CKG-T02 — observation rotulada evidence → rejeição (CKG-002/INV-06)
```
DADO        um nó observation sendo rotulado evidence
QUANDO      o nó é escrito
ENTÃO       rejeitado; tipos distintos preservados
VERIFICAÇÃO observation_labeled_evidence == false; rejected_reason == "OBSERVATION_IS_NOT_EVIDENCE"
```

### Cenário-CKG-T03 — Relação sem tipo/direção → rejeição (CKG-003)
```
DADO        uma relação sem tipo do catálogo (ou sem direção)
QUANDO      a validação roda
ENTÃO       relação rejeitada; nada escrito
VERIFICAÇÃO relation_written == false; rejected_reason == "RELATION_TYPE_INVALID"
```

### Cenário-CKG-T04 — Validade muda por NOVO registro; janela inválida rejeitada (CKG-004)
```
DADO        relação criada em T0 (R0), informação muda em T1; e, à parte, tentativa com valid_to < valid_from
QUANDO      a atualização é processada
ENTÃO       R0 intacto; novo registro (valid_to=T1); consulta "em T0" válida, "agora" não; janela inválida rejeitada
VERIFICAÇÃO existing_record_mutated == false; historical_query_consistent == true; invalid_time_window_rejected == true; rejected_reason == "INVALID_TIME_WINDOW"
```

### Cenário-CKG-T05 — Deleção/mutação proibida (CKG-006)
```
DADO        tentativa de deletar/reescrever um registro arquivado
QUANDO      o gate de imutabilidade roda
ENTÃO       negado (fail-closed); registro íntegro e reconstruível
VERIFICAÇÃO physical_delete == false; record_mutated == false; history_preserved == true
```

### Cenário-CKG-T06 — Nenhuma aresta to_node==conviction (incl. 2 saltos) (CKG-007)
```
DADO        (a) CAUSA(calibration_metric→conviction); (b) 2 saltos CAUSA(metric→hypothesis)+CAUSA(hypothesis→conviction); e confiança registrada
QUANDO      o gate de escrita roda
ENTÃO       toda aresta com destino conviction rejeitada (direta e no 2º salto); confiança em namespace próprio
VERIFICAÇÃO confidence_exposed_in_conviction_object == false; any_edge_to_conviction_written == false; two_hop_to_conviction_blocked == true
```

### Cenário-CKG-T07 — Causal sem mecanismo/regime → rejeição (CKG-008)
```
DADO        CAUSA proposta sem mechanism/regime (só correlação)
QUANDO      o gate de saída roda
ENTÃO       rejeitada; exige mechanism+direction+conditions+regime
VERIFICAÇÃO causal_written == false; rejected_reason == "CAUSAL_FIELDS_MISSING"
```

### Cenário-CKG-T08 — Auth da SPEC-004 indisponível → escrita negada (CKG-009) [E3]
```
DADO        escrita cuja verificação de identidade da SPEC-004 está indisponível/falha
QUANDO      o gate E3 roda
ENTÃO       negada (fail-closed; tratada como não-autorizada)
VERIFICAÇÃO write_allowed == false; fail_closed == true; treated_as_unauthorized == true
```

### Cenário-CKG-T09 — Formado sem selo rejeitado; canônico preserva estados por transição (CKG-010/002)
```
DADO        padrão formado SEM selo SPEC-007; e, à parte, uma hypothesis que transita para REFUTED (∈ conjunto admissível)
QUANDO      o gate de fronteira roda
ENTÃO       formado sem selo rejeitado; hypothesis REFUTED admitida com registro canonical_state_transition (estado preservado)
VERIFICAÇÃO formed_without_seal_accepted == false; canonical_status_in_admissible_set == true; canonical_state_transition_recorded == true
```

### Cenário-CKG-T10 — Trace Reconstruction completa da Evidência (3 saltos) (CKG-011)
```
DADO        E deriva de D; D de C; C de A e B (3 saltos)
QUANDO      pede-se Trace Reconstruction de E
ENTÃO       retorna o fecho completo [A,B,C,D]; nenhum estado alterado
VERIFICAÇÃO trace == ["A","B","C","D"]; trace_complete == true; state_mutated_by_query == false
```

### Cenário-CKG-T11 — Colisão de relações registrada (CKG-013)
```
DADO        CONFIRMA(A→B) vigente (não-SUPERSEDED) e REFUTA(A→B) nova com mesmos (A,B) e validade sobreposta (§D2.2)
QUANDO      a escrita roda
ENTÃO       ambas preservadas; collision_record (com collision_id/computed_by=writer_id=serviço do KG); resolução não decidida pelo KG
VERIFICAÇÃO both_relations_present == true; collision_logged == true; collision_record_has_identity == true; silent_overwrite == false
```

### Cenário-CKG-T12 — Nó PRIMARY sem gate/ancestral com proveniência condicional válida (CKG-005)
```
DADO        hypothesis PRIMARY (sem gate, Lineage vazio) com computed_by presente, sem gate_record, lineage=[]
QUANDO      a escrita roda
ENTÃO       nó escrito como ACTIVE_KNOWLEDGE (lineage=[] legítimo; gate_record ausente OK — espelha CBP-007)
VERIFICAÇÃO node_written == true; computed_by_present == true; lineage_empty_ok == true; knowledge_state == "ACTIVE_KNOWLEDGE"
```

### Cenário-CKG-T13 — Correção = nova versão (supersessão por novo registro) (CKG-012)
```
DADO        um nó ACTIVE_KNOWLEDGE cujo conteúdo é corrigido, com expected_version coincidente
QUANDO      a correção roda
ENTÃO       nova versão com supersedes→anterior; anterior íntegra/não-mutada; SUPERSEDED é estado derivado
VERIFICAÇÃO old_version_preserved == true; old_version_mutated == false; supersedes_link_present == true
```

### Cenário-CKG-T14 — Escrita sem computed_by → rejeição (CKG-005)
```
DADO        um nó submetido SEM computed_by (identidade autenticada do produtor ausente)
QUANDO      o gate de proveniência roda
ENTÃO       escrita rejeitada; nada persistido (computed_by sempre obrigatório — CBP-014)
VERIFICAÇÃO written == false; rejected_reason == "COMPUTED_BY_MISSING"
```

### Cenário-CKG-T16 — Marcador pós-hoc determinístico + desfecho obrigatório (CKG-008/M-04)
```
DADO        (a) CAUSA(A→B) com todos os campos e `recorded_at` POSTERIOR ao `outcome_timestamp`, submetida com posthoc_flag=false; (b) CAUSA sem outcome_ref e sem no_outcome
QUANDO      o gate de saída (CKG-008) roda
ENTÃO       (a) rejeitada `POSTHOC_FLAG_REQUIRED` (carimbo posterior exige posthoc_flag=true); (b) rejeitada `OUTCOME_REF_MISSING`
VERIFICAÇÃO causal_written == false; posthoc_rule_enforced == true; outcome_ref_required == true
```

---

## D8 — Rigor adversarial focado (casos de negação nos pontos de risco)

> **21 casos** cobrindo as 13 BASpecs + fronteiras/decisões abertas. Transversal: **fail-closed**, **nunca deletar/mutar**, **mecanismo físico INDETERMINADO (H-001)**. Todo `rejected_reason` consta de §D3.1.

### ADV-CKG-01 — Deleção disfarçada de "esquecimento" (CKG-006)
**DADO:** "esquecer" traduzido em DELETE físico. **QUANDO:** o gate roda. **ENTÃO:** negar; só arquivamento versionado. **PORQUE:** INV-07. **VERIFICAÇÃO:** physical_delete == false.

### ADV-CKG-02 — Sobrescrita silenciosa de relação contraditória (CKG-013)
**DADO:** REFUTA(A→B) sobre CONFIRMA(A→B). **QUANDO:** a escrita roda. **ENTÃO:** registrar colisão; preservar ambas. **PORQUE:** perder a contradição apaga conhecimento. **VERIFICAÇÃO:** silent_overwrite == false; both_relations_present == true.

### ADV-CKG-03 — Confiança retroalimenta o Conviction Vector (CKG-007/INV-04)
**DADO:** expor a confiança no objeto de convicção, somá-la como 9ª dimensão, ou criar aresta `to_node==conviction`. **QUANDO:** a escrita/escopo roda. **ENTÃO:** rejeitar `EDGE_TO_CONVICTION_FORBIDDEN`; namespace próprio. **PORQUE:** INV-04; dimensionalidade=8 (fechada). **VERIFICAÇÃO:** confidence_exposed_in_conviction_object == false; any_edge_to_conviction_written == false.

### ADV-CKG-04 — Causal pós-hoc por correlação, sem desfecho/marcador (CKG-008/RULE-CAU)
**DADO:** CAUSA(A→B) só por co-ocorrência, (a) sem mechanism/regime; (b) com `recorded_at` > `outcome_timestamp` e posthoc_flag=false; (c) sem outcome_ref e sem no_outcome. **QUANDO:** o gate roda. **ENTÃO:** rejeitar `CAUSAL_FIELDS_MISSING`/`POSTHOC_FLAG_REQUIRED`/`OUTCOME_REF_MISSING`. **PORQUE:** correlação não é causalidade; marcador/desfecho omissível seria contornável (M-04). **VERIFICAÇÃO:** causal_written == false; posthoc_rule_enforced == true; outcome_ref_required == true.

### ADV-CKG-05 — Métrica de custo ligada à convicção via nó do KG (INV-04)
**DADO:** `calibration_metric`/custo ligado à convicção via aresta. **QUANDO:** a escrita roda. **ENTÃO:** armazenar a métrica (CEE-001 l.111) ISOLADA; rejeitar `EDGE_TO_CONVICTION_FORBIDDEN`. **PORQUE:** INV-04 — o CUSTO nunca entra no Conviction Vector. **VERIFICAÇÃO:** any_edge_to_conviction_written == false.

### ADV-CKG-06 — Escrita sem proveniência aceita (CKG-005)
**DADO:** nó/relação sem provenance_ref. **QUANDO:** o gate roda. **ENTÃO:** rejeitar `PROVENANCE_MISSING`. **PORQUE:** sem origem não é reconstruível (P13). **VERIFICAÇÃO:** written == false.

### ADV-CKG-07 — Produtor redefine ontologia/taxonomia (CKG-009/SAS-001 §6.12)
**DADO:** produtor autenticado tenta alterar a ontologia global. **QUANDO:** o gate E3 roda. **ENTÃO:** negar `ONTOLOGY_REDEFINITION_FORBIDDEN`; produtor registra, não redefine. **PORQUE:** SAS-001 §6.12 (extensão a outros produtores = [INFERÊNCIA]). **VERIFICAÇÃO:** ontology_redefined_by_producer == false.

### ADV-CKG-08 — KG forma conhecimento / absorve SPEC-007 (CKG-010/fronteira)
**DADO:** tentativa de extração/retrieval/validação no KG. **QUANDO:** o escopo roda. **ENTÃO:** rejeitar `OUT_OF_SCOPE_FORMATION`. **PORQUE:** formação é SPEC-007. **VERIFICAÇÃO:** formation_in_kg == false.

### ADV-CKG-09 — Mecanismo físico fixado por inércia (CONS-01/mandato)
**DADO:** pressão para fixar "grafo real"/escolher engine. **QUANDO:** as decisões rodam. **ENTÃO:** rejeitar `OPEN_DECISION_H001`; mecanismo físico permanece INDETERMINADO; Opção B ADIADA. **PORQUE:** H-001 é de Andraus (CONS-01). **VERIFICAÇÃO:** h001_decided_by_spec == false.

### ADV-CKG-10 — Absorver vizinhos / tocar decisão aberta (fronteiras/CONS-01)
**DADO:** a SPEC-006 virar memória de trabalho (SPEC-004), transporte (SPEC-005), estado por agente (SPEC-009), ciclo P12 (SPEC-018), ou tocar M-001/J-001/N-001/G-001/K-001/C-001/WF-D03. **QUANDO:** o escopo roda. **ENTÃO:** rejeitar `OUT_OF_SCOPE_OR_OPEN_DECISION`; decisões abertas permanecem ABERTAS (Andraus). **PORQUE:** CONS-01; INV-09. **VERIFICAÇÃO:** neighbors_absorbed == false; open_decisions_touched == false.

### ADV-CKG-11 — Nó redefine contrato canônico / transição proibida (CKG-002/CC-02)
**DADO:** nó-hipótese sobrescreve campos/estado do CHM-001, ou transição INVALIDATED→ACTIVE. **QUANDO:** a escrita roda. **ENTÃO:** rejeitar (`FORBIDDEN_CANONICAL_TRANSITION`/redefinição); referencia por id@version, não redefine. **PORQUE:** CC-02/CONST-01; INV-10; CEM-001 l.473-475. **VERIFICAÇÃO:** canonical_contract_redefined == false; forbidden_canonical_transition_rejected == true.

### ADV-CKG-12 — Relação viola a matriz de integridade (CKG-001/003)
**DADO:** ORIGINA com origem ICT, ou SIMILAR_A entre tipos diferentes. **QUANDO:** o gate §D2.1 roda. **ENTÃO:** rejeitar `ONTOLOGY_INTEGRITY_VIOLATION`. **PORQUE:** integridade da ontologia (INV-02; matriz). **VERIFICAÇÃO:** written == false.

### ADV-CKG-13 — Invalidação mutando o registro existente / janela inválida (CKG-004)
**DADO:** `valid_to` escrito SOBRE o registro de criação (mutação), ou `valid_to < valid_from`. **QUANDO:** a invalidação roda. **ENTÃO:** rejeitar; invalidação só por NOVO registro; janela inválida `INVALID_TIME_WINDOW`. **PORQUE:** append-only real (INV-CBP-01). **VERIFICAÇÃO:** existing_record_mutated == false; invalid_time_window_rejected == true.

### ADV-CKG-14 — Trace incompleto ou consulta que muta estado (CKG-011)
**DADO:** reconstrução de EVIDÊNCIA que para no 1º salto, ou consulta que grava. **QUANDO:** a consulta roda. **ENTÃO:** exigir fecho completo da Evidência (obrigação); consulta read-only. **PORQUE:** CEM-001 l.612-614; H-001 não rebaixa a completude. **VERIFICAÇÃO:** trace_complete == true; state_mutated_by_query == false.

### ADV-CKG-15 — Transição remove/reescreve a versão anterior (CKG-012/INV-07)
**DADO:** SUPERSEDED implementado apagando/reescrevendo a versão anterior. **QUANDO:** a transição roda. **ENTÃO:** rejeitar; anterior preservada; estado = projeção derivada. **PORQUE:** INV-07; INV-CBP-01. **VERIFICAÇÃO:** old_version_preserved == true; old_version_mutated == false.

### ADV-CKG-16 — evidence DERIVED sem aresta DERIVA_DE por ancestral (CKG-003/INV-CKG-02)
**DADO:** `evidence` DERIVED com Lineage=[C] admitido sem materializar `DERIVA_DE`→C. **QUANDO:** o gate roda. **ENTÃO:** rejeitar `DERIVA_DE_EDGE_MISSING`; exigir a aresta; manter acíclico. **PORQUE:** sem a aresta o trace completo não é garantido (INV-CKG-02). **VERIFICAÇÃO:** deriva_de_edge_per_ancestor == true; written == false.

### ADV-CKG-17 — hypothesis com school=ICT (CKG-001/INV-02)
**DADO:** um `hypothesis` cujo `school` derivado do produtor == ICT. **QUANDO:** o gate de nó roda. **ENTÃO:** rejeitar `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`; ICT nunca cria hipótese. **PORQUE:** INV-02; RULE-HH-004 (SPEC-001 l.108). **VERIFICAÇÃO:** hypothesis_school_ict_written == false.

### ADV-CKG-18 — colisão falsamente detectada/ignorada; escopo INVALIDA e SUPERSEDED (CKG-013)
**DADO:** (a) A1 CONFIRMA B, A2 REFUTA B (A1≠A2) — não colide; (b) CONFIRMA(A→B)/REFUTA(A→B) com janelas DISJUNTAS — não colide; (c) ambas vigentes com sobreposição — colide; (d) INVALIDA com `target_relation_id==R.relation_id` sobre R não-SUPERSEDED — colide; (e) CONFIRMA(A→B) SUPERSEDED vs REFUTA(A→B) vigente — não colide. **QUANDO:** o detector roda. **ENTÃO:** (a)/(b)/(e) não geram colisão; (c)/(d) geram. **PORQUE:** colisão = par §D2.2 no escopo do par, sobreposição, ambas não-SUPERSEDED. **VERIFICAÇÃO:** collision_logged == [false,false,true,true,false] para (a..e).

### ADV-CKG-19 — FORK de versão / ordem violada (CKG-006/012)
**DADO:** duas sucessoras apontando `supersedes` para a MESMA versão, ou `expected_version` ≠ corrente, ou `version` ≠ anterior+1. **QUANDO:** o gate roda. **ENTÃO:** negar (`VERSION_FORK_FORBIDDEN`/`EXPECTED_VERSION_MISMATCH`); compare-and-commit (CBP-004 l.239-246). **PORQUE:** sem ordem total não há estado inequívoco (INV-07). **VERIFICAÇÃO:** second_successor_written == false; version_fork == false.

### ADV-CKG-20 — ciclo na linhagem DERIVA_DE (CKG-003/INV-CKG-02; M-02)
**DADO:** arestas A DERIVA_DE B e B DERIVA_DE C já gravadas (C ancestral de B ancestral de A); tentativa C DERIVA_DE A — a origem C já é alcançável a partir do destino A (A→B→C), fecharia ciclo. **QUANDO:** o gate de relação roda. **ENTÃO:** rejeitar `LINEAGE_CYCLE`; o grafo permanece ACÍCLICO (o trace sempre termina). **PORQUE:** linhagem cíclica quebra a Trace Reconstruction (INV-CKG-02). **VERIFICAÇÃO:** lineage_cycle_written == false; lineage_acyclic == true.

### ADV-CKG-21 — admissão de canônico em estado NÃO-admissível / sem selo (CKG-010)
**DADO:** (a) `hypothesis` com `canonical_status=EMERGENT`; (b) formado SEM selo SPEC-007. **QUANDO:** o gate de fronteira roda. **ENTÃO:** rejeitar `CANONICAL_STATUS_NOT_ADMISSIBLE` / `FORMED_WITHOUT_SEAL`; só estado admissível entra (exclui EMERGENT/CANDIDATE). **PORQUE:** não contaminar memória permanente com trabalho (CEM-001 l.494; SPEC-004). **VERIFICAÇÃO:** emergent_hypothesis_admitted == false; formed_without_seal_accepted == false.

> **Cobertura:** 21 casos — toda BASpec tem ≥1 negação: CKG-001→ADV-12/17, T01; 002→ADV-11, T02; 003→ADV-12/16/20, T03;
> 004→ADV-13, T04; 005→ADV-06, T14; 006→ADV-01/19, T05; 007→ADV-03/05, T06; 008→ADV-04, T07/T16; 009→ADV-07, T08;
> 010→ADV-08/21, T09; 011→ADV-14, T10; 012→ADV-15/19, T13; 013→ADV-02/18, T11. Fronteiras/decisões abertas: ADV-09/10.
> Mapeiam para EC-CKG-001..006 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada registro DEVE ser reconstruível (P13): tipo, `version`, `supersedes`, `expected_version`, `targets_record_id`
(invalidação/arquivamento), referência canônica (id@version), proveniência CONDICIONAL (CKG-005: `computed_by` sempre;
`gate_record` se gate; `lineage` se derivado), validade (`valid_from`/`valid_to`/`recorded_at`) e `collision_record`
quando houver. A **Trace Reconstruction COMPLETA da EVIDÊNCIA** é capacidade central (CEM-001 l.608-615) — comportamento
verificável (CKG-011); o trace de hipótese é best-effort [PROPOSTA]. Observabilidade agregada = SPEC-040; reconstrução
expandida de trabalho = SPEC-004 — aqui por referência (coerente com D0–D7 e H-001 ABERTA). [FONTE: CONSTITUTION P13;
CEM-001 l.608-615; SPEC-004 replay; H-001 ABERTA]

---

## Contrato do nó/relação — esqueleto [PROPOSTA]

> Produto central. **Referencia** os canônicos por `canonical_ref`; **não** os redefine (CC-02). Mecanismo físico =
> **INDETERMINADO (H-001 ABERTA)**. Todo write é E3.
>
> **Identidade [M-05]:** `computed_by` = identidade AUTENTICADA do PRODUTOR/proponente; `writer_id` = identidade
> AUTENTICADA do COMMITTER (runtime; serviço do KG para collision/transition). São DISTINTOS (não é mais `writer_id ==
> computed_by`); nenhum deriva do payload (CBP-014). `who` (humano-legível, auditoria) pode diferir de `computed_by` mas é
> obrigatório; a autoridade é `computed_by`/`writer_id` autenticados.
>
> **Estado:** `knowledge_state` não é campo persistido — é projeção derivada (D5). Validade/arquivamento valem para NÓ e
> RELAÇÃO. `canonical_status` (snapshot) + `canonical_state_transition` sustentam `canonical_states_preserved` (CKG-010/T09).

### I/O Schema (lógico — referência; não redefine CHM/CEM/CCM)
```json
{
  "node_record": {
    "node_id": "KG-N-2026-10-12-001",
    "record_kind": "creation | invalidation | archival | canonical_state_transition",
    "version": "monotônico; sucessão de CONTEÚDO usa supersedes/version+1/expected_version (CKG-012). Registros invalidation/archival/canonical_state_transition têm sua PRÓPRIA sequência de version e NÃO entram na cadeia supersedes de conteúdo (m-10)",
    "expected_version": "OBRIGATÓRIO na atualização (== versão corrente no commit, senão DENY EXPECTED_VERSION_MISMATCH); criação inicial não exige (CBP-004 l.243-246)",
    "supersedes": "null | KG-N-...-v0 (sucessão de CONTEÚDO ⇒ SUPERSEDED; aponta p/ ÚLTIMA versão; version==anterior+1; sem FORK)",
    "targets_record_id": "null | KG-N-...-R0 (registro que invalidation/archival REFERENCIA — DISTINTO de supersedes; invalidação ⇒ INVALIDATED_IN_TIME)",
    "node_type": "hypothesis | evidence | observation | conviction | narrative | mission | learning | asset | timeframe | regime | structure | calibration_metric",
    "schema_version": "1 (migração de ontologia/schema = [DECISÃO NECESSÁRIA] — CKG-009)",
    "canonical_ref": "CHM-xxxx@v2 | CEM-xxxx@v1 | CCM-xxxx@v1 | null (referência; NÃO redefine)",
    "canonical_status": "snapshot do Status canônico (CEM-001 l.264/428; CHM-001; só se canonical_ref != null); admissível ∈ conjunto do tipo (CKG-010)",
    "natural_key": "identidade de nó NÃO-canônico — asset/timeframe/regime/narrative/observation/learning/structure/mission/calibration_metric (lista completa — M-06); evita colapso quando canonical_ref=null",
    "school": "Elliott | SMC | Fibonacci | ICT — DERIVADO do producer_id/producer_type do canônico (hypothesis: CHM-001 l.361/SPEC-001; structure: producer_id do agente que a publica, p.ex. SAS-001 §6.12 — M-06); NÃO do payload; só hypothesis/structure; REGRA: hypothesis.school ≠ ICT (INV-02/RULE-HH-004)",
    "hierarchy_role": "PRIMARY | SUB — DERIVADO do papel registrado no canônico (SPEC-001); só hypothesis; HERDA liga SUB a pai PRIMARY",
    "ontological_status": "observational | theoretical (RULE-ONT-01; só structure/regime/narrative — distingue entidade medida de construção teórica, ex.: order block/liquidez)",
    "provenance_ref": { "computed_by": "OBRIGATÓRIO — identidade AUTENTICADA do PRODUTOR (CBP-014; M-05)", "gate_record": "CONDICIONAL — só se resulta de gate (CBP-007)", "lineage": "CONDICIONAL — só se DERIVADO (ref. Lineage CEM-001 Cap.5 / derived_from[] SPEC-004; [] legítimo p/ PRIMARY/asset/timeframe/regime/observation)", "who": "humano-legível (auditoria; pode diferir de computed_by)", "when": "", "why": "", "from": "" },
    "publication": { "origin": "canonical_lifecycle | spec007_seal — DERIVADO do CANAL/identidade AUTENTICADA (não do payload)", "seal_ref": "[DECISÃO NECESSÁRIA — contrato do selo = SPEC-007]" },
    "writer_id": "identidade AUTENTICADA do COMMITTER (runtime; ou serviço do KG) — DISTINTO de computed_by (M-05); falha de auth ⇒ não-autorizado",
    "relevance": "só em record_kind=archival; rebaixamento sob gate E3 (CKG-012)",
    "created_at": "2026-10-12T12:00:00Z",
    "valid_from": "2026-10-12T12:00:00Z (nós também têm validade — CKG-012; rejeita valid_to < valid_from)",
    "valid_to": "null (≡ +∞, vigente — m-09) | timestamp (em record_kind=invalidation; preservado)",
    "recorded_at": "2026-10-12T12:00:00Z"
  },
  "canonical_state_transition_record": {
    "node_id": "KG-N-...-001", "record_kind": "canonical_state_transition",
    "version": "sequência PRÓPRIA (não entra na cadeia supersedes de conteúdo — m-10)",
    "canonical_status": "ACTIVE|DOMINANT|SUPERSEDED|REFUTED|ARCHIVED (hypothesis/CHM-001) | ACTIVE|SUPERSEDED|INVALIDATED|ARCHIVED (evidence/CEM-001 l.258-262 — sem REFUTED) | COMPUTED|GATED_PASS|GATED_BLOCK|SUPERSEDED (conviction/CCM-001 l.58/78). EMERGENT/CANDIDATE NÃO constam — o histórico do KG começa na ADMISSÃO (M-01)",
    "timestamp": "", "origem": "", "justificativa": "(CEM-001 l.428)",
    "computed_by": "SERVIÇO do KG (identidade autenticada — M-05)",
    "writer_id": "SERVIÇO do KG (committer; escrita E3 — M-05)",
    "recorded_at": "2026-10-12T12:00:00Z",
    "transition_validated": "VALIDA contra a tabela do tipo (CHM/CEM): transição proibida (CEM-001 l.473-475) ⇒ FORBIDDEN_CANONICAL_TRANSITION; reativação de estado terminal VETADA"
  },
  "relation_record": {
    "relation_id": "KG-R-2026-10-12-001",
    "record_kind": "creation | invalidation | archival | collision",
    "version": "monotônico (invalidation/archival/collision têm sequência própria — m-10)",
    "expected_version": "OBRIGATÓRIO na atualização (senão DENY); criação não exige",
    "supersedes": "null | KG-R-...-v0 (sucessão de CONTEÚDO ⇒ SUPERSEDED; ÚLTIMA versão; version==anterior+1; sem FORK)",
    "targets_record_id": "null | KG-R-...-R0 (registro que invalidation/archival REFERENCIA — DISTINTO de supersedes)",
    "relation_type": "CONFIRMA | REFUTA | DEPENDE_DE | HERDA | PERTENCE_A | INVALIDA | ORIGINA | DERIVA_DE | SIMILAR_A | CAUSA | HIERARQUIA_DE | ESTATISTICA_DE",
    "from_node": "KG-N-...-A",
    "to_node": "KG-N-...-B (nó) | null quando o ALVO SEMÂNTICO é uma RELAÇÃO (INVALIDA→relation) — então usa target_relation_id (m-09)",
    "target_relation_id": "null | KG-R-...-X (quando o alvo é uma RELAÇÃO — INVALIDA; escopo de colisão INVALIDA = target_relation_id==r2.relation_id)",
    "provenance_ref": { "computed_by": "OBRIGATÓRIO — PRODUTOR autenticado (CBP-014)", "gate_record": "CONDICIONAL", "lineage": "CONDICIONAL (→ Lineage CEM-001 / derived_from[] SPEC-004)", "who": "", "when": "" },
    "writer_id": "COMMITTER autenticado (runtime; serviço do KG) — DISTINTO de computed_by (M-05)",
    "valid_from": "2026-10-12T12:00:00Z",
    "valid_to": "null (≡ +∞, vigente — m-09) | timestamp (invalidada por NOVO registro — preservada)",
    "recorded_at": "2026-10-12T12:00:00Z",
    "relation_confidence": "escala PRÓPRIA em namespace do KG — PARÂMETRO a calibrar (INDETERMINADO; NÃO é Convicção; nunca exposta ao objeto de convicção; não toca J-001/N-001)",
    "causal": "{ mechanism, direction, conditions, regime, posthoc_flag:boolean, outcome_ref, outcome_timestamp, no_outcome?:boolean+justificativa } — obrigatório sse relation_type==CAUSA (RULE-CAU-01/02/03); outcome_ref+outcome_timestamp OBRIGATÓRIOS salvo no_outcome=true (M-04); posthoc_flag DEVE ser true quando recorded_at > outcome_timestamp",
    "similarity_basis": "justificativa da base — OBRIGATÓRIO sse relation_type==SIMILAR_A proposta por juízo (CKG-008)"
  },
  "collision_record": {
    "collision_id": "KG-C-2026-10-12-001", "record_kind": "collision",
    "version": "sequência própria (m-10)",
    "relation_a": "KG-R-...-X", "relation_b": "KG-R-...-Y",
    "computed_by": "SERVIÇO do KG sob capability de detecção (identidade autenticada — M-05)",
    "writer_id": "SERVIÇO do KG (committer; escrita E3 — CKG-009)",
    "detected_at": "", "recorded_at": "2026-10-12T12:00:00Z",
    "note": "ambas preservadas; resolução = SPEC-007/SPEC-018 ou governança (CKG-013)"
  }
}
```
> Nenhum campo computa convicção nem deriva de custo (INV-04). `knowledge_state` é projeção derivada, não campo. Mecanismo físico = INDETERMINADO (H-001 ABERTA).

---

## Enforcement Contracts

### EC-CKG-001 — Escrita de nó/relação no KG permanente [E3]
```
CAPABILITY   : Escrever um nó/relação válido no KG permanente
EFFECT       : Persistência de conhecimento permanente (commit crítico/irreversível; append-only)
PRECOND      : (tipo ∈ ontologia ∧ matriz §D2.1 — CKG-001/003) AND (nó canônico referenciado, não redefinido — CKG-002) AND (proveniência CONDICIONAL: computed_by sempre ∧ [gate⇒gate_record] ∧ [derivado⇒lineage] — CKG-005) AND (fronteira: canonical_status ∈ conjunto admissível do tipo ∨ selo SPEC-007 — CKG-010) AND (CAUSA ⇒ campos CAU + outcome — CKG-008) AND (colisão registrada se houver — CKG-013)
POSTCOND     : novo registro ACTIVE_KNOWLEDGE com proveniência/validade; versão anterior preservada e não-mutada
POLICY       : RULE-CKG-001/002/003/005/008/010/013; CEM-001 l.608-615; CC-02
LEVEL        : E3 (Crítico — "KG publicado → E3 mínimo", atomic-spec §10.2; irreversível)
FAILURE-MODE : Fail-closed — qualquer precondição falha ⇒ REJECTED; nada persistido; log. Falso-DENY E3 CONDICIONAL até limiar amostral (ENF-07)
EVIDENCE     : registro reconstruível (tipo/version/supersedes/ref canônica/proveniência/validade) + amostragem de falso-DENY (ENF-07)
```

### EC-CKG-002 — Imutabilidade / append-only / versionamento [E3]
```
CAPABILITY   : Impedir deleção/mutação de registro e garantir transições versionadas
EFFECT       : Transição por NOVO registro (SUPERSEDED/ARCHIVED/INVALIDATED_IN_TIME) — nunca remoção/reescrita
PRECOND      : (operação ∉ {DELETE físico, UPDATE de registro}) AND (ao substituir: supersedes=última ∧ version==anterior+1 ∧ expected_version==corrente — CBP-004 l.239-246) AND (sem FORK) AND (dedupe: mesma chave sem supersedes divergente ⇒ DENY)
POSTCOND     : histórico preservado e reconstruível; estado = projeção derivada; nenhum registro removido/mutado (INV-07; INV-CBP-01)
POLICY       : RULE-CKG-004/006/012; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01; INV-CKG-01
LEVEL        : E3 (Crítico — perda/reescrita de histórico é irreversível; fail-closed)
FAILURE-MODE : Fail-closed — DELETE/UPDATE/FORK ⇒ negado; log. Falso-DENY E3 CONDICIONAL até limiar (ENF-07)
EVIDENCE     : gate_record de imutabilidade + registro das tentativas de DELETE/UPDATE bloqueadas + ENF-07
```

### EC-CKG-003 — Governança de escrita (autorizado + autenticado) [E3]
```
CAPABILITY   : Admitir escrita só de escritor autorizado/autenticado, sem redefinição de ontologia pelo produtor
EFFECT       : Autorização (ou recusa) de escrita permanente
PRECOND      : (escritor ∈ autorizados ∧ identidade AUTENTICADA — CBP-014; auth indisponível ⇒ não-autorizado) AND (operação ∉ {redefinir ontologia/taxonomia} — SAS-001 §6.12, extensão [INFERÊNCIA]) AND (gate determinístico — ENF-03)
POSTCOND     : só escritor autorizado escreve; produtor registra, não redefine ontologia
POLICY       : RULE-CKG-009; SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04
LEVEL        : E3 (Crítico — escrita permanente; cruza fronteira de confiança)
FAILURE-MODE : Fail-closed — não autorizado / falha de auth / redefinir ontologia ⇒ negado; log. Falso-DENY E3 CONDICIONAL (ENF-07)
EVIDENCE     : gate_record de autorização por identidade autenticada + amostragem de falso-DENY (ENF-07)
```

### EC-CKG-004 — Confiança de relação em namespace próprio (guard; INV-04) [E3]
```
CAPABILITY   : Manter a confiança em namespace próprio e não escrever NENHUMA aresta to_node==conviction
EFFECT       : Guard (na escrita permanente e na consulta) de que confiança não vira campo/aresta de convicção
PRECOND      : (confiança em namespace separado) AND (matriz §D2.1 proíbe QUALQUER aresta to_node.node_type==conviction, direta ou 2 saltos)
POSTCOND     : nenhum campo de convicção recebe a confiança; nenhuma aresta to_node==conviction é escrita
POLICY       : RULE-CKG-007; INV-04 (custo); CCM-001; SPEC-003
LEVEL        : E3 (Crítico — guard sobre a escrita permanente; atomic-spec §10.2)
FAILURE-MODE : Fail-closed — expor confiança / aresta to_node==conviction ⇒ negado; log. Falso-DENY E3 CONDICIONAL (ENF-07)
EVIDENCE     : verificação de namespace separado e ausência de aresta to_node==conviction + ENF-07. Que o CÁLCULO de convicção (SPEC-003) não a consuma = requisito à SPEC-003 / [DECISÃO NECESSÁRIA] — fora do controle do KG
```

### EC-CKG-005 — Registro de relação causal com mecanismo/regime/desfecho (RULE-CAU) [E3]
```
CAPABILITY   : Admitir CAUSA só com mechanism+direction+conditions+regime+posthoc_flag+outcome (ou no_outcome)
EFFECT       : Escrita (ou recusa) de relação CAUSA — persistência permanente (E3)
PRECOND      : (CAUSA) ⇒ (mechanism ∧ direction ∧ conditions ∧ regime ∧ posthoc_flag booleano ∧ (outcome_ref ∧ outcome_timestamp ∨ no_outcome+justificativa) ∧ [recorded_at>outcome_timestamp ⇒ posthoc_flag==true]); (SIMILAR_A por juízo) ⇒ similarity_basis; gate determinístico (Classe H); bounded loop
POSTCOND     : relações causais têm campos auditáveis; nenhuma pós-hoc por correlação sem marcador/desfecho
POLICY       : RULE-CKG-008; RULE-CAU-01/02/03; ENF-03
LEVEL        : E3 (Crítico — write permanente; herda EC-CKG-001)
FAILURE-MODE : Fail-closed — campos ausentes ⇒ rejeitada; retry bounded. Falso-DENY E3 CONDICIONAL (ENF-07)
EVIDENCE     : registro dos campos causais; contagem de tentativas ≤ limite; gate verifica presença, não veracidade (ENF-03) + ENF-07
```

### EC-CKG-006 — Consulta cognitiva / Trace Reconstruction (read-only)
```
CAPABILITY   : Responder consultas e reconstruir a cadeia cognitiva da EVIDÊNCIA (completa) sem alterar estado
EFFECT       : Leitura/navegação (sem escrita)
PRECOND      : (consulta read-only) AND (consumidor autorizado a ler)
POSTCOND     : resposta/trace da Evidência COMPLETO; trace de hipótese best-effort; nenhum estado alterado
POLICY       : RULE-CKG-011; CEM-001 l.608-615/l.612-614; SAS-001 §6.12
LEVEL        : E1 (Contratual — leitura observável; não muta estado)
FAILURE-MODE : Fail-closed — consulta que tente mutar ⇒ negada; completude do trace de Evidência é obrigatória; eficiência ampla = INDETERMINADO até H-001
EVIDENCE     : log de consulta read-only; trace = fecho transitivo de DERIVA_DE
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
Serviço lógico de **memória semântica permanente** (Opção A — camada sobre o conhecimento já validado/publicado).
Combina gates constitutivos (Classe C: ontologia/integridade, proveniência, imutabilidade, governança E3, fronteira,
isolamento confiança×convicção, colisão) + mecânica determinística (Classe D: catálogo, temporalidade bitemporal,
lifecycle, consulta/trace) + um juízo com gate de saída (Classe H: similaridade/causalidade). **Não guarda trabalho, não
transporta, não forma conhecimento, não decide, não computa convicção, não executa, e NÃO escolhe o mecanismo físico
(H-001 ABERTA).** [FONTE: ROADMAP §6; CEM-001 l.608-615; SAS-001 §6.12; research.md §3/§4]

### Roteamento de modelo (CEE-001 §5)
Gates C/D não requerem LLM. O juízo de similaridade/causalidade (Classe H, CKG-008) pode usar apoio semântico **apenas
como detector** para PROPOR; o gate de saída é **determinístico** (ENF-03). Mecanismo físico = **INDETERMINADO = H-001
(ABERTA)**. [FONTE: CEE-001 §5; ENF-03; H-001 ABERTA]

### Dependências técnicas
CEM-001 (BASELINE) · CHM-001 · CCM-001 · CEE-001 l.111 · SAS-001 §6.12 · SPEC-004 v1.2 (BASELINE — proveniência/
`gate_record`/identidade; CBP-004 l.239-246; INV-CBP-01) · SPEC-005 v1.0 (BASELINE — **[INFERÊNCIA]/[DECISÃO NECESSÁRIA]**
eventual consumo de eventos pelo KG; emissão pelo KG = [DECISÃO NECESSÁRIA] — m-08) · SPEC-007 (fronteira — selo de
publicação, ainda não especificada = [DECISÃO NECESSÁRIA]) · CONSTITUTION l.233 · RULES.md (RULE-BB-004, RULE-CAU-01/02/03,
RULE-ONT-01/02, RULE-MECH-01, RULE-HD-02/03/04) · SPEC-019 (governança da ontologia — [INFERÊNCIA]) · SPEC-019/020/021 v1.0 ·
atomic-spec v1.5 (§10.2 E3) · INV-04/05/06/07/09/10 · ENF-01..08. Externas [EXTERNO], não-baseline: research.md §2
(SRC-ZEP-01, SRC-PROV-01, SRC-MEMVSKG-01, SRC-FORGET-01 — DADO não-verbatim) e §5 (REPO-graphiti/graphrag/cognee/mem0 —
elegíveis, nenhum adotado).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Banco de grafos por inércia do nome "Graph" | Opção A; Opção B ADIADA; mecanismo físico = H-001 (ABERTA); ADV-09 |
| Fixar H-001 por engano | contrato independe de H-001; H-001 [DECISÃO NECESSÁRIA]; ADV-09; CONS-01 |
| Absorver a SPEC-007 (formação/retrieval) | Non-goal; CKG-010 (selo); ADV-08 |
| Reabrir/duplicar SPEC-004/005 | CC-02; cobertura×lacuna; INV-09; ADV-10 |
| Confiança virar Convicção | INV-04; CKG-007; EC-CKG-004; ADV-03/05 |
| Deleção/mutação disfarçada de "esquecimento" | INV-07; INV-CBP-01; CKG-006/012; EC-CKG-002 (E3); ADV-01/13/15 |
| Causalidade pós-hoc / sem regime / sem desfecho | RULE-CAU-01/02/03; CKG-008; EC-CKG-005; ADV-04 |
| Colisão resolvida em silêncio | CKG-013; EC-CKG-001; ADV-02 |
| Escrita sem proveniência / produtor redefine ontologia / auth falha-aberto | CKG-005/009; EC-CKG-001/003 (E3); ADV-06/07 |
| Redefinir contrato canônico / reativar terminal | CKG-002; EC-CKG-001; ADV-11; CC-02; CEM-001 l.473-475 |
| Violar matriz (ICT origina) | CKG-001; §D2.1; EC-CKG-001; ADV-12/17; INV-02 |
| Trace incompleto / consulta que muta | CKG-011; EC-CKG-006; ADV-14; CEM-001 l.612-614 |
| LLM como gate | ENF-03; EC-CKG-003/005 |
| Ontologia sem governança | §D2.1; SPEC-019 (spec-time)/K-001 (runtime [DECISÃO NECESSÁRIA]); CKG-009 |
| Crescimento ilimitado | lifecycle versionado (CKG-012); observabilidade = SPEC-040 |

### Impacto (RULE-HG-04)
- **Schemas:** introduz o schema lógico do registro de nó/relação; nenhum schema canônico nem SPEC-004/005 alterado.
- **RAG/KG:** especifica o contrato do próprio KG; formação/retrieval em SPEC-007 (não absorvida).
- **Skills:** nenhuma afetada; INV-06 preservado.
- **Testes:** adiciona `checks.md`; mecanismo físico fica para BUILD (H-001).
- **Modelos/Specs:** CEM/CHM/CCM/SPEC-004/005 não alterados; RULE-BB-004 reforçada no eixo permanente.
- **Compatibilidade:** Minor — não toca canônico baselined, não reabre SPEC-004/005, não fecha decisão aberta (H-001 ABERTA).

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Aplicarão SES-001 §59/§60 (CC-06/CC-07), a Classe por BASpec
(CC-11) e o mecanismo físico (INDETERMINADO, **H-001**). O fechamento de H-001 é de Andraus; a homologação do Plan não o
exige (contrato fechável com mecanismo físico aberto — Opção A).

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — pergunta adversarial por BASpec (13 BASpecs):** cada BASpec tem ENTÃO verificável por observador independente
e ≥1 caso de negação em D8 (CKG-001→ADV-12/17,T01; 002→ADV-11,T02/T09; 003→ADV-12/16/20,T03; 004→ADV-13,T04; 005→ADV-06,
T14; 006→ADV-01/19,T05; 007→ADV-03/05,T06; 008→ADV-04,T07/T16; 009→ADV-07,T08; 010→ADV-08/21,T09; 011→ADV-14,T10; 012→
ADV-15/19,T13; 013→ADV-02/18,T11). "Se a BASpec estivesse errada" é observável em cada caso. Nenhuma restou [DECISÃO
NECESSÁRIA] por falta de verificabilidade (H-001/selo SPEC-007/M-001/J-001/N-001/G-001/K-001/C-001/WF-D03 são fronteiras/
decisões abertas explícitas, não falhas de verificabilidade).

**Bloco B — herança obrigação-a-obrigação (CC-08):** evidência por obrigação herdada:
- CEM-001 "preservar os estados / trace COMPLETO" → CKG-010 preserva os estados **A PARTIR DA ADMISSÃO** (M-01; EMERGENT/CANDIDATE = SPEC-004, registrado em MODIFIED) + CKG-011 trace completo da EVIDÊNCIA (não rebaixado por H-001; hipótese = [PROPOSTA]); não redefine.
- CEM-001 Cap.5 `Lineage` → tipo DERIVA_DE (aresta) + `provenance_ref.lineage` (campo local [PROPOSTA]), distinguidos.
- CHM-001 (estados/versionamento) → CKG-002/012 por referência; não transiciona.
- CCM-001 → CKG-007/EC-CKG-004 isolam confiança (INV-04); estados conviction (l.58/78) no conjunto admissível (CKG-010).
- SPEC-004 v1.2 INV-CBP-01/CBP-004 → CKG-004/006/012 (novos registros; compare-and-commit; estado derivado); `computed_by`(produtor)≠`writer_id`(committer) (M-05).
- SPEC-005 (eventos) → **[INFERÊNCIA]/[DECISÃO NECESSÁRIA]** eventual consumo (D6); emissão pelo KG NÃO afirmada (m-08).
- SAS-001 §6.12 → CKG-009/EC-CKG-003 (escopo Structural Agent; extensão a outros produtores = [INFERÊNCIA]).
- RULE-BB-004/INV-07 → CKG-006/012. RULE-CAU-01/02/03 → CKG-008. CEE-001 l.111 → ADV-05. atomic-spec §10.2 → EC-CKG-001/002/003/005 em E3.
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (MODIFIED = RULE-BB-004 reforçada + especialização M-01 de alcance, RULE-HD-02). **Eixo VERTICAL (RULE-HV) não aplicável.**

**Bloco C — epistêmico / disciplinas N8–N17 (verificado — sem achado residual):**
- **RULE-EPI-01..03:** H-001/mecanismo físico = INDETERMINADO (não fato); nenhuma hipótese tratada como fato.
- **RULE-SEM-01/04:** acepções declaradas (CC-10); termos canônicos não redefinidos.
- **RULE-ONT-01/02:** ontologia declarada (§D2.1); `school`/`hierarchy_role` derivados do produtor (incl. structure — M-06); `ontological_status` {observational, theoretical} (RULE-ONT-01, l.671); alteração por governança (RULE-ONT-02/CKG-009).
- **RULE-INQ:** questões abertas (H-001, selo SPEC-007, allowlist, host do juízo, migração de ontologia) formuladas como [DECISÃO NECESSÁRIA], não respondidas por suposição.
- **RULE-CAU-01/02/03:** CKG-008 exige mechanism+direction+conditions (01), regime (02), marcador pós-hoc + desfecho (03/M-04); gate verifica presença (ENF-03).
- **RULE-CTF:** nenhuma afirmação contrafactual carregada; "o que seria observável se errada" é só teste de verificabilidade.
- **RULE-UNC-01..03:** incerteza localizada (eficiência de consulta ampla até H-001); completude do trace de Evidência NÃO é incerta.
- **RULE-PRB:** nenhuma probabilidade/precisão numérica; confiança = PARÂMETRO a calibrar, sem número.
- **RULE-DEC-01:** o KG armazena/relaciona/consulta; não decide nem executa (INV-05).
- **RULE-MET-01:** nenhuma escala/limiar fabricado; SRC-FORGET-01 = DADO não-verbatim (não sustenta sozinha alegação carregada — "esquecimento=arquivamento" apoia-se em INV-07/RULE-BB-004).

**Bloco D — reforço de escopo:** a Spec **preserva/relaciona/consulta** conhecimento permanente, **não guarda trabalho**
(SPEC-004), **não transporta** (SPEC-005), **não forma** (SPEC-007), **não executa** (INV-05/RULE-DEC-01), **não decide**
nem **computa** convicção. Nenhuma BASpec cruza a fronteira SOT→execução downstream. Dependências de Andraus (homologação;
RULE-CKG/contrato; **H-001**; selo SPEC-007; allowlist/host do juízo; migração de ontologia) marcadas [PROPOSTA]/[DECISÃO
NECESSÁRIA]; M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 abertas, não tocadas.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001; CHM-001; CCM-001; CEE-001; SAS-001; SPEC-004 v1.2; SPEC-005 v1.0; SPEC-001/019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5; RULES v1.5 (RULE-BB-004, RULE-CAU, RULE-ONT, RULE-MECH, RULE-HD); INV-*; ENF-*; CONSTITUTION l.233 | [FONTE] | FATO NORMATIVO |
| RULE-CKG-001..013; INV-CKG-01/02; matriz §D2.1/§D2.2; contrato de nó/relação; BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | Requer homologação |
| Extensão da fronteira SAS-001 §6.12 a produtores não-estruturais; governança da ontologia análoga a RULE-HG; consumo de evento pelo KG | [INFERÊNCIA] | Derivado; a confirmar |
| Fontes SRC-ZEP-01/PROV-01/MEMVSKG-01; REPO-graphiti/graphrag/cognee/mem0 | [EXTERNO] | DADO, nunca baseline |
| SRC-FORGET-01 (sumário WebSearch) | [EXTERNO] | DADO **não-verbatim** — não sustenta sozinha alegação carregada |
| Mecanismo físico de armazenamento | [DECISÃO NECESSÁRIA] | **H-001 — EM ABERTO — não fechar** (Andraus) |
| Banco de grafos dedicado (Opção B) | [DECISÃO NECESSÁRIA] | **ADIADO** — registrado, não apagado (INV-07) |
| Escala numérica de confiança de relação | [DECISÃO NECESSÁRIA] | PARÂMETRO a calibrar — INDETERMINADO (não toca J-001/N-001) |
| Contrato do selo de publicação | [DECISÃO NECESSÁRIA] | Dependência da **SPEC-007** |
| Allowlist de escritores / host do juízo CKG-008 / migração de ontologia | [DECISÃO NECESSÁRIA] | Runtime/governança (K-001/SPEC-018; SPEC-019 spec-time) |
| Emissão de evento pelo KG / consumidor-contrato de consumo | [DECISÃO NECESSÁRIA] | Dependente da SPEC-005 — não afirmada |
| Componente "Cognitive Ontology" separado | [DECISÃO NECESSÁRIA] | Ontologia DENTRO da SPEC-006 (Q-ABERTURA-4); é de Andraus |
| Enum de estados do Blackboard p/ objetos não-hipótese | [DECISÃO NECESSÁRIA] | **M-001 — EM ABERTO (SPEC-004)** — não tocado |
| Fórmula/pesos/limiares do Conviction Vector; pesos por ativo | [DECISÃO NECESSÁRIA] | **J-001 / N-001 — EM ABERTO (SPEC-003/backtest)** — não tocadas |
| Estado persistente por agente / ciclo P12 | [DECISÃO NECESSÁRIA] | **G-001 / K-001 — EM ABERTO (SPEC-009/018)** — não tocadas |
| Granularidade EARS multi-condição / relação convicção-macro-global | [DECISÃO NECESSÁRIA] | **C-001 / WF-D03 — EM ABERTO** — não tocadas |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-006 confirmada (§6/§21); FASE 3, após SPEC-005 BASELINE v1.0.
[x] atomic-spec.md lido: método v1.5 (CC-11/CC-12; RULE-MECH-01; RULE-ECC-04/06; §15 Dossiê; §3 CRITICAL·D0–D7; §10.2 "KG publicado → E3").
[x] Nenhum invariante congelado violado (INV-01..10); INV-04/05/06/07/09/10 reforçados; INV-CKG-01; escrita = E3.
[x] Constitution Check CC-01..CC-12 (N/A justificados CC-06/07/12; CC-02/08/09/10/11 INCIDEM e aplicados).
[x] Disciplinas N8–N17: tratadas no §7-bis Bloco C.
[x] Referências externas [EXTERNO] classificadas; engines NÃO adotadas; verbatim em sources/ (RULE-ECC-04); repositórios régua Equilibrada (RULE-ECC-06 — 4 elegíveis).
[x] RULE-ECC-05 (Multi-Lente): NÃO-incidência confirmada (DHR-SPEC006-001 §2); conformidade WORKFLOW por prudência; não fecha WF-D03.
[x] Spec sem implementação (BUILD adiado); Plan derivado da abertura homologada; Tasks adiadas.
[x] EARS (13) referenciam a regra-fonte por ID; BASpecs (CKG-001..013) com Classe (CC-11); RULEs citadas existentes vs propostas etiquetadas.
[x] Profundidade D0–D7 (+ D8 focado); §D2.1 (matriz) + §D2.2 (colisão); §D3.1 (vocabulário); D4; D5 (estado derivado); D6; D7 x16; D8 x21; D9 por referência.
[x] Enforcement Contract em todo ato com efeito (EC-CKG-001..006); escrita = E3; E1 consulta; guard confiança×convicção = E3; ENF-07 amostral nos E3 (CONDICIONAL até limiar).
[x] Status epistemológico aplicado (FATO NORMATIVO / PROPOSTA / INFERÊNCIA / EXTERNO / DECISÃO NECESSÁRIA).
[x] CONS-01: H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 permanecem ABERTAS; nenhuma usada como invariante fechado; STRUCT-10 respeitado.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] CONSOLIDAÇÃO (Rodada 6): cada regra definida UMA vez (RULE-CKG/BASpec); EARS/D4/D6/EC/T/ADV/Herança referenciam por ID; narrativa histórica só no changelog (1 linha/versão, ordenado 1.0→1.5).
[x] Integridade: nenhuma fonte inventada; linhas canônicas verificadas (CEM-001 l.258-262/l.473-475/l.494/l.602/l.608-615; CCM-001 l.58/78; SPEC-001 l.104/108/515-520/524; SPEC-004 CBP-004 l.239-246/CBP-007 l.543-558/CBP-014 l.311-319; RMR-001 l.128/l.192 BL-029 `Em espera`).
[x] 4Es na ordem; Conformidade > Eficácia. Latência não material (consulta opcional/não-bloqueante — SAS-001 §6.12).
[x] Dependências a montante homologadas; selo SPEC-007 marcado [DECISÃO NECESSÁRIA].
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); obrigatório CRITICAL.
[x] CC-11/§10.6: Classe por BASpec; C com gate de saída; H (CKG-008) com bounded loop + gate.
[x] Abertura (RULE-ECC-01/02/04/06): Dossiê presente e HOMOLOGADO (DHR-SPEC006-001); escopo/quantidade homologados (1 Spec).
[x] Passo 11-bis: nenhum gatilho spec:SPEC-006 isolado; BL-003/BL-010/BL-011 tratados; BL-029 = `Em espera`, independente.
[ ] Gate determinístico (validate_spec_sot.py), check_repo_research.py, build_map.py --check, check_doc_sync.py, check_invariants.py, revisor_gate.py: **NÃO executáveis por mim (sem Bash)** — reportados ao caller para execução.
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] / abertas nesta Spec (não fechadas — CONS-01):
- **H-001** — a SPEC-006 **propõe o recorte** (contrato independe do mecanismo físico), mas **não decide** — é de Andraus. Permanece ABERTA.
- **Opção B (banco de grafos)** — ADIADA (registrada, não apagada — INV-07).
- **Escala de confiança de relação** — PARÂMETRO a calibrar (INDETERMINADO; não toca J-001/N-001).
- **Contrato do selo de publicação** — dependência da **SPEC-007**; [DECISÃO NECESSÁRIA].
- **Allowlist de escritores / host do juízo CKG-008 / migração de ontologia** — runtime/governança (K-001/SPEC-018; SPEC-019); [DECISÃO NECESSÁRIA].
- **Emissão/consumo de evento pelo KG** — dependente da SPEC-005; [DECISÃO NECESSÁRIA] (não afirmada).
- **Produtor/gatilho de promoção trabalho→permanente** — [DECISÃO NECESSÁRIA] (SPEC-018/K-001; distinto do critério de estado, que é verificável).
- **Componente "Cognitive Ontology" separado** — não criado; ontologia DENTRO da SPEC-006; é de Andraus.
- **M-001 / J-001 / N-001 / G-001 / K-001 / C-001 / WF-D03 / ECC-03-001** — permanecem ABERTAS; não tocadas.

**Volume (F-17 — registrado, NÃO dividido):** CRITICAL, 13 BASpecs/16 cenários/21 ADV + §D2.1/§D2.2 + §D3.1 + schema. A
decisão de DIVIDIR a Spec é **exclusivamente de Andraus (Q-ABERTURA-5)** — o Especificador não divide; slot preservado (INV-07).

