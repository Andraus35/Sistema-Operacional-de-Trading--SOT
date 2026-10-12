# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.4 (candidato)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico de armazenamento INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-12 (Rodada 5)

> **Nota de método (Rodada 5):** cada item marcado "Resolvido" abaixo foi conferido ponta-a-ponta por busca cruzada (grep dos termos/IDs alterados) no plan.md **e** neste checks.md, para eliminar resíduo contraditório (F-12). Os 9 Maiores e 8 Menores do parecer NÃO CONFORME foram corrigidos por F-xx (ver §11).
> **Itens em aberto (não marcados ✔):** mecanismo físico (H-001); selo de publicação (SPEC-007); **produtor/gatilho de promoção** trabalho→permanente do caminho (a) (o CRITÉRIO DE ESTADO é agora gate verificável [PROPOSTA]; o gatilho/produtor segue [DECISÃO NECESSÁRIA]); consumidor/contrato de consumo de evento pelo KG; emissão pelo KG; allowlist de escritores; host do juízo CKG-008; migração de ontologia; escala de confiança.

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — alvo ROADMAP §6; CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; memória permanente ≠ trabalho; mecanismo físico INDETERMINADO) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA]; **matriz §D2.1** (`school`/`hierarchy_role` DERIVADOS do produtor, CONFIRMA/REFUTA só evidence, CAUSA destino≠conviction) + **tabela de colisão §D2.2** (escopo por par; INVALIDA; não-SUPERSEDED); **§D3.1** vocabulário de rejected_reason; INV-CKG-01/02 |
| D3 Comportamento (BASpec) | Sim | ✔ | CKG-001..013 com CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | integridade+regra de nó (school derivado), bitemporal (rejeita valid_to<valid_from), imutabilidade/estado derivado+precedência, trace completo por tipo (INV-CKG-02; aciclicidade), dedupe/ordem de versão (expected_version, sem fork), gate causal (posthoc determinístico), namespace confiança (sem aresta→conviction), **detecção de colisão §D2.2** |
| D5 Estado | Sim | ✔ | `knowledge_state` = projeção derivada (com precedência); ≠ estado canônico; transitórios (CANDIDATE_WRITE/REJECTED/PENDING_ANCESTOR em buffer, não persistidos) |
| D6 Protocolo | Sim | ✔ | Sequência; admissão por estado admissível do tipo; capacidade×papel [PROPOSTA]; invalidação = ato autorizado (não cascata); consumo/emissão de evento = [INFERÊNCIA]/[DECISÃO NECESSÁRIA] |
| D7 Teste | Sim (CRITICAL; ≥3) | ✔ | **T01..T16 (16)** — T01 (ORIGINA school=ICT derivado), T12 (proveniência condicional), T14 (sem computed_by), T15 (HERDA cross-escola), **T16 (posthoc determinístico)** |
| D8 Adversarial | Sim (CRITICAL, focado) | ✔ | **ADV-CKG-01..21 (21)** — inclui ADV-17 (hypothesis.school=ICT), ADV-18 (escopo colisão: INVALIDA/SUPERSEDED), **ADV-19 (fork)**, **ADV-20 (ciclo)**, **ADV-21 (admissão)** |
| D9 Auditoria | Por referência | Parcial | registro reconstruível (proveniência condicional; expected_version; targets_record_id); trace completo (INV-CKG-02); observabilidade agregada = SPEC-040 |

