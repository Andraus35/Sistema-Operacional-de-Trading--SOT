# PAP-001 — Protocolo de Adesão Progressiva da Camada de Princípios do SOT

| Campo | Valor |
|---|---|
| ID | PAP-001 |
| Versão | 1.2 — **HOMOLOGADO — BASELINE** (Andraus, 2026-09-19, DHR-PAP-001-C). Dois conteúdos: (a) **Bloco 7** (Vínculo Principiológico em Tempo de Decisão) e (b) **wiring RMR-001 no Bloco 4 §6.3** (consulta obrigatória ao backlog). Parecer Revisor CONFORME. v1.0/v1.1 preservadas sem deleção (INV-07). |
| Tipo | Documento de Governança de Princípios (não é BASpec de componente) |
| Autor | Especificador Principal do SOT (via skill `sot-especificador-pap001`, Bloco A do PE-PR-PAP-001 v1.1 HOMOLOGADO) |
| Autoridade normativa | PEP-001 v1.2 · GPR-001 v1.0 · PP-PAP-001 v1.0 · atomic-spec v1.3 · GEH-001 v1.1 · GRE-001 v2.2 · HRE-001 v2.2 |
| Data | 2026-09-15 |
| Fluxo | Especificador (autor) → Revisor (PRE-001 v1.1 / Bloco B) → Andraus (homologa e resolve K-PAP-001..005) |

> **Status epistemológico global (TRACE-06):** este protocolo é BASELINE HOMOLOGADO a partir de 2026-09-15 (DHR-PAP-001-B). **Exceção:** as células RULES e CONFLICT-MAP do Inventário M0 (§5.4) permanecem `[INFERÊNCIA]` — não são FATO NORMATIVO até a auditoria integral no 1º ciclo de Hygiene (achado M-01 do Revisor, acatado).

---

## 1. Escopo e objetivo

### 1.1 O que o PAP-001 governa
`[FONTE: PP-PAP-001 §1, §2]`

O PAP-001 define **como os 44 princípios do GPR-001 (6 classes) se tornam operativos no SOT de forma progressiva** — sem paralisar o projeto (governance paralysis) e sem perder coerência principiológica entre specs anteriores e futuras (governance drift). Ele resolve o problema canônico de **governance retrofit**: uma camada de princípios (GPR-001) que chegou depois de documentos já homologados no M0.

O PAP-001 entrega cinco mecanismos:
1. Um **regime de aplicabilidade por classe** (retroativo-auditoria / prospectivo-obrigatório / ativado-por-contexto) — Bloco 1.
2. Um **processo 5W2H** prescritivo de integração — Bloco 2.
3. Um **Inventário de Conformidade** vivo (schema + inventário M0) — Bloco 3.
4. Um **Ciclo de Hygiene de Princípios** — Bloco 4.
5. Um **critério de incorporação de novos princípios** + um **protocolo do Revisor** diferenciado por classe — Blocos 5 e 6.

### 1.2 O que está fora do escopo
`[FONTE: PP-PAP-001 §3]`

O PAP-001 **não**: (a) fecha a fórmula do Conviction Vector (J-001 aberto); (b) reescreve specs existentes (apenas mapeia gaps); (c) define persistência/transporte de princípios em runtime (SPEC-004/009/024); (d) trata Skills como unidades formais (I-001 aberto); (e) prescreve as fases MEASURE/MANAGE do NIST Agentic Profile (chegam com Observabilidade e Metacognição). Estes itens aparecem apenas como referência ou `[DECISÃO NECESSÁRIA]`.

### 1.3 Natureza normativa, não implementacional
`[FONTE: PP-PAP-001 §2, linha "não é BASpec" | atomic-spec v1.3]`

O PAP-001 não contém QUANDO/ENTÃO/PORQUE de runtime, state machine, nem profundidade D4–D7 de componente. Sua verificabilidade é: **prescritividade** (cada cláusula define comportamento verificável), **rastreabilidade** (âncora em GPR-001 §X ou benchmark classificado) e **completude** dos 6 blocos.

---

## 2. Alinhamento com o estado da arte
`[FONTE: PP-PAP-001 §1.2]`

O PAP-001 adota, confrontando com a arquitetura SOT (ROAD-01), seis achados de benchmark:

