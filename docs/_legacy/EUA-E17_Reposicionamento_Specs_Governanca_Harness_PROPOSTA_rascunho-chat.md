# EUA-E17 — Reposicionamento das Specs de Governança do Harness no ROADMAP (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E17** (emenda ao `ROADMAP.md`) |
| Natureza | Emenda de reposicionamento sequencial — altera posição de SPEC-019, SPEC-020, SPEC-021 no ROADMAP; não altera seu escopo nem seus baselines |
| Status epistemológico | **PROPOSTA — não homologada.** Autoridade literal permanece: `ROADMAP.md` baseline (2026-09-12) + `atomic-spec.md` v1.4. Este arquivo não altera nenhum baseline; existe para auditoria do Revisor e decisão de Andraus. |
| Autoria | Especificador (chat — Andraus/Claude Sonnet 4.6, 2026-09-21) |
| Data | 2026-09-21 |
| Alvo | `ROADMAP.md` — sequência de fases; renumeração de Fases 8/9 e criação de Fase GOV (interposição) |
| Fundamento no baseline | **SDD-001** (Spec-Driven Development — todo artefato com dependência precede os que dele dependem); **PPQ-001 dial GES** (rigor proporcional ao impacto — impacto de governança é transversal); **CONS-01** (decisões abertas não podem ser tratadas como fechadas — L-001 aberta); **CEE-001 §12 4Es** (Eficácia precede Eficiência — governança é Eficácia); **PAP-001 §6** (gate do Revisor por classe de princípio — pressupõe que governança existe antes de ser aplicada) |
| Princípio-guia | **Uma spec que governa a produção de outras specs deve preceder essas specs, não sucedê-las.** Governança posterior a fatos é auditoria de Harness Debt, não prevenção. |

---

## 1. Justificativa — o problema de ordenação atual `[INFERÊNCIA]`

### 1.1 A dependência invertida

O ROADMAP baseline posiciona:

```
SPEC-001..018  →  produção das specs de domínio cognitivo
SPEC-019       →  FASE 8: Harness Governance & Evolution   (governa quem cria RULE, quem aprova, rollback, versionamento)
SPEC-020       →  FASE 9: Harness Evaluation Specification  (define como as specs serão avaliadas)
SPEC-021       →  FASE 9: Harness Score / Maturity Model    (torna harness-score normativo por spec)
```

Isso cria três dependências invertidas documentadas:

**Dependência 1 — SPEC-019 após SPEC-018:**
O escopo homologado da SPEC-019 inclui: *"quem pode alterar Specs; quem cria RULE; quem aprova; versionamento; emendas; Constitution Check; impacto em schemas/RAG/Skills/testes; compatibilidade; rollback; exceções; auditoria"* (`ROADMAP.md §11`). Isso é **governança do processo de especificação**, não governança de runtime cognitivo. Sem SPEC-019, cada emenda futura às SPEC-002..018 opera sem base formal — o processo atual (Especificador→Revisor→Andraus) existe, mas não está especificado como Spec de domínio; existe como método (`atomic-spec.md`). A decisão aberta **L-001** (`auditoria-saude-harness.md §5`) depende de SPEC-019 e está ativa desde o baseline F.1.

**Dependência 2 — SPEC-020 após SPEC-019:**
A SPEC-020 define as dimensões de avaliação do harness (correctness, grounding, RAG faithfulness, hallucination, role adherence, hypothesis consistency, decision traceability…). Enquanto SPEC-020 não existir, nenhuma das SPEC-001..019 foi avaliada contra critérios constitutivos — apenas contra o método atômico e o gate determinístico. O `harness-eval` e o `harness-score` existentes são proxies (F.3/F.4) usados postumamente, não critérios que as specs deveriam satisfazer durante sua produção. A auditoria `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §8/Q13` documenta isso como `[FATO ESTRUTURAL]`: *"Não foi encontrada evidência documental de uso constitutivo de harness-eval/harness-score durante a especificação."*

**Dependência 3 — ausência de Harness Inheritance Contract:**
A emenda EUA-E04 (CC-08, Herança/Delta) está homologada com vigência imediata para SPEC-002+. Mas o **contrato de herança vertical macro→micro** — quais requisitos um harness pai impõe a um harness filho, como se verifica conformidade entre níveis — não existe como Spec normativa. GEH-001 é conceitual. SPEC-019 é o locus natural para normativizá-lo (junto com rollback, impacto em schemas, versionamento de specs). Enquanto SPEC-019 não existir, SPEC-002..018 são especificadas sem esse contrato — a herança é declarada em cada spec individualmente (via CC-08), mas sem regra de conservação verificável entre níveis.

