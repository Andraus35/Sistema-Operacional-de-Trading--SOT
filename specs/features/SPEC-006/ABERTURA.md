# Proposta de Abertura — SPEC-006: Cognitive Knowledge Graph (slot ROADMAP §6, FASE 3)

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06)
**Autor:** Especificador Principal SOT (Claude Code, Opus 4.8)
**Data:** 2026-10-05
**Status:** **PROPOSTA DE ABERTURA — aguarda parecer do Revisor e HOMOLOGAÇÃO de Andraus** da definição da Spec. NÃO é baseline; o Plan (`plan.md`/`checks.md`) **não** foi escrito e é o próximo gate, só após homologação desta abertura.
**Depende de:** `research.md` (mesmo diretório — leia primeiro, incl. §0 auditoria do conceito legado, §4 cobertura por canônicos/Specs, §5 repositórios e `sources/`).
**Autorização:** Andraus (chat, 2026-10-05). Caminho crítico — FASE 3; próxima na sequência após SPEC-005 homologada (ROADMAP §21/§34; DHR-SPEC005-002).

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-006** (preservado) | Slot do ROADMAP §6 (FASE 3); capacidade **referenciada por canônicos/baselines** (CEM-001 l.494/563/608-615, CONSTITUTION l.233 EC-COG-003, SAS-001 §6.12, CEE-001 l.111, SPEC-001/SPEC-004) → nunca renumerar/apagar (INV-07/CONST-01, RULE-ECC-01). |
| **Nome** | **"Cognitive Knowledge Graph" (MANTIDO)** | Diferente do caso SPEC-005 (onde "Event Bus" sugeria broker), o nome aqui **já é coerente** com a natureza real — o fundamento-fonte define o KG como "**Modelo Cognitivo Permanente**", **não** banco de grafos (KERNEL-V2 l.1103-1104; research.md §0). "Graph" descreve as **relações auditáveis**, não um compromisso com banco de grafos (mecanismo físico = H-001, aberto). Reenquadramento de nome **não recomendado**; confirmar com Andraus (Q-ABERTURA-1). |
| **Complexidade** | **CRITICAL** (pin ROADMAP §6) | O KG ancora INV-07 (versionamento monotônico/imutabilidade), INV-04 (confiança ≠ Convicção), proveniência auditável (P13/CEM-001) e resolve H-001 — risco alto. **Conflito de baseline a reconciliar:** atomic-spec §3 (matriz) lista "Knowledge Graph \| MEDIUM \| D0–D5"; ROADMAP §6 pina **CRITICAL \| D0–D7**. **Recomendo seguir o ROADMAP (CRITICAL)** — a matriz §3 é anterior à EUA-E21 e trata o KG como item menor do que ele é à luz dos invariantes que ancora. **[DECISÃO NECESSÁRIA — reconciliar §3 × §6; Q-ABERTURA-2].** |
| **Profundidade-alvo** | **D0–D7 (núcleo) + D8 adversarial nos pontos de risco** (profile **standard + adversarial**, AGENTS §4) | ROADMAP §6 pina D0–D7; **AGENTS §4 mapeia CRITICAL → D0–D8**. Mesma reconciliação da SPEC-004 (CRITICAL, pin D0–D7, homologada "D0–D7 + D8 adversarial"): aplicar **D8 adversarial** sobre governança de escrita, imutabilidade (INV-07), confiança≠Convicção (INV-04), causalidade pós-hoc (RULE-CAU) e colisão de relações — **sem elevar o profile em silêncio** (declarado aqui; confirmar com Andraus). |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Nasce sob o gate de maturidade normativo. |
| **Classe predominante** (orientação, não vinculante — atomic-spec §10.6; CC-11) | **D (Determinístico)** para ontologia/catálogo de entidades-relações/temporalidade/versionamento/consulta estruturada; **C (Constitutivo)** para a **governança de escrita** (quem escreve, imutabilidade INV-07, gate E2/E3); **H** para eventual juízo de similaridade/causalidade com gate de saída | Declaração **por BASpec** no Plan (CC-11, nunca por Spec inteira — SES-001 §50). Ver §5. |