| Achado | Fonte | Classificação | Como o PAP-001 o usa |
|---|---|---|---|
| Nenhum framework retroage wholesale; adesão progressiva por criticidade | NIST AI RMF — 4 tiers | `[PADRÃO]` | Bloco 1 (regimes por classe). SOT no Tier 2, alvo Tier 3 |
| Chokepoint único de enforcement | NIST Agentic Profile / AAGATE | `[PADRÃO]` | O Revisor é o chokepoint; Bloco 6 o equipa com o GPR-001 |
| Governance debt inventariado e pago em ciclos | Policy Debt (GovLoop/EAPJ) | `[BENCHMARK]` | Bloco 3 (Inventário vivo) + Bloco 4 (Hygiene) |
| Estrutura quadripartite de princípio | TOGAF / EA Wheel | `[PRÁTICA]` | Bloco 5 (ficha Name/Statement/Rationale/Implications) |
| Decisão tem ciclo de vida; nunca deletada | ADR pattern (Fowler / UK Gov) | `[PRÁTICA]` | Bloco 4 (Proposto→Ativo→Deprecado→Supersedido; INV-07) |
| Sequência GOVERN→MAP→MEASURE→MANAGE | NIST Agentic Profile | `[PADRÃO]` | GOVERN/MAP cobertos; MEASURE/MANAGE fora de escopo (§1.2) |
| PDCA para governança de AI | ISO/IEC 42001 | `[PADRÃO]` | Bloco 4 (ciclo Plan-Do-Check-Act de hygiene) |
| Limite "less is more" (4–5 princípios/tier) | TOGAF ADM | `[PRÁTICA]` | Bloco 5 (limite de gestão) |

---

## 3. BLOCO 1 — Classificação de aplicabilidade por classe de princípio
`[FONTE: PP-PAP-001 §2.1 | GPR-001 §2 | NIST AI RMF — PADRÃO]`

O GPR-001 §2 define 44 princípios em 6 classes. O PAP-001 atribui a cada classe **um dos três regimes**. A tabela é normativa e exaustiva (cobre as 6 classes).

| Classe (GPR-001 §2) | Princípios | Regime | Quem verifica | Output esperado |
|---|---|---|---|---|
| **PC — Constitucionais** | PC-01..08 | **Retroativo-como-auditoria** (prospectivo permanece gate) | Revisor | Gap em spec existente → open decision no Inventário. Nova spec: violação = NÃO CONFORME Crítica |
| **PB — Basilares** | PB-01..10 | **Prospectivo-obrigatório** (a partir do SPEC-001) | Revisor (gate) | Gate de conformidade; violação registrada e justificada |
| **PE — Estruturais** | PE-01..08 | **Prospectivo-obrigatório** (a partir do SPEC-001) | Revisor (gate) | Gate de conformidade arquitetural |
| **PCO — Cognitivos** | PCO-01..07 | **Ativado-por-contexto** | Revisor (critério de qualidade) | Item de melhoria; não bloqueia se o contexto não aciona |
| **PO — Operacionais** | PO-01..07 | **Ativado-por-contexto** | Revisor (critério de qualidade) | Item de melhoria; PO-02/PO-03 elevam-se a gate quando há efeito E3 |
| **PS — Situacionais** | PS-01..04 | **Ativado-por-contexto** | Revisor (critério de qualidade) | Verificado só quando o contexto (urgência/cautela/exploração) é declarado |

### 3.1 Definição prescritiva de cada regime

**R1 — Retroativo-como-auditoria** (classe PC). `[FONTE: PP-PAP-001 §2.1 | GPR-001 §2.1]`
- **Definição:** os invariantes constitucionais (PC-01..08) já existiam implicitamente no M0 (co-extensivos aos invariantes homologados — GPR-001 §14). Aplicam-se a specs existentes **apenas como verificação de gap**, sem obrigação de reescrita.
- **Critério de aplicação:** toda spec/documento M0 é auditado célula-a-célula contra PC-01..08 no Inventário (Bloco 3).
- **Restrição inviolável:** PC-01 (hierarquia Elliott→ICT) e PC-02..PC-08 **nunca** podem ser classificados como "retroativo-opcional" — a auditoria não os relaxa; ela apenas não força reescrita imediata (INV-01/02). Em spec **nova**, PC-* é gate eliminatório.
- **Output:** gap PC → open decision (K-derivado) no Inventário; nunca emenda automática.

