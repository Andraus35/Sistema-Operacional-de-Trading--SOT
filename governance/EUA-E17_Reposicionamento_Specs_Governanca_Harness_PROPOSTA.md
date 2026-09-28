# EUA-E17 — Reposicionamento das Specs de Governança do Harness no ROADMAP (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E17** (emenda ao `ROADMAP.md`) |
| Versão | **v2 — formalizada no Claude Code** (Especificador, 2026-09-21). Supersede o rascunho de chat homônimo (raiz), incorporando o parecer do Revisor (M-01/M-02/M-03, m-01/m-02). |
| Natureza | Emenda de **reposicionamento sequencial** no ROADMAP (posição de SPEC-019/020/021 + renumeração de fases) **com um acréscimo de escopo pontual à SPEC-019, condicionado à decisão Q1 de Andraus** (ver §0 e §3.3). Não altera baselines nem o escopo das specs de domínio (SPEC-002..018). |
| Status epistemológico | **HOMOLOGADA — vigência imediata** (DHR-EUA-E17, Andraus, 2026-09-21; Q1–Q6 = Sim; parecer do Revisor CONFORME na v2). Efeitos registrados no `ROADMAP.md`, `CATALOGO-OFICIAL.md`, `CONFLICT-MAP.md` (K-MAN-20) e nos agentes (RPSA). Renumeração editorial de cabeçalhos do ROADMAP = passo diferido. *(Filename mantém "_PROPOSTA" por convenção de repositório — o status vigente é este e o do CATÁLOGO/DHR.)* |
| Autoria | Rascunho: Especificador (chat — Andraus/Claude Sonnet 4.6, 2026-09-21). Formalização: Especificador (Claude Code, Opus 4.8, 2026-09-21). |
| Data | 2026-09-21 |
| Alvo | `ROADMAP.md` — sequência de fases; interposição de uma FASE GOV e renumeração das fases subsequentes |
| Fundamento no baseline | **SDD-001** (todo artefato com dependência precede os que dele dependem); **PPQ-001 dial GES** (rigor proporcional ao impacto — governança é transversal); **CONS-01** (decisão aberta não é fechada — L-001 aberta); **CEE-001 §12 4Es** (Eficácia precede Eficiência — governança é Eficácia); **PAP-001 §6** (gate do Revisor por classe — pressupõe que a governança existe antes de ser aplicada) |
| Princípio-guia | **Uma spec que governa a produção de outras specs deve preceder essas specs, salvo na parte cuja redação depende de conteúdo que só as specs de domínio produzem.** |

---

## 0. Declaração de escopo desta emenda (correção M-02) `[PROPOSTA]`

Para eliminar a tensão apontada pelo Revisor (achado M-02), esta emenda declara explicitamente **o que altera** e **o que não altera**:

**Altera (posição/estrutura do ROADMAP):**
1. A **posição** de SPEC-019, SPEC-020, SPEC-021 — antecipadas para uma FASE GOV interposta entre SPEC-001 (homologada) e SPEC-002.
2. A **numeração das fases** subsequentes (Fases 10–17 → 8–15). A numeração das **Specs** (SPEC-001..045) **não** muda.

**Altera condicionalmente (escopo — só se Andraus aprovar Q1):**
3. Um **acréscimo de escopo à SPEC-019** (Contrato de Herança Vertical macro→micro). Este item **não** é reposicionamento; é ampliação de escopo, isolada aqui e submetida como decisão explícita **Q1**. Se Andraus reprovar Q1, a emenda vale apenas para os itens 1–2 e a SPEC-019 mantém o escopo do baseline.

**Não altera:** o **escopo** de SPEC-020/021; o escopo das specs de domínio; o trio Especificador→Revisor→Andraus; o gate `§23`; nenhum invariante; nenhuma decisão aberta (todas permanecem abertas — CONS-01).

> **Correção do rascunho:** o cabeçalho do rascunho afirmava "não altera seu escopo nem seus baselines". Isso valia para SPEC-020/021, mas **não** para a SPEC-019 (item 3). A afirmação foi corrigida acima: há um acréscimo de escopo à SPEC-019, e ele está isolado como decisão condicional Q1.

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

