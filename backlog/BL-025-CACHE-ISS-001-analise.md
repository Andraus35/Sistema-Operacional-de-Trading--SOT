# BL-025 — CACHE-ISS-001 — Análise Técnica Preparatória

> **NATUREZA DESTE DOCUMENTO (rótulo obrigatório).** Isto é uma **análise técnica preparatória**
> (RMR-001 §5, "Ação ao ativar" do BL-025), **NÃO** um Dossiê de Pesquisa formal (RULE-ECC-02) e
> **NÃO** uma abertura de Spec. Não há número de Spec definitivo aqui, não há `plan.md`/`checks.md`,
> nada é homologável por este documento. Seu único propósito é alimentar uma decisão futura de
> Andraus sobre **se/como** abrir uma Spec (extensão de SPEC-046 via `EC-SPEC046-03`, ou Spec
> autônoma nova). Toda BASpec, esquema e recomendação abaixo é **[PROPOSTA]**.

| Campo | Valor |
|---|---|
| ID | BL-025 — CACHE-ISS-001 |
| Título | Caching Inter-Sessão de Documentos-Fonte com Freshness Guard |
| Tipo | Módulo diferido (análise preparatória) |
| Status | **PROPOSTA** (intake analisado; aguarda decisão de Andraus) |
| Autor | Especificador Principal SOT |
| Data | 2026-09-28 |
| Dependências | SPEC-046 v1.0 (BASELINE, DHR-SPEC046-002 — reusa schema `freshness_record`, EC-SPEC046-01) · CLASSE-MECH-001 (RULE-MECH-01..04, D/H/P/C) · ENF-03 · INV-09 · CONS-01 |
| Agentes afetados | **Exclusivamente Especificador e Revisor (Grupo B)** — confirmado em `AGENTS.md` §3 (só há dois agentes; ambos spec-time) e em SPEC-046 (Grupo B). Grupo A (agentes cognitivos) permanece fora — candidato SPEC-047, não tocado aqui. |

---

## 1. Descrição do problema

**SPEC-046 resolve staleness INTRA-sessão:** dentro de uma mesma sessão/turno, um documento-fonte
lido cedo pode ser reusado como `[FONTE]` só se o hash ainda bater (EC-SPEC046-01, `freshness_record`).

**CACHE-ISS-001 ataca staleness INTER-sessão:** a cada **nova** sessão, Especificador e Revisor
releem do zero `ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`,
`backlog/RMR-001_Painel_Backlog.md` etc. — mesmo quando esses arquivos **não mudaram** desde a
sessão anterior. A proposta: um **manifesto persistente** de hashes (extensão do `freshness_record`)
que, no início da sessão, permita **pular com segurança** a releitura de arquivos cujo hash ainda
bate — sempre **fail-closed** (manifesto ausente/corrompido ⇒ releitura integral obrigatória).

---

## 2. Análise de viabilidade técnica

### 2.a Onde armazenar o manifesto persistente?

Critério declarado (instrução do BL-025): **menor acoplamento com baseline normativo (INV-09)** — o
manifesto é infraestrutura regenerável, **não pode virar baseline por acidente**.

| Opção | Descrição | Acoplamento com baseline (INV-09) | Veredito |
|---|---|---|---|
| **O1 — JSON em `governance/cache/`** | Arquivo de hashes sob `governance/` | **RUIM** — vive dentro do diretório de **autoridade normativa** (`governance/` é F.1, AGENTS.md §2); risco alto de ser confundido com artefato baseline | **Rejeitada** |
| **O2 — Campo embutido no `freshness_record` (SPEC-046)** | Persistir o próprio `freshness_record` entre sessões | Baixo, mas **não resolve o problema**: `freshness_record` é estrutura **de sessão**; embuti-lo não cria a camada de persistência inter-sessão. Precisaria de um veículo de persistência de qualquer forma | **Insuficiente isolada** (é o *schema*, não o *lugar*) |
| **O3 (recomendada) — JSON dedicado em diretório de saída gerada não-normativa** (ex.: `docs/cache/session-freshness-manifest.json`, espelhando o precedente `docs/mapa/`) | Arquivo próprio, fora de `governance/`/`canon/`, em território já estabelecido como **NÃO-NORMATIVO e regenerável** (INV-09 declarado para `docs/mapa/`) | **Mínimo** — reusa exatamente a convenção já homologada do mapa (BL-019): saída gerada, nunca editada à mão, regenerável, com digest | **Recomendada** |

