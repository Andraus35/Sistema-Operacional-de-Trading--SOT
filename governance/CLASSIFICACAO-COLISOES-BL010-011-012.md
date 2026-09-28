# CLASSIFICAÇÃO DE COLISÕES — BL-010 / BL-011 / BL-012 (Master Contracts diferidos)

| Campo | Valor |
|---|---|
| Documento | CLASSIFICACAO-COLISOES-BL010-011-012 |
| Tipo | Classificação / Proposta (NÃO-normativa; NÃO abre Spec; NÃO promove item; NÃO aplica tratamento) |
| Autor | Especificador SOT |
| Data | 2026-09-28 |
| Escopo | Registro formal da **classificação** (adotar/adaptar/rejeitar/adiar) das colisões dos 3 Master Contracts já admitidos como referência externa: **BL-010** (MC-RAG-001), **BL-011** (MC-EXP-001), **BL-012** (MC-COG-001) |
| Autoridade | **HOMOLOGADO** (Andraus, 2026-09-28, DHR-BL010-011-012-001). As 13 entradas foram inseridas em `governance/CONFLICT-MAP.md`. |
| Fonte de mandato | `backlog/ANALISE-PRIORIZACAO-BACKLOG-2026-09-28.md` §3.2 (itens 2-4, recomendação "ADIANTAR só a classificação") |

> **Status epistemológico (TRACE-06).** O estado de cada item e as colisões já registradas nos comentários `K-MAN-14/15/16` do `CONFLICT-MAP.md` e nas células do `RMR-001` são `[FATO NORMATIVO]`/`[FONTE]`. A consolidação em entradas estruturadas de colisão é `[INFERÊNCIA]` fiel a essas fontes. Nada aqui fecha decisão aberta (CONS-01), redefine canônico (CC-02), toca J-001, ou viola INV-05/INV-09.

> **Delimitação — classificar ≠ aplicar.** Este documento apenas **classifica** as colisões (lado que prevalece + justificativa) e as registra. A **aplicação** dos tratamentos (uso dos schemas §6/§18/§19, reconciliação das filas RAG/EXP/COG-SPEC, mapeamento de estados) fica para a **ativação** de cada item — abertura de SPEC-004/006/007 (RAG/EXP) e a consolidação cognitiva (COG) — conforme os gatilhos vigentes no RMR-001. As colisões já constavam do `CONFLICT-MAP.md` como comentários de emenda (`K-MAN-14/15/16`); aqui elas ganham forma tabular auditável, sem novo conteúdo normativo.

> **Salvaguardas invioláveis nesta classificação (AGENTS.md §6).** Nenhuma colisão abaixo (a) fecha **J-001** — `confidence`/calibração/pesos permanecem diferidos ao CCM-001/Conviction Engine; (b) redefine **CEM-001/CHM-001** (**CC-02**) — os pacotes externos PROJETAM os canônicos, não os substituem; (c) toca **INV-05** (decisão≠execução) — nenhuma camada de memória/recuperação/cognição recebe autoridade decisional ou de execução; (d) viola **INV-09** (feedback/status externo ≠ autoridade/baseline).

---

## Convenção de rótulos

Os rótulos `R-xx`/`X-xx` são os **identificadores analíticos** usados nas células do `RMR-001` (BL-010/011/012) e nos comentários `K-MAN-14/15/16` do `CONFLICT-MAP.md`. Eles **não** são um catálogo canônico numerado 1:1 (não existem como lista fechada nos Master Contracts de origem); a correspondência `R-nº → colisão` abaixo é `[INFERÊNCIA]` a partir do texto das células e das emendas, e a classificação é feita **pelo conteúdo da colisão**, não pelo número. Onde o RMR-001 já nomeia explicitamente (ex.: BL-012 "R-05 estados §7 → CHM-001"), o número é `[FONTE]`.

`Decisão de colisão`: **REJEITAR** (não adotar o rótulo/estrutura externa) · **ADAPTAR** (admitir como elemento LOCAL da camada, ancorado no canônico) · **ADIAR** (reconciliar na ativação da Spec-alvo) · **CONFORME** (sem colisão — fronteira já respeitada).

---

