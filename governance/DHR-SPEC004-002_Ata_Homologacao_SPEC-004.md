# DHR-SPEC004-002 — Ata de Homologação — SPEC-004 (Cognitive Blackboard Protocol) v1.1 — BASELINE

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Parecer do Revisor sobre o Plan v1.0: **CONFORME** (2026-10-03; 1 Menor — ACH-004) + re-revisão delta da v1.1: **CONFORME** (sem achados novos) — `specs/features/SPEC-004/plan.md` + `checks.md` |
| Data | 2026-10-03 |
| Status | **HOMOLOGADA — BASELINE v1.1** (instrução direta de Andraus em chat: "Homologar e registrar"). Abertura: DHR-SPEC004-001. |
| Compatibilidade | Minor (não redefine CHM-001/CEM-001/CCM-001; não fecha J-001/N-001/H-001/G-001/WF-D03) |
| Gates determinísticos | `validate_spec_sot.py` PASS 12/12 · `check_repo_research.py` OK · `check_doc_sync.py` ERRO=0 · `build_map.py --check` em dia |

---

## 1. Decisão

**SPEC-004 — Cognitive Blackboard Protocol v1.1 está HOMOLOGADA como BASELINE**:

- **CRITICAL · D0–D7** + rigor adversarial (D8) em escrita concorrente, duplicidade/idempotência e versionamento/supersessão.
- **12 BASpecs (CBP-001..012)**, Classe C/D por BASpec (CC-11); **6 Enforcement Contracts (EC-CBP-001..006)**, **E3 fail-closed** no gate de escrita (cross-workspace e deleção destrutiva).
- **RULE-CBP-001..012 → vigência imediata**; registro físico em `RULES.md` **diferido** (precedente SPEC-002/003; RULE-HG-02).
- **Decisão de Andraus (ACH-004):** atualização **sem `expected_version` é RECUSADA** (fail-closed, `EXPECTED_VERSION_REQUIRED`); criação de objeto novo permanece permitida sem `expected_version`.
- **Fronteiras preservadas:** Event Bus (SPEC-005), Knowledge Graph (SPEC-006), estado por agente (SPEC-009), orquestração (SPEC-008) **fora** do escopo. CRDT = INDETERMINADO (adiado).

## 2. M-001 — decisão PARCIAL de Andraus (CONS-01)

Andraus decidiu (chat, 2026-10-03) a **mecânica** para estados de objetos não-hipótese: **append-only + supersessão** (nada apagado; toda mudança vira nova versão e a anterior fica marcada como substituída), projetando o ciclo do CEM-001. **O enum definitivo de estados de Evidência/Missão/Observação/Convicção permanece ABERTO** (para BUILD ou Spec seguinte). **M-001 não é dada como fechada** e continua listada entre as decisões abertas.

## 3. Achados e tratamento
| ID | Severidade | Tratamento |
|---|---|---|
| ACH-001 / ACH-002 (abertura) | Menor | Corrigidos no Plan (non-load-bearing arXiv; RULE-BB-003 = SUPERSEDED por Q-006) |
| ACH-004 | Menor | Corrigido na v1.1; confirmado pelo Revisor (delta) |
| RES-001 | Risco residual | Verbatim/números de repositório sem web — limite estrutural do Revisor (ENF-03); sem ação |

## 4. Passo 11-bis (RMR-001)
BL-002 (já `Absorvido`) realizado em CBP-012/EC-CBP-002 · **BL-003** → `ATIVADO` (lógico = fronteira SPEC-004; físico → SPEC-006/009, H-001/G-001 abertas) · **BL-029** → `ATIVADO` (proveniência materializada; consumidor→SPEC-014, boundary→SPEC-018/045 pendentes) · **BL-012 e BL-017** seguem ATIVADOS — encaminhamento de Andraus.

## 5. Permanecem ABERTAS
**M-001 (enum)** · **J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001**. Nenhum modelo canônico baseline tocado (CONST-01); nenhuma Spec baselined reescrita (INV-09).

## 6. Registro (efeitos aplicados)
- [x] Este documento · [x] `ROADMAP.md` (linha da SPEC-004, slot do §21, "próximo trabalho") · [x] `governance/CATALOGO-OFICIAL.md` · [x] `backlog/RMR-001_Painel_Backlog.md` (BL-003, BL-029, nota 11-bis) · [x] `build_map.py` + `--check`.
- Próximo da sequência: **SPEC-005** (Event Bus) — **somente com autorização de Andraus** e passo 1-bis do §23.
- Pendência de higiene (RPSA): `.claude/agents/*` com carimbo `sincronizado-até: DHR-SPEC003-001`; atualizar exige emenda de Andraus.

---

**Andraus**
