# REAUDITORIA-SPEC002-001 — Proposta de Correções — SPEC-002

> **Status:** PROPOSTA — NÃO HOMOLOGADA  
> **Natureza:** artefato de revisão / sugestão de correções  
> **Regra de integridade:** este documento **não altera** `SPEC-002`, `CEM-001`, `RULES.md`, `SPEC-003` ou qualquer outro artefato normativo.  
> **Objetivo:** registrar, de forma executável e rastreável, as correções sugeridas após auditoria semântica da SPEC-002 pelas mesmas lentes aplicadas à SPEC-001.

---

## 1. Escopo da proposta

A SPEC-002 v1.0 permanece como baseline histórica.

Esta proposta não constitui uma nova versão da SPEC-002 e não deve ser interpretada como alteração normativa.

O objetivo é fornecer ao Especificador, Revisor e Controlador um conjunto de mudanças sugeridas para eventual adoção formal.

### Princípio

```
AUDITORIA
   ↓
ACHADO
   ↓
PROPOSTA
   ↓
DECISÃO
   ↓
SE APROVADA → EMENDA/ERRATUM
   ↓
VALIDAÇÃO
   ↓
RE-HOMOLOGAÇÃO
```

Nenhuma regra desta proposta deve ser considerada vigente antes da decisão e homologação correspondentes.

---

# 2. Resumo dos achados

| ID | Tema | Severidade proposta | Ação |
|---|---|---:|---|
| P0-EH-001 | Identidade autenticada do produtor | P0 | Corrigir EC-EH-001 |
| P1-EH-002 | Imutabilidade de Evidence vs `_operational` | P1 | Redefinir representação operacional |
| P1-EH-003 | INV-04 deve ser boundary estrutural | P1 | Fortalecer EC-EH-002 |
| P1-EH-004 | CCM-001 historicamente desatualizado | P1 | Erratum documental |
| P1-EH-005 | RULE-EH com estados divergentes | P1 | Reconciliar governança |
| P2-EH-006 | BL-012 pós-homologação | P2 | Resolver encaminhamento |
| P1-EH-007 | M-001 como dependência de implementação | P1 | Explicitar readiness |

---

# 3. P0-EH-001 — Identidade autenticada do produtor

## Problema

O EC-EH-001 exige produtor autorizado, mas não torna suficientemente explícita a origem confiável de `producer_id`.

O risco é permitir que o payload fornecido pelo agente declare sua própria identidade.

Isso enfraquece a própria finalidade da Evidence Provenance.

## Invariante proposta

```
IDENTIDADE AUTENTICADA PELO RUNTIME
        ↓
AUTORIZAÇÃO
        ↓
CAPABILITY
        ↓
producer_id
        ↓
Evidence
```

O campo `producer_id` recebido no payload não deve possuir autoridade para estabelecer a identidade do produtor.

## Patch conceitual sugerido

Adicionar ao EC-EH-001:

```text
IDENTITY PRECONDITION:
producer_id MUST derive from authenticated runtime identity.

A payload-declared producer_id MUST NOT establish producer identity.

If payload producer_id differs from authenticated runtime identity:
  REJECT
  FAIL-CLOSED
  ERROR = PRODUCER_IDENTITY_MISMATCH
  NO EVIDENCE PUBLICATION
```

## Teste proposto

```text
TEST-EH-IDENTITY-001

Given:
  authenticated_runtime_identity = agent-A

And:
  payload.producer_id = agent-B

Then:
  creation MUST be rejected
  error MUST be PRODUCER_IDENTITY_MISMATCH
  no Evidence MUST be published
```

## Estado

```
SPECIFICADO: NÃO SUFICIENTEMENTE
IMPLEMENTADO: NÃO PROVADO
PROVADO: NÃO
```

---

# 4. P1-EH-002 — Imutabilidade da Evidence e representação operacional

## Problema

A SPEC-002 protege a Evidence publicada contra mutações incompatíveis com CEM-001, mas também propõe atributos operacionais como:

