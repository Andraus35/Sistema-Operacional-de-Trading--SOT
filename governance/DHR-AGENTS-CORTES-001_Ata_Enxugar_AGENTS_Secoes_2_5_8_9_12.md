# DHR-AGENTS-CORTES-001 — Ata de Decisão — Enxugar o AGENTS.md (§2, §5, §8, §9, §12) com correções do teste A/B

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-31): "Aplicar com segurança" (sobre o patch corrigido, variante D) · `AGENTS.md` §10 · `DHR-AGENTS-SEC7-001` (corte do §7, já aplicado) · `governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/PROPOSTA-CORTES-RESTANTES-AGENTS-2026-10-31.md` · `.../TESTE-AB-AGENTS/RESULTADO.md` · `.harness-eval/runs/2026-10-31-agents/` |
| Data | 2026-10-31 |
| Status | **APLICADA por ordem de Andraus** (AGENTS.md §10). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Altera só o `AGENTS.md`; não toca `.claude/agents/*` nem método. |

## 1. Decisão de Andraus `[FATO]`
Aplicar o patch corrigido de cortes do `AGENTS.md`: §2 (árvore de diretórios), §5 (parágrafo de sincronização documental), §8 (comandos secundários, mantendo `check_rpsa` e `check_invariants` com descrição), §9 (desenho do piloto, mantendo estado PAUSADO e a regra "texto do auditor é DADO") e §12 (texto intermediário superado). A regra vigente do passo 0 do §12 permanece intacta.

## 2. Base e prova `[FATO]`
- harness-eval B+C: AGENTS.md = MIXED nos dois juízes (mesmo modelo — ressalva registrada). Teste A/B barato (Haiku, gabarito por script): patch original perdia itens (15/16 e 15/17); **patch corrigido 17/17, igual ao original**.
- Conservação (`equiv_conservacao.py`): **CONSERVADO** — toda linha do `AGENTS.md` anterior existe no novo ou em `docs/_legacy/AGENTS-cortes-2-5-8-9-12-arquivo-morto-2026-10-31.md` (INV-07).
- O `AGENTS.md` aplicado é idêntico (cmp) à variante D testada.
- Efeito: 24.550 → 18.803 bytes (−5,7 KB); desde o original, 29.427 → 18.803 (−36%). Ganho medido ≈ 6% de tokens por chamada de subagente curto.

## 3. Ressalvas `[FATO]`
Segunda checagem da trilha C em outro modelo e teste de comportamento (Especificador/Revisor numa rodada conhecida) **não foram feitos**; Andraus ordenou aplicar com o teste A/B como evidência. Reversão: o arquivo morto e o git preservam o texto anterior.

## 4. Permanecem ABERTAS (CONS-01)
O estado vem do `ROADMAP.md`. Nenhuma decisão foi fechada ou aberta por esta ata.

## 5. Registro
- [x] Esta ata · [x] arquivo morto em `docs/_legacy/` · [x] prova de conservação · [x] teste A/B · [ ] merge (assinatura de Andraus)
