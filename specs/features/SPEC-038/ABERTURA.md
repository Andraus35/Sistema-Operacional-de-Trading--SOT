# Proposta de Abertura — SPEC-038: Trading Analysis Tool Harness

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05)
**Autor:** Especificador Principal SOT (Claude Code, Opus 4.8)
**Data:** 2026-10-02 · **Revisão 2026-10-03a** (saneamento ACH-MEN-01 do Revisor; fontes novas: MCP oficial do TradingView + triagem de 7 candidatos + incorporação do TUTORIAL-MCP como ref. não-normativa — instrução de Andraus 2026-10-03) · **Revisão 2026-10-03b** (decisões diretas de Andraus em `governance/DHR-DEC-003_Ata_Decisoes_SPEC038_BL.md`: SPEC-038-TVMCP-001 **DECIDIDA** — canal CDP aceito como perfil exploratório supervisionado, risco ToS assumido por Andraus; BL-031 → Absorvido; BL-032 → dona SPEC-018; ECC-VAL-001 fechada; incorporação do novo TUTORIAL-PINE como ref. não-normativa)
**Status:** **PROPOSTA DE ABERTURA — aguarda parecer do Revisor e HOMOLOGAÇÃO de Andraus** da definição da Spec. Parte das decisões abertas foi fechada por Andraus (DHR-DEC-003, 2026-10-03): ver §4/§8. NÃO é baseline; o Plan (`plan.md`/`checks.md`) **não** foi escrito e é o próximo gate só após homologação desta abertura.
**Depende de:** `research.md` (mesmo diretório — leia primeiro, incl. §4 viabilidade e `sources/_LIMITACAO-WEB.txt`).
**Autorização:** linha paralela autorizada por Andraus (chat, 2026-10-02; ROADMAP linha 32/§25), **viabilidade como critério** — origem BL-031.

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-038** | Slot do ROADMAP §17 (FASE 12); número preservado — nenhuma divisão/renumeração (RULE-ECC-01). |
| **Nome** | **Trading Analysis Tool Harness** | Idêntico ao título do slot; nenhuma capacidade nova inventada (ROADMAP §26). |
| **Complexidade** | **HIGH** | Contrato de ferramentas que alimenta Observação para todo o núcleo analítico; risco real de segurança (tool poisoning), conformidade (ToS) e não-reprodutibilidade (repaint). O slot não traz profundidade pinada no ROADMAP; comparáveis de tooling/infra = HIGH (ex.: SPEC-042/043/044). Não é CRITICAL: não redefine canônico nem decide sinal; produz Observação, não Evidência/decisão. |
| **Profundidade-alvo** | **D0–D7** (profile **standard**, AGENTS.md §4 para HIGH) | D5 (estados de uma invocação de ferramenta: REQUESTED→EXECUTED→{OK\|FAILED\|STALE}), D6 (protocolo de publicação do dado/Observação no Blackboard — por referência, M-001 aberta), D7 (cenários). D8 **não** pinado (HIGH); casos de negação relevantes (dado não-confirmado, ferramenta indisponível) entram como BASpec de falha em D7. **Não elevar em silêncio** (profiles PINADOS). |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Nasce sob o gate de maturidade normativo. |
| **Classe predominante** (orientação, não vinculante — atomic-spec §10.6) | **D (Determinístico)** para captura/validação de dado; **C (Constitutivo)** para o enforcement de proveniência/fail-closed de ferramenta de efeito | Declaração normativa é **por BASpec** no Plan (CC-11). Ver §5. |

**Natureza:** Spec de **tooling de domínio** (Trilha B) — contrato de ferramentas que servem Observação aos agentes. Não é Spec de meta-harness (≠ SPEC-046, que é tooling do próprio Especificador/Revisor).

---

## 2. Fronteira e escopo

### Dentro do escopo
- **Contrato por-ferramenta** `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas` (uma instância de contrato por ferramenta/capacidade).
- **Tipologia de ferramenta de análise:** (a) dados de mercado (OHLC, volume/order-flow); (b) indicadores/dados derivados; (c) marcação/desenho no gráfico (nível, zona); (d) replay/dados históricos. Cada tipo instancia o contrato.
- **Determinismo e proveniência como campos de primeira classe:** declarar barra **fechada/confirmada** (determinística) vs. **em formação** (não-determinística/repaint); dado não-confirmado nunca entra como fato → marcado `INDETERMINADO` (WF-C03, RULE-UNC/PRB/MET). Proveniência verificável (qual ferramenta/fonte/versão/timestamp produziu o dado) projetada sobre o vocabulário de Lineage do CEM-001 (l.712 "configuração de Skill" é interno; a ferramenta produz Observation, não Interpretation).
- **O dado de ferramenta é Observação, não Evidência** (INV-06/CEM-001 l.145/l.282/l.303) — fronteira `Fonte → Dado/Observação → (Agente) → Evidência`.
- **Falhas como contrato:** ferramenta indisponível, dado faltante/ruim, API instável, latência fora de SLA → comportamento fail-safe declarado; nenhuma fabricação (RULE-MET-01).

