# SPEC-001 — Hypothesis Harness

Versão: 1.1
Status: HOMOLOGADA — BASELINE (Andraus, 2026-09-15)
Complexidade: CRITICAL
Profundidade-alvo: D0–D8
Posição no caminho crítico: 1a Spec autorizada (ROADMAP §4)
Nível de maturidade: L2 (Guiado)
Método: atomic-spec.md v1.3 (BASpec, EARS, Enforcement Contract)
Autor: Especificador Principal (Claude Code)
Data: 2026-09-15

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-09-15 | Entrega candidata inicial (D0–D7). |
| 1.1 | 2026-09-15 | Correções homologadas por Andraus: (F-01) profundidade elevada a D0–D8 + seção D8 adversarial formal; (M-01) `QUANDO` da BASpec-HH-005 reescrito para condição observável; (M-03) EC-COG-004/005 etiquetados em TRACE-06; (M-04) Non-goal explícito de latência do Event Bus. Parecer do Revisor: **CONFORME** (1 achado Menor, MEN-01, não-bloqueante). MEN-01 registrado nas Decisões Abertas e encaminhado à SPEC-003. **HOMOLOGADA como baseline** por Andraus. |

---

## Constitution Check

- [x] **Hierarquia Elliott-Fibonacci-Fractal-SMC-ICT respeitada:** a SPEC-001 não redefine a hierarquia; apenas especifica protocolos operacionais para hipóteses criadas de acordo com ela. [FONTE: CONSTITUTION.md; INV-01]
- [x] **Não redefine nenhum Modelo Canônico (CEM/CHM/CCM/CDM/CNM):** a SPEC-001 constrói SOBRE o CHM-001 (BASELINED); não redefine estrutura, taxonomia, estados nem Confidence. [FONTE: CHM-001; CONST-01]
- [x] **Conviction Vector tratado como PENDENTE (J-001 em aberto):** dimensionalidade = 8 (FATO NORMATIVO, decisão homologada); limiares de Fase Piloto (>=70%, 7/9) = FATO NORMATIVO interino, recalibrável após backtest; fórmula/pesos/limiares definitivos = **J-001 em aberto** — [DECISÃO NECESSÁRIA]. A hipótese referencia o objeto de convicção, não o calcula.
- [x] **Nenhuma das 5 Salvaguardas Constitucionais (CEE-001 §10/§11) violada:** SPEC-001 não altera salvaguardas de economia/roteamento (§10) nem de sinal de trading (§11).
- [x] **Complexidade declarada:** CRITICAL (P0, núcleo cognitivo, dependência transitiva de todas as Specs downstream).

---

## D0 — Missão (Intenção)

O Hypothesis Harness é a camada operacional que especifica **como o SOT cria, promove, refuta e arquiva hipóteses em tempo de execução**, construindo sobre o modelo canônico CHM-001 (BASELINED). [FONTE: ROADMAP.md §4]

O Harness **não redefine** a estrutura do objeto hipótese (que é responsabilidade do CHM-001); ele especifica:

1. Protocolos de criação, atualização e transição de estado.
2. Distinção operacional PRIMARY/SUB com herança fractal.
3. Hypothesis Registry como serviço lógico.
4. Protocolo de publicação no Blackboard.
5. Integração com Evidências (por referência ao CEM-001).
6. Slot de convicção operacional (referência ao CCM-001, pendente de redação).
7. Auditabilidade (suporte a P13: toda decisão reconstituível).

**Status epistemológico:** a SPEC-001 é FATO ARQUITETURAL candidato a baseline; CHM-001 e CEM-001 são FATO NORMATIVO (BASELINED); CCM-001 é PENDENTE DE REDAÇÃO (SPEC-003).

---

## D1 — Escopo e Non-goals

### Dentro do escopo (SPEC-001)

| Item | Descrição | Fonte |
|---|---|---|
| Protocolos de transição | Regras operacionais para percorrer os 7 estados canônicos do CHM-001 | CHM-001 Cap.4 |
| PRIMARY/SUB | Elliott cria hipótese PRIMARY; SMC/Fibonacci criam SUB com `parent_id` obrigatório; ICT não cria hipótese | Decisão homologada (hipótese primária/sub) |
| Hypothesis Registry | Alocação de ID, versionamento monotônico, índice de estado ativo, API de consulta | ROADMAP §4 |
| Protocolo Blackboard | O que publicar, quando, em que ordem, com que versionamento | ROADMAP §4; EC-COG-004 |
| Integração com Evidência | Referência por Evidence ID (CEM-001); não copia | CHM-001 §2.10 |
| Slot de convicção | Hipótese referencia objeto de convicção; não calcula convicção | CHM-001 §1.9 |
| Herança fractal | Propagação parent/child em operação (graus/timeframes) | CHM-001 §1.8 |
| Auditabilidade | O que o modelo deve suportar para reconstrução (P13) | CONSTITUTION P13 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Redefinir estrutura do CHM-001 | CHM-001 (BASELINED) | CONST-01 |
| Fórmula/pesos/limiares do Conviction Vector | SPEC-003 (CCM-001) | J-001 em aberto — [DECISÃO NECESSÁRIA] |
| Separação Conviction/Synthesis | Decisão fechada | Topologia já decidida: Fusion-Conviction-Synthesis |
| Schema físico de armazenamento | SPEC-004/006 | Blackboard vs KG = decisão de infraestrutura |
| Camada operacional de Evidence | SPEC-002 | Provenance, qualidade, fusão |
| Estados do Blackboard para objetos não-hipótese | SPEC-004 | M-001 em aberto — pendente |
| Orçamento de latência e entrega do Event Bus | SPEC-005 | SPEC-001 apenas **emite** eventos; produtor não tem autoridade para definir metadados de transporte (Latency/Freshness/Reliability/Expiration) — [FONTE: SAS-001 §6.7]. Contrato do Event Bus (TTL, delivery, latência) pertence à SPEC-005 (ROADMAP §SPEC-005) |

