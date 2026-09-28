# Proposta de Abertura — SPEC-002: Evidence & Evidence Provenance Harness

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02)
**Autor:** Especificador Principal SOT
**Data:** 2026-09-28
**Status:** `[PROPOSTA]` — aguarda parecer do Revisor sobre o Dossiê + homologação de Andraus da **definição**, ANTES do Plan (AGENTS.md §5; ROADMAP §23; atomic-spec §15)
**Depende de:** `DOSSIE-PESQUISA.md` (mesmo diretório) — leia primeiro, inclusive o §0 (limitação WebFetch / RULE-ECC-04).

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-002** | O tema do slot (ROADMAP §4) e o número coincidem; abertura pela ordem regular (ROADMAP §25). Nenhuma divisão/renumeração de slot → número preservado (RULE-ECC-01). |
| **Nome** | **Evidence & Evidence Provenance Harness** | Idêntico ao título do slot; nenhuma capacidade nova inventada (ROADMAP §26). |
| **Complexidade** | **CRITICAL** | Fundação de quase todo o núcleo cognitivo (a Evidência alimenta hipótese, fusão, convicção, KG, RAG). Auditoria de adiantamento classificou risco de abertura **BAIXO** (CEM-001 baselined), mas o **componente** é CRITICAL (P0, ROADMAP §4). |
| **Profundidade-alvo** | **D0–D7** (conforme slot) + **D8 adversarial** para BASpecs com efeito E3 | Perfil CRITICAL = standard + adversarial (AGENTS.md §4). D5 (estados da Evidência — herdados do CEM-001 Cap.4), D6 (protocolo Blackboard — por referência, M-001 aberta), D7 (cenários), D8 (negação: ausência≠contraevidência; dupla-contagem de dependente). |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Nasce sob o gate de maturidade normativo (SPEC-021 homologada). |
| **Classe predominante** (orientação, não vinculante — atomic-spec §10.6) | **H (Híbrido)**, com **C (Constitutivo)** para invariantes de imutabilidade/proveniência | Declaração normativa é **por BASpec** no Plan (CC-11). Ver §5. |

**Natureza:** Spec de **núcleo cognitivo / domínio** (Trilha B), camada operacional sobre canônico — mesmo padrão arquitetural da SPEC-001 (Hypothesis Harness sobre CHM-001).

---

## 2. Fronteira e escopo

### Dentro do escopo (camada Harness/operacional SOBRE CEM-001)

O que a SPEC-002 DEVE cobrir e que o CEM-001 (contrato do objeto) **não** cobre sozinho:

- **Criação/registro operacional de Evidência** — protocolos e regras de transição em operação (como o SOT cria, versiona, supersede, invalida, arquiva evidência), referenciando o contrato e a máquina de estados do CEM-001 (ACTIVE→SUPERSEDED/INVALIDATED→ARCHIVED), **sem redefini-los**.
- **Evidence Registry como serviço lógico** — alocação de ID, versionamento monotônico operacional, índice por estado/produtor/domínio, API de consulta/reconstrução (análogo ao Hypothesis Registry da SPEC-001). *(Armazenamento físico = SPEC-004/006 — M-001/H-001/BL-003 abertas.)*
- **Qualidade, independência e temporalidade operacionais** — como o Harness avalia (qualitativamente, até J-001) directness/timeliness/independence/agreement (SRC-04 adaptado), incluindo a **salvaguarda contra dupla-contagem de evidência dependente**.
- **Natureza da Evidência: favorável / contraevidência / inconclusiva / ausente** — com **ausência** e **inconclusiva** como estados de primeira classe (open-world, SRC-06); ausência **nunca** convertida silenciosamente em contraevidência (RULE-EPI-01/CC-09/INDETERMINADO).
- **Marcação de conflito** entre evidências (registrar que há conflito e sua natureza) — **sem** resolvê-lo/fundi-lo (isso é SPEC-003).
- **Provenance operacional** — produtor (AGENT/ENGINE), ferramenta/Skill que produziu, versão, fonte, e a **atividade** de geração (vocabulário PROV adaptado, SRC-01) projetados sobre os campos canônicos do CEM-001 (Producer/Origin/Source Reference/Lineage).
- **Chain-of-custody e versionamento imutável verificáveis** (SRC-02/SRC-05 adaptados; INV-07; CEM Cap.4).
- **Relação operacional Evidência ↔ Hipótese** — como a evidência transita para/da hipótese (por referência a CHM-001/CEM-001), fronteira `Fonte → Dado → Evidência → Hipótese`. INV-06 (Evidência ≠ Observação de Skill).
- **Auditabilidade (D9 por referência)** — o que o Harness deve suportar para reconstrução (P13), sem fechar mecanismo de persistência.

### Fora do escopo (Non-goals explícitos)

