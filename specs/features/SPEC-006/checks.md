# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.0 (candidato)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico de armazenamento INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-11

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — alvo ROADMAP §6; CRITICAL)

| Nível | Exigido (CRITICAL, alvo D0–D7 + D8) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar conhecimento permanente; ontologia/entidades/relações/temporalidade/proveniência/lifecycle/confiança/consulta/governança; memória permanente ≠ trabalho; mecanismo físico INDETERMINADO; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas S1–S13 + Non-goals (H-001/SPEC-004/005/007/009/018/CCM/ontologia-componente) |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA]; INV-CKG-01 |
| D3 Comportamento (BASpec) | Sim | ✔ | CKG-001..013, cada uma com bloco CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | Validade temporal (invalidar≠deletar), imutabilidade/lifecycle, dedupe de nó/relação, Cognitive Trace Reconstruction, gate causal, isolamento confiança×convicção |
| D5 Estado | Sim | ✔ | `knowledge_state` (CANDIDATE_WRITE/ACTIVE_KNOWLEDGE/SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED/REJECTED) — lifecycle do nó/relação, separado de CHM-001 e de publication_state/domain_state (SPEC-004) |
| D6 Protocolo | Sim | ✔ | Sequência de escrita (10 passos) sobre conhecimento publicado; fronteiras SPEC-004 (trabalho)/SPEC-005 (transporte)/SPEC-007 (formação) |
| D7 Teste | Sim (CRITICAL; ≥3 cenários) | ✔ | Cenários CKG-T01..T11 (11 — inclui temporalidade/T03, deleção-proibida/T05, confiança≠convicção/T06, causal/T07, governança E3/T08, trace/T10, colisão/T11) |
| D8 Adversarial | Sim (CRITICAL — focado nos pontos sensíveis) | ✔ | ADV-CKG-01..10 (deleção disfarçada, sobrescrita silenciosa, confiança→convicção, causal pós-hoc, custo→convicção, sem proveniência, produtor redefine ontologia, formação no KG, fechar H-001, absorver vizinhos) |
| D9 Auditoria | Por referência | Parcial (por referência) | Nó/relação reconstruível (tipo/ref canônica/proveniência/validade/supersessão); Cognitive Trace Reconstruction especificada (CKG-011); observabilidade agregada = SPEC-040; replay de estado = SPEC-004 |

