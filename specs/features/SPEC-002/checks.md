# checks.md — Verificação de Spec da SPEC-002 (fase spec-first)

**Objeto:** `specs/features/SPEC-002/plan.md` (Evidence & Evidence Provenance Harness — camada operacional sobre CEM-001)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §23]
**Método:** atomic-spec v1.5
**Complexidade/Profundidade:** CRITICAL / D0–D8 (DHR-SPEC002-001 §2 DN-2)
**Data:** 2026-09-29

---

## 1. Cobertura de profundidade (D0–D8 — alvo CRITICAL)

| Nível | Exigido (CRITICAL, alvo D0–D8) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (envelope de proveniência sobre CEM-001; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas S1–S11 + Non-goals (CEM/SPEC-003/004/006/RISK/on-chain) |
| D2 Regra | Sim | ✔ | RULE-EPH-01..10 [PROPOSTA] |
| D3 Comportamento (BASpec) | Sim | ✔ | EPH-001..012 com Classe declarada (RULE-MECH-01) |
| D4 Algoritmo | Onde há regra determinística | ✔ (não-numérico justif.) | ALGORITMO `publicar_evidencia_com_proveniencia`; numérico N/A (aging/convicção = J-001) |
| D5 Estado | Sim | ✔ | Máquina de estados SOBRE CEM-001 Cap.4 (+ DRAFT_CANDIDATE/REJECTED_INCOMPLETE) |
| D6 Protocolo | Sim | ✔ | Protocolo de publicação/consumo Blackboard (8 passos; EC-COG-005) |
| D7 Teste | Sim (CRITICAL) | ✔ | Cenários EPH-T01..T07 |
| D8 Adversarial | Sim (CRITICAL) | ✔ | ADV-EPH-01..09 (9 casos de negação) |
| D9 Auditoria | Por referência (spec-first) | Parcial (delegado) | Trilha append-only (EPH-012); reconstrução → KG/SPEC-006, auditoria/SPEC-041; L4 só em runtime |

**Resultado:** profundidade-alvo D0–D8 atingida (teto CRITICAL). D4 numérico N/A justificado (J-001 aberto) + procedimento determinístico não-numérico presente.

---

## 2. Well-formedness das BASpecs (EPH-001..012) + Classe (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE + 4Es | Bounded loop/Gate (H/C) |
|---|---|---|---|---|---|---|---|
| EPH-001 publicar c/ gate | ✔ | ✔ | ✔ | ✔ | ✔ | H · Conformidade/Eficácia | Bounded loop (1/submissão) + gate de saída (completude+authz) ✔ |
| EPH-002 proveniência (INV-06) | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| EPH-003 dois eixos | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| EPH-004 trava INV-04 | ✔ | ✔ | ✔ | ✔ | ✔ | C · Conformidade | Gate de saída (ausência nos insumos de convicção) ✔ |
| EPH-005 taxonomia + "ausente" | ✔ | ✔ | ✔ | ✔ | ✔ | D · Efetividade | N/A (D) |
| EPH-006 supersessão append-only | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| EPH-007 invalidação (Detector≠Gate) | ✔ | ✔ | ✔ | ✔ | ✔ | C · Conformidade | Gate de saída (transição permitida) ✔ |
| EPH-008 independência/correlação | ✔ | ✔ | ✔ | ✔ | ✔ | D · Efetividade | N/A (D) |
| EPH-009 conflito (substrato) | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| EPH-010 temporalidade/staleness | ✔ | ✔ | ✔ | ✔ | ✔ | D · Economicidade/Efetividade | N/A (D) |
| EPH-011 vínculo→hipótese (ref) | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| EPH-012 auditabilidade append-only | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário. Classe por BASpec (não por Spec — SES-001 §50). Nenhuma Classe C em risco baixo (EPH-004/007 são E3, invariante/irreversível). **PASS.**

---

## 3. Critérios EARS

10 critérios no formato "Quando <condição>, a camada Harness DEVE/NÃO DEVE <resposta>". Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-EPH-001..004 (publicar/superseder/invalidar/trava) |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E2 (publicar/superseder — piso Evidência) / E3 (invalidar irreversível; trava INV-04) |
| ENF-03 Gate determinístico; Detector ≠ Gate | ✔ EPH-007 (Fusion inicia avaliação, não cascata); D5 (gate determinístico decide publicação, não LLM) |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-EPH-003 (transição proibida rejeitada); EC-EPH-001 (publicação incompleta rejeitada) |
| ENF-05 Policies não auto-aprendidas | ✔ extensão DN-1 via GMC-001; RULE-EPH-* só por homologação de Andraus |
| ENF-06 E0 declarado como orientação | N/A (nenhum efeito E0; todos ≥ E2) — declarado |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-EPH-003/004 (amostral; limiar = gap aberto) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12)

