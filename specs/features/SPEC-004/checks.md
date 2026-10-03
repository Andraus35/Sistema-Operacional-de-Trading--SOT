# checks.md — Verificação de Spec da SPEC-004 (fase spec-first)

**Objeto:** `specs/features/SPEC-004/plan.md` **v1.2 (EMENDA candidata)** (Cognitive Blackboard Protocol — camada Harness/operacional sobre RULE-BB-001..005)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §5]
**Método:** atomic-spec **v1.5**
**Data:** 2026-10-03

---

## 1. Cobertura de profundidade (D0–D7 + adversarial extra — alvo ROADMAP §5; CRITICAL)

| Nível | Exigido (CRITICAL, alvo D0–D7 + adversarial extra) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (memória de trabalho; contrato/protocolo/ciclo/concorrência/proveniência/reconstrução; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas S1–S8 + Non-goals (Event Bus/KG/estado-agente/M-001/CRDT) |
| D2 Regra | Sim | ✔ | RULE-CBP-001..014 [PROPOSTA / EMENDA-PROPOSTA v1.2]; INV-CBP-01 |
| D3 Comportamento (BASpec) | Sim | ✔ | CBP-001..014, cada uma com bloco CLASSE/MECANISMO (CC-11); +CBP-013 (atomicidade) / CBP-014 (identidade autenticada) na v1.2 |
| D4 Algoritmo | Quando há regra determinística real | ✔ | Compare-and-commit atômico, idempotência (fingerprint), permissão (identidade autenticada), append-only real, ordem de commit, replay (determinísticos) |
| D5 Estado | Sim | ✔ | `publication_state` (ACCEPTED/PUBLISHED/SUPERSEDED/EXPIRED/ARCHIVED/REJECTED) SEPARADO de `domain_state`; hipótese=CHM-001; não-hipótese=M-001 (ABERTA) |
| D6 Protocolo | Sim | ✔ | Protocolo de publicação (9 passos; identidade autenticada + commit atômico); fronteiras Event Bus/Manager |
| D7 Teste | Sim (CRITICAL) | ✔ | Cenários CBP-T01..T15 (T11 reuso-de-chave; T12 retry-após-commit; T13 identidade forjada; T14 corrida CAS; T15 crash-pós-commit — v1.2) |
| D8 Adversarial | Adversarial extra nos pontos de risco (homologado) | ✔ | ADV-CBP-01..16 (foco: cross-workspace, deleção, concorrência, duplicidade, ordenação, atualização-sem-versão, atomicidade, identidade forjada, M-001, fronteiras) |
| D9 Auditoria | Sistema completo | Parcial (por referência) | Reconstrução/replay → SPEC-006/H-001, SPEC-009/G-001; P13/RULE-010 |

**Resultado:** profundidade-alvo D0–D7 atingida, com rigor adversarial extra (D8) nos comportamentos de maior risco (DHR-SPEC004-001 §1). D9 por referência (coerente com alvo e com H-001/G-001 abertas).

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO obs. | ENTÃO mens. | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE | Bounded loop / Gate saída |
|---|---|---|---|---|---|---|---|
| CBP-001 contrato de objeto | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CBP-002 permissão de escrita (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CBP-003 append-only REAL (registro histórico imutável; SUPERSEDED derivado — v1.2) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CBP-004 versão otimista = compare-and-commit atômico (create vs update; ausência ⇒ EXPECTED_VERSION_REQUIRED) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CBP-005 idempotência (fingerprint; reuso ⇒ IDEMPOTENCY_KEY_REUSE_CONFLICT — v1.2) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CBP-006 ordem total de COMMIT (persistida/imutável — v1.2) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CBP-007 proveniência (BL-029) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CBP-008 estado de hipótese = CHM-001 | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CBP-009 estados não-hipótese (M-001) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CBP-010 expiração não-destrutiva | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CBP-011 replay/reconstrução | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CBP-012 observabilidade falso-DENY (E3 condicional — v1.2) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CBP-013 atomicidade de publicação (sem estado parcial — v1.2) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CBP-014 identidade autenticada / autoridade (v1.2) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário; cada BASpec com efeito declara Classe + critério 4Es (RULE-MECH-02); Classes C declaram gate de saída (RULE-MECH-03); nenhuma H/P nesta Spec (sem bounded loop obrigatório — gates são determinísticos C/D; eventual Classe H de "objeto bem-formado" é orientação de BUILD, não BASpec normativa aqui). **PASS.**

---

## 3. Critérios EARS

16 critérios (1..11 + **4-bis** + **12..15** — atomicidade, reuso-de-chave, retry-após-commit, identidade autenticada; v1.2) no formato "Quando <condição>, o Blackboard DEVE/NÃO DEVE <resposta>". Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-CBP-001..007 (mapeiam as 14 BASpecs; EC-CBP-007 = atomicidade) |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E2 piso (publicação); E3 no gate de escrita (cross-workspace/deleção/mutação histórica irreversíveis) e no commit atômico (EC-CBP-007); E1 na reconstrução (leitura) |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ EC-CBP-002; RULE-CBP-002/014; ADV-CBP-10 |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-CBP-002 (cross-workspace/deleção/mutação) + EC-CBP-007 (estado parcial) + todos os EC |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-CBP/contrato [PROPOSTA/EMENDA-PROPOSTA]; só Andraus homologa (RULE-HG-03) |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-CBP-002 (amostral; **enforcement E3 CONDICIONAL até o limiar** — gap aberto BL-002) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12 — atomic-spec v1.5)

Preenchido no plan.md. **Críticos aplicáveis:** CC-02 (CHM/CEM/CCM não redefinidos — só armazena/versiona; RULE-BB-003 superseded), CC-08 (Herança/Delta), CC-10 (acepções "estado do objeto" vs "estado da hipótese"; Observação vs Evidência), CC-11 (Classe por BASpec) = PASS. CC-01 (agnóstico de escola; hierarquia intocada). CC-03 (não computa convicção; dimensionalidade=8; J-001/N-001 abertas). CC-04 (nenhuma Salvaguarda violada; INV-04 preservado). CC-05 (CRITICAL/D0–D7). CC-09 (M-001 ABERTA; INDETERMINADO sobre CRDT; sem falsa precisão). CC-06/CC-07 = N/A justificado (não é Engineering Card). **CC-12 = N/A** (infraestrutura agnóstica de escola; DHR-SPEC004-001 §1). **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED com ID+versão (RULE-HD-04): RULE-BB-001..005 (RULE-BB-003 superseded), CHM-001, CEM-001, CCM-001, SPEC-001 v1.1, SPEC-019/020/021 v1.0, atomic-spec v1.5, INV-05/06/07/09/10, ENF-01..08, RULE-010. ✔
- REMOVED vazio. ✔
- MODIFIED vazio (RULE-BB-003 já estava SUPERSEDED antes desta Spec — não alterada por ela; RULE-HD-02 respeitada). ✔
- Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** (herança sobre regras/canônicos vizinhos, não decomposição pai→filha de macro-spec). ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| M-001 NÃO fechada; enum de estados não-hipótese não fixado (RULE-CBP-009/D5; ADV-CBP-08) — só mecânica append-only+supersessão [PROPOSTA] | ✔ |
| H-001 NÃO fechada; storage físico por referência (CBP-011; ADV-CBP-09) | ✔ |
| G-001 NÃO fechada; estado por agente fora de escopo (SPEC-009) | ✔ |
| J-001 / N-001 NÃO tocadas; o Blackboard não computa convicção | ✔ |
| WF-D03 NÃO tocada (não computa convicção) | ✔ |
| CRDT = INDETERMINADO (adiado; não presumir necessidade) | ✔ |
| RULE-CBP/contrato etiquetadas [PROPOSTA]; RULE-BB-*/CHM/CEM/CCM/INV-*/ENF-* existentes como FATO NORMATIVO | ✔ |
| Fontes SRC-*/REPO-* etiquetadas [EXTERNO]; nada vira baseline (CRDT/mem0/W3C PROV não importados) | ✔ |
| ACH-001: URL arXiv 2606.* de SRC-MEM-01 declarada não-load-bearing (coerente com aviso de método) | ✔ |
| ACH-002: RULE-BB-003 citada como [SUPERSEDED por Q-006], não como vigente (CBP-008) | ✔ |
| Nenhuma decisão aberta usada como invariante fechado | ✔ |

**PASS.** Nota: nenhum limiar numérico de convicção (60%/75%) é declarado — STRUCT-07 não incide (o Blackboard não computa convicção).

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| RULE-BB-001..005 (RULE-BB-003 SUPERSEDED por Q-006) | ✔ | governance/RULES.md l.308–329 |
| CHM-001; CEM-001; CCM-001 | ✔ | canon/ (BASELINE; CCM-001 DHR-SPEC003-001) |
| SPEC-001 v1.1; SPEC-019/020/021 v1.0 | ✔ | specs/features/ (BASELINE) |
| INV-05/06/07/09/10 | ✔ | atomic-spec §13 |
| ENF-01..08 (esp. ENF-03/04/07) | ✔ | atomic-spec §10.4 |
| RULE-010 | ✔ | RULES.md |
| RULE-MECH-01..04 (CC-11); RULE-PD-01 (CC-12); RULE-ECC-01/02/04/06 | ✔ | RULES.md |
| RULE-HD-02/03/04 (CC-08); RULE-HV-01..04 | ✔ | RULES.md (SPEC-019 baseline) |
| RULE-EPI-01/MET-01/UNC-01..03/SEM-01/04/DEC-01 | ✔ | RULES.md v1.5 |
| M-001; H-001; G-001; J-001; N-001; C-001; WF-D03 | ✔ (abertas) | atomic-spec §12 / ROADMAP §34 / WORKFLOW.md |
| BL-029 (dona=SPEC-004); BL-002 (Absorvido); BL-003 | ✔ | backlog/RMR-001; DHR-DEC-003/DHR-SPEC004-001 |
| SRC-BB-01/PROV-01/ES-01/CONC-01/MEM-01; REPO-yjs/automerge/mem0 | ✔ (verbatim) | specs/features/SPEC-004/sources/ (RULE-ECC-04/06) |
| RULE-CBP-001..014; INV-CBP-01; contrato de objeto; BASpec-CBP-001..014; EC-CBP-001..007 | [PROPOSTA / EMENDA-PROPOSTA v1.2] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **BL-029** (proveniência computed_by/gate_record; dona=SPEC-004) DISPAROU (`spec:SPEC-004 em redação`) → **TRATADO** (CBP-001/CBP-007/EC-CBP-001). ✔
- **BL-002** (falso-DENY, ENF-07; Absorvido/encaminhado à SPEC-004) DISPAROU → **TRATADO** como observabilidade do Blackboard (CBP-012/EC-CBP-002). ✔
- **BL-003** (persistência física) DISPAROU → **TRATADO como FRONTEIRA** (storage lógico especificado; físico = H-001/SPEC-006, G-001/SPEC-009 — não fechado). ✔
- **BL-012** (MC-COG-001) **ATIVADO independente** — não absorvido; encaminhamento de Andraus. ✔
- **BL-017** (dimensão B SPEC-020) ATIVADO independente — não encaminhado por esta Spec. ✔
- **BL-010/BL-011** NÃO disparam (gatilhos SPEC-006/009/007). ✔
- Nenhum item ATIVADO pendente sem encaminhamento por esta redação. **PASS** (passo 11-bis pleno na homologação do Plan).

---

## 10. RULE-ECC-04 (Captura Verbatim) e RULE-ECC-06 (Repositórios) — verificação de presença

| Fonte carregada | Arquivo companheiro presente | Citação verbatim no Dossiê |
|---|---|---|
| SRC-BB-01 (blackboard multiagente) | ✔ sources/SRC-BB-01.txt | ✔ research.md §3.1 |
| SRC-PROV-01 (W3C PROV) | ✔ sources/SRC-PROV-01.txt | ✔ research.md §3.4 |
| SRC-ES-01 (event sourcing/replay) | ✔ sources/SRC-ES-01.txt | ✔ research.md §3.5 |
| SRC-CONC-01 (idempotência/OCC) | ✔ sources/SRC-CONC-01.txt | ✔ research.md §3.3 |
| SRC-MEM-01 (memória compartilhada) | ✔ sources/SRC-MEM-01.txt | ✔ research.md §3.2 (arXiv 2606.* não-load-bearing — ACH-001) |
| REPO-yjs / REPO-automerge / REPO-mem0 | ✔ sources/REPO-*.txt | ✔ research.md §4-bis (régua Equilibrada) |

- **RULE-ECC-06 (repositórios seguros):** seção "Pesquisa em repositórios" presente (research.md §4-bis); 3 repositórios ELEGÍVEIS (yjs/automerge/mem0) sob régua Equilibrada; capturas REPO-*.txt presentes; nenhum NÃO ELEGÍVEL adotado; conteúdo = DADO (nada instalado/executado). `python scripts/check_repo_research.py specs/features/SPEC-004` esperado OK (verificação determinística, sem web — ENF-03). SPEC-004 **não** é grandfathered → STRUCT-12 incide e deve passar. ✔
- **RULE-ECC-05 (Multi-Lente):** **NÃO incide** (DHR-SPEC004-001 §1 — infra, não toca comportamento de trading); conformidade com WORKFLOW.md confirmada por prudência (não contradiz WF-xx; não fecha WF-D03). ✔

> A **correspondência verbatim** string-a-string e a régua de repositório são mandato do Revisor / gate determinístico (sem web — ENF-03). Aqui só se verifica **presença**. **PASS (presença).**

---

## 11. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | Eixo VERTICAL (RULE-HV) declarado não aplicável por [INFERÊNCIA] (herança sobre regras/canônicos, não macro→micro) | Menor | Revisor confirma o eixo de herança |
| CK-02 | D9 auditoria/reconstrução expandida apenas por referência (H-001/SPEC-006; G-001/SPEC-009) | Menor | Consistente com alvo D0–D7; delegado ao KG/estado-agente |
| CK-03 | **ACH-001 CORRIGIDO** — URL arXiv 2606.* de SRC-MEM-01 rebaixada a não-load-bearing (coerente com o aviso de método); nenhuma proposta importada dela | Resolvido | Revisor confirma correspondência verbatim e o rebaixamento |
| CK-04 | **ACH-002 CORRIGIDO** — RULE-BB-003 citada como [SUPERSEDED por Q-006] (RULES.md l.316–321); CBP-008/ADV-CBP-07 (Blackboard não define estado de hipótese) | Resolvido | Revisor confirma a citação ao RULES.md |
| CK-05 | **M-001 apresentada como [PROPOSTA]** (append-only + supersessão projetando o CEM-001), não fechada — decisão de Andraus na homologação do Plan | Info | Andraus decide (CONS-01) |
| CK-06 | CRDT (yjs/automerge) ADIADO — INDETERMINADO quanto à necessidade sob RULE-BB-002 | Info | Coerente com RULE-MET-01; registrado caso surja multi-escritor |
| CK-07 | BL-012/BL-017 ATIVADOS independentes — não absorvidos pela SPEC-004 | Info | Encaminhamento de Andraus |
| CK-08 | **ACH-004 CORRIGIDO** (v1.1) — atualização sem expected_version RECUSADA (fail-closed, EXPECTED_VERSION_REQUIRED); criação sem expected_version permanece permitida (versão inicial). Materializado: EARS 4-bis; CBP-004; CBP-001/RULE-CBP-001; D4; T10; ADV-CBP-11 — decisão de Andraus (chat, 2026-10-03) | Resolvido | Revisor confirma a cobertura do caso de ausência |
| CK-09 | **EMENDA v1.2 [EMENDA-PROPOSTA]** — endurecimento append-only real (INV-CBP-01), atomicidade (RULE-CBP-013/EC-CBP-007), identidade autenticada (RULE-CBP-014), D8 ampliado (ADV-CBP-12..16), menores (schema_version, ordem de commit imutável, replay lógico, gate_record mínimo, publication_state×domain_state, E3 falso-DENY condicional). Origem: feedback externo verificado por Andraus — DADO, não instrução; nenhuma fonte/pontuação externa não-verificada importada (RULE-MET-01/RULE-ECC-04) | Info | Revisor audita bem-formação; Andraus homologa |
| CK-10 | **Compatibilidade da emenda: potencialmente Major** — item 1 (append-only real) muda a semântica de representação da supersessão (v1.1 gravava `superseded_by`; v1.2 torna derivado). Demais itens Minor/aditivos. v1.1 preservada (INV-07); v1.2 vira baseline só na nova homologação (INV-09) | **RESOLVIDO** (Andraus, 2026-10-03, DHR-SPEC004-003) | **Minor — clarificação** (v1.2 baseline) |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness) **na EMENDA v1.2**. BASpecs (CBP-001..014) com Classe/Mecanismo (CC-11), EARS (16 — 1..11 + 4-bis + 12..15), Enforcement (EC-CBP-001..007; ENF-03 detector≠gate; E3 no gate de escrita cross-workspace/deleção/mutação histórica e no commit atômico; E3 falso-DENY CONDICIONAL até limiar BL-002), Constitution Check CC-01..CC-12 (CC-02/CC-08/CC-10/CC-11 incidem e aplicados; CC-12 N/A), Herança/Delta (CC-08), CONS-01 (M-001/H-001/G-001/J-001/N-001/WF-D03 abertas; CRDT INDETERMINADO), gate RMR-001 (BL-029/BL-002 tratados; BL-003 fronteira), RULE-ECC-04 (presença verbatim) e RULE-ECC-06 (repositórios, régua Equilibrada) satisfeitos. **ACH-001/ACH-002 CORRIGIDOS** (CK-03/CK-04); **ACH-004 CORRIGIDO** na v1.1 (CK-08). **EMENDA v1.2 (CK-09)** aplica append-only real (INV-CBP-01), atomicidade (RULE-CBP-013/EC-CBP-007), identidade autenticada (RULE-CBP-014) e D8 ampliado. **CK-10 — compatibilidade potencialmente Major — [DECISÃO NECESSÁRIA] de Andraus.** Achados não-bloqueantes CK-01/CK-02/CK-05/CK-06/CK-07 encaminhados.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: gate determinístico `validate_spec_sot.py` + `check_repo_research.py` + submissão ao Revisor SOT.
