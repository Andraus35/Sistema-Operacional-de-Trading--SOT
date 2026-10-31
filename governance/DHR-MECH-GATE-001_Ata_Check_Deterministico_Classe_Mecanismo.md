# DHR-MECH-GATE-001 — Ata de Decisão — check determinístico da Classe/Mecanismo (STRUCT-14) e uso pelo Especificador

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-31): "Implementar" (duas vezes): 1ª = check determinístico de RULE-MECH-01..03; 2ª = recomendações de uso (Especificador roda o gate antes de entregar) |
| Data | 2026-10-31 |
| Status | **DECISÃO REGISTRADA** (ordem direta de Andraus em chat; AGENTS.md §10). Toca `scripts/validate_spec_sot.py`, `governance/GATE-MANIFEST.sha256`, `governance/MECANISMOS.json` e `.claude/agents/especificador.md` **por ordem expressa dele**. Prospectiva (INV-07). |
| Compatibilidade | Minor (acréscimo de check; nenhuma regra alterada). |
| RPSA-escopo | sim |
| RPSA-sync | propagado |
| RPSA-motivo | Altera o texto do agente Especificador (autopré-check §7: rodar o gate determinístico). |

## 1. Decisão `[FATO]`
- `[STRUCT-14]` em `validate_spec_sot.py`: Spec que cita `RULE-MECH-01` deve trazer blocos `CLASSE : D|H|P|C` com os campos mínimos de atomic-spec §10.6 (D: MECANISMO+CRITÉRIO 4Es · H: +BOUNDED LOOP+GATE DE SAÍDA · P: +BOUNDED LOOP · C: +GATE DE SAÍDA). Confere **presença**, não qualidade; 4Es e Classe C em risco baixo seguem com o Revisor (CC-11). Entra no gate do Revisor (Classe D, bloqueante) por herança.
- `tests/test_classe_mecanismo.py` (8 casos) no CI; selo `GATE-MANIFEST` regravado; `MECANISMOS.json` atualizado.
- `especificador.md` §7: o Especificador roda `python scripts/validate_spec_sot.py <plan.md>` (exit 0) antes de entregar; reprovação de STRUCT-14 corrige-se antes do Revisor.

## 2. Ressalvas `[FATO]`
- Não mede o valor do bounded loop (pesquisa web: 2–3 tentativas são defaults de framework, não norma; fontes de qualidade mista, sem Dossiê formal, não é baseline).
- Não retroage sobre SPEC-001/019/020. Os 14 Plans atuais passam.
- Não fechou nem abriu decisão alguma (CONS-01).

## 3. Registro
- [x] Esta ata · [x] validate_spec_sot.py · [x] teste + CI · [x] GATE-MANIFEST · [x] MECANISMOS.json · [x] especificador.md · [x] carimbo RPSA · [ ] merge (assinatura)
