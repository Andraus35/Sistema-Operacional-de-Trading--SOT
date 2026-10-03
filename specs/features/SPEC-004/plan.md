# SPEC-004 — Cognitive Blackboard Protocol

| Campo | Valor |
|---|---|
| ID | SPEC-004 — Cognitive Blackboard Protocol (camada Harness/operacional da memória de trabalho compartilhada) |
| Versão | 1.1 (candidata) |
| Status | **CANDIDATA — aguarda parecer do Revisor e homologação de Andraus.** Abertura HOMOLOGADA (DHR-SPEC004-001, 2026-10-03); este é o **Plan** (próximo gate). NÃO é baseline (INV-09). |
| Fonte | ROADMAP §5 (FASE 2); `ABERTURA.md` + `research.md` (Dossiê HOMOLOGADO — DHR-SPEC004-001; RULE-ECC-01/02/04/06); atomic-spec **v1.5**; `governance/RULES.md` (RULE-BB-001..005); `WORKFLOW.md` (conformidade, não editada) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §5 "P0 — CRITICAL"; atomic-spec §3 "Blackboard Protocol = CRITICAL"] |
| Profundidade-alvo | **D0–D7** (standard; **rigor adversarial extra — D8 — nos comportamentos de maior risco: escrita concorrente, duplicidade/idempotência, versionamento/supersessão**) [FONTE: ROADMAP §5; atomic-spec §3; DHR-SPEC004-001 §1 — Q-ABERTURA-1 homologada: D0–D7 com adversarial extra, sem elevar o profile global em silêncio] |
| Profile (Claude Code) | standard + rigor adversarial extra nos comportamentos E3 |
| Posição no caminho crítico | FASE 2 — MEMÓRIA DE TRABALHO; após FASE 1 (SPEC-001/002/003 BASELINE) e FASE GOV (019/020/021); antes de SPEC-005 (Event Bus) [FONTE: ROADMAP §5/§21] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3 teto spec-first; gate normativo E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01; RULE-PD-01 **(N/A)**; RULE-ECC-04 (verbatim); RULE-ECC-06 (repositórios); RULE-ECC-05 **(N/A — não toca comportamento de trading)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — **D** (versão/ordenação/idempotência/append-only) + **C** (permissão de escrita, proveniência obrigatória, fail-closed de supersessão/append-only) + **H** (juízo de "objeto bem-formado para publicação"); declaração normativa é **por BASpec** |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-03 |
| Abertura | Dossiê de Pesquisa HOMOLOGADO por Andraus (DHR-SPEC004-001, research.md); Plan iniciado dentro da validade do Dossiê (CRITICAL → 90 dias; limite 2027-01-01; ECC-VAL-001 FECHADA, DHR-DEC-003) |

Complexidade: CRITICAL. Profundidade-alvo: D0–D7 (standard; rigor adversarial extra — D8 — em escrita concorrente, duplicidade/idempotência e versionamento/supersessão).

**Status epistemológico de cabeçalho:** a SPEC-004 é a **camada Harness/operacional** sobre as RULE-BB-001..005 (vigentes) — formaliza **o protocolo** da memória de trabalho (contrato de objeto publicado, publicação/leitura/atualização, ciclo de vida append-only, concorrência, proveniência, reconstrução). **NÃO redefine** CHM-001 (estados da hipótese), CEM-001 (Evidência) nem CCM-001 (Convicção) — **CC-02/CONST-01**: o Blackboard **armazena/versiona/publica** esses objetos sob seus contratos canônicos, sem reescrevê-los. **M-001** (estados do Blackboard para objetos NÃO-hipótese) permanece **ABERTA** — este Plan **propõe** uma abordagem ([PROPOSTA]), não a fecha (CONS-01; decisão de Andraus na homologação do Plan). [FONTE: ROADMAP §5; atomic-spec §12; DHR-SPEC004-001 §1]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-10-03 | Entrega candidata inicial do Plan. Camada Harness sobre RULE-BB-001..005; 12 BASpecs (CBP-001..012) com Classe D/C/H (CC-11); 6 Enforcement Contracts (EC-CBP-001..006; E3 no gate de escrita/append-only); 11 EARS; D5 ciclo de objeto [PROPOSTA] (M-001 ABERTA); D6 protocolo; D7 cenários; D8 adversarial focado em concorrência/duplicidade/versionamento; D9 por referência. Corrige **ACH-001** (SRC-MEM-01: URL arXiv 2606.* rebaixada a não-load-bearing, coerente com o aviso de método) e **ACH-002** (RULE-BB-003 **SUPERSEDED por Q-006**; o Blackboard NÃO define estado de hipótese — usa CHM-001; citação a `governance/RULES.md` linhas 316–321). M-001 segue ABERTA ([PROPOSTA] apenas). |
| 1.1 | 2026-10-03 | Correção do achado **ACH-004** (parecer CONFORME do Revisor, 1 Menor): atualização SEM `expected_version` passa a ser RECUSADA (fail-closed, código `EXPECTED_VERSION_REQUIRED`), enquanto a CRIAÇÃO de objeto novo permanece permitida sem `expected_version` (create = versão inicial) — decisão de Andraus (chat, 2026-10-03). Materializado em: **EARS 4-bis**; **BASpec-CBP-004** (QUANDO/ENTÃO/VERIFICAÇÃO + MECANISMO); contrato mínimo **CBP-001 / RULE-CBP-001** (distinção create vs update) + RULE-CBP-004; D4 (algoritmo); **Cenário-CBP-T10**; **ADV-CBP-11**; contrato de objeto (tabela). EARS passa a 12 (1..11 + 4-bis); D7 x10; D8 x11. M-001 permanece ABERTA (a decisão de Andraus sobre M-001 é registrada em ata pelo Controlador, NÃO neste Plan — CONS-01). |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; DHR-SPEC004-001 §2; RMR-001]

O início da redação deste Plan satisfaz `spec:SPEC-004 em redação` — disparam os gatilhos abaixo. A **promoção a `ATIVADO`/`Absorvido` e o encaminhamento são do gate e de Andraus** (CONS-01); o Especificador apenas reflete o tratamento.

- **BL-029** (`spec:SPEC-014 ∨ spec:SPEC-004 em redação`; **dona = SPEC-004**, DHR-DEC-003): proveniência `computed_by`/`gate_record` do objeto no Blackboard. **TRATADO neste Plan** — materializado no contrato de objeto (BASpec-CBP-001) e na **proveniência obrigatória** (BASpec-CBP-007 + EC-CBP-001): todo objeto publicado carrega `computed_by` (quem/qual atividade produziu) e, quando resulta de um gate, `gate_record` (resultado + limiares usados), por referência — **sem** fixar sobre qual valor o gate consumidor opera (isso é fronteira SPEC-003/N3 — não reaberta aqui). [FONTE: RMR-001 BL-029; DHR-DEC-003; SPEC-003 Nota N3]
- **BL-002** (Falso-DENY observável, ENF-07; **Absorvido**, encaminhado à SPEC-004 por DHR-DEC-003): método de observação de falso-DENY do gate E3. **TRATADO neste Plan** — como **requisito de observabilidade do Blackboard** (BASpec-CBP-012 + EC-CBP-002 ENF-07): o gate de escrita E3 declara o método amostral de observação de DENY indevido; o **limiar amostral** permanece **gap de enforcement aberto** (atomic-spec §12), não fixado aqui. [FONTE: RMR-001 BL-002; DHR-DEC-003; ENF-07]
- **BL-003** (Persistência física de hipótese/estado; `spec:SPEC-004 em redação`): especificar o storage (Blackboard/KG) referenciado pelo slot da SPEC-001. **TRATADO como FRONTEIRA** — a SPEC-004 define o **storage lógico** (contrato de objeto + API de reconstrução por replay, BASpec-CBP-011), mas **NÃO fecha o mecanismo físico** (grafo real vs. memória = **H-001**/SPEC-006; estado persistente por agente = **G-001**/SPEC-009). O Hypothesis Registry (SPEC-001) referencia o Blackboard como storage lógico; o físico fica aberto. [FONTE: RMR-001 BL-003; ROADMAP §5; SPEC-001 §escopo]
- **BL-012** (MC-COG-001; `spec:SPEC-002 homologada`): permanece **`ATIVADO`**, **independente desta Spec** — não bloqueia nem é absorvido pela SPEC-004; encaminhamento é de Andraus (registrado para visibilidade do gate). [FONTE: RMR-001 BL-012; DHR-SPEC004-001 §2]
- **BL-017** (dimensão B da SPEC-020): ATIVADO/pendente, independente desta abertura; não encaminhado por esta Spec. [FONTE: DHR-SPEC004-001 §2; ROADMAP §12]
- **BL-011/BL-010** (Master Contracts EXP/RAG): **não disparam** aqui (gatilhos `spec:SPEC-006/009/007`); fonte de requisitos futura. [FONTE: research.md §6.3]
- Nenhum item fica `ATIVADO` pendente **sem encaminhamento** por esta redação (BL-029/BL-002 tratados; BL-003 fronteira; BL-012/BL-017 independentes, de Andraus). O passo 11-bis pleno ocorre na homologação do Plan.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o Blackboard é **infraestrutura agnóstica de escola** — armazena/versiona/publica objetos de qualquer camada analítica **sem** alterar a hierarquia nem a autoridade de criação de hipótese (Elliott cria primária; ICT não cria — INV-01/INV-02). Não introduz nenhum comportamento que sobreponha camada inferior à superior. [FONTE: INV-01/INV-02; ROADMAP §6]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** **foco.** O Blackboard **armazena, versiona e publica** hipótese (CHM-001), Evidência (CEM-001, idioma canônico INV-10) e Convicção (CCM-001) **sem redefinir** nenhum contrato nem máquina de estados. Em especial, **o Blackboard NÃO define estado próprio de hipótese** — usa os estados do CHM-001 (**RULE-BB-003 está [SUPERSEDED por Q-006]** — `governance/RULES.md` l.316–321). CDM-001/CNM-001 pendentes não acionam CONST-01. [FONTE: CC-02; RULES.md RULE-BB-003; CHM-001; CEM-001; CCM-001]
- [x] **CC-03 — Conviction Vector:** o Blackboard **não computa** convicção — apenas armazena/versiona o objeto Conviction Vector (CCM-001). Dimensionalidade=8 (fechada) intocada; **J-001/N-001 permanecem ABERTAS** (fórmula/pesos/limiares definitivos) — não tratadas aqui. Nenhum limiar numérico de convicção é declarado neste Plan. [FONTE: INV-03; J-001/N-001 pendentes]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. O Blackboard não emite sinal, não dimensiona risco e **não** aplica os gates de sinal (isso é SPEC-003/Manager). **INV-04** (custo nunca no Conviction Vector) é preservado por construção — o Blackboard não cria convicção a partir de custo. [FONTE: CEE-001 §10/§11; INV-04]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D7 com adversarial extra (ROADMAP §5; DHR-SPEC004-001).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card; §59/§60 tornam-se obrigatórios nas Tasks/Cards (BUILD adiado — atomic-spec §14). Omissão justificada.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem: ROADMAP §5 → Dossiê (research.md, homologado) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED com ID+versão (RULE-HD-04); REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Eixo VERTICAL (RULE-HV) avaliado e declarado não aplicável (herança sobre regras/canônicos vizinhos, não decomposição pai→filha de macro-spec). [FONTE: EUA-E04 §8.3; RULE-HD-02/03/04]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI):** aplicado — **M-001 declarada ABERTA** ([DECISÃO NECESSÁRIA]), não como fato; **INDETERMINADO** usado onde a necessidade de CRDT/merge multi-escritor não está decidida (research.md §5.3); sem falsa precisão (nenhum número de convicção/limiar fixado); fontes web = DADO [EXTERNO] (research.md §2). [FONTE: RULE-EPI-01..03; research.md §5]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM-01):** **INCIDE e tratado.** Acepções declaradas (ver "Declaração de acepção semântica"): **"estado do objeto no Blackboard"** (ciclo operacional de publicação/supersessão — M-001) vs **"estado da hipótese"** (máquina do CHM-001, não redefinida); **"Observação"** (produzida por Skill) vs **"Evidência"** (produzida por Agente — INV-06); **"memória de trabalho"** (Blackboard, volátil/append-only) vs **"memória permanente"** (Knowledge Graph — SPEC-006). Nenhum termo canônico do GLOSSARIO redefinido (RULE-SEM-04). [FONTE: RULE-SEM-01/04; INV-06; GLOSSARIO]
- [x] **CC-11 — Classe/Mecanismo por BASpec com efeito (RULE-MECH-01):** **INCIDE** — a SPEC-004 cita RULE-MECH-01 e é "SPEC-002 em diante". Cada BASpec com efeito declara Classe (D/H/P/C) com critério 4Es; Classes H/P declaram bounded loop + critério de parada; Classes H/C declaram gate de saída determinístico. Declaração por BASpec, nunca por Spec inteira (SES-001 §50). Ver §D3. [FONTE: RULE-MECH-01..04; atomic-spec §9/§10.6]
- [x] **CC-12 — Princípios de Domínio `PD-xx` (RULE-PD-01):** **N/A — não incide** (DHR-SPEC004-001 §1; ABERTURA §6). O Blackboard é **infraestrutura de memória de trabalho agnóstica de escola** — não define escopo de especialidade (Elliott/SMC/ICT). Mesmo padrão N/A de SPEC-002. Registrado explicitamente, não supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7; DHR-SPEC004-001 §1]

