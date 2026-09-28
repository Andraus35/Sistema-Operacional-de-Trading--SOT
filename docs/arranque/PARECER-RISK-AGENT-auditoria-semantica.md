# PARECER — Auditoria Semântica e Normativa do Risk Agent × repo SOT

| Campo | Valor |
|---|---|
| **Autor** | Claude Code (Especificador/operador) |
| **Data** | 2026-09-22 |
| **Ref** | BRIEFING-CLAUDECODE-RISK-AGENT.md · reference/SOT-RISK-MASTER-001_Consolidado.md · backlog/BL-018-RISK-AGENT-backlog.md |
| **Status** | `[PROPOSTA]` — não-normativo (TRACE-06). Insumo para decisão de Andraus. |
| **Decisões aplicadas** | Andraus 2026-09-22 (C-01,02,03,05,06,07,08,09; C-04 Opção A; INV-RISK-00) |

---

## 1. Achados que corrigiram o enquadramento (1ª passada)

- **F-01 — ARR é fantasma no repo.** `ARR`/`D-ARR-001`/`Agente de Risco-Retorno`: zero ocorrências fora do briefing. Não há componente a superseder. Os parâmetros R:R já vivem como RULE-006/RULE-ICT-002/RULE-SY-003/CEE-001 §11 Salv.5. Portfolio Heat e alavancagem são genuinamente novos. → decisão aberta **RISK-ARR-LOC-001**.
- **F-02 — "Signal Package" é o termo fundacional** (ENGENHARIA-GERAL l.604-606). "TMP" foi introduzido depois. D-RISK-03 restaura, não inventa.
- **F-03 — 11 das 14 camadas herdam N8–N17** (EUA-E05..E14). Delta genuíno = #1 Principiológica, #13 Quantitativa, #14 Risco–Retorno.
- **F-04 — INV-RISK-* duplicam invariantes/RULES existentes** parcialmente → declarar herança (RULE-HV), não recriar. PCO-02/RULE-EPI-01 verificados como existentes.
- **F-05 → RISK-CONV-001** — "convicção de risco" (INV-RISK-02) vs Conviction Vector 8D/J-001.
- **F-06 → CDM-001** — RDR depende do canônico CDM-001 (inexistente).
- **F-07 — Achado E do briefing STALE:** EUA-E17 e SPEC-019 já homologadas; FASE GOV fixa; FASE RISK após FASE 6.
- **INV-05 ≠ P14:** o invariante "SOT não executa; artefato de fronteira" reside em **6 loci** (CONSTITUTION P14 + diagrama · atomic-spec INV-05 §13 · GLOSSARIO l.52 · CHUNK-SY-007 · AGENTS #9 · ROADMAP SPEC-016) — convergência horizontal MAN-001 obrigatória.

## 2. Conflitos/ambiguidades da 2ª passada (Consolidado + BL)

| ID | Tipo | Resolução de Andraus (2026-09-22) |
|---|---|---|
| **C-01** | Colisão de ID — BL-017 já ocupado (dim. B SPEC-020) | Renumerado → **BL-018** |
| **C-02** | Referências penduradas / arquivo na raiz / `reference/` ausente | Consolidado → `reference/`; BL → `backlog/BL-018-...`; parecer persistido (este arquivo) |
| **C-03** | Gap de sequência: P14 citaria Risk Harness inexistente | **EUA-E19a** fatiada — sem "via Risk Harness"; cláusula entra com RISK-SPEC-020 |
| **C-04** | Destino da SPEC-016 | **Opção A — repurposar:** SPEC-016 = contrato de handoff interno Síntese→Risk (TMP snapshot imutável tipado) |
| **C-05** | Namespace P1–P15 colide com CONSTITUTION | **RP1–RP15** |
| **C-06** | R:R sem desambiguação | **"R:R ≥ 1:3 (risco:retorno = 3:1 retorno:risco)"** |
| **C-07** | Numeração/contagem de camadas inconsistente | Unificada pela tabela §3.2: 11 herdam / 3 delta |
| **C-08** | Avaliação duplica SPEC-020 | RISK-SPEC-023 **herda SPEC-020 via RULE-HV**; família 24→**23** specs |
| **C-09** | "supersede ARR" vs "não há supersedação" | Reescrito: **consolida** RULES + **institui** invariantes novos; zero supersedação até RISK-ARR-LOC-001 |

## 3. Nova invariante instituída

**INV-RISK-00 — Isolamento epistêmico** `[FATO ARQUITETURAL — Andraus 2026-09-22]`: pré-condição de todas as RULE-RISK-*. Workspace isolado; input só via handoff tipado imutável do TMP; nunca lê/escreve o Blackboard; Signal Package não realimenta o pipeline. Registrada em: Master §3.6, RISK-SPEC-020, RISK-SPEC-022, SPEC-016 repurposada.

## 4. Forma documental recomendada (aprovada)

**EUA-E19a (restauração semântica — imediata) → EUA-E20 (FASE RISK — após).** Rejeitadas Opção 1 (ampla, risco de Crítico) e Opção 3 sozinha (insuficiente para P14/GES-1).

## 5. Decisões abertas (CONS-01 — não fechar)
D-RISK-SP-001 · **RISK-ARR-LOC-001** · **RISK-CONV-001** · CDM-001 · I-001 · J-001.

---

*Parecer do Claude Code. `[PROPOSTA]` — as decisões de Andraus de 2026-09-22 foram aplicadas aos documentos de referência; nada é baseline até o ciclo Especificador → Revisor → Andraus da EUA-E19a.*
