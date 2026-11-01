> Transcrição integral pelo Orquestrador do relatório do Revisor SOT (`CLASSE-TAREFA: S2`, `model: sonnet`), recuperada do arquivo do subagente após o reinício do contêiner (o resultado não chegou por mensagem). Veredito do Revisor: **NÃO CONFORME — 0 Críticos, 1 Média (D01), 7 Menores (D02–D08)**. Nada homologado. **D06** (mecânico) aplicado pelo Orquestrador. Decisões de Andraus registradas depois (AskUserQuestion, 2026-11-01): bloqueios e negações **no git** (camada permanente); troca de ramo = **nome da sessão + nome do ramo**.

# PARECER DO REVISOR — Logs dos Construtores — R4 — 2026-11-01

Alvo: `governance/propostas/LOGS-CONSTRUTORES/PROPOSTA-LOGS-CONSTRUTORES-2026-11-01.md` (MEDIUM, proposta de processo; acréscimos em §4.2/§4.3/§4.4/§14) e `PLANO-F2-2026-11-01.md` (revisão R4).
MODO: delta (rodada 4). SHA256-ALVO: c67b376079ee9e61fb894040d0b8648aab6915966ec3b56b417b35cfbe8deab1.
VEREDITO D: PASSOU_D (via GATE-D do Orquestrador, sha256 conferido contra o pedido, rodada com `--rapido`).
Sem Bash: não reexecutei testes nem mutações. Conferi só por leitura.

**Veredito: NÃO CONFORME — 0 Críticos, 1 Média (D01), 7 Menores (D02–D08).**
Nada homologado. Nenhuma decisão aberta do ROADMAP foi fechada (CONS-01).

## 1. Fechamento de C01–C07 (R3)
| Achado R3 | Situação R4 | Prova (arquivo:linha) |
|---|---|---|
| C01 (descrição da F1 desatualizada) | **Fechado.** Todos os fatos de código do plano conferem com o `log_ac.py` corrente. | Ver tabela de conferência abaixo. `evento-ac.schema.json:2` tem `$id`, e `:130` tem `block` no enum. |
| C02 (destino de `block` e `exit 2`) | **Parcial.** A tabela §3.7 existe e as linhas dos hooks conferem. Resta D01 (Média) e D02. | Ver §3 abaixo. |
| C03 (contagens) | **Fechado no plano.** Contei 66 `def test_` em `F1/test_log_ac.py` e 40 em `tests/test_roteador_modelos.py`. Os 49 do `MECANISMOS.json:37` seguem corretamente como NÃO MEDIDO. Resta resíduo na PROPOSTA (D06). | |
| C04 (encadeamento entre ramos) | **Fechado com resíduo.** Raiz válida (plano §1 regra 1), `continua_de` na âncora só quando a 1ª linha o tem, precedência única no cabeçalho, `.git` como arquivo. Resta D05. | `log_ac.py:44` testa só `exists()`. |
| C05 (import engolido, pior caso, cauda corrompida) | **Fechado.** WARN no `except` do import com teste e mutação, pior caso declarado e NÃO MEDIDO, procedimento §11.1. | Contas conferidas abaixo. Resta citação imprecisa (D04). |
| C06 (limites da camada, `sem-ata`, `verify`) | **Fechado.** Código e limites declarados. | `log_ac.py:52,55,57,132-133,263-264,269,270,301-302`. |
| C07 (decisões de Andraus) | **Fechado.** Plano §11.3 e PROPOSTA §14 registram data e fonte e declaram que a forma exata do chat é NÃO VERIFICADA. | |

## 2. Achados novos

