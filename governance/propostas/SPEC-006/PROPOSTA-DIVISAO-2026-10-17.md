# PROPOSTA — Divisão da SPEC-006 (Cognitive Knowledge Graph) — para decisão de Andraus (Q-ABERTURA-5)

| Campo | Valor |
|---|---|
| Natureza | **[PROPOSTA] — não normativa, não é baseline, não homologa nada.** Documento de apoio à decisão de Andraus. |
| Autor | Especificador SOT (a pedido do Orquestrador) |
| Data | 2026-10-17 |
| Base lida | Cópia do `plan.md` v1.6 (1498 linhas), `checks.md`, `ABERTURA.md`, `research.md` (não aprofundado), pareceres das rodadas 5/6/7 (cópias no scratchpad, ramo `spec006-plan`); `ROADMAP.md`, `atomic-spec.md` §15, `AGENTS.md` §5, `governance/DHR-SPEC006-001_…md`, `governance/DHR-BACKLOG-001_…md`, `backlog/RMR-001_Painel_Backlog.md` |
| O que NÃO foi feito | Nenhum arquivo do repositório editado (ROADMAP, RMR-001, CATALOGO, Plan intocados). Nenhum Plan das Specs resultantes escrito. Nenhuma decisão aberta fechada (CONS-01: H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 seguem ABERTAS). Nenhum script executado (sem Bash). |
| Convenção | `plan.md:NNN` = linha da cópia v1.6 no scratchpad. [FATO] só com arquivo:linha; contagens por Grep = [INFERÊNCIA] (contagem manual sobre a saída da ferramenta; margem de poucas linhas). |

---

## 0. Fatos de partida

- [FATO] Andraus decidiu "**Uma Spec só** por enquanto; se o Plan ficar grande demais para revisar de uma vez, o Especificador volta a Andraus para propor divisão" — `governance/DHR-SPEC006-001_Ata_Homologacao_Abertura_SPEC-006.md:22`.
- [FATO] Rodada 7: **NÃO CONFORME — 0 Críticas · 4 Médias (R7-1..R7-4) · 10 Menores** — `parecer-revisor-rodada7.md:5`. "Nenhuma decisão de Andraus é necessária para sanar as quatro Médias" — `parecer-revisor-rodada7.md:18`. A divisão do Plan aparece como pendência "só de Andraus" — `parecer-revisor-rodada7.md:18`.
- [FATO] Mesmo sem as Médias, o teto seria **CONFORME condicional**: o ROADMAP diz "Resolve H-001" (`ROADMAP.md:177`), mas a abertura homologou que H-001 NÃO é fechada (`DHR-SPEC006-001…md:20`) — `parecer-revisor-rodada7.md:6`. **Esse teto não depende de dividir ou não.**
- [FATO] Diagnóstico do Revisor na rodada 6: "a mesma regra é copiada em RULE, BASpec, EARS, D4, D6, EC, schema e §7-bis — quase todos os achados da rodada 6 … são divergências entre essas cópias. Remédio de menor custo antes de qualquer divisão: reduzir cópias a referências a D4" — `parecer-revisor-rodada6.md:25`.
- [FATO] A v1.6 adotou a "convenção de fonte única" (`plan.md:26`) e caiu de 1641 para 1498 linhas (`checks.md:176`); ainda assim R7-1 e R7-2 são, de novo, divergências entre cópias (log com regra só em `plan.md:451`; obrigatoriedade no schema sem predicado em D4) — `parecer-revisor-rodada7.md:9-10`.
- [FATO] Na abertura, separar "ontologia/esquema" de "consulta/governança" foi avaliado e **rejeitado** por gerar dependência circular — `ABERTURA.md:70`.
- [FATO] O `checks.md` já esboçou um corte possível: (i) registro e integridade × (ii) fronteira de entrada, causalidade e consulta — "Não executado" — `checks.md:187`.
- [FATO] Re-apontamento de gatilhos: quando um slot alvo de gatilho `spec:` é dividido/fundido/renumerado/descartado, o Especificador propõe, Andraus homologa no mesmo ato, o Controlador registra aditivamente, o Revisor confere; gatilho sem re-apontamento = achado de gate — `backlog/RMR-001_Painel_Backlog.md:64`. `atomic-spec.md:443` exige também, se o slot for citado por Spec BASELINED, listar essas citações e propor erratum aditivo.
- [FATO] BL-003 e BL-011 estão `ATIVADO` com encaminhamento "ao gate da SPEC-006" — `RMR-001…md:102`, `:110`, `:191`; `governance/DHR-BACKLOG-001_…md:15`; COL-EXP-05 e R-04..R-06 "seguem sendo decididas no gate da SPEC-006" — `DHR-BACKLOG-001_…md:18`.