**Achado técnico reaproveitável (evidência, não inferência):** `scripts/build_map.py` **já computa
um SHA-256 por arquivo** do conteúdo dos documentos e um digest combinado, persistido em
`docs/mapa/mapa-projeto.json`, com `--check` comparando digests e retornando exit 1 em defasagem
(`build_map.py:81-82,158,341-342`). Ou seja, **o mecanismo de hash-por-arquivo + manifesto JSON
não-normativo + verificação determinística por `--check` já existe e é precedente homologado**
(BL-019, DHR-EUA-E22). CACHE-ISS-001 pode reusar essa infraestrutura em vez de criar hashing novo.

### 2.b Como o manifesto é escrito ao final da sessão? (restrição ENF-03)

ENF-03: o LLM **não é seu próprio gate** — o registro de freshness precisa de verificação
determinística por **código**, não da autoafirmação do agente de que sua leitura é confiável.

| Opção | ENF-03 | Veredito |
|---|---|---|
| **Manual (o agente escreve o manifesto)** | **VIOLA ENF-03** — o LLM certificaria a si mesmo | **Rejeitada** |
| **Hook (`Stop`/`SubagentStop`/`SessionStart`)** | Conforme — hook é código determinístico; mesmo padrão em camadas já usado por BL-019/BL-006 | **Recomendada (camada 1)** |
| **Script Python (`scripts/`), invocado por hook ou manualmente** | Conforme — hash computado por código; o agente lê o **veredito**, não escreve o hash | **Recomendada (camada 2, reusa `build_map.py`)** |

**Recomendação 2.b:** manifesto **gerado e validado por script determinístico** (reuso do hashing de
`build_map.py`), **acionado por hook** (`SessionStart` valida; `Stop`/`SubagentStop` regenera) — a
mesma garantia em camadas do BL-019. O agente **nunca** escreve o manifesto; consome o veredito
FRESH/STALE/ABSENT produzido pelo código. Isso satisfaz ENF-03 por construção.

### 2.c Custo do próprio mecanismo vs. economia de releitura

- **Custo do mecanismo** [ESTIMATIVA — base de cálculo declarada, não medição]: ler o manifesto +
  recomputar SHA-256 de ~8–10 documentos-núcleo (ordem de ~10²–10³ KB no total). SHA-256 é da ordem
  de microssegundos por KB em código → **custo de CPU ~10²–10³ ms, e ~0 tokens de LLM** (o hashing é
  feito por código, não pelo modelo). Base: contagem de documentos-núcleo do gate de entrada
  (`especificador.md` §4 passo 1) × tamanho típico observado (RMR-001 sozinho ≈ 25k tokens de leitura).
- **Custo de reler do zero** [ESTIMATIVA]: injetar o núcleo em contexto custa **ordem de 10⁴–10⁵
  tokens de LLM por sessão** (só o RMR-001 ≈ 25k; núcleo completo facilmente 40–80k).
- **Conclusão:** o mecanismo troca ~10²–10³ ms de CPU (≈0 tokens) por um veredito que **autoriza**
  não recarregar arquivos comprovadamente inalterados.

**RISCO/HONESTIDADE (RULE-MET-01 — não-fabricação):** um manifesto de hashes **por si só NÃO
recoloca conteúdo no contexto do LLM**. Numa sessão nova, o conteúdo não está em contexto; o
manifesto apenas informa *se é seguro confiar* em um substrato de reuso cross-sessão (ex.: o
prompt-cache do provedor com TTL longo, ou um snapshot armazenado). Portanto CACHE-ISS-001 é o
**freshness guard** desse reuso — **não** um mecanismo que, sozinho, elimina a leitura. Isso é
exatamente análogo a RULE-C46-004 da SPEC-046 (o guard é independente do cache nativo do provedor).
A economia real só se materializa **se existir** um substrato de reuso cross-sessão; sem ele, o
ganho é apenas evitar re-verificação semântica redundante, não a leitura. **Este ponto deve ser
tratado explicitamente na eventual Spec — não presumir economia de tokens que o manifesto sozinho
não entrega.**

