# checks.md — Verificação de Spec da SPEC-049 (fase spec-first)

**Objeto:** `specs/features/SPEC-049/plan.md` **v1.0 (CANDIDATA — primeira entrega do Plan; aguarda Revisor rodada 1, integral, e homologação de Andraus)** (WikiRAG Reading View).
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — **NÃO** é teste de runtime, **NÃO** é parecer do Revisor, **NÃO** é homologação. "VERIFY" interno = feedback. [FONTE: atomic-spec §14]
**Método:** atomic-spec.md v1.5 · tlc-spec-lean (PLAN = Spec; CHECKS = verificação de spec) · overlay GUS-TLC-001
**Data:** 2026-10-31
**Ordem de Andraus:** chat 2026-10-31, "Iniciar o Plan da SPEC-049" (transmitida pelo Orquestrador). Abertura: DHR-SPEC049-001 (HIGH D0–D7, uma Spec, Classe D com a trava E3 herdada).
**Contagens declaradas (por linha em coluna 0 — contadas por Grep no arquivo após a redação; a reconferir no ambiente pai):** **1** INV-WRV (`^INV-WRV-01:` — l.315), **10** RULE-WRV (`^RULE-WRV-0nn:` — 001..010), **11** EARS (`^N. (WRV-` 1–10 + `^11. (INV-WRV`), **11** BASpec (`^### BASpec-WRV-` — 001..011), **3** EC (`^### EC-WRV-` — 001..003), **18 cenários** (`^### Cenário-WRV-T` — T01..T18). Estados locais de D5: `W_RECEBIDA`, `W_LENDO`, `W_COMPILANDO`, `W_VALIDANDO`, `W_EMITIDA`, `W_RECUSADA`, `W_NAO_ENTREGUE`.
**Medida do corpo (RULE-ECC-07):** **1.424 linhas** (arquivo inteiro; nenhuma seção `## Anexo`) — abaixo de 1.600/1.900/2.000; régua de `scripts/check_dimensionamento.py` (linhas antes do 1º `## Anexo`).

---

## 0. Tabela fato → locais (ordem de serviço, condição 6)

> **Feita ANTES da redação:** a coluna "Fonte (Grep)" foi conferida por Grep/Read nas Specs baselined nesta sessão; a coluna "Locais no Plan" lista onde o fato **seria** repetido. **Conferida DEPOIS da redação** por Grep no `plan.md` (coluna "Conferência pós-redação", números de linha do Plan v1.0). Regra: o mesmo fato com o mesmo conteúdo em todos os locais; divergência = defeito a corrigir antes da entrega.

