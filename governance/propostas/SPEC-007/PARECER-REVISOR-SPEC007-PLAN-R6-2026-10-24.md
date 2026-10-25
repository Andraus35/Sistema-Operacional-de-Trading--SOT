# Parecer do Revisor — Plan reduzido da SPEC-007 v2.2 (CANDIDATA), rodada 6 (S2) — 2026-10-24

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura). **Veredito: CONFORME condicional** — 0 Críticas, 0 Médias, 3 Menores (r6-n1..r6-n3). Condição: o Revisor não executou o gate (ferramenta ausente); o Orquestrador rodou `revisor_gate.py` completo sobre o plan.md = `PASSOU_D`, sem sinais (ver adendo). Isto **não é homologação**: o Plan segue candidato; baseline só por ato de Andraus. Nenhuma decisão aberta fechada (CONS-01). Base do delta: 7168d76 (v2.1). Revisão por leitura dirigida dos blocos citados e dependentes.

## R5-M1 — RESOLVIDA em substância
Expressão de VALIDADO (IDs gravados pela CIM ∧ judge≠former ∧ parte D = PASS ∧ ∀ afirmação CLEAR ∧ linha "rótulo" CLEAR ∧ `judge_invocation_ref.content_refs` ∋ `candidate_ref@version`) conferida na RULE-KFH-006 (l.556-561), BASpec-KFH-006 (l.962-998; GATE l.982-984; VERIFICAÇÃO b1..b4), EC-KFH-003 (l.1580-1581), EARS 6 (l.819), D5 (l.1175), D4.5 (l.1160), contrato (l.1230-1236, 1256-1263), ADV-31(a) (l.1529) e T25 (l.1442-1458). Precedência FALHA > INDETERMINADO igual na RULE e no EARS 6.

## Menores da R5
r5-n1..r5-n7: todas OK (F0.4 `formed_inference=false`, T10, ADV-30(d) com a2; RULE-KFH-019 (f5) a/b/c e registro de que (f3) é mais estrita que a letra da ata; E-4 [PROPOSTA] e RU-8, conferida contra SPEC-006 l.1398-1422; ADV-27 (i)(j), ADV-28 (e)-(h), `locus_basis`; `resolved_content_hash` em T25; D3.1 sem `||`; rótulos v2.2).

## Regressões e contagens
87 cabeçalhos = 12 RULE + 2 INV + 12 BASpec + 9 EC + 18 cenários + 22 ADV + 12 EARS: conferem. Colchetes INV-07 presentes. CONS-01: G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, gatilho de promoção, livro (Q7c) e forma de confirmar a identidade de Andraus seguem abertas; P-13 (errata E-1..E-4) segue [PROPOSTA]. Passos 2-8 e 5-bis nas partes alteradas: PASS.

## Menores novas (não bloqueiam; editoriais)
- **r6-n1** RULE-KFH-006 e checks.md l.21 dizem "expressão única, idêntica", mas a redação difere ("IDs gravados pela CIM" × "pelo runtime"; EC-003 não repete as conjunções "IDs/judge≠former/parte D" dentro da cláusula do VALIDADO; D5 e EARS 6 resumem sem a conjunção da invocação). Ação: "equivalente" em vez de "idêntica", ou padronizar e repetir.
- **r6-n2** ADV-28 (l.1523): rótulos F e G com estados diferentes no mesmo caso ((a') F envio FALSE/G TRUE × preâmbulo de (e)-(h) ambos PRIVADO/envio FALSE × F0.3 F@h1 envio TRUE); QUANDO só para (a')(c)(d) depois do ENTÃO de (e)-(h). Ação: fontes distintas (F'/G') ou "sobrescrevendo a F0.3"; reordenar.
- **r6-n3** `locus_basis` (contrato l.1262; ENTÃO de ADV-28) não é checado na VERIFICAÇÃO de ADV-28 (e)-(h) nem em T25, e a RULE-KFH-019 (a)/(b) não manda a CIM gravá-lo. Ação: acrescentar `locus_basis == …` e uma frase na RULE.

## Pendências declaradas
(a) gate verificado pelo Orquestrador (feito: `PASSOU_D`); (b) decisão/homologação de Andraus: se quer só a letra da ata em (f3); a errata P-13 (E-1..E-4); a emenda à SPEC-020 (metade F1); extensão de INVALIDATION a "só Andraus" (r4-n8, [PROPOSTA]); demais decisões abertas. Citações `inteligencia-sot@0abd22e` (7): não verificáveis (clone ausente). Fidelidade dos Anexos ao v2.0/v2.1: não verificável (sem git).

## Encaminhamento
Revisor sugere corrigir r6-n1..r6-n3 junto, sem nova rodada (editoriais, nenhuma muda comportamento). Aguarda decisão de Andraus.

## Adendo da guarda / Orquestrador (2026-10-24)
`python scripts/revisor_gate.py specs/features/SPEC-007/plan.md` (completo, não só `--rapido`) = `PASSOU_D`, 0 sinais H, teto CONFORME condicional; avisos anteriores eram texto histórico dos Anexos. Isso cumpre a condição (a) do Revisor; a elevação a CONFORME pleno e a homologação continuam fora deste parecer.

## Adendo 2 da guarda pós-revisor (Orquestrador, 2026-10-24; DHR-AUDITOR-EXTERNO-018)
- **G1:** `ROADMAP.md` aberto ao vivo: l.34 registra a divisão decidida (DHR-SPEC007-002) e SPEC-007 sem Plan aprovado; l.37 "Decisões FECHADAS" registra DHR-SPEC007-003/004 com K-001 e M-001 abertas. Confere com o que o Plan e o parecer afirmam. Nada a retirar.
- **G2:** `revisor_gate.py` = `PASSOU_D`, 0 sinais H. Avisos (l.31, 3345, 3421, 3422, 3443): l.31 = linha da v1.0 na tabela de versões; as demais ficam dentro do Anexo R (texto v1.x preservado e recuado, INV-07). A RULE-CKG-008 está definida em `specs/features/SPEC-006/plan.md` l.429-472. O corpo vigente tem 12 BASpec (recontado pelo Revisor, 87 cabeçalhos). Falsos positivos; sem achado novo.
