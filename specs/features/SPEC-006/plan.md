# SPEC-006 — Cognitive Knowledge Graph

| Campo | Valor |
|---|---|
| ID | SPEC-006 — Cognitive Knowledge Graph (contrato cognitivo da **memória semântica permanente** do SOT — ontologia enxuta + entidades/relações tipadas + temporalidade + proveniência por referência + lifecycle + confiança de relação + consulta cognitiva + governança de escrita; **mecanismo físico de armazenamento INDETERMINADO — H-001 ABERTA**) |
| Versão | 1.5 (candidato a BASELINE — rodada 6) |
| Status | **CANDIDATO — aguarda verificação de spec (checks.md), gate determinístico, parecer do Revisor e homologação de Andraus.** NÃO é baseline (INV-09). **Hoje o KG é integralmente fail-closed** (todo caminho de entrada depende de [DECISÃO NECESSÁRIA] — §D2.3); o contrato é verificável por predicados de gate e fixtures, a admissão positiva fim a fim é INDETERMINADO. Abertura HOMOLOGADA: DHR-SPEC006-001 (2026-10-11). As RULE-CKG-* e o contrato de nó/relação deste Plan são **[PROPOSTA]** até homologação. **H-001 (mecanismo físico do KG) permanece ABERTA — este Plan NÃO a fecha** (CONS-01; só Andraus). M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 seguem ABERTAS. |
| Fonte | ROADMAP §6 (FASE 3); `specs/features/SPEC-006/ABERTURA.md` + `research.md` + `sources/` (Dossiê — RULE-ECC-01/02/04/06; validade CRITICAL 90 dias, limite 2027-01-03); DHR-SPEC006-001; atomic-spec **v1.5** (§3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7); `governance/RULES.md` (RULE-BB-004, RULE-CAU-01/02/03, RULE-MECH-01, RULE-HD-02/03/04); `canon/CEM-001` (Responsabilidades do KG l.608-615), `canon/CHM-001`, `canon/CCM-001`, `canon/CEE-001` l.111, `canon/SAS-001` §6.12; `WORKFLOW.md` (conformidade, não editada) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §6 "P0 — CRITICAL"; atomic-spec §3 (emenda SPEC006-MATRIZ, 2026-10-05) "Knowledge Graph \| CRITICAL \| D0–D7"; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profundidade-alvo | **D0–D7 + D8 adversarial focado** nos pontos sensíveis (imutabilidade INV-07, confiança de relação ≠ Convicção INV-04, causalidade pós-hoc RULE-CAU, colisão de relações, governança de escrita), **sem elevar o profile em silêncio** — mesma reconciliação da SPEC-004 (CRITICAL, pin D0–D7, homologada "D0–D7 + D8 adversarial") [FONTE: ROADMAP §6; AGENTS.md §4; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 3 — MEMÓRIA SEMÂNTICA E RAG; próxima na sequência após SPEC-005 (BASELINE v1.0, DHR-SPEC005-002). Opera **sobre** conhecimento já validado/publicado; a formação/retrieval é SPEC-007 (não absorvida) [FONTE: ROADMAP §6/§21] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3 teto spec-first; gate normativo E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01 (Classe por BASpec); RULE-PD-01/CC-12 **(N/A — infraestrutura de memória, agnóstica de escola)**; RULE-ECC-04 (verbatim); RULE-ECC-06 (repositórios); RULE-ECC-05 **(N/A — não toca comportamento de trading)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — **D** (ontologia/catálogo de entidades-relações, temporalidade, versionamento, consulta estruturada, Cognitive Trace Reconstruction) + **C** (governança de escrita, imutabilidade/append-only INV-07, proveniência obrigatória, confiança≠Convicção INV-04, fronteira "só conhecimento publicado") + **H** (juízo de similaridade/causalidade com gate de saída e mecanismo declarado — RULE-CAU); declaração normativa é **por BASpec** (SES-001 §50) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-17 (rodada 6; Plan devolvido ao Especificador por ordem de Andraus, chat 2026-10-17, após parecer NÃO CONFORME da rodada 5 — `parecer-revisor-rodada5.md`) — rodada 5: 2026-10-17; v1.0..v1.3: 2026-10-11/12 |
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
| 1.4 | 2026-10-17 | **Rodada 5 (retomada por ordem de Andraus, chat 2026-10-17; 4 defeitos conferidos pelo Orquestrador + 8 reportados por revisões anteriores, cada um reconferido no repositório).** **(V1)** D6 passo 5 alinhado à proveniência CONDICIONAL de CKG-005 (`computed_by` sempre; `gate_record` sse gate; `lineage` sse derivado; `[]` legítimo) + **T16** (teste de sequência D6 para PRIMARY sem gate e sem ancestral). **(V2)** Caminho (a) CANÔNICO de CKG-010 retirado do PRECOND do EC-CKG-001: enquanto o critério de admissão estiver pendente de Andraus, (a) é **fail-closed — não admite** (`PATH_A_ADMISSION_PENDING`); frase de cobertura do §7-bis corrigida (a admissão positiva por (a) é INDETERMINADO, não verificável); convenção de teste (gate em isolamento × persistência condicional) declarada em D7; **ADV-CKG-21**. **(V3)** **Envelope único append-only** (`kg_record`) para TODO tipo de registro (creation/invalidation/archival/canonical_state_transition/collision) com `record_id`/`version`/`supersedes`/`target_record_ref`/`schema_version`/proveniência/`writer_id`/`recorded_at`/validade; eliminados o `collision_record` avulso e o `record_kind=collision` dentro de `relation_record` (um só formato de colisão) + **T17** (reconstrução/auditoria) + **ADV-CKG-19**. **(V4)** BOUNDED LOOP da CKG-008 = **uma passada por submissão**, sem retry automático; ao esgotar ⇒ INDETERMINADO, nada escrito; fonte atomic-spec §10.6 l.315 + RULE-INQ-03 (RULES l.678) + precedente SPEC-002 l.370-371/SPEC-003 l.387-388; versionado com RULE-CKG-008 (alteração só por emenda spec-time) — refletido em RULE/BASpec/D4/EC-CKG-005 + **ADV-CKG-20**. **(R1)** `PENDING_ANCESTOR` incluído na máquina de estados D5 (transitório, limitado ao lote de admissão) e na sequência D6 + **T19**. **(R2)** enum de `canonical_status` corrigido por baseline: `REFUTED` é só do CHM-001; CEM-001 = ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED (l.258-262); CCM-001 = COMPUTED/GATED_PASS/GATED_BLOCK/SUPERSEDED (l.58). **(R3)** `school` declarado campo LOCAL [PROPOSTA] **derivado** de `producer_id` canônico (CHM-001 §2.9 l.361; CEM-001 l.276-278) — não é campo canônico; enum = 5 camadas da hierarquia (inclui **Fractal**, ausente na v1.3); regra espelho RULE-HH-002 (PRIMARY ⇒ Elliott); mapeamento produtor→Fractal = [DECISÃO NECESSÁRIA]; `school` ≠ `Domain` (CC-10). **(R4)** COL-EXP-01..05 (CONFLICT-MAP l.143-147) ganham tabela de tratamento; reconciliação COL-EXP-05 permanece adiada ([DECISÃO NECESSÁRIA]). **(R5)** SIMILAR_A ganha gate de saída determinístico (`similarity_basis` presente ∧ mesmo node_type ∧ from≠to; duplicata simétrica = no-op) + **T18** + **ADV-CKG-22**. **(R6)** EC-CKG-004 elevado a **E3** (guard sobre a escrita permanente — piso atomic-spec l.238). **(R7)** nó ganha `valid_from`/`valid_to` e todo registro ganha `target_record_ref` (via envelope). **(R8)** limiar de falso-DENY mantido como gap aberto (atomic-spec l.273/l.393); declarado só o MÉTODO amostral, sem valor. Extra: linhas de RULES.md corrigidas (RULE-BB-004 l.324; RULE-ONT-01 l.672; RULE-CAU-01/02/03 l.681-683); caminho de entrada de nós de referência (asset/timeframe/regime/observation/calibration_metric) declarado lacuna [DECISÃO NECESSÁRIA]. **Permanecem [DECISÃO NECESSÁRIA]:** critério/produtor/gatilho do caminho (a); caminho de nós de referência; selo SPEC-007; mapeamento produtor→Fractal; consumidor de eventos; emissão pelo KG; allowlist/host do juízo; migração de ontologia; escala de confiança; limiar de falso-DENY; reconciliação COL-EXP-05; H-001, J-001, N-001, M-001, G-001, K-001, C-001, WF-D03, ECC-03-001 (todas ABERTAS). Contagem: 13 BASpecs; 6 EC; 13 EARS; **19 cenários** (T01..T19); **22 adversariais** (ADV-CKG-01..22); 2 invariantes locais (INV-CKG-01/02). |
| 1.5 | 2026-10-17 | **Rodada 6 (parecer NÃO CONFORME da rodada 5 — `parecer-revisor-rodada5.md`; Plan devolvido por Andraus, chat 2026-10-17).** **(C1)** "preservar TODAS as versões" (CEM-001 l.612; l.594-595; l.450): mecanismo `canonical_predecessor_ref` (espelha `previous_version_id` — CHM-001 l.283/588; CCM-001 l.58) + `successor_ref` obrigatório quando `status_to=SUPERSEDED` (gate `VERSION_LINK_MISSING`); T17 (fixture H@1→H@2) + ADV-19(d); Bloco B: evidência PARCIAL/[DECISÃO NECESSÁRIA] (admissão por (a) pendente). **(C2)** CEE-001 l.111: evidência PARCIAL/[DECISÃO NECESSÁRIA] (`calibration_metric` sem caminho de entrada); ADV-05 reescrito (só o isolamento é verificável). **(M1)** caminho (b) e allowlist tratados como (a): contrato do selo pendente ⇒ DENY `SEAL_CONTRACT_UNDEFINED`; mantenedor da allowlist pendente ⇒ DENY `WRITER_ALLOWLIST_UNDEFINED`; "verificável" restrito a predicados. **(M2)** tabela única de caminhos de entrada §D2.3 (nós, relações espelhadas, relações de produtor — SAS-001 l.924 — = caminho (c) [DECISÃO NECESSÁRIA]); convenção de teste (iv) para o detector de colisão (T11/ADV-02/ADV-18 por fixture). **(M3)** EARS 14/15 + **T20** (`ENTRY_PATH_UNDEFINED`, `SCHOOL_UNDERIVABLE`, `WRITER_ALLOWLIST_UNDEFINED`); só Elliott tem `producer_id` conhecido (SPEC-001 l.203) ⇒ SMC/Fibonacci/ICT/Fractal hoje `SCHOOL_UNDERIVABLE`. **(M4)** linha INVALIDA×relação-alvo removida da §D2.2 (INVALIDA ≠ registro `invalidation`); ADV-18(d). **(M5)** gate de CKG-008 = TODA relação CAUSA/SIMILAR_A, qualquer produtor; bounded loop só quando há juízo. **(M6)** memoização removida; limite = 1 invocação por submissão, KG não gera retry; ADV-20 reescrito. **(M7)** conceito "lote"/`PENDING_ANCESTOR` eliminado: ancestral ausente ⇒ REJECTED imediato; T19 por fixture. **(M8)** `envelope_completo` único (D4) referenciado por RULE/schema/EC; `gate_record` = só objeto que RESULTA de gate (upstream ou detector de colisão); decisões dos gates do próprio KG (PASS/DENY/INDETERMINADO) vão ao log `kg_gate_decision` (formato próprio, declarado). **(M9)** guard CKG-007 determinístico por `node_type` (CAUSA `calibration_metric`→`conviction`; nenhum campo de confiança no payload de `conviction`); limite declarado. **(M10)** função de projeção com precedência ARCHIVED > SUPERSEDED > INVALIDATED_IN_TIME > ACTIVE_KNOWLEDGE e `version`/`supersedes` de todos os `record_kind`. **(m1–m7)** âncora CONSTITUTION l.191-192 + INV-06; T01/verificação CKG-001 alinhados; limite de digest declarado; `VALIDITY_WINDOW_INVALID`; limite de gates de presença; legalidade de transição CHM/CEM (`CANONICAL_TRANSITION_ILLEGAL`; CCM sem tabela ⇒ espelha sem validar); cobertura CKG-010→T09/ADV-21. **(m8)** consolidação (listas finais fundidas na tabela de etiquetagem; caminhos numa tabela única). **(G)** gatilho `spec:SPEC-006 em redação` de BL-003/BL-011 tratado pela decisão de Andraus comunicada pelo Orquestrador (ata DHR-BACKLOG-001) — RMR-001 não reaberto. **Permanecem [DECISÃO NECESSÁRIA]:** critério/produtor/gatilho de (a); contrato do selo (b); contrato do caminho (c); caminho de nós de referência e de structure/narrative/mission; mantenedor da allowlist; host do juízo; mapeamento `producer_id`→`school` (SMC/Fibonacci/ICT/Fractal); consumidor de eventos; emissão pelo KG; migração de ontologia; escala de confiança; limiar de falso-DENY; COL-EXP-05; H-001, J-001, N-001, M-001, G-001, K-001, C-001, WF-D03, ECC-03-001 (ABERTAS). Contagem: 13 BASpecs; 6 EC; **15 EARS**; **20 cenários** (T01..T20); 22 adversariais (ADV-CKG-01..22); 2 invariantes locais. |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; DHR-SPEC006-001 §3/§4; DHR-SPEC006-PEND-001; ABERTURA §8/§9; RMR-001 l.128 (linha do BL-029) / l.192 (DHR-SPEC006-PEND-001)]

