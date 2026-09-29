# GMC-CEM001-EXT-001 — Proposta de Evolução do CEM-001 (Categoria B) — Confiabilidade Histórica do Produtor de Evidência

> **Artefato de governança de Modelo Canônico** (GMC-001 Cap.5 — Governança de Propostas, Auditorias e Aprovações).
> Proposta formal de **evolução** do CEM-001 (Canonical Evidence Model), **não** de criação de novo modelo, **não** de reescrita (CONST-01).
> Origem: **ACH-001** (achado Médio do Revisor no parecer CONFORME do Plan da SPEC-002) + decisão de Andraus (2026-09-29) de reclassificar a extensão de **Categoria A → Categoria B** e conduzir o processo formal do GMC-001 Cap.5, em vez de declarar exceção/override.

| Campo | Valor |
|---|---|
| Código provisório (GMC-001 Cap.2 — Iniciação Formal) | **GMC-CEM001-EXT-001** |
| Modelo Canônico afetado | **CEM-001** — Canonical Evidence Model (BASELINED v1.0, `canon/CEM-001-canonical-evidence-model.md`) |
| Tipo de alteração | **Evolução** de modelo existente (GMC-001 Cap.5 Escopo de Governança) |
| **Classificação da alteração** | **Categoria B — Ampliação Estrutural Compatível** (GMC-001 Cap.3): novo campo **opcional** |
| Versão alvo | CEM-001 **v1.1** (incremento **MINOR** — GMC-001 Cap.3 Política de Versionamento: MINOR para Categoria A e B) |
| Estado da proposta | **APPROVED** (Etapas 1–3 do fluxo concluídas; Etapa 4 — registro do Controlador — em `governance/CATALOGO-OFICIAL.md`) |
| Papéis (GMC-001 Cap.2/5) | **Estrategista** = Especificador SOT · **Analista** = Revisor SOT · **Usuário (Validação Estratégica)** = Andraus · **Controlador** = registro no Catálogo Oficial |
| Atas correlatas | DHR-SPEC002-001 (abertura, DN-1) · **DHR-SPEC002-002** (homologação do Plan da SPEC-002 + decisão Categoria B) |
| Spec consumidora | SPEC-002 — Evidence & Evidence Provenance Harness (`specs/features/SPEC-002/plan.md`, EPH-003/EPH-004; DN-1) |
| Data | 2026-09-29 |
| Autor (Estrategista) | Especificador Principal (Claude Code, Opus 4.8) |

---

## 0. Contexto e motivação do ACH-001 (registro histórico — INV-07)

A **abertura** da SPEC-002 (DHR-SPEC002-001, DN-1) decidiu que a **confiabilidade histórica do produtor de evidência** entra como **extensão formal do CEM-001 via GMC-001**, nomeando-a como **Categoria A** ("aditiva, sem mudar semântica existente"), com a trava constitucional de que é **só metadado descritivo/filtro — NUNCA dimensão do Conviction Vector** (INV-04).

Na redação do Plan tentou-se preservar a rotulagem "Categoria A" modelando a confiabilidade como **valor de uma Governed Enumeration**. O **Revisor** (parecer **CONFORME**, achado Médio **ACH-001**) conferiu o **GMC-001 Cap.3** e confirmou, pela classificação **literal** do próprio GMC-001:

- **Categoria A — Extensão:** "inclusão de **novos valores em Governed Enumerations**; inclusão de novos estados previamente previstos". [FONTE: GMC-001 Cap.3]
- **Categoria B — Ampliação Estrutural Compatível:** "**novo campo opcional**; novo relacionamento opcional". [FONTE: GMC-001 Cap.3]

Como **não há hoje nenhuma enumeração compatível pronta no CEM-001** para receber a confiabilidade histórica do produtor como mero "novo valor", a extensão exige **um campo novo** (ainda que opcional). Pela classificação literal, campo novo = **Categoria B**.

**Decisão de Andraus (2026-09-29):** **reclassificar como Categoria B** e conduzir o **processo formal que o próprio GMC-001 já prevê** (Cap.5), em vez de uma exceção/override. Esta proposta é a execução dessa decisão.

