# ANÁLISE DE PRIORIZAÇÃO — Itens PENDENTES do Backlog (RMR-001)

| Campo | Valor |
|---|---|
| Documento | ANALISE-PRIORIZACAO-BACKLOG-2026-09-28 |
| Tipo | Análise / Proposta (NÃO-normativa; NÃO abre Spec; NÃO promove item) |
| Autor | Especificador SOT |
| Data | 2026-09-28 |
| Escopo | Itens do RMR-001 em estado `Em espera` ou `Proposto` |
| Autoridade | Isto é `[PROPOSTA]`. Promoção/adiantamento de qualquer item é ato de Andraus (RMR-001 §5). |
| Fontes | `backlog/RMR-001_Painel_Backlog.md`, `ROADMAP.md`, `governance/RULES.md`, `reference/SOT-RISK-MASTER-001_Consolidado.md`, `reference/camadas/*` |

> **Status epistemológico (TRACE-06):** o estado atual de cada item é `[FATO NORMATIVO]` (verificado no RMR-001 baseline v1.0). A recomendação de adiantamento é `[PROPOSTA]`. A avaliação de ganho/risco é `[INFERÊNCIA]` derivada dos documentos citados. Nenhuma linha deste documento fecha decisão aberta (CONS-01) nem altera baseline (INV-09).

> **Critério de ordenação:** maior ganho nos 4Es do SOT com menor risco primeiro, na hierarquia `Conformidade > Eficácia > Efetividade > Eficiência > Economicidade` (`governance/RULES.md:239`, RULE-CEE-001, verbatim: *"Conformidade Constitucional > Eficácia > Efetividade > Eficiência > Economicidade. Eficiência NUNCA pode sobrepor Eficácia. Economicidade NUNCA pode sobrepor Eficácia (Q-009)."*). "Adiantar" aqui = trabalho preparatório de espec-time que NÃO abre Spec e NÃO promove o item — só reduz risco/leitura futura.

> **Itens avaliados (13):** BL-001, BL-002, BL-003, BL-004, BL-009, BL-010, BL-011, BL-012, BL-013, BL-015, BL-016, BL-017, BL-018. (Excluídos os `Absorvido`/`Descartado`: BL-005/006/007/008/014/019/020/021/022/023/024/025.)

---

## 1. Tabela-resumo (ordenada por prioridade de adiantamento)

