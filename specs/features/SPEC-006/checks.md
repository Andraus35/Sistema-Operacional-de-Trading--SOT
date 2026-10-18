# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.6 (candidato — rodada 7)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico de armazenamento INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-17 (Rodada 7 — ordem de Andraus, chat 2026-10-17, "Rodada 7 enxugando o texto", após o parecer NÃO CONFORME da rodada 6, `parecer-revisor-rodada6.md`)

> **Nota de método:** cada item foi conferido abrindo o plan.md v1.6 e a fonte citada (arquivo:linha). Nenhum validador foi executado pelo Especificador (sem Bash) — ver §12. Linhas do plan.md citadas abaixo são da v1.6 (1498 linhas).
> **Convenção de fonte única (v1.6):** predicados e códigos de rejeição em **D4.1–D4.18** (plan l.798-815); campos no I/O Schema (l.1145-1217); caminhos na §D2.3 (l.439-456). RULE/BASpec/EARS/EC/cenários/ADV citam essas seções.
> **Limitação funcional declarada:** o KG hoje **não admite nenhuma escrita de conhecimento** (§D2.3). Verificáveis: **predicados de gate e fixtures**; admissão positiva fim a fim = **INDETERMINADO**.
> **Itens em aberto (não marcados ✔):** ver a tabela única de etiquetagem do plan (l.1426-1457).

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — alvo ROADMAP §6; CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; permanente ≠ trabalho; mecanismo físico INDETERMINADO) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA] (citam D4); §D2.1 matriz; §D2.2 colisão (janela efetiva); §D2.3 caminhos (+ escritor dos registros internos); INV-CKG-01/02 |
| D3 Comportamento (BASpec) | Sim | ✔ | CKG-001..013 com CLASSE/MECANISMO (CC-11); ENTÃO cita D4 |
| D4 Algoritmo | Quando há regra determinística real | ✔ | **D4.1–D4.18 numerados** — fonte única (inclui D4.2 proveniência com discriminantes, D4.5 log imutável, D4.12 guard único, D4.16 elos tipados, D4.18 admissão atômica) |
| D5 Estado | Sim | ✔ | projeção D4.7; transitórios CANDIDATE_WRITE/REJECTED |
| D6 Protocolo | Sim | ✔ | Passos 1–11 (+5-bis, 5-ter); colisão detectada no 8 e gravada no 9 (atômico) |
| D7 Teste | Sim (CRITICAL; ≥3) | ✔ | **T01..T21 (21)** + convenção (i)–(v); cenários idênticos a VERIFICADO POR referenciam a BASpec |
| D8 Adversarial | Sim (CRITICAL, focado) | ✔ | **ADV-CKG-01..22 (22)** |
| D9 Auditoria | Por referência | Parcial | D4.3/D4.4 + log `kg_gate_decision` (D4.5, imutável); replay (T17); sem digest (limite m3) |

**Resultado:** profundidade-alvo D0–D7 atingida; D8 focado. **PASS (estrutural).**

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REF | VERIF. | CLASSE | Gate/bounded |
|---|---|---|---|---|---|---|---|
| CKG-001 ontologia + regras de nó (D4.1/D4.14) | ✔ | ✔ | ✔ | ✔ | ✔ (= T01) | C | gate ✔ |
| CKG-002 ref canônica + elos tipados (D4.16) | ✔ | ✔ | ✔ | ✔ | ✔ predicado/fixture; ponta-a-ponta INDETERMINADO | D | N/A |
| CKG-003 relação tipada/DERIVA_DE (D4.17) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-004 temporalidade (D4.6) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-005 proveniência (D4.2) | ✔ | ✔ | ✔ | ✔ | ✔ (casos a/b = T12/T14) | C | gate ✔ |
| CKG-006 imutabilidade conhecimento + log (E3) | ✔ | ✔ | ✔ | ✔ | ✔ (caso b = log) | C | gate ✔ |
| CKG-007 guard custo E confiança (D4.12) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ (limite: texto livre) |
| CKG-008 toda CAUSA/SIMILAR_A (D4.10/D4.11) | ✔ | ✔ | ✔ | ✔ | ✔ | H | ≤1 invocação/submissão; host pendente ⇒ 0 ✔ + gate ✔ |
| CKG-009 governança (E3; allowlist) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate ✔ |
| CKG-010 fronteira (D4.15/§D2.3) | ✔ | ✔ | ✔ | ✔ | ✔ só os DENY; admissão positiva **INDETERMINADO** | C | DENY por pendência |
| CKG-011 consulta/trace (D4.8) | ✔ | ✔ | ✔ | ✔ | ✔ (`records_created_by_query == 0`) | D | N/A |
| CKG-012 lifecycle (D4.7) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-013 colisão (D4.13/D4.18) | ✔ | ✔ | ✔ | ✔ | ✔ (fixture; negativo T21) | C | gate ✔ |

