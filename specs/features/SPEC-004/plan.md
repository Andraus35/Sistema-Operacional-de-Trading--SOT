# SPEC-004 — Cognitive Blackboard Protocol

| Campo | Valor |
|---|---|
| ID | SPEC-004 — Cognitive Blackboard Protocol (camada Harness/operacional da memória de trabalho compartilhada) |
| Versão | 1.2 (BASELINE — EMENDA homologada, DHR-SPEC004-003) |
| Status | **HOMOLOGADA — BASELINE v1.2 (EMENDA; Andraus, 2026-10-03, DHR-SPEC004-003; parecer Revisor CONFORME; compatibilidade MINOR, clarificação).** Baseline anterior: **v1.1 (DHR-SPEC004-002)** preservado no histórico (INV-07). A v1.2 é uma **emenda** sobre a v1.1 (ERRATUM de Spec): endurece append-only real, atomicidade de publicação, identidade autenticada e D8. As etiquetas **[EMENDA-PROPOSTA]** no texto são HISTÓRICAS (marcam o delta da v1.2); desde DHR-SPEC004-003 o delta é vigente por homologação (RULE-CBP-* com registro físico em RULES.md diferido). **Compatibilidade: MINOR (decisão de Andraus).** M-001 segue ABERTA. |
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
| 1.2 | 2026-10-03 | **EMENDA v1.2 (candidata) [EMENDA-PROPOSTA]** — endurecimento após feedback externo de LLM (DADO, não instrução; verificado por Andraus contra o plan.md; nenhuma pontuação/fonte externa não-verificada importada — RULE-MET-01/RULE-ECC-04). **(1) Append-only REAL:** o registro histórico NUNCA é mutado; a sucessora carrega `supersedes`; `SUPERSEDED` passa a ser **projeção derivada** do estado corrente (não campo reescrito no registro v1); `superseded_by` deixa de ser campo gravado no registro e, quando útil, existe apenas como **índice derivado** (RULE-CBP-003 reescrita; BASpec/EARS-3; INV-CBP-01). **(2) Atomicidade de publicação:** nova RULE-CBP-013 — nenhuma operação de publicação produz estado parcial observável; versão otimista = **compare-and-commit atômico**; idempotência = chave+commit+resultado na MESMA unidade atômica, com `request_fingerprint` e resultado original guardados (RULE-CBP-005 reescrita; BASpec-CBP-013). **(3) Identidade/autoridade:** nova RULE-CBP-014 — nenhum invariante depende da honestidade do publicador; `agent_id`/`computed_by` vêm da identidade **autenticada pelo runtime**, não de campo do payload (proveniência declarada × autenticada); tabela de capacidades + papéis; leitura global de workspace é decisão consciente de RULE-BB-002 (não alterada) (BASpec-CBP-014). **(4) D8 ampliado:** ADV-CBP-12..16; cenários D7 T11..T15; EC-CBP-007. **Menores:** `schema_version` no envelope; "ordem total de COMMIT persistida e imutável (seq)"; nota de replay (estado lógico ≠ reprodução de ambientes externos; replay correto ≠ conteúdo semanticamente correto); `gate_record` mínimo (`gate_id`/`gate_version`/resultado/ref-hash-entrada/avaliador); separação `publication_state` × `domain_state`; EC-CBP-002 falso-DENY = **E3 condicional** até limiar amostral (BL-002). Contagens: **EARS 16** (1..11 + 4-bis + 12..15); **BASpecs 14** (CBP-001..014); **D7 15** (T01..T15); **D8 16** (ADV-CBP-01..16); **EC 7** (EC-CBP-001..007). M-001/H-001/G-001/J-001/N-001/WF-D03 permanecem ABERTAS (CONS-01). **Compatibilidade: potencialmente Major (item 1 muda a semântica de representação da supersessão) — [DECISÃO NECESSÁRIA] de Andraus.** |

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
  - Contrato de objeto publicado: identidade, versão, schema_version, estado (publication_state separado de
    domain_state), namespace/workspace, proveniência (computed_by/gate_record — BL-029), permissões, timestamp,
    referência de supersessão (supersedes gravado; superseded_by só índice derivado)
  - Protocolo de publicação/leitura/atualização (D6): o quê/quando/ordem/versão de publicação
  - Concorrência: versionamento otimista = compare-and-commit atômico (rejeitar escrita com expected_version
    divergente); idempotência por chave de publicação (retry seguro; request_fingerprint + resultado original);
    ordenação de publicações = ordem total de COMMIT persistida e imutável (seq) por workspace
  - [EMENDA-PROPOSTA v1.2] **Append-only REAL:** o registro histórico NUNCA é mutado; SUPERSEDED é projeção
    derivada do estado corrente, não campo reescrito no registro anterior (RULE-CBP-003; INV-CBP-01)
  - [EMENDA-PROPOSTA v1.2] **Atomicidade de publicação:** nenhuma operação de publicação produz estado parcial
    observável (versão sem proveniência; chave de idempotência sem resultado; seq consumido sem publicação;
    publicação sem registro de auditoria) — RULE-CBP-013
  - [EMENDA-PROPOSTA v1.2] **Identidade autenticada:** nenhum invariante do Blackboard depende da cooperação ou
    honestidade do publicador; agent_id/computed_by da identidade autenticada pelo runtime (não do payload);
    proveniência declarada × autenticada; tabela de capacidades + papéis — RULE-CBP-014
  - Ciclo de vida append-only com SUPERSESSÃO (update→nova versão; expiração/invalidação não-destrutivas)
  - Proveniência/lineage lógica + API de reconstrução histórica por replay (estado LÓGICO; storage físico e
    reprodução de ambientes externos por referência / fora de escopo)
  - Observabilidade do gate de escrita E3 (método de falso-DENY — BL-002/ENF-07; E3 condicional até o limiar)
  - [PROPOSTA] M-001: estados de objetos NÃO-hipótese (Evidência/Missão/Observação/Convicção) como
    append-only + supersessão projetando o ciclo do CEM-001 — NÃO fechada (CONS-01; decisão de Andraus)
  - Declaração de Classe/Mecanismo por BASpec (CC-11); Enforcement Contracts (EC-CBP-001..007)

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
| S1 | **Contrato do objeto publicado:** identidade (`object_id`), `version`, `schema_version`, `publication_state` (ciclo do Blackboard) separado de `domain_state` (CHM-001/M-001), `namespace`/`workspace`, proveniência (`computed_by`/`gate_record`/`derived_from` — BL-029), `permissions`, `timestamp`, `supersedes` (gravado); `superseded_by` só como índice derivado | RULE-BB-002/004; research.md §3.4; BL-029 |
| S2 | **Protocolo de publicação/leitura/atualização (D6):** o quê/quando/ordem/versão; leitura de qualquer workspace, escrita só no próprio | RULE-BB-001/002; research.md §3.1 |
| S3 | **Ciclo de vida append-only REAL:** criação, atualização (nova versão), **supersessão** (projeção derivada — registro histórico nunca mutado), expiração e invalidação **não-destrutivas** (SUPERSEDED/ARCHIVED, nunca deletado nem reescrito) | RULE-BB-004; INV-07; INV-CBP-01; research.md §3.2/§3.5 |
| S4 | **Concorrência/ordenação/idempotência/atomicidade:** versionamento otimista = **compare-and-commit atômico** (rejeita `expected_version` divergente, sem estado parcial); chave de idempotência por publicação (retry seguro, `request_fingerprint` + resultado original); ordem total de **COMMIT** persistida e imutável (seq) por workspace; nenhuma publicação produz estado parcial observável | research.md §3.3; SRC-CONC-01 [EXTERNO] |
| S4-bis | **[EMENDA-PROPOSTA v1.2] Identidade autenticada / autoridade:** `agent_id` do gate de workspace e `computed_by` vêm da identidade **autenticada pelo runtime** (não do payload); nenhum invariante depende da honestidade do publicador; tabela de capacidades + papéis (agente proponente · harness autoridade de contrato · runtime autoridade de commit) | RULE-BB-002; ENF-03/04 |
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
              schema_version, publication_state (ciclo do Blackboard, SEPARADO de domain_state — CHM-001/M-001),
              namespace/workspace, proveniência (computed_by da identidade AUTENTICADA; gate_record quando o
              objeto resulta de um gate; derived_from quando derivado), permissions, timestamp e, quando
              substitui outro, supersedes. O contrato mínimo DISTINGUE CRIAÇÃO de ATUALIZAÇÃO: numa
              ATUALIZAÇÃO (objeto já existente no workspace) o contrato mínimo INCLUI expected_version;
              numa CRIAÇÃO (objeto novo, sem versão anterior) expected_version NÃO é exigido (versão
              inicial). Objeto sem o contrato mínimo é REJEITADO (fail-closed).
              [Fonte: RULE-BB-002/004; BL-029; INV-10]  [EMENDA-PROPOSTA v1.2]