- **Nenhum item do RMR-001 tem gatilho `spec:SPEC-006` homologado isoladamente.** O início da redação deste Plan **satisfaz ramos de gatilho** de itens pré-existentes (BL-003, BL-011). **Tratamento (v1.5 — G):** a promoção de BL-003/BL-011 a `ATIVADO` pelo gatilho `spec:SPEC-006 em redação` foi **decidida por Andraus** e registrada pelo Orquestrador na ata **DHR-BACKLOG-001** (comunicada nesta rodada; a ata não consta deste checkout — conferência é do Orquestrador/Revisor). O Especificador **não** reabre nem edita o RMR-001 (CONS-01); o encaminhamento abaixo é o desta Spec.
- **BL-003** (persistência física de hipótese/estado) — gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação`. **Encaminhamento:** a parte **física** do BL-003 **É** H-001 (ABERTA) / G-001 (ABERTA) → a SPEC-006 **referencia**, **não absorve** (CONS-01).
- **BL-011** (MC-EXP-001, Master Contract da Camada de Experiência e Memória) — gatilho inclui `spec:SPEC-006 em redação`. **Fonte de requisitos** de SPEC-004/006/009/018. **Encaminhamento:** usar como **insumo de requisitos** (ref. externa K-MAN-15) sob os tratamentos COL-EXP-01..05 já classificados (CONFLICT-MAP l.143-147; detalhe em `governance/CLASSIFICACAO-COLISOES-BL010-011-012.md` l.53-62; prevalece SOT canônico; imutabilidade REFORÇA RULE-BB-004/INV-07). Classificação ≠ aplicação; **não promovo**. Aplicação a esta Spec — ver tabela abaixo (v1.4, R4).

| Colisão (CONFLICT-MAP) | Decisão classificada | Tratamento nesta Spec |
|---|---|---|
| COL-EXP-01 (l.143) — status "BASELINE" do MC-EXP-001 | REJEITAR efeito → PROPOSTA | Nenhum texto do MC-EXP-001 é tratado como baseline; esta Spec não cita status externo como norma (INV-09). |
| COL-EXP-02 (l.144) — Quality Gates G0–G8 | REJEITAR global → gate LOCAL | Nenhum rótulo G-xx usado; maturidade = L1–L4 / L3 (RULE-MM). |
| COL-EXP-03 (l.145) — I-EXP-01..12 / EXP-P01..P14 | ADAPTAR como LOCAIS ancorados nos canônicos | Não importados como IDs. Equivalências usadas só via âncora SOT: imutabilidade → RULE-BB-004/INV-07 (CKG-006); pós-hoc → RULE-CAU-03 (CKG-008); memória sem autoridade decisional → INV-05 (D1). |
| COL-EXP-04 (l.146) — Working Memory §7.6 | ADIAR/RELOCAR a SPEC-004 | Fronteira já respeitada: memória de trabalho = SPEC-004 (Non-goals D1). |
| COL-EXP-05 (l.147) — EXP-SPEC-021 ↔ RAG-SPEC-018 (duplicação sobre RULE-004) | ADIAR reconciliação à ativação (SPEC-006/009) | **NÃO executada aqui.** O estado do BL-011 é decidido por Andraus (DHR-BACKLOG-001, ver acima); se este Plan é a "ativação" que dispara a reconciliação é decisão de Andraus/gate = **[DECISÃO NECESSÁRIA]**. Esta Spec não redefine RULE-004. Os tratamentos residuais R-04..R-06 de aplicação (CLASSIFICACAO l.62) seguem o mesmo regime (adiados, não absorvidos). |
- **BL-010** (MC-RAG-001) — `Em espera`, gatilho `spec:SPEC-007 em redação` ∨ `milestone:FASE 3 iniciada`. A FASE 3 é iniciada, mas BL-010 é fonte de requisitos da **SPEC-007** (não da 006) → **tangente**; a SPEC-006 respeita a fronteira (recebe conhecimento publicado; formação/retrieval é SPEC-007). **Não promovo** (gate/Andraus decidem o ramo `milestone`).
- **BL-029** (proveniência/"LLM propõe, harness recomputa") — **`Em espera`** (Andraus, chat 2026-10-05, DHR-SPEC006-PEND-001: devolvido a `Em espera`; gatilho `spec:SPEC-014`/`SPEC-018`/`SPEC-045`; o gatilho `spec:SPEC-004` foi CONSUMIDO; camada de proveniência já materializada na SPEC-004 v1.2). **Independente desta Spec** (não dispara em `spec:SPEC-006`) — não absorvido nem promovido aqui. [FONTE: RMR-001 l.128 (linha do BL-029, estado `Em espera`) / l.192 (DHR-SPEC006-PEND-001); a l.191 é a errata do BL-003, não do BL-029] *(Correção v1.1: a v1.0 dizia `ATIVADO` — incorreto.)*
- O passo 11-bis pleno ocorre na homologação do Plan.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o Knowledge Graph é **infraestrutura de memória agnóstica de escola** — **armazena** conhecimento de qualquer camada analítica (inclusive a relação `HERDA`/`HIERARQUIA_DE`) **sem** alterar a hierarquia nem a autoridade de criação de hipótese (Elliott cria a primária; ICT não cria — INV-01/INV-02). O KG representa a hierarquia como relações; não a redefine, não interpreta, não decide. O campo local `school` enumera as **5 camadas** (Elliott/Fibonacci/Fractal/SMC/ICT — v1.4 R3) e é derivado do `producer_id` canônico; regras espelho: `hypothesis.school ≠ ICT` (RULE-HH-004) e PRIMARY ⇒ Elliott (RULE-HH-002). [FONTE: INV-01/INV-02; ROADMAP §6; SPEC-001 l.100/l.108]
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
    do KG); l.699 (KG = mecanismo oficial de Cognitive Trace Reconstruction do ecossistema). O KG ESPECIFICA o
    mecanismo que cumpre essas responsabilidades; a satisfação ponta-a-ponta de "todas as versões/todos os estados"
    é PARCIAL enquanto a admissão por (a) estiver pendente (§7-bis Bloco B); NÃO redefine o CEM (CC-02/INV-10). Proveniência: o campo LOCAL
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
    o KG prevê o node_type `calibration_metric`, ISOLADO do Conviction Vector (INV-04), e não a computa; o CAMINHO DE
    ENTRADA dessa métrica é [DECISÃO NECESSÁRIA] (§D2.3) ⇒ obrigação herdada com evidência PARCIAL (Bloco B)
  - canon/SAS-001 §6.12 (l.923-924) — Integração com Knowledge Graph: o agente atua EXCLUSIVAMENTE como PRODUTOR;
    pode registrar relações fractais/temporais/estruturais/de causalidade estrutural; NÃO pode redefinir ontologias
    nem alterar taxonomias globais. FUNDAMENTA a governança de escrita (CKG-009); herdado como fronteira, não redefinido;
    o contrato pelo qual o produtor registra relações (caminho (c), §D2.3) é [DECISÃO NECESSÁRIA].
    (l.163 EC-COG-003: KG "consultado quando necessário… não é pré-requisito obrigatório")
  - governance/CONSTITUTION.md l.233 (EC-COG-003 — "Knowledge Graph | Memória relacional de padrões"): âncora
    constitucional; conformar-se, não reescrever (INV-09)
  - governance/RULES.md: RULE-BB-004 (append-only; objetos SUPERSEDED, nunca deletados — l.324) — REFORÇADO pelo KG
    como imutabilidade permanente (INV-07); RULE-CAU-01 (afirmação causal DEVE declarar mecanismo — l.681),
    RULE-CAU-02 (regime/condição de validade — l.682), RULE-CAU-03 (explicação pós-hoc marcada como tal — l.683);
    RULE-INQ-03 (critério de encerramento → INDETERMINADO — l.678, fonte do bounded loop da CKG-008) —
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
  - FRONTEIRA de entrada sob UMA governança — tabela única de caminhos (a)/(b)/(c)/sem caminho (§D2.3); todo caminho
    pendente de decisão é FAIL-CLOSED (pendência = precondição não satisfeita)
  - ENVELOPE ÚNICO append-only `kg_record` para todo registro de conhecimento + log `kg_gate_decision` das decisões dos gates (v1.5)
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
| S2 | **Entidades (nós) por referência aos canônicos:** hypothesis (CHM-001), evidence (CEM-001), **observation** (Skill — INV-06), conviction (CCM-001), narrative, mission, learning, asset, timeframe, regime, structure, calibration_metric (CEE-001 l.111). Nós de **construção teórica** (structure/regime/narrative — ex.: order block, liquidez) carregam `ontological_status` ∈ {observational, theoretical} (RULE-ONT-01), distinguindo entidade medida de postulada | CEM-001; CHM-001; CCM-001; CEE-001 l.111; INV-06; RULE-ONT-01 (RULES.md l.672) |
| S3 | **Relações tipadas:** CONFIRMA/REFUTA/DEPENDE_DE/HERDA/PERTENCE_A/INVALIDA/ORIGINA/**DERIVA_DE**/SIMILAR_A/CAUSA/HIERARQUIA_DE/ESTATISTICA_DE | ROADMAP §6; research.md §4; CEM-001 Cap.5 (Lineage→DERIVA_DE) |
| S4 | **Temporalidade bitemporal das relações:** `valid_from`/`valid_to` (validade) + `recorded_at` (registro); invalidar por novo registro ≠ deletar | research.md §3.1; INV-07; SPEC-004 INV-CBP-01 |
| S5 | **Proveniência obrigatória** (campo local `provenance_ref.lineage` [PROPOSTA] → `Lineage` CEM-001 / `derived_from[]` SPEC-004; `gate_record` SPEC-004); rejeita escrita sem proveniência | CEM-001 Cap.5 (campo `Lineage`); SPEC-004 v1.2; research.md §3.2 |
| S6 | **Imutabilidade / append-only permanente:** estado = projeção derivada; "esquecimento" = arquivamento versionado | INV-07; RULE-BB-004; SPEC-004 INV-CBP-01; research.md §3.6 |
| S7 | **Confiança de relação** — escala própria, ≠ Convicção; nunca retroalimenta o Conviction Vector | INV-04; research.md §4 |
| S8 | **Relações de similaridade/causalidade** com juízo + gate de saída (mecanismo+regime+pós-hoc — RULE-CAU-01/02/03) | RULE-CAU-01/02/03; research.md §8 |
| S9 | **Governança de escrita (E3) + da ontologia:** quem escreve, identidade autenticada (reusa SPEC-004); produtor não redefine ontologia/taxonomia; ontologia governada spec-time (SPEC-019)/runtime (K-001 [DECISÃO NECESSÁRIA]) | SAS-001 §6.12; SPEC-004 v1.2; SPEC-019; atomic-spec §10.2 |
| S10 | **Fronteira de entrada (uma governança; tabela §D2.3):** (a) objetos canônicos via ciclo de vida; (b) conhecimento formado via selo SPEC-007; (c) relações registradas por produtor (SAS-001 l.924); nós de referência sem caminho — todos [DECISÃO NECESSÁRIA] e fail-closed enquanto pendentes | ROADMAP §6/§7; CEM-001 l.494; research.md §3.4 |
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
              runtime é SEMPRE obrigatório** (RULE-CBP-014); (b) **`gate_record` SÓ quando o OBJETO registrado RESULTA de
              um gate** (gate a montante — SPEC-004 CBP-007 — ou o detector de colisão CKG-013, cujo produto é o registro
              collision); os gates de ADMISSÃO do próprio KG (CKG-001/005/006/008/009/010) NÃO produzem o objeto e NÃO
              geram `gate_record` no registro — suas decisões vão ao log `kg_gate_decision` (D4/D9); (c)
              **`provenance_ref.lineage`/`derived_from` SÓ quando DERIVADO** (não-vazio). `lineage=[]` sem `gate_record` é
              legítimo para PRIMARY e nós sem ancestral (NÃO fabricar — RULE-MET-01). Escrita sem a proveniência EXIGÍVEL é
              REJEITADA (fail-closed). `provenance_ref.lineage` [PROPOSTA] referencia `Lineage` (CEM-001 Cap.5)/`derived_from[]`
              (SPEC-004) — não há `lineage_ref` no CEM-001; NÃO redefine os contratos (CC-02).
              [Fonte: CEM-001 Cap.5; SPEC-004 v1.2 (gate_record); research.md §3.2]  [PROPOSTA]

RULE-CKG-006: O KG é APPEND-ONLY PERMANENTE (INV-07; reforça RULE-BB-004; espelha SPEC-004 INV-CBP-01): nenhum registro
              é DELETADO nem MUTADO. "Esquecimento"/consolidação = ARQUIVAMENTO/rebaixamento VERSIONADO (novo registro de
              transição — RULE-CKG-012), nunca remoção. O estado corrente é PROJEÇÃO DERIVADA do conjunto de registros;
              toda transição é reconstruível (P13). **TODO registro** — creation, invalidation, archival,
              canonical_state_transition e collision — usa o MESMO ENVELOPE append-only `kg_record`, cujos campos
              obrigatórios são definidos UMA vez pelo predicado `envelope_completo` (D4); registro que não o satisfaz é
              REJEITADO (`RECORD_ENVELOPE_INCOMPLETE`; janela inválida ⇒ `VALIDITY_WINDOW_INVALID`). **Limite declarado
              (m3):** o envelope não carrega digest/hash encadeado — a DETECÇÃO de mutação in-place abaixo da camada lógica
              depende do mecanismo físico (H-001) e fica para BUILD; esta RULE proíbe a mutação, não a detecta fisicamente.
              [Fonte: INV-07; RULE-BB-004 (RULES.md l.324); SPEC-004 INV-CBP-01; research.md §3.6]  [PROPOSTA]

RULE-CKG-007: A CONFIANÇA de uma relação é escala PRÓPRIA do KG, em NAMESPACE próprio, e NÃO É a Convicção (Conviction
              Vector 8D — CCM-001). **Guard determinístico (v1.5 — M9), por campos do schema:** (i) `relation_confidence`
              só existe no payload de RELAÇÃO; o payload de nó `conviction` NÃO admite campo de confiança
              (`CONFIDENCE_IS_NOT_CONVICTION`); (ii) relação com `from_node.node_type = calibration_metric` e
              `to_node.node_type = conviction` é PROIBIDA (matriz §D2.1; `ONTOLOGY_INTEGRITY_VIOLATION`). **Limite
              declarado:** semântica de custo/confiança embutida em texto livre de outros node_types NÃO é detectável por
              este guard (ENF-03 — o guard verifica tipo/campo, não significado). INV-04 (atomic-spec l.404) proíbe **custo** no Conviction Vector; a proibição de a **confiança** entrar na
              convicção é EXTENSÃO LOCAL [PROPOSTA] desta Spec (não cláusula de INV-04). Que o cálculo de convicção
              (SPEC-003/CCM-001) não a consuma é requisito endereçado à SPEC-003 / [DECISÃO NECESSÁRIA]. Nenhum limiar de
              convicção é fixado; a escala de confiança é PARÂMETRO a calibrar (INDETERMINADO; não toca J-001/N-001).
              [Fonte: INV-04 (custo); CCM-001; RULE-MET-01; research.md §4]  [PROPOSTA]

RULE-CKG-008: Toda relação CAUSA DEVE declarar o MECANISMO (como a origem produz o destino), DIREÇÃO e CONDIÇÕES
              (RULE-CAU-01), o REGIME/condição de validade (RULE-CAU-02) e, se formulada após o resultado, o MARCADOR
              pós-hoc (RULE-CAU-03). Correlação/precedência/padrão histórico NÃO bastam. Relação CAUSA sem esses campos é
              REJEITADA. **Escopo do gate (v1.5 — M5): TODA relação CAUSA ou SIMILAR_A submetida, QUALQUER que seja o
              produtor ou caminho de entrada (agente/(c), formado/(b), juízo do KG)** — o gate de saída determinístico
              verifica a PRESENÇA (não a veracidade — ENF-03) dos campos antes de escrever. SIMILAR_A: `similarity_basis`
              não-vazio ∧ from.node_type == to.node_type ∧ from ≠ to; SIMILAR_A vigente entre o mesmo par em qualquer
              direção ⇒ a nova é no-op. Escore do juízo NÃO é critério de aceite. **Limite declarado (m5):** gate de
              presença aceita qualquer valor não-vazio do tipo exigido; qualidade semântica não é verificada por ele.
              **Quando a proposta vem de JUÍZO (Classe H) — BOUNDED LOOP (v1.5 — M6):** no máximo UMA invocação do juízo
              por submissão; o KG NÃO gera re-tentativa nem nova submissão; gate reprovado ⇒ a submissão ENCERRA em
              INDETERMINADO, nada escrito, decisão no log `kg_gate_decision`. Nova avaliação só por NOVA submissão de um
              produtor autorizado (que é outra submissão, com sua própria invocação — o KG não memoriza resultados). O
              limite é parte desta RULE (emenda spec-time), não parâmetro de runtime. Fonte: atomic-spec §10.6 l.315;
              RULE-INQ-03 (RULES.md l.678); precedente "uma passada … encerra em undetermined" SPEC-002 l.370-371 /
              SPEC-003 l.387-388.
              [Fonte: RULE-CAU-01/02/03 (RULES.md l.681-683); RULE-INQ-03 (l.678); atomic-spec §10.6; research.md §8]  [PROPOSTA]

RULE-CKG-009: A escrita no KG permanente é GOVERNADA e é E3 (commit crítico/irreversível — atomic-spec §10.2 "KG publicado
              → E3 mínimo"), fail-closed: só ESCRITORES AUTORIZADOS escrevem, com identidade AUTENTICADA pelo runtime
              (reusa SPEC-004 CBP-014 — não define auth nova); FALHA do mecanismo de autenticação da SPEC-004 ⇒ o KG
              trata como NÃO-AUTORIZADO (fail-closed). O produtor pode registrar relações mas NÃO pode redefinir a
              ONTOLOGIA nem alterar TAXONOMIAS globais (SAS-001 §6.12). Alteração da ONTOLOGIA é ato de GOVERNANÇA
              (spec-time: análogo a RULE-HG/SPEC-019 — **[INFERÊNCIA]**, a SPEC-019 não cita "ontologia" literalmente;
              runtime: K-001 [DECISÃO NECESSÁRIA]), prospectiva e backward-compatible (nós existentes nunca invalidados
              por mudança de ontologia — INV-07); migração de `schema_version` = [DECISÃO NECESSÁRIA].
              Quem mantém a allowlist de escritores e quem hospeda o juízo de CKG-008 = [DECISÃO NECESSÁRIA]; **enquanto o
              mantenedor da allowlist estiver pendente, a allowlist é INDEFINIDA ⇒ toda escrita DENY `WRITER_ALLOWLIST_UNDEFINED`** (M1).
              [Fonte: SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; SPEC-019 RULE-HG; ENF-03/04]  [PROPOSTA]

RULE-CKG-010: Todo nó/relação entra por UM caminho da tabela §D2.3, sob a MESMA governança (CKG-009): (a) OBJETOS
              CANÔNICOS (hypothesis/evidence/conviction) e suas transições via CICLO DE VIDA canônico — quando admitidos,
              preservando TODOS os estados e TODAS as versões do modelo (hypothesis REFUTED/SUPERSEDED/ARCHIVED — CHM-001
              l.329/769; evidence INVALIDATED/SUPERSEDED/ARCHIVED — CEM-001 l.258-262/494; conviction SUPERSEDED — CCM-001
              l.58); (b) CONHECIMENTO FORMADO (learning; padrões/relações generalizadas) via SELO DE PUBLICAÇÃO da SPEC-007;
              (c) RELAÇÕES registradas por PRODUTOR (SAS-001 l.924). O KG NÃO faz formação/extração/retrieval; formado SEM
              selo é REJEITADO (`SEAL_MISSING`). **Pendência = precondição NÃO satisfeita = DENY (ENF-04), em TODO caminho
              (v1.5 — M1):** critério/produtor/gatilho de (a) pendentes ⇒ `PATH_A_ADMISSION_PENDING`; contrato do selo
              (SPEC-007) pendente ⇒ `SEAL_CONTRACT_UNDEFINED` (a "presença do selo" não é verificável sem contrato);
              contrato de (c) pendente e objeto sem caminho ⇒ `ENTRY_PATH_UNDEFINED`. Nada persistido em nenhum desses DENY.
              [Fonte: ROADMAP §6/§7; CEM-001 l.494; CHM-001 l.329; CCM-001 l.58; SAS-001 l.924; ENF-04; research.md §3.4]  [PROPOSTA]

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
              `valid_from`), nunca mutação/reuso do registro antigo. Nenhuma transição remove registro (INV-07). A
              projeção é a função `estado(v, T)` de D4, com precedência fixa ARCHIVED > SUPERSEDED > INVALIDATED_IN_TIME >
              ACTIVE_KNOWLEDGE (v1.5 — M10). [Fonte: CHM-001; INV-07; SPEC-004 INV-CBP-01; research.md §3.6]  [PROPOSTA]

RULE-CKG-013: Colisão ocorre sse duas relações (i) formam um PAR CONTRADITÓRIO da tabela §D2.2, (ii) têm o MESMO escopo
              (mesmos `from_node` e `to_node`) e (iii) suas janelas de validade se SOBREPÕEM. Nesse caso o KG DETECTA e
              REGISTRA a colisão (registro `record_kind=collision` no envelope único `kg_record`, referenciando ambas por
              `record_id`; ambas preservadas), NUNCA sobrescreve/apaga uma em silêncio. Fora dessas condições NÃO há
              colisão (origens distintas; validades disjuntas; par não listado — ADV-18). A RESOLUÇÃO é de SPEC-007/SPEC-018
              ou governança — o KG só detecta e registra; não decide.
              [Fonte: INV-07; §D2.2; research.md §8; fronteira SPEC-007/SPEC-018]  [PROPOSTA]
```

### D2.1 — Matriz de integridade da ontologia (RULE-CKG-001) [PROPOSTA]

> **Atributo de escola (ADDED — UM campo único: `school`) — origem e enumeração corrigidas na v1.4 (R3):**
> - **Origem:** `school` **NÃO é campo canônico** — o CHM-001 não tem campo de escola; sua proveniência é
>   `producer_type`/`producer_id` (CHM-001 §2.9 l.361); a Evidência tem `Producer ID` (CEM-001 l.276-278). `school` é
>   campo **LOCAL [PROPOSTA]** do KG, **DERIVADO deterministicamente** do `producer_id` canônico por uma tabela de
>   mapeamento [PROPOSTA]: Elliott Specialist → Elliott (ex. `producer_id == "elliott_specialist"`, SPEC-001 l.203);
>   SMC Specialist → SMC; Fibonacci Validator → Fibonacci; ICT Specialist → ICT (nomes: AGENTS.md §3.2; os
>   `producer_id` exatos dos três últimos são fixados nas Specs dos especialistas — não inventados aqui). **Efeito hoje
>   (v1.5 — M3):** só o `producer_id` do Elliott é conhecido (SPEC-001 l.203) ⇒ hypothesis/structure de SMC, Fibonacci,
>   ICT e Fractal caem em `SCHOOL_UNDERIVABLE` até essas Specs fixarem o `producer_id` [DECISÃO NECESSÁRIA] (EARS 15; T20).
> - **Enumeração:** `school` ∈ {Elliott, Fibonacci, Fractal, SMC, ICT} — as **5 camadas da hierarquia** (CC-01/INV-01;
>   a v1.3 omitia Fractal). **Fractal** não tem especialista produtor listado (AGENTS.md §3.2; a camada Fractal é medida
>   pela Fractal Confluence/FCES — CONSTITUTION l.237): o **mapeamento produtor→Fractal = [DECISÃO NECESSÁRIA]**
>   (dependente das Specs dos especialistas). `producer_id` sem mapeamento ⇒ `school` não derivável ⇒ escrita de
>   `hypothesis`/`structure` REJEITADA `SCHOOL_UNDERIVABLE` (fail-closed — a regra INV-02 abaixo exige `school`).
> - **Acepção (CC-10):** `school` (camada analítica da hierarquia) ≠ `Domain` do CEM-001 (STRUCTURAL/INSTITUTIONAL/…,
>   l.290-301, enumeração governada GMC-001) — não substitui nem redefine `Domain`.
> - Para `hypothesis`, `hierarchy_role` ∈ {PRIMARY, SUB} (ref. SPEC-001 `hierarchy_role`, l.87/l.844).
>   *(O termo "origin_agent" da v1.2 foi eliminado — usa-se só `school`.)*
> O KG **espelha**, NÃO decide, a autoridade de criação (CC-01; Elliott cria PRIMARY; ICT não cria — INV-02/RULE-HH-004).
> **Regras de nó (integridade, CKG-001):** (i) `hypothesis.school ≠ ICT` — `hypothesis` com `school=ICT` é PROIBIDA
> (INV-02/RULE-HH-004), fail-closed; (ii) `hierarchy_role=PRIMARY ⇒ school=Elliott` (espelho de RULE-HH-002, SPEC-001
> l.100). (ICT pode aparecer em `structure` de execução, nunca criando hipótese.)
> "**Família estrutural**" é COMPUTADA (não é campo): nós de **mesma `school`** que `PERTENCE_A` o **mesmo par (asset,
> timeframe)** — usada **só** para restringir herança fractal INTRA-escola; a herança sub→pai ENTRE escolas
> (SMC/Fibonacci SUB → Elliott PRIMARY) é NORMAL e NÃO é bloqueada (SPEC-001 RULE-HH-003 l.104, campo `parent_id`;
> CHM-001 `parent_hypothesis_id` l.165/415; CONSTITUTION l.193).

