---
handoff_id: HO-2026-10-18-57
previous: HO-2026-10-18-56
data: 2026-10-18
branch: claude/amazing-fermat-dnbjtz
base_commit: 6549517
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATA v1.11 HOMOLOGADAS (DHR-SPEC006-002/-003); H-001 ABERTA — Andraus quer levá-la à decisão final (tecnologia incluída); Fase 1 (roteamento) executada neste PR, Fase 2 (H-001) é o próximo passo; próxima Spec do ROADMAP = SPEC-007 (abertura pendente)
fase: spec-first
autor: Orquestrador
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Objetivo da frente atual — necessidades e prioridades de Andraus (chat, 2026-10-18)
- **P0 — Medir hash/carimbo:** FEITO (Fase 0). Hash/delta −26% a −31% por rodada, manter; carimbo dispensa ≈ 15 atas, manter. Desperdício real = agente caro em ajuste mínimo + rodada integral repetida. Registro: final de `governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md`.
- **P1 — Roteamento de modelos por tarefa (Fase 1): FEITO neste PR** (ordem expressa de Andraus, 2026-10-18; arquivos protegidos autorizados: emenda à `DHR-ROTEAMENTO-003` §7, `scripts/roteador_modelos.py` + testes, detector de ramos, `MECANISMOS.json`, selo; **vedado** mexer em agentes, `AGENTS.md`, H-001). Como usar (Orquestrador):
  - Classes: **M** (Orquestrador) · **S1/S2** (Revisor → sonnet) · **S3** (Revisor → opus) · **O** (Especificador → opus). Agrupar a fila da rodada por classe: `python scripts/roteador_modelos.py classificar ficha.json` (ficha = `{"achados":[{id,arquivo,linha,antigo,novo,condicao,[natureza|cria_*]}]}`).
  - Chamada de agente com `model` exige no prompt `CLASSE-TAREFA: <classe>` **igual à classe que o hook DERIVA** de fatos (R-AC4) e `model` igual à tabela; senão nega (fail-closed). Linhas próprias no prompt: `ALVO: <plan.md>` (Revisor), `BASE:` + `PARECER:` (delta), `FICHA: <json>`. Especificador (abertura de Spec/Plan/errata) ⇒ O; Revisor integral de Spec CRITICAL ⇒ S3 (opus), delta ⇒ S2 (sonnet), ficha só de conferência ⇒ S1. `effort` segue negado (piloto de esforço pendente, ~150–200 mil tokens, não bloqueia nada). `CLASSE-TAREFA: M` a agente é negada.
  - Classe M: aplicar a ficha → gates → `python scripts/roteador_modelos.py conferir ficha.json` (diff só nas linhas listadas); divergiu ⇒ **escala** (lote O). Correção M/S nunca cria mecanismo (congelamento).
  - Continuar o mesmo agente por `SendMessage` quando o modelo for o mesmo.
- **P2 — H-001: decisão final, tecnologia incluída, sem pendência nem quebra documental (Fase 2)** — próximo, já usando o roteamento. Um PR atômico + `check_doc_sync` etc. (§5).
- **P3 — Processo:** um PR por frente de trabalho (mesclar documentos sozinho com CI verde — `AGENTS.md` §10); detector de ramos órfãos **entregue** (`scripts/check_branches.py` + hook SessionStart, informativo). **Andraus já apagou os 12 ramos contidos e ligou "apagar ramo após o merge" no GitHub.**

