# Parecer do Revisor — Plan da SPEC-008 v1.0 — R1 — 2026-11-08

> Transcrição pelo Orquestrador do retorno do Revisor SOT (somente leitura; classe S3, âncora `plan.md`). **NÃO CONFORME (0 Críticas, 5 Médias, 8 Menores)**, recuperável. Objeto: `specs/features/SPEC-008/plan.md` v1.0 (commit `55d0989`, SHA256-ALVO `1cfca7637c85…`) + `checks.md`.

RELATÓRIO DE REVISÃO — SPEC-008 Plan v1.0 (candidata) — 2026-11-08 — Revisor de Especificação SOT — Rodada R1

MODO: integral · SHA256-ALVO: 1cfca7637c85a9e013374953de4cdb19219f07f5a4964dfdfa6ef4fc9f0a96f9 (é o valor que o Orquestrador enviou; não consigo calcular o hash sem Bash)
Limites: só leitura, sem Bash, sem git e sem web. Não rodei nenhum script. Não verifiquei a ordem "Avançar", que só existe no chat. Não atesto a veracidade das fontes `[EXTERNO]` nem das capturas em `sources/`.

## Veredito: NÃO CONFORME (5 Médias, 0 Críticas, 8 Menores)

O Plan está bem construído e honesto quanto às decisões abertas. Mas a máquina de estados e a trava E3 têm lacunas que dá para provar com as próprias fontes, e o Plan não atende uma exigência de fronteira de uma Spec já homologada (SPEC-048). Mesmo sem as Médias, o teto seria CONFORME condicional (gate não rodado nesta sessão; J-001/N-001/G-001/M-001 abertas).

## 1. Objeto
- Artefato: `specs/features/SPEC-008/plan.md` v1.0 + `checks.md`
- Classificação: CRITICAL, alvo D0–D8, FASE 4, maturidade L3
- A jusante de SPEC-003/004/005 e do MMC-001 v1.0 (todos BASELINE)

## 2. Passo 0 — alinhamento
- **ROADMAP.md** (linha da tabela da SPEC-008): abertura homologada; "Plan pendente, só por ordem de Andraus". A ordem "Avançar" de 2026-11-08 não está registrada no repositório — **não verificável**; cabe à ata do Plan citá-la.
- **atomic-spec**: método vigente confirmado.
- **RMR-001**: nenhum item `ATIVADO` que vincule à SPEC-008.
  - Os gatilhos de BL-026/043/044/045/046 citam `spec:SPEC-008 em redação`.
  - As Disposições do Plan são idênticas às da ABERTURA §9 (PARCIAL / FORA / REFERÊNCIA ×3).

## 3. Gate determinístico
- **GATE NÃO VERIFICADO na minha sessão.** O pedido traz os resultados (`validate_spec_sot.py` 14/14, `revisor_gate` = PASSOU_D, 0 sinais H, `pre_entrega` sem vermelhos), mas não no formato canônico.
  - Falta a linha `GATE-D: … | cmd: … | SHA256-ALVO: … | data:`, então não posso conferir o sha.
  - Pelo §3 isso é falha fechada: teto CONFORME condicional.
- **Falsos positivos de `contagens_declaradas`** (l.41 e l.171): conferi e não escondem divergência real.
  - "~6 ECs" é a estimativa da ABERTURA §3 l.127.
  - O Plan declara 8 EC-MDC de forma consistente: l.44, `checks` l.10, Escala E0–E3 e Autopré-check l.1612. Há de fato 8 cabeçalhos `### EC-MDC-` (l.1306..1403).
  - "§10.3 (Enforcement Contract)" na l.171 é só a seção do atomic-spec.

## 4. Pontos para o Especificador provar (correspondem aos achados)
1. Em que linha da D5 a Spec trata `ALARM_CANCELLED`/`ALARM_EXPIRED` em `ATIVADO`? E com que guarda a hipótese de contexto ainda é elegível quando o setup chega? (M-01)
2. Como se reconcilia a tentativa nova do mecanismo macro (RULE-MDC-005 (e) + 003 (f)) com "uma invocação por ciclo" (005 (a); ADV-06)? Em que linha da D5 ficam falha de publicação, erro do agente analítico, erro do mecanismo macro e aviso de voltas? (M-02)
3. Qual campo do CCM-001 (`global_conviction` ou `score`) é comparado com θ? (M-03)
4. Onde está o orçamento de tempo/`budget_ref` que a SPEC-048 exige da SPEC-008? (M-04)
5. Onde está, na D4.2, a conferência de capacidades "antes de cada ação"? Em que registro vivem `model_calls` / `external_emissions` / `foreign_publications` / `clock_reads`? (M-05)