### 1.2 O custo de retroativação acumula por spec

Cada spec produzida sem governança formal vira Harness Debt no CIC-001 pelo regime D-DHR-PAP-001-01. O regime existe e é correto. Mas a escolha deliberada de produzir 18 specs antes de normatizar a governança que as governa não foi uma decisão consciente registrada — foi uma consequência do ordenamento por domínio de conteúdo. Esta proposta torna esse trade-off explícito para decisão de Andraus.

### 1.3 O que já está resolvido parcialmente

A emenda **EUA-E04** (CC-08, Herança/Delta, homologada 2026-09-20) já introduz a declaração de herança como requisito de spec-time para SPEC-002+. Isso é o passo mais importante e já está vigente. O que falta é a **regra de conservação entre níveis** e os **critérios de avaliação constitutivos** — que são o objeto da SPEC-019 e SPEC-020 respectivamente.

---

## 2. Mapa de rastreabilidade — dependências formais por spec `[INFERÊNCIA]`

A tabela abaixo usa as fontes documentadas (`ROADMAP.md`, `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md`, `auditoria-saude-harness.md §5`, atas DHR, decisões abertas ativas).

| Spec | Depende de (governança) | Consequência se SPEC-019/020 vierem depois |
|---|---|---|
| SPEC-002 | CC-08 (EUA-E04, vigente) · atomic-spec v1.5 (piloto em SPEC-001) | Herança declarada; sem regra de conservação vertical (SPEC-019) |
| SPEC-003 | J-001 (bloqueador), CCM-001 | Sem critérios de avaliação constitutivos (SPEC-020) |
| SPEC-004..009 | Blackboard/Event Bus/KG/RAG/Scheduler/State | Cada spec declara herança via CC-08, mas sem contrato de conservação; avaliação posterior |
| SPEC-010..013 | Agentes analíticos — alto risco de Harness Debt acumulado | 8–9 specs CRITICAL/HIGH sem critérios de avaliação constitutivos |
| SPEC-014..016 | Synthesis · Mission · TMP — fronteira SOT→downstream | Sem SPEC-019, rollback/impacto em schemas não especificado formalmente |
| SPEC-017..018 | Pattern Memory · Learning — K-001 aberta | Sem maturidade normativa por spec (SPEC-021) |
| SPEC-019 | **L-001 (decisão aberta ativa)** | Hoje é Fase 8; produz 18 specs antes de normatizar governança |
| SPEC-020 | SPEC-019 | Critérios de avaliação só definidos depois de todas as specs de domínio |
| SPEC-021 | SPEC-020 | Maturidade por spec só normativa depois das specs de domínio |

**Evidências documentadas das dependências:**
- L-001 aberta gateia SPEC-019 → `auditoria-saude-harness.md §5`: *"L-001 (SPEC-019)"* listada entre decisões abertas que gateiam specs futuras.
- Harness Inheritance Contract ausente → `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §12 Q14`: *"Não. [...] nenhum contrato de herança vertical pai→filho entre harnesses."* `[FATO ESTRUTURAL]`
- harness-eval/score não-constitutivos → `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §8/Q13`: `[FATO ESTRUTURAL]`
- SPEC-020/021 apenas planejadas → `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §20`: *"O que ainda não existe (a construir no replanejamento)"* `[FATO DOCUMENTADO]`

---

## 3. Proposta de reposicionamento `[PROPOSTA]`

### 3.1 Princípio de reposicionamento

**Uma spec de governança cujo escopo incide sobre specs de domínio deve preceder essas specs no ROADMAP, salvo quando sua redação depende de conteúdo que só as specs de domínio produzem.**

Aplicando esse princípio:

- **SPEC-019** (Harness Governance & Evolution) — escopo inteiramente de processo/governança de especificação; não depende de conteúdo de domínio cognitivo para ser redigida. **Deve preceder SPEC-002.**
- **SPEC-020** (Harness Evaluation Specification) — define como specs serão avaliadas; as dimensões (correctness, grounding, role adherence…) são independentes do conteúdo de cada spec. **Deve preceder SPEC-002, ou no máximo SPEC-003.**
- **SPEC-021** (Harness Score / Maturity Model) — define maturidade por spec; pode vir logo após SPEC-020, ainda antes das specs de agentes analíticos (SPEC-010+), onde maturidade começa a ter relevância diferenciada.

