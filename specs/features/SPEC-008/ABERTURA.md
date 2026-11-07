# Proposta de Abertura — SPEC-008: Manager — Orquestração Mecânica (Fase 1 + serviços de tempo) (slot ROADMAP §7, FASE 4)

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06/07) + DHR-BACKLOG-ABERTURA-001
**Autor:** Especificador Principal SOT (Claude Code, Opus 5.5)
**Data:** 2026-11-07
**Status:** **PROPOSTA DE ABERTURA** — aguarda parecer do Revisor (sobre o processo do Dossiê) e **homologação de Andraus** da definição da Spec. **NÃO** é baseline. `plan.md`/`checks.md` **não** foram escritos e só começam após a homologação desta abertura e por ordem expressa de Andraus. Tudo aqui é `[PROPOSTA]` salvo quando marcado `[FONTE]`. Nenhuma decisão aberta é fechada; nenhum baseline é tocado; nenhuma regra nova é criada.
**Depende de:** `research.md` (mesmo diretório — ler primeiro: §0 auditoria, §3 comparação, §4 repositórios, §5 lentes/WORKFLOW, §6 lacunas e conflitos) e `sources/`.
**Autorização:** ordem do Orquestrador por decisão de Andraus (chat, 2026-11-07): "SPEC-008 Manager Fase 1" como próxima Spec a abrir; só abertura.
**Rodada:** **R3** (2026-11-07) — corrige os 3 achados classe O do parecer R2 (`governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-ABERTURA-R2-2026-11-07.md`, incluído o adendo da guarda G1): R2-M01, R2-m01, R2-m02. A R2 corrigiu os achados classe O do parecer R1 (`governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-ABERTURA-R1-2026-11-07.md`); R1-m01 e R1-m03 foram aplicados pelo Orquestrador (FICHA-M). Mapa achado → correção em **§16** (R1→R2) e **§16-bis** (R2→R3). Texto substituído preservado como *[antes: …]* (INV-07). Andraus **não** escolheu nenhuma opção da P-12 ("Rodada 3 sem escolha sua", chat 2026-11-07): a R3 só reescreve as opções e a recomendação; a escolha segue dele. *[antes: "**R2** (2026-11-07) — corrige os achados classe O do parecer R1 (…); R1-m01 e R1-m03 foram aplicados pelo Orquestrador (FICHA-M). Mapa achado → correção em **§16**. …"]*
**Prefixos de ID:** `P-n` = pergunta a Andraus · `CONF-n` = confirmação a Andraus (esta Proposta) · `CF-n` = conflito/divergência e `L-n` = lacuna (research §6). *(Até a R1 confirmações e conflitos usavam ambos `C-n` — R1-m02.)*

> **Em uma frase (para o trader):** o Manager tem três trabalhos — escolher a missão (Fase 0), **tocar a operação do ciclo** (Fase 1) e decidir se manda o sinal (Fase 2); esta Spec é a **Fase 1, o "despachante com relógio"**: ele chama o analista de Elliott primeiro, chama o de SMC só se o primeiro viu oportunidade, pede a leitura de convicção de contexto, deixa um **alarme de preço armado**, abre a Killzone no **horário de Nova York**, chama o ICT **só** se o alarme tocar dentro da janela, e passa o caso para a Fase 2 — tudo por **regra fixa**, sem opinar sobre o mercado, sem gastar menos quando o mercado pede análise, e **nunca** mandando ordem.

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-008** (mantido) + uma 2ª Spec, chamada aqui de **"Spec de Tempo"**, **se** a divisão for aceita (P-2); número candidato **SPEC-050** | SPEC-008 é o slot (`ROADMAP.md` §7; DHR-EUA-E23). O número candidato SPEC-050 é o próximo livre (046/047/048/049 em uso ou reservados; busca 2026-11-07: o texto "SPEC-050" só aparece como dado de teste em `tests/test_telemetria_tokens.py`, e "COG-SPEC-050" (MC-COG-001) e "GOV-/EXP-/SKL-/LRN-SPEC-050" (reference/camadas) são outros espaços de nomes, todos com prefixo). Número = Andraus decide; até lá o texto usa "Spec de Tempo". |
| **Nome** | **SPEC-008 — Manager — Despacho e Ciclo (Fase 1)**; **Spec de Tempo — Manager — Relógio, Killzone e Alarme-gatilho** | Se a divisão for **recusada**: mantém-se "Manager — Orquestração Mecânica (Fase 1 + serviços de tempo)" (`[FONTE]` DHR-EUA-E23). |
| **Complexidade** | **CRITICAL — recomendado para a SPEC-008 (mantém o slot)**. Spec de Tempo: **HIGH — recomendado** (alternativa CRITICAL). | Despacho e ciclo: concorrência entre ativos, aviso duplicado/fora de ordem, reinício no meio do ciclo, tentativa de pular etapa por custo — terreno de D8 adversarial. Relógio/alarme: função de tempo pura, sem efeito externo, sem modelo; casos difíceis (horário de verão, meia-noite, prazo vencido na queda) cabem como cenários negativos de D7 (research §8.1). |
| **Profundidade-alvo** | SPEC-008 **D0–D8** (standard + adversarial); Spec de Tempo **D0–D7** (standard) | AGENTS.md §4. D6 (protocolo do quadro) **aplicável** na SPEC-008 (despacho via quadro — RULE-BB-001/005); na Spec de Tempo só pela publicação de eventos de tempo/alarme. |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Mesmo regime das Specs anteriores. |
| **Classe predominante** (orientação, não vinculante — CC-11 por BASpec) | **D** em tudo + **C** na trava constitutiva · **H/P: nenhuma** | ADR-MANAGER-001 §2.5 (Fase 1 mecânica). Ver §4. |

**Natureza:** Spec de **comportamento do Manager** (Trilha B), **dentro** do ciclo de trading. **RULE-ECC-05 incide** (três lentes — research §5). **CC-12 não incide** (o Manager não é especialista de escola — research §9).

**Validade do Dossiê (ECC-VAL-001):** acesso 2026-11-07 → **2027-02-05** (HIGH ou CRITICAL, 90 dias), para as duas peças.

---

## 2. Fronteira e escopo

