# RETROSPECTIVAS DE FECHAMENTO DO LOOP DOS CONSTRUTORES (LOOP-001 / DHR-LOOP-001)

> **Regra (ordem de Andraus, 2026-10-24):** o tratamento de melhoria — **individual** (Especificador, Revisor, Orquestrador) e **coletivo** (o loop entre eles) — ocorre **ao fim do trabalho completo de uma Spec e ANTES de abrir outra Spec** (Dossiê/abertura/Plan). A coleta de dados (ledger, causas, prevenção) é contínua; o **tratamento** é aqui. Append-only (INV-07). O Orquestrador roda `python scripts/loop_ledger.py --retro-check SPEC-nnn` de cada Spec fechada antes de abrir outra; sem `FEITA`, não abre (salvo dispensa expressa de Andraus).

Linha-índice (lida pelo script; Estado `FEITA` só quando a seção correspondente abaixo estiver completa): `| SPEC-nnn | resumo | data | FEITA |`

| Spec | Escopo | Data | Estado |
|---|---|---|---|
| SPEC-007 | Plan reduzido homologado (DHR-SPEC007-005); 6 rodadas de Plan + 3 de abertura | 2026-10-25 | FEITA |
| SPEC-048 | Abertura (DHR-SPEC048-001) e Plan v1.4 (DHR-SPEC048-002) homologados; 2 rodadas de abertura + 5 de Plan | 2026-10-25 | FEITA |

## Roteiro de cada retrospectiva (checklist; todo item exige evidência do ledger ou do parecer)
1. **Dados:** rodar `loop_ledger.py`; copiar Médias por rodada, rodadas até 0 Média, categorias recorrentes e lacunas de prevenção da Spec; % de achados resolvidos por classe M (economia de rodada).
2. **Individual — Especificador:** padrões de erro próprios (categorias C01..C10), o que o fez reincidir, o que teria evitado (instrução de serviço, checklist, gate).
3. **Individual — Revisor:** severidades desalinhadas, achados reabertos de decisão já tomada, o que não pôde verificar (gate, git, web), tempo/rodadas.
4. **Individual — Orquestrador:** o que escapou aos gates e foi achado tarde, classe M não usada, estados perdidos entre sessões, ordens ambíguas.
5. **Coletivo — o loop:** nº de rodadas, cascatas de correção, handoffs entre agentes, custo evitável (4Es: Conformidade > Eficácia > Efetividade > Eficiência > Economicidade).
6. **Propostas de melhoria** (gates/processo/instruções), cada uma com: problema → evidência → proposta → 4Es afetados → custo; **só viram mecanismo por ordem expressa de Andraus** (com `governance/MECANISMOS.json`). Registrar a decisão dele (aprovada/adiada/rejeitada).
7. Atualizar `CAUSAS-PREVENCAO.md` e marcar a linha-índice como `FEITA` com a data.

<!-- Entradas de retrospectiva abaixo (uma seção por Spec), append-only -->

### Nota de desvio — Orquestrador (individual), 2026-10-25 (insumo da retrospectiva da SPEC-048)
O Orquestrador aplicou 6 correções de Menores do parecer R3 do Plan da SPEC-048 pela classe M (ficha `FICHA-M-PLAN-R3.json`), contra a regra que Andraus explicitou em 2026-10-25 ("achados menores não são corrigidos pelo orquestrador", `DHR-ROTEAMENTO-005`). Causa: leitura extensiva da classe M da `DHR-ROTEAMENTO-003` e do passo 0 criado por mim em `DHR-LOOP-001` sem perguntar o alcance. Prevenção: classe M só para falhas do próprio Orquestrador/gates; alinhar o código do roteador (proposta em `DHR-ROTEAMENTO-005` §3). Categoria: C08 (escopo/alcance da regra).


### Retratação da "Nota de desvio" acima — Orquestrador, 2026-10-25 (append-only, INV-07)
A nota anterior está **incorreta**: Andraus esclareceu que quis dizer o oposto ("os achados menores devem ser identificados e corrigidos deterministicamente pelo orquestrador", `DHR-ROTEAMENTO-006`). As 6 correções da R3 estavam conformes. O erro real foi meu: interpretei uma frase ambígua como proibição sem confirmar o alcance e deixei o mecanismo determinístico faltando (existia só `classificar/conferir`). Prevenção: `scripts/aplicar_ficha_m.py` + bloco `FICHA-M` no parecer. Categoria: C02 (ambiguidade).


## Retrospectiva SPEC-007 (reduzida: formação + selo) — Orquestrador, 2026-10-25
**1. Dados (ledger).** Abertura: 3 rodadas, 0 Média. Plan: Médias 9→5→5→2→1→0 em 6 rodadas (R6 CONFORME condicional, 4 Menores). Recorrentes: C07 citação/âncora, C01 contradição interna, C05 observabilidade; lacunas de prevenção abertas: C99, C01, C06, C10 (ver `CAUSAS-PREVENCAO.md`). Classe M: não usada nesta Spec (a regra nasceu depois); 0%.
**2. Especificador.** Reincide em C01 (mesmo fato em 5–7 lugares) e C07 (âncora por linha). Evitaria: tabela de rastreio fato→locais antes de entregar; âncora por ID, não por linha.
**3. Revisor.** Plan R1–R3 reportou 5–9 Médias por rodada sem delta real (versão intermediária não commitada → revisão integral). Não conseguiu verificar o Benchmark (AUSENTE) nem git (sem Bash). Sem reabertura de decisão homologada.
**4. Orquestrador.** Escaparam aos gates e foram achados tarde: contagem "N BASpecs" em anexo histórico (teste de calibração), placeholder de ata quebrando `check_refs`. Estado perdido entre sessões: SPEC-047 reservado e usado errado na abertura.
**5. Coletivo.** 6 rodadas de Plan é custo alto; cascata principal = divisão (Opção C) mudou o escopo no meio do Plan. Economicidade: INDETERMINADO (tokens não medidos).
**6. Propostas** (só Andraus; nenhuma aplicada): P1 commitar cada versão do Plan para o Revisor revisar por delta; P2 tabela fato→locais exigida na ordem de serviço do Especificador (C01); P3 âncora por ID+hash (G-H do relatório); P4 histórico em arquivo à parte (C06). **Decisão de Andraus: pendente.**

