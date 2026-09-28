# HARNESS-REPORT — SOT Specification Harness
**Data:** 2026-09-09 | **Versão:** 2.0 | **Executor:** Claude Code (Sonnet 4.6)
**Projeto:** Sistema de Operações e Tendências (SOT) — ORYX Agent

---

## Seção 1 — Inventário de fontes utilizadas

### ENGENHARIA GERAL.pdf (171 páginas — fonte primária)

| Documento | Páginas | Usado em |
|-----------|---------|----------|
| Doc01 — Constituição SOT | 16–20 | CONSTITUTION.md (princípios P01–P14), RULES.md |
| Doc02 — ADS (Agent Design Spec) | 21–30 | CONSTITUTION.md (estados cognitivos), specs/ |
| Doc03 — GAS (Global Architecture) | 31–42 | CONSTITUTION.md (Blackboard, Digital Twin) |
| Doc04 — ECES (Elliott Cognitive Engine) | 43–53 | elliott-wave.spec.md, rag/elliott-wave.knowledge.md, schemas |
| Doc05 — FCES (Fractal Confluence) | 54–61 | fibonacci.spec.md, rag/fibonacci.knowledge.md |
| Doc06 — CES (Conviction Engine) | 62–71 | synthesis.spec.md, CONFLICT-MAP.md, synthesis schemas, rag/synthesis.knowledge.md |
| Doc07 — IIES (Institutional Intelligence) | 72–82 | smc.spec.md, rag/smc.knowledge.md, schemas |
| Doc08 — IEIES (ICT Execution) | 83–93 | ict.spec.md, rag/ict.knowledge.md, schemas |
| Doc09 — MOES (Mission Orchestration) | 94–102 | synthesis.spec.md (TMP), synthesis schemas |
| Doc10 — KGS (Knowledge Graph) | 103–109 | referenciado, gap pendente |

### ARIA_Plano_Mestre.md (783 linhas)