---

## 1. Diagnóstico — tamanho e acoplamento

### 1.1 Blocos (mapa seção/CKG → bloco)

| Bloco | Conteúdo | Onde está no `plan.md` v1.6 |
|---|---|---|
| **N — Núcleo do registro** (ontologia, entidade, relação, envelope, log, proveniência, versões, bitemporal, estado, guard INV-04, consulta/trace) | CKG-001, 002, 003, 004, 005, 006, 007, 011, 012; INV-CKG-01/02 | RULEs `:279-323`, `:350-360`; §D2.1 `:369-422`; EARS 1–7, 11, 12, 15–20 `:462-481`; BASpecs `:491-646`, `:729-766`; D4.1–D4.9, D4.12, D4.14, D4.16–D4.18 `:798-815`; D5 `:822-847`; D9 `:1107-1112`; contrato+schema `:1116-1218`; EC-002/004/006 `:1241-1281`, `:1298-1310` |
| **K1 — Causalidade/similaridade** | CKG-008 (Classe H, bounded loop) | RULE `:325-331`; EARS 8 `:469`; BASpec `:648-672`; D4.10–D4.11 `:807-808`; EC-005 `:1283-1296`; T07/T18; ADV-04/20/22 |
| **K2 — Colisão de relações** | CKG-013 | RULE `:362-366`; §D2.2 `:424-437`; EARS 13 `:474`; BASpec `:768-789`; D4.13 `:810`; T11/T21; ADV-02/18 |
| **F — Fronteira de entrada / governança de escrita** | CKG-009, CKG-010; caminhos (a)/(b)/(c), selo SPEC-007, allowlist | RULEs `:333-348`; §D2.3 `:439-456`; EARS 9/10/14 `:470-475`; BASpecs `:674-727` (inclui nota do critério mínimo de (a) `:721-727`); D4.15 `:812`; EC-001 (PRECOND) `:1224-1239`; EC-003 `:1256-1267`; T08/T09/T16/T20; ADV-07/08/21 |
| **T — Transversal (custo fixo por Spec)** | cabeçalho+histórico, nota de gate, CC, Herança/Delta, acepções, WF, PD, D0/D1, D6 (sequência atravessa todos os blocos), Plan, §7-bis, etiquetagem, autopré-check | `:1-271`, `:851-875`, `:1314-1498` |

[INFERÊNCIA] O bloco T ocupa aproximadamente as linhas 1–271 e 1314–1498 (~455 linhas, cerca de 30% do arquivo). Numa divisão com número novo, boa parte disso se repete em cada Spec.

### 1.2 Referências cruzadas entre blocos (contagem por Grep)

Método [INFERÊNCIA]: contei as linhas distintas do `plan.md` que citam identificadores de cada bloco e separei as que ficam dentro do próprio bloco das que ficam fora dele (outros blocos + transversal).
- K: `CKG-008|CKG-013|D4.10|D4.11|D4.13|§D2.2|collision|colis|colide`
- F: `CKG-009|CKG-010|D4.15|§D2.3|SEAL_|PATH_A_|ENTRY_PATH|WRITER_ALLOWLIST|allowlist|selo|caminho (a)|(a) pendente`

| Bloco | Linhas que o citam | Dentro do bloco | **Fora do bloco** |
|---|---|---|---|
| F (fronteira) | ~121 | ~54 | **~67** (ex.: `:7`, `:95`, `:100`, `:110`, `:422`, `:519-520`, `:559`, `:566`, `:835`, `:846`, `:854-862`, `:1134`, `:1143`, `:1157-1160`, `:1213`, `:1352`, `:1377`, `:1384-1390`, `:1400-1408`, `:1441-1450`, `:1496`) |
| K1+K2 (causal + colisão) | ~126 | ~56 | **~70** |
| log `kg_gate_decision` (N) | 32 linhas (`:37` … `:1435`) | — | presente em N, K, F e T |

