# SPEC-046 — Spec-Time Context Caching Harness (Especificador/Revisor)

| Campo | Valor |
|---|---|
| ID | SPEC-046 — Spec-Time Context Caching Harness (Grupo B — Especificador/Revisor) |
| Versão | **1.1 (emenda candidata — aditiva a v1.0 baseline)** |
| Status | **HOMOLOGADA — BASELINE v1.1** (Andraus, 2026-09-28). v1.0: DHR-SPEC046-002 (abertura DHR-SPEC046-001). v1.1 (emenda aditiva — EC-SPEC046-03 + BASpecs CISS-001..004, caching inter-sessão): DHR-SPEC046-003. NÃO altera escopo/fronteira/Classe/EC-SPEC046-01 já homologados de v1.0 (INV-07/versionamento monotônico). |
| Fonte | `specs/features/SPEC-046/PROPOSTA-ABERTURA.md` + `DOSSIE-PESQUISA.md` (homologados, DHR-SPEC046-001); ROADMAP §25-bis/§26; atomic-spec.md v1.4 |
| Complexidade | HIGH |
| Profundidade-alvo | D0–D7 (standard) — com reforço adversarial (D8, ≥1 caso) para satisfazer o gate de maturidade L3 (atomic-spec §7), coerente com o precedente SPEC-021 |
| Profile (Claude Code) | standard (HIGH) — §7-bis (EUA-E18) aplicado nesta redação (Bloco A/B/C abaixo) |
| Posição no caminho crítico | **Paralela/fora de ordem** — aberta por decisão direta de Andraus (RULE-ECC-01), não substitui nem adia SPEC-002 (próximo trabalho da ordem regular) [FONTE: DHR-SPEC046-001 §1] |
| Nível de maturidade-alvo | **L3 Testável** — D5 (estado) + ≥3 cenários D7 + ≥1 adversarial D8 + revisão independente [FONTE: atomic-spec §7] |
| Método | atomic-spec.md **v1.4** |
| Regime normativo citado | **RULE-ECC-01/02/04** (Especificação Emergente + Captura Verbatim); **RULE-MECH-01..04** (Classe/Mecanismo — incide); **ENF-01..08** |
| Autor | Especificador Principal SOT |
| Data | 2026-09-28 |

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-09-28 | Plan candidato inicial. Sana ACH-MEN-01/02 do parecer de abertura (referências e citações verbatim já corrigidas em `PROPOSTA-ABERTURA.md`/`DOSSIE-PESQUISA.md`, DHR-SPEC046-001). Formaliza EC-SPEC046-01 (8 campos) + EC-SPEC046-02, 4 BASpecs com Classe declarada, D0–D8 (D8 de reforço). **HOMOLOGADA baseline (DHR-SPEC046-002).** |
| 1.1 | 2026-09-28 | **Emenda aditiva — Caching Inter-Sessão (CACHE-ISS-001).** Formaliza a extensão recomendada em `backlog/BL-025-CACHE-ISS-001-analise.md` (Opção A, confirmada por Andraus): novo **EC-SPEC046-03** (8 campos, nível **E3** — reavaliado, ver seção) para persistência inter-sessão do freshness_record via manifesto; **BASpecs CISS-001..004** (Classes D/H/C/C); extensões **D4-ISS** (reuso do hashing SHA-256 de `build_map.py`), **D5-ISS** (estados do manifesto: FRESH/STALE/ABSENT/CORROMPIDO), **D7-ISS** (3 cenários) + **D8-ISS** (1 adversarial: manifesto adulterado entre sessões). Novo Non-goal/limitação de honestidade (RULE-MET-01): economia de tokens condicionada a substrato de reuso cross-sessão. **Estritamente aditiva — não toca v1.0 baseline (INV-07).** Emenda candidata — aguarda Revisor + Andraus. |

---

## Nota de gate (passo 11-bis / RMR-001) — itens verificados nesta redação

[FONTE: RMR-001 §6; ROADMAP §23 passo 11-bis]

- **BL-024** — "CACHING SOT — proposta de arquitetura de caching" — abertura do Grupo B formalizada por DHR-SPEC046-001; este Plan é a continuação direta. Gatilho original (`evento:abertura da SPEC-002`) preservado sem alteração — esta linha de trabalho é registrada aditivamente, não o substitui (ver `DOSSIE-PESQUISA.md` §5). Sem ação nova neste Plan além de referência.
- **BL-008** — auditoria retroativa da SPEC-001 — segue `ATIVADO`, independente desta redação.
- **ACH-OBS-01** (DHR-SPEC046-001 §3) — status de BL-008 — não resolvido por este Plan; fora de escopo.
- Nenhum item `ATIVADO` novo disparado pela redação deste Plan. [INFERÊNCIA — coerente com RMR-001 §4]

---

## Sanamento dos achados Menores do parecer de abertura (DHR-SPEC046-001 §3)

| ID | Achado | Encaminhamento nesta rodada |
|---|---|---|
| ACH-MEN-01 | "RULE-ECC-01 item 5" citado sem itens numerados existirem em `governance/RULES.md:426-436` | **Sanado** em `PROPOSTA-ABERTURA.md` §5 (título e corpo) — citação agora referencia `RULE-ECC-01` diretamente, com trecho literal da regra entre aspas em vez de número de item inexistente. Mesma correção aplicada por consistência em `DOSSIE-PESQUISA.md` §5. |
| ACH-MEN-02 | SRC-02/SRC-04/SRC-05 sustentavam alegação carregada sem trecho entre aspas no corpo do Dossiê | **Verificado já sanado** em `DOSSIE-PESQUISA.md` §3 — as três fontes têm trecho literal entre aspas na frase que sustenta a alegação (`"1. Ordering — ... "`, `"GPTCache's realistic default has a 68% false-hit rate..."`, `"No Cache (baseline): 0% hit rate..."`), correspondendo aos arquivos `sources/SRC-02/04/05-*.txt`. |

Ambos os achados **sanados antes** da redação deste Plan, conforme instrução do gate.

---

## Constitution Check (CC-01..CC-12 — atomic-spec §10.5 + emendas)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** SPEC-046 é tooling de **spec-time** (caching de leitura de documentos-fonte pelo Especificador/Revisor); não realiza análise técnica de mercado nem toca a hierarquia analítica. Hierarquia **protegida, não tocada**. [INFERÊNCIA]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM/GMC/SDD/PPQ/SAS/CR):** nenhuma seção redefine estrutura de modelo canônico. O escopo é exclusivamente documentos de governança/processo do próprio harness (`ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `backlog/RMR-001_Painel_Backlog.md`), não objetos CHM-001/CEM-001. [FONTE: CONST-01; PROPOSTA-ABERTURA.md §0 Faseamento]
- [x] **CC-03 — Conviction Vector:** **N/A** — esta Spec não produz, consome nem referencia Conviction Vector; nenhum limiar numérico de convicção é tocado. J-001 (fórmula/pesos/limiares definitivos do Conviction Vector) permanece **em aberto/pendente** [DECISÃO NECESSÁRIA] — não fechada nem tocada por esta Spec.
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** **N/A** — nenhum sinal de trading, nenhum cálculo de custo entrando em convicção; esta Spec não produz sinal operacional.
- [x] **CC-05 — Complexidade declarada:** **HIGH, D0–D7** (com D8 de reforço para L3 — ver §7-bis abaixo).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — artefato é Spec/Plan, não Engineering Card; campos tornam-se obrigatórios na fase de Tasks/BUILD (adiada — atomic-spec §14). Omissão justificada, mesmo tratamento de SPEC-019/020/021.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06). Rastreabilidade de origem: ROADMAP (decisão de Andraus, fora de ordem) → `CACHING SOT.MD` (ref. externa, RPIR) → BL-024 → Dossiê/Proposta homologados (DHR-SPEC046-001) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver seção própria abaixo); INHERITS/ADDED preenchidos com ID+versão; REMOVED vazio; nenhum item ADDED/MODIFIED contradiz herdado (RULE-HD-02). Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** — SPEC-046 não é decomposição micro de nenhum macro-Spec já homologado (é linha paralela nova, não filha de SPEC-019/020/021).
- [x] **CC-09 — Status epistemológico / Epistemic Check:** aplicado — distinção FATO NORMATIVO (DHR-SPEC046-001, EC-SPEC046-01 homologado) / FATO ARQUITETURAL / PROPOSTA (script de implementação, ainda não decidido) / INFERÊNCIA / [EXTERNO] (7 fontes, ver Dossiê) explícita ao longo do documento. Nenhuma hipótese tratada como fato; escolha de veículo técnico (script novo vs. extensão de `check_doc_sync.py`) marcada [PROPOSTA], não fechada.
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM):** **N/A quanto a escola de mercado** (não é domínio Elliott/SMC/ICT). Aplicado de forma análoga a terminologia técnica concorrente ("cache semântico" vs. "correspondência exata/prefixo" vs. "cache HTTP do provedor") — distinção declarada explicitamente no Dossiê (SRC-06) e mantida consistente neste Plan (EC-SPEC046-01 opera no nível de releitura de arquivo, não no nível de `cache_control` do provedor).
- [x] **CC-11 — Classe/Mecanismo por BASpec (RULE-MECH-01, §10.6):** **INCIDE** — esta Spec cita RULE-MECH-01 no próprio texto (ver D2/D3). Cada BASpec com efeito declara Classe (D/H/P), critério 4Es, bounded loop/gate de saída onde H/P. Nenhuma Classe C proposta (risco E2, não E3 — Classe C reservada a enforcement de risco alto, seria violação de Economicidade aqui). Classe predominante da Spec (já homologada na abertura, DHR-SPEC046-001 §2.2): **H**.
- [x] **CC-12 — Princípios de Domínio (RULE-PD-01, §10.7):** **N/A confirmado pelo Revisor no parecer de abertura** (instrução do coordenador) — SPEC-046 não define escopo de especialidade de domínio de mercado (não é Elliott/Fibonacci/SMC/ICT/estrutural). Nenhum `PD-xx` proposto.

