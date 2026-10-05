# DHR-AUDIT-SPEC001-001 — Ata — Sessão de auditoria semântica da SPEC-001 (decisões de chat)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT |
| Data | 2026-10-05 |
| Status | **ORDEM DIRETA DE ANDRAUS** (chat, 2026-10-05: "Assinar a ata… Homologar o erratum e, depois dele, a emenda… Inserir o texto do CATALOGO e dar baixa no D-ECC-1"). Registra as decisões do item 1 e os atos do item 4, **executados** nesta data. |
| Compatibilidade | **Minor** (SPEC-001 v1.1 → v1.2: erratum aditivo + re-homologação pontual `hierarchy_role`; nenhuma decisão aberta fechada) |
| Regime | Auditoria ≠ reescrita (D-DHR-PAP-001-01; INV-09): erratum aditivo (texto original preservado) + re-homologação pontual da emenda; v1.1 preservada em `docs/_legacy/SPEC-001-plan-v1.1.md` e `docs/_legacy/SPEC-001-checks-v1.1.md`. |

## 1. Decisões de Andraus registradas (chat, 2026-10-05) `[FATO: respostas em chat]`
1. Auditoria externa tratada como **DADO**, não como ordem de alteração; verificação própria contra o repositório.
2. **Item 1:** campo novo **`hierarchy_role`** (PRIMARY/SUB); `hypothesis_type` volta ao enum do CHM-001 §2.5. Compatibilidade **Minor**.
3. **Mapeamento produtor → `hypothesis_type`:** adiado; pendência herdada, decidida por Andraus **na abertura** das Specs dos especialistas (Fase 5 — Agentes Analíticos; slots indicativos SPEC-010/011/012, EUA-E21). Regra até lá: o tipo pertence ao enum do CHM-001, sem default e sem mapeamento.
4. **Item 2:** erratum de identidade — o produtor vem da identidade autenticada pelo runtime (RULE-CBP-014), nunca do payload. Compatibilidade do erratum: **Minor**.
5. **Item 3:** declaração global "especificado ≠ implementado ≠ verificado" **no `CATALOGO-OFICIAL.md`**, uma única vez (texto no Anexo A).
6. **Ordem:** erratum primeiro, emenda depois. Baixa do **D-ECC-1** (CIC-001 §4) só **após** homologar o erratum.
7. **CI:** `validate_spec_sot.py` bloqueante para todas as Specs; lint ajustado para aceitar cabeçalho em tabela; `.pyc` fora do controle de versão.

## 2. Atos executados `[FATO]`
- `ERRATUM-SPEC001-002` **homologado e aplicado** (notas aditivas em `SPEC-001/plan.md`; texto original preservado).
- `EMENDA-SPEC001-001` **homologada e aplicada, depois do erratum**: `SPEC-001/plan.md` e `checks.md` → **v1.2** (campo `hierarchy_role`; PRECOND do EC-HH-001 reescrita).
- Declaração global inserida **uma vez** no `governance/CATALOGO-OFICIAL.md` §6 (Anexo A); **D-ECC-1 baixado** no `governance/CIC-001_Inventario_Conformidade.md` §4 quanto à SPEC-001.
- **Não alterados:** `canon/CHM-001`, nenhum outro canon, nenhuma decisão aberta.

## 3. Permanecem ABERTAS (CONS-01)
**M-001 (enum) · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001** — e a pendência herdada do item 1.3 (valor de `hypothesis_type` por especialista; dono: Andraus, na abertura das Specs dos especialistas).

## 4. Atos
- [x] Ata adotada/assinada. · [x] `ERRATUM-SPEC001-002` homologado. · [x] Anexo A inserido no CATALOGO-OFICIAL e D-ECC-1 baixado. · [x] `EMENDA-SPEC001-001` homologada (depois do erratum).

---

## Anexo A — Texto inserido no CATALOGO-OFICIAL (§6 — Registro de Homologação; bloco próprio, uma vez)

> **Status de realização das Specs do Harness (fase spec-first).** Toda Spec homologada do SOT é **especificada** — não **implementada** nem **verificada em runtime**. "HOMOLOGADA — BASELINE" significa que a especificação (BASpecs, EARS, Enforcement Contracts) está congelada e conforme; **não** significa que existe código. Até a fase de implementação: **runtime = NOT IMPLEMENTED**; **conformidade = NOT YET PROVEN** (os cenários `VERIFICADO POR` e os testes de conformidade derivados dos Enforcement Contracts são contratos de teste futuros, ainda não executados). Enforcement declarado (E0–E3) descreve a garantia **exigida**, não uma garantia já **operante**.

Esse texto é o do Item 3 do `ERRATUM-SPEC001-002`; vale para todas as Specs, sem repetição por Spec.

---

**Andraus** *(ordem direta em chat, 2026-10-05)*
