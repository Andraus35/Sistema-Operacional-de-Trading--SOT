# Proposta pré-testada — A2.1: `mapa-projeto.json` fora da árvore versionada

> **Não normativo. NADA APLICADO.** Pré-teste autorizado por Andraus (chat, 2026-10-31). Aplicar exige nova ordem dele. Não fecha decisão aberta (CONS-01).

## O que muda
- `build_map.py --check` passa a ler o digest do `MAPA-PROJETO.md` (versionado) em vez do `.json`; o `.json` continua sendo gerado por `build_map.py`, mas como artefato local ignorado (`.gitignore`).
- `git rm --cached` do `.json` do mapa (−59.188 linhas, 1,66 MB da árvore; o arquivo some do diff de 126 de 211 commits).
- Patches: `PATCH-BUILD-MAP-JSON-LOCAL-*.patch`, `PATCH-TESTES-BUILD-MAP-*.patch`, `PATCH-GITIGNORE-*.patch`.

## Pré-teste (cópia isolada de `HEAD`)
`tests/test_build_map.py` 11/11 (1 teste novo: `--check` passa sem o `.json` e reprova após mudar um doc); `node tests/test-map-sync.js` todos passam; `--check` OK com e sem `.json`, e exit 1 após editar o ROADMAP. **Mutante** (`--check` ignora o digest) **morto**: 2 falhas. `git apply --check` limpo no repositório real.

## Riscos e o que NÃO foi testado
- CI (`ci.yml` l.186) e pre-commit só chamam `--check`: compatíveis. Não rodei o CI.
- Quem consumia o `.json` do repo (clone novo sem `.json`): só testes, que o geram. `.gitattributes` e `.rgignore` ficam com linhas inertes (limpeza opcional).
- O digest do `.md` guarda 16 hex; a comparação usa prefixo.

## Para aplicar (por ordem de Andraus)
1. `git apply` dos 3 patches; 2. `git rm --cached` do `.json` do mapa; 3. suíte completa + `node tests/test-map-sync.js`; 4. `build_map.py` e `--check`; 5. nota em `MECANISMOS.json` (COE-14) e `AGENTS.md` §5 (reservado).
