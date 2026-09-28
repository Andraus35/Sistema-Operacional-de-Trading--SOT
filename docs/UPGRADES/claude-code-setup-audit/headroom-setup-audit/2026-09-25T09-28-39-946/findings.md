# Auditoria de compatibilidade — Headroom

**Execução:** 2026-09-25 09:28:39 -0400  
**Fonte externa analisada:** [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)  
**Regra aplicada:** nenhum arquivo existente do repositório foi alterado.

## Resumo executivo

O Headroom é tecnicamente compatível com o objetivo do SOT Harness de reduzir custo de contexto, especialmente em saídas de ferramentas, logs, arquivos e RAG. O repositório já trata economia de tokens e contexto como preocupações governadas, mas não possui integração Headroom instalada.

O melhor encaixe inicial não é editar o código do harness nem adicionar uma dependência de runtime ao projeto. É testar o Headroom externamente, em modo proxy ou wrapper, com um benchmark de fidelidade e economia antes de qualquer adoção permanente.

## Capacidades relevantes do Headroom

Segundo o README upstream, o Headroom oferece:

- biblioteca Python e SDK TypeScript;
- proxy local com `headroom proxy`;
- wrapper para agentes como Claude, Codex, Copilot, Cursor e Cline;
- MCP server com `headroom_compress`, `headroom_retrieve` e `headroom_stats`;
- compressão de JSON, código e texto;
- cache local dos originais com recuperação sob demanda;
- recursos de memória cross-agent e `headroom learn`;
- execução local, mantendo o conteúdo no ambiente local durante a compressão.

## Compatibilidade com este repositório

### Compatibilidade positiva

- [package.json](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/package.json) já possui comandos de validação e avaliação.
- [.claude/settings.json](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/.claude/settings.json) possui hooks que devem permanecer ativos.
- [RULES.md](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/governance/RULES.md) já menciona economia de tokens, `stable_prefix` e contexto.
- O repositório tem RAG e schemas que podem servir como corpus de benchmark.
- O CI fixa Node 20, compatível com o requisito declarado pelo Headroom.

### Lacunas atuais

- Não há dependência Headroom em `package.json`.
- Não há configuração de proxy, MCP ou wrapper do Headroom.
- Não há benchmark de tokens antes/depois.
- Não há teste de preservação de conteúdo crítico após compressão.
- Não há política explícita para diferenciar conteúdo comprimível de conteúdo que deve permanecer integral.
- Não há decisão homologada sobre uso de `headroom learn`, memória cross-agent ou escrita automática em `AGENTS.md`/`CLAUDE.md`.

## Achados

### H-01 — Boa aderência à camada de economia de tokens

**Prioridade:** Alta  
**Impacto:** O Headroom pode complementar diretamente as preocupações já existentes na camada meta de economia e roteamento.

**Recomendação:** avaliar primeiro como ferramenta externa de observabilidade e proxy, sem incorporá-lo ao harness normativo.

### H-02 — Risco de compressão alterar evidência normativa

**Prioridade:** Crítica  
**Impacto:** Este repositório contém constituição, regras, decisões abertas, schemas e specs onde uma omissão pode mudar o sentido. Compressão não pode ser considerada semanticamente neutra apenas por preservar respostas médias.

**Recomendação:** marcar como não comprimíveis, ou sempre recuperáveis integralmente, os seguintes conteúdos:

- `AGENTS.md`, `ROADMAP.md` e `atomic-spec.md`;
- `governance/`, `canon/` e decisões/homologações;
- schemas JSON;
- planos e checks de Specs em revisão;
- trechos que contenham `DEVE`, `NÃO DEVE`, `MUST`, `SHALL`, `J-001`, `CONS-01`, `INV-*` ou `RULE-*`.

### H-03 — CCR/retrieval precisa de teste de completude

**Prioridade:** Alta  
**Impacto:** O Headroom mantém originais localmente e permite recuperação sob demanda. Se o agente não chamar `headroom_retrieve` quando necessário, pode trabalhar sobre uma visão resumida.

**Recomendação:** criar um teste externo com perguntas cuja resposta depende de uma linha crítica, medir recall e confirmar que a recuperação devolve o original correto.

### H-04 — Proxy/wrapper pode interferir no fluxo de hooks

**Prioridade:** Alta  
**Impacto:** O repositório usa `PreToolUse` e `PostToolUse`. O wrapper do Headroom também pode instalar/configurar componentes do agente e, segundo a documentação, algumas rotas podem registrar ferramentas auxiliares. Há risco de ordem, duplicidade ou alteração de configuração.

**Recomendação:** testar em perfil isolado e verificar que `.claude/settings.json`, `gate-check.js` e `post-edit-check.js` continuam sendo executados.

### H-05 — `headroom learn` pode produzir escrita fora da governança

**Prioridade:** Alta  
**Impacto:** O README informa que `headroom learn` pode escrever correções em `CLAUDE.local.md`, `CLAUDE.md`, `AGENTS.md` ou equivalentes. Isso conflita potencialmente com o regime spec-first e com a necessidade de homologação.

**Recomendação:** não habilitar `headroom learn` para este repositório sem uma regra explícita: saída deve ser apenas relatório/proposta, nunca alteração automática em arquivos normativos.

### H-06 — Dependências operacionais adicionais

**Prioridade:** Média  
**Impacto:** O caminho CLI usa Python/uv e pode envolver Bun, além do Node já presente. Isso aumenta a superfície de setup e CI.

**Recomendação:** não instalar `headroom-ai[all]` no projeto inicialmente. Preferir uma instalação isolada via `uv tool` em ambiente de avaliação.

## Veredito

**Apropriado para piloto controlado, não para ativação imediata no repositório.**

O Headroom parece bem alinhado com a meta de economia de tokens, mas sua compressão deve ser subordinada à preservação de evidência e à governança existente. O primeiro piloto deve medir:

1. redução real de tokens;
2. preservação de regras e linhas críticas;
3. recall após `headroom_retrieve`;
4. integridade dos hooks Claude Code;
5. ausência de escritas automáticas em artefatos normativos.
