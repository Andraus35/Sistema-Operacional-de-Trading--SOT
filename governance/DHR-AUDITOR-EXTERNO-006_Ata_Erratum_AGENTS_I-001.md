# DHR-AUDITOR-EXTERNO-006 — Ata — Erratum do `AGENTS.md` §7 (I-001 já FECHADA) e confirmação da classificação da DHR-RPSA-002

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisões de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-10 |
| Status | **Decisões de Andraus registradas (chat, 2026-10-10)**; o merge desta ata é a ratificação. Não fecha nem abre decisão; não altera checklist, método, regra nem o Revisor. |
| Compatibilidade | n/a (aditiva — INV-07) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Corrige no AGENTS.md a lista de decisoes ativas para refletir o fechamento da I-001 ja registrado (DHR-I001-001); nao altera decisao, checklist, metodo nem regra; agentes leem o ROADMAP. |

## 1. Decisões de Andraus `[FATO: chat, 2026-10-10]`
1. **Autoriza editar o `AGENTS.md` §7** para corrigir o achado **AEX-20261010-005** (Issue #42, P2, drift, procedente): a lista "Ativas" ainda trazia `I-001`, embora ela esteja **FECHADA** desde 2026-09-28 (`DHR-I001-001`; `ROADMAP.md` "Decisões FECHADAS"; `CATALOGO-OFICIAL.md`). Autorização limitada a essa linha de §7.
2. **Classificação RPSA da `DHR-RPSA-002` confirmada** ("classificação ok"): `em_escopo=false`, `sync=fonte-unica`. O caso limítrofe apontado na ata (fluxo do gate RPSA) fica resolvido como **fora de escopo**; o carimbo dos agentes não avança.

## 2. O que mudou `[FATO: texto aplicado]`
Em `AGENTS.md` §7, `I-001` passou de "ativa" a `~~I-001~~ (FECHADA — Andraus, 2026-09-28, DHR-I001-001: Skills = híbrido por Classe, Opção C; o critério de corte exato segue diferido ao Dossiê de abertura da SPEC-025 — fonte: ROADMAP.md "Decisões FECHADAS")`. Nenhuma outra linha do `AGENTS.md` foi alterada. O fechamento **já existia** (Andraus, 2026-09-28); esta ata só alinha o resumo ao registro — **não fecha** decisão nova (CONS-01). O critério de corte da SPEC-025 permanece diferido, não decidido.

## 3. Classificação RPSA desta ata
Declarada no cabeçalho (`nao` / `fonte-unica`): corrige um resumo derivado do ROADMAP; as decisões abertas em si não mudam e os agentes leem o ROADMAP como fonte. Registrada por `scripts/rpsa_auto.py` (primeiro uso do mecanismo da DHR-RPSA-002, ainda sem o workflow ligado).

## 4. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**.

## 5. Registro
- [x] Esta ata · [x] `AGENTS.md` §7 · [x] `rpsa-ledger.json` · [x] `CATALOGO-OFICIAL.md` · [x] mapa

---

**Andraus** — *decisão direta em chat, 2026-10-10; registro feito pelo Orquestrador interno a pedido de Andraus. Assinatura = merge desta ata.*