**PASS (nenhuma admissão positiva marcada como verificável).**

---

## 3. Critérios EARS

**20 critérios** (15 → 20; plan l.462-481). Alterados na v1.6: **EARS 5** (cita D4.2 e os discriminantes), **EARS 6** (inclui o log), **EARS 7** (guard único D4.12 — custo E confiança), **EARS 8** (`posthoc_flag` explícito), **EARS 10** (preservação total só para Evidência — N10), **EARS 13** (colisão na unidade atômica; nenhum `collision` se a admissão falhar). **Novos (N9):** EARS 16 `ANCESTOR_NOT_ADMITTED` (negativo T19/ADV-16), EARS 17 `VERSION_LINK_MISSING` (ADV-19 d), EARS 18 `CANONICAL_TRANSITION_ILLEGAL` (ADV-19 e), EARS 19 `VALIDITY_WINDOW_INVALID` (ADV-19 f), EARS 20 `RECORD_VERSION_INVALID` (ADV-19 g). **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 |
| ENF-02 Nível ≥ piso | ✔ E3 em 001..005 (atomic-spec l.238); EC-002 cobre também o log `kg_gate_decision` com justificativa de nível (plan l.1250); E1 em 006 |
| ENF-03 Detector ≠ Gate | ✔ juízo CKG-008 detector; guards por campo/node_type; limites de presença/forma declarados (D4.2, D4.10, D4.14) |
| ENF-04 Fail-closed | ✔ pendência = DENY em (a), (b), (c), host do juízo, nós sem caminho e allowlist |
| ENF-05 Policies não auto-aprendidas | ✔ bound do loop versionado com a RULE |
| ENF-06 E0 | N/A |
| ENF-07 E3 falso-DENY | ✔ método amostral sobre `kg_gate_decision` (agora imutável — D4.5); limiar = gap aberto — CONDICIONAL |
| ENF-08 Escala E0–E3 | ✔ |

**PASS (ENF-07 com gap aberto declarado).**

---

## 5. Constitution Check (CC-01..CC-12)

CC-01 (5 camadas; regras espelho em D4.14; espelho de FORMA declarado — N3), CC-02 (campos espelhados são cópias de referência; legalidade lida dos grafos canônicos; CCM sem tabela ⇒ espelho), CC-08 (extensão de preservação a hipótese/convicção reetiquetada [PROPOSTA] local — N10; três obrigações herdadas com evidência PARCIAL/[DECISÃO NECESSÁRIA]), CC-09 (nenhum INDETERMINADO convertido em PASS; afirmação falsa sobre a ata corrigida — N1), CC-10 (Termo 5: duas acepções de "PRIMARY"), CC-11 = PASS. CC-03/04 (guard D4.12). CC-05/06/07/12 OK/N-A. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

