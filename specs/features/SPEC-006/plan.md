# SPEC-006 — Cognitive Knowledge Graph

| Campo | Valor |
|---|---|
| ID | SPEC-006 — Cognitive Knowledge Graph (contrato cognitivo da **memória semântica permanente** do SOT — ontologia enxuta + entidades/relações tipadas + temporalidade + proveniência por referência + lifecycle + confiança de relação + consulta cognitiva + governança de escrita; **mecanismo físico de armazenamento INDETERMINADO — H-001 ABERTA**) |
| Versão | 1.11 (ERRATA PROPOSTA — proposta como Minor/aditiva sobre a baseline v1.7, classificação a decidir por Andraus [n-c]; INV-07: nada apagado, v1.7 preservada no changelog) |
| Status | **BASELINE v1.7 — ERRATA v1.11 PROPOSTA (aguarda Revisor e Andraus); a v1.7 segue vigente até a homologação da errata.** (DHR-SPEC006-002) A v1.7 foi **HOMOLOGADA — BASELINE v1.7** (Andraus, 2026-10-13, DHR-SPEC006-002; abertura DHR-SPEC006-001; parecer do Revisor CONFORME COM RESSALVAS); a errata v1.8 incorporou as correções A-01..A-14 da auditoria independente (`governance/propostas/AUDITORIA-INDEPENDENTE-SPEC006/RELATORIO.md` §3); a errata v1.9 incorporou as correções N-01..N-06 do parecer do Revisor sobre a v1.8; a **errata v1.10** incorpora as correções N-07 (Média) + m-A..m-D (Menores) do parecer do Revisor sobre a v1.9 — **aditiva, Minor, nenhuma regra apagada**; a **errata v1.11** incorpora N-08 (Média) + n-a/n-b/n-c (Menores) do parecer do Revisor sobre a v1.10 (`governance/propostas/PARECER-REVISOR-SPEC006-v1.10-2026-10-17.md`) — propagação, sem regra nova (a classificação "Minor/aditiva" é de Andraus — n-c). RULE-CKG-001..013 e INV-CKG-01/02 vigentes por homologação da v1.7 (registro físico em `RULES.md` diferido — RULE-HG-02). **H-001 (mecanismo físico do KG) permanece ABERTA — nem a v1.7 nem esta errata a fecham** (CONS-01; só Andraus). M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 seguem ABERTAS; **CKG-STRUCT-ORIGIN-001 (N-01/N-09) ABERTA** (BL-035). **A-05 (governança): H-001 ficou sem dono após a homologação da v1.7; o re-apontamento (ROADMAP §6 / atomic-spec §12 / revisor.md §8) é decisão de Andraus — esta errata NÃO escolhe a dona** (ver nota A-05 no bloco de decisões abertas). |
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

**Status epistemológico de cabeçalho:** a SPEC-006 é a **camada Harness/operacional da memória permanente** sobre responsabilidades que os canônicos BASELINED já atribuem ao KG (CEM-001 l.608-615 Responsabilidades do KG; l.489-497 tabela "Consumo pelos Componentes" — estados da EVIDÊNCIA, A-03; l.562-565 Cognitive Trace Reconstruction; CONSTITUTION l.233 EC-COG-003; SAS-001 §6.12; CEE-001 l.111). **NÃO redefine** CHM-001/CEM-001/CCM-001, nem reabre SPEC-004/SPEC-005 (**CC-02/CONST-01/INV-09**). **H-001** permanece **ABERTA**. [FONTE: ROADMAP §6/§7; atomic-spec §12; DHR-SPEC006-001 §3]

### Histórico de versões

| Versão | Data | Alterações (1 linha) |
|---|---|---|
| 1.0 | 2026-10-11 | Entrega candidata inicial (Opção A; mecanismo físico INDETERMINADO = H-001). 13 BASpecs, 6 EC, 13 EARS, 11 cenários, 10 adversariais. |
| 1.1 | 2026-10-12 | Rodada 2: STRUCT-10; §7-bis Bloco C; escrita → E3; duas fontes sob governança única; DERIVA_DE; matriz de integridade; estado = projeção derivada. 13 cenários, 15 ADV. |
| 1.2 | 2026-10-12 | Rodada 3: HERDA cross-escola; `provenance_ref.lineage`; `canonical_status`+transição; admissão [DECISÃO NECESSÁRIA]; INV-CKG-02; §D2.2 colisão; bitemporal. 14 cenários, 16 ADV, INV-CKG-01/02. |
| 1.3 | 2026-10-12 | Rodada 4: T01 corrigido + T15; campo único `school`+`hierarchy_role`; `gate_record` condicional; colisão §D2.2; admissão por estado. 15 cenários, 18 ADV. |
| 1.4 | 2026-10-12 | Rodada 5 (9 Maiores + 8 Menores): proveniência condicional; admissão por estado-por-tipo [PROPOSTA]; `to_node==conviction` proibido; `posthoc_flag` determinístico; versionamento sem fork; §D3.1. 16 cenários, 21 ADV. |
| 1.5 | 2026-10-12 | **Rodada 6 — CONSOLIDAÇÃO + 6 Maiores + Menores.** Regra definida UMA vez (RULE-CKG/BASpec, fonte única); EARS/D4/D6/EC/T/ADV/Herança/checks só referenciam por ID. M-01 preservação "a partir da admissão" (MODIFIED) + conviction {COMPUTED,GATED_PASS,GATED_BLOCK,SUPERSEDED}; M-02 aciclicidade invertida; M-03 trace completo só p/ Evidência (hipótese [PROPOSTA]); M-04 outcome_ref/outcome_timestamp obrigatórios (ou no_outcome); M-05 `computed_by`(produtor autenticado)≠`writer_id`(committer); M-06 `school` de structure + natural_key completo; Menores m-02..m-12. Contagem preservada: 13 BASpecs, 6 EC, 13 EARS, 16 cenários, 21 ADV, INV-CKG-01/02. |
| 1.6 | 2026-10-12 | **Rodada 7 — 1 Maior (N-01) + Menores N-02..N-09.** N-01 (opção (a) de Andraus): `school`/`hierarchy_role` SÓ para `hypothesis`; `structure` não deriva school nem origina ORIGINA; SAS-001 §6.12 não é fonte de school → [DECISÃO NECESSÁRIA] CKG-STRUCT-ORIGIN-001 + BL-035. N-02 `outcome_timestamp` derivado do `recorded_at` do `outcome_ref` (OUTCOME_TIMESTAMP_INVALID) + no_outcome×outcome_ref (NO_OUTCOME_CONFLICT). N-03 T17/ADV-22 computed_by≠writer_id (commit direto DENY) + admissão por tipo evidence/conviction (ADV-21). N-04 EXPECTED_VERSION_REQUIRED/VERSION_CONFLICT (códigos SPEC-004), record_kind de relação sem `collision`, CANONICAL_CONTRACT_REDEFINITION_FORBIDDEN. N-06 REFUTED só CHM (SUPERSEDED/ARCHIVED também na Evidência). N-07 reconciliação INV-CKG-02×CKG-003 + timeout bounded [DECISÃO NECESSÁRIA] + self-loop proibido. N-08 colisão INVALIDA×alvo = marcação (não rejeição) + cond.(v) alvo ainda vigente. N-09 `school=Fractal` sem produtor (CKG-STRUCT-ORIGIN-001). Contagem: 13 BASpecs, 6 EC, 13 EARS, **17 cenários (T01..T17)**, **22 ADV**, INV-CKG-01/02. |
| 1.7 | 2026-10-13 | **Reconciliação BL-011 / MC-EXP-001 (DHR-BACKLOG-ABERTURA-001).** Nova seção curta cruzando EXP-SPEC-001..053 + tratamentos X-01/X-04/R-01..R-07 contra os RULE-CKG: memória semântica → REFERÊNCIA (CKG existentes, sem duplicar); memória episódica → FORA (SPEC-007/018/K-001); COL-EXP-01..05 REFLETIDOS/ADIADOS. BL-011 na Nota de gate atualizado de "Pendente" para resultado real (Disposição PARCIAL preservada). Nenhuma regra nova; nenhuma decisão aberta fechada. Contagens inalteradas: 13 BASpecs, 6 EC, 13 EARS, 17 cenários, 22 ADV, INV-CKG-01/02. **(HOMOLOGADA — BASELINE v1.7, DHR-SPEC006-002; permanece vigente até a homologação da errata v1.8.)** |
| 1.8 | 2026-10-16 | **ERRATA PROPOSTA (Minor/aditiva — INV-07: nada apagado; v1.7 preservada acima).** Incorpora A-01..A-14 da auditoria independente (`governance/propostas/AUDITORIA-INDEPENDENTE-SPEC006/RELATORIO.md` §3): A-01 pós-hoc por `formulated_at` (instante de FORMULAÇÃO, não `recorded_at` corrente; RULE-CKG-008/EARS-8/BASpec-008/D4/schema/T16(+caso positivo)/ADV-04/EC-005); A-02 admissão por TRAJETÓRIA (só objeto que esteve em ACTIVE; `TRAJECTORY_NEVER_ACTIVE`; opção conservadora [PROPOSTA], conhecimento negativo = [DECISÃO NECESSÁRIA]; RULE-CKG-010/T09/ADV-21); A-03 RETIRADO o MODIFIED sobre CEM-001 l.494 (premissa falsa — l.494 é estados da EVIDÊNCIA; regra de preservação vira LOCAL em CKG-010; Herança/Delta); A-04 RULE-CKG-001 fail-closed de hypothesis (`canonical_ref≠null`∧`producer∈AUTHORIZED_PRODUCERS`∧`school` derivável∧`PRIMARY⇒Elliott`∧proíbe via selo (b); T18/T19/ADV-23); A-05 nota de governança (H-001 sem dono — re-apontamento é de Andraus; NÃO escolhe dona); A-06..A-09 âncoras corrigidas (CBP-007 l.264-270; RMR por ID/âncora; R-8 em ABERTURA §10; RULES ONT-01 l.671/ONT-02 l.672; CONSTITUTION l.191/192; SPEC-005 l.971; CEM-001 l.606); A-10 `target_relation_id` na chave natural da relação; A-11 INVALIDA+fechamento de `valid_to` = ato ATÔMICO (cond.(v) independe de ordem); A-12 arestas de SAÍDA mínimas p/ conviction/narrative (nenhuma PARA conviction — INV-04) + calibration_metric isolamento intencional [PROPOSTA]; A-13 ADV-08/09/10 e falso-DENY de BASpec-009 reclassificados como checagem de REVISÃO/spec-time; A-14 guard de ESCRITA (EC-004 E3) separado do guard de LEITURA (EC-006 E1). Contagens: 13 BASpecs, 6 EC, 13 EARS, **19 cenários (T01..T19)**, **23 ADV (ADV-01..23)**, INV-CKG-01/02. Nenhuma decisão aberta foi tocada; H-001 permanece ABERTA. |
| 1.9 | 2026-10-16 | **ERRATA PROPOSTA (Minor/aditiva — INV-07: nada apagado; v1.7 segue vigente).** Incorpora N-01..N-06 do parecer do Revisor sobre a v1.8 (2 Média + 4 Menores). **N-01** (Média) predicado de trajetória de admissão (RULE-CKG-010) redefinido POR TIPO — hypothesis: esteve em ACTIVE∨DOMINANT (CHM-001); evidence: esteve em ACTIVE (CEM-001 l.258-262); conviction: esteve em COMPUTED∨GATED_PASS (CCM-001 l.58/78) — corrigindo o predicado global "ACTIVE" que degenerava toda conviction; prova da trajetória vem de `canonical_history_ref` (campo do node_record, resolvido no canônico CHM/CEM/CCM, nunca do payload; ausência ⇒ `CANONICAL_HISTORY_UNRESOLVABLE`); T09 positivo por tipo + ADV-21 negativo por tipo. **N-02** (Média) `formulated_at` (RULE-CKG-008): núcleo causal (`mechanism`/`direction`/`conditions`/`regime`) IMUTÁVEL na cadeia `supersedes` (`CAUSAL_CORE_IMMUTABLE_IN_CHAIN`; correção do núcleo exige NOVA afirmação causal com `formulated_at` próprio — fecha racionalização pós-hoc por reescrita); REMOVIDA a alternativa "`recorded_at` da hipótese referenciada" (sem campo/precedência, permitia antedatar); ADV-04 caso (g). **N-03** (Menor) propagação por referência: BASpec-CKG-001/EARS-1/EC-CKG-001 PRECOND (fail-closed de hypothesis A-04); BASpec-CKG-010/EARS-10/D4/D6 passo 2 (trajetória por tipo); Autopré-check corrigido (T09 positivo; TRAJECTORY_NEVER_ACTIVE em ADV-21). **N-04** (Menor, checks) alinha §5/§6/§11 ao M-01 RETIRADO (A-03); omite contagem de linhas estimada; §8 lista citações novas. **N-05** (Menor) RULE-CKG-013 desambigua A-11: INVALIDA AUTORIZADA (fecha `valid_to` atomicamente ⇒ não colide) vs INVALIDA CONTESTADA/PENDENTE (sem fechamento ⇒ admitida e MARCADA, cond. (v) alcançável — escolha conservadora: admitir+marcar, N-08); alinha D6 passo 7/ADV-18. **N-06** (Menor) matriz DEPENDE_DE declara pares admitidos ((hypothesis\|mission)→(hypothesis\|evidence); conviction→(evidence\|hypothesis); narrative→(evidence\|hypothesis)); narrative→hypothesis "agrega" etiquetado [INFERÊNCIA]; citação BASpec-CBP-007 corrigida l.543-559→l.543-565. Contagens: 13 BASpecs, 6 EC, 13 EARS, **19 cenários (T01..T19)**, **23 ADV (ADV-01..23)**, INV-CKG-01/02. Nenhuma decisão aberta foi tocada; H-001 permanece ABERTA. |
| 1.10 | 2026-10-16 | **ERRATA PROPOSTA (Minor/aditiva — INV-07: nada apagado; v1.7 segue vigente).** Incorpora N-07 (Média) + m-A..m-D (Menores) do parecer do Revisor sobre a v1.9. **N-07** (Média): admissão de `conviction` NEGADA por padrão fail-closed (`CONVICTION_HISTORY_UNDEFINED`) — o CCM-001 (l.58/78) define só o enum `status`, sem tabela de transições/estado inicial/registro timestamp-origem-justificativa, e o Cap.5 (l.117) deixa M-001 ABERTA; o predicado de trajetória e o `canonical_history_ref` de `conviction` passam a [PROPOSTA]/[DECISÃO NECESSÁRIA] (pré-req: histórico de status da conviction no CCM-001/SPEC-003 + M-001 — de Andraus, ALHEIAS a esta Spec); removida toda atribuição "CCM-001 mantém histórico"; T09(c)/ADV-21(g) refletem a negação; arestas de SAÍDA de `conviction` na matriz (A-12) permanecem válidas como esquema, mas nó `conviction` só aparece no grafo quando a decisão for tomada; hypothesis/evidence inalterados. **m-A**: núcleo causal imutável na cadeia `supersedes` (RULE-CKG-008) estendido para incluir `outcome_ref` e `no_outcome` (ADV-04 caso (h)). **m-B**: EARS-8 e VERIFICADO POR de BASpec-CKG-008 alinhados por referência a `CAUSAL_CORE_IMMUTABLE_IN_CHAIN`. **m-C**: subcódigo `CAUSAL_CORE_IMMUTABLE_IN_CHAIN` movido para pai próprio em §D3.1 (não é campo faltante); caminho legítimo de correção do núcleo causal declarado (INVALIDA a CAUSA antiga + NOVA CAUSA com `valid_from`/`formulated_at` próprios ⇒ chave natural distinta, sem falso dedupe/DENY). **m-D**: para `evidence` o predicado "esteve em ACTIVE" é defesa em profundidade (não defeito), pois CEM-001 l.446-447 define ACTIVE como estado padrão e l.460-466 só permite saídas a partir de ACTIVE (ADV-21(f) cobre histórico corrompido/não-resolvível). Contagens: 13 BASpecs, 6 EC, 13 EARS, **19 cenários (T01..T19)**, **23 ADV (ADV-01..23)**, INV-CKG-01/02. Nenhuma decisão aberta foi tocada; H-001 permanece ABERTA. |
| 1.11 | 2026-10-18 | **ERRATA PROPOSTA (INV-07: nada apagado; v1.7 segue vigente).** Incorpora o parecer do Revisor sobre a v1.10 (N-08 Média + n-a/n-b/n-c Menores), sem regra nova. **N-08**: núcleo causal imutável (incl. `outcome_ref`/`no_outcome`, RULE-CKG-008/m-A) propagado ao GATE DE SAÍDA e ao ENTÃO do BASpec-CKG-008 (fecha m-A/m-B), ao PRECOND do EC-CKG-005 (E3) e ao esquema `causal`. **n-a**: checks §17 (linha N-07) ganha assert-absent das duas formulações superadas (atribuição de histórico ao CCM-001; trajetória de conviction pelo status COMPUTED); rastreio em checks §18. **n-b**: ADV-21(f) alinhado à RULE-CKG-010 e à tabela de transições do CEM-001 l.460-466 (ACTIVE não é único predecessor de ARCHIVED). **n-c**: negação de `conviction` por padrão registrada como decisão de Andraus no chat (2026-10-17) SEM ata — a ata de homologação da errata deve registrá-la; classificação Minor/aditiva = decisão de Andraus. Contagens inalteradas: 13 BASpecs, 6 EC, 13 EARS, 19 cenários (T01..T19), 23 ADV, INV-CKG-01/02. Nenhuma decisão aberta tocada; H-001 ABERTA. |

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; DHR-SPEC006-001 §3/§4; DHR-SPEC006-PEND-001; ABERTURA §8/§9; RMR-001 BL-029 + nota DHR-SPEC006-PEND-001 (citados por ID/âncora, não por linha — A-07)]

