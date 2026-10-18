# SPEC-006 — Cognitive Knowledge Graph

| Campo | Valor |
|---|---|
| ID | SPEC-006 — Cognitive Knowledge Graph (contrato cognitivo da **memória semântica permanente** do SOT — ontologia enxuta + entidades/relações tipadas + temporalidade + proveniência por referência + lifecycle + confiança de relação + consulta cognitiva + governança de escrita; **mecanismo físico de armazenamento INDETERMINADO — H-001 ABERTA**) |
| Versão | 1.6 (candidato a BASELINE — rodada 7) |
| Status | **CANDIDATO — aguarda verificação de spec (checks.md), gate determinístico, parecer do Revisor e homologação de Andraus.** NÃO é baseline (INV-09). **Hoje o KG é integralmente fail-closed** (todo caminho de entrada depende de [DECISÃO NECESSÁRIA] — §D2.3); o contrato é verificável por predicados de gate e fixtures, a admissão positiva fim a fim é INDETERMINADO. Abertura HOMOLOGADA: DHR-SPEC006-001 (2026-10-11). As RULE-CKG-* e o contrato de nó/relação deste Plan são **[PROPOSTA]** até homologação. **H-001 (mecanismo físico do KG) permanece ABERTA — este Plan NÃO a fecha** (CONS-01; só Andraus). M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 seguem ABERTAS. |
| Fonte | ROADMAP §6 (FASE 3); `specs/features/SPEC-006/ABERTURA.md` + `research.md` + `sources/` (Dossiê — RULE-ECC-01/02/04/06; validade CRITICAL 90 dias, limite 2027-01-03); DHR-SPEC006-001; atomic-spec **v1.5** (§3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7); `governance/RULES.md` (RULE-BB-004, RULE-CAU-01/02/03, RULE-MECH-01, RULE-HD-02/03/04); `canon/CEM-001` (Responsabilidades do KG l.608-615), `canon/CHM-001`, `canon/CCM-001`, `canon/CEE-001` l.111, `canon/SAS-001` §6.12; `WORKFLOW.md` (conformidade, não editada) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §6 "P0 — CRITICAL"; atomic-spec §3 (emenda SPEC006-MATRIZ, 2026-10-05) "Knowledge Graph \| CRITICAL \| D0–D7"; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profundidade-alvo | **D0–D7 + D8 adversarial focado** nos pontos sensíveis (imutabilidade INV-07, confiança de relação ≠ Convicção INV-04, causalidade pós-hoc RULE-CAU, colisão de relações, governança de escrita), **sem elevar o profile em silêncio** — mesma reconciliação da SPEC-004 (CRITICAL, pin D0–D7, homologada "D0–D7 + D8 adversarial") [FONTE: ROADMAP §6; AGENTS.md §4; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 3 — MEMÓRIA SEMÂNTICA E RAG; próxima na sequência após SPEC-005 (BASELINE v1.0, DHR-SPEC005-002). Opera **sobre** conhecimento já validado/publicado; a formação/retrieval é SPEC-007 (não absorvida) [FONTE: ROADMAP §6/§21] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3 teto spec-first; gate normativo E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01 (Classe por BASpec); RULE-PD-01/CC-12 **(N/A — infraestrutura de memória, agnóstica de escola)**; RULE-ECC-04 (verbatim); RULE-ECC-06 (repositórios); RULE-ECC-05 **(N/A — não toca comportamento de trading)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — **D** (ontologia/catálogo de entidades-relações, temporalidade, versionamento, consulta estruturada, Cognitive Trace Reconstruction) + **C** (governança de escrita, imutabilidade/append-only INV-07, proveniência obrigatória, confiança≠Convicção INV-04, fronteira "só conhecimento publicado") + **H** (juízo de similaridade/causalidade com gate de saída e mecanismo declarado — RULE-CAU); declaração normativa é **por BASpec** (SES-001 §50) |
| Autor | Especificador Principal (Claude Code; v1.0–v1.5 Opus 4.8; v1.6 Opus 5.5) |
| Data | 2026-10-17 (rodada 7; ordem de Andraus, chat 2026-10-17, "Rodada 7 enxugando o texto", após parecer NÃO CONFORME da rodada 6 — `parecer-revisor-rodada6.md`) — rodadas 5/6: 2026-10-17; v1.0..v1.3: 2026-10-11/12 |
| Abertura | Dossiê de Pesquisa HOMOLOGADO por Andraus (DHR-SPEC006-001, `research.md`); Plan iniciado dentro da validade do Dossiê (CRITICAL → 90 dias; limite 2027-01-03; ECC-VAL-001 FECHADA, DHR-DEC-003) |

Complexidade: CRITICAL. Profundidade-alvo: D0–D7 + D8 adversarial focado (standard + adversarial).

**Princípio fundador desta Spec (transversal):** **MEMÓRIA PERMANENTE ≠ MEMÓRIA DE TRABALHO.** *"Blackboard ↓ memória de trabalho. Knowledge Graph ↓ memória permanente. Nunca misturar."* (fundamento KERNEL-V2; ROADMAP §5/§6). O KG é a **representação semântica permanente do conhecimento já validado e suas relações auditáveis** — não é "banco de grafos" (o fundamento-fonte rejeita "banco de dados"; research.md §0) e não é memória de trabalho (SPEC-004). Este Plan define **o QUE** (contrato cognitivo), com o **mecanismo físico de armazenamento declarado INDETERMINADO = H-001 (ABERTA)** — grafo real vs. estrutura em memória vs. tabelas+índice é decisão de engenharia de Andraus, não fechada aqui. [FONTE: ROADMAP §6; DHR-SPEC006-001 Q-ABERTURA-3; research.md §0/§8]

**Status epistemológico de cabeçalho:** a SPEC-006 é a **camada Harness/operacional da memória permanente** sobre responsabilidades que os modelos canônicos BASELINED já atribuem ao KG (CEM-001 l.608-615; l.494; l.562-565 Cognitive Trace Reconstruction; CONSTITUTION l.233 EC-COG-003; SAS-001 §6.12; CEE-001 l.111). **NÃO redefine** CHM-001, CEM-001, CCM-001, nem reabre SPEC-004/SPEC-005 (**CC-02/CONST-01/INV-09**). **H-001** permanece **ABERTA** — este Plan **propõe** o recorte (contrato cognitivo fechável com mecanismo físico INDETERMINADO), não o fecha (decisão de Andraus; CONS-01). [FONTE: ROADMAP §6/§7; atomic-spec §12; DHR-SPEC006-001 §3]

**Convenção de fonte única (v1.6):** cada regra operacional tem UMA seção-fonte — **lógica/predicados e códigos de rejeição em D4.1–D4.18**, **campos no I/O Schema**, **caminhos de entrada na §D2.3**. RULE, BASpec, EARS, EC, cenários e ADV **citam** a seção-fonte e só repetem o mínimo que o formato exige (QUANDO/ENTÃO/VERIFICAÇÃO observável). Em divergência aparente, prevalece a seção-fonte.

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-10-11 | Entrega candidata inicial (Opção A; mecanismo físico INDETERMINADO = H-001). 13 BASpecs (CKG-001..013); 6 EC; 13 EARS; 11 cenários; 10 adversariais. |
| 1.1 | 2026-10-12 | **Rodada 2 (achados do gate, do Revisor e verificados no repositório).** (A) STRUCT-10: removida toda forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta. (B1) §7-bis Bloco C ampliado a todas as N8–N17. (B2) SRC-FORGET-01 declarada sem sustentar alegação carregada sozinha. (B3) EC-CKG-002 registra tentativas de DELETE bloqueadas. (B4) falha de auth da SPEC-004 ⇒ não-autorizado (fail-closed). (C1) escrita permanente elevada a **E3** (atomic-spec §10.2); "piso E2" eliminado. (C2/C9) **duas fontes de entrada** reconciliadas sob uma trilha de governança única; preservação de REFUTED/SUPERSEDED/ARCHIVED declarada; selo de publicação = dependência de SPEC-007 [DECISÃO NECESSÁRIA]. (C3) Cognitive Trace Reconstruction = obrigação **completa** (independe de H-001); T10 ampliado a 3 saltos. (C4) tipo de relação **DERIVA_DE** (aresta de Lineage) acrescentado, separado de `provenance_ref`. (C5) matriz de integridade tipo×origem/destino×direcionalidade/simetria + "família estrutural" + teste de violação. (C6) invalidação/supersessão como **novos registros**; estado = projeção derivada (espelha SPEC-004 INV-CBP-01). (C7) schema com `version`/`supersedes`/selo/escritor/colisão; REJECTED/CANDIDATE_WRITE = estados transitórios (não persistidos). (C8) BL-029 corrigido para **`Em espera`**. (C13) critérios de SUPERSEDED×INVALIDATED_IN_TIME×ARCHIVED, correção/reativação, rebaixamento, autoridade de arquivamento. (C14) `recorded_at` acrescentado à relação (bitemporal real). (C17) RULE-CAU-02 (regime) e RULE-CAU-03 (marcador pós-hoc) incorporadas; atribuição pós-hoc corrigida; gate causal só verifica presença. (C18) node_type **observation** (INV-06). (C21) emissão de evento pelo KG **removida** (só consome); emissão = [DECISÃO NECESSÁRIA] dependente da SPEC-005. (C22) governança/versionamento da ontologia definida (spec-time SPEC-019; runtime K-001 [DECISÃO NECESSÁRIA]). Extra: `gate_record` reatribuído à SPEC-004 (não CEM-001). Cobertura: 13 BASpecs; 6 EC; 13 EARS; 13 cenários (T01..T13); **15 adversariais** (ADV-CKG-01..15). |
| 1.2 | 2026-10-12 | **Rodada 3 (defeitos confirmados por revisão independente, verificados no repositório).** (1) Matriz §D2.1: HERDA = sub→pai pelo `parent_id` (SPEC-001)/`parent_hypothesis_id` (CHM-001), inclusive **entre escolas** (SMC/Fibonacci SUB → Elliott PRIMARY — SPEC-001 RULE-HH-003 l.104; CONSTITUTION l.193); "família estrutural" só restringe sub-hipóteses intra-escola; ORIGINA: origem ∈ {Elliott, SMC, Fibonacci}, nunca ICT (INV-02); atributo `school`/`origin_agent` (por referência ao canônico); o KG só **espelha**, não decide, a autoridade de criação (CC-01). (2) `lineage_ref` (campo inexistente) → `provenance_ref.lineage` [PROPOSTA] = referência ao campo `Lineage` (CEM-001 l.351/359/539-554) / `derived_from[]` (SPEC-004). (3) Preservação de estado canônico: `canonical_status` (snapshot) + registro `canonical_state_transition` (estado/timestamp/origem/justificativa — CEM-001 l.428); estados do KG ≠ estados canônicos (CC-10). (4) Critério de admissão Blackboard→KG do caminho (a) = [DECISÃO NECESSÁRIA] (promoção trabalho→permanente — SPEC-018/K-001). (5) Completude do trace garantida: admitir evidence DERIVED ⇒ exigir aresta DERIVA_DE por ancestral do Lineage (fail-closed); trace ignora validade e é acíclico (INV-CKG-02); teste negativo. (6) INV-04 = só custo; proibição de *confiança* entrar na convicção = regra LOCAL [PROPOSTA] (CKG-007); matriz restringe CAUSA (destino `conviction` proibido a partir de custo/confiança); restrição à SPEC-003 = requisito a ela endereçado/[DECISÃO NECESSÁRIA]. (7) Invalidação de relação = ato AUTORIZADO (CKG-009), **não** automática (CEM-001 l.602 "não implica cascata"; impacto é de CHM/CCM — l.503/606; CHM-001 l.672-676); consumo de evento = [INFERÊNCIA]/[DECISÃO NECESSÁRIA] (SPEC-005 não define "Evidence Invalidated"). (8) Schema: `record_kind`, `relevance`, `target_relation_id`, identidade para nós não-canônicos, `collision_record` como registro. (9) "conhecimento permanente/temporário" tratado/diferido (SPEC-018/K-001 [DECISÃO NECESSÁRIA]). (10) CONFIRMA/REFUTA restritas a `evidence` (INV-06; CONSTITUTION l.191). (11) Bitemporal: consulta valid-time + transaction-time (as-of-registro). (12) Citação RMR-001 → l.128/l.192. (13-18) correções menores. Contagem: 13 BASpecs; 6 EC; 13 EARS; **14 cenários** (T01..T14); **16 adversariais** (ADV-CKG-01..16); 2 invariantes locais (INV-CKG-01/02). |
| 1.3 | 2026-10-12 | **Rodada 4 (6 Maiores do controle, confirmados no repositório).** (1) **T01 corrigido** (a v1.2 NÃO o havia reescrito): T01 agora usa ORIGINA com `school=ICT` (caso que a matriz DE FATO rejeita) + novo **T15 positivo** HERDA SMC-SUB → Elliott-PRIMARY (RULE-HH-003). (2) **Campos unificados:** um só campo `school` (eliminado "origin_agent"); adicionado `hierarchy_role` {PRIMARY,SUB} (ref. SPEC-001); "família" COMPUTADA via `school`+PERTENCE_A(asset,timeframe); regra de nó `hypothesis.school ≠ ICT` (INV-02/RULE-HH-004) com teste (T01) e **ADV-17**; HERDA.pai restrito a `hierarchy_role=PRIMARY`. (3) **gate_record CONDICIONAL** (espelha SPEC-004 CBP-007): `computed_by`/`writer_id` SEMPRE obrigatório; `gate_record` só se há gate; `lineage`/`derived_from` só se derivado; `[]` legítimo (PRIMARY/asset/timeframe/regime/observation); CKG-005/T12/T14/schema ajustados. (4) **SPEC-005/Evidence.Invalidated corrigido:** o tipo é canônico (CEM-001 l.600/722) e a SPEC-005 o TRANSPORTA (l.88/859); o que falta é o consumidor/contrato de consumo pelo KG = [DECISÃO NECESSÁRIA] (linhas l.115/242 — que eram o envelope — removidas). (5) **CKG-013/colisão:** tabela de pares contraditórios §D2.2 (CONFIRMA×REFUTA; INVALIDA×relação-alvo) + escopo (mesmos from/to + sobreposição de validade) + algoritmo D4 + teste negativo **ADV-18** (origens distintas/validades disjuntas não colidem). (6) **CKG-010/admissão:** gate (a) declarado NÃO-ESPECIFICADO/INDETERMINADO (não vacuoso) + [PROPOSTA] de critério mínimo (estados ACTIVE/DOMINANT/SUPERSEDED/REFUTED/ARCHIVED; exclui EMERGENT/CANDIDATE); reatribuição de S14 à SPEC-018/K-001 submetida a Andraus [DECISÃO NECESSÁRIA]; ordem de admissão de ancestrais (`PENDING_ANCESTOR`, sem deadlock de INV-CKG-02). Histórico reordenado 1.0→1.3. Contagem: 13 BASpecs; 6 EC; 13 EARS; **15 cenários** (T01..T15); **18 adversariais** (ADV-CKG-01..18); 2 invariantes locais. |
| 1.4 | 2026-10-17 | **Rodada 5 (retomada por ordem de Andraus, chat 2026-10-17; 4 defeitos conferidos pelo Orquestrador + 8 reportados por revisões anteriores, cada um reconferido no repositório).** **(V1)** D6 passo 5 alinhado à proveniência CONDICIONAL de CKG-005 (`computed_by` sempre; `gate_record` sse gate; `lineage` sse derivado; `[]` legítimo) + **T16** (teste de sequência D6 para PRIMARY sem gate e sem ancestral). **(V2)** Caminho (a) CANÔNICO de CKG-010 retirado do PRECOND do EC-CKG-001: enquanto o critério de admissão estiver pendente de Andraus, (a) é **fail-closed — não admite** (`PATH_A_ADMISSION_PENDING`); frase de cobertura do §7-bis corrigida (a admissão positiva por (a) é INDETERMINADO, não verificável); convenção de teste (gate em isolamento × persistência condicional) declarada em D7; **ADV-CKG-21**. **(V3)** **Envelope único append-only** (`kg_record`) para TODO tipo de registro (creation/invalidation/archival/canonical_state_transition/collision) com `record_id`/`version`/`supersedes`/`target_record_ref`/`schema_version`/proveniência/`writer_id`/`recorded_at`/validade; eliminados o `collision_record` avulso e o `record_kind=collision` dentro de `relation_record` (um só formato de colisão) + **T17** (reconstrução/auditoria) + **ADV-CKG-19**. **(V4)** BOUNDED LOOP da CKG-008 = **uma passada por submissão**, sem retry automático; ao esgotar ⇒ INDETERMINADO, nada escrito; fonte atomic-spec §10.6 l.315 + RULE-INQ-03 (RULES l.678) + precedente SPEC-002 l.370-371/SPEC-003 l.387-388; versionado com RULE-CKG-008 (alteração só por emenda spec-time) — refletido em RULE/BASpec/D4/EC-CKG-005 + **ADV-CKG-20**. **(R1)** `PENDING_ANCESTOR` incluído na máquina de estados D5 (transitório, limitado ao lote de admissão) e na sequência D6 + **T19**. **(R2)** enum de `canonical_status` corrigido por baseline: `REFUTED` é só do CHM-001; CEM-001 = ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED (l.258-262); CCM-001 = COMPUTED/GATED_PASS/GATED_BLOCK/SUPERSEDED (l.58). **(R3)** `school` declarado campo LOCAL [PROPOSTA] **derivado** de `producer_id` canônico (CHM-001 §2.9 l.361; CEM-001 l.276-278) — não é campo canônico; enum = 5 camadas da hierarquia (inclui **Fractal**, ausente na v1.3); regra espelho RULE-HH-002 (PRIMARY ⇒ Elliott); mapeamento produtor→Fractal = [DECISÃO NECESSÁRIA]; `school` ≠ `Domain` (CC-10). **(R4)** COL-EXP-01..05 (CONFLICT-MAP l.143-147) ganham tabela de tratamento; reconciliação COL-EXP-05 permanece adiada ([DECISÃO NECESSÁRIA]). **(R5)** SIMILAR_A ganha gate de saída determinístico (`similarity_basis` presente ∧ mesmo node_type ∧ from≠to; duplicata simétrica = no-op) + **T18** + **ADV-CKG-22**. **(R6)** EC-CKG-004 elevado a **E3** (guard sobre a escrita permanente — piso atomic-spec l.238). **(R7)** nó ganha `valid_from`/`valid_to` e todo registro ganha `target_record_ref` (via envelope). **(R8)** limiar de falso-DENY mantido como gap aberto (atomic-spec l.273/l.393); declarado só o MÉTODO amostral, sem valor. Extra: linhas de RULES.md corrigidas (RULE-BB-004 l.324; RULE-ONT-01 l.672; RULE-CAU-01/02/03 l.681-683); caminho de entrada de nós de referência (asset/timeframe/regime/observation/calibration_metric) declarado lacuna [DECISÃO NECESSÁRIA]. **Permanecem [DECISÃO NECESSÁRIA]:** critério/produtor/gatilho do caminho (a); caminho de nós de referência; selo SPEC-007; mapeamento produtor→Fractal; consumidor de eventos; emissão pelo KG; allowlist/host do juízo; migração de ontologia; escala de confiança; limiar de falso-DENY; reconciliação COL-EXP-05; H-001, J-001, N-001, M-001, G-001, K-001, C-001, WF-D03, ECC-03-001 (todas ABERTAS). Contagem: 13 BASpecs; 6 EC; 13 EARS; **19 cenários** (T01..T19); **22 adversariais** (ADV-CKG-01..22); 2 invariantes locais (INV-CKG-01/02). |
| 1.5 | 2026-10-17 | **Rodada 6 (parecer NÃO CONFORME da rodada 5 — `parecer-revisor-rodada5.md`; Plan devolvido por Andraus, chat 2026-10-17).** **(C1)** "preservar TODAS as versões" (CEM-001 l.612; l.594-595; l.450): mecanismo `canonical_predecessor_ref` (espelha `previous_version_id` — CHM-001 l.283/588; CCM-001 l.58) + `successor_ref` obrigatório quando `status_to=SUPERSEDED` (gate `VERSION_LINK_MISSING`); T17 (fixture H@1→H@2) + ADV-19(d); Bloco B: evidência PARCIAL/[DECISÃO NECESSÁRIA] (admissão por (a) pendente). **(C2)** CEE-001 l.111: evidência PARCIAL/[DECISÃO NECESSÁRIA] (`calibration_metric` sem caminho de entrada); ADV-05 reescrito (só o isolamento é verificável). **(M1)** caminho (b) e allowlist tratados como (a): contrato do selo pendente ⇒ DENY `SEAL_CONTRACT_UNDEFINED`; mantenedor da allowlist pendente ⇒ DENY `WRITER_ALLOWLIST_UNDEFINED`; "verificável" restrito a predicados. **(M2)** tabela única de caminhos de entrada §D2.3 (nós, relações espelhadas, relações de produtor — SAS-001 l.924 — = caminho (c) [DECISÃO NECESSÁRIA]); convenção de teste (iv) para o detector de colisão (T11/ADV-02/ADV-18 por fixture). **(M3)** EARS 14/15 + **T20** (`ENTRY_PATH_UNDEFINED`, `SCHOOL_UNDERIVABLE`, `WRITER_ALLOWLIST_UNDEFINED`); só Elliott tem `producer_id` conhecido (SPEC-001 l.203) ⇒ SMC/Fibonacci/ICT/Fractal hoje `SCHOOL_UNDERIVABLE`. **(M4)** linha INVALIDA×relação-alvo removida da §D2.2 (INVALIDA ≠ registro `invalidation`); ADV-18(d). **(M5)** gate de CKG-008 = TODA relação CAUSA/SIMILAR_A, qualquer produtor; bounded loop só quando há juízo. **(M6)** memoização removida; limite = 1 invocação por submissão, KG não gera retry; ADV-20 reescrito. **(M7)** conceito "lote"/`PENDING_ANCESTOR` eliminado: ancestral ausente ⇒ REJECTED imediato; T19 por fixture. **(M8)** `envelope_completo` único (D4) referenciado por RULE/schema/EC; `gate_record` = só objeto que RESULTA de gate (upstream ou detector de colisão); decisões dos gates do próprio KG (PASS/DENY/INDETERMINADO) vão ao log `kg_gate_decision` (formato próprio, declarado). **(M9)** guard CKG-007 determinístico por `node_type` (CAUSA `calibration_metric`→`conviction`; nenhum campo de confiança no payload de `conviction`); limite declarado. **(M10)** função de projeção com precedência ARCHIVED > SUPERSEDED > INVALIDATED_IN_TIME > ACTIVE_KNOWLEDGE e `version`/`supersedes` de todos os `record_kind`. **(m1–m7)** âncora CONSTITUTION l.191-192 + INV-06; T01/verificação CKG-001 alinhados; limite de digest declarado; `VALIDITY_WINDOW_INVALID`; limite de gates de presença; legalidade de transição CHM/CEM (`CANONICAL_TRANSITION_ILLEGAL`; CCM sem tabela ⇒ espelha sem validar); cobertura CKG-010→T09/ADV-21. **(m8)** consolidação (listas finais fundidas na tabela de etiquetagem; caminhos numa tabela única). **(G)** gatilho `spec:SPEC-006 em redação` de BL-003/BL-011 tratado pela decisão de Andraus comunicada pelo Orquestrador (ata DHR-BACKLOG-001) — RMR-001 não reaberto. **Permanecem [DECISÃO NECESSÁRIA]:** critério/produtor/gatilho de (a); contrato do selo (b); contrato do caminho (c); caminho de nós de referência e de structure/narrative/mission; mantenedor da allowlist; host do juízo; mapeamento `producer_id`→`school` (SMC/Fibonacci/ICT/Fractal); consumidor de eventos; emissão pelo KG; migração de ontologia; escala de confiança; limiar de falso-DENY; COL-EXP-05; H-001, J-001, N-001, M-001, G-001, K-001, C-001, WF-D03, ECC-03-001 (ABERTAS). Contagem: 13 BASpecs; 6 EC; **15 EARS**; **20 cenários** (T01..T20); 22 adversariais (ADV-CKG-01..22); 2 invariantes locais. |
| 1.6 | 2026-10-17 | **Rodada 7 (parecer NÃO CONFORME da rodada 6 — `parecer-revisor-rodada6.md`; ordem de Andraus, chat 2026-10-17: "Rodada 7 enxugando o texto").** **Método:** fonte única por regra — predicados/códigos em **D4.1–D4.18** (numerados), campos no schema, caminhos na §D2.3; RULE/BASpec/EARS/EC/cenários/ADV citam por referência; cenários idênticos ao VERIFICADO POR de uma BASpec passam a referenciá-lo. **(N1)** ata `governance/DHR-BACKLOG-001_…md` e RMR-001 l.102/110/191 (BL-003/BL-011 `ATIVADO`) citados corretamente em todas as ocorrências; encaminhamento item a item de X-01, R-01..R-07 e X-04 (R-04..R-06 definidos por conteúdo — [INFERÊNCIA]); R-07/COL-EXP-05 e fila EXP-SPEC = [DECISÃO NECESSÁRIA]; pergunta "este Plan é a ativação?" removida (a ata decidiu). **(N2)** discriminantes fixos `provenance_ref.produced_by_gate` (booleano explícito) e `evidence_origin_type` (espelho CEM-001 l.280-283) + código `PROVENANCE_INCONSISTENT` (D4.2). **(N3)** `producer_type`/`producer_id` no payload (CHM-001 l.361; CEM-001 l.271-278); limite: o espelho de INV-02 é de FORMA (sem lookup ao canônico). **(N4)** `kg_gate_decision` append-only e imutável sob RULE-CKG-006/EC-CKG-002 (E3), `decision_id` único; T17 resolve o `gate_record` do collision no log; redução a `record_kind` avaliada e rejeitada (D4.5). **(N5)** colisão detectada no passo 8 e gravada só na unidade atômica tudo-ou-nada da admissão (D4.18; SPEC-004 plan l.381/l.689) + **T21**. **(N6)** elos de versão tipados por modelo (D4.16); `successor_ref` obrigatório só para CEM (l.450), [PROPOSTA] local opcional para CHM/CCM; elos presentes DEVEM resolver no KG. **(N7)** `posthoc_flag` obrigatório com valor explícito; ADV-04 reescrito. **(N8)** guard único de custo E confiança (D4.12): payload de `conviction` FECHADO (`additionalProperties:false`). **(N9)** EARS 16–20 (`ANCESTOR_NOT_ADMITTED`, `VERSION_LINK_MISSING`, `CANONICAL_TRANSITION_ILLEGAL`, `VALIDITY_WINDOW_INVALID`, `RECORD_VERSION_INVALID`) + ADV-19(g). **(N10)** "todos os estados/todas as versões" = obrigação herdada só para Evidência (CEM-001 l.494/612); extensão a hipótese/convicção = [PROPOSTA] local em conflito com o critério mínimo de (a) — [DECISÃO NECESSÁRIA]. **(N11)** `colide` com `valid_to_efetivo` (D4.13); §D2.2 e ADV-18(b) alinhados. **(n1–n9)** checks:86 reescrito; `estado(v,T)` só para T ≥ valid_from + `recorded_at` monotônico; INVALIDA→relação via `target_relation_id` (não é node_type); escritor dos registros internos (§D2.3); checks:95 corrigido; convenção (v) de fixtures; EC-006 sem PRECOND de autorização inexistente (autorização de leitura = [DECISÃO NECESSÁRIA]); transição perdida = limite fail-closed + reconciliação [DECISÃO NECESSÁRIA]; host do juízo pendente ⇒ 0 invocações. **Permanecem [DECISÃO NECESSÁRIA]:** as da v1.5 + R-07/fila EXP-SPEC; extensão de preservação a hipótese/convicção × critério de (a); reconciliação de transição perdida; autorização de leitura; coincidência `producer_id`↔objeto canônico (contrato de (a)); H-001, J-001, N-001, M-001, G-001, K-001, C-001, WF-D03, ECC-03-001 (ABERTAS). Contagem: 13 BASpecs; 6 EC; **20 EARS**; **21 cenários** (T01..T21); 22 adversariais; 2 invariantes locais. |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; `governance/DHR-BACKLOG-001_Ata_Promocao_BL003_BL011_ATIVADO.md` §1-§2; `backlog/RMR-001_Painel_Backlog.md` l.102 (BL-003), l.110 (BL-011), l.128 (BL-029), l.191 (nota DHR-BACKLOG-001), l.192 (DHR-SPEC006-PEND-001); `governance/CLASSIFICACAO-COLISOES-BL010-011-012.md` l.23/l.51-62; `governance/CONFLICT-MAP.md` l.143-147]

