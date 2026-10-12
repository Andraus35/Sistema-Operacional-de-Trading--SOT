# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.2 (candidato)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico de armazenamento INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-12 (Rodada 3)

> **Nota de honestidade (RULE-MET-01):** vários itens permanecem **em aberto**, marcados [DECISÃO NECESSÁRIA] no plan.md e **não** marcados ✔ aqui: mecanismo físico (H-001); contrato do selo de publicação (SPEC-007); **critério/evento de admissão do caminho (a) e produtor** (SPEC-018/K-001); allowlist de escritores; host do juízo de CKG-008; migração de ontologia; consumo/emissão de evento pelo KG (SPEC-005 não define "Evidence Invalidated"); escala numérica de confiança de relação. A verificação confere **well-formedness estrutural**, não a resolução dessas decisões.

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — alvo ROADMAP §6; CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; memória permanente ≠ trabalho; mecanismo físico INDETERMINADO; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals (inclui `ontological_status`, permanente×temporário diferido, emissão pelo KG) |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA]; **matriz §D2.1** (com `school`/`origin_agent`, "família" intra-escola, CONFIRMA/REFUTA só evidence, CAUSA restrita); INV-CKG-01/02 |
| D3 Comportamento (BASpec) | Sim | ✔ | CKG-001..013, cada uma com CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | Integridade, bitemporal (valid-time + transaction-time; invalidação=ato autorizado/novo registro), imutabilidade/estado derivado, trace completo (INV-CKG-02), dedupe (natural_key), gate causal, namespace de confiança |
| D5 Estado | Sim | ✔ | `knowledge_state` = **projeção derivada**; HOMÔNIMO mas ≠ estado canônico (`canonical_status` à parte); transitórios não persistidos |
| D6 Protocolo | Sim | ✔ | Sequência (10 passos; duas fontes/uma governança); invalidação = ato autorizado (não cascata); consumo/emissão de evento = [DECISÃO NECESSÁRIA] |
| D7 Teste | Sim (CRITICAL; ≥3) | ✔ | **T01..T14 (14)** — um por BASpec + T14 negativo de proveniência (CKG-005) + caso-feliz T12 |
| D8 Adversarial | Sim (CRITICAL, focado) | ✔ | **ADV-CKG-01..16 (16)** — cobre as 13 BASpecs (incl. ADV-16 trace/DERIVA_DE por ancestral) + fronteiras/decisões abertas |
| D9 Auditoria | Por referência | Parcial (por referência) | registro reconstruível (record_kind/version/supersedes/proveniência/validade/canonical_status); trace **completo** (CKG-011/INV-CKG-02); observabilidade agregada = SPEC-040 |