| Relação | Origem (node_type) | Destino (node_type) | Direcional | Simétrica (consulta) |
|---|---|---|---|---|
| CONFIRMA | **evidence** (NÃO observation — INV-06; workspaces distintos Observations×Evidence, CONSTITUTION l.191-192; restrição [PROPOSTA] derivada de INV-06) | hypothesis | sim | não |
| REFUTA | **evidence** (NÃO observation) | hypothesis | sim | não |
| DEPENDE_DE | hypothesis, mission | hypothesis, evidence | sim | não |
| HERDA | hypothesis (`hierarchy_role=SUB`) | hypothesis (**PAI = `hierarchy_role=PRIMARY`** — RULE-HH-003) — via `parent_id`/`parent_hypothesis_id`; **entre escolas é permitido**; "família estrutural" só restringe SUB intra-escola | sim | não |
| PERTENCE_A | hypothesis, evidence, structure, observation | asset, timeframe, regime, mission | sim | não |
| INVALIDA | evidence, learning | evidence, relation (via `target_relation_id`) | sim | não — AFIRMAÇÃO de conhecimento sobre o alvo; NÃO altera a validade do alvo (isso só ocorre por registro `invalidation` autorizado — CKG-004) e NÃO é par de colisão (§D2.2) |
| ORIGINA | structure/hypothesis com `school` ≠ ICT (derivado de `producer_id`) — **nunca ICT** (INV-02/RULE-HH-004) | hypothesis | sim | não |
| DERIVA_DE | evidence (DERIVED) | evidence (ancestral) | sim | não — **aresta de Lineage** (CEM-001 Cap.5); base do trace (CKG-011); obrigatória por ancestral do Lineage (INV-CKG-02) |
| SIMILAR_A | qualquer | mesmo node_type (≠ o próprio nó) | sim (armazenada) | **sim** (consulta trata A~B ⇔ B~A) — exige `similarity_basis` (gate de saída CKG-008, v1.4 R5); duplicata em direção inversa = no-op |
| CAUSA | qualquer node_type (par `calibration_metric`→`conviction` PROIBIDO — guard por node_type, CKG-007) | qualquer | sim | não — exige mechanism+direction+conditions+regime (+posthoc_flag) (CKG-008) |
| HIERARQUIA_DE | structure, timeframe | structure, timeframe | sim | não |
| ESTATISTICA_DE | learning | hypothesis, structure, asset | sim | não |

> **Distinção DERIVA_DE × proveniência:** `DERIVA_DE` é uma RELAÇÃO navegável do grafo (aresta de Lineage entre nós),
> consumida pela Cognitive Trace Reconstruction (ordem de saída = ancestralidade: dos ancestrais primários aos derivados
> — CEM-001 l.567-577). `provenance_ref.lineage` é um CAMPO de proveniência do registro (quem/de onde; referencia o
> campo `Lineage` do CEM-001 / `derived_from[]` da SPEC-004) — não é aresta navegável. São coisas distintas e coexistem.

> **Invariante local [PROPOSTA] — INV-CKG-01 (Memória permanente imutável):** nenhum registro do KG é deletado ou mutado;
> estado = projeção derivada; toda consolidação/"esquecimento" é arquivamento versionado; toda entidade/relação carrega
> proveniência e é reconstruível; **todo registro, inclusive os especiais (canonical_state_transition, collision), usa o
> envelope único `kg_record`** (v1.4 — V3). Reforça — não redefine — RULE-BB-004, INV-07 e SPEC-004 INV-CBP-01, no eixo permanente. [PROPOSTA]

> **Invariante local [PROPOSTA] — INV-CKG-02 (Completude e aciclicidade da linhagem):** admitir um nó `evidence` DERIVED
> EXIGE que o KG materialize uma aresta `DERIVA_DE` para CADA ancestral do seu `Lineage` (CEM-001 l.565) — fail-closed se
> algum ancestral não estiver referenciado/presente (CKG-003/011); o grafo de `DERIVA_DE` é ACÍCLICO; a Cognitive Trace
> Reconstruction ignora o filtro de validade temporal (um ancestral invalidado no tempo permanece na linhagem — CEM-001
> l.602 "invalidação não implica remoção"). Garante a COMPLETUDE exigida por CEM-001 l.612-614, independente de H-001.
> **Ordem de admissão (v1.5 — M7; conceito "lote" e estado `PENDING_ANCESTOR` ELIMINADOS):** o derivado só é admitido se
> TODOS os ancestrais já estão no KG; ancestral ausente ⇒ REJECTED `ANCESTOR_NOT_ADMITTED` imediato (nada persistido, sem
> estado de espera); o produtor re-submete depois. Sem deadlock [INFERÊNCIA]: o `Lineage` lista evidências
> "imediatamente antecedentes" e é imutável após publicação (CEM-001 l.530/560), logo a ordem ancestral→derivado existe. Hoje inalcançável (evidence só entra por
> (a), pendente) — verificado por predicado sobre fixture (T19). [PROPOSTA]

### D2.2 — Tabela de contradição e escopo de colisão (RULE-CKG-013) [PROPOSTA]

> **Colisão** = duas relações formam um PAR CONTRADITÓRIO E têm o **MESMO escopo** E suas **janelas de validade se
> sobrepõem**. Fora disso NÃO há colisão (evita falso-positivo — ADV-18).

**Escopo (todas as condições):** (1) mesmos `from_node` e `to_node` (mesma direção); (2) ambas vigentes com **sobreposição
temporal** (interseção de `[valid_from, valid_to)` não vazia); (3) o par de `relation_type` consta da tabela abaixo.

| Tipo A | Tipo B (contradiz A) | Simétrico? | Observação |
|---|---|---|---|
| CONFIRMA | REFUTA | **sim** (A↔B) | mesma hipótese-alvo afirmada e negada ao mesmo tempo |

> Pares NÃO listados **não** são contradição estrutural (ex.: DEPENDE_DE × SIMILAR_A, HERDA × PERTENCE_A). **Casos que NÃO
> colidem:** (a) `from_node` diferentes; (b) janelas de validade disjuntas; (c) **INVALIDA × relação-alvo** — a linha da
> v1.4 foi REMOVIDA (M4): INVALIDA mira o alvo por `target_relation_id`, não pelo mesmo (from,to), e é afirmação sobre o
> alvo, não contradição dele (ADV-18 d). A **resolução** de colisão é de SPEC-007/SPEC-018 ou governança (CKG-013). A
> tabela é ENXUTA e extensível por governança (RULE-ONT-02).

### D2.3 — Caminhos de entrada (fonte ÚNICA; RULE-CKG-010/009) [PROPOSTA] — v1.5 (M1/M2)

| Objeto submetido | Caminho | Pendência ([DECISÃO NECESSÁRIA]) | DENY hoje |
|---|---|---|---|
| nó hypothesis/evidence/conviction + `canonical_state_transition` | (a) ciclo de vida canônico | critério/produtor/gatilho de (a) | `PATH_A_ADMISSION_PENDING` |
| relações ESPELHADAS de campo canônico: DERIVA_DE (`Lineage`), HERDA (`parent_id`/`parent_hypothesis_id`) | (a) — materializadas na admissão do nó | idem (a) | `PATH_A_ADMISSION_PENDING` |
| nó learning; padrões/relações generalizadas FORMADOS | (b) selo SPEC-007 | contrato do selo (SPEC-007) | `SEAL_MISSING` (sem selo) / `SEAL_CONTRACT_UNDEFINED` |
| relações registradas por PRODUTOR (SAS-001 l.924) e toda relação sem campo canônico de origem (CONFIRMA, REFUTA, DEPENDE_DE, PERTENCE_A, INVALIDA, ORIGINA, SIMILAR_A, CAUSA, HIERARQUIA_DE, ESTATISTICA_DE) fora de (b) | (c) registro por produtor | contrato de (c) | `ENTRY_PATH_UNDEFINED` |
| nós asset/timeframe/regime/observation/calibration_metric/structure/narrative/mission | sem caminho | caminho inteiro | `ENTRY_PATH_UNDEFINED` |
| registros internos (invalidation, archival, collision) | gerados por ato autorizado (CKG-004/009/012) ou pelo detector (CKG-013) sobre sujeito JÁ admitido | — (inalcançáveis enquanto nada é admitido) | — |
| qualquer escrita | allowlist de escritores (CKG-009) | mantenedor da allowlist | `WRITER_ALLOWLIST_UNDEFINED` |

> **Consequência declarada (v1.5 — honestidade de escopo):** hoje o KG **não admite nenhuma escrita**. O que é verificável
> é o PREDICADO de cada gate sobre entradas e fixtures (convenção D7); a admissão positiva fim a fim é **INDETERMINADO**
> até as decisões acima. Nenhum gate é chamado "verificável" quando depende de contrato indefinido (M1).

---

## Critérios de Aceitação (EARS)

1. Quando um nó ou relação é submetido para escrita, o KG DEVE escrevê-lo somente se o tipo pertence à ontologia e satisfaz a matriz de integridade, e DEVE rejeitar (fail-closed) violação de tipo/integridade, sem escrever.
2. Quando um nó corresponde a um objeto canônico, o KG DEVE referenciá-lo por ID+versão e NÃO DEVE redefinir seu contrato/campos/estados; um nó `observation` NÃO DEVE ser rotulado `evidence`.
3. Quando uma relação é escrita, o KG DEVE exigir tipo, direção e proveniência, e NÃO DEVE aceitar relação sem proveniência; a simetria de SIMILAR_A é semântica de consulta, não ausência de direção.
4. Quando a validade de uma relação muda, o KG DEVE gravar um NOVO registro de invalidação/sucessão e manter o histórico, e NÃO DEVE mutar nem deletar o registro existente.
5. Quando qualquer escrita é tentada sem proveniência, o KG DEVE rejeitá-la (fail-closed).
6. Quando um "esquecimento"/consolidação é solicitado, o KG DEVE arquivar/rebaixar por novo registro versionado, e NÃO DEVE remover nem mutar registro histórico; todo registro (inclusive transição canônica e colisão) DEVE usar o envelope único append-only completo, e o KG DEVE rejeitar registro com envelope incompleto.
7. Quando uma confiança de relação é registrada, o KG DEVE mantê-la só no payload de relação, DEVE rejeitar campo de confiança no payload de nó `conviction` e relação `calibration_metric`→`conviction` (guard por node_type; INV-04 custo como base; que o cálculo de convicção não a consuma é requisito à SPEC-003 / [DECISÃO NECESSÁRIA]).
8. Quando qualquer relação CAUSA ou SIMILAR_A é submetida, de qualquer produtor, o KG DEVE exigir, para CAUSA, mechanism+direction+conditions+regime (e marcador pós-hoc quando aplicável) e, para SIMILAR_A, `similarity_basis` com mesmo node_type e from≠to, e DEVE rejeitá-la sem esses campos; quando a proposta vem de juízo, o KG DEVE invocá-lo no máximo uma vez por submissão, NÃO DEVE gerar re-tentativa, e DEVE encerrar a submissão reprovada em INDETERMINADO.
9. Quando uma escrita no KG permanente é tentada, o KG DEVE aceitá-la (E3) apenas de escritor da allowlist com identidade autenticada (falha de auth ⇒ não-autorizado; allowlist indefinida ⇒ rejeitar), e NÃO DEVE permitir que o produtor redefina ontologia/taxonomia.
10. Quando conhecimento formado é submetido sem selo, ou com selo enquanto o contrato do selo estiver pendente, o KG DEVE rejeitá-lo; quando um objeto canônico é submetido pelo caminho (a) enquanto o critério desse caminho estiver pendente de decisão de Andraus, o KG DEVE rejeitá-lo (fail-closed, nada persistido); depois de decidido o critério, o objeto admitido DEVE preservar todos os estados e versões do seu modelo canônico.
11. Quando um consumidor consulta o KG, o KG DEVE responder read-only e reconstruir a cadeia cognitiva COMPLETA, e NÃO DEVE alterar estado na consulta.
12. Quando um nó/relação transita (SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED), o KG DEVE representar a transição por novo registro preservando o histórico (estado = projeção derivada), e NÃO DEVE remover nem mutar a versão anterior.
13. Quando duas relações entre os mesmos nós se contradizem com validade sobreposta, o KG DEVE detectar e registrar a colisão num registro do envelope único `kg_record` preservando ambas, e NÃO DEVE sobrescrever/apagar uma em silêncio.
14. Quando um objeto é submetido por caminho cujo contrato está indefinido (tabela §D2.3), o KG DEVE rejeitá-lo com `ENTRY_PATH_UNDEFINED` (ou o motivo do caminho pendente), sem persistir nada.
15. Quando um nó hypothesis/structure é submetido com `producer_id` sem mapeamento para `school`, o KG DEVE rejeitá-lo com `SCHOOL_UNDERIVABLE`, sem persistir nada.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec com efeito declara **CLASSE/MECANISMO** (§10.6). D = determinístico; C = constitutivo (é o gate); H =
> híbrido (juízo + gate de saída + bounded loop). **A escrita no KG permanente é E3** (commit crítico/irreversível —
> atomic-spec §10.2); consulta é E1; o guard de isolamento confiança×convicção é **E3** (v1.4 — R6: o guard decide
> admitir/recusar uma escrita no KG permanente, logo herda o piso "KG publicado → E3 mínimo", atomic-spec l.238).

### BASpec-CKG-001 — Ontologia enxuta + matriz de integridade (rejeita violação)
```
BASpec-CKG-001:
  QUANDO:       Um nó ou relação é submetido para escrita no KG
  ENTÃO:        O KG escreve somente se o tipo ∈ ontologia E a matriz de integridade (§D2.1) é satisfeita (origem/destino
                admitidos, direcionalidade/simetria; **regras de nó: `hypothesis.school ≠ ICT`** — INV-02/RULE-HH-004;
                **`hierarchy_role=PRIMARY ⇒ school=Elliott`** — RULE-HH-002; `school` derivável de `producer_id` (senão
                `SCHOOL_UNDERIVABLE`); **HERDA só liga SUB a PAI `hierarchy_role=PRIMARY`**); violação é rejeitada (fail-closed), não escrita. O KG
                apenas ESPELHA os vínculos já criados pelos agentes (ex.: HERDA sub→pai por `parent_id`, inclusive entre
                escolas); NÃO decide a autoridade de criação de hipótese (CC-01)
  PORQUE:       Sem gramática enxuta + integridade, a memória permanente acumula conhecimento incoerente (research.md §8 R-8)
  REFERÊNCIA:   RULE-CKG-001; KERNEL-V2 l.1488-1507; CONSTITUTION l.193; INV-02; RULE-HH-003/004 (SPEC-001)
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico (tipo ∈ catálogo ∧ par origem/destino ∈ matriz ∧ direção/simetria ∧ school derivável ∧ hypothesis.school≠ICT ∧ (PRIMARY ⇒ school=Elliott) ∧ HERDA.pai.hierarchy_role=PRIMARY)
    GATE DE SAÍDA: verificação da matriz §D2.1 + regras de nó (school/hierarchy_role)
    CRITÉRIO 4Es: Conformidade > Eficácia — coerência da ontologia é inviolável
  VERIFICADO POR:
    DADO        (= T01) uma relação ORIGINA cuja origem tem `school == ICT` (fixture; INV-02/RULE-HH-004)
    QUANDO      o gate de integridade roda (predicado — convenção D7 (i))
    ENTÃO       escrita rejeitada; nada persistido. (Regra de nó `hypothesis.school ≠ ICT`: ADV-17; contraste POSITIVO
                HERDA SMC-SUB → Elliott-PRIMARY: T15)
    VERIFICAÇÃO written == false; rejected_reason == "ONTOLOGY_INTEGRITY_VIOLATION"
```

### BASpec-CKG-002 — Entidade por referência ao canônico (não redefine; observation≠evidence)
```
BASpec-CKG-002:
  QUANDO:       Um nó corresponde a um objeto canônico (hypothesis/evidence/conviction) ou é uma observation
  ENTÃO:        O KG referencia o canônico por ID+versão, grava `canonical_status` (snapshot do Status — CEM-001 l.264/428;
                CHM-001; enum POR MODELO, ver schema) e, a cada mudança de Status, um registro `canonical_state_transition`
                no envelope único `kg_record` (payload: estado de/para, timestamp, origem, justificativa — CEM-001 l.428),
                preservando TODOS os estados (CEM-001 l.494); **TODAS as versões (v1.5 — C1):** cada versão canônica é um
                nó próprio (`canonical_ref`=id@version) ligado à anterior por `canonical_predecessor_ref` (espelha
                `previous_version_id` — CHM-001 l.283/588; CCM-001 l.58) e, na transição a SUPERSEDED, à sucessora por
                `successor_ref` (CEM-001 l.450/594-595) — ausente ⇒ `VERSION_LINK_MISSING`; **legalidade (m6):** a
                transição deve constar do grafo canônico (CHM-001 l.744-757; CEM-001 l.460-466) senão
                `CANONICAL_TRANSITION_ILLEGAL`; CCM-001 não tem tabela de transições ⇒ para conviction o KG ESPELHA sem
                validar a transição (só pertencimento ao enum); NÃO redefine contrato/campos; (só para objeto ADMITIDO — (a) pendente, §D2.3);
                um nó observation (Skill — INV-06) NÃO é rotulado evidence. Os estados do KG (D5) são HOMÔNIMOS mas ≠ estados canônicos (CC-10)
  PORQUE:       Redefinir canônico viola CC-02/CONST-01; o Status é o único campo mutável do canônico (CEM-001 l.264), logo o KG
                precisa de snapshot+transições para "preservar todos os estados" (l.494); Observação≠Evidência (INV-06); idioma canônico é do objeto (INV-10)
  REFERÊNCIA:   RULE-CKG-002; CC-02; CC-10; CEM-001 l.264/428/494; INV-06; INV-10
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : referência (canonical_id@version) + snapshot canonical_status + registro canonical_state_transition (legalidade CHM/CEM) + elos de versão; rótulo validado contra INV-06
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
  ENTÃO:        O KG exige a proveniência CONDICIONAL da RULE-CKG-005 (`computed_by`/`writer_id` autenticados SEMPRE;
                `gate_record` sse o objeto RESULTA de gate; `lineage` sse DERIVADO; `[]` legítimo); falta do exigível ⇒
                rejeitada (fail-closed)
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
    ENTÃO       (a) o gate de proveniência APROVA (lineage=[] legítimo, sem gate_record); (b) o gate REPROVA
    VERIFICAÇÃO case_a_provenance_gate == PASS; case_a_lineage_empty_ok == true; case_a_gate_record_required == false;
                case_b_provenance_gate == FAIL; case_b_reason == "COMPUTED_BY_MISSING"   (predicado; = T12/T14; persistência: T16)
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
  ENTÃO:        O KG a mantém só no payload de relação (`relation_confidence`), rejeita campo de confiança no payload de
                nó `conviction` e rejeita relação `calibration_metric`→`conviction` (guard por node_type — RULE-CKG-007;
                limite: semântica em texto livre não é detectada)
  PORQUE:       INV-04 (atomic-spec l.404) proíbe CUSTO no Conviction Vector; esta Spec ESTENDE localmente a mesma
                lógica à confiança de relação (regra LOCAL [PROPOSTA], não cláusula de INV-04) para não contaminar a convicção
  REFERÊNCIA:   RULE-CKG-007; INV-04 (custo); CCM-001
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : guard determinístico por campo/node_type do schema (sem juízo)
    GATE DE SAÍDA: verificação (payload de nó conviction sem campo de confiança ∧ ¬(from.node_type=calibration_metric ∧ to.node_type=conviction))
    CRITÉRIO 4Es: Conformidade > Eficácia — INV-04 (custo) é inviolável; a extensão à confiança é salvaguarda local
  VERIFICADO POR:
    DADO        uma relação CAUSA(calibration_metric → conviction) submetida
    QUANDO      o gate de escrita roda
    ENTÃO       rejeitada (`ONTOLOGY_INTEGRITY_VIOLATION`); idem nó conviction com campo de confiança (`CONFIDENCE_IS_NOT_CONVICTION`)
    VERIFICAÇÃO confidence_exposed_in_conviction_object == false; cost_or_confidence_to_conviction_edge == false
```
> **Nota:** o KG controla só a **sua própria escrita**; que o **cálculo de convicção** (SPEC-003/CCM-001; J-001 ABERTA)
> não consuma a confiança é **requisito endereçado à SPEC-003** ([DECISÃO NECESSÁRIA] na integração). [INFERÊNCIA]

