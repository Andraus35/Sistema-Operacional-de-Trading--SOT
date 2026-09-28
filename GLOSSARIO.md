# GLOSSÁRIO OFICIAL — SOT

**Sistema:** SOT — Sistema Operacional de Trading
**Status:** FATO NORMATIVO (homologado por Andraus, 2026-09-14 — Respostas ao Questionário de Resolução v1, Q-014/Q-015)
**Função:** unificar terminologia e identidade para leitura e busca por agentes de IA. Fonte única de equivalências de nomes.

---

## 1. Identidade do sistema (Q-015)

- **Nome canônico:** `SOT — Sistema Operacional de Trading`.
- A expansão anterior **"Sistema de Operações e Tendências"** está **DESCONTINUADA**. Todo cabeçalho novo usa "Sistema Operacional de Trading".
- **ORYX:** nome histórico do ecossistema/produto anterior. O projeto atual opera exclusivamente sob o nome **SOT**. Documentos baselined que mencionam "ORYX" permanecem válidos; a equivalência é registrada aqui e não exige reedição retroativa.

> Regra de leitura para agentes: onde um documento canônico disser "ORYX" ou "ecossistema ORYX/SOT", leia-se **SOT**.

---

## 2. Equivalência de nomes de agentes (Q-014)

Nomes canônicos (CEM-001 / KERNEL V2 / SAS-001) ↔ nomes operacionais (repositório SOT-Harness):

| Nome canônico (CEM-001/KERNEL) | Nome operacional (repo SOT) | Papel |
|---|---|---|
| Structural Agent | **Elliott Specialist** | Hipótese estrutural primária (Elliott) |
| Institutional Agent | **SMC Specialist** | Sub-hipótese institucional (SMC) |
| Fibonacci Agent | **Fibonacci Validator** | Validação geométrica (não cria contagem) |
| Execution Agent | **ICT Specialist** | Execução (não cria hipótese de nenhum tipo) |
| Fusion Engine | **Fusion Engine** (mantido) | Funde Evidências em Evidência DERIVED (CEM-001) |
| Conviction Engine | **Conviction Engine** (mantido) | Calcula o Conviction Vector (8 dimensões) |
| Synthesis Agent | **Synthesis Agent** (mantido) | Árbitro final; produz o Trading Mission Package |

### Agentes fora do escopo atual do SOT

**Macro Agent, Sentiment Agent, Risk Agent, Context Agent** — presentes na taxonomia genérica do modelo canônico CEM-001 (herança ORYX), **não serão especificados no roadmap atual**. Sua inclusão futura exige decisão explícita de Andraus. As Specs de produção de Evidência (ex.: SPEC-002) restringem a lista de produtores aos agentes do SOT acima.

---

## 2-bis. Aliases de Sucesso — Componentes Eliminados (2026-09-26)
<!-- Registrado pela Auditoria Taxonômica (2026-09-26); autoridade: ADR-MANAGER-001 + ADR-CONFLUENCE-001 v3 + ADR-MISSION-TYPES-001 (Andraus, 2026-09-26). INV-07: nomes antigos preservados aqui como referência histórica — NÃO usar em Specs futuras como componentes independentes. -->

> **Regra:** Se qualquer Spec, documento ou chunk de RAG mencionar os termos da coluna "Nome eliminado", o leitor deve substituir pela coluna "Sucessor canônico".

