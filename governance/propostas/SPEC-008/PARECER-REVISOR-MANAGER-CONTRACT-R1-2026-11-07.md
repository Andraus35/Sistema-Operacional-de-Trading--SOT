# Parecer do Revisor — Manager Contract v0.1 (proposta) — R1 — 2026-11-07

> Transcrição pelo Orquestrador do retorno do Revisor SOT (somente leitura). Objeto: `governance/MMC-001_Manager_Contract.md` (âncora de roteamento: `ABERTURA.md`, CRITICAL). Modo integral, 1ª rodada. Gate determinístico **NÃO VERIFICADO** (ferramenta indisponível; não é plan.md) ⇒ teto CONFORME condicional mesmo sem achados.

## Veredito
**NÃO CONFORME** — 4 Médias e 8 Menores. Atendidos: nenhuma decisão aberta aparece fechada; nenhum modelo canônico redefinido; as 4 divergências de §9 A-4 são reais; nenhum agente/estado novo. Falhas: duas âncoras [FATO] que não dizem o que o contrato afirma (M-01, M-04); INHERITS herda textos que o próprio contrato declara divergentes, sem precedência (M-02); herança de fonte sem versão baseline (M-03).

## Achados
- **M-01 (§6 item 6.4):** "O Manager não reduz sozinho a classe de modelo de nenhum agente" com âncora [FATO] CEE-001 v2.0 §10 S1 e S5; o canon (CEE-001 l.236) diz S1 = "Nenhum agente pode reduzir **sua própria** classe de modelo autonomamente". Sujeito alterado. Ação: transcrever S1 e S5 literalmente; a regra sobre outros agentes só como [INFERÊNCIA] ancorada (CEE §9.3, pausa emergencial "via Scheduler").
- **M-02 (§8.3 INHERITS × §1 × §9 A-4):** herda ADR §2.4 ("TMP → Bot"), WF-F02 (SPEC-015) e WF-K02 ("SPEC-008/015"), que A-4 declara divergentes, e §1 manda prevalecer o texto-fonte. Ação: declarar precedência (INV-05 emendado EUA-E19a sobre ADR §2.4; CONF-1/CONF-5 sobre o nº de Spec em WF-F02/WF-K02, até Andraus corrigir as fontes) ou excluir os trechos; sem regra nova.
- **M-03 (§8.3, §3.1.3, §4):** herda de `ABERTURA.md §2, §4`, não-baseline e sem versão (RULE-HD-04 exige ID+VERSÃO baseline). Ação: ancorar na linha de decisão da ata DHR-SPEC008-001 §1 (P-2, CONF-1, CONF-5, P-4..P-9) ou fixar data/commit e declarar não-baseline (`[DECISÃO NECESSÁRIA]` se Andraus precisar dar versão).
- **M-04 (§10, J-001):** "decisão de envio da Fase 2 fica como parâmetro" com [FATO] DHR-SPEC008-001 §5; a ata não diz isso (§3 ii fala só do limiar "conclusivo" da Fase 1) e omite os limiares-piloto interinos vigentes (INV-03; CEE §11 S2/S4: ≥70% e 7/9). Ação: remover ou reescrever como [INFERÊNCIA].
- **m-01 (C02):** "agente" sem qualificador (GLOSSARIO §1-bis regra 1) — FICHA-M.
- **m-02 (C02):** homônimo "Fase" (pipeline WORKFLOW × Fase do ADR × FASE ROADMAP/RISK) não declarado.
- **m-03 (C10):** gate não-LLM da FSM (WF-F02) sob "Fase 1"; a FSM atravessa a Fase 2 (SPEC-014, H/P) — declarar como obrigação transversal.
- **m-04 (C04):** A-4 omite: RULE-DEC-01 (TMP/Synthesis/B-001), ADR §7 (J-001 → SPEC-015), ADR §4.1/§6 (Event Bus), WF-F01 "reset" × P-12; fronteira Fase 0↔1 (P-12 C, S1) ausente do §4.
- **m-05 (C04):** INHERITS não cobre WF-F01, WF-T01, DHR-SPEC005-002, DHR-DEC-001, CHM-001, AGENTS §6; ADDED omite o [PROPOSTA] de §8.1 (parte em FICHA-M).
- **m-06 (C07):** §5.6 conclui "fontes não fixam a montagem" sem ponderar ROADMAP l.247 (RISK-SPEC-022), WF-K04, WF-06.
- **m-07 (C04):** §6 sem a tensão CEE §9.3 × S2 nem o alcance de P-7; título mais amplo que S2.
- **m-08 (C01):** decisões locais da abertura (CONF-1, Classe orientativa) viram obrigação herdável por SPEC-014/015 (§8.2), em tensão com "não antecipa a abertura" e DHR-EUA-E23 §2 item 3.

## Encaminhamento
Devolver ao Especificador (classe O) M-01..M-04 e m-02..m-08; ajustes mecânicos (m-01, parte de m-05) pela FICHA-M do Orquestrador. A-1..A-4 seguem `[DECISÃO NECESSÁRIA]` para Andraus. Nova revisão exige: toda âncora [FATO] verificável; INHERITS sem fonte divergente sem precedência; referências a não-baseline declaradas; nenhuma regra nova fora do ADDED. Não verificado: chat de Andraus, gate D, mapa.

