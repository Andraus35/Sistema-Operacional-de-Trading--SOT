# Parecer do Revisor — Manager Contract v0.2 (proposta) — R2 — 2026-11-07

> Transcrição pelo Orquestrador do retorno do Revisor SOT (somente leitura). Objeto: `specs/features/SPEC-008/MANAGER-CONTRACT.md` v0.2 (commit d544a78); âncora de roteamento `ABERTURA.md` (CRITICAL). Parecer anterior: `PARECER-REVISOR-MANAGER-CONTRACT-R1-2026-11-07.md`. Gate **NÃO VERIFICADO** (ferramenta indisponível; não é plan.md) ⇒ teto CONFORME condicional. Limite declarado: sem Bash, o Revisor não rodou `git show`; comparou com os marcadores `[antes: …]` e com o R1.

## Veredito
**CONFORME condicional.** M-01..M-04 do R1 resolvidas (conferidas nas fontes: CEE-001 l.236/237/240 e §9.3 l.228-230; ADR §2.4; WF-F02 l.71; WF-K02 l.38; WF-F01 l.70; DHR-SPEC008-001 §1/§3/§5; INV-03; CEE §11 S2/S4). m-02, m-03, m-04, m-06, m-07 resolvidas; m-05 e m-08 com resíduos (abaixo); m-01 (classe M) preservada. Nenhuma Média/Crítica nova. Correções espontâneas do Especificador (§2.6, §8.1, A-4 (a) — datas ADR 2026-09-26 × EUA-E19a 2026-09-22) conferem. Nenhuma regra/campo/estado/transição/agente novo; nenhuma decisão aberta fechada (CONS-01); CONST-01 intacto; A-1..A-5 seguem `[DECISÃO NECESSÁRIA]`.
Impedem CONFORME pleno: (1) gate não verificado; (2) homologação depende de Andraus em A-1 (ID, versão e hash da ABERTURA), A-2 (filiação da Spec de Tempo) e A-5 (efeito vertical das decisões da abertura). Observação (não é achado): a P-4 pedia documento "curto"; ≈284 linhas por causa do histórico `[antes]`.

## Achados (todos Menores)
- **R2-m01 (C02, EPI):** §8.2-bis linha 1 rotula `[FATO]` o alcance de itens que são `[INFERÊNCIA]` (§2.6, §3.2.2, aplicação do 6.1, 6.4-a) — FICHA-M.
- **R2-m02 (C10):** exemplo "enviar ou não ao Risco" (§3.2.2) pressupõe seta `EM_SÍNTESE`→final não escrita em WF-F02 (P-12 pendente) — FICHA-M.
- **R2-m03 (C01):** Spec de Tempo tratada como obrigada (§3.1.3, §8.2-bis) enquanto a filiação é `[PROPOSTA]` pendente de A-2 — FICHA-M.
- **R2-m04 (C04):** regras de uso 1/3 do WORKFLOW citadas como `[FATO]` fora do INHERITS; ROADMAP l.35 e §7/§10-bis fora do CONTEXTO — FICHA-M.
- **R2-m05 (C04/C01) — classe O, não bloqueante:** (a) título do §8.2-bis promete "alcance de cada item" mas não cobre §1-bis, §5.6, §10; (b) exceção do §1 não cobre os trechos "NÃO herdados (citados só como divergência)" (ADR §3.3, §4.1, §4.2, §6, §7) — regra geral "vale o texto-fonte" fica ambígua; (c) ADDED não registra a convenção do §1-bis nem as leituras de alcance do §8.2-bis (`[INFERÊNCIA]`, pendentes de A-5). Pode ser tratado junto da homologação.

## Encaminhamento
Orquestrador aplica a FICHA-M (R2-m01..m04) e roda `build_map --check`/`check_refs`. R2-m05 → Especificador (classe O) se Andraus quiser. Não verificado: comparação por git; chat de Andraus; veracidade de `sources/`; mapa.

