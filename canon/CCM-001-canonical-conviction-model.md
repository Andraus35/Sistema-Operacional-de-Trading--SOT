# CCM-001 — Canonical Conviction Model Specification

**Status:** BASELINED — v1.0 (Andraus, 2026-10-02, DHR-SPEC003-001). Redigido pela SPEC-003 (Conviction Vector, Evidence Fusion Engine & Conviction Engine).
**Proveniência:** `specs/features/SPEC-003/plan.md` v1.5 (HOMOLOGADA) — esqueleto homologado transcrito aqui; nenhum conteúdo além do esqueleto (CC-02/CONST-01). Ata: `governance/DHR-SPEC003-001_Ata_Homologacao_SPEC-003.md`.
**Projeto:** SOT SISTEMA TRADING
**Categoria:** Modelo Canônico do Kernel Cognitivo
**Governança:** GMC-001 (RULE-GMC-001..005)

> **Nota de baseline (INV-09/CONS-01):** este documento é o **contrato canônico (estrutura/método/mecanismo)** da Convicção Global. Os **valores definitivos** — fórmula/pesos/limiares (**J-001**), pesos por ativo (**N-001**) e estados do Blackboard para objetos não-hipótese (**M-001**) — **permanecem DECISÕES ABERTAS**, não fixados aqui (pós-backtest). Os limiares-piloto ≥70% / 7-9 são **FATO NORMATIVO interino** (Questionário v1, recalibráveis). Dimensionalidade = **8** (Questionário v1, fechada). A substância normativa detalhada (BASpecs CF-001..013, RULE-CF-001..012, Enforcement Contracts, cenários D7/D8) vive na SPEC-003 homologada — este canon é o contrato de identidade/campos/fronteiras.

---

## Capítulo 1 — Identidade do Modelo

### Código
CCM-001

### Nome Oficial
Canonical Conviction Model

### Missão
Definir o padrão canônico de representação, cálculo, versionamento e auditabilidade da **Convicção Global** do SOT — o **Conviction Vector de 8 dimensões** e sua agregação explicável, robusta e não-compensatória —, preservando a **Separação Tríplice** (Evidence Strength × Hypothesis Confidence × Global Conviction), a **hierarquia analítica inviolável** (estrutural/Elliott precede e veta; agregação não-compensatória) e a fronteira **INV-04** (custo/dimensionamento NUNCA entram na convicção).

### Objetivo Estratégico
- Padronizar a Convicção Global como insumo decisional reutilizável e auditável;
- garantir explicabilidade da ponderação (PB-06) e rastreabilidade completa (P13/RULE-010);
- preservar a Separação Tríplice (não contaminação entre os três níveis — CHM-001 §1.9/§2.14);
- fornecer o **mecanismo** de convicção sobre subconjunto de dimensões (macro) e sobre o vetor completo (global), invocável pelo Manager Agent — Fase 2.

### Escopo
Aplica-se a toda Convicção Global publicada no ecossistema do SOT (BTC/XAU/NASDAQ — universal, GMC-001).

### Fora do Escopo (fronteiras)
- **Não redefine** CEM-001 (Evidence) nem CHM-001 (Hypothesis) — CC-02/CONST-01.
- **Não** faz Síntese/árbitro/TMP/Signal Package → Manager Agent — Fase 2 (SPEC-014) / Risk Agent.
- **Não** faz position sizing, alavancagem, R:R, Portfolio Heat, Kelly → Risk Agent (INV-04).
- **Não** executa ordem nem emite sinal (INV-05; SOT produz insumo decisional).
- **Não** fixa valores definitivos (J-001/N-001) nem estados do Blackboard para não-hipótese (M-001).

---

## Capítulo 2 — Relação com os Modelos Canônicos Vizinhos (Separação Tríplice)

| Nível | Modelo | Papel | Fronteira |
|---|---|---|---|
| Evidence Confidence / Strength | **CEM-001** (BASELINE) | Peso LOCAL do produtor (0.0–1.0), ≠ Convicção | Não redefinido pelo CCM-001 |
| Hypothesis Confidence | **CHM-001** (BASELINE) | Confiança da hipótese | Não redefinida; "Global Conviction definida pelo futuro CCM-001" (§2.14) |
| **Global Conviction** | **CCM-001** (este) | Convicção sistêmica agregada (Conviction Vector 8D) | Calcula a Global Conviction; não contamina os outros dois |

A Separação Tríplice é **inviolável** (INV-10): nenhum dos três níveis contamina o outro.

---

## Capítulo 3 — Esqueleto do Contrato (camadas) [proveniência: SPEC-003 §CCM-001]

