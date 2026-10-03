# SPEC-038 — Trading Analysis Tool Harness (Plan)

| Campo | Valor |
|---|---|
| ID | SPEC-038 — Trading Analysis Tool Harness (Trilha B — tooling de domínio) |
| Versão | 1.0 (Plan candidato — aguarda Revisor + homologação de Andraus) |
| Status | **PLAN CANDIDATO — NÃO é baseline** (INV-09). Abertura HOMOLOGADA (DHR-SPEC038-001, 2026-10-03); este é o próximo gate. |
| Fonte | `specs/features/SPEC-038/ABERTURA.md` + `research.md` + `sources/` (homologados, DHR-SPEC038-001); ROADMAP §17/§22/§23; atomic-spec.md **v1.5**; WORKFLOW.md v2.1; DHR-DEC-003; DHR-DEC-004 |
| Complexidade | **HIGH** |
| Profundidade-alvo | **D0–D7** (profile **standard**, AGENTS.md §4) — com reforço adversarial D8 (≥1 caso) para o gate de maturidade L3 (atomic-spec §7) |
| Profile (Claude Code) | standard (HIGH) — §7-bis (EUA-E18) aplicado nesta redação (Blocos A/B/C/D) |
| Posição no caminho crítico | **Paralela/fora de ordem** — aberta por decisão direta de Andraus (RULE-ECC-01); não substitui nem adia a SPEC-004 (próximo trabalho da ordem regular) [FONTE: DHR-SPEC038-001 §1] |
| Nível de maturidade-alvo | **L3 Testável** na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) [FONTE: ABERTURA.md §1] |
| Classe predominante (orientação, não vinculante — atomic-spec §10.6) | **D + C** — declaração normativa é por BASpec (CC-11) |
| Regime normativo citado | **RULE-ECC-01/02/04/05** (Especificação Emergente + Captura Verbatim + Multi-Lente); **RULE-MECH-01..04** (Classe/Mecanismo — incide); **ENF-01..08**; **CC-01..CC-12** |
| Método | atomic-spec.md **v1.5** |
| Autor | Especificador Principal SOT (Claude Code, Opus 4.8) |
| Data | 2026-10-03 |

**Restatement para o gate determinístico (prose redundante proposital):**
Status: PLAN CANDIDATO — NÃO é baseline (aguarda Revisor + homologação de Andraus). Complexidade: HIGH. Profundidade-alvo: D0–D7 (standard). Maturidade-alvo: L3.

> **Status epistemológico desta entrega.** O Plan é **FATO ARQUITETURAL candidato a baseline**; a abertura (número/nome/fronteira HIGH·D0–D7/quantidade=1/Classe D+C/CC-12 N/A) já é **FATO NORMATIVO** (DHR-SPEC038-001). Documentado ≠ homologado (TRACE-06). Nada neste Plan vira baseline sem homologação de Andraus (INV-09).

---

## Nota de gate (passo 11-bis / RMR-001) — itens verificados nesta redação

[FONTE: ROADMAP §23 passo 11-bis; RMR-001; DHR-DEC-003; DHR-DEC-004]

- **BL-017** (`tool correctness ↔ SPEC-038`) — **ATIVADO** (DHR-DEC-004 §1.1). O gatilho `spec:SPEC-038 em redação` disparou. A emenda à SPEC-020 que fecha a dimensão B "tool correctness" só ocorre **na homologação da SPEC-038** (não neste Plan — CONS-01). Proposta de texto da emenda em §"Plano de re-apontamento" como `[PROPOSTA]`, não aplicada.
- **BL-031** (`spec:SPEC-038 em redação`) — **Absorvido** (DHR-DEC-003 §1.1). Viabilidade por canal tratada no `research.md`; decisão de canal tomada por Andraus. Nada novo neste Plan além de referência.
- **BL-033** (MASTER — Market Data & Order Flow) — **Em espera** (DHR-DEC-004 §1.3); capacidade/slot indicativo **sem número de Spec**; D-001..D-027 **ABERTAS**. Fora do escopo desta Spec; o `TradingViewAdapter` é previsto aqui como adapter de *uma* fonte, sem acoplar o contrato ao MASTER.
- **BL-034** (observabilidade de agentes) — **Em espera** [INFERÊNCIA — coerente com RMR-001]; a *política* de logs é SPEC-040; este Plan só exige os eventos/estados da chamada de ferramenta como requisito de contrato (ver TH-013).
- **BL-032** (dona do backtest/calibração) — **Em espera**; dona = SPEC-018 (DHR-DEC-003 §1.2). Esta Spec é pré-requisito instrumental, não a dona.
- Nenhum item `ATIVADO` novo é disparado pela redação deste Plan além de BL-017 (já promovido por Andraus). [INFERÊNCIA]

---

## Constitution Check (CC-01..CC-12 — atomic-spec §10.5 + emendas)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** SPEC-038 é harness de **ferramentas**, agnóstico de escola; serve Observação/dado bruto a qualquer escola e **não** cria, ordena nem reinterpreta hipótese estrutural. A hierarquia Elliott→…→ICT é **protegida, não tocada** (INV-01/INV-02). [INFERÊNCIA] [FONTE: ABERTURA.md §7]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** o dado de ferramenta é **Observation** no vocabulário do CEM-001 (l.303–305 "o que foi observado"), **nunca** Evidência/Interpretation (CEM-001 l.145/l.282/l.307). A proveniência projeta-se sobre o campo **Lineage** do CEM-001 (l.351–354: `PRIMARY` → Lineage vazia) **por referência**, sem redefinir o modelo. Nenhuma seção altera estrutura de CEM/CHM/CCM. [FONTE: CONST-01; CEM-001]
- [x] **CC-03 — Conviction Vector não tocado; J-001 permanece ABERTA (pendente):** esta Spec não computa, consome nem referencia convicção; dimensionalidade=8 intocada; nenhum limiar numérico de convicção é declarado. J-001 (fórmula/pesos/limiares definitivos) permanece **em aberto** [DECISÃO NECESSÁRIA] — não fechada nem tocada. [FONTE: INV-03]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma das 5+5 violada; esta Spec não produz Signal Package nem sinal; o **custo** da ferramenta (campo do contrato) **nunca** entra em convicção (INV-04). [FONTE: CEE-001 v2.0]
- [x] **CC-05 — Complexidade declarada:** **HIGH, D0–D7** (com D8 de reforço para L3).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card; campos tornam-se obrigatórios na fase de Tasks/BUILD (adiada — atomic-spec §14). Omissão justificada, mesmo tratamento de SPEC-019/020/021/046.
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06). Rastreabilidade de origem: ROADMAP §17 (slot) → BL-031 (viabilidade) → `research.md`/`ABERTURA.md` homologados (DHR-SPEC038-001) → DHR-DEC-003/004 → este Plan.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** **presente** (seção própria abaixo); INHERITS/ADDED preenchidos com ID+versão; REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02); evidência de satisfação por obrigação herdada no §7-bis Bloco B. Eixo VERTICAL (RULE-HV): **não aplicável** — SPEC-038 não é decomposição micro de macro-Spec homologado (linha paralela nova).
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI-01..03):** aplicado — distinção FATO NORMATIVO / FATO ARQUITETURAL / PROPOSTA / INFERÊNCIA / [EXTERNO] / [DECISÃO NECESSÁRIA] explícita; dado de barra em formação e latência da candidata = **INDETERMINADO**, nunca fabricados; nenhuma conformidade jurídica afirmada; sem falsa precisão (contagem de ferramentas = INDETERMINADO, research.md §5.7).
- [x] **CC-10 — Terminologia concorrente (RULE-SEM):** **N/A quanto a escola de mercado**. Aplicada a termos técnicos decisivos: **Observação** (ferramenta/Skill, CEM-001) vs. **Evidência** (agente, INV-06); "indicador/dado derivado" vs. "evidência"; "barra fechada/confirmada" vs. "barra em formação/repaint". Acepções declaradas no D1/D2.
- [x] **CC-11 — Classe/Mecanismo por BASpec (RULE-MECH-01, §10.6):** **INCIDE** — esta Spec cita RULE-MECH-01 no próprio texto (ver D2). Cada BASpec com efeito declara Classe (D/H/P/C), critério 4Es, bounded loop/gate de saída onde H; Classe C compatível com E2/E3 (risco alto — RULE-MECH-02). Classe predominante (orientação): **D + C**.
- [x] **CC-12 — Princípios de Domínio (RULE-PD-01, §10.7):** **NÃO incide** — SPEC-038 não define escopo de especialidade de escola (Elliott/SMC/ICT); é tooling agnóstico (determinação análoga à SPEC-046 e SPEC-002). Nenhum `PD-xx` proposto. A Classe (CC-11) é declarada; CC-12 fica N/A por ausência de domínio de especialidade. [FONTE: ABERTURA.md §6]