**Resultado:** profundidade-alvo D0–D7 atingida; D8 adversarial focado nos pontos sensíveis declarados na abertura (imutabilidade INV-07, confiança≠Convicção INV-04, causalidade pós-hoc RULE-CAU, colisão de relações, governança de escrita) — mesma reconciliação da SPEC-004. D9 por referência (coerente com alvo e com H-001 ABERTA / SPEC-040).

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO obs. | ENTÃO mens. | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE | Bounded loop / Gate saída |
|---|---|---|---|---|---|---|---|
| CKG-001 ontologia enxuta | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-002 entidade por referência | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CKG-003 relação tipada/proveniência | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CKG-004 temporalidade (invalidar≠deletar) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CKG-005 proveniência obrigatória | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-006 imutabilidade/não-deletar (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-007 confiança ≠ Convicção | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-008 causal c/ mecanismo (RULE-CAU) | ✔ | ✔ | ✔ | ✔ | ✔ | H | bounded loop ✔ + gate de saída ✔ |
| CKG-009 governança de escrita (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-010 fronteira só-publicado | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-011 consulta/trace (read-only) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CKG-012 lifecycle versionado | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CKG-013 colisão de relações | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário; cada BASpec com efeito declara Classe + critério 4Es (RULE-MECH-02); Classes C declaram gate de saída (RULE-MECH-03); Classe H (CKG-008) declara **bounded loop** (nº máximo de tentativas por par de nós, sem retry infinito) **+ gate de saída** determinístico (verifica o mecanismo causal). O LLM é detector, nunca gate (ENF-03). **PASS.**

---

## 3. Critérios EARS

13 critérios no formato "Quando <condição>, o KG DEVE/NÃO DEVE <resposta>" (ontologia, referência canônica, relação tipada/proveniência, temporalidade, proveniência obrigatória, imutabilidade, confiança≠convicção, causal c/ mecanismo, governança de escrita, fronteira publicado, consulta/trace, lifecycle, colisão). Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-CKG-001..006 (mapeiam as 13 BASpecs: 001=escrita/ontologia/proveniência/fronteira/causal; 002=imutabilidade; 003=governança; 004=confiança×convicção; 005=causal; 006=consulta/trace) |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E1 (consulta read-only); E2 (escrita permanente/causal/isolamento); **E3 na imutabilidade/não-deleção e na governança de escrita** (irreversíveis) |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ EC-CKG-003/005; RULE-CKG-008/009; roteamento de modelo (LLM só detector no juízo causal) |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-CKG-002 (não-deleção E3 fail-closed) + EC-CKG-003 (governança E3 fail-closed) + todos os EC |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-CKG/contrato [PROPOSTA]; só Andraus homologa (RULE-HG-03) |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-CKG-002 e EC-CKG-003 (amostral; **enforcement E3 CONDICIONAL até o limiar** — gap aberto, atomic-spec §12) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12 — atomic-spec v1.5)

Preenchido no plan.md. **Críticos aplicáveis:** CC-02 (CHM/CEM/CCM/SPEC-004/005 não redefinidos — só referencia/armazena), CC-08 (Herança/Delta + cobertura×lacuna canônicos/SPEC-004/005), CC-09 (H-001 ABERTA; mecanismo físico INDETERMINADO; causal c/ mecanismo RULE-CAU; sem falsa precisão em confiança), CC-10 (acepções "permanente" vs "trabalho"; "confiança" vs "Convicção"; "esquecimento" = arquivamento), CC-11 (Classe por BASpec) = PASS. CC-01 (agnóstico de escola; hierarquia intocada). CC-03 (não computa convicção; dimensionalidade=8; J-001/N-001 abertas). CC-04 (nenhuma Salvaguarda violada; INV-04 preservado — confiança nunca na convicção). CC-05 (CRITICAL/D0–D7+D8). CC-06/CC-07 = N/A justificado (não é Engineering Card). **CC-12 = N/A** (infraestrutura de memória agnóstica de escola; DHR-SPEC006-001 §2). **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED com ID+versão/linha (RULE-HD-04): **CEM-001** (l.608-615 Responsabilidades do KG; l.562-565/l.699 Cognitive Trace Reconstruction; l.494), **CHM-001**, **CCM-001**, **CEE-001** l.111, **SAS-001** §6.12, **SPEC-004 v1.2**, **SPEC-005 v1.0**, **RULE-BB-004** (l.323), **RULE-CAU-01** (l.680), **CONSTITUTION** l.233, atomic-spec v1.5, SPEC-019/020/021 v1.0, INV-04/05/06/07/09/10, ENF-01..08. ✔
- **Mapa de cobertura × lacuna presente** (arquivo:linha): preservação de linhagem/versões/estados, Cognitive Trace Reconstruction, proveniência, append-only = **herdados/reforçados, não duplicados**; lacuna real = ontologia enxuta + catálogo de entidades/relações + temporalidade + confiança de relação + consulta cognitiva + governança de escrita + lifecycle do KG. ✔
- REMOVED vazio. ✔
- MODIFIED = só RULE-BB-004 **reforçada** (não alterada) no eixo da memória permanente (RULE-HD-02 respeitada; SPEC-004/005 não tocadas — INV-09). ✔
- Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** (herança sobre canônicos/Specs vizinhas/regras, não decomposição pai→filha de macro-spec). ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001 NÃO fechada — contrato cognitivo fechável com mecanismo físico INDETERMINADO; decisão de Andraus (ADV-CKG-09) | ✔ |
| Opção B (banco de grafos) = ADIADA (registrada, não apagada; INV-07) | ✔ |
| Escala de confiança de relação = PARÂMETRO a calibrar (INDETERMINADO; sem número — RULE-MET-01) | ✔ |
| Confiança de relação ≠ Convicção; nunca retroalimenta o Conviction Vector (INV-04; CKG-007/EC-CKG-004) | ✔ |
| M-001 NÃO tocada (fronteira SPEC-004) — permanece ABERTA | ✔ |
| J-001 / N-001 NÃO tocadas; o KG não computa convicção | ✔ |
| G-001 / K-001 NÃO tocadas; estado-agente/ciclo-aprendizado por fronteira (SPEC-009/018) | ✔ |
| C-001 / WF-D03 / ECC-03-001 NÃO fechadas | ✔ |
| SPEC-004/005 NÃO reabertas/duplicadas (CC-02/INV-09; cobertura×lacuna) | ✔ |
| SPEC-007 (formação/retrieval) NÃO absorvida (CKG-010; ADV-CKG-08) | ✔ |
| RULE-CKG/contrato etiquetadas [PROPOSTA]; CEM/CHM/CCM/CEE/SAS/SPEC-004/005/RULE-BB-004/RULE-CAU-01/INV-*/ENF-* existentes como FATO NORMATIVO | ✔ |
| Fontes SRC-*/REPO-* etiquetadas [EXTERNO]; nada vira baseline (Graphiti/GraphRAG/cognee/mem0 não importados) | ✔ |
| Nenhuma decisão aberta usada como invariante fechado (STRUCT-10: H-001/M-001/J-001/N-001/G-001/K-001/C-001 marcadas ABERTAS em contexto; WF-D03/ECC-03-001 não casam `[A-Z]-\d{3}`) | ✔ |

**PASS.** Nota: nenhum limiar numérico de convicção (60%/75%) nem escala numérica de confiança é declarado — STRUCT-07 não incide (o KG não computa convicção; confiança é parâmetro, não invariante fechado).

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| CEM-001 (Responsabilidades do KG l.608-615; Cognitive Trace Reconstruction l.562-565/l.699; l.494) | ✔ | canon/CEM-001-canonical-evidence-model.md (BASELINE) |
| CHM-001; CCM-001 | ✔ | canon/ (BASELINE) |
| CEE-001 l.111 (métrica de calibração entra no KG) | ✔ | canon/CEE-001-cognitive-economy-efficiency-v2.0.md l.111 |
| SAS-001 §6.12 (Integração com KG; produtor não redefine ontologia); l.163 (EC-COG-003 "não é pré-requisito obrigatório") | ✔ | canon/SAS-001-structural-agent-spec.md l.923-924 / l.163 |
| SPEC-004 v1.2 (proveniência/identidade autenticada — RULE-CBP-014); SPEC-005 v1.0 (eventos de ciclo de vida) | ✔ | specs/features/ (BASELINE, DHR-SPEC004-003 / DHR-SPEC005-002) |
| CONSTITUTION l.233 (EC-COG-003 — Memória relacional de padrões) | ✔ | governance/CONSTITUTION.md l.233 |
| RULE-BB-004 (append-only; SUPERSEDED nunca deletado) | ✔ | governance/RULES.md l.323 |
| RULE-CAU-01 (afirmação causal exige mecanismo) | ✔ | governance/RULES.md l.680 |
| INV-04/05/06/07/09/10 | ✔ | atomic-spec §13 |
| ENF-01..08 (esp. ENF-03/04/07) | ✔ | atomic-spec §10.4 |
| RULE-MECH-01..04 (CC-11); RULE-PD-01 (CC-12); RULE-ECC-01/02/04/06 | ✔ | RULES.md |
| RULE-HD-02/03/04 (CC-08); RULE-HV-01..04 | ✔ | RULES.md (SPEC-019 baseline) |
| RULE-EPI-01/MET-01/UNC-01..03/SEM-01/04/DEC-01 | ✔ | RULES.md v1.5 |
| H-001; M-001; J-001; N-001; G-001; K-001; C-001; WF-D03; ECC-03-001 | ✔ (abertas) | ROADMAP §7 / AGENTS §7 / atomic-spec §12 |
| SPEC-001/019/020/021 v1.0; SPEC-007/009/018/040 (slots) | ✔ | specs/features/ · ROADMAP |
| REPO-graphiti/graphrag/cognee/mem0 (elegíveis) | ✔ (verbatim) | specs/features/SPEC-006/sources/ (RULE-ECC-04/06) |
| RULE-CKG-001..013; INV-CKG-01; contrato de nó/relação; BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **Nenhum item com gatilho `spec:SPEC-006` homologado isoladamente** — a redação do Plan **satisfaz ramos de gatilho** de BL-003 (`spec:SPEC-006`), BL-011 (`spec:SPEC-006`) e possivelmente BL-010 (`milestone:FASE 3 iniciada`). ✔
- **BL-003** (persistência física) — a parte física **É** H-001 (ABERTA)/G-001 (ABERTA) → referenciado, não absorvido nem promovido. ✔
- **BL-011** (MC-EXP-001) — insumo de requisitos (COL-EXP-01..05); classificação ≠ aplicação; não promovido. ✔
- **BL-010** (MC-RAG-001) — fonte de requisitos da SPEC-007; tangente; não promovido. ✔
- **BL-029** (proveniência/falso-DENY SPEC-004) `ATIVADO`/pré-existente, independente — não absorvido. ✔
- Promoção/encaminhamento é do gate e de Andraus; o passo 11-bis pleno ocorre na homologação do Plan. **PASS** (reflexo; não-promoção).

---

## 10. RULE-ECC-04 (Captura Verbatim) e RULE-ECC-06 (Repositórios) — verificação de presença

| Fonte carregada | Arquivo companheiro presente | Citação verbatim no Dossiê |
|---|---|---|
| SRC-ZEP-01 (KG temporal/agent memory) | ✔ sources/ (research.md §2) | ✔ research.md §3.1 |
| SRC-PROV-01 (W3C PROV) | ✔ sources/ | ✔ research.md §3.2 |
| SRC-MEMVSKG-01 (KG × RAG) | ✔ sources/ | ✔ research.md §3.4/§3.5 |
| SRC-FORGET-01 (forgetting — DADO, não verbatim) | N/A (sumário WebSearch) | research.md §3.5/§3.6 (marcado DADO não-verbatim) |
| REPO-graphiti / graphrag / cognee / mem0 | ✔ sources/REPO-*.txt | ✔ research.md §5 (régua Equilibrada) |

- **RULE-ECC-06 (repositórios seguros):** seção "Pesquisa em repositórios" presente (research.md §5); **4 ELEGÍVEIS** (graphiti, graphrag, cognee, mem0) sob régua Equilibrada; nenhum adotado como dependência (servem de referência confrontada com INV-07/INV-04/CC-02 e H-001); capturas REPO-*.txt presentes; conteúdo = DADO (nada instalado/executado). SPEC-006 **não** é grandfathered → STRUCT-12 incide. `python scripts/check_repo_research.py specs/features/SPEC-006` esperado OK (sem web — ENF-03). ✔
- **RULE-ECC-05 (Multi-Lente):** **NÃO incide** (DHR-SPEC006-001 §2 — infra de memória, não toca comportamento de trading); conformidade com WORKFLOW.md confirmada por prudência (consulta cognitiva; não fecha WF-D03). ✔
- **Nota de honestidade:** os valores de estrelas/licença/último-commit dos repositórios foram preenchidos por WebFetch da API pública do GitHub (research.md §5/§8) — não reproduzíveis pelo Revisor sem rede (ENF-03). Vereditos ELEGÍVEL são o que o gate confere; risco residual registrado em `sources/_LIMITACAO-WEB.txt`.

> A **correspondência verbatim** string-a-string e a régua de repositório são mandato do Revisor / gate determinístico (sem web — ENF-03). Aqui só se verifica **presença**. **PASS (presença).**

---

## 11. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | Eixo VERTICAL (RULE-HV) declarado não aplicável por [INFERÊNCIA] (herança sobre canônicos/Specs vizinhas/regras, não macro→micro) | Menor | Revisor confirma o eixo de herança |
| CK-02 | D9 auditoria por referência (Cognitive Trace Reconstruction especificada; observabilidade agregada = SPEC-040; replay de estado = SPEC-004) | Menor | Consistente com alvo D0–D7 e H-001 ABERTA |
| CK-03 | **H-001 apresentada como [DECISÃO NECESSÁRIA]** — recorte proposto (contrato cognitivo fechável; mecanismo físico INDETERMINADO), **não** fechada | Info | Andraus decide (CONS-01) |
| CK-04 | **Mecanismo físico de armazenamento = INDETERMINADO**; Opção B (banco de grafos) ADIADA, registrada | Info | Coerente com RULE-MET-01/EPI; BUILD; só Andraus fecha H-001 |
| CK-05 | **Escala de confiança de relação = PARÂMETRO a calibrar** (INDETERMINADO; sem número); ≠ Convicção (INV-04) | Info | Calibração pós-medição; não toca J-001/N-001 |
| CK-06 | **Ontologia DENTRO da SPEC-006** (enxuta), sem componente "Cognitive Ontology" separado (Q-ABERTURA-4) | Info | Revisor confirma; criar componente seria decisão de Andraus (não feita) |
| CK-07 | Baselines que citam o KG tratadas **sem erratum** (número/nome preservados): CEM-001 l.494/562-565/608-615/699, SAS-001 §6.12, CONSTITUTION l.233, CEE-001 l.111 | Info | Revisor confirma inexistência de erratum necessário (INV-09) |
| CK-08 | Imutabilidade/não-deleção e governança de escrita = **E3 fail-closed** (EC-CKG-002/003); falso-DENY E3 CONDICIONAL até o limiar (gap aberto) | Info | Revisor audita ENF-04/07; limiar não fixado (atomic-spec §12) |
| CK-09 | Causalidade = Classe H com bounded loop + gate de saída determinístico (CKG-008; RULE-CAU-01) — única H normativa da Spec | Info | Revisor confirma bounded loop + gate (RULE-MECH-03); LLM detector, não gate (ENF-03) |
| CK-10 | **Risco de volume (CRITICAL, 13 BASpecs/13 EARS/6 EC/11 cenários/10 adversariais):** se exceder uma sessão de revisão, a divisão é decisão de Andraus (Q-ABERTURA-5) — não dividida por conta própria; slot preservado (INV-07) | Menor | Andraus decide eventual divisão |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (CKG-001..013) com Classe/Mecanismo (CC-11; D determinístico + C constitutivo + H híbrido com bounded loop/gate de saída em CKG-008), EARS (13), Enforcement (EC-CKG-001..006; ENF-03 detector≠gate; **E3 fail-closed na imutabilidade/não-deleção e na governança de escrita**; E3 falso-DENY CONDICIONAL até limiar), Constitution Check CC-01..CC-12 (CC-02/CC-08/CC-09/CC-10/CC-11 incidem e aplicados; CC-12 N/A), Herança/Delta (CC-08 + cobertura×lacuna canônicos/SPEC-004/005), CONS-01 (H-001/M-001/J-001/N-001/G-001/K-001/C-001/WF-D03/ECC-03-001 abertas; mecanismo físico INDETERMINADO; Opção B adiada; confiança = parâmetro ≠ Convicção), gate RMR-001 (nenhum gatilho spec:SPEC-006 isolado; BL-003/010/011/029 não promovidos), RULE-ECC-04 (presença verbatim) e RULE-ECC-06 (repositórios, régua Equilibrada — 4 elegíveis) satisfeitos. Achados não-bloqueantes CK-01..CK-10 encaminhados.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: gate determinístico `validate_spec_sot.py` + `check_repo_research.py` + `build_map.py --check` + `check_doc_sync.py` (execução no ambiente pai — Especificador sem Bash) + submissão ao Revisor SOT.
