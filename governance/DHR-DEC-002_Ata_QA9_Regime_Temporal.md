# DHR-DEC-002 — Ata de Decisão — Q-A9 (dimensão do regime de mercado) → dimensão `temporal`

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (delegação à SPEC-003) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Resposta direta de Andraus (chat, 2026-10-01: "Spec decide: temporal + corrigir F-01") à **interpelação I-01** do Revisor (parecer **CONFORME** sobre a SPEC-003 v1.3) |
| Data | 2026-10-01 |
| Status | **DECIDIDA pela SPEC-003 por delegação de Andraus — ratifica na homologação da SPEC-003** (vigência plena no ato de homologação; até lá, decisão candidata registrada) |
| Compatibilidade | Minor no repositório (citações por ID). SPEC-003 v1.3 → v1.4 (delta de decisão + correção F-01, sem renumerar BASpecs). **`WORKFLOW.md` NÃO alterado** (ver §4 — achado para Andraus). |
| Não fecha | Nenhuma decisão aberta além do que §1 registra. **J-001, N-001, M-001, SPEC-015-SCOPE, WF-D03 (residual), D-RISK-SP-001, CDM-001 permanecem ABERTAS** (§2). |

---

## 1. Decisão (Q-A9) — delegada por Andraus à SPEC-003

Na abertura da SPEC-003 (research.md §6-bis / §8.3), Andraus delegou a **Q-A9** à própria Spec: "a SPEC-003 decide em qual das 8 dimensões (fechadas) entra o regime de mercado (WF-C04), usando `research-Q-A9-regime.md` como fonte de dados". Em resposta à interpelação **I-01** do Revisor (parecer CONFORME v1.3), Andraus instruiu em chat: **"Spec decide: temporal + corrigir F-01"**.

**Decisão da SPEC-003 (v1.4):** o **regime de mercado** (tendência / range / alta volatilidade — `WF-C04`) é hospedado na dimensão **`temporal`** do Conviction Vector 8D (**Opção A** de `research-Q-A9-regime.md` §7):

- Regime é **dimensão de convicção, NÃO gate, NÃO veto** (WF-C04) — não habilita/bloqueia sinal por si; gates/veto são exclusivos das Salvaguardas de Sinal (CEE-001 §11) e do Elliott-veto (INV-01).
- **NÃO cria 9ª dimensão** — dimensionalidade = 8 intocada (INV-03/Questionário v1); o regime é uma **feature de contexto hospedada** na `temporal`.
- **NÃO toca o veto estrutural** — **Opção C (estrutural) rejeitada**: mapear regime à estrutural contaminaria o veto de Elliott (INV-01) e duplicaria o sinal de tendência (double-counting; `research-Q-A9-regime.md` §5.1/§6).
- **NÃO é modulador transversal** — **Opção D não adotada** (extrapola o enunciado de WF-C04 "em qual das 8"; só mediante reinterpretação explícita de WF-C04 por Andraus).
- **NÃO entra em custo/sizing** — INV-04 preservado (fluxo unidirecional convicção→risco, WF-X03).
- Regime **em transição / não classificável** → **INDETERMINADO** na dimensão `temporal` (anti-lag), nunca rótulo precoce nem zero (RULE-MET-01).

**Status:** decidida **pela SPEC-003 por delegação de Andraus**; **ratifica na homologação** da SPEC-003. Enquanto não homologada, Q-A9 **não** é escrita como "FECHADA" em nenhum registro (CONS-01).

**Limitação declarada (RULE-MET-01):** a evidência [EXTERNO] de regime-por-dimensão é **Moderada/Fraca** — `research-Q-A9-regime.md` rebaixou SRC-R03 (abstracts; Springer 303 não-fetchada) e SRC-R04 (snippets de WebSearch). A decisão é **arquiteturalmente defensável** (preserva INV-01; evita double-counting; alinha a MTF), **não** forte-empírica.

**Fundamento:** `research-Q-A9-regime.md` (não-normativo, [EXTERNO]) + INV-01 + WF-C04 + INV-03.

---

## 2. Permanecem ABERTAS (CONS-01 — não fechadas por este ato)

| Decisão | Motivo de permanecer aberta |
|---|---|
| **J-001** | Fórmula/pesos/limiares **definitivos** do Conviction Vector — inclui o **peso/limiar do regime** na dimensão `temporal`. Só após backtest. |
| **N-001** | Pesos por ativo (inclui peso do regime por ativo) — manter até o backtest. |
| **M-001** | Estados do Blackboard para objetos não-hipótese — resolve na abertura da SPEC-004. |
| **SPEC-015-SCOPE** | Fronteira/decomposição do Manager — manter aberta. |
| **WF-D03** (residual) | Direção macro×global declarada (WF-C01); nº de invocações fixado (2x, Q-A5/DHR-DEC-001); **dimensão do regime decidida pela SPEC-003** (este ato). **Resíduo aberto = fórmula/pesos/limiares (J-001/N-001)**. Permanece **ABERTA**. |
| **D-RISK-SP-001** | Signal Package / FASE RISK — abre com RISK-SPEC-022. |
| **CDM-001** | Canonical Decision Model — pendente de redação (FASE 6/RDR). |

---

## 3. Efeitos de propagação (aplicados pelo Especificador, 2026-10-01)

- [x] `specs/features/SPEC-003/{plan,checks,research}.md` — **v1.4 candidata**: Q-A9 decidida (regime→`temporal`); RULE-CF-003 estendida; CCM-001 skeleton/I-O (campo de regime na `temporal`, INDETERMINADO se não classificável — nunca zero); CF-004/CF-007/CF-009; EARS #11; D7 CF-T09; D8 ADV-CF-13/14; ADV-CF-12 reformulada; §7-bis (Blocos A/C); **F-01** corrigido (Etiquetagem: Q-A5 ≠ regime); histórico v1.4; lista final. BASpecs **não** renumeradas.
- [x] `ROADMAP.md` — linha "Decisões abertas ativas": WF-D03 residual atualizado (regime decidido pela SPEC-003; resíduo = J-001/N-001). Q-A9 **não** escrita como "FECHADA".
- [x] `governance/CATALOGO-OFICIAL.md` — linha da ata DHR-DEC-002.
- [x] `docs/MATRIZ-WORKFLOW-SPEC.md` — WF-C04 (Q-A9 decidida — temporal); WF-D03 residual; conflito C-3 resolvido.
- [x] `.claude/agents/{especificador,revisor}.md` — `sincronizado-até: DHR-DEC-002` + SYNC-DATE 2026-10-01.

## 4. Achados para Andraus (não aplicados — fora da autoridade do Especificador)

- **`WORKFLOW.md` WF-D03 (descrição) e WF-C04 (nota):** a descrição vigente de WF-D03 cita "em qual das 8 dimensões entra o regime (WF-C04/Q-A9, a cargo da SPEC-003)" como resíduo aberto. Com a decisão deste ato (regime→`temporal`), essa cláusula tornou-se **parcialmente desatualizada** — o resíduo de WF-D03 passa a ser apenas J-001/N-001. **Não aplicado** (edição de `WORKFLOW.md` é exclusiva de Andraus — DHR-WF-001). Registrado para que Andraus ajuste a descrição de WF-D03/WF-C04 na próxima revisão do `WORKFLOW.md`, se desejar, após ratificar a homologação da SPEC-003.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING* (decisão delegada à SPEC-003; ratifica na homologação)
