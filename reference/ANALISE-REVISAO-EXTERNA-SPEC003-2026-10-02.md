# ANÁLISE CRÍTICA DA REVISÃO EXTERNA DA SPEC-003 (LLM externo) — 2026-10-02

> **Natureza:** análise não-normativa, [INFERÊNCIA] do orquestrador com evidência do repositório [FONTE] e externa [EXTERNO]. Não altera a SPEC-003 nem decide nada (CONS-01). Objeto: revisão "SPEC-003 como Harness para LLM" colada por Andraus (LLM sem o contexto completo do projeto). Referência da Spec auditada: `specs/features/SPEC-003/plan.md` v1.4 (candidata).

## 1. Veredito

A revisão externa **acerta no essencial** (a Spec é um contrato forte e o LLM nunca é o gate) e **erra em três pontos por falta de contexto** (cadeia/contrato de saída/estado já existem; taxonomia de autoridade duplicaria a Classe D/H/P/C; "Harness global" já tem donas no ROADMAP). Duas ideias dela são **válidas e aproveitáveis a baixo custo**. Mais importante: **ela e o nosso Revisor deixaram passar três lacunas reais do "cérebro decisório"** (§4), que só aparecem lendo a Spec contra o canon.

## 2. Onde a revisão ACERTA (com prova)

| Afirmação do LLM externo | Prova no projeto | Prova externa |
|---|---|---|
| LLM é detector, nunca o gate | `plan.md:606-607` (CF-012: "LLM nunca é o gate, ENF-03"); `plan.md:840-843` (ADV-CF-08 `LLM_IS_NOT_GATE`); `RULES.md:515` (Classe H DEVE declarar gate determinístico) | arXiv 2609.02246 (Wahi, set/2026): o juiz LLM deve ser "rebaixado de oráculo a conselheiro", com camada determinística que ele não pode sobrescrever [EXTERNO, preprint — verificado] |
| Observáveis/D8 transformam princípio em propriedade verificável | `plan.md:452` (`compensated_by_lower_dims == false`), `:501` (`fabricated_value == false`), `:808-824` | — |
| Garantias críticas devem estar em código/schema, não em prompt | EC-CF-005 E3 fail-closed (`plan.md:1010-1022`) | arXiv 2607.08028 (Ahn & Kim, jul/2026): mover comportamento determinístico "para código, manifestos, schemas e validação" [EXTERNO — verificado] |
| Validar saída antes de uso downstream; menor privilégio; autorização fora do LLM | INV-05; CF-013 ("nenhuma chamada externa", `plan.md:623-640`) | OWASP AI Agent Security Cheat Sheet §1 (least privilege), §4 (separar decisão de execução; política independente), §5 (validar saída/schema) [EXTERNO — verificado] |
| Planejamento validado contra schema dá determinismo | `plan.md:915-950` (esquema CCM-001) | arXiv 2608.26197 (Dhage, ago/2026): reprodutibilidade/determinismo 1.000 em 3 de 4 células com planejamento estruturado validado; custo de latência dependente de modelo [EXTERNO — verificado] |
| Spec é contrato, não runtime | `AGENTS.md` §1 "Spec-first — BUILD/VERIFY adiados"; `plan.md` Tasks adiadas | — |

Nota de honestidade (RULE-MET-01): os três arXiv são **preprints** (autores individuais/pequenos), com tema **LLM-agents corporativos**, não trading. Servem para a *direção* arquitetural, não como prova de eficácia no SOT.

## 3. Onde a revisão ERRA ou superestima (por falta de contexto)

