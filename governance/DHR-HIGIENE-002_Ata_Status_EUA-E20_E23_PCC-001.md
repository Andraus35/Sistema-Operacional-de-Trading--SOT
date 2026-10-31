# DHR-HIGIENE-002 — Ata de Decisão — Status de registros desatualizados (EUA-E20, EUA-E23, PCC-001)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-31): "Resolver pendências" · `AGENTS.md` §10 · `DHR-HIGIENE-001` · `DHR-EUA-E20` · `DHR-EUA-E23` · `DHR-PCC-001/002/003` · `governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` (B4, §6.1) |
| Data | 2026-10-31 |
| Status | **APLICADA por ordem de Andraus** (AGENTS.md §10). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Edita só o campo Status de 3 registros de governança; não toca agentes de construção, método nem AGENTS.md. |

## 1. Escopo `[FATO]`
Atualizar o campo Status de 3 registros cujo texto interno ainda dizia "PROPOSTA", embora haja ata de decisão de Andraus: `EUA-E20_Fase_RISK_Slots_PROPOSTA.md` (ata `DHR-EUA-E20`, 2026-10-01), `EUA-E23_Manager_Unificado_SPEC008_SPEC015_PROPOSTA.md` (ata `DHR-EUA-E23`, 2026-10-01) e `PCC-001_Plano_Continuidade_Contexto_Build_PROPOSTA.md` (Fases 1 e 2 e anexo autorizados por `DHR-PCC-001/002/003`; **Fase 3 segue PROPOSTA**). O **texto anterior ficou preservado** em cada Status (INV-07). Nenhum nome de arquivo foi alterado.

## 2. Verificação dos demais registros apontados `[FATO]`
Conferidos um a um (título e corpo, não só a tabela de Status): **`EMENDA-SPEC001-001` está HOMOLOGADA** (banner no título: "HOMOLOGADO — aplicado em 2026-10-05, DHR-AUDIT-SPEC001-001"; CATALOGO e ata confirmam) — **nada a mudar**; **`REAUDITORIA-SPEC002-001`, `MANIFESTO-DE-ESCOPO` e `PROTOCOLO-AUDITOR-EXTERNO` já declaram explicitamente "PROPOSTA — NÃO HOMOLOGADO"** e as atas `DHR-AUDITOR-EXTERNO-001..004` não os citam — status correto, **nada a mudar**. Só o **`ERRATUM-SPEC019-001`** tem status ambíguo ("PROPOSTA — nada aplicado", sem ata nem CATALOGO, citado por outros errata só como padrão): recebeu **nota neutra "status NÃO CONFIRMADO"**, sem afirmar homologação nem descarte (ordem de Andraus no chat: "marcar como status não confirmado"; aplicada só onde o status não está estabelecido). Os demais ~25 já declaram o status correto por dentro. *Correção desta ata:* a versão anterior listava os cinco como "sem evidência" porque a varredura olhou só a linha de tabela; a releitura dos títulos mostrou o contrário para quatro deles.

## 3. Permanecem ABERTAS (CONS-01)
O estado vem do `ROADMAP.md`. Nenhuma decisão foi fechada ou aberta por esta ata.

## 4. Registro
- [x] Esta ata · [x] texto anterior preservado nos 3 Status · [ ] merge (assinatura de Andraus)
