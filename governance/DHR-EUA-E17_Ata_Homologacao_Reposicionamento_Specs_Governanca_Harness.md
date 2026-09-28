# DHR-EUA-E17 — Ata de Homologação: Reposicionamento das Specs de Governança do Harness (FASE GOV)

| Campo | Valor |
|---|---|
| Código | **DHR-EUA-E17** |
| Objeto | Homologação da emenda **EUA-E17 v2** (`governance/EUA-E17_Reposicionamento_Specs_Governanca_Harness_PROPOSTA.md`) |
| Natureza | Emenda ao `ROADMAP.md` — interposição de uma **FASE GOV** (SPEC-019 integral + SPEC-020 núcleo A + SPEC-021) entre SPEC-001 (homologada) e SPEC-002; renumeração de fases; acréscimo de escopo à SPEC-019 (Contrato de Herança Vertical, Q1). |
| Data | 2026-09-21 |
| Vigência | **Imediata.** Reposição registrada no ROADMAP por banner de emenda (vigência plena); renumeração editorial cabeçalho-a-cabeçalho das Fases 10–17→8–15 = passo editorial diferido (INV-07-safe), sem efeito sobre a vigência. |

---

## 1. Fluxo de autoridade (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (rascunho de chat, 2026-09-21 → docs/_legacy/)
Etapa 2 — Formalização (trata parecer) . ✅ Especificador (Claude Code) — EUA-E17 v2 em governance/
Etapa 3 — Parecer de integridade ....... ✅ Revisor — 1º parecer NÃO CONFORME (M-01/M-02/M-03) → v2 → re-parecer CONFORME
Etapa 4 — Consenso ..................... ✅ Andraus (Decisor Final), 2026-09-21 — instrução "homologue"; Q1–Q6 = Sim
Etapa 5 — Registro Oficial ............. ✅ EFETIVADO (Controlador) — este DHR + edições de baseline
```

Os três critérios de congelamento (GMC-001 Cap.5) satisfeitos: parecer CONFORME + consenso do Usuário + registro pelo Controlador.

---

## 2. Decisões de Andraus (Q1–Q6)

| # | Questão | Decisão |
|---|---|---|
| **Q1** | Incluir o Contrato de Herança Vertical (macro→micro) no escopo da SPEC-019 | **SIM** |
| **Q2** | Reposicionar SPEC-019 (integral) + SPEC-020 (núcleo A) + SPEC-021 para a FASE GOV | **SIM** |
| **Q3** | Aceitar SPEC-019 como processo de especificação (precede as specs que governa) | **SIM** |
| **Q4** | Renumerar as Fases (Fase 8→GOV; 10–17 → 8–15) preservando os números das Specs | **SIM** |
| **Q5** | Registrar no CATÁLOGO OFICIAL e no CONFLICT-MAP (K-MAN-20) | **SIM** |
| **Q6** | SPEC-020 faseada (núcleo A antecipado; dimensões B diferidas a SPEC-007/014/038) | **SIM** |

---

## 3. Objeto homologado

A nova sequência do caminho crítico da Trilha B passa a ser:

```
FASE 0   M0 (homologado)
FASE 1   SPEC-001 (homologada)
FASE GOV SPEC-019 Harness Governance & Evolution (integral, + Contrato de Herança Vertical)  ← próximo autorizado
         SPEC-020 Harness Evaluation (núcleo constitutivo classe A)
         SPEC-021 Harness Score / Maturity Model
FASE 1   SPEC-002 Evidence → SPEC-003 Conviction → … (ordem interna de domínio preservada)
```

- **Núcleo A da SPEC-020** (correctness, grounding, hallucination, role adherence, context management, safety, regression, robustness/adversarial) torna-se **constitutivo** — critérios que SPEC-002+ devem satisfazer durante a produção.
- **Dimensões B da SPEC-020** (RAG faithfulness→SPEC-007; tool correctness→SPEC-038; decision traceability→SPEC-014) **diferidas** — fecham por emenda pontual no ponto de dependência (não são tratadas como fechadas — CONS-01).
- **SPEC-019** ganha o **Contrato de Herança Vertical** (normativiza GEH-001 §6: regra de conservação de requisitos entre harnesses pai/filho + verificação inter-nível); resolve **L-001**.
- **Método da FASE GOV:** atomic-spec **v1.4** vigente (ou v1.5 se homologada antes do início da SPEC-019); independente do piloto EUA-E15.

---

## 4. Efeitos registrados (edições de baseline)

| Documento | Alteração | Estado |
|---|---|---|
| `ROADMAP.md` | Banner de emenda EUA-E17 (FASE GOV) + "próximo autorizado" → SPEC-019 + §25 atualizado | ✅ aplicado |
| `governance/CATALOGO-OFICIAL.md` | Linha EUA-E17 (HOMOLOGADA) §4 + linha DHR-EUA-E17 §7.3 + nota §6 (próximo Trilha B → SPEC-019) | ✅ aplicado |
| `governance/CONFLICT-MAP.md` | Emenda K-MAN-20 (reposição de fases; nenhuma colisão de rótulo — mudança de sequência) | ✅ aplicado |
| `.claude/agents/especificador.md` | `sincronizado-até: DHR-EUA-E16` → `DHR-EUA-E17` (RPSA) | ✅ aplicado |
| `.claude/agents/revisor.md` | `sincronizado-até: DHR-EUA-E16` → `DHR-EUA-E17` (RPSA) | ✅ aplicado |
| `governance/EUA-E17_..._PROPOSTA.md` | Status → HOMOLOGADA (referência a este DHR) | ✅ aplicado |
| `EUA-E17…` (raiz, rascunho) | Arquivado em `docs/_legacy/` (INV-07) | ✅ aplicado |

**Passo editorial diferido (não afeta vigência):** renumeração cabeçalho-a-cabeçalho das Fases 10–17→8–15 nos títulos de seção do ROADMAP. A autoridade da nova ordem é este DHR + o banner + EUA-E17 §3.2. (Padrão "vigência imediata / incorporação editorial diferida", como em EUA-E04..E14.)

---

## 5. Invariantes preservados

- **INV-07:** rascunho arquivado, não deletado; atas anteriores intocadas.
- **INV-09:** homologação formal (não baseline informal); registrada aqui e no CATALOGO.
- **CONS-01:** nenhuma decisão aberta fechada (J/G/H/I/K/L/C/M/N-001 seguem abertas; L-001 será resolvida pela SPEC-019 quando redigida, não agora; dimensões B da SPEC-020 marcadas como diferidas).
- **RPSA (EUA-E16):** agentes re-sincronizados (`sincronizado-até` → DHR-EUA-E17).

---

## 6. Encaminhamento

1. **Passo 11-bis (ROADMAP §23):** consultar `backlog/RMR-001` — tratar itens cujo Gatilho de Ativação dispare com esta homologação (ex.: `spec:SPEC-019 em redação`, `decisao:L-001`). *(Controlador — pendente na próxima consulta ao painel.)*
2. **Próximo trabalho autorizado:** **SPEC-019 — Harness Governance & Evolution** (Fase GOV, posição 1), sob atomic-spec v1.4.
3. **BL-013 (MC-GOV-001)** e **BL-015 (MC-LRN-001)** têm gatilho `spec:SPEC-018/019 em redação` / `decisao:L-001` — passam a poder ativar quando a SPEC-019 entrar em redação (verificar no RMR-001).

---

*Ata registrada pelo Controlador. Homologação por Andraus (Decisor Final), 2026-09-21. Parecer do Revisor: CONFORME (v2). Nenhum registro anterior removido — apenas superseded/aditado (INV-07/INV-09).*