**Natureza:** Spec de **infraestrutura cognitiva de memória** (Trilha B) — memória semântica permanente. **Não** é Spec de especialidade de escola (CC-12 N/A, §6) nem de comportamento de trading (RULE-ECC-05 **não incide** — research.md §7); **análoga** à SPEC-004/SPEC-005/SPEC-002 (serve o comportamento sem *ser* o comportamento).

---

## 2. Fronteira e escopo

### Dentro do escopo (contrato cognitivo da memória permanente)
- **Ontologia enxuta:** tipos de entidade e tipos de relação **permitidos** + regras de integridade (a "gramática" — KERNEL-V2 l.1491-1496), **dentro** da SPEC-006 (não componente separado — §3.6 research; confirmar Q-ABERTURA-4).
- **Entidades (nós):** hipóteses, evidências, narrativas, missões, aprendizados, ativos, timeframes, regimes, estruturas (Elliott/Fibonacci/SMC/ICT) etc. — **por referência** aos contratos canônicos (CHM-001/CEM-001/CCM-001), nunca redefinindo-os (CC-02).
- **Relações:** CONFIRMA / REFUTA / DEPENDE_DE / HERDA / PERTENCE_A / INVALIDA / ORIGINA / similaridade / causalidade / hierarquia / estatística / de hipótese / de evidência / de missão / de aprendizado (pauta §6) — catálogo tipado.
- **Temporalidade / validade no tempo** das relações (quando passou a / deixou de valer) — "invalidar, não deletar" (research.md §3.1; INV-07).
- **Provenance** de toda entidade/relação — **por referência** a CEM-001 Lineage/`gate_record` e SPEC-004 (não redefinir — CC-02); princípio W3C PROV adaptado (research.md §3.2).
- **Versionamento / lifecycle** do nó/relação (permanente vs. temporário; arquivamento sob governança; INV-07) — Cognitive Trace Reconstruction como comportamento verificável (CEM-001 l.563-565).
- **Confiança de relação** — escala própria do KG, **explicitamente ≠ Convicção** (INV-04; não toca J-001/N-001).
- **Consulta cognitiva:** contrato de consulta semântica (padrão/similaridade/causalidade/histórico — KERNEL-V2 l.1440-1449).
- **Governança de escrita:** quem escreve, com que gate (E2/E3), imutabilidade, append-only (INV-07).
- **Distinção formal KG (permanente) ↔ Blackboard (trabalho, SPEC-004) ↔ RAG (SPEC-007)** — reafirmar, não reabrir.

### Fora do escopo (Non-goals explícitos)
| Item | Motivo | Pertence a |
|---|---|---|
| **Mecanismo físico de armazenamento** (grafo real / estrutura em memória / tabelas+índice) | decisão de engenharia deliberadamente aberta | **H-001 (ABERTA — só Andraus)** |
| Memória de trabalho / objetos ACTIVE / log append-only de estado | já baselined — não reabrir (CC-02/INV-09) | **SPEC-004** |
| Notificação/transporte de mudança | já baselined | **SPEC-005** |
| Formação de conhecimento / retrieval / `Documento recuperado ≠ conhecimento validado` | KG recebe conhecimento **já publicado** | **SPEC-007 (RAG/Knowledge Formation)** |
| Estado persistente por agente | G-001 | **SPEC-009** |
| Ciclo de evolução do conhecimento (P12) / backtest de aprendizado | K-001 | **SPEC-018** |
| Redefinir CHM-001/CEM-001/CCM-001 | CC-02/CONST-01 | canônicos baselined (entidades apenas **referenciadas**) |
| Fórmula/pesos/limiares de convicção; confiança como convicção | J-001/N-001 abertas; INV-04 | SPEC-003/CCM-001 / backtest |
| Escolher tecnologia de banco de grafos | H-001 + fora do mandato do Especificador | Andraus |

---

## 3. Opções de forma — decisão explícita (recomendação fundamentada)