**Checklist de consistência principiológica (GPR-001 §15):** PC-02 (SOT não executa) reforçada — a ferramenta **observa/captura**, nunca executa ordem (INV-05; `replay_trade` proibido — TH-009); 4Es na ordem (Eficácia > Efetividade > Eficiência > Economicidade — critério explícito por BASpec); rastreabilidade (cada leitura gera proveniência auditável); preservação da incerteza (barra em formação / dado faltante → INDETERMINADO, nunca zero/fabricado — RULE-UNC/RULE-PRB/RULE-MET). Item CLASSE-MECH-001: cada BASpec com efeito declara Classe. Item PRINC-BID-001: N/A (CC-12).

**Disciplinas cognitivas N8–N17 incidentes:** RULE-EPI (dado não revalidado/não-confirmado não é fato), RULE-MET-01 (não-fabricação — latência/limites não informados = INDETERMINADO, nunca inventados), RULE-CAU-01 (nenhuma afirmação causal sem mecanismo; esta Spec não faz afirmação causal de mercado), RULE-UNC-01/03 (incerteza localizada; não converter incerteza em probabilidade), RULE-DEC (a ferramenta relata/observa; quem decide é o agente/Andraus — decisão≠execução).

---

## §7-bis — Autopré-check de Redução de Viés (obrigatório HIGH/CRITICAL — EUA-E18)

Executado DEPOIS do Constitution Check e ANTES da submissão ao Revisor. Propósito: identificar o que a Spec poderia ter errado.

### Bloco A — Pergunta adversarial por BASpec (D8 aplicado)

Aplicado às BASpecs com maior carga (HIGH/Classe C):

- **TH-001 (contrato por-ferramenta completo):** "Se estivesse errada, o que seria observável?" → uma ferramenta admitida/usada sem um dos 10 campos do contrato — verificável por inspeção do catálogo. "O ENTÃO é verificável por observador independente?" → sim: presença dos 10 campos é binária. "QUANDO satisfeito mas ENTÃO não deve ocorrer?" → ferramenta de infraestrutura puramente interna sem efeito de mercado nem Observação → fora do escopo (D1); não force o contrato onde não há tipologia (a), (b), (c), (d) — tratado como limitação.
- **TH-005 (teto Observação→não-Evidência):** negação = um dado de ferramenta é promovido direto a Evidência sem agente+lineage → viola INV-06; caso de negação em ADV-TH-02.
- **TH-008 (gate de confirmação p/ efeito):** negação = operação de efeito (`pine_set_source`, compilar, `draw_*`, `indicator_add`, `alert_create`, kill do app) executa sem confirmação explícita registrada → ADV-TH-03 (fail-closed).
- **TH-009 (proibição de ordem/`replay_trade`):** negação = qualquer geração/roteamento de ordem ou `replay_trade` → viola INV-05; ADV-TH-04 (fail-closed E3).
- **TH-003 (barra em formação = INDETERMINADO):** negação = valor de barra não fechada entra como fato/determinístico → contamina a cadeia; ADV-TH-01.
- **TH-010 (TradingViewAdapter nunca fonte única):** negação = o contrato acopla-se ao TradingView como fonte única da verdade → viola DHR-DEC-004 §1.2; ADV-TH-05.

Todas as três perguntas foram respondíveis com âncora de fonte; nenhuma BASpec restou como [DECISÃO NECESSÁRIA] por falta de resposta.

### Bloco B — Herança obrigação-a-obrigação (CC-08)

Obrigações herdadas e evidência de satisfação:
1. **CEM-001 (Observation ≠ Evidence/Interpretation; Lineage de PRIMARY vazia):** satisfeita em TH-005/TH-002 e no D1 — a ferramenta produz Observation; promoção a Evidência exige agente+lineage (fora desta Spec, SPEC-002). Nenhuma redefinição (RULE-HD-02).
2. **SPEC-002 (padrão de provenance operacional / Observação→Evidência sob governança):** satisfeita em TH-002 (campos de proveniência por leitura) e na fronteira §"Fronteiras"; SPEC-038 **fornece** a Observação; a promoção/rotulagem de qualidade de Evidência é da SPEC-002. Não suprimida (RULE-HD-03).
3. **WORKFLOW.md v2.1 (WF-C03, WF-K02, WF-A01/A03, WF-V01/V02, WF-02/03/05):** citados por ID, não contraditos; WF-D03 não fechada. Satisfação: TH-003 (WF-C03 INDETERMINADO), TH-011/TH-013 (latência declarada vs. WF-K02 — INDETERMINADO quando não informada), TH-008 (marcação/alarme = análise, não ordem — WF-A01, INV-05).
4. **DHR-DEC-003/004 (perfil exploratório; risco ToS assumido; TradingView uma das fontes via adapter; provedor de máquina não escolhido):** satisfeita em TH-007/TH-008/TH-009/TH-010 e nos Riscos R-1.
Nenhuma obrigação herdada removida ou enfraquecida; nenhuma contradição vertical detectada.

### Bloco C — Verificação epistêmica (RULE-EPI-01..03 / CC-09)

- Nenhuma afirmação causal de mercado é feita (a Spec é agnóstica de escola) — RULE-CAU-01 não gera obrigação de mecanismo aqui.
- Nenhuma hipótese tratada como fato: "canal lícito", "latência suficiente", "conformidade ToS" permanecem [DECISÃO NECESSÁRIA]/INDETERMINADO.
- Incerteza material usa **INDETERMINADO** (latência/limites da candidata, contagem de ferramentas, conformidade do MCP oficial) em vez de PASS/FAIL ou número fabricado (RULE-MET-01/RULE-PRB-02).
- Nenhuma probabilidade declarada sem evento bem-formado (RULE-PRB-01) — a Spec não usa métrica probabilística.
- Nenhuma precisão numérica sem base — nenhum limiar de convicção/qualidade é inventado.

### Bloco D — reforço de escopo (reconfirma §7 vigente)

- A Spec **não executa** ordem nem produz TMP/Signal Package (INV-05 / RULE-DEC-01) — produz Observação/dado — reconfirmado.
- Nenhuma BASpec cruza a fronteira SOT→execução downstream (TH-009 proíbe ordem/`replay_trade`).
- Toda dependência de decisão de Andraus está marcada [DECISÃO NECESSÁRIA] e não como fato (SPEC-038-DATASRC-001 no recorte decidido por DHR-DEC-004; escolha de provedor de máquina ABERTA).

---

## Herança / Delta (§8.3 — EUA-E04)