### BASpec-CKG-008 — Relação causal exige mecanismo+regime+pós-hoc (RULE-CAU-01/02/03)
```
BASpec-CKG-008:
  QUANDO:       Qualquer relação CAUSA ou SIMILAR_A é submetida (qualquer produtor/caminho — escopo único, v1.5 M5)
  ENTÃO:        Para CAUSA, o KG exige mechanism+direction+conditions (RULE-CAU-01), regime (RULE-CAU-02) e, se formulada
                após o resultado, marcador pós-hoc (RULE-CAU-03); para SIMILAR_A, `similarity_basis`, mesmo node_type e
                from≠to (duplicata inversa vigente = no-op); faltando, rejeita; o gate verifica só PRESENÇA (ENF-03; m5);
                se a proposta vem de juízo: ≤1 invocação por submissão, sem retry gerado pelo KG; reprovada ⇒ INDETERMINADO
  PORQUE:       Correlação não é causalidade (RULE-CAU-01); a relação causal pode mudar entre regimes (RULE-CAU-02);
                explicação pós-resultado é viés se não marcada (RULE-CAU-03); similaridade sem critério declarado não é
                auditável (P13); investigação sem critério de encerramento é proibida (RULE-INQ-03; atomic-spec l.315)
  REFERÊNCIA:   RULE-CKG-008; RULE-CAU-01/02/03; RULE-INQ-03 (RULES.md l.678); atomic-spec §10.6 l.315
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : juízo (apoio semântico) PROPÕE; gate de saída determinístico verifica presença dos campos CAU-01/02/03 (CAUSA) ou similarity_basis (SIMILAR_A)
    BOUNDED LOOP: (só quando há juízo) ≤1 invocação por submissão; o KG não gera retry nem nova submissão; reprovada ⇒
                  INDETERMINADO, nada escrito, decisão em `kg_gate_decision`; o KG não memoriza resultados (re-submissão =
                  nova submissão). Limite versionado com RULE-CKG-008; fonte: atomic-spec l.315; RULE-INQ-03; SPEC-002 l.370-371
    GATE DE SAÍDA: verificação (CAUSA ⇒ mechanism ∧ direction ∧ conditions ∧ regime presentes; posthoc_flag quando aplicável) ∧ (SIMILAR_A ⇒ similarity_basis ≠ ∅ ∧ from.node_type = to.node_type ∧ from ≠ to)
    CRITÉRIO 4Es: Eficácia (causalidade válida) > Eficiência; LLM é detector, nunca gate (ENF-03)
  VERIFICADO POR:
    DADO        uma relação CAUSA proposta sem mechanism/regime (só correlação)
    QUANDO      o gate de saída roda
    ENTÃO       relação rejeitada (não escrita); o KG não gera re-tentativa; a submissão encerra em INDETERMINADO
    VERIFICAÇÃO causal_written == false; rejected_reason == "CAUSAL_FIELDS_MISSING"; judgment_invocations_per_submission <= 1;
                kg_generated_retries == 0; proposal_outcome == "INDETERMINADO"
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
    GATE DE SAÍDA: verificação (allowlist definida ∧ escritor ∈ allowlist ∧ auth OK ∧ operação ∉ {redefinir ontologia/taxonomia}); auth indisponível ⇒ DENY; allowlist indefinida (mantenedor [DECISÃO NECESSÁRIA]) ⇒ DENY `WRITER_ALLOWLIST_UNDEFINED`
    CRITÉRIO 4Es: Conformidade > Eficácia — escrita permanente só sob autorização é inviolável (ENF-04)
  VERIFICADO POR:
    DADO        uma escrita cuja verificação de identidade da SPEC-004 está indisponível/falha
    QUANDO      o gate E3 roda
    ENTÃO       escrita negada (fail-closed; tratada como não-autorizada); falso-DENY amostrado (ENF-07)
    VERIFICAÇÃO write_allowed == false; fail_closed == true; treated_as_unauthorized == true
```

### BASpec-CKG-010 — Fronteira de entrada (caminhos (a)/(b)/(c) da §D2.3; pendência = DENY)
```
BASpec-CKG-010:
  QUANDO:       Conhecimento é submetido ao KG
  ENTÃO:        O KG aplica a tabela §D2.3: formado sem selo ⇒ `SEAL_MISSING`; formado com selo enquanto o contrato do selo
                estiver pendente ⇒ `SEAL_CONTRACT_UNDEFINED`; canônico por (a) enquanto o critério de (a) estiver pendente ⇒
                `PATH_A_ADMISSION_PENDING`; caminho (c) ou objeto sem caminho ⇒ `ENTRY_PATH_UNDEFINED` — todos fail-closed,
                nada persistido. DEPOIS de decidido (a), admite gravando `canonical_status` + `canonical_state_transition`
                + elos de versão (CKG-002), preservando todos os estados e versões; o KG NÃO faz formação/retrieval
  PORQUE:       "Documento recuperado ≠ conhecimento validado ≠ publicado"; formação é SPEC-007; pendência tratada como
                admissão contaminaria a memória permanente (E3 irreversível); `canonical_ref@version` sozinho não carrega
                Status (CEM-001 l.264)
  REFERÊNCIA:   RULE-CKG-010; §D2.3; ROADMAP §6/§7; CEM-001 l.264/l.494; ENF-04; research.md §3.4
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico por caminho (§D2.3); pendência = precondição não satisfeita ⇒ DENY (ENF-04) — vale para
                  (a), (b) e (c) igualmente (v1.5 — M1)
    GATE DE SAÍDA: os DENY de pendência são verificáveis como predicado; a admissão POSITIVA por qualquer caminho é
                   **INDETERMINADO** até as [DECISÃO NECESSÁRIA] (nenhum caminho é chamado "verificável" sem contrato)
    CRITÉRIO 4Es: Conformidade > Eficácia — não contaminar com não-validado; não perder estado canônico
  VERIFICADO POR:
    DADO        (i) formado SEM selo; (ii) formado COM selo, contrato do selo pendente; (iii) canônico por (a), critério pendente
    QUANDO      o gate de fronteira roda
    ENTÃO       (i)/(ii)/(iii) rejeitados (fail-closed), nada persistido; admissão positiva segue INDETERMINADO (= T09)
    VERIFICAÇÃO reason(i) == "SEAL_MISSING"; reason(ii) == "SEAL_CONTRACT_UNDEFINED"; reason(iii) == "PATH_A_ADMISSION_PENDING";
                written == false (i,ii,iii); positive_admission == "INDETERMINADO"
```

> **[DECISÃO NECESSÁRIA] — caminho (a):** o gate "origem ∈ ciclo de vida" da v1.2 era vacuoso; desde a v1.4 (a) é
> fail-closed. **[PROPOSTA] de critério mínimo (sem decisão de Andraus), POR MODELO:** hypothesis (CHM-001 l.329) — admitir só
> {ACTIVE, DOMINANT, SUPERSEDED, REFUTED, ARCHIVED}, excluir EMERGENT/CANDIDATE (trabalho — SPEC-004); evidence e
> conviction: nenhum critério proposto. **Produtor** de (a) (a SPEC-005 não escreve no KG — SPEC-005 plan l.971) e
> **gatilho** de promoção: [DECISÃO NECESSÁRIA]. Nós de referência: uma direção possível, NÃO adotada, seria "catálogo
> governado" de enumerações existentes (Timeframe Reference CEM-001 l.327-328; Market Context CEM-001 l.333-340/GMC-001).
> **Reatribuição de S14 à SPEC-018/K-001** (critério de promoção trabalho→permanente) = proposta a Andraus, não fato — a
> ABERTURA enviou à SPEC-018 só o ciclo P12 (K-001).

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
  ENTÃO:        O KG DETECTA e grava um registro `record_kind=collision` que satisfaz `envelope_completo` (D4; `gate_record`
                = decisão do detector), referenciando ambas por record_id (preservadas, versionadas, com proveniência e validade); NÃO sobrescreve/apaga uma em silêncio; relações que NÃO satisfazem as 3 condições (origens
                distintas, validades disjuntas, par não listado) NÃO geram colisão; a resolução é de SPEC-007/SPEC-018 ou governança
  PORQUE:       Preservar a contradição auditável respeita INV-07; resolver em silêncio perderia conhecimento e viés de confirmação; escopo evita falso-positivo
  REFERÊNCIA:   RULE-CKG-013; §D2.2; INV-07; fronteira SPEC-007/SPEC-018
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : detecção determinística — par ∈ tabela §D2.2 ∧ mesmos (from,to) ∧ overlap(valid) ⇒ grava registro collision (kg_record); proíbe sobrescrita silenciosa
    GATE DE SAÍDA: verificação (as 3 condições §D2.2 ⇒ registro collision com envelope completo gravado ∧ ambas preservadas; senão sem colisão)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda de conhecimento e auditabilidade da contradição
  VERIFICADO POR:
    DADO        CONFIRMA(A→B) vigente e uma REFUTA(A→B) nova com validade sobreposta (mesmos A,B)
    QUANDO      a escrita roda
    ENTÃO       ambas preservadas; registro collision gravado com envelope completo; nenhuma apagada; resolução não decidida pelo KG
    VERIFICAÇÃO both_relations_present == true; collision_logged == true; collision_envelope_complete == true; silent_overwrite == false
