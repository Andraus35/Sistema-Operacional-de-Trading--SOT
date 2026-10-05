# DHR-AUDIT-SPEC001-001 — Ata — Sessão de auditoria semântica da SPEC-001 (decisões de chat) [ATA-PROPOSTA]

| Campo | Valor |
|---|---|
| De | Controlador (rascunho para assinatura de Andraus — Decisor Final / Consensus Authority) |
| Para | Especificador SOT / Revisor SOT |
| Data | 2026-10-05 |
| Status | **[ATA-PROPOSTA] — NÃO ASSINADA.** Só vale como ata depois que Andraus a adotar. Registra decisões que Andraus tomou em chat nesta sessão (ACH-005 do Revisor: rastreabilidade). **Não homologa** o erratum nem a emenda. |
| Compatibilidade | n/a (ata de registro; nenhuma BASpec, regra ou decisão aberta alterada) |
| Regime | Auditoria ≠ reescrita (D-DHR-PAP-001-01; INV-09). SPEC-001 v1.1 permanece HOMOLOGADA — BASELINE, inalterada. |

## 1. Decisões de Andraus registradas (chat, 2026-10-05) `[FATO: respostas em chat]`
1. Auditoria externa tratada como **DADO**, não como ordem de alteração; verificação própria contra o repositório.
2. **Item 1:** campo novo **`hierarchy_role`** (PRIMARY/SUB); `hypothesis_type` volta ao enum do CHM-001 §2.5. Compatibilidade **Minor**.
3. **Mapeamento produtor → `hypothesis_type`:** adiado; pendência herdada, decidida por Andraus **na abertura** das Specs dos especialistas (Fase 5 — Agentes Analíticos; slots indicativos SPEC-010/011/012, EUA-E21). Regra até lá: o tipo pertence ao enum do CHM-001, sem default e sem mapeamento.
4. **Item 2:** erratum de identidade — o produtor vem da identidade autenticada pelo runtime (RULE-CBP-014), nunca do payload. Compatibilidade do erratum: **Minor**.
5. **Item 3:** declaração global "especificado ≠ implementado ≠ verificado" **no `CATALOGO-OFICIAL.md`**, uma única vez (texto no Anexo A).
6. **Ordem:** erratum primeiro, emenda depois. Baixa do **D-ECC-1** (CIC-001 §4) só **após** homologar o erratum.
7. **CI:** `validate_spec_sot.py` bloqueante para todas as Specs; lint ajustado para aceitar cabeçalho em tabela; `.pyc` fora do controle de versão.

## 2. O que esta ata NÃO faz `[FATO]`
- Não homologa `ERRATUM-SPEC001-002` nem `EMENDA-SPEC001-001` (ambos [PROPOSTA]; parecer do Revisor: CONFORME COM RESSALVAS, 2 rodadas).
- Não insere o Anexo A no CATALOGO, não baixa o D-ECC-1, não altera `SPEC-001/*`, `canon/*` nem `CIC-001`.
- Não fecha nenhuma decisão aberta.

## 3. Permanecem ABERTAS (CONS-01)
**M-001 (enum) · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001** — e a pendência herdada do item 1.3 (valor de `hypothesis_type` por especialista).

## 4. Atos que dependem de Andraus (ordem)
- [ ] Adotar/assinar esta ata.
- [ ] Homologar `ERRATUM-SPEC001-002` (Minor).
- [ ] Inserir o Anexo A no `governance/CATALOGO-OFICIAL.md` (§6) e dar baixa do D-ECC-1.
- [ ] Homologar `EMENDA-SPEC001-001` (Minor), depois do erratum.

---

## Anexo A — Texto pronto para o CATALOGO-OFICIAL (§6 — Registro de Homologação; inserir como bloco próprio, uma vez) `[PROPOSTA]`

> **Status de realização das Specs do Harness (fase spec-first).** Toda Spec homologada do SOT é **especificada** — não **implementada** nem **verificada em runtime**. "HOMOLOGADA — BASELINE" significa que a especificação (BASpecs, EARS, Enforcement Contracts) está congelada e conforme; **não** significa que existe código. Até a fase de implementação: **runtime = NOT IMPLEMENTED**; **conformidade = NOT YET PROVEN** (os cenários `VERIFICADO POR` e os testes de conformidade derivados dos Enforcement Contracts são contratos de teste futuros, ainda não executados). Enforcement declarado (E0–E3) descreve a garantia **exigida**, não uma garantia já **operante**.

Esse texto é o do Item 3 do `ERRATUM-SPEC001-002`; vale para todas as Specs, sem repetição por Spec.

---

**Andraus** *(assinatura pendente)*
