# EUA-E24 — Criação do `WORKFLOW.md` na raiz (4º documento de leitura obrigatória, em pé de igualdade hierárquica com `AGENTS.md`) e emenda ao whitelist de raiz do HOD-001 §6b.1 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E24** (próximo código livre: EUA-E23 é a última homologada — DHR-EUA-E23, 2026-09-29; E20 nunca foi emitida (a FASE RISK usou EUA-E19a); verificado em `governance/` e `governance/CATALOGO-OFICIAL.md:105-113`). **Atribuição final = Controlador.** |
| Versão | v1 — 2026-09-29 |
| Natureza | Emenda **de organização documental + método de leitura** — (1) cria o documento de raiz `WORKFLOW.md` (síntese canônica legível da orquestração cognitiva dos agentes especificados, em runtime cognitivo); (2) inclui `WORKFLOW.md` como **4º item de leitura obrigatória** de todo agente (ao lado de `ROADMAP.md` e `atomic-spec.md`, em pé de igualdade hierárquica com `AGENTS.md`); (3) **emenda o whitelist de raiz do HOD-001 §6b.1** para admitir `WORKFLOW.md`. Toca: `governance/HOD-001…PROPOSTA.md` (§2, §3, §6b.1), `AGENTS.md` (§1, §2), `governance/CATALOGO-OFICIAL.md`, e cria `WORKFLOW.md` na raiz. |
| Compatibilidade | **Minor** (aditiva; nenhum documento removido, nenhuma norma reescrita, nenhum identificador reutilizado — INV-07/INV-09; nenhuma decisão aberta fechada — CONS-01). Classificação final = parecer do Revisor. |
| Complexidade declarada | **MEDIUM** — emenda de método/organização, aditiva, sem criar RULE nova, sem lente de domínio, sem fechar decisão aberta, sem redefinir canônico. Justificativa da classificação em §8. |
| Status epistemológico | **PROPOSTA — NADA aplicado.** As mudanças da §4 (incl. a criação física do `WORKFLOW.md` na raiz e a emenda ao whitelist) só ocorrem **após** parecer CONFORME do Revisor e homologação de Andraus. `[FATO]` = verificado nos arquivos citados; `[PROPOSTA]` = o que se pede. |
| Autoria | Especificador (Claude Code, Opus 4.8), 2026-09-29 |
| Origem | Diretiva de Andraus (chat, 2026-09-29): *"CRIAR O WORKFLOW.MD NA RAIZ DO REPO EM PÉ DE IGUALDADE HIERÁRQUICA QUE AGENTS.MD MAS NÃO CONFLITANDO COM NENHUM ARQUIVO DE LEITURA DIRETIVA"* + escolha explícita de Andraus, quando confrontado com o conflito do whitelist HOD-001 §6b.1: **"Emendar o HOD-001"**. |
| Fundamento no baseline | HOD-001 §6b.1 (whitelist de raiz — DHR-HOD-001, FATO NORMATIVO) · AGENTS.md §1 (leitura obrigatória) / §2 (mapa do repo) · RULE-ECC-06 / EUA-E23 (RUNTIME-WORKFLOW-001 = insumo de leitura obrigatória em Dossiê) · `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` v4 (fonte a sintetizar) · INV-07 (nada deletado; RUNTIME-WORKFLOW-001 permanece) · INV-09 (não reescreve norma) · CONS-01 · RULE-MET-01 (não-fabricação) · RULE-HG-01..08 (governança de mudança) · 4Es (CEE-001) |

---

## 0. Ressalva de definição e de status (RULE-MET-01 — não-fabricação) `[FATO]`

