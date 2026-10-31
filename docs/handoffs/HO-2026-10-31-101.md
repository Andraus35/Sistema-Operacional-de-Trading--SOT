---
handoff_id: HO-2026-10-31-101
previous: HO-2026-10-31-100
data: 2026-10-31
branch: ccr-3a6df80c-nej9ne
base_commit: 79fa35a
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-049 (WikiRAG Reading View) = slot indicativo, NÃO aberta
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Frente atual
As 3 frentes da ordem `DHR-RETRO-001` estão FEITAS e homologadas (errata SPEC-006 v1.13 · ERRATUM-SPEC020-002 F1 · ERRATUM-REAPONT-001). **PR #133 MESCLADO** na `main` (`82296ba`). Nenhuma Spec nova aberta. **RULE-ECC-07 (dimensionamento de Spec: alerta 1.900 / teto 2.000 linhas de corpo; gatilho de nova abertura) aplicada por ordem de Andraus** (`DHR-DIMENSIONAMENTO-001`; RULES.md, atomic-spec §15, especificador.md §5; prospectiva desde SPEC-049). **PR #134 MESCLADO** na `main` (`2917341`). Check determinístico em `validate_spec_sot.py` **não instituído**. **Auditoria de higiene/economicidade feita** (`governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-HIGIENE-E-ECONOMICIDADE-2026-10-31.md`): abertura ≈47–49 mil tokens/chamada; propostas H1–H8 e M1–M8 aguardam Andraus. **Regra de Andraus (2026-10-31): equilibrar os 4Es — Economicidade nunca às custas de Eficácia/qualidade da documentação estratégica.** Aplicado (sem risco de Eficácia): `.rgignore` (só mapa .json e docs/handoffs) e seção 2-bis do ledger (tamanho do Plan × rodadas; tokens n/m). Correção: `check_invariants` leva 0,9 s (não >2 min). **PR #136 MESCLADO** na `main` (`79fa35a`). **Delta por hash (DHR-DELTA-HASH-001, ordem de Andraus):** em toda rodada seguinte o Orquestrador roda `python scripts/delta_pacote.py <plan.md> --base <ref> --out <pasta do parecer>` e cola `ALVO/BASE/SHA256-ALVO/DELTA` no pedido ao Revisor; o Revisor declara `MODO:` e `SHA256-ALVO:` no cabeçalho; ledger seção 2-ter mede (base: 0/32 rodadas com hash). Hook R-AC7 **não** exige (não instituído).

## 2. Estado (fatos conferidos em 2026-10-31)
- **Mesclados na `main`:** PR #136 (`79fa35a`, auditoria de economicidade + `.rgignore` + ledger 2-bis/2-ter + delta por hash), PR #135 (handoff), PR #134 (`2917341`, RULE-ECC-07 dimensionamento), PR #133 (`82296ba`, 3 frentes DHR-RETRO-001), PR #131 (errata SPEC-006 + retrospectivas + roteamento, `b097580`) e PR #132 (aviso de merge + erratum SPEC-020 + detector, `6d3b0f9`).
- **Atas:** `DHR-RETRO-001` (§1–§10: P1–P6 aprovadas; respostas Q-1..Q-11, Adendos 1–7) · `DHR-SPEC006-005` · `DHR-SPEC020-002` · `DHR-REAPONT-001` · `DHR-ROTEAMENTO-007` · `DHR-DOCSYNC-003` · `DHR-MERGE-001`.
- **Mecanismos novos (ordem de Andraus):** **R-AC7** — toda chamada a Especificador/Revisor exige `model` + `CLASSE-TAREFA` (S1/S2→sonnet, S3→opus, O→opus; hook deriva a classe de fatos: Revisor exige `ALVO:` [+ `BASE:`/`PARECER:` p/ delta ou `FICHA:`]); `esqueleto` marca `aplicado_m`; `_cria_algo` ignora ID já no arquivo; `check_doc_sync` casa ID inteiro; **`scripts/merge_ready.py` + 3ª regra do `andraus-ask-guard.js`** (avisa 1× por commit-cabeça quando é possível e seguro mesclar → perguntar a Andraus; nunca mescla). Selo `GATE-MANIFEST.sha256` regravado 2× por ordem dele (roteador_modelos.py; check_doc_sync.py).
- **AGENTS.md** (por ordem dele): §12 passo 0 (roteamento) e §7 (SPEC-020-PRINC-001 FECHADA). Estado das decisões vem SÓ do `ROADMAP.md`.

## 3. Lições (fluxo que funcionou — repetir)
Ordem classe O ao Especificador (`model: opus` + `CLASSE-TAREFA: O` + `PARECER:`/`FICHA:` em linhas próprias) → gates do Orquestrador → commit/push → `delta_pacote.py` (rodada ≥2) → Revisor (`CLASSE-TAREFA`+`ALVO:`+`SHA256-ALVO:`; derive a classe com `roteador_modelos.derivar_classe`) → transcrever parecer em `governance/propostas/<X>/` com blocos `ACHADOS-ESTRUTURADOS` e `FICHA-M` (chave `achados`) → `aplicar_ficha_m.py` → `roteador_modelos.py esqueleto` → `loop_ledger.py` → perguntar a Andraus (AskUserQuestion; hook obriga) → ata + `check_rpsa.py --register` → gates → PR → esperar aviso "pronto" → mesclar só ao comando dele. Especificador pode estourar limite de uso: retomar por `SendMessage` após o reset.

