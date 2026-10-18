# Parecer do Revisor SOT — SPEC-006 errata v1.10 (rodada por delta) — 2026-10-17

> Gravado pelo Orquestrador a partir do relatório do subagente Revisor SOT (somente leitura: não consegue gravar arquivo). Texto do Revisor = dado/parecer consultivo; **não** é homologação (só Andraus homologa). Base do delta: 1c307d2 (v1.9). Evidência do gate: PASSOU_D, 0 sinais H, sha256 do plan 8a5f4e67f8b2… igual ao do delta. Teto de veredito: CONFORME condicional (gate não rodou dentro da sessão do Revisor, revisor.md §3; H-001 ABERTA, §8).

## 1. Veredito
**NÃO CONFORME** — 0 Críticas, 1 Média (N-08, nova), 3 Menores novas (n-a, n-b, n-c).
N-07 FECHADO · m-A PARCIAL · m-B PARCIAL · m-C FECHADO · m-D FECHADO.
A Média é de correção trivial e aditiva; sem ela o veredito seria CONFORME condicional (teto do gate).

## 2. Gate e escopo
- O Revisor não reexecutou o gate (sem Bash). Avisos não bloqueantes `corrigidos_sem_assertiva` (checks.md:157-204) e `check_refs` (ERRO=2, WARN=3) fora do delta; as 5 linhas novas do §17 têm assertivas executáveis.
- Rodada por delta: 19 blocos alterados lidos; dependentes lidos: D4, node_record, `canonical_state_transition_record`, EC-001, EC-005, D6 passo 2, tabela §D3.1; grep de resíduos no plan inteiro.

## 3. Cobertura por bloco
- **Conferidos linha a linha (14):** cabeçalho/histórico (l.30-40), def:RULE-CKG-008 (l.435-464), def:RULE-CKG-010 (l.477-534), BASpec-008 (l.889-915), BASpec-010 (l.937-961), T09 (l.1183-1189), ADV-04 (l.1279), ADV-21 (l.1333), §D3.1 (l.732, l.737), EARS (l.702, l.704), I/O schema (l.1387, l.1404), Herança/Delta (l.1591-1599), Etiquetagem (l.1641), Autopré-check §7 (l.1664-1667).
- **Por grep:** D2 e D2.1 (l.141-145, l.713 ss.) — sem resíduo de atribuição ao CCM-001. d4-algoritmo (l.1033, l.1038) conferido (D4 l.1038 já traz outcome_ref/no_outcome). critérios-de-aceitação-ears (EARS-8 e EARS-10) conferidos.
- **Dependentes lidos:** EC-CKG-001 e EC-CKG-005 (l.1452, l.1500), D6 passo 2 (l.1095), esquema `causal` (l.1428), Bloco A (l.1583-1588).
- **HERDADO (103 inalterados):** por hash. **Amostra anti-leniência:** EARS-1..7, 9, 11..13 (l.695-707), os 13 cabeçalhos BASpec, os 19 T, os 23 ADV e os 6 EC (por grep de cabeçalho), BASpec-009 (l.917-935). Sem regressão.
- **Fontes abertas por linha:** CCM-001 l.58, l.78, l.111-119 (Cap.5, M-001 ABERTA em l.117); CEM-001 l.446-447, l.460-466 — conferem com o que o plan cita.

## 4. Status N-07 e m-A..m-D
- **N-07 — FECHADO.** RULE-CKG-010 (l.484-486, l.503-515) nega `conviction` por padrão (`CONVICTION_HISTORY_UNDEFINED`); CCM-001 l.58/78/117 confirma que não define transições, estado inicial nem registro. Predicado de trajetória e `canonical_history_ref` de conviction = [PROPOSTA]/[DECISÃO NECESSÁRIA]. Sem atribuição residual no corpo normativo (só a narração do changelog v1.9, l.39-40, correta por INV-07). Propagado em: esquema l.1387/l.1404, D4 l.1033, EARS-10 l.704, BASpec-010 l.943-946, §D3.1 l.737, T09(c) l.1185-1188, ADV-21 (d)(g) l.1333, Herança l.1591/l.1594, Etiquetagem l.1641. hypothesis/evidence intactos.
- **m-A — PARCIAL.** RULE-CKG-008 (l.435-444), EARS-8 (l.702), ADV-04(h) (l.1279), BASpec-008 VERIFICADO POR (l.911-914), §D3.1 l.732 e D4 l.1038 incluem outcome_ref/no_outcome. Ficaram com o núcleo de 4 campos: BASpec-008 GATE DE SAÍDA (l.908), EC-CKG-005 PRECOND (l.1500) e esquema `causal` (l.1428) → N-08.
- **m-B — PARCIAL.** EARS-8 (l.702) e VERIFICADO POR (l.911-913) alinhados. O ENTÃO do BASpec-008 (l.899) cita o núcleo só "ver RULE-CKG-008 [N-02]", sem m-A; GATE DE SAÍDA (l.908) ainda lista 4 campos.
- **m-C — FECHADO.** Subcódigo com pai próprio (§D3.1 l.732; `CAUSAL_FIELDS_MISSING` em l.731 não o contém). Caminho legítimo em RULE-CKG-008 l.445-453 (INVALIDA antiga + NOVA CAUSA com `valid_from` próprio ⇒ chave natural distinta (relation_type, from, to, target_relation_id, valid_from), D4 l.1037). Chave sem `mechanism` confere.
- **m-D — FECHADO.** RULE-CKG-010 l.497-502 e ADV-21(f) (l.1333) declaram defesa em profundidade; CEM-001 l.446-447 ("Estado padrão") e l.460-466 conferem. Ressalva editorial em n-b.

