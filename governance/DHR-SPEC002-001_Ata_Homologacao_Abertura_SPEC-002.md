# DHR-SPEC002-001 — Ata de Homologação — Abertura da SPEC-002 (Evidence & Evidence Provenance Harness)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador de Especificação do SOT / Revisor / Controlador |
| Ref | SPEC-002 — Parecer do Revisor sobre o gate de ABERTURA: CONFORME (2026-09-28) — `specs/features/SPEC-002/PROPOSTA-ABERTURA.md` + `DOSSIE-PESQUISA.md` + `sources/SRC-01..07` |
| Data | 2026-09-28 |
| Status | **ABERTURA HOMOLOGADA** — Dossiê de Pesquisa + Proposta de Abertura homologados. **NÃO é baseline** — o Plan (`plan.md`/`checks.md`, via `tlc-spec-lean`) ainda não foi escrito; esse é o próximo gate. |
| Compatibilidade | Minor (não toca modelo canônico nem decisão aberta) |

---

## 1. Decisão

A **abertura da SPEC-002 — "Evidence & Evidence Provenance Harness" está HOMOLOGADA.**

Abertura pela **ordem regular** do ROADMAP (§25 — "próximo trabalho autorizado"), após a conclusão da FASE GOV (SPEC-019+020+021 homologadas) e da linha paralela SPEC-046 (v1.0+v1.1 homologadas). Número e nome preservados do slot indicativo (ROADMAP §4) — nenhuma divisão/renumeração/fusão (RULE-ECC-01).

**Quantidade — `[DECISÃO NECESSÁRIA: SPEC-002-SPLIT-001]` RESOLVIDA nesta ata:** **1 Spec unificada** (Opção A da Proposta) — CEM-001 já trata Evidência e Proveniência como um único contrato (Cap.3 conteúdo + Cap.5 rastreabilidade indissociáveis); dividir fragmentaria um contrato canônico único e deixaria a proveniência órfã do objeto que ela descreve. Espelha o precedente da SPEC-001 (unificou hipótese + registry + protocolo).

Fluxo cumprido até este ato: slot ROADMAP §4/§25 → Especificador produz Dossiê de Pesquisa (RULE-ECC-02, 7 fontes `[EXTERNO]` via WebSearch real — captura verbatim canônica diferida, ver §3.2) + Proposta de Abertura (número/nome/fronteira/complexidade/Classe/quantidade) → decisão de Andraus sobre `SPEC-002-VERBATIM-001` (DHR-SPEC002-VERBATIM-001, Opção A) → Revisor audita o gate de abertura → **CONFORME** (1 achado Menor ACH-MEN-01, não-bloqueante) → esta homologação, incluindo a decisão de `SPEC-002-SPLIT-001`.

---

## 2. Definição homologada

| Campo | Valor |
|---|---|
| Número/Nome | **SPEC-002 — Evidence & Evidence Provenance Harness** |
| Quantidade | **1 Spec unificada** (não dividir) |
| Complexidade | **CRITICAL** (P0) |
| Profundidade-alvo | **D0–D7** + **D8 adversarial** para BASpecs com efeito E3 |
| Maturidade-alvo | **L3** (Testável), gate normativo **E3** por-Spec (RULE-MM-05/SPEC-021) |
| Classe predominante | **H (Híbrido)**, com **C (Constitutivo)** para invariantes de imutabilidade/proveniência — declaração normativa por BASpec, no Plan (CC-11/RULE-MECH-01) |
| Natureza | Spec de núcleo cognitivo / domínio (Trilha B), camada Harness/operacional **SOBRE** CEM-001 (baseline) — não redefine (CONST-01/CC-02), mesmo padrão arquitetural da SPEC-001 sobre CHM-001 |
| RULE-PD-01 (CC-12) | **Não incide** — CEM-001 é explicitamente neutro de escola/domínio (Princípio 1 — Neutralidade); SPEC-002 não define escopo de especialidade analítica |
| Fronteira | Ver `PROPOSTA-ABERTURA.md` §2 (dentro/fora do escopo) — não altera nesta ata |

---

## 3. Efeitos imediatos desta homologação

1. **SPEC-002 — abertura registrada.** `ROADMAP.md` §26 atualizado: estado de abertura passa de "Indicativo — não aberta" para "Aberta — abertura homologada".
2. **`SPEC-002-SPLIT-001` — resolvida** (não é decisão aberta residual). 1 Spec unificada, conforme §1 acima.
3. **`SPEC-002-VERBATIM-001` — permanece como já decidido em DHR-SPEC002-VERBATIM-001** (Opção A): captura verbatim real das 7 fontes é pré-condição do gate do **Plan**, não desta homologação.
4. **ACH-MEN-01 (achado Menor do parecer do Revisor)** — classificação de tipo de fonte "Teoria" (SRC-03, SRC-06) fora da taxonomia R1 do ROADMAP (Padrão/Prática/Benchmark/Evidência/Experimento/Opinião). Encaminhamento: corrigir a classificação no contexto da redação do Plan; não bloqueia esta homologação.
5. **Próximo gate: o Plan.** O Especificador prossegue para `specs/features/SPEC-002/plan.md` + `checks.md` (skill `tlc-spec-lean`), condicionado a: (a) recaptura verbatim real das 7 fontes (WebFetch operacional — DHR-SPEC002-VERBATIM-001), (b) tratamento de ACH-MEN-01, (c) disparo de RULE-REG-001 (`spec:SPEC-002 em redação` — registrar no `RULES.md` o lote de 10+1 famílias RULE, conforme AGENTS.md §5/ROADMAP). `validate_spec_sot.py` incide nesse gate (não neste).
6. **RMR-001 — nenhum item `ATIVADO`** por este ato (confirmado pelo Revisor, RMR-001 §126). BL-012 (gatilho `spec:SPEC-002 homologada`) dispara apenas na homologação futura do Plan/baseline — não nesta homologação de abertura.
7. **DHR-SPEC002-001 — este documento.** Ata oficial de homologação da abertura. Registrado no histórico de DHRs.
8. Nenhuma decisão aberta fechada (CONS-01): J-001, M-001, H-001, K-001, C-001, G-001, N-001 permanecem abertas — J-001 confirmada como downstream (convicção), não bloqueia a camada de evidência. Nenhum modelo canônico tocado (CONST-01) — CEM-001/CHM-001 permanecem baseline, não reescritos.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