> **Substância inalterada:** a mudança é **de processo** (A → B), não de mérito. A confiabilidade permanece **metadado descritivo/filtro** e **NUNCA** entra no Conviction Vector (INV-04). CONST-01 preservado — é extensão aditiva/compatível, não redefinição.

---

## 1. Etapa 1 — Proposição (GMC-001 Cap.5)

### 1.1 Objetivo

Adicionar ao CEM-001 um **campo opcional** que represente a **confiabilidade histórica (track-record) do produtor de evidência** — um eixo de qualidade **independente** da força do relato específico (`Evidence Strength`, já canônico), como propriedade **intrínseca da evidência** (pertence ao modelo canônico da evidência, não ao harness que a processa — DN-1).

### 1.2 Justificativa arquitetural

- **Propriedade intrínseca da evidência (DN-1):** confiabilidade de fonte é atributo da evidência, não do processo operacional; portanto pertence ao CEM-001 (idioma canônico, INV-10), não à camada Harness (SPEC-002).
- **Doutrina Admiralty / NATO AJP-2.1 (SRC-02, `[EXTERNO]`, `specs/features/SPEC-002/sources/SRC-02.txt`):** *"Each descriptor is considered in isolation to ensure that the reliability of the source does not influence the assessed accuracy of the report."* Trata reliability (da fonte) e credibility (do relato) como **dois eixos independentes**. Fonte tomada como **DADO**, nunca baseline; adota-se o **princípio de dois eixos**, **não** os códigos literais A-F/1-6 (rejeitados como baseline — research.md §6.3).
- **Neutralidade preservada (CEM-001 Princípio 1/2):** o campo é neutro de domínio (não contém regra de Elliott/SMC/ICT/macro); aplica-se igualmente a qualquer evidência.
- **Não colide com o Conviction Vector (INV-04):** o campo é descritivo/filtro; a trava anti-INV-04 é reforçada na Spec consumidora (SPEC-002, BASpec-EPH-004, efeito E3).

### 1.3 Impacto esperado

Nenhum produtor/consumidor existente do CEM-001 é obrigado a mudar. Um novo campo **opcional** amplia o contrato mantendo compatibilidade integral. Consumidores que quiserem usar o eixo de confiabilidade passam a poder lê-lo; os que não quiserem continuam operando inalterados (adaptação **opcional** — GMC-001 Cap.3 Categoria B).

### 1.4 Especificação do elemento a adicionar (conteúdo normativo da extensão)

| Atributo | Definição |
|---|---|
| Nome do campo | `Producer Historical Reliability` (confiabilidade histórica do produtor) |
| Camada CEM-001 | Camada 2 — Origem (junto de `Producer Type`/`Producer ID`), por ser propriedade do **produtor**/origem, não do conteúdo |
| Obrigatoriedade | **OPCIONAL** (nullable). Ausência = `INDETERMINADO` (produtor sem histórico registrado) — não força valor default arbitrário (RULE-EPI / RULE-UNC) |
| Domínio de valores | **Governed Enumeration** sob GMC-001 (tiers ordinais de confiabilidade). Os **valores** do enum são governados pelo GMC-001; a proposta cria o **campo** (Categoria B) cujo tipo é essa enumeração governada |
| Mutabilidade | Segue a regra do CEM-001 Cap.4: imutável após publicação (Status é o único campo mutável). Atualização de track-record ocorre em nova evidência/versão, não por mutação retroativa |
| Relação com `Evidence Strength` | **Eixo independente** — um não influencia o outro (reliability ≠ credibility; SRC-02). Nenhuma fórmula acopla os dois |
| **Trava constitucional (INV-04)** | O campo **NUNCA** entra como dimensão, insumo ou peso do **Conviction Vector**. É metadado descritivo/filtro. Enforcement na Spec consumidora (SPEC-002 EPH-004, E3) |

> A enumeração de tiers **não fixa fórmula, peso numérico ou aging** — isso toca J-001/CCM-001 (SPEC-003), que permanece **ABERTA** (CONS-01). Esta proposta só cria o campo e seu domínio ordinal descritivo.