- **Nenhum item do RMR-001 tem gatilho `spec:SPEC-006` homologado isoladamente.** O início da redação **satisfaz ramos de gatilho** de itens pré-existentes — **tratado como reflexo; promoção/encaminhamento é do gate e de Andraus** (o Especificador NÃO promove — CONS-01).
- **BL-003** (persistência física de hipótese/estado) — `Em espera`, gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação`. **Disposição: PARCIAL** — vinculado à SPEC-006 por regra desde a abertura (DHR-BACKLOG-ABERTURA-001), sem depender de promoção. **Incorporado:** o contrato LÓGICO da memória permanente do KG (o que se grava, versionamento, proveniência, governança de escrita — RULE-CKG-*). **Fora:** a parte **física** (mecanismo de armazenamento) **É** H-001 (ABERTA) / G-001 (ABERTA) → permanece INDETERMINADA, decisão de Andraus (CONS-01); o estado do item no painel não muda (`Absorvido` é de Andraus).
- **BL-011** (MC-EXP-001) — `Em espera`, gatilho inclui `spec:SPEC-006 em redação`. **Disposição: PARCIAL** — vinculado por regra desde a abertura; **fonte de requisitos** sob COL-EXP-01..05 (CONFLICT-MAP; prevalece SOT canônico). **Incorporado (já refletido neste Plan):** confiança de relação ≠ Convicção (RULE-CKG-007; INV-04), imutabilidade/append-only (INV-07), fronteira KG × Blackboard (Working Memory = SPEC-004). **Reconciliado (v1.7 — ver seção "Reconciliação BL-011 / MC-EXP-001" abaixo):** a fila EXP-SPEC-001..053 (aberta e lida em `reference/camadas/CAMADA MEMÓRIA.MD` l.818-1038) e os tratamentos X-01/X-04/R-01..R-07 foram cruzados contra os RULE-CKG. Resultado honesto: **(i)** os concernentes à memória **SEMÂNTICA permanente** (imutabilidade, versionamento, proveniência, temporalidade, integridade, conflito, duplicidade, referência ao canônico) já são cobertos por RULE-CKG-001/002/004/005/006/010/012/013 — tratados por **REFERÊNCIA**, não duplicados (CC-02/INV-09); **(ii)** os de memória **EPISÓDICA/experiência** (retrieval, outcome/performance, decisão/execução, lição/feedback, estratégia, harness) são **FORA** → SPEC-007 (retrieval), SPEC-018/K-001 (aprendizado/evolução), Experiência (*"nunca misturar"*); **(iii)** os tratamentos COL-EXP-01..05 estão todos **REFLETIDOS** ou **ADIADOS** conforme `CONFLICT-MAP.md` (prevalece SOT canônico). **Nenhuma lacuna exigiu nova RULE-CKG.** Os resíduos são **[DECISÃO NECESSÁRIA] pré-existentes** (critério de decaimento/valor/retenção → K-001/SPEC-018, já em S14; produtor/gatilho de promoção trabalho→permanente, já em CKG-010; dup. EXP-SPEC-021↔RAG-SPEC-018 ADIADA a SPEC-007/009 — COL-EXP-05). Classificação ≠ aplicação; o estado no painel **NÃO muda** (`Absorvido` é de Andraus).
- **BL-010** (MC-RAG-001) — `Em espera`, gatilho `spec:SPEC-007 em redação` ∨ `milestone:FASE 3 iniciada`. BL-010 é fonte da **SPEC-007** → **tangente**; a SPEC-006 respeita a fronteira. **Não promovo**.
- **BL-029** (proveniência) — **`Em espera`** (DHR-SPEC006-PEND-001; gatilho `spec:SPEC-014`/`SPEC-018`/`SPEC-045`; o gatilho `spec:SPEC-004` foi CONSUMIDO). **Independente desta Spec** — não absorvido nem promovido. [FONTE: RMR-001 BL-029 / nota DHR-SPEC006-PEND-001 — por ID/âncora, A-07]
- **Pendência de procedência [n-c, v1.11]:** a NEGAÇÃO por padrão da admissão de `conviction` (`CONVICTION_HISTORY_UNDEFINED`, N-07) foi decidida por Andraus **no chat em 2026-10-17** e, até esta versão, **NÃO há ata que a registre** — o único registro é `governance/propostas/HANDOFF-SPEC006-2026-10-17.md` (dado de estado, não ata; AGENTS.md §11). **A ata de homologação da errata DEVE registrá-la** (AGENTS.md §10: a assinatura é a decisão registrada no chat **e citada na ata**); até lá, as menções "decisão de Andraus" neste Plan são [FONTE: chat 2026-10-17, sem ata] e não FATO NORMATIVO. **Observação para Andraus:** a baseline v1.7 admitia `conviction` por estado; a negação RESTRINGE isso — a classificação desta errata como "Minor/aditiva" é **decisão de Andraus**, não do Especificador.
- O passo 11-bis pleno ocorre na homologação do Plan.

---

## Reconciliação BL-011 / MC-EXP-001 (DHR-BACKLOG-ABERTURA-001; COL-EXP-01..05)

[FONTE: `reference/camadas/CAMADA MEMÓRIA.MD` (MC-EXP-001) l.818-1038 — [EXTERNO], DADO, nunca baseline (INV-09/TRACE-06); `governance/CLASSIFICACAO-COLISOES-BL010-011-012.md` §2; `governance/CONFLICT-MAP.md` (COL-EXP-01..05); RMR-001 BL-011]

> **Nota de termos:** "REFERÊNCIA" nas tabelas abaixo = *coberto por RULE-CKG existente, referenciado por ID* — NÃO é a Disposição homônima do RMR-001 §4-bis (fonte de requisitos sem absorver). A Disposição do BL-011 é **PARCIAL**.

> **Fronteira semântica (chave da reconciliação).** O MC-EXP-001 é a camada de **Experiência e Memória** — predominantemente memória **EPISÓDICA** (o que aconteceu em operações: eventos, desfechos, desempenho, lições). A SPEC-006 é a memória **SEMÂNTICA permanente** (conhecimento validado + relações auditáveis). *"Nunca misturar"* (KERNEL-V2). Por isso a maioria das EXP-SPEC é **FORA** do KG; só os invariantes transversais de memória (imutabilidade, proveniência, temporalidade, versionamento, integridade, conflito, duplicidade, referência ao canônico) têm análogo no KG — e já são cobertos por RULE-CKG existentes (tratados por **REFERÊNCIA**, não duplicados — CC-02/INV-09).

### A. Fila EXP-SPEC-001..053 → destino

| Grupo (§ MC-EXP) · EXP-SPEC | Conteúdo | Destino | Base (ID — não duplicar) |
|---|---|---|---|
| §38 Foundations — 001,003,004 (Capability/Event/Context) | contrato/evento/contexto de EXPERIÊNCIA | **FORA** → camada de Experiência (episódica) | *"nunca misturar"*; INV-06 |
| §38 Foundations — 002 Record, 005 Identity, 006 Provenance, 007 Temporal | registro/identidade/proveniência/temporal | **REFERÊNCIA** (invariantes transversais) | RULE-CKG-002 (id+versão), RULE-CKG-005 (proveniência), RULE-CKG-004 (bitemporal) |
| §39 Resultados — 008-012 (Outcome/Error/Success/Performance/Regime) | desfechos/métricas de experiência | **FORA** → Experiência/SPEC-018; CAUSA só REFERENCIA desfecho via `outcome_ref`, não o modela | RULE-CKG-008 (`outcome_ref`); INV-04 (`performance`≠Convicção) |
| §39 Resultados — 013 Decision Trace, 014 Execution Trace | traço de decisão/execução | **FORA** → KG não decide nem executa; execução é downstream | INV-05/RULE-DEC-01 |
| §40 Retrieval — 015-020, 022 (Retrieval/Similar/Contrasting/Temporal/Regime/Relevance/Packet) | recuperação/relevância/packet | **FORA** → SPEC-007 (RAG); KG só consulta read-only; Experience Packet PROJETA CEM (não redefine) | RULE-CKG-011 (read-only); CC-02 (CKG-002) |
| §40 Retrieval — 021 Experience Independence | independência/duplicação inter-camada | **ADIADO** (COL-EXP-05/R-07): dup. EXP-SPEC-021↔RAG-SPEC-018 → SPEC-007/009 | CONFLICT-MAP COL-EXP-05 |
| §41 Retenção/Integridade — 027 Archival, 030 Historical Immutability, 031 Versioned Interpretation, 053 Memory Versioning | arquivamento/imutabilidade/versão | **REFERÊNCIA** (núcleo do KG) | RULE-CKG-006 (append-only/INV-07), RULE-CKG-012 (SUPERSEDED/ARCHIVED/versão), RULE-CKG-004 |
| §41 — 029 Memory Integrity, 034 Memory Contamination | integridade/contaminação | **REFERÊNCIA** | RULE-CKG-001 (ontologia/integridade), RULE-CKG-005 (proveniência), RULE-CKG-010 (admissão: formado sem selo rejeitado), RULE-CKG-009 (E3) |
| §41 — 032 Memory Conflict | conflito entre registros | **REFERÊNCIA** | RULE-CKG-013 (detecta + preserva ambas; §D2.2) |
| §41 — 033 Duplicate Detection | duplicidade | **REFERÊNCIA** | RULE-CKG-012 (dedupe: mesma chave natural sem `supersedes` divergente ⇒ DENY; reescrita idêntica = no-op) |
| §41 — 023 Retention, 024 Value, 025 Decay, 026 Critical Preservation, 028 Compression | retenção/valor/decaimento/compressão | **FORA + [DECISÃO NECESSÁRIA]** → o KG nunca deleta (INV-07; "esquecimento" = arquivamento versionado) e rebaixa `relevance`; o **critério** de decaimento/valor/retenção/compressão NÃO é do KG | RULE-CKG-006/012; S14 (já **[DECISÃO NECESSÁRIA]** → K-001/SPEC-018) |
| §42 Integração Conhecimento — 035-037 (Exp→Knowledge/Knowledge→Exp/Hypothesis→Exp) | formação de conhecimento a partir de experiência | **FORA** → SPEC-007/SPEC-018 (formação); o KG recebe o **publicado** via selo; produtor/gatilho de promoção = **[DECISÃO NECESSÁRIA]** | RULE-CKG-010 (selo; nota [DECISÃO NECESSÁRIA]) |
| §43 Integração Cognição — 038-040 (Exp→Cognition/Presentation/Counterevidence) | entrega/apresentação/contraevidência | **FORA** → consumidor (SPEC-003/cognição); KG oferece só consulta; contraevidência usa CONFIRMA/REFUTA já no catálogo | RULE-CKG-011; §D2.1 (CONFIRMA/REFUTA); INV-05 |
| §44 Integração Learning — 041-044 (Exp→Learning/Lesson/Feedback/Experimentation) | lição/feedback/experimentação | **FORA** → SPEC-018/K-001 | K-001 (ABERTA) |
| §45 Memória Estratégica — 045-049 (Strategy/Performance History/Regime History/Failure+Success Pattern) | experiência/padrões estratégicos | **FORA** → Experiência/SPEC-018; SE publicado como `learning`, entra via selo (CKG-010) e relaciona por `ESTATISTICA_DE` (catálogo) — mas a **formação do padrão** é SPEC-018, não o KG | RULE-CKG-010; §D2.1 (`learning`/ESTATISTICA_DE) |
| §46 Harness — 050-052 (Harness/Benchmark/Economicity) | harness/benchmark da camada | **FORA** → SPEC-021 (RULE-MM)/SPEC-018 | SPEC-021 |

### B. Tratamentos X-/R- (COL-EXP-01..05) → destino

| Tratamento · COL | Decisão de colisão (CONFLICT-MAP) | Situação na SPEC-006 |
|---|---|---|
| X-01 · COL-EXP-01 — status "BASELINE"/"BASELINE PROPOSTA" | REJEITAR efeito → PROPOSTA/ref. externa | **REFLETIDO** — MC-EXP-001 é [EXTERNO]/DADO (research.md; `sources/`); nenhum efeito de baseline (INV-09). |
| X-04 · COL-EXP-04 — Working Memory §7.6 | ADIAR/RELOCAR → SPEC-004 | **REFLETIDO** — Non-goal "memória de trabalho"; EMERGENT/CANDIDATE excluídos da admissão (CKG-010 — regra LOCAL, A-03); *"nunca misturar"*. |
| R-01 · COL-EXP-02 — Quality Gates G0–G8 | REJEITAR namespace global; ADAPTAR local | **REFLETIDO** — SPEC-006 usa maturidade L0–L4 / nível-alvo L3 (RULE-MM, SPEC-021); não adota o namespace G. |
| R-02/R-03 · COL-EXP-03 — I-EXP-01..12 / EXP-P01..P14 | ADAPTAR como LOCAIS ancorados nos canônicos | **REFLETIDO por referência** — I-EXP-01/07 (imutabilidade)=INV-07/RULE-CKG-006; I-EXP-08=RULE-MET-01 (CKG-005/008); I-EXP-09 (sem autoridade decisional)=INV-05/RULE-DEC-01; EXP-P03=RULE-EPI (CC-09); EXP-P04=RULE-CAU-03 (CKG-008). Nenhum invariante global novo criado. |
| R-04/R-05/R-06 — `confidence`≠Conviction/J-001; Experience Packet projeta CEM | CONFORME (fronteiras) | **Fronteira CONFORME refletida** (aplicação formal conforme CLASSIFICACAO-COLISOES §2, linha de R-04..R-06: adiada à ativação) — confiança ≠ Convicção = RULE-CKG-007/INV-04; **J-001 permanece ABERTA**; Experience Packet projeta CEM = CC-02 (CKG-002). |
| R-07 · COL-EXP-05 — EXP-SPEC-021 ↔ RAG-SPEC-018 (dup.) | ADIAR reconciliação → SPEC-007/009 | **ADIADO** — fronteira RAG respeitada (retrieval=SPEC-007); a dup. não é reconciliada aqui (fora do escopo do KG). |

### C. Lacunas e resíduos (honestidade)

- **Nenhuma lacuna de memória semântica exigiu nova RULE-CKG** — todo concern KG-relevante do MC-EXP-001 mapeia a RULE-CKG já definida (seção A). Por isso **nenhuma regra foi criada** nesta rodada (footprint mínimo).
- **Resíduos = [DECISÃO NECESSÁRIA] pré-existentes** (não novos; não fecháveis aqui — CONS-01): (1) critério de decaimento/valor/retenção/compressão (EXP-SPEC-023/024/025/028) → **K-001/SPEC-018** (já em S14); (2) produtor/gatilho de promoção trabalho→permanente (EXP-SPEC-035-037) → já **[DECISÃO NECESSÁRIA]** em CKG-010; (3) dup. EXP-SPEC-021↔RAG-SPEC-018 → **ADIADA** a SPEC-007/009 (COL-EXP-05).
- **Disposição final BL-011: PARCIAL** — INCORPORADO o que é memória semântica permanente (por referência a RULE-CKG); FORA o que é memória episódica/experiência (SPEC-007/018/K-001); vínculo preservado; estado no painel inalterado (`Absorvido` é de Andraus).

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o KG é **infraestrutura de memória agnóstica de escola** — armazena conhecimento de qualquer camada (inclusive `HERDA`/`HIERARQUIA_DE`) **sem** alterar a hierarquia nem a autoridade de criação (Elliott cria a primária; ICT não cria — INV-01/INV-02). O KG espelha a hierarquia como relações; não a redefine, interpreta ou decide. [FONTE: INV-01/INV-02; ROADMAP §6]
- [x] **CC-02 — Não redefine Modelo Canônico baselined nem SPEC-004/005:** o KG **preserva** linhagem/versões/estados e faz *Cognitive Trace Reconstruction* **referenciando** os contratos canônicos (CEM-001 l.608-615; l.562-565) — entidades **referenciadas por ID+versão, nunca redefinidas**. CDM-001/CNM-001 pendentes não acionam CONST-01. [FONTE: CC-02; CEM-001; SPEC-004/005 BASELINE]
- [x] **CC-03 — Conviction Vector:** o KG **não computa** convicção; a **"confiança de relação"** é escala própria e **NÃO é** o Conviction Vector; dimensionalidade=8 (fechada) intocada; fórmula/pesos/limiares definitivos **pendentes (J-001 ABERTA)**; **nenhum limiar de convicção é declarado**. [FONTE: INV-03; J-001 ABERTA; N-001 ABERTA]
- [x] **CC-04 — Salvaguardas (CEE-001 §10/§11):** nenhuma violada. O KG não emite sinal, não dimensiona risco, não aplica gates de sinal. **INV-04** (leitura fiel, atomic-spec l.404): o CUSTO nunca entra no Conviction Vector; "Convicção ≠ Score" é cláusula-identidade distinta. A confiança de relação nunca retroalimenta o Conviction Vector (ver RULE-CKG-007). [FONTE: CEE-001 §10/§11; INV-04]
- [x] **CC-05 — Complexidade declarada:** CRITICAL, D0–D7 + D8 adversarial focado.
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A** — o artefato é Spec/Plan; §59/§60 tornam-se obrigatórios nas Tasks/Cards (BUILD adiado — atomic-spec §14). Omissão justificada.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A (idem CC-06); rastreabilidade: ROADMAP §6 → Dossiê (research.md, HOMOLOGADO DHR-SPEC006-001) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente; INHERITS/ADDED/MODIFIED com ID+versão (RULE-HD-04); REMOVED vazio; MODIFIED = só RULE-BB-004 REFORÇADA (não altera texto/significado) — o antigo M-01 sobre CEM-001 l.494 foi RETIRADO por premissa falsa (A-03: l.494 trata estados da EVIDÊNCIA; a preservação "a partir da admissão" é regra LOCAL CKG-010, não MODIFIED), sem contradizer o herdado (RULE-HD-02/03). Eixo VERTICAL (RULE-HV) avaliado e não aplicável. [FONTE: EUA-E04; RULE-HD-02/03/04]
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
    preservar os estados **da EVIDÊNCIA** (l.613 — bullet "preservar todos os estados" dentro de l.608-615; a preservação
    "a partir da admissão" é regra LOCAL do KG em CKG-010, **NÃO MODIFIED de obrigação canônica** — A-03); Cognitive Trace
    Reconstruction COMPLETA da Evidência a partir das relações de Lineage (l.562-565); navegação da cadeia cognitiva (l.615; l.699).
    Proveniência: o campo LOCAL `provenance_ref.lineage` [PROPOSTA] REFERENCIA o campo `Lineage` (CEM-001 Cap.5;
    l.351/539-554) / `derived_from[]` (SPEC-004) — NÃO existe `lineage_ref` no CEM-001. Estados da Evidência =
    ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED (l.258-262 — a Evidência NÃO tem REFUTED). Transições proibidas l.473-475
    (INVALIDATED/ARCHIVED/SUPERSEDED → ACTIVE). O KG CUMPRE; NÃO redefine o CEM (CC-02/INV-10)
  - canon/CHM-001 (BASELINE) — máquina de estados da HIPÓTESE (EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→
    ARCHIVED) e versionamento append-only; o KG ARMAZENA hipóteses por referência, preservando os estados ADMITIDOS;
    REFUTED é EXCLUSIVO do CHM (hipótese); SUPERSEDED/ARCHIVED também existem na Evidência (CEM-001 l.258-262 — N-06). NÃO cria nem transiciona estado de hipótese (isso é SPEC-001/CHM-001)
  - canon/CCM-001 (BASELINE) — objeto Conviction Vector 8D; estados do objeto conviction = COMPUTED/GATED_PASS/
    GATED_BLOCK/SUPERSEDED (l.58/78) — **mas o CCM-001 NÃO define tabela de transições, estado inicial nem registro
    timestamp/origem/justificativa, e o Cap.5 (l.117) deixa M-001 ABERTA; logo a ADMISSÃO de um NÓ `conviction` no KG é
    NEGADA por padrão (`CONVICTION_HISTORY_UNDEFINED` — N-07; decisão de Andraus no chat 2026-10-17, SEM ata ainda — ver
    Nota de gate [n-c]), e esta Spec NÃO atribui ao CCM-001 um
    histórico que ele não define**; a "confiança de relação" é escala PRÓPRIA e NUNCA é o Conviction Vector (INV-04)
  - specs/features/SPEC-004 v1.2 (BASELINE — DHR-SPEC004-003) — memória de TRABALHO (Blackboard); append-only REAL:
    supersessão = PROJEÇÃO DERIVADA (registro histórico NUNCA mutado; sucessora carrega `supersedes`; INV-CBP-01,
    RULE-CBP-003); versionamento OTIMISTA compare-and-commit (RULE-CBP-004 l.239-246: expected_version obrigatório na
    ATUALIZAÇÃO, EXPECTED_VERSION_REQUIRED l.243-245; criação não exige); proveniência `computed_by`/`gate_record`/
    identidade autenticada (RULE-CBP-007 l.264-270; RULE-CBP-014 l.311-319). O KG é memória PERMANENTE, distinta
    ("Nunca misturar"); HERDA a mecânica append-only e a identidade autenticada por referência; NÃO redefine (CC-02/INV-09)
  - specs/features/SPEC-005 v1.0 (BASELINE — DHR-SPEC005-002) — notificação de mudança (Event Bus); **[INFERÊNCIA]** o
    KG pode CONSUMIR eventos de ciclo de vida só como GATILHO de avaliação autorizada (CKG-009), nunca invalidação
    automática (CEM-001 l.602). O tipo `Evidence.Invalidated` É canônico (CEM-001 l.600/722) e a SPEC-005 o TRANSPORTA
    (plan l.88/l.859); a SPEC-005 **não define** o consumidor nem o contrato de consumo pelo KG = **[DECISÃO NECESSÁRIA]**;
    a SPEC-005 fonta do LOG do Blackboard e NÃO escreve no KG (l.971 — A-09; l.242 é o envelope do evento S1). EMISSÃO de eventos pelo KG = [DECISÃO NECESSÁRIA]
  - canon/CEE-001 (BASELINE) l.111 — a métrica de calibração do roteamento "entra no KG"; o KG ARMAZENA como nó (por
    referência), ISOLADA do Conviction Vector (INV-04); não a computa
  - canon/SAS-001 §6.12 (l.923-924) — o Structural Agent atua EXCLUSIVAMENTE como PRODUTOR; registra relações; NÃO
    redefine ontologias/taxonomias. **Escopo FATO NORMATIVO = o Structural Agent.** A EXTENSÃO dessa fronteira a OUTROS
    produtores do KG é **[INFERÊNCIA]/[PROPOSTA]** desta Spec (não é cláusula do SAS-001) — proposta de governança
    uniforme, a homologar. **SAS-001 §6.12 NÃO atribui `school` e NÃO é fonte de `school` de `structure` (N-01):** citado
    só para "produtor registra, não redefine ontologia". (l.163 EC-COG-003: KG "consultado quando necessário… não é
    pré-requisito obrigatório")
  - governance/CONSTITUTION.md l.233 (EC-COG-003) — âncora constitucional; conformar-se, não reescrever (INV-09)
  - governance/RULES.md: RULE-BB-004 (append-only; SUPERSEDED, nunca deletados — l.323) REFORÇADO como imutabilidade
    permanente (INV-07); RULE-CAU-01 (mecanismo — l.680), RULE-CAU-02 (regime — l.681), RULE-CAU-03 (pós-hoc — l.682)
    incidem sobre CAUSA (CKG-008); RULE-ONT-01 (status ontológico — l.671) / RULE-ONT-02 (ontologia extensível por governança — l.672; A-09)
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
  - **[M-01 RETIRADO na errata v1.8 — A-03]** O antigo MODIFIED que "especializava a responsabilidade CEM-001 l.494
    'preservar os estados'" foi **RETIRADO por premissa falsa**: a CEM-001 l.494 é a linha "Knowledge Graph | Todos os
    estados (preservação permanente)" da tabela **"Consumo pelos Componentes" (l.489-497)**, que trata dos **estados da
    EVIDÊNCIA** (ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED — l.258-262), e NÃO impõe obrigação sobre estados de TRABALHO da
    hipótese. EMERGENT/CANDIDATE são estados da **HIPÓTESE** (CHM-001 §4.2) e **nenhuma obrigação canônica (CEM-001/CHM-001)
    exige guardá-los no KG** (grep "Knowledge Graph" no CHM-001 = 0). Logo NÃO há regra canônica a "modificar". A exclusão
    de EMERGENT/CANDIDATE e a preservação "a partir da admissão" permanecem como **regra LOCAL do KG (RULE-CKG-010)**, não
    como MODIFIED de canônico (preserva CC-02/CONST-01 sem premissa falsa — RULE-HD-02/03). O histórico de transições do KG
    começa na admissão; EMERGENT/CANDIDATE não aparecem em `canonical_state_transition_record` do KG (regra local).
    *(INV-07: o texto do antigo M-01 fica registrado neste changelog/auditoria; nada é apagado.)*

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
| Preservar linhagem/versões/estados **dos objetos admitidos**; Trace completo da Evidência | SIM — CEM-001 l.608-615 (Responsabilidades do KG); l.562-565 (l.489-497 = tabela Consumo, estados da Evidência) | ESPECIFICAR verificável (CKG-010/011); referencia CEM; preservação "a partir da admissão" é regra LOCAL CKG-010 (não MODIFIED — A-03) |
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
              INTEGRIDADE §D2.1 (origem/destino, direcionalidade, simetria por tipo). **REGRA DE NÓ `hypothesis` — fail-closed
              [A-04]:** (i) `canonical_ref ≠ null` — senão DENY `HYPOTHESIS_CANONICAL_REF_MISSING`; (ii) `producer ∈
              AUTHORIZED_PRODUCERS` (SPEC-001 l.97/524 = Elliott/SMC/Fibonacci) — senão DENY `HYPOTHESIS_PRODUCER_UNAUTHORIZED`
              (cobre o Structural Agent, que publica "Hipóteses Estruturais" — SAS-001 §6.11 l.920-921 — e não está na
              allowlist de produtor de hipótese); (iii) `school` NÃO derivável do produtor ⇒ DENY `SCHOOL_NOT_DERIVABLE`
              (NUNCA falha-aberto); (iv) `school ≠ ICT` (ICT não cria hipótese — INV-02/RULE-HH-004) ⇒ `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`;
              (v) `hierarchy_role=PRIMARY ⇒ school=Elliott` (só Elliott cria a primária — SPEC-001 RULE-HH-002 l.100; AGENTS §6
              item 2) — senão DENY `PRIMARY_NOT_ELLIOTT`; (vi) `hypothesis` NÃO pode entrar pelo caminho (b) selo SPEC-007
              (`publication.origin=spec007_seal`) — só pelo ciclo de vida canônico (a) — senão DENY `HYPOTHESIS_VIA_SEAL_FORBIDDEN`.
              HERDA só liga SUB a PAI `hierarchy_role=PRIMARY` (RULE-HH-003), e o PAI PRIMARY é necessariamente Elliott (v).
              Violação é REJEITADA (fail-closed — NUNCA falha-aberto por `school` indeterminável). A ontologia é ENXUTA e vive
              DENTRO da SPEC-006. O KG ESPELHA os vínculos já criados pelos agentes; NÃO decide a autoridade de criação (CC-01).
              [Fonte: KERNEL-V2 l.1488-1507; DHR-SPEC006-001 Q-ABERTURA-4; INV-02; SPEC-001 RULE-HH-002 l.100/RULE-HH-003 l.104/RULE-HH-004 l.108/l.97/l.524; SAS-001 §6.11 l.920-921; AGENTS §6 item 2]  [PROPOSTA]

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
              um `evidence` DERIVED EXIGE materializar uma aresta `DERIVA_DE` por ancestral do seu Lineage — a aresta é
              OBRIGATÓRIA e sua AUSÊNCIA no commit é fail-closed (`DERIVA_DE_EDGE_MISSING`); **a ORDEM de chegada ao KG é
              reconciliada em buffer de admissão (INV-CKG-02), NÃO relaxa o fail-closed** (N-07). **ACICLICIDADE [M-02]:** a
              aresta DERIVA_DE não pode fechar ciclo — REJEITA (`LINEAGE_CYCLE`) se a ORIGEM já é alcançável a PARTIR do
              DESTINO seguindo DERIVA_DE (i.e., o destino já descende da origem; adicionar a aresta tornaria a origem
              descendente do que já é seu descendente); o **self-loop (origem == destino)** é caso degenerado do ciclo e é
              PROIBIDO (`LINEAGE_CYCLE`) — N-07. Contradição não é silenciada (CKG-013).
              [Fonte: ROADMAP §6; research.md §4/§8; INV-07; CEM-001 l.565]  [PROPOSTA]

RULE-CKG-004: A mudança de validade de uma relação é ATO AUTORIZADO (CKG-009), NUNCA automática/cascata (CEM-001 l.602; o
              impacto sobre hipóteses/convicções é de CHM/CCM — l.606; CHM-001 l.672-676; A-09). NÃO muta o registro
              existente: grava NOVO registro (invalidação/sucessão) com `recorded_at` e, quando aplicável, `valid_to`
              (`targets_record_id`=R0 referenciado, DISTINTO de `supersedes`). A validade corrente é PROJEÇÃO DERIVADA.
              **Bitemporal:** valid-time (`valid_from`/`valid_to`) + transaction-time (`recorded_at`). Rejeita janela
              inválida `valid_to < valid_from` (`INVALID_TIME_WINDOW`). Convenção: `valid_to = null` ≡ +∞ (vigente).
              Invalidar ≠ deletar (INV-07; espelha SPEC-004 INV-CBP-01).
              [Fonte: research.md §3.1; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.606; CHM-001 l.672-676]  [PROPOSTA]

RULE-CKG-005: Nenhuma entidade/relação existe sem PROVENIÊNCIA, espelhando a condicionalidade de SPEC-004 RULE-CBP-007
              (l.264-270; a BASpec-CBP-007 fica em l.543-565 — A-06/N-06): (a) `computed_by` — identidade AUTENTICADA do PRODUTOR/PROPONENTE (RULE-CBP-014 l.311-319) —
              SEMPRE obrigatório; (b) `gate_record` SÓ quando o objeto resulta de gate; (c) `provenance_ref.lineage`/
              `derived_from` SÓ quando DERIVADO. Para `asset`/`timeframe`/`regime`/`observation` e hipóteses PRIMARY,
              `lineage=[]` é legítimo (NÃO force gate_record/lineage fabricado — RULE-MET-01). Escrita sem a proveniência
              EXIGÍVEL é REJEITADA (`PROVENANCE_MISSING`; subcódigo `COMPUTED_BY_MISSING`). `provenance_ref.lineage`
              [PROPOSTA] referencia `Lineage` (CEM-001 Cap.5)/`derived_from[]` (SPEC-004) — não há `lineage_ref` no CEM-001.
              **Identidade [M-05]:** `computed_by` (produtor autenticado) é DISTINTO de `writer_id` (identidade autenticada
              do COMMITTER — runtime ou serviço do KG); ambos autenticados, não oriundos do payload (ver D6/contrato). A distinção vale para nós/relações propostos por produtor; em registros gerados pelo serviço do KG (collision, transição, arquivamento) `computed_by = writer_id = serviço` por desenho.
              [Fonte: CEM-001 Cap.5; SPEC-004 RULE-CBP-007 l.264-270/CBP-014 l.311-319; research.md §3.2]  [PROPOSTA]

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
              `posthoc_flag` BOOLEANO obrigatório (RULE-CAU-03); correlação/precedência não bastam. **Desfecho [M-04/N-02]:**
              DEVE referenciar o desfecho — `outcome_ref` obrigatório; **`outcome_timestamp` NÃO vem do payload: é DERIVADO
              do `recorded_at` do registro apontado por `outcome_ref` (N-02)** — se vier informado no payload, DEVE coincidir
              e um `outcome_timestamp` do payload posterior ao `recorded_at` do registro apontado é rejeitado
              (`OUTCOME_TIMESTAMP_INVALID`). Quando não há desfecho, exige declaração explícita `no_outcome=true` +
              justificativa (sem desfecho ⇒ `posthoc_flag=false` e nenhuma regra temporal incide); **`no_outcome=true` COM
              `outcome_ref` presente é CONTRADIÇÃO e é rejeitado** (`NO_OUTCOME_CONFLICT`).
              **Instante de FORMULAÇÃO [A-01] — baseline do marcador pós-hoc:** o marcador compara o desfecho com o instante
              em que a AFIRMAÇÃO CAUSAL foi FORMULADA, NÃO com o `recorded_at` do registro CORRENTE. `formulated_at` :=
              `recorded_at` da PRIMEIRA versão da cadeia `supersedes` desta relação causal. **A alternativa anterior ("ou o
              `recorded_at` da 1ª versão da hipótese referenciada como proponente") foi REMOVIDA [N-02]:** não havia campo
              `proponent_hypothesis_ref` nem precedência definida, e ela permitiria ANTEDATAR a formulação (burlar o marcador
              pós-hoc); a opção CONSERVADORA é usar SEMPRE a 1ª versão da própria cadeia `supersedes` da CAUSA.
              **Imutabilidade do núcleo causal na cadeia `supersedes` [N-02 + m-A] (opção conservadora/fail-closed):** uma sucessora
              (cadeia `supersedes`) de uma relação CAUSA NÃO pode ALTERAR o NÚCLEO CAUSAL = `mechanism`/`direction`/`conditions`/
              `regime` **E TAMBÉM `outcome_ref` E `no_outcome` [m-A]** — tentativa é REJEITADA (`CAUSAL_CORE_IMMUTABLE_IN_CHAIN`).
              **Por que `outcome_ref`/`no_outcome` entram no núcleo imutável [m-A]:** sem isso, uma sucessora poderia TROCAR o
              `outcome_ref` por um registro posterior (deslocando o `outcome_timestamp` derivado) ou LIGAR `no_outcome=true` e passar
              com `posthoc_flag=false` — reabrindo exatamente a racionalização pós-hoc que o marcador fecha. Corrigir qualquer item do
              núcleo causal exige uma NOVA afirmação causal (nova relação, com `formulated_at` próprio = seu `recorded_at`), NUNCA uma
              supersessão; assim uma sucessora escrita DEPOIS do desfecho jamais herda um `formulated_at` antigo para um juízo causal de
              fato NOVO e passa com `posthoc_flag=false` (fecha a racionalização pós-hoc por reescrita — RULES.md l.682). Sucessora que só
              corrige campos NÃO-causais (ex.: `relation_confidence`, metadados) herda `formulated_at` legitimamente.
              **Caminho legítimo de correção do núcleo causal [m-C] (chave natural NÃO inclui `mechanism`):** como corrigir o núcleo
              exige uma NOVA CAUSA e a chave natural de relação é `(relation_type, from_node, to_node, target_relation_id, valid_from)`
              — sem `mechanism` —, uma NOVA CAUSA com o MESMO `(from, to, valid_from)` e `mechanism` diferente colidiria no dedupe
              ("divergente sem `supersedes` ⇒ DENY" — CKG-012). O caminho legítimo e conservador é: (1) **APOSENTAR a CAUSA antiga
              errada** via INVALIDA/registro de invalidação bitemporal (`INVALIDA` ou `record_kind=invalidation` fechando o `valid_to`
              — CKG-004/013; a antiga é PRESERVADA, nunca apagada — INV-07) e (2) escrever a **NOVA CAUSA com `valid_from` PRÓPRIO**
              (o instante em que o novo juízo passa a valer) e `formulated_at` próprio — o `valid_from` distinto torna a chave natural
              DISTINTA, eliminando o falso dedupe/DENY. NÃO se altera a chave natural para incluir `mechanism` (opção mais simples e
              conservadora: reusa INVALIDA já existente, sem ampliar a identidade de relação). Usar o `recorded_at`
              do registro corrente seria DEGENERADO: como o registro apontado por `outcome_ref` precisa EXISTIR antes de ser
              referenciado, `recorded_at(CAUSA) > recorded_at(outcome)` SEMPRE — toda causa com desfecho sairia pós-hoc e a
              RULE-CAU-03 ("poderia ter sido formulada ANTES do resultado?") deixaria de ser representável.
              **Regra determinística:** se `formulated_at` > `outcome_timestamp`, então `posthoc_flag` DEVE ser `true`
              (`POSTHOC_FLAG_REQUIRED`); se `formulated_at` ≤ `outcome_timestamp` — a causa PODERIA ter sido formulada antes
              do desfecho (RULE-CAU-03 = SIM) — NÃO é pós-hoc e `posthoc_flag=false` é legítimo (aceito). Faltando qualquer
              campo (incl. `outcome_ref` sem `no_outcome`): rejeita (`CAUSAL_FIELDS_MISSING`; subcódigos
              `POSTHOC_FLAG_REQUIRED`/`OUTCOME_REF_MISSING`/`OUTCOME_TIMESTAMP_INVALID`/`NO_OUTCOME_CONFLICT`). SIMILAR_A
              proposta por juízo exige `similarity_basis`. Classe H: bounded loop (parada) + gate de saída determinístico que
              verifica a PRESENÇA dos campos e a regra de carimbo (não a veracidade — ENF-03).
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
              (CEM-001 l.258-262)** ∈ {ACTIVE, SUPERSEDED, INVALIDATED, ARCHIVED}; **conviction (CCM-001 l.58/78)** = o enum de
              `status` é {COMPUTED, GATED_PASS, GATED_BLOCK, SUPERSEDED} — **porém `conviction` é NEGADO POR PADRÃO [N-07]
              independentemente do status** (ver a regra de NEGAÇÃO abaixo; o enum NÃO habilita admissão enquanto o histórico
              canônico/M-001 não existir) — **EXCLUINDO EMERGENT/CANDIDATE** (ainda TRABALHO — SPEC-004).
              Fora do conjunto (hypothesis/evidence): `CANONICAL_STATUS_NOT_ADMISSIBLE`.
              **Admissão por TRAJETÓRIA [A-02][N-01] [PROPOSTA — opção conservadora/fail-closed]:** o `canonical_status`
              CORRENTE NÃO basta, porque CHM-001 §4.3 (l.744-748) permite EMERGENT→ARCHIVED, CANDIDATE→ARCHIVED e
              CANDIDATE→REFUTED — uma hipótese órfã NUNCA validada (CHM-001 l.379) chegaria como ARCHIVED/REFUTED por puro
              trabalho, contrariando o fundamento da regra ("o KG guarda conhecimento já validado"). Admite-se objeto canônico
              SÓ se sua TRAJETÓRIA de estados demonstra que ESTEVE no **ESTADO DE VALIDAÇÃO DO SEU TIPO** em algum ponto —
              **predicado POR TIPO [N-01]** (o predicado global "esteve em ACTIVE" estava ERRADO: `conviction` NÃO tem estado
              ACTIVE — CCM-001 l.58/78 — e toda conviction sairia `TRAJECTORY_NEVER_ACTIVE`):
                - **hypothesis (CHM-001):** esteve em **ACTIVE** OU **DOMINANT**;
                - **evidence (CEM-001 l.258-262):** esteve em **ACTIVE** (único estado "vivo" da Evidência — não há DOMINANT/REFUTED).
                  **[m-D] Para `evidence`, "esteve em ACTIVE" é DEFESA EM PROFUNDIDADE, NÃO defeito:** o CEM-001 l.446-447 define ACTIVE
                  como ESTADO PADRÃO e a tabela de transições l.460-466 só permite SAÍDAS a partir de ACTIVE (ACTIVE→SUPERSEDED/
                  INVALIDATED/ARCHIVED; e SUPERSEDED/INVALIDATED→ARCHIVED), de modo que qualquer evidence que tenha alcançado um estado
                  não-ACTIVE NECESSARIAMENTE passou por ACTIVE. O predicado é, portanto, tautológico no caminho feliz — ele existe como
                  SALVAGUARDA contra histórico corrompido ou `canonical_history_ref` não-resolvível (ADV-21(f)), não para rejeitar
                  evidence bem-formada;
                - **conviction — admissão NEGADA POR PADRÃO, fail-closed [N-07] [PROPOSTA/DECISÃO NECESSÁRIA]:** o CCM-001 (l.58/78)
                  define `status` APENAS como um enum ({COMPUTED, GATED_PASS, GATED_BLOCK, SUPERSEDED}, "imutável exceto status") —
                  **NÃO** define tabela de transições, estado inicial, nem registro de timestamp/origem/justificativa; e o Cap.5 (l.117)
                  deixa **M-001** (estados do Blackboard para objetos não-hipótese, incl. o Conviction Vector) **ABERTA**. Logo NÃO existe,
                  no canônico, histórico de status da conviction a resolver, e o `canonical_history_ref` de `conviction` NÃO é resolvível
                  por mecanismo definido. Esta Spec NÃO atribui ao CCM-001 um histórico que ele não define: o predicado de trajetória e o
                  `canonical_history_ref` de `conviction` são **[PROPOSTA]/[DECISÃO NECESSÁRIA]** (pré-requisito: histórico de status da
                  conviction no CCM-001/SPEC-003 **E** M-001 — decisões de Andraus, **ABERTAS e ALHEIAS a esta Spec**). **ENQUANTO isso, a
                  admissão de `conviction` no KG é NEGADA por padrão** (`CONVICTION_HISTORY_UNDEFINED`, fail-closed). Alternativa REGISTRADA
                  e DESCARTADA por ora (menos conservadora): admitir `conviction` só com um `canonical_history_ref` resolvível por mecanismo
                  a definir — escolhida a opção CONSERVADORA (NEGAR). As **arestas de SAÍDA de `conviction` na matriz §D2.1 (DEPENDE_DE —
                  A-12) permanecem VÁLIDAS como esquema**, mas um nó `conviction` só APARECE no grafo quando esta decisão for tomada
                  (admissão de conviction resolvida por Andraus); hypothesis e evidence permanecem como definidos acima.
              Quem chega ao KG sem jamais ter passado pelo estado de validação do seu tipo é REJEITADO fail-closed
              (`TRAJECTORY_NEVER_ACTIVE`). **DE ONDE vem a prova da trajetória [N-01]:** NÃO do histórico
              `canonical_state_transition` do KG (que "começa na ADMISSÃO" — não há histórico na 1ª admissão) NEM do payload. A
              admissão EXIGE um `canonical_history_ref` (campo do `node_record`) que REFERENCIA o histórico de estados MANTIDO
              NO PRÓPRIO CANÔNICO (CHM-001 p/ hypothesis; CEM-001 p/ evidence — **para `conviction` NÃO há histórico canônico a
              resolver: ver a regra de NEGAÇÃO POR PADRÃO [N-07] acima; o CCM-001 l.58/78 define só o enum `status`, Cap.5 l.117
              deixa M-001 ABERTA**) e é RESOLVIDO contra ele — nunca derivado do payload (CBP-014). Ausência/irresolubilidade do
              `canonical_history_ref` (para hypothesis/evidence) ⇒ DENY fail-closed (`CANONICAL_HISTORY_UNRESOLVABLE`); submissão de
              `conviction` ⇒ DENY fail-closed (`CONVICTION_HISTORY_UNDEFINED` — N-07). Resolvida a trajetória (hypothesis/evidence),
              o KG grava os estados A PARTIR DA ADMISSÃO em `canonical_state_transition` (A-03). **Alternativa [DECISÃO NECESSÁRIA]:**
              se REFUTED/ARCHIVED vindos SÓ de trabalho DEVEM entrar como CONHECIMENTO NEGATIVO (lição do que foi descartado) é
              decisão de Andraus — NÃO fechada aqui; por ora prevalece a opção conservadora.
              **Preservação de estados — regra LOCAL [A-03] (NÃO é MODIFIED de canônico):** os estados A PARTIR DA ADMISSÃO são
              preservados no KG; EMERGENT/CANDIDATE nunca são admitidos nem registrados no histórico do KG. Isto é regra LOCAL
              de admissão do KG — **NENHUMA obrigação canônica (CEM-001/CHM-001) exige guardar estados de TRABALHO da hipótese
              no KG**; o MODIFIED sobre CEM-001 l.494 foi RETIRADO (A-03; ver Herança/Delta). O PRODUTOR e o GATILHO/EVENTO de
              promoção trabalho→permanente permanecem **[DECISÃO NECESSÁRIA]** (a SPEC-005 não escreve no KG — plan l.971;
              atribuir à SPEC-018/K-001 é proposta a Andraus, não homologada).
              [Fonte: ROADMAP §6/§7; CEM-001 l.258-262; CHM-001 §4.3 l.744-748/l.379; CCM-001 l.58/78; research.md §3.4]  [PROPOSTA]

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
              no commit (compare-and-commit atômico); `expected_version` é OBRIGATÓRIO na atualização — **ausência ⇒
              `EXPECTED_VERSION_REQUIRED`; divergência (expected_version ≠ versão corrente) ⇒ `VERSION_CONFLICT`** (mapeia os
              códigos de origem da SPEC-004 RULE-CBP-004 l.243-244, N-04; não há código próprio `EXPECTED_VERSION_MISMATCH`);
              criação inicial não exige. Proibido FORK (2ª sucessora da mesma versão ⇒ `VERSION_FORK_FORBIDDEN`). Dedupe:
              mesma chave natural sem `supersedes` divergente ⇒ DENY; reescrita idêntica = no-op.
              [Fonte: CHM-001; INV-07; SPEC-004 INV-CBP-01 / RULE-CBP-004 l.239-246; research.md §3.6]  [PROPOSTA]

RULE-CKG-013: Colisão sse duas relações (i) formam PAR CONTRADITÓRIO da tabela §D2.2, (ii) têm ESCOPO coincidente DO PAR
              (CONFIRMA×REFUTA: mesmos `from_node`/`to_node`; INVALIDA×alvo: `INVALIDA.target_relation_id == r2.relation_id`),
              (iii) janelas de validade se SOBREPÕEM e (iv) AMBAS NÃO-SUPERSEDED; **(v) só para INVALIDA×alvo: o alvo `r2`
              PERMANECE VIGENTE apesar da INVALIDA — invalidação autorizada que FECHA a validade de `r2` NÃO colide (N-08)**.
              **Dois modos de INVALIDA [N-05] (desambiguação de A-11 — escolha conservadora: ADMITIR+MARCAR, não rejeitar):**
              (1) **INVALIDA AUTORIZADA** — acompanhada do registro de invalidação bitemporal que FECHA o `valid_to` de `r2`
              (CKG-004). A INVALIDA e o fechamento são o MESMO ATO ATÔMICO (um único commit); a condição (v) é avaliada SOBRE O
              ESTADO RESULTANTE dos dois registros, NUNCA no instante intermediário em que a INVALIDA já existe mas `r2` ainda
              não foi fechado — logo o resultado NÃO depende da ordem de escrita e `r2` torna-se INVALIDATED_IN_TIME/não-vigente
              ⇒ **NÃO colide** (operação normal). (2) **INVALIDA CONTESTADA/PENDENTE** — a relação INVALIDA é afirmada
              (semanticamente, por `evidence`/`learning`) SEM o registro de fechamento do `valid_to` de `r2` (o proponente não
              detém o ato bitemporal autorizado de fechamento). Essa INVALIDA é **ADMITIDA** — o KG PRESERVA, NUNCA rejeita
              (N-08; a INVALIDA sem fechamento NÃO é rejeitada) —, `r2` PERMANECE VIGENTE e então a condição (v) é ALCANÇÁVEL
              ⇒ `collision_record` (MARCAÇÃO não-destrutiva). Assim a colisão (v) surge SÓ no modo contestado/pendente, e a
              atomicidade de A-11 vale SÓ para o modo autorizado — sem contradição.
              O `collision_record` é MARCAÇÃO NÃO-DESTRUTIVA para governança — ambas PRESERVADAS, nunca rejeição/apagamento
              (N-08). Então o KG DETECTA e grava um `collision_record` COM IDENTIDADE/PROVENIÊNCIA PRÓPRIAS
              (`collision_id`/`version`/`computed_by`=`writer_id`=SERVIÇO do KG sob capability de detecção/`recorded_at`; E3)
              referenciando ambas (preservadas); NUNCA sobrescreve em silêncio. Fora dessas condições NÃO há colisão. A
              RESOLUÇÃO é de SPEC-007/SPEC-018 ou governança — o KG só detecta e registra.
              [Fonte: INV-07; §D2.2; research.md §8; fronteira SPEC-007/SPEC-018]  [PROPOSTA]
```