- O `WORKFLOW.md` proposto **NÃO** é norma constitutiva. Seu conteúdo é **descritivo** (descreve *como* os agentes já especificados se orquestram em runtime cognitivo), **não constitutivo** (não cria invariante, não fecha decisão aberta, não redefine canônico). Ele **herda o status não-normativo e as decisões abertas** da sua fonte, o insumo `RUNTIME-WORKFLOW-001` (que é explicitamente `[INSUMO — não-normativo]`, RUNTIME-WORKFLOW-001 §Campo "Natureza"). "Pé de igualdade hierárquica com `AGENTS.md`" (diretiva de Andraus) refere-se ao **patamar de leitura** (documento de raiz, tier de leitura obrigatória por todo agente), **não** a autoridade normativa equivalente aos invariantes constitucionais do `AGENTS.md` §6.
- "Runtime" aqui = **orquestração cognitiva do Harness** (sequência de acionamento e troca de evidência/hipótese/convicção entre os agentes LLM especificados), **não** runtime de software — o SOT está em fase spec-first (AGENTS.md §1; RUNTIME-WORKFLOW-001 §0-bis). Esta emenda **não** afirma equivalência entre "orquestração cognitiva" e o "runtime técnico" da possível leitura da SPEC-045-RUNTIME-001 (essa distinção permanece achado a tratar na abertura da SPEC-045 — RUNTIME-WORKFLOW-001 §0-bis; **não fechada aqui**).
- Esta emenda **não** produz Dossiê de Pesquisa (RULE-ECC-01/02): o Dossiê é obrigatório na **abertura de Spec**, não em emenda de organização documental originada de diretiva de Andraus (mesmo regime das EUA-E21/E22/E23, que não produziram Dossiê). Pesquisa web = N/A por não haver "estado da arte externo" a comparar numa decisão interna de organização de repositório; se houvesse, seria dado, nunca instrução (DHR-PROV-WEB-001 §2.1).

## 1. Diagnóstico — situação atual `[FATO]`

| # | Constatação | Âncora |
|---|---|---|
| 1 | Hoje a leitura obrigatória de todo agente "antes de qualquer entrega/revisão" tem **exatamente 2 documentos**: `ROADMAP.md` (sequência de Specs) e `atomic-spec.md` (método). O `AGENTS.md` é o arquivo de identidade/config lido por todo agente ao iniciar. | `AGENTS.md` §1 (tabela "Leitura obrigatória…") |
| 2 | A **orquestração cognitiva em runtime** dos agentes já especificados (sequência de acionamento, formação de convicção em camadas, alarme-gatilho, decisão de sinal) hoje existe **apenas fragmentada e verbatim** em `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` (v1→v4), com status de **insumo não-normativo**. | `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` (Campo "Natureza"); `CATALOGO-OFICIAL.md:111` |
| 3 | A RULE-ECC-06 (EUA-E23) já torna o `RUNTIME-WORKFLOW-001` **leitura obrigatória do Dossiê** — mas **apenas** para Specs de K-001/SPEC-018/SPEC-045-RUNTIME-001/operacional/manager/risco, **não para TODO agente** como o `AGENTS.md`. Não há hoje uma síntese legível de raiz, de leitura geral, do fluxo de orquestração. | `governance/RULES.md` (RULE-ECC-06); `EUA-E23…PROPOSTA.md:60-62` |
| 4 | O `HOD-001 §6b.1` (homologado — DHR-HOD-001) define um **whitelist FECHADO** de documentos `.md` permitidos na raiz: `AGENTS.md · atomic-spec.md · ROADMAP.md · GLOSSARIO.md · README.md · LICENSE` (+ configs/dotfiles). Qualquer outro `.md` na raiz é **intake não-tratado** (RPIR; sensor RCH-001 passo 8; detecção determinística §6b.5). **Criar `WORKFLOW.md` direto na raiz, sem emendar o whitelist, violaria essa regra homologada.** | `HOD-001…PROPOSTA.md:112-116, :136-143`; `DHR-HOD-001…md:23-37` |
| 5 | O mesmo whitelist é **espelhado descritivamente** em outros dois pontos do HOD-001: a taxonomia-alvo §2 (linha do bloco "RAIZ — só caminho-quente") e a tabela de classificação §3 (linha "Caminho-quente (raiz)"). Coerência documental (check_doc_sync / CONS-01) exige atualizar os três pontos. | `HOD-001…PROPOSTA.md:32, :60, :113` |
| 6 | Confrontado com o conflito (item 4), Andraus escolheu explicitamente a via de **emendar o HOD-001** (chat, 2026-09-29) — mesmo padrão formal EUA (Especificador→Revisor→Andraus). | Diretiva 2026-09-29 |