## Retrospectiva SPEC-048 (RAG Retrieval & Evidence Packet Harness) — Orquestrador, 2026-10-25
**1. Dados.** Abertura: 2 rodadas, 0 Média (10→7 Menores). Plan: Médias 3→1→0→0→0 em 5 rodadas; Menores 14→5→3→2→0 (R5 sem achados). Classe M: 6 Menores da R3 + correções de R4 aplicadas pelo Orquestrador por ficha (ROTEAMENTO-006); desvio de alcance retratado (ver notas acima).
**2. Especificador.** Convergência rápida (0 Média em R3) graças ao aprendizado da SPEC-007; resíduo em C07/C02 (precedência R1/R2/R3 no reenvio, vocabulário).
**3. Revisor.** Entregou FICHA-M só a partir de R4; severidades estáveis. Limite: citações `inteligencia-sot@0abd22e` não conferidas (repo ausente), registrado em adendo.
**4. Orquestrador.** Erro próprio: li "achados menores não são corrigidos pelo orquestrador" como proibição (DHR-ROTEAMENTO-005) quando era o oposto (006); faltava mecanismo determinístico até `aplicar_ficha_m.py`. Prevenção: confirmar alcance de ordem ambígua antes de registrar.
**5. Coletivo.** 5 rodadas de Plan vs 6 da SPEC-007: ganho de Eficiência. Merge via PR #130 concluído com CI verde.
**6. Propostas** (só Andraus): P5 exigir bloco FICHA-M desde a R1 do pedido de parecer; P6 conferir ordem ambígua do usuário por pergunta curta antes de gravar DHR; P1–P4 acima também valem. **Decisão de Andraus: pendente.**

### Verificação de conduta do Orquestrador (a pedido de Andraus, chat 2026-10-30) — Orquestrador, 2026-10-30 (append-only)
Pergunta de Andraus: o Orquestrador está **corrigindo de fato os achados Menores** e **alternando modelos segundo a tarefa**? Evidência da errata SPEC-006 v1.13 (R1–R4) e de `<tmp>/sot-roteador/uso.jsonl` (12 invocações):
1. **Menores mecânicos (DHR-ROTEAMENTO-006): SIM, parcialmente.** `aplicar_ficha_m.py` aplicou 4 de 7 (A6a, B3b, N2, N5). Escalou 3 (A6b, B3a, N3) por "cria regra/campo/mecanismo/ID normativo novo" — falso positivo provável: o detector `_cria_algo` acusa ID que aparece no texto novo e não no antigo, mesmo quando o ID já existe no documento. Esses 3 foram refeitos pelo Especificador (modelo caro). Em R1 a ficha foi gerada só como esqueleto (tudo `desenho`) sem eu classificar A6 como M: ficou 100% com o Especificador.
2. **Alternância de modelo por tarefa: NÃO.** Todas as 7 invocações de Agent registradas usaram "modelo do frontmatter" (`model: null`, sem `CLASSE-TAREFA`): Especificador = claude-opus-5-5 (coincide com a tabela, classe O); Revisor = claude-sonnet-5-5 (coincide com S1/S2, mas a revisão integral R1/R2 de errata CRITICAL seria S3 = opus pela tabela). A tabela só alterna por `model` + `CLASSE-TAREFA` por invocação; eu não os passei. O hook só exigiu `CLASSE-TAREFA` nas SendMessage com `PARECER:` (3 tentativas; 1 negada por eu esquecer a linha; as outras 2 SendMessage não citavam parecer).
3. **Propostas (só Andraus):** (a) ajustar `_cria_algo` para ignorar ID já presente no arquivo; (b) o Orquestrador passar `model`+`CLASSE-TAREFA` nas chamadas ao Revisor (S3 na revisão integral de Spec CRITICAL, S2 por delta, S1 conferência) e classificar M na ficha já na R1; (c) exigir esse preenchimento por hook (R-AC2 hoje é opcional). Nada aplicado.

### Resposta de Andraus às propostas a/b/c (chat, 2026-10-30; `DHR-ROTEAMENTO-007`) — Orquestrador (append-only)
As 3 propostas foram **aprovadas na íntegra** e implementadas: (a) `_cria_algo` ignora ID já presente no arquivo; (b) `esqueleto` marca `aplicado_m` os achados cujos FICHA-M já foram aplicados, e o Orquestrador passa `model` + `CLASSE-TAREFA` em toda chamada; (c) hook R-AC7 nega invocação de Especificador/Revisor sem `model` + `CLASSE-TAREFA`. Selo do gate regravado por ordem dele (só `roteador_modelos.py`).