- typology
- relationship/dependence attribute
- staleness
- conflict references

em `_operational`.

Isso pode criar uma tensão entre:

```
Evidence publicada = objeto canônico imutável
```

e:

```
Evidence publicada → atualização operacional posterior
```

Especialmente `staleness`, que muda com o tempo.

## Proposta preferencial

Manter a Evidence canônica imutável e representar avaliações operacionais como registros append-only.

```
Evidence EV-001
      │
      ├── OperationalAssessment-001
      ├── OperationalAssessment-002
      └── OperationalAssessment-N
```

Cada avaliação pode registrar:

```text
assessment_id
evidence_id
assessment_type
value
assessed_at
producer/runtime identity
method
source_refs
version
```

## Alternativa

Quando o valor puder ser calculado deterministicamente a partir de dados existentes, considerar atributo derivado em leitura, sem persistir mutação no objeto Evidence.

## Decisão recomendada

**Preferir append-only Operational Assessment**, pois preserva melhor:

- temporalidade
- reconstrução histórica
- auditabilidade
- explicabilidade
- ausência de mutação silenciosa

---

# 5. P1-EH-003 — INV-04 como boundary estrutural

## Problema

A proteção de:

```
Evidence Strength ≠ Conviction
```

está conceitualmente correta.

Entretanto, detectar uma tentativa de converter Strength em Conviction não deve depender exclusivamente de detector semântico.

## Proposta

Transformar a separação em capability boundary.

```
Evidence Capability
       │
       X
       │
Conviction Capability
```

A camada de Evidence não deve possuir capacidade de escrever diretamente em campos ou estruturas pertencentes ao domínio de Conviction.

## Regra proposta

```text
Evidence Strength MAY be persisted and queried within Evidence scope.

Evidence Strength MUST NOT directly populate, overwrite,
or authorize Conviction values.

Conviction values MUST be produced through the Conviction
contract defined by the canonical Conviction Model.
```

## Benefício

A proteção passa de:

```
"detectar violação"
```

para:

```
"tornar a operação proibida por construção"
```

---

# 6. P1-EH-004 — Reconciliação histórica do CCM-001

## Problema

A SPEC-002 foi homologada em 2026-09-28 quando o CCM-001 ainda estava pendente.

Posteriormente, a SPEC-003 foi homologada e passou a estabelecer o CCM-001 vigente.

Não reescrever a história da SPEC-002.

## Erratum sugerido

Adicionar aditivo documental:

```text
As referências ao CCM-001 como PENDENTE correspondem ao estado
epistemológico existente na data de homologação da SPEC-002.

Estado atual:

CCM-001 = BASELINED via SPEC-003 / DHR-SPEC003-001.

A SPEC-002 não define nem redefine:
- fórmula de Conviction
- pesos
- thresholds
- composição do Conviction Vector

Esses elementos permanecem sob o CCM-001 vigente.
```

## Regra

O histórico da SPEC-002 deve permanecer preservado.

A correção deve ser aditiva.

---

# 7. P1-EH-005 — Reconciliação do status de RULE-EH

## Problema

Há referências que apresentam RULE-EH-001..008 como `[PROPOSTA]`, enquanto a ata de homologação registra essas regras como FATO NORMATIVO com vigência imediata.

Existe, portanto, divergência entre:

```
Plan / Checks
        ↕
DHR
        ↕
RULES.md
```

## Proposta

Escolher um único estado normativo.

Como a ata já homologou RULE-EH-001..008, a recomendação é:

```
RULE-EH-001..008
= FATO NORMATIVO BASELINED
```

e registrar fisicamente o conjunto em:

```
governance/RULES.md
```

## Condição

A adoção desta proposta deve ocorrer por alteração normativa própria, não por esta proposta.

---

# 8. P2-EH-006 — BL-012

## Situação

A homologação da SPEC-002 disparou o BL-012.

O backlog registra o item como ATIVADO, com encaminhamento para:

- mapear COG-SPEC
- reconciliar com N8–N17
- rejeitar R-05
- preservar os estados canônicos de CEM-001/CHM-001