INHERITS reconferido na v1.6 (abri cada linha): CEM-001 l.258-264 (Status; único campo mutável), l.271-278 (`Producer Type`/`Producer ID`), l.280-283 (`Evidence Origin Type` PRIMARY/DERIVED), l.351-355 (`Lineage`: PRIMARY ⇒ []; DERIVED ⇒ obrigatória), l.450 (SUPERSEDED "Referencia a Evidência sucessora"), l.494 (tabela de estados **da Evidência**), l.608-615 (Responsabilidades do KG — no capítulo da **Evidência**); CHM-001 l.283 e l.588 (`previous_version_id`; "toda nova versão deverá referenciar exatamente uma versão anterior"), l.361 (`producer_type`, `producer_id`, `created_at`), l.744-757; CCM-001 l.58 e l.75-78 (`version`, `previous_version_id`, `status` — enum sem tabela/grafo de transições de status; a única outra ocorrência de mudança do modelo, l.125, é governança de alteração do próprio CCM, não transição de status — **n1**); SPEC-004 plan l.264-267 (RULE-CBP-007: `gate_record` "quando o objeto resulta de um gate"), l.381 e l.689 (publicação atômica tudo-ou-nada). REMOVED vazio; MODIFIED = só RULE-BB-004 reforçada. **PASS com evidência PARCIAL declarada.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001 NÃO decidida; Opção B ADIADA | ✔ |
| **Fonte única:** cada predicado/código de rejeição está em UMA linha de D4 (l.798-815); RULE-CKG-001..013, BASpecs (ENTÃO/MECANISMO), EARS 1/5/7/8/12/13/17/20, D6 passos 2–9, EC PRECONDs, T06/T17/T21 e ADV-04/05/06/18/19 citam o item de D4 | ✔ (resposta ao "Volume" da rodada 6) |
| Proveniência: a regra está em D4.2 (l.799). RULE-CKG-005 (l.301) enuncia a obrigação e cita D4.2; BASpec-CKG-005 (l.578) **resume** o predicado no ENTÃO e cita D4.2 — **n5:** a v1.5 dizia aqui que a BASpec "não repete a regra", o que era falso; agora o resumo é declarado e a fonte é D4.2 | ✔ |
| Formatos de registro: `kg_record` (conhecimento; D4.3/D4.4) e `kg_gate_decision` (decisões; D4.5) — papéis distintos, AMBOS imutáveis (RULE-CKG-006 l.309; EC-CKG-002 l.1241); um só formato de COLISÃO | ✔ (N4) |
| Guard de INV-04: texto único em D4.12 (l.809); RULE-CKG-007 (l.317), BASpec-CKG-007, EARS 7 (l.468), EC-CKG-004 PRECOND (l.1274), ADV-03/05, T06 e schema (`payload.node.creation[node_type=conviction]`, l.1179) citam "custo E confiança" e D4.12 | ✔ (N8) |
| Colisão com janela efetiva: D4.13 (l.810); §D2.2 (l.426); ADV-18(b) (l.1085) | ✔ (N11) |
| Caminhos de entrada: §D2.3 (l.439-456) referenciada por RULE-CKG-010, D4.15, D6 passo 2, EC-001, EARS 10/14, T09/T20, ADV-21 | ✔ |
| Escopo de CKG-008 = TODA CAUSA/SIMILAR_A; bounded loop sem memoização; host pendente ⇒ 0 invocações (D4.11 l.808; §D2.3 l.447) | ✔ (M5/M6/n9) |
| `PENDING_ANCESTOR`/"lote" eliminados | ✔ — grep "lote"/`PENDING_ANCESTOR` só nas linhas de histórico (l.35-37) |
| Projeção `estado(v,T)` definida só para T ≥ valid_from (D4.7 l.804) | ✔ (n2) |
| M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 ABERTAS; SPEC-004/005 não reabertas; SPEC-007 não absorvida | ✔ |
| STRUCT-10 | conferência manual ✔ — busca por `fechad*/resolvid*/homologad*` a ≤40 caracteres de um ID `[A-Z]-\d{3}` com fronteira de palavra: **0 ocorrências** na v1.6 — **confirmar com o gate (§12)** |

