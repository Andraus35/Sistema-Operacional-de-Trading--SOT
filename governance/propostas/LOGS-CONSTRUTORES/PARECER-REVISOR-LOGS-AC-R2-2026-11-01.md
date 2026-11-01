# PARECER DO REVISOR — Logs dos Construtores — R2 — 2026-11-01

> Transcrição pelo Orquestrador do relatório do Revisor SOT (`CLASSE-TAREFA: S2`, `model: sonnet`). Alvo: `PROPOSTA-LOGS-CONSTRUTORES-2026-11-01.md` (MEDIUM, proposta de processo). `SHA256-ALVO: db11ad009d0225f5860b34f9503f523a5de065d8e4e37469e4a4cf71cde14e22`. `GATE-D: PASSOU_D` (do Orquestrador). **Modo integral** (11 de 19 blocos mudaram; passa da metade, revisor.md §3-bis item 6). Sem Bash/web: testes e medições não reexecutados pelo Revisor; INV-04 não verificado por ele nesta rodada. **Veredito: NÃO CONFORME** — 0 Críticos, 6 Médios (B01–B06), 7 Menores (B07–B13). Nada homologado; nenhuma decisão aberta fechada (CONS-01).

## Fechamento dos achados da R1 (A01–A13)
Fechados: **A04, A06, A07, A09, A11, A12, A13** (e A10 no texto, resíduo B12). Parciais: **A01** (resíduo B01), **A02** (B01), **A03** (B02), **A05** (B04), **A08** (B09).

## Achados novos
| ID | SEV | Tema | Tratamento (Orquestrador, 2026-11-01) |
|---|---|---|---|
| B01 | MÉDIA | `emite_seguro` não levanta mas pode **bloquear** (trava sem prazo + `fsync`) e estourar os 15 s do hook | **Código feito** (trava com prazo, teste com processo segurando a trava, mutação pega) |
| B02 | MÉDIA | Troca de ramo não é emitível (sem semente de `prev_hash`; CLI sem `--continua-de`) | **Parcial**: semente implementada; detecção de ramo e percorredor de pasta **pendentes** (plano) |
| B03 | MÉDIA | Plano promete interface (`emit` por stdin, `--verify` de pasta com âncora) que o código não tem; "pendente" velho | **Pendente** — texto do plano (Especificador) |
| B04 | MÉDIA | Camada vinda do chamador (default L1): esquecimento grava sessão em claro no git | **Código feito** (camada forçada pelo caminho; erro p/ valor desconhecido) |
| B05 | MÉDIA | `run_id`/`session_id`/`agent_id` mapeados de campos nunca lidos por hook do repositório | **Parcial**: `completa_ids` com fallback; **conferência com payload real pendente** |
| B06 | MÉDIA | Escrita não escapa U+0085/2028/2029; leitura por `splitlines` ⇒ falso "adulterado" | **Código feito** (escape na escrita + leitura por `\n`; 2 mutações pegas) |
| B07 | MENOR | Testes que não exercitam a regra; teste de pasta somente leitura vazio como root | **Feito** |
| B08 | MENOR | `saneia` estreito; cauda corrompida desabilita o segmento; escrita curta | **Feito** (sem auto-cura, por decisão de integridade; declarado) |
| B09 | MENOR | Contagens velhas (44 × real); bases 233 × 220 não comparáveis | Contagem **corrigida** (61); bases: **pendente** (Especificador) |
| B10 | MENOR | Tabela §2 do plano omite testes de hook, CI do `--verify`, `AGENTS.md` §8 | **Pendente** (Especificador) |
| B11 | MENOR | F2 executa o conteúdo do BL-039 sem declarar disposição (BL-039/BL-040) | **Pendente** (Especificador) |
| B12 | MENOR | `approval.decided` aceita qualquer `input_ref` | **Feito** (padrão `governance/DHR-*.md`; `verify` não confere existência — declarado) |
| B13 | MENOR | `canal_warn` padrão `stderr`; caminhos relativos ao cwd; `--camada` sem valor quebra | **Feito** |

**Condição para a próxima revisão (delta):** (a) limite de espera na gravação ✔; (b) decisão sobre troca de ramo (parcial); (c) interface do plano alinhada ao código; (d) camada derivada do caminho ✔; (e) fallback de IDs ausentes + conferência com payload real (parcial); (f) leitura de linha alinhada à escrita ✔.