---

## 3. BASpecs propostas (Classe sob RULE-MECH-01..04 — D/H/P/C)

> **Correção de nomenclatura aplicada:** o rascunho original usava "Classe D/H/E". **Não existe
> Classe E.** Taxonomia vigente (DHR-CLASSE-MECH-001, RULES.md:472-493; atomic-spec §10.6):
> **D** (Determinístico) · **H** (Híbrido) · **P** (Probabilístico c/ Gate) · **C** (Constitutivo).
> Cada BASpec abaixo reclassificada; o invariante fail-closed do rascunho (ex-"Classe E") é
> reclassificado como **Classe C**, justificado (não presumido) em CISS-003.

### BASpec-CISS-001 — Persistência do manifesto ao final da sessão
```
CLASSE       : D (Determinístico)
MECANISMO    : script/hook computa SHA-256 por arquivo-núcleo e grava o manifesto JSON — código
               puro, sem julgamento do LLM (reusa hashing de build_map.py)
CRITÉRIO 4Es : Economicidade — habilita a economia de releitura inter-sessão; a garantia de
               identidade (Eficácia) é do próprio hash, já provida por CISS-002/003
QUANDO       : a sessão do Especificador/Revisor encerra (hook Stop/SubagentStop)
ENTÃO        : código grava manifesto = { por arquivo: path, sha256, read_at, source_commit? },
               em diretório de saída gerada não-normativa (§2.a O3)
PORQUE       : sem manifesto persistente não há base de comparação inter-sessão — fundamenta a
               otimização; INV-09 (manifesto é infraestrutura, nunca baseline)
```

### BASpec-CISS-002 — Validação de freshness no início da sessão + skip condicional
```
CLASSE       : H (Híbrido)
MECANISMO    : comparação de hash é determinística (código); a reação (pular releitura vs. reler)
               é decisão do agente com GATE DE SAÍDA determinístico por código — por isso Híbrido
               (idêntico ao padrão de BASpec-C46-002 da SPEC-046)
CRITÉRIO 4Es : Eficiência — reduz releitura redundante sem sacrificar a garantia de identidade
BOUNDED LOOP : no máximo 1 releitura por arquivo STALE por início de sessão — sem retry infinito
               (RULE-MECH-03)
GATE DE SAÍDA: recomputação de SHA-256 atual vs. manifesto, por código (ENF-03) — não autoavaliação
QUANDO       : a sessão inicia (hook SessionStart) e há manifesto válido
ENTÃO        : para cada arquivo-núcleo, código classifica FRESH (hash bate) / STALE (diverge) /
               ABSENT (sem entrada). FRESH ⇒ releitura integral pode ser pulada com segurança;
               STALE/ABSENT ⇒ releitura obrigatória (bounded loop)
PORQUE       : EC-SPEC046-01 estendido ao eixo inter-sessão; nenhuma [FONTE] pode se apoiar em
               conteúdo não-verificado
```