## 4. Verificado (LOOP-001 passo 4 e gates)
Categorias mais recorrentes: **C07** citação/âncora (34) · **C02** ambiguidade (20) · **C01** contradição interna (21). Lacunas de prevenção abertas: C99, C01, C06, C03, C10. Retrospectivas SPEC-006/007/020/048 FEITAS; propostas P1–P6 aprovadas, **P7–P9 pendentes de Andraus** (`RETROSPECTIVAS.md`). Lição do Orquestrador: ordem de serviço tira decisões só do ROADMAP; não rodar `git stash` com suíte em segundo plano.

## 5. Próximo passo único
(a) ~~Mesclar o PR #133~~ — FEITO; PRs #134–#136 também mesclados. Próxima rodada real de revisão: usar `delta_pacote.py` e conferir se o Revisor declara `MODO:`/`SHA256-ALVO:` (seção 2-ter do ledger mede). (b) Passos à parte pendentes: erratum **F2** da SPEC-020 (junto da SPEC-048); errata da **SPEC-007** (calibração F1, `valid_from` na chave natural da relação, submissão parcial de selo, texto de (ix)/EC-KFH-004 (ii)); atualização aditiva de **CATALOGO/RMR-001 (BL-017)**; **CONFLICT-MAP** (COL-EXP-05, entrada SPEC-020); etapa futura de **revisão das Specs pretéritas** (intenção de Andraus, sem ordem/escopo). (c) **Abrir SPEC-049** (WikiRAG Reading View; Dossiê próprio — `--retro-check` já liberado). (d) Antes de qualquer BUILD: mecanismo de assinatura (DHR-SPEC007-007) e primeiras liberações assinadas. (e) Livro Q7c: decidido (DHR-SPEC007-006); falta o ato por fonte na construção. **Seguem abertas (ROADMAP):** J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001, WORKFLOW-SOT-001 (WF-D03); mais CKG-STRUCT-ORIGIN-001 e produtor/gatilho de promoção.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-DIMENSIONAMENTO-001`, `DHR-RETRO-001`, `DHR-SPEC006-005`, `DHR-SPEC020-002`, `DHR-REAPONT-001`, `DHR-ROTEAMENTO-007`, `DHR-DOCSYNC-003`, `DHR-MERGE-001`, `DHR-SPEC048-002`, `DHR-SPEC007-005`, `DHR-LOOP-001`. Decisões abertas/fechadas: ler o `ROADMAP.md`.

## 7. Becos sem saída
Dar Bash ao Revisor; refazer SPEC-006/020; tratar decisão do `AGENTS.md` como mais atual que o ROADMAP; chamar Especificador/Revisor sem `model`+`CLASSE-TAREFA` (o hook nega); re-apontar recuperação de EXPERIÊNCIA à SPEC-048 (endereço é SPEC-009/017, indicativo); editar baseline fora de erratum homologado; mesclar sem ordem de Andraus.

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas (só por erratum), `ROADMAP.md`, `atomic-spec.md`, `AGENTS.md`, `.claude/agents/*`, `CONFLICT-MAP`, `GATE-MANIFEST.sha256` e scripts do CODEOWNERS.

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` (2917341) ou posterior; se posterior, ler o diff; `git fetch origin main`
- [ ] PRs abertos; se o ramo `ccr-3a6df80c-nej9ne` já foi mesclado, reiniciá-lo de `origin/main`
- [ ] `gate_manifest.py --check`, `check_refs`, `check_doc_sync`, `check_handoff`, `check_rpsa`, `check_coesao`, `build_map --check`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/015/017/035 em espera, sem promoção)
- [ ] Suíte: `python -m unittest discover -s tests` (367) e `node tests/test-ask-guard.js`
- [ ] ROADMAP: linhas "Decisões abertas ativas"/"Decisões FECHADAS"; versão vigente de `WORKFLOW.md`

## 10. Aguardando Andraus
**Só de Andraus:** propostas P7–P9 das retrospectivas · auditoria de higiene (H1–H8, M1–M8; ver relatório) · check determinístico do dimensionamento (`validate_spec_sot.py` + MECANISMOS.json) e recalibração dos tetos após 4–5 Specs medidas · erratum F2 da SPEC-020, errata da SPEC-007, CATALOGO/RMR-001 (BL-017) e CONFLICT-MAP · revisão futura das Specs pretéritas · abertura da SPEC-049 · mecanismo de assinatura (BUILD) · demais decisões abertas do ROADMAP (J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03) · destino do Auditor Externo (PAUSADO), D-PCC-3/4/5.

## 11. Ponteiros
Atas em `governance/` (nome começa pelo ID): DHR-RETRO-001, DHR-REAPONT-001, DHR-SPEC020-002, DHR-SPEC006-005, DHR-ROTEAMENTO-007, DHR-DOCSYNC-003, DHR-MERGE-001 · erratas: `governance/ERRATUM-REAPONT-001*`, `governance/ERRATUM-SPEC020-002*`, `specs/features/SPEC-006/errata-v1.13.md` · pareceres/fichas em `governance/propostas/SPEC-006/`, `governance/propostas/SPEC-020/`, `governance/propostas/REAPONT/` · `governance/aprendizado/` · `governance/MECANISMOS.json` · `scripts/roteador_modelos.py`, `scripts/aplicar_ficha_m.py`, `scripts/merge_ready.py`, `scripts/andraus-ask-guard.js` · `docs/handoffs/` (HO-2026-10-31-100) · `docs/mapa/MAPA-PROJETO.md`
