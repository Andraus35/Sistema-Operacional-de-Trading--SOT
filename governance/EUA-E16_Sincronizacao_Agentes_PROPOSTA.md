# EUA-E16 — Sincronização das Definições dos Agentes + Regra Permanente de Sincronização (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E16** (emenda de processo/governança + atualização das definições dos agentes) |
| Natureza | (1) Sincronização imediata de `especificador.md`/`revisor.md` com as homologações 19–21/09; (2) **Regra Permanente de Sincronização de Agentes (RPSA)** — mecanismo de garantia |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-21; ata `DHR-EUA-E16`). Agentes sincronizados (carimbo `sincronizado-até: DHR-EUA-E16`); RPSA instalada (RCH-001 passo 7 + gate RMR-001). |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-21 |
| Alvo | `.claude/agents/especificador.md` · `.claude/agents/revisor.md` (via Controlador); `governance/RCH-001` (sensor); `backlog/RMR-001` (gate de sync); `atomic-spec.md`/CATALOGO (fonte de verdade) |
| Fundamento no baseline | INV-07/INV-09; PC-08 (só Andraus homologa); D-DHR-PAP-001-01; MAN-001 §6 (sensor de drift no Hygiene); RMR-001 §4 (surfacing por gate); RULE-HD-04 (referência por ID+versão) |
| Princípio-guia | **Fonte única de verdade + sincronização forçada por gate.** Os agentes não duplicam a norma — referenciam os baselines; um **carimbo de proveniência** + **sensor de drift** + **gate de sincronização** garantem que a lista de leitura e os checklists embutidos nunca fiquem defasados do que foi homologado em seu escopo. |

---

## 1. Justificativa `[INFERÊNCIA]`

Auditoria de 2026-09-21: `especificador.md` e `revisor.md` estão **congelados em 2026-09-15**, anteriores a todas as homologações de 19–21/09. Drift detectado (D-1..D-10, §2). Além do prompt congelado, há **gap composto**: os baselines que os agentes carregam (`RULES.md` v1.1, `atomic-spec.md` v1.4) ainda **não incorporaram** as emendas (diferido à v1.5, EUA-E15). Resultado: hoje os agentes operariam **cegos** a 11 emendas + 4 Master Contracts + redesignação do piloto.

Corrigir só o drift atual não basta — **o problema recorre** a cada nova homologação em escopo de agente. Esta emenda entrega (a) a sincronização imediata **e** (b) uma **regra permanente** que torna a sincronização uma **condição de gate**, reusando o maquinário já homologado (RMR-001 surfacing + Hygiene sensor + efeitos do Controlador).

---

## 2. Auditoria de drift — o que os agentes NÃO sabem `[FONTE]`

| # | Homologado 19–21/09 | Estado nos agentes |
|---|---|---|
| D-1 | EUA-E03/SES-001 (CC-06/CC-07; 17 campos §59; cadeia §60) | Ausente — Constitution Check só 5 itens |
| D-2 | EUA-E04 Herança/Delta (RULE-HD, CC-08) | Ausente |
| D-3 | N8–N17 (EUA-E05..E14): RULE-EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET + CC-09/CC-10 + INDETERMINADO + INV-EPI | Ausente |
| D-4 | MAN-001 (nós N1–N17; convergência horizontal) | Ausente |
| D-5 | CONFLICT-MAP K-MAN-04..17 + inversões contextuais GPR §3.6 | Ausente |
| D-6 | 4 Master Contracts BL-010..013 (ref. externas) | Ausente |
| D-7 | RMR-001 wiring (ROADMAP §23 passo 11-bis; PAP-001 Bloco 4 §6.3) | Ausente no fluxo |
| D-8 | EUA-E15 (piloto = SPEC-001 auditoria retroativa; SPEC-002 fora do caminho crítico) | Fluxo ainda prospectivo "próxima Spec" |
| D-9 | PAP-001/D-DHR-PAP-001-01 (retroativo-como-auditoria) | Parcial |
| D-10 | Referências externas não-normativas — disciplina "não adotar rótulos" | Ausente |
| **D-11** | Revisor §3: "Conviction **4D**" | **Erro factual** — é 8D (INV-03/Q-008); corrigir |
| **D-12** | frontmatter `model: claude-opus-4-5` | Possivelmente defasado — decisão de Andraus (Q6) |

---

## 3. Parte 1 — Sincronização imediata (Q1–Q2) `[PROPOSTA]`

**Aplicável a AMBOS os agentes (Controlador aplica após homologação):**

**3.1 Lista de leitura obrigatória (GATE DE ENTRADA) — expandir de {roadmap, atomic-spec} para:**
```
roadmap.md · atomic-spec.md · RULES.md · CONFLICT-MAP.md · MAN-001 ·
CATALOGO-OFICIAL.md · RMR-001 (checar itens ATIVADOS — passo 11-bis) ·
atas EUA-Exx homologadas (ponte interina até a v1.5 incorporar as RULE-* ao RULES.md)
```

