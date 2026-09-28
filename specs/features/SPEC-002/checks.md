# checks.md — Verificação de Spec da SPEC-002 (fase spec-first)

**Objeto:** `specs/features/SPEC-002/plan.md` (Evidence & Evidence Provenance Harness — camada operacional sobre CEM-001)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; AGENTS.md §5]
**Método:** atomic-spec v1.4
**Autor:** Especificador Principal SOT
**Data:** 2026-09-28

> **Ressalva de gate (RULE-ECC-04):** esta verificação estrutural roda normalmente. O **protocolo semântico completo do Revisor + homologação** ficam bloqueados até a recaptura verbatim real das 7 fontes `[EXTERNO]` (WebFetch bloqueado; DHR-SPEC002-VERBATIM-001) — ver nota de gate no topo do `plan.md`.

---

## 1. Verificação Estrutural (Gate Determinístico — equivalente STRUCT-01..11)

Como o `validate_spec_sot.py` não pôde ser executado nesta sessão (sem Bash), os itens que o gate determinístico verifica são confirmados manualmente abaixo.

| # | Check (STRUCT) | Resultado | Evidência |
|---|---|---|---|
| 1 | Complexidade declarada | PASS | `Complexidade | CRITICAL` no cabeçalho |
| 2 | Profundidade-alvo declarada | PASS | `Profundidade-alvo | D0–D7 + D8 adversarial` |
| 3 | Profundidade compatível com complexidade | PASS | CRITICAL permite até D8; alvo D0–D7+D8 dentro do limite (AGENTS.md §4) |
| 4 | Constitution Check presente (CC-01..CC-12) | PASS | Seção "Constitution Check" com os 12 itens |
| 5 | EARS presente ("Quando <cond>, ... DEVE") | PASS | Seção "Critérios de Aceitação (EARS)" com 9 critérios |
| 6 | BASpec com campos acentuados (QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR) | PASS | 8 BASpecs (EV-001..008), todas com os 5 campos acentuados |
| 7 | Enforcement Contract (8 campos) presente | PASS | 8 ECs (EC-EV-01..08) com CAPABILITY/EFFECT/PRECOND/POSTCOND/POLICY/LEVEL/FAILURE-MODE/EVIDENCE |
| 8 | Conviction Vector não fechado (J-001 marcado) | PASS | CC-03 + Decisões abertas: "J-001 EM ABERTO — [DECISÃO NECESSÁRIA]" |
| 9 | Etiquetagem (5 tags) presente | PASS | [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] todas usadas |
| 10 | Status epistemológico (FATO NORMATIVO/ARQUITETURAL) | PASS | Tabela TRACE-06: CEM-001 FATO NORMATIVO; Registry FATO ARQUITETURAL |
| 11 | IDs internos sem colisão com decisões abertas (prefixo 3+ / não J-001) | PASS | EV- (evidência), HYP- (hipótese), EC-EV- (contratos); J-001/M-001 só como decisões abertas marcadas |

**Resultado da seção 1:** 11/11 PASS (verificação manual — `validate_spec_sot.py` deve ser re-executado no gate real com Bash). **Nota:** o gate real permanece condicionado à recaptura verbatim (RULE-ECC-04).

---

## 2. Cobertura de profundidade (D0–D7 + D8 — alvo CRITICAL)

| Nível | Exigido (CRITICAL) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão — camada operacional sobre CEM-001, 8 responsabilidades |
| D1 Escopo/Non-goals | Sim | ✔ | Tabela dentro-do-escopo + Non-goals (CEM/SPEC-003/SPEC-004/006/MiFID/etc.) |
| D2 Regra | Sim | ✔ | RULE-EVH-001..009 [PROPOSTA] com Classe indicada |
| D3 Comportamento (BASpec) | Sim | ✔ | BASpec-EV-001..008 com Classe declarada (RULE-MECH-01) |
| D4 Algoritmo | Onde há regra determinística real | ✔ | `dedupe_dependent_evidence` (anti-dupla-contagem, com exemplo) |
| D5 Estado | Estado persistente | ✔ | Estados da Evidência (CEM Cap.4, referenciados não redefinidos) |
| D6 Protocolo | Todos os agentes | ✔ (por referência) | Eventos cognitivos via EC-COG-005; Blackboard/estados = M-001 aberta (SPEC-004), declarado não omitido |
| D7 Teste | Sim (CRITICAL) | ✔ | Cenários EV-T01..T05 (5, ≥3 exigidos) |
| D8 Adversarial | Sim (CRITICAL) | ✔ | ADV-EV-01..07 (7, ≥1 exigido; ADV-EV-01/02 = casos-âncora da abertura) |
| D9 Auditoria | Sistema completo | ✔ (por referência) | Requisitos P13; Cognitive Trace Reconstruction plena diferida ao KG (SPEC-006) |