| Nome eliminado | Tipo | Sucessor canônico | Autoridade | Nota |
|---|---|---|---|---|
| `Master Orchestrator` | Componente legado | **Manager Agent** | ADR-MANAGER-001 | Absorvido integralmente |
| `Mission Engine` | Componente legado | **Manager Agent (Fase 0: Mission Lifecycle)** | ADR-MANAGER-001 | Absorvido na Fase 0 |
| `Decision Orchestrator` | Componente legado | **Manager Agent** | ADR-MANAGER-001 | Absorvido integralmente |
| `Orchestration Layer` | Camada legada | **Manager Agent (Fase 1: Dispatch)** | ADR-MANAGER-001 | Absorvido na Fase 1 |
| `Agente Decisor` | Componente legado | **Manager Agent** | ADR-MANAGER-001 | Absorvido na Fase 2 |
| `Agente de Síntese` (CES) | Componente legado | **Manager Agent (Fase 2: Conviction)** | ADR-MANAGER-001 | Absorvido na Fase 2 |
| `Fractal Confluence Engine (FCE)` | Componente legado | **`confluence-elliott`** (skill do Structural Agent) | ADR-CONFLUENCE-001 v3 | FCE extinto; funcionalidade como skill |
| `fractal-skill` | Skill eliminada | **`confluence-elliott`** | ADR-CONFLUENCE-001 v3 | Extinta |
| `fibonacci-skill` (única) | Skill eliminada | **`level-fibonacci-skill`** + **`confluence-fibonacci-skill`** | ADR-CONFLUENCE-001 v3 | Dividida em 2 skills distintas |
| `Conviction Engine` (motor separado) | Motor GEN-1 | **Manager Agent (Fase 2: Conviction)** | ADR-MANAGER-001 | Funcionalidade absorvida; Fase 2 = cognitivo leve |
| `Synthesis Agent` (árbitro LLM) | Agente GEN-1 | **Manager Agent (Fase 2: Conviction)** | ADR-MANAGER-001 | GEN-1_REFERENCE; será substituído pelo Manager Agent conforme SPEC-015 |

### Manager Agent — nomenclatura normativa das 3 fases

| Fase | Nome normativo | Tipo |
|---|---|---|
| Fase 0 | Manager Agent — Mission Lifecycle | Decisório leve |
| Fase 1 | Manager Agent — Dispatch | Mecânico/determinístico |
| Fase 2 | Manager Agent — Conviction | Cognitivo leve |

### Skills do Structural Agent (nomenclatura vigente — ADR-CONFLUENCE-001 v3)

| Skill | Função |
|---|---|
| `elliott-skill` | Contagem e score Elliott por grade (MTF: S1/D1/H4/H1) |
| `level-fibonacci-skill` | Valida Elliott com níveis Fibonacci |
| `confluence-fibonacci-skill` | Mede confluência de níveis Fibonacci entre timeframes (MTF: S1/D1/H4/H1) |
| `confluence-elliott` | Mede confluência das hipóteses Elliott entre timeframes (MTF: S1/D1/H4/H1) |

---

## 3. Termos e componentes cognitivos