**PASS (com itens explicitamente em aberto, não marcados ✔).**

---

## 8. Verificação mecânica de citações (abri cada arquivo/linha nesta rodada)

| Citado | Diz o afirmado? | Fonte verificada |
|---|---|---|
| Ata DHR-BACKLOG-001: BL-003 e BL-011 → `ATIVADO`, encaminhados ao gate da SPEC-006; COL-EXP-05 e R-04..R-06 decididos no gate da SPEC-006 | ✔ | `governance/DHR-BACKLOG-001_Ata_Promocao_BL003_BL011_ATIVADO.md` §1 (l.15), §2 (l.18) |
| RMR-001: BL-003 `ATIVADO` (l.102); BL-011 `ATIVADO` com "tratar R-01..R-07 e X-04 e a reconciliação COL-EXP-05 no gate da SPEC-006" (l.110); nota datada (l.191) | ✔ | `backlog/RMR-001_Painel_Backlog.md` l.102/l.110/l.191 |
| Rótulos R-xx/X-xx não são catálogo fechado; correspondência por conteúdo; R-04..R-06 = residuais de aplicação | ✔ | CLASSIFICACAO l.23; l.53-62 |
| COL-EXP-01..05 | ✔ | CONFLICT-MAP l.143-147 |
| `Evidence Origin Type` PRIMARY (só AGENT) / DERIVED (só ENGINE) | ✔ | CEM-001 l.280-283 |
| `Lineage`: PRIMARY ⇒ []; DERIVED ⇒ obrigatória | ✔ | CEM-001 l.351-355 |
| `producer_type`, `producer_id` (hipótese) | ✔ | CHM-001 l.361 |
| `previous_version_id` obrigatório em nova versão (hipótese) | ✔ | CHM-001 l.588 |
| CCM-001 tem `previous_version_id` mas não enuncia obrigatoriedade | ✔ (por isso [INFERÊNCIA] em D4.16) | CCM-001 l.58; l.75-78 |
| Sucessora referenciada só na Evidência | ✔ (por isso `successor_ref` obrigatório só p/ CEM — N6) | CEM-001 l.450 |
| "Preservar todas as versões / todos os estados" está no capítulo da Evidência | ✔ (por isso extensão a hipótese/convicção = [PROPOSTA] — N10) | CEM-001 l.494; l.608-615 |
| Publicação atômica tudo-ou-nada | ✔ | SPEC-004 plan l.381; l.689 |
| `gate_record` "quando o objeto resulta de um gate" (sem campo discriminante na SPEC-004) | ✔ (por isso `produced_by_gate` local [PROPOSTA] — N2) | SPEC-004 plan l.264-267 |
| "KG publicado → E3 mínimo" | ✔ | atomic-spec.md l.238 |
| Contagens (§11) | ✔ por busca de cabeçalhos | plan.md v1.6 |

**PASS.** *(A linha da v1.5 "DHR-BACKLOG-001 NÃO localizada neste checkout" era falsa — N1; removida.)*

---

## 9. Gate RMR-001 (passo 11-bis)

- **BL-003 e BL-011 estão `ATIVADO`** (Andraus, chat 2026-10-17; ata DHR-BACKLOG-001 §1; RMR-001 l.102/l.110/l.191), encaminhados ao gate da SPEC-006. O plan registra o encaminhamento item a item (Nota de gate, plan l.44-63): BL-003 = camada lógica neste contrato, parte física H-001/G-001 (ABERTAS); BL-011 = X-01, R-01, R-02/R-03, R-04..R-06 [INFERÊNCIA de conteúdo], X-04 **TRATADOS**; R-07/COL-EXP-05 e a fila EXP-SPEC-001..053 **NÃO executados** = [DECISÃO NECESSÁRIA]. O Especificador **não** edita o RMR-001. *(N1: a v1.5 dizia que o RMR-001 mostrava BL-011 em estado anterior e que a ata não estava no checkout — ambos falsos; corrigido.)*
- BL-010 tangente (SPEC-007); BL-029 independente (RMR-001 l.128).