### 1.5 Classificação da alteração — Categoria B (justificada)

- **Não é Categoria A:** não é "novo valor de enumeração já existente" — não há enum compatível no CEM-001; é campo novo. [GMC-001 Cap.3]
- **É Categoria B:** "novo campo **opcional**" — ampliação estrutural compatível. [GMC-001 Cap.3]
- **Não reclassifica para Categoria C:** a Categoria B só vira C se a alteração **introduzir campo obrigatório**, **exigir alteração em produtores existentes**, **exigir alteração em consumidores existentes** ou **modificar comportamento previamente válido** (GMC-001 Cap.3 "Reclassificação automática para Categoria C"). **Nenhuma** dessas condições ocorre: o campo é opcional, produtores/consumidores existentes seguem operando, nenhum comportamento válido é alterado.

---

## 2. Análise de Impacto Obrigatória (GMC-001 Cap.3)

Resposta às 5 perguntas obrigatórias do Cap.3:

1. **Quais componentes serão afetados?** Nenhum de forma obrigatória. **Produtores** de evidência (agentes SPEC-010..014, futuros) **poderão** popular o campo; enquanto não o fizerem, publicam evidência válida sem ele (opcional). **Consumidores** (Fusion/Conviction/Synthesis — SPEC-003/014; Manager) **poderão** lê-lo como filtro/metadado; nenhum é obrigado. A camada Harness (SPEC-002) já prevê o eixo (EPH-003) e a trava (EPH-004).
2. **Quais modelos serão afetados?** Apenas o **CEM-001** (evolui v1.0 → v1.1). **CHM-001** (hipótese) não é tocado — vínculo evidência→hipótese permanece por referência (INV-10). **CCM-001** (Conviction, pendente/SPEC-003) **não** recebe o campo (trava INV-04). Nenhum outro modelo canônico depende deste campo.
3. **Há quebra de compatibilidade?** **Não.** Campo opcional; produtores e consumidores existentes continuam operando sem adaptação (GMC-001 Cap.3 Regra de compatibilidade da Categoria B). Compatibilidade retroativa integral.
4. **Existe alternativa menos invasiva?** Avaliadas: (a) manter como **metadado solto da camada Harness** (SPEC-002) — **rejeitada** por DN-1 (confiabilidade é intrínseca à evidência, pertence ao canônico). (b) forçar como **novo valor de enum existente** para permanecer Categoria A — **inviável** (não há enum compatível no CEM-001; foi o achado ACH-001). (c) **campo opcional** (esta proposta) — a menos invasiva que ainda satisfaz DN-1: aditiva, compatível, sem tocar campos/estados/transições existentes.
5. **A alteração simplifica ou aumenta complexidade?** **Neutra-a-simplificadora.** Coloca a confiabilidade no lugar arquitetural correto (a evidência), evitando duplicação/ambiguidade entre "qualidade de fonte" e "força do relato"; separa dois eixos que a doutrina (SRC-02) já trata separados. Não adiciona estados, transições nem obrigações.

### 2.1 Compatibilidade Retroativa (GMC-001 Cap.3 — demonstração obrigatória)

| Dimensão | Impacto |
|---|---|
| **Produtores existentes** | Nenhum. Campo opcional; evidência sem o campo continua válida e publicável (gate de conformidade CEM-001 não passa a exigi-lo — SPEC-002 EPH-001). |
| **Consumidores existentes** | Nenhum. Consumidores que ignoram o campo operam inalterados; adaptação é opcional. |
| **Repositórios** | Nenhum obrigatório. Armazenamento físico é de SPEC-004/006 (M-001/H-001 abertas); campo opcional não força schema de storage (não antecipado — CONS-01). |
| **Modelos dependentes** | CHM-001 intocado; CCM-001 (pendente) **não** recebe o campo (INV-04). Nenhuma dependência quebrada. |

---

## 3. Fluxo de governança (GMC-001 Cap.5) — estado de execução

```
Estrategista → Analista → Usuário → Controlador
```