**Disciplinas cognitivas N8–N17 incidentes (RULES.md v1.5):** RULE-EPI (M-001 ABERTA ≠ fato; INDETERMINADO sobre CRDT), RULE-MET-01 (não-fabricação — não afirmar necessidade de mecanismo não verificada; ver ACH-001/aviso de método), RULE-UNC-01..03 (incerteza localizada sobre concorrência multi-escritor), RULE-SEM-01/04 (acepções "estado do objeto" vs "estado da hipótese" declaradas; termos canônicos não redefinidos), RULE-DEC-01 (o Blackboard **guarda estado**, não decide nem executa — INV-05). INDETERMINADO usado onde há incerteza material.

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-004

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - Regras do Blackboard (vigentes): governance/RULES.md v1.1 —
      • RULE-BB-001 (comunicação EXCLUSIVAMENTE via Blackboard; nenhum agente comunica direto com outro)
      • RULE-BB-002 (agente LÊ qualquer workspace; PUBLICA apenas no próprio; NUNCA em workspace alheio)
      • RULE-BB-003 **[SUPERSEDED por Q-006 — Andraus 2026-09-14]** — o ciclo PROPOSED→VALIDATED→ACTIVE→
        SUPERSEDED (KERNEL EC-COG-004) foi DESCONTINUADO; os estados da HIPÓTESE são os do CHM-001; o
        Blackboard NÃO define estado próprio de hipótese (RULES.md l.316–321). Herdado como fronteira
        (CC-02), NÃO como regra viva de estado de hipótese.
      • RULE-BB-004 (Blackboard append-only durante a análise; objetos são SUPERSEDED, nunca deletados)
      • RULE-BB-005 (Orchestrator APENAS coordena via Blackboard; NUNCA analisa — fronteira SPEC-008)
  - Objetos canônicos armazenados (fronteira — NÃO redefinidos): CHM-001 (BASELINE) estados/versionamento
      da hipótese; CEM-001 (BASELINE, DHR-TAX-001) ciclo de vida/Lineage da Evidência + INV-10 (idioma
      canônico); CCM-001 (BASELINE, DHR-SPEC003-001) objeto Conviction Vector 8D
  - Camada a montante: SPEC-001 v1.1 (BASELINE) — Hypothesis Registry referencia o Blackboard como storage
      lógico (versionamento monotônico operacional, índice de estado ativo, reconstrução histórica — BL-003)
  - Método: atomic-spec.md v1.5 (BASpec, D0–D9, EARS, Enforcement E0–E3/F.1–F.4, TRACE-06, Quality Gates
      L1–L4 §7, Classe/Mecanismo §10.6, RULE-MM §maturidade)
  - Governança/Avaliação/Maturidade: SPEC-019 v1.0 (RULE-HG-01..08, RULE-HV-01..04); SPEC-020 v1.0
      (9 lentes/RULE-EV-01..07); SPEC-021 v1.0 (RULE-MM-01..07; nível-alvo L3; gate E3 RULE-MM-05)
  - Enforcement: ENF-01..08 (ênfase ENF-03 Detector≠Gate; ENF-04 fail-closed; ENF-07 falso-DENY no E3)
  - Invariantes: INV-05 (SOT não executa; o Blackboard guarda estado de análise), INV-06 (Evidência≠Observação),
      INV-07 (versionamento monotônico — nada deletado), INV-09 (sem baseline informal), INV-10 (CEM-001 idioma)
  - Setup operacional (fronteira soberana, NÃO redefinida): WORKFLOW.md (versão vigente) — o Blackboard é o
      substrato de estado que o pipeline usa; a SPEC-004 não contradiz nenhum WF-xx e NÃO fecha WF-D03

ADDED (delta local — o que esta spec acrescenta):
  - Contrato de objeto publicado: identidade, versão, estado (operacional), namespace/workspace, proveniência
    (computed_by/gate_record — BL-029), permissões, timestamp, referência de supersessão
  - Protocolo de publicação/leitura/atualização (D6): o quê/quando/ordem/versão de publicação
  - Concorrência: versionamento otimista (rejeitar escrita com expected_version divergente); idempotência por
    chave de publicação (retry seguro); ordenação de publicações no workspace
  - Ciclo de vida append-only com SUPERSESSÃO (update→nova versão; expiração/invalidação não-destrutivas)
  - Proveniência/lineage lógica + API de reconstrução histórica por replay (storage físico por referência)
  - Observabilidade do gate de escrita E3 (método de falso-DENY — BL-002/ENF-07)
  - [PROPOSTA] M-001: estados de objetos NÃO-hipótese (Evidência/Missão/Observação/Convicção) como
    append-only + supersessão projetando o ciclo do CEM-001 — NÃO fechada (CONS-01; decisão de Andraus)
  - Declaração de Classe/Mecanismo por BASpec (CC-11); Enforcement Contracts (EC-CBP-001..006)

MODIFIED (especialização de regra herdada):
  - (nenhuma) — RULE-BB-003 já estava SUPERSEDED antes desta Spec (Q-006); a SPEC-004 apenas a cita no estado
    vigente (superseded), não a altera. RULE-BB-001/002/004/005 são operacionalizadas (protocolo), não alteradas
    em texto nem significado (RULE-HD-02 respeitada).

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal / obrigação-a-obrigação** sobre **regras (RULE-BB) e modelos canônicos** (EUA-E04 §8.3). O eixo **VERTICAL** (RULE-HV-01..04, conservação-como-conjunto pai→filha macro-harness) foi avaliado e **não se aplica**: a SPEC-004 não é decomposição *micro* de uma *macro-spec* — deriva de regras e objetos canônicos vizinhos. A regra ESCRITA de conservação-como-conjunto vertical será redigida junto da SPEC-019/derivadas; aqui não é invocada. [INFERÊNCIA — a confirmar pelo Revisor]

---

## Declaração de acepção semântica (RULE-SEM-01 — CC-10)

> **Termo 1:** "estado do objeto no Blackboard". **Acepção adotada:** o **ciclo operacional** de publicação/versão/supersessão de um objeto no quadro (ex.: COMPUTED→PUBLISHED→SUPERSEDED). **Não é** a máquina de estados da hipótese (CHM-001: EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→ARCHIVED), que o Blackboard **não redefine** (RULE-BB-003 SUPERSEDED por Q-006 — o Blackboard não tem estado de hipótese próprio). Para objetos NÃO-hipótese, o enum de estados é **M-001 (ABERTA)** — este Plan só **propõe** a mecânica append-only+supersessão.
> **Termo 2:** "Observação" (produzida por Skill, determinística) ≠ "Evidência" (produzida por Agente, interpretada — INV-06). O Blackboard armazena ambas sob seus contratos, sem confundi-las.
> **Termo 3:** "memória de trabalho" (Blackboard — volátil para a análise corrente, append-only) ≠ "memória permanente" (Knowledge Graph — SPEC-006). Fronteira declarada; a SPEC-004 não absorve o KG.
> [FONTE: RULE-SEM-01/04; RULES.md RULE-BB-003; CHM-001; INV-06; GLOSSARIO]

---

## Conformidade com o `WORKFLOW.md` (RULE-ECC-05 — determinação de NÃO-incidência)

> **Determinação: RULE-ECC-05 (Pesquisa Multi-Lente) NÃO INCIDE sobre a SPEC-004** [FONTE: DHR-SPEC004-001 §1 — "RULE-ECC-05 (Multi-Lente) não incide — confirmado pelo Revisor"]. Fundamento (research.md §7): a SPEC-004 **não define nem toca comportamento de agente analítico, do Conviction/Fusion Engine, do Manager ou do Risk Agent** — é infraestrutura de memória de trabalho, análoga às Specs de meta-harness excluídas (SPEC-002/019/020/021).
> **Mesmo não incidindo, por prudência confirma-se conformidade:** o Blackboard é o substrato de estado que o pipeline usa; **não contradiz** nenhum `WF-xx` e **não fecha** `WF-D03` (não toca convicção/J-001). Autoridade soberana do `WORKFLOW.md` preservada; divergência seria achado do Revisor, resolvida por Andraus. [FONTE: research.md §7; WORKFLOW.md versão vigente]

---

## D0 — Missão (Intenção)

A SPEC-004 especifica **como o SOT mantém, publica, versiona, supersede e reconstrói os objetos da sua memória de trabalho compartilhada (o Blackboard Cognitivo)** — definindo o **contrato do objeto publicado** (identidade, versão, estado operacional, namespace/workspace, proveniência, permissões, timestamp, supersessão), o **protocolo de publicação/leitura/atualização**, a **concorrência/ordenação/idempotência** de escrita, o **ciclo de vida append-only** (nada deletado — INV-07) e a **reconstrução histórica** por replay — preservando: a **comunicação exclusiva via Blackboard** (RULE-BB-001), a **escrita só no próprio workspace** (RULE-BB-002), o **append-only/supersessão** (RULE-BB-004), a **não-redefinição** dos contratos canônicos armazenados (CHM-001/CEM-001/CCM-001 — CC-02) e a fronteira **INV-05** (o Blackboard guarda estado de análise; não executa, não transporta eventos, não decide). [FONTE: ROADMAP §5; RULES.md RULE-BB-001..005; research.md §5]

**O que a Missão NÃO é (fronteira):**
- Não **transporta** eventos/mudanças (envelope, subscrição, TTL, correlation/causation, retry, replay de eventos, dead-letter) → **SPEC-005 (Event Bus)**. Princípio: *"Blackboard guarda estado; Event Bus transporta mudanças."*
- Não é **memória permanente** / ontologia / grafo → **SPEC-006 (Knowledge Graph)**; **H-001** (grafo real vs. memória) **ABERTA** — não tocar.
- Não define **estado persistente por agente** → **SPEC-009**; **G-001** **ABERTA** — não tocar.
- Não **orquestra** (quem pensa, quando, consenso de controle) → **SPEC-008 (Manager)**; o Blackboard é quadro, não controlador (RULE-BB-005).
- Não **redefine** CHM-001/CEM-001/CCM-001 (estados/campos/ciclo/linhagem) → **CC-02/CONST-01**.
- Não **computa** convicção nem fixa fórmula/pesos/limiares → **SPEC-003/CCM-001** (baselined); **J-001/N-001 ABERTAS**.
- Não **fecha** os estados do Blackboard para objetos não-hipótese → **M-001 ABERTA** (só [PROPOSTA] neste Plan; decisão de Andraus).
- Não especifica **guardrails de runtime** / allow-deny de escrita em produção → **SPEC-042**.

