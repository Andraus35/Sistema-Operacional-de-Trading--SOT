# SPEC-002 — Evidence & Evidence Provenance Harness

> ## ⚠ NOTA DE GATE (topo — ler antes de qualquer verificação) — Captura Verbatim RULE-ECC-04 PENDENTE
>
> **Este Plan está ESCRITO, mas NÃO deve ser submetido ao protocolo semântico COMPLETO do Revisor (GRE-001/HRE-001) até a recaptura verbatim real das 7 fontes `[EXTERNO]`.** [FONTE: DHR-SPEC002-VERBATIM-001; atomic-spec §15 RULE-ECC-04]
>
> **Motivo (RULE-MET-01 — honestidade, não-fabricação):** nesta sessão **WebFetch permanece BLOQUEADO por política de egresso** da organização (confirmado nesta rodada: `EGRESS_BLOCKED` em `en.wikipedia.org`; `/root/.ccr/README.md` classifica como negação de política, não-retryável). WebSearch funcionou e sustentou a pesquisa (RULE-ECC-02 — ATENDIDA), mas a **captura verbatim canônica** de RULE-ECC-04 exige o *fetch* da página real. Os arquivos em `specs/features/SPEC-002/sources/SRC-01..07-*.txt` **NÃO são capturas verbatim** — registram URL + data + método (WebSearch) + trecho retornado pelo buscador (possivelmente sintetizado). Ver `sources/_LIMITACAO-WEBFETCH.txt`.
>
> **Estado da decisão:** `SPEC-002-VERBATIM-001` foi decidida por Andraus na abertura — **Opção A** (DHR-SPEC002-VERBATIM-001): homologar a abertura com base na pesquisa WebSearch real e **diferir a captura verbatim RULE-ECC-04 para uma sessão em que WebFetch esteja liberado**, a ser completada **antes** do gate do Plan. Esta rodada tentou o WebFetch novamente (falhou) — portanto a recaptura **segue pendente** (`DHR-SPEC002-VERBATIM-001` permanece o ato vigente; a condição de liberação de WebFetch ainda não ocorreu).
>
> **Efeito:** fail-closed de RULE-ECC-04 (ausência de captura verbatim para fonte carregada = NÃO CONFORME Crítica) permanece formalmente **aberto para este Plan**. O Plan é entregue como `[PROPOSTA]` candidata; a verificação estrutural (`checks.md`) pode rodar; o **protocolo semântico completo + homologação ficam bloqueados** até a recaptura. Nenhuma alegação carregada deste Plan deve ser tratada como verbatim-verificada enquanto isso.

---

| Campo | Valor |
|---|---|
| ID | **SPEC-002 — Evidence & Evidence Provenance Harness** |
| Versão | 1.0 (candidata) |
| Status | **[PROPOSTA] — candidata, aguarda Revisor + Andraus** (NÃO homologada; NÃO baseline). Gate do Plan condicionado à recaptura verbatim RULE-ECC-04 (nota de gate acima). |
| Fonte | `specs/features/SPEC-002/PROPOSTA-ABERTURA.md` + `DOSSIE-PESQUISA.md` (abertura HOMOLOGADA, DHR-SPEC002-001) · ROADMAP §4/§25 · atomic-spec.md v1.4 · CEM-001 (baseline, DHR-TAX-001) |
| Complexidade | CRITICAL (P0 — fundação do núcleo cognitivo; a Evidência alimenta hipótese→fusão→convicção→KG→RAG) |
| Profundidade-alvo | D0–D7 + D8 adversarial (perfil CRITICAL = standard + adversarial — AGENTS.md §4; profundidade homologada na abertura DHR-SPEC002-001 §2) |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | **SPEC-002** — retomada da Trilha B (domínio cognitivo) após a FASE GOV (019+020+021 homologadas); "próximo trabalho autorizado" (ROADMAP §25) |
| Nível de maturidade-alvo | **L3 (Testável)** — gate normativo E3 por-Spec (RULE-MM-05/SPEC-021); teto spec-first = L3 (RULE-MM-04) |
| Classe predominante (orientação, não vinculante — atomic-spec §10.6) | **H (Híbrido)**, com **C (Constitutivo)** para invariantes de imutabilidade/proveniência (declaração normativa por BASpec — CC-11) |
| Método | atomic-spec.md **v1.4** (BASpec/EARS/Enforcement/Classe/D0–D9/§7-bis) |
| Regime normativo citado | **RULE-MECH-01..04** (Classe/Mecanismo — incide) · **RULE-ECC-01/02/04** · **RULE-HD-01..04** (CC-08) · **RULE-EPI/UNC/PRB/CAU/DEC/MET** (N8–N17, registradas em RULES.md sob RULE-REG-001, 2026-09-28) · **ENF-01..08** |
| RULE-PD-01 (CC-12) | **NÃO incide** — CEM-001 é explicitamente neutro de escola/domínio (Cap.1 Princípio 1; Cap.2 "Neutralidade de Domínio"); SPEC-002 não define escopo de especialidade analítica → nenhum `PD-xx` |
| Autor | Especificador Principal SOT |
| Data | 2026-09-28 |

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-09-28 | Plan candidato inicial (D0–D7 + D8). Camada Harness/operacional sobre CEM-001 (não redefine — CC-02). Trata ACH-MEN-01 (reclassificação SRC-03/SRC-06). Registra pendência RULE-ECC-04/verbatim (nota de gate). Primeira Spec-piloto sob EUA-E04..E14 (CC-08/CC-09/CC-10 + N8–N17), RULE-MECH-01 (Classe por BASpec) e RULE-MM (gate de maturidade). **Candidata — aguarda recaptura verbatim, Revisor e Andraus.** |

---

## Nota de gate (passo 11-bis / RMR-001) — itens verificados nesta redação

[FONTE: ROADMAP §23 passo 11-bis; RMR-001 §4]

- **RULE-REG-001** (`spec:SPEC-002 em redação`) — **TRATADO nesta rodada, ANTES deste Plan:** as 10+1 famílias RULE (RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC + RULE-MET) foram **incorporadas fisicamente** ao `governance/RULES.md` como seções próprias (registro do Controlador sob o gatilho, 2026-09-28), com o texto normativo transcrito das PROPOSTAS/DHRs homologadas (EUA-E04..E14) sem alteração (INV-07). Os 6 achados de `check_doc_sync.py` (RULE-DEC-01/RULE-HD-02/RULE-HD-03/RULE-MET-01 citadas como `[Fonte:]` sem seção) foram resolvidos. RULE-REG-001 → **fechada por registro** (não é nova decisão). [FONTE: RULES.md changelog 2026-09-28; AGENTS.md §5]
- **BL-012** (MC-COG-001, gatilho `spec:SPEC-002 homologada (consolidação cognitiva v1.5)`) — dispara apenas na **homologação futura** do Plan/baseline, não nesta redação. Reconhecido; sem ação agora.
- **BL-024** (CACHING SOT, gatilho `evento:abertura da SPEC-002`) — já **Absorvido** (SPEC-046 v1.0/v1.1). Sem ação.
- **BL-002** (método de falso-DENY observável, gatilho `spec:SPEC-003 homologada`) — permanece diferido; este Plan **declara** o requisito ENF-07 para os ECs E3 sem fechar o limiar (CONS-01).
- **BL-003** (persistência física da Evidência) — permanece aberta; storage físico é Non-goal (SPEC-004/006).
- Nenhum item `ATIVADO` novo disparado pela redação deste Plan além de RULE-REG-001 (tratado). [INFERÊNCIA — coerente com RMR-001 §4]

---

## Sanamento do achado Menor do parecer de abertura (ACH-MEN-01)

[FONTE: DHR-SPEC002-001 §3 item 4; parecer do Revisor sobre a abertura]

**ACH-MEN-01** — SRC-03 (Dempster-Shafer) e SRC-06 (Ausência de Evidência / OWA-CWA) haviam sido rotulados com o tipo "Teoria", que **não pertence** à taxonomia R1 do ROADMAP (`Padrão / Prática / Benchmark / Evidência / Experimento / Opinião`, ROADMAP §2 R1). **Reclassificação (esta redação):**

| ID | Tipo anterior (fora de R1) | Tipo R1 corrigido | Justificativa |
|---|---|---|---|
| SRC-03 — Dempster-Shafer (combinação de evidência conflitante) | "Padrão/Teoria" | **Padrão** | É um *framework formal/método matemático estabelecido* de combinação de crença — padrão metodológico, não asserção empírica (Evidência) nem juízo (Opinião). [EXTERNO] |
| SRC-06 — Ausência de Evidência / OWA-CWA / negação-por-falha | "Padrão/Teoria" | **Padrão** | Princípio lógico canônico (open/closed-world assumption; "absence of evidence is not evidence of absence") — padrão de raciocínio formal, não Evidência empírica nem Opinião. [EXTERNO] |

O termo "Teoria" é abandonado nas citações deste Plan; ambas as fontes passam a ser tratadas como **Padrão** `[EXTERNO]`. A reclassificação não altera a recomendação de comparação já homologada (SRC-03 = **ADIAR** para SPEC-003; SRC-06 = **ADOTAR o princípio / ADAPTAR** a representação).

---