**Errata aditiva (2026-10-05):** a âncora `[FONTE: SAS-001 §6.7]` acima deve ser lida como **SAS-001 §6.10** (Metadados Operacionais de Infraestrutura; §6.9 = integração com o Event Bus) — ver `governance/ERRATUM-SPEC001-001_Ancora_SAS-001_6.10.md`. Texto acima não alterado (INV-09).

---

## D2 — Regras

### Regras de criação

```
RULE-HH-001: Somente produtores autorizados podem criar hipóteses.
             Produtores autorizados: Elliott Specialist, SMC Specialist, Fibonacci Validator.
             ICT NÃO é produtor autorizado. [FONTE: decisão homologada; INV-02]

RULE-HH-002: Toda hipótese PRIMARY deve ser criada exclusivamente pelo Elliott Specialist.
             Hipótese PRIMARY = hipótese estrutural/direcional que define o bias do mercado.
             [FONTE: decisão homologada; CONSTITUTION hierarquia]

RULE-HH-003: Toda hipótese SUB deve possuir campo `parent_id` referenciando hipótese PRIMARY válida.
             SUB sem parent_id = Hipótese Órfã (CHM-001 §2.10.1) — não pode atingir ACTIVE/DOMINANT.
             [FONTE: decisão homologada; CHM-001 §1.8]

RULE-HH-004: ICT Specialist NÃO cria hipótese de nenhum tipo (nem PRIMARY nem SUB).
             ICT confirma ou invalida execução de hipótese existente. [FONTE: decisão homologada; INV-02]
```

### Regras de transição de estado

```
RULE-HH-010: Os únicos estados válidos para uma hipótese são os 7 canônicos do CHM-001:
             EMERGENT, CANDIDATE, ACTIVE, DOMINANT, SUPERSEDED, REFUTED, ARCHIVED.
             RULE-BB-003 (PROPOSED/VALIDATED) está SUPERSEDED. [FONTE: decisão homologada; CHM-001 §4.2]

RULE-HH-011: Hipótese só pode ser base de decisão operacional nos estados ACTIVE ou DOMINANT.
             Hipótese em EMERGENT/CANDIDATE não pode sustentar sinal. [FONTE: CHM-001 §4.6; CONSTITUTION]

RULE-HH-012: Transições permitidas são exclusivamente as do Grafo Canônico (CHM-001 §4.3).
             Transições proibidas: DOMINANT->ACTIVE, ACTIVE->CANDIDATE, CANDIDATE->EMERGENT (regressão).
             [FONTE: CHM-001 §4.4, §4.5]

RULE-HH-013: Hipótese Órfã (sem supporting_evidence_ids válidos) não pode atingir ACTIVE/DOMINANT.
             [FONTE: CHM-001 §2.10.1, RN-3]
```

### Regras de versionamento

```
RULE-HH-020: Linhagem histórica de versões é monotônica e append-only.
             Nenhuma versão anterior pode ser removida/reordenada/substituída retroativamente.
             [FONTE: CHM-001 §3.3; INV-07]

RULE-HH-021: REFUTED/SUPERSEDED/ARCHIVED não deletam a hipótese — alteram apenas estado epistêmico.
             O objeto permanece disponível para auditoria. [FONTE: CHM-001 §3.4, §3.5; INV-07]
```

### Regras de publicação

```
RULE-HH-030: Toda hipótese publicada no Blackboard deve referenciar evidências via Evidence ID (CEM-001).
             Nunca copiar o objeto Evidence — apenas o ID. [FONTE: CHM-001 §2.10; RULE-BB-002]

RULE-HH-031: Publicação no Blackboard é append-only durante análise.
             [FONTE: RULE-BB-004; CONSTITUTION regra 4 do Blackboard]
```

---

## Critérios de Aceitação (EARS)

Os critérios de aceitação seguem notação EARS ("Quando <condição>, o componente DEVE <resposta>"):

1. Quando Elliott Specialist solicita criação de hipótese PRIMARY, o sistema DEVE criar objeto com hypothesis_type = PRIMARY e epistemic_state = EMERGENT.

2. Quando agente não-autorizado (ex.: ICT) tenta criar hipótese, o sistema DEVE rejeitar a operação com erro específico.

3. Quando hipótese SUB é criada sem parent_id válido, o sistema DEVE rejeitar a operação.

4. Quando hipótese em EMERGENT recebe evidência ACTIVE válida, o sistema DEVE transicionar para CANDIDATE.

5. Quando hipótese atinge ACTIVE ou DOMINANT, o sistema DEVE permitir que ela sustente decisão operacional.

6. Quando agente tenta transição de regressão epistêmica (ex.: ACTIVE para CANDIDATE), o sistema DEVE rejeitar a operação.

7. Quando hipótese é refutada, o sistema DEVE alterar estado para REFUTED mas NÃO DEVE deletar o objeto (INV-07).

8. Quando hipótese é publicada no Blackboard, o sistema DEVE emitir evento "Hypothesis.Created" no Event Bus.

---

## D3 — Comportamento (BASpecs)

### BASpec-HH-001 — Criação de Hipótese PRIMARY

```
BASpec-HH-001:
  QUANDO:       Elliott Specialist identifica estrutura de onda válida com confiança >= 60%
                e nenhuma hipótese PRIMARY ACTIVE/DOMINANT conflitante existe para o mesmo
                ativo/grau/timeframe
  ENTÃO:        Sistema cria objeto Hypothesis com:
                - hypothesis_type = PRIMARY
                - producer_id = Elliott Specialist
                - epistemic_state = EMERGENT
                - confidence = [valor atribuído pelo produtor]
                - parent_hypothesis_id = null (PRIMARY não tem parent)
                - supporting_evidence_ids = [lista inicial]
                - version = 1
                - hypothesis_id = gerado pelo Hypothesis Registry
  PORQUE:       Somente Elliott cria hipótese estrutural/direcional (decisão homologada); hipóteses
                iniciam em EMERGENT (CHM-001 §3.1); versionamento monotônico (INV-07)
  REFERÊNCIA:   CHM-001 §3.1; decisão homologada; RULE-HH-001; RULE-HH-002
  VERIFICADO POR:
    DADO        Elliott Specialist com contagem válida em BTC/H4, confidence = 0.72
    QUANDO      Elliott invoca createHypothesis(type=PRIMARY, confidence=0.72, evidence=[EV-101])
    ENTÃO       Sistema retorna Hypothesis com hypothesis_id != null, version = 1,
                epistemic_state = EMERGENT, parent_hypothesis_id = null
    VERIFICAÇÃO hypothesis.hypothesis_type == PRIMARY; hypothesis.producer_id == "elliott_specialist"
```