**R2 — Prospectivo-obrigatório** (classes PB, PE). `[FONTE: PP-PAP-001 §2.1, §2.6]`
- **Definição:** valem como gate para toda spec produzida a partir da homologação do PAP-001 (a começar pelo SPEC-001).
- **Critério de aplicação:** o Revisor verifica PB-01..10 e PE-01..08 no Constitution Check da spec (GPR-001 §15).
- **Output:** conformidade PASS obrigatória; violação de PB-* registrada e justificada (GPR-001 §14: "contradição com PB-xx deve ser registrada e justificada"); violação de PE-* é achado de arquitetura.

**R3 — Ativado-por-contexto** (classes PCO, PO, PS). `[FONTE: PP-PAP-001 §2.1 | GPR-001 §3.6 inversões contextuais]`
- **Definição:** aplicam-se **quando o contexto da spec os aciona** (ex.: PS-01 urgência só em janela de mercado crítica; PCO-02 contraevidência quando há hipótese). São critério de qualidade, não gate eliminatório.
- **Exceção elevatória:** PO-02 (fail-closed) e PO-03 (gate determinístico) tornam-se **gate** quando a spec tem efeito E3 (GPR-001 §3.5 gating) — não são opcionais nesse contexto.
- **Output:** item de melhoria (severidade Menor) quando não coberto; gate quando a exceção elevatória incide.

### 3.2 Regra de proporcionalidade (How much) do regime
`[FONTE: PP-PAP-001 §2.2 (How much) | 4Es GEH-001 §3.2]`
Esforço de auditoria proporcional (PB-08): **retroativa leve** (só PC-*, sem reescrita) < **prospectiva completa** (PC+PB+PE em spec nova) < **hygiene periódica** (todas as classes, Bloco 4). A ordem dos 4Es (Eficácia→…→Economicidade) nunca é invertida ao dimensionar esse esforço.

---

## 4. BLOCO 2 — 5W2H formalizado (prescritivo)
`[FONTE: PP-PAP-001 §2.2 | Andraus, necessidade declarada 2026-09-15]`

Cada eixo define comportamento verificável (não descrição).

| Eixo | Prescrição verificável |
|---|---|
| **What** | São operativos **agora** os 44 princípios do GPR-001 §2 (PC-01..08, PB-01..10, PE-01..08, PCO-01..07, PO-01..07, PS-01..04). Princípios do Manual Universal **não** são operativos até passarem pelo Bloco 5. Critério de adição futura: teste de pertinência (§7.1) + homologação de Andraus. |
| **Who** | **Especificador** propõe (spec e, se autorizado por K-PAP-003, princípio novo); **Revisor** verifica conformidade por classe (regime do Bloco 1) e reporta gap/violação; **Andraus** homologa spec, princípio novo, supersessão e resolução de gap. Nenhum outro papel homologa (PC-08). |
| **When** | Regime temporal por classe: PC = auditoria retroativa contínua + gate prospectivo; PB/PE = a partir da homologação do PAP-001; PCO/PO/PS = quando o contexto aciona. Gatilho para incorporar princípio novo do Manual: proposta aprovada no Bloco 5 → homologação de Andraus. |
| **Where** | **Verificado** no gate de revisão (Revisor, Bloco 6). **Registrado** no Inventário de Conformidade (Bloco 3). **Atualizado** no GPR-001 (via emenda homologada — GPR-001 §14). |
| **Why** | Manter a **identidade** do SOT (PC-01..08 intocados — GPR-001 §8.2) enquanto a camada principiológica amadurece: "manter identidade enquanto adapta comportamento" (GPR-001 §8, organicidade). Evita governance drift e governance paralysis (PP-PAP-001 §1). |
| **How** | GPR-001 como **checklist do Revisor** diferenciado por classe (Bloco 6); Inventário de Conformidade como **living document** (Bloco 3); Ciclo de Hygiene periódico (Bloco 4). |
| **How much** | Esforço proporcional (PB-08 / §3.2): retroativa leve → prospectiva completa → hygiene periódica, sempre na hierarquia 4Es (Eficácia primeiro, Economicidade por último). |

---