**Resultado:** profundidade-alvo D0–D7 atingida; D8 focado. **PASS.**

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REF | VERIF. | CLASSE | Gate/bounded |
|---|---|---|---|---|---|---|---|
| CKG-001 ontologia + matriz + regra de nó (school≠ICT; HERDA pai=PRIMARY) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-002 ref canônica + canonical_status (obs≠evid) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-003 relação tipada/proveniência/DERIVA_DE por ancestral | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-004 temporalidade (ato autorizado; novo registro; bitemporal) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-005 proveniência CONDICIONAL (computed_by sempre; gate_record/lineage condicionais) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-006 imutabilidade/append-only (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-007 confiança namespace próprio (≠ convicção) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-008 causal (mecanismo+regime+posthoc) | ✔ | ✔ | ✔ | ✔ | ✔ | H | bounded ✔ + gate ✔ |
| CKG-009 governança de escrita (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-010 fronteira (a=estado admissível por TIPO canônico [PROPOSTA]; b=selo SPEC-007 verificável; promoção trabalho→permanente = [DECISÃO NECESSÁRIA]) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate (a) ✔ por tipo / gate (b) ✔ |
| CKG-011 consulta/trace completo (read-only) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-012 lifecycle (estado derivado) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-013 colisão (tabela §D2.2; escopo por par incl. INVALIDA via target_relation_id; exclui SUPERSEDED; collision_record com identidade) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |

**PASS.**

---

## 3. Critérios EARS

13 critérios "Quando <condição>, o KG DEVE/NÃO DEVE <resposta>". EARS 7 (confiança namespace próprio) e a proveniência condicional (EARS 5/9) coerentes com CKG-005/007. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 cobrem as 13 BASpecs e toda RULE-CKG |
| ENF-02 Nível ≥ piso | ✔ escrita permanente e guard de confiança×convicção = E3 (001/002/003/004/005); consulta = E1 (006) |
| ENF-03 Detector ≠ Gate | ✔ EC-003/005; juízo CKG-008 detector, gate determinístico |
| ENF-04 Fail-closed | ✔ EC-001/002/003/005 |
| ENF-05 Policies não auto-aprendidas | ✔ [PROPOSTA] |
| ENF-06 E0 | N/A |
| ENF-07 E3 falso-DENY | ✔ EC-001/002/003/005 (amostral; CONDICIONAL até limiar) |
| ENF-08 Escala E0–E3 | ✔ atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12)

CC-02 (não redefine; `lineage` local referencia `Lineage`/`derived_from[]`; `gate_record`/`computed_by` = SPEC-004), CC-08 (Herança; append-only; **proveniência condicional espelha CBP-007**), CC-09 (H-001 INDETERMINADO; causal c/ mecanismo+regime+posthoc), CC-10 (acepções; estados do KG ≠ canônicos; observation≠evidence), CC-11 (Classe por BASpec, incl. H) = PASS. CC-01 (agnóstico; **hypothesis.school ≠ ICT** — INV-02/RULE-HH-004; HERDA cross-escola válido). CC-03/04 (INV-04 = só custo; confiança = regra local). CC-05/06/07/12 OK/N-A. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

INHERITS com ID+versão/linha verificados: **SPEC-004 RULE-CBP-007 (l.543-558 — proveniência CONDICIONAL: computed_by sempre; gate_record se gate; derived_from se derivado) + RULE-CBP-014 (identidade autenticada)**; CEM-001 (`Lineage` l.351/539-554; Status único mutável l.264/428; não-cascata l.602/503; `Evidence.Invalidated` canônico l.600/722; responsabilidades KG l.494/608-615); CHM-001 (`parent_hypothesis_id` l.165/415; l.672-676); SPEC-001 (`parent_id`, RULE-HH-003 l.104, RULE-HH-004); **SPEC-005 (transporta `Evidence.Invalidated` — l.88/l.859)**; CONSTITUTION l.191/193/233; RULE-BB-004, RULE-CAU-01/02/03 (l.680-682), RULE-ONT-01/02 (l.671); atomic-spec §10.2 E3; INV-04/05/06/07/09/10. REMOVED vazio; MODIFIED = só RULE-BB-004 reforçada. **PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001 NÃO decidida; Opção B ADIADA | ✔ |
| `school`/`hierarchy_role` DERIVADOS do `producer_id`/`producer_type` do canônico (não do payload); `origin_agent` eliminado; "família estrutural" REMOVIDA (F-13) | ✔ |
| Regra de nó `hypothesis.school ≠ ICT` (INV-02/RULE-HH-004) com teste (T01/ADV-17); HERDA pai=PRIMARY | ✔ |
| HERDA cross-escola VÁLIDO (T15 positivo); pai=PRIMARY | ✔ |
| Proveniência CONDICIONAL (computed_by sempre; gate_record/lineage condicionais; `[]` legítimo) — espelha CBP-007; não fabrica | ✔ |
| `Evidence.Invalidated` é canônico (CEM-001 l.600/722) e transportado pela SPEC-005 (l.88/859); falta consumidor = [DECISÃO NECESSÁRIA] | ✔ |
| Colisão: tabela §D2.2; escopo por par (CONFIRMA×REFUTA: mesmos from/to; INVALIDA: `target_relation_id==r2.relation_id`); só versões não-SUPERSEDED; teste ADV-18 cobre INVALIDA e SUPERSEDED | ✔ |
| CKG-010 caminho (a) = gate por estado admissível do tipo canônico (hypothesis {ACTIVE,DOMINANT,SUPERSEDED,REFUTED,ARCHIVED}; evidence {ACTIVE,SUPERSEDED,INVALIDATED,ARCHIVED}) [PROPOSTA], aplicado igual em S10/EARS-10/D6/EC-001/T09/BASpec; gatilho/produtor da promoção = [DECISÃO NECESSÁRIA] (Andraus) | ✔ (aberto declarado) |
| Versionamento: `supersedes`=última ∧ `version`=anterior+1 ∧ `expected_version`; sem fork (ADV-19); trace acíclico (ADV-20) | ✔ |
| `posthoc_flag` booleano obrigatório; regra determinística recorded_at>outcome_timestamp (T16, ADV-04) | ✔ |
| Nenhuma aresta `to_node==conviction` (direta/2 saltos/ESTATISTICA_DE); EC-CKG-004 em E3 | ✔ |
| Tabela capacidade×papel [PROPOSTA]; allowlist = [DECISÃO NECESSÁRIA]; SAS-001 §6.12 só como [INFERÊNCIA] fora do Structural Agent | ✔ |
| INV-04 leitura fiel (atomic-spec l.404: custo nunca entra; Convicção≠Score); confiança = regra local [PROPOSTA] | ✔ |
| Invalidação = ato autorizado (CKG-009), não cascata (CEM-001 l.602; CHM-001 l.672-676) | ✔ |
| M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 ABERTAS; SPEC-004/005 não reabertas; SPEC-007 não absorvida | ✔ |
| Nenhuma forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta (STRUCT-10) | ✔ (as 3 adjacências têm pendência em ≤200 chars) |

**PASS (com itens explicitamente em aberto, não marcados ✔).**

---

## 8. Verificação mecânica de citações (R4 — abri cada arquivo/linha)

| Citado | Existe / diz o afirmado? | Fonte verificada |
|---|---|---|
| SPEC-004 RULE-CBP-007: computed_by (sempre, identidade autenticada), gate_record (se gate), derived_from (se derivado) | ✔ CONDICIONAL confirmado | specs/features/SPEC-004/plan.md l.543-558 |
| SPEC-005 transporta `Evidence.Invalidated` | ✔ l.88 (eventos canônicos) + l.859 (`event_type`) | specs/features/SPEC-005/plan.md l.86-88/l.859 |
| CEM-001 `Evidence Invalidated` canônico | ✔ l.600 (evento) / l.722 (lista) | canon/CEM-001 l.600/717-727 |
| SPEC-005 l.115/242 = envelope (`source_ref`), NÃO o tipo do evento | ✔ (por isso a citação da v1.2 estava errada e foi removida) | specs/features/SPEC-005/plan.md |
| SPEC-001 `parent_id`/RULE-HH-003 (pai PRIMARY)/RULE-HH-004 (ICT não cria) | ✔ | specs/features/SPEC-001/plan.md l.100-108 |
| CHM-001 `parent_hypothesis_id`; "não refuta/substitui automaticamente" | ✔ | canon/CHM-001 l.165/415/672-676 |
| CONSTITUTION Hypotheses PRIMARY/SUB via parent_id (l.193); Observations dados brutos (l.191) | ✔ | governance/CONSTITUTION.md l.191/193 |
| RULE-CAU-01/02/03 (l.680-682); RULE-ONT-01 (l.671); RULE-010=convicção (l.54) | ✔ | governance/RULES.md |
| T01 (ORIGINA school=ICT derivado), T12 (PRIMARY lineage=[]), T14 (sem computed_by), T15 (HERDA cross-escola), T16 (posthoc determinístico) | ✔ existem | plan.md D7 |
| ADV-17 (school=ICT), ADV-18 (colisão INVALIDA/SUPERSEDED), ADV-19 (fork), ADV-20 (ciclo), ADV-21 (admissão) | ✔ existem | plan.md D8 |
| Contagem: 13 BASpecs / 6 EC / 13 EARS / 16 cenários / 21 ADV | ✔ conferido por grep de cabeçalhos (`### Cenário-CKG-T` e `### ADV-CKG-`) | plan.md |
| RULE-CKG-*; INV-CKG-01/02; §D2.1/§D2.2; `school`/`hierarchy_role`/`computed_by`/`record_kind` etc. | [PROPOSTA] | esta Spec — campos locais |

Nenhuma citação de baseline sem conferência. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- Nenhum gatilho `spec:SPEC-006` isolado; satisfaz ramos de BL-003/BL-011 (`spec:SPEC-006`); BL-010 tangente (SPEC-007). ✔
- **BL-029 = `Em espera`** (RMR-001 l.128 + l.192; l.191 = errata BL-003); independente; não promovido. ✔
- Passo 11-bis pleno na homologação. **PASS.**

---

## 10. RULE-ECC-04 / RULE-ECC-06 — presença

- SRC-ZEP-01/PROV-01/MEMVSKG-01 verbatim em sources/; SRC-FORGET-01 = DADO não-verbatim (não sustenta alegação carregada). ✔
- 4 repositórios elegíveis (régua Equilibrada); nenhum adotado; `check_repo_research.py` esperado OK (sem web). ✔
- RULE-ECC-05 NÃO incide (infra de memória); WORKFLOW por prudência; não fecha WF-D03. ✔
- **PASS (presença).**

---

## 11. Rastreabilidade dos achados do parecer NÃO CONFORME da v1.3 (F-01..F-17) — autocontida

Cada linha foi conferida por busca cruzada no plan.md v1.4 (changelog linha 1.4) e neste checks.md.

| Achado | Situação | Onde (plan.md) |
|---|---|---|
| F-01 Maior — D6 passo 5/D9 exigiam gate_record sempre | **Resolvido** — passo 5 e D9: `computed_by` ∧ [gate⇒gate_record] ∧ [derivado⇒lineage] | D6 passo 5; D9; CKG-005; T12 |
| F-02 Maior — fronteira (a) tratada como gate em 6 lugares / estados errados | **Resolvido** — critério por estado admissível do tipo canônico [PROPOSTA], aplicado uniformemente; promoção trabalho→permanente segue [DECISÃO NECESSÁRIA] | S10; RULE-CKG-010; EARS-10; D6; EC-CKG-001; T09; ADV-21 |
| F-03 Maior — colisão INVALIDA inalcançável; collision_record sem identidade; SUPERSEDED | **Resolvido** — escopo por par; só não-SUPERSEDED; collision_record com identidade/proveniência/E3 | §D2.2; D4; schema; ADV-18 |
| F-04 Maior — school/hierarchy_role/origin auto-declarados | **Resolvido** — derivados do producer_id/producer_type do canônico e do canal autenticado | §D2.1; schema; T01/T15; ADV-17 |
| F-05 Maior — schema sem valid_from/to, ref, proveniência da transição | **Resolvido** — `targets_record_id`, valid_from/valid_to no nó, campos de proveniência na transição | schema node_record/canonical_state_transition_record |
| F-06 Maior — guard INV-04 contornável; EC-004 em E2 | **Resolvido** — nenhuma aresta `to_node==conviction`; ENTÃO cobre escrita e consulta; EC-CKG-004 = E3; T06 com 2 saltos | §D2.1; CKG-007; EC-CKG-004; T06 |
| F-07 Maior — RULE-CAU-03 não verificável | **Resolvido** — `posthoc_flag` booleano obrigatório + regra determinística; SIMILAR_A com `similarity_basis`+gate; ADV-04 fechado | CKG-008; T07/T16; schema |
| F-08 Maior — versionamento sem gate/ordem | **Resolvido** — `supersedes`=última ∧ `version`=anterior+1 ∧ `expected_version`; sem fork; dedupe | CKG-006/012; EC-CKG-002; ADV-19 |
| F-09 Maior — "quem escreve" aberto; SAS-001 generalizado | **Resolvido como [PROPOSTA]** — tabela capacidade×papel; SAS-001 §6.12 = [INFERÊNCIA] fora do Structural Agent; allowlist concreta = [DECISÃO NECESSÁRIA] (aberta) | CKG-009; tabela de capacidades |
| F-10..F-16 Menores | **Resolvidos** — ver changelog 1.4 (estados do CEM; §D3.1 vocabulário; checks recontado; família estrutural removida; consumo de evento = [INFERÊNCIA]; trace de hipótese/aciclicidade/precedência; igualdade de identidade e INV-04 leitura fiel) | conforme changelog 1.4 |
| F-17 volume | **Registrado, não alterado** — dividir a Spec é decisão de Andraus (Q-ABERTURA-5) | nota de volume |

Itens NÃO adjudicados: não tocados.

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness) na v1.4. 13 BASpecs (Classe D/C/H), 13 EARS, 6 EC (escrita e guard de confiança = E3; ENF-07 nos E3), matriz §D2.1 + tabela de colisão §D2.2, §D3.1, INV-CKG-01/02, proveniência condicional, CKG-010 com critério por tipo [PROPOSTA], 16 cenários (T01..T16), 21 adversariais (ADV-CKG-01..21), CONS-01 preservado (H-001 e demais abertas), gate RMR-001 (BL-029 `Em espera`). Rastreabilidade F-01..F-17 em §11.

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: gate determinístico `validate_spec_sot.py` + `check_repo_research.py` + `build_map.py --check` + `check_doc_sync.py` (ambiente pai — Especificador sem Bash) + submissão ao Revisor SOT.
