# MODELO — Ata operacional curta (A7-lite; DHR-A7A4-001)

> Uso: mudança **puramente operacional**, ordenada por Andraus. **Não vale** (use a ata completa) se a mudança: altera `AGENTS.md`, `.claude/agents/*`, `governance/` normativo, `canon/`, `ROADMAP.md` ou `atomic-spec.md`; homologa Spec/baseline; abre/fecha decisão aberta (CONS-01); ou tem `RPSA-escopo: sim`. Dúvida ⇒ ata completa. **Teto: 15 linhas de corpo (a tabela de campos não conta).** Os campos `Data` e `RPSA-*` ficam em linhas próprias porque `check_rpsa.py --register` os lê. O arquivo continua `governance/DHR-<ID>_Ata_<Tema>.md` (HO-06, RPSA, COE e o mapa seguem valendo).

```
# DHR-<ID> — Ata operacional curta — <tema>
| Campo | Valor |
|---|---|
| De | Andraus (registro pelo Orquestrador) |
| Data | AAAA-MM-DD |   <!-- linha própria: o check_rpsa --register lê `| Data |` -->
| Ordem | "<citação literal curta>" — <onde: chat / AskUserQuestion> |
| Status | **REGISTRO DE DECISÃO OPERACIONAL**. Não fecha nem abre decisão do ROADMAP (CONS-01). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | <uma frase> |
## Mudança  (arquivos, ≤ 5 linhas)
## Verificação  (gates rodados e resultado, 1–3 linhas)
## Não toca  (reservados e decisões abertas, 1 linha)
```