## 5. BLOCO 3 — Schema do Inventário de Conformidade + inventário inicial M0
`[FONTE: PP-PAP-001 §2.3 | Architecture Debt KPI — BENCHMARK | Policy Debt hygiene — BENCHMARK]`

### 5.1 Schema
Tabela bidimensional: **linhas** = cada spec/documento normativo; **colunas** = cada uma das 6 classes de princípio do GPR-001. Cada célula recebe um status.

### 5.2 Status possíveis (definição operacional)
| Status | Definição operacional |
|---|---|
| **PASS** | O documento atende os princípios da classe aplicáveis ao seu escopo; nenhuma tensão aberta. |
| **FLAG** | Tensão identificada; **não invalida** o documento, mas registra item de atenção para o próximo ciclo de Hygiene. |
| **GAP** | Princípio aplicável da classe **não coberto**; gera **open decision** (código K-derivado) no próprio Inventário. |
| **N/A** | A classe não incide sobre o escopo do documento (ex.: PS situacionais sobre um documento de método). Registrar a justificativa. |

### 5.3 Instruções de preenchimento
- **Quem preenche:** Revisor (durante a revisão) e Especificador (ao entregar spec nova). `[FONTE: PP-PAP-001 §2.2 Who]`
- **Quando atualiza:** a cada revisão de spec, a cada ciclo de Hygiene (Bloco 4), e quando uma open decision (J-xxx) resolvida afeta um princípio.
- **Como registra GAP:** todo GAP cria uma linha de open decision `INV-GAP-nnn` com: documento, classe, princípio, descrição do gap, e encaminhamento (auditoria / emenda futura por decisão de Andraus). GAP **não** dispara reescrita automática (§1.2, PP-PAP-001 §3.2).

### 5.4 Inventário inicial M0 — [INFERÊNCIA de auditoria; não homologado]
`[FONTE: PP-PAP-001 §2.3 | documentos M0 existentes no repo]`

Documentos M0 auditados (≥6): `atomic-spec.md` v1.3, `RETOMADA/GEH-001…` v1.1, `ROADMAP.md`, `governance/CONSTITUTION.md`, `governance/RULES.md`, `governance/CONFLICT-MAP.md`.

| Documento M0 | PC | PB | PE | PCO | PO | PS | Base da avaliação |
|---|---|---|---|---|---|---|---|
| **atomic-spec v1.3** | PASS | PASS | PASS | FLAG | PASS | N/A | Define BASpec/D0–D9/E0–E3/etiquetagem; ancora PB-05/08 e PO-04. FLAG PCO: método não formaliza contraevidência (PCO-02) como gate de spec. `[FONTE: atomic-spec.md cabeçalho §1]` |
| **GEH-001 v1.1** | PASS | PASS | PASS | FLAG | PASS | N/A | 4Es (§3 → PB-01..04), centralizar/descentralizar (§6 → PE-02/03), decomposição (§7), antipadrões (§10). FLAG PCO: cobre cognição via ETCLOVG mas não os PCO-* nominalmente. `[FONTE: GEH-001 §3,§6,§7,§10]` |
| **ROADMAP** | PASS | PASS | FLAG | N/A | PASS | N/A | Sequência SPEC-001..045, caminho crítico, maturidade L0–L5. FLAG PE: sequência não declara fronteira de contexto por componente (PE-07). `[FONTE: ROADMAP.md]` |
| **CONSTITUTION v1.1** | PASS | PASS | PASS | PASS | PASS | FLAG | P01–P14 mapeiam PC-01..08 (hierarquia, PC-02, PC-03, PC-04, P12→PO-05); 4Es §. FLAG PS: situacionais (urgência/cautela) não normatizados na Constituição. `[FONTE: CONSTITUTION.md P01-P14, Hierarquia, 4Es]` |
| **RULES** | PASS | FLAG | PASS | N/A | PASS | N/A | Regras de rastreabilidade/enforcement vigentes. FLAG PB: cobertura de PB-06 (explicabilidade da ponderação) a confirmar em leitura profunda. `[INFERÊNCIA — leitura de cabeçalho; requer auditoria profunda no 1º ciclo de Hygiene]` |
| **CONFLICT-MAP** | PASS | PASS | PASS | FLAG | N/A | FLAG | Mapa de conflitos já existente; valida a Matriz de Conflitos do GPR-001 §6. FLAG PCO/PS: confirmar cobertura de inversões contextuais (GPR-001 §3.6). `[INFERÊNCIA — requer auditoria profunda]` |

