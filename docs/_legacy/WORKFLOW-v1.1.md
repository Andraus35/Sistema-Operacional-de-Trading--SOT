> **ARQUIVADO (INV-07) — versão 1.1, superseded por `WORKFLOW.md` v2.0. Não normativo.**

# WORKFLOW — Setup Operacional Canônico do SOT

| Campo | Valor |
|---|---|
| **Versão vigente** | **1.1** |
| **Autor / autoridade** | **Andraus** — declaração soberana do setup operacional (decisão de 2026-10-01) |
| **Fonte original** | Declaração de Andraus, 2026-09-29 (DHR-ECC05-001), transcrita fielmente (RCN-001). Nome anterior: RUNTIME-WORKFLOW-SOT (v1.0, em `reference/`). |
| **Posição** | Raiz do repositório. Referenciado por `AGENTS.md`. |

## Regras de uso e de manutenção (leia antes de citar ou editar)

1. **Autoridade.** Este documento é a fonte primária do *setup operacional* (como o SOT é usado em runtime). Toda Spec que toque o pipeline (agentes Estrutural/Institucional/Operacional, Manager, Risk Agent, Conviction/Fusion) deve **conformar-se** a ele; divergência = achado do Revisor, resolvida por Andraus (nunca pela Spec). **Não** substitui os modelos canônicos (CEM-001/CHM-001/CCM-001…), a hierarquia constitucional (AGENTS.md §6) nem o ADR-MANAGER-001 — apenas declara o que o operador faz.
2. **Citação estável.** O resto do repositório cita **só por ID** (`WF-xx`, `WF-Dxx`) e por "versão vigente" — nunca por número de linha ou posição. IDs **nunca são reutilizados nem renumerados**; item removido vira `[REVOGADO em vX.Y]`, não some.
3. **Edição.** Só Andraus altera o conteúdo. Cada edição: (a) incrementa a versão (Maior = muda/remove passo; Menor = acrescenta/esclarece), (b) acrescenta linha ao Changelog, (c) arquiva a versão anterior em `docs/_legacy/` (nome `WORKFLOW-v<versão>.md`) (INV-07). Mudança de ID ou de significado de um passo exige registrar o impacto nas Specs que o citam (ver §"Citado por" abaixo).
4. **Termos não fechados** ficam em `WF-Dxx` (decisão pendente). Nenhum `WF-Dxx` pode aparecer como fechado em qualquer entrega (CONS-01). Ao fechar, o item vira `FECHADO` com data — não é apagado.
5. **Status epistemológico:** [FONTE] declaração direta do usuário. Mapeamentos para termos do repositório marcados [INFERÊNCIA] até confirmação.

## Pipeline declarado

| ID | Passo (texto fiel à declaração de Andraus) |
|---|---|
| **WF-01** | **Pré-condição.** Antes da abertura da Killzone: sistema ligado; usuário aponta **Time Frame** e **tipo de Trading** (position / swing / day). |
| **WF-02** | **Fase 1 — Contexto estrutural.** **Agente Estrutural** (Elliott — mapeia a `Structural Agent` do ADR-MANAGER-001) observa estrutura de ondas → marca → trata Evidência → forma Hipótese → forma Convicção → entrega análise+convicção. |
| **WF-03** | **Fase 1 — Confirmação institucional (condicional).** Se o Agente Estrutural apontar oportunidade: dispara **Agente Institucional** (SMC — mapeia a `Institutional Agent`), que repete o mesmo ciclo (observar/marcar/tratar/hipótese/convicção) e entrega. |
| **WF-04** | **Fase 1 — Síntese de contexto (Manager, Fase 1/Dispatch do ADR-MANAGER-001).** Manager Agent forma a **convicção macro de contexto**. Se conclusiva: registra um **alarme-gatilho de preço** — nível a ser ativado (ou não) somente após a abertura da Killzone. *(Mecanismo hoje NÃO documentado em nenhuma Spec/ADR — candidato a formalização: ver WF-D02.)* |
| **WF-05** | **Ativação (Killzone).** Se o alarme-gatilho ativa: dispara **Agente Operacional** (mapeia a `Operational Agent`, single TF — ex. M5), num **Time Frame de entrada diferente do TF de contexto**. Faz o devido tratamento (observar/marcar/tratar/hipótese/convicção) e entrega ao Manager. |
| **WF-06** | **Fase 2 — Síntese global (Manager, Fase 2/Conviction do ADR-MANAGER-001).** Manager forma **convicção global**, decide se envia, e monta o pacote de **risco-retorno**. |
| **WF-07** | **Gate de Risco.** Envia ao **Agente de Risco** (família RISK-SPEC, BL-018), que analisa e decide se envia — ou não — o sinal ao **Bot Trade Finance** externo, com os dados de entrada. |

## Termos e pontos em aberto (CONS-01 — decisões de Andraus)

| ID | Ponto | Candidato / observação | Estado |
|---|---|---|---|
| **WF-D01** | Killzone | Não documentada como mecanismo formal (janela de tempo? por sessão/ativo? quem a abre?). | **ABERTA** (parte de WORKFLOW-SOT-001) |
| **WF-D02** | Alarme-gatilho de preço | Não documentado como mecanismo formal (saída da Fase 1 do Manager, precondição da Fase 2). | **ABERTA** (WORKFLOW-SOT-001) |
| **WF-D03** | Convicção macro de contexto × convicção global | Duas convicções (contexto vs. entrada); relação com Conviction Vector 8D / J-001 não fechada. | **ABERTA** (WORKFLOW-SOT-001) |
| **WF-D04** | Papel do ICT | Escola presente, mas ausente do pipeline (Estrutural=Elliott, Institucional=SMC). Em qual passo/agente entra? | **ABERTA** (WORKFLOW-SOT-001) |
| **WF-M01** | Agente Estrutural ↔ `Structural Agent` (Elliott) | ADR-MANAGER-001 §2.3 | [INFERÊNCIA] — confirmar SPEC-010 |
| **WF-M02** | Agente Institucional ↔ `Institutional Agent` (SMC) | ADR-MANAGER-001 §2.3 | [INFERÊNCIA] — confirmar SPEC-011/012 |
| **WF-M03** | Agente Operacional ↔ `Operational Agent` (single TF, M5) | ADR-MANAGER-001 §2.3 | [INFERÊNCIA] — confirmar SPEC-013/014 |

## Citado por (manter coerente ao editar)

`AGENTS.md` · `atomic-spec.md` (RULE-ECC-05) · `governance/RULES.md` (RULE-ECC-05) · `ROADMAP.md` (WORKFLOW-SOT-001) · `governance/CATALOGO-OFICIAL.md` · `.claude/agents/{especificador,revisor}.md` · `specs/features/SPEC-003/{research,plan,checks}.md` (WF-04, WF-06; WF-D01..D04). Atas `DHR-*` são registro histórico imutável e mantêm o nome antigo.

## Changelog

| Versão | Data | Mudança |
|---|---|---|
| 1.1 | 2026-10-01 | Movido para a raiz como `WORKFLOW.md` (era RUNTIME-WORKFLOW-SOT em `reference/`). Conteúdo dos passos **inalterado**; acrescentados IDs estáveis WF-01..07, WF-D01..04, WF-M01..03, regras de uso/manutenção e autoridade soberana de Andraus. Sem fechamento de decisão. |
| 1.0 | 2026-09-29 | Captura original (DHR-ECC05-001), RUNTIME-WORKFLOW-SOT (em `reference/`); arquivado em `docs/_legacy/`. |
