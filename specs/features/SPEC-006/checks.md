# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.4 (candidato — rodada 5)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico de armazenamento INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-17 (Rodada 5 — retomada por ordem de Andraus, chat 2026-10-17: "Retomar o Plan da SPEC-006")

> **Nota de método:** cada item "corrigido" abaixo foi conferido abrindo o plan.md v1.4 e a fonte citada (arquivo:linha). Nenhum validador foi executado pelo Especificador (sem Bash) — ver §12 (comandos que o Orquestrador deve rodar).
> **Itens em aberto (não marcados ✔):** mecanismo físico (H-001); selo de publicação (SPEC-007); **critério/produtor/gatilho de admissão do caminho (a)** (fail-closed enquanto pendente); **caminho de entrada de nós de referência**; **mapeamento produtor→Fractal**; consumidor/contrato de consumo de evento pelo KG; emissão pelo KG; allowlist de escritores; host do juízo CKG-008; migração de ontologia; escala de confiança; **limiar/amostra de falso-DENY (ENF-07)**; **reconciliação COL-EXP-05**.

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — alvo ROADMAP §6; CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; memória permanente ≠ trabalho; mecanismo físico INDETERMINADO) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals; S10 com (a) fail-closed e lacuna de nós de referência |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA]; matriz §D2.1 (`school` LOCAL derivado, 5 camadas, PRIMARY ⇒ Elliott; SIMILAR_A com `similarity_basis`); tabela de colisão §D2.2; INV-CKG-01/02; RULE-CKG-008 com bounded loop explícito |
| D3 Comportamento (BASpec) | Sim | ✔ | CKG-001..013 com CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | envelope único `envelope_completo`; bitemporal com `target_record_ref`; imutabilidade/estado derivado; trace; dedupe; gate causal + SIMILAR_A; **bounded loop (1 invocação por submissão)**; colisão; regras de nó; **fronteira (a) fail-closed**; **ordem de ancestrais por lote** |
| D5 Estado | Sim | ✔ | `knowledge_state` = projeção derivada; transitórios **CANDIDATE_WRITE / PENDING_ANCESTOR / REJECTED** com tabela de transições de admissão (PENDING_ANCESTOR limitado ao lote) |
| D6 Protocolo | Sim | ✔ | Sequência 1–10 (+5-bis); **passo 5 = proveniência CONDICIONAL** (igual a CKG-005); passo 2 com (a) fail-closed |
| D7 Teste | Sim (CRITICAL; ≥3) | ✔ | **T01..T19 (19)** + convenção de teste (gate em isolamento / fixture / persistência por (a) CONDICIONAL) |
| D8 Adversarial | Sim (CRITICAL, focado) | ✔ | **ADV-CKG-01..22 (22)** |
| D9 Auditoria | Por referência | Parcial | envelope único para todo registro; replay (T17); observabilidade agregada = SPEC-040 |