| Opção | Descrição | Prós | Contras | 4Es |
|---|---|---|---|---|
| **(A) Camada fina de memória permanente sobre o log/registros existentes, com consulta cognitiva e governança de escrita; mecanismo físico INDETERMINADO (H-001) — RECOMENDADA** | O KG = contrato cognitivo (ontologia + entidades/relações + temporalidade + proveniência por referência + lifecycle + consulta + governança) **sobre** o conhecimento já validado/publicado; o **mecanismo físico** (grafo real, estrutura em memória, tabelas+índice) fica **aberto em H-001** | Alinha ao que SPEC-004 já entrega (log durável, proveniência); evita over-engineering de banco de grafos sob VPS única/escritor único (research.md §3.5); permite fechar o **contrato cognitivo** sem travar em decisão de engenharia; convergência temporal com estado da arte (Zep/Graphiti) **sem** importar engine | Exige disciplina para não reintroduzir "banco de grafos" por inércia; consulta cognitiva avançada (multi-salto) pode ficar limitada até H-001 ser fechada | **Eficácia** preservada (nada perde auditabilidade/INV-07); **Economicidade** alta (sem infra nova) |
| (B) Grafo completo próprio (banco de grafos / engine dedicada) | KG como banco de grafos real desde já, fechando H-001 "grafo real" | Raciocínio multi-salto nativo; escalável | **Fecha H-001 sem decisão de Andraus** (fora do mandato do Especificador); over-engineering provável sob VPS única/escritor único (research.md §3.5); custo operacional alto sem ganho exercido hoje | Economicidade ruim sem ganho de Eficácia atual; **só se Andraus optar e fechar H-001** |
| (C) Fundir/adiar | Fundir o KG na SPEC-004 (estado) **ou** adiar a SPEC-006 para depois da SPEC-007 (RAG) | Menos Specs agora | **Viola a separação constitutiva** "trabalho vs. permanente" (KERNEL-V2 l.1456-1467 "Nunca misturar"); slot referenciado por canônicos **não pode ser apagado** (INV-07); adiar desalinha a FASE 3 (KG é P0 fundacional, pré-requisito do Learning/Mission — KERNEL-V2 l.1484-1485) | Fere Eficácia (mistura responsabilidades / quebra dependência); rejeitada |

**Decisão proposta: (A) camada fina — a HOMOLOGAR por Andraus.** `SPEC-006-FORMA-001` resolvida na abertura quanto à **direção** (contrato cognitivo fechável; mecanismo físico aberto), **se Andraus confirmar**; o **mecanismo físico permanece H-001 (ABERTA)**. Opção B **registrada** (não apagada), adotável **somente** se Andraus decidir fechar H-001 como "grafo real". A recomendação do Especificador **não** fecha H-001 (CONS-01).

---

## 4. Quantidade — 1 Spec (com avaliação de divisão)

**Proposta: 1 Spec** (SPEC-006). Ontologia + entidades/relações + temporalidade + proveniência + lifecycle + consulta cognitiva + governança de escrita formam **um** contrato coeso de memória permanente; cabe em uma sessão de revisão (com D8 adversarial focado). **Avaliação de divisão (RULE-ECC-01):** considerei separar "ontologia/esquema" de "consulta/governança" — **rejeitado**, fragmentaria um contrato único e criaria dependência circular (consulta e governança pressupõem o esquema). Se, na redação do Plan, o volume exceder uma sessão de revisão (atomic-spec §5), proporei a Andraus uma divisão então (slot preservado, nunca apagado — INV-07). `SPEC-006-SPLIT-001`: **não dividir agora** (sujeito a Andraus; Q-ABERTURA-5).

---

## 5. Classe RULE-MECH-01 (CC-11) — orientação predominante

