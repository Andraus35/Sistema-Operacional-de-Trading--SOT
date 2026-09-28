# RESPOSTAS AO QUESTIONÁRIO DE RESOLUÇÃO — SOT Arranque

**Data:** 2026-09-14
**Respondido por:** Andraus (Consensus Authority / Decisor Final)
**Origem:** Questionário de Resolução v1 — produzido pelo Especificador Principal (Claude Code)
**Natureza:** Decisões vinculantes. O Especificador incorpora estas respostas a `ROADMAP.md`, `atomic-spec.md` e documentos afetados antes de iniciar a SPEC-001.
**Próximo passo:** Especificador aplica as decisões → submete ao Revisor (parecer de integridade) → SPEC-001 arranca.

---

## Tabela de decisões (visão rápida)

| Q | Tema | Decisão | Opção |
|---|---|---|---|
| Q-001 | Status dos modelos canônicos | CHM-001 e CEM-001 = BASELINED; Catálogo atualizado; CCM/CDM/CNM = pendentes de redação | A |
| Q-002 | Limiares de convicção (≥70%, 7/9) | Piso interino calibrável — FATO NORMATIVO com cláusula de recalibração após backtest | B |
| Q-003 | As "5 Salvaguardas Constitucionais" | Emenda formal ao CEE-001 unificando os dois conjuntos num novo §; CEE-001 reversionado | C |
| Q-004 | R:R mínimo: 2:1 ou 3:1? | 3:1 como regra única, fiel ao ARIA de origem; corrigir RULE-ICT-002 e CONSTITUTION | A |
| Q-005 | Quem cria hipótese? | Híbrido: Elliott cria hipótese primária/direcional; demais criam sub-hipóteses referenciadas à primária | C |
| Q-006 | Máquina de estados da hipótese | Reconciliar tudo em um único conjunto homologado; descartar KERNEL e RULE-BB-003 divergentes | C |
| Q-007 | Topologia Conviction/Fusion/Synthesis (B-001) | Três componentes separados: Fusion Engine → Conviction Engine → Synthesis (árbitro) | A |
| Q-008 | Dimensões do Conviction Vector | 8 dimensões (inclui volume; conforme AUDITORIA §J.3) | B |
| Q-009 | Framework 3E vs 4Es | Adotar 4Es e emendar CEE-001/CONSTITUTION para incluir Economicidade | A |
| Q-010 | PPQ-001: vigora ou foi extinto? | PPQ-001 supersedido como fluxo de aprovação; mantido como referência de rigor (dial GES) | B |
| Q-011 | Status normativo de CONSTITUTION/RULES/CONFLICT-MAP | Homologar como baseline F.1 após correções de Q-002/003/004/008 | A |
| Q-012 | Briefing PP-SPEC-001 não existe | ROADMAP §4 como briefing efetivo; remover referência a PP-SPEC-001 | B |
| Q-013 | Caminhos do validador e arquivos de agente | Mover arquivos para os caminhos declarados: `scripts/` e `.claude/agents/` | A |
| Q-014 | Mapeamento de nomes de agentes | Equivalências declaradas; Macro/Sentiment/Risk/Context = fora do escopo atual | A |
| Q-015 | Identidade do sistema: SOT e ORYX | Nome único e expansão canônica: **SOT — Sistema Operacional de Trading** | — |

---

## Decisões detalhadas

---

### Q-001 · STATUS DOS MODELOS CANÔNICOS
**Decisão: [A]**

- **CHM-001** = BASELINED. Evidência suficiente: "CONSOLIDADO — aprovado por Andraus (12/07/2026)" no próprio arquivo. Atualizar o Catálogo para refletir este status.
- **CEM-001** = BASELINED. Mesma lógica.
- **CCM-001, CDM-001, CNM-001** = referências pendentes de redação. Não existem como arquivos. Tratar como `[DECISÃO NECESSÁRIA]` em toda Spec que os referenciar. SPEC-003 é a responsável por redigir o CCM-001.

