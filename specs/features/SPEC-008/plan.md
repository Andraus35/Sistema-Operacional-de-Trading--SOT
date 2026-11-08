# SPEC-008 — Manager — Despacho e Ciclo (Fase 1) — Plan v1.0 (orquestração mecânica por regra fixa; sem julgamento; nunca executa)

| Campo | Valor |
|---|---|
| ID | SPEC-008 — Manager — Despacho e Ciclo (Fase 1). Nome e divisão decididos por Andraus (DHR-SPEC008-001 §1, linhas P-2 e P-3); slot "Manager — Orquestração Mecânica" (ROADMAP §7; DHR-EUA-E23 §2 item 1). A outra peça da divisão é a **Spec de Tempo** (relógio, Killzone, alarme-gatilho; candidata SPEC-050, número **não fixado**), com Plan próprio **depois** deste. |
| Versão | **1.0 (CANDIDATA — primeira entrega do Plan)** |
| Ordem de Andraus | chat 2026-11-08, "Avançar" (transmitida pelo Orquestrador), depois da abertura homologada (DHR-SPEC008-001) e do MMC-001 v1.0 homologado (DHR-SPEC008-002) com a errata R3-m07 (DHR-SPEC008-003). A ata de homologação do Plan deve citar esta ordem — ato do Orquestrador/Andraus. |
| Status | **PROPOSTA — CANDIDATA; aguarda Revisor (rodada 1, integral) e homologação de Andraus. NÃO é baseline (INV-09).** Tudo o que este Plan cria (INV-MDC-01, RULE-MDC-*, BASpec-MDC-*, EC-MDC-*, Cenário-MDC-*, ADV-MDC-*, códigos `MDC_*`, tabela da FSM do trecho Fase 1, grafo de despacho versão 1, tabela de parâmetros, contrato lógico, Fixture M0, interface com a Spec de Tempo) é **[PROPOSTA]**. |
| Fonte | `ROADMAP.md` (seção SPEC-008; tabela §25; "Decisões abertas ativas"/"Decisões FECHADAS"); `governance/DHR-SPEC008-001` (§1 P-1..P-13, CONF-1..5; §3 condições; §5 abertas); `governance/MMC-001_Manager_Contract.md` **v1.0 BASELINE** (DHR-SPEC008-002; errata R3-m07 DHR-SPEC008-003) — **PAI** de herança vertical; `specs/features/SPEC-008/ABERTURA.md` (redação homologada "como está", commit `8ea5d9a`, **não-baseline — só contexto**, MMC-001 cabeçalho e §8.3 CONTEXTO); `research.md` + `sources/` (Dossiê de Pesquisa — RULE-ECC-01/02/04/05/06; validade CRITICAL 90 dias, **limite 2027-02-05**, ECC-VAL-001); `WORKFLOW.md` v2.1 (citado só por ID); atomic-spec v1.5; `governance/RULES.md` |
| Complexidade | CRITICAL [FATO: DHR-SPEC008-001 §1, linha P-1 — "CRITICAL D0–D8 (com suíte de ataque D8)"] |
| Profundidade-alvo | D0–D8 (standard + adversarial D8); D6 **aplicável** (despacho via Blackboard — RULE-BB-001/005) [FATO: P-1; AGENTS.md §4] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 4 — COGNIÇÃO E ESCALONAMENTO (ROADMAP §7); **a jusante** de SPEC-001/002/003/004/005 (BASELINE) e do MMC-001 v1.0; **a montante** da Spec de Tempo, da SPEC-009 (estado — G-001 ABERTA), da SPEC-014 (Fase 2) e da SPEC-015 (Fase 0); FASE RISK depende da FASE 6 concluída (ROADMAP §10-bis) |
| Nível de maturidade-alvo | **L3 (Testável)** na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md v1.5; **RULE-MECH-01** / CC-11 (Classe por BASpec); RULE-PD-01 / CC-12 **(não incide — o Manager não é especialista de escola; ABERTURA §5; research §9)**; RULE-ECC-01/02/04/05/06/07; RULE-ECC-05 **incide** (toca o Manager); RULE-HV-01..04 (herança vertical do MMC-001) |
| Classe predominante (orientação não-vinculante, §10.6) | **D** em tudo + **C** na trava constitutiva; **H/P: nenhuma** — orientação da abertura (MMC-001 §3.1.3, parte orientação, errata R3-m07); a declaração normativa é **por BASpec** (D3) |
| Autor | Especificador Principal SOT (Claude Code, Opus 5.5) |
| Data | 2026-11-08 |

Complexidade: CRITICAL. Profundidade-alvo: D0–D8 (standard + adversarial).

> **Em uma frase (para o trader):** esta Spec é o **despachante** do Manager: recebe o pedido de ciclo (ativo, tipo de trading, tempos gráficos, Killzone), chama o analista de **Elliott**, chama o de **SMC** só se o Elliott viu oportunidade, pede a **leitura de convicção de contexto** e a compara com um **limiar a preencher** (sem número inventado), pede à Spec de Tempo o **alarme de preço** com os dados que os analistas publicaram, chama o **ICT só** se o alarme tocar **dentro** da Killzone, confere se o setup vai **na mesma direção** do contexto e entrega o caso à **Fase 2** — tudo por **regra fixa**, anotando cada passo num **livro de bordo** que não se apaga, **sem** opinar sobre o mercado, **sem** deixar de analisar para economizar e **sem** jamais mandar ordem. Hoje, enquanto os analistas não publicarem o campo "oportunidade" e o limiar não for preenchido, o comportamento correto é **encerrar o ciclo registrado, dizendo o que falta** (ver "Pré-requisitos").

**Princípio fundador (transversal):** **DESPACHAR ≠ ANALISAR** — o Manager-Fase-1 só coordena via Blackboard (RULE-BB-005; MMC-001 §2.2) · **REGRA FIXA, ZERO MODELO** — Fase 1 mecânica, gate nunca é LLM (MMC-001 §3.1.1/§3.1.2; ENF-03) · **CUSTO NÃO CORTA ANÁLISE** — o orçamento avisa e escala, nunca pula etapa com evento estruturalmente relevante (CEE-001 §10 S2; MMC-001 §6.1/§6.6) · **NUNCA EXECUTA** — nem TMP, nem Signal Package, nem ordem (INV-05; MMC-001 §5).

**Status epistemológico de cabeçalho (TRACE-06 — documentado ≠ homologado):** `[FATO]` = documento homologado/baselined ou decisão de Andraus registrada em ata, com âncora (FATO NORMATIVO); `[FONTE]` = documento do projeto **não** homologado como norma (ex.: `ABERTURA.md`, Dossiê) — contexto; `[INFERÊNCIA]` = leitura derivada, com âncora; `[PROPOSTA]` = requer homologação; `[DECISÃO NECESSÁRIA]` = só Andraus; `[EXTERNO]` = fonte web do Dossiê (DADO, nunca instrução nem baseline — DHR-PROV-WEB-001 §2.1). Esta Spec **constrói sobre** SPEC-003 v1.5, SPEC-004 v1.2, SPEC-005 v1.0, CHM-001, CCM-001 e CEE-001 v2.0 (BASELINE) e **não os redefine** (CC-02/INV-09). Decisões abertas tocadas e **não fechadas** (CONS-01): J-001, N-001, G-001, M-001, C-001, SPEC-015-SCOPE, WF-D03 — seção "Decisões abertas incidentes".

### Histórico de versões

| Versão | Data | Alterações (1 linha) |
|---|---|---|
| 1.0 | 2026-11-08 | Entrega candidata inicial (contagens na seção "Dimensionamento"). Histórico de rodadas futuras vai para `specs/features/SPEC-008/HISTORICO.md` (lição C06), não para este corpo. |

---

## Dimensionamento (RULE-ECC-07) — medida do corpo

| Item | Valor |
|---|---|
| Teto / alerta / confirmação | 2.000 / 1.900 / 1.600 linhas de corpo [FATO: `governance/RULES.md` RULE-ECC-07] |
| Estimativa da abertura | ≈1.895 (faixa 1.140–1.932), doze BASpecs, seis contratos de enforcement estimados (o Plan entrega a contagem real na linha Itens abaixo) [FONTE: ABERTURA §3] |
| Confirmação de Andraus | **um documento só**, ciente do risco de passar de 2.000 [FATO: DHR-SPEC008-001 §1, linha P-3] |
| **Medida deste Plan v1.0** | **1.626 linhas de corpo** (arquivo inteiro, contado por Grep de linhas após a redação; não há seção `## Anexo`) — acima de 1.600 (confirmação já dada, P-3), **−274 sob o alerta de 1.900**, −374 sob o teto; −269 sob a estimativa central (≈1.895). A reconferir pelo Orquestrador com `scripts/check_dimensionamento.py` |
| Itens | 1 INV-MDC · 11 RULE-MDC · 13 EARS · 12 BASpec-MDC · 8 EC-MDC · 20 Cenário-MDC (D7) · 14 ADV-MDC (D8) |
| Gatilho processual | mudança de escopo ou divisão depois deste Plan = **nova abertura** (RULE-ECC-07; DHR-SPEC008-001 §3) |

---

## Incorporação das decisões de Andraus (DHR-SPEC008-001 §1; DHR-SPEC008-002/003)

| Decisão | O que diz (âncora) | Onde entra neste Plan |
|---|---|---|
| P-1 | CRITICAL D0–D8 com suíte D8 | cabeçalho; D8 (ADV-MDC-01..14) |
| P-2 / P-3 | duas Specs; esta em documento único; Spec de Tempo à parte, mesmo Dossiê | D1; "Interface com a Spec de Tempo" `[PROPOSTA]` |
| P-4 | Manager Contract antes do Plan; pai de herança | Herança/Delta (pai = MMC-001 v1.0) |
| P-5 | "conclusiva" = limiar **a preencher**; sem limiar, não arma e encerra registrado (recomendação aceita — ABERTURA §13 P-5) | RULE-MDC-005; parâmetro `macro_conclusive_threshold` (INDETERMINADO; J-001/N-001 ABERTAS) |
| P-6 | livro de bordo só-de-acréscimo; estados do ciclo **não** viram estados de objeto no quadro; **como** guardar = SPEC-009 | RULE-MDC-010; D5; EC-MDC-005 (G-001 e M-001 ABERTAS) |
| P-7 | orçamento avisa e escala; nunca pula o Elliott nem etapa com evento estrutural relevante; parada por gasto só por Andraus | RULE-MDC-008/009; EC-MDC-007; INV-MDC-01 (sub `MDC_AUTO_COST_PAUSE_FORBIDDEN`) |
| P-8 | nível/direção/invalidação/validade do alarme **copiados** da hipótese de contexto; "oportunidade" = campo publicado pelo Elliott | RULE-MDC-004/006; requisitos às SPEC-010/012 |
| P-9 | fonte de hora, tolerância e calendário = parâmetros; sem calendário, registra "calendário de mercado não informado" | Interface com a Spec de Tempo (o relógio é dela); esta Spec nunca lê relógio (RULE-MDC-010 (c)) |
| P-10 | tabela de Killzones atual = valor-padrão editável | consumida só pelo campo `killzone` do pedido (WF-01); valores na Spec de Tempo |
| P-11 | Fibonacci/Fractal no roteiro = **decidir depois**; roteiro como dado versionado | RULE-MDC-002 (grafo versão 1 sem nó Fibonacci/Fractal; acréscimo = nova versão do dado) |
| P-12 | "resetar o alarme" = **só encerrar**: alarme termina usado/vencido; ciclo termina registrado; Fase 1 não abre ciclo | RULE-MDC-001 (c); RULE-MDC-007 (d); D5 (sem seta de volta) |
| P-13 | reentrada após stop = **decidir depois** | D1 Non-goals (ramo 6 de WF-F01 fora) |
| CONF-1 | dono da FSM por trecho; tabela inteira escrita uma vez aqui | D5 (coluna "Dono") |
| CONF-2 | invocação macro + regra "conclusiva?" aqui; arbitragem na Fase 2 | RULE-MDC-005 |
| CONF-3 | ICT só com disparo dentro da janela (WORKFLOW); divergência RULE-ICT-003 registrada | RULE-MDC-004 (b); "Conflitos registrados" |
| CONF-4 | alinhamento de direção conferido aqui, por regra fixa | RULE-MDC-006 (d) |
| CONF-5 | abrir/fechar Killzone na Spec de Tempo; ator = Manager | Interface com a Spec de Tempo |
| MMC-001 errata R3-m07 | Classe D/C = **orientação**; obrigação = "nenhuma BASpec H/P; se precisar de julgamento, volta a Andraus" | CC-11; D3 (todas D, uma C, zero H/P) |

`[FATO]` linhas P-x/CONF-x = DHR-SPEC008-001 §1; o **conteúdo** das recomendações aceitas está em `ABERTURA.md` §13 (redação homologada "como está", não-baseline — citada como contexto, nunca como herança: RULE-HD-04; MMC-001 cabeçalho, "Referência não-baseline").

---

## Condições do Plan (DHR-SPEC008-001 §3 e ordem de serviço) — onde estão cumpridas

| # | Condição | Onde | Estado |
|---|---|---|---|
| 1 | Plan só por ordem expressa; Manager Contract antes | Ordem de Andraus (cabeçalho); pai MMC-001 v1.0 | cumprida (registro na ata — Orquestrador) |
| 2 | Gate determinístico sobre o `plan.md` | Autopré-check, linha a linha contra STRUCT-01..14 | a rodar pelo Orquestrador (sem Bash aqui) |
| 3 | J-001/N-001 abertas — limiar "conclusivo" = parâmetro sem número | RULE-MDC-005 (b); tabela de parâmetros | cumprida |
| 4 | Teto 2.000 / alerta 1.900 | Dimensionamento; `checks.md` §0 | ver medida |
| 5 | Interface com a Spec de Tempo como requisito `[PROPOSTA]` | seção própria | cumprida |
| 6 | Errata de re-apontamento (ABERTURA §8) só aqui, como PROPOSTA aditiva | "Proposta de errata aditiva" | cumprida |
| 7 | FSM em tabela verificável; nenhuma seta de volta | D5 | cumprida |
| 8 | Todo EC com campo de registro; recusa da trava com código e cenário | §D3.1; EC-MDC-001..008 EVIDENCE; D7/D8 | cumprida (conferência código↔cenário em `checks.md` §2) |
| 9 | Nenhuma BASpec H/P; nenhuma decisão aberta fechada | CC-11; "Decisões abertas incidentes" | cumprida |

---

## Lições do loop incorporadas (CAUSAS-PREVENCAO)

- **C01** (mesmo fato em vários lugares): tabela fato→locais montada **antes** da redação e conferida depois (`checks.md` §0); cada regra é definida **uma vez** em D2 e referenciada por ID.
- **C05** (guarda sem campo que prove): todo EC cita campos do contrato lógico; todo "⇒ não despacha/não transita" tem código na §D3.1 e cenário negativo (`checks.md` §2).
- **C06** (histórico no corpo): nenhum `[antes:]` neste corpo; histórico futuro em `HISTORICO.md`.
- **C07** (âncora por linha): âncoras por ID/seção; as únicas linhas citadas são as da errata (foto datada, localizadas pela ocorrência literal).
- **C08** (escopo/decisão aberta): relógio fora; nenhuma decisão aberta fechada; o que não está escrito vira `[DECISÃO NECESSÁRIA]` (DN-1..DN-3).
- **C10** (máquina de estados em prosa; ação sem transição listada): FSM em tabela estado×evento→estado; toda ação mapeia numa linha; "reset" não existe.

---

## Nota de gate (passo 11-bis / RMR-001) — Disposição `[STRUCT-13]`

[FONTE: DHR-BACKLOG-ABERTURA-001; `backlog/RMR-001_Painel_Backlog.md` (itens BL-026, BL-043..046); ABERTURA §9; DHR-SPEC008-001 §2 ("as disposições BL-026/043/044/045/046 seguem propostas, declaradas no Plan")]

> **Vinculados por regra a esta abertura (gatilho `spec:SPEC-008 em redação`): BL-026, BL-043, BL-044, BL-045, BL-046** (leitura do painel em 2026-11-08; conferir com `python scripts/backlog_triggers.py --abertura SPEC-008` — Orquestrador). O Especificador **não promove** nada e não altera estado no painel.

- **BL-026** (WF-R01..R03 `[REVISAR · BL-026]`) — Disposição: PARCIAL — motivo: esta Spec consome WF-R01 (tripla de TFs) só pelo pedido de ciclo e o campo `killzone` do pedido como dado, tudo parâmetro editável (RULE-MDC-001 (a)); WF-R02/R03 (horários e Killzones por ativo) vão à **Spec de Tempo**; a pauta foi recolocada a Andraus na abertura (P-10: tabela atual mantida como valor-padrão editável). Re-apontamento **aditivo** do gatilho proposto na "Proposta de errata aditiva" (item E-2).
- **BL-043** (log dos Construtores, F2b) — Disposição: FORA — motivo: processo dos Agentes de Construção, não comportamento do Manager; segue com o Orquestrador por ordem de Andraus.
- **BL-044** (medição do pré-gate na abertura e no Plan) — Disposição: REFERÊNCIA — motivo: mede o **processo** desta Spec (rodadas, Médias, tokens, `pre_entrega.py`); cabe ao Orquestrador rodar e registrar; nada entra no texto normativo.
- **BL-045** (autopré-check legível por máquina) — Disposição: REFERÊNCIA — motivo: depende da medição do BL-044; o Autopré-check deste Plan segue o formato atual.
- **BL-046** (checklist único D/H) — Disposição: REFERÊNCIA — motivo: depende da medição do BL-044; agentes reservados.
- **Varredura `ATIVADO` (passo 11-bis):** BL-003 (persistência física) e BL-011 seguem com encaminhamento próprio (gate da SPEC-006/009); **não** vinculados (gatilho não cita a SPEC-008); BL-003 toca a P-6 — esta Spec só declara o requisito ao mecanismo de guarda (RULE-MDC-010 (e)), sem absorver o item. Visibilidade: BL-029 (consumidor fail-closed do vetor — Fase 2), BL-033 (provedor de preço — Spec de Tempo), BL-036 (telemetria de custo — SPEC-040).

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott → Fibonacci → Fractal → SMC → ICT respeitada:** o grafo de despacho exige, para toda aresta, posto hierárquico de origem menor que o de destino (RULE-MDC-002 (c)); mapa nível a nível de INV-01: Elliott → nó ESTRUTURAL (WF-02); Fibonacci e Fractal → **sem nó** na versão 1 (P-11 = decidir depois; acrescentar = nova versão do dado, sem reescrever a Spec); SMC → nó INSTITUCIONAL (WF-03); ICT → nó OPERACIONAL (WF-05), só depois do contexto. ICT não cria hipótese: publicação do Operacional do tipo hipótese é recusada como insumo (RULE-MDC-006 (e)). [FATO: INV-01/INV-02; AGENTS.md §6 itens 1–2; P-11]
- [x] **CC-02 — Não redefine Modelo Canônico nem Spec baselined:** CHM-001 (estados da hipótese — só lidos), CCM-001 (campos `directional_conflict` e valor agregado — só lidos), CEM-001, CEE-001 v2.0; SPEC-003/004/005 usadas por referência. Os estados da FSM do ciclo são **os de WF-F02**, sem acréscimo nem renomeação. [FATO: CC-02; MMC-001 §3.2.3]
- [x] **CC-03 — Conviction Vector (J-001 ABERTA, pendente):** dimensionalidade = 8 intocada; esta Spec só **invoca** a leitura macro (RULE-CF-010) e **compara** o valor devolvido com parâmetro sem número; fórmula/pesos/limiares definitivos **pendentes** (J-001, N-001 ABERTAS; WF-D03 ABERTA). Os limiares-piloto interinos (≥70%, ≥7/9 — INV-03, FATO NORMATIVO) são do **sinal**, não da leitura de contexto, e **não** são usados como limiar "conclusivo" (P-5). [FATO: INV-03; CEE-001 §11; DHR-SPEC008-001 §3 (ii)]
- [x] **CC-04 — Salvaguardas CEE-001 §10/§11:** §10 S1/S5 (roteamento de modelo — a Fase 1 não muda classe de modelo de ninguém: INV-MDC-01), S2 (nunca suprimir por custo diante de evento estruturalmente relevante — RULE-MDC-008 (c)), S4 (= INV-04: custo nunca entra no Conviction Vector — RULE-MDC-008 (d)); §11 (nenhum sinal sai desta Spec; `directional_conflict = true` ⇒ NEUTRO — RULE-MDC-005 (b)). [FATO: CEE-001 v2.0 §10, §11]
- [x] **CC-05 — Complexidade declarada:** CRITICAL · D0–D8 (P-1).
- [x] **CC-06 — SES-001 §59:** N/A — Spec/Plan; Engineering Cards no BUILD (atomic-spec §14). Omissão justificada.
- [x] **CC-07 — SES-001 §60:** N/A (idem); rastreabilidade: ROADMAP §7 → DHR-EUA-E23 → Dossiê → DHR-SPEC008-001 → MMC-001 v1.0 → este Plan.
- [x] **CC-08 — Herança/Delta:** presente (seção abaixo); **pai vertical MMC-001 v1.0** (RULE-HV-01) com tabela de conservação item a item (§2–§7 do MMC no alcance do seu §8.2-bis); INHERITS horizontal por ID+versão; MODIFIED vazio; **REMOVED vazio**; ADDED não contradiz o herdado (RULE-HD-02/RULE-HV-03) — §7-bis Bloco B.
- [x] **CC-09 — Epistemic Check:** nenhum número de limiar, teto, prazo ou taxa (todos INDETERMINADOS — tabela de parâmetros); INDETERMINADO é estado válido com abstenção produtiva (RULE-MET-02); hipótese ≠ fato (o Manager nunca afirma "há oportunidade" nem "houve ruptura" — lê campos e estados publicados).
- [x] **CC-10 — Terminologia concorrente:** seção "Declaração de acepção semântica" (Termos 1–9; "Fase" conforme MMC-001 §1-bis).
- [x] **CC-11 — Classe/Mecanismo por BASpec (RULE-MECH-01):** onze BASpecs **D** e uma **C** (BASpec-MDC-012 — trava E3, justificada pela capacidade que nega: efeito irreversível fora do caminho governado); **nenhuma H/P** (obrigação MMC-001 §3.1.3, parte firme). **Pisos:** despacho E2; transição E2; pedido à Spec de Tempo E2; entrega à Fase 2 E2; livro de bordo E1; aviso/escalada E1; trava E3 (orientação da abertura, ABERTURA §4; atomic-spec §10.2).
- [x] **CC-12 — `PD-xx` (RULE-PD-01):** N/A — não é Spec de especialidade (research §9). Registrado, não supressão silenciosa.

