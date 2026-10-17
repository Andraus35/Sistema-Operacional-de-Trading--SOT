# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.5 (candidato — rodada 6)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico de armazenamento INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-17 (Rodada 6 — Plan devolvido ao Especificador por ordem de Andraus, chat 2026-10-17, após o parecer NÃO CONFORME da rodada 5, `parecer-revisor-rodada5.md`)

> **Nota de método:** cada item abaixo foi conferido abrindo o plan.md v1.5 e a fonte citada (arquivo:linha). Nenhum validador foi executado pelo Especificador (sem Bash) — ver §12 (comandos que o Orquestrador deve rodar).
> **Limitação funcional declarada (v1.5):** com (a), selo (b), (c), nós de referência e allowlist pendentes, o KG hoje **não admite nenhuma escrita** (plan §D2.3, l.524-538). O que é verificável são **predicados de gate e fixtures**; a admissão positiva fim a fim é **INDETERMINADO**.
> **Itens em aberto (não marcados ✔):** H-001; contrato do selo (SPEC-007); critério/produtor/gatilho do caminho (a); contrato do caminho (c); caminho dos nós asset/timeframe/regime/observation/calibration_metric/structure/narrative/mission; mantenedor da allowlist; host do juízo CKG-008; `producer_id` de SMC/Fibonacci/ICT e mapeamento →Fractal; consumidor de eventos; emissão pelo KG; migração de ontologia; escala de confiança; limiar/amostra de falso-DENY (ENF-07); reconciliação COL-EXP-05.

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — alvo ROADMAP §6; CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; memória permanente ≠ trabalho; mecanismo físico INDETERMINADO) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals; S10 aponta a tabela única §D2.3 |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA]; §D2.1 matriz; §D2.2 colisão (só CONFIRMA×REFUTA); **§D2.3 caminhos de entrada (novo)**; INV-CKG-01/02 |
| D3 Comportamento (BASpec) | Sim | ✔ | CKG-001..013 com CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | `envelope_completo` (definição única); `version`/`supersedes` por record_kind; log `kg_gate_decision`; bitemporal com `valid_to_efetivo`; **`estado(v,T)` com precedência**; trace; dedupe; gate causal/similaridade (toda CAUSA/SIMILAR_A); bounded loop (≤1 invocação); guard CKG-007 por node_type; colisão; fronteira por caminho; elos de versão + legalidade; ancestrais sem espera |
| D5 Estado | Sim | ✔ | `knowledge_state` = projeção (D4 `estado(v,T)`); transitórios CANDIDATE_WRITE / REJECTED (`PENDING_ANCESTOR` eliminado) |
| D6 Protocolo | Sim | ✔ | Passos 1–10 (+5-bis, 5-ter); passo 2 por caminho §D2.3; passo 3 com allowlist |
| D7 Teste | Sim (CRITICAL; ≥3) | ✔ | **T01..T20 (20)** + convenção (i)–(iv) |
| D8 Adversarial | Sim (CRITICAL, focado) | ✔ | **ADV-CKG-01..22 (22)** |
| D9 Auditoria | Por referência | Parcial | `envelope_completo` + `kg_gate_decision`; replay (T17); observabilidade agregada = SPEC-040; sem digest (limite m3) |