## Constitution Check (CC-01..CC-12 — atomic-spec §10.5 + emendas)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** a Evidência é **neutra de escola** (CEM-001 Princípio 1). SPEC-002 não altera a hierarquia analítica; apenas especifica a camada operacional de evidência que os produtores (Agentes da hierarquia) consomem/geram. Produtores de Evidência PRIMARY são AGENTS (Structural/Institutional/etc.); ICT não cria hipótese (irrelevante à camada de evidência). Hierarquia **protegida, não tocada**. [FONTE: CEM-001 Cap.1/Cap.2; INV-01]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** **foco crítico.** SPEC-002 constrói **SOBRE** o CEM-001 (baseline, DHR-TAX-001) — não redefine estrutura (4 camadas), estados (ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED), lineage, imutabilidade nem enumerações governadas. Toda estrutura/estado/lineage referenciados por ID de capítulo; a camada operacional só adiciona **protocolos de operação** ausentes no contrato canônico. CHM-001 referenciado (relação Evidência↔Hipótese), não redefinido. [FONTE: CEM-001; CONST-01]
- [x] **CC-03 — Conviction Vector:** SPEC-002 **não** computa convicção. Evidence Strength (CEM Cap.3, Float 0.0–1.0, força local) ≠ Convicção (CCM, global). Dimensionalidade=8 (FATO NORMATIVO) intocada; fórmula/pesos/limiares **definitivos = J-001 em aberto — [DECISÃO NECESSÁRIA]**. SPEC-002 referencia o slot de força local sem fechar nada de convicção. [FONTE: CEM-001 Cap.3; J-001]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma das 5+5 violada. Custo **não** entra em nada de evidência (INV-04). Nenhum sinal de trading produzido. [FONTE: CEE-001 §10/§11]
- [x] **CC-05 — Complexidade declarada:** **CRITICAL** (P0, núcleo cognitivo). Profundidade D0–D7 + D8. [FONTE: DHR-SPEC002-001 §2]
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card; campos tornam-se obrigatórios na fase de Tasks/BUILD (adiada — atomic-spec §14). Omissão justificada, mesmo tratamento de SPEC-001/019/020/021/046.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06). Rastreabilidade de origem: ROADMAP §4/§25 → Dossiê/Proposta homologados (DHR-SPEC002-001) → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04/RULE-HD):** **presente** (seção própria abaixo); INHERITS = CEM-001 v (baseline) + CHM-001 (relação) + SPEC-001 (padrão/fronteira) + método/regime; ADDED preenchido; REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Eixo VERTICAL (RULE-HV) avaliado: SPEC-002 **não** é decomposição micro de um macro-Spec homologado — herda de **modelo canônico** (CEM-001), não de spec-pai; RULE-HV não incide, RULE-HD sim. [FONTE: RULE-HD-01..04; RULES.md 2026-09-28]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI):** aplicado. **Foco:** ausência de evidência ≠ contraevidência (RULE-EPI-01); **ausente** e **inconclusiva** são estados de 1ª classe (INDETERMINADO válido, não vazio silencioso); qualidade avaliada **qualitativamente** até J-001 (sem falsa precisão — RULE-PRB-02/RULE-EPI). Nenhuma hipótese tratada como fato. [FONTE: RULE-EPI-01..03; RULE-UNC; CC-09]
- [x] **CC-10 — Terminologia concorrente (RULE-SEM):** **N/A quanto a escola de mercado** (CEM domain-neutral). Aplicado a termos técnicos concorrentes decisivos: **Evidência** (CEM, interpretada, produzida por Agente) vs **Observação** (Skill, INV-06) — acepção declarada; **provenance** (protocolo operacional de origem, PROV/PROV-AGENT [EXTERNO]) vs **lineage** (campo canônico do CEM Cap.5, ancestrais diretos) — distinção declarada; **Evidence Strength** (força local, CEM Cap.3) vs **Convicção** (CCM, global) — não colapsar. Nenhum termo canônico do GLOSSARIO/CEM redefinido (RULE-SEM-04). [FONTE: RULE-SEM-01/04; INV-06; CEM Cap.3/Cap.5]
- [x] **CC-11 — Classe/Mecanismo por BASpec (RULE-MECH-01):** **INCIDE** — SPEC-002 cita RULE-MECH-01 no próprio texto (ver D2/D3). Cada BASpec com efeito declara Classe (D/H/P/C), critério 4Es, bounded loop/gate onde H/P, gate de saída onde H/C. Classe **C** reservada aos invariantes de imutabilidade/proveniência (risco alto E3 — RULE-MECH-02: C em risco baixo seria violação de Economicidade). Declaração **por BASpec**, nunca por Spec inteira (SES-001 §50). [FONTE: RULE-MECH-01..04; atomic-spec §10.6]
- [x] **CC-12 — Princípios de Domínio (RULE-PD-01):** **NÃO incide** — CEM-001 é explicitamente neutro de domínio (Cap.1 Princípio 1; Cap.2 "Neutralidade de Domínio"); SPEC-002 não define escopo de especialidade analítica (não é Elliott/SMC/ICT/Fibonacci/estrutural). Nenhum `PD-xx` proposto. Confirmado na abertura (DHR-SPEC002-001 §2). [FONTE: CEM-001 Cap.1/2; DHR-SPEC002-001]

**Checklist de consistência principiológica (GPR-001 §15 / RULE-EV-06):** PC-01 (hierarquia) reforçada — evidência neutra, não altera hierarquia; PC-02/INV-05 (SOT não executa) — SPEC-002 só **registra/marca** evidência e conflito, nunca executa nem resolve conflito (isso é SPEC-003); INV-04 (custo fora da convicção) honrado; 4Es na ordem (Conformidade>Eficácia>Efetividade>Eficiência>Economicidade); rastreabilidade/explicabilidade (CEM Princípios 3/4) — cada registro de evidência é auditável; PB-10/RULE-UNC (preservação de incerteza) — ausência/inconclusiva preservadas, não colapsadas. Item CLASSE-MECH-001: Classe por BASpec (CC-11). Item PRINC-BID-001: N/A (CC-12).

**Disciplinas cognitivas N8–N17 incidentes (RULES.md, registro RULE-REG-001, 2026-09-28):** RULE-EPI-01 (ausência≠contraevidência; hipótese≠fato) · RULE-UNC-01/03 (localizar incerteza; incerteza≠probabilidade — Evidence Strength qualitativo até J-001) · RULE-PRB-02 (não quantificar sem base) · RULE-CAU-01 (independência entre evidências exige mecanismo, não presunção — base do anti-dupla-contagem) · RULE-DEC-01 (SPEC-002 recomenda/registra, não executa nem decide) · RULE-MET-01 (não-fabricação: não declarar independência/proveniência não verificada — declarar limitação) · RULE-INQ-02 (evidência discriminante entre hipóteses concorrentes) · RULE-SEM-01/04 (acepções declaradas; canônico não redefinido).

---

## §7-bis — Autopré-check de Redução de Viés (obrigatório CRITICAL — EUA-E18)

Executado APÓS o Autopré-check (§7) e ANTES da submissão ao Revisor. Reduz — não elimina — o viés de confirmação; a verificação independente do Revisor (Passo 5-bis) compensa parcialmente o resíduo.

### Bloco A — Pergunta adversarial por BASpec (D8 aplicado — CRITICAL/HIGH)

Para cada BASpec CRITICAL/HIGH desta Spec (as 8 são CRITICAL, por serem fundação do núcleo):

- **BASpec-EV-001 (criação/registro):** *"Se estivesse errada, o que seria observável?"* → uma Evidência publicada sem um dos campos obrigatórios do CEM Cap.3 (produtor, observation, interpretation, technical_rationale, rastreabilidade) circularia — verificável por validação de contrato. *ENTÃO verificável por observador independente?* Sim — conformidade CEM é checável por código. *Condição em que QUANDO satisfaz mas ENTÃO não deve ocorrer?* Sim: produtor não autorizado (Skill) tenta publicar → deve REJEITAR (ADV-EV-06).
- **BASpec-EV-002 (registry):** negação = dois Evidence com o mesmo ID, ou versão anterior reescrita → verificável (unicidade/append-only). Coberto por ADV-EV-03.
- **BASpec-EV-003 (qualidade/independência/anti-dupla-contagem):** negação = duas evidências causalmente dependentes contadas como duas confirmações separadas (RULE-004 violada) → ADV-EV-02. Observável: contagem de suporte infla sem mecanismo de independência declarado (RULE-CAU-01).
- **BASpec-EV-004 (natureza incl. ausente):** negação = ausência de evidência registrada/tratada como contraevidência → ADV-EV-01 (o caso adversarial-âncora desta Spec). Observável: um item de natureza CONTRARY cuja fonte é "nada observado".
- **BASpec-EV-005 (marcação de conflito):** negação = SPEC-002 *resolve/funde* o conflito (papel da SPEC-003) → ADV-EV-04. Observável: um campo de "conflito resolvido"/força fundida emitido por esta camada.
- **BASpec-EV-006 (captura de provenance):** negação = evidência sem `activity`/produtor/ferramenta rastreáveis → não reconstruível (P13). Observável por auditoria de rastreabilidade.
- **BASpec-EV-007 (imutabilidade/chain-of-custody):** negação = campo imutável alterado pós-publicação, ou ancestral de lineage removido/adicionado pós-publicação → ADV-EV-03/ADV-EV-07. Observável por diff de campo imutável.
- **BASpec-EV-008 (Evidência↔Hipótese):** negação = hipótese copiando o objeto Evidence em vez de referenciar por ID → viola CEM/CHM. Observável (payload duplicado). 

Nenhuma BASpec ficou sem caso de negação verificável por observador independente → nenhuma marcada `[DECISÃO NECESSÁRIA]` por indeterminação de verificabilidade.

### Bloco B — Herança obrigação-a-obrigação (CC-08 vs CEM-001 / CHM-001 / SPEC-001)

Obrigações herdadas e evidência de satisfação nesta Spec (por ID+versão — RULE-HD-04):

| Origem | Obrigação herdada | Satisfeita em | Evidência |
|---|---|---|---|
| CEM-001 Cap.3 | Contrato de 4 camadas obrigatório; publicação incompleta proibida | BASpec-EV-001; EC-EV-01 PRECOND | Criação exige campos CEM completos, senão REJEITA |
| CEM-001 Cap.4 | Status é o único campo mutável pós-publicação; transições permitidas ACTIVE→SUPERSEDED/INVALIDATED→ARCHIVED; proibidas *→ACTIVE | D5; BASpec-EV-007; EC-EV-07 | Máquina de estados referenciada, não redefinida; imutabilidade E3 |
| CEM-001 Cap.5 | Lineage íntegra; não remover/adicionar ancestrais pós-publicação; Cognitive Trace Reconstruction = capacidade do KG | BASpec-EV-006/EV-007; Non-goal (reconstrução plena = SPEC-006) | Provenance projetada sobre Source Reference/Lineage; reconstrução plena diferida |
| CEM-001 Cap.6 | Consumidor não reinterpreta/modifica Evidência; eventos Evidence Created/Superseded/Invalidated/Archived via EC-COG-005 | D6; BASpec-EV-008 | Referência por ID; eventos emitidos, não redefinidos |
| CEM-001 Princípio 5 | Evidência existe independentemente da hipótese; 1 evidência sustenta N hipóteses | BASpec-EV-008 | Relação por referência, sem acoplamento |
| CHM-001 | Hipótese referencia Evidência por ID; não cascata automática na invalidação | BASpec-EV-008; D6 | `supporting/refuting_evidence_ids`; elegibilidade a revisão, sem cascata |
| SPEC-001 (baseline) | Padrão "camada operacional sobre canônico"; fronteira Fonte→Dado→Evidência→Hipótese; INV-06 (Evidência≠Observação) | D0/D1; BASpec-EV-001/EV-006 | Mesmo padrão arquitetural; Skills produzem Observação, não Evidência |
| INV-07 | Versionamento monotônico; refutado/superseded nunca deletado | BASpec-EV-002/EV-007 | Append-only; SUPERSEDED/INVALIDATED/ARCHIVED preservam histórico |