Três dependências invertidas documentadas:

**Dependência 1 — SPEC-019 após SPEC-018:** o escopo homologado da SPEC-019 é *"quem pode alterar Specs; quem cria RULE; quem aprova; versionamento; emendas; Constitution Check; impacto em schemas/RAG/Skills/testes; compatibilidade; rollback; exceções; auditoria"* (`ROADMAP.md §11`). É **governança do processo de especificação**, não de runtime cognitivo. Sem SPEC-019, cada emenda futura às SPEC-002..018 opera sem base formal; o processo (Especificador→Revisor→Andraus) existe como **método** (`atomic-spec.md`), não como Spec de domínio. **L-001** (`auditoria-saude-harness.md §5`) depende de SPEC-019 e está ativa desde a baseline F.1.

**Dependência 2 — SPEC-020 após SPEC-019:** enquanto SPEC-020 não existir, nenhuma das SPEC-001..019 foi avaliada contra **critérios constitutivos** — apenas contra o método atômico e o gate determinístico. `harness-eval`/`harness-score` são proxies (F.3/F.4) usados **postumamente**. A auditoria `docs/arranque/AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §8/Q13` documenta isso como `[FATO ESTRUTURAL]`: *"Não foi encontrada evidência documental de uso constitutivo de harness-eval/harness-score durante a especificação."*
> **Ressalva de dependência (correção M-01, ver §2.1):** parte das dimensões da SPEC-020 depende de conteúdo de domínio que só specs posteriores produzem. A antecipação **integral** da SPEC-020 criaria uma dependência invertida simétrica. Por isso esta emenda antecipa apenas o **núcleo constitutivo** da SPEC-020 (§3.3).

**Dependência 3 — ausência de Harness Inheritance Contract:** a EUA-E04 (CC-08, Herança/Delta) já exige a **declaração** de herança em spec-time para SPEC-002+. Falta a **regra de conservação verificável entre níveis** (macro→micro) — que GEH-001 descreve **conceitualmente** e que a SPEC-019 é o locus natural para normativizar. `AUDITORIA-…md §12/Q14`: *"nenhum contrato de herança vertical pai→filho entre harnesses."* `[FATO ESTRUTURAL]`

### 1.2 Base de evidência (nota de status)

Esta emenda apoia-se na auditoria `docs/arranque/AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md`, que é uma **auditoria não-homologada** (documentado ≠ homologado, TRACE-06). Seus achados são usados como `[FATO ESTRUTURAL]`/`[FATO DOCUMENTADO]` de diagnóstico, **não** como norma. A autoridade normativa permanece nos baselines (ROADMAP, atomic-spec, canon/).

### 1.3 O que já está resolvido parcialmente

A **EUA-E04** (CC-08, homologada 2026-09-20) já introduz a **declaração** de herança como requisito de spec-time para SPEC-002+ — o passo mais importante e já vigente. Faltam a **regra de conservação entre níveis** (objeto do acréscimo à SPEC-019, Q1) e os **critérios de avaliação constitutivos** (objeto da SPEC-020).

---

## 2. Mapa de rastreabilidade — dependências formais `[INFERÊNCIA]`

### 2.1 Classificação das dimensões da SPEC-020 (correção M-01)

O achado M-01 do Revisor observou que a premissa "todas as dimensões da SPEC-020 são independentes do conteúdo" é **parcialmente falsa**. Correção — as 13 dimensões do escopo baseline (`ROADMAP.md §12`) classificam-se em duas classes:

| Classe | Dimensões | Pode ser redigida antes das specs de domínio? |
|---|---|---|
| **(A) Constitutiva-independente** — disciplina de como *qualquer* spec deve ser avaliável | correctness · grounding · hallucination · role adherence · context management · safety · regression (como disciplina) · robustness/adversarial (como método) | **Sim** — não dependem de nenhum componente específico |
| **(B) Dependente-de-upstream** — só é operacionalizável quando o componente-alvo existe | RAG faithfulness (→ SPEC-007) · tool correctness (→ SPEC-038) · decision traceability (→ SPEC-014 + P13) · hypothesis consistency (→ SPEC-001, **já homologada**, logo já disponível) | **Parcial** — o critério pode ser *declarado*, mas só *fecha* no ponto de dependência |

