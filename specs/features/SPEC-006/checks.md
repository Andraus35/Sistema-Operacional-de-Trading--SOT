# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.9 (ERRATA PROPOSTA — aditiva/Minor sobre a BASELINE v1.7; INV-07: nada apagado)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-16 (v1.9 — ERRATA N-01..N-06 do parecer do Revisor sobre a v1.8; v1.8 = ERRATA A-01..A-14 da auditoria independente; v1.7 = Reconciliação BL-011; v1.6 = Rodada 7 N-01..N-09 do parecer sobre a v1.5)
**Contagens v1.9 (por cabeçalho — recontadas no ambiente pai; declaradas aqui):** 13 BASpec (`### BASpec-CKG-`), 13 EARS (`^N. (CKG-`), 6 EC (`### EC-CKG-`), **19 cenários (`### Cenário-CKG-T` — T01..T19)**, **23 ADV (`### ADV-CKG-` — ADV-01..23)**, INV-CKG-01/02. Alinhadas plan ↔ checks ↔ changelog. (N-01..N-06 são aditivos POR REFERÊNCIA — não criam BASpec/EARS/EC/T/ADV novos; alteram regra/predicado e propagam por ID.)

> **Nota de método (Rodada 7):** cada achado marcado "Corrigido" em §11/§12/§14 foi conferido por busca cruzada (grep dos termos/IDs) no plan.md v1.6 **e** neste checks.md, confirmando ZERO resíduo contraditório antes de marcar. Afirmações de grep abaixo são REAIS (rodadas com a ferramenta de busca). O que foi só parcialmente endereçado ou segue em aberto está marcado "Parcial"/"Aberto" (não "Corrigido").
> **Itens em aberto (não ✔):** mecanismo físico (H-001); selo de publicação (SPEC-007); produtor/gatilho de promoção trabalho→permanente; consumidor/contrato de consumo de evento pelo KG; emissão pelo KG; allowlist de escritores; host do juízo CKG-008; migração de ontologia; escala de confiança; **limite/timeout da espera `PENDING_ANCESTOR` (N-07)**; trace de HIPÓTESE (best-effort [PROPOSTA], sem alegação de completude — M-03); **origem/escola de `structure` e elo structure→hypothesis + `school=Fractal` sem produtor — CKG-STRUCT-ORIGIN-001 (N-01/N-09), BL-035**.

---

## 0. Consolidação (fonte única de regra) — preservada da Rodada 6

| Verificação | Resultado |
|---|---|
| Cada regra normativa definida UMA vez (RULE-CKG-001..013, D2) | ✔ |
| EARS referenciam a regra-fonte por ID (ex.: "(CKG-001) Quando…") | ✔ (13 EARS, cada uma com `(CKG-0NN)`; EARS-9 passou a `(CKG-009/005)` cobrindo computed_by≠writer_id — N-03) |
| BASpecs referenciam RULE por "Aplica RULE-CKG-0NN" + REFERÊNCIA | ✔ |
| D4/D6/EC/D7/D8/Herança referenciam por ID, sem recopiar o texto da regra | ✔ |
| Narrativa histórica fora do corpo (só changelog, 1 linha/versão, ordenado 1.0→1.9) | ✔ |
| Tamanho: cresce pela regra/predicado de N-01/N-02/N-05/N-06 (aditivo por referência); número exato de linhas OMITIDO aqui (conferir com `wc -l` no ambiente pai — N-04); alvo <1100 não atingido (ver §13) | ✔ |
| Reconciliação BL-011 / MC-EXP-001 presente (seção curta A/B/C); EXP-SPEC-001..053 e X-/R- mapeados a RULE-CKG existentes (REFERÊNCIA) ou FORA (SPEC-007/018/K-001); nenhuma RULE-CKG nova; nenhuma decisão aberta fechada | ✔ |

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; memória permanente ≠ trabalho; H-001 INDETERMINADO) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA] (fonte única); §D2.1 matriz; §D2.2 colisão (cond. (v) — N-08); §D3.1 vocabulário; INV-CKG-01/02 |
| D3 Comportamento | Sim | ✔ | BASpec-CKG-001..013 com CLASSE/MECANISMO (CC-11), referenciando a regra |
| D4 Algoritmo | Quando há regra determinística | ✔ | integridade; bitemporal; estado derivado+precedência; trace completo da Evidência; versionamento/dedupe (códigos EXPECTED_VERSION_REQUIRED/VERSION_CONFLICT — N-04); gate causal (outcome derivado+posthoc — N-02); confiança; colisão (cond. (v) — N-08); aciclicidade invertida + self-loop (M-02/N-07) |
| D5 Estado | Sim | ✔ | `knowledge_state` = projeção derivada; ≠ estado canônico (REFUTED só CHM; SUPERSEDED/ARCHIVED também na Evidência — N-06); transitórios não persistidos |
| D6 Protocolo | Sim | ✔ | sequência; admissão por estado-por-tipo; capacidade×papel (computed_by≠writer_id; commit direto do produtor = DENY — M-05/N-03); consumo/emissão = [INFERÊNCIA]/[DECISÃO NECESSÁRIA] |
| D7 Teste | Sim (≥3) | ✔ | **T01..T19 (19)** — T18 (pai SMC-PRIMARY → DENY, A-04), T19 (school não derivável → DENY, A-04); T16 com caso positivo formulated_at<outcome (A-01); T09 com trajetória ACTIVE (A-02) |
| D8 Adversarial | Sim (focado) | ✔ | **ADV-CKG-01..23 (23)** — ADV-23 novo (proteção INV-02/RULE-HH-002 efetiva, não aparente — A-04); ADV-04 com contraste positivo (A-01); ADV-21 com TRAJECTORY_NEVER_ACTIVE (A-02); ADV-18 independe de ordem (A-11); ADV-08/09/10 reclassificados REVISÃO/spec-time (A-13) |
| D9 Auditoria | Por referência | Parcial | registro reconstruível; trace completo da Evidência; observabilidade agregada = SPEC-040 |

