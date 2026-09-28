# EUA-E19a — Restauração Semântica do "Signal Package" (fronteira) + TMP interno (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E19a** (emenda constitucional/semântica — fatia 1 de 2; a fatia 2 é a EUA-E20 futura) |
| Natureza | (1) Emenda à CONSTITUTION P14 + convergência horizontal MAN-001 dos 6 loci do invariante "SOT não executa; artefato de fronteira"; (2) Reconciliação semântica TMP↔Signal Package (RULE-SEM/MSC-001); (3) Consolidação de R:R ≥ 1:3 + instituição de Portfolio Heat ≤ 15% e alavancagem dinâmica como invariantes de risco |
| Status epistemológico | **HOMOLOGADA — BASELINE** (Andraus, 2026-09-22, **DHR-EUA-E19a**; parecer Revisor CONFORME). Deltas aplicados aos 6 loci pelo Controlador. Achados Menores m-002/m-003 e Médio M-001 tratados como delta editorial nesta versão. TRACE-06. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-22 |
| Alvo | `governance/CONSTITUTION.md` P14 + diagrama de pipeline · `atomic-spec.md` INV-05 §13 · `GLOSSARIO.md` l.52 · `rag/synthesis.knowledge.md` CHUNK-SY-007 · `AGENTS.md` não-negociável #9 · `ROADMAP.md` SPEC-016 · `governance/RULES.md` (nova sub-entrada RULE-SEM aplicada + invariantes de risco); `governance/GLOSSARIO.md` (Terminologia Concorrente) |
| Fundamento no baseline | ENGENHARIA-GERAL Doc03 §20 l.604–606 (termo fundacional "Signal Package"); INV-05/INV-07/INV-09; PC-08 (só Andraus homologa); MAN-001 (convergência horizontal); RULE-SEM-01/04 + CC-10 (EUA-E06); RULE-HD-01..04 + CC-08 (EUA-E04); D-RISK-01/02/03/05 e INV-RISK-00 (`reference/SOT-RISK-MASTER-001_Consolidado.md`, decisões de Andraus 2026-09-22) |
| Precedência | Não cria a FASE RISK (isso é a EUA-E20 futura). Não especifica nenhuma RISK-SPEC (BL-018, diferido). Não menciona o Risk Harness (C-03). Não fecha nenhuma decisão aberta (§9). Não cria autoridade nova. |

> **TRACE-06.** Todo conteúdo é `[PROPOSTA]` salvo âncora `[FONTE]`/`[FATO ARQUITETURAL]` explícita. O repo SOT-Harness permanece a autoridade literal; esta emenda existe para auditoria do Revisor e decisão de Andraus.

---

## 1. Justificativa `[INFERÊNCIA]`

