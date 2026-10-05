# Proposta de Abertura — SPEC-005: Cognitive Event Bus (slot ROADMAP §5, FASE 2)

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06)
**Autor:** Especificador Principal SOT (Claude Code, Opus 4.8)
**Data:** 2026-10-04
**Status:** **PROPOSTA DE ABERTURA — aguarda parecer do Revisor e HOMOLOGAÇÃO de Andraus** da definição da Spec. NÃO é baseline; o Plan (`plan.md`/`checks.md`) **não** foi escrito e é o próximo gate, só após homologação desta abertura.
**Depende de:** `research.md` (mesmo diretório — leia primeiro, incl. §4 cobertura SPEC-004, §5 repositórios e `sources/`).
**Autorização:** Andraus (chat, 2026-10-04: "Abrir SPEC-005 reenquadrada"). Caminho crítico — FASE 2; próxima na sequência após SPEC-004 homologada (ROADMAP §21/§25; DHR-SPEC004-003).

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-005** (preservado) | Slot do ROADMAP §5 (FASE 2); número **referenciado por baselines/canônicos** (SPEC-001 EARS 8, SPEC-004, CEM-001 l.725, CONSTITUTION l.235, GPR-001 l.457) → nunca renumerar/apagar (INV-07/CONST-01, RULE-ECC-01). |
| **Nome** | **"Cognitive Event Bus" (MANTIDO)** — decidido por Andraus (chat 2026-10-04; ver §12 Q-ABERTURA-1, respondida). O reenquadramento de rótulo foi **recusado**. | A proposta original era renomear para "Cognitive Change-Notification Bus" porque "Event Bus" carrega a conotação de **broker durável pub/sub** (KERNEL-V2/Doc 13), enquanto a durabilidade/ordem **já é da SPEC-004** (research.md §3/§4). **Andraus decidiu manter o nome legado**; o **escopo real permanece a camada fina** (Opção A, §3) — o rótulo não reautoriza broker. As baselines citam o **número**, não o nome → sem erratum em qualquer hipótese. |
| **Complexidade** | **HIGH** | Pin do ROADMAP §5 (P0 — HIGH) e atomic-spec §3. Menor que SPEC-004 (CRITICAL) porque a persistência/ordem/idempotência **de estado** — o núcleo de maior risco — já é da SPEC-004; a SPEC-005 opera **sobre** um substrato durável já homologado. |
| **Profundidade-alvo** | **D0–D7** (profile **standard**, AGENTS §4) | HIGH → D0–D7. Rigor adversarial extra (sem elevar o profile em silêncio) nos pontos de risco: **entrega duplicada/perdida, ordem observada pelo consumidor, replay a partir de cursor, dead-letter**. |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Nasce sob o gate de maturidade normativo. |
| **Classe predominante** (orientação, não vinculante — atomic-spec §10.6; CC-11) | **D (Determinístico)** para envelope/correlation-causation/cursor/ordering/dedupe; **C (Constitutivo)** para o enforcement de entrega a consumidor autorizado e o fail-safe "transporte não é fonte de verdade" (volta ao log) | Declaração **por BASpec** no Plan (CC-11, nunca por Spec inteira — SES-001 §50). Ver §5. |

**Natureza:** Spec de **infraestrutura cognitiva** (Trilha B) — transporte/notificação de mudanças. **Não** é Spec de especialidade de escola (CC-12 N/A, §6) nem de comportamento de trading (RULE-ECC-05 **não incide** — research.md §7); **análoga** à SPEC-004/SPEC-002 (serve o comportamento sem *ser* o comportamento).

---

## 2. Fronteira e escopo