## 1. BL-010 — MC-RAG-001 (Camada RAG) · K-MAN-14

Fonte: `reference/camadas/MC-RAG-001_Master_Contract_Camada_RAG.md`; célula `RMR-001` BL-010; comentário `CONFLICT-MAP.md` K-MAN-14. Estado do item: **Em espera** (inalterado).

| ID colisão | Rótulo RMR | Elemento externo (âncora) | Colide com (SOT canônico) | Lado que prevalece | Decisão | Justificativa curta |
|---|---|---|---|---|---|---|
| COL-RAG-01 | R-01 | Quality Gates **G0–G8** (§13, l.673+) | Quality Gates **L1–L4** (atomic-spec §7) / harness-score **L0–L4** | **SOT canônico** | REJEITAR namespace G como gate global; ADAPTAR como gates **LOCAIS** da camada RAG | Colisão de namespace de maturidade/gate; mesmo padrão K-MAN-01/02. |
| COL-RAG-02 | (ordem 4Es) | Ordem **§1**: Eficácia→**Eficiência**→**Efetividade**→Economicidade (l.18-19 lista só Eficácia/Eficiência) | Ordem canônica **CEE-001 §12**: Eficácia→Efetividade→Eficiência→Economicidade (AGENTS §6.11) | **SOT canônico** | REJEITAR ordem externa | Inversão de Eficiência/Efetividade; não-negociável AGENTS §6.11; mesmo caso K-MAN-07 (MIQG). |
| COL-RAG-03 | R (I-RAG/RAG-P) | Namespaces **I-RAG-01..10** (§12, l.659+) e **RAG-P01..P14** (§3, l.70+) | INV-01..10 / PC-xx / PB-xx / PCO globais | **SOT canônico** | ADAPTAR como invariantes/princípios **LOCAIS** que **referenciam** os canônicos (não novos globais) | Ex.: I-RAG-01 (proveniência)=RULE-EPI/TRACE-06; I-RAG-05 (incerteza)=RULE-UNC-03. |
| COL-RAG-04 | (RAG-SPEC-018) | RAG-SPEC-018 — Evidence Independence | RULE-004 + RULE-MET-01 | — (sem colisão) | **CONFORME** | Ancora nos canônicos, não redefine; confirmar na ativação. |
| — (fronteira) | — | `confidence` do RAG | Conviction Vector 8D / **J-001** (INV-03 aberto) | **SOT** | CONFORME — **J-001 permanece aberto** | `confidence` de recuperação ≠ convicção; não fecha J-001. |
| — (fronteira) | — | Evidence Packet / Knowledge Candidate | **CEM-001 / CHM-001** (CC-02) | **SOT** | CONFORME — **CC-02 preservado** | Projetam os canônicos, não os redefinem. |
| — (fronteira) | — | RAG §2.2/§23 (recuperação) · RAG-P13 (feedback) | **INV-05** (não decide/executa) · **INV-09** | **SOT** | CONFORME — **INV-05/INV-09 preservados** | RAG não decide nem executa; feedback ≠ autorização. |

**Resultado BL-010:** 3 colisões efetivas (COL-RAG-01/02/03) — todas com prevalência do **SOT canônico** (2 REJEITAR namespace/ordem + 1 ADAPTAR como local); 1 referência CONFORME (COL-RAG-04); 3 fronteiras confirmadas CONFORMES (J-001/CC-02/INV-05/INV-09). Tratamentos residuais (`R-04..R-08` da célula) = **aplicação** (reconciliar RAG-SPEC-001..046, usar schemas) → **ADIADOS** à abertura da SPEC-007. Nada inconclusivo.

---

## 2. BL-011 — MC-EXP-001 (Camada de Experiência e Memória) · K-MAN-15

Fonte: `reference/camadas/CAMADA MEMÓRIA.MD`; célula `RMR-001` BL-011; comentário `CONFLICT-MAP.md` K-MAN-15. Estado do item: **Em espera** (inalterado).

