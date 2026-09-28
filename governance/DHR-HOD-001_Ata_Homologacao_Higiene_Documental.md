# DHR-HOD-001 — Ata de Homologação do Plano de Higiene e Organização Documental + RPIR

| Campo | Valor |
|---|---|
| Código | DHR-HOD-001 |
| Objeto | (1) Plano de reorganização de pastas (taxonomia §2) + arquivamento (INV-07) + reparo de referências; (2) **RPIR — Regra Permanente de Intake e Higiene da Raiz**: raiz = zona de intake; todo doc tratado → pasta respectiva ou excluído quando não incorporado |
| Data | 2026-09-21 |
| Autoridade | **Andraus** (Decisor Final) |
| Proposta | `governance/HOD-001_Plano_Higiene_Organizacao_Documental_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (1 Menor A-01 acatado; grep confirmou 48 refs `CAMADA*.MD` + 24 refs `governance/EUA-E`) |

---

## 1. Ato de Homologação

```
Etapa 1 — Proposta ......... ✅ Especificador (HOD-001, 2026-09-21)
Etapa 2 — Parecer .......... ✅ CONFORME (Revisor SOT; A-01 whitelist acatado)
Etapa 3 — Consenso ......... ✅ Andraus, 2026-09-21
Etapa 4 — Registro ......... ✅ EFETIVADO (regra permanente); execução F1..F5 = Ciclo de Hygiene #2
```

## 2. Decisões homologadas (Q1–Q7)

| # | Questão | Decisão |
|---|---|---|
| Q1 | Taxonomia-alvo (§2) | **APROVADO** |
| Q2 | F1 (root → `reference/camadas/`) | **APROVADO** |
| Q3 | F2 (`governance/emendas/` + `atas/` + `partida/`) | **APROVADO** |
| Q4 | Regra de reparo de referências (grep zero-pendências) + CATALOGO como "Mapa de Pastas" | **APROVADO** |
| Q5 | Execução como **Ciclo de Hygiene #2 (RCH-001)** + agent-sync (EUA-E16) | **APROVADO** |
| Q6 | `CAMADA APRENDIZADO.MD` → backlog (**BL-014**) para triagem antes de mover | **APROVADO** |
| Q7 | Instituir a **RPIR** (§6-bis): raiz = intake; tratado → pasta ou excluído; garantia tripla (gate + RMR + Hygiene passo 8); arquivar por padrão, delete físico só duplicata/lixo com autorização item-a-item | **APROVADO** |

## 3. Efeitos de registro (Controlador)

1. ✅ **RPIR instalada** (regra permanente): whitelist de raiz explícito; estados terminais de intake; garantia tripla — **sensor passo 8 no RCH-001** (efetivado), gate de intake nos Efeitos do Controlador, item de intake no RMR-001.
2. ✅ **BL-014** aberto no RMR-001 (triagem de `CAMADA APRENDIZADO.MD` por auditoria, antes de mover).
3. ✅ **Ciclo de Hygiene #2 autorizado** (F1..F5) — execução das movimentações com reparo de referências (grep zero-pendências) + agent-sync; a ser conduzido pelo Controlador como passo explícito.
4. ⏳ Movimentações físicas (F1..F5) **pendentes de execução** no Ciclo #2 — não realizadas nesta ata (operação com reparo amplo de referências).

## 4. Achado do parecer

| ID | Sev. | Estado |
|---|---|---|
| A-01 | Menor | **ACATADO** — whitelist de raiz explicitado (docs + config por extensão/nome + dotfiles fora de escopo). |

## 5. Conciliação INV-07 × "excluir"

- **Padrão:** não-incorporado → **arquivar** em `docs/_legacy/` (exclusão lógica; INV-07 preservado).
- **Delete físico:** só duplicata exata/lixo, **com autorização item-a-item de Andraus** (PC-08). Nunca automático.

## 6. Próximos passos

1. **Ciclo de Hygiene #2** executa F1..F5 (root→reference/camadas; governance/emendas+atas+partida; reference/externo; triagem; CATALOGO "Mapa de Pastas") com **grep zero-pendências** e **agent-sync** ao final.
2. **BL-014** (CAMADA APRENDIZADO / Learning) triado por auditoria antes de ser movido.
3. A RPIR passa a valer imediatamente: novos docs na raiz seguem o ciclo intake→pasta/excluir.

---

*Ata registrada pelo Controlador. INV-07 preservado; a higiene move e arquiva, nunca reescreve norma (INV-09). Movimentações físicas F1..F5 diferidas ao Ciclo de Hygiene #2 (passo explícito).*
