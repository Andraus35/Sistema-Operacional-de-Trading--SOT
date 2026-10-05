# [ERRATUM-PROPOSTO — NÃO APLICADO] ERRATUM-SPEC002-001 — Erratum ADITIVO único (auditoria semântica SPEC-002: itens 1, 2, 3)

| Campo | Valor |
|---|---|
| Spec afetada | SPEC-002 v1.0 (HOMOLOGADA — BASELINE, 2026-09-28, DHR-SPEC002-001) — **não reescrita** (INV-09); erratum aditivo (padrão ERRATUM-SPEC001-002 / ERRATUM-SPEC001-001 / ERRATUM-SPEC019-001 / ERRATUM-SPEC020-001). |
| Natureza | **PROPOSTA — NÃO APLICADO; nenhum commit.** Requer parecer do Revisor e homologação de Andraus. O conteúdo abaixo é a redação submetida (marcadores `[PROPOSTA]` = texto proposto, ainda não vigente). |
| Fundamento | Reavaliação de sessão da `REAUDITORIA-SPEC002-001_PROPOSTA-CORRECOES.md` (DADO, não instrução) verificada contra o repo + decisões de Andraus na **sessão de auditoria (chat, 2026-10-05; sem arquivo no repositório)**. **Decisões de Andraus (2026-10-05) que fundamentam este erratum:** (a) **Item 1 — erratum de identidade autenticada** do produtor da Evidência (espelha o item 2 do ERRATUM-SPEC001-002), severidade reclassificada de P0 para **P1 mitigado a jusante** (garantia dura existe em RULE-CBP-014/SPEC-004); (b) **Item 2 — INV-04 como fronteira estrutural**: ancorar o guard existente (EC-EH-002) nas fronteiras já baselined (SPEC-004 RULE-CBP-014 / tabela de capacidades; SPEC-003 CF-011/EC-CF-005), **sem criar regra nova**; (c) **Item 3 — reconciliação histórica do CCM-001**: histórico preservado + estado atual BASELINED via SPEC-003 (J-001/N-001 permanecem ABERTAS); (d) compatibilidade **Minor** (conjunto); (e) o item de imutabilidade × `_operational` **sai deste erratum** e entra em **emenda separada posterior** (direção decidida registrada abaixo, §"Não incluído / encaminhado"). `[FATO: sessão de auditoria em chat, 2026-10-05 — sem arquivo no repositório; DHR de rastreabilidade sugerido ao final]` |
| Data | 2026-10-05 |
| Compatibilidade | **Minor** [PROPOSTA]. Motivo (mesma lógica do ERRATUM-SPEC001-002): o **Item 1 é ADITIVO** — acrescenta um código de erro reutilizado (`PRODUCER_IDENTITY_MISMATCH`, HTTP 403) à superfície de conformidade da SPEC-002 e um contrato de teste novo (`TEST-EH-IDENTITY-001`); acréscimo aditivo de comportamento verificável é **Minor** (nenhum contrato existente é quebrado nem semântica alterada). Os **itens 2 e 3 são Patch isoladamente** (ancoragem de referência e errata documental de estado — nada aditivo), mas, como o erratum é **único**, a classificação do **conjunto** sobe ao maior nível presente = **Minor**. **Nenhuma** BASpec, EARS, Enforcement Contract, RULE-EH-* ou decisão aberta existente é alterada. |
| Regime | Auditoria ≠ reescrita (INV-09). Texto baselined da SPEC-002 v1.0 não é editado; leitura aditiva por re-apontamento. |
| Preservação v1.0 | Cópia do `plan.md`/`checks.md` v1.0 em `docs/_legacy/` **será feita no ato de aplicação** (ato de Andraus/Controlador) — **este erratum não cria a cópia agora**. `[PROPOSTA]` |

> Marcadores epistemológicos: cada item declara `[FATO]` (verificado no repo), `[INFERÊNCIA]` (derivado) ou `[PROPOSTA]` (requer decisão). O Revisor audita; Andraus homologa. Este arquivo **não possui autoridade normativa** até a homologação.

