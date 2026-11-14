# Parecer do Revisor — Plan da SPEC-008 v1.1 — R2 — 2026-11-14

> Transcrição pelo Orquestrador do retorno do Revisor SOT (somente leitura; classe S3, âncora `plan.md`). **NÃO CONFORME (0 Críticas, 2 Médias, 11 Menores)**, recuperável. Objeto: `specs/features/SPEC-008/plan.md` v1.1 (commit `366af09`, SHA256-ALVO `a198b8e619b6…`) + `checks.md` + `HISTORICO.md`.

TOKENS: 276350  <!-- tokens NOVOS (in+out+cache criado) do Revisor nesta rodada, via `telemetria_tokens.py tokens a0d4dbf69a6a3ce09` (DHR-TELEMETRIA-002); cache lido à parte -->
RELATÓRIO DE REVISÃO — SPEC-008 Plan v1.1 (candidata) — 2026-11-14 — Revisor de Especificação SOT — Rodada R2

MODO: integral (82 de 126 blocos alterados, mais da metade, então a regra do §3-bis.6 manda revisão integral; usei o delta só para priorizar as 5 Médias)
SHA256-ALVO: a198b8e619b6cd8c4b9b5b70048a8ab14a28b2f1284734c365b2e32f2867072e (valor recebido do Orquestrador; não consigo calculá-lo)
Limites: só leitura, sem Bash, sem git e sem web. Não rodei script. Não vi o texto da v1.0 (sem git), então a fidelidade do HISTORICO só foi conferida contra as citações do parecer R1. A ordem "Avançar" e as respostas DN de 2026-11-08 só existem no chat. Não atesto a veracidade das fontes [EXTERNO] nem das capturas em sources/.

## Veredito: NÃO CONFORME — 0 Críticas, 2 Médias, 11 Menores (recuperável)

As cinco Médias da R1 foram tratadas de fato:
- M-01 e M-03 estão resolvidas;
- M-04 está resolvida;
- M-02 e M-05 deixaram cada uma um resíduo que conto como Média (R2-M-01 e R2-M-02), porque são o mesmo defeito em outro ponto.

As decisões F-1..F-4 de Andraus estão registradas fielmente quanto ao conteúdo:
- não há nó nem aresta de Fibonacci;
- a parte fractal da P-11, a DN-1, a DN-3 e as decisões abertas não foram fechadas.

Mesmo sem as Médias, o teto seria CONFORME condicional: o gate não rodou nesta sessão, e J-001, N-001, G-001 e M-001 estão abertas.

## 1. Objeto
- Artefato: specs/features/SPEC-008/plan.md v1.1 + checks.md + HISTORICO.md.
- CRITICAL D0–D8; FASE 4; maturidade L3.
- A jusante de SPEC-003/004/005 e do MMC-001 v1.0 (BASELINE).

## 2. Passo 0 — alinhamento
- **ROADMAP.md**
  - l.524: abertura e MMC-001 homologados; "Plan pendente, só por ordem de Andraus". A ordem "Avançar" não está no repositório (não verificável; vai para a ata).
  - l.36–37: as decisões abertas conferem. FIBONACCI-SKILL-001 / TEMPOS-GRAFICOS está em "FECHADAS", com a observação "Não fecha decisão aberta".
- **atomic-spec.md**: método vigente confirmado:
  - §10.2 Escala E0–E3 (l.226);
  - ENF-04 e ENF-07 (l.270, l.273);
  - CC-11 (l.292, l.305).
- **RMR-001**:
  - BL-026 (l.133), gatilho `spec:SPEC-008 em redação`, estado "Em espera".
  - BL-029 (l.136) "Em espera"; o ATIVADO aparece riscado.
  - Nenhum item ATIVADO vincula a SPEC-008.
  - As Disposições batem: PARCIAL / FORA / REFERÊNCIA ×3.
