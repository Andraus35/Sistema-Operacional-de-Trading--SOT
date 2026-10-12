# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.3 (candidato)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico de armazenamento INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-12 (Rodada 4)

> **Nota de método (correção vs. v1.2):** cada afirmação de "reescrito/resolvido" abaixo foi conferida abrindo o plan.md. Em particular, **T01 FOI de fato reescrito nesta v1.3** (a v1.2 o checks.md afirmara falsamente que T01 estava reescrito — ele ainda mandava rejeitar "HERDA entre famílias diferentes", caso que a matriz NÃO rejeita). Corrigido.
> **Itens em aberto (não marcados ✔):** mecanismo físico (H-001); selo de publicação (SPEC-007); **critério/produtor/gatilho de admissão do caminho (a)** (NÃO-ESPECIFICADO/INDETERMINADO; reatribuição a SPEC-018/K-001 submetida a Andraus); consumidor/contrato de consumo de evento pelo KG; emissão pelo KG; allowlist de escritores; host do juízo CKG-008; migração de ontologia; escala de confiança.

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — alvo ROADMAP §6; CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; memória permanente ≠ trabalho; mecanismo físico INDETERMINADO) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA]; **matriz §D2.1** (`school` único, `hierarchy_role`, família via PERTENCE_A, CONFIRMA/REFUTA só evidence, CAUSA restrita) + **tabela de colisão §D2.2**; INV-CKG-01/02 |
| D3 Comportamento (BASpec) | Sim | ✔ | CKG-001..013 com CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | integridade+regra de nó, bitemporal (valid-time+transaction-time), imutabilidade/estado derivado, trace completo (INV-CKG-02), dedupe (natural_key), gate causal, namespace confiança, **detecção de colisão §D2.2** |
| D5 Estado | Sim | ✔ | `knowledge_state` = projeção derivada; ≠ estado canônico; transitórios (CANDIDATE_WRITE/REJECTED/PENDING_ANCESTOR) não persistidos |
| D6 Protocolo | Sim | ✔ | Sequência; invalidação = ato autorizado (não cascata); consumo/emissão de evento = [DECISÃO NECESSÁRIA] |
| D7 Teste | Sim (CRITICAL; ≥3) | ✔ | **T01..T15 (15)** — T01 (violação real: ORIGINA school=ICT), T12 (caso-feliz proveniência condicional), T14 (sem computed_by), **T15 (positivo HERDA cross-escola)** |
| D8 Adversarial | Sim (CRITICAL, focado) | ✔ | **ADV-CKG-01..18 (18)** — inclui ADV-17 (hypothesis.school=ICT) e ADV-18 (escopo de colisão: falso-positivo/negativo) |
| D9 Auditoria | Por referência | Parcial | registro reconstruível; trace completo (INV-CKG-02); observabilidade agregada = SPEC-040 |

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
| CKG-010 fronteira (a=INDETERMINADO; b=selo SPEC-007 verificável) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate (b) ✔ / (a) INDETERMINADO |
| CKG-011 consulta/trace completo (read-only) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-012 lifecycle (estado derivado) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-013 colisão (tabela §D2.2 + escopo + overlap) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |

**PASS.**

---

## 3. Critérios EARS

13 critérios "Quando <condição>, o KG DEVE/NÃO DEVE <resposta>". EARS 7 (confiança namespace próprio) e a proveniência condicional (EARS 5/9) coerentes com CKG-005/007. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 cobrem as 13 BASpecs e toda RULE-CKG |
| ENF-02 Nível ≥ piso | ✔ escrita permanente = E3 (001/002/003/005); E2 (004); E1 (006) |
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
| `school` é campo ÚNICO (origin_agent eliminado); `hierarchy_role` adicionado; família via PERTENCE_A | ✔ |
| Regra de nó `hypothesis.school ≠ ICT` (INV-02/RULE-HH-004) com teste (T01/ADV-17); HERDA pai=PRIMARY | ✔ |
| HERDA cross-escola VÁLIDO (T15 positivo); "família" só intra-escola | ✔ |
| Proveniência CONDICIONAL (computed_by sempre; gate_record/lineage condicionais; `[]` legítimo) — espelha CBP-007; não fabrica | ✔ |
| `Evidence.Invalidated` é canônico (CEM-001 l.600/722) e transportado pela SPEC-005 (l.88/859); falta consumidor = [DECISÃO NECESSÁRIA] | ✔ |
| Colisão com tabela §D2.2 + escopo (mesmos from/to + overlap de validade) + teste negativo (ADV-18) | ✔ |
| CKG-010 caminho (a) = NÃO-ESPECIFICADO/INDETERMINADO (não gate vacuoso); [PROPOSTA] de critério mínimo; reatribuição S14 → Andraus [DECISÃO NECESSÁRIA]; ordem de ancestrais (PENDING_ANCESTOR, sem deadlock) | ✔ (abertos declarados) |
| INV-04 = só custo; confiança = regra local [PROPOSTA]; CAUSA custo/confiança→conviction proibida | ✔ |
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
| T01 (ORIGINA school=ICT), T12 (PRIMARY lineage=[]), T14 (sem computed_by), T15 (HERDA cross-escola) | ✔ existem e dizem o afirmado | plan.md D7 |
| ADV-17 (hypothesis.school=ICT), ADV-18 (escopo colisão) | ✔ existem | plan.md D8 |
| Contagem: 13 BASpecs / 6 EC / 13 EARS / 15 cenários / 18 ADV | ✔ conferido por grep de cabeçalhos (15 Cenário + 18 ADV = 33) | plan.md |
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