```

---

## D4 — Algoritmo

Mecânicas **determinísticas reais** (D4 — atomic-spec §2). O **mecanismo físico** (grafo real/estrutura em memória/
tabelas+índice) é **INDETERMINADO = H-001 (ABERTA)**; abaixo está a lógica, não a tecnologia:

- **Integridade (CKG-001):** `aceitar sse tipo ∈ catálogo ∧ (origem.node_type, destino.node_type) ∈ matriz[tipo_relação] ∧ direção/simetria conformes (§D2.1)`.
- **Envelope único — DEFINIÇÃO ÚNICA (CKG-006/013; v1.5 — M8; RULE-CKG-006, schema, EC-001/002 e T17 referenciam esta linha):** `envelope_completo(r) = r.record_id ∧ r.record_kind ∧ r.subject_kind ∧ r.subject_id ∧ r.version ∧ (r.supersedes ∨ null declarado) ∧ r.schema_version ∧ r.provenance_ref.computed_by ∧ r.writer_id ∧ r.recorded_at ∧ r.publication.origin ∧ (creation ⇒ r.valid_from) ∧ (invalidation ⇒ r.valid_to) ∧ (kind ∈ {invalidation, archival, canonical_state_transition} ⇒ r.target_record_ref resolve) ∧ (collision ⇒ payload.relation_a_ref ∧ payload.relation_b_ref resolvem) ∧ (objeto resulta de gate ⇒ provenance_ref.gate_record) ∧ (derivado ⇒ provenance_ref.lineage ≠ [])`; senão `RECORD_ENVELOPE_INCOMPLETE`. **Janela (m4):** `invalidation.valid_to < alvo.valid_from ⇒ VALIDITY_WINDOW_INVALID`.
- **Versão/sucessão de TODO `record_kind` (M10):** `subject_id` de invalidation/archival/canonical_state_transition = o do sujeito-alvo; `version` = posição monotônica do registro na sequência do sujeito (qualquer kind; única por sujeito); `supersedes` ≠ null só em `creation` de conteúdo corrigido (→ creation anterior do mesmo sujeito) e em `invalidation` que corrige invalidação anterior (→ essa invalidação); null em archival/canonical_state_transition/collision. Collision: sujeito próprio, `version=1`. Replay: `registros do sujeito ordenados por version` (determinístico; `recorded_at` não desempata).
- **Log de decisões dos gates (`kg_gate_decision`; M8/M6) — formato próprio, FORA do `kg_record`:** `{decision_id, submission_id, gate_id, gate_version, input_digest, result ∈ {PASS, DENY, INDETERMINADO}, reason, writer_id, decided_at}`; append-only; registra toda decisão de admissão (inclusive DENY sem persistência de conhecimento, outcome do bounded loop e tentativas de DELETE/UPDATE bloqueadas); base da amostragem de falso-DENY (ENF-07). O `gate_record` do detector de colisão = `decision_id` do PASS do detector.
- **Validade bitemporal / invalidar por novo registro (CKG-004):** criação grava `R0{creation, valid_from}`; mudança (ato autorizado) grava `R1{invalidation, target_record_ref=R0, valid_to}` — `R0` nunca mutado. Vale para relação e nó. Invalidações efetivas de `v` = as que miram `v` e não foram supersedidas; `valid_to_efetivo(v) = min(valid_to)` delas. **valid-time** `válida_em(v,T) = valid_from(v) ≤ T ∧ (sem invalidação efetiva ∨ T < valid_to_efetivo(v))`; **transaction-time** `conforme_registrado_em(R)` = a mesma função restrita aos registros com `recorded_at ≤ R`.
- **Projeção de estado (CKG-006/012; M10) — por versão de conteúdo `v` (registro creation), no instante T:** `estado(v,T) = ARCHIVED se ∃ archival com target_record_ref=v; senão SUPERSEDED se ∃ creation c' com c'.supersedes=v; senão INVALIDATED_IN_TIME se ¬válida_em(v,T) ∧ T ≥ valid_from(v); senão ACTIVE_KNOWLEDGE`. Precedência fixa ARCHIVED > SUPERSEDED > INVALIDATED_IN_TIME > ACTIVE_KNOWLEDGE (archival é terminal para a versão — análogo a CHM-001 l.767; a reativação é nova versão). `canonical_status(v)` = `status_to` da última `canonical_state_transition` do sujeito por `version` (ou o snapshot de criação) — trilha separada, não afeta `estado`. Mesma entrada de registros ⇒ mesmo estado em qualquer implementação conforme. `DELETE/UPDATE de registro ⇒ negado`.
- **Cognitive Trace Reconstruction (CKG-011):** `trace(x) = fecho transitivo das arestas DERIVA_DE a partir de x` — **completo** (todos os ancestrais; garantido por INV-CKG-02; IGNORA filtro de validade); ordem de saída = ancestralidade (primários→derivados, CEM-001 l.567-577). Completude é obrigação; eficiência de travessia ampla = H-001.
- **Dedupe (CKG-001/003):** `chave de nó = (node_type, canonical_ref)` quando canônico; `= (node_type, natural_key)` quando `canonical_ref=null` (asset/timeframe/regime/narrative/observation/learning — evita colapso); `chave de relação = (relation_type, from_node, to_node, valid_from)`. Reescrita idêntica = no-op; divergente = novo registro (nunca sobrescreve).
- **Gate causal/similaridade (CKG-008; toda CAUSA/SIMILAR_A, qualquer produtor):** `CAUSA ⇒ exige {mechanism, direction, conditions, regime} ≠ ∅ (+ posthoc_flag quando aplicável); senão rejeita CAUSAL_FIELDS_MISSING`. `SIMILAR_A ⇒ exige similarity_basis ≠ ∅ ∧ from.node_type = to.node_type ∧ from ≠ to; senão rejeita SIMILARITY_BASIS_MISSING / ONTOLOGY_INTEGRITY_VIOLATION`; `∃ SIMILAR_A vigente entre {from,to} em qualquer direção ⇒ no-op`. O gate verifica PRESENÇA, não veracidade (ENF-03).
- **Bounded loop do juízo (CKG-008; v1.5 — M6):** `por submissão: invocações(juízo) ≤ 1; se ¬gate_saída ⇒ outcome=INDETERMINADO, nada escrito, kg_gate_decision(INDETERMINADO, motivo)`; o KG nunca emite nova submissão nem re-tentativa; não há cache/memoização de resultados (re-submissão = nova submissão).
- **Confiança de relação (CKG-007; M9):** `relation_confidence` só em `payload.relation.creation` (escala = PARÂMETRO INDETERMINADO); `node_type=conviction ∧ payload contém campo de confiança ⇒ CONFIDENCE_IS_NOT_CONVICTION`; `from.node_type=calibration_metric ∧ to.node_type=conviction ⇒ ONTOLOGY_INTEGRITY_VIOLATION`.
- **Detecção de colisão (CKG-013/§D2.2):** `colide(r1, r2) sse (r1.type, r2.type) ∈ tabela_contradição §D2.2 ∧ r1.from=r2.from ∧ r1.to=r2.to ∧ overlap([r1.valid_from,r1.valid_to), [r2.valid_from,r2.valid_to))`. Se `colide` ⇒ grava registro `record_kind=collision` (envelope único; payload `relation_a_ref`, `relation_b_ref`, `contradiction_pair`, `overlap_window`; `gate_record` = decisão do detector); senão NÃO. (Falso-positivo evitado: origens distintas ou validades disjuntas ⇒ `colide=false`.)
- **Nó hypothesis (CKG-001/§D2.1):** `school = mapa_produtor(producer_id)` (tabela [PROPOSTA]; sem mapeamento ⇒ `REJECTED SCHOOL_UNDERIVABLE`); `aceitar sse ¬(node_type=hypothesis ∧ school=ICT)` (INV-02/RULE-HH-004) `∧ (hierarchy_role=PRIMARY ⇒ school=Elliott)` (RULE-HH-002); `HERDA ⇒ pai.hierarchy_role=PRIMARY` (RULE-HH-003); "família" = `{n : n.school = m.school ∧ n PERTENCE_A mesmo (asset,timeframe) de m}`.
- **Fronteira (CKG-010; §D2.3; v1.5 — M1/M2):** `caminho(obj) = lookup(§D2.3)`; `contrato(caminho) == PENDENTE ⇒ REJECTED motivo(caminho)` (`PATH_A_ADMISSION_PENDING` / `SEAL_CONTRACT_UNDEFINED` / `ENTRY_PATH_UNDEFINED`); `formado ∧ ¬selo ⇒ SEAL_MISSING`; hoje todo caminho retorna DENY.
- **Elos de versão e legalidade canônica (CKG-002; C1/m6):** `canonical_ref.version > 1 ∧ canônico declara previous_version_id ⇒ exige canonical_predecessor_ref`; `status_to = SUPERSEDED ⇒ exige successor_ref`; senão `VERSION_LINK_MISSING`. `canonical_model ∈ {CHM-001, CEM-001} ∧ (status_from, status_to) ∉ grafo canônico ⇒ CANONICAL_TRANSITION_ILLEGAL`; `status_from ≠ canonical_status corrente ⇒ idem`; CCM-001: só `status_to ∈ enum` (sem tabela).
- **Ordem de ancestrais (INV-CKG-02; v1.5 — M7):** `evidence DERIVED d: ∀a ∈ Lineage(d): a ∈ KG ⇒ segue (materializa DERIVA_DE por ancestral); ∃a ∉ KG ⇒ REJECTED ANCESTOR_NOT_ADMITTED` (sem estado de espera).

Nenhuma fórmula computa convicção. Nenhum limiar de convicção nem escala numérica de confiança é fixado (RULE-MET-01).
[FONTE: atomic-spec §2; CEM-001 Cap.5; SPEC-004 INV-CBP-01; research.md §3.1/§4]

---

## D5 — Máquina de estados (lifecycle do nó/relação — estado = projeção derivada)

> **Fronteira (CC-02/CC-10):** este é o lifecycle do **conhecimento no KG permanente**, separado da máquina da **hipótese**
> (CHM-001) e do **estado do objeto no Blackboard** (SPEC-004) — não redefinidos. **O `knowledge_state` NÃO é um campo
> mutado: é PROJEÇÃO DERIVADA do conjunto de registros** (espelha SPEC-004 INV-CBP-01). **Os estados do KG abaixo são
> HOMÔNIMOS mas ≠ estados canônicos** (SUPERSEDED/ARCHIVED do CHM/CEM/CCM; INVALIDATED só do CEM-001; REFUTED só do
> CHM-001 — v1.4 R2): o KG rastreia o Status canônico à parte,
> no snapshot `canonical_status` + registros `canonical_state_transition` (CKG-002/010) — acepção declarada (CC-10).

| Estado (derivado) | Definição (projeção) | Origem |
|---|---|---|
| ACTIVE_KNOWLEDGE | registro de criação vigente, sem sucessora nem invalidação nem arquivamento aplicável (precedência e função exata: D4 `estado(v,T)`) | criação |
| SUPERSEDED | existe sucessora que o referencia por `supersedes` (conteúdo corrigido/substituído) | CKG-012 |
| INVALIDATED_IN_TIME | existe registro de invalidação com `valid_to`, SEM sucessora de conteúdo (o mundo mudou) | CKG-004/012 |
| ARCHIVED | existe registro de arquivamento vigente (rebaixamento de `relevance` sob gate E3 — CKG-009) | CKG-012 |

> **Estados transitórios de admissão (NÃO persistidos):** `CANDIDATE_WRITE` (sob os gates) e `REJECTED` (falhou em gate;
> decisão no log `kg_gate_decision`, nenhum `kg_record`). O `PENDING_ANCESTOR` da v1.4 foi ELIMINADO (M7 — INV-CKG-02).
>
> | Transição de admissão | Condição | Fonte |
> |---|---|---|
> | (submissão) → CANDIDATE_WRITE | entrada recebida | D6 passo 1 |
> | CANDIDATE_WRITE → REJECTED | qualquer gate D6 reprova, inclusive ancestral ausente (`ANCESTOR_NOT_ADMITTED`) | CKG-001/003/005/006/008/009/010; INV-CKG-02 |
> | CANDIDATE_WRITE → ACTIVE_KNOWLEDGE (registro creation persistido) | todos os gates aprovam (hoje inalcançável — §D2.3) | D6 passo 8 |
> **Correção/reativação:** sempre por NOVO registro (nova versão com `supersedes`, ou nova relação com novo `valid_from`),
> nunca reuso/mutação do registro antigo (INV-07). **Autoridade de arquivamento:** gate E3 de governança (CKG-009).
> **Mecanismo físico = INDETERMINADO (H-001 ABERTA)**; Opção B (banco de grafos) **registrada e adiada** (research.md §3.5),
> adotável só se Andraus decidir H-001 como "grafo real". [FONTE: RULE-CKG-006/012; SPEC-004 INV-CBP-01; DHR-SPEC006-001 §3]

---

## D6 — Protocolo de escrita/consulta (sobre conhecimento publicado)

### Produtores, consumidores e fronteira [FONTE: SAS-001 §6.12; CEM-001 l.608-615; SPEC-004/005; ROADMAP §6/§7]
- O conhecimento entra pelos caminhos da **tabela §D2.3** (a)/(b)/(c), sob a mesma governança (CKG-009); todo caminho pendente é fail-closed.
- O **produtor** (agente, SAS-001 §6.12) registra relações pelo caminho (c) (contrato [DECISÃO NECESSÁRIA]) mas **não redefine** ontologia/taxonomia; escrita E3 sob identidade autenticada (SPEC-004); falha de auth ⇒ não-autorizado.
- **[INFERÊNCIA]/[DECISÃO NECESSÁRIA]** — eventual **consumo** de eventos de ciclo de vida pelo KG serve só de **gatilho** para uma avaliação AUTORIZADA (CKG-009), **nunca** invalidação automática/cascata (CEM-001 l.602). O tipo `Evidence.Invalidated` é canônico (CEM-001 l.600/l.722) e a SPEC-005 o **transporta** (SPEC-005 plan l.88/l.859); o que falta é o **consumidor/contrato de consumo pelo KG** = **[DECISÃO NECESSÁRIA]**. **Emissão de eventos pelo KG NÃO é afirmada** (SPEC-005 fonta do log do Blackboard; emissão originada no KG = [DECISÃO NECESSÁRIA]).
- A **consulta** é read-only e **opcional/não-bloqueante** (SAS-001 §6.12/EC-COG-003).

### Sequência de escrita (um nó/relação)
1. **Submissão:** um objeto (nó/relação/transição) chega por um caminho da §D2.3. Toda decisão de gate abaixo é registrada em `kg_gate_decision` (D4).
2. **Fronteira (CKG-010, gate — §D2.3):** contrato do caminho pendente ⇒ `REJECTED` com o motivo do caminho (`PATH_A_ADMISSION_PENDING` / `SEAL_CONTRACT_UNDEFINED` / `ENTRY_PATH_UNDEFINED`); formado sem selo ⇒ `SEAL_MISSING`. **Hoje toda submissão para aqui.**
3. **Autorização E3 (CKG-009, gate):** allowlist definida ∧ escritor ∈ allowlist ∧ identidade autenticada (falha de auth ⇒ não-autorizado; allowlist indefinida ⇒ `WRITER_ALLOWLIST_UNDEFINED`); produtor não redefine ontologia ⇒ senão `REJECTED`.
4. **Ontologia/integridade (CKG-001/007, gate):** tipo ∈ catálogo ∧ matriz §D2.1 ∧ regras de nó (`school` derivável senão `SCHOOL_UNDERIVABLE`; `hypothesis.school ≠ ICT`; PRIMARY ⇒ Elliott) ∧ guard de confiança (CKG-007) ⇒ senão `REJECTED`.
5. **Proveniência CONDICIONAL (CKG-005, gate):** predicado da RULE-CKG-005 ⇒ senão `REJECTED` (`COMPUTED_BY_MISSING` / `GATE_RECORD_MISSING` / `LINEAGE_MISSING`); `lineage=[]` sem `gate_record` é legítimo para PRIMARY e nós sem ancestral.
5-bis. **Linhagem (INV-CKG-02, se evidence DERIVED):** todos os ancestrais no KG ⇒ materializa uma `DERIVA_DE` por ancestral; senão `REJECTED ANCESTOR_NOT_ADMITTED` (sem espera — M7).
5-ter. **Elos de versão/legalidade canônica (CKG-002, se canônico/transição):** D4 ⇒ senão `VERSION_LINK_MISSING` / `CANONICAL_TRANSITION_ILLEGAL`.
6. **Causalidade/similaridade (CKG-008, TODA CAUSA/SIMILAR_A, qualquer produtor):** campos exigidos presentes ⇒ senão `REJECTED`; duplicata simétrica = no-op; se houver juízo, ≤1 invocação e sem retry (INDETERMINADO).
7. **Colisão (CKG-013):** se contradiz relação vigente (§D2.2), grava registro `record_kind=collision` (envelope único; ambas preservadas), não sobrescreve.
8. **Escrita append-only (CKG-006):** novo `kg_record` com `envelope_completo` (D4) e janela válida (senão `RECORD_ENVELOPE_INCOMPLETE` / `VALIDITY_WINDOW_INVALID`); estado derivado `ACTIVE_KNOWLEDGE`; DELETE/UPDATE de registro proibido.
9. **Temporalidade (CKG-004):** relações carregam `valid_from`/`valid_to`/`recorded_at`; a invalidação de uma relação é **ato AUTORIZADO** (novo registro sob CKG-009), **NÃO automática/em cascata** (CEM-001 l.602 "invalidação não implica cascata"; impacto é de CHM/CCM/CDM — CEM-001 l.503/606; CHM-001 l.672-676).
10. **Consumo de evento (SPEC-005) — [INFERÊNCIA]/[DECISÃO NECESSÁRIA]:** o tipo `Evidence.Invalidated` é canônico (CEM-001 l.600/l.722) e a SPEC-005 o **transporta** (plan l.88/l.859); se o KG o consome, isso **não** dispara invalidação automática de relações — serve só de GATILHO para avaliação autorizada (CKG-009). O que a SPEC-005 **não define** é o **consumidor/contrato de consumo pelo KG** = **[DECISÃO NECESSÁRIA]**. Emissão de evento PELO KG = [DECISÃO NECESSÁRIA] (SPEC-005 fonta do log do Blackboard).

> **Nota de fronteira:** memória de **trabalho** e sua ordem/versão = **SPEC-004**; **notificação** = **SPEC-005**;
> **formação** = **SPEC-007**. A SPEC-006 só **preserva, relaciona e consulta** o conhecimento permanente. [FONTE: ROADMAP §5/§6/§7]

---

## D7 — Cenários de Teste

> **Convenção de teste (v1.4 — V2):** (i) cenários de **gate** verificam o PREDICADO do gate como função determinística
> sobre a entrada (independe dos demais gates); (ii) cenários de **consulta/lifecycle/colisão** usam um **fixture** de
> registros já presentes no KG (como foram admitidos não é objeto do teste); (iii) cenários de **persistência** fim a fim
> são **CONDICIONAIS** — hoje o resultado verificável é o DENY da §D2.3; a admissão positiva é INDETERMINADO até as
> decisões de Andraus; (iv) **(v1.5 — M2)** o detector de colisão (passo 7) é avaliado como PREDICADO sobre uma relação
> nova de **fixture** tratada como já aprovada nos passos 1–6, pois CONFIRMA/REFUTA só entram por (c), pendente; idem
> fixtures com `school` mapeado (SMC) enquanto o `producer_id` não é fixado (T15). 20 cenários (T01..T20).

### Cenário-CKG-T01 — Violação de integridade da ontologia → rejeição (caso que a matriz DE FATO rejeita)
```
DADO        uma relação ORIGINA cuja origem tem school=ICT (fixture; ICT nunca origina — INV-02/RULE-HH-004) — viola a matriz §D2.1
QUANDO      o gate de integridade (§D2.1) roda (predicado — convenção (i); = VERIFICADO POR de BASpec-CKG-001)
ENTÃO       escrita rejeitada; nada persistido
VERIFICAÇÃO written == false; rejected_reason == "ONTOLOGY_INTEGRITY_VIOLATION"
```

### Cenário-CKG-T15 — HERDA SMC-SUB → Elliott-PRIMARY (positivo; entre escolas é VÁLIDO)
```
DADO        hipótese SUB de school=SMC (fixture com mapeamento SMC presumido — convenção (iv); sem ele: SCHOOL_UNDERIVABLE, T20)
            com parent_id apontando para hipótese PAI de school=Elliott (hierarchy_role=PRIMARY)
QUANDO      o gate de integridade (CKG-001/§D2.1) avalia a relação HERDA (predicado do gate — convenção (i))
ENTÃO       o gate APROVA (entre escolas é permitido — RULE-HH-003; "família" só restringe SUB intra-escola); a persistência
            depende ainda da fronteira (caminho (a) hoje fail-closed — T16)
VERIFICAÇÃO integrity_gate == PASS; cross_school_herda_allowed == true; parent_hierarchy_role == "PRIMARY"; parent_school == "Elliott"
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

### Cenário-CKG-T06 — Guard CKG-007 por node_type/campo: CAUSA(calibration_metric→conviction) rejeitada
```
DADO        uma relação CAUSA(calibration_metric → conviction) e uma relação com relation_confidence (fixtures; predicado do passo 4)
QUANDO      o guard de CKG-007 roda
ENTÃO       a CAUSA é rejeitada (ONTOLOGY_INTEGRITY_VIOLATION); relation_confidence só existe no payload da relação, nunca no nó conviction
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

### Cenário-CKG-T09 — Fronteira: formado sem selo / com selo sem contrato / canônico por (a) pendente → DENY (fail-closed)
```
DADO        (i) padrão formado SEM selo; (ii) padrão formado COM selo, contrato do selo pendente; (iii) hipótese canônica que
            transita para REFUTED (CHM-001) submetida pelo caminho (a) com o critério de (a) pendente
QUANDO      o gate de fronteira roda
ENTÃO       os três são rejeitados; nada persistido
VERIFICAÇÃO reason(i) == "SEAL_MISSING"; reason(ii) == "SEAL_CONTRACT_UNDEFINED"; reason(iii) == "PATH_A_ADMISSION_PENDING"; written == false
CONDICIONAL (pós-decisões de Andraus — hoje INDETERMINADO): canonical_state_transition_recorded == true;
            canonical_states_preserved == true; version_links_preserved == true (formato verificável hoje em T17, por fixture)
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
DADO        CONFIRMA(A→B) vigente e REFUTA(A→B) nova já aprovada nos passos 1–6, ambas fixture (convenção (iv)), validade sobreposta
QUANDO      o detector de colisão (passo 7) roda como predicado
ENTÃO       ambas preservadas; registro record_kind=collision gravado no envelope único; nenhuma apagada; resolução não decidida pelo KG
VERIFICAÇÃO both_relations_present == true; collision_logged == true; collision_envelope_complete == true; silent_overwrite == false
```

### Cenário-CKG-T12 — Nó PRIMARY sem gate/ancestral passa no gate de proveniência condicional (caminho feliz do gate)
```
DADO        um nó hypothesis PRIMARY (sem gate, Lineage vazio) com computed_by presente (identidade autenticada), sem gate_record e com lineage=[]
QUANDO      o gate de proveniência (CKG-005) avalia a entrada (predicado do gate — convenção (i))
ENTÃO       o gate APROVA (lineage=[] legítimo; gate_record ausente é OK pois não há gate — espelha CBP-007)
VERIFICAÇÃO provenance_gate == PASS; computed_by_present == true; lineage_empty_ok == true; gate_record_required == false
            (persistência ponta-a-ponta: ver T16 — hoje barrada na fronteira do caminho (a), não na proveniência)
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

### Cenário-CKG-T16 — Sequência D6 completa para PRIMARY sem gate e sem ancestral (v1.4 — V1)
```
DADO        um nó hypothesis PRIMARY (school derivado = Elliott; hierarchy_role=PRIMARY), Lineage=[], sem gate_record,
            com computed_by/writer_id autenticados, submetido pelo caminho (a) com o critério de (a) pendente
QUANDO      a sequência D6 roda (passos 1→8) e, em paralelo, cada gate é avaliado como predicado sobre a mesma entrada
ENTÃO       (i) sequência: para no passo 2 com REJECTED PATH_A_ADMISSION_PENDING; nada persistido;
            (ii) predicados: passo 3 (auth, com allowlist de fixture) PASS; passo 4 PASS; **passo 5 (proveniência condicional) PASS**
            — sem exigir gate_record nem lineage não-vazio; nenhum gate posterior ao 2 reprovaria esta entrada por
            proveniência
VERIFICAÇÃO sequence_stop_step == 2; rejected_reason == "PATH_A_ADMISSION_PENDING"; written == false;
            step5_predicate == PASS; step5_required_gate_record == false; step5_required_lineage_nonempty == false
CONDICIONAL (pós-decisão de Andraus sobre (a), se a hipótese satisfizer o critério): sequence_stop_step == null;
            written == true; knowledge_state == "ACTIVE_KNOWLEDGE" — hoje INDETERMINADO
```

### Cenário-CKG-T17 — Reconstrução/auditoria a partir dos registros (envelope único) (v1.4 — V3)
```
DADO        fixture append-only: relação R (creation R0; invalidation R1 com target_record_ref=R0); relação R' (creation R2)
            contraditória com R0 e validade sobreposta; registro collision C1 (payload relation_a_ref=R0, relation_b_ref=R2);
            nó H@1 (canonical_ref=H@1) com canonical_state_transition S1 (ACTIVE→DOMINANT) e S2 (DOMINANT→SUPERSEDED,
            successor_ref=H@2), ambos com target_record_ref à creation de H@1; nó H@2 com canonical_predecessor_ref=H@1 (C1)
QUANDO      um auditor independente reconstrói o histórico SÓ a partir dos registros (replay por sujeito, ordenado por version — D4)
ENTÃO       todo registro (R0,R1,R2,C1,S1,S2,H@2) satisfaz `envelope_completo` (D4); toda referência resolve; a projeção
            `estado(v,T)` dá R INVALIDATED_IN_TIME em "agora" e vigente antes de valid_to; o histórico canônico de H@1 é
            [S1,S2]; a cadeia de versões H@1→H@2 é navegável nos dois sentidos; C1 auditável no mesmo envelope
VERIFICAÇÃO envelope_complete_all == true; orphan_refs == 0; distinct_knowledge_record_formats == 1; projected_state(R) == "INVALIDATED_IN_TIME";
            canonical_history(H@1) == ["ACTIVE→DOMINANT","DOMINANT→SUPERSEDED"]; version_chain(H) == ["H@1","H@2"]; collision_refs_resolve == true
```

### Cenário-CKG-T18 — SIMILAR_A: gate de saída determinístico (v1.4 — R5)
```
DADO        (a) SIMILAR_A(P1→P2) proposta pelo juízo sem similarity_basis; (b) SIMILAR_A(P1→P1); (c) SIMILAR_A(P1→P2) com
            similarity_basis presente e mesmo node_type; (d) SIMILAR_A(P2→P1) com SIMILAR_A(P1→P2) vigente
QUANDO      o gate de saída (CKG-008) roda
ENTÃO       (a) rejeitada SIMILARITY_BASIS_MISSING; (b) rejeitada (from=to); (c) aprovada pelo gate; (d) no-op (simetria)
VERIFICAÇÃO gate(a) == FAIL; reason(a) == "SIMILARITY_BASIS_MISSING"; gate(b) == FAIL; gate(c) == PASS; new_record(d) == false;
            judgment_invocations_per_submission <= 1
```

