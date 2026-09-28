# MANIFESTO DE REORGANIZAÇÃO — SOT-Harness

**Data:** 2026-09-14
**Executor:** Especificador (Claude Code)
**Objetivo:** (1) aplicar as decisões do Questionário de Resolução v1; (2) reorganizar o repositório em estrutura documental MD para cognição/busca de agente; (3) provar que nada se perdeu; (4) eliminar legados (após confirmação).
**Fonte-arquivo intacta:** `DOCUMENTOS INICIAIS/` (diretório-pai) **não foi alterado** — apenas lido/copiado.

---

## 1. Estrutura final

```
raiz/
├── ROADMAP.md · ATOMIC-SPEC.md · AGENTS.md · GLOSSARIO.md · README.md   (leitura/entrada)
├── governance/   CONSTITUTION · RULES · CONFLICT-MAP · CATALOGO-OFICIAL
├── canon/        CHM-001 · CEM-001 · CEE-001 v2.0 · GMC-001 · SDD-001 · PPQ-001 · SAS-001 · CR-001
├── fundamentos/  KERNEL-V2 · ENGENHARIA-GERAL · ARIA-plano-mestre · AUDITORIA-ideias
├── arranque/     questionario-resolucao-v1 · respostas-questionario-v1 · MANIFESTO (este)
├── specs/ · rag/ · schemas/   (harness 1ª geração — corrigido; ref. até SPEC-010…014)
├── .claude/ · .clinerules/ · scripts/ · tests/ · .github/   (máquina)
└── docs/_legacy/ (staging de exclusão)
```

## 2. Movimentações (origem → destino) — lossless (mv/cp)

| Origem | Destino | Tipo |
|---|---|---|
| `validate_spec_sot.py` (raiz) | `scripts/validate_spec_sot.py` | move (Q-013) |
| `ESPECIFICADOR.md` (raiz) | `.claude/agents/especificador.md` | move (Q-013) |
| `REVISOR.md` (raiz) | `.claude/agents/revisor.md` | move (Q-013) |
| `CONSTITUTION.md` (raiz) | `governance/CONSTITUTION.md` | move |
| `RULES.md` (raiz) | `governance/RULES.md` | move |
| `CONFLICT-MAP.md` (raiz) | `governance/CONFLICT-MAP.md` | move |
| `.specs/arranque/questionario-resolucao-v1.md` | `arranque/questionario-resolucao-v1.md` | move |
| `~/Downloads/respostas-questionario-v1.md` | `arranque/respostas-questionario-v1.md` | cópia (registro) |

## 3. Consolidações (novos artefatos, conteúdo preservado)

| Novo artefato | Origem consolidada |
|---|---|
| `canon/CHM-001-*.md` | `DOCUMENTOS INICIAIS/02_Modelos_Canonicos/CHM-001_Capitulo1..4.md` |
| `canon/CEM-001-*.md` | `.../02_Modelos_Canonicos/CEM-001_Versao_Consolidada.md` |
| `canon/CEE-001-*-v2.0.md` | `.../01_Governanca_Geral/CEE-001_Versao_Consolidada.md` + **emenda v2.0** (§11 Salvaguardas de Sinal, Q-003; §12 4Es, Q-009) |
| `canon/GMC-001 · SDD-001 · PPQ-001` | `.../01_Governanca_Geral/*_Versao_Consolidada*.md` |
| `canon/SAS-001-*.md` | `.../03_Agentes_Especializados/SAS-001_Cap1 + Cap3 + Caps_2_4_5_6_7` |
| `canon/CR-001-*.md` | `.../04_Compliance_Record_CR-001/CR-001_Capitulo6/7/8_*.md` |
| `fundamentos/KERNEL-V2.md` | texto extraído de `KERNEL V2.docx.pdf` (pypdf) |
| `fundamentos/ENGENHARIA-GERAL.md` | texto extraído de `ENGENHARIA GERAL.pdf` (pypdf) |
| `fundamentos/AUDITORIA-ideias-*.md` | texto extraído de `AUDITORIA DE IDEIAS NÃO IMPLEMENTADAS.pdf` (pypdf) |
| `fundamentos/ARIA-plano-mestre.md` | cópia de `ARIA_Plano_Mestre.md` |
| `governance/CATALOGO-OFICIAL.md` | atualização de `CATALOGO_OFICIAL_ORYX.md` (Q-001/Q-010/Q-011) |
| `AGENTS.md` (consolidado) | fusão de `AGENTS.md` (EN) + `AGENTSV2.md` (PT) + mapa da nova estrutura |

