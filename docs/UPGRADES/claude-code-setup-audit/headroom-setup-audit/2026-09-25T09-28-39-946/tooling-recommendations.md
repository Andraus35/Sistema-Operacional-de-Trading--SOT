# Recomendações de ferramentas — Headroom

**Execução:** 2026-09-25 09:28:39 -0400  
**Status:** somente recomendação; nenhuma ferramenta foi instalada.

## Ordem recomendada para avaliação

### 1. Instalação isolada

Usar uma instalação fora do projeto:

```text
uv tool install --python 3.13 "headroom-ai[all]"
```

Alternativa para avaliação de biblioteca Python:

```text
pip install "headroom-ai[all]"
```

Não usar `npm install headroom-ai` esperando obter o CLI: o README upstream diferencia o SDK TypeScript do CLI Python.

### 2. Diagnóstico e benchmark

Ferramentas recomendadas:

```text
headroom doctor
headroom perf
```

Usar como corpus:

- arquivos RAG em `rag/`;
- schemas JSON em `schemas/`;
- saída dos validadores;
- logs de execução dos scripts;
- documentos normativos selecionados, apenas em modo de teste.

Métricas mínimas:

- tokens antes/depois;
- razão de compressão;
- preservação de termos normativos;
- recall de linhas críticas;
- latência;
- quantidade de recuperações integrais necessárias.

### 3. Primeiro modo de integração

**Recomendado:** proxy local ou wrapper em perfil descartável, não MCP permanente.

Motivo: proxy/wrapper permite medir o efeito com menor mudança na arquitetura do projeto. O MCP deve ser avaliado depois, pois adiciona ferramentas de recuperação que precisam entrar no protocolo cognitivo dos agentes.

### 4. Guardrails obrigatórios

Antes de qualquer uso recorrente, criar uma especificação aprovada para:

- conteúdo que não pode ser comprimido;
- conteúdo que exige CCR/retrieval;
- limiar mínimo de preservação;
- comportamento quando a recuperação falhar;
- proibição de `headroom learn` escrever automaticamente em `AGENTS.md`, `CLAUDE.md` ou arquivos de governança;
- retenção e localização do cache original;
- logs e auditoria da compressão.

### 5. Integração futura com MCP

Se o MCP for aprovado, documentar os papéis:

| Ferramenta | Uso controlado |
|---|---|
| `headroom_compress` | reduzir conteúdo não normativo ou já classificado |
| `headroom_retrieve` | recuperar original antes de concluir sobre evidência crítica |
| `headroom_stats` | observabilidade e medição de economia |

O agente não deve assumir que o resumo contém tudo. Para regras, decisões ou schemas, deve recuperar o original.

## Ferramentas complementares

- `uv` para instalação isolada do CLI;
- `headroom doctor` para diagnóstico;
- `headroom perf` para benchmark;
- tokenizer do provedor usado para medir tokens reais;
- scripts locais de comparação byte-a-byte para linhas críticas;
- CI separado para benchmark, sem bloquear o CI funcional até os critérios serem homologados.

## Decisão recomendada

Adotar o Headroom somente como **piloto externo e mensurável**. Não adicionar dependência ao `package.json`, não editar `.claude/settings.json`, não habilitar `headroom learn` e não inserir MCP no fluxo dos agentes antes de uma especificação de compressão e recuperação ser revisada e homologada.
