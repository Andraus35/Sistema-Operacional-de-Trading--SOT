# DHR-BACKLOG-ABERTURA-001 — Ata — Backlog vinculado por regra à abertura de cada Spec (determinístico)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-13 |
| Status | **Decisão de Andraus registrada no chat** (citada abaixo). Entra no repositório por PR; não fecha nem abre decisão aberta. |
| Compatibilidade | Aditiva (INV-07). Não retroage: Spec já homologada não é alcançada. Reversível por `git revert`. |
| RPSA-escopo | sim |
| RPSA-sync | propagado |
| RPSA-motivo | Acrescenta um passo à abertura de Spec em `especificador.md` (rodar `backlog_triggers.py --abertura`; declarar Disposição no Plan) e um item de auditoria em `revisor.md` (Passo 4-bis); carimbos alinhados. |

## 1. Origem `[FATO]`
Andraus, em chat (2026-10-12/13), ao ver BL-003/BL-011/BL-010/BL-029 tratados como "só registra, Andraus decide" na SPEC-006: *"quero que backlogs sejam abertos juntos com sua respectiva spec seja em todo ou em parte no que couber. não depender de decisão de andraus promover automaticamente na abertura para ser objeto de especificação. garantir isso deterministicamente"*. Diagnóstico prévio: a verificação do backlog (passo 11-bis) só ocorria na **homologação**; os gatilhos `spec:… em redação` disparavam na abertura e ficavam sem tratamento até uma promoção manual.

## 2. Regra `[DECISÃO DE ANDRAUS]`
1. **Vinculação por regra.** Todo item não encerrado do RMR-001 cujo gatilho tem uma alternativa `spec:SPEC-nnn em redação` fica **vinculado à SPEC-nnn desde a abertura**, sem depender de promoção de Andraus, para ser objeto de especificação **em todo ou em parte, no que couber**.
2. **Vincular ≠ promover ≠ absorver.** O Estado no painel não muda; `ATIVADO`, `Absorvido` e `Descartado` seguem homologados por Andraus (RMR-001 §5). Gatilhos `milestone:`/`evento:`/`hygiene:`/`decisao:` não vinculam por abertura.
3. **Disposição obrigatória no Plan.** Em cada BL vinculado: `Disposição: INCORPORADO | PARCIAL | REFERÊNCIA | FORA` + motivo. O Revisor audita o motivo.
4. **Garantia determinística:** `python scripts/backlog_triggers.py --abertura SPEC-nnn` (lista); gate **`[STRUCT-13]`** em `validate_spec_sot.py` (fail-closed; também via `revisor_gate`); hooks Stop/SubagentStop/SessionStart avisam (informativo); CI roda os testes (`tests/test_backlog_abertura.py`).
5. **Correção de detector (mesmo ato):** "ABERTURA HOMOLOGADA" deixa de ser lida como Spec homologada em `backlog_triggers.py` (antes, `spec:SPEC-006 homologada` aparecia TRUE por engano).

## 3. Efeito imediato `[FATO]`
SPEC-006 (em redação): BL-003 e BL-011 vinculados — ambos `Disposição: PARCIAL` no Plan v1.6 (BL-011 com pendência explícita: reconciliação da fila EXP-SPEC-001..053 e dos tratamentos R-01..R-07 ainda não conferida contra os BASpecs). BL-010 (SPEC-007) e BL-029 (SPEC-014/018/045) não são vinculados à SPEC-006 pela regra. BL-035 vincula-se à SPEC-007.

## 4. Permanecem ABERTAS (CONS-01)
H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001, CKG-STRUCT-ORIGIN-001. Nada foi fechado.
