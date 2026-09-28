# SPEC-001 — Hypothesis Harness — Verificação de Spec

**Versão:** 1.1
**Status:** Verificação de spec (fase spec-first)
**Objetivo:** Provar que BASpecs, EARS, Enforcement Contracts e estrutura da SPEC-001 estão bem-formados.
**Tipo:** Verificação de Spec (não teste de runtime)
**Autor:** Especificador Principal
**Data:** 2026-09-15

---

## 1. Verificação Estrutural (Gate Determinístico)

### 1.1 Cabeçalho

| Check | Resultado | Evidência |
|---|---|---|
| Complexidade declarada | PASS | `Complexidade: CRITICAL` na linha 5 (formato sem markdown) |
| Profundidade-alvo declarada | PASS | `Profundidade-alvo: D0–D8` na linha 6 (v1.1; D8 adversarial formal presente) |
| Profundidade compatível com complexidade | PASS | CRITICAL permite até D8; D7 dentro do limite |

### 1.2 Constitution Check

| Check | Resultado | Evidência |
|---|---|---|
| Hierarquia Elliott mencionada | PASS | "Hierarquia Elliott-Fibonacci-Fractal-SMC-ICT respeitada" |
| Conviction pendente (J-001 em aberto) | PASS | "J-001 em aberto — [DECISÃO NECESSÁRIA]" |
| Não redefine CHM-001 | PASS | "constrói SOBRE o CHM-001; não redefine" |
| Salvaguardas mencionadas | PASS | "Nenhuma das 5 Salvaguardas Constitucionais violada" |
| Complexidade declarada no check | PASS | "CRITICAL (P0, núcleo cognitivo)" |

### 1.3 Etiquetagem

| Check | Resultado | Evidência |
|---|---|---|
| [FONTE] presente | PASS | Múltiplas ocorrências (ex.: "[FONTE: CHM-001 §3.1]") |
| [INFERÊNCIA] presente | PASS | "Hypothesis Registry (serviço lógico) [INFERÊNCIA]" |
| [PROPOSTA] presente | PASS | "Formato de hypothesis_id [PROPOSTA]" |
| [DECISÃO NECESSÁRIA] presente | PASS | "J-001 em aberto — [DECISÃO NECESSÁRIA]" |

### 1.4 EARS Notation

| Check | Resultado | Evidência |
|---|---|---|
| "Quando <cond>, <comp> DEVE" | PASS | Seção "Critérios de Aceitação (EARS)" com 8 critérios |
| Critérios de aceitação em EARS | PASS | Ex.: "Quando Elliott Specialist solicita criação..., o sistema DEVE criar" |

### 1.5 BASpec Campos (ACENTUADOS)

| Check | Resultado | Evidência |
|---|---|---|
| QUANDO presente | PASS | Todas as 7 BASpecs possuem QUANDO |
| ENTÃO presente (acentuado) | PASS | Todas as 7 BASpecs possuem ENTÃO (com acento) |
| PORQUE presente | PASS | Todas as 7 BASpecs possuem PORQUE |
| REFERÊNCIA presente (acentuado) | PASS | Todas as 7 BASpecs possuem REFERÊNCIA (com acento) |
| VERIFICADO POR presente | PASS | Todas as 7 BASpecs possuem VERIFICADO POR com DADO/QUANDO/ENTÃO |

### 1.6 Enforcement Contract

| Check | Resultado | Evidência |
|---|---|---|
| CAPABILITY presente | PASS | 4 Enforcement Contracts com CAPABILITY |
| EFFECT presente | PASS | 4 ECs com EFFECT |
| PRECOND presente | PASS | 4 ECs com PRECOND |
| POSTCOND presente | PASS | 4 ECs com POSTCOND |
| POLICY presente | PASS | 4 ECs com POLICY |
| LEVEL presente | PASS | 4 ECs com LEVEL (E2 ou E3) |
| FAILURE-MODE presente | PASS | 4 ECs com FAILURE-MODE |
| EVIDENCE presente | PASS | 4 ECs com EVIDENCE |

### 1.7 Conviction Vector Não Fechado

| Check | Resultado | Evidência |
|---|---|---|
| Limiares marcados como pendentes | PASS | "J-001 em aberto — [DECISÃO NECESSÁRIA]" |
| Dimensionalidade=8 marcada como FATO NORMATIVO | PASS | "8 dimensões [FATO NORMATIVO: decisão homologada]" |
| J-001 em Decisões Abertas | PASS | Tabela "Decisões abertas" lista J-001 com "EM ABERTO — pendente" |

