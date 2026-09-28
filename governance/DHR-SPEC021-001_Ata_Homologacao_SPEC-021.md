# DHR-SPEC021-001 — Ata de Homologação — SPEC-021 v1.0 (Harness Score / Maturity Model)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Revisor de Especificação do SOT / Controlador |
| Ref | SPEC-021 v1.0 — Parecer CONFORME de 2026-09-28 (Dossiê+Definição: CONFORME 2026-09-27; Plan/Checks: CONFORME 2026-09-28) |
| Data | 2026-09-28 |
| Status | **HOMOLOGADA — BASELINE** |
| Compatibilidade | Minor |

---

## 1. Decisão

A **SPEC-021 v1.0 está HOMOLOGADA como baseline.** Fecha a FASE GOV (SPEC-019 → SPEC-020 núcleo A → SPEC-021, todas homologadas).

Fluxo completo do ROADMAP §23 cumprido: abertura por Dossiê de Pesquisa (research.md, CONFORME 2026-09-27) + homologação da definição (Q-A1..Q-A7, 2026-09-27/28) — incluindo a reconciliação das 3 escadas de maturidade internas divergentes (CONFLITO-1/Q-A2): a escada canônica **por-Spec** é `L0 Declarativo → L1 Especificado → L2 Guiado → L3 Testável → L4 Autocontrolado` (ROADMAP §12), Quality Gates L1–L4 (atomic-spec §7) viram a tabela de critérios por trás dela, e GPR-001 §11 (L0–L5) permanece eixo diferente (maturidade do sistema inteiro, não redefinida) — gate determinístico PASS (11/11) — parecer semântico do Revisor CONFORME (Passos 0–8 + 5-bis/EUA-E18, 4 achados não-bloqueantes) — **checagem de proporcionalidade EUA-E18 Q7 (3ª Spec sob o protocolo) concluída: PROPORCIONAL**, protocolo mantido obrigatório para HIGH/CRITICAL sem mudança.

**Confirmações desta homologação (achados RV-01/RV-02 do parecer):**
- **RV-01 — CONFIRMADO:** o tratamento "D4 numérico N/A não rebaixa nível" na escada de maturidade é aceito como normativo (RULE-MM-04).
- **RV-02 — CONFIRMADO:** a SPEC-021 é meta-harness **irmã** de SPEC-019/SPEC-020 (mede *quão madura* está uma Spec; SPEC-019 governa *como* mudam, SPEC-020 avalia *se* satisfazem critérios) — RULE-HV (herança vertical) **não se aplica**.

---

## 2. Efeitos imediatos desta homologação

1. **RULE-MM-01..07 — FATO NORMATIVO com vigência imediata.** Registradas em `governance/RULES.md`, nova seção "Regras de Maturidade do Harness (RULE-MM)".
2. **Escada canônica por-Spec — vigência imediata.** `L0→L4` (ROADMAP §12) é o modelo normativo de maturidade por componente a partir desta homologação; abaixo do nível-alvo declarado por complexidade = inelegível à homologação (gate E3, RULE-MM-05).
3. **FASE GOV — CONCLUÍDA.** SPEC-019 + SPEC-020 (núcleo A) + SPEC-021, todas HOMOLOGADAS — BASELINE.
4. **Próximo trabalho autorizado — SPEC-002** (retomada do caminho de domínio, ROADMAP §12/§21). Abertura segue o mesmo protocolo (RULE-ECC-01/02, Dossiê de Pesquisa) — e agora também RULE-MECH-01 (Classe por BASpec) e, se aplicável (Spec de especialidade de domínio), RULE-PD-01 (PD-xx), ambas homologadas em 2026-09-27.
5. **DHR-SPEC021-001 — este documento.** Ata oficial de homologação. Registrado no histórico de DHRs.

---

## 3. Achados menores registrados (não bloquearam a homologação)

| ID | Descrição | Encaminhamento |
|---|---|---|
| RV-01 | D4 numérico N/A na escada de maturidade | Confirmado nesta ata (item 1) — RULE-MM-04 vigente |
| RV-02 | RULE-HV não aplicável (irmã, não filha) | Confirmado nesta ata (item 1) |
| RV-03 | Fontes pós-treino no Dossiê (risco residual epistêmico) | Já registrado; limite de processo, não achado corretivo |
| RV-04 | Observação de processo (build_map.py) | Não bloqueante; gate determinístico já confirmou o mapa em dia |

---

## 4. Registro do Controlador (efeitos aplicados — 2026-09-28)

- [x] **specs/features/SPEC-021/plan.md** — status atualizado para HOMOLOGADA — BASELINE.
- [x] **governance/RULES.md** — adicionada a seção "Regras de Maturidade do Harness (RULE-MM)" (RULE-MM-01..07); cabeçalho anotado.
- [x] **ROADMAP.md** — SPEC-021 marcada HOMOLOGADA — BASELINE (Estado atual + §12 + §25); FASE GOV marcada CONCLUÍDA; **próximo trabalho autorizado atualizado para SPEC-002** (abertura via RULE-ECC-01/02).
- [x] **governance/CATALOGO-OFICIAL.md** — nova linha de ata; Trilha B atualizada para SPEC-002.
- [x] **RMR-001 (backlog)** — passo 11-bis: nenhum item novo `ATIVADO` por esta homologação (nenhum gatilho `spec:SPEC-021 homologada` registrado); checagem de proporcionalidade EUA-E18 Q7 confirmada como concluída (PROPORCIONAL) — nota registrada. `BL-020` permanece `ATIVADO` (independente, aguarda decisão de Andraus). `BL-017` permanece `Proposto`.

**Pendências abertas (fora deste registro):** decisão de Andraus sobre `BL-020` (acesso web do Revisor); abertura de SPEC-002 (Dossiê de Pesquisa pelo Especificador, RULE-ECC-01/02) é o próximo passo do fluxo.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