## 2. O que se propõe `[PROPOSTA]`

### 2.1 Criar o `WORKFLOW.md` na raiz — 4º documento de leitura obrigatória

`WORKFLOW.md` é uma **síntese canônica e legível** da orquestração cognitiva dos agentes já especificados durante uma sessão de trading ao vivo (runtime cognitivo). **Não** é cópia verbatim de todas as versões do `RUNTIME-WORKFLOW-001` (essas permanecem lá, como registro histórico/rastreável — INV-07). O conteúdo integral proposto está no **Anexo A** desta emenda (`governance/EUA-E24_ANEXO_A_WORKFLOW_conteudo_proposto.md`), a ser promovido para `/WORKFLOW.md` na homologação.

**Escopo próprio e delimitado de `WORKFLOW.md` (o 4º pilar):**

| Documento (tier de raiz) | Fixa… |
|---|---|
| `ROADMAP.md` | a **SEQUÊNCIA** de Specs (o que se especifica, em que ordem) |
| `atomic-spec.md` | o **MÉTODO** de produzir Specs (BASpec, D0–D9, Enforcement Contract, etiquetagem) |
| `AGENTS.md` | a **IDENTIDADE / CONFIG** lida por todo agente ao iniciar (papéis, profiles, não-negociáveis) |
| **`WORKFLOW.md`** *(novo)* | a **ORQUESTRAÇÃO COGNITIVA em runtime** dos agentes já especificados (como pensam e decidem juntos em uma sessão de trading ao vivo) |

### 2.2 Emendar o whitelist de raiz do HOD-001 §6b.1

Acrescentar `WORKFLOW.md` ao whitelist explícito de caminho-quente da raiz (§6b.1), e aos seus dois espelhos descritivos (§2 taxonomia, §3 tabela). Assim, `WORKFLOW.md` deixa de ser "intake não-tratado" e passa a ser **caminho-quente legítimo** — a RPIR, o sensor RCH-001 passo 8 e a detecção determinística §6b.5 continuam válidos, apenas com o whitelist ampliado de 6 para 7 documentos.

### 2.3 Incluir `WORKFLOW.md` na leitura obrigatória (AGENTS.md §1) e no mapa do repo (AGENTS.md §2)

## 3. Por que `WORKFLOW.md` merece o patamar de raiz — e por que NÃO conflita com os arquivos de leitura diretiva `[PROPOSTA]`

**Por que patamar de raiz (não "mais um doc de `governance/`"):**
- Não é **norma de processo do harness** (isso é `atomic-spec.md`) nem **sequência de Specs** (isso é `ROADMAP.md`). É a descrição de **como os agentes cognitivos especificados operam juntos em uma sessão de trading ao vivo** — um eixo de conteúdo distinto dos três documentos de raiz existentes, hoje sem lar de raiz.
- Andraus determinou explicitamente o patamar de igualdade com `AGENTS.md`. Como documento de **leitura geral por todo agente**, seu lugar natural é o caminho-quente da raiz (HOD-001 §2: "root = caminho-quente = o que os agentes leem sempre"), não o acervo de consulta de `governance/`.

