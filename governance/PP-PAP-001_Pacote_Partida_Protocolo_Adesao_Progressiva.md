# PP-PAP-001 — Pacote de Partida do PAP-001

**Briefing de escopo, contexto e restrições para o Especificador Principal produzir o PAP-001 — Protocolo de Adesão Progressiva da Camada de Princípios do SOT**

| Campo | Valor |
|---|---|
| ID | PP-PAP-001 (pacote de partida; não é o protocolo) |
| Alvo | PAP-001 — Protocolo de Adesão Progressiva ao GPR-001 |
| Tipo | Documento de Governança de Princípios (não é SPEC de componente) |
| Prioridade | P0 — pré-condição para SPEC-001+ ser escrita com rastreabilidade principiológica |
| Posição no caminho crítico | Antes do SPEC-001; paralelo à homologação do GPR-001 |
| Emitido por | Andraus + Revisor (necessidade conjunta identificada em sessão de 2026-09-15) |
| Autoridade normativa | GPR-001 v1.0, Unidade Atômica v1.2 (HOMOLOGADA), GEH-001, Road Map (HOMOLOGADO), HRE-001, GRE-001 |
| Natureza | Feedforward: define O QUÊ cobrir e sob quais restrições; o Especificador escreve o conteúdo |

> **Como usar.** O Especificador executa o fluxo do PEP-001. Este pacote fixa o alvo, as fronteiras e os critérios de aceitação do PAP-001, reduzindo rodadas de revisão. Nada aqui é o protocolo: é o contrato de escopo contra o qual ele será verificado.

---

## 1. Contexto e Motivação

### 1.1 O problema de retrofit

O SOT atingiu o M0 (Unidade Atômica v1.2 homologada, Road Map baselined) com princípios distribuídos implicitamente entre invariantes constitucionais, specs de governança e diretivas de revisão. O GPR-001 (produzido em 2026-09-15) formalizou essa camada como um **Guia de Princípios, Relações e Organicidade** — 44 princípios em 6 classes, com dinâmicas, eixos de tensão, matrizes de conflito e algoritmo cognitivo.

O problema imediato: o GPR-001 chegou **após** specs e documentos já homologados. Aplicá-lo retroativamente em sua totalidade paralisaria o projeto. Ignorá-lo tornaria cada nova spec principiologicamente inconsistente com as anteriores.

Este é o problema canônico de **governance retrofit**: integrar uma camada de governança por princípios a um sistema em andamento, sem quebrar o que já existe e sem perder a coerência futura.

### 1.2 O que o estado da arte diz (benchmark realizado em 2026-09-15)

A pesquisa comparou seis frameworks: NIST AI RMF, NIST Agentic Profile (AAGATE), ISO/IEC 42001, TOGAF ADM, SAFe, e o conceito de Policy/Architecture Debt. A convergência é clara:

**Achado 1 — Nenhum framework retroage wholesale.** Todos adotam adesão progressiva por criticidade. O NIST AI RMF define 4 tiers de maturidade (Partial → Risk-Informed → Repeatable → Adaptive) e afirma explicitamente que existem "múltiplas trajetórias legítimas" — não há caminho único prescrito. O SOT já está no Tier 2 (Risk-Informed) e deve visar o Tier 3 (Repeatable) com o PAP-001.

**Achado 2 — O padrão universal é o chokepoint único de enforcement.** O NIST Agentic Profile (AAGATE) define três componentes para sistemas agênticos: Governing-Orchestrator, Shadow-Monitor e Tool-Gateway Chokepoint. No SOT, o **Revisor de Especificação já é esse chokepoint**. O PAP-001 equipa esse chokepoint com o GPR-001 como checklist operacional, diferenciado por classe de princípio.

**Achado 3 — Governance debt é mensurável e pago progressivamente.** O conceito de "policy debt" (GovLoop, EAPJ) estabelece que o custo de governança acumulada deve ser inventariado como um KPI e pago em ciclos regulares ("policy hygiene cycles"), não de uma vez. O PAP-001 deve incluir um inventário vivo de conformidade e um ciclo de revisão definido.