**3.2 Constitution Check — substituir os 5 itens por CC-01..CC-10** (conforme atomic-spec §10.5 + emendas):
CC-01 hierarquia · CC-02 não redefinir Modelo Canônico · CC-03 Conviction 8D/J-001 aberto · CC-04 5+5 Salvaguardas · CC-05 complexidade · **CC-06 campos SES-001 §59** · **CC-07 cadeia §60** · **CC-08 Herança/Delta** · **CC-09 status epistemológico/Epistemic Check** · **CC-10 terminologia concorrente (Semântica)**.

**3.3 Verificação das disciplinas cognitivas N8–N17** (via atas até v1.5): RULE-EPI (fato≠interpretação/anti-conversão) · RULE-SEM · RULE-ONT · RULE-INQ · RULE-CAU · RULE-CTF · RULE-UNC · RULE-PRB · RULE-DEC · RULE-MET · **INDETERMINADO** como estado válido · **INV-EPI**.

**3.4 MAN-001 + referências externas** — reconhecer nós N1–N17; disciplina "não adotar rótulos" de referências externas (G-gates, I-xx, namespaces dos Master Contracts BL-010..013); fronteiras J-001/CC-02.

**3.5 Fluxo atualizado (EUA-E15)** — o piloto de incorporação é a **auditoria retroativa da SPEC-001**; regime auditoria-não-reescrita; SPEC-002 não é pré-requisito; consultar RMR-001 (ATIVADOS) no gate.

**3.6 Correções factuais** — Revisor: "Conviction 4D" → **8D** (D-11); ambos: "5 Salvaguardas" → **5+5** onde aparecer isolado.

---

## 4. Parte 2 — Regra Permanente de Sincronização de Agentes (RPSA) — **a garantia** (Q3–Q5) `[PROPOSTA]`

### 4.1 Definição de "escopo de trabalho dos agentes" `[PROPOSTA]`
Uma homologação **toca o escopo dos agentes** quando altera qualquer um de: invariantes (INV-*/PC-*) · Constitution Check (CC-*) · RULE-* · método do atomic-spec (BASpec/D0–D9/Enforcement/etiquetagem) · **SES-001 (campos §59/cadeia §60/overlay de domínio)** · decisões abertas (J-001 etc.) · nós do MAN-001 · referências externas/K-MAN · fluxo ou piloto · GRE-001/HRE-001/PEP-001/PRE-001 · sequência do roadmap. *(SES-001 explícito por A-01, parecer do Revisor.)*

### 4.2 Fonte única de verdade (economicidade) `[PROPOSTA]`
Os agentes **não duplicam** conteúdo normativo volátil — **referenciam** os baselines (CATALOGO/CONFLICT-MAP/atomic-spec/RULES/MAN-001) via lista de leitura obrigatória. Só o **checklist embutido** e a **lista de leitura** exigem sync. Assim o custo de manutenção fica mínimo: o que muda por referência não obriga editar o `.md`; o que está embutido, sim.

### 4.3 Carimbo de proveniência (detecção determinística) `[PROPOSTA]`
Cada agente passa a carregar no cabeçalho:
```
sincronizado-até: <código da última DHR aplicada ao escopo> (ex.: DHR-EUA-E16)
```
Drift é detectável comparando esse carimbo com a **última DHR em escopo** no CATALOGO-OFICIAL. Determinístico, auditável.

### 4.4 Gate de Sincronização (efeito obrigatório do Controlador) `[PROPOSTA]`
Adicionar aos **"Efeitos de registro (Controlador)"** de toda DHR:
> **Passo Agent-Sync:** se a homologação tocar o escopo dos agentes (§4.1), o Controlador **propaga a mudança** a `especificador.md`/`revisor.md` e atualiza o carimbo `sincronizado-até`. Se a propagação não puder ser imediata, abre **item ATIVADO no RMR-001** (gatilho `hygiene:próximo ciclo`) com ação "sincronizar agentes com DHR-xxx".

### 4.5 Gate bloqueante (reusa RMR-001 §4) `[PROPOSTA]`
Um item **Agent-Sync ATIVADO pendente** é **achado de gate**: a **próxima Spec não inicia** com sincronização de agente em aberto (o mesmo mecanismo que já vale para itens ATIVADO do RMR-001). O Revisor reporta; o gate não fecha limpo.

### 4.6 Sensor no Hygiene (RCH-001 — passo 7) `[PROPOSTA]`
Acrescentar à rotina permanente de Check:
```
7. sync de agentes (EUA-E16, RPSA): conferir que o carimbo `sincronizado-até` de
   especificador.md e revisor.md corresponde à última DHR em escopo (§4.1) no CATALOGO.
   Divergência → FLAG no RCH-001 + item no CIC-001 (Harness Debt) + Agent-Sync ATIVADO no RMR-001.
```

---

## 5. Ponte interina vs v1.5 `[PROPOSTA]`