### BASpec-HH-002 — Criação de Hipótese SUB

```
BASpec-HH-002:
  QUANDO:       SMC Specialist ou Fibonacci Validator identifica sub-hipótese de domínio
                E existe hipótese PRIMARY em estado ACTIVE ou DOMINANT com parent_id válido
  ENTÃO:        Sistema cria objeto Hypothesis com:
                - hypothesis_type = SUB
                - producer_id = [agente que criou]
                - epistemic_state = EMERGENT
                - parent_hypothesis_id = [ID da PRIMARY pai]
                - supporting_evidence_ids = [lista inicial]
  PORQUE:       SUB deve sempre referenciar PRIMARY via parent_id (decisão homologada); herança fractal
                do CHM-001; sub-hipótese sem pai válido é Órfã
  REFERÊNCIA:   CHM-001 §1.8; decisão homologada; RULE-HH-003
  VERIFICADO POR:
    DADO        Hipótese PRIMARY HYP-A1 em estado ACTIVE; SMC identifica BOS relevante
    QUANDO      SMC invoca createHypothesis(type=SUB, parent_id=HYP-A1, confidence=0.68)
    ENTÃO       Sistema retorna Hypothesis com parent_hypothesis_id = HYP-A1, hypothesis_type = SUB
    VERIFICAÇÃO hypothesis.parent_hypothesis_id == "HYP-A1"
```

### BASpec-HH-003 — Bloqueio de Criação por ICT

```
BASpec-HH-003:
  QUANDO:       ICT Specialist tenta criar hipótese (PRIMARY ou SUB)
  ENTÃO:        Sistema REJEITA a operação com erro "ICT_NOT_HYPOTHESIS_PRODUCER"
  PORQUE:       ICT não cria hipótese de nenhum tipo — confirma/invalida execução (INV-02)
  REFERÊNCIA:   Decisão homologada; INV-02; RULE-HH-004; RULE-ICT-007
  VERIFICADO POR:
    DADO        ICT Specialist com suposta estrutura de execução
    QUANDO      ICT invoca createHypothesis(type=SUB, parent_id=HYP-A1)
    ENTÃO       Sistema retorna erro 403 com código "ICT_NOT_HYPOTHESIS_PRODUCER"
    VERIFICAÇÃO response.error_code == "ICT_NOT_HYPOTHESIS_PRODUCER"
```

### BASpec-HH-004 — Transição EMERGENT para CANDIDATE

```
BASpec-HH-004:
  QUANDO:       Hipótese em EMERGENT recebe supporting_evidence_ids com >= 1 evidência ACTIVE
                E não é Hipótese Órfã
  ENTÃO:        Sistema transiciona epistemic_state para CANDIDATE
                Registra evento de transição no histórico (timestamp, origem, justificativa)
  PORQUE:       Hipótese com evidência parcial favorável elegível para avaliação (CHM-001 §2.7);
                histórico de transições obrigatório (CHM-001 §4.12)
  REFERÊNCIA:   CHM-001 §4.3; RULE-HH-010
  VERIFICADO POR:
    DADO        Hipótese HYP-B2 em EMERGENT com supporting_evidence_ids = []
    QUANDO      Sistema adiciona Evidence EV-105 (ACTIVE) a supporting_evidence_ids
    ENTÃO       HYP-B2.epistemic_state transiciona para CANDIDATE
    VERIFICAÇÃO HYP-B2.epistemic_state == CANDIDATE; HYP-B2.transition_history.length > 0
```

### BASpec-HH-005 — Transição CANDIDATE para ACTIVE

```
BASpec-HH-005:
  QUANDO:       Hipótese em CANDIDATE satisfaz a precondição observável de EC-HH-003, a saber:
                (1) supporting_evidence_ids.length >= 1
                (2) TODAS as evidências em supporting_evidence_ids apontam para Evidence em estado ACTIVE
                (3) hipótese NÃO é Órfã (CHM-001 §4.6 / ADR-CHM-001-008)
                E não-predominância de contraevidência, definida de forma observável para a
                Fase Piloto como:
                    count(refuting_evidence_ids ACTIVE) < count(supporting_evidence_ids ACTIVE)
                E (se SUB) parent_hypothesis está em ACTIVE ou DOMINANT
                [DECISÃO NECESSÁRIA: J-001 — em aberto] A ponderação definitiva por dimensão de
                convicção (peso relativo de cada Evidence) substituirá a contagem simples acima.
                Impacto declarado na testabilidade: enquanto J-001 estiver em aberto, a
                não-predominância é gate-checkável apenas pela regra de contagem da Fase Piloto;
                o critério ponderado final é responsabilidade da SPEC-003 (CCM-001).
  ENTÃO:        Sistema transiciona epistemic_state para ACTIVE
                Hipótese torna-se elegível para sustentar decisão operacional
  PORQUE:       ACTIVE = hipótese válida e sustentada pelas evidências (CHM-001 §2.7);
                somente ACTIVE/DOMINANT sustentam decisão (RULE-HH-011); a condição de promoção
                deve ser observável por gate determinístico (EC-HH-003)
  REFERÊNCIA:   CHM-001 §4.3; §4.6; RULE-HH-011; EC-HH-003; J-001 (em aberto)
  VERIFICADO POR:
    DADO        Hipótese HYP-C3 em CANDIDATE, não-Órfã, com supporting_evidence_ids = 3 Evidence
                ACTIVE e refuting_evidence_ids = 1 Evidence ACTIVE (1 < 3 → não-predominante)
    QUANDO      Sistema avalia a precondição de EC-HH-003 e a regra de contagem de não-predominância
    ENTÃO       HYP-C3.epistemic_state transiciona para ACTIVE
    VERIFICAÇÃO HYP-C3.epistemic_state == ACTIVE;
                count(refuting ACTIVE)=1 < count(supporting ACTIVE)=3
```