### 3.2 Sequência proposta

```
SEQUÊNCIA ATUAL (baseline)             SEQUÊNCIA PROPOSTA (esta emenda)
─────────────────────────              ──────────────────────────────────
FASE 0   M0 (HOMOLOGADO)               FASE 0   M0 (HOMOLOGADO) — inalterado
FASE 1   SPEC-001 (HOMOLOGADO)         FASE 1   SPEC-001 (HOMOLOGADO) — inalterado
FASE 1   SPEC-002 Evidence             FASE GOV SPEC-019 Harness Governance ← ANTECIPADO
FASE 1   SPEC-003 Conviction           FASE GOV SPEC-020 Harness Evaluation  ← ANTECIPADO
FASE 2   SPEC-004 Blackboard           FASE GOV SPEC-021 Harness Score        ← ANTECIPADO
FASE 2   SPEC-005 Event Bus            FASE 1   SPEC-002 Evidence
FASE 3   SPEC-006 Knowledge Graph      FASE 1   SPEC-003 Conviction
FASE 3   SPEC-007 RAG                  FASE 2   SPEC-004 Blackboard
FASE 4   SPEC-008 Scheduler            FASE 2   SPEC-005 Event Bus
FASE 4   SPEC-009 Cognitive State      FASE 3   SPEC-006 Knowledge Graph
FASE 5   SPEC-010..013 Agentes         FASE 3   SPEC-007 RAG
FASE 6   SPEC-014..016 Synthesis/Mis.  FASE 4   SPEC-008 Scheduler
FASE 7   SPEC-017..018 Memory/Learn.   FASE 4   SPEC-009 Cognitive State
FASE 8   SPEC-019 Harness Gov.         FASE 5   SPEC-010..013 Agentes
FASE 9   SPEC-020 Harness Eval.        FASE 6   SPEC-014..016 Synthesis/Mis.
FASE 9   SPEC-021 Harness Score        FASE 7   SPEC-017..018 Memory/Learn.
FASE 10  SPEC-022 Cognitive Test       FASE 8   SPEC-022 Cognitive Test   ← renumerado
FASE 11  SPEC-023..024 Orq./Meta       FASE 9   SPEC-023..024 Orq./Meta   ← renumerado
FASE 12+ SPEC-025..045                 FASE 10+ SPEC-025..045             ← renumerado
```

### 3.3 Conteúdo da FASE GOV (nova fase interposicionada)

```
FASE GOV — GOVERNANÇA DO HARNESS DE ESPECIFICAÇÃO
(interposicionada entre SPEC-001 HOMOLOGADA e SPEC-002)

SPEC-019 — Harness Governance & Evolution
  Prioridade: P0 — HIGH · Profundidade-alvo: D0–D8
  Escopo (preservado do baseline):
    Quem pode alterar Specs; quem cria RULE; quem aprova; versionamento;
    emendas; Constitution Check; impacto em schemas/RAG/Skills/testes;
    compatibilidade; rollback; exceções; auditoria.
  Acréscimo de escopo por esta emenda (Q1 — decisão de Andraus):
    Contrato de herança vertical macro→micro (Harness Inheritance Contract)
    — normativiza GEH-001 §6 como spec formal; define regra de conservação
    de requisitos entre harnesses pai e filho; define verificação de
    conformidade inter-nível.
  Resolve: L-001 (decisão aberta ativa desde baseline F.1).

SPEC-020 — Harness Evaluation Specification
  Prioridade: P0 — CRITICAL · Profundidade-alvo: D0–D8
  Escopo (preservado do baseline):
    Define como o SOT Harness será avaliado. Dimensões: correctness;
    grounding; RAG faithfulness; hallucination; tool correctness; role
    adherence; hypothesis consistency; decision traceability; robustness;
    adversarial behavior; context management; regression; safety.
  Efeito do reposicionamento:
    Torna harness-eval constitutivo — os critérios desta Spec passam a ser
    requisitos que SPEC-002+ devem satisfazer durante produção, não apenas
    sensores posteriores (F.3→constitutivo).

SPEC-021 — Harness Score / Maturity Model
  Prioridade: P1 — HIGH · Profundidade-alvo: D0–D7
  Escopo (preservado do baseline):
    L0 Declarativo → L1 Especificado → L2 Guiado → L3 Verificado
    → L4 Autocontrolado. Maturidade não se confunde com volume de
    documentação.
  Efeito do reposicionamento:
    Torna harness-score normativo por spec (não apenas repo-global);
    permite comparação de maturidade entre specs e rastreabilidade por nível.
```