**Checklist de consistência principiológica (GPR-001 §15):** PC-02 (SOT não executa) reforçada — o mecanismo de freshness **detecta e recomenda** (reler/rebaixar etiqueta), nunca "executa" no sentido de INV-05/RULE-DEC; 4Es na ordem (Eficácia>Efetividade>Eficiência>Economicidade — AGENTS.md §6 item 11; critério explícito em EC-SPEC046-01 §"Critério 4Es"); rastreabilidade (cada verificação de hash gera evidência auditável); PB-10 (preservação da incerteza) honrada pelo FAILURE-MODE fail-closed (rebaixar para [INFERÊNCIA]/[DECISÃO NECESSÁRIA] em vez de forçar [FONTE]). Item CLASSE-MECH-001 do §15: cada BASpec com efeito declara Classe (CC-11). Item PRINC-BID-001: N/A (CC-12).

**Disciplinas cognitivas N8–N17 incidentes:** RULE-EPI (conteúdo não revalidado não pode ser apresentado como [FONTE]; INDETERMINADO quando releitura não é possível), RULE-MET-01 (não-fabricação — nenhuma métrica de hit-rate/FHR é inventada; CacheEval/semantic-cache-bench explicitamente marcados "não transferíveis sem re-execução no ambiente SOT"), RULE-DEC (decisão≠execução — a verificação de freshness **relata**, quem decide reler/prosseguir é o agente, sob fail-closed), RULE-UNC (incerteza de freshness localizada ao documento específico, não contamina outras afirmações da mesma entrega).

---

## §7-bis — Autopré-check de Redução de Viés (obrigatório HIGH/CRITICAL — EUA-E18)

### Bloco A — Pergunta adversarial por BASpec (D8 aplicado)

Aplicado às 4 BASpecs desta Spec (todas HIGH, nenhuma CRITICAL isolada, mas §7-bis é obrigatório para a Spec como um todo por ser HIGH):

- **BASpec-C46-001 (captura de hash):** "Se esta BASpec estivesse errada, o que seria observável?" → um hash registrado não corresponderia ao SHA-256 real do conteúdo lido (verificável por recomputação independente). "O ENTÃO é verificável por observador independente?" → sim, hash é recomputável por qualquer processo com acesso ao arquivo. "Existe condição em que QUANDO se satisfaz mas ENTÃO não deve ocorrer?" → sim: leitura parcial/truncada do arquivo (ex.: limite de tokens) produziria hash de um conteúdo incompleto — tratado como caso adversarial (ADV-C46-02, abaixo, generalizado para "não verificável").
- **BASpec-C46-002 (verificação de freshness):** caso de negação = hash bate mas o agente reutiliza de qualquer forma um conteúdo que na verdade não é mais representativo (ex.: arquivo foi reescrito para o MESMO conteúdo por coincidência após ser alterado e revertido) — **risco aceito e declarado**: correspondência exata de hash é uma garantia de **conteúdo idêntico no momento da checagem**, não de "nunca mudou entretanto"; isso é suficiente para o objetivo desta Spec (impedir uso de conteúdo *comprovadamente diferente*), não uma garantia absoluta de imutabilidade histórica — documentado como limitação (ver Non-goals/Limitações).
- **BASpec-C46-003 (rebaixamento de etiqueta):** negação = sistema apresenta [FONTE] mesmo quando a releitura falhou — coberto por ADV-C46-01/02 abaixo (fail-closed obrigatório).
- **BASpec-C46-004 (higiene de sessão):** menor risco — é F.3 Feedback, não Enforcement; negação = checklist não detecta uma violação real de ordenação — aceito como limitação de Classe D (checklist determinístico simples, não semântico).

### Bloco B — Herança obrigação-a-obrigação (CC-08)

Não há canônico-pai (CHM-001/CEM-001/GMC-001 etc.) do qual esta Spec herde obrigações operacionais diretas — herda apenas **método** (atomic-spec v1.4) e os **termos já homologados na abertura** (PROPOSTA-ABERTURA.md/DOSSIE-PESQUISA.md, DHR-SPEC046-001). Verificação: (1) obrigações herdadas da abertura = número/nome/fronteira Grupo B/EC-SPEC046-01/Classe H — todas preservadas neste Plan sem alteração (ver Herança/Delta); (2) evidência de satisfação = seções correspondentes deste Plan citam DHR-SPEC046-001 linha a linha; (3) nenhuma obrigação da abertura foi suprimida ou contradita (RULE-HD-02/03) — confirmado por leitura cruzada.

### Bloco C — Verificação epistêmica (RULE-EPI-01..03 / CC-09)

- Afirmação causal única desta Spec ("hash divergente ⇒ conteúdo mudou") tem mecanismo declarado (propriedade criptográfica de SHA-256 — colisão desprezível) — compatível com RULE-CAU-01/RULE-EPI-02, não é correlação.
- Nenhuma hipótese tratada como fato — status "veículo técnico (script)" mantido [PROPOSTA], não fechado.
- Incerteza material (releitura impossível) usa INDETERMINADO/[DECISÃO NECESSÁRIA] em vez de forçar PASS/FAIL — ver BASpec-C46-003.
- Nenhuma probabilidade declarada sem evento bem-formado (RULE-PRB-01) — esta Spec não usa nenhuma métrica probabilística (FHR/hit-rate de CacheEval/semantic-cache-bench explicitamente **não** importados como número).
- Nenhuma precisão numérica sem base — SHA-256 é determinístico (não há "precisão" a falsear); nenhum limiar percentual é proposto.

### Bloco D — reforço de escopo

- Esta Spec não produz recomendação/TMP nem cruza fronteira SOT→execução downstream — **N/A** (não é Spec de domínio de decisão de trading; INV-05/RULE-DEC não incidem diretamente, mas RULE-DEC é citada acima como disciplina geral aplicável a "decisão≠execução" também no nível de tooling).
- Nenhuma dependência de decisão de Andraus tratada como fato — "veículo técnico" permanece [PROPOSTA].

---

## Herança / Delta (§8.3 — EUA-E04)

```
HERANÇA / DELTA — SPEC-046

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO):
  - Método: atomic-spec.md v1.4 — BASpec/EARS/Enforcement/Classe/D0-D9/F.1-F.4/TRACE-06
  - Abertura homologada: PROPOSTA-ABERTURA.md v1.0 + DOSSIE-PESQUISA.md v1.0 (DHR-SPEC046-001,
      2026-09-28) — número (SPEC-046), nome, fronteira (Grupo B), Classe predominante (H),
      Enforcement Contract EC-SPEC046-01 (8 campos, precondição hash/mtime-git, fail-closed, E2)
  - Governança do Harness: RULE-ECC-01/02/04 (RULES.md), ENF-01..08, RULE-MECH-01..04
  - Invariantes: INV-09 (sem baseline informal), TRACE-06 (etiquetagem), CONS-01 (decisão aberta
      não vira invariante fechado)

ADDED (delta local — o que este Plan acrescenta sobre a abertura homologada):
  - 4 BASpecs com Classe declarada (BASpec-C46-001..004)
  - Algoritmo D4 (cálculo/comparação de hash SHA-256, com exemplo numérico)
  - Máquina de estados D5 (FRESH/STALE/UNVERIFIABLE de um registro de freshness)
  - Protocolo D6 — declarado N/A justificado (não há Blackboard/Event Bus envolvido; ver Non-goals)
  - Cenários D7 (4, um por BASpec) + Adversarial D8 (4 casos, reforço para L3)
  - Schema I/O do "freshness_record"
  - EC-SPEC046-02 (novo, nível E1) para a auditoria de higiene de sessão (BASpec-C46-004)
  - (v1.1, aditivo) EC-SPEC046-03 (novo, nível E3 — reavaliado, não herdado do E2 de EC-SPEC046-01)
      + BASpecs CISS-001..004 (Classes D/H/C/C) + D4-ISS/D5-ISS/D7-ISS/D8-ISS + manifesto
      inter-sessão em docs/cache/ (reuso do hashing de build_map.py) + Non-goal/limitação L-ISS-01.
      Estritamente ADITIVO — não altera nem contradiz o EC-SPEC046-01/escopo/Classe de v1.0 (INV-07)

MODIFIED (especialização de regra herdada):
  - (nenhuma — EC-SPEC046-01 é formalizado aqui nos 8 campos completos do atomic-spec §10.3,
    mas o CONTEÚDO normativo — precondição, nível E2, fail-closed — é o mesmo já homologado
    em DHR-SPEC046-001 §2.2; não há alteração de substância, apenas preenchimento formal)

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança:** eixo VERTICAL (RULE-HV) **não aplicável** — SPEC-046 não decompõe nenhum macro-Spec já homologado; é uma linha de trabalho nova e paralela, não filha. [INFERÊNCIA — a confirmar pelo Revisor]

---

## D0 — Missão (Intenção)

O Spec-Time Context Caching Harness especifica **como os agentes Especificador e Revisor podem reutilizar, com segurança epistêmica, conteúdo de documentos-fonte do próprio repositório já lido na mesma sessão/turno** — sem que essa reutilização permita fundamentar uma afirmação `[FONTE]` em uma versão desatualizada de `ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `backlog/RMR-001_Painel_Backlog.md` ou documento equivalente. [FONTE: PROPOSTA-ABERTURA.md §2, §6]

A Spec **não** especifica caching de hipóteses/evidências de mercado (Grupo A — CHM-001/CEM-001), nem configura o mecanismo nativo de `cache_control` do provedor (que já é gerenciado automaticamente e é fail-safe quanto a alteração de bloco — SRC-06). Especifica a camada **acima** desse mecanismo: a precondição de que uma cópia de documento mantida em contexto de sessão ainda corresponde ao estado atual do arquivo no repositório.

