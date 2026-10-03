# Dossiê de Pesquisa — SPEC-038: Trading Analysis Tool Harness

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-SPEC-038 |
| **Método** | ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05) |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 4.8) |
| **Data de acesso web** | 2026-10-02 (fontes originais `[EXTERNO]`) · 2026-10-03 (fontes novas: MCP oficial, 7 candidatos) |
| **Validade do Dossiê (ECC-VAL-001 — FECHADA, DHR-DEC-003 §1.9)** | Complexidade **HIGH** → **90 dias** da data de acesso das fontes, **ou antes** se o contexto mudar materialmente (nova versão de fonte/ToS/decisão sobre o objeto). **Data-limite deste Dossiê = 2026-12-31** (90 dias a partir de 2026-10-02, a data de acesso mais antiga; as fontes de 2026-10-03 expiram em 2027-01-01 — adota-se a mais conservadora). Dossiê vencido **não** dispensa a Spec de reabrir pesquisa (fail-closed, RULE-ECC-02). *Gatilho de reabertura antecipada já ativo:* resposta do TradingView sobre uso não-display/latência via MCP (§4-bis.3) muda o contexto materialmente. |
| **Natureza** | **Dossiê de Pesquisa `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão (CONS-01). |
| **Status epistemológico** | Conteúdo web = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02). Toda fonte etiquetada `[EXTERNO]` e classificada. A veracidade das páginas **não** é atestada. Capturas verbatim em `sources/` com limitação declarada em `sources/_LIMITACAO-WEB.txt`. |
| **Autorização** | Linha paralela autorizada por Andraus (chat, 2026-10-02; ROADMAP linha 32/§25), **viabilidade como critério** — origem BL-031. |
| **Fronteiras respeitadas** | INV-05/INV-09 (SOT não executa ordem; sem baseline informal); INV-06/INV-10 (Evidência≠Observação; ferramenta/Skill produz Observação, não Evidência — CEM-001 l.145/l.282/l.303); INV-01/INV-02 (hierarquia; ICT não cria hipótese). Governança de seleção/fallback/tool poisoning = SPEC-039 (não absorver); guardrails runtime = SPEC-042; detecção de alucinação = SPEC-044. |

> **Aviso de método (RULE-MET-01 — sem bajulação).** A candidata `tradingview-mcp-jackson` foi trazida por Andraus como pergunta de viabilidade, não como solução a ratificar. Este Dossiê reporta um **achado de conformidade grave** (Termos de Uso do TradingView) que o README da ferramenta reconhece e transfere ao usuário. Popularidade/conveniência da ferramenta foi separada da sua licitude e do seu determinismo.

> **Decisão superveniente (DHR-DEC-003, 2026-10-03) — registrada para consistência com `ABERTURA.md`.** Andraus **decidiu** a `SPEC-038-TVMCP-001`: **aceitar o canal CDP (família `tradingview-mcp`) como PERFIL EXPLORATÓRIO supervisionado por humano, assumindo o risco de Termos de Uso**. A **proposta deste Dossiê era REJEITAR** a família CDP como fonte do SOT (§3.4/§4) — essa proposta foi **superada no veredito** por DHR-DEC-003 §1.1 (INV-07: o texto do Dossiê é preservado como registro histórico; apenas o veredito de adoção mudou). **O achado de conformidade (ToS display-only/non-display) permanece factualmente válido e é o risco que Andraus assumiu** — este Dossiê não afirma conformidade nem é parecer jurídico, e o canal **não** é fonte de decisão do SOT (dado = Observação, INV-06). `SPEC-038-DATASRC-001` (fonte de dado de decisão) **permanece ABERTA** — "aguardar TradingView".

---

## 1. Questões e estratégia de busca

**Questões de pesquisa (derivadas de BL-031 + do título do slot ROADMAP §17):**
- Q1. O que o estado da arte define como **contrato de ferramenta** de análise (Finalidade/Input/Output/Precisão/Determinismo/Limitações/Custo/Latência/Provenance/Falhas)?
- Q2. Quais os riscos de **segurança de ferramentas** (MCP tool poisoning) que um harness de ferramentas deve enfrentar por contrato?
- Q3. A candidata `tradingview-mcp-jackson` é **viável** como conexão governada TradingView↔SOT, pelos 8 critérios do BL-031?
- Q4. Que **alternativas de fonte/ferramenta** existem (dados licenciados, bibliotecas determinísticas, export) para a recomendação não ser binária?
- Q5. Como o **determinismo/proveniência** de OHLC/indicadores condiciona a confiabilidade da Observação que alimenta os agentes?
- Q6. Como o slot se **conforma ao WORKFLOW.md** (quais `WF-xx` toca) e onde fica a fronteira com SPEC-039/042/044?

**Estratégia de busca:** WebSearch para mapear o campo (MCP TradingView, tool poisoning, ToS, repainting, provedores de dados); WebFetch para (a) auditar estaticamente o repositório da candidata (raw/README, SEM instalar/executar — BL-031 item 1) e (b) capturar verbatim os termos do TradingView. Fontes classificadas e etiquetadas `[EXTERNO]`; capturas em `sources/SRC-*.txt` (RULE-ECC-04).

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Papel |
|---|---|---|---|
| SRC-TVMCP-01 | github.com/LewisWJackson/tradingview-mcp-jackson (README/código) | **Prática** (impl. de terceiro, não-auditada formalmente) | Auditoria estática da candidata (BL-031 1,3,4,5,6) |
| SRC-TOS-01 | tradingview.com/policies (Termos de Uso) | **Padrão** (termo contratual) | Conformidade/banimento (BL-031 item 2) |
| SRC-MCPTOX-01 | practical-devsecops.com/mcp-tool-poisoning + arXiv 2508.14925 (MCPTox) | **Evidência/Benchmark** + Prática | Segurança de ferramenta (Q2; fronteira SPEC-039) |
| SRC-REPAINT-01 | crosstrade.io + PineCoders FAQ (TradingView) | **Prática** (doc técnica) | Determinismo/repainting (Q5; BL-031 item 8) |
| SRC-DATA-01 | edgeful.com + databento.com | **Prática/Benchmark** (+ viés comercial do fornecedor) | Alternativas de dados (Q4) |
| SRC-TVMCP-OFFICIAL-01 | tradingview.com/mcp/docs + blog de lançamento | **Padrão/Prática** (produto oficial do provedor, em beta) | Canal MCP OFICIAL (§4-bis; reavaliação BL-031) — acesso 2026-10-03 |
| SRC-CANDIDATES-01 | 7 repositórios/serviços de terceiros (ver captura) | **Prática** (impl. de terceiros, não-auditadas) | Triagem dos 7 candidatos (§4-bis) — acesso 2026-10-03 |
| SRC-WORKFLOW-01 | PESQUISA-WORKFLOW B.7 (repo) → nexusfi/mbrenndoerfer | **Prática/Engenharia** (2ª ordem via doc do repo) | Saneamento ACH-MEN-01 (§3.1) |

Fontes de apoio já no repositório (NÃO re-pesquisadas, `[EXTERNO]` prévio): `reference/PESQUISA-WORKFLOW-TRADING-2026-10-01.md` B.7 (pipeline market data→signal→risk→execution, máquina de estados determinística — Forte), B.10 (walk-forward+DSR/PBO — Forte), B.5 (order flow dependente de dados por ativo — Moderada). Reutilizadas por referência, não recontadas (economicidade).

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

### 3.1 Contrato de ferramenta (Q1) — **ADOTAR** (reforça o título do slot)
O slot ROADMAP §17 já exige o contrato `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas`. O estado da arte de arquitetura de sistemas de trading confirma o princípio: *"market data → signal → risk → order management → execution, fluxo unidirecional, cada componente com uma só função"* e *"O núcleo do Order Management é uma máquina de estados determinística; sem ela, edge-cases criam "posições fantasma""* [EXTERNO, Forte — PESQUISA-WORKFLOW B.7; captura verbatim em `sources/SRC-WORKFLOW-01-pipeline-state-machine.txt` (RULE-ECC-04); captura de 2ª ordem a partir do doc de pesquisa do repo — URLs últimas nexusfi/mbrenndoerfer NÃO re-fetchadas; as aspas internas em "posições fantasma" são parte do texto-fonte]. **Adotar** o contrato por-ferramenta como o núcleo da SPEC-038, alinhado a INV-06/INV-10: a ferramenta produz **Observação/dado bruto** (OHLC, volume, desenho, valor de indicador), **nunca Evidência** — a Evidência é interpretação de Agente (CEM-001 l.145 "observação interpretada por um agente especializado"; l.282 `PRIMARY` só para `AGENT`; l.308 Interpretation = do agente).

### 3.2 Segurança de ferramenta / tool poisoning (Q2) — **ADOTAR como requisito de contrato; governança ADIAR a SPEC-039**
*"MCP tool poisoning ... adversarial content is embedded in tool names, descriptions, or input schemas such that an LLM-based agent is deceived into executing attacker-controlled actions"* e *"no cryptographic signing of tool manifests. The MCP specification has no standard mechanism for verifying that the tool description returned at runtime matches what was audited at install time"* [EXTERNO, Evidência — SRC-MCPTOX-01]. Taxa de sucesso média de 36,5% dos ataques; Claude 3.7 Sonnet ainda obedeceu descrições envenenadas em 34% dos casos [EXTERNO, Benchmark MCPTox]. **Implicação SOT:** o contrato de ferramenta DEVE tratar a saída de ferramenta externa como **dado não-confiável** (o conteúdo nunca redireciona o comportamento — mesmo princípio DHR-PROV-WEB-001 §2.1), declarar **proveniência verificável** e **fail-closed** em ferramenta de efeito. **Adotar** no contrato os campos Provenance/Falhas com essa carga; **adiar** à SPEC-039 a *política* de seleção/allowlist/pinning/fallback/resultado-contraditório (é literalmente o escopo do slot SPEC-039 — ROADMAP §17). Fronteira registrada em §6.

### 3.3 Determinismo e proveniência de dados/indicadores (Q5) — **ADOTAR o campo Determinismo com carga forte**
*"Script behavior causing historical vs. realtime calculations or plots to behave differently"* e *"Over 95% of indicators (even standard ones like RSI, MACD) technically repaint because live values aren't finalized until the bar closes"* [EXTERNO, Prática — SRC-REPAINT-01]. Correlato de dados: *"gaps in time-series data which disrupt indicator calculations and invalidate backtests, and inconsistent timestamp alignment leading to look-ahead bias"* [EXTERNO — SRC-DATA-01]. **Implicação SOT:** o campo **Determinismo** do contrato não é cosmético — uma ferramenta que retorna valor de barra **não-confirmada** (repaint) produz Observação não-reprodutível, contaminando a cadeia Observação→Evidência→Hipótese→Convicção. **Adotar:** toda ferramenta DEVE declarar se opera sobre barra **fechada/confirmada** (determinística) ou **em formação** (não-determinística), e marcar o dado accordingly; valor não-confirmado nunca entra como fato (coerente com WF-C03 `INDETERMINADO`, RULE-UNC/PRB/MET). Isto também sustenta o requisito herdado WF-V01 (walk-forward+DSR/PBO) e RULE-CTF-01 (anti-hindsight) para o replay.

### 3.4 Candidata `tradingview-mcp-jackson` (Q3) — ver §4 (núcleo do pedido). **Veredito PROPOSTO (histórico): REJEITAR como conexão automatizada direta ao TradingView.** → **SUPERADO no veredito por DHR-DEC-003 §1.1:** Andraus aceitou o canal CDP como **perfil exploratório supervisionado** (risco ToS assumido). Os achados técnicos/de conformidade abaixo permanecem válidos como risco; o canal **não** é fonte de decisão (Observação, INV-06).

### 3.5 Alternativas de fonte (Q4) — **ADAPTAR: preferir fonte de dados licenciada/determinística; manter recomendação não-binária**
*"Databento is a licensed distributor and direct provider of market data for 50+ trading venues"*; *"licensed API providers more reliable for reproducible research and production systems"* vs. scraping que exige manter infraestrutura própria [EXTERNO, Prática + viés comercial — SRC-DATA-01]. **Implicação SOT:** a necessidade real do SOT (OHLC/volume por ativo BTC/XAU/NASDAQ, determinístico, reprodutível, licenciado) é melhor servida por **provedor de dados licenciado** (ex.: Databento/Polygon — a avaliar, não adotados) e **bibliotecas de indicadores determinísticas** (ex.: TA-Lib/pandas-ta — cálculo próprio reprodutível, sem repaint), com **export manual/CSV** do TradingView como canal lícito de baixa frequência. Nenhum produto é adotado aqui — é insumo para a decisão de Andraus.

---

## 4. Avaliação de viabilidade da candidata `tradingview-mcp-jackson` (BL-031 — 8 critérios)

> Auditoria **estática** de texto (README/listagem de ferramentas via WebFetch); **nada instalado ou executado** (mandato BL-031 item 1). [EXTERNO — SRC-TVMCP-01], salvo onde indicado.

| # | Critério BL-031 | Achado | Severidade |
|---|---|---|---|
| 1 | **Auditoria de código (injeção de Pine; porta CDP 9222)** | Conecta via **Chrome DevTools Protocol em localhost:9222** — porta de debug que, se exposta/sem bind local estrito, dá controle do browser a qualquer processo local; superfície de ataque real. `pine_set_source` **injeta Pine arbitrário** no editor e compila server-side — capacidade de execução de script no contexto da conta. | **Alta** |
| 2 | **Termos de Uso / risco de banimento** | **BLOQUEADOR.** ToS TradingView: dados *"licensed for exclusive display-only use"*; proíbe *"algorithmic decision-making, algorithmic trading"* e a *"development, offering, or utilization of any third-party products, tools, or services designed to facilitate ... non-display usage"*; defesa de "non-usage" por terceiro *"declared null and void"*; suspensão *"without prior notice"* [EXTERNO — SRC-TOS-01]. O próprio README transfere o risco: *"The authors are not responsible for any account bans, suspensions"* [SRC-TVMCP-01]. Usar a candidata para alimentar análise algorítmica do SOT é **uso não-display vedado**. | **Crítica (conformidade)** |
| 3 | **Estabilidade de APIs não documentadas** | README admite: *"accesses undocumented internal TradingView APIs that may change at any time"* [SRC-TVMCP-01]. Sem contrato de estabilidade → quebra silenciosa, Observação não-reprodutível. | **Alta** |
| 4 | **Latência/limites de quote_get/data_get_ohlcv/stream** | *"None stated"* na documentação [SRC-TVMCP-01] → **INDETERMINADO** (não inventar — atomic-spec §15). Relevante ao relógio do Manager (WF-K02, pré-aviso 1h): sem SLA de latência, não há garantia de que o dado chega a tempo da Killzone. | **INDETERMINADO** (não mensurável no repo) |
| 5 | **Tipos de desenho × necessidade** | Oferece `horizontal_line, trend_line, rectangle, text`; **sem Fibonacci, sem Elliott, sem remoção** [SRC-TVMCP-01]. Necessidade SOT: marcar invalidação (horizontal ✓), alvos (horizontal ✓), zonas OTE/retração Fibonacci (**✗ não há primitiva**), ondas Elliott (**✗**). Ausência de remoção impede higiene de marcações obsoletas (conflita com ciclo de vida do alarme WF-A03). | **Média** (cobre o mínimo; falha no específico Elliott/Fib/OTE) |
| 6 | **Leitura de desenhos manuais** | Só lê desenhos **de Pine** (`data_get_pine_lines/labels/boxes`); desenhos manuais do usuário não feitos via Pine não são garantidamente legíveis [SRC-TVMCP-01]. | Média |
| 7 | **Cobertura BTC/XAU/NASDAQ e assinatura paga** | Requer *"a valid TradingView subscription"* e não burla paywall [SRC-TVMCP-01]; cobertura dos três ativos depende do plano do usuário — **não verificável estaticamente** → INDETERMINADO quanto a limites por plano. | INDETERMINADO |
| 8 | **Replay (anti-hindsight) × limites p/ calibração** | Oferece `replay_*` (replay mode). Útil para inspeção visual, mas **não** substitui backtest governado: sem walk-forward/DSR/PBO (WF-V01) e sujeito a repaint (SRC-REPAINT-01) → replay manual contamina com conhecimento do passado (RULE-CTF-01 anti-hindsight). Calibração da J-001 é de **BL-032** (dona a definir), não desta ferramenta. | Média (não serve para calibração) |

**Síntese da viabilidade (PROPOSTA histórica — SUPERADA no veredito por DHR-DEC-003 §1.1; achados factuais preservados, INV-07):**
- O **achado central é o critério 2 (Termos de Uso)**: alimentar a análise algorítmica do SOT com dados do TradingView via automação CDP é **uso não-display explicitamente vedado**, com risco de banimento que o próprio autor declina. Isto é independente da qualidade técnica da ferramenta e **permanece factualmente verdadeiro**.
- Os critérios 1 e 3 adicionam risco de **segurança** (porta CDP, injeção de Pine) e de **não-reprodutibilidade** (APIs internas instáveis).
- **Veredito PROPOSTO originalmente: REJEITAR** a `tradingview-mcp-jackson` como conexão automatizada direta ao TradingView para o SOT. **→ DECISÃO DE ANDRAUS (DHR-DEC-003 §1.1): ACEITAR como perfil exploratório supervisionado por humano, assumindo o risco de ToS** — dado = Observação, nunca Evidência/baseline/ordem; efeitos só com confirmação; **não** é fonte de decisão do SOT. Para a fonte de dado de **decisão**, o Dossiê mantém a preferência por canal lícito: (a) **dados** de provedor licenciado determinístico (§3.5); (b) MCP oficial, a reavaliar pós-resposta do TradingView (§4-bis.1); (c) export CSV manual — escopo de `SPEC-038-DATASRC-001` (ABERTA).

---

## 4-bis. Reavaliação por CANAL com fontes novas (2026-10-03) — MCP oficial + 7 candidatos

> Autorização: Andraus (chat, 2026-10-03) pediu (1) reavaliar compatibilidade TradingView↔SOT com fontes novas e (2) triar 7 candidatos. Auditoria **estática** (páginas/README via WebFetch, mediado por modelo); **nada instalado/executado** (BL-031 item 1). Capturas: `sources/SRC-TVMCP-OFFICIAL-01-*.txt` e `sources/SRC-CANDIDATES-01-triagem-7.txt`. O veredito permanece **PROPOSTA/`[DECISÃO NECESSÁRIA]`** — nada vira baseline (CONS-01, TRACE-06).

### 4-bis.1 Canal NOVO — MCP **OFICIAL** do TradingView (operado pelo próprio TradingView) — reavaliação BL-031

Fato relevante que muda o quadro desde o Dossiê de 2026-10-02: existe um servidor MCP **oficial** do TradingView (`https://mcp.tradingview.com/mcp`, OAuth 2.1, plano Essential+). Isto é categoricamente diferente da candidata original (CDP/Jackson), que é de terceiro e usa APIs internas. Confirmação verbatim em `SRC-TVMCP-OFFICIAL-01`.