### Fora do escopo (Non-goals explícitos)
| Item | Motivo | Pertence a |
|---|---|---|
| *Política* de seleção/preferência/fallback/tool poisoning/resultado contraditório | É o slot vizinho | **SPEC-039** |
| Allow/deny/gates de execução de ferramenta em runtime | Guardrails | **SPEC-042** |
| Detecção de alucinação/afirmação sem fonte | | **SPEC-044** |
| Execução de ordem / qualquer efeito de mercado | **INV-05** (SOT não executa) | fora do SOT / família RISK |
| Fórmula/pesos/limiares de convicção; qualquer cálculo de Conviction Vector | **J-001/N-001 abertas**; INV-03/INV-04 | SPEC-003/CCM-001 (baselined) / backtest BL-032 |
| Backtest/calibração da J-001 (dona e protocolo) | ponte, não resolução; dona **decidida** = SPEC-018 (DHR-DEC-003 §1.2) | **SPEC-018** (via BL-032) |
| Storage físico do dado/Observação (Blackboard/KG) | **M-001/H-001 abertas** | SPEC-004/006 |
| Skills analíticas que *consomem* os dados | | SPEC-025+ |

---

## 3. Quantidade — 1 Spec vs. dividir (decisão explícita)

| Opção | Prós | Contras |
|---|---|---|
| **(A) 1 Spec unificada — ESCOLHIDA** | Um único contrato por-ferramenta cobre todos os tipos (dados/indicador/desenho/replay) com o mesmo molde; cabe em uma sessão de revisão; a governança (SPEC-039) já é slot separado, então SPEC-038 fica naturalmente enxuta (só o contrato). | Densa se a tipologia crescer — mitigado por BASpecs atômicas por tipo. |
| (B) Dividir (dados / marcação / replay) | Unidades menores | Fragmenta um único contrato; cria fronteira artificial com a governança já separada em SPEC-039; re-trabalho. |

**Decisão proposta: (A) 1 Spec.** `SPEC-038-SPLIT-001` resolvida nesta abertura (quantidade definida na abertura — RULE-ECC-01), sujeita à homologação de Andraus.

---

## 4. Veredito de viabilidade **por CANAL** (BL-031) — SPEC-038-TVMCP-001 **DECIDIDA por Andraus** (DHR-DEC-003, 2026-10-03)

Detalhe e evidência em `research.md` §4 e §4-bis. A reavaliação com fontes novas (2026-10-03) separou três canais. **Andraus decidiu** a `SPEC-038-TVMCP-001` em chat (ata `governance/DHR-DEC-003_Ata_Decisoes_SPEC038_BL.md` §1.1); o que era proposta de **rejeição** do canal CDP passou a **aceitação como PERFIL EXPLORATÓRIO supervisionado por humano** (ver abaixo e §4-bis.1). `SPEC-038-DATASRC-001` **permanece ABERTA** (`[DECISÃO NECESSÁRIA]`, CONS-01).

> **Registro histórico (INV-07 — nada apagado).** A **proposta anterior deste Dossiê** (Revisões 2026-10-02 e 2026-10-03a) era **REJEITAR a família CDP** (incl. candidata Jackson, C1/C3/C4/C6) como fonte do SOT, por non-display vedado no ToS (SRC-TOS-01), superfície CDP 9222 e injeção Pine. Essa proposta foi **SUPERADA, no ponto do veredito, por DHR-DEC-003 §1.1** — Andraus **assumiu o risco de Termos de Uso** e aceitou o canal como perfil exploratório. O conteúdo técnico-factual que a fundamentava (riscos de segurança, ToS display-only, instabilidade de API) **permanece válido e vigente como risco**; apenas o *veredito de adoção* mudou. As 6 candidatas de terceiros seguem **não adotadas** (proposta do Dossiê — tabela abaixo).

| Canal | Veredito VIGENTE | Porquê (verbatim em `sources/`) | Fonte da decisão |
|---|---|---|---|
| **(1) Família CDP** (candidata Jackson + C1 tradesdontlie, C3 bidouilles, C4 mikeh-22, C6 ertugrul59) | **ACEITO como PERFIL EXPLORATÓRIO supervisionado por humano** — **DECIDIDO (DHR-DEC-003 §1.1)**. Dado = **Observação**, nunca Evidência/baseline (INV-06), nunca ordem (INV-05; `replay_trade` proibido). Operações que alteram gráfico/conta (`draw_*`, `indicator_add`, `alert_create`, `pine_set_source`, kill do app) só com **confirmação explícita**. | CDP/scraping/automação de sessão = **non-display explicitamente vedado** (SRC-TOS-01); superfície CDP 9222 + injeção Pine (C1/Jackson); API interna instável (C4); README's admitem conflito com ToS e declinam banimento — **esses riscos permanecem reais** | **Andraus ASSUME o risco de Termos de Uso** (uso display-only; "algorithmic decision-making" vedado; suspensão de conta sem aviso). Esta abertura **não é parecer jurídico** nem afirma conformidade; o canal **não é fonte de decisão** do SOT (INV-06). Requisitos de perfil → §4-bis.1 `[PROPOSTA]` para o Plan. |
| **(2) MCP OFICIAL do TradingView** (`mcp.tradingview.com`, OAuth 2.1, Essential+) | **CANAL A REAVALIAR** quando o TradingView responder (não rejeitado, não adotado) | Remove os agravantes do CDP (sem porta de debug, API oficial documentada). Pendências: (a) **conformidade** — doc do MCP não traz termos próprios; ToS geral é display-only; INDETERMINADO se se aplica ao MCP; (b) **latência** — blog: *"market data is delayed"* → tensão com WF-K02/WF-05; (c) beta | Reavaliar à luz da **resposta do TradingView** (pergunta objetiva em `research.md` §4-bis.3) e da latência. Entrelaçado com `SPEC-038-DATASRC-001` (ABERTA). |
| **(3) Provedor de dados licenciado / determinístico** (Databento/Polygon — a avaliar; **não** C2/C5, que são dados de terceiros não-licenciados) | **ALTERNATIVA PREFERENCIAL para dado de DECISÃO** (proposta) | Dado licenciado, reprodutível, sem repaint, com entitlement (SRC-DATA-01); indicadores por biblioteca determinística própria (TA-Lib/pandas-ta — cálculo reprodutível) | `[DECISÃO NECESSÁRIA: SPEC-038-DATASRC-001]` (ABERTA), entrelaçada com BL-032 (dona = SPEC-018) |

