# DHR-AGENTS-SEC7-001 — Ata de Decisão — Enxugar o AGENTS.md §7 (duplicado do ROADMAP)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-31, resposta "Aplicar só o §7" ao AskUserQuestion do Orquestrador) · `AGENTS.md` §10 · `governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` (A5) · `.harness-eval/runs/2026-10-31-agents/` |
| Data | 2026-10-31 |
| Status | **APLICADA por ordem de Andraus** (AGENTS.md §10). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Altera só o `AGENTS.md`; não toca `.claude/agents/*` nem método. |

## 1. Decisão de Andraus `[FATO]`
Aplicar o corte **somente** do §7 do `AGENTS.md`: substituir a narrativa de decisões fechadas por um ponteiro ao `ROADMAP.md` (fonte do estado) mais a lista curta das decisões ativas. Outros cortes sugeridos pelo harness-eval (§2, §5, §8, §9, §12) **não** foram autorizados.

## 2. Base e prova `[FATO]`
- harness-eval B+C do `AGENTS.md`: trilha A 0 quebrados; trilha C classificou o arquivo como MIXED nos dois juízes (mesmo modelo, ressalva registrada), com o §7 narrativo entre os cortes.
- Duplicação medida: 53 dos 55 IDs citados no §7 já constam no `ROADMAP.md`; os 2 restantes (`DHR-BENCH-INTEL-001`, `DHR-DOCSYNC-003`) são notas de correção do próprio AGENTS e ficam no arquivo morto.
- Prova de conservação (`equiv_conservacao.py`): **CONSERVADO** — toda linha do §7 anterior existe no AGENTS.md novo ou em `docs/_legacy/AGENTS-secao7-arquivo-morto-2026-10-31.md` (INV-07).
- Efeito: `AGENTS.md` de 29.427 para 24.306 bytes (≈ −5,1 KB).

## 3. Permanecem ABERTAS (CONS-01)
O estado vem do `ROADMAP.md`. Nenhuma decisão foi fechada ou aberta por esta ata.

## 4. Registro
- [x] Esta ata · [x] arquivo morto em `docs/_legacy/` · [x] prova de conservação · [ ] merge (assinatura de Andraus)