**Status epistemológico:** SPEC-046 é FATO ARQUITETURAL candidato a baseline; a abertura (número/nome/fronteira/Classe/EC-SPEC046-01) já é FATO NORMATIVO (DHR-SPEC046-001).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| Item | Descrição | Fonte |
|---|---|---|
| Precondição de freshness | Hash de conteúdo (SHA-256) ou mtime/commit git como condição de reutilização de leitura anterior | EC-SPEC046-01; SRC-06; SRC-07 |
| Documentos-alvo | `ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `backlog/RMR-001_Painel_Backlog.md`, `governance/CONSTITUTION.md`, `governance/CONFLICT-MAP.md`, `GLOSSARIO.md`, `AGENTS.md` (lista indicativa, extensível) | PROPOSTA-ABERTURA.md §2 |
| Rebaixamento de etiqueta | Quando freshness não verificável, afirmação correspondente não pode ser `[FONTE]` | TRACE-06; CC-09 |
| Auditoria de higiene de sessão (complementar) | Checklist adaptado de SRC-01/SRC-02 (ordenação, injeção de mensagem, fork safety) — F.3 Feedback, não Enforcement principal | SRC-01; SRC-02 |
| Agentes cobertos | Exclusivamente Especificador e Revisor (Grupo B) | DHR-SPEC046-001 §1 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Grupo A — caching de evidências/hipóteses (CHM-001/CEM-001) dos agentes cognitivos internos | Futura SPEC-047 (ou número seguinte) | Faseamento deliberado, decisão de Andraus (DHR-SPEC046-001 §1) |
| ACHADO-M2 (precondição de estado CHM-001 antes de cache HIT) | Futura SPEC-047 | Aplica-se ao Grupo A; não se aplica aqui (Grupo B não manipula hipóteses de mercado) |
| Configuração de `cache_control`/TTL do provedor Anthropic | Fora do harness SOT (infraestrutura de runtime do Claude Code/SDK, não spec-time do SOT) | O mecanismo nativo já é gerenciado pelo provedor e é fail-safe por hash cumulativo de prefixo (SRC-06) — esta Spec opera num nível acima |
| Aplicação automática de correções/patches ao harness (padrão SRC-03) | Rejeitado, não é non-goal temporário | Colide com ENF-03/INV-09 — ver ADV-C46-04 |
| Cache semântico/aproximado (embeddings, similaridade) | Fora de escopo permanente para o Grupo B | Grupo B usa correspondência exata (hash); cache semântico é regime do Grupo A/futuro, se algum dia justificado |
| Interação com Blackboard/Event Bus | N/A — Especificador/Revisor não publicam em Blackboard (isso é runtime cognitivo, SPEC-004/005) | Protocolo D6 declarado N/A justificado abaixo |
| Veículo técnico definitivo de implementação (script novo vs. extensão de `check_doc_sync.py`) | Decisão de implementação, marcada [PROPOSTA] nesta Spec | Não bloqueia o comportamento especificado; é detalhe de BUILD |
| **(v1.1) Recolocar conteúdo de documento-fonte no contexto do LLM entre sessões** | Fora de escopo permanente do EC-SPEC046-03 | Um manifesto de hashes **não** recarrega conteúdo em contexto — apenas autoriza confiar (ou não) em um substrato de reuso cross-sessão externo. Ver Limitação L-ISS-01 abaixo (RULE-MET-01). |

### Limitações declaradas (RULE-MET-01 — não-fabricação)

Correspondência de hash garante **conteúdo idêntico no momento da checagem** — não garante que o arquivo nunca foi alterado e revertido para o mesmo conteúdo entre a leitura original e o uso (ver §7-bis Bloco A). Essa limitação é aceita: o objetivo desta Spec é impedir uso de conteúdo **comprovadamente diferente**, não oferecer uma prova de imutabilidade histórica absoluta.

**(v1.1) L-ISS-01 — a economia de tokens NÃO é entregue pelo manifesto isolado (honestidade RULE-MET-01).** O EC-SPEC046-03 (caching inter-sessão) é um **freshness guard**, não um mecanismo de recarga de contexto. Numa sessão nova, o conteúdo dos documentos-núcleo **não está** em contexto; o manifesto de hashes apenas informa, de forma fail-closed, **se é seguro confiar** em um substrato de reuso cross-sessão (ex.: prompt-cache do provedor com TTL longo, ou um snapshot armazenado). A economia real de leitura (ordem de 10⁴–10⁵ tokens/sessão — [ESTIMATIVA], `BL-025-CACHE-ISS-001-analise.md` §2.c) **só se materializa se esse substrato de reuso existir**; sem ele, o ganho do manifesto é apenas evitar re-verificação semântica redundante, **não** a leitura em si. Isto é declarado como **limitação/Non-goal, não como promessa da capacidade** — o EC-SPEC046-03 não deve ser apresentado como "reduz tokens" isoladamente. Análogo estrutural: RULE-C46-004 (o guard é independente do cache nativo do provedor).

---

## D2 — Regras

```
RULE-C46-001: Toda leitura de documento-fonte do escopo (D1) pelo Especificador ou Revisor DEVE
              registrar hash SHA-256 do conteúdo lido, associado ao path e ao momento da leitura,
              disponível para verificação posterior na mesma sessão/turno.
              [FONTE: EC-SPEC046-01; SRC-07] [PROPOSTA — RULE-MECH-01 incide: Classe D]

RULE-C46-002: Toda afirmação classificada [FONTE] que se apoie em conteúdo de documento-fonte
              NÃO relido no momento do uso DEVE ter sua precondição de freshness verificada
              (hash ou mtime/commit git) antes de ser apresentada como [FONTE].
              [FONTE: EC-SPEC046-01; TRACE-06] [PROPOSTA — Classe H]

RULE-C46-003: Quando a precondição de RULE-C46-002 falhar ou não puder ser verificada, a
              afirmação correspondente NÃO PODE ser etiquetada [FONTE] — DEVE ser rebaixada a
              [INFERÊNCIA] ou [DECISÃO NECESSÁRIA], com nota explícita de fonte não revalidada.
              Fail-closed (ENF-04 — efeito crítico *para a integridade da entrega*, ainda que
              nível E2, não E3).
              [FONTE: TRACE-06; RULE-EPI-01; CC-09] [PROPOSTA — Classe P]

RULE-C46-004: A verificação de freshness (RULE-C46-002) é INDEPENDENTE do mecanismo nativo de
              `cache_control` do provedor Anthropic — a existência de um cache HTTP ativo NUNCA
              substitui nem dispensa a verificação de hash/mtime do arquivo-fonte no repositório.
              [FONTE: SRC-06] [PROPOSTA — reforça RULE-C46-002, não cria BASpec própria]

RULE-C46-005: Nenhuma correção automática de configuração de caching (patches ao harness, padrão
              SRC-03) pode ser aplicada sem revisão humana explícita e homologação — mesmo
              princípio de ENF-03/INV-09 já aplicado a BL-020/DHR-VERBATIM-SRC-001.
              [FONTE: ENF-03; INV-09; DHR-VERBATIM-SRC-001] [PROPOSTA — Classe C rejeitada; ver ADV-C46-04]
```

---

## Critérios de Aceitação (EARS)

Os critérios de aceitação seguem notação EARS ("Quando <condição>, o componente DEVE <resposta>"):

1. Quando o Especificador ou o Revisor lê, pela primeira vez na sessão/turno, um documento-fonte do escopo (D1), o sistema DEVE registrar um freshness_record com hash SHA-256 do conteúdo lido.
2. Quando o Especificador ou o Revisor pretende fundamentar uma afirmação [FONTE] em conteúdo de documento-fonte já lido anteriormente na sessão, o componente DEVE verificar se o hash atual do arquivo corresponde ao hash registrado antes de autorizar a reutilização.
3. Quando o hash atual diverge do hash registrado (ou o freshness_record está ausente), o componente DEVE rejeitar a reutilização e exigir releitura do arquivo antes de qualquer afirmação [FONTE].
4. Quando a releitura exigida não for possível no momento, o componente DEVE rebaixar a etiqueta da afirmação correspondente para [INFERÊNCIA] ou [DECISÃO NECESSÁRIA], nunca [FONTE].
5. Quando um cache HIT do mecanismo nativo do provedor (cache_control) for reportado, o componente NÃO DEVE tratar esse HIT como equivalente à verificação de freshness do arquivo-fonte no repositório.
6. Quando um mecanismo automatizado propuser aplicar correção de configuração de caching diretamente aos arquivos do harness, o componente DEVE rejeitar a aplicação automática sem revisão humana e homologação explícitas.
7. Quando o Especificador ou o Revisor estrutura um prompt de sessão com múltiplos documentos-fonte, o componente DEVE verificar (checklist determinístico) que o conteúdo estável precede o conteúdo variável de sessão.

---

## D3 — Comportamento (BASpecs) — Classe declarada (RULE-MECH-01, CC-11)

### BASpec-C46-001 — Captura de hash na leitura inicial

```
CLASSE        : D (Determinístico)
MECANISMO     : cálculo de hash SHA-256 do conteúdo lido — código puro, sem julgamento do LLM
CRITÉRIO 4Es  : Eficácia — só um hash criptográfico dá garantia binária de identidade de conteúdo;
                não há alternativa mais barata (Economicidade) que preserve a mesma garantia

BASpec-C46-001:
  QUANDO:       Especificador ou Revisor lê, pela primeira vez na sessão/turno, um documento-fonte
                do escopo (D1) — ROADMAP.md, atomic-spec.md, governance/RULES.md,
                governance/CATALOGO-OFICIAL.md, backlog/RMR-001_Painel_Backlog.md ou equivalente
  ENTÃO:        Sistema registra um freshness_record: {path, hash_algorithm="SHA-256", hash_value,
                read_at (timestamp), source_commit (quando disponível via git)}, associado a essa
                leitura, disponível para comparação posterior na mesma sessão
  PORQUE:       Sem esse registro não há base de comparação para a precondição de freshness
                (EC-SPEC046-01) — fundamenta RULE-C46-001
  REFERÊNCIA:   RULE-C46-001; EC-SPEC046-01; SRC-07
  VERIFICADO POR:
    DADO        Especificador lê ROADMAP.md pela 1ª vez no turno T1
    QUANDO      a leitura é concluída
    ENTÃO       sistema registra {path: "ROADMAP.md", hash_algorithm: "SHA-256",
                hash_value: sha256(conteúdo lido), read_at: T1}
    VERIFICAÇÃO freshness_record.hash_value == sha256(conteúdo real do arquivo em T1)
