# AUDITORIA DE HIGIENE DAS SPECS — 2026-10-01

| Campo | Valor |
|---|---|
| Natureza | **NÃO-NORMATIVA · AUDITORIA.** Não abre Spec, não promove item, não fecha decisão, não é baseline (INV-09). Achados são matéria de auditoria do Revisor; encaminhamento é de Andraus. |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Origem | Instrução direta de Andraus (chat, 2026-10-01), Frente 4 |
| Escopo | Slots do `ROADMAP.md` + `specs/features/*` + termos legados vivos + conflitos com ADRs/CEM/CHM. Varredura de sobreposição de escopo, duplicação de mecanismo, ambiguidade de dono. |
| Regra de ação | Cada achado marcado **[APLICÁVEL]** (propagação de decisão já homologada — aplicação mínima) ou **[PROPOSTA]** (decisão de Andraus). Baselined só por DIV/governança (CONST-01). |

---

## 0. Resumo executivo

A higiene das Specs está **majoritariamente boa** (a FASE GOV e SPEC-001/002 estão limpas). Os focos de drift concentram-se em **três clusters de orquestração/síntese** e em **termos legados em documentos baselined**:

1. **Manager** disperso/sub-decomposto por nome legado (SPEC-008/014/015) — tratado por **EUA-E23 v2** (quantidade) + **DHR-ARQ-001/002** (Conviction/Synthesis absorvidos). [parcialmente APLICADO]
2. **Termos legados vivos em canon baselined** (CEE-001, SAS-001, PPQ-001): "Mission Engine", "Master Orchestrator", "Conviction Engine", "FCE" sem anotação DIV de supersedação. [PROPOSTA — sweep por ata, molde DHR-TAX-001]
3. **Ambiguidades de dono** entre Manager-Dispatch × Cognitive Orchestrator (SPEC-023); memórias (004/006/009/017); regime (SPEC-003 Q-A9 × skills SPEC-036/037); Skills × agentes. [PROPOSTA — fronteira na abertura de cada Spec]

Nenhum achado é **Crítico bloqueante** do próximo trabalho (SPEC-003). Os Críticos de taxonomia já foram resolvidos por ADR-MANAGER-001/DHR-ARQ-001/DHR-ARQ-002.

---

## 1. Achados — sobreposição de escopo entre slots

| # | Achado | Severidade | Arquivos:linha | Correção proposta | Classe |
|---|---|---|---|---|---|
| **H-01** | **Manager dividido entre SPEC-008 (Scheduler) e SPEC-015 (Mission)**, nenhum o nomeia como ator único; ADR §4.2 manda SPEC-015 conter dispatch (colide com SPEC-008). | Média | `ROADMAP.md` §7/§9; `MATRIZ-WORKFLOW-SPEC.md` C-1; `ADR-MANAGER-001` §4.2/§7 | Decompor por natureza (2 ou 3 Specs) sob "Manager Contract" — **EUA-E23 v2** (recomenda 3). Fronteira só na abertura (RULE-ECC-01). | **[PROPOSTA]** (EUA-E23) |
| **H-02** | **Synthesis Agent (SPEC-014) autônomo × Fase 2 do Manager** (ADR §2.1 já o absorve). | Média→**Resolvida** | `ROADMAP.md` §9/§21/§26; `GLOSSARIO.md` §2/§3; `MATRIZ` WF-06 | Marcar SPEC-014 como absorvido pela Fase 2 do Manager; escopo migra via EUA-E23. | **[APLICÁVEL]** — feito em **DHR-ARQ-002** (2026-10-01) |
| **H-03** | **Fusion × Conviction × Synthesis** — fronteira entre mecanismo (SPEC-003) e agente. | Média→**Resolvida** | `SPEC-003` plan §D0; `GLOSSARIO.md` §3 | Fusion/Conviction = mecanismos (SPEC-003) invocados pela Fase 2; Synthesis = Fase 2. | **[APLICÁVEL]** — **DHR-ARQ-001** + **DHR-ARQ-002** |
| **H-04** | **Manager-Dispatch (Fase 1) × Cognitive Orchestrator (SPEC-023)** — ambos "coordenam sem analisar". Risco de dupla orquestração. | Média | `ROADMAP.md` §14 (SPEC-023); `ADR-MANAGER-001` §2.3 (Fase 1) | Declarar na abertura da SPEC-023 que o **Manager é o orquestrador de missão/ciclo**; SPEC-023 (se sobreviver como slot) é **coordenação de nível de sistema** (scheduler cognitivo global), não re-despacho de agentes. Avaliar fusão/descarte do slot SPEC-023 no Dossiê. | **[PROPOSTA]** |
| **H-05** | **Blackboard (004) × Cognitive State (009) × KG (006) × Pattern Memory (017)** — fronteiras de "memória" podem sobrepor. | Baixa-Média | `ROADMAP.md` §5/§6/§7/§10 | Já governado por decisões abertas **M-001/G-001/H-001**; fixar fronteira (working vs permanente vs estado vs episódica) na abertura de cada uma. Não fechar agora (CONS-01). | **[PROPOSTA]** |
| **H-06** | **Regime de mercado: SPEC-003 (dimensão Q-A9) × SPEC-036 (Market Regime skill) × SPEC-037 (Volatility/Context skill)** — risco de dupla-dona do conceito "regime". | Média | `MATRIZ` C-3; `ROADMAP.md` §16; `SPEC-003/research-Q-A9-regime.md` | SPEC-003 fixa **em qual das 8 dimensões** o regime entra (Q-A9, decisão de Andraus); as skills 036/037 **produzem** o insumo de regime, não a dimensão de convicção. Fronteira: dimensão (003) × skill produtora (036/037). | **[PROPOSTA]** (Q-A9 + abertura 036/037) |
| **H-07** | **Skills analíticas (026-037) × agentes analíticos (010-013)** — fronteira skill vs agente. | Baixa | `ROADMAP.md` §15/§16; `ADR-CONFLUENCE-001-v3` | I-001 **FECHADA** (híbrido por Classe; corte exato → Dossiê SPEC-025). R-ARCH (skill≠agente) diferido a SPEC-025. Sem ação agora. | **[PROPOSTA]** (SPEC-025) |
| **H-08** | **Risk × TMP × Signal Package** — SPEC-016 (TMP interno) vs RISK-SPEC-022 (Signal Package fronteira) vs família RISK. | Baixa→**coerente** | `ROADMAP.md` §9 (SPEC-016); `GLOSSARIO.md` §3; `EUA-E20` | EUA-E19a já separou: TMP = interno (Synthesis=Manager Fase 2 → Risk); Signal Package = fronteira. Família RISK = 6 macro-slots (EUA-E20). Coerente; só vigiar na abertura. | **[PROPOSTA]** (EUA-E20) |

