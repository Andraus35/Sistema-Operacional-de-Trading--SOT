# EUA-E04 — Bloco "Herança / Delta" no atomic-spec §8 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E04** (emenda ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx ao `atomic-spec.md` |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E04`). Vigência imediata; incorporação ao `atomic-spec` v1.5 diferida ao piloto em SPEC-002 (A-03/P4). |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `atomic-spec.md` §8 (template — inserir §8.3) e §10.5 (Constitution Check — inserir CC-08) |
| Origem conceitual | HCH-001 §14/§16/§59 (herança por delta) — importada **só a mecânica**, sem os rótulos H0–H4 / L0–L4 / M0–M7 (colidem — ver auditoria HCH-001) |
| Fundamento no baseline | SAS-001 "Subordinação aos Modelos Canônicos" (§2.7, §5.3, §5.8, Princípio 6); SES-001 (overlay de domínio); PAP-001 (regime por classe, D-DHR-PAP-001-01); Catálogo "INHERITS + LOCAL DELTA" |
| Precedência | Não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4, harness-score, nem Marcos. Não cria autoridade nova. |

---

## 1. Justificativa `[INFERÊNCIA]`

A herança-por-delta **já é praticada** no SOT, porém de forma **implícita e dispersa**: o SAS-001 subordina-se ao canon, o SES-001 sobrepõe domínio, o PAP-001 regula por classe de princípio e o Constitution Check confere conformidade. Falta **um campo único e uniforme** onde a spec declare, de forma auditável, *o que herda* e *o que acrescenta*. Sem isso, o Revisor reconstrói a cadeia peça por peça e abrem-se dois riscos que o próprio harness nomeia: **duplicação** (copiar o herdado) e **remoção silenciosa** de requisito herdado (Harness Drift/Debt).

Esta emenda torna a herança **explícita, referenciada e auditável**, unificando SAS (subordinação) + SES (overlay) + PAP (regime) + Constitution Check numa só declaração — a custo baixo e sem conflito com baselines.

---

## 2. Classificação do HCH-001 (pendência-mãe) `[DECISÃO — aprovada por Andraus em sessão, 2026-09-20; registro formal pendente de Controlador]`

O HCH-001 (`CAMADA DE HARNESS.MD`) é classificado como **pano de fundo conceitual da Trilha A** — mesmo status do GEH-001 ("referência generalista; os documentos governados é que são a instância do SOT"). **Não é normativo por si só.** Dele importa-se apenas a mecânica de herança-por-delta (esta emenda). Ficam **fora** de adoção, por colisão com baselines: os rótulos H0–H4, a escala "3Es + Economicidade" (§43-44), as maturidades L0–L4 (§29) e M0–M7 (§53).

> Ação de registro pendente: incluir o HCH-001 no CATÁLOGO OFICIAL como "referência externa/pano-de-fundo, não-normativa" e anotar a colisão de rótulos no CONFLICT-MAP (ato do Controlador após parecer do Revisor).

---

## 3. Mudança proposta no Template §8 — novo §8.3 `[PROPOSTA]`

Inserir o bloco na sequência de seções do §8, após "Regras (D2)" e antes de "Comportamento — BASpecs (D3)":

```
→ Regras (D2)
→ HERANÇA / DELTA (§8.3 — NOVO)
→ Comportamento — BASpecs (D3)
```

### §8.3 — Bloco Herança / Delta (especificação)

```
HERANÇA / DELTA

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO):
  - Constituição/Princípios: <IDs PC-/PB-/PE- aplicáveis (GPR-001)>
  - Modelos Canônicos: <CEM-001 v1.0, CHM-001 v1.0, …>
  - Método: atomic-spec v<X> (F.1–F.4, E0–E3)
  - Overlay de domínio, se houver: <SES-001 §…>

ADDED (delta local — o que esta spec acrescenta):
  - Comportamentos/campos de domínio próprios
  - Invariantes locais (não podem contradizer os herdados)
  - Novas ferramentas/sensores/evidências

MODIFIED (especialização de regra herdada):
  - <regra herdada> → <forma especializada> [justificativa]

REMOVED (só com governança — nunca implícito):
  - <requisito herdado suprimido> + justificativa + ref. de homologação
  - (vazio por padrão; item preenchido exige decisão registrada de Andraus)
```

