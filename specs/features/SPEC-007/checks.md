# checks.md — Verificação de Spec da SPEC-007 (fase spec-first)

**Objeto:** `specs/features/SPEC-007/plan.md` **v1.2 (CANDIDATA — correção da rodada 2 do Revisor; aguarda rodada 3 por delta e homologação de Andraus)** (RAG / WikiRAG / Knowledge Formation Harness). *[v1.1: "v1.1 (CANDIDATA — correção da rodada 1 do Revisor; aguarda rodada 2 por delta e homologação de Andraus)"; v1.0: "v1.0 (CANDIDATA — aguarda Revisor integral e homologação de Andraus)"]*
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — **NÃO** é teste de runtime, **NÃO** é parecer do Revisor, **NÃO** é homologação. "VERIFY" interno = feedback. [FONTE: atomic-spec §14]
**Método:** atomic-spec.md v1.5 · tlc-spec-lean (PLAN = Spec; CHECKS = verificação de spec) · overlay GUS-TLC-001
**Data:** 2026-10-23 (v1.0, v1.1 e v1.2)
**Pareceres tratados:** R1 `governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R1-2026-10-23.md` (NÃO CONFORME — 9 Médias, 12 Menores; v1.1); R2 `governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R2-2026-10-23.md` (NÃO CONFORME — 5 Médias N-01..N-05, 14 Menores; v1.2).
**Contagens declaradas (por cabeçalho — recontadas por busca nesta sessão; a reconferir no ambiente pai):** **20** RULE-KFH (`^RULE-KFH-`), 2 INV-KFH, **20** BASpec (`### BASpec-KFH-`), **20** EARS (`^N. (KFH-`), **13** EC (`### EC-KFH-`), **26 cenários** (`### Cenário-KFH-T` — T01..T26), **29 ADV** (`### ADV-KFH-` — 01..29). *[v1.1: 17/17/17/10/23/26; v1.0: 17/17/17/10/22/20]* O Anexo v1.1 do Plan é recuado (não conta em `^RULE-KFH-`).

> **Nota sobre a v1.1 deste checks (n-12/m-12 da R2):** a v1.1 dava PASS em §1/§5/§6/§9 apesar de N-01..N-03. Na v1.2 cada PASS abaixo é **estrutural e condicionado**: os itens que dependem de Andraus aparecem como "Aberto (fail-closed)", e os positivos dependem de pré-condições declaradas (P-1, P-3, P-4a/P-4b, P-10).

## R2 — verificação das correções (N-01..N-05)

| Média | Âncora no Plan v1.2 | Positivo / negativo | Estado |
|---|---|---|---|
| N-01 | RULE-KFH-007 "ORDEM (N-01)"; D4.2 v1.2 (ordem fixa, fail-fast); nota de pré-condições no topo de D7; T14/ADV-21/ADV-22 | T10, T23 / ADV-18(b) | ✔ estrutural |
| N-02 | RULE-KFH-004 "PROPOSTA DE REGISTROS"; RULE-KFH-005 (d) + "DEFINIÇÃO ÚNICA DE `material_hash`"; RULE-KFH-007 (ii)/(vii); D4.2 passo (2); contrato | D4.2 exemplo / ADV-21(d) | ✔ estrutural |
| N-03 | RULE-KFH-020; BASpec-KFH-020; EC-KFH-012; contrato `authorization_act_record`; usos em KFH-001/007(v)/009(a) | T24 / ADV-27, ADV-22(d) | ✔ estrutural; **quem grava = Aberto (SPEC-007-ACTREC-001; conjunto vazio no intervalo)** |
| N-04 | INV-KFH-02 (3 caminhos); RULE-KFH-019; BASpec-KFH-019; EC-KFH-011 (E3); EC-KFH-012 (liberação E3); `consumer_locus` (KFH-010 (e-bis), KFH-012, contrato) | T25 / ADV-28 | ✔ estrutural; **propagação = Aberto (SPEC-007-DERIVTX-001; conjunção no intervalo)** |
| N-05 | RULE-KFH-012 SÍNTESE (mecanismo D+H; risco RULE-UNC-01); RULE-KFH-018; BASpec-KFH-018 (H, laço, gate); EC-KFH-013; IDs no `evidence_packet` | T26 / ADV-29, ADV-15(b), ADV-23 | ✔ estrutural; risco residual declarado |