**Pontos de contato estruturais** (fora do bloco T, isto é, em mecanismo e não em resumo) [INFERÊNCIA]:
- **K1 (causal)**: ~7 — linhas CAUSA/SIMILAR_A da matriz (`:401-402`), linha "juízo" da §D2.3 (`:447`), D6 passo 6 (`:867`), campos `causal`/`similarity_basis` (`:1138`, `:1190-1191`), campo `judgment_invocations` do log (`:1214`), PRECOND do EC-001 (`:1230`). **É separável.**
- **K2 (colisão)**: ~16 — RULE-003 (`:292`), linha INVALIDA da matriz (`:398`), §D2.3 (`:450`), **D4.2/D4.3/D4.4/D4.5** (`:799-802`), **D4.18 atomicidade** (`:815`), D6 passo 9 (`:870`), convenções D7 (`:882-883`), T17 (`:974-982`), ADV-19 (`:1089`), D9 (`:1109`), contrato (`:1125`, `:1139`), envelope `kg_record` (`:1151-1159`), payload (`:1203-1207`), POSTCOND do EC-001 (`:1231`). **A colisão é um `record_kind` do envelope e participa da unidade atômica: não se separa sem copiar as regras do envelope.**
- **F (fronteira)**: está espalhada. Toda BASpec de mutação depende de "ato autorizado CKG-009" (`:559`, `:566`, `:835`), e a ressalva "(a) pendente → INDETERMINADO" aparece em BASpecs, cenários, §7-bis e na Herança (`:95`, `:422`, `:519`, `:929-933`, `:960-968`, `:1000`, `:1377`, `:1394-1395`).

### 1.3 Achados dos pareceres por bloco (Críticas + Médias, rodadas 5–7)

| Rodada | N só | F só | K1 só | K2 só | Cruzados | T |
|---|---|---|---|---|---|---|
| r5 (`parecer-revisor-rodada5.md:11-24`) | C1, M8, M9, M10 | M1, M3 | M5, M6 | M4 | C2 (F×N), M2 (F×K), M7 (F×N) | — |
| r6 (`parecer-revisor-rodada6.md:9-19`) | N2, N3, N4, N6, N8, N9 | — | N7 | — | N5 (K2×N), N10 (F×N), N11 (K2×N) | N1 |
| r7 (`parecer-revisor-rodada7.md:9-12`) | R7-2 | R7-3 | — | — | R7-1 (N×F, e K2 via T21), R7-4 (F×N/Herança) | — |
| **Total (27)** | **11** | **3** | **3** | **1** | **8** (F em 6) | **1** |

Leitura [INFERÊNCIA]:
1. **Nenhuma Média aberta (R7-1..R7-4) está em K1 ou em K2 isolado.** Os achados de K1 (M5, M6, N7) foram fechados (`parecer-revisor-rodada6.md:6`; `parecer-revisor-rodada7.md:6`). Separar a causalidade **não elimina nenhum achado aberto**.
2. **O núcleo N concentra a maioria dos achados** (11 só nele, mais os cruzados). Esses achados ficam na SPEC-006 em **qualquer** divisão, então dividir não os resolve.
3. **F participa de 9 dos 27 achados**, quase todos pela mesma razão: contratos pendentes ([DECISÃO NECESSÁRIA]) que obrigam a escrever ressalvas condicionais em muitos lugares (R7-3: precedência `SEAL_MISSING`×`SEAL_CONTRACT_UNDEFINED`; R7-4: o critério mínimo de (a) [PROPOSTA] contra as obrigações herdadas do CEM; C2, M1, M3, M7, N10).

### 1.4 Cópias por regra (a causa real)