### Dentro do escopo
- **Contrato do EVENTO (≠ objeto do Blackboard):** envelope, tipo de evento, origem, timestamp, **correlation ID**, **causation ID**, referência ao objeto/versão do Blackboard que o originou.
- **Propagação/notificação de mudança** sobre o log append-only da SPEC-004: **cursor de leitura** (último `seq` processado por consumidor), **catch-up/replay de notificações** a partir de um cursor (research.md §3.3).
- **Semântica de entrega:** delivery (at-least-once como piso), **retry**, **dead-letter**, **idempotência de consumo** (dedupe por chave de evento — distinta da idempotência de *escrita* da SPEC-004), **ordering** observado pelo consumidor (total intra-workspace herdado do `seq`; parcial/causal entre workspaces).
- **Destino/subscrição:** quais consumidores (agentes/Skills/Risk/feedback do Bot) recebem quais tipos de evento — **declaração de interesse**, sem assumir orquestração (quem é invocado/quando = Manager/WORKFLOW).
- **Canal de saída de notificação** para a fronteira externa (GPR-001 passo 11 "Blackboard → Event Bus → Bot Trade Finance") — **transporte da notificação**, respeitando INV-05 (SOT não executa ordem; o contrato do Signal Package é RISK-M5).
- **Observabilidade do transporte:** o que é observável (latência, perdas, dead-letter) — insumo para SPEC-040.
- **Metadados de transporte** (Latency/Freshness/Reliability/Expiration — SAS-001 §6.7): a SPEC-005 é a **dona** (o produtor não os define — SPEC-001 l.75).
- **Distinção formal Blackboard ↔ Event Bus** (resolve EVENT-BUS-001 — §8): "Blackboard guarda estado (fonte de verdade durável); Event Bus transporta/notifica mudanças (best-effort sobre o log)".

### Fora do escopo (Non-goals explícitos)
| Item | Motivo | Pertence a |
|---|---|---|
| Persistência/ordem/idempotência/replay/supersessão **de estado** | já baselined — não reabrir (CC-02/INV-09) | **SPEC-004** |
| Durabilidade própria do transporte (broker durável paralelo) | duplicaria a fonte de verdade da SPEC-004; over-engineering em escritor único/VPS (research.md §3.6) | — (adiado; ver Opção C) |
| Memória permanente / ontologia / grafo (H-001) | KG | **SPEC-006** |
| Estado persistente por agente (G-001) | | **SPEC-009** |
| Orquestração: quem reage, quando, em que ordem é invocado | controle ≠ transporte (RULE-BB-005; WORKFLOW FSM) | **SPEC-008 (Manager)** |
| Contrato do Signal Package / execução de ordem | INV-05 (SOT não executa) | **RISK-M5 / RISK-SPEC-022** |
| Redefinir CHM-001/CEM-001/CCM-001 | CC-02/CONST-01 | canônicos baselined (eventos apenas **propagados**) |
| Fórmula/pesos/limiares de convicção (J-001/N-001) | abertas | SPEC-003/CCM-001 / backtest |

---

## 3. Opções de reenquadramento — decisão explícita

| Opção | Descrição | Prós | Contras | 4Es |
|---|---|---|---|---|
| **(A) Camada fina de notificação de mudança sobre o log da SPEC-004 + canal de saída — RECOMENDADA** | Event Bus = *processo separado* que lê o log append-only (cursor) e **notifica** consumidores; durabilidade/ordem ficam na SPEC-004; push é otimização best-effort, fail-safe volta ao cursor | Alinha ao que a SPEC-004 já entrega (research.md §4); evita duplicar durabilidade; alinha ao WORKFLOW (FSM do Manager, agentes por fase); menor risco e custo; resolve EVENT-BUS-001 com fronteira nítida | Exige disciplina para não reintroduzir broker por inércia; ordenação entre workspaces precisa de definição (causal) | **Eficácia** preservada (nada perde durabilidade); **Economicidade** alta (sem infra nova na VPS) |
| (B) Fundir na SPEC-004 via emenda | Tratar notificação como mais um aspecto do Blackboard | Um só contrato | **Viola a separação constitutiva** "estado vs. transporte" (ROADMAP §5); SPEC-004 está BASELINE (reabrir = risco/INV-09); o slot SPEC-005 é referenciado por baselines e **não pode ser apagado** (INV-07) | Fere Eficácia (mistura responsabilidades); rejeitada |
| (C) Broker completo durável (pub/sub Kafka/RabbitMQ-like) | Barramento durável com subscrição autônoma 24/7 (visão KERNEL-V2/Doc 13) | Escalável para múltiplos consumidores distribuídos/alta vazão | **Over-engineering** sob escritor único (RULE-BB-002) + VPS única + log durável já existente (research.md §3.5/§3.6); duplica durabilidade; desalinha do WORKFLOW (agentes por fase, não assinantes autônomos) | Economicidade ruim sem ganho de Eficácia hoje; **adiar** como opção futura (registrada, não apagada) |

**Decisão proposta: (A) camada fina — CONFIRMADA por Andraus** (chat 2026-10-04; §12 Q-ABERTURA-2: camada fina + canal de saída do Signal Package). `SPEC-005-FORMA-001` resolvida na abertura quanto à **direção** (quantidade=1, escopo de notificação, não-broker), com o **mecanismo físico** (push/poll, LISTEN-NOTIFY, fila interna) **adiado ao Plan** (D4/D5) — INDETERMINADO, não presumido. Opção C **registrada e adiada** (não apagada), reavaliável se surgirem múltiplos consumidores distribuídos/alta vazão. Resposta de chat orienta a redação; **homologação formal da abertura segue sendo ato de Andraus**.