---

## Item 1 — Identidade do produtor derivada do runtime autenticado, não do payload

**Localização `[FATO]`:** `specs/features/SPEC-002/plan.md`:
- **EC-EH-001, PRECOND, l.751** — usa `producer ∈ AUTHORIZED_EVIDENCE_PRODUCERS` como condição de autorização, sem declarar **de onde** vem a identidade do produtor;
- **EC-EH-001, EVIDENCE, l.758** — "Log de publicação (producer_id, evidence_id, timestamp)" — `producer_id` tratado como atributo registrado, sem origem declarada;
- **BASpec-EH-003, MECANISMO, l.302** — "gate determinístico sobre `producer_type/producer_id ∈ AUTHORIZED_EVIDENCE_PRODUCERS`" (é onde `producer_id` primeiro entra como base de gate; a BASpec-EH-001, l.248–267, é só alocação de ID/versão, sem `producer_id`);
- **BASpec-EH-004, ENTÃO, l.317** — "O Harness exige provenance operacional completa: `producer_type/producer_id`, …";
- **Apêndice (schema do objeto Evidence), l.709** — `"producer_id": "structural_agent"` tratado como atributo do objeto/payload.

Em todos esses pontos, a identidade do produtor é condição de autorização/proveniência, mas a Spec **não declara que a identidade provém do runtime autenticado** — deixando aberta a leitura de que o payload declararia a própria identidade (o achado P0-EH-001 da reavaliação de sessão, reclassificado P1).

> **Nota de precisão de âncora `[INFERÊNCIA]`:** a reavaliação de sessão referia "BASpec-EH-001 l.~302"; a verificação no repo mostra que `producer_id` como base de gate aparece em **BASpec-EH-003 (l.302)** e **BASpec-EH-004 (l.317)** — não em BASpec-EH-001. As âncoras acima são as reais no `plan.md` da SPEC-002.

**Texto aditivo (leitura vigente) `[PROPOSTA]`:**
> Onde a SPEC-002 usa a identidade do produtor como base de autorização (EC-EH-001 PRECOND; BASpec-EH-003 MECANISMO; BASpec-EH-004) ou de proveniência (EC-EH-001 EVIDENCE; Apêndice/schema do objeto Evidence), o `producer_id`/`producer_type` DEVE ser **derivado da identidade AUTENTICADA pelo runtime (autoridade posicional/por capability)**, NUNCA do campo `producer_id` do payload. Proveniência **DECLARADA** (o que o payload afirma) ≠ proveniência **AUTENTICADA** (o que o runtime comprova). Se o `producer_id` declarado no payload divergir da identidade autenticada, a publicação de Evidência DEVE ser **rejeitada (fail-closed)**, nenhuma Evidência publicada. Isto estende o gate de produtor existente (EC-EH-001 / BASpec-EH-003), não o substitui.

**Âncora por capability/contrato (não só por número de Spec) `[FATO]`:** esta garantia ancora na capability de **identidade/autoridade do Blackboard** — contrato **RULE-CBP-014** ("nenhum invariante do Blackboard PODE depender da cooperação ou da honestidade do publicador; `agent_id`/`computed_by` vêm da identidade AUTENTICADA pelo runtime, NÃO do payload; divergência resulta em `WORKSPACE_WRITE_FORBIDDEN`"), da **SPEC-004 (Cognitive Blackboard Protocol, BASELINE v1.2, DHR-SPEC004-003)**. A âncora é a **capability RULE-CBP-014**; o número SPEC-004 indica apenas o **estado atual** em que a capability está baselined. `[FATO: specs/features/SPEC-004/plan.md l.311–316 (RULE-CBP-014); tabela de capacidades l.341–350 ("Publicar em workspace ALHEIO = DENY", l.347); BASpec-CBP-014 l.700+; EARS #15 l.384; gate de escrita l.420–435 (WORKSPACE_WRITE_FORBIDDEN)]`