**Achado 4 — A estrutura canônica de um princípio é quadripartite (TOGAF/EA Wheel).** Cada entrada de princípio tem: Name, Statement, Rationale, Implications. O GPR-001 já segue essa estrutura nas fichas de exemplo. O PAP-001 deve consolidar isso como padrão obrigatório para qualquer novo princípio adicionado.

**Achado 5 — Decisões arquiteturais têm ciclo de vida próprio (ADR pattern).** Architecture Decision Records (Martin Fowler, UK Gov) estabelecem que decisões não são apagadas — são supersedidas. O ciclo é: Proposed → Active → Deprecated → Superseded. Os open decisions do SOT (J-001, B-001, G-001 etc.) devem ser gerenciados pelo mesmo padrão. O PAP-001 define como princípios e decisões co-evoluem.

**Achado 6 — A sequência GOVERN→MAP→MEASURE→MANAGE é o padrão para sistemas agênticos.** O NIST Agentic Profile define 4 fases de integração progressiva. O SOT já completou substancialmente GOVERN e MAP. MEASURE chegará com os specs de Observabilidade (fases 10–11 do Road Map). MANAGE é a fase de Metacognição (SPEC-024). O PAP-001 não pode prescrever MEASURE ou MANAGE agora — apenas referenciá-los como fases futuras.

### 1.3 A lacuna que o PAP-001 fecha

Sem o PAP-001:
- O Revisor não tem protocolo formal para aplicar GPR-001 diferentemente por classe de princípio
- Não existe critério explícito de o que é retroativo vs. prospectivo
- Não existe inventário de conformidade das specs existentes (governance debt não quantificado)
- Não existe ciclo de revisão do próprio GPR-001 (princípios podem derivar sem mecanismo de atualização)
- Novos princípios do Manual Universal podem ser incorporados sem critério de prioridade

---

## 2. Escopo obrigatório (o que o PAP-001 DEVE cobrir)

O PAP-001 é um **protocolo de governança de princípios**, não uma BASpec de componente técnico. Sua linguagem é normativa, não implementacional. Deve cobrir, no mínimo:

### 2.1 Classificação de aplicabilidade por classe de princípio

Definir explicitamente, para cada uma das 6 classes do GPR-001 (PC, PB, PE, PCO, PO, PS), o regime de aplicação:

- **Regime retroativo-como-auditoria:** aplica apenas como verificação de gap em specs existentes, sem obrigação de reescrita. Gaps tornam-se open decisions no registro de conformidade.
- **Regime prospectivo-obrigatório:** aplica a todas as specs produzidas a partir da data de homologação do PAP-001. O Revisor usa como gate.
- **Regime ativado-por-contexto:** aplica quando o contexto da spec aciona o princípio; não é gate eliminatório mas é critério de qualidade verificado pelo Revisor.

### 2.2 O 5W2H do processo de integração

Formalizar:

| Eixo | Conteúdo a especificar |
|---|---|
| **What** | Quais princípios do GPR-001 são operativos agora; quais do Manual Universal são candidatos a incorporação futura e por qual critério |
| **Who** | Especificador propõe; Revisor verifica conformidade por classe; Andraus homologa princípios novos ou supersedidos |
| **When** | Critério temporal por classe (retroativo-auditoria / prospectivo / ativado-por-contexto); gatilho para incorporar princípio novo do Manual |
| **Where** | Verificado no gate de revisão (Revisor); registrado no Inventário de Conformidade; atualizado no GPR-001 |
| **Why** | Manter identidade do SOT enquanto a camada principiológica amadurece; evitar governance drift e governance paralysis |
| **How** | GPR-001 como checklist do Revisor; Inventário de Conformidade como living document; ciclo de hygiene periódico |
| **How much** | Esforço proporcional: retroativa leve (apenas classe PC); prospectiva completa (todas as classes para specs novas); hygiene trimestral por padrão |

### 2.3 Inventário de Conformidade (living document)

Definir o schema do Inventário de Conformidade — tabela de cada spec/documento normativo existente vs. cada classe de princípio do GPR-001, com status por célula:

- **PASS** — spec atende os princípios da classe
- **FLAG** — tensão identificada; não invalida a spec, mas registra como item de atenção
- **GAP** — princípio da classe aplicável não coberto; gera open decision no registro