```

### BASpec-C46-002 — Verificação de freshness antes de reutilizar leitura anterior

```
CLASSE        : H (Híbrido)
MECANISMO     : comparação de hash é determinística (Classe D isolada), mas a reação
                (autorizar reuso / exigir releitura) é decisão do agente com gate de saída
                verificável por código — por isso Híbrido
CRITÉRIO 4Es  : Eficácia — a comparação exata é a única forma de garantir que a afirmação
                subsequente não se apoia em conteúdo comprovadamente diferente
BOUNDED LOOP  : no máximo 1 releitura automática por arquivo por invocação desta precondição —
                sem retry infinito (RULE-MECH-03)
GATE DE SAÍDA : comparação de hash_value atual vs. registrado — determinística, verificável por
                código, não por autoavaliação do LLM (ENF-03)

BASpec-C46-002:
  QUANDO:       Especificador ou Revisor pretende fundamentar uma afirmação [FONTE] em conteúdo
                de um documento-fonte já lido anteriormente na mesma sessão/turno (não relido
                imediatamente antes do uso)
  ENTÃO:        Sistema recalcula hash_value atual do arquivo e compara com o freshness_record
                registrado (BASpec-C46-001). SE idêntico → autoriza reutilização (cache HIT,
                afirmação pode ser [FONTE]). SE diferente ou freshness_record ausente/não
                recuperável → NÃO autoriza reutilização; exige 1 releitura do arquivo antes de
                prosseguir (bounded loop)
  PORQUE:       EC-SPEC046-01 — fail-closed; nenhuma afirmação [FONTE] pode se apoiar em
                conteúdo potencialmente desatualizado; fundamenta RULE-C46-002 e RULE-C46-004
  REFERÊNCIA:   EC-SPEC046-01; RULE-C46-002; RULE-C46-004; INV-09
  VERIFICADO POR:
    DADO        freshness_record de governance/RULES.md registrado em T1 com hash_value = H1;
                o arquivo é modificado por outro agente/hook em T2 (H2 != H1)
    QUANDO      Especificador tenta fundamentar uma afirmação [FONTE] em T3 usando a cópia da
                leitura T1, sem reler
    ENTÃO       sistema recalcula hash atual = H2; H2 != H1 → reutilização REJEITADA; sistema
                exige releitura antes de a afirmação ser produzida como [FONTE]
    VERIFICAÇÃO afirmação [FONTE] não é emitida sem releitura confirmada (H_novo == H_arquivo_atual);
                evento registrado como MISS
```

### BASpec-C46-003 — Rebaixamento de etiqueta quando releitura não é possível

```
CLASSE        : P (Probabilístico com Gate)
MECANISMO     : julgamento qualitativo do agente sobre se a afirmação ainda é sustentável como
                [INFERÊNCIA] ou deve virar [DECISÃO NECESSÁRIA] — sem verificação binária direta
                (diferente da comparação de hash, que É binária)
CRITÉRIO 4Es  : Conformidade/Eficácia — nunca apresentar [FONTE] não revalidada, mesmo que isso
                custe reformular a afirmação (Economicidade não rebaixa — AGENTS.md §6 item 11)
BOUNDED LOOP  : 1 tentativa de releitura (herdada de BASpec-C46-002); se falhar, decide
                imediatamente entre [INFERÊNCIA] e [DECISÃO NECESSÁRIA] — sem loop adicional

BASpec-C46-003:
  QUANDO:       a verificação de freshness (BASpec-C46-002) falha E o arquivo não pode ser
                relido no momento (ex.: indisponibilidade transitória, erro de I/O)
  ENTÃO:        a afirmação correspondente é etiquetada [INFERÊNCIA] (se o conteúdo original
                ainda for plausivelmente representativo, com ressalva) ou [DECISÃO NECESSÁRIA]
                (se a divergência de hash sugerir mudança material) — nunca [FONTE] — com nota
                explícita "fonte não revalidada nesta sessão; hash divergente detectado em
                <timestamp>" ou "releitura impossível em <timestamp>"
  PORQUE:       TRACE-06 (etiquetagem de status epistemológico); RULE-EPI-01 (hipótese≠fato);
                fundamenta RULE-C46-003
  REFERÊNCIA:   TRACE-06; RULE-EPI-01; RULE-C46-003; EC-SPEC046-01 FAILURE-MODE
  VERIFICADO POR:
    DADO        releitura de governance/CATALOGO-OFICIAL.md falha (arquivo temporariamente
                inacessível) após hash divergente detectado
    QUANDO      Especificador precisa fundamentar uma afirmação que dependeria desse conteúdo
    ENTÃO       etiqueta da afirmação é rebaixada para [INFERÊNCIA] (ou [DECISÃO NECESSÁRIA],
                conforme severidade) com nota de ressalva explícita
    VERIFICAÇÃO nenhuma ocorrência de [FONTE] sem freshness_record validado no mesmo turno para
                o documento correspondente
```

### BASpec-C46-004 — Auditoria de higiene de sessão (complementar, F.3 Feedback)

```
CLASSE        : D (Determinístico)
MECANISMO     : checklist determinístico adaptado de SRC-01/SRC-02 — verificação de ordem/estrutura
                de prompt, não de conteúdo semântico
CRITÉRIO 4Es  : Eficiência — reduz cache misses desnecessários no mecanismo nativo do provedor;
                não é a defesa principal de Eficácia desta Spec (essa é EC-SPEC046-01/BASpecs 001-003)

BASpec-C46-004:
  QUANDO:       Especificador ou Revisor estrutura um prompt/instrução de sessão que inclui
                conteúdo de múltiplos documentos-fonte do escopo (D1)
  ENTÃO:        Sistema verifica (checklist adaptado de SRC-01 "estabilidade de prefixo" e
                SRC-02 "6 regras", ambos [EXTERNO]/adaptar) que: (a) conteúdo estável
                (ROADMAP/atomic-spec/RULES) precede conteúdo variável de sessão; (b) o prompt de
                sistema não é editado em voo fora de tags de sistema apropriadas; (c) ferramentas
                não são adicionadas/removidas sem necessidade em meio à sessão
  PORQUE:       Reduz cache misses desnecessários no cache nativo do provedor (SRC-06); NÃO
                resolve o risco de staleness documental (isso é EC-SPEC046-01/BASpecs 001-003) —
                é F.3 Feedback complementar de eficiência, não Enforcement principal
  REFERÊNCIA:   SRC-01; SRC-02; SRC-06; atomic-spec §5 (F.3)
  VERIFICADO POR:
    DADO        uma sessão nova do Especificador
    QUANDO      ele monta o prompt/contexto inicial da sessão
    ENTÃO       ordem observada é documentos estáveis (ROADMAP→atomic-spec→RULES) antes de
                conteúdo variável de turno
    VERIFICAÇÃO checklist das 6 regras adaptadas de SRC-02 sem violação registrada
```

---

## D4 — Algoritmo (hash de conteúdo)

```
ALGORITMO: verify_freshness
ENTRADA:  path (string) · hash_registrado (string, hex SHA-256) · conteúdo_atual (bytes do arquivo)
PROCESSO:
  1. hash_atual = SHA-256(conteúdo_atual)
  2. SE hash_atual == hash_registrado:
       retornar FRESH
     SENÃO:
       retornar STALE
  3. SE conteúdo_atual não pôde ser lido (erro de I/O):
       retornar UNVERIFIABLE (nunca presumir FRESH por omissão — fail-closed)
SAÍDA:    estado ∈ {FRESH, STALE, UNVERIFIABLE}
EXEMPLO:  hash_registrado = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3" (exemplo ilustrativo,
          truncado); conteúdo_atual = bytes idênticos ao momento da leitura original →
          hash_atual = mesmo valor → FRESH. Se uma única linha de `governance/RULES.md` for
          editada (ex.: nova RULE inserida), hash_atual muda completamente (efeito avalanche do
          SHA-256) → STALE, mesmo que a mudança seja "pequena" em bytes.
```

---

## D5 — Estados (freshness_record)

```
Estado: NÃO-REGISTRADO → (leitura ocorre, BASpec-C46-001) → transição para REGISTRADO
Estado: REGISTRADO → (verificação, BASpec-C46-002) → transição para FRESH quando hash bate
Estado: REGISTRADO → (verificação, BASpec-C46-002) → transição para STALE quando hash diverge
Estado: REGISTRADO → (verificação, BASpec-C46-002, I/O falha) → transição para UNVERIFIABLE
Estado: STALE → (releitura bem-sucedida) → volta a REGISTRADO (novo hash) → FRESH
Estado: STALE / UNVERIFIABLE → (releitura impossível, BASpec-C46-003) → afirmação correspondente
        rebaixada a [INFERÊNCIA]/[DECISÃO NECESSÁRIA]; freshness_record permanece STALE/UNVERIFIABLE
        até nova leitura bem-sucedida (não regride nem se apaga — INV-09/TRACE-06, análogo a
        INV-07 embora não seja hipótese CHM-001)
```

Nenhuma transição permite ir diretamente de STALE/UNVERIFIABLE para "autorizado como [FONTE]" sem passar por uma nova leitura bem-sucedida (fail-closed).

---

## D6 — Protocolo de Publicação no Blackboard

**N/A — justificado.** Especificador e Revisor **não publicam objetos no Blackboard Cognitivo** (esse é o workspace de runtime cognitivo dos agentes analíticos — SPEC-004/005, Grupo A/futuro). O "freshness_record" desta Spec é um artefato **interno à sessão de spec-time** (ou, na implementação, um artefato de tooling em `scripts/`/estado de sessão do Claude Code) — não um objeto CHM-001/CEM-001 publicado em memória de trabalho compartilhada entre agentes cognitivos. Declarado N/A explicitamente (não omitido) — coerente com CC-02/CC-04 (nenhum modelo canônico ou salvaguarda de sinal tocado).

---

## D7 — Cenários de Teste

### Cenário-C46-T01 — Captura de hash válida
```
DADO        Especificador inicia sessão e lê ROADMAP.md pela primeira vez
QUANDO      a leitura é concluída
ENTÃO       freshness_record = {path: "ROADMAP.md", hash_algorithm: "SHA-256",
            hash_value: <sha256 real>, read_at: <timestamp>}
