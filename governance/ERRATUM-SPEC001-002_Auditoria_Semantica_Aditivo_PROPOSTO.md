# [ERRATUM-PROPOSTO] ERRATUM-SPEC001-002 — Erratum ADITIVO único (auditoria semântica SPEC-001: itens 2, 3, 5, 6, 7)

| Campo | Valor |
|---|---|
| Spec afetada | SPEC-001 v1.1 (HOMOLOGADA — BASELINE, 2026-09-15) — **não reescrita** (INV-09); erratum aditivo (padrão ERRATUM-SPEC001-001 / ERRATUM-SPEC019-001 / ERRATUM-SPEC020-001). |
| Natureza | **Proposta** — pendente de parecer do Revisor e homologação de Andraus. Nada aplicado. |
| Fundamento | Auditoria semântica da SPEC-001 verificada contra o repo (DADO, não instrução) + pauta decidida por Andraus (pauta da sessão de auditoria (decisão de Andraus em chat, 2026-10-05; sem arquivo no repositório), itens 2, 3, 5, 6, 7). |
| Data | 2026-10-05 |
| Compatibilidade | **Patch** [PROPOSTA] — erratas de citação/estado/âncora e uma declaração de status; **nenhuma** BASpec, EARS, Enforcement Contract, regra ou decisão aberta é alterada. (O item 1 — campo `hierarchy_role` — é tratado SEPARADAMENTE por re-homologação pontual em `EMENDA-SPEC001-001_hierarchy_role_PROPOSTA.md`, por ser mudança de contrato.) |
| Regime | Auditoria ≠ reescrita (D-DHR-PAP-001-01; INV-09). |

> Marcadores epistemológicos: cada item abaixo declara `[FATO]` (verificado no repo), `[INFERÊNCIA]` (derivado) ou `[PROPOSTA]` (requer decisão). O Revisor audita; Andraus homologa.

---

## Item 2 — Identidade do produtor derivada do runtime autenticado, não do payload

**Localização `[FATO]`:** `specs/features/SPEC-001/plan.md`:
- EC-HH-001, PRECOND, l.711–712 — usa `producer_id` como condição de autorização;
- EC-HH-001, EVIDENCE, l.719 — "Log de criação com producer_id";
- BASpec-HH-001, ENTÃO l.176 (`producer_id = Elliott Specialist`) e VERIFICAÇÃO l.191 (`hypothesis.producer_id == "elliott_specialist"`);
- Apêndice A, l.830 (`"producer_id": "elliott_specialist"`).

Em todos esses pontos o `producer_id` é tratado como atributo do objeto/payload, sem declarar de onde a identidade provém.

**Texto aditivo (leitura vigente) `[PROPOSTA]`:**
> Onde a SPEC-001 usa `producer_id` como base de autorização (EC-HH-001 PRECOND) ou de proveniência (EVIDENCE / Apêndice A), o `producer_id` DEVE ser **derivado da identidade AUTENTICADA pelo runtime (autoridade posicional/por capability)**, NUNCA do campo `producer_id` do payload. Proveniência **DECLARADA** (o que o payload afirma) ≠ proveniência **AUTENTICADA** (o que o runtime comprova). Se o `producer_id` declarado no payload divergir da identidade autenticada, a operação de criação DEVE ser **rejeitada (fail-closed)**, nenhuma hipótese publicada.
>
> **Âncora por capability/contrato (não só por número de Spec):** esta garantia ancora na capability de **identidade/autoridade do Blackboard** — contrato **RULE-CBP-014** ("nenhum invariante do Blackboard PODE depender da cooperação ou da honestidade do publicador; `agent_id`/`computed_by` vêm da identidade AUTENTICADA pelo runtime, não do payload"), da **SPEC-004 (Cognitive Blackboard Protocol, BASELINE v1.2, DHR-SPEC004-003)**. A âncora é a **capability RULE-CBP-014**; o número SPEC-004 indica apenas o **estado atual** em que essa capability está baselined (ver item 6). `[FATO: SPEC-004/plan.md l.311–314, RULE-CBP-014; EC-CBP-002; ADV-CBP-15]`