- **BL-003 e BL-011 estão `ATIVADO`** (Andraus, chat 2026-10-17; ata DHR-BACKLOG-001 §1; RMR-001 l.102/l.110/l.191), com **encaminhamento ao gate da SPEC-006**; nada `Absorvido`. *(v1.6 — N1: a v1.5 afirmava que a ata não constava do checkout e que o BL-011 seguia no estado anterior; ambos falsos — corrigido.)* O Especificador não edita o RMR-001; mudança de estado (ex.: `Absorvido`) é de Andraus.
- **BL-003** (persistência física de hipótese/estado). **Encaminhamento:** a camada LÓGICA da persistência permanente é este contrato (envelope `kg_record`, D4.3–D4.7); a parte FÍSICA **é** H-001/G-001 (ABERTAS — ata §2) → referenciada, não absorvida. Se o BL-003 permanece `ATIVADO` até H-001/G-001 ou é dado por tratado na homologação deste Plan = **[DECISÃO NECESSÁRIA]** (Andraus).
- **BL-011** (MC-EXP-001, ref. externa K-MAN-15) — insumo de requisitos de SPEC-004/006/009/018. Os rótulos R-xx/X-xx **não** são catálogo fechado; a correspondência rótulo→conteúdo é a da CLASSIFICACAO (l.23 — [INFERÊNCIA] por conteúdo). **R-04..R-06** = os "tratamentos residuais de aplicação" (CLASSIFICACAO l.62) que o RMR-001 l.110 enuncia como "confidence≠Conviction/J-001; Experience Packet projeta CEM", lidos junto das 3 fronteiras da CLASSIFICACAO l.58-60 — **[INFERÊNCIA]** (o número exato de cada um não é [FONTE]). Encaminhamento item a item:

| Rótulo | Conteúdo (fonte) | Decisão classificada | Encaminhamento nesta Spec |
|---|---|---|---|
| X-01 | COL-EXP-01 — status "BASELINE" do MC-EXP-001 (CONFLICT-MAP l.143) | REJEITAR efeito → PROPOSTA | **TRATADO:** nenhum texto do MC-EXP-001 citado como norma (INV-09). |
| R-01 | COL-EXP-02 — Quality Gates G0–G8 (l.144) | REJEITAR global → gate LOCAL | **TRATADO:** nenhum rótulo G-xx; maturidade L3 (RULE-MM). |
| R-02/R-03 | COL-EXP-03 — I-EXP-01..12 / EXP-P01..P14 (l.145) | ADAPTAR como LOCAIS | **TRATADO:** nenhum ID importado; equivalências só por âncora SOT — imutabilidade → RULE-BB-004/INV-07 (CKG-006); pós-hoc → RULE-CAU-03 (CKG-008). |
| R-04 [INFERÊNCIA] | `confidence`/`performance_metrics` ≠ Conviction Vector (CLASSIFICACAO l.59; RMR l.110) | CONFORME — J-001 aberto | **TRATADO:** confiança de relação ≠ Convicção, guard D4.12 (CKG-007); J-001 em aberto, não tocada. |
| R-05 [INFERÊNCIA] | Experience Record/Packet projeta CEM/CHM (CLASSIFICACAO l.58) | CONFORME — CC-02 | **TRATADO:** nó referencia o canônico por id@version, não redefine (CKG-002). |
| R-06 [INFERÊNCIA] | memória sem autoridade decisional (INV-05); imutabilidade (INV-07/RULE-BB-004) (CLASSIFICACAO l.60) | CONFORME | **TRATADO:** D0/D1 (KG não decide); CKG-006 (append-only). |
| X-04 | COL-EXP-04 — Working Memory §7.6 (l.146) | ADIAR/RELOCAR a SPEC-004 | **TRATADO como fronteira:** memória de trabalho = SPEC-004 (Non-goals D1). |
| R-07 | COL-EXP-05 — EXP-SPEC-021 ↔ RAG-SPEC-018, duplicação sobre RULE-004 (l.147) | ADIAR reconciliação (SPEC-006/009) | **NÃO executado:** a SPEC-006 não especifica "Experience Independence" nem redefine RULE-004. Reconciliar no gate desta Spec, na SPEC-009 ou junto da SPEC-007 (dona do BL-010) = **[DECISÃO NECESSÁRIA]**; idem a reconciliação da fila EXP-SPEC-001..053 (RMR l.110). |

- **BL-010** (MC-RAG-001) — `Em espera`, gatilho `spec:SPEC-007 em redação` ∨ `milestone:FASE 3 iniciada`. Fonte de requisitos da **SPEC-007** → **tangente**; a SPEC-006 respeita a fronteira (recebe conhecimento publicado). **Não promovo** (gate/Andraus decidem o ramo `milestone`).
- **BL-029** (proveniência/"LLM propõe, harness recomputa") — **`Em espera`** (RMR-001 l.128; DHR-SPEC006-PEND-001, l.192); gatilho `spec:SPEC-014`/`SPEC-018`/`SPEC-045`; **independente desta Spec** — não absorvido nem promovido. *(Correção v1.1: a v1.0 dizia `ATIVADO`.)*
- O passo 11-bis pleno ocorre na homologação do Plan.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o Knowledge Graph é **infraestrutura de memória agnóstica de escola** — **armazena** conhecimento de qualquer camada analítica (inclusive a relação `HERDA`/`HIERARQUIA_DE`) **sem** alterar a hierarquia nem a autoridade de criação de hipótese (Elliott cria a primária; ICT não cria — INV-01/INV-02). O KG representa a hierarquia como relações; não a redefine, não interpreta, não decide. O campo local `school` enumera as **5 camadas** (Elliott/Fibonacci/Fractal/SMC/ICT) e é derivado do `producer_id` (D4.14); regras espelho: `hypothesis.school ≠ ICT` (RULE-HH-004) e PRIMARY ⇒ Elliott (RULE-HH-002). [FONTE: INV-01/INV-02; ROADMAP §6; SPEC-001 l.100/l.108]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM) nem SPEC-004/005:** **foco.** O KG **preserva** linhagem/versões/estados e faz *Cognitive Trace Reconstruction* **referenciando** os contratos canônicos (CEM-001 l.608-615; l.562-565) — entidades são **referenciadas por ID+versão, nunca redefinidas**; campos espelhados (`producer_*`, `evidence_origin_type`, elos de versão) são cópias de referência, não redefinição. Não reabre SPEC-004 nem SPEC-005. CDM-001/CNM-001 pendentes não acionam CONST-01. [FONTE: CC-02; CEM-001 l.608-615; CHM-001; CCM-001; SPEC-004/005 BASELINE]
- [x] **CC-03 — Conviction Vector:** o KG **não computa** convicção — a **"confiança de relação"** do KG é escala própria da memória e **NÃO é** o Conviction Vector; dimensionalidade=8 (fechada) intocada; a fórmula/pesos/limiares definitivos do Conviction Vector permanecem **pendentes (J-001 ABERTA)** e **não** são tratados aqui; **nenhum limiar numérico de convicção é declarado neste Plan**. [FONTE: INV-03; J-001 ABERTA; N-001 ABERTA]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. O KG não emite sinal de trading, não dimensiona risco, não aplica gates de sinal. **INV-04** (custo nunca entra no Conviction Vector — Convicção ≠ Score) preservado por construção: guard D4.12 (custo E confiança; CKG-007; ADV-CKG-05). [FONTE: CEE-001 §10/§11; INV-04]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D7 + D8 adversarial focado (ROADMAP §6; atomic-spec §3 emenda SPEC006-MATRIZ; DHR-SPEC006-001 Q-ABERTURA-2).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card; §59/§60 tornam-se obrigatórios nas Tasks/Cards (BUILD adiado — atomic-spec §14). Omissão justificada.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem: ROADMAP §6 → Dossiê (research.md, HOMOLOGADO DHR-SPEC006-001) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente; INHERITS/ADDED com ID+versão (RULE-HD-04); REMOVED vazio; nenhum ADDED/MODIFIED contradiz o herdado (RULE-HD-02); extensões locais etiquetadas [PROPOSTA] (ex.: preservação de estados de hipótese/convicção — N10). Eixo VERTICAL (RULE-HV) avaliado e declarado não aplicável. [FONTE: EUA-E04 §8.3; RULE-HD-02/03/04]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI):** aplicado — **mecanismo físico do KG = INDETERMINADO (H-001 ABERTA)**, não como fato; **relações causais exigem mecanismo + regime declarados (RULE-CAU-01/02) e `posthoc_flag` explícito (RULE-CAU-03)** (CKG-008); **sem falsa precisão em "confiança de relação"**; fontes web = DADO [EXTERNO] (research.md §2); SRC-FORGET-01 é DADO não-verbatim e não sustenta sozinha nenhuma alegação carregada (§7-bis Bloco C). [FONTE: RULE-EPI-01..03; RULE-CAU-01/02/03; research.md §8]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM-01):** **INCIDE e tratado** (ver "Declaração de acepção semântica"): **"Conhecimento permanente"** (KG) vs **"memória de trabalho"** (Blackboard/SPEC-004) vs **"documento recuperado"** (RAG/SPEC-007) vs **"Observação"** (Skill — INV-06); **"confiança de relação"** (KG) vs **"Convicção"** (CCM-001); **"esquecimento"** (= arquivamento versionado, nunca deleção — INV-07); **estados do KG** (projeção derivada) vs **estados canônicos homônimos** (rastreados à parte em `canonical_status`). Nenhum termo canônico do GLOSSARIO redefinido (RULE-SEM-04). [FONTE: RULE-SEM-01/04; INV-06; GLOSSARIO]
- [x] **CC-11 — Classe/Mecanismo por BASpec com efeito (RULE-MECH-01):** **INCIDE** — cada BASpec com efeito declara Classe (D/C/H) com critério 4Es; Classes C/H declaram gate de saída determinístico; Classe H declara bounded loop + critério de parada (CKG-008). Declaração por BASpec, nunca por Spec inteira (SES-001 §50). Ver §D3. [FONTE: RULE-MECH-01..04; atomic-spec §9/§10.6]
- [x] **CC-12 — Princípios de Domínio `PD-xx` (RULE-PD-01):** **N/A — não incide** (DHR-SPEC006-001 §2; ABERTURA §6; research.md §7). O KG é **infraestrutura de memória agnóstica de escola**. Mesmo padrão N/A de SPEC-002/004/005. Registrado explicitamente, não supressão silenciosa. [FONTE: RULE-PD-01; atomic-spec §10.7; DHR-SPEC006-001 §2]

**Disciplinas cognitivas N8–N17 incidentes (RULES.md v1.5):** RULE-EPI (H-001 ABERTA ≠ fato; mecanismo físico INDETERMINADO), RULE-CAU-01/02/03 (CKG-008), RULE-MET-01 (não-fabricação — nenhuma escala/limiar de confiança fabricado; nenhuma proveniência fabricada), RULE-UNC-01..03 (incerteza localizada sobre eficiência de consulta multi-salto ampla enquanto H-001 ABERTA — não sobre a completude do trace), RULE-SEM-01/04 (acepções), RULE-DEC-01 (o KG **armazena/relaciona/consulta**, não decide nem executa — INV-05). INDETERMINADO usado onde há incerteza material. (Demais disciplinas no §7-bis Bloco C.)

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-006

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - canon/CEM-001 (BASELINE) — Responsabilidades do KG (l.608-615) sobre a EVIDÊNCIA: preservar toda a linhagem, TODAS
    as versões e TODOS os estados; Cognitive Trace Reconstruction COMPLETA; navegação completa. Também l.494, l.562-565,
    l.699. Campos espelhados: `Producer Type`/`Producer ID` (l.271-278), `Evidence Origin Type` (l.280-283), `Lineage`
    (l.351-355). Satisfação ponta-a-ponta PARCIAL enquanto (a) pendente (Bloco B); NÃO redefine o CEM (CC-02/INV-10);
    não existe `lineage_ref` no CEM-001; `gate_record`/identidade autenticada são da SPEC-004 v1.2
  - canon/CHM-001 (BASELINE) — estados da hipótese (EMERGENT→…→ARCHIVED), `previous_version_id` (l.283; obrigatório
    em toda nova versão — l.588), `producer_type`/`producer_id` (l.361); o KG relaciona por referência; NÃO transiciona.
    **Preservar TODOS os estados de hipótese NÃO é obrigação herdada** (CEM-001 l.494 é da Evidência): extensão LOCAL
    [PROPOSTA] (N10; conflito na nota de BASpec-CKG-010)
  - canon/CCM-001 (BASELINE) — objeto Conviction Vector 8D; `previous_version_id`, `status` (l.58); o nó `conviction`
    só REFERENCIA o objeto (payload fechado — D4.12); a "confiança de relação" do KG NUNCA é o Conviction Vector (INV-04)
  - specs/features/SPEC-004 v1.2 (BASELINE — DHR-SPEC004-003) — memória de TRABALHO; append-only REAL (INV-CBP-01;
    plan l.230-234/l.371); publicação atômica tudo-ou-nada (plan l.381/l.689); proveniência (RULE-CBP-007/014).
    FRONTEIRA ("Nunca misturar"): HERDA a mecânica e a identidade autenticada por referência; NÃO redefine (CC-02/INV-09)
  - specs/features/SPEC-005 v1.0 (BASELINE — DHR-SPEC005-002) — TRANSPORTA `Evidence.Invalidated` (canônico — CEM-001
    l.600/l.722; plan l.88/l.859) e NÃO escreve no KG (plan l.242/l.971). **[INFERÊNCIA]** consumo pelo KG só como
    GATILHO de avaliação autorizada (CEM-001 l.602); consumidor e EMISSÃO pelo KG = [DECISÃO NECESSÁRIA]
  - canon/CEE-001 (BASELINE) l.111 — a métrica de calibração "entra no Knowledge Graph"; o KG prevê `calibration_metric`,
    ISOLADO da convicção (D4.12); o CAMINHO DE ENTRADA é [DECISÃO NECESSÁRIA] (§D2.3) ⇒ evidência PARCIAL (Bloco B)
  - canon/SAS-001 §6.12 (l.923-924) — o agente atua EXCLUSIVAMENTE como PRODUTOR; registra relações; NÃO redefine
    ontologias nem taxonomias globais → governança de escrita (CKG-009); contrato do caminho (c) = [DECISÃO NECESSÁRIA].
    (l.163 EC-COG-003: KG "consultado quando necessário… não é pré-requisito obrigatório")
  - governance/CONSTITUTION.md l.233 (EC-COG-003 — "Knowledge Graph | Memória relacional de padrões"); l.191-192
    (workspaces Observations × Evidence): âncoras constitucionais; conformar-se, não reescrever (INV-09)
  - governance/RULES.md: RULE-BB-004 (append-only — l.324) — REFORÇADO como imutabilidade permanente (INV-07);
    RULE-CAU-01/02/03 (l.681-683); RULE-INQ-03 (l.678 — fonte do bounded loop) — incidem sobre CAUSA (CKG-008)
  - Método: atomic-spec.md v1.5 (BASpec, D0–D9, EARS, Enforcement E0–E3 — §10.2 "KG publicado → E3 mínimo" l.238,
    TRACE-06, L1–L4 §7, Classe/Mecanismo §10.6 l.315, RULE-MM; §3 emenda SPEC006-MATRIZ → CRITICAL · D0–D7)
  - SPEC-019 v1.0 (RULE-HG/HV; **[INFERÊNCIA]** alteração da ONTOLOGIA = ato análogo — a SPEC-019 não cita "ontologia";
    runtime = K-001 [DECISÃO NECESSÁRIA]); SPEC-020 v1.0 (9 lentes); SPEC-021 v1.0 (RULE-MM; L3; gate E3)
  - Enforcement: ENF-01..08 (ênfase ENF-03 Detector≠Gate; ENF-04 fail-closed; ENF-07 falso-DENY no E3)
  - Invariantes: INV-04 (**custo** nunca no Conviction Vector; atomic-spec l.404/AGENTS §6.8 — a extensão à
    **confiança** é LOCAL [PROPOSTA], CKG-007), INV-05, INV-06, INV-07, INV-09, INV-10
  - Setup operacional (fronteira soberana, NÃO redefinida): WORKFLOW.md — o KG é a memória de longo prazo consultada
    na formação de contexto; cita por ID os WF-xx que toque, NÃO contradiz nenhum WF-xx e NÃO fecha WF-D03

ADDED (delta local — NÃO coberto pelos canônicos/SPEC-004/005 — ver "Cobertura × lacuna"):
  - Ontologia ENXUTA (DENTRO da SPEC-006 — Q-ABERTURA-4) + MATRIZ de integridade (§D2.1); catálogo de ENTIDADES por
    referência (inclui `observation` — INV-06) e de RELAÇÕES tipadas (CONFIRMA … ESTATISTICA_DE, inclusive DERIVA_DE)
  - TEMPORALIDADE BITEMPORAL (D4.6); PROVENIÊNCIA condicional com discriminantes fixos (D4.2)
  - IMUTABILIDADE append-only (conhecimento e log); estado = PROJEÇÃO (D4.7); envelope único + admissão atômica (D4.3/D4.18)
  - CONFIANÇA de relação ≠ Convicção (guard D4.12); SIMILARIDADE/CAUSALIDADE com gate + bounded loop (D4.10/D4.11)
  - GOVERNANÇA de escrita (E3) e da ONTOLOGIA; FRONTEIRA de entrada (§D2.3; pendente = FAIL-CLOSED)
  - CONSULTA read-only + Cognitive Trace Reconstruction COMPLETA (D4.8); LIFECYCLE; COLISÃO (D4.13)
  - Classe/Mecanismo por BASpec (CC-11); EC-CKG-001..006
  - [PROPOSTA de recorte] contrato cognitivo FECHÁVEL com mecanismo físico INDETERMINADO — NÃO fecha H-001
  - [PROPOSTA] extensão de "todos os estados/versões" a hipótese/convicção (não herdada — N10)

MODIFIED (especialização de regra herdada):
  - RULE-BB-004 (append-only do Blackboard) REFORÇADA, não alterada, como imutabilidade PERMANENTE do KG (INV-07) —
    texto/significado inalterados (RULE-HD-02 respeitada)

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **horizontal / obrigação-a-
> obrigação** (EUA-E04 §8.3). O eixo **VERTICAL** (RULE-HV) foi avaliado e **não se aplica**: a SPEC-006 deriva de
> canônicos, Specs vizinhas e regras, não é decomposição *micro* de uma *macro-spec*. [INFERÊNCIA — a confirmar pelo Revisor]

### Cobertura × lacuna (canônicos / SPEC-004 / SPEC-005) — não duplicar (CC-02/INV-09)