Menores n-01..n-14: ver tabela "Correções da rodada 2" no Plan (todas com âncora).

> **Nota m-12 (correção de ✔ da v1.0):** na v1.0 este arquivo deu ✔ a itens que o parecer R1 mostrou contraditos — §1 D8 (o caso de negação da KFH-016 era formal), §6 linha RULE-CKG-012 (sucessão sem `supersedes`/`version+1`/`expected_version`) e §2/Bloco A da KFH-016. Esses ✔ foram retirados e os itens são reavaliados abaixo **após** as correções da v1.1; o que ainda depende de Andraus está marcado "Aberto", não ✔.

> **Itens em aberto (não ✔ por natureza — dependem de Andraus):** quem mantém a lista de emissores do selo e onde roda o juízo de fidelidade (e, se estendido, SPEC-006 l.482); corte de "alto impacto"; **SPEC-007-NODETYPE-001** (no intervalo: nenhum selo); **SPEC-007-SUCC-001** (no intervalo: só Andraus autoriza sucessão); **SPEC-007-RIGHTS-001 / SPEC-007-EXTTX-001** (no intervalo: só ato de Andraus por fonte; sem ato ⇒ INDETERMINADO/FALSE); **SPEC-007-BBTYPE-001** (no intervalo: pacote só como resposta read-only); **SPEC-007-ACTREC-001** (no intervalo: conjunto de aprovadores vazio — nenhum ato resolve); **SPEC-007-DERIVTX-001** (no intervalo: conjunção das origens-raiz); sinalização de dependentes de item marcado (lacuna, n-05); estados do candidato se viver no Blackboard (M-001, aberta); errata à SPEC-006 para o committer verificar `seal_ref` (proposta); limiares e limites de laço (INDETERMINADO); emenda à SPEC-020 (só na homologação); livro (Q7c, ADIADA); tipo de evento "selo emitido" na SPEC-005.

---

## 0. Consolidação (fonte única de regra)

| Verificação | Resultado |
|---|---|
| Cada regra definida UMA vez em D2 (RULE-KFH-001..020, INV-KFH-01/02); textos v1.0 e v1.1 das regras reescritas preservados nos Anexos do Plan | ✔ |
| EARS prefixados pela regra-fonte `(KFH-0NN)` | ✔ (20; EARS 5/7 atualizados e 18–20 novos na v1.2) |
| BASpecs dizem "Aplica RULE-KFH-0NN" + REFERÊNCIA | ✔ (20) |
| D4/D5/D6/EC/D7/D8/Herança referenciam por ID | ✔ |
| Regras da SPEC-006 citadas por ID+linha, não recopiadas nem alteradas (CC-02) | ✔ (RULE-CKG-004/005/008/009/010/011/012/013; l.976; l.1415) |