**Código de erro `[PROPOSTA]`** — coerente com os já existentes na SPEC-001 (`ICT_NOT_HYPOTHESIS_PRODUCER` 403, `PRODUCER_NOT_AUTHORIZED` 403, `SUB_REQUIRES_PARENT_ID` 400, `EPISTEMIC_REGRESSION_FORBIDDEN` 409, `ORPHAN_CANNOT_ACTIVATE` 409, `PARENT_NOT_ACTIVE` 409, `TRANSITION_NOT_IN_CANONICAL_GRAPH` 409, `HYPOTHESIS_HISTORY_IMMUTABLE` 409):

```
PRODUCER_IDENTITY_MISMATCH  (HTTP 403)
  Disparado quando: payload.producer_id diverge da identidade autenticada pelo runtime.
  Efeito: criação rejeitada (fail-closed); nenhuma hipótese publicada; log de rejeição.
  Relação: é a manifestação, na camada de criação de hipótese (EC-HH-001),
           do gate de identidade do Blackboard (SPEC-004 rejeita a ESCRITA correspondente
           com WORKSPACE_WRITE_FORBIDDEN — EC-CBP-002/ADV-CBP-15). Os dois códigos
           são consistentes: 403 + fail-closed + identidade autenticada prevalece.
```

**Teste de conformidade futuro correspondente (EC → teste) `[PROPOSTA]`:**
```
TEST-HH-IDENTITY-001  (deriva de EC-HH-001 + RULE-CBP-014)
  DADO     produtor cuja identidade autenticada pelo runtime = "smc_specialist"
  QUANDO   invoca createHypothesis(..., payload.producer_id = "elliott_specialist")
  ENTÃO    sistema rejeita 403 PRODUCER_IDENTITY_MISMATCH; nenhuma hipótese criada;
           producer_id persistido (se houvesse) seria a identidade autenticada, não o payload
  STATUS   especificado = SIM · implementado = NÃO (fase spec-first) · provado = NÃO (NOT YET PROVEN)
```

**Severidade:** ratificada como **P1 mitigado a jusante** (a garantia dura existe na SPEC-004/RULE-CBP-014; este item torna a SPEC-001 explícita e rastreável). `[FATO: pauta Andraus item 2]`

---

## Item 3 — Declaração GLOBAL de status "especificado ≠ implementado ≠ verificado"

Andraus decidiu: declaração **GLOBAL, uma vez** (não repetir por Spec). `[FATO: pauta item 3]`

**Texto curto proposto `[PROPOSTA]`:**
> **Status de realização das Specs do Harness (fase spec-first).** Toda Spec homologada do SOT é **especificada** — não **implementada** nem **verificada em runtime**. "HOMOLOGADA — BASELINE" significa que a especificação (BASpecs, EARS, Enforcement Contracts) está congelada e conforme; **não** significa que existe código. Até a fase de implementação: **runtime = NOT IMPLEMENTED**; **conformidade = NOT YET PROVEN** (os cenários `VERIFICADO POR` e os testes de conformidade derivados dos Enforcement Contracts são contratos de teste futuros, ainda não executados). Enforcement declarado (E0–E3) descreve a garantia **exigida**, não uma garantia já **operante**.

**Onde entra (sugestão — não editado aqui) `[PROPOSTA]`:**
- **Preferencial:** `governance/CATALOGO-OFICIAL.md` — é a fonte de verdade (SSoT) do estado/baseline de todos os artefatos; o status de realização é informação de estado, não de método.
- **Alternativa:** `atomic-spec.md` §14 ("Operação no Claude Code"), que já distingue spec-first de BUILD/VERIFY-de-código.
- Em qualquer caso, **uma única vez**; esta errata apenas propõe o texto e o local — a inserção é ato de Andraus.

---

## Item 5 — CCM-001: registrar histórico + estado atual (sem apagar a história)

