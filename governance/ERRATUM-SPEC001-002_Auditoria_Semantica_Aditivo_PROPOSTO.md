# [HOMOLOGADO — aplicado em 2026-10-05, DHR-AUDIT-SPEC001-001] ERRATUM-SPEC001-002 — Erratum ADITIVO único (auditoria semântica SPEC-001: itens 2, 3, 5, 6, 7)

| Campo | Valor |
|---|---|
| Spec afetada | SPEC-001 v1.1 (HOMOLOGADA — BASELINE, 2026-09-15) — **não reescrita** (INV-09); erratum aditivo (padrão ERRATUM-SPEC001-001 / ERRATUM-SPEC019-001 / ERRATUM-SPEC020-001). |
| Natureza | **HOMOLOGADO e APLICADO** por ordem direta de Andraus (chat, 2026-10-05; DHR-AUDIT-SPEC001-001; Revisor CONFORME COM RESSALVAS, 2 rodadas). O conteúdo abaixo mantém a redação original da proposta (marcadores [PROPOSTA] = texto submetido; hoje vigente). |
| Fundamento | Auditoria semântica da SPEC-001 verificada contra o repo (DADO, não instrução) + decisões de Andraus na **sessão de auditoria (chat, 2026-10-05; sem arquivo no repositório)**, itens 2, 3, 5, 6, 7. **Decisões de Andraus (2026-10-05) que fundamentam este erratum e a emenda correlata:** (a) campo `hierarchy_role` (emenda); (b) **erratum de identidade** (item 2, `PRODUCER_IDENTITY_MISMATCH`); (c) declaração global de status no **`governance/CATALOGO-OFICIAL.md`** (item 3); (d) compatibilidade **Minor** (conjunto); (e) **ordem**: erratum (item 2) **antes** da emenda (§0); (f) **baixa de D-ECC-1 somente APÓS** a homologação deste erratum (item 6); (g) **mapeamento produtor→`hypothesis_type` adiado** às Specs dos especialistas (tratado na emenda §8). `[FATO: sessão de auditoria em chat, 2026-10-05 — sem arquivo no repositório; DHR de rastreabilidade sugerido ao final]` |
| Data | 2026-10-05 |
| Compatibilidade | **Minor** [PROPOSTA] — reclassificada de Patch para **Minor** por decisão de Andraus (2026-10-05). Motivo: o **Item 2 é ADITIVO** — acrescenta um código de erro novo (`PRODUCER_IDENTITY_MISMATCH`, HTTP 403) e um contrato de teste novo (`TEST-HH-IDENTITY-001`) à superfície de conformidade da SPEC-001; acréscimo aditivo de comportamento verificável é **Minor** (não Patch, não Major — nenhum contrato existente é quebrado nem semântica alterada). Os **itens 3, 5, 6 e 7 são Patch isoladamente** (erratas de citação/estado/âncora e uma declaração de status — nada aditivo), mas, como o erratum é **único**, a classificação do **conjunto** sobe ao maior nível presente = **Minor**. **Nenhuma** BASpec, EARS, Enforcement Contract, regra ou decisão aberta existente é alterada. (O item 1 — campo `hierarchy_role` — é tratado SEPARADAMENTE por re-homologação pontual em `EMENDA-SPEC001-001_hierarchy_role_PROPOSTA.md`, por ser mudança de contrato; ordem decidida no §0.) |
| Regime | Auditoria ≠ reescrita (D-DHR-PAP-001-01; INV-09). |

> Marcadores epistemológicos: cada item abaixo declara `[FATO]` (verificado no repo), `[INFERÊNCIA]` (derivado) ou `[PROPOSTA]` (requer decisão). O Revisor audita; Andraus homologa.

---

## 0. Co-dependência e ordem com a EMENDA-SPEC001-001 `[FATO: decisão de Andraus, 2026-10-05]`

Este erratum e a `EMENDA-SPEC001-001_hierarchy_role_PROPOSTA.md` (campo `hierarchy_role`) têm **ordem decidida por Andraus**:

- **Este ERRATUM (item 2) é homologado e aplicado ANTES da EMENDA.** A PRECOND reescrita do EC-HH-001 pela emenda (§3 da emenda) passa a tratar `producer_id` como **identidade AUTENTICADA pelo runtime** — garantia que **este item 2 introduz**. Logo, item 2 precede a emenda no caminho de homologação.
- **Os itens 3, 5, 6 e 7 deste erratum INDEPENDEM da emenda** — podem ser homologados sem relação de ordem com ela.
- **Nenhuma outra dependência cruzada.**