**Separação-chave (mantida pós-decisão):** o perfil exploratório do canal (1) serve **Observação** para inspeção supervisionada; a **fonte de dado de DECISÃO** (OHLCV/indicadores que alimentam a cadeia analítica) continua **não decidida** — `SPEC-038-DATASRC-001` ABERTA, "aguardar TradingView" (DHR-DEC-003 §2). As duas não se confundem: aceitar o CDP como perfil exploratório **não** o promove a fonte de decisão.

**Triagem dos 7 candidatos (confirmação da pré-triagem de Andraus — `research.md` §4-bis.2):** as 6 candidatas de terceiros seguem **não adotadas** (proposta do Dossiê); C1,C3,C4,C6,C7 não adotadas como fonte do SOT **[CONFIRMADO]** (C1/C3/C4/C6, família CDP, ficam cobertas pelo perfil exploratório de uso pessoal supervisionado — risco ToS assumido por Andraus — mas **não** entram como componente/fonte do SOT); adiar C2 (reclassificado como provedor de dados de terceiro → entra em SPEC-038-DATASRC-001, não como "conector TradingView") **[CONFIRMADO]**; C5 **adaptar estritamente como referência de engenharia** (seu walk-forward/overfitting é insumo de **BL-032/SPEC-018**), **não** como conector/fonte do SOT **[CONFIRMADO com ajuste fino]**.

- Decisão de ferramenta-governança (seleção/fallback/tool poisoning) é **SPEC-039** — não absorver.

---

## 4-bis. Incorporação do TUTORIAL-MCP (instrução de Andraus) — fonte INTERNA NÃO-NORMATIVA

> O tutorial `reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md` é tratado como **referência interna NÃO-NORMATIVA** (`reference/externo/`, TRACE-06): nada vira baseline, não fecha `SPEC-038-DATASRC-001`, não equivale a decisão de adoção como fonte de decisão. Ele documenta a **mecânica** de um projeto LOCAL (`tradingview-mcp`, CDP) cujo código **não foi auditado** por este Especificador. Abaixo, o que o tutorial **contribui como `[PROPOSTA]`** para o futuro Plan (não para `plan.md` agora). *(O novo tutorial de Pine/backtest é tratado em §4-ter.)*

### 4-bis.1 PERFIL exploratório supervisionado por humano — **DECIDIDO (DHR-DEC-003 §1.1)**; requisitos de perfil para o Plan = `[PROPOSTA]`
Andraus decidiu aceitar o canal CDP como **perfil exploratório supervisionado por humano**, com o risco de Termos de Uso **assumido por ele**. A decisão fixa as **condições de uso** (abaixo, já DECIDIDAS pela ata); sua **materialização como requisitos verificáveis do contrato por-ferramenta** (limites, gates, campos) é `[PROPOSTA]` para o Plan — nunca `plan.md` agora.

**Condições DECIDIDAS (DHR-DEC-003 §1.1) — que o Plan materializa:**
- **Observação, nunca baseline, nunca Evidência** (INV-06 / CEM-001) — quem produz Evidência é o agente, com lineage; o canal **não é fonte de decisão** do SOT.
- **Nunca ordens** (INV-05) — proibir explicitamente `replay_trade` e qualquer geração/roteamento de ordem.
- **Operações que alteram gráfico/conta** (`draw_*`, `indicator_add`, `alert_create`, `pine_set_source`, kill do app) **só com pedido/confirmação explícitos** do humano — por padrão, **somente leitura** (gate de confirmação).
- **Barra em formação = `INDETERMINADO`**; proveniência por leitura; **fail-closed**; **saída de ferramenta = dado não-confiável** (tool poisoning).
- **Risco de Termos de Uso ASSUMIDO por Andraus** — esta abertura não afirma conformidade nem é parecer jurídico.

**Requisitos de abertura para o Plan `[PROPOSTA]` (perfil · limites · gates de confirmação):**
1. **Perfil "exploratório-supervisionado"** como atributo de primeira classe do contrato de cada ferramenta do canal CDP: `modo ∈ {somente-leitura (default), efeito-confirmado}`.
2. **Limites:** o canal CDP produz **apenas Observação** (teto de promoção: nunca sobe a Evidência sem agente+lineage); dado de barra não-fechada marcado `INDETERMINADO`; proibição dura de `replay_trade`/ordem.
3. **Gates de confirmação** (humano-no-laço) para toda ferramenta de **efeito** (`pine_set_source`, compilar/adicionar ao gráfico, `draw_*`, `indicator_add`, `alert_create`, `launch`/kill): BASpec com precondição "confirmação explícita registrada" → Classe C, fail-closed (§5).
4. **Proveniência por leitura** obrigatória (campos §4-bis.2 / §4-ter) e **rótulo de qualidade** (WF-V02).
*(A governança de seleção/quando-usar entre canais permanece SPEC-039; os guardrails de runtime dos gates, SPEC-042.)*