**Consequência para a proposta:** antecipar o **núcleo (A)** da SPEC-020 como critérios constitutivos que SPEC-002+ devem satisfacer; **diferir o fechamento das dimensões (B)** ao ponto em que seu componente-alvo é especificado (RAG faithfulness junto de SPEC-007; tool correctness junto de SPEC-038; decision traceability junto de SPEC-014). `hypothesis consistency` já é fechável (SPEC-001 homologada). Isso preserva a constitutividade sem criar dependência invertida simétrica.

### 2.2 Dependências por spec

| Spec | Depende de (governança) | Efeito se SPEC-019/020 vierem depois |
|---|---|---|
| SPEC-002 | CC-08 (EUA-E04, vigente) · atomic-spec v1.5 (piloto SPEC-001) | Herança declarada; sem regra de conservação vertical (SPEC-019) |
| SPEC-003 | J-001 (bloqueador), CCM-001 | Sem critérios de avaliação constitutivos (núcleo A da SPEC-020) |
| SPEC-004..009 | Blackboard/Event Bus/KG/RAG/Scheduler/State | Herança via CC-08 sem contrato de conservação; avaliação posterior |
| SPEC-010..013 | Agentes analíticos — alto risco de Harness Debt | 8–9 specs CRITICAL/HIGH sem critérios constitutivos |
| SPEC-014..016 | Synthesis · Mission · TMP | Sem SPEC-019, rollback/impacto em schemas não especificado |
| SPEC-017..018 | Pattern Memory · Learning — K-001 aberta | Sem maturidade normativa por spec (SPEC-021) |
| SPEC-019 | **L-001 (decisão aberta ativa)** | Hoje Fase 8; produz 18 specs antes de normatizar governança |
| SPEC-020 | SPEC-019 (núcleo A); SPEC-007/038/014 (dimensões B) | Critérios só definidos após todas as specs de domínio |
| SPEC-021 | SPEC-020 (núcleo A) | Maturidade normativa por spec só após specs de domínio |

**Evidências das dependências:** L-001 gateia SPEC-019 (`auditoria-saude-harness.md §5`); Harness Inheritance Contract ausente (`AUDITORIA-…md §12/Q14` `[FATO ESTRUTURAL]`); harness-eval/score não-constitutivos (`AUDITORIA-…md §8/Q13` `[FATO ESTRUTURAL]`); SPEC-020/021 planejadas (`AUDITORIA-…md §20` `[FATO DOCUMENTADO]`).

---

## 3. Proposta de reposicionamento `[PROPOSTA]`

### 3.1 Princípio de reposicionamento

**Uma spec de governança cujo escopo incide sobre specs de domínio deve preceder essas specs no ROADMAP, salvo na parte cuja redação depende de conteúdo que só as specs de domínio produzem.**

- **SPEC-019** (Harness Governance & Evolution) — escopo inteiramente de processo/governança de especificação; não depende de conteúdo de domínio. **Deve preceder SPEC-002 (integral).**
- **SPEC-020** (Harness Evaluation) — antecipar o **núcleo constitutivo (classe A, §2.1)**; diferir o fechamento das dimensões dependentes (classe B) ao ponto de dependência. **Núcleo A precede SPEC-002; dimensões B fecham em SPEC-007/014/038.**
- **SPEC-021** (Harness Score / Maturity) — modelo L0–L4; segue o núcleo da SPEC-020, ainda antes das specs de agentes analíticos (SPEC-010+).

### 3.2 Sequência proposta