---

## 4. Quantidade — 1 Spec

**1 Spec** (SPEC-005). Contrato de evento + propagação + entrega + subscrição + observabilidade formam **um** conjunto coeso; cabe em uma sessão de revisão; SPEC-004 (estado) e SPEC-006 (permanente) já são slots vizinhos separados. Dividir fragmentaria um contrato coeso. `SPEC-005-SPLIT-001` resolvida: **não dividir** (sujeito a Andraus).

---

## 5. Classe RULE-MECH-01 (CC-11) — orientação predominante

A SPEC-005 citará RULE-MECH-01 no Plan → CC-11 (declaração **por BASpec**, nunca por Spec inteira — SES-001 §50).
- Envelope, correlation/causation ID, cursor de leitura, ordering observado, dedupe de consumo = **Classe D (Determinístico)**.
- Enforcement de **entrega a consumidor autorizado**, fail-safe "transporte ≠ fonte de verdade" (recuperação sempre pelo cursor sobre o log), dead-letter obrigatório em falha = **Classe C (Constitutivo)**, efeito **E1/E2** (notificação é efeito observável; a emissão **externa** ao Bot pode ser **E2/E3** — nível final por comportamento no Plan).
- Eventual juízo "evento bem-formado para propagação" = **Classe H** (gate de saída determinístico; bounded loop + critério de parada declarados por BASpec — RULE-MECH-03).

**Critério 4Es:** Eficácia primeiro — uma notificação perdida de WF-A03 (hipótese→SUPERSEDED/REFUTED) deixaria um alarme vivo indevidamente; por isso o fail-safe volta ao log (a durabilidade é da SPEC-004). Economicidade (não subir broker) nunca acima de Eficácia. Classe C reservada a risco alto (RULE-MECH-02).

---

## 6. Princípios de Domínio (RULE-PD-01 / CC-12) — **NÃO incide**

A SPEC-005 **não** é Spec de especialidade de escola (Elliott/SMC/ICT): é infraestrutura de transporte/notificação, agnóstica de escola (propaga qualquer evento cognitivo). **Nenhum `PD-xx` será proposto** (determinação análoga à SPEC-004/SPEC-002 — harness/infra neutro). A Classe (CC-11, §5) é declarada; CC-12 fica N/A por ausência de domínio de especialidade.

---

## 7. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação na abertura | Nota |
|---|---|---|
| CC-01 | OK | Event Bus é agnóstico de escola; não altera a hierarquia Elliott→…→ICT. |
| CC-02 | **Aplica — foco** | Não redefinir CHM-001/CEM-001/CCM-001 **nem SPEC-004** (BASELINE); apenas **propaga** eventos de ciclo de vida (CEM-001 l.717-727) e **lê/projeta** o log (SPEC-004). |
| CC-03 | OK | Não computa convicção; J-001/N-001 abertas; não toca WF-D03. |
| CC-04 | OK | Nenhuma das 5+5 Salvaguardas violada; custo nunca entra em convicção (INV-04); transporte não altera sinal. |
| CC-05 | OK | HIGH declarado. |
| CC-06/07 | Diferido ao Plan | Engineering Cards com campos SES-001 §59 + cadeia §60. |
| CC-08 | **Aplica — foco** | Bloco Herança/Delta no Plan: INHERITS = RULE-BB-001/004/005 (ID+versão); SPEC-004 (contrato de objeto/`seq`/replay, por referência); CEM-001 (eventos canônicos); SAS-001 §6.7 (metadados de transporte); SPEC-001 EARS 8 (evento "Hypothesis.Created"); WORKFLOW (WF-A03/WF-F02 tocados). REMOVED vazio. Nenhum ADDED contradiz o herdado (RULE-HD-02). |
| CC-09 | **Aplica** | Mecanismo físico (push/poll) = INDETERMINADO até o Plan; EVENT-BUS-001 declarada aberta, não como fato; sem falsa precisão em latência (números só com base). |
| CC-10 | Aplica | Declarar acepção: **Evento** (mudança notificada, SPEC-005) vs **Objeto** (estado versionado, SPEC-004) vs **Observação** (Skill, INV-06); "entrega" (transporte) vs "publicação" (commit de estado — SPEC-004). |
| CC-11 | Aplica (§5) | Classe por BASpec no Plan; C compatível com E1/E2/E3; D determinístico; H com bounded loop. |
| CC-12 | **NÃO incide** (§6) | SPEC-005 não é de especialidade de domínio. |