**Status epistemológico:** a SPEC-004 é FATO ARQUITETURAL candidato a baseline; RULE-CBP-* e o contrato de objeto por ela propostos são **[PROPOSTA]** até homologação. RULE-BB-001..005, CHM-001, CEM-001, CCM-001, SPEC-001/019/020/021, atomic-spec v1.5, INV-*, ENF-*, RULES v1.5 são FATO NORMATIVO. Fontes externas (research.md §2, SRC-*/REPO-*) são [EXTERNO] — DADO, nunca baseline; documentado ≠ homologado (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | **Contrato do objeto publicado:** identidade (`object_id`), `version`, `state` (operacional), `namespace`/`workspace`, proveniência (`computed_by`/`gate_record`/`derived_from` — BL-029), `permissions`, `timestamp`, `supersedes`/`superseded_by` | RULE-BB-002/004; research.md §3.4; BL-029 |
| S2 | **Protocolo de publicação/leitura/atualização (D6):** o quê/quando/ordem/versão; leitura de qualquer workspace, escrita só no próprio | RULE-BB-001/002; research.md §3.1 |
| S3 | **Ciclo de vida append-only:** criação, atualização (nova versão), **supersessão**, expiração e invalidação **não-destrutivas** (SUPERSEDED/ARCHIVED, nunca deletado) | RULE-BB-004; INV-07; research.md §3.2/§3.5 |
| S4 | **Concorrência/ordenação/idempotência:** versionamento otimista (rejeita `expected_version` divergente); chave de idempotência por publicação (retry seguro); ordenação de publicações no workspace | research.md §3.3; SRC-CONC-01 [EXTERNO] |
| S5 | **Proveniência e reconstrução histórica:** `quem publicou / qual atividade / derivado de qual objeto / versão`; API lógica de reconstrução por **replay** — storage físico por referência | research.md §3.4/§3.5; W3C PROV [EXTERNO]; P13 |
| S6 | **Relação Blackboard × memória permanente:** Blackboard = memória de trabalho; KG (SPEC-006) = permanente — fronteira declarada | ROADMAP §5 |
| S7 | **Enforcement Contracts** dos atos com efeito: piso **E2** (publicação em estado compartilhado); **E3** no gate de escrita/append-only (cross-workspace e deleção destrutiva são irreversíveis → fail-closed; ENF-07 falso-DENY → BL-002) | ENF-01/02/04/07; atomic-spec §10.2 |
| S8 | **Classe/Mecanismo por BASpec** (CC-11) e **auditabilidade (D9 por referência)** para reconstrução (P13; RULE-010) | RULE-MECH-01; CONSTITUTION P13; RULE-010 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Transporte de eventos/mudanças (envelope, subscrição, TTL, correlation/causation, retry, replay de eventos, dead-letter) | **SPEC-005 (Event Bus)** | "Blackboard guarda estado; Event Bus transporta mudanças" |
| Memória permanente / ontologia / grafo | **SPEC-006 (KG)** — **H-001 ABERTA** | KG é memória permanente |
| Estado persistente **por agente** | **SPEC-009** — **G-001 ABERTA** | persistência por agente |
| Redefinir CHM-001 / CEM-001 / CCM-001 | canônicos baselined | **CC-02/CONST-01** — só armazenar/versionar |
| Fórmula/pesos/limiares de convicção | **SPEC-003/CCM-001; J-001/N-001 ABERTAS** | INV-03/INV-04; o Blackboard não computa convicção |
| Orquestração (quem pensa, quando, consenso de controle) | **SPEC-008 (Manager)** | controle ≠ quadro (RULE-BB-005) |
| Guardrails de runtime / allow-deny de escrita em produção | **SPEC-042** | runtime |
| **Estados do Blackboard para objetos não-hipótese** (enum definitivo) | **M-001 ABERTA — decisão de Andraus** | só [PROPOSTA] neste Plan (CONS-01) |
| Mecanismo físico de storage (grafo real vs. memória) | **SPEC-006 / H-001 ABERTA** | infraestrutura física |
| Adotar CRDT (yjs/automerge) como baseline de concorrência | — | **ADIADO** (research.md §3.3/§4-bis) — RULE-BB-002 (escritor único por workspace) torna optimistic concurrency suficiente; CRDT = INDETERMINADO quanto à necessidade |

---

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide** (DHR-SPEC004-001 §1). O Cognitive Blackboard Protocol é **infraestrutura de memória de trabalho agnóstica de escola** — não define escopo de especialidade de mercado (Elliott/SMC/ICT). Nenhum `PD-xx` é proposto (CC-12 = N/A). Registrado explicitamente para o Revisor — não é supressão silenciosa. Nuance honesta (RULE-MET-01): RULE-ECC-05 não incidir reforça que a Spec não toca comportamento de especialidade. [FONTE: RULE-PD-01; atomic-spec §10.7; DHR-SPEC004-001 §1]

---

## D2 — Regras

> **Etiqueta:** as RULE-CBP-* e o contrato de objeto abaixo são **[PROPOSTA]** — tornam-se normativos apenas na homologação de Andraus + registro pelo Controlador (RULE-HG-02). Até lá, não são invocáveis como FATO NORMATIVO. As RULE/INV/ENF citadas como fundamento (RULE-BB-001..005, INV-05/06/07/09/10, ENF-03/04/07, RULE-010, CHM-001/CEM-001/CCM-001) **já existem** e são FATO NORMATIVO.

```
RULE-CBP-001: Todo objeto publicado no Blackboard DEVE carregar o contrato mínimo — object_id, version,
              state (operacional), namespace/workspace, proveniência (computed_by; gate_record quando o
              objeto resulta de um gate; derived_from quando derivado), permissions, timestamp e, quando
              substitui outro, supersedes. O contrato mínimo DISTINGUE CRIAÇÃO de ATUALIZAÇÃO: numa
              ATUALIZAÇÃO (objeto já existente no workspace) o contrato mínimo INCLUI expected_version;
              numa CRIAÇÃO (objeto novo, sem versão anterior) expected_version NÃO é exigido (versão
              inicial). Objeto sem o contrato mínimo é REJEITADO (fail-closed).
              [Fonte: RULE-BB-002/004; BL-029; INV-10]  [PROPOSTA]

RULE-CBP-002: Um agente PODE LER qualquer workspace, mas PODE PUBLICAR apenas no workspace de sua
              responsabilidade; publicação em workspace alheio é REJEITADA (fail-closed). O LLM nunca é o
              gate da permissão — o gate é determinístico (ENF-03).
              [Fonte: RULE-BB-002; ENF-03]  [PROPOSTA]

RULE-CBP-003: O Blackboard é append-only: atualizar um objeto cria uma NOVA versão; o objeto anterior é
              SUPERSEDED (nunca deletado). Deleção destrutiva é REJEITADA (fail-closed) — efeito irreversível
              proibido (INV-07; RULE-BB-004).
              [Fonte: RULE-BB-004; INV-07]  [PROPOSTA]

RULE-CBP-004: A escrita usa versionamento OTIMISTA: a publicação de ATUALIZAÇÃO só é aceita se a versão
              esperada (expected_version) está PRESENTE e coincide com a versão corrente do objeto no
              workspace; divergência é REJEITADA (conflito de concorrência, VERSION_CONFLICT) sem corromper
              o estado. A AUSÊNCIA de expected_version numa ATUALIZAÇÃO é REJEITADA (fail-closed, código
              EXPECTED_VERSION_REQUIRED) — atualização cega (sem controle de concorrência) é proibida. A
              CRIAÇÃO de objeto novo (sem versão anterior) NÃO exige expected_version (versão inicial).
              [Fonte: research.md §3.3; SRC-CONC-01 [EXTERNO]]  [PROPOSTA]

RULE-CBP-005: Toda publicação carrega uma CHAVE DE IDEMPOTÊNCIA; reprocessar a mesma publicação (retry) NÃO
              DEVE criar objeto/versão duplicado — o resultado é idêntico ao do primeiro processamento.
              [Fonte: research.md §3.3; SRC-CONC-01 [EXTERNO]]  [PROPOSTA]

RULE-CBP-006: As publicações num mesmo workspace DEVEM ter ordem determinística e reconstruível (ordem total
              por workspace); eventos/publicações fora de ordem NÃO DEVEM produzir estado ambíguo.
              [Fonte: research.md §3.3; P13]  [PROPOSTA]

RULE-CBP-007: Todo objeto publicado DEVE ter proveniência suficiente para reconstrução (P13/RULE-010):
              computed_by (quem/qual atividade), derived_from (ancestrais, quando aplicável) e, quando o
              objeto resulta de um gate, gate_record (resultado + limiares usados). O Blackboard NÃO fixa
              sobre qual valor um gate consumidor opera (fronteira SPEC-003/N3 — não reaberta).
              [Fonte: BL-029; RULE-010; CONSTITUTION P13; W3C PROV [EXTERNO]]  [PROPOSTA]

RULE-CBP-008: O Blackboard NÃO define estado próprio de HIPÓTESE — objetos-hipótese usam a máquina de estados
              do CHM-001 (EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→ARCHIVED). RULE-BB-003
              (PROPOSED/VALIDATED) está SUPERSEDED por Q-006 (RULES.md l.316–321) e NÃO DEVE ser usada.
              [Fonte: RULES.md RULE-BB-003 [SUPERSEDED por Q-006]; CHM-001 §1.7; CC-02]  [PROPOSTA]

RULE-CBP-009: Os ESTADOS do Blackboard para objetos NÃO-hipótese (Evidência, Missão, Observação, Convicção)
              são [PROPOSTA] append-only + SUPERSESSÃO, projetando o ciclo de vida do CEM-001 (update→nova
              versão; invalidação/expiração→estado terminal, nunca deleção). O ENUM DEFINITIVO de estados é
              M-001 (ABERTA) — NÃO fixado aqui; decisão de Andraus na homologação do Plan (CONS-01).
              [Fonte: M-001 (ABERTA); CEM-001 Cap.4; INV-07; research.md §3.2/§5.1]  [PROPOSTA / DECISÃO NECESSÁRIA]

RULE-CBP-010: Expiração e invalidação de objetos de memória de trabalho são NÃO-DESTRUTIVAS: o objeto
              transita para estado terminal (SUPERSEDED/ARCHIVED/EXPIRED) preservando o histórico (INV-07);
              ausência de atualização não implica deleção.
              [Fonte: RULE-BB-004; INV-07; CEM-001 Cap.4]  [PROPOSTA]

RULE-CBP-011: O estado do Blackboard DEVE ser reconstruível por REPLAY das versões append-only (reconstrução
              histórica). O mecanismo FÍSICO de storage (grafo real vs. memória) é H-001/SPEC-006 e o estado
              por agente é G-001/SPEC-009 — NÃO fixados aqui (por referência).
              [Fonte: P13; RULE-010; H-001/G-001 (ABERTAS); SRC-ES-01 [EXTERNO]]  [PROPOSTA]

RULE-CBP-012: O gate de escrita E3 (permissão/append-only) DEVE declarar método amostral de observação de
              falso-DENY (publicação válida negada por engano) — ENF-07. O LIMIAR amostral é gap de
              enforcement aberto (atomic-spec §12), não fixado aqui.
              [Fonte: ENF-07; BL-002; atomic-spec §12]  [PROPOSTA]
```

---

## Notas de honestidade (anti-sobreafirmação — RULE-MET-01) [FONTE]

- **M-001 é PROPOSTA, não decisão.** Este Plan propõe os estados de objetos não-hipótese como append-only + supersessão (RULE-CBP-009), projetando o CEM-001. **Não fecha M-001** — o enum definitivo e a eventual necessidade de estados extra (ex.: contradiction markers do SRC-MEM-01 [EXTERNO]) são decisão de Andraus na homologação do Plan (CONS-01).
- **CRDT = INDETERMINADO quanto à necessidade.** yjs/automerge (REPO-yjs/REPO-automerge [EXTERNO], elegíveis) resolvem co-edição multi-escritor; sob RULE-BB-002 (escritor único por workspace) o versionamento otimista basta. CRDT **adiado**, não rejeitado — registrado caso surja escrita multi-escritor no mesmo workspace (research.md §3.3/§5). Não presumir necessidade (RULE-MET-01).
- **mem0 (ADD/UPDATE/DELETE/NOOP) adaptado, não adotado.** REPO-mem0 [EXTERNO] traz ciclo de vida de objeto de memória, mas **DELETE destrutivo é incompatível com RULE-BB-004/INV-07** → adaptado para append-only/supersessão (research.md §4-bis). Não adotar literalmente.
- **ACH-001 (aviso de método — SRC-MEM-01):** a URL `arXiv 2606.24535` de SRC-MEM-01 pertence à família de IDs implausíveis/futuros que o aviso de método do Dossiê descartou. Portanto ela é tratada como **NÃO load-bearing**: a convergência "Blackboard = centralized shared memory governed" apoia-se na página `emergentmind.com` e no enquadramento geral do survey (DADO [EXTERNO]), **não** nessa URL arXiv; nenhuma proposta deste Plan é importada dela. O aviso de método do Dossiê permanece íntegro (research.md §aviso). [FONTE: DHR-SPEC004-001 ACH-001; research.md §aviso de método / SRC-MEM-01]

---

## Critérios de Aceitação (EARS)

1. Quando um objeto é submetido para publicação no Blackboard, o Blackboard DEVE aceitá-lo somente se carrega o contrato mínimo (object_id, version, state, workspace, proveniência, timestamp) e DEVE rejeitar (fail-closed) objeto sem esses campos.
2. Quando um agente tenta publicar num workspace que não é o seu, o Blackboard DEVE rejeitar a escrita (RULE-BB-002) e NÃO DEVE alterar o estado compartilhado.
3. Quando um objeto existente é atualizado, o Blackboard DEVE criar uma nova versão e marcar a anterior como SUPERSEDED, e NÃO DEVE deletar a versão anterior (append-only, INV-07).
4. Quando uma publicação chega com expected_version divergente da versão corrente, o Blackboard DEVE rejeitar a escrita como conflito de concorrência e NÃO DEVE corromper o objeto.
4-bis. Quando uma publicação de ATUALIZAÇÃO (o objeto já existe no workspace) não informa expected_version, o Blackboard DEVE rejeitar a escrita (fail-closed) com o código "EXPECTED_VERSION_REQUIRED" e NÃO DEVE aplicar a atualização; a CRIAÇÃO de objeto novo (sem versão anterior) permanece permitida sem expected_version (create = versão inicial).
5. Quando a mesma publicação é reprocessada (retry) com a mesma chave de idempotência, o Blackboard NÃO DEVE criar objeto/versão duplicado.
6. Quando publicações concorrentes chegam ao mesmo workspace, o Blackboard DEVE impor ordem determinística e reconstruível e NÃO DEVE produzir estado ambíguo.
7. Quando um objeto é publicado, o Blackboard DEVE registrar sua proveniência (computed_by; derived_from/gate_record quando aplicável) suficiente para reconstrução (P13).
8. Quando um objeto-hipótese é armazenado, o Blackboard DEVE usar os estados do CHM-001 e NÃO DEVE definir estado de hipótese próprio (RULE-BB-003 SUPERSEDED por Q-006).
9. Quando um objeto de memória de trabalho expira ou é invalidado, o Blackboard DEVE transitá-lo para estado terminal preservando o histórico e NÃO DEVE deletá-lo.
10. Quando o estado do Blackboard precisa ser reconstruído, o Blackboard DEVE permitir replay das versões append-only, sem fixar o mecanismo físico de storage (H-001/SPEC-006).
11. Quando o gate de escrita E3 nega uma publicação, o Blackboard DEVE registrar observabilidade amostral de falso-DENY (ENF-07) para auditoria posterior.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec com efeito declara o bloco **CLASSE/MECANISMO** (§10.6). D = determinístico; C = constitutivo (é o próprio gate); H = híbrido (LLM/juízo + gate de saída determinístico + bounded loop); P = probabilístico com gate.

### BASpec-CBP-001 — Contrato de objeto publicado (rejeita objeto malformado)

```
BASpec-CBP-001:
  QUANDO:       Um objeto é submetido para publicação no Blackboard
  ENTÃO:        O Blackboard aceita somente se o objeto carrega o contrato mínimo (object_id, version, state,
                namespace/workspace, proveniência computed_by, timestamp); objeto sem o contrato é rejeitado
                (fail-closed), sem alterar o estado compartilhado
  PORQUE:       Objeto publicado sem contrato/proveniência contamina a reconstrução (P13) e toda a cadeia
  REFERÊNCIA:   RULE-BB-002/004; BL-029; RULE-CBP-001; INV-10
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de validação do contrato mínimo antes de admitir no quadro
    GATE DE SAÍDA: verificação binária (todos os campos mínimos presentes ∧ proveniência ≠ vazia)
    CRITÉRIO 4Es: Conformidade > Eficácia — proteger a integridade/auditabilidade do quadro
  VERIFICADO POR:
    DADO        um objeto sem campo de proveniência submetido ao Blackboard
    QUANDO      a publicação é processada
    ENTÃO       publicação rejeitada; estado inalterado
    VERIFICAÇÃO publish_accepted == false; shared_state_changed == false
```

### BASpec-CBP-002 — Permissão de escrita por workspace (lê qualquer; publica só no próprio) [E3]

```
BASpec-CBP-002:
  QUANDO:       Um agente tenta publicar num workspace
  ENTÃO:        O Blackboard permite a escrita somente no workspace de responsabilidade do agente; publicação
                em workspace alheio é rejeitada (fail-closed); leitura de qualquer workspace é permitida
  PORQUE:       Escrita só no próprio workspace, leitura livre (RULE-BB-002); cross-workspace corrompe o
                estado compartilhado (efeito irreversível) — fail-closed; o LLM nunca é o gate (ENF-03)
  REFERÊNCIA:   RULE-BB-002; ENF-03/04; RULE-CBP-002
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de autorização por (agent_id, workspace); checagem binária de posse
    GATE DE SAÍDA: verificação (workspace == workspace_do_agente) para escrita
    CRITÉRIO 4Es: Conformidade > Eficácia — isolamento de workspace é inviolável (RULE-BB-002)
  VERIFICADO POR:
    DADO        agente A tenta publicar no workspace de B
    QUANDO      o gate de permissão roda
    ENTÃO       escrita rejeitada "WORKSPACE_WRITE_FORBIDDEN"; nada publicado
    VERIFICAÇÃO error_code == "WORKSPACE_WRITE_FORBIDDEN"; cross_workspace_write == false
```

### BASpec-CBP-003 — Append-only / supersessão (update = nova versão; nunca deleta)

```
BASpec-CBP-003:
  QUANDO:       Um objeto existente é atualizado no Blackboard
  ENTÃO:        O Blackboard cria uma NOVA versão e marca a anterior como SUPERSEDED (superseded_by preenchido);
                a versão anterior é preservada; deleção destrutiva é rejeitada (fail-closed)
  PORQUE:       Blackboard append-only; objetos são SUPERSEDED, nunca deletados (RULE-BB-004; INV-07)
  REFERÊNCIA:   RULE-BB-004; INV-07; RULE-CBP-003
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que barra deleção + cria versão sucessora com ligação supersedes/superseded_by
    GATE DE SAÍDA: verificação (nenhuma deleção aplicada ∧ versão anterior preservada ∧ ligação de supersessão)
    CRITÉRIO 4Es: Conformidade > Eficácia — versionamento monotônico (INV-07) é inviolável
  VERIFICADO POR:
    DADO        objeto O v1 atualizado para O v2
    QUANDO      a atualização roda
    ENTÃO       O v1 preservado como SUPERSEDED; O v2 ACTIVE; nada deletado
    VERIFICAÇÃO v1.state == "SUPERSEDED"; v1_deleted == false; v2.supersedes == "O@v1"
```

### BASpec-CBP-004 — Versionamento otimista (rejeita expected_version divergente)

```
BASpec-CBP-004:
  QUANDO:       Uma publicação de ATUALIZAÇÃO (o objeto já existe) chega, informando OU OMITINDO a versão
                esperada do objeto (expected_version)
  ENTÃO:        O Blackboard aceita a escrita somente se expected_version está PRESENTE e == versão corrente;
                expected_version divergente é rejeitada como conflito de concorrência ("VERSION_CONFLICT");
                expected_version AUSENTE numa atualização é rejeitada (fail-closed) com "EXPECTED_VERSION_REQUIRED"
                e a atualização NÃO é aplicada; em nenhum caso o objeto é corrompido nem há escrita parcial. A
                CRIAÇÃO de objeto novo (sem versão anterior) é permitida sem expected_version (versão inicial)
  PORQUE:       Versionamento otimista: aceitar só se a versão corrente coincide com a esperada; atualização
                sem expected_version é escrita cega (sem controle de concorrência) → proibida (SRC-CONC-01)
  REFERÊNCIA:   RULE-CBP-001/004; research.md §3.3; SRC-CONC-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : comparação determinística expected_version == current_version; exige expected_version
                  PRESENTE em atualização (ausente ⇒ EXPECTED_VERSION_REQUIRED), dispensada em criação;
                  rejeição atômica se diverge ou ausente
    CRITÉRIO 4Es: Eficácia — integridade do estado concorrente; determinismo garante reprodutibilidade (P13)
  VERIFICADO POR:
    DADO        objeto O na versão 3; publicação com expected_version == 2
    QUANDO      a escrita roda
    ENTÃO       rejeição "VERSION_CONFLICT"; O permanece na versão 3
    VERIFICAÇÃO error_code == "VERSION_CONFLICT"; object_corrupted == false
    DADO        objeto O já existente (v3); publicação de ATUALIZAÇÃO sem expected_version
    QUANDO      a escrita roda
    ENTÃO       rejeição "EXPECTED_VERSION_REQUIRED"; O permanece na versão 3; atualização não aplicada
    VERIFICAÇÃO error_code == "EXPECTED_VERSION_REQUIRED"; update_applied == false; object_corrupted == false
```

### BASpec-CBP-005 — Idempotência por chave de publicação (retry seguro)

```
BASpec-CBP-005:
  QUANDO:       A mesma publicação (mesma chave de idempotência) é processada mais de uma vez (retry)
  ENTÃO:        O Blackboard produz o mesmo resultado do primeiro processamento e NÃO cria objeto/versão
                duplicado
  PORQUE:       Idempotência garante processamento exatamente-uma-vez mesmo sob retry/falha (SRC-CONC-01)
  REFERÊNCIA:   RULE-CBP-005; research.md §3.3; SRC-CONC-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : deduplicação determinística por idempotency_key; segunda ocorrência é no-op idempotente
    CRITÉRIO 4Es: Eficácia — evitar duplicata preserva a integridade do quadro; Eficiência (retry barato e seguro)
  VERIFICADO POR:
    DADO        publicação P com idempotency_key K processada duas vezes
    QUANDO      o segundo processamento roda
    ENTÃO       nenhum objeto/versão duplicado; resultado idêntico ao primeiro
    VERIFICAÇÃO duplicate_created == false; result_identical == true
```

### BASpec-CBP-006 — Ordenação determinística de publicações no workspace

```
BASpec-CBP-006:
  QUANDO:       Publicações concorrentes ou fora de ordem chegam ao mesmo workspace
  ENTÃO:        O Blackboard impõe uma ordem total determinística por workspace e produz estado reconstruível,
                não ambíguo
  PORQUE:       Ordem reconstruível é pré-condição de reconstrução histórica (P13); fora-de-ordem não deve
                gerar estado ambíguo (SRC-CONC-01)
  REFERÊNCIA:   RULE-CBP-006; P13; SRC-CONC-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : atribuição determinística de ordem (sequência por workspace); resolução estável de concorrência
    CRITÉRIO 4Es: Eficácia — ordem determinística garante reconstrução unívoca
  VERIFICADO POR:
    DADO        duas publicações concorrentes no mesmo workspace
    QUANDO      ambas são admitidas
    ENTÃO       ordem total determinística atribuída; replay reproduz o mesmo estado
    VERIFICAÇÃO total_order_assigned == true; replay_deterministic == true
```

### BASpec-CBP-007 — Proveniência obrigatória (computed_by / gate_record / derived_from) [BL-029]

```
BASpec-CBP-007:
  QUANDO:       Um objeto é publicado no Blackboard
  ENTÃO:        O Blackboard exige proveniência suficiente para reconstrução — computed_by (quem/qual
                atividade), derived_from (ancestrais, quando derivado) e gate_record (resultado + limiares,
                quando o objeto resulta de um gate); objeto sem a proveniência exigível é rejeitado; o
                Blackboard NÃO fixa sobre qual valor um gate consumidor opera (fronteira SPEC-003/N3)
  PORQUE:       Reconstrução D9 (P13/RULE-010) exige proveniência; BL-029 (dona=SPEC-004) materializa aqui
  REFERÊNCIA:   RULE-CBP-007; BL-029; RULE-010; CONSTITUTION P13; W3C PROV [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de presença de proveniência (projeta o Lineage do CEM-001, não o redefine)
    GATE DE SAÍDA: verificação (computed_by presente ∧ gate_record presente quando resulta de gate)
    CRITÉRIO 4Es: Conformidade > Eficácia — proveniência é condição de auditabilidade (D9)
  VERIFICADO POR:
    DADO        objeto que resultou de um gate, publicado sem gate_record
    QUANDO      a publicação roda
    ENTÃO       rejeição "PROVENANCE_REQUIRED"; nada publicado
    VERIFICAÇÃO error_code == "PROVENANCE_REQUIRED"
```

### BASpec-CBP-008 — Objeto-hipótese usa estados do CHM-001 (Blackboard não define estado de hipótese) [ACH-002]

```
BASpec-CBP-008:
  QUANDO:       Um objeto-hipótese é armazenado/publicado no Blackboard
  ENTÃO:        O Blackboard usa a máquina de estados do CHM-001 para a hipótese e NÃO define estado de
                hipótese próprio; uma tentativa de aplicar o ciclo descontinuado PROPOSED/VALIDATED
                (RULE-BB-003 SUPERSEDED por Q-006) é rejeitada
  PORQUE:       RULE-BB-003 está SUPERSEDED por Q-006 (RULES.md l.316–321); os estados da hipótese são do
                CHM-001 (EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→ARCHIVED); CC-02 (não redefinir)
  REFERÊNCIA:   RULES.md RULE-BB-003 [SUPERSEDED por Q-006]; CHM-001 §1.7; RULE-CBP-008; CC-02
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que recusa estado de hipótese fora do enum CHM-001 (sem redefinir CHM-001)
    GATE DE SAÍDA: verificação (estado da hipótese ∈ enum CHM-001)
    CRITÉRIO 4Es: Conformidade > Eficácia — não redefinir canônico (CC-02/CONST-01)
  VERIFICADO POR:
    DADO        tentativa de publicar hipótese com estado "VALIDATED" (ciclo descontinuado)
    QUANDO      o gate de estado roda
    ENTÃO       rejeição "HYPOTHESIS_STATE_MUST_BE_CHM001"; estado CHM-001 exigido
    VERIFICAÇÃO error_code == "HYPOTHESIS_STATE_MUST_BE_CHM001"; blackboard_defines_hypothesis_state == false
```

### BASpec-CBP-009 — Estados de objetos NÃO-hipótese: append-only + supersessão [PROPOSTA — M-001 ABERTA]

```
BASpec-CBP-009:
  QUANDO:       Um objeto NÃO-hipótese (Evidência/Missão/Observação/Convicção) muda de estado no Blackboard
  ENTÃO:        O Blackboard aplica a mecânica append-only + SUPERSESSÃO (update→nova versão; invalidação/
                expiração→estado terminal, nunca deleção), projetando o ciclo de vida do CEM-001; o ENUM
                DEFINITIVO de estados é M-001 (ABERTA) — NÃO fixado neste Plan
  PORQUE:       DELETE/UPDATE destrutivos (padrão mem0 [EXTERNO]) violam RULE-BB-004/INV-07 → adaptados para
                append-only/supersessão alinhados ao CEM-001; M-001 é decisão de Andraus (CONS-01)
  REFERÊNCIA:   M-001 (ABERTA); CEM-001 Cap.4; INV-07; RULE-CBP-009; research.md §3.2/§4-bis
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico append-only (barra deleção) + mecânica de supersessão; enum = M-001 (aberto)
    GATE DE SAÍDA: verificação (transição não-destrutiva ∧ histórico preservado)
    CRITÉRIO 4Es: Conformidade > Eficácia — preservar histórico; não antecipar M-001
  VERIFICADO POR:
    DADO        uma Evidência no Blackboard é invalidada
    QUANDO      a transição roda
    ENTÃO       objeto em estado terminal append-only; histórico preservado; enum = M-001 (não fixado)
    VERIFICAÇÃO destructive_delete == false; history_preserved == true; m001_states_fixed == false
```

### BASpec-CBP-010 — Expiração/invalidação não-destrutiva

```
BASpec-CBP-010:
  QUANDO:       Um objeto de memória de trabalho expira ou é invalidado
  ENTÃO:        O Blackboard transita o objeto para estado terminal (SUPERSEDED/ARCHIVED/EXPIRED) preservando
                o histórico; ausência de atualização NÃO implica deleção
  PORQUE:       Append-only; nada é deletado (RULE-BB-004; INV-07); o ciclo projeta o CEM-001 Cap.4
  REFERÊNCIA:   RULE-CBP-010; RULE-BB-004; INV-07; CEM-001 Cap.4
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : marcação determinística de estado terminal por política de expiração/invalidação; sem deleção
    CRITÉRIO 4Es: Eficácia — expiração correta libera a memória de trabalho sem perder auditabilidade
  VERIFICADO POR:
    DADO        objeto cuja janela de validade expirou
    QUANDO      a política de expiração roda
    ENTÃO       objeto em estado terminal; recuperável para auditoria; não deletado
    VERIFICAÇÃO terminal_state == true; object_deleted == false; auditable == true
```

### BASpec-CBP-011 — Reconstrução histórica por replay (storage físico por referência) [D9]

```
BASpec-CBP-011:
  QUANDO:       É necessário reconstruir o estado do Blackboard num ponto do tempo
  ENTÃO:        O Blackboard reconstrói o estado por REPLAY das versões append-only, de forma determinística;
                o mecanismo FÍSICO de storage (grafo real vs. memória) NÃO é fixado (H-001/SPEC-006; G-001/SPEC-009)
  PORQUE:       Append-only permite replay/reconstrução (SRC-ES-01); P13 (toda decisão reconstruível);
                storage físico é fronteira (H-001/G-001 ABERTAS)
  REFERÊNCIA:   RULE-CBP-011; P13; RULE-010; SRC-ES-01 [EXTERNO]; H-001/G-001 (ABERTAS)
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : replay determinístico das versões ordenadas por workspace até o ponto solicitado
    CRITÉRIO 4Es: Eficácia — reconstrução fiel (P13); Economicidade não rebaixa a fidelidade
  VERIFICADO POR:
    DADO        histórico append-only de um workspace
    QUANDO      o replay até o instante T roda
    ENTÃO       estado reconstruído igual ao estado real em T; storage físico não fixado
    VERIFICAÇÃO reconstructed_state == state_at_T; physical_storage_fixed == false
```

### BASpec-CBP-012 — Observabilidade do gate de escrita E3 (falso-DENY) [BL-002 / ENF-07]

```
BASpec-CBP-012:
  QUANDO:       O gate de escrita E3 (permissão/append-only) nega uma publicação
  ENTÃO:        O Blackboard registra observabilidade amostral de falso-DENY (publicação válida negada por
                engano), para auditoria posterior; o LIMIAR amostral é gap de enforcement aberto (não fixado)
  PORQUE:       Unidade E3 declara método de falso-DENY (ENF-07); BL-002 (encaminhado à SPEC-004) materializa
                a observabilidade do Blackboard
  REFERÊNCIA:   RULE-CBP-012; ENF-07; BL-002; atomic-spec §12
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : amostragem determinística dos DENY do gate E3 + registro para auditoria; limiar = gap aberto
    CRITÉRIO 4Es: Efetividade — observar falso-DENY evita que o gate bloqueie escrita legítima em silêncio
  VERIFICADO POR:
    DADO        gate E3 negou um conjunto de publicações
    QUANDO      a observabilidade roda
    ENTÃO       amostra de DENY registrada para auditoria; limiar amostral não fixado
    VERIFICAÇÃO false_deny_sampling_recorded == true; sampling_threshold_fixed == false
```

---

## D4 — Algoritmo

Mecânicas **determinísticas reais** especificáveis (D4 "onde há regra determinística real" — atomic-spec §2):
- **Versionamento otimista (CBP-004):** numa ATUALIZAÇÃO, `aceita ⇔ (expected_version presente ∧ expected_version == current_version)`; `expected_version` divergente ⇒ `VERSION_CONFLICT`; `expected_version` ausente ⇒ `EXPECTED_VERSION_REQUIRED` (fail-closed, atualização cega proibida). Na CRIAÇÃO (objeto novo, sem versão anterior) `expected_version` não é exigido (versão inicial). Regra binária, sem parâmetro aberto.
- **Idempotência (CBP-005):** `se idempotency_key ∈ processed_keys ⇒ no-op (retorna resultado anterior); senão processa e registra a chave` — exatamente-uma-vez.
- **Permissão de escrita (CBP-002):** `aceita_escrita ⇔ workspace_alvo == workspace_do_agente`; leitura sempre permitida.
- **Append-only/supersessão (CBP-003):** `update(O) ⇒ nova versão v(n+1); O@v(n).state := SUPERSEDED; proibido delete(O)`.
- **Ordenação (CBP-006):** sequência monotônica por workspace (`seq := seq+1` na admissão); replay ordena por `(workspace, seq)`.
- **Replay (CBP-011):** `estado(T) := fold(aplica_versões ordenadas por (workspace, seq) até T)`.

Nenhuma fórmula depende de J-001/N-001 (o Blackboard não computa convicção). Não há limiar numérico de convicção neste Plan. [FONTE: atomic-spec §2; research.md §3.3]

---

## D5 — Máquina de estados (ciclo operacional do objeto no Blackboard)

> **Fronteira (CC-02):** este é o **ciclo operacional de PUBLICAÇÃO** de um objeto no quadro — **não** a máquina de estados da hipótese (CHM-001, não redefinida) nem o enum definitivo de objetos não-hipótese (**M-001 ABERTA**).

Ciclo operacional de publicação [PROPOSTA]:

| Estado | Descrição | Transições |
|---|---|---|
| ACCEPTED | Objeto admitido (contrato + permissão + proveniência válidos) | → PUBLISHED |
| PUBLISHED | Versão corrente visível no workspace | → SUPERSEDED (por nova versão) · → EXPIRED/ARCHIVED (expiração/invalidação) |
| SUPERSEDED | Substituído por nova versão (append-only — INV-07) | terminal (preservado) |
| EXPIRED / ARCHIVED | Expirado/invalidado não-destrutivamente | terminal (preservado, auditável) |
| REJECTED | Falhou no gate (contrato/permissão/versão/proveniência) — nada publicado | terminal |

> **Estados de objetos NÃO-hipótese = M-001 [DECISÃO NECESSÁRIA — ABERTA]:** o ENUM semântico dos objetos Evidência/Missão/Observação/Convicção (ex.: se há `CONTRADICTED`, `CONFIRMED`, etc.) **não é fixado aqui** — este Plan propõe apenas a **mecânica** (append-only + supersessão projetando o CEM-001). Andraus decide na homologação do Plan (CONS-01; RULE-CBP-009). [FONTE: M-001; CEM-001 Cap.4; research.md §5.1]
> **Estados da HIPÓTESE = CHM-001** (não redefinidos; RULE-BB-003 SUPERSEDED por Q-006). [FONTE: CHM-001; RULES.md l.316–321]

---

## D6 — Protocolo de publicação no Blackboard

### Workspaces e produtores [FONTE: RULE-BB-001/002]
- Cada agente/engine publica **apenas** no seu workspace; lê qualquer workspace.
- A comunicação entre componentes é **exclusivamente** via Blackboard (RULE-BB-001); nenhum componente fala direto com outro.

### Sequência de publicação (um objeto)
1. **Submissão:** o produtor submete objeto + `expected_version` + `idempotency_key` + proveniência.
2. **Idempotência (CBP-005):** se a chave já foi processada → no-op idempotente (retorna resultado anterior).
3. **Permissão (CBP-002, E3):** workspace alvo == workspace do produtor? Senão `WORKSPACE_WRITE_FORBIDDEN` (fail-closed).
4. **Contrato (CBP-001) + proveniência (CBP-007):** campos mínimos + computed_by/gate_record presentes? Senão rejeita.
5. **Concorrência (CBP-004):** `expected_version == current_version`? Senão `VERSION_CONFLICT`.
6. **Append-only/ordenação (CBP-003/CBP-006):** cria nova versão; marca anterior SUPERSEDED; atribui ordem (seq) no workspace.
7. **Publicação:** objeto PUBLISHED; reconstrução/proveniência anexada (P13/RULE-010).
8. **Expiração/invalidação (CBP-010):** quando aplicável, transição terminal não-destrutiva.
9. **Observabilidade (CBP-012):** DENY do gate E3 amostrado para auditoria (ENF-07/BL-002).

> **Nota de fronteira:** o **transporte** da notificação de mudança (quem é avisado, com que envelope/retry) é do **Event Bus (SPEC-005)** — "Blackboard guarda estado; Event Bus transporta mudanças". A **coordenação** de quem publica quando é do **Manager (SPEC-008)** (RULE-BB-005). [FONTE: ROADMAP §5; RULE-BB-005]

---

## D7 — Cenários de Teste

### Cenário-CBP-T01 — Contrato mínimo ausente → rejeição
```
DADO        objeto submetido sem proveniência (computed_by ausente)
QUANDO      a publicação roda
ENTÃO       rejeição; estado inalterado
VERIFICAÇÃO publish_accepted == false; shared_state_changed == false
```

### Cenário-CBP-T02 — Escrita cross-workspace → rejeição [E3]
```
DADO        agente A tenta publicar no workspace de B
QUANDO      o gate de permissão roda
ENTÃO       rejeição "WORKSPACE_WRITE_FORBIDDEN"
VERIFICAÇÃO error_code == "WORKSPACE_WRITE_FORBIDDEN"; cross_workspace_write == false
```

### Cenário-CBP-T03 — Update append-only preserva a versão anterior
```
DADO        objeto O v1 atualizado para v2
QUANDO      a atualização roda
ENTÃO       O v1 SUPERSEDED e preservado; O v2 ACTIVE; nada deletado
VERIFICAÇÃO v1.state == "SUPERSEDED"; v1_deleted == false; v2.supersedes == "O@v1"
```

### Cenário-CBP-T04 — Conflito de versão otimista
```
DADO        O na versão 3; publicação com expected_version == 2
QUANDO      a escrita roda
ENTÃO       rejeição "VERSION_CONFLICT"; O permanece v3
VERIFICAÇÃO error_code == "VERSION_CONFLICT"; object_corrupted == false
```

### Cenário-CBP-T05 — Idempotência (retry não duplica)
```
DADO        publicação P com idempotency_key K processada 2x
QUANDO      o segundo processamento roda
ENTÃO       nenhum objeto/versão duplicado
VERIFICAÇÃO duplicate_created == false; result_identical == true
```

### Cenário-CBP-T06 — Ordenação determinística / replay
```
DADO        duas publicações concorrentes no mesmo workspace
QUANDO      ambas admitidas e o replay roda
ENTÃO       ordem total determinística; replay reproduz o mesmo estado
VERIFICAÇÃO total_order_assigned == true; replay_deterministic == true
```

### Cenário-CBP-T07 — Estado de hipótese fora do CHM-001 → rejeição [ACH-002]
```
DADO        tentativa de publicar hipótese com estado "VALIDATED" (ciclo descontinuado RULE-BB-003)
QUANDO      o gate de estado roda
ENTÃO       rejeição "HYPOTHESIS_STATE_MUST_BE_CHM001"
VERIFICAÇÃO error_code == "HYPOTHESIS_STATE_MUST_BE_CHM001"; blackboard_defines_hypothesis_state == false
```

### Cenário-CBP-T08 — Invalidação não-destrutiva (objeto não-hipótese; M-001 aberta)
```
DADO        uma Evidência no Blackboard é invalidada
QUANDO      a transição roda
ENTÃO       estado terminal append-only; histórico preservado; enum = M-001 (não fixado)
VERIFICAÇÃO destructive_delete == false; history_preserved == true; m001_states_fixed == false
```

### Cenário-CBP-T09 — Reconstrução por replay (storage físico por referência)
```
DADO        histórico append-only de um workspace
QUANDO      o replay até o instante T roda
ENTÃO       estado reconstruído == estado real em T; storage físico não fixado
VERIFICAÇÃO reconstructed_state == state_at_T; physical_storage_fixed == false
```

### Cenário-CBP-T10 — Atualização sem expected_version → rejeição (criação continua permitida) [ACH-004]
```
DADO        objeto O já existente (v3); publicação de ATUALIZAÇÃO submetida sem expected_version
QUANDO      a escrita roda
ENTÃO       rejeição "EXPECTED_VERSION_REQUIRED"; O permanece v3; atualização não aplicada
            (criação de objeto novo sem expected_version permanece permitida — versão inicial)
VERIFICAÇÃO error_code == "EXPECTED_VERSION_REQUIRED"; update_applied == false; create_without_version_allowed == true
```

---

## D8 — Rigor adversarial extra [casos de negação — foco: concorrência, duplicidade, versionamento — CRITICAL]

Princípio transversal: **fail-closed** — em qualquer ambiguidade sobre permissão de escrita, contrato/proveniência, versão esperada, duplicidade ou append-only, o Blackboard **não publica / não deleta / não corrompe**, e retorna código específico.

### ADV-CBP-01 — Escrita cross-workspace (viola RULE-BB-002) (consolida CBP-002/T02)
**DADO:** agente tenta publicar em workspace alheio
**QUANDO:** o gate de permissão roda
**ENTÃO:** rejeitar `WORKSPACE_WRITE_FORBIDDEN`; nada publicado
**PORQUE:** escrita só no próprio workspace (RULE-BB-002); cross-workspace é irreversível (fail-closed, ENF-04)
**VERIFICAÇÃO:** error_code == "WORKSPACE_WRITE_FORBIDDEN"; cross_workspace_write == false

### ADV-CBP-02 — Deleção destrutiva de objeto (viola RULE-BB-004/INV-07) (consolida CBP-003)
**DADO:** tentativa de deletar fisicamente um objeto/versão
**QUANDO:** a operação de escrita roda
**ENTÃO:** rejeitar `DESTRUCTIVE_DELETE_FORBIDDEN`; aplicar supersessão (append-only)
**PORQUE:** objetos são SUPERSEDED, nunca deletados (RULE-BB-004; INV-07)
**VERIFICAÇÃO:** destructive_delete == false; history_preserved == true

### ADV-CBP-03 — Escrita concorrente sobrescreve sem checar versão (viola CBP-004)
**DADO:** duas escritas concorrentes no mesmo objeto, uma com expected_version obsoleta
**QUANDO:** a segunda escrita roda
**ENTÃO:** rejeitar `VERSION_CONFLICT`; não aplicar last-write-wins cego; estado íntegro
**PORQUE:** versionamento otimista impede sobrescrita cega (SRC-CONC-01); integridade do estado concorrente
**VERIFICAÇÃO:** lost_update == false; object_corrupted == false

### ADV-CBP-04 — Retry cria duplicata (viola CBP-005)
**DADO:** a mesma publicação reentregue após falha de rede (mesma idempotency_key)
**QUANDO:** o reprocessamento roda
**ENTÃO:** no-op idempotente; rejeitar criação de duplicata (`DUPLICATE_SUPPRESSED`)
**PORQUE:** idempotência garante exatamente-uma-vez (SRC-CONC-01); duplicata corrompe o quadro e a contagem
**VERIFICAÇÃO:** duplicate_created == false

### ADV-CBP-05 — Publicação fora de ordem produz estado ambíguo (viola CBP-006)
**DADO:** publicações entregues fora de ordem ao workspace
**QUANDO:** são admitidas
**ENTÃO:** impor ordem total determinística; rejeitar estado ambíguo (`NONDETERMINISTIC_ORDER_FORBIDDEN`)
**PORQUE:** reconstrução histórica exige ordem determinística (P13)
**VERIFICAÇÃO:** total_order_assigned == true; replay_deterministic == true

### ADV-CBP-06 — Objeto sem proveniência publicado (viola CBP-001/007/BL-029)
**DADO:** objeto submetido sem computed_by (ou sem gate_record quando resulta de gate)
**QUANDO:** a publicação roda
**ENTÃO:** rejeitar `PROVENANCE_REQUIRED`; nada publicado
**PORQUE:** reconstrução D9 exige proveniência (P13/RULE-010; BL-029)
**VERIFICAÇÃO:** error_code == "PROVENANCE_REQUIRED"

### ADV-CBP-07 — Blackboard define estado próprio de hipótese (viola CC-02/RULE-BB-003 superseded) [ACH-002]
**DADO:** tentativa de aplicar o ciclo PROPOSED/VALIDATED (RULE-BB-003) a uma hipótese
**QUANDO:** o gate de estado roda
**ENTÃO:** rejeitar `HYPOTHESIS_STATE_MUST_BE_CHM001`; usar estados do CHM-001
**PORQUE:** RULE-BB-003 SUPERSEDED por Q-006; o Blackboard não redefine CHM-001 (CC-02)
**VERIFICAÇÃO:** blackboard_defines_hypothesis_state == false

### ADV-CBP-08 — Fechar M-001 (enum de objetos não-hipótese) nesta Spec (viola CONS-01)
**DADO:** tentativa de fixar, neste Plan, o enum definitivo de estados de objetos não-hipótese
**QUANDO:** RULE-CBP-009/D5 é redigido
**ENTÃO:** rejeitar `OPEN_DECISION_CANNOT_BE_CLOSED`; só a mecânica append-only+supersessão é proposta
**PORQUE:** M-001 ABERTA — decisão de Andraus na homologação do Plan (CONS-01)
**VERIFICAÇÃO:** m001_states_fixed == false

### ADV-CBP-09 — Absorver Event Bus / KG / estado por agente (viola fronteiras SPEC-005/006/009)
**DADO:** tentativa de a SPEC-004 transportar eventos, virar memória permanente, ou fixar estado por agente
**QUANDO:** o escopo é definido
**ENTÃO:** rejeitar `OUT_OF_SCOPE_NEIGHBOR_SPEC`; transporte=SPEC-005, KG=SPEC-006/H-001, estado-agente=SPEC-009/G-001
**PORQUE:** "Blackboard guarda estado; Event Bus transporta mudanças"; KG é memória permanente; H-001/G-001 ABERTAS
**VERIFICAÇÃO:** event_transport_absorbed == false; kg_absorbed == false; per_agent_state_fixed == false

### ADV-CBP-10 — LLM como gate de escrita (viola ENF-03)
**DADO:** proposta de o componente semântico/LLM "aprovar" a permissão de escrita ou o append-only
**QUANDO:** o gate E3 é processado
**ENTÃO:** rejeitar `LLM_IS_NOT_GATE`; o veredito do gate é determinístico; LLM apenas detector
**PORQUE:** o LLM nunca é seu próprio gate (ENF-03)
**VERIFICAÇÃO:** gate_decided_by == "deterministic"; llm_as_gate == false

### ADV-CBP-11 — Atualização sem expected_version tratada como escrita cega (viola CBP-004) [ACH-004]
**DADO:** atualização de objeto já existente submetida sem expected_version
**QUANDO:** a escrita roda
**ENTÃO:** rejeitar `EXPECTED_VERSION_REQUIRED`; não aplicar atualização cega (sem checagem de versão); estado íntegro
**PORQUE:** atualização sem versão esperada = escrita cega sem controle de concorrência → fail-closed (SRC-CONC-01; ENF-04); a CRIAÇÃO (versão inicial) não requer expected_version e permanece permitida
**VERIFICAÇÃO:** blind_update == false; update_applied == false; object_corrupted == false

> **Cobertura:** 11 cenários adversariais (mínimo CRITICAL = ≥1; foco homologado em concorrência/duplicidade/versionamento — DHR-SPEC004-001 §1). Cobrem casos de negação das BASpecs com efeito e das fronteiras abertas (M-001, H-001, G-001, SPEC-005/006/009). Mapeiam para EC-CBP-001..006 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada publicação DEVE ser reconstruível (P13/RULE-010): objeto + versão + proveniência (computed_by/gate_record/derived_from), ordem (seq por workspace), supersessão (supersedes/superseded_by), estado operacional, resultado do gate de escrita (accept/deny + motivo). A **reconstrução expandida de linhagem** (Cognitive Trace Reconstruction) e o **storage físico** pertencem ao **Knowledge Graph (SPEC-006 / H-001 ABERTA)** e ao **estado por agente (SPEC-009 / G-001 ABERTA)** — aqui ficam **por referência** (coerente com alvo D0–D7; CEM-001 Cap.5). [FONTE: CONSTITUTION P13; RULE-010; CEM-001 Cap.5; H-001/G-001 ABERTAS]

---

## Contrato de objeto do Blackboard — esqueleto [PROPOSTA]

> Produto central da SPEC-004. Projeta o Lineage do CEM-001 e os estados do CHM-001 **sem redefini-los** (CC-02). **Estrutura/mecânica; enum de estados não-hipótese = M-001 (ABERTA).**

| Camada | Conteúdo | Fronteira |
|---|---|---|
| Identidade | `object_id`, `version`, `previous_version_id`, `creation_timestamp`, `state` (operacional: ACCEPTED/PUBLISHED/SUPERSEDED/EXPIRED/ARCHIVED/REJECTED) | Append-only (INV-07) |
| Classificação | `object_type` (hypothesis \| evidence \| mission \| observation \| conviction \| ...), `workspace`, `namespace` | hipótese usa estado CHM-001; não-hipótese = M-001 (ABERTA) |
| Proveniência | `computed_by`, `derived_from[]`, `gate_record` (quando resulta de gate) | BL-029; projeta Lineage CEM-001 (não redefine) |
| Concorrência | `expected_version`, `idempotency_key`, `seq` (ordem no workspace) | versionamento otimista (CBP-004); `expected_version` obrigatório em ATUALIZAÇÃO (ausente ⇒ EXPECTED_VERSION_REQUIRED), dispensado em CRIAÇÃO (versão inicial) |
| Supersessão | `supersedes`, `superseded_by` | nunca deletado (CBP-003) |
| Permissão | `owner_workspace` (escrita só pelo dono; leitura livre) | RULE-BB-002 |
| Rastreabilidade | `reconstruction_ref` (replay até o estado) | P13/RULE-010; storage físico = SPEC-006/009 |

---

## I/O Schemas (lógicos — referência; não redefinem CHM-001/CEM-001/CCM-001)

### Objeto publicado no Blackboard
```json
{
  "object_id": "BB-2026-10-03-001",
  "version": 2,
  "previous_version_id": "BB-2026-10-03-001@v1",
  "creation_timestamp": "2026-10-03T12:00:00Z",
  "state": "PUBLISHED",
  "object_type": "evidence | hypothesis | mission | observation | conviction",
  "workspace": "institutional_agent",
  "owner_workspace": "institutional_agent",
  "provenance": {
    "computed_by": "institutional_agent/activity-123",
    "derived_from": ["BB-...@v1"],
    "gate_record": "{ result, thresholds_used } | null (quando não resulta de gate)"
  },
  "expected_version": 1,
  "idempotency_key": "pub-abc-123",
  "seq": 42,
  "supersedes": "BB-2026-10-03-001@v1",
  "superseded_by": null,
  "hypothesis_state_ref": "CHM-001 enum (quando object_type == hypothesis; NÃO redefinido)",
  "non_hypothesis_state_ref": "M-001 (ABERTA — enum não fixado neste Plan)",
  "reconstruction_ref": "replay(workspace, seq)"
}
```
> O objeto **armazena/versiona** hipótese (estado = CHM-001, não redefinido — RULE-BB-003 SUPERSEDED por Q-006), Evidência (CEM-001, idioma canônico INV-10) e Convicção (CCM-001) **sem redefini-los** (CC-02). O enum de estados não-hipótese é **M-001 (ABERTA)**. Nenhum campo computa convicção nem deriva de custo (INV-04 — fora do escopo deste componente).

---

## Enforcement Contracts

### EC-CBP-001 — Publicação de objeto (contrato + proveniência; append-only)
```
CAPABILITY   : Admitir e publicar um objeto no workspace próprio, versionado e com proveniência
EFFECT       : Publicação (commit) de objeto/versão no estado compartilhado do Blackboard
PRECOND      : (contrato mínimo presente) AND (proveniência computed_by presente) AND (append-only: nova versão)
POSTCOND     : objeto PUBLISHED; versão anterior SUPERSEDED; histórico preservado (INV-07)
POLICY       : RULE-CBP-001/003/007; RULE-BB-002/004; BL-029; INV-07/INV-10
LEVEL        : E2 (Operacional — estado compartilhado alterado, reversível por supersessão)
FAILURE-MODE : Fail-closed — contrato/proveniência ausente ⇒ rejeitar; nada publicado; log
EVIDENCE     : log de publicação (versão, proveniência, seq); objeto recuperável por replay
```

### EC-CBP-002 — Gate de escrita (permissão de workspace + append-only) [E3]
```
CAPABILITY   : Autorizar ou negar a escrita (publicação/atualização/deleção) no Blackboard
EFFECT       : Commit em estado compartilhado (publicação) ou negação (DENY)
PRECOND      : (workspace alvo == workspace do agente — RULE-BB-002) AND (nenhuma deleção destrutiva —
               RULE-BB-004) AND (gate determinístico; LLM nunca é o gate — ENF-03)
POSTCOND     : escrita só no próprio workspace; deleção destrutiva impossível; append-only garantido
POLICY       : RULE-CBP-002/003; RULE-BB-002/004; INV-07; ENF-03/04
LEVEL        : E3 (Crítico — cross-workspace e deleção destrutiva são irreversíveis; corrompem a cadeia)
FAILURE-MODE : Fail-closed — ambiguidade/violação ⇒ negar; nada publicado/deletado; log
EVIDENCE     : gate_record (accept/deny + motivo) + ENF-07: amostragem de falso-DENY (publicação válida negada
             por engano; limiar amostral = gap aberto — BL-002)
```

### EC-CBP-003 — Concorrência (versionamento otimista)
```
CAPABILITY   : Aceitar escrita só se a versão esperada coincide com a corrente
EFFECT       : Publicação de nova versão ou rejeição por conflito de concorrência
PRECOND      : (expected_version == current_version)
POSTCOND     : nova versão publicada; sob divergência, objeto íntegro (sem escrita parcial/lost update)
POLICY       : RULE-CBP-004; SRC-CONC-01 [EXTERNO]
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — versão divergente ⇒ VERSION_CONFLICT; nada escrito
EVIDENCE     : log de conflito; versão corrente preservada
```

### EC-CBP-004 — Idempotência (retry seguro)
```
CAPABILITY   : Processar cada publicação exatamente uma vez, mesmo sob retry
EFFECT       : Publicação única ou no-op idempotente
PRECOND      : (idempotency_key fornecida)
POSTCOND     : nenhum objeto/versão duplicado; resultado idêntico ao primeiro processamento
POLICY       : RULE-CBP-005; SRC-CONC-01 [EXTERNO]
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — chave repetida ⇒ no-op; duplicata suprimida
EVIDENCE     : registro de idempotency_keys processadas; ausência de duplicata
```

### EC-CBP-005 — Supersessão / expiração / invalidação não-destrutiva
```
CAPABILITY   : Transitar objeto para estado terminal sem deleção
EFFECT       : Objeto marcado SUPERSEDED/EXPIRED/ARCHIVED; histórico preservado
PRECOND      : (update ⇒ nova versão) OR (expiração/invalidação ⇒ estado terminal)
POSTCOND     : nada deletado (INV-07); objeto recuperável para auditoria; enum não-hipótese = M-001 (ABERTA)
POLICY       : RULE-CBP-003/009/010; RULE-BB-004; INV-07; M-001
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — tentativa de deleção ⇒ rejeitar; aplicar supersessão
EVIDENCE     : log de transição terminal; histórico íntegro
```

### EC-CBP-006 — Reconstrução histórica (replay)
```
CAPABILITY   : Reconstruir o estado do Blackboard por replay das versões append-only
EFFECT       : Produção de uma visão de estado num ponto do tempo (leitura; sem efeito de escrita)
PRECOND      : (histórico append-only ordenado por (workspace, seq) disponível)
POSTCOND     : estado reconstruído fiel (P13); storage físico não fixado (H-001/G-001)
POLICY       : RULE-CBP-006/011; RULE-010; CONSTITUTION P13; SRC-ES-01 [EXTERNO]
LEVEL        : E1 (Contratual — leitura/reconstrução; evidência observável)
FAILURE-MODE : Fail-closed — histórico incompleto/ambíguo ⇒ reportar lacuna, não fabricar estado
EVIDENCE     : trilha de replay; estado reconstruído verificável contra o histórico
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
Serviço lógico de **memória de trabalho compartilhada** (o Blackboard Cognitivo). Combina gates constitutivos determinísticos (Classe C: contrato/permissão/append-only/proveniência/estado de hipótese) e mecânica determinística (Classe D: versionamento otimista, idempotência, ordenação, expiração, replay, observabilidade). **Não executa, não transporta eventos, não decide, não computa convicção** — guarda e versiona estado de análise para consumo via leitura (RULE-BB-001/002). [FONTE: RULES.md RULE-BB-001..005; atomic-spec §9/§10.6; research.md §3]

### Roteamento de modelo (CEE-001 §5)
Gates constitutivos/determinísticos (C/D) **não requerem LLM** — são código. Um eventual juízo de "objeto bem-formado para publicação" (Classe H, se adotado em BUILD) usaria apoio semântico (Tipo II–III → Sonnet) **apenas como detector**, nunca como gate (ENF-03). Roteamento definitivo por Engineering Card (BUILD adiado). [FONTE: CEE-001 §5; ENF-03]

### Dependências técnicas
RULES.md v1.1 (RULE-BB-001..005) · CHM-001 (BASELINE) · CEM-001 (BASELINE) · CCM-001 (BASELINE, DHR-SPEC003-001) · SPEC-001 v1.1 (BASELINE — Hypothesis Registry → storage) · SPEC-019/020/021 v1.0 (BASELINE) · atomic-spec v1.5 · INV-05/06/07/09/10 · ENF-01..08. Referências externas [EXTERNO], não-baseline: research.md §2 (SRC-BB-01, SRC-PROV-01/W3C PROV, SRC-ES-01, SRC-CONC-01, SRC-MEM-01) e §4-bis (REPO-yjs/automerge/mem0).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Fechar M-001 por engano (pressão de "definir estados") | RULE-CBP-009 [PROPOSTA]; ADV-CBP-08; D5 enum = M-001 ABERTA; CONS-01 |
| Redefinir canônico (CHM/CEM/CCM) ao "guardar" | CC-02 foco; RULE-CBP-008; ADV-CBP-07; só armazenar/versionar |
| Absorver vizinhos (Event Bus/KG/estado-agente) | Non-goals §D1; ADV-CBP-09; fronteiras explícitas |
| Over-engineering de concorrência (CRDT desnecessário) | CRDT ADIADO (research.md §3.3); optimistic concurrency sob RULE-BB-002; INDETERMINADO quanto à necessidade |
| Deleção destrutiva / lost update / duplicata | RULE-CBP-003/004/005; ADV-CBP-02/03/04; EC-CBP-002/003/004 |
| Estado de hipótese próprio (RULE-BB-003 descontinuada) | RULE-CBP-008; ADV-CBP-07; CHM-001 |
| LLM como gate de escrita | ENF-03; ADV-CBP-10; EC-CBP-002 (detector≠gate) |
| ACH-001 (fonte arXiv não verificável sustentando proposta) | SRC-MEM-01 arXiv rebaixada a não-load-bearing (Notas de honestidade); nenhuma proposta importada dela |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz o schema lógico do objeto do Blackboard; nenhum schema canônico do CHM-001/CEM-001/CCM-001 alterado.
- **RAG:** nenhum; o Blackboard não escreve no KG/RAG (memória permanente = SPEC-006).
- **Skills:** nenhuma Skill afetada; INV-06 preservado (Skill produz Observação; o Blackboard só a armazena).
- **Testes:** adiciona `checks.md` (verificação de spec); mecânica de concorrência/replay fica para BUILD.
- **Modelos dependentes:** CHM-001/CEM-001/CCM-001/SPEC-001 não alterados (construção SOBRE); RULE-BB-001..005 operacionalizadas, não alteradas.
- **Compatibilidade:** **Minor** — adiciona a camada de protocolo sobre regras/canônicos existentes, sem invalidar comportamento vigente; nenhuma RULE existente redefinida.

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07) e a Classe por BASpec (CC-11). A decisão de M-001 (enum de estados não-hipótese) é condição da homologação do Plan por Andraus.

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — pergunta adversarial por BASpec com efeito (cobertura TOTAL — CRITICAL, 12 BASpecs):**

- **CBP-001 (contrato, C):** se errada → objeto sem proveniência publicado → observável por `provenance` vazia no quadro; verificável por consumidor independente. Negação: ADV-CBP-06. QUANDO-sim-mas-ENTÃO-não: objeto com contrato mas workspace alheio → ainda rejeitar (CBP-002).
- **CBP-002 (permissão, C/E3):** se errada → escrita cross-workspace → observável por objeto no workspace de B escrito por A; verificável. Negação: ADV-CBP-01. QUANDO-sim-mas-ENTÃO-não: leitura de workspace alheio é permitida (não negar).
- **CBP-003 (append-only, C):** se errada → versão anterior deletada → observável por histórico com buraco; verificável. Negação: ADV-CBP-02.
- **CBP-004 (versão otimista, D):** se errada → lost update por sobrescrita cega → observável por `object_corrupted`/perda de versão; verificável. Negação: ADV-CBP-03; atualização sem expected_version → ADV-CBP-11/T10 (ACH-004). QUANDO-sim-mas-ENTÃO-não: publicação sem expected_version numa CRIAÇÃO (objeto novo) NÃO é rejeitada (versão inicial permitida) — só a ATUALIZAÇÃO exige expected_version.
- **CBP-005 (idempotência, D):** se errada → duplicata por retry → observável por `duplicate_created=true`; verificável. Negação: ADV-CBP-04.
- **CBP-006 (ordenação, D):** se errada → replay não determinístico → observável por estados divergentes em replays; verificável. Negação: ADV-CBP-05.
- **CBP-007 (proveniência, C):** se errada → objeto não reconstruível → observável por `gate_record` ausente onde resultou de gate; verificável. Negação: ADV-CBP-06.
- **CBP-008 (estado de hipótese CHM-001, C):** se errada → Blackboard inventa estado de hipótese → observável por estado fora do enum CHM-001; verificável. Negação: ADV-CBP-07. (ACH-002 corrigido: RULE-BB-003 SUPERSEDED.)
- **CBP-009 (estados não-hipótese, C — M-001 ABERTA):** se errada → M-001 fechada por engano ou deleção destrutiva → observável por `m001_states_fixed=true` ou deleção; verificável. Negação: ADV-CBP-08. QUANDO-sim-mas-ENTÃO-não: mecânica (append-only) proposta, enum não fixado.
- **CBP-010 (expiração não-destrutiva, D):** se errada → expiração deleta → observável por objeto expirado ausente do histórico; verificável. Negação: cobertura em ADV-CBP-02.
- **CBP-011 (replay, D):** se errada → reconstrução infiel ou fixa storage físico → observável por `reconstructed_state≠state_at_T` ou `physical_storage_fixed=true`; verificável. Negação: ADV-CBP-09 (não absorver SPEC-006/009).
- **CBP-012 (observabilidade falso-DENY, D):** se errada → gate bloqueia escrita legítima em silêncio → observável por ausência de amostragem de DENY; verificável. Negação: cobertura em EC-CBP-002 (ENF-07).

Todas as 12 BASpecs com efeito têm ENTÃO verificável por observador independente e caso de negação em D8. Nenhuma restou como [DECISÃO NECESSÁRIA] por falta de verificabilidade (as decisões abertas M-001/H-001/G-001 são fronteiras explícitas, não falhas de verificabilidade).

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista RULE-BB-001..005 (RULE-BB-003 superseded), CHM-001, CEM-001, CCM-001, SPEC-001 v1.1, SPEC-019/020/021 v1.0, atomic-spec v1.5, ENF-01..08, INV-05/06/07/09/10, RULE-010 (ID+versão — RULE-HD-04). Evidência de satisfação por obrigação herdada:
- RULE-BB-001 (comunicação só via Blackboard) → premissa do protocolo D6.
- RULE-BB-002 (escrita só no próprio workspace; leitura livre) → CBP-002/EC-CBP-002.
- RULE-BB-003 (SUPERSEDED por Q-006 — sem estado de hipótese próprio) → CBP-008/ADV-CBP-07 (corrige ACH-002).
- RULE-BB-004 (append-only; SUPERSEDED nunca deletado) → CBP-003/CBP-009/CBP-010/EC-CBP-005.
- RULE-BB-005 (Orchestrator só coordena) → fronteira SPEC-008 (não absorvida) / ADV-CBP-09.
- INV-07 (versionamento monotônico) → CBP-003/CBP-010.
- CHM-001/CEM-001/CCM-001 (não redefinir) → CC-02; só armazenar/versionar (CBP-008; contrato de objeto).
- RULE-010/P13 (reconstrução) → CBP-007/CBP-011/D9.
- ENF-03 (detector≠gate) → ADV-CBP-10; gates C/D determinísticos.
- ENF-04/07 (fail-closed; falso-DENY) → EC-CBP-002.
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (nenhum MODIFIED — RULE-BB-003 já estava superseded antes desta Spec). **Eixo VERTICAL (RULE-HV) declarado não aplicável** (herança sobre regras/canônicos vizinhos, não decomposição pai→filha de macro-spec).

**Bloco C — epistêmico (RULE-EPI/CAU/PRB):** nenhuma afirmação causal forte sem mecanismo; nenhuma hipótese tratada como fato (SRC-*/REPO-* = [EXTERNO]/DADO; nenhum método externo importado como baseline — CRDT adiado, mem0 adaptado); **INDETERMINADO** usado sobre a necessidade de CRDT/merge multi-escritor (não decidida); **M-001 ABERTA** declarada, não forçada a PASS/FAIL; **nenhuma probabilidade/precisão numérica** declarada (o Blackboard não computa convicção; nenhum limiar). **ACH-001:** a URL arXiv 2606.* de SRC-MEM-01 é declarada **não-load-bearing** (coerente com o aviso de método, RULE-MET-01) — a convergência não depende dela.

**Bloco D — reforço de escopo:** a Spec **guarda/versiona estado de análise** (publicação/supersessão/reconstrução), **não executa** ordem, **não transporta** eventos, **não decide** nem **computa convicção** — INV-05/RULE-DEC-01 reconfirmados (§7). Nenhuma BASpec cruza a fronteira SOT→execução downstream nem invade Event Bus (SPEC-005)/KG (SPEC-006)/estado-agente (SPEC-009)/Manager (SPEC-008). Dependências de decisão de Andraus (homologação; efetivação de RULE-CBP/contrato; **M-001**) marcadas [PROPOSTA]/[DECISÃO NECESSÁRIA], não fechadas; J-001/N-001/H-001/G-001/WF-D03 abertas, não tocadas.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| RULE-BB-001..005 (vigentes; RULE-BB-003 SUPERSEDED por Q-006); CHM-001; CEM-001; CCM-001; SPEC-001 v1.1; SPEC-019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5; RULES v1.5; INV-*; ENF-*; RULE-010 | [FONTE] | FATO NORMATIVO |
| RULE-CBP-001..012; contrato de objeto do Blackboard; BASpec-CBP-001..012; EC-CBP-001..006 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Fontes SRC-BB-01/PROV-01/ES-01/CONC-01/MEM-01; REPO-yjs/automerge/mem0 | [EXTERNO] | Referência de método — DADO, nunca baseline (research.md §2/§4-bis) |
| URL arXiv 2606.24535 de SRC-MEM-01 | [EXTERNO] | **Não-load-bearing** (família de IDs implausíveis; aviso de método) — ACH-001 |
| Estados do Blackboard para objetos NÃO-hipótese (enum definitivo) | [DECISÃO NECESSÁRIA] | **M-001 — EM ABERTO — não fechar** (decisão de Andraus na homologação do Plan) |
| Mecanismo físico de storage (grafo real vs. memória) | [DECISÃO NECESSÁRIA] | **H-001 — EM ABERTO (SPEC-006)** |
| Estado persistente por agente | [DECISÃO NECESSÁRIA] | **G-001 — EM ABERTO (SPEC-009)** |
| Fórmula/pesos/limiares definitivos do Conviction Vector; pesos por ativo | [DECISÃO NECESSÁRIA] | **J-001 / N-001 — EM ABERTO (SPEC-003/backtest)** — não tocadas |
| Necessidade de CRDT (multi-escritor no mesmo workspace) | [DECISÃO NECESSÁRIA] | **INDETERMINADO** — adiado (research.md §3.3) |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-004 confirmada como próximo autorizado (§5/§25/§32); FASE 2, após FASE 1 e FASE GOV.
[x] atomic-spec.md lido: método v1.5 confirmado (CC-11/CC-12; RULE-MECH-01; RULE-ECC-04/06; RULE-MM; §15 Dossiê).
[x] Nenhum invariante congelado violado (INV-01..10). INV-05/06/07/09/10 reforçados.
[x] Constitution Check CC-01..CC-12 preenchido (N/A justificados CC-06/07/12; CC-02/CC-08/CC-10/CC-11 INCIDEM e aplicados).
[x] Disciplinas N8–N17: RULE-EPI (M-001 ABERTA; INDETERMINADO sobre CRDT), RULE-MET-01 (não-fabricação; ACH-001), RULE-UNC (incerteza localizada), RULE-SEM-01 (acepções "estado do objeto" vs "estado da hipótese"), RULE-DEC-01 (guarda≠executa).
[x] Referências externas [EXTERNO] classificadas (research.md §2/§4-bis); rótulos externos (CRDT/mem0/W3C PROV) NÃO adotados como baseline; verbatim capturado (RULE-ECC-04, sources/); repositórios sob régua Equilibrada (RULE-ECC-06, research.md §4-bis).
[x] RULE-ECC-05 (Multi-Lente): determinação de NÃO-incidência (infra; não toca comportamento de trading) — confirmada na abertura (DHR-SPEC004-001).
[x] Spec sem implementação (BUILD adiado); Plan derivado; Tasks adiadas (spec-first).
[x] Critérios em EARS (12 — 1..11 + 4-bis); BASpecs completas (CBP-001..012) com Classe declarada (CC-11); RULEs citadas existentes vs propostas (RULE-CBP [PROPOSTA]) etiquetadas.
[x] Profundidade D0–D7 + rigor adversarial extra (D8) nos comportamentos de risco (concorrência/duplicidade/versionamento) atingida (D5 ciclo operacional; D6 protocolo; D7 x10; D8 x11; D9 por referência).
[x] Enforcement Contract em todo ato com efeito (EC-CBP-001..006); piso E2; E3 no gate de escrita (cross-workspace/deleção irreversíveis; fail-closed); ENF-07 amostral declarado no E3 (BL-002).
[x] Status epistemológico aplicado (FATO NORMATIVO / PROPOSTA / EXTERNO / DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: M-001, H-001, G-001, J-001, N-001, WF-D03 permanecem abertas (só mecânica/estrutura); nenhuma decisão aberta usada como invariante fechado.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos/achados registrados (ACH-001 arXiv; ACH-002 RULE-BB-003 superseded) — tratados, não silenciados.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE fabricada como vigente; sem baseline informal.
[x] 4Es na ordem; Conformidade > Eficácia (INV-07 e ENF-03 prevalecem). Latência N/A (camada spec-time).
[x] Dependências a montante homologadas (RULE-BB-*/CHM-001/CEM-001/CCM-001/SPEC-001/019/020/021/atomic-spec v1.5); não downstream de bloqueador aberto (M-001 é dona desta Spec, proposta não fechada).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); Bloco A cobre TODAS as 12 BASpecs com efeito — obrigatório CRITICAL.
[x] CC-11/§10.6: Classe por BASpec com efeito, com critério 4Es; H/P com bounded loop; H/C com gate de saída.
[x] Abertura (RULE-ECC-01/02/04/06): Dossiê presente e HOMOLOGADO (DHR-SPEC004-001); verbatim em sources/; repositórios em research.md §4-bis; escopo/quantidade/número homologados (1 Spec).
[x] Passo 11-bis: BL-029 (dona=SPEC-004) tratado; BL-002 tratado (observabilidade); BL-003 fronteira; BL-012/BL-017 independentes (Andraus).
[ ] Gate determinístico (validate_spec_sot.py) e build_map.py --check: reportado ao caller (execução no ambiente pai — Especificador sem Bash).
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] / abertas nesta Spec (não fechadas — CONS-01):
- **M-001** — estados do Blackboard para objetos NÃO-hipótese (Evidência/Missão/Observação/Convicção): a SPEC-004 é a **dona** e **propõe** append-only + supersessão projetando o CEM-001 (RULE-CBP-009/D5), mas **não fecha** o enum — decisão de Andraus na homologação do Plan.
- **H-001** — Knowledge Graph (grafo real vs. memória): fronteira (SPEC-006); o Blackboard referencia o storage físico, não o fecha.
- **G-001** — estado persistente por agente: fronteira (SPEC-009); não tocado.
- **J-001 / N-001** — fórmula/pesos/limiares definitivos do Conviction Vector / pesos por ativo: o Blackboard só armazena/versiona o objeto, não computa — não tocadas.
- **WF-D03** (residual) — não tocada (o Blackboard não computa convicção).
- **CRDT (necessidade)** — INDETERMINADO; adiado (RULE-BB-002 torna optimistic concurrency suficiente hoje).

Carregado para o Revisor:
- Achados do parecer de abertura CORRIGIDOS: **ACH-001** (SRC-MEM-01 arXiv 2606.* rebaixada a não-load-bearing — Notas de honestidade / Etiquetagem) e **ACH-002** (RULE-BB-003 **SUPERSEDED por Q-006**, citação `governance/RULES.md` l.316–321; CBP-008/ADV-CBP-07 — o Blackboard não define estado de hipótese).
- M-001 apresentada como [PROPOSTA] (append-only + supersessão projetando o CEM-001), **não** fechada.
- Fronteiras SPEC-005/006/008/009 declaradas; CHM-001/CEM-001/CCM-001 não redefinidos (CC-02).
