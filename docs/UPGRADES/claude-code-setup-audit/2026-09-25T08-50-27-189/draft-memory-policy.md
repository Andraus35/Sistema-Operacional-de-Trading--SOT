# Rascunho — Política de memória Claude Mem para o SOT

**Status:** proposta não homologada  
**Operacional:** não  
**Escopo:** uso opcional do `thedotmack/claude-mem` no ambiente local do Claude Code.

## 1. Princípio de autoridade

A memória persistente é uma camada auxiliar de contexto. Ela não é fonte normativa, não fecha decisões abertas e não pode substituir `AGENTS.md`, `ROADMAP.md`, `atomic-spec.md`, `governance/`, `canon/` ou os gates determinísticos.

Quando houver conflito entre uma memória recuperada e um artefato normativo do repositório, o artefato normativo prevalece.

## 2. Conteúdo permitido

Pode ser armazenado, sujeito a filtragem:

- resumo de sessões técnicas;
- decisões humanas já registradas em artefatos oficiais;
- resultados de testes e validações;
- histórico de bugs e correções;
- referências a arquivos e símbolos;
- contexto de trabalho que não contenha dados sensíveis.

## 3. Conteúdo proibido

Não deve ser persistido:

- tokens, API keys, senhas, cookies ou credenciais;
- chaves privadas, certificados privados ou secrets de CI;
- dados pessoais desnecessários;
- conteúdo de arquivos `.env`, dumps ou bancos de dados;
- memória que tente transformar uma decisão aberta em decisão fechada;
- ordens, credenciais de execução ou instruções para operar mercados.

## 4. Retenção

Classes propostas:

| Classe | Uso | Retenção sugerida |
|---|---|---|
| `short` | contexto operacional temporário | 30 dias |
| `standard` | decisões e resultados técnicos | 180 dias |
| `review-required` | material sensível ou ambíguo | até revisão humana |

Os prazos são propostas e não devem ser tratados como política aprovada antes de homologação.

## 5. Recuperação e citações

Memórias recuperadas devem ser tratadas como observações com proveniência. O agente deve confirmar informações relevantes contra o repositório atual antes de usá-las em uma entrega.

## 6. Exclusão e exportação

Exclusão, exportação ou sincronização em nuvem exigem aprovação humana explícita. Dados de memória não devem ser adicionados automaticamente ao Git.

## 7. Critérios de ativação

Antes de ativar o plugin:

1. validar a coexistência dos hooks do plugin com `.claude/settings.json`;
2. testar filtragem de secrets em perfil descartável;
3. confirmar o diretório de armazenamento e suas permissões;
4. registrar versão do plugin e runtime;
5. executar um teste de recuperação sem alterar artefatos do projeto.