## 1. Cobertura de profundidade (D0–D8 — CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S14 + Non-goals (livro Q7c, `rag/` GEN-1, Benchmark) |
| D2 Regra | Sim | ✔ | RULE-KFH-001..020 + INV-KFH-01/02 [PROPOSTA] |
| D3 Comportamento | Sim | ✔ | BASpec-KFH-001..020; §D3.1 (v1.2: `SOURCE_RIGHTS_INDETERMINATE` pai próprio — n-03; `AUTH_ACT_*`, `RECORD_CONTENT_NOT_VALIDATED`, `SYNTHESIS_*`, `SEAL_REVOCATION_REQUESTED`, subs de `SEAL_SCOPE_INVALID`) |
| D4 Algoritmo | Determinísticos/semi | ✔ | D4.2 v1.2: ordem fixa fail-fast (N-01), hash único (N-02), reserva de consumo (n-02), gatilho de sucessora (n-01); v1.1 preservada logo abaixo; D4.4 derivado direto × dependente |
| D5 Estado | Sim | ✔ | `KC_*` + entrada de formação esgotada (m-06); M-001 aberta |
| D6 Protocolo | Sim | ✔ | formação; consulta com entrega read-only no intervalo (M-07); atualização com ato de sucessão (M-02) |
| D7 Teste | Sim | ✔ (positivos condicionados às pré-condições declaradas — N-01/n-12) | T01..T26 (T23 sucessão; T24 ato; T25 CIM; T26 redator) |
| D8 Adversarial | Sim | ✔ (reavaliado — m-12) | ADV-KFH-01..29 (v1.2: ADV-27 ato inválido, ADV-28 derivação/locus, ADV-29 redator; ADV-15/21/22/23/25 ampliados); **KFH-016 agora tem negação própria (ADV-25 → `CONTRADICTION_SILENT_RESOLUTION_FORBIDDEN`)**; ADV-21 (selo reaproveitado), 22 (sucessão sem autorização/versão errada), 23 (injeção na consulta), 24 (ID de modelo forjado), 26 (direitos indeterminados no pacote); ADV-13/17/18(a)/19 = revisão/spec-time |
| D9 Auditoria | Por referência | Parcial | cadeia de reconstrução incl. `seal_consumption`; observabilidade = SPEC-040 (seção m-08) |

**PASS (estrutural).**

## 2. BASpecs + Classe/Mecanismo (CC-11)

20 BASpecs com QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR + CLASSE/MECANISMO/CRITÉRIO 4Es.
- **D:** 001, 003, 005, 008, 011, 012, 015, 016, 017.
- **C (com GATE DE SAÍDA):** 002, 007, 009, 014, **019 (CIM), 020 (ato)**.
- **H (com BOUNDED LOOP + GATE DE SAÍDA):** 004, 006, 010, 013, **018 (redator — N-05)**.
- Casos de negação por BASpec: ver Bloco A do Plan (KFH-016 → ADV-25; v1.0 apontava ADV-12, que testa KFH-012 — retirado, m-12).
**PASS.**

## 3. EARS

20 critérios "Quando <condição>, o pipeline/gate/CIM DEVE <resposta>", cada um com `(KFH-0NN)`. **PASS.**

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 EC em todo efeito | ✔ EC-KFH-001..013 (v1.2: EC-011 CIM, EC-012 ato de autorização, EC-013 etapas da consulta — N-04/N-03/N-05) |
| ENF-02 nível ≥ piso | ✔ entrega do pacote = E2; selo, guard de validade/sucessão, formação sem efeito, guard de namespace, CIM, liberação por ato, consulta sem efeito = E3; WikiRAG = E1; registro de fonte = E2 (a LIBERAÇÃO de direitos/envio saiu do EC-001 para o EC-012, E3 — N-04 (2)) |
| ENF-03 Detector ≠ Gate | ✔ juízos H propõem; gates D/C decidem; auditoria amostral de selos = Detector (gera pedido, não revoga) |
| ENF-04 fail-closed | ✔ incl. os intervalos das decisões abertas novas |
| ENF-05 | ✔ RULE-KFH-017 |
| ENF-06 E0 | N/A |
| ENF-07 falso-DENY E3 | ✔ amostral (limiar = gap aberto) |
| E3 rollback/audit (atomic-spec §10.2) | ✔ EC-KFH-004: compensação por `seal_revocation_request` → ato autorizado → novo registro; detecção amostral (m-09) |
| ENF-08 escala | ✔ seção própria "Escala E0–E3" (m-09) |

**PASS.**

## 5. Constitution Check (CC-01..CC-12)

CC-01, CC-02 (selo = interface; `publication.seal_ref` preenche campo que a SPEC-006 deixou à SPEC-007; verificação do lado do KG = errata proposta, não editada; tipo de nó não decidido — fail-closed), CC-03, CC-04, CC-05, CC-06/07 N/A, CC-08, CC-09 (INDETERMINADO; hash ≠ qualidade; risco residual declarado em ADV-03/23), CC-10, CC-11, CC-12 N/A. **PASS.**

## 6. Herança obrigação-a-obrigação (§7-bis Bloco B) — reavaliada (m-12)