### 3.4 O que NÃO muda

- O **escopo** de SPEC-019/020/021 permanece exatamente como definido no ROADMAP baseline. Esta emenda altera apenas a **posição** no ROADMAP.
- O **caminho crítico de domínio** (SPEC-002→003→004→…) preserva sua ordem interna.
- Os **bloqueadores existentes** (J-001 para SPEC-003, H-001 para SPEC-006, G-001 para SPEC-009, K-001 para SPEC-018, N-001 para SPEC-003) permanecem inalterados.
- A **numeração das specs de domínio** (SPEC-002..018) não muda; apenas a numeração das Fases de SPEC-022 em diante é ajustada (Fase 10→8, etc.).
- As **atas DHR existentes** não são alteradas (INV-07).
- O **trio Especificador→Revisor→Andraus** e o fluxo do `§23 gate por Spec` permanecem inalterados.

---

## 4. Escopo e diferimento `[PROPOSTA]`

- **Esta emenda altera apenas o ROADMAP.md** — especificamente a posição das Fases 8/9 (SPEC-019/020/021) e a renumeração das fases subsequentes.
- **Escopo de cada Spec** permanece inalterado — a redação de SPEC-019/020/021 seguirá o fluxo normal (Especificador → Revisor → Andraus) quando chegada a sua vez.
- **Não retroage** nada. SPEC-001 (HOMOLOGADA) não é reescrita.
- A adição de **Contrato de Herança Vertical** ao escopo de SPEC-019 (§3.3 acréscimo de escopo) é uma questão aberta para Andraus (Q1 abaixo).
- **Renumeração de Fases:** as Fases 10–17 do baseline passam a ser 8–15. Os números das Specs (SPEC-001..045) não mudam — apenas o número da Fase que as agrupa.

---

## 5. Non-goals `[FONTE]`

- Não altera o **escopo** de SPEC-019, SPEC-020, SPEC-021.
- Não altera o **escopo** de nenhuma spec de domínio (SPEC-002..018).
- Não cria novas specs; não elimina specs existentes.
- Não fecha nenhuma decisão aberta (J-001, G-001, H-001, I-001, K-001, L-001, C-001, M-001, N-001 permanecem abertas — CONS-01).
- Não altera o trio Especificador→Revisor→Andraus nem o gate `§23`.
- Não altera `atomic-spec.md`, `RULES.md`, `CONSTITUTION.md`, `CONFLICT-MAP.md`, `GLOSSARIO.md`.
- Não normatiza GEH-001 por si só — apenas reposiciona o ROADMAP para que SPEC-019 (que pode fazê-lo) venha antes das specs de domínio.

---

## 6. Análise de risco `[INFERÊNCIA]`

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| SPEC-019 consome tempo que atrasaria SPEC-002 (bloqueio do caminho crítico) | Média | Médio | SPEC-019 é D0–D8 HIGH, não CRITICAL; pode ser paralelizada com piloto de SPEC-001 (auditoria retroativa EUA-E15) que está em curso |
| SPEC-020 define critérios que mudam a forma de redigir specs subsequentes | Alta (é o ponto) | Positivo | Esse é exatamente o efeito desejado — constitutividade dos critérios de avaliação |
| SPEC-019 fecha L-001 de forma que colida com decisões já tomadas em SPEC-001 | Baixa | Alto | SPEC-001 não tocou o escopo de governança do harness; SPEC-019 não redefine CHM-001/CEM-001; colisão improvável mas deve ser checada pelo Revisor |
| Renumeração de Fases gera confusão em referências existentes | Baixa | Baixo | As Specs mantêm seus números; apenas o número da Fase muda; referências a "Fase 8/9" são raras nos baselines |

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação do Especificador |
|---|---|---|
| **Q1** | Ampliar o escopo de SPEC-019 para incluir explicitamente o **Contrato de Herança Vertical** (normativização do GEH-001 §6 como spec formal — Harness Inheritance Contract, regra de conservação, verificação inter-nível)? | **Sim** — é o elo que falta entre a EUA-E04 (CC-08) e uma governança vertical completa; sem isso SPEC-019 governa horizontal mas não vertical. |
| **Q2** | Aprovar o reposicionamento de SPEC-019, SPEC-020, SPEC-021 para uma **FASE GOV** interposicionada após SPEC-001 e antes de SPEC-002? | **Sim** — elimina a dependência invertida que acumula Harness Debt estrutural em cada spec de domínio produzida. |
| **Q3** | Aceitar que SPEC-019 é **processo de especificação** (não runtime cognitivo) e, portanto, deve preceder as specs que o processo governa? | **Sim** — o escopo homologado do ROADMAP confirma isso ("quem pode alterar Specs; quem cria RULE; quem aprova; versionamento; emendas…" é spec-time, não runtime). |
| **Q4** | Manter a **renumeração de Fases** (Fase 8→GOV; Fases 10–17 → 8–15) preservando a numeração de todas as Specs (SPEC-001..045 inalteradas)? | **Sim** — preserva a rastreabilidade existente (DHR-* referenciam Specs por número, não por Fase). |
| **Q5** | Registrar esta emenda no **CATÁLOGO OFICIAL** e no **CONFLICT-MAP** (nova entrada K-MAN-xx — reposicionamento de Fases altera o que o ROADMAP dizia sobre quando SPEC-019/020/021 chegam)? | **Sim** — INV-07 (rastreabilidade) exige registro; CONFLICT-MAP deve refletir a mudança de posição. |