**Obrigatoriedade (proporcional):**
- **INHERITS** e **ADDED**: obrigatórios em toda spec de componente e Engineering Card.
- **MODIFIED**: obrigatório apenas se houver especialização de regra herdada.
- **REMOVED**: em regra **vazio**; item preenchido sem homologação registrada = eliminatório.

---

## 4. Regras normativas propostas (D2) `[PROPOSTA]`

**Destino no RULES.md (A-02):** as regras abaixo entram como **nova seção "Regras de Herança/Delta (RULE-HD)"** no `governance/RULES.md`, após as seções de RULES existentes, cada uma com `[Fonte: atomic-spec §8.3 / EUA-E04]`. Não alteram nenhuma RULE vigente.

| ID | Regra |
|---|---|
| **RULE-HD-01** | Toda spec de componente e toda Engineering Card DEVE declarar o bloco Herança/Delta (§8.3) com INHERITS e ADDED preenchidos. |
| **RULE-HD-02** | Item em ADDED/MODIFIED NÃO DEVE contradizer item herdado em INHERITS (coerência vertical). Precedência em conflito: PC > PB/PE > regra local (alinha INV-01 e regime PAP). |
| **RULE-HD-03** | Nenhum item herdado PODE ser suprimido fora do campo REMOVED; item em REMOVED sem referência de homologação de Andraus = **NÃO CONFORME Crítica**. |
| **RULE-HD-04** | O bloco NÃO DEVE copiar o conteúdo herdado — apenas **referenciá-lo por ID + VERSÃO baseline**. Referência a versão superseded é achado (sensor de drift). |

---

## 5. Integração com o Constitution Check §10.5 — novo CC-08 `[PROPOSTA]`

| ID | Item | Severidade |
|---|---|---|
| **CC-08** | Bloco Herança/Delta (§8.3) presente; INHERITS/ADDED preenchidos com ID+versão; REMOVED vazio **ou** com homologação registrada; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02) | **Crítica** |

**Regra de verificação (C-HD — Revisor):** o Revisor aplica CC-08 a toda entrega. Falha em INHERITS/ADDED, REMOVED sem homologação, ou contradição vertical = **NÃO CONFORME Crítica**.

---

## 6. Escopo de aplicação (regime híbrido — igual ao PAP-001) `[PROPOSTA]`

Reusa **D-DHR-PAP-001-01** (CATALOGO §7.5):

| Alvo | Regime | Efeito |
|---|---|---|
| Specs novas (SPEC-002 em diante) | **Prospectivo-obrigatório** | Bloco §8.3 obrigatório; gate CC-08 do Revisor |
| Specs já homologadas (SPEC-001, specs de agente) | **Retroativo-como-auditoria** | **Nenhuma reescrita**; ausência do bloco vira Harness Debt registrado no CIC-001, saldável quando a spec for tocada por outro motivo |

Respeita INV-09 (sem reabertura informal de baseline) e evita retrofit big-bang.

---

## 7. Plano de piloto (provar antes de normatizar) `[PROPOSTA]`

**Relação piloto × homologação (A-03):** o piloto **não** é condição para homologar a EUA-E04. A emenda pode ser **homologada com vigência imediata**; o CC-08 passa a valer a partir daí para specs novas. O piloto em SPEC-002 produz a **evidência empírica de auditabilidade** exigida **antes de elevar o `atomic-spec` para v1.5** (incorporação definitiva). Ou seja: homologação da emenda primeiro; piloto como gate para a subida de versão do método.

