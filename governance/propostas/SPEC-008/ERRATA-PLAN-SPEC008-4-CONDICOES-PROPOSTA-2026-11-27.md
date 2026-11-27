# Errata aditiva ao Plan v1.2 da SPEC-008 — as 4 condições da homologação (R3-m04, R3-m05, R3-m07, R3-m08) — PROPOSTA

| Campo | Valor |
|---|---|
| Alvo | `specs/features/SPEC-008/plan.md` **v1.2 — BASELINE** (Andraus, 2026-11-15, `DHR-SPEC008-005`; SHA256 na ata `21a52c6b…dc73df8`) + `checks.md` (verificação) + `HISTORICO.md` (histórico, não-norma) |
| Origem | `DHR-SPEC008-005` §3 itens 1–4 (condições: "a cumprir por errata aditiva ao Plan, em passo à parte por ordem de Andraus") · achados R3-m04, R3-m05, R3-m07, R3-m08 de `governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-PLAN-R3-2026-11-15.md` (l.144–148; bloco ACHADOS-ESTRUTURADOS l.169–173) |
| Ordem | Andraus escolheu "errata das 4 condições SPEC-008" como próxima frente (AskUserQuestion, 2026-11-17) e disse "Prossiga" (chat, 2026-11-27) — repassado pelo Orquestrador (CLASSE-TAREFA O). O chat não foi visto pelo Especificador. |
| Autor | Especificador Principal SOT |
| Data | 2026-11-27 |
| Status | **PROPOSTA** — nada aplicado. Só vigora com homologação de Andraus (INV-09; RULE-HG-02/03). Nenhuma decisão aberta é fechada (CONS-01). |
| Rodada | **R3** — correção do parecer R2 (`PARECER-REVISOR-ERRATA-PLAN-SPEC008-R2-2026-11-27.md`, NÃO CONFORME, 1 Média + 2 Menores): R2-M1 por decisão de Andraus (AskUserQuestion 2026-11-27: "Seguir o plano homologado") — §3.1-bis retirado, ADV-12 (d) só com o que a D4.2 vigente garante, lacuna residual em §3.0-bis; R2-m01 (§2.3); R2-m02 (§1, §10). Anterior: R2 — correção do parecer R1 (`PARECER-REVISOR-ERRATA-PLAN-SPEC008-R1-2026-11-27.md`, CONFORME condicional, 7 Menores): R1-m01 (§3), R1-m02 (§2.1-bis, §1, §2.0, §6), R1-m07 (§4.6, §4.0). R1-m03..m06 aplicados pelo Orquestrador (FICHA-M), mantidos. Decisões E-1..E-5 de Andraus (AskUserQuestion, 2026-11-27) incorporadas (§9). |
| Forma | **Decidida por Andraus em 2026-11-27 (E-2):** **arquivo à parte + ponteiro de uma linha** no Status do `plan.md` (e, se Andraus quiser, uma linha no "Objeto" do `checks.md`), sem alterar o texto baselined — precedente `DHR-SPEC006-005` D2 (l.19). O §2–§5 traz, para cada alvo, o **texto vigente literal** e o **texto novo** (com `[antes: …]`), que é o texto a ler sob a errata. *[antes: "Forma recomendada | … para que a mesma errata sirva à forma \"no próprio lugar\" se Andraus a preferir (§7, E-2)."]* |
| Compatibilidade | **Minor — decidida por Andraus em 2026-11-27 (E-1):** Plan v1.2 → v1.3 (§6). *[antes: "**Minor** recomendada (Plan v1.2 → v1.3); hipótese Major registrada (§6). Escolha de Andraus."]* |

Convenção desta proposta: `[FATO]` = texto homologado/baseline ou ata, com âncora; `[INFERÊNCIA]` = leitura derivada, com âncora; `[PROPOSTA]` = texto novo desta errata; `[DECISÃO NECESSÁRIA]` = só Andraus. Os alvos são citados por **ID do bloco + trecho literal** (sem número de linha como âncora; os números entre parênteses são só auxílio de leitura, foto de 2026-11-27).

---

## 0. Leituras feitas (base desta proposta)

`ROADMAP.md` (SPEC-008: Plan v1.2 BASELINE, 4 condições; Decisões abertas); `atomic-spec.md` (método); `DHR-SPEC008-005` §1–§5; parecer R3 (l.100–175); `plan.md` v1.2 (INV-MDC-01, RULE-MDC-003/004/005/006/007/009/011, EARS, D3.1, BASpec-003/011/012, D4.1, D4.2, D5, Interface, contrato lógico, D7 T11–T23, D8 ADV-12, EC-004/007/008, §7-bis); `checks.md` (§0, §2, §4, §5); `HISTORICO.md`; `DHR-SPEC008-004` (DN-2); parecer R2 (FICHA-M, l.182–247); `FICHA-ESQUELETO-PLAN-R2.json`; `DIFF-PLAN-V1.0-ATUAL-2026-11-14.patch`; `DELTA-SPEC-008-plan-366af09-44e6131f.txt`; `scripts/spec_delta.py` (definição de bloco); `canon/CR-001-compliance-record.md` §7.7 (l.437–451); `DHR-SPEC006-005` (forma); `MMC-001` (Grep: nenhum tipo de aviso nem "Andraus/Fase 0" no pai). Modelo de forma: `ERRATA-MMC-001-R3-m07-PROPOSTA-2026-11-08.md`.

---

## 1. Escopo e alvos (únicos)

| Condição | Alvos no `plan.md` | Alvos no `checks.md` | Outros |
|---|---|---|---|
| 1 — R3-m04 [C10] | RULE-MDC-003 (h); **RULE-MDC-010 (b) e BASpec-MDC-010 ENTÃO (exceção nomeada de retomada — R1-m02)**; D4.2 passo (3) + simulação; D5 F16 (célula Ação) e nota "Falha de `time_request`"; EC-MDC-004 FAILURE-MODE; EARS 3; BASpec-MDC-003 (ENTÃO, DADO, VERIFICAÇÃO); BASpec-MDC-011 (DADO, VERIFICAÇÃO); D3.1 linha `MDC_TIME_REQUEST_FAILED`; **Cenário-MDC-T24 (novo)**; contagens | §0 F6; §2 linha `MDC_TIME_REQUEST_FAILED` e parágrafo da simulação; §4 matriz (RULE-MDC-003, RULE-MDC-011); **§5 ✔ da falha por capacidade** | — |
| 2 — R3-m05 [C05] | INV-MDC-01 (frase "no pedido, nada é aberto"); ADV-MDC-12 (variante (d)); D3.1 linha `MDC_CAPABILITY_CHECK_FAILED`; BASpec-MDC-012 DADO; §7-bis Bloco A linha 012 | §2 linha `MDC_CAPABILITY_CHECK_FAILED` e simulação | — |
| 3 — R3-m07 [C01] | contrato lógico `notice`; EC-MDC-007 CAPABILITY; RULE-MDC-004 (d); EARS 5; Cenário-MDC-T18 (ENTÃO, VERIFICAÇÃO); **"Requisitos a outras Specs", item SPEC-015 (R1-m07)** | — | — |
| 4 — R3-m08 [C06] | — | — | `HISTORICO.md`, tabela "R2 → R3": 3 linhas acrescentadas (§5) |

**Nada mais é tocado** `[PROPOSTA]`: nenhuma outra RULE, EARS, BASpec, EC, linha de D5, cenário ou ADV; nenhum estado, seta, evento, código `MDC_*` ou campo de contrato novo; nenhuma linha de WF-F02 nova (WORKFLOW.md §3.2.3 intocado). IDs novos: só **Cenário-MDC-T24** e a variante **ADV-MDC-12 (d)** (sem renumerar — INV-07). Nenhum subcódigo novo foi necessário: ADV-12 (d) usa o código e o sub vigentes (`MDC_CAPABILITY_CHECK_FAILED` / `MDC_CAPABILITY_REGISTRY_UNAVAILABLE`). **Não tocados por decisão de Andraus (2026-11-27, R2-M1: "Seguir o plano homologado"):** D4.1 (inclusive SAÍDA), D4.2, D5 F01/F37, RULE-MDC-001, BASpec-MDC-001 — nenhuma ordem de gravação nova; o que o Plan vigente não define na falha parcial da F01 fica como lacuna residual (§3.0-bis). *[antes (R2 desta errata): na linha da condição 2 deste quadro constava o alvo "**D4.1 SAÍDA (uma frase — R1-m01)**"]* **Exceções nomeadas a regras gerais** (R1-m02), declaradas aqui e no §6: (1) RULE-MDC-003 (h) / D4.2 (3) — a recusa do `MARK_CONSUMED` da F16 entra na exceção que já existia para o ENC; (2) RULE-MDC-010 (b) / BASpec-MDC-010 — o `MARK_CONSUMED` de ENC/F16 com recusa registrada **não** é "efeito registrado e não confirmado" e não é reemitido na retomada. Nenhuma das duas cria regra (ID) nova: são alíneas de exceção dentro das regras existentes. *[antes: "…Nenhum subcódigo novo foi necessário."]*

---

## 2. Condição 1 — R3-m04 [C10]: falha do `MARK_CONSUMED` pedido por F16

### 2.0 Problema e decisão de desenho

`[FATO]` F16: `ATIVADO` × `PUB(OPERACIONAL)` setup, guarda "elegível ∧ alinhado" → `EM_SÍNTESE`, ação "`MARK_CONSUMED`; publica `phase2_handoff`" (D5). F38 só vale em "`AGUARDANDO`…`ATIVADO`" (D5). A exceção nomeada da D4.2 passo (3) só cobre "a recusa do `MARK_CONSUMED` pedido pela própria linha de ENC — F20/F22 etc." `[INFERÊNCIA]` (parecer R3 l.144): a recusa do `MARK_CONSUMED` da F16, tratada como evento interno `TIME_REQUEST_FAILED`, chega com o ciclo já em `EM_SÍNTESE` e para na D4.2 passo (4) (`MDC_NOT_PHASE1_TRANSITION`, F27): sem reenvio e sem cenário; o ✔ do `checks.md` §5 ("Falha de cada capacidade com efeito … tem caminho fechado") é amplo demais.