---

## 10. RULE-ECC-04 / RULE-ECC-06 — presença

Sem pesquisa web nova nesta rodada (correções internas, ancoradas em baselines do repositório). SRC-ZEP-01/PROV-01/MEMVSKG-01 verbatim em sources/; SRC-FORGET-01 DADO não-verbatim; 4 repositórios elegíveis, nenhum adotado; RULE-ECC-05 não incide. **PASS (presença).**

---

## 11. Rastreabilidade da Rodada 7 (parecer da rodada 6) — linhas do plan.md v1.6

| Item | Procede? | Correção (plan v1.6) |
|---|---|---|
| **N1** ata "ausente" / BL-011 em estado superado | **Sim** (conferido: a ata existe e o RMR-001 l.102/110/191 mostra `ATIVADO`) | Nota de gate l.44-63 (fonte com ata e linhas; tabela X-01..R-07/X-04 com encaminhamento item a item; R-04..R-06 definidos — [INFERÊNCIA], CLASSIFICACAO l.23/l.58-62; R-07 e fila EXP-SPEC = [DECISÃO NECESSÁRIA]; pergunta "este Plan é a ativação?" removida); etiquetagem (linha DHR-BACKLOG-001, l.1432; R-07 l.1447; estado do BL-003); Autopré-check (passo 11-bis); §7-bis Bloco C (RULE-EPI); checks §8/§9 |
| **N2** sem discriminante PRIMARY/DERIVED / "resulta de gate" | Sim | campos fixos `provenance_ref.produced_by_gate` (booleano explícito, local [PROPOSTA]) e `evidence_origin_type` (espelho CEM-001 l.280-283): D4.2 (l.799, + `PROVENANCE_INCONSISTENT`), D4.3 (l.800), schema l.1158/l.1173; RULE-CKG-005 l.301; ADV-06 (a–e) l.1049; limite: consistência, não veracidade |
| **N3** `producer_id` fora do schema | Sim | `producer_type`/`producer_id` no payload (schema l.1171-1172; CHM-001 l.361; CEM-001 l.271-278); limite "espelho de FORMA, sem lookup" em §D2.1 l.379 e D4.14 (l.811); coincidência com o canônico = [DECISÃO NECESSÁRIA] (§D2.3; etiquetagem) |
| **N4** log sem imutabilidade / `decision_id` / T17 | Sim | RULE-CKG-006 l.309 (inclui o log); D4.5 l.802 (`decision_id` único, imutável; resolução do `gate_record` do collision; redução a `record_kind` avaliada e rejeitada, com motivo); EC-CKG-002 l.1241 (cobre o log; LEVEL E3 justificado l.1250); BASpec-CKG-006 caso (b); T05; T17 l.971 (`collision_gate_record_resolves`); §D2.3 l.451 (escritor do log) |
| **N5** colisão antes da validação | Sim | D6 passo 8 detecta sem gravar (l.869), passo 9 commit atômico (l.870); D4.13 l.810; D4.18 l.815 (tudo-ou-nada, espelha SPEC-004 plan l.381/l.689); RULE-CKG-013; BASpec-CKG-013 l.768; EARS 13; **T21** l.1017 (negativo) |
| **N6** versões: `successor_ref` sem fonte p/ CHM/CCM; elos não resolvem | Sim | D4.16 l.813 (tipado por modelo; `canonical_model` fixo pelo node_type; CHM l.588 [FONTE], CCM [INFERÊNCIA], CEM l.450 [FONTE]; `successor_ref` CHM/CCM = [PROPOSTA] local opcional; todo elo presente DEVE resolver ⇒ senão `VERSION_LINK_MISSING`); schema l.1200; T17; ADV-19(d) |
| **N7** `posthoc_flag` opcional | Sim | obrigatório com valor explícito (ausência ≠ false): D4.10 l.807; RULE-CKG-008 l.325; schema l.1190; ADV-04 l.1043 reescrito com caso (b) e limite de veracidade |
| **N8** guard de INV-04 divergente | Sim | texto único D4.12 l.809 (payload `conviction` FECHADO `additionalProperties:false`; relação de QUALQUER tipo `calibration_metric`→`conviction` proibida); todas as cópias citam D4.12 (ver §7) |
| **N9** quatro códigos sem EARS; versão sem código | Sim | EARS 16–20 (l.477-481); `RECORD_VERSION_INVALID` em D4.4 (l.801); negativos T19, ADV-19 (d)(e)(f)(g) l.1088 |
| **N10** "todos os estados/versões" de hipótese/convicção como herdado | Sim | INHERITS CHM (extensão [PROPOSTA] local); RULE-CKG-010 l.341; EARS 10 (só evidência); conflito com o critério mínimo de (a) registrado na nota de BASpec-CKG-010 (l.723) e na etiquetagem = [DECISÃO NECESSÁRIA]; Bloco B |
| **N11** `colide` com `valid_to` bruto | Sim | D4.13 l.810 (`valid_to_efetivo`, D4.6 com `+∞`); §D2.2 l.426; ADV-18(b) l.1085 |
| n1 checks:86 "grep transi" | Sim | §6 acima reescrito (descrição do conteúdo de CCM-001 l.58/75-78/125) |
| n2 `estado(v,T)` p/ T<valid_from; `recorded_at` | Sim | D4.7 l.804 (definida só para T ≥ valid_from); D4.4 l.801 (`recorded_at` monotônico ⇒ `RECORD_VERSION_INVALID`); ADV-19(g) |
| n3 destino "relation" fora do enum | Sim | matriz INVALIDA l.398 (`target_relation_id` com `to_node = null`; "relação" não é node_type); schema `to_node` l.1187; D4.9 chave |
| n4 escritor dos registros internos | Sim | §D2.3 l.449-451 (invalidation/archival = escritor autorizado do ato; collision = identidade de serviço na unidade atômica; log = runtime dos gates) |
| n5 checks:95 | Sim | §7 acima corrigido |
| n6 allowlist de fixture | Sim | convenção (v) de D7 (presunção declarada, só para o predicado); T15/T16 a citam |
| n7 EC-006 autorização de leitura / log de consulta | Sim | EC-CKG-006 l.1298-1309: PRECOND sem autorização inexistente (política de leitura = [DECISÃO NECESSÁRIA]); EVIDENCE = contagem de registros antes/depois; "log de consulta" não afirmado |
| n8 transição perdida | Sim | D4.16 l.813: limite declarado (fail-closed trava o sujeito); reconciliação = [DECISÃO NECESSÁRIA]; risco na tabela |
| n9 limite por submissão; host | Sim | D4.11 l.808 (bound é por submissão por desenho — frequência de produtor fora do KG; `judgment_invocations` no log); host pendente ⇒ 0 invocações e `ENTRY_PATH_UNDEFINED` (§D2.3 l.447) |

