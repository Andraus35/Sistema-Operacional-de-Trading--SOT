# Parecer do Revisor — Plan da SPEC-008 v1.2 — R3 (última rodada; experimento P10) — 2026-11-15

> Transcrição pelo Orquestrador do retorno do Revisor SOT (somente leitura; classe S2 por delta, base `366af09`, pacote `DELTA-SPEC-008-plan-366af09-44e6131f.txt`). **CONFORME condicional — 0 Críticas, 0 Médias, 9 Menores.** Objeto: `specs/features/SPEC-008/plan.md` v1.2 (commit `28eb871`, SHA256-ALVO `44e6131fd903…`) + `checks.md` + `HISTORICO.md`.

TOKENS: 296063  <!-- tokens NOVOS (in+out+cache criado) do Revisor nesta rodada, via `telemetria_tokens.py tokens a247b54d4db38e77b` (DHR-TELEMETRIA-002) -->

RELATÓRIO DE REVISÃO — SPEC-008 Plan v1.2 (candidata) — 2026-11-15 — Revisor de Especificação SOT — Rodada R3 (última; experimento P10)

MODO: delta (38 de 127 blocos alterados). Li inteiros os blocos dependentes das Médias da R2.
SHA256-ALVO: 44e6131fd9035c7030eccde2671c44cf159079390d1542f93a7e5dd48a33f8e8 (recebido do Orquestrador; não consigo calculá-lo)
GATE-D: PASSOU_D (via GATE-D do Orquestrador; o SHA256 da linha é igual ao SHA256-ALVO do pedido; sinais H: 0, nada a confirmar).
Limites: só leitura, sem Bash, git ou web. Não rodei script. Não tenho o texto da v1.1, então não consegui diffar v1.1→v1.2; o que mudou veio do DELTA e da leitura direta. Para a R2-m10 usei o patch `DIFF-PLAN-V1.0-ATUAL-2026-11-14.patch`. Não atesto a veracidade das fontes [EXTERNO] nem das capturas `sources/` (Dossiê HERDADO da R1/R2, inalterado). Não comparei os sha256 das 18 fontes do delta com os da R2, porque o parecer R2 não os registrou.

## VEREDITO: CONFORME condicional — 0 Críticas, 0 Médias, 9 Menores
Pendente (bloqueadores abertos, não fechados pelo Plan): J-001, N-001 (θ sem número), G-001, M-001; DN-1 e parte fractal da P-11 abertas. A rodada não criou nenhum defeito Médio nem Crítico. Resta um padrão recorrente de inconsistência cenário×algoritmo (C01): R1-m06, R2-m02 e agora R3-m01 e R3-m02. Pela regra do experimento, parecer só com Menores não abre rodada nova. Fica à escolha de Andraus: condição de homologação ou construção. Recomendo corrigir R3-m01, m02, m03 e m06 antes da homologação, porque são só redação.

## 2. Passo 0 (G1 declarado)
Abri por Read/Grep:
- ROADMAP.md (l.524 e decisões);
- atomic-spec.md (§10.2 l.226, ENF-04 l.270, ENF-07 l.273, CC-11 l.292);
- RULES.md (RULE-BB-003 SUPERSEDED l.318, RULE-DEC-01, RULE-MET-01, RULE-HV-01, RULE-HD-02..04, RULE-SEM-03, RULE-ECC-07 l.518);
- RMR-001 (BL-026 l.133 e BL-029 l.136 "Em espera"; nenhum ATIVADO vincula a SPEC-008);
- MMC-001 (§8.2-bis);
- CCM-001 (l.61, l.96–98);
- WORKFLOW v2.1 (WF-A01..A03 l.53–55, WF-R01 l.102, WF-D03 l.112);
- atas DHR-SPEC008-004 (l.18–19, 23–24, 30), DHR-FIBFRAC-001 (l.18 F-1, l.21 F-4) e DHR-FIBFRAC-002 (l.18).
Não reabri SPEC-003/004/005/007/048 nem CHM-001: ficam HERDADOS da R2 (não são citados em nenhum bloco alterado além da R2).