| Fato | Fonte (Grep) | Locais no Plan | Conferência pós-redação (Grep no plan.md) |
|---|---|---|---|
| **F1** Entrada com **quatro** campos: `cutoff`, `input_set` (itens/marcas até o corte), `rule_version`, `valid_at` — sem relógio | ABERTURA S1 (l.38), §15 cond. 2 (l.272); ata §1 C-4 (l.29) | RULE-WRV-001 (a); RULE-WRV-007 (a)(d); EARS 1 e 7; BASpec-WRV-001; D4.1; contrato `compilation_input`; T02/T03; EC-WRV-001/002; acepção Termos 4–6 | "quatro campos/QUATRO campos": l.58, 223, 264, 337 (×2), 471, 480, 552, 593, 901, 953, 1145, 1155, 1176 — mesmos quatro nomes em todos ✔ |
| **F2** `valid_at` ausente ⇒ MESMO instante do corte, preenchido antes de compilar; origem (`valid_at_basis` DECLARADO / DERIVADO_DO_CORTE) **só no registro**; nunca o relógio | ata §1 C-4; ABERTURA S1 (iv) | RULE-WRV-001 (b); EARS 1; BASpec-WRV-001; D4.1 (3); contrato `compilation_record`; T02 | l.352-353 (regra), 552 (EARS), 610 (BASpec), 830 (D4.1), 917 (contrato), 954 (T02); "valid_at_basis ∉ página" em T02 ✔ |
| **F3** Recusa por omissão de lado: lado sem entrada ⇒ **página inteira** não emitida, código **`WRV_CONTRADICTION_SIDE_OMITTED` (dono SPEC-049)**; lado fora da entrada/fonte/uso indeterminado/cadeia irresolúvel ⇒ "lado não exibível" + `WRV_CONTRADICTION_INCOMPLETE` | ABERTURA S5 (l.43), §15 cond. 12/14; SPEC-007 l.1678 (EC-KFH-010) e l.873 (código da 007 — não reutilizado) | RULE-WRV-005 (b)(d); EARS 5; BASpec-WRV-005; §D3.1; D4.4; D5; T10/T11; EC-WRV-001; tabela de condições | `WRV_CONTRADICTION_SIDE_OMITTED`: l.59, 110, 436, 556, 579, 680, 836, 853, 1035, 1164 — sempre "página inteira"/"não emite" ✔; `CONTRADICTION_SILENT_RESOLUTION_FORBIDDEN` só como referência (motivo de não reutilizar; §D3.1 "NÃO é emitido"; T10 `code ≠`) ✔ |
| **F4** `input_hash` na página; `output_hash` **só no registro** | ABERTURA S7 (l.46); research §3.1 | RULE-WRV-007 (c); EARS 7; BASpec-WRV-007; D4.6; contrato `reading_view` ("SEM output_hash") e `compilation_record`; T13; EC-WRV-001/002 | l.478 (regra), 558 (EARS), 719 (BASpec), 1065 (T13), 1159 (EC-001); contrato "SEM output_hash" ✔ |
| **F5** Códigos — definição única em §D3.1, com dono | ABERTURA §15 cond. 14; SPEC-048 l.124 (dois códigos do insumo → 049) | §D3.1 (tabela com coluna "Dono"); regras e cenários só referenciam | todos os códigos usados em D2/EARS/BASpec/D4/D5/D7/EC constam da §D3.1 ✔ (conferência por leitura da §D3.1 contra Grep de `WRV_` e `WIKI_`) |
| **F6** Tamanhos: teto 2.000 / alerta 1.900 / confirmação 1.600; estimativa ≈1.570; medida 1.424 | RULES.md l.518-536; ABERTURA §3 | seção "Dimensionamento"; Incorporação P-7; tabela de condições (ata §3); este checks | l.40-47, 76, 112 — valores iguais em todos ✔ |
| **F7** `reading_view_ref` := {`ref_type` = "READING_VIEW", `input_hash`}, dono SPEC-049, disjunto de `published_item_ref@version` e `source_id@source_hash` | ata §1 C-2; SPEC-048 l.1103/1151/1267/1439 | RULE-WRV-008 (a); BASpec-WRV-008; D4.6; contrato `reading_view`; T01/T15; Contrato com a SPEC-048 | "READING_VIEW": l.500, 739, 840, 906, 943, 1089 — mesma forma ✔ |
| **F8** Sem trecho da fonte (P-3, opção A): da fonte só o endereço (`source_id@source_hash`, `locator`) | ata §1 P-3 | RULE-WRV-004; RULE-WRV-005 (b) `LADO_E_FONTE`; Contrato SPEC-007 ponto 2; T08/T11 | por leitura: as quatro âncoras dizem "só o endereço" ✔ |
| **F9** Níveis: emissão E1, registro E1, trava E3 (Classe C) | ABERTURA §4 | cabeçalho; CC-11; BASpec-WRV-008..011 [E1/E3]; EC-WRV-001..003; Escala E0–E3 | por leitura ✔ (nenhum local diz outro nível) |
| **F10** Janela de validade derivada: `valid_from` do registro de criação (SPEC-006 l.1419); `valid_to` da invalidação (l.1404/1420; RULE-CKG-012 l.556-558); null ≡ +∞ (RULE-CKG-004 l.400); janela [valid_from, valid_to) (l.677); sem `valid_from` ⇒ "validade não informada" | SPEC-006 l.395-401, 556-558, 677, 1392, 1400-1421; SPEC-007 RULE-KFH-009 l.683-704 | RULE-WRV-006 (b)(c); D4.2; BASpec-WRV-006; T12; Herança/Delta; tabela de condições (13) | por leitura ✔ (mesmas âncoras em RULE-WRV-006 e Herança) |