O inventário inicial cobre os documentos já homologados (M0): Unidade Atômica v1.2, GEH-001, Road Map, e as emendas anteriores.

### 2.4 Ciclo de Hygiene de Princípios

Definir:
- Frequência do ciclo de revisão do GPR-001 e do Inventário de Conformidade
- Gatilhos de revisão extraordinária (nova milestone homologada, novo princípio proposto, decisão aberta J-xxx resolvida que afeta princípio)
- O que constitui uma proposta de novo princípio vs. refinamento de princípio existente
- O que constitui supersessão de princípio (e que a supersessão não deleta — cria registro histórico)

### 2.5 Critério de incorporação de novos princípios do Manual Universal

O Manual Universal de Engenharia de Princípios Agênticos v2.0 contém princípios adicionais não mapeados no GPR-001 v1.0. O PAP-001 deve definir:
- Critério de relevância para o SOT (teste de pertinência à arquitetura cognitiva de trading)
- Quem propõe, com qual formato de proposta (ficha de princípio + justificativa + impacto em specs existentes)
- Gate de homologação antes de qualquer princípio novo entrar no GPR-001

### 2.6 Protocolo de operacionalização do Revisor

O Revisor já usa GRE-001 e HRE-001. O PAP-001 acrescenta:
- Checklist diferenciado por classe de princípio para uso na revisão
- Instrução de como reportar gaps de princípio no parecer (CONFORME / CONFORME condicional / NÃO CONFORME com achado ancorado em GPR-001)
- Critério para distinguir violação de princípio constitucional (gate eliminatório) de não-cobertura de princípio cognitivo/situacional (item de melhoria)

---

## 3. Fronteiras — o que o PAP-001 NÃO pode fechar

### 3.1 Não define a fórmula de convicção (J-001 aberto)
O PAP-001 pode referenciar o PC-04 (conviction floor: Estrutural≥60%, total≥75%) como princípio constitucional retroativo, mas a fórmula de cálculo é J-001 — não fechar aqui.

### 3.2 Não reescreve specs existentes
O PAP-001 mapeia gaps (Inventário de Conformidade), mas não produz emendas. Emendas são trabalho do Especificador, acionadas por decisão de Andraus após revisão do inventário.

### 3.3 Não define os mecanismos de persistência ou transporte de princípios
O princípio vive no GPR-001 (documento normativo). Como o sistema agente acessa e usa princípios em runtime é responsabilidade das SPEC-004 (Blackboard), SPEC-009 (Cognitive State) e SPEC-024 (Metacognição).

### 3.4 Não cobre Skills como unidades formais (I-001 aberto)
A questão de como Skills operam conforme princípios em runtime é derivada de I-001 e das specs de Skills downstream.

### 3.5 Não prescreve MEASURE e MANAGE da sequência NIST Agentic
Esses estágios chegam com os specs de Observabilidade (fases 10–11) e Metacognição (SPEC-024). O PAP-001 pode mencionar a sequência como contexto arquitetural, mas não antecipar esses estágios.

---

## 4. Invariantes que incidem no PAP-001

- **INV-01/02** — a hierarquia Elliott→Fibonacci→Fractal→SMC→ICT é constitucional. O PC-01 do GPR-001 mapeia diretamente. O PAP-001 não pode classificar PC-01 como retroativo-opcional.
- **INV-07** — versionamento monotônico. Supersessão de princípio segue a mesma regra: nunca deleta, sempre versiona.
- **INV-08/09** — transcrição literal e sem baseline informal. O PAP-001 não pode criar classes de conformidade sem ancoragem em texto homologado.
- **4Es (PB-01..PB-04)** — qualquer ciclo de hygiene ou gate de revisão de princípio aplica a hierarquia Eficácia→Efetividade→Eficiência→Economicidade. O PAP-001 não inverte essa hierarquia ao definir critérios de proporcionalidade.
- **Separação SOT/Bot (PC-02)** — o PAP-001 não pode criar princípios que atribuam execução de ordem ao SOT.
- **CEM-001 como idioma canônico (PC-05)** — qualquer novo princípio proposto não pode redefinir CEM-001.

