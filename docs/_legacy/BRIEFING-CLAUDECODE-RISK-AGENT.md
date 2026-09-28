# BRIEFING — Claude Code: Auditoria Semântica e Normativa do Risk Agent

**Data:** 2026-09-22  
**Origem:** Sessão de design entre Andraus e Claude (claude.ai)  
**Destino:** Claude Code (SOT-Harness repo)  
**Natureza:** [PROPOSTA] — nenhum item aqui é baseline até homologação de Andraus  
**Status epistemológico:** TRACE-06 aplicado em todo o documento

---

## 1. O que aconteceu nesta sessão

Andraus e Claude analisaram dois Master Documents do Risk Agent (SOT-RISK-MASTER-001,
versões 1.0 e 2.0) e tomaram quatro decisões arquiteturais sobre como integrar o Risk
Agent ao pipeline SOT. Essas decisões foram auditadas com challenge independente antes
de serem encaminhadas.

O objetivo agora é que o Claude Code:

1. Audite a base semântica e normativa atual do repositório contra essas decisões
2. Identifique conflitos, gaps e impactos nos documentos existentes
3. Ajude Andraus a tomar a decisão final sobre forma documental
4. Produza os artefatos necessários quando Andraus homologar

---

## 2. Decisões arquiteturais tomadas por Andraus (2026-09-22)

Status: [PROPOSTA DE ANDRAUS — aguarda formalização via EUA]

### D-RISK-01 — Risk Agent absorve o ARR

O Risk Agent absorve integralmente o componente ARR (Agente de Risco-Retorno,
homologado em D-ARR-001 em 2026-09-16). Os parâmetros do D-ARR-001 tornam-se
invariantes mínimos do Risk Agent:

- R:R ≥ 3:1 (herdado de D-ARR-001)
- Risco por operação dinâmico, sensível à oportunidade, inclui sugestão de alavancagem
- Portfolio Heat máximo ≤ 15%

O ARR deixa de existir como componente separado no pipeline.

### D-RISK-02 — Pipeline atualizado

Pipeline anterior (homologado):
```
... → Synthesis → ARR → TMP → Bot Finance
```

Pipeline proposto:
```
... → Synthesis → Risk Agent → Risk Harness → Signal Package → Bot Finance
```

O TMP passa a ser artefato interno de passagem entre Síntese e Risk Agent.
Não atravessa mais a fronteira SOT → exterior.

### D-RISK-03 — Signal Package é a nova fronteira

O Signal Package é o único artefato que atravessa a fronteira SOT → Bot Finance.

Características definidas por Andraus:
- Contém apenas o que o Bot Finance precisa para iniciar seu runtime
- NÃO contém análise, hipóteses, ou raciocínio cognitivo
- Contrato exato (campos, schema) = DECISÃO ABERTA FORMAL (D-RISK-SP-001)
- Diferida à spec de acoplamento (RISK-022, futura)

### D-RISK-04 — Papéis do Bot Finance e do humano

- Bot Finance: logística financeira de transferência de fundos para a corretora
- Trading em si: executado pelo humano (Andraus) com base no Signal Package
- Signal Package serve a DOIS receptores: Bot Finance (runtime de logística) +
  humano (runtime de execução)

### D-RISK-05 — INV-05 atualizada

De: "SOT não executa ordem, produz TMP"
Para: "SOT não executa ordem, produz Signal Package via Risk Harness"

---

## 3. Arquitetura cognitiva do Risk Agent (dos Master Documents)

O Risk Agent é uma entidade cognitiva CRITICAL com:

**14 camadas cognitivas:**
1. Principiológica (15 princípios — P1 Preservação a P15 Integridade)
2. Epistemológica (classifica: observação / dado / fato / estimativa / hipótese /
   desconhecimento)