A SPEC-006 citará RULE-MECH-01 no Plan → CC-11 (declaração **por BASpec**, nunca por Spec inteira — SES-001 §50).
- Ontologia, catálogo de entidades/relações, temporalidade/validade, versionamento, consulta estruturada, dedupe de nó/relação = **Classe D (Determinístico)**.
- **Governança de escrita** (quem escreve; imutabilidade/append-only INV-07; gate de escrita no KG permanente) = **Classe C (Constitutivo)**, efeito **E2/E3** (escrita em memória **permanente** é commit de alto valor — piso E2; publicação crítica/irreversível no KG = E3 fail-closed; nível final por comportamento no Plan).
- Eventual juízo de **similaridade/causalidade** (sugerir relação) = **Classe H** (gate de saída determinístico que valida a relação proposta; **bounded loop + critério de parada** declarados por BASpec — RULE-MECH-03; respeita RULE-CAU: mecanismo obrigatório, nunca pós-hoc).

**Critério 4Es:** Eficácia primeiro — perder linhagem/versão ou aceitar deleção quebraria a reconstrução cognitiva (P13) e INV-07; por isso a escrita é append-only sob gate. Economicidade (não subir banco de grafos) nunca acima de Eficácia. Classe C reservada a risco alto (RULE-MECH-02).

---

## 6. Princípios de Domínio (RULE-PD-01 / CC-12) — **NÃO incide**

A SPEC-006 **não** é Spec de especialidade de escola (Elliott/SMC/ICT): é infraestrutura de memória, agnóstica de escola (armazena conhecimento de qualquer escola como nós/relações). **Nenhum `PD-xx` será proposto** (determinação análoga à SPEC-004/005/002). A Classe (CC-11, §5) é declarada; CC-12 fica N/A por ausência de domínio de especialidade.

---

## 7. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação na abertura | Nota |
|---|---|---|
| CC-01 | OK | KG é agnóstico de escola; não altera a hierarquia Elliott→…→ICT (apenas a representa como relações/HERDA). |
| CC-02 | **Aplica — foco** | Não redefinir CHM-001/CEM-001/CCM-001 **nem SPEC-004/005** (BASELINE); entidades **referenciadas**, não redefinidas; o KG **cumpre** as responsabilidades que o CEM-001 já lhe atribui (l.608-615). |
| CC-03 | OK | Não computa convicção; "confiança de relação" ≠ Convicção (INV-04); J-001/N-001 abertas; não toca WF-D03. |
| CC-04 | OK | Nenhuma das 5+5 Salvaguardas violada; custo/score nunca entram em convicção (INV-04). |
| CC-05 | **Aplica — reconciliar** | CRITICAL declarado (ROADMAP §6) vs. MEDIUM (atomic-spec §3) — ver §1 e Q-ABERTURA-2. |
| CC-06/07 | Diferido ao Plan | Engineering Cards com campos SES-001 §59 + cadeia §60. |
| CC-08 | **Aplica — foco** | Bloco Herança/Delta no Plan: INHERITS = CEM-001 (responsabilidades do KG, l.608-615, ID+versão), CHM-001 (estados/versionamento), RULE-BB-004/INV-07 (append-only/imutabilidade), SPEC-004 (log/proveniência por referência), SPEC-005 (eventos de ciclo de vida), SAS-001 §6.12 (consulta ao KG), CEE-001 l.111 (métrica de calibração). REMOVED vazio. Nenhum ADDED contradiz o herdado (RULE-HD-02). |
| CC-09 | **Aplica** | Mecanismo físico = **INDETERMINADO** até H-001; relações causais exigem mecanismo (RULE-CAU, não pós-hoc); sem falsa precisão em "confiança"; H-001 declarada aberta, não como fato. |
| CC-10 | Aplica | Declarar acepção: **Conhecimento permanente** (KG) vs **memória de trabalho** (Blackboard/SPEC-004) vs **documento recuperado** (RAG/SPEC-007) vs **Observação** (Skill, INV-06); "confiança de relação" (KG) vs "Convicção" (CCM-001). |
| CC-11 | Aplica (§5) | Classe por BASpec no Plan; C compatível com E2/E3; D determinístico; H com bounded loop + gate de saída. |
| CC-12 | **NÃO incide** (§6) | SPEC-006 não é de especialidade de domínio. |