- **governance/DHR-FIBFRAC-001** (2026-11-14) lido.
- **G1 — abri todos os documentos pedidos**:
  - ROADMAP; atomic-spec;
  - RMR-001 (BL-026/027/028/029; BL-043..046 vistos na listagem do Grep);
  - MMC-001 (estrutura, §3.1, §6.2, §8.2-bis);
  - SPEC-048 (l.319, 376, 445, 449, 1158, 1167);
  - SPEC-005 RULE-CEB-010 (l.336–341);
  - SPEC-003 RULE-CF-010 (l.296–301) e WF-C01 (l.164);
  - CCM-001 (l.28, 61–62, 66, 96–101);
  - WORKFLOW v2.1 (WF-04/05/06, T01/T02, A01–A03, F02, P01/P02, R01–R03, D03);
  - SPEC-007 (v2.3 / DHR-SPEC007-005, l.8–10; `max_retrieval_rounds` "orçamento da SPEC-008", l.2136).
  - **Não reabri**: SPEC-004 (RULE-CBP-*) e CHM-001. Herdo a conferência da R1; nenhuma das duas foi tocada pelo delta.

## 3. Gate determinístico
- **VEREDITO D: PASSOU_D** (via GATE-D do Orquestrador; o SHA256 da linha GATE-D é igual ao SHA256-ALVO). Sinais H: 0, nada a confirmar.
- Contagens declaradas conferidas por Grep/leitura:
  - 1 INV (l.326), 11 RULE (l.358..613), 13 EARS (l.643..655), 12 BASpec (l.704..927), 9 EC (l.1476..1602), 22 cenários T (l.1104..1302), 15 ADV (l.1320..1452) = 83;
  - CLASSE C em l.940, GATE DE SAÍDA em l.944;
  - D5 com 38 linhas;
  - corpo de 1.829 linhas ("Pronto para revisão" na l.1829);
  - Grep "DN-1" = 19 e "MARK_CONSUMED" = 29: batem com o checks.

## 4. Pontos para o Especificador provar
1. Que evento e que linha da D5 tratam a falha de um `time_request` (ARM_ALARM / STAGE_TIMER / MARK_CONSUMED) no meio do ciclo? Que contador conta essa "falha seguida", se `failures[]` é por nó? (R2-M-02)
2. Com quais campos do `capability_audit_record` se calcula `foreign_publications` (o filtro usa `workspace`, que o registro não tem)? Qual é o enum de `capability`, e `notice`/`time_request` contam como EXTERNAL_EMIT? (R2-M-01)
3. Na D4.2, o passo (10), que atualiza os contadores, vem depois do (6), que avalia a guarda. Como F33/F34 podem usar `failures` "após D4.3"? (R2-m02)

## 5. Passos
- **Passo 2 — Invariantes: PASS.**
  - Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT: RULE-MDC-002 (c).
  - ICT não cria hipótese: F18, ADV-08.
  - Custo fora da convicção: RULE-MDC-008 (d).
  - NEUTRO antes do limiar: F08a.
  - Nada sai para execução: INV-MDC-01.
  - Dimensões = 8 intocadas.
- **Passo 3 — Constitution Check: PASS.** CC-04 já cita 005 (b) (l.131); CC-11 com 11 D + 1 C.
- **Passo 4 — Rastreabilidade: PASS com Menores** (R2-m05, m06, m07, m09, m10).
- **Passo 4-bis — Dossiê: HERDADO** (inalterado; R1). Risco residual de fonte web declarado.
- **Passo 4-ter — inventário de afirmações**: ver "Conferido e OK" e os achados.
- **Passo 5 — BASpec e profundidade: PASS.**
- **Passo 5-bis**
  - Bloco A: preenchido para as 12 BASpecs (incl. R-19/R-20); os casos são plausíveis.
  - Bloco B: preenchido; SPEC-048 e SPEC-007 acrescentadas; REMOVED e MODIFIED vazios.
  - Adversarial próprio:
    - BASpec-012 (C): o ENTÃO não é detectável para `foreign_publications` (R2-M-01).
    - BASpec-006: QUANDO satisfeito (setup alinhado, hipótese inelegível) com código ambíguo entre 006 (d) e F30 (R2-m01).
    - BASpec-003: espera sem timer se o STAGE_TIMER falhar (R2-M-02).
  - Bloco C, por disciplina:
    - EPI: DN-2 etiquetada [FATO] sem ata (R2-m06).
    - CAU: sem achados.
    - DEC: nenhuma BASpec cruza para a execução.
    - SEM: `rule_id` com INV-MDC-01 (R2-m08); "agente" sem qualificador (R2-m11).
    - ONT, INQ, CTF, UNC, PRB e MET: verificados, sem achados.