**Ações requeridas pelo Especificador:**
1. Atualizar `ROADMAP.md` R1/R4: CHM-001 e CEM-001 = baselined; CCM/CDM/CNM = "pendentes de redação".
2. Atualizar `atomic-spec.md §12`: mover CCM-001 para a tabela de decisões abertas com nota "pendente de redação — SPEC-003".
3. Atualizar o Catálogo Oficial: CHM-001 e CEM-001 passam de "não iniciado" para "BASELINED".
4. Não invocar CONST-01 como bloqueio para CCM/CDM/CNM (não há canônico a proteger).

---

### Q-002 · LIMIARES DE CONVICÇÃO (≥70%, 7/9)
**Decisão: [B]**

Os limiares atuais (≥70% convicção global, 7/9 score) são homologados como **piso interino — Fase Piloto**, com as seguintes condições:

- Status: FATO NORMATIVO — Fase Piloto (recalibrável após backtesting sistemático).
- Os valores são vinculantes para operação, mas explicitamente rotulados como provisórios.
- Gatilho de recalibração: após acumulação de ≥30 sinais com resultado registrado, submeter revisão a Andraus.
- J-001 permanece aberto para a fórmula de agregação, pesos e limiares definitivos (pós-backtest).

**Ações requeridas pelo Especificador:**
1. Emendar INV-03 em `atomic-spec.md`: distinguir "piloto vinculante" de "definitivo fechado". INV-03 passa a ler: "Conviction Vector — fórmula/pesos/limiares definitivos = J-001 em aberto; limiares de Fase Piloto (≥70%, 7/9) = FATO NORMATIVO interino, recalibrável após backtest".
2. Reancorar RULE-003 e RULE-CEE-004 em RULES.md: adicionar rótulo "Fase Piloto — recalibrável" sem alterar os valores.
3. J-001 permanece na tabela de decisões abertas com escopo atualizado: "fórmula/pesos/limiares definitivos pós-calibração".

---

### Q-003 · AS "5 SALVAGUARDAS CONSTITUCIONAIS"
**Decisão: [C]**

Emenda formal ao CEE-001: os dois conjuntos de salvaguardas são unificados num novo parágrafo do CEE-001, e o documento é reversionado.

- **Salvaguardas de Economia e Roteamento** (CEE-001 §10 original — 5 itens): mantidas intactas no §10.
- **Salvaguardas de Sinal de Trading** (hoje misatribuídas ao CEE-001 §10): formalizadas como novo **§11** do CEE-001, com ID próprio ("Salvaguardas de Sinal — CEE-001 §11").
- CEE-001 passa de v1.x para **v2.0** com os dois parágrafos.

**Ações requeridas pelo Especificador:**
1. Redigir emenda ao CEE-001 adicionando §11 com as 5 salvaguardas de sinal (invalidação, 7/9, conflito direcional, 70%, R:R).
2. Submeter emenda ao Revisor → homologação de Andraus → CEE-001 v2.0.
3. Atualizar todas as citações em RULES.md, `atomic-spec.md`, `especificador.md`, `revisor.md`: distinguir "CEE-001 §10" (economia) de "CEE-001 §11" (sinal).
4. INV-04 de `atomic-spec.md §13` permanece ancorado ao §10 (custo não entra no Conviction Vector).

---

### Q-004 · R:R MÍNIMO: 2:1 OU 3:1?
**Decisão: [A]**

**3:1 como regra única**, fiel ao ARIA de origem. A notação canônica é **1:3** (risco:retorno), equivalente a 3:1 (retorno:risco).

**Ações requeridas pelo Especificador:**
1. RULE-ICT-002 em RULES.md: corrigir de "2:1" para "1:3 mínimo" e remover a auto-contradição com a citação do ARIA.
2. CONSTITUTION.md (linha 153), AGENTS.md (linha 67), `specs/synthesis.spec.md` (linhas 22, 57): corrigir de "R:R ≥ 2:1" para "R:R ≥ 1:3".
3. RULE-006 permanece como está (já usa 3:1 / 1:3 corretamente).
4. Registrar no CONFLICT-MAP que RULE-ICT-002 foi corrigida por esta decisão.