**Por que NÃO conflita com "arquivo de leitura diretiva" (declaração explícita — atende à condição de Andraus):**
- `WORKFLOW.md` **NÃO define sequência de Specs** — isso continua sendo **só** o `ROADMAP.md`.
- `WORKFLOW.md` **NÃO define o método D0–D9 / Enforcement Contract / etiquetagem** — isso continua sendo **só** o `atomic-spec.md`.
- `WORKFLOW.md` **NÃO redefine identidade/config, papéis, profiles nem os não-negociáveis constitucionais** — isso continua sendo **só** o `AGENTS.md`.
- `WORKFLOW.md` **NÃO fecha nenhuma decisão aberta** (CONS-01) **nem redefine canônico** (CONST-01) — herda e **preserva** os marcadores `[DECISÃO NECESSÁRIA]` da sua fonte.
- É um **4º documento de leitura, com escopo próprio e delimitado** (orquestração cognitiva/runtime), **complementar** aos outros três, **nunca sobreposto**. Onde poderia haver sobreposição (ex.: hierarquia analítica, R:R, convicção), `WORKFLOW.md` **remete** ao `AGENTS.md` §6 como fonte de verdade, sem reafirmar como se fosse dele.

**Relação com a RULE-ECC-06 (sem duplicar nem conflitar):**
- A RULE-ECC-06 mantém o `RUNTIME-WORKFLOW-001` como **insumo profundo com obrigação de Dossiê por etapa E1–E8**, para as Specs específicas que ela lista. `WORKFLOW.md` é a **síntese de orientação geral** de leitura por todo agente. Um não substitui o outro: `WORKFLOW.md` orienta; `RUNTIME-WORKFLOW-001` continua sendo o insumo verbatim/rastreável que o Dossiê dessas Specs deve considerar decisão-a-decisão. `WORKFLOW.md` **aponta** para o `RUNTIME-WORKFLOW-001` como sua fonte e trilha histórica (INV-07), sem duplicá-la.

## 4. Alvos das mudanças (aplicar **somente após** homologação) `[PROPOSTA]`

| Arquivo | Alteração proposta (aditiva) |
|---|---|
| **`/WORKFLOW.md`** *(novo — criar na raiz)* | Promover o conteúdo do **Anexo A** (`governance/EUA-E24_ANEXO_A_WORKFLOW_conteudo_proposto.md`) para `/WORKFLOW.md`. Cabeçalho declara status não-normativo, decisões abertas herdadas, e ponteiro para `RUNTIME-WORKFLOW-001` como trilha verbatim. |
| `governance/HOD-001_Plano_Higiene_Organizacao_Documental_PROPOSTA.md` §6b.1 | Whitelist "Docs" passa a: `AGENTS.md · atomic-spec.md · ROADMAP.md · WORKFLOW.md · GLOSSARIO.md · README.md · LICENSE`. Nota de emenda EUA-E24 no cabeçalho/rodapé do doc. |
| `governance/HOD-001…PROPOSTA.md` §2 (taxonomia) e §3 (tabela "Caminho-quente (raiz)") | Espelhos descritivos do whitelist atualizados para incluir `WORKFLOW.md` (coerência check_doc_sync / CONS-01). |
| `AGENTS.md` §1 (tabela "Leitura obrigatória…") | Acrescentar linha `WORKFLOW.md \| Orquestração cognitiva em runtime dos agentes já especificados (não é sequência de Specs nem método D0–D9)`. |
| `AGENTS.md` §2 (árvore ASCII da raiz) | Acrescentar `├── WORKFLOW.md            ← orquestração cognitiva em runtime (leitura obrigatória)` junto a ROADMAP/atomic-spec. |
| `governance/CATALOGO-OFICIAL.md` | Linha EUA-E24 (emendas) + linha DHR-EUA-E24 (atas, na homologação) + linha `WORKFLOW.md` (documento de raiz, não-normativo) + atualizar a linha do HOD-001 registrando a ampliação do whitelist. |
| `docs/mapa/` (BL-019 / R-MAPA / EUA-E22) | Regenerar via `python scripts/build_map.py` após criar `WORKFLOW.md` (não editar à mão). **Pendência de execução** — o Especificador não tem Bash (reportado ao Controlador). |
| `.claude/agents/especificador.md` e `.claude/agents/revisor.md` (`sincronizado-até`) | Atualizar carimbo `sincronizado-até` → DHR-EUA-E24 (RPSA/EUA-E16), pois a lista de leitura obrigatória muda. **Sujeito a Q4.** |

