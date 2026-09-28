# SOT-RISK-MASTER-001 — Master Document: Risk Agent SOT

| Campo | Valor |
|---|---|
| **Identificador** | SOT-RISK-MASTER-001 |
| **Versão** | 1.0-consolidado |
| **Data** | 2026-09-22 |
| **Origem** | Sessão de design Andraus × Claude (claude.ai) |
| **Status** | `[PROPOSTA]` — não-normativo até homologação via EUA-E19 + Família RISK-SPEC |
| **Destino** | `reference/` (padrão MC-*); entrada via **BL-018** no RMR-001 (BL-017 já ocupado — dimensões B da SPEC-020; renumerado por decisão de Andraus 2026-09-22, C-01) |
| **Natureza** | Master Specification / Specification-of-Specifications |
| **Componente** | Risk Agent — elo final de análise para execução |
| **Criticidade proposta** | CRITICAL |
| **Profundidade proposta** | D0–D9 |
| **Método** | Atomic Specification v1.4 (vigente) |
| **Governança** | SOT Constitution + RULES + ROADMAP + atomic-spec |

> **TRACE-06:** Todo conteúdo deste documento é `[PROPOSTA]` ou `[FATO ARQUITETURAL — decisão de Andraus, 2026-09-22]` conforme indicado. Nenhuma seção é normativa até homologação formal. O repo SOT-Harness é a autoridade real; este documento entra como referência externa candidata pelo mesmo padrão dos MC-*.

---

## Parte I — Decisões Arquiteturais de Andraus (2026-09-22)

`[FATO ARQUITETURAL — decisão de Andraus, 2026-09-22 — aguarda formalização via EUA-E19]`

### D-RISK-01 — Risk Agent absorve o ARR

O Risk Agent **consolida** as RULES de risco-retorno já vigentes e **institui** invariantes de risco novos. Enquanto **RISK-ARR-LOC-001** (localização do D-ARR-001) permanecer aberta, **não há linguagem de supersedação do ARR** — o "ARR" não existe como componente formal no repo (achado F-01, parecer Claude Code 2026-09-22).

- R:R ≥ 1:3 (risco:retorno = 3:1 retorno:risco) — **consolida** RULE-006 / RULE-ICT-002 / CEE-001 §11 Salvaguarda 5 como invariante mínimo do Risk Agent (as RULES continuam vigentes; o Risk Agent as herda e não as duplica). Convenção idêntica à do repo (Q-004).
- Risco por operação dinâmico, sensível à oportunidade, inclui sugestão de alavancagem — **invariante NOVO instituído aqui** (não existe no repo atual).
- Portfolio Heat máximo ≤ 15% — **invariante NOVO instituído aqui** (não existe no repo atual).

Reenquadramento (C-09, Andraus 2026-09-22): a decisão D-RISK-01 **consolida** RULES vigentes + **institui** dois invariantes novos. **Zero supersedação** até RISK-ARR-LOC-001 ser resolvida.

### D-RISK-02 — Pipeline atualizado

```
ANTES (homologado):
Elliott → ... → Synthesis → TMP → Bot Finance

DEPOIS (proposto):
Elliott → ... → Synthesis → [TMP interno] → Risk Agent → Risk Harness → Signal Package → Bot Finance
```

O TMP passa a ser artefato interno de passagem entre Síntese e Risk Agent. Não atravessa mais a fronteira SOT → exterior.

### D-RISK-03 — Signal Package é a nova fronteira

O Signal Package é o único artefato que atravessa a fronteira SOT → Bot Finance.

**Base fundacional:** "Signal Package" é o termo original da ENGENHARIA-GERAL (Doc03 §20, l.604–606): *"O SOT nunca executará ordens diretamente. Após atingir convicção suficiente, produzirá um Signal Package padronizado para integração com o seu Bot Trade Finance."* O TMP foi introduzido posteriormente. D-RISK-03 restaura o termo fundacional — não inova.

Características definidas:
- Contém **exclusivamente** o que o Bot Finance precisa para iniciar seu runtime
- **NÃO contém** análise, hipóteses, raciocínio cognitivo, ou RDR
- Serve a **dois receptores**: Bot Finance (runtime de logística financeira) + humano/Andraus (runtime de execução do trade)
- Contrato exato (campos, schema) = `[DECISÃO NECESSÁRIA — D-RISK-SP-001]` — diferida à RISK-SPEC-022 (spec de acoplamento)

