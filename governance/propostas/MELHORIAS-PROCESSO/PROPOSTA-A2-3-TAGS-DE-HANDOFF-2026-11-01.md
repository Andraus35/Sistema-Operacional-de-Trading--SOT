# Proposta A2.3 — tags git por handoff no lugar das cópias (medida; NADA APLICADO)

> **Não normativo.** Retoma o item 2.3 da `PROPOSTA-A2-…` (adiado para depois do P11, já aplicado). Pedido por Andraus (AskUserQuestion, 2026-11-01: "Preparar a proposta"). Aplicar exige ordem dele (INV-07, PCC-001). Não fecha decisão aberta (CONS-01).

## 1. Medição (clone desta sessão, `ramo-ccr-d7f01e4e-c5qpb1`, 2026-11-01)
| Fato | Valor |
|---|---|
| Cópias em `docs/handoffs/*.md` | **149** (130 de 2026-10, 18 de 2026-11, +1); 6 subpastas `ramo-*`; pasta inteira **2,9 MB** |
| Tags no repositório (local e remoto) | **0** |
| **O clone é raso** (`git rev-parse --is-shallow-repository` = true) | **343 commits**; o histórico visível começa em 2026-10-18 (`b7cbf8f`) |
| Versões distintas de `HANDOFF.md` alcançáveis no histórico raso | 83 (menos que as 149 cópias: as anteriores a 2026-10-18 só existem como arquivo) |
| `git push --dry-run` de uma tag | aceito (**push real de tag não foi testado**: criaria algo público no repositório) |

## 2. O que a medição diz
1. **Tags não substituem as cópias em sessão de nuvem.** Com clone raso, uma tag que aponte para commit anterior ao corte não resolve (`git show HO-x:HANDOFF.md` falharia). O `check_handoff` HO-04, que hoje compara o handoff substituído com a cópia, passaria a depender de `git fetch --unshallow`/`--tags`, o que é mais pesado que ler um arquivo.
2. **O custo da cópia não é o espaço** (2,9 MB, uma fração do que o mapa já pesava) **nem o ritual de copiar**: é a numeração colidindo entre sessões em paralelo (já tratada pelo P11) e os erros de passo manual.
3. **Erros reais desta sessão no ritual do handoff** (todos meus, todos detectados por `check_handoff`/gate, nenhum chegou à `main`): `HO-04` por editar o handoff sem trocar o id (3 vezes), cópia arquivada que não bate com a versão commitada (1), `replace` silencioso que não gravou a atualização do handoff (2), e commit encadeado com `;` que empurrou o mapa defasado (1; o CI barrou). Isso é o custo médio por entrega, e é mecânico.

## 3. Recomendação (decisão de Andraus)
- **Não aplicar tags agora.** Ganho pequeno, risco médio (quebra de HO-04 em clone raso) e exige migrar 149 arquivos para `_legacy`.
- **Alternativa de maior retorno e baixo risco:** um utilitário informativo, a criar (nome sugerido: `novo_handoff`), que, num só passo, (a) copia o `HANDOFF.md` atual para `docs/handoffs/HO-<id>.md`, (b) troca `handoff_id`/`previous`/`data`/`base_commit`, (c) **falha alto** se algum texto a substituir não for encontrado (acaba o `replace` silencioso) e (d) roda `check_handoff`. Não decide conteúdo; só elimina os passos manuais que erraram. Pré-teste proposto: testes em repositório sintético, mutantes (id não trocado, cópia divergente, âncora ausente). Se aprovado, entra como utilitário em `MECANISMOS.json` (COE-14).
- **Opcional, higiene:** mover cópias com mais de N dias para `docs/_legacy/handoffs/` (nada deletado). Só se Andraus quiser menos arquivos na pasta quente.

## 4. Limites declarados
Não testei empurrar tag de verdade; não medi o tempo de `--unshallow` no ambiente de nuvem; as contagens são do clone desta sessão (raso).