VERIFICAÇÃO hash_value recomputado bate byte-a-byte com o conteúdo lido
```

### Cenário-C46-T02 — Reutilização autorizada (FRESH)
```
DADO        freshness_record de atomic-spec.md registrado em T1; arquivo não foi alterado até T2
QUANDO      Especificador fundamenta uma afirmação [FONTE] em T2 usando a cópia de T1
ENTÃO       sistema recalcula hash em T2, confirma identidade com T1 → reutilização autorizada
VERIFICAÇÃO afirmação é apresentada como [FONTE] legitimamente (hash_atual == hash_registrado)
```

### Cenário-C46-T03 — Reutilização negada (STALE) → releitura obrigatória
```
DADO        freshness_record de governance/RULES.md registrado em T1; arquivo alterado em T2
            (nova RULE-XXX-01 inserida por Andraus/outro agente)
QUANDO      Revisor tenta fundamentar uma verificação [FONTE] em T3 usando a cópia de T1
ENTÃO       sistema detecta hash_atual != hash_registrado → REJEITA reutilização; exige releitura
VERIFICAÇÃO nenhuma afirmação [FONTE] é emitida antes da releitura confirmar novo hash
```

### Cenário-C46-T04 — Releitura impossível → rebaixamento de etiqueta
```
DADO        hash divergente detectado para governance/CATALOGO-OFICIAL.md; arquivo
            temporariamente inacessível para releitura
QUANDO      Especificador precisa prosseguir com a entrega
ENTÃO       afirmação correspondente é etiquetada [INFERÊNCIA] com nota "fonte não revalidada;
            hash divergente detectado em <timestamp>" — nunca [FONTE]
VERIFICAÇÃO etiqueta da afirmação != [FONTE]; nota de ressalva presente no texto da entrega
```

---

## D8 — Adversarial (reforço para gate de maturidade L3)

> Esta Spec é HIGH (não CRITICAL); D8 não é tecnicamente obrigatório pela tabela de profundidade (atomic-spec §2), mas é exigido pelo **gate de maturidade L3** (atomic-spec §7: "D5 + ≥3 cenários D7 + ≥1 adversarial D8 + revisão independente") e reforçado pelo §7-bis Bloco A (obrigatório para HIGH). Mesmo tratamento do precedente SPEC-021.

### ADV-C46-01 — Apresentar [FONTE] sem verificação de freshness
**DADO:** conteúdo de `governance/RULES.md` lido há vários turnos, nunca revalidado
**QUANDO:** agente tenta fundamentar uma afirmação [FONTE] usando essa cópia, sem invocar BASpec-C46-002
**ENTÃO:** sistema DEVE rejeitar a etiquetagem [FONTE] até a verificação de freshness ocorrer
**PORQUE:** RULE-C46-002; TRACE-06; fail-closed (EC-SPEC046-01)
**VERIFICAÇÃO:** nenhuma entrega final contém [FONTE] sem freshness_record correspondente no mesmo turno

### ADV-C46-02 — Hash não computável (leitura truncada/parcial)
**DADO:** arquivo lido apenas parcialmente (ex.: limite de contexto truncou a leitura)
**QUANDO:** sistema tenta registrar freshness_record a partir dessa leitura parcial
**ENTÃO:** sistema DEVE marcar o registro como UNVERIFIABLE (nunca computar hash de conteúdo incompleto e apresentá-lo como válido)
**PORQUE:** BASpec-C46-001 exige hash do conteúdo efetivamente lido; leitura parcial não representa o arquivo inteiro — fail-closed (D4 §PROCESSO passo 3)
**VERIFICAÇÃO:** freshness_record de leitura parcial nunca transiciona para FRESH sem releitura completa

### ADV-C46-03 — Confundir cache HTTP do provedor com verificação de freshness documental
**DADO:** um bloco de prompt está marcado com `cache_control` e o provedor reporta cache HIT (nível de infraestrutura)
**QUANDO:** agente presume que esse HIT do provedor garante que o conteúdo do arquivo-fonte também está atualizado
**ENTÃO:** sistema DEVE rejeitar essa equivalência — cache HIT do provedor (SRC-06) é sobre reuso de computação de prefixo, não sobre freshness do arquivo no repositório; RULE-C46-002 permanece obrigatória independentemente
**PORQUE:** RULE-C46-004; SRC-06 (mecanismo nativo é keyed por hash de PREFIXO DE PROMPT, não por hash de ARQUIVO-FONTE)
**VERIFICAÇÃO:** nenhuma entrega justifica ausência de verificação de freshness citando "cache do provedor ativo"

### ADV-C46-04 — Aplicação automática de correção de caching ao harness
**DADO:** um mecanismo automatizado (padrão SRC-03/prompt-cache-skills) propõe aplicar um patch de configuração de caching diretamente aos arquivos do harness (`.claude/agents/`, `AGENTS.md`, etc.)
**QUANDO:** esse mecanismo tenta aplicar a correção sem revisão humana explícita e homologação
**ENTÃO:** sistema DEVE rejeitar a aplicação automática — a correção só pode ser proposta como [PROPOSTA], nunca aplicada por um agente/skill autônoma
**PORQUE:** RULE-C46-005; ENF-03 (Detector ≠ Gate; LLM não é seu próprio gate); INV-09 (sem baseline informal)
**VERIFICAÇÃO:** nenhuma alteração de arquivo de configuração do harness ocorre sem homologação registrada (DHR)

---

## I/O Schema — `freshness_record`

```json
{
  "path": "ROADMAP.md",
  "hash_algorithm": "SHA-256",
  "hash_value": "string hex, 64 caracteres",
  "read_at": "2026-09-28T00:00:00Z",
  "source_commit": "string hash de commit git, opcional (quando disponível)",
  "status": "REGISTRADO | FRESH | STALE | UNVERIFIABLE",
  "last_verified_at": "timestamp da última verificação (BASpec-C46-002), opcional"
}
```

---

## Enforcement Contracts

### EC-SPEC046-01 — Precondição de Freshness para Reutilização de Conteúdo de Arquivo-Fonte

*(Já homologado em substância na abertura — DHR-SPEC046-001 §2.2; formalizado aqui nos 8 campos completos do atomic-spec §10.3, sem alteração de conteúdo normativo.)*

```
CAPABILITY   : Reutilizar (sem reler do disco) o conteúdo de um documento-fonte do repositório
               (ROADMAP.md, atomic-spec.md, governance/RULES.md, governance/CATALOGO-OFICIAL.md,
               backlog/RMR-001_Painel_Backlog.md, governance/CONSTITUTION.md,
               governance/CONFLICT-MAP.md, GLOSSARIO.md, AGENTS.md) já lido anteriormente na
               mesma sessão/turno, para fundamentar uma afirmação [FONTE] na Spec/parecer em
               produção
EFFECT       : Uma afirmação classificada [FONTE] na entrega do Especificador (ou uma verificação
               do Revisor) é fundamentada em conteúdo que pode não ser mais idêntico ao estado
               atual do arquivo no repositório
PRECOND      : (hash de conteúdo do arquivo-fonte no momento do uso == hash de conteúdo
               registrado no momento da leitura que originou a cópia em contexto) — hash
               recomendado: SHA-256. ALTERNATIVA aceitável quando hash não estiver disponível
               operacionalmente: mtime do arquivo/commit git não avançou desde a leitura
               registrada. Fail-closed: se nenhum dos dois mecanismos estiver disponível, a
               reutilização é DESAUTORIZADA — o agente DEVE reler o arquivo antes de fundamentar
               a afirmação
POSTCOND     : Ou (a) a afirmação [FONTE] é fundamentada em conteúdo comprovadamente idêntico ao
               estado atual (hash/mtime confirmados — BASpec-C46-002), ou (b) o agente relê o
               arquivo e atualiza sua cópia em contexto antes de prosseguir, ou (c) a afirmação é
               rebaixada para [INFERÊNCIA]/[DECISÃO NECESSÁRIA] com nota explícita de fonte não
               revalidada (BASpec-C46-003)
POLICY       : INV-09 (sem baseline informal); TRACE-06 (etiquetagem de origem); CONS-01 (nenhuma
               decisão aberta tratada como fechada por conteúdo desatualizado); RULE-C46-001..004
LEVEL        : E2 (Operacional) — não E3, porque o efeito de uma afirmação [FONTE] desatualizada
               em spec-time é corrigível no próprio gate (Revisor audita, Andraus homologa ou
               não) antes de qualquer commit irreversível; distinto do Grupo A, onde um cache HIT
               de hipótese stale poderia sustentar diretamente um sinal operacional (lá, E3 —
               ACHADO-M2 crítico naquele escopo, não neste)
FAILURE-MODE : Fail-closed dentro do E2 declarado: precondição não verificável → reler do disco
               (nunca presumir freshness); se releitura não for possível, afirmação DEVE ser
               marcada [DECISÃO NECESSÁRIA] ou [INFERÊNCIA] com ressalva — nunca [FONTE] sem
               verificação (BASpec-C46-003)
EVIDENCE     : Registro do hash (ou mtime/commit) da leitura original + hash (ou mtime/commit) no
               momento do uso, disponível para auditoria do Revisor (Detector candidato:
               `scripts/check_doc_sync.py` estendido, ou script novo dedicado — [PROPOSTA], não
               fechada nesta Spec; decisão técnica de BUILD)
```

**Mínimos por nível (E2):** PRECOND + POSTCOND + FAILURE-MODE presentes — ✔ acima.

### EC-SPEC046-02 — Auditoria de Higiene de Sessão (complementar, F.3)

```
CAPABILITY   : Verificar (checklist determinístico) a ordenação e estrutura de um prompt/contexto
               de sessão do Especificador/Revisor
EFFECT       : Relatório de conformidade com as 6 regras adaptadas (SRC-02) — não altera nada,
               apenas informa