## Verificação dos itens pedidos (arquivo:âncora)

**R2-M-01 — RESOLVIDA.**
- Contrato `capability_audit_record` (plan l.1091–1109):
  - enum CAP: 6 PERMITIDAS 1:1 com a allowlist de INV-MDC-01 (l.329–334);
  - 12 NEGADAS: os 10 subs de `MDC_EFFECT_FORBIDDEN` (D3.1 l.709) na mesma ordem, mais MODEL_CALL e CLOCK_READ (l.710–711);
  - `target_workspace` e `object_type` declarados;
  - `TIME_REQUEST` e `NOTICE_LOCAL` NÃO são `ORDER_EMISSION` (l.1102), logo T15/T16/T18 não violam a trava.
- Os cinco predicados (EXECUTED ⊆ allowlist, model_calls, external_emissions, foreign_publications, clock_reads; l.1104–1109) usam só campos e enums declarados.
- BASpec-MDC-012 GATE DE SAÍDA (l.956–959) e EC-MDC-008 POSTCOND (l.1636–1639) remetem a esses predicados. Também ADV-06 (a), ADV-10/11/14 e T01 consultam só o registro.
- F01 com duas conferências por ação (D4.1 SAÍDA l.976; contrato l.1115–1117): PUBLISH_OWN do despacho e TIME_REQUEST do STAGE_TIMER.
- Resíduos Menores: R3-m05 e R3-m07.

**R2-M-02 — RESOLVIDA.**
- `TIME_REQUEST_FAILED`: RULE-MDC-003 (h) l.445–448; D3.1 l.687; D5 F38 l.1030; nota "Falha de `time_request`" l.1032.
- Contador `failures[TEMPO]`: D4.3 l.980; contrato `cycle_log_entry.counters` l.1089.
- Estouro em F20 (l.1012). T-10 na Interface (l.1057). Cenário T23 (l.1348–1358).
- Nenhuma espera sem timer: toda espera pede `STAGE_TIMER` (F01/F03/F06/F09/F13) e a falha do pedido vira F38→F20 (l.1032; RULE-MDC-009 (e)).
- `checks` §5 l.148–149 não tem ✔ falso quanto à D5 inteira. A única exceção é o ✔ de l.148 ("falha de cada capacidade tem caminho fechado"): sobre F16, ver R3-m04.
- Resíduos Menores: R3-m02, m03, m04.

**R2-m01 — RESOLVIDA.** RULE-MDC-006 (d) l.521–527, EARS 8 l.660 e BASpec-006 ENTÃO l.826–828: o ramo 3 só vale com hipótese elegível; inelegível ⇒ (h)/F30 (`MDC_CONTEXT_LOST`, sem ramo). F16/F17/F30 (l.1008–1009, 1022), T12 e ADV-15 concordam.

**R2-m02 — RESOLVIDA (com Menor R3-m01).** Simulei a D4.2 passo a passo (l.978):
- Falha k de `DISPATCH_PUBLISH_FAILED` (T15 c): (0) passa por ser interno [ver R3-m06]; (1) não é publicação; (2) é evento interno do ciclo; (3) ciclo aberto; (4) dono SPEC-008; (5) F33 listada.
- (5b) failures = k. Para k ≤ Fmax a guarda de F33 ("≤ Fmax, já incrementado") é verdadeira, (7) confere PUBLISH_OWN, (8) grava, (9) republica com a mesma `dispatch_key`.
- Para k = Fmax+1, (5b) dá failures > Fmax ⇒ F20 em vez de F33. Tentativas = 1 inicial + Fmax republicações = Fmax+1. Bate com T15 (c) e com D4.3.
- T23 (b) é idêntico com `failures[TEMPO]` (F38/F20). T23 (a) idem: failures[TEMPO]=1 ≤ Fmax ⇒ F38, e zera na confirmação.
- T15 (a): (6) steps+1 > Smax ⇒ F20, e o despacho não ocorre.