### Dentro do escopo — SPEC-008 (Despacho e Ciclo)
- **S1 Pedido de ciclo:** entrada = campos de WF-01 (ativo, tipo de trading, tripla de TFs de WF-T01, Killzone, assistida/pré-programada — WF-K04); campo faltante ⇒ pedido recusado e registrado. Um ciclo por ativo/missão, **isolado** dos outros (WF-P01). Quem cria a missão é a Fase 0 (SPEC-015); até ela existir, o pedido vem de Andraus (WF-01).
- **S2 Grafo de despacho:** dado versionado; recusado se tiver ciclo (research §3.2); a ordem **respeita a hierarquia (INV-01/CC-01) para todo nó presente no grafo** + pipeline WF-02→WF-03→WF-04→WF-05; desempate por regra fixa. **Mapa nível a nível de INV-01:** Elliott → Estrutural (WF-02) · **Fibonacci → sem nó no WORKFLOW** · **Fractal → sem nó no WORKFLOW** · SMC → Institucional (WF-03) · ICT → Operacional (WF-05). Se Fibonacci/Fractal (slot SPEC-011) é etapa despachada pelo Manager ou parte interna do Estrutural = `[DECISÃO NECESSÁRIA]` (**P-11**; research §6 CF-8); até a resposta, a SPEC-008 não inventa nó nem posição. *[antes: "ordem = hierarquia (INV-01/CC-01) + pipeline WF-02→WF-03→WF-04→WF-05" — prometia a hierarquia inteira sem mapear Fibonacci/Fractal (R1-M01)]*
- **S3 Despacho via quadro e barramento:** o Manager publica o pedido no **seu** espaço do quadro (RULE-BB-002) e o aviso sai pelo barramento (SPEC-005); **nunca** chama agente diretamente (RULE-BB-001/005). Cada etapa espera a publicação da anterior (despacho síncrono no ciclo — research §3.2); prazo por etapa = parâmetro.
- **S4 Ativação progressiva:** Institucional só se o Estrutural publicar oportunidade (WF-03); Operacional só com alarme `TRIGGERED` dentro da janela (WF-05). **Inversão #1** (CONFLICT-MAP, linha #1 homologada): ruptura da hipótese dominante ⇒ ciclo completo, **independente de custo**. **Evento que dispara** `[INFERÊNCIA]`: publicação no quadro (SPEC-004), avisada pelo barramento (SPEC-005), da transição da hipótese `DOMINANT → REFUTED` ou `DOMINANT → SUPERSEDED` (transições listadas no CHM-001, l.753-754); o Manager reage ao evento, nunca julga se houve "ruptura". Nome exato do evento conferido no Plan contra a SPEC-004/005; se não houver evento publicado, a obrigação não é cumprível por regra fixa ⇒ volta a Andraus (research §6 L-8). Que a mecânica seja escrita **aqui** é `[PROPOSTA]` apoiada numa nota `[INFERÊNCIA]` do CONFLICT-MAP (research §0 h). *[antes: "**Inversão #1** (CONFLICT-MAP): ruptura da hipótese dominante ⇒ ciclo completo, **independente de custo**." — sem evento observável (R1-m05)]*
- **S5 Leitura macro:** invoca o mecanismo da SPEC-003 sobre o subconjunto estrutural+institucional (RULE-CF-010; 1ª das 2 invocações — Q-A5) e aplica **gate D "conclusiva?"** com limiar **parâmetro** (valor = P-5); discordância direcional Estrutural×Institucional ⇒ NEUTRO e encerra (AGENTS §6.4; WF-F01 ramo 2). Não calcula vetor, não pesa, não arbitra.
- **S6 Pedido de alarme e disparo do Operacional:** convicção macro conclusiva ⇒ **pede** à peça de tempo (Spec de Tempo) que arme o alarme com os campos **copiados** da hipótese-origem (P-8); ao receber `TRIGGERED` dentro da janela, despacha o Operacional; confere o **alinhamento** de direção do setup com a hipótese de contexto (WF-T02 — dono a confirmar, CONF-4). *[antes: "C-4"]*
- **S7 Máquina de estados do ciclo:** WF-F02 como tabela fechada (estado × evento → próximo; par não listado = recusado e registrado); seis ramos de falha de WF-F01 como transições nomeadas **quando mapeiam em transição listada**, conferidos **item a item** (R2-m02; WORKFLOW l.70 × WF-F02 l.71 e WF-A02 l.54) — `[INFERÊNCIA]` sobre a leitura das setas, que o WORKFLOW não nomeia:
  1. **Ramo 1 — sem oportunidade (WF-02/03) → "encerra o ciclo":** ocorre em `AGUARDANDO`; WF-F02 não escreve o estado final ⇒ **P-12** (proposta: `RECUSADO`). Dono: **SPEC-008**.
  2. **Ramo 2 — discordância Estrutural×Institucional → NEUTRO:** ocorre em `AGUARDANDO` (leitura macro, S5); estado final não escrito ⇒ **P-12** (proposta: `RECUSADO`). Dono: **SPEC-008**.
  3. **Ramo 3 — sem confirmação operacional (WF-05) → "reset do alarme":** ocorre em `ATIVADO` (inclui o desalinhamento de CONF-4); "reset" não mapeia em WF-A02 nem em WF-F02 ⇒ **P-12**. Dono: **SPEC-008** (ciclo) e Spec de Tempo (alarme, se a divisão for aceita).
  4. **Ramo 4 — veto de risco (WF-07) → "sem sinal":** ocorre em `EM_RISCO`; é o **único** que mapeia numa transição listada, `EM_RISCO → RECUSADO`, **lendo "sem sinal" como `RECUSADO`** `[INFERÊNCIA]`. Dono: **RISK-SPEC** (FASE RISK, não autorizada) — **não** é da SPEC-008.
  5. **Ramo 5 — alarme expirado → "reset":** ocorre em `ARMADO`; do lado do alarme mapeia em `ARMED → EXPIRED` (WF-A02, estado final listado); do lado do ciclo o "reset" não mapeia ⇒ **P-12** (proposta: `EXPIRADO`). Dono: **SPEC-008** (ciclo) e Spec de Tempo (alarme).
  6. **Ramo 6 — reentrada após stop → "sinalizada pelo SOT" (overtrading = Bot Trade Finance, WF-X04):** ocorre **depois** de `SINAL_ENVIADO` (o ciclo que mandou o sinal já terminou), portanto **fora** de WF-F02; destino, dono e a fonte do evento de stop não estão escritos ⇒ **P-13** (research §6 CF-9). Dono: **nenhum na SPEC-008** até a resposta; a SPEC-008 não especifica o ramo 6.
  *[antes (R2): "(hoje só o ramo 4, veto de risco, cai literalmente em `EM_RISCO → RECUSADO`; os demais dependem de P-12)" — "literalmente" forte demais e ramo 6 sem destino nem dono (R2-m02)]* *[antes (R1): "seis ramos de falha de WF-F01 como transições nomeadas" sem ressalva]*;
  nenhum estado novo nem renomeado (WORKFLOW soberano). **Dono por transição** (tabela "Dono por transição de WF-F02" abaixo): a SPEC-008 conduz de `AGUARDANDO` até a entrada em `EM_SÍNTESE` e as saídas para `EXPIRADO` nesse trecho; a partir de `EM_SÍNTESE`, as transições são da SPEC-014 e, em `EM_RISCO`, da família RISK-SPEC — conflito de três lados em **CONF-1** (research §6 CF-1). Os ramos 3 e 5 ("reset do alarme") **não** mapeiam em transição listada ⇒ **P-12** (research §6 CF-7); a SPEC-008 não cria transição de volta. *[antes: "…nenhum estado novo nem renomeado (WORKFLOW soberano). Dono da FSM = C-1." — FSM dada inteira à SPEC-008 (R1-M04/R1-M05)]*
- **S8 Tetos e orçamento:** teto de passos por ciclo, de voltas que cada agente recebe (inclui `max_retrieval_rounds` pedido pelas SPEC-007/048), de falhas seguidas por agente/ferramenta, prazo por etapa — tabela fixa por tipo de missão × etapa; valores **INDETERMINADOS** (CC-09). Estouro ⇒ estado nomeado + registro + aviso, nunca silêncio. **Nunca** pula etapa com evento estruturalmente relevante por custo (CEE-001 §10 S2). Custo vive em espaço próprio, **nunca** no Conviction Vector (INV-04).
- **S9 Interromper / aguardar / escalar / encerrar:** cada parada tem motivo nomeado; INDETERMINADO é estado válido com abstenção produtiva (RULE-MET-02: o que falta, o que muda a conclusão); escalada a Andraus = registro + aviso, sem decidir por ele.
- **S10 Registro do ciclo:** só-inserção (INV-07); cada despacho grava regra, versão do grafo, evento causador e instante como **fato registrado** (D9: "por que este agente rodou agora"); retomada após queda a partir do registro, sem refazer etapa concluída (research §3.4); mecanismo de guarda = SPEC-009 (P-6).
- **S11 Entrega à Fase 2:** passa o caso à SPEC-014 e **para** na fronteira (`EM_SÍNTESE`); em missão pré-programada (WF-K04) o resultado fica em fila para revisão.
- **S12 Trava constitutiva (Classe C, E3):** o Manager-Fase-1 **não** analisa mercado, **não** cria nem edita hipótese, **não** calcula convicção, **não** muda classe de modelo de agente (CEE-001 §10 S1/S5), **não** monta TMP nem Signal Package e **não** emite ordem (INV-05; RULE-DEC-01).

### Dentro do escopo — Spec de Tempo (Relógio, Killzone e Alarme-gatilho) — **se** a divisão for aceita; senão, volta à SPEC-008
- **T1 Fonte de tempo registrada:** cada decisão de tempo usa um instante gravado como fato; a reexecução lê o registro, nunca o relógio (research §3.4/§3.6).
- **T2 Calendário de Killzones:** tabela por ativo, versionada e editável só por Andraus (WF-K01; WF-R02/R03 `[REVISAR · BL-026]`); valores nunca constantes.
- **T3 Fuso e horário de verão:** cálculo em `America/New_York` pelo banco IANA; fuso da máquina só exibe/agenda (WF-K03); casos obrigatórios: hora inexistente, hora ambígua, janela que cruza meia-noite, máquina em outro fuso.
- **T4 Pré-aviso:** evento 1h antes de cada janela (WF-K02). **Nota (R1-M03):** WF-K02 nomeia o dono do abrir/fechar como "Manager/Scheduler (SPEC-008/015)"; com a divisão o abrir/fechar fica aqui, na Spec de Tempo — o ator continua o Manager, muda só o documento ⇒ divergência de número registrada (research §6 CF-6) e levada a Andraus (**CONF-5**).
- **T5 Objeto do alarme:** campos de WF-A01, **copiados** da hipótese-origem/publicação dos agentes; o alarme é gatilho de **análise**, nunca ordem (INV-05).
- **T6 FSM do alarme:** WF-A02 como tabela fechada; `TRIGGERED` **só** dentro da janela; o preço que dispara é Observação de fonte de dados (Observação ≠ Evidência — INV-06), fonte = INDETERMINADA (research §6 L-5).
- **T7 Morte do alarme:** expira por prazo; cancela se a hipótese-origem vai a `SUPERSEDED`/`REFUTED` (WF-A03; estados CHM-001); prazo vencido durante queda ⇒ `EXPIRED`, nunca disparo atrasado.
- **T8 Mercado fechado / calendário ausente:** parâmetro por ativo (WF-P02); sem calendário ⇒ registro "calendário de mercado não informado" (P-9).