- **Até a v1.5** (piloto SPEC-001, EUA-E15): os agentes leem as **atas EUA-Exx** para as RULE-* (que ainda não estão no RULES.md).
- **A partir da v1.5**: `atomic-spec.md`/`RULES.md` v1.5 carregam as RULE-*; a lista de leitura pode simplificar para os baselines consolidados. O carimbo `sincronizado-até` acompanha a v1.5.

---

## 6. Non-goals `[FONTE]`

- **Não** altera o método de especificação em si (BASpec/D0–D9/Enforcement) — apenas sincroniza o **conhecimento** dos agentes com o que já foi homologado.
- **Não** edita os `.md` dos agentes nesta proposta (isso é ato do Controlador pós-homologação — cabeçalho "não altere sem emenda").
- **Não** cria autoridade nova: o trio Especificador→Revisor→Andraus permanece; a RPSA é mecânica de sincronização, não de decisão.
- **Não** duplica norma nos agentes (fonte única de verdade — §4.2).

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Sincronização imediata dos dois agentes (§3, D-1..D-10) | **Sim** |
| Q2 | Corrigir erros factuais D-11 (4D→8D) e "5→5+5 Salvaguardas" | **Sim** |
| Q3 | Instituir a **RPSA** (§4): escopo de agente + fonte única de verdade + carimbo de proveniência | **Sim** |
| Q4 | **Gate de Sincronização** como efeito obrigatório do Controlador + gate bloqueante (RMR-001 §4) | **Sim** |
| Q5 | **Sensor passo 7** no Hygiene (RCH-001) | **Sim** |
| Q6 | Atualizar `model:` no frontmatter dos agentes (D-11: opus-4-5 → modelo vigente) | **Confirmar** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (esta)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra INV-07/09, PC-08, MAN-001 §6, RMR-001 §4, GRE-001/HRE-001
   ↓
Andraus homologa (decide Q1–Q6)
   ↓
Controlador aplica §3 aos .md dos agentes (carimbo sincronizado-até: DHR-EUA-E16) + wire da RPSA (RMR-001 gate + RCH-001 passo 7)
```

---

## Anexo A — Autopré-check do Especificador (2026-09-21)

- [x] TRACE-06; status = PROPOSTA (CONS-01).
- [x] Não edita os `.md` dos agentes nesta proposta (respeita cabeçalho "não altere sem emenda").
- [x] Reusa maquinário homologado (RMR-001 §4 surfacing, MAN-001 §6 sensor, efeitos do Controlador) — economicidade, sem criar autoridade nova.
- [x] Fonte única de verdade (agentes referenciam, não duplicam) — minimiza manutenção.
- [x] Drift atual mapeado (D-1..D-12) com âncora; correções factuais incluídas.
- [x] Ponte interina (atas) vs v1.5 (baselines consolidados) explícita.

## Anexo B — Parecer do Revisor SOT (2026-09-21)

**Veredito: CONFORME** — 1 achado Menor (A-01, acatado). Acesso ao `RULES.md` v1.1 e às duas definições de agente confirmado (M-02).

**Baselines auditados:** RULES.md v1.1 · especificador.md/revisor.md (congelados 2026-09-15) · atomic-spec v1.4 (§10.5 CC-01..07, §11, INV-03, J-001) · MAN-001 §6 · RMR-001 §4 · RCH-001 · CATALOGO-OFICIAL · CONFLICT-MAP + atas DHR-EUA-E03..E15.

**Drift confirmado por leitura direta:** especificador.md l.161-166 e revisor.md l.124-129 = Constitution Check só 5 itens; **revisor.md l.127 = "Conviction 4D" (ERRO FACTUAL — deve ser 8D, INV-03/Q-008)**; lista de leitura só {roadmap, atomic-spec}; fluxo ignora EUA-E15/RMR; nenhuma referência a N8–N17/MAN-001/Master Contracts. Gap composto confirmado: RULES v1.1 e atomic-spec v1.4 não contêm as RULE-* (diferidas à v1.5) — ponte via atas necessária.

**Resumo por ponto:** (1) drift D-1..D-12 preciso — PASS; (2) gap composto real, ponte §5 necessária — PASS; (3) RPSA suficiente (3 mecanismos + carimbo determinístico; furo "mudança sem DHR" mitigado por PC-08 + sensor Hygiene) — PASS; (4) reusa RMR-001 §4 e MAN-001 §6 sem autoridade nova, PC-08 intacto — PASS; (5) fonte única de verdade reduz drift futuro — PASS; (6) não edita .md agora, carimbo aditivo, INV-07/09 OK — PASS; (7) escopo §4.1 — PASS com A-01; (8) non-goals/Q1–Q6 coerentes — PASS.

**Achado:**

| ID | Severidade | Constatação | Tratamento |
|---|---|---|---|
| A-01 | Menor | Escopo §4.1 não mencionava SES-001 explicitamente (coberto implicitamente via atomic-spec) | **ACATADO** — §4.1 atualizado com "SES-001 (campos §59/cadeia §60/overlay)". |

Nenhum achado Crítico ou Médio.

**Recomendação (Q1–Q6):** Sim para Q1–Q5; Q6 (`model:` frontmatter) = decisão de Andraus. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