---

## 8. Dependências, decisões abertas e encaminhamento de EVENT-BUS-001 (CONS-01 — não fechar)

- **SPEC-004 (BASELINE)** — construir **sobre** (log append-only, `seq`, replay); não redefinir (CC-02/INV-09).
- **RULE-BB-001/004/005** (RULES.md, vigentes) — comunicação de estado via Blackboard; append-only; Orchestrator só coordena. O Event Bus **notifica**, não substitui o canal de estado (resolve a tensão com Doc 13 — research.md §3.6, conflito histórico TRACE-06; **respondido por Andraus**, chat 2026-10-04 (§12 Q-ABERTURA-4): Doc 13 = fundamento histórico não-normativo, superado quanto ao canal de estado — homologação formal pendente).
- **CHM-001/CEM-001/CCM-001** (baselined) — eventos propagados, não redefinidos (CC-02).
- **SPEC-001** (baselined) — emite "Hypothesis.Created"; a SPEC-005 define o transporte (l.75; SAS-001 §6.7).
- **SPEC-006 (KG) / SPEC-009 (estado por agente) / SPEC-008 (Manager) / RISK-M5 (Signal Package)** — fronteiras declaradas; **não absorver**.
- **WORKFLOW.md** (vigente) — conformar-se; WF-A03 (morte do alarme), WF-F02 (FSM) a declarar no Plan; **não** fechar WF-D03.
- **EVENT-BUS-001 (ÓRFÃ) — [DECISÃO NECESSÁRIA — permanece ABERTA].** Decisão "Event Bus existe? Como se distingue do Blackboard?" está aberta em `governance/ADR-MANAGER-001` l.201 e `DHR-ADR-HOC003` l.145, mas **ausente** de AGENTS §7 / ROADMAP §7. **Encaminhamento AUTORIZADO por Andraus** (chat 2026-10-04, §12 Q-ABERTURA-3): (1) registrar **EVENT-BUS-001 como decisão aberta ativa** nas listas oficiais, com **dona = SPEC-005**; (2) a SPEC-005 a **resolve na sua homologação** (a distinção formal é o núcleo da Spec — Opção A §3). A **execução do registro** nas listas (AGENTS §7 / ROADMAP §7) e o **fechamento** são **atos de Andraus/Controlador** — o Especificador **não** os executa (fronteira de governança). **EVENT-BUS-001 NÃO é fechada nesta abertura** (CONS-01); autorizado apenas o *encaminhamento*.
- **Abertas (não fechar):** EVENT-BUS-001, M-001, J-001, N-001, H-001, G-001, WF-D03, C-001 (granularidade EARS — relevante a eventos multi-condição).

---

## 9. Itens RMR-001 e comandos a rodar (o Especificador não promove — CONS-01)

- **Nenhum item do RMR-001 tem gatilho `spec:SPEC-005`** (verificado no painel; `backlog_triggers.py` a rodar). A abertura da SPEC-005 **não dispara item novo**.
- **ATIVADOS pré-existentes independentes desta abertura:** **BL-003** (`spec:SPEC-004 em redação`, já tratado na SPEC-004) · **BL-008** (auditoria retroativa SPEC-001). O Especificador **não** os promove nem encaminha (gate passo 11-bis + Andraus).
- **Em espera (NÃO ATIVADO) — independente desta abertura:** **BL-017** (fechamento das dimensões B da SPEC-020). Estado real no RMR-001 = **`Em espera`** (Andraus, chat 2026-10-03, DHR-BL012-001 — item devolvido a `Em espera`), gatilho `spec:SPEC-007 em redação` ∨ `spec:SPEC-014 em redação` (gatilho `spec:SPEC-038 em redação` já CONSUMIDO — DHR-SPEC038-002; dimensão *tool correctness* fechada por ERRATUM-SPEC020-001; restam RAG faithfulness ↔ SPEC-007 e decision traceability ↔ SPEC-014). A abertura da SPEC-005 **não** satisfaz esse gatilho e **não** o promove (CONS-01).
- **Comandos a rodar (não tenho Bash — listo para o operador/Controlador):**
  - `python scripts/check_repo_research.py specs/features/SPEC-005` (RULE-ECC-06 — deve passar com 2 elegíveis + 1 não elegível registrado)
  - `python scripts/build_map.py` **e** `python scripts/build_map.py --check` (BL-019 — mapa em dia após criar `specs/features/SPEC-005/`)
  - `python scripts/check_doc_sync.py` (drift documental — informativo; **espera-se** que aponte EVENT-BUS-001 como decisão citada em ADR/DHR e ausente das listas oficiais, coerente com §8 — matéria de auditoria do Revisor / decisão de Andraus)

