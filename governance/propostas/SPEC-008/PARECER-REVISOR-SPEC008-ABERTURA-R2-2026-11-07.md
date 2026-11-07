# Parecer do Revisor — Proposta de Abertura da SPEC-008 — R2 integral (S3, opus) — 2026-11-07

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura; resumo fiel). Alvo: `specs/features/SPEC-008/ABERTURA.md` (+ `research.md`, `sources/`). Parecer anterior: `PARECER-REVISOR-SPEC008-ABERTURA-R1-2026-11-07.md`.
> MODO: integral
> SHA256-ALVO: 07639472016a7c00efce105886e9252bf9cfd96815e1b8af80f1eab8d426fdd8 (valor recebido do Orquestrador; o Revisor não recalculou)
> **Veredito: NÃO CONFORME** — 0 Críticas, 1 Média (R2-M01), 2 Menores (R2-m01, R2-m02). Teto, mesmo corrigido: CONFORME condicional (GATE NÃO VERIFICADO; J-001/N-001 pendentes para o limiar macro).

## 1. Síntese
- As 10 correções classe O da R1 resolvem o que pediam (M01..M05, m02, m04..m07): conferidas com fonte aberta (grep exaustivo de 37 linhas da SPEC-003 refeito e batendo; contas de tamanho 2.499 / 1.895 / 1.439 / 1.491 refeitas; WF-A02/WF-F01/WF-K02, EUA-E23 l.113/115, CHM-001 l.753-754 conferidos).
- INV-07 preservado; nenhuma decisão aberta fechada; WORKFLOW não editado; nenhum estado novo na FSM.

## 2. Achados
- **R2-M01 (Média) — P-12, Opção A (a recomendada), ABERTURA l.270 e l.273.** A correção do R1-M05 criou três problemas dentro da opção recomendada: (a) não diz quem origina o ciclo novo (pela S1 o pedido de ciclo vem da Fase 0/SPEC-015 ou de Andraus); (b) não há regra fixa para reaproveitar contexto (julgamento numa Spec Classe D; no ramo 3 tensiona S8 "nunca pula etapa"); (c) laço sem teto — tetos de S8 são "por ciclo", abrir ciclo novo os zera (viola RULE-MECH-03). Ação: declarar originador, regra fixa de validade do contexto (ou não reaproveitar) e teto entre ciclos (rearmes por hipótese-origem por Killzone); alternativa: recomendar a Opção C. Sem decidir por Andraus.
- **R2-m01 (Menor) — research §8.3 (l.232, 237, 239, 248; regra l.267) e ABERTURA §8.** Linhas plan l.98, 191, 224, 1149 misturam WF-D01/D02/D04 e estão "RE" inteiras; WF-D04 (papel do ICT) fica na SPEC-008. Regra de busca sem precedência (ex.: SPEC-048 plan l.342). Marcar "RE (parte WF-D01/D02); FICA (WF-D04)" e acrescentar à regra que WF-D04 fica e que orçamento/latência/invocação prevalecem sobre a vizinhança de WF-K0x.
- **R2-m02 (Menor) — S7 (l.42) e tabela de dono por transição.** "Só o ramo 4 cai literalmente; os demais dependem de P-12" — P-12 cobre só ramos 1, 2, 3, 5; o ramo 6 (reentrada após stop, WORKFLOW l.70) fica sem dono/destino. "Literalmente" é forte: trocar por [INFERÊNCIA] e declarar destino/dono do ramo 6 ou perguntar.

## 3. Encaminhamento
Os três vão ao Especificador (classe O); nenhum é mecânico. Próxima rodada: trazer `GATE-D:` com o mesmo SHA256-ALVO. Este parecer não homologa nada.

<!-- ACHADOS-ESTRUTURADOS
R2-M01|MEDIA|C08|Opção recomendada de P-12 (encerrar + alarme novo em ciclo novo) escrita sem conferir fronteira com a Fase 0 (quem abre ciclo), regra fixa de validade do contexto e teto entre ciclos|Ao propor opção a Andraus que cria ciclo/alarme novo, declarar originador, critério determinístico e teto que sobrevive ao reinício do ciclo (RULE-MECH-03)
R2-m01|MENOR|C07|Linhas mistas WF-D01/D02/D04 marcadas RE inteiras e regra de busca sem precedência entre "junto de Killzone" e "junto de orçamento/latência"|Marcar RE parcial em toda linha mista e testar a regra de busca contra a própria tabela (inclusive SPEC-048 l.342) antes de propô-la
R2-m02|MENOR|C10|Cobertura dos seis ramos de WF-F01 afirmada ("os demais dependem de P-12") sem conferir o ramo 6|Ao afirmar cobertura de lista numerada, enumerar item a item
-->

<!-- FICHA-M {"achados":[]} -->