**Código de erro `[PROPOSTA]` — reutilização de contrato transversal, SEM redefinição:**

O código `PRODUCER_IDENTITY_MISMATCH` **já foi estabelecido** no **ERRATUM-SPEC001-002 (item 2, HOMOLOGADO/APLICADO 2026-10-05, DHR-AUDIT-SPEC001-001)** como a manifestação, na camada de criação de hipótese (EC-HH-001), do gate de identidade do Blackboard. Este erratum **reutiliza o MESMO código** como **contrato transversal** (capability de identidade), **não** cria uma segunda definição — a reavaliação de sessão foi explícita: "o código deve ser tratado como contrato transversal (capability de identidade), não duplicado por Spec".

```
PRODUCER_IDENTITY_MISMATCH  (HTTP 403)  — contrato transversal; definição única
  Origem do código: ERRATUM-SPEC001-002 item 2 (SPEC-001; DHR-AUDIT-SPEC001-001, 2026-10-05).
  Capability subjacente: identidade/autoridade autenticada pelo runtime — RULE-CBP-014 (SPEC-004 v1.2).
  Manifestação nesta Spec (EC-EH-001): payload.producer_id diverge da identidade autenticada
    → publicação de Evidência rejeitada (fail-closed); nenhuma Evidência publicada; log de rejeição.
  Consistência com SPEC-004: o Blackboard rejeita a ESCRITA correspondente com WORKSPACE_WRITE_FORBIDDEN
    (RULE-CBP-014 / BASpec-CBP-014 / EARS #15). 403 + fail-closed + identidade autenticada prevalece.
  Coerente com os códigos já presentes na SPEC-002 (SKILL_NOT_EVIDENCE_PRODUCER, CEM_CONTRACT_INCOMPLETE,
    PROVENANCE_INCOMPLETE, STRENGTH_IS_NOT_CONVICTION, LIFECYCLE_TRANSITION_FORBIDDEN,
    EVIDENCE_HISTORY_IMMUTABLE) — mesmo padrão 403/fail-closed dos gates de produtor/contrato.
```

**Teste de conformidade futuro correspondente (EC → teste) `[PROPOSTA]`:**
```
TEST-EH-IDENTITY-001  (deriva de EC-EH-001 + RULE-CBP-014)
  DADO     produtor cuja identidade autenticada pelo runtime = "smc_specialist"
  QUANDO   publica Evidência com payload.producer_id = "structural_agent"
  ENTÃO    sistema rejeita 403 PRODUCER_IDENTITY_MISMATCH; nenhuma Evidência publicada;
           producer_id persistido (se houvesse) seria a identidade autenticada, não o payload
  STATUS   especificado = SIM · implementado = NÃO (fase spec-first) · provado = NÃO (NOT YET PROVEN)
```

**Severidade:** **P1 mitigado a jusante** — a garantia dura já existe em **RULE-CBP-014 / SPEC-004 v1.2**; este item torna a SPEC-002 explícita e rastreável (espelha o item 2 do ERRATUM-SPEC001-002). `[FATO: reavaliação de sessão, finding P0-EH-001 reclassificado P1]`

---

## Item 2 — INV-04 como fronteira estrutural (ancoragem; SEM regra nova)

**Localização `[FATO]`:** `specs/features/SPEC-002/plan.md`:
- **EC-EH-002, l.761–772** — "Guard INV-04 (Evidence Strength ≠ Convicção)"; **PRECOND l.766** = "(tentativa de mapear Strength → dimensão/valor de convicção **detectada**)"; **LEVEL l.769** = E2 (Operacional);
- **BASpec-EH-005, l.334–353** — guard anti-promoção de Strength a Convicção;
- **RULE-EH-003, l.198–201** — Strength é peso local; não promovido a Convicção.

A reavaliação de sessão (finding P1-EH-003) observou: o EC-EH-002 descreve a PRECOND como **detecção** ("tentativa … detectada"), e por ENF-03 **detector ≠ gate** — logo o detector da SPEC-002 **não pode ser o único mecanismo** de proteção de INV-04.