| # | Critério BL-031 | Achado (canal MCP oficial) | Severidade |
|---|---|---|---|
| 1 | Auditoria de código / superfície de ataque | Não há binário de terceiro nem porta CDP: é serviço remoto oficial com OAuth 2.1 (*"you sign in with your TradingView account, no API keys to manage"*). Some a superfície CDP/injeção-Pine da candidata original. Resta a superfície MCP genérica (tool poisoning) — tratada por contrato (§3.2) e política SPEC-039. | **Baixa** (vs. Alta da candidata CDP) |
| 2 | **Termos de Uso / banimento** | **INDETERMINADO — ponto central.** A doc do MCP **não traz termos próprios**; os Termos gerais do TradingView (SRC-TOS-01) licenciam dados para *"exclusive display-only use"* e vedam *"algorithmic decision-making"* / *"non-display usage"*. NÃO foi observada exceção ao ToS geral para uso via MCP. Se o dado do MCP herda o ToS display-only, alimentar análise algorítmica do SOT permanece em tensão — **mas** é um canal **oficial e sancionado pelo provedor**, o que muda o risco de "banimento por ToS" (vs. o CDP, explicitamente non-display). **Não decidir — perguntar ao TradingView** (§4-bis.3). | **INDETERMINADO (conformidade)** — não é o BLOQUEADOR categórico da candidata CDP |
| 3 | Estabilidade de API | API **oficial e documentada** (vs. "undocumented internal APIs" da candidata). Melhora substancial de reprodutibilidade. Ressalva: *"TradingView MCP Server is in beta"* → superfície/contrato podem mudar. | Média (beta) |
| 4 | **Latência / limites** | *"Tool calls are rate-limited to ~100 requests per minute per user"*; OHLCV *"max 5000"* barras (default 300); na beta *"we may limit the number of requests per day"*. **E o bloqueador funcional:** o blog diz ***"market data is delayed"***. Dado **atrasado** compromete o relógio do Manager (WF-K02: pré-aviso 1h antes da Killzone) e a Ativação (WF-05). | **Alta (funcional)** — dado atrasado pode não servir para timing |
| 5 | Tipos de desenho × necessidade | **Sem ferramenta de desenho** na doc. Não marca invalidação/alvos/Fibonacci no gráfico. (A análise do SOT não exige desenhar no gráfico do usuário — marcar é conveniência; INV-05 proíbe ordem, não exige desenho.) Alertas: só *"simple price condition"*; *"Multi-condition and indicator-based (study) alerts are NOT supported yet"* → não cobre alarme-gatilho multi-condição (WF-A0x). | Média |
| 6 | Leitura de desenhos/indicadores | Oferece screener/technicals-rating/fundamentals/news/calendars, **não** leitura de desenhos de Pine (LuxAlgo etc.) do gráfico do usuário. Para "ler o que o indicador desenhou", o MCP oficial **não** substitui o CDP. | Média (cobertura diferente) |
| 7 | Cobertura BTC/XAU/NASDAQ e plano | Ativos: *"Stocks, ETFs, bonds, forex, indices, futures, crypto"* (cobre os três). Requer Essential+; *"trial plans don't include MCP access"*. | OK (sujeito a plano) |
| 8 | Replay/anti-hindsight p/ calibração | Doc não expõe replay/backtest governado; histórico limitado a 5000 barras/req. Não substitui backtest com walk-forward/DSR/PBO (WF-V01). Calibração = BL-032. | Média (não serve p/ calibração) |