> Os dois documentos citam-se mutuamente de forma coerente: este §0 ↔ EMENDA §0 (co-dependência e ordem); item 2 ↔ EMENDA §3 (PRECOND com identidade autenticada).

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

**Onde entra — LOCAL DECIDIDO por Andraus (2026-10-05) `[FATO: decisão de Andraus]`:**
- **Local decidido: `governance/CATALOGO-OFICIAL.md`** — é a fonte de verdade (SSoT) do estado/baseline de todos os artefatos; o status de realização é informação de estado, não de método. A declaração entra **uma única vez**, global.
- *(Nota histórica, não-alternativa:)* na redação original deste erratum cogitou-se `atomic-spec.md` §14 ("Operação no Claude Code") como alternativa; **essa alternativa foi descartada** por Andraus — o local é o CATALOGO. Registro mantido apenas para rastreabilidade da decisão.
- Esta errata apenas **propõe o texto**; a inserção no `CATALOGO-OFICIAL.md` é **ato de Andraus** — este erratum **não edita o CATALOGO**.

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

**Baixa proposta `[PROPOSTA]`:** com este re-apontamento, **D-ECC-1** fica **sanado para a SPEC-001**. A existência do débito **D-ECC-1 foi verificada** em `governance/CIC-001_Inventario_Conformidade.md` **§4, linha 173** (Harness Debt leve — "refs baselined da SPEC-001 a slots SPEC-002..005 podem apontar para identificador alterado na abertura"), correlacionado a `MAPA-AUDITORIA-SPEC-001` linha 13. `[FATO: CIC-001 §4:173 lido nesta sessão]`
> **Baixa efetiva somente APÓS a homologação deste erratum** (decisão de Andraus, 2026-10-05): a baixa de D-ECC-1 é **ato de Andraus** na/após a homologação — este erratum apenas **propõe** a baixa. **Este erratum NÃO edita o CIC-001**; o CIC-001 será atualizado por quem de direito no ato de homologação. Até lá, D-ECC-1 permanece registrado como está.

---

## Item 7 (opcional — uma nota) — Contagem da BASpec-HH-005 e proveniência da evidência

**Localização `[FATO]`:** BASpec-HH-005, l.257–265 — a regra de não-predominância é explicitamente rotulada "Fase Piloto" (`count(refuting ACTIVE) < count(supporting ACTIVE)`), com `[DECISÃO NECESSÁRIA: J-001]` para a ponderação definitiva.

**Nota aditiva `[INFERÊNCIA]`:**
> A contagem simples da BASpec-HH-005 já é declarada **interina (Fase Piloto)**. A **independência** e a **proveniência** da evidência (anti-double-counting, correlação entre evidências) **não** são responsabilidade da SPEC-001: pertencem ao **mecanismo do CCM-001** (SPEC-003, Fusion/Conviction) e à camada de provenance da **SPEC-002 (CEM-001 Harness)**. A ponderação por dimensão de convicção que substituirá a contagem simples segue vinculada a **J-001**, que **PERMANECE ABERTA** (CONS-01). Esta nota não altera a BASpec-HH-005 nem fecha J-001.

---

## Item 8 (ACH-005, opcional — Andraus decide) — Rastreabilidade das decisões tomadas em chat `[PROPOSTA]`

As decisões que fundamentam este erratum e a emenda correlata foram tomadas **em chat** (sessão de auditoria, 2026-10-05), **sem arquivo no repositório** — achado Menor de rastreabilidade do Revisor (ACH-005). **Sugestão (não vinculante; decisão de Andraus):** abrir uma **ata DHR de sessão de auditoria** registrando, com data e autoria, as decisões de 2026-10-05 (hierarchy_role; erratum de identidade; declaração no CATALOGO; compat. Minor; ordem erratum→emenda; baixa de D-ECC-1 pós-erratum; mapeamento `hypothesis_type` adiado às Specs dos especialistas), à qual este erratum e a emenda passariam a ancorar o `[FATO]`. O Especificador **não cria** essa ata (ato de Andraus); apenas sugere.

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

**[ERRATUM-PROPOSTO] — Pronto para revisão.** Compatibilidade **Minor** (conjunto; item 2 aditivo). **Ordem decidida (§0):** homologado/aplicado **ANTES** da EMENDA-SPEC001-001 (co-dependência pela identidade autenticada); itens 3, 5, 6, 7 independem da emenda. Pendente de parecer do Revisor e de homologação de Andraus. Não aplicado; nenhum commit.
