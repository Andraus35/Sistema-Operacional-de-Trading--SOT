# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.7 (candidato — rodada 8; etapa v1.0 "núcleo", Opção 2 — DHR-SPEC006-002)** (Cognitive Knowledge Graph; mecanismo físico INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-18 (Rodada 8 — DHR-SPEC006-002 D1 "Opção 2" e D3 "Avançar"; após o parecer NÃO CONFORME da rodada 7, `parecer-revisor-rodada7.md`)

> **Nota de método:** cada item foi conferido abrindo o plan.md v1.7 e a fonte citada. Nenhum validador foi executado pelo Especificador (sem Bash) — ver §12. Referências ao plan.md são por **seção/item** (D4.x, EARS n, T/ADV) — mais estáveis que número de linha; as poucas linhas citadas são da v1.7 (1224 linhas, contagem por busca de `^`).
> **Convenção de fonte única "dura" (v1.7):** predicado, obrigatoriedade de campo, ordem/precedência e código de rejeição só em **D4.0–D4.20**; §D2.1/§D2.2 = dados; schema = só campos e tipos.
> **Desenho declarado:** a v1.0 não admite nenhum registro de conhecimento (D4.15). Verificáveis: predicados de gate e fixtures. Admissão positiva = **fora de escopo** (emendas E-a..E-e), não INDETERMINADO convertido em PASS.
> **Itens em aberto (não marcados ✔):** tabela única de etiquetagem do plan.

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (inclui a porta de admissão que nega por padrão) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 (S10/S14 com entrega parcial declarada) + Non-goals (emendas E-a..E-e) |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 (obrigação + ponteiro D4); §D2.1 matriz; §D2.2 contradição; INV-CKG-01/02 |
| D3 Comportamento | Sim | ✔ | CKG-001..013 com CLASSE/MECANISMO (CC-11); ENTÃO cita D4 |
| D4 Algoritmo | Sim | ✔ | **D4.0–D4.20** (novos: D4.0 ordem/precedência; D4.19 presença de campos; D4.20 autorização) |
| D5 Estado | Sim | ✔ | estados = ponteiro a D4.7 (sem redefinição — r7-a); transitórios |
| D6 Protocolo | Sim | ✔ | ordem = D4.0 (passos 1–11) |
| D7 Teste | Sim (≥3) | ✔ | **T01..T22 (22)**; convenção (i)–(v) |
| D8 Adversarial | Sim (focado) | ✔ | **ADV-CKG-01..24 (24)**; ADV-08/09/10 marcados spec-time |
| D9 Auditoria | Por referência | Parcial | D4.3/D4.4/D4.5; recálculo de colisões (T17); sem digest (limite D4.3) |

**PASS (estrutural).**

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO | ENTÃO (cita D4) | PORQUE | REF | VERIF. | CLASSE | Gate/bounded |
|---|---|---|---|---|---|---|---|
| CKG-001 integridade | ✔ | D4.19/D4.1/D4.14 | ✔ | ✔ | = T01 | C | gate ✔ |
| CKG-002 ref. canônica | ✔ | D4.16/D4.1 | ✔ | ✔ | = T02 (`OBSERVATION_IS_NOT_EVIDENCE` agora com predicado em D4.1) | D | N/A |
| CKG-003 relação/linhagem | ✔ | D4.1/D4.2/D4.17 | ✔ | ✔ | = T03 | D | N/A |
| CKG-004 bitemporal | ✔ | D4.6/D4.3 | ✔ | ✔ | = T04 (fixture) | D | N/A |
| CKG-005 proveniência | ✔ | D4.2 | ✔ | ✔ | = T12/T14 | C | gate ✔ |
| CKG-006 imutabilidade | ✔ | D4.3/D4.5 | ✔ | ✔ | = T05 (`RECORD_MUTATION_FORBIDDEN`) | C | gate ✔ |
| CKG-007 custo/confiança | ✔ | D4.12 | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-008 causal/similar | ✔ | D4.10/D4.11 | ✔ | ✔ | = T07 | H | ≤1 invocação; host pendente ⇒ 0 ✔ |
| CKG-009 governança (E3) | ✔ | D4.20/D4.5 | ✔ | ✔ | = T08 + caso (b) log | C | gate ✔ |
| CKG-010 porta de admissão | ✔ | D4.15 | ✔ | ✔ | = T09 (5 casos) | C | gate ✔ |
| CKG-011 consulta/trace | ✔ | D4.8 | ✔ | ✔ | = T10 | D | N/A |
| CKG-012 lifecycle | ✔ | D4.4/D4.7 | ✔ | ✔ | = T13 | D | N/A |
| CKG-013 colisão | ✔ | D4.13/D4.18 | ✔ | ✔ | = T11 (`collisions_for_pair == 1`) | C | gate ✔ |

**PASS** (nenhuma admissão positiva marcada como verificável).

---

## 3. Critérios EARS