**Disciplinas N8–N17 incidentes:** RULE-EPI-01/02 (campos lidos como publicados; nada promovido a fato), RULE-SEM-01/03 (acepções declaradas), RULE-ONT-01 (nenhuma entidade nova no quadro), RULE-CAU-01 (nenhuma afirmação causal sobre mercado), RULE-UNC-01 (incertezas localizadas — §7-bis Bloco C), RULE-PRB-01 (nenhuma probabilidade), **RULE-DEC-01** (o Manager-Fase-1 não produz decisão material; a entrega à Fase 2 declara-se insumo, não recomendação nem execução — INV-05), RULE-MET-01 (não declarar despacho/registro que não ocorreu), **RULE-MET-02** (abstenção produtiva em todo encerramento por INDETERMINADO). INDETERMINADO é estado válido.

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD / RULE-HV)

```
HERANÇA / DELTA — SPEC-008 (v1.0)

PAI VERTICAL (RULE-HV-01 — ID + VERSÃO baseline):
  - governance/MMC-001 v1.0 (BASELINE — DHR-SPEC008-002; errata R3-m07 in loco, Patch — DHR-SPEC008-003):
      conservação do CONJUNTO das obrigações dos §2–§7 no alcance declarado no MMC-001 §8.2-bis
      (tabela "Conservação do pai" abaixo, item a item); regra de leitura do MMC-001 §1 (inclusive as
      exclusões "NÃO herdado — prevalece X") aplicada por referência

INHERITS (horizontal — referência por ID + VERSÃO baseline; RULE-HD-04; NÃO redefinido):
  - specs/features/SPEC-003 v1.5 (BASELINE — DHR-SPEC003-001): RULE-CF-010 (mecanismo macro invocável; invocação
      2x é do Manager — a 1ª, macro, aqui); campo directional_conflict e veto CF-006 (lidos do resultado, não
      recalculados)
  - canon/CCM-001 (BASELINED — DHR-SPEC003-001): esquema de saída (directional_conflict; valor agregado; status)
      — só lido; nada desta Spec entra no vetor (INV-04)
  - canon/CHM-001 (BASELINED; consolidado sem número de versão): estados EMERGENT→…→ARCHIVED; transições
      DOMINANT→REFUTED e DOMINANT→SUPERSEDED (tabela de transições do CHM-001) — lidas para a Inversão #1
  - specs/features/SPEC-004 v1.2 (BASELINE — DHR-SPEC004-003): RULE-CBP-001 (contrato do objeto: object_id,
      version, domain_state separado de publication_state), RULE-CBP-002 (publica só no próprio workspace),
      RULE-CBP-005 (chave de idempotência), RULE-CBP-006 (ordem total por workspace), RULE-CBP-014 (identidade
      autenticada pelo runtime); RULE-CBP-009 (enum não-hipótese = M-001 ABERTA — não usado)
  - specs/features/SPEC-005 v1.0 (BASELINE — DHR-SPEC005-002): RULE-CEB-001 (envelope), RULE-CEB-003 (cursor/replay), RULE-CEB-004 (consumo
      idempotente), RULE-CEB-006 (at-least-once, retry com teto, dead-letter), RULE-CEB-007 (transporte ≠ fonte
      de verdade), RULE-CEB-008 (quem é invocado e quando = Manager/SPEC-008), RULE-CEB-010 (latência = parâmetro)
  - canon/CEE-001 v2.0 (BASELINED): §9.2, §9.3 (pausa emergencial), §10 S1/S2/S4/S5, §11, §12
  - governance/RULES.md: RULE-BB-001/002/003/004/005; RULE-DEC-01; RULE-MET-01/02; RULE-HV-01..04; RULE-HD-02..04;
      RULE-MECH-01..04; RULE-ECC-07; RULE-ICT-003 (só como divergência registrada — CONF-3)
  - governance/CONFLICT-MAP.md "Inversões contextuais" #1 (HOMOLOGADO 2026-09-20)
  - WORKFLOW.md v2.1 (SOBERANO; só por ID): WF-01..WF-07, WF-K02, WF-K04, WF-T01, WF-T02, WF-A01, WF-A02, WF-A03,
      WF-C01, WF-F01, WF-F02, WF-P01, WF-P02, WF-X03, WF-X04 — com as exclusões do MMC-001 §8.3 (WF-F02 frase
      "implementação no Plan do Manager (SPEC-015)" → CONF-1; WF-K02 parêntese "(SPEC-008/015)" → CONF-5;
      WF-F01 ramos 3 e 5 "reset" → P-12)
  - atomic-spec v1.5: INV-01..INV-07, INV-09, INV-10; §10.2 pisos; §10.3 (Enforcement Contract); ENF-01..08; §10.6 Classe
  - DHR-SPEC008-001 §1 (P-1..P-13, CONF-1..5), §3, §5 — FATO NORMATIVO por ata
  - DHR-DEC-001 (Q-A5, via WF-C01); DHR-SPEC005-002 (EVENT-BUS-001 FECHADA)

CONTEXTO (citado, NÃO herdado — RULE-HD-04): ABERTURA.md (commit 8ea5d9a; não-baseline); research.md e sources/
  (Dossiê; [EXTERNO] = DADO); docs/MATRIZ-WORKFLOW-SPEC.md (não-normativa)

ADDED (delta local — [PROPOSTA]): INV-MDC-01; RULE-MDC-001..011; códigos MDC_*; tabela da FSM do trecho Fase 1
  (D5, com dono por transição); grafo de despacho versão 1 (dado); tabela de parâmetros (valores INDETERMINADOS);
  contrato lógico (cycle_request, dispatch_graph, dispatch_request, cycle_log_entry, phase2_handoff,
  time_request, notice); Fixture M0; interface com a Spec de Tempo (requisito); proposta de errata aditiva

MODIFIED: (vazio) — nenhum texto herdado alterado
REMOVED : (vazio)
```

### Conservação do pai — MMC-001 v1.0, item a item (RULE-HV-01/04; alcance = MMC-001 §8.2-bis)

| Item do MMC-001 | Obrigação (resumo) | Alcance | Evidência nesta Spec |
|---|---|---|---|
| §2.1 / §2.5 | Manager = único componente de orquestração; um só ator lógico; nenhum agente novo | todas | D0; D1 Non-goals; nenhum agente de trading criado (contrato lógico só tem objetos do Manager) |
| §2.2 | Manager não analisa, não formula hipótese, não tem skill de análise técnica | todas | INV-MDC-01 (subs `ANALYSIS_PUBLISH`, `HYPOTHESIS_WRITE`); RULE-MDC-004 (a) (oportunidade = campo lido) |
| §2.3 / §2.4 | componentes absorvidos não reaparecem; "Conviction Engine" = mecanismo invocado | todas | D1; RULE-MDC-005 (a) (invoca o mecanismo da SPEC-003) |
| §2.6 | "Scheduler" = função de despacho do Manager | todas | Acepção, Termo 2 |
| §3 (tabela, sem a coluna Classe) | Fase 1 = Dispatch, mecânica; dona SPEC-008 + Spec de Tempo | todas | cabeçalho; D0 |
| §3.1.1 / §3.1.4 | Fase 1 mecânica/determinística; julgamento leve só nas Fases 0 e 2 | todas | CC-11 (onze D + uma C) |
| §3.1.2 | controle de horário determinístico; gate do alarme nunca é LLM | todas | RULE-MDC-010 (c) (não lê relógio; consome instante registrado da Spec de Tempo) |
| §3.1.3 — obrigação | nenhuma BASpec H/P na Fase 1; se precisar de julgamento, volta a Andraus | SPEC-008/Tempo | D3: zero H/P; §7-bis Bloco A (nenhum ponto exigiu julgamento) |
| §3.2.1 / §3.2.2 | FSM do ciclo de WF-F02; gate nunca é LLM em nenhum trecho | todas | D5 (tabela; guarda D em toda linha do trecho Fase 1; trechos de outros donos declarados "gate determinístico — dono X") |
| §3.2.3 | nenhuma Fase cria/renomeia/remove estado ou transição; seta não escrita só com Andraus | todas | D5 (só estados de WF-F02); encerramentos antes de `EM_RISCO` = DN-1 `[DECISÃO NECESSÁRIA]` |
| §4 Fase 0 → Fase 1 | pedido com campos de WF-01; Fase 1 executa pedido já definido | SPEC-008 (obrig.) | RULE-MDC-001 |
| §4 Fase 1 → Fase 0 (P-12) | só encerrar; Fase 1 não abre ciclo novo | SPEC-008 (obrig.) | RULE-MDC-001 (c); RULE-MDC-007 (d); INV-MDC-01 sub `CYCLE_ORIGINATION` |
| §4 Anti-paradoxo | missão não exige hipótese prévia como insumo único | todas | RULE-MDC-001 (a): o pedido não traz hipótese; hipótese nasce depois do despacho |
| §4 Fase 1 → Fase 2 (CONF-1) | fronteira = entrada em `EM_SÍNTESE` | SPEC-008 (obrig.) | RULE-MDC-011; D5 (última transição do trecho) |
| §4 Fase 2 → Risco | TMP interno; fluxo unidirecional | todas | D1 Non-goals; INV-MDC-01 sub `TMP_ASSEMBLY` |
| §4 Manager × SPEC-003 | invoca 2x; macro aqui; não redefine cálculo | todas | RULE-MDC-005 |
| §4 Fase 2 × SPEC-016 | TMP = SPEC-016 | todas | D1 Non-goals |
| §4 Manager × agentes analíticos | só via Blackboard; publica só no próprio espaço; avisos pelo Event Bus | todas | RULE-MDC-003; EC-MDC-002 |
| §4 Manager × Spec de Tempo (CONF-5) | abrir/fechar Killzone na Spec de Tempo; ator = Manager | SPEC-008 (obrig.) | "Interface com a Spec de Tempo" |
| §5.1–§5.5 | não executa; recomendação declarada; alarme = gatilho de análise; pré-programada até a fila de revisão; overtrading = Bot | todas | INV-MDC-01 (subs `ORDER_EMISSION`, `SIGNAL_PACKAGE_ASSEMBLY`); RULE-MDC-011 (b) (WF-K04: o modo segue adiante); RULE-MDC-006 (b) |
| §5.6 | dono da montagem do Signal Package **não** fixado | não-atribuição | esta Spec não monta nem atribui (INV-MDC-01) |
| §6.1 | CEE §10 S2 literal; vale onde o Manager decide despachar | todas | RULE-MDC-008 (c) |
| §6.2 | Inversão #1; mecânica do gatilho nesta Spec | todas | RULE-MDC-004 (d); DN-2 (parte "despertar ciclo") |
| §6.3 | custo nunca no Conviction Vector | todas | RULE-MDC-008 (d) |
| §6.4 / §6.4-a | S1/S5 literais; Manager não altera classe de modelo de outro componente; só pausa emergencial | todas | INV-MDC-01 sub `MODEL_CLASS_CHANGE` |
| §6.5 | ordem dos 4Es | todas | "Critério 4Es" de cada BASpec; Plan — 4Es e latência |
| §6.6 — parada | parada por gasto só por Andraus, nunca automática | todas | RULE-MDC-009 (d); INV-MDC-01 sub `AUTO_COST_PAUSE` |
| §6.6 — orçamento | orçamento do ciclo avisa e escala; nunca pula etapa relevante | SPEC-008/Tempo | RULE-MDC-008 (b)(c) |
| §7 | INV-01..05, 07, 09, 10; CHM-001; CEE §11 — consumidos, não redefinidos | todas | CC-01..CC-04 |
| §1 / §1-bis | regra de leitura e vocabulário "Fase" | todas (leitura) | Acepção, Termo 1 |
| §10 | decisões abertas lembradas, sem obrigação nova | todas | "Decisões abertas incidentes" |

---

## Declaração de acepção semântica (RULE-SEM-01 — CC-10)

> **Termo 1 — "Fase":** sem qualificador = **Fase do Manager** (0 Mission Lifecycle · 1 Dispatch · 2 Conviction — ADR §4.3); "passo WF-xx" = passo do pipeline (WF-02/WF-03 chamam de "Fase 1" o trabalho dos agentes analíticos, que **não** é trabalho do Manager-Fase-1); "FASE" maiúscula = ROADMAP. [FATO: MMC-001 §1-bis]
> **Termo 2 — "despachar" × "chamar":** **despachar** = publicar um pedido de despacho no **próprio** workspace do Manager no Blackboard, avisado pelo Event Bus (RULE-BB-001/005; RULE-CEB-008); **chamar diretamente** um agente analítico é proibido. "Scheduler"/"Cognitive Scheduler" em textos antigos = esta função do Manager (MMC-001 §2.6).
> **Termo 3 — "agente":** sempre qualificado — **agente analítico** (Agente de Trading: Estrutural/Elliott, Institucional/SMC, Operacional/ICT — GLOSSARIO §1-bis/§2); "Agente de Risco" = FASE RISK. O Manager não é agente analítico.
> **Termo 4 — "leitura macro" × "convicção global" × "conclusiva":** **leitura macro** = 1ª das duas invocações do mecanismo do CCM-001 sobre o subconjunto estrutural+institucional (WF-C01; RULE-CF-010); **convicção global** = 2ª leitura, da Fase 2 (fora). **Conclusiva** = o valor agregado devolvido pela leitura macro é **≥** o parâmetro `macro_conclusive_threshold` (comparação D); **não** é o gate de sinal (≥70%/≥7/9, INV-03), que é da Fase 2/Risco.
> **Termo 5 — "oportunidade":** campo **publicado** pelo agente Estrutural (P-8), com valores `SIM | NAO`; ausente ⇒ INDETERMINADO. O Manager **nunca** decide se há oportunidade.
> **Termo 6 — "orçamento" × "teto":** **teto** = limite de controle de laço (passos, voltas, falhas seguidas, prazo por etapa) — estouro encerra a etapa com motivo; **orçamento de custo** = medida de gasto do ciclo — estouro **avisa e escala**, nunca corta etapa (P-7). Nenhum dos dois é convicção (INV-04).
> **Termo 7 — "encerrar" × "reset":** **encerrar** = o ciclo deixa de aceitar evento, com o motivo gravado no livro de bordo (P-12); **"reset"** (WF-F01 ramos 3/5) **não** é ação desta Spec (não mapeia em transição listada — MMC-001 §8.3).
> **Termo 8 — "alarme" × "ordem":** alarme = gatilho de **análise** (WF-A01), objeto da Spec de Tempo; nunca ordem (INV-05). "Killzone" = janela de tempo ICT no relógio de Nova York (WF-K01) ≠ sessão de pregão.
> **Termo 9 — "livro de bordo" × "estado do objeto no quadro":** **livro de bordo** = registro só-inserção do ciclo, próprio do Manager (P-6); **não** é `domain_state`/`publication_state` de objeto do Blackboard (SPEC-004 RULE-CBP-001/009; M-001 ABERTA).
> [FATO: RULE-SEM-01/03/04; GLOSSARIO; MMC-001 §1-bis, §2.6; WF-A01; WF-C01]

---

## Conformidade com o `WORKFLOW.md` v2.1 (RULE-ECC-05 — incide; citação só por ID)

| ID | Como esta Spec se conforma | Observação |
|---|---|---|
| WF-01 / WF-K04 | consome o pedido de ciclo com os campos de WF-01 e o modo assistida/pré-programada (RULE-MDC-001) | não decide tipo de missão (Fase 0) |
| WF-02 / WF-03 | despacha Estrutural; Institucional **só** com oportunidade = SIM (RULE-MDC-004 (a)) | Fibonacci/Fractal sem passo (P-11) |
| WF-04 / WF-C01 | 1ª invocação (macro) + comparação "conclusiva" com parâmetro; se conclusiva, pede o alarme (RULE-MDC-005/006) | WF-D03 ABERTA — não tocada |
| WF-05 / WF-A02 | despacha Operacional **só** com `TRIGGERED` dentro da janela (RULE-MDC-004 (b)) | CONF-3; RULE-ICT-003 divergente, registrada |
| WF-T01 / WF-T02 | TFs do pedido; alinhamento obrigatório conferido por igualdade de direção (RULE-MDC-006 (d)) | CONF-4 |
| WF-A01 / WF-A03 | campos do alarme copiados da hipótese de contexto; morte do alarme = Spec de Tempo | P-8; CONF-5 |
| WF-F01 | ramos 1, 2, 3, 5 = encerramentos do trecho Fase 1; ramo 4 = RISK-SPEC; ramo 6 fora (P-13) | "reset" não herdado (P-12) |
| WF-F02 | tabela inteira em D5, dono por trecho (CONF-1); estados sem acréscimo | frase "SPEC-015" não herdada |
| WF-K01..K03 / WF-R02 / WF-R03 | **não** especificados aqui — Spec de Tempo | CONF-5; BL-026 |
| WF-P01 / WF-P02 | um ciclo por (ativo, missão), isolado; parâmetros por ativo versionados | heat/correlação = RISK-SPEC |
| WF-X03 / WF-X04 | fluxo unidirecional; overtrading = Bot | fora |
| WF-D03 | **ABERTA** — esta Spec só invoca; não define fórmula | CONS-01 |

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide** (o Manager não é Spec de especialidade de escola — ADR §2.5; research §9). Nenhum `PD-xx`.

---

## D0 — Missão (Intenção)

A SPEC-008 especifica **como o Manager, na Fase 1, conduz um ciclo de análise de um ativo do pedido até a entrega à Fase 2**: aceitar ou recusar o pedido; despachar, em ordem fixa que respeita a hierarquia, os agentes analíticos que a condição de cada etapa libera; pedir a leitura de convicção de contexto e compará-la com um limiar declarado; pedir o alarme de preço com os dados publicados; liberar o analista operacional só quando o alarme dispara dentro da Killzone; conferir o alinhamento de direção; conduzir a máquina de estados do ciclo no seu trecho; respeitar tetos e avisar sem cortar análise por custo; parar, aguardar, escalar e encerrar com motivo nomeado; registrar tudo de forma reconstruível — e fazê-lo **sem poder** analisar mercado, mexer em hipótese, calcular convicção, mudar modelo, montar TMP/Signal Package ou emitir ordem.

## D1 — Escopo e Non-goals

### Dentro do escopo (S1–S12 da ABERTURA §2, como homologada)
- **S1** pedido de ciclo e isolamento (RULE-MDC-001) · **S2** grafo e ordem (RULE-MDC-002) · **S3** despacho via quadro e espera (RULE-MDC-003) · **S4** ativação progressiva + Inversão #1 (RULE-MDC-004) · **S5** leitura macro, "conclusiva", NEUTRO (RULE-MDC-005) · **S6** pedido de alarme, Operacional, alinhamento (RULE-MDC-006) · **S7** FSM do ciclo (RULE-MDC-007; D5) · **S8** tetos e orçamento (RULE-MDC-008) · **S9** paradas e escalada (RULE-MDC-009) · **S10** livro de bordo e retomada (RULE-MDC-010) · **S11** entrega à Fase 2 (RULE-MDC-011) · **S12** trava constitutiva (INV-MDC-01).

### Fora do escopo (Non-goals)
| Item | Motivo | Dono |
|---|---|---|
| Relógio, fuso, Killzone (abrir/fechar, pré-aviso WF-K02), objeto e FSM do alarme, mercado fechado | P-2; CONF-5 | **Spec de Tempo** (só a interface aqui) |
| Tipo de missão, portfólio, Campanha, Plano B; quantas vezes tentar de novo | Fase 0; **SPEC-015-SCOPE ABERTA** | **SPEC-015** |
| Arbitragem, convicção global, decisão de envio, pacote risco-retorno, TMP; transições a partir de `EM_SÍNTESE` | Fase 2; CONF-1 | **SPEC-014** / **SPEC-016** |
| Transições em `EM_RISCO`; ramo 4 (veto) | FASE RISK (não autorizada) | **RISK-SPEC** |
| Ramo 6 de WF-F01 (reentrada após stop) | **P-13 = decidir depois** | SPEC-015/014 (abertura) |
| Fórmula, pesos, limiares definitivos; valor do limiar "conclusivo" | **J-001/N-001 ABERTAS**; WF-D03 ABERTA | SPEC-003/CCM-001; calibração (BL-032) |
| Esquema e mecanismo de persistência do livro de bordo | **G-001 ABERTA** | **SPEC-009** |
| Estados de objeto não-hipótese no quadro | **M-001 ABERTA** | SPEC-004 / Andraus |
| Transporte de avisos | BASELINE | **SPEC-005** |
| Análise, hipótese, setup; campo "oportunidade" | INV-02; RULE-BB-005 | **SPEC-010..013** (requisito `[INFERÊNCIA]`) |
| Posição de Fibonacci/Fractal no roteiro | **P-11 = decidir depois** | abertura SPEC-010/011 |
| R:R, sizing, heat; overtrading; execução | WF-X01..X05; INV-05 | RISK-SPEC; Bot Trade Finance |
| Formalização de Skills | I-001 fechada; corte na SPEC-025 | SPEC-025 |
| Telemetria/observabilidade | BL-036..042 | SPEC-040/041 |
| Motor (biblioteca de FSM, fila, banco) | ROADMAP §22 | BUILD |
| Coordenação com "Cognitive Orchestrator" | possível dupla posse (research CF-5) | SPEC-023 |

---

## Pré-requisitos para o primeiro ciclo que chegue à Fase 2 — em linguagem de trader

> **Por que este quadro:** enquanto algum item abaixo faltar, o comportamento correto é **recusar o pedido** ou **encerrar o ciclo registrado, dizendo o que falta** (abstenção produtiva — RULE-MET-02). Não é defeito.

| Ordem | O que precisa existir | Nota técnica | Sem isso |
|---|---|---|---|
| 0 | Tabela de tetos e prazos **preenchida** para o tipo de missão | parâmetros `max_steps_per_cycle`, `max_rounds_per_agent`, `max_consecutive_failures`, `stage_deadline` (RULE-MDC-008 (a)) | pedido recusado `MDC_LIMITS_NOT_CONFIGURED` (laço sem teto é proibido) |
| 1 | O analista de Elliott **publicar o campo "oportunidade"** | requisito `[INFERÊNCIA]` à SPEC-010 (P-8) | ciclo encerrado `MDC_OPPORTUNITY_UNDETERMINED` |
| 2 | O **limiar "conclusivo"** ser preenchido | J-001/N-001 ABERTAS (P-5) | ciclo encerrado `MDC_MACRO_NOT_CONCLUSIVE` (sub `MDC_MACRO_THRESHOLD_UNSET`); alarme não armado |
| 3 | A **Spec de Tempo** existir (armar alarme, timers, instante registrado) | Plan próprio, depois deste | pedido recusado `MDC_TIME_SERVICE_UNAVAILABLE` (sem timer registrado, o prazo de etapa não é executável e a espera não teria fim) |
| 4 | O analista ICT publicar setup com direção, TF e `parent_id` | requisito `[INFERÊNCIA]` à SPEC-013 | ciclo encerrado `MDC_SETUP_MISALIGNED` |