RULE-CBP-002: Um agente PODE LER qualquer workspace, mas PODE PUBLICAR apenas no workspace de sua
              responsabilidade; publicação em workspace alheio é REJEITADA (fail-closed). O LLM nunca é o
              gate da permissão — o gate é determinístico (ENF-03).
              [Fonte: RULE-BB-002; ENF-03]  [PROPOSTA]

RULE-CBP-003: O Blackboard é append-only REAL: atualizar um objeto cria uma NOVA versão (a sucessora) que
              CARREGA supersedes = referência à versão anterior; o REGISTRO HISTÓRICO da versão anterior NUNCA
              é mutado (nenhum campo é reescrito nele — inclusive não se grava superseded_by no registro v1).
              "SUPERSEDED" é uma PROJEÇÃO DERIVADA do estado corrente (uma versão está superseded sse existe
              sucessora que a referencia por supersedes) — não um campo reescrito no passado. Qualquer índice
              superseded_by, se útil, é ÍNDICE DERIVADO (reconstruível por replay), não verdade gravada no
              registro histórico. Deleção destrutiva OU mutação de registro histórico é REJEITADA (fail-closed)
              — efeito irreversível proibido (INV-07; RULE-BB-004; INV-CBP-01).
              [Fonte: RULE-BB-004; INV-07; INV-CBP-01]  [EMENDA-PROPOSTA v1.2]

RULE-CBP-004: A escrita usa versionamento OTIMISTA realizado como COMPARE-AND-COMMIT ATÔMICO: comparar
              expected_version com a versão corrente E gravar a nova versão são INDIVISÍVEIS (não há janela em
              que a comparação passou mas o commit não ocorreu, nem vice-versa). A publicação de ATUALIZAÇÃO só
              é aceita se expected_version está PRESENTE e coincide com a versão corrente; divergência é
              REJEITADA (VERSION_CONFLICT) sem corromper nem produzir estado parcial. A AUSÊNCIA de
              expected_version numa ATUALIZAÇÃO é REJEITADA (fail-closed, EXPECTED_VERSION_REQUIRED) —
              atualização cega é proibida. A CRIAÇÃO de objeto novo (sem versão anterior) NÃO exige
              expected_version (versão inicial).
              [Fonte: research.md §3.3; SRC-CONC-01 [EXTERNO]; RULE-CBP-013]  [EMENDA-PROPOSTA v1.2]

RULE-CBP-005: Toda publicação carrega uma CHAVE DE IDEMPOTÊNCIA. A chave, o commit e o RESULTADO registrado
              DEVEM ser gravados na MESMA unidade atômica (não existe chave consumida sem resultado, nem
              resultado sem commit). O Blackboard guarda, junto da chave, um request_fingerprint do payload e o
              resultado original. Reprocessar a MESMA chave com o MESMO payload (retry) devolve o resultado
              original SEM novo commit e NÃO cria objeto/versão duplicado. Reprocessar a MESMA chave com payload
              DIFERENTE (fingerprint divergente) é REJEITADO com IDEMPOTENCY_KEY_REUSE_CONFLICT (NÃO é no-op —
              não se devolve silenciosamente o resultado antigo para um pedido diferente).
              [Fonte: research.md §3.3; SRC-CONC-01 [EXTERNO]; RULE-CBP-013]  [EMENDA-PROPOSTA v1.2]

RULE-CBP-006: As publicações num mesmo workspace DEVEM ter ORDEM TOTAL DE COMMIT, persistida e imutável (seq
              monotônico atribuído no instante do commit e nunca reescrito); a ordem é reconstruível por replay.
              Eventos/publicações fora de ordem de chegada NÃO DEVEM produzir estado ambíguo — a ordem de commit
              é a verdade.
              [Fonte: research.md §3.3; P13; RULE-CBP-013]  [EMENDA-PROPOSTA v1.2]

RULE-CBP-007: Todo objeto publicado DEVE ter proveniência suficiente para reconstrução (P13/RULE-010):
              computed_by (quem/qual atividade — da identidade AUTENTICADA pelo runtime, RULE-CBP-014),
              derived_from (ancestrais, quando aplicável) e, quando o objeto resulta de um gate, gate_record.
              O gate_record DEVE conter no mínimo: gate_id, gate_version, resultado (accept/deny + motivo),
              referência/hash da entrada avaliada e avaliador. O Blackboard NÃO fixa sobre qual valor um gate
              consumidor opera (fronteira SPEC-003/N3 — não reaberta).
              [Fonte: BL-029; RULE-010; CONSTITUTION P13; W3C PROV [EXTERNO]]  [EMENDA-PROPOSTA v1.2]

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

RULE-CBP-011: O estado LÓGICO do Blackboard DEVE ser reconstruível por REPLAY das versões append-only
              (reconstrução histórica). O replay reconstrói o estado LÓGICO a partir dos registros persistidos;
              NÃO implica reprodução dos ambientes externos de origem (mercado, feeds, execução de agentes).
              Replay correto ≠ conteúdo semanticamente correto: o replay garante fidelidade ao que foi
              registrado, não a correção do que foi registrado. O mecanismo FÍSICO de storage (grafo real vs.
              memória) é H-001/SPEC-006 e o estado por agente é G-001/SPEC-009 — NÃO fixados aqui (por referência).
              [Fonte: P13; RULE-010; H-001/G-001 (ABERTAS); SRC-ES-01 [EXTERNO]]  [EMENDA-PROPOSTA v1.2]

RULE-CBP-012: O gate de escrita E3 (permissão/append-only) DEVE declarar método amostral de observação de
              falso-DENY (publicação válida negada por engano) — ENF-07. O LIMIAR amostral é gap de
              enforcement aberto (atomic-spec §12), não fixado aqui; enquanto o limiar não é definido, o
              enforcement do E3 é declarado CONDICIONAL (ENF-07) — não fechado (BL-002).
              [Fonte: ENF-07; BL-002; atomic-spec §12]  [PROPOSTA]

RULE-CBP-013: ATOMICIDADE DE PUBLICAÇÃO — nenhuma operação de publicação DEVE produzir estado parcial
              OBSERVÁVEL. Em particular, NÃO DEVE existir estado observável em que: (a) exista versão sem
              proveniência; (b) exista chave de idempotência consumida sem resultado registrado; (c) exista seq
              (ordem de commit) consumido sem publicação correspondente; (d) exista publicação sem registro de
              auditoria. Ou a publicação se completa como unidade (versão + proveniência + seq + idempotência +
              auditoria) ou NÃO produz nenhum efeito observável (fail-closed). O versionamento otimista é
              realizado como compare-and-commit atômico (RULE-CBP-004).
              [Fonte: INV-07; ENF-04; research.md §3.3; SRC-CONC-01 [EXTERNO]]  [EMENDA-PROPOSTA v1.2]