## 5. Passos de revisão
- **Passo 2 — Invariantes: PASS.**
  - Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT: postos 1/2/3/4/5 em RULE-MDC-002 (a)(c).
  - ICT não cria hipótese: F18 e ADV-08.
  - Custo fora da convicção: RULE-MDC-008 (d).
  - SOT não executa: INV-MDC-01 e RULE-MDC-011 (d).
  - NEUTRO conferido antes do limiar: F07 e F08a.
  - R:R não é tocado (fica na RISK-SPEC).
  - Dimensionalidade 8 intocada.
- **Passo 3 — Constitution Check: PASS**, com 1 Menor de âncora (m-01).
- **Passo 4 — Rastreabilidade: PASS**, com Menores (m-02, m-05).
  - Conferi RULE-BB-003 em RULES.md l.318-321: o texto "Hipótese só é base de decisão em ACTIVE ou DOMINANT" bate literalmente.
- **Passo 4-ter (M1–M5): tabela "conferido e OK" abaixo.**
- **Passo 5 — BASpec e profundidade: PASS** na forma.
  - 12 BASpecs completas, D4 com exemplo, D5 em tabela, D6 presente, D8 com 14 ADV.
- **Passo 5-bis**
  - Bloco A: preenchido para as 12 BASpecs; os casos de negação são plausíveis.
  - Bloco B: preenchido; a tabela "Conservação do pai" cobre todos os itens do §8.2-bis (inclusive as 9 linhas do §4 e o §6.6 nas duas partes). Nenhuma supressão silenciosa.
    - MMC §6.2 / Inversão #1 ("desperta análise completa") fica parcialmente atendida e honestamente escalada como DN-2. Não é herança silenciosa.
  - Adversarial próprio:
    - BASpec-012 (E3): ENTÃO não detectável pelos registros especificados → M-05.
    - BASpec-006/011: QUANDO satisfeito com hipótese de contexto já REFUTED → M-01.
  - Bloco C, por disciplina:
    - EPI: 1 ponto — o campo agregado é escolhido sem âncora (M-03).
    - CAU: sem achados (só causalidade de regra).
    - DEC: nenhuma BASpec cruza para a execução.
    - SEM: m-08.
    - ONT, INQ, CTF, UNC, PRB e MET: verificados sem achados (INDETERMINADO com abstenção, sem probabilidade, nenhum despacho/registro afirmado sem ocorrer).
- **Passo 6 — EARS e 4Es: PASS.**
- **Passo 7 — Enforcement: FAIL** (M-05; m-07).
  - Pisos conferem com a Escala E0–E3.
  - Falso-DENY amostral com referência independente: ADV-10 (k) e EC-MDC-008.
- **Passo 8 — Decisões: PASS.**
  - CONS-01 íntegro: J-001/N-001 abertas e θ sem número; os limiares-piloto 70% / 7-9 explicitamente não são θ.
  - DN-1/2/3 estão como `[DECISÃO NECESSÁRIA]` sem o Plan decidir.
  - CF-A, CF-B e CF-C estão registrados e não resolvidos. Conferi CF-A no CCM-001 l.28 ("invocável pelo Manager Agent — Fase 2").

## Conferido e OK (fonte aberta nesta sessão)
- **E-3 confirmado.**
  - Grep de "SPEC-008" em `SPEC-002`, `SPEC-006` e `SPEC-020` (todos os arquivos): 0 ocorrências.
  - A linha do BL-017 (RMR-001 l.124) não cita SPEC-008.
