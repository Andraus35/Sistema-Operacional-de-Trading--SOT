---
handoff_id: HO-2026-10-31-130
previous: HO-2026-10-31-129
data: 2026-10-31
branch: ccr-599f6762-60qbvg
base_commit: f4ff6c4
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece. *(Reescrito limpo em HO-129 a partir de duas sessões em paralelo e atualizado em HO-130 após o merge do #149; o texto anterior está em `docs/handoffs/HO-2026-10-31-128.md` e as cadeias paralelas em `docs/handoffs/ramo-*/` — nada perdido, INV-07.)*

## 1. Frente atual
**Nenhuma Spec em redação.** Último fechamento: **SPEC-049** (abertura `DHR-SPEC049-001` + Plan v1.2 BASELINE `DHR-SPEC049-002`, sem BUILD). **Retrospectiva da SPEC-049 FEITA** em 2026-10-31 (`DHR-RETRO-002`; `loop_ledger.py --retro-check SPEC-049` = FEITA). Abrir outra Spec continua **só por ordem de Andraus**.

**Nenhum PR de trabalho aberto além do que traz este próprio handoff (higiene do handoff pós-merge).** O PR **#149** foi **MESCLADO** na `main` (`f4ff6c4`, a comando de Andraus em 2026-10-31): retrospectiva da SPEC-049 FEITA; **P7** `scripts/fato_locais.py` (detector informativo: tabela fato→locais, `--conferir`, `--base`; 20 testes; `MECANISMOS.json` + CI); **P8** emenda ao `.claude/agents/revisor.md` §3 (canal `GATE-D:` do Orquestrador em nuvem; `DHR-AGENTS-P8-001`; resultado negativo nunca se descarta por formato). Para trabalhar: `git checkout -B <ramo> origin/main`.

**Sessão de 2026-10-31 (auditoria de burocracia e higiene; ordens de Andraus no chat; já na `main` via #147 e #148):** `AGENTS.md` 29.427→**18.803 B** (§7: `DHR-AGENTS-SEC7-001`; §2/§5/§8/§9/§12: `DHR-AGENTS-CORTES-001`; texto removido em `docs/_legacy/AGENTS-*-arquivo-morto-*`, prova de conservação `governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/`); `check_refs.py` sem falsos positivos (selo do gate regravado); `.gitattributes`; `docs/UPGRADES`→`_legacy`; status de 3 atas COE-11 e de `EUA-E20`/`EUA-E23`/`PCC-001`, nota em `ERRATUM-SPEC019-001` (`DHR-HIGIENE-001/002`). **Outra sessão:** `[STRUCT-14]` (check de Classe/Mecanismo em `validate_spec_sot.py`; `DHR-MECH-GATE-001`; #150, na `main`).

## 2. Estado (fatos conferidos em 2026-10-31)
- `main` em `858315d`. Suíte: **424 testes** OK; `npm test` 11 schemas; `check_refs` ERRO=0; `check_doc_sync` ERRO=0 (1 WARN antigo: `SPEC-007/plan.md:2650` cita versão velha do `WORKFLOW.md`; baseline, só por erratum); `check_coesao` ERRO=0 (2 INFO: configs-marcador da raiz, mantidas de propósito); `gate_manifest`, `check_rpsa`, `build_map --check`, `loop_ledger --check` verdes.
- **Evidência do corte do AGENTS.md** (`.../EQUIVALENCIA/TESTE-AB-AGENTS/`): achabilidade de fatos 16/17, 17/17 (Haiku); cenários de decisão A×E 11/12 vs 12/12 — o texto SUPERADO que o original mantinha no §12 fez o modelo errar a S3. **Não feito (declarado na ata):** teste do Especificador/Revisor completos (o harness injeta o AGENTS.md atual em qualquer subagente) e 2ª checagem da trilha C em outro modelo; Andraus aceitou a evidência atual. Reversão: git + arquivos mortos.
- **Mecanismos novos:** `GATE-D` (P8, em #149), `fato_locais.py` (P7, em #149), `STRUCT-14`, `equiv_conservacao.py` (utilitário de proposta, não instalado). Telemetria de tokens (`scripts/telemetria_tokens.py`, BL-036/037; custo **equivalente API, não cobrança**). R-AC7 (hook exige `model` + `CLASSE-TAREFA`; **R-GATE barra Haiku em tarefa de gate/revisão — usar Sonnet**).
- **Convenção de handoff por ramo:** sessões paralelas repetiram números (HO-110..127). A cadeia de cada ramo que colide fica em `docs/handoffs/ramo-<ramo>/`; o da `main` fica no lugar. `check_handoff` HO-04 pode acusar a união das cadeias: aviso esperado, informativo.
- **Custo medido da SPEC-049 (tokens de subagentes):** abertura 906.237 + Plan 1.389.735 ≈ **2,30 M**; delta custou 20–24% menos que a R1 integral do Plan (n pequeno).

## 3. Lições (fluxo que funcionou — repetir)
Ordem classe O ao Especificador (`model: opus` + `CLASSE-TAREFA: O` + `PARECER:`/`FICHA:`) → gates do Orquestrador → commit/push → `delta_pacote.py` (rodada ≥2) → Revisor (`CLASSE-TAREFA` + `ALVO:` + `SHA256-ALVO:` + `MODO:`; em nuvem o gate vai em `GATE-D:` do pedido — emenda `DHR-AGENTS-P8-001`, já em vigor) → parecer em `governance/propostas/<X>/` → `aplicar_ficha_m.py` → `loop_ledger.py` → AskUserQuestion → ata + `check_rpsa.py --register` → gates → PR → mesclar só ao comando de Andraus. **Desta sessão:** (1) **ler `MECANISMOS.json` e o TÍTULO do arquivo antes de chamá-lo de órfão ou "sem status"** (errei duas vezes); (2) **atacar o próprio patch** (teste adversarial achou regressão no `check_refs` e a falha "REPROVADO_D descartado por formato" no P8); (3) corte de texto normativo: conservação linha a linha **+ suíte + `check_invariants`** (um detector usava o §7 como fonte); (4) gabarito de teste: registrar antes, e declarar qualquer correção pós-hoc; (5) em mutação, rodar com `python -B` e limpar `__pycache__`; (6) `git fetch origin main` antes de abrir PR — duas vezes a `main` andou durante o trabalho.

## 4. Verificado (LOOP-001 passo 4)
Categorias mais recorrentes: **C07** (39) · **C01** (28) · **C02** (24); SPEC-049 (34 achados): C01 7, C07 5, C05 5, C06 5. Lacunas de prevenção abertas: C99, C01, C06, C03, C10. Retrospectivas SPEC-006/007/020/048/049 FEITAS; P1–P9 decididas (P7 e P8 aplicadas via #149; P9 atendida pelo corte do §7); **P10–P12 pendentes de Andraus**.

## 5. Próximo passo único
**Perguntar a Andraus (AskUserQuestion, com recomendação):** (1) P10–P12; (2) a próxima frente (§10). Nada disso se decide por ele. Quando ele mandar mesclar qualquer PR: esperar o CI verde, mesclar com merge commit travando o `expectedHeadSha`, reiniciar o ramo de `origin/main`.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-RETRO-002`, `DHR-AGENTS-P8-001`, `DHR-AGENTS-CORTES-001`, `DHR-AGENTS-SEC7-001`, `DHR-HIGIENE-001`, `DHR-HIGIENE-002`, `DHR-MECH-GATE-001`, `DHR-SPEC049-002`, `DHR-SPEC049-001`, `DHR-TELEMETRIA-CUSTO-001`, `DHR-CHECKS-INFO-001`, `DHR-DELTA-HASH-001`, `DHR-DIMENSIONAMENTO-001`, `DHR-RETRO-001`, `DHR-ROTEAMENTO-007`, `DHR-MERGE-001`, `DHR-LOOP-001`. Decisões abertas/fechadas: ler o `ROADMAP.md` (linhas "Decisões abertas ativas"/"Decisões FECHADAS").

## 7. Becos sem saída
Dar Bash ao Revisor; refazer SPEC-006/020/048/049; tratar o `AGENTS.md` como mais atual que o ROADMAP; chamar Especificador/Revisor sem `model`+`CLASSE-TAREFA`; rodar tarefa de gate/revisão em Haiku (o roteador nega — não contornar); editar baseline fora de erratum homologado; mesclar sem ordem de Andraus; **abrir outra Spec sem ordem dele**; numerar handoff sem ler a `main`; classificar arquivo como órfão sem ler `MECANISMOS.json`; arquivar as configs-marcador da raiz (`.eslintrc`/`.prettierrc`: o `harness-score` as usa, `DHR-COESAO-002`); cortar leitura estratégica por economia (4Es: Economicidade nunca acima de Eficácia).

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas (só por erratum), `ROADMAP.md`, `atomic-spec.md`, `AGENTS.md`, `.claude/agents/*`, `CONFLICT-MAP`, `GATE-MANIFEST.sha256` e scripts do CODEOWNERS — só por ordem expressa de Andraus.

## 9. Reverificar ao vivo
- [ ] `git fetch origin main`; `git log -1` == `base_commit` (f4ff6c4) ou posterior; se posterior, ler o diff; PRs abertos (esperado: nenhum de trabalho); se o ramo foi mesclado, `git checkout -B <ramo> origin/main`
- [ ] `gate_manifest.py --check`, `check_refs`, `check_doc_sync`, `check_handoff`, `check_rpsa`, `check_coesao`, `build_map --check`, `loop_ledger.py --check`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/015/017/035 disparados sem registro; sem promoção sem Andraus)
- [ ] Suíte: `python -m unittest discover -s tests` (**424**), `node tests/test-hooks.js`, `node tests/test-ask-guard.js`, `npm test` (11 schemas)
- [ ] ROADMAP: decisões abertas/fechadas; versão vigente de `WORKFLOW.md`
- *Aviso esperado:* `check_handoff` HO-04 (união das cadeias de handoff); informativo.

## 10. Aguardando Andraus
1. **P10** rodar o experimento da regra de parada no PRÓXIMO Plan (`.../MELHORIAS-PROCESSO/PROPOSTA-EXPERIMENTO-REGRA-DE-PARADA-2026-10-31.md`; baseline 2,30 M tokens) · **P11** tornar regra o handoff por ramo (`docs/handoffs/ramo-*`) e ensinar o `check_handoff` · **P12** critério objetivo para "rodada real". 2. **Próxima frente** (nenhuma escolhida): erratum F2 da SPEC-020, errata da SPEC-007, CATALOGO/RMR-001 (BL-017), CONFLICT-MAP, **ou** abrir outra Spec. 3. **Itens da auditoria de burocracia**, cada um só por ordem dele (relatório `.../AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md`): mecanismos em 3 camadas (A6), decisão em lote (A3), HANDOFF por delta/tag e RPSA derivado do git (A2), abertura+Plan em ciclo único p/ Specs LOW/MEDIUM (A4), corte das linhas 34/37 do ROADMAP (exige julgamento), roteamento por modelo fixo (A8). 4. **Higiene restante:** nomes de `reference/`, subpastas de `governance/`, confirmar o status do `ERRATUM-SPEC019-001`. 5. Antes de qualquer BUILD: mecanismo de assinatura (DHR-SPEC007-007). 6. Decisões abertas do ROADMAP; destino do Auditor Externo (PAUSADO); quem aprova o 1º `render_profile` v1 (decidir na construção).

## 11. Ponteiros
`governance/propostas/MELHORIAS-PROCESSO/` (auditoria de burocracia, propostas, `EQUIVALENCIA/` com prova de conservação e testes A/B, `PATCH-*`) · `governance/aprendizado/` (LEDGER, CAUSAS-PREVENCAO, RETROSPECTIVAS) · `governance/propostas/SPEC-049/` · `governance/MECANISMOS.json` · `.harness-eval/runs/2026-10-31-agents/` (harness-eval do AGENTS.md) · `docs/_legacy/AGENTS-*` (texto cortado) · `docs/handoffs/` e `docs/handoffs/ramo-*/` · `docs/mapa/MAPA-PROJETO.md` (índice gerado) · atas em `governance/` (nome começa pelo ID).