### Fora do escopo (Non-goals)
| Item | Motivo | Dono |
|---|---|---|
| Tipo de missão, portfólio de missões, Campanha, Plano B | Fase 0 (ADR §2.3); **SPEC-015-SCOPE ABERTA** | **SPEC-015** |
| Arbitragem entre agentes, convicção global, decisão de envio, pacote risco-retorno, TMP | Fase 2 (DHR-ARQ-002) | **SPEC-014** / **SPEC-016** |
| Cálculo do Conviction Vector, fórmula, pesos, limiares definitivos | **J-001/N-001 ABERTAS**; WF-D03 ABERTA | **SPEC-003**/CCM-001 |
| Esquema e mecanismo de persistência do estado | **G-001 ABERTA** | **SPEC-009** |
| Estados de objeto não-hipótese no quadro | **M-001 ABERTA** | SPEC-004 / Andraus |
| Transporte de avisos; canal de saída do Signal Package | BASELINE | **SPEC-005** |
| Análise de mercado, hipótese, setup (entrada/stop/alvo) | INV-02; RULE-BB-005 | **SPEC-010..013** |
| R:R, sizing, heat, avaliação de risco | WF-X01..X05; FASE RISK | **RISK-SPEC** |
| Provedor de preço/dados de mercado | BL-033; DHR-DEC-004 | Market Data / **SPEC-038** |
| Formalização de Skills (o que é Skill e quando despertar como unidade) | I-001 fechada; corte exato adiado | **SPEC-025** |
| Telemetria de tokens e observabilidade | BL-036..042 | **SPEC-040/041** |
| Overtrading; execução de ordem | WF-X04; INV-05 | Bot Trade Finance |
| Journal / checkpoint humano formal | WF-J01 | **SPEC-018** |
| Motor (biblioteca de FSM, agendador, banco) | ROADMAP §22 | BUILD |
| Coordenação entre "Cognitive Orchestrator" e Manager | possível dupla posse futura (research §6 CF-5 *[antes: C-5]*) | SPEC-023 (quando abrir) |

### Anti-dupla-posse (anti-double-ownership)
| Vizinha | A SPEC-008 faz | A vizinha faz | Linha de corte |
|---|---|---|---|
| **SPEC-003** (BASELINE) | **invoca** a leitura macro e aplica gate D com limiar-parâmetro | **calcula** o vetor (subconjunto/completo) | Nada de fórmula/peso aqui (RULE-CF-010; DHR-ARQ-001) |
| **SPEC-009** | declara **o que** precisa sobreviver a queda e o registro só-inserção | define **como** guardar, serializar, expirar (G-001) | Requisito de interface `[PROPOSTA]`; SPEC-009 vem depois (P-6) |
| **SPEC-014** | conduz até `EM_SÍNTESE` e entrega | arbitra, forma convicção global (2ª invocação), decide envio, gera TMP | Fronteira = estado `EM_SÍNTESE` de WF-F02 |
| **SPEC-015** | executa o ciclo de um pedido já definido | cria/decide/gerencia missões | Interface = pedido de ciclo com campos de WF-01 |
| **SPEC-004/005** (BASELINE) | publica no próprio espaço; assina avisos | quadro e barramento | RULE-BB-001/002/005; transporte ≠ controle (SPEC-005) |

### Dono por transição de WF-F02 (FSM do ciclo) — `[PROPOSTA]`, depende de CONF-1 (R1-M04)
Estados = os de WF-F02, sem acréscimo nem renomeação. A **tabela inteira** (todos os pares estado × evento) é escrita **uma vez**, na SPEC-008, com a coluna "dono"; cada vizinha especifica o comportamento das **suas** transições citando a tabela, sem redefini-la. Interface = evento publicado no quadro (SPEC-004) e avisado pelo barramento (SPEC-005).

| Transição (WF-F02) | Evento que a dispara (publicado) | Dono proposto |
|---|---|---|
| (entrada) → `AGUARDANDO` | pedido de ciclo com campos de WF-01 (de Andraus; depois da Fase 0) | **SPEC-008** (consome o pedido; a criação da missão é da SPEC-015) |
| `AGUARDANDO` → `CONTEXTO_FORMADO` | Estrutural (e Institucional, se acionado) publicaram + leitura macro conclusiva | **SPEC-008** |
| `CONTEXTO_FORMADO` → `ARMADO` | alarme confirmado `ARMED` pela Spec de Tempo | **SPEC-008** |
| `ARMADO` → `ATIVADO` | alarme `TRIGGERED` dentro da Killzone (Spec de Tempo) | **SPEC-008** |
| `ATIVADO` → `EM_SÍNTESE` | Operacional publicou o setup + alinhamento conferido (CONF-4) | **SPEC-008** — **última transição da SPEC-008**; o evento "caso entregue à Fase 2" é a interface com a SPEC-014 |
| `EM_SÍNTESE` → `EM_RISCO` | Fase 2 decidiu enviar e gerou o TMP interno | **SPEC-014** |
| `EM_RISCO` → `SINAL_ENVIADO` / `RECUSADO` / `EXPIRADO` | decisão do Risk Agent (WF-07; WF-F01 ramo 4 = veto) ou prazo | **RISK-SPEC** (FASE RISK, não autorizada — fronteira declarada, nada especificado) |
| *Não literal em WF-F02:* saída para estado final **antes** de `EM_RISCO` — ramos 1 (sem oportunidade), 2 (NEUTRO), 3 e 5 ("reset"), prazo vencido em `AGUARDANDO`…`ATIVADO`, e Fase 2 que decide não enviar em `EM_SÍNTESE` | — | **pergunta P-12** — a sequência de WF-F02 só chega aos estados finais a partir de `EM_RISCO`; a SPEC-008 **não** cria essas setas sem a resposta de Andraus. Dono, se Andraus as admitir: SPEC-008 até `ATIVADO`; SPEC-014 em `EM_SÍNTESE` |
| *Fora de WF-F02 (R2-m02):* ramo 6 de WF-F01 — reentrada após stop, depois de `SINAL_ENVIADO` | evento de stop — fonte **INDETERMINADA** (não há, no WORKFLOW, aviso do Bot Trade Finance de volta ao SOT — `[INFERÊNCIA]`) | **pergunta P-13** — a SPEC-008 não especifica; candidatos: quem pede ciclos (SPEC-015 / Andraus) e quem monta o Signal Package (SPEC-014) |

`[INFERÊNCIA]` sobre a leitura das setas de WF-F02 (a sequência do WORKFLOW não nomeia eventos); nenhuma transição nova.

---

## 3. Quantidade e dimensionamento (RULE-ECC-07) — **divisão proposta**

**BASpecs candidatas (só títulos; numeração no Plan; prefixos a definir):**
- **SPEC-008 (12):** 1 pedido de ciclo e isolamento por ativo · 2 grafo de despacho sem ciclo e ordem pela hierarquia · 3 despacho via quadro/barramento e espera · 4 ativação progressiva + Inversão #1 · 5 leitura macro + gate "conclusiva" + NEUTRO · 6 pedido de alarme + despacho do Operacional + alinhamento · 7 FSM do ciclo e seis ramos · 8 tetos e orçamento (sem cortar etapa relevante) · 9 interromper/aguardar/escalar/encerrar · 10 registro do ciclo, reconstrução e retomada · 11 entrega à Fase 2 · 12 trava constitutiva (C/E3).
- **Spec de Tempo (8):** 1 fonte de tempo registrada · 2 calendário de Killzones versionado · 3 fuso e horário de verão · 4 pré-aviso · 5 objeto do alarme · 6 FSM do alarme · 7 morte do alarme · 8 mercado fechado/calendário ausente.

**Linhas previstas do corpo normativo** `[INFERÊNCIA]` — mesma base e método da abertura da SPEC-049 (§3 de lá): SPEC-048 (CRITICAL D0–D8, 12 BASpecs, corpo 1.935 linhas) decomposta em **fixo ≈887**, **≈74 por BASpec** em CRITICAL ((810 + 75 de D8) / 12) e **≈67,5** em HIGH, **≈20 por Enforcement Contract**. Verificação cruzada pela contagem de linhas dos arquivos `plan.md` (Grep, 2026-11-07): SPEC-004 1.325 linhas / 14 BASpecs (≈95 por BASpec, tudo incluído — densidade **baixa**, pré-RULE-ECC-07); SPEC-048 1.935 / 12 (≈161 — densidade **alta**); SPEC-049 1.583 / 11 (≈144).

**Ajuste de errata (como na SPEC-049 §3):** o fixo de 887 inclui ~58 linhas de propostas de errata da SPEC-048; sem errata, o fixo cai para **839** (−48). A errata de re-apontamento (§8) **só existe com a divisão** e cai num **único** Plan — proposto: o da **SPEC-008** (Plan que sai primeiro e slot de onde as referências saem). Logo: Spec única = 839; SPEC-008 = 887; Spec de Tempo = 839. A faixa usa a densidade "tudo incluído" (baixa ≈95, alta ≈161 por BASpec), por isso não soma fixo.