3. Inquérito (procura riscos não declarados, inconsistências, evidências ausentes)
4. Ontológica (universo de entidades: capital, exposição, posição, risco, liquidez...)
5. Semântica (risco ≠ retorno ≠ probabilidade ≠ confiança — distinções operacionais)
6. Causal (mecanismos, não correlações: Condição → Mecanismo → Evento → Consequência)
7. Contrafactual (C1..C7: hipótese falsa, stop não executado, regime alterado...)
8. Incerteza (aleatoriedade / epistêmica / modelo / regime — separadas)
9. Probabilística (distribuições, caudas, calibração, Monte Carlo quando aplicável)
10. Memória (decisão / resultado / modelo / risco — 4 categorias)
11. Metacognitiva (avalia a própria avaliação — obrigatória antes da decisão final)
12. Quantitativa (ferramentas determinísticas: VaR, CVaR, drawdown, correlação...)
13. Risco–Retorno (distribuição de perdas + retorno + incerteza + exposição + cauda)
14. Decisional (ACCEPT / WAIT / REJECT / ABSTAIN)

**Objetos intermediários:**
- RDR (Risk Decision Record): cognição completa — o que o agente sabia, calculou,
  inferiu, quais riscos identificou, por que decidiu. NÃO vai para o Bot Finance.
- Signal Package: contrato operacional mínimo. Referencia o RDR. Vai para o exterior.

**Invariantes do Risk Agent (INV-RISK-01..12):**
- INV-RISK-01: não autorizar exposição sem avaliação de risco
- INV-RISK-02: não confundir convicção analítica com convicção de risco
- INV-RISK-03: não tratar ausência de evidência como evidência positiva
- INV-RISK-04: não ocultar contraevidência material
- INV-RISK-05: não emitir decisão sem avaliação de incerteza material
- INV-RISK-06: não usar cálculo textual quando ferramenta determinística disponível
- INV-RISK-07: não alterar políticas normativas durante a decisão
- INV-RISK-08: não emitir Signal Package sem Risk Harness aprovado
- INV-RISK-09: não permitir que o Bot Finance reinterprete a decisão de risco
- INV-RISK-10: toda decisão deve possuir provenance
- INV-RISK-11: toda decisão crítica deve ser reconstruível
- INV-RISK-12: o agente deve poder ABSTAIN

**Risk Harness (gate E3):**
- Valida invariantes antes de autorizar o Signal Package
- Fail-closed: sem validação, sem package
- O LLM não é seu próprio gate (ENF-03 vigente)

---

## 4. Achados da auditoria das decisões (challenge independente)

A sessão incluiu auditoria das quatro decisões. Resumo dos achados críticos:

### Achado A — Supersedação formal do ARR

**Problema:** D-ARR-001 está homologado e baselinesado. Dizer que o Risk Agent
"absorve" o ARR sem uma ata formal de supersedação cria um ghost component — o ARR
continua citado em atas e specs antigas como se existisse.

**Requisito:** a EUA-E19 (ou artefato equivalente) deve incluir supersedação explícita
do ARR como componente de pipeline, com registro no CATÁLOGO-OFICIAL de que D-ARR-001
está absorvido. Os parâmetros migram com rastreabilidade explícita.

### Achado B — Emenda à CONSTITUTION obrigatória

**Problema:** a CONSTITUTION P14 diz literalmente:
"O SOT nunca executa ordens diretamente. Produz um Trading Mission Package (TMP)
para o Bot Trade Finance."

A decisão D-RISK-05 conflita diretamente com P14. Uma EUA que declara o Signal Package
como fronteira sem emendar P14 cria conflito constitucional ativo.

**Requisito:** emenda formal à CONSTITUTION P14. Texto proposto:
"O SOT nunca executa ordens diretamente. Produz um Signal Package via Risk Harness
para o Bot Trade Finance. O TMP é artefato interno de passagem entre Síntese e
Risk Agent."

### Achado C — synthesis.spec.md muda de responsabilidade