<!-- ACHADOS-ESTRUTURADOS
B01|MEDIA|C05|emite_seguro nunca levanta mas pode bloquear: flock LOCK_EX sem prazo e fsync; wrapper so repassa stdout ao fim do Python; hook morre aos 15 s e o deny vira allow; orcamento so mede latencia tipica; sem teste de lock preso|espera limitada com LOCK_NB e retry curto, WARN ao estourar, teste com lock mantido por outro processo e orcamento de pior caso no plano
B02|MEDIA|C10|plano regra 2 manda abrir segmento -n encadeado no hash-cabeca anterior mas acrescenta nao tem semente de prev_hash e o CLI nao tem continua-de; sessao retomada em outro ramo cria o mesmo arquivo do zero e gera conflito add/add|implementar semente e deteccao de ramo com teste ou declarar a regra como nao suportada e o tratamento adotado
B03|MEDIA|C01|plano 3.3 descreve emit camada arquivo com stdin e 5.2 descreve verify de pasta com ancora e continua_de; o codigo faz emit arquivo json-em-argv e verify de um arquivo sem ler ancora; textos de pendente velhos em 3.2 3.3 3.4 5.2 8|alinhar sintaxe plano e codigo e listar como pendente o percorredor de pasta a leitura de ancora e o continua_de
B04|MEDIA|C09|camada informada pelo chamador com default L1 e valor desconhecido aceito; esquecimento grava session_id em claro em governance/logs e o git nao esquece (INV-07)|derivar ou forcar a camada pelo caminho de destino com lista fechada e erro para valor desconhecido; teste de esquecimento
B05|MEDIA|C05|run_id session_id agent_id obrigatorios mapeados de tool_use_id e prompt_id nunca lidos por hook do repositorio; campo ausente faz valida recusar e saneia nao cobre; evidencia do deny perdida|fallback deterministico para id ausente e conferencia com payload real e eventos sinteticos de tests antes de gravar
B06|MEDIA|C01|escrita usa json.dumps ensure_ascii False que nao escapa U+0085 U+2028 U+2029 e a leitura de verifica usa splitlines que divide neles; falso adulterado e numeracao de ancora deslocada; por leitura nao executado|ler por split de newline ou escapar na escrita; teste com esses caracteres
B07|MENOR|C03|verificacoes de chave de _varre inalcancaveis com esquema fechado e testes de chave testam valor ou passam por campo nao permitido; teste de pasta somente leitura e vazio como root|testar _varre isolado ou reconhecer a redundancia; trocar o teste de pasta somente leitura por um que funcione como root
B08|MENOR|C05|saneia so limpa reason e error contra a afirmacao da proposta 4.4; linha final corrompida ou escrita curta desabilita o segmento sem auto-cura; os.write sem checar retorno|corrigir o texto ou ampliar saneia; tratar cauda invalida e escrita curta
B09|MENOR|C06|hoje 44 na proposta l.107 e l.112 e 44 testes no plano l.4 contra 49 reais; 98 de 233 versus 134 de 220 compara bases diferentes; esquema em schemas ou scripts dito de tres jeitos|atualizar contagens e declarar a base de cada contagem de commits
B10|MENOR|C04|tabela do plano 2 omite testes novos de hook o workflow de CI do verify e o AGENTS.md secao 8|completar a tabela com testes CI e AGENTS
B11|MENOR|C08|F2 executa o conteudo do BL-039 em espera sem declarar absorver adiar ou mudar BL-039 e BL-040 e sem pesar a alternativa de coleta em script separado sem tocar o selo|paragrafo de disposicao com lastro
B12|MENOR|C05|valida aceita qualquer input_ref com path e sha256 de formato valido ou status sem-ata em approval.decided; sem padrao de caminho nem conferencia|restringir o padrao do caminho e declarar o que o verify nao confere
B13|MENOR|C05|canal_warn default stderr contra o plano 3.2; caminhos .telemetria relativos ao cwd; --camada sem valor da IndexError contra a docstring de exit 0|default arquivo, caminho ancorado na raiz do repositorio, tratar argumento ausente
-->

<!-- FICHA-M {"achados":[]} -->
