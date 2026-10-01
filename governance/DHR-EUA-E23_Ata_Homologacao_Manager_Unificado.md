# DHR-EUA-E23 — Ata de Homologação: Manager Agent Unificado (3 Specs sob "Manager Contract")

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Instrução direta de Andraus (chat, 2026-10-01): homologação da **EUA-E23 v2** (3 Specs do Manager sob um "Manager Contract") |
| Data | 2026-10-01 |
| Status | **HOMOLOGADA por instrução direta de Andraus em chat** — adota a **Alternativa 3-Specs** da `governance/EUA-E23_Manager_Unificado_SPEC008_SPEC015_PROPOSTA.md` (v2, §5) |
| Compatibilidade | Minor — não redefine modelo canônico baselined (CONST-01); não renumera nem apaga slots (INV-07); propaga/consolida decisões já homologadas (ADR-MANAGER-001, DHR-ARQ-001/002) e fixa **direção** de decomposição dos slots do Manager. Slots permanecem **indicativos** (RULE-ECC-01/02) — fronteira final só na abertura de cada Spec |
| Autoridade-fonte | `governance/EUA-E23_Manager_Unificado_SPEC008_SPEC015_PROPOSTA.md` (v2); `governance/ADR-MANAGER-001_Manager_Agent_Architecture.md` §2.1/§2.2/§2.3/§2.5 (HOMOLOGADO); `governance/DHR-ARQ-001_...md`; `governance/DHR-ARQ-002_...md`; `ROADMAP.md` §7/§9/§21/§26; `GLOSSARIO.md` §2-bis/§3; `docs/MATRIZ-WORKFLOW-SPEC.md`; `WORKFLOW.md` (soberano — só por ID); RULE-ECC-01/02; RULE-HV (herança vertical); RULE-MECH-01/CLASSE-MECH-001 |
| Não fecha | Nenhuma decisão aberta (CONS-01): **SPEC-015-SCOPE**, **J-001**, **N-001**, **M-001**, **WF-D03**, **Q-A5**, **Q-A9** seguem abertas. Não renumera/apaga slots. Não edita `WORKFLOW.md`. Não autoriza a abertura das Specs (direção, não autorização). |

---

## 1. Problema (resumido — detalhe na proposta)

O **Manager Agent** é o **ator único de orquestração** do SOT em 3 Fases (ADR-MANAGER-001 §2.3): Fase 0 (Mission Lifecycle — decisório leve), Fase 1 (Dispatch — mecânico/determinístico), Fase 2 (Conviction/Síntese — cognitivo leve, que **absorve** o antigo Synthesis Agent por DHR-ARQ-002). Mas o ROADMAP mantinha slots indicativos (**SPEC-008** "Cognitive Scheduler", **SPEC-015** "Mission Engine & Lifecycle", **SPEC-014** "Synthesis Agent") que, somados, cobriam o Manager **sem nomeá-lo como ator único** e **misturando naturezas cognitivas** dentro de slots (assimetrias A-1..A-4 da proposta; Conflito C-1 da MATRIZ; SPEC-015-SCOPE do ADR §7). [FONTE: EUA-E23 §1/§2; ADR-MANAGER-001 §4.2/§7; MATRIZ C-1.]

A instrução de Andraus (2026-10-01) pediu **simetria camadas×agentes** para fixar **quantidade** de Specs do Manager por melhores práticas. A análise de simetria (EUA-E23 §2) e a absorção do Synthesis (DHR-ARQ-002, que tornou a Fase 2 substancial) levaram à recomendação de **3 Specs** (1:1 com as 3 Fases do ADR e os 3 slots existentes), sob um **"Manager Contract"** comum que preserva o **ator único** (ADR §2.2).

## 2. Decisão (direção homologada — NÃO autoriza abertura)

