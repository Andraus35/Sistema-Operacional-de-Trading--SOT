# PARECER DO REVISOR SOT — SPEC-006 errata v1.12 (revisão por delta, revisor.md §3-bis) — 2026-10-18

> **Transcrição pelo Orquestrador** do retorno do Revisor SOT (Sonnet 5.5, `CLASSE-TAREFA: S2`), que não tem Write/Edit (ENF-03) e devolveu o texto no retorno. Conteúdo reproduzido sem mudança de mérito; seções de passos e tabelas resumidas onde indicado. **Não é homologação; só Andraus homologa.**

## 1. Veredito
**CONFORME condicional** — 0 Críticas · 0 Médias · **5 Menores** (m1..m5, §5). Teto: o gate de código rodou fora da sessão do Revisor (revisor.md §3). A H-001 deixou de ser bloqueador (revisor.md §8; ata DHR-H001-001 §3).
Hashes revisados (conforme `governance/propostas/SPEC-006/DELTA-ERRATA-v1.12-2026-10-18.txt`; o Revisor não recalculou): plan.md `479baab698c6c04ac84cb05c01f9492a3a41651332bef43be82a36fd8e441b7a` · checks.md `1081a4f2f6177516305ad1fa08f2294009c74ca12e980d1a2151f2b002dd404b`.
**Classificação PROPOSTA a Andraus (o Revisor não decide): Minor/aditiva.** Base: diff completo (40 hunks) só reescreve o estado do COMO; todo "−" tem o texto anterior reproduzido; nenhuma mudança em RULE-CKG, INV-CKG, BASpec, EARS, EC, T ou ADV; a ata declara "Minor/aditiva". Ressalvas para Andraus pesar: **m3** (ADV-09) e **m2**.

## 2. Pré-condições do delta
32 de 122 blocos (26% < 50%), Complexidade inalterada, parecer anterior condicional (não NÃO CONFORME Crítica) ⇒ delta permitido. Base do HERDADO = plan.md `0f461e88…` (edição editorial pós-homologação, DHR-SPEC006-003 §7) e checks.md `239a233e…` (correção n-d, conferida: procede). Sem os sha256 das fontes do parecer anterior ⇒ blocos inalterados = **HERDADOS CONDICIONAIS**, compensados por amostra ampliada.

## 3. Alinhamento e gates
ROADMAP:37/:177, atomic-spec:378, revisor.md §8 e a ata DHR-H001-001 conferem (D1 Opção C; D2 Opção D desenhada e não ligada; D3 licença; D5 revisão por gatilho; §3 "sem alterar regra/BASpec/EC"; §4 eficiência medida só no BUILD). Gates **declarados pelo Orquestrador, não verificados pelo Revisor:** validate_spec_sot PASS 13/13 · revisor_gate PASSOU_D · check_invariants 0 (avisos informativos: BL-003 2→3; 25 linhas "Corrigido sem assertiva", preexistentes). Assertivas do checks.md §19: as 8 conferidas por Grep no plan.md.

## 4. Os 8 focos (resumo)
1. **Mérito alterado sem declaração: nenhum.** Contagens: 74 cabeçalhos (13 BASpec + 6 EC + 23 ADV + 19 T + 13 EARS). Exceção declarada: ADV-09 (m3).
2. **Frases vigentes "H-001 ABERTA/INDETERMINADO":** nenhuma fora de colchete de preservação/histórico; duas ocorrências fora de colchete com anotação adjacente (plan.md:203 e :1313) — aceitáveis (INV-07).
3. **Preservação confirmada** (texto anterior reproduzido em cada "−").
4. **Abertas** (G-001, M-001, J-001, N-001, K-001, C-001, WF-D03, ECC-03-001, CKG-STRUCT-ORIGIN-001, timeout `PENDING_ANCESTOR`) **continuam ABERTAS**; `CONVICTION_HISTORY_UNDEFINED` (19 linhas) intacta.
5. **Rastreabilidade:** nenhum fato inventado; imprecisões em m1/m2.
6. **Reancoragem** de RULE-CKG-011, BASpec-CKG-011 e EC-CKG-006: não muda modo de falha nem nível (EC-006 segue E1/fail-closed). "Até medir" sem limiar — coerente com RULE-MET-01/UNC; não é achado.
7. **checks.md §19:** executável e coerente.
8. **Reescrita de "H-001 FECHADA" → "decisão do mecanismo físico FECHADA":** semanticamente neutra (mesmo referente e atribuição). Causa-raiz: `ids_abertos_do_status` (`scripts/gate_extra.py`) lê os IDs do Status e não consulta o ROADMAP — **falso positivo do detector, não do texto**; sugere ajuste do detector (consultar "Decisões FECHADAS"). Custo residual: grafia dupla dificulta busca por ID.

## 5. Achados (todos Menores, não bloqueiam)
- **m1** — Âncoras imprecisas: "(DHR-H001-001 §4/§5)" para CKG-STRUCT-ORIGIN-001 e `PENDING_ANCESTOR` (plan Status l.7, checks §19 l.310) e "estudo §9" para eficiência multi-salto (plan l.118, 1631, 1665); corretas: estudo §6, §7 R4, §8 G2; ata §4 e D5.
- **m2** — Afirmações físicas só do estudo [PROPOSTA] sem etiqueta: D9 "o log só-inserção é a trilha" (estudo R3 ressalva adulteração por DBA; cadeia de hash seria regra nova) e "sem chamada a LLM por escrita" (todas [INFERÊNCIA], nada medido). Etiquetar (RULE-EPI).
- **m3** — ADV-09 muda o critério de verificação spec-time por nota ("grep de fechamento = 0" → "toda menção atribui a Andraus/DHR-H001-001"); texto antigo mantido; única alteração que toca VERIFICAÇÃO — Andraus ciente ao classificar. Nenhuma ação obrigatória.
- **m4** — Item "[v1.12] Eficiência de consulta multi-salto" listado sob abertas/[DECISÃO NECESSÁRIA] mas não é decisão nova — rotular como incerteza RULE-UNC [INFERÊNCIA].
- **m5** — Âncoras por número de linha obsoletas (checks.md:274 → `plan.md:1104`); referenciar por ID/âncora.