**Decisão — opção (b), desfecho aceito + T24 (decidida por Andraus em 2026-11-27, E-5).** A ata §3 item 1 admitia (a) ordem (confirmação antes da transição) ou (b) desfecho aceito. (a) foi descartada: exigiria memória de "setup aceito à espera" e guarda nova na F16/F38 e perderia um setup válido por falha do serviço de tempo (F20) `[INFERÊNCIA]`. *[antes: lista "Opções (ata §3 item 1)" com o item "(a) Ordem — confirmação antes da transição. A F16 só passaria a `EM_SÍNTESE` depois de o `MARK_CONSUMED` ser aceito. Recusa ⇒ ciclo fica em `ATIVADO` com setup aceito pendente, F38 reenvia, e acima do teto F20 encerra. Custos: …" e "(b) Desfecho aceito (escolhida)."]*
- **(b) Desfecho aceito.** A recusa do `MARK_CONSUMED` da F16 é **resultado do efeito da própria linha** (como já é para o ENC — exceção R3-m02, D4.2 passo (3)): grava a entrada `MDC_TIME_REQUEST_FAILED` no passo (9), uma tentativa, sem reenvio, sem F38/F20/F27; a transição e o `phase2_handoff` seguem; o alarme, que já está `TRIGGERED`, termina pela FSM dele (WF-A02: `TRIGGERED` → {`CONSUMED` | `EXPIRED` | `CANCELLED`}) e o aviso dessa morte chega ao ciclo em `EM_SÍNTESE` ⇒ D4.2 (4)/F27, sem efeito (T-9).

**Por que (b)** `[INFERÊNCIA]`: (1) é a **menos invasiva**: estende uma exceção que já existe (R3-m02) a uma linha a mais; não cria estado, seta, evento, guarda, linha de D5 nem código (WF-F02 intacto); (2) **fail-safe**: o alarme `TRIGGERED` não dispara de novo (WF-A02 só tem saídas terminais a partir de `TRIGGERED`) e nenhum ICT é redespachado (ciclo fora da Fase 1 — RULE-MDC-011 (c)); (3) preserva a Eficácia: o setup aceito chega à Fase 2; (4) mesmo desfecho observável que a leitura atual "sem reenvio", agora declarado e testado. **Não cria regra (ID) nova**; cria duas **exceções nomeadas** dentro de regras existentes — RULE-MDC-003 (h) (já tinha a do ENC; ganha a F16) e RULE-MDC-010 (b) (retomada: recusa registrada não é reemitida — §2.1-bis; R1-m02) —, ambas nomeadas no texto da regra geral e declaradas no §1 e no §6. Efeito colateral declarado: a Fase 2 recebe um `alarm_ref` cujo estado final pode ser `EXPIRED`/`CANCELLED` em vez de `CONSUMED` — observação para a abertura da SPEC-014, nada decidido aqui (§8).

### 2.1 RULE-MDC-003 (h) — última frase

**Vigente (literal, última linha da alínea):**
```
                (idempotente — T-5); acima ⇒ RULE-MDC-008 (b) (F20). Em ciclo já encerrado, sem reenvio.
```
**Novo `[PROPOSTA]`:**
```
                (idempotente — T-5); acima ⇒ RULE-MDC-008 (b) (F20). Em ciclo já encerrado, sem reenvio. Exceção
                nomeada: a recusa do `MARK_CONSUMED` pedido pela própria linha de ENC ou pela F16 (que já entra em
                `EM_SÍNTESE`) é RESULTADO do efeito dessa linha — entrada `MDC_TIME_REQUEST_FAILED`, uma tentativa,
                sem reenvio e sem F38/F20/F27/F28; o ENC é mantido (T23 (c)) e, na F16, a transição e o
                `phase2_handoff` seguem (T24); o desfecho registrado não é "efeito não confirmado" para a retomada
                (RULE-MDC-010 (b)): não é reemitido; o alarme, já `TRIGGERED`, termina pela FSM dele (WF-A02; T-9).
                *[antes: "(idempotente — T-5); acima ⇒ RULE-MDC-008 (b) (F20). Em ciclo já encerrado, sem reenvio."
                — falha do MARK_CONSUMED da F16 sem desfecho declarado (R3-m04)]*
```
Nota `[INFERÊNCIA]`: a frase sobre a retomada fecha um furo que o mesmo caminho do ENC já tinha (T23 (c) diz "sem reenvio", e RULE-MDC-010 (b) manda reemitir "efeito registrado e não confirmado"); a recusa síncrona (T-10) é confirmação **negativa**, não ausência de confirmação.

### 2.1-bis RULE-MDC-010 (b) e BASpec-MDC-010 ENTÃO — exceção nomeada na regra geral (R1-m02)

A frase de retomada de 2.1 excepciona a regra geral de reemissão; por isso a exceção é nomeada **também** no texto da regra geral e da BASpec que a aplica (prevenção R1-m02: "toda exceção a regra geral nomeada no próprio texto da regra geral").

- **RULE-MDC-010 (b), vigente (trecho literal):** `Efeito registrado e não⏎                confirmado ⇒ na retomada é reemitido com a MESMA chave de idempotência (sem duplicar).`
  **Novo `[PROPOSTA]`:** `Efeito registrado e não confirmado ⇒ na retomada é reemitido com a MESMA chave de idempotência (sem duplicar). Exceção nomeada: \`MARK_CONSUMED\` de ENC ou da F16 cuja recusa já está gravada (entrada \`MDC_TIME_REQUEST_FAILED\`) tem desfecho registrado — não é "não confirmado" e não é reemitido (RULE-MDC-003 (h); T23 (c); T24). *[antes: "Efeito registrado e não confirmado ⇒ na retomada é reemitido com a MESMA chave de idempotência (sem duplicar)." (R1-m02)]*`
- **BASpec-MDC-010 ENTÃO, vigente (literal):** `evento/timer; replay reconstrói o estado e reemite efeito pendente com a mesma chave`
  **Novo `[PROPOSTA]`:** `evento/timer; replay reconstrói o estado e reemite efeito pendente com a mesma chave (salvo \`MARK_CONSUMED\` de ENC/F16 com recusa já gravada — RULE-MDC-010 (b)) *[antes: "…replay reconstrói o estado e reemite efeito pendente com a mesma chave"]*`

Nota: o "⏎" marca a quebra de linha do bloco cercado no `plan.md`. A DADO/VERIFICAÇÃO da BASpec-MDC-010 não muda: T24 (cuja VERIFICAÇÃO inclui "inclusive depois de replay do livro") é citado pela BASpec-MDC-003 e pela BASpec-MDC-011, e a exceção é verificada ali.

### 2.2 D4.2 — passo (3) e simulação

**Vigente (trecho literal):** `(3) ciclo encerrado ou em estado final → \`MDC_CYCLE_CLOSED\` (exceção nomeada: a recusa do \`MARK_CONSUMED\` pedido pela própria linha de ENC — F20/F22 etc. — é RESULTADO do efeito dessa linha, gravado como entrada \`MDC_TIME_REQUEST_FAILED\` no passo (9); não é evento e não passa por este passo);`

**Novo `[PROPOSTA]`:** `(3) ciclo encerrado ou em estado final → \`MDC_CYCLE_CLOSED\` (exceção nomeada: a recusa do \`MARK_CONSUMED\` pedido pela própria linha de ENC — F20/F22 etc. — ou pela F16 é RESULTADO do efeito dessa linha, gravado como entrada \`MDC_TIME_REQUEST_FAILED\` no passo (9), sem reenvio — RULE-MDC-003 (h); não é evento e não passa por este passo nem pelo (4)); *[antes: "… — F20/F22 etc. — é RESULTADO do efeito dessa linha, gravado como entrada \`MDC_TIME_REQUEST_FAILED\` no passo (9); não é evento e não passa por este passo);" (R3-m04)]*`

**Vigente (trecho literal da simulação):** `T19 e ADV-06 (b) param no (3); T11 (b) para no (4);`

**Novo `[PROPOSTA]`:** `T19 e ADV-06 (b) param no (3); T11 (b) e o \`ALARM_EXPIRED\` posterior de T24 param no (4) (a recusa do \`MARK_CONSUMED\` da F16 em T24 não é evento — passo (9)); *[antes: "T19 e ADV-06 (b) param no (3); T11 (b) para no (4);"]*`

### 2.3 D5 — linha F16 (célula Ação)

**Vigente (linha inteira):** `| F16 | \`ATIVADO\` | \`PUB(OPERACIONAL)\` setup | elegível ∧ alinhado (RULE-MDC-006 (d)) | \`EM_SÍNTESE\` | \`MARK_CONSUMED\`; publica \`phase2_handoff\` | \`MDC_HANDOFF_PUBLISHED\` | SPEC-008 (última) |`

**Novo `[PROPOSTA]` (só a célula Ação):** `\`MARK_CONSUMED\` (uma tentativa; recusa ⇒ só entrada \`MDC_TIME_REQUEST_FAILED\`, sem reenvio, sem F27 — RULE-MDC-003 (h); T24); publica \`phase2_handoff\` *[antes: "\`MARK_CONSUMED\`; publica \`phase2_handoff\`"]*` — mesma forma da célula da F20.

**Coluna Código da F16 (R2-m01) — intencional, sem alteração:** a coluna "Código (`entry_type`/code)" continua `MDC_HANDOFF_PUBLISHED`, sem `MDC_TIME_REQUEST_FAILED`. É a mesma forma da F20: lá a coluna traz só `MDC_LIMIT_EXCEEDED` (sub), e a entrada `MDC_TIME_REQUEST_FAILED` da recusa aparece apenas na célula Ação. O motivo é que a coluna registra o código da **linha aplicada** (a transição ou o ENC que a guarda escolhe). A recusa do `MARK_CONSUMED` é uma entrada **secundária**, condicional ao resultado de um efeito: é gravada no passo (9) só quando a Spec de Tempo recusa, e por isso fica descrita na célula Ação (com remissão a RULE-MDC-003 (h) e T24), não na coluna Código.