| Camada | Conteúdo | Fronteira |
|---|---|---|
| Identidade | `conviction_id`, `version`, `previous_version_id`, `creation_timestamp`, `status` (COMPUTED/GATED_PASS/GATED_BLOCK/SUPERSEDED) | Imutável pós-publicação exceto `status` (padrão CEM-001 Cap.4); versionamento monotônico (INV-07) |
| Origem | `producer_id` = Conviction Engine; `source_evidence_ids` (ACTIVE/DERIVED consumidas); `hypothesis_ref` (Hypothesis Confidence lido, não redefinido) | Separação Tríplice |
| Conviction Vector 8D | `{estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica}` — cada dimensão: valor normalizado \| INDETERMINADO. A dimensão **`temporal`** hospeda a **feature de regime** (WF-C04 / Q-A9): tendência/range/alta vol. como contexto; INDETERMINADO se não classificável — nunca zero | Dimensionalidade = 8 fechada (Questionário v1); regime → `temporal` (Q-A9, ratificada DHR-SPEC003-001); valores/pesos = J-001/N-001 (abertos) |
| Agregação | `aggregation_method` (não-compensatória, estrutural-primeiro), `global_conviction`, `score`, `directional_conflict`, `robustness`, `sensitivity` | Fórmula/pesos/limiares definitivos = **J-001** |
| Gate | `gate_result` (pass/block), `thresholds_used` (piloto ≥70% / 7-9 interino) | Limiares definitivos = **J-001**; LLM nunca é o gate (ENF-03) |
| Rastreabilidade | `reconstruction` (dimensões→normalização→pesos→agregação→gate), `per_asset_weights_ref` (**N-001**) | P13/RULE-010 |
| Governança | GMC-001 (universal/neutro/reutilizável/baixo acoplamento) | RULE-GMC-001..005 |

> **Nota (N1/N3 — honestidade, DHR-SPEC003-001):** a **composição do `score` 0–9** (o que são os 9 itens e como mapeiam às 8 dimensões) é [DECISÃO NECESSÁRIA: dona J-001; BL-027/H-16]. A **proveniência da entrada do gate** (sobre qual valor o gate opera — valores por dimensão persistidos/recomputáveis vs. número agregado proposto) e o mecanismo de recomputação/`computed_by`/`gate_record` são [DECISÃO NECESSÁRIA: BL-029; donas Manager Fase 2/SPEC-004/SPEC-018]. A **Salvaguarda de Sinal 1** (hipótese sem nível de invalidação explícito → bloqueada) **não** é materializada como pré-condição do gate neste contrato [DECISÃO NECESSÁRIA: dona a definir por Andraus; BL-028].

---

## Capítulo 4 — Esquema I/O (lógico) do objeto Conviction Vector

```json
{
  "conviction_id": "CV-2026-10-01-001",
  "version": 1,
  "previous_version_id": null,
  "creation_timestamp": "2026-10-01T12:00:00Z",
  "status": "COMPUTED | GATED_PASS | GATED_BLOCK | SUPERSEDED",
  "producer_id": "conviction_engine",
  "source_evidence_ids": ["EV-A", "EV-C(DERIVED)"],
  "hypothesis_ref": "HY-...",
  "conviction_vector": {
    "estrutural": "0.0-1.0 | INDETERMINADO",
    "geometrica": "0.0-1.0 | INDETERMINADO",
    "fractal": "0.0-1.0 | INDETERMINADO",
    "institucional": "0.0-1.0 | INDETERMINADO",
    "operacional": "0.0-1.0 | INDETERMINADO",
    "temporal": {
      "value": "0.0-1.0 | INDETERMINADO",
      "regime": "trending | ranging | high_volatility | INDETERMINADO (feature de contexto — WF-C04/Q-A9; nunca zero; não é gate/veto; peso = J-001/N-001)"
    },
    "volume": "0.0-1.0 | INDETERMINADO",
    "historica": "0.0-1.0 | INDETERMINADO"
  },
  "aggregation_method": "non_compensatory_structural_first",
  "global_conviction": "0.0-1.0 (valores definitivos = J-001)",
  "score": "n/9 (composição definitiva = J-001/BL-027; 7/9 = limiar-piloto interino)",
  "directional_conflict": false,
  "robustness": "qualitativo/ordinal (métrica definitiva = J-001)",
  "gate_result": "PASS | BLOCK",
  "thresholds_used": { "conviction_min": "0.70 (piloto interino)", "score_min": "7/9 (piloto interino)" },
  "per_asset_weights_ref": "N-001 (aberto)",
  "reconstruction": { "...": "dimensões→normalização→pesos→agregação→gate" }
}
```

> `conviction_vector` tem exatamente **8 dimensões** (Questionário v1). A dimensão `temporal` **hospeda** a feature de regime (WF-C04/Q-A9), que **não** acrescenta 9ª dimensão (INV-03) nem é gate/veto (INV-01). Nenhum campo deriva de custo/sizing (INV-04) nem redefine Evidence Strength/Hypothesis Confidence (Separação Tríplice).

---

## Capítulo 5 — Decisões abertas internas ao CCM-001 (CONS-01)

| Decisão | Escopo | Estado |
|---|---|---|
| **J-001** | Fórmula/pesos/limiares **definitivos** do Conviction Vector (inclui calibração do desconto de dependência, peso/decay de aging, métrica de robustez, composição do `score`) | **ABERTA** — pós-backtest; dona do backtest/calibração a definir (BL-032) |
| **N-001** | Pesos por ativo **definitivos** (BTC/XAU/NASDAQ) | **ABERTA** — mecanismo especificado; valores pós-backtest |
| **M-001** | Estados do Blackboard para objetos não-hipótese (publicação do Conviction Vector) | **ABERTA** — SPEC-004 |

O CCM-001 fixa **estrutura/método/mecanismo + limiares-piloto interinos**; os valores definitivos são pós-backtest. Nenhuma decisão aberta é tratada como invariante fechado (INV-03/CONS-01).

---

## Capítulo 6 — Governança

Alteração deste modelo segue **GMC-001** (fluxo Estrategista → Analista → Controlador; RULE-GMC-001..005), com homologação de Andraus. CC-02/CONST-01 passa a incidir sobre o CCM-001 a partir desta baseline. Versionamento monotônico (INV-07): nada é deletado; refutações/substituições viram SUPERSEDED.
