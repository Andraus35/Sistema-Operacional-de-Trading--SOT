# Parecer do Revisor — Manager Contract v0.3 (proposta) — R3 — 2026-11-07

> Transcrição pelo Orquestrador do retorno do Revisor SOT (somente leitura). Objeto: `specs/features/SPEC-008/MANAGER-CONTRACT.md` v0.3 (árvore de trabalho; 362 linhas); âncora de roteamento `ABERTURA.md` (CRITICAL). Anteriores: R1 e R2 na mesma pasta. Gate **NÃO VERIFICADO** (não é plan.md; sem `revisor_gate` em nuvem) ⇒ teto CONFORME condicional. Limites declarados: sem Bash/git (comparou por marcadores `[antes]`, parecer R2 e reflog); o hash `8ea5d9a` não pôde ser conferido pelo Revisor (o Orquestrador conferiu: `git log -1 -- specs/features/SPEC-008/ABERTURA.md` = `8ea5d9a`); o Revisor revisou a árvore de trabalho — o commit entregue a Andraus deve ser igual a ela (confirmado pelo Orquestrador antes do commit desta rodada).

## Veredito
**CONFORME condicional.** Nenhuma Média/Crítica. 7 Menores: 6 mecânicos (FICHA-M R3-m01..m06) e 1 classe O não bloqueante (R3-m07).
- R2-m05: (a) resolvido em parte (R3-m02), (b) resolvido, (c) resolvido. Classe M do R2 preservada.
- A-1..A-5 transcritas sem distorção relevante; MMC-001 só aparece neste arquivo (sem colisão de ID); A-2 filha, SPEC-050 segue candidata; A-3 destino `governance/` sem mover (o "registro no CATALOGO" vem da recomendação do §9 — a ata deve confirmar); A-5 (1) e (2) transcritas.
- Recorte da P-7 fiel à pergunta A-5(2) da v0.2 e etiquetado `[INFERÊNCIA]`; o documento não registra que Andraus o confirmou — a confirmação (dada em chat, 2026-11-07, na rodada v0.3) deve constar da ata.
- §10 idêntico à DHR-SPEC008-001 §5 (CONS-01 OK); campo "CHANGED" não existe (CC-08 / RULE-HD-02 usam INHERITS/ADDED/MODIFIED/REMOVED) — confere; CONST-01/CC-02 intactos; continua "PROPOSTA — não é baseline".

## Achados (todos Menores)
- **R3-m01 (C01):** cabeçalho "Natureza" diz que o único conteúdo novo é o decidido por Andraus; contradiz ADDED (b)/(c) — FICHA-M.
- **R3-m02 (C06):** §8.2-bis diz cobrir "todas" as seções; faltam §8.1, §8.2, §8.2-bis — FICHA-M.
- **R3-m03 (C02, EPI):** "supressão silenciosa (RULE-HV-02)" sob `[FATO]` A-5(1) é inferência (fronteira não é herança fixa) — FICHA-M.
- **R3-m04 (C01):** Autopré-check desatualizado após a divisão do ADDED em (a)/(b)/(c) — FICHA-M.
- **R3-m05 (C02):** "agente novo" sem qualificador (l.359) — FICHA-M.
- **R3-m06 (C02):** "arbitra conflitos entre agentes" sem qualificador (l.60) — FICHA-M.
- **R3-m07 (C02), classe O, não bloqueante:** §3.1.3/§8.2-bis tratam como obrigação a Classe D/C que `ABERTURA.md` §4 (l.140, l.25) chama de orientação; só "nenhuma H/P ⇒ volta a Andraus" (l.144) é firme; tensão com a coluna "não herdável" do §3.

## Encaminhamento
Orquestrador aplica a FICHA-M, roda `build_map --check`/`check_refs`; R3-m07 ao Especificador (classe O) se Andraus quiser. Depois, Andraus homologa; a ata registra A-1..A-5, o recorte da P-7 e o registro no CATALOGO (A-3). Não verificado: chat de Andraus; veracidade de `sources/`; comparação por git.