### 2.4 D5 — nota "Falha de `time_request`" (última frase do parágrafo sob a tabela)

**Vigente (literal):** `\`MARK_CONSUMED\` pedido num ENC que falhe ⇒ só a entrada \`MDC_TIME_REQUEST_FAILED\` (ciclo já encerrado; sem reenvio; o alarme termina pelas regras da Spec de Tempo — T-3/T-6).`

**Novo `[PROPOSTA]` (acréscimo, frase vigente mantida):** `… — T-3/T-6). Idem para o \`MARK_CONSUMED\` da F16 (ciclo já em \`EM_SÍNTESE\`): só a entrada, sem reenvio e sem F27; o alarme, já \`TRIGGERED\`, termina \`EXPIRED\`/\`CANCELLED\` pela FSM dele (WF-A02) e esse aviso chega ao ciclo em \`EM_SÍNTESE\` ⇒ F27, sem efeito (T-9; T24). *[acréscimo R3-m04; frase anterior inalterada]*`

### 2.5 EC-MDC-004 — FAILURE-MODE (trecho final)

**Vigente:** `MARK_CONSUMED em ENC que falhe ⇒ só a entrada, sem reenvio (T23)`
**Novo `[PROPOSTA]`:** `MARK_CONSUMED em ENC ou na F16 que falhe ⇒ só a entrada, sem reenvio (T23; T24) *[antes: "MARK_CONSUMED em ENC que falhe ⇒ só a entrada, sem reenvio (T23)"]*`

### 2.6 EARS 3 — propagação (lição R3-m03: alínea de RULE propagada ao EARS do mesmo ID)

**Vigente (trecho):** `reenviar com a mesma \`request_key\` o pedido à Spec de Tempo recusado (contado em \`failures[TEMPO]\` até o teto) e NÃO DEVE consumir`
**Novo `[PROPOSTA]`:** `reenviar com a mesma \`request_key\` o pedido à Spec de Tempo recusado (contado em \`failures[TEMPO]\` até o teto) — salvo o \`MARK_CONSUMED\` pedido por linha de encerramento ou pela F16, cuja recusa só é registrada, sem reenvio — e NÃO DEVE consumir *[antes: "…(contado em \`failures[TEMPO]\` até o teto) e NÃO DEVE consumir"]*`
Modalidade preservada (RULE-SEM-03): o "DEVE reenviar" continua DEVE; a exceção já existia na RULE (ENC) e passa a constar também no EARS.

### 2.7 BASpec-MDC-003 — ENTÃO (última linha), DADO e VERIFICAÇÃO

- ENTÃO, **vigente:** `                time_request recusado ⇒ reenvio com a mesma request_key, contado em failures[TEMPO] (RULE-MDC-003 (h); F38)` → **novo:** `… (RULE-MDC-003 (h); F38); MARK_CONSUMED de ENC/F16 recusado ⇒ só registro, sem reenvio (T23 (c); T24) *[antes: "…(RULE-MDC-003 (h); F38)"]*`
- DADO, **vigente:** `    DADO        T01 · T14 · T15 (b)(c) · T22 (a)(b) · T23 · ADV-01 (aviso duplicado) · ADV-02 (retomada) · ADV-03 (outro ciclo) ·` → **novo:** `… · T23 · T24 · ADV-01 (aviso duplicado) · …` *[antes: "… · T23 · ADV-01 …"]*
- VERIFICAÇÃO, **vigente:** `    VERIFICAÇÃO ver T01 / T14 / T15 / T22 / T23 / ADV-01..04` → **novo:** `    VERIFICAÇÃO ver T01 / T14 / T15 / T22 / T23 / T24 / ADV-01..04` *[antes: "ver T01 / T14 / T15 / T22 / T23 / ADV-01..04"]*

### 2.8 BASpec-MDC-011 — DADO e VERIFICAÇÃO

- **Vigente:** `    DADO        T11 (a)(b) · ADV-10 (f)(g)(h)` → **novo:** `    DADO        T11 (a)(b) · T24 · ADV-10 (f)(g)(h)` *[antes: "T11 (a)(b) · ADV-10 (f)(g)(h)"]*
- **Vigente:** `    VERIFICAÇÃO ver T11 / ADV-10` → **novo:** `    VERIFICAÇÃO ver T11 / T24 / ADV-10` *[antes: "ver T11 / ADV-10"]*

### 2.9 D3.1 — linha `MDC_TIME_REQUEST_FAILED`

**Vigente:** `| \`MDC_TIME_REQUEST_FAILED\` | — | falha contada em \`failures[TEMPO]\` (reenvio, mesma \`request_key\`); estouro ⇒ \`MDC_LIMIT_EXCEEDED\` sub \`FAILURES\` | 003 (h) | T23 (a)–(c) |`
**Novo `[PROPOSTA]`:** `| \`MDC_TIME_REQUEST_FAILED\` | — | falha contada em \`failures[TEMPO]\` (reenvio, mesma \`request_key\`); estouro ⇒ \`MDC_LIMIT_EXCEEDED\` sub \`FAILURES\`; \`MARK_CONSUMED\` de ENC/F16: só entrada, sem reenvio | 003 (h) | T23 (a)–(c); T24 |` *[antes: a linha vigente acima]*. Idem, linha `MDC_NOT_PHASE1_TRANSITION`: `| 011 (c) | T11 (b) |` → `| 011 (c) | T11 (b); T24 |` *[antes: "T11 (b)"]* (R1-m03).

### 2.10 Cenário-MDC-T24 (novo — aditivo, logo depois de T23, antes do separador e de "## D8"; sem renumerar)

```
### Cenário-MDC-T24 — Falha do `MARK_CONSUMED` pedido pela F16 (MDC-003 (h); MDC-011 (c); F16/F27; T-9; T-10)
DADO        M0; ciclo de R1 em ATIVADO (OPERACIONAL despachado); a Spec de Tempo recusa na própria chamada (T-10) o
            MARK_CONSUMED(A1) pedido pela F16
QUANDO      S1 (alinhado, H1 elegível) é consumido; depois chega ALARM_EXPIRED(A1)
ENTÃO       EM_SÍNTESE e phase2_handoff publicado; a recusa fica só registrada, sem reenvio; o ALARM_EXPIRED não muda o ciclo
VERIFICAÇÃO (simulação D4.2) fsm_row == F16; to_state == EM_SÍNTESE; phase2_handoff == 1; entrada "MDC_TIME_REQUEST_FAILED"
            == 1, gravada no passo (9) (resultado do efeito — não é evento; nenhuma entrada com fsm_row F38/F20/F27 para
            ela); MARK_CONSUMED(A1) enviados == 1, inclusive depois de replay do livro; ALARM_EXPIRED(A1) ⇒ passo (4)
            "MDC_NOT_PHASE1_TRANSITION" (F27); estado == EM_SÍNTESE; dispatch_request(OPERACIONAL) == 1
```
Bloco cercado por ` ``` ` como os demais cenários. "M0" = Fixture M0 do Plan; nenhum número novo (CC-09).

### 2.11 `checks.md` (verificação) — ✔ ajustado

- **§5, item "Falha de cada capacidade com efeito (allowlist) tem caminho fechado na D5"** — vigente (trecho): `(5) \`time_request\` → \`TIME_REQUEST_FAILED\`/F38 → F20, e \`MARK_CONSUMED\` de ENC sem reenvio (T23 (c));` → **novo:** `(5) \`time_request\` → \`TIME_REQUEST_FAILED\`/F38 → F20; \`MARK_CONSUMED\` de ENC sem reenvio (T23 (c)); \`MARK_CONSUMED\` da F16 (ciclo já em \`EM_SÍNTESE\`) = resultado do efeito, só entrada \`MDC_TIME_REQUEST_FAILED\`, sem reenvio e sem F27 — desfecho aceito; a morte posterior do alarme cai em F27 (T24);` e, no fim do item, `Evidência: D5 F20/F33–F38 + notas (l.1032) ✔` → `Evidência: D5 F16/F20/F33–F38 + notas; D4.2 passo (3); RULE-MDC-003 (h); T24 ✔` *[antes: os dois trechos vigentes]*. Restrição explícita do ✔: ele cobre a falha **de cada efeito em cada linha de dono SPEC-008**, incluindo a F16; não cobre linhas de outro dono (F24–F26).
- **§0, F6** — `MARK_CONSUMED de ENC que falhe ⇒ sem reenvio` → `MARK_CONSUMED de ENC ou da F16 que falhe ⇒ sem reenvio`; coluna Locais: acrescentar `D4.2 (3); D5 F16; T24`.
- **§2, linha `MDC_TIME_REQUEST_FAILED` (novo R3)** — `T23 (a)–(c)` → `T23 (a)–(c); T24`. **Parágrafo da simulação** — depois de `T11 (b) → (4);` acrescentar `T24: recusa do \`MARK_CONSUMED\` da F16 = passo (9), não evento; \`ALARM_EXPIRED\` posterior → (4);`.
- **§4, matriz** — RULE-MDC-003, coluna D7: `+ T24`; RULE-MDC-010, coluna D7: `T14, T17` → `T14, T17, T24` (exceção de retomada — §2.1-bis; R1-m02); RULE-MDC-011, coluna D7: `T11` → `T11, T24`. **§2, linha `MDC_NOT_PHASE1_TRANSITION`** — `T11 (b)` → `T11 (b); T24` (R1-m03).

### 2.12 Contagens lidas sob a errata