## 4. Prova de "nada se perdeu" — justificativa de cada legado

| Legado (staging `docs/_legacy/`) | Conteúdo preservado em |
|---|---|
| `AGENTSV2.md` | **Fundido** em `AGENTS.md` (identidade, paths, profiles, fluxo, decisões abertas, gate). |
| `HARNESS-REPORT.md` (snapshot v2.0, 09/09) | Inventário de fontes → `fundamentos/` + `governance/CATALOGO-OFICIAL.md`; GAPs (Event Bus/KG/Blackboard/pattern_memory) → `ROADMAP.md` (SPEC-004/005/006/009/017); resultados de validação → reproduzíveis por `npm test`/`lint`. É um relatório datado, não normativo. |
| `PROMPT_HARNESS_ESPECIFICACAO.md` / `_1.md` | Prompts originais de geração do harness (histórico de processo). O produto desses prompts é o próprio repositório; nenhum conteúdo normativo exclusivo. |
| **Antigo `AGENTS.md` (EN, sobrescrito)** | "Spec conventions" (EARS, citação de fonte, schema Draft-07, frontmatter RAG) → `.clinerules/sot-specs.md` + `sot-schemas.md` + `sot-rag.md`; tabela dos 5 agentes + I/O → `specs/` + `schemas/` + mapa do `AGENTS.md`; "Source documents" → `fundamentos/` + `canon/`. |

> Observação: o conteúdo canônico **baselined** (CHM/CEM/CEE/GMC/SDD/PPQ/SAS/CR) e as fontes (KERNEL/ENG GERAL/ARIA/AUDITORIA) permanecem **também** intactos em `DOCUMENTOS INICIAIS/` (arquivo-fonte). A cópia em `canon/`/`fundamentos/` é para autossuficiência do repo; a original nunca é tocada.

## 5. Verificação de integridade

- `npm test` → **11/11 schemas** válidos (Draft-07).
- `npm run lint` → **5/5 specs** com EARS + seções obrigatórias.
- CI `required_files` → todos resolvem nos novos caminhos (`governance/…`, `AGENTS.md`, `specs/…`, `schemas/…`, `rag/…`).
- Gate `python scripts/validate_spec_sot.py` → executável a partir da raiz.
- Resíduos dos valores antigos (2:1, 70% fechado, 5 dim., 3E, PROPOSED, "Sistema de Operações e Tendências") nos arquivos **ativos**: **zero** (apenas notas de correção intencionais e o staging de legado).

## 6. Lista de exclusão proposta (passo irreversível — aguarda confirmação)

**A eliminar (staging `docs/_legacy/` — 4 arquivos):**
1. `docs/_legacy/AGENTSV2.md` — fundido em AGENTS.md
2. `docs/_legacy/HARNESS-REPORT.md` — snapshot histórico
3. `docs/_legacy/PROMPT_HARNESS_ESPECIFICACAO.md` — prompt original
4. `docs/_legacy/PROMPT_HARNESS_ESPECIFICACAO_1.md` — prompt original (variante)

**Opcional (decisão do usuário):**
5. `.harness-eval/runs/` (27 arquivos, 412K) — saídas históricas de avaliação (regeneráveis por `npm run eval`). Recomendação: manter (evidência histórica) ou apagar se quiser repo enxuto.

**NÃO se toca:** `DOCUMENTOS INICIAIS/` (arquivo-fonte), nenhum arquivo de máquina, nenhum canônico.

---

*Manifesto gerado antes da exclusão. Nenhuma remoção ocorre sem aprovação explícita da lista acima.*