### BASpec-CISS-003 — Invariante fail-closed (manifesto ausente/corrompido/não-verificável)
```
CLASSE       : C (Constitutivo)  [ex-"Classe E" do rascunho — reclassificado, justificado abaixo]
MECANISMO    : enforcement — a validade do manifesto É o gate que constitui se o skip de CISS-002
               é sequer permitido; sua saída é um permit/deny, não uma tarefa
CRITÉRIO 4Es : Conformidade/Eficácia — nunca pular releitura sobre baseline não-verificado, mesmo
               que custe reler tudo (Economicidade não rebaixa — AGENTS.md §6 item 11)
GATE DE SAÍDA: o próprio invariante é o gate (Classe C = é o gate) — manifesto ausente OU
               corrompido OU hash não-computável ⇒ DENY do skip
QUANDO       : início de sessão e o manifesto está ausente, corrompido, ou o hash não pode ser
               computado (erro de I/O, leitura parcial)
ENTÃO        : o skip de releitura é DESAUTORIZADO — releitura integral do núcleo é obrigatória
               (fail-closed, ENF-04). Nunca presumir FRESH por omissão
PORQUE       : ENF-04 (fail-closed); INV-09; CONS-01 (um baseline stale poderia tratar decisão
               aberta como fechada) — fundamenta o default seguro
```
**Justificativa da Classe C (não presunção — RULE-MECH-02):** CISS-003 não *executa uma tarefa*;
ela **constitui a precondição** sob a qual o skip de CISS-002 é permitido — sua saída é
permit/deny, e ela É o gate (mínimo de Classe C = GATE DE SAÍDA). O risco **não é baixo**: pular
releitura sobre um `ROADMAP.md`/`RULES.md` stale poderia sustentar uma afirmação `[FONTE]`
desatualizada ou tratar decisão aberta como fechada (violação CONS-01) — logo Classe C **não** viola
Economicidade (RULE-MECH-02/C4, que só proíbe Classe C em risco baixo). **Alternativa considerada e
descartada:** modelar isto apenas como FAILURE-MODE de CISS-002 (H) — descartada porque um invariante
fail-closed nomeado e auditável independentemente (ENF-04) é mais forte que um ramo de falha embutido.

### BASpec-CISS-004 — Separação de autoridade ENF-03 (o agente não certifica a si mesmo)
```
CLASSE       : C (Constitutivo)
MECANISMO    : enforcement de autoridade — geração e validação do manifesto é de código
               determinístico; o agente consome o veredito, nunca escreve/valida o próprio hash
CRITÉRIO 4Es : Eficácia — a garantia de integridade colapsa se o LLM puder autocertificar freshness
GATE DE SAÍDA: a verificação por código é o gate; qualquer proposta de aplicar/escrever manifesto
               por via não-determinística é rejeitada
QUANDO       : qualquer caminho tenta escrever ou validar o manifesto sem passar pelo script/hook
               determinístico
ENTÃO        : a operação é rejeitada — manifesto só é escrito/validado por código (§2.b);
               correção automática de configuração de caching exige homologação (padrão RULE-C46-005)
PORQUE       : ENF-03 (Detector ≠ Gate; LLM não é seu próprio gate); INV-09
```
**Nota de economicidade (RULE-MECH-02):** dois BASpecs Classe C (003/004) são propostos porque
tratam invariantes **distintos e ambos de risco real** — 003 = default fail-closed (ENF-04); 004 =
autoridade de quem computa (ENF-03). Podem ser **fundidos em um só** se Andraus preferir menos
superfície; mantê-los separados torna ENF-03 e ENF-04 auditáveis independentemente. **[PROPOSTA]**

**Contagem:** mantidas 4 BASpecs (CISS-001..004), como no rascunho, mas reclassificadas
D / H / C / C (não "D/H/E"). Alternativa de redução a 3 (fundir 003+004) registrada acima.

---

## 4. Recomendação estrutural — extensão de SPEC-046 vs. Spec autônoma

Formato Opção A/B/C (mesmo da abertura de SPEC-046, `PROPOSTA-ABERTURA.md`):

| Opção | O que é | Prós | Contras |
|---|---|---|---|
| **A (recomendada) — Extensão de SPEC-046 via novo `EC-SPEC046-03` + BASpecs aditivas** | Inter-sessão entra como novo Enforcement Contract e BASpecs CISS-001..004 acrescidos à SPEC-046 (nova versão) | Mesmo **problema-classe** (staleness de documento-fonte spec-time), mesmo **schema** (`freshness_record` estendido), mesmos **agentes** (Grupo B), mesmo **domínio**; EC **aditivo** ≠ reescrita do EC-SPEC046-01 baseline; **proporcionalidade** (EUA-E18) favorece não gerar 4ª Spec para o que é a dimensão de *persistência* de um EC existente | Reabre SPEC-046 baseline (exige DHR de nova versão); a camada de persistência + invariante Classe C são substância nova não-trivial; risco de "inchar" um EC além do que uma extensão comporta |
| **B — Spec autônoma nova (SPEC-047 ou próximo slot)** | D0–D8 completo, Constitution Check próprio, gate de maturidade próprio, Herança/Delta pesada de SPEC-046 | Não reabre baseline; trata persistência + Classe C com profundidade plena; complexidade própria bem isolada | Duplicação de schema/agentes/domínio com SPEC-046; **4ª Spec nova sob o protocolo emergente dispara checagem de proporcionalidade própria** (EUA-E18 Q7 — a rodada de 3 já fechou); overhead de governança maior para ganho incremental |
| **C — Delta-spec leve (MEDIUM) que INHERITS SPEC-046 (CC-08)** | Spec própria, porém MEDIUM (D0–D5), herdando tudo de SPEC-046 e adicionando só persistência + CISS | Meio-termo; isola a substância nova sem full HIGH | Ainda é Spec nova (proporcionalidade); fronteira A/C tênue |