### BASpec-HH-006 — Refutação de Hipótese

```
BASpec-HH-006:
  QUANDO:       Hipótese em CANDIDATE/ACTIVE/DOMINANT recebe critério explícito de refutação
                (invalidador observado, contraevidência predominante, regra Elliott violada)
  ENTÃO:        Sistema transiciona epistemic_state para REFUTED
                NÃO deleta a hipótese — altera apenas estado epistêmico
                Registra motivo da refutação no histórico
  PORQUE:       REFUTED != DELETE; hipótese permanece para auditoria (CHM-001 §3.4; INV-07)
  REFERÊNCIA:   CHM-001 §3.4; RULE-HH-021
  VERIFICADO POR:
    DADO        Hipótese HYP-D4 em ACTIVE com invalidador declarado em nível X
    QUANDO      Preço viola nível X (invalidador observado)
    ENTÃO       HYP-D4.epistemic_state = REFUTED; HYP-D4 permanece no Blackboard
    VERIFICAÇÃO HYP-D4.epistemic_state == REFUTED; Blackboard.contains(HYP-D4) == true
```

### BASpec-HH-007 — Rejeição de Regressão Epistêmica

```
BASpec-HH-007:
  QUANDO:       Sistema ou agente tenta transicionar hipótese para estado anterior
                (ex.: DOMINANT -> ACTIVE, ACTIVE -> CANDIDATE, CANDIDATE -> EMERGENT)
  ENTÃO:        Sistema REJEITA a operação com erro "EPISTEMIC_REGRESSION_FORBIDDEN"
  PORQUE:       Conhecimento pode ser substituído/refutado/arquivado, não regride (CHM-001 §4.5)
  REFERÊNCIA:   CHM-001 §4.5; RULE-HH-012
  VERIFICADO POR:
    DADO        Hipótese HYP-E5 em ACTIVE
    QUANDO      Agente invoca transitionState(HYP-E5, CANDIDATE)
    ENTÃO       Sistema retorna erro "EPISTEMIC_REGRESSION_FORBIDDEN"
    VERIFICAÇÃO response.error_code == "EPISTEMIC_REGRESSION_FORBIDDEN"
```

---

## D5 — Máquina de Estados (CHM-001)

A máquina de estados da hipótese é a do CHM-001 (Cap.4) — a SPEC-001 **não redefine**.

### Estados Canônicos [FONTE: CHM-001 §4.2]

| Estado | Descrição | Elegível para decisão? |
|---|---|---|
| EMERGENT | Recém-formulada, sem validação suficiente | Não |
| CANDIDATE | Em avaliação com evidências favoráveis parciais | Não |
| ACTIVE | Válida e sustentada pelas evidências disponíveis | **Sim** |
| DOMINANT | Preferencial entre hipóteses concorrentes compatíveis | **Sim** |
| SUPERSEDED | Substituída por versão posterior ou hipótese superior | Não |
| REFUTED | Invalidada por critério explícito de refutação | Não |
| ARCHIVED | Retirada da camada operacional, preservada historicamente | Não |

### Grafo de Transições Permitidas [FONTE: CHM-001 §4.3]

```
EMERGENT    -> CANDIDATE | ARCHIVED
CANDIDATE   -> ACTIVE | REFUTED | ARCHIVED
ACTIVE      -> DOMINANT | REFUTED | SUPERSEDED | ARCHIVED
DOMINANT    -> REFUTED | SUPERSEDED | ARCHIVED
REFUTED     -> ARCHIVED
SUPERSEDED  -> ARCHIVED
```

ARCHIVED é estado terminal. REFUTED e SUPERSEDED são terminais operacionais (só transitam para ARCHIVED).

### Princípio da Não Cascata [FONTE: CHM-001 §3.6, §4.8]

Mudanças de estado **não se propagam automaticamente** para hipóteses relacionadas. A refutação de uma hipótese pai não refuta automaticamente hipóteses filhas — elas tornam-se **elegíveis para revisão**, não transitam automaticamente.

---

## D6 — Protocolo de Publicação no Blackboard

### Workspace designado [FONTE: CONSTITUTION; RULE-BB-002]

Hipóteses são publicadas no workspace **Hypotheses** do Blackboard Cognitivo.

| Produtor | Tipo de hipótese | Workspace |
|---|---|---|
| Elliott Specialist | PRIMARY | Hypotheses |
| SMC Specialist | SUB | Hypotheses |
| Fibonacci Validator | SUB | Hypotheses |

### Sequência de publicação

1. **Criação:** Hypothesis Registry aloca `hypothesis_id` único.
2. **Validação:** Sistema verifica RULE-HH-001..004 (produtor autorizado, parent_id se SUB).
3. **Publicação:** Objeto é publicado no Blackboard em estado EMERGENT.
4. **Evento:** Cognitive Event "Hypothesis.Created" emitido no Event Bus (EC-COG-005).
5. **Versionamento:** `version = 1`, `previous_version_id = null`.

### Atualização de hipótese existente

Quando o produtor refina a hipótese (ex.: nova evidência, ajuste de confidence):

1. Nova versão é criada (`version = n+1`, `previous_version_id = versão anterior`).
2. Versão anterior **permanece** no Blackboard (append-only).
3. Evento "Hypothesis.Updated" emitido.

### Transição de estado

1. Agente ou sistema solicita transição.
2. Sistema valida contra Grafo Canônico (CHM-001 §4.3).
3. Se válida: `epistemic_state` atualizado, registro de transição adicionado.
4. Evento "Hypothesis.StateChanged" emitido.
5. Se inválida (ex.: regressão): operação rejeitada, erro retornado.

---

## D7 — Cenários de Teste

### Cenário-HH-T01 — Criação válida de PRIMARY por Elliott

```
DADO        Elliott Specialist identificou contagem Onda 3 iniciando em BTC/D1
            confidence = 0.78
            supporting_evidence_ids = [EV-101, EV-102]
QUANDO      Elliott invoca Hypothesis Registry para criar hipótese PRIMARY
ENTÃO       Sistema retorna:
              hypothesis_id = "HYP-2026-09-15-001"
              hypothesis_type = PRIMARY
              epistemic_state = EMERGENT
              version = 1
              parent_hypothesis_id = null
              confidence = 0.78
            Evento "Hypothesis.Created" publicado no Event Bus
VERIFICAÇÃO hypothesis_id != null
            epistemic_state == EMERGENT
            hypothesis_type == PRIMARY
            parent_hypothesis_id == null
```