| Capacidade | Coberta por canônico/Spec BASELINED? (arquivo:linha) | Tratamento na SPEC-006 |
|---|---|---|
| Preservar linhagem/versões/**todos os estados** da Evidência; Cognitive Trace Reconstruction completa | **SIM (responsabilidade atribuída)** — CEM-001 l.494/608-615; l.562-565 | **ESPECIFICAR** como comportamento verificável (CKG-011/004/012); referencia CEM, não redefine |
| Máquina de estados da hipótese | **SIM** — CHM-001 | **HERDADA** — o KG armazena por referência; não transiciona; preservação no KG = [PROPOSTA] local |
| Append-only REAL; publicação atômica | **SIM** — SPEC-004 v1.2 (INV-CBP-01; plan l.230-234/l.371/l.381/l.689) | **HERDADA a mecânica** e aplicada ao KG permanente (CKG-004/006/012; D4.18) |
| Memória de TRABALHO / objetos ACTIVE | **SIM** — SPEC-004 v1.2 | **FRONTEIRA** — não reabrir (CC-02/INV-09) |
| Notificação/transporte de mudança | **SIM** — SPEC-005 v1.0 | **FRONTEIRA** — consumo/emissão pelo KG = [DECISÃO NECESSÁRIA] |
| Proveniência (`Lineage`, `Evidence Origin Type`, `Producer*`; `gate_record`/`derived_from[]`) | **SIM** — CEM-001 l.271-283/351-355; CHM-001 l.361; SPEC-004 v1.2 | **REFERÊNCIA obrigatória** (CKG-005; D4.2); campos locais [PROPOSTA] espelham, não redefinem |
| **Ontologia + matriz de integridade** | **NÃO** | **LACUNA CENTRAL — ADDED** (CKG-001) |
| **Catálogo de entidades e relações tipadas** | **NÃO** | **LACUNA CENTRAL — ADDED** (CKG-002/003) |
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
> **Termo 5:** "PRIMARY" tem duas acepções no KG: `hierarchy_role=PRIMARY` (hipótese primária — SPEC-001) ≠
> `evidence_origin_type=PRIMARY` (evidência sem ancestral — CEM-001 l.282). O contexto de campo é sempre explícito.
> [FONTE: RULE-SEM-01/04; INV-04/06/07; GLOSSARIO; KERNEL-V2 (research.md §0); SPEC-001; CEM-001 l.280-283; SPEC-004/005/007]

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

A SPEC-006 especifica **como o SOT preserva, relaciona e consulta o conhecimento permanente já validado** — o **contrato
cognitivo da memória semântica permanente** (ontologia + matriz, entidades e relações tipadas, temporalidade bitemporal,
proveniência por referência, imutabilidade append-only, confiança de relação ≠ Convicção, governança de escrita E3,
fronteira de entrada, consulta e **Cognitive Trace Reconstruction COMPLETA** — CEM-001 l.608-615) — preservando **memória
permanente ≠ trabalho** e deixando o **mecanismo físico INDETERMINADO (H-001 ABERTA)**: define-se **o QUE**, não **o COMO**.
[FONTE: ROADMAP §6; CEM-001 l.608-615; CHM-001; SAS-001 §6.12; DHR-SPEC006-001; research.md §4]

**O que a Missão NÃO é (fronteira):**
- Não é **memória de trabalho** → **SPEC-004 (BASELINE)**. *"Nunca misturar."*
- Não **transporta/notifica** mudança → **SPEC-005 (BASELINE)**; consumo/emissão pelo KG = [DECISÃO NECESSÁRIA].
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
| S2 | **Entidades (nós) por referência aos canônicos:** hypothesis (CHM-001), evidence (CEM-001), **observation** (Skill — INV-06), conviction (CCM-001), narrative, mission, learning, asset, timeframe, regime, structure, calibration_metric (CEE-001 l.111). Nós de **construção teórica** (structure/regime/narrative) carregam `ontological_status` ∈ {observational, theoretical} (RULE-ONT-01) | CEM-001; CHM-001; CCM-001; CEE-001 l.111; INV-06; RULE-ONT-01 (RULES.md l.672) |
| S3 | **Relações tipadas:** CONFIRMA/REFUTA/DEPENDE_DE/HERDA/PERTENCE_A/INVALIDA/ORIGINA/**DERIVA_DE**/SIMILAR_A/CAUSA/HIERARQUIA_DE/ESTATISTICA_DE | ROADMAP §6; research.md §4; CEM-001 Cap.5 (Lineage→DERIVA_DE) |
| S4 | **Temporalidade bitemporal:** `valid_from`/`valid_to` (validade) + `recorded_at` (registro); invalidar por novo registro ≠ deletar | research.md §3.1; INV-07; SPEC-004 INV-CBP-01 |
| S5 | **Proveniência obrigatória** (D4.2); rejeita escrita sem proveniência exigível | CEM-001 Cap.5; SPEC-004 v1.2; research.md §3.2 |
| S6 | **Imutabilidade / append-only permanente:** estado = projeção derivada; "esquecimento" = arquivamento versionado | INV-07; RULE-BB-004; SPEC-004 INV-CBP-01; research.md §3.6 |
| S7 | **Confiança de relação** — escala própria, ≠ Convicção; nunca retroalimenta o Conviction Vector | INV-04; research.md §4 |
| S8 | **Relações de similaridade/causalidade** com juízo + gate de saída (RULE-CAU-01/02/03) | RULE-CAU-01/02/03; research.md §8 |
| S9 | **Governança de escrita (E3) + da ontologia:** quem escreve, identidade autenticada (reusa SPEC-004); produtor não redefine ontologia; ontologia governada spec-time (SPEC-019)/runtime (K-001 [DECISÃO NECESSÁRIA]) | SAS-001 §6.12; SPEC-004 v1.2; SPEC-019; atomic-spec §10.2 |
| S10 | **Fronteira de entrada (uma governança; tabela §D2.3)** — todo caminho [DECISÃO NECESSÁRIA] e fail-closed enquanto pendente | ROADMAP §6/§7; CEM-001 l.494; SAS-001 l.924; research.md §3.4 |
| S11 | **Consulta cognitiva (read-only)** + Cognitive Trace Reconstruction **completa** (obrigação) | CEM-001 l.608-615; SAS-001 §6.12; research.md §3.4 |
| S12 | **Lifecycle do nó/relação:** estado derivado; SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED distinguidos; correção/reativação; nunca remoção | CHM-001; INV-07; SPEC-004 INV-CBP-01; research.md §3.6 |
| S13 | **Detecção/registro de colisão de relações:** contraditórias registradas e versionadas, não resolvidas em silêncio | research.md §8; D8 |
| S14 | **Conhecimento permanente × temporário (ROADMAP §6):** "temporário" = conhecimento com janela de validade (`valid_to`) ou `relevance` rebaixada (arquivado) — nunca deletado. O **critério de promoção trabalho→permanente** NÃO é fechado aqui; **atribuí-lo à SPEC-018/K-001 é PROPOSTA submetida a Andraus = [DECISÃO NECESSÁRIA]** (a ABERTURA só enviou à SPEC-018 o ciclo P12) | ROADMAP §6; ABERTURA §35; research.md §4 (lacuna); K-001 (ABERTA) |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| **Mecanismo físico de armazenamento** | **H-001 (ABERTA — só Andraus)** | decisão de engenharia deliberadamente aberta; INDETERMINADO |
| Memória de trabalho / objetos ACTIVE | **SPEC-004 (BASELINE)** | "Nunca misturar"; CC-02/INV-09 |
| Notificação/transporte; **emissão de evento pelo KG** | **SPEC-005 (BASELINE)** | emissão pelo KG = [DECISÃO NECESSÁRIA] (SPEC-005 fonta do log do Blackboard) |
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
> Andraus + registro do Controlador (RULE-HG-02). As RULE/INV/ENF citadas como fundamento **já existem** e são FATO
> NORMATIVO. **Cada RULE enuncia a obrigação; predicado e código de rejeição estão na seção D4 indicada (fonte única).**

```
RULE-CKG-001: Todo nó e toda relação escritos no KG DEVEM pertencer à ONTOLOGIA permitida (tipo ∈ catálogo) e satisfazer
              a MATRIZ DE INTEGRIDADE (§D2.1) e as regras de nó (D4.14). Violação é REJEITADA (fail-closed), não escrita.
              A ontologia é ENXUTA e vive DENTRO da SPEC-006. Predicado: D4.1/D4.14.
              [Fonte: KERNEL-V2 l.1488-1507 (research.md §0/§3.6); DHR-SPEC006-001 Q-ABERTURA-4]  [PROPOSTA]

RULE-CKG-002: Toda ENTIDADE que corresponde a um objeto canônico (hypothesis/CHM-001, evidence/CEM-001, conviction/
              CCM-001) DEVE referenciá-lo por ID+versão — NUNCA redefinir contrato, campos ou máquina de estados
              (CC-02/INV-10); elos de versão e legalidade de transição: D4.16. Um nó `observation` (INV-06) NÃO pode ser
              rotulado `evidence`.
              [Fonte: CEM-001; CHM-001; CCM-001; CC-02; INV-06; INV-10]  [PROPOSTA]

RULE-CKG-003: Toda RELAÇÃO DEVE ser tipada, armazenada DIRECIONADA (origem→destino) e carregar proveniência (RULE-CKG-005).
              A simetria (ex.: SIMILAR_A) é propriedade SEMÂNTICA da consulta (A~B ⇔ B~A), não ausência de direção.
              Relações contraditórias NÃO são resolvidas em silêncio (RULE-CKG-013).
              [Fonte: ROADMAP §6; research.md §4/§8; INV-07]  [PROPOSTA]

RULE-CKG-004: A mudança de validade de nó/relação é ATO AUTORIZADO (CKG-009), NUNCA automática/em cascata (CEM-001 l.602;
              impacto é de CHM/CCM/CDM — CEM-001 l.503/606; CHM-001 l.672-676). NÃO MUTA o registro existente: grava NOVO
              registro `invalidation`. Bitemporal: valid-time ("válida em T") × transaction-time ("conforme registrado em
              R"); a invalidação pode ser retroativa em valid-time. Predicado: D4.6. Invalidar ≠ deletar (INV-07).
              [Fonte: research.md §3.1; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.503; CHM-001 l.672-676]  [PROPOSTA]

RULE-CKG-005: Nenhuma entidade/relação existe sem PROVENIÊNCIA EXIGÍVEL, espelhando a condicionalidade de SPEC-004
              RULE-CBP-007 (sem regra mais forte): `computed_by` autenticado SEMPRE; `gate_record` sse o objeto RESULTA de
              gate; `lineage` não-vazio sse evidência DERIVED. Os discriminantes são CAMPOS FIXOS (v1.6 — N2):
              `provenance_ref.produced_by_gate` (booleano explícito) e `evidence_origin_type` (espelho de CEM-001
              l.280-283). Os gates de ADMISSÃO do KG não produzem o objeto e não geram `gate_record` (decisões →
              `kg_gate_decision`, D4.5). Predicado e códigos: D4.2. Não fabricar proveniência (RULE-MET-01).
              [Fonte: CEM-001 l.280-283/l.351-355; SPEC-004 RULE-CBP-007/014; research.md §3.2]  [PROPOSTA]

RULE-CKG-006: O KG é APPEND-ONLY PERMANENTE (INV-07; reforça RULE-BB-004; espelha SPEC-004 INV-CBP-01): nenhum registro é
              DELETADO nem MUTADO — inclusive os do log `kg_gate_decision` (v1.6 — N4). "Esquecimento" = arquivamento
              versionado (CKG-012). TODO registro de conhecimento usa o envelope único `kg_record` e satisfaz D4.3
              (`envelope_completo`) e D4.4 (versão/sucessão); senão é REJEITADO. A admissão é UNIDADE ATÔMICA tudo-ou-nada
              (D4.18). **Limite declarado (m3):** sem digest/hash encadeado — a detecção física de mutação in-place é
              H-001/BUILD; esta RULE proíbe a mutação, não a detecta fisicamente.
              [Fonte: INV-07; RULE-BB-004 (RULES.md l.324); SPEC-004 INV-CBP-01, plan l.381/l.689; research.md §3.6]  [PROPOSTA]

RULE-CKG-007: A CONFIANÇA de relação é escala PRÓPRIA do KG e NÃO É a Convicção (CCM-001). **Guard de custo E confiança =
              D4.12 (texto único — v1.6, N8):** payload de nó `conviction` FECHADO; nenhuma relação
              `calibration_metric`→`conviction`; `relation_confidence` só no payload de relação. INV-04 (atomic-spec
              l.404) proíbe CUSTO no Conviction Vector; a extensão à CONFIANÇA é LOCAL [PROPOSTA]. Que o cálculo de
              convicção (SPEC-003) não a consuma é requisito endereçado à SPEC-003 / [DECISÃO NECESSÁRIA]. Escala de
              confiança = PARÂMETRO a calibrar (INDETERMINADO; não toca J-001/N-001, abertas).
              [Fonte: INV-04 (custo); CCM-001; CEE-001 l.111; RULE-MET-01]  [PROPOSTA]

RULE-CKG-008: Toda relação CAUSA DEVE declarar mecanismo, direção e condições (RULE-CAU-01), regime (RULE-CAU-02) e
              `posthoc_flag` com valor EXPLÍCITO true/false (RULE-CAU-03; v1.6 — N7); SIMILAR_A DEVE declarar
              `similarity_basis`, mesmo node_type e from≠to. Escopo: TODA CAUSA/SIMILAR_A, qualquer produtor/caminho.
              O gate verifica PRESENÇA, não veracidade (ENF-03; limite m5). Proposta de JUÍZO (Classe H): BOUNDED LOOP de
              ≤1 invocação POR SUBMISSÃO, KG sem retry; reprovada ⇒ INDETERMINADO; limite versionado com esta RULE.
              Predicados: D4.10/D4.11. [Fonte: RULE-CAU-01/02/03 (RULES.md l.681-683); RULE-INQ-03 (l.678); atomic-spec
              §10.6 l.315; SPEC-002 l.370-371 / SPEC-003 l.387-388]  [PROPOSTA]

RULE-CKG-009: A escrita no KG permanente é GOVERNADA e E3 (atomic-spec §10.2 "KG publicado → E3 mínimo"), fail-closed: só
              ESCRITORES AUTORIZADOS (allowlist) com identidade AUTENTICADA pelo runtime (reusa SPEC-004 CBP-014); falha
              de autenticação ⇒ NÃO-AUTORIZADO. O produtor registra relações mas NÃO redefine ONTOLOGIA/TAXONOMIAS
              (SAS-001 §6.12). Alteração da ontologia = ato de GOVERNANÇA (spec-time [INFERÊNCIA] RULE-HG; runtime K-001),
              prospectiva e backward-compatible (INV-07). Migração de `schema_version`, mantenedor da allowlist e host do
              juízo = [DECISÃO NECESSÁRIA]; **allowlist indefinida ⇒ toda escrita DENY `WRITER_ALLOWLIST_UNDEFINED`**.
              [Fonte: SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; SPEC-019 RULE-HG; ENF-03/04]  [PROPOSTA]

RULE-CKG-010: Todo nó/relação entra por UM caminho da tabela §D2.3 (fonte única), sob a governança de CKG-009: (a) objetos
              canônicos e suas transições via ciclo de vida; (b) conhecimento formado via selo SPEC-007; (c) relações
              registradas por produtor (SAS-001 l.924). O KG NÃO forma/extrai/recupera. Pendência = precondição NÃO
              satisfeita = DENY (ENF-04) em todo caminho; nada persistido (D4.15). **Preservação (v1.6 — N10):** para a
              EVIDÊNCIA, "todos os estados/todas as versões" é obrigação herdada (CEM-001 l.494/l.612); estendê-la a
              hipótese/convicção é [PROPOSTA] LOCAL e CONFLITA com a [PROPOSTA] de critério mínimo de (a) que exclui
              EMERGENT/CANDIDATE — [DECISÃO NECESSÁRIA] (nota após BASpec-CKG-010).
              [Fonte: ROADMAP §6/§7; CEM-001 l.494/l.612; SAS-001 l.924; ENF-04; research.md §3.4]  [PROPOSTA]

RULE-CKG-011: O KG DEVE oferecer CONSULTA cognitiva read-only (padrão/similaridade/causalidade/histórico/multi-salto) e a
              Cognitive Trace Reconstruction COMPLETA pelas relações DERIVA_DE (D4.8). A COMPLETUDE é OBRIGAÇÃO (não
              rebaixada por H-001); só a EFICIÊNCIA de consultas multi-salto AMPLAS fica INDETERMINADA até H-001. A
              consulta é opcional/não-bloqueante (SAS-001 §6.12/EC-COG-003) e NÃO altera estado.
              [Fonte: CEM-001 l.608-615/l.612-614; SAS-001 §6.12/l.163; research.md §3.4]  [PROPOSTA]

RULE-CKG-012: O estado de um nó/relação (ACTIVE_KNOWLEDGE / SUPERSEDED / INVALIDATED_IN_TIME / ARCHIVED) é PROJEÇÃO
              DERIVADA dos registros (D4.7): SUPERSEDED = sucessora de CONTEÚDO; INVALIDATED_IN_TIME = validade terminada
              SEM sucessora (o MUNDO mudou); ARCHIVED = rebaixamento de `relevance` sob gate E3. Correção/reativação = NOVO
              registro; nenhuma transição remove registro (INV-07).
              [Fonte: CHM-001; INV-07; SPEC-004 INV-CBP-01; research.md §3.6]  [PROPOSTA]

RULE-CKG-013: Colisão ocorre sse `colide(r1,r2)` (D4.13): par contraditório da §D2.2 ∧ mesmos `from_node`/`to_node` ∧
              sobreposição das janelas EFETIVAS de validade. O KG DETECTA e REGISTRA (`record_kind=collision`, envelope
              único, ambas preservadas) na MESMA unidade atômica da admissão (D4.18); NUNCA sobrescreve/apaga em
              silêncio. A RESOLUÇÃO é de SPEC-007/SPEC-018 ou governança — o KG não decide.
              [Fonte: INV-07; §D2.2; research.md §8; fronteira SPEC-007/SPEC-018]  [PROPOSTA]
```

### D2.1 — Matriz de integridade da ontologia (RULE-CKG-001) [PROPOSTA]

> **Atributo de escola (ADDED — UM campo único: `school`):**
> - **Origem:** `school` **NÃO é campo canônico**; a proveniência canônica é `producer_type`/`producer_id` (CHM-001 §2.9
>   l.361; CEM-001 l.271-278), que o payload ESPELHA (v1.6 — N3; schema). `school` é campo **LOCAL [PROPOSTA]**,
>   **DERIVADO deterministicamente** do `producer_id` por tabela de mapeamento [PROPOSTA] (D4.14): Elliott Specialist →
>   Elliott (`producer_id == "elliott_specialist"`, SPEC-001 l.203); SMC Specialist → SMC; Fibonacci Validator →
>   Fibonacci; ICT Specialist → ICT (nomes: AGENTS.md §3.2; `producer_id` exatos dos três últimos são fixados nas Specs
>   dos especialistas — não inventados aqui). **Efeito hoje:** só o do Elliott é conhecido ⇒ hypothesis/structure de
>   SMC, Fibonacci, ICT e Fractal caem em `SCHOOL_UNDERIVABLE` até essas Specs fixarem o `producer_id` [DECISÃO NECESSÁRIA].
> - **Limite (N3):** o KG verifica o `producer_id` DECLARADO no registro; não faz lookup ao objeto canônico (fora do KG).
>   O espelho de INV-02 é, portanto, de **FORMA**; a coincidência `producer_id`↔canônico é precondição do contrato de (a)
>   — [DECISÃO NECESSÁRIA].
> - **Enumeração:** `school` ∈ {Elliott, Fibonacci, Fractal, SMC, ICT} (5 camadas — CC-01/INV-01); **Fractal** sem
>   produtor listado (AGENTS.md §3.2; CONSTITUTION l.237) ⇒ mapeamento →Fractal = **[DECISÃO NECESSÁRIA]**. `school` ≠
>   `Domain` do CEM-001 (l.290-301; CC-10). Para `hypothesis`, `hierarchy_role` ∈ {PRIMARY, SUB} (SPEC-001 l.87/l.844).
> O KG **espelha**, NÃO decide, a autoridade de criação (CC-01; Elliott cria PRIMARY; ICT não cria — INV-02/RULE-HH-004).
> Regras de nó: D4.14. "**Família estrutural**" é COMPUTADA (não é campo): nós de **mesma `school`** que `PERTENCE_A` o
> **mesmo par (asset, timeframe)** — restringe **só** herança fractal INTRA-escola; a herança sub→pai ENTRE escolas
> (SMC/Fibonacci SUB → Elliott PRIMARY) é NORMAL (SPEC-001 RULE-HH-003 l.104; CHM-001 `parent_hypothesis_id` l.165/415;
> CONSTITUTION l.193).

| Relação | Origem (node_type) | Destino | Direcional | Simétrica (consulta) |
|---|---|---|---|---|
| CONFIRMA | **evidence** (NÃO observation — INV-06; workspaces distintos, CONSTITUTION l.191-192; restrição [PROPOSTA] derivada de INV-06) | hypothesis | sim | não |
| REFUTA | **evidence** (NÃO observation) | hypothesis | sim | não |
| DEPENDE_DE | hypothesis, mission | hypothesis, evidence | sim | não |
| HERDA | hypothesis (`hierarchy_role=SUB`) | hypothesis (**PAI = `hierarchy_role=PRIMARY`** — RULE-HH-003) via `parent_id`/`parent_hypothesis_id`; **entre escolas é permitido** | sim | não |
| PERTENCE_A | hypothesis, evidence, structure, observation | asset, timeframe, regime, mission | sim | não |
| INVALIDA | evidence, learning | nó `evidence` (`to_node`) **ou** relação-alvo por `target_relation_id` (com `to_node = null`) — "relação" NÃO é node_type (v1.6 — n3) | sim | não — AFIRMAÇÃO de conhecimento sobre o alvo; NÃO altera a validade do alvo (só registro `invalidation` autorizado — CKG-004) e NÃO é par de colisão (§D2.2) |
| ORIGINA | structure/hypothesis com `school` ≠ ICT — **nunca ICT** (INV-02/RULE-HH-004) | hypothesis | sim | não |
| DERIVA_DE | evidence com `evidence_origin_type=DERIVED` | evidence (ancestral) | sim | não — **aresta de Lineage**; base do trace (D4.8); obrigatória por ancestral (INV-CKG-02) |
| SIMILAR_A | qualquer | mesmo node_type (≠ o próprio nó) | sim (armazenada) | **sim** — exige `similarity_basis` (D4.10); duplicata em direção inversa = no-op |
| CAUSA | qualquer node_type | qualquer | sim | não — campos D4.10 |
| HIERARQUIA_DE | structure, timeframe | structure, timeframe | sim | não |
| ESTATISTICA_DE | learning | hypothesis, structure, asset | sim | não |

> **Restrição transversal (guard D4.12):** NENHUMA relação, de qualquer tipo, de `calibration_metric` para `conviction`.
> **DERIVA_DE × proveniência:** `DERIVA_DE` é RELAÇÃO navegável (aresta de Lineage; ordem de saída do trace = dos
> ancestrais primários aos derivados — CEM-001 l.567-577); `provenance_ref.lineage` é CAMPO de proveniência do registro
> (referencia `Lineage`/`derived_from[]`), não aresta. Coexistem.

> **Invariante local [PROPOSTA] — INV-CKG-01 (Memória permanente imutável):** nenhum registro do KG — de conhecimento
> (`kg_record`) ou de decisão (`kg_gate_decision`) — é deletado ou mutado; estado = projeção derivada; "esquecimento" =
> arquivamento versionado; toda entidade/relação carrega proveniência e é reconstruível; todo registro de conhecimento,
> inclusive os especiais, usa o envelope único `kg_record`. Reforça — não redefine — RULE-BB-004, INV-07 e SPEC-004
> INV-CBP-01, no eixo permanente. [PROPOSTA]

> **Invariante local [PROPOSTA] — INV-CKG-02 (Completude e aciclicidade da linhagem):** admitir `evidence` com
> `evidence_origin_type=DERIVED` EXIGE uma aresta `DERIVA_DE` para CADA ancestral do seu `Lineage` (CEM-001 l.355/565),
> com todos os ancestrais JÁ no KG (D4.17 — sem estado de espera; ancestral ausente ⇒ `ANCESTOR_NOT_ADMITTED`); o grafo
> de `DERIVA_DE` é ACÍCLICO; o trace ignora o filtro de validade (CEM-001 l.602). Garante a completude de CEM-001
> l.612-614, independente de H-001. Sem deadlock [INFERÊNCIA]: o `Lineage` lista antecedentes imediatos e é imutável
> após publicação (CEM-001 l.530/560). Hoje inalcançável fim a fim ((a) pendente) — verificado por predicado (T19). [PROPOSTA]

### D2.2 — Tabela de contradição e escopo de colisão (RULE-CKG-013) [PROPOSTA]

> **Colisão** = `colide(r1,r2)` (D4.13 — fonte única): (1) par de `relation_type` desta tabela; (2) mesmos `from_node` e
> `to_node`; (3) **sobreposição das janelas EFETIVAS** `[valid_from, valid_to_efetivo)` (D4.6 — o `valid_to` bruto é nulo
> na criação; v1.6 — N11). Fora disso NÃO há colisão (ADV-18).

| Tipo A | Tipo B (contradiz A) | Simétrico? | Observação |
|---|---|---|---|
| CONFIRMA | REFUTA | **sim** (A↔B) | mesma hipótese-alvo afirmada e negada ao mesmo tempo |

> Pares NÃO listados **não** são contradição estrutural. **NÃO colidem:** (a) `from_node` diferentes; (b) janelas efetivas
> disjuntas (ex.: CONFIRMA invalidada em T1 por registro `invalidation` efetivo e REFUTA com `valid_from` ≥ T1);
> (c) INVALIDA × relação-alvo (INVALIDA mira por `target_relation_id`; é afirmação sobre o alvo — ADV-18 d). A
> **resolução** é de SPEC-007/SPEC-018 ou governança. Tabela ENXUTA e extensível por governança (RULE-ONT-02).

### D2.3 — Caminhos de entrada (fonte ÚNICA; RULE-CKG-010/009) [PROPOSTA]