---

## 1. Condições obrigatórias do Plan (ABERTURA §15; DHR-SPEC049-001 §3)

| # | Condição | Âncora no Plan v1.0 | Estado |
|---|---|---|---|
| 1 | Insumo C-1 reescrito com IDs `WRV`; nenhum `*-KFH-*` reutilizado | "Mapeamento do insumo" (11 linhas, item a item) | ✔ — IDs KFH aparecem só como origem/fonte |
| 2 | Quatro campos + derivação de `valid_at` + sem relógio na página e na validade + cenário "mesmo corte, `valid_at` diferente" | RULE-WRV-001 (a)(b); 006 (e); 007 (b); T02; **T03** | ✔ |
| 3 | CC-08 + §7-bis Bloco B: trava e pontos 1, 2, 5 um a um, com evidência | Herança/Delta; "Contrato com a SPEC-007"; §7-bis Bloco B | ✔ — herança declarada `[INFERÊNCIA]` (C-3) |
| 4 | "Texto de modelo" (C-1) e "emitir" ≠ "publicar" | Acepção, Termos 2 e 3 | ✔ |
| 5 | Ordem neutra e fixa dos lados (D) + negativo de omissão | RULE-WRV-005 (c)(d); T09, T10 | ✔ — ordem por hash da referência |
| 6 | `reading_view_ref` conferido contra SPEC-048 l.1103/1267/1439 | "Contrato com a SPEC-048" (citação das quatro linhas, inclusive l.1151) | ✔ — conferido por Grep em 2026-10-31 |
| 7 | Sem consumo por agentes, sem resumo por modelo, sem envio para fora | D1 Non-goals; RULE-WRV-003, 008 (c), 009 (d); INV-WRV-01 | ✔ |
| 8 | Corpo medido e declarado | seção "Dimensionamento" (1.424) | ✔ (a reconferir pelo Orquestrador com `check_dimensionamento.py`) |
| 9 | ENF-07 na unidade E3 | EC-WRV-003; BASpec-WRV-011; T16 (d) | ✔ (taxa INDETERMINADA — gap aberto) |
| 10 | CC-11 Classe C/E3 justificada pela ameaça e pelo slot | BASpec-WRV-011 CRITÉRIO 4Es; CC-11 | ✔ |
| 11 | Limitação R-9 declarada | RULE-WRV-008 (c); riscos R-9; RU-2 | ✔ |
| 12 | Unidade bloqueada = página inteira; código; "lado não exibível"; negativos de ambos | RULE-WRV-005 (b)(d); T10, T11 | ✔ |
| 13 | Janela de validade derivada, com âncora, sem campo novo | RULE-WRV-006 (b); D4.2; T12 | ✔ — fonte escolhida: registro de criação + registro de invalidação (SPEC-006), base normativa RULE-CKG-012 + l.1392 + RULE-KFH-009 |
| 14 | Código da recusa: reutilizar ou próprio; de quem é | RULE-WRV-005 (d); §D3.1 | ✔ — **próprio**, `WRV_CONTRADICTION_SIDE_OMITTED`, dono SPEC-049 |
| R3-m01 | `research.md` l.10 alinhada a "HIGH decidido, validade 2027-01-29", antigo em `[antes:]` | `research.md` l.10 | ✔ (único edit fora de plan/checks) |
| Ata §3 | Teto 2.000 / alerta 1.900 | "Dimensionamento" | ✔ |

## 2. Mapeamento do insumo

| Verificação | Estado |
|---|---|
| Toda parte do insumo destinada à SPEC-049 pelo mapeamento da SPEC-048 (l.101, 117, 119, 123-125, 129-131, 135) tem destino aqui | ✔ — RULE-KFH-015, cláusula de RULE-KFH-016, EARS 15, dois códigos, BASpec-KFH-015, T21, partes de ADV-KFH-11/25, EC-KFH-009, cláusula de INV-KFH-02, R-8 "2ª verdade" |
| Nenhum ID `*-KFH-*` reutilizado como ID vigente | ✔ |
| Mudanças declaradas (não silenciosas) | ✔ coluna "Mudança declarada" |

