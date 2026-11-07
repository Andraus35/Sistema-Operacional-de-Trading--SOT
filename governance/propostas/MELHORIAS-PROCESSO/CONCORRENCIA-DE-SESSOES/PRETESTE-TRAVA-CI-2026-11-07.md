# Pré-teste da trava determinística "um PR por vez" no CI (nada instalado)

> **Não normativo. RESULTADO DE PRÉ-TESTE.** Andraus perguntou "é determinístico?" e escolheu pré-testar a trava no CI (chat, 2026-11-07). Rascunho da regra: RASCUNHO-ATA-UM-RAMO-UM-PR-2026-11-07 (mesma pasta). Instalar exige ordem expressa dele, ata assinada em `governance/` e o check entrar no ruleset. Não fecha decisão aberta (CONS-01).

## 1. O que foi construído (patch `PATCH-PR-UNICO-2026-11-07.patch`, **não instalado**)
- scripts/check_pr_unico.py (arquivo novo, só no patch) (sem rede; lê JSON da API): **U1 reprova** se existe um PR aberto **mais antigo** com o mesmo prefixo de sessão (`ccr-<8 hex>-<6 alfanum>`, qualquer sufixo); **U2 só avisa** se o PR toca apenas arquivos de handoff.
- Passo `One open PR per session` no `ci.yml`, só em `pull_request`, dentro do job que **já é o check obrigatório** (`Validate SOT Harness`): não precisa de novo check no ruleset. Entradas do GitHub passam por variáveis de ambiente (nada de `${{ github.head_ref }}` dentro do `run:`).
- Passo de teste no CI, entrada em `MECANISMOS.json` (estado `proposta`).

## 2. Resultados `[FATO]`
| Verificação | Resultado |
|---|---|
| tests.test_check_pr_unico | **12/12** |
| Mutantes (cache de bytecode desligado) | 8 testados; 7 mortos de saída, **1 sobreviveu (PR sem número) e ganhou teste**, depois morto |
| YAML do `ci.yml` | válido; passo na posição 7 de 45 |
| Paginação da API (trecho inline) | junta 2 páginas corretamente |
| `check_coesao` só com o patch | **ERRO=3** (COE-04/COE-14: DHR citada sem ata em `governance/`) |
| `check_coesao` com a ata em `governance/` | **ERRO=0** |
| `gate_manifest` | íntegro; `git apply --check` limpo na `main` |
**Reprodução com 30 PRs reais (#153–#182):** U1 teria bloqueado **1** (o #169, aberto 76 min depois do #167, mesma sessão). U2 teria avisado **5 dos 29** PRs mesclados que mexeram só em handoff (#171, #173, #176, #177, #179).

## 3. Falha de desenho achada e corrigida durante o teste
A 1ª versão era **simétrica**: um push no PR mais antigo, com o mais novo aberto, reprovaria os dois e travaria ambos. Agora **só o mais novo é travado**; o antigo segue livre para receber push e ser mesclado (teste e mutante cobrem isso).

## 4. Correção a um número anterior
O rascunho da regra dizia que a sessão criou "ramos simultâneos" (`-camada-a`, `-ledger`, `-mapa`). Medido: em 30 PRs só **1 par** da mesma sessão ficou aberto ao mesmo tempo. O excesso real foi **quantidade de PRs** (14 em uma sessão, ~5 só de handoff), não simultaneidade. Por isso a trava U1 sozinha ataca pouco; quem ataca o grosso é a regra R2 (sem PR só de handoff), e o U2 só a sinaliza como aviso.

## 5. O que continua não-determinístico
- **U2 é só aviso**: um PR só de handoff pode ser legítimo (arquivar ao fim da frente). Transformá-lo em falha exige exceção explícita (decisão de Andraus).
- **R1/R3/R4/R5** (mesclar quando o §10 permitir, acrescentar ao mesmo PR, arquivar ao fim da frente) são texto: dependem do agente.
- **Prefixo é heurística**: ramos fora do padrão (ex.: `claude/...`) escapam do U1.
- **U1 só vale na hora do CI**: depois que o PR antigo é mesclado, o PR novo precisa de novo push ou *Re-run jobs* para ficar verde.
- **Não testado no GitHub Actions real**: o passo `gh api` não rodou numa PR; só o script, a sintaxe e a paginação foram exercitados.

## 6. Para aplicar (só com ordem de Andraus; PR único)
1. Assinar a ata `DHR-UM-RAMO-UM-PR-001` e colocá-la em `governance/` (senão `COE-04/COE-14` reprovam). 2. `git apply` do patch. 3. Rodar a suíte e `check_coesao`. 4. Abrir um PR de teste e confirmar a falha do U1 com dois PRs da mesma sessão (único modo de provar o passo `gh api`). 5. Só então decidir se U1 vira check obrigatório do ruleset (já é, por estar no job obrigatório) e se U2 vira falha.
