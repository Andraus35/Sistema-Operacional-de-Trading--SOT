# Índice de agentes — Construção × Trading

> **Não-normativo** (referência de leitura; a fonte de verdade é `GLOSSARIO.md` §1-bis e `AGENTS.md` §3). Criado por DHR-AGENTES-001 (decisão de Andraus em chat, 2026-10-17). Existe para que ninguém confunda **quem constrói o SOT** com **quem opera o SOT em mercado**.

## A regra de uma linha

| Família | Pergunta que responde | Sigla | Vive em |
|---|---|---|---|
| **Agentes de Construção** | "Quem escreve, revisa e audita as Specs e o harness?" | **AC** | `.claude/agents/`, `scripts/`, `.github/` |
| **Agentes de Trading** | "Quem analisa o mercado e produz o Signal Package?" | **AT** | `specs/*.spec.md`, `rag/`, `schemas/`, `specs/features/` (Specs de domínio) |

**Teste rápido:** se o agente roda **antes** de existir sinal (escreve/valida documento) → AC. Se ele só existe **depois** que o SOT estiver em operação (lê candle, forma hipótese, calcula convicção) → AT. AC **nunca** analisa mercado; AT **nunca** edita Spec ou repositório.

## 1. Agentes de Construção (AC)

| Nome canônico | Arquivo / mecanismo | Papel | Poder |
|---|---|---|---|
| **Orquestrador** (da sessão) | sessão do Claude Code (sem arquivo) | Coordena, roda gates, handoff, PR/merge, delega | Bash + todas as ferramentas |
| **Especificador SOT** | `.claude/agents/especificador.md` | Produz Specs, Plans, Tasks, atas | Read/Write/Edit/Grep/Glob/Web |
| **Revisor SOT** | `.claude/agents/revisor.md` | Audita e emite parecer (ENF-03) | Somente leitura + `revisor_gate` |
| `sot-spec-reviewer` | `.claude/agents/sot-spec-reviewer.md` | Revisão independente de specs | Somente leitura |
| `sot-schema-validator` | `.claude/agents/sot-schema-validator.md` | Valida schemas JSON | Somente leitura |
| **Auditor Externo** | `governance/propostas/AUDITOR-EXTERNO/` (Codex, fora do repo) | Auditoria consultiva de outra família de modelo | Somente leitura; responde só ao Orquestrador |
| Gates determinísticos | `scripts/`, hooks, CI | Detectores/gates de código (Classe D) — não são "agentes" cognitivos | Sem LLM |

Decisor final de ambas as famílias: **Andraus** (humano; não é agente).

## 2. Agentes de Trading (AT) — o produto

| Nome canônico (CEM-001) | Nome operacional | Papel | Observação |
|---|---|---|---|
| Structural Agent | **Elliott Specialist** | Hipótese estrutural primária | Só ele cria hipótese PRIMARY |
| Institutional Agent | **SMC Specialist** | Sub-hipótese institucional | |
| Fibonacci Agent | **Fibonacci Validator** | Validação geométrica | Não cria contagem |
| Operational / Execution Agent | **ICT Specialist** | Setup operacional | **Não cria hipótese** de nenhum tipo |
| **Manager Agent** (Fases 0/1/2) | Manager Agent | Missão, despacho, convicção e síntese | Absorveu Master Orchestrator, Mission Engine e Synthesis Agent |
| **Risk Agent** | FASE RISK (RISK-M1..M6) | Gate de risco antes do Bot Trade Finance | Não autorizado até `milestone:FASE 6 concluída` |

Estado: **spec-first** — nenhum AT está implementado; existem apenas Specs (`specs/*.spec.md` de 1ª geração, marcadas `GEN-1_REFERENCE`, e Specs de domínio em `specs/features/`).

## 3. Armadilhas de vocabulário (leia antes de buscar)

| Termo | Pode significar | Como desambiguar |
|---|---|---|
| **Orquestrador** × **Orchestrator** | AC: a sessão que coordena a construção × termo legado de runtime (CONSTITUTION), hoje **Manager Agent** (AT) | Em texto novo: "Orquestrador (construção)" e "Manager Agent (trading)". |
| **Spec** / `specs/` | `specs/*.spec.md` = especificação de **um agente de trading** (GEN-1) × `specs/features/SPEC-00x/` = especificação **de construção/feature** produzida por AC | Sempre diga "spec de agente de trading" ou "Spec numerada (SPEC-00x)". |
| **Revisor** × **Risk Agent** | AC verifica documentos × AT veta risco em operação | Nunca se substituem. |
| **Trilha A / Trilha B** | Eixos de sequenciamento do CATALOGO/ROADMAP (maquinário de governança × specs de domínio) — **outra divisão**, não esta | Famílias AC/AT ≠ Trilhas A/B. Não usar um nome pelo outro. |
| **Agente** sem qualificador | ambíguo | Em documento **novo**, use "agente de construção" ou "agente de trading". Não retroativo (INV-07). |
| Estrategista / Analista / Controlador | **Papéis de governança** (CEE-001 §9, GMC-001), não agentes executores | Não listar em AC nem AT. |

## 4. Regras de fronteira (resumo; texto vinculante em AGENTS.md §3)

1. **AC não decide trading; AT não edita o repositório.** Nenhum AT recebe Write/Edit sobre Specs.
2. **Roteamento de modelo é separado por família:** AC (camada meta, EUA-E19) × AT (RULE-CEE-002, Tipos I–V). Uma mudança de modelo em uma família não implica a outra.
3. **Métricas de custo/eficácia por família:** custo de construir ≠ custo de operar; custo nunca entra no Conviction Vector (INV-04).
4. **Mudança em um agente AC** → `.claude/agents/*.md` (só Andraus, AGENTS §10). **Mudança em um AT** → Spec numerada + gate de Spec (ROADMAP §23).
5. Um mesmo conceito não ganha dois nomes: onde houver equivalência, vale `GLOSSARIO.md` §2.