RULE-CBP-014: IDENTIDADE / AUTORIDADE — nenhum invariante do Blackboard PODE depender da cooperação ou da
              honestidade do publicador. O agent_id usado no gate de permissão de workspace (RULE-CBP-002) e o
              computed_by da proveniência (RULE-CBP-007) DEVEM vir da identidade AUTENTICADA pelo runtime, NÃO
              de campo do payload. Distingue-se proveniência DECLARADA (o que o payload afirma) de proveniência
              AUTENTICADA (o que o runtime confirma): divergência entre agent_id declarado no payload e a
              identidade autenticada resulta em WORKSPACE_WRITE_FORBIDDEN (não se confia no payload). O
              mecanismo de autenticação é COMO (BUILD/SPEC-042), não fixado aqui. É DECISÃO CONSCIENTE que a
              leitura global de qualquer workspace decorre de RULE-BB-002 (vigente, NÃO alterada por esta Spec).
              [Fonte: RULE-BB-002; ENF-03/04; INV-05]  [EMENDA-PROPOSTA v1.2]
```

> **Invariante local desta Spec [EMENDA-PROPOSTA v1.2]:**
> **INV-CBP-01 (Append-only real):** o registro histórico de uma versão publicada NUNCA é mutado; "SUPERSEDED"
> é projeção derivada do estado corrente (existe sucessora que referencia a versão por `supersedes`), não um
> campo reescrito no registro passado. Reforça — não redefine — INV-07 e RULE-BB-004. [EMENDA-PROPOSTA v1.2]

---

## Capacidades e papéis (identidade/autoridade — RULE-CBP-014) [EMENDA-PROPOSTA v1.2]

> **Princípio:** nenhum invariante do Blackboard pode depender da cooperação ou honestidade do publicador. A
> autoridade é posicional (de onde vem a identidade), não declarativa (o que o payload afirma). O **QUEM** (quais
> entidades existem) é desta Spec; o **COMO** se autentica/autoriza é BUILD/runtime (SPEC-042) — não fixado aqui.

**Papéis:**
- **Agente** = **proponente** — submete objetos; não é autoridade sobre a própria permissão nem sobre o commit.
- **Harness** = **autoridade de contrato** — define/valida o contrato mínimo, a Classe, a proveniência exigível (gate determinístico; LLM nunca é gate — ENF-03).
- **Runtime** = **autoridade de commit** — autentica a identidade, aplica o compare-and-commit atômico, atribui seq, grava auditoria. `agent_id`/`computed_by` vêm daqui, não do payload.
- **Storage** = substrato append-only — guarda registros imutáveis; não decide permissão nem autoria.

**Tabela de capacidades** (DENY = negado por construção, fail-closed):

| Capacidade | Agente | Harness | Runtime | Storage |
|---|---|---|---|---|
| Ler qualquer workspace (RULE-BB-002 — decisão consciente, regra NÃO alterada) | PERMIT | PERMIT | PERMIT | PERMIT (mecânico) |
| Publicar no PRÓPRIO workspace | PERMIT (proposta; commit é do runtime) | — | PERMIT (executa commit) | — |
| Publicar em workspace ALHEIO | **DENY** | **DENY** | **DENY** | **DENY** |
| Atualizar/deletar registro HISTÓRICO (mutação/deleção) | **DENY** | **DENY** | **DENY** (só append) | **DENY** |
| Reconstruir por replay (leitura) | PERMIT | PERMIT | PERMIT | PERMIT (mecânico) |
| Alterar a autorização/identidade (quem pode o quê) | **DENY** | **DENY** (propõe policy; homologação de Andraus — RULE-HG-03) | **DENY** | **DENY** |

> **Nota (CONS-01):** a leitura global de qualquer workspace é registrada aqui como **decisão consciente** que
> decorre de **RULE-BB-002 vigente** — esta Spec NÃO altera RULE-BB-002. A governança de *quem pode o quê em
> runtime* (allow/deny de produção) é **SPEC-042**, não fechada aqui.

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
3. Quando um objeto existente é atualizado, o Blackboard DEVE criar uma nova versão que carrega `supersedes` (referência à anterior) e NÃO DEVE deletar NEM mutar o registro da versão anterior; o estado "SUPERSEDED" da versão anterior é PROJEÇÃO DERIVADA do estado corrente, não um campo reescrito no registro histórico (append-only real, INV-07, INV-CBP-01).
4. Quando uma publicação chega com expected_version divergente da versão corrente, o Blackboard DEVE rejeitar a escrita como conflito de concorrência e NÃO DEVE corromper o objeto.
4-bis. Quando uma publicação de ATUALIZAÇÃO (o objeto já existe no workspace) não informa expected_version, o Blackboard DEVE rejeitar a escrita (fail-closed) com o código "EXPECTED_VERSION_REQUIRED" e NÃO DEVE aplicar a atualização; a CRIAÇÃO de objeto novo (sem versão anterior) permanece permitida sem expected_version (create = versão inicial).
5. Quando a mesma publicação é reprocessada (retry) com a mesma chave de idempotência, o Blackboard NÃO DEVE criar objeto/versão duplicado.
6. Quando publicações concorrentes chegam ao mesmo workspace, o Blackboard DEVE impor ordem determinística e reconstruível e NÃO DEVE produzir estado ambíguo.
7. Quando um objeto é publicado, o Blackboard DEVE registrar sua proveniência (computed_by; derived_from/gate_record quando aplicável) suficiente para reconstrução (P13).
8. Quando um objeto-hipótese é armazenado, o Blackboard DEVE usar os estados do CHM-001 e NÃO DEVE definir estado de hipótese próprio (RULE-BB-003 SUPERSEDED por Q-006).
9. Quando um objeto de memória de trabalho expira ou é invalidado, o Blackboard DEVE transitá-lo para estado terminal preservando o histórico e NÃO DEVE deletá-lo.
10. Quando o estado do Blackboard precisa ser reconstruído, o Blackboard DEVE permitir replay das versões append-only, sem fixar o mecanismo físico de storage (H-001/SPEC-006).
11. Quando o gate de escrita E3 nega uma publicação, o Blackboard DEVE registrar observabilidade amostral de falso-DENY (ENF-07) para auditoria posterior.
12. Quando uma publicação é processada, o Blackboard NÃO DEVE produzir estado parcial observável (versão sem proveniência, chave de idempotência sem resultado, seq consumido sem publicação, ou publicação sem registro de auditoria): ou a publicação se completa como unidade atômica, ou não produz efeito observável. [EMENDA-PROPOSTA v1.2]
13. Quando a mesma chave de idempotência é reapresentada com payload diferente (request_fingerprint divergente), o Blackboard DEVE rejeitar com "IDEMPOTENCY_KEY_REUSE_CONFLICT" e NÃO DEVE devolver silenciosamente o resultado original nem aplicar o novo payload. [EMENDA-PROPOSTA v1.2]
14. Quando um retry chega após o commit mas antes do ACK (mesma chave, mesmo payload), o Blackboard DEVE devolver o resultado original SEM novo commit e NÃO DEVE criar objeto/versão duplicado. [EMENDA-PROPOSTA v1.2]
15. Quando o `agent_id` declarado no payload diverge da identidade autenticada pelo runtime, o Blackboard DEVE rejeitar a escrita com "WORKSPACE_WRITE_FORBIDDEN" e usar a identidade AUTENTICADA (não o payload) para o gate de workspace e para `computed_by`. [EMENDA-PROPOSTA v1.2]

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
  ENTÃO:        O Blackboard permite a escrita somente no workspace de responsabilidade do agente, usando a
                identidade AUTENTICADA pelo runtime (não o agent_id do payload); publicação em workspace alheio
                é rejeitada (fail-closed); leitura de qualquer workspace é permitida
  PORQUE:       Escrita só no próprio workspace, leitura livre (RULE-BB-002); cross-workspace corrompe o
                estado compartilhado (efeito irreversível) — fail-closed; o LLM nunca é o gate (ENF-03);
                nenhum invariante pode depender da honestidade do publicador (RULE-CBP-014)
  REFERÊNCIA:   RULE-BB-002; ENF-03/04; RULE-CBP-002/014
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de autorização por (agent_id AUTENTICADO, workspace); checagem binária de posse
    GATE DE SAÍDA: verificação (workspace == workspace_da_identidade_autenticada) para escrita
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
  ENTÃO:        O Blackboard cria uma NOVA versão (sucessora) que carrega supersedes = referência à anterior;
                o REGISTRO da versão anterior é PRESERVADO e NÃO é mutado (nenhum campo reescrito nele — não se
                grava superseded_by no registro v1); "SUPERSEDED" é projeção derivada do estado corrente;
                deleção destrutiva OU mutação de registro histórico é rejeitada (fail-closed)
  PORQUE:       Blackboard append-only REAL; objetos são SUPERSEDED (projeção derivada), nunca deletados nem
                reescritos (RULE-BB-004; INV-07; INV-CBP-01)
  REFERÊNCIA:   RULE-BB-004; INV-07; INV-CBP-01; RULE-CBP-003
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que barra deleção E mutação do registro histórico + cria versão sucessora
                  com supersedes; superseded_by, se existir, é índice DERIVADO (reconstruível por replay)
    GATE DE SAÍDA: verificação (nenhuma deleção/mutação aplicada ao registro anterior ∧ sucessora carrega supersedes)
    CRITÉRIO 4Es: Conformidade > Eficácia — versionamento monotônico (INV-07) e append-only real (INV-CBP-01) invioláveis
  VERIFICADO POR:
    DADO        objeto O v1 atualizado para O v2
    QUANDO      a atualização roda
    ENTÃO       registro de O v1 inalterado e preservado; O v2 corrente e carrega supersedes="O@v1"; nada deletado nem reescrito
    VERIFICAÇÃO v1_record_mutated == false; v1_deleted == false; v2.supersedes == "O@v1"; superseded_of(v1) derivado == true
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
  ENTÃO:        O Blackboard, se o payload é o MESMO (request_fingerprint coincide), devolve o resultado
                original SEM novo commit e NÃO cria objeto/versão duplicado; se o payload DIFERE (fingerprint
                divergente), rejeita com IDEMPOTENCY_KEY_REUSE_CONFLICT (não devolve resultado antigo nem
                aplica o novo). A chave + commit + resultado são gravados na MESMA unidade atômica
  PORQUE:       Idempotência garante exatamente-uma-vez sob retry/falha (SRC-CONC-01); reusar a chave para
                payload diferente é erro, não no-op (RULE-CBP-005/013)
  REFERÊNCIA:   RULE-CBP-005/013; research.md §3.3; SRC-CONC-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : deduplicação determinística por (idempotency_key, request_fingerprint); mesma chave+payload = no-op
                  que devolve resultado original; mesma chave+payload diferente = IDEMPOTENCY_KEY_REUSE_CONFLICT
    CRITÉRIO 4Es: Eficácia — evitar duplicata e reuso ambíguo preserva a integridade do quadro; Eficiência (retry seguro)
  VERIFICADO POR:
    DADO        publicação P com idempotency_key K (fingerprint F) processada duas vezes com o mesmo payload
    QUANDO      o segundo processamento roda
    ENTÃO       nenhum objeto/versão duplicado; resultado idêntico ao primeiro; sem novo commit
    VERIFICAÇÃO duplicate_created == false; result_identical == true; new_commit == false
    DADO        chave K já usada (fingerprint F); nova publicação com K mas payload diferente (fingerprint F')
    QUANDO      o processamento roda
    ENTÃO       rejeição "IDEMPOTENCY_KEY_REUSE_CONFLICT"; nada aplicado; resultado antigo NÃO devolvido como sucesso
    VERIFICAÇÃO error_code == "IDEMPOTENCY_KEY_REUSE_CONFLICT"; stale_result_returned == false
```

