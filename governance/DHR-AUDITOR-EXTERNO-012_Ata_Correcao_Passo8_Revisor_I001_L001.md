# DHR-AUDITOR-EXTERNO-012 — Ata — Correção do Passo 8 do `.claude/agents/revisor.md` (I-001 e L-001 já fechadas)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-11 |
| Status | **Correção autorizada por Andraus (chat, 2026-10-11).** O merge desta ata e do arquivo alterado é a ratificação. Não fecha nem abre decisão: apenas alinha o texto do Revisor a decisões que Andraus já fechou. |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert` do commit de aplicação. |
| RPSA-escopo | sim |
| RPSA-sync | propagado |
| RPSA-motivo | Remove I-001 e L-001 da lista de bloqueadores abertos do Passo 8 do revisor.md, pois ambas ja estao FECHADAS; muda o criterio embutido no Revisor para limitar parecer a CONFORME condicional; o Especificador nao e afetado. |

## 1. Achado `[FATO]`
O Passo 8 do `.claude/agents/revisor.md` listava `I-001` e `L-001` entre os "bloqueadores abertos" que limitam o parecer a CONFORME condicional. Ambas estão **FECHADAS** (fonte: `AGENTS.md` §7 e `ROADMAP.md`, "Decisões FECHADAS"): **I-001** — Andraus, 2026-09-28, DHR-I001-001 (Skills = híbrido por Classe, Opção C); **L-001** — homologação da SPEC-019, 2026-09-22, DHR-SPEC019-001 (dimensão spec-time; a governança de runtime pertence à SPEC-018/K-001, que segue aberta). Achado do Revisor (auditoria de pendências, 2026-10-11), pré-existente aos PRs #86–#90.

## 2. O que foi alterado `[FATO]`
Uma única linha (Passo 8): `(J-001, G-001, H-001, I-001, K-001, L-001, C-001, M-001, N-001)` → `(J-001, G-001, H-001, K-001, C-001, M-001, N-001)`. Nenhum outro trecho do arquivo foi tocado. K-001 permanece na lista (aberta).

## 3. Reversão `[PROPOSTA]`
`git revert <commit de aplicação>`. O RPSA realinha o carimbo pela ata de reversão.

## 4. Classificação RPSA desta ata
Declarada no cabeçalho (`sim` / `propagado`): altera o checklist embutido no Revisor. Após o merge, `rpsa_auto` registra a classificação e alinha os carimbos `sincronizado-até` de `revisor.md` e `especificador.md`.

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato** (I-001 e L-001 já estavam fechadas).

## 6. Registro
- [x] Esta ata · [x] `.claude/agents/revisor.md` (uma linha) · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] merge (ratificação) · [ ] RPSA automático

---

**Andraus** — *correção autorizada em chat, 2026-10-11; registro feito pelo Orquestrador interno a pedido de Andraus. Assinatura = merge desta ata.*