`plan.md` Dimensionamento "23 Cenário-MDC (D7)"; título "## D7 — Cenários de Teste (23 — T01..T23; …)"; `checks.md` l.10 "**23** cenários D7"; `DHR-SPEC008-005` §2 "23 cenários" e ROADMAP "23 cenários" → **24 (T01..T24)** na v1.3 = v1.2 + esta errata. ADV continua **15** (ADV-12 ganha uma variante, sem ID novo). Na forma decidida (arquivo à parte — E-2) nenhum desses textos é editado *[antes: "Na forma B nenhum desses textos é editado"]*: a contagem vale lida sob a errata (como na errata v1.13 da SPEC-006). Atualizar ROADMAP/CATALOGO é da aplicação (Orquestrador), depois da homologação.

---

## 3. Condição 2 — R3-m05 [C05]: falha parcial na 2ª conferência da F01

### 3.0 Problema e decisão de desenho

`[FATO]` D4.1 SAÍDA: "`cycle_id` + abertura gravada + linha F01 de D5 (aplicada pela D4.2 passos (7)–(9): DUAS conferências por ação — PUBLISH_OWN do `dispatch_request` e TIME_REQUEST do `STAGE_TIMER` —, cada uma com a sua entrada e o seu `capability_check_ref`; qualquer uma falha ⇒ nenhum dos dois efeitos, F37)". `[FATO]` INV-MDC-01: "no pedido, nada é aberto; no meio do ciclo, o ciclo encerra sem efeito algum (D5, F37)". `[FATO]` D4.2 passo (7): "para CADA ação com efeito da linha, confere o registro de capacidades …, TODAS antes de qualquer efeito (INV-MDC-01) → falha ⇒ a linha NÃO é aplicada; evento interno `CAPABILITY_CHECK_FAILED` (F37)"; passo (8): "grava UMA entrada por efeito (antes dele)". `[FATO]` D5 F01: Estado "— (sem ciclo)", Próximo `AGUARDANDO`, Ação "abertura; despacha ESTRUTURAL; timer de etapa", Código `MDC_CYCLE_OPENED`; D5 F37: Estado "`AGUARDANDO`…`ATIVADO`". O parecer R3 (l.145) leu que o ciclo "já [está] aberto em AGUARDANDO"; o parecer R2 desta errata (R2-M1) mostrou que o Plan vigente não sustenta essa ordem. Nenhum ADV cobre o caso. *[antes: "`[INFERÊNCIA]` (parecer R3 l.145): quando a 2ª conferência falha, o ciclo já tem abertura gravada; o desfecho é F37 (já prescrito pela D4.1 SAÍDA), mas a frase da INV-MDC-01 pode ser lida como \"nada aberto\" e nenhum ADV cobre o caso."]*

**Decisão — seguir o plano homologado (Andraus, AskUserQuestion 2026-11-27, resposta ao R2-M1: opção (b) do parecer R2).** Esta errata **não** declara ordem de gravação nova e **não** altera D4.1, D4.2, D5 F01, RULE-MDC-001 nem BASpec-MDC-001. Ela: (i) acrescenta a variante **(d)** em ADV-MDC-12, exigindo só o que a D4.2 vigente garante (prevenção R3-m05: "todo caminho de falha novo tem variante em ADV ou frase no passo"); (ii) reconcilia **na fonte** (INV-MDC-01) a frase "no pedido, nada é aberto" só com o que a D4.1 SAÍDA já diz das conferências da F01; (iii) registra como **lacuna residual** o que o Plan vigente não define (§3.0-bis). Como INV-MDC-01 é a fonte única (D2), BASpec-MDC-012 ENTÃO e EC-MDC-008 FAILURE-MODE ("no meio do ciclo, ENC F37") **não** são editados. *[antes: "**Decisão:** (i) variante **(d)** em ADV-MDC-12 (…); (ii) reconciliar **na fonte** (INV-MDC-01) o sentido de \"pedido\" × \"meio do ciclo\", sem mudar comportamento; (iii) uma frase em D4.1 SAÍDA que torna explícita a ordem \"abertura gravada → conferências da F01\" (§3.1-bis; R1-m01). … passam a ler \"meio do ciclo\" com a definição da INV." — a ordem afirmada contradiz D4.2 (7)–(8) e D5 F01 (R2-M1)]*

### 3.0-bis Lacuna residual — o que o Plan vigente garante e o que fica em aberto

**Garantido pelo Plan vigente** `[FATO]`, sem esta errata:
1. Nenhum dos dois efeitos da F01 ocorre — nem despacho do ESTRUTURAL nem `STAGE_TIMER` (D4.1 SAÍDA: "qualquer uma falha ⇒ nenhum dos dois efeitos"; D4.2 (7): "TODAS antes de qualquer efeito").
2. A recusa é gravada no livro com `MDC_CAPABILITY_CHECK_FAILED`, sub `MDC_CAPABILITY_REGISTRY_UNAVAILABLE` (INV-MDC-01: "a recusa é gravada no livro de bordo (a escrita no próprio livro é fixa no componente, não vem do registro)"; D3.1).
3. Nenhum aviso (F37 "nem aviso"; EC-MDC-007 "registro de capacidades falho ⇒ nenhum aviso (F37)").
4. No `capability_audit_record` do runtime, nenhuma tentativa EXECUTED de `PUBLISH_OWN` nem de `TIME_REQUEST` (contrato lógico; predicados da trava).

**Não definido pelo Plan vigente** `[INFERÊNCIA]` — os textos admitem duas leituras:
- (L1) a linha F01 **não é aplicada** (D4.2 (7)): não há entrada `MDC_CYCLE_OPENED`, o ciclo não chega a `AGUARDANDO` e não há origem para F37 (o par "—" × `CAPABILITY_CHECK_FAILED` cairia em F29);
- (L2) a abertura já está gravada (D4.1 SAÍDA: "`cycle_id` + abertura gravada + linha F01 …"; BASpec-MDC-001 ENTÃO: "aceito ⇒ abertura gravada … e AGUARDANDO"), e F37 encerra a partir de `AGUARDANDO`.
Ficam em aberto, portanto: a existência da entrada `MDC_CYCLE_OPENED`; o `from_state` e o `fsm_row` da recusa (F37 ou nenhum); a gravação de `cycle_closed`; e se a chave (`asset`, `mission_id`) fica ocupada para a D4.1 passo (4) (`MDC_CYCLE_ALREADY_ACTIVE`). As duas leituras preservam a trava (nenhum efeito). O único risco observável `[INFERÊNCIA]` é uma leitura híbrida: abertura gravada **sem** `cycle_closed`, que deixaria a chave ocupada.

**Tratamento** `[DECISÃO NECESSÁRIA]` (Andraus): fica como **pendência para errata futura ou para a construção** (Tasks TK-02 avaliação do pedido e TK-08 tabela D5), o que vier primeiro — mesma via da ata `DHR-SPEC008-005` §3. A pendência é: escolher L1 ou L2 e reconciliar D4.1 SAÍDA, D4.2 (7)–(8), D5 F01/F37 e BASpec-MDC-001. Não é decisão aberta do ROADMAP, nenhuma é fechada (CONS-01) e nenhum ID novo é criado. Até lá, a construção não pode adotar a leitura híbrida.

*[antes (R2 desta errata, parágrafo "Âncora do estado de origem (R1-m01)"): "`[FATO]` BASpec-MDC-001 ENTÃO: … `[INFERÊNCIA]`: o pedido aceito pela D4.1 grava a abertura — entrada `MDC_CYCLE_OPENED`, `to_state` = `AGUARDANDO` — **antes** das duas conferências por ação da F01; … Logo, na variante (d), **a entrada `MDC_CYCLE_OPENED` existe** e F37 parte de `AGUARDANDO` (não F29 …). A frase do §3.1-bis põe essa ordem no texto da D4.1. Nenhuma linha de D5 muda." — ordem de gravação não sustentada pelo Plan vigente (R2-M1); retirada por decisão de Andraus (2026-11-27)]* *[antes: "`[INFERÊNCIA]` declarada (ponto para o Revisor): F37 parte de \"`AGUARDANDO`…`ATIVADO`\" (D5); com a abertura gravada pela D4.1 SAÍDA, o ciclo é tratado como em `AGUARDANDO` para aplicar F37 — leitura do parecer R3 l.145 (\"com o ciclo já aberto em AGUARDANDO. F37 serve\"). Nenhuma linha de D5 muda." — âncora só no parecer (R1-m01)]*

### 3.1 INV-MDC-01 — frase reconciliada

**Vigente (literal; quebra de linha do bloco indicada por "⏎"):** `em ambos, a ação não ocorre; no⏎            pedido, nada é aberto; no meio do ciclo, o ciclo encerra sem efeito algum (D5, F37);`

**Novo `[PROPOSTA]`:** `em ambos, a ação não ocorre; na avaliação do pedido (D4.1 passo (0)), nada é aberto; nas duas conferências da F01, nenhum dos efeitos da F01 ocorre (D4.1 SAÍDA; ADV-12 (d)); no meio do ciclo, o ciclo encerra sem efeito algum (D5, F37; ADV-12 (c)); *[antes: "em ambos, a ação não ocorre; no pedido, nada é aberto; no meio do ciclo, o ciclo encerra sem efeito algum (D5, F37);" — "pedido" ambíguo para a falha nas conferências da F01 (R3-m05)]*`

*[antes (R2 desta errata): "…; depois da abertura gravada — inclusive em qualquer das duas conferências da F01 (D4.1 SAÍDA) — e no meio do ciclo, o ciclo encerra sem efeito algum (D5, F37; ADV-12 (c)(d));" — pressupunha a ordem de gravação retirada (R2-M1)]*

Modalidade preservada: a trava continua fail-closed. A frase só repete, para as conferências da F01, o que a D4.1 SAÍDA já garante ("nenhum dos dois efeitos"); **não** diz se o ciclo foi aberto nem de que estado parte a recusa (lacuna §3.0-bis).

### 3.1-bis D4.1 — SAÍDA: **sem alteração** (retirado na R3)

