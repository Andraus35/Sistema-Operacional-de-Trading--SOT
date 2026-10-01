# DHR-ECC05-001 — Ata de Homologação — Pesquisa Multi-Lente (RULE-ECC-05)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Achado direto de Andraus (2026-09-29) — Dossiê de Pesquisa só cobria a lente de arquitetura |
| Data | 2026-09-29 |
| Status | **HOMOLOGADA — vigência imediata, prospectiva** |
| Compatibilidade | Minor (nova exigência sobre RULE-ECC-02 existente — não a redefine) |

---

## 1. Decisão

**Homologado `RULE-ECC-05` — Pesquisa Multi-Lente.** Toda Spec que define ou toca comportamento de agente analítico (Structural/Institutional/Operational), do Manager Agent (SPEC-015) ou do Risk Agent (família RISK-SPEC) DEVE pesquisar, no Dossiê de abertura, **3 lentes**: (1) Arquitetura do SOT (já exigido por RULE-ECC-02); (2) estado da arte/melhores práticas da **escola de análise** ou **risco-retorno** pertinente ao componente (Elliott/SMC/ICT/gestão de risco); (3) confronto explícito com `reference/RUNTIME-WORKFLOW-SOT.md` (pipeline operacional canônico declarado por Andraus).

**Registrado também** `reference/RUNTIME-WORKFLOW-SOT.md` — captura fiel (RCN-001) do workflow runtime descrito por Andraus: Time Frame/tipo de trading → Agente Estrutural (Elliott) → [se oportunidade] Agente Institucional (SMC) → Manager forma convicção macro de contexto + alarme-gatilho de preço → [se ativado na Killzone] Agente Operacional (TF de entrada) → Manager forma convicção global → Agente de Risco → Bot Trade Finance.

**Decisão aberta nova — `WORKFLOW-SOT-001`** (4 pontos do workflow não fechados nesta homologação — CONS-01): (a) Killzone e (b) alarme-gatilho como mecanismos formais ainda não especificados em nenhuma Spec/ADR; (c) relação entre convicção-macro-de-contexto/convicção-global e o Conviction Vector 8D (J-001); (d) onde o ICT entra no pipeline (não apareceu no relato do usuário, que só cita Elliott=Estrutural e SMC=Institucional). Resolução diferida para a abertura das Specs SPEC-010..015/RISK-SPEC pertinentes.

---

## 2. Efeitos imediatos

1. **RULE-ECC-05 — FATO NORMATIVO com vigência imediata**, registrada em `governance/RULES.md` (família RULE-ECC).
2. **`reference/RUNTIME-WORKFLOW-SOT.md` — insumo obrigatório** de confronto para Specs de trading (não é baseline técnico — não redefine CEM-001/CHM-001/ADR-MANAGER-001).
3. **`atomic-spec.md` §15** — parágrafo "Pesquisa Multi-Lente" adicionado; emenda no cabeçalho.
4. **`.claude/agents/especificador.md`/`revisor.md`** — checklists atualizados; carimbo `sincronizado-até` avançado para esta ata.
5. **Prospectiva — incide a partir de SPEC-003.** Não retroage sobre SPEC-001/002/019/020/021 (nenhuma toca comportamento de trading diretamente).
6. **`WORKFLOW-SOT-001` — nova decisão aberta**, registrada no ROADMAP.

---

## 3. Registro do Controlador (efeitos aplicados — 2026-09-29)

- [x] `reference/RUNTIME-WORKFLOW-SOT.md` — criado.
- [x] `atomic-spec.md` — emenda no cabeçalho; §15 "Pesquisa Multi-Lente".
- [x] `governance/RULES.md` — RULE-ECC-05 na família RULE-ECC; cabeçalho anotado.
- [x] `.claude/agents/especificador.md` — novo item de autopré-check; carimbo atualizado.
- [x] `.claude/agents/revisor.md` — Passo 4-bis emendado; carimbo atualizado.
- [x] `ROADMAP.md` — `WORKFLOW-SOT-001` registrada como decisão aberta.
- [x] `governance/CATALOGO-OFICIAL.md` — nova linha de ata.
- [x] Mapa, referências cruzadas, doc-sync revalidados.

---

## 4. Adendo — Correção de escopo (mesmo dia, 2026-09-29)

Achado do próprio Andraus, logo após a homologação: o texto original de `RULE-ECC-05` citava apenas Structural/Institutional/Operational/Manager/Risk — **excluía a SPEC-003** (Conviction Vector/Fusion Engine/Conviction Engine), que é exatamente onde as 8 dimensões (incl. estrutural/institucional/operacional) são agregadas e onde J-001/N-001 fecham. Corrigido: `RULE-ECC-05` agora inclui explicitamente **"Conviction/Fusion Engine (SPEC-003)"** no escopo. Aplicado em `RULES.md`, `atomic-spec.md §15`, `especificador.md` e `revisor.md` — mesmo dia, antes da abertura da SPEC-003.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