| Regra | Onde é reenunciada (amostra, `plan.md`) | Lugares ≈ |
|---|---|---|
| "(a) pendente ⇒ DENY / admissão positiva INDETERMINADO" | `:7`, `:36-37`, `:95`, `:100`, `:110`, `:341-347`, `:422`, `:443-444`, `:454`, `:471`, `:519`, `:700-727`, `:812`, `:861`, `:929-933`, `:960-968`, `:1000`, `:1094-1095`, `:1228`, `:1352`, `:1377`, `:1385`, `:1390`, `:1394-1395`, `:1442`, `:1496` | ~25 |
| Colisão (detecta, registra, atomicidade) | `:292`, `:362-366`, `:424-437`, `:450`, `:474`, `:768-789`, `:799-802`, `:810`, `:815`, `:869-870`, `:944`, `:1017-1023`, `:1037`, `:1085-1089`, `:1125`, `:1139`, `:1151-1159`, `:1203-1207`, `:1231`, `:1343`, `:1388` | ~20 |
| Obrigatoriedade de campos | o schema diz "obrigatório" (`:1158`, `:1162-1163`, `:1170-1173`, `:1190`, `:1200`), mas D4 só tem predicado de obrigatoriedade para elos de versão (`:813`) → **R7-2** | 2 fontes divergentes |
| Escritor/ordem do log | regra só na §D2.3 (`:451`) e em D4.5/D4.18 (`:802`, `:815`); ausente em RULE-009 (`:333-339`) e EARS 9 (`:470`) → **R7-1** | regra incompleta em várias cópias |
| Histórico de versões | as linhas do changelog (`:33-38`) reenunciam regras (ex.: `:37-38`), o que gera mais uma cópia a manter coerente (r7-d nasceu de citação removida só no changelog — `parecer-revisor-rodada7.md:15`) | 1 cópia extra por regra alterada |

**Conclusão do diagnóstico** [INFERÊNCIA]: o tamanho vem de **duas causas independentes**:
- **Cópias.** Ficam em qualquer divisão. Só o enxugamento resolve, com o D4 como único lugar de obrigatoriedade e de predicado.
- **A superfície de pendências da fronteira F.** É conteúdo que hoje só produz DENY e ressalvas condicionais. Pode ser retirada do texto, ou reduzida a uma regra fail-closed única, sem perder comportamento: o KG já não admite nenhuma escrita (`plan.md:454`).

Separar K1 diminui linhas, mas não diminui achados. Separar K2 aumenta as cópias.

---

## 2. Opções [PROPOSTA]

### Opção 1 — Manter uma Spec, com enxugamento estrutural ("fonte única dura", v1.7)

- **Fronteiras:** inalteradas (CKG-001..013 numa só Spec).
- **Mudanças de método** (o que se elimina são cópias, não comportamento):
  1. **D4 é o único lugar de "obrigatório":** um novo item D4 de presença de campos por `node_type` (resolve a classe R7-2). O schema passa a listar só campos e tipos, sem "obrigatório" e sem códigos.
  2. **RULE-CKG:** obrigação em 1–2 linhas mais um ponteiro para D4 ou §D2.3. As notas "Limite"/"v1.x — Nn" vão para o `checks.md`.
  3. **BASpec:** o ENTÃO diz só "aplica D4.x". O EC PRECOND passa a ser a lista de D4.x.
  4. **Histórico de versões** (`:28-38`): sai do `plan.md` para o `checks.md`/changelog. Fica no Plan só a linha da versão vigente.
  5. **Tabela de riscos** (`:1333-1355`) e **§7-bis Bloco A** (`:1374-1390`): viram ponteiros para a cobertura D8 (`:1100-1103`).
  6. **"Pendente ⇒ DENY"** é enunciado uma vez, na §D2.3; os demais lugares citam.
  7. **R7-1..R7-4 e r7-a..j** são sanados (o Revisor confirma que não exigem decisão de Andraus).
