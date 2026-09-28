# MAN-001 — Mapa da Arquitetura Normativa (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **MAN-001** |
| Natureza | Artefato de governança transversal (camada de convergência horizontal entre Master Contracts) |
| Status epistemológico | **HOMOLOGADO — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-MAN-001`). Vigência imediata. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Origem conceitual | CMHP-001 (`CAMADA PRINCIPIOLÓGICA.MD`) §11–16, §38–39, §66–68, §79–80 — importada **só a mecânica** de convergência horizontal; **sem** os rótulos L0–L6 e I-01..12 (colidem — ver §5) |
| Fundamento no baseline | GPR-001 v1.0 §13 (cadeia vertical de documentos); CONFLICT-MAP (F.1); RCH-001 (ciclo de Hygiene); atomic-spec v1.4 (F.1–F.4) |
| Função | Registrar os Master Contracts do repo como **nós normativos**, suas **interfaces** e **convergências**, e prover **sensor de drift horizontal**. Preenche o único delta real da auditoria CMHP-001. |
| O que NÃO é | Não é segunda constituição; não reescreve GPR-001, atomic-spec nem CONSTITUTION; não cria classe/rótulo de princípio novo. |

---

## 1. Propósito `[INFERÊNCIA]`

O SOT já governa princípios **verticalmente** (GPR-001 v1.0: classes, relações, matrizes, organicidade). O que **não** existe é a governança **horizontal** entre os múltiplos documentos de nível-mestre do repo. Sem ela, um master contract novo pode colidir com baselines sem que nenhum mecanismo detecte — foi o que ocorreu com o HCH-001 (colisões L/M/3Es só pegas por auditoria manual). O MAN-001 torna essa convergência **explícita, registrada e auditável**.

> Regra de ouro adotada (CMHP-001 §81): *master contracts devem convergir sem se fundir; níveis inferiores especializam sem perder origem*.

---

## 2. Nós da Arquitetura Normativa (Master Contracts governados) `[FONTE]`

Cada nó é referenciado por **ID + versão baseline** (disciplina RULE-HD-04, homologada em EUA-E04).

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N1 — Constitucional** | CONSTITUTION (F.1 baselined) | Invariantes-raiz (PC-xx co-extensivos) | `governance/CONSTITUTION.md` |
| **N2 — Principiológico** | GPR-001 v1.0 | Classes, relações, matrizes e organicidade dos princípios | `governance/GPR-001_…md` |
| **N3 — Estrutural / Modelos** | GMC-001 v1.0 · CEM-001 v1.0 · CHM-001 v1.0 · SAS-001 v1.0 | Contratos canônicos de Evidência/Hipótese/Agente | `canon/` |
| **N4 — Método / Harness de Spec** | atomic-spec v1.4 (F.1–F.4, E0–E3, D0–D9) + EUA-E04 (Herança/Delta) | Como se especifica, verifica e faz enforcement | `atomic-spec.md` |
| **N5 — Econômico** | CEE-001 v2.0 (§12 4Es, §10/§11 Salvaguardas) | Economia/eficiência cognitiva | `canon/CEE-001-…v2.0.md` |
| **N6 — Especialização de Domínio** | SES-001 v1.0 | Overlay de Trading (regra superior às specs) | `governance/SES-001_…md` |
| **N7 — Adesão / Inventário / Backlog** | PAP-001 v1.2 · CIC-001 v1.3 · RMR-001 v1.0 | Maquinário de adoção e rastreabilidade (Trilha A) | `governance/`, `backlog/` |
| **N8 — Epistêmico** *(DHR-EUA-E05)* | atomic-spec v1.4 §11 (TRACE-06) + EUA-E05 | Status epistemológico das afirmações; anti-conversão; incerteza/abstenção (INDETERMINADO); INV-EPI | `atomic-spec.md` |
| **N9 — Semântico** *(DHR-EUA-E06)* | GLOSSARIO v1.0 + EUA-E06 (SES-001 §11) | Sentido dos termos; terminologia concorrente por escola; transparência semântica; drift semântico | `GLOSSARIO.md` |
| **N10 — Ontológico** *(DHR-EUA-E07)* | CEM-001 v1.0 / CHM-001 v1.0 + EUA-E07 | O que existe no domínio; observacional vs teórico; autoexpansão governada. Substância nos Modelos Canônicos (CCM/CDM/CNM) | `canon/` |
| **N11 — Inquérito** *(DHR-EUA-E08)* | GEH-001 v1.1 + EUA-E08 | Como investigar: questão→método; evidência discriminante; critério de encerramento (→ INDETERMINADO). Sensores operacionais no harness-eval/GEH | `atomic-spec.md` / `RETOMADA/` |
| **N12 — Causal** *(DHR-EUA-E09)* | RULE-EPI-02 + EUA-E09 | Causa→efeito: mecanismo obrigatório; regime de validade; guard pós-hoc. Intervenção/contrafactual → nó futuro; vocabulário estatístico → CCM | `atomic-spec.md` |
| **N13 — Contrafactual** *(DHR-EUA-E10)* | RULE-CAU-03 + EUA-E10 | Mundos alternativos: baseline; intervenção mínima; anti-hindsight; invalidação. Qualificação probabilística e árvores diferidas | `atomic-spec.md` |
| **N14 — Incerteza** *(DHR-EUA-E11)* | PB-10 + EUA-E11 | Localizar/tipificar a incerteza; não-contaminação; incerteza≠probabilidade. Calibração/sensibilidade → Conviction/CCM (J-001 aberto); quantificação → Probabilística | `atomic-spec.md` |
| **N15 — Probabilística** *(DHR-EUA-E12)* | RULE-UNC-03 + EUA-E12 | Evento probabilístico bem-formado; não quantificar sem base. Calibração/risco/priors/distribuição → Conviction/CCM (J-001 aberto); decisão → Decisional | `atomic-spec.md` |
| **N16 — Decisional** *(DHR-EUA-E13)* | INV-05 + EUA-E13 | Decisão ≠ execução + autoridade declarada (recomendação/TMP, não execução); decisão condicional (→ INDETERMINADO); qualidade do processo ≠ resultado. Modelagem decisional (multicritério/utilidade/robustez/opcionalidade) → CDM-001 (pendente) + Synthesis Agent (J-001 aberto); vieses → Metacognição | `atomic-spec.md` |
| **N17 — Metacognição** *(DHR-EUA-E14 · transversal/2ª ordem)* | TRACE-06 + EUA-E14 | Auto-observação/autorregulação do processo cognitivo: honestidade/não-fabricação; abstenção produtiva (anti-censura); autonegação/revisibilidade. **Monitora N8–N16** — não introduz domínio novo. Calibração → CCM-001 (J-001 aberto); sensores de runtime → harness-eval/GEH; especialização → SES-001 | `atomic-spec.md` |

**Camadas §68 (MSC-001) — TODAS FECHADAS:** ~~Ontologia (→ N10)~~ · ~~Inquérito (→ N11)~~ · ~~Causalidade (→ N12)~~ · ~~Contrafactuais (→ N13)~~ · ~~Incerteza (→ N14)~~ · ~~Probabilística (→ N15)~~ · ~~Decisional (→ N16)~~ · ~~Metacognição (→ N17, transversal)~~. **Fim do ciclo de camadas cognitivas.** N17 é o único nó transversal / de 2ª ordem (atua sobre o funcionamento de N8–N16).

**Referências externas NÃO-normativas (não são nós):** GEH-001 v1.1 (pano de fundo de harness), HCH-001 (harness), CMHP-001 (principiológico), MEG-001 (epistêmico), MSC-001 (semântico), MOC-001 (ontológico), MIQG-001 (inquérito), MCC-001 (causal), MCF-001 (contrafactual), MUN-001 (incerteza), MPB-001 (probabilística), MDC-001 (decisional), MC-001 (metacognição). Emprestam mecânica; não governam. **Localização: `reference/camadas/`** (HOD-001/F1, 2026-09-21; ver Mapa de Pastas no CATALOGO §0).

---

## 3. Interface Normativa por nó (CMHP-001 §39) `[INFERÊNCIA]`

Formato: **Fornece** (saídas normativas) · **Recebe** (entradas) · **Invariantes compartilhadas** · **Converge com**.

- **N1 Constitucional** — Fornece: PC-01..PC-08 (invariantes absolutos). Recebe: nada (raiz). Compartilha: hierarquia analítica, SOT≠execução. Converge com: todos.
- **N2 GPR-001** — Fornece: gramática de relações, matrizes de conflito, fichas de princípio. Recebe: PC-xx de N1; 4Es de N5. Compartilha: classes PB/PE/PCO/PO/PS. Converge com: N1, N4, N5.
- **N3 Estrutural** — Fornece: CEM/CHM/SAS (contratos canônicos). Recebe: PC-03/PC-05 de N1. Compartilha: Evidência≠Observação. Converge com: N4 (specs consomem contratos), N6.
- **N4 Método/Harness** — Fornece: BASpec, D0–D9, E0–E3, F.1–F.4, CC-01..08, bloco Herança/Delta. Recebe: princípios de N2, contratos de N3, 4Es de N5, overlay de N6. Compartilha: proporcionalidade, determinístico-first. Converge com: todos.
- **N5 CEE-001** — Fornece: 4Es (Eficácia→Efetividade→Eficiência→Economicidade), Salvaguardas. Recebe: PB-01..04 de N2. Compartilha: economicidade não rebaixa proteção. Converge com: N2, N4.
- **N6 SES-001** — Fornece: 17 campos de EC + cadeia de derivação (§60). Recebe: método de N4; contratos de N3. Compartilha: não-restrição cognitiva (§50). Converge com: N4, N3.
- **N7 PAP/CIC/RMR** — Fornece: regime de adesão (D-DHR-PAP-001-01), inventário, backlog. Recebe: princípios de N1/N2. Compartilha: sem baseline informal (PC-08/INV-09). Converge com: N2, N4.

---

## 4. Matriz de Convergência (relações horizontais) `[INFERÊNCIA]`

| Par | Relação | Ponto de convergência | Conflito potencial |
|---|---|---|---|
| N1 ↔ N2 | Fundação | PC-xx co-extensivos aos invariantes | — (N2 declara não ser 2ª constituição) |
| N2 ↔ N5 | Convergência | 4Es = PB-01..04 (mesma ordem) | ordem dos Es deve permanecer idêntica |
| N2 ↔ N4 | Propagação | Constitution Check (CC) aplica princípios | princípio sem sensor no método |
| N3 ↔ N4 | Dependência | specs consomem contratos canônicos | spec redefinir contrato (proibido) |
| N4 ↔ N5 | Complementação | economicidade não rebaixa E-nível | economicidade violar hierarquia (AP-06) |
| N4 ↔ N6 | Especialização | overlay SES sobre o método | overlay contradizer método |
| N1/N2 ↔ N7 | Governança | homologação/registro | baseline informal (PC-08) |

**Precedência horizontal em conflito (herda GPR §3.2):** `N1 (PC) > N5 4Es/N2 PB > N4 método > N6 overlay > specs`.

---

## 5. Conflitos conhecidos registrados (inclui achados de auditoria) `[FONTE]`

| # | Origem | Conflito | Estado |
|---|---|---|---|
| K-MAN-01 | HCH-001 (ref externa) | Rótulos H0–H4, "3Es+Economicidade", L0–L4, M0–M7 colidem com 4Es/Quality Gates L1–L4/harness-score/Marcos | **Registrado** (CONFLICT-MAP, DHR-EUA-E04). Não adotar rótulos; só a mecânica (EUA-E04). |
| K-MAN-02 | CMHP-001 (ref externa) | Rótulos **L0–L6** (§8) colidem com Quality Gates L1–L4 / harness-score L0–L4 / maturidade GPR L0–L5; **I-01..I-12** (§72) sobrepõem INV/PC/PB/HCH-INV | **Registrado aqui.** Importar só a mecânica de convergência; não criar namespace novo. |
| K-MAN-03 | N2 ↔ N5 | Risco de a ordem dos 4Es divergir entre GPR-001 e CEE-001 | Monitorar no Hygiene (ambos hoje idênticos: Eficácia→Efetividade→Eficiência→Economicidade). |

---

## 6. Sensor de Drift Horizontal — enxerto no Hygiene (RCH-001) `[PROPOSTA]`

Em vez de maquinário novo, adicionar **um passo** ao ciclo de Hygiene já existente (RCH-001):

```
HYGIENE — Passo novo: Convergência Horizontal (MAN-001)
  Para cada nó (N1..N7) alterado desde o último ciclo:
    1. conferir se as Invariantes Compartilhadas (§3) continuam consistentes com os pares;
    2. conferir se nenhuma alteração introduziu conflito não governado (§4/§5);
    3. divergência → abrir FLAG no RCH-001 + item no CIC-001 (Harness/Normative Debt);
    4. colisão de rótulo com baseline → NÃO CONFORME (bloqueia adoção).