```
HERANÇA / DELTA — SPEC-038

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO — RULE-HD-04):
  - Método: atomic-spec.md v1.5 — BASpec/EARS/Enforcement/Classe D/H/P/C/D0-D9/F.1-F.4/TRACE-06
  - Canônico: CEM-001 (baseline) — Observation ("o que foi observado", l.303-305) ≠ Evidence/
      Interpretation (l.145/l.282/l.307); Lineage de PRIMARY = [] (l.351-354). INV-06/INV-10.
  - Spec baselined: SPEC-002 v1.x (Evidence & Evidence Provenance Harness, DHR-SPEC002-001) —
      padrão de provenance operacional e governança Observação→Evidência, reusado por referência.
  - Setup operacional soberano: WORKFLOW.md v2.1 — WF-02/03/05, WF-K02, WF-A01/A03, WF-C03,
      WF-V01/V02 (conformar-se; citar por ID; não contradizer; não fechar WF-D03 — DHR-WF-001).
  - Decisões de Andraus: DHR-DEC-003 (perfil exploratório CDP; risco ToS assumido; MCP oficial a
      reavaliar; 6 candidatas não adotadas; ECC-VAL-001 fechada) + DHR-DEC-004 (BL-017 ATIVADO;
      DATASRC-001 decidida no recorte: TradingView uma das fontes via adapter; provedor de máquina
      não escolhido; BL-033/MASTER referência externa não-normativa).
  - Governança do Harness: RULE-ECC-01/02/04/05, RULE-MECH-01..04, ENF-01..08, CC-01..CC-12.
  - Invariantes: INV-05 (SOT não executa), INV-06 (Evidência≠Observação), INV-09 (sem baseline
      informal), TRACE-06 (etiquetagem), CONS-01 (decisão aberta não vira invariante fechado).

ADDED (delta local — o que este Plan acrescenta):
  - Contrato por-ferramenta (molde de 10 campos) como unidade do harness (TH-001).
  - Tipologia de ferramenta (dados OHLCV/volume, indicador/derivado, marcação/desenho, replay,
      Pine) instanciando o molde.
  - Campos de Proveniência por leitura e de Proveniência de backtest (TH-002/TH-013).
  - Determinismo (barra fechada vs. em formação) como campo de 1ª classe (TH-003).
  - Perfil "exploratório-supervisionado" (modo ∈ {somente-leitura default, efeito-confirmado}),
      gates de confirmação para ferramentas de efeito, proibição dura de ordem/replay (TH-007/08/09).
  - TradingViewAdapter como adapter de UMA fonte sobre provider abstrato (TH-010).
  - Mapeamento ao schemas/elliott-wave.input.json (unix s → ISO-8601 UTC) (TH-011).
  - Quatro ferramentas Pine com Classe declarada C/C/D/D-C (TH-012).
  - Eventos/estados de observabilidade da chamada de ferramenta REQUESTED→…→UNKNOWN como
      requisito de contrato (TH-013) — política de logs em SPEC-040/BL-034.
  - 6 Enforcement Contracts (EC-TH-01..06); D4/D5/D7/D8; I/O schemas.

MODIFIED (especialização de regra herdada):
  - (nenhuma — o contrato por-ferramenta é camada operacional SOBRE CEM-001/SPEC-002, sem alterar
    a substância normativa herdada; RULE-HD-02 preservada.)

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança:** eixo VERTICAL (RULE-HV) **não aplicável** — SPEC-038 não decompõe nenhum macro-Spec homologado; é linha de trabalho nova e paralela. [INFERÊNCIA — a confirmar pelo Revisor]

---

## D0 — Missão (Intenção)

O Trading Analysis Tool Harness especifica **como cada ferramenta de análise de mercado declara, por contrato, o que produz e sob que garantias**, de modo que o dado que ela entrega entre na cadeia cognitiva do SOT **sempre como Observação verificável e proveniente** — nunca como Evidência, decisão ou ordem. O harness fixa o molde `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas` para toda ferramenta (dados OHLCV/volume, indicadores/derivados, marcação/desenho no gráfico, replay/histórico, e as ferramentas Pine), e impõe que dado não-confirmado, faltante ou de proveniência corrompida seja tratado como `INDETERMINADO` e nunca fabricado. [FONTE: ROADMAP §17; ABERTURA.md §1/§2]

A Spec **não** define *política* de seleção/fallback/tool poisoning (SPEC-039), guardrails de runtime (SPEC-042), detecção de alucinação (SPEC-044), *política* de observabilidade/logs (SPEC-040), nem backtest/calibração (SPEC-018). Especifica o **contrato de ferramenta/dado** que esses slots consomem.

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| Item | Descrição | Fonte |
|---|---|---|
| Contrato por-ferramenta | Molde de 10 campos, uma instância por ferramenta/capacidade | ROADMAP §17; ABERTURA.md §2 |
| Tipologia de ferramenta | (a) dados de mercado (OHLCV, volume/order-flow); (b) indicadores/dados derivados; (c) marcação/desenho no gráfico; (d) replay/histórico; (e) ferramentas Pine (injetar, compilar, ler Strategy Tester, alterar entradas) | ABERTURA.md §2/§4-ter |
| Determinismo e proveniência como campos de 1ª classe | Barra fechada/confirmada (determinística) vs. em formação (não-determinística/repaint); proveniência verificável por leitura | research.md §3.3; ABERTURA.md §4-bis.2 |
| O dado de ferramenta é Observação, não Evidência | Fronteira `Fonte → Dado/Observação → (Agente) → Evidência` | INV-06; CEM-001 |
| Perfil exploratório-supervisionado + gates de confirmação | Modo somente-leitura por padrão; efeito só com confirmação explícita registrada | DHR-DEC-003 §1.1 |
| TradingViewAdapter sobre provider abstrato | TradingView = uma fonte via adapter, nunca fonte única | DHR-DEC-004 §1.2 |
| Falhas como contrato | Ferramenta indisponível, dado faltante/ruim, API instável, latência fora de SLA → fail-safe declarado; nenhuma fabricação | ABERTURA.md §2; RULE-MET-01 |
| Eventos/estados da chamada de ferramenta | REQUESTED→…→UNKNOWN como requisito de contrato (não a política de logs) | Ref. "Uso de Logs"; ROADMAP §18 |

### Fora do escopo (Non-goals explícitos) — "o que SPEC-038 NÃO é"

| Item | Pertence a | Justificativa |
|---|---|---|
| *Política* de seleção/preferência/fallback/tool poisoning/resultado contraditório | **SPEC-039** | É o slot vizinho (ROADMAP §17) |
| Allow/deny/gates de execução em runtime | **SPEC-042** | Guardrails runtime |
| Detecção de alucinação/afirmação sem fonte | **SPEC-044** | — |
| *Política* de observabilidade/logging (schema de trace/span, retenção, correlação) | **SPEC-040** / BL-034 | SPEC-038 só exige os eventos/estados como requisito de contrato |
| Execução de ordem / qualquer efeito de mercado | fora do SOT / família RISK | **INV-05** (SOT não executa; `replay_trade` proibido) |
| Fórmula/pesos/limiares de convicção; qualquer cálculo de Conviction Vector | SPEC-003/CCM-001 (baselined) / backtest | **J-001/N-001 ABERTAS**; INV-03/INV-04 |
| Backtest/calibração da J-001 (dona e protocolo) | **SPEC-018** (via BL-032) | SPEC-038 só dá o contrato de ferramenta/dado |
| Storage físico do dado/Observação (Blackboard/KG) | SPEC-004/006 | **M-001/H-001 ABERTAS** |
| Escolha do provedor de dados de máquina (order flow/futuros/multi-exchange) | Discovery do MASTER / BL-033 | **ABERTA** (DHR-DEC-004 §1.3; D-001..D-027 ABERTAS) |
| Skills analíticas que *consomem* os dados | SPEC-025+ | — |
| Conformidade jurídica com Termos de Uso do TradingView | — | **Não** é parecer jurídico; risco ASSUMIDO por Andraus (DHR-DEC-003 §1.1) |

---

## Princípios de Domínio (§10.7 — PRINC-BID-001)

**N/A (CC-12 não incide).** SPEC-038 é tooling agnóstico de escola; nenhum `PD-xx` é proposto. [FONTE: ABERTURA.md §6]

---

## D2 — Regras

```
RULE-TH-001: Toda ferramenta de análise admitida no harness DEVE declarar um contrato completo com
             os 10 campos (Finalidade, Input, Output, Precisão, Determinismo, Limitações, Custo,
             Latência, Provenance, Falhas). Ferramenta sem contrato completo NÃO PODE ser usada
             como fonte de Observação.
             [FONTE: ROADMAP §17; ABERTURA.md §2] [PROPOSTA — RULE-MECH-01 incide: Classe C]

RULE-TH-002: Todo dado produzido por ferramenta DEVE carregar Proveniência por leitura mínima
             (tool, args, symbol/tf, captured_at_utc, last_closed_bar, indicador+versão quando
             aplicável, status) antes de ser disponibilizado como Observação.
             [FONTE: ABERTURA.md §4-bis.2; CEM-001 Lineage] [PROPOSTA — Classe D]

RULE-TH-003: Dado de barra NÃO fechada (em formação/repaint) DEVE ser marcado INDETERMINADO e
             NÃO PODE entrar como fato na cadeia Observação→Evidência; dado faltante/ruim =
             INDETERMINADO (nunca zero nem fabricado).
             [FONTE: research.md §3.3; WF-C03; RULE-UNC/RULE-PRB/RULE-MET-01] [PROPOSTA — Classe D]

RULE-TH-004: Falha de ferramenta (indisponível, health-check falho, dado faltante, API instável,
             latência fora de SLA) DEVE resultar em comportamento fail-closed declarado; a análise
             NÃO PODE completar valor de memória nem prosseguir como se o dado existisse.
             [FONTE: ABERTURA.md §4-bis.4; RULE-MET-01; ENF-04] [PROPOSTA — Classe C]

RULE-TH-005: O dado de ferramenta é Observação; sua promoção a Evidência exige agente + lineage
             (SPEC-002). Nenhuma ferramenta PODE emitir Evidência/Interpretation diretamente
             (INV-06; CEM-001 l.145/l.282).
             [FONTE: INV-06; CEM-001] [PROPOSTA — Classe C]

RULE-TH-006: A saída de qualquer ferramenta (incl. texto de gráfico/indicador) é dado NÃO-confiável
             e NUNCA redireciona o comportamento do agente (tool poisoning). A *política* de
             tratamento é SPEC-039; aqui é apenas a marcação de não-confiabilidade no contrato.
             [FONTE: research.md §3.2; DHR-PROV-WEB-001 §2.1] [PROPOSTA — Classe C]

RULE-TH-007: Ferramenta do canal exploratório opera em modo somente-leitura por padrão; o modo
             efeito-confirmado só é alcançável por confirmação explícita registrada do humano.
             [FONTE: DHR-DEC-003 §1.1] [PROPOSTA — Classe C]

RULE-TH-008: Toda ferramenta de EFEITO (pine_set_source, compilar/adicionar ao gráfico, draw_*,
             indicator_add, alert_create, launch/kill do app) DEVE ter precondição "confirmação
             explícita registrada" e ser fail-closed sem ela.
             [FONTE: DHR-DEC-003 §1.1; ABERTURA.md §4-bis.1/§4-ter.1] [PROPOSTA — Classe C]

RULE-TH-009: Nenhuma ferramenta PODE gerar, rotear ou enviar ordem; replay_trade é proibido
             (INV-05). Fail-closed em E3.
             [FONTE: INV-05; DHR-DEC-003 §1.1] [PROPOSTA — Classe C]