| ID colisão | Rótulo RMR | Elemento externo (âncora) | Colide com (SOT canônico) | Lado que prevalece | Decisão | Justificativa curta |
|---|---|---|---|---|---|---|
| COL-EXP-01 | X-01 | Status "**BASELINE**" (l.7) + "**BASELINE PROPOSTA**" (l.1518) | INV-09 / PC-08 (status externo ≠ baseline) | **SOT canônico** | REJEITAR efeito normativo; normalizar como **PROPOSTA / ref. externa** | Inconsistência interna do doc; sem efeito de baseline (INV-09). |
| COL-EXP-02 | R-01 | Quality Gates **G0–G8** (§52, l.1191+) | Quality Gates **L1–L4** / harness-score **L0–L4** | **SOT canônico** | REJEITAR namespace G global; ADAPTAR como gates **LOCAIS** | Padrão K-MAN-14. |
| COL-EXP-03 | R-02/R-03 | **I-EXP-01..12** (§51, l.1142+) e **EXP-P01..P14** (§5, l.112+) | INV/PC/PB globais | **SOT canônico** | ADAPTAR como LOCAIS ancorados nos canônicos | I-EXP-01/07 (imutabilidade)=RULE-BB-004/INV-07; I-EXP-08=RULE-004/RULE-MET-01; I-EXP-09=INV-05; EXP-P03=RULE-EPI; EXP-P04=RULE-CAU-03. |
| COL-EXP-04 | X-04 | **Working Memory §7.6** (l.257+) | Blackboard / **SPEC-004** (memória de trabalho) | **SOT canônico** | ADIAR / RELOCAR a SPEC-004 | Working Memory ≠ memória histórica permanente (esta camada); pertence ao Blackboard. |
| COL-EXP-05 | R-07 | **EXP-SPEC-021** (Experience Independence) | **RAG-SPEC-018** (Evidence Independence, BL-010) — ambos ancoram RULE-004 | — (duplicação, não conflito) | ADIAR reconciliação à ativação (SPEC-006/009) | Duplicação inter-camada; reconciliar sem redefinir RULE-004. |
| — (fronteira) | — | Experience Record / Packet | **CEM-001 / CHM-001** (CC-02) | **SOT** | CONFORME — **CC-02 preservado** | Projetam os canônicos. |
| — (fronteira) | — | `confidence` / `performance_metrics` | Conviction Vector 8D / **J-001** (INV-03 aberto) | **SOT** | CONFORME — **J-001 aberto** | Métricas históricas ≠ Conviction Vector. |
| — (fronteira) | — | I-EXP-09 (memória sem autoridade decisional) | **INV-05** · imutabilidade = **INV-07/RULE-BB-004** | **SOT** | CONFORME — **INV-05 preservado; INV-07 reforçado** | Memória não decide; imutabilidade histórica REFORÇADA. |

**Resultado BL-011:** 5 colisões efetivas (COL-EXP-01..05) — prevalência **SOT canônico** em todas (1 REJEITAR status + 1 REJEITAR/ADAPTAR namespace G + 1 ADAPTAR I/P locais + 1 ADIAR Working Memory→SPEC-004 + 1 ADIAR reconciliação dup. com RAG); 3 fronteiras confirmadas CONFORMES. Tratamentos residuais (`R-04..R-06` de aplicação) → **ADIADOS** à ativação (SPEC-006/009). Nada inconclusivo.

---

## 3. BL-012 — MC-COG-001 (Camada de Cognição) · K-MAN-16

Fonte: `reference/camadas/MC-COG-001_Master_Contract_Camada_Cognicao.md`; célula `RMR-001` BL-012; comentário `CONFLICT-MAP.md` K-MAN-16. Estado do item: **Em espera** (inalterado). ~80% do conteúdo já é FATO NORMATIVO (N8–N17).

