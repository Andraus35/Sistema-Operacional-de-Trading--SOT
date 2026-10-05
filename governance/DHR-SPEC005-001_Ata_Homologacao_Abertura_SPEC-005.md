# DHR-SPEC005-001 — Ata de Homologação — Abertura da SPEC-005 (Cognitive Event Bus)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Parecer do Revisor sobre a ABERTURA: **NÃO CONFORME** (1 Médio — RULE-ECC-04, SRC-BB-01; 2 Menores) → corrigido → re-revisão delta **CONFORME** (1 Menor A4 não-bloqueante) — `specs/features/SPEC-005/ABERTURA.md` + `research.md` + `sources/` |
| Data | 2026-10-04 |
| Status | **ABERTURA HOMOLOGADA** (instrução direta de Andraus em chat: "Homologar e registrar") — Dossiê de Pesquisa + Proposta de Abertura. **NÃO é baseline** — o Plan ainda não foi escrito e só inicia por ordem de Andraus. |
| Compatibilidade | Minor (não toca modelo canônico baselined nem fecha decisão aberta) |
| Gates | `check_repo_research.py` OK · `check_doc_sync.py` ERRO=0 · `build_map.py --check` em dia |

---

## 1. Origem
Auditoria documental (orquestrador, 2026-10-04): o Event Bus nasce como ideia inicial de engenharia de software (KERNEL-V2 ~l.1831; ENGENHARIA-GERAL Doc 13 l.4802-4805; metáfora de SO) e a dúvida **EVENT-BUS-001** ("existe? como se distingue do Blackboard?") estava aberta só no ADR-MANAGER-001 l.201 e na DHR-ADR-HOC003 l.145, ausente das listas oficiais. Andraus mandou abrir a SPEC-005 reenquadrada.

## 2. Decisão
- **Número SPEC-005 preservado**; **nome "Cognitive Event Bus" MANTIDO** (decisão de Andraus; reenquadramento de rótulo recusado); **1 Spec**; **HIGH · D0–D7**; Classe predominante **D + C** (declaração por BASpec no Plan, CC-11); CC-12 e RULE-ECC-05 não incidem (confirmado pelo Revisor).
- **Forma A (confirmada):** camada fina de notificação de mudança sobre o log append-only da SPEC-004 (cursor/dedupe de consumo, envelope de evento, correlation/causation, latência/metadados de transporte) **+ canal de saída do Signal Package** (INV-05: SOT não executa ordem). Princípio: **transporte ≠ fonte de verdade**. Mecanismo físico (push/poll) = **INDETERMINADO** até o Plan.
- **Opção B** (fundir na SPEC-004) rejeitada; **Opção C** (broker completo com prioridade/retry/dead-letter) **adiada e registrada**, reavaliável com múltiplos consumidores distribuídos/alta vazão.
- **Sem duplicar** o que a SPEC-004 v1.2 já torna normativo (ordem de commit, idempotência de escrita, replay, identidade autenticada, `supersedes`/`derived_from`).
- **Doc 13** (ENGENHARIA-GERAL) = fundamento **histórico não-normativo**, superado quanto ao canal de estado; **RULE-BB-001 prevalece**. Nada apagado (INV-07).
- Baselines/canônicos que citam o Event Bus (SPEC-001 EARS 8 e l.75, SPEC-004, CEM-001 l.725, CONSTITUTION l.235, GPR-001 l.457, SAS-001 §6.7) apontam para o **número**: sem erratum.

## 3. EVENT-BUS-001 — registro oficial
Registrada por Andraus nas listas oficiais (`AGENTS.md` §7 e `ROADMAP.md` "Decisões abertas ativas") com **dona = SPEC-005**, **ABERTA**; será resolvida **na homologação da SPEC-005**. **Não fechada por este ato.**

## 4. Achados e tratamento
| ID | Severidade | Tratamento |
|---|---|---|
| A1 | Médio | SRC-BB-01: trecho verbatim via WebFetch (openlayer.com) com correspondência string-a-string a research.md §3.1 — RESOLVIDO |
| A2 | Menor | `_LIMITACAO-WEB.txt` ponto 4 atualizado (origem dual: WebFetch + API pública do GitHub consultada pelo orquestrador em 2026-10-04; risco residual mantido) — RESOLVIDO |
| A3 | Menor | BL-017 separado dos ATIVADOS (estado real `Em espera`) — RESOLVIDO |
| A4 | Menor | `research.md` §6.4 ainda traz "Se Andraus aprovar o reenquadramento de nome…" (rename foi recusado); conclusão inalterada, texto não-normativo — a alinhar no Plan |
- **Nota de honestidade:** o gate RULE-ECC-06 falhava por formato (URLs sem `https://`, campos com anotações, data de commit INDETERMINADA); o orquestrador corrigiu o formato e preencheu os valores pela API pública do GitHub (debezium: 13177 ★, Apache-2.0, último commit 2026-10-02; langgraph: 42716 ★, MIT, 2026-10-03; ambos não arquivados). Os vereditos já eram ELEGÍVEL; `postgresql-event-sourcing` segue NÃO ELEGÍVEL (arquivado). Risco residual: valores da API não reproduzíveis pelo Revisor sem rede (ENF-03).

## 5. Permanecem ABERTAS (CONS-01)
**EVENT-BUS-001 · M-001 (enum) · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001.** Dossiê com validade de 90 dias (HIGH): limite 2027-01-02.

## 6. Registro (efeitos aplicados)
- [x] Este documento · [x] `ROADMAP.md` (slot §21, "próximo trabalho", decisões abertas) · [x] `AGENTS.md` §7 · [x] `governance/CATALOGO-OFICIAL.md` · [x] `backlog/RMR-001_Painel_Backlog.md` (nota 11-bis) · [x] RPSA: carimbo dos agentes → `DHR-SPEC005-001` · [x] `build_map.py` + `--check`.
- Próximo gate: Plan (`plan.md` + `checks.md`, via `tlc-spec-lean`) — **somente por ordem de Andraus**.

---

**Andraus**
