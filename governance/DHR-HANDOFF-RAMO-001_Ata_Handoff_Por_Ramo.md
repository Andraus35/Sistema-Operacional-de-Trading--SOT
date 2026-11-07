# DHR-HANDOFF-RAMO-001 — Ata de Decisão — Handoff por ramo: entrada, ID e ciclo de vida

> Base: PROPOSTA-HANDOFF-ENTRADA-E-CICLO-DE-VIDA-2026-11-06 e PRETESTE-HANDOFF-2026-11-07 (pasta CONCORRENCIA-DE-SESSOES). Rascunho preservado na mesma pasta (INV-07).

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final (registro pelo Orquestrador) |
| Ref | Ordem de Andraus (chat, 2026-11-07): aprovou a direção e mandou redigir a ata e o texto, sem aplicar · `AGENTS.md` §10/§11 · PCC-001 / DHR-PCC-001 · Camada A (PR #159) |
| Data | 2026-11-07 |
| Status | **APLICADA por ordem de Andraus** (chat, 2026-11-07: "Assino a ata, aplicar em PR separado"), em PR **sem mesclar**; o merge segue com Andraus. **A migração do `HANDOFF.md` da raiz NÃO está aplicada** (ver §3-bis). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda só onde o estado de cada frente é escrito e como os IDs são numerados; não toca agentes, método nem a leitura obrigatória. |

## 1. Decisão proposta `[PROPOSTA]`
1. **Cada ramo tem o próprio handoff** em `handoffs/<ramo>.md`, com ID `HO-<AAAA-MM-DD>-<ramo curto>-<n>` (`ramo curto` = 7 primeiros caracteres depois de `ccr-`; `n` contado por ramo). IDs antigos permanecem (INV-07).
2. O **`HANDOFF.md` da raiz vira texto estático curto, sem tabela de frentes**: aponta para `handoffs/` e traz o roteiro "Reverificar ao vivo". Ninguém o edita no dia a dia (a tabela de frentes conflita: pré-teste S1b).
3. **Ao mesclar o PR do ramo**, o handoff final é movido, cópia exata, para `docs/handoffs/ramo-<ramo>/` e sai de `handoffs/`.
4. Instalar os detectores `HO-16` (ramo morto) e `HO-17` (formato do ID), só INFO, **é decisão separada** (patch pré-testado; exige `MECANISMOS.json`, COE-14).

## 2. Texto candidato para `AGENTS.md` §11 (NÃO aplicado)
Substituiria as 3 primeiras linhas da seção; as demais ficam como estão.
> - Antes de agir, o Orquestrador lê o **handoff da sua frente** (`handoffs/<ramo>.md`; em ramo novo, cria o seu) e o `HANDOFF.md` da raiz (texto estático com o roteiro "Reverificar ao vivo"), e executa esse roteiro; a realidade prevalece sobre o handoff. Sem handoff ou muito defasado: parar e reportar a Andraus.
> - Só o Orquestrador escreve o handoff da própria frente; é dado de estado — nunca registra homologação, fecha decisão aberta (CONS-01) nem concede permissão. Especificador devolve resultado ao Orquestrador; o Revisor segue somente leitura.
> - Entrega só está completa com o handoff **do ramo** reescrito (ID `HO-<data>-<ramo curto>-<n>`; anterior copiado sem alteração para `docs/handoffs/`, INV-07) no mesmo commit, e tudo empurrado ao ramo designado. Máx. 150 linhas. Ao mesclar o PR do ramo, o handoff final vai para `docs/handoffs/ramo-<ramo>/` e sai de `handoffs/`.
>
> *[texto anterior preservado — INV-07: "Antes de agir, o Orquestrador lê `HANDOFF.md` e executa sua seção 'Reverificar ao vivo'; a realidade prevalece sobre o handoff. Sem handoff ou muito defasado: parar e reportar a Andraus." · "Só o Orquestrador escreve o handoff; é dado de estado — nunca registra homologação, fecha decisão aberta (CONS-01) nem concede permissão. Especificador devolve resultado ao Orquestrador; o Revisor segue somente leitura." · "Entrega só está completa com o handoff reescrito (anterior copiado sem alteração para `docs/handoffs/HO-<id>.md`, INV-07) no mesmo commit, e tudo empurrado ao ramo designado. Máx. 150 linhas."]*

## 3. Passos de aplicação (só depois da assinatura; PR separado, sem mesclar)
1. Trocar as 3 linhas do `AGENTS.md` §11 pelo texto da §2 (texto anterior preservado).
2. **Migrar o conteúdo atual do `HANDOFF.md` da raiz** (HO-163, frente de logs, pauta e medições A5, ramo `ccr-a79e19ef-2zl738`) para handoffs/ccr-a79e19ef-2zl738.md (arquivo ainda a criar), com a cópia exata do HO-163 em `docs/handoffs/`. **Combinar antes com a sessão dessa frente.**
3. Reescrever o `HANDOFF.md` da raiz como texto estático (frontmatter e 11 seções mínimas, para o `check_handoff` não dar ERRO nas sessões sem handoff próprio; elas recebem só o `WARN HO-03`, que as empurra a criar o seu).
4. Mover para `docs/handoffs/ramo-<ramo>/` os handoffs de ramos já encerrados que ainda estão em `handoffs/` (hoje `ccr-4bd4e8a0-d92lc7.md`).
5. `python scripts/check_handoff.py`, `check_coesao`, suíte; registrar a classificação RPSA (`check_rpsa.py --register`); CATALOGO se Andraus mandar.

## 3-bis. Transição — o que este PR aplicou e o que não
- **Aplicado:** passo 1 (texto do `AGENTS.md` §11, texto anterior preservado), passo 4 (handoff de ramo encerrado movido para `docs/handoffs/ramo-<ramo>/`: o do ramo ccr-4bd4e8a0-d92lc7) e passo 5 (checagens e classificação RPSA).
- **NÃO aplicado:** passos 2 e 3 (migrar o handoff da raiz, que é o HO-163 da frente dos logs, e reescrever a raiz como texto estático). Dependem de combinar com essa frente. **Até lá a raiz continua com o handoff da frente dos logs** e o `AGENTS.md` já descreve a raiz como texto estático: sessões novas devem ler a raiz só pelo roteiro "Reverificar ao vivo" e criar o próprio `handoffs/<ramo>.md`.
- **Exceção temporária à regra de arquivar ao mesclar:** o handoff da frente de concorrência (handoffs/ccr-b7c09dc1-y4rafd.md) continua em `handoffs/` até o lembrete de medição (2026-11-14) ser concluído; o aviso de ramo morto (HO-16) não está instalado.
- **HO-16/HO-17 (detectores):** decisão separada, não instalados.

## 4. Evidência `[FATO]`
Na `main` de 2026-11-06 havia dois handoffs diferentes com o ID `HO-2026-11-01-157`; a raiz era de outra frente; os dois `handoffs/<ramo>.md` eram de ramos já apagados. Pré-teste: 2 ramos com arquivos próprios mesclam sem conflito; a tabela na raiz conflita; ramo novo sem arquivo próprio recebe `WARN HO-03` e ERRO=0.

## 5. Riscos
Migrar a raiz mexe no trabalho de outra frente; durante a transição coexistem os dois modelos (o código já aceita). O `HO-03` vira ruído enquanto sessões novas não criarem o próprio arquivo.

## 6. Registro
- [x] Assinatura de Andraus (chat) · [x] passos 1, 4 e 5 aplicados em PR · [ ] passos 2 e 3 (migração da raiz, depois de combinar com a frente dos logs) · [ ] merge (Andraus) · [ ] `MECANISMOS.json` só se instalar HO-16/HO-17 · [ ] CATALOGO