### 4-bis.2 Contrato mínimo (tutorial §9) → projetado no contrato por-ferramenta da SPEC-038 `[PROPOSTA]`
- **Observação ≠ Evidência** (INV-06/CEM-001): a ferramenta produz Observação; promoção a Evidência exige agente + lineage.
- **Determinismo (§9.2):** barra **em formação** = `INDETERMINADO` e **descartada** (trabalhar da penúltima barra para trás); repaint de Pine = **hipótese com timestamp + versão**, nunca fato.
- **Campos de proveniência por leitura (§9.3):** `tool`, `args`, `symbol/tf`, `captured_at_utc`, `last_closed_bar`, `indicator + versão`, `status ∈ {OK|FAILED|STALE|INDETERMINADO}`, `sha256` (opcional). Projetam-se sobre o campo **Provenance** do contrato e o Lineage do CEM-001.
- **Fail-closed (§9.4):** health check falhou / CDP fora / dado faltante ⇒ análise **para**; **nunca** completar preço de memória (RULE-MET-01).
- **Saída de ferramenta = dado não-confiável (§9.5):** tool poisoning; texto do gráfico nunca redireciona comportamento (coerente com DHR-PROV-WEB-001 §2.1; política em SPEC-039).
- **Mapeamento p/ `schemas/elliott-wave.input.json` (§9.6):** `data_get_ohlcv.time` (unix **segundos**) → **ISO-8601 UTC** (o schema exige `timestamp` `date-time`); cruzar `x1/x2` dos desenhos (índices de barra/pivô, **não** tempo) com OHLCV. **[VERIFICADO contra o schema]:** `market_digital_twin.timeframes.{S1,D1,H4,H1,M5}` são arrays `{timestamp,open,high,low,close,volume}`; `webhook_payload` traz `invalidation_level`/`fib_target_1/2` — mas obtidos por `data_get_pine_*` continuam **Observação** (não webhook). O limite "500 barras" do tutorial é do projeto **CDP local**; o MCP **oficial** permite `max 5000` — limites são **por-ferramenta**, declarados no contrato.

### 4-bis.3 Armadilhas A1–A9 (tutorial §7) → **Limitações** no contrato por-ferramenta `[PROPOSTA]`
Cada armadilha vira uma cláusula de **Limitações/Falhas** da ferramenta correspondente: A1 (blobs de `inputs` de indicador protegido estouram contexto → preferir `data_get_pine_*` com `study_filter`); A2 (`verbose` pesado); A3 (`chart_manage_indicator` falha com nome de comunidade); A4 (restauração de layout → reler `chart_get_state` antes de analisar); A5 (Pine data só p/ indicador visível); A6 (`x` do desenho ≠ tempo); A7 (LuxAlgo **repinta** → contagem = hipótese); A8 (`launch`/`tv_launch` matam o app → confirmação); **A9 (alerta `crossing` dispara no pavio, ≠ fechamento H4)** — relevante à regra "fechamento H4" do SOT.

### 4-bis.4 Catálogo de ferramentas (tutorial §5) → molde do contrato `[PROPOSTA]` (esboço; NÃO é `plan.md`)
Cada ferramenta do catálogo (`data_get_ohlcv`, `data_get_pine_*`, `chart_*`, `indicator_*`, `draw_*`, `alert_*`, `replay_*`, `capture_screenshot`, `batch_run`) será instanciada no molde `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas` **no Plan**, após homologação da abertura. Exemplo de esboço (ilustrativo, `[PROPOSTA]`): `data_get_ohlcv` → Finalidade: candles OHLCV; Determinismo: última barra = `INDETERMINADO`; Limitações: 500 barras (CDP) / 5000 (oficial); Provenance: `captured_at_utc`+`last_closed_bar`; Falhas: CDP fora ⇒ fail-closed.

### 4-bis.5 Incoerências do tutorial detectadas (verificação contra o repo — honestidade RULE-MET-01)
1. **Contagem de ferramentas:** tutorial §2 diz *"84 ferramentas"* (projeto CDP local). O MCP **oficial** reporta ~**43** (WebFetch mediado). **Nenhuma** fonte do repo declara "**78**" (o "78" da instrução de Andraus **não** foi encontrado no repositório — ver `research.md` §5 item 7). São objetos distintos (CDP local vs. oficial); número exato = **INDETERMINADO**; o 84 do tutorial é **não-auditado** (código local não revisado).
2. **"automated order generation" no ToS:** **VERIFICADO — está presente** em `sources/SRC-TOS-01` (*"...any form of automated trading, automated order generation, price referencing, order verification, algorithmic decision-making..."*). A citação do tutorial **confere**; não precisa de nova captura.
3. **ABERTURA §4 / sources referenciados pelo tutorial:** o tutorial-MCP §1 aponta para `ABERTURA.md §4`, `SRC-TOS-01`, `SRC-TVMCP-01` e o schema — todos **existem**. O tutorial-MCP §1 registra o veredito **então vigente** ("REJEITAR a candidata CDP") e o próprio marca `SPEC-038-TVMCP-001` como aberta/decisão de Andraus. **Esse veredito foi superado por DHR-DEC-003 §1.1** (canal CDP aceito como perfil exploratório, risco ToS assumido); o tutorial é referência não-normativa anterior à decisão — não há incoerência, apenas defasagem temporal esperada.
4. **Tensão central (atualizada):** o tutorial mostra o canal **já instalado localmente** (C:\Users\André\tradingview-mcp) e operado numa sessão real. Com DHR-DEC-003 §1.1, Andraus **decidiu** aceitar esse canal CDP como **perfil exploratório supervisionado** (risco ToS assumido) — porém o dado permanece **Observação, não fonte de decisão** (INV-06), e `SPEC-038-DATASRC-001` (fonte de dado de decisão) permanece **ABERTA** (CONS-01). Instalação/uso pessoal ≠ adoção como componente/fonte do SOT.

