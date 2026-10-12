# SPEC-006 — Cognitive Knowledge Graph

| Campo | Valor |
|---|---|
| ID | SPEC-006 — Cognitive Knowledge Graph (contrato cognitivo da **memória semântica permanente** do SOT — ontologia enxuta + entidades/relações tipadas + temporalidade + proveniência por referência + lifecycle + confiança de relação + consulta cognitiva + governança de escrita; **mecanismo físico de armazenamento INDETERMINADO — H-001 ABERTA**) |
| Versão | 1.3 (candidato a BASELINE) |
| Status | **CANDIDATO — aguarda verificação de spec (checks.md), gate determinístico, parecer do Revisor e homologação de Andraus.** NÃO é baseline (INV-09). Abertura HOMOLOGADA: DHR-SPEC006-001 (2026-10-11). As RULE-CKG-* e o contrato de nó/relação deste Plan são **[PROPOSTA]** até homologação. **H-001 (mecanismo físico do KG) permanece ABERTA — este Plan NÃO a fecha** (CONS-01; só Andraus). M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 seguem ABERTAS. |
| Fonte | ROADMAP §6 (FASE 3); `specs/features/SPEC-006/ABERTURA.md` + `research.md` + `sources/` (Dossiê — RULE-ECC-01/02/04/06; validade CRITICAL 90 dias, limite 2027-01-03); DHR-SPEC006-001; atomic-spec **v1.5** (§3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7); `governance/RULES.md` (RULE-BB-004, RULE-CAU-01/02/03, RULE-MECH-01, RULE-HD-02/03/04); `canon/CEM-001` (Responsabilidades do KG l.608-615), `canon/CHM-001`, `canon/CCM-001`, `canon/CEE-001` l.111, `canon/SAS-001` §6.12; `WORKFLOW.md` (conformidade, não editada) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §6 "P0 — CRITICAL"; atomic-spec §3 (emenda SPEC006-MATRIZ, 2026-10-05) "Knowledge Graph \| CRITICAL \| D0–D7"; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profundidade-alvo | **D0–D7 + D8 adversarial focado** nos pontos sensíveis (imutabilidade INV-07, confiança de relação ≠ Convicção INV-04, causalidade pós-hoc RULE-CAU, colisão de relações, governança de escrita), **sem elevar o profile em silêncio** — mesma reconciliação da SPEC-004 (CRITICAL, pin D0–D7, homologada "D0–D7 + D8 adversarial") [FONTE: ROADMAP §6; AGENTS.md §4; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 3 — MEMÓRIA SEMÂNTICA E RAG; próxima na sequência após SPEC-005 (BASELINE v1.0, DHR-SPEC005-002). Opera **sobre** conhecimento já validado/publicado; a formação/retrieval é SPEC-007 (não absorvida) [FONTE: ROADMAP §6/§21] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3 teto spec-first; gate normativo E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01 (Classe por BASpec); RULE-PD-01/CC-12 **(N/A — infraestrutura de memória, agnóstica de escola)**; RULE-ECC-04 (verbatim); RULE-ECC-06 (repositórios); RULE-ECC-05 **(N/A — não toca comportamento de trading)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — **D** (ontologia/catálogo de entidades-relações, temporalidade, versionamento, consulta estruturada, Cognitive Trace Reconstruction) + **C** (governança de escrita, imutabilidade/append-only INV-07, proveniência obrigatória, confiança≠Convicção INV-04, fronteira "só conhecimento publicado") + **H** (juízo de similaridade/causalidade com gate de saída e mecanismo declarado — RULE-CAU); declaração normativa é **por BASpec** (SES-001 §50) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-12 |
| Abertura | Dossiê de Pesquisa HOMOLOGADO por Andraus (DHR-SPEC006-001, `research.md`); Plan iniciado dentro da validade do Dossiê (CRITICAL → 90 dias; limite 2027-01-03; ECC-VAL-001 FECHADA, DHR-DEC-003) |

Complexidade: CRITICAL. Profundidade-alvo: D0–D7 + D8 adversarial focado (standard + adversarial).

**Princípio fundador desta Spec (transversal):** **MEMÓRIA PERMANENTE ≠ MEMÓRIA DE TRABALHO.** *"Blackboard ↓ memória de trabalho. Knowledge Graph ↓ memória permanente. Nunca misturar."* (fundamento KERNEL-V2; ROADMAP §5/§6). O KG é a **representação semântica permanente do conhecimento já validado e suas relações auditáveis** — não é "banco de grafos" (o fundamento-fonte rejeita "banco de dados"; research.md §0) e não é memória de trabalho (SPEC-004). Este Plan define **o QUE** (contrato cognitivo), com o **mecanismo físico de armazenamento declarado INDETERMINADO = H-001 (ABERTA)** — grafo real vs. estrutura em memória vs. tabelas+índice é decisão de engenharia de Andraus, não fechada aqui. [FONTE: ROADMAP §6; DHR-SPEC006-001 Q-ABERTURA-3; research.md §0/§8]

**Status epistemológico de cabeçalho:** a SPEC-006 é a **camada Harness/operacional da memória permanente** sobre responsabilidades que os modelos canônicos BASELINED já atribuem ao KG (CEM-001 l.608-615; l.494; l.562-565 Cognitive Trace Reconstruction; CONSTITUTION l.233 EC-COG-003; SAS-001 §6.12; CEE-001 l.111). **NÃO redefine** CHM-001, CEM-001, CCM-001, nem reabre SPEC-004/SPEC-005 (**CC-02/CONST-01/INV-09**). **H-001** permanece **ABERTA** — este Plan **propõe** o recorte (contrato cognitivo fechável com mecanismo físico INDETERMINADO), não o fecha (decisão de Andraus; CONS-01). [FONTE: ROADMAP §6/§7; atomic-spec §12; DHR-SPEC006-001 §3]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-10-11 | Entrega candidata inicial (Opção A; mecanismo físico INDETERMINADO = H-001). 13 BASpecs (CKG-001..013); 6 EC; 13 EARS; 11 cenários; 10 adversariais. |
| 1.1 | 2026-10-12 | **Rodada 2 (achados do gate, do Revisor e verificados no repositório).** (A) STRUCT-10: removida toda forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta. (B1) §7-bis Bloco C ampliado a todas as N8–N17. (B2) SRC-FORGET-01 declarada sem sustentar alegação carregada sozinha. (B3) EC-CKG-002 registra tentativas de DELETE bloqueadas. (B4) falha de auth da SPEC-004 ⇒ não-autorizado (fail-closed). (C1) escrita permanente elevada a **E3** (atomic-spec §10.2); "piso E2" eliminado. (C2/C9) **duas fontes de entrada** reconciliadas sob uma trilha de governança única; preservação de REFUTED/SUPERSEDED/ARCHIVED declarada; selo de publicação = dependência de SPEC-007 [DECISÃO NECESSÁRIA]. (C3) Cognitive Trace Reconstruction = obrigação **completa** (independe de H-001); T10 ampliado a 3 saltos. (C4) tipo de relação **DERIVA_DE** (aresta de Lineage) acrescentado, separado de `provenance_ref`. (C5) matriz de integridade tipo×origem/destino×direcionalidade/simetria + "família estrutural" + teste de violação. (C6) invalidação/supersessão como **novos registros**; estado = projeção derivada (espelha SPEC-004 INV-CBP-01). (C7) schema com `version`/`supersedes`/selo/escritor/colisão; REJECTED/CANDIDATE_WRITE = estados transitórios (não persistidos). (C8) BL-029 corrigido para **`Em espera`**. (C13) critérios de SUPERSEDED×INVALIDATED_IN_TIME×ARCHIVED, correção/reativação, rebaixamento, autoridade de arquivamento. (C14) `recorded_at` acrescentado à relação (bitemporal real). (C17) RULE-CAU-02 (regime) e RULE-CAU-03 (marcador pós-hoc) incorporadas; atribuição pós-hoc corrigida; gate causal só verifica presença. (C18) node_type **observation** (INV-06). (C21) emissão de evento pelo KG **removida** (só consome); emissão = [DECISÃO NECESSÁRIA] dependente da SPEC-005. (C22) governança/versionamento da ontologia definida (spec-time SPEC-019; runtime K-001 [DECISÃO NECESSÁRIA]). Extra: `gate_record` reatribuído à SPEC-004 (não CEM-001). Cobertura: 13 BASpecs; 6 EC; 13 EARS; 13 cenários (T01..T13); **15 adversariais** (ADV-CKG-01..15). |
| 1.2 | 2026-10-12 | **Rodada 3 (defeitos confirmados por revisão independente, verificados no repositório).** (1) Matriz §D2.1: HERDA = sub→pai pelo `parent_id` (SPEC-001)/`parent_hypothesis_id` (CHM-001), inclusive **entre escolas** (SMC/Fibonacci SUB → Elliott PRIMARY — SPEC-001 RULE-HH-003 l.104; CONSTITUTION l.193); "família estrutural" só restringe sub-hipóteses intra-escola; ORIGINA: origem ∈ {Elliott, SMC, Fibonacci}, nunca ICT (INV-02); atributo `school`/`origin_agent` (por referência ao canônico); o KG só **espelha**, não decide, a autoridade de criação (CC-01). (2) `lineage_ref` (campo inexistente) → `provenance_ref.lineage` [PROPOSTA] = referência ao campo `Lineage` (CEM-001 l.351/359/539-554) / `derived_from[]` (SPEC-004). (3) Preservação de estado canônico: `canonical_status` (snapshot) + registro `canonical_state_transition` (estado/timestamp/origem/justificativa — CEM-001 l.428); estados do KG ≠ estados canônicos (CC-10). (4) Critério de admissão Blackboard→KG do caminho (a) = [DECISÃO NECESSÁRIA] (promoção trabalho→permanente — SPEC-018/K-001). (5) Completude do trace garantida: admitir evidence DERIVED ⇒ exigir aresta DERIVA_DE por ancestral do Lineage (fail-closed); trace ignora validade e é acíclico (INV-CKG-02); teste negativo. (6) INV-04 = só custo; proibição de *confiança* entrar na convicção = regra LOCAL [PROPOSTA] (CKG-007); matriz restringe CAUSA (destino `conviction` proibido a partir de custo/confiança); restrição à SPEC-003 = requisito a ela endereçado/[DECISÃO NECESSÁRIA]. (7) Invalidação de relação = ato AUTORIZADO (CKG-009), **não** automática (CEM-001 l.602 "não implica cascata"; impacto é de CHM/CCM — l.503/606; CHM-001 l.672-676); consumo de evento = [INFERÊNCIA]/[DECISÃO NECESSÁRIA] (SPEC-005 não define "Evidence Invalidated"). (8) Schema: `record_kind`, `relevance`, `target_relation_id`, identidade para nós não-canônicos, `collision_record` como registro. (9) "conhecimento permanente/temporário" tratado/diferido (SPEC-018/K-001 [DECISÃO NECESSÁRIA]). (10) CONFIRMA/REFUTA restritas a `evidence` (INV-06; CONSTITUTION l.191). (11) Bitemporal: consulta valid-time + transaction-time (as-of-registro). (12) Citação RMR-001 → l.128/l.192. (13-18) correções menores. Contagem: 13 BASpecs; 6 EC; 13 EARS; **14 cenários** (T01..T14); **16 adversariais** (ADV-CKG-01..16); 2 invariantes locais (INV-CKG-01/02). |
| 1.3 | 2026-10-12 | **Rodada 4 (6 Maiores do controle, confirmados no repositório).** (1) **T01 corrigido** (a v1.2 NÃO o havia reescrito): T01 agora usa ORIGINA com `school=ICT` (caso que a matriz DE FATO rejeita) + novo **T15 positivo** HERDA SMC-SUB → Elliott-PRIMARY (RULE-HH-003). (2) **Campos unificados:** um só campo `school` (eliminado "origin_agent"); adicionado `hierarchy_role` {PRIMARY,SUB} (ref. SPEC-001); "família" COMPUTADA via `school`+PERTENCE_A(asset,timeframe); regra de nó `hypothesis.school ≠ ICT` (INV-02/RULE-HH-004) com teste (T01) e **ADV-17**; HERDA.pai restrito a `hierarchy_role=PRIMARY`. (3) **gate_record CONDICIONAL** (espelha SPEC-004 CBP-007): `computed_by`/`writer_id` SEMPRE obrigatório; `gate_record` só se há gate; `lineage`/`derived_from` só se derivado; `[]` legítimo (PRIMARY/asset/timeframe/regime/observation); CKG-005/T12/T14/schema ajustados. (4) **SPEC-005/Evidence.Invalidated corrigido:** o tipo é canônico (CEM-001 l.600/722) e a SPEC-005 o TRANSPORTA (l.88/859); o que falta é o consumidor/contrato de consumo pelo KG = [DECISÃO NECESSÁRIA] (linhas l.115/242 — que eram o envelope — removidas). (5) **CKG-013/colisão:** tabela de pares contraditórios §D2.2 (CONFIRMA×REFUTA; INVALIDA×relação-alvo) + escopo (mesmos from/to + sobreposição de validade) + algoritmo D4 + teste negativo **ADV-18** (origens distintas/validades disjuntas não colidem). (6) **CKG-010/admissão:** gate (a) declarado NÃO-ESPECIFICADO/INDETERMINADO (não vacuoso) + [PROPOSTA] de critério mínimo (estados ACTIVE/DOMINANT/SUPERSEDED/REFUTED/ARCHIVED; exclui EMERGENT/CANDIDATE); reatribuição de S14 à SPEC-018/K-001 submetida a Andraus [DECISÃO NECESSÁRIA]; ordem de admissão de ancestrais (`PENDING_ANCESTOR`, sem deadlock de INV-CKG-02). Histórico reordenado 1.0→1.3. Contagem: 13 BASpecs; 6 EC; 13 EARS; **15 cenários** (T01..T15); **18 adversariais** (ADV-CKG-01..18); 2 invariantes locais. |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; DHR-SPEC006-001 §3/§4; DHR-SPEC006-PEND-001; ABERTURA §8/§9; RMR-001 l.128 (linha do BL-029) / l.192 (DHR-SPEC006-PEND-001)]