**Síntese canal oficial (PROPOSTA):** o MCP oficial **remove** os dois agravantes mais graves do canal CDP (superfície CDP/injeção-Pine; APIs internas instáveis) e **transforma** o achado de conformidade. O que no CDP é "non-display explicitamente vedado + banimento sem aviso" (risco **assumido** por Andraus no perfil exploratório — DHR-DEC-003 §1.1) passa, no canal oficial, a **duas incógnitas**: (a) o ToS display-only vale para o dado entregue via MCP oficial? (b) o dado atrasado (*"market data is delayed"*) chega a tempo do relógio do Manager? Ambas = `[DECISÃO NECESSÁRIA]`, não resolvidas aqui. **Veredito proposto: canal a REAVALIAR** (não adotado, não rejeitado) — condicionado à resposta do TradingView sobre uso não-display via MCP (§4-bis.3) e à latência vs. WF-K02/WF-05. Entrelaçado com `SPEC-038-DATASRC-001` (ABERTA), que é onde a fonte de dado de **decisão** será decidida.

### 4-bis.2 Triagem dos 7 candidatos (BL-031 — estática, [EXTERNO], verbatim em SRC-CANDIDATES-01)

| # | Candidato | Mecanismo / proveniência | ToS / risco | Veredito PROPOSTO |
|---|---|---|---|---|
| C1 | tradesdontlie/tradingview-mcp | CDP (porta 9222), injeção possível via DevTools | README admite: ToS *"restrict automated data collection, scraping, and non-display usage"*; *"may conflict with those terms"*; *"not responsible for any account bans"* | **REJEITAR** — mesma família CDP da candidata original; mesmo bloqueador non-display + superfície CDP (crítica 1/2) |
| C2 | tradingviewapi.com/mcp (+ /terms/) | Terceiro *"Unofficial… Not affiliated"*; proveniência do dado **NÃO declarada** (só "353+ exchanges") | /terms permite uso comercial e display/cache/forward, MAS *"not affiliated with… TradingView"* e *"We do not provide written indemnification…"*; não é dado do TradingView licenciado | **ADIAR** — é um provedor de dados de terceiro (não TradingView); proveniência indeterminada impede confiar como fonte de decisão; avaliar junto de SPEC-038-DATASRC-001/provedores licenciados |
| C3 | bidouilles/mcp-tradingview-server | Scraping via `tradingview_scraper`; *"for educational and research purposes"* | Scraping de dado do TradingView → non-display/scraping vedado (SRC-TOS-01); licença educacional ≠ uso em produção | **REJEITAR** — scraping (non-display) + licença não-produção |
| C4 | mikeh-22/tradingview-mcp | Login **automatizado** Playwright com usuário/senha; cookies em disco; *"internal, undocumented web API"* | Automação de sessão + credenciais em env + API interna; *"not affiliated"*; endpoints *"may change without notice"* | **REJEITAR** — automação de login (credenciais), API interna instável, non-display; pior perfil de segurança |
| C5 | atilaahmettaner/tradingview-mcp | `tradingview-ta`/screener + Yahoo/Reddit/RSS; **SEM login no TV**; *"does not log into, scrape, or automate a TradingView session"*; backtest 9 estratégias + walk-forward | *"You are responsible for ensuring your own use complies with the terms of any data source"* — mas não automatiza sessão TV | **ADAPTAR só como referência de engenharia** (não fonte de dado do SOT): o módulo de walk-forward/overfitting é insumo de engenharia para **BL-032** (calibração). O dado Yahoo/Reddit/RSS não é fonte licenciada de decisão. Não adotar como conector. |
| C6 | ertugrul59/tradingview-chart-mcp | Selenium + cookies de sessão pessoais; devolve **imagem** (snapshot) | Sem disclaimer de ToS no README; exige credenciais de sessão → uso direto da conta; scraping de imagem | **REJEITAR** — scraping via sessão pessoal (non-display), devolve só imagem; sem contrato de dado |
| C7 | fiale-plus/tradingview-mcp-server | Cliente **não-oficial** de *"public scanner and symbol-search endpoints"*; não autenticado | *"endpoints… may return delayed or incomplete market data"*; *"does not provide historical data… or a TradingView data entitlement"* | **REJEITAR** — endpoints públicos não-oficiais, dado atrasado/incompleto, sem entitlement; não-reprodutível |