---

## 5. Fontes a consultar (com classificação obrigatória)

**Internas (autoridade maior→menor):**
- GPR-001 v1.0 (proposta, aguarda homologação) — fonte primária do conteúdo a protocolar
- Unidade Atômica v1.2 (HOMOLOGADA) — modelo de estrutura e profundidade
- PP-SPEC-001 (HOMOLOGADO) — modelo de pacote de partida a seguir
- GRE-001 / HRE-001 (HOMOLOGADOS) — protocolo do Revisor que o PAP-001 estende
- Road Map (HOMOLOGADO) — posição do PAP-001 no caminho crítico
- GEH-001 (HOMOLOGADO) — 4Es como função objetivo; anti-padrões de centralização/descentralização
- Manual Universal de Engenharia de Princípios Agênticos v2.0 (referência externa não-normativa)

**Externas (benchmark de estado da arte — classificar cada fonte):**
Temas verificados e classificação recomendada:

| Fonte | Classificação |
|---|---|
| NIST AI RMF — 4 tiers de maturidade (arxiv.org/2401.15229) | Padrão |
| NIST Agentic Profile / AAGATE (Cloud Security Alliance) | Padrão |
| TOGAF ADM — Principles Catalog e 7 passos (visual-paradigm.com) | Prática |
| EA Wheel — estrutura quadripartite de princípio | Prática |
| Architecture Decision Records — ciclo de vida de decisões (reflectrally.com, martinfowler.com) | Prática |
| Policy Debt — inventário vivo e hygiene cycles (govloop.com) | Benchmark |
| Architecture Debt KPI framework (eapj.org) | Benchmark |
| ISO/IEC 42001 — PDCA aplicado a AI governance | Padrão |
| SAFe — 10 princípios imutáveis integrados | Benchmark |
| EU AI Act — risk-tiered approach com fases de compliance | Padrão |

Classificar cada fonte usada no PAP-001 com um dos rótulos: `Padrão / Prática / Benchmark / Evidência / Experimento / Opinião`. Nenhuma fonte externa entra automaticamente — confrontar com a arquitetura do SOT antes de incorporar (ROAD-01).

---

## 6. Estrutura de entrega esperada (o que submeter ao Revisor)

O PAP-001 não é uma BASpec técnica — é um protocolo de governança. Sua estrutura de entrega:

1. **Cabeçalho** — ID, versão, status (PROPOSTA), autoridade normativa, data.
2. **Escopo e objetivo** — o que o PAP-001 governa e o que está fora do seu escopo.
3. **Classificação de aplicabilidade** — tabela de regimes por classe de princípio (§2.1), fundamentada no GPR-001.
4. **5W2H formalizado** — cada eixo com conteúdo prescritivo, não descritivo (§2.2).
5. **Schema do Inventário de Conformidade** — tabela schema + status possíveis + instruções de preenchimento (§2.3); o inventário inicial preenchido para os documentos M0.
6. **Ciclo de Hygiene** — definições de frequência, gatilhos, responsáveis, output esperado (§2.4).
7. **Critério de incorporação de novos princípios** — teste de pertinência + formato de proposta + gate de homologação (§2.5).
8. **Protocolo do Revisor** — checklist diferenciado por classe, instrução de reporte (§2.6).
9. **Decisões abertas** — listagem com código K-PAP-xxx das questões não resolvidas que devem subir a Andraus.
10. **Critérios de aceitação** — como o Revisor verificará se o PAP-001 é CONFORME.
11. **Encerrar com** "Pronto para revisão".

---

## 7. Critérios de aceitação do PAP-001 (o que o Revisor exigirá)

O PAP-001 será considerado CONFORME quando:

- Nenhum invariante do §4 violado.
- A classificação de aplicabilidade (§2.1) cobre todas as 6 classes do GPR-001 com regime explícito e justificado.
- O 5W2H (§2.2) é prescritivo — cada eixo define um comportamento ou critério verificável, não uma descrição.
- O Inventário de Conformidade (§2.3) tem schema completo e o inventário inicial dos documentos M0 preenchido.
- O ciclo de Hygiene (§2.4) define frequência, gatilhos e responsáveis sem ambiguidade.
- O critério de incorporação de novos princípios (§2.5) é objetivo — admite decisão sem consulta adicional a Andraus para casos típicos.
- O protocolo do Revisor (§2.6) é operacionalizável — o Revisor pode aplicar sem interpretação adicional.
- Todas as fontes externas estão classificadas com o rótulo de status epistemológico.
- As decisões abertas listadas em §8 estão marcadas [DECISÃO NECESSÁRIA] no corpo do protocolo.
- Nenhuma decisão aberta do SOT (J-001, B-001 etc.) foi usada como invariante fechado.
- O PAP-001 não abre escopo para SPEC-004, SPEC-009 ou SPEC-024 — apenas referencia.
- Rastreabilidade completa: todo critério tem ancoragem em GPR-001, Unidade Atômica ou benchmark classificado.

---

## 8. Decisões abertas que devem subir a Andraus (marcar [DECISÃO NECESSÁRIA])

O Especificador não resolve estas sozinho:

**K-PAP-001 — Localização do Inventário de Conformidade**
O inventário de conformidade é um documento separado (CIC-001) ou uma seção viva do GPR-001? Impacto: se separado, requer próprio ciclo de versão e manutenção; se embutido, o GPR-001 muda a cada revisão de spec.

**K-PAP-002 — Frequência do ciclo de Hygiene**
O ciclo de Hygiene é trimestral, por milestone, ou acionado apenas por evento (nova spec homologada, decisão aberta resolvida)? A frequência fixa é mais previsível; a orientada a evento é mais econômica.

**K-PAP-003 — Autoridade de proposta de novo princípio**
Somente Andraus pode propor novos princípios, ou o Especificador pode propor com Andraus homologando? Se o Especificador pode propor, qual é o formato mínimo exigido?

**K-PAP-004 — Escopo de aplicação do PAP-001**
O PAP-001 aplica apenas a BASpecs e specs de componente, ou também a documentos de governança (GRE-001, HRE-001, GEH-001) quando revisados?

**K-PAP-005 — Tratamento dos open decisions existentes sob o PAP-001**
Os open decisions já catalogados (J-001, B-001, G-001, H-001, I-001, K-001, L-001, C-001) devem ter sua relação com os princípios do GPR-001 mapeada no Inventário de Conformidade? Isso define se o inventory abrange apenas specs ou também decisões em aberto.

---

## 9. Relação com o SPEC-001 (caminho crítico)

O PAP-001 **não bloqueia** o início da redação do SPEC-001. O Especificador pode escrever o SPEC-001 em paralelo. Porém, o SPEC-001 **não pode ser homologado por Andraus antes do PAP-001**, pois o gate de revisão definitivo do SPEC-001 usará o protocolo do Revisor expandido pelo PAP-001.

Benefício estratégico: o SPEC-001 será o **primeiro teste real** do PAP-001. Escrever ambos em paralelo e revisá-los juntos é a forma mais econômica de validar a conformidade entre o protocolo e a prática.

---

## 10. Definition of Done do handoff

Este pacote está "entregue" quando o Especificador tiver:
- (a) o problema e contexto completos (§1)
- (b) o escopo obrigatório e o 5W2H a formalizar (§2)
- (c) as fronteiras do que não pode ser fechado (§3)
- (d) os invariantes incidentes (§4)
- (e) as fontes classificadas (§5)
- (f) a estrutura de entrega esperada (§6)
- (g) os critérios que o Revisor aplicará (§7)
- (h) as decisões abertas a expor (§8)

A partir daqui, o Especificador produz o PAP-001 pelo fluxo do PEP-001. Ao receber "Pronto para revisão", o Revisor emite o parecer. Somente Andraus homologa antes de incorporar o PAP-001 como normativo.

---

*Fim do PP-PAP-001 v1.0 — 2026-09-15. Não é o PAP-001 — é o contrato de escopo que o antecede. Alinhado a GPR-001 v1.0 (proposta), PEP-001, GRE-001, HRE-001 e às baselines Unidade Atômica + Road Map (homologadas em 2026-09-12).*