- **Passo 6 — EARS e 4Es: PASS** (o EARS 8 está em R2-m01).
- **Passo 7 — Enforcement: FAIL** (R2-M-01, R2-M-02). O resto está OK:
  - EC-MDC-009 criado;
  - BASpec-009 em [E2];
  - MDC_NOTICE_PENDING na lista de `entry_type`;
  - falso-DENY contra referência independente.
- **Passo 8 — Decisões: PASS.**
  - CONS-01 íntegro: θ sem número; BL-029 só citado.
  - DN-1 e DN-3 continuam `[DECISÃO NECESSÁRIA]`.
  - Fica abertas: a parte fractal da P-11, a P-13, J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4 e BL-026.
  - CF-D registra a divergência F-4 × WF-R01 sem criar tabela nem parâmetro.

## Conferido e OK (fonte aberta nesta sessão)

**M-01 resolvida**
- RULE-MDC-006 (g)(h) (l.524–535).
- Guardas "elegível" em F12, F13, F16 e F17 (l.991–996).
- F30, F31 e F32 (l.1009–1011).
- Cruzamento alarme × estado (l.1018).
- T13 (e), T21 e ADV-15 (l.1218–1228, l.1292–1300, l.1452–1459).
- Interface T-9 (l.1043).
- Base: WF-A02/A03 (WORKFLOW l.54–55).

**M-02 resolvida, com resíduo (R2-M-02)**
- "Invocação" = pedida (005 (a), l.471–473); 005 (e) sem nova tentativa (l.494–497). Não há mais contradição com 003 (f): a última frase, na l.440, diz que o macro não tem nova tentativa.
- F06 pede timer (l.984); a Interface STAGE_TIMER inclui F06 (l.1038).
- F33, F34, F35 e F36 (l.1012–1015).
- A D4.3 não conta voltas (l.967).

**M-03 resolvida**
- 005 (d) (l.482–493) nomeia `global_conviction` com [INFERÊNCIA] e ignora `gate_result`, `thresholds_used` e `status`.
- As âncoras batem com o CCM-001: l.61, l.66 (N1/N3, BL-029), l.96–97, l.100–101.
- "Mesmo contrato macro/global" vem da SPEC-003 l.164.

**M-04 resolvida**
- `budget` {`max_rounds`, `stage_deadline`} + `budget_ref` em 003 (a) (l.410–418), atendendo SPEC-048 l.1158 e l.1167.
- Reconciliação da latência (l.632–635): bate com SPEC-005 l.336–341 e SPEC-048 l.319/376/449.
- [INFERÊNCIA] da equivalência `max_rounds` = `max_retrieval_rounds` (l.565–568).
- SPEC-007 e SPEC-048 constam em INHERITS e em Requisitos (l.171–173, l.1051–1052).

**M-05 resolvida, com resíduo (R2-M-01)**
- D4.2 passo (7) confere por ação (l.965).
- INV-MDC-01 traz a "PROVA INDEPENDENTE" (l.349–353).
- Contrato `capability_audit_record` (l.1077–1081); EC-008 (l.1579–1600); F37.

