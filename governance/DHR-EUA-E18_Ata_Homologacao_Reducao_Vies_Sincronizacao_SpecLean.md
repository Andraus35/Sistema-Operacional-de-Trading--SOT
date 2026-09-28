# DHR-EUA-E18 — Ata de Homologação: Redução de Viés e Uso Sincronizado da Spec-Lean

| Campo | Valor |
|---|---|
| Código | **DHR-EUA-E18** |
| Objeto | Homologação da emenda **EUA-E18 v3** (`governance/EUA-E18_Reducao_Vies_Sincronizacao_SpecLean_PROPOSTA.md`) |
| Natureza | Emenda dual aos arquivos de agente — `§7-bis Autopré-check de Redução de Viés` no `especificador.md` (§3 dois-momentos + §7-bis Blocos A–D) e `Passo 5-bis Verificação Adversarial e de Conservação de Herança` no `revisor.md` (§4 item 8 + §5 Passo 5-bis + §6 template de relatório, incl. nota de proporcionalidade). Não altera baselines de domínio, gate determinístico nem o trio de autoridade. |
| Data | 2026-09-21 |
| Vigência | **Imediata**, para specs HIGH/CRITICAL a partir de agora (recomendado/não-bloqueante para MEDIUM; N/A para LOW). Primeira aplicação obrigatória: **SPEC-019** (FASE GOV, EUA-E17 — próximo trabalho autorizado). |

---