**Texto aditivo (leitura vigente) `[PROPOSTA]` — ancoragem, NÃO nova regra:**
> O guard INV-04 da SPEC-002 (EC-EH-002 / BASpec-EH-005 / RULE-EH-003) é o braço **da camada de Evidência** de uma fronteira **estrutural já existente e baselined**; o detector desta Spec **não é o único mecanismo** (ENF-03). A fronteira estrutural dura reside, a jusante e por construção, em:
> - **SPEC-004 (Blackboard, BASELINE v1.2):** a tabela de capacidades (RULE-CBP-014) nega por construção **"Publicar em workspace ALHEIO = DENY"** — a camada de Evidência **não tem capability** de escrever no workspace de Convicção; `[FATO: SPEC-004/plan.md tabela de capacidades l.341–350, linha "Publicar em workspace ALHEIO" l.347; RULE-CBP-014 l.311–316]`
> - **SPEC-003 (Conviction, BASELINE):** o guard **CF-011 / EC-CF-005** (Separação Tríplice + INV-04) rejeita, **do lado da convicção**, derivar convicção a partir de Evidence Strength ou de custo/sizing; `[FATO: SPEC-003/plan.md guards "Separação Tríplice (CF-011) e INV-04 (CF-011/EC-CF-005)" l.133; BASpec-CF-011 l.588–; EARS #7 l.337 ("derivar convicção a partir de … Evidence Strength diretamente … DEVE rejeitar"); RULE-CF-008 l.286]`
>
> Assim, INV-04 é protegido em **três camadas complementares**: (i) guard/detector local da SPEC-002 (EC-EH-002, E2); (ii) ausência de capability de escrita cross-workspace na SPEC-004 (RULE-CBP-014, gate E3); (iii) guard do lado da convicção na SPEC-003 (CF-011/EC-CF-005). A regra "Strength NÃO DEVE popular/autorizar Convicção" **já é** RULE-EH-003 (SPEC-002) e INV-04 — **nenhuma regra nova é criada** por este item. O EC-EH-002 **não é reescrito**; apenas se declara explicitamente a sua posição na fronteira (ENF-03).

**Ressalva CONS-01 `[FATO]`:** nada aqui parametriza convicção nem fecha **J-001** (fórmula/pesos/limiares definitivos) ou **N-001** — ambas **PERMANECEM ABERTAS**.

---

## Item 3 — CCM-001: registrar histórico + estado atual (sem apagar a história)

**Localização `[FATO]`:** `specs/features/SPEC-002/plan.md` **l.45** (CC-02: "CCM-001 permanece **pendente (SPEC-003)** — nenhum limiar ligado a convicção é fixado") e correlatos de leitura **l.46** (CC-03, J-001 em aberto), **l.133/l.167** (Non-goals apontam convicção a "SPEC-003 / J-001 / CCM-001"). No Dossiê: `specs/features/SPEC-002/research.md` **l.108** dizia "CCM-001 … pendente (SPEC-003)". `[FATO: âncoras verificadas no repo; research.md l.108 conforme reavaliação de sessão]`

**Texto aditivo (leitura vigente) `[PROPOSTA]`:**
> **Histórico (preservado, INV-07):** na homologação da SPEC-002 (2026-09-28), o **CCM-001 estava pendente de redação (SPEC-003)** — redação **correta para a data** (tanto o `plan.md` l.45 quanto o `research.md` l.108).
> **Atual `[FATO]`:** o **CCM-001 foi redigido e está BASELINED** — `canon/CCM-001-canonical-conviction-model.md`, homologado na **SPEC-003 (BASELINE, 2026-10-02, DHR-SPEC003-001)**. Portanto, onde o `plan.md`/`research.md` da SPEC-002 dizem "CCM-001 pendente (SPEC-003)", **ler**: "CCM-001 BASELINED via SPEC-003 (DHR-SPEC003-001)". O texto original **não** é alterado (INV-09) — a menção histórica permanece como registro de quando foi escrita.
> **O que a SPEC-002 continua NÃO definindo** (inalterado): fórmula de convicção, pesos, limiares/thresholds, composição do Conviction Vector — tudo sob o CCM-001 vigente (SPEC-003).
>
> **Ressalva CONS-01:** a baseline do CCM-001 **não** fecha **J-001** (fórmula/pesos/limiares definitivos) nem **N-001** (pesos por ativo) — ambas **PERMANECEM ABERTAS** (valores definitivos pós-backtest). A SPEC-002 continua a tratar fórmula/pesos/limiares como `[DECISÃO NECESSÁRIA]`.