### D2.1 — Matriz de integridade da ontologia (RULE-CKG-001) [PROPOSTA]

> **`school`/`hierarchy_role` DERIVADOS da proveniência canônica, NÃO auto-declarados [F-04/M-06] — SÓ para `hypothesis`
> (N-01, decisão de Andraus 2026-10-12, opção (a)):** resolvidos do `producer_id`/`producer_type` do objeto canônico
> referenciado (CHM-001 l.361; SPEC-001 l.187/203/214; allowlist `AUTHORIZED_PRODUCERS` SPEC-001 l.97/524) — não de
> atributo do payload (CBP-014). `school` ∈ {Elliott, SMC, Fibonacci} = escola do PRODUTOR DE HIPÓTESE autorizado
> (SPEC-001 RULE-HH-001 l.97: Elliott/SMC/Fibonacci; ICT NÃO é produtor — INV-02); `hierarchy_role` ∈ {PRIMARY, SUB}.
> **`structure` NÃO deriva `school` nesta versão:** não há mapeamento seguro produtor→escola homologado para `structure`;
> SAS-001 §6.12 (l.923-924) diz apenas que o Structural Agent é PRODUTOR e NÃO redefine ontologias — NÃO atribui escola — e
> por isso NÃO é fonte de `school` aqui. A origem/escola de `structure` e o elo `structure→hypothesis` ficam
> **[DECISÃO NECESSÁRIA] (CKG-STRUCT-ORIGIN-001, dona: Andraus)** — ver NOTA no bloco de decisões abertas e BL-035.
> **Fractal (N-09):** está na hierarquia analítica (CONSTITUTION) mas NÃO há produtor de hipótese `Fractal` em SPEC-001
> (`AUTHORIZED_PRODUCERS` = Elliott/SMC/Fibonacci) — logo `school=Fractal` NÃO tem fonte e NÃO é inventado aqui =
> **[INFERÊNCIA]/[DECISÃO NECESSÁRIA]** (mesma dona/gatilho de CKG-STRUCT-ORIGIN-001). O KG **espelha**, NÃO decide, a
> autoridade (CC-01). Regra de nó: `hypothesis.school ≠ ICT` (INV-02/RULE-HH-004 — SPEC-001 l.108/l.515-520). HERDA sub→pai
> ENTRE escolas é NORMAL (SPEC-001 RULE-HH-003 l.104; CHM-001 `parent_hypothesis_id` l.165/415; CONSTITUTION l.193); HERDA
> valida só `pai.hierarchy_role=PRIMARY`.
> **Fail-closed de `hypothesis` [A-04]:** o gate NÃO se limita a rejeitar `school==ICT`. Para `node_type=hypothesis` exige
> `canonical_ref≠null` ∧ `producer ∈ AUTHORIZED_PRODUCERS` (senão DENY — RULE-CKG-001 (i)/(ii)); `school` NÃO derivável do
> produtor ⇒ **DENY `SCHOOL_NOT_DERIVABLE`** (jamais falha-aberto); `hierarchy_role=PRIMARY ⇒ school=Elliott` (só Elliott
> cria a primária — SPEC-001 RULE-HH-002 l.100) ⇒ senão DENY `PRIMARY_NOT_ELLIOTT`; `hypothesis` pelo caminho (b) selo
> SPEC-007 é PROIBIDA (`HYPOTHESIS_VIA_SEAL_FORBIDDEN`) — só entra pelo ciclo de vida canônico (a). Assim a proteção de
> INV-02/RULE-HH-002 é EFETIVA, não apenas aparente (o gate não cai aberto quando a `school` não é derivável).