## 2. Estado (fatos conferidos em 2026-10-18)
- `main` = `6549517` (PRs #118–#121 mesclados). Verificadores sem ERRO (resíduo herdado: `check_refs` 1 ERRO em `governance/propostas/AUDITORIA-INDEPENDENTE-SPEC006/RELATORIO.md:227`; COE-14 WARN: `gate_extra.py`/`spec_delta.py` fora de `governance/MECANISMOS.json` — não incluídos aqui por estarem fora do escopo autorizado).
- **SPEC-006 (13 funções `CKG-001..013`) = baseline v1.7 + errata v1.11 (Major, condicionada)**; plan.md sha256 `0f461e88…`. Parecer do Revisor = CONFORME condicional (teto: H-001 aberta). Não foi subdividida em Specs numeradas (Opção 2, `DHR-SPEC006-OPCAO2-001`; Plan v1.8 arquivado em `governance/propostas/SPEC-006/linha-spec006-plan/`). ROADMAP:177 diz "H-001 permanece ABERTA".
- Ramos remotos: só `main` e o ramo desta sessão; PRs #31 e #2 fechados. Os 8 ramos com commits próprios listados em `governance/propostas/SPEC-006/LISTA-RAMOS-E-PRS-OBSOLETOS-2026-10-18.md` já não aparecem em `origin` (conferir com `python scripts/check_branches.py`).

## 3. Histórico resumido (HO-34..56; cópias integrais em `docs/handoffs/`)
- SPEC-006 refeita e reconciliada com a v1.7 homologada (PR #118); ferramentas `spec_delta.py`, `gate_extra.py`, atas `DHR-BACKLOG-ABERTURA-001`, `DHR-REVISOR-DELTA-001`. Errata v1.11 homologada (`DHR-SPEC006-003`; não fecha M-001). Plano + Fase 0 (PR #121).
- Lições: não empurrar WIP enquanto o Especificador edita; ao reescrever o handoff, arquivar o anterior como **cópia exata** (HO-04) e não citar ata inexistente (HO-06); heredoc sem aspas expande crases — usar `'EOF'`.

## 4. Verificado
Fase 1: `tests/test_roteador_modelos.py` e `tests/test_check_branches.py` (no CI), selo regravado (`gate_manifest.py --check`), mapa regenerado. Nenhum agente, `AGENTS.md` nem decisão aberta alterados.

## 5. Próximo passo único
**Fase 2 (H-001):** (1) Especificador (`CLASSE-TAREFA: O`, opus): estudo [PROPOSTA] (property graph · grafo temporal tipo Graphiti · estrutura em memória/relacional + log append-only · híbrido; critérios INV-07, E3 fail-closed, trace CEM-001, 4Es; reusar Dossiê válido até 2027-01-03); (2) Andraus escolhe a tecnologia (AskUserQuestion); (3) mapa determinístico de ocorrências (ROADMAP 6 · AGENTS 1 · atomic-spec 6 · revisor.md 3 · especificador.md 4 · CATALOGO 23 · RULES 6 · RMR-001 20 · CIC-001 · plan/checks da SPEC-006); (4) PR atômico com ata nova, ROADMAP (decisões), `AGENTS.md` §7, `atomic-spec.md` §12, `revisor.md` §8 (remove o teto "condicional" só da SPEC-006), RMR-001 (BL-003), CATALOGO/CIC, errata da SPEC-006 com Revisor **por delta** (`CLASSE-TAREFA: S2`); troca de referência mecânica = classe M; (5) verificadores + CI verde + mescla — pedir ordem expressa para cada arquivo protegido. **Seguem abertas:** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03.
Pendências só de Andraus: abertura da SPEC-007 (ROADMAP §23 passo 1-bis); demais decisões abertas. Lembrete vigente: assinar o registro de mecanismos como VIGENTE [PRAZO: 2026-10-24].

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
- `DHR-SPEC006-001` (abertura), `-002` (baseline v1.7), `-003` (errata v1.11), `DHR-SPEC006-OPCAO2-001`; `DHR-ROTEAMENTO-003` + Emenda 1 (§7, este PR). Decisões abertas/fechadas: ler o `ROADMAP.md`. **Nenhuma decisão aberta fechada nesta sessão.**

## 7. Becos sem saída
- Dar Bash ao Revisor: rejeitado (DHR-AUDITOR-EXTERNO-009 §2). Não reabrir sem Andraus.
- Refazer a SPEC-006 do zero: já foi (HO-34..40); a baseline é a v1.7+v1.11.
- Dividir a SPEC-006 em Specs numeradas: **não decidido**; só por Andraus.
- 4 agentes (um por modelo/tarefa): trocado por 2 agentes + modelo validado pelo hook.

## 8. Não tocar
- `canon/` BASELINED, specs homologadas (`plan.md` da SPEC-006 só por errata/ordem), `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*`, `AGENTS.md` (só por Andraus). Não regravar `GATE-MANIFEST.sha256` sem decisão dele.

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` (6549517) ou posterior; se posterior, ler o diff
- [ ] CI da `main`; `python scripts/gate_manifest.py --check`; `check_refs.py`/`check_doc_sync.py`/`check_handoff.py`/`check_branches.py`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/BL-029 em espera)
- [ ] PRs abertos (esperado: nenhum além de novos)
- [ ] ROADMAP: "Decisões abertas ativas" ainda lista H-001; linha 177 diz "permanece ABERTA"
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)

## 10. Aguardando Andraus
- H-001 (tecnologia, Fase 2) · SPEC-007 · demais decisões abertas (§5).
- Registro de mecanismos VIGENTE [PRAZO: 2026-10-24]; destino do Auditor Externo (PAUSADO), schemas sem `additionalProperties:false`, piloto de esforço, D-PCC-3/4/5 — ver `docs/handoffs/HO-2026-10-17-34.md` §10 (histórico).

## 11. Ponteiros
`governance/DHR-ROTEAMENTO-003_*` (§7 Emenda 1) · `governance/DHR-ROTEAMENTO-001_*` · `governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md` · `scripts/roteador_modelos.py` · `scripts/check_branches.py` · `docs/agentes/INDICE-AGENTES.md` · `AGENTS.md` §11 · `ROADMAP.md` · `backlog/RMR-001_Painel_Backlog.md` · `docs/mapa/MAPA-PROJETO.md`