---

## D2 — Regras (FONTE ÚNICA de cada obrigação)

> **Etiqueta:** INV-MDC-01 e RULE-MDC-001..011 são **[PROPOSTA]** — normativas só na homologação de Andraus + registro do Controlador (RULE-HG-02). Os fundamentos citados são FATO NORMATIVO (baselines, atas, WORKFLOW). Cada regra é definida **aqui uma única vez**; EARS, BASpecs, D4–D8, EC e `checks.md` só a referenciam por ID. Códigos: só os da §D3.1.

```
INV-MDC-01: TRAVA CONSTITUTIVA DO MANAGER-FASE-1 (Classe C, E3, fail-closed).
            O Manager, ao exercer a Fase 1, tem SÓ estas capacidades (lista FECHADA — allowlist):
            (1) LER qualquer workspace do Blackboard (RULE-BB-002); (2) PUBLICAR no PRÓPRIO workspace só
            `dispatch_request` e `phase2_handoff` (RULE-CBP-002); (3) GRAVAR no PRÓPRIO livro de bordo,
            só-inserção (RULE-MDC-010); (4) INVOCAR o mecanismo de leitura macro do CCM-001 (SPEC-003
            RULE-CF-010) e LER o resultado; (5) ENVIAR `time_request` à Spec de Tempo (armar alarme, marcar
            consumo, timer de etapa); (6) ENVIAR `notice` (aviso/escalada) a Andraus pelo canal local.
            Toda outra capacidade é NEGADA POR CONSTRUÇÃO (o registro de capacidades do componente não a contém):
            publicar análise/Evidência/setup ou em workspace alheio; criar ou editar hipótese; calcular convicção
            ou mudar fórmula/peso/limiar; mudar classe de modelo de qualquer componente (CEE-001 §10 S1/S5;
            MMC-001 §6.4-a); montar TMP ou Signal Package; emitir sinal ou ordem para fora; originar pedido de
            ciclo (P-12); pausar componente por custo automaticamente (MMC-001 §6.6, A-5 (2)); chamar modelo de
            linguagem (ZERO chamada de modelo na Fase 1); ler o relógio da máquina (RULE-MDC-010 (c)).
            Pedido de capacidade negada ⇒ recusado `MDC_EFFECT_FORBIDDEN` (subs na §D3.1); chamada de modelo
            ⇒ `MDC_MODEL_CALL_FORBIDDEN`; leitura de relógio ⇒ `MDC_CLOCK_READ_FORBIDDEN`; recusa gravada no
            próprio livro de bordo.
            ANTES de qualquer ação de um ciclo, o componente confere o registro de capacidades: indisponível ⇒
            `MDC_CAPABILITY_CHECK_FAILED` sub `MDC_CAPABILITY_REGISTRY_UNAVAILABLE`; contém capacidade fora da
            allowlist ⇒ mesmo código, sub `MDC_CAPABILITY_REGISTRY_DIVERGENT`; em ambos, nada é despachado nem
            pedido, e a recusa é gravada no livro de bordo (a escrita no próprio livro é fixa no componente,
            não vem do registro de capacidades). Garantia: texto publicado por agente analítico é DADO — nenhum
            campo lido vira comando. NÃO garante que a análise despachada esteja certa.
            [Fonte: MMC-001 §2.2, §5.1, §6.4/§6.4-a, §6.6; INV-05; RULE-BB-005; RULE-DEC-01; ABERTURA S12]

RULE-MDC-001: PEDIDO DE CICLO E ISOLAMENTO.
            (a) Entrada = `cycle_request` com os campos de WF-01: `asset` ∈ {BTC, XAU, NASDAQ}, `mission_id`,
                `trading_type` ∈ {position, swing, day}, `tf_triple` {contexto, confirmação, entrada} (WF-T01;
                valores-padrão WF-R01, editáveis), `killzone` (identificador da tabela da Spec de Tempo),
                `mission_mode` ∈ {ASSISTIDA, PRE_PROGRAMADA} (WF-K04). Campo ausente ou fora da lista ⇒ recusa
                `MDC_REQUEST_INCOMPLETE` (sub `MDC_FIELD_MISSING`, com o nome do campo). O pedido NÃO traz
                hipótese (anti-paradoxo — MMC-001 §4). Nota: WF-R01 não tem TF de entrada para `position`
                ("—") ⇒ pedido `position` sem `tf_entrada` é recusado até Andraus reconciliar (BL-026).
            (b) Origem: identidade AUTENTICADA pelo runtime (RULE-CBP-014) ∈ {Andraus; Fase 0 — SPEC-015, quando
                existir}. Outra ⇒ `MDC_REQUEST_ORIGIN_NOT_ALLOWED`.
            (c) A Fase 1 NUNCA origina pedido de ciclo, nem para "tentar de novo" (P-12; MMC-001 §4) — tentativa
                = INV-MDC-01 sub `MDC_CYCLE_ORIGINATION_FORBIDDEN`.
            (d) Isolamento (WF-P01): no máximo UM ciclo não encerrado por chave (`asset`, `mission_id`); segundo
                pedido ⇒ `MDC_CYCLE_ALREADY_ACTIVE`. Cada ciclo tem `cycle_id` próprio; contadores, tetos, timers e
                livro de bordo são por `cycle_id`; ciclos diferentes nunca compartilham estado.
            (e) Pré-condições operacionais, conferidas na entrada: tabela de parâmetros preenchida para o
                `trading_type` (RULE-MDC-008 (a)) — senão `MDC_LIMITS_NOT_CONFIGURED`; versão registrada do grafo
                (RULE-MDC-002 (f)) — senão `MDC_GRAPH_VERSION_UNREGISTERED`; serviço de tempo disponível para
                timers — senão `MDC_TIME_SERVICE_UNAVAILABLE`; livro de bordo disponível — senão
                `MDC_CYCLE_RECORD_UNAVAILABLE` (RULE-MDC-010 (b)). Ordem de conferência: D4.1.
            (f) Aceito ⇒ grava a abertura (com `graph_version` e `limits_version` FIXADAS para o ciclo inteiro) e
                o ciclo entra em `AGUARDANDO` (D5, linha F01).
            [Fonte: WF-01, WF-T01, WF-K04, WF-P01; MMC-001 §4; DHR-SPEC008-001 P-12; RULE-CBP-014]

RULE-MDC-002: GRAFO DE DESPACHO VERSIONADO.
            (a) O roteiro é DADO versionado `dispatch_graph@version`: nós {node_id, papel, posto INV-01} e arestas
                com condição de LISTA FECHADA {`OPORTUNIDADE_SIM`, `MACRO_CONCLUSIVA_E_DISPARO_NA_JANELA`}.
                Versão 1: ESTRUTURAL (Elliott, posto 1) →[OPORTUNIDADE_SIM] INSTITUCIONAL (SMC, posto 4)
                →[MACRO_CONCLUSIVA_E_DISPARO_NA_JANELA] OPERACIONAL (ICT, posto 5). Postos de INV-01: Elliott 1,
                Fibonacci 2, Fractal 3, SMC 4, ICT 5.
            (b) Grafo com ciclo dirigido ⇒ versão NÃO registrável, `MDC_GRAPH_CYCLIC` (ordem topológica só existe
                sem ciclo — research §3.2).
            (c) Para toda aresta u→v: posto(u) < posto(v); nó sem posto ou aresta que viola ⇒ versão NÃO
                registrável, `MDC_GRAPH_HIERARCHY_VIOLATION` (CC-01).
            (d) Desempate: nós liberados no mesmo passo são despachados em ordem crescente de (posto, node_id).
            (e) Fibonacci/Fractal: SEM nó na versão 1 (P-11 = decidir depois). Acrescentá-los = nova versão do
                dado, registrada por ato de Andraus, sem reescrever esta Spec; condição nova de aresta fora da
                lista fechada exige errata.
            (f) Só Andraus registra versão do grafo (a versão 1 = DN-3); um ciclo usa a versão fixada na abertura.
            (g) O Manager só despacha nós do grafo; nunca inventa nó, ordem ou condição.
            [Fonte: INV-01; CC-01; WF-02/03/05; P-11; research §3.2 (SRC-AIRFLOW-DAG-01, SRC-TOPO-01 [EXTERNO])]

RULE-MDC-003: DESPACHO VIA QUADRO E ESPERA.
            (a) Despachar = publicar `dispatch_request` no PRÓPRIO workspace (RULE-CBP-002) com {`cycle_id`,
                `node_id`, `stage_seq`, `dispatch_key` = H(`cycle_id`, `node_id`, `stage_seq`) como chave de
                idempotência (RULE-CBP-005), referências dos insumos publicados, `tf`, `max_rounds`,
                `graph_version`}, avisado pelo Event Bus (SPEC-005). NUNCA chamada direta (RULE-BB-001/005).
            (b) Entrada do livro de bordo ANTES da publicação (RULE-MDC-010 (b)).
            (c) Espera síncrona por etapa: a etapa seguinte só depois da publicação da anterior; cada espera tem
                timer pedido à Spec de Tempo com o `stage_deadline` do parâmetro; timer disparado ⇒ encerramento
                `MDC_STAGE_DEADLINE_EXCEEDED`.
            (d) Só é consumida como resposta a publicação do agente analítico do nó despachado: identidade
                autenticada (RULE-CBP-014) cujo papel = papel do nó, referindo o `cycle_id` e o `dispatch_key`.
                Outra ⇒ `MDC_EVENT_FOREIGN_CYCLE` (não consumida; registrada). Notificação sem o envelope mínimo
                da SPEC-005 ⇒ `MDC_EVENT_ENVELOPE_INVALID` (não consumida; registrada).
            (e) Idempotência: o mesmo `dispatch_key` nunca gera segunda publicação (duplicata = entrada
                `MDC_DUPLICATE_IGNORED`, sem efeito); evento já consumido (mesmo `event_id`) não é reprocessado
                (RULE-CEB-004).
            (f) Falha ao publicar o pedido ou erro do agente analítico conta como falha seguida do nó; novas
                tentativas limitadas por `max_consecutive_failures`; estouro ⇒ RULE-MDC-008 (b).
            (g) A ordem de consumo é a do log do Blackboard (RULE-CBP-006); notificação perdida ou atrasada é
                recuperada por replay a partir do cursor (RULE-CEB-003/007) — transporte ≠ verdade.
            [Fonte: RULE-BB-001/002/005; SPEC-004 RULE-CBP-002/005/006/014; SPEC-005 RULE-CEB-001/003/004/007/008;
             research §3.2 (SRC-ANTH-MULTI-01 [EXTERNO] — despacho síncrono)]

RULE-MDC-004: ATIVAÇÃO PROGRESSIVA E INVERSÃO #1.
            (a) INSTITUCIONAL só se a publicação do ESTRUTURAL traz `opportunity = SIM`. `NAO` ⇒ ramo 1 de WF-F01:
                encerramento `MDC_NO_OPPORTUNITY`. Ausente ou fora de {SIM, NAO} ⇒ encerramento
                `MDC_OPPORTUNITY_UNDETERMINED`, com abstenção (RULE-MDC-009 (b)). O Manager nunca decide se há
                oportunidade (P-8).
            (b) OPERACIONAL só com o evento `ALARM_TRIGGERED` da Spec de Tempo, para o alarme DESTE ciclo, com
                `inside_killzone = true` e instante registrado. `inside_killzone` ≠ true ⇒ evento recusado
                `MDC_TRIGGER_OUTSIDE_WINDOW`, sem transição (WF-A02; WF-05; CONF-3).
            (c) Nenhum nó é despachado por "relevância" ou preferência — só pela condição da aresta (RULE-MDC-002).
            (d) Inversão #1 — detecção por regra fixa: publicação, em qualquer workspace, de nova versão de
                objeto-hipótese cuja versão anterior (`supersedes`) tinha `domain_state` = DOMINANT e a nova tem
                REFUTED ou SUPERSEDED (transições do CHM-001) ⇒ entrada `MDC_DOMINANT_RUPTURE_DETECTED` + aviso a
                Andraus/Fase 0 com ativo e referência da hipótese (EC-MDC-007). "Independente do custo" é
                garantido por construção: nenhuma regra desta Spec suprime etapa por custo (RULE-MDC-008 (c)).
                ABRIR um ciclo completo por causa da ruptura = [DECISÃO NECESSÁRIA] DN-2 (a Fase 1 não origina
                ciclo — RULE-MDC-001 (c)). Se a hipótese rompida é a de contexto de um ciclo ativo, o cancelamento
                do alarme é da Spec de Tempo (WF-A03) e chega como `ALARM_CANCELLED` (D5, F15).
            [Fonte: WF-03, WF-05, WF-A02, WF-A03; CONFLICT-MAP Inversão #1; CHM-001 (transições); P-8; CONF-3;
             leitura do evento da Inversão = [INFERÊNCIA] (ABERTURA S4; research L-8), sem novo tipo de evento]

RULE-MDC-005: LEITURA MACRO, "CONCLUSIVA" E NEUTRO.
            (a) Depois da publicação do INSTITUCIONAL, o Manager invoca UMA vez o mecanismo do CCM-001 sobre o
                subconjunto estrutural+institucional (RULE-CF-010; WF-C01), passando as referências das duas
                publicações. Não calcula, não pesa, não arbitra. Segunda invocação macro no mesmo ciclo ⇒ recusada
                `MDC_MACRO_ALREADY_INVOKED` (2x por ciclo = 1 aqui + 1 na Fase 2).
            (b) Resultado com `directional_conflict = true` ⇒ NEUTRO: ramo 2 de WF-F01, encerramento
                `MDC_DIRECTIONAL_CONFLICT_NEUTRAL` (AGENTS.md §6 item 4; CEE-001 §11). O conflito é conferido ANTES
                do limiar e é LIDO do resultado (veto CF-006 da SPEC-003), nunca recalculado.
            (c) Conclusiva ⇔ θ = `macro_conclusive_threshold` (parâmetro por ativo, WF-P02) está preenchido ∧ o
                valor agregado devolvido não é INDETERMINADO ∧ valor ≥ θ. Senão ⇒ encerramento
                `MDC_MACRO_NOT_CONCLUSIVE` com sub `MDC_MACRO_THRESHOLD_UNSET` | `MDC_MACRO_READING_UNDETERMINED` |
                `MDC_MACRO_BELOW_THRESHOLD`; o alarme NÃO é pedido (P-5). θ não tem número aqui (J-001/N-001
                ABERTAS); os limiares-piloto do sinal (INV-03) NÃO são θ.
            (d) "Valor agregado da leitura macro" = [INFERÊNCIA] o campo agregado do esquema do CCM-001 calculado
                sobre o subconjunto (RULE-CF-010); o nome exato é lido do contrato da SPEC-003 na construção, sem
                redefini-lo. Resultado sem valor agregado ou sem `directional_conflict` ⇒ INDETERMINADO ⇒ (c).
            (e) Mecanismo indisponível ou com erro ⇒ falha seguida (RULE-MDC-003 (f)).
            (f) Conclusiva ⇒ `AGUARDANDO` → `CONTEXTO_FORMADO` (D5, F07).
            [Fonte: WF-04, WF-C01; RULE-CF-010; CCM-001 (esquema de saída); AGENTS.md §6 item 4; P-5; CONF-2;
             DHR-SPEC008-001 §3 (ii)]

RULE-MDC-006: ALARME, OPERACIONAL E ALINHAMENTO.
            (a) Em `CONTEXTO_FORMADO`, hipótese de contexto = a hipótese PRIMÁRIA referida na publicação do
                ESTRUTURAL (só Elliott cria primária — AGENTS.md §6 item 2). Elegível ⇔ `domain_state` ∈ {ACTIVE,
                DOMINANT} (RULES.md RULE-BB-003, texto vigente: "Hipótese só é base de decisão em ACTIVE ou
                DOMINANT"). Senão ⇒ encerramento `MDC_ORIGIN_HYPOTHESIS_NOT_ELIGIBLE`.
            (b) Pede à Spec de Tempo `ARM_ALARM` com os campos de WF-A01 COPIADOS da publicação (nível, direção,
                condição de disparo, validade, nível de invalidação, condição de cancelamento) + `parent_id` = a
                hipótese de contexto + `cycle_id` + `killzone` do pedido. Campo ausente ⇒ nada é pedido;
                encerramento `MDC_ALARM_FIELDS_INCOMPLETE`. O Manager nunca calcula nem preenche campo (P-8). O
                alarme é gatilho de ANÁLISE, nunca ordem (WF-A01; INV-05).
            (c) `ALARM_ARMED` do alarme pedido ⇒ `CONTEXTO_FORMADO` → `ARMADO`; `ALARM_TRIGGERED` válido
                (RULE-MDC-004 (b)) ⇒ `ARMADO` → `ATIVADO` + despacho do OPERACIONAL com `tf` = `tf_entrada`.
            (d) Alinhamento (WF-T02; CONF-4): o setup publicado é aceito ⇔ `parent_id` = hipótese de contexto ∧
                direção(setup) = direção(hipótese de contexto) ∧ `tf`(setup) = `tf_entrada` ∧ `tf_entrada` ≠
                `tf_contexto` (WF-05). Falha ⇒ ramo 3 de WF-F01: encerramento `MDC_SETUP_MISALIGNED` (subs
                `DIRECTION_MISMATCH` | `DIRECTION_UNDETERMINED` | `TF_INVALID` | `PARENT_MISMATCH`) + pedido
                `MARK_CONSUMED` à Spec de Tempo (P-12: o alarme termina "usado").
            (e) Publicação do OPERACIONAL que seja objeto-hipótese ⇒ NÃO consumida, `MDC_ICT_HYPOTHESIS_REJECTED`,
                sem transição (INV-02); a espera continua até o prazo.
            (f) Setup aceito ⇒ `MARK_CONSUMED` + `ATIVADO` → `EM_SÍNTESE` (RULE-MDC-011).
            (g) `ALARM_EXPIRED` ⇒ ramo 5: encerramento `MDC_ALARM_EXPIRED`; `ALARM_CANCELLED` ⇒ encerramento
                `MDC_ALARM_CANCELLED`. Nenhum rearme, nenhuma volta a `ARMADO` (P-12).
            [Fonte: WF-04, WF-05, WF-T02, WF-A01..A03, WF-F01; AGENTS.md §6 itens 2–3; INV-02; P-8; P-12; CONF-4]

RULE-MDC-007: MÁQUINA DE ESTADOS DO CICLO (trecho Fase 1).
            (a) Estados = exatamente os de WF-F02. A TABELA de D5 é a fonte única: cada linha = estado × evento ×
                guarda → próximo estado | encerramento, com ação, código e dono (CONF-1).
            (b) Par (estado, evento) não listado ⇒ sem transição, entrada `MDC_TRANSITION_NOT_LISTED`.
            (c) A Fase 1 executa só as linhas de dono SPEC-008 (da abertura até a ENTRADA em `EM_SÍNTESE`); as
                demais estão listadas para completude e são executadas por seus donos com gate determinístico
                (MMC-001 §3.2.2).
            (d) ENCERRAMENTO antes de `EM_RISCO` (linhas marcadas "ENC" em D5): grava `cycle_closed` {motivo
                (código), ramo de WF-F01 quando houver, estado no momento, abstenção quando INDETERMINADO}; depois
                disso nenhum evento do ciclo é aceito (`MDC_CYCLE_CLOSED`). Encerramento NÃO é estado novo: é
                ausência de próxima transição + registro ("ciclo termina registrado" — P-12). O RÓTULO FINAL de
                WF-F02 (`RECUSADO` ou `EXPIRADO`) de cada encerramento = [DECISÃO NECESSÁRIA] DN-1; até a decisão,
                `wf_f02_final_label` = AUSENTE e a Fase 1 não grava transição para estado final. Encerramento em
                `ATIVADO` (alarme já disparado) pede `MARK_CONSUMED` à Spec de Tempo (P-12: termina "usado");
                em `ARMADO`, nenhum pedido ao alarme (requisito T-3 à Spec de Tempo).
            (e) Nenhuma seta de volta, nenhum rearme, nenhum ciclo aberto pela Fase 1 (P-12; MMC-001 §3.2.3).
            (f) Toda guarda é comparação de campos publicados ou registrados; o gate nunca é modelo (ENF-03).
            [Fonte: WF-F01, WF-F02; MMC-001 §3.2; CONF-1; P-12; research §3.3 (SRC-SCXML-01 [EXTERNO] — tabela fechada)]

RULE-MDC-008: TETOS E ORÇAMENTO.
            (a) Tabela `cycle_limits@version` por `trading_type` × etapa: `max_steps_per_cycle`,
                `max_rounds_per_agent` (repassado no `dispatch_request`; a ele se referem os pedidos de orçamento
                da SPEC-007/048, como `max_retrieval_rounds`), `max_consecutive_failures` por nó/mecanismo,
                `stage_deadline`. Valores INDETERMINADOS (CC-09). Sem valor ⇒ pedido recusado
                `MDC_LIMITS_NOT_CONFIGURED` — laço sem teto é proibido (desligar o teto: REJEITADO, research §3.5).
            (b) Estouro de teto de controle ⇒ encerramento `MDC_LIMIT_EXCEEDED` (sub `STEPS` | `ROUNDS` |
                `FAILURES`) + aviso; a contagem vive no livro de bordo do ciclo.
            (c) Orçamento de custo `cost_budget` (parâmetro, INDETERMINADO): estouro ⇒ `MDC_COST_BUDGET_EXCEEDED`
                = aviso + escalada a Andraus, SEM transição e SEM pular ou suprimir etapa. Nenhuma regra desta Spec
                usa custo como condição de despacho (CEE-001 §10 S2, transcrito no MMC-001 §6.1).
            (d) Custo e contagens vivem no livro de bordo; NUNCA entram no Conviction Vector nem são passados ao
                mecanismo do CCM-001 (INV-04 = CEE-001 §10 S4).
            (e) Custo não medido (telemetria ausente — SPEC-040) ⇒ orçamento INDETERMINADO: nenhum aviso de custo
                e nada é cortado.
            [Fonte: CEE-001 §10 S2/S4; MMC-001 §6.1, §6.3, §6.6; P-7; research §3.5 (SRC-OAI-MAXTURNS-01,
             SRC-LGRAPH-RECUR-01, SRC-CB-01 [EXTERNO])]

RULE-MDC-009: PARAR, AGUARDAR, ESCALAR, ENCERRAR.
            (a) Toda parada tem motivo nomeado (código da §D3.1).
            (b) Encerramento por INDETERMINADO grava `abstention` {o que é incerto; o que afeta; sob qual condição
                muda; que informação o reduziria} (RULE-MET-02).
            (c) Escalada a Andraus = `notice` (registro + aviso); nunca decide por ele.
            (d) Parada por gasto só por COMANDO de Andraus com identidade autenticada (MMC-001 §6.6, A-5 (2)):
                aceito ⇒ encerramento `MDC_STOP_BY_ANDRAUS`; comando de outra identidade ou não autenticado ⇒
                `MDC_STOP_COMMAND_NOT_AUTHENTICATED`, nada para. Pausa automática por custo = INV-MDC-01. Mecanismo
                de autenticação = BUILD (princípio DHR-SPEC007-007; mecanismo ABERTO).
            (e) Aguardar = manter o estado até evento ou timer; nunca espera sem timer (RULE-MDC-003 (c)).
            [Fonte: RULE-MET-02; MMC-001 §6.6; P-7; ABERTURA S9]

RULE-MDC-010: LIVRO DE BORDO DO CICLO.
            (a) Só-inserção, por ciclo (INV-07). Entrada: `cycle_id`, `log_seq`, `entry_type`, `rule_id`,
                `graph_version`, `limits_version`, `causation_event_id`, `recorded_instant`, `from_state`,
                `to_state` | —, `code` | —, `refs`.
            (b) Gravar ANTES do efeito (despacho, `time_request`, entrega, aviso). Livro indisponível ⇒ nenhum
                efeito, resposta de erro `MDC_CYCLE_RECORD_UNAVAILABLE` + log do executor. Efeito registrado e não
                confirmado ⇒ na retomada é reemitido com a MESMA chave de idempotência (sem duplicar).
            (c) SEM relógio: o Manager nunca lê a hora da máquina; `recorded_instant` vem do evento ou timer da Spec
                de Tempo (ou do envelope SPEC-005); replay do livro reproduz a mesma sequência de decisões.
            (d) Cada despacho grava POR QUE este agente analítico rodou agora: aresta, condição satisfeita, evento causador,
                regra e versões (D9).
            (e) Retomada após queda: estado = replay do livro; publicação já consumida não é pedida de novo;
                eventos perdidos recuperados pelo cursor (RULE-CEB-003/007). COMO guardar = SPEC-009 (G-001
                ABERTA); aqui só o requisito: sobrevivem o livro inteiro, o cursor e as chaves de idempotência.
            (f) Estados do ciclo NÃO são estados de objeto do Blackboard (P-6; M-001 ABERTA).
            [Fonte: P-6; INV-07; RULE-BB-004; RULE-CEB-003/007; research §3.4 (SRC-TEMPORAL-01 [EXTERNO])]

RULE-MDC-011: ENTREGA À FASE 2.
            (a) Na transição `ATIVADO` → `EM_SÍNTESE`, publica `phase2_handoff` no PRÓPRIO workspace {`cycle_id`,
                `asset`, `mission_mode`, referências das análises publicadas, da leitura macro, do alarme e do setup,
                `graph_version`, `log_head`} e avisa pelo Event Bus. É INSUMO à Fase 2, não recomendação nem decisão
                (RULE-DEC-01; INV-05).
            (b) `mission_mode` = PRE_PROGRAMADA segue no handoff (WF-K04; a fila de revisão é posterior, fora daqui).
            (c) Depois da entrada em `EM_SÍNTESE`, a Fase 1 não executa transição do ciclo (CONF-1); evento dirigido
                à Fase 1 para esse ciclo ⇒ `MDC_NOT_PHASE1_TRANSITION` (registro, sem efeito).
            (d) O handoff NÃO contém TMP, Signal Package, convicção global, R:R nem ordem (INV-MDC-01).
            [Fonte: MMC-001 §4 (Fase 1 → Fase 2), §5; WF-06; WF-K04; CONF-1]
```