### 4-bis.6 Pergunta objetiva ao TradingView (quem envia é Andraus) — ver `research.md` §4-bis.3
Resumo: perguntar se o uso do dado via **MCP oficial** como insumo de **análise algorítmica interna** (sem execução de ordem, sem redistribuição) é permitido ou cai no veto **display-only/non-display**; se há tier com dado **em tempo real** via MCP; e se há termos específicos do MCP além dos gerais.

---

## 4-ter. Incorporação do TUTORIAL-PINE (instrução de Andraus 2026-10-03) — fonte INTERNA NÃO-NORMATIVA

> `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` é **referência interna NÃO-NORMATIVA** (`reference/externo/`, TRACE-06): documenta a **possibilidade real** de usar Pine Script no gráfico como (i) fonte de dado/ferramenta e (ii) ambiente de backtest/calibração. **Não** é entrega de calibração, **não** vira baseline, **não** escolhe dona (já decidida: **SPEC-018**, DHR-DEC-003 §1.2), **não** fecha J-001/N-001. O conteúdo é **DADO**; nenhum número dele é limiar. Baseado em execução real BTCUSDT/H4 em 2026-10-03, cujo código **não foi auditado** por este Especificador.

### 4-ter.1 Quatro "ferramentas Pine" → itens do contrato por-ferramenta da SPEC-038 `[PROPOSTA]`
O tutorial §1.1/§5 comprova que a capacidade Pine se decompõe em **quatro** ferramentas distintas, cada uma com contrato próprio `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas` (preenchimento esboçado no tutorial §5, aqui apenas referenciado — não é `plan.md`):

| Ferramenta Pine (tipo SPEC-038) | Natureza | **Classe (CC-11) [PROPOSTA]** |
|---|---|---|
| **Injetar código** no editor (`pine_set_source`) | **efeito** (sobrescreve o editor) | **C** (efeito; gate de confirmação, fail-closed) |
| **Compilar / adicionar ao gráfico** (`pine_smart_compile`/Ctrl+Enter) | **efeito** (altera o layout do usuário; pode abrir diálogo "Salvar script") | **C** (efeito; gate de confirmação) |
| **Ler métricas do Strategy Tester** (`data_get_strategy_results`) | **leitura** (Observação) | **D** (leitura; proveniência §4-ter.3) |
| **Alterar entradas do script** (`indicator_set_inputs`) | efeito leve/reversível | **D/C** (D se reversível e registrado; C se publica em estado compartilhado) |

O esboço de preenchimento Finalidade→…→Falhas do tutorial §5 entra como **`[PROPOSTA]`** de rascunho para o Plan — não substitui a redação por-BASpec (CC-11, SES-001 §50).

### 4-ter.2 Incidentes reais (tutorial §3.4) → **modos de Falhas** no contrato `[PROPOSTA]`
Cada incidente observado vira cláusula de **Falhas/Limitações** da ferramenta correspondente: (a) `pine_new` falha "Could not open Pine Editor" → precondição "abrir painel antes"; (b) `pine_smart_compile` dispara diálogo "Salvar script" (`study_added:false`) → tratar diálogo inesperado + confirmar por Ctrl+Enter; (c) `indicator_add` não acha script não-salvo → não usar essa via; (d) chaves `indicator_set_inputs` = `in_0,in_1,…` na ordem de declaração (ver §4-ter.4 sobre inferência); (e) `pine_get_console` devolve o editor inteiro (ruído/contexto) → preferir `pine_get_errors`. São **casos de teste prontos** também para a SPEC-022 (fora do escopo SPEC-038).

### 4-ter.3 Campos de proveniência de backtest (tutorial §6) → complemento do **Provenance por leitura** `[PROPOSTA]`
Para a ferramenta de **leitura** do Strategy Tester (Classe D), o Provenance do contrato recebe os campos do tutorial §6: `script_sha256`, `script_versao_pine`, `entradas {in_N}`, `simbolo/tf`, **`janela` (primeira/última barra efetivamente usadas — crítico, §4-ter.4)**, `custos`, `capital/tamanho`, `n_tentativas`, `fase ∈ {treino|teste|inteira}`, `capturado_em_utc`, `metricas`, `status ∈ {OK|FAILED|STALE|INDETERMINADO}`, `rotulo_qualidade` (WF-V02). Sem esses campos o backtest **não é reconstruível** (toca SPEC-041, por referência) e **não** sobe a Evidência (INV-06). Este é um **complemento** do Provenance já previsto em §4-bis.2 — não o substitui.