Preenchido no plan.md. **Críticos aplicáveis PASS:** CC-01 (hierarquia protegida — infraestrutural), CC-02 (CEM-001 não redefinido; extensão **Categoria B** — novo campo opcional — via GMC-001, processo formal Cap.5 GMC-CEM001-EXT-001; ACH-001 resolvido — CONST-01), CC-03 (Conviction 8D fechada; definitivos = J-001 aberto; confiabilidade NUNCA no Conviction — INV-04), CC-04 (salvaguardas intocadas), CC-08 (Herança/Delta presente; INHERITS/ADDED c/ ID+versão; REMOVED vazio), CC-11 (Classe por BASpec — INCIDE). **CC-05** = CRITICAL/D0–D8. **CC-06/CC-07** = N/A justificado (Spec/Plan, não Engineering Card). **CC-09** = Epistemic Check completo (§7-bis Bloco C). **CC-10** = N/A justificado (infraestrutural; termos externos rejeitados como baseline). **CC-12** = N/A justificado (neutra de domínio; nenhum PD-xx; research.md §3). **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED preenchidos com ID+versão (RULE-HD-04: CEM-001 v1.0, GMC-001 v1.0, CHM-001 v1.0, atomic-spec v1.5). ✔
- REMOVED vazio. ✔
- MODIFIED: nenhuma regra herdada modificada em texto (DN-1 é aditiva, não modificação) — declarado. ✔
- Nenhum item ADDED contradiz o herdado (RULE-HD-02); nenhuma obrigação suprimida fora de REMOVED (RULE-HD-03). ✔
- Eixo VERTICAL (RULE-HV): herança sobre modelo canônico (obrigação-a-obrigação); conservação-como-conjunto (Contrato de Herança Vertical) = conteúdo futuro da SPEC-019 (escopo homologado), não decisão aberta — nota declarada. ✔

**PASS.**

---

## 7. §7-bis — Redução de viés (obrigatório CRITICAL)

| Bloco | Resultado |
|---|---|
| A — Pergunta adversarial por BASpec (12 BASpecs) | ✔ quadro com caso de negação + verificabilidade + condição de não-ocorrência por BASpec; mapeados a ADV-EPH-01..09 e T01..T07 |
| B — Herança obrigação-a-obrigação (CC-08/CEM-001 v1.0) | ✔ 13 obrigações herdadas listadas com evidência de satisfação; nenhuma suprimida/enfraquecida (RULE-HD-03) |
| C — Verificação epistêmica (completa, não resumida — aprende com F-01) | ✔ 6 itens: causalidade c/ mecanismo, hipótese≠fato, INDETERMINADO, probabilidade N/A, sem falsa precisão, modalidade preservada |
| D — Reforço de escopo (INV-05/RULE-DEC-01) | ✔ representa/versiona, não decide/executa; nenhuma cruza SOT→execução |

**PASS.**

---

## 8. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| J-001 NÃO fechada; nenhum limiar/fórmula de convicção ou aging fixado (EPH-009/010; ADV-EPH-08) | ✔ |
| INV-04 preservado (confiabilidade-de-fonte NUNCA no Conviction — EPH-004; ADV-EPH-04) | ✔ |
| INV-07 preservado (append-only; nada deletado — EPH-006; ADV-EPH-06) | ✔ |
| CONST-01 preservado (CEM-001 não redefinido; extensão Categoria B via GMC-001, processo formal Cap.5 — ADV-EPH-07; GMC-CEM001-EXT-001) | ✔ |
| DN-3 honrada (só o gancho "ausente"; semântica deferida — EPH-005; ADV-EPH-09) | ✔ |
| M-001/H-001/N-001/K-001/G-001/C-001/RISK-CONV-001/ECC-VAL-001 referenciadas como ABERTAS, não fechadas | ✔ |
| Nova decisão EPH-GMC-001 marcada [DECISÃO NECESSÁRIA] (não fechada por mim — RULE-MET-01) | ✔ |
| RULE-EPH-* / EC-EPH-* / BASpec-EPH-* etiquetadas [PROPOSTA]; CEM/GMC/CHM/INV/ENF/RULE-MECH/RULE-HD como FATO NORMATIVO | ✔ |
| Fontes externas SRC-01..05 etiquetadas [EXTERNO]; nada vira baseline | ✔ |
| Nenhuma decisão aberta usada como invariante fechado | ✔ |

