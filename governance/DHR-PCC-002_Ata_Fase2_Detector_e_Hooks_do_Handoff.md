# DHR-PCC-002 — Ata — Fase 2 do PCC-001: detector, hooks e CI informativo do HANDOFF.md

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Fase 2 AUTORIZADA por Andraus** (chat, 2026-10-17: *"Prosseguir"* seguido da escolha **"Fase 2 do PCC-001 agora"** no AskUserQuestion, antecipando o gatilho de 3 sessões reais do PCC-001 §7). Escopo = só o que é **Detector, não Gate**. Não fecha nem abre decisão aberta. |
| Compatibilidade | Aditiva (INV-07). Reversível por `git revert` (remove scripts, hooks, passo de CI e a linha/bullet do `AGENTS.md`). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Altera `AGENTS.md` (§8 e §11), `.claude/settings.json` e CI; nenhum texto de arquivo de agente (`.claude/agents/*.md`) é alterado. |

## 1. Decisão `[FATO]`
Andraus escolheu executar a Fase 2 já, em vez do Plan da SPEC-006. A opção apresentada dizia que a Fase 2 "exige proposta própria e suas decisões D-PCC-4 e D-PCC-5". O Orquestrador interpretou conservadoramente (Andraus pode corrigir):
- **Autorizado e feito:** `scripts/check_handoff.py` (HO-01..HO-09), `scripts/handoff-hook.js` + hooks `SessionStart`/`Stop`/`SubagentStop`, passo de CI **informativo**, testes, linha em `AGENTS.md` §8 e atualização do último bullet da §11.
- **NÃO decidido / NÃO feito:** **D-PCC-4** (promoção do detector a bloqueante — segue informativo) e **D-PCC-5** (item de handoff no Passo 0 do Revisor — muda `.claude/agents/revisor.md`, só por decisão expressa de Andraus). **D-PCC-3** (BUILD-LEDGER) é da Fase 3.

## 2. Efeitos
1. `scripts/check_handoff.py` — HO-01 frontmatter/seções · HO-02 `base_commit` · HO-03 defasagem · HO-04 cadeia/arquivo idêntico · HO-05 ≤150 linhas · HO-06 DHR inexistente / decisão aberta como fechada (reusa `Facts` do `check_doc_sync.py`) · HO-07 Spec vs ROADMAP · HO-08 segredo · HO-09 linguagem de homologação sem DHR.
2. `scripts/handoff-hook.js` — `session-start` injeta o cabeçalho do handoff + achados; `stop` lembra de reescrever se HO-01/03/04. Nunca bloqueia (exit 0).
3. `.claude/settings.json` — hooks nos três eventos. `.github/workflows/ci.yml` — passo `continue-on-error`. `package.json` — `npm run handoff`.
4. `tests/test_check_handoff.py` (13) e `tests/test-handoff-hook.js` (4).
5. `AGENTS.md` §8 e §11 (Fase 2).

## 3. Limites `[FATO]`
Detector ≠ Gate (ENF-03): não escreve o handoff, não fecha decisão, não registra homologação. Mudanças em `AGENTS.md` seguem só por decisão expressa de Andraus (§10) — aqui citada.

## 4. Permanecem ABERTAS (CONS-01)
O estado das decisões é o do `ROADMAP.md` (linhas "Decisões abertas ativas"/"FECHADAS"), que prevalece. **Nenhuma fechada ou aberta por este ato.** Em aberto do PCC-001: D-PCC-3, D-PCC-4, D-PCC-5.

## 5. Registro
- [x] Esta ata · [x] `AGENTS.md` §8/§11 · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] RPSA automático (sem escopo de agente)

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno.*
