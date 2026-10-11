# SPEC-006 — Cognitive Knowledge Graph

| Campo | Valor |
|---|---|
| ID | SPEC-006 — Cognitive Knowledge Graph (contrato cognitivo da **memória semântica permanente** do SOT — ontologia enxuta + entidades/relações tipadas + temporalidade + proveniência por referência + lifecycle + confiança de relação + consulta cognitiva + governança de escrita; **mecanismo físico de armazenamento INDETERMINADO — H-001 ABERTA**) |
| Versão | 1.0 (candidato a BASELINE) |
| Status | **CANDIDATO — aguarda verificação de spec (checks.md), gate determinístico, parecer do Revisor e homologação de Andraus.** NÃO é baseline (INV-09). Abertura HOMOLOGADA: DHR-SPEC006-001 (2026-10-11). As RULE-CKG-* e o contrato de nó/relação deste Plan são **[PROPOSTA]** até homologação. **H-001 (mecanismo físico do KG) permanece ABERTA — este Plan NÃO a fecha** (CONS-01; só Andraus). M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 seguem ABERTAS. |
| Fonte | ROADMAP §6 (FASE 3); `specs/features/SPEC-006/ABERTURA.md` + `research.md` + `sources/` (Dossiê — RULE-ECC-01/02/04/06; validade CRITICAL 90 dias, limite 2027-01-03); DHR-SPEC006-001; atomic-spec **v1.5** (§3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7); `governance/RULES.md` (RULE-BB-004, RULE-CAU-01, RULE-MECH-01, RULE-HD-02/03/04); `canon/CEM-001` (Responsabilidades do KG l.608-615), `canon/CHM-001`, `canon/CCM-001`, `canon/CEE-001` l.111, `canon/SAS-001` §6.12; `WORKFLOW.md` (conformidade, não editada) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §6 "P0 — CRITICAL"; atomic-spec §3 (emenda SPEC006-MATRIZ, 2026-10-05) "Knowledge Graph \| CRITICAL \| D0–D7"; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profundidade-alvo | **D0–D7 + D8 adversarial focado** nos pontos sensíveis (imutabilidade INV-07, confiança de relação ≠ Convicção INV-04, causalidade pós-hoc RULE-CAU, colisão de relações, governança de escrita), **sem elevar o profile em silêncio** — mesma reconciliação da SPEC-004 (CRITICAL, pin D0–D7, homologada "D0–D7 + D8 adversarial") [FONTE: ROADMAP §6; AGENTS.md §4 (CRITICAL → D0–D8 / profile standard+adversarial); DHR-SPEC006-001 Q-ABERTURA-2] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 3 — MEMÓRIA SEMÂNTICA E RAG; próxima na sequência após SPEC-005 (BASELINE v1.0, DHR-SPEC005-002). Opera **sobre** conhecimento já validado/publicado; a formação/retrieval é SPEC-007 (não absorvida) [FONTE: ROADMAP §6/§21] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3 teto spec-first; gate normativo E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01 (Classe por BASpec); RULE-PD-01/CC-12 **(N/A — infraestrutura de memória, agnóstica de escola)**; RULE-ECC-04 (verbatim); RULE-ECC-06 (repositórios); RULE-ECC-05 **(N/A — não toca comportamento de trading)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — **D** (ontologia/catálogo de entidades-relações, temporalidade, versionamento, consulta estruturada, Cognitive Trace Reconstruction) + **C** (governança de escrita, imutabilidade/append-only INV-07, proveniência obrigatória, confiança≠Convicção INV-04, fronteira "só conhecimento publicado") + **H** (juízo de similaridade/causalidade com gate de saída e mecanismo declarado — RULE-CAU); declaração normativa é **por BASpec** (SES-001 §50) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-11 |
| Abertura | Dossiê de Pesquisa HOMOLOGADO por Andraus (DHR-SPEC006-001, `research.md`); Plan iniciado dentro da validade do Dossiê (CRITICAL → 90 dias; limite 2027-01-03; ECC-VAL-001 FECHADA, DHR-DEC-003) |

Complexidade: CRITICAL. Profundidade-alvo: D0–D7 + D8 adversarial focado (standard + adversarial).

**Princípio fundador desta Spec (transversal):** **MEMÓRIA PERMANENTE ≠ MEMÓRIA DE TRABALHO.** *"Blackboard ↓ memória de trabalho. Knowledge Graph ↓ memória permanente. Nunca misturar."* (fundamento KERNEL-V2; ROADMAP §5/§6). O KG é a **representação semântica permanente do conhecimento já validado e suas relações auditáveis** — não é "banco de grafos" (o fundamento-fonte rejeita "banco de dados"; research.md §0) e não é memória de trabalho (SPEC-004). Este Plan define **o QUE** (contrato cognitivo: ontologia, entidades/relações, temporalidade, proveniência por referência, lifecycle, confiança de relação, consulta cognitiva, governança de escrita, imutabilidade append-only), com o **mecanismo físico de armazenamento declarado INDETERMINADO = H-001 (ABERTA)** — grafo real vs. estrutura em memória vs. tabelas+índice é decisão de engenharia de Andraus, não fechada aqui. [FONTE: ROADMAP §6; DHR-SPEC006-001 Q-ABERTURA-3; research.md §0/§8]

**Status epistemológico de cabeçalho:** a SPEC-006 é a **camada Harness/operacional da memória permanente** sobre responsabilidades que os modelos canônicos BASELINED já atribuem ao KG (CEM-001 l.608-615; l.494; l.562-565 Cognitive Trace Reconstruction; CONSTITUTION l.233 EC-COG-003; SAS-001 §6.12; CEE-001 l.111). **NÃO redefine** CHM-001, CEM-001, CCM-001, nem reabre SPEC-004/SPEC-005 (**CC-02/CONST-01/INV-09**): apenas **armazena, relaciona e consulta** conhecimento permanente sob os contratos canônicos. **H-001** permanece **ABERTA** — este Plan **propõe** o recorte (contrato cognitivo fechável com mecanismo físico INDETERMINADO), não o fecha (decisão de Andraus; CONS-01). [FONTE: ROADMAP §6/§7; atomic-spec §12; DHR-SPEC006-001 §3]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-10-11 | Entrega candidata inicial do Plan (Opção A — camada de memória permanente sobre o conhecimento validado/publicado; mecanismo físico INDETERMINADO = H-001). 13 BASpecs (CKG-001..013) com Classe D/C/H (CC-11); 6 Enforcement Contracts (EC-CKG-001..006; E3 fail-closed na escrita permanente e na proibição de deleção; falso-DENY E3 condicional); 13 EARS; D4 (temporalidade/validade, dedupe de nó/relação, confiança de relação, trace reconstruction); D5 (lifecycle do nó/relação); D6 (protocolo de escrita sobre conhecimento publicado); D7 (≥3 cenários — T01..T11); D8 adversarial focado (ADV-CKG-01..10); D9 por referência. H-001 declarada ABERTA; ontologia enxuta DENTRO da SPEC-006 (Q-ABERTURA-4); 1 Spec (Q-ABERTURA-5). |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; DHR-SPEC006-001 §3/§4; ABERTURA §8/§9; RMR-001]

