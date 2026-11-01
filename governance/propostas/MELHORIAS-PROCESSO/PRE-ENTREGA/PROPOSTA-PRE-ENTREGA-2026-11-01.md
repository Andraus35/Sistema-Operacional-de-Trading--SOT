---
tipo: proposta-pre-testada
status: PROPOSTA (não vigente; nada instalado nem aplicado)
data: 2026-11-01
origem: AUDITORIA-ESPECIFICADOR-PRECHECK-2026-11-01.md (itens P-A e P-F)
---
# P-A + P-F — pré-gate unificado e higiene do especificador.md

Decisões de Andraus (chat, 2026-11-01): começar por P-F(1–5)+P-A; o pré-gate é rodado pelo Orquestrador/hook (o Especificador continua sem Bash); detectores informativos até P-E medir falso alarme; PR sem mesclar.

## Conteúdo
| Arquivo | O que é | Estado |
|---|---|---|
| `pre_entrega.py` | Compõe `validate_spec_sot`, `check_repo_research`, `build_map --check` (bloqueantes, como no CI) e `check_invariants`, `check_dimensionamento`, `check_refs`, `backlog_triggers` + 13 detectores de `gate_extra`/`revisor_detectores` (informativos). Emite `pre-entrega.json` com sha256 de plan/checks. Sem lógica nova. | Testado (`test_pre_entrega.py`, 3 testes OK); **não instalado** |
| `PATCH-ESPECIFICADOR-P-F-2026-11-01.patch` | (1) TMP→Signal Package; (2) `AGENTS.md §3`→`§4`; (3) CCM-001 BASELINED e J-001 sem "trava SPEC-003"; (4) CC-01..CC-12; (5) §9 vira ponteiro ao ROADMAP; (6) item do Autopré-check: o Orquestrador roda `pre_entrega.py` e anexa o JSON. | `git apply --check` OK; **não aplicado** |

## Para instalar (só por ordem expressa de Andraus)
1. Mover `pre_entrega.py` para `scripts/` e o teste para `tests/`; registrar em `governance/MECANISMOS.json` (COE-14) e no `GATE-MANIFEST.sha256`.
2. `git apply` do patch (emenda homologada ao `.claude/agents/especificador.md`; carimbo RPSA via `check_rpsa.py --register`).
3. Fluxo: Especificador edita → Orquestrador roda `pre_entrega.py` → devolve o JSON → corrige até zero bloqueante → Revisor recebe o mesmo JSON (casado por `SHA256-ALVO`).

## Medir antes de promover (4Es)
Contar Médias do R1 com e sem pré-gate em 5 rodadas; P-E (mutação) para recall e falso alarme; detectores só viram bloqueantes por ordem de Andraus.

## Limites
O pré-gate não acrescenta recall: o backtest da auditoria deu 0/3 Médias com os detectores atuais. Seu ganho imediato é **prova anexa e antecipação** (o autor vê antes do Revisor). O recall vem de P-B, C-1/C-2 e P-D.

## Avanço (2026-11-01, "Avançar"): P-E, C-1 e C-2 como protótipos medidos — nada instalado
Arquivos: `detectores_novos.py` (C-1a, C-1b, C-2), `mutacao_pe.py` (bateria de mutação), `test_detectores_novos.py` (5 testes). Rodar: `python -B mutacao_pe.py specs/features/SPEC-049`.

**Mutação (5 defeitos plantados no Plan SPEC-049 baselined):** pegou 4/5 — M1 definição de código apagada (C-1a), M2 grafia divergente (C-1a), M3 recusa sem código (C-1b), M4 número trocado em 1 local (C-2); **escapou M5** (✔ novo em `checks.md` sem evidência — C-4 ainda não escrito). Detectores já existentes (`gate_extra`, `revisor_detectores`): **0/5** nesta bateria.

**Falsos alarmes no Plan baselined:** `gate_extra`/`revisor_detectores` 0; C-1b 0; C-2 (renomeação) 0; **C-1a 1** (`CONTRADICTION_SIDE_OMITTED`, 1 uso sem prefixo `WRV_`; não verifiquei se é erro real ou código de outra Spec). Na 1ª versão, C-1a dava 35 (enums contados como códigos); a restrição às famílias de prefixo da própria tabela cortou para 1.

**Backtest no histórico real (SPEC-049 v1.0→v1.1→v1.2):**
- C-1b achou 1 linha na v1.0 (INV-WRV-01, recusa sem código) — relacionada ao achado R1-M01 do Revisor, mas esse achado cobria outras recusas que o detector **não** viu. Recall parcial. 0 na v1.1/v1.2.
- C-1a: só o 1 caso acima, em todas as versões; **não** reproduziu nenhum achado do Revisor.
- **C-2: não viável ainda.** Versão larga (qualquer token retirado) = 8–9 achados por transição, quase todos ruído (`SPEC-007` em 129 locais). Versão estrita (renomeação 1↔1) = 1 achado na v1.0→v1.1 (provável falso alarme: o código ainda é legítimo em outros pontos) e **0 na v1.1→v1.2, onde o Revisor achou resíduos reais** ("medida 1.540 em F6/§1.8" no `checks.md`) — a linha tinha vários tokens trocados de uma vez e a regra 1↔1 não dispara. Precisaria casar tokens por posição na linha, tratar menção histórica "(v1.1)" como legítima e ignorar IDs genéricos. **Não promover.**

**Leitura honesta:** C-1a/C-1b são viáveis como INFORMATIVOS (baixo falso alarme, pegam mutação sintética), mas o recall sobre achados reais do Revisor foi **pequeno** (≈1 parcial em 3 Médias da v1.0). C-2 não passou. O ganho esperado de P-B (rastro por item) e P-D (gabaritos) segue sendo o maior; detector sozinho não substitui o Revisor. Amostra: 1 Spec, 3 versões.