### Cenário-HH-T02 — Criação válida de SUB por SMC

```
DADO        Hipótese PRIMARY HYP-A1 em estado ACTIVE
            SMC Specialist identificou BOS confirmando direção
            confidence = 0.65
QUANDO      SMC invoca criação de hipótese SUB com parent_id = HYP-A1
ENTÃO       Sistema retorna:
              hypothesis_type = SUB
              parent_hypothesis_id = "HYP-A1"
              epistemic_state = EMERGENT
VERIFICAÇÃO parent_hypothesis_id == "HYP-A1"
            hypothesis_type == SUB
```

### Cenário-HH-T03 — Bloqueio de ICT como produtor

```
DADO        ICT Specialist com setup de execução identificado
QUANDO      ICT tenta criar hipótese SUB
ENTÃO       Sistema retorna erro 403
            error_code = "ICT_NOT_HYPOTHESIS_PRODUCER"
            Nenhuma hipótese criada
VERIFICAÇÃO response.status == 403
            Blackboard.hypothesis_count não incrementou
```

### Cenário-HH-T04 — Rejeição de SUB sem parent_id

```
DADO        SMC Specialist tenta criar hipótese SUB sem informar parent_id
QUANDO      SMC invoca criação com parent_id = null
ENTÃO       Sistema retorna erro 400
            error_code = "SUB_REQUIRES_PARENT_ID"
VERIFICAÇÃO response.status == 400
            Nenhuma hipótese criada
```

### Cenário-HH-T05 — Transição válida EMERGENT -> CANDIDATE

```
DADO        Hipótese HYP-F10 em estado EMERGENT
            supporting_evidence_ids inicialmente vazio
QUANDO      Sistema adiciona Evidence EV-150 (ACTIVE) a HYP-F10
ENTÃO       HYP-F10.epistemic_state = CANDIDATE
            Registro de transição adicionado ao histórico
            Evento "Hypothesis.StateChanged" emitido
VERIFICAÇÃO HYP-F10.epistemic_state == CANDIDATE
            HYP-F10.transition_history.last().to_state == CANDIDATE
```

### Cenário-HH-T06 — Rejeição de regressão epistêmica

```
DADO        Hipótese HYP-G20 em estado ACTIVE
QUANDO      Agente tenta transicionar HYP-G20 para CANDIDATE
ENTÃO       Sistema rejeita operação
            error_code = "EPISTEMIC_REGRESSION_FORBIDDEN"
            HYP-G20.epistemic_state permanece ACTIVE
VERIFICAÇÃO response.error_code == "EPISTEMIC_REGRESSION_FORBIDDEN"
            HYP-G20.epistemic_state == ACTIVE
```

### Cenário-HH-T07 — Refutação preserva objeto (INV-07)

```
DADO        Hipótese HYP-H30 em estado DOMINANT
            Invalidador declarado: preço < 50000
QUANDO      Preço observado = 49500 (invalida hipótese)
ENTÃO       HYP-H30.epistemic_state = REFUTED
            HYP-H30 permanece no Blackboard (não deletada)
            Registro de refutação adicionado com motivo
VERIFICAÇÃO HYP-H30.epistemic_state == REFUTED
            Blackboard.contains("HYP-H30") == true
            HYP-H30.refutation_reason != null
```

---

## D8 — Cenários Adversariais [OBRIGATÓRIO para CRITICAL]

Componentes CRITICAL exigem cobertura adversarial explícita — "o que o sistema DEVE rejeitar"
(AGENTS.md §3; ATOMIC-SPEC.md; SKILL.md D8). Esta seção **formaliza** os casos de negação, alguns
já presentes de forma dispersa em D3/D7 (indicados como *consolida*), garantindo ≥2 cenários
adversariais conforme o método. Todo caso adversarial é uma **falha esperada**: a ausência da
rejeição constitui defeito de conformidade.

Princípio transversal: **fail-closed**. Em qualquer condição ambígua ou não satisfeita, o sistema
NÃO promove/NÃO cria/NÃO transiciona e retorna erro específico com log (EC-HH-001..004).

### Adversarial ADV-HH-01 — ICT como produtor de hipótese (consolida BASpec-HH-003 / T03)
**DADO:** ICT Specialist com suposta estrutura de execução identificada
**QUANDO:** ICT invoca createHypothesis(type=PRIMARY | SUB)
**ENTÃO:** sistema DEVE rejeitar com `403 ICT_NOT_HYPOTHESIS_PRODUCER`; nenhuma hipótese criada
**PORQUE:** ICT confirma/invalida execução, não cria hipótese (INV-02; RULE-HH-004; RULE-ICT-007)
**VERIFICAÇÃO:** response.error_code == "ICT_NOT_HYPOTHESIS_PRODUCER"; Blackboard.hypothesis_count inalterado

### Adversarial ADV-HH-02 — Produtor não-autorizado (Skill) cria hipótese
**DADO:** Uma Skill stateless tenta publicar objeto Hypothesis diretamente
**QUANDO:** produtor com producer_id ∉ AUTHORIZED_PRODUCERS invoca createHypothesis(...)
**ENTÃO:** sistema DEVE rejeitar com `403 PRODUCER_NOT_AUTHORIZED`; nenhuma hipótese criada
**PORQUE:** Skills produzem Observação, não Evidência nem hipótese (INV-06; RULE-HH-001)
**VERIFICAÇÃO:** response.error_code == "PRODUCER_NOT_AUTHORIZED"

### Adversarial ADV-HH-03 — SUB sem parent_id (Órfã de criação) (consolida T04)
**DADO:** SMC/Fibonacci tenta criar hipótese SUB sem informar parent_id
**QUANDO:** invoca createHypothesis(type=SUB, parent_id=null)
**ENTÃO:** sistema DEVE rejeitar com `400 SUB_REQUIRES_PARENT_ID`; nenhuma hipótese criada
**PORQUE:** SUB sem parent válido é Hipótese Órfã (CHM-001 §2.10.1; RULE-HH-003)
**VERIFICAÇÃO:** response.error_code == "SUB_REQUIRES_PARENT_ID"