- **Nenhum item do RMR-001 tem gatilho `spec:SPEC-006` homologado isoladamente.** O início da redação deste Plan **satisfaz ramos de gatilho** de itens pré-existentes — **tratados aqui como reflexo; a promoção/encaminhamento é do gate e de Andraus** (o Especificador NÃO promove — CONS-01).
- **BL-003** (persistência física de hipótese/estado) — `Em espera`, gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação`. A redação deste Plan **satisfaz** o ramo `spec:SPEC-006`. **Encaminhamento:** a parte **física** do BL-003 **É** H-001 (ABERTA) / G-001 (ABERTA) → a SPEC-006 **referencia**, **não absorve nem fecha**. Precedente SPEC-004: "em redação" lido como disparo no início do Plan (DHR-SPEC004-001) — registro e deixo a promoção a Andraus/Controlador (fail-closed).
- **BL-011** (MC-EXP-001, Master Contract da Camada de Experiência e Memória) — `Em espera`, gatilho inclui `spec:SPEC-006 em redação`. **Fonte de requisitos** de SPEC-004/006/009/018. **Encaminhamento:** usar como **insumo de requisitos** (ref. externa K-MAN-15) sob os tratamentos COL-EXP-01..05 já homologados (CONFLICT-MAP; prevalece SOT canônico; imutabilidade REFORÇA RULE-BB-004/INV-07). Classificação ≠ aplicação; **não promovo**.
- **BL-010** (MC-RAG-001) — `Em espera`, gatilho `spec:SPEC-007 em redação` ∨ `milestone:FASE 3 iniciada`. A FASE 3 é iniciada, mas BL-010 é fonte de requisitos da **SPEC-007** (não da 006) → **tangente**; a SPEC-006 respeita a fronteira (recebe conhecimento publicado; formação/retrieval é SPEC-007). **Não promovo** (gate/Andraus decidem o ramo `milestone`).
- **BL-029** (proveniência/falso-DENY — SPEC-004) permanece `ATIVADO`/pré-existente, **independente** desta Spec — não absorvido nem promovido aqui.
- O passo 11-bis pleno ocorre na homologação do Plan.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o Knowledge Graph é **infraestrutura de memória agnóstica de escola** — **armazena** conhecimento de qualquer camada analítica (inclusive a relação `HERDA`/hierárquica entre graus) **sem** alterar a hierarquia nem a autoridade de criação de hipótese (Elliott cria a primária; ICT não cria — INV-01/INV-02). O KG representa a hierarquia como relações; não a redefine, não interpreta, não decide. [FONTE: INV-01/INV-02; ROADMAP §6]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM) nem SPEC-004/005:** **foco.** O KG **preserva** linhagem/versões/estados e faz *Cognitive Trace Reconstruction* **referenciando** os contratos canônicos (CEM-001 l.608-615; l.562-565) — entidades são **referenciadas por ID+versão, nunca redefinidas**. Não reabre a memória de trabalho (SPEC-004, BASELINE) nem o transporte (SPEC-005, BASELINE); recebe conhecimento **permanente** já publicado. CDM-001/CNM-001 pendentes não acionam CONST-01. [FONTE: CC-02; CEM-001 l.608-615; CHM-001; CCM-001; SPEC-004/005 BASELINE]
- [x] **CC-03 — Conviction Vector:** o KG **não computa** convicção — a **"confiança de relação"** do KG é escala própria da memória e **NÃO é** o Conviction Vector; dimensionalidade=8 (fechada) intocada; a fórmula/pesos/limiares definitivos do Conviction Vector permanecem **pendentes (J-001 ABERTA)** e **não** são tratados aqui; **nenhum limiar numérico de convicção é declarado neste Plan**. [FONTE: INV-03; J-001 ABERTA; N-001 ABERTA]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. O KG não emite sinal de trading, não dimensiona risco, não aplica gates de sinal. **INV-04** (custo nunca entra no Conviction Vector — Convicção ≠ Score) preservado por construção: a confiança de relação do KG **nunca** retroalimenta nem redefine o Conviction Vector, e custo/score nunca entram em convicção (CKG-007; ADV-CKG-05). [FONTE: CEE-001 §10/§11; INV-04]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D7 + D8 adversarial focado (ROADMAP §6; atomic-spec §3 emenda SPEC006-MATRIZ; DHR-SPEC006-001 Q-ABERTURA-2).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card; §59/§60 tornam-se obrigatórios nas Tasks/Cards (BUILD adiado — atomic-spec §14). Omissão justificada.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem: ROADMAP §6 → Dossiê (research.md, HOMOLOGADO DHR-SPEC006-001) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED com ID+versão (RULE-HD-04); REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Mapa de cobertura×lacuna (canônicos/SPEC-004) com arquivo:linha incluído. Eixo VERTICAL (RULE-HV) avaliado e declarado não aplicável. [FONTE: EUA-E04 §8.3; RULE-HD-02/03/04]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI):** aplicado — **mecanismo físico do KG = INDETERMINADO (H-001 ABERTA)**, não como fato; **relações causais exigem mecanismo declarado (RULE-CAU-01), nunca correlação pós-hoc** (CKG-008; ADV-CKG-06); **sem falsa precisão em "confiança de relação"** (escala sem número arbitrário até calibração); fontes web = DADO [EXTERNO] (research.md §2). [FONTE: RULE-EPI-01..03; RULE-CAU-01; research.md §8]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM-01):** **INCIDE e tratado** (ver "Declaração de acepção semântica"): **"Conhecimento permanente"** (KG) vs **"memória de trabalho"** (Blackboard/SPEC-004) vs **"documento recuperado"** (RAG/SPEC-007) vs **"Observação"** (Skill — INV-06); **"confiança de relação"** (KG, escala própria) vs **"Convicção"** (CCM-001); **"esquecimento"** (= arquivamento versionado sob governança, nunca deleção — INV-07). Nenhum termo canônico do GLOSSARIO redefinido (RULE-SEM-04). [FONTE: RULE-SEM-01/04; INV-06; GLOSSARIO]
- [x] **CC-11 — Classe/Mecanismo por BASpec com efeito (RULE-MECH-01):** **INCIDE** — a SPEC-006 cita RULE-MECH-01 e é "SPEC-002 em diante". Cada BASpec com efeito declara Classe (D/C/H) com critério 4Es; Classes C/H declaram gate de saída determinístico; Classe H declara bounded loop + critério de parada (CKG-008). Declaração por BASpec, nunca por Spec inteira (SES-001 §50). Ver §D3. [FONTE: RULE-MECH-01..04; atomic-spec §9/§10.6]
- [x] **CC-12 — Princípios de Domínio `PD-xx` (RULE-PD-01):** **N/A — não incide** (DHR-SPEC006-001 §2; ABERTURA §6; research.md §7). O KG é **infraestrutura de memória agnóstica de escola** — não define escopo de especialidade (Elliott/SMC/ICT). Mesmo padrão N/A de SPEC-002/004/005. Registrado explicitamente, não supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7; DHR-SPEC006-001 §2]

**Disciplinas cognitivas N8–N17 incidentes (RULES.md v1.5):** RULE-EPI (H-001 ABERTA ≠ fato; mecanismo físico INDETERMINADO), RULE-CAU-01 (relação causal exige mecanismo declarado — CKG-008; não pós-hoc), RULE-MET-01 (não-fabricação — nenhuma escala/limiar de confiança fabricado; IDs arXiv implausíveis descartados, research.md §aviso), RULE-UNC-01..03 (incerteza localizada sobre consulta multi-salto antes de H-001 fechada), RULE-SEM-01/04 (acepções "conhecimento permanente" vs "trabalho"; "confiança" vs "Convicção"; termos canônicos não redefinidos), RULE-DEC-01 (o KG **armazena/relaciona/consulta**, não decide nem executa — INV-05). INDETERMINADO usado onde há incerteza material.

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-006

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - canon/CEM-001 (BASELINE) — Responsabilidades do Knowledge Graph (l.608-615): preservar toda a linhagem;
    preservar todas as versões; preservar todos os estados; fornecer Cognitive Trace Reconstruction completa a
    partir das relações de Lineage; permitir navegação completa da cadeia cognitiva. Também: l.494 ("Knowledge
    Graph | Todos os estados — preservação permanente"); l.562-565 (Cognitive Trace Reconstruction = capacidade
    do KG, reconstrói navegando as relações de Lineage); l.699 (KG = mecanismo oficial de Cognitive Trace
    Reconstruction do ecossistema). O KG CUMPRE essas responsabilidades; NÃO redefine o CEM (CC-02/INV-10)
  - canon/CHM-001 (BASELINE) — máquina de estados da hipótese (EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→
    REFUTED→ARCHIVED) e versionamento append-only; o KG ARMAZENA/relaciona hipóteses como nós por
    referência, preservando seus estados; NÃO cria nem transiciona estado de hipótese (isso é SPEC-001/CHM-001)
  - canon/CCM-001 (BASELINE) — objeto Conviction Vector 8D; o KG pode armazenar o valor como propriedade de nó
    (por referência), mas a "confiança de relação" do KG é escala PRÓPRIA e NUNCA é o Conviction Vector (INV-04)
  - specs/features/SPEC-004 v1.2 (BASELINE — DHR-SPEC004-003) — memória de TRABALHO (Blackboard), log append-only,
    estados ACTIVE, proveniência (gate_id/identidade autenticada — BL-029), supersessão. FRONTEIRA: o KG é memória
    PERMANENTE, distinta e separada ("Nunca misturar"); reusa a proveniência/identidade autenticada por referência,
    NÃO redefine o contrato de objeto (CC-02/INV-09)
  - specs/features/SPEC-005 v1.0 (BASELINE — DHR-SPEC005-002) — notificação de mudança (Event Bus); o KG CONSOME
    eventos de ciclo de vida (ex.: "Evidence Invalidated" — CEM-001 l.600/l.717-727) para atualizar relações, e
    pode EMITIR eventos de mudança de conhecimento; NÃO redefine o transporte
  - canon/CEE-001 (BASELINE) l.111 — a métrica de calibração do roteamento de modelo "entra no Knowledge Graph";
    o KG ARMAZENA essa métrica como nó/relação (por referência), não a computa
  - canon/SAS-001 §6.12 (l.923-924) — Integração com Knowledge Graph: o agente atua EXCLUSIVAMENTE como PRODUTOR;
    pode registrar relações fractais/temporais/estruturais/de causalidade estrutural; NÃO pode redefinir ontologias
    nem alterar taxonomias globais. Esta fronteira FUNDAMENTA a governança de escrita do KG (CKG-009); SAS-001 §6.12
    é herdado como fronteira, não redefinido. (l.163 EC-COG-003: KG "consultado quando necessário… não é pré-requisito
    obrigatório" — a consulta cognitiva é opcional, não bloqueante)
  - governance/CONSTITUTION.md l.233 (EC-COG-003 — "Knowledge Graph | Memória relacional de padrões"): âncora
    constitucional; conformar-se, não reescrever (INV-09)
  - governance/RULES.md: RULE-BB-004 (append-only; objetos SUPERSEDED, nunca deletados — l.323) — REFORÇADO pelo
    KG como imutabilidade permanente (INV-07); RULE-CAU-01 (afirmação causal é hipótese e DEVE declarar o
    mecanismo — l.680) — incide sobre as relações causais do KG (CKG-008)
  - Método: atomic-spec.md v1.5 (BASpec, D0–D9, EARS, Enforcement E0–E3/F.1–F.4, TRACE-06, Quality Gates L1–L4 §7,
    Classe/Mecanismo §10.6, RULE-MM; §3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7)
  - Governança/Avaliação/Maturidade: SPEC-019 v1.0 (RULE-HG-01..08, RULE-HV-01..04); SPEC-020 v1.0 (9 lentes/
    RULE-EV-01..07); SPEC-021 v1.0 (RULE-MM-01..07; nível-alvo L3; gate E3 RULE-MM-05)
  - Enforcement: ENF-01..08 (ênfase ENF-03 Detector≠Gate; ENF-04 fail-closed; ENF-07 falso-DENY no E3)
  - Invariantes: INV-04 (custo/confiança nunca no Conviction Vector), INV-05 (SOT não executa ordem), INV-06
    (Evidência≠Observação), INV-07 (versionamento monotônico — refutado/arquivado NUNCA deletado), INV-09 (sem
    baseline informal), INV-10 (CEM-001 idioma canônico da Evidência)
  - Setup operacional (fronteira soberana, NÃO redefinida): WORKFLOW.md (versão vigente) — o KG é a memória de longo
    prazo consultada na formação de contexto; a SPEC-006 cita por ID os WF-xx que eventualmente toque, NÃO contradiz
    nenhum WF-xx e NÃO fecha WF-D03 (não computa convicção)

ADDED (delta local — o que esta spec acrescenta; NÃO coberto pelos canônicos/SPEC-004/005 — ver "Cobertura × lacuna"):
  - Ontologia ENXUTA do KG (DENTRO da SPEC-006 — Q-ABERTURA-4): tipos de ENTIDADE (nó) e tipos de RELAÇÃO permitidos
    + regras de integridade (a "gramática do conhecimento"); rejeita tipo não-permitido (gate de integridade)
  - Catálogo de ENTIDADES (nós) por referência aos canônicos: hipóteses, evidências, narrativas, missões,
    aprendizados, ativos, timeframes, regimes, estruturas (Elliott/Fibonacci/SMC/ICT), métricas de calibração
  - Catálogo de RELAÇÕES tipadas: CONFIRMA, REFUTA, DEPENDE_DE, HERDA, PERTENCE_A, INVALIDA, ORIGINA, SIMILAR_A,
    CAUSA (sob RULE-CAU), HIERARQUIA_DE, ESTATISTICA_DE, de hipótese/evidência/missão/aprendizado
  - TEMPORALIDADE / validade no tempo das relações (quando passou a / deixou de valer) — invalidar≠deletar
  - PROVENIÊNCIA obrigatória por entidade/relação (quem/quando/por quê/de onde) por REFERÊNCIA a CEM-001 Lineage/
    gate_record e SPEC-004; rejeita escrita sem proveniência
  - IMUTABILIDADE / append-only permanente: "esquecimento" = arquivamento/rebaixamento versionado, NUNCA deleção (INV-07)
  - CONFIANÇA de relação — escala PRÓPRIA do KG, explicitamente ≠ Convicção (INV-04); nunca retroalimenta o Conviction Vector
  - Relações de SIMILARIDADE/CAUSALIDADE com juízo + gate de saída (mecanismo declarado — RULE-CAU; não pós-hoc)
  - GOVERNANÇA de escrita: quem escreve, com que gate (E2/E3), identidade autenticada (reusa SPEC-004), produtor
    registra relações mas NÃO redefine ontologia/taxonomia (SAS-001 §6.12)
  - FRONTEIRA de entrada: o KG recebe conhecimento JÁ PUBLICADO/validado (SPEC-007); não faz formação/retrieval
  - CONSULTA cognitiva (read-only): padrão/similaridade/causalidade/histórico/multi-salto; Cognitive Trace Reconstruction
  - LIFECYCLE do nó/relação (ACTIVE_KNOWLEDGE / SUPERSEDED / ARCHIVED; transições versionadas sob governança)
  - DETECÇÃO e registro de COLISÃO/contradição de relações (não resolve em silêncio; versiona — alvo D8)
  - Declaração de Classe/Mecanismo por BASpec (CC-11); Enforcement Contracts (EC-CKG-001..006)
  - [PROPOSTA de recorte] contrato cognitivo FECHÁVEL com mecanismo físico INDETERMINADO — NÃO fecha H-001 (decisão de Andraus)

MODIFIED (especialização de regra herdada):
  - RULE-BB-004 (append-only do Blackboard) é REFORÇADA, não alterada, como imutabilidade PERMANENTE do KG
    (INV-07) — eixo de memória permanente, não de trabalho; texto/significado inalterados (RULE-HD-02 respeitada)

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal / obrigação-a-
> obrigação** sobre **modelos canônicos (CEM/CHM/CCM/CEE/SAS), as SPEC-004/005 vizinhas e regras (RULE-BB-004/CAU)**
> (EUA-E04 §8.3). O eixo **VERTICAL** (RULE-HV-01..04, conservação-como-conjunto pai→filha macro-harness) foi avaliado e
> **não se aplica**: a SPEC-006 não é decomposição *micro* de uma *macro-spec* — deriva de canônicos, das Specs vizinhas
> e de regras. A regra ESCRITA de conservação-como-conjunto vertical será redigida junto da SPEC-019/derivadas
> (EUA-E17 Q1, escopo já homologado); aqui não é invocada. [INFERÊNCIA — a confirmar pelo Revisor]

### Cobertura × lacuna (canônicos / SPEC-004 / SPEC-005) — não duplicar (CC-02/INV-09)

| Capacidade | Coberta por canônico/Spec BASELINED? (arquivo:linha) | Tratamento na SPEC-006 |
|---|---|---|
| Preservar linhagem/versões/estados; Cognitive Trace Reconstruction | **SIM (como responsabilidade atribuída ao KG)** — CEM-001 l.608-615; l.562-565 | **ESPECIFICAR** como comportamento verificável do KG (CKG-011); referencia CEM, não redefine |
| Máquina de estados da hipótese | **SIM** — CHM-001 (EMERGENT→…→ARCHIVED) | **HERDADA** — o KG armazena por referência; não cria/transiciona estado de hipótese |
| Memória de TRABALHO / objetos ACTIVE / log append-only | **SIM** — SPEC-004 v1.2 | **FRONTEIRA** — não reabrir (CC-02/INV-09); o KG recebe conhecimento PERMANENTE |
| Notificação/transporte de mudança | **SIM** — SPEC-005 v1.0 | **FRONTEIRA** — o KG consome/emite eventos de ciclo de vida; não redefine o transporte |
| Proveniência (quem/quando/por quê) | **SIM** — CEM-001 Lineage; SPEC-004 v1.2 (gate_id/identidade) | **REFERÊNCIA obrigatória** por entidade/relação (CKG-005); não redefine o contrato |
| Append-only / nunca deletar | **SIM (princípio)** — RULE-BB-004; INV-07 | **REFORÇADO** como imutabilidade PERMANENTE do KG (CKG-006) |
| **Ontologia (tipos/relações permitidas) + integridade** | **NÃO** (canônicos definem objetos, não a gramática do grafo) | **LACUNA CENTRAL — ADDED** (CKG-001) |
| **Catálogo de entidades e relações tipadas** | **NÃO** (ENGENHARIA-GERAL é fundamento histórico, não baseline) | **LACUNA CENTRAL — ADDED** (CKG-002/003) |
| **Temporalidade / validade no tempo das relações** | **Parcial** (CHM/CEM têm estados; não "validade" de relação) | **LACUNA — ADDED** (CKG-004) |
| **Confiança de relação (≠ Convicção)** | **NÃO** (confidence de evidência ≠ confiança de relação) | **LACUNA — ADDED** (CKG-007; INV-04) |
| **Similaridade / causalidade / hierarquia (sob RULE-CAU)** | **Parcial** — RULE-CAU-01 exige mecanismo | **LACUNA — ADDED** (CKG-008) |
| **Consulta cognitiva** | **NÃO** (SAS-001 §6.12 diz "consulta quando necessário", não especifica o contrato) | **LACUNA — ADDED** (CKG-011) |
| **Governança de escrita no KG permanente** | **Parcial** — SAS-001 §6.12 (produtor; não redefine ontologia); RULE-BB-* | **LACUNA — ADDED** (CKG-009; gate E3) |
| **Lifecycle do nó/relação do KG** | **Parcial** (estados de objeto) | **LACUNA — ADDED** (CKG-012) |
| **Mecanismo físico de armazenamento** | **NÃO — H-001 ABERTA** | **NÃO fechar** — decisão de Andraus (INDETERMINADO) |

---

## Declaração de acepção semântica (RULE-SEM-01 — CC-10)

> **Termo 1:** "Conhecimento permanente" (KG — SPEC-006) = conhecimento **já validado/publicado** e suas relações
> auditáveis, preservado para sempre. **≠ "memória de trabalho"** (Blackboard — SPEC-004) = objetos vivos/mutáveis
> da análise em curso. *"Nunca misturar."* O KG recebe o que já foi consolidado; não guarda rascunho de trabalho.
> **Termo 2:** "confiança de relação" (KG) = escala PRÓPRIA da memória que qualifica quão suportada é uma relação.
> **≠ "Convicção"** (Conviction Vector 8D — CCM-001). A confiança de relação **NUNCA** entra, soma ou retroalimenta o
> Conviction Vector (INV-04); custo/score nunca entram em convicção.
> **Termo 3:** "esquecimento"/"forgetting" (estado da arte — research.md §3.6) no KG = **arquivamento/rebaixamento
> versionado sob governança**, **NUNCA deleção** (INV-07; RULE-BB-004). O KG não apaga.
> **Termo 4:** "documento recuperado" (RAG — SPEC-007) ≠ "conhecimento validado" (KG). O KG não armazena trechos
> recuperados; armazena conhecimento **publicado**. **"Observação"** (Skill — INV-06) ≠ "Evidência" (Agente): o KG
> relaciona ambos como nós, sem confundi-los.
> [FONTE: RULE-SEM-01/04; INV-04/06/07; GLOSSARIO; KERNEL-V2 (research.md §0); SPEC-004/005/007]

---

## Conformidade com o `WORKFLOW.md` (RULE-ECC-05 — determinação de NÃO-incidência)

> **Determinação: RULE-ECC-05 (Pesquisa Multi-Lente) NÃO INCIDE sobre a SPEC-006** [FONTE: DHR-SPEC006-001 §2;
> ABERTURA §1/§6; research.md §7]. Fundamento: a SPEC-006 **não define nem toca comportamento de agente analítico,
> do Conviction/Fusion Engine, do Manager (decisão) ou do Risk Agent** — é **infraestrutura de memória** (armazena/
> relaciona/consulta conhecimento permanente já validado), análoga às Specs de meta-harness/infra excluídas
> (SPEC-002/004/005/019/020/021). **Mesmo não incidindo, por prudência confirma-se conformidade:** o KG é a memória de
> longo prazo **consultada quando necessário** pelos agentes (SAS-001 §6.12/l.163 EC-COG-003 — "não é pré-requisito
> obrigatório"), na formação de contexto. A SPEC-006 **cita por ID** os `WF-xx` que eventualmente toque no Plan,
> **não contradiz** nenhum `WF-xx` e **não fecha** `WF-D03` (não computa convicção/J-001). Autoridade soberana do
> `WORKFLOW.md` preservada; divergência seria achado do Revisor, resolvida por Andraus. [FONTE: research.md §7; SAS-001 §6.12]

---

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide** (DHR-SPEC006-001 §2; ABERTURA §6; research.md §7). O Cognitive Knowledge Graph é **infraestrutura
de memória agnóstica de escola** — armazena conhecimento de qualquer escola (Elliott/SMC/ICT) como nós/relações, sem
definir escopo de especialidade de mercado. Nenhum `PD-xx` é proposto (CC-12 = N/A). Registrado explicitamente para o
Revisor — não é supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7; DHR-SPEC006-001 §2]

---

## D0 — Missão (Intenção)

A SPEC-006 especifica **como o SOT preserva, relaciona e consulta o conhecimento permanente já validado** — definindo
o **contrato cognitivo da memória semântica permanente**: a **ontologia enxuta** (tipos de entidade/relação permitidos
+ regras de integridade), o **catálogo de entidades (nós)** por referência aos canônicos (CHM-001/CEM-001/CCM-001) e de
**relações tipadas** (CONFIRMA/REFUTA/DEPENDE_DE/HERDA/PERTENCE_A/INVALIDA/ORIGINA/SIMILAR_A/CAUSA/HIERARQUIA_DE/
ESTATISTICA_DE), a **temporalidade/validade no tempo** das relações (invalidar≠deletar), a **proveniência obrigatória**
por referência a CEM-001/SPEC-004, a **imutabilidade append-only** ("esquecimento" = arquivamento versionado, nunca
deleção — INV-07), a **confiança de relação** (escala própria, ≠ Convicção — INV-04), as **relações de similaridade/
causalidade** sob mecanismo declarado (RULE-CAU, não pós-hoc), a **governança de escrita** (quem escreve, com que gate
E2/E3, identidade autenticada), a **fronteira de entrada** (só conhecimento publicado — SPEC-007), a **consulta
cognitiva** (padrão/similaridade/causalidade/histórico/multi-salto) e a **Cognitive Trace Reconstruction** (CEM-001
l.608-615) — preservando o princípio **memória permanente ≠ memória de trabalho** e deixando o **mecanismo físico de
armazenamento INDETERMINADO (H-001 ABERTA)**: define-se **o QUE** (contratos, invariantes, garantias observáveis), não
**o COMO** (grafo real vs. estrutura em memória vs. tabelas+índice). [FONTE: ROADMAP §6; CEM-001 l.608-615; CHM-001;
SAS-001 §6.12; DHR-SPEC006-001; research.md §4]

**O que a Missão NÃO é (fronteira):**
- Não é **memória de trabalho** / não guarda objetos ACTIVE vivos → **SPEC-004 (Blackboard, BASELINE)**. *"Nunca misturar."*
- Não **transporta/notifica** mudança → **SPEC-005 (Event Bus, BASELINE)**; o KG consome/emite eventos, não redefine o transporte.
- Não **forma conhecimento** / não faz retrieval / `documento recuperado ≠ conhecimento validado` → **SPEC-007 (RAG/Knowledge Formation)**; o KG recebe conhecimento **publicado**.
- Não define **estado persistente por agente** → **SPEC-009**; **G-001 (ABERTA)** — não tocar.
- Não especifica o **ciclo de evolução do conhecimento (P12)** / backtest de aprendizado → **SPEC-018**; **K-001 (ABERTA)** — não tocar.
- Não **computa** convicção nem fixa fórmula/pesos/limiares → **SPEC-003/CCM-001**; **J-001/N-001 (ABERTAS)** — a confiança de relação NÃO é Convicção (INV-04).
- Não **redefine** CHM-001/CEM-001/CCM-001 nem as SPEC-004/005 → **CC-02/CONST-01/INV-09**.
- Não **escolhe o mecanismo físico de armazenamento** → **H-001 (ABERTA — só Andraus)**; INDETERMINADO.
- Não **decide** nem **executa** ordem → INV-05/RULE-DEC-01.

**Status epistemológico:** a SPEC-006 é FATO ARQUITETURAL candidato a baseline; RULE-CKG-* e o contrato de nó/relação
por ela propostos são **[PROPOSTA]** até homologação. CEM-001, CHM-001, CCM-001, CEE-001, SAS-001, SPEC-004 v1.2,
SPEC-005 v1.0, SPEC-001/019/020/021, RULE-BB-004, RULE-CAU-01, atomic-spec v1.5, INV-*, ENF-* são FATO NORMATIVO.
Fontes externas (research.md §2, SRC-*/REPO-*) são [EXTERNO] — DADO, nunca baseline; documentado ≠ homologado (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | **Ontologia enxuta (gramática do conhecimento):** tipos de entidade e relação permitidos + regras de integridade; rejeita tipo/relação fora da ontologia | KERNEL-V2 (research.md §0/§3.6); DHR-SPEC006-001 Q-ABERTURA-4 |
| S2 | **Entidades (nós) por referência aos canônicos:** hipótese (CHM-001), evidência (CEM-001), convicção (CCM-001), narrativa, missão, aprendizado, ativo, timeframe, regime, estrutura, métrica de calibração (CEE-001 l.111) | CEM-001; CHM-001; CCM-001; CEE-001 l.111 |
| S3 | **Relações tipadas:** CONFIRMA/REFUTA/DEPENDE_DE/HERDA/PERTENCE_A/INVALIDA/ORIGINA/SIMILAR_A/CAUSA/HIERARQUIA_DE/ESTATISTICA_DE + relações de hipótese/evidência/missão/aprendizado | ROADMAP §6; research.md §4 |
| S4 | **Temporalidade / validade das relações:** quando uma relação passou a / deixou de valer; invalidar≠deletar (janela de validade) | research.md §3.1; INV-07 |
| S5 | **Proveniência obrigatória** por entidade/relação (quem/quando/por quê/de onde) por referência a CEM-001 Lineage/gate_record e SPEC-004; rejeita escrita sem proveniência | CEM-001 Cap.5; SPEC-004 v1.2; research.md §3.2 |
| S6 | **Imutabilidade / append-only permanente:** nunca apagar; "esquecimento" = arquivamento/rebaixamento versionado sob governança | INV-07; RULE-BB-004; research.md §3.6 |
| S7 | **Confiança de relação** — escala própria do KG, explicitamente ≠ Convicção; nunca retroalimenta o Conviction Vector | INV-04; research.md §4 |
| S8 | **Relações de similaridade/causalidade** com juízo + gate de saída (mecanismo declarado — RULE-CAU; não pós-hoc) | RULE-CAU-01; research.md §8 |
| S9 | **Governança de escrita:** quem escreve, gate E2/E3, identidade autenticada (reusa SPEC-004); produtor registra relações mas não redefine ontologia/taxonomia | SAS-001 §6.12; RULE-BB-*; SPEC-004 v1.2 |
| S10 | **Fronteira de entrada:** o KG recebe conhecimento **já publicado/validado** (SPEC-007); não faz formação/retrieval | ROADMAP §6/§7; research.md §3.4 |
| S11 | **Consulta cognitiva (read-only):** padrão/similaridade/causalidade/histórico/multi-salto + Cognitive Trace Reconstruction | CEM-001 l.608-615; SAS-001 §6.12; research.md §3.4 |
| S12 | **Lifecycle do nó/relação:** ACTIVE_KNOWLEDGE/SUPERSEDED/ARCHIVED; transições versionadas sob governança, nunca remoção | CHM-001; INV-07; research.md §3.6 |
| S13 | **Detecção/registro de colisão de relações:** relações contraditórias são registradas e versionadas, não resolvidas em silêncio | research.md §8; D8 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| **Mecanismo físico de armazenamento** (grafo real / estrutura em memória / tabelas+índice) | **H-001 (ABERTA — só Andraus)** | decisão de engenharia deliberadamente aberta; INDETERMINADO |
| Memória de trabalho / objetos ACTIVE / log append-only de estado | **SPEC-004 (BASELINE)** | "Nunca misturar"; CC-02/INV-09 |
| Notificação/transporte de mudança | **SPEC-005 (BASELINE)** | o KG consome/emite eventos; não redefine o transporte |
| Formação de conhecimento / retrieval / `documento recuperado ≠ conhecimento validado` | **SPEC-007 (RAG/Knowledge Formation)** | o KG recebe conhecimento publicado |
| Estado persistente por agente | **SPEC-009** — **G-001 (ABERTA)** | persistência por agente |
| Ciclo de evolução do conhecimento (P12) / backtest de aprendizado | **SPEC-018** — **K-001 (ABERTA)** | governança de aprendizado |
| Redefinir CHM-001 / CEM-001 / CCM-001 / SPEC-004 / SPEC-005 | canônicos/baseline | **CC-02/CONST-01/INV-09** — só referenciar/armazenar |
| Fórmula/pesos/limiares de convicção; confiança como convicção | **SPEC-003/CCM-001; J-001/N-001 (ABERTAS)** | INV-03/INV-04; o KG não computa convicção |
| Componente "Cognitive Ontology" separado | — (ontologia DENTRO da SPEC-006) | DHR-SPEC006-001 Q-ABERTURA-4; criar componente é decisão de Andraus (não feita) |
| Escolher tecnologia de banco de grafos | **H-001 (ABERTA)** + fora do mandato do Especificador | Andraus |

---

## D2 — Regras

> **Etiqueta:** as RULE-CKG-* e o contrato de nó/relação abaixo são **[PROPOSTA]** — tornam-se normativos apenas na
> homologação de Andraus + registro pelo Controlador (RULE-HG-02). As RULE/INV/ENF citadas como fundamento
> (CEM-001 l.608-615, CHM-001, CCM-001, RULE-BB-004, RULE-CAU-01, INV-04/05/06/07/09/10, ENF-03/04/07, SAS-001 §6.12)
> **já existem** e são FATO NORMATIVO.

```
RULE-CKG-001: Todo nó e toda relação escritos no KG DEVEM pertencer à ONTOLOGIA permitida (tipo de entidade ∈ catálogo
              de entidades; tipo de relação ∈ catálogo de relações) e satisfazer as regras de integridade da ontologia
              (ex.: HERDA só entre nós da mesma família estrutural; CAUSA exige mecanismo — RULE-CKG-008). Nó/relação
              de tipo não-permitido é REJEITADO (fail-closed), não escrito. A ontologia é ENXUTA e vive DENTRO da
              SPEC-006 (não é componente separado).
              [Fonte: KERNEL-V2 (research.md §0/§3.6); DHR-SPEC006-001 Q-ABERTURA-4]  [PROPOSTA]