| # | ID | Título curto | Estado atual `[FATO NORMATIVO]` | Ganho estimado (4Es) | Risco estimado | Recomendação `[PROPOSTA]` |
|---|---|---|---|---|---|---|
| 1 | **BL-009** | Reavaliar SAS-001 sob SES-001 §67 | Em espera | **Alto** — Conformidade (cobertura §59/§60 de canônico); espelha BL-008 já fechado | **Baixo** — auditoria sem reescrita (R1/INV-09) | **ADIANTAR** como auditoria (mapa de conformidade), sem reescrever SAS-001 |
| 2 | **BL-010** | MC-RAG-001 — classificar colisões R-01..R-08 | Em espera | **Médio-alto** — Conformidade + Efetividade (evita adoção silenciosa antes de SPEC-004/006/007) | **Baixo-médio** — classificar ≠ aplicar; respeitar J-001/CC-02/INV-05 | **ADIANTAR só a classificação** (registro no CONFLICT-MAP), sem aplicar tratamentos |
| 3 | **BL-011** | MC-EXP-001 — classificar colisões R-01..R-07/X-04 | Em espera | **Médio** — idem, fronteira com RAG (R-07) | **Baixo-médio** — idem | **ADIANTAR só a classificação** |
| 4 | **BL-012** | MC-COG-001 — classificar colisões (R-05 já resolvida) | Em espera | **Médio** — R-05 (estados §7 vs CHM-001) já classificada como REJEITAR | **Baixo-médio** — não re-especificar N8–N17 | **ADIANTAR só a classificação** residual; R-05 já concluída |
| 5 | **BL-018** | Risk Agent / família RISK-SPEC | Em espera | **Médio-alto** — Conformidade (herança N8–N17 verificável) | **Médio** — decisões RISK-ARR-LOC-001/RISK-CONV-001 abertas; RISK-CONV-001 depende de J-001 | **ADIANTAR só a análise preparatória** (mapa RISK-MASTER × N8–N17); NÃO a ativação plena (ver §3) |
| 6 | **BL-017** | Fechamento das dimensões B da SPEC-020 | **Proposto** | **Baixo** — só rastreabilidade/CONS-01 (fechamento real é upstream) | **Muito baixo** — ato administrativo | Recomendar a Andraus **promover `Proposto`→`Em espera`**; fechamento efetivo aguarda SPEC-007/014/038 |
| 7 | **BL-015** | MC-LRN-001 — classificar colisões | Em espera | **Baixo-médio** — classificação adiantável, aplicação distante (SPEC-018) | **Baixo** | ADIANTAR classificação só se houver folga; baixa urgência |
| 8 | **BL-016** | MC-SKL-001 — classificar colisões | Em espera | **Baixo** — camada Skills distante (FASE 10); R-ARCH diferida a SPEC-025 | **Baixo** | MANTER `Em espera`; classificação adiantável, sem urgência |
| 9 | **BL-001** | VPD nos 5 agentes + SPEC-001 | Em espera | **Baixo** — agentes SPEC-010..014 distantes (FASE 5) | **Baixo** | MANTER `Em espera`; sem ganho relevante agora |
| 10 | **BL-003** | Persistência física de hipótese/estado | Em espera | **Baixo agora** — depende de SPEC-004/006/009 | **Médio se antecipado** — pré-fixaria storage antes do Blackboard | MANTER `Em espera` (bloqueado por SPEC-004) |
| 11 | **BL-002** | Falso-DENY observável (MEN-01) | Em espera | **Baixo agora** — método vive no CCM-001 | **Alto se antecipado** — depende de J-001/SPEC-003 | MANTER `Em espera` (bloqueado por J-001) |
| 12 | **BL-004** | Fórmula/pesos/limiares do Conviction Vector | Em espera | n/a — é o próprio bloqueador J-001 | **Muito alto** — `[DECISÃO NECESSÁRIA: J-001]` + backtest | **NÃO ADIANTAR**; é SPEC-003, trava E3 do gate Convicção→Decisão |
| 13 | **BL-013** | MC-GOV-001 — Camada de Governança | Em espera | — | — | **SEM recomendação de adiantamento** — restrição 1 (ver §4). Manter `Em espera`. |

---

## 2. Justificativa por item (TRACE-06)

**BL-009 (SAS-001 sob SES-001 §67).** `[FATO NORMATIVO]` Estado `Em espera`, ação verbatim: *"Reavaliar SAS-001 pelos campos/derivação SES-001; sem reescrita forçada (R1)"* (`RMR-001:108`). `[INFERÊNCIA]` É o espelho exato do BL-008, que acabou de ser `Absorvido` via Mapa de Auditoria sem reescrever a SPEC-001 (*"SPEC-001 v1.1 não reescrita — INV-09"*, `RMR-001:107`); o mesmo método aplica-se a SAS-001 com risco baixo e alto ganho de Conformidade, de-riscando a 1ª Engineering Card (que chega com SPEC-002). `[PROPOSTA]` Adiantar como auditoria.

**BL-010 / BL-011 / BL-012 (MC-RAG/EXP/COG — classificação).** `[FATO NORMATIVO]` Os três estão `Em espera` com *"tratamentos R-01..R-08 diferidos à ativação"* (`RMR-001:109`) e K-MAN-14/15/16 já registrados. `[INFERÊNCIA]` Classificar as colisões (registrar no CONFLICT-MAP) é ato de Trilha A distinto de aplicá-las na Trilha B; reduz risco de adoção silenciosa de rótulos externos (G-gates, I-xx, estados §7) antes das Specs-alvo. Em BL-012 a colisão mais crítica já está classificada: *"REJEITAR R-05 (usar estados CHM-001, CC-02)"* (`RMR-001:111`). `[PROPOSTA]` Adiantar apenas a classificação; ver §3 (restrição 3).