| Objeto submetido | Caminho | Pendência ([DECISÃO NECESSÁRIA]) | DENY hoje |
|---|---|---|---|
| nó hypothesis/evidence/conviction + `canonical_state_transition` | (a) ciclo de vida canônico | critério/produtor/gatilho de (a); coincidência `producer_id`↔canônico | `PATH_A_ADMISSION_PENDING` |
| relações ESPELHADAS de campo canônico: DERIVA_DE (`Lineage`), HERDA (`parent_id`/`parent_hypothesis_id`) | (a) — materializadas na admissão do nó (D4.18) | idem (a) | `PATH_A_ADMISSION_PENDING` |
| nó learning; padrões/relações generalizadas FORMADOS | (b) selo SPEC-007 | contrato do selo (SPEC-007) | `SEAL_MISSING` (sem selo) / `SEAL_CONTRACT_UNDEFINED` |
| relações registradas por PRODUTOR (SAS-001 l.924) e toda relação sem campo canônico de origem (CONFIRMA, REFUTA, DEPENDE_DE, PERTENCE_A, INVALIDA, ORIGINA, SIMILAR_A, CAUSA, HIERARQUIA_DE, ESTATISTICA_DE) fora de (b) | (c) registro por produtor | contrato de (c) | `ENTRY_PATH_UNDEFINED` |
| proposta de CAUSA/SIMILAR_A originada no JUÍZO do próprio KG (CKG-008) | — | host do juízo | `ENTRY_PATH_UNDEFINED`; o KG faz 0 invocações de juízo enquanto o host estiver pendente (n9) |
| nós asset/timeframe/regime/observation/calibration_metric/structure/narrative/mission | sem caminho | caminho inteiro | `ENTRY_PATH_UNDEFINED` |
| registros internos: `invalidation`/`archival` | ato AUTORIZADO (CKG-004/009/012) sobre sujeito JÁ admitido; `writer_id` = escritor autorizado do ato | — (inalcançáveis enquanto nada é admitido) | — |
| registro interno `collision` | detector (D4.13) dentro da unidade atômica da admissão que o disparou (D4.18); `writer_id` = identidade de serviço do KG, `publication.origin=kg_internal`; herda a autorização dessa admissão (n4) | — | — |
| `kg_gate_decision` (log de decisão, não conhecimento) | runtime dos gates (identidade de serviço; host = H-001/BUILD); gravado em QUALQUER resultado, inclusive DENY — por isso fora da allowlist de conhecimento; imutável (CKG-006) | — | — (nunca negado) |
| qualquer escrita de conhecimento | allowlist de escritores (CKG-009) | mantenedor da allowlist | `WRITER_ALLOWLIST_UNDEFINED` |

> **Consequência declarada:** hoje o KG **não admite nenhuma escrita de conhecimento**. O verificável é o PREDICADO de cada
> gate sobre entradas e fixtures (convenção D7); a admissão positiva fim a fim é **INDETERMINADO** até as decisões acima.
> Nenhum gate é chamado "verificável" quando depende de contrato indefinido.

---

## Critérios de Aceitação (EARS)

1. Quando um nó ou relação é submetido para escrita, o KG DEVE escrevê-lo somente se o tipo pertence à ontologia e satisfaz a matriz de integridade e as regras de nó (D4.1/D4.14), e DEVE rejeitar (fail-closed) violação de tipo/integridade, sem escrever.
2. Quando um nó corresponde a um objeto canônico, o KG DEVE referenciá-lo por ID+versão e NÃO DEVE redefinir seu contrato/campos/estados; um nó `observation` NÃO DEVE ser rotulado `evidence`.
3. Quando uma relação é escrita, o KG DEVE exigir tipo, direção e proveniência, e NÃO DEVE aceitar relação sem proveniência; a simetria de SIMILAR_A é semântica de consulta, não ausência de direção.
4. Quando a validade de uma relação muda, o KG DEVE gravar um NOVO registro de invalidação e manter o histórico, e NÃO DEVE mutar nem deletar o registro existente.
5. Quando qualquer escrita é tentada, o KG DEVE aplicar o predicado de proveniência D4.2 e rejeitá-la (fail-closed) com o código ali definido se faltar a proveniência exigível ou um discriminante (`produced_by_gate`, `evidence_origin_type`).
6. Quando um "esquecimento"/consolidação é solicitado, o KG DEVE arquivar por novo registro versionado, e NÃO DEVE remover nem mutar registro histórico (de conhecimento ou do log `kg_gate_decision`); todo registro de conhecimento DEVE satisfazer `envelope_completo` (D4.3), e o KG DEVE rejeitar o que não satisfaz.
7. Quando um nó `conviction` ou uma relação com destino `conviction` é submetido, o KG DEVE aplicar o guard de custo e confiança D4.12 e rejeitar a violação sem escrever (que o cálculo de convicção não consuma a confiança é requisito à SPEC-003 / [DECISÃO NECESSÁRIA]).
8. Quando qualquer relação CAUSA ou SIMILAR_A é submetida, de qualquer produtor, o KG DEVE exigir os campos de D4.10 (para CAUSA, inclusive `posthoc_flag` com valor explícito) e rejeitá-la sem eles; quando a proposta vem de juízo, o KG DEVE invocá-lo no máximo uma vez por submissão, NÃO DEVE gerar re-tentativa, e DEVE encerrar a submissão reprovada em INDETERMINADO.
9. Quando uma escrita no KG permanente é tentada, o KG DEVE aceitá-la (E3) apenas de escritor da allowlist com identidade autenticada (falha de auth ⇒ não-autorizado; allowlist indefinida ⇒ rejeitar), e NÃO DEVE permitir que o produtor redefina ontologia/taxonomia.
10. Quando conhecimento formado é submetido sem selo, ou com selo enquanto o contrato do selo estiver pendente, o KG DEVE rejeitá-lo; quando um objeto canônico é submetido pelo caminho (a) enquanto o critério desse caminho estiver pendente de decisão de Andraus, o KG DEVE rejeitá-lo (fail-closed, nada persistido); depois de decidido o critério, uma evidência admitida DEVE ter preservados todos os seus estados e versões (CEM-001 l.494/612).
11. Quando um consumidor consulta o KG, o KG DEVE responder read-only e reconstruir a cadeia cognitiva COMPLETA, e NÃO DEVE alterar estado na consulta.
12. Quando um nó/relação transita (SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED), o KG DEVE representar a transição por novo registro preservando o histórico (estado = projeção D4.7), e NÃO DEVE remover nem mutar a versão anterior.
13. Quando uma relação em admissão e uma relação vigente satisfazem `colide` (D4.13), o KG DEVE gravar o registro `collision` na mesma unidade atômica da admissão (D4.18), preservando ambas, e NÃO DEVE sobrescrever/apagar uma em silêncio nem deixar `collision` gravado se a admissão falhar.
14. Quando um objeto é submetido por caminho cujo contrato está indefinido (tabela §D2.3), o KG DEVE rejeitá-lo com `ENTRY_PATH_UNDEFINED` (ou o motivo do caminho pendente), sem persistir nada.
15. Quando um nó hypothesis/structure é submetido com `producer_id` sem mapeamento para `school`, o KG DEVE rejeitá-lo com `SCHOOL_UNDERIVABLE`, sem persistir nada.
16. Quando uma evidência DERIVED é submetida com algum ancestral do `Lineage` ausente do KG, o KG DEVE rejeitá-la imediatamente com `ANCESTOR_NOT_ADMITTED`, sem estado de espera e sem persistir nada.
17. Quando um nó canônico ou transição canônica é submetido sem o elo de versão exigido por D4.16, ou com elo que não resolve no KG, o KG DEVE rejeitá-lo com `VERSION_LINK_MISSING`, sem persistir nada.
18. Quando uma `canonical_state_transition` de CHM-001/CEM-001 é submetida com par de estados fora do grafo canônico ou `status_from` diferente do status corrente, o KG DEVE rejeitá-la com `CANONICAL_TRANSITION_ILLEGAL`, sem persistir nada.
19. Quando um registro `invalidation` é submetido com `valid_to` anterior ao `valid_from` do alvo, o KG DEVE rejeitá-lo com `VALIDITY_WINDOW_INVALID`, sem persistir nada.
20. Quando um registro é submetido com `version`, `supersedes` ou `recorded_at` em desacordo com D4.4, o KG DEVE rejeitá-lo com `RECORD_VERSION_INVALID`, sem persistir nada.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec com efeito declara **CLASSE/MECANISMO** (§10.6). D = determinístico; C = constitutivo (é o gate); H =
> híbrido (juízo + gate de saída + bounded loop). **A escrita no KG permanente é E3** (atomic-spec §10.2 l.238); consulta
> é E1; o guard D4.12 é **E3** (decide admitir/recusar escrita permanente). O ENTÃO cita o predicado de D4 (fonte única).

### BASpec-CKG-001 — Ontologia enxuta + matriz de integridade (rejeita violação)
```
BASpec-CKG-001:
  QUANDO:       Um nó ou relação é submetido para escrita no KG
  ENTÃO:        O KG escreve somente se D4.1 (tipo ∈ ontologia ∧ matriz §D2.1) e D4.14 (school derivável; hypothesis.school
                ≠ ICT; PRIMARY ⇒ Elliott; HERDA só SUB→PRIMARY) são satisfeitos; violação é rejeitada (fail-closed), não
                escrita. O KG apenas ESPELHA os vínculos já criados pelos agentes; NÃO decide autoridade de criação (CC-01)
  PORQUE:       Sem gramática enxuta + integridade, a memória permanente acumula conhecimento incoerente (research.md §8 R-8)
  REFERÊNCIA:   RULE-CKG-001; D4.1/D4.14; KERNEL-V2 l.1488-1507; CONSTITUTION l.193; INV-02; RULE-HH-002/003/004 (SPEC-001)
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico D4.1 ∧ D4.14
    GATE DE SAÍDA: verificação da matriz §D2.1 + regras de nó D4.14
    CRITÉRIO 4Es: Conformidade > Eficácia — coerência da ontologia é inviolável
  VERIFICADO POR:
    DADO        (= T01) uma relação ORIGINA cuja origem tem `school == ICT` (fixture; INV-02/RULE-HH-004)
    QUANDO      o gate de integridade roda (predicado — convenção D7 (i))
    ENTÃO       escrita rejeitada; nada persistido (regra de nó hypothesis.school ≠ ICT: ADV-17; positivo cross-escola: T15)
    VERIFICAÇÃO written == false; rejected_reason == "ONTOLOGY_INTEGRITY_VIOLATION"
```

### BASpec-CKG-002 — Entidade por referência ao canônico (não redefine; observation≠evidence)
```
BASpec-CKG-002:
  QUANDO:       Um nó corresponde a um objeto canônico (hypothesis/evidence/conviction) ou é uma observation
  ENTÃO:        O KG referencia o canônico por ID+versão, grava `canonical_status` (snapshot — enum POR MODELO, schema) e, a
                cada mudança de Status, um registro `canonical_state_transition` (estado de/para, timestamp, origem,
                justificativa — CEM-001 l.428); cada versão canônica é nó próprio com os elos de versão tipados por modelo e
                legalidade de transição de D4.16; NÃO redefine contrato/campos; só para objeto ADMITIDO ((a) pendente —
                §D2.3); observation (INV-06) NÃO é rotulada evidence. Estados do KG (D5) são HOMÔNIMOS ≠ canônicos (CC-10)
  PORQUE:       Redefinir canônico viola CC-02/CONST-01; o Status é o único campo mutável do canônico (CEM-001 l.264), logo o
                KG precisa de snapshot+transições para preservar estados; Observação≠Evidência (INV-06); idioma canônico (INV-10)
  REFERÊNCIA:   RULE-CKG-002; D4.16; CC-02; CC-10; CEM-001 l.264/428/450/494; CHM-001 l.283/588/744-757; CCM-001 l.58; INV-06; INV-10
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : referência (canonical_id@version) + snapshot canonical_status + registro canonical_state_transition + D4.16
    CRITÉRIO 4Es: Eficácia — integridade referencial + preservação dos estados canônicos admitidos
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
  ENTÃO:        O KG exige tipo (catálogo), direção (origem→destino, armazenada) e proveniência (D4.2); SIMILAR_A é simétrica
                só na consulta; admitir evidence DERIVED materializa uma aresta DERIVA_DE por ancestral (INV-CKG-02; D4.17);
                o grafo DERIVA_DE é acíclico; contradição não é silenciada (CKG-013)
  PORQUE:       Relação não-tipada/sem direção/sem proveniência não é auditável (P13); sem a aresta por ancestral, o trace
                completo (CKG-011/CEM-001 l.612-614) não seria garantido
  REFERÊNCIA:   RULE-CKG-003/005; INV-CKG-02; D4.17; CEM-001 l.565; research.md §4
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : validação determinística (tipo ∈ catálogo ∧ direção presente ∧ D4.2)
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
  QUANDO:       Um ato AUTORIZADO (CKG-009) determina que a validade de uma relação mudou — NUNCA invalidação automática/em
                cascata (CEM-001 l.602; impacto é de CHM/CCM — l.503/606)
  ENTÃO:        O KG grava um NOVO registro `invalidation` (D4.6; janela válida senão `VALIDITY_WINDOW_INVALID`), preservando o
                registro de criação intacto; a validade corrente é projeção; a consulta responde por valid-time e por
                transaction-time (D4.6)
  PORQUE:       Invalidar por novo registro preserva a reconstrução histórica (INV-07); só por ato autorizado respeita
                "invalidação não implica cascata" (CEM-001 l.602)
  REFERÊNCIA:   RULE-CKG-004; RULE-CKG-009; D4.6; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.503
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

### BASpec-CKG-005 — Proveniência obrigatória (rejeita escrita sem proveniência exigível)
```
BASpec-CKG-005:
  QUANDO:       Qualquer nó/relação é escrito no KG
  ENTÃO:        O KG aplica o predicado de proveniência D4.2 (computed_by sempre; gate_record sse produced_by_gate=true;
                lineage não-vazio sse evidence_origin_type=DERIVED; discriminantes explícitos); falta do exigível ⇒
                rejeitada (fail-closed) com o código de D4.2
  PORQUE:       Conhecimento sem ORIGEM AUTENTICADA não é reconstruível (CEM-001 Cap.5; P13); exigir gate_record/lineage de
                quem não tem gate/ancestral fabricaria dado (RULE-MET-01) e contrariaria a condicionalidade da CBP-007
  REFERÊNCIA:   RULE-CKG-005; D4.2; SPEC-004 RULE-CBP-007/014; CEM-001 l.280-283/351-355
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico D4.2
    GATE DE SAÍDA: verificação D4.2
    CRITÉRIO 4Es: Conformidade > Eficácia — identidade autenticada é inviolável; sem fabricar proveniência (RULE-MET-01)
  VERIFICADO POR:
    DADO        (a) nó hypothesis PRIMARY com computed_by presente, produced_by_gate=false, lineage=[] (= T12);
                (b) nó sem computed_by (= T14)
    QUANDO      o gate de proveniência roda (predicado)
    ENTÃO       (a) APROVA (lineage=[] legítimo; gate_record não exigido); (b) REPROVA
    VERIFICAÇÃO case_a_provenance_gate == PASS; case_a_gate_record_required == false; case_a_lineage_empty_ok == true;
                case_b_provenance_gate == FAIL; case_b_reason == "COMPUTED_BY_MISSING"   (persistência: T16)
```

### BASpec-CKG-006 — Imutabilidade / append-only permanente (nunca deletar nem mutar) [INV-CKG-01]
```
BASpec-CKG-006:
  QUANDO:       Uma deleção ou mutação de registro — de conhecimento (`kg_record`) ou do log `kg_gate_decision` — é tentada
                (inclusive disfarçada de "esquecimento")
  ENTÃO:        O KG recusa (fail-closed); "esquecimento"/consolidação só por novo registro de arquivamento versionado
                (CKG-012); a recusa é registrada como nova decisão no log; o registro histórico é preservado (INV-07)
  PORQUE:       A memória permanente nunca apaga nem reescreve — quebraria a reconstrução (P13) e INV-07/RULE-BB-004/
                INV-CBP-01; o log é a EVIDENCE dos EC E3 (ENF-07) — mutá-lo apagaria a prova de conformidade
  REFERÊNCIA:   RULE-CKG-006; D4.3/D4.4/D4.5; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico que proíbe DELETE físico e UPDATE de qualquer registro; só novos registros
    GATE DE SAÍDA: verificação (operação ∉ {DELETE, UPDATE de registro}; histórico preservado)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda/não-reescrita de histórico acima de economia de espaço
  VERIFICADO POR:
    DADO        (a) tentativa de deletar fisicamente (ou reescrever) um registro arquivado; (b) tentativa de UPDATE do campo
                `result` de um `kg_gate_decision` existente
    QUANDO      o gate roda
    ENTÃO       ambas negadas (fail-closed); registros íntegros e reconstruíveis
    VERIFICAÇÃO physical_delete == false; record_mutated == false; gate_decision_mutated == false; history_preserved == true
```

### BASpec-CKG-007 — Confiança de relação é propriedade local do KG, nunca exposta ao objeto de convicção [regra LOCAL [PROPOSTA]; INV-04 (custo) como base]
```
BASpec-CKG-007:
  QUANDO:       Um nó `conviction`, uma relação com destino `conviction` ou uma confiança de relação é submetido ao KG
  ENTÃO:        O KG aplica o guard de custo E confiança D4.12 (payload de conviction fechado; nenhuma relação
                calibration_metric→conviction; relation_confidence só no payload de relação) e rejeita a violação
  PORQUE:       INV-04 (atomic-spec l.404) proíbe CUSTO no Conviction Vector; esta Spec ESTENDE localmente a mesma lógica à
                confiança de relação (regra LOCAL [PROPOSTA], não cláusula de INV-04)
  REFERÊNCIA:   RULE-CKG-007; D4.12; INV-04 (custo); CCM-001
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : guard determinístico D4.12 (por campo/node_type; sem juízo)
    GATE DE SAÍDA: verificação D4.12
    CRITÉRIO 4Es: Conformidade > Eficácia — INV-04 (custo) é inviolável; a extensão à confiança é salvaguarda local
  VERIFICADO POR:
    DADO        (a) relação CAUSA(calibration_metric → conviction); (b) nó conviction com campo além dos permitidos (ex.: confiança)
    QUANDO      o gate de escrita roda
    ENTÃO       (a) rejeitada `ONTOLOGY_INTEGRITY_VIOLATION`; (b) rejeitado `CONFIDENCE_IS_NOT_CONVICTION`
    VERIFICAÇÃO cost_or_confidence_to_conviction_edge == false; confidence_exposed_in_conviction_object == false
```
> **Nota:** o KG controla só a **sua própria escrita**; que o **cálculo de convicção** (SPEC-003/CCM-001; J-001 ABERTA)
> não consuma a confiança é **requisito endereçado à SPEC-003** ([DECISÃO NECESSÁRIA] na integração). [INFERÊNCIA]

### BASpec-CKG-008 — Relação causal exige mecanismo+regime+pós-hoc (RULE-CAU-01/02/03)
```
BASpec-CKG-008:
  QUANDO:       Qualquer relação CAUSA ou SIMILAR_A é submetida (qualquer produtor/caminho)
  ENTÃO:        O KG exige os campos de D4.10 (CAUSA: mechanism, direction, conditions, regime e posthoc_flag explícito;
                SIMILAR_A: similarity_basis, mesmo node_type, from≠to; duplicata inversa vigente = no-op); faltando, rejeita;
                verifica só PRESENÇA (ENF-03); se a proposta vem de juízo, aplica o bounded loop D4.11
  PORQUE:       Correlação não é causalidade (RULE-CAU-01); a relação causal muda entre regimes (RULE-CAU-02); explicação
                pós-resultado é viés se não marcada (RULE-CAU-03); investigação sem encerramento é proibida (RULE-INQ-03)
  REFERÊNCIA:   RULE-CKG-008; D4.10/D4.11; RULE-CAU-01/02/03; RULE-INQ-03 (RULES.md l.678); atomic-spec §10.6 l.315
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : juízo (apoio semântico) PROPÕE; gate de saída determinístico D4.10 verifica presença
    BOUNDED LOOP: D4.11 — ≤1 invocação por submissão; KG sem retry nem nova submissão; reprovada ⇒ INDETERMINADO, nada
                  escrito, decisão em `kg_gate_decision`; host pendente ⇒ 0 invocações (§D2.3). Fonte: atomic-spec l.315;
                  RULE-INQ-03; SPEC-002 l.370-371
    GATE DE SAÍDA: verificação D4.10
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
  ENTÃO:        O KG (E3, fail-closed) aceita apenas de escritor da allowlist com identidade AUTENTICADA pelo runtime (reusa
                SPEC-004); falha de autenticação ⇒ NÃO-AUTORIZADO; allowlist indefinida ⇒ `WRITER_ALLOWLIST_UNDEFINED`; o
                produtor registra relações mas NÃO redefine ontologia/taxonomia (SAS-001 §6.12)
  PORQUE:       Escrita em memória permanente é commit crítico/irreversível (E3 — atomic-spec §10.2); autorização não pode
                depender do payload e não pode falhar-aberto
  REFERÊNCIA:   RULE-CKG-009; SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate E3 de autorização por identidade autenticada + escopo (registrar ≠ redefinir ontologia); LLM não é gate
    GATE DE SAÍDA: verificação (allowlist definida ∧ escritor ∈ allowlist ∧ auth OK ∧ operação ∉ {redefinir ontologia/taxonomia})
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
  ENTÃO:        O KG aplica D4.15 sobre a tabela §D2.3: caminho com contrato pendente ou objeto sem caminho ⇒ DENY com o
                motivo do caminho; formado sem selo ⇒ `SEAL_MISSING`; nada persistido. DEPOIS de decidido (a), admite
                gravando `canonical_status` + `canonical_state_transition` + elos de versão (CKG-002); o KG NÃO faz
                formação/retrieval
  PORQUE:       "Documento recuperado ≠ conhecimento validado ≠ publicado"; formação é SPEC-007; pendência tratada como
                admissão contaminaria a memória permanente (E3 irreversível)
  REFERÊNCIA:   RULE-CKG-010; §D2.3; D4.15; ROADMAP §6/§7; CEM-001 l.264/l.494; ENF-04; research.md §3.4
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico por caminho D4.15; pendência = precondição não satisfeita ⇒ DENY (ENF-04)
    GATE DE SAÍDA: os DENY de pendência são verificáveis como predicado; a admissão POSITIVA por qualquer caminho é
                   **INDETERMINADO** até as [DECISÃO NECESSÁRIA]
    CRITÉRIO 4Es: Conformidade > Eficácia — não contaminar com não-validado; não perder estado canônico
  VERIFICADO POR:
    DADO        (i) formado SEM selo; (ii) formado COM selo, contrato do selo pendente; (iii) canônico por (a), critério pendente
    QUANDO      o gate de fronteira roda
    ENTÃO       (i)/(ii)/(iii) rejeitados (fail-closed), nada persistido; admissão positiva segue INDETERMINADO (= T09)
    VERIFICAÇÃO reason(i) == "SEAL_MISSING"; reason(ii) == "SEAL_CONTRACT_UNDEFINED"; reason(iii) == "PATH_A_ADMISSION_PENDING";
                written == false (i,ii,iii); positive_admission == "INDETERMINADO"
```

> **[DECISÃO NECESSÁRIA] — caminho (a):** fail-closed. **[PROPOSTA] de critério mínimo (sem decisão de Andraus):**
> hypothesis (CHM-001 l.329) — admitir só {ACTIVE, DOMINANT, SUPERSEDED, REFUTED, ARCHIVED}; evidence/conviction: nenhum.
> **Conflito registrado (N10):** incompatível com a [PROPOSTA] local de preservar TODOS os estados/versões de hipótese
> (não herdada — CEM-001 l.494/612 é da Evidência) e, por D4.16, faria versão com predecessor não admitido cair em
> `VERSION_LINK_MISSING` — qual prevalece = **[DECISÃO NECESSÁRIA]**. **Produtor** de (a) (a SPEC-005 não escreve no KG
> — plan l.971) e **gatilho**: [DECISÃO NECESSÁRIA]. Nós de referência: "catálogo governado" (CEM-001 l.327-340; GMC-001)
> = direção possível, NÃO adotada. **Reatribuição de S14 à SPEC-018/K-001** = proposta a Andraus, não fato.

### BASpec-CKG-011 — Consulta read-only + Cognitive Trace Reconstruction completa
```
BASpec-CKG-011:
  QUANDO:       Um consumidor consulta o KG ou pede a reconstrução da cadeia cognitiva de uma evidência/hipótese
  ENTÃO:        O KG responde read-only e retorna o trace D4.8 (fecho transitivo COMPLETO das arestas DERIVA_DE, ignorando o
                filtro de validade) sem alterar estado; a completude é garantida por INV-CKG-02 e NÃO é rebaixada por H-001
                (só a eficiência de consultas multi-salto AMPLAS fica INDETERMINADA até H-001)
  PORQUE:       Reconstrução completa é responsabilidade canônica do KG (CEM-001 l.562-565/l.699); consulta não muta
  REFERÊNCIA:   RULE-CKG-011; D4.8; INV-CKG-02; CEM-001 l.608-615/l.612-614/l.602; SAS-001 §6.12
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : travessia determinística D4.8; read-only
    CRITÉRIO 4Es: Eficácia (reconstrução completa — obrigação) > Eficiência (consulta ampla = H-001)
  VERIFICADO POR:
    DADO        Evidence-E deriva de D; D deriva de C; C deriva de A e B (cadeia de 3 saltos)
    QUANDO      pede-se Cognitive Trace Reconstruction de Evidence-E
    ENTÃO       retorna o fecho completo [A,B,C,D] (ordem de ancestralidade); nenhum registro criado pela consulta
    VERIFICAÇÃO trace == ["A","B","C","D"]; trace_complete == true; state_mutated_by_query == false; records_created_by_query == 0