### Tabela de parâmetros (valores INDETERMINADOS — CC-09; nenhum número inventado)

| Parâmetro | Regra | Granularidade | Dono do valor | Sem valor ⇒ |
|---|---|---|---|---|
| `macro_conclusive_threshold` (θ) | RULE-MDC-005 (c) | por ativo (WF-P02) | Andraus / calibração (J-001, N-001 ABERTAS; BL-032) | não conclusiva — alarme não pedido |
| `max_steps_per_cycle` · `max_rounds_per_agent` · `max_consecutive_failures` · `stage_deadline` | RULE-MDC-008 (a) | `trading_type` × etapa | Andraus / BUILD (calibração) | pedido recusado `MDC_LIMITS_NOT_CONFIGURED` |
| `cost_budget` | RULE-MDC-008 (c) | `trading_type` | Andraus | sem aviso de custo; nada cortado |
| latência de despacho/notificação | RULE-CEB-010 (SPEC-005) | consumidor | SPEC-005 (parâmetro) | INDETERMINADO — declarado (4Es e latência) |

---

## Critérios de Aceitação (EARS)

> Cada EARS referencia a regra-fonte por ID; não a reescreve. Granularidade multi-condição segue a prática das SPEC-048/049 (C-001 ABERTA — afeta só a redação).

1. (MDC-001) Quando um pedido de ciclo chega, o Manager-Fase-1 DEVE aceitá-lo só se a origem autenticada for Andraus ou a Fase 0, todos os campos de WF-01 estiverem presentes, não houver ciclo ativo para o mesmo (ativo, missão) e parâmetros, grafo, serviço de tempo e livro de bordo estiverem disponíveis, e NÃO DEVE originar pedido de ciclo por conta própria.
2. (MDC-002) Quando uma versão do grafo de despacho é registrada, o Manager-Fase-1 DEVE recusá-la se tiver ciclo dirigido ou aresta que viole os postos de INV-01 e DEVE despachar só nós da versão fixada no ciclo, desempatando por (posto, node_id).
3. (MDC-003) Quando um nó é despachado, o Manager-Fase-1 DEVE publicar o pedido só no próprio workspace com chave de idempotência, gravar o livro de bordo antes, esperar a publicação com timer de etapa e NÃO DEVE consumir publicação de outro ciclo, de outro papel ou sem envelope.
4. (MDC-004) Quando o Estrutural publica, o Manager-Fase-1 DEVE despachar o Institucional só com `opportunity = SIM` e encerrar o ciclo com motivo nos demais casos; e, quando chega `ALARM_TRIGGERED`, DEVE despachar o Operacional só se `inside_killzone = true`.
5. (MDC-004 (d)) Quando é publicada nova versão de hipótese que passa de DOMINANT a REFUTED ou SUPERSEDED, o Manager-Fase-1 DEVE registrar a ruptura e avisar Andraus/Fase 0, e NÃO DEVE abrir ciclo por conta própria (DN-2).
6. (MDC-005) Quando o Institucional publica, o Manager-Fase-1 DEVE invocar uma única vez a leitura macro, encerrar como NEUTRO se `directional_conflict = true` e só formar contexto se θ estiver preenchido e o valor agregado for ≥ θ.
7. (MDC-006) Quando o contexto está formado, o Manager-Fase-1 DEVE pedir o alarme só com hipótese de contexto em ACTIVE/DOMINANT e todos os campos de WF-A01 copiados da publicação, e NÃO DEVE calcular nem preencher campo.
8. (MDC-006 (d)) Quando o Operacional publica, o Manager-Fase-1 DEVE aceitar o setup só se `parent_id`, direção e TF de entrada conferirem, encerrar pelo ramo 3 marcando o alarme como usado nos demais casos e NÃO DEVE consumir objeto-hipótese do Operacional.
9. (MDC-007) Quando um evento chega para um ciclo, o Manager-Fase-1 DEVE aplicar só a linha correspondente da tabela de D5 e, para par não listado, ciclo encerrado ou trecho de outro dono, NÃO DEVE transitar e DEVE registrar o código.
10. (MDC-008) Quando um teto de controle estoura, o Manager-Fase-1 DEVE encerrar o ciclo com `MDC_LIMIT_EXCEEDED` e avisar; e, quando o orçamento de custo estoura, DEVE avisar e escalar sem pular nem suprimir etapa.
11. (MDC-009/010) Quando qualquer efeito vai ser produzido, o Manager-Fase-1 DEVE gravá-lo antes no livro de bordo só-inserção, sem ler o relógio; com o livro indisponível NÃO DEVE produzir efeito; e, ao encerrar por INDETERMINADO, DEVE gravar a abstenção.
12. (MDC-011) Quando o setup é aceito, o Manager-Fase-1 DEVE publicar `phase2_handoff` só com referências e parar na entrada de `EM_SÍNTESE`, sem TMP, Signal Package, convicção global, R:R nem ordem.
13. (INV-MDC-01) Quando qualquer etapa pede capacidade fora da allowlist ou chamada de modelo, o Manager-Fase-1 NÃO DEVE executá-la e DEVE registrar a recusa; e, com o registro de capacidades indisponível ou divergente, NÃO DEVE despachar nada.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> Cada BASpec REFERENCIA a regra-fonte (D2) por ID. D = determinístico; C = constitutivo (é o gate). Nenhuma H/P (MMC-001 §3.1.3, obrigação). Cenários em D7/D8 partem da Fixture M0.

### D3.1 — Vocabulário único de códigos (dono: SPEC-008, salvo indicação)

| Código | Subcódigos / valores | Tipo | Regra | Cenário |
|---|---|---|---|---|
| `MDC_REQUEST_INCOMPLETE` | `MDC_FIELD_MISSING` (nome do campo) | recusa do pedido | 001 (a) | T02 (a)(b) |
| `MDC_REQUEST_ORIGIN_NOT_ALLOWED` | — | recusa do pedido | 001 (b) | T02 (c) |
| `MDC_CYCLE_ALREADY_ACTIVE` | — | recusa do pedido | 001 (d) | T03 |
| `MDC_LIMITS_NOT_CONFIGURED` | — | recusa do pedido | 001 (e); 008 (a) | T02 (d) |
| `MDC_GRAPH_VERSION_UNREGISTERED` | — | recusa do pedido | 001 (e); 002 (f) | T02 (e) |
| `MDC_TIME_SERVICE_UNAVAILABLE` | — | recusa do pedido | 001 (e) | T02 (f) |
| `MDC_CYCLE_RECORD_UNAVAILABLE` | — | resposta de erro + log do executor (não há livro) | 010 (b) | T17 (b) |
| `MDC_GRAPH_CYCLIC` · `MDC_GRAPH_HIERARCHY_VIOLATION` | — | versão do grafo não registrável | 002 (b)(c) | T04 |
| `MDC_EVENT_FOREIGN_CYCLE` · `MDC_EVENT_ENVELOPE_INVALID` | — | evento não consumido | 003 (d) | ADV-03; ADV-04 |
| `MDC_DUPLICATE_IGNORED` | — | marcação (sem efeito) | 003 (e) | ADV-01; ADV-02 |
| `MDC_STAGE_DEADLINE_EXCEEDED` | — | encerramento | 003 (c) | T14 |
| `MDC_NO_OPPORTUNITY` | ramo 1 | encerramento | 004 (a) | T06 (a) |
| `MDC_OPPORTUNITY_UNDETERMINED` | — | encerramento + abstenção | 004 (a) | T06 (b) |
| `MDC_TRIGGER_OUTSIDE_WINDOW` | — | evento recusado | 004 (b) | T10 (a) |
| `MDC_DOMINANT_RUPTURE_DETECTED` | — | marcação + aviso | 004 (d) | T18 |
| `MDC_MACRO_ALREADY_INVOKED` | — | recusa | 005 (a) | ADV-06 |
| `MDC_DIRECTIONAL_CONFLICT_NEUTRAL` | ramo 2 | encerramento | 005 (b) | T07 |
| `MDC_MACRO_NOT_CONCLUSIVE` | `MDC_MACRO_THRESHOLD_UNSET`, `MDC_MACRO_READING_UNDETERMINED`, `MDC_MACRO_BELOW_THRESHOLD` | encerramento (+ abstenção nas duas primeiras) | 005 (c) | T08 (a)(b)(c) |
| `MDC_ORIGIN_HYPOTHESIS_NOT_ELIGIBLE` | — | encerramento | 006 (a) | T09 (a) |
| `MDC_ALARM_FIELDS_INCOMPLETE` | — | encerramento | 006 (b) | T09 (b) |
| `MDC_SETUP_MISALIGNED` | `DIRECTION_MISMATCH`, `DIRECTION_UNDETERMINED`, `TF_INVALID`, `PARENT_MISMATCH` | encerramento (ramo 3) | 006 (d) | T12 (a)–(d) |
| `MDC_ICT_HYPOTHESIS_REJECTED` | — | publicação não consumida | 006 (e) | ADV-08 |
| `MDC_ALARM_EXPIRED` (ramo 5) · `MDC_ALARM_CANCELLED` | — | encerramento | 006 (g) | T13 (a)(b) |
| `MDC_TRANSITION_NOT_LISTED` · `MDC_CYCLE_CLOSED` | — | sem transição | 007 (b)(d) | ADV-05; T19 |
| `MDC_LIMIT_EXCEEDED` | `STEPS`, `ROUNDS`, `FAILURES` | encerramento + aviso | 008 (b) | T15 (a)–(c) |
| `MDC_COST_BUDGET_EXCEEDED` | — | aviso + escalada (sem transição) | 008 (c) | T16; ADV-09 |
| `MDC_STOP_BY_ANDRAUS` · `MDC_STOP_COMMAND_NOT_AUTHENTICATED` | — | encerramento · comando recusado | 009 (d) | T20 (a)(b) |
| `MDC_NOT_PHASE1_TRANSITION` | — | sem efeito | 011 (c) | T11 (b) |
| `MDC_EFFECT_FORBIDDEN` | `MDC_ANALYSIS_PUBLISH_FORBIDDEN`, `MDC_FOREIGN_WORKSPACE_PUBLISH_FORBIDDEN`, `MDC_HYPOTHESIS_WRITE_FORBIDDEN`, `MDC_CONVICTION_COMPUTE_FORBIDDEN`, `MDC_MODEL_CLASS_CHANGE_FORBIDDEN`, `MDC_TMP_ASSEMBLY_FORBIDDEN`, `MDC_SIGNAL_PACKAGE_ASSEMBLY_FORBIDDEN`, `MDC_ORDER_EMISSION_FORBIDDEN`, `MDC_CYCLE_ORIGINATION_FORBIDDEN`, `MDC_AUTO_COST_PAUSE_FORBIDDEN` | recusa da trava (E3) | INV-MDC-01 | ADV-10 (a)–(j) |
| `MDC_MODEL_CALL_FORBIDDEN` | — | recusa da trava (E3) | INV-MDC-01 | ADV-11 |
| `MDC_CLOCK_READ_FORBIDDEN` | — | recusa da trava (E3) | INV-MDC-01; 010 (c) | ADV-14 |
| `MDC_CAPABILITY_CHECK_FAILED` | `MDC_CAPABILITY_REGISTRY_UNAVAILABLE`, `MDC_CAPABILITY_REGISTRY_DIVERGENT` | nada despachado | INV-MDC-01 | ADV-12 (a)(b) |

**Marcações de fluxo normal (não são recusa):** `MDC_CYCLE_OPENED`, `MDC_DISPATCHED`, `MDC_PUBLICATION_CONSUMED`, `MDC_MACRO_INVOKED`, `MDC_TIME_REQUESTED`, `MDC_TRANSITIONED`, `MDC_HANDOFF_PUBLISHED`, `MDC_CYCLE_CLOSED_RECORDED` (entrada `cycle_closed`) — valores de `entry_type` do livro de bordo.

### BASpec-MDC-001 — Pedido de ciclo e isolamento (ver RULE-MDC-001) [E2]
```
BASpec-MDC-001:
  QUANDO:       Um cycle_request chega (Andraus ou Fase 0)
  ENTÃO:        Aplica RULE-MDC-001 — confere origem, campos de WF-01, ciclo ativo da mesma chave, parâmetros,
                grafo, serviço de tempo e livro (ordem D4.1); aceito ⇒ abertura gravada com versões fixadas e
                AGUARDANDO; recusa ⇒ código; a Fase 1 nunca origina pedido
  PORQUE:       Fase 1 executa pedido já definido; ativos isolados; laço sem teto proibido (MMC-001 §4; WF-P01; P-12)
  REFERÊNCIA:   RULE-MDC-001; WF-01; WF-K04; RULE-CBP-014
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : validação de campos de lista fechada + consulta de ciclo ativo por chave + checagem de disponibilidade
    CRITÉRIO 4Es: Eficácia — pedido incompleto ou duplicado abriria ciclo sem governo; Economicidade — zero modelo
  VERIFICADO POR:
    DADO        T01 (positivo) · T02 (a)–(f) · T03 · ADV-10 (i)
    QUANDO      o pedido é avaliado
    ENTÃO       aceito ⇒ entry_type MDC_CYCLE_OPENED e estado AGUARDANDO; recusado ⇒ código esperado e nenhum despacho
    VERIFICAÇÃO ver T01 / T02 / T03 / ADV-10
```

### BASpec-MDC-002 — Grafo versionado, acíclico e hierárquico (ver RULE-MDC-002) [E2]
```
BASpec-MDC-002:
  QUANDO:       Uma versão do grafo é registrada, ou um ciclo precisa do próximo nó
  ENTÃO:        Aplica RULE-MDC-002 — recusa versão com ciclo ou aresta contra os postos de INV-01; despacha só nós
                da versão fixada; desempate (posto, node_id); versão 1 sem Fibonacci/Fractal (P-11)
  PORQUE:       Ordem por dependência só existe sem ciclo; a hierarquia é constitucional (INV-01/CC-01)
  REFERÊNCIA:   RULE-MDC-002; INV-01; P-11
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : ordenação topológica + conferência de posto por aresta, na hora de registrar a versão
    CRITÉRIO 4Es: Eficácia — impede etapa pulada ou inventada; Efetividade — mesma versão, mesma ordem
  VERIFICADO POR:
    DADO        T01 (ordem da versão 1) · T04 (a) ciclo, (b) aresta ICT→SMC, (c) nó sem posto
    QUANDO      a versão é registrada / o ciclo avança
    ENTÃO       T01: ESTRUTURAL antes de INSTITUCIONAL antes de OPERACIONAL; T04: versão não registrada com código
    VERIFICAÇÃO ver T01 / T04
```

### BASpec-MDC-003 — Despacho pelo quadro, espera com timer, idempotência (ver RULE-MDC-003) [E2]
```
BASpec-MDC-003:
  QUANDO:       Um nó é liberado pela condição da aresta, ou chega uma publicação/notificação para o ciclo
  ENTÃO:        Aplica RULE-MDC-003 — livro antes; dispatch_request no próprio workspace com dispatch_key; aviso pelo
                Event Bus; timer de etapa; só consome publicação do papel/ciclo certo, com envelope; duplicata sem
                efeito; falha conta para o teto
  PORQUE:       Comunicação só via Blackboard; transporte ≠ verdade; reentrega at-least-once não pode duplicar efeito
  REFERÊNCIA:   RULE-MDC-003; RULE-BB-001/005; RULE-CBP-002/005; RULE-CEB-004/007
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : publicação com chave de idempotência + filtro por (cycle_id, dispatch_key, papel autenticado)
    CRITÉRIO 4Es: Eficácia — sem chamada direta nem efeito duplicado; Efetividade — replay reproduz o consumo
  VERIFICADO POR:
    DADO        T01 · T14 · ADV-01 (aviso duplicado) · ADV-02 (retomada) · ADV-03 (outro ciclo) · ADV-04 (sem envelope)
    QUANDO      o despacho e o consumo rodam
    ENTÃO       um dispatch_request por dispatch_key; publicações estranhas não consumidas, com código
    VERIFICAÇÃO ver T01 / T14 / ADV-01..04
```

### BASpec-MDC-004 — Ativação progressiva e Inversão #1 (ver RULE-MDC-004) [E2]
```
BASpec-MDC-004:
  QUANDO:       O Estrutural publica; chega ALARM_TRIGGERED; ou uma hipótese DOMINANT passa a REFUTED/SUPERSEDED
  ENTÃO:        Aplica RULE-MDC-004 — Institucional só com opportunity = SIM; NAO ⇒ ramo 1; ausente ⇒ abstenção;
                Operacional só com inside_killzone = true; ruptura ⇒ registro + aviso, sem abrir ciclo (DN-2)
  PORQUE:       O próximo agente analítico só acorda se a condição anterior for satisfeita (WF-03/WF-05); a ruptura
                exige análise sem corte por custo (Inversão #1), mas a Fase 1 não origina ciclo (P-12)
  REFERÊNCIA:   RULE-MDC-004; WF-03; WF-05; WF-A02; CONFLICT-MAP Inversão #1; CHM-001
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : leitura de campo publicado (opportunity), de flag do evento (inside_killzone) e de domain_state
                  de versões consecutivas do objeto-hipótese
    CRITÉRIO 4Es: Eficiência — não roda SMC/ICT sem oportunidade/disparo; Eficácia — ICT nunca fora da janela
  VERIFICADO POR:
    DADO        T01 · T06 (a)(b) · T10 (a) · T18 · ADV-07 (ICT antes do contexto)
    QUANDO      o evento chega
    ENTÃO       despacho só com a condição; demais casos com código; ruptura com aviso e sem cycle_request
    VERIFICAÇÃO ver T06 / T10 / T18 / ADV-07
```

### BASpec-MDC-005 — Leitura macro, "conclusiva" e NEUTRO (ver RULE-MDC-005) [E2]
```
BASpec-MDC-005:
  QUANDO:       O Institucional publicou no ciclo em AGUARDANDO
  ENTÃO:        Aplica RULE-MDC-005 — 1 invocação macro; directional_conflict = true ⇒ NEUTRO (ramo 2);
                θ ausente / valor INDETERMINADO / valor < θ ⇒ não conclusiva (encerra, sem alarme); conclusiva ⇒
                CONTEXTO_FORMADO
  PORQUE:       Contexto sem limiar declarado não arma alarme (P-5); conflito Elliott×SMC ⇒ NEUTRO (AGENTS §6.4)
  REFERÊNCIA:   RULE-MDC-005; RULE-CF-010; WF-04; WF-C01; CCM-001
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : invocação do mecanismo da SPEC-003 + leitura de dois campos do resultado + comparação ≥ θ
    CRITÉRIO 4Es: Eficácia — não fabrica número nem aprova contexto indeterminado; Economicidade — a Fase 1 não
                  calcula convicção
  VERIFICADO POR:
    DADO        T01 · T07 · T08 (a) θ ausente, (b) INDETERMINADO, (c) abaixo · ADV-06 (2ª invocação)
    QUANDO      a leitura macro volta
    ENTÃO       só valor ≥ θ preenchido e sem conflito forma contexto
    VERIFICAÇÃO ver T07 / T08 / ADV-06
```