- **Nenhum item do RMR-001 tem gatilho `spec:SPEC-006` homologado isoladamente.** O início da redação deste Plan **satisfaz ramos de gatilho** de itens pré-existentes — **tratados aqui como reflexo; a promoção/encaminhamento é do gate e de Andraus** (o Especificador NÃO promove — CONS-01).
- **BL-003** (persistência física de hipótese/estado) — `Em espera`, gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação`. A redação deste Plan **satisfaz** o ramo `spec:SPEC-006`. **Encaminhamento:** a parte **física** do BL-003 **É** H-001 (ABERTA) / G-001 (ABERTA) → a SPEC-006 **referencia**, **não absorve** (CONS-01). Precedente SPEC-004: "em redação" lido como disparo no início do Plan (DHR-SPEC004-001) — registro e deixo a promoção a Andraus/Controlador (fail-closed).
- **BL-011** (MC-EXP-001, Master Contract da Camada de Experiência e Memória) — `Em espera`, gatilho inclui `spec:SPEC-006 em redação`. **Fonte de requisitos** de SPEC-004/006/009/018. **Encaminhamento:** usar como **insumo de requisitos** (ref. externa K-MAN-15) sob os tratamentos COL-EXP-01..05 já homologados (CONFLICT-MAP; prevalece SOT canônico; imutabilidade REFORÇA RULE-BB-004/INV-07). Classificação ≠ aplicação; **não promovo**.
- **BL-010** (MC-RAG-001) — `Em espera`, gatilho `spec:SPEC-007 em redação` ∨ `milestone:FASE 3 iniciada`. A FASE 3 é iniciada, mas BL-010 é fonte de requisitos da **SPEC-007** (não da 006) → **tangente**; a SPEC-006 respeita a fronteira (recebe conhecimento publicado; formação/retrieval é SPEC-007). **Não promovo** (gate/Andraus decidem o ramo `milestone`).
- **BL-029** (proveniência/"LLM propõe, harness recomputa") — **`Em espera`** (Andraus, chat 2026-10-05, DHR-SPEC006-PEND-001: devolvido a `Em espera`; gatilho `spec:SPEC-014`/`SPEC-018`/`SPEC-045`; o gatilho `spec:SPEC-004` foi CONSUMIDO; camada de proveniência já materializada na SPEC-004 v1.2). **Independente desta Spec** (não dispara em `spec:SPEC-006`) — não absorvido nem promovido aqui. [FONTE: RMR-001 l.128 (linha do BL-029, estado `Em espera`) / l.192 (DHR-SPEC006-PEND-001); a l.191 é a errata do BL-003, não do BL-029] *(Correção v1.1: a v1.0 dizia `ATIVADO` — incorreto.)*
- O passo 11-bis pleno ocorre na homologação do Plan.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o Knowledge Graph é **infraestrutura de memória agnóstica de escola** — **armazena** conhecimento de qualquer camada analítica (inclusive a relação `HERDA`/`HIERARQUIA_DE`) **sem** alterar a hierarquia nem a autoridade de criação de hipótese (Elliott cria a primária; ICT não cria — INV-01/INV-02). O KG representa a hierarquia como relações; não a redefine, não interpreta, não decide. [FONTE: INV-01/INV-02; ROADMAP §6]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM) nem SPEC-004/005:** **foco.** O KG **preserva** linhagem/versões/estados e faz *Cognitive Trace Reconstruction* **referenciando** os contratos canônicos (CEM-001 l.608-615; l.562-565) — entidades são **referenciadas por ID+versão, nunca redefinidas**. Não reabre a memória de trabalho (SPEC-004, BASELINE) nem o transporte (SPEC-005, BASELINE). CDM-001/CNM-001 pendentes não acionam CONST-01. [FONTE: CC-02; CEM-001 l.608-615; CHM-001; CCM-001; SPEC-004/005 BASELINE]
- [x] **CC-03 — Conviction Vector:** o KG **não computa** convicção — a **"confiança de relação"** do KG é escala própria da memória e **NÃO é** o Conviction Vector; dimensionalidade=8 (fechada) intocada; a fórmula/pesos/limiares definitivos do Conviction Vector permanecem **pendentes (J-001 ABERTA)** e **não** são tratados aqui; **nenhum limiar numérico de convicção é declarado neste Plan**. [FONTE: INV-03; J-001 ABERTA; N-001 ABERTA]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. O KG não emite sinal de trading, não dimensiona risco, não aplica gates de sinal. **INV-04** (custo nunca entra no Conviction Vector — Convicção ≠ Score) preservado por construção: a confiança de relação do KG **nunca** retroalimenta nem redefine o Conviction Vector; custo/score nunca entram em convicção (CKG-007; ADV-CKG-05). [FONTE: CEE-001 §10/§11; INV-04]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D7 + D8 adversarial focado (ROADMAP §6; atomic-spec §3 emenda SPEC006-MATRIZ; DHR-SPEC006-001 Q-ABERTURA-2).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card; §59/§60 tornam-se obrigatórios nas Tasks/Cards (BUILD adiado — atomic-spec §14). Omissão justificada.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem: ROADMAP §6 → Dossiê (research.md, HOMOLOGADO DHR-SPEC006-001) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED com ID+versão (RULE-HD-04); REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Mapa de cobertura×lacuna com arquivo:linha incluído. Eixo VERTICAL (RULE-HV) avaliado e declarado não aplicável. [FONTE: EUA-E04 §8.3; RULE-HD-02/03/04]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI):** aplicado — **mecanismo físico do KG = INDETERMINADO (H-001 ABERTA)**, não como fato; **relações causais exigem mecanismo + regime declarados (RULE-CAU-01/02) e marcador pós-hoc (RULE-CAU-03)** (CKG-008); **sem falsa precisão em "confiança de relação"** (escala sem número arbitrário até calibração); fontes web = DADO [EXTERNO] (research.md §2); SRC-FORGET-01 é DADO não-verbatim e não sustenta sozinha nenhuma alegação carregada (§7-bis Bloco C). [FONTE: RULE-EPI-01..03; RULE-CAU-01/02/03; research.md §8]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM-01):** **INCIDE e tratado** (ver "Declaração de acepção semântica"): **"Conhecimento permanente"** (KG) vs **"memória de trabalho"** (Blackboard/SPEC-004) vs **"documento recuperado"** (RAG/SPEC-007) vs **"Observação"** (Skill — INV-06); **"confiança de relação"** (KG) vs **"Convicção"** (CCM-001); **"esquecimento"** (= arquivamento versionado, nunca deleção — INV-07); **estados do KG** (SUPERSEDED/ARCHIVED/INVALIDATED_IN_TIME — projeção derivada) vs **estados canônicos homônimos** (CHM/CEM — rastreados à parte em `canonical_status`). Nenhum termo canônico do GLOSSARIO redefinido (RULE-SEM-04). [FONTE: RULE-SEM-01/04; INV-06; GLOSSARIO]
- [x] **CC-11 — Classe/Mecanismo por BASpec com efeito (RULE-MECH-01):** **INCIDE** — cada BASpec com efeito declara Classe (D/C/H) com critério 4Es; Classes C/H declaram gate de saída determinístico; Classe H declara bounded loop + critério de parada (CKG-008). Declaração por BASpec, nunca por Spec inteira (SES-001 §50). Ver §D3. [FONTE: RULE-MECH-01..04; atomic-spec §9/§10.6]
- [x] **CC-12 — Princípios de Domínio `PD-xx` (RULE-PD-01):** **N/A — não incide** (DHR-SPEC006-001 §2; ABERTURA §6; research.md §7). O KG é **infraestrutura de memória agnóstica de escola**. Mesmo padrão N/A de SPEC-002/004/005. Registrado explicitamente, não supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7; DHR-SPEC006-001 §2]

**Disciplinas cognitivas N8–N17 incidentes (RULES.md v1.5):** RULE-EPI (H-001 ABERTA ≠ fato; mecanismo físico INDETERMINADO), RULE-CAU-01/02/03 (relação causal exige mecanismo + regime; marcador pós-hoc — CKG-008), RULE-MET-01 (não-fabricação — nenhuma escala/limiar de confiança fabricado; IDs arXiv implausíveis descartados, research.md §aviso), RULE-UNC-01..03 (incerteza localizada sobre eficiência de consulta multi-salto ampla enquanto H-001 ABERTA — não sobre a completude do trace), RULE-SEM-01/04 (acepções), RULE-DEC-01 (o KG **armazena/relaciona/consulta**, não decide nem executa — INV-05). INDETERMINADO usado onde há incerteza material. (Demais disciplinas tratadas no §7-bis Bloco C.)

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-006

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - canon/CEM-001 (BASELINE) — Responsabilidades do Knowledge Graph (l.608-615): preservar toda a linhagem;
    preservar TODAS as versões; preservar TODOS os estados; fornecer Cognitive Trace Reconstruction COMPLETA a
    partir das relações de Lineage; permitir navegação completa da cadeia cognitiva. Também: l.494 ("Knowledge
    Graph | Todos os estados — preservação permanente"); l.562-565 (Cognitive Trace Reconstruction = capacidade
    do KG); l.699 (KG = mecanismo oficial de Cognitive Trace Reconstruction do ecossistema). O KG CUMPRE essas
    responsabilidades integralmente; NÃO redefine o CEM (CC-02/INV-10). Proveniência: o campo LOCAL
    `provenance_ref.lineage` [PROPOSTA] REFERENCIA o campo `Lineage` do CEM-001 (Cap.5; l.351/539-554) e/ou
    `derived_from[]` da SPEC-004 — NÃO existe campo `lineage_ref` no CEM-001 (nome local desta Spec);
    `gate_record`/identidade autenticada são da SPEC-004 v1.2 (NÃO do CEM-001)
  - canon/CHM-001 (BASELINE) — máquina de estados da hipótese (EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→
    REFUTED→ARCHIVED) e versionamento append-only; o KG ARMAZENA/relaciona hipóteses como nós por referência,
    preservando TODOS os seus estados (inclusive REFUTED/SUPERSEDED/ARCHIVED — CEM-001 l.494); NÃO cria nem
    transiciona estado de hipótese (isso é SPEC-001/CHM-001)
  - canon/CCM-001 (BASELINE) — objeto Conviction Vector 8D; o KG pode armazenar o valor como propriedade de nó
    (por referência), mas a "confiança de relação" do KG é escala PRÓPRIA e NUNCA é o Conviction Vector (INV-04)
  - specs/features/SPEC-004 v1.2 (BASELINE — DHR-SPEC004-003) — memória de TRABALHO (Blackboard); append-only REAL:
    supersessão = PROJEÇÃO DERIVADA (registro histórico NUNCA mutado; sucessora carrega `supersedes`; INV-CBP-01,
    RULE-CBP-003; plan l.230-234/l.324/l.371); proveniência `computed_by`/`gate_record`/identidade autenticada
    (BL-029 materializado na v1.2). FRONTEIRA: o KG é memória PERMANENTE, distinta ("Nunca misturar"); HERDA a
    mecânica append-only-por-novos-registros e a identidade autenticada por referência; NÃO redefine o contrato (CC-02/INV-09)
  - specs/features/SPEC-005 v1.0 (BASELINE — DHR-SPEC005-002) — notificação de mudança (Event Bus); **[INFERÊNCIA]** o KG
    pode CONSUMIR eventos de ciclo de vida apenas como GATILHO de avaliação autorizada (CKG-009), nunca como invalidação
    automática (CEM-001 l.602). O tipo `Evidence.Invalidated` É canônico (CEM-001 l.600/l.722) e a SPEC-005 o **TRANSPORTA**
    (SPEC-005 plan l.88 e l.859 `event_type`); o que a SPEC-005 **NÃO define** é o **consumidor** nem o **contrato de consumo
    pelo KG** — isso é **[DECISÃO NECESSÁRIA]**; a SPEC-005 fonta eventos do LOG do Blackboard (source_ref = object_id@version+seq+workspace)
    e NÃO escreve no KG (SPEC-005 plan l.242/l.971). A EMISSÃO de eventos "conhecimento mudou" ORIGINADOS no KG NÃO é
    afirmada aqui (a SPEC-005 fonta do log do Blackboard) — [DECISÃO NECESSÁRIA] (erratum
    aditivo futuro à SPEC-005, se desejado; não proposto nesta Spec)
  - canon/CEE-001 (BASELINE) l.111 — a métrica de calibração do roteamento de modelo "entra no Knowledge Graph";
    o KG ARMAZENA essa métrica como nó (por referência), ISOLADA do Conviction Vector (INV-04); não a computa
  - canon/SAS-001 §6.12 (l.923-924) — Integração com Knowledge Graph: o agente atua EXCLUSIVAMENTE como PRODUTOR;
    pode registrar relações fractais/temporais/estruturais/de causalidade estrutural; NÃO pode redefinir ontologias
    nem alterar taxonomias globais. FUNDAMENTA a governança de escrita (CKG-009); herdado como fronteira, não redefinido.
    (l.163 EC-COG-003: KG "consultado quando necessário… não é pré-requisito obrigatório")
  - governance/CONSTITUTION.md l.233 (EC-COG-003 — "Knowledge Graph | Memória relacional de padrões"): âncora
    constitucional; conformar-se, não reescrever (INV-09)
  - governance/RULES.md: RULE-BB-004 (append-only; objetos SUPERSEDED, nunca deletados — l.323) — REFORÇADO pelo KG
    como imutabilidade permanente (INV-07); RULE-CAU-01 (afirmação causal DEVE declarar mecanismo — l.680),
    RULE-CAU-02 (regime/condição de validade — l.681), RULE-CAU-03 (explicação pós-hoc marcada como tal — l.682) —
    incidem sobre as relações CAUSA do KG (CKG-008)
  - Método: atomic-spec.md v1.5 (BASpec, D0–D9, EARS, Enforcement E0–E3/F.1–F.4 — §10.2 "KG publicado → E3 mínimo",
    TRACE-06, Quality Gates L1–L4 §7, Classe/Mecanismo §10.6, RULE-MM; §3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7)
  - Governança/Avaliação/Maturidade: SPEC-019 v1.0 (RULE-HG-01..08, RULE-HV-01..04 — governança spec-time do harness).
    **[INFERÊNCIA]** a alteração da ONTOLOGIA do KG seria ato de governança análogo (RULE-HG) — a SPEC-019 **não** cita
    "ontologia" literalmente (0 ocorrências); runtime = K-001 [DECISÃO NECESSÁRIA]. SPEC-020 v1.0 (9 lentes); SPEC-021 v1.0 (RULE-MM; nível-alvo L3; gate E3)
  - Enforcement: ENF-01..08 (ênfase ENF-03 Detector≠Gate; ENF-04 fail-closed; ENF-07 falso-DENY no E3)
  - Invariantes: INV-04 (**custo** nunca no Conviction Vector — Convicção ≠ Score; atomic-spec l.404/AGENTS §6.8); a
    proibição de **confiança de relação** entrar na convicção é regra LOCAL [PROPOSTA] desta Spec (CKG-007), NÃO cláusula de INV-04), INV-05 (SOT não executa ordem), INV-06
    (Evidência≠Observação), INV-07 (versionamento monotônico — refutado/arquivado NUNCA deletado), INV-09 (sem
    baseline informal), INV-10 (CEM-001 idioma canônico da Evidência)
  - Setup operacional (fronteira soberana, NÃO redefinida): WORKFLOW.md — o KG é a memória de longo prazo consultada
    na formação de contexto; cita por ID os WF-xx que toque, NÃO contradiz nenhum WF-xx e NÃO fecha WF-D03

ADDED (delta local — o que esta spec acrescenta; NÃO coberto pelos canônicos/SPEC-004/005 — ver "Cobertura × lacuna"):
  - Ontologia ENXUTA do KG (DENTRO da SPEC-006 — Q-ABERTURA-4): tipos de ENTIDADE e de RELAÇÃO permitidos + MATRIZ
    de integridade (tipo × origem/destino × direcionalidade/simetria) — a "gramática do conhecimento"; rejeita violação
  - Catálogo de ENTIDADES (nós) por referência aos canônicos (inclui `observation` — INV-06, distinta de `evidence`)
  - Catálogo de RELAÇÕES tipadas: CONFIRMA, REFUTA, DEPENDE_DE, HERDA, PERTENCE_A, INVALIDA, ORIGINA, DERIVA_DE
    (aresta de Lineage — separada de `provenance_ref`), SIMILAR_A (simétrica), CAUSA (sob RULE-CAU-01/02/03),
    HIERARQUIA_DE, ESTATISTICA_DE
  - TEMPORALIDADE BITEMPORAL das relações: `valid_from`/`valid_to` (tempo de validade) + `recorded_at` (tempo de
    registro) — invalidação/mudança por NOVO registro, nunca mutação (espelha SPEC-004 INV-CBP-01)
  - PROVENIÊNCIA obrigatória por entidade/relação (`provenance_ref.lineage` [PROPOSTA] → `Lineage` CEM-001 / `derived_from[]` SPEC-004; `gate_record` SPEC-004); rejeita sem proveniência
  - IMUTABILIDADE / append-only permanente: estado = PROJEÇÃO DERIVADA; "esquecimento" = arquivamento versionado, NUNCA deleção (INV-07)
  - CONFIANÇA de relação — escala PRÓPRIA, ≠ Convicção (INV-04); nunca retroalimenta o Conviction Vector
  - Relações de SIMILARIDADE/CAUSALIDADE com juízo + gate de saída (mecanismo+regime+pós-hoc — RULE-CAU-01/02/03)
  - GOVERNANÇA de escrita (E3): quem escreve, identidade autenticada (reusa SPEC-004; falha de auth ⇒ não-autorizado),
    produtor registra relações mas NÃO redefine ontologia/taxonomia (SAS-001 §6.12); governança da ONTOLOGIA (spec-time
    SPEC-019; runtime K-001 [DECISÃO NECESSÁRIA])
  - FRONTEIRA de entrada em DUAS fontes sob UMA governança: (i) objetos canônicos e suas transições via ciclo de vida
    canônico (preserva TODOS os estados); (ii) conhecimento FORMADO via selo de publicação da SPEC-007 [DECISÃO NECESSÁRIA]
  - CONSULTA cognitiva (read-only) + Cognitive Trace Reconstruction COMPLETA (obrigação, independe de H-001)
  - LIFECYCLE do nó/relação (estado = projeção derivada; SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED distinguidos; correção/reativação)
  - DETECÇÃO e registro de COLISÃO de relações (não resolve em silêncio; versiona)
  - Declaração de Classe/Mecanismo por BASpec (CC-11); Enforcement Contracts (EC-CKG-001..006)
  - [PROPOSTA de recorte] contrato cognitivo FECHÁVEL com mecanismo físico INDETERMINADO — NÃO fecha H-001 (decisão de Andraus)

MODIFIED (especialização de regra herdada):
  - RULE-BB-004 (append-only do Blackboard) é REFORÇADA, não alterada, como imutabilidade PERMANENTE do KG (INV-07) —
    eixo permanente, não trabalho; texto/significado inalterados (RULE-HD-02 respeitada)

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal / obrigação-a-
> obrigação** sobre modelos canônicos, as SPEC-004/005 vizinhas e regras (EUA-E04 §8.3). O eixo **VERTICAL** (RULE-HV,
> conservação-como-conjunto pai→filha macro-harness) foi avaliado e **não se aplica**: a SPEC-006 deriva de canônicos,
> Specs vizinhas e regras, não é decomposição *micro* de uma *macro-spec*. [INFERÊNCIA — a confirmar pelo Revisor]

### Cobertura × lacuna (canônicos / SPEC-004 / SPEC-005) — não duplicar (CC-02/INV-09)

| Capacidade | Coberta por canônico/Spec BASELINED? (arquivo:linha) | Tratamento na SPEC-006 |
|---|---|---|
| Preservar linhagem/versões/**todos os estados**; Cognitive Trace Reconstruction completa | **SIM (responsabilidade atribuída)** — CEM-001 l.494/608-615; l.562-565 | **ESPECIFICAR** como comportamento verificável (CKG-011/004/012); referencia CEM, não redefine |
| Máquina de estados da hipótese | **SIM** — CHM-001 | **HERDADA** — o KG armazena por referência, preservando REFUTED/SUPERSEDED/ARCHIVED; não transiciona |
| Append-only REAL (supersessão = projeção derivada; registro nunca mutado) | **SIM** — SPEC-004 v1.2 (INV-CBP-01; plan l.230-234/l.371) | **HERDADA a mecânica** e aplicada ao KG permanente (CKG-004/006/012) |
| Memória de TRABALHO / objetos ACTIVE | **SIM** — SPEC-004 v1.2 | **FRONTEIRA** — não reabrir (CC-02/INV-09) |
| Notificação/transporte de mudança | **SIM** — SPEC-005 v1.0 | **FRONTEIRA** — o KG CONSOME eventos; emissão pelo KG = [DECISÃO NECESSÁRIA] |
| Proveniência (`provenance_ref.lineage` → `Lineage` CEM; `gate_record`/`derived_from[]` SPEC-004) | **SIM** — CEM-001 Cap.5 (campo `Lineage`); SPEC-004 v1.2 | **REFERÊNCIA obrigatória** (CKG-005); campo local [PROPOSTA], não redefine |
| **Ontologia (tipos/relações permitidas) + matriz de integridade** | **NÃO** | **LACUNA CENTRAL — ADDED** (CKG-001) |
| **Catálogo de entidades e relações tipadas (+ DERIVA_DE, observation)** | **NÃO** | **LACUNA CENTRAL — ADDED** (CKG-002/003) |
| **Temporalidade bitemporal das relações** | **Parcial** (CHM/CEM têm estados; não validade de relação) | **LACUNA — ADDED** (CKG-004) |
| **Confiança de relação (≠ Convicção)** | **NÃO** | **LACUNA — ADDED** (CKG-007; INV-04) |
| **Similaridade / causalidade (RULE-CAU-01/02/03)** | **Parcial** — RULE-CAU exige mecanismo | **LACUNA — ADDED** (CKG-008) |
| **Consulta cognitiva** | **NÃO** | **LACUNA — ADDED** (CKG-011) |
| **Governança de escrita + da ontologia** | **Parcial** — SAS-001 §6.12; SPEC-019 (spec-time) | **LACUNA — ADDED** (CKG-009; gate E3) |
| **Lifecycle do nó/relação do KG** | **Parcial** | **LACUNA — ADDED** (CKG-012) |
| **Mecanismo físico de armazenamento** | **NÃO — H-001 ABERTA** | **NÃO fechar** — decisão de Andraus (INDETERMINADO) |

---

## Declaração de acepção semântica (RULE-SEM-01 — CC-10)

> **Termo 1:** "Conhecimento permanente" (KG) = conhecimento **já validado/publicado** e suas relações auditáveis.
> **≠ "memória de trabalho"** (Blackboard — SPEC-004) = objetos vivos da análise em curso. *"Nunca misturar."*
> **Termo 2:** "confiança de relação" (KG) = escala PRÓPRIA. **≠ "Convicção"** (CCM-001). NUNCA retroalimenta o
> Conviction Vector (INV-04); custo/score nunca entram em convicção.
> **Termo 3:** "esquecimento"/"forgetting" (research.md §3.6) = **arquivamento versionado**, **NUNCA deleção** (INV-07).
> **Termo 4:** "documento recuperado" (RAG — SPEC-007) ≠ "conhecimento validado" (KG). **"Observação"** (Skill — INV-06;
> `observation` no KG) ≠ "Evidência" (Agente; `evidence` no KG): tipos de nó distintos, com regra de integridade (CKG-001).
> [FONTE: RULE-SEM-01/04; INV-04/06/07; GLOSSARIO; KERNEL-V2 (research.md §0); SPEC-004/005/007]

---

## Conformidade com o `WORKFLOW.md` (RULE-ECC-05 — determinação de NÃO-incidência)

> **Determinação: RULE-ECC-05 NÃO INCIDE sobre a SPEC-006** [FONTE: DHR-SPEC006-001 §2; ABERTURA §1/§6; research.md §7].
> A SPEC-006 **não define nem toca comportamento de agente analítico, do Conviction/Fusion Engine, do Manager (decisão)
> ou do Risk Agent** — é **infraestrutura de memória**, análoga às Specs excluídas (SPEC-002/004/005/019/020/021).
> **Por prudência confirma-se conformidade:** o KG é a memória consultada **quando necessário** (SAS-001 §6.12/l.163
> EC-COG-003 — "não é pré-requisito obrigatório"). Cita WF-xx só por ID, **não contradiz** nenhum e **não fecha** WF-D03.
> [FONTE: research.md §7; SAS-001 §6.12]

---

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide** (DHR-SPEC006-001 §2; ABERTURA §6; research.md §7). O KG é **infraestrutura de memória agnóstica de
escola** — armazena conhecimento de qualquer escola como nós/relações. Nenhum `PD-xx` é proposto (CC-12 = N/A).
Registrado explicitamente — não é supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7; DHR-SPEC006-001 §2]

---

## D0 — Missão (Intenção)

A SPEC-006 especifica **como o SOT preserva, relaciona e consulta o conhecimento permanente já validado** — definindo o
**contrato cognitivo da memória semântica permanente**: ontologia enxuta (tipos + matriz de integridade), catálogo de
entidades (nós, incl. `observation` — INV-06) e relações tipadas (incl. `DERIVA_DE` de Lineage, `SIMILAR_A` simétrica,
`CAUSA` sob RULE-CAU-01/02/03), temporalidade **bitemporal** (`valid_from`/`valid_to`/`recorded_at`), proveniência
obrigatória (`provenance_ref.lineage` [PROPOSTA] → `Lineage` CEM-001 / `derived_from[]` SPEC-004; `gate_record` SPEC-004), imutabilidade append-only (estado = projeção derivada;
"esquecimento" = arquivamento versionado — INV-07), confiança de relação (escala própria, ≠ Convicção — INV-04),
governança de escrita (E3; quem escreve; identidade autenticada), fronteira de entrada (objetos canônicos via ciclo de
vida + conhecimento formado via selo SPEC-007 [DECISÃO NECESSÁRIA]), consulta cognitiva e **Cognitive Trace
Reconstruction COMPLETA** (CEM-001 l.608-615; obrigação, independe de H-001) — preservando **memória permanente ≠
trabalho** e deixando o **mecanismo físico INDETERMINADO (H-001 ABERTA)**: define-se **o QUE**, não **o COMO**. [FONTE:
ROADMAP §6; CEM-001 l.608-615; CHM-001; SAS-001 §6.12; DHR-SPEC006-001; research.md §4]

**O que a Missão NÃO é (fronteira):**
- Não é **memória de trabalho** → **SPEC-004 (BASELINE)**. *"Nunca misturar."*
- Não **transporta/notifica** mudança → **SPEC-005 (BASELINE)**; o KG CONSOME eventos; emissão pelo KG = [DECISÃO NECESSÁRIA].
- Não **forma conhecimento** / não faz retrieval → **SPEC-007**; o KG recebe conhecimento **publicado**.
- Não define **estado persistente por agente** → **SPEC-009**; **G-001 (ABERTA)** — não tocar.
- Não especifica o **ciclo de evolução do conhecimento (P12)** → **SPEC-018**; **K-001 (ABERTA)** — não tocar.
- Não **computa** convicção → **SPEC-003/CCM-001**; **J-001/N-001 (ABERTAS)** — a confiança de relação NÃO é Convicção (INV-04).
- Não **redefine** CHM-001/CEM-001/CCM-001 nem SPEC-004/005 → **CC-02/CONST-01/INV-09**.
- Não **escolhe o mecanismo físico** → **H-001 (ABERTA — só Andraus)**; INDETERMINADO.
- Não **decide** nem **executa** ordem → INV-05/RULE-DEC-01.

**Status epistemológico:** RULE-CKG-* e o contrato de nó/relação são **[PROPOSTA]** até homologação. CEM-001, CHM-001,
CCM-001, CEE-001, SAS-001, SPEC-004 v1.2, SPEC-005 v1.0, SPEC-001/019/020/021, RULE-BB-004, RULE-CAU-01/02/03,
atomic-spec v1.5, INV-*, ENF-* são FATO NORMATIVO. Fontes externas (research.md §2) são [EXTERNO] — DADO, nunca baseline (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | **Ontologia enxuta + matriz de integridade** (tipos permitidos; tipo×origem/destino×direcionalidade/simetria); rejeita violação | KERNEL-V2 l.1488-1507 (research.md §0/§3.6); DHR-SPEC006-001 Q-ABERTURA-4 |
| S2 | **Entidades (nós) por referência aos canônicos:** hypothesis (CHM-001), evidence (CEM-001), **observation** (Skill — INV-06), conviction (CCM-001), narrative, mission, learning, asset, timeframe, regime, structure, calibration_metric (CEE-001 l.111). Nós de **construção teórica** (structure/regime/narrative — ex.: order block, liquidez) carregam `ontological_status` ∈ {observational, theoretical} (RULE-ONT-01), distinguindo entidade medida de postulada | CEM-001; CHM-001; CCM-001; CEE-001 l.111; INV-06; RULE-ONT-01 (RULES.md l.671) |
| S3 | **Relações tipadas:** CONFIRMA/REFUTA/DEPENDE_DE/HERDA/PERTENCE_A/INVALIDA/ORIGINA/**DERIVA_DE**/SIMILAR_A/CAUSA/HIERARQUIA_DE/ESTATISTICA_DE | ROADMAP §6; research.md §4; CEM-001 Cap.5 (Lineage→DERIVA_DE) |
| S4 | **Temporalidade bitemporal das relações:** `valid_from`/`valid_to` (validade) + `recorded_at` (registro); invalidar por novo registro ≠ deletar | research.md §3.1; INV-07; SPEC-004 INV-CBP-01 |
| S5 | **Proveniência obrigatória** (campo local `provenance_ref.lineage` [PROPOSTA] → `Lineage` CEM-001 / `derived_from[]` SPEC-004; `gate_record` SPEC-004); rejeita escrita sem proveniência | CEM-001 Cap.5 (campo `Lineage`); SPEC-004 v1.2; research.md §3.2 |
| S6 | **Imutabilidade / append-only permanente:** estado = projeção derivada; "esquecimento" = arquivamento versionado | INV-07; RULE-BB-004; SPEC-004 INV-CBP-01; research.md §3.6 |
| S7 | **Confiança de relação** — escala própria, ≠ Convicção; nunca retroalimenta o Conviction Vector | INV-04; research.md §4 |
| S8 | **Relações de similaridade/causalidade** com juízo + gate de saída (mecanismo+regime+pós-hoc — RULE-CAU-01/02/03) | RULE-CAU-01/02/03; research.md §8 |
| S9 | **Governança de escrita (E3) + da ontologia:** quem escreve, identidade autenticada (reusa SPEC-004); produtor não redefine ontologia/taxonomia; ontologia governada spec-time (SPEC-019)/runtime (K-001 [DECISÃO NECESSÁRIA]) | SAS-001 §6.12; SPEC-004 v1.2; SPEC-019; atomic-spec §10.2 |
| S10 | **Fronteira de entrada (duas fontes, uma governança):** objetos canônicos via ciclo de vida (preserva todos os estados) + conhecimento formado via selo SPEC-007 [DECISÃO NECESSÁRIA] | ROADMAP §6/§7; CEM-001 l.494; research.md §3.4 |
| S11 | **Consulta cognitiva (read-only)** + Cognitive Trace Reconstruction **completa** (obrigação) | CEM-001 l.608-615; SAS-001 §6.12; research.md §3.4 |
| S12 | **Lifecycle do nó/relação:** estado derivado; SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED distinguidos; correção/reativação; nunca remoção | CHM-001; INV-07; SPEC-004 INV-CBP-01; research.md §3.6 |
| S13 | **Detecção/registro de colisão de relações:** contraditórias registradas e versionadas, não resolvidas em silêncio | research.md §8; D8 |
| S14 | **Conhecimento permanente × temporário (ROADMAP §6):** o KG guarda conhecimento PERMANENTE; dentro dele, "temporário" = conhecimento com janela de validade (`valid_to`) ou `relevance` rebaixada (arquivado) — nunca deletado. O **critério de promoção trabalho→permanente** NÃO é fechado aqui; **atribuí-lo à SPEC-018/K-001 é PROPOSTA submetida a Andraus = [DECISÃO NECESSÁRIA]** (a ABERTURA só enviou à SPEC-018 o ciclo P12, não o critério de promoção — não presumir reatribuição) | ROADMAP §6; ABERTURA §35; research.md §4 (lacuna); K-001 (ABERTA) |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| **Mecanismo físico de armazenamento** | **H-001 (ABERTA — só Andraus)** | decisão de engenharia deliberadamente aberta; INDETERMINADO |
| Memória de trabalho / objetos ACTIVE | **SPEC-004 (BASELINE)** | "Nunca misturar"; CC-02/INV-09 |
| Notificação/transporte; **emissão de evento pelo KG** | **SPEC-005 (BASELINE)** | o KG consome; emissão pelo KG = [DECISÃO NECESSÁRIA] (SPEC-005 fonta do log do Blackboard) |
| Formação de conhecimento / retrieval | **SPEC-007** | o KG recebe conhecimento publicado |
| Estado persistente por agente | **SPEC-009** — **G-001 (ABERTA)** | persistência por agente |
| Ciclo de evolução do conhecimento (P12) | **SPEC-018** — **K-001 (ABERTA)** | governança de aprendizado |
| Redefinir CHM-001/CEM-001/CCM-001/SPEC-004/005 | canônicos/baseline | **CC-02/CONST-01/INV-09** |
| Fórmula/pesos/limiares de convicção | **SPEC-003/CCM-001; J-001/N-001 (ABERTAS)** | INV-03/INV-04 |
| Componente "Cognitive Ontology" separado | — (ontologia DENTRO da SPEC-006) | DHR-SPEC006-001 Q-ABERTURA-4; criar componente é de Andraus (não feito) |
| Escolher tecnologia de banco de grafos | **H-001 (ABERTA)** | fora do mandato do Especificador; Andraus |

---

## D2 — Regras

> **Etiqueta:** as RULE-CKG-* e o contrato de nó/relação abaixo são **[PROPOSTA]** — normativos só na homologação de
> Andraus + registro do Controlador (RULE-HG-02). As RULE/INV/ENF citadas como fundamento (CEM-001 l.608-615, CHM-001,
> CCM-001, RULE-BB-004, RULE-CAU-01/02/03, INV-04/05/06/07/09/10, ENF-03/04/07, SAS-001 §6.12, SPEC-004 INV-CBP-01)
> **já existem** e são FATO NORMATIVO.

```
RULE-CKG-001: Todo nó e toda relação escritos no KG DEVEM pertencer à ONTOLOGIA permitida (tipo ∈ catálogo) e satisfazer
              a MATRIZ DE INTEGRIDADE (tipos de origem/destino, direcionalidade e simetria admitidos por tipo de relação
              — ver tabela §D2.1). Violação de tipo ou de integridade é REJEITADA (fail-closed), não escrita. A ontologia
              é ENXUTA e vive DENTRO da SPEC-006 (não é componente separado).
              [Fonte: KERNEL-V2 l.1488-1507 (research.md §0/§3.6); DHR-SPEC006-001 Q-ABERTURA-4]  [PROPOSTA]

