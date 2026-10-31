# Proposta pré-testada — prova de conservação para enxugar documentos quentes (A5 / H1–H3)

> **Não normativo. PROPOSTA.** Nada foi aplicado em `AGENTS.md`, `ROADMAP.md` nem em `scripts/`. Não fecha decisão aberta (CONS-01). Segue `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` (A5, B3). Atende à regra de Andraus (2026-10-31): corte de leitura só com check de equivalência e arquivo à parte (INV-07).

## 1. A ferramenta (`equiv_conservacao.py`, 70 linhas, não instalada)
Regra de conservação: **toda linha não vazia do original existe, como multiconjunto e com espaços normalizados, no documento enxuto ou no arquivo morto**. Linhas novas (ponteiros) são permitidas. Se faltar linha, lista a perdida e a **mais parecida** (pega número alterado, ex.: "1:3" virou "1:2"). É Detector (ENF-03): não decide o que pode ser enxugado.
- **Pré-teste:** 8 testes (mover conserva; CRLF/espaços não contam; linha apagada reprova; valor alterado reprova e aponta a parecida; duplicata exige 2 cópias; célula longa truncada reprova; arquivo vazio reprova). 8/8 OK.
- **Ataque por mutação à própria ferramenta:** 4 mutações (multiconjunto→conjunto, sem normalizar espaços, ignorar arquivo morto, sempre conservado) — **4/4 mortas**.

## 2. Simulação no AGENTS.md §7 (medida)
- §7 atual: **5.890 bytes**; ponteiro proposto: **336 bytes** (≈ −5,5 KB, ≈ 1,4 mil tokens por sessão e por subagente).
- Texto integral preservado em `ARQUIVO-MORTO-AGENTS-secao7-2026-10-31.md` (esta pasta).
- Resultado da prova: **CONSERVADO**. Controle negativo (arquivo morto sem a seção): **PERDA de 6 linhas**, como deveria.
- **Teste de duplicação (o que a conservação sozinha não prova):** o §7 cita 55 IDs; **53 já aparecem no `ROADMAP.md`**. Os 2 que não aparecem (`DHR-BENCH-INTEL-001`, `DHR-DOCSYNC-003`) são notas de auditoria das próprias correções do AGENTS — ficam no arquivo morto, não no ROADMAP. Conclusão: o §7 é duplicado do ROADMAP em substância; o ponteiro não perde estado de decisão.
- Ponteiro sugerido para o §7: "O estado das decisões (abertas e fechadas) vive SÓ no `ROADMAP.md` (linhas 'Decisões abertas ativas' e 'Decisões FECHADAS'). Nenhuma decisão aberta pode aparecer como invariante fechado (CONS-01). Histórico integral desta seção: arquivo morto."
- **Efeito colateral a tratar na aplicação:** `check_doc_sync`, `check_invariants` e `check_handoff` leem o AGENTS.md; rodar a suíte inteira e `check_doc_sync` antes e depois (a classe de achado "§7 × ROADMAP" some, que é o ganho).

## 3. ROADMAP — o que a simulação mostrou (NÃO é só mover)
Só 2 linhas passam de 1.500 bytes (11.658 B, 15% do arquivo): **linha 34 "Próximo trabalho autorizado"** e **linha 37 "Decisões FECHADAS"** (9.894 B). A conservação passa se elas forem para arquivo morto, **mas são estado vivo** (o que está autorizado agora e o que já foi decidido). Arquivá-las inteiras tiraria do caminho quente informação que o agente precisa. **Recomendação:** não aplicar corte mecânico; Andraus (ou o Especificador por ordem dele) decide **por julgamento** quais entradas da linha 37 são histórico (fechadas há muito) e quais são restrição vigente; a ferramenta então prova que nada se perdeu. Ganho potencial ≤ 11 KB (≈ 2,9 mil tokens/chamada), mas só após esse julgamento.

## 4. Para aplicar (por ordem de Andraus) — só o §7 do AGENTS
1. `git mv`/copiar o arquivo morto para `docs/_legacy/` (INV-07) e substituir o §7 pelo ponteiro.
2. `python governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/equiv_conservacao.py <AGENTS.md anterior (git show)> AGENTS.md <arquivo morto>` → deve imprimir CONSERVADO.
3. Suíte completa, `check_doc_sync`, `check_handoff`, `check_rpsa --register` se a regra de carimbo do AGENTS exigir (AGENTS.md é monitorado), `build_map`.
4. Decidir se a ferramenta vira script oficial (exigiria registro em `MECANISMOS.json`, COE-14) ou fica como utilitário de proposta.
