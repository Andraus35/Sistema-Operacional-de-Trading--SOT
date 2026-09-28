# DHR-SPEC046-002 — Ata de Homologação — SPEC-046 v1.0 (Spec-Time Context Caching Harness — Especificador/Revisor)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador de Especificação do SOT / Revisor / Controlador |
| Ref | SPEC-046 v1.0 — Abertura: CONFORME (DHR-SPEC046-001, 2026-09-28) · Plan/Checks: CONFORME (parecer do Revisor, 2026-09-28) |
| Data | 2026-09-28 |
| Status | **HOMOLOGADA — BASELINE** |
| Compatibilidade | Minor (linha paralela; não toca modelo canônico nem decisão aberta; não altera SPEC-002) |

---

## 1. Decisão

A **SPEC-046 v1.0 está HOMOLOGADA como baseline.** Fluxo completo cumprido: RPIR (`reference/externo/CACHING SOT.MD`) → parecer de auditoria do Revisor sobre a proposta original (ACHADO-C1/M1/M2) → BL-024 → decisão de Andraus de abrir Spec dedicada, fora de ordem, restrita ao Grupo B → Dossiê de Pesquisa + Proposta de Abertura (RULE-ECC-01/02, 7 fontes `[EXTERNO]`, captura verbatim RULE-ECC-04) → parecer do Revisor sobre a abertura: **CONFORME** (2 achados Menores) → **DHR-SPEC046-001** (homologação da abertura) → Plan (`plan.md`/`checks.md`, sanando os achados da abertura) → gate determinístico `validate_spec_sot.py`: **PASS 11/11** → parecer do Revisor sobre o Plan (protocolo semântico completo GRE-001/HRE-001, Passos 1-8 + 5-bis adversarial/herança): **CONFORME** (3 achados Menores, nenhum bloqueante) → esta homologação.

**Confirmações desta homologação:**
- Escopo permanece restrito ao **Grupo B** (Especificador/Revisor, caching de spec-time) — Grupo A explicitamente fora de escopo, candidato a futura SPEC-047.
- **EC-SPEC046-01** (8 campos, precondição de freshness por hash SHA-256/mtime/commit git, fail-closed) e **EC-SPEC046-02** (E1, auditoria de higiene) — vigentes.
- 4 BASpecs (C46-001..004) com Classe declarada sob RULE-MECH-01..04: D, H, P, D — nenhuma Classe C proposta (coerente com nível de risco E2).
- **Nota de proporcionalidade EUA-E18** (3ª Spec sob o protocolo §5-bis, fecha a rodada de verificação): avaliado como PROPORCIONAL pelo Revisor — protocolo mantido sem alteração.
- SPEC-002 (próximo trabalho da ordem regular) **não é afetada, adiada nem bloqueada** por esta homologação — SPEC-046 permanece linha paralela (ROADMAP §25-bis).

---

## 2. Efeitos imediatos desta homologação

1. **SPEC-046 v1.0 — BASELINE.** `specs/features/SPEC-046/plan.md` (Status atualizado), `checks.md`, `research.md`, `DOSSIE-PESQUISA.md`, `PROPOSTA-ABERTURA.md`, `sources/SRC-01..07.txt` — todos baseline.
2. **RULE-C46-001..005 — de `[PROPOSTA]` para FATO NORMATIVO com vigência imediata**, restritas ao escopo Grupo B (spec-time, Especificador/Revisor).
3. **EC-SPEC046-01/02 — Enforcement Contracts vigentes.** Precondição de freshness (hash/mtime/commit) passa a reger citações `[FONTE]` de documentos-fonte do repositório pelo Especificador e pelo Revisor.
4. **ROADMAP.md** — SPEC-046 marcada HOMOLOGADA — BASELINE em §Estado atual, §25-bis e §26. SPEC-002 permanece "Próximo trabalho autorizado" (ordem regular, inalterada).
5. **`governance/CATALOGO-OFICIAL.md`** — Trilha B atualizada.
6. **BL-024 (RMR-001)** — passa a `Absorvido` (a abertura+baseline do Grupo B foi integralmente entregue; o item cumpriu seu propósito — Grupo A permanece como trabalho futuro, sem número, não coberto por este item).
7. **BL-025 (RMR-001)** — gatilho `spec:SPEC-046 homologada` **DISPARA** com este ato. BL-025 estava em `Proposto` (nunca promovido a `Em espera` — RMR-001 §5 exige homologação de Andraus para essa promoção). **Não promovido automaticamente nesta ata** — fica como achado de gate para decisão de Andraus (ver §3).
8. **DHR-SPEC046-002 — este documento.** Ata oficial de homologação de baseline. Registrado no histórico de DHRs.

