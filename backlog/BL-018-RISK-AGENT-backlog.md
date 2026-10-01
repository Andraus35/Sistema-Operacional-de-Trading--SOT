# BL-018 — Risk Agent SOT (Família RISK-SPEC)

> **Renumerado de BL-017 → BL-018 (Andraus 2026-09-22, C-01):** BL-017 já está ocupado no RMR-001 pelas "dimensões B da SPEC-020". Este item é BL-018.

> Item para inserção no `backlog/RMR-001_Painel_Backlog.md` — formato padrão §6.
> Status inicial: `Proposto` → aguarda homologação de Andraus para `Em espera`.

---

## Linha para o Registro Vivo (RMR-001 §6)

| Campo | Valor |
|---|---|
| **ID** | BL-018 |
| **Título** | Risk Agent SOT — Família RISK-SPEC (elo final de análise para execução) |
| **Tipo** | Módulo diferido |
| **Origem** | Sessão de design Andraus × Claude 2026-09-22 · `reference/SOT-RISK-MASTER-001_Consolidado.md` · Parecer Claude Code 2026-09-22 (`docs/arranque/PARECER-RISK-AGENT-auditoria-semantica.md`) |
| **Afeta** | Trilha B (Cognitiva/Operacional) · CONSTITUTION P14 · atomic-spec INV-05 · GLOSSARIO · AGENTS · ROADMAP · synthesis.spec · CHUNK-SY-007 · D-ARR-001 (sem artefato no repo) · Decisões abertas: J-001, CDM-001, I-001, M-001 |
| **Gatilho de Ativação** | `spec:EUA-E19a homologada` ∧ `milestone:FASE 6 (Synthesis) concluída` |
| **Ação ao ativar** | Especificador redige RISK-SPEC-001 (Princípios de Risco RP1–RP15) seguindo a ordem Grupos A→B→C→D→E→F→G→H; herança via RULE-HV-01..04 declarada nas Specs dos Grupos A e B (e na RISK-SPEC-023 herdando SPEC-020); RISK-SPEC-020 verifica INV-RISK-00 (isolamento epistêmico) como pré-condição; RISK-SPEC-022 (Signal Package) permanece com contrato em aberto até D-RISK-SP-001 ser resolvida |
| **Estado** | `Em espera` (promovido de `Proposto` na homologação da EUA-E19a — DHR-EUA-E19a, 2026-09-22; 1ª condição do gatilho composto satisfeita, resta `milestone:FASE 6 concluída` para ativação plena). Espelha `backlog/RMR-001_Painel_Backlog.md` (fonte de verdade). |

---

## Contexto rico (para o Especificador ao ativar)

### O que é o Risk Agent

Agente cognitivo CRITICAL, elo final de análise antes da execução. Posição no pipeline:

```
Synthesis → [TMP interno] → Risk Agent → Risk Harness → Signal Package → Bot Finance
```

Não é calculador de R:R nem filtro de sinais. É entidade cognitiva especializada em decisão sob risco e incerteza, com autoridade para ACCEPT / WAIT / REJECT / ABSTAIN.

### Decisões arquiteturais de Andraus (2026-09-22) — aguardam EUA-E19

- **D-RISK-01:** Risk Agent **consolida** RULES de R:R vigentes (RULE-006/RULE-ICT-002/CEE-001 §11 Salv.5 — R:R ≥ 1:3 risco:retorno = 3:1 retorno:risco) e **institui** invariantes novos (risco dinâmico/alavancagem; Portfolio Heat ≤ 15%). **Zero linguagem de supersedação do ARR** enquanto RISK-ARR-LOC-001 estiver aberta — ARR não existe no repo como componente formal (F-01). (C-09, Andraus 2026-09-22.)
- **D-RISK-02:** Pipeline atualizado — TMP vira artefato interno; Signal Package é a nova fronteira.
- **D-RISK-03:** Signal Package serve a dois receptores: Bot Finance (logística financeira) + humano/Andraus (execução do trade). Contrato exato = D-RISK-SP-001 (aberta, diferida à RISK-SPEC-022).
- **D-RISK-04:** Bot Finance faz logística financeira. Trading executado pelo humano.
- **D-RISK-05:** INV-05 atualizada — "SOT não executa, produz Signal Package via Risk Harness". Impacta 6 loci (ver Parte I §D-RISK-05 do Master Document).