**PASS.**

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

13 BASpecs com QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR + CLASSE/MECANISMO. Classes: C (001,005,006,007,009,010,013), D (002,003,004,011,012), H (008 — bounded loop + gate de saída). Gates C/H determinísticos. CKG-008 (H) com gate que DERIVA `outcome_timestamp` do `recorded_at` do registro apontado (N-02). CKG-005/009 cobrem computed_by≠writer_id (commit direto do produtor = DENY — N-03), exercitado em T17/ADV-22. **PASS.**

---

## 3. Critérios EARS

13 critérios, cada um prefixado pela regra-fonte `(CKG-0NN)`. EARS 3/4/8/12 cobrem as mecânicas determinísticas (aciclicidade+self-loop N-07, janela inválida, outcome derivado/posthoc N-02, expected_version/fork com códigos de origem N-04) por referência à regra única. EARS-9 `(CKG-009/005)` cobre autorização E3 + commit direto do produtor DENY (N-03). **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 cobrem as 13 BASpecs |
| ENF-02 Nível ≥ piso | ✔ escrita + guard confiança×convicção = E3 (001/002/003/004/005); consulta = E1 (006) |
| ENF-03 Detector ≠ Gate | ✔ EC-003/005; juízo CKG-008 detector, gate determinístico (verifica carimbo DERIVADO, não veracidade) |
| ENF-04 Fail-closed | ✔ EC-001/002/003/005 |
| ENF-05 Policies não auto-aprendidas | ✔ [PROPOSTA] |
| ENF-06 E0 | N/A |
| ENF-07 E3 falso-DENY | ✔ EC-001/002/003/005 (amostral; CONDICIONAL até limiar) |
| ENF-08 Escala E0–E3 | ✔ atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12)

CC-01 (agnóstico; hypothesis.school≠ICT), CC-02 (não redefine; código `CANONICAL_CONTRACT_REDEFINITION_FORBIDDEN` — N-04), CC-03/04 (INV-04 = custo; confiança = regra local), CC-08 (Herança; MODIFIED = SÓ RULE-BB-004 reforçada — o antigo M-01 sobre CEM-001 l.494 foi RETIRADO por premissa falsa em v1.8/A-03; "a partir da admissão" é regra LOCAL CKG-010, não MODIFIED — N-04), CC-09 (H-001 INDETERMINADO; causal c/ mecanismo+regime+posthoc+desfecho derivado; núcleo causal imutável na cadeia — N-02), CC-10 (acepções; REFUTED só CHM — N-06 do parecer anterior), CC-11 (Classe por BASpec, incl. H) = PASS. CC-05/06/07/12 OK/N-A. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