A D4.1 SAÍDA fica como está no Plan vigente. *[antes (R2 desta errata): seção "3.1-bis D4.1 — SAÍDA (uma frase; R1-m01)", que propunha acrescentar a "qualquer uma falha ⇒ nenhum dos dois efeitos, F37), ou recusa." a frase "A abertura (entrada `MDC_CYCLE_OPENED`, `to_state` = `AGUARDANDO` — BASpec-MDC-001) é gravada ANTES dessas duas conferências e não depende delas (a escrita no próprio livro é fixa no componente — INV-MDC-01); por isso a falha de uma delas encerra por F37 a partir de `AGUARDANDO` (ADV-12 (d))." — ordem de gravação nova, contrária a D4.2 (7)–(8) e D5 F01 (R2-M1); retirada por decisão de Andraus, 2026-11-27: "Seguir o plano homologado"]*

### 3.2 ADV-MDC-12 — variante (d)

**Vigente (bloco, literal):**
```
DADO        M0, exceto: (a) K0 indisponível; (b) K0 contém credencial de emissão ao Bot Trade Finance; (c) K0 disponível na
            abertura e indisponível ao chegar E1 (antes do despacho do INSTITUCIONAL)
QUANDO      (a)(b) R1 chega; (c) E1 é processada
ENTÃO       nenhum efeito; recusa gravada; em (c) o ciclo encerra sem efeito algum
VERIFICAÇÃO "MDC_CAPABILITY_CHECK_FAILED", sub (a)(c) "MDC_CAPABILITY_REGISTRY_UNAVAILABLE", (b) "MDC_CAPABILITY_REGISTRY_DIVERGENT";
            capability_check_ref == AUSENTE em (a)(c); (a)(b) dispatch_request == 0; (c) fsm_row == F37,
            dispatch_request(INSTITUCIONAL) == 0, notice == 0, MARK_CONSUMED == 0
```
**Novo `[PROPOSTA]`:**
```
DADO        M0, exceto: (a) K0 indisponível; (b) K0 contém credencial de emissão ao Bot Trade Finance; (c) K0 disponível na
            abertura e indisponível ao chegar E1 (antes do despacho do INSTITUCIONAL); (d) K0 disponível na avaliação do
            pedido (D4.1 passo (0)) e na 1ª conferência da F01 (PUBLISH_OWN) e indisponível na 2ª (TIME_REQUEST do STAGE_TIMER)
QUANDO      (a)(b)(d) R1 chega; (c) E1 é processada
ENTÃO       nenhum efeito; recusa gravada; em (c) o ciclo encerra sem efeito algum; em (d) nenhum dos efeitos da F01 ocorre
VERIFICAÇÃO "MDC_CAPABILITY_CHECK_FAILED", sub (a)(c)(d) "MDC_CAPABILITY_REGISTRY_UNAVAILABLE", (b) "MDC_CAPABILITY_REGISTRY_DIVERGENT";
            capability_check_ref == AUSENTE em (a)(c) e na 2ª conferência de (d); (a)(b) dispatch_request == 0; (c) fsm_row == F37,
            dispatch_request(INSTITUCIONAL) == 0, notice == 0, MARK_CONSUMED == 0; (d) recusa gravada no livro (INV-MDC-01;
            D4.2 (7)), dispatch_request(ESTRUTURAL) == 0, STAGE_TIMER == 0, #(capability_audit_record: PUBLISH_OWN ∧ EXECUTED)
            == 0, #(capability_audit_record: TIME_REQUEST ∧ EXECUTED) == 0, notice == 0; em (d) NÃO verificados (lacuna da
            errata v1.3 §3.0-bis): fsm_row, from_state, entrada de abertura do ciclo e cycle_closed
*[antes: o bloco vigente acima — variante (d) acrescentada (R3-m05)]*
```
*[antes (R2 desta errata, ENTÃO e linhas de (d)): "ENTÃO       nenhum efeito; recusa gravada; em (c)(d) o ciclo encerra sem efeito algum" e "(d) entrada MDC_CYCLE_OPENED == 1 (to_state == AGUARDANDO — D4.1 SAÍDA; BASpec-MDC-001), depois fsm_row == F37 com from_state == AGUARDANDO, dispatch_request(ESTRUTURAL) == 0, STAGE_TIMER == 0, #(capability_audit_record: PUBLISH_OWN ∧ EXECUTED) == 0, notice == 0" — exigia ordem de gravação que o Plan vigente não define (R2-M1)]*
*[antes (R1 desta errata, linhas de (d)): "(d) cycle_id ≠ AUSENTE (abertura gravada — D4.1 SAÍDA), fsm_row == F37, dispatch_request(ESTRUTURAL) == 0, STAGE_TIMER == 0, #(capability_audit_record: PUBLISH_OWN ∧ EXECUTED) == 0, notice == 0" — estado de origem não observável (R1-m01)]*

### 3.3 Propagação (contagem de variantes e definição)

- D3.1, linha `MDC_CAPABILITY_CHECK_FAILED` — vigente: `| nenhum efeito (pedido: nada aberto; meio do ciclo: ENC F37) | INV-MDC-01 | ADV-12 (a)–(c) |` → novo: `| nenhum efeito (pedido: nada aberto; conferências da F01: nenhum efeito da F01; meio do ciclo: ENC F37) | INV-MDC-01 | ADV-12 (a)–(d) |` *[antes: trecho vigente]* *[antes (R2 desta errata): "(pedido: nada aberto; depois da abertura — inclusive F01 — e meio do ciclo: ENC F37)" (R2-M1)]*.
- BASpec-MDC-012 DADO — `ADV-12 (a)–(c)` → `ADV-12 (a)–(d)` *[antes: "ADV-12 (a)–(c)"]*.
- §7-bis Bloco A, linha 012 — `registro cai no meio do ciclo → ADV-12 (c)` → `registro cai no meio do ciclo ou entre as conferências da F01 → ADV-12 (c)(d)` *[antes: trecho vigente]*.
- `checks.md` §2: linha `MDC_CAPABILITY_CHECK_FAILED` (2 subs) `ADV-12 (a)–(c)` → `ADV-12 (a)–(d)`; simulação `ADV-06 (a) e ADV-12 (c) → (7).` → `ADV-06 (a) e ADV-12 (c)(d) → (7).`

---

## 4. Condição 3 — R3-m07 [C01]: enum `notice.kind` e destinatário

### 4.0 Prova de completude (Grep, 2026-11-27) — tabela fato → locais

Grep em `specs/features/SPEC-008/` e em `governance/MMC-001_Manager_Contract.md` pelos padrões pedidos: `notice.kind`, `CAPABILITY`, `Andraus/Fase 0`, `to = `, e também `STOP`, `notice`, `aviso|avisa|escalada`, `Fase 0`.

**Fato A — valores de `notice.kind`.** Quem emite `notice` hoje `[FATO]` (D5 e regras): F20 (`LIMIT_COUNTER_EXCEEDED`, "aviso" → LIMIT), F35 (ROUNDS, "aviso" → LIMIT), F21 ("aviso + escalada" → COST), RULE-MDC-004 (d) (ruptura → RUPTURE). F37: "nenhum efeito (nem `MARK_CONSUMED`, nem aviso)"; EC-007 FAILURE-MODE: "registro de capacidades falho ⇒ nenhum aviso (F37)"; ADV-12 (c): `notice == 0`. F22/F23 (STOP): ações "em `ATIVADO`: `MARK_CONSUMED`" e "—", **sem aviso**; RULE-MDC-009 (d) e T20 não pedem aviso. Logo **CAPABILITY** e **STOP** não têm linha emissora `[INFERÊNCIA]`.

| Ocorrência | Local | Tratamento |
|---|---|---|
| `kind ∈ {LIMIT, COST, RUPTURE, CAPABILITY, STOP}` | contrato lógico, linha `notice` (l.1115) | **altera** (§4.1) |
| `Enviar notice (LIMIT, COST, RUPTURE, CAPABILITY, STOP)` | EC-MDC-007 CAPABILITY (l.1619) | **altera** (§4.2) |
| `notice.kind == LIMIT` | T15 VERIFICAÇÃO (l.1278) | mantém (valor segue no enum) |
| `notice.kind == COST` | T16 VERIFICAÇÃO (l.1287) | mantém |
| `notice.kind == RUPTURE` | T18 VERIFICAÇÃO (l.1305) | mantém o kind; acrescenta `notice.to` (§4.5) |
| `notice.kind == LIMIT` (texto v1.0) | `HISTORICO.md` l.91 | histórico — não tocado (INV-07) |
| `CAPABILITY   :` (rótulo de campo do Enforcement Contract) | EC-MDC-001..009 (9 ocorrências) | não é valor de enum — não tocado |
| `MDC_CAPABILITY_CHECK_FAILED`, `CAPABILITY_CHECK_FAILED`, `MDC_CAPABILITY_REGISTRY_*` | D3.1, D4.1, D4.2, D5 F37, ADV-12, EC-008 | código/evento, não kind — não tocado |
| `STOP` em "encerramento por STOP" | BASpec-MDC-009 CRITÉRIO (l.894) | ENC, não aviso — não tocado |
| `STOP` (texto R1) | `HISTORICO.md` l.43 | histórico — não tocado |
| tipos de aviso | `MMC-001` | 0 ocorrências de `notice`; nada herdado sobre kinds |

**Fato B — destinatário do `notice`.**