**R2-m03 — RESOLVIDA.**
- `MDC_GUARD_NOT_SATISFIED`: RULE-MDC-007 (b) l.552; D3.1 l.704; T14 (b) para no (6) (l.1265–1266).
- ADV-06: (a) para no passo (7) da D4.2 (ação de INVOKE_MACRO com `MDC_MACRO_INVOKED` no livro); (b) resultado tardio para no (3); (c) para no (1).
- D4.2 (1) restrito à primeira publicação consumida por `dispatch_key` (l.978). O objeto-hipótese do ICT (F18) não conta, porque não é consumido. Consistente com ADV-08.

**R2-m05, m06, m07 — RESOLVIDAS.**
- F-1 (plan l.75) é idêntica, caractere a caractere, à DHR-FIBFRAC-001 l.18, inclusive "Elliot" e "servira". F-4 (l.78) idem.
- A ata é citada por ID (l.75–78 e TRACE-06 l.1839).
- DN-1/DN-2 citam DHR-SPEC008-004 §1/§2 (l.73, 1788, 1837, 1845, 1847), e a ata confirma (l.18, 19, 23, 24).
- DN-3 cita DHR-FIBFRAC-002 §1 (l.74, 405, 1838, 1849). A ata confirma "roteiro v1" com Fibonacci como skill.
- RULE-MDC-006 (g) (l.531–537) traz o WF-A02 literal ("só TRIGGERED → {CONSUMED|EXPIRED|CANCELLED}"), o WF-A03 e a etiqueta [INFERÊNCIA]. Bate com WORKFLOW l.54–55.

**R2-m10 — RESOLVIDA em substância.** HISTORICO l.59–102 recupera o texto de EC-002, EC-004, EARS 3/5/6/8/13, BASpec-003/005/006/012, Termo 4, CC-11 e T01/T13/T15. Conferi por Grep contra as linhas `-` do patch: EARS 3, 5, 6, 8, 13, CC-11 e Termo 4 batem literalmente. Resíduo: R3-m08.

**Observações (a)/(b)** estão em CF-E (l.1776) e CF-F (l.1775), com T-11 na Interface. CF-E confere com BL-029 (RMR-001 l.136, GATED_PASS).

**DN-3 / Fibonacci-Fractal:** RULE-MDC-002 (e)(f) (l.397–406), Perguntas (l.1849), Decisões abertas (l.1788) e rótulos (TRACE-06 l.1836–1839) não têm nó nem aresta de Fibonacci/Fractal. Grep "FIBONACCI" = 0. DN-3 consta como decidida com ata. DN-1 e a parte fractal da P-11 seguem abertas. Não achei decisão aberta fechada: J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4, BL-026, DN-1, P-11 fractal e P-13 seguem marcadas como abertas ou "decidir depois".

**Contagens (Grep/Read):**
- 1 INV (l.328), 11 RULE (l.360..623), 13 EARS (l.653..665), 12 BASpec (l.716..939), 9 EC (l.1523..1652), 23 T (l.1133..1348), 15 ADV (l.1364..1499) = 84.
- D5: 39 linhas (F01..F38 com F08a/b; l.992..1030). CLASSE C só em l.952.
- Corpo: 1.883 linhas (última, "Pronto para revisão", em l.1883).
- Grep "DN-1" = 20; "MARK_CONSUMED" = 35; "FIBONACCI" = 0.
- As âncoras de linha do checks.md l.10 e l.98 batem com o plan v1.2.

**FICHA-M da R2 aplicada:**
- m04: l.566 e l.988 trazem "sem disparo".
- m05: l.75, 78 e 1839.
- m08: l.607 e l.1087.
- m11: "este agente" só aparece como "este agente analítico" (l.615, 907, 1517).
- m09: checks l.10 e l.28.

