# PARECER DO REVISOR — Logs dos Construtores — R3 — 2026-11-01

> Transcrição pelo Orquestrador do relatório do Revisor SOT (`CLASSE-TAREFA: S2`, `model: sonnet`), **reenvio**: a 1ª execução da R3 se perdeu num reinício de contêiner e seu parecer nunca foi recebido nem usado. Alvo: `PROPOSTA-LOGS-CONSTRUTORES-2026-11-01.md` (MEDIUM, proposta de processo). `SHA256-ALVO: 4e595e3c9051aeae453d8cc1d13c83e75750b4d051a1005d76a3f47845c50d06`. `GATE-D: PASSOU_D`. Modo **delta** (2 blocos alterados e 2 adicionados de 21). Sem Bash: testes e mutações não reexecutados pelo Revisor. Passo 0: INV-04 verificado em `atomic-spec.md:404`, INV-07 em `:407`, ENF-03 em `:95` e `:269`; BL-036..042 não abertos linha a linha (não verificado além de BL-034/039/040). **Veredito: NÃO CONFORME — 0 Críticos, 2 Médios (C01, C02, ambos de documento), 5 Menores (C03–C07).** O código da F1 resistiu às tentativas de bypass, trava e bifurcação. Nada homologado; nenhuma decisão aberta fechada (CONS-01).
> Conferência do Orquestrador sobre a guarda pós-revisor (DHR-AUDITOR-EXTERNO-018): a guarda acusou G3 sobre a execução **perdida** (a1: a70295…); as linhas citadas existem e batem com o assunto (`log_ac.py:48` `camada_do_caminho`, `:243` WARN com carimbo UTC, `:257` `verifica`, `:292` `--ancora`): falso positivo de prosa lida como citação.

## Fechamento de B01–B13
Fechados no código/plano: **B01, B04, B06, B10**; declaração honesta e suficiente para proposta: **B02, B05** (pendentes da F2, com decisão de Andraus marcada); disposição fundamentada: **B11**; feitos com ressalvas: **B07, B08, B12, B13**; parcial: **B03** (virou C01), **B09** (virou C03).

## Achados novos e tratamento
| ID | SEV | Tema | Tratamento |
|---|---|---|---|
| C01 | MÉDIA | Plano descreve a F1 como era antes das correções (`emit` sem JSON "sai 2 sem WARN"; WARN "sem ts"; "Grep não achou `$id`") — desmentido por `log_ac.py:243`, `:280-282`, esquema l.2 | **Pendente** — Especificador (documento). Código já corrigido pelo Orquestrador |
| C02 | MÉDIA | Destino em L2 de `block` e de `exit 2` não definido (plano §3.1 item 3 manda L2 só `deny/ask/defer`) | **Pendente** — Especificador: tabela hook → evento → `decision` → camada |
| C03 | MENOR | Contagens: "61 testes" onde havia 63; "49 testes" do roteador × 40 `def test_` | **Orquestrador aplicou** (hoje **66**); roteador: 49 (MECANISMOS 2026-10-30) × 40 (grep 2026-11-01) registrado como NÃO MEDIDO qual vale |
| C04 | MENOR | Encadeamento entre ramos: primeira linha nula = segmento-raiz; âncora sem `continua_de`; precedência §10 × §1; `.git` pode ser arquivo | Pendente — Especificador |
| C05 | MENOR | Falha de `import log_ac` engolida sem WARN; orçamento sem pior caso; sem procedimento p/ cauda corrompida | Pendente — Especificador (texto) |
| C06 | MENOR | Camada lexical (symlink/caixa); `sem-ata` sem `task_ref`; `verify` quebra com entradas inválidas | **Código feito** (`task_ref` obrigatório no `sem-ata`; `verify` trata não-objeto/UTF-8/`--ancora` malformado; arquivo sem `\n` final não cola); symlink/caixa = **limite a declarar** (Especificador) |
| C07 | MENOR | Decisões de Andraus do chat (arquivo por sessão; `block`; esquema em `scripts/`; BL-039 PARCIAL) ainda como "recomendo/pendente" | Pendente — Especificador (registrar com data e fonte) |

**Condição para a próxima revisão (delta):** (a) C01: alinhar plano §3.3, §3.2(iii) e §10.3 ao código atual e remover a "medição" do `$id`; (b) C02: declarar `decision`, evento e camada de `block` e de `exit 2` por hook; (c) Menores C04–C07 não bloqueiam (preferir C04 e C05). Não se exige implementação de B02/B05.

<!-- ACHADOS-ESTRUTURADOS
C01|MEDIA|C01|plano descreve o codigo da F1 como estava antes das correcoes do Orquestrador: sai 2 sem WARN no emit sem json, WARN sem ts e Grep que nao achou $id, tudo desmentido por log_ac.py l.243 e l.280-282 e pelo esquema l.2 e testes r4|conferir cada fato sobre o codigo contra a versao corrente antes de escrever FONTE e reabrir o plano quando o Orquestrador muda a F1
C02|MEDIA|C05|destino em L2 de block e de exit 2 nao definido; plano 3.1 item 3 manda L2 receber so deny ask defer e os hooks de bloqueio nao tem decision nem camada declarados|tabela hook para evento decision e camada no plano 3 e na proposta 4.3 sempre que o enum de decision muda
C03|MENOR|C06|contagem 61 testes onde ha 63 em plano e proposta; 49 testes do roteador contra 40 def test_ no arquivo|gerar contagens por comando datado no fechamento da rodada e nao copiar numero de rodada anterior
C04|MENOR|C10|encadeamento entre segmentos de ramos distintos nao e emitivel como descrito: emissor procura anterior na arvore mas a premissa e que esta em outro ramo; formato da ancora sem continua_de; precedencia contraditoria entre cabecalho e 10.1; .git pode ser arquivo|declarar primeira linha nula como segmento raiz valido; ancora so registra continua_de quando a primeira linha o tem; uma unica regra de precedencia
C05|MENOR|C05|falha de import do log_ac no roteador e engolida sem WARN; orcamento so mede p95 e nao o pior caso com trava mais fsync; segmento com cauda corrompida sem procedimento de recuperacao|WARN minimo no except do import com teste; declarar pior caso e perda sob contencao como NAO MEDIDO; descrever o procedimento de novo segmento com continua_de
C06|MENOR|C09|camada derivada de forma lexical aceita symlink e outra caixa e L1 em qualquer pasta; approval.decided sem-ata nao exige task_ref contra o plano 3.4; verify quebra com linha nao objeto UTF-8 invalido e ancora malformada|declarar o limite ou exigir .telemetria para L1; exigir task_ref no sem-ata; tratar entradas invalidas no verify como problema e nao como excecao
C07|MENOR|C08|decisoes de Andraus do chat de 2026-11-01 seguem como recomendo ou pendente no plano 7 j k 10.3 10.4 e na proposta 4.2 l.51 l.67 l.75|registrar cada decisao com data e fonte no plano e na proposta sem fechar decisao aberta do ROADMAP
-->

<!-- FICHA-M {"achados":[]} -->
