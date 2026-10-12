# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.5 (candidato)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-12 (Rodada 6 — CONSOLIDAÇÃO)

> **Nota de método (Rodada 6):** cada achado marcado "Corrigido" em §11/§12 foi conferido por busca cruzada (grep dos termos/IDs) no plan.md v1.5 **e** neste checks.md, confirmando ZERO resíduo contraditório antes de marcar. O que foi só parcialmente endereçado ou segue em aberto está marcado "Parcial"/"Aberto" (não "Corrigido").
> **Itens em aberto (não ✔):** mecanismo físico (H-001); selo de publicação (SPEC-007); produtor/gatilho de promoção trabalho→permanente; consumidor/contrato de consumo de evento pelo KG; emissão pelo KG; allowlist de escritores; host do juízo CKG-008; migração de ontologia; escala de confiança; trace de HIPÓTESE (best-effort [PROPOSTA], sem alegação de completude — M-03).

---

## 0. Consolidação (Rodada 6) — fonte única de regra

| Verificação | Resultado |
|---|---|
| Cada regra normativa definida UMA vez (RULE-CKG-001..013, D2) | ✔ |
| EARS referenciam a regra-fonte por ID (ex.: "(CKG-001) Quando…") | ✔ (13 EARS, cada uma com `(CKG-0NN)`) |
| BASpecs referenciam RULE por "Aplica RULE-CKG-0NN" + REFERÊNCIA | ✔ |
| D4/D6/EC/D7/D8/Herança referenciam por ID, sem recopiar o texto da regra | ✔ |
| Narrativa histórica fora do corpo (só changelog, 1 linha/versão, ordenado 1.0→1.5) | ✔ (m-11) |
| Tamanho: 1576 (v1.4) → **1421 linhas** (v1.5) | ✔ (redução; alvo <1100 não atingido — ver §13) |

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; memória permanente ≠ trabalho; H-001 INDETERMINADO) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA] (fonte única); §D2.1 matriz; §D2.2 colisão; §D3.1 vocabulário; INV-CKG-01/02 |
| D3 Comportamento | Sim | ✔ | BASpec-CKG-001..013 com CLASSE/MECANISMO (CC-11), referenciando a regra |
| D4 Algoritmo | Quando há regra determinística | ✔ | integridade; bitemporal (rejeita valid_to<valid_from); estado derivado+precedência; trace completo da Evidência; versionamento/dedupe (natural_key completo — M-06); gate causal (outcome+posthoc — M-04); confiança; colisão; aciclicidade invertida (M-02) |
| D5 Estado | Sim | ✔ | `knowledge_state` = projeção derivada; ≠ estado canônico (REFUTED só CHM — m-03); transitórios não persistidos |
| D6 Protocolo | Sim | ✔ | sequência; admissão por estado-por-tipo; capacidade×papel (computed_by≠writer_id — M-05); consumo/emissão = [INFERÊNCIA]/[DECISÃO NECESSÁRIA] (m-08) |
| D7 Teste | Sim (≥3) | ✔ | **T01..T16 (16)** |
| D8 Adversarial | Sim (focado) | ✔ | **ADV-CKG-01..21 (21)** — ADV-20 ciclo real (M-02); ADV-04 inclui OUTCOME_REF_MISSING (M-04) |
| D9 Auditoria | Por referência | Parcial | registro reconstruível; trace completo da Evidência; observabilidade agregada = SPEC-040 |

**PASS.**

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

13 BASpecs com QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR + CLASSE/MECANISMO. Classes: C (001,005,006,007,009,010,013), D (002,003,004,011,012), H (008 — bounded loop + gate de saída). Gates C/H determinísticos. **PASS.**

---

## 3. Critérios EARS

13 critérios, cada um prefixado pela regra-fonte `(CKG-0NN)`. EARS 3/4/8/12 cobrem as mecânicas determinísticas (aciclicidade, janela inválida, outcome/posthoc, expected_version/fork) por referência à regra única (m-12). **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 cobrem as 13 BASpecs |
| ENF-02 Nível ≥ piso | ✔ escrita + guard confiança×convicção = E3 (001/002/003/004/005); consulta = E1 (006) |
| ENF-03 Detector ≠ Gate | ✔ EC-003/005; juízo CKG-008 detector, gate determinístico |
| ENF-04 Fail-closed | ✔ EC-001/002/003/005 |
| ENF-05 Policies não auto-aprendidas | ✔ [PROPOSTA] |
| ENF-06 E0 | N/A |
| ENF-07 E3 falso-DENY | ✔ EC-001/002/003/005 (amostral; CONDICIONAL até limiar) |
| ENF-08 Escala E0–E3 | ✔ atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12)