### BASpec-MDC-006 — Alarme pedido, Operacional e alinhamento (ver RULE-MDC-006) [E2]
```
BASpec-MDC-006:
  QUANDO:       O ciclo está em CONTEXTO_FORMADO, ARMADO ou ATIVADO e chega o evento correspondente
  ENTÃO:        Aplica RULE-MDC-006 — hipótese de contexto em ACTIVE/DOMINANT; ARM_ALARM com campos copiados;
                ARMED ⇒ ARMADO; TRIGGERED válido ⇒ ATIVADO + Operacional; setup alinhado ⇒ EM_SÍNTESE; desalinhado
                ⇒ ramo 3 + MARK_CONSUMED; EXPIRED/CANCELLED ⇒ encerramento; objeto-hipótese do ICT não consumido
  PORQUE:       Alarme vem do que os analistas publicaram (P-8); desalinhamento = sem entrada (WF-T02); ICT não cria
                hipótese (INV-02); "reset" = só encerrar (P-12)
  REFERÊNCIA:   RULE-MDC-006; WF-A01..A03; WF-T02; INV-02; CONF-4
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : cópia de campos + conferência de estado CHM-001 + igualdade de direção/TF/parent_id
    CRITÉRIO 4Es: Eficácia — nenhum preço calculado pelo despachante; nenhuma entrada contra o contexto
  VERIFICADO POR:
    DADO        T01 · T09 (a)(b) · T12 (a)–(d) · T13 (a)(b) · ADV-08
    QUANDO      o evento chega no estado
    ENTÃO       transição ou encerramento com o código da linha de D5
    VERIFICAÇÃO ver T09 / T12 / T13 / ADV-08
```

### BASpec-MDC-007 — FSM do ciclo em tabela fechada (ver RULE-MDC-007) [E2]
```
BASpec-MDC-007:
  QUANDO:       Qualquer evento chega para um ciclo
  ENTÃO:        Aplica RULE-MDC-007 — só a linha de D5 correspondente; par não listado ⇒ MDC_TRANSITION_NOT_LISTED;
                ciclo encerrado ⇒ MDC_CYCLE_CLOSED; encerramento sem rótulo final até DN-1; nenhuma seta de volta
  PORQUE:       FSM determinística e auditável (WF-F02); estado/transição novos só com Andraus (MMC-001 §3.2.3)
  REFERÊNCIA:   RULE-MDC-007; WF-F01; WF-F02; CONF-1; P-12
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : tabela estado × evento × guarda → próximo/ENC; lookup exato
    CRITÉRIO 4Es: Eficácia — impossível transitar fora da tabela; Efetividade — replay idêntico
  VERIFICADO POR:
    DADO        T01 (caminho feliz) · T19 · ADV-05 (par não listado) · ADV-13 (tentativa de volta a ARMADO)
    QUANDO      o evento é aplicado
    ENTÃO       to_state conforme a linha, ou sem transição com o código
    VERIFICAÇÃO ver T01 / T19 / ADV-05 / ADV-13
```

### BASpec-MDC-008 — Tetos de controle e orçamento de custo (ver RULE-MDC-008) [E2]
```
BASpec-MDC-008:
  QUANDO:       Um contador de teto passa do limite, ou o custo do ciclo passa do orçamento
  ENTÃO:        Aplica RULE-MDC-008 — teto ⇒ encerramento MDC_LIMIT_EXCEEDED + aviso; orçamento ⇒ aviso + escalada,
                sem transição e sem pular etapa; custo nunca vai ao CCM-001
  PORQUE:       Laço sem teto é proibido; custo não suprime análise com evento relevante (CEE §10 S2; P-7; INV-04)
  REFERÊNCIA:   RULE-MDC-008; CEE-001 §10 S2/S4; MMC-001 §6.6
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : contadores no livro de bordo comparados aos parâmetros da versão fixada no ciclo
    CRITÉRIO 4Es: Eficácia antes de Economicidade — o teto protege contra laço; o custo só informa
  VERIFICADO POR:
    DADO        T15 (a)(b)(c) · T16 · ADV-09 (tentativa de pular o Elliott por custo)
    QUANDO      o contador é atualizado
    ENTÃO       teto ⇒ ENC; orçamento ⇒ aviso, despacho segue
    VERIFICAÇÃO ver T15 / T16 / ADV-09
```

### BASpec-MDC-009 — Parar, aguardar, escalar, encerrar (ver RULE-MDC-009) [E1]
```
BASpec-MDC-009:
  QUANDO:       O ciclo encerra, espera, escala, ou chega comando de parada
  ENTÃO:        Aplica RULE-MDC-009 — motivo nomeado; abstenção quando INDETERMINADO; notice sem decidir por Andraus;
                parada só por comando autenticado de Andraus; espera sempre com timer
  PORQUE:       INDETERMINADO deve ser informativo (RULE-MET-02); parada por gasto só Andraus (A-5 (2))
  REFERÊNCIA:   RULE-MDC-009; RULE-MET-02; MMC-001 §6.6
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : gravação de bloco de abstenção de campos fixos + conferência de identidade do comando
    CRITÉRIO 4Es: Efetividade — o encerramento diz o que falta e o que mudaria a conclusão
  VERIFICADO POR:
    DADO        T06 (b) · T08 (a)(b) · T20 (a)(b) · ADV-10 (j)
    QUANDO      a parada ocorre
    ENTÃO       abstention com quatro campos; comando não autenticado não para
    VERIFICAÇÃO ver T06 / T08 / T20 / ADV-10
```

### BASpec-MDC-010 — Livro de bordo só-inserção, sem relógio, retomada (ver RULE-MDC-010) [E1]
```
BASpec-MDC-010:
  QUANDO:       Qualquer efeito vai ser produzido, ou o componente reinicia
  ENTÃO:        Aplica RULE-MDC-010 — entrada antes do efeito; livro indisponível ⇒ nenhum efeito; instante só de
                evento/timer; replay reconstrói o estado e reemite efeito pendente com a mesma chave
  PORQUE:       "Por que este agente rodou agora" deve ser reconstruível (D9); reinício não refaz etapa (research §3.4)
  REFERÊNCIA:   RULE-MDC-010; INV-07; P-6; RULE-CEB-003/007
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : registro write-ahead só-inserção + replay determinístico
    CRITÉRIO 4Es: Efetividade — mesma sequência de eventos, mesmas decisões; Eficácia — sem efeito não registrado
  VERIFICADO POR:
    DADO        T17 (a) replay, (b) livro indisponível · ADV-02 (queda no meio) · ADV-14 (leitura de relógio)
    QUANDO      o efeito/reinício ocorre
    ENTÃO       nenhuma etapa refeita; nenhum efeito sem entrada; nenhuma leitura de relógio
    VERIFICAÇÃO ver T17 / ADV-02 / ADV-14
```

### BASpec-MDC-011 — Entrega à Fase 2 e parada na fronteira (ver RULE-MDC-011) [E2]
```
BASpec-MDC-011:
  QUANDO:       O setup é aceito em ATIVADO
  ENTÃO:        Aplica RULE-MDC-011 — phase2_handoff só com referências, no próprio workspace; EM_SÍNTESE; nenhuma
                transição posterior pela Fase 1; nada de TMP/Signal Package/convicção global/R:R/ordem
  PORQUE:       Fronteira Fase 1 → Fase 2 = entrada em EM_SÍNTESE (CONF-1); SOT não executa (INV-05)
  REFERÊNCIA:   RULE-MDC-011; MMC-001 §4, §5; WF-06; WF-K04
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : publicação de objeto de referências + guarda de dono por linha de D5
    CRITÉRIO 4Es: Eficácia — fronteira sem dupla posse; Eficiência — Fase 2 recebe tudo por referência
  VERIFICADO POR:
    DADO        T11 (a)(b) · ADV-10 (f)(g)(h)
    QUANDO      a entrega ocorre
    ENTÃO       handoff publicado; evento posterior para a Fase 1 ⇒ MDC_NOT_PHASE1_TRANSITION
    VERIFICAÇÃO ver T11 / ADV-10
```

### BASpec-MDC-012 — Trava constitutiva do Manager-Fase-1 (ver INV-MDC-01) [E3]
```
BASpec-MDC-012:
  QUANDO:       Qualquer etapa do ciclo pede capacidade fora da allowlist, chamada de modelo, ou o ciclo vai começar
                uma ação
  ENTÃO:        Aplica INV-MDC-01 — capacidade negada ⇒ MDC_EFFECT_FORBIDDEN (sub); modelo ⇒ MDC_MODEL_CALL_FORBIDDEN;
                registro de capacidades indisponível/divergente ⇒ MDC_CAPABILITY_CHECK_FAILED, nada despachado;
                recusa gravada no livro de bordo
  PORQUE:       Um despachante que analisa, calcula convicção, muda modelo ou emite sinal/ordem cria caminho de
                sinal fora do governo (INV-05; RULE-BB-005; CEE §10 S1/S5; MMC-001 §2.2, §5)
  REFERÊNCIA:   INV-MDC-01; MMC-001 §2.2, §5.1, §6.4-a, §6.6
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : registro de capacidades do componente (allowlist de seis capacidades) aplicado pelo runtime; o gate
                  é a própria ausência de capacidade; conferência do registro antes de cada ação
    GATE DE SAÍDA: determinístico — capacidades exercidas ⊆ allowlist ∧ model_calls == 0 ∧ publicações fora do
                  próprio workspace == 0 ∧ emissões externas == 0
    CRITÉRIO 4Es: Eficácia sobre Economicidade — o nível E3 mede a capacidade que a trava NEGA (sinal/ordem fora do
                  caminho governado, mudança de modelo, hipótese editada: efeito de risco alto e irreversível); não é
                  Classe C em risco baixo (atomic-spec §10.5, CC-11). Economicidade: a trava não chama modelo nem
                  acrescenta etapa cara
  VERIFICADO POR:
    DADO        ADV-10 (a)–(j) · ADV-11 · ADV-12 (a)(b) · ADV-10 (k) falso-DENY amostral
    QUANDO      a capacidade é pedida / o ciclo começa
    ENTÃO       negada com o subcódigo; nada despachado com registro indisponível/divergente
    VERIFICAÇÃO ver ADV-10 / ADV-11 / ADV-12
```

---

## D4 — Algoritmo

**D4.1 — Avaliação do pedido (RULE-MDC-001).** ENTRADA: `cycle_request` + identidade autenticada. PROCESSO (a primeira falha decide; um código por recusa): (0) registro de capacidades (INV-MDC-01) → `MDC_CAPABILITY_CHECK_FAILED` (gravado no livro se ele estiver disponível; senão, resposta de erro + log do executor); (1) livro de bordo disponível → senão `MDC_CYCLE_RECORD_UNAVAILABLE` (resposta de erro; não há onde gravar); (2) origem ∈ {Andraus, Fase 0} → `MDC_REQUEST_ORIGIN_NOT_ALLOWED`; (3) campos de WF-01 → `MDC_REQUEST_INCOMPLETE`; (4) chave (`asset`, `mission_id`) sem ciclo aberto → `MDC_CYCLE_ALREADY_ACTIVE`; (5) versão do grafo registrada → `MDC_GRAPH_VERSION_UNREGISTERED`; (6) `cycle_limits` preenchida para o `trading_type` → `MDC_LIMITS_NOT_CONFIGURED`; (7) serviço de tempo disponível → `MDC_TIME_SERVICE_UNAVAILABLE`. Recusa (exceto (1)) gravada como entrada com `cycle_id` = AUSENTE. SAÍDA: `cycle_id` + abertura gravada + linha F01 de D5, ou recusa. EXEMPLO (M0): pedido R1 de Andraus, BTC, MIS-1, day, H4/H1/M15, NY_AM, ASSISTIDA ⇒ aceito, `graph_version` = 1, `limits_version` = L0.

**D4.2 — Processamento de evento (RULE-MDC-003/007).** Para cada notificação: (0) envelope mínimo SPEC-005 → `MDC_EVENT_ENVELOPE_INVALID`; (1) `event_id` já consumido ou `dispatch_key`/`request_key` repetido → `MDC_DUPLICATE_IGNORED`; (2) `cycle_id` e papel autenticado conferem com o nó/pedido → `MDC_EVENT_FOREIGN_CYCLE`; (3) ciclo encerrado ou em estado final → `MDC_CYCLE_CLOSED`; (4) linha de outro dono (a partir de `EM_SÍNTESE`) → `MDC_NOT_PHASE1_TRANSITION`; (5) busca exata (estado, evento) em D5 → senão `MDC_TRANSITION_NOT_LISTED`; (6) avalia a guarda da linha; (7) grava a entrada (antes do efeito); (8) produz o efeito da linha; (9) atualiza contadores (D4.3). Nenhum passo lê relógio; instantes vêm do evento.

**D4.3 — Contadores (RULE-MDC-008).** `steps` += 1 a cada despacho e a cada invocação macro; `rounds[nó]` = `max_rounds_per_agent` repassado no pedido (o laço interno é do agente analítico); `failures[nó]` += 1 a cada falha seguida, zera no sucesso; qualquer contador > parâmetro da versão fixada ⇒ evento interno `LIMIT_COUNTER_EXCEEDED` (D5, F20). `cost_spent` (se medido) > `cost_budget` ⇒ evento interno `COST_BUDGET_EXCEEDED` (F21), uma vez por ciclo.

**D4.4 — Leitura macro (RULE-MDC-005).** ENTRADA: refs das publicações ESTRUTURAL e INSTITUCIONAL. PROCESSO: invoca o mecanismo (1x); lê `directional_conflict` e o valor agregado `v`; regra: `conflito = true` ⇒ F08a; senão `θ` ausente ∨ `v` INDETERMINADO ∨ `v` < `θ` ⇒ F08b; senão F07. EXEMPLO (M0, símbolos — sem número): `v` = θ + δ (δ > 0), conflito = false ⇒ F07.

---

## D5 — Estado: máquina do ciclo em TABELA (WF-F02; dono por linha — CONF-1)

> Leitura: "ENC" = encerramento (RULE-MDC-007 (d)): grava `cycle_closed`; nenhum evento posterior aceito; rótulo final de WF-F02 = DN-1. Toda ação é precedida da entrada no livro de bordo (RULE-MDC-010 (b)). Encerramento em `ATIVADO` sempre pede `MARK_CONSUMED` (P-12: alarme "usado"); em `ARMADO`, nenhum pedido ao alarme (requisito T-3 à Spec de Tempo). Linhas de outros donos: listadas, **não** especificadas aqui; gate determinístico do dono (MMC-001 §3.2.2).

| ID | Estado | Evento | Guarda (D) | Próximo | Ação | Código (`entry_type`/code) | Dono |
|---|---|---|---|---|---|---|---|
| F01 | — (sem ciclo) | `CYCLE_REQUEST` | D4.1 aceita | `AGUARDANDO` | abertura; despacha ESTRUTURAL; timer de etapa | `MDC_CYCLE_OPENED` | SPEC-008 |
| F02 | — | `CYCLE_REQUEST` | D4.1 recusa | (não abre) | recusa | código de D4.1 | SPEC-008 |
| F03 | `AGUARDANDO` | `PUB(ESTRUTURAL)` | `opportunity` = SIM | `AGUARDANDO` | despacha INSTITUCIONAL; timer | `MDC_DISPATCHED` | SPEC-008 |
| F04 | `AGUARDANDO` | `PUB(ESTRUTURAL)` | `opportunity` = NAO | ENC (ramo 1) | — | `MDC_NO_OPPORTUNITY` | SPEC-008 |
| F05 | `AGUARDANDO` | `PUB(ESTRUTURAL)` | `opportunity` ausente/fora da lista | ENC | abstenção | `MDC_OPPORTUNITY_UNDETERMINED` | SPEC-008 |
| F06 | `AGUARDANDO` | `PUB(INSTITUCIONAL)` | nó despachado neste ciclo | `AGUARDANDO` | invoca leitura macro (1x) | `MDC_MACRO_INVOKED` | SPEC-008 |
| F07 | `AGUARDANDO` | `MACRO_RESULT` | conflito = false ∧ θ preenchido ∧ `v` ≥ θ | `CONTEXTO_FORMADO` | (segue F09) | `MDC_TRANSITIONED` | SPEC-008 |
| F08a | `AGUARDANDO` | `MACRO_RESULT` | conflito = true | ENC (ramo 2 — NEUTRO) | — | `MDC_DIRECTIONAL_CONFLICT_NEUTRAL` | SPEC-008 |
| F08b | `AGUARDANDO` | `MACRO_RESULT` | conflito = false ∧ (θ ausente ∨ `v` INDETERMINADO ∨ `v` < θ) | ENC | abstenção (θ ausente / INDETERMINADO) | `MDC_MACRO_NOT_CONCLUSIVE` (sub) | SPEC-008 |
| F09 | `CONTEXTO_FORMADO` | `ON_ENTER` (interno) | hipótese de contexto ∈ {ACTIVE, DOMINANT} ∧ campos WF-A01 completos | `CONTEXTO_FORMADO` | `ARM_ALARM`; timer | `MDC_TIME_REQUESTED` | SPEC-008 |
| F10 | `CONTEXTO_FORMADO` | `ON_ENTER` | hipótese de contexto ∉ {ACTIVE, DOMINANT} | ENC | — | `MDC_ORIGIN_HYPOTHESIS_NOT_ELIGIBLE` | SPEC-008 |
| F11 | `CONTEXTO_FORMADO` | `ON_ENTER` | elegível ∧ campo de WF-A01 ausente | ENC | — | `MDC_ALARM_FIELDS_INCOMPLETE` | SPEC-008 |
| F12 | `CONTEXTO_FORMADO` | `ALARM_ARMED` | alarme deste ciclo | `ARMADO` | — | `MDC_TRANSITIONED` | SPEC-008 |
| F13 | `ARMADO` | `ALARM_TRIGGERED` | `inside_killzone` = true | `ATIVADO` | despacha OPERACIONAL (`tf_entrada`); timer | `MDC_DISPATCHED` | SPEC-008 |
| F14 | `ARMADO` | `ALARM_TRIGGERED` | `inside_killzone` ≠ true | (sem transição) | — | `MDC_TRIGGER_OUTSIDE_WINDOW` | SPEC-008 |
| F15 | `ARMADO` | `ALARM_EXPIRED` · `ALARM_CANCELLED` | alarme deste ciclo | ENC (ramo 5 · cancelado) | — | `MDC_ALARM_EXPIRED` · `MDC_ALARM_CANCELLED` | SPEC-008 |
| F16 | `ATIVADO` | `PUB(OPERACIONAL)` setup | alinhado (RULE-MDC-006 (d)) | `EM_SÍNTESE` | `MARK_CONSUMED`; publica `phase2_handoff` | `MDC_HANDOFF_PUBLISHED` | SPEC-008 (última) |
| F17 | `ATIVADO` | `PUB(OPERACIONAL)` setup | não alinhado | ENC (ramo 3) | `MARK_CONSUMED` | `MDC_SETUP_MISALIGNED` (sub) | SPEC-008 |
| F18 | `ATIVADO` | `PUB(OPERACIONAL)` objeto-hipótese | — | (sem transição) | não consumido | `MDC_ICT_HYPOTHESIS_REJECTED` | SPEC-008 |
| F19 | `AGUARDANDO` · `CONTEXTO_FORMADO` · `ATIVADO` | `STAGE_TIMER_FIRED` | timer da etapa corrente | ENC (em `ATIVADO` = ramo 3 por prazo) | em `ATIVADO`: `MARK_CONSUMED` | `MDC_STAGE_DEADLINE_EXCEEDED` | SPEC-008 |
| F20 | `AGUARDANDO`…`ATIVADO` | `LIMIT_COUNTER_EXCEEDED` (interno) | — | ENC | aviso; em `ATIVADO`: `MARK_CONSUMED` | `MDC_LIMIT_EXCEEDED` (sub) | SPEC-008 |
| F21 | `AGUARDANDO`…`ATIVADO` | `COST_BUDGET_EXCEEDED` (interno) | — | (sem transição) | aviso + escalada | `MDC_COST_BUDGET_EXCEEDED` | SPEC-008 |
| F22 | `AGUARDANDO`…`ATIVADO` | `STOP_COMMAND` | identidade autenticada = Andraus | ENC | em `ATIVADO`: `MARK_CONSUMED` | `MDC_STOP_BY_ANDRAUS` | SPEC-008 |
| F23 | qualquer | `STOP_COMMAND` | outra identidade ou não autenticado | (sem transição) | — | `MDC_STOP_COMMAND_NOT_AUTHENTICATED` | SPEC-008 |
| F24 | `EM_SÍNTESE` | decisão da Fase 2 de enviar + TMP interno | gate determinístico do dono | `EM_RISCO` | — | — | **SPEC-014** |
| F25 | `EM_SÍNTESE` | Fase 2 decide não enviar | — | **não literal em WF-F02** | — | — | **SPEC-014** + DN-1 |
| F26 | `EM_RISCO` | decisão do Agente de Risco (ramo 4 = veto) ou prazo | gate determinístico do dono | `SINAL_ENVIADO` · `RECUSADO` · `EXPIRADO` | — | — | **RISK-SPEC** |
| F27 | `EM_SÍNTESE` · `EM_RISCO` | evento dirigido à Fase 1 | — | (sem efeito) | — | `MDC_NOT_PHASE1_TRANSITION` | SPEC-008 |
| F28 | ENC ou final | qualquer | — | (sem transição) | — | `MDC_CYCLE_CLOSED` | SPEC-008 |
| F29 | qualquer | par (estado, evento) não listado | — | (sem transição) | — | `MDC_TRANSITION_NOT_LISTED` | SPEC-008 |

**Fora da tabela (por desenho):** ramo 6 de WF-F01 (depois de `SINAL_ENVIADO` — P-13); Inversão #1 (detector entre ciclos, RULE-MDC-004 (d) — não muda estado de nenhum ciclo; o cancelamento do alarme chega por F15); duplicatas, envelope e ciclo estranho (D4.2 passos 0–2, antes do lookup). **Nenhuma linha leva a `ARMADO` a partir de `ATIVADO` nem de ENC** (sem "reset" — P-12).

---

## D6 — Protocolo (Blackboard)

1. O Manager publica `dispatch_request` **só** no próprio workspace (`manager`), com chave de idempotência; o Event Bus notifica os assinantes autorizados (RULE-CEB-008). 2. O agente analítico lê o pedido, publica a análise **no próprio workspace** referindo `cycle_id`/`dispatch_key`; o Event Bus notifica. 3. O Manager consome pela ordem de commit do workspace (RULE-CBP-006); notificação perdida ⇒ replay pelo cursor. 4. Na entrega, `phase2_handoff` no workspace `manager`. 5. `dispatch_request` e `phase2_handoff` são objetos não-hipótese: `publication_state` conforme SPEC-004; `domain_state` desses objetos **não** é definido aqui (RULE-CBP-009; **M-001 ABERTA**). 6. O ciclo **não** é objeto do quadro: seu estado vive no livro de bordo (P-6).

---

