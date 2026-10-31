# Proposta pré-testada — demais cortes do AGENTS.md (§2, §5, §8, §9, §12)

> **Não normativo. PROPOSTA.** Nada foi aplicado em `AGENTS.md`. Por ordem de Andraus (chat, 2026-10-31) só o §7 foi cortado (`DHR-AGENTS-SEC7-001`); estes cortes **não** foram autorizados. Base: `.harness-eval/runs/2026-10-31-agents/11-mixed-apply.md` (KEEP/CUT dos dois juízes). Não fecha nem abre decisão (CONS-01).

## 1. O que o patch faz (somente `AGENTS.md`)
| Seção | Corte | Fica no AGENTS.md |
|---|---|---|
| §2 | árvore de diretórios (bloco cercado) | parágrafo do mapa + 1 linha com as pastas-chave |
| §5 | parágrafo "Sincronização documental" (1.347 B) | 1 linha com o comando e o papel de Detector |
| §8 | 7 comandos secundários (check_rpsa, check_invariants, check_handoff, check_coesao, revisor_gate, revisor_gate_mcp, loop_ledger) | comandos de uso diário + ponteiro a `governance/MECANISMOS.json` |
| §9 | texto do desenho do piloto do Auditor Externo | estado PAUSADO, regra de reativação e ponteiros |
| §12 | texto intermediário superado (DHR-ROTEAMENTO-005) | regra vigente do passo 0 intacta |
Efeito medido: **24.550 → 18.401 bytes (−6,1 KB, −25%)**; somado ao §7 já aplicado, o arquivo vai de 29.427 para 18.401 (−37%).

## 2. Pré-testes (feitos em cópia isolada, fora do repositório)
1. **Conservação:** `equiv_conservacao.py` → CONSERVADO, mas só depois de corrigir um defeito que **a própria prova pegou**: o corte do §12 é no meio de uma linha, e o arquivo morto tinha só o trecho removido; passou a guardar a **linha original completa**.
2. **Suíte completa:** 385 testes OK (inclui `test_check_invariants.TestFontes`, que falhou na aplicação do §7).
3. **Detectores na cópia:** `check_invariants` 0 achados; `check_refs` ERRO=0 (WARN=2, os mesmos reais); `check_doc_sync` 1 aviso (o de sempre); `check_rpsa` em sincronia; testes de hook OK.
4. **Limite do pré-teste:** a cópia não tem `.git`, então `check_handoff` (HO-02/03/04) e os avisos COE-11 não rodam de verdade — **repetir esses dois no repositório real ao aplicar**.
5. `git apply --check` no repositório real: aplica limpo.

## 3. Riscos e ressalvas
- **Modelo único:** os dois juízes do harness-eval usaram o mesmo modelo e a trilha C é sensível a ele; a skill recomenda checagem em segundo modelo antes de cortar mais de 30% de um arquivo (este patch + §7 = 37%). **Recomendo repetir a trilha C em outro modelo antes de aplicar.**
- O juiz cego declarou que não abriu os arquivos de sobreposição; a sobreposição foi conferida aqui por busca de referências e pelo `MECANISMOS.json`.
- §8: o `MECANISMOS.json` tem uma nota "Não citado no AGENTS.md §8" para um mecanismo; cortar comandos do §8 não a invalida, mas confira ao aplicar.
- Comandos removidos do §8 continuam documentados (MECANISMOS.json e arquivo morto); agentes que dependiam de vê-los no AGENTS.md passam a abrir o registro.

## 4. Para aplicar (por ordem de Andraus)
1. `git mv`/copiar `ARQUIVO-MORTO-AGENTS-cortes-2-5-8-9-12-2026-10-31.md` para `docs/_legacy/` (INV-07).
2. `git apply PATCH-AGENTS-cortes-2-5-8-9-12-2026-10-31.patch`.
3. `equiv_conservacao.py <AGENTS.md anterior via git show> AGENTS.md <arquivo morto>` → CONSERVADO.
4. Suíte completa, `check_invariants`, `check_doc_sync`, `check_handoff`, `check_coesao` (no repositório real), `check_rpsa --register` da nova ata (AGENTS.md é monitorado), `build_map`.
5. Ata curta citando a ordem de Andraus (AGENTS §10).