---

## 2. Achados — termos legados ainda vivos

| # | Termo legado | Onde (vivo, não-`_legacy/`) | Situação | Correção proposta | Classe |
|---|---|---|---|---|---|
| **H-09** | `Synthesis Agent` (autônomo) | `ROADMAP.md`, `GLOSSARIO.md`, `MATRIZ` | Absorvido (ADR §2.1) | Anotar = Fase 2 do Manager | **[APLICÁVEL]** — **DHR-ARQ-002** |
| **H-10** | `Conviction Engine` (agente) | `ROADMAP.md`, `GLOSSARIO.md`, `SPEC-003`, `atomic-spec` | Mecanismo (DHR-ARQ-001) | Já propagado | **[APLICÁVEL]** — **DHR-ARQ-001** |
| **H-11** | `Mission Engine` / `Master Orchestrator` / `Conviction Engine` / `Decision Orchestrator` em **canon BASELINED** | `canon/CEE-001` l.90/94/108/128; `canon/SAS-001` l.866/1035; `canon/PPQ-001` l.35/105/111/171/282/355/370 | Supersedidos por ADR-MANAGER-001, **sem anotação DIV** | **Sweep de anotação DIV** (molde DHR-TAX-001, que anotou CEM-001/CONSTITUTION) — **NÃO reescrever** (CONST-01); só comentário `<!-- DIV ... absorvido pelo Manager Agent — ADR-MANAGER-001 -->`. Requer ata de Andraus. | **[PROPOSTA]** |
| **H-12** | `Fractal Confluence Engine (FCE)` | `canon/SAS-001` l.178 (já tratado como "referência agnóstica" na Correção 5); `canon/SAS-001` (consumers) | Extinto → `confluence-elliott` (ADR-CONFLUENCE-001 v3) | SAS-001 l.178 já neutraliza; demais menções = incluir no sweep DIV de H-11. | **[PROPOSTA]** |
| **H-13** | `Agente Decisor` | `ADR-CONFLUENCE-001-v3` §1/§4 | Reconciliado em `DHR-ADR-HOC003` l.127 (= Manager Fase 2) | Já reconciliado por ata; nenhuma ação (ADR é registro histórico imutável). | **Sem ação** (resolvido) |
| **H-14** | Nome de slot **"Mission Engine"** (SPEC-015) e **"Cognitive Scheduler"** (SPEC-008) | `ROADMAP.md` §7/§9/§26 | Nome de slot ≈ termo legado eliminado | Renomear slots na **abertura** (EUA-E23: "Manager — Orquestração Mecânica / Missão & Ciclo de Vida / Convicção & Síntese"); não renumerar (INV-07). | **[PROPOSTA]** (EUA-E23) |