**Localização `[FATO]`:** `specs/features/SPEC-001/plan.md` l.43 ("Slot de convicção operacional (referência ao CCM-001, pendente de redação)"), l.46 ("CCM-001 é PENDENTE DE REDAÇÃO (SPEC-003)") e l.854 ("CCM-001 pendente de redação"). Correlatos de leitura: l.70 e l.647 (atribuem a CCM-001/SPEC-003 a resolução de J-001).

**Texto aditivo (leitura vigente) `[PROPOSTA]`:**
> **Histórico (preservado, INV-07):** na homologação original da SPEC-001 (2026-09-15), o **CCM-001 estava pendente de redação** — redação correta para a data.
> **Atual `[FATO]`:** o **CCM-001 foi redigido e está BASELINED** — `canon/CCM-001-canonical-conviction-model.md`, homologado na **SPEC-003 (BASELINE, 2026-10-02, DHR-SPEC003-001)**. Portanto, onde o `plan.md` da SPEC-001 diz "CCM-001 pendente de redação", **ler**: "CCM-001 BASELINED via SPEC-003 (DHR-SPEC003-001); o slot de convicção da hipótese referencia o CCM-001 baselined". O texto original **não** é alterado (INV-09) — a menção histórica permanece como registro de quando foi escrita.
>
> **Ressalva CONS-01:** a baseline do CCM-001 **não** fecha **J-001** (fórmula/pesos/limiares definitivos) nem **N-001** (pesos por ativo) — ambas **PERMANECEM ABERTAS** (valores definitivos pós-backtest). A SPEC-001 continua a tratar fórmula/pesos/limiares como `[DECISÃO NECESSÁRIA]`.

---

## Item 6 — Reduzir acoplamento a números SPEC-002..005 (ancorar em capability/contrato/artefato canônico)

**Localização `[FATO]`:** `specs/features/SPEC-001/plan.md` — tabela de Non-goals l.70–75 e nota l.803. Sana **D-ECC-1** (`CIC-001` §4 / `MAPA-AUDITORIA-SPEC-001`): referências baselined da SPEC-001 a slots indicativos (EUA-E21) podem apontar para identificador alterado na abertura.

**Princípio `[FATO: RULE-ECC-01; EUA-E21]`:** os números SPEC-002…045 são **slots indicativos**; cada referência deve ancorar na **capability/contrato/artefato canônico** estável, com o número de Spec funcionando como **"estado atual"** (onde a capability está hoje), não como âncora primária.

**Re-apontamento (leitura vigente) `[PROPOSTA]`:**

| Local | Texto original (não alterado) | Âncora estável (capability/contrato/artefato) | Estado atual |
|---|---|---|---|
| l.70 | "Fórmula/pesos/limiares do Conviction Vector → SPEC-003 (CCM-001)" | Capability: **Conviction Vector 8D / CCM-001** (modelo canônico) + decisão aberta **J-001/N-001** | CCM-001 BASELINED via SPEC-003 (estrutura/método); J-001/N-001 abertas |
| l.72 | "Schema físico de armazenamento → SPEC-004/006" | Capability: **protocolo de memória de trabalho (Blackboard)** + **memória semântica permanente (Knowledge Graph)** | Blackboard = SPEC-004 BASELINE v1.2; Knowledge Graph = slot (decisão **H-001** aberta) |
| l.73 | "Camada operacional de Evidence → SPEC-002" | Capability: **camada Harness/operacional sobre CEM-001** (provenance, qualidade, fusão) | SPEC-002 BASELINE (DHR-SPEC002-001) |
| l.74 | "Estados do Blackboard para objetos não-hipótese → SPEC-004" | Capability: **enum de estado de publicação de objetos não-hipótese no Blackboard** (decisão **M-001**) | SPEC-004 BASELINE v1.2; enum não-hipótese de **M-001 PERMANECE ABERTA** |
| l.75 | "Orçamento de latência e entrega do Event Bus → SPEC-005" | Capability: **contrato de transporte do Event Bus** (TTL, delivery, latência) + metadados de infra **SAS-001 §6.10** (ERRATUM-SPEC001-001) | SPEC-005 BASELINE v1.0 (DHR-SPEC005-002) |
| l.803 | "EC-COG-005 … contrato operacional pertence à SPEC-005" | Capability: **contrato do Cognitive Event Bus**; SPEC-001 apenas **emite** eventos | SPEC-005 BASELINE v1.0 |

