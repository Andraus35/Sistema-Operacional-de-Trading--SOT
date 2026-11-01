# Proposta pré-testada — A6.4 + A6.1 parcial (doc-sync)

> **Não normativo. NADA APLICADO.** Pré-teste autorizado por Andraus (AskUserQuestion, 2026-11-01). Aplicar exige nova ordem dele. Não fecha decisão aberta (CONS-01). Fonte: `PROPOSTA-A6-MECANISMOS-EM-CAMADAS-2026-11-01.md`.

## O que muda (4 patches, aplicam limpo em `HEAD` e são independentes)
- **A6.4** `scripts/doc-sync-check.js`: o aviso de WARN só reaparece quando o **conjunto de achados** muda (assinatura sha256 das linhas `[WARN]/[ERRO]` + contagens, guardada em `.claude/.doc-sync-estado`, gitignored). **ERRO > 0 aparece sempre.** Falha ao ler/gravar o estado = mostra (nunca esconde).
- **A6.1 parcial** `.claude/settings.json`: `doc-sync-check.js stop` sai de `Stop` e `SubagentStop` (−2,44 s por fim de turno). Continua em `SessionStart` e no passo informativo do CI.
- `tests/test-doc-sync-check.js` (10 casos) + ligação em `npm run test:hooks` + linha no `.gitignore`.
- `governance/MECANISMOS.json`: canal e `verificado_em` do `hook.doc-sync-check` (COE-14).

## Pré-teste (cópia isolada de `HEAD`)
10/10 PASS; `node tests/test-hooks.js` passa. **3 mutantes mortos** (WARN sempre mostrado; ERRO tratado como WARN; assinatura só pela contagem). Não rodei o CI nem a suíte Python completa; o patch não toca Python.

## Perda de cobertura declarada
O drift deixa de ser avisado a cada fim de turno; passa a ser avisado no início da sessão e no CI. Um WARN novo criado numa sessão só aparece na seguinte (ou no CI). ERRO continua visível no início da sessão e no CI. `handoff-hook` (HO-03) **não** foi alterado.

## Para aplicar (por ordem de Andraus)
1. `git apply` dos 4 patches; 2. `npm run test:hooks`; 3. `check_coesao`, `check_refs`, mapa; 4. HANDOFF.