## 5. Passos
- **Passo 2 — Invariantes: PASS.** Hierarquia, ICT sem hipótese (F18/ADV-08), custo fora do vetor (RULE-MDC-008 (d)), 8 dimensões intocadas, nada para a execução (ORDER_EMISSION negada).
- **Passo 3 — Constitution Check: PASS.** CC-01..CC-12 coerentes com a v1.2; CC-11 com 11 D + 1 C.
- **Passo 4 — Rastreabilidade: PASS com Menores** (R3-m08 e R3-m09).
- **Passo 4-ter — M1..M5:** tabela abaixo.
- **Passo 5 — BASpec e profundidade: PASS.** Observação: R3-m03.
- **Passo 5-bis:**
  - Bloco A e Bloco B herdados da R2 e conferidos na v1.2: casos plausíveis, REMOVED e MODIFIED vazios.
  - Adversarial próprio:
    - BASpec-012 (C): "se o ENTÃO nunca ocorresse?" O `capability_audit_record` independente detecta; resolvido. Resta o gap R3-m05 (falha parcial em F01 sem cenário).
    - BASpec-003: "e se o `STAGE_TIMER` falhar?" F38→F20, fechado. Resta R3-m02.
    - BASpec-011/F16: R3-m04.
  - Bloco C:
    - EPI: sem achado (F-1..F-4, DN-1/2/3 com ata; (g) e (d) com [INFERÊNCIA]).
    - CAU: sem achado.
    - DEC: nenhuma BASpec cruza para execução.
    - SEM/ONT/INQ/CTF/UNC/PRB/MET: verificados, sem achados; Termo 3 corrige o "agente".
- **Passo 6 — EARS e 4Es: PASS** (R3-m03).
- **Passo 7 — Enforcement: PASS.** ENF-01..08 presentes:
  - E3 fail-closed com prova independente do runtime (ENF-03/04);
  - falso-DENY por amostragem contra referência independente (ENF-07);
  - escala E0–E3 em seção própria (ENF-08);
  - BASpec-009 em E2.
  - Menores: R3-m05 e R3-m07.
- **Passo 8 — Dependências e decisões: PASS** (condicional: J-001, N-001, G-001 e M-001 abertas).

## Passo 4-ter — inventário (afirmação | fonte aberta | resultado)
| Afirmação | Fonte aberta | Resultado |
|---|---|---|
| Enum CAP 1:1 com a allowlist e com os 10 subs + MODEL_CALL/CLOCK_READ | plan l.329–334, 709–711, 1094–1101 | confere |
| Predicados da trava só com campos declarados | plan l.1091–1109 | confere |
| F-1 e F-4 "literais" | DHR-FIBFRAC-001 l.18 e l.21 | confere |
| DN-1 aberta, DN-2 decidida | DHR-SPEC008-004 l.18–19, 23–24 | confere |
| DN-3 decidida | DHR-FIBFRAC-002 l.18 | confere |
| (g): WF-A02 só tem saídas de TRIGGERED; WF-A03 sustenta a morte antes do disparo | WORKFLOW l.54–55 | confere |
| CF-E: precondição `GATED_PASS` do BL-029 | RMR-001 l.136 | confere |
| BL-026 e BL-029 "Em espera"; nenhum ATIVADO vinculado | RMR-001 l.133/136, l.73 | confere |
| Textos anteriores do HISTORICO (EARS 3/5/6/8/13, CC-11, Termo 4) | patch l.53, 74, 280–291 | confere |
| `global_conviction` e `directional_conflict` no esquema do CCM-001 | CCM-001 l.61, 96–98 | confere |
| Contagens do Plan e do checks (84; D5 = 39) | Grep/Read acima | confere |
| `checks` §2 l.98: "nenhum cenário espera código de passo posterior ao que o pararia ✔" | D4.2 l.978 × T19 l.1308 | **não confere** (R3-m01) |
| `checks` §5 l.148: "falha de cada capacidade com efeito tem caminho fechado ✔" | D5 F16/F27/F38 | **não confere por inteiro** (R3-m04) |

## Amostra anti-leniência (blocos inalterados, relidos de forma independente)
INV-MDC-01 × contrato; RULE-MDC-001 × D4.1; RULE-MDC-004 × F13/F14/F15; RULE-MDC-009 (e); RULE-MDC-011 × F16/F27; T05/T10/T20. Dois achados vieram daí (R3-m01 em T19, R3-m07), e ambos sinalizam que a simulação passo a passo ainda não cobre todos os cenários antigos.