```
SEQUÊNCIA ATUAL (baseline)             SEQUÊNCIA PROPOSTA (esta emenda)
─────────────────────────              ──────────────────────────────────
FASE 0   M0 (HOMOLOGADO)               FASE 0   M0 (HOMOLOGADO) — inalterado
FASE 1   SPEC-001 (HOMOLOGADO)         FASE 1   SPEC-001 (HOMOLOGADO) — inalterado
FASE 1   SPEC-002 Evidence             FASE GOV SPEC-019 Harness Governance (integral)  ← ANTECIPADO
FASE 1   SPEC-003 Conviction           FASE GOV SPEC-020 Harness Evaluation (núcleo A)  ← ANTECIPADO
FASE 2   SPEC-004 Blackboard           FASE GOV SPEC-021 Harness Score                  ← ANTECIPADO
FASE 2   SPEC-005 Event Bus            FASE 1   SPEC-002 Evidence
FASE 3   SPEC-006 Knowledge Graph      FASE 1   SPEC-003 Conviction
FASE 3   SPEC-007 RAG                  FASE 2   SPEC-004 Blackboard
FASE 4   SPEC-008 Scheduler            FASE 2   SPEC-005 Event Bus
FASE 4   SPEC-009 Cognitive State      FASE 3   SPEC-006 Knowledge Graph
FASE 5   SPEC-010..013 Agentes         FASE 3   SPEC-007 RAG  (fecha SPEC-020 dim. RAG faithfulness)
FASE 6   SPEC-014..016 Synthesis/Mis.  FASE 4   SPEC-008 Scheduler
FASE 7   SPEC-017..018 Memory/Learn.   FASE 4   SPEC-009 Cognitive State
FASE 8   SPEC-019 Harness Gov.         FASE 5   SPEC-010..013 Agentes
FASE 9   SPEC-020 Harness Eval.        FASE 6   SPEC-014..016 (fecha SPEC-020 dim. decision traceability)
FASE 9   SPEC-021 Harness Score        FASE 7   SPEC-017..018 Memory/Learn.
FASE 10  SPEC-022 Cognitive Test       FASE 8   SPEC-022 Cognitive Test   ← renumerado
FASE 11  SPEC-023..024 Orq./Meta       FASE 9   SPEC-023..024 Orq./Meta   ← renumerado
FASE 12+ SPEC-025..045                 FASE 10+ SPEC-025..045             ← renumerado
```

> **Nota (dimensões B da SPEC-020):** o *fechamento* das dimensões dependentes ocorre no ponto de dependência (RAG faithfulness ↔ SPEC-007 na Fase 3; tool correctness ↔ SPEC-038; decision traceability ↔ SPEC-014 na Fase 6), via emenda pontual à SPEC-020 quando o componente-alvo é homologado. Isso é **complemento**, não reabertura da SPEC-020.

### 3.3 Conteúdo da FASE GOV (nova fase interposicionada)

```
FASE GOV — GOVERNANÇA DO HARNESS DE ESPECIFICAÇÃO
(interposicionada entre SPEC-001 HOMOLOGADA e SPEC-002)

Método vigente da FASE GOV (correção M-03):
  As três specs são redigidas sob o MÉTODO VIGENTE no momento da redação
  (regra do atomic-spec: divergência do método vigente = achado de revisão).
  Na data desta emenda o método vigente é atomic-spec v1.4. Se a v1.5 for
  homologada antes do início da SPEC-019, aplica-se a v1.5.
  As specs da FASE GOV NÃO dependem das 11 emendas cognitivas EUA-E04..E14
  (RULE-EPI..MET) que a v1.5 incorpora — são governança de processo, não
  disciplina cognitiva. Logo, a FASE GOV é independente do piloto EUA-E15
  (auditoria retroativa da SPEC-001), podendo correr em paralelo a ele.

SPEC-019 — Harness Governance & Evolution
  Prioridade: P0 — HIGH · Profundidade-alvo: D0–D8
  Escopo (preservado do baseline):
    Quem pode alterar Specs; quem cria RULE; quem aprova; versionamento;
    emendas; Constitution Check; impacto em schemas/RAG/Skills/testes;
    compatibilidade; rollback; exceções; auditoria.
  Acréscimo de escopo por esta emenda (SUJEITO A Q1 — decisão de Andraus):
    Contrato de herança vertical macro→micro (Harness Inheritance Contract)
    — normativiza GEH-001 §6.4/§6.7 como spec formal; define regra de conservação
    de requisitos entre harnesses pai e filho; define verificação de
    conformidade inter-nível.
    [Se Q1 = NÃO: este bloco cai e SPEC-019 mantém apenas o escopo baseline.]
  Resolve: L-001 (decisão aberta ativa desde baseline F.1).

SPEC-020 — Harness Evaluation Specification  (núcleo constitutivo — classe A)
  Prioridade: P0 — CRITICAL · Profundidade-alvo: D0–D8
  Escopo antecipado (classe A — §2.1):
    correctness; grounding; hallucination; role adherence; context
    management; safety; regression; robustness/adversarial (como método).
  Escopo diferido (classe B — fecha no ponto de dependência):
    RAG faithfulness (→ SPEC-007); tool correctness (→ SPEC-038);
    decision traceability (→ SPEC-014). hypothesis consistency já fechável
    (SPEC-001 homologada).
  Efeito do reposicionamento:
    Torna o núcleo A constitutivo — critérios que SPEC-002+ devem satisfazer
    durante a produção, não apenas sensores posteriores (F.3→constitutivo).

SPEC-021 — Harness Score / Maturity Model
  Prioridade: P1 — HIGH · Profundidade-alvo: D0–D7
  Escopo (preservado do baseline):
    L0 Declarativo → L1 Especificado → L2 Guiado → L3 Verificado
    → L4 Autocontrolado. Maturidade ≠ volume de documentação.
  Efeito do reposicionamento:
    Torna harness-score normativo por spec (não apenas repo-global);
    permite comparação de maturidade entre specs e rastreabilidade por nível.
```

