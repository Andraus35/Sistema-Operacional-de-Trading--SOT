# ADR-MISSION-TYPES-001 — Tipos de Missão: Exploratória e de Validação
**Versão:** 1.0  
**Status:** HOMOLOGADO  
**Data:** 2026-09-26  
**Decisor:** Andraus  
**AEH:** HOC-003  
**Relacionado:** ADR-MANAGER-001

---

## 1. CONTEXTO

### 1.1 Problema original

O design legado (MOES Doc 09, GAS Doc 03) assumia que toda missão começa com uma **hipótese prévia** que é passada como contexto aos agentes analíticos. Isso criava um paradoxo circular:

- Para criar missão → precisa de hipótese
- Para formular hipótese → precisam dos agentes analíticos
- Para despachar agentes analíticos → precisa de missão

**Andraus identificou o problema:**  
> "Qual a razão de ter hipótese antes de haver análise dos agentes? Não são os agentes que tratarão evidências, formularão hipóteses e formarão convicção?"

### 1.2 Tensão subjacente

O paradigma do Harness Cognitivo estabelece que cada agente analítico:
- Trata evidências de seu domínio
- Formula hipóteses locais
- Gera Vetor de Convicção

O design legado assumia o inverso: hipótese global → agentes validam.

A resolução desta tensão exige dois tipos distintos de missão — não um único tipo que force uma dependência circular.

---

## 2. DECISÃO

### 2.1 Dois tipos de missão

Existem exatamente **dois tipos** de missão no SOT SISTEMA TRADING:

---

#### TIPO 1 — MISSÃO EXPLORATÓRIA

| Atributo | Valor |
|---|---|
| **Hipótese de entrada** | Nenhuma |
| **Trigger** | Evento de mercado / abertura de sessão / invalidação de hipótese anterior |
| **Comportamento do Manager Agent** | Despacha agentes SEM hipótese |
| **Comportamento dos agentes** | Formulam hipóteses locais livremente; publicam no Blackboard |
| **Output** | Hipótese dominante emerge da Fase 2 (Conviction) → TMP |
| **Papel no ciclo** | Ponto de partida de qualquer ciclo de análise |

**Fluxo:**
```
Trigger (mercado/sessão/invalidação)
      ↓
Manager Agent (Fase 0) → cria Missão Exploratória
      ↓
Manager Agent (Fase 1) → despacha agentes SEM hipótese
      ↓
Agentes: analisam evidências → formulam hipóteses locais → publicam Conviction Vectors
      ↓
Manager Agent (Fase 2) → arbitra convicções → hipótese dominante emerge → TMP
```

---

#### TIPO 2 — MISSÃO DE VALIDAÇÃO

| Atributo | Valor |
|---|---|
| **Hipótese de entrada** | SIM — hipótese dominante do ciclo anterior |
| **Trigger** | Conclusão de Missão Exploratória com hipótese dominante |
| **Comportamento do Manager Agent** | Despacha agentes COM hipótese como contexto |
| **Comportamento dos agentes** | Validam / refutam a tese; publicam convicção ao Blackboard |
| **Output** | TMP atualizado com convicção consolidada |
| **Papel no ciclo** | Refinamento iterativo após hipótese exploratória estabelecida |

**Fluxo:**
```
Hipótese dominante (de Missão Exploratória anterior)
      ↓
Manager Agent (Fase 0) → cria Missão de Validação com hipótese como contexto
      ↓
Manager Agent (Fase 1) → despacha agentes COM hipótese
      ↓
Agentes: validam/refutam → publicam Conviction Vectors com posição sobre hipótese
      ↓
Manager Agent (Fase 2) → consolida convicção → TMP atualizado
      ↓
[SE hipótese invalidada] → Manager Agent gera Plano B → nova Missão Exploratória
```

---

### 2.2 Ciclo completo de missões

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  Trigger inicial / invalidação                   │
│         ↓                                        │
│  MISSÃO EXPLORATÓRIA                             │
│  (agentes livres → hipótese emerge)              │
│         ↓                                        │
│  Hipótese dominante confirmada?                  │
│  ├── SIM → MISSÃO DE VALIDAÇÃO                   │
│  │         (agentes validam/refutam)             │
│  │         ↓                                     │
│  │   Hipótese mantida? → TMP → Bot              │
│  │   Hipótese refutada? → Plano B →             │
│  │         nova MISSÃO EXPLORATÓRIA             │
│  └── NÃO → nova MISSÃO EXPLORATÓRIA             │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 2.3 Resolução do paradoxo circular