## 6. ACHADOS
**Críticas: nenhuma. Médias: nenhuma.**

Menores:
- **R3-m01 [C01]** (T19, plan l.1308–1313, + checks l.98). T19 parte de "ciclo encerrado por T13 (a)", isto é, em ARMADO, e o INSTITUCIONAL já foi consumido (F06). Ele espera `MDC_CYCLE_CLOSED` para "PUB(INSTITUCIONAL) atrasada". Pela D4.2 (1), reformulada na R3 (só a 1ª publicação por `dispatch_key`; "nova versão, republicação ou resposta posterior"), essa publicação para no passo (1) com `MDC_DUPLICATE_IGNORED`, não no (3). O checks l.98 lista T19→(3) e afirma "nenhum cenário espera código de passo posterior" (✔ falso para essa parte). Ação: trocar o 2º evento por um que chegue ao (3) (p.ex. `STAGE_TIMER_FIRED`/`ALARM_ARMED(A1)` tardio) ou corrigir o código esperado, e corrigir o checks l.98. Não mecânico (escolha de evento).
- **R3-m02 [C01]** (F20 l.1012, nota D5 l.1032, RULE-MDC-003 (h) l.448, T23 (c) l.1351–1357). A falha do `MARK_CONSUMED` do ENC é "só a entrada `MDC_TIME_REQUEST_FAILED`". Pela D4.2, um evento `TIME_REQUEST_FAILED` depois do ENC para no (3)/F28 (`MDC_CYCLE_CLOSED`). Falta dizer uma frase: essa falha é resultado do efeito da própria linha F20/F22 (entrada de resultado), não um evento processado pelo (3). Sem isso, T23 (c) contradiz F28.
- **R3-m03 [C01, propagação]** EARS 3 (l.655) e BASpec-MDC-003 ENTÃO (l.760–764) não mencionam RULE-MDC-003 (h) (falha de `time_request`/F38), embora a BASpec cite T23 em DADO/VERIFICAÇÃO e a matriz do checks §4 ligue RULE-MDC-003 ao EARS 3. Acrescentar a cláusula.
- **R3-m04 [C10]** F16 (l.1008) pede `MARK_CONSUMED` e entra em `EM_SÍNTESE`. F38 só cobre AGUARDANDO…ATIVADO; uma falha do `MARK_CONSUMED` depois da transição cai em F27 (`MDC_NOT_PHASE1_TRANSITION`), sem reenvio e sem cenário. É fail-safe (o alarme termina pelas regras da Spec de Tempo), mas o ✔ de checks l.148 é amplo demais. Declarar (a) a ordem (confirmação antes da transição) ou (b) o desfecho aceito, com cenário.
- **R3-m05 [C05]** A falha da 2ª conferência de F01 (TIME_REQUEST do `STAGE_TIMER`) acontece com o ciclo já aberto em AGUARDANDO. F37 serve, mas INV-MDC-01 (l.348–349) diz "no pedido, nada é aberto", e nenhum ADV cobre essa falha parcial (ADV-12 só cobre o passo (0) e o meio do ciclo em F03). Acrescentar a variante em ADV-12 ou uma frase em D4.1 SAÍDA.
- **R3-m06 [C02]** D4.2 (0) (l.978) aplica o "envelope mínimo SPEC-005" a "cada notificação ou evento interno". Eventos internos (`DISPATCH_PUBLISH_FAILED`, `TIME_REQUEST_FAILED`, `LIMIT_COUNTER_EXCEEDED`, `ON_ENTER`, `CAPABILITY_CHECK_FAILED`) não trazem envelope, e a simulação de T15 (c)/T23 só passa se (0) valer apenas para notificações. Restringir o (0) a notificações.
- **R3-m07 [C01]** `notice.kind = CAPABILITY` (contrato l.1114; EC-007 l.1617) é inalcançável: F37/ADV-12 exigem "notice == 0" e "nenhum aviso". Além disso, o contrato fixa `to = Andraus`, enquanto RULE-MDC-004 (d), EARS 5 e T18 dizem "Andraus/Fase 0". Alinhar o enum e o destinatário.
- **R3-m08 [C06]** HISTORICO R2→R3 (l.104–133) não traz linhas para BASpec-MDC-003 (T23 acrescentado em DADO/VERIFICAÇÃO) nem para T22 (o delta o marca como alterado e não consegui identificar a mudança sem a v1.1). Também não aponta para a FICHA-M do parecer R2 como fonte do texto anterior das edições de classe M (m04, m08, m09, m11). Plan l.33 e l.34 prometem "texto anterior … HISTORICO.md".
- **R3-m09 [C06, mecânico]** Plan l.34 data a v1.2 como 2026-11-14, mas HISTORICO l.11 e checks l.6 dizem 2026-11-15 (FICHA-M abaixo).

