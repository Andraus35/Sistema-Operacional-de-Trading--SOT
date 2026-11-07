---
handoff_id: HO-2026-11-01-152
previous: HO-2026-11-01-151
data: 2026-11-01
branch: ccr-4bd4e8a0-d92lc7
base_commit: b1b0e1b
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo `ccr-4bd4e8a0-d92lc7`; Camada A)

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece. *(Reescrito limpo em HO-152: o texto anterior, que misturava frentes de outras sessões, está em `docs/handoffs/HO-2026-11-01-151.md` — nada perdido, INV-07.)* **Atenção:** o hook de início só lê `handoffs/<ramo>.md` quando a sessão estiver NESTE ramo; numa sessão em ramo novo ele lerá o `HANDOFF.md` da raiz (outra cadeia). Para continuar esta frente, leia este arquivo explicitamente.

## 1. Frente atual
**Auditoria do pré-check do Especificador + frente de burocracia A7/A4/A9 — ENCERRADA e na `main`.** Nada pendente neste ramo; nenhum PR meu aberto (os #167–#170 são de outras sessões). Entregue por ordens expressas de Andraus (chat/AskUserQuestion, 2026-11-01):
- **#153 `726c67a`** — `DHR-PRE-ENTREGA-001`: `scripts/pre_entrega.py` (pré-gate unificado; selado em `GATE-MANIFEST.sha256` + CODEOWNERS; passo no CI; `util.pre-entrega`) e P-F no `especificador.md`. **Fluxo:** o Orquestrador roda `python scripts/pre_entrega.py specs/features/<SPEC>` e anexa o `pre-entrega.json` (bloqueantes = os do CI; detectores informativos) antes do Revisor; o Especificador segue sem Bash.
- **#158 `297a2d9`** — `DHR-A7A4-001` (**A7-lite**: `governance/MODELO-ATA-OPERACIONAL-CURTA.md`, ata ≤ 15 linhas só para mudança puramente operacional; **A4-b**: o experimento P10 mede também a abertura) e `DHR-A9TESTE-001` (**A9-teste**: `revisor.md` → Signal Package, `especificador.md` → CC-01..CC-12, `tests/test_agentes_sem_fatos_defasados.py` + CI + `det.agentes-fatos-defasados`).
- **#160 `32acfe7`** — backlog **BL-044..BL-047** (`Em espera`): BL-044 medição no próximo Plan, BL-045 P-B + C-4 estreito + C-1a/C-1b (C-2 a reformular), BL-046 A9-completo — os três em `spec:SPEC-008 em redação` (mesmo vínculo do BL-043); BL-047 A8 em `spec:SPEC-040 em redação`.
**Decidido por Andraus:** P-B e C-4 "testar antes de instalar"; A7-lite (não o log único); A4-b (não fundir abertura e Plan); A9-teste sim, A9-completo depois da medição; a medição usa a SPEC-008 (se ele abrir outra, re-aponta na abertura). Em `governance/propostas/MELHORIAS-PROCESSO/PRE-ENTREGA/` e `A9/` ficam as propostas (nada instalado além do que está acima).

## 2. Estado (fatos conferidos ao vivo em 2026-11-01, `main` em `b1b0e1b`)
- Suíte **503 testes** OK; `node tests/test-hooks.js`, `test-ask-guard.js` e `npm test` (11 schemas) OK.
- `check_doc_sync` ERRO=0; `check_coesao` ERRO=0 (2 INFO); `check_rpsa` OK; `gate_manifest --check` íntegro; `build_map --check` em dia; `check_handoff` ERRO=0 (WARN HO-03 esperado: arquivos mudaram depois do último handoff).
- `check_refs`: **ERRO=0 WARN=1 só depois de `python scripts/loop_ledger.py`** — o `LEDGER-ACHADOS.md` agora é **gerado e não versionado** (`DHR-LEDGER-GERADO-001`); sem gerar, dá ERRO=2 falso.
- `backlog_triggers`: 4 disparados sem registro (BL-010/015/017/035) e 2 ATIVADOS (BL-003/BL-011) — antigos, de Andraus; não são desta frente.
- Medidas desta frente: detectores atuais pegaram **0/3 Médias** do Plan v1.0 da SPEC-049 (o ganho do pré-gate é prova anexa e antecipação, não recall); C-1a/C-1b úteis como informativos; **C-2 inviável**; ✔ sem evidência nenhuma **escapa** do C-4; catálogo de Autopré-check = **31** itens (16 D, 15 ATESTADO); atas: 159 (só ≈ 8 puramente operacionais); as 14 Specs feitas são todas HIGH/CRITICAL.

## 3. Lições (repetir)
(1) `git fetch origin main` antes de qualquer PR — a `main` andou 4 a 5 vezes durante a sessão; resolver **mesclando `origin/main` no ramo** (nunca force), `mergeable_state: clean` + CI verde e merge commit com `expectedHeadSha`. (2) Handoff próprio em `handoffs/<ramo>.md` (Camada A); não editar o `HANDOFF.md` da raiz. (3) Não editar arquivos durante a suíte (o `test_pre_entrega` roda `build_map --check` e vê o mapa desatualizado). (4) `COE-14`: `ata` aceita um ID só e o tipo é `utilitario` sem acento; `check_rpsa --register` exige linha própria `| Data |`. (5) **Conferir números antes de escrever** (erros meus: 32→31 itens, 80→58 atas, 435→416 testes). (6) `pkill -f` casa o próprio shell — matar por PID; `sleep` e laços de polling são barrados/ruidosos: consultar o resultado direto. (7) Ata de mudança em agente é **completa**; o modelo curto exclui `.claude/agents/*`.

## 4. Verificado (LOOP-001 passo 4)
Sem parecer do Revisor nesta frente (nenhuma Spec em rodada); nada novo no ledger a registrar. Lacunas de prevenção abertas: ver `python scripts/loop_ledger.py` (C99, C01, C06, C03, C10 até 2026-10-31).

## 5. Próximo passo único
**Andraus manda abrir uma Spec** (recomendação: **SPEC-008**, a próxima do ROADMAP) e roda-se junto o **BL-044**: Dossiê de Pesquisa → proposta de abertura → homologação dele antes do Plan; `python scripts/backlog_triggers.py --abertura SPEC-008` lista BL-026/043/044/045/046 e o Plan declara a Disposição de cada um ([STRUCT-13]); pré-gate antes de cada entrega; medir tokens e Médias por rodada **da abertura e do Plan** (protocolo no fim de `PRE-ENTREGA/PROPOSTA-PRE-ENTREGA-2026-11-01.md`). **Abrir Spec só por ordem dele.**

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-PRE-ENTREGA-001`, `DHR-A7A4-001`, `DHR-A9TESTE-001`, `DHR-BACKLOG-ABERTURA-001`, `DHR-LEDGER-GERADO-001`. Decisões abertas/fechadas: ler o `ROADMAP.md` (linhas "Decisões abertas ativas"/"Decisões FECHADAS").

## 7. Becos sem saída
Abrir Spec sem ordem; instalar P-B, C-4 ou A9-completo antes da medição do BL-044; log único de decisões (A7-log, rejeitado pela medição); reintroduzir o C-2 largo; fundir abertura e Plan para todas as Specs (A4 original — a premissa quase não tem população); mexer em agentes, selo ou `AGENTS.md` sem ordem; editar o `HANDOFF.md` da raiz neste ramo; tratar o mapeamento BL→Spec como decidido por Andraus (é julgamento do Orquestrador); `sleep`/polling para esperar CI.

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas (só por erratum), `ROADMAP.md`, `atomic-spec.md`, `AGENTS.md`, `.claude/agents/*`, `CONFLICT-MAP`, `GATE-MANIFEST.sha256` e scripts do CODEOWNERS (inclui `scripts/pre_entrega.py`) — só por ordem expressa de Andraus.

## 9. Reverificar ao vivo
- [ ] `git fetch origin main`; `git log -1` == `base_commit` (b1b0e1b) ou posterior; se posterior, ler o diff; PRs abertos (hoje #167–#170, de outras sessões); se o ramo foi mesclado, `git checkout -B <ramo> origin/main`
- [ ] **`python scripts/loop_ledger.py` ANTES de `check_refs`** (ledger gerado); depois `check_refs`, `check_doc_sync`, `check_handoff`, `check_rpsa`, `check_coesao`, `gate_manifest.py --check`, `build_map.py --check`
- [ ] `python scripts/backlog_triggers.py` (BL-044..046 vinculados à SPEC-008; BL-047 à SPEC-040)
- [ ] Suíte: `python -m unittest discover -s tests` (**503**, ~2 min — não editar nada durante), `node tests/test-hooks.js`, `node tests/test-ask-guard.js`, `npm test` (11 schemas)
- [ ] ROADMAP: decisões abertas/fechadas; PRs #169 (mapa gerado) e #170 (ledger/check_refs) podem mudar o `build_map`/`check_refs` — reler antes de confiar nos números acima

## 10. Aguardando Andraus
1. **Mandar abrir uma Spec** (SPEC-008 recomendada) — destrava BL-044/045/046 e o P10 com abertura. 2. Corrigir ou confirmar o mapeamento BL→Spec (BL-044..046 → SPEC-008; BL-047 → SPEC-040). 3. Depois da medição: instalar ou não P-B, C-4 estreito, C-1a/C-1b e A9-completo (cada um com ata, selo e `MECANISMOS.json`). 4. A8 (BL-047) só com telemetria por Spec (SPEC-040). 5. Antigos, fora desta frente: ATIVADOS BL-003/BL-011 e os 4 disparados sem registro; PRs #167–#170 de outras sessões. A pauta consolidada de decisões da burocracia está em `governance/PAUTA-DE-DECISOES.md`.

## 11. Ponteiros
`governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-ESPECIFICADOR-PRECHECK-2026-11-01.md` (relatório e backtest) · `.../PRE-ENTREGA/` (propostas, protocolo de medição, catálogo AP, detectores novos, mutação) · `.../A9/` · `.../PROPOSTA-A7-*`, `PROPOSTA-A4-*` · `governance/MODELO-ATA-OPERACIONAL-CURTA.md` · `backlog/RMR-001_Painel_Backlog.md` (BL-043..047) · atas `governance/DHR-PRE-ENTREGA-001*`, `DHR-A7A4-001*`, `DHR-A9TESTE-001*` · `docs/handoffs/` e `docs/handoffs/ramo-*/` (cadeias) · `HANDOFF.md` da raiz (outra cadeia, fallback) · `docs/mapa/MAPA-PROJETO.md` (índice gerado).
