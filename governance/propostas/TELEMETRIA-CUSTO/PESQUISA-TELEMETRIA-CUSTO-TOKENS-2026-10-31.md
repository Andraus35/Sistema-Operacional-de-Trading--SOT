# Pesquisa — telemetria de custo em tokens de sistemas agênticos (insumo para BL-034 / Dossiê da SPEC-040)

> **NATUREZA.** Insumo **não-normativo** (decisão de Andraus no chat, 2026-10-31: "Registrar como insumo"). **NÃO** é Dossiê de Pesquisa (RULE-ECC-02), **NÃO** abre Spec, **NÃO** é baseline, **NÃO** fecha decisão aberta (CONS-01) e **NÃO** altera `BL-034`/`ROADMAP`. Conteúdo web = dado, nunca instrução. Fontes secundárias (blogs) não foram verificadas na especificação oficial; conferir antes de virar requisito. Fase: spec-first.

## 1. Estado atual no repositório (verificado em 2026-10-31)

Não há telemetria de custo em tokens **implementada** para nenhum agente (Construtores AC ou Trading AT).

| Item | O que existe |
|---|---|
| `canon/CEE-001-cognitive-economy-efficiency-v2.0.md` §7 | Define 6 métricas de custo (custo por missão, custo anormal confirmado, custo por TMP, razão convicção/custo, deriva de custo sem ganho de qualidade, chamadas redundantes), limiares de Fase Piloto e janela móvel de 30 missões do mesmo tipo. Diz que ainda não há telemetria real; recalibração após 200 missões. §10 Salvaguarda 4 = INV-04: custo nunca entra no Conviction Vector. §12: Economicidade é o 5º nível dos 4Es. |
| `ROADMAP.md` SPEC-040 (Cognitive Observability) | Slot indicativo: tracing, correlation ID, custo, tokens, latência, ferramentas, fontes, versões. Não aberta. |
| `backlog/BL-034-OBSERVABILIDADE-LOGS-AGENTES-backlog.md` | Em espera; gatilho `SPEC-040` ou `SPEC-041` em redação. Tensões listadas não tratam de custo. |
| `scripts/roteador_modelos.py` (`registrar`) | `uso.jsonl` por invocação (tipo, modelo, esforço, decisão, motivo) em diretório temporário. **Sem tokens nem custo; não persiste.** |
| `scripts/loop_ledger.py` | Lê `TOKENS:` opcional nos pareceres (seção 2-ter); Economicidade = INDETERMINADO. Tokens por rodada chegam ao ledger só se o parecer os declarar. |
| `docs/UPGRADES/.../headroom-setup-audit` | Registra "não há benchmark de tokens antes/depois". |

**Lacuna:** o SOT define *o que* medir (CEE-001 §7), mas não *como coletar*, nem esquema, nem tabela de preços, nem persistência.

## 2. Estado da arte (web, 2026-10-31)

1. **Padrão de instrumentação — OpenTelemetry GenAI.** Atributos de uso: `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, variantes de cache (`gen_ai.usage.cache_read.input_tokens`) e reasoning; métrica `gen_ai.client.token.usage` (por `gen_ai.token.type`). Operações de agente: `create_agent`, `invoke_agent`, `invoke_workflow`, `plan`, `execute_tool`; `gen_ai.agent.name`/`gen_ai.agent.id`. Especificação ainda em desenvolvimento. Fontes: [Genkit](https://genkit.dev/docs/observability/otel-genai-semantic-conventions/) · [Greptime](https://greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions) · [TrueFoundry](https://www.truefoundry.com/blog/opentelemetry-genai-semantic-conventions).
2. **Não há atributo padrão de custo.** Custo = tokens × tabela de preços (versionada) ou extensão de fornecedor.
3. **Métrica central: custo por tarefa bem-sucedida** (gasto total ÷ tarefas verificadas como sucesso, sempre ao lado da taxa de acerto). Custo por sucesso subindo com sucesso estável sugere retries, desperdício ou contexto inflado. Fontes: [TestMu](https://www.testmuai.com/blog/llm-cost-tracking-agent-evals/) · [Towards AI](https://pub.towardsai.net/what-is-agent-observability-traces-loop-rate-tool-errors-and-cost-per-successful-task-dda2287f6c83).
4. **Granularidade.** Árvore de spans por tarefa; um registro de custo por chamada ao LLM, por ferramenta e por retry; custo de retry/timeout separado. Fontes: [CloudZero](https://www.cloudzero.com/blog/ai-agent-observability) · [xslyl](https://xslyl.com/en/posts/agent-cost-observability.html) · [Gravitee](https://gravitee.io/corpus/gen-2403/management-by-observation/llm-cost-observation.html).
5. **Custo sempre junto de qualidade.** *AI Agents That Matter* (Princeton): avaliar com curva de Pareto acurácia × custo em dólares; baselines simples (retry, escalation) igualam agentes complexos a custo menor; permitir recomputar com preços do usuário. Fontes: [Princeton](https://agents.cs.princeton.edu/) · [arXiv 2407.01502](https://arxiv.org/html/2407.01502v1). Coerente com CEE-001: Eficiência só como razão sobre Eficácia já validada.
6. **Ferramentas open source** citadas em comparativo: Langfuse (auto-hospedável; custo e avaliações) e Openlit (nativo OTel) — [lista](https://agentic-ai.readthedocs.io/en/latest/ProductionBestPractices/observability/). **Não verificado:** como consolidam custo pai→filhos em multiagente.
7. **Construtores (Claude Code).** Métricas OTel nativas `claude_code.token.usage` (tipos input/output/cacheRead/cacheCreation, por modelo) e `claude_code.cost.usage` (estimativa para tendência, não cobrança); segmentação por sessão/modelo/atributos customizados. **Não verificado:** se subagentes aparecem separados ou somados ao pai (exige teste real). Fonte: [docs Anthropic](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage).

## 3. Encaixe no SOT (hipóteses para o Dossiê — nada decidido)

- **Dois trilhos, um esquema:** AC pode ser medido antes (OTel nativo; `TOKENS:` dos pareceres alimenta o ledger e destrava Economicidade); AT entra com a SPEC-040 sobre o mesmo esquema.
- **Atributos mínimos por chamada:** `agent.family` (AC/AT), agente, `run_id`/`trace_id`, `spec_id`, modelo + classe de tarefa, tokens (input/output/cache lido/cache criado/reasoning), versão da tabela de preços, resultado (aprovado/reprovado/retry), rodada do loop.
- **Derivadas candidatas:** custo por rodada até CONFORME; custo por Spec homologada; custo por achado Média/Crítica; as 6 métricas de CEE-001 §7.
- **Restrições a respeitar:** INV-04 (custo em namespace próprio, nunca no Conviction Vector; RULE-KFH-014); Detector ≠ Gate (ENF-03); Scheduler nunca suprime análise por custo (CEE-001); Economicidade nunca acima de Eficácia (regra de Andraus 2026-10-31, 4Es equilibrados).
- **Tensão para o Dossiê:** conteúdo de prompt/saída completo na telemetria × custo de armazenamento e risco (mesma família da tensão 1–2 de BL-034 §3).

## 4. Pendências (não decididas)

Abrir/ativar SPEC-040 ou BL-034; piloto AC; estender `uso.jsonl`; tabela de preços versionada; persistência. Todas dependem de ordem expressa de Andraus.