**Menores da R1**
- m-05: l.371–372 e l.265.
- m-06: simulação na D4.2 (l.965); ADV-05 e ADV-07 batem com as categorias do passo (2).
- m-07: l.869, l.702, l.1602, l.1616.
- m-08: `fsm_row` (l.597, l.1519); resíduo em R2-m08.
- m-01..m-04 da FICHA aplicados: l.131, l.168, l.175, l.605, l.1705.

**Contagens do checks e decisões F-1..F-4**
- Contagens do checks l.10 e §1 #7 (38 linhas da D5).
- F-1..F-4 conferem com DHR-FIBFRAC-001 §1 em conteúdo. A transcrição literal diverge (R2-m05).
- Grep "FIBONACCI" = 0. "S1/D1/H4/H1/M5" aparece só em texto de decisão ou conflito (l.76, 258, 362, 1725, 1786).

## 6. Achados

**MÉDIAS**

**R2-M-01 [C05] Os contadores da trava E3 usam campo e enum que o contrato não define** (resíduo do M-05)
- Onde: contrato `capability_audit_record` (l.1077–1081); BASpec-012 GATE DE SAÍDA (l.944–946); EC-MDC-008 POSTCOND (l.1587–1589).
- O que está errado:
  - `foreign_publications` = #(capability = PUBLISH ∧ workspace ≠ manager ∧ EXECUTED), mas o registro não tem campo `workspace`.
  - Os valores MODEL_CALL / EXTERNAL_EMIT / PUBLISH / CLOCK_READ não formam enum declarado e não estão ligados às seis capacidades da allowlist. Assim, "EXECUTED ⊆ allowlist" fica sem definição.
  - Não está dito se `notice` (6) e `time_request` (5) contam como EXTERNAL_EMIT. Se contarem, o EC-008 exige `external_emissions == 0` e falharia em T15/T18.
  - A D4.1 passo (0) faz uma só conferência, mas F01 produz dois efeitos (despacho e STAGE_TIMER), e o INV-MDC-01 pede conferência "para a capacidade daquela ação".
- Ação:
  - declarar o enum de `capability` mapeado 1:1 às seis capacidades da allowlist, mais as capacidades negadas;
  - acrescentar `target_workspace | —` (ou equivalente) ao registro;
  - dizer como `notice` e `time_request` se classificam;
  - explicitar a conferência por ação em F01.
- Condição para nova revisão: cada predicado do GATE DE SAÍDA e do POSTCOND do EC-008 é calculável só com campos do `capability_audit_record`.

**R2-M-02 [C10/C01] Falha de `time_request` no meio do ciclo não tem evento, linha na D5 nem contador** (resíduo do M-02)
- Onde: EC-MDC-004 FAILURE-MODE (l.1533–1534); D5; `checks` §5 l.144.
- O que está errado:
  - O EC-004 diz "no meio do ciclo ⇒ falha seguida (teto)", mas não existe evento do tipo TIME_REQUEST_FAILED nem linha na D5.
  - `failures[nó]` é por nó, e a Spec de Tempo não é nó.
  - Se o STAGE_TIMER pedido em F01/F03/F06/F09/F13 falhar, a espera fica sem timer, o que viola RULE-MDC-009 (e).
  - Se o ARM_ALARM falhar, `CONTEXTO_FORMADO` depende só do timer de F09.
  - O `checks` §5 marca ✔ "Todo FAILURE-MODE com 'nova tentativa' tem evento + linha + timer", o que é falso aqui.
- Ação: criar o evento, a linha da D5 (nova tentativa com a mesma `request_key` até um teto, ou encerramento), o contador e o cenário; corrigir o checks §5.
- Condição para nova revisão: toda falha de capacidade (5) tem um caminho fechado na D5.

**MENORES** (R2-m04, m05, m08, m09 e m11 vão na FICHA-M; os demais ao Especificador)