**21 critérios** (20 → 21). Mudanças: **EARS 10** passa a ser a regra única de admissão (`ADMISSION_CONTRACT_UNDEFINED`), absorvendo os antigos 10 e 14 e retirando a cláusula condicional de preservação da Evidência (vai para "Escopo em etapas"); **EARS 14** novo (`FIELD_PRESENCE_VIOLATION` — D4.19, R7-2); **EARS 9** cita D4.20 (conhecimento) e o log tem critério próprio; **EARS 21** novo (regra de escrita do log — R7-1); EARS 1/2/5/6/7/8 reescritos como referência a D4 (sem reenunciar o predicado). Todos no formato "Quando…, o KG DEVE…". **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo efeito | ✔ EC-CKG-001..006; o append ao log está coberto por EC-002 (imutabilidade) e EC-003 (escritor) |
| ENF-02 Nível ≥ piso | ✔ E3 em 001..005 (atomic-spec l.238); E1 em 006 |
| ENF-03 Detector ≠ Gate | ✔ juízo só propõe; limites de presença/forma declarados (D4.1, D4.2, D4.10, D4.14) |
| ENF-04 Fail-closed | ✔ D4.15 (nega por padrão); D4.5 (iii) identidade de serviço indisponível ⇒ nenhum commit |
| ENF-05 Policies não auto-aprendidas | ✔ bound de D4.11 versionado com a RULE |
| ENF-06 E0 | N/A |
| ENF-07 E3 falso-DENY | ✔ método amostral sobre o log; limiar = gap aberto — CONDICIONAL; EC-002 declara que a prova é lógica, sem digest (r7-g) |
| ENF-08 Escala E0–E3 | ✔ |

**PASS (ENF-07 com gap aberto declarado).**

---

## 5. Constitution Check (CC-01..CC-12)

CC-01 (5 camadas; espelhos RULE-HH-002/004 em D4.14, sem bypass por ausência de `hierarchy_role` — D4.19), CC-02 (payload fechado — ADV-11), CC-03/04 (D4.12; J-001 pendente), CC-08 (herança da Evidência com leitura única — sem supressão), CC-09 (admissão positiva = fora de escopo, não PASS), CC-10 (Termos 1–7), CC-11 = PASS. CC-05/06/07/12 OK/N-A. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

INHERITS reconferido na v1.7: CEM-001 l.257-264 (Status; único campo mutável), l.271-278 (Producer Type/ID), **l.280-283 (Evidence Origin Type: PRIMARY "Permitido apenas para `AGENT`"; DERIVED "Permitido apenas para `ENGINE`" — base do acoplamento novo em D4.2, R7-2)**, l.351-355, l.450, l.494, l.608-615; CHM-001 l.283/l.361/l.588/l.744-757; CCM-001 l.58; SPEC-004 plan l.264-265 (RULE-CBP-007), **l.338 (runtime autentica a identidade; `computed_by` vem daqui, não do payload)**, **l.381 (sem "publicação sem registro de auditoria")**, l.689; SPEC-005 plan l.88, l.859, l.971 (citação "l.242" removida — r7-d). REMOVED vazio; MODIFIED = só RULE-BB-004 reforçada. Itens retirados do ADDED da v1.6: extensão de preservação a hipótese/convicção (agora emenda E-a). **PASS com evidência PARCIAL declarada.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001 não decidida; Opção B adiada; divergência ROADMAP l.177 × Q-ABERTURA-3 registrada como [DECISÃO NECESSÁRIA] | ✔ |
| **Fonte única dura:** busca por "obrigatório" no plan v1.7 → só ocorrências descritivas de baseline (CHM-001 l.588; SAS-001 l.163) e o título do §7-bis; nenhuma no schema | ✔ (R7-2) |
| Códigos removidos (`PATH_A_ADMISSION_PENDING`, `SEAL_MISSING`, `SEAL_CONTRACT_UNDEFINED`, `ENTRY_PATH_UNDEFINED`) e §D2.3: busca → só na linha 1.7 do histórico (como texto de mudança) | ✔ |
| Todo código usado em BASpec/EARS/T/ADV/EC está definido em D4 (conferido código a código: 26 códigos) | ✔ |
| Ordem e precedência: só D4.0; D6 e EC-001 citam D4.0 | ✔ (R7-3, r7-b) |
| Regra do log: só D4.5; citada por RULE-CKG-009, BASpec-CKG-009, EARS 21, EC-002/003, D4.18, T17/T21/T22, ADV-23 | ✔ (R7-1) |
| Estados do lifecycle: definição só em D4.7; D5 é ponteiro | ✔ (r7-a) |
| M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 ABERTAS; SPEC-004/005 não reabertas; SPEC-007 não absorvida | ✔ |
| STRUCT-10 | conferência manual: nenhuma forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta sem negação; a linha da divergência usa "Resolve H-001" (citação do ROADMAP) seguida de "(H-001 não fechada)" — **confirmar com o gate (§12)** |

**PASS (itens em aberto explicitamente não marcados ✔).**

---

## 8. Verificação mecânica de citações (abri cada arquivo/linha nesta rodada)