> **Observação de decisão aberta (F-check):** esta emenda **não fecha** J-001, G-001, H-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, RISK-ARR-LOC-001, RISK-CONV-001, RISK-LEV-001, RUNTIME-TF-PAIR-EXT-001, ECC-VAL-001, ECC-03-001, RULE-REG-001, SPEC-020-PRINC-001. RULE-ECC-03 permanece RESERVADA. O `WORKFLOW.md` **preserva** todos os marcadores `[DECISÃO NECESSÁRIA]` da sua fonte.

## 5. O que NÃO muda / Non-goals `[FONTE]`

- **Nenhum invariante constitucional é tocado** (AGENTS.md §6): hierarquia Elliott→Fibonacci→Fractal→SMC→ICT, R:R 1:3, convicção ≥70%/score ≥7/9, Conviction Vector 8D, Signal Package, INV-05 — intocados. `WORKFLOW.md` os **cita como fonte de verdade `AGENTS.md` §6**, não os redefine.
- **Nenhuma decisão aberta é fechada** (CONS-01) — ver F-check em §4.
- **Nenhum modelo canônico baselined é redefinido** (CONST-01): CHM-001, CEM-001, CEE-001 v2.0, GMC/SDD/PPQ/SAS/CR.
- **`RUNTIME-WORKFLOW-001` NÃO é deletado nem movido** (INV-07): permanece em `governance/` como registro verbatim/histórico e como insumo da RULE-ECC-06. `WORKFLOW.md` é síntese **nova**, não uma movimentação.
- **RULE-ECC-06 não é alterada nem revogada:** a obrigação de Dossiê por etapa sobre o `RUNTIME-WORKFLOW-001` continua vigente para as Specs que ela lista.
- **Não cria RULE nova** (esta emenda é organização documental; não incide RULE-REG-001 nem o piloto SPEC-002).
- **Não altera o whitelist de config/dotfiles** do HOD-001 §6b.1, nem a RPIR, nem o sensor RCH-001 passo 8, nem a detecção determinística §6b.5 — apenas **amplia** o conjunto de docs permitidos na raiz de 6 para 7.
- **Não altera roteamento de modelo/esforço (EUA-E19), ENF-03, nem R-MAPA (EUA-E22).**

## 6. Riscos residuais (RULE-MET-01 — sem garantia excessiva)

1. **Elevação de status percebida.** Risco de futuros leitores tratarem `WORKFLOW.md` (documento de raiz, leitura obrigatória) como **norma constitutiva**, quando ele é descritivo e herda status não-normativo/decisões abertas. **Mitigação:** cabeçalho de `WORKFLOW.md` declara explicitamente o status (Anexo A §Cabeçalho); §0 e §3 desta emenda fixam "patamar de leitura ≠ autoridade normativa". Risco reduzido, não eliminado.
2. **Custo de leitura (4Es — Economicidade).** Tornar `WORKFLOW.md` leitura obrigatória de **todo** agente acrescenta tokens por sessão. **Mitigação:** o documento é síntese concisa (não verbatim); e Q3 abre a Andraus a opção de esconá-lo como **núcleo sempre-obrigatório** (igualdade plena com AGENTS.md) **ou** submetê-lo ao dial GES/EUA-E19 (núcleo vs. lista completa). Custo aceito como Eficácia superior (agente entende a orquestração antes de especificar/auditar agente operacional).
3. **Drift entre `WORKFLOW.md` e `RUNTIME-WORKFLOW-001`.** Se o insumo evoluir (v5+) e a síntese não for atualizada, divergem. **Mitigação:** `WORKFLOW.md` referencia o insumo como fonte e a v que sintetiza (v4); atualização futura do insumo dispara revisão da síntese (candidato a item de backlog / gatilho — não normatizado aqui, apenas sinalizado). Risco declarado.
4. **Coerência do whitelist em 3 pontos.** Emendar §6b.1 sem atualizar os espelhos §2/§3 geraria drift detectável por check_doc_sync. **Mitigação:** §4 lista os três pontos explicitamente.

