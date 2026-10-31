---
handoff_id: HO-2026-10-31-112
previous: HO-2026-10-31-111
data: 2026-10-31
branch: ccr-599f6762-60qbvg
base_commit: d37c6d1
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (Andraus, 2026-10-31, DHR-SPEC049-001; HIGH D0–D7, uma Spec; Plan pendente, só por ordem de Andraus; NÃO é baseline)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece. Versão anterior (narrativa longa de 2026-10-31): `docs/handoffs/HO-2026-10-31-109.md`.

## 1. Frente atual
**SPEC-049: abertura homologada (`DHR-SPEC049-001`), PR #140 mesclado na `main` (`f22eb37`). Plan pendente, só por ordem de Andraus; condições do Plan na ata §3 (inclui o Menor R3-m01).** Nenhuma outra Spec aberta. Sessão de 2026-10-31 (ramo `ccr-599f6762-60qbvg`): auditoria de burocracia e higiene entregue em `governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` (PROPOSTA, nada normativo aplicado).

## 2. Estado (fatos conferidos em 2026-10-31)
- **Aplicado nesta sessão (sem arquivo normativo):** `docs/UPGRADES/` movido para `docs/_legacy/UPGRADES/` (git mv; `.rgignore` ajustado); HANDOFF reescrito compacto, anterior arquivado.
- **Aplicado por ordem de Andraus (chat):** patch do `check_refs.py` (WARN 6→2, 20/20 testes, falha no script atual) em `governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-PATCH-CHECK-REFS-E-MAPA-2026-10-31.md` + 2 `.patch`; selo do gate regravado e MECANISMOS.json atualizado. Mapa JSON fora da árvore: adiado (consumidores: `build_map.py` e 2 testes).
- **Não aplicado, por ser do CODEOWNERS ou normativo:** `revisao-independente/` (citada em `governance/AVALIACAO-MECANISMOS-REVISOR-2026-10-17.md`), status nos 33 `_PROPOSTA`, atas COE-11.
- **Atas recentes:** `DHR-SPEC049-001`, `DHR-DIMENSIONAMENTO-001`, `DHR-RETRO-001`, `DHR-CHECKS-INFO-001`, `DHR-MERGE-001`.

## 3. Lições (fluxo que funcionou — repetir)
Ordem classe O ao Especificador (`model: opus` + `CLASSE-TAREFA: O` + `PARECER:`/`FICHA:` em linhas próprias) → gates do Orquestrador → commit/push → `delta_pacote.py` (rodada ≥2) → Revisor (`CLASSE-TAREFA`+`ALVO:`+`SHA256-ALVO:`) → transcrever parecer em `governance/propostas/<X>/` com `ACHADOS-ESTRUTURADOS` e `FICHA-M` → `aplicar_ficha_m.py` → `loop_ledger.py` → AskUserQuestion a Andraus → ata + `check_rpsa.py --register` → gates → PR → mesclar só ao comando dele. Especificador pode estourar limite de uso: retomar por `SendMessage`.

## 4. Verificado (LOOP-001 passo 4 e gates)
Categorias mais recorrentes: **C07** citação/âncora (34) · **C01** contradição interna (21) · **C02** ambiguidade (20). Lacunas de prevenção abertas: C99, C01, C06, C03, C10. Medido na auditoria: 35 rodadas, 0 Críticas, 39 Médias, 138 Menores; abertura da SPEC-049 = 906 mil tokens em 6 chamadas.

## 5. Próximo passo único
Andraus escolhe o que fazer com a auditoria (grupos 2 e 3 do relatório: regra de parada de rodadas, hash de delta obrigatório, mecanismos em 3 camadas, roteamento por modelo fixo — todos exigem ordem dele e medição). Pendentes à parte: erratum F2 da SPEC-020; errata da SPEC-007 (inclui citação de versão antiga do `WORKFLOW.md` em `plan.md:2650`); atualização de CATALOGO/RMR-001 (BL-017); CONFLICT-MAP; mecanismo de assinatura antes de qualquer BUILD; retrospectiva da SPEC-049 ao fechar a Spec.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-SPEC049-001`, `DHR-DIMENSIONAMENTO-001`, `DHR-RETRO-001`, `DHR-ROTEAMENTO-007`, `DHR-DOCSYNC-003`, `DHR-MERGE-001`, `DHR-LOOP-001`. Decisões abertas/fechadas: ler o `ROADMAP.md`.

## 7. Becos sem saída
Dar Bash ao Revisor; refazer SPEC-006/020; tratar decisão do `AGENTS.md` como mais atual que o ROADMAP; chamar Especificador/Revisor sem `model`+`CLASSE-TAREFA` (o hook nega); editar baseline fora de erratum homologado; mesclar sem ordem de Andraus; mexer em script do CODEOWNERS sem ordem.

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas (só por erratum), `ROADMAP.md`, `atomic-spec.md`, `AGENTS.md`, `.claude/agents/*`, `CONFLICT-MAP`, `GATE-MANIFEST.sha256` e scripts do CODEOWNERS.

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` ou posterior; se posterior, ler o diff; `git fetch origin main`
- [ ] PRs abertos; se o ramo `ccr-599f6762-60qbvg` já foi mesclado, reiniciá-lo de `origin/main`
- [ ] `gate_manifest.py --check`, `check_refs`, `check_doc_sync`, `check_handoff`, `check_rpsa`, `check_coesao`, `build_map --check`
- [ ] `python scripts/backlog_triggers.py`
- [ ] Suíte: `python -m unittest discover -s tests` e `node tests/test-ask-guard.js`
- [ ] ROADMAP: linhas "Decisões abertas ativas"/"Decisões FECHADAS"; versão vigente de `WORKFLOW.md`

## 10. Aguardando Andraus
Plano da SPEC-049 (só por ordem dele) · destino da auditoria de burocracia (grupos 2 e 3) · propostas P7–P9 das retrospectivas · H1–H8 e M1–M8 da auditoria de economicidade · erratas/atualizações listadas no §5 · demais decisões abertas do ROADMAP · destino do Auditor Externo (PAUSADO), D-PCC-3/4/5.

## 11. Ponteiros
`governance/propostas/MELHORIAS-PROCESSO/` (3 relatórios + auditoria de burocracia) · `governance/aprendizado/` · `governance/MECANISMOS.json` · `docs/handoffs/` · `docs/mapa/MAPA-PROJETO.md` · `specs/features/SPEC-049/` · atas em `governance/` (nome começa pelo ID).
