# DHR-ASK-002 — Ata — Regra de fim de turno do Orquestrador (decisão de Andraus por AskUserQuestion)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — a ratificar por Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **PROPOSTA — vira vigente só com o merge de Andraus.** Formaliza uma regra que **já opera** por hook desde 2026-10-11 e que não tinha ata (o script `scripts/andraus-ask-guard.js` cita "DHR-ASK-002", mas o arquivo não existia). Não fecha nem abre decisão aberta. |
| Compatibilidade | Aditiva (INV-07). Não altera hook, script, `AGENTS.md` nem agentes. Reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Apenas registra por ata uma regra já aplicada por hook; nenhum arquivo de agente nem checklist é alterado. |

## 1. Regra `[FATO: comportamento atual dos hooks]`
1. Quando o Especificador SOT ou o Revisor SOT **entregam** algo, o Orquestrador não encerra o turno sem antes perguntar a Andraus por `AskUserQuestion` (hook `Stop`: `scripts/andraus-ask-guard.js`; marcador: `scripts/andraus-ask-mark.js`; lembrete: `scripts/andraus-ask-reminder.js`).
2. Pergunta, oferta ou pedido de decisão escrita só em **texto** no fim do turno é bloqueada uma vez por fala; a decisão de Andraus vai por `AskUserQuestion`, com a recomendação em primeiro lugar e a opção "adiar" quando tocar decisão aberta.
3. Natureza: **Detector/lembrete (ENF-03)**, fail-open, nunca decide nem homologa; pergunta retórica sem decisão de Andraus é reescrita sem pergunta.

## 2. Limites `[FATO]`
Ids de agentes lançados antes de compactação ou retomada da sessão não são reconhecidos. O histórico é assíncrono (por isso o marcador). Não cobre sessão sem hooks.

## 3. Permanecem ABERTAS (CONS-01)
Nenhuma decisão aberta é fechada ou aberta por este ato; o estado é o do `ROADMAP.md`.

## 4. Registro
- [x] Esta ata (PROPOSTA) · [ ] merge de Andraus · [ ] `CATALOGO-OFICIAL.md` (governance normativo — só após decisão de Andraus)

---

**Andraus** — *a ratificar por merge; proposta do Orquestrador interno, 2026-10-17.*
