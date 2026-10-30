# Parecer do Revisor — Errata aditiva v1.13 à SPEC-006 (R4, v1.3, delta curto) — 2026-10-25

> Transcrição pelo Orquestrador (Revisor sem Write). Alvo: `specs/features/SPEC-006/errata-v1.13.md` v1.3 (commit `66aa2d8`). Gates do Orquestrador: check_refs 0 ERRO, check_invariants 0, revisor_gate PASSOU_D, suíte completa OK, mapa em dia, `plan.md` intacto (`dd5a609f3007…`). Revisor não reproduz gate/hash (GATE NÃO VERIFICADO por ele). Adendo G1: o Revisor reabriu ROADMAP/AGENTS/ata; não localizou o caminho de RMR-001 (herdado do R3, que o conferiu) e atomic-spec/RULES foram pedidos no reenvio.

**VEREDITO: CONFORME condicional.** N1, N3, N4 resolvidos; N2 mantido; 1 Menor novo (N5), não bloqueia. Q-1..Q-11 aderentes à ata §4–§6; sem ramo condicional vivo; aditividade confirmada (54 ocorrências, todas em `errata-v1.13.md`); CONS-01 preservado. Condições: gate reproduzido pelo Orquestrador (feito: PASSOU_D, suíte OK) e homologação de Andraus (pendente). Observação: ratificar `SEAL_SUCCESSION_MISMATCH` no item 4(b) junto com a homologação.

- **N5 MENOR (C02)** — célula "Decisões de Andraus incorporadas": "seguem pendentes" no presente, já resolvido nos Adendos 2 e 3. Mecânico (FICHA-M).

<!-- ACHADOS-ESTRUTURADOS
N5|MENOR|C02|Cabeçalho l.9 mantém "Q-10 e o código SEAL_SUCCESSION_MISMATCH seguem pendentes" no tempo presente no corpo vivo, resolvido só pelas frases seguintes|Ao incorporar decisão posterior, datar ou atualizar a frase que registrava o estado anterior em vez de só acrescentar o adendo
-->

<!-- FICHA-M
{"achados":[
{"id":"N5","sev":"MENOR","arquivo":"specs/features/SPEC-006/errata-v1.13.md","antigo":"Q-10 e o código `SEAL_SUCCESSION_MISMATCH` seguem pendentes. `[FONTE]`","novo":"Q-10 e o código `SEAL_SUCCESSION_MISMATCH` seguiam pendentes à data do §4 (resolvidos nos Adendos 2 e 3, abaixo). `[FONTE]`","condicao":"texto antigo ocorre uma única vez, na célula 'Decisões de Andraus incorporadas' do cabeçalho (l.9); a ocorrência do Anexo V1.1 usa redação diferente"}
]}
-->