### Achados críticos do parecer (Claude Code, 2026-09-22)

**F-01 — ARR é fantasma no repo.** Não existe D-ARR-001 no repositório. A absorção consolida RULES existentes (RULE-006/RULE-ICT-002/CEE-001 §11 Salv.5) + adiciona dois invariantes genuinamente novos (Portfolio Heat e alavancagem dinâmica). Não há supersedação de ata.

**F-02 — "Signal Package" é o termo fundacional.** ENGENHARIA-GERAL Doc03 §20 usa "Signal Package" como termo original. TMP foi introduzido depois. D-RISK-03 restaura o termo fundacional — argumento forte para a emenda de P14.

**F-03 — 11 das 14 camadas herdam N8–N17** (contagem unificada pela tabela §3.2 do Master — C-07). As camadas #2–#12 mapeiam sobre N8–N17 já homologadas. Delta genuíno = **3 camadas**: #1 Principiológica (RP1–RP15), #13 Quantitativa (VaR/CVaR/drawdown), #14 Risco–Retorno. Specs dos Grupos A e B declaram herança via RULE-HV-01..04, não recriam.

**F-07 — EUA-E17 já homologada.** FASE GOV está fixa. FASE RISK posiciona-se após FASE 6 (Synthesis) sem conflito.

**INV-RISK-00 — Isolamento epistêmico (pré-condição, Andraus 2026-09-22).** Workspace isolado; input só via handoff tipado imutável do TMP; Risk Agent nunca lê/escreve no Blackboard; Signal Package não realimenta o pipeline analítico. Ancora em RISK-SPEC-020 (Risk Harness), RISK-SPEC-022 (Signal Package) e SPEC-016 repurposada. Fundamento: challenge só é independente sem acesso ao processo que gerou a conclusão (ref. AgenticAITA 2026, ~3,2% rejeição = challenge genuíno).

### Pré-requisito: EUA-E19a (antes de qualquer RISK-SPEC)

A **EUA-E19a** (fatiada — C-03) deve preceder todas as RISK-SPECs. Escopo mínimo:
1. Emenda à CONSTITUTION P14 + convergência horizontal dos 6 loci de INV-05 — **SEM menção ao Risk Harness** ("via Risk Harness" entra quando RISK-SPEC-020 for homologada)
2. Reconciliação semântica TMP (interno) / Signal Package (fronteira) com registro RULE-SEM da terminologia concorrente
3. Consolidação de R:R ≥ 1:3 (risco:retorno = 3:1 retorno:risco) + instituição de Portfolio Heat ≤ 15% + alavancagem como invariantes mínimos do Risk Agent

### Família de Specs proposta

**23 Specs** em 8 Grupos: Fundamento (4) → Cognição (5) → Decisão (4) → Quantificação (3) → Memória+Metacognição (3) → Operacionalização (3) → Skills (diferidas a I-001) → Avaliação (1 — Grupo H fundido, RISK-SPEC-023 herda SPEC-020, C-08).

Ver estrutura completa em `reference/SOT-RISK-MASTER-001_Consolidado.md` §6.2.

