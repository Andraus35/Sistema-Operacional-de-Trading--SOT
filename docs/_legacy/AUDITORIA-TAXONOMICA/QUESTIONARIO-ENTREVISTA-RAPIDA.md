# Questionário de Entrevista Rápida: Intenções Iniciais vs Estado Atual

**Instruções:** Responda cada bloco **em 1–3 linhas**. O objetivo é capturar sua intenção original, não elaboração. Depois sistematizaremos em decisões formais.

---

## BLOCO A: Visão Original do SOT

### A.1 — Origem e paradigma
**Pergunta:** O SOT começou como especificação de um **software/bot executável** (com API, banco de dados, webhook)? Ou sempre foi **descrição de agentes cognitivos** especificados por Specs?

**Sua resposta:**
```
[escreva aqui]
```

---

### A.2 — Quando virou spec-first?
**Pergunta:** Quando você decidiu passar de "implementar software" para "especificar harness cognitivo + aiar decisões de build"?

**Sua resposta:**
```
[escreva aqui]
```

---

### A.3 — O que herdar de GEN-1
**Pergunta:** Dos artefatos de primeira geração (síntese.spec.md, score 0–9, schemas antigos, RAG histórico), **o que deve continuar funcionando** e o que **pode ser descartado ou marcado como legado**?

**Sua resposta:**
```
[escreva aqui]
```

---

## BLOCO B: Decisões Abertas com Risco de Bloqueio

### B.1 — Conviction Vector (J-001)
**Pergunta:** A **fórmula/pesos/limiares do Conviction Vector 8D** (J-001 aberto) bloqueia SPEC-003 (Conviction Engine)? Ou pode ser piloto/iterativo inicialmente?

**Sua resposta:**
```
[escreva aqui]
```

---

### B.2 — Master Orchestrator + Mission Engine
**Pergunta:** Esses termos na **Constituição foram nomes de componentes reais do software antigo**? Ou eram padrões de coordenação ainda não decididos? **Devem ser componentes no harness ou apenas legado**?

**Sua resposta:**
```
[escreva aqui]
```

---

### B.3 — Fractal
**Pergunta:** Fractal (camada entre Elliott e SMC) é:
- (A) um agente especialista independente?
- (B) uma skill ou subfunção do Elliott?
- (C) apenas uma dimensão calculada dentro de outro agente?
- (D) funcionalidade futura, ainda não prioridade?

**Sua resposta:**
```
[Escolha A/B/C/D + motivo em 1 linha]
```

---

### B.4 — Score 0–9
**Pergunta:** O score operacional (0–9, agregado de Elliott+SMC+ICT) continuará como **filtro piloto independente do Conviction Vector**, ou será **substituído por CCM-001/J-001** quando homologado?

**Sua resposta:**
```
[escreva aqui]
```

---

## BLOCO C: Conformidade com Baseline Vigente

### C.1 — Canônicos em formação vs BASELINED
**Pergunta:** Quando você leu que CEM-001, SDD-001, CEE-001 estavam no `canon/`, esperava que fossem **BASELINED (vinculantes) ou CANDIDATOS (ainda em formação)**?

**Sua resposta:**
```
[escreva aqui]
```

---

### C.2 — Precedência: Canônico vs DHR
**Pergunta:** Se um **canônico (por ex., CEM-001) tem texto antigo** e uma **DHR (por ex., EUA-E19a) muda a norma**, qual **Spec nova deve ler por default**? O DHR ou o canônico atualizado?

**Sua resposta:**
```
[escreva aqui]
```

---

### C.3 — GPR-001 com resíduos 4D/60%
**Pergunta:** GPR-001 é **baseline de governança que gates PAP/CIC usam**, mas contém referências a **Conviction 4D e thresholds antigos (60%/75%)**. Isso deve ser:
- (A) corrigido em emenda de compatibilidade AGORA?
- (B) deixado para CCM-001 resolver?
- (C) tratado como histórico, com novo guia substituindo?

**Sua resposta:**
```
[Escolha A/B/C + motivo]
```

---

## BLOCO D: Rastreabilidade e Autoridade

### D.1 — Validação de regras
**Pergunta:** Quando um agente encontra uma **regra em documentação**, deve:
- (A) validar TODA regra contra governance/→ROADMAP→ATOMIC-SPEC?
- (B) assumir que tudo no repo está alinhado (confiança)?
- (C) preferir o **último DHR** que menciona o tópico?

**Sua resposta:**
```
[Escolha A/B/C + motivo em 1 linha]
```

---

### D.2 — Single Source of Truth
**Pergunta:** Qual é **o documento único** que diz qual Spec fazer a seguir e em qual ordem?
- (A) `ROADMAP.md`?
- (B) `governance/CATALOGO-OFICIAL.md`?
- (C) último `DHR-*` ou ata de homologação?

**Sua resposta:**
```
[Escolha A/B/C + razão]
```

---

### D.3 — Conflito RAG vs ATOMIC-SPEC
**Pergunta:** Se um **chunk de RAG diz "score estrutural ≥60%"** e **ATOMIC-SPEC diz "convicção ≥70%"**, qual regra prevalece para **gate de Síntese**?

**Sua resposta:**
```
[escreva aqui]
```

---

## BLOCO E: Prioridade de Alinhamento

### E.1 — Urgência das emendas
**Pergunta:** Das 10 ações críticas listadas em DIAGNOSTICO-EXECUTIVO (GPR-001, CEM-001, GEN-1, RAG chunks, etc.), **qual precisa estar FEITA antes de SPEC-002 ser homologada**?

**Sua resposta:**
```
[liste 1–3 por ordem de bloqueio]
```

---

### E.2 — Risco aceitável
**Pergunta:** Qual **nível de risco de contaminação** você aceita em Specs futuras se não fizer alinhamento AGORA?
- (A) Nenhum — tudo deve estar resolvido antes de SPEC-002
- (B) Baixo — posso permitir piloto/iterativo em SPEC-002, mas deve estar fechado antes de SPEC-020
- (C) Moderado — agente continua auditar; gate é suficiente

**Sua resposta:**
```
[Escolha A/B/C + razão]
```

---

## BLOCO F: Decisões que NÃO podem ser inferidas

### F.1 — Fractal AGORA ou depois?
**Pergunta:** **Fractal precisa estar decidido ANTES de qualquer Elliott Spec, ou pode aguardar SPEC-010-014?** (Se não decidir agora, marca-se como UNRESOLVED e bloqueia Elliott.)

**Sua resposta:**
```
[AGORA / DEPOIS + motivo]
```

---

### F.2 — Orchestrator único
**Pergunta:** Você quer **uma única decisão formalizando "Orchestrator"** como termo em Rules (seja Master, Decision ou Cognitive), **ou cada componente mantém autonomia sem orquestrador central**?

**Sua resposta:**
```
[escreva aqui]
```

---

## Resumo para Sistematização

**Ao responder, você estará capturando:**
1. ✅ Intenção original (era software? sempre harness?)
2. ✅ Decisões que podem ser FECHADAS AGORA
3. ✅ Decisões que devem ser REABERTAS formalmente
4. ✅ O que é REFERÊNCIA/LEGADO vs BINDINANTE
5. ✅ Prioridade de alinhamento antes de próximas Specs

---

**Próximo passo após você responder:**
- Sistematizarei respostas em **5–7 decisões formais** (documento)
- Criarei **emendas** ou **tickets de decisão aberta** para Revisor/Andraus
- Gerar **plano de implementação** (semana 1: emendas críticas; semana 2: metadados; semana 3: validação)

---