- **E-1 confirmado.**
  - As 9 linhas RE existem com o texto literal: plan 46/98/191/224/1149; research 129/183/300/301.
  - Grep de "SPEC-008/015" na SPEC-003 dá 11 ocorrências = 9 RE + 2 HIST (plan 33; checks 63), como diz o `checks` §1 #6.
  - As 5 HIST (plan 30/33; checks 40/54/63) estão certas.
- **E-2:** o gatilho antigo de BL-026 bate com o RMR-001 l.133.
- **Contagens do `checks.md` l.10:** 1/11/13/12/8/20/14 = 79, todas nas linhas declaradas. Corpo de 1.626 linhas; as diferenças −274 e −269 conferem.
- **`checks` l.19:** as 17 linhas DN-1 conferem uma a uma.
- **D5:** 30 linhas (F01..F29 com F08a/F08b); nenhuma seta para `ARMADO` a partir de `ATIVADO` ou ENC; sem "reset".
- **CHM-001 l.753-754:** transições DOMINANT→REFUTED e DOMINANT→SUPERSEDED.
- **SPEC-004 RULE-CBP-001/002/005/006/009/014 e SPEC-005 RULE-CEB-001/003/004/006/007/008/010** existem e dizem o que o Plan atribui.
- **WORKFLOW** WF-01/02/03/04/05/A01/A02/A03/F01/F02/R01/T02/K04/D03 conferem com o uso, salvo m-05. WF-R01 tem mesmo `position` com entrada "—", o que sustenta o CF-B.
- **DHR-SPEC008-001:** P-1..P-13 e CONF-1..5 incorporados como estão; §3 (ii) cumprido; a lista de abertas do §5 está reproduzida.
- **MMC-001:** §3.1.3 (só a parte firme é obrigação), §8.2-bis e §10 lidos; o Plan os respeita.

## 6. Achados

**MÉDIAS**

**M-01 [C10] Falta tratar alarme cancelado ou vencido depois do disparo** (D5 F15/F16; RULE-MDC-006 (d)(g); Interface T-3)
- Pelas fontes, o alarme pode morrer depois do disparo:
  - WF-A02: `TRIGGERED → {CONSUMED | EXPIRED | CANCELLED}`.
  - WF-A03: cancelamento automático se a hipótese de origem passa a SUPERSEDED/REFUTED.
- No Plan, `ALARM_CANCELLED`/`EXPIRED` só existem em `ARMADO` (F15). Em `ATIVADO` caem em F29 (sem transição).
- O alinhamento (006 (d)) não reconfere a elegibilidade (006 (a)) quando o setup chega.
- Efeito: um setup alinhado a uma hipótese já REFUTED pode passar a `EM_SÍNTESE` e ser entregue à Fase 2.
- O mesmo vale para `CONTEXTO_FORMADO` antes de `ALARM_ARMED` (só o timer resolve).
- Ação: incluir as linhas `ATIVADO × ALARM_CANCELLED/EXPIRED` (ENC, com código e ramo) e a guarda de elegibilidade na hora do setup (F16), com cenário e ADV.

**M-02 [C10/C01] Caminhos de falha fora da máquina de estados e contradição na tentativa nova** (RULE-MDC-003 (f), 005 (a)(e); D4.3; D5; `checks` §5)
- Contradição: 005 (e) manda tratar erro do mecanismo macro como "falha seguida" com nova tentativa (003 (f)), mas 005 (a) recusa a segunda invocação (`MDC_MACRO_ALREADY_INVOKED`), e o ADV-06 testa só "CV1 já lido".
- Não há evento nem linha na D5 para:
  - falha de publicação do `dispatch_request`;
  - erro do agente analítico;
  - erro do mecanismo macro;
  - aviso de voltas esgotadas (T15 (b)) — além disso, a D4.3 diz que `rounds` não é contado pelo Manager.
- A espera depois de F06 (resultado macro) não tem timer. Isso viola RULE-MDC-009 (e) ("nunca espera sem timer"), e a Interface `STAGE_TIMER` não lista F06.
- O `checks` §5 marca ✔ "toda ação de efeito mapeia numa linha", o que é falso para a tentativa nova.
- Ação: definir o que é "invocação" (pedida ou concluída); incluir eventos, linhas da D5 e timers dessas falhas; corrigir o `checks` §5.