**Recomendação [PROPOSTA]: Opção A (extensão via `EC-SPEC046-03`), complexidade MEDIUM.**
Razões: (i) inter-sessão é a **mesma classe de problema** que intra-sessão, só no eixo de
persistência — mesmo schema, agentes e domínio; (ii) **proporcionalidade** (EUA-E18) desaconselha
uma 4ª Spec nova para uma dimensão de um EC existente; (iii) um EC **aditivo** não reescreve o
EC-SPEC046-01 baseline (INV-07 preservado). **Condição de escalonamento (caveat):** se, na redação,
a camada de persistência + o invariante Classe C exigirem D0–D8 completo e gate de maturidade
próprio, **escalar para Opção B**. A decisão é de **Andraus** — este documento não a fecha (CONS-01).

---

## 5. Dependências, impacto e status

- **Dependências:** SPEC-046 v1.0 BASELINE (schema `freshness_record`, EC-SPEC046-01) · CLASSE-MECH-001
  (D/H/P/C) · ENF-03/ENF-04 · INV-09 · CONS-01 · precedente de infraestrutura BL-019 (`build_map.py`
  hashing + manifesto não-normativo).
- **Impacto estimado** [ESTIMATIVA — ordem de grandeza, não medição]:
  - Economia potencial: ordem de **10⁴–10⁵ tokens/sessão** de releitura de núcleo **condicionada à
    existência de um substrato de reuso cross-sessão** (ver §2.c — sem esse substrato, o manifesto é
    guard, não economia).
  - Custo do mecanismo: ~10²–10³ ms de CPU, ~0 tokens de LLM por início de sessão.
  - Superfície de código nova: ~1 script (ou extensão de `build_map.py`) + 1 entrada de hook +
    1 artefato JSON não-normativo.
- **Status:** **PROPOSTA** — aguarda decisão de Andraus sobre abrir (Opção A/B/C) ou não.
- **Riscos-chave:** (R1) manifesto sozinho não recoloca conteúdo em contexto (§2.c) — não prometer
  economia que ele não entrega; (R2) localização errada (`governance/cache/`) arriscaria baseline
  acidental (INV-09) — mitigado por O3; (R3) ENF-03 — manifesto nunca escrito pelo agente.

---

## 6. Etiquetagem (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| SPEC-046 v1.0 / `freshness_record` / EC-SPEC046-01 | [FONTE] | FATO NORMATIVO (DHR-SPEC046-002) |
| Hashing por arquivo + manifesto não-normativo de `build_map.py` | [FONTE] | FATO ARQUITETURAL (BL-019, `build_map.py:81-82,341`) |
| RULE-MECH-01..04 / taxonomia D/H/P/C | [FONTE] | FATO NORMATIVO (DHR-CLASSE-MECH-001, RULES.md:472-493) |
| BASpecs CISS-001..004, esquema do manifesto, recomendação Opção A | [PROPOSTA] | Requer decisão de Andraus |
| Economia de tokens / custo de CPU | [ESTIMATIVA] | Ordem de grandeza declarada, não medida |
| Grupo A / SPEC-047 | [DECISÃO NECESSÁRIA] | Fora de escopo — futuro |

Nenhuma decisão aberta tratada como fechada (CONS-01). Nada aqui é baseline (INV-09).