**Preservado da rodada 5 (sem regressão):** C2 (CEE-001 l.111 PARCIAL — Bloco B; ADV-05), M1 (pendência = DENY em todo caminho — §D2.3/D4.15), M3 (EARS 14/15 + T20), M4 (INVALIDA fora da §D2.2), M5 (escopo CKG-008), M7 (sem estado de espera — D4.17/T19), M10 (precedência D4.7; versão por kind D4.4).

**Contagens (antes → depois), conferidas por busca de cabeçalhos:** BASpecs 13 → 13 (`### BASpec-CKG-`); EC 6 → 6 (`### EC-CKG-`); EARS 15 → **20** (`^N. Quando` em "Critérios de Aceitação"); cenários 20 → **21** (`### Cenário-CKG-T`); adversariais 22 → 22 (`### ADV-CKG-`); invariantes locais 2 → 2; EC em E3: 5 → 5. Cabeçalhos BASpec+EC+cenário+ADV = 62 (13+6+21+22); com EARS = 82. **plan.md: 1641 → 1498 linhas (meta ≤ 1500 cumprida; −143).**

## 11-bis. Respostas às 8 interpelações do parecer da rodada 6 (âncoras plan.md v1.6)

1. **Encaminhamento de R-01..R-07/X-04 e o que são R-04..R-06:** Nota de gate, plan l.48-59. Os rótulos não são catálogo fechado (CLASSIFICACAO l.23); por conteúdo: X-01=COL-EXP-01, R-01=COL-EXP-02, R-02/R-03=COL-EXP-03, X-04=COL-EXP-04, R-07=COL-EXP-05 ([FONTE], CLASSIFICACAO l.53-57); **R-04..R-06** = os residuais "de aplicação" (CLASSIFICACAO l.62) que o RMR-001 l.110 enuncia como "confidence≠Conviction/J-001; Experience Packet projeta CEM", lidos com as fronteiras de CLASSIFICACAO l.58-60 — R-04 confiança≠Conviction (l.55), R-05 Packet projeta CEM/CHM (l.56), R-06 memória sem autoridade decisional/imutabilidade (l.57) — **[INFERÊNCIA]** declarada. X-01..R-06 e X-04 TRATADOS; R-07 e a fila EXP-SPEC = [DECISÃO NECESSÁRIA] (l.59; etiquetagem l.1447).
2. **Campo que distingue DERIVED/PRIMARY e "resulta de gate":** `evidence_origin_type` (espelho CEM-001 l.280-283; schema l.1173) e `provenance_ref.produced_by_gate` (booleano explícito; schema l.1158); predicado D4.2 (l.799) com `PROVENANCE_INCONSISTENT`; obrigatórios no envelope D4.3 (l.800). ADV-06 (l.1049) e INV-CKG-02 (agora sobre `evidence_origin_type=DERIVED`) tornam-se determinísticos. Limite: verifica consistência, não veracidade frente ao objeto a montante.
3. **Onde o gate lê `producer_id`:** no próprio payload (`producer_type`/`producer_id`, schema l.1171-1172; espelho CHM-001 l.361 / CEM-001 l.271-278); D4.14 (l.811) deriva `school` dele. Não há lookup ao canônico: o espelho de INV-02 é declarado **de forma** (§D2.1 l.379); a coincidência com o objeto canônico é precondição do contrato de (a) = [DECISÃO NECESSÁRIA].
4. **Imutabilidade do `kg_gate_decision`; T17 e `gate_record`:** RULE-CKG-006 (l.309) e INV-CKG-01 cobrem o log; D4.5 (l.802) — append-only, imutável, `decision_id` único; EC-CKG-002 (l.1241, E3 justificado l.1250) e BASpec-CKG-006 caso (b) com `gate_decision_mutated == false`. T17 (l.971): o `gate_record` de C1 = `DEC-1`, que resolve para `kg_gate_decision{gate_id=CKG-013, result=PASS}` (`collision_gate_record_resolves == true`); `gate_record` de objeto a montante é referência à SPEC-004 (resolução fora do KG — limite declarado em D4.5). A redução a `record_kind` foi avaliada e rejeitada com motivo (D4.5).
5. **O que impede `collision` persistido se a escrita reprova; atomicidade:** o detector só avalia no passo 8 (l.869, D4.13 "SEM gravar"); a gravação ocorre na unidade atômica tudo-ou-nada do passo 9 (l.870; D4.18 l.815, espelho de SPEC-004 plan l.381/l.689): se qualquer registro da unidade falha D4.3/D4.4, nenhum é gravado. Negativo: **T21** (l.1017; `collision_written == false`, `dangling_collision_refs == 0`).
6. **Fonte de `successor_ref` para CHM/CCM; os elos precisam resolver?** Não há fonte: para CHM/CCM `successor_ref` é opcional, **[PROPOSTA] local** (D4.16 l.813; schema l.1200); obrigatório só para CEM (l.450). Predecessor: CHM obrigatório ([FONTE] l.588), CCM obrigatório por [INFERÊNCIA] (l.58). **Sim, todo elo presente deve resolver para nó já no KG**, senão `VERSION_LINK_MISSING` (EARS 17, l.478) — consequência e conflito com o critério de (a) registrados (nota l.723).
7. **O que torna ADV-04 e o guard de custo verificáveis sem enumerar campos:** ADV-04 (l.1043): `posthoc_flag` passou a ser obrigatório com valor explícito (D4.10 l.807) — sua AUSÊNCIA é detectável por presença (o valor falso declarado continua não detectável: limite declarado). Guard de custo: em vez de lista de vedados, o payload de `conviction` é **fechado** por allowlist de campos (`additionalProperties:false`, D4.12 l.809; schema l.1179) — qualquer campo fora dela, inclusive custo ou confiança, é rejeitado; mais a proibição de toda relação `calibration_metric`→`conviction`. Verificado em T06 e ADV-05.
8. **Volume:** **1641 → 1498 linhas** (≤1500), com mais conteúdo normativo (5 EARS, T21, D4.18). O método foi o remédio indicado pelo Revisor — fonte única em D4.1–D4.18 e citação nas demais representações; 11 cenários idênticos a VERIFICADO POR (T01–T05, T07, T08, T10, T12–T14) viraram referência, e T09 em parte. **Proposta de divisão:** o Especificador não a propõe nesta rodada porque o componente é coeso (os 13 comportamentos compartilham envelope, caminhos e log) e a causa dos achados era duplicação, não amplitude; se Andraus quiser reduzir o tamanho por sessão de revisão, um corte possível — [DECISÃO NECESSÁRIA], Q-ABERTURA-5 — seria (i) contrato de registro e integridade (D2, D4.1–D4.9, D4.12–D4.18, schema) e (ii) fronteira de entrada, causalidade e consulta (§D2.3, D4.10/D4.11, CKG-008/010/011). Não executado.

