# Proposta pré-testada — falsos positivos do check_refs e destino do mapa JSON

> **Não normativo. PROPOSTA.** Nada foi aplicado em `scripts/` nem em `governance/GATE-MANIFEST.sha256`. Segue a auditoria `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` (itens B10 e B1). Não fecha decisão aberta (CONS-01).

## 1. Patch do `check_refs.py` (B10)
- **Por que não foi aplicado:** `scripts/check_refs.py` consta no `.github/CODEOWNERS` e no selo `governance/GATE-MANIFEST.sha256`; o HANDOFF o lista em "Não tocar". Aplicar exige ordem de Andraus e regravar o selo.
- **O que muda (6 linhas):** (a) ignora placeholder de numeração `RULE-XXX-0NN`; (b) ignora caminho absoluto fora do repositório (ex.: o README do proxy do ambiente); (c) comando `wc|cat|head|tail` usa o último argumento como caminho.
- **Pré-teste (feito em cópia isolada, fora do repositório):**
  1. 5 testes novos em `tests/test_check_refs.py`: 3 reproduzem os falsos positivos reais e **falham no script atual**; 2 garantem que regra real sem definição (`RULE-ZZ-99`) e caminho relativo inexistente **continuam alertando**.
  2. Com o patch: 20/20 testes passam; sem o patch: 3 falham (prova de que testam algo).
  3. Efeito na árvore real: WARN **6 → 2**; os 2 restantes são reais (`RULE-REV-01` sem definição; um caminho antigo do handoff em PROPOSTA congelada). ERRO continua 0; INFO 327 → 325.
- **Arquivos:** `PATCH-CHECK-REFS-FALSOS-POSITIVOS-2026-10-31.patch` e `PATCH-CHECK-REFS-TESTES-2026-10-31.patch` (aplicar com `git apply` a partir da raiz).
- **Para aplicar (por ordem de Andraus):** aplicar os dois patches → `python -m unittest tests/test_check_refs.py` → `python scripts/gate_manifest.py` regravando o selo (ou o fluxo que a DHR-AUDITOR-EXTERNO-015 define) → `python scripts/check_coesao.py` → suíte completa → atualizar a nota de `verificado_em` do mecanismo em `governance/MECANISMOS.json` no mesmo PR (COE-14).

## 2. Mapa JSON fora da árvore (B1) — achado de consumidores
Quem lê `docs/mapa/mapa-projeto.json` (busca em scripts, testes, CI, hooks): `scripts/build_map.py`, `tests/test_build_map.py`, `tests/test-map-sync.js` e, só como evidência antiga, `.claude/skills/harness-eval/runs/2026-09-26-full/`. Portanto **não é um simples "tirar do git"**: exige mudar `build_map.py` (CODEOWNERS), o modo `--check` (CI e pre-commit comparam o JSON) e dois testes. **Recomendação:** adiar; ganho (ruído de diff) menor que o risco de quebrar o `--check`. Alternativa de baixo risco: manter o JSON e só marcá-lo como gerado no `.gitattributes` (`linguist-generated`, esconde do diff do GitHub) — não alterado aqui.