INHERITS com ID+versão/linha verificados: **SPEC-004 RULE-CBP-004 (l.239-246 — compare-and-commit; VERSION_CONFLICT l.243 / EXPECTED_VERSION_REQUIRED l.243-244), RULE-CBP-007 (DEFINIÇÃO l.264-270 — a BASpec-CBP-007 fica em l.543-565; correção N-06), RULE-CBP-014 (l.311-319)**; CEM-001 (l.258-262 estados sem REFUTED, estado de validação = ACTIVE — N-01; l.264/428; l.473-475 transições proibidas; **l.494 = tabela "Consumo pelos Componentes", estados da EVIDÊNCIA — NÃO é obrigação sobre a hipótese; o antigo MODIFIED M-01 sobre essa linha foi RETIRADO por premissa falsa em v1.8/A-03**; l.562-565/l.608-615; l.602); CHM-001; CCM-001 (estados l.58/78; validação = COMPUTED/GATED_PASS — N-01); SPEC-001 (RULE-HH-001 l.97 produtores Elliott/SMC/Fibonacci; RULE-HH-002 l.100; RULE-HH-004 l.108; ADV-HH-01 l.515-520; AUTHORIZED_PRODUCERS l.524); SPEC-005 (transporta `Evidence.Invalidated` l.88/859); RULE-BB-004, RULE-CAU-01/02/03 (l.680-682), RULE-ONT-01/02 (l.671); atomic-spec §10.2 E3; INV-04/05/06/07/09/10. **MODIFIED = SÓ RULE-BB-004 reforçada (RULE-HD-02); M-01 RETIRADO (A-03) — a preservação "a partir da admissão" é regra LOCAL CKG-010, não MODIFIED de canônico (N-04).** SAS-001 §6.12 citado SÓ para "produtor registra, não redefine ontologia" — NÃO é fonte de `school`. REMOVED vazio. **PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001/M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 + **CKG-STRUCT-ORIGIN-001 (nova, N-01)** ABERTAS; SPEC-004/005 não reabertas; SPEC-007 não absorvida | ✔ |
| STRUCT-10: nenhuma forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta (grep dos IDs: 0 afirmações de fechamento) | ✔ |
| `school`/`hierarchy_role` DERIVADOS do produtor **SÓ para hypothesis** (N-01, opção (a) de Andraus); `structure` NÃO deriva school nem origina ORIGINA; SAS-001 §6.12 não é fonte de school; grep `structure.*school`/`school.*structure` no corpo normativo = só nota de exclusão/decisão | ✔ (N-01) |
| `school=Fractal` sem produtor em SPEC-001 → registrado [INFERÊNCIA]/[DECISÃO NECESSÁRIA], não inventado | ✔ (N-09) |
| Aciclicidade DERIVA_DE invertida + self-loop proibido; sem resíduo "destino já é ancestral transitivo" (grep=0) | ✔ (M-02/N-07) |
| Preservação de estados = "A PARTIR DA ADMISSÃO"; sem resíduo "TODOS os estados" (grep=0) | ✔ (M-01) |
| `computed_by` (produtor) ≠ `writer_id` (committer); sem resíduo "writer_id == computed_by" (grep=0); commit direto do produtor = DENY (T17/ADV-22) | ✔ (M-05/N-03) |
| CAUSA: `outcome_ref` obrigatório; `outcome_timestamp` DERIVADO do `recorded_at` do apontado (OUTCOME_TIMESTAMP_INVALID); no_outcome×outcome_ref (NO_OUTCOME_CONFLICT); posthoc determinístico | ✔ (M-04/N-02) |
| REFUTED só CHM; SUPERSEDED/ARCHIVED também na Evidência; sem resíduo "REFUTED/SUPERSEDED/ARCHIVED são do CHM" (grep=0) | ✔ (m-03/N-06) |
| SIMILAR_A exclui `conviction` na matriz | ✔ (m-07) |
| natural_key completo — **9 tipos** (asset/timeframe/regime/narrative/observation/learning/structure/mission/calibration_metric) | ✔ (N-05 — corrigido de "10") |
| Códigos de rejeição: todos em §D3.1 (incl. EXPECTED_VERSION_REQUIRED/VERSION_CONFLICT em vez de EXPECTED_VERSION_MISMATCH — N-04; OUTCOME_TIMESTAMP_INVALID/NO_OUTCOME_CONFLICT — N-02; CANONICAL_CONTRACT_REDEFINITION_FORBIDDEN — N-04); `EXPECTED_VERSION_MISMATCH` aparece 1x só na nota que diz que NÃO é código próprio (grep=1) | ✔ (N-02/N-04) |
| `collision` NÃO é mais `record_kind` de `relation_record` (é `collision_record` próprio); grep do enum de relation_record sem "collision" | ✔ (N-04) |
| Colisão INVALIDA×alvo = MARCAÇÃO não-destrutiva (não rejeição) + cond. (v) alvo ainda vigente; invalidação autorizada normal NÃO colide | ✔ (N-08) |
| Reconciliação INV-CKG-02 (buffer `PENDING_ANCESTOR` bounded) × RULE-CKG-003 (fail-closed): sem contradição; timeout = [DECISÃO NECESSÁRIA], sem número | ✔ (N-07) |
| "eventos consumidos" / "D6 consome" → [INFERÊNCIA]/[DECISÃO NECESSÁRIA]; sem afirmativo (grep=0) | ✔ (m-08) |
| SAS-001 §6.12 = FATO NORMATIVO só p/ Structural Agent; extensão = [INFERÊNCIA] | ✔ (m-02) |

**PASS (com itens explicitamente em aberto, não ✔).**

---

## 8. Verificação mecânica de citações (abri cada arquivo/linha)

| Citado | Confere? | Fonte |
|---|---|---|
| CEM-001 estados Evidência (sem REFUTED) | ✔ l.258-262 | canon/CEM-001-canonical-evidence-model.md |
| **CEM-001 estado de validação da Evidência = ACTIVE (único "vivo"; não há DOMINANT/REFUTED) — base do predicado de trajetória POR TIPO (N-01)** | ✔ l.258-262 | idem |
| CEM-001 transições proibidas → ACTIVE | ✔ l.473-475 | idem |
| CCM-001 estados conviction COMPUTED/GATED_PASS/GATED_BLOCK/SUPERSEDED | ✔ l.58/78 | canon/CCM-001-canonical-conviction-model.md |
| **CCM-001 validação da conviction = COMPUTED∨GATED_PASS (conviction NÃO tem ACTIVE) — base do predicado de trajetória POR TIPO (N-01)** | ✔ l.58/78 | idem |
| SPEC-004 RULE-CBP-004 (compare-and-commit; VERSION_CONFLICT l.243; EXPECTED_VERSION_REQUIRED l.243-244) | ✔ l.239-246 | specs/features/SPEC-004/plan.md |
| SPEC-004 **RULE-CBP-007 (DEFINIÇÃO)** | ✔ **l.264-270** (bloco BASpec-CBP-007 = **l.543-565**, fecho em l.565 — correção N-06) | specs/features/SPEC-004/plan.md |
| SPEC-001 RULE-HH-001 (produtores Elliott/SMC/Fibonacci; ICT/Fractal NÃO produzem hipótese); **RULE-HH-002 (só Elliott cria primária) — base de PRIMARY⇒Elliott (A-04)** | ✔ l.97; RULE-HH-002 l.100; RULE-HH-004 l.108; AUTHORIZED_PRODUCERS l.524 | specs/features/SPEC-001/plan.md |
| **KERNEL-V2 "uma Narrativa pode agregar múltiplas Hipóteses" — base [INFERÊNCIA] de DEPENDE_DE narrative→hypothesis (N-06)** | ✔ l.1500 ([EXTERNO]/DADO, não baseline — INV-09/TRACE-06) | docs/fundamentos/KERNEL-V2.md |
| Contagem: 13 BASpecs / 6 EC / 13 EARS / **19 cenários (T01..T19)** / **23 ADV (ADV-01..23)** | ✔ por grep de cabeçalhos (v1.9; recontar no ambiente pai) | plan.md |
| RULE-CKG-*; INV-CKG-01/02; §D2.1/§D2.2; campos locais; CKG-STRUCT-ORIGIN-001 | [PROPOSTA]/[DECISÃO NECESSÁRIA] | esta Spec |

