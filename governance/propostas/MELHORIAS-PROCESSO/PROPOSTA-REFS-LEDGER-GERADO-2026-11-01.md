# Proposta — Referências ao `LEDGER-ACHADOS.md` (gerado, não versionado) no `check_refs`

> **Não normativo. PROPOSTA PRÉ-TESTADA — NADA APLICADO.** Pedido: Andraus (AskUserQuestion, 2026-11-01: "Preparar tudo para próxima sessão"). Não fecha decisão aberta (CONS-01).

## 1. Problema (medido 2026-11-01, `main` em `b1b0e1b`)
Desde o PR #164 (`DHR-LEDGER-GERADO-001`) o `governance/aprendizado/LEDGER-ACHADOS.md` é **gerado e ignorado pelo git** (`.gitignore:51`). Quatro documentos antigos ainda o citam, e `python scripts/check_refs.py` dá **ERRO=2 WARN=3**:
| Onde | Nível | Tipo de arquivo |
|---|---|---|
| `governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R3-2026-10-24.md:31` | ERRO | parecer histórico |
| `specs/features/SPEC-049/ABERTURA.md:98` | ERRO | **abertura homologada (baseline)** |
| `governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-DIMENSIONAMENTO-DE-SPEC-2026-10-31.md:71` | WARN | proposta |
| `.../PROPOSTA-EXPERIMENTO-REGRA-DE-PARADA-2026-10-31.md:9` | WARN | proposta |
O passo de refs no CI é **informativo** (`continue-on-error`), então nada bloqueia; mas o ERRO "quebra em doc vivo" por definição e esconde erros reais.

## 2. Opções
| # | Opção | Toca | Resultado | Risco |
|---|---|---|---|---|
| **A** (recomendada) | Acrescentar o caminho a `GENERATED_LOCAL` em `scripts/check_refs.py` l.201 (a lista de "artefatos gerados e ignorados pelo git", A2.1, já existe só com `docs/mapa/mapa-projeto.json`) + 1 teste espelhando `test_artefato_gerado_local_nao_e_caminho_quebrado` (`tests/test_check_refs.py` l.51–59) | `scripts/check_refs.py` (**SELADO**: regravar `GATE-MANIFEST.sha256`, linha 13) | **ERRO 2 → 0, WARN 3 → 1** (pré-teste em memória, abaixo) | baixo; mesma regra do A2.1, não mexe nos documentos |
| B | Editar os 4 documentos (trocar o caminho por "ledger gerado") | 1 **baseline** (`SPEC-049/ABERTURA.md`) exige erratum homologado; os outros 3 são propostas/parecer | zera os 4 | alto: erratum de baseline por uma referência a arquivo gerado; mexe em texto histórico (INV-07) |
| C | Deixar como está | — | ERRO=2 permanente (informativo) | esconde erro real futuro |
**Pré-teste (feito, nada gravado):** carregar `check_refs.py` como módulo, acrescentar `governance/aprendizado/LEDGER-ACHADOS.md` a `GENERATED_LOCAL` em memória e rodar: antes `ERRO=2 WARN=3`; depois `ERRO=0 WARN=1` (o WARN que sobra é `PLANO-F2-2026-11-01.md:188`, "schemas/evento-ac.schema.json", dos logs).

## 3. Passos prontos para a próxima sessão (precisam de ordem de Andraus)
1. `scripts/check_refs.py` l.201: `GENERATED_LOCAL = {"docs/mapa/mapa-projeto.json", "governance/aprendizado/LEDGER-ACHADOS.md"}`.
2. `tests/test_check_refs.py`: novo teste copiando l.51–59 para o ledger.
3. `python scripts/gate_manifest.py --write` (muda só a linha 13) e `--check`.
4. Ata **curta** não vale (toca script selado): ata completa (ID a definir na sessão), `check_rpsa.py --register … --scope nao`, `MECANISMOS.json` (nota de `det.check-refs`), suíte, PR sem mesclar.
5. Opcional, separado: o WARN do `PLANO-F2` l.188 cita o esquema numa pasta antiga (decisão tomada: o esquema ficou ao lado do módulo, em `scripts`); texto histórico da proposta, só nota aditiva.
**Recomendação: A.** Declarado: o ERRO do `SPEC-049/ABERTURA.md` é baseline; a opção A evita mexer nele.