---

## Rastreabilidade para PTR-piloto (manifesto de escopo)

> Tabela de disposição por finding (reavaliação de sessão da REAUDITORIA-SPEC002-001) + estado de realização S/I/P (specified / implemented / proven). Serve de **manifesto de escopo** para o piloto manual de PTR (Post-Treatment Reconciliation) — comparar `baseline → proposta autorizada → tratamento → estado tratado`. Marcado `[PROPOSTA]` — não vinculante até homologação.

| Finding (reavaliação) | Disposição | Artefato / linha alvo | Estado S/I/P |
|---|---|---|---|
| P0-EH-001 — identidade do produtor (reclass. **P1**) | **Tratado neste erratum (Item 1)** — leitura aditiva + código transversal `PRODUCER_IDENTITY_MISMATCH` + TEST-EH-IDENTITY-001 | SPEC-002 `plan.md`: EC-EH-001 PRECOND l.751 / EVIDENCE l.758; BASpec-EH-003 l.302; BASpec-EH-004 l.317; Apêndice l.709 | S=SIM · I=NÃO · P=NÃO |
| P1-EH-003 — INV-04 fronteira estrutural | **Tratado neste erratum (Item 2)** — ancoragem a SPEC-004/SPEC-003; sem regra nova | SPEC-002 `plan.md`: EC-EH-002 l.761–772; BASpec-EH-005 l.334; RULE-EH-003 l.198 | S=SIM · I=NÃO · P=NÃO |
| P1-EH-004 — CCM-001 "pendente" | **Tratado neste erratum (Item 3)** — errata documental aditiva | SPEC-002 `plan.md` l.45/l.46; `research.md` l.108 | S=SIM · I=N/A · P=N/A |
| P1-EH-002 — imutabilidade × `_operational` | **Encaminhado** — emenda SEPARADA posterior; direção decidida (derivar na leitura + nova versão por supersessão); NÃO cria `OperationalAssessment`; não depende de M-001 | (futuro) SPEC-002 `plan.md`: EC-EH-004 l.789–801; schema `_operational` l.718–725; BASpec-EH-009 l.430 | S=NÃO (fora deste erratum) |
| P1-EH-005 — RULE-EH estado único | **Encaminhado** — registro físico de RULE-EH-001..008 em `governance/RULES.md` é ato de Andraus/Controlador (RULE-HG-02 / RULE-REG-001), não erratum da SPEC-002 | (futuro) `governance/RULES.md` | N/A (governança) |
| P2-EH-006 — BL-012 | **Descartado** — obsoleto: BL-012 **Absorvido** em 2026-10-03 (DHR-BL012-001; RMR-001 l.135); a reavaliação de sessão o dizia "ATIVADO", desatualizado | — | N/A |
| P1-EH-007 — "runtime BLOCKED BY M-001" | **Descartado como rótulo** — exagerado; SPEC-004 v1.2 já fixa a mecânica; só o **enum** de estados não-hipótese segue em M-001 (aberta). Sem rótulo "BLOCKED" | — | N/A |
| §10 modelo transversal | **Descartado** — redundante com E0–E3/ENF-03 já existentes; proposta arquitetural, não norma | — | N/A |
| §11 "J-001 já resolvida" | **Descartado / corrigido** — **ERRO**: J-001 está **ABERTA** (CONS-01; DHR-SPEC003-001 manteve). Nunca adotado | — | N/A |

