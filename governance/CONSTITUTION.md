# SOT Constitution — Sistema Operacional de Trading
<!-- Fonte: ENGENHARIA GERAL.pdf Doc01 + Doc02 + Doc03 | Versão 1.1 -->
<!-- Correções homologadas por Andraus 2026-09-14 (Respostas ao Questionário v1): Q-002 (limiares Fase Piloto), Q-004 (R:R 1:3), Q-005 (hipótese PRIMARY/SUB), Q-006 (estados CHM-001), Q-008 (8 dimensões), Q-009 (4Es), Q-015 (nome). Ver GLOSSARIO.md. -->

---

## Missão do sistema

O SOT é um Sistema Operacional de Inteligência para Trading Institucional que constrói
uma interpretação probabilística, explicável e auditável do mercado financeiro.
**O SOT não procura sinais. O SOT procura compreender o estado estrutural do mercado.**
Toda decisão operacional é consequência dessa compreensão.

---

## Hierarquia metodológica inviolável

```
1. Elliott Wave      → O mapa. Define a estrutura. Sempre primeiro.
2. Fibonacci         → A régua. Valida geometria. Confirma ou rejeita Elliott.
3. Confluência Fractal → Mede coerência entre S1/D1/H4/H1/M5.
4. SMC Institucional → Confirma se o institucional apoia a hipótese estrutural.
5. ICT               → Apenas a execução. Último a agir. Nunca primeiro.
```

Nenhuma camada inferior pode invalidar arbitrariamente uma camada superior.
ICT nunca cria hipóteses. SMC nunca corrige Elliott.

---

## Princípios cognitivos universais

**P01 — Explicabilidade:** O sistema nunca responde apenas "Comprar" ou "Vender".
Toda conclusão deve responder: qual hipótese, quais evidências, quais contraevidências,
quais alternativas, por que foram rejeitadas, o que invalida, o que falta confirmar.

**P02 — Convicção, não score:** O sistema não soma pontos. Constrói convicção
probabilística. A convicção é multidimensional — **8 dimensões** (Q-008): estrutural,
geométrica, fractal, institucional, operacional, temporal, volume, histórica.

**P03 — Hipóteses múltiplas:** O sistema nunca assume uma única interpretação válida.
Mantém sempre: Hipótese Principal + Hipóteses Alternativas + Estado de Convicção de cada.
Eliminação de hipótese exige evidências objetivas.

**P04 — Refutação antes de confirmação:** O agente nunca procura confirmação.
Procura provar que sua hipótese está errada. A ausência de refutação aumenta a convicção.

**P05 — Fractalidade obrigatória:** Toda análise considera múltiplos graus simultaneamente.
A qualidade aumenta com a convergência entre S1, D1, H4, H1, M5.

**P06 — Separação de responsabilidades:** Cada agente possui uma única responsabilidade.
Nenhum agente pode assumir funções pertencentes a outro.

**P07 — Imutabilidade da teoria:** O SOT nunca altera regras de Elliott, proporções de
Fibonacci, fundamentos de SMC, fundamentos de ICT. O aprendizado ocorre apenas sobre
calibração e comportamento específico dos ativos.

**P08 — Persistência cognitiva:** Os agentes não recomeçam a cada candle. Mantêm um
modelo mental persistente do mercado. Novos eventos apenas atualizam esse modelo.

**P09 — Neutralidade de entrada:** O agente nunca inicia procurando compra ou venda.
Inicia procurando compreender o estado do mercado.

**P10 — Dupla Narrativa:** Toda análise produz duas histórias paralelas:
- Narrativa Estrutural (Elliott + Fibonacci + Fractal): "O que o mercado está construindo?"
- Narrativa Institucional (SMC): "Como os institucionais estão construindo isso?"
O Conviction Engine compara as duas narrativas. Convergência = convicção elevada.

**P11 — Evidências independentes:** Evidências causalmente relacionadas (ex: BOS e
rompimento de estrutura) não podem ser contadas duas vezes.

**P12 — Governança da evolução:** Nenhuma nova regra entra diretamente em produção.
Todo novo conhecimento percorre: Extração → Formalização → Validação → Backtest
→ Stress Test → Sandbox → Aprovação → Produção.

**P13 — Auditabilidade:** Toda decisão deve ser reconstruível. O sistema armazena:
estado do mercado, hipóteses, evolução da convicção, evidências, módulos participantes,
versão das Skills, versão da arquitetura, parâmetros utilizados.