---

## 8. Dependências, decisões abertas e encaminhamento de H-001 (CONS-01 — não fechar)

- **H-001 (mecanismo físico do KG) — [DECISÃO NECESSÁRIA — permanece ABERTA; só Andraus].** A SPEC-006 pode fechar o **contrato cognitivo** com o mecanismo físico **INDETERMINADO** (Opção A), **ou** Andraus pode optar por fechar H-001 agora. A **direção** é decisão de abertura (Q-ABERTURA-3); o **fechamento** é dele. O Especificador **não** fecha H-001 (research.md §8).
- **SPEC-004 (BASELINE)** — construir **sobre** (log durável, proveniência, estados); não redefinir (CC-02/INV-09). KG = memória **permanente**, Blackboard = **trabalho** ("Nunca misturar" — KERNEL-V2 l.1467).
- **SPEC-005 (BASELINE)** — o KG **consome/emite** eventos de ciclo de vida (CEM-001 l.600); não redefine o transporte.
- **SPEC-007 (RAG/Knowledge Formation)** — fronteira: KG recebe conhecimento **publicado**; formação/validação/retrieval é SPEC-007 — **não absorver**.
- **CHM-001/CEM-001/CCM-001 (baselined)** — entidades referenciadas, não redefinidas (CC-02); o KG cumpre as responsabilidades do CEM-001 (l.608-615).
- **CONSTITUTION l.233 (EC-COG-003)** / **SAS-001 §6.12** / **CEE-001 l.111** — âncoras do KG; conformar-se, não reescrever (INV-09).
- **WORKFLOW.md** (vigente) — conformar-se; citar por ID os `WF-xx` tocados no Plan (consulta cognitiva na formação de contexto); **não** fechar WF-D03.
- **Ontologia como componente separado** (KERNEL-V2 l.1488-1507) — **[DECISÃO NECESSÁRIA leve]** recomendo ontologia enxuta DENTRO da SPEC-006 (§3.6 research); criar componente novo é de Andraus (Q-ABERTURA-4). Sem criar slot novo nesta abertura.
- **Abertas (não fechar):** H-001, G-001, M-001, J-001, N-001, K-001, WF-D03, C-001 (granularidade EARS — relevante a relações multi-condição).

**Tratamento dos itens do RMR-001 (o Especificador NÃO promove — CONS-01):**
- **BL-003** (persistência física de hipótese/estado; `Em espera`, gatilho `spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação`) — a abertura da SPEC-006 **satisfaz o ramo `spec:SPEC-006`**. **Encaminhamento proposto:** a parte **física** do BL-003 **É** H-001/G-001 (abertas) → a SPEC-006 **referencia**, **não absorve nem fecha**. *(Precedente SPEC-004: "em redação" foi lido como disparo no **início do Plan**, não na abertura — DHR-SPEC004-001; registro ambas as leituras e deixo a promoção a Andraus/Controlador no passo 11-bis — fail-closed.)*
- **BL-011** (MC-EXP-001, fonte de requisitos de SPEC-004/006/009/018; `Em espera`, gatilho inclui `spec:SPEC-006 em redação`) — **Encaminhamento proposto:** usar como **insumo de requisitos** (ref. externa, K-MAN-15), aplicando os tratamentos COL-EXP-01..05 já homologados (CONFLICT-MAP; prevalece SOT canônico; imutabilidade REFORÇA RULE-BB-004/INV-07). Classificação ≠ aplicação; **não promovo**.
- **BL-010** (MC-RAG-001; gatilho `milestone:FASE 3 iniciada`) — a abertura **inicia a FASE 3**; mas BL-010 é fonte de requisitos da **SPEC-007**, não da 006 → registrar como **tangente**; gate/Andraus decidem se o ramo `milestone` é disparado. **Não promovo.**

---

## 9. Itens RMR-001 e comandos a rodar (o Especificador não promove — CONS-01)

