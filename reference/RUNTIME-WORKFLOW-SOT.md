# RUNTIME-WORKFLOW-SOT — Workflow Operacional Canônico (declarado por Andraus, 2026-09-29)

> **Natureza:** referência externa/operacional — captura o workflow real de uso do SOT em runtime, tal como declarado por Andraus. **Não é baseline técnico** (não redefine CEM-001/CHM-001/ADR-MANAGER-001) — é **insumo obrigatório de confronto** para toda Spec futura que toque o pipeline de agentes analíticos, o Manager Agent (SPEC-015) ou o Risk Agent (BL-018), via `RULE-ECC-05` (proposta, pendente de homologação).
> **Status epistemológico:** [FONTE] — declaração direta do usuário, transcrita fielmente (RCN-001), não parafraseada.

## Pipeline declarado

1. **Pré-condição.** Antes da abertura da Killzone: sistema ligado; usuário aponta **Time Frame** e **tipo de Trading** (position / swing / day).
2. **Fase 1 — Contexto estrutural.** **Agente Estrutural** (Elliott — mapeia a `Structural Agent` do ADR-MANAGER-001) observa estrutura de ondas → marca → trata Evidência → forma Hipótese → forma Convicção → entrega análise+convicção.
3. **Fase 1 — Confirmação institucional (condicional).** Se o Agente Estrutural apontar oportunidade: dispara **Agente Institucional** (SMC — mapeia a `Institutional Agent`), que repete o mesmo ciclo (observar/marcar/tratar/hipótese/convicção) e entrega.
4. **Fase 1 — Síntese de contexto (Manager, Fase 1/Dispatch do ADR-MANAGER-001).** Manager Agent forma a **convicção macro de contexto**. Se conclusiva: registra um **alarme-gatilho de preço** — nível a ser ativado (ou não) somente após a abertura da Killzone. *(Mecanismo hoje NÃO documentado em nenhuma Spec/ADR — candidato a formalização.)*
5. **Ativação (Killzone).** Se o alarme-gatilho ativa: dispara **Agente Operacional** (mapeia a `Operational Agent`, single TF — ex. M5), num **Time Frame de entrada diferente do TF de contexto**. Faz o devido tratamento (observar/marcar/tratar/hipótese/convicção) e entrega ao Manager.
6. **Fase 2 — Síntese global (Manager, Fase 2/Conviction do ADR-MANAGER-001).** Manager forma **convicção global**, decide se envia, e monta o pacote de **risco-retorno**.
7. **Gate de Risco.** Envia ao **Agente de Risco** (família RISK-SPEC, BL-018), que analisa e decide se envia — ou não — o sinal ao **Bot Trade Finance** externo, com os dados de entrada.

## Termos que precisam de reconciliação formal (não fechados aqui — CONS-01)

| Termo do usuário | Candidato de mapeamento | Status |
|---|---|---|
| Agente Estrutural | `Structural Agent` (Elliott) — ADR-MANAGER-001 §2.3 | [INFERÊNCIA] — confirmar na SPEC-010 |
| Agente Institucional | `Institutional Agent` (SMC) — ADR-MANAGER-001 §2.3 | [INFERÊNCIA] — confirmar na SPEC-011/012 |
| Agente Operacional | `Operational Agent` (single TF, M5) — ADR-MANAGER-001 §2.3 | [INFERÊNCIA] — confirmar na SPEC-013/014 |
| Killzone | Não documentado como mecanismo formal | **[DECISÃO NECESSÁRIA]** |
| Alarme-gatilho de preço | Não documentado como mecanismo formal (parece ser saída da Fase 1 do Manager, consumida como precondição da Fase 2) | **[DECISÃO NECESSÁRIA]** |
| Convicção macro de contexto / convicção global | Duas convicções distintas (contexto vs. entrada) — relação com Conviction Vector 8D (J-001) não fechada | **[DECISÃO NECESSÁRIA]** |
| ICT | Mencionado pelo usuário como escola presente, mas não aparece no pipeline acima (Estrutural=Elliott, Institucional=SMC) | **[DECISÃO NECESSÁRIA]** — ICT entra em qual fase/agente? |

## Uso obrigatório

Toda Spec que abrir cobrindo Structural/Institutional/Operational Agent, Manager Agent (SPEC-015) ou Risk Agent (RISK-SPEC) DEVE confrontar seu Dossiê de Pesquisa contra este documento (RULE-ECC-05, proposta) — não apenas contra arquitetura de software.