**D01 — MÉDIA — a emissão em L2 pelos hooks JS não é representável com o que o plano declara (M3).**
- Constatação:
  - O plano §3.7 manda `gate-check.js` gravar `deny` em L2 no `exit 2`.
  - `valida` recusa `session_id` em claro em L2 (`log_ac.py:136`).
  - `gate-check.js` lê o payload só por `readToolInput()` (`gate-check.js:9`). Essa função devolve apenas `payload.tool_input || payload` (`hook-io.js:28`), então o `session_id` é descartado. O mesmo vale para `post-edit-check.js:8`.
  - A CLI `emit` não calcula `hash_sessao` nem chama `completa_ids` (`log_ac.py:291-298`). O JS teria de calcular `"h:" + sha256(sid)[:12]` sozinho.
  - O plano não diz quem faz isso. Também não lista `scripts/hook-io.js` entre os arquivos que mudam (§2, linhas 1–40 da tabela).
  - Sem `session_id`, `completa_ids` cai em `"sem-sessao"` (`log_ac.py:157`). Todos os `deny` do `gate-check` iriam para o mesmo segmento `hash_sessao("sem-sessao")` em todas as sessões e ramos. Isso recria o conflito add/add que a decisão "um arquivo por sessão" quer evitar.
  - O plano §10.2 verifica `session_id` só em `andraus-ask-mark.js`, `andraus-ask-guard.js` e `telemetria_tokens.py`. `gate-check.js` não aparece.
- Fonte: `scripts/hook-io.js:23-41`, `scripts/gate-check.js:9`, `log_ac.py:136,157,291-298`, plano §2, §3.3, §3.7, §10.2.
- Ação:
  - Declarar como `gate-check.js` obtém o `session_id`. Ou `hook-io.js` passa a expor o payload inteiro, e então entra na tabela §2 como arquivo que muda. Ou o `gate-check` não grava L2.
  - Declarar quem faz o hash (JS ou opção nova da CLI).
  - Acrescentar um teste: sem `session_id`, o `gate-check` não escreve em L2 compartilhado.
- Condição para nova revisão: a tabela §2 e a §3.7 concordam sobre quais arquivos mudam e de onde vem a sessão em hash em cada hook JS.

**D02 — MENOR — `post-edit-check.js` omitido da §3.7.**
- Ele é hook de `settings.json:29-31` (PostToolUse `Write|Edit|MultiEdit`) e sai com `process.exit(BLOCK)` em `post-edit-check.js:20`.
- A regra da §3.7 diz "`exit 2` vai a L2". Mas em PostToolUse a ferramenta já rodou, então `deny` e `block` não descrevem o efeito.
- A condição (b) do R3 era "por hook". Declarar a linha ou excluir o hook explicitamente.

**D03 — MENOR — `andraus-ask-guard` mistura três causas de `block`.**
- Ele emite `decision: 'block'` por três caminhos: `decidir`, `decidirPergunta` e `decidirMerge` (`andraus-ask-guard.js:177-178,184`).
- O terceiro é um AVISO de que o merge é possível (`andraus-ask-guard.js:158-163`), não bloqueio de política.
- O plano §2 (nota) fixa um `policy_id` por hook, então o aviso e o enforcement caem na mesma linha de L2.
- Distinguir o `policy_id` por caminho, ou registrar o aviso só em L1.

**D04 — MENOR — citações imprecisas.**
- Plano §1 regra 1 cita "`prev = continua_de`" em `:262`. O texto real é `probs, prev, ult, n = [], continua_de, None, 0`.
- Plano §4 e §11.1 atribuem a `json.loads(ult)` em `:223` a cauda "não UTF-8". O `UnicodeDecodeError` nasce em `.decode("utf-8")` em `:197`, dentro de `_ultima_linha` (chamada em `:222`). Só a cauda não-JSON nasce em `:223`.
- O efeito descrito (uma `ValueError` depois da trava) está correto. Só a âncora de linha está errada.

**D05 — MENOR — segmento encadeado e ainda sem âncora falha no `verify`.**
- Um segmento criado depois da última âncora, com 1ª linha de `prev_hash` não nulo (troca de ramo com predecessor visível, ou `-r<k>` de recuperação), é verificado como raiz. `log_ac.py:271` acusa "prev_hash não confere" com `prev = None`.
- O plano §1 regra 5 diz "segmento ausente da âncora = só integridade interna" e §5.2(c) deriva o `continua_de` da âncora. O CI informativo do `verify` daria falso alarme.
- Declarar o resultado do `verify` para esse caso: um estado "continuidade não verificada", distinto de "problema".

**D06 — MENOR, mecânico — PROPOSTA l.110 e l.115 apontam para §12 (61 testes) quando o certo é §14 (66).**
Vai na FICHA-M. Os dois textos antigos aparecem uma vez cada.