### BASpec-CBP-006 — Ordenação determinística de publicações no workspace

```
BASpec-CBP-006:
  QUANDO:       Publicações concorrentes ou fora de ordem de chegada chegam ao mesmo workspace
  ENTÃO:        O Blackboard impõe uma ORDEM TOTAL DE COMMIT, persistida e imutável (seq monotônico atribuído no
                commit e nunca reescrito), por workspace, e produz estado reconstruível, não ambíguo
  PORQUE:       Ordem de commit persistida é a verdade e pré-condição de reconstrução histórica (P13);
                fora-de-ordem de chegada não deve gerar estado ambíguo (SRC-CONC-01)
  REFERÊNCIA:   RULE-CBP-006; P13; SRC-CONC-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : atribuição determinística de seq no COMMIT (ordem total por workspace), persistida e imutável
    CRITÉRIO 4Es: Eficácia — ordem de commit imutável garante reconstrução unívoca
  VERIFICADO POR:
    DADO        duas publicações concorrentes no mesmo workspace
    QUANDO      ambas são admitidas
    ENTÃO       ordem total de COMMIT (seq persistido/imutável) atribuída; replay reproduz o mesmo estado
    VERIFICAÇÃO total_order_assigned == true; replay_deterministic == true
```

### BASpec-CBP-007 — Proveniência obrigatória (computed_by / gate_record / derived_from) [BL-029]

```
BASpec-CBP-007:
  QUANDO:       Um objeto é publicado no Blackboard
  ENTÃO:        O Blackboard exige proveniência suficiente para reconstrução — computed_by (quem/qual
                atividade, da identidade AUTENTICADA pelo runtime — RULE-CBP-014), derived_from (ancestrais,
                quando derivado) e gate_record (quando o objeto resulta de um gate) contendo no mínimo gate_id,
                gate_version, resultado, referência/hash da entrada e avaliador; objeto sem a proveniência
                exigível é rejeitado; o Blackboard NÃO fixa sobre qual valor um gate consumidor opera (SPEC-003/N3)
  PORQUE:       Reconstrução D9 (P13/RULE-010) exige proveniência; BL-029 (dona=SPEC-004) materializa aqui
  REFERÊNCIA:   RULE-CBP-007/014; BL-029; RULE-010; CONSTITUTION P13; W3C PROV [EXTERNO]
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
  ENTÃO:        O Blackboard reconstrói o estado LÓGICO por REPLAY das versões append-only, de forma
                determinística; o replay NÃO reproduz ambientes externos de origem e replay correto ≠ conteúdo
                semanticamente correto; o mecanismo FÍSICO de storage NÃO é fixado (H-001/SPEC-006; G-001/SPEC-009)
  PORQUE:       Append-only permite replay/reconstrução do estado lógico (SRC-ES-01); P13 (toda decisão
                reconstruível); storage físico é fronteira (H-001/G-001 ABERTAS)
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

### BASpec-CBP-013 — Atomicidade de publicação (sem estado parcial observável) [EMENDA-PROPOSTA v1.2]

```
BASpec-CBP-013:
  QUANDO:       Uma publicação é processada (criação ou atualização), inclusive sob falha/crash no meio
  ENTÃO:        O Blackboard ou completa a publicação como UNIDADE ATÔMICA (versão + proveniência + seq +
                idempotência + registro de auditoria) ou NÃO produz nenhum efeito observável; nunca há estado
                parcial observável (versão sem proveniência, chave sem resultado, seq sem publicação,
                publicação sem auditoria); o compare-and-commit da versão otimista é indivisível (RULE-CBP-004)
  PORQUE:       Estado parcial observável corrompe reconstrução, contagem e integridade (INV-07); fail-closed (ENF-04)
  REFERÊNCIA:   RULE-CBP-013/004/005; INV-07; ENF-04; SRC-CONC-01 [EXTERNO]
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : commit atômico tudo-ou-nada (compare-and-commit); efeitos (versão/proveniência/seq/idempotência/
                  auditoria) tornam-se observáveis juntos ou nenhum
    GATE DE SAÍDA: verificação (nenhum efeito observável fora da unidade atômica)
    CRITÉRIO 4Es: Conformidade > Eficácia — integridade do quadro acima de desempenho
  VERIFICADO POR:
    DADO        uma publicação interrompida por crash após o cálculo da versão mas antes do commit completo
    QUANDO      o estado é observado
    ENTÃO       nenhum efeito parcial: nem versão, nem seq, nem chave consumida sem resultado
    VERIFICAÇÃO partial_state_observable == false; (committed_fully == true XOR no_effect == true)
