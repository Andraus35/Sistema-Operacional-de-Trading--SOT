# DHR-SPEC046-003 — Ata de Homologação — SPEC-046 v1.1 (Emenda: Caching Inter-Sessão / CACHE-ISS-001)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador de Especificação do SOT / Revisor / Controlador |
| Ref | SPEC-046 v1.1 — Parecer do Revisor: CONFORME (2026-09-28), 1 achado Menor (ACH-v1.1-01) |
| Data | 2026-09-28 |
| Status | **HOMOLOGADA — BASELINE (v1.1, aditiva a v1.0)** |
| Compatibilidade | Minor (aditiva; INV-07 — v1.0 intacta) |

---

## 1. Decisão

A **emenda v1.1 de SPEC-046 está HOMOLOGADA como baseline**, aditiva à v1.0 (DHR-SPEC046-002). Origem: BL-025 (CACHE-ISS-001, proposta de Andraus) → análise preparatória do Especificador (`backlog/BL-025-CACHE-ISS-001-analise.md`) → recomendação de extensão (não Spec autônoma) → emenda formal (`plan.md`/`checks.md`, v1.0→v1.1) → gate determinístico PASS 11/11 (confirmado independentemente) → parecer do Revisor: **CONFORME**.

**Confirmado nesta homologação:**
- **EC-SPEC046-03** (8 campos) vigente — nível **E3** (reavaliado, não herdado do E2 de EC-SPEC046-01; persistência inter-sessão remove o backstop de releitura intra-sessão), com **ENF-07** (método falso-DENY) declarado substantivamente.
- **BASpecs CISS-001..004** (Classes D/H/C/C) vigentes, mantidas separadas (auditoria independente ENF-03 vs. ENF-04).
- Reuso do hashing SHA-256 já homologado (`scripts/build_map.py:81,341-342`, BL-019) — **verificado no código pelo Revisor**, sem hashing novo.
- Manifesto em `docs/cache/` (não-normativo, análogo a `docs/mapa/`) — INV-09 preservado.
- **L-ISS-01** (RULE-MET-01 — economia de tokens condicionada a substrato de reuso externo, não prometida pelo manifesto isolado) incorporada ao corpo normativo.
- v1.0 (EC-SPEC046-01/02, BASpecs C46-001..004) permanece **intacta** — INV-07.

**ACH-v1.1-01 (Menor) — resolvido nesta ata:** o §7-bis Bloco A não foi explicitamente estendido para CISS-001..004. **Decisão de Andraus: aceito D8-ISS (ADV-CISS-01) + campo VERIFICADO POR de cada BASpec como substituto funcional suficiente** para esta versão — não bloqueia. Se uma futura emenda (v1.2+) tocar essas BASpecs, o §7-bis deve ser estendido explicitamente naquele ato.

---

## 2. Efeitos imediatos

1. `specs/features/SPEC-046/plan.md` — Status do cabeçalho atualizado para v1.1 HOMOLOGADA — BASELINE.
2. RULE-C46-001..005 (v1.0) inalteradas; nenhuma nova RULE global — CISS-001..004 são BASpecs sob o mesmo regime, EC-SPEC046-03 vigente.
3. `backlog/RMR-001_Painel_Backlog.md` — **BL-025 → `Absorvido`** (a extensão foi entregue e homologada; a análise preparatória e a emenda formal cumpriram o propósito do item).
4. Nenhuma decisão aberta fechada (CONS-01); nenhum modelo canônico tocado (CONST-01); SPEC-002 (ordem regular) inalterada.

---

## 3. Registro do Controlador (a aplicar)

- [x] `governance/DHR-SPEC046-003_...md` — este documento.
- [ ] `specs/features/SPEC-046/plan.md` — Status → v1.1 HOMOLOGADA — BASELINE.
- [ ] `backlog/RMR-001_Painel_Backlog.md` — BL-025 → `Absorvido`.
- [ ] `python scripts/check_refs.py` + `python scripts/build_map.py --check`.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