**Confirmação/refutação da triagem preliminar de Andraus** (chat: rejeitar 1,3,4,6,7 e o original; adiar 2; adaptar 5): **CONFIRMADA** com as fontes capturadas. Ajuste fino: C5 adaptado **estritamente como referência de engenharia para BL-032** (não como conector/fonte do SOT); C2 adiado e **reclassificado** como provedor de dados de terceiro (entra na avaliação de SPEC-038-DATASRC-001, não como "conector TradingView").

### 4-bis.3 Pergunta objetiva a enviar ao suporte/legal do TradingView (PROPOSTA — quem envia é Andraus)
> "Nossa aplicação consome dados de mercado exclusivamente através do **MCP Server oficial** do TradingView (`mcp.tradingview.com`, OAuth 2.1, plano Essential+). Pretendemos usar esses dados como **insumo de análise algorítmica interna** (geração de hipóteses/recomendações para decisão humana; **não** executamos ordens, **não** redistribuímos o dado, **não** fazemos order routing). (1) Esse uso é permitido pelo acesso via MCP, ou os Termos de **display-only / non-display** (algorithmic decision-making) também se aplicam ao dado entregue via MCP? (2) Os dados via MCP na beta são **delayed**; há plano/tier com dado em tempo real via MCP? (3) Há algum termo específico do MCP além dos Termos gerais (`tradingview.com/policies`)?"