- **R2-m01 [C01]** RULE-MDC-006 (d) (l.515–520) e o EARS 8 (l.650) mandam setup com hipótese inelegível para o ramo 3 com `MDC_SETUP_MISALIGNED`. Já (h), F30 e ADV-15 dão `MDC_CONTEXT_LOST`, sem ramo. Ação: em (d) e no EARS 8, restringir o ramo 3 à hipótese elegível e remeter a inelegível para (h)/F30.
- **R2-m02 [C01]** As guardas de F33/F34 dizem "após D4.3", mas a D4.2 atualiza contadores no passo (10), depois do efeito (9). Lido literalmente, há Fmax+2 tentativas; T15 (c) espera Fmax+1. Ação: fixar a ordem (contagem de falha antes da guarda). Mesma prevenção do m-06 da R1 (recorrente).
- **R2-m03 [C10]** A saída de "linha listada com guarda falsa" não está definida. Consequências:
  - uma segunda PUB(INSTITUCIONAL) com o macro já pedido não tem código, e o ADV-06 (a) espera `MDC_MACRO_ALREADY_INVOKED` sem evento ou linha que o produza;
  - F03–F05 não têm guarda de sub-etapa: uma nova versão do ESTRUTURAL com a mesma `dispatch_key` durante a espera macro pode reaplicar F04 se o passo (1) da D4.2 for lido como "mesma versão".
  - Ação: definir o código da guarda falsa e restringir o passo (1) à primeira publicação consumida por `dispatch_key`.
- **R2-m04 [C01]** RULE-MDC-007 (d) (l.556) e a nota da D5 (l.975) dizem "em ARMADO, nenhum pedido ao alarme", mas F30 em ARMADO × ALARM_TRIGGERED pede MARK_CONSUMED. Precisa acrescentar "sem disparo". FICHA-M.
- **R2-m05 [C07]** A citação "literal" de F-1 (l.73; também HISTORICO l.65) corrige "Elliot" para "Elliott" e "servira" para "servirá"; a ata DHR-FIBFRAC-001 §1 traz o texto original. Além disso, o Plan não cita a ata pelo ID: a l.1786 ainda diz "a citar na ata". FICHA-M só no plan; o HISTORICO l.65 vai ao Especificador.
- **R2-m06 [C08]** DN-2 (e as respostas DN-1/DN-3) aparecem como [FATO] (l.1785; l.72), mas nenhuma ata as registra (Grep em governance/). A própria definição de [FATO] do Plan (l.26) exige ata. Ação: o Orquestrador registra em ata, ou o Especificador re-etiqueta como [FONTE: AskUserQuestion via Orquestrador].
- **R2-m07 [C07]** RULE-MDC-006 (g) (l.524) atribui ao WF-A02 a transição "ARMED/TRIGGERED → EXPIRED|CANCELLED". O WF-A02 literal (WORKFLOW l.54) só tem saídas de TRIGGERED; a morte antes do disparo vem do WF-A03. Precisa de etiqueta [INFERÊNCIA].
- **R2-m08 [C02]** "rule_id SEMPRE ID de RULE" (l.597, l.1073), mas as recusas da trava têm `rule_id` = INV-MDC-01. FICHA-M.
- **R2-m09 [C06]** O checks.md tem duas afirmações inexatas:
  - l.22 cita "(l.691..914)" para as BASpecs, quando o certo é l.704..927;
  - l.28 diz "cinco linhas inalteradas", mas o motivo do BL-026 ganhou F-4/CF-D.
  - Vai na FICHA-M.
- **R2-m10 [C06]** O HISTORICO.md está incompleto em relação ao INV-07. Pelo próprio conteúdo da v1.1, mudaram e não têm o texto anterior preservado:
  - EC-002 FAILURE-MODE (cita F33–F35, inexistentes na v1.0);
  - EC-004 PRECOND (cita F30/F32/F37);
  - EARS 3/6/8/13;
  - BASpec-003/005/006/012;
  - Termo 4;
  - T01/T13/T15.
  - A l.33 do Plan afirma "Texto anterior … de cada troca: HISTORICO.md". Ação: recuperar o texto com git a partir de 55d0989/5c172dc (o Orquestrador).
