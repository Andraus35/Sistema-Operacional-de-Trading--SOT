# DHR-LOGS-AC-001 — Ata de Decisão — Log estruturado dos agentes Construtores (AC), F2a: módulo, roteador e telemetria

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Revisor SOT / Controlador |
| Ref | Respostas de Andraus no chat (AskUserQuestion), 2026-11-01: "Autorizar a F2 já"; "Um arquivo por sessão"; "Sim, acrescentar bloquear"; "Guardar no git" (bloqueios e negações); "Nome da sessão mais nome do ramo"; "Ao lado do módulo, na pasta de scripts"; "Parcial, só construtores" (BL-039) · `governance/propostas/LOGS-CONSTRUTORES/` (proposta, pesquisa, plano F2, pareceres R1–R4 do Revisor, F1 pré-testada) |
| Data | 2026-11-01 |
| Status | **DECISÃO REGISTRADA** (decisão direta de Andraus em chat; AGENTS.md §10). Aditiva (INV-07); reversível por `git revert` + `gate_manifest.py --write`. |
| Compatibilidade | Patch (novo módulo; altera o roteador e a telemetria sem mudar nenhuma decisão de política). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Não altera texto de agente de construção nem método; altera script selado (roteador) com regravação do selo por ordem expressa. |

## 1. Decisão `[FATO]`
Aplicar a **F2a** da proposta de logs dos Construtores (fatia segura do plano F2; a F2b fica para depois, ver §3):
1. `scripts/log_ac.py` + `scripts/evento-ac.schema.json` (de `F1/`): esquema de evento só da família **AC**, validação sem dependências, recusa de campos de conteúdo e de padrões de segredo, cadeia de hash com anexo atômico e trava com prazo, camada **forçada pelo caminho** (`governance/logs/L2|L3`), `emite_seguro` que **nunca levanta**, `nome_segmento` = `<hex12 da sessão>-<r8 do ramo>`.
2. `scripts/roteador_modelos.py` (**selado**; selo regravado nesta ata): depois de a decisão estar impressa e fora do `try` da decisão, emite `policy.decision` — **L1** (`.telemetria/eventos.jsonl`, local) para toda decisão; **L2** (`governance/logs/L2/<sessão>-<ramo>.jsonl`, **no git**) para `deny`, **sem texto livre** e com a sessão em hash curto. Falha do módulo = WARN mínimo em `.telemetria/log-ac-falhas.log`, **nunca** muda a decisão.
3. `scripts/telemetria_tokens.py`: emite `agent.run` (L1) no mesmo esquema e registra em `.telemetria/payload-forma.jsonl` **só os nomes das chaves** do payload real (insumo da pendência B05); a telemetria legada fica intacta.
4. Testes: `tests/test_log_ac.py` (68), `tests/test_roteador_log_ac.py` (6), `tests/test_telemetria_log_ac.py` (6); `MECANISMOS.json`; selo (`gate_manifest.py --write`).

## 2. Ressalvas `[FATO]`
- **Detector (ENF-03):** o log registra e nunca decide. A cadeia de hash prova **integridade, não autoria**; o varredor de segredos é Detector com falsos negativos conhecidos; truncamento do fim só é detectado com o hash-cabeça ancorado.
- **Custo** fora do Conviction Vector (INV-04). Só família AC; os agentes de Trading ficam com SPEC-040/041/042 e BL-034/038. BL-039 absorvido **parcialmente** (só construtores); o painel do backlog **não** foi alterado.
- Nenhuma decisão aberta do ROADMAP foi fechada (CONS-01). `AGENTS.md` **não** foi alterado.
- **Parecer do Revisor:** a proposta e o plano terminaram a R4 como **NÃO CONFORME** (0 Críticos; Médios 10→6→2→1); o resíduo é a F2b (hooks JS). Esta ata aplica só a F2a, cujos pontos de risco (isolamento do log, trava com prazo, camada pelo caminho, sessão em hash) foram os que o Revisor atacou e não conseguiu quebrar no código.
- **Medido (2026-11-01):** roteador ≈ 46 ms/chamada antes da F2a (p95 **não medido** depois); suíte completa **504 testes OK** (424 anteriores + 80 novos), `test-hooks.js`, `test-ask-guard.js` e `npm test` (11 schemas) OK; mutações pegas (log dentro do `try` da decisão; `except` do bloco de log estreitado; trava bloqueante; leitura por `splitlines`; camada pelo chamador; separador de linha final).
- **Validação ao vivo (2026-11-01, sessão de nuvem):** uma chamada ao Revisor sem `model` foi **negada** (R-AC7) e gerou `policy.decision`/`deny` em L1 e em L2 (`session_id` em hash `h:…`, `reason` nulo, `prev_hash` nulo = segmento-raiz, `log_ac.py verify` = cadeia íntegra); uma chamada permitida (Explore/sonnet) gerou `policy.decision`/`allow` e `agent.run` em L1.
- **Forma real do payload (B05, só nomes de chaves, PostToolUse/Agent):** `cwd, duration_ms, effort, hook_event_name, permission_mode, prompt_id, scratchpad_dir, session_id, tool_input, tool_name, tool_response, tool_use_id, transcript_path`. Logo `tool_use_id`, `prompt_id` e `session_id` **existem**; `agent_id` **não** vem nesse evento (o fallback `completa_ids` usa `subagent_type`). Insumo para a F2b; o payload de `Stop` e dos hooks JS ainda **não** foi capturado.
- **Testes não poluem o log real:** achado e corrigido no fechamento (o teste do `canal_warn` apagava `LOG_AC_FALHAS`).

## 3. Pendente (F2b — NÃO feito, não tratado como resolvido)
Emissão pelos hooks JS (`gate-check`, `andraus-ask-guard`, `andraus-ask-mark`, `revisor-guard`, pós-guarda, `post-edit-check`): bloqueada por **D01** (`hook-io.js` descarta o payload; sem `session_id` os eventos cairiam em `sem-sessao`); percorredor de pasta do `verify` e leitura de âncora; regra do segmento `-r<k>` de recuperação; estado "continuidade não verificada" (D05); disposição de BL-036 (D07); `policy_id` por caminho no ask-guard (D03). Hook de depuração em `settings.json` **não** foi criado: a forma do payload é capturada pela telemetria (só nomes de chaves).

## 4. Registro
- [x] Esta ata · [x] módulo + esquema + testes · [x] roteador (selo regravado) · [x] telemetria · [x] `MECANISMOS.json` · [ ] merge (mescla só por ordem de Andraus)