| Citado | Diz o afirmado? | Fonte verificada |
|---|---|---|
| Opção 2 (mesmo número, em etapas; v1.0 nega toda escrita sem contrato; contratos por emendas aditivas); não é divisão para o RMR-001; ordem "Avançar" | ✔ | `governance/DHR-SPEC006-002_…md` §1 D1–D3 |
| H-001 e demais seguem abertas; teto CONFORME condicional pela divergência ROADMAP:177 × Q-ABERTURA-3 | ✔ | DHR-SPEC006-002 §2; `ROADMAP.md` l.177 |
| BL-003/BL-011 `ATIVADO`; R-04..R-06 e COL-EXP-05 decididos no gate da SPEC-006 | ✔ | DHR-BACKLOG-001 §1 (l.15), §2 (l.18); RMR-001 l.102/l.110 |
| PRIMARY só AGENT; DERIVED só ENGINE | ✔ | CEM-001 l.280-283 |
| Status é o único campo mutável | ✔ | CEM-001 l.264 |
| KG preserva "Todos os estados" | ✔ | CEM-001 l.494; l.611-614 |
| Runtime autentica a identidade; `computed_by` não vem do payload | ✔ | SPEC-004 plan l.338 |
| Proibida "publicação sem registro de auditoria" | ✔ | SPEC-004 plan l.381 |
| SPEC-005: `Evidence.Invalidated` no envelope; propagação de eventos CEM; não escreve no KG | ✔ | SPEC-005 plan l.859; l.86-89; l.971 |
| "KG publicado → E3 mínimo"; ENF-07; gaps; INV-04 | ✔ | atomic-spec l.238; l.273; l.393; l.404 |

**PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **BL-003 e BL-011 `ATIVADO`** (RMR-001 l.102/l.110), encaminhados ao gate da SPEC-006; DHR-SPEC006-002 D2: a entrega em etapas não re-aponta gatilhos. Nota de gate do plan: BL-003 = camada lógica no núcleo, admissão em E-a, física em H-001/G-001 (ABERTAS); BL-011 = tabela com **"encaminhamento — tratamento proposto"** (r7-f: a v1.6 dizia "TRATADO", contrariando a ata §2); R-07 e fila EXP-SPEC = [DECISÃO NECESSÁRIA]. RMR-001 não editado.
- BL-010 tangente (SPEC-007); BL-029 independente.

---

## 10. RULE-ECC-04 / RULE-ECC-06 — presença

Sem pesquisa web nova nesta rodada (reestruturação por decisão de Andraus e correções ancoradas no repositório). Dossiê homologado na abertura (validade até 2027-01-03); 4 repositórios elegíveis, nenhum adotado; RULE-ECC-05 não incide. **PASS (presença).**

---

## 11. Rastreabilidade da Rodada 8 (parecer da rodada 7)

| Item | Procede? | Correção (plan v1.7) |
|---|---|---|
| **R7-1** log fora da unidade atômica, sem governança, PASS forjável, carve-out só na §D2.3, T21 contraditório | Sim | **D4.5** (fonte única do log): escritor único = identidade de serviço autenticada; outra identidade ⇒ `LOG_WRITER_UNAUTHORIZED`; ordem/falha (i)–(iii): decisões PASS **dentro** da unidade D4.18 (espelha SPEC-004 l.381), DENY como única escrita, identidade indisponível ⇒ nenhum commit; resolução do `gate_record` do collision exige `writer_id` de serviço e mesma `submission_id`; escopo "o log não é conhecimento". D4.18 inclui as decisões PASS. Norma: RULE-CKG-009 e BASpec-CKG-009 (caso b), EARS 21, EC-002/003. **T21** com identidades explícitas (serviço disponível; falha por `RECORD_VERSION_INVALID`); **T22** (append falha ⇒ nada gravado; PASS forjado negado; identidade indisponível); **ADV-23**. A §D2.3 (onde o carve-out vivia) foi eliminada |
| **R7-2** obrigatoriedade no schema sem predicado | Sim | **D4.19** (tabela única de presença; payload fechado; `school` proibido na submissão); D4.2 ganha `evidence_origin_type` fora de evidence e o acoplamento PRIMARY⇒AGENT / DERIVED⇒ENGINE (CEM-001 l.282-283); D4.0 põe D4.19 antes de D4.14 (sem bypass de RULE-HH-002); schema sem "obrigatório"; §7-bis Bloco C corrigido (RULE-ONT-01 agora tem predicado); **T20** (c)–(g), **ADV-24** |
| **R7-3** `SEAL_MISSING` inalcançável; precedência não declarada | Sim | Dissolvido pela Opção 2: o selo e seus códigos saem (emenda E-b); D4.15 tem **um** código; precedência geral em **D4.0** (primeiro predicado reprovado define o código; D4.15 primeiro) |
| **R7-4** critério mínimo de (a) pode suprimir obrigações da Evidência | Sim (leitura de supressão possível) | A [PROPOSTA] de critério mínimo foi **retirada** (emenda E-a, sem contrato). Leitura única no plan, "Escopo em etapas": a v1.0 não restringe estados/versões de Evidência e **toda emenda fica proibida de restringi-los** sem REMOVED governado (RULE-HD-03); Bloco B: PARCIAL por bloqueio a montante, [DECISÃO NECESSÁRIA] sobre a emenda, não sobre a obrigação |
| r7-a D5 × D4.7 | Sim | D5 só aponta a D4.7 |
| r7-b ordem passos 5/7; códigos de `computed_by`/`produced_by_gate` | Sim | D4.0 fixa a ordem; D4.3 **não** avalia `provenance_ref` (só D4.2) ⇒ um código por campo ausente |
| r7-c ADV-06 "condicionalidade não é brecha" | Sim | ADV-06 reescrito com o limite declarado (`produced_by_gate=false` falso não detectável; consistência ≠ veracidade) |
| r7-d SPEC-005 "l.242" | Sim | removida; Herança cita l.88/l.859/l.971 |
| r7-e aciclicidade sem predicado | Sim | D4.17: derivação (aresta sempre para nó já admitido ⇒ ordem topológica; auto-referência ⇒ `ANCESTOR_NOT_ADMITTED`); T19 caso F + `deriva_de_cycles == 0` |
| r7-f "TRATADO" para R-04..R-06 | Sim | "encaminhamento — tratamento proposto" em toda a tabela; etiquetagem [INFERÊNCIA]/[PROPOSTA] |
| r7-g EVIDENCE lida do próprio log, sem digest | Sim | EC-CKG-002 EVIDENCE declara que a prova é lógica; integridade física não provada (H-001/BUILD); D4.3 limite |
| r7-h sem auditoria de colisão; multiplicidade | Sim | D4.13: um collision por par (chave D4.9); auditoria por recálculo como-registrado; T17 `recomputed_collisions == recorded_collisions`; ADV-18 (e) |
| r7-i `successor_ref` no payload fechado de conviction; `school` supplied × derived | Sim | `successor_ref` retirado da allowlist de D4.12 (fica em `canonical_state_transition`); T06 (e). `school` = atributo derivado, proibido na submissão (D4.19); T20 (e), ADV-24 (c) |
| r7-j "Estruturalmente CONFORME" no checks | Sim | substituído por "verificação estrutural: PASS (feedback interno)" — ver Resultado |

