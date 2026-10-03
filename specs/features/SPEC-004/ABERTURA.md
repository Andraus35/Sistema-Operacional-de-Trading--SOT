# Proposta de Abertura — SPEC-004: Cognitive Blackboard Protocol

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/06)
**Autor:** Especificador Principal SOT (Claude Code, Opus 4.8)
**Data:** 2026-10-03
**Status:** **PROPOSTA DE ABERTURA — aguarda parecer do Revisor e HOMOLOGAÇÃO de Andraus** da definição da Spec. NÃO é baseline; o Plan (`plan.md`/`checks.md`) **não** foi escrito e é o próximo gate, só após homologação desta abertura.
**Depende de:** `research.md` (mesmo diretório — leia primeiro, incl. §4-bis Pesquisa em repositórios e `sources/`).
**Autorização:** caminho crítico — FASE 2; **próximo trabalho autorizado** (ROADMAP §25; FASE 1 concluída com a SPEC-003 homologada — DHR-SPEC003-001).

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-004** | Slot do ROADMAP §5 (FASE 2); número preservado — nenhuma divisão/renumeração (RULE-ECC-01). |
| **Nome** | **Cognitive Blackboard Protocol** | Idêntico ao título do slot; nenhuma capacidade nova inventada (ROADMAP §26). |
| **Complexidade** | **CRITICAL** | Pinada no ROADMAP §5 (P0 CRITICAL) e em atomic-spec §3 (Blackboard Protocol = CRITICAL). É o substrato de estado de **todo** o núcleo cognitivo (hipótese/evidência/convicção/missão transitam por ele); erro aqui contamina toda a cadeia. |
| **Profundidade-alvo** | **D0–D7** (profile **standard + adversarial D8 por ser CRITICAL**) | ROADMAP §5 e atomic-spec §3 pinam **D0–D7** para o Blackboard Protocol. **Observação de conflito aparente (AGENTS.md §4: CRITICAL → D0–D8):** o ROADMAP/atomic-spec pinam D0–D7 para ESTE componente especificamente. **[DECISÃO NECESSÁRIA — Q-ABERTURA-1]:** manter D0–D7 (pin específico do componente) ou elevar a D0–D8 (regra geral de CRITICAL, como se fez na SPEC-002 Q-A2)? Proposta do Especificador: **D0–D7 com D8 adversarial aplicado aos comportamentos de efeito E3** (concorrência/idempotência/supersessão), sem elevar o alvo global em silêncio (profiles PINADOS). Decisão de Andraus. |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Nasce sob o gate de maturidade normativo. |
| **Classe predominante** (orientação, não vinculante — atomic-spec §10.6) | **D (Determinístico)** para versão/ordenação/idempotência/append-only; **C (Constitutivo)** para enforcement de permissão de escrita (RULE-BB-002) e fail-closed de supersessão | Declaração normativa é **por BASpec** no Plan (CC-11). Ver §5. |

**Natureza:** Spec de **infraestrutura cognitiva** (Trilha B) — memória de trabalho compartilhada. **Não** é Spec de especialidade de escola (CC-12 N/A, §6) nem de comportamento de trading (RULE-ECC-05 não incide — research.md §7); é **análoga** às Specs de meta-harness neutras (SPEC-002), servindo o comportamento sem *ser* o comportamento.

---

## 2. Fronteira e escopo

### Dentro do escopo
- **Contrato do objeto publicado no Blackboard:** identidade, **versão**, **estado** (ciclo de vida), **namespace/workspace**, **proveniência**, **permissões** (RULE-BB-002), timestamp, referência de supersessão.
- **Protocolo de publicação/leitura/atualização** (D6): o quê publicar, quando, em que ordem, com que versionamento; leitura de qualquer workspace, escrita só no próprio (RULE-BB-001/002).
- **Ciclo de vida de objetos (D5):** criação, atualização (via nova versão), **supersessão**, expiração, invalidação — **append-only** (RULE-BB-004/INV-07). **Estados de objetos NÃO-hipótese (Evidência/Missão/Observação/Convicção) = M-001** (ABERTA — proposta de abordagem no Plan, não fechada aqui).
- **Concorrência, ordenação, idempotência (D4/D5):** versionamento otimista (rejeitar escrita com versão esperada divergente); chave de idempotência por publicação (retry seguro); ordem total/parcial de publicações num workspace.
- **Proveniência e reconstrução histórica (D6/D9 por referência):** quem publicou / qual atividade gerou / derivado de qual objeto / versão; API lógica de reconstrução do estado por replay — **sem** fechar o storage físico.
- **Relação Blackboard × memória permanente:** o Blackboard é memória de **trabalho**; o Knowledge Graph (SPEC-006) é memória **permanente** — fronteira declarada.