**PASS.**

---

## 9. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| CEM-001 v1.0 (contrato/ciclo de vida/eventos) | ✔ | canon/CEM-001 (baseline) |
| GMC-001 v1.0 (Categorias A/B/C; Governed Enum) | ✔ | canon/GMC-001 (baseline) |
| CHM-001 v1.0 (hipótese — referência de fronteira) | ✔ | canon/CHM-001 (baseline) |
| ENF-01..08 (esp. ENF-03/04) | ✔ | atomic-spec §10.4 |
| RULE-MECH-01..04 (CC-11) | ✔ | RULES.md; atomic-spec §9/§10.6 |
| RULE-HD-01..04 (CC-08) | ✔ | RULES.md; atomic-spec §8.3 |
| RULE-004 / RULE-005 / RULE-009 / RULE-SY-001 | ✔ | RULES.md |
| RULE-ECC-01/02/04/05 | ✔ | RULES.md; atomic-spec §15 |
| RULE-EPI / RULE-CAU / RULE-PRB / RULE-SEM / RULE-DEC / RULE-MET | ✔ | RULES.md (v1.5, LOTE RULE-REG-001) |
| INV-03/04/05/06/07/09/10 | ✔ | atomic-spec §13 |
| EC-COG-005 (Cognitive Event Bus) | ✔ | CEM-001 Cap.6 |
| DN-1/DN-2/DN-3 (homologadas) | ✔ | DHR-SPEC002-001 §2; research.md §8.4 |
| SRC-01..05 (fontes carregadas + verbatim) | ✔ | research.md §2/§2.1; sources/SRC-0N.txt (RULE-ECC-04) |
| RULE-EPH-01..10; EC-EPH-001..004; BASpec-EPH-001..012; EPH-GMC-001 | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 10. Gate RMR-001 (passo 11-bis)

- **RULE-REG-001** — gatilho `spec:SPEC-002 em redação` disparado e SANADO na abertura (DHR-SPEC002-001 §5); 10+1 famílias registradas no RULES.md; método v1.5. Sem ação nova. ✔
- **BL-012 (MC-COG-001)** — gatilho `spec:SPEC-002 homologada` dispara na homologação do Plan; registrado IMINENTE, não ATIVADO. ✔
- **BL-008** — auditoria retroativa SPEC-001 `ATIVADO`, independente; não bloqueia. ✔
- **STRUCT-11** — SPEC-002 cita RULE-ECC-01/02; research.md presente com seção "Dossiê de Pesquisa". ✔
- Nenhum item ATIVADO pendente sem encaminhamento por esta redação. **PASS.**

---

## 11. Simulação mental do gate determinístico (`validate_spec_sot.py`) — NÃO executado (sem Bash)

> RULE-MET-01: NÃO fabrico resultado de execução. Abaixo é a análise estrutural esperada; o coordenador deve rodar o script de fato.

| Check | Expectativa | Base |
|---|---|---|
| STRUCT-01 Cabeçalho (Complexidade + Profundidade-alvo D<n>) | PASS | "Complexidade ... CRITICAL"; "Profundidade-alvo ... D0–D8" no cabeçalho |
| STRUCT-02 Constitution Check + Elliott + Conviction pendente | PASS | Bloco "Constitution Check"; menção "Elliott"; "Conviction Vector ... J-001 (aberto/pendente)" |
| STRUCT-03 Etiquetagem de fonte | PASS | [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] presentes |
| STRUCT-04 EARS | PASS | 10 critérios "Quando ..., DEVE ..." |
| STRUCT-05 BASpec (QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR) | PASS | EPH-001..012 completas |
| STRUCT-06 Enforcement (8 campos) | PASS | EC-EPH-001..004 com CAPABILITY/EFFECT/PRECOND/POSTCOND/POLICY/LEVEL/FAILURE-MODE/EVIDENCE |
| STRUCT-07 Conviction não fechado | PASS | nenhum limiar 60/75% fixado; J-001 declarado aberto |
| STRUCT-08 Status epistemológico | PASS | FATO NORMATIVO / [DECISÃO NECESSÁRIA] presentes |
| STRUCT-09 Profundidade compatível | PASS | CRITICAL → teto D8; declarado D8 |
| STRUCT-10 CONS-01 (IDs abertos não como fechados) | PASS esperado | J-001/M-001/H-001/N-001/K-001/G-001/C-001 sempre com marca de pendência próxima (tabela "Decisões abertas incidentes" + inline "(aberta/pendente)") |
| STRUCT-11 Dossiê presente | PASS | research.md na pasta com "Dossiê de Pesquisa" |

