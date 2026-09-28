# DHR-DOCSYNC-001 — Ata de Homologação — Detector de Sincronização Documental + Correções de Registro

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Auditoria profunda de incoerência/contradição do repositório (2026-09-28, sessão Claude Code) + parecer do Revisor SOT (CONFORME, 2026-09-28) |
| Data | 2026-09-28 |
| Status | **HOMOLOGADA — vigência imediata** |
| Compatibilidade | Minor (nova ferramenta F.3 + correções aditivas de registro; nenhum modelo canônico redefinido; nenhuma decisão aberta fechada) |

---

## 1. Decisão

**HOMOLOGA-SE** o conjunto de mudanças abaixo, auditado pelo Revisor SOT (parecer CONFORME, 2026-09-28) e verificado pelos gates determinísticos do harness (`npm test` 11/11, `npm run lint` 8/8, `python -m unittest discover -s tests` 58/58, `scripts/check_refs.py` ERRO=0, `scripts/build_map.py --check` em dia):

**1.1 — Novo mecanismo F.3 Feedback: `scripts/check_doc_sync.py`.** Detector determinístico, somente leitura (Detector ≠ Gate — ENF-03; nunca promove item nem fecha decisão — CONS-01), que cruza fatos objetivos do próprio repositório para achar drift de sincronização documental: (D1) decisão ABERTA do `ROADMAP.md` citada como fechada inline; (D2) decisão FECHADA ainda listada como aberta nos documentos-registro (`governance/CATALOGO-OFICIAL.md`, `governance/CIC-*.md`); (D3) `[Fonte: ...]` do próprio `governance/RULES.md` fundamentando regra normativa em família RULE-xx sem seção registrada (RULE-HG-02); (D4) Estado de item do `RMR-001` fora do enum do seu próprio §2; (D5) documento de intake `backlog/BL-0NN-*.md` dessincronizado do painel vivo. Acompanhado de `scripts/doc-sync-check.js` (hooks `Stop`/`SubagentStop`/`SessionStart`, sempre exit 0 — nunca bloqueia o agente) e `tests/test_check_doc_sync.py` (11 testes). Wiring: `package.json` (`npm run sync`), `.github/workflows/ci.yml` (passo informativo, `continue-on-error: true` — mesma régua de introdução gradual de `scripts/check_refs.py`/`scripts/backlog_triggers.py`), `AGENTS.md` §5/§8.

**1.2 — Correções de registro (fatos já homologados, nenhuma decisão nova fechada):**
- `governance/CATALOGO-OFICIAL.md` §5 e `governance/CIC-001` §5.1/§5.3/§8/§9 — L-001 sincronizada como FECHADA (já era FECHADA desde DHR-SPEC019-001, 2026-09-22; só os dois registros estavam desatualizados). Histórico preservado (strikethrough + notas aditivas — INV-07).
- `governance/RULES.md` — `RULE-CEE-001` corrigida para os 5 níveis dos 4Es (faltava Economicidade, já vigente desde Q-009/CEE-001 §12); nova seção `## Regras de Avaliação do Harness (RULE-EV)` registrando `RULE-EV-01..07` (já homologadas com a SPEC-020, 2026-09-27, DHR-SPEC020-001 — só o passo de registro pelo Controlador, exigido por RULE-HG-02, estava pendente).
- `backlog/BL-018-RISK-AGENT-backlog.md` — campo Estado sincronizado com o painel vivo (`Em espera`, já promovido por DHR-EUA-E19a em 2026-09-22); nota honesta de que a promoção ocorreu pelo Passo 11-bis (gatilho automático), não por um Ato de admissão dedicado.
- `specs/features/SPEC-020/plan.md` e `specs/features/SPEC-021/plan.md` — adicionada a palavra "Status:" ao eco textual já existente (linha de Complexidade/Profundidade-alvo), corrigindo falha pré-existente do `npm run lint`. Nota pós-homologação aditiva em SPEC-020/plan.md linha 155 (RULE-EV já registrada).