```

### BASpec-CKG-012 — Lifecycle do nó/relação (estado = projeção derivada; novos registros)
```
BASpec-CKG-012:
  QUANDO:       Um nó/relação é substituído (correção de conteúdo), invalidado no tempo, ou rebaixado (arquivamento)
  ENTÃO:        O KG grava um NOVO registro (creation com supersedes / invalidation / archival sob gate E3) e o estado é a
                projeção D4.7; correção/reativação = novo registro; nenhuma versão é removida/mutada
  PORQUE:       Conhecimento permanente/temporário se opera por lifecycle versionado, não por deleção/mutação (INV-07; INV-CBP-01)
  REFERÊNCIA:   RULE-CKG-012; D4.4/D4.7; CHM-001; INV-07; SPEC-004 INV-CBP-01
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : transições append-only (novo registro aponta para o anterior por supersedes/target_record_ref); D4.7
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
  QUANDO:       Uma relação em admissão e uma relação vigente satisfazem `colide` (D4.13)
  ENTÃO:        O KG grava um registro `record_kind=collision` que satisfaz D4.3, referenciando ambas por record_id, na MESMA
                unidade atômica tudo-ou-nada da admissão (D4.18); NÃO sobrescreve/apaga em silêncio; relações que não
                satisfazem `colide` NÃO geram colisão; a resolução é de SPEC-007/SPEC-018 ou governança
  PORQUE:       Preservar a contradição auditável respeita INV-07; resolver em silêncio perderia conhecimento; o escopo evita
                falso-positivo; a atomicidade evita `collision` com referência pendurada
  REFERÊNCIA:   RULE-CKG-013; §D2.2; D4.13/D4.18; INV-07; SPEC-004 plan l.381/l.689; fronteira SPEC-007/SPEC-018
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : detecção determinística D4.13 + gravação atômica D4.18; proíbe sobrescrita silenciosa
    GATE DE SAÍDA: verificação (colide ⇒ collision com envelope completo gravado junto da creation ∧ ambas preservadas;
                   admissão reprovada ⇒ nenhum collision; ¬colide ⇒ nenhum collision)
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda de conhecimento e auditabilidade da contradição
  VERIFICADO POR:
    DADO        CONFIRMA(A→B) vigente e uma REFUTA(A→B) nova com janela efetiva sobreposta (mesmos A,B)
    QUANDO      a escrita roda
    ENTÃO       ambas preservadas; registro collision gravado com envelope completo; nenhuma apagada; resolução não decidida
    VERIFICAÇÃO both_relations_present == true; collision_logged == true; collision_envelope_complete == true; silent_overwrite == false
```

---

## D4 — Algoritmo (FONTE ÚNICA de predicados e códigos de rejeição)

Mecânicas **determinísticas reais** (atomic-spec §2). O **mecanismo físico** é **INDETERMINADO = H-001 (ABERTA)**;
abaixo está a lógica, não a tecnologia. Todo item é [PROPOSTA].

- **D4.1 Integridade (CKG-001):** `aceitar sse tipo ∈ catálogo ∧ (origem.node_type, destino) ∈ matriz[tipo_relação] ∧ direção/simetria conformes (§D2.1)`; senão `ONTOLOGY_INTEGRITY_VIOLATION`; tipo fora do catálogo ⇒ `RELATION_TYPE_INVALID`; observation rotulada evidence ⇒ `OBSERVATION_IS_NOT_EVIDENCE`.
- **D4.2 Proveniência (CKG-005; v1.6 — N2):** `computed_by` ausente ⇒ `COMPUTED_BY_MISSING`; `produced_by_gate ∉ {true,false}` ⇒ `PROVENANCE_INCONSISTENT`; `node_type=evidence ∧ evidence_origin_type ∉ {PRIMARY, DERIVED}` ⇒ `PROVENANCE_INCONSISTENT`; `produced_by_gate=true ∧ gate_record ausente` ⇒ `GATE_RECORD_MISSING`; `produced_by_gate=false ∧ gate_record presente` ⇒ `PROVENANCE_INCONSISTENT`; `evidence_origin_type=DERIVED ∧ lineage=[]` ⇒ `LINEAGE_MISSING`; `evidence_origin_type=PRIMARY ∧ lineage≠[]` ⇒ `PROVENANCE_INCONSISTENT` (CEM-001 l.354). Para node_types não-evidence e relações, `lineage` é opcional (sem discriminante canônico — `[]` legítimo). `collision`: o KG grava `produced_by_gate=true` e `gate_record=decision_id` do PASS do detector. **Limite:** o KG verifica a CONSISTÊNCIA dos discriminantes declarados, não sua veracidade frente ao objeto a montante (sem lookup; ENF-03).
- **D4.3 Envelope único — `envelope_completo(r)` (CKG-006/013):** `r.record_id ∧ r.record_kind ∧ r.subject_kind ∧ r.subject_id ∧ r.version ∧ (r.supersedes ∨ null declarado) ∧ r.schema_version ∧ r.provenance_ref.computed_by ∧ r.provenance_ref.produced_by_gate ∈ {true,false} ∧ r.writer_id ∧ r.recorded_at ∧ r.publication.origin ∧ (creation ⇒ r.valid_from) ∧ (invalidation ⇒ r.valid_to) ∧ (kind ∈ {invalidation, archival, canonical_state_transition} ⇒ r.target_record_ref resolve) ∧ (collision ⇒ payload.relation_a_ref ∧ payload.relation_b_ref resolvem)`; senão `RECORD_ENVELOPE_INCOMPLETE`. **Janela (m4):** `invalidation.valid_to < alvo.valid_from ⇒ VALIDITY_WINDOW_INVALID`.
- **D4.4 Versão/sucessão de TODO `record_kind` (M10; v1.6 — N9/n2):** `subject_id` de invalidation/archival/canonical_state_transition = o do sujeito-alvo; `version(r) = 1 + max(version dos registros já gravados do sujeito)` (1 se nenhum); `recorded_at(r) ≥ recorded_at` do registro `version(r)−1` do sujeito; `supersedes` ≠ null só em `creation` de conteúdo corrigido (→ creation anterior do MESMO sujeito) e em `invalidation` que corrige invalidação anterior (→ essa invalidação); null em archival/canonical_state_transition/collision e na 1ª creation. Collision: sujeito próprio, `version=1`. Violação ⇒ `RECORD_VERSION_INVALID`. Replay: registros do sujeito ordenados por `version`.
- **D4.5 Log `kg_gate_decision` (v1.6 — N4):** `{decision_id, submission_id, gate_id, gate_version, input_digest, result ∈ {PASS, DENY, INDETERMINADO}, reason, judgment_invocations, writer_id, decided_at}`; `decision_id` ÚNICO e imutável (chave de resolução); append-only e IMUTÁVEL (RULE-CKG-006; EC-CKG-002 E3); registra TODA decisão de gate (inclusive DENY sem persistência de conhecimento, outcome do bounded loop, tentativas de DELETE/UPDATE bloqueadas, falha de commit D4.18); base da amostragem de falso-DENY (ENF-07). Resolução: o `gate_record` de um `collision` DEVE resolver para um `kg_gate_decision` com `gate_id=CKG-013 ∧ result=PASS`; o `gate_record` de objeto a montante é referência à SPEC-004 (resolução fora do KG — limite). **Redução a `record_kind` do `kg_record` — avaliada e rejeitada:** decisão ≠ conhecimento (D9); o DENY seria uma escrita de conhecimento sujeita aos gates que ela mesma registra (circular com CKG-009/§D2.3, hoje todo DENY); imutabilidade, chave única e EC são obtidos sem 2º envelope de conhecimento.
- **D4.6 Validade bitemporal (CKG-004):** criação `R0{creation, valid_from}`; mudança (ato autorizado) `R1{invalidation, target_record_ref=R0, valid_to}` — R0 nunca mutado. Vale para relação e nó. Invalidações efetivas de `v` = as que miram `v` e não foram supersedidas; `valid_to_efetivo(v) = min(valid_to)` delas, ou `+∞` se nenhuma. **valid-time** `válida_em(v,T) = valid_from(v) ≤ T < valid_to_efetivo(v)`; **transaction-time** `conforme_registrado_em(R)` = a mesma função restrita aos registros com `recorded_at ≤ R`.
- **D4.7 Projeção de estado (CKG-006/012; M10; n2):** definida para `T ≥ valid_from(v)` (para `T < valid_from(v)`, `v` não existe em valid-time e não é retornado): `estado(v,T) = ARCHIVED se ∃ archival com target_record_ref=v; senão SUPERSEDED se ∃ creation c' com c'.supersedes=v; senão INVALIDATED_IN_TIME se ¬válida_em(v,T); senão ACTIVE_KNOWLEDGE`. Precedência fixa ARCHIVED > SUPERSEDED > INVALIDATED_IN_TIME > ACTIVE_KNOWLEDGE (archival é terminal para a versão — análogo a CHM-001 l.767; reativação = nova versão). `canonical_status(v)` = `status_to` da última `canonical_state_transition` do sujeito por `version` (ou o snapshot de criação) — trilha separada. Mesma entrada de registros ⇒ mesmo estado em qualquer implementação conforme. `DELETE/UPDATE de registro ⇒ negado`.
- **D4.8 Cognitive Trace Reconstruction (CKG-011):** `trace(x) = fecho transitivo das arestas DERIVA_DE a partir de x` — **completo** (INV-CKG-02; IGNORA filtro de validade); ordem de saída = ancestralidade (primários→derivados, CEM-001 l.567-577). Consulta: zero registros criados. Eficiência de travessia ampla = H-001.
- **D4.9 Dedupe (CKG-001/003):** `chave de nó = (node_type, canonical_ref)` quando canônico; `= (node_type, natural_key)` quando `canonical_ref=null`; `chave de relação = (relation_type, from_node, to_node | target_relation_id, valid_from)`. Reescrita idêntica = no-op; divergente = novo registro (nunca sobrescreve).
- **D4.10 Gate causal/similaridade (CKG-008; toda CAUSA/SIMILAR_A):** `CAUSA ⇒ exige mechanism, direction, conditions, regime ≠ ∅ ∧ posthoc_flag ∈ {true,false}` (valor explícito; ausência NÃO equivale a false — v1.6, N7); senão `CAUSAL_FIELDS_MISSING`. `SIMILAR_A ⇒ exige similarity_basis ≠ ∅ ∧ from.node_type = to.node_type ∧ from ≠ to`; senão `SIMILARITY_BASIS_MISSING` / `ONTOLOGY_INTEGRITY_VIOLATION`; `∃ SIMILAR_A vigente entre {from,to} em qualquer direção ⇒ no-op`. Verifica PRESENÇA, não veracidade (ENF-03): `posthoc_flag=false` declarado falsamente não é detectável pelo gate.
- **D4.11 Bounded loop do juízo (CKG-008; M6; n9):** `por submissão: invocações(juízo) ≤ 1; se ¬D4.10 ⇒ outcome=INDETERMINADO, nada escrito, kg_gate_decision(INDETERMINADO, judgment_invocations)`; o KG nunca emite nova submissão nem re-tentativa; sem cache/memoização (re-submissão de produtor = nova submissão, cuja frequência está fora do KG). Host do juízo pendente ⇒ `invocações = 0` (§D2.3).
- **D4.12 Guard de custo E confiança (CKG-007/INV-04; v1.6 — N8, texto único):** (i) payload de nó `conviction` é FECHADO — admite só `{node_type, canonical_ref, canonical_status, canonical_predecessor_ref, successor_ref}` (`additionalProperties:false`); qualquer outro campo (confiança, custo, score, `relation_confidence` ou outro) ⇒ `CONFIDENCE_IS_NOT_CONVICTION`; (ii) relação de QUALQUER tipo com `from.node_type=calibration_metric ∧ to.node_type=conviction` ⇒ `ONTOLOGY_INTEGRITY_VIOLATION`; (iii) `relation_confidence` só em `payload.relation.creation` (escala = PARÂMETRO INDETERMINADO). Limite: semântica de custo/confiança em texto livre de OUTROS node_types não é detectada (ENF-03).
- **D4.13 Colisão (CKG-013/§D2.2; v1.6 — N11):** `colide(r1,r2) sse (r1.type, r2.type) ∈ tabela §D2.2 ∧ r1.from=r2.from ∧ r1.to=r2.to ∧ [valid_from(r1), valid_to_efetivo(r1)) ∩ [valid_from(r2), valid_to_efetivo(r2)) ≠ ∅` (D4.6, avaliado sobre os registros já gravados no instante da detecção). Predicado avaliado no passo 8 do D6, SEM gravar; gravação só em D4.18 (payload `relation_a_ref`=creation vigente, `relation_b_ref`=creation em admissão, `contradiction_pair`, `overlap_window`).
- **D4.14 Nó hypothesis/structure (CKG-001/§D2.1):** `school = mapa_produtor(producer_id)` (tabela [PROPOSTA]; sem mapeamento ⇒ `SCHOOL_UNDERIVABLE`); `node_type=hypothesis ∧ school=ICT ⇒ HYPOTHESIS_SCHOOL_ICT_FORBIDDEN` (INV-02/RULE-HH-004); `hierarchy_role=PRIMARY ∧ school≠Elliott ⇒ ONTOLOGY_INTEGRITY_VIOLATION` (RULE-HH-002); `HERDA ∧ pai.hierarchy_role≠PRIMARY ⇒ ONTOLOGY_INTEGRITY_VIOLATION` (RULE-HH-003); "família" = `{n : n.school = m.school ∧ n PERTENCE_A mesmo (asset,timeframe) de m}`. Verifica o `producer_id` declarado (limite de forma — §D2.1).
- **D4.15 Fronteira (CKG-010; §D2.3):** `caminho(obj) = lookup(§D2.3)`; `contrato(caminho) == PENDENTE ⇒ REJECTED motivo(caminho)` (`PATH_A_ADMISSION_PENDING` / `SEAL_CONTRACT_UNDEFINED` / `ENTRY_PATH_UNDEFINED`); `formado ∧ ¬selo ⇒ SEAL_MISSING`; hoje todo caminho de conhecimento retorna DENY.
- **D4.16 Elos de versão e legalidade canônica (CKG-002; v1.6 — N6/n8):** `canonical_model` é FIXO pelo node_type (hypothesis→CHM-001, evidence→CEM-001, conviction→CCM-001 — sem ler o objeto canônico). **hypothesis:** `canonical_ref.version > 1 ⇒ canonical_predecessor_ref` obrigatório ([FONTE] CHM-001 l.588). **conviction:** idem ([INFERÊNCIA] do campo `previous_version_id`, CCM-001 l.58, + INV-07; o CCM não enuncia a obrigatoriedade). **evidence:** `status_to=SUPERSEDED ⇒ successor_ref` obrigatório ([FONTE] CEM-001 l.450); `canonical_predecessor_ref` opcional (o CEM não tem o campo). `successor_ref` em CHM/CCM = opcional, [PROPOSTA] local (a cadeia é navegável pelo predecessor da sucessora). **Resolução:** todo elo presente DEVE resolver para nó já no KG (logo, predecessor antes do sucessor; para evidence, sucessora admitida antes da transição a SUPERSEDED) — ausente ou não resolvido ⇒ `VERSION_LINK_MISSING`. **Legalidade:** `canonical_model ∈ {CHM-001, CEM-001} ∧ (status_from, status_to) ∉ grafo canônico (CHM-001 l.744-757; CEM-001 l.460-466) ⇒ CANONICAL_TRANSITION_ILLEGAL`; `status_from ≠ canonical_status corrente ⇒ idem`; CCM-001: só `status_to ∈ enum` (sem tabela). **Limite (n8):** uma transição perdida trava as seguintes do mesmo sujeito (fail-closed); a reconciliação (quem reenvia a transição faltante) é do produtor/contrato de (a) = [DECISÃO NECESSÁRIA].
- **D4.17 Ordem de ancestrais (INV-CKG-02; M7):** `evidence d com evidence_origin_type=DERIVED: ∀a ∈ Lineage(d): a ∈ KG ⇒ materializa DERIVA_DE(d→a) na unidade de D4.18; ∃a ∉ KG ⇒ ANCESTOR_NOT_ADMITTED` (sem estado de espera).
- **D4.18 Admissão atômica tudo-ou-nada (CKG-006/013; v1.6 — N5) [PROPOSTA; espelha SPEC-004 plan l.381/l.689]:** após os passos 1–8 do D6 aprovarem, os registros da submissão — `creation` do sujeito, `creation` de cada `DERIVA_DE` materializada (D4.17) e, se `colide`, o `collision` — são validados por D4.3/D4.4 e gravados JUNTOS; se qualquer um falha, NENHUM é gravado (sem `collision` pendurado — T21) e a falha vai ao `kg_gate_decision`. O `kg_gate_decision` é gravado em qualquer resultado (fora da unidade de conhecimento). Mecanismo físico da atomicidade = H-001/BUILD.

Nenhuma fórmula computa convicção. Nenhum limiar de convicção nem escala numérica de confiança é fixado (RULE-MET-01).
[FONTE: atomic-spec §2; CEM-001 Cap.5/l.271-283/l.351-355/l.450; CHM-001 l.361/l.588/l.744-757; CCM-001 l.58; SPEC-004 INV-CBP-01, plan l.381/l.689; research.md §3.1/§4]

---

## D5 — Máquina de estados (lifecycle do nó/relação — estado = projeção derivada)

> **Fronteira (CC-02/CC-10):** lifecycle do **conhecimento no KG permanente**, separado da máquina da **hipótese** (CHM-001)
> e do **estado do objeto no Blackboard** (SPEC-004) — não redefinidos. **O `knowledge_state` NÃO é campo mutado: é a
> PROJEÇÃO D4.7.** Os estados abaixo são **HOMÔNIMOS mas ≠ estados canônicos** (SUPERSEDED/ARCHIVED do CHM/CEM/CCM;
> INVALIDATED só do CEM-001; REFUTED só do CHM-001); o Status canônico é rastreado à parte (`canonical_status` +
> `canonical_state_transition` — CKG-002/010).

| Estado (derivado) | Definição (projeção — função exata: D4.7) | Origem |
|---|---|---|
| ACTIVE_KNOWLEDGE | registro de criação vigente, sem sucessora nem invalidação efetiva nem arquivamento | criação |
| SUPERSEDED | existe sucessora que o referencia por `supersedes` (conteúdo corrigido/substituído) | CKG-012 |
| INVALIDATED_IN_TIME | `T ≥ valid_to_efetivo` (D4.6), SEM sucessora de conteúdo (o mundo mudou) | CKG-004/012 |
| ARCHIVED | existe registro de arquivamento (rebaixamento de `relevance` sob gate E3 — CKG-009) | CKG-012 |

> **Estados transitórios de admissão (NÃO persistidos):** `CANDIDATE_WRITE` (sob os gates) e `REJECTED` (falhou em gate;
> decisão no log `kg_gate_decision`, nenhum `kg_record`).
>
> | Transição de admissão | Condição | Fonte |
> |---|---|---|
> | (submissão) → CANDIDATE_WRITE | entrada recebida | D6 passo 1 |
> | CANDIDATE_WRITE → REJECTED | qualquer gate D6 reprova (inclusive `ANCESTOR_NOT_ADMITTED`) ou a unidade atômica falha | D6 passos 2–9; D4.18 |
> | CANDIDATE_WRITE → ACTIVE_KNOWLEDGE (unidade atômica gravada) | todos os gates aprovam (hoje inalcançável — §D2.3) | D6 passo 9 |
> **Correção/reativação:** sempre por NOVO registro, nunca reuso/mutação (INV-07). **Autoridade de arquivamento:** gate E3
> de governança (CKG-009). **Mecanismo físico = INDETERMINADO (H-001 ABERTA)**; Opção B (banco de grafos) **registrada e
> adiada** (research.md §3.5). [FONTE: RULE-CKG-006/012; SPEC-004 INV-CBP-01; DHR-SPEC006-001 §3]

---

## D6 — Protocolo de escrita/consulta (sobre conhecimento publicado)

### Produtores, consumidores e fronteira [FONTE: SAS-001 §6.12; CEM-001 l.608-615; SPEC-004/005; ROADMAP §6/§7]
- O conhecimento entra pelos caminhos da **tabela §D2.3**, sob a mesma governança (CKG-009); todo caminho pendente é fail-closed.
- O **produtor** (SAS-001 §6.12) registra relações pelo caminho (c) (contrato [DECISÃO NECESSÁRIA]) mas **não redefine** ontologia/taxonomia; escrita E3 sob identidade autenticada (SPEC-004).
- **[INFERÊNCIA]/[DECISÃO NECESSÁRIA]** — eventual **consumo** de `Evidence.Invalidated` (canônico, CEM-001 l.600/l.722; transportado pela SPEC-005, plan l.88/l.859) serve só de **gatilho** para avaliação AUTORIZADA (CKG-009), **nunca** invalidação automática (CEM-001 l.602); consumidor/contrato de consumo e emissão pelo KG = **[DECISÃO NECESSÁRIA]**.
- A **consulta** é read-only e **opcional/não-bloqueante** (SAS-001 §6.12/EC-COG-003).

### Sequência de escrita (uma submissão)
1. **Submissão:** um objeto chega por um caminho da §D2.3. Toda decisão de gate é registrada em `kg_gate_decision` (D4.5).
2. **Fronteira (CKG-010):** D4.15. **Hoje toda submissão de conhecimento para aqui.**
3. **Autorização E3 (CKG-009):** allowlist definida ∧ escritor ∈ allowlist ∧ identidade autenticada ∧ não redefine ontologia; senão `REJECTED` (`WRITER_ALLOWLIST_UNDEFINED` se indefinida).
4. **Ontologia/integridade (CKG-001/007):** D4.1 ∧ D4.14 ∧ guard D4.12.
5. **Proveniência (CKG-005):** D4.2.
5-bis. **Linhagem (INV-CKG-02, evidence DERIVED):** D4.17.
5-ter. **Elos de versão/legalidade canônica (CKG-002, canônico/transição):** D4.16.
6. **Causalidade/similaridade (CKG-008, toda CAUSA/SIMILAR_A):** D4.10; se há juízo, D4.11.
7. **Envelope/versão (CKG-006):** os registros candidatos satisfazem D4.3 e D4.4 (senão `RECORD_ENVELOPE_INCOMPLETE` / `VALIDITY_WINDOW_INVALID` / `RECORD_VERSION_INVALID`).
8. **Detecção de colisão (CKG-013):** predicado D4.13 contra relações vigentes — **sem gravar** (v1.6 — N5).
9. **Commit atômico (CKG-006/013):** D4.18 — creation + DERIVA_DE materializadas + collision (se houver) gravados juntos, ou nenhum; estado derivado `ACTIVE_KNOWLEDGE`. DELETE/UPDATE de registro proibido.
10. **Temporalidade (CKG-004):** a invalidação é **ato AUTORIZADO** posterior (novo registro sob CKG-009), **nunca automática/em cascata** (CEM-001 l.602; impacto é de CHM/CCM/CDM — l.503/606; CHM-001 l.672-676).
11. **Consumo de evento (SPEC-005) — [INFERÊNCIA]/[DECISÃO NECESSÁRIA]:** se o KG consome `Evidence.Invalidated`, isso só dispara avaliação autorizada (CKG-009); emissão de evento PELO KG = [DECISÃO NECESSÁRIA].

> **Nota de fronteira:** memória de **trabalho** e sua ordem/versão = **SPEC-004**; **notificação** = **SPEC-005**;
> **formação** = **SPEC-007**. A SPEC-006 só **preserva, relaciona e consulta** o conhecimento permanente. [FONTE: ROADMAP §5/§6/§7]

---

## D7 — Cenários de Teste

> **Convenção de teste:** (i) cenários de **gate** verificam o PREDICADO do gate sobre a entrada (independe dos demais
> gates); (ii) **consulta/lifecycle/colisão** usam **fixture** de registros já no KG; (iii) **persistência** fim a fim é
> **CONDICIONAL** — hoje o verificável é o DENY da §D2.3; (iv) o detector de colisão (passo 8) é PREDICADO sobre relação de
> fixture tratada como aprovada nos passos 1–7; (v) **(n6)** um fixture pode PRESUMIR, declarando-o, um contrato pendente
> (allowlist com o escritor do teste, mapeamento `producer_id`→`school`, sujeito já admitido) só para o predicado sob teste,
> nunca concluindo admissão positiva. **Cenário idêntico ao VERIFICADO POR de uma BASpec o referencia** (fonte única). 21 cenários.

### Cenário-CKG-T01 — Violação de integridade da ontologia → rejeição
= VERIFICADO POR de BASpec-CKG-001 (ORIGINA com origem `school=ICT` ⇒ `ONTOLOGY_INTEGRITY_VIOLATION`; predicado (i)).

### Cenário-CKG-T15 — HERDA SMC-SUB → Elliott-PRIMARY (positivo; entre escolas é VÁLIDO)
```
DADO        hipótese SUB de school=SMC (fixture com mapeamento SMC presumido — convenção (v); sem ele: SCHOOL_UNDERIVABLE, T20)
            com parent_id apontando para hipótese PAI de school=Elliott (hierarchy_role=PRIMARY)
