# SPEC-005 — Cognitive Event Bus

| Campo | Valor |
|---|---|
| ID | SPEC-005 — Cognitive Event Bus (camada fina de notificação de mudança sobre o log append-only da SPEC-004 + canal de saída da notificação do Signal Package) |
| Versão | 1.0 (BASELINE — homologado, DHR-SPEC005-002) |
| Status | **HOMOLOGADA — BASELINE v1.0 (Andraus, 2026-10-05, DHR-SPEC005-002; parecer Revisor CONFORME; compat. Minor).** Abertura: DHR-SPEC005-001 (2026-10-04). **EVENT-BUS-001 FECHADA por Andraus na homologação** (aprovou a distinção proposta em CEB-012: Blackboard guarda a verdade; Event Bus só notifica). As etiquetas [PROPOSTA] / [DECISÃO NECESSÁRIA] no corpo do documento são HISTÓRICAS (descrevem o estado pré-homologação); desde DHR-SPEC005-002 as RULE-CEB-001..012 e INV-CEB-01 são vigentes por homologação (registro físico em RULES.md diferido — RULE-HG-02). M-001, J-001, N-001, H-001, G-001, WF-D03 e ECC-03-001 seguem ABERTAS. |
| Fonte | ROADMAP §5 (FASE 2); `specs/features/SPEC-005/ABERTURA.md` + `research.md` (Dossiê HOMOLOGADO — DHR-SPEC005-001; RULE-ECC-01/02/04/06); atomic-spec **v1.5**; `governance/RULES.md` (RULE-BB-001/004/005); `WORKFLOW.md` (conformidade, não editada) |
| Complexidade | **HIGH** [FONTE: ROADMAP §5 "P0 — HIGH"; atomic-spec §3 "SMC/Institutional · Event Bus = HIGH"; DHR-SPEC005-001 §2] |
| Profundidade-alvo | **D0–D7** (profile **standard**; sem D8 pinado — nenhuma elevação em silêncio; rigor adversarial focado, sem elevar o profile, nos pontos de risco: entrega duplicada/perdida, ordem observada pelo consumidor, replay a partir de cursor, dead-letter, saída externa) [FONTE: ROADMAP §5; AGENTS.md §4; DHR-SPEC005-001 §2] |
| Profile (Claude Code) | standard |
| Posição no caminho crítico | FASE 2 — MEMÓRIA DE TRABALHO E COMUNICAÇÃO; após SPEC-004 (Blackboard, BASELINE v1.2); opera **sobre** o log append-only já homologado [FONTE: ROADMAP §5/§21] |
| Nível de maturidade-alvo | **L3 (Testável)** — HIGH → L3 teto spec-first; gate normativo E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01 (Classe por BASpec); RULE-PD-01/CC-12 **(N/A)**; RULE-ECC-04 (verbatim); RULE-ECC-06 (repositórios); RULE-ECC-05 **(N/A — não toca comportamento de trading)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — **D** (envelope, correlation/causation, cursor, dedupe de consumo, ordering observado, metadados de transporte, observabilidade) + **C** (fail-safe "transporte ≠ fonte de verdade", dead-letter obrigatório, entrega a consumidor autorizado, canal de saída externo do Signal Package); declaração normativa é **por BASpec** |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-04 |
| Abertura | Dossiê de Pesquisa HOMOLOGADO por Andraus (DHR-SPEC005-001, research.md); Plan iniciado dentro da validade do Dossiê (HIGH → 90 dias; limite 2027-01-02; ECC-VAL-001 FECHADA, DHR-DEC-003) |

Complexidade: HIGH. Profundidade-alvo: D0–D7 (standard).

**Princípio fundador desta Spec (transversal):** **TRANSPORTE ≠ FONTE DE VERDADE.** *"Blackboard guarda estado; Event Bus transporta/notifica mudanças."* (ROADMAP §5). A durabilidade, a ordem de commit, a idempotência de escrita, o replay e a supersessão **de estado** são da **SPEC-004 (BASELINE v1.2)** — a SPEC-005 **não** as reintroduz. A SPEC-005 é a **camada fina de notificação** (Forma A, DHR-SPEC005-001 §2) que lê o log append-only por **cursor** e **notifica** consumidores, mais o **canal de saída** da notificação do Signal Package à fronteira externa (INV-05: o SOT não executa ordem). O mecanismo físico (push/poll/LISTEN-NOTIFY) é **INDETERMINADO** até o BUILD — esta Spec define **o QUE** (contratos, invariantes, garantias observáveis), não **o COMO**. [FONTE: ROADMAP §5; DHR-SPEC005-001 §2; research.md §3]

**Status epistemológico de cabeçalho:** a SPEC-005 é a **camada Harness/operacional de transporte de notificação** sobre o log append-only da SPEC-004 (vigente/BASELINE) e sobre as RULE-BB-001/004/005. **NÃO redefine** CHM-001, CEM-001, CCM-001 nem a SPEC-004 (**CC-02/CONST-01/INV-09**): apenas **propaga** eventos de ciclo de vida sob seus contratos canônicos. **EVENT-BUS-001** (o Event Bus existe? como se distingue do Blackboard?) permanece **ABERTA** — este Plan **propõe** a distinção, não a fecha (CONS-01; decisão de Andraus). [FONTE: ROADMAP §5/§7; atomic-spec §12; DHR-SPEC005-001 §3]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-10-04 | Entrega candidata inicial do Plan (Forma A). Camada fina de notificação sobre o log da SPEC-004 + canal de saída do Signal Package; 12 BASpecs (CEB-001..012) com Classe D/C (CC-11); 5 Enforcement Contracts (EC-CEB-001..005; E3 fail-closed na saída externa do Signal Package; falso-DENY E3 condicional); 12 EARS; D4 (cursor/dedupe/correlation-causation); D5 (ciclo de vida do evento/entrega); D6 (protocolo de notificação); D7 (≥3 cenários — T01..T10); D8 (rigor adversarial focado, sem profile elevado — ADV-CEB-01..08); D9 por referência. EVENT-BUS-001 apresentada como **[PROPOSTA]** de resolução, não fechada. Orçamento de latência/metadados de transporte declarado como **PARÂMETRO a calibrar** ([DECISÃO NECESSÁRIA]/INDETERMINADO — sem número arbitrário). Corrige o Menor A4 (research.md §6.4 alinhado à decisão de manter o nome). |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; DHR-SPEC005-001 §6; RMR-001]

- **Nenhum item do RMR-001 tem gatilho `spec:SPEC-005`** (verificado na abertura; `backlog_triggers.py` a rodar). O início da redação deste Plan **não dispara item novo**. [FONTE: DHR-SPEC005-001; ABERTURA §9]
- **[ERRATA 2026-10-05, ERRATUM-SPEC005-001: BL-008 = `Absorvido` (DHR-BL008-001), não ATIVADO]** · **BL-008** (auditoria retroativa SPEC-001) e **BL-003** (persistência física) permanecem `ATIVADO`/pré-existentes, **independentes desta Spec** — não absorvidos nem promovidos aqui (gate passo 11-bis + Andraus). [FONTE: RMR-001; ABERTURA §9]
- **BL-017** (dimensões B da SPEC-020) está `Em espera` (gatilho `spec:SPEC-007`/`spec:SPEC-014`), **independente desta abertura** — não promovido por esta Spec (CONS-01). [FONTE: RMR-001; DHR-BL012-001]
- A **promoção/encaminhamento** é do gate e de Andraus; o Especificador apenas reflete o tratamento. O passo 11-bis pleno ocorre na homologação do Plan.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o Event Bus é **infraestrutura de transporte agnóstica de escola** — transporta/notifica mudanças de qualquer camada analítica **sem** alterar a hierarquia nem a autoridade de criação de hipótese (Elliott cria primária; ICT não cria — INV-01/INV-02). Não introduz comportamento que sobreponha camada inferior à superior; não interpreta nem decide. [FONTE: INV-01/INV-02; ROADMAP §6]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM) nem a SPEC-004:** **foco.** O Event Bus **propaga** eventos de ciclo de vida da hipótese (CHM-001) e da Evidência (CEM-001 l.717-727, idioma canônico INV-10) e do objeto Convicção (CCM-001) **sem redefinir** contrato, campos nem máquina de estados. **Não reabre** a SPEC-004 (BASELINE v1.2): durabilidade/ordem/idempotência de escrita/replay/supersessão **de estado** são dela; a SPEC-005 **lê/projeta/notifica** sobre o log, não o redefine (INV-09). CDM-001/CNM-001 pendentes não acionam CONST-01. [FONTE: CC-02; CEM-001 l.725; SPEC-004 v1.2; CHM-001; CCM-001]
- [x] **CC-03 — Conviction Vector:** o Event Bus **não computa** convicção — apenas transporta a **notificação** de que um objeto Conviction Vector mudou. Dimensionalidade=8 (fechada) intocada; a fórmula/pesos/limiares definitivos do Conviction Vector permanecem **pendentes (J-001 ABERTA)** e **não** são tratados aqui; nenhum limiar numérico de convicção é declarado neste Plan. [FONTE: INV-03; J-001 pendente/ABERTA; N-001 ABERTA]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. O Event Bus não emite sinal de trading, não dimensiona risco e não aplica gates de sinal (isso é SPEC-003/Manager/RISK-M5). **INV-04** (custo nunca no Conviction Vector) preservado por construção — o transporte não cria convicção nem injeta custo. [FONTE: CEE-001 §10/§11; INV-04]
- [x] **CC-05 — Complexidade declarada:** HIGH, D0–D7 standard (ROADMAP §5; DHR-SPEC005-001 §2).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card; §59/§60 tornam-se obrigatórios nas Tasks/Cards (BUILD adiado — atomic-spec §14). Omissão justificada.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem: ROADMAP §5 → Dossiê (research.md, HOMOLOGADO DHR-SPEC005-001) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED com ID+versão (RULE-HD-04); REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Mapa de cobertura×lacuna da SPEC-004 v1.2 com arquivo:linha incluído. Eixo VERTICAL (RULE-HV) avaliado e declarado não aplicável. [FONTE: EUA-E04 §8.3; RULE-HD-02/03/04]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI):** aplicado — **EVENT-BUS-001 declarada ABERTA** ([DECISÃO NECESSÁRIA]), não como fato; mecanismo físico (push/poll/LISTEN-NOTIFY) = **INDETERMINADO**; **orçamento de latência = PARÂMETRO a calibrar** ([DECISÃO NECESSÁRIA] — sem falsa precisão: nenhum número arbitrário); fontes web = DADO [EXTERNO] (research.md §2). [FONTE: RULE-EPI-01..03; research.md §8]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM-01):** **INCIDE e tratado** (ver "Declaração de acepção semântica"): **"Evento"** (mudança notificada, best-effort — SPEC-005) vs **"Objeto"** (estado versionado durável — SPEC-004) vs **"Observação"** (produzida por Skill — INV-06); **"entrega/notificação"** (transporte — SPEC-005) vs **"publicação/commit"** (de estado — SPEC-004); **"idempotência de consumo"** (dedupe do consumidor — SPEC-005) vs **"idempotência de escrita"** (SPEC-004). Nenhum termo canônico do GLOSSARIO redefinido (RULE-SEM-04). [FONTE: RULE-SEM-01/04; INV-06; GLOSSARIO]
- [x] **CC-11 — Classe/Mecanismo por BASpec com efeito (RULE-MECH-01):** **INCIDE** — a SPEC-005 cita RULE-MECH-01 e é "SPEC-002 em diante". Cada BASpec com efeito declara Classe (D/C) com critério 4Es; Classes C declaram gate de saída determinístico; não há Classe H/P normativa nesta Spec (eventual juízo de "evento bem-formado" seria orientação de BUILD — detector, nunca gate, ENF-03). Declaração por BASpec, nunca por Spec inteira (SES-001 §50). Ver §D3. [FONTE: RULE-MECH-01..04; atomic-spec §9/§10.6]
- [x] **CC-12 — Princípios de Domínio `PD-xx` (RULE-PD-01):** **N/A — não incide** (DHR-SPEC005-001 §2; ABERTURA §6). O Event Bus é **infraestrutura de transporte agnóstica de escola** — não define escopo de especialidade (Elliott/SMC/ICT). Mesmo padrão N/A de SPEC-002/SPEC-004. Registrado explicitamente, não supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7; DHR-SPEC005-001 §2]