> **Nota de honestidade epistemológica (INV-08/09, TRACE-06):** as linhas RULES e CONFLICT-MAP foram avaliadas por leitura de cabeçalho/uso citado, não por auditoria integral. Estão marcadas `[INFERÊNCIA]` e devem ser confirmadas no primeiro ciclo de Hygiene antes de virarem FATO. Nenhuma célula acima é baseline homologado.

> **K-PAP-001 — RESOLVIDA (Andraus, 2026-09-15):** o Inventário é **documento separado CIC-001**, com ciclo de versão próprio, mantendo o GPR-001 estável (PC-07). O CIC-001 será produzido como artefato subsequente; este §5 define seu schema.
>
> **K-PAP-005 — RESOLVIDA (Andraus, 2026-09-15):** o CIC-001 inclui **mapeamento seletivo** das open decisions existentes (J-001, B-001, G-001, H-001, I-001, K-001, L-001, C-001) → **apenas as que tocam um princípio** são mapeadas contra o GPR-001 (ex.: J-001↔PC-04; I-001↔PE-04; L-001↔PO-05). Decisões sem vínculo principiológico não são mapeadas (economia — 4Es).

---

## 6. BLOCO 4 — Ciclo de Hygiene de Princípios
`[FONTE: PP-PAP-001 §2.4 | ISO/IEC 42001 PDCA — PADRÃO | Policy hygiene — BENCHMARK | ADR — PRÁTICA]`

### 6.1 Estrutura PDCA do ciclo
- **Plan:** listar specs/documentos alterados desde o último ciclo e as open decisions resolvidas.
- **Do:** reauditar as células afetadas do Inventário (Bloco 3).
- **Check:** o Revisor confronta cada célula com o GPR-001; registra PASS/FLAG/GAP.
- **Act:** emitir output do ciclo (§6.3).

### 6.2 Frequência e gatilhos
- **Frequência padrão:** **K-PAP-002 — RESOLVIDA (Andraus, 2026-09-15): "por milestone homologada + gatilhos de evento"** (§6.2). Mais econômica que calendário fixo num projeto ainda produzindo specs (PB-04); ISO/IEC 42001 PDCA admite ciclo orientado a evento `[PADRÃO]`.
- **Gatilhos de revisão extraordinária:** (a) nova milestone homologada; (b) nova spec homologada; (c) open decision J-xxx resolvida que afete um princípio; (d) proposta de princípio novo (Bloco 5).

### 6.3 Output do ciclo
Atualização do Inventário de Conformidade; **opcionalmente** proposta de emenda ao GPR-001 (se um FLAG recorrente virar princípio); registro de supersessão (se um princípio obsolesceu).

**[Emenda v1.2 — HOMOLOGADA, DHR-PAP-001-C] Consulta obrigatória ao RMR-001:** todo ciclo de Hygiene consulta `backlog/RMR-001_Painel_Backlog.md`, verifica os itens de backlog cujo **Gatilho de Ativação** disparou desde o último ciclo e **promove os `ATIVADO`** (encaminhando cada um a decisão/spec/emenda/auditoria conforme sua "Ação ao ativar"), registrando por que os demais seguem `Em espera`. Nenhum item `ATIVADO` fica sem encaminhamento ao fim do ciclo. Materializa o mecanismo de surfacing do RMR-001 §4.

### 6.4 Ciclo de vida de um princípio (INV-07 / ADR)
`[FONTE: PP-PAP-001 §2.4 | INV-07 atomic-spec | ADR — PRÁTICA]`
```
Proposto → Ativo → Deprecado → Supersedido
```
Supersessão **nunca deleta** — cria registro histórico versionado (INV-07 / PC-07). Um princípio Deprecado permanece auditável; um Supersedido aponta para o que o substituiu.

---

## 7. BLOCO 5 — Critério de incorporação de novos princípios do Manual Universal
`[FONTE: PP-PAP-001 §2.5 | Manual Universal §4–7 — referência externa não-normativa | TOGAF "less is more" — PRÁTICA]`

