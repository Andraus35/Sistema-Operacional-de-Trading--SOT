# HOMOLOGADO — ADR-CONFLUENCE-001 v3
## Status: ✅ HOMOLOGADO por Andraus em 2026-09-26

---

Registro consolidado. Produzo agora a **ENTREGA 2** para o Claude Code.

---

# ENTREGA 2 — Draft para Claude Code (Especificador)
## Em voz de Andraus | Para incorporação ao Harness

---

**DECISÃO ARQUITETURAL — ADR-CONFLUENCE-001 v3**
**Autoridade:** Andraus (Decisor Final)
**Data:** 2026-09-26
**Status:** HOMOLOGADA

---

### 1. RENOMEAÇÃO E EXTINÇÃO

- `fractal-skill` → **EXTINTA**
- `fibonacci-skill` (skill única) → **EXTINTA**
- Fractal Confluence Engine (FCE) → **CONCEITO ABSORVIDO** por `confluence-elliott`
- Agente de Síntese / CES (Conviction Engine) → **RENOMEADO** para **Agente Decisor**

---

### 2. NOVO CATÁLOGO DE SKILLS — STRUCTURAL AGENT

O Structural Agent passa a ter 4 skills:

```
elliott-skill              — contagem e score Elliott por grade (MTF: S1/D1/H4/H1)
level-fibonacci-skill      — valida Elliott com níveis Fibonacci; extensível a outras matérias futuras
confluence-fibonacci-skill — mede confluência de níveis Fibonacci entre timeframes (MTF: S1/D1/H4/H1)
confluence-elliott         — mede confluência das hipóteses Elliott entre timeframes (MTF: S1/D1/H4/H1)
```

Cada skill produz seu próprio score. O conjunto de scores compõe o **Vetor de Convicção Estrutural**.

---

### 3. CONFLUENCE-SKILLS POR AGENTE

```
confluence-elliott         → Structural Agent     [MTF: S1/D1/H4/H1]
confluence-smc             → Institutional Agent  [MTF: S1/D1/H4/H1]
confluence-ict             → Operational Agent    [Single TF: M5]
```

**Regra:** Confluência é **interna à matéria de cada agente**. Nenhuma confluence-skill cruza matérias de agentes distintos.

**Escopo temporal por agente:**
- Structural Agent e Institutional Agent → multi-timeframe (S1/D1/H4/H1)
- Operational Agent → single timeframe (M5 apenas)
- `confluence-ict` mede confluência entre **conceitos ICT dentro do M5**, não entre timeframes

---

### 4. ARQUITETURA DE PUBLICAÇÃO — BLACKBOARD

```
Structural Agent    → publica Vetor de Convicção Estrutural    → BLACKBOARD
Institutional Agent → publica Vetor de Convicção Institucional → BLACKBOARD
Operational Agent   → publica Vetor de Convicção Operacional   → BLACKBOARD
                                    ↓
                            AGENTE DECISOR
                      (lê Blackboard, forma Convicção Global,
                       emite decisão operacional final)
```

---

### 5. O QUE NÃO ESTÁ DEFINIDO AQUI

As camadas internas de cada `confluence-skill` (o que cada uma mede, seus inputs, processo e output detalhado) **serão especificadas em SPECs próprias**, abertas quando cada skill for desenvolvida. Esta decisão registra apenas a arquitetura macro.

---

### 6. IMPACTO EM DOCUMENTOS EXISTENTES

O Especificador deve atualizar referências nos seguintes artefatos:

| Artefato | Impacto |
|----------|---------|
| `FCES` (Doc 05 ENGENHARIA_GERAL) | LEGADO — substituído por `confluence-elliott` |
| `CES` (Doc 06) | Renomear para **Agente Decisor** em todas as referências |
| Qualquer menção a `fractal-skill` | Substituir por `confluence-elliott` |
| Qualquer menção a `fibonacci-skill` | Separar em `level-fibonacci-skill` e `confluence-fibonacci-skill` |
| Conviction Vector 7D/8D | Revisar dimensões — dimensão 6.3 "Fractal" muda de posição/nome |
| Schemas e specs que referenciam FCE | Atualizar para `confluence-elliott` |

---

**FIM DA ENTREGA 2**

---

Andraus, a decisão está registrada e o draft está pronto para o Especificador. Próximo tema da auditoria?