| Seção | Usado em |
|-------|----------|
| §5 — Scoring Matrix (0-9) | synthesis.spec.md, RULES.md (RULE-SY-*) |
| §6 — Position sizing | synthesis.output.json (sizing_sugerido) |
| §7 — Telegram alert | synthesis.output.json (alerta_telegram), rag/synthesis.knowledge.md |
| §10 Skill1-4 | specs/*, rag/* |

### SAS-001_Cap1_Pos_Correcoes.md (185 linhas)
| Seção | Usado em |
|-------|----------|
| Missão e antiescopo Elliott | elliott-wave.spec.md, rag/elliott-wave.knowledge.md |

### CEE-001_Versao_Consolidada.md (novo — v2.0)
| Seção | Categoria | Usado em |
|-------|-----------|----------|
| §2 Framework 3E | SP | CONSTITUTION.md (nova seção) |
| §3 Prioridade hierárquica | SP/RL | CONSTITUTION.md + RULES.md (RULE-CEE-001) |
| §5 Roteamento por complexidade | RL | CONSTITUTION.md (tabela), RULES.md (RULE-CEE-002) |
| §6.1 InferenceContextEnvelope | SC | schemas/inference-context-envelope.json + rag/synthesis.knowledge.md |
| §10 Salvaguardas Constitucionais | RL | RULES.md (RULE-CEE-004) |

### GMC-001_Versao_Consolidada.md (novo — v2.0)
| Seção | Categoria | Usado em |
|-------|-----------|----------|
| §1 Princípios 1-5 | RL | RULES.md (RULE-GMC-001 a RULE-GMC-005) |
| §2-5 Processo, catálogo | GO | Descartado (governança interna) |

### SDD-001_Versao_Consolidada.md (novo — v2.0)
| Seção | Categoria | Usado em |
|-------|-----------|----------|
| §3.1 Template SPEC (EARS) | SP | CONSTITUTION.md (validado — template já usado) |
| §4 Constitution Check | RL | RULES.md (RULE-SDD-002) |
| §5 Living Spec | SP | RULES.md (RULE-SDD-001) |

### PPQ-001_Versao_Consolidada-1.md (novo — v2.0)
| Seção | Categoria | Usado em |
|-------|-----------|----------|
| §3 Diretriz Mestra | SP | CONSTITUTION.md (referenciado) |
| §10.2 Dial GES (4 Níveis) | RL | RULES.md (RULE-PPQ-001) |
| §4-9 Stage-Gate, RACI, 5W2H | GO | Descartado |

### KERNEL V2.docx.pdf (novo — v2.0)
| Seção | Categoria | Usado em |
|-------|-----------|----------|
| EC-COG-004 Blackboard: 8 workspaces, Regras 1-5 | SP/RL/SC | CONSTITUTION.md (tabela + regras), RULES.md (RULE-BB-001 a BB-005) |
| EC-COG-005 Cognitive Event Bus: taxonomia | SC | referenciado |
| 12 domínios arquiteturais | SP | CONSTITUTION.md (tabela) |
| SOT Design Patterns | SP | CONSTITUTION.md + specs/ |
| EC-COG-001 a EC-COG-003 | SC | referenciado |

---

## Seção 2 — Resultados de validação (Parte 2-B)

### 2.1 harness-score v1.6.5

**Nível de maturidade: L2 "Guided"**

```
Score: 71/108 (66%)   Detectado: Claude Code, Cline

Context & Guides     85%  17/20 pts  ████████████████████
Skills & Commands   100%  17/17 pts  ████████████████████  ← 100%
Hooks & Guardrails    0%   0/14 pts  (requer criação manual de .claude/settings.json)
Sensors & Feedback   40%   8/20 pts
CI Feedback          79%  11/14 pts
Hygiene & Safety     78%  18/23 pts
```

**Evolução:** L0 (14/108, 13%) → L2 (71/108, 66%) na mesma sessão.

**Para atingir L3** (sensors ≥ 60%): adicionar `.eslintrc.json`, `tsconfig.json`, `.prettierrc`.
**Para Hooks/Guardrails (+14 pts)**: criar `.claude/settings.json` com hooks manualmente (bloqueado em auto-mode por política de auto-modificação).

### 2.2 harness-eval (Track A Correctness)

**Inventário:** T0: 1 | T1: 2 | T2: 4 | Claims: 114 | Plants: 6
**Resultado:** 10 BROKEN — **todos nas docs internas do harness-eval**, não nos arquivos SOT-Harness.

Os 10 broken referem-se a paths genéricos no SKILL.md e PROTOCOL.md do harness-eval (`.agents/skills`, `.cursor/skills`, `lib/...`, `bin/console`) que não existem neste repositório — comportamento esperado para ferramenta instalada em repositório de especificação.

**Conclusão:** 0 broken nas especificações SOT. Harness factualmente correto.

**Tracks B e C** (redundância e utilidade): não executadas — requerem aprovação do usuário via Q2 e consomem tokens LLM significativos. Tracks opcionais conforme `agent-skills` SKILL.md.

---

## Seção 3 — Resultados da Cross-validation (Parte 3)

| Verificação | Resultado |
|---|---|
| RULE-EW-002 threshold atualizado para 60% | ✓ |
| `directional_conflict` presente em synthesis.input.json | ✓ |
| `approved_hypothesis` permite null em ict.input.json | ✓ `"type": ["object", "null"]` |
| 4 estados de sinal em synthesis.output.json | ✓ COMPRA/VENDA/NEUTRO/AGUARDAR_SETUP |
| R:R mínimo 2:1 declarado em synthesis.output.json | ✓ `"minimum": 2.0` |
| ICT INACTIVE como primeiro comportamento em ict.spec.md | ✓ |
| 5 salvaguardas constitucionais (CEE-001 §10) em RULES.md | ✓ RULE-CEE-004 |
| Blackboard 8 workspaces em CONSTITUTION.md | ✓ nova seção |
| 5 regras do Blackboard em RULES.md | ✓ RULE-BB-001 a BB-005 |
| Framework 3E em CONSTITUTION.md | ✓ nova seção |
| InferenceContextEnvelope schema | ✓ criado |
| RAG synthesis.knowledge.md | ✓ 12 chunks criados |
| 11/11 schemas JSON válidos | ✓ |
| 5/5 specs com EARS + seções obrigatórias | ✓ |
| Hierarquia metodológica consistente em todos os arquivos | ✓ |

---

## Seção 4 — Lacunas identificadas

### GAP-001: KERNEL V2.docx — RESOLVIDO ✓
**Resolução (v2.0):** Lido via `KERNEL V2.docx.pdf`. EC-COG-004 (Blackboard) e EC-COG-005 (Event Bus) incorporados ao CONSTITUTION.md e RULES.md.

### GAP-002: Documentos em `PLANEJAMENTO\Nova pasta\` — PARCIALMENTE RESOLVIDO
**O que foi lido:** CEE-001, GMC-001, SDD-001, PPQ-001 (pasta `Projeto 1 - ORYX Agent\01_Governanca_Geral\`)
**Ainda pendente:** outros arquivos .docx em `PLANEJAMENTO\Nova pasta\` (ferramentas sem pandoc disponível)
**Impacto:** Moderado — provavelmente regras operacionais adicionais

### GAP-003: Algoritmo do Conviction Vector não especificado — PENDENTE (Alta prioridade)
**Status:** Mantido. Doc06 descreve as 8 dimensões mas não fornece fórmula de ponderação por independência.
**Proposta:** Nenhuma dimensão individual < 30%. Criar spec `conviction-algorithm.md`.

### GAP-004: Schema pattern_memory — PENDENTE (Baixa prioridade)
**Status:** Mantido. Campos documentados em rag/synthesis.knowledge.md mas schema formal ausente.
**Solução:** Criar `schemas/pattern-memory.json`.

### GAP-005: Knowledge Graph (EC-COG-003 / Doc10) — PENDENTE (Baixa prioridade)
**Status:** Mantido. Arquitetura de memória relacional não especificada.

### GAP-006: Event Bus (EC-COG-005) — NOVO — PENDENTE
**O que contém:** Taxonomia completa de eventos cognitivos (Market, Elliott, Fibonacci, Institutional, Context, Conviction, Mission, Learning, BotFinance events).
**Impacto:** Schema de eventos para pub/sub não formalizado.
**Solução:** Criar `schemas/cognitive-event.json`.

### GAP-007: Blackboard schema formal — NOVO — PENDENTE
**O que contém:** EC-COG-004 define 8 workspaces e estados de objeto.
**Impacto:** Agentes publicam no Blackboard mas o schema de mensagem não está formalizado.
**Solução:** Criar `schemas/blackboard-message.json` e `specs/blackboard.spec.md`.

---

## Seção 5 — O que ainda precisa de especificação

### Prioridade ALTA (bloqueia implementação)

1. **Algoritmo do Conviction Vector** (GAP-003)
   — Criar `specs/conviction-algorithm.md` com fórmula de independência ponderada

2. **Schema Blackboard** (GAP-007)
   — Criar `schemas/blackboard-message.json` + `specs/blackboard.spec.md`

3. **Schema Cognitive Event Bus** (GAP-006)
   — Criar `schemas/cognitive-event.json` baseado em EC-COG-005

### Prioridade MÉDIA

4. **Integração TradingView** — spec de webhook receptor, autenticação, parsing
5. **Schema pattern_memory** (GAP-004) — `schemas/pattern-memory.json`
6. **Schema Trading Mission Package completo** — `schemas/trading-mission-package.json`
7. **Integração Telegram** — spec de envio do alerta

### Prioridade BAIXA

8. **Spec do Knowledge Graph** (GAP-005)
9. **Spec de backtesting e validação histórica**
10. **Spec de monitoramento de posição aberta**

---

## Seção 6 — Próximos passos recomendados

### Passo 1 — Completar GAP-003 (Conviction Vector algorithm)
```
Criar SOT-Harness/specs/conviction-algorithm.md
Definir: peso por dimensão, regra de independência, penalizações por correlação
Criar SOT-Harness/schemas/conviction-vector.json
```

### Passo 2 — Implementar Elliott Specialist como primeira prova de conceito
Usando os arquivos do SOT-Harness como referência:
- Entrada: `schemas/elliott-wave.input.json`
- Comportamento: `specs/elliott-wave.spec.md`
- Regras: `RULES.md` seção RULE-EW-*
- Conhecimento: `rag/elliott-wave.knowledge.md`
- Saída: `schemas/elliott-wave.output.json`
- Modelo: Claude Sonnet (Tipo III — julgamento especialista)
- Envelope: `schemas/inference-context-envelope.json`

### Passo 3 — Atingir harness-score L3
Para subir de L2 → L3 (sensors ≥ 60%):
```bash
# Criar .eslintrc.json para SNS-02 (+5 pts)
# Criar tsconfig.json para SNS-03 (+4 pts)
# Criar .prettierrc para SNS-04 (+3 pts)
# Criar .claude/settings.json com hooks para HKS-01 a HKS-05 (+14 pts)
```
Criar `.claude/settings.json` manualmente (fora do modo automático) com:
```json
{ "hooks": { "PreToolUse": [{"matcher": "Write|Edit", "hooks": [{"type": "command", "command": "node scripts/gate-check.js"}]}], "PostToolUse": [{"matcher": "Write|Edit", "hooks": [{"type": "command", "command": "node scripts/post-edit-check.js"}]}] } }
```

### Passo 4 — Pipeline end-to-end
Construir fixtures de teste usando os schemas de I/O e validar o pipeline completo:
Elliott → Fibonacci → SMC → ICT → Synthesis com dados históricos de BTC.

---

## Seção 7 — Inventário completo de arquivos produzidos

```
SOT-Harness/
├── AGENTS.md                    — Context file para agentes (CTX-01/02 ✓)
├── README.md                    — Introdução do projeto (CTX-07 ✓)
├── CONSTITUTION.md              — 14 princípios + Framework 3E + Blackboard + 12 domínios
├── RULES.md                     — 55+ regras (RULE-*, RULE-EW-*, FB-*, SM-*, ICT-*, SY-*, CEE-*, GMC-*, BB-*, SDD-*, PPQ-*)
├── CONFLICT-MAP.md              — Tabelas de conflito direcional, fractal, temporal, convicção
├── HARNESS-REPORT.md            — Este arquivo (v2.0)
├── package.json                 — test + lint scripts (SNS-01 ✓)
├── package-lock.json            — Lockfile (HYG-07 ✓)
├── .gitignore                   — Inclui .env (HYG-01/02 ✓)
├── .clinerules/
│   ├── sot-specs.md             — Regras scoped para specs/ (CTX-03 ✓)
│   ├── sot-schemas.md           — Regras scoped para schemas/
│   └── sot-rag.md               — Regras scoped para rag/
├── .claude/
│   ├── skills/
│   │   ├── SKILL.md             — Skill principal (SKL-01/02/04 ✓)
│   │   ├── validate-sot-spec.md — Skill validação de specs
│   │   └── update-harness.md    — Skill atualização do harness
│   ├── agents/
│   │   ├── sot-spec-reviewer.md — Subagente revisor de specs (AGT-01/02 ✓)
│   │   └── sot-schema-validator.md — Subagente validador de schemas
│   └── commands/
│       ├── validate-harness.md  — Workflow de validação (SKL-03 ✓)
│       └── update-spec.md       — Workflow de atualização
├── scripts/
│   ├── gate-check.js            — Script hook gate (para HKS-05)
│   └── post-edit-check.js       — Script hook feedback
├── tests/
│   ├── validate-schemas.js      — Valida 11 schemas JSON (SNS-05 ✓)
│   └── lint-specs.js            — Lint 5 specs EARS (SNS-05 ✓)
├── .github/
│   └── workflows/ci.yml         — CI pipeline (CI-01/02/03 ✓)
├── specs/
│   ├── elliott-wave.spec.md
│   ├── fibonacci.spec.md
│   ├── smc.spec.md
│   ├── ict.spec.md
│   └── synthesis.spec.md
├── schemas/
│   ├── elliott-wave.input.json       ├── elliott-wave.output.json
│   ├── fibonacci.input.json          ├── fibonacci.output.json
│   ├── smc.input.json                ├── smc.output.json
│   ├── ict.input.json                ├── ict.output.json
│   ├── synthesis.input.json          ├── synthesis.output.json
│   └── inference-context-envelope.json  (novo v2.0 — CEE-001 §6.1)
└── rag/
    ├── elliott-wave.knowledge.md  — 15 chunks
    ├── fibonacci.knowledge.md     — 12 chunks
    ├── smc.knowledge.md           — 12 chunks
    ├── ict.knowledge.md           — 12 chunks
    └── synthesis.knowledge.md     — 12 chunks  (novo v2.0)
```

**Total v2.0:** 33 arquivos | 63 chunks RAG | 55+ regras | 11 schemas JSON Draft-07

### Comparação v1.0 → v2.0

| Dimensão | v1.0 | v2.0 | Δ |
|---|---|---|---|
| Arquivos totais | 18 | 33 | +15 |
| Chunks RAG | 51 | 63 | +12 (synthesis adicionada) |
| Regras | 40+ | 55+ | +15 (CEE-001, GMC-001, KERNEL V2, SDD-001, PPQ-001) |
| Schemas | 10 | 11 | +1 (InferenceContextEnvelope) |
| harness-score | L0 (14/108) | L2 (71/108) | +57 pts |
| Documentos fonte lidos | 3 | 8 | +5 |