### Cenário-CKG-T19 — Ordem de ancestrais sem estado de espera (v1.5 — M7)
```
DADO        fixture: A (evidence PRIMARY) presente no KG; evidence C (DERIVED, Lineage=[A]); evidence D (DERIVED, Lineage=[X]),
            X ausente do KG (predicado de INV-CKG-02 — convenção (i); hoje inalcançável fim a fim, (a) pendente)
QUANDO      o passo 5-bis avalia C e D
ENTÃO       C passa, com DERIVA_DE(C→A) materializada no candidato; D é rejeitada imediatamente; não existe estado de espera
VERIFICAÇÃO step5bis(C) == PASS; deriva_de(C→A) == true; step5bis(D) == FAIL; reason(D) == "ANCESTOR_NOT_ADMITTED"; waiting_states == 0
```

### Cenário-CKG-T20 — Caminho indefinido, escola não derivável e allowlist indefinida → DENY (v1.5 — M3/M1)
```
DADO        (a) nó asset submetido; (b) relação CAUSA registrada por produtor (SAS-001 l.924 — caminho (c)); (c) hypothesis
            com producer_id do SMC Specialist (não fixado — só "elliott_specialist" é conhecido, SPEC-001 l.203), avaliada
            no passo 4 como predicado; (d) escrita qualquer avaliada no passo 3 com o mantenedor da allowlist pendente
QUANDO      os gates rodam
ENTÃO       todos rejeitados; nada persistido; decisão registrada em kg_gate_decision
VERIFICAÇÃO reason(a) == "ENTRY_PATH_UNDEFINED"; reason(b) == "ENTRY_PATH_UNDEFINED"; reason(c) == "SCHOOL_UNDERIVABLE";
            reason(d) == "WRITER_ALLOWLIST_UNDEFINED"; written == false (a..d)
```

---

## D8 — Rigor adversarial focado (casos de negação nos pontos de risco)

> Alvo **D0–D7 + D8 adversarial focado** (CRITICAL, pin D0–D7). **22 casos** (v1.4: +ADV-19..22) cobrindo **todas as 13 BASpecs** e as
> fronteiras/decisões abertas. Princípio transversal: **fail-closed**, **nunca deletar/mutar**, **mecanismo físico INDETERMINADO (H-001)**.

### ADV-CKG-01 — Deleção disfarçada de "esquecimento" (CKG-006/INV-07)
**DADO:** "esquecer" traduzido em DELETE físico. **QUANDO:** o gate roda. **ENTÃO:** negar; só arquivamento versionado. **PORQUE:** memória permanente nunca apaga (INV-07). **VERIFICAÇÃO:** physical_delete == false.

### ADV-CKG-02 — Sobrescrita silenciosa de relação contraditória (CKG-013)
**DADO:** REFUTA(A→B) sobre CONFIRMA(A→B) (fixture — D7 convenção (iv)). **QUANDO:** o detector (passo 7) roda. **ENTÃO:** registrar colisão; preservar ambas. **PORQUE:** perder a contradição apaga conhecimento. **VERIFICAÇÃO:** silent_overwrite == false; both_relations_present == true.

### ADV-CKG-03 — Confiança de relação retroalimenta o Conviction Vector (CKG-007/INV-04)
**DADO:** tentativa de expor a confiança no objeto de convicção ou de somá-la como 9ª dimensão. **QUANDO:** a escrita/escopo é definido. **ENTÃO:** rejeitar `CONFIDENCE_IS_NOT_CONVICTION`; namespace próprio. **PORQUE:** INV-04 (custo) como base + extensão local (CKG-007); dimensionalidade=8 (fechada). **VERIFICAÇÃO:** confidence_exposed_in_conviction_object == false.

### ADV-CKG-04 — Relação causal pós-hoc por correlação (CKG-008/RULE-CAU-01/03)
**DADO:** CAUSA(A→B) só por co-ocorrência, formulada após o resultado, sem marcador. **QUANDO:** o gate roda. **ENTÃO:** rejeitar; exigir mechanism+direction+conditions+regime e marcador pós-hoc (RULE-CAU-03). **PORQUE:** correlação não é causalidade (RULE-CAU-01); regime muda a relação (RULE-CAU-02). **VERIFICAÇÃO:** causal_written == false.

### ADV-CKG-05 — Métrica de custo/calibração ligada à convicção (INV-04; CKG-007)
**DADO:** (a) relação CAUSA(`calibration_metric`→`conviction`); (b) nó `conviction` cujo payload traz campo de confiança/custo. **QUANDO:** o gate de integridade (passo 4) roda como predicado. **ENTÃO:** rejeitar (a) `ONTOLOGY_INTEGRITY_VIOLATION` e (b) `CONFIDENCE_IS_NOT_CONVICTION`. O ARMAZENAMENTO da métrica (CEE-001 l.111) NÃO é demonstrado aqui — seu caminho de entrada é `ENTRY_PATH_UNDEFINED` (§D2.3; Bloco B: PARCIAL). **PORQUE:** INV-04. **VERIFICAÇÃO:** cost_or_confidence_to_conviction_edge == false; confidence_field_in_conviction_payload == false.

### ADV-CKG-06 — Escrita sem proveniência aceita (CKG-005)
**DADO:** nó/relação sem provenance_ref (logo sem `computed_by`), ou DERIVADO sem `lineage`, ou resultante de gate sem `gate_record`. **QUANDO:** o gate roda. **ENTÃO:** rejeitar (`COMPUTED_BY_MISSING` / `LINEAGE_MISSING` / `GATE_RECORD_MISSING`) — a condicionalidade de CKG-005 não é brecha para omitir o exigível. **PORQUE:** sem origem não é reconstruível (P13). **VERIFICAÇÃO:** written == false.

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
**DADO:** um nó `hypothesis` com `school == ICT` submetido. **QUANDO:** o gate de integridade de nó roda. **ENTÃO:** rejeitar (fail-closed) `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`; ICT nunca cria hipótese. **PORQUE:** INV-02; RULE-HH-004 (SPEC-001). **VERIFICAÇÃO:** written == false; rejected_reason == "HYPOTHESIS_SCHOOL_ICT_FORBIDDEN".

### ADV-CKG-18 — colisão falsamente detectada / falsamente ignorada (CKG-013; escopo)
**DADO (fixtures — D7 (iv)):** (a) A1 CONFIRMA B e A2 REFUTA B (origens A1≠A2); (b) CONFIRMA(A→B) e REFUTA(A→B) com janelas DISJUNTAS; (c) CONFIRMA(A→B) e REFUTA(A→B) vigentes com sobreposição; (d) INVALIDA(E→R, `target_relation_id`=R) vigente com R vigente. **QUANDO:** o detector (passo 7) roda. **ENTÃO:** só (c) gera registro `record_kind=collision`; (d) não é par da §D2.2 (M4) e não altera a validade de R. **PORQUE:** colisão = par contraditório nos MESMOS (from,to) com sobreposição (CKG-013). **VERIFICAÇÃO:** collision_logged(a)==false; (b)==false; (c)==true; (d)==false; estado(R) inalterado em (d).

### ADV-CKG-19 — Registro especial com envelope incompleto / formato paralelo (CKG-006/013; v1.4 — V3)
**DADO:** (a) registro `collision` sem `record_id`/`computed_by`/`version`; (b) `canonical_state_transition` sem `target_record_ref` ou com referência inexistente; (c) colisão num formato avulso fora do `kg_record`; (d) transição H@1→SUPERSEDED sem `successor_ref` (C1); (e) transição CHM REFUTED→ACTIVE (fora do grafo CHM-001 l.744-757 — m6); (f) invalidation com `valid_to` < `valid_from` do alvo (m4). **QUANDO:** os gates de escrita (passos 5-ter/8) rodam. **ENTÃO:** rejeitar (a)/(b)/(c) `RECORD_ENVELOPE_INCOMPLETE`, (d) `VERSION_LINK_MISSING`, (e) `CANONICAL_TRANSITION_ILLEGAL`, (f) `VALIDITY_WINDOW_INVALID`. **PORQUE:** D9/INV-CKG-01 (P13); CEM-001 l.594-595/612; legalidade canônica. **VERIFICAÇÃO:** written(a..f) == false; distinct_knowledge_record_formats == 1.

### ADV-CKG-20 — Juízo em laço de re-tentativa (CKG-008; v1.4 — V4)
**DADO:** uma submissão de CAUSA proposta por juízo é reprovada no gate de saída; uma implementação tentaria re-invocar o juízo dentro da mesma submissão ou gerar, ela própria, nova submissão. **QUANDO:** o bounded loop é aplicado. **ENTÃO:** o KG invoca o juízo no máximo uma vez nessa submissão, não gera re-tentativa nem submissão, encerra em INDETERMINADO, nada escrito, decisão no `kg_gate_decision`. (Nova submissão de PRODUTOR é outra submissão — controlar sua frequência não é do KG.) **PORQUE:** atomic-spec l.315; RULE-INQ-03. **VERIFICAÇÃO:** judgment_invocations_per_submission <= 1; kg_generated_retries == 0; kg_generated_submissions == 0; proposal_outcome == "INDETERMINADO"; written == false.

### ADV-CKG-21 — Admissão pelo caminho (a) enquanto o critério está pendente (CKG-010/EC-CKG-001; v1.4 — V2)
**DADO:** uma evidência ACTIVE (ou hipótese EMERGENT) submetida pelo caminho (a) "porque veio do ciclo de vida canônico", com o critério de (a) ainda pendente de Andraus. **QUANDO:** o gate de fronteira/EC-CKG-001 roda. **ENTÃO:** negar (fail-closed) `PATH_A_ADMISSION_PENDING`; "origem ∈ ciclo de vida" NÃO satisfaz a precondição; nada persistido. **PORQUE:** precondição pendente = não satisfeita (ENF-04); admitir pelo gate vacuoso da v1.2 contaminaria a memória permanente (E3, irreversível). **VERIFICAÇÃO:** path_a_written == false; rejected_reason == "PATH_A_ADMISSION_PENDING".

### ADV-CKG-22 — SIMILAR_A aceita só pelo escore do juízo (CKG-008; v1.4 — R5)
**DADO:** SIMILAR_A proposta com escore alto do juízo mas sem `similarity_basis`, ou entre node_types distintos. **QUANDO:** o gate de saída roda. **ENTÃO:** rejeitar (`SIMILARITY_BASIS_MISSING` / `ONTOLOGY_INTEGRITY_VIOLATION`); escore NÃO é critério de aceite (escala de confiança INDETERMINADA). **PORQUE:** ENF-03 (detector ≠ gate); RULE-MET-01 (sem limiar fabricado). **VERIFICAÇÃO:** written == false; acceptance_by_score == false.