| Cenário | Central (fixo + BASpecs + ECs) | Faixa (densidade baixa ≈95 · alta ≈161 por BASpec) | Leitura RULE-ECC-07 (central **e** faixa contra alerta 1.900 e teto 2.000) |
|---|---|---|---|
| **Spec única** (20 BASpecs, ~9 ECs, CRITICAL) | 839 + 20×74 + 9×20 = **≈2.499** | 1.900 – 3.220 | Central **acima do teto**; faixa do alerta (base) a 1,6× o teto (topo) ⇒ divisão **deve** ser proposta antes do Plan |
| **SPEC-008** (12 BASpecs, ~6 ECs, CRITICAL) | 887 + 12×74 + 6×20 = **≈1.895** | 1.140 – 1.932 | Central **5 linhas abaixo do alerta**; **topo da faixa passa do alerta** (1.932) e fica 68 abaixo do teto; acima de 1.600 ⇒ **Andraus confirma** (P-3). Risco real de o Plan medido passar de 2.000 — ver P-3 |
| **Spec de Tempo** (8 BASpecs, ~3 ECs, HIGH) | 839 + 8×67,5 + 3×20 = **≈1.439** | 760 – 1.290 | Central e faixa abaixo de 1.600 (em CRITICAL: 839 + 8×74 + 60 ≈ **1.491**) |

*[antes: Spec única "887 + 20×74 + 9×20 = ≈2.547 · Acima do teto 2.000"; SPEC-008 "Abaixo do teto e do alerta (1.900) por pouco"; Spec de Tempo em CRITICAL "887 + 8×74 + 60 ≈ 1.539" — comparação só pelo valor central e ajuste de errata aplicado só à Spec de Tempo (R1-m04)]*

**Proposta de decomposição (recomendada): duas Specs por fronteira de contrato.** A Spec de Tempo **produz** eventos de tempo (janela aberta/fechada, pré-aviso) e estados do alarme, e **consome** o pedido de armar, os estados da hipótese-origem (CHM-001) e a Observação de preço; a SPEC-008 **consome** esses eventos e **produz** despachos e transições do ciclo. O que muda junto fica junto: mudar horário de Killzone ou regra de horário de verão (BL-026) não mexe no grafo de despacho; mudar a ordem dos agentes não mexe no relógio. Não é divisão por fase nem por tipo de tarefa (RULE-ECC-07). Cada peça é revisável sozinha.

**Alternativas registradas:** (B) **Spec única** — passa do teto; só se Andraus mandar mesmo assim. (C) **Três peças** (tempo · alarme+ciclo · despacho+orçamento) — o fixo de ~840–890 linhas se repete três vezes (≈4.200 linhas no total contra ≈3.330 das duas peças — 1.895 + 1.439 = 3.334) e corta o alarme do ciclo, que mudam juntos (`ARMADO`/`ATIVADO` do ciclo espelham `ARMED`/`TRIGGERED` do alarme). **Incertezas:** base n=1 decomposta; densidade varia ~1,7× entre Specs; o histórico de rodadas cresce com o número de rodadas. **Gatilho processual:** mudar escopo ou dividir depois de o Plan começar = nova abertura.

**Ordem proposta:** Plan da **SPEC-008 primeiro** (ordem de Andraus), declarando a interface com a Spec de Tempo como requisito `[PROPOSTA]` (padrão SPEC-048→SPEC-049); depois o Plan da Spec de Tempo. **Este Dossiê cobre as duas** (research §3.6/§3.7 e repositórios); se Andraus preferir Dossiê próprio para a Spec de Tempo, ela abre depois com o seu (P-2).

---

## 4. Classe RULE-MECH-01 (CC-11) — orientação por tipo de BASpec

- **Classe D (regra fixa, sem modelo):** pedido de ciclo; grafo e ordem; despacho e espera; ativação progressiva; gate "conclusiva" (comparação com parâmetro); NEUTRO por discordância; alinhamento de direção; FSM do ciclo; tetos e estouro; paradas e escalada; registro; entrega à Fase 2; todo o relógio, Killzone, pré-aviso e alarme.
- **Classe C (E3, fail-closed):** a trava constitutiva S12 — se o Manager-Fase-1 tentar qualquer capacidade negada (analisar, criar hipótese, calcular convicção, mudar classe de modelo, montar TMP/Signal Package, emitir ordem), a ação é **recusada** e registrada. **Justificativa CC-11** `[INFERÊNCIA]`: o risco negado é alto e irreversível (ordem/sinal fora do caminho governado violaria INV-05 e as Salvaguardas de Sinal); a trava não chama modelo nem acrescenta etapa cara (Economicidade preservada).
- **Classe H/P: nenhuma** — julgamento leve é das Fases 0/2 (ADR §2.5). Se o Plan precisar de julgamento, é sinal de escopo errado ⇒ volta a Andraus.
- **Pisos de nível (D2) propostos:** publicação do pedido de despacho **E2** (desvia o caminho da análise); armar/cancelar alarme **E2**; transição do ciclo **E2**; registro **E1**; entrega à Fase 2 **E2**; trava **E3**. Economicidade nunca rebaixa nível. ENF-07: a trava E3 declara método de falso-DENY (despacho legítimo recusado), limiar = lacuna aberta.

**Critério 4Es:** Eficácia — um despachante que opina ou corta análise por custo cria caminho de sinal sem governo; por isso tudo é D e a trava é C. Efetividade — mesma entrada, mesma sequência de despachos (reconstrução). Eficiência — ativação progressiva evita rodar SMC/ICT sem oportunidade. Economicidade — zero chamada de modelo na Fase 1.

---

## 5. Princípios de Domínio (RULE-PD-01 / CC-12) — **NÃO incide**
O Manager não é Spec de especialidade de escola (ADR-MANAGER-001 §2.5). Nenhum `PD-xx`. `[INFERÊNCIA]`

---

## 6. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação | Nota |
|---|---|---|
| CC-01 | **Aplica — foco** | Ordem de despacho respeita a hierarquia para os nós presentes; posição de Fibonacci/Fractal = P-11 `[DECISÃO NECESSÁRIA]`; ICT só depois do contexto; ICT não cria hipótese. *[antes: "Ordem de despacho = hierarquia; …"]* |
| CC-02 | Aplica | Não redefine CHM-001/CEM-001/CCM-001/CEE-001; consome por referência. |
| CC-03 | **Aplica** | Só **invoca**; limiar macro = parâmetro (P-5); J-001/N-001 abertas; 8 dimensões intocadas. |
| CC-04 | **Aplica** | CEE-001 §10 S1/S2/S5 (roteamento e "não suprimir por custo") e §11 (nenhum sinal sai daqui). |
| CC-05 | Aplica | CRITICAL (SPEC-008) / HIGH (Spec de Tempo) propostos — P-1/P-2. |
| CC-06/07 | Diferido ao Plan | Engineering Cards no BUILD. |
| CC-08 | **Aplica — foco** | Pai vertical = "Manager Contract" (P-4) ou ADR-MANAGER-001 v1.0; INHERITS: ADR §2.2/2.3/2.5, DHR-ARQ-001/002, DHR-EUA-E23, RULE-CF-010 (SPEC-003), RULE-BB-001/002/005, CEE-001 §10, CONFLICT-MAP Inversão #1, interfaces pedidas por SPEC-004/005/007/048. REMOVED vazio (proposta). |
| CC-09 | **Aplica** | Nenhum número (tetos, prazos, limiar macro = INDETERMINADOS); INDETERMINADO como estado válido. |
| CC-10 | **Aplica** | Acepções: "despachar" ≠ "chamar diretamente"; "orçamento" (custo/tetos) ≠ convicção; "convicção macro" = leitura do mesmo vetor (WF-C01), ≠ convicção global; "alarme" = gatilho de análise ≠ ordem; "Killzone" (janela de tempo ICT) ≠ sessão de pregão. |
| CC-11 | Aplica (§4) | Por BASpec; D + C; zero H/P. |
| CC-12 | **NÃO incide** (§5) | — |

---

## 7. Decisões de Andraus que entram nesta Spec — disposição proposta

| Decisão | Fonte | Disposição |
|---|---|---|
| Manager ator único; Fase 1 mecânica | ADR-MANAGER-001 §2.2/§2.5 | **Incorporar** como herança (S12; Classe D). |
| 3 Specs sob "Manager Contract"; slots indicativos | DHR-EUA-E23 | Aplicado; divisão interna proposta (§3) é permitida pelo item 3 da ata. |
| Invocação 2x (macro Fase 1) | Q-A5 / DHR-DEC-001; RULE-CF-010 | **Incorporar** (S5). Fórmula **não**. |
| Killzone e alarme como mecanismos formais | WF-D01, WF-D02 FECHADAS | **Incorporar** (S6, T1–T8). |
| ICT = Operacional, não cria hipótese | WF-D04 FECHADA | **Incorporar** (S4/S6). |
| Event Bus existe como camada fina | EVENT-BUS-001 FECHADA (DHR-SPEC005-002) | **Usar** para avisos de despacho. |
| Ruptura de hipótese dominante ⇒ análise completa | CONFLICT-MAP Inversão #1 (HOMOLOGADO 2026-09-20) | **Incorporar** (S4). |