| Item | Motivo | Pertence a |
|---|---|---|
| Redefinir a estrutura/estados/lineage do CEM-001 | CC-02/CONST-01 | CEM-001 (canônico) / GMC-001 |
| Fusão de evidência, agregação, Conviction Vector, fórmula/pesos | Topologia Q-007; **J-001 aberta**; Evidence Strength ≠ Convicção (CEM Cap.3) | SPEC-003 |
| Storage físico da Evidência (Blackboard/KG) | **M-001/H-001/BL-003 abertas** | SPEC-004/006/009 |
| Estados do Blackboard para objetos não-hipótese | **M-001 aberta** | SPEC-004 |
| Limiar numérico de qualidade/independência | **J-001 aberta**; RULE-EV-05 | SPEC-003/CCM-001 |
| Execução de ordem / escopo regulatório de execução (MiFID) | **INV-05** (SOT não executa ordem) | fora do SOT / família RISK |
| Cognitive Trace Reconstruction (implementação) | CEM Cap.5 atribui ao Knowledge Graph | SPEC-006 |

---

## 3. Quantidade — manter 1 Spec unificada vs. dividir (decisão explícita)

Avaliei se "Evidence" e "Evidence Provenance" deveriam ser duas Specs:

| Opção | Prós | Contras |
|---|---|---|
| **(A) 1 Spec unificada — ESCOLHIDA** | O CEM-001 já trata evidência e proveniência como um único contrato (Cap. 3 conteúdo + Cap. 5 rastreabilidade indissociáveis); proveniência sem o objeto que ela descreve é vazia; cabe numa sessão de revisão como camada operacional coesa; espelha SPEC-001 (que unificou hipótese + registry + protocolo). | Spec densa (mitigado por profundidade adaptativa e BASpecs atômicas). |
| (B) 2 Specs (Evidence / Provenance) | Unidades menores | Fragmenta um contrato canônico único; cria fronteira artificial; proveniência ficaria órfã do objeto; re-trabalho de rastreabilidade. |

**Decisão proposta:** **(A) 1 Spec.** Registrado como `[DECISÃO NECESSÁRIA: SPEC-002-SPLIT-001]` para confirmação de Andraus (a quantidade é definida na abertura — RULE-ECC-01).

---

## 4. Dependências e decisões abertas incidentes

- **CEM-001** (`canon/CEM-001-canonical-evidence-model.md`) — **baseline** (DHR-TAX-001, 2026-09-26); **construir SOBRE, não redefinir** (CC-02). Reduz risco do Dossiê (auditoria de adiantamento: risco BAIXO). *(Correção de localização: ver §7 — o hint de origem apontava `canon/CEE-001-...v2.0.md`, que é outro documento.)*
- **CHM-001** — baseline; consumidor de Evidência; SPEC-002 referencia (relação Evidência↔Hipótese), não redefine.
- **SPEC-001** (Hypothesis Harness) — baseline; padrão de "camada operacional sobre canônico" + fronteira `Fonte→Dado→Evidência→Hipótese` já citada.
- **SPEC-020** (9 lentes constitutivas) e **SPEC-021** (gate E3 de maturidade) — aplicam-se a SPEC-002 como a toda Spec ≥ SPEC-002; cobertura verificada no Autopré-check do Plan.
- **RULE-MECH-01** (Classe por BASpec) — **incide** (SPEC-002 em diante); esta Spec **cita RULE-MECH-01** → sob CC-11. Ver §5.
- **RULE-PD-01 / CC-12 (Princípios de Domínio)** — **NÃO incide.** SPEC-002 **não** é Spec de especialidade de escola (Elliott/SMC/ICT); o CEM-001 é **explicitamente neutro de domínio** (Cap. 1, Princípio 1; Cap. 2 "Neutralidade de Domínio"). Portanto **nenhum `PD-xx` será proposto**. (Determinação análoga à da SPEC-046, por motivo diferente: lá era tooling; aqui é harness de kernel domain-neutral.)
- **Decisões abertas incidentes (CONS-01 — não fechar):** **J-001** (downstream — convicção; **não bloqueia** a camada de evidência/provenance; SPEC-002 referencia o slot de força sem fechar fórmula); **M-001** (estados Blackboard p/ Evidência — SPEC-004); **H-001** (KG — SPEC-006); **BL-003** (storage físico); **BL-002** (falso-DENY observável — declarar ENF-07 sem fechar limiar). Todas permanecem **abertas**.
- **RULE-REG-001** (`spec:SPEC-002 em redação`) — reconhecido: registrar o lote de 10+1 famílias RULE no `RULES.md` (piloto atomic-spec v1.5) no gate de redação do Plan (ver Dossiê §5).
- **`[DECISÃO NECESSÁRIA: SPEC-002-VERBATIM-001]`** (RULE-ECC-04 sob WebFetch bloqueado) — ver Dossiê §0/§6.

