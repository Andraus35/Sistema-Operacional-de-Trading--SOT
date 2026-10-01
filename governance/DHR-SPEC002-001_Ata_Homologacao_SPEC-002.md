# DHR-SPEC002-001 — Ata de Homologação — SPEC-002 v1.0 (Evidence & Evidence Provenance Harness)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Revisor de Especificação do SOT / Controlador |
| Ref | SPEC-002 v1.0 — Parecer CONFORME de 2026-09-28 (Dossiê+Definição: CONFORME 2026-09-28; Plan/Checks: CONFORME 2026-09-28) |
| Data | 2026-09-28 |
| Status | **HOMOLOGADA — BASELINE** |
| Compatibilidade | Minor |

---

## 1. Decisão

**A SPEC-002 v1.0 está HOMOLOGADA como baseline.** Primeira Spec de domínio após a conclusão da FASE GOV; primeira produzida sob **atomic-spec v1.5**; primeira sob **RULE-MECH-01** (Classe por BASpec, CC-11) com conformidade total no §7-bis (corrige o gap de cobertura que a SPEC-020 teve).

Fluxo completo cumprido: abertura por Dossiê de Pesquisa (RULE-ECC-01/02/04, com captura verbatim de 6 fontes) — CONFORME; homologação da definição (Q-A1..Q-A7) + registro físico das 11 famílias cognitivas (RULE-REG-001, DHR-REG-001) — 2026-09-28; gate determinístico PASS (11/11); parecer semântico do Revisor — CONFORME (0 Crítico/Médio, 1 Menor não-bloqueante — referência desatualizada a BL-008 no plan.md, já sanada nesta ata; 2 notas informativas).

CEM-001 e CHM-001 (canônicos) **não foram redefinidos** (CC-02) — a Spec constrói exclusivamente sobre eles. RULE-HV (herança vertical) confirmada **não aplicável** (SPEC-002 deriva de modelo canônico, não de macro-spec).

---

## 2. Efeitos imediatos desta homologação

1. **RULE-EH-001..008 — FATO NORMATIVO com vigência imediata.** Registro formal em `governance/RULES.md` (nova seção "Regras de Evidência do Harness — RULE-EH") é passo diferido do Controlador, mesmo padrão da SPEC-020.
2. **Evidence Registry operacional sobre CEM-001 — vigência imediata**, cobrindo provenance, qualidade/força local (≠ Convicção, INV-04), independência, tipologia (favorável/contra/inconclusiva/AUSENTE), detecção-e-registro de conflito (nunca resolução), temporalidade/aging, ciclo de vida.
3. **CC-11 aplicada com sucesso** — 10 BASpecs (EH-001..010) com Classe declarada (D×2, C×5, P×2, H×1), primeira validação prática de RULE-MECH-01.
4. **BL-012 (MC-COG-001) — gatilho `spec:SPEC-002 homologada` DISPARA.** Tratado no passo 11-bis abaixo.
5. **Correção do achado ACH-M01** (parecer do Revisor): referência a `BL-008` no `plan.md`/`checks.md` estava desatualizada (BL-008 já Absorvido antes desta homologação) — nota, não bloqueou o parecer.
6. **DHR-SPEC002-001 — este documento.** Registrado no histórico de DHRs.

---

## 3. Achados registrados (não bloquearam a homologação)

| ID | Descrição | Encaminhamento |
|---|---|---|
| ACH-M01 | Referência desatualizada a `BL-008` (ATIVADO) no plan.md/checks.md — já Absorvido | Registrado; não requer emenda (não é conteúdo normativo) |
| ACH-OBS01 | Autopré-check não declarou execução de `build_map.py --check` (subagente sem Bash) | Confirmado nesta ata (item 4, Controlador) |
| ACH-OBS02 | BL-012 dispara nesta homologação | Tratado no passo 11-bis (item 4 abaixo) |

---

## 4. Registro do Controlador (efeitos aplicados — 2026-09-28)

- [x] `specs/features/SPEC-002/plan.md` — status atualizado para HOMOLOGADA — BASELINE.
- [x] `ROADMAP.md` — SPEC-002 marcada HOMOLOGADA — BASELINE (Estado atual + §4); próximo trabalho autorizado atualizado para **SPEC-003** (Conviction Vector, Evidence Fusion Engine & Conviction Engine — P0 BLOCKER, fecha J-001/N-001).
- [x] `governance/CATALOGO-OFICIAL.md` — entrada atualizada (Trilha B).
- [x] `backlog/RMR-001` — passo 11-bis: gatilho `spec:SPEC-002 homologada` do **BL-012** disparou → **BL-012 promovido `Em espera`→`ATIVADO`**; encaminhamento: mapear COG-SPEC contra N8–N17 aplicando REJEITAR R-05 (usar estados CEM-001/CHM-001, nunca os estados §7 do MC-COG — COL-COG-01/CC-02) — fica pendente de decisão de Andraus, não implementado nesta ata. `BL-002`/`BL-003`/`BL-004`/`BL-017` não disparam (não incluem SPEC-002).
- [x] `python scripts/build_map.py --check`, `check_refs.py`, `check_doc_sync.py`, `backlog_triggers.py`, suíte de testes: revalidados.

**Pendências abertas (fora deste registro):** decisão de Andraus sobre `BL-012` (ATIVADO); registro físico de RULE-EH-001..008 em `RULES.md` (diferido, mesmo padrão da SPEC-020); abertura de SPEC-003 é o próximo passo do fluxo — e é o **bloqueador principal** do ROADMAP (fecha J-001/N-001).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