RULE-CKG-002: Toda ENTIDADE (nó) do KG que corresponde a um objeto canônico (hipótese/CHM-001, evidência/CEM-001,
              convicção/CCM-001) DEVE referenciá-lo por ID+versão — NUNCA redefinir seu contrato, campos ou máquina de
              estados (CC-02/INV-10). O KG armazena/relaciona por referência; o objeto canônico é a fonte do seu próprio
              contrato.
              [Fonte: CEM-001; CHM-001; CCM-001; CC-02; INV-10]  [PROPOSTA]

RULE-CKG-003: Toda RELAÇÃO do KG DEVE ser tipada (um tipo do catálogo), direcionada (origem→destino) e carregar
              proveniência (RULE-CKG-005). Relações contraditórias entre os mesmos nós NÃO são resolvidas em silêncio:
              são REGISTRADAS e versionadas (RULE-CKG-013); o KG preserva a contradição para auditoria.
              [Fonte: ROADMAP §6; research.md §4/§8; INV-07]  [PROPOSTA]

RULE-CKG-004: Toda relação DEVE suportar TEMPORALIDADE/validade no tempo (quando passou a valer; quando deixou de valer).
              Quando a informação muda, a relação antiga é INVALIDADA (marca de fim de validade), NUNCA deletada; a
              consulta pode perguntar "o que é verdade agora" ou "o que era verdade em T". Invalidar ≠ deletar (INV-07).
              [Fonte: research.md §3.1; INV-07; CEM-001 l.602 (invalidação não implica remoção)]  [PROPOSTA]

RULE-CKG-005: Nenhuma entidade ou relação pode existir no KG sem PROVENIÊNCIA — quem a produziu, quando, por quê e de
              onde — por REFERÊNCIA a CEM-001 Lineage/gate_record e à proveniência da SPEC-004 (gate_id/identidade
              autenticada). Escrita sem proveniência é REJEITADA (fail-closed). A proveniência referencia os contratos
              canônicos; NÃO os redefine (CC-02).
              [Fonte: CEM-001 Cap.5; SPEC-004 v1.2; research.md §3.2]  [PROPOSTA]

RULE-CKG-006: O KG é APPEND-ONLY PERMANENTE (INV-07; reforça RULE-BB-004 no eixo permanente): nenhum nó/relação é
              DELETADO. "Esquecimento"/consolidação = ARQUIVAMENTO ou rebaixamento de relevância VERSIONADO sob
              governança (lifecycle — RULE-CKG-012), nunca remoção. Toda transição preserva a versão anterior e é
              reconstruível (P13).
              [Fonte: INV-07; RULE-BB-004 (RULES.md l.323); research.md §3.6]  [PROPOSTA]

RULE-CKG-007: A CONFIANÇA de uma relação é escala PRÓPRIA do KG e NÃO É a Convicção (Conviction Vector 8D — CCM-001).
              A confiança de relação NUNCA entra, soma ou retroalimenta o Conviction Vector; custo/score NUNCA entram em
              convicção (INV-04). Nenhum limiar numérico de convicção é fixado neste Plan; a escala de confiança de
              relação é PARÂMETRO a calibrar ([DECISÃO NECESSÁRIA]/INDETERMINADO — sem número arbitrário; não toca
              J-001/N-001).
              [Fonte: INV-04; CCM-001; RULE-MET-01; research.md §4]  [PROPOSTA]

RULE-CKG-008: Toda relação CAUSAL (CAUSA) DEVE declarar o MECANISMO que a sustenta (como a origem produz o destino),
              além de condições e direção — correlação/precedência/padrão histórico NÃO bastam (RULE-CAU-01). Relação
              causal sem mecanismo declarado é REJEITADA (não pós-hoc). O juízo de similaridade/causalidade que PROPÕE
              uma relação é Classe H: tem bounded loop (critério de parada explícito) + gate de saída determinístico
              que verifica a presença do mecanismo antes de escrever.
              [Fonte: RULE-CAU-01 (RULES.md l.680); research.md §8]  [PROPOSTA]

RULE-CKG-009: A escrita no KG permanente é governada: só ESCRITORES AUTORIZADOS escrevem, com identidade AUTENTICADA
              pelo runtime (reusa SPEC-004 — não define auth nova). O produtor pode registrar relações (fractais/
              temporais/estruturais/causais estruturais) mas NÃO pode redefinir a ONTOLOGIA nem alterar TAXONOMIAS
              globais (SAS-001 §6.12). A escrita em memória permanente é commit de alto valor: piso E2; publicação
              crítica/irreversível no KG = E3 fail-closed.
              [Fonte: SAS-001 §6.12; SPEC-004 RULE-CBP-014 (identidade autenticada); ENF-03/04]  [PROPOSTA]