**Resultado:** profundidade-alvo D0–D7 + D8 atingida; D6/D9 por referência justificados (não omissos). **PASS.**

---

## 3. Well-formedness das BASpecs (EV-001..008) + Classe (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE + 4Es | Bounded loop/Gate (H/P/C) |
|---|---|---|---|---|---|---|---|
| EV-001 criação/registro | ✔ | ✔ | ✔ | ✔ | ✔ | H · Eficácia | Bounded loop (1 correção) + gate (contrato CEM) ✔ |
| EV-002 registry (ID/versão) | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| EV-003 qualidade/independência | ✔ | ✔ | ✔ | ✔ | ✔ | P · Eficácia | Bounded loop (finito por conjunto) ✔; sem gate binário (julgamento qualitativo — mínimo P) |
| EV-004 natureza/ausência 1ª classe | ✔ | ✔ | ✔ | ✔ | ✔ | H · Conformidade/Eficácia | Gate constitutivo (ausência⇒≠CONTRARY) ✔ |
| EV-005 marcação de conflito | ✔ | ✔ | ✔ | ✔ | ✔ | H · Eficácia | Gate (ausência de força fundida) ✔ |
| EV-006 provenance | ✔ | ✔ | ✔ | ✔ | ✔ | H · Eficácia/Explicabilidade | Gate (completude de provenance) ✔ |
| EV-007 imutabilidade/chain-of-custody | ✔ | ✔ | ✔ | ✔ | ✔ | C · Eficácia/Conformidade | Gate = o próprio enforcement (diff de campo imutável) ✔ |
| EV-008 Evidência↔Hipótese | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário. Classe declarada por BASpec (não por Spec — SES-001 §50, CC-11). Classe **C** usada apenas em EV-007 (imutabilidade — risco alto E3; RULE-MECH-02 satisfeita, não é risco baixo). H/P declaram bounded loop (RULE-MECH-03); H/C declaram gate de saída (ENF-03). **PASS.**

---

## 4. Critérios EARS

Formato "Quando <condição>, o componente DEVE <resposta>" verificável nos 9 critérios de aceitação e nas 8 BASpecs (QUANDO/ENTÃO) + 7 adversariais (DADO/QUANDO/ENTÃO). Sem multi-outcome não-decomposto — cada BASpec tem 1 condição observável + 1 comportamento mensurável. **PASS.**

---

## 5. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-EV-01..08 (uma por BASpec com efeito) |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ Evidência de Agente E2 (piso); imutabilidade/anti-conversão E3 (criticidade×irreversibilidade) |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ validação de contrato/diff de campo imutável = código (EV-001/004/007); dedupe por fonte/lineage (EV-003) |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-EV-04 (ausência⇒nunca CONTRARY) e EC-EV-07 (imutabilidade/lineage) fail-closed E3 |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-EVH-* são [PROPOSTA] até homologação; nenhuma auto-aplicação |
| ENF-06 E0 declarado como orientação | N/A (mínimo declarado é E1; sem E0 nesta Spec) |
| ENF-07 E3 declara método de falso-DENY (amostral; limiar = gap aberto) | ✔ EC-EV-04 e EC-EV-07 declaram método amostral; LIMIAR = [DECISÃO NECESSÁRIA: BL-002] (diferido, não fechado — CONS-01) |
| ENF-08 Escala E0–E3 referenciada em seção própria | ✔ seção "Escala E0–E3 (F.1–F.4)" citando atomic-spec §10.2 |

**Resultado:** **PASS** (ENF-06 N/A justificado; ENF-07 satisfeito com limiar declarado como decisão aberta).

---

## 6. Constitution Check (CC-01..CC-12)