O invariante "o SOT não executa; produz um artefato de fronteira para o downstream" reside hoje em **6 loci** que divergiram terminologicamente: cinco deles falam em **TMP** como o artefato **de fronteira** (CONSTITUTION P14, atomic-spec INV-05, GLOSSARIO l.52, CHUNK-SY-007, AGENTS #9), enquanto a base fundacional do projeto — ENGENHARIA-GERAL Doc03 §20, l.604–606 — usa **"Signal Package"** como o termo original do artefato que atravessa a fronteira SOT → Bot Trade Finance `[FONTE]`:

> *"O SOT nunca executará ordens diretamente. Após atingir convicção suficiente, produzirá um Signal Package padronizado para integração com o seu Bot Trade Finance…"* (ENGENHARIA-GERAL l.604–606).

O "TMP" foi introduzido **depois**. Com a repurposação da SPEC-016 (Andraus 2026-09-22, C-04 Opção A — ROADMAP l.212-213 `[FONTE]`), o TMP passa a ser **artefato interno de passagem** entre a Síntese e o Risk Agent, e o **Signal Package** volta a ser o **único artefato de fronteira**. Esta emenda **restaura o termo fundacional** e faz os 6 loci convergirem horizontalmente (MAN-001), **sem** introduzir componente ainda inexistente (C-03: sem "Risk Harness").

Aproveita-se a mesma emenda para (a) registrar a **terminologia concorrente** TMP↔Signal Package sob RULE-SEM/MSC-001 (sem deletar "TMP" — INV-07) e (b) **consolidar** o R:R já vigente e **instituir** os dois invariantes de risco novos que Andraus decidiu (Portfolio Heat, alavancagem dinâmica), **sem** qualquer linguagem de supersedação do "ARR" (RISK-ARR-LOC-001 aberta — F-01).

---

## 2. Escopo e Non-goals (D1)

**No escopo (autorizado por Andraus 2026-09-22 — não ampliar):**
1. Emenda à CONSTITUTION P14 + convergência horizontal MAN-001 dos 6 loci.
2. Reconciliação semântica TMP (interno) ↔ Signal Package (fronteira) via RULE-SEM/MSC-001.
3. Consolidação de R:R ≥ 1:3 + instituição de Portfolio Heat ≤ 15% e alavancagem dinâmica.

**Fora do escopo (Non-goals):**
- **NÃO** menciona o Risk Harness (C-03) — a cláusula "via Risk Harness" só entra em P14/INV-05 quando **RISK-SPEC-020** for homologada.
- **NÃO** cria a FASE RISK (EUA-E20 futura); **NÃO** especifica nenhuma RISK-SPEC (BL-018 diferido).
- **NÃO** fecha RISK-ARR-LOC-001, RISK-CONV-001, D-RISK-SP-001, CDM-001, I-001, J-001 (§9).
- **NÃO** redefine nenhum Modelo Canônico (CC-02); **NÃO** toca o Conviction Vector 8D/J-001 (CC-03).

---

## 3. Bloco Herança / Delta (§8.3 — CC-08) `[PROPOSTA]`

```
HERANÇA / DELTA — EUA-E19a

INHERITS (herdado — referência por ID + versão; NÃO redefinido):
  - Constituição/Princípios: CONSTITUTION P14 (integração desacoplada) · P13 (auditabilidade)
  - Invariantes: INV-05 (SOT não executa) · INV-07 (versionamento monotônico) · INV-09 (sem baseline informal) · INV-10 (idioma canônico)
  - Método: atomic-spec v1.4 (F.1–F.4, E0–E3, §8.3, §10.5)
  - Regras herdadas: RULE-SEM-01/04 + CC-10 (EUA-E06) · RULE-HD-01..04 + CC-08 (EUA-E04)
  - R:R vigente: RULE-006 · RULE-ICT-002 · CEE-001 §11 Salvaguarda 5 (permanecem vigentes)
  - Fundacional: ENGENHARIA-GERAL Doc03 §20 l.604–606 ("Signal Package")

ADDED (delta local desta emenda):
  - Restauração do termo "Signal Package" como artefato de fronteira nos 6 loci
  - Reconhecimento de "TMP" como artefato INTERNO (Síntese → Risk Agent)
  - Registro de terminologia concorrente TMP↔Signal Package (RULE-SEM/GLOSSARIO)
  - Invariantes de risco: INV-RISK-RR (consolidação) · INV-RISK-HEAT (novo) · INV-RISK-LEV (novo)

MODIFIED (especialização de regra herdada):
  - INV-05 / P14: papel de FRONTEIRA transferido de "TMP" para "Signal Package";
    "TMP" MODIFICADO para papel interno. (Não é remoção — é reatribuição de papel.)

REMOVED (só com governança — nunca implícito):
  - (vazio) — "TMP" NÃO é removido de nenhum locus (INV-07). Muda de papel, permanece registrado.
```

> **Nota CC-08 / RULE-HD-02:** nenhum item ADDED contradiz o herdado. A reatribuição de papel de fronteira (TMP→Signal Package) é coerente com a repurposação já autorizada da SPEC-016 (C-04) e com o termo fundacional (ENGENHARIA-GERAL). **RULE-HD-03:** REMOVED vazio — "TMP" preservado (INV-07).

---

## 4. Ponto 1 — Emenda à CONSTITUTION P14 + convergência horizontal dos 6 loci (D2) `[PROPOSTA]`

### 4.1 Texto novo do invariante (aplicável a todos os loci)

> **"O SOT não executa ordem; produz um Signal Package para o Bot Trade Finance. O TMP é artefato interno de passagem entre a Síntese e o Risk Agent."**

**Restrição C-03 (crítica):** a cláusula **"via Risk Harness"** NÃO integra este texto. Ela só será acrescentada a P14/INV-05 **quando RISK-SPEC-020 for homologada** — evita invariante constitucional apontando para componente inexistente (CONS-01). `[FATO ARQUITETURAL — decisão de Andraus 2026-09-22, C-03]`

### 4.2 Convergência horizontal MAN-001 — os 6 loci

A aplicação física do texto a cada locus é **ato do Controlador pós-homologação** (não editado nesta proposta — padrão EUA-E04). A tabela abaixo é o alvo de convergência:

| # | Locus | Texto atual (âncora) `[FONTE]` | Delta a aplicar |
|---|---|---|---|
| L1 | CONSTITUTION P14 (l.80-81) + diagrama (l.104-107) | "Produz um Trading Mission Package (TMP) para o Bot Trade Finance"; diagrama `Synthesis → TMP → Bot Trade Finance` | Substituir por texto §4.1; diagrama passa a `Synthesis → [TMP interno] → … → Signal Package → Bot Trade Finance` (o "…" downstream permanece não-nomeado até RISK-SPEC-020, C-03) |
| L2 | atomic-spec INV-05 §13 (l.336) | "SOT não executa ordem; produz o Trading Mission Package (TMP)" | Substituir por texto §4.1 |
| L3 | GLOSSARIO l.52 | "TMP … Contrato final que atravessa a fronteira SOT → sistema de execução downstream" | TMP reclassificado como artefato **interno**; nova entrada "Signal Package" = artefato de fronteira (ver §5) |
| L4 | CHUNK-SY-007 (rag/synthesis.knowledge.md l.133+) | "O TMP é o output final do sistema para o Bot Trade Finance" | TMP = handoff interno Síntese→Risk Agent; output de fronteira = Signal Package |
| L5 | AGENTS.md não-negociável #9 (l.103) | "SOT não executa ordem — produz o Trading Mission Package (TMP)" | Substituir por texto §4.1 |
| L6 | ROADMAP SPEC-016 (l.212-213) | Já repurposada (C-04): TMP = handoff interno; fronteira → RISK-SPEC-022 (Signal Package) | **Já convergente** — apenas confirmar alinhamento terminológico com §4.1 |

> **BASpec-E19a-01** — QUANDO qualquer um dos 6 loci descreve o artefato que atravessa a fronteira SOT→downstream · ENTÃO ele DEVE nomeá-lo "Signal Package" e descrever o "TMP" como artefato interno Síntese→Risk Agent · PORQUE termo fundacional (ENGENHARIA-GERAL l.604-606) + repurposação SPEC-016 (C-04) + convergência horizontal MAN-001 · REFERÊNCIA: CONSTITUTION P14, MAN-001, EUA-E19a §4.1 · VERIFICADO POR: DADO os 6 loci pós-Controlador · QUANDO auditados por termo de fronteira · ENTÃO nenhum locus nomeia "TMP" como artefato de fronteira e nenhum menciona "Risk Harness" (C-03).

---

## 5. Ponto 3 — Reconciliação semântica TMP ↔ Signal Package (RULE-SEM/MSC-001) (D2) `[PROPOSTA]`

Registro de **terminologia concorrente** no GLOSSARIO (seção Terminologia Concorrente, padrão MSC-001/EUA-E06) — **sem deletar "TMP"** (INV-07):

| Termo | Acepção após E19a | Papel |
|---|---|---|
| **TMP (Trading Mission Package)** | Artefato **interno** de passagem — snapshot da decisão de síntese entregue por handoff à camada de risco | Interno (Síntese → Risk Agent). Ancora INV-RISK-00 (isolamento epistêmico) — declarado na SPEC-016 repurposada, não aqui |
| **Signal Package** | Artefato **de fronteira** — único artefato que atravessa SOT → Bot Trade Finance | Fronteira (termo fundacional restaurado) |

> **BASpec-E19a-02** — QUANDO um componente ou spec usa "TMP" ou "Signal Package" com sentido decisivo para fronteira vs. interno · ENTÃO DEVE declarar explicitamente qual acepção usa (RULE-SEM-01) e NÃO DEVE redefinir o termo canônico do GLOSSARIO (RULE-SEM-04) · PORQUE a distinção fronteira/interno é decisiva para INV-05 e para o isolamento epistêmico downstream · REFERÊNCIA: RULE-SEM-01/04, CC-10, MSC-001 · VERIFICADO POR: DADO um texto que cite ambos os termos · QUANDO auditado · ENTÃO cada uso tem acepção declarada e "TMP" permanece registrado (não deletado — INV-07).

**Superseder ≠ deletar:** o **papel de fronteira** do TMP é **supersedido** pelo Signal Package; o **objeto TMP permanece** registrado (agora com papel interno). Nenhum conteúdo é apagado (INV-07/RULE-HD-03).

---

## 6. Ponto 4 — Consolidação de R:R + instituição de invariantes de risco (D2) `[PROPOSTA]`

> **Namespace:** prefixo **INV-RISK-** (evita colidir com INV-* do SOT). Estes invariantes são instituídos em nível de governança; sua **operacionalização e enforcement** (gate, cálculo) ficam **diferidos** à família RISK-SPEC (BL-018) — esta emenda não os especifica.

| ID | Invariante | Natureza | Relação com repo |
|---|---|---|---|
| **INV-RISK-RR** | R:R ≥ 1:3 **(risco:retorno = 3:1 retorno:risco; numérico ≥ 3.0)** como mínimo de risco | **Consolidação** — RULES permanecem vigentes; herdadas, não duplicadas | Consolida RULE-006 · RULE-ICT-002 · CEE-001 §11 Salvaguarda 5 (Q-004). **Zero supersedação** de ata/componente |
| **INV-RISK-HEAT** | Portfolio Heat ≤ 15% | **NOVO** — instituído aqui | Não existe no repo atual (F-01) |
| **INV-RISK-LEV** | Risco por operação **dinâmico**, sensível à oportunidade, incluindo sugestão de alavancagem | **NOVO** — instituído aqui | Não existe no repo atual (F-01) |

**Zero supersedação do ARR (C-09):** o "ARR"/"D-ARR-001" **não existe como componente formal no repo** (F-01, parecer 2026-09-22). Portanto INV-RISK-RR **consolida** RULES já vigentes (que permanecem em vigor) e **não superseda** nada. Enquanto **RISK-ARR-LOC-001** estiver aberta, esta emenda usa **exclusivamente** linguagem de consolidação/instituição — nunca de supersedação. `[FATO ARQUITETURAL — Andraus 2026-09-22, C-09]`

> **BASpec-E19a-03** — QUANDO o SOT avalia a admissibilidade de uma oportunidade para exposição · ENTÃO R:R DEVE ser ≥ 1:3 (≥ 3.0 numérico) E o Portfolio Heat DEVE permanecer ≤ 15% · PORQUE preservação de capital e proporcionalidade de risco (invariantes mínimos) · REFERÊNCIA: INV-RISK-RR/HEAT, RULE-006, CEE-001 §11 Salv.5 · VERIFICADO POR: DADO uma oportunidade com R:R = 2.5 **ou** Heat resultante = 16% · QUANDO avaliada · ENTÃO é rejeitada por violar invariante mínimo. *(A verificação como gate E3 é diferida à RISK-SPEC-020 — C-03; aqui institui-se apenas o invariante.)*

---

## 7. Enforcement (onde há efeito) `[PROPOSTA]`

Esta emenda é **F.1 (feedforward/autoridade)** — não tem efeito de runtime próprio. Registra, porém, a implicação de enforcement do artefato de fronteira que ela renomeia:

```
CAPABILITY   : emitir o artefato de fronteira SOT → Bot Trade Finance
EFFECT       : emissão externa do Signal Package (cruza a fronteira do SOT)
PRECOND      : (diferida) — invariantes de risco satisfeitos; contrato do Signal Package
POSTCOND     : (diferida) — artefato de fronteira emitido e auditável
POLICY       : INV-05 (SOT não executa); INV-RISK-RR/HEAT/LEV
LEVEL        : E3 (crítico + irreversível — emissão externa)
FAILURE-MODE : fail-closed — sem emissão. GATE/mecanismo DIFERIDO à RISK-SPEC-020 (C-03).
ENF-07       : método de falso-DENY (amostral, sem limiar fixo) DIFERIDO à RISK-SPEC-020 (m-003).
EVIDENCE     : (diferida à RISK-SPEC-020/022)
```

> **Nota C-03/ENF-03:** o gate determinístico da emissão (LLM não é seu próprio gate) NÃO é especificado aqui — é a RISK-SPEC-020, ainda inexistente. Esta emenda apenas **classifica** o efeito como E3 fail-closed e defere o mecanismo. Não há detector/gate criado nesta proposta.

---

## 7-bis. Autopré-check de Redução de Viés (EUA-E18) `[PROPOSTA]`
<!-- Adicionado como delta editorial na homologação (M-001, Revisor 2026-09-22). -->

**Bloco A — Casos de negação por BASpec:**
- **BASpec-E19a-01** (convergência dos 6 loci): negação plausível — um locus permanece nomeando "TMP" como fronteira, ou um locus passa a mencionar "Risk Harness" (viola C-03). Detectável por auditoria dos 6 loci pós-Controlador (o VERIFICADO POR da BASpec).
- **BASpec-E19a-02** (terminologia concorrente): negação — um uso de TMP/Signal Package sem acepção declarada, ou "TMP" deletado de um locus (viola INV-07). Detectável por leitura do GLOSSARIO §3-bis + loci.
- **BASpec-E19a-03** (invariantes de risco): negação — oportunidade com R:R < 1:3 ou Heat > 15% admitida. Detectável por exemplo numérico (R:R=2.5 ou Heat=16% → rejeição). *(Gate E3 diferido à RISK-SPEC-020.)*

**Bloco B — Herança obrigação-a-obrigação (CC-08):** INHERITS lista por ID+versão (INV-05/07/09/10, RULE-SEM-01/04, RULE-HD-01..04, atomic-spec v1.4, RULE-006/ICT-002/CEE-001 §11 Salv.5, ENGENHARIA-GERAL Doc03 §20). MODIFIED = reatribuição de papel de fronteira TMP→Signal Package (não remoção). REMOVED vazio (INV-07). Nenhuma obrigação herdada suprimida ou contradita (RULE-HD-02/03). Ver §3.

---

## 8. Constitution Check (§10.5 + emendas) `[PROPOSTA]`

| ID | Item | Resultado |
|---|---|---|
| CC-01 | Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT | N/A — emenda não toca hierarquia analítica. PASS |
| CC-02 | Não redefine Modelo Canônico (CEM/CHM/CCM/CDM/CNM) | PASS — nenhum canônico tocado; "Signal Package"/"TMP" não são canônicos |
| CC-03 | Conviction Vector 8D; limiares definitivos = J-001 aberto | PASS — não toca Conviction Vector; J-001 permanece aberta (§9) |
| CC-04 | 5+5 Salvaguardas (CEE-001 §10/§11) não violadas | PASS — INV-RISK-RR consolida §11 Salv.5 sem alterá-la; INV-04 (custo≠convicção) intacto |
| CC-05 | Complexidade declarada | HIGH (emenda constitucional multi-locus, D0–D2 + BASpecs) |
| CC-06 | Campos SES-001 §59 | N/A — não é Engineering Card |
| CC-07 | Cadeia de derivação SES-001 §60 | N/A — não é Engineering Card |
| CC-08 | Bloco Herança/Delta declarado | PASS — §3 (INHERITS/ADDED/MODIFIED preenchidos; REMOVED vazio) |
| CC-09 | Status epistemológico / Epistemic Check | PASS — tudo `[PROPOSTA]`; decisões de Andraus marcadas `[FATO ARQUITETURAL]`; nenhuma hipótese como fato |
| CC-10 | Terminologia concorrente declarada (RULE-SEM) | PASS — §5 registra TMP↔Signal Package |

---

## 9. Decisões abertas incidentes (CONS-01 — NÃO fechar) `[DECISÃO NECESSÁRIA]`

| ID | Estado | Por que permanece aberta |
|---|---|---|
| RISK-ARR-LOC-001 | **Aberta** | ARR não existe no repo; esta emenda consolida RULES + institui invariantes, sem supersedação. Não fecha |
| RISK-CONV-001 | **Aberta** | "convicção de risco" vs Conviction Vector 8D/J-001 — fecha em RISK-SPEC-010, não antes de J-001 |
| D-RISK-SP-001 | **Aberta** | Contrato exato (campos/schema) do Signal Package — diferido à RISK-SPEC-022 |
| CDM-001 | **Aberta** | Idioma canônico do RDR — diferido à RISK-SPEC-021 |
| I-001 | **Aberta** | Skills como unidades formais — RISK-SPEC-SKL-* |
| J-001 | **Aberta** | Fórmula/pesos/limiares definitivos do Conviction Vector — SPEC-003 |

> **Nota CONS-01:** nenhum item acima aparece como invariante fechado nesta emenda. A cláusula "via Risk Harness" (C-03) é o único elemento explicitamente adiado para RISK-SPEC-020.

---

## 10. Fluxo de autoridade

```
[feito] Especificador redige esta PROPOSTA
   ↓
Revisor SOT (GRE-001/HRE-001) emite parecer contra CONSTITUTION P14, INV-05/07/09, MAN-001,
   RULE-SEM/CC-10, RULE-HD/CC-08, CEE-001 §11, e a restrição C-03
   ↓
Andraus homologa (DHR-EUA-E19a)
   ↓
Controlador aplica os deltas aos 6 loci + GLOSSARIO/RULES + registra terminologia concorrente
   ↓
(futuro) EUA-E20 institui a FASE RISK; RISK-SPEC-020 acrescenta "via Risk Harness" a P14/INV-05
```

---

## 11. Autopré-check do Especificador (2026-09-22)

- [x] ROADMAP lido — SPEC-016 REPURPOSADA (l.212-213); RISK-ARR-LOC-001/RISK-CONV-001 registradas; FASE GOV fixa (EUA-E17); nada tratado como baseline.
- [x] atomic-spec v1.4 lido — método (BASpec, §8.3/CC-08, §10.5, INV-05 §13, Enforcement E0–E3, etiquetagem).
- [x] Nenhum invariante congelado violado: INV-05 é **emendado por proposta** (não silenciosamente); INV-07 preservado (TMP não deletado); INV-09 respeitado (nada declarado baseline).
- [x] Ponto 1 coberto: §4 — texto novo §4.1 + tabela de convergência dos 6 loci + BASpec-E19a-01.
- [x] Ponto 2 (C-03) coberto: sem menção ao Risk Harness; cláusula "via Risk Harness" diferida a RISK-SPEC-020 (§4.1, §7, §9).
- [x] Ponto 3 coberto: §5 — reconciliação TMP↔Signal Package com RULE-SEM-01/04 + CC-10; TMP não deletado (INV-07); papel de fronteira supersedido.
- [x] Ponto 4 coberto: §6 — INV-RISK-RR (consolidação, zero supersedação — C-09), INV-RISK-HEAT (novo), INV-RISK-LEV (novo); convenção R:R exata (Q-004).
- [x] Bloco Herança/Delta (§3) + CC-01..CC-10 (§8) presentes.
- [x] Enforcement (§7): efeito de fronteira classificado E3 fail-closed; mecanismo/gate diferido (C-03/ENF-03) — não cria detector/gate aqui.
- [x] Etiquetagem TRACE-06 aplicada; decisões de Andraus marcadas `[FATO ARQUITETURAL]`; demais `[PROPOSTA]`.
- [x] CONS-01: RISK-ARR-LOC-001, RISK-CONV-001, D-RISK-SP-001, CDM-001, I-001, J-001 mantidas abertas (§9); nenhuma usada como invariante fechado.
- [x] Non-goals respeitados: não cria FASE RISK, não especifica RISK-SPEC, não redefine canônicos, não toca J-001/Conviction 8D.
- [x] "Pronto para revisão."

---

*PROPOSTA não-homologada. Autoridade literal permanece: CONSTITUTION + atomic-spec v1.4 + documentos-base. Esta emenda não altera nenhum baseline; existe para auditoria do Revisor e decisão de Andraus. Produzida pelo Especificador (Claude Code) em 2026-09-22.*