RULE-CKG-010: O KG recebe conhecimento JÁ PUBLICADO/validado; NÃO faz formação de conhecimento, extração de texto nem
              retrieval (isso é SPEC-007). "Documento recuperado ≠ conhecimento validado ≠ conhecimento publicado": só o
              conhecimento publicado entra como nó/relação. Entrada de conhecimento não-publicado é REJEITADA (fronteira).
              [Fonte: ROADMAP §6/§7; research.md §3.4]  [PROPOSTA]

RULE-CKG-011: O KG DEVE oferecer CONSULTA cognitiva read-only (padrão/similaridade/causalidade/histórico/multi-salto) e
              a Cognitive Trace Reconstruction — reconstrução da cadeia cognitiva completa navegando as relações de
              Lineage (CEM-001 l.608-615; l.562-565). A consulta é opcional/não-bloqueante para a operação do agente
              (SAS-001 §6.12/EC-COG-003) e NÃO altera estado (read-only). O alcance de consulta multi-salto pode ficar
              limitado enquanto H-001 permanecer ABERTA (INDETERMINADO — declarado, não presumido).
              [Fonte: CEM-001 l.608-615; SAS-001 §6.12/l.163; research.md §3.4]  [PROPOSTA]

RULE-CKG-012: Todo nó/relação tem LIFECYCLE versionado — ACTIVE_KNOWLEDGE → SUPERSEDED (substituído por versão nova,
              cadeia preservada) → ARCHIVED (rebaixado sob governança). As transições são versionadas e reconstruíveis;
              NENHUMA transição remove o registro histórico (INV-07). A distinção conhecimento permanente vs. temporário
              é operacionalizada por este lifecycle, não por deleção.
              [Fonte: CHM-001; INV-07; research.md §3.6]  [PROPOSTA]

RULE-CKG-013: Quando duas relações entre os mesmos nós se contradizem (ex.: CONFIRMA × REFUTA), o KG DETECTA e REGISTRA
              a colisão (ambas preservadas, versionadas, com proveniência e validade temporal), NUNCA sobrescreve ou
              apaga uma delas em silêncio. A resolução (qual prevalece) é matéria de conhecimento/validação (SPEC-007/
              SPEC-018) ou de governança — o KG preserva a contradição auditável, não a decide.
              [Fonte: INV-07; research.md §8; fronteira SPEC-007/SPEC-018]  [PROPOSTA]
```

> **Invariante local desta Spec [PROPOSTA]:**
> **INV-CKG-01 (Memória permanente imutável):** nenhum nó/relação do KG é deletado; toda consolidação/"esquecimento" é
> arquivamento versionado sob governança; toda entidade/relação carrega proveniência e é reconstruível. Reforça — não
> redefine — RULE-BB-004 e INV-07, no eixo da memória **permanente**. [PROPOSTA]

---

## Critérios de Aceitação (EARS)

1. Quando um nó ou relação é submetido para escrita, o KG DEVE escrevê-lo somente se seu tipo pertence à ontologia permitida e satisfaz as regras de integridade, e DEVE rejeitar (fail-closed) tipo não-permitido, sem escrever.
2. Quando um nó corresponde a um objeto canônico (hipótese/evidência/convicção), o KG DEVE referenciá-lo por ID+versão e NÃO DEVE redefinir seu contrato, campos ou estados.
3. Quando uma relação é escrita, o KG DEVE exigir tipo, direção e proveniência, e NÃO DEVE aceitar relação sem proveniência.
4. Quando a informação de uma relação muda, o KG DEVE invalidar a relação antiga marcando o fim de sua validade e manter o histórico, e NÃO DEVE deletá-la.
5. Quando qualquer escrita é tentada sem proveniência (quem/quando/por quê/de onde), o KG DEVE rejeitá-la (fail-closed).
6. Quando um "esquecimento"/consolidação é solicitado, o KG DEVE arquivar/rebaixar de forma versionada sob governança, e NÃO DEVE remover o registro histórico.
7. Quando uma confiança de relação é registrada, o KG DEVE mantê-la como escala própria e NÃO DEVE permitir que ela entre, some ou retroalimente o Conviction Vector.
8. Quando uma relação causal é proposta, o KG DEVE exigir o mecanismo declarado (como a origem produz o destino) e DEVE rejeitar relação causal sem mecanismo (não pós-hoc).
9. Quando uma escrita no KG permanente é tentada, o KG DEVE aceitá-la apenas de escritor autorizado com identidade autenticada, e NÃO DEVE permitir que o produtor redefina a ontologia ou taxonomias globais.
10. Quando conhecimento não-publicado é submetido ao KG, o KG DEVE rejeitá-lo (recebe só conhecimento validado/publicado; formação é SPEC-007).
11. Quando um consumidor consulta o KG, o KG DEVE responder read-only (padrão/similaridade/causalidade/histórico/multi-salto) e reconstruir a cadeia cognitiva, e NÃO DEVE alterar estado na consulta.
12. Quando um nó/relação transita de estado (SUPERSEDED/ARCHIVED), o KG DEVE versionar a transição preservando o histórico, e NÃO DEVE remover a versão anterior.
13. Quando duas relações entre os mesmos nós se contradizem, o KG DEVE detectar e registrar a colisão preservando ambas versionadas, e NÃO DEVE sobrescrever ou apagar uma delas em silêncio.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec com efeito declara o bloco **CLASSE/MECANISMO** (§10.6). D = determinístico; C = constitutivo (é o
> próprio gate); H = híbrido (juízo + gate de saída determinístico + bounded loop). A escrita em memória permanente é
> commit de alto valor (piso E2; E3 na publicação crítica/irreversível e na proibição de deleção).

### BASpec-CKG-001 — Ontologia enxuta (rejeita tipo não-permitido)

```
BASpec-CKG-001:
  QUANDO:       Um nó ou relação é submetido para escrita no KG
  ENTÃO:        O KG escreve somente se o tipo de entidade/relação pertence à ontologia permitida e satisfaz as regras
                de integridade; tipo não-permitido é rejeitado (fail-closed), não escrito; a ontologia é enxuta e vive
                DENTRO da SPEC-006 (não é componente separado)
  PORQUE:       Sem gramática enxuta e regras de integridade, a memória permanente acumula conhecimento incoerente
                (research.md §8 R-8)
  REFERÊNCIA:   RULE-CKG-001; KERNEL-V2 (research.md §3.6)
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de conformidade de tipo (tipo ∈ ontologia ∧ integridade satisfeita); rejeita se falhar
    GATE DE SAÍDA: verificação (tipo_entidade/tipo_relacao ∈ catálogo ∧ regras de integridade satisfeitas)
    CRITÉRIO 4Es: Conformidade > Eficácia — coerência da ontologia é inviolável; determinismo garante reprodutibilidade
  VERIFICADO POR:
    DADO        um nó de tipo não-declarado na ontologia submetido para escrita
    QUANDO      o gate de integridade roda
    ENTÃO       escrita rejeitada; nada persistido
    VERIFICAÇÃO node_written == false; rejected_reason == "ONTOLOGY_TYPE_NOT_ALLOWED"
```

### BASpec-CKG-002 — Entidade por referência ao canônico (não redefine)

```
BASpec-CKG-002:
  QUANDO:       Um nó corresponde a um objeto canônico (hipótese/CHM-001, evidência/CEM-001, convicção/CCM-001)
  ENTÃO:        O KG o referencia por ID+versão e NÃO redefine seu contrato, campos nem máquina de estados; armazena/
                relaciona por referência (o objeto canônico é a fonte do seu próprio contrato)
  PORQUE:       Redefinir um canônico baselined viola CC-02/CONST-01; o idioma canônico é do próprio objeto (INV-10)
  REFERÊNCIA:   RULE-CKG-002; CC-02; INV-10
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : armazenamento de referência (ref = canonical_id@version); sem cópia redefinidora do contrato
    CRITÉRIO 4Es: Eficácia — integridade referencial preserva a fonte canônica da verdade
  VERIFICADO POR:
    DADO        um nó-hipótese referenciando CHM-001 por id@version
    QUANDO      o nó é escrito
    ENTÃO       o nó guarda a referência; nenhum campo/estado do CHM-001 é redefinido no KG
    VERIFICAÇÃO canonical_ref_present == true; canonical_contract_redefined == false
```

### BASpec-CKG-003 — Relação tipada, direcionada, com proveniência

```
BASpec-CKG-003:
  QUANDO:       Uma relação entre dois nós é escrita
  ENTÃO:        O KG exige tipo (do catálogo), direção (origem→destino) e proveniência (RULE-CKG-005); relação sem
                esses elementos é rejeitada; relações contraditórias não são resolvidas em silêncio (CKG-013)
  PORQUE:       Relação não-tipada/sem direção/sem proveniência não é auditável nem reconstruível (P13)
  REFERÊNCIA:   RULE-CKG-003/005; research.md §4
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : validação determinística de (tipo ∈ catálogo ∧ direção presente ∧ proveniência presente)
    CRITÉRIO 4Es: Eficácia — relações auditáveis e navegáveis
  VERIFICADO POR:
    DADO        uma relação sem tipo do catálogo submetida
    QUANDO      a validação roda
    ENTÃO       relação rejeitada; nada escrito
    VERIFICAÇÃO relation_written == false; rejected_reason == "RELATION_TYPE_INVALID"
```

### BASpec-CKG-004 — Temporalidade / validade (invalidar ≠ deletar)

```
BASpec-CKG-004:
  QUANDO:       A informação de uma relação muda (ex.: uma hipótese passa a REFUTED e sua relação CONFIRMA deixa de valer)
  ENTÃO:        O KG INVALIDA a relação antiga marcando o fim de sua validade temporal e preserva o histórico; NÃO a
                deleta; a consulta pode perguntar "o que é verdade agora" ou "o que era verdade em T"
  PORQUE:       Invalidar≠deletar preserva a reconstrução histórica (INV-07) e a validade bitemporal do conhecimento
  REFERÊNCIA:   RULE-CKG-004; INV-07; CEM-001 l.602
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : escrita de marca de fim de validade (valid_to) + preservação da versão anterior; consulta por janela temporal
    CRITÉRIO 4Es: Eficácia — nenhuma verdade histórica perdida
  VERIFICADO POR:
    DADO        uma relação válida desde T0 cuja informação muda em T1
    QUANDO      a atualização é processada
    ENTÃO       relação antiga marcada valid_to=T1 (preservada); consulta "em T0" ainda a retorna; consulta "agora" não
    VERIFICAÇÃO old_relation_deleted == false; valid_to_set == true; historical_query_consistent == true
```

### BASpec-CKG-005 — Proveniência obrigatória (rejeita escrita sem proveniência)

```
BASpec-CKG-005:
  QUANDO:       Qualquer nó/relação é escrito no KG
  ENTÃO:        O KG exige proveniência (quem/quando/por quê/de onde) por referência a CEM-001 Lineage/gate_record e à
                proveniência da SPEC-004; escrita sem proveniência é rejeitada (fail-closed)
  PORQUE:       Conhecimento sem origem não é confiável nem reconstruível (CEM-001 Cap.5; P13)
  REFERÊNCIA:   RULE-CKG-005; CEM-001 Cap.5; SPEC-004 v1.2
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que verifica presença de proveniência referenciada antes de persistir
    GATE DE SAÍDA: verificação (provenance_ref presente ∧ aponta a CEM-001/SPEC-004)
    CRITÉRIO 4Es: Conformidade > Eficácia — proveniência é inviolável para auditabilidade
  VERIFICADO POR:
    DADO        um nó submetido sem provenance_ref
    QUANDO      o gate de escrita roda
    ENTÃO       escrita rejeitada; nada persistido
    VERIFICAÇÃO written == false; rejected_reason == "PROVENANCE_MISSING"
```

### BASpec-CKG-006 — Imutabilidade / append-only permanente (nunca deletar) [INV-CKG-01]

```
BASpec-CKG-006:
  QUANDO:       Uma operação de deleção de nó/relação é tentada (inclusive disfarçada de "esquecimento")
  ENTÃO:        O KG recusa a deleção (fail-closed); "esquecimento"/consolidação só pode ser arquivamento/rebaixamento
                VERSIONADO sob governança (CKG-012); o registro histórico é sempre preservado (INV-07)
  PORQUE:       A memória permanente nunca apaga — deleção quebraria a reconstrução cognitiva (P13) e INV-07/RULE-BB-004
  REFERÊNCIA:   RULE-CKG-006; INV-07; RULE-BB-004
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que proíbe DELETE; só permite transição de lifecycle versionada (arquivar/rebaixar)
    GATE DE SAÍDA: verificação (operação ≠ DELETE física; histórico preservado após a operação)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda de histórico acima de qualquer economia de espaço
  VERIFICADO POR:
    DADO        uma tentativa de deletar fisicamente um nó arquivado
    QUANDO      o gate roda
    ENTÃO       deleção negada (fail-closed); nó permanece arquivado e reconstruível
    VERIFICAÇÃO physical_delete == false; history_preserved == true
```

### BASpec-CKG-007 — Confiança de relação ≠ Convicção (INV-04)

```
BASpec-CKG-007:
  QUANDO:       Uma confiança de relação é registrada ou lida
  ENTÃO:        O KG a mantém como escala PRÓPRIA da memória e impede que ela entre, some ou retroalimente o Conviction
                Vector 8D (CCM-001); custo/score nunca entram em convicção; nenhum limiar numérico de convicção é fixado
  PORQUE:       Convicção ≠ Score (INV-04); misturar confiança de relação com convicção corromperia o Conviction Vector
  REFERÊNCIA:   RULE-CKG-007; INV-04; CCM-001
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que isola o campo de confiança de relação de qualquer entrada do Conviction Vector
    GATE DE SAÍDA: verificação (confiança de relação NÃO é insumo de cálculo de convicção; namespaces separados)
    CRITÉRIO 4Es: Conformidade > Eficácia — INV-04 é inviolável
  VERIFICADO POR:
    DADO        uma relação com confiança registrada e um cálculo de Conviction Vector no mesmo ciclo
    QUANDO      o cálculo de convicção roda (fora do KG)
    ENTÃO       a confiança de relação NÃO é usada como dimensão/insumo do Conviction Vector
    VERIFICAÇÃO relation_confidence_in_conviction == false
