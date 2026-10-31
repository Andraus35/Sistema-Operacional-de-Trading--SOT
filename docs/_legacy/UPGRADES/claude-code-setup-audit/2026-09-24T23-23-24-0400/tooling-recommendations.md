# Ferramentas recomendadas por funcionalidade

| Funcionalidade | Ferramenta existente/recomendada | Uso |
|---|---|---|
| Contexto principal do agente | `AGENTS.md` | Identidade, governança, mapa e não-negociáveis |
| Delegação especializada | `.claude/agents/*.md` | Especificação, revisão e validação independente |
| Workflows sob demanda | `.claude/commands/*.md` | Validação do harness e atualização de specs |
| Guardrail antes de escrita | `.claude/settings.json` + `scripts/gate-check.js` | Bloqueio de violações constitucionais |
| Feedback pós-edição | `scripts/post-edit-check.js` | Validação de JSON após edição |
| Validação de contratos | `npm test` | 11 schemas JSON |
| Lint de especificações | `npm run lint` | EARS e seções das 5 specs |
| Gate determinístico | `python scripts/validate_spec_sot.py <plan.md>` | Estrutura BASpec/Constitution/Enforcement |
| Avaliação de maturidade | `npx harness-score --json` | Score e lacunas do harness |
| Integração contínua | `.github/workflows/ci.yml` | Repetição automática das validações |
| Ambiente Copilot cloud | `.github/workflows/copilot-setup-steps.yml` (ausente) | Setup determinístico antes de sessões cloud |
| Distribuição como plugin | Manifesto Claude Code (ausente) | Empacotar para outros repositórios, se necessário |

## Recomendação de decisão

O setup atual já cobre operação local de Claude Code e possui maturidade alta. A única adição estrutural claramente indicada para o ambiente GitHub Copilot cloud é um workflow `copilot-setup-steps`; ele deve ser criado apenas quando esse ambiente fizer parte do fluxo operacional, pois a solicitação desta execução proibiu alterações de configuração.