**D07 — MENOR — BL-036 sem disposição.**
- Abri BL-036..042 (`RMR-001_Painel_Backlog.md:143-149`) e BL-034 (`:141`). O plano §10.4 dispõe só BL-039 (decidido pelo Andraus: PARCIAL, só construtores) e BL-040.
- BL-036 manda propor o "esquema de coleta (base OpenTelemetry GenAI)" e o piloto nos Construtores, sob ordem de Andraus (`:143`). `agent.run` com `metrics` é exatamente isso.
- Registrar a disposição de BL-036 (referência, parcial ou pré-empção declarada) e que BL-037, BL-041 e BL-042 não são tocados. BL-038 já está coberto pelo campo `family` (PROPOSTA §0).

**D08 — MENOR — observabilidade do roteador.**
- Nos dois casos abaixo o roteador devolve 0 sem evento: exceção dentro do `try` (`roteador_modelos.py:459-460`) e `tool_name` fora de escopo (`:451-452`).
- O plano §3.1 item 3 diz "L1 recebe toda decisão", mas uma falha de `decidir()` (um fail-open) não deixa rastro. A pergunta "se o ENTÃO nunca ocorresse, detectaríamos?" tem resposta "não" para esse caminho.
- Declarar como limite, ou emitir um WARN mínimo também nesse `except`.

## 3. Pontos pedidos

### Tabela §3.7: evento, `decision`, exit e timeout por linha
Abri cada arquivo e o `settings.json`. As citações de linha conferem, exceto onde o item diz o contrário.

| Linha | Confere? |
|---|---|
| roteador | Sim. `settings.json:14-19` (matcher, comando e `timeout` 15 em `:19`). `roteador_modelos.py:461-463` imprime `deny` e `:464` devolve 0. `roteador-modelos.js:15` sai 0. |
| gate-check | Sim. `settings.json:5-9` (sem `timeout`). `gate-check.js:12,17,20` saem cedo. `:50` faz `exit(BLOCK)`. `hook-io.js:13` define `BLOCK = 2`. A âncora `gate-check.js:3` diz apenas "Bloqueia com exit 2", o que basta para PreToolUse. |
| ask-guard | Sim. `settings.json:89-90` (`timeout` 40). `andraus-ask-guard.js:173` (saídas antecipadas), `:184` (`block`), `:187` (exit 0). Ver D03. |
| ask-mark | Sim. `settings.json:55-59`. `andraus-ask-mark.js:30,32`. |
| revisor-guard | Sim. `settings.json:121-126` (`timeout` 120). `revisor_guard.py:198-199`. `revisor-guard.js:14`. |
| posguarda | Sim. `settings.json:94-95` (`timeout` 120). `revisor_posguarda.py:95-96`. `revisor-posguarda.js:14-15`. |
| handoff-hook | Sim. `settings.json:80-81` (`timeout` 30). `handoff-hook.js:76` só imprime e sai 0. |
| map-sync | Sim. `settings.json:70` (`timeout` 120). `map-sync.js:96`. |
| doc-sync-check | Sim. `settings.json:75` (`timeout` 60). `doc-sync-check.js:69`. |

Omissão: `post-edit-check.js` (D02).

### "`block` e `exit 2` vão a L2": coerência com ENF-03 e com a latência
- **ENF-03 (`atomic-spec.md:95,269`):** é coerente. O log só registra e nunca decide.
  - A emissão acontece depois de fixada a decisão, com `emite_seguro` que nunca levanta (`log_ac.py:247`).
  - O WARN vai para arquivo e não para `stderr` (`log_ac.py:250-253`). Isso respeita o `stderr` que vira mensagem ao modelo em `revisor-guard.js:14` e `gate-check.js:48-50`.
  - A coluna `enforcement_point` com `"<hook>:exit2"` preserva a distinção entre `deny` e `block`.
  - Deixar bloqueios só em L1 (descartável) manteria a lacuna 2 da PROPOSTA §3.