```

### BASpec-CKG-008 — Relação causal exige mecanismo (RULE-CAU; não pós-hoc)

```
BASpec-CKG-008:
  QUANDO:       Um juízo propõe uma relação causal (CAUSA) ou de similaridade entre nós
  ENTÃO:        O KG exige, para CAUSA, o MECANISMO declarado (como a origem produz o destino), condições e direção;
                relação causal sem mecanismo é rejeitada (não pós-hoc); o juízo que propõe a relação opera com bounded
                loop (critério de parada) e passa por gate de saída determinístico que verifica a presença do mecanismo
  PORQUE:       Correlação/precedência/padrão histórico não bastam para causalidade (RULE-CAU-01); causal pós-hoc é viés
  REFERÊNCIA:   RULE-CKG-008; RULE-CAU-01
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : juízo (pode usar apoio semântico) PROPÕE a relação; gate de saída determinístico verifica mecanismo+direção
    BOUNDED LOOP: nº máximo de tentativas de proposta por par de nós; sem retry infinito — parada explícita
    GATE DE SAÍDA: verificação determinística (relação CAUSA ⇒ mechanism_declared ∧ direction ∧ conditions presentes)
    CRITÉRIO 4Es: Eficácia (causalidade válida) > Eficiência; o LLM é detector, nunca o gate (ENF-03)
  VERIFICADO POR:
    DADO        uma relação CAUSA proposta sem mechanism declarado (só correlação)
    QUANDO      o gate de saída roda
    ENTÃO       relação rejeitada (não escrita); exige mecanismo
    VERIFICAÇÃO causal_written == false; rejected_reason == "CAUSAL_MECHANISM_MISSING"
```

### BASpec-CKG-009 — Governança de escrita (autorizado + autenticado; não redefine ontologia) [E3]

```
BASpec-CKG-009:
  QUANDO:       Uma escrita no KG permanente é tentada
  ENTÃO:        O KG aceita apenas de escritor AUTORIZADO com identidade AUTENTICADA pelo runtime (reusa SPEC-004); o
                produtor pode registrar relações mas NÃO pode redefinir a ontologia nem alterar taxonomias globais
                (SAS-001 §6.12); publicação crítica/irreversível no KG é E3 fail-closed
  PORQUE:       Escrita em memória permanente é commit de alto valor/irreversível; autorização não pode depender do payload
  REFERÊNCIA:   RULE-CKG-009; SAS-001 §6.12; SPEC-004 RULE-CBP-014; ENF-03/04
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico de autorização por identidade autenticada + escopo (registrar ≠ redefinir ontologia); LLM não é gate
    GATE DE SAÍDA: verificação (escritor ∈ autorizados ∧ identidade autenticada ∧ operação ∉ {redefinir ontologia/taxonomia})
    CRITÉRIO 4Es: Conformidade > Eficácia — escrita permanente só sob autorização é inviolável (ENF-04)
  VERIFICADO POR:
    DADO        um produtor autenticado tentando alterar a ontologia global (não só registrar relação)
    QUANDO      o gate E3 roda
    ENTÃO       operação negada (fail-closed); registrar relação seria permitido; redefinir ontologia não; falso-DENY amostrado (ENF-07)
    VERIFICAÇÃO ontology_redefined_by_producer == false; fail_closed == true
```

### BASpec-CKG-010 — Fronteira: só conhecimento publicado (não forma conhecimento)

```
BASpec-CKG-010:
  QUANDO:       Conhecimento é submetido ao KG
  ENTÃO:        O KG aceita apenas conhecimento JÁ PUBLICADO/validado (SPEC-007); conhecimento não-publicado (documento
                recuperado, candidato não validado) é rejeitado; o KG NÃO faz formação/extração/retrieval
  PORQUE:       "Documento recuperado ≠ conhecimento validado ≠ publicado" — formação é SPEC-007; o KG é a memória do publicado
  REFERÊNCIA:   RULE-CKG-010; ROADMAP §6/§7; research.md §3.4
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que verifica o selo de "conhecimento publicado" (origem SPEC-007) antes de aceitar
    GATE DE SAÍDA: verificação (entrada tem selo de publicação/validação; senão rejeita)
    CRITÉRIO 4Es: Conformidade > Eficácia — não contaminar a memória permanente com não-validado
  VERIFICADO POR:
    DADO        um trecho recuperado (não publicado) submetido ao KG
    QUANDO      o gate de fronteira roda
    ENTÃO       entrada rejeitada; formação permanece em SPEC-007
    VERIFICAÇÃO accepted == false; rejected_reason == "KNOWLEDGE_NOT_PUBLISHED"
```

### BASpec-CKG-011 — Consulta cognitiva read-only + Cognitive Trace Reconstruction

```
BASpec-CKG-011:
  QUANDO:       Um consumidor consulta o KG (padrão/similaridade/causalidade/histórico/multi-salto) ou pede a reconstrução
                da cadeia cognitiva de uma evidência/hipótese
  ENTÃO:        O KG responde read-only navegando as relações (incl. Lineage — Cognitive Trace Reconstruction, CEM-001
                l.608-615) sem alterar estado; a consulta é opcional/não-bloqueante (SAS-001 §6.12/EC-COG-003)
  PORQUE:       Reconstrução da cadeia cognitiva é responsabilidade atribuída ao KG (CEM-001 l.562-565/l.699); consulta não muta
  REFERÊNCIA:   RULE-CKG-011; CEM-001 l.608-615; SAS-001 §6.12
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : travessia determinística das relações a partir de um nó; reconstrução por navegação de Lineage; read-only
    CRITÉRIO 4Es: Eficácia (reconstrução completa) + Eficiência (travessia dirigida); alcance multi-salto limitado até H-001 (INDETERMINADO)
  VERIFICADO POR:
    DADO        Evidence-D com Lineage [C], C com Lineage [A,B]
    QUANDO      pede-se Cognitive Trace Reconstruction de Evidence-D
    ENTÃO       retorna [A,B,C]; nenhum estado alterado
    VERIFICAÇÃO trace == ["A","B","C"]; state_mutated_by_query == false
```

### BASpec-CKG-012 — Lifecycle do nó/relação (versionado; nunca remove)

```
BASpec-CKG-012:
  QUANDO:       Um nó/relação é substituído ou rebaixado (consolidação/"esquecimento")
  ENTÃO:        O KG transita ACTIVE_KNOWLEDGE→SUPERSEDED (cadeia preservada) ou →ARCHIVED (rebaixado sob governança) de
                forma VERSIONADA; a versão anterior é preservada e reconstruível; nenhuma transição remove o histórico
  PORQUE:       O conhecimento permanente/temporário é operacionalizado por lifecycle versionado, não por deleção (INV-07)
  REFERÊNCIA:   RULE-CKG-012; CHM-001; INV-07
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : máquina de estados do nó/relação com transições append-only (nova versão aponta para a anterior)
    CRITÉRIO 4Es: Eficácia — reconstrução íntegra do histórico de conhecimento
  VERIFICADO POR:
    DADO        um nó ACTIVE_KNOWLEDGE substituído por versão nova
    QUANDO      a transição roda
    ENTÃO       nó antigo → SUPERSEDED (preservado, apontado pela nova versão); histórico reconstruível
    VERIFICAÇÃO old_version_preserved == true; supersedes_link_present == true
```

### BASpec-CKG-013 — Colisão de relações (detecta e registra; não resolve em silêncio)

```
BASpec-CKG-013:
  QUANDO:       Duas relações entre os mesmos nós se contradizem (ex.: CONFIRMA × REFUTA)
  ENTÃO:        O KG DETECTA e REGISTRA a colisão, preservando ambas versionadas (com proveniência e validade temporal);
                NÃO sobrescreve nem apaga uma em silêncio; a resolução (qual prevalece) é de SPEC-007/SPEC-018 ou governança
  PORQUE:       Preservar a contradição auditável respeita INV-07; resolver em silêncio perderia conhecimento e viés de confirmação
  REFERÊNCIA:   RULE-CKG-013; INV-07; fronteira SPEC-007/SPEC-018
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : detecção determinística de par contraditório + registro de ambas; proíbe sobrescrita silenciosa
    GATE DE SAÍDA: verificação (ambas as relações preservadas ∧ colisão registrada ∧ nenhuma apagada)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda de conhecimento e auditabilidade da contradição
  VERIFICADO POR:
    DADO        relação CONFIRMA(A→B) existente e uma REFUTA(A→B) nova submetida
    QUANDO      a escrita roda
    ENTÃO       ambas preservadas; colisão registrada; nenhuma apagada; resolução não decidida pelo KG
    VERIFICAÇÃO both_relations_present == true; collision_logged == true; silent_overwrite == false
```

---

## D4 — Algoritmo

Mecânicas **determinísticas reais** especificáveis (D4 "onde há regra determinística real" — atomic-spec §2). O
**mecanismo físico de armazenamento** (grafo real/estrutura em memória/tabelas+índice) é **INDETERMINADO = H-001
(ABERTA)**; abaixo está a lógica, não a tecnologia:

- **Validade temporal / invalidar≠deletar (CKG-004):** `ao mudar a informação de R: R.valid_to := T_mudança (preserva R); cria R' com valid_from := T_mudança`. Consulta "em T": `relações com valid_from ≤ T < valid_to`. Consulta "agora": `valid_to == null`.
- **Imutabilidade (CKG-006/012):** `DELETE físico ⇒ negado; "esquecer" ⇒ transição de lifecycle (ACTIVE_KNOWLEDGE→SUPERSEDED|ARCHIVED) com nova_versão.supersedes := versão_anterior`. Histórico sempre reconstruível.
- **Dedupe de nó/relação (CKG-001/003):** `chave de nó = (tipo, canonical_ref) ; chave de relação = (tipo, origem, destino, janela_de_validade)`. Reescrita idêntica = no-op; divergente = nova versão (não sobrescreve).
- **Cognitive Trace Reconstruction (CKG-011):** `trace(x) = travessia das relações de Lineage a partir de x, acumulando ancestrais diretos e indiretos` (CEM-001 l.562-577). Alcance multi-salto pode ser limitado até H-001 (INDETERMINADO).
- **Gate causal (CKG-008):** `relação.tipo == CAUSA ⇒ exige {mechanism, direction, conditions} ≠ ∅; senão rejeita`. O juízo que propõe é bounded (nº máximo de tentativas por par de nós).
- **Confiança de relação (CKG-007):** `confidence ∈ escala própria do KG (PARÂMETRO a calibrar — INDETERMINADO)`; **proibido** `confidence → qualquer dimensão/insumo do Conviction Vector` (namespaces separados; INV-04).

Nenhuma fórmula computa convicção (o KG não é o Conviction Engine). Nenhum limiar numérico de convicção nem escala
numérica de confiança é fixado neste Plan (RULE-MET-01). [FONTE: atomic-spec §2; CEM-001 Cap.5; research.md §3.1/§4]

---

## D5 — Máquina de estados (lifecycle do nó/relação do KG)

> **Fronteira (CC-02):** este é o lifecycle do **conhecimento no KG permanente**. É **separado** da máquina de estados da
> **hipótese** (CHM-001: EMERGENT→…→ARCHIVED) e do **estado do objeto no Blackboard** (publication_state/domain_state —
> SPEC-004) — **não redefinidos** aqui. O KG armazena hipóteses como nós por referência, preservando seus estados.

Lifecycle do nó/relação — `knowledge_state` [PROPOSTA]:

| Estado | Descrição | Transições |
|---|---|---|
| CANDIDATE_WRITE | Submetido; passando pelos gates (ontologia/proveniência/autorização/fronteira) | → ACTIVE_KNOWLEDGE (gates ok) · → REJECTED (gate falha) |
| ACTIVE_KNOWLEDGE | Conhecimento permanente vigente (nó/relação válido agora) | → SUPERSEDED (substituído por versão nova) · → ARCHIVED (rebaixado sob governança) · (relação) → INVALIDATED_IN_TIME (fim de validade) |
| SUPERSEDED | Substituído por versão nova; cadeia preservada (supersedes) | terminal (reconstruível; nunca deletado) |
| INVALIDATED_IN_TIME | Relação cuja validade terminou (valid_to definido); preservada | terminal (consultável "em T"; nunca deletada) |
| ARCHIVED | Rebaixado de relevância sob governança (consolidação/"esquecimento") | terminal (reconstruível; nunca deletado) |
| REJECTED | Falhou em gate (ontologia/proveniência/autorização/fronteira/causal) — não persistido | terminal |

> **Nota de imutabilidade (INV-CKG-01):** nenhum estado transita para deleção física; todas as transições são
> append-only e reconstruíveis (INV-07; RULE-BB-004). O **mecanismo físico** que materializa esses estados =
> **INDETERMINADO (H-001 ABERTA)**; a Opção B (banco de grafos dedicado) está **registrada e adiada** (research.md
> §3.5), adotável só se Andraus fechar H-001 como "grafo real". [FONTE: RULE-CKG-006/012; DHR-SPEC006-001 §3]

---

## D6 — Protocolo de escrita/consulta (sobre conhecimento publicado)

### Produtores, consumidores e fronteira [FONTE: SAS-001 §6.12; CEM-001 l.608-615; SPEC-004/005; ROADMAP §6/§7]
- A **origem** de todo conhecimento escrito no KG é conhecimento **já publicado/validado** (SPEC-007) — o KG **não** forma conhecimento.
- O **produtor** (agente) registra relações (fractais/temporais/estruturais/causais estruturais) mas **não redefine** a ontologia/taxonomia (SAS-001 §6.12); a escrita é governada por identidade autenticada (reusa SPEC-004).
- O KG **consome** eventos de ciclo de vida (ex.: "Evidence Invalidated" — CEM-001 l.600/l.717-727; via SPEC-005) para atualizar a validade das relações, e pode **emitir** eventos de mudança de conhecimento (via SPEC-005); **não** redefine o transporte.
- A **consulta** é read-only e **opcional/não-bloqueante** (SAS-001 §6.12/EC-COG-003 — "não é pré-requisito obrigatório").

### Sequência de escrita (um nó/relação)
1. **Submissão:** conhecimento publicado (SPEC-007) propõe nó/relação ao KG.
2. **Fronteira (CKG-010, gate):** verifica selo de "publicado/validado"; não-publicado ⇒ `REJECTED`.
3. **Autorização (CKG-009, gate E3):** escritor autorizado + identidade autenticada; produtor não redefine ontologia ⇒ senão `REJECTED`.
4. **Ontologia/integridade (CKG-001, gate):** tipo ∈ catálogo ∧ integridade ⇒ senão `REJECTED`.
5. **Proveniência (CKG-005, gate):** provenance_ref presente (CEM-001/SPEC-004) ⇒ senão `REJECTED`.
6. **Causalidade (CKG-008, se CAUSA):** mechanism+direction+conditions presentes ⇒ senão `REJECTED`.
7. **Colisão (CKG-013):** se contradiz relação existente, registra colisão (ambas preservadas), não sobrescreve.
8. **Escrita append-only (CKG-006):** `ACTIVE_KNOWLEDGE`; substituição ⇒ `SUPERSEDED` da anterior (supersedes); deleção física proibida.
9. **Temporalidade (CKG-004):** relações carregam valid_from/valid_to; mudança ⇒ `INVALIDATED_IN_TIME`, nunca deleção.
10. **Evento (SPEC-005):** emite notificação de mudança de conhecimento (transporte ≠ fonte de verdade — fronteira SPEC-005).

> **Nota de fronteira:** a **memória de trabalho** e sua ordem/versão são do **Blackboard (SPEC-004)**; a **notificação**
> é do **Event Bus (SPEC-005)**; a **formação** do conhecimento é do **RAG (SPEC-007)**. A SPEC-006 só **preserva,
> relaciona e consulta** o conhecimento permanente. [FONTE: ROADMAP §5/§6/§7; "Nunca misturar"]

