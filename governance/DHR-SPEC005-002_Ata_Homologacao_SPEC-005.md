# DHR-SPEC005-002 — Ata de Homologação — SPEC-005 (Cognitive Event Bus) v1.0 — BASELINE

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Parecer do Revisor sobre o Plan: **CONFORME** (2026-10-05; 0 Crítico, 0 Médio, 3 Menores) — `specs/features/SPEC-005/plan.md` + `checks.md` |
| Data | 2026-10-05 |
| Status | **HOMOLOGADA — BASELINE v1.0** (instrução direta de Andraus em chat: "Aprovar a distinção e homologar"). Abertura: DHR-SPEC005-001. |
| Compatibilidade | Minor (não redefine CHM-001/CEM-001/CCM-001/SPEC-004; não fecha decisão aberta além de EVENT-BUS-001, dona = esta Spec) |
| Gates | `validate_spec_sot.py` 12/12 PASS · `check_repo_research.py` OK · `check_doc_sync.py` ERRO=0 · `build_map.py --check` em dia · `npm run lint`: "Status:" pré-existente (SPEC-004/046), não-regressão |

---

## 1. Decisões de Andraus (chat, 2026-10-05)
1. **EVENT-BUS-001 — FECHADA:** aprovada a distinção do CEB-012 — o **Event Bus existe** como camada fina de notificação de mudança, **distinta do Blackboard**: o Blackboard guarda a verdade (estado); o Event Bus só notifica (**transporte ≠ fonte de verdade**); se um aviso se perde, nada se perde — o consumidor relê o log pelo cursor. Doc 13 (ENGENHARIA-GERAL) = fundamento histórico não-normativo (RULE-BB-001 prevalece).
2. **Latência:** orçamento/limite = **parâmetro a calibrar depois com dados reais de operação**, sem número arbitrário (não toca J-001/N-001).
3. **Broker completo** (prioridade, dead-letter distribuído, entrega entre máquinas): **ADIADO e REGISTRADO**, com condição de reavaliação (múltiplos consumidores distribuídos / alto volume). Nada apagado (INV-07).
4. **Saída ao Bot Trade Finance:** desenho "porta blindada" confirmado — **E3 fail-closed** (destino não autorizado ou notificação malformada → nada sai). **O SOT não executa ordem** (INV-05); o contrato do Signal Package em si = RISK-M5, não reaberto.

## 2. O que a SPEC-005 v1.0 estabelece
- **HIGH · D0–D7** (sem D8 pinado), Classe **D + C por BASpec** (CC-11); **12 BASpecs (CEB-001..012)**; **5 Enforcement Contracts (EC-CEB-001..005)**; 12 EARS; D7 T01..T10; D8 focado ADV-CEB-01..08.
- **RULE-CEB-001..012 + INV-CEB-01 → vigência imediata**; registro físico em `RULES.md` **diferido** (precedente SPEC-002/003/004; RULE-HG-02).
- **Sem duplicar a SPEC-004 v1.2:** herda por ID+versão ordem de commit, idempotência de escrita, replay, identidade autenticada, atomicidade (RULE-CBP-001/003/005/006/011/013/014). Lacuna real coberta: contrato do evento, envelope, correlation/causation, cursor/dedupe de **consumo**, entrega/retry/dead-letter limitados, ordering observado, metadados de transporte, saída externa.
- Baselines que citam o Event Bus apontam para o **número**: sem erratum (SPEC-001 EARS 8 e l.75, CEM-001 l.725, CONSTITUTION l.235, GPR-001 l.457, SAS-001 §6.9/§6.10). Mecanismo físico (push/poll) = INDETERMINADO (BUILD).

## 3. Achados do parecer (todos Menores, não-bloqueantes)
| ID | Tratamento |
|---|---|
| A-CK-09 | `SPEC-001/plan.md` l.75 cita "SAS-001 §6.7" (= Cognitive Budget) para metadados de transporte; o correto é **§6.10** (§6.9 = integração com o Event Bus). A SPEC-005 cita as seções corretas. Correção só por **erratum à SPEC-001 (INV-09) — pendente de decisão de Andraus** |
| A-CK-01 | Eixo VERTICAL (RULE-HV) N/A confirmado |
| A-ECC04-RISCO | Verbatim/valores de repositório sem web: limite estrutural do Revisor (ENF-03); declarado |

## 4. Permanecem ABERTAS (CONS-01)
**M-001 (enum) · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001.** (EVENT-BUS-001 **FECHADA** por este ato.) Pendências de gatilho: BL-003 e BL-008 seguem ATIVADOS (independentes); BL-017 `Em espera`; nenhum item com gatilho `spec:SPEC-005`.

## 5. Registro (efeitos aplicados)
- [x] Este documento · [x] `ROADMAP.md` (linha de estado, slot §21, próximo trabalho, listas de decisões abertas/fechadas) · [x] `AGENTS.md` §7 · [x] `governance/CATALOGO-OFICIAL.md` · [x] `backlog/RMR-001_Painel_Backlog.md` (11-bis) · [x] `plan.md` (versão/status) · [x] RPSA: carimbo dos agentes → `DHR-SPEC005-002` · [x] `build_map.py` + `--check`.
- Próximo da sequência: **SPEC-006** (Cognitive Knowledge Graph — H-001) — somente com autorização de Andraus e passo 1-bis do §23.

---

**Andraus**
