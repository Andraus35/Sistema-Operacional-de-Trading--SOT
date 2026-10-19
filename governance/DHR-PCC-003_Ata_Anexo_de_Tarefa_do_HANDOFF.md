# DHR-PCC-003 — Ata — Anexo de tarefa: extensão do HANDOFF para trabalho entre sessões (sem duplicidade)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT / Controlador |
| Ref | `PCC-001` (§1 "não criar memória paralela"; §3 o `HANDOFF.md`), `DHR-PCC-001` (Fase 1), `DHR-PCC-002` (Fase 2: detector e hooks), exemplo `governance/propostas/SPEC-007/BRIEFING-PLAN-SPEC007-2026-10-19.md` |
| Data | 2026-10-19 |
| Status | **DECISÃO DE ANDRAUS REGISTRADA** (chat, 2026-10-19, AskUserQuestion: "Adotar como extensão do HANDOFF" + "Informativo agora; promover depois pela regra D-PCC-4"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **Autoriza expressamente** a linha de `AGENTS.md` §11 (arquivo protegido). Não fecha D-PCC-3, D-PCC-4 nem D-PCC-5. |
| Compatibilidade | Aditiva (INV-07). Reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Acrescenta checagens informativas ao detector do handoff e um item de protocolo em AGENTS §11; nenhum arquivo de agente, checklist nem método é alterado. |

## 1. Problema `[FATO]`
Tarefas grandes entre sessões (ex.: o Plan de uma Spec CRITICAL) precisam de um **pacote de entrada** que não cabe nas 150 linhas do `HANDOFF.md`. Na prática surgiram **três formatos informais sem regra** (passagem de sessão `HANDOFF-SPEC006-2026-10-17.md`, brief de decisão `BRIEFING-DECISAO-I-001.md` e o briefing do Plan da SPEC-007), com risco de (a) **duplicar** conteúdo que já vive em ata/ROADMAP/handoff e divergir, e (b) **ambiguidade** sobre o que ler primeiro. O `PCC-001` já proíbe memória paralela: o handoff **aponta**, não copia.

## 2. Decisão `[FATO]`
O pacote de entrada por tarefa passa a ser o **anexo de tarefa**, extensão do `HANDOFF.md` (continua sendo o **único** ponto de entrada):
1. **Um só ativo.** No máximo um anexo `ATIVO` por vez, citado pelo campo `anexo:` do frontmatter do handoff (`anexo: null` quando não há). Sem citação, não vale.
2. **Só ponteiros.** Decisões, estado e regras entram por **ID e linha**, nunca por cópia (ata/ROADMAP/CATALOGO prevalecem). Conteúdo único permitido: entradas a ler, obrigações já decididas **apontadas**, receita operacional, custo. Máx. **80 linhas**.
3. **Cabeçalho padrão** (frontmatter): `tipo: anexo-de-tarefa` · `anexo_id` · `tarefa` · `serve_handoff` · `base_commit` · `status: ATIVO|CONSUMIDO`.
4. **Ciclo de vida:** `ATIVO` enquanto a tarefa não termina; ao terminar, `status: CONSUMIDO`, o arquivo é **movido (não apagado — INV-07)** para `docs/handoffs/anexos/` e o handoff passa a `anexo: null`.
5. **Local:** enquanto ativo, junto do trabalho (`governance/propostas/<Spec>/`); arquivado em `docs/handoffs/anexos/`. O **brief de decisão** (`BRIEFING-DECISAO-*`, para Andraus decidir) é de outro tipo e **não** é anexo de tarefa; as passagens de sessão antigas ficam como registro histórico.
6. **Informativo (Detector ≠ Gate, ENF-03).** `scripts/check_handoff.py` ganha HO-11 (anexo citado inexistente / cabeçalho incompleto / status inválido — ERRO), HO-12 (órfão, mais de um ATIVO, CONSUMIDO ainda citado — WARN), HO-13 (> 80 linhas — WARN), HO-14 (DHR sem ata, decisão aberta tratada como fechada, segredo — ERRO), HO-15 (linha longa copiada do HANDOFF/ROADMAP/atas — WARN). O hook `SessionStart` mostra o cabeçalho do anexo ativo logo após o do handoff. CI e hooks seguem **não-bloqueantes**; **promover a bloqueante é a D-PCC-4 (aberta, só de Andraus)**.
7. **Escritor único:** só o Orquestrador escreve o anexo (como o handoff); o Revisor segue somente leitura; o Especificador recebe o anexo **por caminho** no prompt.

## 3. O que muda `[FATO]`
`scripts/check_handoff.py` · `scripts/handoff-hook.js` · testes (`tests/test_check_handoff.py`, `tests/test-handoff-hook.js`) · `AGENTS.md` §11 (uma linha) · `PCC-001` §3.5 · `governance/MECANISMOS.json` (`det.check-handoff`, `hook.handoff-hook`) · o briefing do Plan da SPEC-007 reescrito como anexo (só ponteiros) · nota histórica em `HANDOFF-SPEC006-2026-10-17.md`.

## 4. Limites honestos `[FATO]`
O detector só vê **forma** (existência, cabeçalho, tamanho, cópia literal de linhas longas); não prova que o anexo está **certo** — quem confere a fonte é o Orquestrador/Revisor. Cópia parafraseada não é detectada. Com o registro de mecanismos VIGENTE (`DHR-COESAO-005`), esta mudança atualiza `MECANISMOS.json` no mesmo PR.

## 5. Permanecem ABERTAS (CONS-01)
D-PCC-3 (BUILD-LEDGER) · D-PCC-4 (promoção a bloqueante) · D-PCC-5 (item de handoff no Passo 0 do Revisor) · G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001. **Nenhuma fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] detector + hook + testes · [x] `AGENTS.md` §11 · [x] `PCC-001` §3.5 · [x] `MECANISMOS.json` · [x] anexo da SPEC-007 reescrito · [ ] merge (assinatura)

---

**Andraus** — *decisão em chat, 2026-10-19; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