CC-01 (agnóstico; hypothesis.school≠ICT), CC-02 (não redefine), CC-03/04 (INV-04 = custo; confiança = regra local), CC-08 (Herança; **MODIFIED M-01 declara a especialização de preservação "a partir da admissão"**), CC-09 (H-001 INDETERMINADO; causal c/ mecanismo+regime+posthoc+desfecho), CC-10 (acepções; REFUTED só CHM), CC-11 (Classe por BASpec, incl. H) = PASS. CC-05/06/07/12 OK/N-A. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

INHERITS com ID+versão/linha verificados: **SPEC-004 RULE-CBP-004 (l.239-246 — compare-and-commit/expected_version — correção m-06), RULE-CBP-007 (l.543-558), RULE-CBP-014 (l.311-319)**; CEM-001 (l.258-262 estados sem REFUTED; l.264/428; l.468-475/l.473-475 transições proibidas; l.494; l.562-565/l.608-615; l.602); CHM-001; CCM-001 (estados l.58/78 — M-01); SPEC-001 (RULE-HH-003 l.104, RULE-HH-004 l.108, ADV-HH-01 l.515-520, AUTHORIZED_PRODUCERS l.524 — m-06); SPEC-005 (transporta `Evidence.Invalidated` l.88/859); RULE-BB-004, RULE-CAU-01/02/03 (l.680-682), RULE-ONT-01/02 (l.671); atomic-spec §10.2 E3; INV-04/05/06/07/09/10. **MODIFIED = RULE-BB-004 reforçada + especialização M-01 (alcance "a partir da admissão" — RULE-HD-02, não contradição).** REMOVED vazio. **PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001/M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 ABERTAS; SPEC-004/005 não reabertas; SPEC-007 não absorvida | ✔ |
| STRUCT-10: nenhuma forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta (grep case-sensitive dos 7 IDs: 0 afirmações de fechamento) | ✔ |
| `school`/`hierarchy_role` DERIVADOS do produtor (incl. `structure`: produtor que publica — M-06) | ✔ |
| Aciclicidade DERIVA_DE invertida (rejeita se ORIGEM alcançável a partir do DESTINO) — sem resíduo "destino já é ancestral da origem" | ✔ (M-02; grep=0) |
| Preservação de estados = "A PARTIR DA ADMISSÃO"; sem resíduo "TODOS os estados" | ✔ (M-01; grep=0) |
| `computed_by` (produtor autenticado) ≠ `writer_id` (committer); sem resíduo "writer_id == computed_by" | ✔ (M-05; grep=0) |
| CAUSA exige `outcome_ref`+`outcome_timestamp` (ou `no_outcome`); posthoc determinístico | ✔ (M-04) |
| REFUTED só CHM (Evidência não tem REFUTED); sem resíduo "REFUTED do CHM/CEM" | ✔ (m-03; grep=0) |
| SIMILAR_A exclui `conviction` na matriz | ✔ (m-07) |
| natural_key completo (10 tipos, incl. structure/mission/calibration_metric) | ✔ (M-06) |
| Códigos de rejeição: todos em §D3.1 (incl. EXPECTED_VERSION_MISMATCH, INVALID_TIME_WINDOW, FORBIDDEN_CANONICAL_TRANSITION, OUTCOME_REF_MISSING, SCOPE_OR_OPEN_DECISION_VIOLATION); convenção pai/sub explícita | ✔ (m-04) |
| "eventos consumidos" / "D6 consome" → [INFERÊNCIA]/[DECISÃO NECESSÁRIA]; sem afirmativo | ✔ (m-08; grep=0) |
| INVALIDA: `to_node=null` + `target_relation_id`; `valid_to=null`≡+∞ no overlap | ✔ (m-09) |
| record_kind: canonical_state_transition/collision/invalidation/archival têm sequência de version própria (não entram na cadeia supersedes de conteúdo) | ✔ (m-10) |
| SAS-001 §6.12 = FATO NORMATIVO só p/ Structural Agent; extensão = [INFERÊNCIA] (RULE-CKG-009, BASpec-009, EC-003, S9, D6, ADV-07) | ✔ (m-02) |

**PASS (com itens explicitamente em aberto, não ✔).**

---

## 8. Verificação mecânica de citações (abri cada arquivo/linha)