**Resultado:** profundidade-alvo D0–D7 atingida; D8 focado. D9 por referência (coerente com alvo e H-001 ABERTA).

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REF | VERIF. | CLASSE | Bounded loop / Gate saída |
|---|---|---|---|---|---|---|---|
| CKG-001 ontologia + matriz | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-002 ref canônica + canonical_status (obs≠evid) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-003 relação tipada/proveniência/DERIVA_DE por ancestral | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-004 temporalidade (ato autorizado; novo registro) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-005 proveniência obrigatória | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-006 imutabilidade/append-only (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-007 confiança em namespace próprio (≠ convicção) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-008 causal (mecanismo+regime+posthoc) | ✔ | ✔ | ✔ | ✔ | ✔ | H | bounded loop ✔ + gate de saída ✔ |
| CKG-009 governança de escrita (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-010 fronteira (canônico/ciclo de vida + selo SPEC-007) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-011 consulta/trace completo (read-only) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-012 lifecycle (estado derivado) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-013 colisão de relações | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |

Cada BASpec com efeito declara Classe + critério 4Es (RULE-MECH-02); Classes C declaram gate de saída; Classe H (CKG-008) declara bounded loop + gate de saída (verifica presença de CAU-01/02/03, não veracidade — ENF-03). **PASS.**

---

## 3. Critérios EARS

13 critérios "Quando <condição>, o KG DEVE/NÃO DEVE <resposta>". EARS 7 reformulado (confiança em namespace próprio; requisito à SPEC-003 endereçado, não imposto). Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 cobrem as 13 BASpecs e toda RULE-CKG: write (001: RULE-CKG-001/002/003/005/008/010/013); imutabilidade/versionamento (002: RULE-CKG-004/006/012); governança (003: RULE-CKG-009); confiança namespace (004: RULE-CKG-007); causal (005: RULE-CKG-008); consulta (006: RULE-CKG-011) |
| ENF-02 Nível ≥ piso | ✔ **escrita permanente = E3** (atomic-spec §10.2) em EC-001/002/003/005; E2 (guard confiança, 004); E1 (consulta, 006) |
| ENF-03 Gate determinístico; Detector ≠ Gate | ✔ EC-003/005; juízo de CKG-008 é detector, gate determinístico |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-001/002/003/005 (E3 fail-closed) |
| ENF-05 Policies não auto-aprendidas | ✔ [PROPOSTA]; só Andraus homologa |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-001/002/003/**005** (amostral; CONDICIONAL até limiar — gap aberto). *(Correção R3 item 15: EC-005 agora cita a amostragem no EVIDENCE.)* |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12 — atomic-spec v1.5)

Preenchido no plan.md. **Críticos aplicáveis:** CC-02 (canônicos/SPEC-004/005 não redefinidos; `gate_record` reatribuído à SPEC-004; `lineage` é campo LOCAL que referencia `Lineage`/`derived_from[]`), CC-08 (Herança/Delta; append-only por novos registros; INV-CKG-02), CC-09 (H-001 INDETERMINADO; causal c/ mecanismo+regime+posthoc; completude do trace não rebaixada), CC-10 (acepções; **estados do KG ≠ estados canônicos**; observation≠evidence), CC-11 (Classe por BASpec, incl. H) = PASS. CC-01 (agnóstico de escola; o KG só **espelha** a autoridade de criação — Elliott PRIMARY, ICT não origina/INV-02). CC-03 (não computa convicção). CC-04 (**INV-04 = só custo**; proibição de confiança = regra local [PROPOSTA]; matriz restringe CAUSA custo/confiança→conviction). CC-05 (CRITICAL/D0–D7+D8). CC-06/CC-07 = N/A justificado. **CC-12 = N/A**. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED com ID+versão/linha (RULE-HD-04): CEM-001 (l.264/428/494/503/602/608-615/562-565/699 — campo `Lineage`, Status único mutável, não-cascata), CHM-001 (`parent_hypothesis_id` l.165/415; l.672-676), CCM-001, CEE-001 l.111, SAS-001 §6.12, SPEC-001 (`parent_id`, RULE-HH-003 l.104), SPEC-004 v1.2 (INV-CBP-01; `derived_from[]`/`gate_record`), SPEC-005 v1.0, CONSTITUTION l.191/193/233, RULE-BB-004, **RULE-CAU-01/02/03 (l.680-682)**, **RULE-ONT-01/02 (l.671)**, atomic-spec v1.5 (§10.2 E3), INV-04/05/06/07/09/10, ENF-01..08. ✔
- **Mapa de cobertura × lacuna** presente (arquivo:linha). ✔
- REMOVED vazio; MODIFIED = só RULE-BB-004 reforçada (RULE-HD-02). ✔
- **Atribuições corrigidas (R3):** `gate_record`/`derived_from[]` = SPEC-004 (não CEM-001); `lineage` = campo local [PROPOSTA] (não há `lineage_ref` no CEM-001); `parent_id` (SPEC-001) / `parent_hypothesis_id` (CHM-001) citados corretamente; RULE-010 removida (era de convicção — só P13). ✔
- Eixo VERTICAL (RULE-HV) avaliado e **não aplicável**. ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001 NÃO decidida — contrato cognitivo independe do mecanismo físico (ADV-CKG-09) | ✔ |
| Opção B (banco de grafos) = ADIADA (registrada; INV-07) | ✔ |
| Confiança de relação em namespace próprio; INV-04 = **só custo**; proibição de confiança = regra local [PROPOSTA] (CKG-007) | ✔ |
| Matriz restringe CAUSA custo/confiança→`conviction`; CONFIRMA/REFUTA só `evidence` (INV-06; CONSTITUTION l.191) | ✔ |
| Invalidação = ato AUTORIZADO (CKG-009), NÃO cascata automática (CEM-001 l.602; CHM-001 l.672-676) | ✔ |
| Consumo/emissão de evento pelo KG = [INFERÊNCIA]/[DECISÃO NECESSÁRIA] (SPEC-005 não define "Evidence Invalidated") — **não** ✔ fechado | aberto (declarado) |
| Critério/evento de admissão do caminho (a) + produtor = [DECISÃO NECESSÁRIA] (SPEC-018/K-001) — **não** ✔ fechado | aberto (declarado) |
| Contrato do selo de publicação = [DECISÃO NECESSÁRIA] (SPEC-007); allowlist/host do juízo/migração de ontologia = [DECISÃO NECESSÁRIA] | aberto (declarado) |
| Preservação de estado canônico por `canonical_status` + `canonical_state_transition` (CEM-001 l.264/428/494); estados do KG ≠ canônicos | ✔ |
| Trace completo garantido por INV-CKG-02 (aresta DERIVA_DE por ancestral; acíclico; ignora validade) | ✔ |
| Append-only = **novos registros** (`record_kind`); estado = projeção derivada (SPEC-004 INV-CBP-01) | ✔ |
| M-001 / J-001 / N-001 / G-001 / K-001 / C-001 / WF-D03 / ECC-03-001 NÃO tocadas — permanecem ABERTAS | ✔ |
| SPEC-004/005 NÃO reabertas; SPEC-007 (formação) NÃO absorvida | ✔ |
| Nenhuma forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta (STRUCT-10) | ✔ |
| SRC-FORGET-01 = DADO não-verbatim, não sustenta alegação carregada | ✔ |

**PASS (com itens explicitamente em aberto, não marcados ✔).**

---

## 8. Verificação de RULEs/IDs/campos citados (existência real — conferência mecânica R3)

| Citado | Existe? | Fonte verificada |
|---|---|---|
| CHM-001 `parent_hypothesis_id` | ✔ | canon/CHM-001 l.165/415 |
| SPEC-001 `parent_id`; RULE-HH-003 | ✔ | specs/features/SPEC-001/plan.md l.58/l.104 |
| CEM-001 campo `Lineage` (NÃO `lineage_ref`) | ✔ | canon/CEM-001 l.351/359/426/539-554 |
| SPEC-004 `derived_from[]`; `gate_record`/`computed_by` | ✔ | specs/features/SPEC-004/plan.md l.176/217/266/543 |
| CEM-001 "Status é o único campo mutável"; transição registra timestamp/origem/justificativa | ✔ | canon/CEM-001 l.264/428 |
| CEM-001 "invalidação não implica remoção/cascata"; impacto é de CHM/CCM/CDM; Fusion inicia | ✔ | canon/CEM-001 l.602/503/606 |
| CHM-001 "REFUTED/SUPERSEDED não refuta/substitui automaticamente" | ✔ | canon/CHM-001 l.672-676 |
| INV-04 = **só custo** no Conviction Vector | ✔ | atomic-spec l.404; AGENTS §6.8 |
| CONSTITUTION Observations=dados brutos (l.191); Hypotheses PRIMARY/SUB via parent_id (l.193); EC-COG-003 (l.233) | ✔ | governance/CONSTITUTION.md l.191/193/233 |
| RULE-CAU-01 (l.680), RULE-CAU-02 (regime, l.681), RULE-CAU-03 (pós-hoc, l.682) | ✔ | governance/RULES.md |
| RULE-ONT-01 (observacional × teórica, order block/liquidez), RULE-ONT-02 (l.671-672) | ✔ | governance/RULES.md l.671-672 |
| RULE-010 = alteração de convicção rastreável (NÃO P13) → removida do D9 | ✔ | governance/RULES.md l.54 |
| SPEC-019 não cita "ontologia" (0 ocorrências) → marcado [INFERÊNCIA] | ✔ | specs/features/SPEC-019 (grep 0) |
| atomic-spec §10.2 "KG publicado → E3 mínimo" | ✔ | atomic-spec.md §10.2 |
| RMR-001 BL-029 `Em espera` — l.128 (linha) + l.192 (DHR-SPEC006-PEND-001); l.191 = errata BL-003 | ✔ | backlog/RMR-001 l.128/l.191/l.192 |
| RULE-CKG-001..013; INV-CKG-01/02; matriz §D2.1; DERIVA_DE; `canonical_status`/`canonical_state_transition`/`record_kind`/`natural_key`/`ontological_status`/`relevance`/`target_relation_id` | [PROPOSTA] | esta Spec — campos locais, não citados como de baseline |

Nenhuma referência a RULE/campo inexistente apresentada como de baseline. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- Nenhum gatilho `spec:SPEC-006` homologado isoladamente; satisfaz ramos de BL-003/BL-011 (`spec:SPEC-006`) e possivelmente BL-010 (`milestone:FASE 3`). ✔
- BL-003 (persistência física) — parte física = H-001/G-001 (ABERTAS) → referenciado, não absorvido. ✔
- BL-011 (MC-EXP-001) — insumo de requisitos; não promovido. ✔
- BL-010 (MC-RAG-001) — fonte da SPEC-007; tangente; não promovido. ✔
- **BL-029 = `Em espera`** (Andraus, DHR-SPEC006-PEND-001; RMR-001 l.128 + l.192; `ATIVADO` riscado), gatilho `spec:SPEC-014`/`SPEC-018`/`SPEC-045`. Independente; não promovido. **[citação corrigida R3 item 12: l.128/l.192, não l.191].** ✔
- Passo 11-bis pleno na homologação. **PASS.**

---

## 10. RULE-ECC-04 (Captura Verbatim) e RULE-ECC-06 (Repositórios) — verificação de presença

| Fonte carregada | Arquivo companheiro | Citação verbatim no Dossiê |
|---|---|---|
| SRC-ZEP-01 / SRC-PROV-01 / SRC-MEMVSKG-01 | ✔ sources/ | ✔ research.md §3 |
| SRC-FORGET-01 | N/A (WebSearch — **DADO não-verbatim**) | research.md §3.5/§3.6 (não sustenta alegação carregada) |
| REPO-graphiti / graphrag / cognee / mem0 | ✔ sources/REPO-*.txt | ✔ research.md §5 (régua Equilibrada; 4 elegíveis) |

- **RULE-ECC-06:** 4 elegíveis; nenhum adotado; SPEC-006 não é grandfathered → STRUCT-12 incide; `check_repo_research.py` esperado OK (sem web). ✔
- **RULE-ECC-05:** NÃO incide (infra de memória); conformidade WORKFLOW por prudência; não fecha WF-D03. ✔
- **Nota de honestidade:** metadados de repositório via WebFetch da API pública (research.md §5/§8), não reproduzíveis sem rede (ENF-03). Risco residual em `sources/_LIMITACAO-WEB.txt`.

> Correspondência verbatim e régua = mandato do Revisor/gate. Aqui só **presença**. **PASS (presença).**

---

## 11. Rastreabilidade dos achados da Rodada 3 (autocontida — 18 itens + Extra)

| Item R3 | Situação |
|---|---|
| 1 [CRÍTICA] Matriz HERDA/ORIGINA/escola | **Resolvido** — HERDA sub→pai por `parent_id`/`parent_hypothesis_id`, inclusive entre escolas; "família" só intra-escola; ORIGINA ∈ {Elliott,SMC,Fibonacci}, nunca ICT; atributo `school`/`origin_agent`; KG só espelha (CC-01); T01/ADV-12 reescritos (ICT-ORIGINA como violação; HERDA cross-escola como caso válido) |
| 2 [MAIOR] `lineage_ref` inexistente | **Resolvido** — renomeado `provenance_ref.lineage` [PROPOSTA] = ref. a `Lineage` (CEM-001)/`derived_from[]` (SPEC-004); corrigido em CKG-005/RULE-CKG-005/schema/D9/INHERITS |
| 3 [MAIOR] preservar todos os estados canônicos | **Resolvido** — `canonical_status` (snapshot) + registro `canonical_state_transition` (estado/timestamp/origem/justificativa — CEM-001 l.428); estados do KG ≠ canônicos (CC-10); CKG-002/010, T09 |
| 4 [MAIOR] critério de admissão Blackboard×KG | **[DECISÃO NECESSÁRIA]** declarado (promoção trabalho→permanente = SPEC-018/K-001; produtor do caminho (a) aberto) — bloco após CKG-010 |
| 5 [MAIOR] trace completo não garantido | **Resolvido** — INV-CKG-02 (aresta DERIVA_DE por ancestral do Lineage, fail-closed; acíclico; ignora validade); CKG-003/011; ADV-16 |
| 6 [MAIOR] INV-04 | **Resolvido** — INV-04 = só custo; confiança = regra local [PROPOSTA]; matriz restringe CAUSA custo/confiança→conviction; CKG-007 reformulado (namespace; requisito à SPEC-003 endereçado); EC-CKG-004/T06 |
| 7 [MAIOR] cascata de invalidação | **Resolvido** — invalidação = ato autorizado (CKG-009), não cascata (CEM-001 l.602; CHM-001 l.672-676); exemplo de CKG-004 trocado; consumo de evento [INFERÊNCIA]/[DECISÃO NECESSÁRIA] (SPEC-005 não define "Evidence Invalidated") |
| 8 [MÉDIA] schema incompleto | **Resolvido** — `record_kind`, `relevance`, `target_relation_id`, `natural_key` (nós não-canônicos), `collision_record` como registro, validade/arquivamento para nó e relação |
| 9 [MÉDIA] permanente/temporário | **Resolvido/diferido** — S14: temporário = janela de validade/relevância rebaixada; critério de promoção = SPEC-018/K-001 [DECISÃO NECESSÁRIA] |
| 10 [MÉDIA] observation CONFIRMA/REFUTA | **Resolvido** — CONFIRMA/REFUTA restritas a `evidence` (INV-06; CONSTITUTION l.191) |
| 11 [MÉDIA] bitemporal | **Resolvido** — duas dimensões: valid-time (`valid_from`/`valid_to`) + transaction-time (`recorded_at`, consulta "conforme registrado em R"); D4/CKG-004 |
| 12 [MÉDIA] citação RMR-001 | **Resolvido** — l.128 (BL-029) + l.192 (DHR-SPEC006-PEND-001); l.191 = errata BL-003 |
| 13 [MENOR] checks §11 contagem/pointers | **Resolvido** — esta seção é autocontida (18 itens + Extra); sem "ver relatório"/"§C22"/"achado C1" |
| 14 [MENOR] T04-neg/ADV CKG-003 | **Resolvido** — T14 (negativo de proveniência CKG-005); ADV-16 (CKG-003/DERIVA_DE por ancestral); Bloco A corrigido |
| 15 [MENOR] EC-CKG-005 falso-DENY | **Resolvido** — EVIDENCE cita amostragem de falso-DENY (ENF-07) |
| 16 [MENOR] RULE-010 × P13 | **Resolvido** — D9 cita só P13 (RULE-010 é de convicção, l.54) |
| 17 [MENOR] SPEC-019/ontologia | **Resolvido** — marcado [INFERÊNCIA] (SPEC-019 não cita "ontologia"); runtime = K-001 [DECISÃO NECESSÁRIA] |
| 18 [MENOR] RULE-ONT ontological_status | **Resolvido** — atributo `ontological_status` {observational, theoretical} em structure/regime/narrative (RULES.md l.671); Bloco C atualizado |
| Extra | **Resolvido** — `gate_record` reatribuído à SPEC-004 (não CEM-001) em toda a Spec |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (CKG-001..013) com Classe (CC-11; D+C+H), EARS (13), Enforcement (EC-CKG-001..006; **escrita = E3**; ENF-07 em todos os E3 incl. EC-005), Constitution Check CC-01..CC-12, Herança/Delta (CC-08; atribuições corrigidas), matriz §D2.1 (escola/família/CONFIRMA-REFUTA/CAUSA), INV-CKG-01/02, bitemporalidade real, append-only por novos registros, preservação de estado canônico, 14 cenários (T01..T14), 16 adversariais (ADV-CKG-01..16), CONS-01 (decisões abertas intactas), gate RMR-001 (BL-029 `Em espera`, l.128/l.192), RULE-ECC-04/06 satisfeitos. Rastreabilidade autocontida dos 18 achados da Rodada 3 (+Extra) em §11.

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: gate determinístico `validate_spec_sot.py` + `check_repo_research.py` + `build_map.py --check` + `check_doc_sync.py` (ambiente pai — Especificador sem Bash) + submissão ao Revisor SOT.