**Disciplinas cognitivas N8–N17 incidentes (RULES.md v1.5):** RULE-EPI (EVENT-BUS-001 ABERTA ≠ fato; INDETERMINADO sobre mecanismo físico), RULE-MET-01 (não-fabricação — nenhum número de latência fabricado; IDs arXiv implausíveis descartados, research.md §aviso), RULE-UNC-01..03 (incerteza localizada sobre ordenação cross-workspace e perda de notificação), RULE-SEM-01/04 (acepções "evento" vs "objeto" declaradas; termos canônicos não redefinidos), RULE-DEC-01 (o Event Bus **transporta/notifica**, não decide nem executa — INV-05). INDETERMINADO usado onde há incerteza material.

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-005

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - SPEC-004 v1.2 (BASELINE — DHR-SPEC004-003): o SUBSTRATO durável. A SPEC-005 opera SOBRE ela e
    NÃO a reabre. Herdado como FRONTEIRA/fonte de verdade (ver "Cobertura × lacuna" abaixo):
      • log append-only; ordem total de COMMIT por workspace (seq persistido/imutável) — RULE-CBP-006
      • idempotência de ESCRITA (chave + request_fingerprint) — RULE-CBP-005
      • replay/reconstrução do estado LÓGICO — RULE-CBP-011
      • supersessão append-only real (supersedes gravado; superseded_by derivado) — RULE-CBP-003/INV-CBP-01
      • schema_version no envelope do objeto — RULE-CBP-001
      • identidade AUTENTICADA pelo runtime (não do payload) — RULE-CBP-014
      • atomicidade de publicação (sem estado parcial observável) — RULE-CBP-013
  - Regras do Blackboard (vigentes): governance/RULES.md —
      • RULE-BB-001 (comunicação EXCLUSIVAMENTE via Blackboard; o Event Bus NOTIFICA, não substitui o
        canal de estado — l.308-310)
      • RULE-BB-004 (append-only; objetos SUPERSEDED, nunca deletados — l.323-325) — a notificação é
        best-effort SOBRE esse log durável
      • RULE-BB-005 (Orchestrator/Manager APENAS coordena; não analisa — l.327-329) — fronteira SPEC-008:
        o Event Bus transporta, não orquestra (quem reage/quando é do Manager)
  - Objetos canônicos cujos eventos são PROPAGADOS (fronteira — NÃO redefinidos): CHM-001 (BASELINE)
    eventos de ciclo de vida da hipótese; CEM-001 (BASELINE) eventos canônicos "Evidence Created/
    Superseded/Invalidated/Archived" propagados pela "infraestrutura oficial… EC-COG-005 — Cognitive
    Event Bus" (canon/CEM-001 l.717-727; "O CEM não define o comportamento interno dessa infraestrutura");
    CCM-001 (BASELINE) objeto Conviction Vector 8D (só notificado, nunca computado — INV-04)
  - Camada a montante: SPEC-001 v1.1 (BASELINE) — EARS 8 "emitir evento 'Hypothesis.Created' no Event Bus"
    (specs/features/SPEC-001/plan.md l.159, l.367); l.75 DELEGA à SPEC-005 o "Orçamento de latência e entrega
    do Event Bus" e os metadados de transporte (o produtor não tem autoridade para defini-los — SAS-001 §6.10)
  - Contratos de agente (fronteira — NÃO redefinidos): SAS-001 §6.9 (Integração com Event Bus: publicações/
    consumos permitidos; "eventos transportam fatos — nunca decisões finais"); SAS-001 §6.10 (Metadados
    Operacionais de Infraestrutura: Freshness/Latency/Reliability/Expiration definidos pelos componentes de
    transporte — i.e., a SPEC-005; "o Structural Agent não possui autoridade para definir tais metadados")
  - Fundação constitucional (fronteira): CONSTITUTION.md l.235 (EC-COG-005 — Cognitive Event Bus);
    GPR-001 l.456-457 ("Blackboard → Event Bus → Bot Trade Finance"); INV-05 (SOT não executa ordem)
  - Método: atomic-spec.md v1.5 (BASpec, D0–D9, EARS, Enforcement E0–E3/F.1–F.4, TRACE-06, Quality Gates
    L1–L4 §7, Classe/Mecanismo §10.6, RULE-MM)
  - Governança/Avaliação/Maturidade: SPEC-019 v1.0 (RULE-HG-01..08, RULE-HV-01..04); SPEC-020 v1.0
    (9 lentes/RULE-EV-01..07); SPEC-021 v1.0 (RULE-MM-01..07; nível-alvo L3; gate E3 RULE-MM-05)
  - Enforcement: ENF-01..08 (ênfase ENF-03 Detector≠Gate; ENF-04 fail-closed; ENF-07 falso-DENY no E3)
  - Invariantes: INV-05 (SOT não executa; transporta a notificação do Signal Package, não a ordem),
    INV-06 (Evidência≠Observação), INV-07 (versionamento monotônico — herdado da SPEC-004), INV-09
    (sem baseline informal), INV-10 (CEM-001 idioma canônico)
  - Setup operacional (fronteira soberana, NÃO redefinida): WORKFLOW.md (versão vigente) — WF-A03 (morte
    do alarme: cancelamento quando a hipótese-origem passa a SUPERSEDED/REFUTED — l.55); WF-F02 (FSM
    determinística do ciclo — l.71); WF-F01 ramo (3)/(5) (reset do alarme); a SPEC-005 cita por ID, NÃO
    contradiz nenhum WF-xx e NÃO fecha WF-D03

ADDED (delta local — o que esta spec acrescenta; NÃO coberto pela SPEC-004 — ver "Cobertura × lacuna"):
  - Contrato do EVENTO (≠ objeto do Blackboard): envelope (event_id, event_type, origin, timestamp,
    correlation_id, causation_id, source_ref = object_id@version + seq + workspace, schema_version)
  - Propagação/notificação de mudança sobre o log append-only: CURSOR de consumo (último seq processado
    por consumidor) + catch-up/replay de NOTIFICAÇÕES a partir do cursor
  - Idempotência de CONSUMO / dedupe por chave de evento (DISTINTA da idempotência de ESCRITA da SPEC-004)
  - Ordenação OBSERVADA pelo consumidor (total intra-workspace herdada do seq; parcial/causal entre workspaces)
  - Semântica de entrega: at-least-once como PISO; retry com bounded loop; DEAD-LETTER obrigatório em falha
    persistente
  - Fail-safe "transporte ≠ fonte de verdade": perda de notificação NUNCA perde estado; recuperação sempre
    pelo cursor sobre o log (SPEC-004); push é otimização best-effort
  - Entrega a consumidor AUTORIZADO (declaração de interesse/subscrição — sem assumir orquestração)
  - Canal de SAÍDA da notificação do Signal Package à fronteira externa (Bot Trade Finance) — transporte da
    notificação, respeitando INV-05 (o contrato do Signal Package em si é RISK-M5/RISK-SPEC-022)
  - Metadados de transporte / ORÇAMENTO DE LATÊNCIA (Freshness/Latency/Reliability/Expiration — SAS-001 §6.10):
    a SPEC-005 é a DONA; o valor é PARÂMETRO a calibrar — [DECISÃO NECESSÁRIA]/INDETERMINADO, sem número
    arbitrário (não toca J-001/N-001)
  - Observabilidade do transporte (latência, perdas, dead-letter) — insumo para SPEC-040
  - [PROPOSTA] Distinção formal Blackboard↔Event Bus (resolve EVENT-BUS-001) — NÃO fechada (decisão de Andraus)
  - Declaração de Classe/Mecanismo por BASpec (CC-11); Enforcement Contracts (EC-CEB-001..005)

MODIFIED (especialização de regra herdada):
  - (nenhuma) — RULE-BB-001/004/005 são operacionalizadas no eixo de TRANSPORTE (notificação), não alteradas
    em texto nem significado (RULE-HD-02 respeitada). A SPEC-004 não é tocada (INV-09).

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal /
> obrigação-a-obrigação** sobre **regras (RULE-BB), a SPEC-004 vizinha e modelos canônicos** (EUA-E04 §8.3).
> O eixo **VERTICAL** (RULE-HV-01..04, conservação-como-conjunto pai→filha macro-harness) foi avaliado e
> **não se aplica**: a SPEC-005 não é decomposição *micro* de uma *macro-spec* — deriva de regras, da SPEC-004
> e de objetos canônicos vizinhos. A regra ESCRITA de conservação-como-conjunto vertical será redigida junto
> da SPEC-019/derivadas (EUA-E17 Q1, escopo já homologado); aqui não é invocada. [INFERÊNCIA — a confirmar pelo Revisor]

### Cobertura × lacuna da SPEC-004 v1.2 (BASELINE) — não duplicar (CC-02/INV-09)

| Capacidade | Coberta pela SPEC-004 v1.2? (arquivo:linha) | Tratamento na SPEC-005 |
|---|---|---|
| Ordem de commit / `seq` por workspace | **SIM** — RULE-CBP-006 (`SPEC-004/plan.md` l.258-262); ordem total persistida/imutável | **HERDADA** — o cursor e o ordering observado pelo consumidor **reusam** o `seq`; não se cria ordem nova |
| Idempotência de ESCRITA | **SIM** — RULE-CBP-005 (`SPEC-004/plan.md` l.249-256); chave + `request_fingerprint` | **DISTINTA** — a SPEC-005 adiciona idempotência de **CONSUMO** (dedupe do consumidor por chave de evento); não reabre a de escrita |
| Replay / reconstrução do estado lógico | **SIM** — RULE-CBP-011 (`SPEC-004/plan.md` l.288-294) | **HERDADA** — a SPEC-005 faz replay de **NOTIFICAÇÕES** a partir do cursor; a reconstrução de estado é da SPEC-004 |
| Identidade autenticada | **SIM** — RULE-CBP-014 (`SPEC-004/plan.md` l.311-319) | **HERDADA** — a entrega a consumidor autorizado reusa a identidade autenticada do runtime; não se define auth nova |
| Supersessão / `supersedes`·`derived_from` | **SIM** — RULE-CBP-003/INV-CBP-01 (`SPEC-004/plan.md` l.229-237) | **HERDADA** — o evento referencia `object_id@version`; o Event Bus propaga, não versiona estado |
| `schema_version`, atomicidade de publicação | **SIM** — RULE-CBP-001/013 (`SPEC-004/plan.md` l.214-222, l.302-309) | **HERDADA** no `source_ref`; o envelope do evento tem seu próprio `schema_version` (de transporte) |
| **Evento / envelope / origem / destino / subscrição** | **NÃO** | **LACUNA CENTRAL — ADDED** (CEB-001/002/008) |
| **Cursor de consumo / dedupe de entrega** | **NÃO** | **LACUNA — ADDED** (CEB-003/004) |
| **Ordering observado pelo consumidor (cross-workspace)** | Parcial (só intra-workspace via `seq`) | **LACUNA — ADDED** (CEB-005: parcial/causal entre workspaces) |
| **TTL / retry / dead-letter / delivery** | **NÃO** | **LACUNA — ADDED** (CEB-006) |
| **Fail-safe transporte ≠ fonte de verdade** | Implícito (log é a verdade) | **ADDED — torna explícito** (CEB-007) |
| **Canal de saída externo (Signal Package)** | **NÃO** | **LACUNA — ADDED** (CEB-009; E3; INV-05) |
| **Latência / metadados de transporte** | **NÃO** (`SPEC-001/plan.md` l.75 delega à SPEC-005; SAS-001 §6.10) | **LACUNA — ADDED** (CEB-010; PARÂMETRO a calibrar) |
| **Relação Blackboard↔Event Bus (distinção formal)** | Parcial (fronteira declarada) | **ADDED — [PROPOSTA]** (CEB-012; resolve EVENT-BUS-001, não fecha) |

---

## Declaração de acepção semântica (RULE-SEM-01 — CC-10)

> **Termo 1:** "Evento" (SPEC-005) = **mudança notificada**, transporte best-effort sobre o log. **≠ "Objeto"**
> (SPEC-004) = **estado versionado durável** (fonte de verdade). O evento **referencia** o objeto (`source_ref =
> object_id@version + seq + workspace`); não o substitui nem o guarda.
> **Termo 2:** "entrega/notificação" (transporte — SPEC-005) **≠ "publicação/commit"** (de estado no Blackboard —
> SPEC-004). Perder uma notificação não perde estado (recupera-se pelo cursor); perder um commit perderia estado
> (impossível — SPEC-004 é append-only durável).
> **Termo 3:** "idempotência de consumo" (dedupe do consumidor por chave de evento — SPEC-005) **≠ "idempotência
> de escrita"** (chave + `request_fingerprint` no commit — SPEC-004, RULE-CBP-005). São camadas distintas.
> **Termo 4:** "Observação" (produzida por Skill, determinística — INV-06) **≠ "Evidência"** (produzida por Agente).
> O Event Bus propaga eventos sobre ambas, sem confundi-las.
> [FONTE: RULE-SEM-01/04; INV-06; GLOSSARIO; SPEC-004 v1.2]

---

## Conformidade com o `WORKFLOW.md` (RULE-ECC-05 — determinação de NÃO-incidência)

> **Determinação: RULE-ECC-05 (Pesquisa Multi-Lente) NÃO INCIDE sobre a SPEC-005** [FONTE: DHR-SPEC005-001 §2 —
> "RULE-ECC-05 não incide, confirmado pelo Revisor"; research.md §7]. Fundamento: a SPEC-005 **não define nem toca
> comportamento de agente analítico, do Conviction/Fusion Engine, do Manager (decisão) ou do Risk Agent** — é
> infraestrutura de transporte/notificação, análoga às Specs de meta-harness/infra excluídas (SPEC-002/004/019/020/021).
> **Mesmo não incidindo, por prudência confirma-se conformidade:** o Event Bus serve a FSM do ciclo (**WF-F02**,
> `WORKFLOW.md` l.71) e gatilhos como **WF-A03** (morte do alarme quando a hipótese-origem passa a SUPERSEDED/REFUTED,
> l.55) e os resets de alarme de **WF-F01** (l.70). **Cita por ID**, **não contradiz** nenhum `WF-xx` e **não fecha**
> `WF-D03` (não computa convicção/J-001). Autoridade soberana do `WORKFLOW.md` preservada; divergência seria achado
> do Revisor, resolvida por Andraus. [FONTE: research.md §7; WORKFLOW.md l.55/l.70/l.71]

---

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide** (DHR-SPEC005-001 §2; ABERTURA §6). O Cognitive Event Bus é **infraestrutura de transporte/
notificação agnóstica de escola** — não define escopo de especialidade de mercado (Elliott/SMC/ICT). Nenhum `PD-xx`
é proposto (CC-12 = N/A). Registrado explicitamente para o Revisor — não é supressão silenciosa. [FONTE: RULE-PD-01;
atomic-spec §10.7; DHR-SPEC005-001 §2]

---

## D0 — Missão (Intenção)

