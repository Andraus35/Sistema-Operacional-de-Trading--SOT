# DHR-SPEC008-003 — Ata de Homologação — Errata R3-m07 ao Manager Contract (MMC-001)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Proposta `governance/propostas/SPEC-008/ERRATA-MMC-001-R3-m07-PROPOSTA-2026-11-08.md` (v2) · pareceres do Revisor na mesma pasta: R1 (NÃO CONFORME, 1 Média + 4 Menores) e R2 (CONFORME condicional, 0 Média, 1 Menor classe O não bloqueante) · alvo `governance/MMC-001_Manager_Contract.md` (MMC-001 v1.0, `DHR-SPEC008-002`, condição do §4) |
| Data | 2026-11-08 |
| Status | **ERRATA R3-m07 HOMOLOGADA e APLICADA ao MMC-001 — classe Patch, a versão NÃO muda (MMC-001 v1.0)**. Decisões de Andraus por AskUserQuestion, 2026-11-08: ordem "Aplicar a errata do R3-m07"; versão "Patch, sem mudar o número (Recomendado)"; forma "No próprio contrato, texto antigo preservado (Recomendado)". Assinatura = decisão registrada e citada nesta ata (AGENTS.md §10). *[Estado anterior preservado — INV-07: "condição R3-m07 pendente (DHR-SPEC008-002 §4)"]* |
| Compatibilidade | **Patch** — correção que devolve a modalidade da fonte (orientação × obrigação, RULE-SEM-03); base: regra de leitura do MMC-001 §1 ("se algum item divergir do texto-fonte, vale o texto-fonte") e DHR-SPEC008-002 §4. Minor e Major foram analisados na proposta (§3) e **não** escolhidos. CR-001 l.439: Patch não altera a versão |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Errata de texto em contrato de herança vertical: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]` (AskUserQuestion, 2026-11-08)
| # | Ponto | Decisão |
|---|---|---|
| O-1 | Ordem | Aplicar a errata do R3-m07 |
| E-1 | Versão | **Patch, sem mudar o número**. A resposta anterior ("Patch v1.0.1") foi dada sobre descrição inconsistente com a CR-001 (parecer R1, ER1-M01) e foi **reconfirmada** nesta rodada, já com as três hipóteses |
| E-2 | Forma | **No próprio contrato**, com o texto antigo preservado em `[antes]` (INV-07) |

## 2. Efeitos aplicados (Orquestrador) — só em `governance/MMC-001_Manager_Contract.md`
1. **§3.1.3 (l.72):** a Classe D/C passa a **orientação** (não vinculante, CC-11 por BASpec); fica como **obrigação** só "nenhuma BASpec H/P na Fase 1; se o Plan precisar de julgamento, volta a Andraus". Alcance da parte firme inalterado.
2. **§8.2-bis (l.169):** a linha se desdobra em obrigação (alcance como antes) e orientação (alcance **nenhum**); `[antes]` acrescentado junto ao bloco existente.
3. **§8.3 ADDED (c) (l.230):** Classe D/C = orientação, sem alcance vertical; "orçamento do ciclo" da P-7 segue só para SPEC-008/Tempo.
4. **Cabeçalho (l.3):** "ata §3" → "ata §4" (ER1-m03) **e ponteiro de uma linha para esta ata** (ER2-m01, Menor classe O do R2, incorporado como ponteiro puramente de rastreabilidade; sem regra nova).
Nada mais foi editado no contrato. Texto de cada alvo extraído da proposta, sem retranscrição; cada trecho antigo conferido como único no baseline. `ROADMAP.md` e `CATALOGO-OFICIAL.md`: registro desta ata; "Próximo trabalho autorizado" não muda.

## 3. O que esta ata NÃO afirma
- Gate determinístico não verificado (contrato não é `plan.md`; `revisor_gate` inerte em nuvem). O Revisor não tem Bash/git: comparou por leitura; o Orquestrador conferiu a unicidade dos trechos antigos antes de aplicar.
- Não cria regra, campo, estado, transição, ID normativo nem agente de trading; não edita `WORKFLOW.md`, `AGENTS.md`, `canon/` nem Spec baselined; não abre o Plan da SPEC-008.
- O chat/AskUserQuestion de Andraus não está no repositório (consta daqui).

## 4. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 · D-PCC-4 · P-11 e P-13 · dono da montagem do Signal Package. **Nenhuma decisão aberta é fechada por esta ata.**

## 5. Registro
- [x] Esta ata · [x] Decisões de Andraus (AskUserQuestion 2026-11-08) · [x] MMC-001 (4 alvos) · [x] ROADMAP · [x] CATALOGO · [x] RPSA · [x] handoff do ramo · [ ] merge (PR, CI verde — assinatura) · [ ] Plan da SPEC-008 (só por ordem de Andraus) · [ ] retrospectiva da SPEC-008 (antes de abrir outra Spec)

---

**Andraus** — *decisões dadas por AskUserQuestion, 2026-11-08; registro pelo Orquestrador.*