> **Cobertura:** 22 casos — toda BASpec tem ≥1 negação: CKG-001→ADV-12/17; 002→ADV-11/**19(d,e)**; 003→ADV-12/16; 004→ADV-13/**19(f)**; 005→ADV-06;
> 006→ADV-01/19; 007→ADV-03/05; 008→ADV-04/20/22; 009→ADV-07 + T20(d); 010→**T09/ADV-21 + T20(a,b)** (ADV-08 = fronteira de escopo, não nega o QUANDO — m7); 011→ADV-14/16; 012→ADV-15; 013→ADV-02/18/19. Fronteiras/decisões
> abertas: ADV-09/10. Mapeiam para EC-CKG-001..006 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Cada registro de conhecimento — de nó, de relação e os ESPECIAIS (invalidation, archival, canonical_state_transition,
collision) — DEVE ser reconstruível (P13) e satisfazer `envelope_completo` (D4 — definição única); a colisão tem UM só
formato. As DECISÕES dos gates (PASS/DENY/INDETERMINADO, inclusive do bounded loop e DELETE/UPDATE bloqueados) ficam no
log `kg_gate_decision` (D4) — segundo formato, declarado, com papel distinto (decisão ≠ conhecimento). Auditoria por
replay: T17. A **Cognitive Trace Reconstruction COMPLETA** é capacidade central do
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
| **Envelope único** | TODO registro de conhecimento é um `kg_record`; campos obrigatórios = predicado `envelope_completo` (D4 — fonte única) | idem | CKG-006/013; D9; T17; ADV-19. Decisões de gate: `kg_gate_decision` (D4), fora do envelope |
| Tipo de registro | `record_kind` ∈ {creation, invalidation, archival, canonical_state_transition} | `record_kind` ∈ {creation, invalidation, archival} | colisão = `subject_kind=collision`, `record_kind=collision` (UM só formato; o `collision_record` avulso e o `record_kind=collision` dentro de relação da v1.3 foram eliminados) |
| Identidade | `node_id` (= `subject_id`), `node_type` (∈ ontologia), `version` (monotônico), `schema_version` | `relation_id` (= `subject_id`), `relation_type` (∈ ontologia), `from_node`, `to_node`, `version`, `schema_version` | tipos ∈ catálogo + matriz §D2.1 (CKG-001/003) |
| Alvo do registro | `target_record_ref` (invalidation/archival/canonical_state_transition → record_id ao qual se aplicam; deve resolver) | idem | R7; D4 |
| Chave natural (dedupe) | canônico: `canonical_ref`; **não-canônico** (asset/timeframe/regime/narrative/observation/learning): `natural_key` (ex.: asset="BTC"; timeframe="H4") — evita colapso quando `canonical_ref=null` | `(relation_type, from_node, to_node, valid_from)` | CKG-001/003 |
| Versionamento | `supersedes` (ref à versão anterior ou null) | `supersedes` (ou null) | append-only; estado = projeção derivada (CKG-006/012) |
| Escola/papel | `school` ∈ {Elliott, Fibonacci, Fractal, SMC, ICT} — campo LOCAL [PROPOSTA], DERIVADO de `producer_id` (CHM-001 §2.9; CEM-001 l.276-278), NÃO canônico; `hypothesis.school ≠ ICT`; PRIMARY ⇒ Elliott; mapeamento →Fractal [DECISÃO NECESSÁRIA] + `hierarchy_role` {PRIMARY, SUB} (só hypothesis; ref. SPEC-001) | — | espelha, não decide (CC-01; INV-02/RULE-HH-002/004); `school` ≠ `Domain` CEM-001 (CC-10) |
| Referência canônica | `canonical_ref` = `canonical_id@version`; `canonical_status` (snapshot do Status canônico — enum POR MODELO: CHM-001 l.329 / CEM-001 l.258-262 / CCM-001 l.58) | — | referencia, não redefine (CC-02/CKG-002); estados do KG ≠ estados canônicos (CC-10) |
| Transição canônica / versões | registro `record_kind=canonical_state_transition` com payload { canonical_model, status_from, status_to, `successor_ref` (sse status_to=SUPERSEDED), transition_timestamp, transition_origin, justification } (CEM-001 l.428/450); nó com `canonical_predecessor_ref` (espelha `previous_version_id`) | — | TODOS os estados e versões (CEM-001 l.494/612); legalidade CHM/CEM (CCM espelhado sem validar); só objeto ADMITIDO ((a) pendente) |
| Proveniência (condicional — RULE-CKG-005) | `provenance_ref` = { `computed_by` sempre; `gate_record` sse o objeto RESULTA de gate; `lineage` sse derivado } | idem | CKG-005/CBP-007; nome local [PROPOSTA] |
| Publicação/escrita | `publication.origin` ∈ {`canonical_lifecycle` (a), `spec007_seal` (b), `producer_registration` (c), `kg_internal`}; `writer_id` autenticado | idem | §D2.3; governança E3 (CKG-009/010) |
| Temporalidade | `valid_from`, `valid_to` (null=vigente; fechado por registro `invalidation`), `recorded_at` (v1.4 — R7: o nó passa a ter validade; `created_at` da v1.3 = `recorded_at` do registro creation) | `valid_from`, `valid_to` (null=vigente), `recorded_at` | bitemporal (CKG-004) |
| Relevância/arquivamento | `relevance` (em registro `archival`; rebaixamento sob gate E3 — CKG-012) | idem | lifecycle (CKG-012) |
| Confiança | — | `relation_confidence` (escala PRÓPRIA, namespace do KG — **PARÂMETRO a calibrar**, INDETERMINADO) | ≠ Convicção; namespace próprio (CKG-007/INV-04 custo) |
| Causalidade | — | se `CAUSA`: `mechanism`, `direction`, `conditions`, `regime`, `posthoc_flag` | RULE-CAU-01/02/03 (CKG-008) |
| Similaridade | — | se `SIMILAR_A`: `similarity_basis` (atributos/critério comparados; não-vazio) | gate de saída CKG-008 (v1.4 — R5) |
| Alvo relação (INVALIDA→relation) | — | `target_relation_id` (quando `to_node` é uma relação, não um nó) | matriz §D2.1 (INVALIDA) |
| Colisão | — | — (não é campo de relação) | registro próprio `subject_kind=collision`, `record_kind=collision`, envelope único; payload `relation_a_ref`/`relation_b_ref` (record_id), `contradiction_pair`, `overlap_window`, `detected_at`; `gate_record` = `decision_id` do detector (o registro RESULTA do gate CKG-013) |

> **Estado:** `knowledge_state` NÃO é campo persistido — é **projeção derivada** do conjunto de registros (D5). Estados
> transitórios `CANDIDATE_WRITE`/`REJECTED` pertencem ao fluxo de admissão (rejeição ⇒ só `kg_gate_decision`, nenhum `kg_record`).
> **Validade/arquivamento valem para NÓ e RELAÇÃO** (RULE-CKG-012 "nó/relação"): nós também têm registros `invalidation`/
> `archival` quando aplicável. **`canonical_status`** (snapshot) + registros `canonical_state_transition` são o que sustenta
> `canonical_states_preserved` (CKG-010/T09) — o `canonical_ref@version` sozinho não carrega Status (CEM-001 l.264).

### I/O Schema (lógico — referência; não redefine CHM-001/CEM-001/CCM-001)
```json
{
  "kg_record": {
    "_comentario": "ENVELOPE ÚNICO append-only: TODO registro de conhecimento; obrigatoriedade = predicado envelope_completo (D4); version/supersedes por record_kind = D4 (M10); conteúdo específico em payload; SEM digest (limite m3 — H-001/BUILD)",
    "record_id": "KG-REC-2026-10-17-0001 (único, imutável; referenciável por target_record_ref/relation_a_ref/relation_b_ref)",
    "record_kind": "creation | invalidation | archival | canonical_state_transition | collision",
    "subject_kind": "node | relation | collision",
    "subject_id": "KG-N-... | KG-R-... | KG-C-... (o nó/relação/colisão a que o registro pertence)",
    "version": "posição monotônica do registro na sequência do subject_id (qualquer record_kind; 1, 2, ...)",
    "supersedes": "record_id da creation anterior do MESMO subject (conteúdo corrigido) | record_id da invalidation corrigida | null (archival/canonical_state_transition/collision/1ª creation)",
    "target_record_ref": "null (creation; collision) | record_id ao qual o registro se aplica (invalidation/archival/canonical_state_transition) — DEVE resolver para registro existente",
    "schema_version": "1 (contrato do KG; migração de ontologia/schema = [DECISÃO NECESSÁRIA] — CKG-009)",
    "provenance_ref": { "computed_by": "OBRIGATÓRIO — identidade AUTENTICADA pelo runtime (SPEC-004 RULE-CBP-014)", "gate_record": "CONDICIONAL — sse o OBJETO resulta de gate (gate a montante, SPEC-004 CBP-007; ou decision_id do detector CKG-013 no collision); os gates de admissão do KG NÃO o geram (vão a kg_gate_decision)", "lineage": "CONDICIONAL — obrigatório não-vazio sse DERIVADO (ref. ao campo Lineage do CEM-001 Cap.5 / derived_from[] da SPEC-004; [] legítimo p/ PRIMARY/asset/timeframe/regime/observation; NÃO existe lineage_ref no CEM-001)", "who": "", "when": "", "why": "", "from": "" },
    "writer_id": "(identidade autenticada pelo runtime — SPEC-004; falha de auth ⇒ não-autorizado)",
    "publication": { "origin": "canonical_lifecycle (a) | spec007_seal (b) | producer_registration (c) | kg_internal — §D2.3; (a)/(b)/(c) hoje fail-closed ([DECISÃO NECESSÁRIA])", "seal_ref": "[DECISÃO NECESSÁRIA — contrato do selo = SPEC-007]" },
    "recorded_at": "2026-10-17T12:00:00Z (transaction-time)",
    "valid_from": "obrigatório em creation (nó E relação); null nos demais kinds",
    "valid_to": "obrigatório em invalidation; DEVE ser ≥ valid_from do alvo (senão VALIDITY_WINDOW_INVALID); null nos demais kinds",
    "payload": "um dos payloads abaixo, conforme (subject_kind, record_kind)"
  },
  "payload.node.creation": {
    "node_type": "hypothesis | evidence | observation | conviction | narrative | mission | learning | asset | timeframe | regime | structure | calibration_metric",
    "canonical_ref": "CHM-xxxx@v2 | CEM-xxxx@v1 | CCM-xxxx@v1 | null (referência; NÃO redefine o canônico)",
    "canonical_status": "snapshot do Status canônico, enum POR MODELO (R2): CHM-001 l.329 = EMERGENT|CANDIDATE|ACTIVE|DOMINANT|SUPERSEDED|REFUTED|ARCHIVED; CEM-001 l.258-262 = ACTIVE|SUPERSEDED|INVALIDATED|ARCHIVED (SEM REFUTED); CCM-001 l.58 = COMPUTED|GATED_PASS|GATED_BLOCK|SUPERSEDED; só se canonical_ref != null",
    "canonical_predecessor_ref": "canonical_id@version anterior — espelha previous_version_id (CHM-001 l.283/588; CCM-001 l.58); obrigatório sse o canônico o declara (senão VERSION_LINK_MISSING); null na 1ª versão",
    "_sem_confianca": "payload de node_type=conviction NÃO admite campo de confiança/custo (CONFIDENCE_IS_NOT_CONVICTION — CKG-007)",
    "natural_key": "(identidade de nó NÃO-canônico, p.ex. asset='BTC' | timeframe='H4' — evita colapso quando canonical_ref=null)",
    "school": "Elliott | Fibonacci | Fractal | SMC | ICT — LOCAL [PROPOSTA], DERIVADO de producer_id (CHM-001 §2.9 l.361; CEM-001 l.276-278); só hypothesis/structure; REGRAS: hypothesis.school ≠ ICT (INV-02/RULE-HH-004); hierarchy_role=PRIMARY ⇒ Elliott (RULE-HH-002); mapeamento produtor→Fractal = [DECISÃO NECESSÁRIA]; sem mapeamento ⇒ SCHOOL_UNDERIVABLE",
    "hierarchy_role": "PRIMARY | SUB (só hypothesis; ref. SPEC-001 hierarchy_role; HERDA só liga SUB a pai PRIMARY)",
    "ontological_status": "observational | theoretical (RULE-ONT-01; só structure/regime/narrative)"
  },
  "payload.relation.creation": {
    "relation_type": "CONFIRMA | REFUTA | DEPENDE_DE | HERDA | PERTENCE_A | INVALIDA | ORIGINA | DERIVA_DE | SIMILAR_A | CAUSA | HIERARQUIA_DE | ESTATISTICA_DE",
    "from_node": "KG-N-...-A",
    "to_node": "KG-N-...-B (nó)",
    "target_relation_id": "null | KG-R-...-X (quando o alvo é uma RELAÇÃO — ex.: INVALIDA→relation; matriz §D2.1)",
    "relation_confidence": "escala PRÓPRIA em namespace do KG — PARÂMETRO a calibrar (INDETERMINADO; NÃO é Convicção; nunca exposta ao objeto de convicção; não toca J-001/N-001, que seguem abertas)",
    "causal": "{ mechanism, direction, conditions, regime, posthoc_flag } (obrigatório sse relation_type == CAUSA — RULE-CAU-01/02/03)",
    "similarity_basis": "[atributos/critério comparados] (obrigatório não-vazio sse relation_type == SIMILAR_A — CKG-008, v1.4 R5)"
  },
  "payload.invalidation": { "reason": "(ato AUTORIZADO — CKG-004/009; nunca cascata)" },
  "payload.archival": { "relevance": "(rebaixamento sob gate E3 — CKG-012)", "reason": "" },
  "payload.canonical_state_transition": {
    "canonical_model": "CHM-001 | CEM-001 | CCM-001",
    "canonical_ref": "canonical_id@version",
    "status_from": "valor do enum do canonical_model (ver payload.node.creation.canonical_status)",
    "status_to": "valor do enum do canonical_model — REFUTED só CHM-001; INVALIDATED só CEM-001; (status_from,status_to) ∈ grafo canônico CHM-001 l.744-757 / CEM-001 l.460-466 (senão CANONICAL_TRANSITION_ILLEGAL); CCM-001: só ∈ enum (sem tabela — espelha sem validar)",
    "successor_ref": "canonical_id@version da sucessora — obrigatório sse status_to == SUPERSEDED (CEM-001 l.450/594-595; senão VERSION_LINK_MISSING)",
    "transition_timestamp": "", "transition_origin": "", "justification": "(CEM-001 l.428: timestamp+origem+justificativa)"
  },
  "payload.collision": {
    "relation_a_ref": "record_id do registro creation da relação A (deve resolver)",
    "relation_b_ref": "record_id do registro creation da relação B (deve resolver)",
    "contradiction_pair": "CONFIRMA×REFUTA (§D2.2 — única linha; INVALIDA×alvo removida na v1.5)",
    "overlap_window": "[início, fim) da interseção de validade",
    "detected_at": "", "note": "ambas preservadas; resolução = SPEC-007/SPEC-018 ou governança (CKG-013)"
  },
  "kg_gate_decision": {
    "_comentario": "LOG de decisões dos gates (formato próprio, FORA do kg_record; append-only) — D4",
    "decision_id": "", "submission_id": "", "gate_id": "CKG-001|005|006|008|009|010|013|...", "gate_version": "",
    "input_digest": "", "result": "PASS | DENY | INDETERMINADO", "reason": "ex.: PATH_A_ADMISSION_PENDING", "writer_id": "", "decided_at": ""
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
PRECOND      : (FRONTEIRA — CKG-010/§D2.3: o caminho do objeto tem contrato DEFINIDO e satisfeito; **pendência de (a), do contrato do selo (b), do contrato de (c) ou caminho inexistente NÃO satisfazem esta precondição ⇒ DENY** `PATH_A_ADMISSION_PENDING`/`SEAL_CONTRACT_UNDEFINED`/`ENTRY_PATH_UNDEFINED`; formado sem selo ⇒ `SEAL_MISSING`) AND (governança — EC-CKG-003) AND (ontologia/matriz/regras de nó/`school` derivável — CKG-001/003) AND (canônico referenciado, não redefinido; elos de versão e transição legal — CKG-002) AND (proveniência CONDICIONAL — CKG-005) AND (evidence DERIVED ⇒ ancestrais no KG + DERIVA_DE por ancestral — INV-CKG-02) AND (CAUSA/SIMILAR_A ⇒ campos — CKG-008) AND (`envelope_completo` ∧ janela válida — D4/CKG-006) AND (colisão registrada se houver — CKG-013)
POSTCOND     : novo registro (envelope único) com estado derivado ACTIVE_KNOWLEDGE, proveniência/validade; versão anterior preservada e não-mutada em caso de supersessão
POLICY       : RULE-CKG-001/002/003/005/006/008/010/013; INV-CKG-02; CEM-001 l.608-615; CC-02; ENF-04
LEVEL        : E3 (Crítico — "KG publicado → E3 mínimo", atomic-spec §10.2 l.238; irreversível)
FAILURE-MODE : Fail-closed — qualquer precondição falha OU está pendente de decisão ⇒ REJECTED; nada persistido; `kg_gate_decision`. **Falso-DENY E3: método amostral (abaixo); limiar = gap aberto (atomic-spec l.273/l.393) — CONDICIONAL; nenhum valor inventado.** DENY por pendência (§D2.3, `WRITER_ALLOWLIST_UNDEFINED`) é DENY por desenho, NÃO falso-DENY
EVIDENCE     : `kg_record` que satisfaz `envelope_completo` (D4) + **método de falso-DENY (ENF-07):** todo DENY gera `kg_gate_decision` (gate_id/version, input_digest, reason); uma AMOSTRA é reavaliada por re-execução determinística do gate sobre a entrada registrada + revisão humana; tamanho de amostra e limiar = gap aberto
```

### EC-CKG-002 — Imutabilidade / append-only / versionamento [E3]
```
CAPABILITY   : Impedir deleção/mutação de registro e garantir transições versionadas
EFFECT       : Transição por NOVO registro (SUPERSEDED/ARCHIVED/INVALIDATED_IN_TIME) — nunca remoção nem reescrita
PRECOND      : (operação ∉ {DELETE físico, UPDATE de registro}) AND (TODO registro satisfaz `envelope_completo` e a regra de `version`/`supersedes` por record_kind — D4; senão RECORD_ENVELOPE_INCOMPLETE / VALIDITY_WINDOW_INVALID)
POSTCOND     : histórico preservado e reconstruível por replay (T17); estado = `estado(v,T)` (D4); um só formato de registro de conhecimento; nenhum registro removido/mutado (INV-07; INV-CBP-01)
POLICY       : RULE-CKG-004/006/012; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01; INV-CKG-01
LEVEL        : E3 (Crítico — perda/reescrita de histórico é irreversível; fail-closed)
FAILURE-MODE : Fail-closed — tentativa de DELETE/UPDATE ⇒ negada; log. **Falso-DENY E3 CONDICIONAL até limiar (ENF-07)**
EVIDENCE     : `kg_gate_decision` de cada tentativa de DELETE/UPDATE bloqueada (não é `gate_record` — o KG não produz objeto ao bloquear) + ENF-07 (bloqueio indevido de arquivamento legítimo)
```

### EC-CKG-003 — Governança de escrita (autorizado + autenticado; não redefine ontologia) [E3]
```
CAPABILITY   : Admitir escrita só de escritor autorizado/autenticado, sem redefinição de ontologia pelo produtor
EFFECT       : Autorização (ou recusa) de escrita permanente no KG
PRECOND      : (allowlist DEFINIDA — mantenedor [DECISÃO NECESSÁRIA]; indefinida ⇒ DENY `WRITER_ALLOWLIST_UNDEFINED`) AND (escritor ∈ allowlist ∧ identidade AUTENTICADA pelo runtime — SPEC-004 CBP-014; auth indisponível/falha ⇒ não-autorizado) AND (operação ∉ {redefinir ontologia/taxonomia global} — SAS-001 §6.12) AND (gate determinístico — ENF-03)
POSTCOND     : só escritor autorizado escreve; produtor registra relações, não redefine ontologia (ato de governança)
POLICY       : RULE-CKG-009; SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04
LEVEL        : E3 (Crítico — escrita em memória permanente; cruza fronteira de confiança)
FAILURE-MODE : Fail-closed — escritor não autorizado / falha de auth da SPEC-004 / tentativa de redefinir ontologia ⇒ negada; log. **Falso-DENY E3 CONDICIONAL até limiar (ENF-07)**
EVIDENCE     : `kg_gate_decision` da autorização (identidade autenticada; motivo do DENY) + amostragem de falso-DENY (ENF-07)
```

### EC-CKG-004 — Confiança de relação em namespace próprio do KG (guard local; INV-04 custo como base) [E3]
```
CAPABILITY   : Manter a confiança de relação em namespace próprio do KG e não escrever arestas custo/confiança→conviction
EFFECT       : Guard (na escrita do KG) de que confiança não é exposta ao objeto de convicção nem vira aresta para `conviction`
PRECOND      : (payload de nó conviction sem campo de confiança/custo) AND ¬(from.node_type = calibration_metric ∧ to.node_type = conviction) — guard por campo/node_type (RULE-CKG-007; limite: texto livre não detectado)
POSTCOND     : nenhum campo do nó conviction recebe confiança; nenhuma relação calibration_metric→conviction é escrita
POLICY       : RULE-CKG-007; INV-04 (custo); CCM-001
LEVEL        : **E3** (v1.4 — R6; a v1.3 declarava E2) — o guard decide ADMITIR/RECUSAR uma escrita no KG permanente, logo o
               efeito é "KG publicado" (piso E3 — atomic-spec l.238; economicidade não rebaixa — ENF-02)
FAILURE-MODE : Fail-closed — tentativa de expor confiança no objeto de convicção / aresta custo/confiança→conviction ⇒ negada; log.
               **Falso-DENY E3: mesmo método amostral do EC-CKG-001; limiar = gap aberto (ENF-07) — CONDICIONAL**
EVIDENCE     : verificação (na escrita do KG) de namespace separado e ausência da aresta + amostragem de falso-DENY (ENF-07). A garantia de que o CÁLCULO de
               convicção (SPEC-003/CCM-001) não consome a confiança é requisito endereçado à SPEC-003 / [DECISÃO NECESSÁRIA] — fora do controle do KG
```

### EC-CKG-005 — Registro de relação causal com mecanismo/regime (RULE-CAU) [E3]
```
CAPABILITY   : Admitir relação causal apenas com mechanism+direction+conditions+regime (+posthoc quando aplicável) e relação de similaridade apenas com similarity_basis
EFFECT       : Escrita (ou recusa) de TODA relação CAUSA/SIMILAR_A, qualquer produtor/caminho (escopo único — M5) — persistência permanente (E3)
PRECOND      : (relation_type == CAUSA) ⇒ (mechanism ∧ direction ∧ conditions ∧ regime presentes; posthoc_flag quando aplicável); (relation_type == SIMILAR_A) ⇒ (similarity_basis ≠ ∅ ∧ from.node_type = to.node_type ∧ from ≠ to); gate de saída determinístico; **se há juízo: ≤1 invocação por submissão, sem retry gerado pelo KG**
POSTCOND     : relações causais/de similaridade têm campos auditáveis (presença — limite m5); nenhuma submissão consome mais de uma invocação do juízo
POLICY       : RULE-CKG-008; RULE-CAU-01/02/03; RULE-INQ-03 (RULES.md l.678); atomic-spec §10.6 l.315; ENF-03
LEVEL        : E3 (Crítico — é um write permanente; herda EC-CKG-001)
FAILURE-MODE : Fail-closed — campos ausentes ou gate reprovado ⇒ rejeitada; submissão ENCERRA em INDETERMINADO (nada escrito; `kg_gate_decision`); KG sem retry/sem memoização. Limite versionado com RULE-CKG-008. **Falso-DENY E3 CONDICIONAL até limiar (ENF-07)**
EVIDENCE     : campos causais/similarity_basis por relação; **invocações do juízo por submissão ≤ 1 e retries gerados pelo KG = 0** (em `kg_gate_decision`); outcome INDETERMINADO; presença, não veracidade (ENF-03); amostragem de falso-DENY (método do EC-CKG-001)
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
| Admissão por caminho com contrato vacuoso/pendente — (a), selo (b), (c), allowlist (contaminação irreversível) | fail-closed por caminho (§D2.3; CKG-009/010; EC-CKG-001/003); T09/T20; ADV-CKG-21. **Custo declarado:** até as decisões de Andraus o KG não admite NENHUMA escrita — limitação funcional assumida em favor de Conformidade/Eficácia (4Es) |
| Formatos paralelos de registro / registro especial sem identidade | envelope único `kg_record` (CKG-006/013); EC-CKG-002; T17; ADV-CKG-19 |
| Juízo em laço (custo/latência sem fim) | ≤1 invocação por submissão; KG sem retry (CKG-008; EC-CKG-005); ADV-CKG-20 |
| Mutação in-place abaixo da camada lógica não detectada | limite declarado (RULE-CKG-006, m3): sem digest no envelope; detecção física = H-001/BUILD |

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

- **CKG-001 (ontologia/integridade + regra de nó, C):** se errada → violação da matriz, ou hypothesis.school=ICT, ou PRIMARY com school≠Elliott, ou `school` não derivável aceito, ou HERDA→pai não-PRIMARY persistidos → observável; verificável como predicado. Negação: ADV-CKG-12/17, T01, T20(c) (`SCHOOL_UNDERIVABLE`); POSITIVO cross-escola: T15 (fixture com mapeamento SMC presumido).
- **CKG-002 (ref canônica + versões, D):** se errada → contrato redefinido, observation=evidence, enum trocado entre modelos, versão SUPERSEDED sem elo à sucessora, ou transição ilegal aceita → observável; verificável como predicado (T02, T17 fixture, ADV-11, ADV-19 d/e). QUANDO-sim-mas-ENTÃO-não: transição de conviction fora de qualquer tabela — o KG NÃO deve rejeitar por legalidade (CCM-001 sem tabela; espelha). Ponta-a-ponta: INDETERMINADO ((a) pendente).
- **CKG-003 (relação tipada, D):** se errada → relação sem tipo/direção/proveniência, ou evidence DERIVED aceita com ancestral ausente → observável; verificável como predicado. Negação: ADV-CKG-12/16, T03, **T19** (e caso-feliz T12).
- **CKG-004 (temporalidade, D):** se errada → registro existente mutado/deletado → observável por `existing_record_mutated=true`; verificável. Negação: ADV-CKG-13, T04. QUANDO-sim-mas-ENTÃO-não: consulta "agora" não retorna invalidada (correto).
- **CKG-005 (proveniência condicional, C):** se errada → nó sem `computed_by` aceito, OU gate_record/lineage forçados onde não há gate/ancestral → observável; verificável. Negação: ADV-CKG-06, **T14** (sem computed_by); caso-feliz condicional: T12 (predicado) + **T16** (sequência D6 — v1.4 V1: o passo 5 da v1.3 contradizia esta BASpec; alinhado). QUANDO-sim-mas-ENTÃO-não: PRIMARY sem gate/ancestral — o gate NÃO deve exigir gate_record/lineage (T16 `step5_required_* == false`).
- **CKG-006 (imutabilidade + envelope, C/E3):** se errada → DELETE/UPDATE ocorre, ou registro especial sem identidade/versão/proveniência, ou dois formatos de colisão → observável; verificável. Negação: ADV-CKG-01/**19**, T05, **T17**.
- **CKG-007 (confiança≠convicção, C/E3):** se errada → campo de confiança no nó conviction ou relação calibration_metric→conviction aceitos → observável por campo/node_type; verificável. Limite: semântica em texto livre não detectada (M9). Negação: ADV-CKG-03/05, T06.
- **CKG-008 (causal/similaridade, H):** se errada → CAUSA de QUALQUER produtor sem mecanismo/regime escrita, SIMILAR_A sem base aceita, ou KG re-invocando o juízo/gerando retry → observável (`judgment_invocations_per_submission > 1`, `kg_generated_retries > 0`); verificável. Negação: ADV-CKG-04/20/22, T07, T18. QUANDO-sim-mas-ENTÃO-não: SIMILAR_A duplicada inversa — no-op (T18 d).
- **CKG-009 (governança E3, C):** se errada → auth falha-aberto, allowlist indefinida tratada como aberta, ou produtor redefine ontologia → observável; verificável como predicado. Negação: ADV-CKG-07, T08, T20(d).
- **CKG-010 (fronteira, C):** se errada → objeto admitido por caminho com contrato pendente ((a), selo (b), (c)) ou sem caminho → observável; **verificáveis só os DENY** (predicados — T09, T20, ADV-21); a **admissão POSITIVA por qualquer caminho é INDETERMINADO** ([DECISÃO NECESSÁRIA]). QUANDO-sim-mas-ENTÃO-não: formado COM selo — hoje NÃO deve ser admitido (contrato do selo pendente).
- **CKG-011 (consulta/trace completo, D):** se errada → trace incompleto ou consulta muta → observável por `trace_complete=false`; verificável. Negação: ADV-CKG-14, T10.
- **CKG-012 (lifecycle, D):** se errada → versão anterior removida/mutada → observável; verificável. Negação: ADV-CKG-15, T13.
- **CKG-013 (colisão, C):** se errada → contraditória sobrescrita em silêncio, OU colisão falsa (origens distintas/validades disjuntas), OU colisão gravada fora do envelope → observável; verificável. Negação: ADV-CKG-02/**18**/**19**, T11, T17; escopo em §D2.2.