| Etapa | Papel | Estado | Evidência |
|---|---|---|---|
| **Proposição** (Etapa 1) | Estrategista (Especificador) | ✅ concluída | esta proposta (§1–§2), com objetivo/justificativa/impacto/análise/classificação |
| **Auditoria** (Etapa 2) | Analista (Revisor) | ✅ concluída | parecer **CONFORME** do Plan da SPEC-002 + achado **ACH-001** (Médio) que estabeleceu a classificação correta (Categoria B); conferência literal do GMC-001 Cap.3 pelo Revisor |
| **Consenso** (Etapa 3) | Usuário (Andraus) | ✅ concluída | decisão de 2026-09-29: reclassificar para Categoria B e conduzir o processo formal Cap.5 (DHR-SPEC002-002) |
| **Registro Oficial** (Etapa 4) | Controlador | ⏳ a registrar | entrada em `governance/CATALOGO-OFICIAL.md` §1 (CEM-001 → evolução Categoria B, v1.1); incorporação física do campo opcional em `canon/CEM-001-...md` = ato editorial do Controlador |

> **Transição de estado no Catálogo (GMC-001 Cap.5):** resultado de auditoria CONFORME → estado **APPROVED**; APPROVED é transitório e deve ser encaminhado ao Controlador para homologação/registro (GMC-001 Cap.2 "Regra do estado APPROVED"). O registro final (Etapa 4) e a eventual transição do CEM-001 v1.0 → SUPERSEDED / v1.1 → BASELINED são atos do Controlador no Catálogo.

---

## 4. Restrições invioláveis desta extensão

- **INV-04 (constraint explícita):** o campo `Producer Historical Reliability` **NUNCA** entra como dimensão, insumo ou peso do **Conviction Vector**. Custo/qualidade-de-fonte ≠ convicção (Salvaguarda 4, CEE-001 §10). Enforcement na SPEC-002 (EPH-004, efeito E3, fail-closed).
- **CONST-01:** extensão **aditiva e compatível** — não redefine campo, estado ou transição existente do CEM-001. É Categoria B (novo campo opcional), não reescrita.
- **CONS-01:** não fecha nenhuma decisão aberta. **J-001** (fórmula/pesos/limiares definitivos do Conviction), **N-001**, **CCM-001** permanecem **ABERTAS** — esta proposta **não** fixa fórmula, peso ou aging da confiabilidade.
- **INV-07:** registro histórico da discussão Categoria A vs B preservado (§0); nada deletado.
- **INV-EPI / RULE-EPI / RULE-UNC:** ausência de track-record = `INDETERMINADO`, não valor default arbitrário; sem falsa precisão numérica (o domínio é ordinal descritivo, não score).
- **RULE-MET-01:** esta proposta é ato do Estrategista; **não** homologa nem registra sozinha — o registro é do Controlador; a homologação estratégica é de Andraus (já dada).

---

## 5. Critérios de aceitação da proposta (GMC-001 Cap.3/5)

- [x] Classificação formal da alteração declarada (**Categoria B**) e justificada contra a régua literal do Cap.3.
- [x] Análise de impacto obrigatória (5 perguntas) presente e respondida (§2).
- [x] Compatibilidade retroativa demonstrada (produtores/consumidores/repositórios/modelos dependentes — §2.1).
- [x] Versionamento explícito (MINOR: v1.0 → v1.1).
- [x] Segregação de responsabilidades respeitada (Estrategista propõe; Analista auditou; Usuário deu consenso; Controlador registra).
- [x] Auditabilidade: proposta, auditoria (ACH-001), consenso (DHR-SPEC002-002) e registro reconstituíveis.
- [x] INV-04 declarada como constraint explícita da extensão.

---

*GMC-CEM001-EXT-001 — Proposta de evolução Categoria B do CEM-001. Governança: GMC-001 Cap.5. Estado: APPROVED (registro do Controlador no Catálogo Oficial). Não redefine o CEM-001 (CONST-01). Não fecha decisão aberta (CONS-01). Não fabrica resultado de execução (RULE-MET-01). Substância de DN-1 preservada: metadado descritivo, NUNCA no Conviction Vector (INV-04).*