| Ocorrência | Local | Tratamento |
|---|---|---|
| `to = Andraus` | contrato `notice` (l.1115) — única ocorrência de `notice.to`; as outras 10 de "to = " no `plan.md` são final de palavra ("contexto = ", "conflito = ", "encerramento = ", "custo = ", "desalinhamento = ", "incerto = ") | mantém |
| "(6) ENVIAR `notice` (aviso/escalada) a Andraus pelo canal local" | INV-MDC-01 allowlist (l.334) — **fonte** do destinatário (Classe C, E3, lista fechada) | mantém |
| "NOTICE_LOCAL (6: a Andraus pelo canal local)"; "(destino interno ao SOT / Andraus)" | contrato `capability_audit_record` (l.1097–1098, l.1103) | mantém |
| "aviso + escalada a Andraus" · "Escalada a Andraus = `notice`" · "ENC + aviso a Andraus" · "`notice` a Andraus" · "Aviso e escalada a Andraus"/"Aviso a Andraus" · "avisar Andraus" | RULE-MDC-008 (c); RULE-MDC-009 (c); T15 ENTÃO; Métricas; EC-007 título/EFFECT; EC-008 CAPABILITY | já "Andraus" — não tocados |
| "aviso a ⏎ Andraus/Fase 0" | RULE-MDC-004 (d) (l.463–464) | **altera** (§4.3) |
| "avisar Andraus/Fase 0" | EARS 5 (l.657) | **altera** (§4.4) |
| "aviso a Andraus/Fase 0" | T18 ENTÃO (l.1304) | **altera** (§4.5) |
| "ciclo novo pedido por Andraus/Fase 0" | RULE-MDC-005 (e) (l.503) | origem de **pedido de ciclo**, não `notice` — não tocado |
| "pede orientações a Andraus/Fase 0" | Interface, requisito T-4 à Spec de Tempo (l.1058) | pré-aviso WF-K02 da **Spec de Tempo**, não `notice` desta Spec — não tocado |
| "ruptura ⇒ registro + aviso"; "ruptura com aviso" | BASpec-MDC-004 ENTÃO/VERIFICADO (l.784, l.796) | sem destinatário — não tocado |
| "abrir ou não ciclo após aviso de ruptura" | Requisitos a outras Specs, item SPEC-015 (l.1070) | **altera** (§4.6): recebe o requisito novo que a RULE-MDC-004 (d) delega à SPEC-015 (R1-m07) *[antes: "coerente — não tocado"]* |
| "Fase 0" (demais 11 linhas: l.13, 214, 215, 257, 290, 369, 653, 719, 977, 1529, 1788) | cabeçalho, Herança, WORKFLOW, origem do pedido, decisões abertas | não tratam de destinatário de aviso — não tocados |
| "avisa Andraus/Fase 0" | `DHR-SPEC008-004` §1, DN-2 (ata homologada) | fonte — não tocada; leitura em §4.3 e E-3 |
| `checks.md` | só "(6) `notice` → `MDC_NOTICE_PENDING`" (§5) e F13 (T15/T16/T18) — sem kind nem destinatário | não tocado |

Conclusão `[INFERÊNCIA]`: depois da errata, nenhum local do Plan nomeia valor de kind sem linha emissora nem destinatário de `notice` diferente de "Andraus"; os únicos "Andraus/Fase 0" que ficam (l.503, l.1058) não são destinatário de `notice`; o requisito à SPEC-015 que a nova RULE-MDC-004 (d) cria está listado em "Requisitos a outras Specs" (§4.6).

### 4.0-bis Decisão de desenho

- **Enum — `kind` = {LIMIT, COST, RUPTURE}; STOP retirado (decidido por Andraus em 2026-11-27, E-4):** derivar `kind` das linhas que avisam (prevenção R3-m07: "enum e destinatário derivados da allowlist"; aqui, das linhas que exercem a capacidade (6)). Tornar `CAPABILITY` alcançável exigiria avisar quando o registro de capacidades falhou — contraria F37/ADV-12 (fail-closed: "nenhum efeito") `[INFERÊNCIA]`. **STOP** não estava no achado; entra porque a mesma prova (Fato A) mostra que também é inalcançável. *[antes: "…retirar é o mínimo; mantê-lo exigiria acrescentar \"aviso\" à F22 (comportamento novo) — escolha em E-4."]*
- **Destinatário — só Andraus; Fase 0 por remissão à SPEC-015 (decidido por Andraus em 2026-11-27, E-3):** fica **`to = Andraus`** (allowlist (6) da INV-MDC-01, Classe C/E3 — lista fechada). As três frases "Andraus/Fase 0" passam a "Andraus", com a menção à Fase 0 preservada como **remissão à SPEC-015** (a Fase 0 não existe ainda; RULE-MDC-001 (b) já a trata como "SPEC-015, quando existir"); o requisito correspondente vai a "Requisitos a outras Specs" (§4.6). DN-2 em si ("a Fase 1 só detecta e avisa; não abre ciclo") não muda. *[antes: "Alternativa (acrescentar Fase 0 como destinatário) muda a lista fechada da trava E3 e o enum CAP `NOTICE_LOCAL` — mais invasiva (§6, Major). Como a frase de DN-2 na ata diz \"avisa Andraus/Fase 0\", a leitura é submetida a Andraus (E-3) `[DECISÃO NECESSÁRIA]`; …"]*

### 4.1 Contrato lógico — linha `notice`

**Vigente:** `notice          : {cycle_id | —, kind ∈ {LIMIT, COST, RUPTURE, CAPABILITY, STOP}, code, refs[], to = Andraus}`
**Novo `[PROPOSTA]`:**
```
notice          : {cycle_id | —, kind ∈ {LIMIT, COST, RUPTURE}, code, refs[], to = Andraus}   — kind 1:1 com as linhas que
                   avisam (LIMIT: F20, F35; COST: F21; RUPTURE: RULE-MDC-004 (d)); F37 nunca avisa; to = allowlist (6)
                   *[antes: "kind ∈ {LIMIT, COST, RUPTURE, CAPABILITY, STOP}" — CAPABILITY e STOP sem linha emissora (R3-m07)]*
```

### 4.2 EC-MDC-007 — CAPABILITY

**Vigente:** `CAPABILITY   : Enviar notice (LIMIT, COST, RUPTURE, CAPABILITY, STOP) pelo canal local`
**Novo `[PROPOSTA]`:** `CAPABILITY   : Enviar notice (LIMIT, COST, RUPTURE) a Andraus pelo canal local *[antes: "Enviar notice (LIMIT, COST, RUPTURE, CAPABILITY, STOP) pelo canal local"]*`

### 4.3 RULE-MDC-004 (d)

**Vigente (literal):** `REFUTED ou SUPERSEDED (transições do CHM-001) ⇒ entrada \`MDC_DOMINANT_RUPTURE_DETECTED\` + aviso a⏎                Andraus/Fase 0 com ativo e referência da hipótese (EC-MDC-007).`
**Novo `[PROPOSTA]`:** `REFUTED ou SUPERSEDED (transições do CHM-001) ⇒ entrada \`MDC_DOMINANT_RUPTURE_DETECTED\` + aviso a Andraus (\`notice.to\` = Andraus, canal local — capacidade (6) de INV-MDC-01) com ativo e referência da hipótese (EC-MDC-007); a Fase 0 (SPEC-015, quando existir) toma conhecimento da ruptura pelo meio que a SPEC-015 definir — esta Spec não ganha destinatário nem capacidade (DN-2: "avisa Andraus/Fase 0", DHR-SPEC008-004 §1). *[antes: "… + aviso a Andraus/Fase 0 com ativo e referência da hipótese (EC-MDC-007)." — destinatário divergente do contrato \`to = Andraus\` (R3-m07)]*`

### 4.4 EARS 5

**Vigente (trecho):** `o Manager-Fase-1 DEVE registrar a ruptura e avisar Andraus/Fase 0, e NÃO DEVE abrir ciclo por conta própria`
**Novo `[PROPOSTA]`:** `o Manager-Fase-1 DEVE registrar a ruptura e avisar Andraus (destinatário do \`notice\` — INV-MDC-01 (6); Fase 0 conforme RULE-MDC-004 (d)), e NÃO DEVE abrir ciclo por conta própria *[antes: "…e avisar Andraus/Fase 0, e NÃO DEVE…"]*` — DEVE/NÃO DEVE preservados (RULE-SEM-03).

### 4.5 Cenário-MDC-T18

- ENTÃO, **vigente:** `ENTÃO       ruptura registrada e aviso a Andraus/Fase 0; nenhum ciclo aberto pela Fase 1` → **novo:** `ENTÃO       ruptura registrada e aviso a Andraus; nenhum ciclo aberto pela Fase 1` *[antes: "…aviso a Andraus/Fase 0; …"]*
- VERIFICAÇÃO, **vigente (trecho):** `notice.kind == RUPTURE com asset == XAU e ref H7` → **novo:** `notice.kind == RUPTURE, notice.to == Andraus, com asset == XAU e ref H7` *[antes: "notice.kind == RUPTURE com asset == XAU e ref H7"]*

### 4.6 "Requisitos a outras Specs" — item SPEC-015 (R1-m07)

A nova RULE-MDC-004 (d) (§4.3) delega à SPEC-015 o meio pelo qual a Fase 0 toma conhecimento da ruptura; o requisito entra na seção própria no mesmo passo (prevenção R1-m07).

**Vigente (trecho literal):** `**SPEC-015:** origem dos pedidos; quantas vezes tentar (P-12, \`[PROPOSTA]\` do MMC-001 §8.2-bis); abrir ou não ciclo após aviso de ruptura (DN-2: a Fase 1 só avisa).`
**Novo `[PROPOSTA]`:** `**SPEC-015:** origem dos pedidos; quantas vezes tentar (P-12, \`[PROPOSTA]\` do MMC-001 §8.2-bis); abrir ou não ciclo após aviso de ruptura (DN-2: a Fase 1 só avisa); meio pelo qual a Fase 0 toma conhecimento da ruptura — o \`notice\` desta Spec vai só a Andraus (RULE-MDC-004 (d); INV-MDC-01 (6)); qualquer outro meio é da SPEC-015, sem capacidade nova na Fase 1. *[antes: "…abrir ou não ciclo após aviso de ruptura (DN-2: a Fase 1 só avisa)."]*`

Etiqueta: requisito `[INFERÊNCIA]`, como os demais da seção; não fecha SPEC-015-SCOPE (segue ABERTA — CONS-01).

---

## 5. Condição 4 — R3-m08 [C06]: `HISTORICO.md`, R2 → R3