### 4-ter.4 Protocolo de calibração (tutorial §4) → **nota de encaminhamento à SPEC-018/BL-032** (FORA do escopo da SPEC-038)
O protocolo §4 (declarar baseline RULE-CTF-01; anti-hindsight; separar treino/teste; contar tentativas; DSR/PBO e estabilidade temporal fora do TradingView — WF-V01) é **calibração**, cuja **dona é a SPEC-018** (DHR-DEC-003 §1.2, ampliar SPEC-018 sob WF-V01/RULE-CTF-01). A SPEC-038 **fornece o contrato de ferramenta/dados** (incluindo a ferramenta de leitura do tester e sua proveniência); **não** executa, especifica ou valida calibração. J-001/N-001 seguem abertas. Encaminhamento declarado em §8/§9, não resolvido (CONS-01).

### 4-ter.5 Verificação do tutorial contra o repo e incoerências/inferências declaradas (honestidade RULE-MET-01)
1. **`buy_hold_return` não conferido:** o tutorial §3.4 declara explicitamente *"**não conferi** a base de cálculo do campo"* (interpretou como retorno buy&hold em USDT). **INDETERMINADO** — não usar o campo como fato; só reforça "registrar a janela".
2. **Chaves `in_2`/`in_4` inferidas:** o tutorial §3.4 confirmou `in_0`/`in_1`/`in_3` e marca `in_2` (ATR) e `in_4` (R:R) como **inferência** não confirmada. Herdar como `[INFERÊNCIA]` no esboço de contrato — não como fato.
3. **Esboço treino/teste NÃO executado:** o bloco Pine de janelas de data (tutorial §4.2) é declarado *"Esboço — não testado"*. Não tratar como mecanismo validado; pertence à SPEC-018 de todo modo.
4. **Topo corrigido 87.395,67 vs 87.278:** o tutorial §3/§8 corrige o topo da onda 5 para **87.395,67** (candles brutos H4, 21/09 20h UTC), contra **87.278** lido de indicador de terceiro no tutorial-MCP anterior. A lição ("conferir o dado bruto antes de citar") **reforça** o requisito de Determinismo/proveniência da SPEC-038; a divergência numérica entre os dois tutoriais fica **registrada**, não reconciliada artificialmente (ambos são `[EXTERNO]`/DADO, não baseline).
5. Demais mapeamentos do tutorial a Specs (017/018/022/039/040/041/042/044) são **[INFERÊNCIA]** do próprio tutorial (ele lê só o slot no ROADMAP) — não vinculam a SPEC-038.

### 4-ter.6 Tensão registrada (ToS × perfil exploratório) — honestidade
Ler as métricas do Strategy Tester por CDP é **coleta automatizada** de dado do TradingView — cai **no mesmo risco de Termos de Uso já ASSUMIDO por Andraus** no perfil exploratório (§4-bis.1 / DHR-DEC-003 §1.1). **Não se estende** esse risco assumido a "fonte de decisão": o dado do tester é **Observação de backtest exploratório**, nunca Evidência/baseline (INV-06), e a fonte de dado de decisão continua `SPEC-038-DATASRC-001` ABERTA. A tensão é **registrada**, não resolvida — e não é parecer jurídico.

---

## 5. Classe RULE-MECH-01 (CC-11) — orientação predominante

SPEC-038 citará RULE-MECH-01 no Plan → sob CC-11 (declaração por BASpec, nunca por Spec inteira — SES-001 §50).
- Captura de dado, validação de schema, hash/timestamp de proveniência, checagem barra-fechada = **Classe D (Determinístico)**.
- Enforcement de proveniência verificável e **fail-closed** em ferramenta de efeito (marcação/desenho que publica em estado compartilhado; **ferramentas Pine de efeito** — injetar código, compilar/adicionar ao gráfico, `draw_*`, `indicator_add`, `alert_create` — §4-ter.1, com **gate de confirmação** humano), impedir dado não-confirmado de entrar como fato = **Classe C (Constitutivo)**, efeito **E2/E3** (dado/marcação é commit no Blackboard; nível final por comportamento).
- Eventual normalização/juízo de qualidade de dado ("dado ruim?") = **Classe H** (gate de saída determinístico). Bounded loop + gate declarados por BASpec no Plan (RULE-MECH-03).

**Critério 4Es:** Eficácia primeiro — dado não-determinístico (repaint) ou de proveniência corrompida contamina toda a cadeia Observação→Evidência→Convicção; só depois Eficiência/Economicidade. Classe C reservada a risco alto (RULE-MECH-02).

---

## 6. Princípios de Domínio (RULE-PD-01 / CC-12) — **NÃO incide**

SPEC-038 **não** é Spec de especialidade de escola (Elliott/SMC/ICT): é harness de **ferramentas**, agnóstico de escola (serve dados a qualquer escola, não decide análise). Portanto **nenhum `PD-xx` será proposto** (determinação análoga à da SPEC-046 — tooling; e à SPEC-002 — harness neutro). A Classe (CC-11, §5) é declarada; CC-12 fica N/A por ausência de domínio de especialidade.

---

