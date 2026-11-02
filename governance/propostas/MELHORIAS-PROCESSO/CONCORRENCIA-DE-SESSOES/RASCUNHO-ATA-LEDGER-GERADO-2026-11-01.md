# RASCUNHO — DHR-LEDGER-GERADO-001 — Ata de Decisão — LEDGER-ACHADOS gerado, não versionado

> **RASCUNHO para Andraus ler, editar e assinar. NÃO vigora e NADA foi aplicado.** Pré-teste: `PROPOSTA-LEDGER-2026-11-01.md`.

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final (registro pelo Orquestrador) |
| Ref | Ordem de Andraus (chat, 2026-11-01) · `AGENTS.md` §12 (LOOP-001/DHR-LOOP-001) · `PROPOSTA-LEDGER-2026-11-01.md` |
| Data | [preencher na assinatura] |
| Status | **PROPOSTA — vigora só com a ordem expressa de Andraus**. Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda só se o ledger derivado é commitado; o método do loop (categorias, registro de causas, retrospectiva) não muda. |

## 1. Decisão proposta `[PROPOSTA]`
`governance/aprendizado/LEDGER-ACHADOS.md` deixa de ser versionado: `.gitignore` + `git rm --cached`. `loop_ledger.py` já gera sob demanda e é função pura dos pareceres; o **parecer** continua sendo a fonte.

## 2. O que muda
1. `.gitignore` + `git rm --cached` do ledger.
2. `AGENTS.md` §12 passo 2: de "rodar `loop_ledger.py` e commitar o ledger com o parecer" para "o ledger é gerado; o parecer com o bloco `ACHADOS-ESTRUTURADOS` é a fonte". Passos 1, 3, 4 e 5 inalterados (o passo 4 usa a saída do script).
3. `MECANISMOS.json`: nota em `loop_ledger` (COE-14). Nenhum script muda.

## 3. Evidência `[FATO]`
Teste com 2 pareceres reais da SPEC-048 em dois ramos: ledger commitado → `CONFLICT`; ledger gerado → merge limpo e duas gerações idênticas. Não medido nos ~19 pareceres. **Correção:** `ci.yml` chamava `loop_ledger.py --check` (informativo); a ata aplicada (PR #164) o trocou por geração.

## 4. Registro
- [ ] Assinatura de Andraus · [ ] aplicar em PR · [ ] CATALOGO