```

Isso materializa CMHP-001 §66–68 (drift) reusando o mecanismo homologado, ao menor custo (economicidade).

---

## 7. O que NÃO integrar (já temos / colide) `[FONTE]`

| Do CMHP-001 | Motivo |
|---|---|
| UNP (§7), classes/hierarquia (§8), relações (§10) | Já em GPR-001 §1/§2/§3/§5/§6 e §12 (ficha) |
| Propagação vertical / herança (§17–19) | Já em EUA-E04 (bloco Herança/Delta) |
| Rótulos L0–L6 (§8), I-01..12 (§72) | Colidem (K-MAN-02); manter Quality Gates L1–L4, INV, PC/PB, Marcos |
| Escada Valor→…→Ação (§6), 85 seções | Excesso; violaria necessidade-e-suficiência (CMHP §43) |

---

## 8. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Classificar CMHP-001 como referência externa não-normativa (igual HCH-001/GEH-001) | **Sim** |
| Q2 | Aprovar MAN-001 como o único artefato novo (mapa de convergência horizontal) | **Sim** |
| Q3 | Enxertar o sensor de drift horizontal no Hygiene (RCH-001) | **Sim** |
| Q4 | Nome/código do artefato (MAN-001) e localização (`governance/`) | Confirmar |

---

## 9. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra GPR-001, atomic-spec, CONFLICT-MAP, RCH-001
   ↓
Andraus homologa (decide Q1–Q4)
   ↓
Controlador registra MAN-001 no Catálogo + classifica CMHP-001 (K-MAN-02) + wire do passo no RCH-001
```