---

## D7 — Cenários de Teste

### Cenário-CKG-T01 — Tipo fora da ontologia → rejeição
```
DADO        um nó de tipo não-declarado na ontologia
QUANDO      o gate de integridade roda
ENTÃO       escrita rejeitada; nada persistido
VERIFICAÇÃO node_written == false; rejected_reason == "ONTOLOGY_TYPE_NOT_ALLOWED"
```

### Cenário-CKG-T02 — Entidade referencia canônico sem redefinir
```
DADO        um nó-hipótese referenciando CHM-001 por id@version
QUANDO      o nó é escrito
ENTÃO       referência preservada; nenhum campo/estado do CHM-001 redefinido
VERIFICAÇÃO canonical_ref_present == true; canonical_contract_redefined == false
```

### Cenário-CKG-T03 — Validade temporal (invalidar ≠ deletar)
```
DADO        relação válida desde T0 cuja informação muda em T1
QUANDO      a atualização é processada
ENTÃO       relação antiga marcada valid_to=T1 (preservada); consulta "em T0" ainda a retorna
VERIFICAÇÃO old_relation_deleted == false; valid_to_set == true; historical_query_consistent == true
```

### Cenário-CKG-T04 — Escrita sem proveniência → rejeição
```
DADO        um nó submetido sem provenance_ref
QUANDO      o gate de escrita roda
ENTÃO       escrita rejeitada; nada persistido
VERIFICAÇÃO written == false; rejected_reason == "PROVENANCE_MISSING"
```

### Cenário-CKG-T05 — Deleção proibida (esquecimento = arquivamento versionado)
```
DADO        tentativa de deletar fisicamente um nó arquivado
QUANDO      o gate de imutabilidade roda
ENTÃO       deleção negada (fail-closed); nó permanece arquivado e reconstruível
VERIFICAÇÃO physical_delete == false; history_preserved == true
```

### Cenário-CKG-T06 — Confiança de relação não entra na Convicção
```
DADO        relação com confiança registrada e um cálculo de Conviction Vector no mesmo ciclo
QUANDO      o cálculo de convicção roda (fora do KG)
ENTÃO       a confiança de relação NÃO é usada como dimensão/insumo do Conviction Vector
VERIFICAÇÃO relation_confidence_in_conviction == false
```

### Cenário-CKG-T07 — Causal sem mecanismo → rejeição (não pós-hoc)
```
DADO        relação CAUSA proposta sem mechanism (só correlação)
QUANDO      o gate de saída roda
ENTÃO       relação rejeitada; exige mecanismo declarado
VERIFICAÇÃO causal_written == false; rejected_reason == "CAUSAL_MECHANISM_MISSING"
```

### Cenário-CKG-T08 — Produtor tenta redefinir ontologia → negado [E3]
```
DADO        produtor autenticado tentando alterar a ontologia global (não só registrar relação)
QUANDO      o gate E3 de governança roda
ENTÃO       operação negada (fail-closed); registrar relação seria permitido; redefinir ontologia não
VERIFICAÇÃO ontology_redefined_by_producer == false; fail_closed == true
```

### Cenário-CKG-T09 — Conhecimento não-publicado → rejeição (fronteira SPEC-007)
```
DADO        um trecho recuperado (não publicado) submetido ao KG
QUANDO      o gate de fronteira roda
ENTÃO       entrada rejeitada; formação permanece em SPEC-007
VERIFICAÇÃO accepted == false; rejected_reason == "KNOWLEDGE_NOT_PUBLISHED"
```

### Cenário-CKG-T10 — Cognitive Trace Reconstruction (read-only)
```
DADO        Evidence-D com Lineage [C], C com Lineage [A,B]
QUANDO      pede-se Cognitive Trace Reconstruction de Evidence-D
ENTÃO       retorna [A,B,C]; nenhum estado alterado
VERIFICAÇÃO trace == ["A","B","C"]; state_mutated_by_query == false
```

### Cenário-CKG-T11 — Colisão de relações registrada (não resolve em silêncio)
```
DADO        relação CONFIRMA(A→B) existente e uma REFUTA(A→B) nova submetida
QUANDO      a escrita roda
ENTÃO       ambas preservadas; colisão registrada; nenhuma apagada; resolução não decidida pelo KG
VERIFICAÇÃO both_relations_present == true; collision_logged == true; silent_overwrite == false
```

---

## D8 — Rigor adversarial focado (casos de negação nos pontos de risco)

> Profundidade-alvo é **D0–D7 + D8 adversarial focado** (CRITICAL, pin D0–D7; mesma reconciliação da SPEC-004). Os
> casos de negação abaixo concentram-se nos pontos de maior risco: **imutabilidade (INV-07)**, **confiança ≠ Convicção
> (INV-04)**, **causalidade pós-hoc (RULE-CAU)**, **colisão de relações** e **governança de escrita**. Princípio
> transversal: **fail-closed**, **nunca deletar**, **mecanismo físico INDETERMINADO (H-001)**.

### ADV-CKG-01 — Deleção disfarçada de "esquecimento" (viola CKG-006/INV-07)
**DADO:** pedido de "esquecer" um nó traduzido em DELETE físico. **QUANDO:** o gate roda. **ENTÃO:** negar; só arquivamento/rebaixamento versionado. **PORQUE:** memória permanente nunca apaga (INV-07/RULE-BB-004). **VERIFICAÇÃO:** physical_delete == false.

### ADV-CKG-02 — Sobrescrita silenciosa de relação contraditória (viola CKG-013)
**DADO:** REFUTA(A→B) nova sobre CONFIRMA(A→B) existente. **QUANDO:** a escrita roda. **ENTÃO:** registrar colisão; preservar ambas; não sobrescrever. **PORQUE:** perder a contradição apaga conhecimento e introduz viés. **VERIFICAÇÃO:** silent_overwrite == false; both_relations_present == true.

### ADV-CKG-03 — Confiança de relação retroalimenta o Conviction Vector (viola CKG-007/INV-04)
**DADO:** proposta de somar a confiança de relação como 9ª dimensão/insumo da convicção. **QUANDO:** o escopo é definido. **ENTÃO:** rejeitar `CONFIDENCE_IS_NOT_CONVICTION`; namespaces separados. **PORQUE:** Convicção ≠ Score; custo/confiança nunca entram (INV-04); dimensionalidade=8 fechada. **VERIFICAÇÃO:** relation_confidence_in_conviction == false.

### ADV-CKG-04 — Relação causal pós-hoc por correlação (viola CKG-008/RULE-CAU-01)
**DADO:** CAUSA(A→B) proposta só por co-ocorrência histórica. **QUANDO:** o gate de saída roda. **ENTÃO:** rejeitar; exigir mecanismo+direção+condições. **PORQUE:** correlação não é causalidade (RULE-CAU-01). **VERIFICAÇÃO:** causal_written == false.

### ADV-CKG-05 — Custo/score escrito como propriedade que vira convicção (viola INV-04)
**DADO:** tentativa de escrever custo/score de um componente como insumo de convicção via nó do KG. **QUANDO:** a escrita roda. **ENTÃO:** o KG pode armazenar a métrica de calibração (CEE-001 l.111) como nó, mas isolada do Conviction Vector; rejeitar qualquer ligação custo→convicção. **PORQUE:** INV-04. **VERIFICAÇÃO:** cost_into_conviction == false.

### ADV-CKG-06 — Escrita sem proveniência aceita (viola CKG-005)
**DADO:** nó/relação sem provenance_ref. **QUANDO:** o gate roda. **ENTÃO:** rejeitar `PROVENANCE_MISSING`; nada persistido. **PORQUE:** conhecimento sem origem não é reconstruível (P13; CEM-001 Cap.5). **VERIFICAÇÃO:** written == false.

### ADV-CKG-07 — Produtor redefine ontologia/taxonomia (viola CKG-009/SAS-001 §6.12)
**DADO:** produtor autenticado tenta alterar a ontologia global. **QUANDO:** o gate E3 roda. **ENTÃO:** negar (fail-closed); produtor registra relações, não redefine ontologia. **PORQUE:** SAS-001 §6.12 (produtor não altera taxonomias globais). **VERIFICAÇÃO:** ontology_redefined_by_producer == false.

### ADV-CKG-08 — KG forma conhecimento / absorve SPEC-007 (viola CKG-010/fronteira)
**DADO:** tentativa de fazer extração/retrieval/validação dentro do KG. **QUANDO:** o escopo é definido. **ENTÃO:** rejeitar `OUT_OF_SCOPE_FORMATION`; formação é SPEC-007; o KG recebe conhecimento publicado. **PORQUE:** "documento recuperado ≠ conhecimento validado ≠ publicado". **VERIFICAÇÃO:** formation_in_kg == false.

### ADV-CKG-09 — Fechar H-001 / escolher banco de grafos por inércia (viola CONS-01/mandato)
**DADO:** pressão para fixar "grafo real" (ou escolher engine) ao especificar o KG. **QUANDO:** as decisões são definidas. **ENTÃO:** rejeitar `OPEN_DECISION_H001`; mecanismo físico permanece INDETERMINADO; Opção B registrada e adiada. **PORQUE:** H-001 é decisão de Andraus (CONS-01); o contrato cognitivo é fechável sem fechar H-001. **VERIFICAÇÃO:** h001_closed_by_spec == false.

### ADV-CKG-10 — Absorver/duplicar vizinhos ou fechar decisão aberta (viola fronteiras/CONS-01)
**DADO:** tentativa de a SPEC-006 virar memória de trabalho (SPEC-004), transporte (SPEC-005), estado por agente (SPEC-009), ciclo de aprendizado (SPEC-018), ou **fechar** M-001/J-001/N-001/G-001/K-001/C-001/WF-D03. **QUANDO:** o escopo/decisões são definidos. **ENTÃO:** rejeitar `OUT_OF_SCOPE_OR_OPEN_DECISION`; fronteiras explícitas; decisões abertas permanecem ABERTAS (Andraus). **PORQUE:** CONS-01; INV-09; "Nunca misturar". **VERIFICAÇÃO:** neighbors_absorbed == false; open_decisions_closed == false.

> **Cobertura:** 10 casos de negação sobre os pontos sensíveis declarados na abertura (imutabilidade INV-07, confiança≠
> Convicção INV-04, causalidade pós-hoc RULE-CAU, colisão de relações, governança de escrita) e as fronteiras/decisões
> abertas (H-001, SPEC-004/005/007/009/018). Mapeiam para EC-CKG-001..006 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada nó/relação DEVE ser reconstruível (P13/RULE-010): tipo, referência canônica (id@version), proveniência (CEM-001
Lineage/gate_record + SPEC-004), validade temporal (valid_from/valid_to), `knowledge_state` e cadeia de supersessão. A
**Cognitive Trace Reconstruction** (reconstrução da cadeia cognitiva completa de qualquer evidência/hipótese) é
capacidade central do KG (CEM-001 l.608-615; l.562-565; l.699) — especificada como comportamento verificável (CKG-011).
A **observabilidade agregada** (métricas de uso/crescimento da memória) e a **reconstrução expandida de estado de
trabalho** pertencem à SPEC-040 (Observabilidade) e à SPEC-004 (replay de estado) — aqui ficam **por referência**
(coerente com alvo D0–D7 e com H-001 ABERTA). [FONTE: CONSTITUTION P13; RULE-010; CEM-001 l.608-615; SPEC-004 replay; H-001 ABERTA]

---

## Contrato do nó/relação — esqueleto [PROPOSTA]

> Produto central da SPEC-006. **Referencia** os objetos canônicos (CHM/CEM/CCM) por `canonical_ref`; **não** os
> redefine (CC-02). Memória permanente ≠ trabalho. O **mecanismo físico** que materializa este contrato = **INDETERMINADO
> (H-001 ABERTA)**.

| Camada | Conteúdo (nó) | Conteúdo (relação) | Fronteira |
|---|---|---|---|
| Identidade | `node_id`, `node_type` (∈ ontologia), `schema_version` | `relation_id`, `relation_type` (∈ ontologia), `from_node`, `to_node` | tipos ∈ catálogo (CKG-001/003) |
| Referência canônica | `canonical_ref` = `canonical_id@version` (CHM/CEM/CCM) | — | referencia, não redefine (CC-02/CKG-002) |
| Proveniência | `provenance_ref` (CEM-001 Lineage/gate_record + SPEC-004) | idem | obrigatória (CKG-005) |
| Temporalidade | `created_at` | `valid_from`, `valid_to` (null = vigente) | invalidar≠deletar (CKG-004) |
| Confiança | — | `relation_confidence` (escala PRÓPRIA — **PARÂMETRO a calibrar**, INDETERMINADO) | ≠ Convicção; nunca retroalimenta o Conviction Vector (CKG-007/INV-04) |
| Causalidade | — | se `relation_type == CAUSA`: `mechanism`, `direction`, `conditions` (obrigatórios) | RULE-CAU-01 (CKG-008) |
| Lifecycle | `knowledge_state` (CANDIDATE_WRITE/ACTIVE_KNOWLEDGE/SUPERSEDED/ARCHIVED/REJECTED) | +INVALIDATED_IN_TIME | append-only; `supersedes` (CKG-006/012) |

### I/O Schema (lógico — referência; não redefine CHM-001/CEM-001/CCM-001)
```json
{
  "node": {
    "node_id": "KG-N-2026-10-11-001",
    "node_type": "hypothesis | evidence | conviction | narrative | mission | learning | asset | timeframe | regime | structure | calibration_metric",
    "schema_version": "1 (versão do contrato do KG; migração NÃO definida aqui)",
    "canonical_ref": "CHM-xxxx@v2 | CEM-xxxx@v1 | CCM-xxxx@v1 (referência; NÃO redefine o canônico)",
    "provenance_ref": "{ lineage_ref (CEM-001), gate_record (SPEC-004), who, when, why, from }",
    "created_at": "2026-10-11T12:00:00Z",
    "knowledge_state": "ACTIVE_KNOWLEDGE"
  },
  "relation": {
    "relation_id": "KG-R-2026-10-11-001",
    "relation_type": "CONFIRMA | REFUTA | DEPENDE_DE | HERDA | PERTENCE_A | INVALIDA | ORIGINA | SIMILAR_A | CAUSA | HIERARQUIA_DE | ESTATISTICA_DE",
    "from_node": "KG-N-...-A",
    "to_node": "KG-N-...-B",
    "provenance_ref": "{ ... }",
    "valid_from": "2026-10-11T12:00:00Z",
    "valid_to": "null (vigente) | 2026-11-01T00:00:00Z (invalidada no tempo — preservada)",
    "relation_confidence": "escala PRÓPRIA do KG — PARÂMETRO a calibrar ([DECISÃO NECESSÁRIA]/INDETERMINADO; NÃO é Convicção; não toca J-001/N-001)",
    "causal": "{ mechanism, direction, conditions } (obrigatório sse relation_type == CAUSA — RULE-CAU-01)",
    "knowledge_state": "ACTIVE_KNOWLEDGE"
  }
}
```
> O nó **referencia** o objeto canônico por `canonical_ref`; não o redefine (CC-02). Nenhum campo computa convicção nem
> deriva de custo (INV-04 — fora do escopo deste componente). Mecanismo físico de armazenamento = INDETERMINADO (H-001 ABERTA).