Nenhuma citação de baseline sem conferência. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

Nenhum gatilho `spec:SPEC-006` isolado; satisfaz ramos de BL-003/BL-011; **BL-011 (MC-EXP-001) RECONCILIADO na v1.7** (seção "Reconciliação BL-011 / MC-EXP-001"): fila EXP-SPEC-001..053 + X-01/X-04/R-01..R-07 cruzados → memória semântica por REFERÊNCIA a RULE-CKG existentes (sem duplicar), memória episódica FORA (SPEC-007/018/K-001), COL-EXP-01..05 REFLETIDOS/ADIADOS; Disposição PARCIAL preservada; estado no painel inalterado (`Absorvido` é de Andraus); nenhuma regra nova. BL-010 tangente (SPEC-007); **BL-029 = `Em espera`**; **BL-035 (novo, `Em espera`) — CKG-STRUCT-ORIGIN-001** registrado pelo Especificador (RMR-001 §5), gatilho `decisao:CKG-STRUCT-ORIGIN-001 resolvida` ∨ `spec:SPEC-007 em redação` (não disparado); o Especificador NÃO promove. Passo 11-bis pleno na homologação. **PASS.**

---

## 10. RULE-ECC-04 / RULE-ECC-06 — presença

SRC-ZEP-01/PROV-01/MEMVSKG-01 verbatim em sources/; SRC-FORGET-01 = DADO não-verbatim. 4 repositórios elegíveis (régua Equilibrada); nenhum adotado. RULE-ECC-05 NÃO incide; WORKFLOW por prudência; não fecha WF-D03. **PASS (presença).**

---

## 11. Rastreabilidade — Maiores do parecer sobre a v1.4 (M-01..M-06) + m-01

Conferidos por grep cruzado (plan.md v1.6 **e** este checks.md; resíduo contraditório = 0 onde "Corrigido").

| Achado | Situação | Onde (plan.md) / evidência de grep |
|---|---|---|
| **m-01** falso-DENY/ENF-07 amostral declarado nos E3 | **Corrigido** (registrado — não estava listado antes) — EC-CKG-001/002/003/004/005 declaram "Falso-DENY E3 CONDICIONAL até limiar (ENF-07)"; limiar amostral = gap aberto (não ✔) | EC-CKG-001..005 FAILURE-MODE/EVIDENCE |
| **M-01** admissão exclui EMERGENT/CANDIDATE vs "TODOS os estados" | **Corrigido e depois RECLASSIFICADO (v1.8/A-03; mantido v1.9)** — a exclusão/preservação "a partir da admissão" é hoje **regra LOCAL CKG-010**, NÃO mais um MODIFIED de canônico: o antigo MODIFIED M-01 sobre CEM-001 l.494 foi RETIRADO por premissa falsa (l.494 = tabela Consumo, estados da EVIDÊNCIA). MODIFIED remanescente = SÓ RULE-BB-004 reforçada. schema `canonical_state_transition` diz "EMERGENT/CANDIDATE NÃO constam" | regra LOCAL CKG-010; schema; Herança/Delta (M-01 RETIRADO) |
| **M-02** aciclicidade invertida | **Corrigido** — rejeita se ORIGEM alcançável a partir do DESTINO; self-loop proibido (N-07); ADV-20 ciclo real | RULE-CKG-003; BASpec-003; D4; ADV-20 |
| **M-03** trace de hipótese sem gate → completude falsa | **Corrigido** — completude GARANTIDA só p/ EVIDÊNCIA; hipótese = [PROPOSTA] best-effort | RULE-CKG-011; D4; INV-CKG-02 |
| **M-04** pós-hoc contornável | **Corrigido** (reforçado por N-02) — `outcome_ref` obrigatório; `outcome_timestamp` DERIVADO | RULE-CKG-008; D4; §D3.1; T16; ADV-04 |
| **M-05** writer_id==computed_by | **Corrigido** (reforçado por N-03) — distintos; commit direto do produtor = DENY (T17/ADV-22); grep "writer_id == computed_by"=0 | RULE-CKG-005; D6 tabela; T17; ADV-22 |
| **M-06** `school` de structure; natural_key | **SUPERSEDIDO em parte por N-01** — a parte "`school` de structure" foi REMOVIDA (só hypothesis deriva school); a parte "natural_key completo (9 tipos)" permanece | §D2.1 nota; schema `natural_key`/`school` |

---

## 12. Rastreabilidade — Menores preservados (m-02..m-12)

(inalterados desde a v1.5, conferidos por grep onde marcados "Corrigido"; só os tocados pela Rodada 7 têm nota):

