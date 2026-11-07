# RASCUNHO — DHR-UM-RAMO-UM-PR-001 — Ata de Decisão — Uma frente, um ramo, um PR por vez

> **RASCUNHO para Andraus ler, editar e assinar. NÃO vigora e NADA foi aplicado** (`AGENTS.md` §10 e §11 são arquivos reservados: só mudam com a ordem expressa dele). Fica em `propostas/` para não acionar o `rpsa-auto` nem o CATALOGO antes disso. Origem: pergunta de Andraus (chat, 2026-11-07): "O ideal é uma branch, um pull request e mesclar". Patch do aviso: PATCH-BR03-check-branches-2026-11-07 (mesma pasta; **não instalado**).

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final (registro pelo Orquestrador) |
| Ref | Ordem de Andraus (chat, 2026-11-07): redigir a regra resolvendo os 5 pontos de atrito, sem aplicar · `AGENTS.md` §10/§11 · DHR-HANDOFF-RAMO-001 · DHR-ASSINATURA-001 |
| Data | [preencher na assinatura] |
| Status | **PROPOSTA — vigora só com a ordem expressa de Andraus.** Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda só o fluxo de ramos e PRs das sessões; não toca agentes, método nem leitura obrigatória. |

## 1. Fato de partida `[FATO]`
Hoje **não existe regra** que limite ramos ou PRs abertos: o §10 só diz "PR é o meio" e o §11 manda um handoff por ramo. Desde 01/11 foram 27 PRs mesclados; só uma sessão abriu 14, cerca de 5 deles "só handoff", e criou ramos simultâneos (`-camada-a`, `-ledger`, `-mapa`) por causa de "PR separado". Cada PR a mais custa um ciclo de CI (~4 min) e, com o ruleset, deixa os outros desatualizados.

## 2. Decisão proposta `[PROPOSTA]`
**R1 — Uma frente = um ramo = um PR aberto por vez.** "PR separado" passa a significar **em sequência**: o próximo só abre depois de mesclar o anterior, reaproveitando o mesmo nome de ramo (`git checkout -B <ramo> origin/main`).
**R2 — O handoff vai no mesmo PR do trabalho.** Não se abre PR só para registrar o merge: o handoff diz "aguardando merge" e a próxima sessão reverifica ao vivo.
**R3 — Mesclar quando o §10 permitir.** Conteúdo operacional já aprovado: mesclar ao CI verde e informar. Conteúdo reservado (`AGENTS.md`, `governance/` normativo, `ROADMAP`, `.claude/agents/`, `canon/`): esperar a ordem expressa de Andraus.
**R4 — PR esperando ordem.** Se a nova tarefa é a mesma do PR, acrescentar commits no mesmo PR (o CI roda de novo). Se é outra tarefa, não abrir outro PR: aguardar ou perguntar a Andraus.
**R5 — Quando o handoff do ramo é arquivado.** Em vez de "ao mesclar o PR do ramo" (DHR-HANDOFF-RAMO-001 R3), **quando a frente termina**. Entre PRs da mesma frente o handoff do ramo continua em `handoffs/`.
**R6 — Frentes realmente paralelas** (ex.: logs e concorrência) podem ter um PR cada; cada frente com no máximo um.
**R7 — Aviso informativo `BR-03`** no `check_branches`: mais de um ramo remoto do mesmo prefixo de sessão (`ccr-<id>-<sufixo>`). Só avisa; não bloqueia.

## 3. Texto candidato (NÃO aplicado)
**`AGENTS.md` §10** — acrescentar ao fim da seção:
> **Um ramo, um PR por vez (DHR-UM-RAMO-UM-PR-001).** Cada frente trabalha em um ramo e mantém no máximo um PR aberto; "PR separado" significa em sequência (o próximo só depois de mesclar o anterior, no mesmo nome de ramo). O handoff vai no mesmo PR do trabalho; não se abre PR só para registrar o merge. PR com conteúdo reservado espera a ordem expressa de Andraus; se a nova tarefa é a mesma, acrescenta-se ao mesmo PR; se é outra, aguarda-se.

**`AGENTS.md` §11** — na 3ª linha, trocar a última frase:
> *de:* "Ao mesclar o PR do ramo, o handoff final vai para `docs/handoffs/ramo-<ramo>/` e sai de `handoffs/`."
> *para:* "Quando a **frente** termina (não a cada merge), o handoff final do ramo vai para `docs/handoffs/ramo-<ramo>/` e sai de `handoffs/`."

O texto anterior das duas passagens fica preservado em nota *[texto anterior preservado — INV-07]*.

## 4. Pré-teste do aviso BR-03 `[FATO]`
`tests.test_check_branches` **6/6** (3 testes novos); **4 mutantes mortos** (acusar com 1 ramo só; ignorar ramos com sufixo; deixar de contar o ramo atual; virar WARN); `gate_manifest --check` íntegro; `git apply --check` limpo na `main`. Não testado no GitHub real nem em clone de nuvem.

## 5. Efeitos e limites
- **Não há limite duro no GitHub** para PRs abertos; a regra vale por texto e aviso. Um workflow que reprove o CI por "PR demais" pode travar uma frente legítima: não proposto.
- **A frente fica mais lenta quando o PR espera ordem** (R4): é o preço da regra.
- Detecção só pelo prefixo do ramo, porque todos os PRs saem da conta de Andraus.
- A regra reduz ramos e PRs simultâneos; **não reduz** o número de merges nem o tempo de CI por PR.

## 6. Passos de aplicação (só depois da assinatura; PR único, sem mesclar sem ordem)
1. Aplicar os dois textos do §3 no `AGENTS.md` (texto anterior preservado). 2. Opcional e separado: instalar o `BR-03` (`git apply` do patch; `MECANISMOS.json` no mesmo PR, COE-14). 3. `check_handoff`, `check_refs`, `check_coesao`, `check_rpsa --register`; suíte. 4. Atualizar o handoff.

## 7. Registro
- [ ] Assinatura de Andraus · [ ] aplicar em PR · [ ] BR-03 (decisão separada) · [ ] CATALOGO