---

## 10. Riscos

- **R-1 (over-engineering — broker por inércia terminológica):** o nome "Event Bus" puxa para a Opção C. **Contenção (atualizada 2026-10-04):** Andraus **manteve o nome** mas **confirmou a Opção A** (§12 Q-ABERTURA-1/Q-ABERTURA-2); o risco de "broker por inércia do nome" é contido declarando no texto que o **escopo é camada fina** (não-broker) independentemente do rótulo; C fica adiada e registrada (não apagada). O Plan deve reafirmar "transporte ≠ fonte de verdade" para não reintroduzir durabilidade.
- **R-2 (reabrir/duplicar a SPEC-004):** especificar durabilidade/ordem no transporte duplicaria a baseline. Contenção: CC-02 foco; Non-goal explícito; "transporte ≠ fonte de verdade".
- **R-3 (absorver vizinhos):** diluir fronteira com Manager (controle) / KG / Signal Package. Contenção: fronteiras §2 explícitas.
- **R-4 (fechar EVENT-BUS-001 por engano):** a pressão de "distinguir do Blackboard" pode levar a fechar a decisão órfã sem Andraus. Contenção: EVENT-BUS-001 fica **[DECISÃO NECESSÁRIA]**; o Plan **propõe** a distinção, a homologação é de Andraus.
- **R-5 (latência subdeclarada):** TMP/alarme que chega tarde ao downstream perde relevância (4Es). Contenção: latência é requisito do Plan (SAS-001 §6.7), declarada quando o consumidor é sensível a tempo.
- **R-6 (conflito histórico Doc 13):** tratar Doc 13 como norma. Contenção: TRACE-06 (documentado ≠ homologado); RULE-BB-001 prevalece; **respondido por Andraus** (chat 2026-10-04, §12 Q-ABERTURA-4 — Doc 13 histórico não-normativo, superado quanto ao canal de estado); homologação formal pendente.

---

## 11. Edições a documentos de governança — NÃO executadas pelo Especificador
*(O Especificador não edita ROADMAP/CATALOGO/RMR-001/WORKFLOW/agentes — AGENTS.md §5.)* Esta abertura **não** altera nenhum documento normativo. Após homologação, o Controlador/Andraus registram o estado (ROADMAP §25/§26, CATALOGO, RMR-001 passo 11-bis) e, se Andraus aceitar §8, registram **EVENT-BUS-001** nas listas oficiais. Nenhum modelo canônico baseline tocado (CONST-01). Nenhuma Spec baselined reescrita (INV-09).

---

## 12. Perguntas a Andraus (decisão de abertura) — em linguagem de trader

> **Contexto em uma frase:** a "caixa de estado" do sistema (onde ficam hipóteses, evidências, convicção) já está pronta e lacrada (SPEC-004). A SPEC-005 é só o **mensageiro** que avisa "algo mudou" para quem precisa saber — inclusive o aviso que sai para o robô executor lá fora.

> **Estado destas perguntas (atualização 2026-10-04):** as quatro foram **respondidas por Andraus** (chat 2026-10-04) e as respostas **não foram contestadas**. Ficam **registradas abaixo** como insumo para a HOMOLOGAÇÃO formal da abertura (a homologação é ato de Andraus; estas respostas de chat orientam a redação, não substituem o ato). **Nenhuma decisão aberta é fechada aqui** (CONS-01): em particular, **EVENT-BUS-001 permanece ABERTA**, a ser resolvida na homologação da própria SPEC-005.

1. **Q-ABERTURA-1 (nome):** O rótulo "Event Bus" sugere um sistema de mensageria pesado (tipo correio com central própria). Como a caixa de estado já guarda tudo com segurança, recomendo que a SPEC-005 seja só um **mensageiro leve** que avisa mudanças — e sugiro renomear para algo como **"Barramento de Notificação de Mudanças"**, mantendo "Event Bus" como apelido antigo. **Mantém o nome antigo ou aceita o reenquadramento?** *(Recomendação: reenquadrar — evita construir infraestrutura cara que o seu setup de VPS única não precisa.)*
   - **Resposta de Andraus (chat 2026-10-04) — respondida, não contestada:** **MANTER o nome "Cognitive Event Bus".** O reenquadramento de rótulo foi **recusado**; o nome legado permanece. O **escopo real continua sendo a camada fina** (Opção A, abaixo) — apenas o rótulo é preservado; não há volta a broker por causa do nome. *(Prevalece sobre a "Proposta" da §1; o campo Nome da §1 fica resolvido como "Cognitive Event Bus".)*