- **Herda / produz:** igual à v1.6.
- **Decisões abertas tocadas (nenhuma fechada):** H-001 (fronteira), G-001 (via BL-003), K-001 (ontologia em runtime; S14), J-001/N-001 (só "não tocadas"), M-001 (não tocada).
- **Dependências e ordem:** r8 → Revisor → Andraus → SPEC-007 segue a ordem do ROADMAP (`ROADMAP.md:172-182`).
- **Impacto em SPEC-007 e demais slots:** nenhum além do atual (o selo do caminho (b) continua dependência [DECISÃO NECESSÁRIA]).
- **Re-apontamento:** **nenhum** (slot não dividido). BL-003/BL-011 seguem com encaminhamento ao gate da SPEC-006 (`RMR-001…md:102`, `:110`). R-07/COL-EXP-05 continua [DECISÃO NECESSÁRIA].
- **Custo de revisão:** 1 rodada sobre um único documento, ainda grande. O Plan seria provavelmente ainda o maior do repositório (comparativo em `parecer-revisor-rodada6.md:25`) [INFERÊNCIA].
- **Prós:** cumpre a letra da Q-ABERTURA-5. Custo de governança zero. As 4 Médias são sanáveis sem decisão de Andraus.
- **Contras:** a superfície F pendente (~67 linhas fora do bloco) continua no texto. É a fonte provável dos próximos achados (F esteve em 9 dos 27) [INFERÊNCIA]. Cada decisão futura de Andraus sobre (a)/(b)/(c) reabre o Plan inteiro.

### Opção 2 — Uma Spec (mesmo número) em duas etapas: SPEC-006 v1.0 "núcleo fail-closed" agora + emendas aditivas de admissão por caminho depois (com o enxugamento da Opção 1)

- **Fronteiras:**
  - **v1.0 (agora):** N + K1 + K2 + CKG-009 (governança de escrita genérica: allowlist, identidade autenticada, regra de escrita do log) + **CKG-010 reduzido a uma regra:** "enquanto não houver contrato de admissão homologado para o caminho do objeto ⇒ DENY com motivo = caminho; nada persistido".
  - **Saem da v1.0:**
    - a [PROPOSTA] de critério mínimo de (a) (`plan.md:721-727`), fonte de R7-4/N10;
    - o código `SEAL_MISSING` e a precedência de (b) (fonte de R7-3), que vão para a emenda (b);
    - as cláusulas "CONDICIONAL pós-decisão" de T09/T16 (`:932-933`, `:967-968`).
  - **Emendas futuras v1.x** (aditivas, INV-07), cada uma quando a decisão existir: **(b)** selo, junto ou depois da SPEC-007; **(a)** critério/produtor/gatilho, por decisão de Andraus (e a reatribuição de S14 a SPEC-018/K-001); **(c)** registro por produtor (SAS-001 l.924); nós de referência; consumo de `Evidence.Invalidated`/emissão.
- **Herda / produz:**
  - A v1.0 herda os mesmos baselines da v1.6 (`plan.md:91-126`). Produz ontologia+matriz, envelope `kg_record`, log, predicados D4 e a **porta de admissão** como predicado único.
  - Cada emenda herda a v1.0 e produz o contrato de um caminho.
- **Decisões abertas tocadas (nenhuma fechada):**
  - v1.0: H-001, G-001 (BL-003), K-001 (ontologia em runtime).
  - Emendas: K-001 (promoção trabalho→permanente). Possível interface com M-001 (estados de objetos não-hipótese podem condicionar o critério de (a) para evidence/conviction) [INFERÊNCIA — a confirmar].
- **Dependências e ordem:** v1.0 → SPEC-007 (declara o selo como interface) → emenda (b). A emenda (a) é independente, por decisão de Andraus.
- **Impacto em SPEC-007:** a SPEC-007 passa a ter de expor o contrato do selo como interface consumida pela emenda (b). O conteúdo é o mesmo de hoje, explicitado.
- **Impacto nos demais slots:** SPEC-009 (G-001) e SPEC-018 (K-001) sem mudança.
- **Specs BASELINED:** **sem erratum.** As citações a SPEC-006 tratam de KG/memória permanente/ontologia/grafo/trace/H-001, e tudo isso fica na v1.0: `specs/features/SPEC-002/plan.md:135`, `:159`, `:169`, `:692`, `:948`; `SPEC-003/plan.md:223`; `SPEC-004/plan.md:158`, `:191`, `:198`; `SPEC-005/plan.md:224`, `:261`, `:971` [INFERÊNCIA a partir dessas linhas].
- **Re-apontamento exigido:** nenhum gatilho `spec:` muda de alvo (número preservado). Proponho uma **nota aditiva** no RMR-001, a ser registrada pelo Controlador após a decisão:
  - **BL-003:** parte lógica (envelope/versão) tratada na v1.0; admissão de hipótese/estado na emenda (a); parte física = H-001/G-001.
  - **BL-011:** X-01, R-01..R-06 e X-04 tratados na v1.0 (`plan.md:52-58`); R-07/COL-EXP-05 e fila EXP-SPEC = [DECISÃO NECESSÁRIA] (v1.0, emenda, SPEC-009 ou SPEC-007).
  - **DHR-BACKLOG-001:** "gate da SPEC-006" (`:15`, `:18`) lido como o gate da v1.0. A ata não é editada (INV-07); a leitura fica na nota nova.
  - Se Andraus entender que a entrega em etapas é uma "divisão" no sentido de `RMR-001…md:64`, o mesmo conteúdo vira **re-apontamento formal**, homologado no ato.