```

### BASpec-CBP-014 — Identidade autenticada / autoridade (nenhum invariante depende do publicador) [EMENDA-PROPOSTA v1.2]

```
BASpec-CBP-014:
  QUANDO:       Uma publicação chega com agent_id/computed_by declarados no payload
  ENTÃO:        O Blackboard usa a identidade AUTENTICADA pelo runtime (não o payload) para o gate de workspace
                e para computed_by; se o agent_id declarado diverge da identidade autenticada, rejeita com
                WORKSPACE_WRITE_FORBIDDEN; nenhum invariante depende da honestidade do publicador
  PORQUE:       Confiar no payload permitiria forjar posse de workspace e proveniência (RULE-BB-002; RULE-CBP-014);
                proveniência DECLARADA ≠ AUTENTICADA
  REFERÊNCIA:   RULE-CBP-014/002/007; RULE-BB-002; ENF-03/04
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que substitui/valida agent_id e computed_by pela identidade autenticada do runtime
    GATE DE SAÍDA: verificação (agent_id_efetivo == identidade_autenticada ∧ computed_by derivado da autenticada)
    CRITÉRIO 4Es: Conformidade > Eficácia — integridade de autoridade é inviolável
  VERIFICADO POR:
    DADO        payload declara agent_id == "B" mas a identidade autenticada é "A" (dona de outro workspace)
    QUANDO      o gate roda
    ENTÃO       rejeição "WORKSPACE_WRITE_FORBIDDEN"; identidade autenticada prevalece; payload não confiável
    VERIFICAÇÃO error_code == "WORKSPACE_WRITE_FORBIDDEN"; identity_source == "runtime_authenticated"
```

---

## D4 — Algoritmo

Mecânicas **determinísticas reais** especificáveis (D4 "onde há regra determinística real" — atomic-spec §2):
- **Versionamento otimista = compare-and-commit atômico (CBP-004/013):** numa ATUALIZAÇÃO, `atomic { aceita ⇔ (expected_version presente ∧ expected_version == current_version) ⇒ grava v(n+1) }` — comparar e gravar são INDIVISÍVEIS; `expected_version` divergente ⇒ `VERSION_CONFLICT`; `expected_version` ausente ⇒ `EXPECTED_VERSION_REQUIRED` (fail-closed). Na CRIAÇÃO (objeto novo) `expected_version` não é exigido (versão inicial). Sem estado parcial observável.
- **Idempotência (CBP-005):** `se idempotency_key ∈ processed ∧ fingerprint == armazenado ⇒ devolve resultado original SEM novo commit; se idempotency_key ∈ processed ∧ fingerprint ≠ armazenado ⇒ IDEMPOTENCY_KEY_REUSE_CONFLICT; senão processa e grava {chave, fingerprint, resultado} na MESMA unidade atômica do commit` — exatamente-uma-vez.
- **Permissão de escrita (CBP-002/014):** `aceita_escrita ⇔ workspace_alvo == workspace_da_identidade_AUTENTICADA`; `agent_id` declarado ≠ autenticado ⇒ `WORKSPACE_WRITE_FORBIDDEN`; leitura sempre permitida.
- **Append-only real/supersessão (CBP-003):** `update(O) ⇒ nova versão v(n+1) com supersedes=O@v(n); registro de O@v(n) IMUTÁVEL (não reescrito); superseded(O@v(n)) é DERIVADO (∃ sucessora que o referencia); proibido delete(O) e mutate(O@v(n))`.
- **Ordenação por commit (CBP-006):** `seq := seq+1` atribuído no COMMIT, persistido e imutável; replay ordena por `(workspace, seq)`.
- **Replay (CBP-011):** `estado_lógico(T) := fold(aplica_versões ordenadas por (workspace, seq) até T)` — reconstrói o estado LÓGICO; não reproduz ambientes externos de origem.

Nenhuma fórmula depende de J-001/N-001 (o Blackboard não computa convicção). Não há limiar numérico de convicção neste Plan. [FONTE: atomic-spec §2; research.md §3.3]

---

## D5 — Máquina de estados (ciclo operacional do objeto no Blackboard)

> **Fronteira (CC-02) — separação `publication_state` × `domain_state` [EMENDA-PROPOSTA v1.2]:** este é o
> **`publication_state`** (ciclo operacional de PUBLICAÇÃO do objeto no quadro — vida do Blackboard). Ele é
> SEPARADO do **`domain_state`** (o estado de domínio do objeto: máquina do CHM-001 para hipótese; enum M-001
> ABERTA para não-hipótese). Os dois coexistem no contrato sem se confundir: o Blackboard controla
> `publication_state`; o `domain_state` pertence aos contratos canônicos (CHM-001/CEM-001/CCM-001) e a M-001 —
> **não redefinidos** (CC-02).

Ciclo operacional de publicação — `publication_state` [PROPOSTA]:

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
1. **Submissão:** o produtor submete objeto + `schema_version` + `expected_version` + `idempotency_key` + proveniência declarada.
2. **Identidade autenticada (CBP-014):** o runtime resolve a identidade AUTENTICADA; `agent_id`/`computed_by` vêm dela, não do payload; `agent_id` declarado ≠ autenticado ⇒ `WORKSPACE_WRITE_FORBIDDEN`.
3. **Idempotência (CBP-005):** chave já processada com MESMO `request_fingerprint` → devolve resultado original sem novo commit; chave com fingerprint DIFERENTE → `IDEMPOTENCY_KEY_REUSE_CONFLICT`.
4. **Permissão (CBP-002, E3):** workspace alvo == workspace da identidade autenticada? Senão `WORKSPACE_WRITE_FORBIDDEN` (fail-closed).
5. **Contrato (CBP-001) + proveniência (CBP-007):** campos mínimos + `computed_by` + `gate_record` (gate_id/gate_version/resultado/ref-hash/avaliador) presentes? Senão rejeita.
6. **Commit atômico (CBP-004/013):** compare-and-commit indivisível — `expected_version == current_version`? Senão `VERSION_CONFLICT`. No MESMO ato atômico: cria nova versão com `supersedes`, atribui `seq` (ordem de commit imutável), grava idempotência+resultado+auditoria. Registro histórico NÃO é mutado (CBP-003). Nenhum estado parcial observável.
7. **Publicação:** objeto com `publication_state=PUBLISHED`; proveniência/seq anexados; reconstrução por replay (P13/RULE-010).
8. **Expiração/invalidação (CBP-010):** quando aplicável, transição terminal não-destrutiva.
9. **Observabilidade (CBP-012):** DENY do gate E3 amostrado para auditoria (ENF-07/BL-002; E3 condicional até o limiar).

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

### Cenário-CBP-T03 — Update append-only REAL: registro anterior imutável [EMENDA-PROPOSTA v1.2]
```
DADO        objeto O v1 atualizado para v2
QUANDO      a atualização roda
ENTÃO       registro de O v1 PRESERVADO e NÃO mutado; O v2 corrente carrega supersedes="O@v1";
            "SUPERSEDED" de v1 é projeção derivada; nada deletado nem reescrito
VERIFICAÇÃO v1_record_mutated == false; v1_deleted == false; v2.supersedes == "O@v1"
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
ENTÃO       ordem total de COMMIT (seq persistido/imutável) imposta; replay reproduz o mesmo estado
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

### Cenário-CBP-T11 — Mesma chave de idempotência + payload diferente → conflito [EMENDA-PROPOSTA v1.2]
```
DADO        idempotency_key K já usada (fingerprint F); nova publicação com K e payload diferente (F')
QUANDO      o processamento roda
ENTÃO       rejeição "IDEMPOTENCY_KEY_REUSE_CONFLICT"; nada aplicado; resultado antigo NÃO devolvido como sucesso
VERIFICAÇÃO error_code == "IDEMPOTENCY_KEY_REUSE_CONFLICT"; stale_result_returned == false
```

### Cenário-CBP-T12 — Retry após commit antes do ACK → devolve resultado original [EMENDA-PROPOSTA v1.2]
```
DADO        publicação P (chave K, payload F) que fez COMMIT mas cujo ACK se perdeu; cliente reenvia P
QUANDO      o retry roda
ENTÃO       devolve o resultado original SEM novo commit; nenhum objeto/versão duplicado
VERIFICAÇÃO new_commit == false; duplicate_created == false; result_identical == true
```

