# MAPA DO PROJETO — SOT Harness

> **NÃO-NORMATIVO e REGENERÁVEL** (BL-019). Não é baseline (INV-09), não substitui o [CATALOGO-OFICIAL](../../governance/CATALOGO-OFICIAL.md) — que segue como locator autoritativo — e não fecha decisão aberta (CONS-01). Em conflito, vale o documento de origem.
>
> Regenerar: `python scripts/build_map.py` · Verificar defasagem: `python scripts/build_map.py --check`

Gerado em **2026-11-01** · digest `5931af3e1ea4e76d` · **623** documentos · **11281** arestas doc→doc · fontes: `scripts/check_refs.py`, `scripts/backlog_triggers.py`

## 1. Camadas (por diretório)

| Área | Docs | Função | Mais referenciados |
|---|---:|---|---|
| **raiz** | 7 | entradas: ROADMAP, atomic-spec, AGENTS, GLOSSARIO, README | [ROADMAP.md](../../ROADMAP.md) (415) · [atomic-spec.md](../../atomic-spec.md) (293) · [AGENTS.md](../../AGENTS.md) (288) |
| **governance** | 307 | autoridade normativa: Constituição, RULES, CATALOGO, atas DHR, emendas EUA | [RULES.md](../../governance/RULES.md) (482) · [PCC-001_Plano_Continuidade_Contexto_Build_PROPOSTA.md](../../governance/PCC-001_Plano_Continuidade_Contexto_Build_PROPOSTA.md) (184) · [CATALOGO-OFICIAL.md](../../governance/CATALOGO-OFICIAL.md) (132) |
| **canon** | 9 | modelos canônicos BASELINED (CHM/CEM/CEE/GMC/SDD/PPQ/SAS/CR) | [CEM-001-canonical-evidence-model.md](../../canon/CEM-001-canonical-evidence-model.md) (165) · [CCM-001-canonical-conviction-model.md](../../canon/CCM-001-canonical-conviction-model.md) (114) · [CEE-001-cognitive-economy-efficiency-v2.0.md](../../canon/CEE-001-cognitive-economy-efficiency-v2.0.md) (104) |
| **specs** | 58 | Specs por feature (plan.md + checks.md) e specs de agente | [SPEC-006/plan.md](../../specs/features/SPEC-006/plan.md) (319) · [SPEC-007/plan.md](../../specs/features/SPEC-007/plan.md) (259) · [SPEC-001/plan.md](../../specs/features/SPEC-001/plan.md) (251) |
| **backlog** | 6 | RMR-001 e backlogs (gatilhos de ativação) | [RMR-001_Painel_Backlog.md](../../backlog/RMR-001_Painel_Backlog.md) (412) · [BL-018-RISK-AGENT-backlog.md](../../backlog/BL-018-RISK-AGENT-backlog.md) (21) · [BL-016-MC-SKL-001-encaminhamento.md](../../backlog/BL-016-MC-SKL-001-encaminhamento.md) (14) |
| **reference** | 28 | referências externas não-normativas (camadas, master contracts) | [MC-RAG-001_Master_Contract_Camada_RAG.md](../../reference/camadas/MC-RAG-001_Master_Contract_Camada_RAG.md) (28) · [MC-COG-001_Master_Contract_Camada_Cognicao.md](../../reference/camadas/MC-COG-001_Master_Contract_Camada_Cognicao.md) (25) · [CAMADA MEMÓRIA.MD](../../reference/camadas/CAMADA%20MEM%C3%93RIA.MD) (9) |
| **rag** | 5 | chunks de conhecimento por agente | [synthesis.knowledge.md](../../rag/synthesis.knowledge.md) (3) · [smc.knowledge.md](../../rag/smc.knowledge.md) (1) |
| **.claude** | 9 | agentes e skills do Claude Code | [especificador.md](../../.claude/agents/especificador.md) (107) · [revisor.md](../../.claude/agents/revisor.md) (90) · [SKILL.md](../../.claude/skills/harness-eval/SKILL.md) (3) |
| **docs** | 189 | documentação histórica e de arranque (não essencial à operação) | [INDICE-AGENTES.md](../../docs/agentes/INDICE-AGENTES.md) (52) · [HO-2026-10-31-128.md](../../docs/handoffs/HO-2026-10-31-128.md) (25) · [HO-2026-10-17-34.md](../../docs/handoffs/HO-2026-10-17-34.md) (19) |
| **RETOMADA** | 1 | material de retomada (GEH-001) | [GEH-001_Guia_Agente_Especificacoes_Harness.md](../../RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md) (41) |
| **.clinerules** | 4 | regras Cline | [sot-rag.md](../../.clinerules/sot-rag.md) (2) · [sot-schemas.md](../../.clinerules/sot-schemas.md) (2) · [sot-map.md](../../.clinerules/sot-map.md) (1) |

## 2. Dependências entre camadas

Seta A → B = documentos de A referenciam documentos de B (só pares com ≥ 8 referências).

```mermaid
flowchart LR
  docs["docs"] -->|3491| governance["governance"]
  docs["docs"] -->|1042| specs["specs"]
  governance["governance"] -->|1025| specs["specs"]
  docs["docs"] -->|797| raiz["raiz"]
  governance["governance"] -->|464| raiz["raiz"]
  specs["specs"] -->|455| governance["governance"]
  docs["docs"] -->|212| backlog["backlog"]
  governance["governance"] -->|210| backlog["backlog"]
  raiz["raiz"] -->|165| governance["governance"]
  backlog["backlog"] -->|111| governance["governance"]
  _claude[".claude"] -->|102| governance["governance"]
  docs["docs"] -->|97| _claude[".claude"]
  governance["governance"] -->|97| _claude[".claude"]
  specs["specs"] -->|95| raiz["raiz"]
  governance["governance"] -->|68| reference["reference"]
  specs["specs"] -->|57| backlog["backlog"]
  raiz["raiz"] -->|51| specs["specs"]
  backlog["backlog"] -->|40| specs["specs"]
  reference["reference"] -->|32| specs["specs"]
  _claude[".claude"] -->|26| specs["specs"]
  reference["reference"] -->|25| governance["governance"]
  governance["governance"] -->|23| canon["canon"]
  governance["governance"] -->|22| docs["docs"]
  backlog["backlog"] -->|20| raiz["raiz"]
  backlog["backlog"] -->|20| reference["reference"]
  reference["reference"] -->|19| raiz["raiz"]
  canon["canon"] -->|16| governance["governance"]
  specs["specs"] -->|15| reference["reference"]
  _claude[".claude"] -->|11| raiz["raiz"]
  raiz["raiz"] -->|9| backlog["backlog"]
```

## 3. Hubs — IDs mais referenciados

| ID | Documentos que citam | Definido em |
|---|---:|---|
| `INV-07` | 346 | [governance/RULES.md](../../governance/RULES.md) |
| `SPEC-006` | 319 | [specs/features/SPEC-006/plan.md](../../specs/features/SPEC-006/plan.md) |
| `SPEC-007` | 259 | [specs/features/SPEC-007/plan.md](../../specs/features/SPEC-007/plan.md) |
| `SPEC-020` | 216 | [specs/features/SPEC-020/plan.md](../../specs/features/SPEC-020/plan.md) |
| `BL-011` | 199 | [backlog/RMR-001_Painel_Backlog.md](../../backlog/RMR-001_Painel_Backlog.md) |
| `BL-003` | 191 | [backlog/RMR-001_Painel_Backlog.md](../../backlog/RMR-001_Painel_Backlog.md) |
| `BL-017` | 182 | [backlog/RMR-001_Painel_Backlog.md](../../backlog/RMR-001_Painel_Backlog.md) |
| `SPEC-002` | 182 | [specs/features/SPEC-002/plan.md](../../specs/features/SPEC-002/plan.md) |
| `BL-010` | 169 | [backlog/RMR-001_Painel_Backlog.md](../../backlog/RMR-001_Painel_Backlog.md) |
| `SPEC-048` | 165 | [specs/features/SPEC-048/plan.md](../../specs/features/SPEC-048/plan.md) |
| `SPEC-003` | 157 | [specs/features/SPEC-003/plan.md](../../specs/features/SPEC-003/plan.md) |
| `SPEC-049` | 142 | [specs/features/SPEC-049/plan.md](../../specs/features/SPEC-049/plan.md) |
| `SPEC-001` | 121 | [specs/features/SPEC-001/plan.md](../../specs/features/SPEC-001/plan.md) |
| `DHR-SPEC007-005` | 115 | [governance/DHR-SPEC007-005_Ata_Homologacao_Plan_Reduzido_SPEC-007.md](../../governance/DHR-SPEC007-005_Ata_Homologacao_Plan_Reduzido_SPEC-007.md) |
| `INV-09` | 110 | [governance/RULES.md](../../governance/RULES.md) |
| `SPEC-005` | 109 | [specs/features/SPEC-005/plan.md](../../specs/features/SPEC-005/plan.md) |
| `SPEC-004` | 107 | [specs/features/SPEC-004/plan.md](../../specs/features/SPEC-004/plan.md) |
| `DHR-LOOP-001` | 103 | [governance/DHR-LOOP-001_Ata_Regra_Coleta_Deterministica_de_Achados_4Es.md](../../governance/DHR-LOOP-001_Ata_Regra_Coleta_Deterministica_de_Achados_4Es.md) |
| `DHR-SPEC048-002` | 99 | [governance/DHR-SPEC048-002_Ata_Homologacao_Plan_SPEC-048.md](../../governance/DHR-SPEC048-002_Ata_Homologacao_Plan_SPEC-048.md) |
| `DHR-RETRO-001` | 98 | [governance/DHR-RETRO-001_Ata_Aprovacao_Propostas_P1-P6_e_Ordem_das_Erratas.md](../../governance/DHR-RETRO-001_Ata_Aprovacao_Propostas_P1-P6_e_Ordem_das_Erratas.md) |
| `RULE-ECC-01` | 97 | [governance/RULES.md](../../governance/RULES.md) |
| `DHR-REAPONT-001` | 93 | [governance/DHR-REAPONT-001_Ata_Homologacao_Erratum_Reapontamento.md](../../governance/DHR-REAPONT-001_Ata_Homologacao_Erratum_Reapontamento.md) |
| `DHR-SPEC006-005` | 92 | [governance/DHR-SPEC006-005_Ata_Homologacao_Errata_v1.13_SPEC-006.md](../../governance/DHR-SPEC006-005_Ata_Homologacao_Errata_v1.13_SPEC-006.md) |
| `DHR-SPEC007-007` | 90 | [governance/DHR-SPEC007-007_Ata_Diretriz_Autenticacao_Criptografica_dos_Atos.md](../../governance/DHR-SPEC007-007_Ata_Diretriz_Autenticacao_Criptografica_dos_Atos.md) |
| `DHR-ROTEAMENTO-007` | 89 | [governance/DHR-ROTEAMENTO-007_Ata_Roteamento_Obrigatorio_e_Detector_de_ID.md](../../governance/DHR-ROTEAMENTO-007_Ata_Roteamento_Obrigatorio_e_Detector_de_ID.md) |

## 4. Cadeia de Specs

| Spec | Estado | Plano | Docs que citam |
|---|---|---|---:|
| `SPEC-001` | **Homologada** | [specs/features/SPEC-001/plan.md](../../specs/features/SPEC-001/plan.md) | 121 |
| `SPEC-002` | **Homologada** | [specs/features/SPEC-002/plan.md](../../specs/features/SPEC-002/plan.md) | 182 |
| `SPEC-003` | **Homologada** | [specs/features/SPEC-003/plan.md](../../specs/features/SPEC-003/plan.md) | 157 |
| `SPEC-004` | **Homologada** | [specs/features/SPEC-004/plan.md](../../specs/features/SPEC-004/plan.md) | 107 |
| `SPEC-005` | **Homologada** | [specs/features/SPEC-005/plan.md](../../specs/features/SPEC-005/plan.md) | 109 |
| `SPEC-006` | **Homologada** | [specs/features/SPEC-006/plan.md](../../specs/features/SPEC-006/plan.md) | 319 |
| `SPEC-007` | **Homologada** | [specs/features/SPEC-007/plan.md](../../specs/features/SPEC-007/plan.md) | 259 |
| `SPEC-008` | Indicativa (não aberta) | — | 34 |
| `SPEC-009` | Indicativa (não aberta) | — | 89 |
| `SPEC-010` | Indicativa (não aberta) | — | 50 |
| `SPEC-011` | Indicativa (não aberta) | — | 6 |
| `SPEC-012` | Indicativa (não aberta) | — | 6 |
| `SPEC-013` | Indicativa (não aberta) | — | 8 |
| `SPEC-014` | Indicativa (não aberta) | — | 61 |
| `SPEC-015` | Indicativa (não aberta) | — | 23 |
| `SPEC-016` | Indicativa (não aberta) | — | 17 |
| `SPEC-017` | Indicativa (não aberta) | — | 9 |
| `SPEC-018` | Indicativa (não aberta) | — | 77 |
| `SPEC-019` | **Homologada** | [specs/features/SPEC-019/plan.md](../../specs/features/SPEC-019/plan.md) | 67 |
| `SPEC-020` | **Homologada** | [specs/features/SPEC-020/plan.md](../../specs/features/SPEC-020/plan.md) | 216 |
| `SPEC-021` | **Homologada** | [specs/features/SPEC-021/plan.md](../../specs/features/SPEC-021/plan.md) | 58 |
| `SPEC-022` | Indicativa (não aberta) | — | 14 |
| `SPEC-023` | Indicativa (não aberta) | — | 4 |
| `SPEC-024` | Indicativa (não aberta) | — | 9 |
| `SPEC-025` | Indicativa (não aberta) | — | 27 |
| `SPEC-026` | Indicativa (não aberta) | — | 3 |
| `SPEC-027` | Indicativa (não aberta) | — | 0 |
| `SPEC-028` | Indicativa (não aberta) | — | 0 |
| `SPEC-029` | Indicativa (não aberta) | — | 0 |
| `SPEC-030` | Indicativa (não aberta) | — | 0 |
| `SPEC-031` | Indicativa (não aberta) | — | 0 |
| `SPEC-032` | Indicativa (não aberta) | — | 1 |
| `SPEC-033` | Indicativa (não aberta) | — | 0 |
| `SPEC-034` | Indicativa (não aberta) | — | 0 |
| `SPEC-035` | Indicativa (não aberta) | — | 0 |
| `SPEC-036` | Indicativa (não aberta) | — | 2 |
| `SPEC-037` | Indicativa (não aberta) | — | 1 |
| `SPEC-038` | **Homologada** | [specs/features/SPEC-038/plan.md](../../specs/features/SPEC-038/plan.md) | 38 |
| `SPEC-039` | Indicativa (não aberta) | — | 8 |
| `SPEC-040` | Indicativa (não aberta) | — | 48 |
| `SPEC-041` | Indicativa (não aberta) | — | 17 |
| `SPEC-042` | Indicativa (não aberta) | — | 14 |
| `SPEC-043` | Indicativa (não aberta) | — | 12 |
| `SPEC-044` | Indicativa (não aberta) | — | 14 |
| `SPEC-045` | Indicativa (não aberta) | — | 11 |
| `SPEC-046` | **Homologada** | [specs/features/SPEC-046/plan.md](../../specs/features/SPEC-046/plan.md) | 31 |
| `SPEC-047` | Indicativa (não aberta) | — | 35 |
| `SPEC-048` | **Homologada** | [specs/features/SPEC-048/plan.md](../../specs/features/SPEC-048/plan.md) | 165 |
| `SPEC-049` | **Homologada** | [specs/features/SPEC-049/plan.md](../../specs/features/SPEC-049/plan.md) | 142 |

## 5. Backlog e integridade

- **Backlog (RMR-001):** ATIVADOS = BL-003, BL-011 · disparados sem registro = 4 · verificação manual = 3 itens (`python scripts/backlog_triggers.py`).
- **Referências (check_refs):** ERRO=0 · WARN=8 · INFO=342 (históricos congelados) — `python scripts/check_refs.py`.

## 6. Documentos sem referência de entrada

Nenhum outro documento cita por caminho, por ID resolvido ou pela chave do arquivo (ex.: `CHM-001`). Só arquivos `.md` são varridos: referências vindas de CI, JSON ou schemas não contam. Candidatos a revisão de higiene (RPIR) — **não** significa lixo.

- [.claude/commands/update-spec.md](../../.claude/commands/update-spec.md) — Update SOT Agent Spec
- [.claude/commands/validate-harness.md](../../.claude/commands/validate-harness.md) — Validate SOT Harness
- [.claude/skills/sot-especificador-pap001/SKILL.md](../../.claude/skills/sot-especificador-pap001/SKILL.md) — MISSÃO: PRODUZIR O PAP-001
- [governance/DHR-SPEC002-001_Ata_Homologacao_Abertura_SPEC-002.md](../../governance/DHR-SPEC002-001_Ata_Homologacao_Abertura_SPEC-002.md) — DHR-SPEC002-001 — Ata de Homologação — Abertura da SPEC-002 (Evidence & Evidence Provenance Harness)
- [governance/ERRATUM-SPEC019-001_PROPOSTA.md](../../governance/ERRATUM-SPEC019-001_PROPOSTA.md) — ERRATUM-SPEC019-001 — Correção aditiva do status de L-001 na SPEC-019 homologada (PROPOSTA)
- [governance/EUA-E19a_Restauracao_Signal_Package_PROPOSTA.md](../../governance/EUA-E19a_Restauracao_Signal_Package_PROPOSTA.md) — EUA-E19a — Restauração Semântica do "Signal Package" (fronteira) + TMP interno (PROPOSTA)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A2/PROPOSTA-A2-1-MAPA-JSON-LOCAL-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A2/PROPOSTA-A2-1-MAPA-JSON-LOCAL-2026-10-31.md) — Proposta pré-testada — A2.1: `mapa-projeto.json` fora da árvore versionada
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/MEDICAO-A6-2-HISTORICO-DOS-DETECTORES-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/MEDICAO-A6-2-HISTORICO-DOS-DETECTORES-2026-11-01.md) — Medição A6.2 — o que os detectores acharam nos últimos 30 merges da `main`
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PREPARO-ARQUIVAMENTO-AUDITOR-EXTERNO-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PREPARO-ARQUIVAMENTO-AUDITOR-EXTERNO-2026-11-01.md) — Preparo — arquivar o Auditor Externo (A6.3)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PROPOSTA-A6-4-E-A6-1-PARCIAL-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PROPOSTA-A6-4-E-A6-1-PARCIAL-2026-11-01.md) — Proposta pré-testada — A6.4 + A6.1 parcial (doc-sync)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PROPOSTA-A6-AVISOS-FIXOS-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PROPOSTA-A6-AVISOS-FIXOS-2026-11-01.md) — Proposta pré-testada — tratar os avisos permanentes (A6.2 reformulado)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/P11/PROPOSTA-P11-HANDOFF-POR-RAMO-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/P11/PROPOSTA-P11-HANDOFF-POR-RAMO-2026-10-31.md) — Proposta pré-testada — P11: handoff por ramo como regra (e `check_handoff` entende a união de cadeias)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/PROPOSTA-PROVA-DE-EQUIVALENCIA-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/PROPOSTA-PROVA-DE-EQUIVALENCIA-2026-10-31.md) — Proposta pré-testada — prova de conservação para enxugar documentos quentes (A5 / H1–H3)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/cenarios/RESULTADO.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/cenarios/RESULTADO.md) — Teste de cenários (aplicação de regras) — AGENTS.md original (A) × atual (E)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/cenarios/cenarios.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/cenarios/cenarios.md) — Cenários (responda cada um em UMA linha: `S<n>: <decisão/ação> — <regra em 1 frase>`; use SÓ o documento indicado; se o documento não bastar para decidir, `S<n>: NAO CONSTA`)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/RESULTADO.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/RESULTADO.md) — Pré-teste adversarial do canal `GATE-D` (P8, `DHR-AGENTS-P8-001`)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/cenarios.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/cenarios.md) — Cenários do Revisor (responda cada um em UMA linha: `C<n>: <o que o parecer faz> — <regra em 1 frase>`; use SÓ o §3 fornecido; se não bastar, `C<n>: NAO CONSTA`)
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/revisor-sec3.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/revisor-sec3.md) — revisor-sec3
- [governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/perguntas.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/perguntas.md) — Perguntas (responda cada uma em UMA linha curta, formato `Q<n>: <resposta>`; use SÓ o documento indicado; se o documento não permitir responder, escreva `Q<n>: NAO CONSTA`)
- [governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-A2-RITUAL-DE-FECHAMENTO-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-A2-RITUAL-DE-FECHAMENTO-2026-10-31.md) — Proposta A2 — Ritual de fechamento manual (medida antes de cortar)
- [governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-A3-PAUTA-DE-DECISOES-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-A3-PAUTA-DE-DECISOES-2026-11-01.md) — Proposta A3 — Pauta única de decisões de Andraus (decisão em lote)
- [governance/propostas/SPEC-002/ERRATUM-SPEC002-001_Aditivo_PROPOSTO.md](../../governance/propostas/SPEC-002/ERRATUM-SPEC002-001_Aditivo_PROPOSTO.md) — [ERRATUM-PROPOSTO — NÃO APLICADO] ERRATUM-SPEC002-001 — Erratum ADITIVO único (auditoria semântica SPEC-002: itens 1, 2, 3)
- [governance/propostas/SPEC-006/linha-spec006-plan/checks-v1.8-candidato.md](../../governance/propostas/SPEC-006/linha-spec006-plan/checks-v1.8-candidato.md) — checks.md — Verificação de Spec da SPEC-006 (fase spec-first)
- [governance/propostas/SPEC-006/linha-spec006-plan/plan-v1.8-candidato.md](../../governance/propostas/SPEC-006/linha-spec006-plan/plan-v1.8-candidato.md) — SPEC-006 — Cognitive Knowledge Graph
- [rag/elliott-wave.knowledge.md](../../rag/elliott-wave.knowledge.md) — RAG — Elliott Wave Specialist Knowledge Base
- [rag/fibonacci.knowledge.md](../../rag/fibonacci.knowledge.md) — RAG — Fibonacci Validator Knowledge Base
- [rag/ict.knowledge.md](../../rag/ict.knowledge.md) — RAG — ICT Specialist Knowledge Base
- [reference/externo/MASTER — MARKET DATA, ORDER FLOW E INTEGRAÇÃO TRADINGVIEW.MD](../../reference/externo/MASTER%20%E2%80%94%20MARKET%20DATA%2C%20ORDER%20FLOW%20E%20INTEGRA%C3%87%C3%83O%20TRADINGVIEW.MD) — MASTER — MARKET DATA, ORDER FLOW E INTEGRAÇÃO TRADINGVIEW
- [specs/features/SPEC-046/research.md](../../specs/features/SPEC-046/research.md) — Dossiê de Pesquisa — SPEC-046 (companion — convenção de nome do gate determinístico)