- **Condição:** a recomendação só é implementável com D01 resolvido (sessão em hash nos hooks JS) e sem misturar o aviso de merge em L2 (D03).
- **Latência:** as contas do plano conferem.
  - A trava espera ≤1 s (`log_ac.py:33,203-208`). Um `TimeoutError` não é `ValueError`, então não há retry nesse caso.
  - O retry por `ValueError` depois da trava custa mais uma espera (`:245-246`). O teto é ≤2 s por emissão e ≤4 s com as 2 emissões do roteador.
  - O `fsync` (`:230`) não tem teto. O pior caso não é limitado pelo código, e o plano declara isso e o marca NÃO MEDIDO.
  - O deny já impresso se perde se o conjunto passar de 15 s, porque o wrapper só repassa o `stdout` ao fim (`roteador-modelos.js:11,14`). O plano declara isso (§4).
  - O `spawnSync` de 3 s do helper `log-ac.js` pode matar o processo no meio do `os.write` (`:229`). O plano reconhece e trata em §11.1.
  - Para as linhas L2 do `gate-check` e do `post-edit-check`, o timeout padrão da ferramenta segue NÃO VERIFICADO (`settings.json` sem `timeout`). O plano declara isso (§4).

## 4. Conferência por amostra independente
Afirmação, fonte aberta, resultado. Tudo confere:

| Afirmação | Fonte | Resultado |
|---|---|---|
| 66 testes na F1 | `test_log_ac.py` (contagem de `def test_`) | Confere |
| 40 `def test_` em `test_roteador_modelos.py` × 49 no `MECANISMOS.json:37` | Contagem direta | Confere. Qual valor vale segue NÃO MEDIDO, como o plano declara. |
| `emit` sai 0 sem `<json>` | `log_ac.py:288-290` | Confere |
| WARN com carimbo UTC | `log_ac.py:248` | Confere |
| `canal_warn` `"arquivo"` e `"stderr"` | `log_ac.py:250-253` | Confere |
| `verify` sai 2 em `--ancora` malformado | `log_ac.py:301-302` | Confere |
| `LOCK_PRAZO = 1.0` | `log_ac.py:33` | Confere |
| Esquema carregado no import | `log_ac.py:18-23` | Confere |
| Camada derivada do caminho | `log_ac.py:52-59` | Confere |
| `sem-ata` exige `task_ref` | `log_ac.py:132-133` | Confere |
| `_RE_ATA` | `log_ac.py:35` | Confere |
| `validate-schemas.js` valida todo `.json` de `schemas/` | `tests/validate-schemas.js:20` | Confere |
| `.telemetria/` ignorado, `governance/logs/` não | `.gitignore:44` | Confere |
| BL-039 e BL-040 (texto e gatilhos) | `RMR-001_Painel_Backlog.md:146-147` | Confere |
| `block` no enum | `evento-ac.schema.json:130` | Confere |

Amostra anti-leniência (≥5 blocos inalterados): §6 (provas), §5 (passos de processo), §3.4 (`approval.*`), §3.6, §1 "Limite honesto", e PROPOSTA §4.5 e §6. Sem achado novo, salvo as citações já registradas em D04.

## 5. Passo 0 e passos eliminatórios
- **Passo 0:**
  - ROADMAP §18 lido (`ROADMAP.md:363-371`, SPEC-040/041 como slots indicativos, ref. não-normativa).
  - `atomic-spec.md`: ENF-03 em `:95,269`, INV-04 em `:404`, INV-07 em `:407`.
  - `RMR-001`: nenhum item ATIVADO ligado a esta frente. BL-003 e BL-011 estão ATIVADOS por `spec:SPEC-006` (`:110,118`), sem relação.
  - **Não verificado:** `governance/RULES.md` só confirmei que existe e é legível (contagem de cabeçalhos). Não li o conteúdo, e esta proposta não cita RULE nova.
- **Passo 2 (invariantes):** PASS. Custo fora do Conviction Vector (INV-04), SOT não executa ordem, versionamento monotônico (INV-07). O texto preserva o histórico.
- **Passo 3 (CC):** o artefato é uma proposta de processo, não uma Spec, então o CC-01..CC-12 integral não se aplica.
- **Passo 7 (ENF-01..08):** o log não decide (ENF-03), WARN fail-open, sem auto-aprendizado de policy. A fronteira E3 não é tocada.
- **Passo 8 (decisões):** nenhuma decisão aberta do ROADMAP foi fechada. As decisões (b), (c), (j) e (k-BL-039) são internas à proposta, e as demais seguem pendentes (a, d–i, l, m), tratadas como pendentes.