### Cenário-CBP-T13 — agent_id forjado no payload ≠ identidade autenticada → rejeição [EMENDA-PROPOSTA v1.2]
```
DADO        payload declara agent_id "B" (dono de outro workspace); identidade autenticada é "A"
QUANDO      o gate de permissão roda
ENTÃO       rejeição "WORKSPACE_WRITE_FORBIDDEN"; identidade autenticada prevalece; payload não confiável
VERIFICAÇÃO error_code == "WORKSPACE_WRITE_FORBIDDEN"; identity_source == "runtime_authenticated"
```

### Cenário-CBP-T14 — Corrida de compare-and-commit na mesma expected_version → exatamente uma vence [EMENDA-PROPOSTA v1.2]
```
DADO        duas atualizações concorrentes do objeto O v3, ambas com expected_version == 3
QUANDO      ambas correm o compare-and-commit atômico
ENTÃO       exatamente UMA comita (O v4); a outra recebe "VERSION_CONFLICT"; sem lost update; sem estado parcial
VERIFICAÇÃO exactly_one_committed == true; lost_update == false; partial_state_observable == false
```

### Cenário-CBP-T15 — Crash após commit antes do ACK → sem estado parcial [EMENDA-PROPOSTA v1.2]
```
DADO        publicação que completou o commit atômico mas sofreu crash antes de responder
QUANDO      o estado é observado e o cliente faz retry (mesma chave, mesmo payload)
ENTÃO       o commit está íntegro e completo (unidade atômica); retry devolve o resultado original; sem duplicata
VERIFICAÇÃO partial_state_observable == false; new_commit == false; duplicate_created == false
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
**ENTÃO:** impor ordem total de COMMIT (seq persistido/imutável); rejeitar estado ambíguo (`NONDETERMINISTIC_ORDER_FORBIDDEN`)
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

### ADV-CBP-12 — Mesma chave de idempotência com payload diferente tratada como no-op (viola CBP-005) [EMENDA-PROPOSTA v1.2]
**DADO:** chave K já usada (fingerprint F); nova publicação com K e payload diferente (F')
**QUANDO:** o processamento roda
**ENTÃO:** rejeitar `IDEMPOTENCY_KEY_REUSE_CONFLICT`; NÃO devolver o resultado antigo como sucesso nem aplicar o novo
**PORQUE:** reusar a chave para pedido diferente mascara erro e corrompe a semântica exatamente-uma-vez (RULE-CBP-005)
**VERIFICAÇÃO:** error_code == "IDEMPOTENCY_KEY_REUSE_CONFLICT"; stale_result_returned == false

### ADV-CBP-13 — Corrida na mesma chave de idempotência (viola CBP-005/013) [EMENDA-PROPOSTA v1.2]
**DADO:** dois processamentos concorrentes da MESMA chave K (mesmo payload)
**QUANDO:** ambos correm
**ENTÃO:** exatamente UM commit; o outro converge ao mesmo resultado sem segundo commit; sem duplicata
**PORQUE:** chave+commit+resultado na mesma unidade atômica garantem exatamente-uma-vez sob corrida (RULE-CBP-013)
**VERIFICAÇÃO:** exactly_one_commit == true; duplicate_created == false

### ADV-CBP-14 — Corrida de compare-and-commit na mesma expected_version (viola CBP-004/013) [EMENDA-PROPOSTA v1.2]
**DADO:** duas atualizações concorrentes com a MESMA expected_version corrente
**QUANDO:** ambas correm o compare-and-commit
**ENTÃO:** exatamente UMA vence; a outra recebe `VERSION_CONFLICT`; sem lost update; sem estado parcial
**PORQUE:** comparar e gravar são indivisíveis — não há janela para duas vencerem (RULE-CBP-004/013)
**VERIFICAÇÃO:** exactly_one_committed == true; lost_update == false; partial_state_observable == false

### ADV-CBP-15 — agent_id forjado no payload (viola CBP-014/RULE-BB-002) [EMENDA-PROPOSTA v1.2]
**DADO:** payload declara agent_id de outro agente/workspace; identidade autenticada é outra
**QUANDO:** o gate de permissão roda
**ENTÃO:** rejeitar `WORKSPACE_WRITE_FORBIDDEN`; usar a identidade AUTENTICADA (não o payload)
**PORQUE:** nenhum invariante pode depender da honestidade do publicador (RULE-CBP-014; RULE-BB-002)
**VERIFICAÇÃO:** error_code == "WORKSPACE_WRITE_FORBIDDEN"; identity_source == "runtime_authenticated"

### ADV-CBP-16 — Crash após commit antes do ACK produz duplicata/estado parcial (viola CBP-013) [EMENDA-PROPOSTA v1.2]
**DADO:** publicação que comitou atomicamente mas sofreu crash antes do ACK; cliente faz retry
**QUANDO:** o estado é observado e o retry roda
**ENTÃO:** nenhum estado parcial observável; retry devolve o resultado original SEM novo commit; sem duplicata
**PORQUE:** atomicidade tudo-ou-nada + idempotência por chave (RULE-CBP-013/005)
**VERIFICAÇÃO:** partial_state_observable == false; new_commit == false; duplicate_created == false

> **Cobertura:** 16 cenários adversariais (mínimo CRITICAL = ≥1; foco homologado em concorrência/duplicidade/versionamento + atomicidade + identidade — DHR-SPEC004-001 §1; emenda v1.2). Cobrem casos de negação das BASpecs com efeito (inclui CBP-013/014) e das fronteiras abertas (M-001, H-001, G-001, SPEC-005/006/009). Mapeiam para EC-CBP-001..007 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada publicação DEVE ser reconstruível (P13/RULE-010): objeto + versão + proveniência (computed_by AUTENTICADO/gate_record com gate_id·gate_version·resultado·ref-hash·avaliador/derived_from), ordem de COMMIT (seq por workspace, imutável), supersessão (`supersedes` gravado; `superseded_by` derivado), `publication_state`, resultado do gate de escrita (accept/deny + motivo). O replay reconstrói o estado **LÓGICO** do Blackboard a partir dos registros persistidos — **não** implica reprodução dos ambientes externos de origem; **replay correto ≠ conteúdo semanticamente correto** (fidelidade ao registrado, não correção do registrado). A **reconstrução expandida de linhagem** (Cognitive Trace Reconstruction) e o **storage físico** pertencem ao **Knowledge Graph (SPEC-006 / H-001 ABERTA)** e ao **estado por agente (SPEC-009 / G-001 ABERTA)** — aqui ficam **por referência** (coerente com alvo D0–D7; CEM-001 Cap.5). [FONTE: CONSTITUTION P13; RULE-010; CEM-001 Cap.5; H-001/G-001 ABERTAS]

---

## Contrato de objeto do Blackboard — esqueleto [PROPOSTA]

> Produto central da SPEC-004. Projeta o Lineage do CEM-001 e os estados do CHM-001 **sem redefini-los** (CC-02). **Estrutura/mecânica; enum de estados não-hipótese = M-001 (ABERTA).**

| Camada | Conteúdo | Fronteira |
|---|---|---|
| Identidade | `object_id`, `version`, `schema_version`, `previous_version_id`, `creation_timestamp`, `publication_state` (ACCEPTED/PUBLISHED/SUPERSEDED/EXPIRED/ARCHIVED/REJECTED) | Append-only real (INV-07/INV-CBP-01); registro histórico imutável |
| Estado de domínio | `domain_state` (CHM-001 p/ hipótese; M-001 ABERTA p/ não-hipótese) — SEPARADO de `publication_state` | CC-02 — não redefinido |
| Classificação | `object_type` (hypothesis \| evidence \| mission \| observation \| conviction \| ...), `workspace`, `namespace` | hipótese usa estado CHM-001; não-hipótese = M-001 (ABERTA) |
| Proveniência | `computed_by` (identidade AUTENTICADA pelo runtime — RULE-CBP-014), `derived_from[]`, `gate_record` (gate_id/gate_version/resultado/ref-hash-entrada/avaliador, quando resulta de gate) | BL-029; projeta Lineage CEM-001 (não redefine); declarada × autenticada |
| Concorrência/atomicidade | `expected_version`, `idempotency_key`, `request_fingerprint`, `seq` (ordem de COMMIT persistida e imutável) | compare-and-commit atômico (CBP-004/013); `expected_version` obrigatório em ATUALIZAÇÃO (ausente ⇒ EXPECTED_VERSION_REQUIRED), dispensado em CRIAÇÃO |
| Supersessão | `supersedes` (GRAVADO na sucessora); `superseded_by` = **índice DERIVADO** (reconstruível por replay — NÃO gravado no registro histórico) | nunca deletado nem mutado (CBP-003/INV-CBP-01) |
| Permissão | `owner_workspace` (escrita só pelo dono, via identidade autenticada; leitura livre) | RULE-BB-002; RULE-CBP-014 |
| Rastreabilidade | `reconstruction_ref` (replay do estado LÓGICO até o ponto) | P13/RULE-010; storage físico = SPEC-006/009; replay ≠ reprodução de ambientes externos |

---

## I/O Schemas (lógicos — referência; não redefinem CHM-001/CEM-001/CCM-001)

### Objeto publicado no Blackboard
```json
{
  "object_id": "BB-2026-10-03-001",
  "version": 2,
  "schema_version": "1 (versão do envelope do objeto; estratégia de migração NÃO definida aqui)",
  "previous_version_id": "BB-2026-10-03-001@v1",
  "creation_timestamp": "2026-10-03T12:00:00Z",
  "publication_state": "PUBLISHED (ciclo do Blackboard — SEPARADO de domain_state)",
  "domain_state": "CHM-001 enum (hipótese) | M-001 ABERTA (não-hipótese) — NÃO redefinido (CC-02)",
  "object_type": "evidence | hypothesis | mission | observation | conviction",
  "workspace": "institutional_agent",
  "owner_workspace": "institutional_agent",
  "provenance": {
    "computed_by": "institutional_agent/activity-123 (da identidade AUTENTICADA pelo runtime — RULE-CBP-014; NÃO do payload)",
    "derived_from": ["BB-...@v1"],
    "gate_record": "{ gate_id, gate_version, result, input_ref_or_hash, evaluator } | null (quando não resulta de gate)"
  },
  "expected_version": 1,
  "idempotency_key": "pub-abc-123",
  "request_fingerprint": "hash do payload (detecta reuso de chave com payload diferente — IDEMPOTENCY_KEY_REUSE_CONFLICT)",
  "seq": 42,
  "supersedes": "BB-2026-10-03-001@v1 (GRAVADO na sucessora)",
  "superseded_by": "DERIVADO — índice reconstruível por replay; NÃO gravado no registro histórico (INV-CBP-01)",
  "reconstruction_ref": "replay(workspace, seq) — estado LÓGICO; não reproduz ambientes externos"
}
```
> O objeto **armazena/versiona** hipótese (estado = CHM-001, não redefinido — RULE-BB-003 SUPERSEDED por Q-006), Evidência (CEM-001, idioma canônico INV-10) e Convicção (CCM-001) **sem redefini-los** (CC-02). O enum de estados não-hipótese é **M-001 (ABERTA)**. Nenhum campo computa convicção nem deriva de custo (INV-04 — fora do escopo deste componente).

---

## Enforcement Contracts

### EC-CBP-001 — Publicação de objeto (contrato + proveniência; append-only)
```
CAPABILITY   : Admitir e publicar um objeto no workspace próprio, versionado e com proveniência
EFFECT       : Publicação (commit) atômica de objeto/versão no estado compartilhado do Blackboard
PRECOND      : (contrato mínimo + schema_version presentes) AND (proveniência computed_by AUTENTICADA presente)
               AND (append-only real: nova versão com supersedes; registro histórico imutável)