| Situação | Design legado (paradoxo) | Design atual (resolvido) |
|---|---|---|
| Ciclo inicial | Precisa hipótese para criar missão ❌ | Missão Exploratória não requer hipótese ✅ |
| Ciclo subsequente | Idem ❌ | Missão de Validação usa hipótese do ciclo anterior ✅ |
| Invalidação | Não previsto ❌ | Plano B → nova Missão Exploratória ✅ |

---

## 3. OBJETO MISSÃO

Schema do objeto Missão (normalizado a partir de DCEBS Doc 13, Section 8):

```json
{
  "ID": "string",
  "Tipo": "Exploratória | Validação",
  "Objetivo": "string",
  "Hipotese_entrada": "null | HypothesisObject",
  "Estado": "Criada | Planejada | Delegada | Executada | Validada | Consolidada | Encerrada | Cancelada",
  "Dependencias": ["MissionID"],
  "Agentes_envolvidos": ["AgentID"],
  "Prioridade": "Alta | Média | Baixa",
  "Prazo": "timestamp",
  "Resultado": "null | TMP"
}
```

**Extensão normativa:** o campo `Tipo` e `Hipotese_entrada` são adições desta ADR ao schema legado. `Hipotese_entrada` é obrigatoriamente `null` para Missões Exploratórias.

---

## 4. JUSTIFICATIVA

### 4.1 Por que dois tipos e não um

Um único tipo forçaria a escolha entre:
- Sempre exigir hipótese (paradoxo circular para ciclos iniciais)
- Nunca exigir hipótese (desperdiça informação de ciclos anteriores)

Dois tipos resolvem ambos os casos sem comprometer nenhum.

### 4.2 Compatibilidade com Harness Cognitivo

O Harness Cognitivo exige autonomia analítica dos agentes. Na Missão Exploratória, esta autonomia é total — sem hipótese de entrada. Na Missão de Validação, a hipótese é *contexto*, não restrição — agentes podem e devem refutá-la se as evidências assim indicarem.

### 4.3 Resolução do legado

O conceito de missão dos documentos legados (GAS Doc 03, MOES Doc 09) é preservado em sua essência (ciclo de vida, objeto Missão, Campanhas Operacionais), mas decomposto nos dois tipos. Não é rejeição do legado — é refinamento.

---

## 5. ALTERNATIVAS CONSIDERADAS E REJEITADAS

### A1: Missão única com hipótese opcional
**Rejeitada.** Ambiguidade no comportamento dos agentes (devem ou não validar? quando há hipótese e quando não há?). Dois tipos explícitos eliminam esta ambiguidade.

### A2: Manter design legado (hipótese sempre precede missão)
**Rejeitada.** Paradoxo circular identificado por Andraus. Incompatível com autonomia analítica do Harness Cognitivo.

### A3: Eliminar o conceito de hipótese completamente
**Rejeitada.** Descarta informação valiosa de ciclos anteriores. Missões de Validação aproveitam hipóteses estabelecidas para refinamento eficiente.

---

## 6. CONSEQUÊNCIAS

### 6.1 Para specs futuras

- **SPEC-015** (Manager Agent): deve implementar lógica de decisão Tipo de Missão na Fase 0
- Specs dos agentes analíticos: devem documentar comportamento diferenciado por tipo de missão (hipótese como contexto disponível vs. ausente)

### 6.2 Para o objeto Missão

- Schema da DCEBS Doc 13 deve ser estendido com campos `Tipo` e `Hipotese_entrada`
- Campo `Hipotese_entrada = null` é canônico para Missões Exploratórias

### 6.3 Para o ciclo operacional

- Plano B (missão de contingência) é responsabilidade do Manager Agent Fase 0
- Campanhas Operacionais (conceito do MOES Doc 09) permanecem válidas como agrupamento de missões relacionadas

---

## 7. DECISÕES ABERTAS RELACIONADAS

| ID | Descrição | Status |
|---|---|---|
| MISSION-TRIGGER-001 | Quais eventos específicos de mercado disparam Missão Exploratória? | Aberta (SPEC-015) |
| MISSION-PLANB-001 | Estrutura e escopo do Plano B | Aberta (SPEC-015) |
| MISSION-CAMPAIGN-001 | Definição formal de Campanha Operacional no contexto dos dois tipos | Aberta (SPEC-015) |

---

*ADR-MISSION-TYPES-001 v1.0 · HOMOLOGADO por Andraus · 2026-09-26 · HOC-003*