| Achado | Situação | Evidência |
|---|---|---|
| m-02 SAS-001 §6.12 | **Corrigido** (reforçado N-01: também deixa de ser fonte de school) | RULE-CKG-009; INHERITS |
| m-03 REFUTED só CHM | **Corrigido** (reforçado N-06: SUPERSEDED/ARCHIVED também na Evidência) | D5; INHERITS CEM-001 |
| m-04 códigos fora do §D3.1 | **Corrigido** (reforçado N-02/N-04: novos códigos todos em §D3.1) | §D3.1 |
| m-06 citações (CBP-004/ICT/expected_version) | **Corrigido** (N-04: EXPECTED_VERSION_REQUIRED/VERSION_CONFLICT; N-05: CBP-007 l.264-270) | Herança; CKG-012; §8 |
| m-07 SIMILAR_A | **Corrigido** — matriz exclui conviction | §D2.1 |
| m-08 eventos | **Corrigido** — [INFERÊNCIA]/[DECISÃO NECESSÁRIA] | D6 |
| m-09 INVALIDA→relação / valid_to nulo | **Corrigido** (reforçado N-08: cond.(v); N-04: `collision` fora do record_kind de relação) | schema; §D2.2; D4 |
| m-10 record_kind / versão | **Corrigido** (N-04: `collision` removido de `relation_record.record_kind`) | schema |
| m-11 histórico fora de ordem | **Corrigido** — changelog ordenado 1.0→1.9 | Histórico de versões |
| m-12 novas regras sem EARS/T/ADV | **Corrigido** — Rodada 7: N-02 (EARS-8/T16/ADV-04), N-03 (EARS-9/T17/ADV-22/ADV-21), N-04 (ADV-19/ADV-11), N-07 (BASpec-003/INV-CKG-02; self-loop = ADV-20 caso (c); o timeout da espera é [DECISÃO NECESSÁRIA], não testável), N-08 (ADV-18) | EARS; D7; D8 |

---

## 13. Observação de volume (consolidação)

O número exato de linhas é OMITIDO aqui (N-04) — conferir com `wc -l specs/features/SPEC-006/plan.md` no ambiente pai (o Especificador não tem Bash). A errata v1.9 cresce pouco: regra/predicado de N-01/N-02/N-05/N-06 definidos UMA vez e propagados por referência (sem BASpec/EARS/EC/T/ADV novos). A regra segue definida uma única vez (D2) e referenciada; a reconciliação mapeia por REFERÊNCIA, não cria regra. O alvo `<1100` NÃO foi atingido sem risco à cobertura (CRITICAL). **Dividir a Spec é decisão exclusiva de Andraus (Q-ABERTURA-5; F-17)** — não feito.

---

## 14. Rastreabilidade — Parecer sobre a v1.5 (N-01..N-09) — Rodada 7

| Achado (parecer) | Situação | Onde (plan.md) / evidência |
|---|---|---|
| **N-01 (Maior, opção (a) de Andraus)** `school`/`hierarchy_role` só hypothesis; remover derivação de school p/ structure; SAS-001 §6.12 não é fonte de school; ORIGINA só de hypothesis; `structure` não origina; [DECISÃO NECESSÁRIA] CKG-STRUCT-ORIGIN-001 + NOTA + BL-035 | **Corrigido** — §D2.1 nota; matriz ORIGINA; D4 integridade; schema `school`; §7-bis Bloco C; INHERITS SAS-001; bloco de decisões + Etiquetagem; BL-035 no RMR-001 (`Em espera`). grep `structure.*school` no corpo normativo = só notas de exclusão/decisão | §D2.1; matriz; D4; schema; §7-bis; decisões; `backlog/RMR-001` BL-035 |
| **N-02 (Menor)** `outcome_timestamp` do payload | **Corrigido** — DERIVADO do `recorded_at` do registro apontado por `outcome_ref` (OUTCOME_TIMESTAMP_INVALID); `no_outcome`+`outcome_ref` ⇒ NO_OUTCOME_CONFLICT; casos negativos em T16/ADV-04 | RULE-CKG-008; BASpec-008; D4; §D3.1; EARS-8; T16; ADV-04; schema causal; EC-005 |
| **N-03 (Menor)** falta EARS/T/ADV p/ computed_by≠writer_id; caso negativo conviction/evidence na admissão | **Corrigido** — EARS-9 `(CKG-009/005)`; **T17** + **ADV-22** (commit direto do produtor → DENY, capacidade×papel D6); ADV-21 estendido (admissão por tipo evidence DOMINANT / conviction EMERGENT) | EARS-9; T17; ADV-22; ADV-21; D6 tabela |
| **N-04 (Menor)** EXPECTED_VERSION_MISMATCH p/ ausência+divergência; `collision` em record_kind de relação; ADV-11 sem código p/ redefinição | **Corrigido** — EXPECTED_VERSION_REQUIRED (ausência) + VERSION_CONFLICT (divergência) dos códigos SPEC-004 l.243-244; `collision` removido de `relation_record.record_kind`; CANONICAL_CONTRACT_REDEFINITION_FORBIDDEN em §D3.1 e ADV-11 | RULE-CKG-012; §D3.1; D4; schema; ADV-19; ADV-11 |
| **N-05 (Menor)** checks: grep falso; "10 tipos"; CBP-007 l.543-558; falta m-01 | **Corrigido** — grep "EMERGENT|CANDIDATE|ACTIVE=0" removido (falso: ~15 ocorrências legítimas de EMERGENT em prosa de exclusão; o correto é "schema `canonical_state_transition` diz 'EMERGENT/CANDIDATE NÃO constam'"); natural_key = **9 tipos**; CBP-007 = **l.264-270** (bloco BASpec l.543-565 — fecho em l.565, corrigido definitivamente em N-06); **m-01 adicionado** ao §11; afirmações de grep reais | este checks §0/§1/§6/§7/§8/§11 |
| **N-06 (Menor)** SUPERSEDED/ARCHIVED atribuídos ao CHM como exclusivos | **Corrigido** — REFUTED EXCLUSIVO do CHM; SUPERSEDED/ARCHIVED também na Evidência (CEM-001 l.258-262); grep "REFUTED/SUPERSEDED/ARCHIVED são do CHM"=0 | INHERITS CHM-001 §4.2 (estados da hipótese); CEM-001 l.258-262; D5 (fronteira) — A-09: âncora "CHM-001 l.86" (irrelevante) corrigida |
| **N-07 (Menor)** INV-CKG-02 (buffer aguarda) × CKG-003 (fail-closed); self-loop | **Corrigido** — reconciliados (espera BOUNDED em buffer; esgotado ⇒ fail-closed `DERIVA_DE_EDGE_MISSING`); timeout = **[DECISÃO NECESSÁRIA]** (sem número); self-loop proibido (`LINEAGE_CYCLE`) | RULE-CKG-003; INV-CKG-02; BASpec-003; D4; decisões + Etiquetagem |
| **N-08 (Menor)** INVALIDA×alvo colide por construção | **Corrigido** — colisão = MARCAÇÃO não-destrutiva (preserva ambas, não rejeita); cond. (v): só colide se o alvo PERMANECE VIGENTE; invalidação autorizada que fecha o alvo NÃO colide; ADV-18 caso (f) | §D2.2; RULE-CKG-013; BASpec-013; D4; D6 passo 7; ADV-18 |
| **N-09 (Menor)** enum `school` sem Fractal | **Corrigido** — sem produtor de hipótese Fractal em SPEC-001 (`AUTHORIZED_PRODUCERS`=Elliott/SMC/Fibonacci); `school=Fractal` sem fonte registrado [INFERÊNCIA]/[DECISÃO NECESSÁRIA] (CKG-STRUCT-ORIGIN-001), não inventado | §D2.1 nota; schema `school`; decisões/BL-035 |