### Fora do escopo (Non-goals explícitos)
| Item | Motivo | Pertence a |
|---|---|---|
| Transporte de eventos/mudanças (envelope, subscrição, retry, replay, dead-letter, correlation/causation) | "Blackboard guarda estado; Event Bus transporta mudanças" | **SPEC-005** |
| Memória **permanente** / ontologia / grafo (H-001) | KG é memória permanente | **SPEC-006** |
| Schema de **estado persistente por agente** (G-001) | persistência por agente | **SPEC-009** |
| Redefinir CHM-001 (máquina de estados da hipótese), CEM-001 (Evidência), CCM-001 (Convicção) | **CC-02/CONST-01** | canônicos baselined (apenas armazenados/versionados aqui) |
| Fórmula/pesos/limiares de convicção (J-001/N-001) | abertas; INV-03/INV-04 | SPEC-003/CCM-001 (baselined) / backtest BL-032 |
| Orquestração (quem pensa, quando, consenso de controle) | controle ≠ quadro | **SPEC-008 (Manager)** |
| Guardrails de runtime / allow-deny de escrita em produção | runtime | **SPEC-042** |
| Governança de formação de conhecimento (publicar no KG) | | SPEC-007/018 |

---

## 3. Quantidade — 1 Spec vs. dividir (decisão explícita)

| Opção | Prós | Contras |
|---|---|---|
| **(A) 1 Spec unificada — ESCOLHIDA** | O contrato de objeto + protocolo + ciclo de vida + concorrência + proveniência formam **um** conjunto coeso de memória de trabalho; cabe em uma sessão de revisão; Event Bus (SPEC-005) e KG (SPEC-006) já são slots vizinhos separados, então a SPEC-004 fica naturalmente enxuta. | Densa em D5 (estados) — mitigado por BASpecs atômicas por tipo de objeto e pelo adiamento de M-001 ao Plan. |
| (B) Dividir (objeto/estado · concorrência · proveniência) | Unidades menores | Fragmenta um contrato coeso; cria fronteiras artificiais; re-trabalho; concorrência/proveniência não fazem sentido sem o contrato de objeto. |

**Decisão proposta: (A) 1 Spec.** `SPEC-004-SPLIT-001` resolvida nesta abertura (quantidade definida na abertura — RULE-ECC-01), sujeita à homologação de Andraus.

---

## 4. Decisões a tratar — mapa (o que esta Spec é dona, o que só referencia)

| Decisão | Papel da SPEC-004 | Status |
|---|---|---|
| **M-001** — estados do Blackboard para objetos NÃO-hipótese (Evidência/Missão/Observação/Convicção) | **DONA** — a SPEC-004 deve propor a abordagem (append-only + supersessão projetando o ciclo do CEM-001 — research.md §3.2) | **ABERTA** — proposta no Plan, homologação de Andraus; **não fechar nesta abertura** (CONS-01) |
| **BL-029** — proveniência `computed_by`/`gate_record` do objeto | **DONA** (DHR-DEC-003) — materializa no contrato de objeto/proveniência | Endereçar no Plan (ativa `spec:SPEC-004 em redação`) |
| **BL-002** — método de observação de falso-DENY do gate E3 | **requisito de observabilidade do Blackboard** (encaminhado à SPEC-004, DHR-DEC-003) | Endereçar no Plan |
| **BL-003** — persistência física de hipótese/estado | referencia o storage; **não fecha** o mecanismo físico | ativa `spec:SPEC-004 em redação` |
| **H-001** (KG real vs. memória) | **só fronteira** — não é dona (SPEC-006) | ABERTA — não tocar |
| **G-001** (estado persistente por agente) | **só fronteira** — não é dona (SPEC-009) | ABERTA — não tocar |
| **J-001/N-001** (convicção) | **só armazena/versiona** o objeto de convicção; não computa | ABERTAS — não tocar |
| Fronteira **SPEC-005** (Event Bus) e **SPEC-006** (KG) | declarada explicitamente (§2) | — |

**Relação com RULE-BB-\*, CHM-001, CEM-001:** a SPEC-004 opera **sobre** RULE-BB-001..005 (comunicação exclusiva via Blackboard; escrita só no próprio workspace; **RULE-BB-003 vigente** = o Blackboard NÃO define estado próprio de hipótese, usa o CHM-001; append-only RULE-BB-004; Orchestrator só coordena RULE-BB-005). Armazena/versiona hipótese (CHM-001), Evidência (CEM-001, idioma canônico INV-10) e Convicção (CCM-001) **sem redefinir** nenhum (CC-02). **WORKFLOW.md:** citar por ID apenas os `WF-xx` eventualmente tocados; não contradizer; não fechar `WF-D03` (conformidade declarada no Plan — research.md §7).