PRECOND      : N/A (E1 — contratual, não operacional)
POSTCOND     : N/A (E1)
POLICY       : SRC-01; SRC-02 (adaptados, [EXTERNO])
LEVEL        : E1 (Contratual) — F.3 Feedback, não Enforcement de efeito crítico
FAILURE-MODE : N/A (E1 não exige FAILURE-MODE pleno — mínimo é CAPABILITY+EFFECT+LEVEL+EVIDENCE)
EVIDENCE     : Relatório de checklist (6 itens, adaptados de SRC-02) anexado à sessão, quando
               aplicável
```

**Mínimos por nível (E1):** CAPABILITY + EFFECT + LEVEL + EVIDENCE — ✔ acima (PRECOND/POSTCOND/FAILURE-MODE declarados N/A, coerente com o mínimo E1 do atomic-spec §10.3).

---

# EXTENSÃO v1.1 — Caching Inter-Sessão (EC-SPEC046-03 + BASpecs CISS-001..004)

> **Natureza desta seção.** Bloco **aditivo** a v1.0 (baseline DHR-SPEC046-002). Formaliza a extensão recomendada e confirmada por Andraus (`backlog/BL-025-CACHE-ISS-001-analise.md`, Opção A). **Não altera nem substitui** o escopo, fronteira, Classe predominante (H) ou o EC-SPEC046-01 de v1.0 — é a **dimensão de persistência inter-sessão** do mesmo problema-classe (staleness de documento-fonte spec-time), não uma reescrita (INV-07). [FONTE: BL-025-CACHE-ISS-001-analise.md §4, Opção A] [PROPOSTA — aguarda Revisor + Andraus]

## v1.1 · D0 — Delta de missão (inter-sessão)

Onde v1.0/EC-SPEC046-01 impede que uma afirmação `[FONTE]` se apoie em conteúdo desatualizado **dentro da mesma sessão**, o EC-SPEC046-03 estende a mesma disciplina ao **eixo inter-sessão**: a cada nova sessão, Especificador/Revisor releem do zero o núcleo (`ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `backlog/RMR-001_Painel_Backlog.md`) mesmo quando nada mudou. O EC-SPEC046-03 especifica um **manifesto persistente de hashes** que autoriza **pular com segurança** a releitura integral de arquivos cujo hash ainda bate — **sempre fail-closed** (manifesto ausente/corrompido ⇒ releitura integral obrigatória). [FONTE: BL-025-CACHE-ISS-001-analise.md §1]

**Ressalva de honestidade (RULE-MET-01):** ver **L-ISS-01** (D1) — o manifesto é um *freshness guard*, não recoloca conteúdo em contexto; a economia de tokens é condicionada a um substrato de reuso cross-sessão externo e **não** é prometida pelo EC-SPEC046-03 isolado.

## v1.1 · Enforcement Contract — EC-SPEC046-03 (Persistência Inter-Sessão do Freshness Guard)

*Aditivo a EC-SPEC046-01 (não o contradiz). EC-SPEC046-01 governa a reutilização **intra-sessão** de conteúdo já em contexto; EC-SPEC046-03 governa a decisão de **pular a releitura inicial** com base em um manifesto **persistido entre sessões**. Um freshness_record intra-sessão não sobrevive à sessão; um manifesto persistente sobrevive — vetor de risco distinto (justifica reavaliação de nível abaixo).*

```
CAPABILITY   : Pular (skip) a releitura integral de um documento-fonte do núcleo no INÍCIO de uma
               nova sessão do Especificador/Revisor, com base num manifesto persistente de hashes
               SHA-256 gerado ao término de sessão anterior, quando o hash atual do arquivo ainda
               corresponde ao hash registrado no manifesto
EFFECT       : O agente pode operar uma sessão inteira SEM reler um documento-núcleo — se o
               manifesto (indevidamente) reportar FRESH para um arquivo que de fato mudou, o agente
               fundamentaria toda a sessão em baseline não-verificado (ex.: tratar decisão aberta
               do ROADMAP como fechada — violação CONS-01 — ou [FONTE] sobre RULES.md stale)
PRECOND      : (a) manifesto existe, é íntegro (parseável) e foi gerado por CÓDIGO determinístico
               (script/hook — NUNCA escrito pelo agente, ENF-03); E (b) SHA-256 recomputado do
               arquivo no início da sessão == hash registrado no manifesto (estado FRESH). Fail-closed:
               se (a) OU (b) falhar (ausente/corrompido/divergente/não-computável), o skip é
               DESAUTORIZADO e a releitura integral do arquivo é obrigatória
POSTCOND     : Ou (a) o skip é autorizado APENAS para arquivos comprovadamente idênticos (FRESH por
               código — CISS-002), e o núcleo efetivamente carregado é idêntico ao estado atual do
               repositório; ou (b) qualquer arquivo STALE/ABSENT/CORROMPIDO é relido integralmente
               antes de qualquer uso (CISS-003, fail-closed); em nenhum caminho um documento stale
               fundamenta afirmação/decisão da sessão
POLICY       : ENF-03 (Detector ≠ Gate; LLM não certifica o próprio manifesto — CISS-004);
               ENF-04 (fail-closed); INV-09 (manifesto = infraestrutura não-normativa, nunca
               baseline); CONS-01 (baseline stale não pode fechar decisão aberta); TRACE-06;
               RULE-C46-001..004 (herdadas, eixo intra-sessão)
LEVEL        : E3 (Crítico) — REAVALIADO, NÃO herdado de EC-SPEC046-01 (E2). Justificativa da
               elevação: em EC-SPEC046-01 (intra-sessão) a falha é auto-limitada porque o arquivo
               É lido em algum momento da mesma sessão — a leitura serve de backstop. EC-SPEC046-03
               REMOVE esse backstop: um manifesto falso-FRESH faz o agente NUNCA reler o arquivo na
               sessão inteira, de modo que a falha NÃO é auto-corrigível dentro da sessão e um
               artefato adulterado SOBREVIVE entre sessões (persistência = superfície de ataque
               durável). Criticidade epistêmica alta + falha não auto-corrigível ⇒ E3.
               (Nota de fronteira: o efeito permanece corrigível no gate humano — Revisor/Andraus —
               antes de qualquer commit de baseline; por isso E3 exige fail-closed obrigatório, mas
               não há irreversibilidade de execução — o SOT não executa. A elevação a E3 é pela
               remoção do backstop + persistência, não por irreversibilidade de mercado.)
FAILURE-MODE : Fail-closed OBRIGATÓRIO (E3): manifesto ausente/corrompido/hash divergente/
               não-computável/leitura parcial ⇒ skip DESAUTORIZADO ⇒ releitura integral do núcleo
               (CISS-003). Nunca presumir FRESH por omissão. O agente jamais escreve/valida o
               próprio manifesto (CISS-004).
               MÉTODO DE FALSO-DENY (ENF-07, exigido em E3): um falso-DENY (manifesto marca STALE
               um arquivo que na verdade não mudou) NÃO é perigoso — degrada apenas para releitura
               integral (o comportamento seguro/baseline). Custo do falso-DENY = reler o núcleo
               (~10⁴–10⁵ tokens) — aceitável e auditável (evento MISS registrado); nunca produz
               conteúdo stale. Assim o desenho é assimétrico por construção: falso-DENY é barato e
               seguro, falso-ALLOW é impedido pela precondição de hash por código.
EVIDENCE     : Manifesto JSON versionado em diretório de saída gerada NÃO-NORMATIVA (D4-ISS:
               `docs/cache/`, análogo a `docs/mapa/`) + log por arquivo do veredito
               FRESH/STALE/ABSENT/CORROMPIDO produzido por CÓDIGO no início da sessão, auditável
               pelo Revisor. Detector candidato: reuso/extensão do hashing de `scripts/build_map.py`
               (§D4-ISS) — [PROPOSTA], decisão de BUILD.
```

**Mínimos por nível (E3):** CAPABILITY + EFFECT + PRECOND + POSTCOND + POLICY + FAILURE-MODE + método de falso-DENY (ENF-07) + EVIDENCE — ✔ todos presentes acima.

## v1.1 · D3 — BASpecs CISS-001..004 (Classe declarada — RULE-MECH-01, CC-11)

> **Decisão definitiva sobre fundir CISS-003/004 (a análise deixou em aberto):** **MANTIDAS SEPARADAS (4 BASpecs, D/H/C/C).** Justificativa (RULE-MECH-02, não presunção): CISS-003 e CISS-004 constituem invariantes **distintos** — CISS-003 = *default* fail-closed (qual é o comportamento seguro quando o manifesto não é confiável, ENF-04); CISS-004 = *autoridade* (quem tem o direito de escrever/validar o manifesto, ENF-03). Fundi-los tornaria a auditoria do Revisor incapaz de verificar ENF-03 e ENF-04 **independentemente** — uma falha de autoridade (agente escreveu o manifesto) e uma falha de default (manifesto ausente tratado como FRESH) têm causas e correções diferentes. A superfície extra de um 4º BASpec Classe C é proporcional porque ambos são risco real (não risco baixo — RULE-MECH-02/C4 não é violada). Alternativa de fusão registrada e **descartada**.

### BASpec-CISS-001 — Persistência do manifesto ao término da sessão
```
CLASSE        : D (Determinístico)
MECANISMO     : script/hook computa SHA-256 por arquivo-núcleo e grava o manifesto JSON — código
                puro, sem julgamento do LLM (reusa o hashing de build_map.py:81, §D4-ISS)
CRITÉRIO 4Es  : Economicidade — habilita a economia de releitura inter-sessão; a garantia de
                identidade (Eficácia) é do próprio hash SHA-256, provida por CISS-002/003

BASpec-CISS-001:
  QUANDO:       a sessão do Especificador/Revisor encerra (hook Stop/SubagentStop)
  ENTÃO:        código grava/atualiza o manifesto = { schema_version, generated_at, generated_by:
                "code", por_arquivo: [{path, sha256, read_at, source_commit?}] } em diretório de
                saída gerada NÃO-NORMATIVA (`docs/cache/`, §D4-ISS) — nunca em governance/ nem canon/
  PORQUE:       sem manifesto persistente não há base de comparação inter-sessão; INV-09 (manifesto
                é infraestrutura regenerável, nunca baseline); fundamenta a otimização
  REFERÊNCIA:   EC-SPEC046-03; INV-09; BL-019/build_map.py (precedente de manifesto não-normativo)
  VERIFICADO POR:
    DADO        sessão do Especificador que leu ROADMAP.md e RULES.md encerra em Tn
    QUANDO      o hook Stop/SubagentStop dispara
    ENTÃO       manifesto em docs/cache/ contém {path, sha256, read_at} por arquivo-núcleo
    VERIFICAÇÃO manifesto.por_arquivo[i].sha256 == sha256(conteúdo real do arquivo i em Tn); campo
                generated_by == "code" (nunca "agent")
```