| Relação | Origem (node_type) | Destino (node_type) | Direcional | Simétrica (consulta) |
|---|---|---|---|---|
| CONFIRMA | **evidence** (NÃO observation — CONSTITUTION l.191 Observations vs l.192 Evidence; INV-06; A-09) | hypothesis | sim | não |
| REFUTA | **evidence** (NÃO observation) | hypothesis | sim | não |
| DEPENDE_DE | hypothesis, mission, **conviction** (A-12 — aresta de SAÍDA; **NENHUMA aresta PARA conviction**, INV-04), **narrative** (A-12 — narrative → hypothesis modela "agrega" [INFERÊNCIA]; KERNEL-V2 l.1500 "Narrativa agrega Hipóteses", [EXTERNO]/DADO) | hypothesis, evidence | sim | não — **pares admitidos restritos, N-06: ver nota abaixo** |
| HERDA | hypothesis (`hierarchy_role=SUB`) | hypothesis (**PAI = PRIMARY** — RULE-HH-003); entre escolas permitido | sim | não |
| PERTENCE_A | hypothesis, evidence, structure, observation | asset, timeframe, regime, mission | sim | não |
| INVALIDA | evidence, learning | evidence, relation (via `target_relation_id`) | sim | não |
| ORIGINA | **hypothesis** cujo `school` (derivado do produtor) ∈ {Elliott, SMC, Fibonacci} — **nunca ICT** (INV-02); `structure` **NÃO** é origem de ORIGINA nesta versão (CKG-STRUCT-ORIGIN-001 [DECISÃO NECESSÁRIA]) | hypothesis | sim | não |
| DERIVA_DE | evidence (DERIVED) | evidence (ancestral) | sim | não — aresta de Lineage; base do trace (CKG-011); obrigatória por ancestral (INV-CKG-02) |
| SIMILAR_A | qualquer **exceto conviction** (m-07) | mesmo node_type **exceto conviction** | sim (armazenada) | **sim** (A~B ⇔ B~A) |
| CAUSA | qualquer | qualquer — **destino `conviction` PROIBIDO (QUALQUER origem; predicado `to_node.node_type==conviction`; INV-04)** | sim | não — exige mechanism+direction+conditions+regime + `posthoc_flag` (CKG-008) |
| HIERARQUIA_DE | structure, timeframe | structure, timeframe | sim | não |
| ESTATISTICA_DE | learning | hypothesis, structure, asset | sim | não |

> **Pares admitidos de DEPENDE_DE [N-06]:** a matriz restringe os pares origem→destino desta relação (fora deles ⇒
> `RELATION_TYPE_INVALID`, ∈ `ONTOLOGY_INTEGRITY_VIOLATION`): **(hypothesis | mission) → (hypothesis | evidence)**;
> **conviction → (evidence | hypothesis)** (SÓ aresta de SAÍDA — torna navegáveis as fontes da convicção CCM-001
> `source_evidence_ids`/`hypothesis_ref`; **NENHUMA aresta PARA conviction** — INV-04); **narrative → (evidence | hypothesis)**
> (narrative → hypothesis modela "Narrativa agrega Hipóteses" — KERNEL-V2 l.1500, **[INFERÊNCIA]** sobre fonte [EXTERNO],
> não baseline). Pares não listados não são DEPENDE_DE válidos.
>
> **Navegabilidade de tipos antes isolados [A-12]:** `conviction` e `narrative` ganharam arestas de SAÍDA mínimas
> (DEPENDE_DE) para que as fontes da convicção (CCM-001 `source_evidence_ids`/`hypothesis_ref`) e a agregação de hipóteses
> pela narrativa (KERNEL-V2 l.1500) sejam navegáveis na cadeia cognitiva (CEM-001 l.614-615) — **sempre de SAÍDA; NENHUMA
> aresta tem `to_node.node_type==conviction`** (INV-04 intocado; RULE-CKG-007). **Caveat [N-07]: as arestas de SAÍDA de
> `conviction` acima permanecem VÁLIDAS como ESQUEMA da ontologia, mas um nó `conviction` só APARECE efetivamente no grafo
> quando a admissão de `conviction` for resolvida por Andraus (hoje NEGADA por padrão — `CONVICTION_HISTORY_UNDEFINED`,
> RULE-CKG-010 [N-07]).** Até lá, estas arestas não têm origem `conviction` instanciável. **`calibration_metric`:** o isolamento é
> **INTENCIONAL [PROPOSTA]** — a métrica de calibração "entra no KG" como NÓ isolado (CEE-001 l.111), sem relação de
> saída obrigatória nesta versão (não há cadeia cognitiva a navegar a partir dela); qualquer elo futuro é **[DECISÃO
> NECESSÁRIA]**. Nunca é destino de aresta (INV-04).
>
> **DERIVA_DE × proveniência:** `DERIVA_DE` é RELAÇÃO navegável (aresta de Lineage entre nós), consumida pela Trace
> Reconstruction (ordem = ancestralidade — CEM-001 l.567-577). `provenance_ref.lineage` é CAMPO de proveniência do
> registro (referencia `Lineage`/`derived_from[]`) — não é aresta navegável. Coexistem.

> **INV-CKG-01 (Memória permanente imutável) [PROPOSTA]:** nenhum registro é deletado/mutado; estado = projeção derivada;
> consolidação = arquivamento versionado; toda entidade/relação carrega proveniência e é reconstruível. Reforça — não
> redefine — RULE-BB-004/INV-07/SPEC-004 INV-CBP-01, no eixo permanente.

> **INV-CKG-02 (Completude e aciclicidade da linhagem da EVIDÊNCIA) [PROPOSTA]:** admitir um `evidence` DERIVED EXIGE
> uma aresta `DERIVA_DE` para CADA ancestral do seu `Lineage` (CEM-001 l.565) — fail-closed se algum ausente (CKG-003);
> o grafo DERIVA_DE é ACÍCLICO, incluindo a proibição de **self-loop** (M-02/N-07); o trace ignora validade (ancestral
> invalidado permanece — CEM-001 l.602). Garante a COMPLETUDE do trace de EVIDÊNCIA (CEM-001 l.612-614), independente de
> H-001. **NÃO cobre o trace de hipótese** (que é [PROPOSTA] best-effort — CKG-011).
> **Reconciliação com o fail-closed de CKG-003 (N-07):** o fail-closed de CKG-003 e a espera por ordem NÃO se contradizem —
> são momentos distintos. O derivado só é ADMITIDO quando TODAS as arestas `DERIVA_DE` por ancestral estão materializáveis
> (ancestrais presentes); enquanto um ancestral ainda não chegou, o derivado fica em `PENDING_ANCESTOR` — estado
> TRANSITÓRIO em buffer de admissão FORA do armazenamento (não é registro do KG; durabilidade do buffer = H-001). A espera
> é **BOUNDED por um LIMITE/TIMEOUT de admissão = [DECISÃO NECESSÁRIA]** (parâmetro a calibrar — runtime/K-001; SEM número
> arbitrário aqui — RULE-MET-01): esgotado o limite, o derivado é **REJEITADO fail-closed** (`DERIVA_DE_EDGE_MISSING`),
> jamais admitido sem todas as arestas e jamais esperando para sempre. Assim: nunca admissão incompleta (CKG-003); nunca
> espera infinita (bounded); o limite concreto é de Andraus/runtime, não fixado nesta Spec.

### D2.2 — Tabela de contradição e escopo de colisão (RULE-CKG-013) [PROPOSTA]

**Escopo — depende do par:** CONFIRMA×REFUTA = mesmos `from_node`/`to_node`; INVALIDA×alvo = `INVALIDA.target_relation_id
== r2.relation_id`. **Condições (todas):** (i) par ∈ tabela; (ii) escopo coincidente; (iii) sobreposição temporal
(interseção de `[valid_from, valid_to)` não vazia, com `valid_to=null`≡+∞); (iv) ambas NÃO-SUPERSEDED.

> **Natureza da colisão (N-08):** o `collision_record` é uma **MARCAÇÃO não-destrutiva de conflito para governança** (ambas
> as relações PRESERVADAS; o KG **nunca rejeita nem apaga** por colisão — resolução é de SPEC-007/SPEC-018/governança). Não
> é, portanto, um efeito "ruim" a evitar — é um sinal auditável.

> **INVALIDA×alvo — por que NÃO colide por construção (N-08):** a INVALIDA é o mecanismo AUTORIZADO de invalidação
> (CKG-004): no caminho normal, a invalidação FECHA a validade do alvo `r2` (novo registro com `valid_to`), tornando `r2`
> **INVALIDATED_IN_TIME / NÃO-vigente** — e aí **NÃO há colisão** (a INVALIDA cumpriu seu papel; não há duas afirmações
> vigentes em conflito). A colisão só é marcada quando `r2` **PERMANECE VIGENTE** (`valid_to=null` ou período sobreposto)
> APESAR da INVALIDA vigente — i.e., uma invalidação pendente/contestada sobre uma relação ainda afirmada como válida.
> Essa restrição (condição (v) abaixo) impede que todo uso normal de INVALIDA gere colisão. **[A-11]** A INVALIDA e o
> fechamento do `valid_to` do alvo são um ÚNICO ATO ATÔMICO; (v) é avaliada sobre o estado resultante dos dois registros
> (nunca no instante intermediário) — a decisão de colisão NÃO depende da ordem de escrita.

| Tipo A | Tipo B (contradiz A) | Escopo do par | Simétrico? | Observação |
|---|---|---|---|---|
| CONFIRMA | REFUTA | mesmos `from_node`/`to_node` | **sim** | mesma hipótese afirmada e negada ao mesmo tempo |
| INVALIDA | relação-alvo `r2` | `INVALIDA.target_relation_id == r2.relation_id` | não | **(v)** INVALIDA vigente E `r2` PERMANECE VIGENTE apesar dela (a invalidação NÃO fechou a validade de `r2`); invalidação autorizada normal que fecha `r2` NÃO colide (N-08) |

> Pares NÃO listados não são contradição estrutural. **NÃO colidem:** (a) `from_node` diferentes; (b) validades disjuntas;
> (c) uma SUPERSEDED; (d) **INVALIDA que fechou a validade do alvo** (alvo não mais vigente — operação normal, N-08). A
> resolução é de SPEC-007/SPEC-018 ou governança. Tabela ENXUTA, extensível por governança (RULE-ONT-02).

---

## Critérios de Aceitação (EARS)

> Cada EARS referencia a regra-fonte (D2) por ID; não reescreve a regra.

1. (CKG-001) Quando um nó/relação é submetido para escrita, o KG DEVE escrevê-lo só se o tipo ∈ ontologia e a matriz §D2.1 é satisfeita, e DEVE rejeitar (fail-closed) violação de tipo/integridade; para `hypothesis`, DEVE exigir o fail-closed de §D2.1 [A-04] (`canonical_ref≠null` ∧ `producer∈AUTHORIZED_PRODUCERS` ∧ `school` derivável ∧ PRIMARY⇒Elliott ∧ ¬via selo), nunca falhando-aberto.
2. (CKG-002) Quando um nó corresponde a objeto canônico, o KG DEVE referenciá-lo por ID+versão e NÃO DEVE redefinir contrato/campos/estados; DEVE validar cada `canonical_state_transition` contra a tabela do tipo e rejeitar transição proibida/reativação de estado terminal; `observation` NÃO DEVE ser rotulado `evidence`.
3. (CKG-003) Quando uma relação é escrita, o KG DEVE exigir tipo, direção e proveniência; para `evidence` DERIVED DEVE exigir `DERIVA_DE` por ancestral e DEVE rejeitar aresta que feche ciclo na linhagem.
4. (CKG-004) Quando a validade de uma relação muda, o KG DEVE gravar NOVO registro de invalidação/sucessão, DEVE rejeitar janela `valid_to < valid_from`, e NÃO DEVE mutar nem deletar o registro existente.
5. (CKG-005) Quando qualquer escrita é tentada, o KG DEVE exigir `computed_by` (produtor autenticado) sempre, `gate_record` se há gate e `lineage` se derivado, e DEVE rejeitá-la sem a proveniência exigível.
6. (CKG-006) Quando um "esquecimento"/consolidação é solicitado, o KG DEVE arquivar/rebaixar por novo registro versionado, e NÃO DEVE remover nem mutar registro histórico.
7. (CKG-007) Quando uma confiança de relação é registrada ou lida, o KG DEVE mantê-la em namespace próprio e NÃO DEVE escrevê-la/devolvê-la em campos do objeto de convicção, nem escrever QUALQUER aresta `to_node.node_type == conviction` (direta ou por 2 saltos).
8. (CKG-008) Quando uma relação causal é proposta, o KG DEVE exigir mechanism+direction+conditions+regime, `posthoc_flag` booleano, `outcome_ref` (ou `no_outcome=true`+justificativa), DEVE DERIVAR `outcome_timestamp` do `recorded_at` do registro apontado por `outcome_ref` (rejeitando carimbo de payload posterior) e rejeitar `no_outcome=true` com `outcome_ref` presente, DEVE forçar `posthoc_flag=true` quando `formulated_at` > `outcome_timestamp` (instante de FORMULAÇÃO, não do registro corrente — A-01) e aceitar `posthoc_flag=false` quando `formulated_at` ≤ `outcome_timestamp`, e DEVE rejeitar causal sem esses campos; DEVE rejeitar sucessora da cadeia `supersedes` que ALTERE o núcleo causal {mechanism/direction/conditions/regime/`outcome_ref`/`no_outcome`} (`CAUSAL_CORE_IMMUTABLE_IN_CHAIN` — ver RULE-CKG-008 [N-02/m-A]); SIMILAR_A por juízo DEVE carregar `similarity_basis`.
9. (CKG-009/005) Quando uma escrita permanente é tentada, o KG DEVE aceitá-la (E3) apenas de escritor autorizado/autenticado (falha de auth ⇒ não-autorizado), NÃO DEVE permitir que o produtor redefina ontologia/taxonomia, e NÃO DEVE aceitar commit direto do PRODUTOR (`computed_by` como `writer_id`) — só o COMMITTER autorizado (runtime/serviço do KG) escreve (capacidade×papel, D6).
10. (CKG-010) Quando conhecimento formado sem selo é submetido, o KG DEVE rejeitá-lo; objetos canônicos entram só quando `canonical_status` ∈ conjunto admissível do tipo (exclui EMERGENT/CANDIDATE) E a TRAJETÓRIA passou pelo estado de validação do tipo (predicado POR TIPO — RULE-CKG-010 [N-01]: hypothesis ACTIVE∨DOMINANT; evidence ACTIVE; **conviction NEGADO POR PADRÃO — `CONVICTION_HISTORY_UNDEFINED`, N-07**), prova (hypothesis/evidence) resolvida do `canonical_history_ref` no canônico (nunca do payload; ausência ⇒ `CANONICAL_HISTORY_UNRESOLVABLE`; submissão de `conviction` ⇒ DENY `CONVICTION_HISTORY_UNDEFINED`), preservando os estados a partir da admissão.
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
| `ONTOLOGY_INTEGRITY_VIOLATION` | `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`, `ORIGINA_ICT_FORBIDDEN`, `RELATION_TYPE_INVALID`, `SIMILAR_A_TYPE_MISMATCH`, `PRIMARY_NOT_ELLIOTT` (A-04), `SCHOOL_NOT_DERIVABLE` (A-04), `HYPOTHESIS_PRODUCER_UNAUTHORIZED` (A-04), `HYPOTHESIS_CANONICAL_REF_MISSING` (A-04) | CKG-001/003; T01/T03/T18/T19; ADV-12/17 |
| `OBSERVATION_IS_NOT_EVIDENCE` | — | CKG-002; T02; ADV-11 |
| `FORBIDDEN_CANONICAL_TRANSITION` | — | CKG-002; T09; ADV-11 |
| `CANONICAL_CONTRACT_REDEFINITION_FORBIDDEN` | — | CKG-002 (redefinir campos/estado do canônico — CC-02/INV-10); ADV-11 (N-04) |
| `PROVENANCE_MISSING` | `COMPUTED_BY_MISSING` | CKG-005; T14; ADV-06 |
| `CAUSAL_FIELDS_MISSING` | `POSTHOC_FLAG_REQUIRED`, `OUTCOME_REF_MISSING`, `OUTCOME_TIMESTAMP_INVALID`, `NO_OUTCOME_CONFLICT` | CKG-008; T07/T16; ADV-04 |
| `CAUSAL_CORE_IMMUTABLE_IN_CHAIN` **(pai próprio [m-C] — NÃO é campo faltante; é mutação PROIBIDA do núcleo causal {mechanism/direction/conditions/regime/outcome_ref/no_outcome} na cadeia `supersedes`, N-02/m-A)** | — | CKG-008/012; ADV-04 (caso h) |
| `CONFIDENCE_IS_NOT_CONVICTION` | `EDGE_TO_CONVICTION_FORBIDDEN` | CKG-007; T06; ADV-03/05 |
| `WRITE_UNAUTHORIZED` | `AUTH_UNAVAILABLE`, `ONTOLOGY_REDEFINITION_FORBIDDEN` | CKG-009; T08; ADV-07 |
| `IMMUTABILITY_VIOLATION` | `PHYSICAL_DELETE_FORBIDDEN`, `RECORD_UPDATE_FORBIDDEN`, `VERSION_FORK_FORBIDDEN`, `EXPECTED_VERSION_REQUIRED` (ausência), `VERSION_CONFLICT` (divergência) — códigos de origem SPEC-004 CBP-004 l.243-244 (N-04) | CKG-006/012; T05/T13; ADV-01/13/15/19 |
| `INVALID_TIME_WINDOW` | — | CKG-004; T04; ADV-13 |
| `ADMISSION_REJECTED` | `FORMED_WITHOUT_SEAL`, `CANONICAL_STATUS_NOT_ADMISSIBLE`, `TRAJECTORY_NEVER_ACTIVE` (A-02; predicado POR TIPO — N-01), `CANONICAL_HISTORY_UNRESOLVABLE` (N-01), `CONVICTION_HISTORY_UNDEFINED` (N-07 — `conviction` negado por padrão; CCM-001 l.58/78 não define histórico; M-001 ABERTA), `HYPOTHESIS_VIA_SEAL_FORBIDDEN` (A-04) | CKG-010; T09; ADV-21/23 |
| `LINEAGE_INCOMPLETE` | `DERIVA_DE_EDGE_MISSING`, `LINEAGE_CYCLE` | CKG-003/011; ADV-16/20 |
| `SCOPE_OR_OPEN_DECISION_VIOLATION` **(marcador de REVISÃO/spec-time — A-13; NÃO é código de rejeição de runtime)** | `OUT_OF_SCOPE_FORMATION`, `OPEN_DECISION_H001`, `OUT_OF_SCOPE_OR_OPEN_DECISION` | checagem de revisão de escopo/decisão aberta (ADV-08/09/10 — spec-time, não gate de runtime) |