### 7.1 Teste de pertinência (binário)
Um princípio candidato do Manual só é elegível se responder **SIM** a ambas:
1. O princípio afeta o **harness cognitivo de trading** do SOT (análise, convicção, síntese, TMP)?
2. O SOT tem **análogo constitucional implícito** ou lacuna declarada (ex.: GPR-001 §9 lacunas "Contestação formal (24)" e "Simplicidade suficiente (33)")?

Se qualquer resposta for NÃO → o princípio é registrado como "fora de escopo do SOT", não incorporado.

### 7.2 Formato de proposta (ficha quadripartite)
`[PRÁTICA: TOGAF / EA Wheel]` — toda proposta contém, no mínimo:
- **Name / Statement / Rationale / Implications** (estrutura quadripartite);
- **Justificativa de pertinência** (resultado do teste §7.1);
- **Mapeamento de impacto** em specs existentes (quais células do Inventário mudam);
- **Classe proposta** (PC/PB/PE/PCO/PO/PS) e regime resultante (Bloco 1).

### 7.3 Gate de homologação
`[FONTE: GPR-001 §14 | PC-08]` Toda adição ao GPR-001 é homologada por **Andraus**. **K-PAP-003 — RESOLVIDA (Andraus, 2026-09-15): o Especificador propõe** (ficha quadripartite §7.2) **e Andraus homologa**. O gate de homologação (PC-08) permanece exclusivo de Andraus; a proposta pelo Especificador reduz gargalo sem perda de controle.

### 7.4 Limite de gestão ("less is more")
`[PRÁTICA: TOGAF ADM]` Preferir **4–5 princípios fundamentais por tier**; acima disso cresce a intratabilidade. Novos princípios entram por **necessidade cognitiva real**, nunca por completude ornamental (anti-padrão AP-12, GPR-001 §10).

---

## 8. BLOCO 6 — Protocolo operacional do Revisor (extensão a HRE-001/GRE-001)
`[FONTE: PP-PAP-001 §2.6 | HRE-001 v2.2 | GRE-001 v2.2]`

O PAP-001 **estende** (não substitui) o protocolo do Revisor.

### 8.1 Checklist diferenciado por classe
| Classe | Modo de verificação | Efeito de não-conformidade |
|---|---|---|
| PC-01..08 | **Gate eliminatório** | Violação → NÃO CONFORME **Crítica** (bloqueia homologação) |
| PB-01..10 / PE-01..08 | **Gate prospectivo** | Violação → NÃO CONFORME **Média**; registrar e justificar (GPR-001 §14) |
| PCO / PO / PS | **Critério de qualidade** | Não-cobertura → achado **Menor** (registra, não bloqueia), salvo exceção elevatória PO-02/PO-03 em E3 |

### 8.2 Instrução de reporte de gap
Todo achado de princípio é ancorado como `GPR-001 §X / PC-yy` no parecer, com severidade explícita e encaminhamento (bloqueia / registra / melhora). Formato compatível com o contrato de saída do Bloco B (PE-PR-PAP-001 §5).

### 8.3 Distinção de severidade
`[FONTE: GPR-001 §2.1 elasticidade nula vs. §2.4-2.6]`
- **Crítica** — violação de princípio **constitucional** (PC-*): bloqueia.
- **Média** — violação de princípio **basilar/estrutural** (PB/PE) em spec prospectiva.
- **Menor** — não-cobertura de princípio **cognitivo/operacional/situacional** (PCO/PO/PS) quando o contexto o aciona.

### 8.4 Cruzamento com o Inventário
Antes de emitir parecer sobre spec **existente**, o Revisor consulta o Inventário de Conformidade (Bloco 3) para não reabrir gaps já registrados nem exigir reescrita vedada por §1.2.

---

## 8-bis. BLOCO 7 — Vínculo Principiológico em Tempo de Decisão (VPD)
`[FONTE: GPR-001 §2.2 PB-06 (explicabilidade da ponderação), §6 (Matriz de Conflito), §7 passo 9 (DELIBERAR) | CONSTITUTION P01 | atomic-spec Enforcement Contract]`
`[Emenda v1.2 — 2026-09-16, comissionada por Andraus]`

