# DHR-EUA-E19a — Ata de Homologação — Restauração Semântica do Signal Package

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador / Revisor / Controlador |
| Ref | EUA-E19a — parecer Revisor CONFORME (2026-09-22) |
| Data | 2026-09-22 |
| Status | **HOMOLOGADA — BASELINE** |
| Compatibilidade | Minor (semântica; nenhum objeto deletado — INV-07) |

---

## 1. Decisão

A **EUA-E19a está HOMOLOGADA como baseline.** Parecer do Revisor CONFORME (8 passos PASS; nenhum achado Crítico ou Médio bloqueante). Acesso ao RULES.md vigente confirmado (M-02). Achados M-001 (§7-bis ausente), m-002 (threshold INV-RISK-LEV), m-003 (ENF-07) tratados como **delta editorial** nesta homologação, por decisão de Andraus, sem reabrir o ciclo.

**Precedente de método (K-E19a-01 = Opção A):** uma **EUA é veículo válido para emendar invariantes INV-*/princípios P-*** homologados, desde que percorra o trio completo com Constitution Check obrigatório (RULE-HG-01/HG-06) e homologação de Andraus (RULE-HG-03). Este é o **primeiro caso** de emenda de invariante existente no harness — precedente aberto e transparente.

---

## 2. Efeitos imediatos (aplicados pelo Controlador, 2026-09-22)

1. **P14 / INV-05 emendados** — texto novo: *"O SOT não executa ordem; produz um Signal Package para o Bot Trade Finance. O TMP é artefato interno de passagem entre a Síntese e o Risk Agent."* Aplicado aos **6 loci** (convergência horizontal MAN-001):
   - [x] L1 `governance/CONSTITUTION.md` P14 + diagrama de pipeline
   - [x] L2 `atomic-spec.md` INV-05 §13
   - [x] L3 `GLOSSARIO.md` (TMP reclassificado interno; nova entrada "Signal Package"; seção §3-bis Terminologia Concorrente)
   - [x] L4 `rag/synthesis.knowledge.md` CHUNK-SY-007
   - [x] L5 `AGENTS.md` não-negociável #9
   - [x] L6 `ROADMAP.md` SPEC-016 — já convergente (repurposada, C-04)
2. **Terminologia concorrente TMP↔Signal Package** registrada no GLOSSARIO §3-bis (RULE-SEM/MSC-001, CC-10). "TMP" **não deletado** (INV-07) — muda de papel.
3. **Invariantes de risco registrados** em `atomic-spec.md` §13: **INV-RISK-RR** (consolidação de R:R ≥ 1:3 = 3:1 retorno:risco), **INV-RISK-HEAT** (Portfolio Heat ≤ 15%, novo), **INV-RISK-LEV** (alavancagem dinâmica, novo; threshold diferido — m-002). **Zero supersedação do ARR** (RISK-ARR-LOC-001 aberta).
4. **Restrição C-03 honrada:** nenhum locus menciona "Risk Harness"; a cláusula "via Risk Harness" entra em P14/INV-05 apenas quando **RISK-SPEC-020** for homologada.
5. **m-001 corrigido:** `ROADMAP.md` — RISK-ARR-LOC-001 permanece **ABERTA** (removida a anotação incorreta "fecha na EUA-E19a").
6. **RMR-001:** **BL-018 → `Em espera`** (parcial — ativação plena aguarda `milestone:FASE 6 concluída`).

---

## 3. Decisões que permanecem ABERTAS (CONS-01 — não fechadas por esta ata)
RISK-ARR-LOC-001 · RISK-CONV-001 · D-RISK-SP-001 · CDM-001 · I-001 · J-001.

---

## 4. Próximo passo
A **EUA-E20** (institui a FASE RISK, após a FASE 6) permanece futura. O trabalho autorizado do caminho crítico segue inalterado: **SPEC-020 — núcleo A** (FASE GOV). A família RISK-SPEC (BL-018) só entra em redação quando o gatilho composto `EUA-E19a homologada ∧ FASE 6 concluída` disparar — a primeira condição está agora satisfeita.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
