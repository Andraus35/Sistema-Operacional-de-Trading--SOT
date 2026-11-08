# DHR-SPEC008-002 — Ata de Homologação — Manager Contract (MMC-001 v1.0)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-008/MANAGER-CONTRACT.md` v0.3 (361 linhas; commit `16b11f0`) · pareceres do Revisor em `governance/propostas/SPEC-008/`: R1 (NÃO CONFORME, 4 Médias), R2 (CONFORME condicional, 0 Média, por delta) e R3 (CONFORME condicional, 0 Média, 7 Menores; 6 aplicados como classe M) · `DHR-SPEC008-001` (abertura; §3 manda o contrato antes do Plan) · `DHR-EUA-E23` §2 item 2 (contrato comum do Manager) · `ADR-MANAGER-001` |
| Data | 2026-11-08 |
| Status | **MANAGER CONTRACT HOMOLOGADO — MMC-001 v1.0 — BASELINE** (decisão direta de Andraus por AskUserQuestion, 2026-11-08: "Homologar com condição (Recomendado)"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). Homologação **CONDICIONADA** (§4). *[Estado anterior preservado — INV-07: "PROPOSTA v0.3 — CONFORME condicional (R3); NÃO é baseline"]* |
| Compatibilidade | Minor (não toca modelo canônico baselined; nenhuma fonte editada — A-4) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de contrato de herança vertical: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-11-07 — confirmadas por esta homologação)
| # | Ponto | Decisão |
|---|---|---|
| A-1 | ID e versão | **MMC-001 v1.0**, a vigorar **a partir desta ata**. `ABERTURA.md` segue só como contexto não-baseline (hash `8ea5d9a`, fixado pelo Orquestrador) |
| A-2 | Spec de Tempo (candidata SPEC-050; número **não fixado**) | **Herda** do contrato (quarta filha, além de SPEC-015, SPEC-008 e SPEC-014) |
| A-3 | Lugar | `governance/`, com registro no `CATALOGO-OFICIAL.md` na entrega desta homologação |
| A-4 | Divergências de texto conhecidas (ADR §2.4/§3.3/§4.1/§4.2/§6/§7, WF-F01/F02/K02, RULE-DEC-01…) | O contrato declara **qual texto prevalece**; **nenhuma fonte é editada** (`WORKFLOW.md` só por Andraus) |
| A-5 | Alcance vertical das decisões da abertura | (1) CONF-1 / P-12 / CONF-5 = **fronteira vigente, não herança fixa** para SPEC-014/015, revisável só com homologação de Andraus na abertura delas; (2) **P-7**: parada por gasto **só por Andraus, nunca automática**, nas **três Fases**; "orçamento avisa e escala" fica só na SPEC-008/Spec de Tempo — **recorte confirmado por Andraus em chat, 2026-11-07** (o contrato o marca `[INFERÊNCIA]`; esta ata o registra como confirmado, atendendo ao parecer R3) |
| Homologação | MMC-001 v1.0 | **Homologar** (decisão desta ata) |

## 2. Efeitos aplicados (Orquestrador)
1. Mover o contrato para `governance/MMC-001_Manager_Contract.md` com `git mv` (**feito**) (histórico preservado); cabeçalho: ID **MMC-001**, versão **v1.0**, Status baseline, remover "PROPOSTA — não é baseline" **mantendo** o texto anterior em `[antes: …]` (INV-07). **Só o cabeçalho muda**; o corpo não é editado (INV-09 vale daqui em diante: mudança só por errata homologada).
2. `ROADMAP.md`: seção e tabela do §25 da SPEC-008 ("Manager Contract homologado"); item em "Decisões FECHADAS" (`SPEC-008-MMC-001`, A-1..A-5). **"Próximo trabalho autorizado" não muda** (precedente DHR-SPEC049-001).
3. `governance/CATALOGO-OFICIAL.md`: registro de MMC-001 v1.0 e desta ata.
4. Referências: corrigir ponteiros ao caminho antigo (`handoffs/`, `ABERTURA.md`, pareceres só com `[antes]`); rodar `check_refs.py`.
5. `python scripts/check_rpsa.py --register DHR-SPEC008-002 … --write` (classifica a ata nova); depois `check_rpsa.py`.
6. Handoff do ramo reescrito no mesmo commit (AGENTS.md §11). Mapa: `build_map.py` + `--check` (não commitar `docs/mapa/`).
7. Filhas (SPEC-014/015/008/Spec de Tempo) só podem declarar o pai como baseline **por ID + versão** (RULE-HV-01) a partir daqui.

## 3. O que esta ata NÃO afirma (condições de conformidade)
- Gate determinístico **não verificado**: o contrato não é `plan.md` e o `revisor_gate` é inerte em nuvem (teto CONFORME condicional). Comparação com o parecer R3 por git foi feita pelo Orquestrador, não pelo Revisor.
- Veracidade de `sources/` do Dossiê da SPEC-008: risco residual declarado. O chat não está no repositório (A-1..A-5 e o recorte da P-7 constam daqui).
- **Não** edita `WORKFLOW.md`, `AGENTS.md`, `canon/`, nem Spec baselined. **Não** cria regra, campo, estado, transição ou agente de trading além de A-1..A-5. **Não** abre o Plan da SPEC-008 (só por ordem expressa de Andraus). **Não** fixa o número SPEC-050.
- Tensão no canon registrada e **não resolvida** (§6.6 do contrato: pausa emergencial do CEE §9.3 × evento estruturalmente relevante) — CONST-01.

## 4. Condição da homologação `[FATO]` (escolha de Andraus, AskUserQuestion, 2026-11-08: opção (a))
**R3-m07 (Menor, C02, classe O, não bloqueante):** §3.1.3 e §8.2-bis tratam como obrigação a Classe D/C que `ABERTURA.md` §4 (l.140, l.25) chama de orientação; só "nenhuma H/P ⇒ volta a Andraus" é firme.
**Homologar com condição:** errata aditiva ao contrato, em passo à parte e por ordem de Andraus, preservando a modalidade (orientação × obrigação, RULE-SEM-03) em §3.1.3/§8.2-bis. Recomendação do Orquestrador aceita (precedente DHR-SPEC049-002 §3); o Revisor classificou o achado como não bloqueante. Os outros caminhos (corrigir antes; sem condição) foram oferecidos e **não** escolhidos.

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 · D-PCC-4 · P-11 e P-13 ("decidir depois") · dono da montagem do Signal Package (não fixado — contrato §5.6). **Nenhuma decisão aberta é fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] Confirmação de Andraus (AskUserQuestion 2026-11-08) · [x] `git mv` + cabeçalho MMC-001 · [x] ROADMAP · [x] CATALOGO · [x] RPSA · [x] handoff do ramo · [ ] merge (PR, CI verde — assinatura) · [ ] Plan da SPEC-008 (só por ordem de Andraus) · [ ] retrospectiva da SPEC-008 (`loop_ledger.py --retro-check SPEC-008`, antes de abrir outra Spec) · [ ] errata R3-m07 (se opção a)

---

**Andraus** — *homologação dada por AskUserQuestion, 2026-11-08; registro pelo Orquestrador.*