---

## 5. Classe RULE-MECH-01 (CC-11) — orientação predominante

SPEC-004 citará RULE-MECH-01 no Plan → sob CC-11 (declaração por BASpec, nunca por Spec inteira — SES-001 §50).
- Alocação de versão, ordenação, chave de idempotência, append-only/supersessão, checagem de versão esperada = **Classe D (Determinístico)**.
- Enforcement de **permissão de escrita** (RULE-BB-002: publicar só no próprio workspace), **fail-closed** em violação de append-only/versão divergente, precondição de proveniência obrigatória = **Classe C (Constitutivo)**, efeito **E2/E3** (publicação é commit em estado compartilhado; nível final por comportamento).
- Eventual juízo de "objeto bem-formado para publicação" = **Classe H** (gate de saída determinístico; bounded loop + critério de parada declarados por BASpec no Plan — RULE-MECH-03).

**Critério 4Es:** Eficácia primeiro — um objeto publicado com versão/proveniência corrompida ou fora de ordem contamina a reconstrução (D9) e toda a cadeia; só depois Eficiência/Economicidade. Classe C reservada a risco alto (RULE-MECH-02).

---

## 6. Princípios de Domínio (RULE-PD-01 / CC-12) — **NÃO incide**

SPEC-004 **não** é Spec de especialidade de escola (Elliott/SMC/ICT): é infraestrutura de memória de trabalho, agnóstica de escola (serve qualquer objeto cognitivo). Portanto **nenhum `PD-xx` será proposto** (determinação análoga à SPEC-002/SPEC-046 — harness/infra neutro). A Classe (CC-11, §5) é declarada; CC-12 fica N/A por ausência de domínio de especialidade.

---

## 7. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação na abertura | Nota |
|---|---|---|
| CC-01 | OK | Blackboard é agnóstico de escola; não altera a hierarquia Elliott→…→ICT. |
| CC-02 | **Aplica — foco** | Não redefinir CHM-001/CEM-001/CCM-001; o Blackboard **armazena/versiona**, não redefine (RULE-BB-003 vigente). |
| CC-03 | OK | Não computa convicção; dimensionalidade=8 intocada; J-001/N-001 abertas. |
| CC-04 | OK | Nenhuma das 5+5 Salvaguardas violada; custo nunca entra em convicção (INV-04). |
| CC-05 | OK | CRITICAL declarado. |
| CC-06/07 | Diferido ao Plan | Engineering Cards com campos SES-001 §59 + cadeia §60. |
| CC-08 | **Aplica — foco** | Bloco Herança/Delta no Plan: INHERITS = RULE-BB-001..005 (ID+versão) + CEM-001 (ciclo de vida/Lineage, p/ objetos de Evidência) + CHM-001 (estados da hipótese, por referência) + WORKFLOW (WF-xx tocados). REMOVED vazio. Nenhum ADDED contradiz o herdado (RULE-HD-02). |
| CC-09 | **Aplica** | M-001 declarada ABERTA, não como fato; INDETERMINADO onde a necessidade de CRDT/estado não está decidida; sem falsa precisão. |
| CC-10 | Aplica | Declarar acepção: Observação (Skill/ferramenta) vs Evidência (agente, INV-06); "estado do objeto no Blackboard" vs "estado da hipótese (CHM-001)". |
| CC-11 | Aplica (§5) | Classe por BASpec no Plan; C compatível com E2/E3; D determinístico; H com bounded loop. |
| CC-12 | **NÃO incide** (§6) | SPEC-004 não é de especialidade de domínio. |

---

## 8. Dependências e decisões abertas incidentes (CONS-01 — não fechar)
- **RULE-BB-001..005** (RULES.md) — construir **sobre** (vigentes); RULE-BB-003 permanece SUPERSEDED quanto a estado de hipótese (usa CHM-001).
- **CHM-001 / CEM-001 / CCM-001** (baselined) — armazenar/versionar, **não** redefinir (CC-02/CONST-01).
- **SPEC-001** (baselined) — Hypothesis Registry referencia o Blackboard como storage (BL-003).
- **SPEC-005 (Event Bus) / SPEC-006 (KG) / SPEC-009 (estado por agente)** — fronteiras declaradas; **não absorver**.
- **SPEC-020/021** — 9 lentes + gate E3 aplicam-se; cobertura no Autopré-check do Plan.
- **Abertas (não fechar):** **M-001** (dona = SPEC-004, a propor no Plan), H-001, G-001, J-001, N-001, C-001 (granularidade EARS — relevante ao protocolo).
- **WORKFLOW.md** (vigente) — conformar-se; WF-xx tocados a declarar no Plan; **não** fechar WF-D03.
- **RMR-001:** BL-003/BL-029/BL-002 ativam `spec:SPEC-004 em redação` (tratar no Plan/gate 11-bis). Promoção a `ATIVADO` e encaminhamento são de Andraus (CONS-01).