### BASpec-CISS-002 — Validação no início da sessão + skip condicional
```
CLASSE        : H (Híbrido)
MECANISMO     : comparação de hash é determinística (código); a reação (pular releitura vs. reler)
                é decisão do agente com GATE DE SAÍDA determinístico por código — idêntico ao padrão
                de BASpec-C46-002 (v1.0)
CRITÉRIO 4Es  : Eficiência — reduz releitura redundante sem sacrificar a garantia de identidade
                (Eficácia preservada pelo hash; Economicidade não sobe acima de Eficácia)
BOUNDED LOOP  : no máximo 1 releitura por arquivo STALE/ABSENT por início de sessão — sem retry
                infinito (RULE-MECH-03)
GATE DE SAÍDA : recomputação de SHA-256 atual vs. manifesto, por CÓDIGO (ENF-03) — não autoavaliação
                do LLM; o agente lê o veredito FRESH/STALE/ABSENT, não computa o hash

BASpec-CISS-002:
  QUANDO:       a sessão inicia (hook SessionStart) e há manifesto válido (CISS-003 não disparou)
  ENTÃO:        para cada arquivo-núcleo, código classifica FRESH (hash bate) / STALE (diverge) /
                ABSENT (sem entrada). FRESH ⇒ a releitura integral PODE ser pulada com segurança;
                STALE/ABSENT ⇒ releitura integral obrigatória (bounded loop, 1 releitura)
  PORQUE:       EC-SPEC046-03 estende EC-SPEC046-01 ao eixo inter-sessão; nenhuma [FONTE]/decisão
                da sessão pode se apoiar em conteúdo não-verificado
  REFERÊNCIA:   EC-SPEC046-03; RULE-C46-002 (análogo intra-sessão); INV-09
  VERIFICADO POR:
    DADO        manifesto com sha256(governance/RULES.md)=H1; o arquivo foi alterado entre sessões
                (H2 != H1)
    QUANDO      nova sessão inicia e o código recomputa o hash de RULES.md
    ENTÃO       veredito = STALE ⇒ skip DESAUTORIZADO ⇒ RULES.md é relido integralmente antes de uso
    VERIFICAÇÃO nenhum arquivo classificado STALE/ABSENT é usado como [FONTE] sem releitura; evento
                registrado como MISS
```

### BASpec-CISS-003 — Invariante fail-closed (manifesto ausente/corrompido/não-verificável)
```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement — a validade do manifesto É o gate que constitui se o skip de CISS-002
                é sequer permitido; a saída é permit/deny, não uma tarefa (mínimo de Classe C =
                GATE DE SAÍDA, atomic-spec §10.6)
CRITÉRIO 4Es  : Conformidade/Eficácia — nunca pular releitura sobre baseline não-verificado, mesmo
                que custe reler todo o núcleo (Economicidade não rebaixa — AGENTS.md §6 item 11)
GATE DE SAÍDA : o próprio invariante é o gate (Classe C) — manifesto ausente OU corrompido OU hash
                não-computável (I/O, leitura parcial) ⇒ DENY do skip

BASpec-CISS-003:
  QUANDO:       início de sessão e o manifesto está ausente, corrompido (não-parseável), ou o hash
                de algum arquivo não pode ser computado (erro de I/O, leitura parcial/truncada)
  ENTÃO:        o skip de releitura é DESAUTORIZADO para o(s) arquivo(s) afetado(s) — releitura
                integral obrigatória (fail-closed, ENF-04). Nunca presumir FRESH por omissão. Se o
                manifesto inteiro está ausente/corrompido ⇒ releitura integral de TODO o núcleo
  PORQUE:       ENF-04 (fail-closed); INV-09; CONS-01 (um baseline stale poderia tratar decisão
                aberta como fechada); fundamenta o default seguro
  REFERÊNCIA:   EC-SPEC046-03 FAILURE-MODE; ENF-04; INV-09; CONS-01
  VERIFICADO POR:
    DADO        docs/cache/session-freshness-manifest.json ausente (primeira sessão) OU com JSON
                truncado/corrompido
    QUANDO      nova sessão inicia e o código tenta validar o manifesto
    ENTÃO       veredito global = DENY ⇒ releitura integral do núcleo; nenhum skip autorizado
    VERIFICAÇÃO nenhum arquivo-núcleo é pulado quando o manifesto não é íntegro e verificável por
                código; ausência de manifesto nunca resulta em skip
```
**Justificativa da Classe C (RULE-MECH-02 — não presunção):** CISS-003 não *executa uma tarefa*; **constitui a precondição** sob a qual o skip de CISS-002 é permitido — sua saída é permit/deny e ela É o gate. Risco NÃO é baixo: pular releitura sobre `ROADMAP.md`/`RULES.md` stale sustentaria `[FONTE]` desatualizada ou fecharia decisão aberta (violação CONS-01) — logo Classe C não viola Economicidade (RULE-MECH-02/C4 só proíbe Classe C em risco baixo). Alternativa descartada: modelar apenas como FAILURE-MODE de CISS-002 (H) — um invariante fail-closed nomeado e auditável por ENF-04 é mais forte que um ramo de falha embutido.

### BASpec-CISS-004 — Separação de autoridade ENF-03 (o agente não certifica a si mesmo)
```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement de autoridade — geração e validação do manifesto são de CÓDIGO
                determinístico (script/hook); o agente consome o veredito, nunca escreve/valida o
                próprio hash; a saída é permit/deny sobre "quem computou"
CRITÉRIO 4Es  : Eficácia — a garantia de integridade colapsa se o LLM puder autocertificar freshness
GATE DE SAÍDA : a verificação por código é o gate; qualquer caminho que escreva/valide o manifesto
                por via não-determinística (o agente afirmando "está fresco") é rejeitado

BASpec-CISS-004:
  QUANDO:       qualquer caminho tenta escrever ou validar o manifesto sem passar pelo script/hook
                determinístico (ex.: o agente propõe gravar/certificar o manifesto ele mesmo)
  ENTÃO:        a operação é REJEITADA — o manifesto só é escrito/validado por código (§D4-ISS);
                aplicação automática de correção de configuração de caching exige homologação
                (mesmo princípio de RULE-C46-005/v1.0)
  PORQUE:       ENF-03 (Detector ≠ Gate; LLM não é seu próprio gate); INV-09
  REFERÊNCIA:   ENF-03; INV-09; RULE-C46-005 (v1.0, análogo)
  VERIFICADO POR:
    DADO        o agente (LLM) tenta gravar docs/cache/session-freshness-manifest.json diretamente
                ou afirmar "manifesto válido" sem execução de código
    QUANDO      essa via não-determinística é tentada
    ENTÃO       a operação é rejeitada; campo generated_by só aceita "code"; validação só conta se
                produzida por script/hook
    VERIFICAÇÃO nenhum manifesto com generated_by != "code" é aceito; nenhum skip é autorizado por
                autoafirmação do agente
```
**Nota de economicidade (RULE-MECH-02):** dois BASpecs Classe C (003/004) tratam invariantes distintos e ambos de risco real — 003 = default fail-closed (ENF-04); 004 = autoridade de quem computa (ENF-03). Mantidos separados para auditoria independente de ENF-03 e ENF-04 (ver decisão definitiva acima). Nenhum Classe C sobre risco baixo.

## v1.1 · D4-ISS — Algoritmo (reuso da infraestrutura homologada de `build_map.py`)

> **Achado reaproveitável (evidência, não proposta de hashing novo):** `scripts/build_map.py` **já** computa SHA-256 por arquivo do conteúdo dos documentos e um digest combinado, persistido em `docs/mapa/mapa-projeto.json`, com `--check` comparando digests e retornando exit 1 em defasagem — verificado nesta redação em `build_map.py:81` (`hashlib.sha256(text[p].encode('utf-8')).hexdigest()` por arquivo) e `build_map.py:341-342` (comparação de digest em `--check`). O EC-SPEC046-03 **reusa** esse mecanismo em vez de introduzir hashing novo. [FONTE: build_map.py:81, 341-342; BL-025-CACHE-ISS-001-analise.md §2.a] [FATO ARQUITETURAL — BL-019]

```
ALGORITMO: validate_session_manifest  (executado por CÓDIGO — hook SessionStart / script)
ENTRADA:  manifest_path (docs/cache/session-freshness-manifest.json) · lista de arquivos-núcleo
PROCESSO:
  1. SE manifest_path ausente OU não-parseável (corrompido) OU generated_by != "code":
       retornar DENY_GLOBAL  → releitura integral de TODO o núcleo (CISS-003/CISS-004, fail-closed)
  2. PARA cada arquivo-núcleo f:
       a. tentar ler conteúdo de f
          SE erro de I/O ou leitura parcial → veredito[f] = CORROMPIDO/UNVERIFIABLE (fail-closed)
       b. hash_atual = SHA-256(conteúdo de f)          # reusa build_map.py:81
       c. SE f não tem entrada no manifesto            → veredito[f] = ABSENT
          SENÃO SE hash_atual == manifesto[f].sha256   → veredito[f] = FRESH
          SENÃO                                        → veredito[f] = STALE
  3. skip_autorizado = { f : veredito[f] == FRESH }
     releitura_obrigatoria = { f : veredito[f] ∈ {STALE, ABSENT, CORROMPIDO} }
SAÍDA:    por arquivo, veredito ∈ {FRESH, STALE, ABSENT, CORROMPIDO}; o agente consome o veredito,
          NÃO computa o hash (ENF-03 / CISS-004)

LOCAL DO MANIFESTO: docs/cache/session-freshness-manifest.json
  - Escolhido por ANALOGIA a docs/mapa/ (BL-019): território de saída GERADA, NÃO-NORMATIVA,
    regenerável, nunca editada à mão. NÃO em governance/cache/ nem canon/ — para não arriscar
    virar baseline por acidente (INV-09). [FONTE: BL-025-CACHE-ISS-001-analise.md §2.a, Opção O3]
GERAÇÃO: hook Stop/SubagentStop (grava/atualiza, CISS-001) — mesma garantia em camadas do BL-019.
VEÍCULO TÉCNICO DEFINITIVO (script novo dedicado vs. extensão de build_map.py): [PROPOSTA] — decisão
  de BUILD, não fechada nesta emenda.
```