---

## 8. Re-apontamento — errata e gatilhos (só proposta; nada executado)

- **Sem divisão:** nenhuma errata.
- **Com divisão:** nota aditiva de re-apontamento (padrão ERRATUM-REAPONT-001), proposta no Plan da SPEC-008 (§3, ajuste de errata), cobrindo as **9 linhas RE** da varredura exaustiva da SPEC-003 (research §8.3: `plan.md` l.46, l.98, l.191, l.224, l.1149; `research.md` l.129, l.183, l.300, l.301) → Spec de Tempo — **6 delas são mistas** (`plan.md` l.46, l.98, l.191, l.224, l.1149; `research.md` l.183) e só a parte Killzone/alarme (WF-D01/D02) é re-apontada; a parte **papel do ICT (WF-D04)** e a invocação **ficam** na SPEC-008 (é ela que despacha o Operacional — S4/S6); inteiras só `research.md` l.129, l.300, l.301 (R2-m01) *[antes: "… l.300, l.301) → Spec de Tempo;" — linhas mistas tratadas como RE inteiras]*; as linhas de **histórico de versão e de rodada** (`plan.md` l.30, l.33; `checks.md` l.40, l.54, l.63) **não são editadas** (INV-07) — a nota as lista como lidas sob a errata; invocação macro e demais referências à SPEC-008 (orquestração, orçamento, latência — SPEC-004/005/007/048) **ficam**. Sem reescrever a SPEC-003 (INV-09). **Regra de busca para a ata** (padrão DHR-SPEC048-001 Q-7, `[PROPOSTA]`): texto em research §8.3; a busca é refeita quando a errata for escrita. *[antes: "…para `SPEC-003/plan.md` l.46 e l.224 (Killzone/alarme 'Manager/Scheduler (SPEC-008…') → Spec de Tempo; … Lista exata reconferida por Grep no Plan." — lista por amostra (R1-M02)]*
- **Gatilhos do RMR-001:** com divisão, BL-026 ganha `∨ spec:<número da Spec de Tempo> em redação` (aditivo). BL-043..046 ficam como estão.
- **ROADMAP §7/§21/§26:** registrar a abertura e, se aceita, o slot da Spec de Tempo com o número que Andraus decidir (só Orquestrador/Andraus — §12).

---

## 9. Itens do backlog vinculados por regra — disposições PROPOSTAS (declaradas no Plan; o Especificador não promove)

