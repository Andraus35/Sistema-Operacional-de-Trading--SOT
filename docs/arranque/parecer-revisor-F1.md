# PARECER DE INTEGRIDADE F.1 — Revisor SOT

**Data:** 2026-09-15
**Emissor:** Agente Revisor de Especificação SOT (independente, somente-leitura)
**Objeto:** Aplicação das 15 decisões do Questionário de Resolução v1 na baseline F.1 + emenda CEE-001 v2.0.
**Registro:** parecer emitido pelo Revisor; correção do achado aplicada pelo Especificador (adendo ao final).

---

## Veredicto original: NÃO CONFORME (1 achado Médio)

### Verificação das 15 decisões — todas CONFORME

| Q | Verificação (arquivo:trecho) | Status |
|---|---|---|
| Q-001 | CHM/CEM BASELINED em `governance/CATALOGO-OFICIAL.md`; CCM/CDM/CNM pendentes | CONFORME |
| Q-002 | 70%/7-9 rotulados "Fase Piloto — recalibrável" em `RULES.md`, `CONSTITUTION.md` | CONFORME |
| Q-003 | §10 (Economia) vs §11 (Sinal) distintos em `CEE-001 v2.0`; RULE-CEE-004 → §11 | CONFORME |
| Q-004 | R:R 1:3 em CONSTITUTION, RULES, `schemas/synthesis.output.json`, `ict.output.json` | CONFORME |
| Q-005 | PRIMARY/SUB em CONSTITUTION; INV-02 nota ICT em ATOMIC-SPEC | CONFORME |
| Q-006 | CHM-001 7 estados em CONSTITUTION; RULE-BB-003 SUPERSEDED em RULES | CONFORME |
| Q-007 | B-001 FECHADA em ATOMIC-SPEC, CATALOGO, GLOSSARIO, especificador.md, revisor.md §8 | CONFORME (exceto A01 — corrigido) |
| Q-008 | 8 dimensões em CONSTITUTION P02, synthesis.spec, synthesis.output.json (required=8) | CONFORME |
| Q-009 | 4Es em CONSTITUTION, CEE-001 §12, GLOSSARIO | CONFORME |
| Q-010 | PPQ supersedido parcial em CATALOGO, revisor.md §2 | CONFORME |
| Q-011 | F.1 BASELINED em CATALOGO | CONFORME |
| Q-012 | PP-SPEC-001 removido; ROADMAP referencia §4 | CONFORME |
| Q-013 | Arquivos em `.claude/agents/`, `scripts/` | CONFORME |
| Q-014 | Equivalências em GLOSSARIO | CONFORME |
| Q-015 | "Sistema Operacional de Trading" em CONSTITUTION, GLOSSARIO | CONFORME |
| CONS-01 | Nenhuma decisão aberta (J/G/H/I/K/L/C/M/N-001) como invariante fechado | CONFORME |

Passos 2 (Invariantes + Salvaguardas), 3 (Constitution Check), 6 (4Es), 8 (Dependências): **PASS**.

### Achados

| ID | Sev. | Local | Constatação | Status |
|---|---|---|---|---|
| **A01** | **Média** | `.claude/agents/revisor.md:167` (§5 Passo 8) | B-001 listada entre bloqueadores abertos, contradizendo Q-007 e o próprio §8:261 | **CORRIGIDO** (ver adendo) |
| A02 | Menor | `canon/CEE-001-...v2.0.md:45` (§2 título "Framework 3E") | Título não renomeado; §12 é autoritativo (4Es) | Mitigado (ponteiro §2→§12 adicionado); não bloqueia |
| A03 | Menor | `.harness-eval/runs/*` | Runs históricas (09/09, 09/11) contêm valores pré-correção | Resíduo histórico não normativo; não bloqueia |

---

## Adendo de correção do Especificador (2026-09-15)

**A01 — RESOLVIDO.** `.claude/agents/revisor.md:167` alterado de
`(J-001, B-001, G-001, H-001, I-001, K-001, L-001, C-001)`
para
`(J-001, G-001, H-001, I-001, K-001, L-001, C-001, M-001, N-001)` + nota "*(B-001 FECHADA — Q-007)*".
Verificação: `grep B-001 .claude/agents/revisor.md` → B-001 aparece apenas como "FECHADA" (linhas 167 e 261). **Condição de nova revisão do Revisor satisfeita.**

**A02** — mitigado: `canon/CEE-001-...v2.0.md` §2 recebeu ponteiro "estendido para 4Es — ver §12". O título original é preservado (redação v1.1); §12 prevalece.

**A03** — registrado como resíduo histórico. `.harness-eval/runs/*` não são normativos e não são consultados como fonte de regra; mantidos (decisão do usuário de não apagar) com esta ressalva.

---

## Passe de confirmação do Revisor (2026-09-15) — VEREDICTO: CONFORME

Re-revisão focada no A01: o Revisor confirmou que `.claude/agents/revisor.md:167` **não lista mais B-001** entre os bloqueadores abertos (lista atual: J-001, G-001, H-001, I-001, K-001, L-001, C-001, M-001, N-001; B-001 apenas como nota "FECHADA"). Condição de nova revisão satisfeita. A02/A03 permanecem menores/não bloqueantes.

> **VEREDICTO FINAL: CONFORME.** Encaminhamento: **pronto para homologação de Andraus como baseline F.1** (Q-011, BLOCO 4). Só após o registro no Catálogo a SPEC-001 arranca.