## Interface com a Spec de Tempo — requisito `[PROPOSTA]` (DHR-SPEC008-001 §3; CONF-5; P-9)

> Ator = Manager nas duas peças; muda só o documento (MMC-001 §4, linha "Manager × Spec de Tempo"). Esta seção **não** especifica o relógio: só o que a SPEC-008 pede e o que ela espera receber. Vira obrigação da Spec de Tempo só na abertura/Plan dela, com homologação de Andraus.

| Sentido | Mensagem | Campos mínimos | Uso nesta Spec |
|---|---|---|---|
| SPEC-008 → Tempo | `ARM_ALARM` | campos de WF-A01 copiados, `parent_id`, `cycle_id`, `killzone`, `request_key` | F09 |
| SPEC-008 → Tempo | `MARK_CONSUMED` | `alarm_id`, `cycle_id`, `request_key` | F16, F17, F19–F20, F22 em `ATIVADO` |
| SPEC-008 → Tempo | `STAGE_TIMER` | `cycle_id`, `stage_seq`, `stage_deadline`, `request_key` | F01, F03, F09, F13 |
| Tempo → SPEC-008 | `ALARM_ARMED` · `ALARM_EXPIRED` · `ALARM_CANCELLED` (com motivo) | `alarm_id`, `cycle_id`, `recorded_instant` | F12, F15 |
| Tempo → SPEC-008 | `ALARM_TRIGGERED` | + `inside_killzone`, `price_observation_ref` (Observação — INV-06) | F13, F14 |
| Tempo → SPEC-008 | `STAGE_TIMER_FIRED` | `cycle_id`, `stage_seq`, `recorded_instant` | F19 |

**Requisitos `[PROPOSTA]` à Spec de Tempo:** (T-1) janela da Killzone, disparo e `inside_killzone` calculados **lá** (CONF-5; WF-K01..K03); (T-2) todo evento traz `recorded_instant` registrado (a SPEC-008 nunca lê relógio — RULE-MDC-010 (c)); (T-3) alarme `ARMED` cujo ciclo foi encerrado termina pelas regras dela (prazo/cancelamento — WF-A03), sem pedido da SPEC-008; disparo tardio para ciclo encerrado chega e é descartado por F28; (T-4) o pré-aviso de WF-K02 pede orientações a Andraus/Fase 0, **não** abre ciclo na Fase 1; (T-5) pedidos idempotentes por `request_key`; (T-6) prazo vencido durante queda ⇒ `EXPIRED`, nunca disparo atrasado; (T-7) mercado fechado/calendário ausente conforme P-9; (T-8) o alarme é gatilho de análise, nunca ordem (WF-A01). Divergência de número em WF-K02 ("SPEC-008/015") registrada: prevalece CONF-5 (MMC-001 §8.3).

---

## Requisitos a outras Specs (fora do controle desta) — `[INFERÊNCIA]`

- **SPEC-010 (Elliott/Estrutural):** publicar `opportunity` ∈ {SIM, NAO} e a hipótese primária com os campos de WF-A01 (P-8). **SPEC-012 (SMC/Institucional):** publicar referindo `cycle_id`/`dispatch_key`. **SPEC-013 (ICT/Operacional):** setup com direção, TF e `parent_id`; nunca objeto-hipótese (INV-02).
- **SPEC-003 (BASELINE):** nenhum pedido de mudança — o campo agregado e `directional_conflict` são **lidos** do contrato existente (RULE-MDC-005 (d)).
- **SPEC-009:** guardar livro de bordo, cursor e chaves de idempotência para a retomada (G-001 ABERTA). **SPEC-014:** consumir `phase2_handoff`; transições a partir de `EM_SÍNTESE` com gate determinístico (MMC-001 §3.2.2); F25 (não enviar) = DN-1. **SPEC-015:** origem dos pedidos; quantas vezes tentar (P-12, `[PROPOSTA]` do MMC-001 §8.2-bis); DN-2. **SPEC-040:** medida de custo que alimenta `cost_budget`.

---

## Contrato lógico — esqueleto `[PROPOSTA]` (referência; não redefine CEM/CHM/CCM nem objetos da SPEC-004/005)

```
cycle_request   : {asset, mission_id, trading_type, tf_triple{contexto, confirmacao, entrada}, killzone,
                   mission_mode, origin_identity (do runtime)}
dispatch_graph  : {version, nodes[{node_id, role, rank}], edges[{from, to, condition ∈ lista fechada}], approved_ref}
cycle_limits    : {version, by_trading_type{stage → {max_steps_per_cycle, max_rounds_per_agent,
                   max_consecutive_failures, stage_deadline}}, cost_budget, macro_conclusive_threshold{asset → θ}}
dispatch_request: {cycle_id, node_id, stage_seq, dispatch_key, input_refs[], tf, max_rounds, graph_version}
cycle_log_entry : {cycle_id | AUSENTE, log_seq, entry_type, rule_id, graph_version, limits_version, causation_event_id,
                   recorded_instant, from_state, to_state | —, code | —, refs[], counters{steps, failures[]},
                   capability_check_ref | AUSENTE, abstention? {incerto, afeta, condicao_de_mudanca, informacao}}
cycle_closed    : {cycle_id, code, wf_f01_branch | —, state_at_close, wf_f02_final_label = AUSENTE (DN-1), log_seq}
time_request    : {kind ∈ {ARM_ALARM, MARK_CONSUMED, STAGE_TIMER}, cycle_id, request_key, payload}
phase2_handoff  : {cycle_id, asset, mission_mode, analysis_refs[], macro_reading_ref, alarm_ref, setup_ref,
                   graph_version, log_head}   — SEM TMP, Signal Package, convicção global, R:R, ordem
notice          : {cycle_id | —, kind ∈ {LIMIT, COST, RUPTURE, CAPABILITY, STOP}, code, refs[], to = Andraus}
capability_registry: {version, allowlist[6]}   — conferido antes de cada ação (INV-MDC-01)
```

---

## Fixture M0 (base dos cenários; valores simbólicos de teste — nenhum número calibrado, CC-09)

- Pedido **R1**: Andraus (autenticado), BTC, MIS-1, day, TFs H4/H1/M15 (WF-R01, padrão editável), `killzone` = NY_AM, ASSISTIDA. Grafo versão 1 (RULE-MDC-002 (a)). `cycle_limits` **L0** preenchida com valores de teste simbólicos (Smax, Rmax, Fmax, Dprazo); `cost_budget` = B; θ(BTC) = θ.
- **E1**: publicação do Estrutural (`opportunity` = SIM) referindo **H1** — hipótese primária DOMINANT, direção ALTA, com nível, condição de disparo, validade, invalidação e condição de cancelamento. **I1**: publicação do Institucional. **CV1**: resultado macro, `directional_conflict` = false, `v` = θ + δ (δ > 0).
- **A1**: alarme do ciclo; eventos `ALARM_ARMED(A1)`, `ALARM_TRIGGERED(A1, inside_killzone = true)`. **S1**: setup do Operacional, direção ALTA, TF M15, `parent_id` = H1.
- Registro de capacidades **K0** = allowlist exata de INV-MDC-01. Livro de bordo e serviço de tempo disponíveis.

---

## D7 — Cenários de Teste (20 — T01..T20; fixture M0 salvo indicação)

### Cenário-MDC-T01 — Caminho feliz até a entrega (positivo; MDC-001..007, 011)
```
DADO        M0
QUANDO      R1; depois E1, I1, CV1, ALARM_ARMED(A1), ALARM_TRIGGERED(A1, inside_killzone = true), S1
ENTÃO       F01 → F03 → F06 → F07 → F09 → F12 → F13 → F16; ESTRUTURAL, INSTITUCIONAL, OPERACIONAL despachados nessa ordem
VERIFICAÇÃO estados: AGUARDANDO, AGUARDANDO, AGUARDANDO, CONTEXTO_FORMADO, ARMADO, ATIVADO, EM_SÍNTESE; dispatch_request == 3;
            macro_invocations == 1; time_request ARM_ALARM.payload == campos de H1 copiados; MARK_CONSUMED(A1) == 1;
            phase2_handoff publicado; toda entrada de efeito com log_seq menor que o do efeito; model_calls == 0
```

### Cenário-MDC-T02 — Pedido recusado (negativos; MDC-001)
```
DADO        M0, exceto, um de cada vez: (a) R1 sem killzone; (b) R1 com trading_type = position e tf_entrada ausente;
            (c) R1 vindo de identidade de agente analítico; (d) cycle_limits sem stage_deadline para day; (e) grafo sem
            versão registrada; (f) serviço de tempo indisponível
QUANDO      o pedido é avaliado (D4.1)
ENTÃO       nenhum ciclo aberto; nenhum despacho
VERIFICAÇÃO (a)(b) code == "MDC_REQUEST_INCOMPLETE", sub "MDC_FIELD_MISSING" (campo nomeado); (c) "MDC_REQUEST_ORIGIN_NOT_ALLOWED";
            (d) "MDC_LIMITS_NOT_CONFIGURED"; (e) "MDC_GRAPH_VERSION_UNREGISTERED"; (f) "MDC_TIME_SERVICE_UNAVAILABLE";
            entrada com cycle_id == AUSENTE; dispatch_request == 0
```

### Cenário-MDC-T03 — Mesma chave recusada; ativo diferente em paralelo (MDC-001 (d); WF-P01)
```
DADO        ciclo de R1 em ARMADO
QUANDO      (a) chega R1' = (BTC, MIS-1); (b) chega R2 = (XAU, MIS-2) válido
ENTÃO       (a) recusado; (b) aceito, com cycle_id, contadores e timers próprios
VERIFICAÇÃO (a) code == "MDC_CYCLE_ALREADY_ACTIVE"; (b) cycle_id(R2) ≠ cycle_id(R1); eventos de R2 não alteram contadores de R1
```

### Cenário-MDC-T04 — Versão do grafo não registrável (negativos; MDC-002)
```
DADO        proposta de versão 2 com (a) aresta OPERACIONAL→ESTRUTURAL fechando ciclo; (b) aresta OPERACIONAL(5)→INSTITUCIONAL(4);
            (c) nó FIBONACCI sem posto declarado
QUANDO      o registro da versão é tentado
ENTÃO       versão não registrada; ciclos seguem na versão 1
VERIFICAÇÃO (a) "MDC_GRAPH_CYCLIC"; (b)(c) "MDC_GRAPH_HIERARCHY_VIOLATION"; graph_version em uso == 1
```

### Cenário-MDC-T05 — Grafo com Fibonacci em versão futura (positivo; MDC-002 (e); P-11)
```
DADO        versão 2 registrada por ato de Andraus: ESTRUTURAL(1) →[OPORTUNIDADE_SIM] FIBONACCI(2) →[OPORTUNIDADE_SIM] INSTITUCIONAL(4)
QUANDO      ciclo novo aberto depois do registro; o ciclo de R1 (aberto antes) segue
ENTÃO       ciclo novo despacha FIBONACCI entre ESTRUTURAL e INSTITUCIONAL; ciclo de R1 continua na versão 1
VERIFICAÇÃO ordem de dispatch_request do ciclo novo == [ESTRUTURAL, FIBONACCI, INSTITUCIONAL, ...]; graph_version(R1) == 1;
            nenhuma linha da Spec alterada (só dado)
```

### Cenário-MDC-T06 — Sem oportunidade e oportunidade indeterminada (MDC-004 (a); ramo 1)
```
DADO        M0, exceto E1 com (a) opportunity = NAO; (b) sem o campo opportunity
QUANDO      E1 é consumida
ENTÃO       ENC; INSTITUCIONAL não despachado
VERIFICAÇÃO (a) code == "MDC_NO_OPPORTUNITY", wf_f01_branch == 1; (b) code == "MDC_OPPORTUNITY_UNDETERMINED", abstention com os
            quatro campos (incerto = opportunity; informacao = campo publicado pela SPEC-010); dispatch_request == 1;
            wf_f02_final_label == AUSENTE
```

### Cenário-MDC-T07 — Conflito direcional ⇒ NEUTRO (MDC-005 (b); ramo 2)
```
DADO        M0, exceto CV1 com directional_conflict = true e v ≥ θ
QUANDO      CV1 é lido
ENTÃO       ENC NEUTRO antes de olhar o limiar; alarme não pedido
VERIFICAÇÃO code == "MDC_DIRECTIONAL_CONFLICT_NEUTRAL"; wf_f01_branch == 2; time_request ARM_ALARM == 0; conflito não recalculado
            (valor lido == valor do resultado)
```

### Cenário-MDC-T08 — Contexto não conclusivo (MDC-005 (c); P-5)
```
DADO        M0, exceto: (a) θ(BTC) ausente; (b) CV1 com valor agregado INDETERMINADO; (c) v = θ − δ
QUANDO      CV1 é lido
ENTÃO       ENC; alarme não pedido
VERIFICAÇÃO code == "MDC_MACRO_NOT_CONCLUSIVE"; sub (a) "MDC_MACRO_THRESHOLD_UNSET", (b) "MDC_MACRO_READING_UNDETERMINED",
            (c) "MDC_MACRO_BELOW_THRESHOLD"; abstention presente em (a)(b); ARM_ALARM == 0; nenhum número de θ no livro em (a)
```

### Cenário-MDC-T09 — Hipótese de contexto não elegível; campos do alarme incompletos (MDC-006 (a)(b))
```
DADO        M0, exceto: (a) H1 em CANDIDATE; (b) H1 sem nível de invalidação
QUANDO      o ciclo entra em CONTEXTO_FORMADO
ENTÃO       ENC; nada pedido à Spec de Tempo; o Manager não preenche o campo
VERIFICAÇÃO (a) "MDC_ORIGIN_HYPOTHESIS_NOT_ELIGIBLE"; (b) "MDC_ALARM_FIELDS_INCOMPLETE"; ARM_ALARM == 0
```

### Cenário-MDC-T10 — Disparo fora da janela; depois, dentro (MDC-004 (b); CONF-3)
```
DADO        ciclo de R1 em ARMADO
QUANDO      (a) ALARM_TRIGGERED(A1, inside_killzone = false); (b) em seguida ALARM_TRIGGERED(A1, inside_killzone = true) com novo event_id
ENTÃO       (a) evento recusado, estado ARMADO, OPERACIONAL não despachado; (b) ATIVADO e OPERACIONAL despachado
VERIFICAÇÃO (a) code == "MDC_TRIGGER_OUTSIDE_WINDOW", to_state == —; (b) F13; dispatch_request(OPERACIONAL) == 1
```

### Cenário-MDC-T11 — Entrega à Fase 2 e parada na fronteira (MDC-011)
```
DADO        T01 concluído (EM_SÍNTESE)
QUANDO      (a) o handoff é inspecionado; (b) chega STAGE_TIMER_FIRED atrasado para o ciclo
ENTÃO       (a) só referências; (b) nenhuma transição pela Fase 1
VERIFICAÇÃO (a) phase2_handoff contém analysis_refs, macro_reading_ref, alarm_ref, setup_ref e mission_mode; não contém tmp,
            signal_package, global_conviction, rr nem order; (b) code == "MDC_NOT_PHASE1_TRANSITION"; estado == EM_SÍNTESE
```

### Cenário-MDC-T12 — Setup desalinhado (MDC-006 (d); ramo 3; CONF-4)
```
DADO        ciclo em ATIVADO; S1 trocado por: (a) direção BAIXA; (b) sem direção; (c) TF H4 (= tf_contexto); (d) parent_id ≠ H1
QUANDO      o setup é consumido
ENTÃO       ENC pelo ramo 3; alarme marcado usado
VERIFICAÇÃO code == "MDC_SETUP_MISALIGNED"; sub (a) DIRECTION_MISMATCH, (b) DIRECTION_UNDETERMINED, (c) TF_INVALID, (d)
            PARENT_MISMATCH; wf_f01_branch == 3; MARK_CONSUMED(A1) == 1; phase2_handoff == 0
```

### Cenário-MDC-T13 — Alarme vencido ou cancelado (MDC-006 (g); ramo 5; WF-A03)
```
DADO        ciclo em ARMADO
QUANDO      (a) ALARM_EXPIRED(A1); (b) ALARM_CANCELLED(A1, motivo = H1 REFUTED)
ENTÃO       ENC; nenhum alarme novo; nenhuma volta a ARMADO
VERIFICAÇÃO (a) "MDC_ALARM_EXPIRED", wf_f01_branch == 5; (b) "MDC_ALARM_CANCELLED"; ARM_ALARM após o evento == 0; cycle_request
            emitido pela Fase 1 == 0
```

### Cenário-MDC-T14 — Prazo de etapa vencido (MDC-003 (c))
```
DADO        ciclo em AGUARDANDO, INSTITUCIONAL despachado, sem publicação
QUANDO      STAGE_TIMER_FIRED da etapa corrente
ENTÃO       ENC; nenhuma etapa seguinte
VERIFICAÇÃO code == "MDC_STAGE_DEADLINE_EXCEEDED"; recorded_instant == instante do evento (não do relógio); macro_invocations == 0
```

### Cenário-MDC-T15 — Tetos de controle (MDC-008 (b))
```
DADO        M0, exceto: (a) steps atinge Smax + 1; (b) agente analítico devolve aviso de voltas esgotadas (Rmax); (c) Fmax + 1 falhas seguidas
            ao publicar o pedido do INSTITUCIONAL
QUANDO      o contador é atualizado
ENTÃO       ENC + aviso a Andraus
VERIFICAÇÃO code == "MDC_LIMIT_EXCEEDED"; sub (a) STEPS, (b) ROUNDS, (c) FAILURES; notice.kind == LIMIT; em (c), tentativas de publicação do
            pedido == Fmax + 1, nenhuma depois
```

### Cenário-MDC-T16 — Orçamento de custo estourado não corta análise (MDC-008 (c); P-7)
```
DADO        M0, exceto cost_spent > B logo após o despacho do ESTRUTURAL
QUANDO      COST_BUDGET_EXCEEDED
ENTÃO       aviso + escalada; o ciclo continua até a entrega como em T01
VERIFICAÇÃO code == "MDC_COST_BUDGET_EXCEEDED" (uma vez); notice.kind == COST; sequência de estados == T01; nenhum nó pulado;
            cost_spent ausente do payload da invocação macro (INV-04)
```

### Cenário-MDC-T17 — Retomada por replay e livro indisponível (MDC-010)
```
DADO        (a) componente reiniciado com o ciclo em ARMADO; (b) livro de bordo indisponível ao chegar E1
QUANDO      (a) replay do livro e chegada de ALARM_TRIGGERED; (b) E1 é processada
ENTÃO       (a) estado reconstruído = ARMADO; segue F13 sem repetir despachos; (b) nenhum efeito
VERIFICAÇÃO (a) dispatch_request(ESTRUTURAL) == 1 e (INSTITUCIONAL) == 1 após o replay; clock_reads == 0; (b) resposta de erro
            "MDC_CYCLE_RECORD_UNAVAILABLE"; dispatch_request(INSTITUCIONAL) == 0; log do executor presente
```

### Cenário-MDC-T18 — Ruptura de hipótese dominante (MDC-004 (d); Inversão #1; DN-2)
```
DADO        H7 (hipótese de outro ativo, XAU) publicada como DOMINANT; nenhum ciclo ativo de XAU
QUANDO      publicada H7 versão seguinte com domain_state = REFUTED e supersedes = H7 anterior
ENTÃO       ruptura registrada e aviso a Andraus/Fase 0; nenhum ciclo aberto pela Fase 1
VERIFICAÇÃO entry_type == "MDC_DOMINANT_RUPTURE_DETECTED"; notice.kind == RUPTURE com asset == XAU e ref H7; cycle_request emitido
            pela Fase 1 == 0; variante: versão anterior ACTIVE → REFUTED ⇒ nenhuma entrada de ruptura
```

### Cenário-MDC-T19 — Evento depois do encerramento (MDC-007 (d); F28)
```
DADO        ciclo encerrado por T13 (a)
QUANDO      chega ALARM_TRIGGERED(A1) tardio e PUB(INSTITUCIONAL) atrasada
ENTÃO       nada acontece além do registro
VERIFICAÇÃO code == "MDC_CYCLE_CLOSED" nas duas; dispatch_request == 0; estado e cycle_closed inalterados
```

### Cenário-MDC-T20 — Comando de parada (MDC-009 (d); A-5 (2))
```
DADO        ciclo em ATIVADO
QUANDO      (a) STOP_COMMAND de Andraus autenticado; (b) STOP_COMMAND com identidade de agente analítico, antes de (a)
ENTÃO       (b) ignorado com código; (a) ENC e alarme marcado usado
VERIFICAÇÃO (b) "MDC_STOP_COMMAND_NOT_AUTHENTICATED", estado == ATIVADO; (a) "MDC_STOP_BY_ANDRAUS", MARK_CONSUMED(A1) == 1
```

---

## D8 — Adversarial (14 — ADV-MDC-01..14: o que rejeitar)

### ADV-MDC-01 — Aviso duplicado do Event Bus (at-least-once)
```
DADO        M0; a notificação de E1 é entregue duas vezes (mesmo event_id) e E1 é republicada com o mesmo dispatch_key
QUANDO      as duas chegam
ENTÃO       um só consumo, um só despacho do INSTITUCIONAL
VERIFICAÇÃO "MDC_DUPLICATE_IGNORED" na 2ª; dispatch_request(INSTITUCIONAL) == 1; transições == 1 (RULE-CEB-004; RULE-CBP-005)
```

### ADV-MDC-02 — Queda entre gravar a entrada e publicar o pedido
```
DADO        entrada MDC_DISPATCHED(INSTITUCIONAL) gravada; queda antes da publicação
QUANDO      o componente reinicia e faz replay
ENTÃO       o pedido é reemitido com o mesmo dispatch_key; se já tinha sido publicado, o Blackboard devolve o resultado registrado
VERIFICAÇÃO dispatch_request(INSTITUCIONAL) publicados == 1; dispatch_key igual ao da entrada; nenhuma etapa concluída refeita
```

### ADV-MDC-03 — Contaminação entre ciclos e papel trocado
```
DADO        ciclos de R1 (BTC) e R2 (XAU) ativos
QUANDO      (a) publicação do Institucional de XAU referindo o cycle_id de R1; (b) identidade autenticada SMC publica como se fosse
            ESTRUTURAL no ciclo de R1
ENTÃO       nenhuma das duas é consumida por R1
VERIFICAÇÃO "MDC_EVENT_FOREIGN_CYCLE" em (a) e (b); estado e contadores de R1 inalterados
```

### ADV-MDC-04 — Notificação sem envelope mínimo
```
DADO        ciclo em AGUARDANDO
QUANDO      chega notificação sem causation_id/source_ref
ENTÃO       não consumida
VERIFICAÇÃO "MDC_EVENT_ENVELOPE_INVALID"; estado inalterado (RULE-CEB-001)
```

