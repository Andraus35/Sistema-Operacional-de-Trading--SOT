---
handoff_id: HO-2026-10-18-59
previous: HO-2026-10-18-58
data: 2026-10-18
branch: claude/amazing-fermat-dnbjtz
base_commit: 836e04b
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATA v1.11 HOMOLOGADAS (DHR-SPEC006-002/-003); H-001 FECHADA por Andraus (DHR-H001-001, Opção C); ERRATA v1.12 HOMOLOGADA — Minor/aditiva (DHR-SPEC006-004, Andraus 2026-10-18); próxima Spec do ROADMAP = SPEC-007 (abertura pendente)
fase: spec-first
autor: Orquestrador
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Objetivo da frente atual — prioridades de Andraus (chat, 2026-10-18)
- **P0 medir hash/carimbo** FEITO; **P1 roteamento de modelos** FEITO e MESCLADO (PR #122, `836e04b`): classes M/S1/S2/S3/O, hook fail-closed com classe DERIVADA de fatos (`ALVO`/`BASE`/`PARECER`/`FICHA`), detector de ramos órfãos, `DHR-ROTEAMENTO-003` §7 (Emenda 1). Uso: `python scripts/roteador_modelos.py classificar|conferir ficha.json`; prompt do agente leva `CLASSE-TAREFA: <classe>` + `model` igual à tabela (Especificador/abertura/errata = O·opus; Revisor delta = S2·sonnet; integral CRITICAL = S3·opus; ficha mecânica = M, o Orquestrador executa). `effort` segue negado (piloto pendente).
- **P2 H-001 (Fase 2): decidida por Andraus em 2026-10-18 — Opção C (PostgreSQL só-inserção, bitemporal, travessia recursiva; índice de grafo derivado desenhado e não ligado; licença PostgreSQL ≈ BSD/MIT; revisão por gatilho no início do BUILD)** — ata `DHR-H001-001`; estudo [PROPOSTA] em `governance/propostas/H001/`. Aplicado neste PR: ata, ROADMAP, `AGENTS.md` §7, `atomic-spec.md` §12, `revisor.md`/`especificador.md` (RPSA registrado e alinhado), CATALOGO, CIC-001, RMR-001 e **errata v1.12** da SPEC-006 (plan+checks, aditiva, sem regra nova).
- **Parecer do Revisor (Sonnet, por delta)** sobre a v1.12: **CONFORME condicional**, 0 Críticas, 0 Médias, 5 Menores (`governance/propostas/PARECER-REVISOR-SPEC006-v1.12-2026-10-18.md`). m1/m2/m4/m5 corrigidas pelo Orquestrador (classe M) **depois** do parecer — hashes finais diferem dos auditados (adendo no parecer); m3 (ADV-09) é ciência de Andraus. Andraus **homologou como Minor/aditiva** (`DHR-SPEC006-004`; correções m1/m2/m4/m5 aceitas sem nova auditoria; m3 ciente).
- **P3 processo:** um PR por frente; Andraus já apagou os 12 ramos e ligou "apagar ramo após o merge".

## 2. Estado (fatos conferidos em 2026-10-18)
- `main` = `836e04b` (PR #122). Este ramo (`claude/amazing-fermat-dnbjtz`) reiniciado da main e à frente com a Fase 2; PR único aberto no fim da sessão.
- SPEC-006: plan.md final sha256 `71834065…` (ver parecer); a v1.11 homologada era `0f461e88…` (auditado `8527addb…`). Errata v1.12 **HOMOLOGADA** (plan.md sha256 `7ce76f10…`, checks `1ee11bb7…`). Pendente só o merge do PR #123 (assinatura).
- Detector `scripts/gate_extra.py::decisoes_abertas_fechadas` lê os IDs "abertos" do Status do plan e **não consulta o ROADMAP**: acusa "H-001 FECHADA" mesmo fechada. Contornado reescrevendo 15 linhas para "decisão do mecanismo físico FECHADA" (neutro, segundo o Revisor). **Ajuste autorizado por Andraus, ainda NÃO feito** (§5).
- Resíduos herdados: `check_refs` 1 ERRO (`AUDITORIA-INDEPENDENTE-SPEC006/RELATORIO.md:227`); COE-14 WARN `gate_extra.py`/`spec_delta.py` fora de `MECANISMOS.json`.

## 3. Histórico resumido (HO-34..57; cópias integrais em `docs/handoffs/`)
- SPEC-006 reconciliada (PR #118), errata v1.11 homologada (`DHR-SPEC006-003`), plano + Fase 0 (#121), Fase 1 roteador (#122). Lições: não empurrar WIP enquanto o Especificador edita; arquivar o handoff anterior como **cópia exata** (HO-04) e commitar o handoff uma só vez por id; heredoc com `'EOF'`; o detector de decisões abertas usa o 1º segmento "·" da linha de "Decisões FECHADAS" como lista e captura todos os IDs dele — novas decisões fechadas entram a partir do 2º segmento.

## 4. Verificado
validate_spec_sot 13/13 · revisor_gate PASSOU_D · check_invariants 0 · check_doc_sync 0 · check_rpsa OK · selo íntegro · mapa em dia (conferir no PR).

## 5. Próximo passo único
(a) mesclar o PR #123 com CI verde (conteúdo já aprovado por Andraus no chat, AGENTS.md §10); (b) **ajustar `gate_extra.py` (AUTORIZADO por Andraus, 2026-10-18)** em PR à parte: `decisoes_abertas_fechadas` deve subtrair as "Decisões FECHADAS" do ROADMAP, com testes, registro em `MECANISMOS.json` (+ `spec_delta.py`) — depois, se quiser, desfazer a grafia dupla "decisão do mecanismo físico FECHADA" no plan (só por errata). Depois: abertura da SPEC-007 (ROADMAP §23 passo 1-bis). **Seguem abertas:** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001. Lembrete vigente: assinar o registro de mecanismos como VIGENTE [PRAZO: 2026-10-24].

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
- `DHR-H001-001` (H-001 fechada, Opção C), `DHR-SPEC006-001/-002/-003`, `DHR-ROTEAMENTO-003` + Emenda 1. Decisões abertas/fechadas: ler o `ROADMAP.md`.

## 7. Becos sem saída
- Dar Bash ao Revisor: rejeitado (DHR-AUDITOR-EXTERNO-009 §2). Refazer a SPEC-006 do zero: redundante. Dividir a SPEC-006 em Specs numeradas: não decidido, só Andraus. 4 agentes por modelo: trocado por 2 agentes + modelo validado pelo hook. Reescrever Specs homologadas antigas que citam H-001 como aberta (SPEC-002/004/038…): não (INV-07; o ROADMAP é a fonte do estado).

## 8. Não tocar
- `canon/` BASELINED, specs homologadas (`plan.md` da SPEC-006 só por errata/ordem), `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*`, `AGENTS.md`, `gate_extra.py` (só por Andraus). Não regravar `GATE-MANIFEST.sha256` sem decisão dele.

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` (836e04b) ou posterior; se posterior, ler o diff
- [ ] CI da `main`; `gate_manifest.py --check`; `check_refs`/`check_doc_sync`/`check_handoff`/`check_branches`/`check_rpsa`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS)
- [ ] PRs abertos (esperado: o da Fase 2 até Andraus decidir)
- [ ] ROADMAP: "Decisões abertas ativas" NÃO lista H-001; "Decisões FECHADAS" a lista (DHR-H001-001)
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)

## 10. Aguardando Andraus
- Merge do PR #123 · SPEC-007 · demais decisões abertas.
- Registro de mecanismos VIGENTE [PRAZO: 2026-10-24]; destino do Auditor Externo (PAUSADO), schemas sem `additionalProperties:false`, piloto de esforço, D-PCC-3/4/5 — ver `docs/handoffs/HO-2026-10-17-34.md` §10 (histórico).

## 11. Ponteiros
`governance/DHR-H001-001_*` · `governance/DHR-SPEC006-004_*` · `governance/propostas/H001/ESTUDO-TECNOLOGIA-H001-2026-10-18.md` · `governance/propostas/PARECER-REVISOR-SPEC006-v1.12-2026-10-18.md` · `governance/propostas/SPEC-006/DELTA-ERRATA-v1.12-2026-10-18.txt` · `governance/DHR-ROTEAMENTO-003_*` (§7) · `scripts/roteador_modelos.py` · `AGENTS.md` §11 · `ROADMAP.md` · `backlog/RMR-001_Painel_Backlog.md` · `docs/mapa/MAPA-PROJETO.md`