- **R2-m11 [C02]** "este agente" sem qualificador nas l.895 e l.1470 (resíduo do m-03). FICHA-M.
- **Observações sem achado:**
  - (a) A precondição proposta no BL-029, "Manager só consome status == GATED_PASS", se fosse aplicada à Fase 1, bloquearia toda leitura macro. Convém registrar em "Conflitos" que o escopo dela é a Fase 2.
  - (b) ALARM_TRIGGERED que chega antes de ALARM_ARMED cai em F29 e o disparo se perde. É fail-safe, mas não há requisito de ordem por alarme à Spec de Tempo.
  - (c) O nó fictício NOVO_X do T05 tem posto 3, o posto do Fractal. Está declarado como teste, então está OK.

## 7. Encaminhamento
- **Ao Especificador (classe O)**: R2-M-01, R2-M-02, R2-m01, m02, m03, m06, m07 e m10, mais o HISTORICO l.65 (parte do R2-m05).
- **Ao Orquestrador**: aplicar a FICHA-M (R2-m04, m05, m08, m09, m11) e, para o R2-m06, registrar as respostas DN de 2026-11-08 em ata.
- **Próxima rodada**: pode ser por delta. As Médias tocam D5, EC-004/008, o contrato e o checks §5; revisar inteiros os dependentes (F01, F09, F13, Interface, ADV-10/11/12/14).

<!-- ACHADOS-ESTRUTURADOS
R2-M-01|MEDIA|C05|predicados da trava E3 usam campo workspace e enum de capability inexistentes no capability_audit_record; notice/time_request sem classificação; F01 sem conferência por ação|todo predicado de GATE/POSTCOND é escrito só com campos e enums declarados no contrato lógico, conferidos campo a campo
R2-M-02|MEDIA|C10|falha de time_request no meio do ciclo sem evento/linha D5/contador; espera pode ficar sem timer; checks §5 marca ✔ falso|para cada capacidade da allowlist com efeito, listar a falha e exigir evento+linha D5+contador antes de marcar ✔
R2-m01|MENOR|C01|006(d)/EARS 8 dão MISALIGNED/ramo 3 a hipótese inelegível; (h)/F30/ADV-15 dão CONTEXT_LOST|ao criar guarda nova, varrer regra, EARS e cenários que citam o mesmo predicado
R2-m02|MENOR|C01|guarda F33/F34 "após D4.3" contra a ordem da D4.2 (contadores no passo 10)|simular a D4.2 passo a passo em cada cenário com contador
R2-m03|MENOR|C10|guarda falsa sem código; ADV-06(a) sem evento; F03-F05 sem guarda de sub-etapa|definir o desfecho de "linha listada, guarda falsa" e mapear todo cenário a um evento
R2-m04|MENOR|C01|007(d)/nota D5 "em ARMADO nenhum pedido" x F30 ARMADO×TRIGGERED pede MARK_CONSUMED|exceção nomeada no mesmo período da regra geral
R2-m05|MENOR|C07|citação "literal" de F-1 corrigida em relação à ata; ata DHR-FIBFRAC-001 não citada por ID|literal = cópia exata da ata; citar o ID da ata quando ela existe
R2-m06|MENOR|C08|DN-2 (e DN-1/DN-3) como [FATO] sem ata|[FATO] só com ata; sem ata = [FONTE]
R2-m07|MENOR|C07|WF-A02 recebe transição ARMED→EXPIRED que só o WF-A03 sustenta|atribuição a WF-xx só com o texto literal; combinação = [INFERÊNCIA]
R2-m08|MENOR|C02|rule_id "SEMPRE RULE" x recusas da trava com INV-MDC-01|definir o domínio do campo incluindo todos os emissores
R2-m09|MENOR|C06|checks com faixa de linha velha (l.691..914) e "linhas inalteradas" falso para BL-026|reconferir as âncoras do checks depois da última edição do plan
R2-m10|MENOR|C06|HISTORICO sem o texto anterior de EC-002/004, EARS, BASpecs, Termo 4, T01/T13/T15|gerar o HISTORICO do diff (git) e não de memória
R2-m11|MENOR|C02|"este agente" sem qualificador (l.895, l.1470)|Grep "este agente" antes da entrega
-->