---

*PROPOSTA não-homologada. Não altera nenhum baseline; existe para auditoria do Revisor e decisão de Andraus. Referências por ID+versão (RULE-HD-04, EUA-E04 homologada).*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · GPR-001 v1.0 · atomic-spec v1.4 (+EUA-E04) · CATALOGO-OFICIAL (2026-09-20) · CONFLICT-MAP · CEE-001 v2.0 · PAP-001 v1.2 · RCH-001 · CMHP-001 (ref. externa).

**Resumo dos 7 itens:** (1) Nós N1–N7 — IDs+versões conferem com o Catálogo, nenhum ausente/sobrando/errado — PASS; (2) precedência horizontal coerente com GPR-001 §3.2 e CEE-001 §12; N5 (4Es) e N2 (PB-01..04) co-extensivos e no mesmo patamar — PASS; (3) sem colisão de namespace (evita L0–L6 e I-01..12) e sem recriar UNP/classes/herança; não é 2ª constituição — PASS; (4) K-MAN-01/02/03 consistentes com o CONFLICT-MAP (K-MAN-02 = registro novo válido do CMHP-001) — PASS; (5) sensor de drift no Hygiene proporcional, alinhado a ENF-03 e PC-08/INV-09 — PASS; (6) etiquetagem TRACE-06 e CONS-01 corretas — PASS; (7) apenas 1 achado Menor.

**Achado Menor e tratamento:**

| ID | Achado | Tratamento |
|---|---|---|
| A-01 | SAS-001 sem versão inline no formato uniforme da célula N3 | **Acatado** — N3 agora lista `GMC-001 v1.0 · CEM-001 v1.0 · CHM-001 v1.0 · SAS-001 v1.0` |

**Recomendação do Revisor (Q1–Q4):** concorda com todas — classificar CMHP-001 como referência externa não-normativa; aprovar MAN-001 como único artefato novo; enxertar o sensor de drift no RCH-001; código/localização `governance/`.

**Encaminhamento:** CONFORME → pronto para homologação de Andraus (decisões Q1–Q4, §8). O parecer não homologa; atesta integridade.
