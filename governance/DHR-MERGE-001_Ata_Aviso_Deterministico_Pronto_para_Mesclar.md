# DHR-MERGE-001 — Ata de Decisão — Aviso determinístico "já é possível e seguro mesclar"

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-30): "Devo ser deterministicamente avisado quando já posso mesclar. Garanta isso e incorpore ao Hook de perguntas ao usuário." · `DHR-ASK-002` (hook de perguntas) · `AGENTS.md` §10 · `DHR-COESAO-005` |
| Data | 2026-10-30 |
| Status | **REGRA DE PROCESSO ADOTADA** (decisão direta de Andraus em chat; AGENTS.md §10). Não toca arquivo selado. |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Regra operacional do Orquestrador/hook: não altera texto de agente de construção nem método. |

## 1. Decisão de Andraus `[FATO]`
Quando o trabalho do ramo estiver pronto para mesclar, o Orquestrador **é avisado por código** (não por julgamento) e **pergunta a Andraus por AskUserQuestion**: "já é possível e seguro mesclar; posso mesclar ao seu comando". A mesclagem continua sendo ato de Andraus (AGENTS.md §10).

## 2. Mecanismo `[FATO]`
- `scripts/merge_ready.py` (Detector, ENF-03): PRONTO ⇔ PR aberto do ramo atual, não-rascunho, `mergeable_state == clean`, cabeça do PR == `git rev-parse HEAD`, árvore limpa, ≥ 1 check-run e todos concluídos com success/neutral/skipped. Informa arquivos do PR reservados pelo CODEOWNERS. REST via `gh api` (GraphQL indisponível em sessões Claude Code). Erro/rede ⇒ INDETERMINADO (nunca afirma "pronto").
- `scripts/andraus-ask-guard.js` (Stop) — **3ª regra**: se as regras anteriores não bloquearam e o detector devolve PRONTO, bloqueia o fim de turno **uma vez por commit-cabeça** e manda perguntar a Andraus. `stop_hook_active` nunca bloqueia; falha ⇒ libera. Timeout do hook 15→40 s (`.claude/settings.json`).
- Testes: `tests/test_merge_ready.py` (10) e `tests/test-ask-guard.js` (+8). `governance/MECANISMOS.json` no mesmo PR (COE-14).

## 3. Limites honestos `[FATO]`
Só vê o ramo **atual** e o PR **aberto** dele; checks que o GitHub ainda não registrou ⇒ "não pronto". Não mescla, não aprova e não decide; "seguro" = critérios objetivos acima, **não** parecer de Revisor nem homologação. Mudança de cabeça (novo commit) reabre o aviso.

## 4. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001. Nenhuma foi fechada.

## 5. Registro
- [x] Esta ata · [x] código + testes · [x] MECANISMOS.json · [x] hook timeout · [ ] verificação ao vivo no 1º PR verde · [ ] merge (assinatura)