`HISTORICO.md` é histórico, não norma (cabeçalho do próprio arquivo); a proposta é **acrescentar** três linhas ao fim da tabela "R2 → R3 (v1.1 → v1.2)", antes da linha "| — | Itens e medida |", sem alterar as existentes (INV-07).

### 5.1 De onde vem o texto anterior (v1.1)

- `[FATO]` `DIFF-PLAN-V1.0-ATUAL-2026-11-14.patch` = "git diff v1.0 → atual" (`HISTORICO.md`, Complemento R2-m10); as linhas `+` são o texto do arquivo no momento da geração.
- `[INFERÊNCIA]` esse "atual" é a **v1.1** (commit `366af09`): as linhas `+` não trazem nenhum texto novo da FICHA-M do R2 (ex.: l.267 do patch traz `ID de uma RULE — ex.:`, texto **antigo** do R2-m08a; não há "`ARMADO` sem disparo" do R2-m04a) nem nada da v1.2 (`T23`, `TIME_REQUEST_FAILED`, `failures[TEMPO]`: 0 ocorrências no patch). Risco residual: sem `git show 366af09:…` (o Especificador não tem Bash) não se prova que nenhuma edição ocorreu entre o commit e a geração do patch; o Orquestrador pode conferir com `git show 366af09:specs/features/SPEC-008/plan.md`.
- `[FATO]` blocos do `DELTA-…-366af09-44e6131f.txt` são seções por cabeçalho `##`–`####`, cada uma até o próximo cabeçalho (`scripts/spec_delta.py`, função `blocos`, l.33–51), comparadas por sha256 do texto com espaços normalizados.

### 5.2 Linhas propostas `[PROPOSTA]`

```
| R2-M-02 (T23) | BASpec-MDC-003 VERIFICADO POR — DADO e VERIFICAÇÃO | DADO: "T01 · T14 · T15 (b)(c) · T22 (a)(b) · ADV-01 (aviso duplicado) · ADV-02 (retomada) · ADV-03 (outro ciclo) · ADV-04 (sem envelope)"; VERIFICAÇÃO: "ver T01 / T14 / T15 / T22 / ADV-01..04" (linhas `+` do `DIFF-PLAN-V1.0-ATUAL-2026-11-14.patch`, l.337–338 e l.343 = v1.1) | T23 (falha de `time_request`) acrescentado a DADO e VERIFICAÇÃO; ENTÃO inalterado na R2→R3 (a troca da última linha do ENTÃO é Pós-R3, R3-m03) |
| — (T22) | Cenário-MDC-T22 | conteúdo v1.1 (patch l.561–573) **idêntico** ao da v1.2: nenhuma palavra trocada | o DELTA o marca "alterado" porque, na v1.1, o bloco de T22 ia até "## D8" e incluía o separador "---"; na v1.2, T23 entrou logo depois e o "---" passou a fechar o bloco de T23 (`spec_delta.py` `blocos`, l.33–51) — conferido pelo Orquestrador por `git show 366af09` (2026-11-27): conteúdo idêntico, só a fronteira do bloco mudou |
| R2-m04, m05 (parte), m08, m09, m11 (classe M) | edições do Orquestrador entre a v1.1 e a v1.2 (plan.md e checks.md) | texto anterior **literal** = campo `"antigo"` de cada entrada do bloco `<!-- FICHA-M … -->` do parecer R2 (`governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-PLAN-R2-2026-11-14.md`, entradas R2-m04a/b, m05a/b/c, m08a/b, m09a/b, m11a/b); classificação "aplicado_m" (R2-m04, m08, m09, m11; R2-m05 = "desenho", com entradas a/b/c na FICHA-M) em `governance/propostas/SPEC-008/FICHA-ESQUELETO-PLAN-R2.json` (só natureza, sem texto) | aplicadas pelo Orquestrador (classe M), fora das linhas acima; R2-m05b e R2-m05c têm também linha própria nesta tabela (R2-m05; R2-m06 TRACE-06) |
```

### 5.3 O que não consegui recuperar (dito, não inventado)

- **Prova por git** de que as linhas `+` do patch são exatamente a v1.1 do commit `366af09` — só indícios (§5.1).
- **A mudança de T22** além do separador: não encontrei diferença de conteúdo; se o `git show` mostrar outra, a linha "— (T22)" deve ser trocada pelo texto real.
- **Demais blocos que o DELTA marca como alterados** (35) **não** foram reconciliados um a um com o HISTORICO: fora da condição 4 (que pede BASpec-003, T22 e o ponteiro à FICHA-M). Indício `[INFERÊNCIA]`: BASpec-MDC-010 e D9 aparecem como alterados pelo R2-m11a/b (FICHA-M; "Por que este agente analítico rodou agora", plan l.908 e l.1519), já cobertos pela linha de ponteiro.

---

## 6. Compatibilidade (RULE-HG-04) — Minor, decidida por Andraus em 2026-11-27 (E-1) *[antes: "— `[PROPOSTA]`; escolha de Andraus"]*

`[FATO]` CR-001 §7.7 (l.437–441): **Patch** = "Correções exclusivamente editoriais (ortografia, formatação, referências cruzadas, notas sem efeito normativo)" — "Não altera a versão"; **Minor** = "Mudanças compatíveis que adicionam comportamento sem invalidar comportamento anterior" — "Incremento Minor (ex.: 1.0 → 1.1)"; **Major** = "Mudanças que removem, invalidam ou alteram comportamento normativo vigente" — "Nova baseline major". CRR55 (l.450): Minor preserva a validade dos identificadores vigentes; CRR56 (l.451): quebra só como Major declarada.

**Análise de impacto** `[INFERÊNCIA]`: schemas — nenhum (Grep em `schemas/`: 0 ocorrências de `notice`, `MDC_`, `SPEC-008`); RAG — nenhum; Skills — nenhuma; testes — `tests/test_fsm_check.py` (l.95) e `tests/test_cenario_precondicao.py` (l.56) **leem** o `plan.md` da SPEC-008 (tabela D5 e cenários): na forma decidida (arquivo à parte) o arquivo só ganha o ponteiro no Status — rodar a suíte depois de aplicar (Orquestrador) *[antes: "na forma B o arquivo não muda; na forma A a célula da F16 e o T24 entram na leitura desses testes — rodar a suíte depois de aplicar (Orquestrador)"]*; modelos canônicos — nenhum (CEM/CHM/CCM/CEE intocados, CC-02); dependentes — Spec de Tempo, SPEC-009/014/015 ainda sem Plan; não há BUILD.

| Parte | Leitura |
|---|---|
| C1 (R3-m04) | declara o desfecho de um caminho sem desfecho e acrescenta T24 → **adiciona** comportamento verificável; o observável antigo ("sem reenvio") continua; nada invalidado. **Exceções nomeadas declaradas** (R1-m02): RULE-MDC-003 (h)/D4.2 (3) passam a incluir a F16; RULE-MDC-010 (b)/BASpec-MDC-010 deixam de reemitir, na retomada, o `MARK_CONSUMED` de ENC/F16 com recusa já gravada. A 2ª estreita a regra geral de reemissão só num caso em que a reemissão contradiria o "sem reenvio" já vigente (T23 (c)); nenhum caminho alcançável que antes reemitia com sucesso deixa de fazê-lo `[INFERÊNCIA]` — por isso não é tratada como quebra (CRR56) |
| C2 (R3-m05) | ADV-12 (d) novo, exigindo só o que a D4.1 SAÍDA e a D4.2 (7) vigentes garantem (recusa gravada; nenhum efeito da F01; nenhum aviso) → **adiciona** obrigação verificável, sem mudar desfecho; frase da INV só repete a D4.1 SAÍDA; nenhuma ordem de gravação nova (R2-M1); lacuna residual registrada, não resolvida (§3.0-bis) *[antes: "ADV-12 (d) novo; frase da INV alinhada à D4.1 SAÍDA vigente (F37) → adiciona cenário, sem mudar desfecho"]* |
| C3 (R3-m07) | retira do enum dois valores **sem linha emissora** (nenhum comportamento alcançável removido); alinha três frases ao destinatário que a trava E3 já fixava (`to = Andraus`); acrescenta um requisito `[INFERÊNCIA]` à SPEC-015 (§4.6) |
| C4 (R3-m08) | só histórico (não-norma) → editorial |

- **Patch — não se aplica** `[INFERÊNCIA]`: T24 e ADV-12 (d) são obrigações verificáveis novas (não "exclusivamente editoriais").
- **Reavaliação na R3 (R2-M1)** `[INFERÊNCIA]`: continua **Minor**. Retirar a ordem de gravação (§3.1-bis) tira desta errata a única mudança que alteraria comportamento vigente (estado inicial da FSM). T24 e ADV-12 (d) continuam sendo obrigações verificáveis novas, e ADV-12 (d) agora exige só o que o Plan vigente já garante. A lacuna §3.0-bis não muda nada: ela só fica registrada.
- **Minor — decidida por Andraus em 2026-11-27 (E-1)**: Plan **v1.2 → v1.3** (v1.3 = v1.2 + esta errata, como a "errata v1.13" da SPEC-006). Nenhum identificador vigente perde validade (CRR55): T01–T23, ADV-01–15 e EC-001–009 seguem verificáveis; T18 só ganha uma verificação. Minor se sustenta com E-3 = só Andraus (destinatário que a trava E3 já fixava) e E-4 = retirar STOP (valor sem linha emissora) — ambas decididas por Andraus na mesma data (parecer R1, ponto prioritário (4)). *[antes: "**Minor — recomendada**: …; T18 só ganha uma verificação." e o item "**Major — hipótese registrada**: (i) se Andraus ler \"avisar Andraus/Fase 0\" (EARS 5, vigente) como obrigação de avisar a Fase 0 … → Major (CRR56); (ii) se Andraus escolher acrescentar a Fase 0 como destinatário (E-3 (b)) … → Major. …" — hipóteses sem uso depois de E-1/E-3]*

---

## 7. Forma de aplicação e dimensionamento