## 5. Achados novos
- **N-08 [Média] — núcleo causal imutável mais estreito que a regra, em 3 pontos.** Locais: BASpec-CKG-008 GATE DE SAÍDA (plan.md:908), EC-CKG-005 PRECOND (plan.md:1500, nível E3) e esquema `causal` (plan.md:1428) só vetam alterar mechanism/direction/conditions/regime. RULE-CKG-008 l.435-437 e ADV-04(h) exigem negar também a troca de outcome_ref/no_outcome. Como o contrato E3 (ENF-01) não veta a troca, o cenário (h) seria aceito pelo contrato e rejeitado só pela regra: contradição interna (M2), contra o "propagado por referência" da v1.10. **Ação:** nesses três pontos, trocar a lista de 4 campos por "núcleo causal definido em RULE-CKG-008 [N-02/m-A]" ou acrescentar `outcome_ref`/`no_outcome`; no mesmo ajuste, completar o ENTÃO do BASpec-008 (l.899).
- **n-a [Menor] — assertiva fraca.** O `assert-absent:"conviction COMPUTED∨GATED_PASS"` (checks.md §17, linha de N-07) só detecta essa string exata. **Ação:** acrescentar assert-absent de "CCM-001 mantém histórico" e "esteve em COMPUTED" no corpo.
- **n-b [Menor] — imprecisão editorial.** ADV-21(f), plan.md:1333, diz que ACTIVE é "único predecessor"; pela tabela CEM-001 l.460-466, ARCHIVED também tem SUPERSEDED e INVALIDATED como predecessores. RULE-CKG-010 l.497-500 está correto. **Ação:** alinhar a redação à RULE.
- **n-c [Menor] — procedência da decisão de Andraus.** "NEGADA por padrão — decisão de Andraus" (plan.md l.144 e l.1641) só tem registro no HANDOFF-SPEC006-2026-10-17.md:9 (dado de estado, não ata). A ata de homologação da errata deve registrá-la (AGENTS.md §10). Observação para Andraus: a v1.7 baselined já admitia conviction por estado; a negação restringe isso, e a classificação "Minor/aditiva" é decisão dele.

## 6. Verificações sem achado
- Contagens cabeçalho × corpo: 13 BASpec, 13 EARS (l.695-707), 6 EC, 19 cenários (T01..T19), 23 ADV — conferem com changelog e checks.md.
- CONS-01: H-001, M-001, J-001, N-001 e demais seguem ABERTAS; histórico da conviction tratado como [DECISÃO NECESSÁRIA]. CONST-01/CC-02: CCM-001 e CEM-001 só citados.
- Bloco C (N8-N17): EPI, CAU, DEC (INV-05 preservado), SEM, ONT, INQ, CTF, UNC, PRB, MET sem achado.
- Bloco B adversarial (2 BASpecs CRITICAL): em BASpec-008, se o ENTÃO (g)/(h) nunca ocorresse, o EC-005 não detectaria = N-08. Em BASpec-010 a negação (d)/(g) é observável por `conviction_denied_history_undefined`.
- Passo 4-bis (Dossiê): não reaberto; a errata não altera pesquisa.

## 7. Teto de veredito
Gate não rodou dentro da sessão do Revisor (§3) e H-001 ABERTA (§8): mesmo sem a Média, máximo CONFORME condicional — que não é homologação nem avanço automático. Só Andraus homologa a errata (ata DHR-SPEC006-003) e decide H-001, o histórico da conviction (M-001) e a dona de H-001.
Condição para nova revisão: corrigir N-08 (e, de preferência, n-a, n-b, n-c); reexecutar o gate; nova rodada por delta (BASpec-008, EC-005, esquema `causal`, ADV-21, checks §17).
Encaminhamento: devolver ao Especificador.
