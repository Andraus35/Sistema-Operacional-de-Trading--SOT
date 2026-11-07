# Parecer do Revisor — Proposta de Abertura da SPEC-008 — R3 delta (S2, sonnet) — 2026-11-07

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura; resumo fiel). Alvo: `specs/features/SPEC-008/ABERTURA.md` (+ `research.md`). Pareceres anteriores: R1 e R2 (+ adendo G1) nesta pasta.
> MODO: delta (BASE 758fec1)
> SHA256-ALVO: e534515b25c004f87ee451a9cec0b6e8c2ffd5b2ec9a5f9ba24a2e7de5af7e57 (valor recebido do Orquestrador; o Revisor não recalculou)
> GATE-D: GATE NÃO VERIFICADO (ferramenta indisponível; abertura não tem plan.md para o gate determinístico).
> **Veredito: CONFORME condicional** — 0 Críticas, 0 Médias, 1 Menor (R3-m01, editorial, não bloqueia). Pendências: gate não verificado; escolhas de Andraus (P-1..P-13, P-12.1, CONF-1..5); J-001/N-001 para o limiar macro. Este parecer não homologa nada.

## 1. Resultado por achado do R2
- **R2-M01 (P-12 Opção A) — resolvido.** Três travas: (a) ciclo novo pedido pela Fase 0/SPEC-015 ou por Andraus, nunca pela Fase 1 sozinha (exceção = P-12.1); (b) nada reaproveitado, sem julgamento de Classe D e sem pular etapa (S8); (c) teto de N rearmes por hipótese-origem por Killzone, parâmetro (CC-09), sem N ⇒ nenhum rearme, estouro ⇒ pedido recusado na entrada com motivo, registro e aviso, sem estado novo. Âncora conforme o adendo G1 (RULE-MECH-03 não incide literalmente). Recomendação passou de A para C; a escolha segue de Andraus.
- **R2-m01 (linhas mistas SPEC-003) — resolvido.** 6 RE parciais + 3 RE inteiras = 9 (inalterado); regra de busca com precedência (orçamento/latência/invocação prevalecem sobre a vizinhança de WF-K0x); testada contra SPEC-048 plan l.342, l.1131 e research l.123 (todas FICA).
- **R2-m02 (seis ramos de WF-F01) — resolvido.** Enumerados item a item; ramo 4 único com transição escrita (`EM_RISCO → RECUSADO`, [INFERÊNCIA]); ramo 6 → P-13; CF-9 e R-17.

## 2. Conferências transversais
CONS-01 OK (nenhuma decisão aberta fechada) · nada decidido por Andraus · nenhum estado/transição novo · INV-07 OK · P-12/P-12.1/P-13 em linguagem de trader com opções e recomendação · referências cruzadas e contas de tamanho (2.499 / 1.895 / 1.439 / 1.491) consistentes · amostra anti-leniência sem achado.

## 3. Achado
- **R3-m01 (Menor, editorial, não bloqueia) — ABERTURA §15 l.327.** O item CONS-01 do autopré-check lista "P-11, P-12, CONF-5" sem P-12.1 e P-13 (criados na R3). Acrescentar mantendo o texto anterior como *[antes: …]*.

## 4. Encaminhamento
CONFORME condicional → segue para Andraus (P-1..P-13, P-12.1, CONF-1..5). Nenhum Plan antes da homologação. Observação para o Plan (não é achado): se P-11 = C, o Constitution Check do Plan declara a P-11 como pendência (CC-01 é Crítica); se P-12 = A, o Plan precisa de BASpec para a contagem entre ciclos (depende de G-001/SPEC-009).

<!-- ACHADOS-ESTRUTURADOS
R3-m01|MENOR|C06|Lista de pontos novos no item CONS-01 do Autopré-check (§15 l.327) não foi atualizada com P-12.1 e P-13 criados na R3|Ao criar pergunta ou ID novo, grep da lista anterior de IDs em todo o documento (§14, §15, §16) e atualizar cada ocorrência no mesmo passo
-->

<!-- FICHA-M {"achados":[{"id":"R3-m01","sev":"MENOR","arquivo":"specs/features/SPEC-008/ABERTURA.md","linha":327,"antigo":"marcados como pergunta (P-11, P-12, CONF-5), não como invariante.","novo":"marcados como pergunta (P-11, P-12, P-12.1, P-13, CONF-5), não como invariante. *[antes: \"(P-11, P-12, CONF-5)\"]*","condicao":"ABERTURA §15 l.327 lista os pontos novos sem P-12.1 e P-13, que o item R3 (l.333) já cita"}]} -->

---

## Adendo — guarda pós-revisor G1 (2026-11-07) — Revisor SOT, somente leitura
> Transcrição pelo Orquestrador. O Revisor da R3 abriu `ROADMAP.md` (l.199-204, 36, 524), `governance/RULES.md` (l.518-529 RULE-ECC-07; l.555 RULE-MECH-03), `atomic-spec.md` (l.11-14, 315, 439) e `backlog/RMR-001_Painel_Backlog.md` (BL-003 l.110, BL-011 l.118, BL-026/043/044/045/046 l.133 e l.150-153) e conferiu o que a abertura afirma a partir deles.
- **Resultado: nada muda.** Veredito segue CONFORME condicional (0 Críticas, 0 Médias, 1 Menor R3-m01, já aplicado pelo Orquestrador como classe M). Nada ficou "não verificado" nos quatro arquivos.
- Ressalvas: o gate segue NÃO VERIFICADO (sem ferramenta/`GATE-D`); o painel RMR-001 foi lido por grep só nos itens citados (varredura de ATIVADO por script é do Orquestrador); os rótulos de disposição ([STRUCT-13]) dos 5 BLs são dado do Orquestrador (detector não rodado pelo Revisor).