| Obrigação herdada | Evidência no Plan v1.2 (v1.1 + acréscimos) | Estado |
|---|---|---|
| RULE-CKG-004 — validade de relação nunca automática/cascata | estendida LOCALMENTE (m-01) em RULE-KFH-008/009; EC-005/006; T15; ADV-07 | ✔ |
| RULE-CKG-005 — computed_by ≠ writer_id | RULE-KFH-007; EC-004; T10 | ✔ |
| RULE-CKG-008 — campos de CAUSA/SIMILAR_A | RULE-KFH-007 (vii) | ✔ |
| RULE-CKG-009 — escritor do KG autorizado | respeitada na escrita; lista de emissores do selo = regra LOCAL análoga (m-02) | ✔ (quem mantém a lista: Aberto) |
| RULE-CKG-010 (b) / RULE-CKG-001 (vi) / l.1415 `seal_ref` | INV-KFH-01; RULE-KFH-007 (iv)/(vii)–(ix); T10/T13; ADV-01/21 | ✔ (verificação pelo committer do KG: errata proposta — Aberto) |
| RULE-CKG-012 — sucessão com supersedes/version+1/expected_version | RULE-KFH-009 (a); D4.4; T23; ADV-22 | ✔ na forma; **quem autoriza = Aberto (SPEC-007-SUCC-001; no intervalo, Andraus)** *[v1.0 tinha ✔ sem esses campos — retirado, m-12]* |
| RULE-CKG-011/013 | RULE-KFH-010 (d); RULE-KFH-016 + ADV-25 | ✔ |
| SPEC-004 RULE-CBP-002/004/014 | RULE-KFH-012; EC-007; KFH-006 (IDs do runtime) | ✔ na forma; **object_type = Aberto (SPEC-007-BBTYPE-001; M-001 aberta)** |
| CEM-001 / INV-06 / INV-10 | RULE-KFH-012 | ✔ |
| CHM-001 (nomes de estado) | D5 `KC_*` | ✔ |
| INV-04 / CCM-001 | RULE-KFH-014; EC-008 | ✔ |
| SPEC-020 dimensão B | F1/F2 (objeto da F2 definido — M-06) + emenda proposta | ✔ (emenda: Aberto, ato de Andraus) |
| RULE-004 / RULE-MET-01 | RULE-KFH-011; COL-EXP-05; RULE-KFH-006 (ID ≠ independência de erro — n-11) | ✔ |
| SPEC-006 l.1410 (chave natural) / RULE-CKG-008 l.443-445 (núcleo causal) | RULE-KFH-007 (vii) — n-01/n-10; ADV-22(e)/(f) | ✔ |
| SPEC-004 RULE-CBP-005 (idempotência) / l.1044 / l.1065 | RULE-KFH-012 VOCABULÁRIO/ENTREGA (n-06/n-09) | ✔ na forma; publicação no Blackboard só após SPEC-007-BBTYPE-001 (Aberto) |
| RULE-BB-001 (RULES.md l.309) | RULE-KFH-012 ENQUADRAMENTO — [INFERÊNCIA] (n-08) | Aberto (confirmação em SPEC-007-BBTYPE-001) |

REMOVED vazio; MODIFIED vazio.

## 7. Notas da abertura (R3-01..R3-07)

| Nota | Verificação |
|---|---|
| R3-01 | Carimbo: aviso ajustado — 8.1/8.3 decidem parte de SPEC-006 l.482 **se estendidas** aos escritores do KG; K-001 aberta. ✔ |
| R3-02 | "Já normativo" (RULE-CKG-009, escritores do KG) × "local nova" (lista de emissores do selo — A-bis, m-02) × "em aberto". ✔ |
| R3-03 | Benchmark: origem por ideia; B8 declarado documento datado de revisão (m-07). ✔ |
| R3-04 | P-1..P-11 (P-4 dividida em P-4a/P-4b — n-13) sem número de Spec no corpo; notas técnicas separadas. ✔ |
| R3-05 | Texto anterior preservado integral (Anexo + colchetes locais). ✔ |
| R3-06 | COL-EXP-05 `[PROPOSTA]`. ✔ |
| R3-07 | INV-KFH-02 = "não vira efeito", agora nas duas trilhas (M-05). ✔ |

