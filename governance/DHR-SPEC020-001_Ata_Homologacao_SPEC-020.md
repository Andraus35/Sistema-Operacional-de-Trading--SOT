# DHR-SPEC020-001 — Ata de Homologação — SPEC-020 v1.0 (Harness Evaluation Specification, núcleo A)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Revisor de Especificação do SOT / Controlador |
| Ref | SPEC-020 v1.0 (núcleo A) — Parecer CONFORME de 2026-09-27 (Dossiê + Definição: CONFORME 2026-09-27; Plan/Checks: CONFORME 2026-09-27) |
| Data | 2026-09-27 |
| Status | **HOMOLOGADA — BASELINE** |
| Compatibilidade | Minor |

---

## 1. Decisão

A **SPEC-020 v1.0 (núcleo A) está HOMOLOGADA como baseline.**

O fluxo completo do ROADMAP §23 foi cumprido: (1-bis) abertura por Dossiê de Pesquisa (RULE-ECC-01/02, 1ª aplicação piloto da EUA-E21) com parecer CONFORME do Revisor e homologação da definição por Andraus (Q-A1..Q-A6, 2026-09-27); (2-9) plan.md + checks.md produzidos pelo Especificador, gate determinístico `validate_spec_sot.py` PASS (10/10); (10) parecer semântico do Revisor (Passos 0–8 + 5-bis/EUA-E18) — **CONFORME**, com o ponto crítico CK-02 (RULE-HV não se aplica — SPEC-020 é meta-harness *irmã* de SPEC-019, não filha) confirmado pelo Revisor com argumento técnico próprio.

**Efetivação de SPEC-020-PRINC-001** (decisão aberta incidente): nesta homologação, a consistência principiológica do GPR-001 §15 torna-se **critério constitutivo verificável** — a 9ª lente (BASpec-EV-009, `principle consistency`) entra em vigor como parte do núcleo A da SPEC-020, própria e não integrada às demais lentes (Q-A2).

**Sobre os achados não-bloqueantes:** homologa-se a SPEC-020 v1.0 como está. Os dois achados (um Médio, um Menor) são refinamentos de cobertura adversarial que não afetam a corretude normativa do núcleo A; ficam registrados para emenda futura (§3).

---

## 2. Efeitos imediatos desta homologação

1. **SPEC-020-PRINC-001 — EFETIVA.** A 9ª lente (principle consistency / GPR-001 §15) passa a ser critério constitutivo verificável para as Specs-filhas avaliadas pela SPEC-020, a partir desta data.
2. **RULE-EV-01..07 — FATO NORMATIVO com vigência imediata** (deixam de ser `[PROPOSTA]`). Registro formal em `governance/RULES.md` (nova seção "Regras de Avaliação do Harness — RULE-EV") é passo diferido do Controlador (ver Pendências).
3. **PRINC-BID-001 permanece ABERTA e prospectiva** (BL-022, registrada 2026-09-27) — não retroage sobre esta homologação, conforme decidido por Andraus no mesmo ciclo.
4. **BL-020 (reavaliar acesso web do Revisor após o piloto da EUA-E21)** — gatilho `spec:SPEC-020 homologada` DISPARA por esta homologação. Tratado no passo 11-bis abaixo.
5. **BL-021 (adaptar ferramental à EUA-E21)** — gatilho `spec:SPEC-020 em redação` já havia disparado (achado de `backlog_triggers.py`, tratado separadamente na mesma sessão — ver registro próprio no RMR-001).
6. **DHR-SPEC020-001 — este documento.** Ata oficial de homologação. Registrado no histórico de DHRs (CATALOGO-OFICIAL).

---

## 3. Achados não-bloqueantes registrados para emenda futura

| ID | Severidade | Descrição | Encaminhamento |
|---|---|---|---|
| ACH-SPEC020-M01 | Médio (não-bloqueante, EUA-E18) | §7-bis Bloco A (casos de negação) cobre apenas 5 das 9 BASpecs (EV-003/004/006/007/009); faltam EV-001 (correctness), EV-002 (grounding), EV-005 (context management), EV-008 (robustness) | Emenda futura — adicionar caso de negação explícito para as 4 lentes restantes |
| ACH-SPEC020-m02 | Menor | BASpec-EV-009 (principle consistency) não distingue "checklist §15 aplicado e nada violado" (PASS legítimo) de "spec não toca nenhum princípio PC-xx" (escopo trivial) — gap de observabilidade | Refinamento futuro de BASpec-EV-009 |

---

## 4. Registro do Controlador (efeitos aplicados — 2026-09-27)

Passos 12–14 e 11-bis do gate (§23 do ROADMAP) executados:

- [x] **specs/features/SPEC-020/plan.md** — status atualizado para HOMOLOGADA — BASELINE.
- [x] **ROADMAP.md** — SPEC-020 marcada HOMOLOGADA — BASELINE (Estado atual + §12 + §25); **próximo trabalho autorizado atualizado para SPEC-021**; SPEC-020-PRINC-001 movida para "Decisões FECHADAS".
- [x] **governance/CATALOGO-OFICIAL.md** — entradas atualizadas (Trilha B; linha de status; nova linha DHR-SPEC020-001).
- [x] **RMR-001 (backlog)** — passo 11-bis: gatilho `spec:SPEC-020 homologada` do **BL-020** disparou → **BL-020 promovido `Proposto`→`ATIVADO`**; encaminhamento: avaliar com a evidência do piloto (Dossiê da SPEC-020) se a amostragem de fontes pelo Revisor reduz o risco N5 — fica para decisão de Andraus em ato separado (exigiria emenda EUA ao `tools:` do `revisor.md`); não implementado nesta ata. `BL-017` permanece `Proposto` (dimensões classe B ainda diferidas — gatilhos próprios SPEC-007/014/038 não disparados).

**Pendências abertas (fora deste registro):** registro formal de RULE-EV-01..07 em `governance/RULES.md` (passo editorial diferido); decisão de Andraus sobre BL-020 (ATIVADO, aguarda encaminhamento).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
