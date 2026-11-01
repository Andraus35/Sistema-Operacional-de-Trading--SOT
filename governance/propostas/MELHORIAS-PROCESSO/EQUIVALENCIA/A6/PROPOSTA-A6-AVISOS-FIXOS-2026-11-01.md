# Proposta pré-testada — tratar os avisos permanentes (A6.2 reformulado)

> **Não normativo. NADA APLICADO.** Reformulação escolhida por Andraus (AskUserQuestion, 2026-11-01): sem contador, tratar avisos fixos. Aplicar exige nova ordem dele (`check_refs.py` está no selo e no CODEOWNERS). Não fecha decisão aberta (CONS-01).

Hoje restam **2 avisos fixos**, de causas diferentes:

| Aviso | Causa | Tratamento |
|---|---|---|
| `check_refs`: `SPEC-049/checks.md:8` "RULE sem definição: RULE-WRV-0" | **Falso positivo do detector**: o texto `RULE-WRV-0nn` é um placeholder de numeração; o detector lê só `RULE-WRV-0` e deixa o `nn` de fora | **Patch pronto** (2 arquivos): ignora o token que termina em `-0` seguido de `nn`/`NN`. Pré-teste em cópia isolada: `tests/test_check_refs.py` 27/27; WARN 1→0; **mutante morto**; `RULE-WRV-07` inexistente continua sendo achado |
| `check_doc_sync`: `SPEC-007/plan.md:2650` cita versão antiga do `WORKFLOW.md` | **Real, em baseline homologado** | **Não tocar.** Só por erratum da SPEC-007, que já consta nas pendências de Andraus (HANDOFF §10 item 4) |

Para aplicar o primeiro (por ordem dele): `git apply` dos 2 patches → `python -m unittest tests.test_check_refs` → `python scripts/gate_manifest.py --write` (muda só a linha do `check_refs.py`; arquivo no CODEOWNERS) → `MECANISMOS.json` (`verificado_em`, COE-14) → gates, mapa, handoff.

**Limite:** o segundo aviso continua até a errata da SPEC-007; não há como silenciá-lo sem decisão sobre baseline.