`SPEC-038-TVMCP-001` foi **DECIDIDA** por Andraus (DHR-DEC-003 §1.1: canal CDP aceito como perfil exploratório, risco ToS assumido; MCP oficial = canal a reavaliar). Enquanto não houver resposta do TradingView, o **canal oficial permanece a reavaliar** e a **fonte de dado de decisão** permanece `[DECISÃO NECESSÁRIA: SPEC-038-DATASRC-001]` (ABERTA).

---

## 5. Lacunas, conflitos e INDETERMINADOS (honestidade — RULE-MET-01)

1. **Latência e limites por plano da candidata = INDETERMINADO** (não informados; não inventar — critérios 4 e 7).
2. **Auditoria de código é estática e mediada por modelo** (`sources/_LIMITACAO-WEB.txt`): não substitui leitura byte-a-byte do fonte nem SAST. Um parecer definitivo de segurança exigiria clonar e analisar o repositório — fora do mandato (não instalar/executar).
3. **Conformidade legal é interpretação de ToS, não aconselhamento jurídico** — reporta a cláusula verbatim; a decisão de risco é de Andraus.
4. **Dona do backtest/calibração (BL-032) — DECIDIDA (DHR-DEC-003 §1.2): dona = SPEC-018** (ampliar sob WF-V01/RULE-CTF-01; não cria slot novo). A SPEC-038 fornece a ferramenta de dados/replay e seu contrato/proveniência, mas **não** calibra a J-001 nem decide a fonte histórica de decisão; ponte em §7. **J-001/N-001 seguem abertas** (valores definitivos pós-backtest).
5. **J-001/N-001 permanecem ABERTAS** — nenhuma recomendação de ferramenta as toca.
6. Este Dossiê **não auditou a veracidade das páginas** (mandato de pesquisa — atomic-spec §15); tratá-las como DADO.
7. **Contagem de ferramentas divergente (INDETERMINADO):** o MCP **oficial** reportou ~**43** funções (9 categorias) via WebFetch (mediado); o TUTORIAL local cita **84 ferramentas** (projeto CDP local, codebase diferente); **nenhuma** fonte do repositório declara "**78**". Os três números referem-se a objetos distintos (oficial vs. CDP local) e/ou são mediados por modelo — o número exato é INDETERMINADO; não reconciliar artificialmente.
8. **Latência do MCP oficial = "delayed" na beta** (blog) → **INDETERMINADO** se chega a tempo do relógio do Manager (WF-K02/WF-05); não há SLA de tempo real publicado; não presumir.
9. **Proveniência de dados de terceiros (C2 tradingviewapi, C5 Yahoo/Reddit/RSS) = INDETERMINADA/não-TradingView** — não confundir "nome TradingView no produto" com dado licenciado do TradingView.
10. **Conformidade do MCP oficial com display-only = INDETERMINADA** — depende de resposta do TradingView (§4-bis.3); não decidida (CONS-01).
11. **TUTORIAL-PINE (`reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md`) = referência interna NÃO-NORMATIVA, não auditada** — incorporado em `ABERTURA.md` §4-ter como possibilidade real de fonte de dado/ferramenta e de ambiente de backtest via Pine. Incoerências/inferências que o próprio tutorial declara e que **NÃO** foram verificadas por este Dossiê: (a) `buy_hold_return` — base de cálculo **não conferida** pelo autor (INDETERMINADO); (b) chaves `in_2`/`in_4` dos inputs = **inferência** não confirmada (só `in_0`/`in_1`/`in_3` confirmadas); (c) bloco Pine de separação treino/teste = **esboço não executado**; (d) topo da onda 5 corrigido para **87.395,67** (candles brutos H4) vs. **87.278** lido de indicador de terceiro no tutorial-MCP anterior — divergência registrada, não reconciliada. Nenhum número do tutorial é limiar (J-001/N-001 abertas). Ler o Strategy Tester por CDP = coleta automatizada → mesmo risco ToS já assumido por Andraus no perfil exploratório, **sem** estendê-lo a "fonte de decisão" (`ABERTURA.md` §4-ter.6).