## v1.1 · D5-ISS — Estados do manifesto (extensão da máquina de v1.0)

Compatível com a máquina de v1.0 (FRESH/STALE/UNVERIFIABLE do freshness_record intra-sessão); adiciona os estados de **um manifesto persistente** e cobre ausência/corrupção e o gate ENF-03:

```
Manifesto: AUSENTE            → (início de sessão, CISS-003) → DENY_GLOBAL → releitura integral do
                                núcleo → (hook Stop grava, CISS-001) → PRESENTE
Manifesto: PRESENTE + íntegro + generated_by=="code" → (CISS-002) → validação por arquivo
Manifesto: PRESENTE mas CORROMPIDO (não-parseável)   → (CISS-003) → DENY_GLOBAL → releitura integral
Manifesto: PRESENTE mas generated_by!="code"         → (CISS-004) → REJEITADO → releitura integral
Por arquivo (dentro de manifesto íntegro):
  entrada FRESH  (hash bate)          → skip da releitura AUTORIZADO
  entrada STALE  (hash diverge)       → skip NEGADO → releitura integral (bounded loop, 1x) → nova
                                        entrada FRESH ao término (CISS-001)
  entrada ABSENT (sem registro)       → skip NEGADO → releitura integral → nova entrada (CISS-001)
  entrada CORROMPIDO/UNVERIFIABLE     → skip NEGADO → releitura integral (fail-closed)
```

Nenhuma transição permite ir de AUSENTE/CORROMPIDO/STALE/ABSENT diretamente para "skip autorizado" sem releitura integral bem-sucedida (fail-closed). O manifesto nunca é escrito/validado pelo agente — só por código (CISS-004). Estados não regridem silenciosamente: um veredito STALE só vira FRESH após releitura + regravação por código (INV-09/TRACE-06).

## v1.1 · D7-ISS — Cenários de teste (≥3)

### Cenário-CISS-T01 — Skip autorizado (FRESH inter-sessão)
```
DADO        manifesto com sha256(ROADMAP.md)=H1; ROADMAP.md não mudou entre a sessão S1 e S2
QUANDO      S2 inicia e o código (hook SessionStart) recomputa o hash de ROADMAP.md = H1
ENTÃO       veredito = FRESH → releitura integral de ROADMAP.md pode ser pulada com segurança
VERIFICAÇÃO o núcleo efetivamente confiado é idêntico ao estado atual do repo; veredito produzido
            por código, não por autoafirmação do agente
```

### Cenário-CISS-T02 — Skip negado (STALE inter-sessão) → releitura
```
DADO        manifesto com sha256(governance/RULES.md)=H1; entre S1 e S2 Andraus insere uma RULE nova
            (H2 != H1)
QUANDO      S2 inicia e o código recomputa o hash de RULES.md = H2
ENTÃO       veredito = STALE → skip NEGADO → RULES.md é relido integralmente antes de qualquer uso
VERIFICAÇÃO nenhuma [FONTE]/decisão de S2 se apoia na versão H1; evento MISS registrado
```

### Cenário-CISS-T03 — Manifesto ausente/corrompido → fail-closed global
```
DADO        docs/cache/session-freshness-manifest.json ausente (1ª sessão) OU com JSON truncado
QUANDO      nova sessão inicia e o código tenta validar
ENTÃO       DENY_GLOBAL → releitura integral de todo o núcleo; nenhum skip autorizado (CISS-003)
VERIFICAÇÃO ausência/corrupção de manifesto nunca resulta em skip; releitura integral confirmada
```

## v1.1 · D8-ISS — Adversarial (risco novo desta emenda)

### ADV-CISS-01 — Manifesto ADULTERADO entre sessões (falso-FRESH)
```
DADO        um manifesto persistente é editado (por acidente, hook defeituoso, ou adulteração) para
            registrar, para governance/RULES.md, o hash de uma versão ANTIGA — enquanto o arquivo
            real no repo já mudou; a intenção (ou o efeito) é fazer o agente PULAR a releitura e
            operar sobre RULES.md stale a sessão inteira
QUANDO      nova sessão inicia e o agente tenta pular a releitura confiando no manifesto
ENTÃO       o sistema DEVE recomputar o SHA-256 REAL do arquivo por CÓDIGO (não confiar no valor
            gravado no manifesto como se fosse o conteúdo): hash_real != hash_gravado ⇒ veredito
            STALE ⇒ skip NEGADO ⇒ releitura integral. Um manifesto que afirma FRESH mas cujo hash
            gravado não corresponde ao SHA-256 recomputado do arquivo NUNCA autoriza o skip
PORQUE      EC-SPEC046-03 PRECOND (b) exige recomputação por código do hash ATUAL do arquivo, não
            leitura passiva do campo do manifesto; ENF-03 (o manifesto é dado, não gate); a
            elevação a E3 existe exatamente por este vetor (persistência = superfície durável)
VERIFICAÇÃO nenhum skip é autorizado com base apenas no valor gravado no manifesto; o skip só ocorre
            se SHA-256(conteúdo_atual_do_arquivo) == valor gravado E generated_by=="code". Um agente
            que tente pular a releitura sem o veredito FRESH produzido por código é bloqueado (CISS-004)
```

> **Observação de robustez (por que ADV-CISS-01 é contido):** o manifesto guarda um hash, mas a
> autorização de skip depende de **recomputar** o SHA-256 do arquivo real e compará-lo — não de
> confiar no campo. Adulterar o campo para "FRESH" sem que o arquivo real corresponda apenas produz
> um mismatch ⇒ STALE ⇒ releitura (o comportamento seguro). Para forçar um falso-ALLOW o atacante
> precisaria alterar o arquivo-fonte real para colidir em SHA-256 com o hash gravado — inviável
> (resistência a colisão). O único falso-positivo residual é o mesmo de v1.0 (arquivo alterado e
> revertido ao conteúdo idêntico — L-ISS-01/§7-bis Bloco A), aceito e declarado.

---

## Campos SES-001 (§8.1) — Engineering Card

**N/A nesta entrega** (CC-06/CC-07) — artefato é Spec/Plan, não Engineering Card. Os 17 campos tornam-se obrigatórios quando as Tasks/Engineering Cards desta Spec forem produzidas (BUILD adiado — atomic-spec §14). Mesmo tratamento de SPEC-019/020/021.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| Abertura homologada (número/nome/fronteira/Classe H/EC-SPEC046-01 em substância) | [FONTE] | FATO NORMATIVO (DHR-SPEC046-001) |
| Mecanismo nativo de prompt caching Anthropic (hash cumulativo de prefixo) | [FONTE] | FATO NORMATIVO (documentação oficial do provedor, SRC-06) |
| 4 BASpecs, D4 algoritmo, D5 estados, D7/D8 cenários (este Plan) | [PROPOSTA] | Requer parecer do Revisor + homologação de Andraus |
| (v1.1) EC-SPEC046-03 (E3), BASpecs CISS-001..004, D4-ISS/D5-ISS/D7-ISS/D8-ISS, manifesto docs/cache/ | [PROPOSTA] | Emenda candidata — requer parecer do Revisor + homologação de Andraus |
| (v1.1) Reuso do hashing SHA-256 + manifesto não-normativo de `build_map.py` (build_map.py:81,341-342) | [FONTE] | FATO ARQUITETURAL (BL-019) — infraestrutura já homologada, reaproveitada |
| (v1.1) L-ISS-01 — economia de tokens condicionada a substrato de reuso cross-sessão | [PROPOSTA]/[ESTIMATIVA] | Limitação declarada (RULE-MET-01), não promessa da capacidade |
| Veículo técnico de implementação (script novo vs. `check_doc_sync.py` estendido) | [PROPOSTA] | Não fechado — decisão de BUILD |
| RULE-C46-001..005 | [PROPOSTA] | Novas nesta Spec — não fechadas até homologação |
| SRC-01..07 (Dossiê) | [EXTERNO] | Não-baseline; comparadas e classificadas (adotar/adaptar/rejeitar/adiar) |
| Grupo A / ACHADO-M2 | [DECISÃO NECESSÁRIA] | Fora de escopo — fica para SPEC-047 futura |

---

## Decisões abertas incidentes

| ID | Descrição | Status | Impacto nesta Spec |
|---|---|---|---|
| **ECC-VAL-001** | Validade/prazo do Dossiê de Pesquisa | EM ABERTO | Este Plan foi produzido no mesmo dia da homologação da abertura (2026-09-28) — dentro de qualquer janela razoável, mas a regra geral segue aberta |
| **Grupo A (futura SPEC-047)** | Caching de evidências/hipóteses (CHM-001/CEM-001) | Explicitamente diferido (não é decisão aberta no sentido de bloqueio — é faseamento deliberado) | Nenhum — non-goal declarado |
| **Veículo técnico de implementação** | script novo vs. `scripts/check_doc_sync.py` estendido | [DECISÃO NECESSÁRIA] — não resolvida neste Plan | Não bloqueia o comportamento especificado (EC-SPEC046-01/BASpecs); é decisão de BUILD |

Nenhuma decisão aberta tratada como invariante fechado (CONS-01).

---

**Pronto para revisão.**