POSTCOND     : objeto PUBLISHED; sucessora carrega supersedes; registro anterior NÃO mutado; histórico preservado
               (INV-07/INV-CBP-01); "SUPERSEDED" é projeção derivada
POLICY       : RULE-CBP-001/003/007/014; RULE-BB-002/004; BL-029; INV-07/INV-10/INV-CBP-01
LEVEL        : E2 (Operacional — estado compartilhado alterado; append-only, não destrutivo)
FAILURE-MODE : Fail-closed — contrato/proveniência ausente OU mutação de registro histórico ⇒ rejeitar; nada publicado; log
EVIDENCE     : log de publicação (versão, proveniência, seq); objeto recuperável por replay
```

### EC-CBP-002 — Gate de escrita (permissão de workspace + append-only) [E3]
```
CAPABILITY   : Autorizar ou negar a escrita (publicação/atualização/deleção) no Blackboard
EFFECT       : Commit em estado compartilhado (publicação) ou negação (DENY)
PRECOND      : (workspace alvo == workspace da identidade AUTENTICADA pelo runtime — RULE-BB-002/CBP-014) AND
               (nenhuma deleção destrutiva nem mutação de registro histórico — RULE-BB-004/INV-CBP-01) AND
               (gate determinístico; LLM nunca é o gate — ENF-03)
POSTCOND     : escrita só no próprio workspace; deleção destrutiva/mutação histórica impossível; append-only garantido;
               nenhum invariante depende da honestidade do publicador
POLICY       : RULE-CBP-002/003/014; RULE-BB-002/004; INV-07/INV-CBP-01; ENF-03/04
LEVEL        : E3 (Crítico — cross-workspace, deleção destrutiva e mutação histórica são irreversíveis; corrompem a cadeia)
FAILURE-MODE : Fail-closed — ambiguidade/violação/identidade divergente ⇒ negar (WORKSPACE_WRITE_FORBIDDEN); nada publicado/deletado; log
EVIDENCE     : gate_record (gate_id/gate_version/accept-deny+motivo/ref-hash/avaliador) + ENF-07: amostragem de falso-DENY.
             **Enforcement do E3 CONDICIONAL até o limiar amostral ser definido (BL-002) — NÃO fechado** (atomic-spec §12)
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
CAPABILITY   : Processar cada publicação exatamente uma vez, mesmo sob retry; detectar reuso de chave
EFFECT       : Publicação única, no-op que devolve resultado original, ou rejeição por reuso de chave
PRECOND      : (idempotency_key fornecida) AND (request_fingerprint calculável); chave+commit+resultado na MESMA unidade atômica
POSTCOND     : nenhum objeto/versão duplicado; mesma chave+payload ⇒ resultado original sem novo commit; mesma
               chave+payload diferente ⇒ IDEMPOTENCY_KEY_REUSE_CONFLICT (não no-op, não devolve resultado antigo)
POLICY       : RULE-CBP-005/013; SRC-CONC-01 [EXTERNO]
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed — chave repetida com mesmo payload ⇒ devolve original; com payload diferente ⇒ REUSE_CONFLICT
EVIDENCE     : registro de {idempotency_key, request_fingerprint, resultado}; ausência de duplicata
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