| CC | Resultado | Evidência |
|---|---|---|
| CC-01 Hierarquia | PASS | Evidência neutra de escola; hierarquia protegida, não tocada |
| CC-02 Não redefine canônico | PASS | Constrói SOBRE CEM-001; estrutura/estados/lineage referenciados por capítulo, não redefinidos |
| CC-03 Conviction pendente (J-001) | PASS | Evidence Strength ≠ Convicção; J-001 [DECISÃO NECESSÁRIA] |
| CC-04 Salvaguardas CEE-001 | PASS | Nenhuma violada; custo fora de tudo (INV-04) |
| CC-05 Complexidade | PASS | CRITICAL, D0–D7+D8 |
| CC-06 Campos SES-001 §59 | PASS (N/A justificado) | Artefato é Plan, não Engineering Card (adiado a Tasks/BUILD) |
| CC-07 Cadeia de derivação §60 | PASS (N/A justificado) | Rastreabilidade de origem declarada (ROADMAP→Dossiê→Plan) |
| CC-08 Herança/Delta (RULE-HD) | PASS | Bloco presente; INHERITS/ADDED com ID+versão; REMOVED vazio; sem contradição (RULE-HD-02); RULE-HV N/A justificado |
| CC-09 Epistemic Check | PASS | Ausência≠contraevidência; INDETERMINADO 1ª classe; sem falsa precisão; qualitativo até J-001 |
| CC-10 Terminologia concorrente | PASS | Evidência vs Observação; provenance vs lineage; Evidence Strength vs Convicção — acepções declaradas; canônico não redefinido |
| CC-11 Classe por BASpec | PASS | 8 BASpecs com Classe (D/H/P/C); C só em EV-007 (risco alto); bounded loop/gate onde exigível |
| CC-12 Princípios de Domínio | PASS (N/A confirmado) | CEM domain-neutral; nenhum PD-xx (DHR-SPEC002-001 §2) |

**Resultado:** 12/12 conformes (3 N/A justificados). **PASS.**

---

## 7. §7-bis — Redução de Viés (EUA-E18) — presença e completude

| Bloco | Presente | Evidência |
|---|---|---|
| A — Pergunta adversarial por BASpec | ✔ | 8 BASpecs com caso de negação verificável; mapeados a ADV-EV-01..07 |
| B — Herança obrigação-a-obrigação (CC-08 vs CEM/CHM/SPEC-001) | ✔ | Tabela de 8 obrigações herdadas + evidência de satisfação; RULE-HD-02/03 confirmados |
| C — Verificação epistêmica (RULE-EPI-01..03) | ✔ | Afirmação causal (independência) com mecanismo; INDETERMINADO; sem falsa precisão; N8–N17 aplicadas |
| D — Reforço de escopo | ✔ | Registra/marca, não executa/resolve; dependências de Andraus marcadas [DECISÃO NECESSÁRIA] |

**Resultado:** **PASS** (obrigatório para CRITICAL; presente e substrato do Passo 5-bis do Revisor).

---

## 8. Verificação de Consistência (CONS-01)

| Decisão Aberta | Aparece como fechado? | Marcador de pendência presente? | Resultado |
|---|---|---|---|
| J-001 | Não | Sim ([DECISÃO NECESSÁRIA], EM ABERTO) | PASS |
| M-001 | Não | Sim (EM ABERTO — SPEC-004) | PASS |
| H-001 / BL-003 | Não | Sim (EM ABERTO — SPEC-006) | PASS |
| BL-002 (falso-DENY) | Não | Sim (EC-EV-04/07 declaram sem fechar limiar) | PASS |
| SPEC-002-VERBATIM-001 | Não | Sim (PENDENTE; nota de gate) | PASS |

**Resultado:** nenhuma decisão aberta tratada como invariante fechado. **PASS.**

---

## 9. Verificação de Integridade (referências)

### 9.1 RULEs citadas