---

## 5. Classe RULE-MECH-01 (CC-11) — orientação predominante

SPEC-002 **cita RULE-MECH-01** no próprio texto → sob CC-11 (declaração de Classe **por BASpec**, no Plan; nunca por Spec inteira — preserva SES-001 §50).

**Predominante (orientação de leitura, não vinculante — atomic-spec §10.6):** **H (Híbrido)**. O núcleo é:
- captura de proveniência, alocação de ID, versionamento, comparação de hash/estado = **determinístico (Classe D)**;
- avaliação de qualidade/independência/natureza (favorável/contra/inconclusiva/ausente) = **julgamento com gate de saída** (Classe **H/P** — julgamento do agente produtor + verificação estrutural de conformidade CEM);
- **enforcement de imutabilidade e integridade de proveniência** (impedir alteração de campo imutável pós-publicação; impedir ausência→contraevidência silenciosa) = **Classe C (Constitutivo)**, alinhado a efeito **E3** (publicação de evidência é commit compartilhado; fail-closed).

**Critério 4Es:** Eficácia primeiro — uma evidência com proveniência corrompida ou com ausência tratada como negação contamina toda a cadeia downstream (hipótese→convicção→decisão); só depois Eficiência/Economicidade. Classe C reservada aos invariantes de risco alto (RULE-MECH-02: C em risco baixo = violação de Economicidade). Bounded loop + gate de saída determinístico declarados por BASpec H/P no Plan (RULE-MECH-03).

---

## 6. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação na abertura | Nota |
|---|---|---|
| CC-01 | OK | Evidência é neutra de escola; só produtores da hierarquia (Agentes) geram evidência primária; ICT não cria hipótese (irrelevante à Evidência). Não altera a hierarquia. |
| CC-02 | **Crítico — foco** | **Não redefinir CEM-001.** Toda estrutura/estado/lineage de evidência é do CEM-001; SPEC-002 só adiciona a camada operacional. |
| CC-03 | OK | SPEC-002 **não** computa convicção; Evidence Strength ≠ Convicção (CEM Cap.3); dimensionalidade=8 intocada; J-001 aberta. |
| CC-04 | OK | Nenhuma das 5+5 Salvaguardas violada; custo não entra em nada de evidência. |
| CC-05 | OK | CRITICAL declarado. |
| CC-06/CC-07 | Diferido ao Plan | Engineering Cards com campos SES-001 §59 + cadeia §60 na redação. |
| **CC-08** | **Aplica — foco** | **Bloco Herança/Delta obrigatório no Plan:** INHERITS = CEM-001 (ID+versão baseline) + CHM-001 (relação) + SPEC-001 (padrão/fronteira). REMOVED vazio. Nenhum ADDED pode contradizer o herdado (RULE-HD-02). |
| CC-09 | Aplica — foco | Ausência≠contraevidência; INDETERMINADO como estado válido; sem falsa precisão (qualidade qualitativa até J-001). |
| CC-10 | Aplica | Declarar acepção: Evidência (CEM) vs Observação (Skill, INV-06); "provenance" vs "lineage" (CEM Cap.5); não redefinir termo canônico. |
| CC-11 | Aplica (§5) | Classe por BASpec no Plan; H/P com bounded loop + gate; C compatível com E3. |
| CC-12 | **NÃO incide** | SPEC-002 não é Spec de especialidade de domínio (CEM domain-neutral); nenhum `PD-xx`. |

---

## 7. Achado a reportar (correção de referência de localização do CEM-001)

O material de instrução da tarefa apontou o CEM-001 como estando em `canon/CEE-001-cognitive-economy-efficiency-v2.0.md`. **Isso está incorreto:** `CEE-001` é o *Cognitive Economy & Efficiency* (economia/4Es/salvaguardas). O **CEM-001 (Canonical Evidence Model)** vive em **`canon/CEM-001-canonical-evidence-model.md`** (baseline, DHR-TAX-001) — confirmado por Glob/Grep. A SPEC-002 constrói sobre o **CEM-001**. Registrado como `[INFERÊNCIA]`/correção factual para o caller e para o Plan.

---

## 8. Próximo passo

Esta Proposta + o `DOSSIE-PESQUISA.md` seguem para **parecer do Revisor** sobre o processo do Dossiê (atomic-spec §15) e, em seguida, **homologação de Andraus** da definição (número, nome, fronteira, quantidade, Classe) **e** da `[DECISÃO NECESSÁRIA: SPEC-002-VERBATIM-001]` (RULE-ECC-04/WebFetch) — **antes** de qualquer `plan.md`/`checks.md`.

**Pronto para revisão.**
</content>
