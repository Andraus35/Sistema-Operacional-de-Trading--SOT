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

## 1-bis. Duas famílias de agentes (DHR-AGENTES-001, 2026-10-17)

O repositório usa a palavra "agente" para dois grupos que **não se misturam**:

- **Agentes de Construção (AC)** — constroem e auditam o SOT enquanto ele é só especificação: **Orquestrador** (da sessão), **Especificador SOT**, **Revisor SOT**, `sot-spec-reviewer`, `sot-schema-validator`, **Auditor Externo**. Vivem em `.claude/agents/`, `scripts/`, `.github/`.
- **Agentes de Trading (AT)** — o produto, que analisará mercado em operação: **Elliott Specialist** (Structural), **SMC Specialist** (Institutional), **Fibonacci Validator**, **ICT Specialist** (Operational), **Manager Agent** (Fases 0/1/2) e o **Risk Agent** (FASE RISK). Vivem como Specs (`specs/*.spec.md` GEN-1, `specs/features/`), `rag/`, `schemas/`; nenhum está implementado.

**Regras de leitura:** (1) em documento **novo**, "agente" sem qualificador é ambíguo — escreva "agente de construção" ou "agente de trading" (não retroativo, INV-07); (2) **Orquestrador** = sessão que coordena a construção (AC); o termo legado **Orchestrator** de runtime foi absorvido pelo **Manager Agent** (AT); (3) `specs/*.spec.md` = spec de **um agente de trading**; `specs/features/SPEC-00x/` = Spec numerada produzida por AC; (4) **Famílias AC/AT ≠ Trilhas A/B** (eixos de sequenciamento do CATALOGO/ROADMAP); (5) Estrategista/Analista/Controlador são **papéis de governança**, não agentes executores. Índice completo e fronteiras: `docs/agentes/INDICE-AGENTES.md` (não-normativo).

---

## 2. Equivalência de nomes de agentes — **agentes de trading** (Q-014)

Nomes canônicos (CEM-001 / KERNEL V2 / SAS-001) ↔ nomes operacionais (repositório SOT-Harness):

| Nome canônico (CEM-001/KERNEL) | Nome operacional (repo SOT) | Papel |
|---|---|---|
| Structural Agent | **Elliott Specialist** | Hipótese estrutural primária (Elliott) |
| Institutional Agent | **SMC Specialist** | Sub-hipótese institucional (SMC) |
| Fibonacci Agent | **Fibonacci Validator** | Validação geométrica (não cria contagem) |
| Execution Agent | **ICT Specialist** | Execução (não cria hipótese de nenhum tipo) |
| Fusion Engine | **Fusion Engine** (mantido) | Funde Evidências em Evidência DERIVED (CEM-001) |
| Conviction Engine | **Mecanismo** (rótulo legado) — Classe D/H do CCM-001, **invocado pelo Manager Agent — Fase 2 (Conviction)** (DHR-ARQ-001; ver §2-bis l.55) | Calcula o Conviction Vector (8 dimensões) — não é agente/componente separado |
| Synthesis Agent | **Manager Agent — Fase 2 (Convicção & Síntese)** (DHR-ARQ-002, 2026-10-01 — absorvido; não é agente autônomo) | Árbitro final; produz o Trading Mission Package (TMP interno) — agora função da Fase 2 do Manager |

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
| `Synthesis Agent` (árbitro LLM) | Agente GEN-1 | **Manager Agent (Fase 2: Conviction)** | ADR-MANAGER-001; **DHR-ARQ-002** | GEN-1_REFERENCE; **absorção propagada por DHR-ARQ-002 (2026-10-01)** — escopo do slot SPEC-014 repurposado p/ a Spec do Manager-Fase-2 definida pela EUA-E23 (não SPEC-015; não renumerado, INV-07) |

### Manager Agent — nomenclatura normativa das 3 fases

| Fase | Nome normativo | Tipo |
|---|---|---|
| Fase 0 | Manager Agent — Mission Lifecycle | Decisório leve |
| Fase 1 | Manager Agent — Dispatch | Mecânico/determinístico |
| Fase 2 | Manager Agent — Conviction | Cognitivo leve |