---

## 8. Fluxo de autoridade

```
[feito] Especificador (chat) redige a PROPOSTA (este arquivo)
   ↓
Andraus valida o diagnóstico e leva ao Claude Code
   ↓
Especificador (Claude Code) refina e formaliza a proposta no repo
   ↓
Revisor SOT emite parecer (CONFORME / NÃO CONFORME)
   contra: ROADMAP.md · atomic-spec.md · SDD-001 · PPQ-001 · CONS-01 ·
           CEE-001 §12 · decisões abertas ativas · INV-07/09
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Controlador atualiza ROADMAP.md · CATÁLOGO OFICIAL · CONFLICT-MAP (K-MAN-xx) · RMR-001 (passo 11-bis)
   ↓
Próximo trabalho autorizado: SPEC-019 (Fase GOV, posição 1)
```

---

## 9. Evidências de suporte (âncoras documentais)

| Afirmação | Evidência | Tipo |
|---|---|---|
| SPEC-019 escopo = governança de especificação, não runtime | `ROADMAP.md §11`: *"quem pode alterar Specs; quem cria RULE; quem aprova; versionamento; emendas; Constitution Check; impacto em schemas/RAG/Skills/testes; compatibilidade; rollback; exceções; auditoria"* | `[FATO DOCUMENTADO]` |
| L-001 aberta, gateia SPEC-019, ativa desde baseline F.1 | `auditoria-saude-harness.md §5`: *"L-001 (SPEC-019)"* | `[FATO DOCUMENTADO]` |
| Harness Inheritance Contract ausente (normativo) | `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §12/Q14`: *"Não. [...] nenhum contrato de herança vertical pai→filho"* | `[FATO ESTRUTURAL]` |
| harness-eval/score não constitutivos durante especificação | `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §8/Q13`: *"Não foi encontrada evidência documental de uso constitutivo"* | `[FATO ESTRUTURAL]` |
| SPEC-020/021 apenas planejadas | `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §20` | `[FATO DOCUMENTADO]` |
| GEH-001 conceitual, não normativo | `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §12`: *"apenas o substrato conceitual (GEH-001) e um análogo horizontal (MAN-001). A propagação vertical é ambição documentada, não regra vigente."* | `[FATO ESTRUTURAL]` |
| MAN-001 = convergência horizontal, não vertical | `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §12`: *"MAN-001 resolve o horizontal, não o vertical"* | `[FATO DOCUMENTADO]` |
| Custo de retroativação existe mas é controlável | Regime D-DHR-PAP-001-01 (retroativo-como-auditoria); CIC-001 (Harness Debt) | `[FATO DOCUMENTADO]` |

---

*PROPOSTA não-homologada. Nenhum arquivo do repositório foi alterado. Autoridade literal permanece: `ROADMAP.md` baseline (2026-09-12) + `atomic-spec.md` v1.4 + emendas EUA-E04..E16 vigentes. Para homologação: Especificador (Claude Code) deve formalizar a proposta no repo, submetê-la ao Revisor e obter consenso de Andraus (GMC-001 Cap.5).*
