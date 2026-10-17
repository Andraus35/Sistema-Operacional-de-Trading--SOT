# DHR-PCC-001 — Ata — Fase 1 do PCC-001: continuidade de contexto entre sessões do Orquestrador

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Fase 1 AUTORIZADA por Andraus** (chat, 2026-10-17: *"aprovado, siga com a Fase 1"*, após apresentação do PCC-001 com as decisões D-PCC-1..5 e recomendações). Fases 2 e 3 **não** autorizadas. Não fecha nem abre decisão aberta. |
| Compatibilidade | Aditiva (INV-07). Reversível por `git revert` (remove `HANDOFF.md`, §11 do `AGENTS.md` e a linha do whitelist). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Altera `AGENTS.md` (nova §11) e o whitelist da raiz; nenhum texto de arquivo de agente (`.claude/agents/*.md`) é alterado. |

## 1. Decisão `[FATO]`
Andraus aprovou a Fase 1 do `governance/PCC-001_Plano_Continuidade_Contexto_Build_PROPOSTA.md`. Interpretação registrada (o Orquestrador adotou as recomendações do plano; Andraus pode corrigir):
- **D-PCC-1 = A:** `HANDOFF.md` na raiz (emenda do whitelist HOD-001 §6b.1; precedente `WORKFLOW.md`).
- **D-PCC-2 = sim:** §11 em `AGENTS.md` e a emenda do whitelist, nesta ata.
- **D-PCC-3, D-PCC-4, D-PCC-5: NÃO decididas** (Fases 2–3; D-PCC-5 muda `.claude/agents/revisor.md`, só por Andraus).

## 2. Efeitos (Fase 1 — cumprimento manual)
1. `HANDOFF.md` criado na raiz (HO-2026-10-17-01, cadeia inicia; contrato de campos PCC-001 §3.2).
2. `docs/handoffs/` criado (arquivo L4, monotônico).
3. `AGENTS.md`: linha no mapa do repositório + **§11 Continuidade entre sessões**.
4. HOD-001 §6b.1: `HANDOFF.md` no whitelist de caminho-quente.
5. **Sem** scripts, hooks, CI ou mudança de agentes (Fase 2).

## 3. Limites `[FATO]`
O handoff é dado de estado do Orquestrador: não registra homologação, não fecha decisão aberta, não concede permissão. Mudanças em `AGENTS.md` seguem só por decisão expressa de Andraus (AGENTS.md §10) — aqui citada.

## 4. Gatilho da Fase 2 (proposto no PCC-001 §7)
Fase 1 usada por ≥3 sessões reais sem fricção grave; depois, proposta específica com D-PCC-4/5.

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.**

## 6. Registro
- [x] Esta ata · [x] `AGENTS.md` §11 · [x] HOD-001 §6b.1 · [x] `HANDOFF.md` · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] RPSA automático (sem escopo de agente)

## 7. Errata (2026-10-17, ordem de Andraus no chat: "corrige a errata na ata DHR-PCC-001")
Aditiva (INV-07): o texto acima fica como está; esta seção o corrige.
- **§5 está incorreto em um item:** lista **SPEC-038-DATASRC-001** entre as decisões ABERTAS. Ela está **DECIDIDA neste recorte** (Andraus, 2026-10-03, DHR-DEC-004: TradingView como uma das fontes via adapter, risco ToS assumido; provedor de dados de máquina só após Discovery do MASTER, BL-033). Fonte: `ROADMAP.md`, linha "Decisões FECHADAS", e `AGENTS.md` §7.
- **Causa:** a lista do §5 foi copiada da ata `DHR-ASSINATURA-001` §5 em vez de apontar para o ROADMAP. A lista não deve ser tomada como fonte de verdade.
- **Regra:** o estado das decisões abertas/fechadas é o do `ROADMAP.md` (prevalece em divergência); este ato **não** fecha nem abre nenhuma decisão. As demais decisões do §5 não foram reavaliadas aqui — consulte o ROADMAP.
- **Nota:** a `DHR-ASSINATURA-001` §5 contém a mesma lista; não foi alterada por esta errata (fora do escopo pedido).

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno.*