## Conferido e OK (fonte aberta nesta sessão)
- R2-m01, m02 (simulação refeita), m03, m05, m06, m07, m10 (em substância), observações (a)/(b).
- DN-3 e as demais decisões abertas (CONS-01), Fibonacci/Fractal sem nó.
- Contagens do Plan e do checks; âncoras de linha do checks.md; mapa código↔cenário do checks §2, salvo a observação de T19.
- Termo 3/"agente" qualificado.
- Atas DHR-SPEC008-004, DHR-FIBFRAC-001 e 002.

## 4. Interpelação
Não interpelei de novo: as provas pedidas na R2 (§4) estão no Plan (R2-M-01 e M-02, ordem da D4.2). Fica como pergunta para o Especificador: R3-m01 (T19 × D4.2 (1)) e R3-m02 (T23 c × F28).

## 7. VEREDICTO e 8. ENCAMINHAMENTO
**CONFORME condicional (pendente J-001, N-001, G-001, M-001).** Não é homologação nem aprovação tácita. Segue para Andraus com os 9 Menores. R3-m09 vai por FICHA-M. R3-m01, m02, m03 e m06 são recomendados como condição de homologação (redação). m04, m05, m07 e m08 podem ficar para a construção ou virar condição, à escolha de Andraus.
Risco residual declarado: fontes [EXTERNO] e capturas não verificáveis sem web; sem git não confirmei o texto da v1.1.

<!-- ACHADOS-ESTRUTURADOS
R3-m01|MENOR|C01|T19 espera MDC_CYCLE_CLOSED para PUB(INSTITUCIONAL) atrasada, mas a D4.2 (1) restrita à 1ª publicação por dispatch_key a para antes, com DUPLICATE_IGNORED; checks §2 afirma ✔ falso|simular a D4.2 passo a passo em TODO cenário que cite código de passo, inclusive os inalterados, depois de mudar a ordem ou o escopo de um passo
R3-m02|MENOR|C01|falha do MARK_CONSUMED do ENC gravada como entrada MDC_TIME_REQUEST_FAILED após ENC contradiz D4.2 (3)/F28 sem exceção declarada|ao criar exceção a uma regra geral (ciclo encerrado não aceita evento), nomeá-la no passo geral
R3-m03|MENOR|C01|EARS 3 e BASpec-003 ENTÃO sem a cláusula da RULE-MDC-003 (h) nova|ao acrescentar alínea a uma RULE, Grep por EARS/BASpec do mesmo ID e propagar
R3-m04|MENOR|C10|falha do MARK_CONSUMED em F16 (já em EM_SÍNTESE) cai em F27 sem reenvio e sem cenário; checks §5 ✔ amplo|para cada efeito de cada linha da D5, listar a falha e o estado em que ela é processada
R3-m05|MENOR|C05|falha parcial na 2ª conferência de F01 sem cenário; INV diz "no pedido nada é aberto"|todo caminho de falha novo tem variante em ADV ou frase no passo
R3-m06|MENOR|C02|D4.2 (0) exige envelope SPEC-005 para evento interno|escopo explícito de cada passo da D4.2 por categoria de emissor
R3-m07|MENOR|C01|notice.kind CAPABILITY inalcançável (F37/ADV-12: nenhum aviso); to = Andraus × "Andraus/Fase 0"|enum e destinatário derivados da allowlist
R3-m08|MENOR|C06|HISTORICO R2→R3 sem linhas de BASpec-003 e T22 e sem ponteiro à FICHA-M da R2|gerar o HISTORICO do diff (git) das duas versões
R3-m09|MENOR|C06|data da v1.2 no Plan (2026-11-14) ≠ HISTORICO e checks (2026-11-15)|datar a versão no mesmo commit que cria o HISTORICO
-->