QUANDO      o gate de integridade (D4.1/D4.14) avalia a relação HERDA (predicado — convenção (i))
ENTÃO       o gate APROVA (entre escolas é permitido — RULE-HH-003); a persistência depende ainda da fronteira ((a) — T16)
VERIFICAÇÃO integrity_gate == PASS; cross_school_herda_allowed == true; parent_hierarchy_role == "PRIMARY"; parent_school == "Elliott"
```

### Cenário-CKG-T02 — observation rotulada evidence → rejeição (INV-06)
= VERIFICADO POR de BASpec-CKG-002 (`OBSERVATION_IS_NOT_EVIDENCE`).

### Cenário-CKG-T03 — Relação sem tipo/direção → rejeição
= VERIFICADO POR de BASpec-CKG-003 (`RELATION_TYPE_INVALID`).

### Cenário-CKG-T04 — Validade muda por NOVO registro (sem mutar/deletar)
= VERIFICADO POR de BASpec-CKG-004 (R0 intacto; invalidation com valid_to=T1; consulta valid-time consistente).

### Cenário-CKG-T05 — Deleção/mutação proibida, inclusive no log de decisões
= VERIFICADO POR de BASpec-CKG-006 (casos (a) registro arquivado e (b) `kg_gate_decision`; ambos negados).

### Cenário-CKG-T06 — Guard D4.12 (custo E confiança) por node_type/campo
```
DADO        (fixtures; predicado do passo 4) (a) relação CAUSA(calibration_metric → conviction); (b) relação PERTENCE_A
            (calibration_metric → conviction); (c) nó conviction com campo "cost"; (d) relação com relation_confidence
QUANDO      o guard D4.12 roda
ENTÃO       (a),(b) rejeitadas ONTOLOGY_INTEGRITY_VIOLATION (qualquer relation_type); (c) rejeitado CONFIDENCE_IS_NOT_CONVICTION;
            (d) aceita pelo guard (relation_confidence só no payload de relação)
VERIFICAÇÃO reason(a) == reason(b) == "ONTOLOGY_INTEGRITY_VIOLATION"; reason(c) == "CONFIDENCE_IS_NOT_CONVICTION"; guard(d) == PASS;
            cost_or_confidence_to_conviction_edge == false
```

### Cenário-CKG-T07 — Causal sem mecanismo/regime → rejeição
= VERIFICADO POR de BASpec-CKG-008 (`CAUSAL_FIELDS_MISSING`; pós-hoc sem flag explícito: ADV-04).

### Cenário-CKG-T08 — Auth da SPEC-004 indisponível → escrita negada (fail-closed) [E3]
= VERIFICADO POR de BASpec-CKG-009.

### Cenário-CKG-T09 — Fronteira: formado sem selo / com selo sem contrato / canônico por (a) pendente → DENY
```
= VERIFICADO POR de BASpec-CKG-010 (casos (i)/(ii)/(iii)), com (iii) = hipótese canônica que transita para REFUTED (CHM-001).
CONDICIONAL (pós-decisões de Andraus — hoje INDETERMINADO): canonical_state_transition_recorded == true;
            evidence_states_preserved == true (CEM-001 l.494); version_links_resolve == true (formato verificável hoje em T17)
```

### Cenário-CKG-T10 — Cognitive Trace Reconstruction completa (3 saltos)
= VERIFICADO POR de BASpec-CKG-011 (trace == [A,B,C,D]; records_created_by_query == 0).

### Cenário-CKG-T11 — Colisão de relações registrada (não resolve em silêncio)
```
DADO        CONFIRMA(A→B) vigente e REFUTA(A→B) nova já aprovada nos passos 1–7, ambas fixture (convenção (iv)), janelas
            efetivas sobrepostas
QUANDO      o detector (passo 8) e o commit atômico (passo 9) rodam
ENTÃO       ambas preservadas; collision gravado na mesma unidade da creation de REFUTA; nenhuma apagada; resolução não decidida
VERIFICAÇÃO both_relations_present == true; collision_logged == true; collision_envelope_complete == true; silent_overwrite == false
```

### Cenário-CKG-T12 — Nó PRIMARY sem gate/ancestral passa no gate de proveniência (caminho feliz do gate)
= VERIFICADO POR de BASpec-CKG-005, caso (a) (persistência ponta-a-ponta: T16 — barrada na fronteira, não na proveniência).

### Cenário-CKG-T13 — Correção de conteúdo = nova versão (supersessão por novo registro)
= VERIFICADO POR de BASpec-CKG-012.

### Cenário-CKG-T14 — Escrita sem identidade autenticada → rejeição
= VERIFICADO POR de BASpec-CKG-005, caso (b) (`COMPUTED_BY_MISSING`; computed_by é sempre obrigatório — CBP-014).

### Cenário-CKG-T16 — Sequência D6 completa para PRIMARY sem gate e sem ancestral
```
DADO        nó hypothesis PRIMARY (producer_id="elliott_specialist" ⇒ school=Elliott; hierarchy_role=PRIMARY), lineage=[],
            produced_by_gate=false, sem gate_record, computed_by/writer_id autenticados, pelo caminho (a) com critério pendente
QUANDO      a sequência D6 roda (passos 1→9) e, em paralelo, cada gate é avaliado como predicado sobre a mesma entrada
ENTÃO       (i) sequência: para no passo 2 com REJECTED PATH_A_ADMISSION_PENDING; nada persistido;
            (ii) predicados: passo 3 (allowlist de fixture — convenção (v)) PASS; passo 4 PASS; passo 5 (D4.2) PASS sem exigir
            gate_record nem lineage não-vazio
VERIFICAÇÃO sequence_stop_step == 2; rejected_reason == "PATH_A_ADMISSION_PENDING"; written == false;
            step5_predicate == PASS; step5_required_gate_record == false; step5_required_lineage_nonempty == false
CONDICIONAL (pós-decisão de Andraus sobre (a), se a hipótese satisfizer o critério): sequence_stop_step == null;
            written == true; knowledge_state == "ACTIVE_KNOWLEDGE" — hoje INDETERMINADO
```

### Cenário-CKG-T17 — Reconstrução/auditoria a partir dos registros (envelope único + log)
```
DADO        fixture append-only: relação R (creation R0; invalidation R1 com target_record_ref=R0); relação R' (creation R2)
            contraditória com R0 e janela efetiva sobreposta; registro collision C1 (relation_a_ref=R0, relation_b_ref=R2,
            produced_by_gate=true, gate_record=DEC-1); log com DEC-1 {gate_id=CKG-013, result=PASS}; nó H@1 (canonical_ref=H@1)
            com canonical_state_transition S1 (ACTIVE→DOMINANT) e S2 (DOMINANT→SUPERSEDED), target_record_ref à creation de
            H@1; nó H@2 com canonical_predecessor_ref=H@1 (CHM: obrigatório pois version=2; successor_ref opcional — D4.16)
QUANDO      um auditor independente reconstrói o histórico SÓ a partir dos registros (replay por sujeito, por version — D4.4)
ENTÃO       todo registro (R0,R1,R2,C1,S1,S2,H@2) satisfaz D4.3 e D4.4; toda referência resolve, inclusive o gate_record de C1
            no log; estado(R,"agora") = INVALIDATED_IN_TIME e vigente antes de valid_to; histórico canônico de H@1 = [S1,S2];
            cadeia H@1→H@2 navegável (H@2→H@1 pelo elo; H@1→H@2 por índice derivado do elo)
VERIFICAÇÃO envelope_complete_all == true; orphan_refs == 0; collision_gate_record_resolves == true; distinct_knowledge_record_formats == 1;
            projected_state(R) == "INVALIDATED_IN_TIME"; canonical_history(H@1) == ["ACTIVE→DOMINANT","DOMINANT→SUPERSEDED"];
            version_chain(H) == ["H@1","H@2"]
```

### Cenário-CKG-T18 — SIMILAR_A: gate de saída determinístico
```
DADO        (a) SIMILAR_A(P1→P2) proposta pelo juízo sem similarity_basis; (b) SIMILAR_A(P1→P1); (c) SIMILAR_A(P1→P2) com
            similarity_basis presente e mesmo node_type; (d) SIMILAR_A(P2→P1) com SIMILAR_A(P1→P2) vigente
QUANDO      o gate de saída D4.10 roda
ENTÃO       (a) rejeitada SIMILARITY_BASIS_MISSING; (b) rejeitada (from=to); (c) aprovada pelo gate; (d) no-op (simetria)
VERIFICAÇÃO gate(a) == FAIL; reason(a) == "SIMILARITY_BASIS_MISSING"; gate(b) == FAIL; gate(c) == PASS; new_record(d) == false;
            judgment_invocations_per_submission <= 1
```

### Cenário-CKG-T19 — Ordem de ancestrais sem estado de espera
```
DADO        fixture: A (evidence PRIMARY) no KG; evidence C (DERIVED, Lineage=[A]); evidence D (DERIVED, Lineage=[X]), X ausente
            (predicado de D4.17 — convenção (i); hoje inalcançável fim a fim, (a) pendente)
QUANDO      o passo 5-bis avalia C e D
ENTÃO       C passa, com DERIVA_DE(C→A) no candidato; D é rejeitada imediatamente; não existe estado de espera
VERIFICAÇÃO step5bis(C) == PASS; deriva_de(C→A) == true; step5bis(D) == FAIL; reason(D) == "ANCESTOR_NOT_ADMITTED"; waiting_states == 0
```

### Cenário-CKG-T20 — Caminho indefinido, escola não derivável e allowlist indefinida → DENY
```
DADO        (a) nó asset submetido; (b) relação CAUSA registrada por produtor (SAS-001 l.924 — caminho (c)); (c) hypothesis
            com producer_id do SMC Specialist (não fixado), avaliada no passo 4 como predicado; (d) escrita qualquer
            avaliada no passo 3 com o mantenedor da allowlist pendente
QUANDO      os gates rodam
ENTÃO       todos rejeitados; nada persistido; decisão registrada em kg_gate_decision
VERIFICAÇÃO reason(a) == "ENTRY_PATH_UNDEFINED"; reason(b) == "ENTRY_PATH_UNDEFINED"; reason(c) == "SCHOOL_UNDERIVABLE";
            reason(d) == "WRITER_ALLOWLIST_UNDEFINED"; written == false (a..d)
```

### Cenário-CKG-T21 — Admissão reprovada no commit não deixa `collision` pendurado (v1.6 — N5)
```
DADO        fixture: CONFIRMA(A→B) vigente; REFUTA(A→B) nova aprovada nos passos 1–8 (colide = true), mas o registro collision
            gerado falha D4.3 na validação da unidade (D4.18) — fixture: identidade de serviço do KG indisponível ⇒ computed_by ausente
QUANDO      o commit atômico (passo 9) roda
ENTÃO       a unidade não é gravada: nem a creation de REFUTA nem o collision; a falha fica no kg_gate_decision
VERIFICAÇÃO reason == "RECORD_ENVELOPE_INCOMPLETE"; refuta_written == false; collision_written == false; dangling_collision_refs == 0;
            gate_decision_logged == true