A SPEC-005 especifica **como o SOT notifica consumidores sobre mudanças de estado já comprometidas no Blackboard
(SPEC-004) e como transporta a notificação do Signal Package à fronteira externa** — definindo o **contrato do
EVENTO** (envelope, origem, timestamp, correlation/causation ID, referência ao objeto/versão/seq que o originou),
a **propagação por cursor** sobre o log append-only (catch-up/replay de notificações), a **semântica de entrega**
(at-least-once como piso, retry com bounded loop, dead-letter, idempotência de **consumo**), a **ordenação observada
pelo consumidor**, a **entrega a consumidor autorizado**, o **canal de saída externo do Signal Package** e os
**metadados/orçamento de latência de transporte** — preservando o princípio **transporte ≠ fonte de verdade**: a
durabilidade, a ordem de commit, a idempotência de escrita, o replay e a supersessão **de estado** são da **SPEC-004
(BASELINE)**, nunca reintroduzidos aqui; e **INV-05** (o SOT não executa ordem; a SPEC-005 transporta a notificação,
o Bot Trade Finance executa). [FONTE: ROADMAP §5; CEM-001 l.717-727; SPEC-001 l.75; SAS-001 §6.9/§6.10; research.md §3]

**O que a Missão NÃO é (fronteira):**
- Não **guarda estado** / não é fonte de verdade / não versiona objeto → **SPEC-004 (Blackboard, BASELINE)**. Princípio: *"Blackboard guarda estado; Event Bus transporta mudanças."*
- Não é **memória permanente** / ontologia / grafo → **SPEC-006 (Knowledge Graph)**; **H-001 (ABERTA)** — não tocar.
- Não define **estado persistente por agente** → **SPEC-009**; **G-001 (ABERTA)** — não tocar.
- Não **orquestra** (quem reage, quando, em que ordem é invocado) → **SPEC-008 (Manager)**; o Event Bus transporta, não decide invocação (RULE-BB-005; WORKFLOW FSM WF-F02).
- Não **redefine** CHM-001/CEM-001/CCM-001 nem a **SPEC-004** → **CC-02/CONST-01/INV-09**.
- Não **computa** convicção nem fixa fórmula/pesos/limiares → **SPEC-003/CCM-001**; **J-001/N-001 ABERTAS**.
- Não especifica o **contrato do Signal Package** (campos, validação de sinal, execução) → **RISK-M5/RISK-SPEC-022** (a SPEC-005 só transporta a **notificação**, respeitando INV-05).
- Não constrói um **broker durável paralelo** (Opção C) → **ADIADA** (DHR-SPEC005-001 §2; reavaliável com múltiplos consumidores distribuídos/alta vazão).