### Motivação (prova)
Auditoria de 2026-09-16 provou que os specs de cognição têm **zero** referências à camada principiológica: `elliott-wave.spec.md`, `fibonacci.spec.md`, `smc.spec.md`, `ict.spec.md`, `synthesis.spec.md` e `specs/features/SPEC-001/plan.md` — **0 hits** de GPR-001 e de PC/PB/PCO/PE-08. Ou seja: no **momento da decisão**, o harness cognitivo não conversa com a camada de princípios; os princípios estão implícitos como limiares hardcoded, sem registro rastreável de ponderação. O Bloco 6 governa a conversa em **spec-time**; este Bloco 7 institui a conversa em **decision-time**, tornando-a obrigatória, verificável e auditável.

### Escopo de incidência
Aplica-se a toda spec que produza **Decisão, Convicção, Síntese ou ponderação de hipótese por agente** — nominalmente SPEC-003 (Conviction/CCM-001), SPEC-014 (Synthesis), SPEC-010..013 (agentes analíticos), e às revisões dos specs de agente de 1ª geração (`specs/*.spec.md`). Não incide sobre specs de pura infraestrutura sem decisão (ex.: SPEC-004 Blackboard, SPEC-005 Event Bus), salvo no que transportam o Registro de Ponderação.

### Requisito VPD (o que a spec DEVE exigir do componente em runtime)
No momento em que o componente pondera princípios para decidir, DEVE emitir um **Registro de Ponderação** contendo:

| ID | Exigência | Âncora |
|---|---|---|
| **VPD-1** | Os IDs GPR-001 dos princípios efetivamente pesados (ex.: PC-01, PC-04, PB-01, PCO-01, PE-08) | GPR-001 §2 |
| **VPD-2** | Em conflito, a regra da **Matriz de Conflito** aplicada e qual princípio prevaleceu | GPR-001 §6 |
| **VPD-3** | O princípio **sacrificado** e o porquê da ponderação | PB-06 (GPR-001 §2.2) |
| **VPD-4** | Gravação no workspace **Meta-Cognition** do Blackboard, com provenance, auditável post-hoc | PB-07 · CONSTITUTION §Blackboard |
| **VPD-5** | A ponderação respeita a hierarquia constitucional: nenhum PC-* cede; 4Es na ordem Eficácia→Economicidade | PC-01..08 · PB-01..04 |

### Gate do Revisor (estende o Bloco 6)
O Revisor **REPROVA (NÃO CONFORME — Crítica)** qualquer spec no escopo acima que não exija VPD-1..5 de forma verificável. Item adicional obrigatório no Constitution Check dessas specs:
> `[ ] VPD presente — o componente cita, aplica (§6) e grava (Meta-Cognition) os princípios GPR-001 ponderados na decisão, com o sacrificado justificado (PB-06/PB-07).`

### Registro no CIC-001
O Inventário ganha a coluna **VPD** por spec de decisão: `PRESENTE` / `AUSENTE` / `N/A`. Os specs de 1ª geração (5 agentes + SPEC-001) entram como **`VPD-AUSENTE` (gap conhecido)** — não força reescrita imediata (regime R1), mas ao serem redigidos sob o roadmap (SPEC-010..014) ou emendados, o VPD torna-se **gate**.

### Efeito de garantia
A conversa decision-time fica **garantida** (é gate: nenhuma spec de decisão homologa sem VPD) e **provável** (produz artefato de runtime no Meta-Cognition, auditável por PB-07) — fechando o gap provado na Motivação.

---

## 9. Decisões K-PAP-001..005 — RESOLVIDAS por Andraus (2026-09-15)
`[FONTE: PP-PAP-001 §8 | DHR-PAP-001-B]`

Todas as 5 decisões foram deliberadas e homologadas por Andraus em 2026-09-15 (DHR-PAP-001-B). Preservadas com código e resolução (INV-07 — não deletadas):

| Código | Questão | Resolução homologada (Andraus, 2026-09-15) |
|---|---|---|
| **K-PAP-001** | Inventário: documento separado CIC-001 ou seção viva do GPR-001? | **Documento separado CIC-001** (ciclo de versão próprio; GPR-001 estável — PC-07). §5. |
| **K-PAP-002** | Frequência do Hygiene? | **Por milestone homologada + gatilhos de evento** (PB-04; ISO 42001 PDCA). §6.2. |
| **K-PAP-003** | Quem propõe princípio novo? | **Especificador propõe (ficha §7.2) + Andraus homologa** (gate PC-08 exclusivo de Andraus). §7.3. |
| **K-PAP-004** | Escopo: só specs ou também docs de governança? | **Também documentos de governança** (GRE/HRE/GEH/CONSTITUTION/RULES) quando revisados, sob regime R1 (retroativo-auditoria leve, sem reescrita). §3, §9.1. |
| **K-PAP-005** | Open decisions existentes mapeadas vs. GPR-001? | **Sim, mapeamento seletivo** — apenas as que tocam um princípio (J-001↔PC-04; I-001↔PE-04; L-001↔PO-05). §5.4. |