---

### Q-005 · QUEM CRIA HIPÓTESE?
**Decisão: [C] — Híbrido**

- **Hipótese primária/direcional**: criada exclusivamente pelo **Agente Estrutural (Elliott Specialist)**. Apenas ele determina a direção e o grau estrutural dominante.
- **Sub-hipóteses**: criadas pelos demais agentes (SMC/Fibonacci/ICT), sempre referenciadas à hipótese primária via herança fractal (relação parent/child do CHM-001).
- ICT **não cria hipótese** de nenhum tipo — confirma ou invalida a execução de uma sub-hipótese existente. INV-02 permanece intacto.
- O objeto "hipótese" no Blackboard diferencia: `hypothesis_type: PRIMARY | SUB` com campo `parent_id` obrigatório para SUB.

**Ações requeridas pelo Especificador:**
1. Emendar CONSTITUTION.md tabela Blackboard: "Hypotheses | Elliott Specialist (PRIMARY) + demais agentes (SUB, referenciadas)".
2. SPEC-001 especifica a distinção PRIMARY/SUB e o contrato parent/child sobre o CHM-001.
3. INV-01 e INV-02 de `atomic-spec.md §13` permanecem; acrescentar nota: "ICT não cria hipótese de nenhum tipo (nem primária nem sub)".

---

### Q-006 · MÁQUINA DE ESTADOS DA HIPÓTESE
**Decisão: [C] — Conjunto único homologado**

O conjunto canônico é o **CHM-001** (7 estados epistêmicos): EMERGENT → CANDIDATE → ACTIVE → DOMINANT → SUPERSEDED → REFUTED → ARCHIVED.

- RULE-BB-003 (PROPOSED/VALIDATED/ACTIVE/SUPERSEDED) é **descontinuada** e substituída pelo mapeamento CHM-001 → Blackboard.
- Os estados do KERNEL EC-COG-002 e EC-COG-004 divergentes são descartados como versões de trabalho não homologadas.
- O Blackboard usa os 7 estados do CHM-001 diretamente; não há estado de publicação separado.

**Ações requeridas pelo Especificador:**
1. RULES.md: marcar RULE-BB-003 como SUPERSEDED, apontar para "CHM-001 §states".
2. SPEC-001 (D5): usar os 7 estados do CHM-001 sem camada adicional.
3. SPEC-004 (Blackboard): herdar os estados da hipótese do CHM-001; não definir máquina de estados própria para hipóteses.
4. Acrescentar à tabela de decisões abertas: "Estados do Blackboard para objetos não-hipótese (Evidência, Missão) = pendente SPEC-004".

---

### Q-007 · TOPOLOGIA CONVICTION / FUSION / SYNTHESIS (B-001)
**Decisão: [A] — Três componentes separados**

- **Fusion Engine** (determinístico): funde Evidências heterogêneas em Evidência DERIVED. Entidade canônica do CEM-001. Não calcula convicção.
- **Conviction Engine** (semi-determinístico): recebe Evidência DERIVED do Fusion Engine e calcula o Conviction Vector de 8 dimensões.
- **Synthesis Agent** (LLM): árbitro final — recebe o Conviction Vector + hipóteses e produz a decisão / Trading Mission Package.

B-001 encerrado: **Conviction Engine é separado do Synthesis Agent**.

**Ações requeridas pelo Especificador:**
1. `atomic-spec.md §12`: fechar B-001 com esta decisão; remover da tabela de decisões abertas.
2. CONSTITUTION.md: confirmar separação Conviction Engine ↔ Synthesis Agent.
3. `specs/synthesis.spec.md`: desmembrar — convicção vai para a spec do Conviction Engine (SPEC-003); arbitragem permanece no Synthesis (SPEC-014).
4. ROADMAP.md SPEC-003: título passa a "Conviction Vector, Evidence Fusion Engine & Conviction Engine".