2. **Q-ABERTURA-2 (forma — A/B/C):** Três caminhos: **(A)** mensageiro leve que lê a caixa de estado e avisa quem precisa — barato, alinhado ao seu fluxo onde os agentes são chamados por fase; **(B)** juntar tudo na SPEC-004 (não recomendo — mistura as peças e mexe em algo já lacrado); **(C)** um sistema de mensageria completo e caro (só compensa com muitos consumidores espalhados, o que não é o seu caso hoje). **Confirma o caminho (A)?** *(Recomendação: A; deixo C registrado como opção futura, nada é apagado.)*
   - **Resposta de Andraus (chat 2026-10-04) — respondida, não contestada:** **Caminho (A) CONFIRMADO** — camada fina de notificação de mudança sobre o log da SPEC-004 **+ canal de saída do Signal Package**. Opção C fica registrada como opção futura (nada apagado — INV-07). O **mecanismo físico** (push/poll, LISTEN-NOTIFY, fila interna) segue **INDETERMINADO até o Plan** (D4/D5) — não presumido.

3. **Q-ABERTURA-3 (a decisão órfã EVENT-BUS-001):** Há uma pergunta antiga registrada nos bastidores — "o Event Bus existe mesmo? Como ele difere da caixa de estado?" — que nunca entrou na lista oficial de pendências. Recomendo **colocá-la na lista oficial com a SPEC-005 como responsável por respondê-la** na homologação. **Autoriza registrar essa pendência e deixar a SPEC-005 resolvê-la?** *(Recomendação: sim; eu não posso registrar sozinho — é decisão sua.)*
   - **Resposta de Andraus (chat 2026-10-04) — respondida, não contestada:** **Autorizado registrar EVENT-BUS-001** nas listas oficiais com **dona = SPEC-005**, **permanecendo ABERTA** e a ser **resolvida na homologação da SPEC-005**. O registro físico nas listas (AGENTS §7 / ROADMAP §7) e o eventual fechamento são **atos de Andraus/Controlador** — o Especificador **não** os executa nesta entrega. **EVENT-BUS-001 NÃO é fechada aqui** (CONS-01); apenas o *encaminhamento* (registrar como aberta, dona SPEC-005) está autorizado.

4. **Q-ABERTURA-4 (texto histórico Doc 13):** Um documento antigo de fundamentos diz "tudo passa pelo Event Bus", o que conflita com a regra vigente "tudo de estado passa pela caixa de estado (Blackboard)". Leio o documento antigo como **histórico/não-vigente** nesse ponto. **Confirma que o Doc 13 fica como referência histórica, sem valer como regra?** *(Recomendação: sim.)*
   - **Resposta de Andraus (chat 2026-10-04) — respondida, não contestada:** **Confirmado.** O **Doc 13 (ENGENHARIA-GERAL) é fundamento histórico NÃO-NORMATIVO**, **superado quanto ao canal de estado** (RULE-BB-001/SPEC-004 prevalecem: estado trafega/persiste no Blackboard; o Event Bus apenas notifica mudanças). TRACE-06 (documentado ≠ homologado). Não há conflito normativo a resolver pela Spec.

---

## 13. Próximo passo
Com o Dossiê (`research.md`), as capturas (`sources/`) e esta Proposta prontos, o conjunto segue para **parecer do Revisor** sobre o processo do Dossiê (atomic-spec §15; RULE-ECC-04 verbatim; RULE-ECC-06 repositórios — 2 elegíveis + 1 não elegível; RULE-ECC-05 não-incidência a confirmar) e, em seguida, **homologação de Andraus** da **definição da Spec** (número, nome, HIGH, D0–D7, quantidade=1, direção Opção A, Classe, não-incidência de CC-12/ECC-05) e do **encaminhamento de EVENT-BUS-001**, **antes** de qualquer `plan.md`/`checks.md`. Decisões abertas incidentes (EVENT-BUS-001, M-001, J-001, N-001, H-001, G-001, WF-D03) **permanecem abertas** (CONS-01).

**Pronto para revisão.**
