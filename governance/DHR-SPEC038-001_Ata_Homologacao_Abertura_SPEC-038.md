# DHR-SPEC038-001 — Ata de Homologação — Abertura da SPEC-038 (Trading Analysis Tool Harness)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | SPEC-038 — Parecer do Revisor sobre o gate de ABERTURA: **CONFORME** (2026-10-03, reauditoria pós-DHR-DEC-003; 1 Menor não-bloqueante) — `specs/features/SPEC-038/ABERTURA.md` + `research.md` + `sources/` |
| Data | 2026-10-03 |
| Status | **ABERTURA HOMOLOGADA** (instrução direta de Andraus em chat: "Homologar") — Dossiê de Pesquisa + Proposta de Abertura. **NÃO é baseline** — o Plan (`plan.md`/`checks.md`, via `tlc-spec-lean`) ainda não foi escrito; é o próximo gate. |
| Compatibilidade | Minor (não toca modelo canônico baselined nem fecha decisão aberta) |

---

## 1. Decisão

A **abertura da SPEC-038 — "Trading Analysis Tool Harness" está HOMOLOGADA**, com a definição proposta no `ABERTURA.md`:

- **Número SPEC-038 preservado** (slot do ROADMAP §17, FASE 12); **quantidade = 1 Spec** (SPEC-038-SPLIT-001 resolvida na abertura).
- **Complexidade HIGH · profundidade D0–D7 · profile standard** (D8 não pinado; nenhuma elevação em silêncio).
- **Classe predominante (orientação): D + C**; declaração normativa por BASpec no Plan (CC-11). **CC-12/RULE-PD-01 não incide** (harness de ferramentas agnóstico de escola).
- **Contrato por ferramenta:** `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas`. Dado de ferramenta = **Observação**, não Evidência (INV-06/CEM-001); nunca ordem (INV-05).
- **Fronteiras:** SPEC-038 = contrato de ferramenta · SPEC-039 = seleção/governança/tool poisoning/fallback · SPEC-042 = guardrails runtime · SPEC-044 = alucinação · backtest/calibração = SPEC-018 (BL-032, DHR-DEC-003).
- **Perfil exploratório supervisionado por humano** (canal CDP, DHR-DEC-003 §1.1): requisitos de abertura levados ao Plan como proposta; **risco de Termos de Uso do TradingView assumido por Andraus**; esta homologação **não** afirma conformidade jurídica nem torna o canal fonte de decisão.
- **Dossiê** com validade de 90 dias (HIGH; ECC-VAL-001): limite **2026-12-31**, ou antes se o TradingView responder sobre uso não-display via MCP.

Abertura em **linha paralela** à SPEC-004 (caminho crítico), autorizada por Andraus em 2026-10-02; **não substitui nem adia a SPEC-004**.

## 2. Efeitos imediatos
1. SPEC-038 passa de "Indicativo — não aberta" para **"Aberta — abertura homologada (DHR-SPEC038-001); Plan pendente"** (ROADMAP).
2. Próximo gate: o Plan (`specs/features/SPEC-038/plan.md` + `checks.md`), com `validate_spec_sot.py` e Autopré-check §7-bis (HIGH).
3. BL-031 já `Absorvido` (DHR-DEC-003). BL-017 (tool correctness ↔ SPEC-038) **permanece como está**: promoção a ATIVADO é ato separado de Andraus; a dimensão B da SPEC-020 só fecha por emenda na **homologação da SPEC-038** (não na abertura — CONS-01).

## 3. Achado do parecer
| ID | Severidade | Descrição | Encaminhamento |
|---|---|---|---|
| ACH-MEN-NEW-01 | Menor | `SRC-WORKFLOW-01` é captura de 2ª ordem (via PESQUISA-WORKFLOW B.7); declarada honestamente no arquivo | Sem ação bloqueante; re-fetch das URLs primárias quando o Dossiê for reaberto |

Nenhum achado Crítico ou Maior.

## 4. Permanecem ABERTAS (CONS-01)
**SPEC-038-DATASRC-001** (fonte de dado de decisão — aguardar TradingView; Andraus envia a pergunta do `research.md` §4-bis.3) · **J-001 · N-001 · M-001 · H-001 · WF-D03 (residual) · ECC-03-001**. Nenhuma fechada por este ato. Nenhum modelo canônico baseline tocado (CONST-01); nenhuma Spec baselined reescrita (INV-09).

## 5. Registro (efeitos aplicados)
- [x] Este documento · [x] `ROADMAP.md` (estado do slot, linha de próximo trabalho) · [x] `governance/CATALOGO-OFICIAL.md` · [x] `backlog/RMR-001_Painel_Backlog.md` (nota) · [x] `python scripts/build_map.py` + `--check`.
- Pendência de higiene (RPSA): `.claude/agents/*` têm carimbo `sincronizado-até: DHR-SPEC003-001`; atualizar exige emenda de Andraus (agentes não editam seus próprios arquivos).

---

**Andraus**