---

### Q-008 · DIMENSÕES DO CONVICTION VECTOR
**Decisão: [B] — 8 dimensões**

As 8 dimensões do Conviction Vector são: **estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica** (conforme AUDITORIA §J.3).

- Volume é dimensão plena (não opcional), relevante para BTC e NASDAQ; pesos por ativo são parte de J-001.
- J-001 permanece aberto para fórmula de agregação, pesos e limiares definitivos.
- A dimensionalidade (8) é agora FATO NORMATIVO; entra como invariante fechado no escopo da SPEC-003/CCM-001.

**Ações requeridas pelo Especificador:**
1. CONSTITUTION.md P02: corrigir de 7 para 8 dimensões; acrescentar "volume".
2. `specs/synthesis.spec.md`: corrigir `conviction_vector` de 5 para 8 campos.
3. `atomic-spec.md §12`: atualizar DECISÃO-ABERTA-007 como fechada (dimensionalidade = 8); J-001 reduzido a fórmula/pesos/limiares.
4. SPEC-003 parte de 8 dimensões como dado fixo.

---

### Q-009 · FRAMEWORK 3E vs 4Es
**Decisão: [A] — Adotar 4Es; emendar CEE-001 e CONSTITUTION**

Economicidade é formalizada como 4º nível da hierarquia inviolável: **Eficácia → Efetividade → Eficiência → Economicidade**.

- CEE-001 recebe emenda (novo §) formalizando o 4º E com a distinção: Eficiência = como bem o sistema usa os recursos; Economicidade = custo mínimo para o resultado, nunca acima de Eficácia.
- CONSTITUTION.md §Framework: atualizar "3E" para "4Es".
- Esta emenda pode ser bundled com a emenda de Q-003 (CEE-001 v2.0).

**Ações requeridas pelo Especificador:**
1. Incluir o 4º E na emenda do CEE-001 (bundled com Q-003 → CEE-001 v2.0).
2. CONSTITUTION.md: atualizar referências de "3E" para "4Es" com a hierarquia completa.
3. `atomic-spec.md §10.1` e `especificador.md`: já corretos; nenhuma alteração necessária.

---

### Q-010 · PPQ-001: VIGORA OU FOI EXTINTO?
**Decisão: [B] — Supersedido parcialmente**

- **PPQ-001 como fluxo de aprovação**: **SUPERSEDIDO** pelo trio Especificador → Revisor → Andraus. Nenhum papel intermediário do PPQ-001 está ativo.
- **PPQ-001 como referência de rigor (dial GES)**: **MANTIDO**. RULE-PPQ-001 e o dial GES (rigor proporcional ao impacto) permanecem ativos como critério de profundidade.
- `revisor.md` está incorreto na afirmação "Não há PPQ-001" — a frase nega o fluxo de papéis, não o documento.

**Ações requeridas pelo Especificador:**
1. `revisor.md §2`: corrigir para "Não há papéis intermediários do PPQ-001. O documento PPQ-001 permanece como referência de rigor (dial GES) via RULE-PPQ-001."
2. Catálogo Oficial: adicionar nota de superseção parcial ao PPQ-001 — "fluxo de aprovação supersedido; dial GES ativo".
3. RULES.md: manter RULE-PPQ-001 intacta; adicionar nota "fluxo de aprovação não vigente".

---

### Q-011 · STATUS NORMATIVO DE CONSTITUTION/RULES/CONFLICT-MAP
**Decisão: [A] — Homologar como baseline F.1**

CONSTITUTION.md, RULES.md e CONFLICT-MAP.md serão homologados como **baseline F.1** após a aplicação das correções decididas em Q-002, Q-003, Q-004 e Q-008.