> **Atualização DHR-EUA-E20 (2026-10-01) — FASE RISK instituída com 6 macro-slots indicativos.** A família passa a ser representada no ROADMAP (§10-bis) por **6 macro-slots INDICATIVOS** (RULE-ECC-01/02), não por 23 slots numerados: **RISK-M1** (Fundamento & Cognição = Grupos A+B, RISK-SPEC-001..009) · **RISK-M2** (Decisão & Risco-Retorno = Grupo C, RISK-SPEC-010..013; fecha RISK-CONV-001 em RISK-SPEC-010; ancora INV-RISK-RR/HEAT/LEV) · **RISK-M3** (Quantificação & Stress = Grupo D, RISK-SPEC-014..016) · **RISK-M4** (Memória/Aprendizado/Metacognição = Grupo E, RISK-SPEC-017..019) · **RISK-M5** (Operacionalização = Grupo F, RISK-SPEC-020..022; "via Risk Harness" entra em RISK-SPEC-020; ancora INV-RISK-00 + SPEC-016/TMP) · **RISK-M6** (Avaliação = Grupo H, RISK-SPEC-023, herda SPEC-020 via RULE-HV). Skills (Grupo G) diferidas a I-001 (FECHADA)/SPEC-025. **Cobertura integral dos 23 RISK-SPEC preservada** (nenhuma capacidade descartada). **Estado permanece `Em espera`:** a EUA-E20 institui a FASE (direção), **não autoriza** a família — o gatilho composto `spec:EUA-E19a homologada ∧ milestone:FASE 6 (Synthesis) concluída` ainda não está plenamente satisfeito. **Re-interpretação do milestone (DHR-ARQ-002):** "FASE 6/Synthesis concluída" = **Manager — Fase 2 (Convicção & Síntese, SPEC-014 repurposado) homologada**; o gatilho será **re-apontado** na autorização da família (não fechado aqui; CONS-01). Decisões abertas RISK-ARR-LOC-001/RISK-CONV-001/J-001/D-RISK-SP-001/CDM-001 **continuam abertas**.

### Decisões abertas a vigiar (CONS-01)

| ID | Questão | Trava |
|---|---|---|
| D-RISK-SP-001 | Contrato exato do Signal Package | RISK-SPEC-022 |
| RISK-ARR-LOC-001 | Escopo preciso da absorção do ARR na EUA-E19 | EUA-E19 |
| RISK-CONV-001 | "Convicção de Risco" vs. Conviction Vector 8D (J-001) | RISK-SPEC-010 |
| CDM-001 | Idioma canônico do RDR (objeto de decisão) | RISK-SPEC-021 |
| J-001 | Limiares definitivos do Conviction Vector | RISK-SPEC-009/010 |
| I-001 | Skills como unidades formais | RISK-SPEC-SKL-* |

### Referência documental

- `reference/SOT-RISK-MASTER-001_Consolidado.md` — documento completo desta sessão
- `docs/arranque/PARECER-RISK-AGENT-auditoria-semantica.md` — parecer do Claude Code
- Padrão de herança: EUA-E04..E16, DHR-MC-RAG-001..SKL-001 (BL-010..016)
- Padrão de família de Specs: SPEC-001..025 no ROADMAP

---

## Ato de admissão (para o Claude Code preencher após homologação)

```
Etapa 1 — Triagem de conformidade ..... [ ] Especificador — sem ata dedicada (ver nota abaixo)
Etapa 2 — Registro do item ............ [x] BL-018 registrado em `Proposto` no RMR-001 (2026-09-22)
Etapa 3 — Parecer de integridade ...... [ ] Revisor SOT — sem parecer dedicado (ver nota abaixo)
Etapa 4 — Consenso .................... [ ] Andraus (Decisor Final) — ver nota abaixo
Etapa 5 — Registro Oficial ............ [ ] Controlador — ver nota abaixo
```

**Nota sobre a promoção `Proposto`→`Em espera` (2026-09-22):** não houve um Ato de admissão dedicado nos moldes das Etapas 1/3/4/5 acima (sem ata própria de triagem/parecer/consenso só para BL-018). A promoção ocorreu pelo mecanismo do **Passo 11-bis** do ROADMAP §23 (RMR-001 §4/§5): o gatilho `spec:EUA-E19a homologada` disparou como efeito colateral da homologação da própria EUA-E19a (DHR-EUA-E19a, 2026-09-22), e o painel vivo registrou a promoção nesse gate (ver `backlog/RMR-001_Painel_Backlog.md`, nota do Passo 11-bis). Isto é válido pelo próprio desenho do RMR-001 (o Passo 11-bis existe exatamente para não exigir um ciclo completo de admissão por item quando o gatilho já dispara por uma homologação maior) — mas por honestidade epistêmica (RULE-MET-01/TRACE-06) as caixas acima não são marcadas como se um Ato de admissão dedicado tivesse ocorrido.

---

*Produzido por Claude (claude.ai) em sessão com Andraus (2026-09-22).*
*Aguarda homologação de Andraus para entrar no RMR-001 como `Em espera`.*
