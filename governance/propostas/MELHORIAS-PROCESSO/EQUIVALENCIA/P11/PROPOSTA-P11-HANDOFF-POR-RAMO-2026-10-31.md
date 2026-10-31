# Proposta pré-testada — P11: handoff por ramo como regra (e `check_handoff` entende a união de cadeias)

> **Não normativo. PROPOSTA — NADA APLICADO.** Aprovada por Andraus (chat, 2026-10-31; `DHR-RETRO-003`) **como proposta pré-testada**: aplicar exige nova ordem dele. Não fecha decisão aberta (CONS-01).

## 1. Problema (medido)
Sessões em paralelo repetiram números de handoff (HO-110..122 e HO-127) e exigiram preservar uma das cadeias em `docs/handoffs/ramo-<ramo>/` no merge. O `check_handoff` (HO-04) então acusava ERRO por "união de cadeias", ruído que a `main` já descrevia como "aviso esperado".

## 2. O que muda (2 patches, pré-testados em cópia isolada)
- **`PATCH-CHECK-HANDOFF-ramo-2026-10-31.patch`** (`scripts/check_handoff.py`, HO-04): se o arquivo arquivado difere do handoff substituído **e** existe cópia EXATA do substituído em `docs/handoffs/ramo-*/<mesmo id>.md`, vira **INFO** ("cadeia do ramo preservada"); senão continua **ERRO**.
- **`PATCH-TESTES-CHECK-HANDOFF-ramo-2026-10-31.patch`** (`tests/test_check_handoff.py`): 4 testes — aceita cópia exata; **recusa** cópia adulterada; **recusa** sem cópia; **recusa** cópia com conteúdo certo e id errado.
- **Texto da regra (para o `AGENTS.md` §11, arquivo reservado — não aplicado):** "Sessões em paralelo: antes de numerar um handoff, ler a `main`. Se o número colidir, a cadeia do ramo vai para `docs/handoffs/ramo-<ramo>/` (INV-07) e o handoff da `main` fica em `docs/handoffs/`; `check_handoff` aceita a cópia exata como INFO."

## 3. Pré-teste
`tests.test_check_handoff` 25/25 com o patch; o teste de aceitação **falha** no script original e os 3 de recusa passam nos dois (guardas); **4 mutantes mortos** (aceitar qualquer ramo, glob sem id, INFO→ERRO, ERRO→INFO). `git apply --check` limpo no repositório real. Efeito na árvore real hoje: nenhum (a cadeia atual está limpa).

## 4. Para aplicar (por ordem de Andraus)
1. `git apply` dos dois patches; 2. `python -m unittest tests/test_check_handoff.py` e a suíte completa; 3. atualizar `governance/MECANISMOS.json` (nota de `verificado_em` do mecanismo `check_handoff`); 4. (opcional, reservado) acrescentar o texto da regra ao `AGENTS.md` §11 com ata; 5. `check_coesao`, `check_rpsa`, mapa.