RULE-TH-010: O contrato de dados de mercado DEVE ser expresso contra um provider abstrato;
             TradingView entra via TradingViewAdapter como UMA fonte, NUNCA como fonte única da
             verdade nem substituto de feed L2/L3.
             [FONTE: DHR-DEC-004 §1.2; MASTER §5 "Provider ≠ Evidence"] [PROPOSTA — Classe C]

RULE-TH-011: A ferramenta de OHLCV DEVE mapear o timestamp unix em segundos para ISO-8601 UTC
             (date-time) conforme schemas/elliott-wave.input.json; símbolos restritos ao enum
             {BTCUSDT, XAUUSD, NAS100}; timeframes {S1,D1,H4,H1,M5}.
             [FONTE: schemas/elliott-wave.input.json; ABERTURA.md §4-bis.2] [PROPOSTA — Classe D]

RULE-TH-012: Toda invocação de ferramenta DEVE expor os estados REQUESTED→EXECUTED→
             {OK|FAILED|STALE|INDETERMINADO|UNKNOWN} como requisito de contrato de observabilidade;
             a *política* de logs/trace é SPEC-040/BL-034.
             [FONTE: ref. "Uso de Logs"; ROADMAP §18] [PROPOSTA — Classe D]
```

---

## Critérios de Aceitação (EARS)

Notação EARS ("Quando <condição>, o componente DEVE <resposta>"):

1. Quando uma ferramenta é admitida no harness sem um dos 10 campos do contrato, o componente DEVE recusar seu uso como fonte de Observação.
2. Quando uma ferramenta produz um dado de mercado, o componente DEVE anexar a Proveniência por leitura antes de disponibilizá-lo como Observação.
3. Quando o dado recebido corresponde a uma barra em formação (não fechada), o componente DEVE marcá-lo INDETERMINADO e não o tratar como fato.
4. Quando a ferramenta está indisponível ou o dado está faltante/ruim, o componente DEVE falhar fechado e nunca completar o valor de memória.
5. Quando um dado de ferramenta é recebido, o componente DEVE tratá-lo como Observação e não o DEVE promover a Evidência sem agente + lineage.
6. Quando uma ferramenta de efeito (draw_*, indicator_add, alert_create, pine_set_source, compilar/adicionar ao gráfico, kill do app) é invocada, o componente DEVE exigir confirmação explícita registrada antes de executar.
7. Quando qualquer componente solicita geração ou roteamento de ordem, ou invoca replay_trade, o componente DEVE rejeitar a operação (INV-05).
8. Quando o contrato de dados de mercado é instanciado, o componente DEVE expressá-lo contra um provider abstrato, com TradingView como uma fonte via adapter e nunca como fonte única.
9. Quando a ferramenta de OHLCV entrega candles, o componente DEVE converter o timestamp unix em segundos para ISO-8601 UTC conforme o schema do Elliott.
10. Quando uma ferramenta é invocada, o componente DEVE registrar os estados REQUESTED→EXECUTED→{OK|FAILED|STALE|INDETERMINADO|UNKNOWN} como requisito de contrato.

---

## D3 — Comportamento (BASpecs) — Classe declarada (RULE-MECH-01, CC-11)

### BASpec-TH-001 — Contrato por-ferramenta completo (gate de admissão)

```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement — gate de admissão que verifica a presença dos 10 campos do contrato;
                ferramenta sem contrato completo é barrada (não é julgamento do LLM)
CRITÉRIO 4Es  : Eficácia — uma ferramenta sem contrato de Determinismo/Provenance contamina toda a
                cadeia Observação→Evidência; a completude é condição de confiança (risco alto → C,
                RULE-MECH-02). Economicidade não rebaixa.
GATE DE SAÍDA : checagem determinística de presença dos 10 campos (ENF-03)

BASpec-TH-001:
  QUANDO:       uma ferramenta de análise (tipo a/b/c/d/e do D1) é admitida ou invocada no harness
  ENTÃO:        o sistema verifica a presença dos 10 campos do contrato (Finalidade, Input, Output,
                Precisão, Determinismo, Limitações, Custo, Latência, Provenance, Falhas); se algum
                faltar → ferramenta NÃO autorizada como fonte de Observação (fail-closed)
  PORQUE:       RULE-TH-001 — contrato completo é condição de confiança da Observação
  REFERÊNCIA:   RULE-TH-001; ROADMAP §17; EC-TH-01
  VERIFICADO POR:
    DADO        uma ferramenta de indicador sem o campo Determinismo preenchido
    QUANDO      ela é admitida no catálogo do harness
    ENTÃO       o gate recusa a admissão como fonte de Observação
    VERIFICAÇÃO nenhuma Observação é aceita de ferramenta com contrato incompleto
```

### BASpec-TH-002 — Proveniência por leitura

```
CLASSE        : D (Determinístico)
MECANISMO     : captura de campos de proveniência (código puro) anexados ao dado lido
CRITÉRIO 4Es  : Eficácia — sem proveniência a Observação não é auditável nem reconstruível (P13)

BASpec-TH-002:
  QUANDO:       uma ferramenta produz um dado de mercado/indicador/desenho
  ENTÃO:        o sistema anexa a Proveniência por leitura: {tool, args, symbol, tf,
                captured_at_utc, last_closed_bar, indicator+versão (quando aplicável),
                status ∈ {OK|FAILED|STALE|INDETERMINADO|UNKNOWN}}; projeção sobre o Lineage do
                CEM-001 (Observation, não Interpretation)
  PORQUE:       RULE-TH-002 — Observação precisa ser verificável quanto a origem/momento
  REFERÊNCIA:   RULE-TH-002; CEM-001 l.303-305/l.351-354; EC-TH-02
  VERIFICADO POR:
    DADO        data_get_ohlcv retorna candles de BTCUSDT/H4
    QUANDO      o dado é disponibilizado como Observação
    ENTÃO       cada registro carrega captured_at_utc + last_closed_bar + status
    VERIFICAÇÃO nenhum dado é disponibilizado sem os campos mínimos de proveniência
```

### BASpec-TH-003 — Determinismo: barra em formação = INDETERMINADO

```
CLASSE        : D (Determinístico)
MECANISMO     : comparação determinística entre o timestamp do candle e o fechamento da barra;
                barra não fechada → status INDETERMINADO, descartada do fato
CRITÉRIO 4Es  : Eficácia — dado não-reprodutível (repaint) invalida a cadeia; Economicidade jamais
                rebaixa a marcação

BASpec-TH-003:
  QUANDO:       a ferramenta entrega um candle/valor de indicador cuja barra ainda não fechou
                (em formação) ou cujo dado está faltante/ruim
  ENTÃO:        o sistema marca o dado INDETERMINADO, não o trata como fato, e trabalha da última
                barra FECHADA para trás; nunca preenche com zero nem valor de memória
  PORQUE:       RULE-TH-003; WF-C03 (order flow faltante = INDETERMINADO); RULE-UNC/RULE-PRB/RULE-MET-01
  REFERÊNCIA:   RULE-TH-003; research.md §3.3; WF-C03
  VERIFICADO POR:
    DADO        o último candle de H4 ainda está em formação (barra atual)
    QUANDO      data_get_ohlcv entrega a série incluindo essa barra
    ENTÃO       a barra atual é marcada INDETERMINADO; a penúltima (fechada) é a mais recente usável
    VERIFICAÇÃO nenhuma Observação FECHADA é derivada de barra em formação
```

### BASpec-TH-004 — Fail-closed em falha de ferramenta

```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement — ausência de health-check/dado válido interrompe a cadeia (gate)
CRITÉRIO 4Es  : Eficácia — prosseguir com dado inexistente fabrica realidade (RULE-MET-01); risco
                alto → C
GATE DE SAÍDA : verificação determinística de disponibilidade/validade do dado (ENF-03)

BASpec-TH-004:
  QUANDO:       a ferramenta está indisponível, o health-check falha, o dado está faltante/ruim ou
                a latência excede o SLA declarado
  ENTÃO:        o sistema falha fechado: a análise PARA para aquela Observação; status FAILED/STALE/
                UNKNOWN registrado; nunca completa preço/valor de memória
  PORQUE:       RULE-TH-004; ENF-04 (fail-closed); RULE-MET-01 (não-fabricação)
  REFERÊNCIA:   RULE-TH-004; ABERTURA.md §4-bis.4; EC-TH-02
  VERIFICADO POR:
    DADO        o canal CDP está fora do ar (health-check falha)
    QUANDO      um agente solicita OHLCV
    ENTÃO       status = FAILED; nenhuma Observação é fabricada; a análise não prossegue com o dado
    VERIFICAÇÃO nenhuma Observação é emitida sem dado válido
```

### BASpec-TH-005 — Teto de promoção: Observação, nunca Evidência

```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement de fronteira — a ferramenta emite Observation; promoção a Evidence é
                barrada no contrato (só agente+lineage da SPEC-002 promove)