- **Forma — arquivo à parte + ponteiro (decidida por Andraus em 2026-11-27, E-2):** esta errata vira arquivo à parte (sugestão: `specs/features/SPEC-008/errata-v1.3 (arquivo a criar na homologação)`, nome final na aplicação) + ponteiro de uma linha no Status do `plan.md` ("Errata v1.3 aditiva: `errata-v1.3.md` (DHR-…); lê-se o Plan sob ela") e, opcionalmente, no "Objeto" do `checks.md`. Precedente: `DHR-SPEC006-005` D2 (l.19): "nenhuma regra/BASpec/EARS/EC/T/ADV/contagem alterada" no texto baselined.
- **Dimensionamento (RULE-ECC-07):** o corpo do `plan.md` não muda de tamanho (só o ponteiro, na célula de Status). *[antes: item "**Forma A (no lugar):** as mesmas trocas do §2–§4 com `[antes]` (INV-07). Estimativa `[INFERÊNCIA]`: +~18 linhas de corpo … ⇒ ≈ 1.903 linhas, **acima do alerta de 1.900** … Na forma B o corpo do `plan.md` não muda de tamanho." — alternativa sem uso depois de E-2]*
- Em qualquer forma, o Orquestrador deve conferir, antes de aplicar, que os trechos "vigentes" citados aqui ainda existem literalmente (hash do `plan.md` na ata: `21a52c6b…`).

---

## 8. O que a homologação desta errata NÃO afirma

- Não reabre o Plan nem a homologação `DHR-SPEC008-005`; não muda nenhuma outra condição de conformidade da ata §4.
- Não fecha decisão aberta (CONS-01): **J-001, N-001, G-001, M-001**, K-001, C-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4, BL-026, P-13, **DN-1**, P-11 (parte fractal) e θ seguem abertas. DN-2 segue como decidida ("só detecta e avisa"); a errata não decide **como** a Fase 0 receberá a ruptura (SPEC-015).
- Não especifica a Spec de Tempo: T-9/T-10 e WF-A02 são só citados; a errata não exige da Spec de Tempo nada além do que a Interface já pede.
- Não decide nada pela SPEC-014: o fato de o alarme poder terminar `EXPIRED`/`CANCELLED` (e não `CONSUMED`) depois de um handoff (C1) fica como **observação** para a abertura dela.
- Não define o que acontece na falha parcial da 2ª conferência da F01 além do que o Plan vigente já garante: a existência da entrada de abertura, o estado de origem (`fsm_row`/`from_state`), o `cycle_closed` e a ocupação da chave (`asset`, `mission_id`) ficam como lacuna residual `[DECISÃO NECESSÁRIA]`, para errata futura ou para a construção (§3.0-bis). Esta errata não altera D4.1, D4.2, D5 F01/F37, RULE-MDC-001 nem BASpec-MDC-001 (decisão de Andraus, 2026-11-27).
- Não prova que as linhas `+` do patch são a v1.1 exata (§5.3) nem reconcilia os 35 blocos do DELTA.
- Não foi revisada pelo Revisor; nenhum script rodou (sem Bash): `validate_spec_sot.py` não se aplica a este arquivo; `check_refs.py`, `build_map.py --check` e `check_dimensionamento.py` ficam com o Orquestrador.
- Não muda versão, ROADMAP, CATALOGO nem RPSA por si: isso é da aplicação, depois da homologação (com E-1/E-2 já decididas por Andraus). As respostas de Andraus de 2026-11-27 (E-1..E-5) fixam o texto desta proposta; **não** são a homologação da errata.

---

## 9. Decisões de Andraus sobre esta errata (AskUserQuestion, 2026-11-27, repassadas pelo Orquestrador)

As cinco foram respondidas por Andraus; fixam o texto da proposta. A homologação da errata continua pendente (Status = PROPOSTA; INV-09). *[antes: título "## 9. Pendências de Andraus — `[DECISÃO NECESSÁRIA]` (nada decidido aqui)"]*

| # | Ponto | Estado | Justificativa (mantida da R1) |
|---|---|---|---|
| E-1 | Compatibilidade | **Minor (v1.2 → v1.3) — decidida por Andraus em 2026-11-27** | §6; Patch não cabe (T24 e ADV-12 (d) são obrigações novas) |
| E-2 | Forma | **Arquivo à parte + ponteiro — decidida por Andraus em 2026-11-27** | §7; a troca no lugar passaria do alerta de 1.900 linhas (estimativa) |
| E-3 | Destinatário do aviso de ruptura | **Só Andraus (`to = Andraus`); Fase 0 por remissão à SPEC-015 — decidida por Andraus em 2026-11-27** | a trava E3 (INV-MDC-01 (6)) já fixava Andraus; acrescentar a Fase 0 mudaria a lista fechada (Major) |
| E-4 | `STOP` no enum | **Retirar (kind = LIMIT, COST, RUPTURE) — decidida por Andraus em 2026-11-27** | sem linha emissora (§4.0, Fato A); mantê-lo exigiria aviso novo na F22 |
| E-5 | R3-m04 | **Opção (b) desfecho aceito + T24 — decidida por Andraus em 2026-11-27** | §2.0; a opção (a) criaria guarda/memória nova e poderia perder setup válido |

*[antes (colunas "Opções (recomendada primeiro)"): E-1 "**Minor** (v1.3) · Major (v2.0)"; E-2 "**B — arquivo à parte + ponteiro** · A — no lugar"; E-3 "**(a) `to = Andraus`; Fase 0 por remissão à SPEC-015** · (b) acrescentar Fase 0 à allowlist (6) e a `to`"; E-4 "**retirar** (sem linha emissora) · manter e acrescentar \"aviso\" à F22 (comportamento novo)"; E-5 "**(b) desfecho aceito** · (a) ordem (confirmação antes da transição)"]*

---

## 10. Autopré-check (curto)

- [x] ROADMAP.md (SPEC-008 v1.2 BASELINE, 4 condições; decisões abertas) e atomic-spec.md consultados; ata `DHR-SPEC008-005` §3–§4, parecer R3 (l.144–148), plan/checks/HISTORICO, patch, DELTA, FICHA-M R2 e `DHR-SPEC008-004` lidos.
- [x] Uma seção por condição, com decisão de desenho justificada e mínima; alvos por ID de bloco + trecho literal.
- [x] Texto vigente citado literalmente; texto novo com `[antes: …]` (INV-07); nada aplicado (INV-09).
- [x] Sem estado, seta, evento, código, campo de contrato ou linha de D5 novos; WF-F02 intacto; IDs novos só T24 e a variante ADV-12 (d).
- [x] C01 (recorrente): tabela fato → locais por Grep para `notice.kind`, `CAPABILITY`, `Andraus/Fase 0`, `to = ` (e `STOP`, `Fase 0`, aviso); propagação a EARS/BASpec/D3.1/checks listada em cada condição.
- [x] RULE-SEM-03: DEVE/NÃO DEVE preservados em EARS 3 e EARS 5; DN-2 não reescrita.
- [x] CONS-01: J-001, N-001, G-001, M-001 (e demais) seguem abertas (§8).
- [x] Compatibilidade contra CR-001 l.437–451 literal; Patch não cabe; Minor (decidida por Andraus, E-1); exceções nomeadas (RULE-MDC-003 (h), RULE-MDC-010 (b)) declaradas no §1, §2.0 e §6 (R1-m02).
- [x] R2: R1-m01 (tratado na R2 e **revisto na R3** pelo R2-M1 — ver item abaixo); R1-m02 *[antes: "R1-m01 (âncora BASpec-MDC-001 + D4.1 SAÍDA; frase §3.1-bis; `from_state == AGUARDANDO` e `MDC_CYCLE_OPENED` em ADV-12 (d));"]* (exceção nomeada em RULE-MDC-010 (b) e BASpec-MDC-010); R1-m07 (requisito à SPEC-015, §4.6; tabela §4.0 corrigida). R1-m03..m06 do Orquestrador intocados.
- [x] R3: **R2-M1** fechado pela decisão de Andraus (2026-11-27, "Seguir o plano homologado"). Feito: §3.1-bis retirado com `[antes]`; nenhuma ordem de gravação nova; D4.1, D4.2, D5 F01/F37, RULE-MDC-001 e BASpec-MDC-001 não tocados; ADV-12 (d) verifica só recusa gravada, nenhum efeito da F01 e nenhum aviso; INV-MDC-01 e D3.1 repetem a D4.1 SAÍDA; a lacuna residual fica em §3.0-bis (`[DECISÃO NECESSÁRIA]`, sem ID novo, nenhuma decisão aberta fechada). **R2-m01:** coluna Código da F16 sem `MDC_TIME_REQUEST_FAILED` é intencional (§2.3). **R2-m02:** §1 atualizado (subcódigos, alvos não tocados); compatibilidade reavaliada e mantida como Minor (§6).
- [x] Prova de coerência (Grep no texto desta errata por `MDC_CYCLE_OPENED`, `AGUARDANDO`, `F01`, `F37`, `3.1-bis`): as ocorrências fora de `[antes]` estão em três grupos. (1) §3.0 e §3.0-bis citam o Plan vigente (D4.2 (7)–(8), D5 F01/F37, BASpec-MDC-001) e descrevem as leituras L1/L2 como lacuna. (2) INV-MDC-01, ADV-12 (d) e D3.1 dizem só "nenhum efeito da F01" ou declaram `fsm_row`/`from_state`/abertura como NÃO verificados. (3) Os usos de F37 são de ADV-12 (c), da D5 e do enum `notice`. Nenhum texto novo afirma que `MDC_CYCLE_OPENED`/`AGUARDANDO` são gravados antes das conferências da F01.
- [x] R3-m08: o que não foi possível recuperar está dito (§5.3); nenhum texto anterior inventado.
- [ ] Gates mecânicos (`check_refs.py`, `build_map.py --check`, `check_dimensionamento.py`, conferência dos trechos vigentes por hash) — com o Orquestrador (sem Bash).

**Pronto para revisão.**