**M-03 [C02/C08] Campo comparado com θ não identificado** (RULE-MDC-005 (c)(d); D4.4; F07/F08b)
- O CCM-001 Cap.3 l.61 e o esquema l.96-97 têm dois agregados: `global_conviction` e `score`.
- A nota do CCM-001 l.66 marca como `[DECISÃO NECESSÁRIA]` "sobre qual valor o gate opera" (BL-029).
- O Plan adia o nome do campo para "a construção". Assim o gate Classe D fica sem objeto definido, e a escolha seria feita no BUILD sem Andraus.
- O Plan também não diz o que faz com `gate_result`/`thresholds_used` (que vêm com os limiares-piloto) no resultado macro.
- Ação: nomear o campo com `[INFERÊNCIA]` e âncora no CCM-001, ou abrir uma DN; declarar que `gate_result` é ignorado na leitura macro; citar o BL-029.

**M-04 [C04, fronteira M4] Orçamento de tempo e de latência exigido pela SPEC-048 não representado**
- A SPEC-048 v1.4 é BASELINE (DHR-SPEC048-002). Ela diz:
  - l.1158: "SPEC-008: fornecer orçamento (rodadas, tempo) no pedido";
  - l.1167: `budget_ref (SPEC-008)`;
  - l.319/376/449: orçamento de recursos e de latência = SPEC-008 (e SPEC-043).
- No Plan:
  - o `dispatch_request` só traz `max_rounds`, sem tempo nem `budget_ref`;
  - a tabela de parâmetros dá a latência como dona da SPEC-005;
  - a seção "Requisitos a outras Specs" omite SPEC-007 e SPEC-048;
  - RULE-MDC-008 (a) iguala `max_rounds_per_agent` a `max_retrieval_rounds` sem etiqueta `[INFERÊNCIA]`.
- Isso contradiz o próprio Dossiê (research §8.3 l.266: orçamento e latência "FICA" na SPEC-008).
- Ação: representar o orçamento de tempo no pedido (ou registrar a divergência como conflito), reconciliar o dono da latência com SPEC-005 RULE-CEB-010 e SPEC-048, e etiquetar a equivalência.

**M-05 [C05/C01] Trava E3 sem registro que prove a execução** (INV-MDC-01; BASpec-MDC-012; EC-MDC-008; D4.2; contrato lógico)
- INV-MDC-01, BASpec-012 e EC-008 mandam conferir o registro de capacidades "antes de cada ação" (`capability_check_ref` por ação). A D4.2 (passos 0–9) não tem essa conferência; ela só aparece na D4.1, no pedido.
- O POSTCOND/EVIDENCE do EC-008 e os ADV-10/11/14 usam `model_calls`, `external_emissions`, `foreign_publications` e `clock_reads`. Esses contadores não são campo de nenhum objeto do contrato (`counters{steps, failures[]}` apenas), e o Plan não diz que fonte os produz.
- É exatamente a lição C05, e o `checks` §1 #13 marca ✔ sem esse lastro.
- Ação: pôr a conferência por ação na D4.2 e declarar o registro ou observador (campo do contrato ou requisito ao runtime/SPEC-040) que produz cada contagem.

**MENORES**
- **m-01 [C07]** CC-04 (l.123) cita "RULE-MDC-005 (c)" para o NEUTRO; o certo é (b). — FICHA-M
- **m-02 [C04]** O INHERITS (l.160-164) omite RULE-BB-003 (usada em 006 (a)) e RULE-CEB-003 (usada em 003 (g) e 010 (e)). — FICHA-M
- **m-03 [C02]** "agente" sem qualificador na l.1112 (T15) e na l.525. — FICHA-M
- **m-04 [C06]** E-1 (l.1507) diz "23 ocorrências", mas são as 23 linhas FICA da busca mais ampla do research §8.3, não ocorrências de "SPEC-008". — FICHA-M
- **m-05 [C07]** WF-P01 só diz que BTC, XAU e NASDAQ operam em paralelo. O isolamento "um ciclo aberto por (ativo, missão)" é proposta do próprio Plan, mas RULE-MDC-001 (d) e a tabela WORKFLOW (l.253) o atribuem a WF-P01. Etiquetar como `[PROPOSTA]`. (Vai ao Especificador.)
- **m-06 [C01]** ADV-05 (b) e ADV-07 esperam `MDC_TRANSITION_NOT_LISTED`, mas o passo (2) da D4.2 ("confere com o nó/pedido") pegaria antes um evento de Tempo sem pedido, dando `MDC_EVENT_FOREIGN_CYCLE`. Fixar a ordem ou o código esperado.
- **m-07 [C05]**
  - BASpec-MDC-009 está em [E1], mas inclui encerramento por STOP (mudança de estado, E2 no EC-003).
  - O aviso "pendente" do EC-007 não tem `entry_type` na lista de marcações.
  - A invocação macro (capacidade 4 da allowlist) não tem EC próprio: a matriz liga 005 ao EC-003, que é de transição.