| Termo | Definição canônica | Fonte |
|---|---|---|
| Hipótese | Melhor representação explicável do estado atual do domínio observado, produzida a partir da convergência de evidências independentes e continuamente sujeita à refutação. | CHM-001 §1.2 |
| Hipótese PRIMARY | Hipótese estrutural/direcional, criada **exclusivamente** pelo Elliott Specialist (Q-005). | Decisão Q-005 |
| Hipótese SUB | Sub-hipótese de domínio (SMC/Fibonacci), sempre referenciada à hipótese primária via `parent_id` (herança fractal do CHM-001). ICT **não** cria hipótese. | Decisão Q-005 |
| Evidência | Observação objetiva produzida por um agente especializado, capaz de sustentar/enfraquecer/refutar hipóteses. | CEM-001 |
| Conviction Vector | Vetor multidimensional de convicção — **8 dimensões** (Q-008): estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica. Fórmula/pesos/limiares definitivos = J-001 (aberto). | CONSTITUTION P02 (corrigido) / Decisão Q-008 |
| Conviction Global | Resultado sistêmico de convicção, calculado pelo modelo canônico **CCM-001** (pendente de redação — SPEC-003). | CHM-001 §1.9 |
| Fusion Engine | Motor determinístico que funde Evidências heterogêneas em Evidência DERIVED. Não calcula convicção. | CEM-001 / Decisão Q-007 |
| Conviction Engine | Motor que recebe Evidência DERIVED e calcula o Conviction Vector. **Separado** do Synthesis Agent (B-001 fechado). | Decisão Q-007 |
| Synthesis Agent | Árbitro final (LLM): recebe Conviction Vector + hipóteses e produz decisão / TMP (handoff interno à camada de risco). | Decisão Q-007 |
| TMP (Trading Mission Package) | Artefato **interno** de passagem — snapshot da decisão de síntese entregue por handoff à camada de risco (Síntese → Risk Agent). **Deixou de ser o artefato de fronteira** (EUA-E19a, 2026-09-22). Ancora INV-RISK-00 (isolamento epistêmico — SPEC-016 repurposada). | INV-05 (emendado); EUA-E19a |
| **Signal Package** | Artefato **de fronteira** — único artefato que atravessa a fronteira SOT → Bot Trade Finance. Termo fundacional (ENGENHARIA-GERAL l.604-606) restaurado pela EUA-E19a. O SOT não executa ordem. Contrato exato = D-RISK-SP-001 (aberta, RISK-SPEC-022). | INV-05 (emendado); EUA-E19a |
| **Score 0–9** | Score operacional agregado (Elliott + SMC + ICT, cada layer até 3 pontos). **Status: PILOT** — mantido como filtro paralelo até CCM-001/J-001 serem homologados (Andraus, 2026-09-26). **NÃO substitui o Conviction Vector 8D.** Limiares: `score ≥ 7/9` para sinal (Fase Piloto, Q-002, recalibrável). | RAG synthesis.knowledge.md / Q-002 / Decisão 2026-09-26 |
| **Manager Agent** | Único componente de orquestração do SOT. Não é agente analítico. Operam em 3 Fases: Fase 0 (Mission Lifecycle), Fase 1 (Dispatch), Fase 2 (Conviction). Absorve 6 componentes legados (ver §2-bis). SPEC-015 = spec formal. | ADR-MANAGER-001 (2026-09-26) |
| **Missão Exploratória** | Tipo de missão sem hipótese de entrada (`Hipotese_entrada = null`). Agentes formulam hipóteses locais livremente. Ponto de partida de qualquer ciclo. | ADR-MISSION-TYPES-001 (2026-09-26) |
| **Missão de Validação** | Tipo de missão com hipótese dominante do ciclo anterior como contexto. Agentes validam ou refutam. Se refutada → Plano B → nova Missão Exploratória. | ADR-MISSION-TYPES-001 (2026-09-26) |

---

## 3-bis. Terminologia Concorrente (RULE-SEM / MSC-001)
<!-- Registrado por EUA-E19a (DHR-EUA-E19a, Andraus 2026-09-22, CC-10). "TMP" NÃO foi deletado (INV-07) — apenas mudou de papel. -->

| Termos concorrentes | Acepção vigente | Papel |
|---|---|---|
| **TMP** vs **Signal Package** | Antes da E19a, "TMP" nomeava o artefato de fronteira. Após a E19a: **TMP = artefato interno** (Síntese → Risk Agent); **Signal Package = artefato de fronteira** (SOT → Bot Trade Finance). Todo uso decisivo para a distinção fronteira/interno DEVE declarar a acepção (RULE-SEM-01) e não redefinir estes termos (RULE-SEM-04). | Superseder de papel, não deleção (INV-07) |

---

## 4. Modelos canônicos (status de baseline — Q-001)

| Código | Nome | Status |
|---|---|---|
| CEM-001 | Canonical Evidence Model | **BASELINED** |
| CHM-001 | Canonical Hypothesis Model | **BASELINED** |
| CCM-001 | Canonical Conviction Model | **Pendente de redação** — responsabilidade da SPEC-003 |
| CDM-001 | Canonical Decision Model | **Pendente de redação** |
| CNM-001 | Canonical Narrative Model | **Pendente de redação** |

> Não invocar CONST-01 ("não redefinir modelo canônico") como bloqueio para CCM/CDM/CNM — não há canônico a proteger enquanto não redigidos.

---

## 5. Framework de prioridade (Q-009)

**4Es — hierarquia inviolável:** `Conformidade Constitucional > Eficácia → Efetividade → Eficiência → Economicidade`.
A antiga formulação "Framework 3E" (sem Economicidade) está **atualizada para 4Es**. Economicidade nunca sobe acima de Eficácia.

---

*Glossário oficial do SOT. Homologado por Andraus (Decisor Final), 2026-09-14. Alterações seguem o fluxo Especificador → Revisor → Andraus.*
