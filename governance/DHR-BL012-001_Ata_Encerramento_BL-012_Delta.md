# DHR-BL012-001 — Ata — Encerramento do BL-012 (MC-COG-001) após reavaliação do delta; BL-017 volta a `Em espera`

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `governance/BL-012-DELTA_PROPOSTA.md` ([PROPOSTA] do Especificador) · DHR-DEC-003 · DHR-BL010-011-012-001 (5 colisões COL-COG-01..05, já homologadas) |
| Data | 2026-10-03 |
| Status | **DECISÕES DIRETAS DE ANDRAUS** (chat): BL-012 → `Absorvido` (com ponteiros); BL-017 → `Em espera`; "dossiê único por análise" → **não criar** |
| Compatibilidade | Minor (só estado de backlog; nenhum canônico tocado) |

---

## 1. Decisões
1. **BL-012 → `Absorvido`**, com ponteiros: removido o que já é norma (17/20 campos do §6 projetam CHM-001/CEM-001/SPEC-001/002/004, RULE-UNC/EPI), o que foi rejeitado (estados §7 → CHM-001, CC-02) e o que pertence a outros donos (§18: RAG→BL-010/SPEC-007; EXP→BL-011/SPEC-006/009; LRN→BL-015; GOV→BL-013/SPEC-018; SKL→BL-016/SPEC-025), o item não retém trabalho de especificação próprio. **Nada apagado** (INV-07). MC-COG-001 segue **referência externa não-normativa**; valor residual = checklist de cobertura cognitiva §31, a conferir quando CDM-001/CNM-001 e as Specs de integração forem redigidas.
2. **Q1 — "dossiê único por análise" (`cognitive_unit_id`): NÃO criar** — duplicaria o Blackboard (SPEC-004) e engessaria o sistema.
3. **Q2 — "ficha do problema" (objective/question/context): ADIADA** ao contrato de decisão (CDM-001/CNM-001, pendentes).
4. **§19 Cognitive Output Contract** → ADIADO a CDM-001/CNM-001. **`confidence`/calibração** → J-001/CCM-001 (**aberta**).
5. **BL-017 → `Em espera`:** a dimensão B "tool correctness" já foi fechada (ERRATUM-SPEC020-001, DHR-SPEC038-002); restam *RAG faithfulness* (SPEC-007) e *decision traceability* (SPEC-014), que só fecham quando esses componentes entrarem em redação. Gatilho recomposto: `spec:SPEC-007 em redação` ∨ `spec:SPEC-014 em redação` (o gatilho `spec:SPEC-038 em redação` foi consumido).

## 2. Permanecem ABERTAS (CONS-01)
**J-001 · N-001 · M-001 (enum) · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001.** Nenhuma fechada por este ato. CONST-01/CC-02 preservados (CEM/CHM/CCM não redefinidos).

## 3. Sincronização efetuada na mesma ordem de Andraus (RESOLVER, chat 2026-10-03)
- **RPSA:** carimbo `sincronizado-até` de `.claude/agents/especificador.md` e `revisor.md` atualizado de `DHR-ECC06-001` para `DHR-SPEC004-002` (+ resumo das atas SPEC-004).
- **`scripts/check_refs.py`:** a janela de cabeçalho do `atomic-spec.md` (onde EUA-E01/E02 são declaradas homologadas) passou de 15 para 20 linhas — a linha 16 ("emendas EUA-E01/EUA-E02") ficava de fora, gerando 2 falsos ERROS. Não houve edição de `atomic-spec.md`/`ROADMAP.md`.

## 4. Registro
- [x] Este documento · [x] `backlog/RMR-001_Painel_Backlog.md` (BL-012, BL-017, notas) · [x] `governance/CATALOGO-OFICIAL.md` · [x] `build_map.py` + `--check`.

---

**Andraus**