**BL-018 (Risk Agent).** `[FATO NORMATIVO]` `Em espera`; gatilho composto verbatim: *"`spec:EUA-E19a homologada` ∧ `milestone:FASE 6 (Synthesis) concluída`"* — 1ª condição satisfeita, *"resta `milestone:FASE 6 concluída` para ativação plena"* (`RMR-001:117`). `[INFERÊNCIA]` A análise preparatória (mapear `SOT-RISK-MASTER-001` × N8–N17) não depende de FASE 6 porque N8–N17 já são FATO NORMATIVO; a redação das 23 RISK-SPEC, sim. `[PROPOSTA]` Adiantar só o preparatório (§3).

**BL-017 (dimensões B da SPEC-020).** `[FATO NORMATIVO]` Único item em `Proposto`, *"aguarda promoção a `Em espera` por Andraus"* (`RMR-001:116`). `[INFERÊNCIA]` O fechamento real é upstream (RAG↔SPEC-007, decision traceability↔SPEC-014, tool correctness↔SPEC-038), então o único ato adiantável é a promoção administrativa, que higieniza o CONS-01 sem risco. `[PROPOSTA]` Recomendar a Andraus a promoção; não tratar dimensões B como fechadas (CONS-01).

**BL-015 / BL-016 (MC-LRN / MC-SKL).** `[FATO NORMATIVO]` Ambos `Em espera`, classificação (K-MAN-18/19) feita, tratamentos diferidos à ativação (`RMR-001:114-115`). `[INFERÊNCIA]` Aplicação depende de SPEC-018 (Learning) e SPEC-025 (Skills), ambas distantes; adiantar classificação residual dá ganho marginal. `[PROPOSTA]` Baixa urgência; adiantar só com folga.

**BL-001 (VPD).** `[FATO NORMATIVO]` `Em espera`, gatilho `spec:SPEC-010..014 em redação` (`RMR-001:100`). `[INFERÊNCIA]` Agentes analíticos estão na FASE 5, muito à frente; sem ganho relevante agora. `[PROPOSTA]` Manter.

**BL-003 (persistência física).** `[FATO NORMATIVO]` `Em espera`, gatilho `spec:SPEC-004 em redação` (`RMR-001:102`). `[INFERÊNCIA]` Especificar storage antes do Blackboard/KG (SPEC-004/006/009) inverteria a dependência do caminho crítico. `[PROPOSTA]` Manter `Em espera`.

**BL-002 (falso-DENY).** `[FATO NORMATIVO]` `Em espera`, gatilho `spec:SPEC-003 homologada ∨ decisao:J-001 resolvida` (`RMR-001:101`). `[INFERÊNCIA]` O método de observação vive no CCM-001, que só é redigido na SPEC-003; antecipar depende de J-001 (`[DECISÃO NECESSÁRIA]`). `[PROPOSTA]` Manter.

**BL-004 (fórmula do Conviction Vector).** `[FATO NORMATIVO]` `Em espera`; é o próprio conteúdo de J-001/CCM-001/SPEC-003 (`RMR-001:103`; `ROADMAP:30` — *"J-001 … trava E3 do gate Convicção→Decisão em SPEC-003"*). `[INFERÊNCIA]` Adiantar fecharia J-001 sem backtest — proibido. `[PROPOSTA]` NÃO adiantar.

**BL-013 (MC-GOV).** Ver §4 — sem recomendação de adiantamento (restrição 1).

---

## 3. Restrições 2 e 3 — separação de fases

### 3.1 BL-018 — "análise preparatória" (adiantável) vs "ativação plena" (não adiantável)

`[FATO NORMATIVO]` O gatilho é composto e só a 1ª condição disparou (`RMR-001:117`, verbatim citado em §2). A "Ação ao ativar" mistura dois blocos: *"Admitir SOT-RISK-MASTER-001 como ref. externa"* e *"redigir família 23 RISK-SPEC (Grupos A–H; herança N8–N17 via RULE-HV; …)"* (`RMR-001:117`).