- **m-08 [C02]** `rule_id` aparece como ID de RULE em RULE-MDC-010 (a)(d) e como "linha F-nn" no EC-003 e no Bloco A. Definir um só sentido ou criar dois campos.

## 7. Encaminhamento
Devolver ao Especificador (classe O) M-01..M-05 e m-05..m-08. O Orquestrador aplica a FICHA-M (m-01..m-04). Nova rodada pode ser por delta; M-01/M-02 tocam D5, D4 e cenários — revisar os dependentes inteiros.

Anexo A, resumido. Condição para nova revisão:
- M-01: linhas e guarda na D5 + cenário.
- M-02: tentativa nova definida, sem contradição, falhas na D5 e timer em F06.
- M-03: campo nomeado com âncora, ou DN aberta.
- M-04: orçamento de tempo/`budget_ref` representado ou conflito registrado; dono da latência reconciliado.
- M-05: conferência por ação na D4.2 e fonte declarada de cada contagem do EC-008.

<!-- ACHADOS-ESTRUTURADOS
M-01|MEDIA|C10|ATIVADO sem linha para ALARM_CANCELLED/EXPIRED (WF-A02/A03) e sem reconferir elegibilidade da hipótese no setup|cruzar estados da FSM do objeto vizinho (alarme) com cada estado do ciclo antes de fechar D5
M-02|MEDIA|C10|falhas (publicação, agente, mecanismo macro, voltas) e tentativa nova sem linha na D5; 005(a) x 005(e) contraditórias; F06 sem timer|para cada FAILURE-MODE com "nova tentativa", exigir evento+linha D5+timer e conferir contra regra de cardinalidade
M-03|MEDIA|C02|campo comparado com θ adiado para construção; CCM-001 tem global_conviction e score e marca a entrada do gate como DECISÃO NECESSÁRIA (BL-029)|todo gate D nomeia o campo de entrada com âncora no esquema herdado ou vira DN
M-04|MEDIA|C04|SPEC-048 baseline exige orçamento (rodadas, tempo)/budget_ref da SPEC-008; Plan omite e atribui latência à SPEC-005|varrer "SPEC-0nn:" nas seções Requisitos das Specs baselined que citam a Spec em redação (M4) antes da entrega
M-05|MEDIA|C05|trava E3: conferência por ação ausente na D4.2; contadores model_calls/external_emissions/foreign_publications/clock_reads sem campo nem fonte|todo POSTCOND/EVIDENCE de EC só usa campos do contrato lógico ou fonte declarada
m-01|MENOR|C07|CC-04 cita 005(c) para NEUTRO; é 005(b)|conferir alínea citada contra a regra
m-02|MENOR|C04|INHERITS omite RULE-BB-003 e RULE-CEB-003 usadas no corpo|Grep RULE-* do corpo contra a lista INHERITS
m-03|MENOR|C02|"agente" sem qualificador (l.525, l.1112)|Grep "agente " sem "analítico/de Risco"
m-04|MENOR|C06|"23 ocorrências" são linhas FICA da busca ampla, não ocorrências|contagem nomeia a unidade e o padrão de busca
m-05|MENOR|C07|isolamento por (ativo, missão) atribuído a WF-P01, que só diz paralelismo entre ativos|atribuição a WF-xx só com o texto literal; acréscimo = [PROPOSTA]
m-06|MENOR|C01|ADV-05(b)/ADV-07 esperam TRANSITION_NOT_LISTED, mas o passo (2) da D4.2 daria FOREIGN_CYCLE|simular a ordem da D4.2 para cada cenário negativo
m-07|MENOR|C05|BASpec-009 E1 com ENC; notice pendente sem entry_type; invocação macro sem EC|cada capacidade da allowlist tem EC; nível da BASpec ≥ nível dos efeitos que contém
m-08|MENOR|C02|rule_id = ID de RULE x linha F-nn|um campo, um sentido
-->