**Status epistemológico:** a SPEC-005 é FATO ARQUITETURAL candidato a baseline; RULE-CEB-* e o contrato de evento por ela propostos são **[PROPOSTA]** até homologação. SPEC-004 v1.2, RULE-BB-001/004/005, CHM-001, CEM-001, CCM-001, SPEC-001/019/020/021, atomic-spec v1.5, INV-*, ENF-*, RULES v1.5 são FATO NORMATIVO. Fontes externas (research.md §2, SRC-*/REPO-*) são [EXTERNO] — DADO, nunca baseline; documentado ≠ homologado (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | **Contrato do EVENTO (envelope):** `event_id`, `event_type`, `origin`, `timestamp`, `correlation_id`, `causation_id`, `source_ref` (object_id@version + seq + workspace), `schema_version` de transporte; rejeita evento malformado | CEM-001 l.717-727; research.md §3.1 |
| S2 | **Correlation / causation:** `causation_id` = `event_id` do evento causador; `correlation_id` preservado ao longo de uma cadeia (rastreabilidade de causa) | research.md §3.1; P13 |
| S3 | **Cursor de consumo:** cada consumidor registra o último `seq` processado; catch-up/replay de notificações a partir do cursor | SRC-ES-01 [EXTERNO]; research.md §3.3; SPEC-004 RULE-CBP-006 |
| S4 | **Idempotência de consumo / dedupe:** o consumidor deduplica por chave de evento (DISTINTA da idempotência de escrita da SPEC-004) | research.md §3.3; SRC-NOTIFY-01 [EXTERNO] |
| S5 | **Ordenação observada pelo consumidor:** total intra-workspace (herdada do `seq`); parcial/causal entre workspaces (sem forçar ordem global ambígua) | research.md §3.3; SPEC-004 RULE-CBP-006 |
| S6 | **Semântica de entrega:** at-least-once como PISO; retry com bounded loop; DEAD-LETTER obrigatório em falha persistente | research.md §3.4; SRC-NOTIFY-01 [EXTERNO] |
| S7 | **Fail-safe transporte ≠ fonte de verdade:** perda de notificação nunca perde estado; recuperação sempre pelo cursor sobre o log; push é otimização best-effort | research.md §3.2/§3.4; RULE-BB-004 |
| S8 | **Entrega a consumidor autorizado:** declaração de interesse/subscrição; entrega só a consumidores autorizados (reusa identidade autenticada do runtime — SPEC-004 RULE-CBP-014) | RULE-BB-002/CBP-014; SAS-001 §6.9 |
| S9 | **Canal de saída externo do Signal Package:** transporte da notificação à fronteira externa (Bot Trade Finance); E3 fail-closed; INV-05 (SOT não executa ordem) | GPR-001 l.457; INV-05 |
| S10 | **Metadados de transporte / orçamento de latência:** Freshness/Latency/Reliability/Expiration (SPEC-005 é dona); valor = PARÂMETRO a calibrar ([DECISÃO NECESSÁRIA]/INDETERMINADO) | SPEC-001 l.75; SAS-001 §6.10 |
| S11 | **Observabilidade do transporte:** latência, perdas, dead-letter observáveis — insumo para SPEC-040 | research.md §3; ROADMAP §18 |
| S12 | **Distinção formal Blackboard↔Event Bus [PROPOSTA]:** resolve EVENT-BUS-001 (não fecha — decisão de Andraus) | DHR-SPEC005-001 §3; research.md §3.1 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Durabilidade/ordem/idempotência de escrita/replay/supersessão **de estado** | **SPEC-004 (BASELINE)** | já baselined; "transporte ≠ fonte de verdade"; CC-02/INV-09 |
| Broker durável próprio (pub/sub Kafka/RabbitMQ-like, 24/7) | — (**ADIADO** — Opção C) | over-engineering sob escritor único + VPS + log durável existente (research.md §3.5/§3.6); reavaliável com múltiplos consumidores distribuídos/alta vazão |
| Memória permanente / ontologia / grafo | **SPEC-006 (KG)** — **H-001 ABERTA** | KG é memória permanente |
| Estado persistente **por agente** | **SPEC-009** — **G-001 ABERTA** | persistência por agente |
| Orquestração (quem reage, quando, em que ordem é invocado) | **SPEC-008 (Manager)** | controle ≠ transporte (RULE-BB-005; WORKFLOW FSM) |
| Contrato do Signal Package (campos, validação de sinal, execução de ordem) | **RISK-M5 / RISK-SPEC-022** | INV-05; a SPEC-005 só transporta a notificação |
| Redefinir CHM-001 / CEM-001 / CCM-001 / SPEC-004 | canônicos/baseline | **CC-02/CONST-01/INV-09** — só propagar/notificar |
| Fórmula/pesos/limiares de convicção | **SPEC-003/CCM-001; J-001/N-001 ABERTAS** | INV-03/INV-04; o Event Bus não computa convicção |
| Mecanismo físico de transporte (push/poll/LISTEN-NOTIFY, fila interna) | — | **INDETERMINADO** até BUILD (D4/D5); define-se o QUE, não o COMO |
| Valor numérico fixo do orçamento de latência | — (**PARÂMETRO a calibrar**) | **[DECISÃO NECESSÁRIA]/INDETERMINADO** — sem número arbitrário (RULE-MET-01); não toca J-001/N-001 |

---

## D2 — Regras

> **Etiqueta:** as RULE-CEB-* e o contrato de evento abaixo são **[PROPOSTA]** — tornam-se normativos apenas na
> homologação de Andraus + registro pelo Controlador (RULE-HG-02). As RULE/INV/ENF citadas como fundamento
> (SPEC-004 RULE-CBP-*, RULE-BB-001/004/005, INV-05/06/07/09/10, ENF-03/04/07, CEM-001, CHM-001, CCM-001) **já existem**
> e são FATO NORMATIVO.

```
RULE-CEB-001: Todo evento transportado DEVE carregar o envelope mínimo — event_id, event_type, origin, timestamp,
              correlation_id, causation_id, source_ref (object_id@version + seq + workspace do Blackboard) e
              schema_version de transporte. Evento sem o envelope mínimo é REJEITADO (fail-closed), não propagado.
              O envelope NÃO duplica o objeto: referencia-o por source_ref (transporte ≠ fonte de verdade).
              [Fonte: CEM-001 l.717-727; research.md §3.1; SPEC-004 RULE-CBP-001/006]  [PROPOSTA]

RULE-CEB-002: Todo evento DEVE preservar a cadeia causal: causation_id aponta para o event_id do evento que o
              causou (ou nulo, se raiz); correlation_id é preservado ao longo de toda a cadeia derivada. A cadeia
              DEVE ser reconstruível (P13).
              [Fonte: P13; RULE-010; research.md §3.1]  [PROPOSTA]

RULE-CEB-003: Cada consumidor DEVE manter um CURSOR (último seq processado por workspace). O catch-up/replay de
              notificações a partir do cursor DEVE reusar a ordem total de COMMIT do log (SPEC-004 RULE-CBP-006) —
              o Event Bus NÃO cria ordem própria de estado. A notificação push é OTIMIZAÇÃO best-effort; a
              recuperação canônica é sempre pelo cursor sobre o log.
              [Fonte: SRC-ES-01 [EXTERNO]; SPEC-004 RULE-CBP-006/011; research.md §3.3]  [PROPOSTA]

RULE-CEB-004: O consumo DEVE ser idempotente: o consumidor deduplica por chave de evento (ex.: event_id ou
              (source_ref, event_type)), de modo que o reprocessamento de um evento já consumido NÃO produza
              efeito duplicado. Esta idempotência de CONSUMO é DISTINTA da idempotência de ESCRITA da SPEC-004
              (RULE-CBP-005) — não a reabre nem a substitui.
              [Fonte: research.md §3.3; SRC-NOTIFY-01 [EXTERNO]; SPEC-004 RULE-CBP-005]  [PROPOSTA]

RULE-CEB-005: A ordem OBSERVADA pelo consumidor DEVE ser total DENTRO de um workspace (herdada do seq — SPEC-004)
              e, ENTRE workspaces, parcial/causal (respeitando causation_id). O Event Bus NÃO DEVE impor nem
              prometer uma ordem total global ambígua; eventos sem relação causal podem ser entregues em ordem
              relativa indefinida sem violar a garantia.
              [Fonte: SPEC-004 RULE-CBP-006; research.md §3.3]  [PROPOSTA]

RULE-CEB-006: A entrega DEVE ser at-least-once como PISO. O retry DEVE ter bounded loop (critério de parada
              explícito — nº máximo de tentativas e/ou janela), NUNCA retry infinito. Após esgotar o retry, o
              evento DEVE ir para DEAD-LETTER (registro observável), nunca descartado em silêncio. Combinada com
              a idempotência de consumo (RULE-CEB-004), a garantia efetiva de processamento é exatamente-uma-vez.
              [Fonte: SRC-NOTIFY-01 [EXTERNO]; research.md §3.4; ENF-04]  [PROPOSTA]

RULE-CEB-007: TRANSPORTE ≠ FONTE DE VERDADE (invariante local INV-CEB-01). A perda, duplicação ou atraso de uma
              NOTIFICAÇÃO NUNCA DEVE causar perda de ESTADO: o estado durável, a ordem e o histórico são do log
              append-only da SPEC-004. Em qualquer falha de transporte, a recuperação DEVE ser possível por replay
              a partir do cursor sobre o log (SPEC-004 RULE-CBP-011). O Event Bus NÃO DEVE ser usado como armazém
              de estado autoritativo nem substituir o canal de estado (RULE-BB-001).
              [Fonte: RULE-BB-001/004; SPEC-004 RULE-CBP-011; research.md §3.2/§3.6]  [PROPOSTA]

RULE-CEB-008: A entrega DEVE ocorrer apenas a consumidores AUTORIZADOS, conforme declaração de interesse/subscrição.
              A autorização reusa a identidade AUTENTICADA pelo runtime (SPEC-004 RULE-CBP-014); o Event Bus NÃO
              decide QUEM é invocado NEM QUANDO (isso é orquestração = Manager/SPEC-008, RULE-BB-005) — apenas
              entrega a quem declarou interesse e está autorizado. O gate de autorização é determinístico (ENF-03).
              [Fonte: RULE-BB-002/005; SPEC-004 RULE-CBP-014; SAS-001 §6.9; ENF-03]  [PROPOSTA]

RULE-CEB-009: O canal de SAÍDA da notificação do Signal Package à fronteira externa (Bot Trade Finance) é E3
              (efeito externo irreversível). A emissão externa DEVE ser fail-closed: se o canal/consumidor não é
              autorizado, ou a notificação não é bem-formada, NÃO emite. O SOT NÃO executa ordem (INV-05): a
              SPEC-005 transporta a NOTIFICAÇÃO; o contrato do Signal Package em si é RISK-M5/RISK-SPEC-022 (não
              reaberto aqui). A unidade E3 declara método amostral de observação de falso-DENY (ENF-07); o limiar
              é gap de enforcement aberto, não fixado aqui.
              [Fonte: GPR-001 l.457; INV-05; ENF-04/07; RISK-M5]  [PROPOSTA]

RULE-CEB-010: A SPEC-005 é a DONA dos metadados de transporte (Freshness/Latency/Reliability/Expiration — SAS-001
              §6.10; SPEC-001 l.75 delega). O ORÇAMENTO de latência/entrega por tipo de consumidor sensível a tempo
              DEVE ser declarado como PARÂMETRO a calibrar — [DECISÃO NECESSÁRIA]/INDETERMINADO; NENHUM número
              arbitrário é fixado neste Plan (RULE-MET-01). O parâmetro NÃO toca J-001/N-001. Onde o consumidor é
              sensível a tempo (ex.: notificação do Signal Package / morte de alarme WF-A03), a latência é material
              e DEVE ser observável (SPEC-040).
              [Fonte: SPEC-001 l.75; SAS-001 §6.10; RULE-MET-01]  [PROPOSTA / DECISÃO NECESSÁRIA]

RULE-CEB-011: O transporte DEVE ser observável: latência de entrega, perdas/reentregas e ocupação da dead-letter
              DEVEM ser registradas para auditoria (insumo da SPEC-040). O mecanismo FÍSICO de transporte
              (push/poll/LISTEN-NOTIFY, fila interna) é COMO (BUILD), NÃO fixado aqui — INDETERMINADO.
              [Fonte: ROADMAP §18; research.md §3; RULE-MET-01]  [PROPOSTA]

RULE-CEB-012: [PROPOSTA de resolução de EVENT-BUS-001 — NÃO fecha] O Event Bus distingue-se do Blackboard assim:
              o Blackboard GUARDA estado (fonte de verdade durável, append-only — SPEC-004); o Event Bus
              TRANSPORTA/NOTIFICA mudanças desse estado (best-effort, sobre o log). O Event Bus é um PROCESSO
              SEPARADO de notificação, NÃO um segundo armazém de estado. Esta distinção RESOLVE a questão
              EVENT-BUS-001 apenas como PROPOSTA — a decisão é de Andraus na homologação (CONS-01). O Doc 13
              (ENGENHARIA-GERAL) "tudo via Event Bus" é fundamento HISTÓRICO não-normativo, superado quanto ao
              canal de estado por RULE-BB-001/SPEC-004 (TRACE-06).
              [Fonte: ROADMAP §5; RULE-BB-001; CEM-001 l.725; DHR-SPEC005-001 §3; research.md §3.1/§3.6]  [PROPOSTA / DECISÃO NECESSÁRIA]
```

> **Invariante local desta Spec [PROPOSTA]:**
> **INV-CEB-01 (Transporte ≠ fonte de verdade):** nenhuma garantia de estado do SOT pode depender da entrega do
> Event Bus; a perda/duplicação/atraso de uma notificação é sempre recuperável por replay do cursor sobre o log
> append-only (SPEC-004). Reforça — não redefine — RULE-BB-001/004 e INV-07. [PROPOSTA]

---

## Critérios de Aceitação (EARS)

1. Quando um evento é submetido para transporte, o Event Bus DEVE propagá-lo somente se carrega o envelope mínimo (event_id, event_type, origin, timestamp, correlation_id, causation_id, source_ref, schema_version) e DEVE rejeitar (fail-closed) evento sem esses campos, sem propagar.
2. Quando um evento é derivado de outro, o Event Bus DEVE preencher causation_id com o event_id do evento causador e preservar o correlation_id ao longo da cadeia.
3. Quando um consumidor precisa processar notificações após ficar offline, o Event Bus DEVE permitir catch-up a partir do cursor do consumidor reusando a ordem de COMMIT do log (SPEC-004) e NÃO DEVE perder eventos entre o cursor e o fim do log.
4. Quando o mesmo evento é entregue mais de uma vez (at-least-once), o consumidor DEVE deduplicá-lo por chave de evento e NÃO DEVE produzir efeito duplicado.
5. Quando um consumidor observa eventos, o Event Bus DEVE garantir ordem total dentro de um workspace (herdada do seq) e ordem parcial/causal entre workspaces, e NÃO DEVE prometer ordem total global ambígua.
6. Quando a entrega de um evento falha, o Event Bus DEVE reentregar sob retry de bounded loop (nunca infinito) e, esgotado o retry, DEVE roteá-lo para dead-letter observável, e NÃO DEVE descartá-lo em silêncio.
7. Quando uma notificação é perdida, duplicada ou atrasada, o Event Bus NÃO DEVE causar perda de estado: a recuperação DEVE ser possível por replay do cursor sobre o log append-only (SPEC-004).
8. Quando um evento deve ser entregue, o Event Bus DEVE entregá-lo apenas a consumidores autorizados (identidade autenticada do runtime) e NÃO DEVE decidir quem é invocado nem quando (orquestração = Manager).
9. Quando uma notificação de Signal Package deve ir à fronteira externa, o Event Bus DEVE emiti-la somente se o canal/consumidor é autorizado e a notificação é bem-formada (E3 fail-closed), e o SOT NÃO DEVE executar ordem (INV-05).
10. Quando um consumidor sensível a tempo recebe notificação, o Event Bus DEVE anexar metadados de transporte e respeitar o orçamento de latência declarado como PARÂMETRO a calibrar, e NÃO DEVE fixar número arbitrário de latência no Plan.
11. Quando eventos são transportados, reentregues ou vão para dead-letter, o Event Bus DEVE registrar observabilidade (latência/perdas/dead-letter) para auditoria.
12. Quando um consumidor pede estado autoritativo, o Event Bus NÃO DEVE servi-lo como fonte de verdade e DEVE apontar ao Blackboard (SPEC-004); a distinção formal (EVENT-BUS-001) permanece ABERTA.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec com efeito declara o bloco **CLASSE/MECANISMO** (§10.6). D = determinístico; C = constitutivo
> (é o próprio gate). Não há Classe H/P normativa nesta Spec (gates são determinísticos; eventual juízo de
> "evento bem-formado" é orientação de BUILD — detector, nunca gate, ENF-03).

### BASpec-CEB-001 — Envelope de evento (rejeita evento malformado)

```
BASpec-CEB-001:
  QUANDO:       Um evento é submetido para transporte/notificação
  ENTÃO:        O Event Bus propaga somente se o evento carrega o envelope mínimo (event_id, event_type, origin,
                timestamp, correlation_id, causation_id, source_ref=object_id@version+seq+workspace, schema_version);
                evento sem o envelope é rejeitado (fail-closed), não propagado; o envelope referencia o objeto por
                source_ref e NÃO duplica seu conteúdo de estado
  PORQUE:       Evento sem envelope/referência não é rastreável (P13) e poderia virar um segundo armazém de estado
                (viola transporte ≠ fonte de verdade)
  REFERÊNCIA:   RULE-CEB-001; CEM-001 l.717-727; SPEC-004 RULE-CBP-001
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : validação determinística dos campos do envelope + presença de source_ref; rejeição se faltar
    CRITÉRIO 4Es: Eficácia — integridade/rastreabilidade do transporte; determinismo garante reprodutibilidade (P13)
  VERIFICADO POR:
    DADO        um evento submetido sem source_ref (sem referência a object_id@version)
    QUANDO      o transporte processa
    ENTÃO       evento rejeitado; nada propagado
    VERIFICAÇÃO event_propagated == false; rejected_reason == "ENVELOPE_INCOMPLETE"
```

### BASpec-CEB-002 — Correlation / causation (cadeia causal reconstruível)

```
BASpec-CEB-002:
  QUANDO:       Um evento é derivado de outro (ex.: "Alarm.Cancelled" causado por "Hypothesis.Superseded")
  ENTÃO:        O Event Bus exige causation_id apontando para o event_id do evento causador e preserva o
                correlation_id ao longo da cadeia; a cadeia causal é reconstruível
  PORQUE:       Rastreabilidade causal (P13) permite auditar por que uma notificação ocorreu
  REFERÊNCIA:   RULE-CEB-002; P13; RULE-010
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : propagação determinística de correlation_id + atribuição de causation_id = event_id do causador
    CRITÉRIO 4Es: Eficácia — auditabilidade da cadeia de eventos
  VERIFICADO POR:
    DADO        evento E2 derivado de E1
    QUANDO      E2 é construído
    ENTÃO       E2.causation_id == E1.event_id; E2.correlation_id == E1.correlation_id
    VERIFICAÇÃO causation_chain_reconstructible == true
```

### BASpec-CEB-003 — Cursor de consumo (catch-up/replay a partir do cursor)

```
BASpec-CEB-003:
  QUANDO:       Um consumidor precisa processar notificações (inclusive após ficar offline)
  ENTÃO:        O Event Bus permite catch-up/replay a partir do CURSOR do consumidor (último seq processado por
                workspace), reusando a ordem total de COMMIT do log (SPEC-004); push é otimização best-effort, a
                recuperação canônica é pelo cursor sobre o log
  PORQUE:       Consumidor-com-cursor dá notificação de mudança sem armazém novo e sem perder eventos (SRC-ES-01)
  REFERÊNCIA:   RULE-CEB-003; SPEC-004 RULE-CBP-006/011; SRC-ES-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : leitura determinística do log a partir de (workspace, cursor_seq); avanço do cursor só após consumo
    CRITÉRIO 4Es: Eficácia — nenhuma mudança perdida; Eficiência — catch-up sem reprocessar tudo
  VERIFICADO POR:
    DADO        consumidor com cursor em seq=100; o log avançou até seq=120
    QUANDO      o consumidor faz catch-up
    ENTÃO       recebe as notificações de seq 101..120 na ordem do log; cursor avança para 120
    VERIFICAÇÃO delivered_range == [101,120]; ordered_by_seq == true; no_missed_event == true
```

### BASpec-CEB-004 — Idempotência de consumo (dedupe por chave de evento)

```
BASpec-CEB-004:
  QUANDO:       O mesmo evento é entregue mais de uma vez (at-least-once; reentrega após falha)
  ENTÃO:        O consumidor deduplica por chave de evento, de modo que o reprocessamento NÃO produz efeito
                duplicado; esta idempotência de CONSUMO é distinta da idempotência de ESCRITA da SPEC-004
  PORQUE:       At-least-once + dedupe de consumo = exatamente-uma-vez efetivo, sem reabrir a camada de escrita
  REFERÊNCIA:   RULE-CEB-004/006; SPEC-004 RULE-CBP-005; SRC-NOTIFY-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : deduplicação determinística por chave de evento (event_id / (source_ref,event_type))
    CRITÉRIO 4Es: Eficácia — evitar efeito duplicado; Eficiência — reentrega segura
  VERIFICADO POR:
    DADO        evento com event_id="EV-1" entregue duas vezes ao consumidor
    QUANDO      a segunda entrega é processada
    ENTÃO       nenhum efeito duplicado; a segunda é reconhecida como já consumida
    VERIFICAÇÃO duplicate_effect == false; dedup_hit == true
```

### BASpec-CEB-005 — Ordem observada pelo consumidor (total intra-workspace; parcial/causal entre workspaces)

```
BASpec-CEB-005:
  QUANDO:       Um consumidor observa eventos de um ou mais workspaces
  ENTÃO:        O Event Bus garante ordem TOTAL dentro de um workspace (herdada do seq — SPEC-004) e ordem
                PARCIAL/CAUSAL entre workspaces (respeitando causation_id); NÃO promete ordem total global ambígua
  PORQUE:       Forçar ordem total global sobre eventos sem relação causal seria ambíguo e não reconstruível
  REFERÊNCIA:   RULE-CEB-005; SPEC-004 RULE-CBP-006
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : ordenação por (workspace, seq) intra-workspace; por causation_id entre workspaces
    CRITÉRIO 4Es: Eficácia — ordem reconstruível sem falsa promessa de ordem global
  VERIFICADO POR:
    DADO        eventos A1,A2 (workspace A, seq 1,2) e B1 (workspace B) sem relação causal com A
    QUANDO      o consumidor os observa
    ENTÃO       A1 antes de A2 (total intra-workspace); B1 em ordem relativa indefinida com A (parcial)
    VERIFICAÇÃO intra_workspace_total_order == true; global_total_order_promised == false
```

### BASpec-CEB-006 — Entrega at-least-once, retry bounded, dead-letter obrigatório

```
BASpec-CEB-006:
  QUANDO:       A entrega de um evento a um consumidor falha
  ENTÃO:        O Event Bus reentrega (at-least-once) com retry de bounded loop (critério de parada explícito,
                nunca infinito); esgotado o retry, envia o evento para DEAD-LETTER (registro observável), nunca
                descarta em silêncio
  PORQUE:       Garantir entrega sem retry infinito; falha persistente visível (dead-letter) em vez de perda silenciosa
  REFERÊNCIA:   RULE-CEB-006; ENF-04; SRC-NOTIFY-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : política determinística de retry com limite + roteamento para dead-letter ao esgotar
    GATE DE SAÍDA: verificação (nº de tentativas ≤ limite ∧ evento não-entregue ⇒ dead-letter registrada)
    BOUNDED LOOP: nº máximo de tentativas e/ou janela temporal — parada explícita; retry infinito proibido
    CRITÉRIO 4Es: Conformidade > Eficácia — nenhuma notificação some em silêncio; parada garante Economicidade
  VERIFICADO POR:
    DADO        um evento cuja entrega falha além do limite de tentativas
    QUANDO      o retry se esgota
    ENTÃO       evento roteado para dead-letter; registro observável; sem descarte silencioso; sem retry infinito
    VERIFICAÇÃO dead_lettered == true; silent_drop == false; retries <= max_retries
```

### BASpec-CEB-007 — Transporte ≠ fonte de verdade (fail-safe pelo cursor sobre o log) [INV-CEB-01]

```
BASpec-CEB-007:
  QUANDO:       Uma notificação é perdida, duplicada ou atrasada (falha de transporte)
  ENTÃO:        Nenhum estado do SOT é perdido: a recuperação ocorre por replay a partir do cursor sobre o log
                append-only (SPEC-004); o Event Bus NÃO é fonte de verdade nem armazém de estado autoritativo
  PORQUE:       O estado durável/ordem/histórico são do Blackboard (RULE-BB-001/004); o transporte é best-effort
                sobre ele (transporte ≠ fonte de verdade — INV-CEB-01)
  REFERÊNCIA:   RULE-CEB-007; RULE-BB-001/004; SPEC-004 RULE-CBP-011; INV-CEB-01
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que proíbe o Event Bus de servir estado autoritativo; recuperação sempre pelo cursor
    GATE DE SAÍDA: verificação (fonte autoritativa de recuperação == log da SPEC-004, não o buffer de transporte)
    CRITÉRIO 4Es: Conformidade > Eficácia — garantia de não-perda de estado acima de desempenho de push
  VERIFICADO POR:
    DADO        notificações perdidas por queda do canal push durante uma janela
    QUANDO      o consumidor recupera
    ENTÃO       todo o estado é reconstruído por replay do cursor sobre o log; nada de estado é perdido
    VERIFICAÇÃO state_loss == false; recovered_via == "cursor_over_log"
```

### BASpec-CEB-008 — Entrega a consumidor autorizado (não orquestra)

```
BASpec-CEB-008:
  QUANDO:       Um evento deve ser entregue a consumidores que declararam interesse
  ENTÃO:        O Event Bus entrega apenas a consumidores AUTORIZADOS (identidade autenticada do runtime — SPEC-004);
                NÃO decide QUEM é invocado NEM QUANDO (orquestração = Manager/SPEC-008); entrega a quem subscreveu e
                está autorizado; consumidor não autorizado é recusado (fail-closed)
  PORQUE:       Transporte ≠ controle (RULE-BB-005); autorização não pode depender da honestidade do payload (CBP-014)
  REFERÊNCIA:   RULE-CEB-008; RULE-BB-002/005; SPEC-004 RULE-CBP-014; ENF-03
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de autorização por identidade autenticada + tabela de subscrição; LLM não é gate
    GATE DE SAÍDA: verificação (consumidor ∈ subscritos autorizados pela identidade autenticada)
    CRITÉRIO 4Es: Conformidade > Eficácia — entrega só a autorizado é inviolável
  VERIFICADO POR:
    DADO        consumidor não autorizado tenta receber um tipo de evento restrito
    QUANDO      o gate de entrega roda
    ENTÃO       entrega recusada "CONSUMER_NOT_AUTHORIZED"; o Event Bus não decidiu invocação (só entregou/recusou)
    VERIFICAÇÃO error_code == "CONSUMER_NOT_AUTHORIZED"; orchestration_decided == false
```

### BASpec-CEB-009 — Canal de saída externo do Signal Package (E3; INV-05)

```
BASpec-CEB-009:
  QUANDO:       Uma notificação de Signal Package deve ser transportada à fronteira externa (Bot Trade Finance)
  ENTÃO:        O Event Bus emite a NOTIFICAÇÃO somente se o canal/consumidor externo é autorizado e a notificação
                é bem-formada (fail-closed); o SOT NÃO executa a ordem (INV-05) — transporta a notificação, a
                execução é do Bot; o contrato do Signal Package em si é RISK-M5/RISK-SPEC-022 (não reaberto)
  PORQUE:       Emissão externa é irreversível (E3) e cruza a fronteira de confiança; INV-05 (SOT não executa ordem)
  REFERÊNCIA:   RULE-CEB-009; INV-05; GPR-001 l.457; ENF-04/07; RISK-M5
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de emissão externa (canal autorizado ∧ notificação bem-formada); fail-closed
    GATE DE SAÍDA: verificação (destino externo autorizado ∧ payload de notificação válido ∧ não é ordem de execução)
    CRITÉRIO 4Es: Conformidade > Eficácia — emissão externa irreversível exige fail-closed (ENF-04)
  VERIFICADO POR:
    DADO        notificação de Signal Package para um canal externo não autorizado
    QUANDO      o gate de emissão E3 roda
    ENTÃO       emissão negada (fail-closed); nada enviado à fronteira externa; falso-DENY amostrado (ENF-07)
    VERIFICAÇÃO external_emitted == false; fail_closed == true; order_executed_by_sot == false
```

### BASpec-CEB-010 — Metadados de transporte / orçamento de latência (parâmetro a calibrar)

```
BASpec-CEB-010:
  QUANDO:       Um consumidor sensível a tempo (ex.: Signal Package, morte de alarme WF-A03) recebe notificação
  ENTÃO:        O Event Bus anexa metadados de transporte (Freshness/Latency/Reliability/Expiration) e respeita o
                ORÇAMENTO de latência declarado como PARÂMETRO a calibrar; NENHUM número arbitrário é fixado neste
                Plan (o valor é [DECISÃO NECESSÁRIA]/INDETERMINADO até calibração; não toca J-001/N-001)
  PORQUE:       O produtor não tem autoridade sobre metadados de transporte (SAS-001 §6.10; SPEC-001 l.75 delega à
                SPEC-005); notificação que chega tarde perde relevância (4Es) — latência é material e observável
  REFERÊNCIA:   RULE-CEB-010; SAS-001 §6.10; SPEC-001 l.75; RULE-MET-01
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : anexo determinístico de metadados de transporte; orçamento = parâmetro configurável (não fixado)
    CRITÉRIO 4Es: Eficácia primeiro (não perder a mudança); Eficiência na latência; valor calibrado após medição
  VERIFICADO POR:
    DADO        notificação para consumidor sensível a tempo, com orçamento de latência configurado (parâmetro)
    QUANDO      a entrega ocorre
    ENTÃO       metadados de transporte anexados; latência observável; nenhum número fixado no Plan (parâmetro)
    VERIFICAÇÃO transport_metadata_present == true; latency_budget_is_parameter == true; hardcoded_latency == false
```

### BASpec-CEB-011 — Observabilidade do transporte (insumo SPEC-040)

```
BASpec-CEB-011:
  QUANDO:       Eventos são transportados, reentregues ou vão para dead-letter
  ENTÃO:        O Event Bus registra observabilidade (latência de entrega, perdas/reentregas, ocupação da
                dead-letter) para auditoria; o mecanismo físico de transporte (push/poll/LISTEN-NOTIFY) NÃO é
                fixado aqui (INDETERMINADO — BUILD)
  PORQUE:       Observabilidade do transporte é insumo da SPEC-040; o COMO é BUILD, não o QUE (contrato/invariantes)
  REFERÊNCIA:   RULE-CEB-011; ROADMAP §18; research.md §3
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : registro determinístico de métricas de transporte para auditoria
    CRITÉRIO 4Es: Efetividade — observar o transporte permite detectar degradação sem decidir pelo consumidor
  VERIFICADO POR:
    DADO        uma janela com reentregas e um evento em dead-letter
    QUANDO      a observabilidade roda
    ENTÃO       métricas de latência/perdas/dead-letter registradas; mecanismo físico não fixado
    VERIFICAÇÃO transport_observability_recorded == true; physical_mechanism_fixed == false
```

### BASpec-CEB-012 — Distinção Blackboard↔Event Bus (não guardar estado autoritativo) [PROPOSTA — EVENT-BUS-001 ABERTA]

```
BASpec-CEB-012:
  QUANDO:       Um consumidor precisa de estado autoritativo (não apenas da notificação de mudança)
  ENTÃO:        O consumidor lê o Blackboard (SPEC-004, fonte de verdade); o Event Bus NÃO serve estado
                autoritativo — ele só NOTIFICA que algo mudou; a distinção formal (proposta de resolução de
                EVENT-BUS-001) NÃO é fechada neste Plan (decisão de Andraus na homologação)
  PORQUE:       Transporte ≠ fonte de verdade (INV-CEB-01); o Event Bus é processo separado de notificação, não
                segundo armazém de estado; EVENT-BUS-001 permanece ABERTA (CONS-01)
  REFERÊNCIA:   RULE-CEB-012/007; RULE-BB-001; CEM-001 l.725; DHR-SPEC005-001 §3
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que proíbe o Event Bus de responder como fonte de estado autoritativo
    GATE DE SAÍDA: verificação (pedido de estado autoritativo ⇒ redirecionado ao Blackboard, não servido pelo bus)
    CRITÉRIO 4Es: Conformidade > Eficácia — não confundir transporte com fonte de verdade
  VERIFICADO POR:
    DADO        um consumidor consulta o Event Bus pedindo o estado corrente autoritativo de um objeto
    QUANDO      o pedido roda
    ENTÃO       o Event Bus não serve estado autoritativo; aponta ao Blackboard; EVENT-BUS-001 permanece ABERTA
    VERIFICAÇÃO authoritative_state_served_by_bus == false; event_bus_001_decision == "ABERTA"
```

---

## D4 — Algoritmo

Mecânicas **determinísticas reais** especificáveis (D4 "onde há regra determinística real" — atomic-spec §2). O mecanismo físico (push/poll/LISTEN-NOTIFY) é **INDETERMINADO** (BUILD); abaixo está a lógica, não a tecnologia:

- **Cursor / catch-up (CEB-003):** `para consumidor C no workspace W: entrega eventos com seq ∈ (cursor[C,W], max_seq(W)] em ordem de seq; cursor[C,W] := seq só após consumo confirmado`. Perda de push ⇒ recuperação por re-leitura a partir de `cursor[C,W]` sobre o log (SPEC-004).
- **Dedupe de consumo (CEB-004):** `se event_key ∈ consumed[C] ⇒ no-op (dedup_hit); senão processa e grava event_key em consumed[C]` — at-least-once + dedupe ⇒ exatamente-uma-vez efetivo. `event_key = event_id` (ou `(source_ref, event_type)`).
- **Correlation/causation (CEB-002):** `E_novo.causation_id := E_causa.event_id; E_novo.correlation_id := E_causa.correlation_id` (ou novo `correlation_id` se raiz).
- **Ordering observado (CEB-005):** intra-workspace `order := sort_by(seq)`; cross-workspace `order := ordem-parcial por causation_id` (eventos sem relação causal: ordem relativa indefinida, não ambígua).
- **Retry bounded + dead-letter (CEB-006):** `tentativas := 0; enquanto não-entregue ∧ tentativas < MAX: reentrega; tentativas += 1; se ainda não-entregue ⇒ dead_letter(evento)` — `MAX` é parâmetro (bounded loop; sem retry infinito).
- **Orçamento de latência (CEB-010):** `latency_budget[tipo_consumidor]` é **parâmetro a calibrar** — NÃO fixado (INDETERMINADO); a latência observada é medida e comparada ao parâmetro (SPEC-040).

Nenhuma fórmula depende de J-001/N-001 (o Event Bus não computa convicção). Nenhum limiar numérico de convicção nem de latência é fixado neste Plan. [FONTE: atomic-spec §2; research.md §3.3; RULE-MET-01]

---

## D5 — Máquina de estados (ciclo de vida do evento / entrega)

> **Fronteira (CC-02):** este é o ciclo do **EVENTO em transporte** (vida da notificação). Ele é **separado** do
> ciclo do **OBJETO no Blackboard** (publication_state / domain_state — SPEC-004) e da máquina de estados da
> **hipótese** (CHM-001) — **não redefinidos** aqui. O evento referencia o objeto; não o versiona.

Ciclo de vida do evento / entrega — `delivery_state` [PROPOSTA]:

| Estado | Descrição | Transições |
|---|---|---|
| EMITTED | Evento bem-formado, aceito para transporte (envelope válido — CEB-001) | → DELIVERING |
| DELIVERING | Em entrega a consumidor(es) autorizado(s) | → ACKED (consumo confirmado) · → RETRYING (falha) |
| RETRYING | Reentrega sob bounded loop (at-least-once; retry ≤ MAX) | → ACKED · → DEAD_LETTERED (esgotou retry) |
| ACKED | Consumido e deduplicado (idempotência de consumo — CEB-004) | terminal (observável) |
| DEAD_LETTERED | Falha persistente — registrado, nunca descartado em silêncio (CEB-006) | terminal (observável; reprocessável por decisão operacional) |
| REJECTED | Envelope inválido — não propagado (CEB-001) | terminal |

> **Nota de recuperação (INV-CEB-01):** qualquer estado de transporte perdido é **recuperável** por replay a partir
> do cursor sobre o log append-only da SPEC-004 — o `delivery_state` é do transporte, **não** é fonte de verdade de
> estado. [FONTE: RULE-CEB-007; SPEC-004 RULE-CBP-011]
> **O mecanismo FÍSICO (push/poll/LISTEN-NOTIFY, fila interna) = INDETERMINADO** (BUILD); a Opção C (broker durável)
> está ADIADA (não é este `delivery_state`). [FONTE: DHR-SPEC005-001 §2; research.md §3.5]

---

## D6 — Protocolo de notificação (sobre o log da SPEC-004)

### Produtores, consumidores e fronteira [FONTE: RULE-BB-001/005; CEM-001 l.725; SAS-001 §6.9]
- A **fonte** de todo evento é uma mudança **já comprometida** no log da SPEC-004 (commit atômico, seq atribuído). O Event Bus **não** origina estado.
- A **comunicação de estado** permanece exclusivamente via Blackboard (RULE-BB-001); o Event Bus **notifica** sobre ela.
- A **orquestração** (quem reage, quando, em que ordem é invocado) é do **Manager (SPEC-008)** (RULE-BB-005; WORKFLOW WF-F02) — o Event Bus entrega/notifica, não decide invocação.

### Sequência de notificação (um evento)
1. **Origem:** uma publicação commitada no Blackboard (SPEC-004, com `seq`) gera um evento candidato.
2. **Envelope (CEB-001):** monta `event_id`, `event_type`, `origin`, `timestamp`, `correlation_id`, `causation_id`, `source_ref=object_id@version+seq+workspace`, `schema_version`; envelope inválido ⇒ `REJECTED`.
3. **Cadeia causal (CEB-002):** `causation_id`/`correlation_id` preenchidos a partir do evento causador.
4. **Subscrição/autorização (CEB-008, gate):** determina os consumidores autorizados que declararam interesse (identidade autenticada do runtime); consumidor não autorizado ⇒ recusado.
5. **Entrega (CEB-006):** at-least-once; em falha, `RETRYING` com bounded loop; esgotado ⇒ `DEAD_LETTERED` (observável).
6. **Consumo idempotente (CEB-004):** o consumidor avança o cursor (CEB-003) e deduplica por chave de evento ⇒ `ACKED`.
7. **Saída externa (CEB-009, E3):** para notificação de Signal Package, o gate de emissão externa (fail-closed) verifica canal autorizado + notificação bem-formada; o SOT **não** executa ordem (INV-05).
8. **Metadados/latência (CEB-010):** metadados de transporte anexados; orçamento de latência = parâmetro a calibrar.
9. **Observabilidade (CEB-011):** latência/perdas/dead-letter registradas (insumo SPEC-040).
10. **Fail-safe (CEB-007):** em qualquer falha de transporte, recuperação por replay do cursor sobre o log (SPEC-004) — nenhum estado é perdido.

> **Nota de fronteira:** o **estado durável** e sua **ordem/versão/supersessão** são do **Blackboard (SPEC-004)**;
> a **coordenação** de quem publica/reage quando é do **Manager (SPEC-008)**. A SPEC-005 só **transporta/notifica**.
> [FONTE: ROADMAP §5; RULE-BB-001/005; SPEC-004 v1.2]

---

## D7 — Cenários de Teste

### Cenário-CEB-T01 — Envelope incompleto → rejeição
```
DADO        evento submetido sem source_ref
QUANDO      o transporte processa
ENTÃO       evento rejeitado; nada propagado
VERIFICAÇÃO event_propagated == false; rejected_reason == "ENVELOPE_INCOMPLETE"
```

### Cenário-CEB-T02 — Cadeia causal preservada
```
DADO        evento E2 ("Alarm.Cancelled") derivado de E1 ("Hypothesis.Superseded") — WF-A03
QUANDO      E2 é construído
ENTÃO       E2.causation_id == E1.event_id; E2.correlation_id == E1.correlation_id
VERIFICAÇÃO causation_chain_reconstructible == true
```

### Cenário-CEB-T03 — Cursor / catch-up após offline
```
DADO        consumidor com cursor em seq=100; log avançou até seq=120
QUANDO      o consumidor faz catch-up
ENTÃO       recebe 101..120 na ordem do log; cursor avança para 120
VERIFICAÇÃO delivered_range == [101,120]; no_missed_event == true
```

### Cenário-CEB-T04 — Idempotência de consumo (reentrega não duplica)
```
DADO        evento "EV-1" entregue duas vezes (at-least-once)
QUANDO      a segunda entrega é processada
ENTÃO       nenhum efeito duplicado; dedupe reconhece evento já consumido
VERIFICAÇÃO duplicate_effect == false; dedup_hit == true
```

### Cenário-CEB-T05 — Ordem intra-workspace total; cross-workspace parcial
```
DADO        A1,A2 (workspace A, seq 1,2) e B1 (workspace B) sem relação causal com A
QUANDO      o consumidor os observa
ENTÃO       A1 antes de A2; B1 em ordem relativa indefinida (parcial), sem ambiguidade
VERIFICAÇÃO intra_workspace_total_order == true; global_total_order_promised == false
```

### Cenário-CEB-T06 — Retry bounded + dead-letter
```
DADO        evento cuja entrega falha além do limite de tentativas
QUANDO      o retry se esgota
ENTÃO       evento roteado para dead-letter; registro observável; sem descarte silencioso; sem retry infinito
VERIFICAÇÃO dead_lettered == true; silent_drop == false; retries <= max_retries
```

### Cenário-CEB-T07 — Fail-safe: perda de push não perde estado
```
DADO        notificações perdidas por queda do canal push durante uma janela
QUANDO      o consumidor recupera
ENTÃO       todo o estado reconstruído por replay do cursor sobre o log (SPEC-004); nada de estado perdido
VERIFICAÇÃO state_loss == false; recovered_via == "cursor_over_log"
```

### Cenário-CEB-T08 — Consumidor não autorizado → recusa (não orquestra)
```
DADO        consumidor não autorizado tenta receber tipo de evento restrito
QUANDO      o gate de entrega roda
ENTÃO       recusa "CONSUMER_NOT_AUTHORIZED"; o Event Bus não decidiu invocação
VERIFICAÇÃO error_code == "CONSUMER_NOT_AUTHORIZED"; orchestration_decided == false
```

### Cenário-CEB-T09 — Saída externa do Signal Package a canal não autorizado → fail-closed [E3]
```
DADO        notificação de Signal Package para canal externo não autorizado
QUANDO      o gate de emissão E3 roda
ENTÃO       emissão negada (fail-closed); nada enviado; SOT não executa ordem; falso-DENY amostrado (ENF-07)
VERIFICAÇÃO external_emitted == false; fail_closed == true; order_executed_by_sot == false
```

### Cenário-CEB-T10 — Pedido de estado autoritativo ao bus → redirecionado ao Blackboard
```
DADO        consumidor pede ao Event Bus o estado corrente autoritativo de um objeto
QUANDO      o pedido roda
ENTÃO       o bus não serve estado autoritativo; aponta ao Blackboard; EVENT-BUS-001 permanece ABERTA
VERIFICAÇÃO authoritative_state_served_by_bus == false; event_bus_001_decision == "ABERTA"
```

---

## D8 — Rigor adversarial focado (sem profile elevado — casos de negação nos pontos de risco)

> Profundidade-alvo é **D0–D7** (HIGH, sem D8 pinado). Os casos de negação abaixo são **rigor adversarial focado**
> nos pontos de maior risco (entrega perdida/duplicada, ordem, dead-letter, saída externa, confusão transporte×estado),
> **sem elevar o profile** (AGENTS.md §4; DHR-SPEC005-001 §2). Princípio transversal: **fail-closed** e
> **transporte ≠ fonte de verdade**.

### ADV-CEB-01 — Evento sem envelope/source_ref propagado (viola CEB-001)
**DADO:** evento sem `source_ref` submetido. **QUANDO:** o transporte processa. **ENTÃO:** rejeitar `ENVELOPE_INCOMPLETE`; nada propagado. **PORQUE:** evento não rastreável contamina P13 e vira estado órfão. **VERIFICAÇÃO:** event_propagated == false.

### ADV-CEB-02 — Perda de notificação tratada como perda de estado (viola CEB-007/INV-CEB-01)
**DADO:** canal push cai e notificações se perdem. **QUANDO:** o consumidor recupera. **ENTÃO:** reconstruir por replay do cursor sobre o log (SPEC-004); nenhum estado perdido. **PORQUE:** transporte ≠ fonte de verdade — o log é a verdade (RULE-BB-004). **VERIFICAÇÃO:** state_loss == false.

### ADV-CEB-03 — Reentrega cria efeito duplicado (viola CEB-004)
**DADO:** o mesmo evento é reentregue (at-least-once). **QUANDO:** o consumo roda. **ENTÃO:** dedupe por chave; nenhum efeito duplicado. **PORQUE:** at-least-once sem dedupe de consumo corromperia o consumidor. **VERIFICAÇÃO:** duplicate_effect == false.

### ADV-CEB-04 — Retry infinito (viola CEB-006)
**DADO:** entrega falha persistentemente. **QUANDO:** o retry roda. **ENTÃO:** parar no limite (bounded loop) e rotear para dead-letter; nunca retry infinito. **PORQUE:** retry infinito fere Economicidade e esconde falha. **VERIFICAÇÃO:** retries <= max_retries; dead_lettered == true.

### ADV-CEB-05 — Descarte silencioso de evento não entregue (viola CEB-006)
**DADO:** evento não entregue após esgotar retry. **QUANDO:** a política roda. **ENTÃO:** dead-letter observável; proibido descartar em silêncio (`SILENT_DROP_FORBIDDEN`). **PORQUE:** perda silenciosa é não-auditável (P13). **VERIFICAÇÃO:** silent_drop == false.

### ADV-CEB-06 — Event Bus vira armazém de estado autoritativo (viola CEB-007/012/RULE-BB-001)
**DADO:** proposta de servir estado autoritativo pelo bus (paralelo ao Blackboard). **QUANDO:** o escopo é definido. **ENTÃO:** rejeitar `TRANSPORT_IS_NOT_SOURCE_OF_TRUTH`; estado autoritativo só no Blackboard. **PORQUE:** duplicaria a fonte de verdade da SPEC-004 (INV-09). **VERIFICAÇÃO:** authoritative_state_served_by_bus == false.

### ADV-CEB-07 — Saída externa emite ordem / emite a canal não autorizado (viola CEB-009/INV-05)
**DADO:** notificação de Signal Package a canal não autorizado, ou tentativa de executar ordem. **QUANDO:** o gate E3 roda. **ENTÃO:** fail-closed; nada emitido; o SOT não executa ordem (transporta notificação). **PORQUE:** emissão externa irreversível (ENF-04); INV-05. **VERIFICAÇÃO:** external_emitted == false; order_executed_by_sot == false.

### ADV-CEB-08 — Absorver vizinhos / fechar EVENT-BUS-001 por engano (viola fronteiras / CONS-01)
**DADO:** tentativa de a SPEC-005 virar broker durável, orquestrar (Manager), guardar estado permanente (KG), fixar estado por agente, ou **fechar** EVENT-BUS-001/M-001/J-001/N-001/H-001/G-001/WF-D03. **QUANDO:** o escopo/decisões são definidos. **ENTÃO:** rejeitar `OUT_OF_SCOPE_OR_OPEN_DECISION`; Opção C ADIADA; orquestração=SPEC-008; KG=SPEC-006/H-001 (ABERTA); estado-agente=SPEC-009/G-001 (ABERTA); decisões abertas permanecem ABERTAS (decisão de Andraus). **PORQUE:** CONS-01; INV-09; fronteiras explícitas. **VERIFICAÇÃO:** broker_built == false; open_decisions_closed == false.

> **Cobertura:** 8 casos de negação cobrindo os pontos de risco das BASpecs com efeito e as fronteiras abertas
> (EVENT-BUS-001, Opção C adiada, SPEC-004/006/008/009, RISK-M5). Mapeiam para EC-CEB-001..005 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada evento DEVE ser reconstruível (P13/RULE-010): envelope completo (`event_id`, `event_type`, `origin`, `timestamp`, `correlation_id`, `causation_id`, `source_ref`, `schema_version`), `delivery_state`, cadeia causal (`causation_id`), cursor do consumidor e registro de dead-letter. A **reconstrução de ESTADO** e a **ordem de commit** são do **Blackboard (SPEC-004, replay — RULE-CBP-011)** — o Event Bus reconstrói a **trilha de notificação/entrega**, não o estado (transporte ≠ fonte de verdade). A reconstrução expandida de linhagem e a observabilidade agregada pertencem à **SPEC-040 (Observabilidade)** e ao **KG (SPEC-006 / H-001 ABERTA)** — aqui ficam **por referência** (coerente com alvo D0–D7). [FONTE: CONSTITUTION P13; RULE-010; SPEC-004 RULE-CBP-011; ROADMAP §18; H-001 ABERTA]

---

## Contrato do evento — esqueleto [PROPOSTA]

> Produto central da SPEC-005. **Referencia** o objeto do Blackboard (SPEC-004) por `source_ref`; **não** o duplica
> nem redefine CHM-001/CEM-001/CCM-001 (CC-02). Transporte ≠ fonte de verdade.

| Camada | Conteúdo | Fronteira |
|---|---|---|
| Identidade | `event_id`, `event_type`, `schema_version` (de transporte), `timestamp`, `origin` | distinta do `object_id`/`version` do Blackboard |
| Causalidade | `correlation_id`, `causation_id` | cadeia reconstruível (P13) |
| Referência de estado | `source_ref` = `object_id@version` + `seq` + `workspace` | aponta ao log da SPEC-004; NÃO carrega o estado |
| Entrega | `delivery_state` (EMITTED/DELIVERING/RETRYING/ACKED/DEAD_LETTERED/REJECTED), `retries`, `dead_letter_ref` | at-least-once + dedupe; bounded retry |
| Consumo | `consumer_id`, `cursor_seq`, `dedup_key` | idempotência de consumo (≠ escrita SPEC-004) |
| Transporte | `transport_metadata` (Freshness/Latency/Reliability/Expiration), `latency_budget` (**PARÂMETRO a calibrar** — INDETERMINADO) | SAS-001 §6.10; SPEC-001 l.75; não toca J-001/N-001 |

### I/O Schema (lógico — referência; não redefine CHM-001/CEM-001/CCM-001)
```json
{
  "event_id": "EV-2026-10-04-001",
  "event_type": "Hypothesis.Superseded | Evidence.Invalidated | Conviction.Updated | SignalPackage.Ready | Alarm.Cancelled",
  "schema_version": "1 (versão do envelope de TRANSPORTE; migração NÃO definida aqui)",
  "timestamp": "2026-10-04T12:00:00Z",
  "origin": "institutional_agent",
  "correlation_id": "corr-abc",
  "causation_id": "EV-2026-10-04-000 (event_id do evento causador) | null (raiz)",
  "source_ref": "BB-2026-10-03-001@v2 + seq=42 + workspace=institutional_agent (referência ao log SPEC-004)",
  "delivery_state": "DELIVERING",
  "retries": 0,
  "dead_letter_ref": "null | DL-...",
  "consumer_cursor": "{ consumer_id, cursor_seq } (idempotência de CONSUMO — ≠ escrita SPEC-004)",
  "transport_metadata": "{ freshness, latency, reliability, expiration }",
  "latency_budget": "PARÂMETRO a calibrar — [DECISÃO NECESSÁRIA]/INDETERMINADO (sem número arbitrário; não toca J-001/N-001)"
}
```
> O evento **referencia** o objeto por `source_ref`; não guarda estado autoritativo (transporte ≠ fonte de verdade). Nenhum campo computa convicção nem deriva de custo (INV-04 — fora do escopo deste componente).

---

## Enforcement Contracts

### EC-CEB-001 — Emissão/entrega de notificação (envelope + causalidade)
```
CAPABILITY   : Montar um evento bem-formado e entregá-lo a consumidores autorizados
EFFECT       : Notificação (entrega) de um evento a consumidor(es) — NÃO altera estado durável (SPEC-004)
PRECOND      : (envelope mínimo + source_ref presentes — CEB-001) AND (causalidade preenchida — CEB-002)
POSTCOND     : evento entregue/ACKED ou roteado a RETRYING/DEAD_LETTERED; nenhum estado durável alterado
POLICY       : RULE-CEB-001/002; CEM-001 l.717-727; P13
LEVEL        : E1 (Contratual — notificação observável; o efeito de estado é da SPEC-004, não daqui)
FAILURE-MODE : Fail-closed — envelope inválido ⇒ REJECTED; nada propagado; log
EVIDENCE     : log de evento (envelope + delivery_state); cadeia causal reconstruível
```

### EC-CEB-002 — Entrega at-least-once, retry bounded, dead-letter
```
CAPABILITY   : Entregar com at-least-once, retry limitado e dead-letter em falha persistente
EFFECT       : Reentrega de evento ou roteamento para dead-letter (observável)
PRECOND      : (retries < MAX) para reentrega; (retries == MAX ∧ não-entregue) para dead-letter
POSTCOND     : evento entregue+deduplicado (exatamente-uma-vez efetivo) OU em dead-letter observável; nunca descarte silencioso
POLICY       : RULE-CEB-004/006; ENF-04; SRC-NOTIFY-01 [EXTERNO]
LEVEL        : E2 (Operacional — estado de entrega/dead-letter; bounded loop)
FAILURE-MODE : Fail-closed — esgotou retry ⇒ dead-letter (não descartar); retry infinito proibido
EVIDENCE     : registro de retries + dead-letter; ausência de efeito duplicado no consumidor
```

### EC-CEB-003 — Fail-safe transporte ≠ fonte de verdade (recuperação pelo cursor)
```
CAPABILITY   : Garantir que nenhuma perda de transporte cause perda de estado
EFFECT       : Recuperação de notificações por replay do cursor sobre o log (leitura; sem escrita de estado)
PRECOND      : (log append-only da SPEC-004 disponível) AND (cursor do consumidor registrado)
POSTCOND     : estado reconstruído pelo log; o Event Bus NÃO serve estado autoritativo (INV-CEB-01)
POLICY       : RULE-CEB-003/007/012; RULE-BB-001/004; SPEC-004 RULE-CBP-011; INV-CEB-01
LEVEL        : E2 (Operacional — fail-safe sobre o substrato durável)
FAILURE-MODE : Fail-closed — ambiguidade de transporte ⇒ recuperar pelo log, nunca fabricar estado no bus
EVIDENCE     : trilha de catch-up a partir do cursor; equivalência com o estado reconstruído do log
```

### EC-CEB-004 — Entrega a consumidor autorizado (não orquestra)
```
CAPABILITY   : Entregar eventos apenas a consumidores autorizados que declararam interesse
EFFECT       : Entrega (ou recusa) de notificação a um consumidor
PRECOND      : (consumidor ∈ subscritos autorizados pela identidade AUTENTICADA do runtime — CBP-014) AND (gate determinístico — ENF-03)
POSTCOND     : só consumidor autorizado recebe; o Event Bus não decide invocação (controle = Manager/SPEC-008)
POLICY       : RULE-CEB-008; RULE-BB-002/005; SPEC-004 RULE-CBP-014; ENF-03
LEVEL        : E2 (Operacional — autorização de entrega)
FAILURE-MODE : Fail-closed — consumidor não autorizado ⇒ CONSUMER_NOT_AUTHORIZED; nada entregue
EVIDENCE     : log de autorização por identidade autenticada; recusa registrada
```

### EC-CEB-005 — Canal de saída externo do Signal Package [E3]
```
CAPABILITY   : Transportar a notificação do Signal Package à fronteira externa (Bot Trade Finance)
EFFECT       : Emissão externa de notificação (irreversível) — NÃO é execução de ordem (INV-05)
PRECOND      : (canal/consumidor externo autorizado) AND (notificação bem-formada) AND (não é ordem de execução — INV-05)
POSTCOND     : notificação emitida só sob autorização + boa-formação; o SOT não executa ordem (o Bot executa)
POLICY       : RULE-CEB-009; INV-05; GPR-001 l.457; ENF-04/07; RISK-M5
LEVEL        : E3 (Crítico — emissão externa irreversível, cruza a fronteira de confiança)
FAILURE-MODE : Fail-closed — canal não autorizado / notificação malformada ⇒ não emitir; log.
             **Enforcement do E3 CONDICIONAL até o limiar amostral de falso-DENY ser definido (gap aberto, ENF-07)** (atomic-spec §12)
EVIDENCE     : gate_record de emissão externa (destino/autorização/resultado) + ENF-07: amostragem de falso-DENY
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
Serviço lógico de **transporte/notificação de mudanças** (camada fina, Forma A) sobre o log append-only da SPEC-004, mais o **canal de saída** da notificação do Signal Package. Combina gates constitutivos determinísticos (Classe C: dead-letter obrigatório, fail-safe transporte≠fonte de verdade, entrega a autorizado, saída externa E3) e mecânica determinística (Classe D: envelope, correlation/causation, cursor, dedupe de consumo, ordering observado, metadados/observabilidade). **Não guarda estado, não orquestra, não decide, não computa convicção, não executa ordem.** [FONTE: RULES.md RULE-BB-001/004/005; atomic-spec §9/§10.6; research.md §3]

### Roteamento de modelo (CEE-001 §5)
Gates constitutivos/determinísticos (C/D) **não requerem LLM** — são código. Um eventual juízo de "evento bem-formado para propagação" (Classe H, se adotado em BUILD) usaria apoio semântico **apenas como detector**, nunca como gate (ENF-03). Roteamento definitivo por Engineering Card (BUILD adiado). O mecanismo físico de transporte (push/poll/LISTEN-NOTIFY) é **INDETERMINADO** (BUILD). [FONTE: CEE-001 §5; ENF-03]

### Dependências técnicas
SPEC-004 v1.2 (BASELINE — log append-only, seq, replay, RULE-CBP-*) · RULES.md (RULE-BB-001/004/005) · CHM-001 (BASELINE) · CEM-001 (BASELINE — eventos canônicos l.717-727) · CCM-001 (BASELINE) · SPEC-001 v1.1 (BASELINE — EARS 8 l.159; delegação l.75) · SAS-001 (§6.9/§6.10) · CONSTITUTION l.235 · GPR-001 l.457 · SPEC-019/020/021 v1.0 (BASELINE) · atomic-spec v1.5 · INV-05/06/07/09/10 · ENF-01..08. Referências externas [EXTERNO], não-baseline: research.md §2 (SRC-OUTBOX-01, SRC-ES-01, SRC-NOTIFY-01, SRC-BROKER-01, SRC-BB-01, SRC-LLM-01) e §5 (REPO-debezium, REPO-langgraph elegíveis; REPO-postgresql-event-sourcing NÃO ELEGÍVEL/arquivado).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Over-engineering: broker durável por inércia do nome "Event Bus" | Forma A (camada fina); Opção C ADIADA (research.md §3.5/§3.6); RULE-CEB-007 (transporte≠fonte de verdade); ADV-CEB-06 |
| Reabrir/duplicar a SPEC-004 (durabilidade/ordem no transporte) | CC-02 foco; Non-goal explícito; cobertura×lacuna; INV-09; ADV-CEB-06 |
| Absorver vizinhos (KG/estado-agente/Manager/Signal Package) | Non-goals §D1; ADV-CEB-08; fronteiras explícitas; RISK-M5 |
| Fechar EVENT-BUS-001 por engano (pressão de "distinguir do Blackboard") | CEB-012 [PROPOSTA]; ADV-CEB-08; CONS-01; decisão de Andraus |
| Perda de notificação tratada como perda de estado | RULE-CEB-007/INV-CEB-01; CEB-007; ADV-CEB-02; EC-CEB-003 (recuperação pelo cursor) |
| Retry infinito / descarte silencioso | RULE-CEB-006; CEB-006; ADV-CEB-04/05; EC-CEB-002 (bounded loop + dead-letter) |
| Efeito duplicado por at-least-once | RULE-CEB-004; CEB-004; ADV-CEB-03 (dedupe de consumo) |
| Saída externa executa ordem / emite a canal não autorizado | INV-05; RULE-CEB-009; CEB-009; ADV-CEB-07; EC-CEB-005 (E3 fail-closed) |
| LLM como gate de entrega/autorização | ENF-03; EC-CEB-004 (detector≠gate) |
| Latência subdeclarada (TMP/alarme chega tarde) | RULE-CEB-010; CEB-010; orçamento = parâmetro observável (SPEC-040); 4Es |
| Fixar número de latência sem base | RULE-MET-01; orçamento = [DECISÃO NECESSÁRIA]/INDETERMINADO; não toca J-001/N-001 |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz o schema lógico do **evento** (envelope de transporte); nenhum schema canônico do CHM-001/CEM-001/CCM-001 nem da SPEC-004 alterado.
- **RAG/KG:** nenhum; o Event Bus não escreve no KG/RAG (memória permanente = SPEC-006).
- **Skills:** nenhuma Skill afetada; INV-06 preservado (Skill produz Observação; o Event Bus só propaga eventos sobre ela).
- **Testes:** adiciona `checks.md` (verificação de spec); mecânica de transporte fica para BUILD.
- **Modelos/Specs dependentes:** SPEC-004/CHM-001/CEM-001/CCM-001/SPEC-001 não alterados (construção SOBRE); RULE-BB-001/004/005 operacionalizadas no eixo de transporte, não alteradas.
- **Compatibilidade:** Minor — não toca modelo canônico baselined, não reabre a SPEC-004, não fecha decisão aberta (DHR-SPEC005-001 §Compatibilidade).

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07), a Classe por BASpec (CC-11) e o mecanismo físico de transporte (push/poll/LISTEN-NOTIFY — hoje INDETERMINADO). A resolução de EVENT-BUS-001 é condição da homologação do Plan por Andraus.

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório HIGH)

**Bloco A — pergunta adversarial por BASpec com efeito (cobertura das BASpecs CRITICAL/HIGH — 12 BASpecs):**

- **CEB-001 (envelope, D):** se errada → evento sem source_ref propagado → observável por evento órfão sem referência de estado; verificável. Negação: ADV-CEB-01.
- **CEB-002 (causalidade, D):** se errada → cadeia causal não reconstruível → observável por `causation_id` ausente/quebrado; verificável. QUANDO-sim-mas-ENTÃO-não: evento raiz tem `causation_id` nulo (correto).
- **CEB-003 (cursor, D):** se errada → eventos perdidos após offline → observável por `no_missed_event=false`; verificável. Negação: ADV-CEB-02 (recuperação pelo cursor).
- **CEB-004 (dedupe, D):** se errada → efeito duplicado por reentrega → observável por `duplicate_effect=true`; verificável. Negação: ADV-CEB-03.
- **CEB-005 (ordering, D):** se errada → ordem global ambígua prometida → observável por replays divergentes cross-workspace; verificável. QUANDO-sim-mas-ENTÃO-não: eventos sem relação causal podem vir em ordem relativa indefinida (não é erro).
- **CEB-006 (entrega/retry/dead-letter, C):** se errada → retry infinito ou descarte silencioso → observável por `retries>max` ou `silent_drop=true`; verificável. Negação: ADV-CEB-04/05.
- **CEB-007 (transporte≠fonte de verdade, C):** se errada → perda de notificação vira perda de estado → observável por `state_loss=true`; verificável. Negação: ADV-CEB-02/06.
- **CEB-008 (entrega autorizada, C):** se errada → consumidor não autorizado recebe, ou o bus decide invocação → observável por `orchestration_decided=true`; verificável. Negação: ADV-CEB-08.
- **CEB-009 (saída externa, C/E3):** se errada → emissão a canal não autorizado ou execução de ordem → observável por `external_emitted=true`/`order_executed_by_sot=true`; verificável. Negação: ADV-CEB-07. QUANDO-sim-mas-ENTÃO-não: notificação bem-formada a canal autorizado é emitida (correto).
- **CEB-010 (latência, D):** se errada → número de latência fabricado no Plan → observável por `hardcoded_latency=true`; verificável. QUANDO-sim-mas-ENTÃO-não: orçamento como parâmetro é aceitável (não é erro).
- **CEB-011 (observabilidade, D):** se errada → transporte não observável → observável por ausência de métricas; verificável.
- **CEB-012 (distinção, C — EVENT-BUS-001 ABERTA):** se errada → bus serve estado autoritativo ou fecha EVENT-BUS-001 → observável por `authoritative_state_served_by_bus=true` ou decisão fechada; verificável. Negação: ADV-CEB-06/08.

Todas as 12 BASpecs com efeito têm ENTÃO verificável por observador independente e caso de negação em D8. Nenhuma restou como [DECISÃO NECESSÁRIA] por falta de verificabilidade (EVENT-BUS-001/M-001/J-001/N-001/H-001/G-001/WF-D03 são fronteiras/decisões abertas explícitas, não falhas de verificabilidade).

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista a SPEC-004 v1.2 (RULE-CBP-001/003/005/006/011/013/014), RULE-BB-001/004/005, CHM-001, CEM-001 (l.717-727), CCM-001, SPEC-001 v1.1 (EARS 8 l.159; l.75), SAS-001 §6.9/§6.10, CONSTITUTION l.235, GPR-001 l.457, atomic-spec v1.5, ENF-01..08, INV-05/06/07/09/10 (ID+versão/linha — RULE-HD-04). Evidência de satisfação por obrigação herdada:
- SPEC-004 ordem de commit/seq (RULE-CBP-006) → reusada por CEB-003/005 (cursor/ordering); não recriada.
- SPEC-004 idempotência de escrita (RULE-CBP-005) → CEB-004 adiciona idempotência de **consumo** distinta; não reabre.
- SPEC-004 replay (RULE-CBP-011) → CEB-003/007 (catch-up e fail-safe) reusam; não redefinem.
- SPEC-004 identidade autenticada (RULE-CBP-014) → CEB-008 (entrega autorizada) reusa.
- RULE-BB-001 (só via Blackboard) → o Event Bus notifica, não substitui o canal de estado (CEB-007/012).
- RULE-BB-004 (append-only) → base do fail-safe (CEB-007).
- RULE-BB-005 (Orchestrator só coordena) → fronteira SPEC-008 (CEB-008; ADV-CEB-08).
- CEM-001 l.717-727 (eventos canônicos) → propagados por CEB-001/002 (CC-02 — não redefinidos).
- SPEC-001 l.75 (delegação de latência) / SAS-001 §6.10 → CEB-010 (SPEC-005 é dona dos metadados de transporte).
- INV-05 (SOT não executa) → CEB-009/EC-CEB-005 (E3 fail-closed na saída externa).
- ENF-03/04/07 → EC-CEB-004 (detector≠gate), EC-CEB-002/005 (fail-closed), EC-CEB-005 (falso-DENY).
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (nenhum MODIFIED). **Eixo VERTICAL (RULE-HV) declarado não aplicável** (herança sobre a SPEC-004/regras/canônicos vizinhos, não decomposição pai→filha de macro-spec).

**Bloco C — epistêmico (RULE-EPI/CAU/PRB):** nenhuma afirmação causal forte sem mecanismo; nenhuma hipótese tratada como fato (SRC-*/REPO-* = [EXTERNO]/DADO; nenhum método externo importado como baseline — broker ADIADO, outbox/CDC adaptados); **INDETERMINADO** usado sobre o mecanismo físico de transporte (push/poll/LISTEN-NOTIFY); **orçamento de latência = PARÂMETRO a calibrar** ([DECISÃO NECESSÁRIA]), não forçado a número; **EVENT-BUS-001 ABERTA** declarada, não forçada a PASS/FAIL; **nenhuma probabilidade/precisão numérica** declarada (nenhum limiar de convicção nem de latência). IDs arXiv implausíveis descartados (research.md §aviso; RULE-MET-01); o trecho dev.to (LISTEN/NOTIFY) 404 mantido só como DADO não-verificado, com equivalente verbatim em centrifugal.dev.

**Bloco D — reforço de escopo:** a Spec **transporta/notifica** mudança de estado (notificação), **não guarda estado**, **não executa** ordem (INV-05/RULE-DEC-01 reconfirmados — §7), **não decide** invocação (Manager) nem **computa** convicção. Nenhuma BASpec cruza a fronteira SOT→execução downstream (CEB-009 transporta a notificação do Signal Package; o Bot executa) nem invade Blackboard (SPEC-004)/KG (SPEC-006)/estado-agente (SPEC-009)/Manager (SPEC-008)/Signal Package (RISK-M5). Dependências de decisão de Andraus (homologação; efetivação de RULE-CEB/contrato; **EVENT-BUS-001**) marcadas [PROPOSTA]/[DECISÃO NECESSÁRIA], não fechadas; M-001/J-001/N-001/H-001/G-001/WF-D03/ECC-03-001 abertas, não tocadas.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| SPEC-004 v1.2; RULE-BB-001/004/005; CHM-001; CEM-001; CCM-001; SPEC-001 v1.1; SPEC-019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5; RULES v1.5; INV-*; ENF-*; RULE-010; SAS-001 §6.9/§6.10; CONSTITUTION l.235; GPR-001 l.457 | [FONTE] | FATO NORMATIVO |
| RULE-CEB-001..012; INV-CEB-01; contrato de evento; BASpec-CEB-001..012; EC-CEB-001..005 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Fontes SRC-OUTBOX-01/ES-01/NOTIFY-01/BROKER-01/BB-01/LLM-01; REPO-debezium/langgraph | [EXTERNO] | Referência de método — DADO, nunca baseline (research.md §2/§5) |
| REPO-postgresql-event-sourcing (arquivado) | [EXTERNO] | **NÃO ELEGÍVEL** (régua Equilibrada) — não adotado |
| Distinção formal Blackboard↔Event Bus (resolução de EVENT-BUS-001) | [DECISÃO NECESSÁRIA] | **EVENT-BUS-001 — EM ABERTO — não fechar** (decisão de Andraus na homologação; CEB-012 só propõe) |
| Mecanismo físico de transporte (push/poll/LISTEN-NOTIFY, fila interna) | [DECISÃO NECESSÁRIA] | **INDETERMINADO** — BUILD |
| Broker durável completo (Opção C) | [DECISÃO NECESSÁRIA] | **ADIADO** — reavaliável com múltiplos consumidores distribuídos/alta vazão |
| Orçamento de latência/entrega de transporte | [DECISÃO NECESSÁRIA] | **PARÂMETRO a calibrar** — INDETERMINADO (sem número; não toca J-001/N-001) |
| Enum de estados do Blackboard p/ objetos não-hipótese | [DECISÃO NECESSÁRIA] | **M-001 — EM ABERTO (SPEC-004)** — não tocado |
| Fórmula/pesos/limiares definitivos do Conviction Vector; pesos por ativo | [DECISÃO NECESSÁRIA] | **J-001 / N-001 — EM ABERTO (SPEC-003/backtest)** — não tocadas |
| Knowledge Graph (grafo real vs memória) / estado por agente | [DECISÃO NECESSÁRIA] | **H-001 / G-001 — EM ABERTO (SPEC-006/009)** — não tocadas |
| Relação convicção-macro/global com Conviction Vector | [DECISÃO NECESSÁRIA] | **WF-D03 — EM ABERTO (WORKFLOW)** — não tocada |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-005 confirmada como próximo autorizado (§5/§21/"próximo trabalho"); FASE 2, após SPEC-004 BASELINE v1.2.
[x] atomic-spec.md lido: método v1.5 confirmado (CC-11/CC-12; RULE-MECH-01; RULE-ECC-04/06; RULE-MM; §15 Dossiê).
[x] Nenhum invariante congelado violado (INV-01..10). INV-05/06/07/09/10 reforçados; transporte ≠ fonte de verdade (INV-CEB-01).
[x] Constitution Check CC-01..CC-12 preenchido (N/A justificados CC-06/07/12; CC-02/CC-08/CC-10/CC-11 INCIDEM e aplicados).
[x] Disciplinas N8–N17: RULE-EPI (EVENT-BUS-001 ABERTA; INDETERMINADO sobre mecanismo físico), RULE-MET-01 (não fabricar número de latência; arXiv descartado), RULE-UNC (ordenação cross-workspace/perda de notificação), RULE-SEM-01 (acepções "evento" vs "objeto"), RULE-DEC-01 (transporta≠decide≠executa).
[x] Referências externas [EXTERNO] classificadas (research.md §2/§5); rótulos externos (outbox/CDC/broker/LangGraph) NÃO adotados como baseline; verbatim capturado (RULE-ECC-04, sources/); repositórios sob régua Equilibrada (RULE-ECC-06, research.md §5 — 2 elegíveis + 1 não elegível).
[x] RULE-ECC-05 (Multi-Lente): determinação de NÃO-incidência (infra; não toca comportamento de trading) — confirmada na abertura (DHR-SPEC005-001 §2); conformidade WORKFLOW por prudência (WF-A03/WF-F02; não fecha WF-D03).
[x] Spec sem implementação (BUILD adiado); Plan derivado da abertura homologada; Tasks adiadas (spec-first).
[x] Critérios em EARS (12); BASpecs completas (CEB-001..012) com Classe declarada (CC-11); RULEs citadas existentes vs propostas (RULE-CEB [PROPOSTA]) etiquetadas.
[x] Profundidade D0–D7 (sem D8 pinado) atingida; rigor adversarial focado (D8 ADV-CEB-01..08) sem elevar o profile; D4 (cursor/dedupe/correlation); D5 (ciclo do evento/entrega); D6 protocolo; D7 x10; D9 por referência.
[x] Enforcement Contract em todo ato com efeito (EC-CEB-001..005); piso E1/E2; E3 na saída externa do Signal Package (irreversível; fail-closed); ENF-07 amostral declarado no E3 — enforcement CONDICIONAL até o limiar (gap aberto).
[x] Status epistemológico aplicado (FATO NORMATIVO / PROPOSTA / EXTERNO / DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: EVENT-BUS-001, M-001, J-001, N-001, H-001, G-001, WF-D03, ECC-03-001 permanecem ABERTAS; nenhuma decisão aberta usada como invariante fechado; Doc 13 = histórico não-normativo (não fecha).
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos/achados registrados: conflito de linhagem Doc 13×RULE-BB-001 tratado como histórico (TRACE-06); Menor A4 (research.md §6.4) corrigido.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE fabricada como vigente; sem baseline informal.
[x] 4Es na ordem; Conformidade > Eficácia (INV-05/INV-CEB-01 e ENF-03/04 prevalecem). Latência declarada como material e PARÂMETRO a calibrar (consumidor sensível a tempo).
[x] Dependências a montante homologadas (SPEC-004 v1.2/RULE-BB-*/CHM/CEM/CCM/SPEC-001/019/020/021/atomic-spec v1.5); não downstream de bloqueador aberto não resolvido (EVENT-BUS-001 é dona desta Spec, proposta não fechada).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); Bloco A cobre TODAS as 12 BASpecs com efeito — obrigatório HIGH.
[x] CC-11/§10.6: Classe por BASpec com efeito, com critério 4Es; Classe C com gate de saída; CEB-006 (C) com bounded loop; nenhuma H/P normativa.
[x] Abertura (RULE-ECC-01/02/04/06): Dossiê presente e HOMOLOGADO (DHR-SPEC005-001); verbatim em sources/; repositórios em research.md §5; escopo/quantidade/número homologados (1 Spec).
[x] Passo 11-bis: nenhum item com gatilho spec:SPEC-005; BL-008/BL-003/BL-017 independentes (Andraus).
[ ] Gate determinístico (validate_spec_sot.py), check_repo_research.py, build_map.py --check e check_doc_sync.py: reportados ao caller (execução no ambiente pai — Especificador sem Bash).
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] / abertas nesta Spec (não fechadas — CONS-01):
- **EVENT-BUS-001** — "o Event Bus existe? como se distingue do Blackboard?": a SPEC-005 é a **dona** e **propõe** a distinção (RULE-CEB-012: Blackboard guarda estado / Event Bus transporta mudanças; processo separado, não segundo armazém), mas **não fecha** — decisão de Andraus na homologação. Permanece ABERTA.
- **Mecanismo físico de transporte** (push/poll/LISTEN-NOTIFY, fila interna) — **INDETERMINADO** (BUILD).
- **Broker durável completo (Opção C)** — **ADIADO** (registrado, não apagado; reavaliável com múltiplos consumidores distribuídos/alta vazão).
- **Orçamento de latência/metadados de transporte** — **PARÂMETRO a calibrar** (INDETERMINADO; sem número arbitrário; não toca J-001/N-001).
- **M-001** (estados do Blackboard p/ objetos não-hipótese) — fronteira (SPEC-004); não tocada, permanece ABERTA.
- **J-001 / N-001** (fórmula/pesos/limiares definitivos do Conviction Vector / pesos por ativo) — o Event Bus só notifica, não computa; não tocadas, permanecem ABERTAS.
- **H-001 / G-001** (KG / estado por agente) — fronteiras (SPEC-006/009); não tocadas, permanecem ABERTAS.
- **WF-D03** (residual) — não tocada (o Event Bus não computa convicção); permanece ABERTA.
- **ECC-03-001** (escopo da RULE-ECC-03) — não tocada; permanece ABERTA.

Carregado para o Revisor:
- Cobertura × lacuna da SPEC-004 v1.2 (BASELINE) com arquivo:linha — a SPEC-005 **não duplica** ordem de commit/seq, idempotência de escrita, replay, identidade autenticada, supersessão, schema_version, atomicidade (herdados por ID+versão; CC-08).
- Baselines que citam o Event Bus tratados **sem erratum** (número preservado): SPEC-001 EARS 8 (`SPEC-001/plan.md` l.159/l.367) e l.75 (delegação de latência/transporte); CEM-001 l.725 (propagação EC-COG-005); CONSTITUTION l.235; GPR-001 l.457; SAS-001 §6.9/§6.10.
- Necessidade real WF-A03 (cancelar alarme quando hipótese→SUPERSEDED/REFUTED) tratada como cadeia causal de evento (CEB-002/T02); WF-xx citados só por ID; WF-D03 não fechada.
- EVENT-BUS-001 apresentada como **[PROPOSTA]** de resolução (CEB-012); **não** fechada — decisão de Andraus; Doc 13 = histórico não-normativo (RULE-BB-001 prevalece).
- Saída externa do Signal Package = **E3 fail-closed** (EC-CEB-005; INV-05 — SOT não executa ordem; contrato do Signal Package = RISK-M5, não reaberto).
- Menor A4 corrigido: research.md §6.4 alinhado à decisão de **manter o nome** "Cognitive Event Bus".
