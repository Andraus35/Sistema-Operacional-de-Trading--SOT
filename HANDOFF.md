---
handoff_id: HO-2026-10-17-07
previous: HO-2026-10-17-06
data: 2026-10-17
branch: ccr-d43bf9b0-h336k5
base_commit: 1c6754b
spec_autorizada: SPEC-006 (abertura homologada, DHR-SPEC006-001; Plan pendente — só por ordem de Andraus) — ROADMAP prevalece
fase: spec-first
autor: Orquestrador
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Objetivo da frente atual
Eficiência do 4Es na camada meta: roteamento de modelo **por tarefa** (hoje só por papel). Pedido de Andraus (chat, 2026-10-17): auditar tarefas por criticidade, pesquisar estado da arte/benchmarks e propor aplicação do 4Es. A frente anterior (reforço do Revisor, DHR-AUDITOR-EXTERNO-015) segue como estava no HO-06 (`docs/handoffs/HO-2026-10-17-06.md`).

## 2. Estado
Fase spec-first; BUILD/VERIFY-de-código adiados. Última Spec homologada: SPEC-005; SPEC-006 com abertura homologada e Plan não iniciado. PCC-001 Fases 1 e 2 em vigor (D-PCC-3/4/5 em aberto).

## 3. Feito nesta sessão
- **Entregue (PROPOSTA, não normativa):** `governance/propostas/ROTEAMENTO-MODELOS/AUDITORIA-ROTEAMENTO-MODELOS_PROPOSTA.md` — auditoria interna (12 achados A-01..A-12), matriz de ~30 tarefas por criticidade N0–N4, 14 fontes externas classificadas, preços, Matriz de Roteamento Meta (R1–R12), protocolo de teste Eficácia-first, cenário ilustrativo e decisões D1–D6. Nenhum arquivo normativo alterado.
- Achados-chave: (1) premissa de plataforma da EUA-E19 §1 caducou — `effort`, `model` por invocação existem hoje; o "esforço médio/alto" dos agentes não é aplicado; (2) Opus 5.5 custa 20% menos que o Opus 4.8 do Especificador (não testado); (3) `sot-spec-reviewer` e `sot-schema-validator` sem `model:` herdam o mais caro; (4) sem telemetria de custo por tarefa; (5) Orquestrador pode rodar o gate D antes de gastar uma revisão LLM.

## 4. Verificado
- `build_map --check` em dia; `check_doc_sync` ERRO=0; `check_invariants` no arquivo novo: 0 achados.
- `check_refs`: 1 ERRO **preexistente** (`governance/CATALOGO-OFICIAL.md:198` — DHR-010 sem definição); não é desta entrega.
- Não conferido: CI da `main`, PRs abertos, telemetria real (não existe), disponibilidade do advisor tool em Claude Code, billing (API × cota).

## 5. Próximo passo único
Perguntar a Andraus D1–D6 (§11.2 do documento): em especial autorizar a **onda 0** (pré-gate + `model`/`effort` por invocação só em N1 não-crítico + telemetria manual) e informar se o custo é por API ou por cota. Sem outra ordem, **não** iniciar o Plan da SPEC-006 nem editar `.claude/agents/*.md`.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
- Nenhuma nova. EUA-E24 é só **código candidato**. Decisões abertas/fechadas: ler `ROADMAP.md`. Nenhuma alterada.

## 7. Becos sem saída
- Rebaixar o Revisor por custo: rejeitado pela medição (DHR-AUDITOR-EXTERNO-014: 0/18 vs 14–16/18).
- Roteador aprendido: não recomendado (LLMRouterBench; "Routing Gap Is Task Type"). Haiku como gate: vedado (ENF-03).
- Dar Bash ao Revisor: rejeitado (DHR-AUDITOR-EXTERNO-009 §2).

## 8. Não tocar
- `canon/` BASELINED, specs homologadas, `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*.md`, `AGENTS.md` (só por Andraus). Não regravar `GATE-MANIFEST.sha256` sem decisão de Andraus.

## 9. Reverificar ao vivo
- [ ] CI da `main` e do ramo
- [ ] `python scripts/gate_manifest.py --check`, `check_refs.py`, `check_doc_sync.py`
- [ ] PRs abertos (#31 Auditor externo, #2 capturas SPEC-003 na última checagem)
- [ ] `python scripts/backlog_triggers.py`
- [ ] Versão vigente de `WORKFLOW.md` (2.1 nesta sessão)
- [ ] Preços/modelos (página oficial) antes de qualquer decisão de roteamento
- [ ] `git log -1` == `base_commit` ou posterior; se posterior, ler o diff

## 10. Aguardando Andraus
- D1–D6 do documento de roteamento (acima).
- Herdado do HO-06: merge da DHR-AUDITOR-EXTERNO-015; diagnosticar por que o MCP do Revisor não carrega em nuvem (afeta a economia: sem gate D o LLM caça defeitos detectáveis por código); D-PCC-3/4/5; prioridade da SPEC-006; 2 itens de backlog disparados sem registro.

## 11. Ponteiros
`governance/propostas/ROTEAMENTO-MODELOS/AUDITORIA-ROTEAMENTO-MODELOS_PROPOSTA.md` · `canon/CEE-001-…v2.0.md` §5/§9/§10 · `governance/EUA-E19_*` · `governance/DHR-AUDITOR-EXTERNO-014_*` · `AGENTS.md` §11 · `docs/mapa/MAPA-PROJETO.md`