**Problema:** a synthesis.spec.md define o TMP como output final da Síntese ("output
final do sistema para o Bot Trade Finance"). Com D-RISK-02, o output da Síntese passa
a ser *input do Risk Agent* — não mais artefato de fronteira.

**Requisito:** revisão (ou adendo) à synthesis.spec.md declarando que o TMP produzido
pela Síntese é artefato interno, e que a fronteira SOT → exterior agora é o Signal
Package emitido pelo Risk Agent via Risk Harness.

### Achado D — Signal Package tem dois receptores

**Problema:** Andraus declarou que o Bot Finance faz logística financeira e o humano
executa o trading. Isso significa que o Signal Package serve a dois receptores
simultaneamente com necessidades potencialmente diferentes:
- Bot Finance precisa de: instrução de runtime (o que mover, para onde, quanto)
- Humano precisa de: parâmetros de execução (ativo, direção, entrada, stop, alvo,
  sizing, invalidação, janela temporal)

**Requisito:** RISK-022 (spec de acoplamento) deve ter como requisito explícito que o
Signal Package é especificado para ambos os receptores. O contrato não pode ser
definido olhando apenas para o Bot Finance.

### Achado E — Sequenciamento EUA-E17 × EUA-E19

**Problema:** EUA-E17 (proposta não-homologada) propõe FASE GOV no ROADMAP. EUA-E19
proporia Fase RISK. Se as duas forem processadas em paralelo sem relação formal, a
posição relativa das fases fica indefinida.

**Requisito:** EUA-E19 deve ser explícita sobre a dependência: "posição da Fase RISK
relativa à Fase GOV depende da resolução da EUA-E17" — ou deve ser sequenciada após
a EUA-E17.

---

## 5. O que precisamos que o Claude Code faça

### Tarefa A — Auditoria semântica e normativa (PRIORITÁRIA)

Varrer os documentos normativos ativos do repositório e mapear todos os pontos
que são impactados pelas decisões D-RISK-01..05 e pelos achados A..E.

Documentos a auditar (mínimo):

```
governance/CONSTITUTION.md           → Achado B (P14)
governance/RULES.md                  → referências ao ARR, ao TMP como fronteira
governance/CATALOGO-OFICIAL.md       → D-ARR-001, ARR como componente
governance/CONFLICT-MAP.md           → possíveis conflitos com D-RISK-01..05
specs/synthesis.spec.md              → Achado C (TMP como output final)
schemas/synthesis.output.json        → schema atual inclui TMP como output
AGENTS.md                            → pipeline documentado lá
GLOSSARIO.md                         → TMP definido como "contrato final"
ROADMAP.md                           → ARR posicionado no pipeline
docs/fundamentos/ENGENHARIA-GERAL.md → TMP e Signal Package definidos lá
rag/synthesis.knowledge.md           → CHUNK-SY-007 define TMP como output final
```

Para cada documento, o Claude Code deve produzir:

```
DOCUMENTO: <caminho>
IMPACTO: [CRÍTICO / MÉDIO / MENOR / NENHUM]
TRECHO CONFLITANTE: <citação exata com §/linha>
DECISÃO QUE CONFLITA: D-RISK-0X / Achado X
AÇÃO NECESSÁRIA: <o que precisa mudar>
```

### Tarefa B — Mapeamento de referências ao ARR

Fazer grep completo de todas as ocorrências de "ARR", "D-ARR-001",
"Agente de Risco-Retorno" no repositório e listar quais precisam de
atualização formal vs. quais são registros históricos que devem ser preservados
(INV-07 — versionamento monotônico: nada é deletado, apenas supersedado).

### Tarefa C — Mapeamento de referências ao TMP como fronteira

Fazer grep completo de "TMP", "Trading Mission Package" buscando especificamente
ocorrências onde o TMP é descrito como artefato de saída do SOT ou fronteira
com o Bot Finance — vs. ocorrências onde é apenas mencionado como conceito.

### Tarefa D — Parecer sobre forma documental

Com base nos achados das Tarefas A, B e C, o Claude Code deve emitir um parecer
sobre qual forma documental é mais adequada para formalizar as decisões D-RISK-01..05:

**Opção 1 — EUA-E19 única (ampla)**
Uma única EUA registra todas as decisões + supersedação ARR + emenda P14 + autoriza
Fase RISK. Risco: escopo largo pode gerar achado Crítico no Revisor e travar tudo.

**Opção 2 — EUA-E19 + EUA-E20 sequenciais**
EUA-E19: registra D-RISK-01..05 e supersedação do ARR (escopo enxuto).
EUA-E20: propõe Fase RISK no ROADMAP e posiciona RISK-MASTER-001 (após EUA-E17).
Risco: dois ciclos de revisão.

**Opção 3 — DHR-RISK-001 (Ata de Homologação de Arquitetura)**
Documento tipo DHR para decisão arquitetural de domínio (não emenda ao método).
Homologa as decisões D-RISK-01..05 sem criar uma EUA. A Fase RISK no ROADMAP vem
depois separadamente.

O parecer deve incluir:
- Qual opção é mais coerente com a governança vigente
- Quais riscos de processo cada opção carrega
- Recomendação fundamentada

### Tarefa E — Esboço dos artefatos (somente após parecer aprovado por Andraus)

Somente após Andraus aprovar o parecer da Tarefa D, o Claude Code deve produzir
os artefatos documentais na forma correta para revisão.

---

## 6. Contexto de governança que o Claude Code precisa respeitar

### Invariantes invioláveis
- INV-07: versionamento monotônico — nada é deletado, apenas supersedado com registro
- INV-09: sem baseline informal — nenhuma decisão é "baseline" sem homologação de Andraus
- CONS-01: nenhuma decisão aberta pode aparecer como invariante fechado
- TRACE-06: documentado ≠ homologado; status epistemológico deve ser explícito
- ENF-03: LLM nunca é seu próprio gate; gate é determinístico

### Fluxo de autoridade (não pode ser pulado)
```
Especificador (Claude Code) → Revisor de Especificação → Andraus (homologa)
```

Nenhum artefato produzido pelo Claude Code é normativo até passar por esse fluxo.

### Etiquetagem obrigatória (TRACE-06)
Todo artefato produzido deve usar:
- [FATO NORMATIVO] — para conteúdo já homologado que está sendo citado
- [FATO ARQUITETURAL] — para decisões de Andraus desta sessão (não homologadas ainda)
- [PROPOSTA] — para sugestões do Especificador
- [DECISÃO NECESSÁRIA] — para pontos que requerem deliberação de Andraus

### O que NÃO fazer
- Não reescrever specs existentes sem autorização (INV-09)
- Não tratar as decisões desta sessão como baseline (ainda são [FATO ARQUITETURAL])
- Não fechar decisões abertas (J-001, G-001, etc.) implicitamente
- Não criar referências circulares entre documentos não-redigidos
- Não produzir EUA sem o formato padrão (ver EUA-E04..E16 como referência)

---

## 7. Decisões abertas que este trabalho NÃO deve fechar

- J-001: fórmula/pesos/limiares definitivos do Conviction Vector
- D-RISK-SP-001: contrato exato do Signal Package (campos, schema)
- Posição da Fase RISK relativa à Fase GOV (depende de EUA-E17)
- CDM-001 (Canonical Decision Model) — o RDR é um objeto de decisão e precisará
  do CDM-001 como idioma canônico; mas CDM-001 ainda não existe
- I-001: Skills como unidades formais separadas (trava as Skills do Risk Agent)

---

## 8. Referências para o Claude Code localizar no repositório

Documentos dos Master Documents do Risk Agent (não estão no repositório ainda —
foram apresentados por Andraus nesta sessão como proposta):
- SOT-RISK-MASTER-001 v1.0 (arquitetura cognitiva)
- SOT-RISK-MASTER-001 v2.0 (engenharia de especificação)

Documentos normativos ativos no repositório a consultar como referência de formato:
- governance/EUA-E04_Heranca_Delta_PROPOSTA.md (formato EUA enxuta)
- governance/DHR-EUA-E04_Ata_Homologacao_Heranca_Delta.md (formato DHR)
- governance/EUA-E16_Sincronizacao_Agentes_PROPOSTA.md (formato EUA com
  múltiplas decisões)
- governance/CONSTITUTION.md (P14 a ser emendada)
- atomic-spec.md (método vigente)
- governance/RULES.md (onde novas RULE-RISK vão residir)

---

## 9. Pergunta central para o Claude Code responder

> Com base na auditoria dos documentos normativos ativos, quais são os impactos
> reais das decisões D-RISK-01..05 na base semântica e normativa existente?
> E qual forma documental é mais adequada para formalizar essas decisões de modo
> coerente com a governança vigente?

A resposta deve ser um parecer fundamentado, com achados numerados, ancoragem
em arquivo:§ para cada ponto, e recomendação clara sobre a forma documental.

---

## 10. O que Andraus vai decidir com base no parecer

1. Aprovar ou ajustar a forma documental recomendada
2. Autorizar ou ajustar o escopo de cada artefato
3. Homologar os artefatos após ciclo Especificador → Revisor

---

*Documento produzido por Claude (claude.ai) em sessão com Andraus (2026-09-22).*
*Status: [PROPOSTA] — não homologado.*
*Destino: Claude Code / SOT-Harness repo.*
