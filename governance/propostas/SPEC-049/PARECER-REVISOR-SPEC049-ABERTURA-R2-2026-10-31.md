# Parecer do Revisor — Proposta de Abertura da SPEC-049 (WikiRAG Reading View) — R2 integral (S2, sonnet) — 2026-10-31

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura). Alvo: `specs/features/SPEC-049/ABERTURA.md` (revisão 2) + `research.md`.
> MODO: integral
> SHA256-ALVO: 6599e96bcef5d760b9fdab3d88f7ea928ed587b1862c1e324163cc81879ed6b8 (valor recebido; o Revisor não calculou — sem Bash)
> TOKENS: 134928
> **Veredito: CONFORME condicional** — 0 Críticas, 0 Médias, 2 Menores novos (R2-m01, R2-m02); os 9 achados do R1 estão resolvidos. Delta não aplicável (15 de 20 blocos alterados > metade, revisor.md §3-bis.6): revisão integral, com delta e parecer R1 só como auxílio de leitura.

## 1. Veredito
Condicional por três causas, nenhuma falha do Especificador: (i) `revisor_gate` indisponível na sessão do Revisor (gates do Orquestrador = dado de estado); (ii) P-1..P-7 e C-1..C-4 dependem de Andraus; (iii) teto do Revisor numa abertura é CONFORME condicional. Nada decidido por Andraus; nenhuma decisão aberta fechada.

## 2. Passo 0 e passos 2-8
Passo 0 mantido (ROADMAP l.192-193/523, atomic-spec §15, RULES RULE-ECC-06/07; C-2 em DHR-SPEC048-001 l.28). Passos 2, 3, 4/4-bis, 7, 8: PASS. Passos 5/5-bis/6 não incidem no Plan (pergunta adversarial às candidatas 1, 5 e 7 → R2-m02; M01 do R1 fechada). Bloco C: EPI com herança etiquetada `[INFERÊNCIA]`; CAU, DEC, SEM, ONT, INQ, CTF, UNC, PRB, MET sem achados; nenhuma BASpec cruza para execução.

## 3. Conferência dos achados do R1 (fonte aberta)
| Achado R1 | Situação | Evidência |
|---|---|---|
| M01 (`valid_at`) | Fechada | propagação completa (ver §4) |
| m01 (derivação) | Fechada | contas refeitas contra os cabeçalhos do plan da SPEC-048 (§4) |
| m02 (≈850 vs ≈880) | Fechada, sem recaída | research l.201 e ABERTURA §3 dizem ≈1.380 (MEDIUM); Grep por 880/1.250/850 só acha linhas `[antes:]` |
| m03 (hash circular) | Fechada | research §3.1 l.92 = §3.6 = S7 |
| m04 (granularidade) | Fechada, com ressalva R2-m02 | S5 (a)/(b), cond. 12; código existe em SPEC-007 l.1678, 873, 2066, 3070 |
| m05 (etiqueta) | Fechada | SPEC-007 l.432-443 vinculante; l.444-447 [PROPOSTA] |
| m06 (ENF-07, CC-11, R-9) | Fechada | cond. 9, 10, 11; atomic-spec l.273/292/305; imprecisão editorial: "SPEC-007 l.433-436" para caminhos E3 (estão em l.438-441), sem efeito |
| m07 (lista de linhas) | Fechada | Grep de `SPEC-049` em SPEC-048/plan.md: 31 linhas = research §8.3; `reading_view_ref` l.1103/1267/1439 |
| m08 (citação literal) | Fechada | SPEC-007 l.1224/1225/1228 literais; RULE-KFH-001/P-11 separada |

## 4. M01 e m01 — conferência detalhada
**M01:** `valid_at` como 4º campo da entrada propagado a S1 (iv), S6, S7, BASpec 1, §4, CC-10, §7 H-001, R-5/R-8, P-5, C-4, §12/§14, §15 cond. 2 e §16; research §0, §3.1, §3.3, §3.6, §6 (Grep: 8 ocorrências no ABERTURA, 3 no research). A contradição não reabre: corte = `recorded_at`; `valid_at` = tempo de validade; sem `valid_at` no pedido, a regra o preenche com o instante do corte e grava na entrada; nunca lê o relógio; "mesma entrada ⇒ mesma página" fecha para os quatro campos.
**m01:** D2 l.416-745 = 330; BASpecs l.808-1098 = 291; D7 l.1215-1403 = 189; soma 810 (67,5/BASpec); ECs l.1490-1652 = 163 (8 ECs, ~20 cada); D8 l.1404-1478 = 75; restante 887; erratas −48; §7-bis em MEDIUM −39. HIGH 839+675+60 = 1.574 (≈1.570; faixa 1.417–1.622); MEDIUM 800+520+60 = 1.380 (faixa 1.242–1.428); extrapolação proporcional 1.935/12×10 = 1.612. Pela RULE-ECC-07 (RULES l.518-531) o limiar de 1.600 pede confirmação de Andraus: tratar HIGH como exigindo confirmação (P-7) é a leitura conservadora correta; em MEDIUM a P-7 não se aplica.

## 5. Processo do Dossiê
ECC-04: `sources/` inalterado; aspas novas do research são texto do SOT, não `[EXTERNO]`; sem achado. ECC-06: §4 inalterado. ECC-07: conferido. CONS-01: nenhuma decisão aberta tratada como fechada; P-2, P-3, P-6, P-7 e C-4 são propostas; `valid_at` é "nome proposto". Backlog (§9) inalterado; `backlog_triggers --abertura` = 0 itens (dado do Orquestrador, não verificado pelo Revisor).