- **Custo de revisão:** r8 sobre um documento menor. Depois, revisões curtas por emenda. Precedentes de emenda aditiva sobre Spec homologada: SPEC-046 v1.1 (`ROADMAP.md:480`); SPEC-020 "núcleo A" com dimensões B fechadas depois (`ROADMAP.md:28`, `:291`).
- **Prós:**
  - Retira do texto a maior fonte de ressalvas condicionais sem número novo, Dossiê novo ou erratum.
  - R7-3 e R7-4 deixam de existir porque a [PROPOSTA] que os gerava é removida, e não por remendo.
  - Colisão e causalidade, que estão estáveis, ficam onde estão.
  - A ontologia continua dentro da SPEC-006 (Q-ABERTURA-4).
  - Os pontos D8 da Q-ABERTURA-2 (colisão, causalidade pós-hoc, INV-04, INV-07) continuam na v1.0.
- **Contras:**
  - A v1.0 não admite nada. É igual a hoje (`plan.md:454`), mas agora declarado como desenho.
  - As capacidades S10/S14 (`plan.md:249`, `:253`) ficam parcialmente entregues e isso tem de ser declarado na cobertura (`ROADMAP.md:499`).
  - A obrigação herdada "preservar todos os estados/versões" da Evidência (CEM-001 l.494/612) segue PARCIAL até a emenda (a), como já está hoje (`plan.md:1394-1395`).
  - Andraus precisa aceitar que "uma Spec só" se cumpre por número, não por entrega única.

### Opção 3 — Duas Specs numeradas: SPEC-006 (núcleo, como a v1.0 da Opção 2) + nova Spec "Admissão ao Knowledge Graph" (ou parte (b) fundida na abertura da SPEC-007)

- **Fronteiras:**
  - SPEC-006 = N + K1 + K2 + CKG-009 genérico + porta de admissão fail-closed.
  - **SPEC-0NN** (número e nome de Andraus): caminhos (a)/(b)/(c), critério de promoção, consumo do selo, contrato de registro por produtor, nós de referência, consumo/emissão de eventos, reconciliação de transição perdida (`plan.md:813`), extensão "todos os estados" a hipótese/convicção (N10).
  - Número aparente: SPEC-047 está reservada (`ROADMAP.md:538`), então o próximo livre parece ser SPEC-048 [INFERÊNCIA]. Numeração fora de faixa tem precedente (`ROADMAP.md:476-478`, SPEC-046).
- **Herda / produz:** SPEC-0NN herda SPEC-006 (envelope, gates, EC-001), SPEC-007 (selo), SPEC-004 (origem do caminho (a)), CHM/CEM/CCM, SAS-001 l.924, SPEC-005 (`Evidence.Invalidated`). Produz os contratos de admissão.
- **Decisões abertas tocadas:** como na Opção 2, divididas entre as duas Specs. Nenhuma fechada.
- **Dependências e ordem:** SPEC-006 → SPEC-007 → SPEC-0NN, que precisa do selo e da decisão sobre (a). A alternativa é abrir uma SPEC-0NN parcial, só (a)/(c), antes da SPEC-007.
- **Impacto em SPEC-007 e slots:**
  - Se (b) for fundido na SPEC-007, o slot SPEC-007 cresce (já é CRITICAL D0–D8 — `ROADMAP.md:180`).
  - Se não, nova linha em §26 (`ROADMAP.md:497-509`) e no CATALOGO.
  - Specs BASELINED: sem erratum, pelos mesmos motivos da Opção 2, **desde que a consulta/trace (CKG-011) fique na SPEC-006**. SPEC-002 delega o trace "ao KG (SPEC-006)" (`SPEC-002/plan.md:159`, `:692`).