---

## 9. Itens RMR-001 — reflexo na abertura (o Controlador registra; aqui só o reflexo)
- **BL-003** (`spec:SPEC-004 em redação`) → ativará ao iniciar o Plan; ação: especificar storage do Blackboard referenciado pela SPEC-001. Não executado nesta abertura.
- **BL-029** (dona = SPEC-004, DHR-DEC-003) → proveniência `computed_by`/`gate_record`; endereçar no Plan.
- **BL-002** (Absorvido; encaminhado à SPEC-004) → observabilidade do Blackboard (falso-DENY); endereçar no Plan.
- **BL-011/BL-010** (Master Contracts EXP/RAG) → **não disparam** aqui (gatilhos SPEC-006/009/007); fonte de requisitos futura.
- ATIVADOS atuais independentes desta abertura: **BL-012** (MC-COG-001), **BL-017** (dimensão B SPEC-020) — pendentes de decisão de Andraus; não encaminhados por esta abertura.

---

## 10. Riscos
- **R-1 (fechar M-001 por engano):** a pressão de "definir estados" pode levar a fechar M-001 sem Andraus. Contenção: M-001 fica **ABERTA**; o Plan **propõe** a abordagem (append-only+supersessão), não a homologa (CONS-01).
- **R-2 (redefinir canônico):** o Blackboard "guarda" hipótese/evidência/convicção — risco de redefinir CHM/CEM/CCM. Contenção: CC-02 foco; RULE-BB-003 vigente; só armazenar/versionar.
- **R-3 (absorver vizinhos):** diluir fronteira com Event Bus (SPEC-005)/KG (SPEC-006). Contenção: fronteiras §2 explícitas; princípio "estado vs. transporte vs. permanente".
- **R-4 (over-engineering de concorrência):** adotar CRDT (yjs/automerge) onde RULE-BB-002 (escritor único por workspace) torna optimistic concurrency suficiente. Contenção: CRDT **adiado** (research.md §3.3/§5); decisão de mecanismo no Plan (D4).
- **R-5 (profundidade):** divergência D0–D7 (pin) × D0–D8 (regra CRITICAL). Contenção: **Q-ABERTURA-1** levada a Andraus (§1).

---

## 11. Edições a documentos de governança — NÃO executadas pelo Especificador
*(O Especificador não edita ROADMAP/CATALOGO/RMR-001/agentes — AGENTS.md §5.)* Esta abertura **não** altera nenhum documento normativo. Após homologação, o Controlador/Andraus registram o estado (ROADMAP §25/§26, CATALOGO, RMR-001 passo 11-bis). Nenhum modelo canônico baseline tocado (CONST-01). Nenhuma Spec baselined reescrita (research.md §6.4; INV-09).

---

## 12. Perguntas a Andraus (decisão de abertura)
1. **Q-ABERTURA-1 (profundidade):** manter **D0–D7** (pin do ROADMAP §5 / atomic-spec §3 para o Blackboard) ou elevar a **D0–D8** (regra geral CRITICAL, AGENTS.md §4, como na SPEC-002)? Proposta: **D0–D7 + D8 adversarial nos comportamentos E3**.
2. **Q-ABERTURA-2 (M-001 — abordagem):** aceita que a SPEC-004 **proponha** (no Plan, sem fechar) os estados de objetos não-hipótese como **append-only + supersessão projetando o ciclo do CEM-001**, deixando a homologação de M-001 para o fechamento do Plan?
3. **Q-ABERTURA-3 (escopo):** confirma **1 Spec** (não dividir) com as fronteiras SPEC-005/006/009 como propostas (§2)?

---

## 13. Próximo passo
Com o Dossiê (`research.md`), as capturas (`sources/`) e esta Proposta prontos, o conjunto segue para **parecer do Revisor** sobre o processo do Dossiê (atomic-spec §15; RULE-ECC-04 verbatim; RULE-ECC-06 repositórios; RULE-ECC-05 não-incidência a confirmar) e, em seguida, **homologação de Andraus** da **definição da Spec** (número, nome, CRITICAL, profundidade, quantidade=1, Classe, não-incidência de CC-12/ECC-05), **antes** de qualquer `plan.md`/`checks.md`. Decisões abertas incidentes (M-001, H-001, G-001, J-001, N-001) **permanecem abertas** (CONS-01).

**Pronto para revisão.**
