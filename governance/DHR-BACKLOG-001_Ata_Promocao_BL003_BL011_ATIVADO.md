# DHR-BACKLOG-001 — Ata — Promoção de BL-003 e BL-011 a ATIVADO (gatilho `spec:SPEC-006 em redação`)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17, AskUserQuestion: "Promover os dois a ATIVADO")**. O merge desta ata por Andraus é a ratificação. Não fecha nem abre decisão aberta (CONS-01). |
| Compatibilidade | Aditiva (INV-07): o estado anterior `Em espera` é preservado riscado na própria linha. Reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Atualiza apenas o estado de dois itens do painel de backlog RMR-001; nenhum arquivo de agente, checklist, metodo nem regra e alterado. |

## 1. Decisão `[FATO]`
O Plan da SPEC-006 (v1.4, candidato, ramo `spec006-plan`) satisfaz o gatilho `spec:SPEC-006 em redação` de **BL-003** (persistência física de hipótese/estado) e **BL-011** (MC-EXP-001, camada de experiência e memória). O detector `backlog_triggers.py` os acusava como "disparados sem registro" (achado de gate). Andraus promove os dois de `Em espera` a **`ATIVADO`**, com encaminhamento ao gate da SPEC-006 (RMR-001 §4/§5). Nada é `Absorvido`; nada é implementado por esta ata.

## 2. Limites `[FATO]`
H-001 (mecanismo físico do KG) e G-001 permanecem ABERTAS; a parte física de BL-003 continua dependendo delas. A reconciliação COL-EXP-05 e R-04..R-06 (BL-011) segue sendo decidida no gate da SPEC-006, não aqui.

## 3. Permanecem ABERTAS (CONS-01)
Nenhuma decisão aberta fechada ou aberta; o estado é o do `ROADMAP.md`.

## 4. Registro
- [x] Esta ata · [x] `backlog/RMR-001_Painel_Backlog.md` (linhas BL-003, BL-011 e nota datada) · [ ] merge de Andraus (ratificação)

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno.*