- **Nenhum item do RMR-001 tem gatilho `spec:SPEC-006` homologado isoladamente**; a abertura **satisfaz ramos de gatilho** de **BL-003** (`spec:SPEC-006`), **BL-011** (`spec:SPEC-006`) e possivelmente **BL-010** (`milestone:FASE 3 iniciada`) — **tratados no passo 11-bis** (§8). O Especificador **não** promove nem encaminha (gate + Andraus).
- **ATIVADO pré-existente independente desta abertura:** **BL-029** (proveniência/falso-DENY — SPEC-004; DHR-ERRATA-001). Não o promovo.
- **Comandos a rodar (não tenho Bash — listo para o operador/Controlador):**
  - `python scripts/check_repo_research.py specs/features/SPEC-006` (RULE-ECC-06 — deve passar com 4 elegíveis)
  - `python scripts/build_map.py` **e** `python scripts/build_map.py --check` (BL-019 — mapa em dia após criar `specs/features/SPEC-006/`)
  - `python scripts/check_doc_sync.py` (drift documental — informativo; **espera-se** que aponte H-001 e os BL-003/010/011 como itens cujos gatilhos a abertura satisfaz — matéria de auditoria do Revisor / decisão de Andraus)
  - `python scripts/backlog_triggers.py` (gatilhos do RMR-001 — confirmar quais ramos a abertura dispara)

---

## 10. Riscos

- **R-1 (over-engineering — banco de grafos por inércia):** o nome "Graph" e o fundamento histórico (ENGENHARIA-GERAL l.3588-3662) puxam para a Opção B. **Contenção:** o próprio fundamento rejeita "banco de dados" (KERNEL-V2 l.1103); o Plan declara "contrato cognitivo primeiro, mecanismo físico = H-001 aberto"; B só se Andraus fechar H-001.
- **R-2 (fechar H-001 por engano):** a pressão de "especificar o KG" pode levar a fechar o mecanismo físico sem Andraus. **Contenção:** H-001 fica **[DECISÃO NECESSÁRIA]**; o contrato cognitivo é fechável **sem** fechar H-001 (Opção A).
- **R-3 (invadir a SPEC-007/RAG):** especificar formação/retrieval de conhecimento. **Contenção:** Non-goal explícito; KG recebe conhecimento **publicado**; `Documento recuperado ≠ conhecimento validado` é SPEC-007.
- **R-4 (reabrir/duplicar SPEC-004/005):** especificar memória de trabalho ou transporte. **Contenção:** CC-02 foco; "Nunca misturar" (KERNEL-V2 l.1467); fronteiras §2.
- **R-5 (confiança virar Convicção):** a pauta lista "confiança" e "relações estatísticas". **Contenção:** INV-04 explícito — confiança de relação ≠ Convicção; não tocar J-001/N-001.
- **R-6 (deleção disfarçada de "esquecimento"):** o estado da arte fala em "forgetting" (research.md §3.6). **Contenção:** INV-07 — esquecimento = arquivamento/rebaixamento versionado, nunca deleção.
- **R-7 (causalidade pós-hoc):** relações causais sem mecanismo. **Contenção:** RULE-CAU (EUA-E09) — mecanismo obrigatório; alvo de D8 adversarial.
- **R-8 (ontologia inconsistente ao longo do tempo):** acúmulo de conhecimento incoerente (KERNEL-V2 l.1505). **Contenção:** ontologia enxuta com regras de integridade; governança de escrita (Classe C/E3).

---

## 11. Edições a documentos de governança — NÃO executadas pelo Especificador
*(O Especificador não edita ROADMAP/CATALOGO/RMR-001/WORKFLOW/agentes — AGENTS.md §5.)* Esta abertura **não** altera nenhum documento normativo. Após homologação, o Controlador/Andraus registram o estado (ROADMAP, CATALOGO, RMR-001 passo 11-bis) e decidem a promoção/encaminhamento de BL-003/BL-010/BL-011. Nenhum modelo canônico baseline tocado (CONST-01). Nenhuma Spec baselined reescrita (INV-09). **H-001 NÃO é fechada** (CONS-01).

---