### Adversarial ADV-HH-04 — Promoção de Hipótese Órfã a ACTIVE
**DADO:** Hipótese em CANDIDATE sem supporting_evidence_ids válidos (nenhuma Evidence ACTIVE)
**QUANDO:** sistema/agente tenta transicionar para ACTIVE ou DOMINANT
**ENTÃO:** sistema DEVE rejeitar (fail-closed) com `409 ORPHAN_CANNOT_ACTIVATE`; estado inalterado
**PORQUE:** Órfã não atinge ACTIVE/DOMINANT (CHM-001 §4.6 / ADR-CHM-001-008; RULE-HH-013; EC-HH-003)
**VERIFICAÇÃO:** response.error_code == "ORPHAN_CANNOT_ACTIVATE"; epistemic_state permanece CANDIDATE

### Adversarial ADV-HH-05 — SUB promovida com parent não-ACTIVE/DOMINANT
**DADO:** Hipótese SUB cujo parent_hypothesis está em REFUTED, SUPERSEDED ou ARCHIVED
**QUANDO:** sistema tenta transicionar a SUB para ACTIVE
**ENTÃO:** sistema DEVE rejeitar com `409 PARENT_NOT_ACTIVE`; SUB não promovida
**PORQUE:** SUB só sustenta decisão sob PRIMARY ativa (EC-HH-003 precond; herança fractal CHM-001 §1.8)
**VERIFICAÇÃO:** response.error_code == "PARENT_NOT_ACTIVE"

### Adversarial ADV-HH-06 — Regressão epistêmica (consolida BASpec-HH-007 / T06)
**DADO:** Hipótese em ACTIVE (ou DOMINANT)
**QUANDO:** agente invoca transitionState para estado anterior (ACTIVE→CANDIDATE, DOMINANT→ACTIVE, CANDIDATE→EMERGENT)
**ENTÃO:** sistema DEVE rejeitar com `409 EPISTEMIC_REGRESSION_FORBIDDEN`; estado inalterado
**PORQUE:** conhecimento é substituído/refutado/arquivado, não regride (CHM-001 §4.5; RULE-HH-012)
**VERIFICAÇÃO:** response.error_code == "EPISTEMIC_REGRESSION_FORBIDDEN"

### Adversarial ADV-HH-07 — Transição fora do Grafo Canônico
**DADO:** Hipótese em EMERGENT
**QUANDO:** agente tenta transição não prevista no grafo (ex.: EMERGENT→ACTIVE, pulando CANDIDATE)
**ENTÃO:** sistema DEVE rejeitar com `409 TRANSITION_NOT_IN_CANONICAL_GRAPH`; estado inalterado
**PORQUE:** apenas transições do Grafo Canônico são permitidas (CHM-001 §4.3; RULE-HH-012)
**VERIFICAÇÃO:** response.error_code == "TRANSITION_NOT_IN_CANONICAL_GRAPH"

### Adversarial ADV-HH-08 — Deleção/reescrita de hipótese ou versão (viola INV-07)
**DADO:** Hipótese em REFUTED (ou qualquer versão anterior na linhagem monotônica)
**QUANDO:** agente tenta deletar o objeto OU reescrever/reordenar versão anterior
**ENTÃO:** sistema DEVE rejeitar com `409 HYPOTHESIS_HISTORY_IMMUTABLE`; objeto e histórico preservados
**PORQUE:** REFUTED/SUPERSEDED/ARCHIVED ≠ DELETE; linhagem é append-only (CHM-001 §3.3, §3.4; INV-07; RULE-HH-020, RULE-HH-021)
**VERIFICAÇÃO:** response.error_code == "HYPOTHESIS_HISTORY_IMMUTABLE"; Blackboard.contains(objeto) == true

> **Cobertura:** 8 cenários adversariais formais (mínimo exigido para CRITICAL = ≥2).
> Todos mapeiam para os Enforcement Contracts EC-HH-001..004 (modo de falha fail-closed).

---

## Hypothesis Registry (Serviço Lógico)

### Responsabilidades [FONTE: ROADMAP §4; INFERÊNCIA]

O Hypothesis Registry é um serviço lógico (não um banco de dados) que gerencia:

| Função | Descrição |
|---|---|
| Alocação de ID | Gera `hypothesis_id` único e imutável |
| Versionamento | Mantém linhagem monotônica de versões (INV-07) |
| Índice de estado | Catálogo de hipóteses por `epistemic_state` |
| API de consulta | Busca por ID, por estado, por produtor, por parent |
| Reconstrução histórica | Suporta P13 (toda decisão reconstituível) |

### Contrato de ID [PROPOSTA]

```
hypothesis_id ::= "HYP-" + YYYY-MM-DD + "-" + SEQUENCE
Exemplo: HYP-2026-09-15-001
```

O formato exato é [PROPOSTA] — pode ser ajustado sem impacto normativo.

### Armazenamento físico

O Hypothesis Registry **não define onde** as hipóteses são armazenadas (Blackboard vs Knowledge Graph). Isso pertence a SPEC-004/006. O Registry é uma **interface lógica** sobre o repositório físico.

---

## Integração com Evidência (CEM-001)

### Referência por ID [FONTE: CHM-001 §2.10; CEM-001]

Hipóteses referenciam evidências por `Evidence ID` — nunca copiam o objeto Evidence.

```
supporting_evidence_ids: ["EV-001", "EV-002", "EV-003"]
refuting_evidence_ids: ["EV-010"]
```

### Fronteira Fonte -> Dado -> Evidência -> Hipótese [FONTE: CEM-001 Cap.1]

```
Fonte (ex.: TradingView) 
  -> Dado bruto (OHLC, Volume)
    -> Observação (Skill stateless produz)
      -> Evidência (Agent interpreta, CEM-001)
        -> Hipótese (CHM-001, esta SPEC)
```