**Ordem de execução obrigatória:**
1. Aplicar correções: Q-004 (R:R 3:1) + Q-005 (hipótese primária/sub) + Q-008 (8 dimensões) em CONSTITUTION/RULES.
2. Redigir emenda CEE-001 v2.0 (Q-003 + Q-009).
3. Submeter os três arquivos corrigidos ao Revisor para parecer de integridade.
4. Andraus homologa → registrar no Catálogo como "BASELINED F.1".
5. **Só então**: iniciar SPEC-001.

---

### Q-012 · BRIEFING PP-SPEC-001 NÃO EXISTE
**Decisão: [B]**

O **ROADMAP §4** (escopo da SPEC-001, já atualizado com as decisões Q-001/005/006) é o briefing efetivo da SPEC-001.

**Ações requeridas pelo Especificador:**
1. ROADMAP.md §25: remover a referência "PP-SPEC-001 (briefing)" e substituir por "Ver ROADMAP §4 para escopo e fronteiras da SPEC-001".
2. Não criar nenhum arquivo PP-SPEC-001.

---

### Q-013 · CAMINHOS DO VALIDADOR E ARQUIVOS DE AGENTE
**Decisão: [A] — Mover arquivos para os caminhos declarados**

- `validate_spec_sot.py` → mover de raiz para `scripts/validate_spec_sot.py`
- `especificador.md` → mover de raiz para `.claude/agents/especificador.md`
- `revisor.md` → mover de raiz para `.claude/agents/revisor.md`

As referências nos documentos (`revisor.md`, `AGENTS.md`) permanecem corretas; só os arquivos se movem.

**Ações requeridas pelo Especificador:**
1. Executar os moves no repositório antes do início da SPEC-001.
2. Confirmar que o gate `python scripts/validate_spec_sot.py` funciona a partir da raiz do repo.

---

### Q-014 · MAPEAMENTO DE NOMES DE AGENTES
**Decisão: [A] — Equivalências declaradas; escopo atual restrito**

Glossário oficial de equivalências (a ser registrado em GLOSSÁRIO.md ou seção dedicada do ROADMAP):

| Nome canônico (CEM-001/KERNEL) | Nome operacional (repo SOT) |
|---|---|
| Structural Agent | Elliott Specialist |
| Institutional Agent | SMC Specialist |
| Fusion Engine | Fusion Engine (mantido) |
| Conviction Engine | Conviction Engine (mantido) |
| Synthesis Agent | Synthesis Agent (mantido) |
| Fibonacci Agent | Fibonacci Validator |
| Execution Agent | ICT Specialist |

**Macro Agent, Sentiment Agent, Risk Agent, Context Agent** = fora do escopo atual do SOT (herança do modelo genérico ORYX). Não serão especificados no roadmap atual. Se necessário no futuro, decisão explícita de Andraus.

**Ações requeridas pelo Especificador:**
1. Criar `GLOSSÁRIO.md` na raiz do repositório com esta tabela de equivalências.
2. SPEC-002 (Evidence Harness): lista de produtores de Evidência restrita aos agentes do SOT (sem Macro/Sentiment/Risk/Context).

---

### Q-015 · IDENTIDADE DO SISTEMA: SOT E ORYX
**Decisão: [nome único]**

**Nome único e expansão canônica:** `SOT — Sistema Operacional de Trading`

- A expansão "Sistema de Operações e Tendências" (CONSTITUTION.md linha 1) é **descontinuada**.
- A relação com ORYX: **SOT é o sistema de trading; ORYX foi o nome do ecossistema/produto anterior.** O projeto atual opera sob o nome SOT exclusivamente.
- Todos os cabeçalhos novos usam "SOT — Sistema Operacional de Trading".
- Documentos baselined que mencionam "ORYX" não precisam ser editados agora; a equivalência fica registrada no GLOSSÁRIO.md.

**Ações requeridas pelo Especificador:**
1. CONSTITUTION.md linha 1: corrigir expansão para "Sistema Operacional de Trading".
2. `GLOSSÁRIO.md`: registrar "ORYX = nome histórico do ecossistema; SOT = nome atual do sistema de trading".
3. `atomic-spec.md`, `roadmap.md`, `especificador.md`, `revisor.md`: já usam "Sistema Operacional de Trading" — sem alteração.