**Arquivos que o tratamento tocará QUANDO aplicado (manifesto de escopo — `[PROPOSTA]`, ato de Andraus/Controlador, não agora):**
- `specs/features/SPEC-002/plan.md` — **não reescrito**; recebe, se Andraus assim decidir, uma nota de re-apontamento/ponteiro a este erratum (padrão dos errata anteriores). `[INFERÊNCIA]`
- `docs/_legacy/` — cópia de `plan.md`/`checks.md` v1.0 preservada no ato de aplicação (INV-09).
- `governance/propostas/SPEC-002/ERRATUM-SPEC002-001_Aditivo_PROPOSTO.md` — este arquivo (recebe o cabeçalho de homologação quando aplicado, à moda do ERRATUM-SPEC001-002).
- `governance/CATALOGO-OFICIAL.md` — atualização de estado/baseline da SPEC-002 (Minor) — **ato de Andraus**; este erratum **não edita** o CATALOGO.
- *(Fora deste erratum — emendas/atos separados:)* `governance/RULES.md` (registro físico de RULE-EH — Controlador); futura emenda de imutabilidade × `_operational`.
- **Gates a rodar por quem orquestra** (este agente **não tem Bash**): `python scripts/build_map.py` + `--check` (BL-019), `python scripts/check_refs.py`, `python scripts/check_doc_sync.py`, `python scripts/validate_spec_sot.py` sobre o `plan.md` afetado — todos **antes da entrega/homologação**.

---

## Não incluído / encaminhado (fora de escopo deste erratum — por decisão de Andraus)

1. **Imutabilidade da Evidência × bloco `_operational` (P1-EH-002).** **Direção DECIDIDA por Andraus (2026-10-05):** "**derivar na leitura + nova versão por supersessão**" — `staleness_flag` e similares **derivados na leitura** (determinístico: timestamp × Timeframe Reference — BASpec-EH-009, Classe D, já compatível); tipologia/relationship gravadas **uma vez na publicação**, evolução por **nova versão (supersessão)**, nunca mutação do objeto publicado. **NÃO cria** um objeto `OperationalAssessment` (a proposta da reavaliação de sessão de criar um novo tipo persistido foi considerada excessiva e arriscada). **Não depende de M-001** (não introduz novo objeto não-hipótese persistido). Entra por **emenda SEPARADA posterior** — registrada aqui apenas como direção decidida, **não tratada neste erratum**. `[FATO: decisão de Andraus; INFERÊNCIA sobre o mecanismo compatível]`
2. **Registro físico de RULE-EH-001..008 em `governance/RULES.md` (P1-EH-005).** Pendência de **registro físico** — ato de Andraus/Controlador (RULE-HG-02 / RULE-REG-001, mesmo diferimento já declarado em DHR-SPEC002-001: "registro físico em RULES.md diferido — precedente SPEC-002"). **Não é correção da SPEC-002**; rotular as RULE-EH como "BASELINED" no texto do Plan seria estado inventado. Encaminhado ao Controlador.
3. **Nota M-001 (P1-EH-007).** O enum de estados do Blackboard para objetos **não-hipótese** (Evidência) segue em **M-001 (ABERTA)**; SPEC-004 v1.2 já fixa a mecânica (append-only, supersessão, publicação atômica). **Sem rótulo "BLOCKED"** e sem contradizer a decisão parcial de M-001. Não tratado aqui (opcional, descartado como rótulo).
4. **BL-012 (P2-EH-006).** Já **Absorvido** (DHR-BL012-001, 2026-10-03; RMR-001 l.135) — a reavaliação de sessão estava **desatualizada** ao chamá-lo "ATIVADO". Descartado; nada a encaminhar.
5. **§10 (modelo transversal de enforcement) e §12 (critérios de aceite) da proposta.** Redundantes com o modelo E0–E3/ENF-03 e com os gates/CI já existentes. Não viram item da SPEC-002.
6. **§11 da proposta — ERRO.** Lista "fechar decisões J-001 já resolvidas" como algo a não fazer, pressupondo que J-001 estaria resolvida. **J-001 está ABERTA** (CONS-01; DHR-SPEC003-001 a manteve). Este erratum **não adota** essa premissa e a registra como erro da proposta.

