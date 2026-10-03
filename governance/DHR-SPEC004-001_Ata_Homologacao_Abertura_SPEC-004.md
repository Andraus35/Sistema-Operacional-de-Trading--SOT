# DHR-SPEC004-001 — Ata de Homologação — Abertura da SPEC-004 (Cognitive Blackboard Protocol)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | SPEC-004 — Parecer do Revisor sobre o gate de ABERTURA: **CONFORME** (2026-10-03; 2 Menores não-bloqueantes) — `specs/features/SPEC-004/ABERTURA.md` + `research.md` + `sources/` |
| Data | 2026-10-03 |
| Status | **ABERTURA HOMOLOGADA** (instrução direta de Andraus em chat: "Homologar a abertura") — Dossiê de Pesquisa + Proposta de Abertura. **NÃO é baseline** — o Plan (`plan.md`/`checks.md`, via `tlc-spec-lean`) ainda não foi escrito; é o próximo gate. |
| Compatibilidade | Minor (não toca modelo canônico baselined nem fecha decisão aberta) |

---

## 1. Decisão

A **abertura da SPEC-004 — "Cognitive Blackboard Protocol" está HOMOLOGADA**, com a definição proposta no `ABERTURA.md` e as respostas de Andraus (chat, 2026-10-03):

- **Número SPEC-004 preservado** (slot do ROADMAP §5, FASE 2); **quantidade = 1 Spec**, com fronteiras como propostas: **fora** — Event Bus (SPEC-005), Knowledge Graph (SPEC-006), estado persistente por agente (SPEC-009), orquestração (SPEC-008).
- **Complexidade CRITICAL · profundidade D0–D7** (pin do ROADMAP §5), com rigor adversarial extra nos pontos de maior risco (escrita concorrente, duplicidade, versionamento). Nenhuma elevação de profile em silêncio.
- **Direção para M-001 (orientação ao Plan, NÃO fechamento):** estados de objetos não-hipótese como append-only + supersessão projetando o ciclo do CEM-001 (nada apagado). A decisão final é de Andraus na homologação do Plan.
- **CC-12/RULE-PD-01 não incide** (infraestrutura agnóstica de escola). **RULE-ECC-05 (Multi-Lente) não incide** — confirmado pelo Revisor.
- **Dossiê** com validade de 90 dias (CRITICAL; ECC-VAL-001): limite **2027-01-01**, ou antes se o contexto mudar.

## 2. Efeitos imediatos
1. SPEC-004 passa de "Indicativo — não aberta" para **"Aberta — abertura homologada (DHR-SPEC004-001); Plan pendente"** (ROADMAP).
2. Próximo gate: o Plan (`specs/features/SPEC-004/plan.md` + `checks.md`), com `validate_spec_sot.py` e Autopré-check §7-bis (CRITICAL).
3. Passo 11-bis (gatilhos): BL-029 (dona=SPEC-004), BL-002 e BL-003 disparam `spec:SPEC-004 em redação` quando o Plan iniciar — tratar então. **BL-012 segue ATIVADO** (independente desta abertura; encaminhamento é de Andraus).

## 3. Achados do parecer (corrigir no Plan)
| ID | Severidade | Descrição | Encaminhamento |
|---|---|---|---|
| ACH-001 | Menor | Aviso de método diz que IDs arXiv 2606.* foram descartados, mas SRC-MEM-01 mantém arXiv 2606.24535 com ressalva | Ajustar o aviso ou remover a URL arXiv de SRC-MEM-01 no Plan |
| ACH-002 | Menor | `ABERTURA.md` §4 diz "RULE-BB-003 vigente"; RULES.md a marca [SUPERSEDED por Q-006] | Reformular no Plan: CHM-001 como estados da hipótese (Q-006; RULE-BB-003 superseded) |

Nenhum achado Crítico ou Maior.

## 4. Permanecem ABERTAS (CONS-01)
**M-001** (dona = SPEC-004; só fecha na homologação do Plan) · **J-001 · N-001 · H-001 · G-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001**. Nenhuma fechada por este ato. Nenhum modelo canônico baseline tocado (CONST-01); nenhuma Spec baselined reescrita (INV-09).

## 5. Registro (efeitos aplicados)
- [x] Este documento · [x] `ROADMAP.md` · [x] `governance/CATALOGO-OFICIAL.md` · [x] `backlog/RMR-001_Painel_Backlog.md` (nota) · [x] `python scripts/build_map.py` + `--check`.
- Pendência de higiene (RPSA): `.claude/agents/*` têm carimbo `sincronizado-até: DHR-SPEC003-001`; atualizar exige emenda de Andraus.

---

**Andraus**