CRITÉRIO 4Es  : Eficácia/Conformidade — INV-06 é fronteira constitutiva; risco alto → C
GATE DE SAÍDA : rótulo de tipo "Observation" imutável na saída da ferramenta (ENF-03)

BASpec-TH-005:
  QUANDO:       uma ferramenta produz um dado (OHLCV, indicador, desenho, métrica de tester)
  ENTÃO:        o dado é rotulado Observation; o contrato NÃO permite que a ferramenta o rotule
                Evidence/Interpretation nem atribua Evidence Strength — promoção exige agente+lineage
                (SPEC-002)
  PORQUE:       RULE-TH-005; INV-06; CEM-001 (l.145/l.282/l.307)
  REFERÊNCIA:   RULE-TH-005; CEM-001; EC-TH-05
  VERIFICADO POR:
    DADO        data_get_strategy_results devolve métricas do Strategy Tester
    QUANDO      o dado é disponibilizado
    ENTÃO       é Observation de backtest; não é Evidência nem sobe a convicção
    VERIFICAÇÃO nenhuma ferramenta emite objeto rotulado Evidence
```

### BASpec-TH-006 — Saída de ferramenta = dado não-confiável (tool poisoning)

```
CLASSE        : C (Constitutivo)
MECANISMO     : marcação constitutiva de não-confiabilidade; o conteúdo da saída nunca é instrução
CRITÉRIO 4Es  : Eficácia — tool poisoning (36,5% de sucesso médio, research.md §3.2) contamina a
                decisão; risco alto → C
GATE DE SAÍDA : saída da ferramenta tratada como dado, nunca como comando (ENF-03); política SPEC-039

BASpec-TH-006:
  QUANDO:       uma ferramenta (incl. texto/rótulo de gráfico ou descrição de ferramenta MCP)
                retorna conteúdo
  ENTÃO:        o conteúdo é tratado como dado NÃO-confiável; NUNCA redireciona o comportamento do
                agente; a política de seleção/quarentena/contradição é da SPEC-039
  PORQUE:       RULE-TH-006; DHR-PROV-WEB-001 §2.1 (dado ≠ instrução); research.md §3.2
  REFERÊNCIA:   RULE-TH-006; SPEC-039 (fronteira)
  VERIFICADO POR:
    DADO        a descrição de uma ferramenta MCP contém instrução adversarial embutida
    QUANDO      o agente lê essa descrição
    ENTÃO       a instrução é ignorada como dado; o comportamento não muda
    VERIFICAÇÃO nenhuma mudança de comportamento é atribuível a conteúdo de saída de ferramenta
```

### BASpec-TH-007 — Perfil exploratório-supervisionado (somente-leitura por padrão)

```
CLASSE        : C (Constitutivo)
MECANISMO     : atributo de 1ª classe modo ∈ {somente-leitura (default), efeito-confirmado}; default
                read-only é enforcement
CRITÉRIO 4Es  : Eficácia/Conformidade — default seguro evita efeito não-intencional em gráfico/conta
GATE DE SAÍDA : modo default = somente-leitura, só alterável por TH-008 (ENF-03)

BASpec-TH-007:
  QUANDO:       uma ferramenta do canal exploratório (CDP) é instanciada
  ENTÃO:        seu modo default é somente-leitura (produz apenas Observação); o modo
                efeito-confirmado só é alcançável pelo gate de confirmação (TH-008)
  PORQUE:       RULE-TH-007; DHR-DEC-003 §1.1 (perfil exploratório supervisionado)
  REFERÊNCIA:   RULE-TH-007; DHR-DEC-003 §1.1; EC-TH-03
  VERIFICADO POR:
    DADO        a ferramenta draw_* é instanciada sem confirmação
    QUANDO      um agente a invoca
    ENTÃO       o modo é somente-leitura; a operação de desenho não ocorre
    VERIFICAÇÃO nenhuma operação de efeito ocorre em modo default
```

### BASpec-TH-008 — Gate de confirmação humana para ferramenta de efeito

```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement — precondição "confirmação explícita registrada"; fail-closed sem ela
CRITÉRIO 4Es  : Eficácia/Conformidade — efeito em gráfico/conta é (semi)irreversível; E3
GATE DE SAÍDA : confirmação registrada verificável por código (ENF-03)

BASpec-TH-008:
  QUANDO:       uma ferramenta de EFEITO é invocada (pine_set_source, pine_smart_compile/adicionar
                ao gráfico, draw_*, indicator_add, alert_create, launch/kill do app, indicator_set_inputs
                quando publica em estado compartilhado)
  ENTÃO:        o sistema exige confirmação explícita registrada do humano ANTES de executar;
                sem confirmação → fail-closed (operação não ocorre)
  PORQUE:       RULE-TH-008; DHR-DEC-003 §1.1; ENF-04
  REFERÊNCIA:   RULE-TH-008; ABERTURA.md §4-bis.1/§4-ter.1; EC-TH-03
  VERIFICADO POR:
    DADO        pine_set_source vai sobrescrever o editor Pine
    QUANDO      é invocada sem confirmação registrada
    ENTÃO       a operação é bloqueada (fail-closed); só procede após confirmação explícita
    VERIFICAÇÃO nenhuma operação de efeito ocorre sem confirmação registrada
```

### BASpec-TH-009 — Proibição dura de ordem / replay_trade

```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement de fronteira INV-05 — qualquer geração/roteamento de ordem ou
                replay_trade é barrado incondicionalmente
CRITÉRIO 4Es  : Conformidade/Eficácia — INV-05 é invariante fundador; irreversível; E3
GATE DE SAÍDA : lista de operações proibidas verificada por código (ENF-03)

BASpec-TH-009:
  QUANDO:       qualquer componente solicita geração/roteamento de ordem ou invoca replay_trade
  ENTÃO:        o sistema REJEITA a operação incondicionalmente (nem com confirmação humana é
                permitida — não há "ordem supervisionada" no SOT); fail-closed
  PORQUE:       RULE-TH-009; INV-05 (SOT não executa); DHR-DEC-003 §1.1 (replay_trade proibido)
  REFERÊNCIA:   RULE-TH-009; INV-05; EC-TH-04
  VERIFICADO POR:
    DADO        um pedido de replay_trade
    QUANDO      chega ao harness
    ENTÃO       é rejeitado sem exceção; nenhuma ordem é gerada/roteada
    VERIFICAÇÃO nenhuma operação de ordem/replay_trade é executável pelo harness
```

### BASpec-TH-010 — TradingViewAdapter sobre provider abstrato (nunca fonte única)

```
CLASSE        : C (Constitutivo)
MECANISMO     : enforcement de arquitetura — o contrato de dados é expresso contra provider abstrato;
                TradingViewAdapter implementa a interface como UMA fonte
CRITÉRIO 4Es  : Eficácia — acoplar o contrato a uma fonte única cria ponto único de falha e viola
                DHR-DEC-004; risco alto → C
GATE DE SAÍDA : o contrato não referencia TradingView como fonte única (verificável no design)

BASpec-TH-010:
  QUANDO:       o contrato de dados de mercado é instanciado
  ENTÃO:        é expresso contra um provider abstrato; TradingView entra via TradingViewAdapter
                como UMA fonte, nunca como fonte única da verdade nem substituto de feed L2/L3;
                o provedor de dados de máquina permanece não escolhido (BL-033)
  PORQUE:       RULE-TH-010; DHR-DEC-004 §1.2; MASTER §5 "Provider ≠ Evidence"
  REFERÊNCIA:   RULE-TH-010; DHR-DEC-004 §1.2; EC-TH-05
  VERIFICADO POR:
    DADO        o harness precisa de OHLCV de BTCUSDT
    QUANDO      o contrato é instanciado
    ENTÃO       o acesso é pelo provider abstrato; TradingViewAdapter é uma implementação possível
    VERIFICAÇÃO nenhuma BASpec/EC acopla o contrato a TradingView como fonte única
```

### BASpec-TH-011 — Mapeamento ao schema do Elliott (unix s → ISO-8601 UTC)

```
CLASSE        : D (Determinístico)
MECANISMO     : conversão determinística unix(segundos) → ISO-8601 UTC; validação de enum de símbolo/tf
CRITÉRIO 4Es  : Eficácia — o consumidor (Elliott) exige timestamp date-time; desalinhamento gera
                look-ahead bias (research.md §3.3)

BASpec-TH-011:
  QUANDO:       a ferramenta de OHLCV entrega candles para consumo pelo Agente Estrutural (Elliott)
  ENTÃO:        o sistema converte time unix(segundos) → ISO-8601 UTC (date-time), valida symbol ∈
                {BTCUSDT, XAUUSD, NAS100} e tf ∈ {S1,D1,H4,H1,M5}, e preenche o array
                market_digital_twin.timeframes conforme schemas/elliott-wave.input.json
  PORQUE:       RULE-TH-011; schema do Elliott exige timestamp date-time
  REFERÊNCIA:   RULE-TH-011; schemas/elliott-wave.input.json; ABERTURA.md §4-bis.2
  VERIFICADO POR:
    DADO        data_get_ohlcv.time = 1758484800 (unix s) para BTCUSDT/H4
    QUANDO      o dado é mapeado ao schema do Elliott
    ENTÃO       timestamp = "2025-09-21T20:00:00Z" (ISO-8601 UTC); symbol/tf validados
    VERIFICAÇÃO nenhum candle entra no schema com timestamp unix bruto