**Contagens (antes → depois), por busca de cabeçalhos:** BASpecs 13 → 13; EC 6 → 6; EARS 20 → **21**; cenários 21 → **22**; adversariais 22 → **24**; invariantes locais 2 → 2; itens D4 18 → **21** (D4.0–D4.20); EC em E3: 5 → 5. Cabeçalhos BASpec+EC+cenário+ADV = 65 (13+6+22+24). **plan.md: 1498 → 1224 linhas** (contagem por `^`; inclui o novo D4.0/D4.19/D4.20, T22, ADV-23/24). Interpelações Q1–Q5/Q7 da rodada 7: o resumo do parecer (`parecer-revisor-rodada7.md`) não traz o texto delas; o conteúdo dos achados que as motivaram está coberto pela tabela acima — se o Revisor as reapresentar, respondo item a item.

---

## 12. Comandos que o Orquestrador deve rodar (Especificador sem Bash — NÃO executados)

```
python scripts/validate_spec_sot.py specs/features/SPEC-006/plan.md      # gate determinístico (STRUCT-01..12; STRUCT-10)
python scripts/revisor_gate.py specs/features/SPEC-006/plan.md           # gate fundido (contagem_declarada, campos_atribuidos_baseline, estado_backlog)
python scripts/check_repo_research.py specs/features/SPEC-006            # RULE-ECC-06
python scripts/check_invariants.py specs/features/SPEC-006/plan.md       # valores/ordem das regras fixas (informativo)
python scripts/check_refs.py                                             # referências cruzadas (DHR-SPEC006-002, DHR-BACKLOG-001)
python scripts/check_doc_sync.py                                         # drift documental (informativo)
python scripts/backlog_triggers.py                                       # BL-003/BL-011 ATIVADO
python scripts/build_map.py && python scripts/build_map.py --check       # BL-019 — mapa em dia
npm run lint                                                             # lint EARS
wc -l specs/features/SPEC-006/plan.md                                    # confirmar ~1224 linhas
```

---

## Resultado da verificação de spec

**Verificação estrutural: PASS (feedback interno — não é parecer)**, com os pontos declarados: 13 BASpecs (D/C/H), 21 EARS, 6 EC (E3 em 001..005), §D2.1/§D2.2, INV-CKG-01/02, D4.0–D4.20 como fonte única dura, porta de admissão única fail-closed, log com escritor único e decisões PASS dentro da unidade atômica, 22 cenários, 24 adversariais, CONS-01 preservado. Duas obrigações herdadas (Evidência: estados/versões; CEE-001 l.111) com evidência PARCIAL por bloqueio a montante, declarada.

> Feedback interno — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: comandos do §12 + submissão ao Revisor SOT; [DECISÃO NECESSÁRIA] encaminhadas a Andraus.

---

## Apêndice H — Histórico detalhado das versões 1.0–1.6 do plan.md (transferido sem alteração — INV-07)