**P14 — Integração desacoplada:** O SOT nunca executa ordens diretamente.
Produz um **Signal Package** para o Bot Trade Finance. O TMP é artefato interno de passagem entre a Síntese e o Risk Agent.
<!-- Emendado por EUA-E19a (DHR-EUA-E19a, Andraus 2026-09-22): restauração do termo fundacional "Signal Package" (ENGENHARIA-GERAL l.604-606). A cláusula "via Risk Harness" será acrescentada quando RISK-SPEC-020 for homologada (C-03). -->

---

## Sequência de execução dos agentes

```
TradingView → Data Acquisition
                    ↓
             Market Digital Twin (estado vivo do mercado)
                    ↓
             <!-- [LEGADO 2026-09-26] Mission Engine → ELIMINADO; absorvido pelo Manager Agent Fase 0 (ADR-MANAGER-001, HOC-003) -->
             <!-- [LEGADO 2026-09-26] Master Orchestrator → ELIMINADO; absorvido pelo Manager Agent (ADR-MANAGER-001, HOC-003) -->
             Manager Agent (Fase 0: Mission Lifecycle → Fase 1: Dispatch → Fase 2: Conviction)
            /       |        \         \
     Elliott    Fibonacci    SMC      ICT
     Specialist  Validator  Specialist  Specialist
            \       |        /         /
             Blackboard Cognitivo (comunicação exclusiva)
                    ↓
             Conviction Engine (compara narrativas, calcula convicção)
                    ↓
             Synthesis Agent (árbitro final)
                    ↓
             [TMP — artefato interno]
                    ↓
             … (camada de risco — RISK-SPEC-020, futura)
                    ↓
             Signal Package (fronteira SOT → exterior)
                    ↓
             Bot Trade Finance
```

Dependências de sequência obrigatórias:
1. Elliott deve completar antes de Fibonacci poder validar
2. Fibonacci deve completar antes de Fractal poder medir confluência
3. Structural conviction deve atingir mínimo antes de SMC iniciar
4. SMC deve completar antes de ICT iniciar
5. ICT permanece INATIVO se não houver hipótese estrutural aprovada

---

## O que nenhum agente faz

- **Elliott Specialist** nunca faz: análise institucional, BOS/CHoCH/MSS, Order Blocks,
  FVG, cálculo de convicção global, execução de trade
- **Fibonacci Validator** nunca faz: criar contagens Elliott, gerar sinais isoladamente
- **SMC Specialist** nunca faz: contar ondas Elliott, alterar hipótese estrutural,
  gerar sinais sem contexto estrutural, sobrepor decisão de Elliott
- **ICT Specialist** nunca faz: criar hipóteses estruturais (de nenhum tipo — nem primária nem sub),
  operar sem hipótese aprovada, alterar Elliott, aceitar R:R < 1:3
- **Synthesis Agent** nunca faz: análise direta de mercado, operar sem convicção ≥ 70% (limiar de Fase Piloto — Q-002),
  resolver conflito direcional favorecendo SMC sobre Elliott

---

## Definições canônicas

**Hipótese:** Interpretação estrutural do mercado com justificativa, evidências,
contraevidências, condições de invalidação e projeções futuras. Nunca uma verdade.

**Convicção:** Estimativa dinâmica e multidimensional da robustez de uma hipótese
diante do estado atual do mercado. Não é score. É uma medida contínua de confiança.

**Evidência:** Dado observável que aumenta ou reduz a convicção de uma hipótese.
Evidências correlacionadas contam como uma. Evidências independentes somam.

**Bias:** Direção direcional (bullish/bearish/neutral) resultante da análise estrutural.
Somente Elliott pode definir o bias primário. SMC confirma ou enfraquece.

**Invalidador:** Condição específica que, se observada, descarta uma hipótese.
Todo sinal deve declarar seu invalidador explicitamente.

**Confluência:** Convergência de múltiplas evidências independentes em uma mesma zona
de preço ou hipótese. Quantidade de confluências ≠ qualidade de confluências.

**Sinal operacional:** Output do Synthesis Agent quando convicção global ≥ 70% e
R:R calculado ≥ 1:3 e nenhum conflito direcional aberto entre Elliott e SMC.
*(Limiares ≥ 70% e score ≥ 7/9 = FATO NORMATIVO de Fase Piloto, recalibrável após backtest — Q-002. R:R ≥ 1:3 = regra única — Q-004.)*

---

## Framework 4Es — Prioridade de execução cognitiva
<!-- Fonte: CEE-001 §2-3 + GEH-001 §3 | Q-009 (Andraus 2026-09-14) — Economicidade adicionada como 4º E -->