| Citado | Confere? | Fonte |
|---|---|---|
| CEM-001 estados Evidência (sem REFUTED) | ✔ l.258-262 | canon/CEM-001-canonical-evidence-model.md |
| CEM-001 transições proibidas → ACTIVE | ✔ l.473-475 | idem |
| CCM-001 estados conviction COMPUTED/GATED_PASS/GATED_BLOCK/SUPERSEDED | ✔ l.58/78 | canon/CCM-001-canonical-conviction-model.md |
| SPEC-004 RULE-CBP-004 (compare-and-commit; EXPECTED_VERSION_REQUIRED) | ✔ l.239-246 (não l.338 — m-06) | specs/features/SPEC-004/plan.md |
| SPEC-001 RULE-HH-004 (ICT não cria hipótese) | ✔ l.108; ADV-HH-01 l.515-520; AUTHORIZED_PRODUCERS l.524 | specs/features/SPEC-001/plan.md |
| Contagem: 13 BASpecs / 6 EC / 13 EARS / 16 cenários / 21 ADV | ✔ por grep de cabeçalhos | plan.md |
| RULE-CKG-*; INV-CKG-01/02; §D2.1/§D2.2; campos locais | [PROPOSTA] | esta Spec |

Nenhuma citação de baseline sem conferência. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

Nenhum gatilho `spec:SPEC-006` isolado; satisfaz ramos de BL-003/BL-011; BL-010 tangente (SPEC-007); **BL-029 = `Em espera`** (RMR-001 l.128/l.192), independente, não promovido. Passo 11-bis pleno na homologação. **PASS.**

---

## 10. RULE-ECC-04 / RULE-ECC-06 — presença

SRC-ZEP-01/PROV-01/MEMVSKG-01 verbatim em sources/; SRC-FORGET-01 = DADO não-verbatim. 4 repositórios elegíveis (régua Equilibrada); nenhum adotado. RULE-ECC-05 NÃO incide; WORKFLOW por prudência; não fecha WF-D03. **PASS (presença).**

---

## 11. Rastreabilidade — Maiores do parecer sobre a v1.4 (M-01..M-06)

Cada linha conferida por grep cruzado no plan.md v1.5 **e** neste checks.md (resíduo contraditório = 0 onde "Corrigido").

| Achado | Situação | Onde (plan.md) / evidência de grep |
|---|---|---|
| **M-01** admissão exclui EMERGENT/CANDIDATE vs "TODOS os estados" | **Corrigido** — MODIFIED declara especialização "a partir da admissão" (RULE-HD-02); schema `canonical_state_transition` sem EMERGENT/CANDIDATE; conviction = {COMPUTED,GATED_PASS,GATED_BLOCK,SUPERSEDED} (CCM-001 l.58/78). grep "TODOS os estados"=0; grep "EMERGENT\|CANDIDATE\|ACTIVE"=0 | MODIFIED; CKG-010; S10; EARS-10; D6 passo 2; CC-04/07(herança); §7-bis B; schema |
| **M-02** aciclicidade invertida | **Corrigido** — rejeita se ORIGEM alcançável a partir do DESTINO (3 lugares); ADV-20 com ciclo real (A→B,B→C,C→A). grep "destino já é ancestral transitivo"=0 | RULE-CKG-003; BASpec-003; D4; ADV-20 |
| **M-03** trace de hipótese sem gate → completude falsa | **Corrigido** — completude GARANTIDA só p/ EVIDÊNCIA (INV-CKG-02/DERIVA_DE); trace de HIPÓTESE = [PROPOSTA] best-effort, sem alegação de completude; aplicado uniformemente | RULE-CKG-011; BASpec-011; D4; D9; INV-CKG-02; EARS-11 |
| **M-04** pós-hoc contornável (outcome opcional) | **Corrigido** — `outcome_ref`+`outcome_timestamp` obrigatórios (ou `no_outcome=true`+justificativa); subcódigo OUTCOME_REF_MISSING; negativo em T16/ADV-04 | RULE-CKG-008; BASpec-008; D4; §D3.1; EARS-8; T16; ADV-04; schema causal; EC-005 |
| **M-05** writer_id==computed_by perde identidade do produtor | **Corrigido** — `computed_by` = produtor autenticado; `writer_id` = committer (runtime/serviço do KG); distintos; collision/transition = serviço do KG. grep "writer_id == computed_by"=0 | RULE-CKG-005; nota de identidade; D6 tabela; schema (3 records) |
| **M-06** `school` de structure sem fonte; natural_key incompleto | **Corrigido** — `school` de structure derivado do producer_id do agente que a publica (SAS-001 §6.12), por referência; natural_key completo (10 tipos) | §D2.1 nota; D4 dedupe; schema `natural_key`/`school` |

---

## 12. Rastreabilidade — Menores (m-02..m-12) e F-17

