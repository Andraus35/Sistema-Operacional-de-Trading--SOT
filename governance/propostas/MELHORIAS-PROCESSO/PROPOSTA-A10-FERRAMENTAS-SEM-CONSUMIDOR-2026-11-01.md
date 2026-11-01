# Proposta A10 — Ferramentas sem consumidor: quase todas têm consumidor; só um diretório é candidato

> **Não normativo. PROPOSTA MEDIDA — NADA APLICADO.** Fonte: `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` §A10/B5. Pedido: nº 4 da `PAUTA-DE-DECISOES.md` (Andraus, AskUserQuestion 2026-11-01). Não decide por Andraus nem fecha decisão aberta (CONS-01).

## 1. Medido hoje (2026-11-01)
| Item | Tamanho | Último commit | Consumidor real | Conclusão |
|---|---|---|---|---|
| `.eslintrc.json` | 255 B | 2026-10-17 | sensor **SNS-02** do `harness-score` (`docs/_legacy/HARNESS-REPORT.md` l.97, l.218); CI roda `npx harness-score` (`ci.yml` l.238, `continue-on-error`) | **Manter** (decisão `DHR-COESAO-002` §4: movido não; existe de propósito) |
| `.prettierrc` | 159 B | 2026-10-17 | sensor **SNS-04** (idem) | **Manter** |
| `tsconfig.json` | 404 B | 2026-10-17 | sensor **SNS-03** (+4 pts; HARNESS-REPORT l.97, l.219). Nenhum `tsc` em `package.json`/CI/hooks | **Manter**, mesma razão — a auditoria o listou como "sem consumidor" sem ver o sensor |
| `.pre-commit-config.yaml` | 870 B | 2026-10-17 | roda schemas/specs/mapa quando o desenvolvedor instala o `pre-commit`; o CI cobre o mesmo; `gate-check` já saiu (`DHR-COESAO-002` §2) | **Manter** |
| `harness-score` | `npx` | — | `package.json` (`eval`/`score`/`score:diff`) e `ci.yml` (informativo) | **Manter** (opcional, informativo) |
| `revisao-independente/` | 2 `.txt` | 2026-10-17 | só citado por `DHR-HIGIENE-001`, `AVALIACAO-MECANISMOS-REVISOR-2026-10-17.md` e por si; procedimento ad hoc da SPEC-006 (ramo `spec006-plan`) | **Único candidato real** |
**Limite:** `npx harness-score` exige rede e não está instalado aqui; **não** conferi o placar nem se os sensores ainda contam esses arquivos (a fonte é o relatório arquivado `HARNESS-REPORT.md`).

## 2. Opção única (precisa de ordem dele; nada aplicada)
**Arquivar `revisao-independente/` em `docs/_legacy/revisao-independente/`** com `LEIA-ME` datado (INV-07: nada é apagado), e atualizar as 3 referências (`check_refs` deve ficar com ERRO=0). Toca só pasta não reservada; ata curta (`MODELO-ATA-OPERACIONAL-CURTA.md`). Ganho: ~1 pasta a menos no mapa/raiz e uma explicação a menos no `check_coesao`; **ganho de tokens ≈ 0** (não é leitura obrigatória). **Recomendação: aprovar**, sem pressa (baixo valor, baixo risco).

## 3. Efeito sobre a auditoria
A10 fica **fechado como "falso alarme parcial"**: 5 de 6 itens têm consumidor (sensores do `harness-score`, pre-commit, CI). Reabrir só se Andraus decidir aposentar o `harness-score` — aí os três arquivos de config ficariam sem consumidor.