**Resultado:** profundidade-alvo D0–D7 atingida; D8 focado. **PASS (estrutural).**

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REF | VERIF. | CLASSE | Gate/bounded |
|---|---|---|---|---|---|---|---|
| CKG-001 ontologia + matriz + regras de nó (school derivável; ≠ICT; PRIMARY⇒Elliott; HERDA pai=PRIMARY) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-002 ref canônica + canonical_status (enum por modelo) + transição no envelope | ✔ | ✔ | ✔ | ✔ | ✔ (ref/rótulo/enum); gravação ponta-a-ponta INDETERMINADO (depende de (a)) | D | N/A |
| CKG-003 relação tipada/proveniência/DERIVA_DE por ancestral | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-004 temporalidade (ato autorizado; novo registro; bitemporal) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-005 proveniência CONDICIONAL | ✔ | ✔ | ✔ | ✔ | ✔ (predicado do gate) | C | gate ✔ |
| CKG-006 imutabilidade/append-only + envelope único (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-007 confiança namespace próprio (≠ convicção) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-008 causal + SIMILAR_A | ✔ | ✔ | ✔ | ✔ | ✔ | H | **bounded = 1 passada; esgotou ⇒ INDETERMINADO** ✔ + gate ✔ |
| CKG-009 governança de escrita (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-010 fronteira | ✔ | ✔ | ✔ | ✔ | ✔ em (b) e no DENY de (a); admissão positiva por (a) **INDETERMINADO** | C | gate (b) ✔ / (a) DENY fail-closed |
| CKG-011 consulta/trace completo (read-only) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-012 lifecycle (estado derivado) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-013 colisão (tabela §D2.2 + escopo + overlap; registro no envelope) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |

**PASS (com CKG-010(a) explicitamente INDETERMINADO — não marcado como verificável).**

---

## 3. Critérios EARS

13 critérios "Quando <condição>, o KG DEVE/NÃO DEVE <resposta>". Alterados na v1.4: **EARS 6** (envelope único + rejeição de envelope incompleto), **EARS 8** (SIMILAR_A + uma passada/INDETERMINADO), **EARS 10** (caminho (a) rejeitado enquanto pendente), **EARS 13** (colisão no envelope, com validade sobreposta). Coerentes com CKG-005/006/008/010/013. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 cobrem as 13 BASpecs e toda RULE-CKG |
| ENF-02 Nível ≥ piso | ✔ escrita permanente = E3 em **001/002/003/004/005** (004 elevado de E2 → E3 — R6; atomic-spec l.238); E1 (006, read-only) |
| ENF-03 Detector ≠ Gate | ✔ EC-003/005; juízo CKG-008 detector, gate determinístico; escore do juízo não aceita SIMILAR_A |
| ENF-04 Fail-closed | ✔ EC-001/002/003/004/005; **pendência do critério (a) = precondição não satisfeita ⇒ DENY** |
| ENF-05 Policies não auto-aprendidas | ✔ [PROPOSTA]; limite "uma passada" versionado com a RULE (não parâmetro de runtime) |
| ENF-06 E0 | N/A |
| ENF-07 E3 falso-DENY | ✔ **método** amostral declarado (DENY registrado; amostra reavaliada por re-execução determinística + revisão humana) nos E3; **limiar/tamanho de amostra = gap aberto** (atomic-spec l.273/l.393) — CONDICIONAL, nenhum valor inventado |
| ENF-08 Escala E0–E3 | ✔ atomic-spec §10.2 |

**PASS (ENF-07 com gap aberto declarado).**

---

## 5. Constitution Check (CC-01..CC-12)

CC-01 (agnóstico; `school` com as **5 camadas** — Fractal incluído; `hypothesis.school ≠ ICT`; PRIMARY ⇒ Elliott; HERDA cross-escola passa no gate), CC-02 (não redefine; `school` declarado LOCAL derivado de `producer_id`, não campo canônico; enum de `canonical_status` por modelo; `gate_record`/`computed_by` = SPEC-004), CC-08 (Herança; obrigação "preservar todos os estados" com evidência PARCIAL/[DECISÃO NECESSÁRIA] declarada — não suprimida), CC-09 (INDETERMINADO não convertido em PASS no EC-CKG-001; bounded loop → INDETERMINADO), CC-10 (`school` ≠ `Domain`; estados do KG ≠ canônicos; REFUTED só CHM, INVALIDATED só CEM), CC-11 (Classe por BASpec; H com parada explícita) = PASS. CC-03/04 (INV-04 = só custo; confiança = regra local; EC-004 em E3). CC-05/06/07/12 OK/N-A. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

INHERITS com ID+versão/linha reconferidos na v1.4: SPEC-004 RULE-CBP-007 (proveniência CONDICIONAL) + RULE-CBP-014; CEM-001 (Status l.258-264; Producer ID l.276-278; `Lineage` l.351-362; mutação só de Status l.428; consumo pelo KG l.494; trace l.562-578; não-cascata l.602; responsabilidades l.608-615); CHM-001 (estados l.329; proveniência `producer_type`/`producer_id` §2.9 l.361; `parent_hypothesis_id` l.165/415; terminais l.769); CCM-001 (`status` l.58); SPEC-001 (RULE-HH-002 l.100, RULE-HH-003 l.104, RULE-HH-004 l.108; `hierarchy_role` l.87/l.844; `producer_id` exemplo l.203); RULES.md (RULE-BB-004 **l.324**; RULE-ONT-01 **l.672**; RULE-INQ-03 **l.678**; RULE-CAU-01/02/03 **l.681-683** — a v1.3 citava l.323/671/680-682); atomic-spec l.238 (piso E3), l.273/l.393 (ENF-07/gap), l.315 (bounded loop); CONFLICT-MAP l.143-147 (COL-EXP). REMOVED vazio; MODIFIED = só RULE-BB-004 reforçada. **PASS (com evidência parcial declarada em "preservar todos os estados").**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001 NÃO decidida; Opção B ADIADA | ✔ |
| Proveniência condicional idêntica em RULE-CKG-005, BASpec-CKG-005, **D6 passo 5**, schema, T12/T14/**T16**, ADV-06 | ✔ (V1) |
| Caminho (a): RULE-CKG-010, BASpec-CKG-010, D4, D6 passo 2, **EC-CKG-001 PRECOND**, EARS 10, T09/T16, ADV-21, §7-bis Bloco A/B — todos dizem "fail-closed enquanto pendente; admissão positiva INDETERMINADO" | ✔ (V2) |
| Um só formato de registro (`kg_record`) em RULE-CKG-006/013, INV-CKG-01, BASpec-CKG-002/013, D4, D6, D9, contrato, schema, T11/T17, ADV-18/19 | ✔ (V3) — `collision_record` avulso e `record_kind=collision` em relação eliminados |
| Bounded loop "uma passada → INDETERMINADO" em RULE-CKG-008, BASpec-CKG-008, D4, EC-CKG-005, EARS 8, ADV-20 | ✔ (V4) |
| `PENDING_ANCESTOR` em INV-CKG-02, D4, **D5**, D6 5-bis, T19 | ✔ (R1) |
| `canonical_status` com enum por modelo (REFUTED só CHM-001) | ✔ (R2) |
| `school` LOCAL derivado; 5 camadas; Fractal mapeamento [DECISÃO NECESSÁRIA] | ✔ (R3) |
| COL-EXP-01..05 com tratamento; COL-EXP-05 adiada | ✔ (R4) |
| SIMILAR_A com gate determinístico (RULE/BASpec/D4/D6/matriz/schema/EC-005/T18/ADV-22) | ✔ (R5) |
| EC-CKG-004 = E3 (EC, D3 cabeçalho, §7 autopré-check, Bloco B) | ✔ (R6) |
| Nó com `valid_from`/`valid_to`; todo registro com `target_record_ref` | ✔ (R7) |
| Limiar de falso-DENY = gap aberto, sem valor | ✔ (R8) |
| M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 ABERTAS; SPEC-004/005 não reabertas; SPEC-007 não absorvida | ✔ |
| Nenhuma forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta (STRUCT-10) | conferência manual ✔ — **confirmar com o gate (§12)** |

**PASS (com itens explicitamente em aberto, não marcados ✔).**

---

## 8. Verificação mecânica de citações (abri cada arquivo/linha nesta rodada)

| Citado | Existe / diz o afirmado? | Fonte verificada |
|---|---|---|
| CEM-001 Status = ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED (sem REFUTED); só Status mutável | ✔ | canon/CEM-001 l.257-264; l.444-466 |
| CEM-001 Producer ID | ✔ | canon/CEM-001 l.276-278 |
| CHM-001 estados (inclui REFUTED) e proveniência `producer_type`/`producer_id` (sem campo de escola) | ✔ | canon/CHM-001 l.329; l.359-363; l.769 |
| CCM-001 status COMPUTED/GATED_PASS/GATED_BLOCK/SUPERSEDED | ✔ | canon/CCM-001 l.58 |
| SPEC-001 RULE-HH-002/003/004; `hierarchy_role`; `producer_id == "elliott_specialist"` | ✔ | specs/features/SPEC-001/plan.md l.100/104/108; l.87/844; l.203 |
| Fractal sem especialista produtor listado; Fractal Confluence (FCES) | ✔ | AGENTS.md §3.2; governance/CONSTITUTION.md l.237 |
| atomic-spec: piso E3 "KG publicado"; ENF-07; bounded loop; gap de falso-DENY | ✔ | atomic-spec.md l.238; l.273; l.315; l.393 |
| RULE-INQ-03 (encerramento → INDETERMINADO) | ✔ | governance/RULES.md l.678 |
| RULE-BB-004 / RULE-ONT-01 / RULE-CAU-01..03 (linhas corrigidas) | ✔ | governance/RULES.md l.324 / l.672 / l.681-683 |
| Precedente bounded loop "uma passada … encerra em undetermined" | ✔ | specs/features/SPEC-002/plan.md l.370-371; specs/features/SPEC-003/plan.md l.387-388 |
| COL-EXP-01..05 e "ADIAR reconciliação (SPEC-006/009)"; residuais R-04..R-06 adiados | ✔ | governance/CONFLICT-MAP.md l.143-147; governance/CLASSIFICACAO-COLISOES-BL010-011-012.md l.53-62 |
| Contagem: 13 BASpecs / 6 EC / 13 EARS / 19 cenários / 22 ADV / 2 INV locais | ✔ conferido por busca de cabeçalhos (`### BASpec-CKG-` ×13; `### Cenário-CKG-T` ×19; `### ADV-CKG-` ×22; `### EC-CKG-` ×6) | plan.md |
| RULE-CKG-*; INV-CKG-01/02; §D2.1/§D2.2; `kg_record`; `school`; `similarity_basis`; bounded loop "uma passada" | [PROPOSTA] | esta Spec — campos/regras locais |

Nenhuma citação de baseline sem conferência. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- Nenhum gatilho `spec:SPEC-006` isolado; satisfaz ramos de BL-003/BL-011 (`spec:SPEC-006`); BL-010 tangente (SPEC-007). ✔
- BL-011: tabela de tratamento COL-EXP-01..05 adicionada; reconciliação COL-EXP-05 **não executada** (adiada; [DECISÃO NECESSÁRIA]). ✔
- **BL-029 = `Em espera`** (RMR-001 l.128 + l.192); independente; não promovido. ✔ *(linhas do RMR-001 não reconferidas nesta rodada — o Orquestrador confirma via `backlog_triggers.py`.)*
- Passo 11-bis pleno na homologação. **PASS.**

---

## 10. RULE-ECC-04 / RULE-ECC-06 — presença

- SRC-ZEP-01/PROV-01/MEMVSKG-01 verbatim em sources/; SRC-FORGET-01 = DADO não-verbatim (não sustenta alegação carregada). ✔
- 4 repositórios elegíveis (régua Equilibrada); nenhum adotado. Nenhuma pesquisa web nova nesta rodada (correções internas, ancoradas em baselines do repositório). ✔
- RULE-ECC-05 NÃO incide (infra de memória); WORKFLOW por prudência; não fecha WF-D03. ✔
- **PASS (presença).**

---

## 11. Rastreabilidade da Rodada 5 (V1–V4 conferidos pelo Orquestrador; R1–R8 reconferidos pelo Especificador)

| Item | Procede? | Correção (plan.md v1.4) |
|---|---|---|
| V1 — D6.5 exigia lineage+gate_record sempre | Sim | D6 passo 5 condicional; T12 vira teste de predicado; **T16** sequência D6 (PRIMARY sem gate/ancestral: para no passo 2 por (a) pendente; passo 5 = PASS sem exigir gate_record/lineage); BASpec-CKG-005 VERIFICAÇÃO em termos de predicado; ADV-06 alinhado |
| V2 — EC-CKG-001 admitia (a) INDETERMINADO; frase "todas as 13 verificáveis" | Sim | PRECOND do EC-CKG-001 exclui (a) enquanto pendente (DENY `PATH_A_ADMISSION_PENDING`); RULE/BASpec-CKG-010, D4, D6, EARS 10, T09, ADV-21; frase de cobertura reescrita (12 + CKG-010 parcial); Bloco B: "preservar todos os estados" = evidência parcial/[DECISÃO NECESSÁRIA]; convenção de teste em D7 |
| V3 — registros especiais sem envelope; dois formatos de colisão | Sim | envelope único `kg_record` (record_id, record_kind, subject_kind/id, version, supersedes, target_record_ref, schema_version, provenance_ref, writer_id, publication, recorded_at, valid_from/valid_to, payload); RULE-CKG-006/013, INV-CKG-01, D4 `envelope_completo`, D9, contrato, schema; **T17** (reconstrução/auditoria); **ADV-19** |
| V4 — bounded loop sem valor/fonte/esgotamento | Sim | "UMA passada por submissão; sem retry; esgotou ⇒ INDETERMINADO, nada escrito; re-submissão idêntica não re-invoca"; fonte atomic-spec l.315 + RULE-INQ-03 l.678 + SPEC-002 l.370-371/SPEC-003 l.387-388; versionado com RULE-CKG-008; RULE/BASpec/D4/EC-CKG-005; **ADV-20** |
| R1 — PENDING_ANCESTOR fora da D5 | Sim | D5 com tabela de transições de admissão; limitado ao lote (`ANCESTOR_NOT_ADMITTED`); D4; D6 5-bis; **T19** |
| R2 — REFUTED no CEM-001 | Sim (CEM-001 l.258-262 não tem REFUTED) | enum de `canonical_status`/`status_to` por modelo (CHM/CEM/CCM); RULE/BASpec-CKG-010; D5; [PROPOSTA] de critério mínimo só para hypothesis |
| R3 — `school` sem origem canônica; Fractal ausente | Sim (CHM-001 não tem campo de escola; enum omitia Fractal) | `school` LOCAL [PROPOSTA] derivado de `producer_id`; enum 5 camadas; PRIMARY ⇒ Elliott (RULE-HH-002); `SCHOOL_UNDERIVABLE`; mapeamento →Fractal [DECISÃO NECESSÁRIA]; `school` ≠ `Domain` |
| R4 — COL-EXP em uma linha só | Em parte (os IDs existem no CONFLICT-MAP l.143-147; faltava a aplicação) | tabela COL-EXP-01..05 na Nota de gate; COL-EXP-05 adiada [DECISÃO NECESSÁRIA] |
| R5 — SIMILAR_A sem gate de saída | Sim | gate `similarity_basis` ∧ mesmo node_type ∧ from≠to; duplicata simétrica no-op; **T18**; **ADV-22** |
| R6 — EC-CKG-004 em E2 | Sim (piso atomic-spec l.238) | EC-CKG-004 → E3 + falso-DENY; cabeçalho D3; Bloco B; autopré-check |
| R7 — nó sem `ref`/`valid_to` | Sim | nó com `valid_from`/`valid_to`; `target_record_ref` no envelope (substitui o `ref` informal do D4) |
| R8 — limiar falso-DENY | Procede como gap (não é defeito a "corrigir" com número) | mantido gap aberto; declarado só o MÉTODO amostral (ENF-07); [DECISÃO NECESSÁRIA] |
| Extra — linhas de RULES.md deslocadas | Sim | l.324/l.672/l.681-683 (+ RULE-INQ-03 l.678) |
| Extra — nós de referência sem caminho de entrada | Identificado nesta rodada | lacuna [DECISÃO NECESSÁRIA]; fail-closed `ENTRY_PATH_UNDEFINED` |

---

## 12. Comandos que o Orquestrador deve rodar (Especificador sem Bash — NÃO executados)

```
python scripts/validate_spec_sot.py specs/features/SPEC-006/plan.md      # gate determinístico (STRUCT-10 etc.)
python scripts/revisor_gate.py specs/features/SPEC-006/plan.md           # gate fundido do Revisor (Classe D + sinais H)
python scripts/check_repo_research.py specs/features/SPEC-006            # RULE-ECC-06
python scripts/check_invariants.py specs/features/SPEC-006/plan.md       # valores/ordem das regras fixas (informativo)
python scripts/check_refs.py                                             # referências cruzadas
python scripts/check_doc_sync.py                                         # drift documental (informativo)
python scripts/backlog_triggers.py                                       # gatilhos RMR-001 (BL-003/010/011/029)
python scripts/build_map.py && python scripts/build_map.py --check       # BL-019 — mapa em dia
npm run lint                                                             # lint EARS
```

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness), com os pontos INDETERMINADOS declarados: 13 BASpecs (Classe D/C/H), 13 EARS, 6 EC (escrita = E3 em 001..005; ENF-07 com método e limiar em aberto), matriz §D2.1 + tabela §D2.2, INV-CKG-01/02, envelope único, proveniência condicional coerente em todas as representações, caminho (a) fail-closed, bounded loop explícito, 19 cenários (T01..T19), 22 adversariais (ADV-CKG-01..22), CONS-01 preservado.

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: comandos do §12 (ambiente do Orquestrador) + submissão ao Revisor SOT; decisões [DECISÃO NECESSÁRIA] encaminhadas a Andraus.