<!-- FICHA-M {"achados":[
{"id":"R3-m09","sev":"MENOR","arquivo":"specs/features/SPEC-008/plan.md","antigo":"| 1.2 | 2026-11-14 | Correção do parecer R2 (R2-M-01","novo":"| 1.2 | 2026-11-15 | Correção do parecer R2 (R2-M-01","condicao":"data da v1.2 igual a HISTORICO.md l.11 e checks.md l.6; a linha da v1.1 (2026-11-14) fica intacta"}
]} -->
(Nota: R3-m01..m08 não são mecânicos. Exigem escolha de evento, de redação ou de regra e vão ao Especificador ou a Andraus.)

Arquivos revisados:
/home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/plan.md
/home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/checks.md
/home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/HISTORICO.md
/home/user/Sistema-Operacional-de-Trading--SOT/governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-PLAN-R2-2026-11-14.md
/home/user/Sistema-Operacional-de-Trading--SOT/governance/propostas/SPEC-008/DIFF-PLAN-V1.0-ATUAL-2026-11-14.patch
/home/user/Sistema-Operacional-de-Trading--SOT/governance/DHR-FIBFRAC-001_Ata_Decisoes_Fibonacci_Skill_e_Tempos_Graficos.md
/home/user/Sistema-Operacional-de-Trading--SOT/governance/DHR-FIBFRAC-002_Ata_Roteiro_v1_Confirmado_e_Glossario_Confluencia.md
/home/user/Sistema-Operacional-de-Trading--SOT/governance/DHR-SPEC008-004_Ata_Respostas_DN1_DN2_do_Plan_SPEC-008.md

## Adendo G1/G2 (guarda pós-revisor, DHR-AUDITOR-EXTERNO-018)
**G2:** `GATE-D: PASSOU_D | cmd: python scripts/revisor_gate.py specs/features/SPEC-008/plan.md | SHA256-ALVO: 44e6131fd9035c7030eccde2671c44cf159079390d1542f93a7e5dd48a33f8e8 | data: 2026-11-15` (sinais H: 0; o Revisor conferiu que o SHA da linha GATE-D é igual ao SHA256-ALVO). `validate_spec_sot.py` 14/14; `pre_entrega` 0 bloqueantes.
**G1:** o próprio Revisor abriu ROADMAP, atomic-spec (§10.2, ENF-04/07, CC-11), RULES.md (RULE-BB-003 SUPERSEDED, RULE-DEC-01, RULE-MET-01, RULE-HV-01, RULE-HD-02..04, RULE-SEM-03, RULE-ECC-07), RMR-001, MMC-001, CCM-001, WORKFLOW e as atas DHR-SPEC008-004/DHR-FIBFRAC-001/002; declarou herdados da R2 (não reabertos) SPEC-003/004/005/007/048 e CHM-001. Nada a acrescentar pelo Orquestrador.
**Experimento P10 (DHR-EXPERIMENTO-PARADA-001):** pedido com cláusula `EXPERIMENTO: P10-REGRA-DE-PARADA`, `SHA256-ALVO` e pacote de delta — aceito pelo hook `experimentos-ativos` (3ª rodada = teto 3). Parecer só com Menores ⇒ **não abre rodada nova**; a escolha entre condição de homologação e construção é de Andraus.
**G2 (reconfirmação do harness):** `VEREDITO D: PASSOU_D`, sinais H: 0; as 4 verificações informativas do repositório inteiro apontam para OUTROS arquivos (fora do escopo desta Spec: `pipeline_schemas` e `specs_1a_geracao` — fibonacci/elliott, preexistentes). Nenhum achado do gate a confirmar ou descartar neste Plan.
