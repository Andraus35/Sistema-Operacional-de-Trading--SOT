# Auditoria de setup Claude Code

**Execução:** 2026-09-24 23:23:24 -0400  
**Escopo:** levantamento somente leitura de configuração, ferramentas e oportunidades de melhoria.  
**Regra aplicada:** nenhum arquivo existente do repositório foi alterado; somente esta pasta de auditoria foi criada.

## Estado observado

- O repositório já possui uma base Claude Code funcional em `.claude/`, com 4 agentes, skills, comandos e hooks.
- O `harness-score` detectou `claude-code` e `cline`.
- O score geral foi **102/108 (94%)**, nível **Self-correcting**.
- `npm test` passou com **11/11 schemas**.
- `npm run lint` passou com **5/5 specs**.
- O plano [SPEC-001](../../specs/features/SPEC-001/plan.md) passou nos 10 checks estruturais.
- O plano [SPEC-019](../../specs/features/SPEC-019/plan.md) falhou em `STRUCT-10`: `L-001`, `J-001` e `K-001` foram interpretados pelo gate como decisões abertas sem marcador de pendência no contexto local. Isso conflita com o status baseline declarado no próprio plano e indica uma lacuna de precisão do detector/contexto, não uma alteração aplicada nesta execução.
- Não foi encontrado `.github/workflows/copilot-setup-steps.yml`.
- Não foi encontrado manifesto de plugin Claude (`.claude-plugin/plugin.json` ou equivalente). O conteúdo presente é configuração de projeto Claude Code, não um pacote de plugin distribuível.
- O comando `git status` não pôde ser usado porque a pasta não é um checkout Git nesta sessão.

## Achados e melhorias

### M-01 — Reprodutibilidade do ambiente Copilot ausente

**Prioridade:** Alta  
**Evidência:** não existe `.github/workflows/copilot-setup-steps.yml`; o CI atual configura Node 20 e executa `npm test`, `npm run lint` e `npx harness-score`, mas isso não é automaticamente reutilizado pelo ambiente do Copilot cloud agent.

**Melhoria indicada:** adicionar, em uma mudança futura explicitamente aprovada, um workflow `copilot-setup-steps` com `actions/setup-node@v4`, Node 20 e instalação determinística das dependências. O workflow deve permanecer separado do CI normal e usar permissões mínimas.

**Ferramentas recomendadas:** GitHub Actions, `actions/setup-node`, `npm ci`; considerar `actions/cache` apenas se houver benefício mensurável.

### M-02 — Regras Cline sem frontmatter de ativação

**Prioridade:** Média  
**Evidência:** o `harness-score` marcou `CTX-04` como falho para `.clinerules/sot-rag.md`, `.clinerules/sot-schemas.md` e `.clinerules/sot-specs.md`; score perdido: 3 pontos.

**Melhoria indicada:** declarar metadados de ativação compatíveis com o formato aceito pelo Cline, preferencialmente escopo por caminho. Não aplicar automaticamente, pois isso alteraria arquivos existentes.

**Ferramentas recomendadas:** Cline rules frontmatter; validar novamente com `npx harness-score --json`.

### M-03 — Comando de validação referencia relatório possivelmente ausente

**Prioridade:** Média  
**Evidência:** `.claude/commands/validate-harness.md` exige verificar `HARNESS-REPORT.md`, enquanto o inventário atual mostra somente referências históricas em `docs/_legacy/` e nos runs de avaliação.

**Melhoria indicada:** escolher explicitamente entre atualizar o comando para apontar ao catálogo/artefato vigente ou restaurar um relatório canônico com governança clara. Evitar que o agente trate um artefato histórico como fonte operacional.

**Ferramentas recomendadas:** comando Claude Code dedicado, `harness-score`, `scripts/validate_spec_sot.py`.

### M-04 — Gate estrutural tem sensibilidade a contexto local de decisões

**Prioridade:** Alta  
**Evidência:** [SPEC-019](../../specs/features/SPEC-019/plan.md) declara L-001 fechada e J-001/K-001 como decisões abertas, mas o `STRUCT-10` falhou por não reconhecer a marcação de estado no contexto examinado.

**Melhoria indicada:** em mudança futura, melhorar a heurística do gate para distinguir `FECHADA`, `ABERTA`, `PENDENTE` e menções históricas, com testes de regressão para IDs de decisão. Não desabilitar o check.

**Ferramentas recomendadas:** testes unitários do `validate_spec_sot.py`, fixtures de planos, CI.

### M-05 — Setup Claude Code é local, não um plugin distribuível

**Prioridade:** Baixa  
**Evidência:** há `.claude/settings.json`, `.claude/agents/`, `.claude/commands/` e `.claude/skills/`, mas não há manifesto de plugin.

**Melhoria indicada:** se a intenção for distribuir isso como plugin para outros repositórios, criar posteriormente uma estrutura de plugin e documentar o contrato de instalação. Se a intenção for apenas operar neste repositório, a estrutura atual é suficiente e não requer plugin adicional.

**Ferramentas recomendadas:** Claude Code plugin manifest, empacotamento/versionamento, smoke test em repositório limpo.

## Não achados relevantes

- Hooks de `PreToolUse` e `PostToolUse` existem e referenciam scripts presentes.
- O teste de schemas, lint de specs, type checking (`tsconfig.json`) e formatter (`.prettierrc`) estão identificáveis.
- O workflow CI já fixa Node 20 e executa as validações principais.
- Não foram instaladas dependências nem executados comandos de escrita sobre o projeto.

## Ordem sugerida de tratamento

1. M-04: corrigir a precisão do gate, preservando o bloqueio constitucional.
2. M-01: adicionar setup determinístico do Copilot somente se o ambiente cloud agent for realmente usado.
3. M-02: melhorar ativação das regras Cline.
4. M-03: alinhar o comando de validação com o artefato canônico vigente.
5. M-05: somente se houver objetivo explícito de distribuição como plugin.
