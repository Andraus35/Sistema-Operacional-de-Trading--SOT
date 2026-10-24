# checks.md — Verificação de Spec da SPEC-007 (fase spec-first)

**Objeto:** `specs/features/SPEC-007/plan.md` **v2.0 (CANDIDATA — Plan reduzido: formação + selo; DHR-SPEC007-002, Opção C; aguarda Revisor rodada 4, por delta contra o commit da v1.2, e homologação de Andraus)** (RAG / WikiRAG / Knowledge Formation Harness). *[v1.2: "v1.2 (CANDIDATA — correção da rodada 2 do Revisor; aguarda rodada 3 por delta e homologação de Andraus)"; v1.1: "v1.1 (CANDIDATA — correção da rodada 1 do Revisor; aguarda rodada 2 por delta e homologação de Andraus)"; v1.0: "v1.0 (CANDIDATA — aguarda Revisor integral e homologação de Andraus)"]*
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — **NÃO** é teste de runtime, **NÃO** é parecer do Revisor, **NÃO** é homologação. "VERIFY" interno = feedback. [FONTE: atomic-spec §14]
**Método:** atomic-spec.md v1.5 · tlc-spec-lean (PLAN = Spec; CHECKS = verificação de spec) · overlay GUS-TLC-001
**Data:** 2026-10-24 (v2.0); 2026-10-23 (v1.0, v1.1 e v1.2)
**Ordem de Andraus:** chat 2026-10-24, "Plan reduzido da SPEC-007" (transmitida pelo Orquestrador).
**Pareceres tratados:** R1 (NÃO CONFORME — 9 Médias; v1.1); R2 (NÃO CONFORME — 5 Médias; v1.2); **R3** `governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R3-2026-10-24.md` (NÃO CONFORME — 5 Médias R3-M1..R3-M5, 6 Menores r3-n1..r3-n6; v2.0). Atas incorporadas: DHR-SPEC007-002 (divisão), DHR-SPEC007-003 (P-1..P-11).
**Contagens declaradas (por cabeçalho/linha em coluna 0 — recontadas por busca nesta sessão; a reconferir no ambiente pai):** **12** RULE-KFH (`^RULE-KFH-`: 001–009, 016, 019, 020), 2 INV-KFH, **12** BASpec (`^### BASpec-KFH-`), **12** EARS (`^N. (KFH-`), **9** EC (`^### EC-KFH-`: 001–006, 010, 011, 012), **18 cenários** (`^### Cenário-KFH-T`: T01–T15, T23, T24, T25), **22 ADV** (`^### ADV-KFH-`: 01–05, 07, 08, 13, 16–22, 24, 25, 27, 28, 30, 31, 32). *[v1.2: vinte/2/vinte/vinte/treze/vinte e seis/vinte e nove; v1.1 e v1.0 no Anexo]* Os Anexos T, R e H do Plan são recuados ou estão em bloco de código: não contam.

> **Natureza dos ✔ abaixo:** estruturais e condicionados. O que depende de Andraus aparece como "Aberto"; as decisões da DHR-SPEC007-003 aparecem como "decidida (DHR-SPEC007-003) — normativa na homologação"; os positivos de selo dependem da **Fixture F0** (estado injetado, D7), que não afirma que esse estado já exista.

---

## R3 — verificação das correções (R3-M1..R3-M5)