---

## 15. Errata v1.8 — A-01..A-14 (auditoria independente §3) — status REAL + assertivas executáveis

> **Honestidade (seja honesto):** status = Corrigido / Parcial / Não corrigido. Cada linha traz ≥1 assertiva executável
> (`assert-present:"..."` / `assert-absent:"..."` em plan.md; o gate `scripts/gate_extra.py` as executa com espaços
> colapsados). As assertivas foram conferidas por grep no plan.md v1.8. As decisões conservadoras e os [DECISÃO NECESSÁRIA]
> remanescentes estão anotados.

| Achado | Sev. | Status | Assertiva executável (plan.md) | Nota |
|---|---|---|---|---|
| **A-01** pós-hoc por instante de FORMULAÇÃO | Maior | **Corrigido** | assert-present:"baseline do marcador pós-hoc" · assert-present:"CONTRASTE POSITIVO" · assert-absent:"[recorded_at>outcome_timestamp ⇒ posthoc_flag==true]" | `formulated_at` (1ª versão supersedes/hipótese) substitui `recorded_at` corrente em RULE-CKG-008/EARS-8/BASpec-008/D4/schema/T16/ADV-04/EC-005; T16(e)/ADV-04(f) = causa formulada ANTES do desfecho ACEITA (não pós-hoc) |
| **A-02** admissão por TRAJETÓRIA | Maior | **Corrigido (opção conservadora)** | assert-present:"Admissão por TRAJETÓRIA [A-02]" · assert-present:"TRAJECTORY_NEVER_ACTIVE" | Admite só objeto que ESTEVE em ACTIVE; EMERGENT→ARCHIVED (nunca validada) REJEITADA (T09/ADV-21(e)). **[DECISÃO NECESSÁRIA]:** conhecimento negativo (REFUTED/ARCHIVED de trabalho) = de Andraus |
| **A-03** retirar MODIFIED falso sobre CEM-001 l.494 | Maior | **Corrigido** | assert-present:"RETIRADO por premissa falsa" · assert-absent:"ESPECIALIZADA no KG para" | l.494 = tabela Consumo (estados da EVIDÊNCIA); preservação "a partir da admissão" vira regra LOCAL CKG-010; MODIFIED = só RULE-BB-004 reforçada |
| **A-04** RULE-CKG-001 fail-closed de hypothesis | Maior | **Corrigido** | assert-present:"PRIMARY_NOT_ELLIOTT" · assert-present:"HYPOTHESIS_VIA_SEAL_FORBIDDEN" · assert-present:"SCHOOL_NOT_DERIVABLE" | canonical_ref≠null ∧ producer∈AUTHORIZED_PRODUCERS ∧ school derivável ∧ PRIMARY⇒Elliott ∧ ¬via selo (b); T18/T19/ADV-23 |
| **A-05** H-001 sem dono (governança) | Maior | **Registrado (nota) — não resolvido aqui** | assert-present:"Nota A-05 (governança" | Re-apontamento da dona de H-001 (ROADMAP §6/atomic-spec §12/revisor.md §8) = decisão de Andraus; errata NÃO escolhe dona nem edita esses docs |
| **A-06** CBP-007 l.543-558 → l.264-270 | Menor | **Corrigido (extensão do bloco refinada em N-06 — l.543-565)** | assert-present:"RULE-CBP-007 l.264-270" · assert-absent:"RULE-CBP-007 l.543-558" | 5 ocorrências trocadas; bloco BASpec-CBP-007 vai de l.543 a l.565 (verificado no SPEC-004) |
| **A-07** RMR-001 por LINHA → por ID/âncora | Menor | **Corrigido** | assert-absent:"RMR-001 l.128" · assert-present:"por ID/âncora" | BL-029 + nota DHR-SPEC006-PEND-001 citados por ID |
| **A-08** "research.md §8 R-8" → ABERTURA §10 | Menor | **Corrigido** | assert-present:"ABERTURA.md §10 R-8" · assert-absent:"research.md §8 R-8" | R-8 confirmado em ABERTURA.md §10 (Riscos) l.149 |
| **A-09** âncoras trocadas | Menor | **Corrigido** | assert-present:"CEM-001 l.602/l.606" · assert-present:"ONT-02 (ontologia extensível por governança — l.672" | RULES ONT-01 l.671/ONT-02 l.672; CONSTITUTION l.191/192; SPEC-005 l.971; CEM-001 l.606; checks N-06 "CHM-001 l.86" corrigido |
| **A-10** chave natural da relação | Menor | **Corrigido** | assert-present:"target_relation_id, valid_from" | INVALIDA (to_node=null) não colapsa |
| **A-11** ordem INVALIDA × valid_to | Menor | **Corrigido** | assert-present:"MESMO ATO ATÔMICO" | par atômico; cond.(v) sobre estado resultante; independe de ordem (RULE-CKG-013/D6/ADV-18) |
| **A-12** tipos de nó sem relação | Menor | **Corrigido (conservador)** | assert-present:"NENHUMA aresta PARA conviction" | conviction/narrative ganham DEPENDE_DE de SAÍDA (NENHUMA aresta PARA conviction — INV-04); calibration_metric = isolamento intencional [PROPOSTA] |
| **A-13** VERIFICADO POR não executável (ADV-08/09/10, BASpec-009) | Menor | **Corrigido** | assert-present:"CHECAGEM DE REVISÃO/SPEC-TIME — A-13" | ADV-08/09/10 reclassificados spec-time; falso-DENY removido do desfecho de BASpec-009 |
| **A-14** EC-004 (E3) × EC-006 (E1) | Menor | **Corrigido** | assert-present:"distinto do guard de ESCRITA E3" | guard de ESCRITA = E3 (EC-004); guard de LEITURA = E1 (EC-006) |