## 6. Limites desta revisão
- Sem Bash: a execução verde dos testes e as mutações informadas pelo Orquestrador não foram reexecutadas por mim.
- `git worktree` e o comportamento de `.git` como arquivo: o plano marca INFERÊNCIA e eu não pude testar.
- Latência (p50/p95, `fsync` em nuvem) e volume de L2: NÃO MEDIDO, como o plano declara.

<!-- ACHADOS-ESTRUTURADOS
D01|MEDIA|C01|a emissao em L2 por hooks JS nao e representavel: gate-check nao tem session_id porque hook-io readToolInput descarta o payload, e a CLI emit nao faz hash_sessao nem completa_ids; hook-io.js nao esta na tabela de arquivos que mudam; sem sessao cai em sem-sessao e recria conflito add/add|conferir, para cada linha que grava L2, de onde vem o session_id em hash e quem o calcula, e cruzar a tabela de arquivos que mudam com a tabela hook x camada
D02|MENOR|C01|post-edit-check.js sai com exit 2 em PostToolUse e nao esta na tabela 3.7 embora a regra diga exit 2 vai a L2|enumerar todos os hooks de settings.json com exit 2 ou decision antes de declarar a tabela completa
D03|MENOR|C05|andraus-ask-guard emite block por tres caminhos e um deles e aviso de merge nao enforcement mas ha um policy_id fixo por hook|policy_id por caminho de decisao ou aviso so em L1
D04|MENOR|C07|citacoes de linha imprecisas: prev igual a continua_de nao e o texto literal de log_ac.py l.262 e o erro de UTF-8 nasce em l.197 e nao em l.223|citar o trecho literal e a linha onde a excecao nasce
D05|MENOR|C10|segmento encadeado ainda sem ancora e verificado como raiz e acusa prev_hash nao confere em log_ac.py l.271 contra a regra de so integridade interna|declarar o estado continuidade nao verificada distinto de problema no verify de pasta
D06|MENOR|C06|PROPOSTA l.110 e l.115 apontam para 12 onde o numero atual 66 esta em 14|buscar por texto hoje N ao mudar a contagem
D07|MENOR|C08|BL-036 manda propor o esquema de coleta e o piloto nos Construtores e o plano 10.4 so dispoe BL-039 e BL-040|listar todos os BL vinculados com disposicao e motivo mesmo em proposta
D08|MENOR|C05|excecao dentro do try do roteador e tool_name fora de escopo saem com 0 sem evento portanto toda decisao em L1 nao cobre o fail-open|declarar o limite ou WARN minimo no except
-->

<!-- FICHA-M {"achados":[{"id":"D06","sev":"MENOR","arquivo":"governance/propostas/LOGS-CONSTRUTORES/PROPOSTA-LOGS-CONSTRUTORES-2026-11-01.md","antigo":"hoje 66, ver §12","novo":"hoje 66, ver §14","condicao":"troca de referencia de secao; §12 traz 61 e a contagem atual 66 esta em §14"},{"id":"D06b","sev":"MENOR","arquivo":"governance/propostas/LOGS-CONSTRUTORES/PROPOSTA-LOGS-CONSTRUTORES-2026-11-01.md","antigo":"hoje 66, §12","novo":"hoje 66, §14","condicao":"troca de referencia de secao; §12 traz 61 e a contagem atual 66 esta em §14"}]} -->

## 7. Veredito
**NÃO CONFORME.**
- A Média D01 volta ao Especificador.
- Preferir também D02, D03 e D05.
- Os demais Menores não bloqueiam.
- D06 vai ao Orquestrador pela FICHA-M.

Condição para a próxima revisão (delta):
- D01: a tabela §2 e a §3.7 concordam sobre os arquivos que mudam e a origem do `session_id` em hash em cada hook JS.
- Incluir `post-edit-check.js` na §3.7 ou excluí-lo expressamente.

## 8. Encaminhamento
Devolver ao Especificador (classe O, `PARECER:` + `FICHA:` classificando D01–D08). O Orquestrador aplica D06 pela FICHA-M. Nada vai à homologação do Andraus ainda.