| # | Afirmação | Por que está errada/parcial | Prova |
|---|---|---|---|
| E1 | "Cadeia Schema→Semântico→Invariante→Gate→Estado→Persistência não está fechada" | **Parcial.** A cadeia existe: pipeline de 11 passos, esquema I/O, 6 Enforcement Contracts (PRECOND/POSTCOND/FAILURE-MODE/EVIDENCE) e máquina de estados. O que falta é **quem intercepta** (ponto de interceptação), e isso pertence a Specs de runtime já previstas (SPEC-018/K-001, SPEC-045, Manager Contract/EUA-E23), não a SPEC-003 | `plan.md:691-703` (D6), `:915-950`, `:956-1035` (ECs), `:665-678` (D5); `ROADMAP` SPEC-018/045; DHR-EUA-E23 |
| E2 | "Falta um Output Contract único" | **Errada como afirmada.** O objeto Conviction Vector (CCM-001) já é o contrato de saída, com `status`, `gate_result`, `thresholds_used`, `reconstruction`, `source_evidence_ids`. Lacuna real é menor: não registra **quem computou** cada campo (`computed_by`) nem um `gate_record` explícito no objeto | `plan.md:917-950`; `EC-CF-005 EVIDENCE: gate_record` (`:1020`) |
| E3 | "Adicionar taxonomia AUTHORITY MODE (LLM / LLM_PROPOSE / DETERMINISTIC / HUMAN)" | **Duplicaria** a Classe D/H/P/C + ENF-03 (D=determinístico; H=julgamento + gate determinístico; P=probabilístico + gate; C=constitutivo; HUMAN = Andraus). Criar 2ª taxonomia contraria o pedido de higiene sem duplicação. O que vale é **explicitar a semântica "o Harness recomputa"** dentro da Classe H (ver R3) | `RULES.md:515-517`; `plan.md:441-447`; RULE-MECH-01..04; DHR-CLASSE-MECH-001 |
| E4 | "Capability boundary ausente" | **Parcial.** INV-05 + "workspace próprio" (EC-CF-006) + CF-013 já restringem efeito; falta uma **declaração negativa explícita** (o que o mecanismo NÃO pode chamar). A allowlist concreta de ferramentas por agente é de runtime (SPEC-018/045), não da Spec de convicção | `plan.md:1024-1035`; INV-05 |
| E5 | "Harness global para evitar floresta de validadores" | **Direção certa, mas já tem dono** no repo: camada de Enforcement (atomic-spec §10, E0–E3), SPEC-019 (policy), SPEC-018/K-001 (governança runtime), SPEC-045 (caminho de leitura runtime), BL-013. A lacuna real é **a ausência de um campo "ENFORCER/ponto de interceptação" no Enforcement Contract** (emenda única no método, não 1 validador por Spec) | `atomic-spec.md` §10; ROADMAP §12/§20 |
| E6 | "Não adicionar mais regras cognitivas agora" | **Errada para o objetivo do Andraus (qualidade de trading).** A revisão avalia "quão Harness", não "quão boa é a lógica de convicção para operar". Há lacunas de domínio (§4) que só se veem contra o canon | §4 |
| E7 | Tratar "implementação física 🔴" como fraqueza | Está **deliberadamente adiada** (spec-first); não é defeito da Spec | `AGENTS.md` §1 |

## 4. Lacunas REAIS que NENHUM dos dois revisores apontou (o ponto de maior valor)