Sequência:
1. Andraus homologa a EUA-E04 (vigência imediata).
2. Especificador redige SPEC-002 já com o bloco §8.3.
3. Revisor aplica CC-08 no parecer de SPEC-002.
4. Se couber sem atrito e for auditável → Controlador incorpora ao `atomic-spec` **v1.5**.
5. Se surgir atrito de granularidade → calibra-se o bloco antes da subida a v1.5.

---

## 8. Non-goals (limites da emenda) `[PROPOSTA]`

- **Não** importa H0–H4, L0–L4 nem M0–M7 do HCH-001.
- **Não** altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4, harness-score nem Marcos.
- **Não** cria autoridade nova: homologação = Andraus; verificação = Revisor (GRE-001/HRE-001); registro = Controlador.

---

## 9. Pendências para decisão de Andraus `[DECISÃO NECESSÁRIA]`

| # | Questão | Recomendação do Especificador |
|---|---|---|
| P1 | Aprovar código EUA-E04 + inserção §8.3 e CC-08 | Aprovar (padrão EUA-Exx já consolidado) |
| P2 | Escopo prospectivo vs. retroativo | **Híbrido** (§6) — igual ao PAP-001 |
| P3 | RULE-HD-04 referência vs. cópia | **Referência por ID+versão**, cópia proibida |
| P4 | Autorizar piloto em SPEC-002 antes de subir atomic-spec para v1.5 | **Sim** (§7) |

---

## 10. Próximos passos no fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra atomic-spec + baselines
   ↓
Andraus homologa (decide P1–P4)
   ↓
Piloto em SPEC-002 (prova empírica)
   ↓
Controlador incorpora ao atomic-spec (v1.5) + registra HCH-001 no Catálogo + ata DHR
```

---

*PROPOSTA não-homologada. Autoridade literal permanece: `atomic-spec.md` v1.4 + documentos-base. Este arquivo não altera nenhum baseline; existe para auditoria do Revisor e decisão de Andraus.*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** atomic-spec v1.4 · RULES.md v1.1 · CATALOGO-OFICIAL (2026-09-20) · CEE-001 v2.0 · PAP-001 v1.2 · GPR-001 v1.0 · HCH-001 (ref. externa).

**Resumo dos 7 itens:** (1) formato EUA-Exx + encaixe de §8.3 e CC-08 no template/§10.5 — PASS; (2) RULE-HD-01..04 coerentes com RULES.md, ENF-03, INV-01, INV-09 — PASS; (3) **nenhuma colisão** (não importa H0–H4, L0–L4, M0–M7, "3Es"; preserva Quality Gates L1–L4, harness-score, Marcos, 4Es) — PASS; (4) escopo híbrido fiel a D-DHR-PAP-001-01 e a INV-09 — PASS; (5) RULE-HD-04 auditável, sensor de drift real — PASS; (6) etiquetagem TRACE-06 e CONS-01 — PASS; (7) achados apenas Menores.

**Achados Menores e tratamento:**

| ID | Achado | Tratamento |
|---|---|---|
| A-01 | Classificação do HCH-001 aprovada em sessão; registro formal do Controlador pendente | **Pendente** — ato do Controlador (Catálogo/CONFLICT-MAP); não bloqueia |
| A-02 | RULE-HD sem seção-destino no RULES.md | **Acatado** — §4 agora define nova seção "Regras de Herança/Delta (RULE-HD)" |
| A-03 | Relação piloto × homologação ambígua | **Acatado** — §7 esclarece: homologação imediata; piloto como gate para subir a v1.5 |

**Recomendação do Revisor:** autorizar o piloto em SPEC-002 antes de elevar o `atomic-spec` a v1.5.

**Encaminhamento:** CONFORME → pronto para homologação de Andraus (decisões P1–P4, §9). O parecer não homologa; atesta integridade.