O SOT opera segundo o Framework **4Es** com hierarquia de prioridade INVIOLÁVEL:

```
Eficácia     → "Fazer a coisa certa" — seguir a teoria corretamente
Efetividade  → "Alcançar o resultado no tempo certo" — output acionável (inclui latência)
Eficiência   → "Usar o mínimo de recurso por execução" — reduzir custo, latência, tokens
Economicidade → "Menor custo unitário de provisionamento" — classe de modelo, cache, roteamento
```

**Ordem de prioridade:** Conformidade Constitucional > Eficácia > Efetividade > Eficiência > Economicidade

Nenhuma otimização de custo sobe esse degrau. Eficiência (e Economicidade) NUNCA sobrepõem Eficácia.
Um modelo mais rápido/barato que gera análise incorreta é pior que um modelo lento que gera análise correta.

---

## Blackboard Cognitivo — 8 workspaces
<!-- Fonte: KERNEL V2.docx.pdf EC-COG-004 | Versão 1.1 -->

O Blackboard Cognitivo é o único canal de comunicação entre agentes. Comunicação
direta agente→agente é proibida constitucionalmente.

| Workspace | Responsável | Conteúdo |
|---|---|---|
| Observations | Todos (publicam) | Dados brutos de mercado, payloads |
| Evidence | Especialistas | Evidências estruturais e institucionais |
| Hypotheses | Elliott Specialist (PRIMARY) + demais agentes (SUB, referenciadas via parent_id) | Hipótese primária estrutural + sub-hipóteses de domínio (Q-005) |
| Narratives | SMC Specialist | Narrativa institucional, Dupla Narrativa |
| Conviction | Conviction Engine | Vetor de convicção multidimensional |
| Missions | Orchestrator | Missões ativas, contexto operacional |
| Alerts | Synthesis Agent | Sinais, TMPs, alertas Telegram |
| Meta-Cognition | Orchestrator | Estado do sistema, versões, auditoria |

**5 regras constitucionais do Blackboard:**
1. Todo agente publica apenas no seu workspace designado
2. Leitura é livre — publicação é restrita
3. Hipótese só pode ser base de decisão nos estados ACTIVE ou DOMINANT (estados canônicos do CHM-001 — Q-006; ciclo EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→ARCHIVED)
4. Blackboard é append-only — estados evoluem, objetos não são deletados
5. O Orchestrator coordena, nunca analisa diretamente

---

## Modelo de roteamento cognitivo
<!-- Fonte: CEE-001_Versao_Consolidada.md §5 | Versão 1.1 -->

| Tipo cognitivo | Descrição | Modelo |
|---|---|---|
| Tipo I — Determinístico | Regras fixas, scoring, cálculos | Haiku |
| Tipo II — Procedimental | Sequências passo-a-passo | Haiku |
| Tipo III — Especialista | Julgamento técnico, análise de padrões | Sonnet |
| Tipo IV — Multi-narrativa | Conflito entre narrativas, árbitro | Opus (reservado) |
| Tipo V — Raciocínio profundo | Casos extremos, ambiguidade máxima | Opus (reservado) |

Decisão de roteamento é responsabilidade do Orchestrator — agentes não escolhem seu próprio modelo.

---

## Arquitetura de 12 domínios cognitivos
<!-- Fonte: KERNEL V2.docx.pdf §1 | Versão 1.1 -->

O SOT é organizado em 12 domínios arquiteturais (Engineering Cards EC-COG-001 a EC-COG-012+):

| Domínio | Módulo | Responsabilidade |
|---|---|---|
| Kernel | EC-COG-001 | Contratos fundamentais do sistema |
| Hipótese Canônica | EC-COG-002 | Modelo de hipótese estruturada |
| Knowledge Graph | EC-COG-003 | Memória relacional de padrões |
| Blackboard | EC-COG-004 | Comunicação inter-agente |
| Event Bus | EC-COG-005 | Pub/sub de eventos cognitivos |
| Elliott Engine | ECES | Processamento de ondas |
| Fractal Confluence | FCES | Confluência multi-timeframe |
| Conviction Engine | CES | Vetor de convicção multidimensional |
| Institutional Intel | IIES | Análise SMC contextual |
| ICT Execution | IEIES | Execução de alta precisão |
| Mission Orchestration | MOES | TMP e coordenação de missões |
| Knowledge Governance | KGS | Evolução controlada do conhecimento |