RULE-CKG-002: Toda ENTIDADE (nó) que corresponde a um objeto canônico (hypothesis/CHM-001, evidence/CEM-001,
              conviction/CCM-001) DEVE referenciá-lo por ID+versão — NUNCA redefinir seu contrato, campos ou máquina de
              estados (CC-02/INV-10). Um nó `observation` (Skill — INV-06) NÃO pode ser rotulado `evidence`.
              [Fonte: CEM-001; CHM-001; CCM-001; CC-02; INV-06; INV-10]  [PROPOSTA]

RULE-CKG-003: Toda RELAÇÃO DEVE ser tipada (um tipo do catálogo), armazenada DIRECIONADA (origem→destino) e carregar
              proveniência (RULE-CKG-005). A simetria, quando aplicável (ex.: SIMILAR_A), é propriedade SEMÂNTICA da
              consulta (A~B ⇔ B~A), não ausência de direção no armazenamento. Relações contraditórias NÃO são resolvidas
              em silêncio (RULE-CKG-013).
              [Fonte: ROADMAP §6; research.md §4/§8; INV-07]  [PROPOSTA]

RULE-CKG-004: A mudança de validade de uma relação é ATO AUTORIZADO (CKG-009), NUNCA automática/em cascata (CEM-001 l.602
              "invalidação não implica cascata"; o impacto sobre hipóteses/convicções é de CHM/CCM/CDM — CEM-001 l.503/606;
              CHM-001 l.672-676). Ela NÃO MUTA o registro existente: grava um NOVO registro (invalidação/sucessão) com
              `recorded_at` e, quando aplicável, `valid_to`. A VALIDADE CORRENTE é PROJEÇÃO DERIVADA. **Duas dimensões
              temporais (bitemporal):** valid-time (`valid_from`/`valid_to` — "válida em T") e transaction-time
              (`recorded_at` — "conforme registrado em R"); a invalidação é um registro POSTERIOR em transaction-time que
              pode marcar `valid_to` em valid-time (inclusive retroativo). Invalidar ≠ deletar (INV-07; espelha SPEC-004 INV-CBP-01).
              [Fonte: research.md §3.1; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.503; CHM-001 l.672-676]  [PROPOSTA]

RULE-CKG-005: Nenhuma entidade/relação pode existir sem PROVENIÊNCIA, **espelhando a condicionalidade de SPEC-004
              RULE-CBP-007** (não criando regra mais forte): (a) **`computed_by`/`writer_id` da identidade AUTENTICADA pelo
              runtime é SEMPRE obrigatório** (RULE-CBP-014); (b) **`gate_record` SÓ quando o objeto resulta de um gate**
              (contém gate_id/version/resultado/entrada/avaliador); (c) **`provenance_ref.lineage`/`derived_from` SÓ quando
              DERIVADO** (`Lineage`/`derived_from[]` não-vazio). Para nós `asset`/`timeframe`/`regime`/`observation` e
              hipóteses PRIMARY (Lineage vazio, sem gate) a proveniência "presente" = `computed_by` presente + `lineage=[]`
              legítimo (lista vazia é válida, NÃO force gate_record fabricado — RULE-MET-01). Escrita sem a proveniência
              EXIGÍVEL é REJEITADA (fail-closed). Referencia os contratos canônicos; NÃO os redefine (CC-02). `provenance_ref.lineage`
              [PROPOSTA] referencia `Lineage` (CEM-001 Cap.5)/`derived_from[]` (SPEC-004) — não há `lineage_ref` no CEM-001.
              [Fonte: CEM-001 Cap.5; SPEC-004 v1.2 (gate_record); research.md §3.2]  [PROPOSTA]

RULE-CKG-006: O KG é APPEND-ONLY PERMANENTE (INV-07; reforça RULE-BB-004; espelha SPEC-004 INV-CBP-01): nenhum registro
              é DELETADO nem MUTADO. "Esquecimento"/consolidação = ARQUIVAMENTO/rebaixamento VERSIONADO (novo registro de
              transição — RULE-CKG-012), nunca remoção. O estado corrente é PROJEÇÃO DERIVADA do conjunto de registros;
              toda transição é reconstruível (P13).
              [Fonte: INV-07; RULE-BB-004 (RULES.md l.323); SPEC-004 INV-CBP-01; research.md §3.6]  [PROPOSTA]

RULE-CKG-007: A CONFIANÇA de uma relação é escala PRÓPRIA do KG, em NAMESPACE próprio, e NÃO É a Convicção (Conviction
              Vector 8D — CCM-001). O KG NÃO a expõe em campos do objeto de convicção nem escreve relação CAUSA cujo
              destino seja `conviction` a partir de `calibration_metric`/propriedade de custo/confiança (matriz §D2.1).
              INV-04 (atomic-spec l.404) proíbe **custo** no Conviction Vector; a proibição de a **confiança** entrar na
              convicção é EXTENSÃO LOCAL [PROPOSTA] desta Spec (não cláusula de INV-04). Que o cálculo de convicção
              (SPEC-003/CCM-001) não a consuma é requisito endereçado à SPEC-003 / [DECISÃO NECESSÁRIA]. Nenhum limiar de
              convicção é fixado; a escala de confiança é PARÂMETRO a calibrar (INDETERMINADO; não toca J-001/N-001).
              [Fonte: INV-04 (custo); CCM-001; RULE-MET-01; research.md §4]  [PROPOSTA]

RULE-CKG-008: Toda relação CAUSA DEVE declarar o MECANISMO (como a origem produz o destino), DIREÇÃO e CONDIÇÕES
              (RULE-CAU-01), o REGIME/condição de validade (RULE-CAU-02) e, se formulada após o resultado, o MARCADOR
              pós-hoc (RULE-CAU-03). Correlação/precedência/padrão histórico NÃO bastam. Relação CAUSA sem esses campos é
              REJEITADA. O juízo que PROPÕE relação (CAUSA/SIMILAR_A) é Classe H: bounded loop (parada explícita) + gate
              de saída determinístico que verifica a PRESENÇA (não a veracidade — ENF-03) desses campos antes de escrever.
              [Fonte: RULE-CAU-01/02/03 (RULES.md l.680-682); research.md §8]  [PROPOSTA]