```

### BASpec-TH-012 — Quatro ferramentas Pine com Classe declarada

```
Declaração de Classe por sub-ferramenta Pine (CC-11; ABERTURA.md §4-ter.1):
  - pine_set_source (injetar código)                 → Classe C (efeito; gate TH-008; fail-closed)
  - pine_smart_compile / adicionar ao gráfico        → Classe C (efeito; gate TH-008)
  - data_get_strategy_results (ler Strategy Tester)  → Classe D (leitura; proveniência TH-013)
  - indicator_set_inputs (alterar entradas)          → Classe D se reversível e registrado; C se
                                                        publica em estado compartilhado (gate TH-008)
CRITÉRIO 4Es  : Eficácia — separar leitura (D) de efeito (C) impede que uma leitura de métrica
                arraste o risco de uma escrita no gráfico do usuário

BASpec-TH-012:
  QUANDO:       uma das quatro ferramentas Pine é invocada
  ENTÃO:        aplica-se a Classe declarada acima: injetar/compilar/alterar-que-publica → gate de
                confirmação (TH-008, C); ler Strategy Tester → leitura com proveniência (TH-013, D)
  PORQUE:       RULE-TH-008/RULE-TH-002; ABERTURA.md §4-ter.1 (efeito vs. leitura)
  REFERÊNCIA:   RULE-TH-008; RULE-TH-002; EC-TH-03
  VERIFICADO POR:
    DADO        pine_smart_compile (efeito) e data_get_strategy_results (leitura)
    QUANDO      ambas são invocadas
    ENTÃO       a 1ª exige confirmação (C); a 2ª só captura proveniência (D)
    VERIFICAÇÃO Classe correta aplicada a cada sub-ferramenta Pine
```

### BASpec-TH-013 — Proveniência de backtest + eventos/estados de observabilidade

```
CLASSE        : D (Determinístico)
MECANISMO     : captura de campos de proveniência de backtest + emissão dos estados da chamada
CRITÉRIO 4Es  : Eficácia — backtest sem janela/entradas/custos não é reconstruível (toca SPEC-041)

BASpec-TH-013:
  QUANDO:       a ferramenta de leitura do Strategy Tester (Classe D) produz métricas, ou qualquer
                ferramenta é invocada
  ENTÃO:        (a) o Provenance recebe os campos de backtest {script_sha256, script_versao_pine,
                entradas {in_N}, simbolo/tf, janela (primeira/última barra usadas), custos,
                capital/tamanho, n_tentativas, fase ∈ {treino|teste|inteira}, capturado_em_utc,
                status, rotulo_qualidade (WF-V02)}; (b) a invocação expõe os estados
                REQUESTED→EXECUTED→{OK|FAILED|STALE|INDETERMINADO|UNKNOWN} como requisito de contrato
  PORQUE:       RULE-TH-002/RULE-TH-012; ABERTURA.md §4-ter.3; ref. "Uso de Logs"; sem esses campos
                o backtest não sobe a Evidência (INV-06) e a chamada não é auditável
  REFERÊNCIA:   RULE-TH-002; RULE-TH-012; ABERTURA.md §4-ter.3; EC-TH-02; EC-TH-06
  VERIFICADO POR:
    DADO        data_get_strategy_results sem o campo "janela" preenchido
    QUANDO      o dado é disponibilizado
    ENTÃO       status = INDETERMINADO quanto à reconstrução; não sobe a Evidência
    VERIFICAÇÃO nenhuma métrica de backtest é usável sem janela + proveniência
```

> **Nota de honestidade (RULE-MET-01):** campos como `buy_hold_return`, `in_2`/`in_4` e o bloco de janela treino/teste do tutorial-Pine são `[INFERÊNCIA]`/não verificados pelo próprio tutorial (research.md §5.11) — **não** são tratados como fato nesta Spec; a execução/validação de calibração é da SPEC-018.

---

## D4 — Algoritmo (mapeamento de timestamp e gate de completude)

```
ALGORITMO: map_ohlcv_to_elliott_schema
ENTRADA:  candles[] (cada um com time unix em SEGUNDOS, open, high, low, close, volume), symbol, tf
PROCESSO:
  1. SE symbol ∉ {BTCUSDT, XAUUSD, NAS100}  → rejeitar (RULE-TH-011)
  2. SE tf ∉ {S1, D1, H4, H1, M5}           → rejeitar
  3. PARA cada candle:
       timestamp_iso = ISO-8601-UTC(from_unix_seconds(candle.time))   // s → "YYYY-MM-DDTHH:MM:SSZ"
       SE candle é a barra em formação (não fechada) → status = INDETERMINADO; descartar do fato
  4. preencher market_digital_twin.timeframes[tf] = [{timestamp_iso, open, high, low, close, volume}]
SAÍDA:    objeto conforme schemas/elliott-wave.input.json (Observation; nunca Evidence)
EXEMPLO:  time = 1758484800 (unix s) → "2025-09-21T20:00:00Z"  (BTCUSDT/H4)
          [EXEMPLO ILUSTRATIVO — a correspondência exata de epoch é verificável; não é limiar]

ALGORITMO: contract_completeness_gate   (BASpec-TH-001)
ENTRADA:  tool_contract (objeto)
PROCESSO: campos_obrigatorios = [Finalidade, Input, Output, Precisao, Determinismo, Limitacoes,
                                 Custo, Latencia, Provenance, Falhas]
          SE algum campo ausente/vazio → AUTORIZADO = false (fail-closed)
          SENÃO → AUTORIZADO = true
SAÍDA:    AUTORIZADO ∈ {true, false}
```

> **Nota (ROADMAP §22):** nenhum código de implementação é entregue; os blocos acima são pseudo-algoritmo de especificação (D4). Esboços Pine aparecem **apenas como referência marcada** no tutorial `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` (`[EXTERNO]`, não auditado) — **não** replicados como artefato desta Spec.

---

## D5 — Estados (invocação de ferramenta)

```
Estado: REQUESTED → (ferramenta executa) → EXECUTED
Estado: EXECUTED  → OK            quando o dado é válido e de barra fechada
Estado: EXECUTED  → STALE         quando o dado é de barra em formação/repaint (→ INDETERMINADO no fato)
Estado: EXECUTED  → FAILED        quando health-check/dado faltante/API instável (fail-closed, TH-004)
Estado: EXECUTED  → INDETERMINADO quando o dado existe mas não é determinístico/confirmável
Estado: REQUESTED/EXECUTED → UNKNOWN  quando o resultado da chamada não pôde ser determinado
        (timeout sem confirmação de efeito, latência além do SLA) — nunca presumir OK (fail-closed)
```

Nenhuma transição permite ir de STALE/FAILED/INDETERMINADO/UNKNOWN direto a "Observação FECHADA utilizável" sem uma nova leitura OK (fail-closed). A *política* de logging desses estados (retenção, correlação, trace/span) é **SPEC-040/BL-034**, não esta Spec.

---

## D6 — Protocolo de Publicação no Blackboard

**Por referência — M-001 ABERTA.** A Observação produzida por uma ferramenta será **publicada** no Blackboard como objeto não-hipótese; os **estados do Blackboard para objetos não-hipótese** (Observação, Missão) são **M-001 (ABERTA)** — SPEC-004. Esta Spec **não** define esses estados nem a mecânica de publicação; apenas declara que o dado entra como **Observation** (CEM-001), com proveniência, e **nunca** como Evidência/hipótese. Declarado por referência (não omitido) — coerente com CC-02/CC-04. [DECISÃO NECESSÁRIA: M-001 permanece aberta — não fechar aqui]

---

## D7 — Cenários de Teste

### Cenário-TH-T01 — OHLCV mapeado ao schema do Elliott
```
DADO        data_get_ohlcv devolve candles de BTCUSDT/H4 com time em unix segundos
QUANDO      o TradingViewAdapter mapeia ao schema do Elliott
ENTÃO       timestamp vira ISO-8601 UTC; symbol/tf validados; proveniência anexada; barra em formação
            marcada INDETERMINADO
VERIFICAÇÃO objeto conforme schemas/elliott-wave.input.json; nenhum timestamp unix bruto; é Observation
```

### Cenário-TH-T02 — Ferramenta de efeito exige confirmação
```
DADO        um agente quer marcar a invalidação no gráfico via draw_* (efeito)
QUANDO      a ferramenta é invocada em modo default (somente-leitura)
ENTÃO       o sistema exige confirmação explícita registrada; sem ela, não desenha (fail-closed)
VERIFICAÇÃO nenhuma operação de efeito ocorre sem confirmação registrada
```

### Cenário-TH-T03 — Canal fora do ar → fail-closed
```
DADO        o canal CDP está indisponível (health-check falha)
QUANDO      um agente solicita OHLCV
ENTÃO       status = FAILED/UNKNOWN; nenhuma Observação fabricada; análise não prossegue com o dado
VERIFICAÇÃO nenhuma Observação emitida sem dado válido (RULE-MET-01)
```

### Cenário-TH-T04 — Leitura de Strategy Tester como Observação de backtest
```
DADO        data_get_strategy_results devolve métricas com a janela (primeira/última barra) preenchida
QUANDO      o dado é disponibilizado
ENTÃO       é Observation de backtest com proveniência completa (script_sha256, entradas, custos,
            janela, fase); não sobe a Evidência; calibração é da SPEC-018