---

## Sequência de execução para o Especificador

As decisões geram as seguintes ações, na ordem obrigatória:

```
BLOCO 1 — Correções imediatas nos arquivos raiz (sem homologação prévia)
  1. Mover arquivos para paths corretos (Q-013)
  2. Criar GLOSSÁRIO.md com equivalências e identidade (Q-014, Q-015)
  3. Atualizar ROADMAP.md: R1/R4, escopo SPEC-001, §25, B-001 fechado (Q-001, Q-005, Q-007, Q-012)
  4. Atualizar atomic-spec.md: INV-03, INV-04 nota ICT, §12 decisões abertas (Q-002, Q-005, Q-007, Q-008)

BLOCO 2 — Correções em CONSTITUTION / RULES / CONFLICT-MAP
  5. CONSTITUTION: expansão SOT, R:R 3:1, hipótese PRIMARY/SUB, 8 dimensões, 4Es (Q-004, Q-005, Q-008, Q-009, Q-015)
  6. RULES: RULE-ICT-002 (3:1), RULE-BB-003 (SUPERSEDED), RULE-PPQ-001 (nota), limiares Fase Piloto (Q-002, Q-004, Q-006, Q-010)
  7. CONFLICT-MAP: registrar RULE-ICT-002 corrigida

BLOCO 3 — Emenda CEE-001 v2.0 (bundled Q-003 + Q-009)
  8. Redigir CEE-001 v2.0: §10 (economia, inalterado) + §11 (salvaguardas de sinal) + §12 (4Es)
  9. Submeter ao Revisor → homologação Andraus → CEE-001 v2.0 baselined

BLOCO 4 — Homologação dos três arquivos F.1 (Q-011)
  10. Submeter CONSTITUTION + RULES + CONFLICT-MAP corrigidos ao Revisor
  11. Parecer de integridade do Revisor
  12. Homologação Andraus → registrar no Catálogo como "BASELINED F.1"

BLOCO 5 — Atualização do Catálogo (Q-001, Q-010, Q-011)
  13. CHM-001 e CEM-001 → BASELINED
  14. PPQ-001 → nota de superseção parcial
  15. CONSTITUTION/RULES/CONFLICT-MAP → BASELINED F.1

BLOCO 6 — SPEC-001 arranca (terreno limpo)
```

---

## Decisões abertas remanescentes (após este questionário)

As seguintes decisões abertas permanecem ativas (não foram fechadas por este questionário):

| ID | Descrição | Status após este questionário |
|---|---|---|
| J-001 | Fórmula/pesos/limiares definitivos do Conviction Vector (pós-backtest) | **Reduzido**: dimensionalidade fechada em 8; limiares de Fase Piloto homologados. Fórmula/pesos/limiares definitivos ainda abertos. Bloqueia SPEC-003 para a parte definitiva. |
| G-001 | Schema de estado persistente por agente | Inalterado — SPEC-009 |
| H-001 | Knowledge Graph: grafo real ou estrutura em memória? | Inalterado — SPEC-006 |
| I-001 | Skills como unidades formais separadas? | Inalterado — SPEC-025 |
| K-001 | Ciclo P12 detalhado | Inalterado — SPEC-018 |
| L-001 | Governança do próprio harness | Inalterado — SPEC-019 |
| C-001 | Granularidade EARS multi-condição | Inalterado — padrão de BASpec |
| — | Estados do Blackboard para objetos não-hipótese (Evidência, Missão) | Novo — SPEC-004 |
| — | Pesos por ativo do Conviction Vector (BTC/XAU/NASDAQ) | Novo — parte de J-001 pós-backtest |

---

*Fim das respostas ao Questionário de Resolução v1. Autoridade: Andraus (Decisor Final). Data: 2026-09-14.*
*Nenhuma Spec inicia antes da conclusão do Bloco 4 (homologação F.1) e do Bloco 5 (Catálogo atualizado).*