## 6. Passos (resumo)
Passo 2 PASS · Passo 3 (CC-01..12) PASS · Passo 4 PASS com m1/m2 · Passo 5-bis A/B/C sem achados além de m2 (EPI) · Passo 6 PASS · Passo 7 (ENF) PASS · Passo 8 (decisões abertas) PASS. Limite: sem web nem Bash; não atesta veracidade das fontes do estudo nem os hashes.

## 7. Cobertura
Conferidos agora: cabeçalho/Status, princípio fundador, histórico 1.12, nota BL-003, CC-09/N8–N17, Herança/Delta, Cobertura×lacuna, D0/Non-goals, RULE-CKG-011, INV-CKG-02, BASpec-CKG-010/011, D4, D5, D8/ADV-09, ADV-14, D9, esqueleto/I-O, EC-CKG-006, Natureza/Roteamento/Riscos, Impacto/Tasks, Autopré-check, Etiquetagem, lista final de abertas, checks.md §19. Dependentes por Grep: H-001 (67 ocorrências), CKG-011, EC-CKG-006, ADV-09, ADV-14, `PENDING_ANCESTOR`, `CONVICTION_HISTORY_UNDEFINED`. Amostra anti-leniência (9 blocos inalterados, sem achados): EC-CKG-001..006; RULE-CKG-008; contagens; CCM-001 l.58/78; CEM-001 l.608–615; negação de `conviction`; checks §17 n-d; DHR-SPEC006-003 D2; ROADMAP/atomic-spec. Não conferido: estado de merge da ata; mapa; 25 avisos "sem assertiva"; conteúdo web do estudo; qual motor guarda o log do Blackboard (SPEC-004).

## 8. Encaminhamento (só Andraus)
Decidir a classificação (proposta: Minor/aditiva); o Revisor recomenda corrigir m1 e m2 antes da ata (editoriais); o ajuste do detector `decisoes_abertas_fechadas` é matéria do Orquestrador.

---
## Adendo do Orquestrador (2026-10-18) — o que foi feito depois do parecer
Aplicadas, como correção **classe M** (texto prescrito pelo parecer, sem regra/campo/mecanismo novo), as Menores **m1, m2, m4 e m5** (9 linhas no plan.md e 4 no checks.md; **m3** fica como ciência de Andraus). Os gates rodaram de novo: validate_spec_sot PASS 13/13 · revisor_gate PASSOU_D · check_invariants 0. **Hashes finais:** plan.md `718340652a79e04200e8603a130c86ff31c29eef315ff5f39bc031cb5cb5c58b` · checks.md `1ee11bb7652f59dc5560bf115f78746b4cb3453c33971dcb605443e84b9506b5` — **diferentes dos auditados** (§1); a diferença é só a das Menores acima e **não foi reauditada pelo Revisor** (precedente: DHR-SPEC006-003 D5; aceitação é de Andraus). O detector `gate_extra.py` **não** foi alterado (fora da autorização).

---
## Adendo do Revisor (guarda pós-revisor, DHR-AUDITOR-EXTERNO-018) — transcrição pelo Orquestrador
- **G1 (núcleo do Passo 0 aberto):** `governance/RULES.md` — famílias RULE-BB-004, DEC-01, MET-01, EPI-01..03, CAU-01..03, UNC-01..03 existem; RULE-CKG-* não está em RULES.md (registro físico diferido, RULE-HG-02), como o plan declara. `backlog/RMR-001` — BL-035 (l.142) = CKG-STRUCT-ORIGIN-001, `Em espera`, decisão aberta; BL-003 (l.110) com a nota de 2026-10-18, coerente.
- **G2 (gate do harness):** revisor_gate PASSOU_D, sinais H = 0. WARN `check_refs` em `checks.md:188` **descartado** (prosa histórica da v1.9, N-04; não é comando; fora do diff). O resultado do gate não é parecer do Revisor.
- **Achado novo m6 (Média, pré-existente — não introduzido pela v1.12):** plan.md:51 dizia BL-003 `Em espera`, mas RMR-001:110 o registra `ATIVADO` (Andraus, 2026-10-17, DHR-BACKLOG-001); a v1.12 editou a linha sem corrigir o estado. Item tratado (Disposição PARCIAL), logo não é achado de gate, mas o estado declarado é inexato (Passo 4-ter, M1(b)). Veredito mantido: **CONFORME condicional** para o delta; estritamente, m6 é Média (revisor.md §6 ⇒ NÃO CONFORME); por ser pré-existente, editorial e a errata já homologada, a decisão (aceitar × reabrir) é de Andraus.
- **Decisão de Andraus (chat, 2026-10-18):** corrigir agora, uma linha. O Orquestrador aplicou em plan.md l.51 (BL-003) e l.52 (BL-011, mesmo defeito, conferido em RMR-001 l.118), texto anterior preservado. **Hash final do plan.md: `dd5a609f30078515c673a9e66990c54ee0c5e2ab881b6bcc51d6a573579b6255`** (checks.md inalterado: `1ee11bb7…`). Gates: validate_spec_sot 13/13 · revisor_gate PASSOU_D · check_invariants 0. Não reauditado pelo Revisor.