### EC-CBP-007 — Atomicidade de publicação (sem estado parcial observável) [EMENDA-PROPOSTA v1.2]
```
CAPABILITY   : Realizar cada publicação como unidade atômica tudo-ou-nada
EFFECT       : Efeitos (versão + proveniência + seq + idempotência + auditoria) observáveis juntos, ou nenhum
PRECOND      : (compare-and-commit indivisível — RULE-CBP-004) AND (chave+commit+resultado na mesma unidade)
POSTCOND     : nenhum estado parcial observável (versão sem proveniência, chave sem resultado, seq sem publicação,
               publicação sem auditoria); sob corrida na mesma expected_version, exatamente UMA vence
POLICY       : RULE-CBP-013/004/005; INV-07; ENF-04; SRC-CONC-01 [EXTERNO]
LEVEL        : E3 (Crítico — estado parcial observável corrompe reconstrução/contagem/integridade — irreversível)
FAILURE-MODE : Fail-closed — falha/crash no meio ⇒ nenhum efeito observável (rollback); retry via idempotência
EVIDENCE     : ausência de estado parcial em observação pós-crash; seq sem buraco; chave sempre com resultado
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
| Mutação do registro histórico ("marcar SUPERSEDED" reescrevendo v1) | INV-CBP-01; RULE-CBP-003; ADV-CBP-02; EC-CBP-001 (registro imutável; SUPERSEDED derivado) |
| Estado parcial observável (crash/corrida no meio da publicação) | RULE-CBP-013; ADV-CBP-13/14/16; EC-CBP-007 (compare-and-commit atômico) |
| Identidade forjada no payload (posse/proveniência falsa) | RULE-CBP-014; ADV-CBP-15; EC-CBP-002 (identidade autenticada do runtime) |
| Reuso de chave de idempotência com payload diferente | RULE-CBP-005; ADV-CBP-12; EC-CBP-004 (IDEMPOTENCY_KEY_REUSE_CONFLICT) |
| Estado de hipótese próprio (RULE-BB-003 descontinuada) | RULE-CBP-008; ADV-CBP-07; CHM-001 |
| LLM como gate de escrita | ENF-03; ADV-CBP-10; EC-CBP-002 (detector≠gate) |
| ACH-001 (fonte arXiv não verificável sustentando proposta) | SRC-MEM-01 arXiv rebaixada a não-load-bearing (Notas de honestidade); nenhuma proposta importada dela |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz o schema lógico do objeto do Blackboard; nenhum schema canônico do CHM-001/CEM-001/CCM-001 alterado.
- **RAG:** nenhum; o Blackboard não escreve no KG/RAG (memória permanente = SPEC-006).
- **Skills:** nenhuma Skill afetada; INV-06 preservado (Skill produz Observação; o Blackboard só a armazena).
- **Testes:** adiciona `checks.md` (verificação de spec); mecânica de concorrência/replay fica para BUILD.
- **Modelos dependentes:** CHM-001/CEM-001/CCM-001/SPEC-001 não alterados (construção SOBRE); RULE-BB-001..005 operacionalizadas, não alteradas.
- **Compatibilidade da EMENDA v1.2:** **[DECISÃO NECESSÁRIA] — potencialmente Major.** O item 1 (append-only REAL) **muda a semântica de representação da supersessão** em relação à v1.1: a v1.1 descrevia "marcar a anterior como SUPERSEDED (`superseded_by` preenchido)" — mutação do registro; a v1.2 proíbe mutar o registro histórico e torna `SUPERSEDED`/`superseded_by` projeção/índice derivado. Para qualquer implementação/schema que já assumisse `superseded_by` gravado, isto é **mudança incompatível (Major)**. Os demais itens (atomicidade, identidade autenticada, D8, menores) são **aditivos/endurecedores (Minor)** — não invalidam comportamento vigente além do item 1. **Classificação (Andraus, chat 2026-10-03, DHR-SPEC004-003): MINOR — clarificação de ambiguidade da v1.1** (nenhuma implementação existe; SPEC-001/002/003/038 não dependem de `superseded_by` gravado — parecer do Revisor). A v1.1 permanece no histórico (INV-07); a v1.2 é baseline desde DHR-SPEC004-003.

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07) e a Classe por BASpec (CC-11). A decisão de M-001 (enum de estados não-hipótese) é condição da homologação do Plan por Andraus.

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — pergunta adversarial por BASpec com efeito (cobertura TOTAL — CRITICAL, 14 BASpecs):**

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
- **CBP-013 (atomicidade, C) [v1.2]:** se errada → estado parcial observável (versão sem proveniência, seq sem publicação, chave sem resultado) → observável por `partial_state_observable=true` em observação pós-crash; verificável. Negação: ADV-CBP-13/14/16. QUANDO-sim-mas-ENTÃO-não: corrida na mesma expected_version → exatamente UMA vence (as demais VERSION_CONFLICT).
- **CBP-014 (identidade autenticada, C) [v1.2]:** se errada → publicador forja posse de workspace/proveniência → observável por objeto com `identity_source≠runtime_authenticated` ou escrita cross-workspace aceita; verificável. Negação: ADV-CBP-15. QUANDO-sim-mas-ENTÃO-não: leitura global permanece permitida (RULE-BB-002).

Todas as 14 BASpecs com efeito têm ENTÃO verificável por observador independente e caso de negação em D8. Nenhuma restou como [DECISÃO NECESSÁRIA] por falta de verificabilidade (as decisões abertas M-001/H-001/G-001 são fronteiras explícitas, não falhas de verificabilidade).

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
| EMENDA v1.2: RULE-CBP-003/004/005/006/007 reescritas; RULE-CBP-013/014; INV-CBP-01; BASpec-CBP-013/014; EC-CBP-007; EARS 12..15; ADV-CBP-12..16; T11..T15; tabela de capacidades/papéis; schema_version; publication_state×domain_state; request_fingerprint | [EMENDA-PROPOSTA v1.2] | Requer NOVA homologação (sobre v1.1 baselined); v1.1 preservada no histórico (INV-07) |
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
[x] Critérios em EARS (16 — 1..11 + 4-bis + 12..15); BASpecs completas (CBP-001..014) com Classe declarada (CC-11); RULEs citadas existentes vs propostas (RULE-CBP [PROPOSTA]/[EMENDA-PROPOSTA v1.2]) etiquetadas.
[x] Profundidade D0–D7 + rigor adversarial extra (D8) nos comportamentos de risco (concorrência/duplicidade/versionamento/atomicidade/identidade) atingida (D5 ciclo operacional; D6 protocolo; D7 x15; D8 x16; D9 por referência).
[x] Enforcement Contract em todo ato com efeito (EC-CBP-001..007); piso E2; E3 no gate de escrita (cross-workspace/deleção/mutação histórica irreversíveis; fail-closed) e no commit atômico (EC-CBP-007); ENF-07 amostral declarado no E3 — enforcement CONDICIONAL até o limiar (BL-002).
[x] Status epistemológico aplicado (FATO NORMATIVO / PROPOSTA / EXTERNO / DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: M-001, H-001, G-001, J-001, N-001, WF-D03 permanecem abertas (só mecânica/estrutura); nenhuma decisão aberta usada como invariante fechado.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos/achados registrados (ACH-001 arXiv; ACH-002 RULE-BB-003 superseded) — tratados, não silenciados.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE fabricada como vigente; sem baseline informal.
[x] 4Es na ordem; Conformidade > Eficácia (INV-07 e ENF-03 prevalecem). Latência N/A (camada spec-time).
[x] Dependências a montante homologadas (RULE-BB-*/CHM-001/CEM-001/CCM-001/SPEC-001/019/020/021/atomic-spec v1.5); não downstream de bloqueador aberto (M-001 é dona desta Spec, proposta não fechada).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); Bloco A cobre TODAS as 14 BASpecs com efeito (inclui CBP-013/014 da emenda v1.2) — obrigatório CRITICAL.
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
- **EMENDA v1.2 [EMENDA-PROPOSTA]** sobre a v1.1 baselined (origem: feedback externo de LLM — DADO, verificado por Andraus; nenhuma fonte/pontuação externa não-verificada importada, RULE-MET-01/RULE-ECC-04): (1) append-only REAL (registro histórico imutável; SUPERSEDED/superseded_by derivado — INV-CBP-01); (2) atomicidade de publicação / compare-and-commit atômico (RULE-CBP-013; EC-CBP-007); (3) identidade autenticada + tabela de capacidades/papéis (RULE-CBP-014); (4) D8 ampliado (ADV-CBP-12..16, T11..T15); menores (schema_version, ordem de commit imutável, nota de replay lógico, gate_record mínimo, publication_state×domain_state, E3 falso-DENY condicional). **[DECISÃO NECESSÁRIA] — compatibilidade potencialmente Major (item 1 muda a semântica de representação da supersessão): classificação Minor vs Major é de Andraus.** v1.1 preservada no histórico (INV-07); v1.2 só vira baseline na nova homologação (INV-09).