### D-RISK-04 — Papéis downstream

- **Bot Finance:** logística financeira de transferência de fundos para a corretora
- **Trading em si:** executado pelo humano (Andraus) com base no Signal Package
- O Signal Package deve ser especificado para ambos os receptores simultaneamente

### D-RISK-05 — INV-05 atualizada

- **De:** "SOT não executa ordem, produz TMP" (CONSTITUTION P14, atomic-spec INV-05, GLOSSARIO, AGENTS #9, CHUNK-SY-007, ROADMAP SPEC-016)
- **Para:** "SOT não executa ordem, produz Signal Package via Risk Harness"
- TMP permanece como artefato interno entre Síntese e Risk Agent

> **Impacto constitucional:** P14 da CONSTITUTION requer emenda formal (GES-1). Os 6 loci onde este invariante reside devem convergir horizontalmente (MAN-001). Lista dos loci: CONSTITUTION P14 + diagrama · atomic-spec INV-05 · GLOSSARIO l.52 · CHUNK-SY-007 · AGENTS #9 · ROADMAP SPEC-016.

> **Faseamento EUA-E19a (C-03, Andraus 2026-09-22):** a emenda é **fatiada**. A **EUA-E19a** (primeira e imediata) restaura **"Signal Package" como fronteira** + **TMP interno** + registro RULE-SEM da terminologia concorrente, **SEM mencionar o Risk Harness** (que só existe a partir de RISK-SPEC-020). A cláusula **"via Risk Harness"** entra em P14/INV-05 **somente quando RISK-SPEC-020 for homologada** — evita invariante constitucional apontando para componente inexistente (CONS-01).

---

## Parte II — Identidade e Missão do Risk Agent

`[PROPOSTA]`

### 2.1 O que é

O Risk Agent é o agente cognitivo especializado do SOT responsável por:

1. Receber os resultados da cadeia analítica (TMP interno produzido pela Síntese)
2. Realizar avaliação independente e especializada do risco
3. Confrontar as hipóteses recebidas com challenge independente
4. Ponderar risco e retorno segundo princípios de decisão próprios
5. Determinar se a oportunidade é admissível para geração de Signal Package
6. Autorizar e emitir o Signal Package via Risk Harness quando todas as condições forem satisfeitas

### 2.2 O que não é

- Mero calculador de R:R
- Filtro mecânico de sinais
- Extensão ou subordinado da Síntese
- Gerador automático de ordens
- Executor financeiro

### 2.3 Missão (D0)

> **Determinar, de forma independente, fundamentada, probabilística, causal, contrafactual, quantitativa e metacognitiva, se a exposição a uma oportunidade de mercado é justificável diante das evidências, incertezas, consequências, retorno potencial, contexto e princípios de decisão de risco do SOT — e, quando admissível, autorizar o Signal Package via Risk Harness.**

### 2.4 Posição no pipeline

```
ANÁLISE (Elliott → Fibonacci → Fractal → SMC → ICT)
        ↓
BLACKBOARD → FUSION ENGINE → CONVICTION ENGINE
        ↓
SYNTHESIS AGENT → TMP [artefato interno]
        ↓
┌─────────────────────────────────────────┐
│              RISK AGENT                 │
│  (14 camadas — ver Parte III)           │
└──────────────────┬──────────────────────┘
                   ↓
           RISK DECISION RECORD (RDR)
                   ↓
              DECISÃO
         ACCEPT / WAIT / REJECT / ABSTAIN
                   ↓ (somente ACCEPT)
             RISK HARNESS (gate E3)
                   ↓
            SIGNAL PACKAGE ←─── fronteira SOT → exterior
                   ↓
              BOT FINANCE (logística)
              HUMANO / ANDRAUS (execução do trade)
```

---

## Parte III — Arquitetura Cognitiva

`[PROPOSTA]`

### 3.1 Princípio fundamental

O Risk Agent possui **simetria estrutural com os demais agentes cognitivos do SOT**. A especialização ocorre no conteúdo e na aplicação das camadas, não pela remoção delas.

> **Confluência com N8–N17 (achado F-03, Claude Code 2026-09-22; contagem unificada pela tabela §3.2 — C-07, Andraus 2026-09-22):** **11 das 14 camadas** (as de #2 a #12) mapeiam sobre as camadas cognitivas N8–N17 já homologadas (EUA-E05..E14) e são **herdadas** via RULE-HV-01..04. O **delta genuíno** do Risk Agent são **3 camadas**: **#1 Principiológica** (princípios de risco RP1–RP15), **#13 Quantitativa** (VaR/CVaR/drawdown) e **#14 Risco–Retorno**.

### 3.2 As 14 camadas

| # | Camada | Natureza | Relação com repo atual |
|---|---|---|---|
| 1 | Principiológica | Filosofia de risco (RP1–RP15) | Delta genuíno: princípios de risco específicos |
| 2 | Epistemológica | O que o agente sabe / como sabe | Herda N8 (RULE-EPI, MEG-001) |
| 3 | Inquérito | Busca ativa de riscos não declarados | Herda N11 (RULE-INQ, MIQG-001) |
| 4 | Ontológica | Universo de entidades de risco | Herda N10 (RULE-ONT, MOC-001) |
| 5 | Semântica | Distinções operacionais (risco ≠ retorno ≠ probabilidade) | Herda N9 (RULE-SEM, MSC-001) |
| 6 | Causal | Mecanismos causais, não correlações | Herda N12 (RULE-CAU, MCC-001) |
| 7 | Contrafactual | Cenários alternativos C1–C7 | Herda N13 (RULE-CTF, MCF-001) |
| 8 | Incerteza | Aleatoriedade / epistêmica / modelo / regime | Herda N14 (RULE-UNC, MUN-001) |
| 9 | Probabilística | Distribuições, caudas, calibração | Herda N15 (RULE-PRB, MPB-001) |
| 10 | Decisional | ACCEPT / WAIT / REJECT / ABSTAIN | Herda N16 (RULE-DEC, MDC-001) |
| 11 | Memória | Decisão / resultado / modelo / risco (4 categorias) | Herda N17 parcialmente (RULE-MET) |
| 12 | Metacognitiva | Avalia a própria avaliação | Herda N17 (RULE-MET, MC-001) |
| 13 | **Quantitativa** | VaR, CVaR, drawdown, correlação, Monte Carlo | **DELTA genuíno — novo** |
| 14 | **Risco–Retorno** | Distribuição de perdas + retorno + incerteza + exposição + cauda | **DELTA genuíno — novo** |

### 3.3 Objetos intermediários

**Risk Decision Record (RDR)** — objeto cognitivo intermediário, interno ao Risk Agent:
- O que o agente sabia, o que consultou, o que calculou, o que inferiu
- Quais riscos identificou, qual decisão tomou, por que tomou
- Permanece interno — NÃO vai para o Bot Finance
- `[DECISÃO NECESSÁRIA: depende de CDM-001, ainda não redigido]`

**Signal Package** — contrato operacional mínimo de saída:
- Referencia o RDR (por ID, não por cópia)
- Contém apenas o que o Bot Finance + humano precisam para operar
- Campos exatos = `[DECISÃO NECESSÁRIA — D-RISK-SP-001]`

### 3.4 Princípios de risco (RP1–RP15)

> **Namespace (C-05, Andraus 2026-09-22):** prefixo **RP** para não colidir com os princípios da CONSTITUTION (P-numeração; ex.: P13, P14). "RP14 Challenge" ≠ "P14 execução" constitucional.

RP1 Preservação · RP2 Proporcionalidade · RP3 Assimetria · RP4 Evidência · RP5 Incerteza · RP6 Não-confundibilidade · RP7 Não-compensação-indevida · RP8 Cauda · RP9 Contexto · RP10 Agregação · RP11 Reversibilidade · RP12 Transparência · RP13 Abstinência · RP14 Challenge · RP15 Integridade

### 3.5 Saídas decisionais

| Estado | Condição |
|---|---|
| **ACCEPT** | Evidência suficiente · risco compreendido · incerteza aceitável · R:R admissível · princípios satisfeitos · invariantes satisfeitas · pacote consistente |
| **WAIT** | Hipótese plausível mas existe condição relevante não resolvida |
| **REJECT** | Risco incompatível · evidência insuficiente · contradição material · exposição inadequada · princípio ou invariante violada |
| **ABSTAIN** | Avaliação não atingiu confiabilidade suficiente — comportamento desejável, não falha |

### 3.6 Invariantes propostos (INV-RISK-00..12)

> **Confluência com achado F-04 (Claude Code):** vários INV-RISK mapeiam sobre invariantes/RULES existentes. A especificação deve declarar herança, não duplicação.

**INV-RISK-00 — Isolamento epistêmico (PRÉ-CONDIÇÃO de todas as demais RULE-RISK-*)** `[FATO ARQUITETURAL — decisão de Andraus, 2026-09-22]`

> O Risk Agent opera em **workspace isolado** do Blackboard analítico. Seu único input autorizado é o **TMP recebido por handoff formal com contrato tipado** — um snapshot **imutável, versionado, com timestamp**, sem possibilidade de alteração retroativa após a entrega. O Risk Agent **nunca lê o Blackboard diretamente, nunca escreve de volta nele**, e sua saída (Signal Package) **não alimenta o pipeline analítico**.
>
> **Fundamento epistêmico:** o challenge do Risk Agent só é genuinamente independente se ele não tiver acesso ao processo que gerou a conclusão que está questionando. Um Risk Agent que leu o mesmo Blackboard que a Síntese *confirma* — não *desafia*. [FONTE: pesquisa de estado da arte AgenticAITA 2026 — isolamento de contexto → taxa de rejeição não-trivial (~3,2%) como evidência de challenge genuíno] `[EXTERNO — referência de benchmark, não-normativa]`
>
> **Interação com RULE-BB-001/002:** INV-RISK-00 é compatível e mais restritivo — o Risk Agent não é um agente-analista comum no barramento Blackboard; o handoff tipado é a única ponte. **Registrado também em:** RISK-SPEC-020 (Risk Harness — pré-condição), RISK-SPEC-022 (Signal Package — contrato de saída), SPEC-016 repurposada (TMP como snapshot imutável de entrada).

| ID | Invariante | Relação com repo |
|---|---|---|
| **INV-RISK-00** | **Isolamento epistêmico: workspace isolado; input só via handoff tipado imutável do TMP; sem leitura/escrita no Blackboard; saída não realimenta o pipeline** | **Delta genuíno — pré-condição (Andraus 2026-09-22)** |
| INV-RISK-01 | Não autorizar exposição sem avaliação de risco | Delta |
| INV-RISK-02 | Não confundir convicção analítica com convicção de risco | `[DECISÃO NECESSÁRIA: RISK-CONV-001]` |
| INV-RISK-03 | Não tratar ausência de evidência como evidência positiva | Herda RULE-EPI-01 |
| INV-RISK-04 | Não ocultar contraevidência material | Herda PCO-02 |
| INV-RISK-05 | Não emitir decisão sem avaliação de incerteza material | Delta |
| INV-RISK-06 | Não usar cálculo textual quando ferramenta determinística disponível | Herda ENF + SPEC-038 |
| INV-RISK-07 | Não alterar políticas normativas durante a decisão | Herda RULE-HG-02 + RULE-DEC |
| INV-RISK-08 | Não emitir Signal Package sem Risk Harness aprovado | Delta — gate E3 |
| INV-RISK-09 | Bot Finance não reinterpreta a decisão de risco | Delta |
| INV-RISK-10 | Toda decisão deve possuir provenance | Herda CEM-001 / P13 |
| INV-RISK-11 | Toda decisão crítica deve ser reconstruível | Herda P13 / D9 |
| INV-RISK-12 | O agente deve poder ABSTAIN | Herda INDETERMINADO/HOLD (EUA-E05) |

---

## Parte IV — Risk Harness

`[PROPOSTA]`

O Risk Harness é o gate E3 do Risk Agent. Não substitui o raciocínio — verifica se o raciocínio satisfaz as condições mínimas para produzir ação operacional.

**Funções:** validar entradas · verificar invariantes · verificar cálculos · verificar consistência do Signal Package · verificar limites de exposição · detectar ausência de campos críticos · bloquear inconsistências materiais · registrar decisão com provenance.

**Princípio:** fail-closed. Sem validação do Harness, sem Signal Package. O LLM não é seu próprio gate (ENF-03 vigente).

---

## Parte V — Benchmarks e Avaliação

`[PROPOSTA]`

> **Confluência com SPEC-020 (C-08, Andraus 2026-09-22):** a camada de avaliação do Risk Agent **NÃO cria taxonomia paralela**. A **RISK-SPEC-023 herda a SPEC-020 (Harness Evaluation, núcleo A) via RULE-HV-01..04** — correctness/grounding/hallucination/role-adherence/context/safety/regression/robustness-adversarial vêm da SPEC-020 como critérios constitutivos. As dimensões D1–D15 abaixo são o **delta de risco** sobre esse núcleo (não um substituto). O Grupo H passa de 2 specs para **1** (023+024 fundidas) → família reduz de 24 para **23 specs**.

### 5.1 Risk Agent Evaluation Stack (4 níveis)

- **B0 — Skill:** a ferramenta produz a Observação correta?
- **B1 — Capability:** o agente possui a capacidade cognitiva?
- **B2 — Agent:** o Risk Agent integra capacidades e decide corretamente?
- **B3 — System:** o Risk Agent permanece seguro e eficaz conectado ao SOT e ao downstream?

### 5.2 Referências externas (não-normativas)

FinBen · InvestorBench · RISCTrade · SAEA · Federal Reserve Model Risk Management · Basel Stress Testing

Tratadas como fontes de requisitos e inspiração para validação — não substituem a especificação própria do SOT.

### 5.3 Dimensões de avaliação próprias do SOT (D1–D15)

D1 Risk Identification · D2 Risk Classification · D3 Quantitative Correctness · D4 Evidence Grounding · D5 Uncertainty Calibration · D6 Counterfactual Robustness · D7 Causal Coherence · D8 Risk–Return Reasoning · D9 Decision Consistency · D10 Mandate Compliance · D11 Stress Robustness · D12 Abstention Quality · D13 Metacognition · D14 Memory Quality · D15 Operational Integrity

---

## Parte VI — Decomposição em Família de Specs (RISK-SPEC)

`[PROPOSTA — aguarda autorização via EUA-E19a (restauração semântica) → EUA-E20 (FASE RISK)]`

### 6.1 Justificativa para família própria

O Risk Agent é o elo final de análise para execução. Sua posição no pipeline é única: recebe toda a cognição analítica e decide se ela se transforma em exposição real de capital. Essa responsabilidade justifica família própria de Specs, pela mesma razão que a Hypothesis Harness (SPEC-001), Evidence Harness (SPEC-002) e Conviction (SPEC-003) são Specs independentes apesar de integrarem o mesmo pipeline.

Uma família própria garante:
- Cada dimensão cognitiva tem sua spec, seus BASpecs, seu enforcement e seus testes independentes
- O Risk Harness (gate E3) tem spec própria com garantias formais separadas do raciocínio
- A spec de acoplamento (Signal Package) pode evoluir independentemente sem reabrir as specs cognitivas
- A profundidade D0–D9 é aplicada adequadamente por spec, não comprimida em uma única entrega

### 6.2 Estrutura da Família RISK-SPEC

```
SOT-RISK-MASTER-001 (este documento — referência externa, reference/; entrada via BL-018)
│
├── EUA-E19a (restauração semântica — precede todas as specs; SEM Risk Harness — C-03)
│      └── cláusula "via Risk Harness" em P14/INV-05 entra só com RISK-SPEC-020 homologada
│
├── FASE RISK (posição: após FASE 6 — Synthesis)
│
│   GRUPO A — Fundamento (4 Specs)
│   ├── RISK-SPEC-001  Princípios de Risco (D0–D3)
│   ├── RISK-SPEC-002  Epistemologia de Risco (herda N8; delta: limites de conhecimento de risco)
│   ├── RISK-SPEC-003  Ontologia de Risco (herda N10; delta: entidades capital/exposição/posição)
│   └── RISK-SPEC-004  Semântica de Risco (herda N9; delta: risco≠retorno≠probabilidade≠confiança)
│
│   GRUPO B — Cognição (5 Specs)
│   ├── RISK-SPEC-005  Inquérito de Risco (herda N11; delta: riscos não declarados)
│   ├── RISK-SPEC-006  Causalidade de Risco (herda N12; delta: mecanismo→consequência)
│   ├── RISK-SPEC-007  Contrafactuais de Risco (herda N13; C1–C7 específicos)
│   ├── RISK-SPEC-008  Incerteza de Risco (herda N14; delta: incerteza de modelo/regime)
│   └── RISK-SPEC-009  Probabilística de Risco (herda N15; delta: caudas, calibração, Monte Carlo)
│
│   GRUPO C — Decisão (4 Specs)
│   ├── RISK-SPEC-010  Decisão sob Risco (herda N16; delta: ACCEPT/WAIT/REJECT/ABSTAIN)
│   ├── RISK-SPEC-011  Risco–Retorno (DELTA genuíno — novo; consolida R:R≥1:3 (risco:retorno=3:1 retorno:risco) + institui Heat≤15%)
│   ├── RISK-SPEC-012  Exposição e Capital (DELTA genuíno — sizing, alavancagem, concentração)
│   └── RISK-SPEC-013  Risco de Modelo (DELTA genuíno — risco das próprias hipóteses/modelos)
│
│   GRUPO D — Quantificação (3 Specs)
│   ├── RISK-SPEC-014  Toolbox Quantitativo (VaR, CVaR, drawdown, correlação — DELTA genuíno)
│   ├── RISK-SPEC-015  Stress e Simulação (cenários adversos, Monte Carlo, bootstrap)
│   └── RISK-SPEC-016  Calibração (Brier score, log-loss, intervalos de confiança)
│
│   GRUPO E — Memória e Metacognição (3 Specs)
│   ├── RISK-SPEC-017  Memória de Risco (decisão/resultado/modelo/risco — 4 categorias)
│   ├── RISK-SPEC-018  Aprendizado de Risco (qualidade da decisão ≠ resultado realizado)
│   └── RISK-SPEC-019  Metacognição de Risco (herda N17; delta: avalia a própria avaliação de risco)
│
│   GRUPO F — Operacionalização (3 Specs)
│   ├── RISK-SPEC-020  Risk Harness (gate E3 — enforcement crítico)
│   ├── RISK-SPEC-021  Risk Decision Record (RDR — objeto cognitivo intermediário; depende CDM-001)
│   └── RISK-SPEC-022  Signal Package (spec de acoplamento — contrato em aberto D-RISK-SP-001)
│
│   GRUPO G — Skills (diferido)
│   └── RISK-SPEC-SKL-* (diferido a I-001 — mesmo padrão das demais Skills do ROADMAP)
│
│   GRUPO H — Avaliação (1 Spec — fundidas 023+024 por C-08)
│   └── RISK-SPEC-023  Avaliação de Risco & Adversarial — HERDA SPEC-020 (núcleo A) via RULE-HV;
│                      delta: Stack B0–B3 + D1–D15 de risco + adversarial de risco
│                      (hallucination, temporal misalignment, prompt injection)
│
└── Total proposto: 23 Specs + Skills diferidas  (era 24; Grupo H fundido — C-08, Andraus 2026-09-22)
```

### 6.3 Regra de herança

As Specs dos Grupos A e B que herdam N8–N17 devem:
1. Declarar herança explícita via RULE-HV-01..04 (herança vertical, homologada)
2. Especificar apenas o **delta** de risco — não recriar o que N8–N17 já cobrem
3. Referenciar a Spec-pai por ID+versão (RULE-HD-04)

### 6.4 Ordem de especificação

**EUA-E19a (restauração semântica) → ** Fase A (Fundamento) → Fase B (Cognição) → Fase C (Decisão) → Fase D (Quantificação) → Fase E (Memória) → Fase F (Operacionalização) → Fase G (Skills) → Fase H (Avaliação, herda SPEC-020)

**Nota INV-RISK-00:** RISK-SPEC-020 (Risk Harness) e SPEC-016 repurposada devem ancorar o isolamento epistêmico como pré-condição. RISK-SPEC-020 verifica INV-RISK-00 antes de qualquer autorização de Signal Package.

RISK-SPEC-020 (Risk Harness) é pré-requisito de RISK-SPEC-021 e RISK-SPEC-022.
RISK-SPEC-021 depende de CDM-001 — `[DECISÃO NECESSÁRIA: pode ser especificado com contrato provisório?]`

---

## Parte VII — Decisões Abertas Registradas

`[CONS-01 — nenhuma das seguintes pode ser declarada fechada sem Andraus]`

| ID | Decisão | Trava |
|---|---|---|
| D-RISK-SP-001 | Contrato exato do Signal Package (campos, schema) | RISK-SPEC-022 |
| RISK-ARR-LOC-001 | D-ARR-001 não existe no repo — a absorção consolida RULES + adiciona novos invariantes; não há supersedação de ata | EUA-E19 (esclarece escopo) |
| RISK-CONV-001 | "Convicção de Risco" (INV-RISK-02) cria 2ª noção de convicção; relação com Conviction Vector 8D e J-001 precisa ser resolvida | RISK-SPEC-010; não fechar sem J-001 |
| CDM-001 | Canonical Decision Model — o RDR é objeto de decisão; sem CDM-001 o idioma canônico não existe | RISK-SPEC-021 |
| I-001 | Skills como unidades formais separadas | RISK-SPEC-SKL-* |
| J-001 | Fórmula/pesos/limiares definitivos do Conviction Vector | RISK-SPEC-009, RISK-SPEC-010 |

---

## Parte VIII — Decisões que este Master NÃO fecha

1. Limites quantitativos de exposição além do Portfolio Heat ≤ 15%
2. Modelo definitivo de sizing por ativo
3. Thresholds definitivos de decisão (além de R:R ≥ 1:3 risco:retorno = 3:1 retorno:risco)
4. Política de risco por ativo (BTC vs XAU vs NASDAQ)
5. Integração formal com Conviction Engine (além da leitura do TMP)
6. Persistência física da memória do Risk Agent
7. Ferramentas quantitativas definitivas e suas implementações
8. Política de atualização das Skills de risco
9. Modelo definitivo de Risk Score (se vier a existir)
10. Estados definitivos do Blackboard para objetos de risco (ligado a M-001)
11. Política de kill-switch do Risk Agent
12. Política de fail-closed além do Risk Harness
13. Orçamento de latência
14. Catálogo definitivo de proxies determinísticos

---

## Parte IX — Checklist de Pré-requisitos para EUA-E19a

`[PROPOSTA — para verificação pelo Especificador antes de redigir a EUA-E19a]`

Antes de redigir a EUA-E19a, o Especificador deve verificar:

- [x] 6 loci do invariante "SOT não executa; artefato de fronteira" mapeados e confirmados (parecer Claude Code 2026-09-22): CONSTITUTION P14 + diagrama · atomic-spec INV-05 §13 · GLOSSARIO l.52 · CHUNK-SY-007 · AGENTS #9 · ROADMAP SPEC-016
- [ ] Texto proposto para emenda de P14 na CONSTITUTION revisado por Andraus — **E19a: sem "via Risk Harness"** (C-03); só "Signal Package" fronteira + TMP interno
- [x] RISK-ARR-LOC-001 registrada como decisão aberta no ROADMAP (Controlador, 2026-09-22)
- [x] RISK-CONV-001 registrada como decisão aberta no ROADMAP (Controlador, 2026-09-22)
- [x] Posição da FASE RISK confirmada — FASE GOV já homologada; FASE RISK após FASE 6 (F-07)
- [ ] Formato da EUA-E19a confirmado como EUA enxuta (padrão EUA-E04 a EUA-E16)

---

*Produzido por Claude (claude.ai) em sessão com Andraus (2026-09-22).*
*Este documento consolida os dois Master Documents originais (SOT-RISK-MASTER-001 v1.0 arquitetura cognitiva + v1.0 engenharia de especificação) com os achados do parecer do Claude Code (2026-09-22).*
*Status: `[PROPOSTA]` — entra no repo como referência externa candidata via BL-018.*