### 3.4 O que NÃO muda

- O **escopo** de SPEC-020/021 permanece como no baseline (a SPEC-020 é *faseada* em núcleo A + complementos B, mas o conjunto de dimensões é o mesmo).
- O **caminho crítico de domínio** (SPEC-002→003→004→…) preserva a ordem interna.
- Os **bloqueadores** (J-001→SPEC-003, H-001→SPEC-006, G-001→SPEC-009, K-001→SPEC-018, N-001→SPEC-003) permanecem.
- A **numeração das Specs** (SPEC-001..045) não muda; só o número das Fases de SPEC-022 em diante.
- As **atas DHR** não são alteradas (INV-07).
- O **trio Especificador→Revisor→Andraus** e o gate `§23` permanecem.

---

## 4. Escopo e diferimento `[PROPOSTA]`

- **Esta emenda altera apenas o `ROADMAP.md`** — posição da FASE GOV + renumeração de fases; e, condicionalmente (Q1), acrescenta o Contrato de Herança Vertical ao escopo da SPEC-019.
- **Escopo de cada Spec** segue o fluxo normal (Especificador → Revisor → Andraus) na sua vez.
- **Não retroage.** SPEC-001 (homologada) não é reescrita.
- **Método da FASE GOV:** v1.4 vigente (ou v1.5 se homologada antes); independente do piloto EUA-E15 (§3.3).
- **Renumeração:** Fases 10–17 → 8–15. Números de Specs inalterados.

---

## 5. Non-goals `[FONTE]`

- Não altera o **escopo** de SPEC-020/021 nem de nenhuma spec de domínio (SPEC-002..018).
- Não cria novas specs; não elimina specs existentes.
- Não fecha nenhuma decisão aberta (J/G/H/I/K/L/C/M/N-001 permanecem abertas — CONS-01).
- Não altera o trio nem o gate `§23`.
- Não altera `atomic-spec.md`, `RULES.md`, `CONSTITUTION.md`, `CONFLICT-MAP.md`, `GLOSSARIO.md`.
- Não normatiza GEH-001 por si só — apenas reposiciona o ROADMAP para que a SPEC-019 (que pode fazê-lo, se Q1=SIM) venha antes das specs de domínio.

---