- **Re-apontamento exigido (formal, `RMR-001…md:64`):**
  - **BL-003** (`spec:SPEC-006 em redação` ∨ `spec:SPEC-009 em redação`): parte lógica permanece na SPEC-006; admissão de hipótese/estado → SPEC-0NN; manter `spec:SPEC-009`.
  - **BL-011:** X-01, R-01..R-06 e X-04 permanecem na SPEC-006; R-07/COL-EXP-05 + fila EXP-SPEC → [DECISÃO NECESSÁRIA] (SPEC-006, SPEC-0NN, SPEC-009 ou SPEC-007).
  - **DHR-BACKLOG-001:** ata nova ou nota que leia "gate da SPEC-006" (`:15`, `:18`) segundo a divisão (INV-07: a ata não é editada).
  - **BL-010:** se SPEC-0NN for criada, acrescentá-la de forma aditiva à "Ação ao ativar", que hoje cita 006/007/024 (`RMR-001…md:109`).
  - O conjunto é proposto no Dossiê da SPEC-0NN e homologado no mesmo ato.
- **Exigências de abertura:** **Dossiê de Pesquisa** (RULE-ECC-02). Reaproveitar `research.md`, válido até 2027-01-03 (`DHR-SPEC006-001…md:25`), ou fazer Dossiê novo = decisão de Andraus.
- **Custo de revisão:** o maior das três opções. Inclui abertura, parecer sobre o Dossiê, homologação, Plan completo da SPEC-0NN e o bloco T duplicado (CC, Herança, §7-bis, etiquetagem, autopré-check).
- **Prós:** fronteiras numéricas nítidas. A SPEC-0NN pode ser aberta só quando as decisões existirem.
- **Contras:**
  - O EC-001 da SPEC-006 passa a ter precondição definida em outra Spec, ainda não homologada (autopré-check: "dependências a montante já homologadas").
  - Há risco de copiar regras do envelope entre Specs, o oposto do objetivo.
  - Contraria formalmente a Q-ABERTURA-5.
  - É a variante com mais atos de Andraus.

#### Variante 3b — três Specs (núcleo / causalidade+colisão / fronteira) — avaliada e **não recomendada**
- A **colisão** tem ~16 pontos de contato estrutural no envelope e na atomicidade (§1.2). Separá-la obriga a copiar D4.2–D4.5/D4.18 ou cria dependência circular, e isso agrava a causa dos achados.
- A **causalidade** é separável (~7 contatos), mas não tem nenhum achado aberto (§1.3). Separá-la só multiplica o custo fixo e tira da SPEC-006 um ponto D8 que Andraus nomeou (`DHR-SPEC006-001…md:19`).
- O corte esboçado no `checks.md:187` põe a consulta/trace numa segunda Spec. Com número novo, isso exigiria erratum na SPEC-002 (`plan.md:159`, `:692` da SPEC-002) e mistura causalidade com fronteira.

### Quadro comparativo [INFERÊNCIA]

| Critério | Opção 1 | Opção 2 | Opção 3 |
|---|---|---|---|
| Remove cópias (causa dos achados) | sim | sim | sim no núcleo; risco de cópia entre Specs |
| Remove a superfície F pendente | não | sim (para emendas) | sim (para outra Spec) |
| Novo número / Dossiê / §26 | não | não | sim |
| Re-apontamento formal RMR-001 | não | nota aditiva (formal se Andraus assim entender) | sim (BL-003, BL-011, nota DHR-BACKLOG-001, BL-010) |
| Erratum em Spec BASELINED | não | não | não (se o trace ficar no núcleo) |
| Rodadas até homologar o núcleo | 1+ (documento grande) | 1+ (documento menor) | 1+ no núcleo, mais um ciclo completo da SPEC-0NN |
| Fidelidade à Q-ABERTURA-5 | literal | por número | contraria |
| Teto do parecer | CONFORME condicional (H-001 × `ROADMAP.md:177`) em todas | idem | idem |

---

## 3. Recomendação [PROPOSTA]