### 9.1 Efeito de K-PAP-004 no escopo
O PAP-001 aplica-se a specs de componente **e** a documentos de governança quando revisados. Sobre documentos de governança incide o **regime R1** (retroativo-como-auditoria): verificação de gap sem obrigação de reescrita. Isso é coerente com o Inventário M0 (§5.4), que já audita GEH-001, CONSTITUTION e RULES.

> Nenhuma decisão foi usada como invariante fechado durante a fase de proposta (CONS-01). A homologação de Andraus (DHR-PAP-001-B) é o ato que as fecha.

---

## 10. Critérios de aceitação declarados
`[FONTE: PP-PAP-001 §7]`

O PAP-001 pede-se CONFORME quando: (1) nenhum invariante do §4/PP-PAP-001 violado; (2) as 6 classes têm regime explícito (Bloco 1); (3) o 5W2H é prescritivo (Bloco 2); (4) o Inventário tem schema + M0 preenchido (Bloco 3); (5) o Hygiene define PDCA, gatilhos e ciclo de vida (Bloco 4); (6) o critério de incorporação é objetivo (Bloco 5); (7) o protocolo do Revisor é operacionalizável (Bloco 6); (8) todas as fontes externas classificadas (§2, §11); (9) as 5 decisões K-PAP expostas como [DECISÃO NECESSÁRIA]; (10) nenhuma decisão aberta do SOT fechada; (11) sem abertura de escopo para SPEC-004/009/024; (12) rastreabilidade completa.

---

## 11. Classificação das fontes externas usadas

| Fonte | Rótulo |
|---|---|
| NIST AI RMF — 4 tiers de maturidade | `[PADRÃO]` |
| NIST Agentic Profile / AAGATE | `[PADRÃO]` |
| ISO/IEC 42001 — PDCA | `[PADRÃO]` |
| TOGAF ADM — Architecture Principles / "less is more" | `[PRÁTICA]` |
| EA Wheel — estrutura quadripartite | `[PRÁTICA]` |
| ADR pattern (Martin Fowler / UK Gov) | `[PRÁTICA]` |
| Policy Debt / governance hygiene (GovLoop) | `[BENCHMARK]` |
| Architecture Debt KPI (EAPJ) | `[BENCHMARK]` |
| Manual Universal de Engenharia de Princípios Agênticos v2.0 | Referência externa **não-normativa** (todo princípio importado requer Bloco 5) |

Nenhuma fonte externa foi incorporada automaticamente — cada uma foi confrontada com a arquitetura SOT (ROAD-01).

---

## 12. Declaração

Autopré-check (§10 do Bloco A) satisfeito: 6 blocos presentes e prescritivos; Inventário M0 preenchido; 5 decisões K-PAP expostas; nenhuma decisão aberta usada como invariante fechado; fontes classificadas; fronteiras respeitadas (J-001 não fechado, sem reescrita de specs, MEASURE/MANAGE não prescritos); 4Es na hierarquia correta; Manual citado apenas por confronto; sem QUANDO/ENTÃO/PORQUE de runtime; GEH-001 lido de `RETOMADA/GEH-001…` v1.1.

**Pronto para revisão.**

---

*PAP-001 v1.1 — **HOMOLOGADO — BASELINE** (Andraus, 2026-09-15, DHR-PAP-001-B). Produzido pelo Especificador via skill `sot-especificador-pap001` (Bloco A do PE-PR-PAP-001 v1.1); auditado pelo Revisor (Bloco B → CONFORME condicional); K-PAP-001..005 resolvidas por Andraus. v1.0 PROPOSTA supersedida sem deleção (INV-07). Pendência não-bloqueante: auditoria integral de RULES e CONFLICT-MAP no 1º ciclo de Hygiene (achado M-01).*