<!-- FICHA-M {"achados":[
{"id":"R2-m04a","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"e `ARMADO`, nenhum pedido ao alarme (requisito T-3 à Spec de Tempo).","novo":"e `ARMADO` sem disparo, nenhum pedido ao alarme (requisito T-3 à Spec de Tempo).","condicao":"Grep '`ARMADO` sem disparo, nenhum pedido' = 1 em RULE-MDC-007 (d)"},
{"id":"R2-m04b","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"em `CONTEXTO_FORMADO`/`ARMADO`, nenhum pedido ao alarme","novo":"em `CONTEXTO_FORMADO`/`ARMADO` sem disparo, nenhum pedido ao alarme","condicao":"nota de leitura da D5 com 'sem disparo'"},
{"id":"R2-m05a","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"utilizado por agentes Elliott, SMC e ICT. A skill servirá para confirmação","novo":"utilizado por agentes Elliot, SMC e ICT. A skill servira para confirmação","condicao":"citação idêntica a DHR-FIBFRAC-001 §1 F-1"},
{"id":"R2-m05b","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"(Andraus, AskUserQuestion 2026-11-14, via Orquestrador; literal)","novo":"(Andraus, AskUserQuestion 2026-11-14 — DHR-FIBFRAC-001 §1; literal)","condicao":"Grep 'DHR-FIBFRAC-001' >= 1 na tabela de Incorporação"},
{"id":"R2-m05c","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"`[FATO]` (decisões de Andraus, AskUserQuestion 2026-11-14; a citar na ata)","novo":"`[FATO]` (decisões de Andraus, AskUserQuestion 2026-11-14 — DHR-FIBFRAC-001 §1)","condicao":"Grep 'a citar na ata)' sem a linha F-1..F-4 da tabela TRACE-06"},
{"id":"R2-m08a","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"ID de uma RULE — ex.: `RULE-MDC-006`)","novo":"ID de uma RULE ou INV-MDC-01 — ex.: `RULE-MDC-006`)","condicao":"RULE-MDC-010 (a) admite INV-MDC-01 em rule_id"},
{"id":"R2-m08b","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"rule_id (ID de RULE), fsm_row","novo":"rule_id (ID de RULE ou INV-MDC-01), fsm_row","condicao":"contrato cycle_log_entry igual a RULE-MDC-010 (a)"},
{"id":"R2-m11a","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"\"Por que este agente rodou agora\"","novo":"\"Por que este agente analítico rodou agora\"","condicao":"Grep 'este agente rodou' = 0"},
{"id":"R2-m11b","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"(\"por que este agente rodou agora\")","novo":"(\"por que este agente analítico rodou agora\")","condicao":"Grep 'este agente rodou' = 0"},
{"id":"R2-m09a","sev":"MENOR","arquivo":"specs/features/SPEC-008/checks.md","antigo":"Grep `^### BASpec-MDC-` (l.691..914)","novo":"Grep `^### BASpec-MDC-` (l.704..927)","condicao":"faixa igual à do checks l.10"},
{"id":"R2-m09b","sev":"MENOR","arquivo":"specs/features/SPEC-008/checks.md","antigo":"| cinco linhas inalteradas ✔ |","novo":"| cinco Disposições inalteradas (PARCIAL/FORA/REFERÊNCIA ×3); motivo do BL-026 acrescido de F-4/CF-D (HISTORICO) ✔ |","condicao":"F10 coerente com a Nota de gate do plan l.117"}
]} -->
(Nota sobre a FICHA-M: são 11 entradas em 10 linhas de 2 arquivos. R2-m04a/b tocam as l.556 e l.975; R2-m05a/b ficam ambas na l.73. Nenhuma entrada cria regra, campo, ID ou mecanismo.)

## Cobertura por bloco (MODO integral)
- **Conferidos agora**:
  - cabeçalho, Dimensionamento, Incorporação F-1..F-4, Condições, Nota de gate, CC-01..12;
  - INHERITS e tabela de Conservação (leitura); Acepção; tabela WORKFLOW; D0/D1; Pré-requisitos;
  - INV-MDC-01 e RULE-MDC-001..011; parâmetros e reconciliação; EARS 1–13; D3.1;
  - BASpec-001..012; D4.1–D4.4; D5 F01..F37 e notas; D6; Interface; Requisitos; contrato;
  - Fixture M0; T01–T22; ADV-01..15; EC-001..009 e Escala;
  - Plan (riscos, 4Es, Tasks); errata E-1..E-3; Conflitos; Decisões abertas; §7-bis A–D;
  - TRACE-06; Perguntas; Autopré-check;
  - checks.md inteiro; HISTORICO.md inteiro.
- **HERDADOS da R1 (fonte inalterada)**: Dossiê (research/sources); linhas da errata E-1 na SPEC-003; conteúdo de SPEC-004 RULE-CBP-* e CHM-001.
- **Não conferido**: texto da v1.0 (sem git); execução de scripts.

Arquivos:
/home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/plan.md
/home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/checks.md
/home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/HISTORICO.md
/home/user/Sistema-Operacional-de-Trading--SOT/governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-PLAN-R1-2026-11-08.md
/home/user/Sistema-Operacional-de-Trading--SOT/governance/DHR-FIBFRAC-001_Ata_Decisoes_Fibonacci_Skill_e_Tempos_Graficos.md
/home/user/Sistema-Operacional-de-Trading--SOT/canon/CCM-001-canonical-conviction-model.md
/home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-048/plan.md
/home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-005/plan.md
/home/user/Sistema-Operacional-de-Trading--SOT/WORKFLOW.md
/home/user/Sistema-Operacional-de-Trading--SOT/backlog/RMR-001_Painel_Backlog.md

## Adendo G1/G2 (guarda pós-revisor, DHR-AUDITOR-EXTERNO-018)
**G2:** `GATE-D: PASSOU_D | cmd: python scripts/revisor_gate.py specs/features/SPEC-008/plan.md | SHA256-ALVO: a198b8e619b6cd8c4b9b5b70048a8ab14a28b2f1284734c365b2e32f2867072e | data: 2026-11-14` (sinais H: 0; o Revisor conferiu que o SHA da linha GATE-D é igual ao SHA256-ALVO). `validate_spec_sot.py` 14/14.
**G1:** o próprio Revisor abriu ROADMAP, atomic-spec (§10.2, ENF-04/07, CC-11), RMR-001 (BL-026/029, BL-043..046), MMC-001, SPEC-048/005/003/007, CCM-001 e WORKFLOW; declarou não reaberto apenas SPEC-004 (RULE-CBP-*) e CHM-001, herdados da R1 e não tocados pelo delta. Nada a acrescentar pelo Orquestrador.

## Adendo G1 (guarda pós-revisor, DHR-AUDITOR-EXTERNO-018) — governance/RULES.md
Aberto pelo Orquestrador (Grep). **Nada muda no veredito, sem achado novo.** As regras que o Plan cita e dependem do `RULES.md` existem: RULE-BB-001/002/004/005, RULE-BB-003 (marcada SUPERSEDED por Q-006 no próprio arquivo — o Plan usa só o texto "hipótese só é base de decisão em ACTIVE ou DOMINANT", conferido pelo Revisor na R1 l.318-321), RULE-DEC-01, RULE-MET-01, RULE-HV-01, RULE-HD-02, RULE-SEM-03 e RULE-ECC-07. O Revisor registrou o `RULES.md` como conferido nas rodadas R1/R2 (RULE-BB-003) e não declarou nenhum item como não verificado por indisponibilidade.