## Proposta

Não modificar a SPEC-002 para absorver esse trabalho.

Tratar BL-012 como efeito de governança separado:

```
ATIVADO
  ↓
DECISÃO / EXECUÇÃO
  ↓
VALIDAÇÃO
  ↓
CONCLUÍDO ou NOVO ENCAMINHAMENTO
```

---

# 9. P1-EH-007 — Dependência M-001

## Problema

A SPEC-002 corretamente não inventa os estados do Blackboard para Evidence.

Porém, isso significa que a implementação completa do protocolo de publicação depende da definição de M-001/SPEC correspondente.

## Proposta

Explicitar a distinção:

```
SPEC-002 = BASELINE SEMÂNTICA
```

mas:

```
RUNTIME READINESS
= BLOCKED BY M-001
```

até que o contrato de Blackboard necessário esteja disponível.

Isso evita interpretar "SPEC HOMOLOGADA" como "runtime pronto".

---

# 10. Modelo global de enforcement recomendado

Os achados da SPEC-001 e SPEC-002 sugerem um padrão transversal.

Para objetos cognitivos com efeitos no sistema:

```
COGNITIVE TIME
Agent / LLM reasoning
        ↓
Cognitive Contract

RUNTIME TIME
Authenticated Identity
        ↓
Authorization
        ↓
Capability
        ↓
Schema
        ↓
State / Lifecycle
        ↓
Domain Contract
        ↓
Persistence
        ↓
Event
        ↓
Audit

DELIVERY TIME
Spec Validator
        ↓
Tests
        ↓
CI
        ↓
Regression
        ↓
Artifact Integrity
```

Este modelo é uma **proposta arquitetural transversal**, não uma alteração automática da SPEC-002.

---

# 11. O que NÃO deve ser alterado

A eventual correção da SPEC-002 não deve:

- redefinir CEM-001
- redefinir CHM-001
- antecipar Conviction
- fechar decisões J-001 já resolvidas pela evolução posterior
- absorver M-001
- absorver SPEC-003
- criar uma segunda Evidence Layer
- transformar Strength em Conviction
- delegar decisões críticas a LLM
- transformar detector semântico em único mecanismo de segurança
- reescrever o histórico da homologação v1.0

---

# 12. Critério de aceite da futura correção

Uma futura emenda/revisão da SPEC-002 deveria ser considerada conforme somente se:

- [ ] identidade do produtor for derivada de contexto autenticado do runtime
- [ ] divergência de identidade resultar em fail-closed
- [ ] Evidence canônica permanecer imutável após publicação
- [ ] atributos operacionais tiverem representação compatível com imutabilidade
- [ ] Strength não puder escrever diretamente em Conviction
- [ ] CCM-001 atual estiver reconciliado documentalmente
- [ ] RULE-EH possuir estado único em todos os artefatos
- [ ] BL-012 possuir encaminhamento rastreável
- [ ] dependência M-001 estiver explicitamente classificada
- [ ] SPECIFICADO / IMPLEMENTADO / PROVADO permanecerem separados
- [ ] validator determinístico continuar sendo gate de entrega
- [ ] testes adversariais cobrirem identidade, mutabilidade e boundary Strength→Conviction

---

# 13. Classificação final desta proposta

```
P0 — 1
P1 — 5
P2 — 1

NÃO HÁ PROPOSTA DE REESCRITA DA SPEC-002.

Tipo de intervenção:
CORREÇÃO PONTUAL + ERRATA + RECONCILIAÇÃO
```

## Decisão recomendada

```
SPEC-002 v1.0
      ↓
MANTER COMO BASELINE HISTÓRICA
      ↓
ESTE DOCUMENTO
      ↓
DECISÃO DE ANDRAUS
      ↓
EMENDAS/ERRATA APROVADAS
      ↓
VALIDAÇÃO
      ↓
RE-HOMOLOGAÇÃO CORRETIVA
```

**Este arquivo não possui autoridade normativa.**