## 1. Fluxo de autoridade (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (rascunho de chat, 2026-09-21 → docs/_legacy/)
Etapa 2 — Formalização (v2) ............ ✅ Especificador (Claude Code) — trata achados #1–#5 da autocrítica
Etapa 3 — 1º parecer formal ............ ✅ Revisor — NÃO CONFORME RECUPERÁVEL (M-01/M-02/M-03; m-01/m-02/m-03)
Etapa 4 — Formalização (v3) ............ ✅ Especificador (Claude Code) — trata M-01/M-02/M-03/m-01/m-02/m-03
Etapa 5 — Re-parecer formal ............ ✅ Revisor — CONFORME (2 Menores editoriais, corrigidos)
Etapa 6 — Consenso ..................... ✅ Andraus (Decisor Final), 2026-09-21 — instrução "SIM"; Q1–Q7 = Sim
Etapa 7 — Registro Oficial ............. ✅ EFETIVADO (Controlador) — este DHR + edições de baseline
```

Os três critérios de congelamento (GMC-001 Cap.5) satisfeitos: parecer CONFORME + consenso do Usuário + registro pelo Controlador.

---

## 2. Decisões de Andraus (Q1–Q7)

| # | Questão | Decisão |
|---|---|---|
| **Q1** | Aprovar a adição do §7-bis (Autopré-check de Redução de Viés) ao `especificador.md` | **SIM** |
| **Q2** | Aprovar a adição do Passo 5-bis ao protocolo de revisão do `revisor.md` | **SIM** |
| **Q3** | Achados do Passo 5-bis são Críticos apenas para herança não demonstrada e violação INV-05; Médios/Menores nos demais casos | **SIM** |
| **Q4** | Obrigatoriedade para HIGH/CRITICAL; opcional (recomendado, não-bloqueante) para MEDIUM | **SIM** |
| **Q5** | Diferir a incorporação ao `atomic-spec.md` ao piloto vigente (auditoria retroativa da SPEC-001, EUA-E15) rumo à v1.5 | **SIM** |
| **Q6** | Registrar no CATÁLOGO OFICIAL e no CONFLICT-MAP (K-MAN-21) | **SIM** |
| **Q7** | Checagem qualitativa de proporcionalidade (4Es) ao final das 3 primeiras specs da FASE GOV (Especificador §7.1 / Revisor §4.4), sem criar instrumento novo | **SIM** |

---

## 3. Objeto homologado

- **`especificador.md`** ganha o **§7-bis — Autopré-check de Redução de Viés** (Blocos A/B/C/D), inserido entre o Autopré-check §7 e os Invariantes §8, e o mapeamento "dois momentos da spec-lean" (Produção / Auto-revisão adversarial) no §3.
- **`revisor.md`** ganha o **Passo 5-bis — Verificação Adversarial e de Conservação de Herança** (seções A/B/C), inserido entre o Passo 5 e o Passo 6; o item 8 na lista de interpelação do §4 (exige §7-bis preenchido); e a linha correspondente + nota de proporcionalidade no template de relatório do §6.
- **Delimitação normativa (correção M-02 tratada na v3):** o Bloco B (Especificador) e a seção A do Passo 5-bis (Revisor) verificam apenas a herança **obrigação-a-obrigação** já vigente via CC-08 (EUA-E04). O **escopo** de a SPEC-019 tratar a regra de conservação-como-conjunto (Contrato de Herança Vertical) já está homologado (EUA-E17/DHR-EUA-E17 §2, Q1=SIM) — o que ainda não existe é a **regra escrita**, a redigir quando a SPEC-019 for elaborada. Nenhuma decisão fechada é tratada como pendente; nenhuma decisão aberta é tratada como fechada (CONS-01, bidirecional).
- **Nota de proporcionalidade (Q7):** ao final das 3 primeiras specs sob este protocolo na FASE GOV (SPEC-019 → SPEC-020 núcleo A → SPEC-021), o Revisor registra no relatório da terceira (hoje, SPEC-021) uma avaliação qualitativa de proporcionalidade do overhead — sem criar ferramenta determinística nova.

---

## 4. Efeitos registrados (edições de baseline)

| Documento | Alteração | Estado |
|---|---|---|
| `.claude/agents/especificador.md` | Novo §7-bis (Blocos A–D) entre §7 e §8; bloco "dois momentos" no §3; `sincronizado-até: DHR-EUA-E17` → `DHR-EUA-E18` (RPSA) | ✅ aplicado |
| `.claude/agents/revisor.md` | Novo Passo 5-bis (seções A–C) entre Passo 5 e Passo 6; item 8 no §4 (interpelação); linha Passo 5-bis + nota de proporcionalidade no template §6; `sincronizado-até: DHR-EUA-E17` → `DHR-EUA-E18` (RPSA) | ✅ aplicado |
| `governance/CATALOGO-OFICIAL.md` | Linha EUA-E18 (HOMOLOGADA) + linha DHR-EUA-E18 na tabela de atas | ✅ aplicado |
| `governance/CONFLICT-MAP.md` | Emenda K-MAN-21 (Manual Universal §44/§46 como PRÁTICA — separação de perspectivas / contestação estruturada; não normativo) | ✅ aplicado |
| `backlog/RMR-001_Painel_Backlog.md` | Passo 11-bis — gate desta homologação: nenhum item novo `ATIVADO` | ✅ aplicado |
| `governance/EUA-E18_..._PROPOSTA.md` | Status → HOMOLOGADA (referência a este DHR) | ✅ aplicado |
| `EUA-E18…` (raiz, rascunho) | Já arquivado em `docs/_legacy/` (INV-07) na formalização da v2 | ✅ (anterior) |

---

## 5. Invariantes preservados

- **INV-07:** rascunho arquivado, não deletado; atas anteriores (incl. o 1º parecer NÃO CONFORME sobre a v2) intocadas — registradas no próprio corpo da EUA-E18 v3 (§11).
- **INV-09:** homologação formal (não baseline informal); registrada aqui e no CATALOGO.
- **CONS-01 (bidirecional):** nenhuma decisão aberta (J/G/H/I/K/L/C/M/N-001) fechada por esta emenda; e — correção do erro apontado no 1º parecer (M-02) — nenhuma decisão já fechada (Q1 da EUA-E17) tratada como pendente.
- **RPSA (EUA-E16):** agentes re-sincronizados (`sincronizado-até` → DHR-EUA-E18).
- **Independência estrutural do Revisor (ENF-03):** não tocada — Write/Edit continuam ausentes do `revisor.md`.
- **Gate determinístico (`validate_spec_sot.py`):** não alterado.

---

## 6. Encaminhamento

1. **Passo 11-bis (ROADMAP §23):** consultado `backlog/RMR-001` — nenhum item novo `ATIVADO` por esta homologação (a emenda é de protocolo dos agentes, não de sequência de specs). Gate fecha limpo.
2. **Primeira aplicação obrigatória:** **SPEC-019** (Harness Governance & Evolution, FASE GOV) já é produzida sob o §7-bis obrigatório e revisada sob o Passo 5-bis obrigatório (é HIGH, per EUA-E17 §3.3).
3. **Checagem de proporcionalidade (Q7):** agendada para o relatório de revisão da 3ª spec sob este protocolo — hoje, **SPEC-021** (ordem SPEC-019 → SPEC-020 núcleo A → SPEC-021, EUA-E17 §3.2). Sem tooling novo; nota qualitativa no relatório do Revisor.

---

*Ata registrada pelo Controlador. Homologação por Andraus (Decisor Final), 2026-09-21. Parecer do Revisor: CONFORME (v3, após 1º parecer NÃO CONFORME RECUPERÁVEL sobre a v2). Nenhum registro anterior removido — apenas superseded/aditado (INV-07/INV-09).*