```

---

## D8 — Rigor adversarial focado (casos de negação nos pontos de risco)

> Alvo **D0–D7 + D8 adversarial focado** (CRITICAL, pin D0–D7). **22 casos** cobrindo **todas as 13 BASpecs** e as
> fronteiras/decisões abertas. Princípio transversal: **fail-closed**, **nunca deletar/mutar**, **H-001 INDETERMINADO**.

### ADV-CKG-01 — Deleção disfarçada de "esquecimento" (CKG-006/INV-07)
**DADO:** "esquecer" traduzido em DELETE físico de um registro ou em UPDATE de um `kg_gate_decision`. **QUANDO:** o gate roda. **ENTÃO:** negar; só arquivamento versionado. **PORQUE:** memória permanente nunca apaga (INV-07). **VERIFICAÇÃO:** physical_delete == false; gate_decision_mutated == false.

### ADV-CKG-02 — Sobrescrita silenciosa de relação contraditória (CKG-013)
**DADO:** REFUTA(A→B) sobre CONFIRMA(A→B) (fixture — D7 (iv)). **QUANDO:** detector (passo 8) e commit (passo 9). **ENTÃO:** registrar colisão; preservar ambas. **PORQUE:** perder a contradição apaga conhecimento. **VERIFICAÇÃO:** silent_overwrite == false; both_relations_present == true.

### ADV-CKG-03 — Confiança de relação retroalimenta o Conviction Vector (CKG-007/INV-04)
**DADO:** tentativa de expor a confiança no objeto de convicção ou de somá-la como 9ª dimensão. **QUANDO:** a escrita/escopo é definido. **ENTÃO:** rejeitar por D4.12 (`CONFIDENCE_IS_NOT_CONVICTION`); namespace próprio. **PORQUE:** INV-04 (custo) como base + extensão local; dimensionalidade=8 (fechada). **VERIFICAÇÃO:** confidence_exposed_in_conviction_object == false.

### ADV-CKG-04 — Relação causal pós-hoc sem marcador (CKG-008/RULE-CAU-03; v1.6 — N7)
**DADO:** (a) CAUSA(A→B) só por co-ocorrência, sem mechanism/regime; (b) CAUSA com mechanism/direction/conditions/regime, formulada após o resultado, SEM `posthoc_flag`. **QUANDO:** o gate D4.10 roda. **ENTÃO:** rejeitar ambas `CAUSAL_FIELDS_MISSING` — a ausência do flag não vale como `false`. **PORQUE:** RULE-CAU-01/03. **Limite:** um `posthoc_flag=false` declarado falsamente não é detectável (presença ≠ veracidade — ENF-03). **VERIFICAÇÃO:** causal_written(a) == causal_written(b) == false; reason(b) == "CAUSAL_FIELDS_MISSING".

### ADV-CKG-05 — Métrica de custo/calibração ligada à convicção (INV-04; CKG-007)
**DADO:** (a) relação (qualquer tipo) `calibration_metric`→`conviction`; (b) nó `conviction` cujo payload traz campo de confiança ou de custo. **QUANDO:** guard D4.12 (passo 4) como predicado. **ENTÃO:** rejeitar (a) `ONTOLOGY_INTEGRITY_VIOLATION` e (b) `CONFIDENCE_IS_NOT_CONVICTION`. O ARMAZENAMENTO da métrica (CEE-001 l.111) NÃO é demonstrado — seu caminho é `ENTRY_PATH_UNDEFINED` (Bloco B: PARCIAL). **PORQUE:** INV-04. **VERIFICAÇÃO:** cost_or_confidence_to_conviction_edge == false; confidence_field_in_conviction_payload == false.

### ADV-CKG-06 — Escrita sem proveniência exigível aceita (CKG-005; v1.6 — N2)
**DADO:** (a) registro sem `computed_by`; (b) evidence com `evidence_origin_type=DERIVED` e `lineage=[]`; (c) `produced_by_gate=true` sem `gate_record`; (d) `produced_by_gate` ausente; (e) evidence sem `evidence_origin_type`. **QUANDO:** o gate D4.2 roda. **ENTÃO:** rejeitar (a) `COMPUTED_BY_MISSING`, (b) `LINEAGE_MISSING`, (c) `GATE_RECORD_MISSING`, (d)/(e) `PROVENANCE_INCONSISTENT` — a condicionalidade não é brecha. **PORQUE:** sem origem não é reconstruível (P13). **VERIFICAÇÃO:** written(a..e) == false.

### ADV-CKG-07 — Produtor redefine ontologia/taxonomia (CKG-009/SAS-001 §6.12)
**DADO:** produtor autenticado tenta alterar a ontologia global. **QUANDO:** o gate E3 roda. **ENTÃO:** negar (fail-closed); produtor registra, não redefine (ato de governança). **PORQUE:** SAS-001 §6.12. **VERIFICAÇÃO:** ontology_redefined_by_producer == false.

### ADV-CKG-08 — KG forma conhecimento / absorve SPEC-007 (CKG-010/fronteira)
**DADO:** tentativa de extração/retrieval/validação no KG. **QUANDO:** o escopo é definido. **ENTÃO:** rejeitar `OUT_OF_SCOPE_FORMATION`. **PORQUE:** formação é SPEC-007. **VERIFICAÇÃO:** formation_in_kg == false.

### ADV-CKG-09 — Mecanismo físico fixado / banco de grafos por inércia (CONS-01/mandato)
**DADO:** pressão para fixar "grafo real" (ou escolher engine). **QUANDO:** as decisões são definidas. **ENTÃO:** rejeitar `OPEN_DECISION_H001`; mecanismo físico permanece INDETERMINADO; Opção B adiada. **PORQUE:** H-001 é decisão de Andraus (CONS-01). **VERIFICAÇÃO:** h001_decided_by_spec == false.

### ADV-CKG-10 — Absorver/duplicar vizinhos ou tocar decisão aberta (fronteiras/CONS-01)
**DADO:** a SPEC-006 virar memória de trabalho (SPEC-004), transporte (SPEC-005), estado por agente (SPEC-009), ciclo de aprendizado (SPEC-018), ou tocar M-001/J-001/N-001/G-001/K-001/C-001/WF-D03, ou executar a reconciliação R-07 sem decisão. **QUANDO:** o escopo é definido. **ENTÃO:** rejeitar `OUT_OF_SCOPE_OR_OPEN_DECISION`; decisões abertas permanecem ABERTAS (Andraus). **PORQUE:** CONS-01; INV-09. **VERIFICAÇÃO:** neighbors_absorbed == false; open_decisions_touched == false.

### ADV-CKG-11 — Nó redefine contrato canônico (CKG-002/CC-02)
**DADO:** nó-hipótese que sobrescreve campos/estado do CHM-001. **QUANDO:** a escrita roda. **ENTÃO:** rejeitar; nó referencia por id@version, não redefine. **PORQUE:** CC-02/CONST-01; INV-10. **VERIFICAÇÃO:** canonical_contract_redefined == false.

### ADV-CKG-12 — Relação viola a matriz de integridade (CKG-001/003)
**DADO:** ORIGINA com origem ICT (INV-02) ou SIMILAR_A entre tipos diferentes. **QUANDO:** o gate D4.1 roda. **ENTÃO:** rejeitar `ONTOLOGY_INTEGRITY_VIOLATION`. **PORQUE:** integridade da ontologia (INV-02; matriz). **VERIFICAÇÃO:** written == false.

### ADV-CKG-13 — Invalidação mutando o registro existente (CKG-004/INV-CBP-01)
**DADO:** `valid_to` escrito SOBRE o registro de criação (mutação). **QUANDO:** a invalidação roda. **ENTÃO:** rejeitar; invalidação só por NOVO registro. **PORQUE:** append-only real (SPEC-004 INV-CBP-01). **VERIFICAÇÃO:** existing_record_mutated == false.

### ADV-CKG-14 — Trace incompleto ou consulta que muta estado (CKG-011)
**DADO:** reconstrução que para no 1º salto, ou consulta que grava. **QUANDO:** a consulta roda. **ENTÃO:** exigir fecho completo (D4.8); consulta read-only. **PORQUE:** CEM-001 l.612-614; H-001 não rebaixa a completude. **VERIFICAÇÃO:** trace_complete == true; records_created_by_query == 0.

### ADV-CKG-15 — Transição remove/reescreve a versão anterior (CKG-012/INV-07)
**DADO:** SUPERSEDED implementado apagando/reescrevendo a versão anterior. **QUANDO:** a transição roda. **ENTÃO:** rejeitar; a anterior é preservada; estado é projeção D4.7. **PORQUE:** INV-07; INV-CBP-01. **VERIFICAÇÃO:** old_version_preserved == true; old_version_mutated == false.

### ADV-CKG-16 — evidence DERIVED admitida sem aresta DERIVA_DE por ancestral (CKG-003/INV-CKG-02)
**DADO:** evidence DERIVED com Lineage=[C] admitida sem materializar `DERIVA_DE`→C, ou com C ausente. **QUANDO:** o gate de admissão roda. **ENTÃO:** rejeitar (fail-closed); exigir a aresta por ancestral (D4.17); grafo acíclico. **PORQUE:** sem a aresta o trace completo não é garantido (INV-CKG-02). **VERIFICAÇÃO:** deriva_de_edge_per_ancestor == true; written == false (quando ancestral ausente).

### ADV-CKG-17 — hypothesis com school=ICT (viola regra de nó — INV-02/RULE-HH-004)
**DADO:** nó `hypothesis` com `school == ICT`. **QUANDO:** D4.14 roda. **ENTÃO:** rejeitar `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`; ICT nunca cria hipótese. **PORQUE:** INV-02; RULE-HH-004. **VERIFICAÇÃO:** written == false; rejected_reason == "HYPOTHESIS_SCHOOL_ICT_FORBIDDEN".

### ADV-CKG-18 — colisão falsamente detectada / falsamente ignorada (CKG-013; escopo; v1.6 — N11)
**DADO (fixtures — D7 (iv)):** (a) A1 CONFIRMA B e A2 REFUTA B (A1≠A2); (b) CONFIRMA(A→B) com invalidation efetiva `valid_to=T1` e REFUTA(A→B) com `valid_from=T2 ≥ T1` (janelas EFETIVAS disjuntas); (c) CONFIRMA(A→B) e REFUTA(A→B) com janelas efetivas sobrepostas; (d) INVALIDA(E→R, `target_relation_id`=R) com R vigente. **QUANDO:** o detector D4.13 (passo 8) roda. **ENTÃO:** só (c) colide; (d) não é par da §D2.2 e não altera a validade de R. **PORQUE:** colisão usa `valid_to_efetivo` (o `valid_to` bruto da creation é nulo). **VERIFICAÇÃO:** colide(a)==false; colide(b)==false; colide(c)==true; colide(d)==false; estado(R) inalterado em (d).

### ADV-CKG-19 — Registro com envelope/versão/elo/janela inválidos ou formato paralelo (CKG-002/004/006/013; v1.6 — N9)
**DADO:** (a) `collision` sem `record_id`/`computed_by`/`version`; (b) `canonical_state_transition` sem `target_record_ref` ou com referência inexistente; (c) colisão num formato avulso fora do `kg_record`; (d) evidence com transição a SUPERSEDED sem `successor_ref`, ou hipótese version=2 com predecessor ausente do KG; (e) transição CHM REFUTED→ACTIVE (fora do grafo CHM-001 l.744-757); (f) invalidation com `valid_to` < `valid_from` do alvo; (g) registro com `version` que repete a de outro registro do mesmo sujeito, ou `recorded_at` anterior ao do registro `version−1`. **QUANDO:** passos 5-ter/7. **ENTÃO:** rejeitar (a)/(b)/(c) `RECORD_ENVELOPE_INCOMPLETE`, (d) `VERSION_LINK_MISSING`, (e) `CANONICAL_TRANSITION_ILLEGAL`, (f) `VALIDITY_WINDOW_INVALID`, (g) `RECORD_VERSION_INVALID`. **PORQUE:** D9/INV-CKG-01 (P13); CEM-001 l.450/594-595/612; CHM-001 l.588; legalidade canônica. **VERIFICAÇÃO:** written(a..g) == false; distinct_knowledge_record_formats == 1.

### ADV-CKG-20 — Juízo em laço de re-tentativa (CKG-008)
**DADO:** submissão de CAUSA proposta por juízo reprovada no gate de saída; uma implementação tentaria re-invocar o juízo na mesma submissão ou gerar nova submissão. **QUANDO:** D4.11 é aplicado. **ENTÃO:** ≤1 invocação nessa submissão, sem re-tentativa nem submissão gerada pelo KG, INDETERMINADO, nada escrito, `judgment_invocations` no `kg_gate_decision`. (Nova submissão de PRODUTOR é outra submissão — sua frequência não é do KG.) **PORQUE:** atomic-spec l.315; RULE-INQ-03. **VERIFICAÇÃO:** judgment_invocations_per_submission <= 1; kg_generated_retries == 0; kg_generated_submissions == 0; proposal_outcome == "INDETERMINADO"; written == false.

### ADV-CKG-21 — Admissão pelo caminho (a) enquanto o critério está pendente (CKG-010/EC-CKG-001)
**DADO:** uma evidência ACTIVE (ou hipótese EMERGENT) submetida pelo caminho (a) "porque veio do ciclo de vida canônico", com o critério de (a) pendente. **QUANDO:** D4.15/EC-CKG-001 roda. **ENTÃO:** negar `PATH_A_ADMISSION_PENDING`; "origem ∈ ciclo de vida" NÃO satisfaz a precondição; nada persistido. **PORQUE:** precondição pendente = não satisfeita (ENF-04); E3 irreversível. **VERIFICAÇÃO:** path_a_written == false; rejected_reason == "PATH_A_ADMISSION_PENDING".

### ADV-CKG-22 — SIMILAR_A aceita só pelo escore do juízo (CKG-008)
**DADO:** SIMILAR_A com escore alto do juízo mas sem `similarity_basis`, ou entre node_types distintos. **QUANDO:** D4.10 roda. **ENTÃO:** rejeitar (`SIMILARITY_BASIS_MISSING` / `ONTOLOGY_INTEGRITY_VIOLATION`); escore NÃO é critério. **PORQUE:** ENF-03; RULE-MET-01. **VERIFICAÇÃO:** written == false; acceptance_by_score == false.

> **Cobertura:** 22 casos — toda BASpec tem ≥1 negação: CKG-001→ADV-12/17; 002→ADV-11/19(d,e); 003→ADV-12/16; 004→ADV-13/19(f);
> 005→ADV-06; 006→ADV-01/19(a–c,g); 007→ADV-03/05; 008→ADV-04/20/22; 009→ADV-07 + T20(d); 010→T09/ADV-21 + T20(a,b) (ADV-08 =
> fronteira de escopo, não nega o QUANDO); 011→ADV-14/16; 012→ADV-15; 013→ADV-02/18/19 + T21. Fronteiras/decisões abertas:
> ADV-09/10. Mapeiam para EC-CKG-001..006 (fail-closed).

---

## D9 — Auditabilidade (por referência)

Todo registro de conhecimento (inclusive os especiais) DEVE ser reconstruível (P13) e satisfazer D4.3/D4.4; a colisão tem
UM só formato. As DECISÕES dos gates ficam no log `kg_gate_decision` (D4.5) — segundo formato, declarado, papel distinto,
igualmente imutável. Replay: T17. Trace completo: CKG-011 (CEM-001 l.562-565/l.608-615/l.699). Observabilidade agregada e
estado de trabalho: SPEC-040/SPEC-004, **por referência**. [FONTE: CONSTITUTION P13; CEM-001 l.608-615; SPEC-004 replay; H-001 ABERTA]

---

## Contrato do nó/relação — esqueleto [PROPOSTA]

> Produto central da SPEC-006. **Referencia** os objetos canônicos por `canonical_ref`; **não** os redefine (CC-02).
> Mecanismo físico = **INDETERMINADO (H-001 ABERTA)**. Todo write é E3. **Esta seção é a fonte única dos CAMPOS**;
> obrigatoriedade e predicados estão em D4.

| Camada | Nó | Relação | Fronteira |
|---|---|---|---|
| **Envelope único** | TODO registro de conhecimento é um `kg_record`; obrigatoriedade = D4.3 + D4.4 | idem | CKG-006/013; D9; T17; ADV-19. Decisões de gate: `kg_gate_decision` (D4.5), fora do envelope |
| Tipo de registro | `record_kind` ∈ {creation, invalidation, archival, canonical_state_transition} | `record_kind` ∈ {creation, invalidation, archival} | colisão = `subject_kind=collision`, `record_kind=collision` (UM só formato) |
| Identidade | `node_id` (= `subject_id`), `node_type`, `version`, `schema_version` | `relation_id` (= `subject_id`), `relation_type`, `from_node`, `to_node` (ou `target_relation_id`), `version`, `schema_version` | D4.1; D4.4 |
| Alvo do registro | `target_record_ref` (invalidation/archival/canonical_state_transition; deve resolver) | idem | D4.3 |
| Chave natural (dedupe) | `canonical_ref` (canônico) ou `natural_key` (não-canônico) | `(relation_type, from_node, to_node \| target_relation_id, valid_from)` | D4.9 |
| Versionamento | `supersedes` | `supersedes` | D4.4; estado = D4.7 |
| Produtor/escola | `producer_type`, `producer_id` (espelho — CHM-001 l.361; CEM-001 l.271-278); `school` LOCAL derivado; `hierarchy_role` | — | D4.14; limite de forma (§D2.1) |
| Referência canônica | `canonical_ref` = `canonical_id@version`; `canonical_status` (enum POR MODELO); `evidence_origin_type` (só evidence — CEM-001 l.280-283) | — | CC-02/CKG-002; D4.2 |
| Transição canônica / versões | registro `canonical_state_transition` (payload no schema); nó com `canonical_predecessor_ref` | — | D4.16 (tipado por modelo) |
| Proveniência | `provenance_ref` = { `computed_by`, `produced_by_gate`, `gate_record`, `lineage` } | idem | D4.2; nome local [PROPOSTA] |
| Publicação/escrita | `publication.origin` ∈ {`canonical_lifecycle` (a), `spec007_seal` (b), `producer_registration` (c), `kg_internal`}; `writer_id` autenticado | idem | §D2.3; CKG-009/010 |
| Temporalidade | `valid_from`, `valid_to` (fechado só por registro `invalidation`), `recorded_at` | idem | D4.6 |
| Relevância/arquivamento | `relevance` (em registro `archival`) | idem | CKG-012 |
| Confiança | — (payload de `conviction` FECHADO) | `relation_confidence` (escala PRÓPRIA — PARÂMETRO INDETERMINADO) | D4.12 |
| Causalidade / similaridade | — | `causal` {mechanism, direction, conditions, regime, posthoc_flag}; `similarity_basis` | D4.10 |
| Colisão | — | — (não é campo de relação) | registro próprio; payload no schema; D4.13/D4.18 |

> **Estado:** `knowledge_state` NÃO é campo persistido — é a projeção D4.7. Validade/arquivamento valem para NÓ e RELAÇÃO.
> `canonical_status` + registros `canonical_state_transition` sustentam a preservação de estados canônicos admitidos
> (CKG-010/T09) — o `canonical_ref@version` sozinho não carrega Status (CEM-001 l.264).

### I/O Schema (lógico — referência; não redefine CHM-001/CEM-001/CCM-001)
```json
{
  "kg_record": {
    "_comentario": "ENVELOPE ÚNICO append-only de conhecimento; obrigatoriedade = D4.3; version/supersedes/recorded_at = D4.4; SEM digest (limite m3 — H-001/BUILD)",
    "record_id": "KG-REC-2026-10-17-0001 (único, imutável)",
    "record_kind": "creation | invalidation | archival | canonical_state_transition | collision",
    "subject_kind": "node | relation | collision",
    "subject_id": "KG-N-... | KG-R-... | KG-C-...",
    "version": "1 + max(version do subject_id) — D4.4 (senão RECORD_VERSION_INVALID)",
    "supersedes": "record_id da creation anterior do MESMO subject | da invalidation corrigida | null — D4.4",
    "target_record_ref": "null (creation; collision) | record_id ao qual se aplica (invalidation/archival/canonical_state_transition) — DEVE resolver",
    "schema_version": "1 (migração de ontologia/schema = [DECISÃO NECESSÁRIA] — CKG-009)",
    "provenance_ref": { "computed_by": "OBRIGATÓRIO — identidade AUTENTICADA (SPEC-004 RULE-CBP-014)", "produced_by_gate": "true | false — OBRIGATÓRIO explícito (discriminante LOCAL [PROPOSTA]; collision ⇒ true)", "gate_record": "sse produced_by_gate=true (SPEC-004 CBP-007; collision: decision_id do detector)", "lineage": "ref. ao Lineage CEM-001 / derived_from[] SPEC-004 — não-vazio sse DERIVED; [] sse PRIMARY; opcional nos demais", "who": "", "when": "", "why": "", "from": "" },
    "writer_id": "(identidade autenticada; collision = identidade de serviço do KG — §D2.3)",
    "publication": { "origin": "canonical_lifecycle (a) | spec007_seal (b) | producer_registration (c) | kg_internal — §D2.3", "seal_ref": "[DECISÃO NECESSÁRIA — contrato do selo = SPEC-007]" },
    "recorded_at": "2026-10-17T12:00:00Z (transaction-time; monotônico por subject — D4.4)",
    "valid_from": "obrigatório em creation (nó E relação); null nos demais kinds",
    "valid_to": "obrigatório em invalidation; ≥ valid_from do alvo (senão VALIDITY_WINDOW_INVALID); null nos demais kinds",
    "payload": "um dos payloads abaixo, conforme (subject_kind, record_kind)"
  },
  "payload.node.creation": {
    "node_type": "hypothesis | evidence | observation | conviction | narrative | mission | learning | asset | timeframe | regime | structure | calibration_metric",
    "canonical_ref": "CHM-xxxx@v2 | CEM-xxxx@v1 | CCM-xxxx@v1 | null",
    "canonical_status": "enum POR MODELO: CHM-001 l.329 = EMERGENT|CANDIDATE|ACTIVE|DOMINANT|SUPERSEDED|REFUTED|ARCHIVED; CEM-001 l.258-262 = ACTIVE|SUPERSEDED|INVALIDATED|ARCHIVED; CCM-001 l.58 = COMPUTED|GATED_PASS|GATED_BLOCK|SUPERSEDED; só se canonical_ref != null",
    "canonical_predecessor_ref": "canonical_id@version anterior — obrigatório por D4.16 (hypothesis/conviction com version>1); deve resolver no KG",
    "producer_type": "AGENT | ENGINE (espelho CEM-001 l.271-275 / CHM-001 l.361) — obrigatório em hypothesis/evidence/structure",
    "producer_id": "espelho CHM-001 l.361 / CEM-001 l.276-278 — obrigatório em hypothesis/evidence/structure; entrada de school (D4.14)",
    "evidence_origin_type": "PRIMARY | DERIVED (espelho CEM-001 l.280-283) — obrigatório sse node_type=evidence (D4.2)",
    "natural_key": "(nó NÃO-canônico, p.ex. asset='BTC' | timeframe='H4')",
    "school": "Elliott | Fibonacci | Fractal | SMC | ICT — LOCAL [PROPOSTA], DERIVADO de producer_id (D4.14); só hypothesis/structure",
    "hierarchy_role": "PRIMARY | SUB (só hypothesis; ref. SPEC-001)",
    "ontological_status": "observational | theoretical (RULE-ONT-01; só structure/regime/narrative)"
  },
  "payload.node.creation[node_type=conviction]": {
    "_comentario": "FECHADO — guard D4.12 (custo E confiança); qualquer outro campo ⇒ CONFIDENCE_IS_NOT_CONVICTION",
    "additionalProperties": false,
    "properties": ["node_type", "canonical_ref", "canonical_status", "canonical_predecessor_ref", "successor_ref"]
  },
  "payload.relation.creation": {
    "relation_type": "CONFIRMA | REFUTA | DEPENDE_DE | HERDA | PERTENCE_A | INVALIDA | ORIGINA | DERIVA_DE | SIMILAR_A | CAUSA | HIERARQUIA_DE | ESTATISTICA_DE",
    "from_node": "KG-N-...-A",
    "to_node": "KG-N-...-B | null quando target_relation_id é usado",
    "target_relation_id": "null | KG-R-...-X (alvo é RELAÇÃO — INVALIDA; matriz §D2.1)",
    "relation_confidence": "escala PRÓPRIA — PARÂMETRO INDETERMINADO; NÃO é Convicção; não toca J-001/N-001 (abertas)",
    "causal": "{ mechanism, direction, conditions, regime, posthoc_flag: true|false (explícito) } — obrigatório sse CAUSA (D4.10)",
    "similarity_basis": "[atributos/critério comparados] — não-vazio sse SIMILAR_A (D4.10)"
  },
  "payload.invalidation": { "reason": "(ato AUTORIZADO — CKG-004/009; nunca cascata)" },
  "payload.archival": { "relevance": "(rebaixamento sob gate E3 — CKG-012)", "reason": "" },
  "payload.canonical_state_transition": {
    "canonical_model": "CHM-001 | CEM-001 | CCM-001 (FIXO pelo node_type — D4.16)",
    "canonical_ref": "canonical_id@version",
    "status_from": "= canonical_status corrente (D4.16)",
    "status_to": "∈ enum do modelo; (status_from,status_to) ∈ grafo CHM-001 l.744-757 / CEM-001 l.460-466; CCM-001: só ∈ enum",
    "successor_ref": "canonical_id@version da sucessora — OBRIGATÓRIO para CEM-001 com status_to=SUPERSEDED (l.450); opcional [PROPOSTA] local para CHM/CCM; se presente, deve resolver",
    "transition_timestamp": "", "transition_origin": "", "justification": "(CEM-001 l.428)"
  },
  "payload.collision": {
    "relation_a_ref": "record_id da creation da relação vigente (deve resolver)",
    "relation_b_ref": "record_id da creation em admissão (gravada na mesma unidade — D4.18)",
    "contradiction_pair": "CONFIRMA×REFUTA (§D2.2)",
    "overlap_window": "[início, fim) da interseção das janelas efetivas (D4.13)",
    "detected_at": "", "note": "ambas preservadas; resolução = SPEC-007/SPEC-018 ou governança"
  },
  "kg_gate_decision": {
    "_comentario": "LOG de decisões (formato próprio, fora do kg_record); append-only e IMUTÁVEL (RULE-CKG-006; EC-CKG-002) — D4.5",
    "decision_id": "ÚNICO e imutável", "submission_id": "", "gate_id": "CKG-001|005|006|008|009|010|013|...", "gate_version": "",
    "input_digest": "", "result": "PASS | DENY | INDETERMINADO", "reason": "ex.: PATH_A_ADMISSION_PENDING",
    "judgment_invocations": "0 | 1 (D4.11)", "writer_id": "identidade de serviço do runtime dos gates", "decided_at": ""
  }
}
```
> Nenhum campo computa convicção nem deriva de custo (INV-04). Mecanismo físico = INDETERMINADO (H-001 ABERTA).

---

## Enforcement Contracts

### EC-CKG-001 — Escrita de nó/relação no KG permanente [E3]
```
CAPABILITY   : Escrever um nó/relação válido no KG permanente
EFFECT       : Persistência de conhecimento permanente (commit crítico/irreversível; append-only; unidade atômica)
PRECOND      : D4.15 (caminho §D2.3 com contrato DEFINIDO e satisfeito — pendência de (a), do selo (b), de (c), do host do juízo
               ou caminho inexistente NÃO satisfaz ⇒ DENY) AND EC-CKG-003 AND D4.1/D4.14 AND D4.12 AND D4.2 AND D4.17 AND D4.16
               AND D4.10/D4.11 AND D4.3/D4.4
POSTCOND     : unidade atômica D4.18 gravada (creation + DERIVA_DE + collision se houver) ou nada; estado derivado ACTIVE_KNOWLEDGE;
               versão anterior preservada e não-mutada em caso de supersessão
POLICY       : RULE-CKG-001/002/003/005/006/008/010/013; INV-CKG-02; CEM-001 l.608-615; CC-02; ENF-04
LEVEL        : E3 (Crítico — "KG publicado → E3 mínimo", atomic-spec §10.2 l.238; irreversível)
FAILURE-MODE : Fail-closed — precondição falha OU pendente ⇒ REJECTED; nada persistido; `kg_gate_decision`. Falso-DENY E3: limiar = gap
               aberto (atomic-spec l.273/l.393) — CONDICIONAL. DENY por pendência (§D2.3) é DENY por desenho, NÃO falso-DENY
EVIDENCE     : `kg_record`s conformes a D4.3/D4.4 + método ENF-07: AMOSTRA de `kg_gate_decision` DENY reavaliada por re-execução
               determinística do gate sobre a entrada registrada (input_digest) + revisão humana; tamanho/limiar = gap aberto
```

### EC-CKG-002 — Imutabilidade / append-only / versionamento (conhecimento E log de decisões) [E3]
```
CAPABILITY   : Impedir deleção/mutação de `kg_record` e de `kg_gate_decision` e garantir transições versionadas
EFFECT       : Transição por NOVO registro (SUPERSEDED/ARCHIVED/INVALIDATED_IN_TIME) — nunca remoção nem reescrita; log só cresce
PRECOND      : (operação ∉ {DELETE físico, UPDATE de registro}, em ambos os repositórios) AND (D4.3 ∧ D4.4 para registro de
               conhecimento; `decision_id` único para o log — D4.5)
POSTCOND     : histórico de conhecimento e de decisões preservado e reconstruível por replay (T17); estado = D4.7; um só formato
               de registro de conhecimento; nenhum registro removido/mutado (INV-07; INV-CBP-01)
POLICY       : RULE-CKG-004/006/012; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01; INV-CKG-01
LEVEL        : E3 (Crítico — perda/reescrita de histórico é irreversível; o log é a EVIDENCE dos EC E3 e da amostragem ENF-07:
               mutá-lo destruiria a prova de conformidade de forma irreversível; economicidade não rebaixa — ENF-02)
FAILURE-MODE : Fail-closed — tentativa de DELETE/UPDATE ⇒ negada; a negação é nova decisão no log. Falso-DENY E3 CONDICIONAL até limiar (ENF-07)
EVIDENCE     : `kg_gate_decision` de cada tentativa bloqueada; `gate_decision_mutated == false` (BASpec-CKG-006 caso (b)); ENF-07
```

### EC-CKG-003 — Governança de escrita (autorizado + autenticado; não redefine ontologia) [E3]
```
CAPABILITY   : Admitir escrita só de escritor autorizado/autenticado, sem redefinição de ontologia pelo produtor
EFFECT       : Autorização (ou recusa) de escrita permanente no KG
PRECOND      : (allowlist DEFINIDA — mantenedor [DECISÃO NECESSÁRIA]; indefinida ⇒ DENY `WRITER_ALLOWLIST_UNDEFINED`) AND (escritor ∈
               allowlist ∧ identidade AUTENTICADA — SPEC-004 CBP-014; auth indisponível/falha ⇒ não-autorizado) AND (operação ∉
               {redefinir ontologia/taxonomia global} — SAS-001 §6.12) AND (gate determinístico — ENF-03)
POSTCOND     : só escritor autorizado escreve; produtor registra relações, não redefine ontologia (ato de governança)
POLICY       : RULE-CKG-009; SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04
LEVEL        : E3 (Crítico — escrita em memória permanente; cruza fronteira de confiança)
FAILURE-MODE : Fail-closed — escritor não autorizado / falha de auth / tentativa de redefinir ontologia ⇒ negada; log. Falso-DENY E3 CONDICIONAL (ENF-07)
EVIDENCE     : `kg_gate_decision` da autorização (identidade autenticada; motivo do DENY) + amostragem de falso-DENY (ENF-07)
```

### EC-CKG-004 — Guard de custo E confiança (D4.12; INV-04 custo como base) [E3]
```
CAPABILITY   : Manter a confiança de relação em namespace próprio e impedir custo/confiança no nó ou nas arestas de `conviction`
EFFECT       : Guard (na escrita do KG) sobre o payload de `conviction` e as relações com destino `conviction`
PRECOND      : D4.12 (payload de conviction fechado ∧ nenhuma relação calibration_metric→conviction ∧ relation_confidence só em relação)
POSTCOND     : nenhum campo além dos permitidos no nó conviction; nenhuma relação calibration_metric→conviction escrita
POLICY       : RULE-CKG-007; INV-04 (custo); CCM-001
LEVEL        : E3 — o guard decide ADMITIR/RECUSAR escrita no KG permanente (piso "KG publicado → E3", atomic-spec l.238; ENF-02)
FAILURE-MODE : Fail-closed — violação de D4.12 ⇒ negada; log. Falso-DENY E3: método do EC-CKG-001; limiar = gap aberto — CONDICIONAL
EVIDENCE     : `kg_gate_decision` com reason ∈ {CONFIDENCE_IS_NOT_CONVICTION, ONTOLOGY_INTEGRITY_VIOLATION} + amostragem (ENF-07). Que o
               CÁLCULO de convicção (SPEC-003/CCM-001) não consuma a confiança é requisito à SPEC-003 / [DECISÃO NECESSÁRIA] — fora do KG
```

### EC-CKG-005 — Registro de relação causal/de similaridade (RULE-CAU) [E3]
```
CAPABILITY   : Admitir CAUSA só com os campos de D4.10 (inclusive posthoc_flag explícito) e SIMILAR_A só com similarity_basis
EFFECT       : Escrita (ou recusa) de TODA relação CAUSA/SIMILAR_A, qualquer produtor/caminho — persistência permanente (E3)
PRECOND      : D4.10 AND (se há juízo) D4.11
POSTCOND     : relações causais/de similaridade têm campos auditáveis (presença — limite m5); nenhuma submissão consome mais de
               uma invocação do juízo; host pendente ⇒ nenhuma invocação
POLICY       : RULE-CKG-008; RULE-CAU-01/02/03; RULE-INQ-03 (RULES.md l.678); atomic-spec §10.6 l.315; ENF-03
LEVEL        : E3 (Crítico — write permanente; herda EC-CKG-001)
FAILURE-MODE : Fail-closed — campos ausentes ou gate reprovado ⇒ rejeitada; submissão ENCERRA em INDETERMINADO; KG sem retry/sem
               memoização. Limite versionado com RULE-CKG-008. Falso-DENY E3 CONDICIONAL (ENF-07)
EVIDENCE     : `judgment_invocations` ≤ 1 e retries gerados pelo KG = 0 no `kg_gate_decision`; outcome INDETERMINADO; presença, não
               veracidade (ENF-03); amostragem de falso-DENY (método do EC-CKG-001)
```

### EC-CKG-006 — Consulta cognitiva / Cognitive Trace Reconstruction (read-only)
```
CAPABILITY   : Responder consultas e reconstruir a cadeia cognitiva COMPLETA sem alterar estado
EFFECT       : Leitura/navegação de nós e relações (sem escrita)
PRECOND      : (consulta é read-only). Autorização de LEITURA: não há regra definida neste Plan — política de acesso de leitura
               = [DECISÃO NECESSÁRIA] (n7); não é declarada como precondição verificada
POSTCOND     : resposta/trace COMPLETO (D4.8) retornado; nenhum registro criado ou alterado pela consulta
POLICY       : RULE-CKG-011; CEM-001 l.608-615/l.612-614; SAS-001 §6.12
LEVEL        : E1 (Contratual — leitura observável; não muta estado)
FAILURE-MODE : Consulta que tente gravar ⇒ negada; completude do trace é obrigatória; eficiência de consulta ampla = INDETERMINADO até H-001
EVIDENCE     : contagem de registros antes/depois da consulta (`records_created_by_query == 0`); trace = fecho transitivo D4.8
               (log de consulta NÃO é afirmado — não especificado)