## 6. Achados novos
**R2-m01 (MENOR, C07/C02):** `valid_from`/`valid_to` são campos de RELAÇÃO na SPEC-006 (plan l.322, 395, 710; SPEC-007 RULE-KFH-009 l.683-685), e o ABERTURA os atribui ao "item" (S1 (iv), S6, research §3.3). Não localizou campo de janela em nó `learning` (Interface ponto 1, SPEC-007 l.1224). Impacto: `valid_at` só tem efeito em itens com janela; se nós `learning` não tiverem janela, quase todos os blocos sairiam "não informada" e a M01 ficaria inócua (o fallback "validade não informada ⇒ sinal, nunca atual" evita vigência falsa; por isso Menor). Ação: etiquetar `[INFERÊNCIA]` a premissa de que o item tem janela, dizer de onde vem (campo do nó, relação de invalidação ou estado `INVALIDATED_IN_TIME`, SPEC-006 l.1073) e acrescentar condição ao Plan (derivar a validade da SPEC-006/007, sem inventar campo). Sem decisão de Andraus.
**R2-m02 (MENOR, C01):** S5 (b) (lado ausente da entrada ⇒ bloco com "lado não exibível") não foi propagada ao research §3.8 l.122 ("contradição sem os dois lados ⇒ não emite"); research §3.5 diz "análogo a `CONTRADICTION_SILENT_RESOLUTION_FORBIDDEN`" enquanto ABERTURA S5 (a) e cond. 12 dizem "por referência, não redefinido". O código é produzido pelo registro da contradição na SPEC-007 (EC-KFH-010, l.1678; D3.1 l.873); SPEC-007 l.2067-2068 passa "lado a lado na WikiRAG" a outra Spec. Ação: alinhar research §3.8 e §3.5 a S5 (a)/(b); no Plan, declarar se o compilador reutiliza o código da SPEC-007 ou usa um próprio (prefixo `WRV`).

<!-- ACHADOS-ESTRUTURADOS
ID|SEV|CATEGORIA|CAUSA|PREVENCAO
R2-m01|MENOR|C07|valid_from/valid_to atribuídos ao item mas definidos na SPEC-006 (RULE-CKG-004, S4) para relações; nó learning sem campo de janela localizado|Ao propor campo de entrada ligado a uma regra herdada, abrir a regra e conferir a quem o campo pertence (nó versus relação) antes de atribuí-lo ao item
R2-m02|MENOR|C01|Granularidade nova do não-emite (S5 a/b) não propagada ao research §3.8/§3.5; código da SPEC-007 tratado como análogo num texto e reutilizado no outro|Após mudar uma regra de recusa, fazer Grep do mesmo conceito no Dossiê e na Proposta e declarar de quem é o identificador do código
-->

<!-- FICHA-M {"achados":[]} -->
(Nenhum dos 2 Menores é estritamente mecânico: ambos exigem julgamento do Especificador. Zero achados M.)

## 7. Cobertura (integral)
ABERTURA cabeçalho/Status/§1 (validades 2027-01-29 e 2027-02-28 recalculadas), §2 S1-S11 e contratos, §3, §4, §5-§6, §7-§10, §11-§16: conferido agora. research §0, §3.1, §3.3, §3.5, §3.6, §3.8, §6, §8.2, §8.3: conferido agora; demais seções lidas sem alteração relevante; §4 e capturas HERDADOS do R1. `sources/` (14 SRC, 6 REPO, `_LIMITACAO`): HERDADO do R1, sem releitura nem hash comparado (o sha256 de `sources/` não veio no pedido).

## 8. Não pude verificar
Resultado de qualquer gate · sha256 do alvo/research (sem Bash) · veracidade das páginas web e números dos repositórios; adulteração de `sources/` · se algum nó `learning` carrega janela de validade no desenho final da SPEC-006/007 · estado git e `backlog_triggers --abertura` · interpelação formal ao Especificador.

## 9. Encaminhamento
Abertura pronta para decisão de Andraus (P-1..P-7, C-1..C-4). Os 2 Menores vão ao Especificador (classe O) no mesmo envio da próxima correção ou ficam como condição da homologação, à escolha de Andraus (AGENTS §12). Não bloqueiam. CONFORME condicional não é homologação nem autorização do Plan.

## 10. Adendo do Orquestrador — guarda pós-revisor (DHR-AUDITOR-EXTERNO-018) — dado de estado, não parecer
- **G3 (`SPEC-048/plan.md:31` — arquivo não encontrado): falso positivo.** O "31" é a **contagem** de linhas ("Grep de `SPEC-049` em SPEC-048/plan.md: 31 linhas"), não um número de linha. Conferido pelo Orquestrador em 2026-10-31: a contagem por Grep de "SPEC-049" no plan da SPEC-048 = 31; `reading_view_ref` nas linhas 1103, 1267 e 1439 (como o parecer e o research §8.3 declaram).
- **G1 (`backlog/RMR-001` não aberto na sessão do R2): conferido pelo Orquestrador.** O painel foi aberto: nenhuma linha contém o gatilho `spec:SPEC-049` (0 ocorrências) e os itens BL-003, BL-010, BL-011, BL-017, BL-029 e BL-035 existem nas linhas 110, 117, 118, 124, 136 e 142; `python scripts/backlog_triggers.py --abertura SPEC-049` = 0 itens vinculados. As afirmações do §9 do ABERTURA que dependem do painel (disposições BL-010/035 REFERÊNCIA, BL-017/029 FORA, nenhum vínculo por regra) permanecem coerentes. O R1 já havia aberto o painel (parecer R1 §2/§3 item 7).