**Cobertura de verificabilidade (v1.5 — M1):** as 13 BASpecs têm ENTÃO verificável **como PREDICADO de gate ou sobre
fixture** por observador independente, e ≥1 negação em D8. **Nenhuma** tem admissão POSITIVA fim a fim verificável hoje:
todo caminho de entrada está pendente (§D2.3) ⇒ INDETERMINADO até as [DECISÃO NECESSÁRIA]; em CKG-010 só os DENY são
verificáveis (o caminho (b) NÃO é mais chamado "verificável" — seu gate depende do contrato do selo).

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista CEM-001 (l.494/608-615/562-565/699), CHM-001, CCM-001,
CEE-001 l.111, SAS-001 §6.12, SPEC-004 v1.2 (INV-CBP-01; `gate_record`), SPEC-005 v1.0, RULE-BB-004, RULE-CAU-01/02/03,
CONSTITUTION l.233, atomic-spec v1.5, ENF-01..08, INV-04/05/06/07/09/10. Evidência por obrigação herdada:
- CEM-001 "trace COMPLETO" (l.614) → CKG-011 + INV-CKG-02 (trace completo, não rebaixado por H-001; T10 por fixture); não redefine.
- CEM-001 "preservar TODOS os estados" (l.613/l.494) → **evidência PARCIAL:** FORMATO especificado e verificável por fixture (snapshot `canonical_status` por modelo + `canonical_state_transition` com legalidade CHM/CEM — CKG-002; T17; ADV-19 e); admissão por (a) fail-closed ⇒ ponta-a-ponta = **[DECISÃO NECESSÁRIA]** (não enfraquecida nem removida — bloqueada a montante; RULE-HD-03 respeitada).
- CEM-001 "preservar TODAS as versões" (l.612; relação entre versões explícita l.594-595; sucessora referenciada l.450) → **evidência PARCIAL (v1.5 — C1):** mecanismo = cada versão canônica é um nó (`canonical_ref`=id@version) com `canonical_predecessor_ref` (espelha `previous_version_id` — CHM-001 l.283/588; CCM-001 l.58) + `successor_ref` obrigatório na transição a SUPERSEDED (`VERSION_LINK_MISSING`); versões do PRÓPRIO KG: `supersedes` (CKG-012; T13). Teste: T17 (`version_chain(H) == [H@1,H@2]`, fixture) + ADV-19(d). Ponta-a-ponta depende de (a) = **[DECISÃO NECESSÁRIA]**.
- CEM-001 Cap.5 `Lineage` → tipo DERIVA_DE (aresta navegável) + `provenance_ref.lineage` (campo local [PROPOSTA] que referencia `Lineage`/`derived_from[]`), distinguidos.
- CHM-001 (estados/versionamento) → CKG-002/012 por referência; não transiciona.
- CCM-001 → CKG-007/EC-CKG-004 isolam confiança (INV-04).
- SPEC-004 v1.2 INV-CBP-01 (append-only real; registro nunca mutado) → CKG-004/006/012 (novos registros; estado derivado); `gate_record` reatribuído à SPEC-004 (não CEM-001).
- SPEC-005 (eventos) → D6 consome; emissão pelo KG NÃO afirmada ([DECISÃO NECESSÁRIA]).
- SAS-001 §6.12 (produtor não redefine ontologia) → CKG-009/EC-CKG-003.
- RULE-BB-004/INV-07 → CKG-006/012.
- RULE-CAU-01/02/03 → CKG-008 (mechanism+regime+posthoc).
- CEE-001 l.111 ("entra no Knowledge Graph como métrica de calibração") → **evidência PARCIAL (v1.5 — C2):** o node_type `calibration_metric` e seu ISOLAMENTO da convicção são verificáveis (CKG-007; ADV-05; T06); o ARMAZENAMENTO não é demonstrado — o caminho de entrada da métrica é `ENTRY_PATH_UNDEFINED` (§D2.3) = **[DECISÃO NECESSÁRIA]** (não suprimida — bloqueada a montante; RULE-HD-03).
- atomic-spec §10.2 ("KG publicado → E3") → EC-CKG-001/002/003/**004**/005 em E3 (004 elevado na v1.4 — R6).
- atomic-spec §10.6 l.315 (bounded loop com parada explícita) + RULE-INQ-03 → CKG-008 "≤1 invocação por submissão; KG sem retry; encerra INDETERMINADO" (v1.5 — M6).
- SAS-001 §6.12 l.924 (produtor registra relações) → caminho (c) declarado (§D2.3); contrato = **[DECISÃO NECESSÁRIA]** (fail-closed).
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (único MODIFIED = RULE-BB-004 reforçada — RULE-HD-02).
**Eixo VERTICAL (RULE-HV) não aplicável.**

**Bloco C — epistêmico / disciplinas N8–N17 (verificado — achado / sem achado):**
- **RULE-EPI-01..03:** **achados corrigidos (v1.4 e v1.5)** — a v1.3 convertia o INDETERMINADO de (a) em PASS; a v1.4 repetia o padrão no selo (b) e na allowlist (chamados "verificáveis" com contrato indefinido) e afirmava que o KG "ARMAZENA" a métrica CEE e "CUMPRE integralmente" CEM l.608-615; agora todo caminho pendente = DENY, e essas obrigações = PARCIAL explícito. H-001/mecanismo físico = INDETERMINADO (não fato); `school` declarado LOCAL derivado (não mais "por referência ao canônico", que sugeria campo canônico inexistente); nenhuma hipótese tratada como fato.
- **RULE-SEM-01/04:** sem achado — acepções declaradas (CC-10); termos canônicos não redefinidos.
- **RULE-ONT-01/02 (ontológica):** **verificado** — a ontologia do KG (tipos/entidades/matriz §D2.1) é declarada explicitamente, com "família estrutural" definida; nós de **construção teórica** (structure/regime/narrative — order block, liquidez) carregam `ontological_status` ∈ {observational, theoretical} (RULE-ONT-01, RULES.md l.672), distinguindo entidade medida de postulada; nenhum tipo canônico redefinido; alteração de ontologia por governança (RULE-ONT-02/CKG-009). Sem achado residual.
- **RULE-INQ (inquirição):** **verificado** — questões abertas (etiquetagem, abaixo) formuladas como [DECISÃO NECESSÁRIA], não respondidas por suposição; **RULE-INQ-03** aplicada ao juízo da CKG-008 (≤1 invocação → INDETERMINADO); sem achado.
- **RULE-CAU-01/02/03:** sem achado — CKG-008 exige mechanism+direction+conditions (01), regime (02) e marcador pós-hoc (03); gate verifica presença, não veracidade (ENF-03).
- **RULE-CTF (contrafactual):** **verificado** — nenhuma afirmação contrafactual carregada no Plan; o "o que seria observável se a BASpec estivesse errada" (Bloco A) é usado só como teste de verificabilidade, não como alegação; sem achado.
- **RULE-UNC-01..03 (incerteza):** sem achado — incerteza localizada (eficiência de consulta ampla até H-001) declarada; completude do trace NÃO é incerta (obrigação).
- **RULE-PRB (probabilidade):** sem achado — nenhuma probabilidade/precisão numérica declarada; confiança de relação = PARÂMETRO a calibrar, sem número.
- **RULE-DEC-01 (decisão≠execução):** sem achado — o KG armazena/relaciona/consulta; não decide nem executa (INV-05).
- **RULE-MET-01 (não-fabricação):** sem achado — IDs arXiv implausíveis descartados (research.md §aviso); **SRC-FORGET-01 é DADO não-verbatim (WebSearch) e NÃO sustenta sozinha nenhuma alegação carregada** — "esquecimento=arquivamento" apoia-se em INV-07/RULE-BB-004 (FATO NORMATIVO), com SRC-FORGET-01 só como contexto.

**Bloco D — reforço de escopo:** a Spec **preserva/relaciona/consulta** conhecimento permanente, **não guarda trabalho**
(SPEC-004), **não transporta** (SPEC-005), **não forma conhecimento** (SPEC-007), **não executa** ordem (INV-05/RULE-DEC-01
— §7), **não decide** nem **computa** convicção. Nenhuma BASpec cruza a fronteira SOT→execução downstream. Toda
dependência de decisão de Andraus está marcada [PROPOSTA]/[DECISÃO NECESSÁRIA] na tabela de etiquetagem (fonte única), não fechada.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001; CHM-001; CCM-001; CEE-001; SAS-001; SPEC-004 v1.2; SPEC-005 v1.0; SPEC-001/019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5 (§10.2 E3); RULES v1.5 (RULE-BB-004, RULE-CAU-01/02/03, RULE-MECH-01, RULE-HD-*); INV-*; ENF-*; CONSTITUTION l.233 | [FONTE] | FATO NORMATIVO |
| RULE-CKG-001..013; INV-CKG-01/02; matriz §D2.1; tabelas §D2.2/§D2.3; envelope `kg_record`, log `kg_gate_decision`, função `estado(v,T)` e contrato de nó/relação; campo `school`; elos de versão; bounded loop; BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| DHR-BACKLOG-001 (promoção BL-003/BL-011 a ATIVADO) | [FONTE — comunicada pelo Orquestrador] | Decisão de Andraus; ata não presente neste checkout — conferência do Orquestrador/Revisor |
| Fontes SRC-ZEP-01/PROV-01/MEMVSKG-01; REPO-graphiti/graphrag/cognee/mem0 | [EXTERNO] | Referência — DADO, nunca baseline |
| SRC-FORGET-01 (sumário WebSearch) | [EXTERNO] | DADO **não-verbatim** — não sustenta sozinha alegação carregada (§7-bis Bloco C) |
| Mecanismo físico de armazenamento | [DECISÃO NECESSÁRIA] | **H-001 — EM ABERTO — não fechar** (Andraus; contrato cognitivo independe dela) |
| Banco de grafos dedicado (Opção B) | [DECISÃO NECESSÁRIA] | **ADIADO** — registrado, não apagado (INV-07) |
| Escala numérica de confiança de relação | [DECISÃO NECESSÁRIA] | **PARÂMETRO a calibrar** — INDETERMINADO (não toca J-001/N-001) |
| Contrato do selo de publicação — caminho (b) | [DECISÃO NECESSÁRIA] | Dependência da **SPEC-007**; até lá DENY `SEAL_CONTRACT_UNDEFINED` (v1.5) |
| Critério/produtor/gatilho de admissão do caminho (a) (canônico) | [DECISÃO NECESSÁRIA] | **Pendente de Andraus** — DENY `PATH_A_ADMISSION_PENDING`; [PROPOSTA] mínima só para hypothesis |
| Contrato do caminho (c) (relações registradas por produtor — SAS-001 l.924) | [DECISÃO NECESSÁRIA] | v1.5 — DENY `ENTRY_PATH_UNDEFINED` |
| Caminho de nós asset/timeframe/regime/observation/calibration_metric/structure/narrative/mission | [DECISÃO NECESSÁRIA] | DENY `ENTRY_PATH_UNDEFINED`; obrigação CEE-001 l.111 PARCIAL |
| Mapeamento `producer_id` → `school` (SMC/Fibonacci/ICT/Fractal) | [PROPOSTA] (tabela) / [DECISÃO NECESSÁRIA] (ids) | Só Elliott conhecido (SPEC-001 l.203) ⇒ demais `SCHOOL_UNDERIVABLE`; Fractal sem produtor listado (AGENTS §3.2) |
| Reconciliação COL-EXP-05 (EXP-SPEC-021 ↔ RAG-SPEC-018) | [DECISÃO NECESSÁRIA] | Adiada (CONFLICT-MAP l.147); BL-011 `Em espera`, não promovido |
| Limiar/amostra de falso-DENY (ENF-07) | [DECISÃO NECESSÁRIA] | Gap aberto (atomic-spec l.273/l.393); só o método amostral está declarado |
| Mantenedor da allowlist de escritores / host do juízo CKG-008 / migração de ontologia | [DECISÃO NECESSÁRIA] | Runtime/governança — não decidido aqui; allowlist indefinida ⇒ DENY `WRITER_ALLOWLIST_UNDEFINED` (v1.5) |
| Consumidor/contrato de consumo de eventos (`Evidence.Invalidated`) pelo KG | [DECISÃO NECESSÁRIA] | SPEC-005 transporta; consumidor não definido |
| Reatribuição do critério de promoção (S14) à SPEC-018/K-001 | [DECISÃO NECESSÁRIA] | Proposta a Andraus, não fato |
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
[x] Critérios em EARS (15); BASpecs completas (CKG-001..013) com Classe (CC-11); RULEs citadas existentes vs propostas etiquetadas.
[x] Profundidade D0–D7 (+ D8 focado) atingida; D2.1 (matriz) + D2.2 (colisão) + D2.3 (caminhos); D4 (envelope_completo único, version/supersedes por kind, kg_gate_decision, estado(v,T), bounded loop, fronteira, elos de versão, ancestrais); D5 (transitórios CANDIDATE_WRITE/REJECTED); D6; D7 x20 (T01..T20); D8 ADV-CKG-01..22; D9.
[x] Enforcement Contract em todo ato com efeito (EC-CKG-001..006); escrita permanente = E3 (001..005); E1 consulta (006); ENF-07: método amostral sobre kg_gate_decision; limiar = gap aberto — CONDICIONAL.
[x] EC-CKG-001/003 PRECOND: nenhum caminho/allowlist pendente satisfaz a precondição (DENY por desenho — v1.5 M1).
[x] Status epistemológico aplicado (FATO NORMATIVO / PROPOSTA / EXTERNO / DECISÃO NECESSÁRIA); documentado ≠ homologado.
[x] CONS-01 respeitado: H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 permanecem ABERTAS; nenhuma decisão aberta usada como invariante fechado.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Achados da rodada 6 (C1–C2, M1–M10, m1–m8, G) tratados — rastreabilidade em checks.md §11.
[x] Integridade: nenhuma fonte inventada; nenhuma RULE fabricada; linhas canônicas verificadas (CEM-001 l.450/460-475/494/530/560/562-565/594-595/602/608-615/699; CHM-001 l.283/329/361/588/744-757/767-769; CCM-001 l.58; CEE-001 l.111; SAS-001 l.924; CONSTITUTION l.191-192/233; SPEC-001 l.203; SPEC-002 l.370-371; SPEC-003 l.387-388; atomic-spec l.315; RULES.md l.324/672/678/681-683; CONFLICT-MAP l.143-147). DHR-BACKLOG-001 NÃO localizada neste checkout (citada como comunicada pelo Orquestrador).
[x] 4Es na ordem; Conformidade > Eficácia. Latência não é material para memória permanente (consulta opcional/não-bloqueante — SAS-001 §6.12).
[x] Dependências a montante homologadas; não downstream de bloqueador aberto não resolvido (H-001 é desta Spec — proposta de recorte; selo SPEC-007 marcado como dependência [DECISÃO NECESSÁRIA]).
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D); Bloco A: 13 BASpecs verificáveis como predicado/fixture, admissão positiva INDETERMINADO; Bloco B: "todos os estados", "todas as versões" e CEE-001 l.111 = evidência PARCIAL/[DECISÃO NECESSÁRIA]; Bloco C cobre N8–N17.
[x] CC-11/§10.6: Classe por BASpec; Classes C com gate de saída; Classe H (CKG-008) com bounded loop (≤1 invocação por submissão; KG sem retry; ⇒ INDETERMINADO) + gate de saída sobre TODA CAUSA/SIMILAR_A.
[x] Abertura (RULE-ECC-01/02/04/06): Dossiê presente e HOMOLOGADO (DHR-SPEC006-001); escopo/quantidade/número homologados (1 Spec).
[x] Passo 11-bis: BL-003/BL-011 — promoção decidida por Andraus (DHR-BACKLOG-001, comunicada); BL-010 tangente; BL-029 `Em espera`, independente; RMR-001 não editado.
[ ] Gate determinístico (validate_spec_sot.py), revisor_gate.py, check_repo_research.py, build_map.py (+ --check), check_doc_sync.py, check_invariants.py: **NÃO executados por mim (sem Bash)** — listados em checks.md para o Orquestrador rodar.
```

---

**Pronto para revisão.**

**[DECISÃO NECESSÁRIA] / abertas (não fechadas — CONS-01):** lista ÚNICA na tabela "Etiquetagem e Status Epistemológico"
acima (v1.5 — consolidação m8). H-001 permanece ABERTA (recorte proposto, não decidido); J-001/N-001/M-001/G-001/K-001/
C-001/WF-D03/ECC-03-001 não tocadas.

Carregado para o Revisor (rodada 6):
- **Limitação funcional declarada:** com (a), selo (b), (c), nós de referência e allowlist pendentes, o KG hoje **não admite nenhuma escrita** (§D2.3); tudo o que é verificável são predicados de gate e fixtures; admissão positiva fim a fim = INDETERMINADO.
- Respostas às 8 interpelações do parecer da rodada 5: checks.md §11-bis (âncoras arquivo:linha desta v1.5).
- Baselines que citam o KG tratadas **sem erratum** (CEM-001 l.494/562-565/608-615/699; SAS-001 §6.12; CONSTITUTION l.233; CEE-001 l.111 — INV-09).
- **Volume (Q-ABERTURA-5):** ver checks.md §11 (número de linhas); a divisão é decisão de Andraus — o Especificador **não** divide por conta própria.
