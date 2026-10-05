# DHR-SPEC006-PEND-001 — Ata — BL-029 `Em espera` e emenda Minor ao `atomic-spec` §3 (Knowledge Graph)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-05 |
| Status | **ORDEM DIRETA DE ANDRAUS** (chat, 2026-10-05: "Resolver decisão 2 e 3 e a seguir mesclar o PR #7"). Resolve duas das três decisões pendentes da abertura da SPEC-006. **Não homologa a abertura da SPEC-006.** |
| Compatibilidade | **Minor** (emenda ao `atomic-spec` §3: reclassificação de um componente na matriz; nenhuma BASpec, regra ou decisão aberta alterada) |
| Regime | Aditivo (INV-07/INV-09): linhas anteriores preservadas como histórico no próprio documento. |

## 1. Decisões `[FATO: ordem direta em chat, 2026-10-05; recomendação do Revisor local da abertura, aceita]`
1. **Decisão 2 — BL-029 → `Em espera`.** Gatilho: `spec:SPEC-014 em redação` ∨ `spec:SPEC-018 em redação` ∨ `spec:SPEC-045 em redação`. O gatilho `spec:SPEC-004 em redação` já foi **consumido** (SPEC-004 homologada). A camada de proveniência (`computed_by`/`gate_record`) segue materializada na SPEC-004 v1.1/v1.2; consumidor → SPEC-014 e *capability boundary* → SPEC-018/045 permanecem pendentes. **Não** marcado `Absorvido` (a lacuna das camadas pendentes existe). Mesmo molde do BL-003 em DHR-ERRATA-001. Registro em `backlog/RMR-001_Painel_Backlog.md` (linha BL-029 e nota); o estado anterior `ATIVADO` fica riscado/preservado.
2. **Decisão 3 — Emenda Minor ao `atomic-spec.md` §3:** Knowledge Graph **MEDIUM · D0–D5 → CRITICAL · D0–D7**, alinhando a matriz ao pin do `ROADMAP.md` §6 (SPEC-006: P0 — CRITICAL, D0–D7) e à reconciliação já adotada para a SPEC-004. A linha anterior (`ICT · Fibonacci · Knowledge Graph | MEDIUM | D0–D5`) fica registrada no cabeçalho do `atomic-spec` e `ICT · Fibonacci` permanece MEDIUM · D0–D5.

## 2. O que este ato NÃO faz `[FATO]`
- **Não homologa a abertura da SPEC-006** (decisão 1): segue **proposta** (`specs/features/SPEC-006/`, PR #7). Não há `plan.md`. Mesclar o PR #7 apenas coloca a proposta na `main`.
- Não altera `ROADMAP.md`, `canon/*`, nenhuma Spec baselined nem decisão aberta.

## 3. Itens de acompanhamento identificados `[FATO — fora do escopo autorizado; não tratados]`
- **Espelho da matriz fora do documento:** `.claude/skills/SKILL.md` (l.178) ainda lista "Knowledge Graph (EC-COG-003) | MEDIUM | D0-D5". Fica **divergente** do `atomic-spec` §3 até a skill ser sincronizada (ato do Controlador/Andraus; não editado aqui).
- **Carimbo RPSA dos agentes** (`sincronizado-até`): `.claude/agents/especificador.md` e `revisor.md` seguem em `DHR-ERRATA-001`; não foram avançados para as atas posteriores (DHR-AUDIT-SPEC001-001, DHR-AUDITOR-EXTERNO-001 e esta). Atualização é ato do Controlador.

## 4. Permanecem ABERTAS (CONS-01)
**H-001 · G-001 · M-001 · J-001 · N-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001** e a pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.**

## 5. Registro
- [x] Esta ata · [x] `atomic-spec.md` §3 + cabeçalho · [x] `backlog/RMR-001_Painel_Backlog.md` (BL-029 + nota) · [x] `governance/CATALOGO-OFICIAL.md` · [x] `build_map.py` + `--check` · [ ] homologação da abertura da SPEC-006 — **ato de Andraus, pendente**.

---

**Andraus** *(ordem direta em chat, 2026-10-05)*