## 7. Autopré-check de Redução de Viés (EUA-E18) — proporcional a MEDIUM `[PROPOSTA]`

> Para MEDIUM, o §7-bis é **recomendado, não bloqueante**. Executado aqui em versão proporcional (a emenda não cria BASpec com efeito de runtime; os "casos de negação" incidem sobre as próprias cláusulas da emenda).

**Bloco A — casos de negação (a emenda poderia ser satisfeita na forma e falhar na substância?):**

| # | Cláusula | Caso de negação | Detectável? Por quem? | Tratamento |
|---|---|---|---|---|
| N1 | 2.1/2.2 | `WORKFLOW.md` criado na raiz **sem** a emenda ao §6b.1 aplicada → viola HOD-001 (intake não-tratado). | Sim — determinístico (detecção §6b.5: `ls raiz \ whitelist ≠ ∅`); sensor RCH-001 passo 8. | §4 amarra a criação do arquivo à emenda simultânea do whitelist (mesma homologação). |
| N2 | 2.1/§0 | `WORKFLOW.md` promovido a **norma constitutiva** de fato (fecha decisão aberta ou cria invariante ao consolidar). | Sim — semântico; Revisor confronta o texto do Anexo A contra CONS-01/CONST-01. | Cabeçalho declara status não-normativo; marcadores `[DECISÃO NECESSÁRIA]` preservados. Fechar decisão = achado Crítico. |
| N3 | §5 | `RUNTIME-WORKFLOW-001` deletado/movido "porque agora existe o WORKFLOW.md". | Sim — INV-07; grep de existência do arquivo. | Non-goal explícito: insumo permanece; síntese é adição, não substituição. |
| N4 | 3 | `WORKFLOW.md` redefine sequência de Specs / método / config (sobreposição com ROADMAP/atomic-spec/AGENTS). | Sim — Revisor confronta escopo declarado vs. conteúdo do Anexo A. | Declaração explícita de não-sobreposição (§3); Anexo A remete às fontes de verdade. |
| N5 | 2.2 | Whitelist emendado em §6b.1 mas espelhos §2/§3 não → drift. | Sim — check_doc_sync / Revisor. | §4 lista os três pontos. |

**Bloco B — herança/conservação (CC-08 análogo):** esta emenda **herda** o whitelist homologado do HOD-001 §6b.1 e a régua RPIR/sensor RCH-001 passo 8. Evidência de conservação: nenhuma cláusula do whitelist é **removida ou enfraquecida** — a única mudança é **aditiva** (6→7 docs); RPIR, estados terminais de intake (§6b.2), conciliação INV-07×excluir (§6b.3), garantia tripla (§6b.4) e detecção determinística (§6b.5) permanecem **integralmente**. Nenhuma obrigação herdada suprimida.

**Bloco C — epistêmico (RULE-EPI/CAU/PRB/MET / CC-09):** nenhuma afirmação causal ("WORKFLOW.md garante melhor especificação"); a emenda amplia **cobertura/legibilidade**, não faz promessa de resultado. Nenhuma probabilidade/precisão numérica declarada. Nenhuma hipótese tratada como fato: o status de `WORKFLOW.md` é declarado como **descritivo/não-normativo herdado**, não como norma. A sigla "ECC" não é expandida (não aplicável aqui; nenhuma inferência sobre RULE-ECC-03 RESERVADA).

## 8. Justificativa da complexidade MEDIUM `[INFERÊNCIA]`

Classificada **MEDIUM** (não HIGH como a EUA-E23) porque: (a) é **aditiva e de organização documental**, não cria RULE normativa nova nem toca o conteúdo mínimo do Dossiê; (b) **não** envolve lentes de domínio, pesquisa web, nem fecha/abre decisão aberta; (c) **não** redefine canônico nem invariante; (d) o risco material concentra-se em **coerência documental** (whitelist em 3 pontos) e em **status percebido**, ambos mitigáveis por declaração explícita e detecção determinística. O Bloco A/B/C do §7-bis foi executado proporcionalmente por prudência (não por obrigação MEDIUM), dado que a emenda toca uma regra homologada (HOD-001).