---

## 3. Achados do parecer (Plan) — encaminhamento

| ID | Severidade | Descrição | Encaminhamento |
|---|---|---|---|
| ACH-MEN-03 | Menor | `research.md` e `DOSSIE-PESQUISA.md` se sobrepõem (risco de drift futuro) | **Diferido** — tarefa de manutenção; não bloqueia baseline |
| ACH-MEN-04 | Menor | `build_map.py --check` não declarado nos artefatos | **Sanado nesta ata** — confirmado "Mapa em dia" (176 documentos) antes da homologação |
| ACH-MEN-05 | Menor | Exemplo de hash no D4 é SHA-1 (40 chars) rotulado "truncado" de SHA-256 (64 chars) — cosmético | **Diferido** — tarefa de manutenção; não bloqueia baseline |
| ACH-OBS-01 | Observação (pré-existente, herdada da ata de abertura) | BL-008 permanece `ATIVADO` desde DHR-EUA-E15 (2026-09-21) | **Não resolvido nesta ata** — pré-existente e independente de SPEC-046. Permanece pendente de Andraus. |
| — (novo, desta ata) | Achado de gate | BL-025 (CACHE-ISS-001) tem gatilho `spec:SPEC-046 homologada` que dispara com este ato, mas o item está em `Proposto`, não `Em espera` — RMR-001 §5 exige homologação de Andraus para essa promoção | Registrado nesta ata; promoção `Proposto→Em espera`/`ATIVADO` é decisão separada de Andraus, não implícita nesta homologação de SPEC-046 |

Nenhum achado Crítico ou Médio. Nenhuma decisão aberta (J-001, M-001, ECC-VAL-001 etc.) fechada por este ato — CONS-01 preservado. Nenhum modelo canônico baseline tocado — CONST-01 preservado.

---

## 4. Registro do Controlador (efeitos aplicados — 2026-09-28)

- [x] `governance/DHR-SPEC046-002_...md` — este documento.
- [x] `specs/features/SPEC-046/plan.md` — Status atualizado para HOMOLOGADA — BASELINE.
- [x] `ROADMAP.md` — SPEC-046 marcada HOMOLOGADA — BASELINE (§25-bis + §26); SPEC-002 confirmada inalterada como próximo trabalho da ordem regular.
- [x] `governance/CATALOGO-OFICIAL.md` — Trilha B atualizada.
- [x] `backlog/RMR-001_Painel_Backlog.md` — BL-024 → `Absorvido`; BL-025 com nota de gatilho disparado (achado de gate, promoção pendente de decisão explícita de Andraus).
- [x] `python scripts/check_refs.py` + `python scripts/build_map.py --check` — a rodar após as edições acima.

**Pendências abertas (fora deste registro):** confirmação de status de BL-008 (ACH-OBS-01); decisão de Andraus sobre promover BL-025 (`Proposto`→`Em espera`) e, se sim, acionar o Especificador para a análise de viabilidade técnica de CACHE-ISS-001; abertura futura do Grupo A (SPEC-047, sem número atribuído).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