### BASpec-CKG-001 — Ontologia enxuta + matriz de integridade (ver RULE-CKG-001)
```
BASpec-CKG-001:
  QUANDO:       Um nó/relação é submetido para escrita
  ENTÃO:        Aplica RULE-CKG-001 — escreve só se tipo ∈ ontologia ∧ matriz §D2.1 satisfeita (incl. regra de nó
                `hypothesis.school ≠ ICT` e HERDA.pai=PRIMARY); **para `hypothesis`, fail-closed [A-04] — ver §D2.1
                "Fail-closed de `hypothesis`": `canonical_ref≠null` ∧ `producer∈AUTHORIZED_PRODUCERS` ∧ `school` derivável ∧
                `hierarchy_role=PRIMARY ⇒ school=Elliott` ∧ ¬(via selo SPEC-007)**; violação rejeitada (fail-closed; nunca
                falha-aberto). Espelha vínculos criados pelos agentes; não decide autoridade (CC-01)
  PORQUE:       Sem gramática enxuta + integridade, a memória permanente acumula conhecimento incoerente (ABERTURA.md §10 R-8 — A-08)
  REFERÊNCIA:   RULE-CKG-001; §D2.1 (fail-closed de hypothesis — A-04); INV-02; RULE-HH-002/003/004 (SPEC-001 l.100/104/108); AUTHORIZED_PRODUCERS (SPEC-001 l.97/524)
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico (tipo ∈ catálogo ∧ par origem/destino ∈ matriz ∧ direção/simetria ∧ hypothesis.school≠ICT ∧ HERDA.pai=PRIMARY ∧ [hypothesis ⇒ canonical_ref≠null ∧ producer∈AUTHORIZED_PRODUCERS ∧ school derivável ∧ (PRIMARY⇒Elliott) ∧ ¬via selo] — A-04)
    GATE DE SAÍDA: verificação da matriz §D2.1 + regras de nó + fail-closed de hypothesis (A-04; nunca falha-aberto)
    CRITÉRIO 4Es: Conformidade > Eficácia — coerência da ontologia é inviolável
  VERIFICADO POR:
    DADO        (a) um `hypothesis` cujo `school` derivado do produtor == ICT; (b) um `hypothesis` com `producer` fora de AUTHORIZED_PRODUCERS (school não derivável); (c) um `hypothesis` PRIMARY com school≠Elliott; (d) um `hypothesis` via selo SPEC-007
    QUANDO      o gate de integridade roda
    ENTÃO       escrita rejeitada em todos; nada persistido (contraste positivo: HERDA SMC-SUB → Elliott-PRIMARY é VÁLIDA — T15; negativos detalhados em T18/T19/ADV-23)
    VERIFICAÇÃO written == false; rejected_reason ∈ {"HYPOTHESIS_SCHOOL_ICT_FORBIDDEN","SCHOOL_NOT_DERIVABLE","HYPOTHESIS_PRODUCER_UNAUTHORIZED","PRIMARY_NOT_ELLIOTT","HYPOTHESIS_VIA_SEAL_FORBIDDEN"} (∈ ONTOLOGY_INTEGRITY_VIOLATION); fail_open == false
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
  REFERÊNCIA:   RULE-CKG-002; CC-02; CC-10; CEM-001 l.264/428/468-475; INV-06; INV-10
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
                (OBRIGATÓRIA; ausência fail-closed, ordem reconciliada em buffer bounded — INV-CKG-02/N-07); **rejeita aresta
                DERIVA_DE que feche ciclo — se a ORIGEM já é alcançável a partir do DESTINO [M-02] — e proíbe self-loop
                (origem==destino) [N-07]**; SIMILAR_A é simétrica só na consulta; contradição não silenciada (CKG-013)
  PORQUE:       Relação sem tipo/direção/proveniência não é auditável (P13); sem a aresta por ancestral o trace completo da
                Evidência (CKG-011/CEM-001 l.612-614) não seria garantido; linhagem cíclica nunca termina
  REFERÊNCIA:   RULE-CKG-003/005; INV-CKG-02; CEM-001 l.565
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : validação (tipo ∈ catálogo ∧ direção ∧ proveniência ∧ ACICLICIDADE: rejeita se origem alcançável a partir do destino via DERIVA_DE ∧ ¬self-loop origem==destino — N-07)
    GATE DE SAÍDA: verificação (tipo ∧ direção ∧ proveniência ∧ ¬cria_ciclo ∧ ¬self-loop)
    CRITÉRIO 4Es: Eficácia — relações auditáveis e navegáveis; linhagem acíclica (trace termina)
  VERIFICADO POR:
    DADO        (a) relação sem tipo do catálogo; (b) aresta DERIVA_DE cuja origem já é alcançável a partir do destino (fecharia ciclo); (c) aresta DERIVA_DE com origem == destino (self-loop)
    QUANDO      a validação roda
    ENTÃO       (a) rejeitada `RELATION_TYPE_INVALID`; (b) rejeitada `LINEAGE_CYCLE`; (c) rejeitada `LINEAGE_CYCLE`
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
  REFERÊNCIA:   RULE-CKG-004/009; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.606
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
  REFERÊNCIA:   RULE-CKG-005; SPEC-004 RULE-CBP-007 l.264-270/CBP-014 l.311-319; CEM-001 Cap.5
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
                `outcome_ref` (ou `no_outcome=true`+justificativa) [M-04]; **`outcome_timestamp` DERIVADO do `recorded_at`
                do registro apontado por `outcome_ref` [N-02]** (payload divergente/posterior ⇒ `OUTCOME_TIMESTAMP_INVALID`;
                `no_outcome=true` com `outcome_ref` ⇒ `NO_OUTCOME_CONFLICT`); força `posthoc_flag=true` quando `formulated_at`
                > `outcome_timestamp` e aceita `posthoc_flag=false` quando `formulated_at` ≤ `outcome_timestamp` (instante de
                FORMULAÇÃO = `recorded_at` da 1ª versão da cadeia `supersedes`, não o registro corrente — A-01; alternativa
                "hipótese referenciada" descartada da regra — N-02); **NEGA (`CAUSAL_CORE_IMMUTABLE_IN_CHAIN`) sucessora da
                cadeia `supersedes` que altere o NÚCLEO CAUSAL = `mechanism`/`direction`/`conditions`/`regime` E `outcome_ref`/
                `no_outcome`** (RULE-CKG-008 [N-02/m-A]; correção do núcleo exige NOVA CAUSA — caminho legítimo m-C);
                faltando qualquer campo rejeita. SIMILAR_A por juízo exige `similarity_basis`. Gate verifica PRESENÇA e a regra
                de carimbo, não veracidade (ENF-03)
  PORQUE:       Correlação não é causalidade (CAU-01); regime muda a relação (CAU-02); explicação pós-resultado é viés se não marcada (CAU-03); comparar com o `recorded_at` do registro corrente tornaria TODA causa pós-hoc (degenerado) — por isso o baseline é o instante de FORMULAÇÃO (A-01) e o carimbo do desfecho deriva do registro apontado (N-02)
  REFERÊNCIA:   RULE-CKG-008; RULE-CAU-01/02/03
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : juízo (apoio semântico) PROPÕE; gate determinístico verifica presença dos campos e a regra temporal
    BOUNDED LOOP: nº máx. de tentativas por par de nós; sem retry infinito (CAUSA e SIMILAR_A)
    GATE DE SAÍDA: verificação (CAUSA ⇒ mechanism ∧ direction ∧ conditions ∧ regime ∧ posthoc_flag ∧ (outcome_ref ∨ no_outcome) ∧ ¬(outcome_ref ∧ no_outcome) ∧ [outcome_ref ⇒ outcome_timestamp := recorded_at(outcome_ref) ∧ payload_ts ≤ recorded_at(outcome_ref)] ∧ [formulated_at>outcome_timestamp ⇒ posthoc_flag==true] ∧ [formulated_at≤outcome_timestamp ⇒ posthoc_flag=false aceito, não pós-hoc — A-01], formulated_at := recorded_at da 1ª versão da cadeia supersedes [alternativa "hipótese referenciada" removida; núcleo causal mechanism/direction/conditions/regime/outcome_ref/no_outcome imutável na cadeia supersedes (sucessora que altere qualquer um ⇒ CAUSAL_CORE_IMMUTABLE_IN_CHAIN) — RULE-CKG-008 N-02/m-A]; SIMILAR_A ⇒ similarity_basis)
    CRITÉRIO 4Es: Eficácia (causalidade válida) > Eficiência; LLM é detector, nunca gate (ENF-03)
  VERIFICADO POR:
    DADO        (a) CAUSA sem mechanism/regime; (b) CAUSA com formulated_at > outcome_timestamp e posthoc_flag=false; (c) CAUSA sem outcome_ref e sem no_outcome; (d) CAUSA com outcome_timestamp (payload) POSTERIOR ao recorded_at do registro apontado por outcome_ref; (e) CAUSA com no_outcome=true E outcome_ref presente; (f) CAUSA cujo formulated_at é ANTERIOR ao outcome_timestamp (a afirmação foi formulada ANTES do desfecho) e posthoc_flag=false; (g) sucessora da cadeia `supersedes` que ALTERA o núcleo causal — mechanism/direction/conditions/regime OU `outcome_ref` OU `no_outcome` (m-A) — ver ADV-04 casos (g)/(h)
    QUANDO      o gate de saída roda
    ENTÃO       (a) `CAUSAL_FIELDS_MISSING`; (b) `POSTHOC_FLAG_REQUIRED`; (c) `OUTCOME_REF_MISSING`; (d) `OUTCOME_TIMESTAMP_INVALID`; (e) `NO_OUTCOME_CONFLICT`; (f) ACEITA (não pós-hoc — posthoc_flag=false é legítimo; A-01); (g) `CAUSAL_CORE_IMMUTABLE_IN_CHAIN` (núcleo causal imutável na cadeia; correção exige NOVA CAUSA — RULE-CKG-008 [N-02/m-A], caminho legítimo m-C)
    VERIFICAÇÃO causal_written_in_f == true; posthoc_rule_enforced == true; outcome_ref_required == true; outcome_timestamp_derived_from_ref == true; posthoc_baseline_is_formulated_at == true; no_outcome_conflict_rejected == true; causal_core_immutable_incl_outcome_denied == true
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
    ENTÃO       negada (fail-closed; tratada como não-autorizada). [A-13: a amostragem de falso-DENY E3 é propriedade de enforcement (ENF-07, EC-CKG-003), não desfecho verificável deste cenário]
    VERIFICAÇÃO write_allowed == false; fail_closed == true; treated_as_unauthorized == true
```