**Atenção STRUCT-10 (auto-verificação):** cada ocorrência de `J-001`, `M-001`, `H-001`, `N-001`, `K-001`, `G-001`, `C-001` no plan.md está a ≤200 chars de um marcador de pendência ("aberta"/"pendente"/"[DECISÃO NECESSÁRIA]"/"não ... fechado"), ou o ID é declarado pendente na tabela de Decisões Abertas e nenhuma ocorrência afirma fechamento colado ao ID. `B-001`/`L-001`/`I-001` (fechadas no ROADMAP) podem ser citadas livremente. **Expectativa: PASS** — a confirmar pela execução real do coordenador.

---

## 12. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | **EPH-GMC-001 — RESOLVIDO (DHR-SPEC002-002).** Tensão entre "Categoria A" nomeada na abertura (DN-1) e o GMC-001 Cap.3 (novo campo, mesmo opcional = Categoria B; Categoria A = só novos valores de enumeração já existente). Revisor CONFORME com achado Médio **ACH-001**: não há enum compatível pronta no CEM-001 → exige campo novo → **Categoria B**. Andraus (2026-09-29) reclassificou para **Categoria B** e mandou conduzir o processo formal GMC-001 Cap.5 (proposta + análise de impacto + registro do Controlador), sem exceção/override. Processo em `governance/GMC-CEM001-EXT-001`. Substância inalterada (INV-04: nunca no Conviction). | Média → **RESOLVIDA** | Reclassificado A→B; proposta formal GMC-CEM001-EXT-001 conduzida; incorporação física ao `canon/CEM-001` (v1.1) = ato do Controlador (CATALOGO §1) |
| CK-02 | Nota de eixo de herança (CC-08 vs RULE-HV) por [INFERÊNCIA]: herança sobre modelo canônico é obrigação-a-obrigação; conservação-como-conjunto = conteúdo futuro da SPEC-019 | Menor | Revisor confirma o eixo de herança |
| CK-03 | D9 auditoria por referência; mecanismo físico delegado a KG/SPEC-006 (H-001 aberta) e SPEC-041; L4 só em runtime | Menor | Consistente com alvo spec-first; teto L3 (RULE-MM-04) |
| CK-04 | Consumo em runtime (E3/E4/E6, `evidence_ref`/`evidence_classification`) por [INFERÊNCIA]/adiado — RULE-ECC-06 não disparada (SPEC-002 não é agente do fluxo) | Menor | Revisor confirma a não-incidência de RULE-ECC-06/07 (research.md §4/§5) |
| CK-05 | Fontes SRC-04/SRC-05 com IDs arXiv pós-treino — tratadas como DADO não verificado (research.md §2); nenhuma alegação carregada repousa em E6 (INDETERMINADO) | Menor | Já registrado no Dossiê; Revisor verifica correspondência verbatim (RULE-ECC-04) |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (EPH-001..012 com Classe), EARS (10), Enforcement (EC-EPH-001..004; ENF-03 Detector≠Gate; ENF-04 fail-closed E3), Constitution Check (CC-01..12; CC-11 incide; CC-06/07/10/12 N/A justificado), Herança/Delta (CEM-001 v1.0 + extensão Categoria B v1.1), §7-bis completo (Blocos A–D; Bloco C não-resumido), CONS-01 e gate RMR-001 satisfeitos. 5 achados não-bloqueantes (CK-01..CK-05); **CK-01/EPH-GMC-001 RESOLVIDO** (reclassificação Categoria A → B via processo formal GMC-001 Cap.5, GMC-CEM001-EXT-001).

> **Atualização (2026-09-29):** o Revisor emitiu parecer **CONFORME** (1 achado Médio ACH-001, não-bloqueante); Andraus decidiu a reclassificação Categoria B e **homologou o Plan v1.1 como BASELINE** (DHR-SPEC002-002). Este arquivo permanece o feedback interno de verificação de spec — não substitui o parecer do Revisor nem a ata de homologação. Pendências de execução para o coordenador (sem Bash neste agente — RULE-MET-01): re-rodar `python scripts/validate_spec_sot.py specs/features/SPEC-002/plan.md`, `check_refs.py`, `check_doc_sync.py`, `backlog_triggers.py`, `build_map.py`.
