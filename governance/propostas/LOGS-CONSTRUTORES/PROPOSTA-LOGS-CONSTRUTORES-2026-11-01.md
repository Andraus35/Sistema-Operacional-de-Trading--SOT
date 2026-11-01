# PROPOSTA — Consolidação dos logs dos agentes Construtores (AC)

> **Status: PROPOSTA — não aplicada, não normativa, não é baseline.** Ordem de Andraus (chat, 2026-11-01): "consolidar e solidificar os logs apenas dos construtores segundo melhores práticas e estado da arte; ver referência master no repo; a parte para agentes do Trading fica para Spec ou backlog próprio". Esta proposta **não abre Spec**, **não fecha decisão aberta** (CONS-01) e **não altera** hooks, scripts selados, `AGENTS.md` ou `MECANISMOS.json`. Aplicar exige ordem expressa de Andraus + ata + `MECANISMOS.json` no mesmo PR (COE-14).

## 0. Escopo e fronteira
- **Dentro:** logs de quem **constrói** o SOT — Especificador, Revisor, Orquestrador, hooks e detectores deste repositório (família AC, `AGENTS.md` §3.1).
- **Fora:** logs do **produto em operação** (agentes de Trading, AT). Continuam em **SPEC-040/041/042** (slots indicativos) e no backlog **BL-034** (master), **BL-036..042** (telemetria de custo) e **BL-038** (extensão do esquema aos AT). Nenhum item novo de backlog é necessário: o BL-038 já é o "backlog próprio" dos AT. O esquema abaixo é **só AC** e foi desenhado para a SPEC-040 poder **reutilizá-lo ou substituí-lo sem migração forçada** (campo `family`; sem pré-empção, EUA-E21).
- **Custo** nunca entra no Conviction Vector (INV-04). Tokens/USD aqui são **dado de processo**, custo equivalente de API, não cobrança.