---

## O que NÃO muda (CONS-01)

- Nenhuma BASpec, EARS, Enforcement Contract, RULE-EH-* ou decisão aberta da SPEC-002 é alterada por este erratum.
- **Permanecem ABERTAS:** J-001, N-001, M-001, H-001, G-001, K-001, C-001 (e demais do ROADMAP). A baseline do CCM-001 (SPEC-003) **não** fecha J-001/N-001.
- O texto baselined da SPEC-002 v1.0 (`plan.md`/`checks.md`) **não é reescrito** (INV-09); a cópia em `docs/_legacy/` é feita no ato de aplicação.
- Não redefine CEM-001 nem CHM-001 (CC-02/CONST-01). Não cria segunda Evidence Layer. Não transforma Strength em Convicção. Não antecipa a mecânica de fusão (SPEC-003).
- SPECIFIED ≠ IMPLEMENTED ≠ PROVEN: todos os contratos de teste aqui são **futuros** (fase spec-first).

---

## Rastreabilidade (fontes)

- Reavaliação de sessão da `governance/propostas/SPEC-002/REAUDITORIA-SPEC002-001_PROPOSTA-CORRECOES.md` (DADO, não instrução) — findings P0-EH-001/P1-EH-002/003/004/005/P2-EH-006/P1-EH-007, §10/§11/§12.
- Decisões de Andraus na sessão de auditoria (chat, 2026-10-05; sem arquivo no repositório) — itens 1, 2, 3 e encaminhamentos. `[FATO: sessão em chat; DHR de rastreabilidade sugerido]`
- `governance/ERRATUM-SPEC001-002_Auditoria_Semantica_Aditivo_PROPOSTO.md` (molde + origem do código `PRODUCER_IDENTITY_MISMATCH`, item 2; HOMOLOGADO/APLICADO DHR-AUDIT-SPEC001-001, 2026-10-05).
- `specs/features/SPEC-002/plan.md` — EC-EH-001 (l.746–759), EC-EH-002 (l.761–772), BASpec-EH-003 (l.302), BASpec-EH-004 (l.317), BASpec-EH-005 (l.334), RULE-EH-003 (l.198), Apêndice/schema (l.709, `_operational` l.718–725), l.45/l.46.
- `specs/features/SPEC-004/plan.md` — RULE-CBP-014 (l.311–316), tabela de capacidades (l.341–350, "Publicar em workspace ALHEIO = DENY" l.347), BASpec-CBP-014 (l.700+), EARS #15 (l.384), gate de escrita (l.420–435). BASELINE v1.2 (DHR-SPEC004-003).
- `specs/features/SPEC-003/plan.md` — guards CF-011 / EC-CF-005 (l.133), BASpec-CF-011 (l.588–), EARS #7 (l.337), RULE-CF-008 (l.286). BASELINE (DHR-SPEC003-001).
- `canon/CCM-001-canonical-conviction-model.md` (BASELINED via SPEC-003/DHR-SPEC003-001).
- `governance/RULES.md` RULE-ECC-01 (slots indicativos / re-apontamento), RULE-HG-02 (registro físico), RULE-REG-001.
- `ROADMAP.md` (estado das Specs e decisões abertas) · `atomic-spec.md` v1.5 (método).

---

**[ERRATUM-PROPOSTO — NÃO APLICADO]** · Compatibilidade **Minor** (conjunto; item 1 aditivo) · Itens 1, 2, 3 em escopo (itens de imutabilidade, RULE-EH, M-001, BL-012, §10, §11 **encaminhados/descartados**, ver seção própria) · Pendente de parecer do Revisor e de homologação de Andraus · Nenhum commit · Cópia v1.0 em `docs/_legacy/` e edição do CATALOGO = atos de Andraus/Controlador no momento da aplicação.