**[DECISÃO NECESSÁRIA] remanescentes (não fechadas — CONS-01):** H-001 (mecanismo físico + A-05 dona); conhecimento negativo na admissão (A-02 alternativa); CKG-STRUCT-ORIGIN-001 (N-01/N-09, BL-035); timeout `PENDING_ANCESTOR` (N-07); selo SPEC-007; allowlist/host do juízo; migração de ontologia; escala de confiança; M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001.

---

## 16. Errata v1.9 — N-01..N-06 (parecer do Revisor sobre a v1.8) — status REAL + assertivas executáveis

> **Honestidade:** status = Corrigido / Parcial / Não corrigido. Cada linha traz ≥1 assertiva executável
> (`assert-present:"..."` / `assert-absent:"..."` em plan.md; o gate do ambiente pai as executa com espaços colapsados).
> As assertivas foram conferidas por grep no plan.md v1.9. **Regra definida UMA vez; demais seções referenciam por ID**
> (N-01 em RULE-CKG-010; N-02 em RULE-CKG-008; N-05 em RULE-CKG-013; N-06 na matriz §D2.1). **O Especificador NÃO tem Bash
> — NÃO declara gates rodados; a execução (`validate_spec_sot.py`, `revisor_gate.py`, `check_doc_sync.py`, `build_map.py --check`,
> `wc -l`) é do ambiente pai.**