<!-- FICHA-M {"achados":[
{"id":"m-01","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"`directional_conflict = true` ⇒ NEUTRO — RULE-MDC-005 (c))","novo":"`directional_conflict = true` ⇒ NEUTRO — RULE-MDC-005 (b))","condicao":"Grep 'NEUTRO — RULE-MDC-005 (b))' = 1 na linha do CC-04"},
{"id":"m-02a","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"RULE-BB-001/002/004/005; RULE-DEC-01; RULE-MET-01/02","novo":"RULE-BB-001/002/003/004/005; RULE-DEC-01; RULE-MET-01/02","condicao":"INHERITS contém RULE-BB-003 (usada em RULE-MDC-006 (a))"},
{"id":"m-02b","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"RULE-CEB-001 (envelope), RULE-CEB-004 (consumo","novo":"RULE-CEB-001 (envelope), RULE-CEB-003 (cursor/replay), RULE-CEB-004 (consumo","condicao":"INHERITS contém RULE-CEB-003 (usada em RULE-MDC-003 (g) e 010 (e))"},
{"id":"m-03a","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"(b) agente devolve aviso de voltas esgotadas","novo":"(b) agente analítico devolve aviso de voltas esgotadas","condicao":"Grep 'agente devolve' = 0"},
{"id":"m-03b","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"Cada despacho grava POR QUE este agente rodou agora","novo":"Cada despacho grava POR QUE este agente analítico rodou agora","condicao":"Grep 'POR QUE este agente analítico' = 1"},
{"id":"m-04","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"As outras 23 ocorrências (invocação","novo":"As outras 23 linhas FICA do research §8.3 (invocação","condicao":"Grep '23 ocorrências' = 0 no plan.md"}
]} -->

Arquivos: /home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/plan.md · /home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/checks.md · /home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-048/plan.md (l.1158, l.1167) · /home/user/Sistema-Operacional-de-Trading--SOT/canon/CCM-001-canonical-conviction-model.md (l.61, l.66, l.96-97) · /home/user/Sistema-Operacional-de-Trading--SOT/WORKFLOW.md (WF-A02, WF-A03, WF-P01)

## Adendo G1/G2 (guarda pós-revisor, DHR-AUDITOR-EXTERNO-018)
**G2 (gate de código):** o Orquestrador rodou `python scripts/revisor_gate.py specs/features/SPEC-008/plan.md` sobre o mesmo SHA256 do parecer: **VEREDITO D: PASSOU_D**, sinais H: 0; `validate_spec_sot.py` 14/14 PASS; `pre_entrega` 0 bloqueantes. Linha canônica: `GATE-D: PASSOU_D | cmd: python scripts/revisor_gate.py specs/features/SPEC-008/plan.md | SHA256-ALVO: 1cfca7637c85a9e013374953de4cdb19219f07f5a4964dfdfa6ef4fc9f0a96f9 | data: 2026-11-08`. Nenhum achado do gate a confirmar ou descartar (0 sinais); as 3 verificações informativas do repositório inteiro apontam para outros arquivos. O gate PASSOU_D não cobre as 5 Médias (são semânticas: C10/C05/C04/C02).
**G1 (atomic-spec.md):** aberto pelo Orquestrador (Grep). As afirmações do parecer que dependem dele conferem: §10.2 Escala E0–E3 (l.226) — pisos de nível; ENF-04 fail-closed em efeito irreversível (l.270) e ENF-07 falso-DENY amostral da unidade E3 (l.273) — base da Média M-05; CC-11 (l.292) — Classe por BASpec, Classe C compatível com o nível de risco. Nada muda no veredito. O Revisor registrou o atomic-spec como 'método vigente confirmado'.
