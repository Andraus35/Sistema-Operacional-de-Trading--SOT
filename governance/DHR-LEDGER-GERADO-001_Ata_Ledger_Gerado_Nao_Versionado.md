# DHR-LEDGER-GERADO-001 — Ata de Decisão — LEDGER-ACHADOS gerado, não versionado

> Pré-teste: PROPOSTA-LEDGER-2026-11-01 (pasta CONCORRENCIA-DE-SESSOES, ramo ccr-b7c09dc1-y4rafd) (ramo `ccr-b7c09dc1-y4rafd`).

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final (registro pelo Orquestrador) |
| Ref | Ordem de Andraus (chat, 2026-11-01) · `AGENTS.md` §12 (LOOP-001/DHR-LOOP-001) · PROPOSTA-LEDGER-2026-11-01 |
| Data | 2026-11-01 |
| Status | **APLICADA por ordem de Andraus** (chat, 2026-11-01: "Assino o ledger agora, mapa depois"), em PR **sem mesclar**; o merge segue com Andraus. Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda só se o ledger derivado é commitado; o método do loop (categorias, registro de causas, retrospectiva) não muda. |

## 1. Decisão proposta `[PROPOSTA]`
`governance/aprendizado/LEDGER-ACHADOS.md` deixa de ser versionado: `.gitignore` + `git rm --cached`. `loop_ledger.py` já gera sob demanda e é função pura dos pareceres; o **parecer** continua sendo a fonte.

## 2. O que muda
1. `.gitignore` + `git rm --cached` do ledger.
2. `AGENTS.md` §12 passo 2: de "rodar `loop_ledger.py` e commitar o ledger com o parecer" para "o ledger é gerado; o parecer com o bloco `ACHADOS-ESTRUTURADOS` é a fonte". Passos 1, 3, 4 e 5 inalterados (o passo 4 usa a saída do script).
3. `MECANISMOS.json`: nota em `det.loop-ledger` (COE-14). `ci.yml`: passo informativo passa de `--check` para geração. Nenhum script muda.

## 3. Evidência `[FATO]`
Teste com 2 pareceres reais da SPEC-048 em dois ramos: ledger commitado → `CONFLICT`; ledger gerado → merge limpo e duas gerações idênticas. Não medido nos ~19 pareceres. **Correção:** `ci.yml` chamava `loop_ledger.py --check` como passo informativo; foi trocado por geração informativa (`--stdout`).

## 3-bis. Acoplamento descoberto no CI do PR #164 `[FATO]`
O `build_map.py` indexa arquivos do **disco**, não do Git. Um `LEDGER-ACHADOS.md` gravado localmente (mesmo ignorado) entra no resumo do mapa commitado e o CI, sem o arquivo, calcula outro resumo (`build_map_check` vermelho). Por isso o ledger é **lido por `--stdout` e nunca gravado**. Alternativa estrutural: tirar também o mapa do Git (rascunho `DHR-MAPA-GERADO-001`).

## 4. Registro
- [x] Assinatura de Andraus (chat) · [x] aplicado em PR · [ ] merge (Andraus) · [ ] CATALOGO