Nenhuma obrigação herdada foi silenciosamente removida ou enfraquecida (RULE-HD-03); nenhum ADDED contradiz o herdado (RULE-HD-02). Este bloco é o substrato do Passo 5-bis seção A do Revisor.

### Bloco C — Verificação epistêmica (RULE-EPI-01..03 / CC-09)

- Afirmação causal única de risco desta Spec: *"duas evidências independentes contam como duas; duas dependentes contam como uma"* — tem **mecanismo declarado** (dependência causal via Lineage/produtor/fonte comum — RULE-CAU-01; RULE-004), não é correlação presumida. Quando a independência **não puder ser verificada**, a camada **declara a limitação** e trata como potencialmente dependente (fail-closed conservador — RULE-MET-01), nunca presume independência.
- Nenhuma hipótese tratada como fato — SPEC-002 é `[PROPOSTA]`/FATO ARQUITETURAL candidato; CEM-001 é FATO NORMATIVO.
- Incerteza material → **INDETERMINADO** (natureza "inconclusiva"/"ausente" de 1ª classe) em vez de PASS/FAIL forçado.
- Nenhuma probabilidade declarada sem evento bem-formado (RULE-PRB-01) — Evidence Strength é qualitativo local, não probabilidade global; nenhum "X%" fabricado.
- Nenhuma precisão numérica sem base (CC-09) — nenhum limiar numérico de qualidade/independência (RULE-EV-05/J-001 aberto).

### Bloco D — reforço de escopo (ponteiro para §7)

- SPEC-002 **registra e marca** evidência e conflito; **não executa** (INV-05/RULE-DEC-01) e **não resolve/funde** conflito (SPEC-003) — reconfirmado.
- Nenhuma BASpec cruza a fronteira SOT→execução downstream — reconfirmado.
- Toda dependência de decisão de Andraus (J-001, M-001, H-001, BL-002, BL-003, RULE-ECC-04/verbatim) está marcada `[DECISÃO NECESSÁRIA]`/pendente, não como fato.

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-002

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO baseline — RULE-HD-04):
  - Modelo Canônico: CEM-001 (Canonical Evidence Model, BASELINED — DHR-TAX-001, 2026-09-26)
      · Cap.3 (contrato de 4 camadas: Identidade/Origem/Conteúdo Cognitivo/Rastreabilidade)
      · Cap.4 (ciclo de vida: ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED; imutabilidade pós-publicação)
      · Cap.5 (linhagem cognitiva; Cognitive Trace Reconstruction = capacidade do KG)
      · Cap.6 (regras de consumo; eventos cognitivos via EC-COG-005)
      · Princípios 1–8 (Neutralidade, Objetividade, Explicabilidade, Rastreabilidade, Independência,
        Reutilização, Refutabilidade, Interoperabilidade)
  - Modelo Canônico: CHM-001 (Canonical Hypothesis Model, BASELINED) — relação Evidência↔Hipótese
      (consumidora), referenciada, NÃO redefinida
  - Spec baseline: SPEC-001 (Hypothesis Harness, v1.1) — padrão "camada operacional sobre canônico" +
      fronteira Fonte→Dado→Evidência→Hipótese + INV-06 (Evidência≠Observação)
  - Método: atomic-spec.md v1.4 — BASpec/EARS/Enforcement/Classe/D0-D9/F.1-F.4/TRACE-06/§7-bis
  - Governança/regime: RULE-HD-01..04 (CC-08), RULE-EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET
      (N8-N17, RULES.md 2026-09-28), RULE-MECH-01..04 (Classe), RULE-MM-01..07 (maturidade),
      RULE-EV-01..07 (9 lentes), RULE-ECC-01/02/04, ENF-01..08
  - Invariantes: INV-03 (J-001 aberto), INV-04 (custo fora da convicção), INV-05 (SOT não executa),
      INV-06 (Evidência≠Observação), INV-07 (versionamento monotônico), INV-09 (sem baseline informal),
      INV-10 (CEM = idioma canônico da Evidence)

ADDED (delta local — o que esta spec acrescenta SOBRE o CEM-001, sem redefini-lo):
  - Protocolos operacionais de criação/registro/supersessão/invalidação/arquivamento de Evidência
    (COMO o SOT percorre, em operação, os estados canônicos do CEM Cap.4)
  - Evidence Registry como serviço lógico (alocação de ID, versionamento monotônico operacional,
    índice por estado/produtor/domínio, API de consulta/reconstrução) — análogo ao Hypothesis Registry
  - Avaliação operacional de qualidade/independência/temporalidade (qualitativa até J-001) +
    salvaguarda anti-dupla-contagem de evidência dependente (RULE-004/RULE-CAU-01)
  - Natureza operacional: favorável / contraevidência / inconclusiva / AUSENTE como estado de 1ª classe
    (RULE-EPI-01/CC-09) — projeção sobre o conteúdo cognitivo do CEM, sem novo campo canônico
  - Marcação operacional de conflito entre evidências (registrar, sem resolver — resolução = SPEC-003)
  - Protocolo operacional de captura de provenance (producer/tool/skill/version/source/activity —
    vocabulário PROV/PROV-AGENT [EXTERNO] projetado sobre Producer/Origin/Source Reference/Lineage do CEM)
  - Enforcement operacional de imutabilidade e integridade de proveniência/chain-of-custody (Classe C, E3)
  - 8 BASpecs com Classe declarada (EV-001..008) + D4/D5/D6/D7/D8 + Enforcement Contracts EC-EV-01..08

MODIFIED (especialização de regra herdada):
  - (nenhuma) — SPEC-002 não especializa regra do CEM; apenas adiciona a camada operacional.

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo:** RULE-HV (herança VERTICAL macro→micro) **não aplicável** — SPEC-002 herda de um **modelo canônico** (CEM-001), não decompõe um macro-Spec homologado. RULE-HD (herança de canônico/método) é o eixo que incide. [INFERÊNCIA — a confirmar pelo Revisor]

---

## D0 — Missão (Intenção)

O Evidence & Evidence Provenance Harness é a **camada operacional que especifica como o SOT cria, registra, versiona, supersede, invalida, arquiva, qualifica, marca e rastreia Evidências Cognitivas em tempo de execução**, construindo **SOBRE** o modelo canônico CEM-001 (BASELINED). [FONTE: ROADMAP §4; CEM-001]

O Harness **não redefine** a estrutura, os estados, a linhagem nem a imutabilidade da Evidência (responsabilidade do CEM-001 — CC-02/CONST-01); ele especifica:

