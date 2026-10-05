# DHR-ERRATA-001 — Ata — Errata aditivas (SPEC-001 âncora SAS-001; SPEC-005 estado do BL-008) e encaminhamento do BL-003

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Data | 2026-10-05 |
| Status | **ORDEM DIRETA DE ANDRAUS** (chat: "resolver"; BL-003 → "Voltar a Em espera, gatilho SPEC-006/009") |
| Compatibilidade | **Patch** (errata de citação/estado; nenhuma BASpec, regra ou decisão aberta alterada) |

## 1. Decisões e efeitos
1. **ERRATUM-SPEC001-001** (`governance/ERRATUM-SPEC001-001_Ancora_SAS-001_6.10.md`): `SPEC-001/plan.md` l.75 cita SAS-001 §6.7 (Cognitive Budget) para metadados de transporte; a âncora correta é **§6.10** (§6.9 = integração com o Event Bus) — achado A-CK-09 do Revisor (SPEC-005). Nota aditiva inserida em `SPEC-001/plan.md`; texto original **não** alterado (INV-09).
2. **ERRATUM-SPEC005-001** (`governance/ERRATUM-SPEC005-001_Estado_BL-008.md`): **BL-008 já era `Absorvido`** (DHR-BL008-001, 2026-09-28; painel RMR-001 l.107). A menção "BL-008 ATIVADO" nos documentos da SPEC-005 e em notas do orquestrador/atas DHR-SPEC005-001/002 vinha de uma nota histórica anterior à absorção — corrigida por errata aditiva (nota em `SPEC-005/plan.md`); itens `ATIVADO` reais: **BL-003** (agora devolvido, ver 3) e **BL-029**.
3. **BL-003 → `Em espera`** (decisão de Andraus): a camada **lógica** da persistência está definida na SPEC-004 (fronteira); a **física** depende de H-001 (SPEC-006) e G-001 (SPEC-009), **ABERTAS**. Gatilho reposto: `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação` (o gatilho `spec:SPEC-004 em redação` foi consumido). **Não** marcado `Absorvido` (a lacuna física continua existindo). BL-029 permanece `ATIVADO` (camada Blackboard materializada na SPEC-004; consumidor→SPEC-014, boundary→SPEC-018/045 pendentes).

## 2. Permanecem ABERTAS (CONS-01)
**M-001 (enum) · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001.** Nenhuma fechada por este ato.

## 3. Registro
- [x] Este documento · [x] 2 erratas · [x] notas aditivas em `SPEC-001/plan.md` e `SPEC-005/plan.md` · [x] `backlog/RMR-001_Painel_Backlog.md` (BL-003, notas) · [x] `governance/CATALOGO-OFICIAL.md` · [x] carimbo RPSA dos agentes → `DHR-ERRATA-001` · [x] `build_map.py` + `--check`.

---

**Andraus**