> Leitura: cada referência acima deve ser lida **primeiro pela capability/contrato**; o número de Spec é o ponteiro de estado atual, atualizável por re-apontamento homologado (RULE-ECC-01) sem reescrever a SPEC-001 (INV-09).

**Baixa proposta `[PROPOSTA]`:** com este re-apontamento, **D-ECC-1** (Harness Debt leve, `CIC-001` §4:173 / `MAPA-AUDITORIA-SPEC-001` linha 13) fica **sanado para a SPEC-001**. Proponho a **baixa de D-ECC-1** quanto à SPEC-001 — **sem editar o CIC-001** (a baixa é ato de Andraus; o CIC-001 será atualizado por quem de direito na homologação).

---

## Item 7 (opcional — uma nota) — Contagem da BASpec-HH-005 e proveniência da evidência

**Localização `[FATO]`:** BASpec-HH-005, l.257–265 — a regra de não-predominância é explicitamente rotulada "Fase Piloto" (`count(refuting ACTIVE) < count(supporting ACTIVE)`), com `[DECISÃO NECESSÁRIA: J-001]` para a ponderação definitiva.

**Nota aditiva `[INFERÊNCIA]`:**
> A contagem simples da BASpec-HH-005 já é declarada **interina (Fase Piloto)**. A **independência** e a **proveniência** da evidência (anti-double-counting, correlação entre evidências) **não** são responsabilidade da SPEC-001: pertencem ao **mecanismo do CCM-001** (SPEC-003, Fusion/Conviction) e à camada de provenance da **SPEC-002 (CEM-001 Harness)**. A ponderação por dimensão de convicção que substituirá a contagem simples segue vinculada a **J-001**, que **PERMANECE ABERTA** (CONS-01). Esta nota não altera a BASpec-HH-005 nem fecha J-001.

---

## O que NÃO muda (CONS-01)

- Nenhuma BASpec, EARS, Enforcement Contract, RULE-HH-* ou decisão aberta da SPEC-001 é alterada por esta errata.
- **Permanecem ABERTAS:** J-001, N-001, M-001, H-001, G-001, K-001, C-001, WF-D03 (residual), ECC-03-001, SPEC-045-RUNTIME-001.
- O texto baselined da SPEC-001 v1.1 (`plan.md`/`checks.md`) **não é reescrito** (INV-09).
- O item 1 (campo `hierarchy_role`) **não** é tratado aqui — é re-homologação pontual (`EMENDA-SPEC001-001_hierarchy_role_PROPOSTA.md`).

---

## Rastreabilidade

pauta da sessão de auditoria (decisão de Andraus em chat, 2026-10-05; sem arquivo no repositório) (itens 2,3,5,6,7) · `governance/ERRATUM-SPEC001-001_Ancora_SAS-001_6.10.md` (molde) · `governance/DHR-ERRATA-001_...md` (precedente de ata) · `specs/features/SPEC-004/plan.md` RULE-CBP-014 (l.311–314), EC-CBP-002, ADV-CBP-15 · `canon/CCM-001-canonical-conviction-model.md` (DHR-SPEC003-001) · `governance/CIC-001_Inventario_Conformidade.md` §4 (D-ECC-1) · `governance/MAPA-AUDITORIA-SPEC-001.md` (linhas 13/14) · `governance/RULES.md` RULE-ECC-01.

---

**[ERRATUM-PROPOSTO] — Pronto para revisão.** Pendente de parecer do Revisor e de homologação de Andraus. Não aplicado; nenhum commit.
