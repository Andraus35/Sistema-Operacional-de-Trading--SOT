# DHR-MAPA-GERADO-001 — Ata de Decisão — Mapa do projeto gerado, não versionado

> Pré-teste: PROPOSTA-MAPA-2026-11-01 (pasta CONCORRENCIA-DE-SESSOES, ramo ccr-b7c09dc1-y4rafd).

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final (registro pelo Orquestrador) |
| Ref | Ordem de Andraus (chat, 2026-11-01): "pré-testar o mapa primeiro" · `AGENTS.md` §5/§10 · BL-019 · PROPOSTA-MAPA-2026-11-01 |
| Data | 2026-11-01 |
| Status | **APLICADA por ordem de Andraus** (chat, 2026-11-01: "Assino, aplicar em PR separado"), em PR **sem mesclar**; o merge segue com Andraus. Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda onde o mapa vive (gerado, não versionado); não toca agentes, método nem a lista de leitura obrigatória. |

## 1. Decisão proposta `[PROPOSTA]`
`docs/mapa/MAPA-PROJETO.md` deixa de ser versionado: entra no `.gitignore` (como o `.json` já está desde A2.1) e passa a ser **saída gerada** por `python scripts/build_map.py`.

## 2. O que muda
1. `.gitignore` + `git rm --cached docs/mapa/MAPA-PROJETO.md`.
2. `ci.yml`: passo "Generate project map" logo após o Setup Python (os testes de gate chamam `--check` mais cedo no job). `.pre-commit-config.yaml`: gerar e checar.
3. `AGENTS.md` §5 (parágrafo "Mapa do projeto"): trocar "hooks regeneram… CI e pre-commit bloqueiam com `--check`" por "mapa é gerado localmente pelos hooks e pelo CI; não é commitado". BL-019: registrar a mudança.
4. **Não altera** `build_map.py`, `pre_entrega.py`, `run_gates.py`, `revisor_gate.py` (selados). `--check` passa a provar geração, não frescor de arquivo commitado.

## 3. Evidência `[FATO]`
Clone novo da `main` pós-#159: sem mapa `--check`=2; após gerar `--check`=0; `gate_manifest` íntegro; 22 testes OK; 2 ramos com `.md` distintos mesclam sem conflito. Não testado no GitHub Actions real.

## 4. Riscos
Leitor do GitHub não vê o mapa pronto; sessão sem Python/hook fica sem mapa até gerar (o `--check` reprova, não passa em falso).

## 5. Registro
- [x] Assinatura de Andraus (chat) · [x] aplicado em PR · [x] `MECANISMOS.json` (COE-14) · [ ] merge (Andraus) · [ ] CATALOGO