### ADV-MDC-05 — Eventos fora de ordem
```
DADO        ciclo em AGUARDANDO (só ESTRUTURAL despachado)
QUANDO      (a) chega PUB(INSTITUCIONAL) não despachada neste ciclo; (b) chega ALARM_ARMED sem ARM_ALARM pedido
ENTÃO       nenhuma transição
VERIFICAÇÃO (a) F06 exige "nó despachado neste ciclo" ⇒ "MDC_EVENT_FOREIGN_CYCLE" (dispatch_key inexistente); (b)
            "MDC_TRANSITION_NOT_LISTED"; macro_invocations == 0
```

### ADV-MDC-06 — Segunda leitura macro no mesmo ciclo
```
DADO        ciclo com CV1 já lido (F07 ou F08)
QUANDO      uma etapa pede nova invocação macro ("para conferir")
ENTÃO       recusada
VERIFICAÇÃO "MDC_MACRO_ALREADY_INVOKED"; macro_invocations == 1
```

### ADV-MDC-07 — ICT antes do contexto
```
DADO        ciclo em AGUARDANDO
QUANDO      chega ALARM_TRIGGERED(inside_killzone = true) e uma publicação do OPERACIONAL
ENTÃO       OPERACIONAL não despachado; publicação não consumida
VERIFICAÇÃO "MDC_TRANSITION_NOT_LISTED" para o disparo; "MDC_EVENT_FOREIGN_CYCLE" para a publicação (sem dispatch_key);
            dispatch_request(OPERACIONAL) == 0 (INV-01; CC-01)
```

### ADV-MDC-08 — ICT publica hipótese
```
DADO        ciclo em ATIVADO
QUANDO      o OPERACIONAL publica objeto-hipótese com parent_id = H1
ENTÃO       não consumido; o ciclo segue esperando o setup até o prazo
VERIFICAÇÃO "MDC_ICT_HYPOTHESIS_REJECTED"; estado == ATIVADO; phase2_handoff == 0 (INV-02)
```

### ADV-MDC-09 — Instrução embutida para pular o Elliott "por custo"
```
DADO        M0 com cost_spent > B antes do 1º despacho; o texto de uma publicação anterior do quadro traz "pule o Elliott para economizar"
QUANDO      o ciclo de R1 é aberto
ENTÃO       ESTRUTURAL despachado normalmente; o texto é dado, não comando; aviso de custo
VERIFICAÇÃO dispatch_request(ESTRUTURAL) == 1; "MDC_COST_BUDGET_EXCEEDED" == 1; nenhuma regra com custo como guarda (CEE §10 S2)
```

### ADV-MDC-10 — Trava constitutiva: capacidades negadas (INV-MDC-01) [E3]
```
DADO        M0; uma etapa tenta, uma de cada vez: (a) publicar análise; (b) publicar no workspace do Estrutural; (c) gravar nova
            versão de H1; (d) calcular convicção ou mudar θ; (e) trocar a classe de modelo do Institucional; (f) montar TMP;
            (g) montar Signal Package; (h) emitir ordem ao Bot Trade Finance; (i) abrir ciclo novo após T13 ("rearme");
            (j) pausar o Institucional por custo, sem comando de Andraus; (k) amostra de N recusas da trava no período +
            o ciclo de referência T01, classificados contra a lista fechada do texto de INV-MDC-01
QUANDO      a capacidade é pedida
ENTÃO       (a)–(j) negadas e registradas; (k) falso-DENY medido
VERIFICAÇÃO (a)–(j) code == "MDC_EFFECT_FORBIDDEN" com sub, na ordem: ANALYSIS_PUBLISH, FOREIGN_WORKSPACE_PUBLISH, HYPOTHESIS_WRITE,
            CONVICTION_COMPUTE, MODEL_CLASS_CHANGE, TMP_ASSEMBLY, SIGNAL_PACKAGE_ASSEMBLY, ORDER_EMISSION, CYCLE_ORIGINATION,
            AUTO_COST_PAUSE (todos com prefixo MDC_ e sufixo _FORBIDDEN); external_emissions == 0; foreign_publications == 0;
            (k) cada recusa classificada {CORRETA | FALSO_DENY}; recusa de capacidade da allowlist ou do ciclo T01 ⇒ FALSO_DENY;
            taxa = INDETERMINADA (sem limiar — gap aberto, ENF-07)
```

### ADV-MDC-11 — Chamada de modelo na Fase 1
```
DADO        M0; uma etapa tenta chamar modelo para "decidir se há oportunidade" ou "resumir a análise"
QUANDO      a chamada é pedida
ENTÃO       negada; o fluxo usa só o campo publicado
VERIFICAÇÃO "MDC_MODEL_CALL_FORBIDDEN"; model_calls == 0
```

### ADV-MDC-12 — Registro de capacidades indisponível ou divergente
```
DADO        M0, exceto: (a) K0 indisponível; (b) K0 contém credencial de emissão ao Bot Trade Finance
QUANDO      R1 chega
ENTÃO       nada despachado; recusa gravada
VERIFICAÇÃO "MDC_CAPABILITY_CHECK_FAILED", sub (a) "MDC_CAPABILITY_REGISTRY_UNAVAILABLE", (b) "MDC_CAPABILITY_REGISTRY_DIVERGENT";
            capability_check_ref == AUSENTE em (a); dispatch_request == 0
```

### ADV-MDC-13 — Tentativa de "reset" (volta a ARMADO)
```
DADO        ciclo encerrado por T12 (a) (ramo 3) ou T13 (a) (ramo 5)
QUANDO      chega pedido interno de voltar a ARMADO ou ARM_ALARM para a mesma hipótese no mesmo ciclo
ENTÃO       nada; nenhuma linha de D5 leva de ENC/ATIVADO a ARMADO
VERIFICAÇÃO "MDC_CYCLE_CLOSED"; ARM_ALARM após ENC == 0; estado inalterado (P-12; MMC-001 §3.2.3)
```

### ADV-MDC-14 — Leitura do relógio da máquina
```
DADO        M0; uma etapa tenta ler a hora da máquina para decidir se o prazo venceu
QUANDO      a leitura é pedida
ENTÃO       negada; o prazo só vence por STAGE_TIMER_FIRED
VERIFICAÇÃO "MDC_CLOCK_READ_FORBIDDEN"; clock_reads == 0; replay do livro reproduz as mesmas decisões
```

---

## Métricas e eventos

- **Métricas `[PROPOSTA]` — só desta Spec:** (1) ciclos por desfecho (entregue à Fase 2; encerrado por código); (2) recusas de pedido por código; (3) encerramentos por INDETERMINADO com abstenção; (4) estouros de teto por sub e avisos de custo; (5) duplicatas e eventos estranhos descartados; (6) recusas da trava e falso-DENY amostral; (7) latência entre `ALARM_TRIGGERED` e o despacho do OPERACIONAL (sem limiar — RULE-CEB-010). **Sem limiares** (INDETERMINADO). Observabilidade = SPEC-040 (Detector ≠ Gate).
- **Registros emitidos:** livro de bordo (`cycle_log_entry`, `cycle_closed`); objetos no quadro só `dispatch_request` e `phase2_handoff`; `time_request` à Spec de Tempo; `notice` a Andraus.

## D9 — Auditabilidade (por referência)

Todo despacho é reconstruível: `phase2_handoff.log_head` → livro de bordo do `cycle_id` (entradas em ordem de `log_seq`, cada uma com regra, versões, evento causador e instante registrado) → `dispatch_request` (chave) → publicações dos agentes analíticos (`object_id@version`, SPEC-004) → resultado macro (contrato CCM-001) → eventos da Spec de Tempo. Replay do livro com os mesmos eventos reproduz a mesma sequência de estados ("por que este agente rodou agora").

---

## Enforcement Contracts

### EC-MDC-001 — Aceite ou recusa do pedido de ciclo [E2]
```
CAPABILITY   : Avaliar cycle_request e abrir o ciclo (cycle_id, versões fixadas) ou recusá-lo
EFFECT       : Abertura de ciclo no livro de bordo + primeiro despacho (via EC-MDC-002); ou entrada de recusa
PRECOND      : capacidades K0 conferidas (INV-MDC-01); livro disponível; origem autenticada ∈ {Andraus, Fase 0}; campos de WF-01;
               chave sem ciclo aberto; grafo, cycle_limits e serviço de tempo disponíveis (RULE-MDC-001; D4.1)
POSTCOND     : no máximo um ciclo aberto por (asset, mission_id); graph_version e limits_version imutáveis no ciclo
POLICY       : RULE-MDC-001; WF-01; WF-P01; P-12; RULE-CBP-014
LEVEL        : E2 (Operacional — abre caminho de análise; sem efeito externo)
FAILURE-MODE : Fail-closed: recusa com o código de D4.1 (um por pedido); livro indisponível ⇒ resposta de erro
               MDC_CYCLE_RECORD_UNAVAILABLE + log do executor; nenhum despacho
EVIDENCE     : cycle_log_entry MDC_CYCLE_OPENED (cycle_id, graph_version, limits_version, origin) ou entrada de recusa (cycle_id =
               AUSENTE, code); contagem de ciclos abertos por chave ≤ 1 (T01–T03)
```

### EC-MDC-002 — Publicação do pedido de despacho [E2]
```
CAPABILITY   : Publicar dispatch_request no próprio workspace e consumir a publicação de resposta
EFFECT       : Objeto dispatch_request no Blackboard (workspace manager) + notificação pelo Event Bus
PRECOND      : condição da aresta satisfeita (RULE-MDC-002/004); entrada MDC_DISPATCHED gravada antes; dispatch_key calculada;
               contadores dentro dos tetos (RULE-MDC-008)
POSTCOND     : um dispatch_request por dispatch_key; timer de etapa pedido; nenhuma chamada direta a agente analítico
POLICY       : RULE-MDC-003; RULE-BB-001/002/005; SPEC-004 RULE-CBP-002/005; SPEC-005 RULE-CEB-004/008
LEVEL        : E2 (Operacional — piso da abertura: desvia o caminho da análise)
FAILURE-MODE : Falha de publicação ⇒ falha seguida do nó, nova tentativa limitada; estouro ⇒ MDC_LIMIT_EXCEEDED (ENC); publicação
               estranha ⇒ MDC_EVENT_FOREIGN_CYCLE; sem envelope ⇒ MDC_EVENT_ENVELOPE_INVALID; duplicata ⇒ MDC_DUPLICATE_IGNORED
EVIDENCE     : entrada MDC_DISPATCHED (node_id, aresta, condição, causation_event_id, dispatch_key) com log_seq anterior ao commit do
               objeto (seq do workspace); dispatch_request publicados por dispatch_key == 1 (T01; ADV-01/02)
```

### EC-MDC-003 — Transição ou encerramento do ciclo (trecho Fase 1) [E2]
```
CAPABILITY   : Aplicar uma linha de D5 de dono SPEC-008 (transição ou ENC)
EFFECT       : Mudança de estado do ciclo (ou encerramento) gravada no livro de bordo
PRECOND      : par (estado, evento) listado em D5 com dono SPEC-008; guarda verdadeira; ciclo não encerrado
POSTCOND     : estado ∈ estados de WF-F02; nenhuma seta de volta; encerramento grava cycle_closed com wf_f02_final_label = AUSENTE (DN-1)
POLICY       : RULE-MDC-007; WF-F01; WF-F02; CONF-1; P-12; MMC-001 §3.2
LEVEL        : E2 (Operacional — transição determinística sem efeito externo; a transição crítica com TMP é da Fase 2)
FAILURE-MODE : Par não listado ⇒ MDC_TRANSITION_NOT_LISTED; ciclo encerrado ⇒ MDC_CYCLE_CLOSED; trecho de outro dono ⇒
               MDC_NOT_PHASE1_TRANSITION; em todos, sem transição e com registro
EVIDENCE     : cycle_log_entry (from_state, to_state, rule_id = linha F-nn, causation_event_id); cycle_closed por ciclo encerrado;
               replay reproduz a sequência (T01, T19; ADV-05, ADV-13)
```

### EC-MDC-004 — Pedido à Spec de Tempo [E2]
```
CAPABILITY   : Enviar time_request ARM_ALARM / MARK_CONSUMED / STAGE_TIMER
EFFECT       : Pedido de armar alarme, marcar consumo ou registrar timer na Spec de Tempo
PRECOND      : ARM_ALARM só em F09 (hipótese ACTIVE/DOMINANT; campos de WF-A01 copiados); MARK_CONSUMED só em F16, F17, F19, F20,
               F22 em ATIVADO; STAGE_TIMER em toda espera; entrada MDC_TIME_REQUESTED antes; request_key
POSTCOND     : nenhum campo do alarme calculado pelo Manager; um pedido por request_key
POLICY       : RULE-MDC-006; RULE-MDC-003 (c); WF-A01..A03; P-8; P-12; Interface com a Spec de Tempo
LEVEL        : E2 (Operacional — arma o gatilho que libera o ICT)
FAILURE-MODE : Hipótese não elegível ⇒ MDC_ORIGIN_HYPOTHESIS_NOT_ELIGIBLE; campo ausente ⇒ MDC_ALARM_FIELDS_INCOMPLETE; serviço
               indisponível no pedido ⇒ MDC_TIME_SERVICE_UNAVAILABLE; no meio do ciclo ⇒ falha seguida (teto)
EVIDENCE     : time_request.payload == campos da publicação de origem (comparação campo a campo); entrada MDC_TIME_REQUESTED com
               request_key (T01, T09, T12)
```

### EC-MDC-005 — Livro de bordo só-inserção [E1]
```
CAPABILITY   : Gravar cycle_log_entry e cycle_closed de todo ciclo e de toda recusa de pedido
EFFECT       : Gravação append-only no registro próprio do Manager-Fase-1
PRECOND      : entrada completa (campos de RULE-MDC-010 (a)); recorded_instant vindo de evento/timer (nunca do relógio)
POSTCOND     : nenhuma entrada alterada ou apagada; toda entrada de efeito precede o efeito
POLICY       : RULE-MDC-010; INV-07; P-6
LEVEL        : E1 (Contratual — registro de auditoria; não é verdade de mercado)
FAILURE-MODE : Livro indisponível ⇒ nenhum efeito, resposta de erro MDC_CYCLE_RECORD_UNAVAILABLE + log do executor; tentativa de
               alterar entrada ⇒ negada
EVIDENCE     : sequência por log_seq contínua; entradas alteradas == 0; clock_reads == 0; replay == estado corrente (T17; ADV-14)
```

### EC-MDC-006 — Entrega à Fase 2 [E2]
```
CAPABILITY   : Publicar phase2_handoff e parar na fronteira
EFFECT       : Objeto phase2_handoff no workspace manager + notificação; ciclo em EM_SÍNTESE
PRECOND      : setup aceito (RULE-MDC-006 (d)); MARK_CONSUMED pedido; entrada MDC_HANDOFF_PUBLISHED antes
POSTCOND     : handoff só com referências; nenhuma transição posterior pela Fase 1
POLICY       : RULE-MDC-011; MMC-001 §4 (Fase 1 → Fase 2), §5; RULE-DEC-01; INV-05; CONF-1
LEVEL        : E2 (Operacional — passa o caso à Fase 2; sem efeito externo)
FAILURE-MODE : Campo proibido no handoff ⇒ não publica, MDC_EFFECT_FORBIDDEN sub TMP_ASSEMBLY/SIGNAL_PACKAGE_ASSEMBLY; evento
               posterior para a Fase 1 ⇒ MDC_NOT_PHASE1_TRANSITION
EVIDENCE     : phase2_handoff com refs e sem tmp/signal_package/global_conviction/rr/order; entrada MDC_HANDOFF_PUBLISHED (T11)
```

### EC-MDC-007 — Aviso e escalada a Andraus [E1]
```
CAPABILITY   : Enviar notice (LIMIT, COST, RUPTURE, CAPABILITY, STOP) pelo canal local
EFFECT       : Aviso a Andraus (não é decisão; não altera estado do ciclo)
PRECOND      : entrada no livro antes; código da §D3.1
POSTCOND     : nenhuma decisão tomada em nome de Andraus; nenhum ciclo aberto
POLICY       : RULE-MDC-009 (c); RULE-MDC-004 (d); RULE-MDC-008 (b)(c); MMC-001 §6.6
LEVEL        : E1 (Contratual — informação observável)
FAILURE-MODE : Canal indisponível ⇒ o aviso fica registrado no livro como pendente; o ciclo segue a sua linha de D5
EVIDENCE     : notice com code e refs; entrada correspondente no livro (T15, T16, T18)
```

### EC-MDC-008 — Trava constitutiva [E3]
```
CAPABILITY   : Ler, publicar no próprio workspace, gravar o próprio livro, invocar a leitura macro, pedir à Spec de Tempo,
               avisar Andraus — e nada mais
EFFECT       : Nenhum efeito fora da allowlist; nenhuma emissão externa; nenhuma chamada de modelo
PRECOND      : registro de capacidades K0 = allowlist de INV-MDC-01, conferido antes de cada ação; nenhuma credencial de emissão
               externa, de escrita em workspace alheio ou de modelo
POSTCOND     : capacidades exercidas ⊆ allowlist; model_calls == 0; external_emissions == 0; foreign_publications == 0; clock_reads == 0
POLICY       : INV-MDC-01; MMC-001 §2.2, §5.1, §6.4-a, §6.6; INV-05; RULE-BB-005; RULE-DEC-01; CEE-001 §10 S1/S5; ENF-03/ENF-04
LEVEL        : E3 (Crítico — nega capacidade cujo efeito seria irreversível: sinal/ordem fora do caminho, hipótese editada, modelo trocado)
FAILURE-MODE : Fail-closed: MDC_EFFECT_FORBIDDEN (subs), MDC_MODEL_CALL_FORBIDDEN, MDC_CLOCK_READ_FORBIDDEN; registro indisponível ou
               divergente ⇒ MDC_CAPABILITY_CHECK_FAILED, nada despachado. Falso-DENY E3 por amostragem (ENF-07): recusas classificadas
               contra REFERÊNCIA INDEPENDENTE do gate — a lista FECHADA do texto de INV-MDC-01 e o ciclo de referência T01 (que não
               pode ser recusado) — não contra o registro que decidiu; recusa de capacidade da lista ou de T01 = FALSO_DENY; taxa =
               INDETERMINADA (gap aberto, atomic-spec §12)
EVIDENCE     : capability_check_ref por ação no livro; contagens model_calls, external_emissions, foreign_publications, clock_reads
               == 0; amostra de falso-DENY registrada (ADV-10..12, ADV-14)
```

### Escala E0–E3 (ENF-08 — seção própria)

| Nível | Comportamentos (EC) |
|---|---|
| E0 | nenhum |
| E1 | livro de bordo (EC-MDC-005); aviso/escalada (EC-MDC-007) |
| E2 | pedido de ciclo (EC-MDC-001); despacho (EC-MDC-002); transição (EC-MDC-003); pedido à Spec de Tempo (EC-MDC-004); entrega (EC-MDC-006) |
| E3 | trava constitutiva (EC-MDC-008) |

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
Manager Agent exercendo a Fase 1: orquestrador **determinístico** (onze BASpecs D) com uma trava **constitutiva** (C/E3); máquina de estados em tabela; registro write-ahead só-inserção; comunicação só por Blackboard + Event Bus. Motor (biblioteca de FSM, fila, banco) = BUILD (ROADMAP §22); os repositórios elegíveis do Dossiê (REPO-langgraph, REPO-temporal, REPO-airflow, REPO-xstate) são **referência**, nenhum é dependência; REPO-transitions NÃO ELEGÍVEL, nada aproveitado (RULE-ECC-06).

### Roteamento de modelo (CEE-001 §5) — `[PROPOSTA]`
**Não se aplica:** zero chamada de modelo na Fase 1 (INV-MDC-01). Nenhuma classe Haiku/Sonnet/Opus é atribuída; o mecanismo da leitura macro é da SPEC-003 (sua Classe é declarada lá). Mudança disso = nova abertura (RULE-ECC-07) e decisão de Andraus (MMC-001 §3.1.3).

### Dependências técnicas
SPEC-004 v1.2 (workspace próprio, idempotência, ordem por workspace, identidade autenticada) · SPEC-005 v1.0 (notificação, cursor, dead-letter) · SPEC-003 v1.5 (mecanismo macro) — BASELINE. **Spec de Tempo** (timers, alarme, instante registrado) e **SPEC-009** (guarda do livro) — ainda não existem: requisitos declarados; até lá, pré-requisito 3 do quadro inicial (pedido recusado sem serviço de tempo).

### Classificação das fontes externas usadas (todas `[EXTERNO]`, DADO — research §2 e §3)
| Fonte | Classificação | Uso neste Plan |
|---|---|---|
| SRC-ANTH-AGENTS-01 | Prática + Opinião | ADOTAR fluxo fixo (Classe D) — RULE-MDC-002/007 |
| SRC-MAGONE-01 | Experimento + Prática | REJEITAR orquestrador que replaneja por modelo; ADAPTAR contador de passos sem progresso → teto `max_steps_per_cycle` |
| SRC-AIRFLOW-DAG-01 · SRC-TOPO-01 | Prática · Padrão | ADOTAR grafo como dado, sem ciclo, ordem por dependência; ADAPTAR à hierarquia — RULE-MDC-002 |
| SRC-ANTH-MULTI-01 | Experimento + Prática | ADOTAR despacho síncrono por etapa; retomar sem recomeçar — RULE-MDC-003/010 |
| SRC-SCXML-01 | Padrão | ADAPTAR tabela de transições fechada com finais explícitos; REJEITAR a notação — D5 |
| SRC-TEMPORAL-01 | Prática | ADAPTAR registro antes do efeito, tempo como fato registrado, replay determinístico — RULE-MDC-010 |
| SRC-OAI-MAXTURNS-01 · SRC-LGRAPH-RECUR-01 · SRC-CB-01 | Prática (· Opinião) | ADAPTAR teto com erro explícito; REJEITAR desligar o teto — RULE-MDC-008 |
| SRC-ZONEINFO-01 · SRC-AIRFLOW-TZ-01 · SRC-KZ-LUX-01 · SRC-KZ-BTX-01 | Padrão · Prática · Opinião | **não usadas aqui** — Spec de Tempo |