### 1.8 Status Epistemológico

| Check | Resultado | Evidência |
|---|---|---|
| FATO NORMATIVO usado | PASS | "CHM-001... FATO NORMATIVO (BASELINED)" |
| FATO ARQUITETURAL usado | PASS | "Hypothesis Registry... FATO ARQUITETURAL" |
| Documentado != homologado explícito | PASS | "CHM-001 e CEM-001 são FATO NORMATIVO (BASELINED)" |

### 1.9 IDs Internos (sem colisão com decisões abertas)

| Check | Resultado | Evidência |
|---|---|---|
| IDs de hipótese usam prefixo 3+ letras | PASS | HYP-A1, HYP-B2, HYP-C3, etc. (não H-001) |
| IDs de evidência usam prefixo 3+ letras | PASS | EV-101, EV-102, EV-105, etc. (não E-001) |
| Tokens Q-00X removidos | PASS | Decisões descritas por conteúdo ("decisão homologada") |
| J-001/M-001/N-001 com marcador pendência | PASS | Todos com "em aberto", "pendente" ou "[DECISÃO NECESSÁRIA]" |

---

## 2. Verificação de BASpecs

### 2.1 BASpec-HH-001 (Criação de Hipótese PRIMARY)

| Critério | Verificação |
|---|---|
| Condição observável | "Elliott Specialist identifica estrutura de onda válida com confiança >= 60%" |
| Comportamento específico | "Sistema cria objeto Hypothesis com hypothesis_type = PRIMARY" |
| Justificativa rastreável | "Somente Elliott cria hipótese estrutural/direcional" |
| REFERÊNCIA presente (acentuado) | "CHM-001 §3.1; decisão homologada; RULE-HH-001; RULE-HH-002" |
| Verificação com DADO/QUANDO/ENTÃO | Presente com input e expected output |
| **Resultado** | **PASS** |

### 2.2 BASpec-HH-002 (Criação de Hipótese SUB)

| Critério | Verificação |
|---|---|
| Condição observável | "SMC ou Fibonacci identifica sub-hipótese E existe PRIMARY ACTIVE/DOMINANT" |
| Comportamento específico | "Sistema cria Hypothesis com hypothesis_type = SUB, parent_hypothesis_id = [ID]" |
| Justificativa rastreável | "SUB deve sempre referenciar PRIMARY via parent_id" |
| REFERÊNCIA presente (acentuado) | "CHM-001 §1.8; decisão homologada; RULE-HH-003" |
| Verificação com DADO/QUANDO/ENTÃO | Presente |
| **Resultado** | **PASS** |

### 2.3 BASpec-HH-003 (Bloqueio de ICT)

| Critério | Verificação |
|---|---|
| Condição observável | "ICT Specialist tenta criar hipótese" |
| Comportamento específico | "Sistema REJEITA com erro ICT_NOT_HYPOTHESIS_PRODUCER" |
| Justificativa rastreável | "ICT não cria hipótese de nenhum tipo (INV-02)" |
| REFERÊNCIA presente (acentuado) | "Decisão homologada; INV-02; RULE-HH-004; RULE-ICT-007" |
| Verificação com DADO/QUANDO/ENTÃO | Presente com erro esperado |
| **Resultado** | **PASS** |

### 2.4 BASpec-HH-004 (Transição EMERGENT -> CANDIDATE)

| Critério | Verificação |
|---|---|
| Condição observável | "Hipótese em EMERGENT recebe supporting_evidence_ids com >= 1 evidência ACTIVE" |
| Comportamento específico | "Sistema transiciona epistemic_state para CANDIDATE" |
| Justificativa rastreável | "Hipótese com evidência parcial favorável elegível para avaliação" |
| REFERÊNCIA presente (acentuado) | "CHM-001 §4.3; RULE-HH-010" |
| Verificação com DADO/QUANDO/ENTÃO | Presente |
| **Resultado** | **PASS** |

### 2.5 BASpec-HH-005 (Transição CANDIDATE -> ACTIVE)