## 7. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação na abertura | Nota |
|---|---|---|
| CC-01 | OK | Ferramenta é agnóstica de escola; não altera a hierarquia Elliott→…→ICT. |
| CC-02 | OK — atenção | Não redefinir CEM-001; o dado de ferramenta é Observation/Lineage, não redefine Evidência. |
| CC-03 | OK | Não computa convicção; dimensionalidade=8 intocada; J-001 aberta. |
| CC-04 | OK | Nenhuma das 5+5 Salvaguardas violada; custo da ferramenta nunca entra em convicção (INV-04). |
| CC-05 | OK | HIGH declarado. |
| CC-06/07 | Diferido ao Plan | Engineering Cards com campos SES-001 §59 + cadeia §60. |
| CC-08 | **Aplica — foco** | Bloco Herança/Delta no Plan: INHERITS = CEM-001 (Observation/Lineage, ID+versão) + SPEC-002 (padrão de proveniência/provenance operacional) + WORKFLOW (WF-xx tocados). REMOVED vazio. Nenhum ADDED contradiz o herdado (RULE-HD-02). |
| CC-09 | **Aplica — foco** | Dado não-confirmado/faltante = `INDETERMINADO`, nunca fabricado; sem falsa precisão; latência da candidata = INDETERMINADO (não inventar). |
| CC-10 | Aplica | Declarar acepção: Observação (ferramenta/Skill) vs Evidência (agente, INV-06); "indicador/dado derivado" vs "evidência". |
| CC-11 | Aplica (§5) | Classe por BASpec no Plan; C compatível com E2/E3; D determinístico. |
| CC-12 | **NÃO incide** (§6) | SPEC-038 não é de especialidade de domínio. |

---

## 8. Dependências e decisões abertas incidentes (CONS-01 — não fechar)
- **CEM-001** (baseline) — construir SOBRE (Observation/Lineage); não redefinir (CC-02).
- **SPEC-002** (baseline) — padrão de provenance operacional reusado por referência.
- **WORKFLOW.md** (v2.1) — conformar-se; WF-xx tocados em research.md §8 (WF-02/03/05, WF-K02, WF-A01/A03, WF-C03, WF-V01/V02). **Não** fechar WF-D03.
- **SPEC-020/021** — 9 lentes + gate E3 aplicam-se; cobertura no Autopré-check do Plan. **BL-017 tool correctness** fecha por emenda à SPEC-020 **na homologação da SPEC-038**, não agora.
- **Abertas (não fechar):** J-001, N-001 (convicção/pesos); M-001 (estados Blackboard p/ Observação); H-001 (KG). **`SPEC-038-DATASRC-001` permanece ABERTA** ("aguardar TradingView" — DHR-DEC-003 §2).
- **BL-032 (dona do backtest/calibração) — DECIDIDA (DHR-DEC-003 §1.2): dona = SPEC-018** (ampliar o ciclo Extração→…→Aprovação com backtest/calibração sob WF-V01 e RULE-CTF-01; gatilho `spec:SPEC-018 em redação` preservado; não cria slot novo). A SPEC-038 é **pré-requisito instrumental** (fornece contrato de ferramenta/dados), **não** a dona — ponte em §7 de `research.md`. J-001/N-001 seguem abertas (valores definitivos pós-backtest).
- **`SPEC-038-TVMCP-001` — DECIDIDA (DHR-DEC-003 §1.1):** canal CDP **ACEITO como perfil exploratório supervisionado** (risco ToS assumido por Andraus; dado = Observação, nunca Evidência/ordem; efeitos só com confirmação — §4/§4-bis.1); MCP oficial = canal a reavaliar quando o TradingView responder; 6 candidatas de terceiros não adotadas. **Não é mais `[DECISÃO NECESSÁRIA]`** quanto ao veredito; os requisitos de perfil para o Plan são `[PROPOSTA]` (§4-bis.1).
- **`[DECISÃO NECESSÁRIA: SPEC-038-DATASRC-001]` (ABERTA)** — fonte de dados de **decisão** (OHLCV/indicadores que alimentam a cadeia analítica) é de **Andraus**, "aguardar TradingView" (DHR-DEC-003 §2), entrelaçada com BL-032/SPEC-018. Opções: provedor licenciado (Databento/Polygon) vs. MCP oficial vs. export manual vs. ambos. C2 (tradingviewapi) entra aqui como provedor de terceiro a avaliar, **não** como conector TradingView. **Não confundir** com o perfil exploratório do CDP (que é Observação, não fonte de decisão).
- **`[DECISÃO NECESSÁRIA: promover BL-017 a ATIVADO]`** — o detector de gatilhos aponta BL-017 (`tool correctness ↔ SPEC-038`) como **disparado sem registro**; a promoção a `ATIVADO` é **de Andraus** — o Especificador **não** promove (CONS-01). Encaminhamento ao gate permanece: fechar a dimensão B por emenda à SPEC-020 **na homologação da SPEC-038**, não agora.
- **Fontes novas desta revisão (2026-10-03):** `sources/SRC-TVMCP-OFFICIAL-01-*.txt`, `sources/SRC-CANDIDATES-01-triagem-7.txt`, `sources/SRC-WORKFLOW-01-*.txt` (saneamento ACH-MEN-01).

---