1. Protocolos de criação/registro e transição de estado operacional da Evidência.
2. Evidence Registry como serviço lógico (ID, versionamento, índice, API de consulta/reconstrução).
3. Avaliação operacional de qualidade, independência e temporalidade — com salvaguarda anti-dupla-contagem.
4. Natureza da Evidência (favorável/contraevidência/inconclusiva/**ausente** como estado de 1ª classe).
5. Marcação de conflito entre evidências (registrar, **sem** resolver — isso é SPEC-003).
6. Captura de provenance operacional (producer/tool/skill/version/source/activity).
7. Enforcement de imutabilidade e integridade de proveniência/chain-of-custody (INV-07).
8. Relação operacional Evidência↔Hipótese (por referência a CHM-001/CEM-001).

**Status epistemológico:** SPEC-002 é FATO ARQUITETURAL candidato a baseline; CEM-001 e CHM-001 são FATO NORMATIVO (BASELINED); CCM-001 (fusão/convicção) é PENDENTE DE REDAÇÃO (SPEC-003, J-001 aberto).

---

## D1 — Escopo e Non-goals

### Dentro do escopo (camada Harness/operacional SOBRE CEM-001)

| Item | Descrição | Fonte |
|---|---|---|
| Criação/registro operacional | Protocolos de como o SOT cria/versiona/supersede/invalida/arquiva Evidência em operação, referenciando o contrato e a máquina de estados do CEM (não redefinindo) | CEM-001 Cap.3/Cap.4; SRC-02 [EXTERNO] |
| Evidence Registry (serviço lógico) | Alocação de ID, versionamento monotônico operacional, índice por estado/produtor/domínio, API de consulta/reconstrução | ROADMAP §4; análogo ao Hypothesis Registry (SPEC-001); SRC-07 [EXTERNO] |
| Qualidade/independência/temporalidade | Avaliação qualitativa (até J-001) de directness/timeliness/independence/agreement + salvaguarda anti-dupla-contagem | SRC-04 [EXTERNO] (adaptar); RULE-004; RULE-CAU-01 |
| Natureza da Evidência | favorável / contraevidência / inconclusiva / **ausente** (1ª classe, open-world); ausência nunca vira contraevidência | SRC-06 [EXTERNO] (adotar princípio); RULE-EPI-01; CC-09 |
| Marcação de conflito | Registrar que há conflito e sua natureza; **sem** resolver/fundir | CEM Cap.3; CONS-01 (resolução = SPEC-003) |
| Provenance operacional | producer(AGENT/ENGINE)/tool/skill/version/source + **activity** de geração, projetados sobre campos canônicos do CEM | SRC-01 [EXTERNO] (adaptar); CEM Cap.2/Cap.5 |
| Chain-of-custody / imutabilidade | Cadeia de custódia e versão imutável verificáveis em operação | SRC-02/SRC-05 [EXTERNO] (adaptar); INV-07; CEM Cap.4 |
| Relação Evidência↔Hipótese | Como a evidência transita para/da hipótese (por referência a CHM-001/CEM-001); fronteira Fonte→Dado→Evidência→Hipótese | CHM-001; CEM-001; INV-06 |
| Auditabilidade (D9 por referência) | O que o Harness deve suportar para reconstrução (P13), sem fechar mecanismo de persistência | CONSTITUTION P13; CEM Cap.5 |

### Fora do escopo (Non-goals explícitos)

| Item | Pertence a | Justificativa |
|---|---|---|
| Redefinir estrutura/estados/lineage/imutabilidade do CEM-001 | CEM-001 (canônico) / GMC-001 | CC-02/CONST-01 |
| Fusão de evidência, agregação, Conviction Vector, fórmula/pesos | SPEC-003 (CCM-001) | Topologia Q-007; **J-001 aberta**; Evidence Strength ≠ Convicção (CEM Cap.3); SRC-03 (Dempster-Shafer) = **ADIAR** |
| Resolver conflito entre evidências | SPEC-003 (Fusion/Conviction) | SPEC-002 **marca**, não resolve — CONS-01 |
| Storage físico da Evidência (Blackboard/KG) | SPEC-004/006/009 | **M-001/H-001/BL-003 abertas** |
| Estados do Blackboard para objetos não-hipótese | SPEC-004 | **M-001 aberta** |
| Limiar numérico de qualidade/independência | SPEC-003/CCM-001 | **J-001 aberta**; RULE-EV-05 (avaliação qualitativa até J-001) |
| Cognitive Trace Reconstruction (implementação) | SPEC-006 (Knowledge Graph) | CEM Cap.5 atribui ao KG |
| Execução de ordem / escopo regulatório de execução (MiFID) | fora do SOT / família RISK | **INV-05** (SOT não executa ordem); SRC-05 = **ADAPTAR** só o princípio de trilha imutável, **REJEITAR** escopo de execução |
| Mecanismo criptográfico específico de tamper-evidence | Implementação (BUILD) | Contrato ≠ mecanismo (atomic-spec §10.1) |

---

## D2 — Regras

```
RULE-EVH-001: Somente produtores autorizados pelo CEM-001 podem criar Evidência. Produtores de
               Evidência PRIMARY são AGENTS (Structural/Institutional/Macro/Sentiment/Risk/Context);
               produtor de Evidência DERIVED é ENGINE autorizado (Fusion Engine). Skills produzem
               Observação, NÃO Evidência (INV-06).
               [FONTE: CEM-001 Cap.2/Cap.6; INV-06] [RULE-MECH-01 incide: Classe H]

RULE-EVH-002: Toda Evidência criada DEVE obedecer ao contrato de 4 camadas do CEM (Cap.3);
               publicação incompleta (sem produtor, observation, interpretation, technical_rationale
               ou rastreabilidade) DEVE ser rejeitada. PRIMARY exige Lineage vazia []; DERIVED exige
               Lineage não-vazia.
               [FONTE: CEM-001 Cap.3/Cap.5] [Classe H, gate de saída = validação de contrato]

RULE-EVH-003: Após publicação, apenas o campo Status é mutável (CEM Cap.4). Nenhum campo de
               Identidade/Origem/Conteúdo Cognitivo/Rastreabilidade PODE ser alterado; nenhum
               ancestral de Lineage PODE ser adicionado/removido. Violação = NÃO CONFORME Crítica.
               [FONTE: CEM-001 Cap.4/Cap.5; INV-07] [Classe C — enforcement de imutabilidade, E3]

RULE-EVH-004: Ausência de evidência NÃO DEVE ser convertida em contraevidência. "Ausente" e
               "inconclusiva" são naturezas de 1ª classe (open-world); a falta de observação vira
               estado explícito (INDETERMINADO), nunca negação silenciosa.
               [FONTE: RULE-EPI-01; RULE-UNC-03; CC-09; SRC-06 [EXTERNO]] [Classe H, gate constitutivo]

RULE-EVH-005: Evidências causalmente dependentes (mesma fonte/produtor/lineage comum) DEVEM ser
               tratadas como uma única para efeito de contagem de suporte — não como confirmações
               independentes. Quando a independência não puder ser verificada, a camada DEVE declarar
               a limitação e tratar como potencialmente dependente (fail-closed).
               [FONTE: RULE-004; RULE-CAU-01; RULE-MET-01; SRC-04 [EXTERNO]] [Classe P]

RULE-EVH-006: Conflito entre evidências DEVE ser registrado (existência + natureza), NUNCA resolvido
               nem fundido nesta camada. Resolução/fusão pertence à SPEC-003 (Fusion/Conviction).
               [FONTE: CEM Cap.3; CONS-01; J-001] [Classe H]

RULE-EVH-007: Toda Evidência DEVE ter provenance operacional rastreável: producer(type+id),
               tool/skill que produziu, version, source reference e a atividade de geração —
               projetados sobre os campos canônicos do CEM (Producer/Origin/Source Reference/Lineage),
               sem criar campo concorrente ao contrato canônico.
               [FONTE: CEM Cap.2/Cap.5; SRC-01/SRC-07 [EXTERNO]] [Classe H captura; integridade = Classe C]

RULE-EVH-008: Hipótese referencia Evidência por Evidence ID (CEM/CHM); NUNCA copia o objeto Evidence.
               A invalidação de Evidência NÃO cascateia automaticamente sobre hipóteses/derivadas —
               apenas as torna elegíveis a revisão (não cascata; avaliação pertence a CHM/CCM/CDM).
               [FONTE: CEM Cap.4/Cap.5; CHM-001; INV-06] [Classe D]

RULE-EVH-009: Nenhuma avaliação de qualidade/independência/natureza DEVE fixar limiar numérico
               dependente de convicção — permanece qualitativa até J-001 (CCM-001/SPEC-003).
               [FONTE: RULE-EV-05; J-001; INV-03; CONS-01] [reforça RULE-EVH-005, não cria BASpec própria]
```

---

## Critérios de Aceitação (EARS)

Notação EARS ("Quando <condição>, o componente DEVE <resposta>"):

1. Quando um AGENT autorizado produz uma observação interpretada conforme seu domínio, o sistema DEVE criar uma Evidência conforme o contrato de 4 camadas do CEM-001 e registrá-la no Evidence Registry em estado ACTIVE.
2. Quando uma Skill (produtor não autorizado) tenta publicar Evidência, o sistema DEVE rejeitar a operação (Skill produz Observação, não Evidência — INV-06).
3. Quando uma Evidência é criada, o sistema DEVE alocar um Evidence ID único e imutável e registrar version = 1 no Registry.
4. Quando duas ou mais evidências compartilham fonte/produtor/lineage comum, o sistema DEVE tratá-las como uma única para contagem de suporte, nunca como confirmações independentes.
5. Quando não há observação disponível para um atributo, o sistema DEVE registrar natureza "ausente"/"inconclusiva" (INDETERMINADO), nunca "contraevidência".
6. Quando duas evidências entram em conflito, o sistema DEVE marcar o conflito e sua natureza, sem resolvê-lo nem fundir forças.
7. Quando uma Evidência é publicada, o sistema DEVE registrar provenance completa (producer/tool/skill/version/source/activity) e torná-la imutável (apenas Status mutável).
8. Quando qualquer componente tenta alterar um campo imutável ou remover/adicionar um ancestral de Lineage após a publicação, o sistema DEVE rejeitar a operação (fail-closed) e preservar o objeto histórico.
9. Quando uma hipótese referencia uma Evidência, o sistema DEVE usar o Evidence ID, nunca copiar o objeto Evidence.

---

## D3 — Comportamento (BASpecs) — Classe declarada (RULE-MECH-01, CC-11)

### BASpec-EV-001 — Criação/registro operacional de Evidência

```
CLASSE        : H (Híbrido)
MECANISMO     : o AGENT/ENGINE produz o conteúdo cognitivo (julgamento de domínio); a validação de
                conformidade com o contrato CEM (4 camadas, autorização de produtor, regra
                PRIMARY/DERIVED×Lineage) é gate determinístico verificável por código
CRITÉRIO 4Es  : Eficácia — evidência mal-formada contamina toda a cadeia downstream; a validação de
                contrato é a garantia mínima, não substituível por atalho mais barato (Economicidade)
BOUNDED LOOP  : no máximo 1 tentativa de correção do payload por submissão; sem retry infinito (RULE-MECH-03)
GATE DE SAÍDA : validação de contrato CEM Cap.3 (campos obrigatórios + PRIMARY/DERIVED×Lineage) — código, não LLM (ENF-03)

BASpec-EV-001:
  QUANDO:       Um AGENT autorizado (CEM Cap.2) conclui uma observação interpretada de seu domínio
                (ou o Fusion Engine deriva de evidências ACTIVE) e solicita a publicação de Evidência
  ENTÃO:        Sistema valida o contrato CEM Cap.3 (Identidade/Origem/Conteúdo Cognitivo/
                Rastreabilidade completos; PRIMARY⇒Lineage=[], DERIVED⇒Lineage≠[]) e, se conforme,
                cria a Evidência com Status=ACTIVE, version=1, Evidence ID alocado pelo Registry,
                Creation Timestamp e provenance registrada; se não conforme, REJEITA (nada publicado)
  PORQUE:       CEM-001 exige contrato completo e produtor autorizado; publicação incompleta é
                proibida (CEM Cap.3/Cap.6); Skill não produz Evidência (INV-06); fundamenta RULE-EVH-001/002
  REFERÊNCIA:   CEM-001 Cap.2/Cap.3; INV-06; RULE-EVH-001; RULE-EVH-002
  VERIFICADO POR:
    DADO        Structural Agent com observação interpretada válida em BTC/H4, Domain=STRUCTURAL,
                Origin=PRIMARY, technical_rationale presente
    QUANDO      Structural Agent invoca createEvidence(...) com todos os campos CEM Cap.3
    ENTÃO       Sistema retorna Evidência com evidence_id != null, version=1, status=ACTIVE, Lineage=[]
    VERIFICAÇÃO evidence.producer_type=="AGENT"; evidence.origin_type=="PRIMARY"; contrato CEM Cap.3 completo
```

### BASpec-EV-002 — Evidence Registry (alocação de ID, versionamento, índice, API)

```
CLASSE        : D (Determinístico)
MECANISMO     : alocação de ID único, versionamento monotônico e indexação são operações determinísticas
                (código puro, sem julgamento do LLM)
CRITÉRIO 4Es  : Eficácia — unicidade de ID e append-only são garantias binárias; sem elas a
                rastreabilidade (P13) e o INV-07 quebram

BASpec-EV-002:
  QUANDO:       O sistema cria uma nova Evidência ou uma nova versão de Evidência existente
  ENTÃO:        Evidence Registry aloca evidence_id único e imutável (nova Evidência) ou incrementa
                version com previous_version_id apontando à anterior (nova versão), atualiza o índice
                por estado/produtor/domínio, e mantém a linhagem de versões monotônica (append-only)
  PORQUE:       ID único e versionamento monotônico são pré-condição de rastreabilidade e auditoria
                (P13); nenhuma versão anterior é deletada/reescrita (INV-07); fundamenta RULE-EVH-002
  REFERÊNCIA:   CEM-001 Cap.3 (Identidade); INV-07; ROADMAP §4 (Registry como serviço lógico)
  VERIFICADO POR:
    DADO        Evidência EV-2026-09-28-001 (version=1, ACTIVE) precisa de nova interpretação
    QUANDO      sistema cria EV-2026-09-28-002 e supersede a anterior
    ENTÃO       EV-...-002.version incrementado; EV-...-001 permanece no Registry (SUPERSEDED),
                índice de estado atualizado
    VERIFICAÇÃO Registry.get(EV-...-001) != null (preservada); ids únicos; version monotônica
```

### BASpec-EV-003 — Qualidade/independência/temporalidade + salvaguarda anti-dupla-contagem

```
CLASSE        : P (Probabilístico com Gate)
MECANISMO     : avaliação qualitativa de directness/timeliness/independence/agreement é julgamento do
                agente (sem verificação binária direta); o gate de dependência (mesma fonte/produtor/
                lineage ⇒ contar como uma) é a parada constitutiva
CRITÉRIO 4Es  : Eficácia — tratar evidências dependentes como confirmações separadas infla o suporte e
                corrompe a convicção downstream; a integridade prevalece sobre Economicidade
BOUNDED LOOP  : avaliação de independência por par de evidências é finita (conjunto de suporte da
                hipótese); sem reprocessamento infinito. Independência não verificável ⇒ decide
                imediatamente "potencialmente dependente" (fail-closed), sem loop adicional

BASpec-EV-003:
  QUANDO:       O Harness avalia um corpo de evidências (≥2) que sustentam a mesma hipótese
  ENTÃO:        Sistema atribui, qualitativamente (até J-001), directness/timeliness/independence/
                agreement a cada Evidência E, para evidências que compartilham fonte/produtor/lineage
                comum, marca-as como dependentes e as conta como UMA única para efeito de suporte;
                quando a independência não puder ser verificada, declara a limitação e trata como
                potencialmente dependente (fail-closed)
  PORQUE:       Evidências causalmente relacionadas contam como uma (RULE-004); independência exige
                mecanismo, não presunção (RULE-CAU-01); não fabricar independência (RULE-MET-01);
                avaliação qualitativa até J-001 (RULE-EV-05); fundamenta RULE-EVH-005/009
  REFERÊNCIA:   RULE-004; RULE-CAU-01; RULE-MET-01; RULE-EV-05; SRC-04 [EXTERNO]
  VERIFICADO POR:
    DADO        EV-A e EV-B derivadas ambas da mesma Source Reference (mesmo feed) sustentando HYP-1
    QUANDO      sistema avalia o suporte de HYP-1
    ENTÃO       EV-A e EV-B marcadas dependentes; contagem de suporte = 1 (não 2)
    VERIFICAÇÃO support_count(HYP-1)==1; flag dependent==true em EV-A/EV-B; nenhuma força fundida (isso é SPEC-003)
```

### BASpec-EV-004 — Natureza da Evidência (favorável/contra/inconclusiva/AUSENTE 1ª classe)

```
CLASSE        : H (Híbrido)
MECANISMO     : a classificação da natureza (favorável/contra/inconclusiva) é julgamento do produtor;
                o gate constitutivo é determinístico: entrada "sem observação" ⇒ natureza ∈
                {ausente, inconclusiva}, NUNCA "contraevidência"
CRITÉRIO 4Es  : Conformidade/Eficácia — converter ausência em negação é um erro epistêmico que
                contamina a hipótese; a proibição prevalece (Economicidade não rebaixa)
BOUNDED LOOP  : classificação é single-shot por Evidência; sem loop
GATE DE SAÍDA : regra código-checável "input=ausência ⇒ output≠CONTRARY" (ENF-03)

BASpec-EV-004:
  QUANDO:       Uma Evidência é classificada quanto à sua relação com uma hipótese, OU quando um
                atributo esperado não tem observação disponível
  ENTÃO:        Sistema registra a natureza como favorável, contraevidência, inconclusiva ou AUSENTE;
                quando não há observação, registra "ausente"/"inconclusiva" (INDETERMINADO) como estado
                explícito de 1ª classe — NUNCA como contraevidência
  PORQUE:       Ausência de evidência não é evidência de ausência (SRC-06 [EXTERNO]); hipótese≠fato e
                anti-conversão silenciosa (RULE-EPI-01); incerteza localizada (RULE-UNC); fundamenta RULE-EVH-004
  REFERÊNCIA:   RULE-EPI-01; RULE-UNC-01/03; CC-09; SRC-06 [EXTERNO]
  VERIFICADO POR:
    DADO        Nenhuma observação institucional (SMC) disponível para o candle corrente
    QUANDO      o Harness registra o estado da evidência institucional para HYP-1
    ENTÃO       natureza = "ausente" (INDETERMINADO), com nota "sem observação neste candle"
    VERIFICAÇÃO evidence.nature ∈ {ABSENT, INCONCLUSIVE}; evidence.nature != CONTRARY
```

### BASpec-EV-005 — Marcação de conflito (registrar, sem resolver)

```
CLASSE        : H (Híbrido)
MECANISMO     : a detecção da natureza do conflito é julgamento; o gate determinístico impede qualquer
                emissão de força fundida/conflito resolvido por esta camada
CRITÉRIO 4Es  : Eficácia — marcar (não resolver) preserva a fronteira com a SPEC-003; resolver aqui
                violaria a topologia Fusion→Conviction
BOUNDED LOOP  : marcação single-shot por par conflitante
GATE DE SAÍDA : ausência de qualquer campo "força fundida"/"conflito resolvido" na saída (ENF-03)

BASpec-EV-005:
  QUANDO:       Duas Evidências ACTIVE apontam em direções incompatíveis sobre a mesma hipótese/atributo
  ENTÃO:        Sistema registra a existência do conflito e sua natureza (ex.: direcional, temporal,
                de fonte), referenciando os Evidence IDs conflitantes — sem resolver, sem fundir, sem
                atribuir força agregada
  PORQUE:       Marcação de conflito é da camada de evidência; resolução/fusão é da SPEC-003
                (Fusion→Conviction); CONS-01 (não fechar J-001); fundamenta RULE-EVH-006
  REFERÊNCIA:   CEM Cap.3; CONS-01; J-001; RULE-EVH-006
  VERIFICADO POR:
    DADO        EV-X (favorável a alta) e EV-Y (favorável a baixa) ACTIVE sobre HYP-1
    QUANDO      o Harness avalia o par
    ENTÃO       registra conflict_marker{evidence_ids:[EV-X,EV-Y], type:"directional", resolved:false}
    VERIFICAÇÃO conflict_marker.resolved==false; nenhuma força agregada emitida por SPEC-002
```

### BASpec-EV-006 — Captura de provenance operacional

```
CLASSE        : H (Híbrido)
MECANISMO     : a captura de producer/tool/skill/version/source/activity é assistida pelo produtor;
                o gate determinístico valida a completude da provenance contra o CEM Cap.2/Cap.5
CRITÉRIO 4Es  : Eficácia/Explicabilidade — sem provenance completa a Evidência não é reconstruível (P13)
BOUNDED LOOP  : captura single-shot na criação
GATE DE SAÍDA : validação de completude de provenance (producer_type/id, source_reference, activity) — código

BASpec-EV-006:
  QUANDO:       Uma Evidência é criada (BASpec-EV-001)
  ENTÃO:        Sistema captura e registra a provenance operacional — producer (type AGENT/ENGINE + id),
                tool/skill que produziu, version, source reference e a atividade de geração
                (invocação que a gerou) — projetada sobre os campos canônicos do CEM (Producer Type,
                Producer ID, Source Reference, Lineage), sem criar campo concorrente
  PORQUE:       Rastreabilidade completa (CEM Princípio 4/Cap.5); vocabulário PROV/PROV-AGENT
                (entity/activity/agent) adaptado, não adotado como canônico (SRC-01 [EXTERNO]);
                fundamenta RULE-EVH-007
  REFERÊNCIA:   CEM Cap.2/Cap.5; SRC-01/SRC-07 [EXTERNO]; RULE-EVH-007
  VERIFICADO POR:
    DADO        Structural Agent (skill confluence-elliott, v2.1) gera Evidência a partir de Market Data
    QUANDO      a Evidência é publicada
    ENTÃO       provenance = {producer_type:"AGENT", producer_id:"structural_agent",
                tool:"confluence-elliott", version:"2.1", source_reference:"Market Data", activity:"<invocação>"}
    VERIFICAÇÃO provenance completa; projetada sobre campos CEM; nenhum campo canônico redefinido
```

### BASpec-EV-007 — Imutabilidade + chain-of-custody + integridade de proveniência

```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement determinístico de imutabilidade pós-publicação — é o próprio gate; rejeita
                qualquer alteração de campo imutável ou de ancestral de Lineage
CRITÉRIO 4Es  : Eficácia/Conformidade — a integridade histórica da cadeia de custódia é invariante de
                risco alto (INV-07); Classe C reservada a este enforcement (RULE-MECH-02)
GATE DE SAÍDA : comparação de campo imutável antes/depois; qualquer diff em campo não-Status = DENY (ENF-03)

BASpec-EV-007:
  QUANDO:       Qualquer componente tenta alterar uma Evidência publicada (campo de Identidade/Origem/
                Conteúdo Cognitivo/Rastreabilidade) OU adicionar/remover ancestral de Lineage
  ENTÃO:        Sistema REJEITA a operação (fail-closed) — apenas transição de Status pelas transições
                permitidas do CEM Cap.4 é aceita; o objeto histórico é preservado (INV-07)
  PORQUE:       Após publicação, só Status é mutável (CEM Cap.4); Lineage é registro histórico imutável
                (CEM Cap.5); versionamento monotônico (INV-07); fundamenta RULE-EVH-003
  REFERÊNCIA:   CEM Cap.4/Cap.5; INV-07; RULE-EVH-003; SRC-02/SRC-05 [EXTERNO]
  VERIFICADO POR:
    DADO        Evidência EV-Z publicada (ACTIVE), campo Interpretation = "correção concluída"
    QUANDO      um componente tenta reescrever EV-Z.Interpretation
    ENTÃO       Sistema rejeita com erro "EVIDENCE_FIELD_IMMUTABLE"; EV-Z preservada intacta
    VERIFICAÇÃO response.error_code=="EVIDENCE_FIELD_IMMUTABLE"; EV-Z.Interpretation inalterado
```

### BASpec-EV-008 — Relação operacional Evidência↔Hipótese (referência, não cópia; não cascata)

```
CLASSE        : D (Determinístico)
MECANISMO     : referência por Evidence ID e propagação de evento de invalidação são determinísticas
CRITÉRIO 4Es  : Eficácia — referência por ID (não cópia) preserva independência (CEM Princípio 5) e
                evita duplicação; não cascata preserva a autonomia do CHM/CCM

BASpec-EV-008:
  QUANDO:       Uma hipótese passa a ser sustentada/refutada por uma Evidência, OU uma Evidência em
                supporting/refuting de uma hipótese transita para INVALIDATED
  ENTÃO:        No primeiro caso, o vínculo é registrado por Evidence ID (nunca cópia do objeto); no
                segundo, o sistema emite o evento "Evidence Invalidated" (via EC-COG-005) e torna a
                hipótese dependente ELEGÍVEL A REVISÃO — sem cascata automática de estado
  PORQUE:       Evidência existe independentemente da hipótese e é referenciada por ID (CEM Princípio 5;
                CHM-001); invalidação não cascateia automaticamente (CEM Cap.4/Cap.5; CHM Princípio da
                Não Cascata); avaliação de impacto pertence a CHM/CCM/CDM; fundamenta RULE-EVH-008
  REFERÊNCIA:   CEM Cap.4/Cap.5; CHM-001; INV-06; RULE-EVH-008
  VERIFICADO POR:
    DADO        HYP-1 com supporting_evidence_ids=[EV-A]; EV-A transita para INVALIDATED
    QUANDO      o Harness processa a invalidação
    ENTÃO       evento "Evidence Invalidated" emitido; HYP-1 marcada elegível_a_revisão (estado não
                muda automaticamente)
    VERIFICAÇÃO HYP-1 referencia EV-A por ID (não cópia); HYP-1.state inalterado; evento emitido
```

---

## D4 — Algoritmo (avaliação de independência / anti-dupla-contagem)

```
ALGORITMO: dedupe_dependent_evidence
ENTRADA:  conjunto S de Evidências ACTIVE que sustentam a hipótese H
PROCESSO:
  1. Para cada par (Ei, Ej) em S:
       se compartilham Source Reference OU Producer ID OU têm lineage com ancestral comum:
           marcar (Ei, Ej) como DEPENDENTES
       senão se independência NÃO verificável (dados insuficientes):
           marcar como POTENCIALMENTE_DEPENDENTES (fail-closed — RULE-MET-01)
       senão:
           marcar como INDEPENDENTES
  2. Agrupar por componente de dependência (fecho transitivo das marcações DEPENDENTES/POTENCIAIS)
  3. support_count(H) = número de GRUPOS (não de Evidências)
SAÍDA:    support_count (inteiro) + mapa de dependência (auditável)
EXEMPLO:  S = {EV-A, EV-B, EV-C}; EV-A e EV-B compartilham Source Reference "feed-X" (dependentes);
          EV-C é de outra fonte (independente) → 2 grupos → support_count = 2 (não 3).
          NOTA: nenhuma FORÇA é agregada aqui (isso é SPEC-003/J-001); apenas a CONTAGEM de suporte
          é deduplicada. Nenhum limiar numérico de qualidade é fixado (RULE-EV-05).
```

> **Fronteira J-001/CONS-01:** este algoritmo **não** pondera, funde nem calcula convicção — apenas evita contar evidência dependente como confirmação independente (RULE-004). A ponderação por dimensão de convicção é da SPEC-003 (CCM-001, J-001 aberto).

---

## D5 — Estados da Evidência (CEM-001 Cap.4 — NÃO redefinidos)

A máquina de estados da Evidência é a do CEM-001 Cap.4 — a SPEC-002 **referencia, não redefine** (CC-02).

| Estado | Descrição (CEM Cap.4) | Elegível para inferência/fusão? |
|---|---|---|
| ACTIVE | Válida e disponível para consumo | **Sim** |
| SUPERSEDED | Substituída por versão mais recente; preservada e auditável | Não |
| INVALIDATED | Considerada incorreta; preserva histórico de erro; auditável | Não |
| ARCHIVED | Retirada da camada operacional ativa; só consulta histórica | Não |

### Transições permitidas [FONTE: CEM Cap.4]

```
ACTIVE      -> SUPERSEDED | INVALIDATED | ARCHIVED
SUPERSEDED  -> ARCHIVED
INVALIDATED -> ARCHIVED
```

### Transições proibidas [FONTE: CEM Cap.4]

```
INVALIDATED -> ACTIVE     SUPERSEDED -> ACTIVE     ARCHIVED -> ACTIVE
```

> **Regra herdada (CEM Cap.4):** Status é o único campo mutável pós-publicação; toda mudança de estado registra timestamp, origem e justificativa (auditabilidade). Nenhuma transição leva de SUPERSEDED/INVALIDATED/ARCHIVED de volta a ACTIVE (fail-closed — BASpec-EV-007). A camada operacional (SPEC-002) especifica **quando/como** o SOT dispara essas transições, não os estados em si.

---

## D6 — Protocolo de Publicação/Eventos (Blackboard por referência; M-001 aberta)

**Storage físico e estados do Blackboard para objetos não-hipótese = fora de escopo (M-001/BL-003 abertas — SPEC-004).** SPEC-002 especifica o **serviço lógico e o contrato de eventos**, não o substrato físico (mesmo padrão que a SPEC-001 usou para o Hypothesis Registry).

### Eventos cognitivos canônicos (CEM Cap.6 — referenciados, não redefinidos)

O ciclo de vida da Evidência emite os eventos canônicos do CEM Cap.6, propagados pela infraestrutura oficial (**EC-COG-005 — Cognitive Event Bus**; contrato operacional do bus = SPEC-005):

| Evento | Disparo |
|---|---|
| Evidence Created | Publicação de nova Evidência (BASpec-EV-001) |
| Evidence Superseded | Nova versão substitui anterior (BASpec-EV-002) |
| Evidence Invalidated | Evidência transita para INVALIDATED (BASpec-EV-008) |
| Evidence Archived | Evidência transita para ARCHIVED |

> **Fronteira declarada (não omitida):** SPEC-002 **emite** os eventos; TTL/delivery/ordering/latência do Event Bus pertencem à **SPEC-005** (produtor não define metadados de transporte — mesmo princípio de SPEC-001 D1). Estados do Blackboard para a Evidência (objeto não-hipótese) = **M-001 aberta**, SPEC-004. Persistência física = **BL-003 aberta**.

---

## D7 — Cenários de Teste

### Cenário-EV-T01 — Criação válida de Evidência PRIMARY por AGENT
```
DADO        Institutional Agent com observação interpretada válida (Domain=INSTITUTIONAL, Origin=PRIMARY),
            todos os campos CEM Cap.3 presentes, Lineage=[]
QUANDO      Institutional Agent invoca createEvidence(...)
ENTÃO       Sistema cria Evidência: evidence_id="EV-2026-09-28-010", version=1, status=ACTIVE,
            producer_type=AGENT, provenance completa; evento "Evidence Created" emitido
VERIFICAÇÃO evidence_id != null; status==ACTIVE; Lineage==[]; contrato CEM Cap.3 completo
```

### Cenário-EV-T02 — Anti-dupla-contagem de evidência dependente
```
DADO        EV-A e EV-B sustentam HYP-1; ambas com Source Reference "feed-X" (dependentes); EV-C de fonte distinta
QUANDO      o Harness avalia o suporte de HYP-1 (dedupe_dependent_evidence)
ENTÃO       EV-A/EV-B agrupadas (1 grupo) + EV-C (1 grupo) → support_count(HYP-1)=2 (não 3)
VERIFICAÇÃO support_count==2; nenhuma força agregada emitida (fronteira SPEC-003)
```

### Cenário-EV-T03 — Ausência tratada como estado de 1ª classe (não contraevidência)
```
DADO        Nenhuma observação estrutural disponível para o candle corrente de HYP-1
QUANDO      o Harness registra o estado da evidência estrutural
ENTÃO       natureza="ausente" (INDETERMINADO) com nota "sem observação neste candle" — nunca CONTRARY
VERIFICAÇÃO evidence.nature ∈ {ABSENT, INCONCLUSIVE}; evidence.nature != CONTRARY
```

### Cenário-EV-T04 — Marcação de conflito sem resolução
```
DADO        EV-X (favorável a alta) e EV-Y (favorável a baixa) ACTIVE sobre HYP-1
QUANDO      o Harness avalia o par
ENTÃO       conflict_marker{evidence_ids:[EV-X,EV-Y], type:"directional", resolved:false} registrado
VERIFICAÇÃO conflict_marker.resolved==false; nenhuma força fundida/convicção emitida por SPEC-002
```

### Cenário-EV-T05 — Imutabilidade pós-publicação (chain-of-custody)
```
DADO        Evidência EV-Z publicada (ACTIVE) com Interpretation registrada
QUANDO      um componente tenta reescrever EV-Z.Interpretation OU remover um ancestral de EV-Z.Lineage
ENTÃO       Sistema rejeita (fail-closed) com "EVIDENCE_FIELD_IMMUTABLE"; EV-Z preservada intacta
VERIFICAÇÃO response.error_code=="EVIDENCE_FIELD_IMMUTABLE"; EV-Z inalterada; histórico preservado
```

---

## D8 — Cenários Adversariais [OBRIGATÓRIO para CRITICAL]

Princípio transversal: **fail-closed** — em condição ambígua/não satisfeita, o sistema NÃO cria/NÃO altera/NÃO converte e retorna erro específico com log. Todo caso é uma **falha esperada**: a ausência da rejeição é defeito de conformidade.

### ADV-EV-01 — Ausência de evidência interpretada como contraevidência (âncora epistêmica)
**DADO:** nenhuma observação disponível para um atributo esperado de HYP-1
**QUANDO:** um componente tenta registrar essa ausência como "contraevidência" (natureza CONTRARY)
**ENTÃO:** sistema DEVE rejeitar/reclassificar para "ausente"/"inconclusiva" (INDETERMINADO); nunca CONTRARY
**PORQUE:** ausência de evidência ≠ evidência de ausência (SRC-06 [EXTERNO]); RULE-EPI-01; RULE-EVH-004; CC-09
**VERIFICAÇÃO:** nature ∈ {ABSENT, INCONCLUSIVE}; nenhuma Evidência CONTRARY cuja fonte é "nada observado"

### ADV-EV-02 — Dupla-contagem de evidência dependente
**DADO:** EV-A e EV-B causalmente dependentes (mesma fonte/produtor/lineage) sustentando HYP-1
**QUANDO:** o sistema tenta contá-las como duas confirmações independentes
**ENTÃO:** sistema DEVE tratá-las como uma única (support_count agrupado); independência não verificável ⇒ potencialmente dependente (fail-closed)
**PORQUE:** RULE-004; independência exige mecanismo (RULE-CAU-01); não fabricar independência (RULE-MET-01); RULE-EVH-005
**VERIFICAÇÃO:** support_count conta grupos, não evidências; flag dependent/potentially_dependent presente

### ADV-EV-03 — Mutação de campo imutável pós-publicação
**DADO:** Evidência publicada (ACTIVE)
**QUANDO:** um componente tenta alterar um campo de Identidade/Origem/Conteúdo Cognitivo/Rastreabilidade
**ENTÃO:** sistema DEVE rejeitar (fail-closed) "EVIDENCE_FIELD_IMMUTABLE"; só Status é mutável (CEM Cap.4)
**PORQUE:** CEM Cap.4 (imutabilidade pós-publicação); INV-07; RULE-EVH-003; EC-EV-07 (E3)
**VERIFICAÇÃO:** response.error_code=="EVIDENCE_FIELD_IMMUTABLE"; objeto preservado

### ADV-EV-04 — Resolver/fundir conflito dentro da SPEC-002
**DADO:** conflito marcado entre EV-X e EV-Y
**QUANDO:** um componente tenta, nesta camada, resolver o conflito ou emitir força agregada/fundida
**ENTÃO:** sistema DEVE rejeitar — resolução/fusão é da SPEC-003 (Fusion→Conviction); SPEC-002 só marca
**PORQUE:** topologia Q-007 (Fusion→Conviction→Synthesis); CONS-01 (J-001 aberto); RULE-EVH-006
**VERIFICAÇÃO:** nenhum campo "conflito resolvido"/força fundida emitido por SPEC-002

### ADV-EV-05 — Origem inconsistente (PRIMARY com Lineage, ou DERIVED por AGENT)
**DADO:** tentativa de criar Evidência PRIMARY com Lineage≠[] OU DERIVED com producer_type=AGENT
**QUANDO:** o produtor invoca createEvidence(...)
**ENTÃO:** sistema DEVE rejeitar — PRIMARY⇒AGENT⇒Lineage=[]; DERIVED⇒ENGINE⇒Lineage≠[] (CEM Cap.3)
**PORQUE:** CEM Cap.3 (Evidence Origin Type); RULE-EVH-002
**VERIFICAÇÃO:** response rejeita; nenhuma Evidência inconsistente publicada

### ADV-EV-06 — Skill (produtor não autorizado) publica Evidência
**DADO:** uma Skill stateless tenta publicar objeto Evidence diretamente
**QUANDO:** producer não ∈ produtores autorizados do CEM (AGENT/ENGINE) invoca createEvidence(...)
**ENTÃO:** sistema DEVE rejeitar "PRODUCER_NOT_AUTHORIZED"; Skill produz Observação, não Evidência
**PORQUE:** INV-06 (Evidência≠Observação); CEM Cap.2/Cap.6; RULE-EVH-001
**VERIFICAÇÃO:** response.error_code=="PRODUCER_NOT_AUTHORIZED"

### ADV-EV-07 — Remoção/adição de ancestral de Lineage pós-publicação
**DADO:** Evidência DERIVED publicada com Lineage=[EV-A, EV-B]
**QUANDO:** um componente tenta remover EV-A ou adicionar EV-C à Lineage após a publicação
**ENTÃO:** sistema DEVE rejeitar (fail-closed) "LINEAGE_IMMUTABLE"; a linhagem é registro histórico imutável
**PORQUE:** CEM Cap.5 (não remover/adicionar ancestrais pós-publicação); INV-07; RULE-EVH-003; EC-EV-07 (E3)
**VERIFICAÇÃO:** response.error_code=="LINEAGE_IMMUTABLE"; Lineage preservada

> **Cobertura:** 7 cenários adversariais formais (mínimo exigido para CRITICAL/D8 = ≥1; §7-bis Bloco A cobre todas as 8 BASpecs). ADV-EV-01 e ADV-EV-02 são os casos-âncora exigidos pela abertura (ausência mal-interpretada como contraevidência; dupla-contagem de dependente).

---

## I/O Schema — Evidência (CEM-001 + extensão operacional de provenance/natureza)

> **Nota (CC-02):** o schema abaixo **referencia** os campos canônicos do CEM-001 Cap.3/Cap.5; a camada operacional adiciona apenas metadados operacionais (nature, provenance.activity, dependency, conflict_marker), sem redefinir nem substituir o contrato canônico.

```json
{
  "evidence_id": "EV-2026-09-28-010",
  "evidence_version": 1,
  "previous_version_id": null,
  "creation_timestamp": "2026-09-28T00:00:00Z",
  "status": "ACTIVE | SUPERSEDED | INVALIDATED | ARCHIVED",
  "producer_type": "AGENT | ENGINE",
  "producer_id": "institutional_agent",
  "evidence_origin_type": "PRIMARY | DERIVED",
  "domain": "STRUCTURAL | INSTITUTIONAL | MACRO | SENTIMENT | RISK | CONTEXT",
  "observation": "o que foi observado (CEM Cap.3)",
  "interpretation": "o que a observação significa (CEM Cap.3)",
  "technical_rationale": "por que essa interpretação (CEM Cap.3)",
  "evidence_strength": 0.0,
  "timeframe_reference": "M5|M15|H1|H4|D1|W1|MN",
  "market_context": "BULL_MARKET | BEAR_MARKET | RANGE | RISK_ON | RISK_OFF",
  "source_reference": "Market Data | Economic Calendar | On-Chain Data",
  "lineage": [],
  "_operational": {
    "provenance": {
      "tool": "confluence-elliott",
      "skill_version": "2.1",
      "activity": "<invocação/atividade de geração — vocabulário PROV adaptado>"
    },
    "nature_vs_hypothesis": {
      "hypothesis_id": "HYP-1",
      "nature": "FAVORABLE | CONTRARY | INCONCLUSIVE | ABSENT"
    },
    "dependency": {
      "dependent_group_id": "grp-1",
      "status": "INDEPENDENT | DEPENDENT | POTENTIALLY_DEPENDENT"
    },
    "conflict_marker": {
      "evidence_ids": ["EV-X", "EV-Y"],
      "type": "directional | temporal | source",
      "resolved": false
    }
  }
}
```

---

## Enforcement Contracts (ENF-01..08)

### EC-EV-01 — Criação/Publicação de Evidência

```
CAPABILITY   : Criar e publicar uma Evidência Cognitiva conforme o contrato CEM-001
EFFECT       : Publicação de Evidência em estado compartilhado (Registry/Blackboard); evento "Evidence Created"
PRECOND      : (producer ∈ produtores autorizados CEM Cap.2) AND (contrato CEM Cap.3 completo) AND
               (PRIMARY⇒AGENT⇒Lineage=[]) AND (DERIVED⇒ENGINE⇒Lineage≠[])
POSTCOND     : Evidência existe com Evidence ID único, version=1, status=ACTIVE, provenance registrada
POLICY       : CEM Cap.2/Cap.3/Cap.6; INV-06; RULE-EVH-001/002
LEVEL        : E2 (Operacional — Evidência de Agente = piso E2; estado compartilhado alterado)
FAILURE-MODE : Rejeitar publicação; nada publicado; log de rejeição
EVIDENCE     : Log de criação (producer_id, evidence_id, timestamp, resultado de validação de contrato)
```

### EC-EV-02 — Alocação de ID / Versionamento (Registry)

```
CAPABILITY   : Alocar Evidence ID único e versionar monotonicamente
EFFECT       : Registro no Evidence Registry; atualização de índice
PRECOND      : (evidence_id inédito) AND (nova versão ⇒ previous_version_id aponta à anterior)
POSTCOND     : ID único alocado; version monotônica; versão anterior preservada
POLICY       : CEM Cap.3; INV-07
LEVEL        : E2 (Operacional)
FAILURE-MODE : Rejeitar; nenhuma reescrita/deleção de versão anterior
EVIDENCE     : Registro de alocação; linhagem de versões auditável
```

### EC-EV-03 — Avaliação de qualidade/independência (anti-dupla-contagem)

```
CAPABILITY   : Avaliar qualidade/independência e deduplicar evidência dependente na contagem de suporte
EFFECT       : Marcação de dependência; support_count deduplicado (NÃO agrega força — SPEC-003)
PRECOND      : (avaliação qualitativa, sem limiar numérico — J-001 aberto) AND
               (independência não verificável ⇒ tratar como potencialmente dependente — fail-closed)
POSTCOND     : Evidências dependentes contadas como uma; mapa de dependência auditável
POLICY       : RULE-004; RULE-CAU-01; RULE-MET-01; RULE-EV-05; J-001
LEVEL        : E2 (Operacional)
FAILURE-MODE : Fail-closed conservador: na dúvida, dependente (nunca inflar suporte)
EVIDENCE     : Mapa de grupos de dependência + support_count por hipótese
```

### EC-EV-04 — Registro de natureza (ausência de 1ª classe; anti-conversão)

```
CAPABILITY   : Registrar a natureza da Evidência (favorável/contra/inconclusiva/ausente)
EFFECT       : Natureza registrada como metadado operacional da Evidência vs hipótese
PRECOND      : (input="ausência de observação" ⇒ nature ∈ {ABSENT, INCONCLUSIVE}, NUNCA CONTRARY)
POSTCOND     : Natureza registrada; ausência preservada como INDETERMINADO explícito
POLICY       : RULE-EPI-01; RULE-UNC-01/03; CC-09; SRC-06 [EXTERNO]; RULE-EVH-004
LEVEL        : E3 (Crítico) — converter ausência em contraevidência corrompe a hipótese downstream de
               forma que só é corrigível a montante; fail-closed
FAILURE-MODE : Fail-closed: na ausência de observação, jamais emitir CONTRARY; reclassificar/rejeitar
EVIDENCE     : Registro de natureza + nota de ausência/inconclusividade; amostra auditável
MÉTODO DE FALSO-DENY (ENF-07): amostragem periódica de itens classificados ABSENT/INCONCLUSIVE para
               confirmar que nenhum era, de fato, contraevidência legítima suprimida. LIMIAR de
               falso-DENY = [DECISÃO NECESSÁRIA: BL-002] (diferido a SPEC-003; declarado, não fechado — CONS-01)
```

### EC-EV-05 — Marcação de conflito (sem resolver)

```
CAPABILITY   : Registrar conflito entre evidências
EFFECT       : conflict_marker registrado (resolved=false)
PRECOND      : (nenhuma força agregada/fundida é emitida por esta camada)
POSTCOND     : Conflito e sua natureza registrados; referência aos Evidence IDs conflitantes
POLICY       : CEM Cap.3; CONS-01; J-001; RULE-EVH-006
LEVEL        : E2 (Operacional)
FAILURE-MODE : Rejeitar qualquer tentativa de resolução/fusão nesta camada (fronteira SPEC-003)
EVIDENCE     : conflict_marker auditável; ausência de campo de força fundida
```

### EC-EV-06 — Captura de provenance operacional

```
CAPABILITY   : Capturar e registrar provenance (producer/tool/skill/version/source/activity)
EFFECT       : Provenance registrada, projetada sobre campos canônicos do CEM
PRECOND      : (provenance completa: producer_type/id, source_reference, activity presentes)
POSTCOND     : Provenance rastreável; Evidência reconstruível (P13) até origem
POLICY       : CEM Cap.2/Cap.5; SRC-01/SRC-07 [EXTERNO]; RULE-EVH-007
LEVEL        : E2 (Operacional)
FAILURE-MODE : Rejeitar publicação sem provenance completa (fail-closed)
EVIDENCE     : Registro de provenance; ausência de campo concorrente ao CEM
```

### EC-EV-07 — Imutabilidade / Chain-of-custody / Integridade de proveniência

```
CAPABILITY   : Enforçar imutabilidade pós-publicação de campos canônicos e da Lineage
EFFECT       : Rejeição de qualquer alteração de campo imutável ou de ancestral de Lineage
PRECOND      : (alteração solicitada afeta apenas o campo Status por transição permitida CEM Cap.4)
POSTCOND     : Campos imutáveis preservados; Lineage íntegra; objeto histórico preservado (INV-07)
POLICY       : CEM Cap.4/Cap.5; INV-07; RULE-EVH-003
LEVEL        : E3 (Crítico + irreversível) — corrupção da cadeia de custódia é irreversível; fail-closed
FAILURE-MODE : Fail-closed: DENY a qualquer diff em campo não-Status; erro específico; objeto intacto
EVIDENCE     : Diff de campo imutável (antes/depois) + registro de DENY; audit trail (P13)
MÉTODO DE FALSO-DENY (ENF-07): amostragem de operações DENY para confirmar que nenhuma transição de
               Status legítima (CEM Cap.4) foi bloqueada indevidamente. LIMIAR = [DECISÃO NECESSÁRIA: BL-002]
               (diferido; declarado, não fechado — CONS-01)
```

### EC-EV-08 — Relação Evidência↔Hipótese (referência; não cascata)

```
CAPABILITY   : Vincular Evidência a hipótese por ID e propagar evento de invalidação
EFFECT       : Vínculo por Evidence ID; evento "Evidence Invalidated"; hipótese elegível a revisão
PRECOND      : (vínculo usa Evidence ID, nunca cópia do objeto Evidence)
POSTCOND     : Referência por ID registrada; na invalidação, hipótese marcada elegível a revisão (sem cascata)
POLICY       : CEM Cap.4/Cap.5; CHM-001 (Não Cascata); INV-06; RULE-EVH-008
LEVEL        : E1 (Contratual — vínculo por referência) / E2 na emissão de evento de invalidação
FAILURE-MODE : Rejeitar cópia de objeto Evidence; nenhuma cascata automática de estado
EVIDENCE     : Referência por ID auditável; evento de invalidação registrado
```

### Escala E0–E3 (F.1–F.4) — referência [ENF-08]

Níveis conforme atomic-spec §10.2 (E0 orientação · E1 contratual · E2 operacional · E3 crítico/fail-closed). Piso por tipo: Evidência de Agente → E2 mínimo; enforcement de imutabilidade/integridade e anti-conversão de ausência → E3 (criticidade × irreversibilidade). Economicidade nunca rebaixa (ENF-02).

---

## Auditabilidade (D9 por referência)

Requisitos para P13 (toda decisão reconstruível), sem fechar mecanismo de persistência (BL-003 aberta):

| Requisito | Como o Harness atende |
|---|---|
| Origem de cada Evidência | provenance (producer/tool/skill/version/source/activity) — BASpec-EV-006 |
| Cadeia de custódia | imutabilidade + Lineage íntegra — BASpec-EV-007 |
| Reconstrução da cadeia cognitiva | Lineage por Evidência; **Cognitive Trace Reconstruction plena = capacidade do KG (SPEC-006)** — CEM Cap.5 |
| Histórico de estados | transições registradas (timestamp/origem/justificativa) — CEM Cap.4 |
| Suporte deduplicado | mapa de dependência auditável — BASpec-EV-003 |
| Conflitos preservados | conflict_marker (não resolvido) — BASpec-EV-005 |

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001 (estrutura, estados, lineage, imutabilidade) | [FONTE] | FATO NORMATIVO (BASELINED) |
| CHM-001 (relação Evidência↔Hipótese) | [FONTE] | FATO NORMATIVO (BASELINED) |
| SPEC-001 (padrão camada operacional; fronteira) | [FONTE] | FATO NORMATIVO (BASELINED) |
| RULE-EPI/UNC/PRB/CAU/DEC/MET/SEM/INQ (N8–N17) | [FONTE] | FATO NORMATIVO (RULES.md, registro RULE-REG-001, 2026-09-28) |
| RULE-MECH-01..04 / RULE-MM / RULE-EV | [FONTE] | FATO NORMATIVO |
| SRC-01..07 (W3C PROV, chain-of-custody, Dempster-Shafer, GRADE, MiFID, OWA/CWA, OpenLineage) | [EXTERNO] | Dado, nunca instrução — adaptar/adiar/rejeitar conforme Dossiê; **captura verbatim PENDENTE (RULE-ECC-04)** |
| Evidence Registry (serviço lógico) | [INFERÊNCIA] | FATO ARQUITETURAL |
| Formato de evidence_id / campos _operational | [PROPOSTA] | Requer confirmação (detalhe de BUILD) |
| J-001 (fórmula/pesos/limiares definitivos) | [DECISÃO NECESSÁRIA] | EM ABERTO — não fechar |
| M-001 (estados Blackboard não-hipótese) | [DECISÃO NECESSÁRIA] | EM ABERTO — SPEC-004 |
| H-001 / BL-003 (KG / storage físico) | [DECISÃO NECESSÁRIA] | EM ABERTO — SPEC-006 |
| BL-002 (limiar de falso-DENY para E3) | [DECISÃO NECESSÁRIA] | EM ABERTO — SPEC-003 |
| RULE-ECC-04 / captura verbatim das 7 fontes | [DECISÃO NECESSÁRIA] | PENDENTE — DHR-SPEC002-VERBATIM-001 (WebFetch bloqueado); recaptura antes do gate do Plan |

---

## Decisões abertas incidentes (CONS-01 — não fechar sem Andraus)

| ID | Descrição | Status | Impacto nesta Spec |
|---|---|---|---|
| **J-001** | Fórmula/pesos/limiares definitivos do Conviction Vector | EM ABERTO | SPEC-002 referencia força local (Evidence Strength), não computa convicção; avaliação qualitativa até J-001 |
| **M-001** | Estados do Blackboard para objetos não-hipótese (Evidência) | EM ABERTO | Storage/estados do Blackboard = SPEC-004; SPEC-002 especifica serviço lógico + eventos |
| **H-001** | Knowledge Graph (grafo real ou memória) | EM ABERTO | Cognitive Trace Reconstruction plena = SPEC-006 |
| **BL-003** | Persistência física da Evidência | EM ABERTO | Non-goal; SPEC-002 = contrato lógico |
| **BL-002** | Método/limiar observável de falso-DENY para efeitos E3 | EM ABERTO | EC-EV-04/EC-EV-07 declaram ENF-07 sem fechar limiar (diferido a SPEC-003) |
| **SPEC-002-VERBATIM-001** | Captura verbatim RULE-ECC-04 sob WebFetch bloqueado | PENDENTE (Opção A homologada; recaptura ainda não ocorreu) | Bloqueia o protocolo semântico completo do Revisor + homologação (nota de gate no topo) |

---

**Pronto para verificação estrutural (`checks.md`).** **NÃO pronto para o protocolo semântico completo do Revisor nem para homologação** enquanto a captura verbatim RULE-ECC-04 das 7 fontes não for refeita com WebFetch operacional (DHR-SPEC002-VERBATIM-001) — ver nota de gate no topo.

[DECISÃO NECESSÁRIA] que permanece em aberto nesta Spec: J-001; M-001; H-001; BL-003; BL-002; SPEC-002-VERBATIM-001 (captura verbatim das 7 fontes [EXTERNO]).
