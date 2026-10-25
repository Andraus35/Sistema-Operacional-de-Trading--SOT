---
handoff_id: HO-2026-10-25-87
previous: HO-2026-10-25-86
data: 2026-10-25
branch: ccr-3235944c-duo3sl
base_commit: 01a8290
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12; SPEC-007 (reduzida: formação + selo) = Plan v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002, Revisor R5 CONFORME condicional); SPEC-049 (WikiRAG Reading View) = slot indicativo, NÃO aberta; sem BUILD (fase spec-first). Tudo MESCLADO na main (PR #130, c9f98b3)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece. Máx. 150 linhas.

## 0. Quem é Andraus e como trabalhar com ele (LEIA PRIMEIRO)
- Andraus é o Decisor Final, trader (não técnico). **Fale em linguagem de trader**: o que muda na prática, sem siglas soltas; resumo em 3–5 linhas; **recomendação primeiro, marcada "(Recomendado)"**, via `AskUserQuestion` a cada entrega/parecer (o hook de fim de turno `andraus-ask-guard.js` bloqueia o encerramento sem pergunta).
- **Nunca decidir, homologar ou fechar decisão aberta por ele (CONS-01).** A assinatura dele = decisão no chat citada em ata (AGENTS.md §10). Mudança em selo do gate, `AGENTS.md`, `MECANISMOS.json`, mecanismo/gate novo: só por ordem expressa dele.
- Ele prefere: qualidade máxima do Plan antes de seguir; economia de rodadas caras (por isso o Orquestrador corrige Menores mecânicos); melhoria contínua do loop dos construtores sob os 4Es; merge via PR após CI verde quando ele ordenar ("Dar Merge quando fechar o plan" foi cumprido para o PR #130). Sem push direto à `main`; sem criar PR sem pedido dele.
- Ele já decidiu (ver atas): dividir SPEC-007 (formação+selo) e SPEC-048 (consulta/pacote); autenticação dos atos dele por assinatura criptográfica em dispositivo físico (mecanismo = BUILD); livro *Evidence-Based Technical Analysis* só uso pessoal; todo analista "fora" até ele confirmar modelo de casa.
- **Erro a não repetir:** li "achados menores não são corrigidos pelo orquestrador" como proibição; era o contrário (`DHR-ROTEAMENTO-006` supera a 005). Em frase ambígua dele, perguntar o alcance antes de gravar regra.

## 1. Onde estamos (fatos de 2026-10-25)
- **PR #130 MESCLADO** (`c9f98b3`, CI verde): Plan SPEC-007 v2.3 e Plan SPEC-048 v1.4 baseline; LOOP-001 (ledger, causas, retrospectivas); roteamento de achados R-AC5/R-AC6 (selo aprovado por ele); `scripts/aplicar_ficha_m.py` (+ `tests/test_aplicar_ficha_m.py`, no CI e em `MECANISMOS.json`).
- **Correção de Menores (regra vigente, `DHR-ROTEAMENTO-006`, AGENTS.md §12 passo 0):** ao pedir parecer ao Revisor, EXIGIR bloco `<!-- FICHA-M {"achados":[{"id","sev":"MENOR","arquivo","antigo","novo","condicao"}]} -->` para Menores mecânicos; o Orquestrador roda `python scripts/aplicar_ficha_m.py <parecer.md>` (dry com `--dry`). Média/Crítica/semântica: Especificador com `PARECER:` + `FICHA:` classificando TODOS os achados (hook R-AC5/R-AC6). Revisor não grava arquivo nem roda Bash: transcrever o parecer (com bloco `ACHADOS-ESTRUTURADOS`) e rodar `python scripts/loop_ledger.py`.
- Sem BUILD; fail-closed: nada é liberado/carimbado/consultado sem atos de Andraus (RIGHTS, EXT_TRANSMISSION, LOCAL_EXECUTOR, ACTREC). Pacotes vazios com falta declarada são o comportamento correto até lá.
- Respondidas por ele na homologação da 048 (opção recomendada): P-1 só ele confirma analista↔modelo; P-2 pedido só como campos de lista fechada; P-3 resumo desligado até ele ligar.

## 2. Estado (fatos conferidos em 2026-10-25)
- `main` = `01a8290` (inclui o merge `c9f98b3` do PR #130 e o registro automático RPSA). O ramo `ccr-3235944c-duo3sl` foi mesclado; este handoff recomeça o ramo da `main`.
- Planos homologados (baseline, sem BUILD): SPEC-007 v2.3 e SPEC-048 v1.4 (12 RULE-RET, 12 BASpec, 8 EC, 14 cenários, 23 ADV). Pareceres: SPEC-007 R1–R6, SPEC-048 R1–R5; o Revisor sempre tem teto "CONFORME condicional" (não roda o gate).
- Estados do painel de backlog não mudaram (sem promoção — só Andraus). Benchmark `inteligencia-sot@0abd22e` ausente (citações não conferidas).

## 3. Decisões abertas (CONS-01 — ler `ROADMAP.md`; não fechar)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · "produtor/gatilho de promoção" · mecanismo da autenticação (BUILD) · se o Manager conta como "quem pediu" a consulta (SPEC-048).

## 4. Verificado (2026-10-25)
`validate_spec_sot` OK nos dois Planos, `revisor_gate` PASSOU_D, `check_invariants` 0, `check_refs` 0 ERRO, `check_coesao` 0 ERRO, `check_doc_sync` 0 ERRO (1 WARN histórico: SPEC-007 cita WORKFLOW v1.2), `check_handoff` e `build_map --check` verdes, suíte `tests/test_*.py` e `npm test` verdes, CI do PR #130 verde.

## 5. Próximo passo único (ordem)
1. **Retrospectivas de fechamento SPEC-007 e SPEC-048** em `governance/aprendizado/RETROSPECTIVAS.md` (ambas PENDENTE; roteiro lá; incluir a "Retratação" da nota de desvio). Individual (Especificador, Revisor, Orquestrador) + coletiva. Rodar `python scripts/loop_ledger.py --retro-check SPEC-007` e `SPEC-048`; **sem retrospectiva FEITA não se abre outra Spec** (salvo dispensa dele). Três categorias mais recorrentes e lacunas: ver `LEDGER-ACHADOS.md`.
2. **Levar a ele as propostas de melhoria** (nunca aplicar sem ordem): `governance/propostas/MELHORIAS-PROCESSO/RELATORIO-MELHORIAS-AGENTES-E-GATES-2026-10-24.md` (prioridades: recibo de gate, fechamento de códigos + matriz de rastreio, varredura de impacto, histórico fora do plano) + as novas da retrospectiva.
3. Só depois, por ordem dele: abertura da SPEC-049, ou errata aditiva SPEC-006 (E-1..E-4), emenda SPEC-020 (F1/F2), errata de re-apontamento (SPEC-002/003/006), errata SPEC-007 (E7-1..E7-3).

## 6. Lições operacionais
- Roteador exige linhas `ALVO:` (um caminho), `BASE:` e `PARECER:` em linha própria; ordem ao Especificador sem `FICHA:` completa é negada. Commitar versões intermediárias do Plan permite revisão por delta real (BASE = commit da versão anterior).
- Handoff: HO-04 exige novo `handoff_id` a cada edição e o anterior em `docs/handoffs/HO-<id>.md` como **cópia exata da versão commitada** (`git show HEAD:HANDOFF.md`); não citar ata futura (HO-06).
- Guarda pós-revisor (DHR-AUDITOR-EXTERNO-018): após cada parecer, anotar adendo G1/G2 (rodar `revisor_gate.py` no plan.md e conferir âncoras do núcleo do Passo 0).
- Subagentes: o Especificador e o Revisor podem parar por limite de uso; retomar por `SendMessage`. Revisor reporta via `SubagentHandback`; relatório recuperável do transcrito em `/root/.claude/projects/.../subagents/`.
- Mapa: após mexer em `.md`, `python scripts/build_map.py`; COE-14 exige `MECANISMOS.json` ao criar mecanismo; `tipo` só do enum (hook, guarda, gate, detector, utilitario, workflow, agente, config, skill).
- Benchmark `inteligencia-sot@0abd22e` ausente: citações dele não conferidas (usar `add_repo` leitura se precisar).

## 7. Becos sem saída
Dar Bash ao Revisor; Orquestrador corrigir Média/Crítica/semântica; abrir SPEC-049 ou outra Spec sem retrospectiva e sem ordem; editar baselines (SPEC-002/003/006/007/020/048) fora de errata/ordem; usar motores/código do Inteligencia-SOT (Benchmark apenas); incluir o livro como fonte sem os atos de liberação; push direto à `main`.

## 8. Não tocar
`canon/` BASELINED, specs homologadas, `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*`, `AGENTS.md`, `CONFLICT-MAP` e selo `GATE-MANIFEST.sha256` — só por ordem expressa de Andraus.

## 9. Reverificar ao vivo
- [ ] `git log -1` posterior a `01a8290` (main); ramo `ccr-3235944c-duo3sl` foi MESCLADO: trabalho novo = recomeçar o ramo da `main` (`git checkout -B ccr-3235944c-duo3sl origin/main`)
- [ ] CI da `main`; `gate_manifest.py --check`; `check_refs`/`check_doc_sync`/`check_handoff`/`check_rpsa`/`check_coesao`/`loop_ledger.py --check`/`build_map.py --check`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/017 vinculados à SPEC-048, BL-035 à SPEC-007, sem promoção)
- [ ] PRs abertos; `ROADMAP.md` "Decisões abertas ativas"; versão vigente de `WORKFLOW.md`
- [ ] suíte: `for t in tests/test_*.py; do python -m unittest $t; done` e `npm test`

## 10. Aguardando Andraus
**Só dele:** ordem para a retrospectiva/melhorias do loop (propostas), abertura da SPEC-049, errata SPEC-006 / emenda SPEC-020 / errata de re-apontamento / errata SPEC-007, autenticação dos atos (BUILD), atos por fonte para o livro, e as decisões abertas da seção 3 (G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, promoção, Manager como "quem pediu").

## 11. Ponteiros
Atas: `DHR-SPEC048-002` (homologação), `DHR-SPEC048-001`, `DHR-SPEC007-001..007`, `DHR-ROTEAMENTO-003/004/006`, `DHR-LOOP-001`. Planos: `specs/features/SPEC-007/plan.md` (v2.3), `specs/features/SPEC-048/{plan,checks,ABERTURA,research}.md`. Pareceres: `governance/propostas/SPEC-007/`, `governance/propostas/SPEC-048/` (R1–R5). Aprendizado: `governance/aprendizado/{LEDGER-ACHADOS,CAUSAS-PREVENCAO,RETROSPECTIVAS}.md`. Script de Menores: `scripts/aplicar_ficha_m.py`. Mapa: `docs/mapa/MAPA-PROJETO.md`.