---

## 6. Escopo/quantidade resultantes, fronteiras e re-apontamento de gatilhos

### 6.1 Escopo e quantidade (detalhe na `ABERTURA.md`)
Proposta: **1 Spec** (SPEC-038), número preservado (slot não dividido/renumerado), complexidade **HIGH**, profundidade **D0–D7** (profile standard, AGENTS.md §4). Cobre a capacidade "Trading Analysis Tool Harness" do ROADMAP §26 (contrato de ferramentas de análise), **sem** absorver governança de seleção.

### 6.2 Fronteiras explícitas (NÃO absorver)
- **SPEC-038 (este slot):** contrato por-ferramenta (Finalidade→...→Falhas); tipologia de ferramenta (dados OHLC/volume, indicador, desenho/marcação, replay); o dado de ferramenta é **Observação**, não Evidência (INV-06); determinismo/proveniência como campos de contrato.
- **SPEC-039 (Tool Selection & Governance):** *quando* usar/não usar; ferramenta preferencial; **fallback**; validação; **tool poisoning**; dados não-confiáveis; resultado contraditório. A *política* fica aqui.
- **SPEC-042 (Runtime Guardrails):** allow/deny/limites/gates de execução da ferramenta em runtime.
- **SPEC-044:** detecção de alucinação/afirmação sem fonte.
- **INV-05:** nenhuma ferramenta executa ordem; marcação/desenho/alarme é análise, não ordem.

### 6.3 Re-apontamento de gatilhos RMR-001 (estado pós-DHR-DEC-003; EUA-E21/RULE-ECC-01)
O número/slot SPEC-038 é **preservado** → nenhum re-apontamento de gatilho `spec:` é necessário. A **abertura** da SPEC-038 dispara (gatilho `spec:SPEC-038 em redação`), por precedente de que a abertura conta como "em redação" (cf. BL-004 na abertura da SPEC-003):
- **BL-031** (`spec:SPEC-038 em redação`) → **Absorvido** (DHR-DEC-003 §1.1, encaminhado à SPEC-038); tratado por esta avaliação de viabilidade (§4) e pela decisão de canal de Andraus.
- **BL-017** (dimensão B da SPEC-020, `spec:SPEC-007/014/**038** em redação`) → o detector reporta **disparado sem registro**; a **promoção a `ATIVADO` é de Andraus** (`[DECISÃO NECESSÁRIA: promover BL-017]` — não executada pelo Especificador, CONS-01). Encaminhamento quando promovido = fechar `tool correctness` por emenda pontual à SPEC-020 **quando a SPEC-038 for homologada** (não agora).
- **BL-032** → **DECIDIDA: dona = SPEC-018** (DHR-DEC-003 §1.2); não dispara aqui (gatilho `spec:SPEC-018 em redação`) — apenas ponte de rastreabilidade (§7).
- **BL-026** NÃO dispara (gatilho `spec:SPEC-008/010-015`) — não é SPEC-038.