<!-- ACHADOS-ESTRUTURADOS
M-01|MEDIA|C07|Salvaguarda CEE §10 S1 parafraseada como [FATO] com sujeito alterado (propria classe -> classe de outros); literal perdido|Transcrever salvaguarda constitucional literal (RCN-001); derivacao so como [INFERENCIA] com ancora propria
M-02|MEDIA|C01|INHERITS herda ADR §2.4, WF-F02 e WF-K02 que o proprio A-4 declara divergentes; regra de leitura do §1 manda prevalecer o texto-fonte desatualizado|Ao listar divergencia conhecida, declarar no INHERITS qual texto prevalece ou excluir o trecho
M-03|MEDIA|C04|Pai vertical herda de ABERTURA.md, nao-baseline e sem versao, contra RULE-HD-04 (ID+VERSAO baseline)|Ancorar heranca na ata homologada (linha de decisao) ou fixar versao/commit da fonte
M-04|MEDIA|C08|§10 atribui a DHR-SPEC008-001 §5 que a decisao de envio da Fase 2 fica como parametro; a ata nao diz isso e os limiares-piloto interinos (INV-03) vigoram|Conferir por string cada [FATO] em lista de decisoes; nao acrescentar parentese interpretativo sem etiqueta [INFERENCIA]
m-01|MENOR|C02|"agente" sem qualificador em documento novo (GLOSSARIO §1-bis regra 1)|Varredura de "agente" sem "de trading"/"de construcao" no autopre-check
m-02|MENOR|C02|Homonimo "Fase" (pipeline WORKFLOW x Fase do ADR x FASE do ROADMAP/RISK) nao declarado|Declarar acepcoes concorrentes (CC-10) quando o termo e decisivo
m-03|MENOR|C10|Gate nao-LLM da FSM do ciclo (WF-F02) posto sob "Fase 1"; a FSM atravessa a Fase 2 (SPEC-014)|Obrigacao de FSM inteira declarada como transversal as Fases
m-04|MENOR|C04|A-4 omite divergencias: RULE-DEC-01 (TMP/Synthesis/B-001), ADR §7 J-001 (SPEC-015), ADR §4.1/§6 Event Bus, WF-F01 reset x P-12; fronteira P-12 C omitida no §4|Varrer cada fonte do INHERITS contra atas posteriores antes de declarar a lista
m-05|MENOR|C04|INHERITS nao cobre WF-F01, WF-T01, DHR-SPEC005-002, DHR-DEC-001, CHM-001 e AGENTS §6 citados no corpo; ADDED omite o [PROPOSTA] do §8.1|Cruzar mecanicamente as fontes citadas no corpo com o INHERITS e os [PROPOSTA] com o ADDED
m-06|MENOR|C07|§5.6 conclui que as fontes nao fixam a montagem sem ponderar ROADMAP l.247 (RISK-SPEC-022), WF-K04 e WF-06|Buscar todas as ocorrencias do termo-chave antes de inferir ausencia
m-07|MENOR|C04|§6 nao registra a tensao CEE §9.3 (pausa emergencial) x S2 nem o alcance de P-7; titulo mais amplo que S2|Ao consolidar, trazer tensoes de canon ja registradas na abertura
m-08|MENOR|C01|Decisoes da abertura da SPEC-008 (CONF-1, Classe orientativa) viram obrigacao herdavel por SPEC-014/015, contra "nao antecipa a abertura"|Declarar o efeito vertical de cada decisao local ao promove-la ao pai
-->

<!-- FICHA-M {"achados":[
{"id":"m-01a","sev":"MENOR","arquivo":"governance/MMC-001_Manager_Contract.md","antigo":"ID normativo nem agente.","novo":"ID normativo nem agente de trading.","condicao":"GLOSSARIO §1-bis regra 1: 'agente' qualificado (AT) na linha Natureza do cabeçalho"},
{"id":"m-01b","sev":"MENOR","arquivo":"governance/MMC-001_Manager_Contract.md","antigo":"não é agente nem componente separado","novo":"não é agente de trading nem componente separado","condicao":"GLOSSARIO §1-bis regra 1: 'agente' qualificado na linha 2.4"},
{"id":"m-01c","sev":"MENOR","arquivo":"governance/MMC-001_Manager_Contract.md","antigo":"**não** criam agente adicional","novo":"**não** criam agente de trading adicional","condicao":"GLOSSARIO §1-bis regra 1: 'agente' qualificado na linha 2.5"},
{"id":"m-05a","sev":"MENOR","arquivo":"governance/MMC-001_Manager_Contract.md","antigo":"como índice (§8.2) — ambos [PROPOSTA].","novo":"como índice (§8.2) — ambos [PROPOSTA]. Filiação da Spec de Tempo (§8.1) = [PROPOSTA], pendente de A-2.","condicao":"ADDED lista todo item [PROPOSTA] do documento, inclusive o do §8.1"}
]} -->