| Média | Âncora no Plan v2.0 | Positivo / negativo | Estado |
|---|---|---|---|
| R3-M1 pré-condições por cenário | D7 "Fixture F0" (F0.1–F0.5); RULE-KFH-007 "ORDEM"; D4.2 ordem fixa; cada cenário/ADV de selo "F0, exceto …" quebrando **um** passo | T10 / T11, T12(a)(b)(c), T13, T14, ADV-18(b), ADV-21, ADV-22, ADV-30, ADV-31 | ✔ estrutural (teste por passo com estado injetado) |
| R3-M2 `material_hash`/`record_hash` | RULE-KFH-005 "SERIALIZAÇÃO ÚNICA" (M, canon, `record_hash`, `material_hash`); RULE-KFH-004 (candidato sem texto de registro); RULE-KFH-007 (ii) (pedido sem registros; `sealed_records` derivada) e (ix) (materialização pelo pipeline; campos de publicação fora do hash); D4.3 novo; contrato | D4.3 exemplo / ADV-30 (a)(b)(c), ADV-21(a)(d) | ✔ estrutural; KG-side = errata E-3 **proposta** (RU-3 declarado) |
| R3-M3 linha parada consolidada | seção "Pré-requisitos mínimos para a 1ª fonte publicada" (linguagem de trader; ordem 1→2→3→4(→5)); Roteamento corrigido ("linha inteira parada"); frase "nem chega aos analistas" restaurada | — | ✔ |
| R3-M4 rótulo de impacto | RULE-KFH-004 "CLASSIFICAÇÃO"; RULE-KFH-005 (e) e `material_hash` com `knowledge_kind`/`target_node_type`; RULE-KFH-006 eixo `KIND_MISCLASSIFIED`; RULE-KFH-007 (v); RU-4; auditoria amostral (EC-004 (iii)) | T14 / ADV-31 (a)(b)(c) | ✔ estrutural; risco residual RU-4 declarado |
| R3-M5 envelope da CIM | RULE-KFH-019 (f) (f1–f4); D4.5 novo; contrato `model_invocation_record`, `provider_registry`, `instruction_template`; EC-KFH-011 | T25 / ADV-32 (a)–(d), ADV-28 (a')(c)(d) | ✔ estrutural; parte "entrega a consumidor" vai à SPEC-048 (Anexo T) |

| Menor | Âncora | Estado |
|---|---|---|
| r3-n1 | RULE-KFH-007 entradas (A)/(B), (vii-bis), (viii); D4.2 passo (8); contrato `seal_consumption` | ✔ |
| r3-n2 | D4.4; T15 | ✔ |
| r3-n3 | RULE-KFH-007 (vii); D4.2 (5-bis); ADV-22(g) | ✔ |
| r3-n4 | D1 "S1–S10"; §7-bis Bloco A "(12 vigentes)" | ✔ |
| r3-n5 | (a)(b)(d) RULE-KFH-020; (c) RULE-KFH-019 (b) registro de provedores | ✔ (forma de confirmar a identidade = BUILD, Aberto) |
| r3-n6 | vai com o pacote à SPEC-048 (P-9 decidida) — Anexo T, nota de pendências | transferido |

## DHR-SPEC007-002 / DHR-SPEC007-003 — verificação de incorporação

| Item | Verificação | Estado |
|---|---|---|
| Fronteira §3 da divisão | tabela "Mapeamento v1.2 → v2.0" decide RULE a RULE e BASpec a BASpec; tudo que saiu está intacto no Anexo T; IDs transferidos não reutilizados | ✔ |
| "Usa a trava, não a redefine" | INV-KFH-02 e RULE-KFH-019 "INTERFACE COM A SPEC-048"; seção "Interface com a SPEC-048" (I-1..I-6) | ✔ |
| SPEC-048 não aberta | nenhum arquivo criado fora de `specs/features/SPEC-007/`; requisitos à SPEC-048 = `[PROPOSTA]` não vinculante | ✔ |
| ACTREC / RIGHTS / EXTTX / DERIVTX / NODETYPE / SUCC | "decidida (DHR-SPEC007-003)" em RULE-KFH-020 / 001 / 019 (b) / 019 (c) / 007 (iv-bis) / 009 (a) | ✔ (normativa só na homologação) |
| P-1 / P-2 | RULE-KFH-006 (independência e ponto separado como regra); RULE-KFH-007 (iii) ato ISSUER_LIST; (v) corte definição/regra | ✔; parte de SPEC-006 l.482 → errata **proposta** (E-1) |
| BBTYPE (P-9) | só no Anexo T (destino SPEC-048) | ✔ |
| P-5 / P-6 | emenda à SPEC-020 só metade F1; COL-EXP-05: definição de origem-raiz aqui, contagem na SPEC-048 (P-14) | ✔ (P-14 aberta) |
| Livro (Q7c) | fora (Non-goals; RULE-KFH-001 ALCANCE; quadro de pré-requisitos) | ✔ |
| Seguem abertas | K-001, M-001, G-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção, forma de confirmar a identidade, host do juízo CKG-008, SPEC-007-LOCUS-001 (nova) | Aberto |

---

## 0. Consolidação (fonte única de regra)

| Verificação | Resultado |
|---|---|
| Cada regra vigente definida UMA vez em D2 (RULE-KFH-001..009, 016, 019, 020; INV-KFH-01/02); texto v1.2 das reescritas no Anexo R (R.5); transferidas no Anexo T (T.1); v1.0/v1.1 nos anexos próprios | ✔ |
| EARS prefixados pela regra-fonte `(KFH-0NN)` | ✔ (12) |
| BASpecs dizem "Aplica RULE-KFH-0NN" + REFERÊNCIA | ✔ (12) |
| D4/D5/D6/EC/D7/D8/Herança referenciam por ID | ✔ |
| Regras da SPEC-006 citadas por ID+linha, não recopiadas nem alteradas (CC-02) | ✔ (RULE-CKG-004/005/008/009/010/011/012/013; l.453-454; l.976; l.1405; l.1410; l.1415) |
| Serialização única definida uma vez (RULE-KFH-005) e só referenciada (RULE-KFH-007/020; D4.3) | ✔ |

## 1. Cobertura de profundidade (D0–D8 — CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (formação + selo) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S10 + Non-goals (SPEC-048, livro Q7c, `rag/` GEN-1, Benchmark) |
| D2 Regra | Sim | ✔ | 12 RULE-KFH + INV-KFH-01/02 [PROPOSTA] |
| D3 Comportamento | Sim | ✔ | 12 BASpecs; §D3.1 (novos: `TARGET_NODE_TYPE_FORBIDDEN`, `KIND_MISCLASSIFIED`, `INVOCATION_ENVELOPE_INVALID`, `CONTENT_PROVENANCE_MISSING`, `AUTH_IDENTITY_UNAVAILABLE`, `OUT_OF_SCOPE_048`) |
| D4 Algoritmo | Determinísticos/semi | ✔ | D4.1 literal; D4.2 selo (entradas A/B, fail-fast, atômico); D4.3 serialização (novo); D4.4 marca; D4.5 envelope CIM (novo) — todos com exemplo |
| D5 Estado | Sim | ✔ | `KC_*`; M-001 aberta |
| D6 Protocolo | Sim | ✔ | formação (com passo 0 de pré-requisitos); chamadas de modelo; atualização (SUCCESSION/INVALIDATION); contradição |
| D7 Teste | Sim | ✔ (positivos condicionados à Fixture F0) | T01–T15, T23, T24, T25 |
| D8 Adversarial | Sim | ✔ | 22 ADV; novos ADV-30 (R3-M2), ADV-31 (R3-M4), ADV-32 (R3-M5); ADV-07 (caso D8 da RULE-CKG-004) mantido; ADV-13/17/18(a)/19 = revisão/spec-time |
| D9 Auditoria | Por referência | Parcial | cadeia item→selo→atos→validação→candidato→unidade→fonte; invocações; observabilidade = SPEC-040 |

**PASS (estrutural).**

## 2. BASpecs + Classe/Mecanismo (CC-11)

12 BASpecs com QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR + CLASSE/MECANISMO/CRITÉRIO 4Es.
- **D:** 001, 003, 005, 008, 016.
- **C (com GATE DE SAÍDA):** 002, 007, 009, 019 (CIM), 020 (ato).
- **H (com BOUNDED LOOP + GATE DE SAÍDA):** 004, 006.
- Casos de negação por BASpec: §7-bis Bloco A do Plan (12 vigentes).
**PASS.**

## 3. EARS

12 critérios "Quando <condição>, o pipeline/gate/CIM DEVE <resposta>", cada um com `(KFH-0NN)`. **PASS.**

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 EC em todo efeito | ✔ EC-KFH-001..006, 010, 011, 012 (EC-007/008/009/013 e a parte "feedback" do EC-010 foram à SPEC-048 — Anexo T) |
| ENF-02 nível ≥ piso | ✔ registros operacionais E2 (001, 003, 005, 010); formação sem efeito, selo, guard de validade, CIM, ato = E3 |
| ENF-03 Detector ≠ Gate | ✔ juízo H propõe; gates D/C decidem; auditoria amostral (EC-004 (i)–(iii); EC-011) = Detector (gera pedido, não revoga) |
| ENF-04 fail-closed | ✔ incl. identidade indisponível, lista de emissores vazia sem ato, nenhum executor LOCAL enquanto SPEC-007-LOCUS-001 aberta |
| ENF-05 | ✔ (feedback foi à SPEC-048; aqui nenhuma política é alterada por evento do pipeline) |
| ENF-06 E0 | N/A |
| ENF-07 falso-DENY E3 | ✔ amostral (limiar = gap aberto) |
| E3 rollback/audit (atomic-spec §10.2) | ✔ EC-KFH-004: compensação por `seal_revocation_request` → ato INVALIDATION de Andraus → novo registro pelo KG |
| ENF-08 escala | ✔ seção própria "Escala E0–E3" (E1 vazio nesta Spec, declarado) |

**PASS.**

## 5. Constitution Check (CC-01..CC-12)

CC-01 (só `learning`; nunca hipótese), CC-02 (selo = interface; ontologia não estendida; erratas só propostas), CC-03 (nenhum escore produzido aqui; J-001/N-001 abertas), CC-04, CC-05, CC-06/07 N/A, CC-08 (inclui nota de obrigações que acompanham comportamento transferido), CC-09 (INDETERMINADO; RU-1..RU-6), CC-10, CC-11 (pisos E2/E3), CC-12 N/A. **PASS.**

## 6. Herança obrigação-a-obrigação (§7-bis Bloco B)

| Obrigação herdada | Evidência no Plan v2.0 | Estado |
|---|---|---|
| RULE-CKG-004 — validade nunca automática/cascata | RULE-KFH-008/009; EC-005/006; T15; ADV-07 (caso D8) | ✔ |
| RULE-CKG-005 — computed_by ≠ writer_id | RULE-KFH-007; EC-004; T10 | ✔ |
| RULE-CKG-008 — campos de CAUSA/SIMILAR_A; núcleo causal; chave de relação | RULE-KFH-007 (vii); ADV-22(f)(g) | ✔ |
| RULE-CKG-009 — escritor do KG autorizado | respeitada na escrita; lista de emissores do selo = regra local aprovada por Andraus (P-1) | ✔ (l.482: parte decidida em ata → errata proposta; host do juízo CKG-008: Aberto) |
| RULE-CKG-010 (b) / RULE-CKG-001 (vi) / l.1415 `seal_ref` | INV-KFH-01; RULE-KFH-007 (iv)/(viii)/(ix); T10/T13; ADV-01/21/30 | ✔ (verificação pelo committer: errata E-3 proposta — Aberto) |
| RULE-CKG-011 — read-only | gatilho de sucessora | ✔ (forma "recuperação read-only" → SPEC-048) |
| RULE-CKG-012 — sucessão | RULE-KFH-009 (a); D4.4; T23; ADV-22 | ✔ (quem autoriza: decidida — P-8) |
| RULE-CKG-013 — contradição | RULE-KFH-016; ADV-25 | ✔ |
| SPEC-004 RULE-CBP-014 | identidade do runtime em KFH-001/006/007; princípio estendido localmente à identidade humana (KFH-020) | ✔ (forma de confirmar: BUILD — Aberto) |
| CHM-001 (nomes de estado) | D5 `KC_*` | ✔ |
| INV-04 / CCM-001 | nenhum escore produzido; nenhum campo de convicção no contrato | ✔ |
| SPEC-020 dimensão B | F1 + emenda metade F1 proposta | ✔ (ato de Andraus na homologação) |
| RULE-004 / RULE-MET-01 | origem-raiz (RULE-KFH-001); "IDs ≠ independência de erro" (RULE-KFH-006) | ✔ |
| Obrigações que acompanham comportamento transferido (CBP-002/004/005, RULE-BB-001, CEM-001 na forma "pacote", INV-04 na forma "relevância", RULE-004 na forma "contagem no pacote") | nota em "Herança / Delta"; evidência v1.2 no Anexo T | Transferidas com o comportamento (DHR-SPEC007-002) — não suprimidas |

REMOVED vazio; MODIFIED vazio.

## 7. Notas da abertura (R3-01..R3-07)

| Nota | Verificação |
|---|---|
| R3-01 | cumprida pela ata DHR-SPEC007-003 (P-1 decide parte de l.482); errata E-1 proposta; K-001 aberta. ✔ |
| R3-02 | Carimbo A / A-bis / B (decidido) / C (aberto). ✔ |
| R3-03 | Benchmark: origem por ideia; nada copiado; 7 citações não reconferíveis (clone ausente). ✔ |
| R3-04 | P-12..P-14 sem número de Spec no corpo; notas técnicas separadas; quadro de pré-requisitos em linguagem de trader. ✔ |
| R3-05 | colchetes integrais ou apontando para texto integral no Anexo R/T. ✔ |
| R3-06 | COL-EXP-05 `[PROPOSTA]`. ✔ |
| R3-07 | INV-KFH-02 = "não vira efeito". ✔ |

## 8. Backlog — [STRUCT-13]

| BL | Linha do Plan com `Disposição:` | Valor |
|---|---|---|
| BL-010 | Nota de gate | PARCIAL (formação/selo aqui; recuperação/pacote → SPEC-048) |
| BL-017 | Nota de gate | PARCIAL (F1 aqui; F2 na SPEC-048 — DHR-SPEC007-002) |
| BL-035 | Nota de gate | REFERÊNCIA |
| BL-011 | Nota de gate + COL-EXP-05 | PARCIAL [PROPOSTA] (P-6 aceita); segue `ATIVADO` |
| BL-029 | Nota de gate | REFERÊNCIA [PROPOSTA] (voluntária; não vinculado; `Em espera`) |

`backlog_triggers --abertura SPEC-007`: a reconferir pelo Orquestrador na v2.0 (3 vinculados nas rodadas anteriores). Nenhum item promovido nem encerrado.

## 9. CONS-01

Abertas (não usadas como invariante fechado): G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção (como), livro (Q7c), forma de confirmar a identidade de Andraus, host do juízo CKG-008, sinalização de dependentes (lacuna), **SPEC-007-LOCUS-001** (nova; fail-closed: nenhum executor LOCAL). Decididas como política (DHR-SPEC007-003) e tratadas como "decidida — normativa na homologação": ACTREC, RIGHTS, EXTTX, DERIVTX, NODETYPE, SUCC, P-1/P-2. **PASS (a confirmar por STRUCT-10).**

## 10. Integridade de fontes

- Âncoras conferidas nesta sessão: ROADMAP l.179-189 (nota de divisão; slot SPEC-048), l.517; SPEC-006 `plan.md` l.420-489 (RULE-CKG-007..010; núcleo causal l.443-445; chave de relação l.453-454; l.482), l.1400-1419 (l.1405 node_type; l.1410 natural_key; l.1415 publication/seal_ref); SPEC-004 `plan.md` l.311-319 (RULE-CBP-014); DHR-SPEC007-002; DHR-SPEC007-003; pareceres R1/R2/R3. Demais âncoras herdadas da v1.2 (conferidas naquela sessão; ver Anexo).
- **Benchmark:** clone ausente. As 7 citações `inteligencia-sot@0abd22e:` vêm só do Dossiê (research §5.2); nenhuma nova; nenhuma reconferida; nada copiado.
- **Contagens históricas** em texto preservado (Anexos R/T/H e colchetes) não são contagens vigentes; aviso do detector `contagens_declaradas` sobre elas = histórico (ver HANDOFF §3).
- **Fora do meu escopo de edição:** cabeçalho da SPEC-006 ("1.12 ERRATA PROPOSTA"); erratas à SPEC-006/SPEC-020 (só propostas no Plan); CONFLICT-MAP (COL-EXP-05).

## 11. Gates (a rodar pelo Orquestrador — sem Bash nesta sessão)

`python scripts/validate_spec_sot.py specs/features/SPEC-007/plan.md` · `python scripts/revisor_gate.py specs/features/SPEC-007/plan.md --rapido` · `python scripts/check_invariants.py specs/features/SPEC-007/plan.md` · `python scripts/check_refs.py` · `python scripts/check_doc_sync.py` · `python scripts/check_repo_research.py --all` · `python scripts/backlog_triggers.py --abertura SPEC-007` · `python scripts/build_map.py --check`.

---

*VERIFY interno = feedback. Não é CONFORME nem homologação.*

---

## Anexo — checks.md v1.2 preservado (INV-07; integral; recuado 4 espaços)

```text
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
```