1. **Adoção da Alternativa 3-Specs** (EUA-E23 v2 §5). Os três slots indicativos existentes são **repurposados sem renumerar nem apagar** (INV-07) como as três Specs do Manager Agent, uma por natureza cognitiva / Fase do ADR:

   | Slot (não renumerado) | Novo nome de slot | Fase (ADR) | Classe predominante* | Escopo-resumo |
   |---|---|---|---|---|
   | **SPEC-008** | **Manager — Orquestração Mecânica** | Fase 1 + serviços de tempo | **D/C** (gates não-LLM, ENF-03) | Dispatch/grafo de dependências; relógio/Killzone; alarme FSM; FSM do ciclo; orçamento/ativação progressiva |
   | **SPEC-015** | **Manager — Missão & Ciclo de Vida** | Fase 0 | **H/P** (decisório leve + gate) | Tipo de missão (Exploratória/Validação); ciclo de vida; portfólio; Campanha; Plano B; relação hipótese→missão |
   | **SPEC-014** (repurposado; absorve Synthesis — DHR-ARQ-002) | **Manager — Convicção & Síntese** | Fase 2 | **H/P** (cognitivo leve + gate de saída) | Ler Vetores de Convicção do Blackboard; **invocar** o mecanismo da SPEC-003/CCM-001; arbitrar conflitos; formar Convicção Global; gerar **TMP interno** (handoff ao Risco) |

   *\*"Classe predominante" é **orientação não-vinculante** (RULE-MECH-01/CLASSE-MECH-001 — a declaração normativa de Classe é por BASpec, SES-001 §50). Não constitui enforcement por Spec inteira.*

2. **"Manager Contract" instituído como direção.** Cria-se, quando da abertura, um documento de **contrato comum** (não um agente novo) — **pai de herança vertical (RULE-HV)** das três Specs — que garante o **ator único** (ADR §2.2) e disciplina as fronteiras Fase 0↔Fase 1↔Fase 2 (evitando reintroduzir o paradoxo circular que o ADR resolveu). O Manager permanece **um único ator lógico**; não se cria agente adicional.

3. **Slots permanecem INDICATIVOS (RULE-ECC-01/02).** Esta ata fixa **direção e nomes de slot**; **número, fronteira e decomposição final** de cada uma das três Specs só se fixam **na abertura**, por Dossiê de Pesquisa + homologação de Andraus (ROADMAP §23 passo 1-bis). A decomposição pode ainda ser revista (dividir/fundir — INV-07) na abertura, com justificativa homologada. **Fallback 2-Specs** (EUA-E23 §4, Fase 0+Fase 2 juntas) permanece registrado como alternativa histórica, não adotada.

4. **Fronteira Manager-Fase-2 × SPEC-003 (anti-double-ownership).** A **SPEC-003** redige **o mecanismo** (CCM-001, fusão, cálculo do Conviction Vector 8D); a **SPEC-014 repurposada (Manager — Convicção & Síntese)** é **o invocador/árbitro** que usa o mecanismo e decide, gerando o TMP interno. A Fase 2 **não** redefine o cálculo do vetor (DHR-ARQ-001). [FONTE: EUA-E23 §4.1.]

5. **Coerência com a EUA-E20 (FASE RISK):** a simetria **não exige** alterar o número de macro-slots de risco (6). O Risk Agent é sub-harness completo (grão de container); o Manager é grão de Spec concreta (1 natureza/1 Spec). Ver DHR-EUA-E20 §2.

6. **Escopo do que NÃO é decidido aqui (CONS-01):** não fecha SPEC-015-SCOPE, J-001, N-001, M-001, WF-D03, Q-A5, Q-A9; não renumera/apaga slots; não edita o `WORKFLOW.md` (soberano); não altera o número de macro-slots RISK; não decide sizing/execução (INV-05); **não autoriza a abertura** das três Specs (que seguem o gate regular do §23 na sua vez do caminho crítico).