| ID colisão | Rótulo RMR | Elemento externo (âncora) | Colide com (SOT canônico) | Lado que prevalece | Decisão | Justificativa curta |
|---|---|---|---|---|---|---|
| COL-COG-01 | **R-05** `[FONTE]` | Estados cognitivos **§7** (l.201-229): CREATED→ANALYZED→PARTIALLY_VALIDATED→MONITORED→STRENGTHENED→PRINCIPAL / REFUTED / INCONCLUSIVE | **CHM-001 / RULE-BB-003**: EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→ARCHIVED (risco de **CC-02**) | **CHM-001 (canônico)** | **REJEITAR** os estados §7; COG-SPEC-004 **mapeia para CHM-001**, não cria lifecycle paralelo | Achado central; já classificada como REJEITAR (RMR-001 BL-012). **CC-02 protegido.** |
| COL-COG-02 | R-01 | Quality Gates **G0–G9** (§22, l.626+) | Quality Gates **L1–L4** / harness-score **L0–L4** | **SOT canônico** | REJEITAR namespace G global; ADAPTAR como gates **LOCAIS** | Padrão K-MAN-14. |
| COL-COG-03 | R-02/R-03 | **I-COG-01..12** (§21, l.587+) e **COG-P01..P15** (§4, l.86+) | N8–N17 / INV / PC / PB globais | **SOT canônico** | ADAPTAR como LOCAIS que referenciam N8–N17 | I-COG-01=RULE-EPI/TRACE-06; I-COG-06=RULE-CAU-01; I-COG-11=RULE-MET-01/INV-09. |
| COL-COG-04 | R-06 | §15/§16 calibração/bayes/risco (COG-SPEC-035..039/043) | CCM-001 / Conviction Engine (**J-001 aberto**) | **SOT** | **ADIAR** ao CCM-001; não define | Não fecha nem calibra o Conviction Vector 8D. **J-001 aberto.** |
| COL-COG-05 | X-01 | Status "**Baseline**" (l.6) | INV-09 (status externo sem efeito) | **SOT canônico** | REJEITAR efeito; normalizar como **ref. externa** | Sem efeito normativo (INV-09). |
| — (fronteira) | — | probabilístico/`confidence` genéricos | Conviction Vector 8D / **J-001** | **SOT** | CONFORME — **J-001 aberto** | Genéricos ≠ Conviction 8D. |
| — (fronteira) | — | COG-SPEC-040 (análise) | **INV-05** (análise ≠ autoridade decisional) · I-COG-11=RULE-MET-01/**INV-09** | **SOT** | CONFORME — **INV-05 preservado** | Cognição analisa, não decide/executa; feedback ≠ fabricação. |

**Resultado BL-012:** 5 colisões efetivas (COL-COG-01..05) — prevalência **CHM-001/SOT canônico** em todas. A colisão central (COL-COG-01 / R-05) **já estava classificada como REJEITAR** (usar estados CHM-001) e é aqui **confirmada** — é o achado de maior risco (CC-02) e o único com conflito de conteúdo (não só de namespace). Demais: 2 REJEITAR namespace/status + 1 ADAPTAR locais + 1 ADIAR calibração→CCM-001. 2 fronteiras CONFORMES. Tratamentos de **mapeamento** (aproveitar §6/§18/§19 como schemas) → **ADIADOS** à consolidação cognitiva. Nada inconclusivo.

---

## 4. Entradas aditivas PROPOSTAS ao `governance/CONFLICT-MAP.md`

> **NÃO aplicar** — texto exato para o **Controlador inserir após homologação de Andraus** (mesmo padrão RULES.md/atomic-spec.md). Preservar INV-07 (aditivo, nada removido). As colisões já constam como comentários `K-MAN-14/15/16`; esta seção apenas as consolida em forma tabular auditável. Inserir como **nova seção** ao final do `CONFLICT-MAP.md`, antes de "## O que é impossível por definição" ou como seção própria.

```markdown
## Colisões classificadas — Master Contracts diferidos (BL-010/011/012)

<!-- Emenda AAAA-MM-DD (DHR-<id>): consolidação tabular das colisões já registradas em
     K-MAN-14 (MC-RAG-001/BL-010), K-MAN-15 (MC-EXP-001/BL-011), K-MAN-16 (MC-COG-001/BL-012).
     Classificar ≠ aplicar: tratamentos de aplicação permanecem diferidos à ativação
     (SPEC-004/006/007 e consolidação cognitiva). Nenhuma colisão fecha J-001, redefine
     CEM-001/CHM-001 (CC-02) ou toca INV-05/INV-09. Fonte: governance/CLASSIFICACAO-COLISOES-BL010-011-012.md -->

| Item | ID | Elemento externo | Colide com (SOT) | Prevalece | Decisão | K-MAN |
|---|---|---|---|---|---|---|
| BL-010 | COL-RAG-01 | Quality Gates G0–G8 (§13) | L1–L4 / L0–L4 | SOT | REJEITAR global → gate LOCAL | K-MAN-14 |
| BL-010 | COL-RAG-02 | Ordem 4Es §1 (Efic.→Eficiência→Efetividade) | CEE-001 §12 | SOT | REJEITAR ordem externa | K-MAN-14 |
| BL-010 | COL-RAG-03 | I-RAG-01..10 (§12) / RAG-P01..P14 (§3) | INV/PC/PB | SOT | ADAPTAR como LOCAIS | K-MAN-14 |
| BL-010 | COL-RAG-04 | RAG-SPEC-018 (Evidence Independence) | RULE-004/RULE-MET-01 | SOT | CONFORME (não redefine) | K-MAN-14 |
| BL-011 | COL-EXP-01 | Status "BASELINE"/"BASELINE PROPOSTA" | INV-09/PC-08 | SOT | REJEITAR efeito → PROPOSTA | K-MAN-15 |
| BL-011 | COL-EXP-02 | Quality Gates G0–G8 (§52) | L1–L4 / L0–L4 | SOT | REJEITAR global → gate LOCAL | K-MAN-15 |
| BL-011 | COL-EXP-03 | I-EXP-01..12 (§51) / EXP-P01..P14 (§5) | INV/PC/PB | SOT | ADAPTAR como LOCAIS | K-MAN-15 |
| BL-011 | COL-EXP-04 | Working Memory §7.6 | Blackboard/SPEC-004 | SOT | ADIAR/RELOCAR a SPEC-004 | K-MAN-15 |
| BL-011 | COL-EXP-05 | EXP-SPEC-021 ↔ RAG-SPEC-018 (dup.) | RULE-004 | SOT | ADIAR reconciliação (SPEC-006/009) | K-MAN-15 |
| BL-012 | COL-COG-01 | Estados cognitivos §7 | CHM-001/RULE-BB-003 (CC-02) | CHM-001 | REJEITAR §7 → mapear p/ CHM-001 | K-MAN-16 |
| BL-012 | COL-COG-02 | Quality Gates G0–G9 (§22) | L1–L4 / L0–L4 | SOT | REJEITAR global → gate LOCAL | K-MAN-16 |
| BL-012 | COL-COG-03 | I-COG-01..12 (§21) / COG-P01..P15 (§4) | N8–N17/INV/PC/PB | SOT | ADAPTAR como LOCAIS | K-MAN-16 |
| BL-012 | COL-COG-04 | Calibração/bayes/risco §15/§16 | CCM-001 (J-001 aberto) | SOT | ADIAR ao CCM-001 (não define) | K-MAN-16 |
| BL-012 | COL-COG-05 | Status "Baseline" (l.6) | INV-09 | SOT | REJEITAR efeito → ref. externa | K-MAN-16 |

Fronteiras confirmadas CONFORMES (todos os itens): J-001 permanece aberto (confidence/calibração ≠ Conviction Vector 8D);
CC-02 preservado (pacotes externos PROJETAM CEM-001/CHM-001); INV-05 preservado (nenhuma camada decide/executa);
INV-09 preservado (feedback/status externo ≠ autoridade/baseline).
```

---

## 5. Notas de conformidade

- Este documento é `[PROPOSTA]`/classificação: **não abre Spec, não promove item, não aplica tratamento**. A inserção no `CONFLICT-MAP.md` é ato do Controlador **após homologação de Andraus**.
- **CONS-01:** nenhuma decisão aberta foi fechada — **J-001**, K-001, G/H/I/M/N-001, ECC-VAL-001, ECC-03-001 permanecem abertas.
- **CC-02:** nenhum canônico (CEM-001/CHM-001) redefinido; COL-COG-01 (estados §7) **protege** CHM-001 ao rejeitar o lifecycle paralelo.
- **INV-05/INV-09:** preservados em todas as classificações.
- **INV-07:** proposta é aditiva; nenhuma célula/entrada existente é removida.
- Os três itens permanecem **Em espera** — a classificação não altera estado.