| Critério | Verificação |
|---|---|
| Condição observável | "Hipótese em CANDIDATE possui evidências suficientes E não possui refuting predominantes" |
| Comportamento específico | "Sistema transiciona epistemic_state para ACTIVE" |
| Justificativa rastreável | "ACTIVE = hipótese válida e sustentada" |
| REFERÊNCIA presente (acentuado) | "CHM-001 §4.3; §4.6; RULE-HH-011" |
| Verificação com DADO/QUANDO/ENTÃO | Presente |
| **Resultado** | **PASS** |

### 2.6 BASpec-HH-006 (Refutação)

| Critério | Verificação |
|---|---|
| Condição observável | "Hipótese recebe critério explícito de refutação" |
| Comportamento específico | "Sistema transiciona para REFUTED; NÃO deleta" |
| Justificativa rastreável | "REFUTED != DELETE; hipótese permanece para auditoria (INV-07)" |
| REFERÊNCIA presente (acentuado) | "CHM-001 §3.4; RULE-HH-021" |
| Verificação com DADO/QUANDO/ENTÃO | Presente |
| **Resultado** | **PASS** |

### 2.7 BASpec-HH-007 (Rejeição de Regressão)

| Critério | Verificação |
|---|---|
| Condição observável | "Sistema ou agente tenta transicionar para estado anterior" |
| Comportamento específico | "Sistema REJEITA com erro EPISTEMIC_REGRESSION_FORBIDDEN" |
| Justificativa rastreável | "Conhecimento não regride (CHM-001 §4.5)" |
| REFERÊNCIA presente (acentuado) | "CHM-001 §4.5; RULE-HH-012" |
| Verificação com DADO/QUANDO/ENTÃO | Presente |
| **Resultado** | **PASS** |

---

## 3. Verificação de Enforcement Contracts

### 3.1 EC-HH-001 (Criação de Hipótese)

| Campo | Valor | Conformidade |
|---|---|---|
| CAPABILITY | "Criar objeto Hypothesis no sistema" | Presente |
| EFFECT | "Publicação no Blackboard (workspace Hypotheses)" | Efeito externo |
| PRECOND | Validação de produtor, tipo, parent_id | Condições claras |
| POSTCOND | Hipótese existe em EMERGENT com ID alocado | Estado garantido |
| POLICY | "RULE-HH-001, RULE-HH-002, RULE-HH-003, RULE-HH-004" | RULEs existem |
| LEVEL | E2 (Operacional) | >= piso (Hipótese = E2 mínimo) |
| FAILURE-MODE | "Rejeitar criação; nenhuma hipótese publicada" | Fail-safe |
| EVIDENCE | "Log de criação com producer_id, hypothesis_id, timestamp" | Observável |
| **Resultado** | **PASS** |

### 3.2 EC-HH-002 (Transição de Estado)

| Campo | Valor | Conformidade |
|---|---|---|
| CAPABILITY | "Transicionar epistemic_state" | Presente |
| EFFECT | "Alteração de estado em objeto compartilhado; evento no Event Bus" | Efeito externo |
| PRECOND | Transição no grafo, não regressão, não órfã | Condições claras |
| POSTCOND | Estado atualizado, transition_record, evento emitido | Estado garantido |
| POLICY | "CHM-001 §4.3; RULE-HH-010, RULE-HH-011, RULE-HH-012" | Referências válidas |
| LEVEL | E2 (Operacional) | Apropriado |
| FAILURE-MODE | "Rejeitar transição; estado inalterado" | Fail-safe |
| EVIDENCE | "transition_record com from_state, to_state, timestamp" | Observável |
| **Resultado** | **PASS** |

### 3.3 EC-HH-003 (Promoção para ACTIVE/DOMINANT)

| Campo | Valor | Conformidade |
|---|---|---|
| CAPABILITY | "Promover hipótese a estado elegível para decisão" | Presente |
| EFFECT | "Hipótese torna-se base válida para sinal operacional" | Efeito crítico |
| PRECOND | Evidências ACTIVE, não órfã, parent válido | Condições claras |
| POSTCOND | Hipótese em ACTIVE ou DOMINANT | Estado garantido |
| POLICY | "CHM-001 §4.6; RULE-HH-011; Salvaguardas CEE-001 §11" | Referências válidas |
| LEVEL | E3 (Crítico) | Correto — base de decisão de trading |
| FAILURE-MODE | "Fail-closed: não promover; permanece no estado anterior" | Fail-closed para E3 |
| EVIDENCE | "Registro de promoção; audit trail para P13" | Observável |
| **Resultado** | **PASS** |

### 3.4 EC-HH-004 (Refutação)