| # | Achado (trading / cérebro decisório) | Evidência | Severidade |
|---|---|---|---|
| **N1** | **O gate E3 depende de `score ≥ 7/9`, mas a SPEC-003 nunca define o que é o "score" nem de onde vêm os "9"**. O score 0–9 vem da 1ª geração (cada agente especialista pontuava 0–3; Synthesis somava → 0–9) e coexiste com o Conviction Vector 8D como "filtro paralelo PILOT" (H-16). Com 8 dimensões e a nova taxonomia (Estrutural/Institucional/Operacional + Manager), **a quantidade que o gate avalia está indefinida** | `plan.md:604,658,943` (`"score": "n/9"` sem fórmula); `.claude/agents/sot-spec-reviewer.md:34` ("0-3 per agent, 0-9 total"); `AUDITORIA-HIGIENE… H-16`; GLOSSARIO l.92; CEE-001 §11 item 2 | **Maior** |
| **N2** | **CC-04 afirma que o gate CF-012 preserva as 5 Salvaguardas de Sinal, mas o gate só verifica 3 condições** (convicção, score, conflito). A Salvaguarda 1 ("hipótese sem nível de invalidação explícito → bloqueada") **não está em CF-012/EC-CF-005** — ou a Spec corrige a afirmação ou inclui a pré-condição | `plan.md:54` (CC-04) × `:603-605` (CF-012) × CEE-001 §11 item 1 | **Maior** |
| **N3** | **Proveniência da entrada do gate:** o gate (Classe C) compara `global_conviction`, mas esse número é produzido pelo mecanismo de agregação (Classe H, com julgamento qualitativo). Não está dito que o gate **recomputa/valida** o número a partir das notas por dimensão persistidas. Sem isso, o "gate determinístico" pode apenas comparar um número que o LLM propôs. **Aqui a revisão externa tem razão** (princípio "LLM propõe, Harness verifica") | `plan.md:441-447` (CF-005 H), `:598-614` (CF-012 C), `:941-946` | **Médio** |
| N4 | **Semântica do "70%":** é score normalizado, não probabilidade (RULE-PRB-02). Se o operador o ler como probabilidade, precisa de calibração (confiabilidade/Brier) — hoje só prevista de forma genérica em J-001. Registrar no WORKFLOW/CCM-001 que **70% ≠ 70% de chance** até a calibração pós-backtest | RULE-PRB-02; AGENTS §6.6; J-001 aberta [INFERÊNCIA: método de calibração padrão] | Médio |
| N5 | **Risco de excesso de veto (falso-DENY):** agregação estrutural-primeiro + veto pode bloquear convicções válidas. O método de medição (ENF-07) está declarado, mas o limiar amostral está aberto — vale ligar ao BL-002 (dispara na homologação) | `plan.md:1020-1021`; BL-002 | Menor |

## 5. O que adotar (recomendações priorizadas — todas [PROPOSTA]; nada aplicado)

| Prio | Ação | Onde | Custo |
|---|---|---|---|
| **R1** | Definir o **Score 0–9** (N1): opções (a) manter 0–3 por agente analítico (Estrutural/Institucional/Operacional) somado deterministicamente a partir do vetor; (b) aposentar o score e substituir por critério do vetor 8D (H-16); (c) deixar para J-001 com marcador explícito. **Decisão de Andraus** | SPEC-003 RULE-CF-009/CF-012/esquema | Baixo (Spec) + decisão |
| **R2** | **N2:** ou incluir em CF-012/EC-CF-005 a pré-condição `hypothesis_ref` com nível de invalidação explícito (Salvaguarda 1), ou corrigir CC-04 | SPEC-003 | Baixo |
| **R3** | **N3 + parte válida de E2/E3:** regra "o gate **valida/recomputa** `global_conviction`/`score` a partir das notas por dimensão persistidas; LLM só propõe notas"; campo `computed_by` e `gate_record` no objeto; pré-condição **do consumidor**: o Manager só consome vetores `status == GATED_PASS` | SPEC-003 (mecanismo) + Manager Contract (EUA-E23) | Baixo |
| **R4** | **E4:** declaração negativa de capacidade do mecanismo de convicção (lê evidência, calcula, publica no Blackboard; NÃO executa ordem, NÃO dimensiona risco, NÃO chama o Bot) | SPEC-003 D1 | Baixo |
| **R5** | **E1/E5:** emenda **única** no método: campo `ENFORCER/PONTO DE INTERCEPTAÇÃO` no Enforcement Contract (atomic-spec §10) + registrar como insumo do Dossiê da SPEC-018/K-001 o "contrato comum de enforcement runtime" (schema/guard/state/capability) — em vez de 1 validador por Spec | atomic-spec; backlog BL-013 | Médio (emenda) |
| **R6** | **Não adotar** a taxonomia AUTHORITY MODE; explicitar a semântica "recomputa" na Classe H (R3) | — | Zero |
| R7 | N4/N5: registrar "70% ≠ probabilidade" no CCM-001 e vincular medição de falso-DENY ao BL-002 | SPEC-003/BL-002 | Baixo |

## 6. Limites desta análise

- Não executei backtest nem verifiquei desempenho de trading; N4/N5 são [INFERÊNCIA].
- Verifiquei a existência e o teor dos três arXiv e do OWASP; não avaliei a qualidade metodológica interna dos preprints.
- A revisão externa citou números de linha/nomes que conferi no repo (ADV-CF-03/08, observáveis) — corretos.