> **Decomposição em Specs (EUA-E23/DHR-EUA-E23, 2026-10-01):** as 3 Fases do Manager Agent mapeiam 1:1 a **3 Specs** sob um **"Manager Contract"** comum (pai de herança vertical RULE-HV; ator único — ADR-MANAGER-001 §2.2), sem renumerar slots (INV-07): **Fase 1 → SPEC-008 "Manager — Orquestração Mecânica"** (D/C); **Fase 0 → SPEC-015 "Manager — Missão & Ciclo de Vida"** (H/P); **Fase 2 → SPEC-014 "Manager — Convicção & Síntese"** (H/P; absorve o Synthesis Agent — DHR-ARQ-002). Slots **indicativos** (RULE-ECC-01/02): fronteira final só na abertura. SPEC-015-SCOPE/J-001/N-001/M-001/WF-D03 seguem abertas (CONS-01).

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
| Conviction Global | Resultado sistêmico de convicção, calculado pelo modelo canônico **CCM-001** (**BASELINED** — SPEC-003/DHR-SPEC003-001, 2026-10-02; estrutura/método/mecanismo + limiares-piloto; valores definitivos = J-001/N-001, abertos). | CHM-001 §1.9; CCM-001 |
| Fusion Engine | Motor determinístico que funde Evidências heterogêneas em Evidência DERIVED. Não calcula convicção. | CEM-001 / Decisão Q-007 |
| Conviction Engine | **Mecanismo legado** (não agente/componente independente — DHR-ARQ-001, 2026-10-01): recebe Evidência DERIVED e calcula o Conviction Vector, como **etapa invocada pelo Manager Agent — Fase 2 (Conviction)** (ADR-MANAGER-001 / CEM-001 DIV-CEM-4). B-001 (Q-007) parcialmente SUPERSEDIDA na parte "componente separado"; preservada a separação **lógica** de etapas Fusão→cálculo do Conviction Vector→síntese; INV-07. Rótulo de Classe D/H do CCM-001 (SPEC-003). | Decisão Q-007; ADR-MANAGER-001; DHR-ARQ-001 |
| Synthesis Agent | **Absorvido pelo Manager Agent — Fase 2 (Convicção & Síntese)** (DHR-ARQ-002, propaga ADR-MANAGER-001 §2.1). Não é agente autônomo. A Fase 2 do Manager: recebe Conviction Vector + hipóteses, arbitra, forma Convicção Global (invocando o mecanismo da SPEC-003) e produz decisão / TMP interno (handoff à camada de risco). | Decisão Q-007; ADR-MANAGER-001; DHR-ARQ-002 |
| TMP (Trading Mission Package) | Artefato **interno** de passagem — snapshot da decisão de síntese entregue por handoff à camada de risco (Síntese → Risk Agent). **Deixou de ser o artefato de fronteira** (EUA-E19a, 2026-09-22). Ancora INV-RISK-00 (isolamento epistêmico — SPEC-016 repurposada). | INV-05 (emendado); EUA-E19a |
| **Signal Package** | Artefato **de fronteira** — único artefato que atravessa a fronteira SOT → Bot Trade Finance. Termo fundacional (ENGENHARIA-GERAL l.604-606) restaurado pela EUA-E19a. O SOT não executa ordem. Contrato exato = D-RISK-SP-001 (aberta, RISK-SPEC-022). | INV-05 (emendado); EUA-E19a |
| **Score 0–9** | Score operacional agregado (Elliott + SMC + ICT, cada layer até 3 pontos). **Status: PILOT** — mantido como filtro paralelo até CCM-001/J-001 serem homologados (Andraus, 2026-09-26). **NÃO substitui o Conviction Vector 8D.** Limiares: `score ≥ 7/9` para sinal (Fase Piloto, Q-002, recalibrável). | RAG synthesis.knowledge.md / Q-002 / Decisão 2026-09-26 |
| **Manager Agent** | Único componente de orquestração do SOT. Não é agente analítico. Opera em 3 Fases: Fase 0 (Mission Lifecycle), Fase 1 (Dispatch), Fase 2 (Conviction). Absorve 6 componentes legados (ver §2-bis). **Specs formais (EUA-E23/DHR-EUA-E23):** 3 Specs sob o "Manager Contract" — SPEC-008 (Orquestração Mecânica/Fase 1), SPEC-015 (Missão & Ciclo de Vida/Fase 0), SPEC-014 (Convicção & Síntese/Fase 2; absorve Synthesis). Slots indicativos, não renumerados (INV-07). | ADR-MANAGER-001 (2026-09-26); DHR-EUA-E23 (2026-10-01) |
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
| CCM-001 | Canonical Conviction Model | **BASELINED** (v1.0; SPEC-003/DHR-SPEC003-001, 2026-10-02) — `canon/CCM-001-canonical-conviction-model.md` |
| CDM-001 | Canonical Decision Model | **Pendente de redação** |
| CNM-001 | Canonical Narrative Model | **Pendente de redação** |

> Não invocar CONST-01 ("não redefinir modelo canônico") como bloqueio para CCM/CDM/CNM — não há canônico a proteger enquanto não redigidos.

---

## 5. Framework de prioridade (Q-009)

**4Es — hierarquia inviolável:** `Conformidade Constitucional > Eficácia → Efetividade → Eficiência → Economicidade`.
A antiga formulação "Framework 3E" (sem Economicidade) está **atualizada para 4Es**. Economicidade nunca sobe acima de Eficácia.

---

*Glossário oficial do SOT. Homologado por Andraus (Decisor Final), 2026-09-14. Alterações seguem o fluxo Especificador → Revisor → Andraus.*
