# PARECER DO REVISOR SOT — ABERTURA da SPEC-007, 3ª rodada (por delta, S2/Sonnet) — 2026-10-19

> **Transcrição resumida pelo Orquestrador** do retorno do Revisor (sem Write/Edit — ENF-03). Não é homologação; só Andraus homologa. Base: commit `7241ab3`; delta e gates em `governance/propostas/SPEC-007/DELTA-ABERTURA-v3-2026-10-19.txt` (gates rodados pelo Orquestrador). Hashes declarados: ABERTURA `5a276ea378ba…` · research `023542d1a064…` (não recomputados pelo Revisor).

## 1. Veredito
**CONFORME condicional** (teto: gate fora da sessão do Revisor). **0 Críticas, 0 Médias, 7 Menores novas (R3-01..R3-07).** N-01..N-09 corrigidos no texto atual (ressalvas Menores em N-02/N-04/N-05; N-08: cláusula "B1–B12 só mudaram formato" não verificável sem git). **A abertura PODE SEGUIR a Andraus para homologação**; recomendada uma passada curta em R3-01/R3-02/R3-03 (não é condição). O "condicional" vem só do gate.

## 2. Achados novos (Menores)
- **R3-01** (`ABERTURA.md:204-206, :209`) — a nota diz que 8.1 e 8.3 tocam `SPEC-006 plan.md:482` e K-001 "sem fechá-los", mas um "sim" decide na prática parte de "quem mantém a allowlist / quem hospeda o juízo CKG-008". Alinhar com a Q-4: avisar que "sim" decide parte do item e deve constar na ata. K-001 segue aberta.
- **R3-02** (`ABERTURA.md:33, :121`; `research.md:251`) — ainda listam "emissor autenticado/allowlist" como [DECISÃO NECESSÁRIA] inteira; a Q-8 já registra a identidade autenticada como normativa (RULE-CKG-009). Separar "já normativo (identidade autenticada, falha ⇒ recusa)" de "em aberto (quem mantém a lista, quem hospeda o juízo)".
- **R3-03** (`ABERTURA.md:194-195`) — Q-7(a) composta; exemplo da nota cita B13 e "relatórios de teste", que não conferem: trocar por B10/§5.1 e "políticas, contratos e especificações".
- **R3-04** (`ABERTURA.md:185, :208`) — corpo da Q-4 ainda cita "SPEC-018"; em `:208` há 5ª confirmação sem pergunta explícita ("Concorda?").
- **R3-05** (`ABERTURA.md:183, :191`) — colchetes INV-07 de Q-3 e Q-6 com reticências (o trecho continua no texto atual).
- **R3-06** (`ABERTURA.md:130`) — "Entrega do Plan sobre COL-EXP-05" em tom imperativo, sem etiqueta: marcar `[PROPOSTA]` (a D8 só obriga o Plan a *tratar* o resíduo).
- **R3-07** (`research.md:101`) — requisito (i) "instrução embutida… nunca muda o comportamento" mais forte que o alcance honesto da mesma linha: reescrever como "não vira efeito". Editorial: ordem R-8, R-11, R-12, R-9, R-10.

## 3. Verificação
17 citações do Benchmark conferidas no clone somente-leitura (`inteligencia-sot@0abd22e`), todas batem. `governance/RULES.md` aberto: famílias RULE-004, ECC-01..06, MECH-01/03, PD-01, MM-05, EPI-01/02, CAU-01, MET-01 existem; RULE-CKG-004/009/010 vivem em `SPEC-006/plan.md`. Coerência ABERTURA × research × ata (`AGENTS.md:137`, D7, D8, R-8/R-11/R-12) conferida; divergência única = R3-02. CONS-01: nenhuma pergunta fecha decisão aberta. Limites: gate não visto rodando; sem web; sem git (hashes/diffs não recomputados); clone lido como DADO.

## 4. O que ainda vai a Andraus
As 8 perguntas de abertura (Q-ABERTURA-1..8, com 8.1–8.4); em Q-4 e Q-8 o "sim" decide parte de "produtor/gatilho de promoção" (`SPEC-006 plan.md:976`) e, via R3-01, parte do item `plan.md:482` — devem constar na ata da homologação; registro pós-homologação de `CONFLICT-MAP.md:147` (COL-EXP-05 → SPEC-007) e nota do BL-011; licença/titularidade (Q-7 b, c1, c2). Seguem abertas: K-001, G-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção.

---
## Adendo do Orquestrador (guarda pós-revisor G1/G3, DHR-AUDITOR-EXTERNO-018) — 2026-10-19
- **G3:** (a) as 6 citações `docs/HARNESS-QUALIDADE.md:3/:4`, `docs/governanca/POLITICA.md:19`, `docs/governanca/CONTRATOS.md:3`, `docs/GATE-ARTEFATO-IMPLEMENTADO.md:35`, `docs/REVISOR-ADVERSARIAL-HIBRIDO-2026-10-13.md:12` e `rag/traducao/documento-ativo.json:55` são do **repositório-benchmark** (`inteligencia-sot@0abd22e`): existem no clone com a linha citada. (b) `SPEC-006/plan.md:474/:395/:976` são **`specs/features/SPEC-006/plan.md`** (forma abreviada): l.474 = RULE-CKG-009, l.395 = RULE-CKG-004, l.976 = "Produtor/gatilho de promoção = [DECISÃO NECESSÁRIA]" — conferido. (c) `ROADMAP.md:37` e `:180`: os "trechos" são paráfrases do Revisor, não aspas; conferido o conteúdo: l.37 registra "RULE-REG-001 — FECHADA (Andraus, 2026-09-28, DHR-REG-001)"; l.180 registra "P0 — CRITICAL · Profundidade-alvo: D0–D8". Nenhum achado depende de citação inexistente.
- **G1 (`atomic-spec.md` não aberto na 3ª rodada):** a 3ª rodada foi por delta e herdou a conferência da 1ª, que abriu o `atomic-spec.md` (inclui `:238`). Conferência complementar do Orquestrador (Grep): §15 "Abertura de Spec/Dossiê" (emendas EUA-E21, RULE-ECC-04/05/06) presentes; matriz §3 com "Knowledge Graph → CRITICAL · D0–D7" (l.67, emenda SPEC006-MATRIZ) — a SPEC-007 propõe CRITICAL D0–D8, o pin do ROADMAP (l.180); `atomic-spec.md:238` "Commit crítico (TMP, KG publicado, transição crítica) → E3 mínimo" confere. Não é parecer do Revisor.