## 3. Efeitos aplicados (propagação mínima e rastreável — Controlador, 2026-10-01)

| Arquivo | Mudança | Natureza |
|---|---|---|
| `ROADMAP.md` §7 (SPEC-008) | Nome de slot → "Manager — Orquestração Mecânica (Fase 1 + serviços de tempo)"; nota EUA-E23 (Manager Contract, ator único, Classe D/C orientativa, não renumerado) | Direção/registro |
| `ROADMAP.md` §9 (SPEC-014/SPEC-015) | SPEC-014 → "Manager — Convicção & Síntese (Fase 2)"; SPEC-015 → "Manager — Missão & Ciclo de Vida (Fase 0)"; nota EUA-E23 em cada; sem renumeração | Direção/registro |
| `ROADMAP.md` §21 (caminho crítico) | Anotações "[= Manager Fase 1/0/2]" harmonizadas com os 3 nomes; nota de Manager Contract | Direção/registro |
| `ROADMAP.md` §26 (capacidades) | Linhas SPEC-008/014/015 anotadas com os novos nomes de slot + EUA-E23; capacidades preservadas | Direção/registro |
| `GLOSSARIO.md` §2-bis (3 fases) + §3 (Manager Agent) | Mapa das 3 Fases ↔ 3 Specs do Manager (SPEC-008/015/014); "Manager Contract" citado; SPEC-015 deixa de ser a única "spec formal" | Terminologia |
| `docs/MATRIZ-WORKFLOW-SPEC.md` | Conflito C-1 marcado **encaminhado por EUA-E23** (3 Specs sob Manager Contract; fronteira final na abertura); WF-04/WF-06 "Spec dona" harmonizada aos 3 nomes | Matriz derivada (não-normativa) |
| `governance/CATALOGO-OFICIAL.md` §7.3 | Linha DHR-EUA-E23 (REGISTRADO); prefixo **EUA-E23 registrado como usado** | SSoT |
| `.claude/agents/especificador.md` + carimbo | `sincronizado-até` → última DHR; SYNC-DATE 2026-10-01; nota EUA-E23 | RPSA |
| `.claude/agents/revisor.md` + carimbo | `sincronizado-até` → última DHR; SYNC-DATE 2026-10-01; nota EUA-E23 | RPSA |

**Não tocado (baselined / soberano):**
- `WORKFLOW.md` — soberano de Andraus (WF-04/WF-06 já falam de "Manager" como ator único; consistente com esta ata).
- `canon/*` — nenhuma redefinição de modelo canônico (CONST-01). A varredura de termos legados em canon é tratada **separadamente** por `DHR-DIV-001` (só comentários DIV, texto normativo preservado).
- `specs/features/SPEC-003/*` — **sem renumeração de BASpecs**; SPEC-003 permanece consistente (Manager Fase 2 invoca o mecanismo — DHR-ARQ-001). Esta ata apenas confirma o dono da Fase 2 (SPEC-014 repurposado).

## 4. Guardas de sincronização (detector `check_doc_sync.py`)

- **D1/D2:** nenhuma decisão aberta é fechada nem flipada. SPEC-015-SCOPE, J-001, N-001, M-001, WF-D03, Q-A5, Q-A9 seguem **abertas**. B-001 permanece FECHADA (DHR-ARQ-001). A "quantidade de Specs do Manager" deixa de ser matéria aberta da EUA-E23 (direção decidida = 3), mas a **fronteira/decomposição final** permanece a decidir na abertura (RULE-ECC-01) — não é decisão CONS-01 registrada, é método.
- **D6 (WORKFLOW.md):** nenhuma `WF-Dxx` aberta declarada fechada; nenhum `WF-xx` inexistente citado; `WORKFLOW.md` não editado.
- **Slots:** SPEC-008/014/015 **repurposados, não renumerados nem apagados** (INV-07). Permanecem **indicativos** (RULE-ECC-01/02) até a abertura.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