## 7. Índice de documentos

`←` = documentos que o citam · `→` = documentos que ele cita.

### raiz

| Documento | Título | ← | → |
|---|---|---:|---:|
| [AGENTS.md](../../AGENTS.md) | AGENTS.md — SOT (Sistema Operacional de Trading) | 288 | 41 |
| [GLOSSARIO.md](../../GLOSSARIO.md) | GLOSSÁRIO OFICIAL — SOT | 34 | 13 |
| [HANDOFF.md](../../HANDOFF.md) | HANDOFF — SOT | 20 | 48 |
| [README.md](../../README.md) | SOT-Harness | 2 | 9 |
| [ROADMAP.md](../../ROADMAP.md) | roadmap.md — SOT: Road Map Sequencial de Especificação do Harness Cognitivo | 415 | 87 |
| [WORKFLOW.md](../../WORKFLOW.md) | WORKFLOW — Setup Operacional Canônico do SOT | 215 | 12 |
| [atomic-spec.md](../../atomic-spec.md) | atomic-spec.md — Unidade Atômica de Especificação do Harness Cognitivo do SOT | 293 | 38 |

### governance

| Documento | Título | ← | → |
|---|---|---:|---:|
| [ADR-CONFLUENCE-001-v3_Skills_Confluence_Architecture.md](../../governance/ADR-CONFLUENCE-001-v3_Skills_Confluence_Architecture.md) | HOMOLOGADO — ADR-CONFLUENCE-001 v3 | 12 | 0 |
| [ADR-MANAGER-001_Manager_Agent_Architecture.md](../../governance/ADR-MANAGER-001_Manager_Agent_Architecture.md) | ADR-MANAGER-001 — Manager Agent: Arquitetura Unificada de Orquestração | 32 | 1 |
| [ADR-MISSION-TYPES-001_Mission_Types.md](../../governance/ADR-MISSION-TYPES-001_Mission_Types.md) | ADR-MISSION-TYPES-001 — Tipos de Missão: Exploratória e de Validação | 4 | 1 |
| [AUDITORIA-ADIANTAMENTO-SLOTS-ROADMAP-2026-09-28.md](../../governance/AUDITORIA-ADIANTAMENTO-SLOTS-ROADMAP-2026-09-28.md) | AUDITORIA DE ADIANTAMENTO DE ABERTURA — Slots Indicativos do ROADMAP | 5 | 21 |
| [AUDITORIA-COESAO-MECANISMOS-2026-10-17.md](../../governance/AUDITORIA-COESAO-MECANISMOS-2026-10-17.md) | Auditoria de coesão dos mecanismos do repositório (2026-10-17) | 31 | 17 |
| [AUDITORIA-HIGIENE-SPECS-2026-10-01.md](../../governance/AUDITORIA-HIGIENE-SPECS-2026-10-01.md) | AUDITORIA DE HIGIENE DAS SPECS — 2026-10-01 | 3 | 15 |
| [AUDITORIA-REVISOR-MATURIDADE-2026-10-17.md](../../governance/AUDITORIA-REVISOR-MATURIDADE-2026-10-17.md) | Auditoria por testes do Revisor SOT — interpelação e adversarial — nível de m... | 6 | 4 |
| [AVALIACAO-MECANISMOS-REVISOR-2026-10-17.md](../../governance/AVALIACAO-MECANISMOS-REVISOR-2026-10-17.md) | Avaliação dos mecanismos (regras, guardrails, hooks, policy, determinísticos)... | 49 | 11 |
| [BL-012-DELTA_PROPOSTA.md](../../governance/BL-012-DELTA_PROPOSTA.md) | BL-012 (MC-COG-001) — Reavaliação do DELTA — [PROPOSTA] | 34 | 15 |
| [BRIEFING-DECISAO-I-001.md](../../governance/BRIEFING-DECISAO-I-001.md) | BRIEFING DE DECISÃO — I-001 ("Skills como unidades formais separadas?") | 5 | 16 |
| [CATALOGO-OFICIAL.md](../../governance/CATALOGO-OFICIAL.md) | CATÁLOGO OFICIAL — Estado e Baseline dos Artefatos (SOT) | 132 | 222 |
| [CIC-001_Inventario_Conformidade.md](../../governance/CIC-001_Inventario_Conformidade.md) | CIC-001 --- Inventario de Conformidade de Principios do SOT | 43 | 28 |
| [CLASSIFICACAO-COLISOES-BL010-011-012.md](../../governance/CLASSIFICACAO-COLISOES-BL010-011-012.md) | CLASSIFICAÇÃO DE COLISÕES — BL-010 / BL-011 / BL-012 (Master Contracts diferi... | 5 | 11 |
| [CONFLICT-MAP.md](../../governance/CONFLICT-MAP.md) | Conflict Map — SOT (Sistema Operacional de Trading) | 60 | 40 |
| [CONSTITUTION.md](../../governance/CONSTITUTION.md) | SOT Constitution — Sistema Operacional de Trading | 27 | 1 |
| [DHR-ADR-HOC003_Ata_Homologacao_HOC003.md](../../governance/DHR-ADR-HOC003_Ata_Homologacao_HOC003.md) | DHR-ADR-HOC003 — Ata de Homologação — Cluster HOC-003 (Auditoria Taxonômica 2... | 7 | 6 |
| [DHR-AGENTES-001_Ata_Separacao_Agentes_Construcao_e_Trading.md](../../governance/DHR-AGENTES-001_Ata_Separacao_Agentes_Construcao_e_Trading.md) | DHR-AGENTES-001 — Ata — Separação nominal dos agentes de Construção e dos age... | 51 | 9 |
| [DHR-AGENTS-CORTES-001_Ata_Enxugar_AGENTS_Secoes_2_5_8_9_12.md](../../governance/DHR-AGENTS-CORTES-001_Ata_Enxugar_AGENTS_Secoes_2_5_8_9_12.md) | DHR-AGENTS-CORTES-001 — Ata de Decisão — Enxugar o AGENTS.md (§2, §5, §8, §9,... | 38 | 5 |
| [DHR-AGENTS-P8-001_Ata_Gate_do_Revisor_via_Orquestrador_em_Nuvem.md](../../governance/DHR-AGENTS-P8-001_Ata_Gate_do_Revisor_via_Orquestrador_em_Nuvem.md) | DHR-AGENTS-P8-001 — Ata de Decisão — Gate determinístico do Revisor: canal `G... | 33 | 6 |
| [DHR-AGENTS-SEC7-001_Ata_Enxugar_AGENTS_Secao7.md](../../governance/DHR-AGENTS-SEC7-001_Ata_Enxugar_AGENTS_Secao7.md) | DHR-AGENTS-SEC7-001 — Ata de Decisão — Enxugar o AGENTS.md §7 (duplicado do R... | 44 | 6 |
| [DHR-ARQ-001_Ata_Unificacao_Manager_Conviction.md](../../governance/DHR-ARQ-001_Ata_Unificacao_Manager_Conviction.md) | DHR-ARQ-001 — Ata de Unificação: Manager Agent absorve o Conviction Engine (p... | 19 | 13 |
| [DHR-ARQ-002_Ata_Manager_Absorve_Synthesis.md](../../governance/DHR-ARQ-002_Ata_Manager_Absorve_Synthesis.md) | DHR-ARQ-002 — Ata de Unificação: Manager Agent absorve o Synthesis Agent (pro... | 20 | 17 |
| [DHR-ASK-002_Ata_Regra_Fim_de_Turno_PROPOSTA.md](../../governance/DHR-ASK-002_Ata_Regra_Fim_de_Turno_PROPOSTA.md) | DHR-ASK-002 — Ata — Regra de fim de turno do Orquestrador (decisão de Andraus... | 33 | 4 |
| [DHR-ASSINATURA-001_Ata_Assinatura_por_Decisao_Registrada.md](../../governance/DHR-ASSINATURA-001_Ata_Assinatura_por_Decisao_Registrada.md) | DHR-ASSINATURA-001 — Ata — A assinatura de Andraus passa a ser a decisão regi... | 5 | 6 |
| [DHR-AUDIT-SPEC001-001_Ata_Sessao_Auditoria_PROPOSTA.md](../../governance/DHR-AUDIT-SPEC001-001_Ata_Sessao_Auditoria_PROPOSTA.md) | DHR-AUDIT-SPEC001-001 — Ata — Sessão de auditoria semântica da SPEC-001 (deci... | 9 | 7 |
| [DHR-AUDITOR-EXTERNO-001_Ata_Piloto_Controlado.md](../../governance/DHR-AUDITOR-EXTERNO-001_Ata_Piloto_Controlado.md) | DHR-AUDITOR-EXTERNO-001 — Ata — Auditor externo (GPT): piloto controlado, hie... | 9 | 5 |
| [DHR-AUDITOR-EXTERNO-002_Ata_Ativacao_e_Limites.md](../../governance/DHR-AUDITOR-EXTERNO-002_Ata_Ativacao_e_Limites.md) | DHR-AUDITOR-EXTERNO-002 — Ata — Ativação do canal do Auditor Externo (piloto)... | 2 | 10 |
| [DHR-AUDITOR-EXTERNO-003_Ata_Bot_Agendado_Oracle.md](../../governance/DHR-AUDITOR-EXTERNO-003_Ata_Bot_Agendado_Oracle.md) | DHR-AUDITOR-EXTERNO-003 — Ata — Bot agendado do Auditor Externo (Codex soment... | 3 | 9 |
| [DHR-AUDITOR-EXTERNO-004_Ata_Ratificacao_RPSA_e_AGENTS.md](../../governance/DHR-AUDITOR-EXTERNO-004_Ata_Ratificacao_RPSA_e_AGENTS.md) | DHR-AUDITOR-EXTERNO-004 — Ata — Ratificação da classificação RPSA das atas 00... | 3 | 12 |
| [DHR-AUDITOR-EXTERNO-005_Ata_Roteamento_de_Achados_Faixa_Dupla.md](../../governance/DHR-AUDITOR-EXTERNO-005_Ata_Roteamento_de_Achados_Faixa_Dupla.md) | DHR-AUDITOR-EXTERNO-005 — Ata — Roteamento determinístico de achados do Audit... | 1 | 5 |
| [DHR-AUDITOR-EXTERNO-006_Ata_Erratum_AGENTS_I-001.md](../../governance/DHR-AUDITOR-EXTERNO-006_Ata_Erratum_AGENTS_I-001.md) | DHR-AUDITOR-EXTERNO-006 — Ata — Erratum do `AGENTS.md` §7 (I-001 já FECHADA) ... | 1 | 7 |
| [DHR-AUDITOR-EXTERNO-007_Ata_Pausa_do_Auditor_e_Reforco_do_Revisor.md](../../governance/DHR-AUDITOR-EXTERNO-007_Ata_Pausa_do_Auditor_e_Reforco_do_Revisor.md) | DHR-AUDITOR-EXTERNO-007 — Ata — Pausa do Auditor Externo e reforço do Revisor... | 11 | 7 |
| [DHR-AUDITOR-EXTERNO-008_Ata_Reforco_do_Revisor.md](../../governance/DHR-AUDITOR-EXTERNO-008_Ata_Reforco_do_Revisor.md) | DHR-AUDITOR-EXTERNO-008 — Ata — Reforço do Revisor interno (pacote de evidênc... | 4 | 6 |
| [DHR-AUDITOR-EXTERNO-009_Ata_Gate_Fundido_Classe_D_do_Revisor.md](../../governance/DHR-AUDITOR-EXTERNO-009_Ata_Gate_Fundido_Classe_D_do_Revisor.md) | DHR-AUDITOR-EXTERNO-009 — Ata — Gate fundido (Classe D) como ferramenta ofici... | 71 | 8 |
| [DHR-AUDITOR-EXTERNO-010_Ata_Proposta_Emenda_do_Revisor_Gate_Fundido.md](../../governance/DHR-AUDITOR-EXTERNO-010_Ata_Proposta_Emenda_do_Revisor_Gate_Fundido.md) | DHR-AUDITOR-EXTERNO-010 — Ata — Proposta de emenda do `.claude/agents/revisor... | 2 | 7 |
| [DHR-AUDITOR-EXTERNO-011_Ata_Aplicacao_da_Emenda_do_Revisor.md](../../governance/DHR-AUDITOR-EXTERNO-011_Ata_Aplicacao_da_Emenda_do_Revisor.md) | DHR-AUDITOR-EXTERNO-011 — Ata — Aplicação ao `.claude/agents/revisor.md` da e... | 1 | 8 |
| [DHR-AUDITOR-EXTERNO-012_Ata_Correcao_Passo8_Revisor_I001_L001.md](../../governance/DHR-AUDITOR-EXTERNO-012_Ata_Correcao_Passo8_Revisor_I001_L001.md) | DHR-AUDITOR-EXTERNO-012 — Ata — Correção do Passo 8 do `.claude/agents/reviso... | 1 | 9 |
| [DHR-AUDITOR-EXTERNO-013_Ata_Novas_Verificacoes_D_no_Gate_do_Revisor.md](../../governance/DHR-AUDITOR-EXTERNO-013_Ata_Novas_Verificacoes_D_no_Gate_do_Revisor.md) | DHR-AUDITOR-EXTERNO-013 — Ata — Novas verificações determinísticas (Classe D)... | 2 | 7 |
| [DHR-AUDITOR-EXTERNO-014_Ata_Revisor_Modelo_e_Metodo_V2.md](../../governance/DHR-AUDITOR-EXTERNO-014_Ata_Revisor_Modelo_e_Metodo_V2.md) | DHR-AUDITOR-EXTERNO-014 — Ata — Revisor SOT: modelo elevado e Passo 4-ter (in... | 18 | 7 |
| [DHR-AUDITOR-EXTERNO-015_Ata_Brechas_de_Ferramenta_e_Medicao_do_Revisor.md](../../governance/DHR-AUDITOR-EXTERNO-015_Ata_Brechas_de_Ferramenta_e_Medicao_do_Revisor.md) | DHR-AUDITOR-EXTERNO-015 — Ata — Brechas de ferramenta dos subagentes de revis... | 57 | 6 |
| [DHR-AUDITOR-EXTERNO-016_Ata_Fusao_dos_Subagentes_Antigos_no_Revisor.md](../../governance/DHR-AUDITOR-EXTERNO-016_Ata_Fusao_dos_Subagentes_Antigos_no_Revisor.md) | DHR-AUDITOR-EXTERNO-016 — Ata — Fusão do que era útil dos subagentes de 1ª ge... | 56 | 9 |
| [DHR-AUDITOR-EXTERNO-017_Ata_Deteccao_Deterministica_e_Guarda_do_Revisor.md](../../governance/DHR-AUDITOR-EXTERNO-017_Ata_Deteccao_Deterministica_e_Guarda_do_Revisor.md) | DHR-AUDITOR-EXTERNO-017 — Ata — Detectores determinísticos adicionais no gate... | 4 | 10 |
| [DHR-AUDITOR-EXTERNO-018_Ata_Guarda_Pos_Revisor_no_Orquestrador.md](../../governance/DHR-AUDITOR-EXTERNO-018_Ata_Guarda_Pos_Revisor_no_Orquestrador.md) | DHR-AUDITOR-EXTERNO-018 — Ata — Guarda pós-Revisor no Orquestrador (hook Stop... | 61 | 5 |
| [DHR-AUDITOR-EXTERNO-019_Ata_Arquivamento_do_Auditor_Externo.md](../../governance/DHR-AUDITOR-EXTERNO-019_Ata_Arquivamento_do_Auditor_Externo.md) | DHR-AUDITOR-EXTERNO-019 — Ata — Arquivamento do Auditor Externo (A6.3) | 3 | 5 |
| [DHR-BACKLOG-001_Ata_Promocao_BL003_BL011_ATIVADO.md](../../governance/DHR-BACKLOG-001_Ata_Promocao_BL003_BL011_ATIVADO.md) | DHR-BACKLOG-001 — Ata — Promoção de BL-003 e BL-011 a ATIVADO (gatilho `spec:... | 29 | 4 |
| [DHR-BACKLOG-ABERTURA-001_Ata_Vinculacao_Automatica_de_Backlog_na_Abertura.md](../../governance/DHR-BACKLOG-ABERTURA-001_Ata_Vinculacao_Automatica_de_Backlog_na_Abertura.md) | DHR-BACKLOG-ABERTURA-001 — Ata — Backlog vinculado por regra à abertura de ca... | 36 | 7 |
| [DHR-BENCH-INTEL-001_Ata_Inteligencia-SOT_como_Benchmark.md](../../governance/DHR-BENCH-INTEL-001_Ata_Inteligencia-SOT_como_Benchmark.md) | DHR-BENCH-INTEL-001 — Ata — Repositório paralelo `Inteligencia-SOT` como Benc... | 47 | 9 |
| [DHR-BL008-001_Ata_Homologacao_Mapa_Auditoria_SPEC-001.md](../../governance/DHR-BL008-001_Ata_Homologacao_Mapa_Auditoria_SPEC-001.md) | DHR-BL008-001 — Ata de Homologação — Mapa de Auditoria da SPEC-001 (BL-008) | 9 | 11 |
| [DHR-BL009-001_Ata_Homologacao_Mapa_Auditoria_SAS-001.md](../../governance/DHR-BL009-001_Ata_Homologacao_Mapa_Auditoria_SAS-001.md) | DHR-BL009-001 — Ata de Homologação — Mapa de Auditoria do SAS-001 (BL-009) | 3 | 6 |
| [DHR-BL010-011-012-001_Ata_Homologacao_Classificacao_Colisoes.md](../../governance/DHR-BL010-011-012-001_Ata_Homologacao_Classificacao_Colisoes.md) | DHR-BL010-011-012-001 — Ata de Homologação — Classificação de Colisões (MC-RA... | 8 | 4 |
| [DHR-BL012-001_Ata_Encerramento_BL-012_Delta.md](../../governance/DHR-BL012-001_Ata_Encerramento_BL-012_Delta.md) | DHR-BL012-001 — Ata — Encerramento do BL-012 (MC-COG-001) após reavaliação do... | 6 | 17 |
| [DHR-CHECKS-INFO-001_Ata_Detectores_Informativos_Dimensionamento_e_Hash.md](../../governance/DHR-CHECKS-INFO-001_Ata_Detectores_Informativos_Dimensionamento_e_Hash.md) | DHR-CHECKS-INFO-001 — Ata de Decisão — Detectores informativos: dimensionamen... | 72 | 7 |
| [DHR-CIC-001_Ata_Homologacao_CIC-001.md](../../governance/DHR-CIC-001_Ata_Homologacao_CIC-001.md) | DHR-CIC-001 — Ata de Homologação do CIC-001 v1.0 | 5 | 2 |
| [DHR-CLASSE-MECH-001_Ata_Homologacao_Classe_Mecanismo.md](../../governance/DHR-CLASSE-MECH-001_Ata_Homologacao_Classe_Mecanismo.md) | DHR-CLASSE-MECH-001 — Ata de Homologação — Taxonomia de Classe/Mecanismo de I... | 12 | 20 |
| [DHR-COESAO-001_Ata_Decisoes_Auditoria_de_Coesao.md](../../governance/DHR-COESAO-001_Ata_Decisoes_Auditoria_de_Coesao.md) | DHR-COESAO-001 — Ata — Decisões de Andraus sobre a auditoria de coesão dos me... | 30 | 8 |
| [DHR-COESAO-002_Ata_Decisoes_Legado_Auditor_Precommit_Revisor.md](../../governance/DHR-COESAO-002_Ata_Decisoes_Legado_Auditor_Precommit_Revisor.md) | DHR-COESAO-002 — Ata — Decisões de Andraus sobre Auditor Externo, pre-commit,... | 61 | 8 |
| [DHR-COESAO-003_Ata_AGENTS_Tabelas_e_RULE-COESAO.md](../../governance/DHR-COESAO-003_Ata_AGENTS_Tabelas_e_RULE-COESAO.md) | DHR-COESAO-003 — Ata — AGENTS.md §3/§8 alinhados à realidade e RULE-COESAO-01... | 27 | 7 |
| [DHR-COESAO-004_Ata_Lembretes_Datados_no_HANDOFF.md](../../governance/DHR-COESAO-004_Ata_Lembretes_Datados_no_HANDOFF.md) | DHR-COESAO-004 — Ata — Lembretes datados no HANDOFF (HO-10) para que melhoria... | 23 | 4 |
| [DHR-COESAO-005_Ata_Registro_de_Mecanismos_VIGENTE.md](../../governance/DHR-COESAO-005_Ata_Registro_de_Mecanismos_VIGENTE.md) | DHR-COESAO-005 — Ata — Registro de mecanismos (`governance/MECANISMOS.json`) ... | 33 | 7 |
| [DHR-DEC-001_Ata_Decisoes_QA5_RISKCONV_RISKARR.md](../../governance/DHR-DEC-001_Ata_Decisoes_QA5_RISKCONV_RISKARR.md) | DHR-DEC-001 — Ata de Decisões — Q-A5, RISK-CONV-001, RISK-ARR-LOC-001, DIV co... | 18 | 14 |
| [DHR-DEC-002_Ata_QA9_Regime_Temporal.md](../../governance/DHR-DEC-002_Ata_QA9_Regime_Temporal.md) | DHR-DEC-002 — Ata de Decisão — Q-A9 (dimensão do regime de mercado) → dimensã... | 9 | 10 |
| [DHR-DEC-003_Ata_Decisoes_SPEC038_BL.md](../../governance/DHR-DEC-003_Ata_Decisoes_SPEC038_BL.md) | DHR-DEC-003 — Ata de Decisões — SPEC-038 (TVMCP-001), BL-002/012/027/028/029/... | 29 | 9 |
| [DHR-DEC-004_Ata_Decisoes_BL017_DATASRC_MASTER.md](../../governance/DHR-DEC-004_Ata_Decisoes_BL017_DATASRC_MASTER.md) | DHR-DEC-004 — Ata de Decisões — BL-017, SPEC-038-DATASRC-001, MASTER Market D... | 17 | 13 |
| [DHR-DELTA-HASH-001_Ata_Delta_por_Hash_Propostas_1_a_3.md](../../governance/DHR-DELTA-HASH-001_Ata_Delta_por_Hash_Propostas_1_a_3.md) | DHR-DELTA-HASH-001 — Ata de Decisão — Delta por hash: pacote gravado, SHA256-... | 66 | 4 |
| [DHR-DIMENSIONAMENTO-001_Ata_RULE-ECC-07_Tetos_de_Spec.md](../../governance/DHR-DIMENSIONAMENTO-001_Ata_RULE-ECC-07_Tetos_de_Spec.md) | DHR-DIMENSIONAMENTO-001 — Ata de Decisão — RULE-ECC-07: dimensionamento de Sp... | 85 | 7 |
| [DHR-DIV-001_Ata_Varredura_Termos_Legados_Canon.md](../../governance/DHR-DIV-001_Ata_Varredura_Termos_Legados_Canon.md) | DHR-DIV-001 — Ata de Varredura DIV: termos legados em documentos CANON BASELINED | 7 | 12 |
| [DHR-DOCSYNC-001_Ata_Homologacao_Sincronizacao_Documental.md](../../governance/DHR-DOCSYNC-001_Ata_Homologacao_Sincronizacao_Documental.md) | DHR-DOCSYNC-001 — Ata de Homologação — Detector de Sincronização Documental +... | 2 | 13 |
| [DHR-DOCSYNC-002_Ata_Homologacao_Encaminhamento_Residuais.md](../../governance/DHR-DOCSYNC-002_Ata_Homologacao_Encaminhamento_Residuais.md) | DHR-DOCSYNC-002 — Ata de Homologação — Encaminhamento dos Residuais de DHR-DO... | 5 | 20 |
| [DHR-DOCSYNC-003_Ata_Detector_ID_Inteiro_e_AGENTS_SPEC-020-PRINC-001.md](../../governance/DHR-DOCSYNC-003_Ata_Detector_ID_Inteiro_e_AGENTS_SPEC-020-PRINC-001.md) | DHR-DOCSYNC-003 — Ata de Decisão — Detector de sincronização casa ID inteiro;... | 65 | 7 |
| [DHR-ECC05-001_Ata_Homologacao_Pesquisa_Multi_Lente.md](../../governance/DHR-ECC05-001_Ata_Homologacao_Pesquisa_Multi_Lente.md) | DHR-ECC05-001 — Ata de Homologação — Pesquisa Multi-Lente (RULE-ECC-05) | 9 | 8 |
| [DHR-ECC06-001_Ata_Homologacao_Pesquisa_Repositorios.md](../../governance/DHR-ECC06-001_Ata_Homologacao_Pesquisa_Repositorios.md) | DHR-ECC06-001 — Ata de Homologação — RULE-ECC-06: Pesquisa em repositórios se... | 8 | 7 |
| [DHR-ERRATA-001_Ata_Errata_SPEC001_SPEC005_BL003.md](../../governance/DHR-ERRATA-001_Ata_Errata_SPEC001_SPEC005_BL003.md) | DHR-ERRATA-001 — Ata — Errata aditivas (SPEC-001 âncora SAS-001; SPEC-005 est... | 9 | 12 |
| [DHR-EUA-E04_Ata_Homologacao_Heranca_Delta.md](../../governance/DHR-EUA-E04_Ata_Homologacao_Heranca_Delta.md) | DHR-EUA-E04 — Ata de Homologação da Emenda EUA-E04 (Bloco Herança/Delta) | 79 | 5 |
| [DHR-EUA-E05_Ata_Homologacao_Epistemic_Check.md](../../governance/DHR-EUA-E05_Ata_Homologacao_Epistemic_Check.md) | DHR-EUA-E05 — Ata de Homologação da Emenda EUA-E05 (Epistemic Check) | 30 | 7 |
| [DHR-EUA-E06_Ata_Homologacao_Camada_Semantica.md](../../governance/DHR-EUA-E06_Ata_Homologacao_Camada_Semantica.md) | DHR-EUA-E06 — Ata de Homologação da Emenda EUA-E06 (Camada Semântica) | 14 | 6 |
| [DHR-EUA-E07_Ata_Homologacao_Camada_Ontologica.md](../../governance/DHR-EUA-E07_Ata_Homologacao_Camada_Ontologica.md) | DHR-EUA-E07 — Ata de Homologação da Emenda EUA-E07 (Camada Ontológica) | 10 | 5 |
| [DHR-EUA-E08_Ata_Homologacao_Camada_Inquerito.md](../../governance/DHR-EUA-E08_Ata_Homologacao_Camada_Inquerito.md) | DHR-EUA-E08 — Ata de Homologação da Emenda EUA-E08 (Camada de Inquérito) | 10 | 5 |
| [DHR-EUA-E09_Ata_Homologacao_Camada_Causal.md](../../governance/DHR-EUA-E09_Ata_Homologacao_Camada_Causal.md) | DHR-EUA-E09 — Ata de Homologação da Emenda EUA-E09 (Camada Causal) | 14 | 4 |
| [DHR-EUA-E10_Ata_Homologacao_Camada_Contrafactual.md](../../governance/DHR-EUA-E10_Ata_Homologacao_Camada_Contrafactual.md) | DHR-EUA-E10 — Ata de Homologação da Emenda EUA-E10 (Camada Contrafactual) | 11 | 5 |
| [DHR-EUA-E11_Ata_Homologacao_Camada_Incerteza.md](../../governance/DHR-EUA-E11_Ata_Homologacao_Camada_Incerteza.md) | DHR-EUA-E11 — Ata de Homologação da Emenda EUA-E11 (Camada de Incerteza) | 12 | 4 |
| [DHR-EUA-E12_Ata_Homologacao_Camada_Probabilistica.md](../../governance/DHR-EUA-E12_Ata_Homologacao_Camada_Probabilistica.md) | DHR-EUA-E12 — Ata de Homologação da Emenda EUA-E12 (Camada Probabilística) | 11 | 5 |
| [DHR-EUA-E13_Ata_Homologacao_Camada_Decisional.md](../../governance/DHR-EUA-E13_Ata_Homologacao_Camada_Decisional.md) | DHR-EUA-E13 — Ata de Homologação da Emenda EUA-E13 (Camada Decisional) | 13 | 4 |
| [DHR-EUA-E14_Ata_Homologacao_Camada_Metacognicao.md](../../governance/DHR-EUA-E14_Ata_Homologacao_Camada_Metacognicao.md) | DHR-EUA-E14 — Ata de Homologação da Emenda EUA-E14 (Camada Metacognição) | 11 | 5 |
| [DHR-EUA-E15_Ata_Homologacao_Redesignacao_Piloto_SPEC-001.md](../../governance/DHR-EUA-E15_Ata_Homologacao_Redesignacao_Piloto_SPEC-001.md) | DHR-EUA-E15 — Ata de Homologação da Redesignação do Piloto de Incorporação (S... | 20 | 6 |
| [DHR-EUA-E16_Ata_Homologacao_Sincronizacao_Agentes.md](../../governance/DHR-EUA-E16_Ata_Homologacao_Sincronizacao_Agentes.md) | DHR-EUA-E16 — Ata de Homologação da Sincronização dos Agentes + RPSA | 25 | 6 |
| [DHR-EUA-E17_Ata_Homologacao_Reposicionamento_Specs_Governanca_Harness.md](../../governance/DHR-EUA-E17_Ata_Homologacao_Reposicionamento_Specs_Governanca_Harness.md) | DHR-EUA-E17 — Ata de Homologação: Reposicionamento das Specs de Governança do... | 24 | 16 |
| [DHR-EUA-E18_Ata_Homologacao_Reducao_Vies_Sincronizacao_SpecLean.md](../../governance/DHR-EUA-E18_Ata_Homologacao_Reducao_Vies_Sincronizacao_SpecLean.md) | DHR-EUA-E18 — Ata de Homologação: Redução de Viés e Uso Sincronizado da Spec-... | 34 | 16 |
| [DHR-EUA-E19_Ata_Homologacao_Economia_Tokens_Camada_Meta.md](../../governance/DHR-EUA-E19_Ata_Homologacao_Economia_Tokens_Camada_Meta.md) | DHR-EUA-E19 — Ata de Homologação: Economia de Tokens na Camada Meta (Roteamen... | 23 | 11 |
| [DHR-EUA-E19a_Ata_Homologacao_Restauracao_Signal_Package.md](../../governance/DHR-EUA-E19a_Ata_Homologacao_Restauracao_Signal_Package.md) | DHR-EUA-E19a — Ata de Homologação — Restauração Semântica do Signal Package | 27 | 10 |
| [DHR-EUA-E20_Ata_Homologacao_Fase_RISK.md](../../governance/DHR-EUA-E20_Ata_Homologacao_Fase_RISK.md) | DHR-EUA-E20 — Ata de Homologação: FASE RISK (6 macro-slots indicativos da fam... | 49 | 18 |
| [DHR-EUA-E21_Ata_Homologacao_Especificacao_Emergente.md](../../governance/DHR-EUA-E21_Ata_Homologacao_Especificacao_Emergente.md) | DHR-EUA-E21 — Ata de Homologação: Especificação Emergente (ROADMAP como direç... | 42 | 16 |
| [DHR-EUA-E22_Ata_Homologacao_Manutencao_Mapa_Projeto.md](../../governance/DHR-EUA-E22_Ata_Homologacao_Manutencao_Mapa_Projeto.md) | DHR-EUA-E22 — Ata de Homologação: Manutenção obrigatória do Mapa do Projeto (... | 14 | 14 |
| [DHR-EUA-E23_Ata_Homologacao_Manager_Unificado.md](../../governance/DHR-EUA-E23_Ata_Homologacao_Manager_Unificado.md) | DHR-EUA-E23 — Ata de Homologação: Manager Agent Unificado (3 Specs sob "Manag... | 44 | 13 |
| [DHR-H001-001_Ata_Fechamento_H-001_Mecanismo_Fisico_do_KG.md](../../governance/DHR-H001-001_Ata_Fechamento_H-001_Mecanismo_Fisico_do_KG.md) | DHR-H001-001 — Ata — Fechamento da decisão H-001 (mecanismo físico de armazen... | 51 | 15 |
| [DHR-HIGIENE-001_Ata_Pendencias_Baratas_Status_e_Refs.md](../../governance/DHR-HIGIENE-001_Ata_Pendencias_Baratas_Status_e_Refs.md) | DHR-HIGIENE-001 — Ata de Decisão — Pendências baratas de higiene (status de a... | 34 | 11 |
| [DHR-HIGIENE-002_Ata_Status_EUA-E20_E23_PCC-001.md](../../governance/DHR-HIGIENE-002_Ata_Status_EUA-E20_E23_PCC-001.md) | DHR-HIGIENE-002 — Ata de Decisão — Status de registros desatualizados (EUA-E2... | 32 | 13 |
| [DHR-HOD-001_Ata_Homologacao_Higiene_Documental.md](../../governance/DHR-HOD-001_Ata_Homologacao_Higiene_Documental.md) | DHR-HOD-001 — Ata de Homologação do Plano de Higiene e Organização Documental... | 3 | 5 |
| [DHR-I001-001_Ata_Homologacao_Fechamento_I-001.md](../../governance/DHR-I001-001_Ata_Homologacao_Fechamento_I-001.md) | DHR-I001-001 — Ata de Homologação — Fechamento de I-001 (Skills como unidades... | 12 | 8 |
| [DHR-LOOP-001_Ata_Regra_Coleta_Deterministica_de_Achados_4Es.md](../../governance/DHR-LOOP-001_Ata_Regra_Coleta_Deterministica_de_Achados_4Es.md) | DHR-LOOP-001 — Ata de Decisão — Regra determinística de coleta de achados do ... | 103 | 13 |
| [DHR-MAN-001_Ata_Homologacao_Mapa_Arquitetura_Normativa.md](../../governance/DHR-MAN-001_Ata_Homologacao_Mapa_Arquitetura_Normativa.md) | DHR-MAN-001 — Ata de Homologação do MAN-001 (Mapa da Arquitetura Normativa) | 4 | 3 |
| [DHR-MC-COG-001_Ata_Admissao_Backlog_BL-012.md](../../governance/DHR-MC-COG-001_Ata_Admissao_Backlog_BL-012.md) | DHR-MC-COG-001 — Ata de Homologação da Admissão ao Backlog (BL-012 · Camada d... | 3 | 5 |
| [DHR-MC-EXP-001_Ata_Admissao_Backlog_BL-011.md](../../governance/DHR-MC-EXP-001_Ata_Admissao_Backlog_BL-011.md) | DHR-MC-EXP-001 — Ata de Homologação da Admissão ao Backlog (BL-011 · Camada d... | 3 | 8 |
| [DHR-MC-GOV-001_Ata_Admissao_Backlog_BL-013.md](../../governance/DHR-MC-GOV-001_Ata_Admissao_Backlog_BL-013.md) | DHR-MC-GOV-001 — Ata de Homologação da Admissão ao Backlog (BL-013 · Camada d... | 4 | 7 |
| [DHR-MC-LRN-001_Ata_Admissao_Backlog_BL-015.md](../../governance/DHR-MC-LRN-001_Ata_Admissao_Backlog_BL-015.md) | DHR-MC-LRN-001 — Ata de Homologação da Admissão ao Backlog (BL-015 · Camada d... | 3 | 7 |
| [DHR-MC-RAG-001_Ata_Admissao_Backlog_BL-010.md](../../governance/DHR-MC-RAG-001_Ata_Admissao_Backlog_BL-010.md) | DHR-MC-RAG-001 — Ata de Homologação da Admissão ao Backlog (BL-010 · Camada RAG) | 4 | 7 |
| [DHR-MC-SKL-001_Ata_Admissao_Backlog_BL-016.md](../../governance/DHR-MC-SKL-001_Ata_Admissao_Backlog_BL-016.md) | DHR-MC-SKL-001 — Ata de Homologação da Admissão ao Backlog (BL-016 · Camada d... | 5 | 7 |
| [DHR-MECH-GATE-001_Ata_Check_Deterministico_Classe_Mecanismo.md](../../governance/DHR-MECH-GATE-001_Ata_Check_Deterministico_Classe_Mecanismo.md) | DHR-MECH-GATE-001 — Ata de Decisão — check determinístico da Classe/Mecanismo... | 29 | 3 |
| [DHR-MERGE-001_Ata_Aviso_Deterministico_Pronto_para_Mesclar.md](../../governance/DHR-MERGE-001_Ata_Aviso_Deterministico_Pronto_para_Mesclar.md) | DHR-MERGE-001 — Ata de Decisão — Aviso determinístico "já é possível e seguro... | 85 | 3 |
| [DHR-PAP-001-A_Adendo_Rehomologacao_PE-PR-PAP-001_v1.1.md](../../governance/DHR-PAP-001-A_Adendo_Rehomologacao_PE-PR-PAP-001_v1.1.md) | DHR-PAP-001-A — Adendo de Re-Homologação do PE-PR-PAP-001 v1.1 | 14 | 8 |
| [DHR-PAP-001-B_Ata_Homologacao_PAP-001.md](../../governance/DHR-PAP-001-B_Ata_Homologacao_PAP-001.md) | DHR-PAP-001-B — Ata de Homologação do PAP-001 v1.1 | 14 | 4 |
| [DHR-PAP-001-C_Ata_Homologacao_VPD_RMR-001.md](../../governance/DHR-PAP-001-C_Ata_Homologacao_VPD_RMR-001.md) | DHR-PAP-001-C — Ata de Homologação: VPD (Bloco 7), Wiring RMR-001 e Painel RM... | 14 | 6 |
| [DHR-PAP-001_Ata_Homologacao_Camada_Principios.md](../../governance/DHR-PAP-001_Ata_Homologacao_Camada_Principios.md) | DHR-PAP-001 — Ata de Homologação da Camada de Princípios do SOT | 14 | 8 |
| [DHR-PCC-001_Ata_Homologacao_Fase1_Continuidade_Contexto.md](../../governance/DHR-PCC-001_Ata_Homologacao_Fase1_Continuidade_Contexto.md) | DHR-PCC-001 — Ata — Fase 1 do PCC-001: continuidade de contexto entre sessões... | 10 | 10 |
| [DHR-PCC-002_Ata_Fase2_Detector_e_Hooks_do_Handoff.md](../../governance/DHR-PCC-002_Ata_Fase2_Detector_e_Hooks_do_Handoff.md) | DHR-PCC-002 — Ata — Fase 2 do PCC-001: detector, hooks e CI informativo do HA... | 5 | 5 |
| [DHR-PCC-003_Ata_Anexo_de_Tarefa_do_HANDOFF.md](../../governance/DHR-PCC-003_Ata_Anexo_de_Tarefa_do_HANDOFF.md) | DHR-PCC-003 — Ata — Anexo de tarefa: extensão do HANDOFF para trabalho entre ... | 30 | 9 |
| [DHR-PRE-ENTREGA-001_Ata_Pre_Gate_Unificado_e_Higiene_do_Especificador.md](../../governance/DHR-PRE-ENTREGA-001_Ata_Pre_Gate_Unificado_e_Higiene_do_Especificador.md) | DHR-PRE-ENTREGA-001 — Ata de Decisão — Pré-gate unificado antes do Revisor (P... | 9 | 7 |
| [DHR-PRINC-BID-001_Ata_Homologacao_Heranca_Bidirecional.md](../../governance/DHR-PRINC-BID-001_Ata_Homologacao_Heranca_Bidirecional.md) | DHR-PRINC-BID-001 — Ata de Homologação — Herança Principiológica Bidirecional | 9 | 10 |
| [DHR-PROV-WEB-001_Ata_Provisao_Pesquisa_Web_Especificador.md](../../governance/DHR-PROV-WEB-001_Ata_Provisao_Pesquisa_Web_Especificador.md) | DHR-PROV-WEB-001 — Ata de Homologação — Provisão de Pesquisa Web ao Especific... | 32 | 2 |
| [DHR-REAPONT-001_Ata_Homologacao_Erratum_Reapontamento.md](../../governance/DHR-REAPONT-001_Ata_Homologacao_Erratum_Reapontamento.md) | DHR-REAPONT-001 — Ata de Homologação — ERRATUM-REAPONT-001 (re-apontamento SP... | 93 | 17 |
| [DHR-REG-001_Ata_Homologacao_Registro_Familias_Cognitivas.md](../../governance/DHR-REG-001_Ata_Homologacao_Registro_Familias_Cognitivas.md) | DHR-REG-001 — Ata de Homologação — Registro Físico das 11 Famílias Cognitivas... | 18 | 16 |
| [DHR-RETRO-001_Ata_Aprovacao_Propostas_P1-P6_e_Ordem_das_Erratas.md](../../governance/DHR-RETRO-001_Ata_Aprovacao_Propostas_P1-P6_e_Ordem_das_Erratas.md) | DHR-RETRO-001 — Ata de Decisão — Propostas P1–P6 das retrospectivas e ordem d... | 98 | 11 |
| [DHR-RETRO-002_Ata_Retrospectiva_SPEC-049_e_P7_P8_P9.md](../../governance/DHR-RETRO-002_Ata_Retrospectiva_SPEC-049_e_P7_P8_P9.md) | DHR-RETRO-002 — Ata de Decisão — Retrospectiva da SPEC-049 feita agora; propo... | 29 | 8 |
| [DHR-RETRO-003_Ata_P10_P11_P12_e_Proxima_Frente.md](../../governance/DHR-RETRO-003_Ata_P10_P11_P12_e_Proxima_Frente.md) | DHR-RETRO-003 — Ata de Decisão — Propostas P10, P11 e P12; próxima frente; me... | 26 | 5 |
| [DHR-REVISOR-DELTA-001_Ata_Revisao_por_Delta_com_Hash.md](../../governance/DHR-REVISOR-DELTA-001_Ata_Revisao_por_Delta_com_Hash.md) | DHR-REVISOR-DELTA-001 — Ata — Revisor SOT passa a revisar por delta (hash por... | 23 | 5 |
| [DHR-ROTEAMENTO-001_Ata_Decisoes_Roteamento_de_Modelos_Onda0.md](../../governance/DHR-ROTEAMENTO-001_Ata_Decisoes_Roteamento_de_Modelos_Onda0.md) | DHR-ROTEAMENTO-001 — Ata — Decisões D1–D6 sobre roteamento de modelos dos age... | 53 | 8 |
| [DHR-ROTEAMENTO-002_Ata_Troca_do_Especificador_para_Opus_5_5.md](../../governance/DHR-ROTEAMENTO-002_Ata_Troca_do_Especificador_para_Opus_5_5.md) | DHR-ROTEAMENTO-002 — Ata — Troca do modelo do Especificador SOT de claude-opu... | 35 | 6 |
| [DHR-ROTEAMENTO-003_Ata_Roteador_Deterministico_de_Modelos.md](../../governance/DHR-ROTEAMENTO-003_Ata_Roteador_Deterministico_de_Modelos.md) | DHR-ROTEAMENTO-003 — Ata — Roteador determinístico de modelo por tarefa (hook... | 83 | 8 |
| [DHR-ROTEAMENTO-004_Ata_Roteamento_de_Achados_Ordem_de_Correcao.md](../../governance/DHR-ROTEAMENTO-004_Ata_Roteamento_de_Achados_Ordem_de_Correcao.md) | DHR-ROTEAMENTO-004 — Ata de Decisão — Roteamento determinístico de ACHADOS (o... | 17 | 6 |
| [DHR-ROTEAMENTO-005_Ata_Orquestrador_Nao_Corrige_Achados_do_Revisor.md](../../governance/DHR-ROTEAMENTO-005_Ata_Orquestrador_Nao_Corrige_Achados_do_Revisor.md) | DHR-ROTEAMENTO-005 — Ata de Decisão — O Orquestrador não corrige achados do R... | 18 | 6 |
| [DHR-ROTEAMENTO-006_Ata_Orquestrador_Corrige_Menores_Mecanicos.md](../../governance/DHR-ROTEAMENTO-006_Ata_Orquestrador_Corrige_Menores_Mecanicos.md) | DHR-ROTEAMENTO-006 — Ata de Decisão — O Orquestrador identifica e corrige det... | 14 | 8 |
| [DHR-ROTEAMENTO-007_Ata_Roteamento_Obrigatorio_e_Detector_de_ID.md](../../governance/DHR-ROTEAMENTO-007_Ata_Roteamento_Obrigatorio_e_Detector_de_ID.md) | DHR-ROTEAMENTO-007 — Ata de Decisão — Roteamento de modelo obrigatório por ho... | 89 | 5 |
| [DHR-RPSA-001_Ata_Automacao_dos_Carimbos_RPSA.md](../../governance/DHR-RPSA-001_Ata_Automacao_dos_Carimbos_RPSA.md) | DHR-RPSA-001 — Ata — Automação determinística dos carimbos RPSA e sincronizaç... | 3 | 10 |
| [DHR-RPSA-002_Ata_Classificacao_RPSA_Automatica.md](../../governance/DHR-RPSA-002_Ata_Classificacao_RPSA_Automatica.md) | DHR-RPSA-002 — Ata — Classificação RPSA automática após a aprovação de Andraus | 3 | 7 |
| [DHR-SES-001_Ata_Homologacao_SES-001_EUA-E03.md](../../governance/DHR-SES-001_Ata_Homologacao_SES-001_EUA-E03.md) | DHR-SES-001 — Ata de Homologação: SES-001, EUA-E03 e Emenda de Inversões Cont... | 6 | 5 |
| [DHR-SPEC002-001_Ata_Homologacao_Abertura_SPEC-002.md](../../governance/DHR-SPEC002-001_Ata_Homologacao_Abertura_SPEC-002.md) | DHR-SPEC002-001 — Ata de Homologação — Abertura da SPEC-002 (Evidence & Evide... | 0 | 12 |
| [DHR-SPEC002-001_Ata_Homologacao_SPEC-002.md](../../governance/DHR-SPEC002-001_Ata_Homologacao_SPEC-002.md) | DHR-SPEC002-001 — Ata de Homologação — SPEC-002 v1.0 (Evidence & Evidence Pro... | 12 | 10 |
| [DHR-SPEC002-VERBATIM-001_Ata_Decisao_Captura_Verbatim_Diferida.md](../../governance/DHR-SPEC002-VERBATIM-001_Ata_Decisao_Captura_Verbatim_Diferida.md) | DHR-SPEC002-VERBATIM-001 — Ata de Decisão — Captura Verbatim Diferida (RULE-E... | 1 | 7 |
| [DHR-SPEC003-001_Ata_Homologacao_SPEC-003.md](../../governance/DHR-SPEC003-001_Ata_Homologacao_SPEC-003.md) | DHR-SPEC003-001 — Ata de Homologação — SPEC-003 v1.5 (Conviction Vector, Evid... | 23 | 20 |
| [DHR-SPEC004-001_Ata_Homologacao_Abertura_SPEC-004.md](../../governance/DHR-SPEC004-001_Ata_Homologacao_Abertura_SPEC-004.md) | DHR-SPEC004-001 — Ata de Homologação — Abertura da SPEC-004 (Cognitive Blackb... | 10 | 12 |
| [DHR-SPEC004-002_Ata_Homologacao_SPEC-004.md](../../governance/DHR-SPEC004-002_Ata_Homologacao_SPEC-004.md) | DHR-SPEC004-002 — Ata de Homologação — SPEC-004 (Cognitive Blackboard Protoco... | 7 | 11 |
| [DHR-SPEC004-003_Ata_Homologacao_Emenda_v1.2_SPEC-004.md](../../governance/DHR-SPEC004-003_Ata_Homologacao_Emenda_v1.2_SPEC-004.md) | DHR-SPEC004-003 — Ata de Homologação — Emenda v1.2 da SPEC-004 (Cognitive Bla... | 12 | 10 |
| [DHR-SPEC005-001_Ata_Homologacao_Abertura_SPEC-005.md](../../governance/DHR-SPEC005-001_Ata_Homologacao_Abertura_SPEC-005.md) | DHR-SPEC005-001 — Ata de Homologação — Abertura da SPEC-005 (Cognitive Event ... | 11 | 12 |
| [DHR-SPEC005-002_Ata_Homologacao_SPEC-005.md](../../governance/DHR-SPEC005-002_Ata_Homologacao_SPEC-005.md) | DHR-SPEC005-002 — Ata de Homologação — SPEC-005 (Cognitive Event Bus) v1.0 — ... | 14 | 12 |
| [DHR-SPEC006-001_Ata_Homologacao_Abertura_SPEC-006.md](../../governance/DHR-SPEC006-001_Ata_Homologacao_Abertura_SPEC-006.md) | DHR-SPEC006-001 — Ata de Homologação — Abertura da SPEC-006 (Cognitive Knowle... | 66 | 12 |
| [DHR-SPEC006-002_Ata_Homologacao_SPEC-006.md](../../governance/DHR-SPEC006-002_Ata_Homologacao_SPEC-006.md) | DHR-SPEC006-002 — Ata de Homologação — SPEC-006 (Cognitive Knowledge Graph) v... | 46 | 14 |
| [DHR-SPEC006-003_Ata_Homologacao_Errata_v1.11_SPEC-006.md](../../governance/DHR-SPEC006-003_Ata_Homologacao_Errata_v1.11_SPEC-006.md) | DHR-SPEC006-003 — Ata de Homologação — Errata v1.11 da SPEC-006 (Cognitive Kn... | 31 | 13 |
| [DHR-SPEC006-004_Ata_Homologacao_Errata_v1.12_SPEC-006.md](../../governance/DHR-SPEC006-004_Ata_Homologacao_Errata_v1.12_SPEC-006.md) | DHR-SPEC006-004 — Ata de Homologação — Errata v1.12 da SPEC-006 (Cognitive Kn... | 40 | 11 |
| [DHR-SPEC006-005_Ata_Homologacao_Errata_v1.13_SPEC-006.md](../../governance/DHR-SPEC006-005_Ata_Homologacao_Errata_v1.13_SPEC-006.md) | DHR-SPEC006-005 — Ata de Homologação — Errata aditiva v1.13 da SPEC-006 (liga... | 92 | 11 |
| [DHR-SPEC006-OPCAO2-001_Ata_Opcao2_Etapas_e_Nota_Aditiva_SPEC-006.md](../../governance/DHR-SPEC006-OPCAO2-001_Ata_Opcao2_Etapas_e_Nota_Aditiva_SPEC-006.md) | DHR-SPEC006-OPCAO2-001 — Ata — SPEC-006 em etapas (Opção 2) e nota aditiva ao... | 17 | 6 |
| [DHR-SPEC006-PEND-001_Ata_BL029_EmEspera_e_Emenda_atomic-spec_S3.md](../../governance/DHR-SPEC006-PEND-001_Ata_BL029_EmEspera_e_Emenda_atomic-spec_S3.md) | DHR-SPEC006-PEND-001 — Ata — BL-029 `Em espera` e emenda Minor ao `atomic-spe... | 8 | 12 |
| [DHR-SPEC007-001_Ata_Homologacao_Abertura_SPEC-007.md](../../governance/DHR-SPEC007-001_Ata_Homologacao_Abertura_SPEC-007.md) | DHR-SPEC007-001 — Ata de Homologação — Abertura da SPEC-007 (RAG / WikiRAG / ... | 44 | 13 |
| [DHR-SPEC007-002_Ata_Divisao_SPEC-007_e_Slot_SPEC-048.md](../../governance/DHR-SPEC007-002_Ata_Divisao_SPEC-007_e_Slot_SPEC-048.md) | DHR-SPEC007-002 — Ata de Decisão — Divisão da SPEC-007 (Opção C) e slot da SP... | 42 | 22 |
| [DHR-SPEC007-003_Ata_Respostas_Perguntas_P1-P11_SPEC-007.md](../../governance/DHR-SPEC007-003_Ata_Respostas_Perguntas_P1-P11_SPEC-007.md) | DHR-SPEC007-003 — Ata de Decisão — Respostas de Andraus às perguntas P-1..P-1... | 43 | 12 |
| [DHR-SPEC007-004_Ata_Respostas_P12-P14_e_Ordem_Rodada5_SPEC-007.md](../../governance/DHR-SPEC007-004_Ata_Respostas_P12-P14_e_Ordem_Rodada5_SPEC-007.md) | DHR-SPEC007-004 — Ata de Decisão — Respostas P-12..P-14 do Plan reduzido da S... | 32 | 9 |
| [DHR-SPEC007-005_Ata_Homologacao_Plan_Reduzido_SPEC-007.md](../../governance/DHR-SPEC007-005_Ata_Homologacao_Plan_Reduzido_SPEC-007.md) | DHR-SPEC007-005 — Ata de Homologação — Plan reduzido da SPEC-007 v2.3 (formaç... | 115 | 11 |
| [DHR-SPEC007-006_Ata_Decisao_Livro_Q7c.md](../../governance/DHR-SPEC007-006_Ata_Decisao_Livro_Q7c.md) | DHR-SPEC007-006 — Ata de Decisão — Q7(c): uso do livro *Evidence-Based Techni... | 65 | 9 |
| [DHR-SPEC007-007_Ata_Diretriz_Autenticacao_Criptografica_dos_Atos.md](../../governance/DHR-SPEC007-007_Ata_Diretriz_Autenticacao_Criptografica_dos_Atos.md) | DHR-SPEC007-007 — Ata de Decisão — Diretriz de autenticação criptográfica dos... | 90 | 6 |
| [DHR-SPEC019-001_Ata_Homologacao_SPEC-019.md](../../governance/DHR-SPEC019-001_Ata_Homologacao_SPEC-019.md) | DHR-SPEC019-001 — Ata de Homologação — SPEC-019 v1.0 (Harness Governance & Ev... | 17 | 6 |
| [DHR-SPEC020-001_Ata_Homologacao_SPEC-020.md](../../governance/DHR-SPEC020-001_Ata_Homologacao_SPEC-020.md) | DHR-SPEC020-001 — Ata de Homologação — SPEC-020 v1.0 (Harness Evaluation Spec... | 18 | 9 |
| [DHR-SPEC020-002_Ata_Homologacao_Erratum_SPEC020-002_F1.md](../../governance/DHR-SPEC020-002_Ata_Homologacao_Erratum_SPEC020-002_F1.md) | DHR-SPEC020-002 — Ata de Homologação — ERRATUM-SPEC020-002 (dimensão B "RAG f... | 89 | 14 |
| [DHR-SPEC021-001_Ata_Homologacao_SPEC-021.md](../../governance/DHR-SPEC021-001_Ata_Homologacao_SPEC-021.md) | DHR-SPEC021-001 — Ata de Homologação — SPEC-021 v1.0 (Harness Score / Maturit... | 8 | 7 |
| [DHR-SPEC038-001_Ata_Homologacao_Abertura_SPEC-038.md](../../governance/DHR-SPEC038-001_Ata_Homologacao_Abertura_SPEC-038.md) | DHR-SPEC038-001 — Ata de Homologação — Abertura da SPEC-038 (Trading Analysis... | 9 | 14 |
| [DHR-SPEC038-002_Ata_Homologacao_SPEC-038.md](../../governance/DHR-SPEC038-002_Ata_Homologacao_SPEC-038.md) | DHR-SPEC038-002 — Ata de Homologação — SPEC-038 (Trading Analysis Tool Harnes... | 14 | 12 |
| [DHR-SPEC046-001_Ata_Homologacao_Abertura_SPEC-046.md](../../governance/DHR-SPEC046-001_Ata_Homologacao_Abertura_SPEC-046.md) | DHR-SPEC046-001 — Ata de Homologação — Abertura da SPEC-046 (Spec-Time Contex... | 7 | 11 |
| [DHR-SPEC046-002_Ata_Homologacao_SPEC-046.md](../../governance/DHR-SPEC046-002_Ata_Homologacao_SPEC-046.md) | DHR-SPEC046-002 — Ata de Homologação — SPEC-046 v1.0 (Spec-Time Context Cachi... | 6 | 14 |
| [DHR-SPEC046-003_Ata_Homologacao_SPEC-046_v1.1.md](../../governance/DHR-SPEC046-003_Ata_Homologacao_SPEC-046_v1.1.md) | DHR-SPEC046-003 — Ata de Homologação — SPEC-046 v1.1 (Emenda: Caching Inter-S... | 4 | 8 |
| [DHR-SPEC048-001_Ata_Homologacao_Abertura_SPEC-048.md](../../governance/DHR-SPEC048-001_Ata_Homologacao_Abertura_SPEC-048.md) | DHR-SPEC048-001 — Ata de Homologação — Abertura da SPEC-048 (RAG Retrieval & ... | 36 | 17 |
| [DHR-SPEC048-002_Ata_Homologacao_Plan_SPEC-048.md](../../governance/DHR-SPEC048-002_Ata_Homologacao_Plan_SPEC-048.md) | DHR-SPEC048-002 — Ata de Homologação — Plan da SPEC-048 v1.4 (RAG Retrieval &... | 99 | 16 |
| [DHR-SPEC049-001_Ata_Homologacao_Abertura_SPEC-049.md](../../governance/DHR-SPEC049-001_Ata_Homologacao_Abertura_SPEC-049.md) | DHR-SPEC049-001 — Ata de Homologação — Abertura da SPEC-049 (WikiRAG Reading ... | 75 | 18 |
| [DHR-SPEC049-002_Ata_Homologacao_Plan_SPEC-049.md](../../governance/DHR-SPEC049-002_Ata_Homologacao_Plan_SPEC-049.md) | DHR-SPEC049-002 — Ata de Homologação — Plan da SPEC-049 v1.2 (WikiRAG Reading... | 45 | 12 |
| [DHR-TAX-001_Ata_Alinhamento_Taxonomico.md](../../governance/DHR-TAX-001_Ata_Alinhamento_Taxonomico.md) | DHR-TAX-001 — Ata de Alinhamento Taxonômico — 4 Correções de Bloqueadores Crí... | 11 | 9 |
| [DHR-TELEMETRIA-CUSTO-001_Ata_Telemetria_Tokens_Construtores.md](../../governance/DHR-TELEMETRIA-CUSTO-001_Ata_Telemetria_Tokens_Construtores.md) | DHR-TELEMETRIA-CUSTO-001 — Ata de Decisão — Telemetria de tokens dos agentes ... | 50 | 5 |
| [DHR-VERBATIM-SRC-001_Ata_Homologacao_Captura_Verbatim.md](../../governance/DHR-VERBATIM-SRC-001_Ata_Homologacao_Captura_Verbatim.md) | DHR-VERBATIM-SRC-001 — Ata de Homologação — Captura Verbatim de Fonte (RULE-E... | 12 | 10 |
| [DHR-WF-001_Ata_Homologacao_WORKFLOW_Soberano.md](../../governance/DHR-WF-001_Ata_Homologacao_WORKFLOW_Soberano.md) | DHR-WF-001 — Ata de Homologação — WORKFLOW.md soberano na raiz + conformidade... | 9 | 8 |
| [DHR-WF-002_Ata_Homologacao_WORKFLOW_v2.md](../../governance/DHR-WF-002_Ata_Homologacao_WORKFLOW_v2.md) | DHR-WF-002 — Ata de Homologação — WORKFLOW.md v2.0 (decisões sobre o Dossiê d... | 5 | 8 |
| [EMENDA-SPEC001-001_hierarchy_role_PROPOSTA.md](../../governance/EMENDA-SPEC001-001_hierarchy_role_PROPOSTA.md) | [HOMOLOGADO — aplicado em 2026-10-05, DHR-AUDIT-SPEC001-001] EMENDA-SPEC001-0... | 1 | 15 |
| [ERRATUM-REAPONT-001_Re-apontamento_SPEC-007_para_SPEC-048.md](../../governance/ERRATUM-REAPONT-001_Re-apontamento_SPEC-007_para_SPEC-048.md) | ERRATUM-REAPONT-001: errata aditiva de re-apontamento (recuperação e pacote: ... | 101 | 35 |
| [ERRATUM-SPEC001-001_Ancora_SAS-001_6.10.md](../../governance/ERRATUM-SPEC001-001_Ancora_SAS-001_6.10.md) | ERRATUM-SPEC001-001 — Âncora de fonte: SAS-001 §6.7 → §6.10 (metadados de tra... | 3 | 5 |
| [ERRATUM-SPEC001-002_Auditoria_Semantica_Aditivo_PROPOSTO.md](../../governance/ERRATUM-SPEC001-002_Auditoria_Semantica_Aditivo_PROPOSTO.md) | [HOMOLOGADO — aplicado em 2026-10-05, DHR-AUDIT-SPEC001-001] ERRATUM-SPEC001-... | 3 | 21 |
| [ERRATUM-SPEC005-001_Estado_BL-008.md](../../governance/ERRATUM-SPEC005-001_Estado_BL-008.md) | ERRATUM-SPEC005-001 — Estado do BL-008: `Absorvido`, não `ATIVADO` — erratum ... | 1 | 13 |
| [ERRATUM-SPEC019-001_PROPOSTA.md](../../governance/ERRATUM-SPEC019-001_PROPOSTA.md) | ERRATUM-SPEC019-001 — Correção aditiva do status de L-001 na SPEC-019 homolog... | 0 | 11 |
| [ERRATUM-SPEC020-001_Fechamento_tool_correctness.md](../../governance/ERRATUM-SPEC020-001_Fechamento_tool_correctness.md) | ERRATUM-SPEC020-001 — Fechamento da dimensão B "tool correctness" (BL-017) — ... | 6 | 9 |
| [ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md](../../governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md) | ERRATUM-SPEC020-002 — Dimensão B "RAG faithfulness", metade F1 (fidelidade do... | 5 | 32 |
| [ESTUDO-GARANTIAS-DETERMINISTICAS-2026-10-17.md](../../governance/ESTUDO-GARANTIAS-DETERMINISTICAS-2026-10-17.md) | Estudo — garantias determinísticas para prevenir os erros de coesão (hooks, r... | 29 | 8 |
| [EUA-E04_Heranca_Delta_PROPOSTA.md](../../governance/EUA-E04_Heranca_Delta_PROPOSTA.md) | EUA-E04 — Bloco "Herança / Delta" no atomic-spec §8 (PROPOSTA) | 3 | 6 |
| [EUA-E05_Epistemic_Check_PROPOSTA.md](../../governance/EUA-E05_Epistemic_Check_PROPOSTA.md) | EUA-E05 — Epistemic Check no atomic-spec §11 (PROPOSTA) | 3 | 8 |
| [EUA-E06_Camada_Semantica_PROPOSTA.md](../../governance/EUA-E06_Camada_Semantica_PROPOSTA.md) | EUA-E06 — Camada Semântica: Terminologia Concorrente + RULE-SEM (PROPOSTA) | 3 | 8 |
| [EUA-E07_Camada_Ontologica_PROPOSTA.md](../../governance/EUA-E07_Camada_Ontologica_PROPOSTA.md) | EUA-E07 — Camada Ontológica: RULE-ONT (observacional vs teórico) + nó N10 (PR... | 2 | 9 |
| [EUA-E08_Camada_Inquerito_PROPOSTA.md](../../governance/EUA-E08_Camada_Inquerito_PROPOSTA.md) | EUA-E08 — Camada de Inquérito: RULE-INQ (classificação de questão + evidência... | 2 | 8 |
| [EUA-E09_Camada_Causal_PROPOSTA.md](../../governance/EUA-E09_Camada_Causal_PROPOSTA.md) | EUA-E09 — Camada Causal: RULE-CAU (mecanismo obrigatório + regime + guard pós... | 2 | 8 |
| [EUA-E10_Camada_Contrafactual_PROPOSTA.md](../../governance/EUA-E10_Camada_Contrafactual_PROPOSTA.md) | EUA-E10 — Camada Contrafactual: RULE-CTF (baseline + intervenção mínima + ant... | 2 | 8 |
| [EUA-E11_Camada_Incerteza_PROPOSTA.md](../../governance/EUA-E11_Camada_Incerteza_PROPOSTA.md) | EUA-E11 — Camada de Incerteza: RULE-UNC (localizar/tipificar + não-contaminaç... | 2 | 9 |
| [EUA-E12_Camada_Probabilistica_PROPOSTA.md](../../governance/EUA-E12_Camada_Probabilistica_PROPOSTA.md) | EUA-E12 — Camada Probabilística: RULE-PRB (evento bem-formado + não quantific... | 2 | 9 |
| [EUA-E13_Camada_Decisional_PROPOSTA.md](../../governance/EUA-E13_Camada_Decisional_PROPOSTA.md) | EUA-E13 — Camada Decisional: RULE-DEC (decisão≠execução+autoridade · condicio... | 2 | 12 |
| [EUA-E14_Camada_Metacognicao_PROPOSTA.md](../../governance/EUA-E14_Camada_Metacognicao_PROPOSTA.md) | EUA-E14 — Camada Metacognição: RULE-MET (honestidade/não-fabricação · abstenç... | 2 | 12 |
| [EUA-E15_Redesignacao_Piloto_SPEC-001_PROPOSTA.md](../../governance/EUA-E15_Redesignacao_Piloto_SPEC-001_PROPOSTA.md) | EUA-E15 — Redesignação do Piloto de Incorporação para SPEC-001 (auditoria ret... | 4 | 18 |
| [EUA-E16_Sincronizacao_Agentes_PROPOSTA.md](../../governance/EUA-E16_Sincronizacao_Agentes_PROPOSTA.md) | EUA-E16 — Sincronização das Definições dos Agentes + Regra Permanente de Sinc... | 3 | 12 |
| [EUA-E17_Reposicionamento_Specs_Governanca_Harness_PROPOSTA.md](../../governance/EUA-E17_Reposicionamento_Specs_Governanca_Harness_PROPOSTA.md) | EUA-E17 — Reposicionamento das Specs de Governança do Harness no ROADMAP (PRO... | 2 | 25 |
| [EUA-E18_Reducao_Vies_Sincronizacao_SpecLean_PROPOSTA.md](../../governance/EUA-E18_Reducao_Vies_Sincronizacao_SpecLean_PROPOSTA.md) | EUA-E18 — Redução de Viés e Uso Sincronizado da Spec-Lean entre Especificador... | 2 | 19 |
| [EUA-E19_Economia_Tokens_Camada_Meta_PROPOSTA.md](../../governance/EUA-E19_Economia_Tokens_Camada_Meta_PROPOSTA.md) | EUA-E19 — Economia de Tokens na Camada Meta (Especificador/Revisor): Roteamen... | 2 | 15 |
| [EUA-E19a_Restauracao_Signal_Package_PROPOSTA.md](../../governance/EUA-E19a_Restauracao_Signal_Package_PROPOSTA.md) | EUA-E19a — Restauração Semântica do "Signal Package" (fronteira) + TMP intern... | 0 | 16 |
| [EUA-E20_Fase_RISK_Slots_PROPOSTA.md](../../governance/EUA-E20_Fase_RISK_Slots_PROPOSTA.md) | EUA-E20 — FASE RISK: slots-macro indicativos da família RISK-SPEC (PROPOSTA) | 2 | 17 |
| [EUA-E21_Especificacao_Emergente_Pesquisa_Web_PROPOSTA.md](../../governance/EUA-E21_Especificacao_Emergente_Pesquisa_Web_PROPOSTA.md) | EUA-E21 — Especificação Emergente: o ROADMAP não pré-determina Specs nem quan... | 1 | 23 |
| [EUA-E22_Manutencao_Mapa_Projeto_PROPOSTA.md](../../governance/EUA-E22_Manutencao_Mapa_Projeto_PROPOSTA.md) | EUA-E22 — Manutenção obrigatória do Mapa do Projeto (BL-019) por todos os age... | 1 | 12 |
| [EUA-E23_Manager_Unificado_SPEC008_SPEC015_PROPOSTA.md](../../governance/EUA-E23_Manager_Unificado_SPEC008_SPEC015_PROPOSTA.md) | EUA-E23 — Manager Agent Unificado: simetria camadas×agentes e quantidade de S... | 2 | 17 |
| [GPR-001_Guia_Principios_Relacoes_SOT.md](../../governance/GPR-001_Guia_Principios_Relacoes_SOT.md) | GPR-001 — Guia de Princípios, Relações e Organicidade do SOT | 59 | 13 |
| [HOD-001_Plano_Higiene_Organizacao_Documental_PROPOSTA.md](../../governance/HOD-001_Plano_Higiene_Organizacao_Documental_PROPOSTA.md) | HOD-001 — Plano de Higiene e Organização Documental (PROPOSTA) | 23 | 11 |
| [MAN-001_Mapa_Arquitetura_Normativa_PROPOSTA.md](../../governance/MAN-001_Mapa_Arquitetura_Normativa_PROPOSTA.md) | MAN-001 — Mapa da Arquitetura Normativa (PROPOSTA) | 47 | 18 |
| [MANUAL_UNIVERSAL_ENGENHARIA_DE_PRINCIPIOS_AGENTICOS.md](../../governance/MANUAL_UNIVERSAL_ENGENHARIA_DE_PRINCIPIOS_AGENTICOS.md) | MANUAL UNIVERSAL DE ENGENHARIA DE PRINCÍPIOS, PONDERAÇÃO E DINÂMICA PARA SIST... | 1 | 0 |
| [MAPA-AUDITORIA-SAS-001.md](../../governance/MAPA-AUDITORIA-SAS-001.md) | Mapa de Auditoria do SAS-001 (BL-009) — reavaliação sob SES-001 §59/§60 | 2 | 15 |
| [MAPA-AUDITORIA-SPEC-001.md](../../governance/MAPA-AUDITORIA-SPEC-001.md) | Mapa de Auditoria da SPEC-001 (BL-008) — versão canônica completa (14 linhas) | 8 | 32 |
| [MAPA-AUDITORIA-SPEC-001_LINHAS-ADICIONAIS_RASCUNHO.md](../../governance/MAPA-AUDITORIA-SPEC-001_LINHAS-ADICIONAIS_RASCUNHO.md) | Mapa de Auditoria da SPEC-001 (BL-008) — linhas adicionais EUA-E21 e EUA-E22 ... | 8 | 16 |
| [PAP-001_Protocolo_Adesao_Progressiva_Principios.md](../../governance/PAP-001_Protocolo_Adesao_Progressiva_Principios.md) | PAP-001 — Protocolo de Adesão Progressiva da Camada de Princípios do SOT | 23 | 17 |
| [PCC-001_Plano_Continuidade_Contexto_Build_PROPOSTA.md](../../governance/PCC-001_Plano_Continuidade_Contexto_Build_PROPOSTA.md) | PCC-001 — Plano de Continuidade de Contexto e Memória entre Sessões do Orques... | 184 | 14 |
| [PE-PR-PAP-001_Prompts_Especificador_Revisor_PAP001.md](../../governance/PE-PR-PAP-001_Prompts_Especificador_Revisor_PAP001.md) | PE-PR-PAP-001 — Prompts de Invocação do Especificador e do Revisor para o PAP... | 9 | 13 |
| [PP-PAP-001_Pacote_Partida_Protocolo_Adesao_Progressiva.md](../../governance/PP-PAP-001_Pacote_Partida_Protocolo_Adesao_Progressiva.md) | PP-PAP-001 — Pacote de Partida do PAP-001 | 12 | 5 |
| [RCH-001_Registro_Ciclos_Hygiene.md](../../governance/RCH-001_Registro_Ciclos_Hygiene.md) | RCH-001 — Registro de Ciclos de Hygiene de Princípios | 19 | 22 |
| [RULES.md](../../governance/RULES.md) | Rules — SOT (Sistema Operacional de Trading) | 482 | 41 |
| [SES-001_Especializacao_Cognitiva_Trading.md](../../governance/SES-001_Especializacao_Cognitiva_Trading.md) | EMENDA SES-001 | 61 | 3 |
| [CAUSAS-PREVENCAO.md](../../governance/aprendizado/CAUSAS-PREVENCAO.md) | CAUSAS E PREVENÇÃO DOS ACHADOS RECORRENTES (LOOP-001 / DHR-LOOP-001) | 19 | 7 |
| [LEDGER-ACHADOS.md](../../governance/aprendizado/LEDGER-ACHADOS.md) | LEDGER DE ACHADOS DO LOOP DOS CONSTRUTORES — GERADO (não editar à mão) | 22 | 52 |
| [RETROSPECTIVAS.md](../../governance/aprendizado/RETROSPECTIVAS.md) | RETROSPECTIVAS DE FECHAMENTO DO LOOP DOS CONSTRUTORES (LOOP-001 / DHR-LOOP-001) | 90 | 30 |
| [TELEMETRIA-TOKENS.md](../../governance/aprendizado/TELEMETRIA-TOKENS.md) | TELEMETRIA DE TOKENS DOS CONSTRUTORES — retrato (gerado por `python scripts/t... | 14 | 3 |
| [RELATORIO.md](../../governance/propostas/AUDITORIA-INDEPENDENTE-SPEC006/RELATORIO.md) | Auditoria Independente e Adversarial: SPEC-006 v1.7 (Cognitive Knowledge Grap... | 14 | 15 |
| [ESTUDO-TECNOLOGIA-H001-2026-10-18.md](../../governance/propostas/H001/ESTUDO-TECNOLOGIA-H001-2026-10-18.md) | ESTUDO DE TECNOLOGIA — H-001: mecanismo físico de armazenamento da memória pe... | 11 | 11 |
| [HANDOFF-SPEC006-2026-10-17.md](../../governance/propostas/HANDOFF-SPEC006-2026-10-17.md) | Passagem de sessão — SPEC-006 (errata) e endurecimento do gate — 2026-10-17 | 3 | 16 |
| [AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md) | Auditoria — burocracia excessiva (método, ferramentas, agentes) e higiene de ... | 53 | 36 |
| [AUDITORIA-ESPECIFICADOR-PRECHECK-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-ESPECIFICADOR-PRECHECK-2026-11-01.md) | Auditoria do Especificador — Autopré-check e prevenção determinística de erros | 10 | 12 |
| [AUDITORIA-HIGIENE-E-ECONOMICIDADE-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-HIGIENE-E-ECONOMICIDADE-2026-10-31.md) | Auditoria profunda — higiene de leitura e economicidade (4Es) do repositório | 40 | 18 |
| [PROPOSTA-A2-1-MAPA-JSON-LOCAL-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A2/PROPOSTA-A2-1-MAPA-JSON-LOCAL-2026-10-31.md) | Proposta pré-testada — A2.1: `mapa-projeto.json` fora da árvore versionada | 0 | 1 |
| [MEDICAO-A6-2-HISTORICO-DOS-DETECTORES-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/MEDICAO-A6-2-HISTORICO-DOS-DETECTORES-2026-11-01.md) | Medição A6.2 — o que os detectores acharam nos últimos 30 merges da `main` | 0 | 0 |
| [PREPARO-ARQUIVAMENTO-AUDITOR-EXTERNO-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PREPARO-ARQUIVAMENTO-AUDITOR-EXTERNO-2026-11-01.md) | Preparo — arquivar o Auditor Externo (A6.3) | 0 | 5 |
| [PROPOSTA-A6-4-E-A6-1-PARCIAL-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PROPOSTA-A6-4-E-A6-1-PARCIAL-2026-11-01.md) | Proposta pré-testada — A6.4 + A6.1 parcial (doc-sync) | 0 | 1 |
| [PROPOSTA-A6-AVISOS-FIXOS-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/A6/PROPOSTA-A6-AVISOS-FIXOS-2026-11-01.md) | Proposta pré-testada — tratar os avisos permanentes (A6.2 reformulado) | 0 | 4 |
| [ARQUIVO-MORTO-AGENTS-secao7-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/ARQUIVO-MORTO-AGENTS-secao7-2026-10-31.md) | Arquivo morto — AGENTS.md §7 (texto integral até 2026-10-31) | 1 | 29 |
| [PROPOSTA-P11-HANDOFF-POR-RAMO-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/P11/PROPOSTA-P11-HANDOFF-POR-RAMO-2026-10-31.md) | Proposta pré-testada — P11: handoff por ramo como regra (e `check_handoff` en... | 0 | 3 |
| [PROPOSTA-CORTES-RESTANTES-AGENTS-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/PROPOSTA-CORTES-RESTANTES-AGENTS-2026-10-31.md) | Proposta pré-testada — demais cortes do AGENTS.md (§2, §5, §8, §9, §12) | 3 | 6 |
| [PROPOSTA-PROVA-DE-EQUIVALENCIA-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/PROPOSTA-PROVA-DE-EQUIVALENCIA-2026-10-31.md) | Proposta pré-testada — prova de conservação para enxugar documentos quentes (... | 0 | 8 |
| [RESULTADO.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/RESULTADO.md) | Teste A/B barato e controlado — o AGENTS.md enxuto ainda deixa um agente resp... | 2 | 2 |
| [RESULTADO.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/cenarios/RESULTADO.md) | Teste de cenários (aplicação de regras) — AGENTS.md original (A) × atual (E) | 0 | 6 |
| [cenarios.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/cenarios/cenarios.md) | Cenários (responda cada um em UMA linha: `S<n>: <decisão/ação> — <regra em 1 ... | 0 | 0 |
| [RESULTADO.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/RESULTADO.md) | Pré-teste adversarial do canal `GATE-D` (P8, `DHR-AGENTS-P8-001`) | 0 | 2 |
| [cenarios.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/cenarios.md) | Cenários do Revisor (responda cada um em UMA linha: `C<n>: <o que o parecer f... | 0 | 0 |
| [revisor-sec3.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/p8-gate-d/revisor-sec3.md) | revisor-sec3 | 0 | 2 |
| [perguntas.md](../../governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/perguntas.md) | Perguntas (responda cada uma em UMA linha curta, formato `Q<n>: <resposta>`; ... | 0 | 0 |
| [PROPOSTA-PRE-ENTREGA-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/PRE-ENTREGA/PROPOSTA-PRE-ENTREGA-2026-11-01.md) | P-A + P-F — pré-gate unificado e higiene do especificador.md | 5 | 6 |
| [PROPOSTA-A2-RITUAL-DE-FECHAMENTO-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-A2-RITUAL-DE-FECHAMENTO-2026-10-31.md) | Proposta A2 — Ritual de fechamento manual (medida antes de cortar) | 0 | 6 |
| [PROPOSTA-A3-PAUTA-DE-DECISOES-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-A3-PAUTA-DE-DECISOES-2026-11-01.md) | Proposta A3 — Pauta única de decisões de Andraus (decisão em lote) | 0 | 7 |
| [PROPOSTA-A6-MECANISMOS-EM-CAMADAS-2026-11-01.md](../../governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-A6-MECANISMOS-EM-CAMADAS-2026-11-01.md) | Proposta A6 — Mecanismos em camadas e caducidade (medida antes de cortar) | 1 | 4 |
| [PROPOSTA-DIMENSIONAMENTO-DE-SPEC-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-DIMENSIONAMENTO-DE-SPEC-2026-10-31.md) | Proposta — dimensionamento de Spec: critério medido para "uma Spec ou várias" | 2 | 17 |
| [PROPOSTA-EXPERIMENTO-REGRA-DE-PARADA-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-EXPERIMENTO-REGRA-DE-PARADA-2026-10-31.md) | Proposta — experimento da regra de parada de rodadas (A1 da auditoria de buro... | 8 | 10 |
| [PROPOSTA-PATCH-CHECK-REFS-E-MAPA-2026-10-31.md](../../governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-PATCH-CHECK-REFS-E-MAPA-2026-10-31.md) | Proposta pré-testada — falsos positivos do check_refs e destino do mapa JSON | 12 | 2 |
| [RELATORIO-MELHORIAS-AGENTES-E-GATES-2026-10-24.md](../../governance/propostas/MELHORIAS-PROCESSO/RELATORIO-MELHORIAS-AGENTES-E-GATES-2026-10-24.md) | Relatório — pontos fracos dos agentes construtores (Especificador e Revisor) ... | 17 | 7 |
| [MINUTA-ATA-REGISTRO-MECANISMOS-VIGENTE-2026-10-18.md](../../governance/propostas/MINUTA-ATA-REGISTRO-MECANISMOS-VIGENTE-2026-10-18.md) | MINUTA — Ata de vigência do registro de mecanismos (`governance/MECANISMOS.js... | 4 | 4 |
| [PARECER-REVISOR-SPEC006-v1.10-2026-10-17.md](../../governance/propostas/PARECER-REVISOR-SPEC006-v1.10-2026-10-17.md) | Parecer do Revisor SOT — SPEC-006 errata v1.10 (rodada por delta) — 2026-10-17 | 4 | 3 |
| [PARECER-REVISOR-SPEC006-v1.11-2026-10-18.md](../../governance/propostas/PARECER-REVISOR-SPEC006-v1.11-2026-10-18.md) | Parecer do Revisor SOT — SPEC-006 errata v1.11 (rodada por delta) — 2026-10-18 | 8 | 6 |
| [PARECER-REVISOR-SPEC006-v1.12-2026-10-18.md](../../governance/propostas/PARECER-REVISOR-SPEC006-v1.12-2026-10-18.md) | PARECER DO REVISOR SOT — SPEC-006 errata v1.12 (revisão por delta, revisor.md... | 8 | 11 |
| [PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md](../../governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md) | PLANO — Fechar a H-001 sem quebra documental + roteamento de modelos por tare... | 8 | 13 |
| [PARECER-REVISOR-ERRATUM-REAPONT-001-R1-2026-10-30.md](../../governance/propostas/REAPONT/PARECER-REVISOR-ERRATUM-REAPONT-001-R1-2026-10-30.md) | Parecer do Revisor — ERRATUM-REAPONT-001 v1.0 (R1, S2/sonnet) — 2026-10-30 | 3 | 10 |
| [PARECER-REVISOR-ERRATUM-REAPONT-001-R2-2026-10-31.md](../../governance/propostas/REAPONT/PARECER-REVISOR-ERRATUM-REAPONT-001-R2-2026-10-31.md) | Parecer do Revisor — ERRATUM-REAPONT-001 v1.2 — R2 por delta (S2, sonnet) — 2... | 3 | 8 |
| [PARECER-REVISOR-ERRATUM-REAPONT-001-R3-2026-10-31.md](../../governance/propostas/REAPONT/PARECER-REVISOR-ERRATUM-REAPONT-001-R3-2026-10-31.md) | Parecer do Revisor — ERRATUM-REAPONT-001 v1.3 — R3 delta curta (S2, sonnet) —... | 3 | 3 |
| [PARECER-REVISOR-ERRATUM-REAPONT-001-R4-2026-10-31.md](../../governance/propostas/REAPONT/PARECER-REVISOR-ERRATUM-REAPONT-001-R4-2026-10-31.md) | Parecer do Revisor — ERRATUM-REAPONT-001 v1.4 — R4 delta curta (S2, sonnet) —... | 3 | 2 |
| [AUDITORIA-ROTEAMENTO-MODELOS_PROPOSTA.md](../../governance/propostas/ROTEAMENTO-MODELOS/AUDITORIA-ROTEAMENTO-MODELOS_PROPOSTA.md) | Auditoria de tarefas por criticidade e Dossiê de roteamento de modelos (camad... | 4 | 21 |
| [TELEMETRIA-ONDA0.md](../../governance/propostas/ROTEAMENTO-MODELOS/TELEMETRIA-ONDA0.md) | Telemetria manual — onda 0 de roteamento (rascunho, não normativo) | 15 | 4 |
| [ERRATUM-SPEC002-001_Aditivo_PROPOSTO.md](../../governance/propostas/SPEC-002/ERRATUM-SPEC002-001_Aditivo_PROPOSTO.md) | [ERRATUM-PROPOSTO — NÃO APLICADO] ERRATUM-SPEC002-001 — Erratum ADITIVO único... | 0 | 19 |
| [REAUDITORIA-SPEC002-001_PROPOSTA-CORRECOES.md](../../governance/propostas/SPEC-002/REAUDITORIA-SPEC002-001_PROPOSTA-CORRECOES.md) | REAUDITORIA-SPEC002-001 — Proposta de Correções — SPEC-002 | 1 | 6 |
| [LISTA-RAMOS-E-PRS-OBSOLETOS-2026-10-18.md](../../governance/propostas/SPEC-006/LISTA-RAMOS-E-PRS-OBSOLETOS-2026-10-18.md) | Lista — ramos remotos e PRs candidatos a limpeza (2026-10-18) | 11 | 4 |
| [MINUTA-ATA-HOMOLOGACAO-ERRATA-v1.11.md](../../governance/propostas/SPEC-006/MINUTA-ATA-HOMOLOGACAO-ERRATA-v1.11.md) | MINUTA — Ata de homologação da errata v1.11 da SPEC-006 (Cognitive Knowledge ... | 5 | 11 |
| [PARECER-REVISOR-SPEC006-ERRATA-v1.13-R1-2026-10-25.md](../../governance/propostas/SPEC-006/PARECER-REVISOR-SPEC006-ERRATA-v1.13-R1-2026-10-25.md) | Parecer do Revisor — Errata aditiva v1.13 à SPEC-006 (R1) — 2026-10-25 | 1 | 5 |
| [PARECER-REVISOR-SPEC006-ERRATA-v1.13-R2-2026-10-25.md](../../governance/propostas/SPEC-006/PARECER-REVISOR-SPEC006-ERRATA-v1.13-R2-2026-10-25.md) | Parecer do Revisor — Errata aditiva v1.13 à SPEC-006 (R2, por delta) — 2026-1... | 2 | 3 |
| [PARECER-REVISOR-SPEC006-ERRATA-v1.13-R3-2026-10-25.md](../../governance/propostas/SPEC-006/PARECER-REVISOR-SPEC006-ERRATA-v1.13-R3-2026-10-25.md) | Parecer do Revisor — Errata aditiva v1.13 à SPEC-006 (R3, v1.2, delta com B1 ... | 2 | 4 |
| [PARECER-REVISOR-SPEC006-ERRATA-v1.13-R4-2026-10-25.md](../../governance/propostas/SPEC-006/PARECER-REVISOR-SPEC006-ERRATA-v1.13-R4-2026-10-25.md) | Parecer do Revisor — Errata aditiva v1.13 à SPEC-006 (R4, v1.3, delta curto) ... | 1 | 3 |
| [PROPOSTA-DIVISAO-2026-10-17.md](../../governance/propostas/SPEC-006/PROPOSTA-DIVISAO-2026-10-17.md) | PROPOSTA — Divisão da SPEC-006 (Cognitive Knowledge Graph) — para decisão de ... | 18 | 24 |
| [checks-v1.8-candidato.md](../../governance/propostas/SPEC-006/linha-spec006-plan/checks-v1.8-candidato.md) | checks.md — Verificação de Spec da SPEC-006 (fase spec-first) | 0 | 16 |
| [parecer-revisor-rodada5.md](../../governance/propostas/SPEC-006/linha-spec006-plan/parecer-revisor-rodada5.md) | Parecer do Revisor SOT — SPEC-006 Plan v1.4 (rodada 5) — 2026-10-17 | 4 | 6 |
| [parecer-revisor-rodada6.md](../../governance/propostas/SPEC-006/linha-spec006-plan/parecer-revisor-rodada6.md) | Parecer do Revisor SOT — SPEC-006 Plan v1.5 (rodada 6) — 2026-10-17 | 3 | 7 |
| [parecer-revisor-rodada7.md](../../governance/propostas/SPEC-006/linha-spec006-plan/parecer-revisor-rodada7.md) | Parecer do Revisor SOT — SPEC-006 Plan v1.6 (rodada 7) — 2026-10-17 | 2 | 8 |
| [parecer-revisor-rodada8.md](../../governance/propostas/SPEC-006/linha-spec006-plan/parecer-revisor-rodada8.md) | Parecer do Revisor — rodada 8 — SPEC-006 plan v1.7 (núcleo, Opção 2) — 2026-1... | 16 | 5 |
| [parecer-revisor-rodada9.md](../../governance/propostas/SPEC-006/linha-spec006-plan/parecer-revisor-rodada9.md) | Parecer do Revisor — rodada 9 — SPEC-006 plan v1.8 — 2026-10-18 | 12 | 4 |
| [plan-v1.8-candidato.md](../../governance/propostas/SPEC-006/linha-spec006-plan/plan-v1.8-candidato.md) | SPEC-006 — Cognitive Knowledge Graph | 0 | 28 |
| [PARECER-REVISOR-SPEC007-ABERTURA-2026-10-19.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-ABERTURA-2026-10-19.md) | PARECER DO REVISOR SOT — ABERTURA da SPEC-007 (revisão integral, 1ª rodada) —... | 4 | 15 |
| [PARECER-REVISOR-SPEC007-ABERTURA-R2-2026-10-19.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-ABERTURA-R2-2026-10-19.md) | PARECER DO REVISOR SOT — ABERTURA da SPEC-007, 2ª rodada (por delta, S2/Sonne... | 2 | 11 |
| [PARECER-REVISOR-SPEC007-ABERTURA-R3-2026-10-19.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-ABERTURA-R3-2026-10-19.md) | PARECER DO REVISOR SOT — ABERTURA da SPEC-007, 3ª rodada (por delta, S2/Sonne... | 3 | 14 |
| [PARECER-REVISOR-SPEC007-PLAN-R1-2026-10-23.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R1-2026-10-23.md) | Parecer do Revisor — Plan da SPEC-007 v1.0 (CANDIDATA), rodada 1 (integral, S... | 2 | 13 |
| [PARECER-REVISOR-SPEC007-PLAN-R2-2026-10-23.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R2-2026-10-23.md) | Parecer do Revisor — Plan da SPEC-007 v1.1 (CANDIDATA), rodada 2 (S2, revisão... | 1 | 7 |
| [PARECER-REVISOR-SPEC007-PLAN-R3-2026-10-24.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R3-2026-10-24.md) | Parecer do Revisor — Plan da SPEC-007 v1.2 (CANDIDATA), rodada 3 — 2026-10-24 | 3 | 7 |
| [PARECER-REVISOR-SPEC007-PLAN-R4-2026-10-24.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R4-2026-10-24.md) | Parecer do Revisor — Plan reduzido da SPEC-007 v2.0 (CANDIDATA), rodada 4 (S3... | 4 | 7 |
| [PARECER-REVISOR-SPEC007-PLAN-R5-2026-10-24.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R5-2026-10-24.md) | Parecer do Revisor — Plan reduzido da SPEC-007 v2.1 (CANDIDATA), rodada 5 (S2... | 3 | 8 |
| [PARECER-REVISOR-SPEC007-PLAN-R6-2026-10-24.md](../../governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R6-2026-10-24.md) | Parecer do Revisor — Plan reduzido da SPEC-007 v2.2 (CANDIDATA), rodada 6 (S2... | 3 | 8 |
| [PARECER-REVISOR-ERRATUM-SPEC020-002-R1-2026-10-30.md](../../governance/propostas/SPEC-020/PARECER-REVISOR-ERRATUM-SPEC020-002-R1-2026-10-30.md) | Parecer do Revisor — ERRATUM-SPEC020-002 v1.0 (metade F1 da dimensão B) — R1 ... | 3 | 7 |
| [PARECER-REVISOR-ERRATUM-SPEC020-002-R2-2026-10-30.md](../../governance/propostas/SPEC-020/PARECER-REVISOR-ERRATUM-SPEC020-002-R2-2026-10-30.md) | Parecer do Revisor — ERRATUM-SPEC020-002 v1.1 — R2 integral (S3, opus) — 2026... | 2 | 7 |
| [PARECER-REVISOR-ERRATUM-SPEC020-002-R3-2026-10-30.md](../../governance/propostas/SPEC-020/PARECER-REVISOR-ERRATUM-SPEC020-002-R3-2026-10-30.md) | Parecer do Revisor — ERRATUM-SPEC020-002 v1.2 — R3 (S3, opus) — 2026-10-30 | 1 | 5 |
| [PARECER-REVISOR-SPEC048-ABERTURA-R1-2026-10-24.md](../../governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-ABERTURA-R1-2026-10-24.md) | Parecer do Revisor — Proposta de abertura da SPEC-048 + Dossiê, rodada 1 (S3,... | 4 | 13 |
| [PARECER-REVISOR-SPEC048-ABERTURA-R2-2026-10-24.md](../../governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-ABERTURA-R2-2026-10-24.md) | Parecer do Revisor — Abertura da SPEC-048 (Revisão 3 do Especificador), rodad... | 2 | 7 |
| [PARECER-REVISOR-SPEC048-PLAN-R1-2026-10-24.md](../../governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R1-2026-10-24.md) | Parecer do Revisor — Plan da SPEC-048 v1.0 (CANDIDATO), rodada 1 (S3, integra... | 3 | 13 |
| [PARECER-REVISOR-SPEC048-PLAN-R2-2026-10-24.md](../../governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R2-2026-10-24.md) | Parecer do Revisor — Plan da SPEC-048 v1.1 (CANDIDATO), rodada 2 (S2, por del... | 3 | 7 |
| [PARECER-REVISOR-SPEC048-PLAN-R3-2026-10-24.md](../../governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R3-2026-10-24.md) | Parecer do Revisor — Plan da SPEC-048 v1.2 (CANDIDATO), rodada 3 (S2, por del... | 3 | 9 |
| [PARECER-REVISOR-SPEC048-PLAN-R4-2026-10-25.md](../../governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R4-2026-10-25.md) | Parecer do Revisor — Plan da SPEC-048 v1.3 (CANDIDATO), rodada 4 (S2, por del... | 15 | 4 |
| [PARECER-REVISOR-SPEC048-PLAN-R5-2026-10-25.md](../../governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R5-2026-10-25.md) | Parecer do Revisor — Plan da SPEC-048 v1.4, rodada 5 (delta, S2) — 2026-10-25 | 2 | 7 |
| [PARECER-REVISOR-SPEC049-ABERTURA-R1-2026-10-31.md](../../governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-ABERTURA-R1-2026-10-31.md) | Parecer do Revisor — Proposta de Abertura da SPEC-049 (WikiRAG Reading View) ... | 3 | 9 |
| [PARECER-REVISOR-SPEC049-ABERTURA-R2-2026-10-31.md](../../governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-ABERTURA-R2-2026-10-31.md) | Parecer do Revisor — Proposta de Abertura da SPEC-049 (WikiRAG Reading View) ... | 2 | 10 |
| [PARECER-REVISOR-SPEC049-ABERTURA-R3-2026-10-31.md](../../governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-ABERTURA-R3-2026-10-31.md) | Parecer do Revisor — Proposta de Abertura da SPEC-049 (WikiRAG Reading View) ... | 1 | 9 |
| [PARECER-REVISOR-SPEC049-PLAN-R1-2026-10-31.md](../../governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-PLAN-R1-2026-10-31.md) | Parecer do Revisor — Plan v1.0 da SPEC-049 (WikiRAG Reading View) — R1 integr... | 1 | 13 |
| [PARECER-REVISOR-SPEC049-PLAN-R2-2026-10-31.md](../../governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-PLAN-R2-2026-10-31.md) | Parecer do Revisor — Plan v1.1 da SPEC-049 (WikiRAG Reading View) — R2 por de... | 1 | 15 |
| [PARECER-REVISOR-SPEC049-PLAN-R3-2026-10-31.md](../../governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-PLAN-R3-2026-10-31.md) | Parecer do Revisor — Plan v1.2 da SPEC-049 (WikiRAG Reading View) — R3 por de... | 1 | 11 |
| [ROTEIRO-RETROSPECTIVA-SPEC049-RASCUNHO-2026-10-31.md](../../governance/propostas/SPEC-049/ROTEIRO-RETROSPECTIVA-SPEC049-RASCUNHO-2026-10-31.md) | Roteiro (RASCUNHO) — retrospectiva de fechamento da SPEC-049 | 4 | 6 |
| [PESQUISA-TELEMETRIA-CUSTO-TOKENS-2026-10-31.md](../../governance/propostas/TELEMETRIA-CUSTO/PESQUISA-TELEMETRIA-CUSTO-TOKENS-2026-10-31.md) | Pesquisa — telemetria de custo em tokens de sistemas agênticos (insumo para B... | 17 | 5 |

### canon

| Documento | Título | ← | → |
|---|---|---:|---:|
| [CCM-001-canonical-conviction-model.md](../../canon/CCM-001-canonical-conviction-model.md) | CCM-001 — Canonical Conviction Model Specification | 114 | 6 |
| [CEE-001-cognitive-economy-efficiency-v2.0.md](../../canon/CEE-001-cognitive-economy-efficiency-v2.0.md) | CEE-001 — Cognitive Economy & Efficiency Specification | 104 | 4 |
| [CEM-001-canonical-evidence-model.md](../../canon/CEM-001-canonical-evidence-model.md) | CEM-001 — Canonical Evidence Model Specification | 165 | 2 |
| [CHM-001-canonical-hypothesis-model.md](../../canon/CHM-001-canonical-hypothesis-model.md) | CHM-001 — Canonical Hypothesis Model (consolidado) | 103 | 0 |
| [CR-001-compliance-record.md](../../canon/CR-001-compliance-record.md) | CR-001 — Compliance Record Specification (consolidado, Cap.6-8) | 7 | 0 |
| [GMC-001-governance-canonical-models.md](../../canon/GMC-001-governance-canonical-models.md) | GMC-001 — Canonical Models Governance Specification | 51 | 0 |
| [PPQ-001-project-process-quality.md](../../canon/PPQ-001-project-process-quality.md) | PPQ-001 — Especificação de Gestão de Projetos, Processos e Qualidade | 23 | 3 |
| [SAS-001-structural-agent-spec.md](../../canon/SAS-001-structural-agent-spec.md) | SAS-001 — Structural Agent Specification (consolidado) | 82 | 3 |
| [SDD-001-spec-driven-development.md](../../canon/SDD-001-spec-driven-development.md) | SDD-001 — Protocolo de Spec-Driven Development do ORYX AGENT | 11 | 0 |

### specs

| Documento | Título | ← | → |
|---|---|---:|---:|
| [elliott-wave.spec.md](../../specs/elliott-wave.spec.md) | Spec — Elliott Wave Specialist | 3 | 1 |
| [SPEC-001/checks.md](../../specs/features/SPEC-001/checks.md) | SPEC-001 — Hypothesis Harness — Verificação de Spec | 74 | 2 |
| [SPEC-001/plan.md](../../specs/features/SPEC-001/plan.md) | SPEC-001 — Hypothesis Harness | 251 | 9 |
| [DOSSIE-PESQUISA.md](../../specs/features/SPEC-002/DOSSIE-PESQUISA.md) | Dossiê de Pesquisa — SPEC-002 (Evidence & Evidence Provenance Harness) | 2 | 14 |
| [PROPOSTA-ABERTURA.md](../../specs/features/SPEC-002/PROPOSTA-ABERTURA.md) | Proposta de Abertura — SPEC-002: Evidence & Evidence Provenance Harness | 5 | 16 |
| [SPEC-002/checks.md](../../specs/features/SPEC-002/checks.md) | checks.md — Verificação de Spec da SPEC-002 (fase spec-first) | 3 | 10 |
| [SPEC-002/plan.md](../../specs/features/SPEC-002/plan.md) | SPEC-002 — Evidence & Evidence Provenance Harness | 182 | 22 |
| [research.md](../../specs/features/SPEC-002/research.md) | SPEC-002 — Evidence & Evidence Provenance Harness — DOSSIÊ DE PESQUISA (ABERT... | 48 | 21 |
| [SPEC-003/checks.md](../../specs/features/SPEC-003/checks.md) | checks.md — Verificação de Spec da SPEC-003 (fase spec-first) | 3 | 18 |
| [SPEC-003/plan.md](../../specs/features/SPEC-003/plan.md) | SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine | 157 | 29 |
| [research-Q-A9-regime.md](../../specs/features/SPEC-003/research-Q-A9-regime.md) | SPEC-003 — Q-A9: Dimensão do Regime de Mercado (WF-C04) — DOSSIÊ DE PESQUISA | 7 | 4 |
| [research.md](../../specs/features/SPEC-003/research.md) | SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine — DO... | 3 | 23 |
| [ABERTURA.md](../../specs/features/SPEC-004/ABERTURA.md) | Proposta de Abertura — SPEC-004: Cognitive Blackboard Protocol | 41 | 17 |
| [SPEC-004/checks.md](../../specs/features/SPEC-004/checks.md) | checks.md — Verificação de Spec da SPEC-004 (fase spec-first) | 2 | 12 |
| [SPEC-004/plan.md](../../specs/features/SPEC-004/plan.md) | SPEC-004 — Cognitive Blackboard Protocol | 107 | 22 |
| [research.md](../../specs/features/SPEC-004/research.md) | Dossiê de Pesquisa — SPEC-004: Cognitive Blackboard Protocol | 2 | 16 |
| [ABERTURA.md](../../specs/features/SPEC-005/ABERTURA.md) | Proposta de Abertura — SPEC-005: Cognitive Event Bus (slot ROADMAP §5, FASE 2) | 4 | 19 |
| [SPEC-005/checks.md](../../specs/features/SPEC-005/checks.md) | checks.md — Verificação de Spec da SPEC-005 (fase spec-first) | 2 | 10 |
| [SPEC-005/plan.md](../../specs/features/SPEC-005/plan.md) | SPEC-005 — Cognitive Event Bus | 109 | 24 |
| [research.md](../../specs/features/SPEC-005/research.md) | Dossiê de Pesquisa — SPEC-005: Cognitive Event Bus (slot ROADMAP §5, FASE 2) | 2 | 23 |
| [ABERTURA.md](../../specs/features/SPEC-006/ABERTURA.md) | Proposta de Abertura — SPEC-006: Cognitive Knowledge Graph (slot ROADMAP §6, ... | 5 | 19 |
| [SPEC-006/checks.md](../../specs/features/SPEC-006/checks.md) | checks.md — Verificação de Spec da SPEC-006 (fase spec-first) | 7 | 16 |
| [errata-v1.13.md](../../specs/features/SPEC-006/errata-v1.13.md) | SPEC-006 — Errata v1.13 (ADITIVA) — ligação com o selo da SPEC-007 (E-1..E-4)... | 47 | 18 |
| [SPEC-006/plan.md](../../specs/features/SPEC-006/plan.md) | SPEC-006 — Cognitive Knowledge Graph | 319 | 39 |
| [research.md](../../specs/features/SPEC-006/research.md) | Dossiê de Pesquisa — SPEC-006: Cognitive Knowledge Graph (slot ROADMAP §6, FA... | 6 | 24 |
| [ABERTURA.md](../../specs/features/SPEC-007/ABERTURA.md) | Proposta de Abertura — SPEC-007: RAG / WikiRAG / Knowledge Formation Harness ... | 11 | 26 |
| [SPEC-007/checks.md](../../specs/features/SPEC-007/checks.md) | checks.md — Verificação de Spec da SPEC-007 (fase spec-first) | 2 | 15 |
| [SPEC-007/plan.md](../../specs/features/SPEC-007/plan.md) | SPEC-007 — RAG / WikiRAG / Knowledge Formation Harness — Plan REDUZIDO (forma... | 259 | 41 |
| [research.md](../../specs/features/SPEC-007/research.md) | Dossiê de Pesquisa — SPEC-007: RAG / WikiRAG / Knowledge Formation Harness (s... | 4 | 28 |
| [SPEC-019/checks.md](../../specs/features/SPEC-019/checks.md) | checks.md — Verificação de Spec da SPEC-019 (fase spec-first) | 1 | 8 |
| [SPEC-019/plan.md](../../specs/features/SPEC-019/plan.md) | SPEC-019 — Harness Governance & Evolution (+ Contrato de Herança Vertical) | 67 | 19 |
| [SPEC-020/checks.md](../../specs/features/SPEC-020/checks.md) | checks.md — Verificação de Spec da SPEC-020 (fase spec-first) | 4 | 8 |
| [SPEC-020/plan.md](../../specs/features/SPEC-020/plan.md) | SPEC-020 — Harness Evaluation Specification (núcleo A) | 216 | 24 |
| [research.md](../../specs/features/SPEC-020/research.md) | SPEC-020 — Harness Evaluation Specification (núcleo A) — DOSSIÊ DE PESQUISA (... | 2 | 16 |
| [SPEC-021/checks.md](../../specs/features/SPEC-021/checks.md) | checks.md — Verificação de Spec da SPEC-021 (fase spec-first) | 1 | 10 |
| [SPEC-021/plan.md](../../specs/features/SPEC-021/plan.md) | SPEC-021 — Harness Score / Maturity Model | 58 | 21 |
| [research.md](../../specs/features/SPEC-021/research.md) | SPEC-021 — Harness Score / Maturity Model — DOSSIÊ DE PESQUISA (ABERTURA) | 1 | 19 |
| [ABERTURA.md](../../specs/features/SPEC-038/ABERTURA.md) | Proposta de Abertura — SPEC-038: Trading Analysis Tool Harness | 6 | 18 |
| [SPEC-038/checks.md](../../specs/features/SPEC-038/checks.md) | SPEC-038 — Trading Analysis Tool Harness (Checks — verificação de spec) | 1 | 8 |
| [SPEC-038/plan.md](../../specs/features/SPEC-038/plan.md) | SPEC-038 — Trading Analysis Tool Harness (Plan) | 38 | 25 |
| [research.md](../../specs/features/SPEC-038/research.md) | Dossiê de Pesquisa — SPEC-038: Trading Analysis Tool Harness | 4 | 20 |
| [DOSSIE-PESQUISA.md](../../specs/features/SPEC-046/DOSSIE-PESQUISA.md) | Dossiê de Pesquisa — SPEC-046 (Grupo B: Caching de Spec-Time — Especificador/... | 3 | 9 |
| [PROPOSTA-ABERTURA.md](../../specs/features/SPEC-046/PROPOSTA-ABERTURA.md) | Proposta de Abertura — SPEC-046: Spec-Time Context Caching Harness (Grupo B —... | 4 | 21 |
| [SPEC-046/checks.md](../../specs/features/SPEC-046/checks.md) | checks.md — Verificação de Spec da SPEC-046 (fase spec-first) | 1 | 9 |
| [SPEC-046/plan.md](../../specs/features/SPEC-046/plan.md) | SPEC-046 — Spec-Time Context Caching Harness (Especificador/Revisor) | 31 | 23 |
| [research.md](../../specs/features/SPEC-046/research.md) | Dossiê de Pesquisa — SPEC-046 (companion — convenção de nome do gate determin... | 0 | 5 |
| [ABERTURA.md](../../specs/features/SPEC-048/ABERTURA.md) | Proposta de Abertura — SPEC-048: RAG Retrieval & Evidence Packet Harness (slo... | 5 | 25 |
| [SPEC-048/checks.md](../../specs/features/SPEC-048/checks.md) | checks.md — Verificação de Spec da SPEC-048 (fase spec-first) | 2 | 15 |
| [SPEC-048/plan.md](../../specs/features/SPEC-048/plan.md) | SPEC-048 — RAG Retrieval & Evidence Packet Harness — Plan v1.0 (recuperação +... | 165 | 42 |
| [research.md](../../specs/features/SPEC-048/research.md) | Dossiê de Pesquisa — SPEC-048: RAG Retrieval & Evidence Packet Harness (slot ... | 3 | 27 |
| [ABERTURA.md](../../specs/features/SPEC-049/ABERTURA.md) | Proposta de Abertura — SPEC-049: WikiRAG Reading View (slot ROADMAP §6, FASE 3) | 6 | 26 |
| [SPEC-049/checks.md](../../specs/features/SPEC-049/checks.md) | checks.md — Verificação de Spec da SPEC-049 (fase spec-first) | 4 | 10 |
| [SPEC-049/plan.md](../../specs/features/SPEC-049/plan.md) | SPEC-049 — WikiRAG Reading View — Plan v1.2 (visão de leitura por regra fixa,... | 142 | 29 |
| [research.md](../../specs/features/SPEC-049/research.md) | Dossiê de Pesquisa — SPEC-049: WikiRAG Reading View (slot ROADMAP §6, FASE 3) | 3 | 21 |
| [fibonacci.spec.md](../../specs/fibonacci.spec.md) | Spec — Fibonacci Validator | 3 | 1 |
| [ict.spec.md](../../specs/ict.spec.md) | Spec — ICT Specialist (Execution Intelligence) | 2 | 1 |
| [smc.spec.md](../../specs/smc.spec.md) | Spec — SMC Specialist (Institutional Intelligence) | 2 | 0 |
| [synthesis.spec.md](../../specs/synthesis.spec.md) | Spec — Synthesis Agent (Árbitro Final) | 7 | 2 |

### backlog

| Documento | Título | ← | → |
|---|---|---:|---:|
| [ANALISE-PRIORIZACAO-BACKLOG-2026-09-28.md](../../backlog/ANALISE-PRIORIZACAO-BACKLOG-2026-09-28.md) | ANÁLISE DE PRIORIZAÇÃO — Itens PENDENTES do Backlog (RMR-001) | 4 | 16 |
| [BL-016-MC-SKL-001-encaminhamento.md](../../backlog/BL-016-MC-SKL-001-encaminhamento.md) | BL-016 — Encaminhamento do MC-SKL-001 (Camada de Skills) após fechamento de I... | 14 | 14 |
| [BL-018-RISK-AGENT-backlog.md](../../backlog/BL-018-RISK-AGENT-backlog.md) | BL-018 — Risk Agent SOT (Família RISK-SPEC) | 21 | 17 |
| [BL-025-CACHE-ISS-001-analise.md](../../backlog/BL-025-CACHE-ISS-001-analise.md) | BL-025 — CACHE-ISS-001 — Análise Técnica Preparatória | 6 | 15 |
| [BL-034-OBSERVABILIDADE-LOGS-AGENTES-backlog.md](../../backlog/BL-034-OBSERVABILIDADE-LOGS-AGENTES-backlog.md) | BL-034 — Observabilidade e logs de agentes (master externo) — intake de backlog | 6 | 7 |
| [RMR-001_Painel_Backlog.md](../../backlog/RMR-001_Painel_Backlog.md) | RMR-001 — Painel Vivo de Backlog e Rastreabilidade de Ativação | 412 | 116 |

### reference

| Documento | Título | ← | → |
|---|---|---:|---:|
| [ANALISE-REVISAO-EXTERNA-SPEC003-2026-10-02.md](../../reference/ANALISE-REVISAO-EXTERNA-SPEC003-2026-10-02.md) | ANÁLISE CRÍTICA DA REVISÃO EXTERNA DA SPEC-003 (LLM externo) — 2026-10-02 | 3 | 11 |
| [PESQUISA-ENFORCEMENT-SCORE-INVALIDACAO-2026-10-02.md](../../reference/PESQUISA-ENFORCEMENT-SCORE-INVALIDACAO-2026-10-02.md) | PESQUISA — Enforcement / Score / Invalidação / Ponto de Interceptação de Polí... | 2 | 14 |
| [PESQUISA-WORKFLOW-TRADING-2026-10-01.md](../../reference/PESQUISA-WORKFLOW-TRADING-2026-10-01.md) | PESQUISA — Estado da Arte para Evolução do WORKFLOW Operacional do SOT | 7 | 8 |
| [RESPOSTAS-WORKFLOW-2026-10-01.md](../../reference/RESPOSTAS-WORKFLOW-2026-10-01.md) | RESPOSTAS DE ANDRAUS — evolução do WORKFLOW.md (2026-10-01) | 4 | 6 |
| [SOT-RISK-MASTER-001_Consolidado.md](../../reference/SOT-RISK-MASTER-001_Consolidado.md) | SOT-RISK-MASTER-001 — Master Document: Risk Agent SOT | 8 | 15 |
| [CAMADA APRENDIZADO.MD](../../reference/camadas/CAMADA%20APRENDIZADO.MD) | MC-LRN-001 — MASTER CONTRACT DA CAMADA DE LEARNING | 7 | 0 |
| [CAMADA CONFRACTUAL.MD](../../reference/camadas/CAMADA%20CONFRACTUAL.MD) | MASTER SPEC | 2 | 0 |
| [CAMADA DE CAUSALIDADE.MD](../../reference/camadas/CAMADA%20DE%20CAUSALIDADE.MD) | MASTER SPEC — CAMADA CAUSAL DO UNIVERSO COGNITIVO DO LLM | 2 | 0 |
| [CAMADA DE HARNESS.MD](../../reference/camadas/CAMADA%20DE%20HARNESS.MD) | HCH-001 | 3 | 0 |
| [CAMADA DECISIONAL.MD](../../reference/camadas/CAMADA%20DECISIONAL.MD) | MASTER SPEC | 2 | 0 |
| [CAMADA EPISTÊMICA.MD](../../reference/camadas/CAMADA%20EPIST%C3%8AMICA.MD) | MEG-001 | 4 | 0 |
| [CAMADA GOVERNANÇA CONHECIMENTO.MD](../../reference/camadas/CAMADA%20GOVERNAN%C3%87A%20CONHECIMENTO.MD) | MC-GOV-001 — MASTER CONTRACT DA CAMADA DE GOVERNANÇA | 3 | 0 |
| [CAMADA INCERTEZA.MD](../../reference/camadas/CAMADA%20INCERTEZA.MD) | MASTER SPEC | 2 | 0 |
| [CAMADA INQUÉRITO.MD](../../reference/camadas/CAMADA%20INQU%C3%89RITO.MD) | MIQG-001 | 2 | 0 |
| [CAMADA MEMÓRIA.MD](../../reference/camadas/CAMADA%20MEM%C3%93RIA.MD) | MC-EXP-001 — MASTER CONTRACT DA CAMADA DE EXPERIÊNCIA E MEMÓRIA | 9 | 0 |
| [CAMADA METACOGNIÇÃO.MD](../../reference/camadas/CAMADA%20METACOGNI%C3%87%C3%83O.MD) | MASTER DOCUMENTO | 3 | 0 |
| [CAMADA ONTOLÓGICA.MD](../../reference/camadas/CAMADA%20ONTOL%C3%93GICA.MD) | MASTER SPEC — CAMADA ONTOLÓGICA DO UNIVERSO COGNITIVO DO LLM | 2 | 0 |
| [CAMADA PRINCIPIOLÓGICA.MD](../../reference/camadas/CAMADA%20PRINCIPIOL%C3%93GICA.MD) | CMHP-001 | 5 | 0 |
| [CAMADA PROBABILISTICA.MD](../../reference/camadas/CAMADA%20PROBABILISTICA.MD) | MASTER SPEC | 2 | 0 |
| [CAMADA SEMÂNTICA.MD](../../reference/camadas/CAMADA%20SEM%C3%82NTICA.MD) | MASTER SPEC — CAMADA SEMÂNTICA DO UNIVERSO COGNITIVO DO LLM | 2 | 0 |
| [CAMADAS SKILLS.MD](../../reference/camadas/CAMADAS%20SKILLS.MD) | MC-SKL-001 | 6 | 0 |
| [MC-COG-001_Master_Contract_Camada_Cognicao.md](../../reference/camadas/MC-COG-001_Master_Contract_Camada_Cognicao.md) | MC-COG-001 — Master Contract da Camada de Cognição | 25 | 0 |
| [MC-RAG-001_Master_Contract_Camada_RAG.md](../../reference/camadas/MC-RAG-001_Master_Contract_Camada_RAG.md) | MC-RAG-001 — Master Contract da Camada RAG | 28 | 0 |
| [CACHING SOT.MD](../../reference/externo/CACHING%20SOT.MD) | CACHING SOT | 9 | 3 |
| [MASTER — MARKET DATA, ORDER FLOW E INTEGRAÇÃO TRADINGVIEW.MD](../../reference/externo/MASTER%20%E2%80%94%20MARKET%20DATA%2C%20ORDER%20FLOW%20E%20INTEGRA%C3%87%C3%83O%20TRADINGVIEW.MD) | MASTER — MARKET DATA, ORDER FLOW E INTEGRAÇÃO TRADINGVIEW | 0 | 2 |
| [TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md](../../reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md) | Tutorial técnico — Pine Script, backtest e calibração como suplemento do SOT | 6 | 14 |
| [TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md](../../reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md) | Tutorial técnico — Claude Code lendo e manipulando o TradingView (MCP + CDP) | 6 | 8 |
| [Uso de Logs por Agentes de IA.MD](../../reference/externo/Uso%20de%20Logs%20por%20Agentes%20de%20IA.MD) | MASTER DOCUMENT | 4 | 0 |

### rag

| Documento | Título | ← | → |
|---|---|---:|---:|
| [elliott-wave.knowledge.md](../../rag/elliott-wave.knowledge.md) | RAG — Elliott Wave Specialist Knowledge Base | 0 | 0 |
| [fibonacci.knowledge.md](../../rag/fibonacci.knowledge.md) | RAG — Fibonacci Validator Knowledge Base | 0 | 0 |
| [ict.knowledge.md](../../rag/ict.knowledge.md) | RAG — ICT Specialist Knowledge Base | 0 | 0 |
| [smc.knowledge.md](../../rag/smc.knowledge.md) | RAG — SMC Specialist Knowledge Base | 1 | 0 |
| [synthesis.knowledge.md](../../rag/synthesis.knowledge.md) | RAG — Synthesis Agent Knowledge Base | 3 | 2 |

### .claude

| Documento | Título | ← | → |
|---|---|---:|---:|
| [especificador.md](../../.claude/agents/especificador.md) | VOCÊ É O ESPECIFICADOR PRINCIPAL DO SOT | 107 | 60 |
| [revisor.md](../../.claude/agents/revisor.md) | Write, Edit e Bash são INTENCIONALMENTE AUSENTES. | 90 | 63 |
| [update-spec.md](../../.claude/commands/update-spec.md) | Update SOT Agent Spec | 0 | 0 |
| [validate-harness.md](../../.claude/commands/validate-harness.md) | Validate SOT Harness | 0 | 2 |
| [SKILL.md](../../.claude/skills/harness-eval/SKILL.md) | Harness Eval | 3 | 3 |
| [GLOSSARY.md](../../.claude/skills/harness-eval/references/GLOSSARY.md) | Harness Eval — plain-language glossary | 2 | 0 |
| [PROTOCOL.md](../../.claude/skills/harness-eval/references/PROTOCOL.md) | Harness Evaluation Protocol | 1 | 3 |
| [judge-prompts.md](../../.claude/skills/harness-eval/references/judge-prompts.md) | Judge spawn prompts | 1 | 0 |
| [SKILL.md](../../.claude/skills/sot-especificador-pap001/SKILL.md) | MISSÃO: PRODUZIR O PAP-001 | 0 | 10 |

### docs

| Documento | Título | ← | → |
|---|---|---:|---:|
| [MATRIZ-WORKFLOW-SPEC.md](../../docs/MATRIZ-WORKFLOW-SPEC.md) | MATRIZ `WF-xx → Spec dona` — WORKFLOW.md × Specs | 9 | 17 |
| [INDICE-AGENTES.md](../../docs/agentes/INDICE-AGENTES.md) | Índice de agentes — Construção × Trading | 52 | 6 |
| [AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md](../../docs/arranque/AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md) | AUDITORIA DO ESTADO ATUAL DOS AGENTES E HARNESS | 2 | 19 |
| [MANIFESTO-reorganizacao.md](../../docs/arranque/MANIFESTO-reorganizacao.md) | MANIFESTO DE REORGANIZAÇÃO — SOT-Harness | 2 | 16 |
| [PARECER-CAMADA-PRINCIPIOLOGICA-hierarquica.md](../../docs/arranque/PARECER-CAMADA-PRINCIPIOLOGICA-hierarquica.md) | PARECER — Camada hierárquica principiológica: necessidade de adiantamento com... | 2 | 6 |
| [PARECER-RISK-AGENT-auditoria-semantica.md](../../docs/arranque/PARECER-RISK-AGENT-auditoria-semantica.md) | PARECER — Auditoria Semântica e Normativa do Risk Agent × repo SOT | 3 | 10 |
| [ata-homologacao-F1.md](../../docs/arranque/ata-homologacao-F1.md) | ATA DE HOMOLOGAÇÃO — Baseline F.1 do Harness SOT | 1 | 11 |
| [auditoria-saude-harness.md](../../docs/arranque/auditoria-saude-harness.md) | AUDITORIA DE SAÚDE E CONFORMIDADE DO HARNESS — SOT | 1 | 12 |
| [parecer-revisor-F1.md](../../docs/arranque/parecer-revisor-F1.md) | PARECER DE INTEGRIDADE F.1 — Revisor SOT | 3 | 5 |
| [questionario-resolucao-v1.md](../../docs/arranque/questionario-resolucao-v1.md) | QUESTIONÁRIO DE RESOLUÇÃO — SOT Arranque | 3 | 14 |
| [respostas-questionario-v1.md](../../docs/arranque/respostas-questionario-v1.md) | RESPOSTAS AO QUESTIONÁRIO DE RESOLUÇÃO — SOT Arranque | 2 | 13 |
| [ARIA-plano-mestre.md](../../docs/fundamentos/ARIA-plano-mestre.md) | ARIA — Agente de Reconhecimento Institucional e Análise | 3 | 0 |
| [AUDITORIA-ideias-nao-implementadas.md](../../docs/fundamentos/AUDITORIA-ideias-nao-implementadas.md) | AUDITORIA DE IDEIAS NÃO IMPLEMENTADAS — Fonte de referência (texto extraído d... | 3 | 0 |
| [ENGENHARIA-GERAL.md](../../docs/fundamentos/ENGENHARIA-GERAL.md) | ENGENHARIA GERAL — Fonte de referência (texto extraído do PDF) | 3 | 0 |
| [KERNEL-V2.md](../../docs/fundamentos/KERNEL-V2.md) | KERNEL V2 — Fonte de referência (texto extraído do PDF) | 3 | 0 |
| [HO-2026-10-17-01.md](../../docs/handoffs/HO-2026-10-17-01.md) | HANDOFF — SOT | 3 | 14 |
| [HO-2026-10-17-02.md](../../docs/handoffs/HO-2026-10-17-02.md) | HANDOFF — SOT | 0 | 17 |
| [HO-2026-10-17-03.md](../../docs/handoffs/HO-2026-10-17-03.md) | HANDOFF — SOT | 0 | 18 |
| [HO-2026-10-17-04.md](../../docs/handoffs/HO-2026-10-17-04.md) | HANDOFF — SOT | 0 | 19 |
| [HO-2026-10-17-05.md](../../docs/handoffs/HO-2026-10-17-05.md) | HANDOFF — SOT | 0 | 13 |
| [HO-2026-10-17-06.md](../../docs/handoffs/HO-2026-10-17-06.md) | HANDOFF — SOT | 0 | 13 |
| [HO-2026-10-17-07.md](../../docs/handoffs/HO-2026-10-17-07.md) | HANDOFF — SOT | 0 | 14 |
| [HO-2026-10-17-08.md](../../docs/handoffs/HO-2026-10-17-08.md) | HANDOFF — SOT | 0 | 14 |
| [HO-2026-10-17-09.md](../../docs/handoffs/HO-2026-10-17-09.md) | HANDOFF — SOT | 0 | 15 |
| [HO-2026-10-17-10.md](../../docs/handoffs/HO-2026-10-17-10.md) | HANDOFF — SOT | 0 | 17 |
| [HO-2026-10-17-11.md](../../docs/handoffs/HO-2026-10-17-11.md) | HANDOFF — SOT | 0 | 24 |
| [HO-2026-10-17-12.md](../../docs/handoffs/HO-2026-10-17-12.md) | HANDOFF — SOT | 0 | 24 |
| [HO-2026-10-17-13.md](../../docs/handoffs/HO-2026-10-17-13.md) | HANDOFF — SOT | 0 | 16 |
| [HO-2026-10-17-14.md](../../docs/handoffs/HO-2026-10-17-14.md) | HANDOFF — SOT | 0 | 16 |
| [HO-2026-10-17-15.md](../../docs/handoffs/HO-2026-10-17-15.md) | HANDOFF — SOT | 0 | 17 |
| [HO-2026-10-17-16.md](../../docs/handoffs/HO-2026-10-17-16.md) | HANDOFF — SOT | 0 | 17 |
| [HO-2026-10-17-17.md](../../docs/handoffs/HO-2026-10-17-17.md) | HANDOFF — SOT | 0 | 17 |
| [HO-2026-10-17-18.md](../../docs/handoffs/HO-2026-10-17-18.md) | HANDOFF — SOT | 0 | 18 |
| [HO-2026-10-17-19.md](../../docs/handoffs/HO-2026-10-17-19.md) | HANDOFF — SOT | 0 | 19 |
| [HO-2026-10-17-20.md](../../docs/handoffs/HO-2026-10-17-20.md) | HANDOFF — SOT | 0 | 19 |
| [HO-2026-10-17-21.md](../../docs/handoffs/HO-2026-10-17-21.md) | HANDOFF — SOT | 0 | 20 |
| [HO-2026-10-17-22.md](../../docs/handoffs/HO-2026-10-17-22.md) | HANDOFF — SOT | 0 | 20 |
| [HO-2026-10-17-23.md](../../docs/handoffs/HO-2026-10-17-23.md) | HANDOFF — SOT | 0 | 22 |
| [HO-2026-10-17-24.md](../../docs/handoffs/HO-2026-10-17-24.md) | HANDOFF — SOT | 0 | 23 |
| [HO-2026-10-17-25.md](../../docs/handoffs/HO-2026-10-17-25.md) | HANDOFF — SOT | 0 | 24 |
| [HO-2026-10-17-26.md](../../docs/handoffs/HO-2026-10-17-26.md) | HANDOFF — SOT | 0 | 25 |
| [HO-2026-10-17-27.md](../../docs/handoffs/HO-2026-10-17-27.md) | HANDOFF — SOT | 0 | 27 |
| [HO-2026-10-17-28.md](../../docs/handoffs/HO-2026-10-17-28.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-17-29.md](../../docs/handoffs/HO-2026-10-17-29.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-17-30.md](../../docs/handoffs/HO-2026-10-17-30.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-17-31.md](../../docs/handoffs/HO-2026-10-17-31.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-17-32.md](../../docs/handoffs/HO-2026-10-17-32.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-17-33.md](../../docs/handoffs/HO-2026-10-17-33.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-17-34.md](../../docs/handoffs/HO-2026-10-17-34.md) | HANDOFF — SOT | 19 | 34 |
| [HO-2026-10-17-35.md](../../docs/handoffs/HO-2026-10-17-35.md) | HANDOFF — SOT | 0 | 31 |
| [HO-2026-10-17-36.md](../../docs/handoffs/HO-2026-10-17-36.md) | HANDOFF — SOT | 0 | 31 |
| [HO-2026-10-18-37.md](../../docs/handoffs/HO-2026-10-18-37.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-18-38.md](../../docs/handoffs/HO-2026-10-18-38.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-18-39.md](../../docs/handoffs/HO-2026-10-18-39.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-18-40.md](../../docs/handoffs/HO-2026-10-18-40.md) | HANDOFF — SOT | 0 | 34 |
| [HO-2026-10-18-41.md](../../docs/handoffs/HO-2026-10-18-41.md) | HANDOFF — SOT | 0 | 37 |
| [HO-2026-10-18-42.md](../../docs/handoffs/HO-2026-10-18-42.md) | HANDOFF — SOT | 0 | 37 |
| [HO-2026-10-18-43.md](../../docs/handoffs/HO-2026-10-18-43.md) | HANDOFF — SOT | 0 | 38 |
| [HO-2026-10-18-44.md](../../docs/handoffs/HO-2026-10-18-44.md) | HANDOFF — SOT | 0 | 37 |
| [HO-2026-10-18-45.md](../../docs/handoffs/HO-2026-10-18-45.md) | HANDOFF — SOT | 0 | 38 |
| [HO-2026-10-18-46.md](../../docs/handoffs/HO-2026-10-18-46.md) | HANDOFF — SOT | 0 | 38 |
| [HO-2026-10-18-47.md](../../docs/handoffs/HO-2026-10-18-47.md) | HANDOFF — SOT | 0 | 40 |
| [HO-2026-10-18-48.md](../../docs/handoffs/HO-2026-10-18-48.md) | HANDOFF — SOT | 0 | 41 |
| [HO-2026-10-18-49.md](../../docs/handoffs/HO-2026-10-18-49.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-10-18-50.md](../../docs/handoffs/HO-2026-10-18-50.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-10-18-51.md](../../docs/handoffs/HO-2026-10-18-51.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-18-52.md](../../docs/handoffs/HO-2026-10-18-52.md) | HANDOFF — SOT | 0 | 29 |
| [HO-2026-10-18-53.md](../../docs/handoffs/HO-2026-10-18-53.md) | HANDOFF — SOT | 0 | 30 |
| [HO-2026-10-18-54.md](../../docs/handoffs/HO-2026-10-18-54.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-18-55.md](../../docs/handoffs/HO-2026-10-18-55.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-18-56.md](../../docs/handoffs/HO-2026-10-18-56.md) | HANDOFF — SOT | 0 | 24 |
| [HO-2026-10-18-57.md](../../docs/handoffs/HO-2026-10-18-57.md) | HANDOFF — SOT | 0 | 24 |
| [HO-2026-10-18-58.md](../../docs/handoffs/HO-2026-10-18-58.md) | HANDOFF — SOT | 0 | 22 |
| [HO-2026-10-18-59.md](../../docs/handoffs/HO-2026-10-18-59.md) | HANDOFF — SOT | 0 | 23 |
| [HO-2026-10-18-60.md](../../docs/handoffs/HO-2026-10-18-60.md) | HANDOFF — SOT | 0 | 23 |
| [HO-2026-10-18-61.md](../../docs/handoffs/HO-2026-10-18-61.md) | HANDOFF — SOT | 0 | 23 |
| [HO-2026-10-18-62.md](../../docs/handoffs/HO-2026-10-18-62.md) | HANDOFF — SOT | 0 | 23 |
| [HO-2026-10-18-63.md](../../docs/handoffs/HO-2026-10-18-63.md) | HANDOFF — SOT | 0 | 23 |
| [HO-2026-10-18-64.md](../../docs/handoffs/HO-2026-10-18-64.md) | HANDOFF — SOT | 0 | 23 |
| [HO-2026-10-19-65.md](../../docs/handoffs/HO-2026-10-19-65.md) | HANDOFF — SOT | 0 | 19 |
| [HO-2026-10-19-66.md](../../docs/handoffs/HO-2026-10-19-66.md) | HANDOFF — SOT | 0 | 19 |
| [HO-2026-10-19-67.md](../../docs/handoffs/HO-2026-10-19-67.md) | HANDOFF — SOT | 0 | 19 |
| [HO-2026-10-19-68.md](../../docs/handoffs/HO-2026-10-19-68.md) | HANDOFF — SOT | 0 | 19 |
| [HO-2026-10-19-69.md](../../docs/handoffs/HO-2026-10-19-69.md) | HANDOFF — SOT | 1 | 20 |
| [HO-2026-10-24-70.md](../../docs/handoffs/HO-2026-10-24-70.md) | HANDOFF — SOT | 1 | 21 |
| [HO-2026-10-24-71.md](../../docs/handoffs/HO-2026-10-24-71.md) | HANDOFF — SOT | 1 | 22 |
| [HO-2026-10-24-72.md](../../docs/handoffs/HO-2026-10-24-72.md) | HANDOFF — SOT | 1 | 23 |
| [HO-2026-10-24-73.md](../../docs/handoffs/HO-2026-10-24-73.md) | HANDOFF — SOT | 1 | 24 |
| [HO-2026-10-24-74.md](../../docs/handoffs/HO-2026-10-24-74.md) | HANDOFF — SOT | 1 | 25 |
| [HO-2026-10-24-75.md](../../docs/handoffs/HO-2026-10-24-75.md) | HANDOFF — SOT | 1 | 28 |
| [HO-2026-10-24-76.md](../../docs/handoffs/HO-2026-10-24-76.md) | HANDOFF — SOT | 1 | 29 |
| [HO-2026-10-24-77.md](../../docs/handoffs/HO-2026-10-24-77.md) | HANDOFF — SOT | 1 | 30 |
| [HO-2026-10-24-78.md](../../docs/handoffs/HO-2026-10-24-78.md) | HANDOFF — SOT | 1 | 30 |
| [HO-2026-10-24-79.md](../../docs/handoffs/HO-2026-10-24-79.md) | HANDOFF — SOT | 1 | 33 |
| [HO-2026-10-24-80.md](../../docs/handoffs/HO-2026-10-24-80.md) | HANDOFF — SOT | 1 | 34 |
| [HO-2026-10-25-81.md](../../docs/handoffs/HO-2026-10-25-81.md) | HANDOFF — SOT | 11 | 37 |
| [HO-2026-10-25-82.md](../../docs/handoffs/HO-2026-10-25-82.md) | HANDOFF — SOT | 0 | 37 |
| [HO-2026-10-25-83.md](../../docs/handoffs/HO-2026-10-25-83.md) | HANDOFF — SOT | 0 | 38 |
| [HO-2026-10-25-84.md](../../docs/handoffs/HO-2026-10-25-84.md) | HANDOFF — SOT | 0 | 38 |
| [HO-2026-10-25-85.md](../../docs/handoffs/HO-2026-10-25-85.md) | HANDOFF — SOT | 0 | 39 |
| [HO-2026-10-25-86.md](../../docs/handoffs/HO-2026-10-25-86.md) | HANDOFF — SOT | 0 | 39 |
| [HO-2026-10-25-87.md](../../docs/handoffs/HO-2026-10-25-87.md) | HANDOFF — SOT | 0 | 39 |
| [HO-2026-10-30-88.md](../../docs/handoffs/HO-2026-10-30-88.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-10-30-89.md](../../docs/handoffs/HO-2026-10-30-89.md) | HANDOFF — SOT | 0 | 43 |
| [HO-2026-10-30-90.md](../../docs/handoffs/HO-2026-10-30-90.md) | HANDOFF — SOT | 0 | 44 |
| [HO-2026-10-30-91.md](../../docs/handoffs/HO-2026-10-30-91.md) | HANDOFF — SOT | 0 | 46 |
| [HO-2026-10-31-100.md](../../docs/handoffs/HO-2026-10-31-100.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-101.md](../../docs/handoffs/HO-2026-10-31-101.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-102.md](../../docs/handoffs/HO-2026-10-31-102.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-103.md](../../docs/handoffs/HO-2026-10-31-103.md) | HANDOFF — SOT | 0 | 29 |
| [HO-2026-10-31-104.md](../../docs/handoffs/HO-2026-10-31-104.md) | HANDOFF — SOT | 0 | 29 |
| [HO-2026-10-31-105.md](../../docs/handoffs/HO-2026-10-31-105.md) | HANDOFF — SOT | 0 | 29 |
| [HO-2026-10-31-106.md](../../docs/handoffs/HO-2026-10-31-106.md) | HANDOFF — SOT | 0 | 29 |
| [HO-2026-10-31-107.md](../../docs/handoffs/HO-2026-10-31-107.md) | HANDOFF — SOT | 0 | 29 |
| [HO-2026-10-31-108.md](../../docs/handoffs/HO-2026-10-31-108.md) | HANDOFF — SOT | 0 | 29 |
| [HO-2026-10-31-109.md](../../docs/handoffs/HO-2026-10-31-109.md) | HANDOFF — SOT | 13 | 30 |
| [HO-2026-10-31-110.md](../../docs/handoffs/HO-2026-10-31-110.md) | HANDOFF — SOT | 0 | 31 |
| [HO-2026-10-31-111.md](../../docs/handoffs/HO-2026-10-31-111.md) | HANDOFF — SOT | 0 | 32 |
| [HO-2026-10-31-112.md](../../docs/handoffs/HO-2026-10-31-112.md) | HANDOFF — SOT | 0 | 32 |
| [HO-2026-10-31-113.md](../../docs/handoffs/HO-2026-10-31-113.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-31-114.md](../../docs/handoffs/HO-2026-10-31-114.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-31-115.md](../../docs/handoffs/HO-2026-10-31-115.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-31-116.md](../../docs/handoffs/HO-2026-10-31-116.md) | HANDOFF — SOT | 0 | 36 |
| [HO-2026-10-31-120.md](../../docs/handoffs/HO-2026-10-31-120.md) | HANDOFF — SOT | 0 | 36 |
| [HO-2026-10-31-121.md](../../docs/handoffs/HO-2026-10-31-121.md) | HANDOFF — SOT | 0 | 36 |
| [HO-2026-10-31-122.md](../../docs/handoffs/HO-2026-10-31-122.md) | HANDOFF — SOT | 0 | 32 |
| [HO-2026-10-31-123.md](../../docs/handoffs/HO-2026-10-31-123.md) | HANDOFF — SOT | 0 | 36 |
| [HO-2026-10-31-124.md](../../docs/handoffs/HO-2026-10-31-124.md) | HANDOFF — SOT | 0 | 38 |
| [HO-2026-10-31-125.md](../../docs/handoffs/HO-2026-10-31-125.md) | HANDOFF — SOT | 0 | 39 |
| [HO-2026-10-31-126.md](../../docs/handoffs/HO-2026-10-31-126.md) | HANDOFF — SOT | 0 | 40 |
| [HO-2026-10-31-127.md](../../docs/handoffs/HO-2026-10-31-127.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-10-31-128.md](../../docs/handoffs/HO-2026-10-31-128.md) | HANDOFF — SOT | 25 | 45 |
| [HO-2026-10-31-129.md](../../docs/handoffs/HO-2026-10-31-129.md) | HANDOFF — SOT | 0 | 39 |
| [HO-2026-10-31-130.md](../../docs/handoffs/HO-2026-10-31-130.md) | HANDOFF — SOT | 0 | 38 |
| [HO-2026-10-31-131.md](../../docs/handoffs/HO-2026-10-31-131.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-10-31-132.md](../../docs/handoffs/HO-2026-10-31-132.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-10-31-133.md](../../docs/handoffs/HO-2026-10-31-133.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-10-31-92.md](../../docs/handoffs/HO-2026-10-31-92.md) | HANDOFF — SOT | 0 | 47 |
| [HO-2026-10-31-93.md](../../docs/handoffs/HO-2026-10-31-93.md) | HANDOFF — SOT | 0 | 24 |
| [HO-2026-10-31-94.md](../../docs/handoffs/HO-2026-10-31-94.md) | HANDOFF — SOT | 0 | 24 |
| [HO-2026-10-31-95.md](../../docs/handoffs/HO-2026-10-31-95.md) | HANDOFF — SOT | 0 | 25 |
| [HO-2026-10-31-96.md](../../docs/handoffs/HO-2026-10-31-96.md) | HANDOFF — SOT | 0 | 26 |
| [HO-2026-10-31-97.md](../../docs/handoffs/HO-2026-10-31-97.md) | HANDOFF — SOT | 0 | 26 |
| [HO-2026-10-31-98.md](../../docs/handoffs/HO-2026-10-31-98.md) | HANDOFF — SOT | 0 | 27 |
| [HO-2026-10-31-99.md](../../docs/handoffs/HO-2026-10-31-99.md) | HANDOFF — SOT | 0 | 27 |
| [HO-2026-11-01-132.md](../../docs/handoffs/HO-2026-11-01-132.md) | HANDOFF — SOT | 0 | 43 |
| [HO-2026-11-01-133.md](../../docs/handoffs/HO-2026-11-01-133.md) | HANDOFF — SOT | 0 | 43 |
| [HO-2026-11-01-134.md](../../docs/handoffs/HO-2026-11-01-134.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-11-01-135.md](../../docs/handoffs/HO-2026-11-01-135.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-11-01-136.md](../../docs/handoffs/HO-2026-11-01-136.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-11-01-137.md](../../docs/handoffs/HO-2026-11-01-137.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-11-01-138.md](../../docs/handoffs/HO-2026-11-01-138.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-11-01-139.md](../../docs/handoffs/HO-2026-11-01-139.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-11-01-140.md](../../docs/handoffs/HO-2026-11-01-140.md) | HANDOFF — SOT | 4 | 42 |
| [HO-2026-11-01-141.md](../../docs/handoffs/HO-2026-11-01-141.md) | HANDOFF — SOT | 0 | 46 |
| [HO-2026-11-01-146.md](../../docs/handoffs/HO-2026-11-01-146.md) | HANDOFF — SOT | 0 | 48 |
| [HO-2026-11-01-147.md](../../docs/handoffs/HO-2026-11-01-147.md) | HANDOFF — SOT | 0 | 48 |
| [AT-SPEC007-PLAN-2026-10-19.md](../../docs/handoffs/anexos/AT-SPEC007-PLAN-2026-10-19.md) | Anexo de tarefa — Plan da SPEC-007 | 0 | 15 |
| [LEIA-ME.md](../../docs/handoffs/anexos/LEIA-ME.md) | Anexos de tarefa CONSUMIDOS (arquivo — INV-07) | 0 | 3 |
| [HO-2026-10-31-110.md](../../docs/handoffs/ramo-ccr-3a6df80c-nej9ne/HO-2026-10-31-110.md) | HANDOFF — SOT | 0 | 32 |
| [HO-2026-10-31-111.md](../../docs/handoffs/ramo-ccr-3a6df80c-nej9ne/HO-2026-10-31-111.md) | HANDOFF — SOT | 0 | 32 |
| [HO-2026-10-31-112.md](../../docs/handoffs/ramo-ccr-3a6df80c-nej9ne/HO-2026-10-31-112.md) | HANDOFF — SOT | 0 | 32 |
| [HO-2026-10-31-116.md](../../docs/handoffs/ramo-ccr-3a6df80c-nej9ne/HO-2026-10-31-116.md) | HANDOFF — SOT | 0 | 36 |
| [HO-2026-10-31-117.md](../../docs/handoffs/ramo-ccr-3a6df80c-nej9ne/HO-2026-10-31-117.md) | HANDOFF — SOT | 0 | 36 |
| [HO-2026-11-01-134.md](../../docs/handoffs/ramo-ccr-4bd4e8a0-d92lc7/HO-2026-11-01-134.md) | HANDOFF — SOT | 0 | 44 |
| [HO-2026-11-01-135.md](../../docs/handoffs/ramo-ccr-4bd4e8a0-d92lc7/HO-2026-11-01-135.md) | HANDOFF — SOT | 0 | 44 |
| [HO-2026-11-01-136.md](../../docs/handoffs/ramo-ccr-4bd4e8a0-d92lc7/HO-2026-11-01-136.md) | HANDOFF — SOT | 0 | 45 |
| [HO-2026-10-31-110.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-110.md) | HANDOFF — SOT | 0 | 27 |
| [HO-2026-10-31-111.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-111.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-112.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-112.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-113.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-113.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-114.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-114.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-115.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-115.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-116.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-116.md) | HANDOFF — SOT | 0 | 28 |
| [HO-2026-10-31-117.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-117.md) | HANDOFF — SOT | 0 | 29 |
| [HO-2026-10-31-118.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-118.md) | HANDOFF — SOT | 0 | 30 |
| [HO-2026-10-31-119.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-119.md) | HANDOFF — SOT | 0 | 30 |
| [HO-2026-10-31-120.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-120.md) | HANDOFF — SOT | 0 | 30 |
| [HO-2026-10-31-121.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-121.md) | HANDOFF — SOT | 0 | 30 |
| [HO-2026-10-31-122.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-122.md) | HANDOFF — SOT | 0 | 31 |
| [HO-2026-10-31-127.md](../../docs/handoffs/ramo-ccr-599f6762-60qbvg/HO-2026-10-31-127.md) | HANDOFF — SOT | 0 | 43 |
| [HO-2026-10-31-116.md](../../docs/handoffs/ramo-ccr-6119d28b-a50xaw/HO-2026-10-31-116.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-31-117.md](../../docs/handoffs/ramo-ccr-6119d28b-a50xaw/HO-2026-10-31-117.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-31-118.md](../../docs/handoffs/ramo-ccr-6119d28b-a50xaw/HO-2026-10-31-118.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-10-31-119.md](../../docs/handoffs/ramo-ccr-6119d28b-a50xaw/HO-2026-10-31-119.md) | HANDOFF — SOT | 0 | 33 |
| [HO-2026-11-01-141.md](../../docs/handoffs/ramo-ccr-d7f01e4e-c5qpb1/HO-2026-11-01-141.md) | HANDOFF — SOT | 0 | 42 |
| [HO-2026-11-01-142.md](../../docs/handoffs/ramo-ccr-d7f01e4e-c5qpb1/HO-2026-11-01-142.md) | HANDOFF — SOT | 0 | 43 |
| [HO-2026-11-01-143.md](../../docs/handoffs/ramo-ccr-d7f01e4e-c5qpb1/HO-2026-11-01-143.md) | HANDOFF — SOT | 0 | 43 |
| [HO-2026-11-01-144.md](../../docs/handoffs/ramo-ccr-d7f01e4e-c5qpb1/HO-2026-11-01-144.md) | HANDOFF — SOT | 0 | 44 |

### RETOMADA

| Documento | Título | ← | → |
|---|---|---:|---:|
| [GEH-001_Guia_Agente_Especificacoes_Harness.md](../../RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md) | GEH-001 — Guia do Agente Especialista em Especificações e Harness | 41 | 1 |

### .clinerules

| Documento | Título | ← | → |
|---|---|---:|---:|
| [sot-map.md](../../.clinerules/sot-map.md) | Mapa do projeto (BL-019) | 1 | 3 |
| [sot-rag.md](../../.clinerules/sot-rag.md) | SOT RAG Knowledge Base Rules | 2 | 0 |
| [sot-schemas.md](../../.clinerules/sot-schemas.md) | SOT Schema Editing Rules | 2 | 0 |
| [sot-specs.md](../../.clinerules/sot-specs.md) | SOT Spec Editing Rules | 1 | 0 |