## 6. Análise de risco `[INFERÊNCIA]`

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| SPEC-019 atrasa SPEC-002 (bloqueio do caminho crítico) | Média | Médio | SPEC-019 é HIGH (D0–D8), não CRITICAL; pode ser paralelizada com o piloto EUA-E15 em curso |
| SPEC-020 (núcleo A) muda a forma de redigir specs subsequentes | Alta (é o ponto) | Positivo | Efeito desejado — constitutividade dos critérios de avaliação |
| Dimensões B da SPEC-020 tratadas como fechadas antes do componente-alvo (CONS-01) | Média | Alto | §2.1/§3.3 marcam as dimensões B como **diferidas**; fecham por emenda pontual no ponto de dependência — não antes |
| SPEC-019 fecha L-001 colidindo com SPEC-001 | Baixa | Alto | SPEC-001 não tocou governança do harness; Revisor deve checar na redação da SPEC-019 |
| Renumeração de Fases confunde referências | Baixa | Baixo | Specs mantêm seus números; referências a "Fase 8/9" são raras nos baselines |
| Agentes ficam dessincronizados após renumeração / mudança do "próximo autorizado" | Média | Médio | **RPSA (EUA-E16):** re-sincronizar `especificador.md`/`revisor.md` (carimbo `sincronizado-até`) na homologação — ver §8 |

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação do Especificador |
|---|---|---|
| **Q1** | Ampliar o escopo da SPEC-019 para incluir o **Contrato de Herança Vertical** (normativização do GEH-001 §6.4/§6.7 — regra de conservação + verificação inter-nível)? | **Sim** — é o elo entre a EUA-E04 (CC-08) e uma governança vertical completa; sem ele a SPEC-019 governa o horizontal mas não o vertical. |
<!-- Ajuste editorial de referência (Controlador, 2026-09-22, DHR-SPEC019-001 / K-DRIFT-GEH-01): "GEH-001 §6" → "§6.4/§6.7". O §6 do GEH-001 é "centralizar/descentralizar"; a mecânica de conservação vertical vive em §6.4 (o que nunca descentralizar) e §6.7 (o que centralizar). Não altera substância. -->
| **Q2** | Aprovar o reposicionamento de SPEC-019 (integral) + SPEC-020 (núcleo A) + SPEC-021 para uma **FASE GOV** entre SPEC-001 e SPEC-002? | **Sim** — elimina a dependência invertida sem criar a simétrica (dimensões B diferidas). |
| **Q3** | Aceitar que SPEC-019 é **processo de especificação** (não runtime) e deve preceder as specs que governa? | **Sim** — confirmado pelo escopo homologado no ROADMAP §11. |
| **Q4** | Manter a **renumeração de Fases** (Fase 8→GOV; 10–17 → 8–15) preservando a numeração das Specs? | **Sim** — preserva a rastreabilidade (DHR-* referenciam Specs por número, não por Fase). |
| **Q5** | Registrar a emenda no **CATÁLOGO OFICIAL** e no **CONFLICT-MAP** (nova entrada K-MAN-xx)? | **Sim** — INV-07 exige registro; o CONFLICT-MAP deve refletir a mudança de posição. |
| **Q6** *(novo)* | Confirmar que a **SPEC-020 é faseada** (núcleo A antecipado; dimensões B — RAG faithfulness/tool correctness/decision traceability — fechadas por emenda pontual em SPEC-007/038/014)? | **Sim** — é a mitigação do achado M-01; evita dependência invertida simétrica. |

---

## 8. Fluxo de autoridade

```
[feito] Especificador (chat) redige a PROPOSTA (rascunho, raiz)
   ↓
[feito] Revisor SOT emite parecer → NÃO CONFORME recuperável (M-01/M-02/M-03; m-01/m-02)
   ↓
[feito] Especificador (Claude Code) formaliza esta v2 em governance/ tratando os achados
   ↓
Revisor SOT re-emite parecer (CONFORME / NÃO CONFORME)
   contra: ROADMAP.md · atomic-spec.md · SDD-001 · PPQ-001 · CONS-01 ·
           CEE-001 §12 · decisões abertas ativas · INV-07/09
   ↓
Andraus homologa (decide Q1–Q6)
   ↓
Controlador atualiza: ROADMAP.md · CATÁLOGO OFICIAL · CONFLICT-MAP (K-MAN-xx) · RMR-001 (passo 11-bis)
   ↓
RPSA (EUA-E16): re-sincronizar especificador.md / revisor.md (sincronizado-até → nova DHR)
   ↓
Próximo trabalho autorizado: SPEC-019 (Fase GOV, posição 1)
```