### BASpec-CKG-010 — Fronteira de entrada (ver RULE-CKG-010)
```
BASpec-CKG-010:
  QUANDO:       Conhecimento é submetido ao KG
  ENTÃO:        Aplica RULE-CKG-010 — admite (a) canônicos cujo `canonical_status` ∈ conjunto admissível do tipo (exclui
                EMERGENT/CANDIDATE) **E cuja TRAJETÓRIA passou pelo ESTADO DE VALIDAÇÃO DO SEU TIPO — predicado POR TIPO [N-01],
                ver RULE-CKG-010 (hypothesis: ACTIVE∨DOMINANT; evidence: ACTIVE; **conviction: NEGADO POR PADRÃO —
                `CONVICTION_HISTORY_UNDEFINED`, N-07**); a prova da trajetória (hypothesis/evidence) vem do `canonical_history_ref`
                resolvido no canônico (CHM/CEM), nunca do payload — ausência ⇒ `CANONICAL_HISTORY_UNRESOLVABLE`; jamais-validado ⇒
                `TRAJECTORY_NEVER_ACTIVE`; submissão de `conviction` ⇒ DENY `CONVICTION_HISTORY_UNDEFINED`**, gravando `canonical_status`+transições
                (preserva estados a partir da admissão — regra LOCAL CKG-010, A-03), e (b) formado com selo SPEC-007; formado
                sem selo rejeitado; o KG não forma/retrieval
  PORQUE:       "Documento recuperado ≠ validado ≠ publicado"; formação é SPEC-007; o canonical_ref@version sozinho não carrega Status (CEM-001 l.264) — exige canonical_status+transições; o status corrente admissível não basta — exige trajetória que passou pela validação do tipo (A-02/N-01)
  REFERÊNCIA:   RULE-CKG-010 (trajetória POR TIPO + canonical_history_ref — N-01); ROADMAP §6/§7; CEM-001 l.258-262/l.264; CHM-001 §4.3 l.744-748 (trajetória — A-02); CCM-001 l.58/78
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : (b) gate (selo SPEC-007 presente); (a) gate POR TIPO (`canonical_status` ∈ conjunto admissível do tipo ∧ trajetória de validação do tipo resolvida via `canonical_history_ref` — N-01) — ambos verificáveis, fail-closed
    GATE DE SAÍDA: verificação (selo presente) / (canonical_status ∈ conjunto admissível do tipo ∧ trajetória passou pela validação do tipo — ver RULE-CKG-010)
    CRITÉRIO 4Es: Conformidade > Eficácia — não contaminar com não-validado; não perder estado canônico (dos admitidos)
  VERIFICADO POR:
    DADO        (a) conhecimento formado SEM selo; (b) hypothesis com canonical_status=EMERGENT (ainda trabalho); (c) positivos por tipo e negativos de trajetória/histórico em T09/ADV-21
    QUANDO      o gate de fronteira roda
    ENTÃO       (a) rejeitado `FORMED_WITHOUT_SEAL`; (b) rejeitada `CANONICAL_STATUS_NOT_ADMISSIBLE`; (c) ver T09 (admissão positiva por tipo) e ADV-21 (`TRAJECTORY_NEVER_ACTIVE`/`CANONICAL_HISTORY_UNRESOLVABLE` por tipo)
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
                coincidente (sem FORK — `VERSION_FORK_FORBIDDEN`; ausência ⇒ `EXPECTED_VERSION_REQUIRED`; divergência ⇒ `VERSION_CONFLICT`, N-04); estado = projeção derivada; nada removido/mutado
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
  QUANDO:       Duas relações satisfazem as condições de colisão (§D2.2: (i)–(iv) + (v) para INVALIDA×alvo)
  ENTÃO:        Aplica RULE-CKG-013 — DETECTA e grava `collision_record` (MARCAÇÃO NÃO-DESTRUTIVA para governança — N-08)
                com identidade/proveniência próprias (`collision_id`/`version`/`computed_by`=`writer_id`=serviço do KG/
                `recorded_at`; E3) referenciando ambas (preservadas); **nunca rejeita/apaga**; relações fora das condições não
                geram colisão — **invalidação autorizada que FECHA o alvo NÃO colide (N-08)**; resolução = SPEC-007/SPEC-018/governança
  PORQUE:       Preservar a contradição auditável respeita INV-07; resolver em silêncio perderia conhecimento (viés de confirmação); escopo + condição (v) evitam falso-positivo (INVALIDA não colide por construção — N-08)
  REFERÊNCIA:   RULE-CKG-013; §D2.2; INV-07; fronteira SPEC-007/SPEC-018
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : detecção determinística (par ∈ §D2.2 ∧ escopo_do_par ∧ overlap(valid) ∧ ¬superseded(ambas) ∧ cond_v[INVALIDA⇒alvo ainda vigente]) ⇒ grava collision_record (marcação, não rejeição); proíbe sobrescrita silenciosa
    GATE DE SAÍDA: verificação (condições (i)–(v) ⇒ collision_record com collision_id/computed_by/writer_id ∧ ambas preservadas; senão sem colisão)
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

- **Integridade (CKG-001):** aceitar sse tipo ∈ catálogo ∧ (origem.node_type, destino.node_type) ∈ matriz[tipo] ∧ direção/simetria conformes (§D2.1). Nó hypothesis: `school`/`hierarchy_role` (SÓ para hypothesis — N-01) DERIVADOS do `producer_id`/`producer_type` do canônico (`school` ∈ {Elliott,SMC,Fibonacci}; `structure` NÃO deriva school e Fractal não tem produtor em SPEC-001 — CKG-STRUCT-ORIGIN-001 [DECISÃO NECESSÁRIA]); ORIGINA só de hypothesis. **Fail-closed de hypothesis [A-04]:** `aceitar sse hypothesis ⇒ (canonical_ref≠null ∧ producer∈AUTHORIZED_PRODUCERS ∧ school derivável ∧ school≠ICT ∧ (hierarchy_role=PRIMARY ⇒ school=Elliott) ∧ publication.origin≠spec007_seal)` — qualquer predicado falso ⇒ DENY (`HYPOTHESIS_CANONICAL_REF_MISSING`/`HYPOTHESIS_PRODUCER_UNAUTHORIZED`/`SCHOOL_NOT_DERIVABLE`/`HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`/`PRIMARY_NOT_ELLIOTT`/`HYPOTHESIS_VIA_SEAL_FORBIDDEN`), NUNCA falha-aberto; `HERDA ⇒ pai.hierarchy_role=PRIMARY` (e pai PRIMARY é Elliott).
- **Admissão (CKG-010) [N-01/N-07]:** `admite(x) sse (x formado ∧ selo SPEC-007) ∨ (x canônico ∧ x.tipo ∈ {hypothesis, evidence} ∧ canonical_status ∈ admissível[tipo] ∧ trajetória[tipo](x))`, com `trajetória[tipo]` = passou pelo ESTADO DE VALIDAÇÃO do tipo — hypothesis: ACTIVE∨DOMINANT; evidence: ACTIVE (ver RULE-CKG-010). **`conviction` é NEGADO POR PADRÃO (`CONVICTION_HISTORY_UNDEFINED`, fail-closed — N-07): não há predicado de trajetória admissível enquanto o histórico canônico de status da conviction (CCM-001 l.58/78 só define o enum) e M-001 (Cap.5 l.117) não existirem — decisões de Andraus.** A trajetória (hypothesis/evidence) é RESOLVIDA do `canonical_history_ref` no canônico (CHM/CEM), nunca do payload: irresolúvel ⇒ `CANONICAL_HISTORY_UNRESOLVABLE`; jamais-validado ⇒ `TRAJECTORY_NEVER_ACTIVE` (fail-closed).
- **Validade bitemporal (CKG-004):** criação grava `R0{creation, valid_from, recorded_at}`; mudança grava `R1{invalidation, targets_record_id=R0, valid_to, recorded_at}`; R0 nunca mutado. Rejeita `valid_to < valid_from`. `valid_to=null`≡+∞. valid-time: `válida_em(T) = ∃ creation com valid_from≤T ∧ ¬∃ invalidation aplicável com valid_to≤T`; transaction-time: conjunto com `recorded_at≤R`.
- **Imutabilidade / estado derivado + PRECEDÊNCIA (CKG-006/012):** `DELETE/UPDATE de registro ⇒ negado`. Estado(x) por precedência: (1) SUPERSEDED sse ∃ sucessora `supersedes=x`; senão (2) INVALIDATED_IN_TIME sse ∃ invalidation `targets_record_id=x` sem sucessora; senão (3) ARCHIVED sse ∃ archival vigente; senão (4) ACTIVE_KNOWLEDGE.
- **Trace Reconstruction (CKG-011):** `trace(x)` = fecho transitivo de `DERIVA_DE` a partir de x para **evidence** — COMPLETO (garantido por INV-CKG-02; ignora validade, inclui SUPERSEDED/ARCHIVED — CEM-001 l.602); ordem = ancestralidade (CEM-001 l.567-577). **Para hipótese** (ORIGINA/HERDA/DEPENDE_DE) = best-effort [PROPOSTA], sem garantia de completude [M-03]. Completude (Evidência) é obrigação; eficiência de travessia ampla = H-001.
- **Versionamento/dedupe (CKG-012):** atualização aceita sse `supersedes`=última ∧ `version`=anterior+1 ∧ `expected_version`=corrente (compare-and-commit — SPEC-004 CBP-004 l.239-246); ausência de expected_version na atualização ⇒ `EXPECTED_VERSION_REQUIRED`, divergência ⇒ `VERSION_CONFLICT` (códigos de origem SPEC-004 l.243-244 — N-04); 2ª sucessora da mesma versão ⇒ `VERSION_FORK_FORBIDDEN`. **Chave natural (não-canônico):** `(node_type, natural_key)` para asset/timeframe/regime/narrative/observation/learning/**structure/mission/calibration_metric** (M-06 — lista completa); canônico: `(node_type, canonical_ref)`; relação: `(relation_type, from_node, to_node, target_relation_id, valid_from)` — **`target_relation_id` incluído [A-10]** para que INVALIDA (cujo `to_node=null` e alvo é uma RELAÇÃO) não colapse: duas INVALIDA da mesma origem, no mesmo `valid_from`, contra relações-alvo DIFERENTES, têm chaves distintas (não há falso dedupe/DENY). Reescrita idêntica = no-op; divergente sem supersedes ⇒ DENY.
- **Gate causal (CKG-008):** `CAUSA ⇒ {mechanism, direction, conditions, regime} ≠ ∅ ∧ posthoc_flag booleano ∧ (outcome_ref XOR no_outcome=true+justificativa)`. Quando `outcome_ref`: `outcome_timestamp := recorded_at(registro apontado por outcome_ref)` [N-02] — payload posterior ⇒ `OUTCOME_TIMESTAMP_INVALID`; `no_outcome=true ∧ outcome_ref` ⇒ `NO_OUTCOME_CONFLICT`; `formulated_at := recorded_at(1ª versão da cadeia supersedes da CAUSA)` [A-01; alternativa "hipótese referenciada" removida — N-02] e `[formulated_at>outcome_timestamp ⇒ posthoc_flag=true]`, `[formulated_at≤outcome_timestamp ⇒ posthoc_flag=false legítimo, não pós-hoc]` (o `recorded_at` do registro corrente NÃO é o baseline — seria sempre > outcome, degenerando). **Núcleo causal imutável na cadeia [N-02/m-A]:** sucessora que ALTERA mechanism/direction/conditions/regime **ou `outcome_ref` ou `no_outcome` [m-A]** ⇒ `CAUSAL_CORE_IMMUTABLE_IN_CHAIN` (correção do núcleo exige NOVA CAUSA com `valid_from`/`formulated_at` próprios, aposentando a antiga via INVALIDA — caminho legítimo m-C; ver RULE-CKG-008). `SIMILAR_A ⇒ similarity_basis`. Juízo bounded. Verifica PRESENÇA e carimbo DERIVADO, não veracidade (ENF-03).
- **Confiança (CKG-007):** `confidence ∈ escala própria (PARÂMETRO a calibrar — INDETERMINADO)`; proibido em campo de convicção e `¬∃ aresta e : e.to_node.node_type==conviction` (direta ou multi-salto; INV-04).
- **Colisão (CKG-013/§D2.2):** `colide(r1,r2) sse (r1.type,r2.type)∈§D2.2 ∧ escopo_do_par ∧ overlap([r1.valid_from,r1.valid_to),[r2.valid_from,r2.valid_to)) ∧ ¬superseded(ambas) ∧ cond_v`, com `escopo_do_par` = (CONFIRMA×REFUTA: from/to iguais) ∨ (INVALIDA×alvo: `r1.target_relation_id==r2.relation_id`), e `cond_v` = (CONFIRMA×REFUTA: true) ∨ (INVALIDA×alvo: `r2 ainda VIGENTE` — i.e. a INVALIDA NÃO fechou valid_to de r2; invalidação autorizada normal ⇒ ¬colide, N-08). Se colide ⇒ grava collision_record (MARCAÇÃO não-destrutiva, E3; ambas preservadas); senão não.

Nenhuma fórmula computa convicção; nenhum limiar de convicção nem escala numérica de confiança fixado (RULE-MET-01). [FONTE: atomic-spec §2; CEM-001 Cap.5; SPEC-004 INV-CBP-01; research.md §3.1/§4]

---

## D5 — Máquina de estados (lifecycle do nó/relação — estado = projeção derivada)

> **Fronteira (CC-02/CC-10):** lifecycle do **conhecimento no KG permanente**, separado da máquina da **hipótese**
> (CHM-001) e do **estado no Blackboard** (SPEC-004). `knowledge_state` NÃO é campo mutado — é PROJEÇÃO DERIVADA (espelha
> SPEC-004 INV-CBP-01). Os estados do KG são HOMÔNIMOS mas ≠ estados canônicos: apenas **REFUTED** é EXCLUSIVO do
> **CHM** (hipótese); SUPERSEDED/ARCHIVED também ocorrem na Evidência (CEM-001 l.258-262 — N-06), cujo conjunto é
> ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED, **sem REFUTED** (m-03).
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
> collision/transição) — valores DISTINTOS para nós/relações PROPOSTOS por produtor; em registros GERADOS pelo serviço do KG
> (collision, transição, arquivamento) `computed_by = writer_id = serviço` por desenho; nenhum depende do payload (CBP-014).
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
2. **Fronteira (CKG-010):** canônico só se `canonical_status` ∈ conjunto admissível do tipo (exclui EMERGENT/CANDIDATE) **E a TRAJETÓRIA passou pelo estado de validação do tipo — predicado POR TIPO, resolvido do `canonical_history_ref` no canônico (ver RULE-CKG-010 [N-01]); irresolúvel ⇒ `CANONICAL_HISTORY_UNRESOLVABLE`, jamais-validado ⇒ `TRAJECTORY_NEVER_ACTIVE`**; formado exige selo ⇒ senão `REJECTED`.
3. **Autorização E3 (CKG-009):** escritor autorizado + identidade autenticada; produtor não redefine ontologia ⇒ senão `REJECTED`.
4. **Ontologia/integridade (CKG-001):** tipo ∈ catálogo ∧ matriz §D2.1 ⇒ senão `REJECTED`.
5. **Proveniência (CKG-005):** `computed_by` (produtor) presente ∧ [gate ⇒ gate_record] ∧ [derivado ⇒ lineage] ⇒ senão `REJECTED`.
6. **Causalidade (CKG-008, se CAUSA):** mechanism+direction+conditions+regime+posthoc_flag+outcome(ou no_outcome) ⇒ senão `REJECTED`.
7. **Colisão (CKG-013):** se forma par contraditório no escopo §D2.2 com validade sobreposta, ambas não-SUPERSEDED e (INVALIDA×alvo) alvo ainda VIGENTE (cond. (v) — N-08), grava `collision_record` (MARCAÇÃO não-destrutiva; não sobrescreve). **[A-11/N-05]** dois modos de INVALIDA (ver RULE-CKG-013): a INVALIDA **AUTORIZADA** fecha o `valid_to` do alvo no MESMO ATO ATÔMICO (um commit) ⇒ alvo não-vigente ⇒ NÃO colide (cond. (v) avaliada sobre o estado resultante dos dois registros, nunca no instante intermediário — independe da ordem de escrita); a INVALIDA **CONTESTADA/PENDENTE** (sem fechamento) é ADMITIDA (preservada, N-08), o alvo permanece vigente e a cond. (v) é alcançável ⇒ `collision_record`.
8. **Escrita append-only (CKG-006/012):** novo registro; substituição ⇒ sucessora com `supersedes`+`expected_version` (sem fork); DELETE/UPDATE proibido.
9. **Temporalidade (CKG-004):** relações carregam `valid_from`/`valid_to`/`recorded_at`; invalidação é ato AUTORIZADO (novo registro), não cascata (CEM-001 l.602).

> **Nota de fronteira:** memória de **trabalho**/versão = SPEC-004; **notificação** = SPEC-005; **formação** = SPEC-007.
> A SPEC-006 só **preserva, relaciona e consulta** o conhecimento permanente. [FONTE: ROADMAP §5/§6/§7]

---

## D7 — Cenários de Teste (19 — T01..T19)

### Cenário-CKG-T01 — ORIGINA com origem ICT → rejeição (matriz §D2.1 / CKG-001)
```
DADO        uma relação ORIGINA cuja origem (hypothesis — única origem de ORIGINA, N-01) tem `school` derivado do produtor = ICT (ICT nunca origina — INV-02/RULE-HH-004; SPEC-001 l.108/l.515-520)
QUANDO      o gate de integridade (§D2.1) roda
ENTÃO       escrita rejeitada; nada persistido
VERIFICAÇÃO written == false; rejected_reason == "ORIGINA_ICT_FORBIDDEN" (∈ ONTOLOGY_INTEGRITY_VIOLATION — §D3.1)
```

### Cenário-CKG-T15 — HERDA SMC-SUB → Elliott-PRIMARY (positivo; entre escolas é VÁLIDO)
```
DADO        hipótese SUB (produtor SMC, SUB) com parent_id → hipótese PAI (produtor Elliott, PRIMARY)
QUANDO      a relação HERDA é escrita
ENTÃO       aceita (entre escolas permitido — RULE-HH-003; HERDA valida só pai=PRIMARY, e pai PRIMARY é Elliott — A-04); nada rejeitado (contraste NEGATIVO: pai SMC-PRIMARY = T18)
VERIFICAÇÃO relation_written == true; cross_school_herda_allowed == true; parent_hierarchy_role == "PRIMARY"; parent_school == "Elliott"
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