RULE-CKG-009: A escrita no KG permanente é GOVERNADA e é E3 (commit crítico/irreversível — atomic-spec §10.2 "KG publicado
              → E3 mínimo"), fail-closed: só ESCRITORES AUTORIZADOS escrevem, com identidade AUTENTICADA pelo runtime
              (reusa SPEC-004 CBP-014 — não define auth nova); FALHA do mecanismo de autenticação da SPEC-004 ⇒ o KG
              trata como NÃO-AUTORIZADO (fail-closed). O produtor pode registrar relações mas NÃO pode redefinir a
              ONTOLOGIA nem alterar TAXONOMIAS globais (SAS-001 §6.12). Alteração da ONTOLOGIA é ato de GOVERNANÇA
              (spec-time: análogo a RULE-HG/SPEC-019 — **[INFERÊNCIA]**, a SPEC-019 não cita "ontologia" literalmente;
              runtime: K-001 [DECISÃO NECESSÁRIA]), prospectiva e backward-compatible (nós existentes nunca invalidados
              por mudança de ontologia — INV-07); migração de `schema_version` = [DECISÃO NECESSÁRIA].
              Quem mantém a allowlist de escritores e quem hospeda o juízo de CKG-008 = [DECISÃO NECESSÁRIA] (runtime; K-001/SPEC-018).
              [Fonte: SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; SPEC-019 RULE-HG; ENF-03/04]  [PROPOSTA]

RULE-CKG-010: O KG recebe conhecimento por DUAS fontes sob a MESMA governança (CKG-009): (a) OBJETOS CANÔNICOS e suas
              transições (hypothesis/evidence/conviction) via seu CICLO DE VIDA canônico (já validados por SPEC-001/002/003)
              — admitidos preservando TODOS os estados, inclusive REFUTED/SUPERSEDED/ARCHIVED (CEM-001 l.494); (b)
              CONHECIMENTO FORMADO (padrões/aprendizados/relações generalizadas) via SELO DE PUBLICAÇÃO da SPEC-007. O KG
              NÃO faz formação/extração/retrieval. Conhecimento formado SEM selo é REJEITADO. O contrato do selo de
              publicação é DEPENDÊNCIA da SPEC-007 (ainda não especificada) = [DECISÃO NECESSÁRIA].
              [Fonte: ROADMAP §6/§7; CEM-001 l.494; research.md §3.4]  [PROPOSTA]

RULE-CKG-011: O KG DEVE oferecer CONSULTA cognitiva read-only (padrão/similaridade/causalidade/histórico/multi-salto) e a
              Cognitive Trace Reconstruction — reconstrução da cadeia cognitiva COMPLETA (todos os ancestrais diretos e
              indiretos) navegando as relações DERIVA_DE/Lineage (CEM-001 l.608-615/l.612-614). A COMPLETUDE do trace é
              OBRIGAÇÃO canônica e NÃO é rebaixada pelo mecanismo físico (H-001); o que permanece INDETERMINADO até H-001
              é a EFICIÊNCIA/custo de consultas multi-salto AMPLAS (ex.: similaridade de alto grau), não a completude da
              linhagem. A consulta é opcional/não-bloqueante (SAS-001 §6.12/EC-COG-003) e NÃO altera estado (read-only).
              [Fonte: CEM-001 l.608-615/l.612-614; SAS-001 §6.12/l.163; research.md §3.4]  [PROPOSTA]

RULE-CKG-012: O estado de um nó/relação (ACTIVE_KNOWLEDGE / SUPERSEDED / INVALIDATED_IN_TIME / ARCHIVED) é PROJEÇÃO
              DERIVADA do conjunto de registros, não um campo mutado. Critérios: SUPERSEDED = existe versão sucessora que
              o referencia por `supersedes` (CONTEÚDO corrigido/substituído); INVALIDATED_IN_TIME = relação cuja validade
              terminou (`valid_to` em registro de invalidação) SEM sucessora de conteúdo (o MUNDO mudou); ARCHIVED =
              rebaixamento de relevância sob governança (campo `relevance` em registro de arquivamento; autoridade = gate
              E3 de CKG-009). CORREÇÃO/REATIVAÇÃO = NOVO registro (nova versão com `supersedes`, ou nova relação com novo
              `valid_from`), nunca mutação/reuso do registro antigo. Nenhuma transição remove registro (INV-07).
              [Fonte: CHM-001; INV-07; SPEC-004 INV-CBP-01; research.md §3.6]  [PROPOSTA]

RULE-CKG-013: Colisão ocorre sse duas relações (i) formam um PAR CONTRADITÓRIO da tabela §D2.2, (ii) têm o MESMO escopo
              (mesmos `from_node` e `to_node`) e (iii) suas janelas de validade se SOBREPÕEM. Nesse caso o KG DETECTA e
              REGISTRA a colisão (um `collision_record` referenciando ambas; ambas preservadas, versionadas, com proveniência
              e validade), NUNCA sobrescreve/apaga uma em silêncio. Fora dessas condições NÃO há colisão (ex.: origens
              distintas; validades disjuntas — ADV-18). A RESOLUÇÃO (qual prevalece) é de SPEC-007/SPEC-018 ou governança —
              o KG só detecta e registra; não decide.
              [Fonte: INV-07; §D2.2; research.md §8; fronteira SPEC-007/SPEC-018]  [PROPOSTA]
```

### D2.1 — Matriz de integridade da ontologia (RULE-CKG-001) [PROPOSTA]

> **Atributo de escola (ADDED — UM campo único: `school`):** nós `hypothesis`/`structure` carregam `school` ∈ {Elliott,
> SMC, Fibonacci, ICT} e, para `hypothesis`, `hierarchy_role` ∈ {PRIMARY, SUB} (ref. SPEC-001 `hierarchy_role`) — **por
> referência** ao canônico que os produziu (CHM-001). *(O termo "origin_agent" da v1.2 foi eliminado — usa-se só `school`.)*
> O KG **espelha**, NÃO decide, a autoridade de criação (CC-01; Elliott cria PRIMARY; ICT não cria — INV-02/RULE-HH-004).
> **Regra de nó (integridade, CKG-001):** `hypothesis.school ∈ {Elliott, SMC, Fibonacci}` — `hypothesis` com `school=ICT`
> é PROIBIDA (INV-02/RULE-HH-004), fail-closed. (ICT pode aparecer em `structure` de execução, nunca criando hipótese.)
> "**Família estrutural**" é COMPUTADA (não é campo): nós de **mesma `school`** que `PERTENCE_A` o **mesmo par (asset,
> timeframe)** — usada **só** para restringir herança fractal INTRA-escola; a herança sub→pai ENTRE escolas
> (SMC/Fibonacci SUB → Elliott PRIMARY) é NORMAL e NÃO é bloqueada (SPEC-001 RULE-HH-003 l.104, campo `parent_id`;
> CHM-001 `parent_hypothesis_id` l.165/415; CONSTITUTION l.193).

| Relação | Origem (node_type) | Destino (node_type) | Direcional | Simétrica (consulta) |
|---|---|---|---|---|
| CONFIRMA | **evidence** (NÃO observation — CONSTITUTION l.191; INV-06) | hypothesis | sim | não |
| REFUTA | **evidence** (NÃO observation) | hypothesis | sim | não |
| DEPENDE_DE | hypothesis, mission | hypothesis, evidence | sim | não |
| HERDA | hypothesis (`hierarchy_role=SUB`) | hypothesis (**PAI = `hierarchy_role=PRIMARY`** — RULE-HH-003) — via `parent_id`/`parent_hypothesis_id`; **entre escolas é permitido**; "família estrutural" só restringe SUB intra-escola | sim | não |
| PERTENCE_A | hypothesis, evidence, structure, observation | asset, timeframe, regime, mission | sim | não |
| INVALIDA | evidence, learning | evidence, relation (via `target_relation_id`) | sim | não |
| ORIGINA | structure/hypothesis com `school` ∈ {Elliott, SMC, Fibonacci} — **nunca ICT** (INV-02/RULE-HH-004) | hypothesis | sim | não |
| DERIVA_DE | evidence (DERIVED) | evidence (ancestral) | sim | não — **aresta de Lineage** (CEM-001 Cap.5); base do trace (CKG-011); obrigatória por ancestral do Lineage (INV-CKG-02) |
| SIMILAR_A | qualquer | mesmo node_type | sim (armazenada) | **sim** (consulta trata A~B ⇔ B~A) |
| CAUSA | qualquer **exceto** origem com propriedade de custo/confiança quando destino=`conviction` | qualquer — **destino `conviction` PROIBIDO a partir de `calibration_metric`/custo/confiança (INV-04)** | sim | não — exige mechanism+direction+conditions+regime (+posthoc_flag) (CKG-008) |
| HIERARQUIA_DE | structure, timeframe | structure, timeframe | sim | não |
| ESTATISTICA_DE | learning | hypothesis, structure, asset | sim | não |

> **Distinção DERIVA_DE × proveniência:** `DERIVA_DE` é uma RELAÇÃO navegável do grafo (aresta de Lineage entre nós),
> consumida pela Cognitive Trace Reconstruction (ordem de saída = ancestralidade: dos ancestrais primários aos derivados
> — CEM-001 l.567-577). `provenance_ref.lineage` é um CAMPO de proveniência do registro (quem/de onde; referencia o
> campo `Lineage` do CEM-001 / `derived_from[]` da SPEC-004) — não é aresta navegável. São coisas distintas e coexistem.

> **Invariante local [PROPOSTA] — INV-CKG-01 (Memória permanente imutável):** nenhum registro do KG é deletado ou mutado;
> estado = projeção derivada; toda consolidação/"esquecimento" é arquivamento versionado; toda entidade/relação carrega
> proveniência e é reconstruível. Reforça — não redefine — RULE-BB-004, INV-07 e SPEC-004 INV-CBP-01, no eixo permanente. [PROPOSTA]

> **Invariante local [PROPOSTA] — INV-CKG-02 (Completude e aciclicidade da linhagem):** admitir um nó `evidence` DERIVED
> EXIGE que o KG materialize uma aresta `DERIVA_DE` para CADA ancestral do seu `Lineage` (CEM-001 l.565) — fail-closed se
> algum ancestral não estiver referenciado/presente (CKG-003/011); o grafo de `DERIVA_DE` é ACÍCLICO; a Cognitive Trace
> Reconstruction ignora o filtro de validade temporal (um ancestral invalidado no tempo permanece na linhagem — CEM-001
> l.602 "invalidação não implica remoção"). Garante a COMPLETUDE exigida por CEM-001 l.612-614, independente de H-001.
> **Ordem de admissão (evita deadlock):** o derivado só é admitido depois de (ou junto com) os ancestrais; enquanto um
> ancestral não for admitido, o derivado AGUARDA (`PENDING_ANCESTOR`, transitório), **não** falha-para-sempre (ver CKG-010). [PROPOSTA]

### D2.2 — Tabela de contradição e escopo de colisão (RULE-CKG-013) [PROPOSTA]

> **Colisão** = duas relações formam um PAR CONTRADITÓRIO E têm o **MESMO escopo** E suas **janelas de validade se
> sobrepõem**. Fora disso NÃO há colisão (evita falso-positivo — ADV-18).

**Escopo (todas as condições):** (1) mesmos `from_node` e `to_node` (mesma direção); (2) ambas vigentes com **sobreposição
temporal** (interseção de `[valid_from, valid_to)` não vazia); (3) o par de `relation_type` consta da tabela abaixo.

| Tipo A | Tipo B (contradiz A) | Simétrico? | Observação |
|---|---|---|---|
| CONFIRMA | REFUTA | **sim** (A↔B) | mesma hipótese-alvo afirmada e negada ao mesmo tempo |
| INVALIDA | (a relação-alvo `target_relation_id` que ela invalida, se essa continua vigente) | não | INVALIDA vigente sobre relação que segue ACTIVE_KNOWLEDGE |

> Pares NÃO listados **não** são contradição estrutural (ex.: DEPENDE_DE × SIMILAR_A, HERDA × PERTENCE_A). **Casos que NÃO
> colidem:** (a) `from_node` diferentes (A1 CONFIRMA B, A2 REFUTA B — origens distintas); (b) janelas de validade disjuntas
> (uma já invalidada no tempo antes da outra valer). A **resolução** de uma colisão registrada é de SPEC-007/SPEC-018 ou
> governança — o KG só detecta e registra (CKG-013). A tabela é ENXUTA e extensível por governança (RULE-ONT-02).

---

## Critérios de Aceitação (EARS)

1. Quando um nó ou relação é submetido para escrita, o KG DEVE escrevê-lo somente se o tipo pertence à ontologia e satisfaz a matriz de integridade, e DEVE rejeitar (fail-closed) violação de tipo/integridade, sem escrever.
2. Quando um nó corresponde a um objeto canônico, o KG DEVE referenciá-lo por ID+versão e NÃO DEVE redefinir seu contrato/campos/estados; um nó `observation` NÃO DEVE ser rotulado `evidence`.
3. Quando uma relação é escrita, o KG DEVE exigir tipo, direção e proveniência, e NÃO DEVE aceitar relação sem proveniência; a simetria de SIMILAR_A é semântica de consulta, não ausência de direção.
4. Quando a validade de uma relação muda, o KG DEVE gravar um NOVO registro de invalidação/sucessão e manter o histórico, e NÃO DEVE mutar nem deletar o registro existente.
5. Quando qualquer escrita é tentada sem proveniência, o KG DEVE rejeitá-la (fail-closed).
6. Quando um "esquecimento"/consolidação é solicitado, o KG DEVE arquivar/rebaixar por novo registro versionado, e NÃO DEVE remover nem mutar registro histórico.
7. Quando uma confiança de relação é registrada, o KG DEVE mantê-la em namespace próprio e NÃO DEVE expô-la em campos do objeto de convicção nem escrever aresta CAUSA custo/confiança→`conviction` (INV-04 custo como base; que o cálculo de convicção não a consuma é requisito à SPEC-003 / [DECISÃO NECESSÁRIA]).
8. Quando uma relação causal é proposta, o KG DEVE exigir mechanism+direction+conditions+regime (e marcador pós-hoc quando aplicável) e DEVE rejeitar causal sem esses campos.
9. Quando uma escrita no KG permanente é tentada, o KG DEVE aceitá-la (E3) apenas de escritor autorizado com identidade autenticada (falha de auth ⇒ não-autorizado), e NÃO DEVE permitir que o produtor redefina ontologia/taxonomia.
10. Quando conhecimento formado sem selo de publicação é submetido, o KG DEVE rejeitá-lo; objetos canônicos entram por seu ciclo de vida preservando todos os estados.
11. Quando um consumidor consulta o KG, o KG DEVE responder read-only e reconstruir a cadeia cognitiva COMPLETA, e NÃO DEVE alterar estado na consulta.
12. Quando um nó/relação transita (SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED), o KG DEVE representar a transição por novo registro preservando o histórico (estado = projeção derivada), e NÃO DEVE remover nem mutar a versão anterior.
13. Quando duas relações entre os mesmos nós se contradizem, o KG DEVE detectar e registrar a colisão preservando ambas, e NÃO DEVE sobrescrever/apagar uma em silêncio.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec com efeito declara **CLASSE/MECANISMO** (§10.6). D = determinístico; C = constitutivo (é o gate); H =
> híbrido (juízo + gate de saída + bounded loop). **A escrita no KG permanente é E3** (commit crítico/irreversível —
> atomic-spec §10.2); consulta é E1; o guard de isolamento confiança×convicção é E2.

### BASpec-CKG-001 — Ontologia enxuta + matriz de integridade (rejeita violação)
```
BASpec-CKG-001:
  QUANDO:       Um nó ou relação é submetido para escrita no KG
  ENTÃO:        O KG escreve somente se o tipo ∈ ontologia E a matriz de integridade (§D2.1) é satisfeita (origem/destino
                admitidos, direcionalidade/simetria; **regra de nó: `hypothesis.school ≠ ICT`** — INV-02/RULE-HH-004;
                **HERDA só liga SUB a PAI `hierarchy_role=PRIMARY`**); violação é rejeitada (fail-closed), não escrita. O KG
                apenas ESPELHA os vínculos já criados pelos agentes (ex.: HERDA sub→pai por `parent_id`, inclusive entre
                escolas); NÃO decide a autoridade de criação de hipótese (CC-01)
  PORQUE:       Sem gramática enxuta + integridade, a memória permanente acumula conhecimento incoerente (research.md §8 R-8)
  REFERÊNCIA:   RULE-CKG-001; KERNEL-V2 l.1488-1507; CONSTITUTION l.193; INV-02; RULE-HH-003/004 (SPEC-001)
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico (tipo ∈ catálogo ∧ par origem/destino ∈ matriz ∧ direção/simetria ∧ hypothesis.school≠ICT ∧ HERDA.pai.hierarchy_role=PRIMARY)
    GATE DE SAÍDA: verificação da matriz §D2.1 + regras de nó (school/hierarchy_role)
    CRITÉRIO 4Es: Conformidade > Eficácia — coerência da ontologia é inviolável
  VERIFICADO POR:
    DADO        um nó `hypothesis` com `school == ICT` (ICT não cria hipótese — INV-02/RULE-HH-004)
    QUANDO      o gate de integridade roda
    ENTÃO       escrita rejeitada; nada persistido. (Contraste POSITIVO: HERDA de uma SUB SMC para a PAI Elliott
                (`hierarchy_role=PRIMARY`), via `parent_id`, é VÁLIDA entre escolas — não é violação; ver T15)
    VERIFICAÇÃO written == false; rejected_reason == "HYPOTHESIS_SCHOOL_ICT_FORBIDDEN"
```

### BASpec-CKG-002 — Entidade por referência ao canônico (não redefine; observation≠evidence)
```
BASpec-CKG-002:
  QUANDO:       Um nó corresponde a um objeto canônico (hypothesis/evidence/conviction) ou é uma observation
  ENTÃO:        O KG referencia o canônico por ID+versão, grava `canonical_status` (snapshot do Status — CEM-001 l.264/428;
                CHM-001) e, a cada mudança de Status, um registro `canonical_state_transition` (estado/timestamp/origem/
                justificativa — CEM-001 l.428), preservando TODOS os estados (CEM-001 l.494); NÃO redefine contrato/campos;
                um nó observation (Skill — INV-06) NÃO é rotulado evidence. Os estados do KG (D5) são HOMÔNIMOS mas ≠ estados canônicos (CC-10)
  PORQUE:       Redefinir canônico viola CC-02/CONST-01; o Status é o único campo mutável do canônico (CEM-001 l.264), logo o KG
                precisa de snapshot+transições para "preservar todos os estados" (l.494); Observação≠Evidência (INV-06); idioma canônico é do objeto (INV-10)
  REFERÊNCIA:   RULE-CKG-002; CC-02; CC-10; CEM-001 l.264/428/494; INV-06; INV-10
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : referência (canonical_id@version) + snapshot canonical_status + registro canonical_state_transition; rótulo validado contra INV-06
    CRITÉRIO 4Es: Eficácia — integridade referencial + preservação de todos os estados canônicos
  VERIFICADO POR:
    DADO        um nó observation sendo rotulado evidence
    QUANDO      o nó é escrito
    ENTÃO       rejeitado; observation e evidence são tipos distintos
    VERIFICAÇÃO observation_labeled_evidence == false; rejected_reason == "OBSERVATION_IS_NOT_EVIDENCE"
```

### BASpec-CKG-003 — Relação tipada, direcionada, com proveniência
```
BASpec-CKG-003:
  QUANDO:       Uma relação entre dois nós é escrita
  ENTÃO:        O KG exige tipo (catálogo), direção (origem→destino, armazenada) e proveniência (CKG-005); SIMILAR_A é
                simétrica só na semântica de consulta (A~B ⇔ B~A), não ausência de direção; **admitir um nó `evidence`
                DERIVED EXIGE materializar uma aresta `DERIVA_DE` por ancestral do seu Lineage — fail-closed se algum
                ancestral não estiver referenciado/presente (INV-CKG-02); o grafo DERIVA_DE é acíclico**; contradição não é silenciada (CKG-013)
  PORQUE:       Relação não-tipada/sem direção/sem proveniência não é auditável (P13); sem a aresta por ancestral, o trace
                completo (CKG-011/CEM-001 l.612-614) não seria garantido
  REFERÊNCIA:   RULE-CKG-003/005; INV-CKG-02; CEM-001 l.565; research.md §4
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : validação determinística (tipo ∈ catálogo ∧ direção presente ∧ proveniência presente)
    CRITÉRIO 4Es: Eficácia — relações auditáveis e navegáveis
  VERIFICADO POR:
    DADO        uma relação sem tipo do catálogo submetida
    QUANDO      a validação roda
    ENTÃO       relação rejeitada; nada escrito
    VERIFICAÇÃO relation_written == false; rejected_reason == "RELATION_TYPE_INVALID"
```

### BASpec-CKG-004 — Temporalidade bitemporal (invalidar por NOVO registro ≠ deletar/mutar)
```
BASpec-CKG-004:
  QUANDO:       Um ato AUTORIZADO (CKG-009) determina que a validade de uma relação mudou (ex.: um escritor autorizado
                registra que a relação SIMILAR_A entre dois padrões deixou de valer num novo regime) — NUNCA invalidação
                automática/em cascata (CEM-001 l.602; impacto é de CHM/CCM — l.503/606)
  ENTÃO:        O KG grava um NOVO registro de invalidação (com recorded_at e valid_to), preservando o registro de criação
                intacto; NÃO muta nem deleta o registro existente; a validade corrente é projeção derivada; a consulta
                responde por valid-time ("válida em T") e por transaction-time ("conforme registrado em R")
  PORQUE:       Invalidar por novo registro preserva a reconstrução histórica (INV-07); invalidar só por ato autorizado
                respeita "invalidação não implica cascata" (CEM-001 l.602) e a propriedade do impacto por CHM/CCM
  REFERÊNCIA:   RULE-CKG-004; RULE-CKG-009; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.503
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : novo registro de invalidação (valid_to, recorded_at); estado derivado por projeção; sem mutação
    CRITÉRIO 4Es: Eficácia — nenhuma verdade histórica perdida nem reescrita
  VERIFICADO POR:
    DADO        relação criada válida desde T0 (registro R0), cuja informação muda em T1
    QUANDO      a atualização é processada
    ENTÃO       R0 intacto; novo registro de invalidação com valid_to=T1; consulta "em T0" retorna válida; "agora" não
    VERIFICAÇÃO existing_record_mutated == false; existing_record_deleted == false; historical_query_consistent == true
```

### BASpec-CKG-005 — Proveniência obrigatória (rejeita escrita sem proveniência)
```
BASpec-CKG-005:
  QUANDO:       Qualquer nó/relação é escrito no KG
  ENTÃO:        O KG exige proveniência CONDICIONAL (espelha SPEC-004 RULE-CBP-007): `computed_by`/`writer_id` (identidade
                AUTENTICADA) SEMPRE; `gate_record` SÓ quando resulta de gate; `provenance_ref.lineage`/`derived_from` SÓ
                quando DERIVADO (lista vazia é legítima para PRIMARY/asset/timeframe/regime/observation — não force
                gate_record fabricado); escrita SEM `computed_by` (ou sem gate_record quando HÁ gate, ou sem lineage quando
                DERIVADO) é rejeitada (fail-closed)
  PORQUE:       Conhecimento sem ORIGEM AUTENTICADA não é reconstruível (CEM-001 Cap.5; P13); mas exigir gate_record/lineage
                de quem não tem gate/ancestral fabricaria dado (RULE-MET-01) e contrariaria a condicionalidade da CBP-007
  REFERÊNCIA:   RULE-CKG-005; SPEC-004 RULE-CBP-007/014; CEM-001 Cap.5 (campo `Lineage`)
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico — computed_by presente; gate_record sse resulta de gate; lineage sse derivado
    GATE DE SAÍDA: verificação (computed_by presente ∧ [gate ⇒ gate_record] ∧ [derivado ⇒ lineage não-vazio])
    CRITÉRIO 4Es: Conformidade > Eficácia — identidade autenticada é inviolável; sem fabricar proveniência (RULE-MET-01)
  VERIFICADO POR:
    DADO        (a) um nó PRIMARY sem gate e sem ancestral, com computed_by presente; (b) um nó sem computed_by
    QUANDO      o gate de escrita roda
    ENTÃO       (a) aceito (lineage=[] legítimo, sem gate_record); (b) rejeitado
    VERIFICAÇÃO case_a_written == true; case_a_lineage_empty_ok == true; case_b_written == false; case_b_reason == "COMPUTED_BY_MISSING"
```

### BASpec-CKG-006 — Imutabilidade / append-only permanente (nunca deletar nem mutar) [INV-CKG-01]
```
BASpec-CKG-006:
  QUANDO:       Uma deleção ou mutação de registro de nó/relação é tentada (inclusive disfarçada de "esquecimento")
  ENTÃO:        O KG recusa (fail-closed); "esquecimento"/consolidação só por novo registro de arquivamento versionado
                (CKG-012); o registro histórico é sempre preservado e nunca reescrito (INV-07)
  PORQUE:       A memória permanente nunca apaga nem reescreve — quebraria a reconstrução (P13) e INV-07/RULE-BB-004/INV-CBP-01
  REFERÊNCIA:   RULE-CKG-006; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que proíbe DELETE físico e UPDATE de registro; só novos registros de transição
    GATE DE SAÍDA: verificação (operação ∉ {DELETE, UPDATE de registro} ; histórico preservado)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda/não-reescrita de histórico acima de economia de espaço
  VERIFICADO POR:
    DADO        tentativa de deletar fisicamente (ou reescrever) um registro arquivado
    QUANDO      o gate roda
    ENTÃO       negado (fail-closed); registro permanece íntegro e reconstruível
    VERIFICAÇÃO physical_delete == false; record_mutated == false; history_preserved == true
```

### BASpec-CKG-007 — Confiança de relação é propriedade local do KG, nunca exposta ao objeto de convicção [regra LOCAL [PROPOSTA]; INV-04 (custo) como base]
```
BASpec-CKG-007:
  QUANDO:       Uma confiança de relação é registrada ou lida no KG
  ENTÃO:        O KG a mantém em NAMESPACE PRÓPRIO e NUNCA a expõe em campos do objeto de convicção (CCM-001) nem a
                emite como insumo para o cálculo de convicção; além disso o KG NÃO escreve relação CAUSA cujo destino
                seja `conviction` a partir de `calibration_metric`/propriedade de custo/confiança (matriz §D2.1)
  PORQUE:       INV-04 (atomic-spec l.404) proíbe CUSTO no Conviction Vector; esta Spec ESTENDE localmente a mesma
                lógica à confiança de relação (regra LOCAL [PROPOSTA], não cláusula de INV-04) para não contaminar a convicção
  REFERÊNCIA:   RULE-CKG-007; INV-04 (custo); CCM-001
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : guard determinístico — confiança em namespace do KG; proíbe CAUSA(custo/confiança→conviction) na escrita
    GATE DE SAÍDA: verificação (confiança ∉ campos do objeto de convicção ∧ não há aresta custo/confiança→conviction)
    CRITÉRIO 4Es: Conformidade > Eficácia — INV-04 (custo) é inviolável; a extensão à confiança é salvaguarda local
  VERIFICADO POR:
    DADO        uma relação CAUSA(calibration_metric → conviction) submetida
    QUANDO      o gate de escrita roda
    ENTÃO       rejeitada; a confiança de relação permanece em namespace próprio, não exposta ao objeto de convicção
    VERIFICAÇÃO confidence_exposed_in_conviction_object == false; cost_or_confidence_to_conviction_edge == false
```
> **Nota (item 6):** o que o KG controla é a **sua própria escrita** (campo/namespace e arestas). A garantia de que o
> **cálculo de convicção** (SPEC-003/CCM-001 — baseline; J-001 ABERTA) não consome a confiança de relação é **requisito
> endereçado à SPEC-003** (ou [DECISÃO NECESSÁRIA] na integração), NÃO uma obrigação imposta por esta Spec a um baseline. [INFERÊNCIA]

### BASpec-CKG-008 — Relação causal exige mecanismo+regime+pós-hoc (RULE-CAU-01/02/03)
```
BASpec-CKG-008:
  QUANDO:       Um juízo propõe uma relação CAUSA (ou SIMILAR_A) entre nós
  ENTÃO:        Para CAUSA, o KG exige mechanism+direction+conditions (RULE-CAU-01), regime/condição de validade
                (RULE-CAU-02) e, se formulada após o resultado, marcador pós-hoc (RULE-CAU-03); faltando, rejeita; o gate
                de saída verifica apenas a PRESENÇA desses campos (não a veracidade — ENF-03)
  PORQUE:       Correlação não é causalidade (RULE-CAU-01); a relação causal pode mudar entre regimes (RULE-CAU-02);
                explicação pós-resultado é viés se não marcada (RULE-CAU-03)
  REFERÊNCIA:   RULE-CKG-008; RULE-CAU-01/02/03
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : juízo (apoio semântico) PROPÕE; gate de saída determinístico verifica presença dos campos CAU-01/02/03
    BOUNDED LOOP: nº máximo de tentativas de proposta por par de nós; sem retry infinito
    GATE DE SAÍDA: verificação (CAUSA ⇒ mechanism ∧ direction ∧ conditions ∧ regime presentes; posthoc_flag quando aplicável)
    CRITÉRIO 4Es: Eficácia (causalidade válida) > Eficiência; LLM é detector, nunca gate (ENF-03)
  VERIFICADO POR:
    DADO        uma relação CAUSA proposta sem mechanism/regime (só correlação)
    QUANDO      o gate de saída roda
    ENTÃO       relação rejeitada (não escrita)
    VERIFICAÇÃO causal_written == false; rejected_reason == "CAUSAL_FIELDS_MISSING"
```

### BASpec-CKG-009 — Governança de escrita E3 (autorizado+autenticado; não redefine ontologia) [E3]
```
BASpec-CKG-009:
  QUANDO:       Uma escrita no KG permanente é tentada
  ENTÃO:        O KG (E3, fail-closed) aceita apenas de escritor AUTORIZADO com identidade AUTENTICADA pelo runtime (reusa
                SPEC-004); FALHA do mecanismo de autenticação da SPEC-004 ⇒ tratado como NÃO-AUTORIZADO; o produtor registra
                relações mas NÃO redefine ontologia/taxonomia (SAS-001 §6.12); alteração de ontologia é ato de governança
  PORQUE:       Escrita em memória permanente é commit crítico/irreversível (E3 — atomic-spec §10.2); autorização não pode
                depender do payload e não pode falhar-aberto
  REFERÊNCIA:   RULE-CKG-009; SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate E3 de autorização por identidade autenticada + escopo (registrar ≠ redefinir ontologia); LLM não é gate
    GATE DE SAÍDA: verificação (escritor ∈ autorizados ∧ auth OK ∧ operação ∉ {redefinir ontologia/taxonomia}); auth indisponível ⇒ DENY
    CRITÉRIO 4Es: Conformidade > Eficácia — escrita permanente só sob autorização é inviolável (ENF-04)
  VERIFICADO POR:
    DADO        uma escrita cuja verificação de identidade da SPEC-004 está indisponível/falha
    QUANDO      o gate E3 roda
    ENTÃO       escrita negada (fail-closed; tratada como não-autorizada); falso-DENY amostrado (ENF-07)
    VERIFICAÇÃO write_allowed == false; fail_closed == true; treated_as_unauthorized == true
```

### BASpec-CKG-010 — Fronteira de entrada (canônico via ciclo de vida + formado via selo SPEC-007)
```
BASpec-CKG-010:
  QUANDO:       Conhecimento é submetido ao KG
  ENTÃO:        O KG admite (a) objetos canônicos e suas transições via ciclo de vida — gravando `canonical_status` +
                registros `canonical_state_transition` (preservando TODOS os estados, incl. REFUTED/SUPERSEDED/ARCHIVED —
                CEM-001 l.494) — e (b) conhecimento FORMADO com selo de publicação da SPEC-007; formado SEM selo é rejeitado;
                o KG NÃO faz formação/retrieval
  PORQUE:       "Documento recuperado ≠ conhecimento validado ≠ publicado"; formação é SPEC-007; o KG DEVE preservar todos
                os estados canônicos — e como o `canonical_ref@version` sozinho não carrega Status (CEM-001 l.264), isso exige
                `canonical_status`+`canonical_state_transition`
  REFERÊNCIA:   RULE-CKG-010; ROADMAP §6/§7; CEM-001 l.264/l.494; research.md §3.4
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : caminho (b) FORMADO = gate determinístico verificável (exige selo SPEC-007). Caminho (a) CANÔNICO = o
                  critério de admissão (qual estado/evento promove trabalho→permanente) é **NÃO-ESPECIFICADO/INDETERMINADO**
                  nesta Spec — NÃO é gate verificável ainda (ver bloco abaixo); grava canonical_status/transition quando admitido
    GATE DE SAÍDA: (b) verificação (selo SPEC-007 presente) — verificável; (a) **INDETERMINADO** até [DECISÃO NECESSÁRIA] (não declarar como gate verificável)
    CRITÉRIO 4Es: Conformidade > Eficácia — não contaminar com não-validado; não perder estado canônico
  VERIFICADO POR:
    DADO        um conhecimento formado (padrão) submetido SEM selo (caminho b)
    QUANDO      o gate de fronteira (b) roda
    ENTÃO       o formado sem selo é rejeitado (parte verificável); o critério do caminho (a) é INDETERMINADO (abaixo)
    VERIFICAÇÃO formed_without_seal_accepted == false; path_a_admission_criterion == "INDETERMINADO"
```

> **[DECISÃO NECESSÁRIA] — critério/produtor de admissão do caminho (a) (item 6 R4):** o gate "origem ∈ ciclo de vida
> canônico" da v1.2 era **vacuoso** (qualquer estado — EMERGENT/CANDIDATE/ACTIVE — passaria). Correção: o caminho (a) é
> declarado **NÃO-ESPECIFICADO/INDETERMINADO** (não um gate verificável) até Andraus. **[PROPOSTA] de critério mínimo
> (não homologada):** admitir no KG permanente apenas objeto canônico JÁ VALIDADO (SPEC-001/002/003) cujo estado ∈
> {ACTIVE, DOMINANT, SUPERSEDED, REFUTED, ARCHIVED} — **excluir EMERGENT/CANDIDATE** (ainda trabalho — SPEC-004). O
> **produtor** do caminho (a) (a SPEC-005 não escreve no KG — SPEC-005 plan l.971) e o **gatilho/evento** de promoção são
> **[DECISÃO NECESSÁRIA]**.
> **Reatribuição de S14 à SPEC-018/K-001 — submetida a Andraus [DECISÃO NECESSÁRIA]:** a ABERTURA enviou à SPEC-018 apenas
> o **ciclo P12** (K-001); atribuir a ela o **critério de promoção trabalho→permanente** é extrapolação — **não homologada**;
> fica como proposta a Andraus, não como fato.
> **Ordem de admissão de ancestrais (evita deadlock de INV-CKG-02):** um `evidence` DERIVED só é admitido DEPOIS de (ou na
> mesma transação que) seus ancestrais do Lineage; enquanto um ancestral PRIMARY não for admitido, a admissão do derivado
> **AGUARDA** (estado de admissão `PENDING_ANCESTOR`, transitório, não persistido) — **não** falha-para-sempre. Se o
> ancestral nunca for admitido (decisão de promoção), o derivado permanece não-admitido (não entra sem linhagem completa). [PROPOSTA]

### BASpec-CKG-011 — Consulta read-only + Cognitive Trace Reconstruction completa
```
BASpec-CKG-011:
  QUANDO:       Um consumidor consulta o KG ou pede a reconstrução da cadeia cognitiva de uma evidência/hipótese
  ENTÃO:        O KG responde read-only navegando as arestas DERIVA_DE e retorna a cadeia COMPLETA (fecho transitivo de
                todos os ancestrais — CEM-001 l.608-615/l.612-614) sem alterar estado; a completude é GARANTIDA por INV-CKG-02
                (toda evidence DERIVED materializou uma aresta DERIVA_DE por ancestral do Lineage); o trace IGNORA o filtro de
                validade temporal (ancestral invalidado no tempo permanece na linhagem — CEM-001 l.602); a completude NÃO é
                rebaixada por H-001 (só a eficiência de consultas multi-salto AMPLAS fica INDETERMINADA até H-001)
  PORQUE:       Reconstrução completa é responsabilidade canônica do KG (CEM-001 l.562-565/l.699); consulta não muta
  REFERÊNCIA:   RULE-CKG-011; INV-CKG-02; CEM-001 l.608-615/l.612-614/l.602; SAS-001 §6.12
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : travessia determinística das arestas DERIVA_DE a partir do nó, acumulando ancestrais até o fecho transitivo; read-only
    CRITÉRIO 4Es: Eficácia (reconstrução completa — obrigação) > Eficiência (eficiência de consulta ampla = H-001)
  VERIFICADO POR:
    DADO        Evidence-E deriva de D; D deriva de C; C deriva de A e B (cadeia de 3 saltos)
    QUANDO      pede-se Cognitive Trace Reconstruction de Evidence-E
    ENTÃO       retorna o fecho completo [A,B,C,D] (ordem de ancestralidade); nenhum estado alterado
    VERIFICAÇÃO trace == ["A","B","C","D"]; trace_complete == true; state_mutated_by_query == false
```

### BASpec-CKG-012 — Lifecycle do nó/relação (estado = projeção derivada; novos registros)
```
BASpec-CKG-012:
  QUANDO:       Um nó/relação é substituído (correção de conteúdo), invalidado no tempo, ou rebaixado (arquivamento)
  ENTÃO:        O KG grava um NOVO registro: SUPERSEDED = sucessora com supersedes (conteúdo corrigido); INVALIDATED_IN_TIME
                = invalidação com valid_to sem sucessora de conteúdo; ARCHIVED = arquivamento com campo relevance sob gate
                E3 (CKG-009). O estado é projeção derivada; correção/reativação = novo registro; nenhuma versão é removida/mutada
  PORQUE:       Conhecimento permanente/temporário se opera por lifecycle versionado, não por deleção/mutação (INV-07; INV-CBP-01)
  REFERÊNCIA:   RULE-CKG-012; CHM-001; INV-07; SPEC-004 INV-CBP-01
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : transições append-only (novo registro aponta para o anterior por supersedes); estado por projeção derivada
    CRITÉRIO 4Es: Eficácia — reconstrução íntegra do histórico de conhecimento
  VERIFICADO POR:
    DADO        um nó ACTIVE_KNOWLEDGE cujo conteúdo é corrigido
    QUANDO      a correção roda
    ENTÃO       nova versão criada com supersedes→anterior; a anterior permanece íntegra; estado SUPERSEDED é derivado
    VERIFICAÇÃO old_version_preserved == true; old_version_mutated == false; supersedes_link_present == true
```

### BASpec-CKG-013 — Colisão de relações (detecta e registra; não resolve em silêncio)
```
BASpec-CKG-013:
  QUANDO:       Duas relações satisfazem as 3 condições de colisão (§D2.2): par contraditório ∧ mesmos (from_node,to_node) ∧ validade sobreposta
  ENTÃO:        O KG DETECTA e grava um collision_record referenciando ambas (preservadas, versionadas, com proveniência e
                validade); NÃO sobrescreve/apaga uma em silêncio; relações que NÃO satisfazem as 3 condições (origens
                distintas, validades disjuntas, par não listado) NÃO geram colisão; a resolução é de SPEC-007/SPEC-018 ou governança
  PORQUE:       Preservar a contradição auditável respeita INV-07; resolver em silêncio perderia conhecimento e viés de confirmação; escopo evita falso-positivo
  REFERÊNCIA:   RULE-CKG-013; §D2.2; INV-07; fronteira SPEC-007/SPEC-018
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : detecção determinística — par ∈ tabela §D2.2 ∧ mesmos (from,to) ∧ overlap(valid) ⇒ grava collision_record; proíbe sobrescrita silenciosa
    GATE DE SAÍDA: verificação (as 3 condições §D2.2 ⇒ collision_record gravado ∧ ambas preservadas; senão sem colisão)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda de conhecimento e auditabilidade da contradição
  VERIFICADO POR:
    DADO        CONFIRMA(A→B) vigente e uma REFUTA(A→B) nova com validade sobreposta (mesmos A,B)
    QUANDO      a escrita roda
    ENTÃO       ambas preservadas; collision_record gravado; nenhuma apagada; resolução não decidida pelo KG
    VERIFICAÇÃO both_relations_present == true; collision_logged == true; silent_overwrite == false
```

---

## D4 — Algoritmo

Mecânicas **determinísticas reais** (D4 — atomic-spec §2). O **mecanismo físico** (grafo real/estrutura em memória/
tabelas+índice) é **INDETERMINADO = H-001 (ABERTA)**; abaixo está a lógica, não a tecnologia:

- **Integridade (CKG-001):** `aceitar sse tipo ∈ catálogo ∧ (origem.node_type, destino.node_type) ∈ matriz[tipo_relação] ∧ direção/simetria conformes (§D2.1)`.
- **Validade bitemporal / invalidar por novo registro (CKG-004):** criação grava `R0{record_kind=creation, valid_from, recorded_at}`; mudança (ato autorizado) grava `R1{record_kind=invalidation, ref=R0, valid_to, recorded_at}` — `R0` nunca mutado. Duas dimensões: **valid-time** `válida_em(T) = ∃ creation com valid_from≤T ∧ ¬∃ invalidation aplicável com valid_to≤T`; **transaction-time** `conforme_registrado_em(R) = conjunto de registros com recorded_at≤R`. "agora" = sem invalidation aplicável no estado corrente.
- **Imutabilidade / estado derivado (CKG-006/012):** `DELETE/UPDATE de registro ⇒ negado`. Estado(x) = projeção: `SUPERSEDED sse ∃ sucessora com supersedes=x`; `INVALIDATED_IN_TIME sse ∃ invalidation sem sucessora de conteúdo`; `ARCHIVED sse ∃ registro archival vigente`; senão `ACTIVE_KNOWLEDGE`.
- **Cognitive Trace Reconstruction (CKG-011):** `trace(x) = fecho transitivo das arestas DERIVA_DE a partir de x` — **completo** (todos os ancestrais; garantido por INV-CKG-02; IGNORA filtro de validade); ordem de saída = ancestralidade (primários→derivados, CEM-001 l.567-577). Completude é obrigação; eficiência de travessia ampla = H-001.
- **Dedupe (CKG-001/003):** `chave de nó = (node_type, canonical_ref)` quando canônico; `= (node_type, natural_key)` quando `canonical_ref=null` (asset/timeframe/regime/narrative/observation/learning — evita colapso); `chave de relação = (relation_type, from_node, to_node, valid_from)`. Reescrita idêntica = no-op; divergente = novo registro (nunca sobrescreve).
- **Gate causal (CKG-008):** `CAUSA ⇒ exige {mechanism, direction, conditions, regime} ≠ ∅ (+ posthoc_flag quando aplicável); senão rejeita`. Juízo bounded (nº máx. de tentativas por par). O gate verifica PRESENÇA, não veracidade (ENF-03).
- **Confiança de relação (CKG-007):** `confidence ∈ escala própria (PARÂMETRO a calibrar — INDETERMINADO)`; **proibido** `confidence → insumo do Conviction Vector` (namespaces separados; INV-04).
- **Detecção de colisão (CKG-013/§D2.2):** `colide(r1, r2) sse (r1.type, r2.type) ∈ tabela_contradição §D2.2 ∧ r1.from=r2.from ∧ r1.to=r2.to ∧ overlap([r1.valid_from,r1.valid_to), [r2.valid_from,r2.valid_to))`. Se `colide` ⇒ grava `collision_record`; senão NÃO. (Falso-positivo evitado: origens distintas ou validades disjuntas ⇒ `colide=false`.)
- **Nó hypothesis (CKG-001/§D2.1):** `aceitar sse ¬(node_type=hypothesis ∧ school=ICT)` (INV-02/RULE-HH-004); `HERDA ⇒ pai.hierarchy_role=PRIMARY` (RULE-HH-003); "família" = `{n : n.school = m.school ∧ n PERTENCE_A mesmo (asset,timeframe) de m}`.

Nenhuma fórmula computa convicção. Nenhum limiar de convicção nem escala numérica de confiança é fixado (RULE-MET-01).
[FONTE: atomic-spec §2; CEM-001 Cap.5; SPEC-004 INV-CBP-01; research.md §3.1/§4]

---

## D5 — Máquina de estados (lifecycle do nó/relação — estado = projeção derivada)

> **Fronteira (CC-02/CC-10):** este é o lifecycle do **conhecimento no KG permanente**, separado da máquina da **hipótese**
> (CHM-001) e do **estado do objeto no Blackboard** (SPEC-004) — não redefinidos. **O `knowledge_state` NÃO é um campo
> mutado: é PROJEÇÃO DERIVADA do conjunto de registros** (espelha SPEC-004 INV-CBP-01). **Os estados do KG abaixo são
> HOMÔNIMOS mas ≠ estados canônicos** (SUPERSEDED/ARCHIVED/REFUTED do CHM/CEM): o KG rastreia o Status canônico à parte,
> no snapshot `canonical_status` + registros `canonical_state_transition` (CKG-002/010) — acepção declarada (CC-10).

| Estado (derivado) | Definição (projeção) | Origem |
|---|---|---|
| ACTIVE_KNOWLEDGE | registro de criação vigente, sem sucessora nem invalidação nem arquivamento aplicável | criação |
| SUPERSEDED | existe sucessora que o referencia por `supersedes` (conteúdo corrigido/substituído) | CKG-012 |
| INVALIDATED_IN_TIME | existe registro de invalidação com `valid_to`, SEM sucessora de conteúdo (o mundo mudou) | CKG-004/012 |
| ARCHIVED | existe registro de arquivamento vigente (rebaixamento de `relevance` sob gate E3 — CKG-009) | CKG-012 |

> **Estados transitórios de admissão (NÃO persistidos):** `CANDIDATE_WRITE` (sob os gates) e `REJECTED` (falhou em gate)
> são estados do fluxo de admissão — **nada é persistido** quando rejeitado (CKG-001/005/009/010). Não aparecem como
> registros do KG.
> **Correção/reativação:** sempre por NOVO registro (nova versão com `supersedes`, ou nova relação com novo `valid_from`),
> nunca reuso/mutação do registro antigo (INV-07). **Autoridade de arquivamento:** gate E3 de governança (CKG-009).
> **Mecanismo físico = INDETERMINADO (H-001 ABERTA)**; Opção B (banco de grafos) **registrada e adiada** (research.md §3.5),
> adotável só se Andraus decidir H-001 como "grafo real". [FONTE: RULE-CKG-006/012; SPEC-004 INV-CBP-01; DHR-SPEC006-001 §3]

---

## D6 — Protocolo de escrita/consulta (sobre conhecimento publicado)

### Produtores, consumidores e fronteira [FONTE: SAS-001 §6.12; CEM-001 l.608-615; SPEC-004/005; ROADMAP §6/§7]
- O conhecimento entra por **duas fontes sob a mesma governança (CKG-009)**: (a) objetos canônicos e transições via seu **ciclo de vida** (preservando todos os estados); (b) conhecimento **formado** com **selo de publicação da SPEC-007** (contrato do selo = [DECISÃO NECESSÁRIA], dependência da SPEC-007).
- O **produtor** (agente, SAS-001 §6.12) registra relações mas **não redefine** ontologia/taxonomia; a escrita é E3 sob identidade autenticada (SPEC-004); falha de auth ⇒ não-autorizado.
- **[INFERÊNCIA]/[DECISÃO NECESSÁRIA]** — eventual **consumo** de eventos de ciclo de vida pelo KG serve só de **gatilho** para uma avaliação AUTORIZADA (CKG-009), **nunca** invalidação automática/cascata (CEM-001 l.602). O tipo `Evidence.Invalidated` é canônico (CEM-001 l.600/l.722) e a SPEC-005 o **transporta** (SPEC-005 plan l.88/l.859); o que falta é o **consumidor/contrato de consumo pelo KG** = **[DECISÃO NECESSÁRIA]**. **Emissão de eventos pelo KG NÃO é afirmada** (SPEC-005 fonta do log do Blackboard; emissão originada no KG = [DECISÃO NECESSÁRIA]).
- A **consulta** é read-only e **opcional/não-bloqueante** (SAS-001 §6.12/EC-COG-003).

### Sequência de escrita (um nó/relação)
1. **Submissão:** objeto canônico (via ciclo de vida) ou conhecimento formado (SPEC-007) propõe nó/relação.
2. **Fronteira (CKG-010, gate):** canônico admitido por ciclo de vida; formado exige selo de publicação ⇒ senão `REJECTED`.
3. **Autorização E3 (CKG-009, gate):** escritor autorizado + identidade autenticada (falha de auth ⇒ não-autorizado); produtor não redefine ontologia ⇒ senão `REJECTED`.
4. **Ontologia/integridade (CKG-001, gate):** tipo ∈ catálogo ∧ matriz §D2.1 ⇒ senão `REJECTED`.
5. **Proveniência (CKG-005, gate):** `provenance_ref.lineage` (→ `Lineage` CEM-001 / `derived_from[]` SPEC-004) + `gate_record` presentes ⇒ senão `REJECTED`.
6. **Causalidade (CKG-008, se CAUSA):** mechanism+direction+conditions+regime (+posthoc) presentes ⇒ senão `REJECTED`.
7. **Colisão (CKG-013):** se contradiz relação vigente, grava `collision_record` (ambas preservadas), não sobrescreve.
8. **Escrita append-only (CKG-006):** novo registro `ACTIVE_KNOWLEDGE`; substituição ⇒ sucessora com `supersedes`; DELETE/UPDATE de registro proibido.
9. **Temporalidade (CKG-004):** relações carregam `valid_from`/`valid_to`/`recorded_at`; a invalidação de uma relação é **ato AUTORIZADO** (novo registro sob CKG-009), **NÃO automática/em cascata** (CEM-001 l.602 "invalidação não implica cascata"; impacto é de CHM/CCM/CDM — CEM-001 l.503/606; CHM-001 l.672-676).
10. **Consumo de evento (SPEC-005) — [INFERÊNCIA]/[DECISÃO NECESSÁRIA]:** o tipo `Evidence.Invalidated` é canônico (CEM-001 l.600/l.722) e a SPEC-005 o **transporta** (plan l.88/l.859); se o KG o consome, isso **não** dispara invalidação automática de relações — serve só de GATILHO para avaliação autorizada (CKG-009). O que a SPEC-005 **não define** é o **consumidor/contrato de consumo pelo KG** = **[DECISÃO NECESSÁRIA]**. Emissão de evento PELO KG = [DECISÃO NECESSÁRIA] (SPEC-005 fonta do log do Blackboard).

> **Nota de fronteira:** memória de **trabalho** e sua ordem/versão = **SPEC-004**; **notificação** = **SPEC-005**;
> **formação** = **SPEC-007**. A SPEC-006 só **preserva, relaciona e consulta** o conhecimento permanente. [FONTE: ROADMAP §5/§6/§7]

---

## D7 — Cenários de Teste

### Cenário-CKG-T01 — Violação de integridade da ontologia → rejeição (caso que a matriz DE FATO rejeita)
```
DADO        uma relação ORIGINA cuja origem tem school=ICT (ICT nunca origina — INV-02/RULE-HH-004) — viola a matriz §D2.1
QUANDO      o gate de integridade (§D2.1) roda
ENTÃO       escrita rejeitada; nada persistido
VERIFICAÇÃO written == false; rejected_reason == "ONTOLOGY_INTEGRITY_VIOLATION"
```

### Cenário-CKG-T15 — HERDA SMC-SUB → Elliott-PRIMARY (positivo; entre escolas é VÁLIDO)
```
DADO        hipótese SUB de school=SMC com parent_id apontando para hipótese PAI de school=Elliott (hierarchy_role=PRIMARY)
QUANDO      a relação HERDA é escrita
ENTÃO       aceita (entre escolas é permitido — RULE-HH-003; "família" só restringe SUB intra-escola); nada rejeitado
VERIFICAÇÃO relation_written == true; cross_school_herda_allowed == true; parent_hierarchy_role == "PRIMARY"
```

### Cenário-CKG-T02 — observation rotulada evidence → rejeição (INV-06)
```
DADO        um nó observation sendo rotulado evidence
QUANDO      o nó é escrito
ENTÃO       rejeitado; tipos distintos preservados
VERIFICAÇÃO observation_labeled_evidence == false; rejected_reason == "OBSERVATION_IS_NOT_EVIDENCE"
```

### Cenário-CKG-T03 — Relação sem tipo/direção → rejeição
```
DADO        uma relação sem tipo do catálogo (ou sem direção) submetida
QUANDO      a validação roda
ENTÃO       relação rejeitada; nada escrito
VERIFICAÇÃO relation_written == false; rejected_reason == "RELATION_TYPE_INVALID"
```

### Cenário-CKG-T04 — Validade muda por NOVO registro (sem mutar/deletar)
```
DADO        relação criada válida desde T0 (R0), cuja informação muda em T1
QUANDO      a atualização é processada
ENTÃO       R0 intacto; novo registro de invalidação (valid_to=T1); consulta "em T0" retorna válida; "agora" não
VERIFICAÇÃO existing_record_mutated == false; existing_record_deleted == false; historical_query_consistent == true
```

### Cenário-CKG-T05 — Deleção/mutação proibida (esquecimento = arquivamento versionado)
```
DADO        tentativa de deletar fisicamente (ou reescrever) um registro arquivado
QUANDO      o gate de imutabilidade roda
ENTÃO       negado (fail-closed); registro íntegro e reconstruível
VERIFICAÇÃO physical_delete == false; record_mutated == false; history_preserved == true
```

### Cenário-CKG-T06 — Confiança não exposta ao objeto de convicção; CAUSA(custo→conviction) rejeitada
```
DADO        uma relação CAUSA(calibration_metric → conviction) submetida e uma relação com confiança registrada
QUANDO      o gate de escrita do KG roda
ENTÃO       a CAUSA(custo→conviction) é rejeitada; a confiança fica em namespace próprio, não exposta em campo do objeto de convicção
VERIFICAÇÃO confidence_exposed_in_conviction_object == false; cost_or_confidence_to_conviction_edge == false
```

### Cenário-CKG-T07 — Causal sem mecanismo/regime → rejeição (não pós-hoc)
```
DADO        relação CAUSA proposta sem mechanism/regime (só correlação)
QUANDO      o gate de saída roda
ENTÃO       relação rejeitada; exige mechanism+direction+conditions+regime
VERIFICAÇÃO causal_written == false; rejected_reason == "CAUSAL_FIELDS_MISSING"
```

### Cenário-CKG-T08 — Auth da SPEC-004 indisponível → escrita negada (fail-closed) [E3]
```
DADO        uma escrita cuja verificação de identidade da SPEC-004 está indisponível/falha
QUANDO      o gate E3 de governança roda
ENTÃO       escrita negada (fail-closed; tratada como não-autorizada)
VERIFICAÇÃO write_allowed == false; fail_closed == true; treated_as_unauthorized == true
```

### Cenário-CKG-T09 — Conhecimento formado sem selo → rejeição; canônico preserva estados (via transition record)
```
DADO        um padrão formado submetido SEM selo de publicação da SPEC-007; e, à parte, um objeto canônico que transita para REFUTED
QUANDO      o gate de fronteira roda
ENTÃO       o formado sem selo é rejeitado; o canônico REFUTED é admitido com registro canonical_state_transition (estado preservado)
VERIFICAÇÃO formed_without_seal_accepted == false; canonical_state_transition_recorded == true; canonical_states_preserved == true
```

### Cenário-CKG-T10 — Cognitive Trace Reconstruction completa (3 saltos)
```
DADO        E deriva de D; D de C; C de A e B (cadeia de 3 saltos)
QUANDO      pede-se Cognitive Trace Reconstruction de E
ENTÃO       retorna o fecho completo [A,B,C,D]; nenhum estado alterado
VERIFICAÇÃO trace == ["A","B","C","D"]; trace_complete == true; state_mutated_by_query == false
```

### Cenário-CKG-T11 — Colisão de relações registrada (não resolve em silêncio)
```
DADO        CONFIRMA(A→B) vigente e uma REFUTA(A→B) nova submetida
QUANDO      a escrita roda
ENTÃO       ambas preservadas; collision_record gravado; nenhuma apagada; resolução não decidida pelo KG
VERIFICAÇÃO both_relations_present == true; collision_logged == true; silent_overwrite == false
```

### Cenário-CKG-T12 — Nó PRIMARY sem gate/ancestral é escrito com proveniência condicional válida (caminho feliz)
```
DADO        um nó hypothesis PRIMARY (sem gate, Lineage vazio) com computed_by presente (identidade autenticada), sem gate_record e com lineage=[]
QUANDO      a escrita roda
ENTÃO       nó escrito como ACTIVE_KNOWLEDGE (lineage=[] legítimo; gate_record ausente é OK pois não há gate — espelha CBP-007)
VERIFICAÇÃO node_written == true; computed_by_present == true; lineage_empty_ok == true; knowledge_state == "ACTIVE_KNOWLEDGE"
```

### Cenário-CKG-T13 — Correção de conteúdo = nova versão (supersessão por novo registro)
```
DADO        um nó ACTIVE_KNOWLEDGE cujo conteúdo é corrigido
QUANDO      a correção roda
ENTÃO       nova versão com supersedes→anterior; a anterior permanece íntegra e não-mutada; SUPERSEDED é estado derivado
VERIFICAÇÃO old_version_preserved == true; old_version_mutated == false; supersedes_link_present == true
```

### Cenário-CKG-T14 — Escrita sem identidade autenticada → rejeição (negativo de CKG-005)
```
DADO        um nó submetido SEM computed_by (identidade autenticada ausente) — independentemente de gate_record/lineage
QUANDO      o gate de proveniência (CKG-005) roda
ENTÃO       escrita rejeitada; nada persistido (computed_by é sempre obrigatório — CBP-014)
VERIFICAÇÃO written == false; rejected_reason == "COMPUTED_BY_MISSING"
```

---

## D8 — Rigor adversarial focado (casos de negação nos pontos de risco)

> Alvo **D0–D7 + D8 adversarial focado** (CRITICAL, pin D0–D7). **18 casos** cobrindo **todas as 13 BASpecs** e as
> fronteiras/decisões abertas. Princípio transversal: **fail-closed**, **nunca deletar/mutar**, **mecanismo físico INDETERMINADO (H-001)**.

### ADV-CKG-01 — Deleção disfarçada de "esquecimento" (CKG-006/INV-07)
**DADO:** "esquecer" traduzido em DELETE físico. **QUANDO:** o gate roda. **ENTÃO:** negar; só arquivamento versionado. **PORQUE:** memória permanente nunca apaga (INV-07). **VERIFICAÇÃO:** physical_delete == false.

### ADV-CKG-02 — Sobrescrita silenciosa de relação contraditória (CKG-013)
**DADO:** REFUTA(A→B) sobre CONFIRMA(A→B). **QUANDO:** a escrita roda. **ENTÃO:** registrar colisão; preservar ambas. **PORQUE:** perder a contradição apaga conhecimento. **VERIFICAÇÃO:** silent_overwrite == false; both_relations_present == true.

### ADV-CKG-03 — Confiança de relação retroalimenta o Conviction Vector (CKG-007/INV-04)
**DADO:** tentativa de expor a confiança no objeto de convicção ou de somá-la como 9ª dimensão. **QUANDO:** a escrita/escopo é definido. **ENTÃO:** rejeitar `CONFIDENCE_IS_NOT_CONVICTION`; namespace próprio. **PORQUE:** INV-04 (custo) como base + extensão local (CKG-007); dimensionalidade=8 (fechada). **VERIFICAÇÃO:** confidence_exposed_in_conviction_object == false.

### ADV-CKG-04 — Relação causal pós-hoc por correlação (CKG-008/RULE-CAU-01/03)
**DADO:** CAUSA(A→B) só por co-ocorrência, formulada após o resultado, sem marcador. **QUANDO:** o gate roda. **ENTÃO:** rejeitar; exigir mechanism+direction+conditions+regime e marcador pós-hoc (RULE-CAU-03). **PORQUE:** correlação não é causalidade (RULE-CAU-01); regime muda a relação (RULE-CAU-02). **VERIFICAÇÃO:** causal_written == false.

### ADV-CKG-05 — Custo/score escrito como propriedade que vira convicção (INV-04)
**DADO:** custo/score de um componente ligado à convicção via nó do KG. **QUANDO:** a escrita roda. **ENTÃO:** armazenar a métrica de calibração (CEE-001 l.111) ISOLADA; rejeitar ligação custo→convicção. **PORQUE:** INV-04. **VERIFICAÇÃO:** cost_into_conviction == false.

### ADV-CKG-06 — Escrita sem proveniência aceita (CKG-005)
**DADO:** nó/relação sem provenance_ref. **QUANDO:** o gate roda. **ENTÃO:** rejeitar `PROVENANCE_MISSING`. **PORQUE:** sem origem não é reconstruível (P13). **VERIFICAÇÃO:** written == false.

### ADV-CKG-07 — Produtor redefine ontologia/taxonomia (CKG-009/SAS-001 §6.12)
**DADO:** produtor autenticado tenta alterar a ontologia global. **QUANDO:** o gate E3 roda. **ENTÃO:** negar (fail-closed); produtor registra, não redefine ontologia (ato de governança). **PORQUE:** SAS-001 §6.12. **VERIFICAÇÃO:** ontology_redefined_by_producer == false.

### ADV-CKG-08 — KG forma conhecimento / absorve SPEC-007 (CKG-010/fronteira)
**DADO:** tentativa de extração/retrieval/validação no KG. **QUANDO:** o escopo é definido. **ENTÃO:** rejeitar `OUT_OF_SCOPE_FORMATION`. **PORQUE:** formação é SPEC-007. **VERIFICAÇÃO:** formation_in_kg == false.

### ADV-CKG-09 — Mecanismo físico fixado / banco de grafos por inércia (CONS-01/mandato)
**DADO:** pressão para fixar "grafo real" (ou escolher engine). **QUANDO:** as decisões são definidas. **ENTÃO:** rejeitar `OPEN_DECISION_H001`; mecanismo físico permanece INDETERMINADO; Opção B adiada. **PORQUE:** H-001 é decisão de Andraus (CONS-01); contrato cognitivo independe dela. **VERIFICAÇÃO:** h001_decided_by_spec == false.

### ADV-CKG-10 — Absorver/duplicar vizinhos ou tocar decisão aberta (fronteiras/CONS-01)
**DADO:** a SPEC-006 virar memória de trabalho (SPEC-004), transporte (SPEC-005), estado por agente (SPEC-009), ciclo de aprendizado (SPEC-018), ou tocar M-001/J-001/N-001/G-001/K-001/C-001/WF-D03. **QUANDO:** o escopo é definido. **ENTÃO:** rejeitar `OUT_OF_SCOPE_OR_OPEN_DECISION`; decisões abertas permanecem ABERTAS (Andraus). **PORQUE:** CONS-01; INV-09. **VERIFICAÇÃO:** neighbors_absorbed == false; open_decisions_touched == false.

### ADV-CKG-11 — Nó redefine contrato canônico (CKG-002/CC-02)
**DADO:** nó-hipótese que sobrescreve campos/estado do CHM-001. **QUANDO:** a escrita roda. **ENTÃO:** rejeitar; nó referencia por id@version, não redefine. **PORQUE:** CC-02/CONST-01; INV-10. **VERIFICAÇÃO:** canonical_contract_redefined == false.

### ADV-CKG-12 — Relação viola a matriz de integridade (CKG-001/003)
**DADO:** ORIGINA com origem ICT (ICT não origina hipótese — INV-02) ou SIMILAR_A entre tipos diferentes. **QUANDO:** o gate §D2.1 roda. **ENTÃO:** rejeitar `ONTOLOGY_INTEGRITY_VIOLATION`. **PORQUE:** integridade da ontologia (INV-02; matriz). **VERIFICAÇÃO:** written == false.

### ADV-CKG-13 — Invalidação mutando o registro existente (CKG-004/INV-CBP-01)
**DADO:** `valid_to` escrito SOBRE o registro de criação (mutação). **QUANDO:** a invalidação roda. **ENTÃO:** rejeitar; invalidação só por NOVO registro. **PORQUE:** append-only real; registro histórico nunca mutado (SPEC-004 INV-CBP-01). **VERIFICAÇÃO:** existing_record_mutated == false.

### ADV-CKG-14 — Trace incompleto ou consulta que muta estado (CKG-011)
**DADO:** reconstrução que para no 1º salto, ou consulta que grava. **QUANDO:** a consulta roda. **ENTÃO:** exigir fecho completo (obrigação canônica); consulta é read-only. **PORQUE:** CEM-001 l.612-614 (completa); H-001 não rebaixa a completude. **VERIFICAÇÃO:** trace_complete == true; state_mutated_by_query == false.

### ADV-CKG-15 — Transição remove/reescreve a versão anterior (CKG-012/INV-07)
**DADO:** SUPERSEDED implementado apagando/reescrevendo a versão anterior. **QUANDO:** a transição roda. **ENTÃO:** rejeitar; a anterior é preservada; estado é projeção derivada. **PORQUE:** INV-07; INV-CBP-01. **VERIFICAÇÃO:** old_version_preserved == true; old_version_mutated == false.

### ADV-CKG-16 — evidence DERIVED admitida sem aresta DERIVA_DE por ancestral (CKG-003/INV-CKG-02)
**DADO:** um nó `evidence` DERIVED com Lineage=[C] é admitido, mas sem materializar a aresta `DERIVA_DE`→C (ancestral não referenciado). **QUANDO:** o gate de admissão roda. **ENTÃO:** rejeitar (fail-closed); exigir a aresta por ancestral; manter o grafo acíclico. **PORQUE:** sem a aresta o trace completo (CKG-011/CEM-001 l.612-614) não é garantido (INV-CKG-02). **VERIFICAÇÃO:** deriva_de_edge_per_ancestor == true; written == false (quando ancestral ausente).

### ADV-CKG-17 — hypothesis com school=ICT (viola regra de nó — INV-02/RULE-HH-004)
**DADO:** um nó `hypothesis` com `school == ICT` submetido. **QUANDO:** o gate de integridade de nó roda. **ENTÃO:** rejeitar (fail-closed) `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`; ICT nunca cria hipótese. **PORQUE:** INV-02; RULE-HH-004 (SPEC-001). **VERIFICAÇÃO:** hypothesis_school_ict_written == false.

### ADV-CKG-18 — colisão falsamente detectada / falsamente ignorada (CKG-013; escopo)
**DADO:** (a) A1 CONFIRMA B e A2 REFUTA B (origens A1≠A2) — NÃO é colisão; (b) CONFIRMA(A→B) e REFUTA(A→B) com janelas de validade DISJUNTAS — NÃO é colisão; (c) CONFIRMA(A→B) e REFUTA(A→B) vigentes com sobreposição — É colisão. **QUANDO:** o detector de colisão roda. **ENTÃO:** (a)/(b) não geram `collision_record`; (c) gera. **PORQUE:** colisão = par contraditório (§D2.2) nos MESMOS (from,to) com sobreposição temporal (CKG-013). **VERIFICAÇÃO:** collision_logged(a)==false; collision_logged(b)==false; collision_logged(c)==true.

> **Cobertura:** 18 casos — toda BASpec tem ≥1 negação: CKG-001→ADV-12/**17**; 002→ADV-11; 003→ADV-12/16; 004→ADV-13; 005→ADV-06;
> 006→ADV-01; 007→ADV-03/05; 008→ADV-04; 009→ADV-07; 010→ADV-08; 011→ADV-14/16; 012→ADV-15; 013→ADV-02/**18**. Fronteiras/decisões
> abertas: ADV-09/10. Mapeiam para EC-CKG-001..006 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada registro de nó/relação DEVE ser reconstruível (P13): tipo, `version`, `supersedes`, referência canônica
(id@version), proveniência (`provenance_ref.lineage` → `Lineage` CEM-001 / `derived_from[]` SPEC-004; `gate_record` SPEC-004), validade (`valid_from`/`valid_to`/
`recorded_at`) e `collision_record` quando houver. A **Cognitive Trace Reconstruction COMPLETA** é capacidade central do
KG (CEM-001 l.608-615; l.562-565; l.699) — especificada como comportamento verificável (CKG-011). A **observabilidade
agregada** (métricas de crescimento da memória) e a **reconstrução expandida de estado de trabalho** pertencem à SPEC-040
e à SPEC-004 — aqui ficam **por referência** (coerente com alvo D0–D7 e H-001 ABERTA). [FONTE: CONSTITUTION P13;
CEM-001 l.608-615; SPEC-004 replay; H-001 ABERTA]

---

## Contrato do nó/relação — esqueleto [PROPOSTA]

> Produto central da SPEC-006. **Referencia** os objetos canônicos por `canonical_ref`; **não** os redefine (CC-02).
> Mecanismo físico = **INDETERMINADO (H-001 ABERTA)**. Todo write é E3 (atomic-spec §10.2).

| Camada | Nó | Relação | Fronteira |
|---|---|---|---|
| Tipo de registro | `record_kind` ∈ {creation, invalidation, archival, canonical_state_transition} | `record_kind` ∈ {creation, invalidation, archival, collision} | D4/D5 (append-only; todo registro tem um kind) |
| Identidade | `node_id`, `node_type` (∈ ontologia), `version` (monotônico), `schema_version` | `relation_id`, `relation_type` (∈ ontologia), `from_node`, `to_node`, `version`, `schema_version` | tipos ∈ catálogo + matriz §D2.1 (CKG-001/003) |
| Chave natural (dedupe) | canônico: `canonical_ref`; **não-canônico** (asset/timeframe/regime/narrative/observation/learning): `natural_key` (ex.: asset="BTC"; timeframe="H4") — evita colapso quando `canonical_ref=null` | `(relation_type, from_node, to_node, valid_from)` | CKG-001/003 |
| Versionamento | `supersedes` (ref à versão anterior ou null) | `supersedes` (ou null) | append-only; estado = projeção derivada (CKG-006/012) |
| Escola/papel | `school` (Elliott/SMC/Fibonacci/ICT — campo ÚNICO; `hypothesis.school ≠ ICT`) + `hierarchy_role` {PRIMARY, SUB} (só hypothesis; ref. SPEC-001); por referência ao canônico | — | espelha, não decide (CC-01; INV-02/RULE-HH-004) |
| Referência canônica | `canonical_ref` = `canonical_id@version`; `canonical_status` (snapshot do Status canônico — CEM-001 l.264/428; CHM-001) | — | referencia, não redefine (CC-02/CKG-002); estados do KG ≠ estados canônicos (CC-10) |
| Transição canônica | registro `canonical_state_transition` = { estado, timestamp, origem, justificativa } (CEM-001 l.428) | — | preserva TODOS os estados canônicos (CEM-001 l.494) |
| Proveniência (condicional — espelha CBP-007) | `provenance_ref` = { **`computed_by` OBRIGATÓRIO** (identidade autenticada — CBP-014); `gate_record` SÓ se resulta de gate; `lineage` SÓ se derivado (→ `Lineage` CEM-001 / `derived_from[]` SPEC-004; `[]` legítimo), who, when } | idem | `computed_by` sempre; demais condicionais (CKG-005/CBP-007); nome local [PROPOSTA] |
| Publicação/escrita | `publication` = { origem: `canonical_lifecycle` \| `spec007_seal` (selo = [DECISÃO NECESSÁRIA]) }, `writer_id` (identidade autenticada — SPEC-004) | idem | governança E3 (CKG-009/010) |
| Temporalidade | `created_at`, `recorded_at` | `valid_from`, `valid_to` (null=vigente), `recorded_at` | bitemporal (CKG-004) |
| Relevância/arquivamento | `relevance` (em registro `archival`; rebaixamento sob gate E3 — CKG-012) | idem | lifecycle (CKG-012) |
| Confiança | — | `relation_confidence` (escala PRÓPRIA, namespace do KG — **PARÂMETRO a calibrar**, INDETERMINADO) | ≠ Convicção; namespace próprio (CKG-007/INV-04 custo) |
| Causalidade | — | se `CAUSA`: `mechanism`, `direction`, `conditions`, `regime`, `posthoc_flag` | RULE-CAU-01/02/03 (CKG-008) |
| Alvo relação (INVALIDA→relation) | — | `target_relation_id` (quando `to_node` é uma relação, não um nó) | matriz §D2.1 (INVALIDA) |
| Colisão | — | registro `collision` (`record_kind=collision`) referenciando as relações em conflito | CKG-013 |

> **Estado:** `knowledge_state` NÃO é campo persistido — é **projeção derivada** do conjunto de registros (D5). Estados
> transitórios `CANDIDATE_WRITE`/`REJECTED` pertencem ao fluxo de admissão (nada persistido quando rejeitado).
> **Validade/arquivamento valem para NÓ e RELAÇÃO** (RULE-CKG-012 "nó/relação"): nós também têm registros `invalidation`/
> `archival` quando aplicável. **`canonical_status`** (snapshot) + registros `canonical_state_transition` são o que sustenta
> `canonical_states_preserved` (CKG-010/T09) — o `canonical_ref@version` sozinho não carrega Status (CEM-001 l.264).

### I/O Schema (lógico — referência; não redefine CHM-001/CEM-001/CCM-001)
```json
{
  "node_record": {
    "node_id": "KG-N-2026-10-12-001",
    "record_kind": "creation | invalidation | archival | canonical_state_transition",
    "version": 1,
    "supersedes": "null | KG-N-...-v0",
    "node_type": "hypothesis | evidence | observation | conviction | narrative | mission | learning | asset | timeframe | regime | structure | calibration_metric",
    "schema_version": "1 (contrato do KG; migração de ontologia/schema = [DECISÃO NECESSÁRIA] — CKG-009)",
    "canonical_ref": "CHM-xxxx@v2 | CEM-xxxx@v1 | CCM-xxxx@v1 | null (referência; NÃO redefine o canônico)",
    "canonical_status": "(snapshot do Status canônico — CEM-001 l.264/428; CHM-001; só se canonical_ref != null)",
    "natural_key": "(identidade de nó NÃO-canônico, p.ex. asset='BTC' | timeframe='H4' — evita colapso quando canonical_ref=null)",
    "school": "Elliott | SMC | Fibonacci | ICT (campo ÚNICO; só hypothesis/structure; REGRA: hypothesis.school ≠ ICT — INV-02/RULE-HH-004)",
    "hierarchy_role": "PRIMARY | SUB (só hypothesis; ref. SPEC-001 hierarchy_role; HERDA só liga SUB a pai PRIMARY)",
    "ontological_status": "observational | theoretical (RULE-ONT-01; só structure/regime/narrative — distingue entidade medida de construção teórica, ex.: order block/liquidez)",
    "provenance_ref": { "computed_by": "OBRIGATÓRIO — identidade AUTENTICADA pelo runtime (SPEC-004 RULE-CBP-014)", "gate_record": "CONDICIONAL — só quando resulta de gate (SPEC-004 CBP-007)", "lineage": "CONDICIONAL — só quando DERIVADO (ref. ao campo Lineage do CEM-001 Cap.5 / derived_from[] da SPEC-004; [] legítimo p/ PRIMARY/asset/timeframe/regime/observation; NÃO existe lineage_ref no CEM-001)", "who": "", "when": "", "why": "", "from": "" },
    "publication": { "origin": "canonical_lifecycle | spec007_seal", "seal_ref": "[DECISÃO NECESSÁRIA — contrato do selo = SPEC-007]" },
    "writer_id": "(identidade autenticada pelo runtime — SPEC-004; falha de auth ⇒ não-autorizado)",
    "relevance": "(só em record_kind=archival; rebaixamento sob gate E3 — CKG-012)",
    "created_at": "2026-10-12T12:00:00Z",
    "recorded_at": "2026-10-12T12:00:00Z"
  },
  "canonical_state_transition_record": {
    "node_id": "KG-N-...-001", "record_kind": "canonical_state_transition",
    "canonical_status": "EMERGENT|CANDIDATE|ACTIVE|DOMINANT|SUPERSEDED|REFUTED|ARCHIVED (snapshot — CHM-001) | ACTIVE|SUPERSEDED|REFUTED|INVALIDATED|ARCHIVED (CEM-001)",
    "timestamp": "", "origem": "", "justificativa": "(CEM-001 l.428: timestamp+origem+justificativa)"
  },
  "relation_record": {
    "relation_id": "KG-R-2026-10-12-001",
    "record_kind": "creation | invalidation | archival | collision",
    "version": 1,
    "supersedes": "null | KG-R-...-v0",
    "relation_type": "CONFIRMA | REFUTA | DEPENDE_DE | HERDA | PERTENCE_A | INVALIDA | ORIGINA | DERIVA_DE | SIMILAR_A | CAUSA | HIERARQUIA_DE | ESTATISTICA_DE",
    "from_node": "KG-N-...-A",
    "to_node": "KG-N-...-B (nó) ",
    "target_relation_id": "null | KG-R-...-X (quando o alvo é uma RELAÇÃO — ex.: INVALIDA→relation; matriz §D2.1)",
    "provenance_ref": { "computed_by": "OBRIGATÓRIO (identidade autenticada — SPEC-004 CBP-014)", "gate_record": "CONDICIONAL (só se resulta de gate)", "lineage": "CONDICIONAL (só se derivado; → Lineage CEM-001 / derived_from[] SPEC-004)", "who": "", "when": "" },
    "writer_id": "(identidade autenticada — SPEC-004)",
    "valid_from": "2026-10-12T12:00:00Z",
    "valid_to": "null (vigente) | timestamp (invalidada por NOVO registro — preservada)",
    "recorded_at": "2026-10-12T12:00:00Z",
    "relation_confidence": "escala PRÓPRIA em namespace do KG — PARÂMETRO a calibrar (INDETERMINADO; NÃO é Convicção; nunca exposta ao objeto de convicção; não toca J-001/N-001)",
    "causal": "{ mechanism, direction, conditions, regime, posthoc_flag } (obrigatório sse relation_type == CAUSA — RULE-CAU-01/02/03)"
  },
  "collision_record": {
    "record_kind": "collision", "relation_a": "KG-R-...-X", "relation_b": "KG-R-...-Y",
    "detected_at": "", "note": "ambas preservadas; resolução = SPEC-007/SPEC-018 ou governança (CKG-013)"
  }
}
```
> Nenhum campo computa convicção nem deriva de custo (INV-04). `knowledge_state` é projeção derivada, não campo.
> Mecanismo físico = INDETERMINADO (H-001 ABERTA).

---

## Enforcement Contracts

### EC-CKG-001 — Escrita de nó/relação no KG permanente [E3]
```
CAPABILITY   : Escrever um nó/relação válido no KG permanente
EFFECT       : Persistência de conhecimento permanente (commit crítico/irreversível; append-only)
PRECOND      : (tipo ∈ ontologia ∧ matriz de integridade §D2.1 — CKG-001/003) AND (nó canônico referenciado, não redefinido — CKG-002) AND (proveniência presente — CKG-005) AND (fronteira: ciclo de vida canônico ∨ selo SPEC-007 — CKG-010) AND (CAUSA ⇒ mechanism+direction+conditions+regime — CKG-008) AND (colisão registrada se houver — CKG-013)
POSTCOND     : novo registro ACTIVE_KNOWLEDGE com proveniência/validade; versão anterior preservada e não-mutada em caso de supersessão
POLICY       : RULE-CKG-001/002/003/005/008/010/013; CEM-001 l.608-615; CC-02
LEVEL        : E3 (Crítico — "KG publicado → E3 mínimo", atomic-spec §10.2; irreversível)
FAILURE-MODE : Fail-closed — qualquer precondição falha ⇒ REJECTED; nada persistido; log. **Falso-DENY E3 CONDICIONAL até o limiar amostral ser definido (gap aberto, ENF-07)** (atomic-spec §12)
EVIDENCE     : registro reconstruível (tipo/version/supersedes/ref canônica/proveniência/validade) + amostragem de falso-DENY (ENF-07)
```

### EC-CKG-002 — Imutabilidade / append-only / versionamento [E3]
```
CAPABILITY   : Impedir deleção/mutação de registro e garantir transições versionadas
EFFECT       : Transição por NOVO registro (SUPERSEDED/ARCHIVED/INVALIDATED_IN_TIME) — nunca remoção nem reescrita
PRECOND      : (operação ∉ {DELETE físico, UPDATE de registro}) AND (sucessora aponta para a anterior por supersedes quando substitui)
POSTCOND     : histórico preservado e reconstruível; estado = projeção derivada; nenhum registro removido/mutado (INV-07; INV-CBP-01)
POLICY       : RULE-CKG-004/006/012; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01; INV-CKG-01
LEVEL        : E3 (Crítico — perda/reescrita de histórico é irreversível; fail-closed)
FAILURE-MODE : Fail-closed — tentativa de DELETE/UPDATE ⇒ negada; log. **Falso-DENY E3 CONDICIONAL até limiar (ENF-07)**
EVIDENCE     : gate_record de imutabilidade + **registro das tentativas de DELETE/UPDATE bloqueadas (observabilidade do gate)** + ENF-07 (bloqueio indevido de arquivamento legítimo)
```

### EC-CKG-003 — Governança de escrita (autorizado + autenticado; não redefine ontologia) [E3]
```
CAPABILITY   : Admitir escrita só de escritor autorizado/autenticado, sem redefinição de ontologia pelo produtor
EFFECT       : Autorização (ou recusa) de escrita permanente no KG
PRECOND      : (escritor ∈ autorizados ∧ identidade AUTENTICADA pelo runtime — SPEC-004 CBP-014; auth indisponível/falha ⇒ não-autorizado) AND (operação ∉ {redefinir ontologia/taxonomia global} — SAS-001 §6.12) AND (gate determinístico — ENF-03)
POSTCOND     : só escritor autorizado escreve; produtor registra relações, não redefine ontologia (ato de governança)
POLICY       : RULE-CKG-009; SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04
LEVEL        : E3 (Crítico — escrita em memória permanente; cruza fronteira de confiança)
FAILURE-MODE : Fail-closed — escritor não autorizado / falha de auth da SPEC-004 / tentativa de redefinir ontologia ⇒ negada; log. **Falso-DENY E3 CONDICIONAL até limiar (ENF-07)**
EVIDENCE     : gate_record de autorização por identidade autenticada + amostragem de falso-DENY (ENF-07)
```

### EC-CKG-004 — Confiança de relação em namespace próprio do KG (guard local; INV-04 custo como base)
```
CAPABILITY   : Manter a confiança de relação em namespace próprio do KG e não escrever arestas custo/confiança→conviction
EFFECT       : Guard (na escrita do KG) de que confiança não é exposta ao objeto de convicção nem vira aresta para `conviction`
PRECOND      : (confiança de relação em namespace separado) AND (matriz §D2.1 proíbe CAUSA custo/confiança→conviction)
POSTCOND     : nenhum campo do objeto de convicção recebe a confiança do KG; nenhuma aresta custo/confiança→conviction é escrita
POLICY       : RULE-CKG-007; INV-04 (custo); CCM-001
LEVEL        : E2 (Operacional — guard constitutivo sobre a ESCRITA do KG; INV-04 base)
FAILURE-MODE : Fail-closed — tentativa de expor confiança no objeto de convicção / aresta custo/confiança→conviction ⇒ negada; log
EVIDENCE     : verificação (na escrita do KG) de namespace separado e ausência da aresta. A garantia de que o CÁLCULO de
               convicção (SPEC-003/CCM-001) não consome a confiança é requisito endereçado à SPEC-003 / [DECISÃO NECESSÁRIA] — fora do controle do KG
```

### EC-CKG-005 — Registro de relação causal com mecanismo/regime (RULE-CAU) [E3]
```
CAPABILITY   : Admitir relação causal apenas com mechanism+direction+conditions+regime (+posthoc quando aplicável)
EFFECT       : Escrita (ou recusa) de relação CAUSA — persistência permanente (E3)
PRECOND      : (relation_type == CAUSA) ⇒ (mechanism ∧ direction ∧ conditions ∧ regime presentes; posthoc_flag quando aplicável); gate de saída determinístico (Classe H); bounded loop no juízo
POSTCOND     : relações causais têm campos auditáveis; nenhuma causal pós-hoc por correlação sem marcador
POLICY       : RULE-CKG-008; RULE-CAU-01/02/03; ENF-03
LEVEL        : E3 (Crítico — é um write permanente; herda EC-CKG-001)
FAILURE-MODE : Fail-closed — campos ausentes ⇒ rejeitada; retry bounded (sem retry infinito). **Falso-DENY E3 CONDICIONAL até limiar (ENF-07)**
EVIDENCE     : registro dos campos causais por relação; contagem de tentativas ≤ limite; o gate verifica presença, não veracidade (ENF-03); **amostragem de falso-DENY (ENF-07 — método amostral, limiar = gap aberto)**
```

### EC-CKG-006 — Consulta cognitiva / Cognitive Trace Reconstruction (read-only)
```
CAPABILITY   : Responder consultas e reconstruir a cadeia cognitiva COMPLETA sem alterar estado
EFFECT       : Leitura/navegação de nós e relações (sem escrita)
PRECOND      : (consulta é read-only) AND (consumidor autorizado a ler)
POSTCOND     : resposta/trace COMPLETO retornado; nenhum estado alterado pela consulta
POLICY       : RULE-CKG-011; CEM-001 l.608-615/l.612-614; SAS-001 §6.12
LEVEL        : E1 (Contratual — leitura observável; não muta estado)
FAILURE-MODE : Fail-closed — consulta que tente mutar estado ⇒ negada; completude do trace é obrigatória; eficiência de consulta ampla = INDETERMINADO até H-001
EVIDENCE     : log de consulta read-only; trace = fecho transitivo das arestas DERIVA_DE
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
Serviço lógico de **memória semântica permanente** (Opção A — camada sobre o conhecimento já validado/publicado).
Combina gates constitutivos determinísticos (Classe C: ontologia/integridade, proveniência, imutabilidade/append-only,
governança de escrita E3, fronteira, isolamento confiança×convicção, colisão) + mecânica determinística (Classe D:
catálogo, temporalidade bitemporal, lifecycle, consulta/trace completo) + um juízo com gate de saída (Classe H:
proposta de similaridade/causalidade sob mecanismo+regime). **Não guarda memória de trabalho, não transporta, não forma
conhecimento, não decide, não computa convicção, não executa ordem, e NÃO escolhe o mecanismo físico (H-001 ABERTA).**
[FONTE: ROADMAP §6; CEM-001 l.608-615; SAS-001 §6.12; research.md §3/§4]

### Roteamento de modelo (CEE-001 §5)
Gates C/D **não requerem LLM**. O juízo de similaridade/causalidade (Classe H, CKG-008) pode usar apoio semântico
**apenas como detector** para PROPOR; o gate de saída que verifica a presença dos campos é **determinístico** (ENF-03).
Mecanismo físico = **INDETERMINADO = H-001 (ABERTA)**. [FONTE: CEE-001 §5; ENF-03; H-001 ABERTA]

### Dependências técnicas
CEM-001 (BASELINE — l.608-615; l.562-565/l.699; l.494) · CHM-001 · CCM-001 · CEE-001 l.111 · SAS-001 §6.12 · SPEC-004 v1.2
(BASELINE — proveniência/`gate_record`/identidade; INV-CBP-01 append-only) · SPEC-005 v1.0 (BASELINE — eventos consumidos;
emissão pelo KG = [DECISÃO NECESSÁRIA]) · SPEC-007 (fronteira — selo de publicação, ainda não especificada = [DECISÃO
NECESSÁRIA]) · CONSTITUTION l.233 · RULES.md (RULE-BB-004, RULE-CAU-01/02/03, RULE-MECH-01, RULE-HD-02/03/04) · SPEC-019
(governança da ontologia) · SPEC-019/020/021 v1.0 · atomic-spec v1.5 (§10.2 E3) · INV-04/05/06/07/09/10 · ENF-01..08.
Referências externas [EXTERNO], não-baseline: research.md §2 (SRC-ZEP-01, SRC-PROV-01, SRC-MEMVSKG-01, SRC-FORGET-01 —
DADO não-verbatim) e §5 (REPO-graphiti/graphrag/cognee/mem0 — elegíveis, nenhum adotado).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Over-engineering: banco de grafos por inércia do nome "Graph" | Opção A; Opção B ADIADA (research.md §3.5); mecanismo físico = H-001 (ABERTA); ADV-CKG-09 |
| Fixar H-001 por engano | contrato cognitivo independe de H-001; H-001 [DECISÃO NECESSÁRIA]; ADV-CKG-09; CONS-01 |
| Invadir/absorver a SPEC-007 (formação/retrieval) | Non-goal; CKG-010 (selo); ADV-CKG-08 |
| Reabrir/duplicar SPEC-004/005 | CC-02; cobertura×lacuna; INV-09; ADV-CKG-10 |
| Confiança de relação virar Convicção | INV-04; CKG-007; EC-CKG-004; ADV-CKG-03/05 |
| Deleção/mutação disfarçada de "esquecimento" | INV-07; INV-CBP-01; RULE-CKG-006/012; EC-CKG-002 (E3); ADV-CKG-01/13/15 |
| Causalidade pós-hoc / sem regime | RULE-CAU-01/02/03; CKG-008; EC-CKG-005; ADV-CKG-04 |
| Colisão de relações resolvida em silêncio | CKG-013; EC-CKG-001 (POLICY cita RULE-CKG-013); ADV-CKG-02 |
| Escrita sem proveniência / produtor redefine ontologia / auth falha-aberto | CKG-005/009; EC-CKG-001/003 (E3); SAS-001 §6.12; ADV-CKG-06/07 |
| Redefinir contrato canônico | CKG-002; EC-CKG-001; ADV-CKG-11; CC-02 |
| Violar matriz de integridade (ex.: ICT origina) | CKG-001; §D2.1; EC-CKG-001; ADV-CKG-12; INV-02 |
| Trace incompleto / consulta que muta | CKG-011; EC-CKG-006; ADV-CKG-14; CEM-001 l.612-614 |
| LLM como gate de escrita/causalidade | ENF-03; EC-CKG-003/005 (detector≠gate) |
| Ontologia inconsistente / mudança sem governança | matriz §D2.1; governança spec-time (SPEC-019)/runtime (K-001 [DECISÃO NECESSÁRIA]); CKG-009 |
| Crescimento ilimitado da memória | lifecycle versionado (CKG-012); observabilidade = SPEC-040 (por referência) |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz o schema lógico do **registro de nó/relação do KG**; nenhum schema canônico nem das SPEC-004/005 alterado.
- **RAG/KG:** especifica o contrato do próprio KG; formação/retrieval permanece em SPEC-007 (não absorvida).
- **Skills:** nenhuma Skill afetada; INV-06 preservado (`observation` ≠ `evidence`).
- **Testes:** adiciona `checks.md`; mecanismo físico fica para BUILD (H-001).
- **Modelos/Specs dependentes:** CEM/CHM/CCM/SPEC-004/005 não alterados; RULE-BB-004 reforçada no eixo permanente.
- **Compatibilidade:** Minor — não toca modelo canônico baselined, não reabre SPEC-004/005, não fecha decisão aberta (H-001 permanece ABERTA).

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07), a
Classe por BASpec (CC-11) e o **mecanismo físico** (hoje INDETERMINADO, **H-001**). O fechamento de H-001 é decisão de
Andraus; a homologação do Plan **não** o exige (contrato cognitivo fechável com mecanismo físico aberto — Opção A).

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — pergunta adversarial por BASpec com efeito (cobertura das 13 BASpecs CRITICAL):**