`[INFERÊNCIA]` Separação proposta:
- **ADIANTÁVEL (preparatório, sem FASE 6):** mapear cada obrigação do `SOT-RISK-MASTER-001` contra as disciplinas N8–N17. Isto é lícito porque N8–N17 já são FATO NORMATIVO (EUA-E04..E14, herdadas via RULE-HV — `governance/RULES.md:401`), e o documento-fonte já é candidato a ref. externa `[PROPOSTA]` (`SOT-RISK-MASTER-001:9` — *"`[PROPOSTA]` — não-normativo até homologação via EUA-E19 + Família RISK-SPEC"*). O mapa N8–N17 é classificação/gap-analysis, não redação de spec, e não depende do Synthesis Agent (SPEC-014/FASE 6).
- **NÃO ADIANTÁVEL (ativação plena):** redigir as 23 RISK-SPEC, admitir formalmente a ref. externa (Etapas 1–5), ou fixar "convicção de risco". Estas exigem `milestone:FASE 6 concluída` e/ou colidem com decisões abertas.

`[INFERÊNCIA] Achado de risco:` mesmo o preparatório deve marcar `[DECISÃO NECESSÁRIA]` para **RISK-ARR-LOC-001** (D-ARR-001 ausente do repo — *"não há linguagem de supersedação do ARR"*, `SOT-RISK-MASTER-001:28`) e **RISK-CONV-001**, que *"fecha em RISK-SPEC-010, não antes de J-001"* (`ROADMAP:31`). Ou seja, o mapa preparatório pode listar a "convicção de risco" como ponto de contato, mas não pode resolvê-la (bloqueada por J-001).

### 3.2 BL-010/011/012 — "classificação de colisões" (adiantável) vs "aplicação" (não adiantável)

`[FATO NORMATIVO]` Nos três itens, a admissão como referência externa e o registro K-MAN-14/15/16 já ocorreram; o que resta é *"tratamentos R-01..R-08 diferidos à ativação"* (`RMR-001:109-111`).

`[INFERÊNCIA]` "Classificar" (rotular cada colisão como adotar/adaptar/rejeitar/adiar e registrá-la no CONFLICT-MAP) é ato de Trilha A que não implementa nada na Trilha B. É adiantável e de baixo risco, com ganho de Conformidade (nada é adotado em silêncio) e de Efetividade (SPEC-004/006/007 chegam com as fronteiras já mapeadas). "Aplicar" (usar os schemas §6/§18/§19, reconciliar as filas RAG/EXP/COG-SPEC) é redação de requisito nas Specs-alvo — não adiantável. Salvaguarda: a classificação NÃO pode fechar J-001/CC-02/INV-05/INV-09 (fronteiras já anotadas nos próprios itens). Em BL-012, R-05 já vem classificada como REJEITAR (`RMR-001:111`) — evidência de que o padrão "classificar sem aplicar" já é praticado.

---

## 4. Restrição 1 — BL-013 NÃO recebe recomendação de adiantamento

`[FATO NORMATIVO]` Por decisão expressa de Andraus no gate DHR-SPEC019-001, o BL-013 permanece `Em espera`, re-diferido. Verbatim (`RMR-001:112`): *"Gatilho `spec:SPEC-019`/`decisao:L-001` disparou no gate DHR-SPEC019-001 (2026-09-22): Andraus decidiu que governança de runtime NÃO é resíduo de L-001 nem foi absorvida pela SPEC-019 (escopo spec-time) → BL-013 permanece Em espera, re-diferido; ativa apenas em SPEC-018/K-001."*

`[PROPOSTA]` Este documento registra apenas a **manutenção de `Em espera`** para BL-013 e **não recomenda** qualquer adiantamento, em conformidade com a restrição 1 do mandato e com o gate citado. Sua ativação pertence a SPEC-018/K-001.

---

## 5. Notas de conformidade

- Este documento é `[PROPOSTA]`/análise: **não abre Spec, não promove item, não edita o RMR-001** (que é BASELINE homologado — INV-09; edição exigiria o trio Especificador→Revisor→Andraus). Optou-se por **não** inserir nota no painel, para não tocar baseline sem homologação; a inserção de um ponteiro é faculdade de Andraus.
- Nenhuma decisão aberta foi fechada (CONS-01): J-001, RISK-ARR-LOC-001, RISK-CONV-001, ECC-VAL-001, ECC-03-001, K-001, G/H/I/M/N-001 permanecem abertas.
- Capturas verbatim (RULE-ECC-04) usadas para toda alegação carregada, com `arquivo:linha`.