| Campo | Valor | Conformidade |
|---|---|---|
| CAPABILITY | "Transicionar hipótese para REFUTED" | Presente |
| EFFECT | "Hipótese deixa de ser elegível; permanece para auditoria" | Efeito |
| PRECOND | Critério de refutação explícito observado | Condição clara |
| POSTCOND | REFUTED; objeto preservado (INV-07) | Estado garantido |
| POLICY | "CHM-001 §3.4; RULE-HH-021; INV-07" | Referências válidas |
| LEVEL | E2 (Operacional) | Apropriado |
| FAILURE-MODE | "Rejeitar e solicitar justificativa" | Fail-safe |
| EVIDENCE | "refutation_record com motivo, timestamp, evidence_ids" | Observável |
| **Resultado** | **PASS** |

---

## 4. Verificação de Consistência (CONS-01)

| Decisão Aberta | Aparece como fechado? | Marcador de pendência presente? | Resultado |
|---|---|---|---|
| J-001 | Não | Sim ("em aberto", "pendente", "[DECISÃO NECESSÁRIA]") | PASS |
| M-001 | Não | Sim ("em aberto — pendente") | PASS |
| N-001 | Não | Sim ("em aberto — pendente") | PASS |

---

## 5. Verificação de Integridade

### 5.1 Referências a RULEs

| RULE citada | Existe em RULES.md? | Resultado |
|---|---|---|
| RULE-HH-001..004 | Criadas nesta Spec | OK (novas) |
| RULE-HH-010..013 | Criadas nesta Spec | OK (novas) |
| RULE-HH-020..021 | Criadas nesta Spec | OK (novas) |
| RULE-HH-030..031 | Criadas nesta Spec | OK (novas) |
| RULE-BB-002 | Sim (RULES.md) | PASS |
| RULE-BB-004 | Sim (RULES.md) | PASS |
| RULE-ICT-007 | Sim (RULES.md) | PASS |

### 5.2 Referências a Fontes

| Fonte citada | Existe? | Resultado |
|---|---|---|
| CHM-001 §1.8, §2.7, §2.10, §3.1, §3.4, §4.2, §4.3, §4.5, §4.6, §4.12 | Sim (canon/CHM-001) | PASS |
| CEM-001 Cap.1, Cap.2, Cap.4 | Sim (canon/CEM-001) | PASS |
| Decisões homologadas (PRIMARY/SUB, estados, dimensões) | Sim (respostas-questionario-v1) | PASS |
| CONSTITUTION P13, hierarquia | Sim (governance/CONSTITUTION) | PASS |
| INV-02, INV-07 | Sim (ATOMIC-SPEC §13) | PASS |

---

## 6. Resumo da Verificação

| Categoria | Checks | Resultado |
|---|---|---|
| Estrutura (cabeçalho, Constitution Check, IDs) | 12 | 12 PASS |
| BASpecs (7 unidades) | 7 | 7 PASS |
| Enforcement Contracts (4 unidades) | 4 | 4 PASS |
| Consistência CONS-01 | 3 | 3 PASS |
| Integridade de referências | 12 | 12 PASS |
| **TOTAL** | **38** | **38 PASS** |

---

## 7. Conclusão

A SPEC-001 (Hypothesis Harness) passou em todas as verificações de spec após correções:

1. **Cabeçalho:** formato sem markdown para regex (`Complexidade: CRITICAL`, `Profundidade-alvo: D0–D8` na v1.1).
2. **BASpecs acentuadas:** ENTÃO e REFERÊNCIA com acentos corretos.
3. **IDs sem colisão:** prefixos HYP-, EV-, CONV- (não H-001, E-001).
4. **Tokens Q-00X removidos:** decisões descritas por conteúdo.
5. **J-001/M-001/N-001:** sempre com marcadores de pendência próximos.

**Status:** PRONTO PARA REVISÃO pelo Revisor (protocolo semântico GRE-001/HRE-001).

**Gate determinístico:** `python scripts/validate_spec_sot.py specs/features/SPEC-001/plan.md` deve retornar EXIT 0.

**[DECISÃO NECESSÁRIA] que permanece em aberto:**
- **J-001** — Fórmula/pesos/limiares definitivos do Conviction Vector (em aberto — pendente)
- **M-001** — Estados do Blackboard para objetos não-hipótese (em aberto — pendente)
- **N-001** — Pesos por ativo do Conviction Vector (em aberto — pendente)
