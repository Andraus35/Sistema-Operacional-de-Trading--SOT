# DHR-PAP-001-A — Adendo de Re-Homologação do PE-PR-PAP-001 v1.1

**Declaração formal de re-homologação por Andraus. Produz efeito normativo imediato. Adendo ao DHR-PAP-001.**

| Campo | Valor |
|---|---|
| ID | DHR-PAP-001-A |
| Versão | 1.0 — BASELINE HOMOLOGADA |
| Adendo a | DHR-PAP-001 (2026-09-15) |
| Objeto | PE-PR-PAP-001 v1.1 (EMENDA — errata de rastreabilidade) |
| Autoridade homologadora | Andraus (Decisor Final / Consensus Authority do SOT) |
| Data | 2026-09-15 |
| Registrado por | Revisor de Especificação (registro de ato declarado por Andraus) |

---

## 1. Declaração de Re-Homologação

Andraus, na qualidade de Decisor Final e única autoridade de homologação do SOT, declara em 2026-09-15:

> **"Re-homologo."**

O **PE-PR-PAP-001 v1.1** passa imediatamente de EMENDA (Proposta) ao status **HOMOLOGADO — BASELINE**. A v1.0 (homologada por DHR-PAP-001) fica supersedida por esta v1.1, sem deleção (INV-07) — o §0 do PE-PR-PAP-001 preserva o registro histórico.

---

## 2. O que esta re-homologação corrige (rastreabilidade — não altera cláusula prescritiva)

O PE-PR-PAP-001 v1.1 corrigiu **apenas** a camada de rastreabilidade (tabelas de contexto obrigatório e autoridade normativa). Missão, escopo dos 6 blocos, invariantes, decisões abertas K-PAP-001..005 e contrato de saída permanecem **inalterados**.

| Item | v1.0 (supersedido) | v1.1 (homologado) |
|---|---|---|
| S-01 | Unidade Atômica v1.2 em `claude/UnidadeAtomica…` | `atomic-spec.md` (raiz) — **v1.3** |
| S-02 | Road Map em `claude/ROADMAP_SOT…` | `roadmap.md` / `ROADMAP.md` (raiz) |
| S-03 | PEP-001 v1.2 (arquivo implícito `claude/…`) | embutido em `.claude/agents/especificador.md` |
| S-04 | PRE-001 v1.1 em `claude/PRE-001…` | embutido em `.claude/agents/revisor.md` |
| S-05 | HRE-001 v2.1 em `claude/HRE-001…` | embutido em `.claude/agents/revisor.md` — **v2.2** |
| S-06 | GRE-001 v2.1 em `claude/GRE-001…` | embutido em `.claude/agents/revisor.md` — **v2.2** |
| S-07 | GEH-001 em `claude/GEH-001…` (ausente/inferência CEE-001) | `RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md` (raiz) — **v1.1** |

---

## 3. Decisão K-PEPR-001 — RESOLVIDA

**Questão:** localização canônica de GEH-001, citado como autoridade normativa mas ausente do repositório.

**Resolução (Andraus, 2026-09-15):**
- GEH-001 **v1.1** é a versão canônica (superset: corpo generalista + apêndice §13 da edição Claude Code; corpo inalterado em relação à v1.0).
- Localização canônica no repo: `RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md` (bate com a designação de `docs/arranque/questionario-resolucao-v1.md:38,197,362`).
- Cópia verificada (432 linhas, íntegra), trazida de `../GEH-001_…md`.
- A referência `DHR-PAP-001:117` ("GEH-001 — inalterado") lê-se, a partir de agora, como **v1.1 canônica** — a diferença v1.0→v1.1 é exclusivamente o apêndice §13, sem impacto nas seções citadas pela governança (§3/§6.1/§6.4/§7/§10, ETCLOVG).
- **[FATO]** CEE-001:340 apenas cita GEH-001 §3 — não o substitui. A inferência inicial (GEH-001→CEE-001) fica formalmente refutada e arquivada.

---

## 4. Efeito imediato

- **PE-PR-PAP-001 v1.1** → HOMOLOGADO — BASELINE. Os Blocos A e B tornam-se os prompts operacionais vigentes.
- A skill `sot-especificador-pap001` (`.claude/skills/sot-especificador-pap001/SKILL.md`), que operacionaliza o Bloco A, fica **liberada para acionamento** — Bloqueio 2 (aderência de papel) eliminado nativamente, pois a skill descreve o PAP-001 como Protocolo de Governança (não BASpec).
- **M1-PRE** permanece: próximo entregável é o **PAP-001 — A PRODUZIR** (Especificador via skill → Revisor via Bloco B → homologação de Andraus).

Sequência autorizada a partir de agora:
1. Especificador produz o PAP-001 (skill `sot-especificador-pap001`)
2. Revisor audita o PAP-001 (Bloco B do PE-PR-PAP-001 v1.1)
3. Andraus homologa o PAP-001 (resolve K-PAP-001..005)
4. SPEC-001 pode ser homologado (pós PAP-001 homologado)

---

## 5. Não-Regressão

Esta re-homologação não altera nenhum outro documento baselined. GPR-001 v1.0, PP-PAP-001 v1.0, atomic-spec v1.3, CONSTITUTION, RULES, CONFLICT-MAP — inalterados. As decisões abertas K-PAP-001..005 e J-001..L-001 permanecem abertas.

---

*Fim do DHR-PAP-001-A v1.0. Ato declarado por Andraus em 2026-09-15. Registrado pelo Revisor de Especificação. Adendo a DHR-PAP-001.*