- **BL-026** (WF-R01..R03, `Em espera`) — `Disposição: PARCIAL` — motivo: a SPEC-008 consome WF-R01 (TFs) pelo pedido de ciclo e trata tudo como parâmetro editável; WF-R02/R03 (horários e Killzones por ativo) vão à Spec de Tempo (ou ficam aqui se não houver divisão). A pauta de valores é **recolocada agora** a Andraus (P-10), como o item manda.
- **BL-043** (log dos Construtores, F2b) — `Disposição: FORA` — motivo: processo dos Construtores, não comportamento do Manager; a execução (auditoria do código da F2a, F2b, selo) segue com o Orquestrador **por ordem de Andraus**, independente do conteúdo desta Spec.
- **BL-044** (medição do pré-gate na abertura e no Plan) — `Disposição: REFERÊNCIA` — motivo: o protocolo mede o **processo** desta Spec (Médias e tokens por rodada da abertura e do Plan; pré-gate antes de cada entrega). Cabe ao Orquestrador rodar e registrar; nada entra no texto normativo.
- **BL-045** (autopré-check legível por máquina) — `Disposição: REFERÊNCIA` — motivo: depende da medição do BL-044.
- **BL-046** (checklist único D/H) — `Disposição: REFERÊNCIA` — motivo: depende da medição do BL-044; agentes reservados.
- **Não vinculados, só visibilidade:** BL-029 (consumidor fail-closed do vetor — Fase 2/SPEC-014; não toca a Fase 1), BL-033 (provedor de preço do alarme — L-5), BL-036 (telemetria de custo — o orçamento da SPEC-008 é de controle, não de medição; SPEC-040).
- **Varredura de itens `ATIVADO` (R1-m07; passo 11-bis):** **BL-003** (persistência física de hipótese/estado) está **`ATIVADO`** (RMR-001: Andraus, 2026-10-17, DHR-BACKLOG-001; gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação`; encaminhamento "tratar no gate da SPEC-006"; H-001 fechada, G-001 aberta). **Não** é vinculado à SPEC-008 por regra (o gatilho não cita a SPEC-008), mas toca a P-6 (memória do ciclo até a SPEC-009): a SPEC-008 só declara o requisito e **não** absorve o item — já tem encaminhamento, não fica pendente sem dono. O único outro item com estado `ATIVADO` na coluna de estado do painel (leitura de 2026-11-07) é **BL-011** (MC-EXP-001, encaminhado ao gate da SPEC-006) — não toca o Manager-Fase-1; a conferência por script (`backlog_triggers.py`) é do Orquestrador (§12). *[antes: a lista de visibilidade não varria itens `ATIVADO`]*

---

## 10. Dependências e decisões abertas (CONS-01 — não fechar)

**Montante homologado:** SPEC-001 (estados da hipótese via CHM-001), SPEC-002, SPEC-003 (RULE-CF-010), SPEC-004 (quadro), SPEC-005 (barramento), SPEC-019/020/021, CEE-001 v2.0, ADR-MANAGER-001, `WORKFLOW.md` v2.1. **Fornecedoras de interface que pedem algo à SPEC-008 (R1-m07):** **SPEC-007** (orçamento de recursos da consulta; `max_retrieval_rounds` = "orçamento da SPEC-008"; latência — `SPEC-007/plan.md` l.1982, l.2136, l.2297, l.2679) e **SPEC-048** (mesmo teto e latência do pacote; WF-K02 — `SPEC-048/plan.md` l.342, l.445, l.1131); **SPEC-006** (memória/KG) **não** cita a SPEC-008 (Grep 2026-11-07) — entra só como montante das SPEC-007/048. Versões homologadas como registradas na ABERTURA da SPEC-049 (l.191): SPEC-007 v2.3, SPEC-006 v1.7 + erratas, SPEC-048 v1.4 `[FONTE]`. *[antes: a lista de montante não citava SPEC-006/007/048]* **A jusante e depois no caminho crítico:** SPEC-009 (estado), SPEC-014/015 (Fases 2/0) — interfaces declaradas como requisito.

**Abertas que esta Spec toca e não fecha:** **J-001/N-001** (limiar macro e tetos — P-5), **G-001** (persistência — P-6), **M-001** (estados no quadro — P-6), **SPEC-015-SCOPE** (fronteira com a Fase 0), **WF-D03** (só para dizer que a Fase 1 invoca e não define fórmula), **C-001** (redação EARS). **Não tocadas:** K-001, SPEC-045-RUNTIME-001, ECC-03-001, D-PCC-4.

---

## 11. Riscos (com contenção)

- **R-1 Despachante vira analista** — S12 (C/E3); RULE-BB-005; zero modelo.
- **R-2 Corte de análise por custo** — S8 + CEE-001 §10 S2 + Inversão #1; orçamento avisa/escala, não pula (P-7).
- **R-3 ICT rodando fora da janela ou sem contexto** — S4/S6 + T6; INV-02; divergência RULE-ICT-003 registrada (CONF-3; research CF-3). *[antes: "(C-3)"]*
- **R-4 Horário errado na troca de horário de verão / máquina em outro fuso** — T3 com casos obrigatórios; tabela em NY, não em UTC fixo (research §3.7).
- **R-5 Ciclo perdido ou duplicado após queda** — S10 registro só-inserção; retomada; alarme vencido ⇒ `EXPIRED`.
- **R-6 Aviso duplicado ou fora de ordem do barramento** — transições idempotentes pela tabela fechada; par não listado recusado (D8).
- **R-7 Limiar macro inventado** — P-5: parâmetro; sem valor ⇒ não arma (fail-closed).
- **R-8 Ativos se contaminando** — S1: um ciclo isolado por ativo/missão.
- **R-9 Dupla posse com SPEC-003/009/014/015** — §2 anti-dupla-posse e dono por transição de WF-F02; CONF-1/CONF-2/CONF-4/CONF-5. *[antes: "C-1/C-2/C-4"]*
- **R-10 Plan grande demais** — §3: divisão; P-3.
- **R-11 Persistência indefinida até a SPEC-009** — P-6; requisito declarado; lacuna registrada.
- **R-12 Alarme sem fonte de preço** — L-5; T6 fail-closed: sem Observação de preço, alarme não dispara.
- **R-13 Etapa da hierarquia pulada ou inventada (Fibonacci/Fractal)** — S2: o grafo só despacha nós existentes; posição = P-11 (CF-8).
- **R-14 "Reset" implementado como transição não escrita** — S7/T6: nenhuma seta de volta sem resposta de Andraus (P-12; CF-7).
- **R-15 Inversão #1 sem gatilho observável** — S4: só reage a evento publicado; sem evento ⇒ volta a Andraus (L-8).

---

## 12. Edições a documentos de governança — NÃO executadas

O Especificador **não** edita ROADMAP, CATALOGO, RMR-001, CONFLICT-MAP, WORKFLOW, RULES, atas, AGENTS.md, agentes, canon nem Specs baselined. Após a homologação, cabe ao Orquestrador/Andraus: ata de abertura; ROADMAP §7 (e slot Spec de Tempo + §21/§26, se aceito); CATALOGO; RMR-001 (re-apontamento aditivo do BL-026, se aceito); nota aditiva à SPEC-003 (§8, se aceito); WORKFLOW **só Andraus** (WF-F02 "SPEC-015", se ele decidir alinhar — CONF-1; WF-K02 "SPEC-008/015", se a divisão for aceita e ele decidir alinhar — CONF-5; ramos de WF-F01 × WF-A02/WF-F02 — P-12; posição de Fibonacci/Fractal no pipeline — P-11); **regenerar `docs/MATRIZ-WORKFLOW-SPEC.md`** (não-normativa) após a homologação — linhas WF-K01..K03, WF-A01..A03, WF-R02/R03, WF-D01/D02 (Spec de Tempo, se aceita) e WF-04, WF-F01/F02, WF-T02 (conforme CONF-1/2/4) (research §5). *[antes: "…(WF-F02 'SPEC-015', se ele decidir alinhar — C-1)."]*

**Comandos a rodar (não tenho Bash — para o Orquestrador):**
- `python scripts/backlog_triggers.py --abertura SPEC-008` (esperado: BL-026, BL-043, BL-044, BL-045, BL-046)
- `python scripts/check_repo_research.py specs/features/SPEC-008` e `--all` (esperado OK: 4 elegíveis, 1 não elegível coerente)
- `python scripts/build_map.py` e `--check` (BL-019)
- `python scripts/check_refs.py` · `python scripts/check_doc_sync.py` · `python scripts/check_invariants.py` (informativos)
- `python scripts/pre_entrega.py specs/features/SPEC-008` se aplicável à abertura (protocolo do BL-044)

---

## 13. Perguntas a Andraus (linguagem de trader)

1. **P-1 (peso do despachante).** *Recomendação: tratar a parte que chama os analistas e conduz o ciclo como peça **crítica** (CRITICAL), com testes de ataque.* É ela que decide se o ICT roda, se o SMC é chamado e quando o caso vai para a decisão final; um erro aqui abre caminho de sinal fora do roteiro. **Confirma crítico?**
   > *Nota técnica:* CRITICAL D0–D8 (slot); alternativa HIGH D0–D7 sem suíte D8.
2. **P-2 (dividir em duas).** *Recomendação: separar em **duas** Specs — "Despacho e Ciclo" (SPEC-008) e "Relógio, Killzone e Alarme" (a "Spec de Tempo", número novo — candidato SPEC-050 —, peso alto/HIGH).* Numa só, o plano passa do tamanho máximo que a regra permite revisar de uma vez. O relógio e o alarme mudam por motivos próprios (horários, horário de verão) e não mexem na ordem dos analistas. **Aceita a divisão, o número candidato SPEC-050 e que este mesmo Dossiê valha para as duas?**
   > *Nota técnica:* §3; RULE-ECC-07 (única ≈2.499 > 2.000); alternativas única e três peças; Spec de Tempo em CRITICAL ≈1.491. *[antes: "única ≈2.547 … Spec de Tempo em CRITICAL ≈1.539" — R1-m04]*
3. **P-3 (tamanho da SPEC-008).** *Recomendação: manter "Despacho e Ciclo" como **um documento só**.* A conta dá cerca de **1.895 linhas** — praticamente em cima da linha de alerta (1.900) — e, na pior densidade, **1.932**, já acima do alerta e só 68 linhas abaixo do **teto de 2.000**. Por passar de 1.600, a regra pede sua confirmação. **Aviso:** se o Plan, medido de verdade, passar de 2.000 linhas, ele **não** pode seguir assim — dividir depois de o Plan começar é **nova abertura** (volta a você; o Plan antigo fica congelado). Dividir mais agora partiria coisas que mudam juntas. **Confirma um documento só, ciente desse risco?**
   > *Nota técnica:* RULE-ECC-07 (`RULES.md` l.522-529: alerta 1.900, teto 2.000, >1.600 confirma, gatilho processual); o Plan mede e declara o corpo. *[antes: "A conta dá cerca de **1.900 linhas** (faixa 1.140–1.930), acima de 1.600 — por isso a regra pede sua confirmação. Dividir mais partiria coisas que mudam juntas. **Confirma?**" — nota técnica "l.526-527" — R1-m04]*
4. **P-4 (contrato comum do Manager).** *Recomendação: escrever **antes** do Plan da SPEC-008 um documento curto, o "Manager Contract", que só junta o que você já decidiu sobre o Manager (ator único, três fases, Fase 1 mecânica, nunca executa, nunca corta análise por custo) — sem regra nova —, e homologá-lo junto.* As três Specs do Manager herdam dele. Alternativa: usar a própria ADR do Manager como "pai" agora e escrever o contrato só quando abrir a Fase 0. **Qual prefere?**
   > *Nota técnica:* DHR-EUA-E23 §2 item 2; RULE-HV-01..04; contrato inexistente (research §0 d). Opção rejeitada: contrato dentro da SPEC-008 (irmã viraria mãe).
5. **P-5 (quando a convicção de contexto é "conclusiva").** Para armar o alarme, o Manager precisa saber se a convicção de contexto (Elliott + SMC) basta — e **não existe número decidido** para isso (os 70% e 7/9 são do **sinal**, não do contexto). *Recomendação: **adiar o número** (vai com a calibração, J-001/N-001); a Spec escreve a regra com um limiar a preencher e, enquanto ele não existir, o alarme **não é armado** e o ciclo encerra registrado ("contexto não conclusivo").* Alternativa: você fixa agora um valor-piloto. **Adiar (recomendado) ou fixar um piloto?**
   > *Nota técnica:* WF-04; RULE-CF-010; CC-03/CC-09; J-001 e WF-D03 seguem ABERTAS.
6. **P-6 (onde fica a "memória" do ciclo até a SPEC-009).** *Recomendação: a SPEC-008 mantém o próprio **livro de bordo só-de-acréscimo** (cada passo do ciclo e do alarme), que permite retomar depois de uma queda; os estados do ciclo e do alarme **não** viram estados de objeto no quadro; **como** guardar fica para a SPEC-009.* **Confirma?**
   > *Nota técnica:* G-001 e M-001 seguem ABERTAS; research §3.4, §6 L-3/L-4.
7. **P-7 (orçamento × "nunca deixar de analisar por custo").** *Recomendação: o orçamento do ciclo **avisa e escala** quando estoura; **nunca** pula o Elliott (nem outra etapa com evento estrutural relevante) para economizar; o "botão de parada por gasto" que o documento de economia permite só é apertado **por você**, nunca automaticamente.* **Confirma?**
   > *Nota técnica:* CEE-001 §10 S2 × §9.3 (tensão no canon, não reescrito — CONST-01); Inversão #1.
8. **P-8 (de onde vêm o preço do alarme e a "oportunidade").** *Recomendação: o nível, a direção, a invalidação e a validade do alarme são **copiados** do que os analistas publicaram (hipótese de contexto); a "oportunidade" que libera o SMC é um campo que o Elliott publica. O Manager **nunca** calcula preço nem decide se há oportunidade.* **Confirma?**
   > *Nota técnica:* WF-A01; WF-03; ADR §2.5; requisito às SPEC-010/012 (`[INFERÊNCIA]`).
9. **P-9 (relógio da máquina e mercado fechado).** *Recomendação: a fonte de hora confiável, a tolerância de atraso do relógio e o calendário de feriados/pregão por ativo ficam como **parâmetros a preencher** na construção; sem calendário, a Killzone vale pela tabela e o livro de bordo anota "calendário de mercado não informado" — sem preço, o alarme não dispara de qualquer forma.* **Confirma?**
   > *Nota técnica:* research §3.6, §6 L-6 (pesquisa inconclusiva); WF-P02/N-001.
10. **P-10 (horários das Killzones — BL-026 em pauta).** As fontes de varejo concordam com a sua tabela em Londres, NY PM e London Close, mas **divergem** em duas janelas: **Ásia** (sua tabela 20:00–24:00; há quem use 20:00–22:00) e **NY AM** (sua tabela 07:00–10:00; há quem use 08:30–11:00), sempre em horário de Nova York. Também falta decidir **quais Killzones valem por ativo** e conciliar a **entrada M5** do ICT com a tabela de tempos gráficos. *Recomendação: manter a sua tabela atual como valor-padrão editável e refinar por ativo só depois do backtest; a Spec trata tudo como parâmetro.* **Mantém, ou quer editar algum valor agora (edição sua no WORKFLOW)?**
    > *Nota técnica:* WF-R01..R03; SRC-KZ-LUX-01, SRC-KZ-BTX-01; research §3.7.
11. **P-11 (Fibonacci e Fractal no roteiro) — NOVA (R1-M01).** A hierarquia do SOT é Elliott → **Fibonacci → Fractal** → SMC → ICT, mas o seu roteiro (WORKFLOW) só tem três chamadas: Elliott, SMC (se Elliott viu oportunidade) e ICT (se o alarme tocar). Fibonacci e Fractal não aparecem como etapa — e eles têm Spec própria prevista (SPEC-011). A pergunta é: **o Manager chama o Fibonacci/Fractal como etapa separada, ou isso é trabalho de dentro do analista de Elliott?**
    - **Opção A — etapa separada:** o Manager chama Fibonacci/Fractal logo depois do Elliott e antes do SMC, só quando o Elliott viu oportunidade. Segue a hierarquia ao pé da letra, mas acrescenta um passo que o WORKFLOW não tem (edição sua no WORKFLOW).
    - **Opção B — dentro do Elliott:** o Elliott usa Fibonacci/Fractal na própria leitura (proporções e graus) e publica uma análise só; o Manager não muda. Bate com o WORKFLOW como está; a SPEC-010/011 resolve como os dois conversam.
    - **Opção C — decidir depois:** a SPEC-008 deixa o roteiro como **dado versionado** (dá para acrescentar a etapa sem reescrever a Spec) e a resposta vem na abertura da SPEC-010/011.
    *Recomendação: **C agora, com A como direção provável**:* o Fibonacci publica sub-hipóteses próprias (AGENTS §6.2), o que é coisa de etapa separada; mas não vale travar a SPEC-008 por isso, já que o roteiro é editável. **Atenção:** se Fibonacci/Fractal virar etapa antes da 1ª leitura de convicção, pode-se querer que as dimensões geométrica/fractal entrem nessa leitura — hoje o WORKFLOW (WF-C01) diz estrutural+institucional; isso **não** é mudado aqui (J-001/WF-D03 seguem abertas). **Qual opção?**
    > *Nota técnica:* INV-01/CC-01; ROADMAP §8 (SPEC-011); AGENTS §3.2/§6.2; WF-V02; WF-C01; research §3.2, §6 CF-8.
12. **P-12 (o que é "resetar o alarme") — NOVA (R1-M05).** O WORKFLOW diz "reset do alarme" em dois casos: quando o ICT não confirma a entrada depois do disparo (ramo 3) e quando o alarme vence (ramo 5). Só que a máquina do alarme que você aprovou só anda para a frente: armado → disparado → {usado | vencido | cancelado}; não há "voltar a armado". O mesmo vale para a máquina do ciclo, que só chega a "recusado/vencido" depois do Risco. A Spec **não** pode inventar a volta sozinha.
    - **Opção A — encerrar e, se a ideia ainda vale, ligar um alarme novo:** o alarme velho termina como "usado" (ramo 3) ou "vencido" (ramo 5) e fica no livro de bordo; se a hipótese de contexto continua viva (não foi refutada nem substituída), nasce **um alarme novo**, ligado à **mesma hipótese de origem**, dentro de **um ciclo novo** (o ciclo atual termina registrado; o novo aproveita o contexto já publicado enquanto ele valer). No caso do vencido, o alarme novo só nasce depois de **uma nova leitura de contexto conclusiva**. Usa só os estados que já existem — nada anda para trás.
    - **Opção B — voltar o mesmo alarme para "armado":** exige você acrescentar essa volta no WORKFLOW (WF-A02/WF-F02).
    - **Opção C — "reset" = só encerrar:** o alarme termina e o ciclo acaba; uma nova tentativa só com novo ciclo.
    E, no mesmo tema: **sem oportunidade (ramo 1), NEUTRO (ramo 2), "reset" (ramos 3 e 5), prazo vencido antes do Risco e Fase 2 que decide não enviar** terminam o ciclo em qual estado final — "recusado" ou "vencido"? *Recomendação: Opção **A** para o alarme; e, para o ciclo: ramos 1, 2 e "Fase 2 não envia" → **recusado**; ramo 5 e prazo vencido → **vencido (EXPIRADO)**; ramo 3 → **recusado** — tudo saindo do ponto onde o ciclo está, sem estado novo. Como isso acrescenta setas que o WORKFLOW não escreve, é você quem confirma (e, se quiser, registra no WORKFLOW).* **Concorda?**
    > *Nota técnica:* WF-F01 ramos 1/2/3/5; WF-A02; WF-F02; WF-A03; CHM-001 (estados da hipótese); research §3.3, §6 CF-7; ABERTURA §2 (dono por transição).

**Confirmações (na homologação):** *(renumeradas de `C-n` para `CONF-n` — R1-m02; o conteúdo de CONF-2 e CONF-3 não mudou)*
- **CONF-1 — quem conduz a máquina de estados do ciclo (três versões nos documentos).** O WORKFLOW (WF-F02) diz "Plan do Manager (SPEC-015)" (a Fase 0); o ROADMAP e a ata EUA-E23 põem "FSM do ciclo" na SPEC-008 (a Fase 1); e a proposta EUA-E23 também lista WF-F02 sob a SPEC-014 (a Fase 2). Na prática a máquina atravessa as fases: a Fase 1 toca o ciclo até entregar o caso à síntese; daí em diante quem decide é a Fase 2 e, depois, o Risco. *Recomendação: **dono por trecho** — a SPEC-008 escreve a tabela inteira da máquina (uma só, para não haver duas versões) e conduz de "aguardando" até "em síntese"; a SPEC-014 conduz de "em síntese" em diante; o Risco conduz "em risco"; a SPEC-015 (Fase 0) só cria o pedido de ciclo. A passagem de um trecho para outro é um aviso publicado no quadro. Se quiser, você ajusta o texto "SPEC-015" do WORKFLOW depois.* **Confirma?**
  > *Nota técnica:* WF-F02; ROADMAP §7; DHR-EUA-E23 §2; EUA-E23 PROPOSTA l.113/l.115; ABERTURA §2 "Dono por transição de WF-F02"; research §6 CF-1. *[antes: "**C-1 — quem conduz a máquina de estados do ciclo.** O WORKFLOW (WF-F02) diz 'Plan do Manager (SPEC-015)'; o ROADMAP e a ata EUA-E23 põem 'FSM do ciclo' na SPEC-008. *Recomendação: a SPEC-008 conduz a máquina (é mecânica), citando WF-F02 por ID; se quiser, você ajusta o texto do WORKFLOW depois.* **Confirma?**" — dois lados só (R1-M04)]*
- **CONF-2 — a 1ª leitura de convicção.** *Recomendação: a SPEC-008 pede a leitura macro e aplica a regra "conclusiva?"; a arbitragem entre analistas é da Fase 2 (SPEC-014).* (RULE-CF-010 × EUA-E23 §4; research CF-2) **Confirma?**
- **CONF-3 — ICT fora da Killzone.** A regra antiga RULE-ICT-003 aceita entrada fora da Killzone com convicção reduzida; o seu WORKFLOW (WF-A02/WF-05) só aceita disparo **dentro** da janela. *Recomendação: a SPEC-008 segue o WORKFLOW; a divergência fica registrada para quando a Spec do ICT (SPEC-013) abrir.* (research CF-3) **Confirma?**
- **CONF-4 — conferir se o setup do ICT está na direção do contexto.** *Recomendação: a SPEC-008 faz essa conferência por regra fixa (direção igual ou não) antes de passar à Fase 2; desalinhado = sem entrada e o alarme segue a resposta da P-12 (WF-T02, WF-F01 ramo 3).* (A MATRIZ, que não é norma, põe WF-T02 na SPEC-013.) **Confirma?** *[antes: "C-4 … desalinhado = sem entrada e o alarme é resetado (WF-T02, WF-F01 ramo 3)." — "resetado" dependia de transição inexistente (R1-M05)]*
- **CONF-5 — quem abre e fecha a Killzone, se a divisão for aceita — NOVA (R1-M03).** O WORKFLOW (WF-K02) diz que o dono do abrir/fechar é o "Manager/Scheduler (SPEC-008/015)". Com a divisão, essa regra fica escrita na Spec de Tempo. **Quem abre e fecha continua sendo o Manager** — muda só o documento onde a regra mora. *Recomendação: aceitar; você, se quiser, troca o número entre parênteses no WORKFLOW depois; o mapa WORKFLOW→Spec (MATRIZ, não-normativo) é refeito pelo Orquestrador.* **Confirma?**
  > *Nota técnica:* WF-K02; ABERTURA §3 e T4; research §5 (lente 3 refeita) e §6 CF-6.

> Nenhuma decisão aberta é fechada (CONS-01): J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03 e D-PCC-4 seguem abertas. P-11, P-12, CONF-1 e CONF-5 tocam texto do `WORKFLOW.md`: o Especificador **não** o edita e **não** cria estado nem transição; só Andraus decide e edita.

---

## 14. Próximo passo
`research.md` + `sources/` + esta Proposta seguem para **parecer do Revisor** sobre o processo do Dossiê (RULE-ECC-02/04/05/06/07; não incidência de CC-12; disposições do backlog; conflitos registrados) e, depois, **homologação de Andraus** (P-1..P-12, CONF-1..CONF-5, fronteira, divisão e Classe orientativa) *[antes: "P-1..P-10, C-1..C-4"]* — **antes** de qualquer `plan.md`/`checks.md`.

---

## 15. Autopré-check (PEP-001 §7) — resumo

- [x] ROADMAP lido (§7 slot SPEC-008/009; §9 SPEC-014/015; §21; §23 passo 1-bis; decisões abertas/fechadas; EUA-E21/E23). Slot **indicativo, não aberto**; abertura ordenada (2026-11-07).
- [x] atomic-spec §15 lido (Dossiê, verbatim, multi-lente, repositórios, dimensionamento).
- [x] Dossiê presente e completo — RULE-ECC-02 (questões, fontes classificadas `[EXTERNO]`, adotar/adaptar/rejeitar/adiar, lacunas, escopo, re-apontamento).
- [x] Captura verbatim por fonte carregada (14 SRC) — RULE-ECC-04; citações no Dossiê copiadas das capturas.
- [x] "Pesquisa em repositórios" com régua Equilibrada (4 elegíveis, 1 não elegível; nenhum adotado como motor) — RULE-ECC-06.
- [x] Multi-Lente (RULE-ECC-05): Arquitetura + Escola (ICT/Killzone; risco-retorno declarado não pertinente) + WORKFLOW por ID, com divergências registradas.
- [x] Estimativa de tamanho com derivação; teto ultrapassado na Spec única ⇒ divisão proposta antes do Plan — RULE-ECC-07.
- [x] Classe orientativa (D + C; zero H/P); pisos E1/E2/E3; fail-closed na trava E3.
- [x] Nenhum invariante violado (INV-01/02/04/05/06/07/09; hierarquia; Conviction Vector intocado; SOT não executa).
- [x] CONS-01: nenhuma decisão aberta usada como fechada (§10, §13); pontos novos que dependem de Andraus marcados como pergunta (P-11, P-12, CONF-5), não como invariante.
- [x] Backlog: 5 itens vinculados com disposição proposta; nada promovido.
- [x] Nada editado fora de `specs/features/SPEC-008/`; nenhum Plan/checks escrito; nenhum artefato inventado (o número da Spec de Tempo é só **proposta**, candidato SPEC-050).
- [ ] Gates do Orquestrador (`backlog_triggers --abertura`, `check_repo_research`, `build_map`, `check_refs`, `check_doc_sync`) — pendentes (sem Bash).
- [x] "VERIFY" não apresentado como CONFORME nem homologação.
- [x] **R2:** achados classe O do parecer R1 (M01–M05; m02, m04–m07) tratados — mapa em §16; R1-m01/m03 (FICHA-M do Orquestrador) não tocados, salvo a troca de prefixo `C-4`→`CF-4` exigida por R1-m02 na mesma linha; nenhum estado/transição criado; WORKFLOW não editado; nenhuma decisão aberta fechada; perguntas novas P-11, P-12, CONF-5 e CONF-1 reescrita.
- [ ] Linha `GATE-D:` com o SHA256-ALVO da R2 — do Orquestrador (parecer R1 §4).

**Pronto para revisão.**

---

## 16. Resposta ao parecer R1 (2026-11-07)

| Achado | Sev. | O que foi feito | Onde |
|---|---|---|---|
| **R1-M01** Fibonacci/Fractal fora do despacho | Média | Mapa nível a nível de INV-01; lacuna WORKFLOW × hierarquia registrada; pergunta a Andraus com 3 opções e recomendação (C agora, A provável); risco R-13 | ABERTURA S2, R-13, P-11; research §3.2, §5 (WF-02/03), §6 CF-8, §7 |
| **R1-M02** Re-apontamento da SPEC-003 por amostra | Média | Grep exaustivo de `SPEC-008\|SPEC-015\|Scheduler` em plan/research/checks: 37 linhas classificadas (RE 9 · HIST 5 · FICA 23); regra de busca proposta para a ata (padrão Q-7 da SPEC-048) com tratamento do histórico de versões/rodadas (não editado, listado) | research §8.3 (tabela + regra); ABERTURA §8 |
| **R1-M03** WF-K02 nomeia SPEC-008/015 dona da Killzone | Média | Lente 3 refeita por busca de número no WORKFLOW e na MATRIZ; conflito CF-6 registrado; confirmação nova a Andraus; incluído em §12 (WORKFLOW só Andraus; MATRIZ regenerada pelo Orquestrador) | ABERTURA T4, §12, CONF-5; research §5 (linha WF-K01..K03 + "Lente 3 refeita"), §6 CF-6, §7 |
| **R1-M04** Dono da FSM após `EM_SÍNTESE` | Média | Tabela de dono **por transição** de WF-F02 com evento de interface; conflito de três lados (WORKFLOW SPEC-015 × ROADMAP/DHR SPEC-008 × EUA-E23 PROPOSTA SPEC-014); setas não literais remetidas a P-12 | ABERTURA S7, §2 "Dono por transição de WF-F02", CONF-1; research §5 (WF-F01/F02), §6 CF-1, §7 |
| **R1-M05** "Reset" × FSM fechada WF-A02 | Média | Registrado como ambiguidade do WORKFLOW; pergunta com 3 opções (recomendação A: encerrar + alarme novo ligado à mesma hipótese-origem, só estados existentes) e destino final dos ramos 1/2/3/5; CONF-4 deixa de dizer "resetado"; nenhum estado novo | ABERTURA S7, P-12, CONF-4, R-14; research §3.3, §5 (WF-A01..A03), §6 CF-7 |
| R1-m01 | Menor | Aplicado pelo Orquestrador (FICHA-M) — não tocado (só o prefixo `C-4`→`CF-4`, por R1-m02) | research §0 (g) |
| **R1-m02** IDs `C-n` homônimos | Menor | Conflitos do research → `CF-n`; confirmações da ABERTURA → `CONF-n`; todas as referências cruzadas atualizadas; legenda de prefixos | cabeçalho; S6, S7, Non-goals, R-3, R-9, §12, §13, §14; research §0 (g), §5, §6, §7 |
| R1-m03 | Menor | Aplicado pelo Orquestrador (FICHA-M) — não tocado | ABERTURA §1 |
| **R1-m04** Faixa × alerta; ajuste de errata | Menor | Ajuste de errata coerente (−48 onde não há errata: Spec única e Spec de Tempo; errata só no Plan da SPEC-008); centrais refeitas (única ≈2.499; Tempo CRITICAL ≈1.491); faixa **e** central comparadas ao alerta e ao teto; P-3 avisa do teto 2.000 e do gatilho de nova abertura | ABERTURA §3, P-2 (nota), P-3; research §8.2 |
| **R1-m05** Inversão #1 sem evento | Menor | Evento declarado: transição `DOMINANT → REFUTED/SUPERSEDED` (CHM-001 l.753-754) publicada no quadro e avisada pelo barramento `[INFERÊNCIA]`; lacuna L-8 se não existir; risco R-15 | ABERTURA S4, R-15; research §3.5, §6 L-8 |
| **R1-m06** Nota `[INFERÊNCIA]` promovida a fato normativo | Menor | Linha #1 da tabela = FATO NORMATIVO; nota de integração = INFERÊNCIA; assumir a mecânica aqui = `[PROPOSTA]` | research §0 (h); ABERTURA S4 |
| **R1-m07** Visibilidade: BL-003 e Specs 006/007/048 | Menor | Varredura de `ATIVADO` (BL-003 e BL-011; BL-003 toca a P-6, já encaminhado, não absorvido); montante com SPEC-007/048 (interfaces com linhas) e SPEC-006 (sem citação direta) | ABERTURA §9, §10; research §0 (i) |

Perguntas novas ou alteradas para Andraus: **P-11** (nova), **P-12** (nova), **CONF-5** (nova), **CONF-1** (reescrita, três lados), **CONF-4** (ajuste do "reset"), **P-3** (aviso do teto), **P-2** (números da nota técnica).