## 8. Backlog — [STRUCT-13]

| BL | Linha do Plan com `Disposição:` | Valor |
|---|---|---|
| BL-010 | Nota de gate | PARCIAL |
| BL-017 | Nota de gate | PARCIAL |
| BL-035 | Nota de gate | REFERÊNCIA |
| BL-011 | Nota de gate + COL-EXP-05 | PARCIAL [PROPOSTA]; segue `ATIVADO` |
| BL-029 (m-11) | Nota de gate (menção, não vinculado) | sem disposição; painel diz `Em espera` (l.136) — divergência com o parecer registrada |

`backlog_triggers --abertura SPEC-007`: 3 vinculados (rodado pelo Orquestrador na rodada 1 — m-10b). Nenhum item promovido nem encerrado.

## 9. CONS-01

G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção (como), livro (Q7c): abertas. Novas [DECISÃO NECESSÁRIA] (não fechadas; fail-closed no intervalo): SPEC-007-NODETYPE-001, SPEC-007-SUCC-001, SPEC-007-RIGHTS-001, SPEC-007-EXTTX-001, SPEC-007-BBTYPE-001, **SPEC-007-ACTREC-001, SPEC-007-DERIVTX-001** (v1.2), corte de alto impacto, lista de emissores/juízo, sinalização de dependentes (lacuna). A RULE-KFH-020 só REPRESENTA atos; não cria autoridade nem diz quem decide. A regra provisória "ontologia vigente ∖ canônicos" (que decidia de fato o tipo de nó — M-03) foi retirada. **PASS (a confirmar por STRUCT-10).**

## 10. Integridade de fontes

- Âncoras do SOT conferidas nesta sessão: SPEC-006 `plan.md` l.395-413, 443-445, 474-589, 556-567, 976, 1395-1462 (l.1410, l.1415); SPEC-004 `plan.md` l.224-227, 239-246, 249-254 (CBP-005), 311-319, 1040-1047 (l.1044), 1055-1074 (l.1065); RULES.md l.309 (RULE-BB-001); research.md l.214 (dono das métricas); SPEC-002 l.170; SPEC-020 l.116/144/720/728; RULES.md l.36, 521-538, 656-705; CONFLICT-MAP l.139-147; MC-RAG-001 l.70-110, 497-500; CAMADA MEMÓRIA l.902-904; RMR-001 l.117-118, l.136; ROADMAP l.34/36/37/179-182; research §5.2 (B1/B3/B6/B8/B10).
- **Benchmark:** clone ausente nesta sessão. As 7 citações `inteligencia-sot@0abd22e:…` do Plan (B1 ×2, B3, B6, B8, B10, + NOTICE) vêm **só** do Dossiê (research §5.2); nenhuma nova foi acrescentada e nenhuma foi reconferida por mim; dependem do adendo G3 da guarda pós-revisor. Nada copiado.
- **Fora do meu escopo de edição (m-12, 2ª parte):** o cabeçalho da SPEC-006 ainda diz "1.12 (ERRATA PROPOSTA …)" na linha Versão, embora a linha Status registre a homologação (DHR-SPEC006-004). Registrado para o Orquestrador/Andraus; não editado (só `specs/features/SPEC-007/`).

## 11. Gates (a rodar pelo Orquestrador — sem Bash nesta sessão)

`python scripts/validate_spec_sot.py specs/features/SPEC-007/plan.md` · `python scripts/revisor_gate.py specs/features/SPEC-007/plan.md --rapido` · `python scripts/check_invariants.py specs/features/SPEC-007/plan.md` · `python scripts/check_refs.py` · `python scripts/check_doc_sync.py` · `python scripts/check_repo_research.py --all` · `python scripts/backlog_triggers.py --abertura SPEC-007` · `python scripts/build_map.py --check`.

---

*VERIFY interno = feedback. Não é CONFORME nem homologação.*