### Cenário-CKG-T09 — Formado sem selo rejeitado; admissão positiva POR TIPO (hypothesis/evidence) com trajetória; conviction NEGADO por padrão (CKG-010/002/N-01/N-07)
```
DADO        padrão formado SEM selo SPEC-007; e, à parte: (a) hypothesis ACTIVE→REFUTED com `canonical_history_ref` RESOLVÍVEL no canônico (trajetória PASSOU por ACTIVE — validada antes de refutada; CHM-001); (b) evidence ACTIVE→SUPERSEDED com `canonical_history_ref` RESOLVÍVEL (trajetória PASSOU por ACTIVE — CEM-001 l.258-262); (c) conviction com `canonical_status=COMPUTED` submetido para admissão (o CCM-001 l.58/78 define só o enum `status`; NÃO há histórico de transições; M-001 Cap.5 l.117 ABERTA)
QUANDO      o gate de fronteira roda
ENTÃO       formado sem selo rejeitado; (a)/(b) ADMITIDAS (cada trajetória passou pelo estado de validação do SEU tipo — A-02/N-01) com registro canonical_state_transition (estado preservado a partir da admissão); **(c) conviction REJEITADO por padrão `CONVICTION_HISTORY_UNDEFINED` (N-07) — NÃO se assume COMPUTED→SUPERSEDED como trajetória resolvível; a admissão de conviction é [PROPOSTA]/[DECISÃO NECESSÁRIA], de Andraus**
VERIFICAÇÃO formed_without_seal_accepted == false; hypothesis_admitted_trajectory_active_or_dominant == true; evidence_admitted_trajectory_active == true; conviction_denied_history_undefined == true; conviction_state_transition_recorded == false; canonical_history_ref_resolved_from_canonical == true
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

### Cenário-CKG-T16 — Marcador pós-hoc por instante de FORMULAÇÃO + desfecho obrigatório + carimbo derivado (CKG-008/M-04/N-02/A-01)
```
DADO        (a) CAUSA(A→B) com todos os campos e `formulated_at` (1ª versão da cadeia supersedes) POSTERIOR ao `outcome_timestamp`, submetida com posthoc_flag=false; (b) CAUSA sem outcome_ref e sem no_outcome; (c) CAUSA com `outcome_timestamp` de payload POSTERIOR ao `recorded_at` do registro apontado por `outcome_ref`; (d) CAUSA com `no_outcome=true` E `outcome_ref` presente; (e) CAUSA cujo `formulated_at` é ANTERIOR ao `outcome_timestamp` (afirmação formulada ANTES do desfecho) e posthoc_flag=false
QUANDO      o gate de saída (CKG-008) roda
ENTÃO       (a) rejeitada `POSTHOC_FLAG_REQUIRED` (formulada APÓS o desfecho exige posthoc_flag=true); (b) rejeitada `OUTCOME_REF_MISSING`; (c) rejeitada `OUTCOME_TIMESTAMP_INVALID` (carimbo deriva do recorded_at do apontado — N-02); (d) rejeitada `NO_OUTCOME_CONFLICT`; (e) ACEITA (não pós-hoc — formulada antes do desfecho; posthoc_flag=false legítimo — A-01)
VERIFICAÇÃO posthoc_rule_enforced == true; outcome_ref_required == true; outcome_timestamp_derived_from_ref == true; posthoc_baseline_is_formulated_at == true; case_e_accepted_not_posthoc == true; no_outcome_conflict_rejected == true
```

### Cenário-CKG-T17 — Commit direto do produtor (computed_by como writer_id) → DENY (CKG-009/005/D6 capacidade×papel) [E3]
```
DADO        um AGENTE produtor autenticado tenta COMMITAR diretamente um nó (apresenta-se como `writer_id`, i.e. `computed_by == writer_id == agente`) — capacidade "Commit permanente E3" do agente = DENY na tabela D6
QUANDO      o gate E3 de autorização/identidade roda
ENTÃO       negado; só o COMMITTER autorizado (runtime/serviço do KG) escreve; o agente permanece apenas PRODUTOR (`computed_by`)
VERIFICAÇÃO write_allowed == false; producer_as_committer_denied == true; computed_by_distinct_from_writer_id == true; rejected_reason == "WRITE_UNAUTHORIZED"
```

### Cenário-CKG-T18 — HERDA sub → pai SMC-PRIMARY → rejeição (PRIMARY só Elliott) (CKG-001/A-04)
```
DADO        uma hipótese SUB com parent_id → hipótese PAI cujo `hierarchy_role=PRIMARY` e `school=SMC` (PRIMARY não-Elliott)
QUANDO      o gate de nó/integridade (§D2.1) roda
ENTÃO       rejeitada; só Elliott cria a primária (SPEC-001 RULE-HH-002 l.100); contraste com T15 (pai Elliott-PRIMARY é VÁLIDO)
VERIFICAÇÃO written == false; rejected_reason == "PRIMARY_NOT_ELLIOTT" (∈ ONTOLOGY_INTEGRITY_VIOLATION)
```

### Cenário-CKG-T19 — hypothesis com school não derivável → DENY fail-closed (CKG-001/A-04)
```
DADO        (a) um `hypothesis` cujo `producer` está FORA de AUTHORIZED_PRODUCERS (ex.: Structural Agent — SAS-001 §6.11); (b) um `hypothesis` com `canonical_ref=null`; (c) um `hypothesis` admitido pelo caminho (b) selo SPEC-007 (`publication.origin=spec007_seal`)
QUANDO      o gate de integridade roda
ENTÃO       (a) DENY `HYPOTHESIS_PRODUCER_UNAUTHORIZED` (school não derivável ⇒ também `SCHOOL_NOT_DERIVABLE`); (b) DENY `HYPOTHESIS_CANONICAL_REF_MISSING`; (c) DENY `HYPOTHESIS_VIA_SEAL_FORBIDDEN`; nunca falha-aberto
VERIFICAÇÃO written == false; fail_open == false; school_not_derivable_denied == true
```

---

## D8 — Rigor adversarial focado (casos de negação nos pontos de risco)

> **23 casos** cobrindo as 13 BASpecs + fronteiras/decisões abertas. Transversal: **fail-closed**, **nunca deletar/mutar**, **mecanismo físico INDETERMINADO (H-001)**. Todo `rejected_reason` de RUNTIME consta de §D3.1; ADV-08/09/10 são checagens de REVISÃO/spec-time (A-13), não gates de runtime.

### ADV-CKG-01 — Deleção disfarçada de "esquecimento" (CKG-006)
**DADO:** "esquecer" traduzido em DELETE físico. **QUANDO:** o gate roda. **ENTÃO:** negar; só arquivamento versionado. **PORQUE:** INV-07. **VERIFICAÇÃO:** physical_delete == false.

### ADV-CKG-02 — Sobrescrita silenciosa de relação contraditória (CKG-013)
**DADO:** REFUTA(A→B) sobre CONFIRMA(A→B). **QUANDO:** a escrita roda. **ENTÃO:** registrar colisão; preservar ambas. **PORQUE:** perder a contradição apaga conhecimento. **VERIFICAÇÃO:** silent_overwrite == false; both_relations_present == true.

### ADV-CKG-03 — Confiança retroalimenta o Conviction Vector (CKG-007/INV-04)
**DADO:** expor a confiança no objeto de convicção, somá-la como 9ª dimensão, ou criar aresta `to_node==conviction`. **QUANDO:** a escrita/escopo roda. **ENTÃO:** rejeitar `EDGE_TO_CONVICTION_FORBIDDEN`; namespace próprio. **PORQUE:** INV-04; dimensionalidade=8 (fechada). **VERIFICAÇÃO:** confidence_exposed_in_conviction_object == false; any_edge_to_conviction_written == false.

### ADV-CKG-04 — Causal pós-hoc por correlação, sem desfecho/marcador (CKG-008/RULE-CAU)
**DADO:** CAUSA(A→B) só por co-ocorrência, (a) sem mechanism/regime; (b) com `formulated_at` > `outcome_timestamp` (formulada APÓS o desfecho) e posthoc_flag=false; (c) sem outcome_ref e sem no_outcome; (d) com `outcome_timestamp` de payload posterior ao `recorded_at` do registro apontado por `outcome_ref`; (e) com `no_outcome=true` E `outcome_ref` presente; **(f) CONTRASTE POSITIVO:** CAUSA bem-formada cujo `formulated_at` é ANTERIOR ao `outcome_timestamp` (formulada ANTES do desfecho) com posthoc_flag=false; **(g) RACIONALIZAÇÃO PÓS-HOC POR REESCRITA [N-02]:** uma SUCESSORA (cadeia `supersedes`) de uma CAUSA, escrita DEPOIS do desfecho, que REESCREVE `mechanism`/`direction`/`conditions`/`regime` e tenta herdar o `formulated_at` antigo passando com posthoc_flag=false; **(h) RACIONALIZAÇÃO POR TROCA DE DESFECHO [m-A]:** uma SUCESSORA (cadeia `supersedes`), escrita DEPOIS do desfecho, que mantém mechanism/direction/conditions/regime mas TROCA o `outcome_ref` por um registro posterior (deslocando o `outcome_timestamp` derivado) OU liga `no_outcome=true`, tentando herdar o `formulated_at` antigo e passar com posthoc_flag=false. **QUANDO:** o gate roda. **ENTÃO:** (a)–(e) rejeitar `CAUSAL_FIELDS_MISSING`/`POSTHOC_FLAG_REQUIRED`/`OUTCOME_REF_MISSING`/`OUTCOME_TIMESTAMP_INVALID`/`NO_OUTCOME_CONFLICT`; (f) ACEITAR (não pós-hoc — A-01); **(g)/(h) rejeitar `CAUSAL_CORE_IMMUTABLE_IN_CHAIN`** (núcleo causal imutável na cadeia inclui mechanism/direction/conditions/regime E `outcome_ref` E `no_outcome` — m-A; corrigir qualquer item exige NOVA CAUSA com `valid_from`/`formulated_at` próprios, aposentando a antiga por INVALIDA — caminho legítimo m-C). **PORQUE:** correlação não é causalidade; o baseline pós-hoc é o instante de FORMULAÇÃO, não o `recorded_at` do registro corrente (que seria sempre posterior ao desfecho, degenerando RULE-CAU-03 — A-01); carimbo do desfecho deriva do registro apontado (M-04/N-02); reescrever o núcleo causal — inclusive TROCAR o desfecho (`outcome_ref`/`no_outcome`) — via `supersedes` laundry o `formulated_at` e burlaria o marcador pós-hoc (N-02/m-A). **VERIFICAÇÃO:** cases_a_to_e_written == false; case_f_accepted_not_posthoc == true; case_g_causal_core_immutable_denied == true; case_h_outcome_swap_denied == true; posthoc_rule_enforced == true; posthoc_baseline_is_formulated_at == true; outcome_ref_required == true; outcome_timestamp_derived_from_ref == true.

### ADV-CKG-05 — Métrica de custo ligada à convicção via nó do KG (INV-04)
**DADO:** `calibration_metric`/custo ligado à convicção via aresta. **QUANDO:** a escrita roda. **ENTÃO:** armazenar a métrica (CEE-001 l.111) ISOLADA; rejeitar `EDGE_TO_CONVICTION_FORBIDDEN`. **PORQUE:** INV-04 — o CUSTO nunca entra no Conviction Vector. **VERIFICAÇÃO:** any_edge_to_conviction_written == false.

### ADV-CKG-06 — Escrita sem proveniência aceita (CKG-005)
**DADO:** nó/relação sem provenance_ref. **QUANDO:** o gate roda. **ENTÃO:** rejeitar `PROVENANCE_MISSING`. **PORQUE:** sem origem não é reconstruível (P13). **VERIFICAÇÃO:** written == false.

### ADV-CKG-07 — Produtor redefine ontologia/taxonomia (CKG-009/SAS-001 §6.12)
**DADO:** produtor autenticado tenta alterar a ontologia global. **QUANDO:** o gate E3 roda. **ENTÃO:** negar `ONTOLOGY_REDEFINITION_FORBIDDEN`; produtor registra, não redefine. **PORQUE:** SAS-001 §6.12 (extensão a outros produtores = [INFERÊNCIA]). **VERIFICAÇÃO:** ontology_redefined_by_producer == false.

### ADV-CKG-08 — KG forma conhecimento / absorve SPEC-007 (CKG-010/fronteira) [CHECAGEM DE REVISÃO/SPEC-TIME — A-13]
> **Reclassificado (A-13):** é checagem de ESCOPO de SPEC-TIME (o Revisor verifica que a Spec não especifica formação/retrieval) — NÃO um gate de runtime. `OUT_OF_SCOPE_FORMATION` é marcador de revisão, não `rejected_reason` executável em runtime.
**DADO:** a Spec tentaria especificar extração/retrieval/validação no KG. **QUANDO:** a revisão de escopo roda (spec-time). **ENTÃO:** achado de revisão — fora de escopo; formação é SPEC-007. **PORQUE:** formação é SPEC-007. **VERIFICAÇÃO (revisão):** a Spec não contém comportamento de formação/retrieval (conferível por leitura).

### ADV-CKG-09 — Mecanismo físico fixado por inércia (CONS-01/mandato) [CHECAGEM DE REVISÃO/SPEC-TIME — A-13]
> **Reclassificado (A-13):** governança de spec-time (o Revisor/Andraus verificam que a Spec não fecha H-001), NÃO gate de runtime. `OPEN_DECISION_H001` é marcador de revisão, não `rejected_reason` de runtime.
**DADO:** pressão para fixar "grafo real"/escolher engine na Spec. **QUANDO:** a revisão de decisões abertas roda (spec-time). **ENTÃO:** achado de revisão — mecanismo físico permanece INDETERMINADO; Opção B ADIADA. **PORQUE:** H-001 é de Andraus (CONS-01). **VERIFICAÇÃO (revisão):** a Spec não fecha H-001 (conferível por leitura — grep de fechamento = 0).

### ADV-CKG-10 — Absorver vizinhos / tocar decisão aberta (fronteiras/CONS-01) [CHECAGEM DE REVISÃO/SPEC-TIME — A-13]
> **Reclassificado (A-13):** checagem de ESCOPO de spec-time, NÃO gate de runtime. `OUT_OF_SCOPE_OR_OPEN_DECISION` é marcador de revisão, não `rejected_reason` de runtime.
**DADO:** a SPEC-006 tentaria virar memória de trabalho (SPEC-004), transporte (SPEC-005), estado por agente (SPEC-009), ciclo P12 (SPEC-018), ou tocar M-001/J-001/N-001/G-001/K-001/C-001/WF-D03. **QUANDO:** a revisão de escopo roda (spec-time). **ENTÃO:** achado de revisão — decisões abertas permanecem ABERTAS (Andraus). **PORQUE:** CONS-01; INV-09. **VERIFICAÇÃO (revisão):** vizinhos não absorvidos; decisões abertas não tocadas (conferível por leitura).

### ADV-CKG-11 — Nó redefine contrato canônico / transição proibida (CKG-002/CC-02)
**DADO:** nó-hipótese sobrescreve campos/estado do CHM-001, ou transição INVALIDATED→ACTIVE. **QUANDO:** a escrita roda. **ENTÃO:** rejeitar (`CANONICAL_CONTRACT_REDEFINITION_FORBIDDEN` para redefinição de campos/estado; `FORBIDDEN_CANONICAL_TRANSITION` para a transição proibida — ambos em §D3.1, N-04); referencia por id@version, não redefine. **PORQUE:** CC-02/CONST-01; INV-10; CEM-001 l.473-475. **VERIFICAÇÃO:** canonical_contract_redefined == false; forbidden_canonical_transition_rejected == true.

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
**DADO:** (a) A1 CONFIRMA B, A2 REFUTA B (A1≠A2) — não colide; (b) CONFIRMA(A→B)/REFUTA(A→B) com janelas DISJUNTAS — não colide; (c) ambas vigentes com sobreposição — colide; (d) **INVALIDA CONTESTADA/PENDENTE [N-05]** vigente com `target_relation_id==R.relation_id` sobre R que **PERMANECE VIGENTE** (afirmada SEM o registro de fechamento do `valid_to` de R; é ADMITIDA — preservada, N-08 — e satisfaz a condição (v) §D2.2) — colide (MARCAÇÃO, não rejeição); (e) CONFIRMA(A→B) SUPERSEDED vs REFUTA(A→B) vigente — não colide; (f) **INVALIDA AUTORIZADA [N-05] que FECHOU a validade de R** (R agora INVALIDATED_IN_TIME / não-vigente — invalidação autorizada NORMAL, ato atômico A-11) — **NÃO colide (N-08)**. **QUANDO:** o detector roda. **ENTÃO:** (a)/(b)/(e)/(f) não geram colisão; (c)/(d) geram. **PORQUE:** colisão = par §D2.2 no escopo do par, sobreposição, ambas não-SUPERSEDED e (INVALIDA×alvo) alvo ainda vigente (v); invalidação autorizada normal não colide por construção. **[A-11]** Como a INVALIDA e o fechamento do `valid_to` do alvo são um ÚNICO ATO ATÔMICO e a cond. (v) é avaliada sobre o estado resultante dos dois registros (nunca no instante intermediário), o resultado de (d)/(f) INDEPENDE da ordem de escrita — não há janela em que a INVALIDA já exista e R ainda apareça vigente por mero atraso de registro. **VERIFICAÇÃO:** collision_logged == [false,false,true,true,false,false] para (a..f); collision_decision_order_independent == true.

### ADV-CKG-19 — FORK de versão / ordem violada (CKG-006/012)
**DADO:** duas sucessoras apontando `supersedes` para a MESMA versão (fork), ou `expected_version` ausente, ou `expected_version` ≠ corrente, ou `version` ≠ anterior+1. **QUANDO:** o gate roda. **ENTÃO:** negar — fork ⇒ `VERSION_FORK_FORBIDDEN`; ausência ⇒ `EXPECTED_VERSION_REQUIRED`; divergência ⇒ `VERSION_CONFLICT` (compare-and-commit, CBP-004 l.239-246/l.243-244 — N-04). **PORQUE:** sem ordem total não há estado inequívoco (INV-07). **VERIFICAÇÃO:** second_successor_written == false; version_fork == false.

### ADV-CKG-20 — ciclo na linhagem DERIVA_DE (CKG-003/INV-CKG-02; M-02)
**DADO:** arestas A DERIVA_DE B e B DERIVA_DE C já gravadas (C ancestral de B ancestral de A); tentativa C DERIVA_DE A — a origem C já é alcançável a partir do destino A (A→B→C), fecharia ciclo. **QUANDO:** o gate de relação roda. **ENTÃO:** rejeitar `LINEAGE_CYCLE`; o grafo permanece ACÍCLICO (o trace sempre termina). **PORQUE:** linhagem cíclica quebra a Trace Reconstruction (INV-CKG-02). **Caso (c) — self-loop:** DERIVA_DE com origem == destino ⇒ rejeitar `LINEAGE_CYCLE`. **VERIFICAÇÃO:** lineage_cycle_written == false; lineage_acyclic == true.

### ADV-CKG-21 — admissão de canônico em estado NÃO-admissível / sem selo (CKG-010)
**DADO:** o gate de admissão POR TIPO (não só hypothesis): (a) `hypothesis` com `canonical_status=EMERGENT`; (b) formado SEM selo SPEC-007; (c) `evidence` com `canonical_status` FORA do seu conjunto {ACTIVE,SUPERSEDED,INVALIDATED,ARCHIVED} — ex.: `DOMINANT` (estado só de hipótese, CEM-001 l.258-262 não tem REFUTED/DOMINANT); **(d) [N-07]** `conviction` submetido em QUALQUER status (ex.: `COMPUTED` ou `SUPERSEDED`); **(e) [A-02 — TRAJETÓRIA]** `hypothesis` com `canonical_status=ARCHIVED` cuja TRAJETÓRIA é EMERGENT→ARCHIVED (hipótese órfã NUNCA validada — CHM-001 l.745 — jamais passou por ACTIVE), embora ARCHIVED esteja no conjunto admissível; **(f) [N-01 — TRAJETÓRIA POR TIPO; m-D — DEFESA EM PROFUNDIDADE]** `evidence` com `canonical_status=ARCHIVED` cujo `canonical_history_ref` está CORROMPIDO/NÃO-RESOLVÍVEL (de modo que não se comprova a passagem por ACTIVE) — note que, no caminho feliz, "esteve em ACTIVE" é TAUTOLÓGICO para `evidence` (ACTIVE é o estado padrão e toda trajetória da Evidência parte dele; ARCHIVED tem como predecessores ACTIVE, SUPERSEDED e INVALIDATED, e estes dois só são alcançados a partir de ACTIVE — CEM-001 l.446-447/l.460-466; RULE-CKG-010 [m-D/n-b]), logo este predicado é SALVAGUARDA contra histórico corrompido, NÃO rejeição de evidence bem-formada; **(g) [N-07]** `conviction` com `canonical_status=SUPERSEDED` (ou qualquer outro) submetido para admissão; **(h) [N-01 — PROVA DA TRAJETÓRIA]** objeto canônico hypothesis/evidence submetido SEM `canonical_history_ref` resolvível no canônico (ou com trajetória declarada só no payload). **QUANDO:** o gate de fronteira roda. **ENTÃO:** (a)/(c) rejeitar `CANONICAL_STATUS_NOT_ADMISSIBLE`; (b) `FORMED_WITHOUT_SEAL`; **(d)/(g) rejeitar `CONVICTION_HISTORY_UNDEFINED`** (`conviction` é NEGADO POR PADRÃO — N-07; NÃO se assume trajetória COMPUTED/GATED_PASS resolvível: o CCM-001 l.58/78 só define o enum, M-001 Cap.5 l.117 ABERTA; a admissão de conviction é [PROPOSTA]/[DECISÃO NECESSÁRIA]); **(e)/(f) rejeitar `TRAJECTORY_NEVER_ACTIVE`** (status corrente admissível NÃO basta — exige ter passado pelo estado de validação do SEU tipo; predicado POR TIPO, opção conservadora; para evidence, defesa em profundidade — A-02/N-01/m-D); **(h) rejeitar `CANONICAL_HISTORY_UNRESOLVABLE`** (a prova da trajetória vem do canônico, nunca do payload — N-01); o conjunto admissível e a trajetória são POR TIPO (hypothesis: ACTIVE∨DOMINANT; evidence: ACTIVE; conviction: NEGADO por padrão — N-07). **PORQUE:** não contaminar memória permanente com trabalho/estado fora da máquina canônica do tipo nem com conhecimento NUNCA validado, nem admitir trajetória auto-declarada no payload, nem atribuir ao CCM-001 um histórico que ele não define (CEM-001 l.258-262/l.446-447/l.460-466; CHM-001 §4.3 l.744-748; CCM-001 l.58/78 + Cap.5 l.117; CBP-014; SPEC-004). **VERIFICAÇÃO:** emergent_hypothesis_admitted == false; formed_without_seal_accepted == false; evidence_nonadmissible_status_admitted == false; conviction_admitted_any_status == false; conviction_denied_history_undefined == true; never_validated_admitted_any_type == false; canonical_history_from_payload_admitted == false.

### ADV-CKG-22 — Produtor comita direto (computed_by == writer_id == agente) (CKG-009/005/D6) [E3]
**DADO:** um agente produtor tenta ser o COMMITTER (apresenta `writer_id` = sua própria identidade de produtor), contornando o runtime/serviço do KG. **QUANDO:** o gate E3 (capacidade×papel, D6) roda. **ENTÃO:** negar `WRITE_UNAUTHORIZED`; `computed_by` (produtor) e `writer_id` (committer) permanecem DISTINTOS; commit direto por agente = DENY. **PORQUE:** identidade não depende do payload (CBP-014); capacidade "Commit permanente E3" do agente = DENY (D6; M-05). **VERIFICAÇÃO:** write_allowed == false; producer_as_committer_denied == true; computed_by_distinct_from_writer_id == true.

### ADV-CKG-23 — hypothesis com proteção INV-02/RULE-HH-002 só aparente (gate falha-aberto) (CKG-001/A-04)
**DADO:** tentativas de burlar o gate de nó por caminhos NÃO cobertos por "rejeitar só school==ICT": (a) `hypothesis` cujo `producer` está FORA de AUTHORIZED_PRODUCERS (Structural Agent — SAS-001 §6.11) de modo que a `school` não é derivável; (b) `hypothesis` com `hierarchy_role=PRIMARY` e `school=SMC` (PRIMARY não-Elliott); (c) `hypothesis` injetada pelo caminho (b) selo SPEC-007 (`publication.origin=spec007_seal`). **QUANDO:** o gate de integridade roda. **ENTÃO:** (a) DENY `SCHOOL_NOT_DERIVABLE`/`HYPOTHESIS_PRODUCER_UNAUTHORIZED` (NUNCA falha-aberto); (b) DENY `PRIMARY_NOT_ELLIOTT`; (c) DENY `HYPOTHESIS_VIA_SEAL_FORBIDDEN`. **PORQUE:** a proteção de INV-02/RULE-HH-002 precisa ser EFETIVA, não aparente — o gate não pode cair aberto quando a `school` não é derivável (A-04). **VERIFICAÇÃO:** fail_open == false; primary_not_elliott_denied == true; hypothesis_via_seal_denied == true; school_not_derivable_denied == true.

> **Cobertura:** 23 casos — toda BASpec tem ≥1 negação: CKG-001→ADV-12/17/23, T01/T18/T19; 002→ADV-11, T02; 003→ADV-12/16/20, T03;
> 004→ADV-13, T04; 005→ADV-06/22, T14/T17; 006→ADV-01/19, T05; 007→ADV-03/05, T06; 008→ADV-04, T07/T16; 009→ADV-07/22, T08/T17;
> 010→ADV-08/21, T09; 011→ADV-14, T10; 012→ADV-15/19, T13; 013→ADV-02/18, T11. ADV-21 cobre admissão POR TIPO
> (hypothesis/evidence/conviction). Fronteiras/decisões abertas: ADV-09/10. Mapeiam para EC-CKG-001..006 (fail-closed).

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
    "expected_version": "OBRIGATÓRIO na atualização (== versão corrente no commit); ausência ⇒ DENY EXPECTED_VERSION_REQUIRED, divergência ⇒ DENY VERSION_CONFLICT (códigos de origem SPEC-004 CBP-004 l.243-244 — N-04); criação inicial não exige",
    "supersedes": "null | KG-N-...-v0 (sucessão de CONTEÚDO ⇒ SUPERSEDED; aponta p/ ÚLTIMA versão; version==anterior+1; sem FORK)",
    "targets_record_id": "null | KG-N-...-R0 (registro que invalidation/archival REFERENCIA — DISTINTO de supersedes; invalidação ⇒ INVALIDATED_IN_TIME)",
    "node_type": "hypothesis | evidence | observation | conviction | narrative | mission | learning | asset | timeframe | regime | structure | calibration_metric",
    "schema_version": "1 (migração de ontologia/schema = [DECISÃO NECESSÁRIA] — CKG-009)",
    "canonical_ref": "CHM-xxxx@v2 | CEM-xxxx@v1 | CCM-xxxx@v1 | null (referência; NÃO redefine)",
    "canonical_status": "snapshot do Status canônico (CEM-001 l.264/428; CHM-001; só se canonical_ref != null); admissível ∈ conjunto do tipo (CKG-010)",
    "canonical_history_ref": "OBRIGATÓRIO na admissão de nó canônico hypothesis/evidence (N-01) — REFERENCIA o histórico de estados MANTIDO NO PRÓPRIO CANÔNICO (CHM-001 p/ hypothesis; CEM-001 p/ evidence); RESOLVIDO contra o canônico, NUNCA do payload (CBP-014); sustenta o predicado de TRAJETÓRIA POR TIPO (CKG-010): hypothesis esteve em ACTIVE∨DOMINANT; evidence em ACTIVE; irresolúvel ⇒ DENY CANONICAL_HISTORY_UNRESOLVABLE; jamais-validado ⇒ DENY TRAJECTORY_NEVER_ACTIVE. **conviction: NÃO há histórico canônico a referenciar — CCM-001 l.58/78 só define o enum `status`, M-001 (Cap.5 l.117) ABERTA — logo `conviction` é NEGADO POR PADRÃO (DENY CONVICTION_HISTORY_UNDEFINED, N-07); o campo/predicado de conviction é [PROPOSTA]/[DECISÃO NECESSÁRIA]**",
    "natural_key": "identidade de nó NÃO-canônico — asset/timeframe/regime/narrative/observation/learning/structure/mission/calibration_metric (lista completa — M-06); evita colapso quando canonical_ref=null",
    "school": "Elliott | SMC | Fibonacci — DERIVADO do producer_id/producer_type do canônico (hypothesis: CHM-001 l.361/SPEC-001 l.97/524); NÃO do payload; SÓ para hypothesis (N-01); REGRA: hypothesis.school ≠ ICT (ICT não é produtor — INV-02/RULE-HH-004); **NÃO derivável ⇒ DENY SCHOOL_NOT_DERIVABLE (fail-closed, nunca falha-aberto — A-04)**. structure NÃO deriva school; Fractal não tem produtor em SPEC-001 — CKG-STRUCT-ORIGIN-001 [DECISÃO NECESSÁRIA]",
    "hierarchy_role": "PRIMARY | SUB — DERIVADO do papel registrado no canônico (SPEC-001); só hypothesis; **PRIMARY ⇒ school=Elliott (só Elliott cria a primária — SPEC-001 RULE-HH-002 l.100; senão DENY PRIMARY_NOT_ELLIOTT — A-04)**; HERDA liga SUB a pai PRIMARY",
    "ontological_status": "observational | theoretical (RULE-ONT-01; só structure/regime/narrative — distingue entidade medida de construção teórica, ex.: order block/liquidez)",
    "provenance_ref": { "computed_by": "OBRIGATÓRIO — identidade AUTENTICADA do PRODUTOR (CBP-014; M-05)", "gate_record": "CONDICIONAL — só se resulta de gate (CBP-007)", "lineage": "CONDICIONAL — só se DERIVADO (ref. Lineage CEM-001 Cap.5 / derived_from[] SPEC-004; [] legítimo p/ PRIMARY/asset/timeframe/regime/observation)", "who": "humano-legível (auditoria; pode diferir de computed_by)", "when": "", "why": "", "from": "" },
    "publication": { "origin": "canonical_lifecycle | spec007_seal — DERIVADO do CANAL/identidade AUTENTICADA (não do payload); **hypothesis com origin=spec007_seal ⇒ DENY HYPOTHESIS_VIA_SEAL_FORBIDDEN — hipótese só entra pelo ciclo de vida canônico (A-04)**", "seal_ref": "[DECISÃO NECESSÁRIA — contrato do selo = SPEC-007]" },
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
    "canonical_status": "ACTIVE|DOMINANT|SUPERSEDED|REFUTED|ARCHIVED (hypothesis/CHM-001) | ACTIVE|SUPERSEDED|INVALIDATED|ARCHIVED (evidence/CEM-001 l.258-262 — sem REFUTED). **conviction: o enum CCM-001 l.58/78 (COMPUTED|GATED_PASS|GATED_BLOCK|SUPERSEDED) NÃO habilita admissão — `conviction` é NEGADO POR PADRÃO (CONVICTION_HISTORY_UNDEFINED — N-07; CCM-001 não define histórico de transições; M-001 Cap.5 l.117 ABERTA), logo não gera canonical_state_transition_record nesta versão.** EMERGENT/CANDIDATE NÃO constam — o histórico do KG começa na ADMISSÃO (regra LOCAL CKG-010 — A-03); admissão (hypothesis/evidence) exige TRAJETÓRIA que passou pelo ESTADO DE VALIDAÇÃO DO TIPO (hypothesis ACTIVE∨DOMINANT; evidence ACTIVE — A-02/N-01), provada via canonical_history_ref resolvido no canônico (nunca do payload)",
    "timestamp": "", "origem": "", "justificativa": "(CEM-001 l.428)",
    "computed_by": "SERVIÇO do KG (identidade autenticada — M-05)",
    "writer_id": "SERVIÇO do KG (committer; escrita E3 — M-05)",
    "recorded_at": "2026-10-12T12:00:00Z",
    "transition_validated": "VALIDA contra a tabela do tipo (CHM/CEM): transição proibida (CEM-001 l.473-475) ⇒ FORBIDDEN_CANONICAL_TRANSITION; reativação de estado terminal VETADA"
  },
  "relation_record": {
    "relation_id": "KG-R-2026-10-12-001",
    "record_kind": "creation | invalidation | archival (colisão é registro PRÓPRIO `collision_record`, NÃO um record_kind de relação — N-04)",
    "version": "monotônico (invalidation/archival têm sequência própria — m-10)",
    "expected_version": "OBRIGATÓRIO na atualização (ausência ⇒ DENY EXPECTED_VERSION_REQUIRED; divergência ⇒ DENY VERSION_CONFLICT — N-04); criação não exige",
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
    "causal": "{ mechanism, direction, conditions, regime, posthoc_flag:boolean, outcome_ref, outcome_timestamp (DERIVADO — ver nota), formulated_at (DERIVADO — ver nota), no_outcome?:boolean+justificativa } — obrigatório sse relation_type==CAUSA (RULE-CAU-01/02/03); `outcome_ref` OBRIGATÓRIO salvo `no_outcome=true` (XOR — no_outcome+outcome_ref ⇒ NO_OUTCOME_CONFLICT, M-04); `outcome_timestamp` NÃO vem do payload: DERIVADO do `recorded_at` do registro apontado por `outcome_ref` (payload posterior ⇒ OUTCOME_TIMESTAMP_INVALID — N-02); `formulated_at` NÃO vem do payload: DERIVADO do `recorded_at` da 1ª versão da cadeia `supersedes` desta CAUSA (alternativa "hipótese referenciada" REMOVIDA — N-02) — A-01; **sucessora que ALTERA o núcleo causal (RULE-CKG-008) = mechanism/direction/conditions/regime/outcome_ref/no_outcome ⇒ DENY `CAUSAL_CORE_IMMUTABLE_IN_CHAIN` (N-02/m-A; correção exige NOVA CAUSA com formulated_at próprio)**; posthoc_flag DEVE ser true quando formulated_at > outcome_timestamp e é legitimamente false quando formulated_at ≤ outcome_timestamp (o recorded_at do registro corrente NÃO é o baseline — seria sempre posterior ao desfecho)",
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
PRECOND      : (tipo ∈ ontologia ∧ matriz §D2.1 ∧ [hypothesis ⇒ fail-closed A-04: canonical_ref≠null ∧ producer∈AUTHORIZED_PRODUCERS ∧ school derivável ∧ (PRIMARY⇒Elliott) ∧ ¬via selo] — CKG-001/003) AND (nó canônico referenciado, não redefinido — CKG-002) AND (proveniência CONDICIONAL: computed_by sempre ∧ [gate⇒gate_record] ∧ [derivado⇒lineage] — CKG-005) AND (fronteira: canonical_status ∈ conjunto admissível do tipo POR TIPO ∧ trajetória de validação do tipo resolvida via canonical_history_ref [N-01] ∨ selo SPEC-007 — CKG-010) AND (CAUSA ⇒ campos CAU + outcome + núcleo causal imutável na cadeia [N-02] — CKG-008) AND (colisão registrada se houver — CKG-013)
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

### EC-CKG-004 — Confiança de relação em namespace próprio (guard de ESCRITA; INV-04) [E3]
```
CAPABILITY   : Na ESCRITA permanente, manter a confiança em namespace próprio e não escrever NENHUMA aresta to_node==conviction
EFFECT       : Guard **na ESCRITA permanente** (E3) de que a confiança não vira campo/aresta de convicção. **[A-14]** O guard de LEITURA (consulta não expõe a confiança em resultado de convicção) é E1 e está em EC-CKG-006 — este EC cobre SÓ a escrita.
PRECOND      : (confiança em namespace separado) AND (matriz §D2.1 proíbe QUALQUER aresta to_node.node_type==conviction, direta ou 2 saltos) — verificado no COMMIT de escrita
POSTCOND     : nenhum campo de convicção recebe a confiança na escrita; nenhuma aresta to_node==conviction é escrita
POLICY       : RULE-CKG-007; INV-04 (custo); CCM-001; SPEC-003
LEVEL        : E3 (Crítico — guard sobre a ESCRITA permanente; atomic-spec §10.2)
FAILURE-MODE : Fail-closed — escrever confiança em campo de convicção / aresta to_node==conviction ⇒ negado; log. Falso-DENY E3 CONDICIONAL (ENF-07)
EVIDENCE     : verificação de namespace separado e ausência de aresta to_node==conviction na escrita + ENF-07. Que o CÁLCULO de convicção (SPEC-003) não a consuma = requisito à SPEC-003 / [DECISÃO NECESSÁRIA] — fora do controle do KG
```

### EC-CKG-005 — Registro de relação causal com mecanismo/regime/desfecho (RULE-CAU) [E3]
```
CAPABILITY   : Admitir CAUSA só com mechanism+direction+conditions+regime+posthoc_flag+outcome (ou no_outcome)
EFFECT       : Escrita (ou recusa) de relação CAUSA — persistência permanente (E3)
PRECOND      : (CAUSA) ⇒ (mechanism ∧ direction ∧ conditions ∧ regime ∧ posthoc_flag booleano ∧ (outcome_ref XOR no_outcome+justificativa) ∧ [outcome_ref ⇒ outcome_timestamp DERIVADO do recorded_at do registro apontado — payload posterior ⇒ OUTCOME_TIMESTAMP_INVALID; no_outcome com outcome_ref ⇒ NO_OUTCOME_CONFLICT] ∧ [formulated_at>outcome_timestamp ⇒ posthoc_flag==true; formulated_at≤outcome_timestamp ⇒ posthoc_flag=false legítimo — A-01] ∧ [sucessora NÃO altera o núcleo causal definido em RULE-CKG-008 = mechanism/direction/conditions/regime/outcome_ref/no_outcome — senão CAUSAL_CORE_IMMUTABLE_IN_CHAIN, N-02/m-A]); (SIMILAR_A por juízo) ⇒ similarity_basis; gate determinístico (Classe H); bounded loop
POSTCOND     : relações causais têm campos auditáveis; nenhuma pós-hoc por correlação sem marcador/desfecho
POLICY       : RULE-CKG-008; RULE-CAU-01/02/03; ENF-03
LEVEL        : E3 (Crítico — write permanente; herda EC-CKG-001)
FAILURE-MODE : Fail-closed — campos ausentes ⇒ rejeitada; retry bounded. Falso-DENY E3 CONDICIONAL (ENF-07)
EVIDENCE     : registro dos campos causais; contagem de tentativas ≤ limite; gate verifica presença, não veracidade (ENF-03) + ENF-07
```

### EC-CKG-006 — Consulta cognitiva / Trace Reconstruction (read-only)
```
CAPABILITY   : Responder consultas e reconstruir a cadeia cognitiva da EVIDÊNCIA (completa) sem alterar estado; **[A-14]** garantir, na LEITURA, que a confiança de relação NÃO é devolvida em campo do objeto de convicção
EFFECT       : Leitura/navegação (sem escrita)
PRECOND      : (consulta read-only) AND (consumidor autorizado a ler) AND **[A-14]** (resultado NÃO expõe `relation_confidence` em campo de convicção — guard de LEITURA, INV-04)
POSTCOND     : resposta/trace da Evidência COMPLETO; trace de hipótese best-effort; nenhum estado alterado; confiança não exposta em objeto de convicção
POLICY       : RULE-CKG-011; RULE-CKG-007 (guard de leitura — A-14); CEM-001 l.608-615/l.612-614; SAS-001 §6.12; INV-04
LEVEL        : E1 (Contratual — leitura observável; não muta estado) — **o guard de leitura da confiança é E1, distinto do guard de ESCRITA E3 (EC-CKG-004) — A-14**
FAILURE-MODE : Fail-closed — consulta que tente mutar ⇒ negada; consulta que exponha confiança em campo de convicção ⇒ filtrada/negada (E1); completude do trace de Evidência é obrigatória; eficiência ampla = INDETERMINADO até H-001
EVIDENCE     : log de consulta read-only; trace = fecho transitivo de DERIVA_DE; verificação de que o resultado não traz `relation_confidence` em campo de convicção
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
e ≥1 caso de negação em D8 (CKG-001→ADV-12/17/23,T01/T18/T19; 002→ADV-11,T02/T09; 003→ADV-12/16/20,T03; 004→ADV-13,T04; 005→ADV-06/22,
T14/T17; 006→ADV-01/19,T05; 007→ADV-03/05,T06; 008→ADV-04,T07/T16 (incl. caso POSITIVO formulated_at<outcome — A-01); 009→ADV-07/22,T08/T17; 010→ADV-08/21,T09 (admissão POSITIVA por tipo — N-01; TRAJECTORY_NEVER_ACTIVE/CANONICAL_HISTORY_UNRESOLVABLE por tipo ficam em ADV-21, não em T09 — N-03); 011→ADV-14,T10; 012→
ADV-15/19,T13; 013→ADV-02/18,T11). "Se a BASpec estivesse errada" é observável em cada caso. Nenhuma restou [DECISÃO
NECESSÁRIA] por falta de verificabilidade (H-001/selo SPEC-007/M-001/J-001/N-001/G-001/K-001/C-001/WF-D03 são fronteiras/
decisões abertas explícitas, não falhas de verificabilidade).

