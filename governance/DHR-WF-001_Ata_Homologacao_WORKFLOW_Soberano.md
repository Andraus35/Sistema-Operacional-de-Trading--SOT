# DHR-WF-001 — Ata de Homologação — WORKFLOW.md soberano na raiz + conformidade (RULE-ECC-05) + detector D6

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Instrução direta de Andraus (chat, 2026-10-01): "WORKFLOW.md deve ficar na raiz e ser referência para o AGENTS.md"; "concordo… siga com os itens 1 e 2" |
| Data | 2026-10-01 |
| Status | **HOMOLOGADA — vigência imediata, prospectiva** (por instrução direta de Andraus em chat) |
| Compatibilidade | Minor (RULE-ECC-05 ganha cláusula de conformidade; não redefine baseline) |

---

## 1. Decisão

1. **`WORKFLOW.md` (raiz) = setup operacional soberano de Andraus.** Nome anterior: RUNTIME-WORKFLOW-SOT (em `reference/`). Conteúdo dos passos inalterado na v1.1; IDs estáveis `WF-xx`/`WF-Dxx`/`WF-Mxx`; versão vigente + changelog no cabeçalho; versão anterior arquivada em `docs/_legacy/`. Só Andraus altera o conteúdo.
2. **Item 1 — RULE-ECC-05, lente (3):** de *confronto* para ***confronto e conformidade***. A Spec que toca o pipeline cita por ID os `WF-xx` tocados, não contradiz nenhum e **não fecha `WF-Dxx` aberta**. Divergência = achado **Maior** do Revisor, resolvida por Andraus (nunca pela Spec). Propagado a `RULES.md`, `atomic-spec.md` (cabeçalho + §15), `especificador.md`, `revisor.md` (carimbo `sincronizado-até: DHR-WF-001`).
3. **Item 2 — detector D6 (`scripts/check_doc_sync.py`):** ID `WF-xx` citado e inexistente → ERRO; `WF-Dxx` aberta declarada fechada → ERRO (CONS-01); ID `[REVOGADO]` citado → WARN; versão citada ≠ vigente → WARN. Detector (ENF-03): não bloqueia, não fecha decisão; coberto por testes em `tests/test_check_doc_sync.py`.
4. **Whitelist de raiz (HOD-001 §6b.1)** emendado para incluir `WORKFLOW.md`.
5. **`AGENTS.md`** referencia o WORKFLOW.md (§1 tabela de leitura, §2 mapa, §5 detector).
6. **SPEC-003 congelada** (candidata v1.0, sem alteração de mérito) até o WORKFLOW.md v2; depois o Especificador reconcilia por delta. Na SPEC-003 só foram trocadas citações de caminho/ID.

## 2. Não decidido (CONS-01)

`WORKFLOW-SOT-001` segue **aberta**: WF-D01 (Killzone), WF-D02 (alarme-gatilho), WF-D03 (convicção macro × global × J-001), WF-D04 (papel do ICT). Resolução depende de Andraus (WORKFLOW.md v2).

## 3. Registro do Controlador (efeitos aplicados — 2026-10-01)

- [x] `WORKFLOW.md` v1.1 na raiz; `docs/_legacy/WORKFLOW-v1.0.md`.
- [x] `governance/RULES.md` (RULE-ECC-05), `atomic-spec.md`, `.claude/agents/*.md` (carimbo RPSA), `AGENTS.md`.
- [x] `governance/HOD-001_…_PROPOSTA.md` §6b.1 (whitelist).
- [x] `scripts/check_doc_sync.py` D6 + testes; `governance/CATALOGO-OFICIAL.md` (linha da ata).
- [x] Mapa, referências cruzadas, doc-sync revalidados.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
