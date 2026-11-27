# Parecer do Revisor SOT — R1 (integral) — errata aditiva ao Plan v1.2 da SPEC-008 (4 condições da DHR-SPEC008-005 §3)

> **Transcrição pelo Orquestrador** do relatório do Revisor (somente leitura; subagente `af1e3e60f81d509df`, 2026-11-27), preservando veredicto, achados e os blocos `ACHADOS-ESTRUTURADOS` e `FICHA-M` na forma original (LOOP-001; `aplicar_ficha_m.py`). Passos de revisão e conferências estão resumidos; o relatório integral ficou na conversa. Não é homologação.

- **Objeto:** `governance/propostas/SPEC-008/ERRATA-PLAN-SPEC008-4-CONDICOES-PROPOSTA-2026-11-27.md` · **Complexidade:** CRITICAL D0–D8 · **Modo:** integral (1ª rodada) · **SHA256-ALVO:** não recebido · **TOKENS:** INDETERMINADO.
- **Veredicto: CONFORME condicional.** 0 Críticas, 0 Médias, 7 Menores (4 mecânicos na FICHA-M). Gate NÃO VERIFICADO (`revisor_gate` inerte em nuvem; não se aplica a errata) ⇒ teto do veredito = CONFORME condicional; `check_refs` ERRO=0 (dado do Orquestrador).
- **Pontos prioritários:** (1) F37 a partir de AGUARDANDO: inferência se sustenta, âncora fraca e resultado não observável (m01); (2) opção (b) de R3-m04 não cria estado/seta/evento/código nem linha de D5 (WF-F02 e MMC-001 §3.2.3 intactos), mas a frase de retomada é regra nova não declarada (m02); (3) tabela fato→locais de R3-m07 completa nos 5 locais; uma contagem errada (m04) e um requisito à SPEC-015 sem propagação (m07); (4) Patch não cabe (CR-001 l.439); Minor defensável só com E-3 = só Andraus e E-4 = retirar; (5) HISTORICO: BASpec-MDC-003 e ponteiro à FICHA-M conferem; erro de atribuição de R2-m05 (m05); rótulo do T22 defasado (m06); (6) nenhuma decisão aberta fechada; RULE-SEM-03 preservada.
- **Conferido e OK:** trechos "vigentes" citados batem literalmente com plan.md e checks.md; Passos 2–7 PASS; adversarial T24/ADV-12(d) com detecção.
- **Risco residual:** git não conferido pelo Revisor; fontes externas não verificadas; D4.2 refeita só para T24 e ADV-12 (d).

## Achados (todos Menores)
- **R1-m01 [C10] (classe O):** ancorar o estado de origem na BASpec-MDC-001 ENTÃO ("aceito ⇒ abertura gravada … AGUARDANDO") + D4.1 SAÍDA; acrescentar `from_state == AGUARDANDO` à VERIFICAÇÃO de ADV-12 (d); dizer se a entrada `MDC_CYCLE_OPENED` existe nesse caso.
- **R1-m02 [C01] (classe O):** a frase de retomada de RULE-MDC-003 (h) excepciona RULE-MDC-010 (b) e BASpec-MDC-010 ENTÃO sem remissão; declarar a exceção no §1 e §6 e nomeá-la nas duas regras (ou retirar a frase e o "inclusive depois de replay" do T24).
- **R1-m03 [C01] (M):** propagar T24 à linha `MDC_NOT_PHASE1_TRANSITION` da D3.1 e do checks §2.
- **R1-m04 [C06] (M):** "as outras 14 de `to = `" → 10.
- **R1-m05 [C07] (M):** R2-m05 = "desenho" no ESQUELETO, não "aplicado_m".
- **R1-m06 [C06] (M):** rótulo `[INFERÊNCIA]` do T22 defasado (conferido por `git show 366af09`).
- **R1-m07 [C04] (classe O):** a nova RULE-MDC-004 (d) delega à SPEC-015 o meio de aviso à Fase 0; propagar o requisito à seção "Requisitos a outras Specs".

## Encaminhamento
Orquestrador aplica a FICHA-M (m03–m06); Especificador trata m01, m02, m07; depois a proposta vai a Andraus. Decisões E-1..E-5 (Andraus respondeu em 2026-11-27: só Andraus; retirar STOP; opção (b); Minor v1.2→v1.3; arquivo à parte).