VERIFICAÇÃO métrica de backtest sem janela → INDETERMINADO; nunca vira convicção
```

---

## D8 — Adversarial (reforço para o gate de maturidade L3)

> SPEC-038 é HIGH (não CRITICAL); D8 não é exigido pela tabela de profundidade, mas é requerido pelo gate L3 (atomic-spec §7) e pelo §7-bis Bloco A. Casos de negação para as BASpecs Classe C (≥1 por BASpec C — exigência da entrega).

### ADV-TH-01 — Barra em formação apresentada como fato
**DADO:** o último candle de H4 está em formação. **QUANDO:** um agente tenta usar seu close como determinístico. **ENTÃO:** o sistema DEVE marcá-lo INDETERMINADO e recusar o uso como fato. **PORQUE:** RULE-TH-003; WF-C03. **VERIFICAÇÃO:** nenhuma Observação FECHADA deriva de barra em formação.

### ADV-TH-02 — Dado de ferramenta promovido direto a Evidência (negação de TH-005/C)
**DADO:** um dado de indicador. **QUANDO:** um componente tenta rotulá-lo Evidence com Evidence Strength. **ENTÃO:** o sistema DEVE rejeitar — só agente+lineage (SPEC-002) promove. **PORQUE:** RULE-TH-005; INV-06. **VERIFICAÇÃO:** nenhuma ferramenta emite objeto Evidence.

### ADV-TH-03 — Efeito sem confirmação (negação de TH-007/TH-008/C)
**DADO:** `pine_set_source` prestes a sobrescrever o editor. **QUANDO:** invocada sem confirmação registrada. **ENTÃO:** o sistema DEVE falhar fechado. **PORQUE:** RULE-TH-008; ENF-04. **VERIFICAÇÃO:** nenhuma operação de efeito sem confirmação.

### ADV-TH-04 — Tentativa de ordem/replay_trade (negação de TH-009/C)
**DADO:** um pedido de `replay_trade` ou de roteamento de ordem. **QUANDO:** chega ao harness. **ENTÃO:** o sistema DEVE rejeitar incondicionalmente (nem com confirmação). **PORQUE:** RULE-TH-009; INV-05. **VERIFICAÇÃO:** nenhuma ordem/replay_trade executável.

### ADV-TH-05 — Acoplar o contrato a TradingView como fonte única (negação de TH-010/C)
**DADO:** uma proposta de instanciar o contrato diretamente sobre a API do TradingView. **QUANDO:** o design é avaliado. **ENTÃO:** o sistema DEVE recusar — o contrato é sobre provider abstrato; TradingView é uma fonte via adapter. **PORQUE:** RULE-TH-010; DHR-DEC-004 §1.2. **VERIFICAÇÃO:** nenhuma EC/BASpec acopla o contrato a fonte única.

### ADV-TH-06 — Saída de ferramenta como instrução (negação de TH-006/C)
**DADO:** descrição de ferramenta MCP com injeção adversarial. **QUANDO:** o agente a lê. **ENTÃO:** o sistema DEVE tratá-la como dado, nunca como comando. **PORQUE:** RULE-TH-006; DHR-PROV-WEB-001 §2.1. **VERIFICAÇÃO:** nenhuma mudança de comportamento atribuível a saída de ferramenta.

### ADV-TH-07 — Contrato incompleto admitido (negação de TH-001/C)
**DADO:** ferramenta sem campo Determinismo. **QUANDO:** admitida. **ENTÃO:** o gate DEVE recusá-la como fonte de Observação. **PORQUE:** RULE-TH-001. **VERIFICAÇÃO:** nenhuma Observação de ferramenta com contrato incompleto.

---

## I/O Schemas (especificação, não implementação)

### Contrato por-ferramenta (molde)
```json
{
  "tool": "data_get_ohlcv",
  "finalidade": "string",
  "input": { "symbol": "enum[BTCUSDT,XAUUSD,NAS100]", "tf": "enum[S1,D1,H4,H1,M5]", "...": "..." },
  "output": "string (tipo e forma do dado)",
  "precisao": "string | INDETERMINADO",
  "determinismo": "enum[FECHADA_DETERMINISTICA, EM_FORMACAO_NAO_DETERMINISTICA]",
  "limitacoes": ["string"],
  "custo": "string | INDETERMINADO (NUNCA entra em convicção — INV-04)",
  "latencia": "string | INDETERMINADO",
  "provenance": { "$ref": "#/provenance_record" },
  "falhas": ["string (modo fail-closed declarado)"]
}
```

### provenance_record (por leitura)
```json
{
  "tool": "string", "args": {}, "symbol": "string", "tf": "string",
  "captured_at_utc": "date-time", "last_closed_bar": "date-time",
  "indicator": "string (quando aplicável)", "indicator_version": "string (quando aplicável)",
  "script_sha256": "string (backtest; quando aplicável)", "janela": "string (1ª/última barra usadas)",
  "status": "enum[OK,FAILED,STALE,INDETERMINADO,UNKNOWN]", "rotulo_qualidade": "string (WF-V02)",
  "tipo": "Observation (imutável — nunca Evidence)"
}
```

### tool_call_event (requisito de observabilidade — política em SPEC-040)
```json
{ "estado": "enum[REQUESTED,EXECUTED,OK,FAILED,STALE,INDETERMINADO,UNKNOWN]",
  "tool": "string", "requested_at_utc": "date-time", "resolved_at_utc": "date-time | null" }
```

---

## Enforcement Contracts

### EC-TH-01 — Gate de admissão por completude de contrato (TH-001)
```
CAPABILITY   : admitir/usar uma ferramenta como fonte de Observação
EFFECT       : publicação de uma Observação na cadeia cognitiva a partir da ferramenta
PRECOND      : os 10 campos do contrato por-ferramenta estão presentes e não-vazios
POSTCOND     : ou a ferramenta é admitida com contrato completo, ou é recusada como fonte
POLICY       : RULE-TH-001; ROADMAP §17; INV-06 (Observação, não Evidência)
LEVEL        : E2 (Operacional) — precond/postcond/capabilities de admissão
FAILURE-MODE : fail-closed — contrato incompleto ⇒ ferramenta não autorizada como fonte
EVIDENCE     : registro do contrato (10 campos) auditável; decisão de admissão logada
```

### EC-TH-02 — Proveniência e fail-closed de dado (TH-002/TH-003/TH-004/TH-013)
```
CAPABILITY   : disponibilizar um dado de ferramenta como Observação
EFFECT       : grava/publica a Observação (com proveniência) para consumo dos agentes
PRECOND      : proveniência por leitura anexada; barra em formação marcada INDETERMINADO; dado válido
POSTCOND     : Observação disponível com status ∈ {OK|STALE|INDETERMINADO}; ou análise para (FAILED/UNKNOWN)
POLICY       : RULE-TH-002/003/004; WF-C03; RULE-MET-01 (não-fabricação); ENF-04
LEVEL        : E2 (Operacional)
FAILURE-MODE : fail-closed — sem dado válido/proveniência ⇒ não emite Observação; nunca fabrica valor
EVIDENCE     : provenance_record por Observação; status registrado; auditável pelo Revisor/observabilidade
```

### EC-TH-03 — Gate de confirmação para ferramenta de efeito (TH-007/TH-008/TH-012)
```
CAPABILITY   : executar uma ferramenta de EFEITO (draw_*, indicator_add, alert_create,
               pine_set_source, compilar/adicionar ao gráfico, launch/kill, indicator_set_inputs
               que publica)
EFFECT       : altera o gráfico/layout/conta do usuário (efeito externo, (semi)irreversível)
PRECOND      : confirmação explícita registrada do humano; modo = efeito-confirmado
POSTCOND     : ou a operação ocorre com confirmação registrada, ou não ocorre (fail-closed)
POLICY       : RULE-TH-007/008; DHR-DEC-003 §1.1; INV-05 (efeito ≠ ordem); ENF-04
LEVEL        : E3 (Crítico) — efeito externo (semi)irreversível
FAILURE-MODE : fail-closed — sem confirmação registrada ⇒ operação bloqueada
EVIDENCE     : registro da confirmação (quem/quando) + registro da operação
MÉTODO FALSO-DENY (ENF-07): amostragem periódica de confirmações negadas vs. operações legítimas
               bloqueadas; limiar de falso-DENY = gap aberto (atomic-spec §12) — não fechar aqui