- **CKG-001 (ontologia/integridade + regra de nó, C):** se errada → violação da matriz, ou hypothesis.school=ICT, ou HERDA→pai não-PRIMARY persistidos → observável; verificável. Negação: ADV-CKG-12/**17**, T01; caso POSITIVO cross-escola: T15.
- **CKG-002 (ref canônica, D):** se errada → contrato canônico redefinido, ou observation=evidence → observável; verificável. Negação: ADV-CKG-11, T02.
- **CKG-003 (relação tipada, D):** se errada → relação sem tipo/direção/proveniência, ou evidence DERIVED sem aresta DERIVA_DE por ancestral → observável; verificável. Negação: ADV-CKG-12/16, T03 (e caso-feliz T12).
- **CKG-004 (temporalidade, D):** se errada → registro existente mutado/deletado → observável por `existing_record_mutated=true`; verificável. Negação: ADV-CKG-13, T04. QUANDO-sim-mas-ENTÃO-não: consulta "agora" não retorna invalidada (correto).
- **CKG-005 (proveniência condicional, C):** se errada → nó sem `computed_by` aceito, OU gate_record/lineage forçados onde não há gate/ancestral → observável; verificável. Negação: ADV-CKG-06, **T14** (sem computed_by); caso-feliz condicional: T12 (PRIMARY com lineage=[]).
- **CKG-006 (imutabilidade, C/E3):** se errada → DELETE/UPDATE ocorre → observável; verificável. Negação: ADV-CKG-01, T05.
- **CKG-007 (confiança≠convicção, C):** se errada → confiança entra na convicção → observável; verificável. Negação: ADV-CKG-03/05, T06.
- **CKG-008 (causal c/ mecanismo+regime, H):** se errada → causal pós-hoc/sem regime escrita → observável; verificável. Negação: ADV-CKG-04, T07.
- **CKG-009 (governança E3, C):** se errada → auth falha-aberto ou produtor redefine ontologia → observável; verificável. Negação: ADV-CKG-07, T08.
- **CKG-010 (fronteira, C):** se errada → formado sem selo entra, ou estado canônico perdido → observável; verificável. Negação: ADV-CKG-08, T09.
- **CKG-011 (consulta/trace completo, D):** se errada → trace incompleto ou consulta muta → observável por `trace_complete=false`; verificável. Negação: ADV-CKG-14, T10.
- **CKG-012 (lifecycle, D):** se errada → versão anterior removida/mutada → observável; verificável. Negação: ADV-CKG-15, T13.
- **CKG-013 (colisão, C):** se errada → contraditória sobrescrita em silêncio, OU colisão falsa (origens distintas/validades disjuntas) → observável; verificável. Negação: ADV-CKG-02/**18**, T11; escopo em §D2.2.

Todas as 13 BASpecs têm ENTÃO verificável por observador independente e ≥1 caso de negação em D8. Nenhuma restou como
[DECISÃO NECESSÁRIA] por falta de verificabilidade (H-001/selo SPEC-007/M-001/J-001/N-001/G-001/K-001/C-001/WF-D03 são
fronteiras/decisões abertas explícitas, não falhas de verificabilidade).

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista CEM-001 (l.494/608-615/562-565/699), CHM-001, CCM-001,
CEE-001 l.111, SAS-001 §6.12, SPEC-004 v1.2 (INV-CBP-01; `gate_record`), SPEC-005 v1.0, RULE-BB-004, RULE-CAU-01/02/03,
CONSTITUTION l.233, atomic-spec v1.5, ENF-01..08, INV-04/05/06/07/09/10. Evidência por obrigação herdada:
- CEM-001 "preservar TODOS os estados / trace COMPLETO" → CKG-010 (preserva REFUTED/SUPERSEDED/ARCHIVED) + CKG-011 (trace completo, não rebaixado por H-001); não redefine.
- CEM-001 Cap.5 `Lineage` → tipo DERIVA_DE (aresta navegável) + `provenance_ref.lineage` (campo local [PROPOSTA] que referencia `Lineage`/`derived_from[]`), distinguidos.
- CHM-001 (estados/versionamento) → CKG-002/012 por referência; não transiciona.
- CCM-001 → CKG-007/EC-CKG-004 isolam confiança (INV-04).
- SPEC-004 v1.2 INV-CBP-01 (append-only real; registro nunca mutado) → CKG-004/006/012 (novos registros; estado derivado); `gate_record` reatribuído à SPEC-004 (não CEM-001).
- SPEC-005 (eventos) → D6 consome; emissão pelo KG NÃO afirmada ([DECISÃO NECESSÁRIA]).
- SAS-001 §6.12 (produtor não redefine ontologia) → CKG-009/EC-CKG-003.
- RULE-BB-004/INV-07 → CKG-006/012.
- RULE-CAU-01/02/03 → CKG-008 (mechanism+regime+posthoc).
- CEE-001 l.111 → ADV-CKG-05 (métrica isolada).
- atomic-spec §10.2 ("KG publicado → E3") → EC-CKG-001/002/003/005 em E3.
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (único MODIFIED = RULE-BB-004 reforçada — RULE-HD-02).
**Eixo VERTICAL (RULE-HV) não aplicável.**

**Bloco C — epistêmico / disciplinas N8–N17 (verificado — achado / sem achado):**
- **RULE-EPI-01..03:** sem achado — H-001/mecanismo físico = INDETERMINADO (não fato); nenhuma hipótese tratada como fato.
- **RULE-SEM-01/04:** sem achado — acepções declaradas (CC-10); termos canônicos não redefinidos.
- **RULE-ONT-01/02 (ontológica):** **verificado** — a ontologia do KG (tipos/entidades/matriz §D2.1) é declarada explicitamente, com "família estrutural" definida; nós de **construção teórica** (structure/regime/narrative — order block, liquidez) carregam `ontological_status` ∈ {observational, theoretical} (RULE-ONT-01, RULES.md l.671), distinguindo entidade medida de postulada; nenhum tipo canônico redefinido; alteração de ontologia por governança (RULE-ONT-02/CKG-009). Sem achado residual.
- **RULE-INQ (inquirição):** **verificado** — questões abertas (H-001, selo SPEC-007, allowlist de escritores, host do juízo CKG-008, migração de ontologia) formuladas como [DECISÃO NECESSÁRIA], não respondidas por suposição; sem achado.
- **RULE-CAU-01/02/03:** sem achado — CKG-008 exige mechanism+direction+conditions (01), regime (02) e marcador pós-hoc (03); gate verifica presença, não veracidade (ENF-03).
- **RULE-CTF (contrafactual):** **verificado** — nenhuma afirmação contrafactual carregada no Plan; o "o que seria observável se a BASpec estivesse errada" (Bloco A) é usado só como teste de verificabilidade, não como alegação; sem achado.
- **RULE-UNC-01..03 (incerteza):** sem achado — incerteza localizada (eficiência de consulta ampla até H-001) declarada; completude do trace NÃO é incerta (obrigação).
- **RULE-PRB (probabilidade):** sem achado — nenhuma probabilidade/precisão numérica declarada; confiança de relação = PARÂMETRO a calibrar, sem número.
- **RULE-DEC-01 (decisão≠execução):** sem achado — o KG armazena/relaciona/consulta; não decide nem executa (INV-05).
- **RULE-MET-01 (não-fabricação):** sem achado — IDs arXiv implausíveis descartados (research.md §aviso); **SRC-FORGET-01 é DADO não-verbatim (WebSearch) e NÃO sustenta sozinha nenhuma alegação carregada** — "esquecimento=arquivamento" apoia-se em INV-07/RULE-BB-004 (FATO NORMATIVO), com SRC-FORGET-01 só como contexto.

**Bloco D — reforço de escopo:** a Spec **preserva/relaciona/consulta** conhecimento permanente, **não guarda trabalho**
(SPEC-004), **não transporta** (SPEC-005), **não forma conhecimento** (SPEC-007), **não executa** ordem (INV-05/RULE-DEC-01
— §7), **não decide** nem **computa** convicção. Nenhuma BASpec cruza a fronteira SOT→execução downstream. Dependências de
decisão de Andraus (homologação; RULE-CKG/contrato; **H-001**; selo SPEC-007; allowlist/host do juízo; migração de
ontologia) marcadas [PROPOSTA]/[DECISÃO NECESSÁRIA], não fechadas; M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001
abertas, não tocadas.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001; CHM-001; CCM-001; CEE-001; SAS-001; SPEC-004 v1.2; SPEC-005 v1.0; SPEC-001/019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5 (§10.2 E3); RULES v1.5 (RULE-BB-004, RULE-CAU-01/02/03, RULE-MECH-01, RULE-HD-*); INV-*; ENF-*; CONSTITUTION l.233 | [FONTE] | FATO NORMATIVO |
| RULE-CKG-001..013; INV-CKG-01; matriz §D2.1; contrato de nó/relação; BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Fontes SRC-ZEP-01/PROV-01/MEMVSKG-01; REPO-graphiti/graphrag/cognee/mem0 | [EXTERNO] | Referência — DADO, nunca baseline |
| SRC-FORGET-01 (sumário WebSearch) | [EXTERNO] | DADO **não-verbatim** — não sustenta sozinha alegação carregada (§7-bis Bloco C) |
| Mecanismo físico de armazenamento | [DECISÃO NECESSÁRIA] | **H-001 — EM ABERTO — não fechar** (Andraus; contrato cognitivo independe dela) |
| Banco de grafos dedicado (Opção B) | [DECISÃO NECESSÁRIA] | **ADIADO** — registrado, não apagado (INV-07) |
| Escala numérica de confiança de relação | [DECISÃO NECESSÁRIA] | **PARÂMETRO a calibrar** — INDETERMINADO (não toca J-001/N-001) |
| Contrato do selo de publicação (entrada de conhecimento formado) | [DECISÃO NECESSÁRIA] | Dependência da **SPEC-007** (ainda não especificada) |
| Allowlist de escritores autorizados / host do juízo CKG-008 / migração de ontologia | [DECISÃO NECESSÁRIA] | Runtime/governança (K-001/SPEC-018; SPEC-019 spec-time) — não decidido aqui |
| Emissão de evento "conhecimento mudou" pelo KG | [DECISÃO NECESSÁRIA] | Dependente da SPEC-005 (fonta do log do Blackboard) — não afirmada |
| Componente "Cognitive Ontology" separado | [DECISÃO NECESSÁRIA] | Ontologia DENTRO da SPEC-006 (Q-ABERTURA-4); criar componente é de Andraus (não feito) |
| Enum de estados do Blackboard p/ objetos não-hipótese | [DECISÃO NECESSÁRIA] | **M-001 — EM ABERTO (SPEC-004)** — não tocado |
| Fórmula/pesos/limiares do Conviction Vector; pesos por ativo | [DECISÃO NECESSÁRIA] | **J-001 / N-001 — EM ABERTO (SPEC-003/backtest)** — não tocadas |
| Estado persistente por agente / ciclo de evolução (P12) | [DECISÃO NECESSÁRIA] | **G-001 / K-001 — EM ABERTO (SPEC-009/018)** — não tocadas |
| Granularidade EARS multi-condição / relação convicção-macro-global | [DECISÃO NECESSÁRIA] | **C-001 / WF-D03 — EM ABERTO** — não tocadas |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-006 confirmada (§6/§21); FASE 3, após SPEC-005 BASELINE v1.0.
[x] atomic-spec.md lido: método v1.5 (CC-11/CC-12; RULE-MECH-01; RULE-ECC-04/06; §15 Dossiê; §3 CRITICAL·D0–D7; §10.2 "KG publicado → E3").
[x] Nenhum invariante congelado violado (INV-01..10). INV-04/05/06/07/09/10 reforçados; memória permanente imutável (INV-CKG-01); escrita = E3.
[x] Constitution Check CC-01..CC-12 (N/A justificados CC-06/07/12; CC-02/CC-08/CC-09/CC-10/CC-11 INCIDEM e aplicados).
[x] Disciplinas N8–N17: tratadas uma a uma no §7-bis Bloco C (RULE-EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET) — "verificado/sem achado".
[x] Referências externas [EXTERNO] classificadas; engines externas NÃO adotadas; verbatim em sources/ (RULE-ECC-04); repositórios régua Equilibrada (RULE-ECC-06 — 4 elegíveis); SRC-FORGET-01 marcada DADO não-verbatim.
[x] RULE-ECC-05 (Multi-Lente): NÃO-incidência (infra de memória) confirmada (DHR-SPEC006-001 §2); conformidade WORKFLOW por prudência; não fecha WF-D03.
[x] Spec sem implementação (BUILD adiado); Plan derivado da abertura homologada; Tasks adiadas.
[x] Critérios em EARS (13); BASpecs completas (CKG-001..013) com Classe (CC-11); RULEs citadas existentes vs propostas etiquetadas.
[x] Profundidade D0–D7 (+ D8 focado) atingida; D2.1 (matriz) + D2.2 (colisão); D4; D5 (estado derivado); D6; D7 x15 (T01..T15); D8 ADV-CKG-01..18; D9 por referência.
[x] Enforcement Contract em todo ato com efeito (EC-CKG-001..006); **escrita permanente = E3** (atomic-spec §10.2); E1 consulta; E2 guard de isolamento; ENF-07 amostral nos E3 — CONDICIONAL até o limiar (gap aberto).
[x] Status epistemológico aplicado (FATO NORMATIVO / PROPOSTA / EXTERNO / DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 permanecem ABERTAS; nenhuma decisão aberta usada como invariante fechado.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos/achados da Rodada 2 (A, B1-4, C1-22, Extra) tratados — ver relatório; append-only como novos registros alinhado à SPEC-004 INV-CBP-01; gate_record reatribuído à SPEC-004.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE fabricada; linhas canônicas verificadas (CEM-001 l.494/562-565/608-615/699; SAS-001 §6.12; CONSTITUTION l.233; CEE-001 l.111; RULE-BB-004 l.323; RULE-CAU-01/02/03 l.680-682; SPEC-004 INV-CBP-01; RMR-001 l.128 (BL-029)/l.192 (DHR-SPEC006-PEND-001) BL-029 `Em espera`).
[x] 4Es na ordem; Conformidade > Eficácia. Latência não é material para memória permanente (consulta opcional/não-bloqueante — SAS-001 §6.12).
[x] Dependências a montante homologadas; não downstream de bloqueador aberto não resolvido (H-001 é desta Spec — proposta de recorte; selo SPEC-007 marcado como dependência [DECISÃO NECESSÁRIA]).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); Bloco A cobre as 13 BASpecs; Bloco C cobre N8–N17 uma a uma — obrigatório CRITICAL.
[x] CC-11/§10.6: Classe por BASpec; Classes C com gate de saída; Classe H (CKG-008) com bounded loop + gate de saída.
[x] Abertura (RULE-ECC-01/02/04/06): Dossiê presente e HOMOLOGADO (DHR-SPEC006-001); escopo/quantidade/número homologados (1 Spec).
[x] Passo 11-bis: nenhum gatilho spec:SPEC-006 isolado; BL-003/BL-010/BL-011 tratados; **BL-029 = `Em espera`** (corrigido), independente.
[ ] Gate determinístico (validate_spec_sot.py), check_repo_research.py, build_map.py --check, check_doc_sync.py: **NÃO executáveis por mim (sem Bash)** — reportados ao caller.
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] / abertas nesta Spec (não fechadas — CONS-01):
- **H-001** — a SPEC-006 **propõe o recorte** (contrato cognitivo independe do mecanismo físico), mas **não decide** — é de Andraus. Permanece ABERTA.
- **Opção B (banco de grafos dedicado)** — ADIADA (registrada, não apagada — INV-07).
- **Escala de confiança de relação** — PARÂMETRO a calibrar (INDETERMINADO; não toca J-001/N-001).
- **Contrato do selo de publicação** (entrada de conhecimento formado) — dependência da **SPEC-007**; [DECISÃO NECESSÁRIA].
- **Allowlist de escritores / host do juízo CKG-008 / migração de ontologia** — runtime/governança (K-001/SPEC-018; SPEC-019); [DECISÃO NECESSÁRIA].
- **Emissão de evento pelo KG** — dependente da SPEC-005; [DECISÃO NECESSÁRIA] (não afirmada).
- **Componente "Cognitive Ontology" separado** — não criado; ontologia DENTRO da SPEC-006 (Q-ABERTURA-4); é de Andraus.
- **M-001 / J-001 / N-001 / G-001 / K-001 / C-001 / WF-D03 / ECC-03-001** — permanecem ABERTAS; não tocadas.

Carregado para o Revisor:
- Cobertura × lacuna (canônicos/SPEC-004/005) com arquivo:linha — a SPEC-006 **não duplica** linhagem/versões/estados/proveniência/append-only (herdados; CC-08); lacuna real = ontologia+matriz, catálogo (+ DERIVA_DE, observation), temporalidade bitemporal, confiança de relação, consulta/trace, governança de escrita.
- Baselines que citam o KG tratadas **sem erratum** (número/nome preservados): CEM-001 l.494/562-565/608-615/699, SAS-001 §6.12/l.163, CONSTITUTION l.233, CEE-001 l.111 (research.md §6.4; INV-09).
- **H-001** apresentada como **[DECISÃO NECESSÁRIA]** — recorte proposto, **não** fechada — decisão de Andraus.
- Escrita permanente = **E3 fail-closed** (EC-CKG-001/002/003/005; atomic-spec §10.2); imutabilidade = E3; governança = E3; falso-DENY E3 CONDICIONAL até o limiar (gap aberto, ENF-07).
- Append-only como **novos registros** (estado = projeção derivada) — alinhado à SPEC-004 INV-CBP-01 (registro histórico nunca mutado).
- Cognitive Trace Reconstruction = obrigação **completa** (independe de H-001); só a eficiência de consulta ampla fica INDETERMINADA.
- Confiança de relação **≠ Convicção** (INV-04) — isolada (CKG-007/EC-CKG-004); não toca J-001/N-001.
- Causalidade sob **RULE-CAU-01/02/03** — mechanism+regime+posthoc; gate verifica presença, não veracidade (ENF-03).
- **BL-029 = `Em espera`** (corrigido; gatilho SPEC-014/018/045; independente desta Spec).
- Possível risco de volume (CRITICAL, 13 BASpecs/15 cenários/18 ADV + matriz §D2.1/§D2.2 + schema expandido): se o Revisor/Andraus julgar que excede uma sessão de revisão, a divisão é decisão de Andraus (Q-ABERTURA-5) — o Especificador **não** divide por conta própria; slot preservado (INV-07).
