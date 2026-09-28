# Rascunho — desenho de hooks de segurança para Claude Mem

**Status:** desenho não operacional. Nenhum hook foi adicionado ao repositório.

## Objetivo

Definir verificações que deverão ser avaliadas antes de habilitar o Claude Mem no ambiente local. O desenho não altera o atual `.claude/settings.json`.

## Pre-write / observation gate

Antes de permitir que uma observação seja persistida:

1. rejeitar padrões de secrets, tokens, chaves privadas e credenciais;
2. rejeitar caminhos `.env`, `secrets/`, dumps e arquivos privados;
3. rejeitar conteúdo classificado como `blocked`;
4. exigir `project_key`, tipo de registro e timestamp;
5. impedir que uma observação seja marcada como decisão homologada sem referência oficial;
6. emitir uma mensagem explícita de bloqueio, nunca um fallback silencioso.

## Post-write feedback

Após a gravação:

1. validar o registro contra o schema proposto;
2. verificar que o registro não foi escrito no working tree;
3. registrar hash e identificador da observação;
4. verificar classe de retenção;
5. produzir diagnóstico claro em caso de falha.

## Coexistência com o harness atual

- Não substituir `PreToolUse` ou `PostToolUse` existentes.
- Não desabilitar `scripts/gate-check.js`.
- Não alterar o comportamento do gate de specs.
- Não permitir que memória injete instruções acima de `AGENTS.md` ou da governança.
- Testar instalação e desinstalação em perfil isolado antes de uso no projeto.

## Testes mínimos propostos

- secret conhecido é bloqueado;
- arquivo `.env` é bloqueado;
- registro válido é aceito;
- registro com decisão aberta apresentada como fechada é bloqueado;
- falha do worker é reportada explicitamente;
- desinstalação não remove nem edita arquivos do repositório.