```

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
Serviço lógico de **memória semântica permanente** (Opção A — camada sobre o conhecimento já validado/publicado): gates
Classe C (ontologia, proveniência, imutabilidade, governança E3, fronteira, guard custo/confiança, colisão) + mecânica
Classe D (catálogo, bitemporal, lifecycle, trace) + juízo Classe H com gate de saída (similaridade/causalidade). **Não
guarda trabalho, não transporta, não forma conhecimento, não decide, não computa convicção, não executa ordem, NÃO
escolhe o mecanismo físico (H-001 ABERTA).** [FONTE: ROADMAP §6; CEM-001 l.608-615; SAS-001 §6.12; research.md §3/§4]

### Roteamento de modelo (CEE-001 §5)
Gates C/D **não requerem LLM**. O juízo (Classe H, CKG-008) pode usar apoio semântico **apenas como detector** para
PROPOR; o gate de saída D4.10 é **determinístico** (ENF-03); host do juízo = [DECISÃO NECESSÁRIA] (até lá, 0 invocações).
Mecanismo físico = **INDETERMINADO = H-001 (ABERTA)**. [FONTE: CEE-001 §5; ENF-03; H-001 ABERTA]

### Dependências técnicas
Os baselines do bloco INHERITS (com as linhas lá citadas) · SPEC-007 (selo — [DECISÃO NECESSÁRIA]) · atomic-spec v1.5 ·
ENF-01..08. Referências [EXTERNO], não-baseline: research.md §2 (SRC-ZEP-01, SRC-PROV-01, SRC-MEMVSKG-01, SRC-FORGET-01 —
DADO não-verbatim) e §5 (REPO-graphiti/graphrag/cognee/mem0 — elegíveis, nenhum adotado).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Over-engineering: banco de grafos por inércia do nome "Graph" | Opção A; Opção B ADIADA (research.md §3.5); H-001 (ABERTA); ADV-CKG-09 |
| Fixar H-001 por engano | contrato cognitivo independe de H-001; ADV-CKG-09; CONS-01 |
| Invadir/absorver a SPEC-007 | Non-goal; CKG-010 (selo); ADV-CKG-08 |
| Reabrir/duplicar SPEC-004/005 | CC-02; cobertura×lacuna; INV-09; ADV-CKG-10 |
| Confiança de relação virar Convicção / custo no nó de convicção | D4.12; EC-CKG-004; ADV-CKG-03/05; T06 |
| Deleção/mutação disfarçada de "esquecimento" (conhecimento ou log) | INV-07; RULE-CKG-006/012; EC-CKG-002 (E3); ADV-CKG-01/13/15 |
| Causalidade pós-hoc / sem regime | D4.10 (`posthoc_flag` explícito); EC-CKG-005; ADV-CKG-04 |
| Colisão resolvida em silêncio / `collision` pendurado por admissão parcial | D4.13/D4.18; EC-CKG-001; ADV-CKG-02; T11/T21 |
| Escrita sem proveniência / produtor redefine ontologia / auth falha-aberto | D4.2; CKG-009; EC-CKG-001/003 (E3); ADV-CKG-06/07 |
| Discriminantes de proveniência/produtor declarados falsamente a montante | limite declarado (D4.2/D4.14: forma, sem lookup); coincidência com o canônico = contrato de (a) [DECISÃO NECESSÁRIA] |
| Redefinir contrato canônico | CKG-002; EC-CKG-001; ADV-CKG-11; CC-02 |
| Violar matriz de integridade (ex.: ICT origina) | D4.1/D4.14; EC-CKG-001; ADV-CKG-12/17; INV-02 |
| Trace incompleto / consulta que muta | D4.8; EC-CKG-006; ADV-CKG-14; CEM-001 l.612-614 |
| LLM como gate de escrita/causalidade | ENF-03; EC-CKG-003/005 (detector≠gate) |
| Ontologia inconsistente / mudança sem governança | §D2.1; governança spec-time (SPEC-019)/runtime (K-001 [DECISÃO NECESSÁRIA]); CKG-009 |
| Crescimento ilimitado da memória | lifecycle versionado (CKG-012); observabilidade = SPEC-040 (por referência) |
| Admissão por caminho com contrato vacuoso/pendente | fail-closed por caminho (§D2.3; D4.15; EC-CKG-001/003); T09/T20; ADV-CKG-21. **Custo declarado:** até as decisões de Andraus o KG não admite NENHUMA escrita de conhecimento — limitação assumida em favor de Conformidade/Eficácia (4Es) |
| Transição canônica perdida trava o sujeito | limite declarado (D4.16 n8); reconciliação = [DECISÃO NECESSÁRIA] |
| Juízo em laço (custo/latência sem fim) | D4.11; EC-CKG-005; ADV-CKG-20 |
| Mutação in-place abaixo da camada lógica não detectada | limite declarado (RULE-CKG-006, m3): sem digest; detecção física = H-001/BUILD |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** introduz o schema lógico do registro de nó/relação do KG e do log de decisões; nenhum schema canônico nem das SPEC-004/005 alterado.
- **RAG/KG:** especifica o contrato do próprio KG; formação/retrieval permanece em SPEC-007.
- **Skills:** nenhuma Skill afetada; INV-06 preservado.
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

- **CKG-001 (C):** se errada → violação da matriz, hypothesis.school=ICT, PRIMARY com school≠Elliott, `school` não derivável ou HERDA→pai não-PRIMARY persistidos → observável por predicado D4.1/D4.14. Negação: ADV-12/17, T01, T20(c); positivo cross-escola: T15 (convenção (v)). QUANDO-sim-mas-ENTÃO-não: `producer_id` declarado falso — não observável pelo KG (limite de forma, §D2.1).
- **CKG-002 (D):** se errada → contrato redefinido, observation=evidence, enum trocado, elo de versão ausente/não resolvido, transição ilegal aceita → observável (T02, T17, ADV-11, ADV-19 d/e). QUANDO-sim-mas-ENTÃO-não: transição de conviction fora de qualquer tabela — NÃO rejeitar por legalidade (CCM-001 sem tabela). Ponta-a-ponta: INDETERMINADO ((a) pendente).
- **CKG-003 (D):** se errada → relação sem tipo/direção/proveniência, ou evidence DERIVED com ancestral ausente aceita → observável. Negação: ADV-12/16, T03, T19.
- **CKG-004 (D):** se errada → registro existente mutado/deletado → `existing_record_mutated=true`. Negação: ADV-13, ADV-19(f), T04.
- **CKG-005 (C):** se errada → registro sem `computed_by`, ou discriminante ausente/inconsistente aceito, OU gate_record/lineage forçados sem gate/ancestral → observável por D4.2. Negação: ADV-06(a–e), T14; caso-feliz: T12/T16. QUANDO-sim-mas-ENTÃO-não: hipótese PRIMARY sem gate — o gate NÃO deve exigir gate_record/lineage (T16).
- **CKG-006 (C/E3):** se errada → DELETE/UPDATE em `kg_record` ou `kg_gate_decision`, registro sem identidade/versão, ou dois formatos de colisão → observável. Negação: ADV-01/19, T05, T17.
- **CKG-007 (C/E3):** se errada → campo extra no nó conviction ou relação calibration_metric→conviction aceitos → observável por campo/node_type (D4.12). Limite: texto livre. Negação: ADV-03/05, T06.
- **CKG-008 (H):** se errada → CAUSA sem mecanismo/regime/`posthoc_flag` escrita, SIMILAR_A sem base aceita, ou >1 invocação / retry → observável (`judgment_invocations`). Negação: ADV-04/20/22, T07, T18. QUANDO-sim-mas-ENTÃO-não: SIMILAR_A duplicada inversa — no-op (T18 d).
- **CKG-009 (C):** se errada → auth falha-aberto, allowlist indefinida tratada como aberta, produtor redefine ontologia → observável. Negação: ADV-07, T08, T20(d).
- **CKG-010 (C):** se errada → admissão por caminho pendente ou sem caminho → observável; **verificáveis só os DENY** (T09, T20, ADV-21); admissão POSITIVA = INDETERMINADO. QUANDO-sim-mas-ENTÃO-não: formado COM selo — hoje NÃO admitido.
- **CKG-011 (D):** se errada → trace incompleto ou consulta grava → `trace_complete=false` / `records_created_by_query>0`. Negação: ADV-14, T10.
- **CKG-012 (D):** se errada → versão anterior removida/mutada → observável. Negação: ADV-15, T13.
- **CKG-013 (C):** se errada → contraditória sobrescrita, colisão falsa (origens distintas/janelas efetivas disjuntas), colisão fora do envelope, ou `collision` gravado sem a creation → observável. Negação: ADV-02/18/19, T11, T17, **T21**.

**Cobertura de verificabilidade:** as 13 BASpecs têm ENTÃO verificável **como PREDICADO de gate ou sobre fixture** e ≥1 negação em D8. **Nenhuma** tem admissão POSITIVA fim a fim verificável hoje (§D2.3 ⇒ INDETERMINADO).

**Bloco B — herança obrigação-a-obrigação (CC-08):** evidência por obrigação herdada:
- CEM-001 "trace COMPLETO" (l.614) → CKG-011 + INV-CKG-02 (D4.8; T10); não redefine.
- CEM-001 "preservar TODOS os estados" (l.613/l.494 — **da Evidência**) → **PARCIAL:** formato verificável por fixture (`canonical_status` + `canonical_state_transition` com legalidade — CKG-002; T17; ADV-19 e); admissão por (a) fail-closed ⇒ ponta-a-ponta **[DECISÃO NECESSÁRIA]** (bloqueada a montante, não enfraquecida — RULE-HD-03). **Extensão a hipótese/convicção = [PROPOSTA] local, NÃO herdada** (N10), em conflito com o critério mínimo de (a) — [DECISÃO NECESSÁRIA].
- CEM-001 "preservar TODAS as versões" (l.612; l.594-595; sucessora l.450) → **PARCIAL:** elos tipados D4.16 (`successor_ref` obrigatório para Evidência; predecessor obrigatório para hipótese — CHM-001 l.588); versões do PRÓPRIO KG: `supersedes` (D4.4; T13). Teste: T17 + ADV-19(d). Ponta-a-ponta depende de (a) = **[DECISÃO NECESSÁRIA]**.
- CEM-001 Cap.5 `Lineage`/`Evidence Origin Type`/`Producer*` → DERIVA_DE + `provenance_ref.lineage` + discriminantes espelhados (D4.2/D4.14) — espelho de FORMA (limite declarado).
- CHM-001 (estados/versionamento/provenance) → CKG-002/012 por referência; D4.16 (l.588); não transiciona.
- CCM-001 → D4.12/EC-CKG-004 isolam custo e confiança (INV-04); elo de versão por [INFERÊNCIA] (l.58).
- SPEC-004 v1.2 INV-CBP-01 + publicação atômica (plan l.381/l.689) → CKG-004/006/012 + D4.18; `gate_record` reatribuído à SPEC-004.
- SPEC-005 (eventos) → consumo/emissão = [DECISÃO NECESSÁRIA]; SAS-001 §6.12/l.924 → CKG-009/EC-CKG-003, caminho (c) = [DECISÃO NECESSÁRIA].
- RULE-BB-004/INV-07 → CKG-006/012 (inclusive o log); RULE-CAU-01/02/03 → D4.10 (`posthoc_flag` explícito).
- CEE-001 l.111 → **PARCIAL:** isolamento verificável (D4.12; ADV-05; T06); ARMAZENAMENTO não demonstrado — caminho `ENTRY_PATH_UNDEFINED` = **[DECISÃO NECESSÁRIA]**.
- atomic-spec §10.2 ("KG publicado → E3") → EC-CKG-001..005 em E3; §10.6 l.315 + RULE-INQ-03 → D4.11.
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (único MODIFIED = RULE-BB-004 reforçada — RULE-HD-02).
**Eixo VERTICAL (RULE-HV) não aplicável.**

**Bloco C — epistêmico / disciplinas N8–N17:**
- **RULE-EPI-01..03:** **achados corrigidos** — v1.3–v1.5 converteram INDETERMINADO em PASS em (a)/(b)/allowlist (corrigido na v1.5); **v1.6 (N1):** a v1.5 afirmava como fato a ausência da ata DHR-BACKLOG-001 e um estado superado do BL-011 — falso; corrigido com âncora (ata §1; RMR-001 l.102/110/191); **v1.6 (N10):** obrigação da Evidência apresentada como herdada para hipótese/convicção — reetiquetada [PROPOSTA]. H-001 = INDETERMINADO; nenhuma hipótese tratada como fato.
- **RULE-SEM-01/04:** sem achado — acepções declaradas (CC-10), inclusive as duas de "PRIMARY" (Termo 5).
- **RULE-ONT-01/02:** verificado — ontologia explícita (§D2.1); `ontological_status` para nós teóricos (RULES.md l.672); "relação" não é node_type (n3); alteração por governança. Sem achado residual.
- **RULE-INQ:** verificado — questões abertas formuladas como [DECISÃO NECESSÁRIA]; RULE-INQ-03 aplicada (D4.11).
- **RULE-CAU-01/02/03:** sem achado — D4.10 exige os campos e o `posthoc_flag` explícito; presença ≠ veracidade (ENF-03).
- **RULE-CTF:** verificado — nenhuma afirmação contrafactual carregada; o Bloco A usa o "se estivesse errada" só como teste de verificabilidade.
- **RULE-UNC-01..03:** sem achado — incerteza localizada (eficiência de consulta ampla até H-001); completude do trace NÃO é incerta.
- **RULE-PRB:** sem achado — nenhuma probabilidade/precisão numérica; confiança de relação = PARÂMETRO a calibrar.
- **RULE-DEC-01:** sem achado — o KG armazena/relaciona/consulta; não decide nem executa (INV-05).
- **RULE-MET-01:** sem achado — nenhuma proveniência fabricada (discriminantes explícitos, não inferidos); IDs arXiv implausíveis descartados (research.md); SRC-FORGET-01 é DADO não-verbatim e não sustenta sozinha alegação carregada; o mapeamento R-04..R-06 é [INFERÊNCIA] declarada, não fato.

**Bloco D — reforço de escopo:** a Spec **preserva/relaciona/consulta** conhecimento permanente, **não guarda trabalho**
(SPEC-004), **não transporta** (SPEC-005), **não forma conhecimento** (SPEC-007), **não executa** ordem (INV-05/RULE-DEC-01),
**não decide** nem **computa** convicção. Nenhuma BASpec cruza a fronteira SOT→execução downstream. Toda dependência de
decisão de Andraus está marcada [PROPOSTA]/[DECISÃO NECESSÁRIA] na tabela de etiquetagem (fonte única), não fechada.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001; CHM-001; CCM-001; CEE-001; SAS-001; SPEC-004 v1.2; SPEC-005 v1.0; SPEC-001/019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5 (§10.2 E3); RULES v1.5 (RULE-BB-004, RULE-CAU-01/02/03, RULE-INQ-03, RULE-MECH-01, RULE-HD-*); INV-*; ENF-*; CONSTITUTION l.191-192/l.233 | [FONTE] | FATO NORMATIVO |
| DHR-BACKLOG-001 (`governance/DHR-BACKLOG-001_Ata_Promocao_BL003_BL011_ATIVADO.md`): BL-003/BL-011 `ATIVADO`, encaminhados ao gate da SPEC-006 (RMR-001 l.102/110/191) | [FONTE] | Decisão de Andraus registrada (chat 2026-10-17); a ata declara o merge como ratificação |
| CLASSIFICACAO-COLISOES-BL010-011-012; CONFLICT-MAP l.143-147 (COL-EXP-01..05) | [FONTE] | FATO NORMATIVO (DHR-BL010-011-012-001) |
| Correspondência R-04..R-06 → conteúdo (fronteiras CLASSIFICACAO l.58-60) | [INFERÊNCIA] | Rótulos não são catálogo fechado (CLASSIFICACAO l.23) |
| RULE-CKG-001..013; INV-CKG-01/02; §D2.1/§D2.2/§D2.3; D4.1–D4.18; envelope `kg_record`; log `kg_gate_decision`; campos locais (`school`, `produced_by_gate`, elos de versão); BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Fontes SRC-ZEP-01/PROV-01/MEMVSKG-01; REPO-graphiti/graphrag/cognee/mem0 | [EXTERNO] | Referência — DADO, nunca baseline |
| SRC-FORGET-01 (sumário WebSearch) | [EXTERNO] | DADO **não-verbatim** — não sustenta sozinha alegação carregada |
| Mecanismo físico de armazenamento | [DECISÃO NECESSÁRIA] | **H-001 — EM ABERTO — não fechar** (Andraus) |
| Banco de grafos dedicado (Opção B) | [DECISÃO NECESSÁRIA] | **ADIADO** — registrado, não apagado (INV-07) |
| Escala numérica de confiança de relação | [DECISÃO NECESSÁRIA] | **PARÂMETRO a calibrar** — INDETERMINADO (não toca J-001/N-001) |
| Contrato do selo — caminho (b) | [DECISÃO NECESSÁRIA] | Dependência da **SPEC-007**; DENY `SEAL_CONTRACT_UNDEFINED` |
| Critério/produtor/gatilho do caminho (a); coincidência `producer_id`/discriminantes ↔ objeto canônico | [DECISÃO NECESSÁRIA] | DENY `PATH_A_ADMISSION_PENDING`; [PROPOSTA] mínima só para hypothesis |
| Extensão de "todos os estados/versões" a hipótese/convicção × critério mínimo de (a) que exclui EMERGENT/CANDIDATE | [PROPOSTA] × [PROPOSTA] em conflito → [DECISÃO NECESSÁRIA] | Só a Evidência tem a obrigação herdada (CEM-001 l.494/612) |
| Contrato do caminho (c) (SAS-001 l.924) | [DECISÃO NECESSÁRIA] | DENY `ENTRY_PATH_UNDEFINED` |
| Caminho de nós asset/timeframe/regime/observation/calibration_metric/structure/narrative/mission | [DECISÃO NECESSÁRIA] | DENY `ENTRY_PATH_UNDEFINED`; CEE-001 l.111 PARCIAL |
| Mapeamento `producer_id` → `school` (SMC/Fibonacci/ICT/Fractal) | [PROPOSTA] (tabela) / [DECISÃO NECESSÁRIA] (ids) | Só Elliott conhecido (SPEC-001 l.203) ⇒ demais `SCHOOL_UNDERIVABLE` |
| R-07 / COL-EXP-05 (EXP-SPEC-021 ↔ RAG-SPEC-018) e reconciliação da fila EXP-SPEC-001..053 (BL-011 `ATIVADO`) | [DECISÃO NECESSÁRIA] | Onde reconciliar: gate SPEC-006, SPEC-009 ou com SPEC-007 (Andraus) |
| Estado do BL-003 após este Plan (`ATIVADO` até H-001/G-001 ou tratado na homologação) | [DECISÃO NECESSÁRIA] | Andraus; RMR-001 não editado |
| Limiar/amostra de falso-DENY (ENF-07) | [DECISÃO NECESSÁRIA] | Gap aberto (atomic-spec l.273/l.393); só o método está declarado |
| Mantenedor da allowlist / host do juízo CKG-008 / migração de ontologia | [DECISÃO NECESSÁRIA] | DENY `WRITER_ALLOWLIST_UNDEFINED`; host pendente ⇒ 0 invocações |
| Política de autorização de LEITURA (EC-CKG-006) | [DECISÃO NECESSÁRIA] | Não especificada; não declarada como precondição verificada |
| Reconciliação de transição canônica perdida (D4.16) | [DECISÃO NECESSÁRIA] | Hoje fail-closed (trava o sujeito) |
| Consumidor/contrato de consumo de `Evidence.Invalidated`; emissão de evento pelo KG | [DECISÃO NECESSÁRIA] | SPEC-005 transporta; consumidor/emissão não definidos |
| Reatribuição do critério de promoção (S14) à SPEC-018/K-001 | [DECISÃO NECESSÁRIA] | Proposta a Andraus, não fato |
| Componente "Cognitive Ontology" separado | [DECISÃO NECESSÁRIA] | Ontologia DENTRO da SPEC-006 (Q-ABERTURA-4) |
| Volume do Plan / eventual divisão (Q-ABERTURA-5) | [DECISÃO NECESSÁRIA] | Andraus; ver checks.md §11-bis item 8 |
| Estados do Blackboard p/ não-hipótese; fórmula/pesos/limiares e pesos por ativo do Conviction Vector; estado por agente; ciclo P12; EARS multi-condição; convicção macro-global | [DECISÃO NECESSÁRIA] | **M-001, J-001, N-001, G-001, K-001, C-001, WF-D03 — EM ABERTO** — não tocadas |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] ROADMAP.md lido: SPEC-006 confirmada (§6/§21); FASE 3, após SPEC-005 BASELINE v1.0.
[x] atomic-spec.md lido: método v1.5 (CC-11/CC-12; RULE-MECH-01; RULE-ECC-04/06; §15 Dossiê; §3 CRITICAL·D0–D7; §10.2 l.238 "KG publicado → E3").
[x] Nenhum invariante congelado violado (INV-01..10). INV-04/05/06/07/09/10 reforçados; INV-CKG-01 cobre também o log de decisões.
[x] Constitution Check CC-01..CC-12 (N/A justificados CC-06/07/12; CC-02/08/09/10/11 INCIDEM e aplicados).
[x] Disciplinas N8–N17: §7-bis Bloco C.
[x] Referências externas [EXTERNO] classificadas; nenhuma adotada; verbatim em sources/ (RULE-ECC-04); RULE-ECC-06 (4 elegíveis); sem pesquisa web nova nesta rodada.
[x] RULE-ECC-05: NÃO-incidência (DHR-SPEC006-001 §2); conformidade WORKFLOW por prudência; WF-D03 não tocada.
[x] Spec sem implementação (BUILD adiado); Plan derivado da abertura homologada; Tasks adiadas.
[x] EARS (20); BASpecs (13) com Classe (CC-11); toda RULE citada existe ou está etiquetada [PROPOSTA]; códigos de rejeição definidos em D4.
[x] Profundidade D0–D7 (+ D8 focado): §D2.1–§D2.3; D4.1–D4.18; D5; D6 (11 passos + 5-bis/5-ter); D7 x21; D8 x22; D9.
[x] Enforcement Contract em todo ato com efeito (EC-CKG-001..006); E3 em 001..005 (002 cobre o log); E1 em 006; ENF-07 método amostral, limiar = gap aberto.
[x] Status epistemológico e etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicados; documentado ≠ homologado.
[x] CONS-01: H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 permanecem ABERTAS; nenhuma usada como invariante fechado.
[x] Achados da rodada 7 (N1–N11, n1–n9) tratados — rastreabilidade em checks.md §11.
[x] Integridade: nenhuma fonte inventada; linhas verificadas nesta rodada: DHR-BACKLOG-001 §1-§2; RMR-001 l.102/110/128/191/192; CLASSIFICACAO l.23/51-62; CONFLICT-MAP l.143-147; CEM-001 l.258-283/351-356/450/494/608-615; CHM-001 l.283/361/588; CCM-001 l.58/75-78/125; SPEC-004 plan l.264-267/l.381/l.689; atomic-spec l.238.
[x] 4Es na ordem; Conformidade > Eficácia. Latência não material (consulta opcional/não-bloqueante — SAS-001 §6.12).
[x] Dependências a montante homologadas; selo SPEC-007 = dependência [DECISÃO NECESSÁRIA]. "VERIFY" ≠ CONFORME ≠ homologação.
[x] §7-bis (EUA-E18) preenchido (Blocos A–D).
[x] CC-11/§10.6: Classe por BASpec; C com gate de saída; H (CKG-008) com bounded loop D4.11 + gate D4.10.
[x] Abertura (RULE-ECC-01/02/04/06): Dossiê presente e HOMOLOGADO (DHR-SPEC006-001).
[x] Passo 11-bis: BL-003/BL-011 `ATIVADO` (DHR-BACKLOG-001; RMR-001 l.102/110/191) — encaminhamento item a item na Nota de gate; BL-010 tangente; BL-029 `Em espera`; RMR-001 não editado.
[ ] Gate determinístico e demais scripts: **NÃO executados por mim (sem Bash)** — listados em checks.md §12 para o Orquestrador.
```

---

**Pronto para revisão.**

**[DECISÃO NECESSÁRIA] / abertas (não fechadas — CONS-01):** lista ÚNICA na tabela "Etiquetagem e Status Epistemológico".
H-001 permanece ABERTA (recorte proposto, não decidido); J-001/N-001/M-001/G-001/K-001/C-001/WF-D03/ECC-03-001 não tocadas.

Carregado para o Revisor (rodada 7):
- **Limitação funcional declarada:** hoje o KG **não admite nenhuma escrita de conhecimento** (§D2.3); verificáveis são predicados de gate e fixtures; admissão positiva fim a fim = INDETERMINADO.
- **Fonte única:** predicados/códigos em D4.1–D4.18; demais representações citam. Respostas às 8 interpelações: checks.md §11-bis. Baselines que citam o KG tratadas **sem erratum** (INV-09).
- **Volume (Q-ABERTURA-5):** número de linhas e justificativa em checks.md §11-bis item 8; a divisão é decisão de Andraus — o Especificador **não** divide por conta própria.