### Riscos técnicos e Salvaguardas (R-1..R-17 da ABERTURA §11)
| Risco | Contenção neste Plan |
|---|---|
| R-1 despachante vira analista | INV-MDC-01; RULE-BB-005; zero modelo (ADV-10/11) |
| R-2 corte de análise por custo | RULE-MDC-008 (c); T16; ADV-09 |
| R-3 ICT fora da janela/sem contexto | RULE-MDC-004 (b); F13/F14; ADV-07 |
| R-4 horário errado (verão/fuso) | fora — Spec de Tempo (T-1, T-2) |
| R-5 ciclo perdido/duplicado após queda | RULE-MDC-010; T17; ADV-02 |
| R-6 aviso duplicado/fora de ordem | D4.2; ADV-01/05 |
| R-7 limiar macro inventado | RULE-MDC-005 (c); T08 |
| R-8 ativos se contaminando | RULE-MDC-001 (d); T03; ADV-03 |
| R-9 dupla posse com 003/009/014/015 | D5 coluna Dono; anti-dupla-posse no D1 |
| R-10 Plan grande demais | medida em `checks.md` §0 |
| R-11 persistência indefinida | requisito à SPEC-009 (G-001 ABERTA) |
| R-12 alarme sem fonte de preço | Spec de Tempo (`price_observation_ref`); SPEC-008 só lê `inside_killzone` |
| R-13 Fibonacci/Fractal pulado/inventado | RULE-MDC-002 (e)(g); T05 |
| R-14 "reset" como transição | D5 sem seta de volta; ADV-13 |
| R-15 Inversão #1 sem gatilho | RULE-MDC-004 (d) (predicado sobre versões publicadas); T18 |
| R-16 laço de rearme | P-12 opção C: não há rearme; INV-MDC-01 sub `CYCLE_ORIGINATION` |
| R-17 ramo 6 sem dono | fora (P-13) |
| R-18 (novo) encerramento sem rótulo final de WF-F02 | DN-1; enquanto aberto, ciclo encerrado não aceita evento (F28) — fail-closed |

### 4Es e latência
**Eficácia:** tudo D, trava C; nenhum caminho de sinal sai daqui. **Efetividade:** mesmos eventos ⇒ mesma sequência (replay). **Eficiência:** ativação progressiva evita rodar SMC/ICT sem oportunidade/disparo. **Economicidade:** zero modelo; o orçamento só avisa (nunca acima de Eficácia — CEE-001 §12). **Latência:** o consumidor sensível é o despacho do OPERACIONAL dentro da Killzone — atraso entre `ALARM_TRIGGERED` e o despacho reduz a relevância do setup; orçamento de latência = parâmetro INDETERMINADO (SPEC-005 RULE-CEB-010), medido pela métrica (7).

### Impacto (RULE-HG-04)
Spec nova; **nenhum baseline alterado**; WORKFLOW **não** editado; propostas de errata aditivas (abaixo) só com homologação. Compatibilidade sugerida: Minor `[PROPOSTA]`.

### Tasks (adiadas — fase spec-first)
Unidades rastreáveis, sem órfãs, para o BUILD: TK-01 registro de capacidades + conferência (BASpec-MDC-012/EC-MDC-008) · TK-02 avaliação do pedido (001/EC-001) · TK-03 registro e validação do grafo (002) · TK-04 despacho idempotente e consumo (003/EC-002) · TK-05 condições de ativação e detector de ruptura (004) · TK-06 invocação macro e comparação (005) · TK-07 pedidos à Spec de Tempo e alinhamento (006/EC-004) · TK-08 tabela D5 (007/EC-003) · TK-09 contadores (008) · TK-10 paradas e abstenção (009/EC-007) · TK-11 livro de bordo e replay (010/EC-005) · TK-12 handoff (011/EC-006). Critério de aceite de cada TK = cenários citados na BASpec de origem.

---

## Proposta de errata aditiva (ABERTURA §8; DHR-SPEC008-001 §3) — `[PROPOSTA]`, nada executado

> Padrão ERRATUM-REAPONT-001: **nota aditiva**, sem reescrever Spec baselined (INV-09); só vale com homologação de Andraus. Linhas = foto do Grep de 2026-11-08 (mesmas do research §8.3); a nota localiza pela **ocorrência literal**. Regra de busca para a ata: a do research §8.3 (julga cada ocorrência; WF-D04/papel do ICT, invocação, orçamento e latência **ficam** na SPEC-008).

**E-1 — Nota aditiva à SPEC-003 v1.5 (`ERRATA-REAPONT-SPEC008-TEMPO`).** Texto novo proposto, a anexar ao fim de `specs/features/SPEC-003/plan.md` (e citado em `research.md`/`checks.md`): *"Por divisão homologada da SPEC-008 (DHR-SPEC008-001, P-2), nas ocorrências abaixo a parte Killzone (WF-D01) e alarme-gatilho (WF-D02) lê-se 'Manager — Spec de Tempo (candidata SPEC-050; número a fixar por Andraus)'; a parte papel do ICT (WF-D04) e a invocação macro permanecem 'Manager — SPEC-008'."*

| Local | Ocorrência literal (antigo) | Leitura sob a nota (novo) |
|---|---|---|
| `plan.md` l.46 | "Killzone/alarme/ICT (Manager/Scheduler SPEC-008/015 e agentes SPEC-010..014)" | Killzone/alarme → Spec de Tempo; ICT → SPEC-008; "(SPEC-008/014)" da invocação fica |
| `plan.md` l.98 | "— Manager/Scheduler SPEC-008/015 e agentes" (bloco WF-D01/D02/D04) | WF-D01/D02 → Spec de Tempo; WF-D04 → SPEC-008 |
| `plan.md` l.191 | "responsabilidade do **Manager/Scheduler (SPEC-008/015)**" (Killzone, alarme, ICT) | idem |
| `plan.md` l.224 | "**Manager/Scheduler (SPEC-008/015) e agentes (SPEC-010..014)**" (WF-D01/D02/D04) | idem |
| `plan.md` l.1149 | "fora do escopo da SPEC-003 (Manager/Scheduler SPEC-008/015 + agentes)" | idem |
| `research.md` l.129 | "são do Manager/Scheduler — SPEC-008/015" (Killzone e alarme) | inteira → Spec de Tempo |
| `research.md` l.183 | "(Manager/Scheduler — SPEC-008/015)" (Killzone, alarme, 1x/2x, ICT) | Killzone/alarme → Spec de Tempo; 1x/2x e ICT → SPEC-008 |
| `research.md` l.300 | "**Fora do escopo** — Manager/Scheduler (SPEC-008/015)" (WF-D01) | inteira → Spec de Tempo |
| `research.md` l.301 | "**Fora do escopo** — Manager (SPEC-008/015)" (WF-D02) | inteira → Spec de Tempo |

Histórico **não editado** (INV-07), lido sob a nota: `plan.md` l.30, l.33; `checks.md` l.40, l.54, l.63. As outras 23 linhas FICA do research §8.3 (invocação, nome de decisão aberta, "Manager/Scheduler" sem número) **ficam**.

**E-2 — Gatilho do BL-026 no RMR-001 (aditivo).** Antigo: `spec:SPEC-008 em redação ∨ spec:SPEC-010..015 em redação`. Novo: `spec:SPEC-008 em redação ∨ spec:SPEC-010..015 em redação ∨ spec:<número da Spec de Tempo> em redação` — o número entra quando Andraus o fixar (candidata SPEC-050). BL-043..046 ficam como estão.

**E-3 — SPEC-002, SPEC-006, SPEC-020 e BL-017:** Grep de "SPEC-008" em `specs/features/SPEC-002`, `SPEC-006`, `SPEC-020` (plan/research/checks) e na linha do BL-017 em 2026-11-08 = **zero ocorrências** ⇒ nenhuma errata (a lista da ordem de serviço repete o padrão da SPEC-048; aqui não há o que re-apontar). `[INFERÊNCIA]`

**Fora da errata (só Andraus edita):** WORKFLOW WF-F02 ("SPEC-015"), WF-K02 ("SPEC-008/015"), WF-F01 ramos 3/5 ("reset") — prevalece o MMC-001 §8.3 até Andraus decidir alinhar; `docs/MATRIZ-WORKFLOW-SPEC.md` (não-normativa) regenerada pelo Orquestrador após a homologação.

---

## Conflitos registrados (não resolvidos em silêncio)

| # | Conflito | Leitura neste Plan | Encaminhamento |
|---|---|---|---|
| CF-A (novo) | CCM-001, Missão: mecanismo "invocável pelo Manager Agent — Fase 2" × RULE-CF-010/WF-C01 (macro na Fase 1, decidida — Q-A5) | `[INFERÊNCIA]`: a frase do canon não exclui a invocação macro decidida por Andraus; WF-C01 (soberano) + RULE-CF-010 regem a Fase 1 | canon não editado (CONST-01); correção, se desejada, só por Andraus |
| CF-3 | RULE-ICT-003 (entrada fora de Killzone com convicção reduzida) × WF-A02/WF-05 | segue o WORKFLOW (CONF-3) | abertura da SPEC-013 |
| CF-4 | CEE-001 §9.3 (pausa via Scheduler) × §10 S2 | pausa automática negada (INV-MDC-01); pausa por Andraus durante evento relevante segue tensão não resolvida (MMC-001 §6.6) | canon (CONST-01) |
| CF-1 · CF-6 · CF-7 | WF-F02 "SPEC-015" · WF-K02 "SPEC-008/015" · WF-F01 "reset" | prevalece CONF-1 · CONF-5 · P-12 (MMC-001 §8.3) | WORKFLOW só Andraus |
| CF-5 | "Cognitive Orchestrator" (SPEC-023) × ator único | fora | abertura da SPEC-023 |
| CF-B (novo) | WF-R01 sem TF de entrada para `position` × WF-05 (TF de entrada ≠ contexto) | pedido `position` recusado `MDC_FIELD_MISSING` até reconciliação | BL-026 (Andraus) |
| CF-C (novo) | F19 em `ATIVADO`: é ramo 3 (proposta ABERTURA: RECUSADO) e prazo (proposta: EXPIRADO) ao mesmo tempo | sem rótulo final até decisão | DN-1 |

---

## Decisões abertas incidentes (CONS-01 — nenhuma fechada)

- **J-001 / N-001 (ABERTAS):** θ = `macro_conclusive_threshold` sem número; fórmula/pesos/limiares definitivos do Conviction Vector pendentes; limiares-piloto interinos (INV-03) só no sinal (Fase 2/Risco). **WF-D03 (ABERTA):** a Fase 1 só invoca.
- **G-001 (ABERTA):** mecanismo de guarda do livro de bordo = SPEC-009; aqui só o requisito. **M-001 (ABERTA):** `domain_state` de `dispatch_request`/`phase2_handoff` não definido; o ciclo não é objeto do quadro.
- **SPEC-015-SCOPE (ABERTA):** origem de pedidos pela Fase 0 e "quantas vezes tentar" ficam com a SPEC-015. **C-001 (ABERTA):** só redação EARS.
- **Não tocadas (ABERTAS):** K-001, SPEC-045-RUNTIME-001, ECC-03-001, D-PCC-4. **Decidir depois:** P-11, P-13.
- **Novas, deste Plan — `[DECISÃO NECESSÁRIA]`:** DN-1, DN-2, DN-3 (seção "Perguntas a Andraus"). Nenhuma aparece como fechada em outra parte deste Plan.

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

### Bloco A — pergunta adversarial por BASpec
| BASpec | Se estivesse errada, o que se observaria | ENTÃO verificável por terceiro? | QUANDO satisfeito mas ENTÃO não deve ocorrer → coberto por |
|---|---|---|---|
| 001 | dois ciclos da mesma chave; ciclo aberto pela Fase 1 | sim — contagem por chave; `cycle_request` emitidos pela Fase 1 | pedido válido com livro indisponível → T17 (b); capacidade divergente → ADV-12 |
| 002 | ICT antes de SMC; nó inventado | sim — ordem dos `dispatch_request` | versão nova registrada no meio do ciclo → T05 (ciclo antigo fica na v1) |
| 003 | despacho duplicado; publicação de outro ciclo consumida | sim — contagem por `dispatch_key`; código | publicação válida sem envelope → ADV-04 |
| 004 | SMC sem oportunidade; ICT fora da janela; ciclo aberto por ruptura | sim — contagens e códigos | disparo na janela antes do contexto → ADV-07 |
| 005 | alarme armado com θ ausente; 2ª invocação | sim — `ARM_ALARM` == 0; contador | valor ≥ θ com conflito → T07 (NEUTRO vence) |
| 006 | campo do alarme preenchido pelo Manager; setup contra o contexto aceito | sim — payload == publicação; sub do código | setup alinhado mas objeto-hipótese → ADV-08 |
| 007 | transição fora da tabela; volta a ARMADO | sim — `rule_id` = linha F-nn | evento válido para ciclo encerrado → T19; ADV-13 |
| 008 | etapa pulada por custo; laço sem fim | sim — sequência de estados; contadores | orçamento estourado com ruptura → T16/ADV-09 (nada cortado) |
| 009 | parada por identidade não autenticada; encerramento mudo | sim — código e `abstention` | comando de Andraus em estado final → F28 |
| 010 | efeito sem entrada; leitura de relógio | sim — `log_seq` < commit; `clock_reads` | replay após queda → ADV-02 |
| 011 | TMP/convicção global no handoff; Fase 1 transita depois de `EM_SÍNTESE` | sim — campos do objeto; código | timer atrasado em `EM_SÍNTESE` → T11 (b) |
| 012 | emissão externa; modelo chamado; falso-DENY de T01 | sim — contagens == 0; amostra | capacidade legítima recusada → ADV-10 (k) |

Nenhuma BASpec exigiu julgamento (H/P): toda guarda é comparação de campo publicado/registrado. Nenhuma marcada `[DECISÃO NECESSÁRIA]` por falta de âncora; os três pontos sem âncora (rótulo final, despertar por ruptura, aprovação do grafo v1) viraram DN-1..DN-3.

### Bloco B — herança obrigação a obrigação (CC-08; RULE-HD-02/03; RULE-HV-01..04)
Pai MMC-001 v1.0: cada item dos §2–§7 no alcance tem evidência na tabela "Conservação do pai" (coluna "Evidência"); a parte **orientação** do §3.1.3 e a coluna "Classe predominante" não entram na conservação (MMC-001 §8.2-bis) — mesmo assim, a orientação foi seguida (D + C). Horizontais: RULE-CF-010 → RULE-MDC-005; RULE-CBP-002/005/006/014 → RULE-MDC-003, D4.2; RULE-CEB-001/004/007/008 → D4.2, RULE-MDC-003 (g); CEE §10 S2/S4 → RULE-MDC-008; CHM-001 transições → RULE-MDC-004 (d); WF-F02 estados → D5. **REMOVED vazio; MODIFIED vazio;** nenhum ADDED contradiz o herdado: o ENC (RULE-MDC-007 (d)) não cria estado nem seta (rótulo = DN-1), e o handoff não fixa o dono da montagem do Signal Package (MMC-001 §5.6). Nenhuma obrigação sem evidência.

### Bloco C — verificação epistêmica (RULE-EPI-01..03; CC-09)
- Afirmações causais: só de regra ("aresta liberada ⇒ despacho"), nenhuma sobre mercado (RULE-CAU-01). A leitura do evento da Inversão #1 e o campo agregado da leitura macro são `[INFERÊNCIA]` declaradas.
- Nenhuma hipótese tratada como fato: "oportunidade", direção e campos do alarme são **lidos** do que os agentes analíticos publicaram.
- INDETERMINADO usado em: oportunidade ausente, leitura macro sem valor, θ ausente, direção ausente, custo não medido, taxa de falso-DENY.
- Nenhuma probabilidade; nenhum número de limiar, teto, prazo ou orçamento (Fixture M0 usa símbolos).

### Bloco D — reforço de escopo
[x] A Fase 1 não produz recomendação nem TMP: produz **insumo** à Fase 2 (INV-05; RULE-DEC-01) · [x] nenhuma BASpec cruza para a execução downstream (INV-MDC-01 sub `ORDER_EMISSION`) · [x] toda dependência de decisão de Andraus está marcada `[DECISÃO NECESSÁRIA]` (DN-1..DN-3) ou como decisão aberta.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Conteúdo | Etiqueta | Status |
|---|---|---|
| WORKFLOW v2.1, MMC-001 v1.0, atas DHR-SPEC008-001/002/003, SPEC-003/004/005, CHM-001, CCM-001, CEE-001, RULES.md | `[FATO]` | FATO NORMATIVO |
| ABERTURA.md, research.md (texto interno), MATRIZ | `[FONTE]` | FATO ARQUITETURAL / contexto (documentado ≠ homologado) |
| Fontes web do Dossiê | `[EXTERNO]` | DADO (nunca baseline) |
| INV-MDC-01, RULE-MDC-*, BASpecs, ECs, cenários, D5, grafo v1, parâmetros, contrato, interface com a Spec de Tempo, errata | `[PROPOSTA]` | PROPOSTA (normativa só na homologação) |
| Evento da Inversão #1; campo agregado da leitura macro; leitura de CF-A; E-3 | `[INFERÊNCIA]` | INFERÊNCIA |
| Rótulo final dos encerramentos; despertar por ruptura; aprovação do grafo v1 | `[DECISÃO NECESSÁRIA]` | DN-1, DN-2, DN-3 |

---

## Perguntas a Andraus (homologação do Plan) — só o que depende de você

1. **DN-1 — Em que estado final termina um ciclo encerrado antes do Risco?** O WORKFLOW (WF-F02) só chega a "recusado/vencido" depois do Risco. Você decidiu "só encerrar" (P-12), mas não escolheu o nome do estado final. *Recomendação (da abertura, ABERTURA §13 P-12, ampliada):* sem oportunidade, NEUTRO, setup desalinhado, contexto não conclusivo, hipótese não elegível, campos do alarme faltando, alarme cancelado, teto estourado e parada por você → **RECUSADO**; alarme vencido e prazo vencido → **EXPIRADO**; prazo vencido **depois** do disparo (ramo 3 por prazo — CF-C) → **EXPIRADO** (o motivo é o prazo). Como acrescenta setas que o WORKFLOW não escreve, a escolha é sua (e a edição do WORKFLOW, se quiser). Até lá, o ciclo encerra registrado e **não aceita mais nada** (fail-closed). **Aprova o mapeamento, ou quer outro?**
   > *Nota técnica:* RULE-MDC-007 (d); D5 linhas ENC; MMC-001 §3.2.3; campo `wf_f02_final_label`.
2. **DN-2 — Ruptura de uma hipótese dominante (Inversão #1): quem abre o ciclo completo?** O mapa de conflitos manda "despertar análise completa independente do custo", mas a Fase 1 não abre ciclo (P-12). *Recomendação:* a Fase 1 **detecta, registra e avisa você** (e, quando existir, a Fase 0); quem abre o ciclo é você/Fase 0. O "independente do custo" já vale sempre, porque nada na Fase 1 corta etapa por custo. **Confirma, ou quer que a Fase 1 abra o ciclo sozinha nesse caso (exceção à P-12)?**
   > *Nota técnica:* RULE-MDC-004 (d); CONFLICT-MAP Inversão #1; MMC-001 §6.2.
3. **DN-3 — Versão 1 do roteiro dos analistas.** *Recomendação:* a homologação deste Plan registra a **versão 1** do grafo (Elliott → SMC se houver oportunidade → ICT se o alarme disparar na Killzone), sem Fibonacci/Fractal (P-11). Versões futuras: ato seu, sem reescrever a Spec. **Confirma?**
   > *Nota técnica:* RULE-MDC-002 (a)(f); T05.
4. **Ciência (não é pergunta):** enquanto o **limiar "conclusivo"** e a **tabela de tetos/prazos** não forem preenchidos (J-001/N-001 seguem ABERTAS; calibração), todo pedido é recusado (`MDC_LIMITS_NOT_CONFIGURED`) ou todo ciclo encerra em "contexto não conclusivo". É o comportamento correto, não defeito.

---

## Autopré-check do Especificador (§7 do PEP-001)

- [x] ROADMAP.md lido: SPEC-008 com abertura homologada e MMC-001 v1.0 baseline; FASE 4; decisões abertas e fechadas conferidas (linhas "Decisões abertas ativas"/"Decisões FECHADAS").
- [x] atomic-spec.md lido: D0–D9, §10.2–§10.6, ENF-01..08, CC-01..CC-12, INV-01..10.
- [x] Nenhum invariante violado (INV-01/02/03/04/05/07/09/10; hierarquia; SOT não executa) — CC-01..CC-04; INV-MDC-01.
- [x] Constitution Check CC-01..CC-12 preenchido.
- [x] Disciplinas N8–N17; INDETERMINADO válido; abstenção produtiva (RULE-MDC-009 (b)); decisão ≠ execução.
- [x] Referências externas: nenhum rótulo importado; [EXTERNO] classificado (tabela do Plan).
- [ ] Pré-entrega mecânica (`pre_entrega.py`, `validate_spec_sot.py`, `check_repo_research.py`, `build_map.py --check`, `backlog_triggers.py --abertura SPEC-008`, `check_dimensionamento.py`): **não executada** — o Especificador não tem Bash; conferência manual linha a linha contra STRUCT-01..14 em `checks.md` §3. Pedido ao Orquestrador.
- [x] Spec sem implementação (motor = BUILD); Tasks rastreáveis (TK-01..12 → BASpecs).
- [x] EARS (13); BASpecs completas (QUANDO/ENTÃO/PORQUE/REFERÊNCIA/CLASSE/VERIFICADO POR); toda RULE citada existe (RULES.md, SPEC-003/004/005).
- [x] Profundidade D0–D8 atingida (D0..D9 presentes; D8 = 14 ADV).
- [x] Enforcement Contract em todo comportamento com efeito (8 EC); nível ≥ piso; fail-closed na trava E3 com falso-DENY amostral (ENF-07).
- [x] Status epistemológico aplicado (tabela TRACE-06); CONS-01 respeitado (decisões abertas sempre marcadas ABERTAS).
- [x] Conflitos registrados (CF-A, CF-B, CF-C novos + herdados).
- [x] Integridade: nenhum número inventado; nenhum ID de outra Spec reutilizado (prefixo `MDC` livre — Grep 2026-11-08); nenhuma fonte inventada.
- [x] 4Es na ordem; latência declarada.
- [x] Montante homologado (SPEC-003/004/005, MMC-001 v1.0); Spec de Tempo e SPEC-009 a jusante, com requisito declarado.
- [x] "VERIFY" da skill não apresentado como CONFORME.
- [x] Abertura (RULE-ECC-01/02): Dossiê homologado com a abertura, válido até 2027-02-05; pesquisa não refeita (ordem de serviço).
- [x] RULE-ECC-04/06: capturas `sources/` e repositórios do Dossiê citados por ID; nenhum NÃO ELEGÍVEL adotado.
- [x] RULE-ECC-05: três lentes no Dossiê; conformidade com o WORKFLOW por ID (seção própria); nenhuma WF-Dxx fechada.
- [x] RULE-MECH-01: Classe por BASpec antes do corpo; zero H/P.
- [x] RULE-PD-01: não incide.
- [ ] Mapa do projeto (`build_map.py --check`): a cargo do Orquestrador (hooks regeneram; sem Bash aqui).

**Pronto para revisão.**