<!-- ACHADOS-ESTRUTURADOS
R2-m01|MENOR|C02|Linha 1 do §8.2-bis rotula [FATO] o alcance de itens que sao [INFERENCIA] (§2.6, §3.2.2, 6.1 aplicacao, 6.4-a) no instrumento que define a heranca|Em tabela agregadora de alcance, manter a etiqueta propria de cada item e nunca rotular o conjunto
R2-m02|MENOR|C10|Exemplo do §3.2.2 ("enviar ou nao") pressupoe seta EM_SINTESE->final nao escrita em WF-F02 (P-12 pendente)|Conferir todo exemplo de transicao contra a lista literal de setas do WF-F02
R2-m03|MENOR|C01|Spec de Tempo tratada como obrigada (§3.1.3, §8.2-bis) enquanto a filiacao e [PROPOSTA] pendente de A-2|Condicionar toda obrigacao de filha proposta a decisao que a cria
R2-m04|MENOR|C04|Regras de uso 1/3 do WORKFLOW citadas como [FATO] fora do INHERITS; ROADMAP l.35 e §7/§10-bis fora do CONTEXTO|Cruzar mecanicamente toda ancora do corpo com INHERITS/CONTEXTO antes da entrega
R2-m05|MENOR|C04|§8.2-bis nao cobre §1-bis/§5.6/§10; excecao do §1 nao cobre os trechos "NAO herdados (so divergencia)"; ADDED omite a convencao do §1-bis e as leituras de alcance|Ao criar tabela "de cada item", varrer todas as secoes; alinhar a regra de leitura com todas as classes de exclusao do §8.3
-->

<!-- FICHA-M {"achados":[
{"id":"R2-m01","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"`[FATO]` das âncoras de cada linha","novo":"etiqueta própria de cada linha (`[FATO]` ou `[INFERÊNCIA]` — §2.6, §3.2.2, aplicação do 6.1 e 6.4-a são `[INFERÊNCIA]`); alcance = RULE-HV-01","condicao":"RULE-EPI: o agregador não converte inferência em fato"},
{"id":"R2-m02","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"(ex.: enviar ou não ao Risco)","novo":"(ex.: enviar ao Risco; a saída por \"não enviar\" em `EM_SÍNTESE` não é seta escrita em WF-F02 — §3.2.3, P-12)","condicao":"WF-F02 l.71 e DHR-SPEC008-001 §4: nenhuma transição criada"},
{"id":"R2-m03a","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"**Alcance:** só SPEC-008 e Spec de Tempo (§8.2-bis)","novo":"**Alcance:** só SPEC-008 e, se A-2 = sim, Spec de Tempo (§8.2-bis)","condicao":"§8.1: filiação da Spec de Tempo = [PROPOSTA], A-2"},
{"id":"R2-m03b","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"**SPEC-008 e Spec de Tempo**.","novo":"**SPEC-008 e Spec de Tempo** (esta, se A-2 = sim).","condicao":"§8.1: filiação da Spec de Tempo = [PROPOSTA], A-2"},
{"id":"R2-m03c","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"**SPEC-008/Spec de Tempo**: obrigação","novo":"**SPEC-008/Spec de Tempo** (esta, se A-2 = sim): obrigação","condicao":"§8.1: filiação da Spec de Tempo = [PROPOSTA], A-2"},
{"id":"R2-m04a","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"WORKFLOW v2.1: WF-01, WF-04, WF-06, WF-07, WF-C01, WF-T01","novo":"WORKFLOW v2.1: regras de uso 1 e 3, WF-01, WF-04, WF-06, WF-07, WF-C01, WF-T01","condicao":"§3.2.3 cita as regras de uso 1 e 3 como [FATO]"},
{"id":"R2-m04b","sev":"MENOR","arquivo":"specs/features/SPEC-008/MANAGER-CONTRACT.md","antigo":"ROADMAP.md (l.33, l.36, l.247 — estado, não baseline versionado)","novo":"ROADMAP.md (l.33, l.35, l.36, l.247, §7, §10-bis — estado, não baseline versionado)","condicao":"A-4 (f) cita l.35; §1-bis cita §7/§10-bis"}
]} -->
