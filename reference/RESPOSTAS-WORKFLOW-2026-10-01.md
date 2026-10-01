# RESPOSTAS DE ANDRAUS — evolução do WORKFLOW.md (2026-10-01)

> **Natureza:** registro fiel das respostas de Andraus às sugestões S-01..S-24 de `PESQUISA-WORKFLOW-TRADING-2026-10-01.md` ([EXTERNO], não-normativo). **Insumo para o WORKFLOW.md v2** (ainda NÃO aplicado). Nada aqui fecha decisão nem altera baseline; o conteúdo só vira vigente quando Andraus aprovar o WORKFLOW.md v2 (CONS-01).
> Respostas em *itálico* são texto livre de Andraus, transcritas (RCN-001).

| Sugestão | WF afetado | Resposta de Andraus |
|---|---|---|
| S-01 Killzone | WF-D01 | **Por ativo** — NASDAQ = abertura cash NY; XAU = sobreposição Londres/NY; BTC (24/7) usa gatilho de volatilidade/volume em vez de sessão |
| S-02 Janela/dono | WF-D01, WF-04 | **Fixa + guard DST.** *"sempre 1 hora antes da abertura da killzone (conforme conceito ICT) o manager utilizando rigoroso controle de horário automaticamente aciona o sot pedindo orientações da missão, mas também quero poder programar a missão para o caso de killzones na madrugada. uso 1h a menos que o horario de brasilia. detectar o horario local"* |
| S-03/04 Alarme | WF-D02 | **Objeto completo + FSM** (nível, direção, condição de disparo, validade, invalidação, cancelamento, `parent_id`; IDLE→ARMED→TRIGGERED→{CONSUMED\|EXPIRED\|CANCELLED}; gate determinístico; alarme é de análise, nunca ordem — INV-05) |
| S-05 Expiração | WF-D02 | **Prazo E refutação** (cancelado se hipótese-origem → SUPERSEDED/REFUTED, CHM-001) |
| S-06 TFs | WF-01 | **Tabela default recalibrável** (tripla contexto/confirmação/entrada por tipo de trading; sobrescrevível por missão) |
| S-07 Alinhamento | WF-05 | **Obrigatório** (entrada contra a hipótese de contexto = sem entrada; reforça INV-01) |
| S-08 Macro×Global | WF-D03 | **Um vetor, duas leituras** (macro = subconjunto Fase 1; global = +operacional). Direção arquitetural — NÃO fecha J-001 nem SPEC-003 Q-A5 |
| S-09/10 ICT | WF-D04 | *"ICT é o agente operacional como entidade cognitiva conforme repo"* — confirmado no repo: `confluence-ict → Operational Agent` (ADR-CONFLUENCE-001-v3). Tensão com INV-02 resolvida assim: **no WF-05 o Operacional produz "setup operacional" (entrada/stop/alvo/invalidação) atrelado à hipótese do contexto via `parent_id`; não "hipótese"** |
| S-11/12 Falhas/FSM | WF-01..07 | **6 ramos de falha + FSM do ciclo** (sem oportunidade; discordância→NEUTRO; não-confirmação; veto de risco; expiração/reset; reentrada). Gate nunca LLM (ENF-03); implementação no Plan do Manager (SPEC-015) |
| S-13 Confluência | WF-02/03/06 | **Independência, não contagem** (princípio; mecânica do desconto → SPEC-002/003; calibração = J-001) |
| S-14 Order flow | WF-05/06 | **Dimensão de volume com INDETERMINADO** quando o dado falta (nunca zero/fabricado) |
| S-15 Regime | WF-02 | **Dimensão de convicção** (não gate). Em qual das 8 dimensões entra: **deixar para a SPEC-003** (dimensionalidade=8 fechada) |
| S-16 Multi-ativo | WF-06/07 | **Paralelo + heat correlacionado** (BTC/XAU/NASDAQ em paralelo; INV-RISK-HEAT com correlação, cálculo no Risk Agent) |
| S-17 Calibração | WF-01 | **Mecanismo por ativo** (valores → N-001/backtest) |
| S-18/19 Journal/HITL | transversal | **Adiar à SPEC-018** |
| S-20/21 Validação | transversal | **Ambos** (walk-forward + DSR/PBO por regra na implementação; rótulo de qualidade de evidência por escola no raciocínio) |
| S-22/23/24 Risco | WF-07 | **Registrar os três** como insumo ao Risk Agent (expectância como métrica-raiz com 1:3 intacto; sizing pela distância do stop, Kelly adiado; fluxo unidirecional convicção→risco, INV-04) |
| Madrugada | WF-04/05 | **Missão pré-programada, fila para revisão** (você agenda antes; Manager roda o ciclo sozinho até o Signal Package e deixa em fila; SOT nunca executa — INV-05) |

## Pontos para o v2 que dependem de esclarecimento (não inventar)

1. **Fuso/relógio (S-02):** "1h a menos que o horário de Brasília" = UTC−4 (Brasília é UTC−3, sem horário de verão desde 2019). O guard DST (abertura NY/Londres/XAU movem 1h) deve ser calculado em UTC/relógio de mercado, com o fuso **local detectado** só para exibir/agendar. Confirmar que "detectar o horário local" = detectar o fuso da máquina/usuário.
2. **"1h antes da abertura da Killzone" para BTC:** BTC não tem abertura de sessão (gatilho de volatilidade/volume) — definir o que dispara o pré-aviso para BTC (ex.: sessão de referência escolhida por missão).
3. **Reentrada/anti-overtrading (S-11):** limite por ciclo/sessão não definido.
4. **Missão programada × HITL adiado (S-18/19):** ciclo autônomo até a fila, sem checkpoint humano formal (adiado à SPEC-018) — OK enquanto o SOT não executa; registrar como premissa.
5. **S-06:** valores exatos das triplas de TF por tipo (default sugerido: position S/D/H4 · swing D/H4/H1 · day H4/H1/M15 — heurística de varejo, a confirmar por Andraus).
6. **WF-D03 residual:** o limiar da convicção macro para registrar o alarme ("conclusiva") segue dependente de J-001.