<!-- ACHADOS-ESTRUTURADOS
R3-m01|MENOR|C01|Cabecalho Natureza diz que o unico conteudo novo e o decidido por Andraus, mas ADDED (b)/(c) traz [PROPOSTA] e [INFERENCIA] do Especificador|Ao reestruturar o ADDED, reconciliar toda frase-resumo (cabecalho, autopre-check, §14) com os grupos do bloco
R3-m02|MENOR|C06|Linha 163 afirma que a tabela do §8.2-bis cobre todas as secoes; faltam §8.1, §8.2, §8.2-bis|Toda alegacao "todas/cada" conferida contra o sumario de secoes antes da entrega
R3-m03|MENOR|C02|Linha 171 enquadra como supressao silenciosa (RULE-HV-02), sob [FATO] A-5(1), uma fronteira declarada nao-heranca fixa|Separar a decisao literal de Andraus do enquadramento normativo derivado ([INFERENCIA])
R3-m04|MENOR|C01|Autopre-check (linha 286) diz ADDED so [PROPOSTA], desatualizado apos divisao (a)/(b)/(c)|Reexecutar o autopre-check depois da ultima edicao do bloco Heranca/Delta
R3-m05|MENOR|C02|"agente novo" sem qualificador na linha 359|Grep de "agente" sem qualificador em texto novo antes da entrega
R3-m06|MENOR|C02|"arbitra conflitos entre agentes" sem qualificador na linha 60|Idem R3-m05, incluindo blocos herdados de rodadas anteriores
R3-m07|MENOR|C02|§3.1.3/§8.2-bis tratam como obrigacao a Classe D/C que ABERTURA.md §4 (l.140, l.25) chama de orientacao; tensao com a coluna "nao herdavel" do §3|Ao citar fonte nao-baseline, preservar a modalidade (orientacao x obrigacao) — RULE-SEM-03
-->

<!-- FICHA-M {"achados":[
{"id":"R3-m01","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"o único conteúdo novo é o que Andraus decidiu em chat de 2026-11-07 (A-1..A-5 — §9, §8.3 ADDED).","novo":"o único conteúdo novo **normativo** é o que Andraus decidiu em chat de 2026-11-07 (A-1..A-5 — §9, §8.3 ADDED (a)); os demais acréscimos são `[PROPOSTA]` de leitura ou `[INFERÊNCIA]` de alcance (§8.3 ADDED (b) e (c)).","condicao":"§8.3 ADDED (b)/(c), linhas 223-233"},
{"id":"R3-m02","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"a tabela abaixo cobre **todas** as seções do contrato:","novo":"a tabela abaixo cobre **todas** as seções do contrato, exceto §8.1, §8.2 e §8.2-bis, que são o próprio mecanismo de herança (RULE-HV-01..04 e RULE-HD-04, já vigentes; o índice de leitura do §8.2 é `[PROPOSTA]` — §8.3 ADDED (b)):","condicao":"tabela do §8.2-bis sem linhas para §8.1/§8.2/§8.2-bis"},
{"id":"R3-m03","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"qualquer outra mudança = supressão silenciosa (RULE-HV-02)","novo":"mudança sem essa homologação não é admitida (enquadrá-la como supressão silenciosa, RULE-HV-02, é `[INFERÊNCIA]` — a fronteira não é herança fixa)","condicao":"RULES.md l.417: RULE-HV-02 incide sobre requisito herdado; A-5(1) = não herança fixa"},
{"id":"R3-m04","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"ADDED só com itens de leitura/filiação/requisito marcados `[PROPOSTA]`.","novo":"ADDED em três grupos (§8.3): (a) decisões A-1..A-5 de Andraus, (b) `[PROPOSTA]` do Especificador, (c) `[INFERÊNCIA]` de alcance. *[antes: \"ADDED só com itens de leitura/filiação/requisito marcados `[PROPOSTA]`.\"]*","condicao":"§8.3 linhas 215-233"},
{"id":"R3-m05","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"Nenhuma regra, campo, estado, transição ou agente novo além do decidido em A-1..A-5.","novo":"Nenhuma regra, campo, estado, transição ou agente de trading novo além do decidido em A-1..A-5.","condicao":"GLOSSARIO §1-bis: agente sem qualificador é ambíguo"},
{"id":"R3-m06","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"arbitra conflitos entre agentes;","novo":"arbitra conflitos entre agentes analíticos;","condicao":"GLOSSARIO §1-bis; §2.2 do próprio contrato"}
]} -->