## 12. Perguntas a Andraus (decisão de abertura) — em linguagem de trader

> **Contexto em uma frase:** a "mesa de trabalho" do sistema (onde as ideias vivas são montadas durante a análise) já está pronta (SPEC-004). A SPEC-006 é a **memória de longo prazo** — o "caderno permanente" onde o que o sistema **já aprendeu e confirmou** (padrões, hipóteses resolvidas, lições, como as coisas se ligam) fica guardado para sempre, de forma auditável e nunca apagada.

1. **Q-ABERTURA-1 (nome):** O nome "Knowledge Graph" já descreve bem o que é — um caderno de conhecimento com as ligações entre as coisas. Diferente do caso anterior (Event Bus), **não** recomendo renomear. **Confirma manter "Cognitive Knowledge Graph"?** *(Recomendação: manter.)*

2. **Q-ABERTURA-2 (peso da Spec):** Dois documentos internos divergem: a tabela de método trata o Knowledge Graph como item "médio", mas o road map o marca como "crítico". Como esse caderno guarda a memória permanente e **nunca pode apagar nada** (regra dura do sistema), recomendo tratá-lo como **crítico**. **Confirma CRITICAL (com rigor adversarial extra nos pontos sensíveis), seguindo o road map?** *(Recomendação: CRITICAL.)*

3. **Q-ABERTURA-3 (a grande decisão — como guardar):** Há uma pergunta antiga em aberto (H-001): o caderno deve ser um **banco de grafos de verdade** (infraestrutura pesada) ou uma **camada leve** montada sobre o que já guardamos hoje? Recomendo **fechar agora só as REGRAS do caderno** (o que ele guarda, como se consulta, quem pode escrever, nunca apagar) e **deixar a tecnologia de armazenamento em aberto** (decidir depois, quando houver necessidade real) — assim não gastamos com infraestrutura pesada que a sua VPS única não precisa ainda. **Aceita fechar as regras e deixar a tecnologia (H-001) em aberto?** *(Recomendação: sim, Opção A. Eu não posso fechar H-001 — é decisão sua.)*

4. **Q-ABERTURA-4 (gramática do conhecimento):** Um documento antigo sugeria um componente separado só para a "gramática" do conhecimento (o que cada conceito significa e que ligações são permitidas). Recomendo manter essa gramática **dentro** da própria SPEC-006, enxuta, sem criar uma peça nova. **Confirma gramática dentro da SPEC-006, sem componente separado?** *(Recomendação: sim.)*

5. **Q-ABERTURA-5 (uma Spec só):** Recomendo manter **uma única** Spec (regras + ligações + consulta + governança de escrita juntas). Se na hora de detalhar ficar grande demais para revisar de uma vez, eu volto para você propor dividir. **Confirma uma Spec só por enquanto?** *(Recomendação: sim; nada é apagado se dividirmos depois.)*

> **Estas 5 perguntas aguardam decisão de Andraus na HOMOLOGAÇÃO da abertura.** Nenhuma decisão aberta é fechada aqui (CONS-01): em particular, **H-001 permanece ABERTA**; G-001, M-001, J-001, N-001, K-001, WF-D03 idem.

---

## 13. Próximo passo
Com o Dossiê (`research.md`), as capturas (`sources/`) e esta Proposta prontos, o conjunto segue para **parecer do Revisor** sobre o processo do Dossiê (atomic-spec §15; RULE-ECC-04 verbatim; RULE-ECC-06 repositórios — 4 elegíveis; RULE-ECC-05 não-incidência a confirmar) e, em seguida, **homologação de Andraus** da **definição da Spec** (número, nome, CRITICAL, D0–D7+D8 adversarial, quantidade=1, direção Opção A, Classe, não-incidência de CC-12/ECC-05) e das **5 perguntas de abertura**, **antes** de qualquer `plan.md`/`checks.md`. Decisões abertas incidentes (H-001, G-001, M-001, J-001, N-001, K-001, WF-D03) **permanecem abertas** (CONS-01).

**Pronto para revisão.**