**1.3 — Duas novas decisões abertas registradas (CONS-01 — permanecem ABERTAS, esta ata NÃO as fecha):**
- **RULE-REG-001** — famílias `RULE-DEC`/`RULE-HD`/`RULE-MET` citadas como `[Fonte: ...]` em regras já normativas de `RULES.md`, sem seção própria registrada; texto-fonte disperso em EUA-E04/E13/E14. Requer decisão de Andraus sobre autoria (Especificador redige as três seções a partir das atas de origem) e, para `RULE-HD` especificamente, se é família autônoma ou terminologia interna do mecanismo CC-08/`RULE-HV` (caso em que a citação deveria apontar direto para `RULE-HV-02/03`, sem criar seção `RULE-HD`).
- **RMR-EST-001** — Estado `Diferido` do BL-013 no `RMR-001` fora do enum de 5 valores do próprio §2 (`Proposto`/`Em espera`/`ATIVADO`/`Absorvido`/`Descartado`). Requer decisão de Andraus entre corrigir o dado (`Diferido`→`Em espera`, narrativa move para a coluna Ação) ou emendar formalmente o §2 do RMR-001 para incluir `Diferido` como sexto estado.

Nenhum item de 1.3 é resolvido por esta ata — permanecem registrados em `ROADMAP.md` ("Decisões abertas ativas"), `AGENTS.md` §7, `governance/CATALOGO-OFICIAL.md` §5 e `governance/CIC-001` §5.2, aguardando decisão substantiva.

---

## 2. Efeitos imediatos desta homologação

1. `scripts/check_doc_sync.py`, `scripts/doc-sync-check.js`, `tests/test_check_doc_sync.py` — **FATO NORMATIVO** (mecanismo F.3 do harness), vigência imediata.
2. `.claude/settings.json`, `package.json`, `.github/workflows/ci.yml`, `AGENTS.md` — wiring efetivado.
3. `governance/CATALOGO-OFICIAL.md`, `governance/CIC-001_Inventario_Conformidade.md`, `governance/RULES.md`, `backlog/BL-018-RISK-AGENT-backlog.md`, `specs/features/SPEC-020/plan.md`, `specs/features/SPEC-021/plan.md` — correções de registro efetivadas (item 1.2).
4. `RULE-REG-001` e `RMR-EST-001` — decisões abertas registradas (item 1.3), CONS-01 preservado.

---

## 3. Registro do Controlador (efeitos aplicados — 2026-09-28)

- [x] `scripts/check_doc_sync.py` + `scripts/doc-sync-check.js` + `tests/test_check_doc_sync.py` criados e testados (11/11).
- [x] `.claude/settings.json`, `package.json`, `.github/workflows/ci.yml`, `AGENTS.md` §5/§8 — wiring aplicado.
- [x] `governance/CATALOGO-OFICIAL.md` — L-001 sincronizada (§5); RULE-REG-001/RMR-EST-001 registradas (§5); nova linha de ata (§7.3, abaixo).
- [x] `governance/CIC-001_Inventario_Conformidade.md` — L-001 movida §5.1→§5.3; RULE-REG-001/RMR-EST-001 registradas (§5.2); §8/§9 com nota de atualização posterior.
- [x] `governance/RULES.md` — RULE-CEE-001 (5 níveis); seção RULE-EV-01..07 registrada; `[DECISÃO NECESSÁRIA: RULE-REG-001]` anotada nas 5 citações órfãs.
- [x] `backlog/BL-018-RISK-AGENT-backlog.md` — Estado sincronizado; nota sobre Passo 11-bis.
- [x] `backlog/RMR-001_Painel_Backlog.md` — `[DECISÃO NECESSÁRIA: RMR-EST-001]` anotada na linha do BL-013.
- [x] `ROADMAP.md` §"Decisões abertas ativas" e `AGENTS.md` §7 — RULE-REG-001/RMR-EST-001 registradas.
- [x] `specs/features/SPEC-020/plan.md`, `specs/features/SPEC-021/plan.md` — lint corrigido; nota pós-homologação aditiva.
- [x] Mapa do projeto, referências cruzadas e suíte de testes revalidados (`build_map.py --check`, `check_refs.py`, `npm test`, `npm run lint`, `python -m unittest discover`, `check_doc_sync.py`).

**Pendências (não bloqueiam; são o objeto de RULE-REG-001/RMR-EST-001):** autoria do texto normativo de `RULE-DEC`/`RULE-HD`/`RULE-MET` (ou decisão de que `RULE-HD` não é família própria); decisão sobre o Estado `Diferido` do BL-013 no enum do RMR-001 §2.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