## 9. Itens RMR-001 — estado pós-DHR-DEC-003 (Controlador já registrou; aqui só o reflexo na abertura)
- **BL-031** → **Absorvido** (DHR-DEC-003 §1.1: *"BL-031 → Absorvido"*, encaminhado à SPEC-038). A viabilidade TradingView↔SOT foi tratada por este Dossiê (§4) e a decisão de canal tomada por Andraus. Origem desta linha paralela.
- **BL-017** (`tool correctness ↔ SPEC-038`) → **`[DECISÃO NECESSÁRIA: promover a ATIVADO]`**. O detector de gatilhos (`scripts/backlog_triggers.py`) o reporta **disparado sem registro**; a promoção a `ATIVADO` é **de Andraus**, não do Especificador (CONS-01). Encaminhamento quando promovido: fechar a dimensão B (tool correctness) por emenda pontual à SPEC-020 **na homologação da SPEC-038** — não agora.
- **BL-032** → **DECIDIDA: dona = SPEC-018** (DHR-DEC-003 §1.2); não dispara aqui (gatilho `spec:SPEC-018 em redação`) — só ponte de rastreabilidade (§7 de `research.md`).
- **BL-026** **não** dispara (gatilho diferente) — só rastreabilidade.

---

## 10. Riscos
- **R-1 (conformidade — risco ASSUMIDO):** automatizar dados do TradingView (CDP, e eventualmente ler o Strategy Tester — §4-ter.6) cai no uso **non-display/algorithmic decision-making** vedado pelo ToS → risco de suspensão de conta sem aviso. **Andraus ASSUMIU este risco (DHR-DEC-003 §1.1)** para o perfil exploratório supervisionado; esta abertura **não afirma conformidade nem é parecer jurídico**. Contenção: dado = Observação (nunca fonte de decisão/Evidência/ordem), somente-leitura por padrão, efeitos só com confirmação. A fonte de dado de **decisão** (DATASRC-001, ABERTA) busca canal lícito (§4 canal 3 / MCP oficial).
- **R-2 (segurança):** ferramentas externas/MCP sujeitas a tool poisoning (36,5% de sucesso médio; Claude 34%) — o contrato deve tratar saída de ferramenta como dado não-confiável; *política* em SPEC-039.
- **R-3 (determinismo):** >95% dos indicadores repintam — dado não-confirmado como fato invalida a cadeia; mitigado pelo campo Determinismo obrigatório.
- **R-4 (escopo):** absorver governança (SPEC-039) ou calibração (BL-032) — mitigado pelas fronteiras §2/§6.3 do Dossiê.

---

## 11. Edições a documentos de governança — **já executadas por Andraus/Controlador** (DHR-DEC-003 §3)
*(O Especificador não edita ROADMAP/CATALOGO/RMR-001/agentes; registra o estado — AGENTS.md §5.)*
As decisões de DHR-DEC-003 já tiveram registros consequentes aplicados (fora do escopo desta edição): `backlog/RMR-001` (estados/donas de BL-002/012/027/028/029/030/031/032), `ROADMAP.md` (linhas de decisões), `AGENTS.md §7`, `atomic-spec.md §15` e `governance/RULES.md` (ECC-VAL-001). Nenhum modelo canônico baseline tocado (CONST-01). **Pendência de Andraus ainda aberta:** promover **BL-017** a `ATIVADO` (detector reporta disparado sem registro — §8/§9; não executado pelo Especificador). Nenhuma edição em Specs baselined (sem erratum necessário — research.md §6.4; INV-09).

---

## 12. Próximo passo
Com `SPEC-038-TVMCP-001`, `BL-031` e `BL-032` já **decididos por Andraus** (DHR-DEC-003), esta Proposta + `research.md` + `sources/` seguem para **parecer do Revisor** sobre o processo do Dossiê (atomic-spec §15; RULE-ECC-04 verbatim; RULE-ECC-05 3 lentes; ECC-VAL-001 validade declarada em `research.md`) e, em seguida, **homologação de Andraus** da **definição da Spec** (número, nome, fronteira HIGH/D0–D7, quantidade=1, Classe, não-incidência de CC-12). Resta aberta a `[DECISÃO NECESSÁRIA: SPEC-038-DATASRC-001]` (fonte de dado de decisão — "aguardar TradingView") e a pendência de promover BL-017 — **antes** de qualquer `plan.md`/`checks.md`.

**Pronto para revisão.**

---

## 13. Adendo pós-homologação (DHR-DEC-004, 2026-10-03 — aditivo, INV-07)

- **`SPEC-038-DATASRC-001` DECIDIDA neste recorte por Andraus:** TradingView (perfil exploratório CDP, risco ToS assumido) entra como **uma das fontes**, via adapter, **nunca como fonte única da verdade**; o **provedor de dados de máquina** (order flow/futuros/BTC multi-exchange) **não é escolhido** e depende do Discovery/benchmark do MASTER (`reference/externo/MASTER — MARKET DATA, ORDER FLOW E INTEGRAÇÃO TRADINGVIEW.MD`, ref. externa NÃO-normativa) → **BL-033**. Dado de qualquer fonte = Observação (INV-06; Provider ≠ Evidence).
- **BL-017 → ATIVADO:** a dimensão B 'tool correctness' só fecha por emenda à SPEC-020 na homologação da SPEC-038.
- A SPEC-038 permanece restrita ao **contrato de ferramenta**; Market Data & Order Flow (provider abstrato, Order Flow Engine, D-001..D-027) é capacidade candidata fora desta Spec. O Plan deve prever o `TradingViewAdapter` como adapter de uma fonte, sem acoplar o contrato ao TradingView.
- Este adendo não reescreve a abertura homologada (DHR-SPEC038-001); a definição homologada permanece inalterada.