## 9. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Criar `WORKFLOW.md` na raiz como **4º documento de leitura obrigatória**, com o conteúdo do Anexo A (síntese não-normativa da orquestração cognitiva)? | Sim |
| Q2 | **Emendar o HOD-001 §6b.1** (e espelhos §2/§3) acrescentando `WORKFLOW.md` ao whitelist de raiz? | Sim |
| Q3 | `WORKFLOW.md` é **núcleo sempre-obrigatório** (igualdade plena com AGENTS.md/ROADMAP/atomic-spec, lido em qualquer complexidade) **ou** entra no **dial GES/EUA-E19** (núcleo em HIGH/CRITICAL; reduzido em LOW/MEDIUM)? | **Núcleo sempre-obrigatório** (fiel a "pé de igualdade com AGENTS.md"); o custo é baixo (síntese concisa) — mas é decisão de Andraus. |
| Q4 | Atualizar `sincronizado-até` de ambos os agentes → DHR-EUA-E24 (a lista de leitura obrigatória muda)? | Sim |
| Q5 | Confirmar o código **EUA-E24** e o local do conteúdo (Anexo A em `governance/` até a homologação, promovido para `/WORKFLOW.md` na homologação)? | Sim |
| Q6 | O `RUNTIME-WORKFLOW-001` permanece como insumo verbatim/histórico e mantém sua obrigação RULE-ECC-06 (a síntese não o substitui)? | Sim |

## 10. Fluxo de autoridade (RULE-HG-01 / RULE-HG-08; GMC-001 Cap.5)

```
Etapa 1 — Diretiva de Andraus (chat, 2026-09-29: "criar WORKFLOW.md na raiz…" + "Emendar o HOD-001") .... ✅
Etapa 2 — Formalização (esta proposta v1 + Anexo A — NADA aplicado) ...................................... ✅ (este documento)
Etapa 3 — Parecer do Revisor (contra HOD-001 §6b.1, INV-07/09, CONS-01, CONST-01, 4Es, RULE-ECC-06) ..... ⏳
Etapa 4 — Consenso de Andraus (Q1–Q6) .................................................................. ⏳
Etapa 5 — Aplicação da §4 (criar /WORKFLOW.md a partir do Anexo A; emendar HOD-001 §6b.1/§2/§3;
          AGENTS.md §1/§2; CATALOGO; sincronizado-até; build_map.py --check) + DHR-EUA-E24 ............ ⏳
```

## 11. Evidências (âncoras)

`governance/HOD-001_Plano_Higiene_Organizacao_Documental_PROPOSTA.md` (:32 taxonomia; :60 tabela caminho-quente; :112-116 §6b.1 whitelist; :136-143 sensor/detecção) · `governance/DHR-HOD-001_Ata_Homologacao_Higiene_Documental.md` (:23-37 Q1–Q7 homologados) · `AGENTS.md` (§1 leitura obrigatória; §2 mapa do repo; §6 invariantes) · `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` (v4; §0-bis runtime cognitivo; §1-quater decisões; §2-bis E1–E8; §6 schemas) · `governance/EUA-E23_Lentes_Dominio_Dossie_Pesquisa_PROPOSTA.md` (RULE-ECC-06) · `governance/CATALOGO-OFICIAL.md` (:105-113) · `schemas/runtime-workflow.*.json` (5 schemas).

---

*Proposta registrada pelo Especificador (Claude Code, Opus 4.8), 2026-09-29. **PROPOSTA — nada aplicado**; a criação do `/WORKFLOW.md` e a emenda ao HOD-001 §6b.1 só ocorrem após parecer CONFORME do Revisor e homologação de Andraus (RULE-HG-01/03/08). INV-07 preservado (RUNTIME-WORKFLOW-001 não removido); INV-09 (não reescreve norma — apenas amplia whitelist e adiciona documento); CONS-01 (nenhuma decisão aberta fechada).*
