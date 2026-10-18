# Lista — ramos remotos e PRs candidatos a limpeza (2026-10-18)

> **[PROPOSTA] — só lista; nada foi fechado, apagado ou mesclado.** A decisão é de Andraus. Contagens: commits que o ramo tem a menos/mais que a `main` (`git rev-list --left-right --count origin/main...ramo`) em 2026-10-18, após o PR #118.

## Ramos totalmente contidos na `main` (0 commits próprios) — candidatos seguros a apagar
`assinatura-delegacao-merge` · `ccr-63ea68aa-ks4bkd` (a linha da SPEC-006 integrada pelo #118) · `ccr-7917ac44-2l55cz` · `ccr-a5f30778-9nezl9` · `ccr-d43bf9b0-h336k5` · `claude/new-session-ch6cqa` · `f3-aplicacao` · `gate-detectores` · `revisor-modelo-metodo-v2` · `revisor-passo8-i001-l001` · `rpsa-registra-013-assinatura` · `spec006-abertura-homologada`

## Ramos com commits próprios (revisar antes de qualquer decisão)
| Ramo | Commits próprios | Observação |
|---|---|---|
| `spec006-plan` | 10 | linha antiga da SPEC-006 (Plan v1.4–v1.6); o Plan v1.8 e os pareceres 5–9 foram arquivados em `governance/propostas/SPEC-006/linha-spec006-plan/` pelo #118 |
| `ccr-3a0d581c-6cj4ig` | 2 | "Teste A" do roteamento de modelos |
| `ccr-60575b67-ffmqlh` | 9 | Plan candidato da SPEC-002 + registro RULE-REG-001 (28/09) |
| `spec-006-abertura` | 37 | abertura **proposta** da SPEC-006 (05/10); a homologada já está na `main` |
| `auditor-externo-integracao` | 80 | **PR #31 (aberto)** — Auditor Externo, hoje PAUSADO (AGENTS §9) |
| `ccr-e3c0fb7e-63d2l9` | 18 | **PR #2 (aberto)** — capturas verbatim parciais da SPEC-003 (30/09), SPEC-003 já homologada |
| `ccr-f02efedf-w33g38` | 88 | OPERACAO.md do Auditor Externo (V4 ao vivo) |
| `ferramentas-estresse` | 99 | marcado "NUNCA mesclar" no próprio commit |

## PRs abertos
- **#31** `auditor-externo-integracao` — obsoleto se o Auditor Externo continuar PAUSADO.
- **#2** `ccr-e3c0fb7e-63d2l9` — obsoleto (SPEC-003 homologada).