```

### EC-TH-04 — Proibição de ordem / replay_trade (TH-009)
```
CAPABILITY   : (nenhuma — capacidade explicitamente negada)
EFFECT       : geração/roteamento de ordem ou replay_trade (PROIBIDO)
PRECOND      : (não há precondição que autorize — incondicionalmente barrado)
POSTCOND     : nenhuma ordem/replay_trade é gerada/roteada pelo harness
POLICY       : RULE-TH-009; INV-05 (SOT não executa ordem)
LEVEL        : E3 (Crítico) — irreversível
FAILURE-MODE : fail-closed absoluto — pedido de ordem/replay_trade sempre rejeitado
EVIDENCE     : registro de rejeição; ausência de qualquer efeito de mercado
MÉTODO FALSO-DENY (ENF-07): N/A — não há DENY legítimo a falsear (nenhuma ordem é jamais permitida)
```

### EC-TH-05 — Teto de promoção e provider abstrato (TH-005/TH-010)
```
CAPABILITY   : produzir Observação a partir de uma fonte de dados de mercado
EFFECT       : publica Observation (nunca Evidence) via provider abstrato
PRECOND      : dado rotulado Observation; acesso via provider abstrato (TradingViewAdapter = 1 fonte)
POSTCOND     : Observação publicada; promoção a Evidência só por agente+lineage (SPEC-002)
POLICY       : RULE-TH-005/010; INV-06; DHR-DEC-004 §1.2; CEM-001
LEVEL        : E2 (Operacional)
FAILURE-MODE : fail-closed — tentativa de rotular Evidence ou acoplar fonte única ⇒ rejeitada
EVIDENCE     : rótulo "Observation" imutável; design referencia provider abstrato
```

### EC-TH-06 — Requisito de observabilidade da chamada (TH-013)
```
CAPABILITY   : expor os estados da invocação de ferramenta
EFFECT       : emite tool_call_event (REQUESTED→EXECUTED→{OK|FAILED|STALE|INDETERMINADO|UNKNOWN})
PRECOND      : N/A (E1 — contratual)
POSTCOND     : N/A (E1)
POLICY       : RULE-TH-012; ref. "Uso de Logs"; a POLÍTICA de logs é SPEC-040/BL-034
LEVEL        : E1 (Contratual) — requisito de contrato, não enforcement de efeito crítico
FAILURE-MODE : N/A (E1 — mínimo CAPABILITY+EFFECT+LEVEL+EVIDENCE)
EVIDENCE     : tool_call_event observável por chamada
```

---

## Fronteiras (SPEC-038 × 039 × 040 × 042 × 044 × 018)

| Slot | Responsabilidade | Fronteira com SPEC-038 |
|---|---|---|
| **SPEC-038** | **Contrato de ferramenta/dado** (molde 10 campos; Observação; proveniência; determinismo; fail-closed; gates de confirmação; adapter) | — |
| **SPEC-039** | *Política* de seleção/preferência/fallback/tool poisoning/resultado contraditório | SPEC-038 marca "dado não-confiável"; SPEC-039 decide o que fazer com isso |
| **SPEC-040** | *Política* de observabilidade/logs (trace/span, correlação, retenção) | SPEC-038 exige os estados REQUESTED→…→UNKNOWN; SPEC-040 define a política de logging |
| **SPEC-042** | Guardrails de runtime (allow/deny/limites/gates de execução) | SPEC-038 declara o gate de confirmação no contrato; SPEC-042 aplica em runtime |
| **SPEC-044** | Detecção de alucinação/afirmação sem fonte | SPEC-038 garante proveniência; SPEC-044 detecta ausência dela |
| **SPEC-018** | Backtest/calibração da J-001 (dona = BL-032) | SPEC-038 fornece a ferramenta de leitura do tester + proveniência; SPEC-018 calibra |

---

## Riscos

- **R-1 (conformidade — risco ASSUMIDO por Andraus):** automatizar dados do TradingView (CDP; e eventualmente ler o Strategy Tester) cai no uso non-display/"algorithmic decision-making" vedado pelo ToS → suspensão de conta sem aviso. **Andraus ASSUMIU este risco (DHR-DEC-003 §1.1);** este Plan **não afirma conformidade nem é parecer jurídico**. Contenção: dado = Observação (nunca fonte de decisão/Evidência/ordem), somente-leitura por padrão, efeitos só com confirmação. [DECISÃO NECESSÁRIA: SPEC-038-DATASRC-001 decidida no recorte DHR-DEC-004; provedor de dados de máquina permanece ABERTO]
- **R-2 (segurança):** ferramentas externas/MCP sujeitas a tool poisoning (research.md §3.2) — contrato trata saída como dado não-confiável; *política* em SPEC-039.
- **R-3 (determinismo):** >95% dos indicadores repintam (research.md §3.3) — mitigado pelo campo Determinismo obrigatório (TH-003).
- **R-4 (escopo):** absorver governança (SPEC-039), observabilidade (SPEC-040) ou calibração (SPEC-018) — mitigado pelas fronteiras acima.
- **R-5 (latência):** latência da candidata/MCP = INDETERMINADO (research.md §5) — não inventada; tensão com WF-K02 registrada, não resolvida.

---

## Plano de re-apontamento / erratum e emenda à SPEC-020 (BL-017)

- **Número SPEC-038 preservado** → nenhum re-apontamento de gatilho `spec:` necessário (research.md §6.3). Referências baselined (SPEC-003/plan.md:1196 ponteiro; SPEC-020 via BL-017) apontam o número preservado → **nenhum erratum aditivo** (padrão ERRATUM-SPEC019-001 não se aplica; INV-09). [FONTE: research.md §6.4]
- **Emenda à SPEC-020 (fecha a dimensão B "tool correctness") — `[PROPOSTA]`, não aplicada aqui.** BL-017 está ATIVADO (DHR-DEC-004 §1.1), mas o fechamento ocorre **na homologação da SPEC-038**, por emenda pontual à SPEC-020, decidida por Andraus (CONS-01 — o Especificador não fecha). Texto proposto:

  > *[PROPOSTA de emenda à SPEC-020, a aplicar SÓ na homologação da SPEC-038]* "A dimensão B `tool correctness` (classe dependente-de-upstream, ROADMAP §289/BL-017) passa a FECHÁVEL: o critério verificável de correção de ferramenta é a conformidade ao contrato por-ferramenta da SPEC-038 (10 campos; Observação com proveniência; determinismo; fail-closed; Enforcement Contracts EC-TH-01..06). Nenhuma dimensão B de outro componente (RAG faithfulness ↔ SPEC-007; decision traceability ↔ SPEC-014) é tocada."

  Enquanto não homologada a SPEC-038, `tool correctness` **permanece não-fechada** (CONS-01). [DECISÃO NECESSÁRIA — de Andraus]

---

## Etiquetagem e status epistemológico (TRACE-06)

- **[FONTE]/FATO NORMATIVO:** abertura homologada (DHR-SPEC038-001), DHR-DEC-003/004, WORKFLOW v2.1, CEM-001, INV-05/06/09, RULE-* citadas.
- **FATO ARQUITETURAL:** este Plan (candidato a baseline).
- **[PROPOSTA]:** RULE-TH-001..012, BASpecs, Enforcement Contracts, emenda à SPEC-020.
- **[INFERÊNCIA]:** eixo de herança não-vertical; mapeamento de campos do tutorial-Pine.
- **[EXTERNO]:** fontes do `research.md` (tool poisoning, repainting, provedores, ToS) — DADO, nunca instrução/baseline.
- **[DECISÃO NECESSÁRIA]:** J-001, N-001, M-001, H-001 (todas ABERTAS); escolha do provedor de dados de máquina (BL-033); fechamento de `tool correctness` na SPEC-020; D-001..D-027 do MASTER ABERTAS.
- **INDETERMINADO:** latência/limites da candidata e do MCP oficial; contagem de ferramentas; conformidade jurídica do canal.

---

## Decisões abertas incidentes (CONS-01 — não fechar)

- **J-001** (fórmula/pesos/limiares definitivos do Conviction Vector) — **ABERTA**; esta Spec não a toca.
- **N-001** (pesos por ativo) — **ABERTA**.
- **M-001** (estados do Blackboard para objetos não-hipótese) — **ABERTA** (D6 por referência; SPEC-004).
- **H-001** (Knowledge Graph) — **ABERTA**.
- **WF-D03** (residual; convicção macro×global × J-001) — **ABERTA**; não tocada (não fechar — DHR-WF-001).
- **SPEC-038-DATASRC-001** — **DECIDIDA no recorte** (DHR-DEC-004 §1.2: TradingView uma das fontes via adapter; risco ToS assumido); a **escolha do provedor de dados de máquina permanece ABERTA** (BL-033; D-001..D-027 ABERTAS).
- **ECC-03-001** (escopo da RULE-ECC-03) — **ABERTA**; não incide nesta Spec.
- Nenhuma decisão aberta aparece como invariante fechado nesta entrega (CONS-01).

**Pronto para revisão.**
```