<!-- ACHADOS-ESTRUTURADOS
R1-m01|MENOR|C10|ADV-12 (d) espera fsm_row F37 a partir de AGUARDANDO apoiado só no parecer R3; F01 Estado "—" + D4.2 (7) "linha não aplicada" admite F29; from_state não verificado|ancorar o estado de origem no Plan (BASpec-MDC-001) e torná-lo observável (from_state) no cenário de falha
R1-m02|MENOR|C01|frase de retomada em RULE-MDC-003 (h) excepciona RULE-MDC-010 (b)/BASpec-010 sem nomear a exceção lá; não declarada no escopo nem na compatibilidade|toda exceção a regra geral nomeada no próprio texto da regra geral e listada no escopo/compatibilidade da errata
R1-m03|MENOR|C01|T24 verifica MDC_NOT_PHASE1_TRANSITION mas D3.1 l.708 e checks §2 l.73 não recebem T24|ao criar cenário, Grep por cada code que ele verifica e propagar à D3.1 e ao checks §2
R1-m04|MENOR|C06|"as outras 14 de 'to = '" — Grep dá 10|contagem copiada da saída do Grep, não estimada
R1-m05|MENOR|C07|R2-m05 atribuído "aplicado_m" no ESQUELETO, que diz "desenho"|citar o valor por ID ao atribuir classificação de arquivo
R1-m06|MENOR|C06|linha "— (T22)" diz "não conferida por git" após conferência do Orquestrador (git show 366af09)|atualizar rótulo de inferência quando a evidência Classe D chega antes da revisão
R1-m07|MENOR|C04|RULE-MDC-004 (d) nova delega à SPEC-015 o meio de aviso à Fase 0 sem propagar a "Requisitos a outras Specs" (l.1070)|todo requisito novo a outra Spec listado na seção de requisitos no mesmo passo
-->

<!-- FICHA-M {"achados":[
{"id":"R1-m03a","sev":"MENOR","arquivo":"governance/propostas/SPEC-008/ERRATA-PLAN-SPEC008-4-CONDICOES-PROPOSTA-2026-11-27.md","antigo":"; T24 |` *[antes: a linha vigente acima]*","novo":"; T24 |` *[antes: a linha vigente acima]*. Idem, linha `MDC_NOT_PHASE1_TRANSITION`: `| 011 (c) | T11 (b) |` → `| 011 (c) | T11 (b); T24 |` *[antes: \"T11 (b)\"]* (R1-m03).","condicao":"§2.9 propaga T24 também à linha MDC_NOT_PHASE1_TRANSITION da D3.1"},
{"id":"R1-m03b","sev":"MENOR","arquivo":"governance/propostas/SPEC-008/ERRATA-PLAN-SPEC008-4-CONDICOES-PROPOSTA-2026-11-27.md","antigo":"RULE-MDC-011, coluna D7: `T11` → `T11, T24`.","novo":"RULE-MDC-011, coluna D7: `T11` → `T11, T24`. **§2, linha `MDC_NOT_PHASE1_TRANSITION`** — `T11 (b)` → `T11 (b); T24` (R1-m03).","condicao":"§2.11 propaga T24 à linha MDC_NOT_PHASE1_TRANSITION do checks §2"},
{"id":"R1-m04","sev":"MENOR","arquivo":"governance/propostas/SPEC-008/ERRATA-PLAN-SPEC008-4-CONDICOES-PROPOSTA-2026-11-27.md","antigo":"as outras 14 de \"to = \" no","novo":"as outras 10 de \"to = \" no","condicao":"Grep 'to = ' no plan.md = 11 ocorrências (1 notice.to + 10 finais de palavra)"},
{"id":"R1-m05","sev":"MENOR","arquivo":"governance/propostas/SPEC-008/ERRATA-PLAN-SPEC008-4-CONDICOES-PROPOSTA-2026-11-27.md","antigo":"classificação \"aplicado_m\" em `governance/propostas/SPEC-008/FICHA-ESQUELETO-PLAN-R2.json` (só natureza, sem texto)","novo":"classificação \"aplicado_m\" (R2-m04, m08, m09, m11; R2-m05 = \"desenho\", com entradas a/b/c na FICHA-M) em `governance/propostas/SPEC-008/FICHA-ESQUELETO-PLAN-R2.json` (só natureza, sem texto)","condicao":"atribuição igual ao ESQUELETO l.24–53"},
{"id":"R1-m06","sev":"MENOR","arquivo":"governance/propostas/SPEC-008/ERRATA-PLAN-SPEC008-4-CONDICOES-PROPOSTA-2026-11-27.md","antigo":"— `[INFERÊNCIA]`, não conferida por git |","novo":"— conferido pelo Orquestrador por `git show 366af09` (2026-11-27): conteúdo idêntico, só a fronteira do bloco mudou |","condicao":"linha '— (T22)' sem rótulo de inferência não conferida"}
]} -->