---

## 12. Comandos que o Orquestrador deve rodar (Especificador sem Bash — NÃO executados)

```
python scripts/validate_spec_sot.py specs/features/SPEC-006/plan.md      # gate determinístico (STRUCT-01..12; STRUCT-10)
python scripts/revisor_gate.py specs/features/SPEC-006/plan.md           # gate fundido (estado_backlog, contagem_declarada, campos_atribuidos_baseline, dhr_backlog)
python scripts/check_repo_research.py specs/features/SPEC-006            # RULE-ECC-06
python scripts/check_invariants.py specs/features/SPEC-006/plan.md       # valores/ordem das regras fixas (informativo)
python scripts/check_refs.py                                             # referências cruzadas (ata DHR-BACKLOG-001, CLASSIFICACAO)
python scripts/check_doc_sync.py                                         # drift documental (informativo)
python scripts/backlog_triggers.py                                       # BL-003/BL-011 ATIVADO x DHR-BACKLOG-001
python scripts/build_map.py && python scripts/build_map.py --check       # BL-019 — mapa em dia
npm run lint                                                             # lint EARS
wc -l specs/features/SPEC-006/plan.md                                    # confirmar 1498 linhas
```

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness), com os pontos INDETERMINADOS declarados: 13 BASpecs (D/C/H), 20 EARS, 6 EC (E3 em 001..005; EC-002 cobre o log), §D2.1/§D2.2/§D2.3, INV-CKG-01/02, D4.1–D4.18 como fonte única, admissão atômica, todo caminho pendente fail-closed, 21 cenários, 22 adversariais, CONS-01 preservado. Três obrigações herdadas com evidência PARCIAL/[DECISÃO NECESSÁRIA] explícita; extensão de preservação a hipótese/convicção = [PROPOSTA] em conflito declarado.

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: comandos do §12 + submissão ao Revisor SOT; decisões [DECISÃO NECESSÁRIA] encaminhadas a Andraus.