**Resultado:** profundidade-alvo D0–D7 atingida; D8 focado. **PASS (estrutural).**

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REF | VERIF. | CLASSE | Gate/bounded |
|---|---|---|---|---|---|---|---|
| CKG-001 ontologia + matriz + regras de nó | ✔ | ✔ | ✔ | ✔ | ✔ (= T01, predicado) | C | gate ✔ |
| CKG-002 ref canônica + estados + **versões** + legalidade | ✔ | ✔ | ✔ | ✔ | ✔ predicado/fixture; ponta-a-ponta INDETERMINADO | D | N/A |
| CKG-003 relação tipada/proveniência/DERIVA_DE | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-004 temporalidade | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-005 proveniência CONDICIONAL | ✔ | ✔ | ✔ | ✔ | ✔ (predicado) | C | gate ✔ |
| CKG-006 imutabilidade/envelope (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-007 guard confiança≠convicção (por node_type/campo) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ (limite: texto livre) |
| CKG-008 toda CAUSA/SIMILAR_A | ✔ | ✔ | ✔ | ✔ | ✔ | H | ≤1 invocação/submissão; KG sem retry ✔ + gate ✔ |
| CKG-009 governança (E3; allowlist) | ✔ | ✔ | ✔ | ✔ | ✔ (predicado) | C | gate ✔ |
| CKG-010 fronteira (§D2.3) | ✔ | ✔ | ✔ | ✔ | ✔ só os DENY; admissão positiva **INDETERMINADO** | C | gate = DENY por pendência |
| CKG-011 consulta/trace | ✔ | ✔ | ✔ | ✔ | ✔ (fixture) | D | N/A |
| CKG-012 lifecycle (`estado(v,T)`) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-013 colisão | ✔ | ✔ | ✔ | ✔ | ✔ (fixture, convenção (iv)) | C | gate ✔ |

**PASS (nenhuma admissão positiva marcada como verificável).**

---

## 3. Critérios EARS

**15 critérios** (13 → 15). Alterados na v1.5: **EARS 7** (guard por node_type/campo), **EARS 8** (escopo = toda CAUSA/SIMILAR_A; ≤1 invocação; KG sem retry), **EARS 9** (allowlist indefinida ⇒ rejeitar), **EARS 10** (selo sem contrato ⇒ rejeitar; "estados e versões"); **novos EARS 14** (`ENTRY_PATH_UNDEFINED`) e **EARS 15** (`SCHOOL_UNDERIVABLE`), cobertos negativamente por **T20**. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 |
| ENF-02 Nível ≥ piso | ✔ E3 em 001..005 (atomic-spec l.238); E1 em 006 |
| ENF-03 Detector ≠ Gate | ✔ juízo CKG-008 detector; guard CKG-007 por campo/node_type (sem juízo); gates de presença declaram o limite (m5) |
| ENF-04 Fail-closed | ✔ pendência = precondição não satisfeita ⇒ DENY em **(a), (b), (c), nós sem caminho e allowlist** (EC-001/003) |
| ENF-05 Policies não auto-aprendidas | ✔ limite do bounded loop versionado com a RULE |
| ENF-06 E0 | N/A |
| ENF-07 E3 falso-DENY | ✔ método amostral sobre `kg_gate_decision`; limiar = gap aberto (atomic-spec l.273/l.393) — CONDICIONAL; DENY por pendência ≠ falso-DENY |
| ENF-08 Escala E0–E3 | ✔ |

**PASS (ENF-07 com gap aberto declarado).**

---

## 5. Constitution Check (CC-01..CC-12)

CC-01 (5 camadas; `hypothesis.school ≠ ICT`; PRIMARY ⇒ Elliott; hoje só Elliott tem `producer_id` conhecido ⇒ demais `SCHOOL_UNDERIVABLE`), CC-02 (não redefine; elos de versão ESPELHAM `previous_version_id`; legalidade lida dos grafos canônicos, não redefinida; CCM sem tabela ⇒ espelho sem validação), CC-08 (três obrigações herdadas com evidência PARCIAL/[DECISÃO NECESSÁRIA] explícita: "todos os estados", "todas as versões", CEE-001 l.111), CC-09 (nenhum INDETERMINADO convertido em PASS — inclusive selo e allowlist), CC-10, CC-11 = PASS. CC-03/04 (INV-04; guard CKG-007 por campo). CC-05/06/07/12 OK/N-A. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

INHERITS reconferido na v1.5 (abri cada linha): CEM-001 l.428 (Status único mutável; registrar timestamp/origem/justificativa), l.450 (SUPERSEDED "Referencia a Evidência sucessora"), l.460-475 (transições permitidas/proibidas), l.494, l.530/544/560 (Lineage: antecedentes diretos; imutável), l.562-578, l.594-595 (relação entre versões explícita), l.602, l.608-615; CHM-001 l.283/588 (`previous_version_id`), l.744-757 (grafo de transições), l.767-769 (terminais); CCM-001 l.58 (`previous_version_id`; sem tabela de transições — grep "transi" só em l.125, governança); CEE-001 l.111; SAS-001 l.924; SPEC-001 l.203; CONSTITUTION l.191-192. REMOVED vazio; MODIFIED = só RULE-BB-004 reforçada. **PASS com evidência PARCIAL declarada (C1/C2).**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001 NÃO decidida; Opção B ADIADA | ✔ |
| Proveniência condicional: a REGRA está só em RULE-CKG-005 (l.337-346); BASpec-CKG-005, D6 passo 5, contrato/schema e T12/T14/T16 a **referenciam** (não repetem); `gate_record` = só objeto que RESULTA de gate (a montante ou detector CKG-013); gates de admissão do KG → `kg_gate_decision` | ✔ (M8) — a frase da v1.4 "idêntica em todas as representações" era falsa (EC-002/003 exigiam `gate_record` do próprio KG); corrigido |
| Formatos de registro: **dois, com papéis distintos e declarados** — `kg_record` (conhecimento; `envelope_completo`, D4 l.893) e `kg_gate_decision` (decisões PASS/DENY/INDETERMINADO, D4 l.895; schema l.1350). Um só formato de COLISÃO (dentro do `kg_record`) | ✔ (M8) — a frase da v1.4 "um só formato" estava errada para DENY/bounded loop; corrigida |
| `envelope_completo` definido UMA vez (D4 l.893) e referenciado por RULE-CKG-006, BASpec-CKG-013, D6 passo 8, D9, contrato, schema, EC-001/002, T17 | ✔ (M8) — inclui `publication.origin`, `valid_from` (creation), `valid_to` (invalidation), `gate_record`/`lineage` condicionais |
| Caminhos de entrada: fonte única §D2.3 (l.524-538) referenciada por RULE-CKG-010, BASpec-CKG-010, D4 l.905, D6 passo 2, EC-001, EARS 10/14, T09/T20, ADV-21, Blocos A/B, etiquetagem | ✔ (M1/M2) |
| Escopo de CKG-008 = TODA CAUSA/SIMILAR_A em RULE (l.375), BASpec (QUANDO), EARS 8, D4, D6 passo 6, EC-005 EFFECT | ✔ (M5) |
| Bounded loop sem memoização em RULE/BASpec/D4 l.901/EC-005/ADV-20 | ✔ (M6) |
| `PENDING_ANCESTOR`/"lote" eliminados de INV-CKG-02, D4, D5, D6, contrato, T19 | ✔ (M7) — grep "lote" só no texto que declara a eliminação |
| Guard CKG-007 por campo/node_type em RULE, matriz, BASpec, EARS 7, D4 l.902, schema (`_sem_confianca`), EC-004, T06, ADV-05 | ✔ (M9) |
| Projeção `estado(v,T)` (D4 l.897) referenciada por RULE-CKG-012, D5, EC-002, T17 | ✔ (M10) |
| M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 ABERTAS; SPEC-004/005 não reabertas; SPEC-007 não absorvida | ✔ |
| STRUCT-10 (nenhuma forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta) | conferência manual ✔ — busca devolve só falsos-positivos de substring (CHM-001/CEM-001 contêm "M-001"; EC-CKG-001 contém "G-001"), já presentes na v1.4 que passou no gate; o qualificador do critério mínimo de (a) foi reescrito como "(sem decisão de Andraus)" — **confirmar com o gate (§12)** |

**PASS (com itens explicitamente em aberto, não marcados ✔).**

---

## 8. Verificação mecânica de citações (abri cada arquivo/linha nesta rodada)

| Citado | Diz o afirmado? | Fonte verificada |
|---|---|---|
| "preservar todas as versões" / relação entre versões explícita / sucessora referenciada | ✔ | canon/CEM-001 l.612; l.594-595; l.450 |
| Transições permitidas/proibidas da Evidência | ✔ | canon/CEM-001 l.460-475 |
| `previous_version_id` (hipótese; toda nova versão referencia a anterior) | ✔ | canon/CHM-001 l.283; l.588 |
| Grafo de transições e terminalidade da hipótese | ✔ | canon/CHM-001 l.744-757; l.767-769 |
| CCM-001 `previous_version_id`; sem tabela de transições | ✔ | canon/CCM-001 l.58 (grep "transi" sem tabela) |
| Métrica de calibração "entra no Knowledge Graph" | ✔ | canon/CEE-001 l.111 |
| Produtor registra relações; não redefine ontologia | ✔ | canon/SAS-001 l.924 |
| `producer_id == "elliott_specialist"` | ✔ | specs/features/SPEC-001/plan.md l.203 |
| Workspaces Observations × Evidence | ✔ (sustenta só a distinção; a restrição CONFIRMA/REFUTA ⇒ evidence é [PROPOSTA] derivada de INV-06 — m1) | governance/CONSTITUTION.md l.191-192 |
| Bounded loop "uma passada … undetermined" | ✔ | SPEC-002 plan l.370-371; SPEC-003 plan l.387-388 |
| atomic-spec bounded loop obrigatório em H/P | ✔ | atomic-spec.md l.315 |
| Lineage = antecedentes diretos; imutável após publicação | ✔ | canon/CEM-001 l.530; l.560 |
| DHR-BACKLOG-001 | **NÃO localizada** neste checkout (grep sem ocorrências) — citada como comunicada pelo Orquestrador | — |
| Contagens (ver §11) | ✔ por busca de cabeçalhos | plan.md |

**PASS** (com DHR-BACKLOG-001 a confirmar pelo Orquestrador).

---

## 9. Gate RMR-001 (passo 11-bis)

- BL-003/BL-011: gatilho `spec:SPEC-006 em redação` disparado; promoção a `ATIVADO` **decidida por Andraus** (ata DHR-BACKLOG-001, comunicada pelo Orquestrador; não presente neste checkout). O Plan registra o tratamento (plan l.42-44) e **não** reabre/edita o RMR-001. Neste checkout o RMR-001 ainda mostra `Em espera` (l.102/l.110) — a sincronização é do Orquestrador (`backlog_triggers.py`).
- BL-010 tangente (SPEC-007); BL-029 `Em espera`, independente. COL-EXP-05 adiada ([DECISÃO NECESSÁRIA]).

---

## 10. RULE-ECC-04 / RULE-ECC-06 — presença

Sem pesquisa web nova nesta rodada (correções internas, ancoradas em baselines do repositório). SRC-ZEP-01/PROV-01/MEMVSKG-01 verbatim em sources/; SRC-FORGET-01 DADO não-verbatim; 4 repositórios elegíveis, nenhum adotado; RULE-ECC-05 não incide. **PASS (presença).**

---

## 11. Rastreabilidade da Rodada 6 (parecer da rodada 5) — linhas do plan.md v1.5

| Item | Procede? | Correção |
|---|---|---|
| **C1** "todas as versões" sem mecanismo | Sim | `canonical_predecessor_ref` + `successor_ref` (gate `VERSION_LINK_MISSING`): BASpec-CKG-002 l.601-607; D4 l.906; D6 5-ter l.960; schema l.1317/l.1340; contrato (linha "Transição canônica / versões"); T17 l.1123-1135 (`version_chain`); ADV-19(d) l.1228-1229; Bloco B l.1532 = **PARCIAL/[DECISÃO NECESSÁRIA]** |
| **C2** CEE-001 l.111 mapeada a ADV-05 | Sim | INHERITS l.113-115 (não "ARMAZENA"); ADV-05 l.1186-1187 (ENTÃO só isolamento; armazenamento não demonstrado); Bloco B l.1541 = **PARCIAL/[DECISÃO NECESSÁRIA]** |
| **M1** (b) e allowlist vacuosos | Sim | `SEAL_CONTRACT_UNDEFINED` (RULE-CKG-010 l.402-412; §D2.3; BASpec-CKG-010; T09); `WRITER_ALLOWLIST_UNDEFINED` (RULE-CKG-009 l.398-399; BASpec-CKG-009 GATE; EC-003 PRECOND l.1392; T20 d); "Consequência declarada" l.536-538; Bloco A cobertura l.1522-1525 |
| **M2** caminho de relações e node_types | Sim | §D2.3 l.524-538 (relações espelhadas por (a); relações de produtor e demais = (c); structure/narrative/mission sem caminho); convenção (iv) l.978-980; T11/ADV-02/ADV-18 por fixture |
| **M3** sem EARS/cenário para `ENTRY_PATH_UNDEFINED`/`SCHOOL_UNDERIVABLE` | Sim | EARS 14/15 l.557-558; T20 l.1156-1165; "Efeito hoje" l.449-451 (só Elliott conhecido) |
| **M4** INVALIDA × relação-alvo | Sim | linha removida da §D2.2 (l.518-522); INVALIDA na matriz l.477 ("afirmação"; ≠ registro `invalidation`); schema `contradiction_pair`; ADV-18(d) |
| **M5** escopo de CKG-008 | Sim | "toda CAUSA/SIMILAR_A, qualquer produtor": RULE l.375-377; BASpec QUANDO; EARS 8; D4; D6 passo 6 l.961; EC-005 EFFECT |
| **M6** memoização sem lastro | Sim (precedentes não têm cache) | memoização removida (RULE l.381-386; BASpec BOUNDED LOOP; D4 l.901; EC-005); ADV-20 l.1231-1232 reescrito (≤1 invocação, `kg_generated_retries == 0`, frequência de produtor fora do KG) |
| **M7** "lote" indefinido | Sim | conceito eliminado: INV-CKG-02 l.500-505 (rejeição imediata; sem espera; hoje inalcançável); D4 l.907; D5; D6 5-bis l.959; T19 l.1147-1154 por fixture |
| **M8** envelope/`gate_record` divergentes | Sim | `envelope_completo` único (D4 l.893); `gate_record` só p/ objeto que resulta de gate (RULE-CKG-005 l.339-343); `kg_gate_decision` (D4 l.895; schema l.1350); EC-002/003 EVIDENCE → `kg_gate_decision`; §7 acima corrigido |
| **M9** guard custo/confiança não determinístico | Sim | por node_type/campo: RULE-CKG-007 l.361-366 (+ limite); matriz CAUSA; D4 l.902; schema `_sem_confianca`; EC-004 PRECOND l.1404; T06; ADV-05 |
| **M10** projeção subespecificada | Sim | `estado(v,T)` com precedência ARCHIVED > SUPERSEDED > INVALIDATED_IN_TIME > ACTIVE_KNOWLEDGE (D4 l.897); `version`/`supersedes` por kind (D4 l.894; schema); `valid_to_efetivo` (D4 l.896); RULE-CKG-012 l.428-429 |
| m1 CONSTITUTION l.191 | Sim | matriz CONFIRMA (l.472): INV-06 + l.191-192 + [PROPOSTA] derivada |
| m2 T01 × VERIFICAÇÃO CKG-001 | Sim | BASpec-CKG-001 VERIFICADO POR = T01 (`ONTOLOGY_INTEGRITY_VIOLATION`); ADV-17 com `written`/`rejected_reason` |
| m3 sem digest | Sim | limite declarado (RULE-CKG-006 l.354-356; schema `_comentario`; risco novo) — não adicionado digest (função de hash = H-001/BUILD) |
| m4 `valid_to < valid_from` | Sim | `VALIDITY_WINDOW_INVALID` (D4 l.893; schema `valid_to`; ADV-19 f) |
| m5 gates de presença | Sim | limite declarado (RULE-CKG-008 l.379-380; BASpec-CKG-008; EC-005 POSTCOND) |
| m6 legalidade de `canonical_state_transition` | Sim | CHM l.744-757 / CEM l.460-466 ⇒ `CANONICAL_TRANSITION_ILLEGAL`; CCM espelhado sem validar (D4 l.906; schema `status_to`; ADV-19 e) |
| m7 cobertura CKG-010 → ADV-08 | Sim | cobertura l.1240-1241: CKG-010 → T09/ADV-21/T20 (ADV-08 rotulado fronteira de escopo) |
| m8 volume | Sim | consolidação (listas finais fundidas na etiquetagem; caminhos numa tabela; BASpec-CKG-010 enxugada; RULE/BASpec/EC referenciam D4). **plan.md: 1652 → 1641 linhas (NÃO ultrapassou 1652).** Volume continua alto para uma sessão; a divisão é decisão de Andraus (Q-ABERTURA-5) |
| G BL-003/BL-011 | Não é do autor | tratado por DHR-BACKLOG-001 (comunicada; ausente neste checkout) — plan l.42-44; RMR-001 não editado |

**Contagens (antes → depois), conferidas por busca de cabeçalhos:** BASpecs 13 → 13 (`### BASpec-CKG-`); EC 6 → 6 (`### EC-CKG-`); EARS 13 → **15** (`^N. Quando`); cenários 19 → **20** (`### Cenário-CKG-T`); adversariais 22 → 22 (`### ADV-CKG-`); invariantes locais 2 → 2; EC em E3: 5 → 5. Soma de cabeçalhos = 76 (13+6+15+20+22).

## 11-bis. Respostas às 8 interpelações do parecer (âncoras plan.md v1.5)

1. **"Preservar TODAS as versões":** cada versão canônica é nó próprio (`canonical_ref`=id@version) ligado por `canonical_predecessor_ref` (espelha `previous_version_id`, CHM-001 l.283/588, CCM-001 l.58) e `successor_ref` na transição a SUPERSEDED (CEM-001 l.450/594-595) — plan l.601-607, l.906, l.1317, l.1340; teste T17 (`version_chain(H) == ["H@1","H@2"]`, l.1123-1135) e negação ADV-19(d). Ponta-a-ponta = PARCIAL/[DECISÃO NECESSÁRIA] (Bloco B l.1532), porque a admissão por (a) é fail-closed.
2. **Verificador de (b) sem o selo:** não existe — e por isso (b) deixou de ser chamado verificável: sem contrato do selo, o gate de (b) é DENY `SEAL_CONTRACT_UNDEFINED` (RULE-CKG-010 l.402-412; §D2.3 l.524-538; T09(ii)). Só os DENY são verificáveis (Bloco A l.1522-1525).
3. **Caminho de relações de agente, de REFUTA em T11 e dos node_types sem caminho:** §D2.3 l.524-538 — relações de produtor (SAS-001 l.924) e CONFIRMA/REFUTA/… = caminho (c), contrato [DECISÃO NECESSÁRIA] ⇒ `ENTRY_PATH_UNDEFINED`; DERIVA_DE/HERDA espelhadas por (a); learning por (b); structure/narrative/mission/asset/… sem caminho. T11/ADV-02/ADV-18 usam fixture explícita até o passo 7 (convenção (iv), l.978-980).
4. **"Lote":** conceito eliminado (não definido como [PROPOSTA]); ancestral ausente ⇒ `ANCESTOR_NOT_ADMITTED` imediato, sem espera; sem deadlock porque o Lineage aponta para antecedentes e é imutável (CEM-001 l.530/560) [INFERÊNCIA] — plan l.500-505, l.907, l.959, T19 l.1147-1154.
5. **Onde persiste/invalida o resultado do bounded loop; por que ADV-20 é do KG:** não há resultado memorizado (memoização removida); cada decisão vai ao log append-only `kg_gate_decision` (D4 l.895), sem invalidação porque não é consultado como cache. ADV-20 (l.1231-1232) passou a testar só o que o KG controla: ≤1 invocação por submissão, zero retries/submissões geradas pelo KG; a frequência de novas submissões de produtor está fora do KG.
6. **INVALIDA × `invalidation`:** a relação INVALIDA é afirmação de conhecimento sobre o alvo (matriz l.477) e não altera sua validade; só o registro `invalidation` por ato autorizado (CKG-004) altera. A linha 2 da §D2.2 foi removida (l.518-522) por não satisfazer o escopo (mesmo from,to); ADV-18(d) cobre a não-colisão.
7. **Campos que tornam "custo/confiança" determinístico:** `node_type` (`calibration_metric` → `conviction` proibido) e ausência de campo de confiança no payload de `conviction` (`relation_confidence` só no payload de relação) — RULE-CKG-007 l.361-366, D4 l.902, EC-004 l.1404; limite declarado: semântica em texto livre não é detectada.
8. **`gate_record` do KG em toda escrita?** **Não.** `gate_record` só quando o OBJETO resulta de gate (gate a montante, ou o detector CKG-013 para o registro collision); os gates de admissão do KG registram suas decisões no `kg_gate_decision` — RULE-CKG-005 l.339-343; D4 l.893/895; EC-002/003 EVIDENCE. Coerente com T12 (PRIMARY sem `gate_record`).

---

## 12. Comandos que o Orquestrador deve rodar (Especificador sem Bash — NÃO executados)

```
python scripts/validate_spec_sot.py specs/features/SPEC-006/plan.md      # gate determinístico (STRUCT-10 etc.)
python scripts/revisor_gate.py specs/features/SPEC-006/plan.md           # gate fundido do Revisor (Classe D + sinais H)
python scripts/check_repo_research.py specs/features/SPEC-006            # RULE-ECC-06
python scripts/check_invariants.py specs/features/SPEC-006/plan.md       # valores/ordem das regras fixas (informativo)
python scripts/check_refs.py                                             # referências cruzadas (DHR-BACKLOG-001 citada)
python scripts/check_doc_sync.py                                         # drift documental (informativo)
python scripts/backlog_triggers.py                                       # BL-003/BL-011 x DHR-BACKLOG-001
python scripts/build_map.py && python scripts/build_map.py --check       # BL-019 — mapa em dia
npm run lint                                                             # lint EARS (15 critérios)
wc -l specs/features/SPEC-006/plan.md                                    # confirmar 1641 linhas
```

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness), com os pontos INDETERMINADOS declarados: 13 BASpecs (D/C/H), 15 EARS, 6 EC (E3 em 001..005), §D2.1/§D2.2/§D2.3, INV-CKG-01/02, `envelope_completo` único + `kg_gate_decision`, projeção `estado(v,T)`, todo caminho pendente fail-closed, 20 cenários, 22 adversariais, CONS-01 preservado. Três obrigações herdadas com evidência PARCIAL/[DECISÃO NECESSÁRIA] explícita.

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: comandos do §12 + submissão ao Revisor SOT; decisões [DECISÃO NECESSÁRIA] encaminhadas a Andraus.