| RULE citada | Existe? | Resultado |
|---|---|---|
| RULE-EVH-001..009 | Criadas nesta Spec (prefixo local RULE-EVH- para não colidir com RULE-EV-01..07 da SPEC-020) | OK (novas) |
| RULE-004 | Sim (RULES.md) | PASS |
| RULE-EPI-01..03 / RULE-UNC-01/03 / RULE-PRB-02 / RULE-CAU-01 / RULE-DEC-01 / RULE-MET-01 / RULE-SEM-01/04 / RULE-INQ-02 | Sim (RULES.md — registro RULE-REG-001, 2026-09-28) | PASS |
| RULE-HD-01..04 | Sim (RULES.md — registro RULE-REG-001, 2026-09-28) | PASS |
| RULE-MECH-01..04 / RULE-MM-04/05 / RULE-EV-05 | Sim (RULES.md) | PASS |
| RULE-ECC-02/04 | Sim (RULES.md) | PASS |
| ENF-01..08 | Sim (atomic-spec §10.4) | PASS |

> **Nota de prefixo:** as regras locais desta Spec usam `RULE-EVH-0xx` (Evidence Harness) deliberadamente para **não colidir** com a família `RULE-EV-01..07` (Avaliação do Harness, SPEC-020) já registrada no RULES.md. [INFERÊNCIA — coerência de namespace]

### 9.2 Fontes citadas

| Fonte citada | Existe? | Resultado |
|---|---|---|
| CEM-001 Cap.1–8 (estrutura, estados, lineage, consumo, governança) | Sim (canon/CEM-001-canonical-evidence-model.md) | PASS |
| CHM-001 (relação Evidência↔Hipótese) | Sim (canon/) | PASS |
| SPEC-001 (padrão camada operacional; fronteira; INV-06) | Sim (specs/features/SPEC-001/plan.md) | PASS |
| INV-03/04/05/06/07/09/10 | Sim (atomic-spec §13) | PASS |
| SRC-01..07 [EXTERNO] | Arquivos em sources/ presentes; **captura verbatim PENDENTE (RULE-ECC-04; WebFetch bloqueado)** | PENDENTE — não verbatim-verificado |
| DHR-SPEC002-001 / DHR-SPEC002-VERBATIM-001 | Sim (governance/) | PASS |

**Resultado:** referências internas íntegras; **fontes [EXTERNO] carecem de captura verbatim (RULE-ECC-04)** — achado registrado, bloqueia o gate semântico completo (não a verificação estrutural).

---

## 10. Resumo da Verificação

| Categoria | Checks | Resultado |
|---|---|---|
| Estrutura (STRUCT-01..11 manual) | 11 | 11 PASS |
| Cobertura de profundidade D0–D8 | 10 | PASS (D6/D9 por referência) |
| BASpecs (8) + Classe | 8 | 8 PASS |
| EARS | — | PASS |
| Enforcement Contracts (8) + ENF-01..08 | 8 | 8 PASS |
| Constitution Check CC-01..12 | 12 | 12 PASS (3 N/A justificados) |
| §7-bis (A/B/C/D) | 4 | PASS |
| Consistência CONS-01 | 5 | 5 PASS |
| Integridade de referências | — | PASS internas; **PENDENTE verbatim [EXTERNO]** |

---

## 11. Conclusão

A SPEC-002 (Evidence & Evidence Provenance Harness) passou em todas as verificações **estruturais** de spec (BASpec/EARS/Enforcement/Classe/CC/§7-bis bem-formados).

**Bloqueio ativo (não estrutural):** a **captura verbatim RULE-ECC-04** das 7 fontes `[EXTERNO]` **não pôde ser feita** (WebFetch bloqueado por egresso — confirmado nesta rodada). Por DHR-SPEC002-VERBATIM-001 (Opção A), a recaptura é **pré-condição do gate do Plan** e deve ocorrer em sessão com WebFetch operacional, **antes** do protocolo semântico completo do Revisor e da homologação.

**Status:**
- **Verificação estrutural:** PASS.
- **Protocolo semântico completo do Revisor (GRE-001/HRE-001):** **BLOQUEADO até a recaptura verbatim** (fail-closed RULE-ECC-04).
- **Gate determinístico real:** `python scripts/validate_spec_sot.py specs/features/SPEC-002/plan.md` deve retornar EXIT 0 (re-executar com Bash disponível).

**[DECISÃO NECESSÁRIA] em aberto:** J-001; M-001; H-001; BL-003; BL-002; **SPEC-002-VERBATIM-001** (captura verbatim das 7 fontes [EXTERNO], pendente por WebFetch bloqueado).