## 1. Fontes
- **Master do repositório (NÃO-normativo):** `reference/externo/Uso de Logs por Agentes de IA.MD` — princípio central "log não é memória, é evidência estruturada da execução"; run/trace/span (§5–7); registro mínimo por run (§8); metadados sempre, conteúdo só por política (§10–11); invariantes e política (§23–24); aprovação humana (§25); schema mínimo (§29); sampling (§32), retenção (§33), redaction (§34), integridade (§35); níveis (§36); log ≠ memória (§37).
- **Estado da arte (consulta rápida, 1 busca, 2026-11-01):** as convenções **OpenTelemetry GenAI** para agentes (`invoke_agent`, `execute_tool`, `gen_ai.agent.*`, `gen_ai.usage.*`) seguem com status **Development** — [especificação oficial](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans); relato de que em 12/06/2026 migraram para um repositório dedicado ([Greptime](https://greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions) e [Dash0](https://www.dash0.com/knowledge/opentelemetry-genai-semantic-conventions-explained) divergem em detalhes — **conferir a versão corrente antes de congelar nomes**). **Consequência de projeto:** usar OTel só como **vocabulário e mapeamento** (campos nomeados de forma convertível), **sem dependência de runtime** e **sem congelar** atributos instáveis.
- **Limite honesto:** isto é uma verificação rápida, **não um Dossiê de Pesquisa** (RULE-ECC-02, que se aplica a Spec nova). Se Andraus quiser promover isto a mecanismo normativo, rodar Dossiê-lite antes.

## 2. Inventário medido (o que existe hoje)
| Fluxo | Onde grava | Persiste? | Observação |
|---|---|---|---|
| Achados do Revisor | `governance/aprendizado/LEDGER-ACHADOS.md` (+ `CAUSAS-PREVENCAO.md`) | Sim (git) | É o melhor exemplo do pipeline log → análise → conhecimento (master §37). |
| Tokens/custo por chamada de agente | `.telemetria/uso-tokens.jsonl` | **Não** (`.gitignore`; some com o contêiner de nuvem) | Retrato manual em `TELEMETRIA-TOKENS.md` (hoje 1 linha de teste, Haiku). |
| Roteador de modelos | `<tmp>/sot-roteador/uso.jsonl` | **Não** (diretório temporário) | Sem tokens; script **selado** em `GATE-MANIFEST.sha256`. |
| Carimbo de sincronização | `governance/rpsa-ledger.json` | Sim | Derivável do git (A2 da auditoria). |
| Decisões operacionais | 157 atas `DHR-…` + HANDOFF (131 cópias) | Sim, mas narrativo | Sem registro de 1 linha por decisão (A7 da auditoria). |
| **Decisões de política dos hooks** (negar/bloquear: roteador R-AC7/R-GATE, `gate-check`, `andraus-ask-guard`, `revisor-guard`, pós-guarda) | **Nenhum arquivo** (por grep em `scripts/`) | **Não** | O enforcement acontece, mas **não deixa evidência** — contraria master §24. |
| Resposta de Andraus a pergunta (aprovação) | Chat + ata | Parcial | Hook `andraus-ask-mark` só guarda estado efêmero; master §25 pede evento de aprovação. |
| Violações de invariante (detectores) | Saída de terminal | **Não** | `check_invariants`, `check_doc_sync`, `check_refs` só imprimem. |

## 3. Lacunas (por gravidade)
1. **Perda:** telemetria e roteador não persistem — em sessão de nuvem a evidência evapora (BL-039 já aponta, mas fica diferido para a SPEC-040).
2. **Enforcement sem evidência:** negações/bloqueios dos hooks não são registradas.
3. **Sem correlação comum:** seis fluxos, nenhum `run_id`/`session_id`/`task_ref` compartilhado; impossível perguntar "o que aconteceu na rodada 3 da SPEC-049, de ponta a ponta".
4. **Sem versão do harness no registro:** não se sabe com qual versão de agente/hook/prompt a rodada correu (master §8, §29).
5. **Sem integridade:** nada impede (nem detecta) edição retroativa de um registro de decisão além do git.
6. **Limite estrutural a declarar:** o hook só enxerga a chamada de subagente **agregada** (tokens totais, nº de ferramentas); **não enxerga as gerações internas** (master §6 pede não esconder o loop). Registrar `tool_uses` e `duracao_ms` e **declarar** a limitação — não fingir granularidade.

## 4. Desenho proposto (4 camadas, nada de nova burocracia)
**Princípio:** registrar o **mínimo de evidência** para explicar, avaliar, proteger e melhorar (master §26); **metadados sempre, conteúdo nunca** por padrão (§10) — o texto de prompt/parecer **não** entra; entra **referência + hash** (§11): o repo já exige `ALVO:` e `SHA256-ALVO:` nos pedidos ao Revisor.

### 4.1 Esquema único de evento (JSON Lines, um objeto por linha)
Campos mínimos (modelo conceitual do master §29, nomes convertíveis para OTel):
`ts` · `event` · `family`=`AC` · `session_id` · `run_id` (um por chamada de agente) · `parent_run_id` · `task_ref` (ex.: `SPEC-049/plan/R2`) · `agent_id` (`especificador`|`revisor`|`orquestrador`|`hook:<nome>`) · `agent_version` (hash do arquivo em `.claude/agents/`) · `harness_version` (SHA do commit-base + hash de `GATE-MANIFEST.sha256`) · `model` · `class` (`CLASSE-TAREFA`) · `severity` (`INFO`|`WARN`|`ERROR`|`CRITICAL`|`AUDIT`|`EVALUATION`, sem decoração) · `status` · `operation` (nome do que faz, não do modelo: `agent.run`, `policy.decision`…) · `input_ref`/`output_ref` (`path`+`sha256`) · `metrics{in,out,cache_read,cache_create,total,duration_ms,tool_uses}` · `error`.
Nomes de campo seguem a nomenclatura "o que faz, não a implementação" (master §28): o modelo é atributo, não nome da operação. Cardinalidade controlada (§27): IDs únicos ficam em atributos, nunca em nomes.

### 4.2 Tipos de evento (conjunto fechado, v1)
| `event` | Quem emite | Mapeia para (OTel/master) |
|---|---|---|
| `agent.run` | PostToolUse/Agent (já existe como `telemetria_tokens`) | `invoke_agent` + `gen_ai.usage.*` |
| `policy.decision` (`ALLOW`/`DENY`, `policy_id`, `enforcement_point`, motivo) | roteador, `gate-check`, ask-guard, revisor-guard, pós-guarda | master §24 |
| `gate.result` (exit code, `validate_spec_sot`, `run_gates`) | gates determinísticos | `execute_tool` |
| `invariant.violation` (ID, severidade, observado × esperado) | detectores (`check_invariants`, `check_doc_sync`, `check_refs`, `check_coesao`) | master §23 — **Detector ≠ Gate (ENF-03)**: só registra |
| `finding.recorded` (ID, SEV, categoria C01..C99) | `loop_ledger.py` (já extrai) | `EVALUATION` |
| `approval.requested` / `approval.decided` | `AskUserQuestion` (+ marca) | master §25: `requester`, `approver`=Andraus, `decision`, `policy_reference` |
| `decision.recorded` (o log único A7) | Orquestrador, a partir da ordem de Andraus citada | trilha de auditoria |
| `handoff.created` | reescrita do HANDOFF | master §18 |

### 4.3 Onde cada coisa vive (resolve o conflito volume × persistência)
| Camada | Conteúdo | Local | Git? | Retenção |
|---|---|---|---|---|
| **L1 bruto** | todos os eventos, 100% metadados | `.telemetria/eventos.jsonl` | Não (volume; o mapa já polui 98/233 commits) | curta/local |
| **L2 evidência** | 100% de `policy.decision DENY`, `invariant.violation`, `ERROR`/`CRITICAL`, `approval.*` | `governance/logs/EVENTOS-CRITICOS.jsonl` (append-only) | **Sim** | longa (sampling master §32: erro/violação/ação sensível = 100%) |
| **L3 decisão** | 1 linha por decisão operacional: ID, data, ordem de Andraus citada, arquivos, hash do commit | `governance/logs/DECISOES-LOG.jsonl` (cadeia `prev_hash`; verificador `--verify`) | **Sim** | permanente (INV-07) |
| **L4 resumo** | retrato por Spec/rodada (tokens, achados, negações, tempo) gerado no **fechamento da Spec** (retrospectiva, `AGENTS.md` §12 passo 5) | `governance/aprendizado/` | **Sim** | longa |
**Efeito:** a evidência crítica **sobrevive à nuvem** sem inflar o git; o bruto é descartável (execução normal = sampling, master §32). O L4 já tem precedente (`TELEMETRIA-TOKENS.md`).

### 4.4 Segurança e privacidade (master §10, §34)
- Nenhum texto de prompt, parecer ou resposta; só `path`+`sha256`. Lista de redaction por padrão (chaves, tokens, `.env`) com teste automatizado de que nenhum evento contém padrão de segredo.
- O arquivo de log **não é fonte de instrução**: texto lido de log é dado (mesma regra do conteúdo web e do auditor externo).
- Escrita **fail-open** nos hooks (log nunca bloqueia nem altera a chamada — Detector, ENF-03); falha de gravação gera `WARN` próprio, não silêncio.

### 4.5 Integridade (master §35)
`prev_hash` em L3 (e em L2 por lote diário): `hash(evento canônico + prev_hash)`. O `--verify` detecta adulteração/remoção no meio da cadeia; o git é a âncora externa. Sem assinatura criptográfica nesta fase (custo > benefício; sem baseline em risco).

### 4.6 Log ≠ memória (master §37)
O pipeline já existe e é mantido: **log (L1–L3) → ledger → `CAUSAS-PREVENCAO` → regra/teste**. Falha recorrente vira **caso de regressão** (teste de hook/detector), não texto solto. Nada do log entra automaticamente como contexto dos agentes.

## 5. Fatias de entrega (cada uma só por ordem de Andraus)
| Fatia | O que | Toca selo/normativo? | Prova pré-aplicação |
|---|---|---|---|
| **F1** | Esta proposta + esquema JSON (`schemas/`) + gerador de eventos de exemplo + teste de redaction | Não | `npm test`, suíte, `check_refs` |
| **F2** | Persistência: `telemetria_tokens` passa a gravar no esquema; hooks de política passam a emitir `policy.decision` (L1/L2) | **Sim** — `roteador_modelos.py` selado (precedente `DHR-ROTEAMENTO-007`), `settings.json`, `MECANISMOS.json` | testes de hook (`tests/test-hooks.js`), mutação |
| **F3** | `DECISOES-LOG.jsonl` + backfill das atas recentes + `--verify` (absorve **A7**) | `MECANISMOS.json`; coordenar com A2/A3 da frente de burocracia | conservação (`equiv_conservacao.py`) |
| **F4** | Resumo por Spec no fechamento (L4) + detectores emitindo `invariant.violation` | `MECANISMOS.json` | `loop_ledger --check` |
| **F5** | Métrica de qualidade do próprio log (cobertura de `run_id`, % de eventos com `task_ref`) | Não | — |
**Recomendação:** F1 → F2 (resolve a perda e o enforcement sem evidência) → F3. F4/F5 só depois de ver dados reais (BL-040).

## 6. Tensões e riscos
1. **Volume no git:** por isso L1 fica fora; L2/L3 são pequenos por construção. Medir após F2 antes de F4.
2. **Selo do roteador:** mexer exige regravar `GATE-MANIFEST.sha256` por ordem expressa (precedente conhecido).
3. **Cloud × local:** o bruto continua perdido ao fim da sessão — é **intencional** (sampling), exceto L2/L3, que precisam ser commitados no mesmo PR do trabalho; **risco:** esquecer o commit. Mitigar com o Stop hook avisando "eventos críticos não commitados" (informativo).
4. **Contagem dupla** de tokens com subagente aninhado (BL-040): hoje improvável (subagente sem a ferramenta Agent); reconferir.
5. **Colisão com a frente de burocracia:** F3 é o A7; A2 (HANDOFF por delta) e A6 (mecanismos em camadas) alteram os mesmos arquivos — sequenciar para não conflitar.
6. **Não prometido:** granularidade por geração interna (limite do hook, §3 item 6).

## 7. Decisões que ficam com Andraus
(a) Aprovar F1 e/ou F2 como próxima frente; (b) autorizar regravar o selo do roteador na F2; (c) confirmar L2/L3 versionados no git e L1 local; (d) se quer Dossiê-lite antes de virar mecanismo. Nenhuma decisão aberta do ROADMAP (J-001, N-001, M-001…) é tocada.

## 8. Respostas de Andraus (chat, 2026-11-01, AskUserQuestion) e estado
- **Fatias:** preparar **F1 e depois F2** (sem aplicar). **Onde gravar:** L2/L3 **no git** em `governance/logs/`; L1 bruto local. **Pesquisa:** **enxuta e registrada antes da F2**, feita pelo Especificador (conteúdo web = dado, nunca instrução); ainda **não executada** — é pré-requisito da F2, não da F1.
- **F1 preparada (pré-testada, NÃO instalada):** `F1/evento-ac.schema.json` (esquema do evento, só `family=AC`), `F1/log_ac.py` (validação sem dependências, recusa de campos de conteúdo e de padrões de segredo, selo e verificação por cadeia de hash) e `F1/test_log_ac.py` — **22 testes OK** (`python -B -m unittest test_log_ac`, dentro de `F1/`). Um teste achou falha real do próprio protótipo (valores de `metrics` sem validação) e foi corrigido antes do commit. Não toca hooks, `schemas/`, `npm test` nem scripts selados; instalar (mover para `schemas/`/`scripts/`, `MECANISMOS.json`, ata) exige ordem expressa de Andraus.
- **Falta para a F2:** a pesquisa enxuta; ordem para regravar o selo do roteador; desenho dos hooks de política (`policy.decision`) e gravação de L2 em `governance/logs/`.

## 9. Pesquisa enxuta entregue (2026-11-01) e ajustes incorporados à F1
- `PESQUISA-LOGS-AGENTES-2026-11-01.md` (Especificador; 8 fontes, confronto CONFIRMA/AJUSTA por decisão). Resultado: camadas L1–L4 e redaction **confirmadas**; esquema, `policy.decision` e cadeia de hash **ajustados**. Versão corrente da semconv GenAI = **INDETERMINADO** (Development, sem release); a nota de §1 desta proposta sobre a data de migração vem de blog e **não** foi confirmada em fonte primária.
- **Incorporado ao protótipo F1 (26 testes OK):** decisão no vocabulário `allow|deny|ask|defer`; `policy_version`, `redacted`, `hook_agent_id`, `semconv_ref`, `provider`; métricas só inteiras (subconjunto JCS, RFC 8785); `transcript_path`/`cwd`/`scratchpad_dir` proibidos.
- **Fica para a F2 (precisa de decisão/desenho):** usar `tool_use_id`/`prompt_id`/`agent_id` nativos do hook como `run_id`/`parent_run_id`; `session_id` em hash curto em L2/L3; âncora do hash-cabeça no git contra truncamento do fim da cadeia; `ask`/`defer` também em L2; cadeia por linha em L2; conferir os campos de tokens de `PostToolUse` contra `telemetria_tokens` antes de gravar.