---

## 9. Registro de tratamento do parecer do Revisor (rastreabilidade)

| Achado do parecer | Severidade | Tratamento nesta v2 |
|---|---|---|
| **M-01** — premissa "dimensões da SPEC-020 independentes" parcialmente falsa | Média | **Tratado** — §2.1 classifica dimensões em (A) constitutiva-independente e (B) dependente-de-upstream; §3.1/§3.3 antecipam só o núcleo A e diferem B; Q6 formaliza o faseamento. |
| **M-02** — header "não altera escopo" vs acréscimo à SPEC-019 | Média | **Tratado** — §0 declara o acréscimo de escopo à SPEC-019 como item condicional isolado (Q1); cabeçalho corrigido. |
| **M-03** — método vigente da FASE GOV não declarado | Média | **Tratado** — §3.3/§4 declaram v1.4 vigente (ou v1.5 se homologada antes) e a independência do piloto EUA-E15. |
| **m-01** — arquivo na raiz | Menor | **Tratado** — esta v2 reside em `governance/`; o rascunho da raiz fica superseded (encaminhamento em §11). |
| **m-02** — re-sincronização RPSA não prevista | Menor | **Tratado** — §6 (risco) e §8 (fluxo) incluem o passo RPSA. |
| Ressalva — base em auditoria não-homologada | Ressalva | **Tratado** — §1.2 declara o status (documentado ≠ homologado; usada como diagnóstico, não norma). |

---

## 10. Evidências de suporte (âncoras documentais)

| Afirmação | Evidência | Tipo |
|---|---|---|
| SPEC-019 escopo = governança de especificação, não runtime | `ROADMAP.md §11` | `[FATO DOCUMENTADO]` |
| L-001 aberta, gateia SPEC-019 | `auditoria-saude-harness.md §5` | `[FATO DOCUMENTADO]` |
| Harness Inheritance Contract ausente | `AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md §12/Q14` | `[FATO ESTRUTURAL]` |
| harness-eval/score não constitutivos durante especificação | `AUDITORIA-…md §8/Q13` | `[FATO ESTRUTURAL]` |
| SPEC-020/021 apenas planejadas | `AUDITORIA-…md §20` | `[FATO DOCUMENTADO]` |
| SPEC-020 dimensões B dependem de SPEC-007/038/014 | `ROADMAP.md §12/§6/§9/§17` (escopos) | `[INFERÊNCIA]` |
| GEH-001 conceitual, não normativo | `AUDITORIA-…md §12`; `CATALOGO-OFICIAL.md §4` | `[FATO ESTRUTURAL]` |
| MAN-001 = convergência horizontal | `AUDITORIA-…md §12` | `[FATO DOCUMENTADO]` |
| Método vigente ao redigir = regra do atomic-spec | `atomic-spec.md` (autoridade literal / "método vigente") | `[FATO DOCUMENTADO]` |
| RPSA exige re-sync dos agentes | `DHR-EUA-E16` (RPSA) | `[FATO DOCUMENTADO]` |

---

## 11. Encaminhamento do rascunho da raiz (RPIR / HOD-001)

O rascunho de chat `EUA-E17_Reposicionamento_Specs_Governanca_Harness_PROPOSTA.md` na **raiz** é intake tratado por esta formalização. Conforme RPIR (HOD-001): "raiz = intake; tratado → pasta ou excluído; arquivar por padrão". Recomendação: **mover o rascunho para `docs/_legacy/`** (INV-07 — histórico preservado, nunca deletado) ou removê-lo se Andraus autorizar delete físico de rascunho superseded. **Este arquivo (v2, `governance/`) passa a ser a versão de referência da EUA-E17.**

---

*PROPOSTA não-homologada — v2 formalizada. Reside em `governance/` (Mapa de Pastas: emendas EUA-E* → `governance/`). Autoridade literal permanece: `ROADMAP.md` baseline (2026-09-12) + `atomic-spec.md` v1.4 + emendas EUA-E04..E16 vigentes. Para homologação: Revisor re-emite parecer → Andraus decide Q1–Q6 → Controlador registra → RPSA re-sincroniza os agentes.*