---

## Enforcement Contracts

### EC-CKG-001 — Escrita de nó/relação no KG permanente (gates de ontologia + proveniência + fronteira)
```
CAPABILITY   : Escrever um nó/relação válido no KG permanente
EFFECT       : Persistência de conhecimento permanente (commit de alto valor; append-only)
PRECOND      : (tipo ∈ ontologia ∧ integridade — CKG-001) AND (proveniência presente — CKG-005) AND (conhecimento publicado — CKG-010) AND (relação CAUSA ⇒ mecanismo — CKG-008)
POSTCOND     : nó/relação em ACTIVE_KNOWLEDGE com proveniência e validade; versão anterior preservada se houver supersessão
POLICY       : RULE-CKG-001/003/005/008/010; CEM-001 l.608-615; CC-02
LEVEL        : E2 (Operacional — commit em memória permanente; gates determinísticos)
FAILURE-MODE : Fail-closed — qualquer gate falha ⇒ REJECTED; nada persistido; log
EVIDENCE     : registro do nó/relação (tipo/ref canônica/proveniência/validade/knowledge_state) reconstruível
```

### EC-CKG-002 — Imutabilidade / proibição de deleção [E3]
```
CAPABILITY   : Impedir deleção física e garantir arquivamento versionado
EFFECT       : Transição de lifecycle versionada (SUPERSEDED/ARCHIVED/INVALIDATED_IN_TIME) — nunca remoção
PRECOND      : (operação ≠ DELETE física) AND (nova versão aponta para a anterior quando substitui)
POSTCOND     : histórico preservado e reconstruível; nenhum registro removido (INV-07)
POLICY       : RULE-CKG-006/012; INV-07; RULE-BB-004; INV-CKG-01
LEVEL        : E3 (Crítico — perda de histórico é irreversível; fail-closed)
FAILURE-MODE : Fail-closed — tentativa de DELETE ⇒ negada; log. **Enforcement do E3 CONDICIONAL até o limiar amostral de falso-DENY ser definido (gap aberto, ENF-07)** (atomic-spec §12)
EVIDENCE     : gate_record de imutabilidade + ENF-07: amostragem de falso-DENY (bloqueio indevido de arquivamento legítimo)
```

### EC-CKG-003 — Governança de escrita (autorizado + autenticado; não redefine ontologia) [E3]
```
CAPABILITY   : Admitir escrita só de escritor autorizado/autenticado, sem redefinição de ontologia pelo produtor
EFFECT       : Autorização (ou recusa) de escrita permanente no KG
PRECOND      : (escritor ∈ autorizados ∧ identidade AUTENTICADA pelo runtime — SPEC-004 CBP-014) AND (operação ∉ {redefinir ontologia/taxonomia global} — SAS-001 §6.12) AND (gate determinístico — ENF-03)
POSTCOND     : só escritor autorizado escreve; produtor registra relações, não redefine ontologia
POLICY       : RULE-CKG-009; SAS-001 §6.12; SPEC-004 RULE-CBP-014; ENF-03/04
LEVEL        : E3 (Crítico — escrita em memória permanente, cruza fronteira de confiança)
FAILURE-MODE : Fail-closed — escritor não autorizado / tentativa de redefinir ontologia ⇒ negada; log. **Falso-DENY E3 CONDICIONAL até limiar (ENF-07)**
EVIDENCE     : gate_record de autorização por identidade autenticada + amostragem de falso-DENY (ENF-07)
```

### EC-CKG-004 — Isolamento confiança de relação × Conviction Vector (INV-04)
```
CAPABILITY   : Manter a confiança de relação isolada do cálculo de convicção
EFFECT       : Garantia (guard) de que confiança de relação nunca entra no Conviction Vector
PRECOND      : (campo de confiança de relação em namespace separado do Conviction Vector)
POSTCOND     : nenhuma dimensão/insumo do Conviction Vector recebe a confiança de relação nem custo/score
POLICY       : RULE-CKG-007; INV-04; CCM-001
LEVEL        : E2 (Operacional — guard constitutivo; INV-04)
FAILURE-MODE : Fail-closed — tentativa de ligar confiança/custo → convicção ⇒ negada; log
EVIDENCE     : verificação de que o cálculo de convicção (SPEC-003) não consome o campo de confiança do KG
```

### EC-CKG-005 — Registro de relação causal com mecanismo (RULE-CAU)
```
CAPABILITY   : Admitir relação causal apenas com mecanismo declarado
EFFECT       : Escrita (ou recusa) de relação CAUSA
PRECOND      : (relation_type == CAUSA) ⇒ (mechanism ∧ direction ∧ conditions presentes); gate de saída determinístico (Classe H)
POSTCOND     : relações causais no KG têm mecanismo auditável; nenhuma causal pós-hoc por correlação
POLICY       : RULE-CKG-008; RULE-CAU-01; ENF-03
LEVEL        : E2 (Operacional — gate de saída sobre juízo; LLM detector, nunca gate)
FAILURE-MODE : Fail-closed — causal sem mecanismo ⇒ rejeitada; bounded loop no juízo (sem retry infinito)
EVIDENCE     : registro do mechanism/direction/conditions por relação causal; contagem de tentativas ≤ limite
```