**Opção 2, executada junto com o enxugamento "fonte única dura" da Opção 1.** Fundamentos:
1. **A causa é a cópia, não a amplitude.** O próprio Revisor diz isso (`parecer-revisor-rodada6.md:25`), e R7-1/R7-2 o confirmam (`parecer-revisor-rodada7.md:9-10`). Por isso o enxugamento é obrigatório em qualquer opção, e dividir sem ele não resolve.
2. **O único bloco cuja retirada reduz achados é a fronteira pendente F.** Ela está em 9 dos 27 achados e em ~67 linhas fora do próprio bloco. Hoje ela só produz DENY (`plan.md:454`), então pode virar uma regra fail-closed única na v1.0 sem perder comportamento. Os contratos de cada caminho entram como emendas quando as decisões [DECISÃO NECESSÁRIA] existirem.
3. **Separar K não compensa.** K1 não tem achado aberto, e K2 está acoplado ao envelope.
4. **Manter o número preserva** as citações das Specs BASELINED, os gatilhos `spec:SPEC-006`, o Dossiê homologado e a decisão Q-ABERTURA-4. E segue precedentes de emenda aditiva (SPEC-046 v1.1, SPEC-020 núcleo A).
5. **Se Andraus preferir zero mudança de governança,** a Opção 1 é viável: as 4 Médias são sanáveis sem decisão dele (`parecer-revisor-rodada7.md:18`). O custo é manter a superfície F e o risco de novas rodadas por ela.

Em **qualquer** opção, o teto do parecer só sobe de CONFORME condicional se Andraus resolver a divergência entre `ROADMAP.md:177` ("Resolve H-001") e `DHR-SPEC006-001…md:20` (H-001 não fechada).

---

## 4. O que depende só de Andraus

1. **Escolher a opção** (reabre a Q-ABERTURA-5 — `DHR-SPEC006-001…md:22`).
2. Na Opção 2: aceitar a entrega em etapas como "uma Spec só" e decidir se ela conta como "divisão" para o RMR-001 §3 (`RMR-001…md:64`), ou seja, nota aditiva ou re-apontamento formal.
3. Na Opção 3: número e nome da nova Spec; reaproveitar o `research.md` (válido até 2027-01-03) ou exigir Dossiê novo; levar (b) para a abertura da SPEC-007 ou não.
4. A divergência entre `ROADMAP.md:177` e Q-ABERTURA-3 (H-001), que limita o parecer a CONFORME condicional.
5. **H-001** e todas as demais decisões abertas (CONS-01). Nenhuma é fechada por esta proposta.
6. Critério, produtor e gatilho do caminho (a), e a reatribuição de S14 (promoção trabalho→permanente) a SPEC-018/K-001 (`plan.md:253`).
7. Contrato do selo (b) com a SPEC-007; contrato (c); caminho dos nós de referência; mantenedor da allowlist; host do juízo; mapeamento `producer_id`→`school` para SMC/Fibonacci/ICT/Fractal (`plan.md:1441-1450`).
8. Onde reconciliar R-07/COL-EXP-05 e a fila EXP-SPEC-001..053 (`plan.md:59`; `DHR-BACKLOG-001…md:18`).
9. Estado do BL-003 após a homologação (`plan.md:47`, `:1448`).
10. Onde vive a extensão "todos os estados/versões" a hipótese/convicção (N10), hoje em conflito com o critério de (a) (`plan.md:1443`).
11. A ordem de registro, feito pelo Controlador **depois** da decisão: `ROADMAP.md` §6/§26, `governance/CATALOGO-OFICIAL.md`, notas no RMR-001, ata DHR.

---

## 5. Limites desta proposta
- As contagens de §1.2–§1.4 são manuais, feitas sobre a saída do Grep (margem de poucas linhas), e não medem bytes nem esforço de revisão. Os percentuais e faixas são [INFERÊNCIA], não medição.
- O `research.md` não foi relido em profundidade: a proposta não depende do conteúdo do Dossiê, só de sua validade (`DHR-SPEC006-001…md:25`).
- A interface com M-001 na Opção 2 é [INFERÊNCIA] a confirmar.
- Nada aqui é CONFORME nem homologação. O VERIFY interno não foi apresentado como parecer.