**Bloco B — herança obrigação-a-obrigação (CC-08):** evidência por obrigação herdada:
- CEM-001 "preservar os estados (da Evidência) / trace COMPLETO" → CKG-010 preserva os estados **a partir da admissão** como regra LOCAL (A-03 — o MODIFIED de CEM-001 l.494 foi RETIRADO por premissa falsa; EMERGENT/CANDIDATE são estados da HIPÓTESE e cabem à SPEC-004, não há obrigação canônica de guardá-los no KG) + CKG-011 trace completo da EVIDÊNCIA (não rebaixado por H-001; hipótese = [PROPOSTA]); admissão exige trajetória que passou pelo ESTADO DE VALIDAÇÃO DO TIPO (predicado POR TIPO — A-02/N-01; hypothesis ACTIVE∨DOMINANT, evidence ACTIVE; **conviction NEGADO por padrão — N-07, CCM-001 não define histórico de status, M-001 ABERTA**), provada via `canonical_history_ref` no canônico; não redefine.
- CEM-001 Cap.5 `Lineage` → tipo DERIVA_DE (aresta) + `provenance_ref.lineage` (campo local [PROPOSTA]), distinguidos.
- CHM-001 (estados/versionamento) → CKG-002/012 por referência; não transiciona.
- CCM-001 → CKG-007/EC-CKG-004 isolam confiança (INV-04); `conviction` é **NEGADO por padrão na admissão** (`CONVICTION_HISTORY_UNDEFINED` — N-07; CCM-001 l.58/78 define só o enum `status`, sem histórico de transições; M-001 Cap.5 l.117 ABERTA; pré-requisito/decisão de Andraus), logo nenhum estado de conviction é admitido no KG nesta versão (CKG-010).
- SPEC-004 v1.2 INV-CBP-01/CBP-004 → CKG-004/006/012 (novos registros; compare-and-commit; estado derivado); `computed_by`(produtor)≠`writer_id`(committer) (M-05).
- SPEC-005 (eventos) → **[INFERÊNCIA]/[DECISÃO NECESSÁRIA]** eventual consumo (D6); emissão pelo KG NÃO afirmada (m-08).
- SAS-001 §6.12 → CKG-009/EC-CKG-003 (escopo Structural Agent; extensão a outros produtores = [INFERÊNCIA]).
- RULE-BB-004/INV-07 → CKG-006/012. RULE-CAU-01/02/03 → CKG-008. CEE-001 l.111 → ADV-05. atomic-spec §10.2 → EC-CKG-001/002/003/005 em E3.
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (MODIFIED = RULE-BB-004 reforçada; o antigo M-01 sobre CEM-001 l.494 foi RETIRADO por premissa falsa — A-03 — e a preservação "a partir da admissão" passou a regra LOCAL CKG-010, RULE-HD-02/03). **Eixo VERTICAL (RULE-HV) não aplicável.**

**Bloco C — epistêmico / disciplinas N8–N17 (verificado — sem achado residual):**
- **RULE-EPI-01..03:** H-001/mecanismo físico = INDETERMINADO (não fato); nenhuma hipótese tratada como fato.
- **RULE-SEM-01/04:** acepções declaradas (CC-10); termos canônicos não redefinidos.
- **RULE-ONT-01/02:** ontologia declarada (§D2.1); `school`/`hierarchy_role` derivados do produtor **só para hypothesis** (N-01; structure/Fractal sem fonte segura = CKG-STRUCT-ORIGIN-001 [DECISÃO NECESSÁRIA]); `ontological_status` {observational, theoretical} (RULE-ONT-01, l.671); alteração por governança (RULE-ONT-02/CKG-009).
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
RULE-CKG/contrato; **H-001**; selo SPEC-007; allowlist/host do juízo; migração de ontologia; **CKG-STRUCT-ORIGIN-001**
(origem/escola de `structure`; `school=Fractal` — N-01/N-09, BL-035); **timeout `PENDING_ANCESTOR`** (N-07)) marcadas
[PROPOSTA]/[DECISÃO NECESSÁRIA]; M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 abertas, não tocadas.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001; CHM-001; CCM-001; CEE-001; SAS-001; SPEC-004 v1.2; SPEC-005 v1.0; SPEC-001/019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5; RULES v1.5 (RULE-BB-004, RULE-CAU, RULE-ONT, RULE-MECH, RULE-HD); INV-*; ENF-*; CONSTITUTION l.233 | [FONTE] | FATO NORMATIVO |
| RULE-CKG-001..013; INV-CKG-01/02; matriz §D2.1/§D2.2; contrato de nó/relação; BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | Requer homologação |
| Extensão da fronteira SAS-001 §6.12 a produtores não-estruturais; governança da ontologia análoga a RULE-HG; consumo de evento pelo KG | [INFERÊNCIA] | Derivado; a confirmar |
| Origem/escola de `structure` e elo `structure→hypothesis`; `school=Fractal` sem produtor (N-09) | [DECISÃO NECESSÁRIA] | **CKG-STRUCT-ORIGIN-001 — ABERTA** (dona: Andraus; BL-035); N-01 opção (a) |
| Fontes SRC-ZEP-01/PROV-01/MEMVSKG-01; REPO-graphiti/graphrag/cognee/mem0 | [EXTERNO] | DADO, nunca baseline |
| SRC-FORGET-01 (sumário WebSearch) | [EXTERNO] | DADO **não-verbatim** — não sustenta sozinha alegação carregada |
| Mecanismo físico de armazenamento | [DECISÃO NECESSÁRIA] | **H-001 — EM ABERTO — não fechar** (Andraus) |
| Banco de grafos dedicado (Opção B) | [DECISÃO NECESSÁRIA] | **ADIADO** — registrado, não apagado (INV-07) |
| Escala numérica de confiança de relação | [DECISÃO NECESSÁRIA] | PARÂMETRO a calibrar — INDETERMINADO (não toca J-001/N-001) |
| Limite/timeout da espera `PENDING_ANCESTOR` (buffer de admissão — N-07) | [DECISÃO NECESSÁRIA] | BOUNDED; valor = runtime/K-001; esgotado ⇒ fail-closed |
| Contrato do selo de publicação | [DECISÃO NECESSÁRIA] | Dependência da **SPEC-007** |
| Allowlist de escritores / host do juízo CKG-008 / migração de ontologia | [DECISÃO NECESSÁRIA] | Runtime/governança (K-001/SPEC-018; SPEC-019 spec-time) |
| Emissão de evento pelo KG / consumidor-contrato de consumo | [DECISÃO NECESSÁRIA] | Dependente da SPEC-005 — não afirmada |
| Componente "Cognitive Ontology" separado | [DECISÃO NECESSÁRIA] | Ontologia DENTRO da SPEC-006 (Q-ABERTURA-4); é de Andraus |
| Admissão / histórico de estados de `conviction` no KG | [DECISÃO NECESSÁRIA] | **NEGADA POR PADRÃO — decisão de Andraus no chat (2026-10-17), SEM ata ainda: a ata de homologação da errata deve registrá-la (AGENTS.md §10); a classificação "Minor/aditiva" é decisão de Andraus [n-c]** (`CONVICTION_HISTORY_UNDEFINED`, N-07): o CCM-001 (l.58/78) define só o enum `status`, sem histórico de transições, e o Cap.5 (l.117) deixa M-001 ABERTA; pré-requisito para admitir = histórico de status da conviction no CCM-001/SPEC-003 **E** M-001 — **ABERTAS e de Andraus**; esta Spec não as fecha nem atribui ao CCM-001 histórico que ele não define |
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
[x] Profundidade D0–D7 (+ D8 focado); §D2.1 (matriz) + §D2.2 (colisão); §D3.1 (vocabulário); D4; D5 (estado derivado); D6; D7 x19; D8 x23; D9 por referência.
[x] Enforcement Contract em todo ato com efeito (EC-CKG-001..006); escrita = E3; E1 consulta; guard confiança×convicção = E3; ENF-07 amostral nos E3 (CONDICIONAL até limiar).
[x] Status epistemológico aplicado (FATO NORMATIVO / PROPOSTA / INFERÊNCIA / EXTERNO / DECISÃO NECESSÁRIA).
[x] CONS-01: H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 e a nova CKG-STRUCT-ORIGIN-001 (N-01/N-09; BL-035) + o timeout `PENDING_ANCESTOR` (N-07) permanecem ABERTAS; nenhuma usada como invariante fechado; STRUCT-10 respeitado.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] CONSOLIDAÇÃO (Rodada 6, preservada): cada regra definida UMA vez (RULE-CKG/BASpec); EARS/D4/D6/EC/T/ADV/Herança referenciam por ID; narrativa histórica só no changelog (1 linha/versão, ordenado 1.0→1.11).
[x] Integridade: nenhuma fonte inventada; âncoras canônicas RE-VERIFICADAS na errata v1.8 (A-06..A-09) e v1.9 (N-01: CEM-001 l.258-262 estado de validação da Evidência = ACTIVE; CCM-001 l.58/78 = COMPUTED/GATED_PASS; N-06: BASpec-CBP-007 l.543-565): CEM-001 l.258-262/l.473-475/l.602/l.606/l.608-615 e l.489-497 (tabela Consumo — l.494 é estados da EVIDÊNCIA, não obrigação sobre hipótese — A-03); CHM-001 §4.3 l.744-748/l.379 (A-02); CCM-001 l.58/78; CONSTITUTION l.191/192 (A-09); SPEC-001 l.97/100/104/108/515-520/524; SPEC-004 CBP-004 l.239-246/CBP-007 l.264-270 (DEFINIÇÃO; BASpec em l.543-565 — A-06/N-06)/CBP-014 l.311-319; SPEC-005 l.971 (A-09); RULES ONT-01 l.671/ONT-02 l.672 (A-09); ABERTURA §10 R-8 (A-08); RMR-001 por ID/âncora BL-029 (nota DHR-SPEC006-PEND-001) `Em espera` — A-07.
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
  - **Nota A-05 (governança — achado da auditoria independente):** a SPEC-006 foi homologada (v1.7) com **H-001 ABERTA** (Opção A, correto), mas **H-001 ficou SEM DONO** após a homologação — ROADMAP §6, atomic-spec §12 e revisor.md §8 ainda atribuem H-001 à SPEC-006 (já homologada). O **re-apontamento da dona de H-001** (ex.: BL com gatilho de BUILD/Spec futura, e atualização de ROADMAP §6 / atomic-spec §12 / revisor.md §8) é **decisão exclusiva de Andraus** — esta errata **NÃO escolhe a dona** nem edita aqueles documentos (CONS-01; AGENTS §10). Apenas REGISTRA o achado.
- **Opção B (banco de grafos)** — ADIADA (registrada, não apagada — INV-07).
- **Escala de confiança de relação** — PARÂMETRO a calibrar (INDETERMINADO; não toca J-001/N-001).
- **Limite/timeout da espera em `PENDING_ANCESTOR`** (buffer de admissão, INV-CKG-02/N-07) — BOUNDED, mas o valor é [DECISÃO NECESSÁRIA] (runtime/K-001; sem número arbitrário — RULE-MET-01); esgotado ⇒ fail-closed `DERIVA_DE_EDGE_MISSING`.
- **Contrato do selo de publicação** — dependência da **SPEC-007**; [DECISÃO NECESSÁRIA].
- **Allowlist de escritores / host do juízo CKG-008 / migração de ontologia** — runtime/governança (K-001/SPEC-018; SPEC-019); [DECISÃO NECESSÁRIA].
- **Emissão/consumo de evento pelo KG** — dependente da SPEC-005; [DECISÃO NECESSÁRIA] (não afirmada).
- **Produtor/gatilho de promoção trabalho→permanente** — [DECISÃO NECESSÁRIA] (SPEC-018/K-001; distinto do critério de estado, que é verificável).
- **CKG-STRUCT-ORIGIN-001 — origem/escola de `structure` e elo `structure→hypothesis`** — [DECISÃO NECESSÁRIA] (dona: Andraus; gatilho: quando houver mapeamento seguro produtor→escola para `structure`). N-01 (opção (a), decisão de Andraus 2026-10-12): `school`/`hierarchy_role` valem SÓ para `hypothesis`; `structure` NÃO deriva `school` e NÃO é origem de ORIGINA nesta versão; SAS-001 §6.12 NÃO é fonte de `school`. **Fractal (N-09)** entra na mesma decisão: sem produtor de hipótese `Fractal` em SPEC-001, `school=Fractal` não tem fonte e não é inventado. Registrado também em **BL-035** (RMR-001, `Em espera`).
- **Componente "Cognitive Ontology" separado** — não criado; ontologia DENTRO da SPEC-006; é de Andraus.
- **M-001 / J-001 / N-001 / G-001 / K-001 / C-001 / WF-D03 / ECC-03-001** — permanecem ABERTAS; não tocadas.

**Volume (F-17 — registrado, NÃO dividido):** CRITICAL, 13 BASpecs/19 cenários/23 ADV + §D2.1/§D2.2 + §D3.1 + schema. A
decisão de DIVIDIR a Spec é **exclusivamente de Andraus (Q-ABERTURA-5)** — o Especificador não divide; slot preservado (INV-07).