### EC-CKG-006 — Consulta cognitiva / Cognitive Trace Reconstruction (read-only)
```
CAPABILITY   : Responder consultas cognitivas e reconstruir a cadeia cognitiva sem alterar estado
EFFECT       : Leitura/navegação de nós e relações (sem escrita)
PRECOND      : (consulta é read-only) AND (consumidor autorizado a ler)
POSTCOND     : resposta/trace retornado; nenhum estado do KG alterado pela consulta
POLICY       : RULE-CKG-011; CEM-001 l.608-615; SAS-001 §6.12
LEVEL        : E1 (Contratual — leitura observável; não muta estado)
FAILURE-MODE : Fail-closed — consulta que tente mutar estado ⇒ negada; alcance multi-salto limitado até H-001 (INDETERMINADO)
EVIDENCE     : log de consulta read-only; trace reconstruído = relações de Lineage navegadas
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
Serviço lógico de **memória semântica permanente** (Opção A — camada de memória permanente sobre o conhecimento já
validado/publicado), definindo o contrato cognitivo (ontologia enxuta + entidades/relações tipadas + temporalidade +
proveniência por referência + lifecycle + confiança de relação + consulta cognitiva + governança de escrita +
imutabilidade append-only). Combina gates constitutivos determinísticos (Classe C: ontologia, proveniência,
imutabilidade/não-deleção, governança de escrita E3, fronteira só-publicado, isolamento confiança×convicção, colisão)
e mecânica determinística (Classe D: catálogo de entidades/relações, temporalidade, lifecycle, consulta/trace
reconstruction) e um juízo com gate de saída (Classe H: proposta de similaridade/causalidade sob mecanismo). **Não
guarda memória de trabalho, não transporta, não forma conhecimento, não decide, não computa convicção, não executa
ordem, e NÃO escolhe o mecanismo físico de armazenamento (H-001 ABERTA).** [FONTE: ROADMAP §6; CEM-001 l.608-615; SAS-001 §6.12; research.md §3/§4]

### Roteamento de modelo (CEE-001 §5)
Gates constitutivos/determinísticos (C/D) **não requerem LLM** — são código. O juízo de similaridade/causalidade
(Classe H, CKG-008) pode usar apoio semântico **apenas como detector** para PROPOR a relação; o gate de saída que
verifica o mecanismo é **determinístico** (ENF-03 — LLM nunca é seu próprio gate). Roteamento definitivo por
Engineering Card (BUILD adiado). O **mecanismo físico de armazenamento** (grafo real/estrutura em memória/tabelas+índice)
é **INDETERMINADO = H-001 (ABERTA)**. [FONTE: CEE-001 §5; ENF-03; H-001 ABERTA]

### Dependências técnicas
CEM-001 (BASELINE — Responsabilidades do KG l.608-615; Cognitive Trace Reconstruction l.562-565/l.699) · CHM-001 (BASELINE) ·
CCM-001 (BASELINE) · CEE-001 l.111 (BASELINE) · SAS-001 §6.12 · SPEC-004 v1.2 (BASELINE — proveniência/identidade autenticada) ·
SPEC-005 v1.0 (BASELINE — eventos de ciclo de vida) · SPEC-007 (fronteira — conhecimento publicado; ainda não especificada) ·
CONSTITUTION l.233 (EC-COG-003) · RULES.md (RULE-BB-004, RULE-CAU-01, RULE-MECH-01, RULE-HD-02/03/04) · SPEC-019/020/021 v1.0 (BASELINE) ·
atomic-spec v1.5 · INV-04/05/06/07/09/10 · ENF-01..08. Referências externas [EXTERNO], não-baseline: research.md §2
(SRC-ZEP-01, SRC-PROV-01, SRC-MEMVSKG-01, SRC-FORGET-01) e §5 (REPO-graphiti/graphrag/cognee/mem0 — elegíveis, nenhum adotado).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Over-engineering: banco de grafos por inércia do nome "Graph" | Opção A (camada de memória permanente); Opção B registrada e ADIADA (research.md §3.5); mecanismo físico = H-001 (ABERTA); ADV-CKG-09 |
| Fechar H-001 por engano (pressão de "especificar o KG") | contrato cognitivo fechável sem fechar H-001; H-001 [DECISÃO NECESSÁRIA]; ADV-CKG-09; CONS-01 |
| Invadir/absorver a SPEC-007 (formação/retrieval) | Non-goal explícito; CKG-010 (só conhecimento publicado); ADV-CKG-08; "documento recuperado ≠ conhecimento validado" |
| Reabrir/duplicar SPEC-004/005 (trabalho/transporte) | CC-02 foco; "Nunca misturar"; cobertura×lacuna; INV-09; ADV-CKG-10 |
| Confiança de relação virar Convicção | INV-04; CKG-007; EC-CKG-004; ADV-CKG-03/05 |
| Deleção disfarçada de "esquecimento" | INV-07; RULE-CKG-006/012; EC-CKG-002 (E3); ADV-CKG-01 |
| Causalidade pós-hoc (correlação como causa) | RULE-CAU-01; CKG-008; EC-CKG-005; ADV-CKG-04 |
| Colisão de relações resolvida em silêncio | CKG-013; EC-CKG-001; ADV-CKG-02 |
| Escrita sem proveniência / produtor redefine ontologia | CKG-005/009; EC-CKG-001/003 (E3); SAS-001 §6.12; ADV-CKG-06/07 |
| LLM como gate de escrita/causalidade | ENF-03; EC-CKG-003/005 (detector≠gate) |
| Ontologia inconsistente ao longo do tempo | ontologia enxuta + regras de integridade (CKG-001); governança de escrita (Classe C/E3) |
| Crescimento ilimitado da memória | lifecycle versionado (CKG-012; arquivamento/rebaixamento, nunca deleção); observabilidade = SPEC-040 (por referência) |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz o schema lógico do **nó/relação do KG**; nenhum schema canônico do CHM-001/CEM-001/CCM-001 nem das SPEC-004/005 alterado.
- **RAG/KG:** especifica o contrato do próprio KG; a formação/retrieval permanece em SPEC-007 (não absorvida).
- **Skills:** nenhuma Skill afetada; INV-06 preservado (Skill produz Observação; o KG a relaciona como nó, sem confundi-la com Evidência).
- **Testes:** adiciona `checks.md` (verificação de spec); mecanismo físico fica para BUILD (H-001).
- **Modelos/Specs dependentes:** CEM-001/CHM-001/CCM-001/SPEC-004/005 não alterados (construção SOBRE); RULE-BB-004 reforçada no eixo permanente, não alterada.
- **Compatibilidade:** Minor — não toca modelo canônico baselined, não reabre SPEC-004/005, não fecha decisão aberta (H-001 permanece ABERTA; DHR-SPEC006-001 §Compatibilidade).

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07), a
Classe por BASpec (CC-11) e o **mecanismo físico de armazenamento** (grafo real/estrutura em memória/tabelas+índice —
hoje INDETERMINADO, **H-001**). O fechamento de H-001 é decisão de Andraus; a homologação do Plan **não** o exige
(contrato cognitivo fechável com mecanismo físico aberto — Opção A).

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — pergunta adversarial por BASpec com efeito (cobertura das 13 BASpecs CRITICAL):**

- **CKG-001 (ontologia, C):** se errada → tipo fora da ontologia persistido → observável por nó de tipo inválido no KG; verificável. Negação: ADV-CKG-01 (contexto), T01. QUANDO-sim-mas-ENTÃO-não: tipo válido com integridade satisfeita é escrito (correto).
- **CKG-002 (referência canônica, D):** se errada → contrato canônico redefinido no KG → observável por campo/estado divergente do CHM/CEM/CCM; verificável. Negação: viola CC-02 (T02).
- **CKG-003 (relação tipada, D):** se errada → relação sem tipo/direção/proveniência escrita → observável por relação não-navegável; verificável. T03/T11.
- **CKG-004 (temporalidade, D):** se errada → relação deletada em vez de invalidada → observável por `old_relation_deleted=true`; verificável. Negação: ADV-CKG-01. QUANDO-sim-mas-ENTÃO-não: consulta "agora" não retorna a relação invalidada (correto).
- **CKG-005 (proveniência, C):** se errada → nó/relação sem origem aceito → observável por `provenance_ref` ausente; verificável. Negação: ADV-CKG-06, T04.
- **CKG-006 (imutabilidade, C/E3):** se errada → deleção física ocorre → observável por `physical_delete=true`; verificável. Negação: ADV-CKG-01, T05.
- **CKG-007 (confiança≠convicção, C):** se errada → confiança de relação entra na convicção → observável por `relation_confidence_in_conviction=true`; verificável. Negação: ADV-CKG-03/05, T06.
- **CKG-008 (causal c/ mecanismo, H):** se errada → causal pós-hoc por correlação escrita → observável por relação CAUSA sem mechanism; verificável. Negação: ADV-CKG-04, T07.
- **CKG-009 (governança escrita, C/E3):** se errada → produtor redefine ontologia ou escritor não-autorizado escreve → observável por `ontology_redefined_by_producer=true`; verificável. Negação: ADV-CKG-07, T08.
- **CKG-010 (fronteira publicado, C):** se errada → conhecimento não-publicado entra → observável por entrada sem selo de publicação; verificável. Negação: ADV-CKG-08, T09.
- **CKG-011 (consulta/trace, D):** se errada → consulta muta estado, ou trace incompleto → observável por `state_mutated_by_query=true` ou trace≠esperado; verificável. T10. QUANDO-sim-mas-ENTÃO-não: alcance multi-salto limitado até H-001 é declarado, não é erro.
- **CKG-012 (lifecycle, D):** se errada → versão anterior removida na transição → observável por `old_version_preserved=false`; verificável. Negação: ADV-CKG-01.
- **CKG-013 (colisão, C):** se errada → relação contraditória sobrescrita em silêncio → observável por `silent_overwrite=true`; verificável. Negação: ADV-CKG-02, T11.

Todas as 13 BASpecs com efeito têm ENTÃO verificável por observador independente e caso de negação em D8. Nenhuma restou
como [DECISÃO NECESSÁRIA] por falta de verificabilidade (H-001/M-001/J-001/N-001/G-001/K-001/C-001/WF-D03 são fronteiras/
decisões abertas explícitas, não falhas de verificabilidade).

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista CEM-001 (l.608-615; l.562-565; l.494; l.699), CHM-001,
CCM-001, CEE-001 l.111, SAS-001 §6.12, SPEC-004 v1.2, SPEC-005 v1.0, RULE-BB-004, RULE-CAU-01, CONSTITUTION l.233, atomic-spec
v1.5, ENF-01..08, INV-04/05/06/07/09/10 (ID+versão/linha — RULE-HD-04). Evidência de satisfação por obrigação herdada:
- CEM-001 Responsabilidades do KG (preservar linhagem/versões/estados; Cognitive Trace Reconstruction) → CKG-011/006/012/004 as especificam como comportamento verificável; não redefinem o CEM.
- CHM-001 (estados/versionamento) → CKG-002/012 armazenam por referência, preservando estados; não criam/transicionam estado de hipótese.
- CCM-001 (Conviction Vector) → CKG-007/EC-CKG-004 isolam a confiança de relação do Conviction Vector (INV-04); não computam convicção.
- SPEC-004 v1.2 (proveniência/identidade autenticada) → CKG-005/009 reusam por referência; não redefinem a proveniência nem o contrato de objeto.
- SPEC-005 v1.0 (eventos) → D6 consome/emite eventos de ciclo de vida; não redefine o transporte.
- SAS-001 §6.12 (produtor não redefine ontologia) → CKG-009/EC-CKG-003 operacionalizam a fronteira.
- RULE-BB-004 / INV-07 (append-only) → CKG-006/012 reforçam como imutabilidade permanente.
- RULE-CAU-01 (mecanismo causal) → CKG-008/EC-CKG-005 exigem mecanismo (não pós-hoc).
- CEE-001 l.111 (métrica entra no KG) → ADV-CKG-05 armazena a métrica isolada da convicção.
- INV-04/05/06/09/10 → CKG-007 (INV-04), D0/Non-goals (INV-05/06), [PROPOSTA] (INV-09), CKG-002 (INV-10).
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (único MODIFIED = RULE-BB-004 reforçada, não alterada —
RULE-HD-02 respeitada). **Eixo VERTICAL (RULE-HV) declarado não aplicável** (herança sobre canônicos/Specs vizinhas/regras,
não decomposição pai→filha de macro-spec).

**Bloco C — epistêmico (RULE-EPI/CAU/PRB):** nenhuma afirmação causal forte sem mecanismo (CKG-008 exige-o — RULE-CAU-01);
nenhuma hipótese tratada como fato (SRC-*/REPO-* = [EXTERNO]/DADO; Graphiti/GraphRAG/cognee/mem0 NÃO importados — adiados);
**INDETERMINADO** usado sobre o mecanismo físico (H-001) e sobre o alcance de consulta multi-salto; **confiança de relação =
PARÂMETRO a calibrar** ([DECISÃO NECESSÁRIA]), não forçada a número; **nenhuma probabilidade/precisão numérica** declarada
(nenhum limiar de convicção nem escala numérica de confiança). IDs arXiv implausíveis descartados (research.md §aviso; RULE-MET-01).

**Bloco D — reforço de escopo:** a Spec **preserva/relaciona/consulta** conhecimento permanente, **não guarda trabalho**
(SPEC-004), **não transporta** (SPEC-005), **não forma conhecimento** (SPEC-007), **não executa** ordem (INV-05/RULE-DEC-01
reconfirmados — §7), **não decide** nem **computa** convicção. Nenhuma BASpec cruza a fronteira SOT→execução downstream.
Dependências de decisão de Andraus (homologação; efetivação de RULE-CKG/contrato; **H-001**) marcadas [PROPOSTA]/[DECISÃO
NECESSÁRIA], não fechadas; M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 abertas, não tocadas.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001; CHM-001; CCM-001; CEE-001; SAS-001; SPEC-004 v1.2; SPEC-005 v1.0; SPEC-001/019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5; RULES v1.5 (RULE-BB-004, RULE-CAU-01, RULE-MECH-01, RULE-HD-*); INV-*; ENF-*; CONSTITUTION l.233 | [FONTE] | FATO NORMATIVO |
| RULE-CKG-001..013; INV-CKG-01; contrato de nó/relação; BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Fontes SRC-ZEP-01/PROV-01/MEMVSKG-01/FORGET-01; REPO-graphiti/graphrag/cognee/mem0 | [EXTERNO] | Referência de método — DADO, nunca baseline (research.md §2/§5) |
| Mecanismo físico de armazenamento (grafo real vs. estrutura em memória vs. tabelas+índice) | [DECISÃO NECESSÁRIA] | **H-001 — EM ABERTO — não fechar** (decisão de Andraus; contrato cognitivo fechável sem fechá-la) |
| Banco de grafos dedicado (Opção B) | [DECISÃO NECESSÁRIA] | **ADIADO** — registrado, não apagado (INV-07); adotável só se Andraus fechar H-001 como "grafo real" |
| Escala numérica de confiança de relação | [DECISÃO NECESSÁRIA] | **PARÂMETRO a calibrar** — INDETERMINADO (sem número; não toca J-001/N-001) |
| Componente "Cognitive Ontology" separado | [DECISÃO NECESSÁRIA] | Ontologia DENTRO da SPEC-006 (Q-ABERTURA-4); criar componente é de Andraus (não feito) |
| Enum de estados do Blackboard p/ objetos não-hipótese | [DECISÃO NECESSÁRIA] | **M-001 — EM ABERTO (SPEC-004)** — não tocado |
| Fórmula/pesos/limiares definitivos do Conviction Vector; pesos por ativo | [DECISÃO NECESSÁRIA] | **J-001 / N-001 — EM ABERTO (SPEC-003/backtest)** — não tocadas |
| Estado persistente por agente / ciclo de evolução do conhecimento (P12) | [DECISÃO NECESSÁRIA] | **G-001 / K-001 — EM ABERTO (SPEC-009/018)** — não tocadas |
| Granularidade EARS multi-condição / relação convicção-macro-global | [DECISÃO NECESSÁRIA] | **C-001 / WF-D03 — EM ABERTO** — não tocadas |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-006 confirmada como próximo autorizado (§6/§21/"próximo trabalho"); FASE 3, após SPEC-005 BASELINE v1.0.
[x] atomic-spec.md lido: método v1.5 confirmado (CC-11/CC-12; RULE-MECH-01; RULE-ECC-04/06; RULE-MM; §15 Dossiê; §3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7).
[x] Nenhum invariante congelado violado (INV-01..10). INV-04/05/06/07/09/10 reforçados; memória permanente imutável (INV-CKG-01).
[x] Constitution Check CC-01..CC-12 preenchido (N/A justificados CC-06/07/12; CC-02/CC-08/CC-09/CC-10/CC-11 INCIDEM e aplicados).
[x] Disciplinas N8–N17: RULE-EPI (H-001 ABERTA; INDETERMINADO sobre mecanismo físico), RULE-CAU-01 (relação causal com mecanismo — CKG-008), RULE-MET-01 (não fabricar escala/limiar; arXiv implausíveis descartados), RULE-UNC (consulta multi-salto antes de H-001), RULE-SEM-01 (acepções "permanente" vs "trabalho"; "confiança" vs "Convicção"), RULE-DEC-01 (armazena≠decide≠executa).
[x] Referências externas [EXTERNO] classificadas (research.md §2/§5); engines externas (Graphiti/GraphRAG/cognee/mem0) NÃO adotadas como baseline; verbatim capturado (RULE-ECC-04, sources/); repositórios sob régua Equilibrada (RULE-ECC-06, research.md §5 — 4 elegíveis, nenhum adotado).
[x] RULE-ECC-05 (Multi-Lente): determinação de NÃO-incidência (infra de memória; não toca comportamento de trading) — confirmada na abertura (DHR-SPEC006-001 §2); conformidade WORKFLOW por prudência (consulta cognitiva; não fecha WF-D03).
[x] Spec sem implementação (BUILD adiado); Plan derivado da abertura homologada; Tasks adiadas (spec-first).
[x] Critérios em EARS (13); BASpecs completas (CKG-001..013) com Classe declarada (CC-11); RULEs citadas existentes vs propostas (RULE-CKG [PROPOSTA]) etiquetadas.
[x] Profundidade D0–D7 (+ D8 adversarial focado) atingida; D4 (temporalidade/dedupe/trace/confiança); D5 (lifecycle do nó/relação); D6 protocolo; D7 x11; D8 ADV-CKG-01..10; D9 por referência.
[x] Enforcement Contract em todo ato com efeito (EC-CKG-001..006); piso E1 (consulta)/E2 (escrita/causal/isolamento); E3 na imutabilidade e na governança de escrita (irreversíveis; fail-closed); ENF-07 amostral declarado nos E3 — enforcement CONDICIONAL até o limiar (gap aberto).
[x] Status epistemológico aplicado (FATO NORMATIVO / PROPOSTA / EXTERNO / DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 permanecem ABERTAS; nenhuma decisão aberta usada como invariante fechado.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos/achados registrados: tensão "banco de grafos × memória cognitiva" tratada como enquadramento histórico coerente (research.md §0; fundamento rejeita "banco de dados"); H-001 não fechada.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE fabricada como vigente; sem baseline informal; linhas canônicas citadas verificadas (CEM-001 l.494/562-565/608-615/699; SAS-001 §6.12; CONSTITUTION l.233; CEE-001 l.111; RULE-BB-004 l.323; RULE-CAU-01 l.680).
[x] 4Es na ordem; Conformidade > Eficácia (INV-04/INV-07/INV-CKG-01 e ENF-03/04 prevalecem). Latência não é material para memória permanente (consulta opcional/não-bloqueante — SAS-001 §6.12).
[x] Dependências a montante homologadas (CEM/CHM/CCM/CEE/SAS/SPEC-004 v1.2/SPEC-005 v1.0/SPEC-001/019/020/021/atomic-spec v1.5); não downstream de bloqueador aberto não resolvido (H-001 é desta Spec; proposta de recorte, não fechada).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); Bloco A cobre TODAS as 13 BASpecs com efeito — obrigatório CRITICAL.
[x] CC-11/§10.6: Classe por BASpec com efeito, com critério 4Es; Classes C com gate de saída; Classe H (CKG-008) com bounded loop + gate de saída.
[x] Abertura (RULE-ECC-01/02/04/06): Dossiê presente e HOMOLOGADO (DHR-SPEC006-001); verbatim em sources/; repositórios em research.md §5; escopo/quantidade/número homologados (1 Spec).
[x] Passo 11-bis: nenhum item com gatilho spec:SPEC-006 isolado; BL-003/BL-010/BL-011/BL-029 tratados (não promovidos — Andraus/gate).
[ ] Gate determinístico (validate_spec_sot.py), check_repo_research.py, build_map.py --check e check_doc_sync.py: **NÃO executáveis por mim (sem Bash)** — reportados ao caller (execução no ambiente pai — Orquestrador). Ver relatório final.
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] / abertas nesta Spec (não fechadas — CONS-01):
- **H-001** — "Knowledge Graph: grafo real ou estrutura em memória?": a SPEC-006 é a dona e **propõe o recorte** (contrato cognitivo fechável com mecanismo físico INDETERMINADO — Opção A), mas **não fecha** — decisão de Andraus. Permanece ABERTA.
- **Opção B (banco de grafos dedicado)** — ADIADA (registrada, não apagada — INV-07; adotável só se Andraus fechar H-001 como "grafo real").
- **Escala de confiança de relação** — PARÂMETRO a calibrar (INDETERMINADO; sem número arbitrário; não toca J-001/N-001).
- **Componente "Cognitive Ontology" separado** — não criado; ontologia DENTRO da SPEC-006 (Q-ABERTURA-4); criar componente é de Andraus.
- **M-001** (estados do Blackboard p/ objetos não-hipótese) — fronteira (SPEC-004); não tocada, permanece ABERTA.
- **J-001 / N-001** (fórmula/pesos/limiares definitivos do Conviction Vector / pesos por ativo) — o KG não computa convicção; não tocadas, permanecem ABERTAS.
- **G-001 / K-001** (estado por agente / ciclo de evolução P12) — fronteiras (SPEC-009/018); não tocadas, permanecem ABERTAS.
- **C-001** (granularidade EARS multi-condição) — relevante a relações multi-condição; não fechada.
- **WF-D03 / ECC-03-001** — não tocadas; permanecem ABERTAS.

Carregado para o Revisor:
- Cobertura × lacuna (canônicos/SPEC-004/005) com arquivo:linha — a SPEC-006 **não duplica** linhagem/versões/estados/proveniência/append-only (herdados por ID+versão; CC-08); a lacuna real = ontologia enxuta + catálogo de entidades/relações + temporalidade + confiança de relação + consulta cognitiva + governança de escrita.
- Baselines que citam o KG tratadas **sem erratum** (número/nome preservados): CEM-001 l.494/562-565/608-615/699, SAS-001 §6.12/l.163, CONSTITUTION l.233, CEE-001 l.111 (research.md §6.4; INV-09).
- **H-001** apresentada como **[DECISÃO NECESSÁRIA]** — recorte proposto (contrato cognitivo fechável; mecanismo físico INDETERMINADO), **não** fechada — decisão de Andraus; fundamento histórico rejeita "banco de dados" (research.md §0).
- Imutabilidade/não-deleção = **E3 fail-closed** (EC-CKG-002); governança de escrita = **E3 fail-closed** (EC-CKG-003); falso-DENY E3 CONDICIONAL até o limiar (gap aberto, ENF-07).
- Confiança de relação **≠ Convicção** (INV-04) — isolada do Conviction Vector (CKG-007/EC-CKG-004); não toca J-001/N-001.
- Causalidade sob **RULE-CAU-01** — mecanismo obrigatório, não pós-hoc (CKG-008/EC-CKG-005; Classe H com bounded loop + gate de saída).
- Possível risco de volume (CRITICAL, 13 BASpecs): se o Revisor/Andraus julgar que o Plan excede uma sessão de revisão, a divisão é decisão de Andraus (Q-ABERTURA-5) — o Especificador **não** divide por conta própria; slot preservado (INV-07).