## 3. Constitution Check e herança

| Item | Verificação | Estado |
|---|---|---|
| CC-01..CC-12 presentes | lista no Plan, cada um com nota | ✔ (N/A justificados: CC-06, CC-07, CC-12) |
| CC-03 / J-001 | Conviction Vector declarado pendente (J-001 ABERTA); nenhum limiar | ✔ |
| CC-08 INHERITS por ID+versão | SPEC-007 v2.3, SPEC-006 v1.7+v1.11/v1.12/v1.13, SPEC-048 v1.4, SPEC-004 v1.2, SPEC-005 v1.0, CEM/CHM/CCM v1.0, RULES por linha | ✔ |
| REMOVED / MODIFIED | ambos vazios — nada suprimido | ✔ |
| RULE-HV | não se aplica (horizontal) — declarado | ✔ |
| CC-11 por BASpec | 10 D + 1 C; zero H/P (sem bounded loop a declarar); C com GATE DE SAÍDA | ✔ |

## 4. BASpecs — campos e Classe (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REFERÊNCIA | CLASSE (4Es) | VERIFICADO POR (positivo / negativo) |
|---|---|---|---|---|---|---|
| WRV-001 | ✔ | ✔ | ✔ | RULE-WRV-001 | D (Eficácia) | T02, T03 / T04, T05 |
| WRV-002 | ✔ | ✔ | ✔ | RULE-WRV-002 | D (Eficácia, Eficiência) | T06 / T14 (b) |
| WRV-003 | ✔ | ✔ | ✔ | RULE-WRV-003 | D (Eficácia) | T06 / T07 |
| WRV-004 | ✔ | ✔ | ✔ | RULE-WRV-004 | D (Eficácia) | T08 (P1) / T08 (P7) |
| WRV-005 | ✔ | ✔ | ✔ | RULE-WRV-005 | D (Eficácia) | T09, T11 / T10 |
| WRV-006 | ✔ | ✔ | ✔ | RULE-WRV-006 | D (Eficácia) | T12 (R1) / T12 (R3, P6) |
| WRV-007 | ✔ | ✔ | ✔ | RULE-WRV-007 | D (Eficácia, Eficiência) | T13 / T14 (a)(c)(d) |
| WRV-008 | ✔ | ✔ | ✔ | RULE-WRV-008 | D (Eficácia) | T15 (forma) / T15 (submissão) |
| WRV-009 | ✔ | ✔ | ✔ | RULE-WRV-009 | D (Eficácia) | T17 (a) / T17 (a')(b)(c) |
| WRV-010 | ✔ | ✔ | ✔ | RULE-WRV-010 | D (Eficácia) | T01 / contraste T04 |
| WRV-011 | ✔ | ✔ | ✔ | INV-WRV-01 | **C** (Eficácia sobre Economicidade; justificativa da condição 10) + GATE DE SAÍDA | T16 (a) / T16 (b)(c), T18; falso-DENY T16 (d) |

## 5. Rastreio RULE ↔ EARS ↔ BASpec ↔ cenário ↔ EC

| Regra | EARS | BASpec | Cenários | EC |
|---|---|---|---|---|
| INV-WRV-01 | 11 | 011 | T16, T18 | EC-WRV-003 |
| RULE-WRV-001 | 1 | 001 | T02, T03, T04, T05 | EC-WRV-001 |
| RULE-WRV-002 | 2 | 002 | T06, T14 (b) | EC-WRV-001 |
| RULE-WRV-003 | 3 | 003 | T06, T07 | EC-WRV-001 |
| RULE-WRV-004 | 4 | 004 | T08 | EC-WRV-001 |
| RULE-WRV-005 | 5 | 005 | T09, T10, T11 | EC-WRV-001 |
| RULE-WRV-006 | 6 | 006 | T03, T12 | EC-WRV-001 |
| RULE-WRV-007 | 7 | 007 | T02, T13, T14 | EC-WRV-001, EC-WRV-002 |
| RULE-WRV-008 | 8 | 008 | T15 | EC-WRV-001, EC-WRV-003 |
| RULE-WRV-009 | 9 | 009 | T17, T18 | EC-WRV-001 |
| RULE-WRV-010 | 10 | 010 | T01 | EC-WRV-001 |

Nenhuma regra sem EARS/BASpec/cenário; nenhum cenário órfão (T01..T18 todos citados por alguma BASpec).

## 6. Enforcement Contracts — mínimos por nível (atomic-spec §10.3)

| EC | Nível | Campos | Mínimo do nível | Estado |
|---|---|---|---|---|
| EC-WRV-001 emissão | E1 | os 8 | E1: + EVIDENCE | ✔ (acima do mínimo: PRECOND/POSTCOND/FAILURE-MODE presentes) |
| EC-WRV-002 registro | E1 | os 8 | E1: + EVIDENCE | ✔ |
| EC-WRV-003 trava | E3 | os 8 | E3: + POLICY + falso-DENY amostral | ✔ (ENF-07; taxa INDETERMINADA; fail-closed — ENF-04) |
| Escala E0–E3 em seção própria | — | — | ENF-08 | ✔ |

## 7. CONS-01 e decisões

| Verificação | Estado |
|---|---|
| J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção — todas marcadas ABERTAS/pendentes onde aparecem | ✔ (por leitura; STRUCT-10 a confirmar no gate) |
| H-001 citada como FECHADA (ROADMAP "Decisões FECHADAS") | ✔ |
| Perguntas novas (P-1 guarda de exibição; P-2 ativo via `ESTATISTICA_DE`) com lado seguro já vigente; nenhuma bloqueante | ✔ |
| Nenhum `[DECISÃO NECESSÁRIA]` que exija parar | ✔ — nada da redação dependeu de decisão ausente da ata |

## 8. Previsão do gate determinístico (`validate_spec_sot.py`) — NÃO executado (sem Bash)

| Check | Onde o Plan atende |
|---|---|
| STRUCT-01 cabeçalho | linhas "Complexidade" / "Profundidade-alvo" da tabela e linha "Complexidade: HIGH. Profundidade-alvo: D0–D7" |
| STRUCT-02 Constitution Check | seção CC; "Elliott"; "Conviction Vector (J-001 ABERTA, pendente)" |
| STRUCT-03 etiquetas | [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] |
| STRUCT-04 EARS | 11 itens "Quando …, a compilação DEVE …" |
| STRUCT-05 BASpec | QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR em todas |
| STRUCT-06 EC | os 8 campos em EC-WRV-001..003 |
| STRUCT-07 | nenhum limiar de convicção |
| STRUCT-08 | "FATO NORMATIVO" / "documentado ≠ homologado" |
| STRUCT-09 | HIGH com D0–D7 (teto D7) |
| STRUCT-10 | IDs de decisão aberta sempre com marca de pendência próxima; H-001 fechada no ROADMAP |
| STRUCT-11/12 | cita RULE-ECC-01/02; `research.md` com "Dossiê de Pesquisa"; `sources/REPO-*.txt` (régua da abertura) |
| STRUCT-13 | 0 itens vinculados por regra (ata §2); disposições voluntárias declaradas no formato `Disposição:` |

## 9. Não verificado aqui (fica com o Orquestrador / Revisor)

- Execução dos gates: `validate_spec_sot.py`, `revisor_gate.py`, `check_invariants.py`, `check_refs.py`, `check_doc_sync.py`, `check_dimensionamento.py`, `check_repo_research.py --all`, `backlog_triggers.py --abertura SPEC-049`, `build_map.py --check`, suíte de testes.
- Veracidade das fontes web (`sources/`) — risco residual já declarado na abertura (ata §4).
- Números de linha citados das Specs baselined foram conferidos nesta sessão (Autopré-check do Plan, item "Integridade"); deriva futura de linha é achado C07, não mudança de mérito.