### 6.4 Referências em Specs BASELINED a SPEC-038 (item 6 do §15) — erratum aditivo?
Referências baselined encontradas: `specs/features/SPEC-003/plan.md:1196` (BL-031 → SPEC-038, mero ponteiro de rastreabilidade) e **SPEC-020** (dimensão B `tool correctness ↔ SPEC-038`, via ROADMAP §12 / BL-017). Ambas **apontam para o número SPEC-038 como slot futuro**; como o número é preservado, **nenhum erratum aditivo de re-apontamento é necessário** (padrão ERRATUM-SPEC019-001 não se aplica). Nenhuma Spec baselined é reescrita (INV-09).

---

## 7. Ponte para SPEC-018 (dona do backtest/calibração da J-001 — BL-032 DECIDIDA)
A SPEC-038 é **pré-requisito instrumental** da calibração (precisa de dados históricos determinísticos e reprodutíveis e de uma ferramenta de leitura de backtest com proveniência), mas **não** a resolve. **DHR-DEC-003 §1.2 fechou BL-032: a dona é a SPEC-018** (ampliar o ciclo Extração→Formalização→Validação→Backtest→Stress→Sandbox→Aprovação com as etapas de backtest/calibração sob **WF-V01** e **RULE-CTF-01**; gatilho `spec:SPEC-018 em redação` preservado; sem slot novo). A SPEC-038 apenas **expõe** o contrato de uma ferramenta de dados históricos/replay e de **leitura do Strategy Tester** (Observação, Classe D) com determinismo, proveniência (campos em `ABERTURA.md` §4-ter.3) e ressalva anti-hindsight declarados — deixando J-001/N-001 e a execução da calibração para a SPEC-018 (CONS-01). O **protocolo de calibração** detalhado por `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` §4 (walk-forward, DSR/PBO fora do TradingView, separação treino/teste) é **insumo não-normativo para a SPEC-018**, não entrega da SPEC-038.

---

## 8. Conformidade RULE-ECC-05 (Pesquisa Multi-Lente)
- **Lente 1 — Arquitetura:** §3.1/§3.2 (contrato de ferramenta, máquina de estados determinística, tool poisoning) — aplicada.
- **Lente 2 — Estado da arte de ferramentas/dados de análise técnica:** §3.3/§3.5/§4 (OHLC/volume, Pine Script, repainting/determinismo, proveniência, provedores licenciados vs scraping, segurança MCP) — aplicada. *(Observação: a "escola de análise" Elliott/SMC/ICT já foi pesquisada em PESQUISA-WORKFLOW-TRADING-2026-10-01 e não é o objeto desta Spec — SPEC-038 serve dados/ferramentas às escolas, não redefine as escolas; reusada por referência, não recontada.)*
- **Lente 3 — Confronto E conformidade com WORKFLOW.md:** a SPEC-038 toca, por fornecer o insumo de dados/marcação: **WF-02/WF-03/WF-05** (agentes consomem dados/indicadores/desenhos), **WF-K02** (latência de dados vs. relógio/pré-aviso do Manager), **WF-A01/WF-A03** (marcação do alarme-gatilho; morte por refutação — desenho de nível/invalidação), **WF-C03** (order flow/volume → dimensão de volume; dado faltante = INDETERMINADO), **WF-V01** (walk-forward+DSR/PBO como requisito herdado para replay/backtest), **WF-V02** (rótulo de qualidade de dado/evidência por escola). A SPEC-038 **não contradiz** nenhum `WF-xx` e **não fecha** a `WF-D03` aberta (não toca convicção/J-001). Divergência eventual = achado de Andraus, nunca da Spec (DHR-WF-001).

> **Nota (ver Adendo 8-A, 2026-10-03):** a redação acima (homologada no Dossiê, DHR-SPEC038-001) leu a **lente 2** como "estado da arte de ferramentas/dados". O Adendo 8-A abaixo corrige o enquadramento após leitura literal de RULE-ECC-05 e **declara a não-incidência** da regra sobre a SPEC-038 — o texto original é preservado (INV-07), apenas enquadrado corretamente.

---

## Adendo 8-A — Determinação de incidência de RULE-ECC-05 (aditivo, 2026-10-03; INV-07)

[FONTE: `governance/RULES.md` l.478–495 (RULE-ECC-05, DHR-ECC05-001/DHR-WF-001); `atomic-spec.md` §15; saneamento do achado Menor M-01 do parecer CONFORME do Revisor sobre o Plan v1.0. Adendo **aditivo** — não reescreve o Dossiê homologado; preserva §8 acima (INV-07).]

**Texto-gatilho da regra (verbatim, `governance/RULES.md` l.478–490):** *"Toda Spec que define ou toca comportamento de agente analítico (Structural/Institutional/Operational), do Conviction/Fusion Engine (SPEC-003 …), do Manager Agent (SPEC-015) ou do Risk Agent (família RISK-SPEC) DEVE, no seu Dossiê de Pesquisa (RULE-ECC-02), pesquisar TRÊS lentes … (2) Estado da arte/melhores práticas da escola de análise ou de risco-retorno pertinente ao componente (Elliott/SMC/ICT/gestão de risco) … Specs de meta-harness/governança (SPEC-002/019/020/021 e análogas) ficam fora do escopo — não tocam comportamento de trading."*

**Determinação: RULE-ECC-05 NÃO INCIDE sobre a SPEC-038.** Fundamento:

1. **A SPEC-038 não define nem toca comportamento de agente analítico, do Conviction/Fusion Engine, do Manager ou do Risk Agent.** É harness de **contrato de ferramenta/dado**, agnóstico de escola: produz **Observação** (dado bruto — OHLCV/volume/indicador/desenho/métrica de tester), **nunca** Evidência, hipótese, convicção, decisão ou ordem (CC-01/CC-02/INV-06; Plan D0). Não cria, ordena nem reinterpreta hipótese estrutural; não agrega convicção; não sintetiza; não avalia risco-retorno.
2. **É "análoga" às Specs de meta-harness explicitamente excluídas** (SPEC-002/019/020/021) — infraestrutura/tooling que serve o comportamento de trading sem *ser* comportamento de trading. A exclusão literal da regra ("e análogas … não tocam comportamento de trading") alcança a SPEC-038 pelo mesmo critério.
3. **Coerência interna:** a mesma razão já sustentou **CC-10 N/A quanto a escola** e **CC-12 N/A** (PRINC-BID-001 não incide — "tooling agnóstico"; Plan §Constitution Check / §Princípios de Domínio). Fazer a lente 2 incidir contradiria essas determinações já declaradas.
4. **Lente 2 literal seria sobre a escola/risco-retorno (Elliott/SMC/ICT/gestão de risco), não sobre ferramentas/dados.** Como a SPEC-038 não é componente de escola nem de risco-retorno, não há "escola pertinente ao componente" a pesquisar sob a lente 2. O que a SPEC-038 pesquisa (contrato de ferramenta, determinismo/repaint, proveniência, segurança MCP, provedores) pertence à **lente 1 (arquitetura)** — e está feito (§3.1–§3.5/§4).

**Consequências:**
- **Nenhuma pesquisa web nova nem captura verbatim adicional é exigida** por este saneamento: como a regra não incide, não há obrigação de lente 2 "escola/risco-retorno" a cumprir. As fontes já capturadas em `sources/` (acesso 2026-10-02/03) permanecem suficientes e não foram ampliadas por este adendo.
- A informação de que a escola de análise já foi pesquisada em `PESQUISA-WORKFLOW-TRADING-2026-10-01` (reusada por referência) permanece verdadeira e **reforça** — não funda — a não-incidência.
- O confronto/conformidade com `WORKFLOW.md` (§8 lente 3) permanece **útil e mantido** por prudência (a SPEC-038 fornece insumo ao pipeline), mesmo não sendo exigido pela regra que não incide. Nenhum `WF-xx` é contrariado; `WF-D03` não é fechada (DHR-WF-001).
- **A determinação de incidência é do Revisor/Andraus** auditar; esta é a posição fundamentada do Especificador [PROPOSTA — a confirmar pelo Revisor]. Se o Revisor/Andraus entender que a regra incide, o Especificador cumprirá a lente 2 literal (pesquisa da escola/risco-retorno com `[EXTERNO]` + captura verbatim) — não há bloqueio, apenas a determinação de que, como está, não é exigível.

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-02; capturas verbatim em `sources/`)
- [tradingview-mcp-jackson (GitHub)](https://github.com/LewisWJackson/tradingview-mcp-jackson) — SRC-TVMCP-01
- [TradingView — Terms of Service / Policies](https://www.tradingview.com/policies/) — SRC-TOS-01
- [Practical DevSecOps — MCP Tool Poisoning](https://www.practical-devsecops.com/mcp-tool-poisoning/) — SRC-MCPTOX-01
- [MCPTox benchmark (arXiv 2508.14925)](https://arxiv.org/pdf/2508.14925) — SRC-MCPTOX-01
- [crosstrade.io — Pine Script Repainting](https://crosstrade.io/blog/pine-script-repainting) — SRC-REPAINT-01
- [PineCoders FAQ — avoid repainting with security()](https://www.tradingview.com/script/cyPWY96u-How-to-avoid-repainting-when-using-security-PineCoders-FAQ/) — SRC-REPAINT-01
- [edgeful — futures data API comparison (Polygon/Databento)](https://www.edgeful.com/blog/posts/futures-data-api-polygon-databento-edgeful-comparison) — SRC-DATA-01
- [Databento — Futures Market Data](https://databento.com/futures) — SRC-DATA-01
- [TradingView — MCP Server docs](https://www.tradingview.com/mcp/docs) — SRC-TVMCP-OFFICIAL-01 (acesso 2026-10-03)
- [TradingView — MCP Server public beta (blog)](https://www.tradingview.com/blog/en/tradingview-mcp-server-public-beta-60864/) — SRC-TVMCP-OFFICIAL-01 (acesso 2026-10-03)
- 7 candidatos (acesso 2026-10-03) — SRC-CANDIDATES-01: [tradesdontlie](https://github.com/tradesdontlie/tradingview-mcp) · [tradingviewapi.com](https://tradingviewapi.com/mcp) · [bidouilles](https://github.com/bidouilles/mcp-tradingview-server) · [mikeh-22](https://github.com/mikeh-22/tradingview-mcp) · [atilaahmettaner](https://github.com/atilaahmettaner/tradingview-mcp) · [ertugrul59](https://github.com/ertugrul59/tradingview-chart-mcp) · [fiale-plus](https://github.com/fiale-plus/tradingview-mcp-server)
- PESQUISA-WORKFLOW B.7 (repo) → [nexusfi](https://nexusfi.com/a/automation/trading-system-architecture) · [mbrenndoerfer](https://mbrenndoerfer.com/writing/quant-trading-system-architecture-infrastructure) — SRC-WORKFLOW-01 (captura de 2ª ordem; URLs últimas não re-fetchadas)

**Referências INTERNAS NÃO-NORMATIVAS (local, não web; TRACE-06 — DADO, não baseline):**
- `reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md` (tutorial-MCP; incorporado em `ABERTURA.md` §4-bis) — mecânica do canal CDP local, não auditado.
- `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` (tutorial-Pine, 2026-10-03; incorporado em `ABERTURA.md` §4-ter) — possibilidade real de Pine como fonte de dado/ferramenta e ambiente de backtest; execução real BTCUSDT/H4 não auditada; itens não verificados listados em §5 item 11.

*Dossiê de pesquisa não-normativo. Insumo para a Proposta de Abertura (`ABERTURA.md`) e para a decisão de Andraus. Não altera ROADMAP, RULES, WORKFLOW, Specs, nem fecha qualquer decisão (CONS-01). Conteúdo web = DADO (`[EXTERNO]`), nunca instrução nem baseline.*