> Linhas copiadas literalmente da tabela "Histórico de versões" do `plan.md` v1.6 (l.32-38). Não normativas; preservadas para rastreabilidade. As referências de linha nelas são das versões respectivas, não da v1.7.

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-10-11 | Entrega candidata inicial (Opção A; mecanismo físico INDETERMINADO = H-001). 13 BASpecs (CKG-001..013); 6 EC; 13 EARS; 11 cenários; 10 adversariais. |
| 1.1 | 2026-10-12 | **Rodada 2 (achados do gate, do Revisor e verificados no repositório).** (A) STRUCT-10: removida toda forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta. (B1) §7-bis Bloco C ampliado a todas as N8–N17. (B2) SRC-FORGET-01 declarada sem sustentar alegação carregada sozinha. (B3) EC-CKG-002 registra tentativas de DELETE bloqueadas. (B4) falha de auth da SPEC-004 ⇒ não-autorizado (fail-closed). (C1) escrita permanente elevada a **E3** (atomic-spec §10.2); "piso E2" eliminado. (C2/C9) **duas fontes de entrada** reconciliadas sob uma trilha de governança única; preservação de REFUTED/SUPERSEDED/ARCHIVED declarada; selo de publicação = dependência de SPEC-007 [DECISÃO NECESSÁRIA]. (C3) Cognitive Trace Reconstruction = obrigação **completa** (independe de H-001); T10 ampliado a 3 saltos. (C4) tipo de relação **DERIVA_DE** (aresta de Lineage) acrescentado, separado de `provenance_ref`. (C5) matriz de integridade tipo×origem/destino×direcionalidade/simetria + "família estrutural" + teste de violação. (C6) invalidação/supersessão como **novos registros**; estado = projeção derivada (espelha SPEC-004 INV-CBP-01). (C7) schema com `version`/`supersedes`/selo/escritor/colisão; REJECTED/CANDIDATE_WRITE = estados transitórios (não persistidos). (C8) BL-029 corrigido para **`Em espera`**. (C13) critérios de SUPERSEDED×INVALIDATED_IN_TIME×ARCHIVED, correção/reativação, rebaixamento, autoridade de arquivamento. (C14) `recorded_at` acrescentado à relação (bitemporal real). (C17) RULE-CAU-02 (regime) e RULE-CAU-03 (marcador pós-hoc) incorporadas; atribuição pós-hoc corrigida; gate causal só verifica presença. (C18) node_type **observation** (INV-06). (C21) emissão de evento pelo KG **removida** (só consome); emissão = [DECISÃO NECESSÁRIA] dependente da SPEC-005. (C22) governança/versionamento da ontologia definida (spec-time SPEC-019; runtime K-001 [DECISÃO NECESSÁRIA]). Extra: `gate_record` reatribuído à SPEC-004 (não CEM-001). Cobertura: 13 BASpecs; 6 EC; 13 EARS; 13 cenários (T01..T13); **15 adversariais** (ADV-CKG-01..15). |
| 1.2 | 2026-10-12 | **Rodada 3 (defeitos confirmados por revisão independente, verificados no repositório).** (1) Matriz §D2.1: HERDA = sub→pai pelo `parent_id` (SPEC-001)/`parent_hypothesis_id` (CHM-001), inclusive **entre escolas** (SMC/Fibonacci SUB → Elliott PRIMARY — SPEC-001 RULE-HH-003 l.104; CONSTITUTION l.193); "família estrutural" só restringe sub-hipóteses intra-escola; ORIGINA: origem ∈ {Elliott, SMC, Fibonacci}, nunca ICT (INV-02); atributo `school`/`origin_agent` (por referência ao canônico); o KG só **espelha**, não decide, a autoridade de criação (CC-01). (2) `lineage_ref` (campo inexistente) → `provenance_ref.lineage` [PROPOSTA] = referência ao campo `Lineage` (CEM-001 l.351/359/539-554) / `derived_from[]` (SPEC-004). (3) Preservação de estado canônico: `canonical_status` (snapshot) + registro `canonical_state_transition` (estado/timestamp/origem/justificativa — CEM-001 l.428); estados do KG ≠ estados canônicos (CC-10). (4) Critério de admissão Blackboard→KG do caminho (a) = [DECISÃO NECESSÁRIA] (promoção trabalho→permanente — SPEC-018/K-001). (5) Completude do trace garantida: admitir evidence DERIVED ⇒ exigir aresta DERIVA_DE por ancestral do Lineage (fail-closed); trace ignora validade e é acíclico (INV-CKG-02); teste negativo. (6) INV-04 = só custo; proibição de *confiança* entrar na convicção = regra LOCAL [PROPOSTA] (CKG-007); matriz restringe CAUSA (destino `conviction` proibido a partir de custo/confiança); restrição à SPEC-003 = requisito a ela endereçado/[DECISÃO NECESSÁRIA]. (7) Invalidação de relação = ato AUTORIZADO (CKG-009), **não** automática (CEM-001 l.602 "não implica cascata"; impacto é de CHM/CCM — l.503/606; CHM-001 l.672-676); consumo de evento = [INFERÊNCIA]/[DECISÃO NECESSÁRIA] (SPEC-005 não define "Evidence Invalidated"). (8) Schema: `record_kind`, `relevance`, `target_relation_id`, identidade para nós não-canônicos, `collision_record` como registro. (9) "conhecimento permanente/temporário" tratado/diferido (SPEC-018/K-001 [DECISÃO NECESSÁRIA]). (10) CONFIRMA/REFUTA restritas a `evidence` (INV-06; CONSTITUTION l.191). (11) Bitemporal: consulta valid-time + transaction-time (as-of-registro). (12) Citação RMR-001 → l.128/l.192. (13-18) correções menores. Contagem: 13 BASpecs; 6 EC; 13 EARS; **14 cenários** (T01..T14); **16 adversariais** (ADV-CKG-01..16); 2 invariantes locais (INV-CKG-01/02). |
| 1.3 | 2026-10-12 | **Rodada 4 (6 Maiores do controle, confirmados no repositório).** (1) **T01 corrigido** (a v1.2 NÃO o havia reescrito): T01 agora usa ORIGINA com `school=ICT` (caso que a matriz DE FATO rejeita) + novo **T15 positivo** HERDA SMC-SUB → Elliott-PRIMARY (RULE-HH-003). (2) **Campos unificados:** um só campo `school` (eliminado "origin_agent"); adicionado `hierarchy_role` {PRIMARY,SUB} (ref. SPEC-001); "família" COMPUTADA via `school`+PERTENCE_A(asset,timeframe); regra de nó `hypothesis.school ≠ ICT` (INV-02/RULE-HH-004) com teste (T01) e **ADV-17**; HERDA.pai restrito a `hierarchy_role=PRIMARY`. (3) **gate_record CONDICIONAL** (espelha SPEC-004 CBP-007): `computed_by`/`writer_id` SEMPRE obrigatório; `gate_record` só se há gate; `lineage`/`derived_from` só se derivado; `[]` legítimo (PRIMARY/asset/timeframe/regime/observation); CKG-005/T12/T14/schema ajustados. (4) **SPEC-005/Evidence.Invalidated corrigido:** o tipo é canônico (CEM-001 l.600/722) e a SPEC-005 o TRANSPORTA (l.88/859); o que falta é o consumidor/contrato de consumo pelo KG = [DECISÃO NECESSÁRIA] (linhas l.115/242 — que eram o envelope — removidas). (5) **CKG-013/colisão:** tabela de pares contraditórios §D2.2 (CONFIRMA×REFUTA; INVALIDA×relação-alvo) + escopo (mesmos from/to + sobreposição de validade) + algoritmo D4 + teste negativo **ADV-18** (origens distintas/validades disjuntas não colidem). (6) **CKG-010/admissão:** gate (a) declarado NÃO-ESPECIFICADO/INDETERMINADO (não vacuoso) + [PROPOSTA] de critério mínimo (estados ACTIVE/DOMINANT/SUPERSEDED/REFUTED/ARCHIVED; exclui EMERGENT/CANDIDATE); reatribuição de S14 à SPEC-018/K-001 submetida a Andraus [DECISÃO NECESSÁRIA]; ordem de admissão de ancestrais (`PENDING_ANCESTOR`, sem deadlock de INV-CKG-02). Histórico reordenado 1.0→1.3. Contagem: 13 BASpecs; 6 EC; 13 EARS; **15 cenários** (T01..T15); **18 adversariais** (ADV-CKG-01..18); 2 invariantes locais. |
| 1.4 | 2026-10-17 | **Rodada 5 (retomada por ordem de Andraus, chat 2026-10-17; 4 defeitos conferidos pelo Orquestrador + 8 reportados por revisões anteriores, cada um reconferido no repositório).** **(V1)** D6 passo 5 alinhado à proveniência CONDICIONAL de CKG-005 (`computed_by` sempre; `gate_record` sse gate; `lineage` sse derivado; `[]` legítimo) + **T16** (teste de sequência D6 para PRIMARY sem gate e sem ancestral). **(V2)** Caminho (a) CANÔNICO de CKG-010 retirado do PRECOND do EC-CKG-001: enquanto o critério de admissão estiver pendente de Andraus, (a) é **fail-closed — não admite** (`PATH_A_ADMISSION_PENDING`); frase de cobertura do §7-bis corrigida (a admissão positiva por (a) é INDETERMINADO, não verificável); convenção de teste (gate em isolamento × persistência condicional) declarada em D7; **ADV-CKG-21**. **(V3)** **Envelope único append-only** (`kg_record`) para TODO tipo de registro (creation/invalidation/archival/canonical_state_transition/collision) com `record_id`/`version`/`supersedes`/`target_record_ref`/`schema_version`/proveniência/`writer_id`/`recorded_at`/validade; eliminados o `collision_record` avulso e o `record_kind=collision` dentro de `relation_record` (um só formato de colisão) + **T17** (reconstrução/auditoria) + **ADV-CKG-19**. **(V4)** BOUNDED LOOP da CKG-008 = **uma passada por submissão**, sem retry automático; ao esgotar ⇒ INDETERMINADO, nada escrito; fonte atomic-spec §10.6 l.315 + RULE-INQ-03 (RULES l.678) + precedente SPEC-002 l.370-371/SPEC-003 l.387-388; versionado com RULE-CKG-008 (alteração só por emenda spec-time) — refletido em RULE/BASpec/D4/EC-CKG-005 + **ADV-CKG-20**. **(R1)** `PENDING_ANCESTOR` incluído na máquina de estados D5 (transitório, limitado ao lote de admissão) e na sequência D6 + **T19**. **(R2)** enum de `canonical_status` corrigido por baseline: `REFUTED` é só do CHM-001; CEM-001 = ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED (l.258-262); CCM-001 = COMPUTED/GATED_PASS/GATED_BLOCK/SUPERSEDED (l.58). **(R3)** `school` declarado campo LOCAL [PROPOSTA] **derivado** de `producer_id` canônico (CHM-001 §2.9 l.361; CEM-001 l.276-278) — não é campo canônico; enum = 5 camadas da hierarquia (inclui **Fractal**, ausente na v1.3); regra espelho RULE-HH-002 (PRIMARY ⇒ Elliott); mapeamento produtor→Fractal = [DECISÃO NECESSÁRIA]; `school` ≠ `Domain` (CC-10). **(R4)** COL-EXP-01..05 (CONFLICT-MAP l.143-147) ganham tabela de tratamento; reconciliação COL-EXP-05 permanece adiada ([DECISÃO NECESSÁRIA]). **(R5)** SIMILAR_A ganha gate de saída determinístico (`similarity_basis` presente ∧ mesmo node_type ∧ from≠to; duplicata simétrica = no-op) + **T18** + **ADV-CKG-22**. **(R6)** EC-CKG-004 elevado a **E3** (guard sobre a escrita permanente — piso atomic-spec l.238). **(R7)** nó ganha `valid_from`/`valid_to` e todo registro ganha `target_record_ref` (via envelope). **(R8)** limiar de falso-DENY mantido como gap aberto (atomic-spec l.273/l.393); declarado só o MÉTODO amostral, sem valor. Extra: linhas de RULES.md corrigidas (RULE-BB-004 l.324; RULE-ONT-01 l.672; RULE-CAU-01/02/03 l.681-683); caminho de entrada de nós de referência (asset/timeframe/regime/observation/calibration_metric) declarado lacuna [DECISÃO NECESSÁRIA]. **Permanecem [DECISÃO NECESSÁRIA]:** critério/produtor/gatilho do caminho (a); caminho de nós de referência; selo SPEC-007; mapeamento produtor→Fractal; consumidor de eventos; emissão pelo KG; allowlist/host do juízo; migração de ontologia; escala de confiança; limiar de falso-DENY; reconciliação COL-EXP-05; H-001, J-001, N-001, M-001, G-001, K-001, C-001, WF-D03, ECC-03-001 (todas ABERTAS). Contagem: 13 BASpecs; 6 EC; 13 EARS; **19 cenários** (T01..T19); **22 adversariais** (ADV-CKG-01..22); 2 invariantes locais (INV-CKG-01/02). |
| 1.5 | 2026-10-17 | **Rodada 6 (parecer NÃO CONFORME da rodada 5 — `parecer-revisor-rodada5.md`; Plan devolvido por Andraus, chat 2026-10-17).** **(C1)** "preservar TODAS as versões" (CEM-001 l.612; l.594-595; l.450): mecanismo `canonical_predecessor_ref` (espelha `previous_version_id` — CHM-001 l.283/588; CCM-001 l.58) + `successor_ref` obrigatório quando `status_to=SUPERSEDED` (gate `VERSION_LINK_MISSING`); T17 (fixture H@1→H@2) + ADV-19(d); Bloco B: evidência PARCIAL/[DECISÃO NECESSÁRIA] (admissão por (a) pendente). **(C2)** CEE-001 l.111: evidência PARCIAL/[DECISÃO NECESSÁRIA] (`calibration_metric` sem caminho de entrada); ADV-05 reescrito (só o isolamento é verificável). **(M1)** caminho (b) e allowlist tratados como (a): contrato do selo pendente ⇒ DENY `SEAL_CONTRACT_UNDEFINED`; mantenedor da allowlist pendente ⇒ DENY `WRITER_ALLOWLIST_UNDEFINED`; "verificável" restrito a predicados. **(M2)** tabela única de caminhos de entrada §D2.3 (nós, relações espelhadas, relações de produtor — SAS-001 l.924 — = caminho (c) [DECISÃO NECESSÁRIA]); convenção de teste (iv) para o detector de colisão (T11/ADV-02/ADV-18 por fixture). **(M3)** EARS 14/15 + **T20** (`ENTRY_PATH_UNDEFINED`, `SCHOOL_UNDERIVABLE`, `WRITER_ALLOWLIST_UNDEFINED`); só Elliott tem `producer_id` conhecido (SPEC-001 l.203) ⇒ SMC/Fibonacci/ICT/Fractal hoje `SCHOOL_UNDERIVABLE`. **(M4)** linha INVALIDA×relação-alvo removida da §D2.2 (INVALIDA ≠ registro `invalidation`); ADV-18(d). **(M5)** gate de CKG-008 = TODA relação CAUSA/SIMILAR_A, qualquer produtor; bounded loop só quando há juízo. **(M6)** memoização removida; limite = 1 invocação por submissão, KG não gera retry; ADV-20 reescrito. **(M7)** conceito "lote"/`PENDING_ANCESTOR` eliminado: ancestral ausente ⇒ REJECTED imediato; T19 por fixture. **(M8)** `envelope_completo` único (D4) referenciado por RULE/schema/EC; `gate_record` = só objeto que RESULTA de gate (upstream ou detector de colisão); decisões dos gates do próprio KG (PASS/DENY/INDETERMINADO) vão ao log `kg_gate_decision` (formato próprio, declarado). **(M9)** guard CKG-007 determinístico por `node_type` (CAUSA `calibration_metric`→`conviction`; nenhum campo de confiança no payload de `conviction`); limite declarado. **(M10)** função de projeção com precedência ARCHIVED > SUPERSEDED > INVALIDATED_IN_TIME > ACTIVE_KNOWLEDGE e `version`/`supersedes` de todos os `record_kind`. **(m1–m7)** âncora CONSTITUTION l.191-192 + INV-06; T01/verificação CKG-001 alinhados; limite de digest declarado; `VALIDITY_WINDOW_INVALID`; limite de gates de presença; legalidade de transição CHM/CEM (`CANONICAL_TRANSITION_ILLEGAL`; CCM sem tabela ⇒ espelha sem validar); cobertura CKG-010→T09/ADV-21. **(m8)** consolidação (listas finais fundidas na tabela de etiquetagem; caminhos numa tabela única). **(G)** gatilho `spec:SPEC-006 em redação` de BL-003/BL-011 tratado pela decisão de Andraus comunicada pelo Orquestrador (ata DHR-BACKLOG-001) — RMR-001 não reaberto. **Permanecem [DECISÃO NECESSÁRIA]:** critério/produtor/gatilho de (a); contrato do selo (b); contrato do caminho (c); caminho de nós de referência e de structure/narrative/mission; mantenedor da allowlist; host do juízo; mapeamento `producer_id`→`school` (SMC/Fibonacci/ICT/Fractal); consumidor de eventos; emissão pelo KG; migração de ontologia; escala de confiança; limiar de falso-DENY; COL-EXP-05; H-001, J-001, N-001, M-001, G-001, K-001, C-001, WF-D03, ECC-03-001 (ABERTAS). Contagem: 13 BASpecs; 6 EC; **15 EARS**; **20 cenários** (T01..T20); 22 adversariais (ADV-CKG-01..22); 2 invariantes locais. |
| 1.6 | 2026-10-17 | **Rodada 7 (parecer NÃO CONFORME da rodada 6 — `parecer-revisor-rodada6.md`; ordem de Andraus, chat 2026-10-17: "Rodada 7 enxugando o texto").** **Método:** fonte única por regra — predicados/códigos em **D4.1–D4.18** (numerados), campos no schema, caminhos na §D2.3; RULE/BASpec/EARS/EC/cenários/ADV citam por referência; cenários idênticos ao VERIFICADO POR de uma BASpec passam a referenciá-lo. **(N1)** ata `governance/DHR-BACKLOG-001_…md` e RMR-001 l.102/110/191 (BL-003/BL-011 `ATIVADO`) citados corretamente em todas as ocorrências; encaminhamento item a item de X-01, R-01..R-07 e X-04 (R-04..R-06 definidos por conteúdo — [INFERÊNCIA]); R-07/COL-EXP-05 e fila EXP-SPEC = [DECISÃO NECESSÁRIA]; pergunta "este Plan é a ativação?" removida (a ata decidiu). **(N2)** discriminantes fixos `provenance_ref.produced_by_gate` (booleano explícito) e `evidence_origin_type` (espelho CEM-001 l.280-283) + código `PROVENANCE_INCONSISTENT` (D4.2). **(N3)** `producer_type`/`producer_id` no payload (CHM-001 l.361; CEM-001 l.271-278); limite: o espelho de INV-02 é de FORMA (sem lookup ao canônico). **(N4)** `kg_gate_decision` append-only e imutável sob RULE-CKG-006/EC-CKG-002 (E3), `decision_id` único; T17 resolve o `gate_record` do collision no log; redução a `record_kind` avaliada e rejeitada (D4.5). **(N5)** colisão detectada no passo 8 e gravada só na unidade atômica tudo-ou-nada da admissão (D4.18; SPEC-004 plan l.381/l.689) + **T21**. **(N6)** elos de versão tipados por modelo (D4.16); `successor_ref` obrigatório só para CEM (l.450), [PROPOSTA] local opcional para CHM/CCM; elos presentes DEVEM resolver no KG. **(N7)** `posthoc_flag` obrigatório com valor explícito; ADV-04 reescrito. **(N8)** guard único de custo E confiança (D4.12): payload de `conviction` FECHADO (`additionalProperties:false`). **(N9)** EARS 16–20 (`ANCESTOR_NOT_ADMITTED`, `VERSION_LINK_MISSING`, `CANONICAL_TRANSITION_ILLEGAL`, `VALIDITY_WINDOW_INVALID`, `RECORD_VERSION_INVALID`) + ADV-19(g). **(N10)** "todos os estados/todas as versões" = obrigação herdada só para Evidência (CEM-001 l.494/612); extensão a hipótese/convicção = [PROPOSTA] local em conflito com o critério mínimo de (a) — [DECISÃO NECESSÁRIA]. **(N11)** `colide` com `valid_to_efetivo` (D4.13); §D2.2 e ADV-18(b) alinhados. **(n1–n9)** checks:86 reescrito; `estado(v,T)` só para T ≥ valid_from + `recorded_at` monotônico; INVALIDA→relação via `target_relation_id` (não é node_type); escritor dos registros internos (§D2.3); checks:95 corrigido; convenção (v) de fixtures; EC-006 sem PRECOND de autorização inexistente (autorização de leitura = [DECISÃO NECESSÁRIA]); transição perdida = limite fail-closed + reconciliação [DECISÃO NECESSÁRIA]; host do juízo pendente ⇒ 0 invocações. **Permanecem [DECISÃO NECESSÁRIA]:** as da v1.5 + R-07/fila EXP-SPEC; extensão de preservação a hipótese/convicção × critério de (a); reconciliação de transição perdida; autorização de leitura; coincidência `producer_id`↔objeto canônico (contrato de (a)); H-001, J-001, N-001, M-001, G-001, K-001, C-001, WF-D03, ECC-03-001 (ABERTAS). Contagem: 13 BASpecs; 6 EC; **20 EARS**; **21 cenários** (T01..T21); 22 adversariais; 2 invariantes locais. |