Evidência é produzida por Agentes/Engines autorizados (CEM-001 Cap.2). Skills produzem **Observação**, não Evidência (INV-06).

### Impacto de invalidação de Evidência

Quando uma Evidência em `supporting_evidence_ids` transita para INVALIDATED:

1. Evento "Evidence.Invalidated" propagado via Event Bus.
2. Hipótese dependente torna-se **elegível para revisão**.
3. NÃO há cascata automática — produtor decide se refuta/mantém a hipótese.

[FONTE: CEM-001 Cap.4; CHM-001 §3.6 (Princípio da Não Cascata)]

---

## Slot de Convicção Operacional

### Referência ao CCM-001 [FONTE: CHM-001 §1.9]

A hipótese **referencia** o objeto de convicção (Conviction Global = CCM-001). Ela não calcula convicção.

```
conviction_reference: {
  conviction_object_id: "CV-001"  // referência ao CCM-001
  last_updated: "2026-09-15T10:30:00Z"
}
```

### Dimensionalidade [FATO NORMATIVO: decisão homologada]

O Conviction Vector possui **8 dimensões**: estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica.

### Fórmula/Pesos/Limiares [DECISÃO NECESSÁRIA: J-001 em aberto]

A fórmula de agregação, pesos por dimensão e limiares definitivos são **J-001 em aberto** — [DECISÃO NECESSÁRIA]. A SPEC-001 não fecha esses valores. SPEC-003 (CCM-001) é responsável por resolver J-001.

Os limiares de Fase Piloto (>=70% convicção global, score >=7/9) são FATO NORMATIVO interino, recalibrável após backtest (decisão homologada).

---

## Herança Fractal Operacional

### Propagação parent/child [FONTE: CHM-001 §1.8; decisão homologada]

Hipóteses SUB herdam contexto fractal da PRIMARY pai:

| Campo herdado | Descrição |
|---|---|
| Grau estrutural | Grau de onda do CHM-001 pai |
| Timeframe de referência | H4/D1/W1 da PRIMARY |
| Bias direcional | Bullish/Bearish da PRIMARY |
| Nível de invalidação | Herdado ou refinado |

### Regra de coerência

Hipótese SUB que contradiz a direção da PRIMARY pai deve ser marcada com `conflict_with_parent = true`. O Synthesis Agent considera esse conflito na decisão (RULE-005, RULE-SY-001).

---

## Auditabilidade (D9 por referência)

### Requisitos para P13 (toda decisão reconstituível) [FONTE: CONSTITUTION P13]

O Hypothesis Harness deve suportar:

| Requisito | Como o Harness atende |
|---|---|
| Estado do mercado no momento | Referência a snapshot de Market Context |
| Hipóteses ativas | Índice do Hypothesis Registry por estado |
| Evolução da convicção | Referência ao histórico do CCM-001 |
| Evidências que sustentaram | `supporting_evidence_ids` com timestamp |
| Módulos participantes | `producer_id` + `contributing_agents` |
| Versão das Skills | Metadata de versão no objeto |
| Parâmetros utilizados | `domain_payload` do CHM-001 |

### Histórico de transições [FONTE: CHM-001 §4.12]

Toda transição epistêmica gera registro com:

```
transition_record: {
  from_state: "CANDIDATE"
  to_state: "ACTIVE"
  timestamp: "2026-09-15T10:35:00Z"
  triggered_by: "evidence_threshold_reached"
  evidence: ["EV-105", "EV-106"]
}
```

---

## Enforcement Contracts

### EC-HH-001 — Criação de Hipótese

```
CAPABILITY   : Criar objeto Hypothesis no sistema
EFFECT       : Publicação no Blackboard (workspace Hypotheses)
PRECOND      : (producer_id in AUTHORIZED_PRODUCERS) AND
               (hypothesis_type == PRIMARY implies producer_id == "elliott_specialist") AND
               (hypothesis_type == SUB implies parent_id != null)
POSTCOND     : Hypothesis existe no Blackboard com epistemic_state = EMERGENT,
               hypothesis_id alocado, version = 1
POLICY       : RULE-HH-001, RULE-HH-002, RULE-HH-003, RULE-HH-004
LEVEL        : E2 (Operacional — estado compartilhado alterado)
FAILURE-MODE : Rejeitar criação; retornar erro específico; nenhuma hipótese publicada
EVIDENCE     : Log de criação com producer_id, hypothesis_id, timestamp
```

### EC-HH-002 — Transição de Estado Epistêmico

```
CAPABILITY   : Transicionar epistemic_state de hipótese existente
EFFECT       : Alteração de estado em objeto compartilhado; evento no Event Bus
PRECOND      : (transição in GRAFO_CANONICO_CHM001) AND
               (não é regressão epistêmica) AND
               (se destino == ACTIVE|DOMINANT, hipótese não é Órfã)
POSTCOND     : epistemic_state atualizado; transition_record adicionado;
               evento "Hypothesis.StateChanged" emitido
POLICY       : CHM-001 §4.3; RULE-HH-010, RULE-HH-011, RULE-HH-012
LEVEL        : E2 (Operacional)
FAILURE-MODE : Rejeitar transição; retornar erro específico; estado inalterado
EVIDENCE     : transition_record com from_state, to_state, timestamp, justificativa
```

### EC-HH-003 — Transição para ACTIVE/DOMINANT (decisão)

```
CAPABILITY   : Promover hipótese a estado elegível para decisão
EFFECT       : Hipótese torna-se base válida para sinal operacional
PRECOND      : (supporting_evidence_ids.length >= 1) AND
               (todos os evidence_ids apontam para Evidence ACTIVE) AND
               (não é Hipótese Órfã) AND
               (se SUB, parent em ACTIVE|DOMINANT)
POSTCOND     : Hipótese em ACTIVE ou DOMINANT; elegível para Synthesis
POLICY       : CHM-001 §4.6; RULE-HH-011; Salvaguardas CEE-001 §11
LEVEL        : E3 (Crítico — base de decisão de trading)
FAILURE-MODE : Fail-closed: não promover; hipótese permanece no estado anterior;
               log de rejeição com motivo
EVIDENCE     : Registro de promoção; lista de evidências que sustentaram;
               audit trail para reconstrução (P13)
```