> **Observação sobre `canon/` baselined (H-11/H-12):** DHR-ARQ-001 anotou o CEM-001 por DIV porque o CEM-001 **cita** os componentes como produtor/consumidor. CEE-001/SAS-001/PPQ-001 têm o mesmo tipo de menção, mas **não há ata** que autorize tocá-los — por isso **[PROPOSTA]**, não aplicação. Recomenda-se um **DHR único de "sweep DIV de termos legados em canon"** (molde DHR-TAX-001), de risco baixo (só comentários, texto preservado — INV-07).

---

## 3. Achados — duplicação de mecanismo e ambiguidade de dono

| # | Achado | Severidade | Correção proposta | Classe |
|---|---|---|---|---|
| **H-15** | **"Formar convicção"** aparece em WF-04/WF-06 (Manager) e no mecanismo (SPEC-003) — risco de duplicar o cálculo. | Baixa→**coerente** | DHR-ARQ-001: Manager Fase 2 **invoca** o mecanismo da SPEC-003; não recalcula. Fronteira nítida em EUA-E23 §4.1. | **[APLICÁVEL]** (resolvido) |
| **H-16** | **Score 0–9 (PILOT) × Conviction Vector 8D** coexistem (GLOSSARIO l.92). | Baixa | Score 0–9 é **filtro paralelo PILOT** até CCM-001/J-001; GLOSSARIO já declara "NÃO substitui o Conviction Vector 8D". Vigiar: ao homologar SPEC-003, decidir aposentadoria do Score PILOT (não agora — J-001 aberto). | **[PROPOSTA]** (pós-SPEC-003) |
| **H-17** | **FSM do ciclo (WF-F02) × FSM do alarme (WF-A02)** — ambas determinísticas, donas candidatas SPEC-008/015. | Baixa | Atribuir ambas à Spec "Manager — Orquestração Mecânica" (Classe D/C) na abertura (EUA-E23). | **[PROPOSTA]** (EUA-E23) |

---

## 4. Conflitos com ADRs / CEM / CHM

- **Sem conflito ativo com CEM-001/CHM-001:** SPEC-003 constrói sobre eles sem redefinir (CC-02); CEM-001 já usa "Manager Agent (Fase 2)" (sem "Synthesis Agent"). ✓
- **ADR-MANAGER-001 §2.1 (FATO NORMATIVO "nenhum nome legado em specs futuras"):** os achados H-09/H-10/H-14 são justamente o cumprimento pendente dessa cláusula nos documentos de direção — tratados por DHR-ARQ-001/002 (aplicado) e EUA-E23 (proposto).
- **ADR-CONFLUENCE-001 v3 × ADR-MANAGER-001 ("Agente Decisor"):** já reconciliado em DHR-ADR-HOC003 (H-13). ✓

---

## 5. Plano de higiene priorizado

| Prioridade | Ação | Classe | Dependência |
|---|---|---|---|
| **P1 (feito)** | Propagar absorção Synthesis → Manager Fase 2 | [APLICÁVEL] | **DHR-ARQ-002** (2026-10-01) ✓ |
| **P1 (feito)** | Propagar Conviction Engine → mecanismo | [APLICÁVEL] | **DHR-ARQ-001** (2026-10-01) ✓ |
| **P2** | Homologar quantidade de Specs do Manager (2 vs 3) + renomear slots 008/014/015 | [PROPOSTA] | **EUA-E23 v2** → Andraus |
| **P2** | Decidir Q-A9 (dimensão do regime) → desambigua H-06 | [PROPOSTA] | `research-Q-A9-regime.md` → Andraus |
| **P3** | Ata de **sweep DIV** de termos legados em canon baselined (CEE-001/SAS-001/PPQ-001) | [PROPOSTA] | Andraus (molde DHR-TAX-001) |
| **P3** | Fronteira Manager-Dispatch × Cognitive Orchestrator (SPEC-023) — avaliar fusão/descarte do slot | [PROPOSTA] | abertura SPEC-023 (Dossiê) |
| **P4** | Fronteiras de memória (004/006/009/017) | [PROPOSTA] | M-001/G-001/H-001 (abertas) |
| **P4** | Aposentadoria do Score 0–9 PILOT | [PROPOSTA] | pós-homologação SPEC-003/J-001 |
| **P4** | Skill × agente (fronteira) | [PROPOSTA] | SPEC-025 (I-001 fechada) |

> **Regra de fechamento:** nada neste plano promove item do RMR-001 nem fecha decisão. P1 são propagações de decisões já homologadas (aplicadas nesta data). P2–P4 dependem de Andraus. Nenhum achado bloqueia o próximo trabalho autorizado (SPEC-003).

---

*Auditoria de Higiene das Specs — 2026-10-01. NÃO-NORMATIVA. Produzida pelo Especificador (Claude Code) por instrução de Andraus. Achados sujeitos a auditoria do Revisor; encaminhamento de Andraus.*