| Achado | Sev. | Status | Assertiva executável (plan.md) | Nota (escolha conservadora) |
|---|---|---|---|---|
| **N-01** predicado de trajetória por tipo + origem da prova | Média | **Corrigido** | assert-present:"predicado POR TIPO [N-01]" · assert-present:"CANONICAL_HISTORY_UNRESOLVABLE" · assert-present:"canonical_history_ref" | RULE-CKG-010 (fonte única): hypothesis ACTIVE∨DOMINANT; evidence ACTIVE (CEM-001 l.258-262); conviction COMPUTED∨GATED_PASS (CCM-001 l.58/78). Prova da trajetória = `canonical_history_ref` (campo do node_record) resolvido NO CANÔNICO, nunca do payload; ausência ⇒ `CANONICAL_HISTORY_UNRESOLVABLE`. Propagado por ID a EARS-10/BASpec-010/D4/D6 passo 2/schema. T09 positivo por tipo; ADV-21 negativo por tipo (f/g/h). |
| **N-02** `formulated_at` — reescrita pós-hoc e alternativa frágil | Média | **Corrigido (opção mais conservadora: PROIBIR + REMOVER)** | assert-present:"CAUSAL_CORE_IMMUTABLE_IN_CHAIN" · assert-present:"foi REMOVIDA [N-02]" | RULE-CKG-008: (1) sucessora que ALTERA mechanism/direction/conditions/regime é REJEITADA (`CAUSAL_CORE_IMMUTABLE_IN_CHAIN`) — corrigir o núcleo exige NOVA CAUSA com `formulated_at` próprio (fecha a racionalização pós-hoc por reescrita, RULES.md l.682); (2) alternativa "`recorded_at` da hipótese referenciada" REMOVIDA (sem campo/precedência; permitia antedatar). ADV-04 caso (g) = cenário negativo da sucessora reescrita. |
| **N-03** propagação incompleta da errata v1.8 | Menor | **Corrigido** | assert-present:"fail-closed A-04: canonical_ref≠null" · assert-present:"admissão POSITIVA por tipo — N-01" | Alinhados por referência: BASpec-CKG-001 (ENTÃO/MECANISMO/GATE/VERIFICADO POR com fail-closed A-04), EARS-1, EC-CKG-001 PRECOND; BASpec-CKG-010/EARS-10/D4/D6 passo 2 (trajetória por tipo). Autopré-check corrigido: T09 é só o POSITIVO; `TRAJECTORY_NEVER_ACTIVE`/`CANONICAL_HISTORY_UNRESOLVABLE` ficam em ADV-21. |
| **N-04** checks tratavam MODIFIED retirado como vigente; linha-conta; §8 | Menor | **Corrigido** (neste checks) | assert-present:"M-01 RETIRADO na errata v1.8 — A-03" (prova no plan de que o MODIFIED foi retirado) | §5/§6/§11 reescritos: MODIFIED = SÓ RULE-BB-004 reforçada; M-01 RETIRADO (A-03); "a partir da admissão" é regra LOCAL CKG-010; l.494 = tabela Consumo (estados da EVIDÊNCIA). §0/§13: número de linhas OMITIDO (conferir `wc -l` no pai). §8: citações novas de N-01 (CEM l.258-262 ACTIVE; CCM l.58/78 COMPUTED/GATED_PASS) e N-06 (CBP-007 l.543-565; KERNEL-V2 l.1500) listadas. |
| **N-05** A-11 atomicidade × colisão (v) | Menor | **Corrigido (conservador: ADMITIR+MARCAR, não rejeitar)** | assert-present:"Dois modos de INVALIDA [N-05]" · assert-present:"INVALIDA CONTESTADA/PENDENTE" | RULE-CKG-013 desambigua: INVALIDA AUTORIZADA (fecha `valid_to` no mesmo ato atômico ⇒ não colide) vs INVALIDA CONTESTADA/PENDENTE (sem fechamento ⇒ ADMITIDA e preservada, N-08; alvo vigente ⇒ cond. (v) alcançável ⇒ `collision_record`). A rejeição foi DESCARTADA por contrariar N-08 (o KG preserva, não rejeita). Alinhado em D6 passo 7 e ADV-18 (d)=contestado, (f)=autorizado. |
| **N-06** matriz DEPENDE_DE sem pares; citação CBP-007 | Menor | **Corrigido** | assert-present:"Pares admitidos de DEPENDE_DE [N-06]" · assert-present:"l.543-565" | Pares declarados: (hypothesis\|mission)→(hypothesis\|evidence); conviction→(evidence\|hypothesis) [só SAÍDA; nenhuma PARA conviction — INV-04]; narrative→(evidence\|hypothesis) [narrative→hypothesis "agrega" = KERNEL-V2 l.1500, etiquetado [INFERÊNCIA] sobre fonte [EXTERNO]]. Citação BASpec-CBP-007 corrigida l.543-559→l.543-565 (fecho em l.565 — verificado no SPEC-004). |

**[DECISÃO NECESSÁRIA] remanescentes (não fechadas — CONS-01):** inalteradas desde v1.8 — H-001 (mecanismo físico + A-05 dona); conhecimento negativo na admissão (A-02 alternativa); CKG-STRUCT-ORIGIN-001 (BL-035); timeout `PENDING_ANCESTOR` (N-07 da rodada anterior); selo SPEC-007; allowlist/host do juízo; migração de ontologia; escala de confiança; M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001. **Nenhuma decisão aberta foi tocada; H-001 permanece ABERTA.**

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness) na v1.9 (ERRATA N-01..N-06 do parecer do Revisor sobre a v1.8). 13 BASpecs (D/C/H), 13 EARS (referenciando regra-fonte), 6 EC (escrita = E3 / leitura = E1 separados — A-14), §D2.1/§D2.2 (cond. (v) — N-08; dois modos de INVALIDA — N-05)/§D3.1 (códigos novos `CANONICAL_HISTORY_UNRESOLVABLE`/`CAUSAL_CORE_IMMUTABLE_IN_CHAIN`), INV-CKG-01/02, proveniência condicional, CKG-010 TRAJETÓRIA POR TIPO + `canonical_history_ref` (A-02/N-01) [PROPOSTA], **19 cenários (T01..T19)**, **23 adversariais (ADV-01..23)** (contagens declaradas; recontar cabeçalhos no ambiente pai: 13 BASpec/13 EARS/6 EC/19 T/23 ADV — N-01..N-06 são aditivos POR REFERÊNCIA, sem BASpec/EARS/EC/T/ADV novos). v1.7 acrescentou a **Reconciliação BL-011 / MC-EXP-001** (seção curta, sem regra nova). CONS-01 preservado (H-001, J-001, K-001, M-001, N-001, G-001, CKG-STRUCT-ORIGIN-001 e demais ABERTAS; nenhuma fechada), gate RMR-001 (BL-011 reconciliado, Disposição PARCIAL, estado inalterado; BL-029/BL-035 `Em espera`). N-01..N-06 em §16 com assertivas executáveis (conferidas por grep no plan.md v1.9).

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: gates no ambiente pai (Especificador sem Bash) — `validate_spec_sot.py`, `revisor_gate.py`, `check_repo_research.py --all`, `check_doc_sync.py`, `backlog_triggers.py`, `check_invariants.py`, `build_map.py --check` — e submissão ao Revisor SOT.