| Achado | Situação | Evidência |
|---|---|---|
| m-02 SAS-001 §6.12 generalizado sem [INFERÊNCIA] | **Corrigido** — qualificador "FATO NORMATIVO só p/ Structural Agent; extensão = [INFERÊNCIA]" citado na fonte (RULE-CKG-009) e referenciado em BASpec-009/EC-003/S9/D6/ADV-07 | RULE-CKG-009; D6 |
| m-03 "REFUTED do CHM/CEM" (Evidência não tem REFUTED) | **Corrigido** — D5 e Herança: REFUTED só CHM; Evidência = ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED. grep=0 | D5; INHERITS CEM-001 |
| m-04 códigos fora do §D3.1; pai/sub ambíguo | **Corrigido** — §D3.1 inclui EXPECTED_VERSION_MISMATCH, INVALID_TIME_WINDOW, FORBIDDEN_CANONICAL_TRANSITION, OUTCOME_REF_MISSING, SCOPE_OR_OPEN_DECISION_VIOLATION; convenção pai/sub explícita (T01=ORIGINA_ICT_FORBIDDEN; CKG-001=HYPOTHESIS_SCHOOL_ICT_FORBIDDEN) | §D3.1 |
| m-05 §11 declarava F-10..F-16 "Resolvidos" com Parciais | **Corrigido** — esta §11/§12 só marca "Corrigido" o conferido ponta-a-ponta; abertos ficam "Aberto"/Parcial | §11/§12/nota de método |
| m-06 citações (CBP-004 l.338; ICT l.524; expected_version) | **Corrigido** — CBP-004 → l.239-246; ICT exclusão → l.108/l.515-520 (l.524 = AUTHORIZED_PRODUCERS); expected_version EXIGIDO na atualização (CKG-012). grep "l.338"=0 | Herança; §D2.1; CKG-012; D4 |
| m-07 SIMILAR_A permitia conviction~conviction | **Corrigido** — matriz exclui `conviction` em origem e destino de SIMILAR_A. grep "SIMILAR_A \| qualquer \|"=0 | §D2.1 |
| m-08 "eventos consumidos"/"D6 consome" afirmativos | **Corrigido** — [INFERÊNCIA]/[DECISÃO NECESSÁRIA]. grep "eventos consumidos"=0 | Dependências; D6; §7-bis B |
| m-09 INVALIDA→relação (to_node) / valid_to nulo | **Corrigido** — `to_node=null` + `target_relation_id`; `valid_to=null`≡+∞ no overlap | schema relation_record; §D2.2; D4 |
| m-10 record_kind / versão de transição/invalidação | **Corrigido** — sequência de version própria (fora da cadeia supersedes de conteúdo) declarada no schema | schema (version notes) |
| m-11 histórico fora de ordem | **Corrigido** — changelog 1.0→1.5, 1 linha/versão | Histórico de versões |
| m-12 novas regras sem EARS/T/ADV | **Corrigido** — cobertas por referência: aciclicidade (EARS-3/BASpec-003/ADV-20), janela inválida (EARS-4/T04/ADV-13), transição canônica (EARS-2/CKG-002/T09/ADV-11), fork/expected_version (EARS-12/CKG-012/ADV-19), outcome (EARS-8/T16/ADV-04); trace de hipótese = [PROPOSTA] sem completude (sem T dedicado, justificado — M-03). Contagem recontada por grep de cabeçalhos | EARS; D7; D8 |
| F-17 volume | **Registrado, NÃO dividido** — dividir é decisão de Andraus (Q-ABERTURA-5) | nota de volume |

---

## 13. Observação de volume (consolidação)

Redução de 1576 → **1421 linhas**. A regra agora é definida uma única vez (D2) e referenciada; eliminados os textos de
regra duplicados e as anotações históricas "(F-xx)" do corpo. O alvo `<1100` NÃO foi atingido sem risco à cobertura
(13 BASpecs/16 T/21 ADV/6 EC/§D2.1/§D2.2/§D3.1/schema são conteúdo atômico legítimo de uma Spec CRITICAL). **Dividir a
Spec é decisão exclusiva de Andraus (Q-ABERTURA-5; F-17)** — não feito. Encaminho a decisão de redução adicional vs.
divisão a Andraus.

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness) na v1.5. 13 BASpecs (D/C/H), 13 EARS (referenciando regra-fonte), 6 EC
(escrita e guard = E3), §D2.1/§D2.2/§D3.1, INV-CKG-01/02, proveniência condicional, CKG-010 por tipo [PROPOSTA], 16
cenários, 21 adversariais, CONS-01 preservado (H-001 e demais abertas), gate RMR-001 (BL-029 `Em espera`). M-01..M-06 e
m-02..m-12 em §11/§12 com grep cruzado = 0 resíduo contraditório onde "Corrigido".

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: gates no
> ambiente pai (Especificador sem Bash) — `validate_spec_sot.py`, `revisor_gate.py`, `check_repo_research.py --all`,
> `check_doc_sync.py`, `check_invariants.py`, `build_map.py --check` — e submissão ao Revisor SOT.