## 11. Rastreabilidade dos 6 Maiores da Rodada 4 (autocontida)

| Item R4 | Situação | Onde (plan.md) |
|---|---|---|
| 1 [MAIOR] T01 falso/positivo faltante | **Resolvido** — T01 reescrito (ORIGINA `school=ICT`, que a matriz REJEITA) + **T15** positivo (HERDA SMC-SUB→Elliott-PRIMARY). **Conferido abrindo o plan.md** (a v1.2 NÃO havia reescrito T01 — correção da falsa afirmação do checks v1.2). | D7 T01/T15; §7-bis Bloco A |
| 2 [MAIOR] campos faltantes/ambíguos | **Resolvido** — campo ÚNICO `school` (origin_agent eliminado); `hierarchy_role` {PRIMARY,SUB} (ref. SPEC-001); família COMPUTADA via `school`+PERTENCE_A(asset,timeframe); regra de nó `hypothesis.school≠ICT` (INV-02/RULE-HH-004) + T01 + ADV-17; HERDA pai=PRIMARY (RULE-HH-003) | §D2.1 nota; matriz; BASpec-CKG-001; schema node_record |
| 3 [MAIOR] gate_record universal | **Resolvido** — espelha CBP-007: `computed_by` sempre (identidade autenticada); `gate_record` só se gate; `lineage`/`derived_from` só se derivado; `[]` legítimo; sem fabricar (RULE-MET-01) | RULE-CKG-005; BASpec-CKG-005; T12/T14; schema provenance_ref |
| 4 [MAIOR] SPEC-005/Evidence.Invalidated | **Resolvido** — o tipo é canônico (CEM-001 l.600/722) e a SPEC-005 o TRANSPORTA (l.88/859); falta consumidor/contrato = [DECISÃO NECESSÁRIA]; citação errada l.115/242 (envelope) removida | INHERITS SPEC-005; D6 passo 10; bloco de consumo |
| 5 [MAIOR] CKG-013 sem tabela/escopo | **Resolvido** — tabela §D2.2 (CONFIRMA×REFUTA simétrica; INVALIDA×relação-alvo); escopo (mesmos from/to + overlap de validade); algoritmo D4; teste negativo **ADV-18** | §D2.2; RULE-CKG-013; BASpec-CKG-013; D4; ADV-18 |
| 6 [MAIOR] CKG-010 gate vacuoso | **Resolvido/[DECISÃO NECESSÁRIA]** — caminho (a) declarado NÃO-ESPECIFICADO/INDETERMINADO (não gate verificável) + [PROPOSTA] de critério mínimo (exclui EMERGENT/CANDIDATE); reatribuição S14→SPEC-018/K-001 submetida a Andraus; ordem de ancestrais (PENDING_ANCESTOR) evita deadlock de INV-CKG-02 | BASpec-CKG-010; bloco [DECISÃO NECESSÁRIA]; S14; INV-CKG-02 |

Itens NÃO adjudicados pelo controle: não tocados (conforme instrução).

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). 13 BASpecs (Classe D/C/H), 13 EARS, 6 EC (escrita=E3; ENF-07 nos E3), matriz §D2.1 + tabela de colisão §D2.2, INV-CKG-01/02, proveniência condicional (espelha CBP-007), SPEC-005 corrigido, CKG-010 não-vacuoso (a=INDETERMINADO), 15 cenários (T01..T15), 18 adversariais (ADV-CKG-01..18), CONS-01 preservado, Herança/Delta com citações conferidas, gate RMR-001 (BL-029 `Em espera`). Rastreabilidade autocontida dos 6 Maiores em §11; cada "reescrito" foi confirmado no plan.md.

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: gate determinístico `validate_spec_sot.py` + `check_repo_research.py` + `build_map.py --check` + `check_doc_sync.py` (ambiente pai — Especificador sem Bash) + submissão ao Revisor SOT.