### EC-HH-004 — Refutação de Hipótese

```
CAPABILITY   : Transicionar hipótese para REFUTED
EFFECT       : Hipótese deixa de ser elegível para decisão; permanece para auditoria
PRECOND      : (critério de refutação explícito observado) AND
               (hipótese em CANDIDATE|ACTIVE|DOMINANT)
POSTCOND     : epistemic_state = REFUTED; objeto preservado (INV-07);
               refutation_reason registrado
POLICY       : CHM-001 §3.4; RULE-HH-021; INV-07
LEVEL        : E2 (Operacional)
FAILURE-MODE : Se critério não explícito, rejeitar e solicitar justificativa
EVIDENCE     : refutation_record com motivo, timestamp, evidence_ids que causaram
```

---

## Decisões Incidentes

### Decisões fechadas (homologadas por Andraus)

| Decisão | Conteúdo | Status |
|---|---|---|
| Hipótese PRIMARY/SUB | Elliott cria PRIMARY; SMC/Fibonacci criam SUB; ICT não cria | FATO NORMATIVO |
| Estados canônicos | 7 estados do CHM-001 (RULE-BB-003 superseded) | FATO NORMATIVO |
| Dimensionalidade | 8 dimensões do Conviction Vector | FATO NORMATIVO |
| Limiares Fase Piloto | >=70% convicção, >=7/9 score (recalibráveis) | FATO NORMATIVO interino |
| Topologia | Fusion -> Conviction -> Synthesis (separados) | FATO NORMATIVO |

### Decisões abertas — [DECISÃO NECESSÁRIA]

| ID | Descrição | Status | Impacto nesta Spec |
|---|---|---|---|
| **J-001** | Fórmula/pesos/limiares definitivos do Conviction Vector | EM ABERTO — pendente | Slot de convicção referencia CCM-001; não fecha valores |
| **M-001** | Estados do Blackboard para objetos não-hipótese | EM ABERTO — pendente | SPEC-001 cobre apenas hipóteses; pertence a SPEC-004 |
| **N-001** | Pesos por ativo do Conviction Vector | EM ABERTO — pendente | Parte de J-001; não se aplica a SPEC-001 |
| **MEN-01** | EC-HH-003 (E3) não declara método explícito de observação de falso-DENY (ENF-07) | EM ABERTO — pendente | Gap aceito (ATOMIC-SPEC.md §ENF-07 = gap aberto). Não bloqueia SPEC-001 v1.1 (homologada). Encaminhado à **SPEC-003 (CCM-001)**; vinculado a **J-001** (ponderação por dimensão de convicção define o limiar de predominância que torna o falso-DENY observável). [FONTE: Parecer Revisor 2026-09-15, MEN-01; homologação Andraus 2026-09-15] |

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CHM-001 (estados, taxonomia, estrutura) | [FONTE] | FATO NORMATIVO (BASELINED) |
| CEM-001 (contrato de Evidência) | [FONTE] | FATO NORMATIVO (BASELINED) |
| EC-COG-004 (Blackboard Cognitivo — infra do Kernel) | [FONTE] | FATO NORMATIVO (Kernel / CONSTITUTION) |
| EC-COG-005 (Cognitive Event Bus — infra do Kernel) | [FONTE] | FATO NORMATIVO (Kernel / CONSTITUTION); contrato operacional pertence à SPEC-005 |
| Decisão hipótese PRIMARY/SUB | [FONTE] | FATO NORMATIVO (homologado Andraus) |
| Decisão estados canônicos | [FONTE] | FATO NORMATIVO (homologado Andraus) |
| Decisão 8 dimensões | [FONTE] | FATO NORMATIVO (homologado Andraus) |
| Decisão limiares Fase Piloto | [FONTE] | FATO NORMATIVO interino |
| Hypothesis Registry (serviço lógico) | [INFERÊNCIA] | FATO ARQUITETURAL |
| Formato de hypothesis_id | [PROPOSTA] | Requer confirmação |
| J-001 (fórmula/pesos/limiares) — em aberto | [DECISÃO NECESSÁRIA] | EM ABERTO — pendente — não fechar |
| M-001 (estados Blackboard não-hipótese) — em aberto | [DECISÃO NECESSÁRIA] | EM ABERTO — pendente |
| N-001 (pesos por ativo) — em aberto | [DECISÃO NECESSÁRIA] | EM ABERTO — pendente |

---

## Apêndice A — Schemas I/O (referência)

### Objeto Hypothesis (CHM-001 + extensão operacional)

```json
{
  "hypothesis_id": "HYP-2026-09-15-001",
  "version": 1,
  "previous_version_id": null,
  "hypothesis_type": "PRIMARY | SUB",
  "generation_mechanism": "OBSERVATIONAL | INFERENTIAL | SIMULATED | COMPOSITE",
  "epistemic_state": "EMERGENT | CANDIDATE | ACTIVE | DOMINANT | SUPERSEDED | REFUTED | ARCHIVED",
  "confidence": 0.78,
  "producer_type": "AGENT",
  "producer_id": "elliott_specialist",
  "created_at": "2026-09-15T10:30:00Z",
  "parent_hypothesis_id": null,
  "child_hypothesis_ids": [],
  "sibling_hypothesis_ids": [],
  "generation": 0,
  "supporting_evidence_ids": ["EV-101", "EV-102"],
  "refuting_evidence_ids": [],
  "depends_on_hypothesis_ids": [],
  "competing_hypothesis_ids": [],
  "conviction_reference": {
    "conviction_object_id": "CONV-001",
    "last_updated": "2026-09-15T10:35:00Z"
  },
  "domain_payload": {},
  "transition_history": []
}
```

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] que permanece em aberto nesta Spec:
- **J-001** — Fórmula/pesos/limiares definitivos do Conviction Vector (em aberto — pendente; impacta slot de convicção; CCM-001 pendente de redação)
- **M-001** — Estados do Blackboard para objetos não-hipótese (em aberto — pendente; pertence a SPEC-004)
- **N-001** — Pesos por ativo do Conviction Vector (em aberto — pendente; parte de J-001)
