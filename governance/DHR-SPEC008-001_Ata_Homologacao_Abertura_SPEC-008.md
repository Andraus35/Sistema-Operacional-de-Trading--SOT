# DHR-SPEC008-001 — Ata de Homologação — Abertura da SPEC-008 (Manager — Orquestração Mecânica, Fase 1)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Proposta `specs/features/SPEC-008/ABERTURA.md` (com §16/§16-bis, respostas aos pareceres) + Dossiê `research.md` + `sources/` (14 SRC + 5 REPO) · pareceres do Revisor em `governance/propostas/SPEC-008/` (R1 NÃO CONFORME, 5 Médias → R2 NÃO CONFORME, 1 Média + adendo G1 → **R3 CONFORME condicional**, 1 Menor aplicado como classe M) · `DHR-EUA-E23` (3 Specs do Manager) · `DHR-DIMENSIONAMENTO-001` (RULE-ECC-07) · `DHR-SPEC049-001` (precedente de forma) |
| Data | 2026-11-07 |
| Status | **ABERTURA HOMOLOGADA** (decisão direta de Andraus em chat, 2026-11-07: "Homologo a abertura da SPEC-008"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **NÃO é baseline** — o Plan não existe e só inicia por ordem de Andraus. Homologação **CONDICIONADA** (§3). |
| Compatibilidade | Minor (não toca modelo canônico baselined; nenhuma Spec baselined editada) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de abertura de Spec: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]`
Escolha da Spec: SPEC-008 como próxima (chat, 2026-11-07). Respostas dadas em chat na mesma data e **confirmadas pela homologação** da `ABERTURA.md` como está:

| # | Tema | Decisão |
|---|---|---|
| P-1 | Peso do despachante | **CRITICAL D0–D8** (com suíte de ataque D8) |
| P-2 | Divisão | **Duas Specs**: SPEC-008 "Despacho e Ciclo" e **Spec de Tempo** (relógio, Killzone, alarme-gatilho; HIGH D0–D7; número candidato **SPEC-050**, livre no ROADMAP); o mesmo Dossiê vale para as duas |
| P-3 | Tamanho | SPEC-008 em **um documento só** (≈1.895 linhas, encosto no alerta de 1.900; teto 2.000, RULE-ECC-07) |
| P-4..P-9 | Manager Contract, "conclusiva", livro de bordo, orçamento, origem do preço do alarme, relógio/mercado fechado | **Seguir as recomendações do Especificador** (`ABERTURA.md` §13) |
| P-10 | Killzones (BL-026) | **Manter a tabela atual** como valor-padrão editável |
| P-11 | Fibonacci/Fractal no roteiro | **Decidir depois** (opção C; roteiro como dado versionado) |
| P-12 | "Resetar o alarme" | **Só encerrar** (opção C): alarme termina "usado"/"vencido"; ciclo termina registrado; P-12.1 não se aplica |
| P-13 | Reentrada após stop | **Decidir depois** (opção C; vai à abertura da SPEC-015/SPEC-014) |
| CONF-1..5 | Dono da FSM por trecho, 1ª leitura de convicção, ICT fora da Killzone, setup × direção do contexto, dono de abrir/fechar Killzone | **Seguir as recomendações do Especificador** |
| Homologação | Abertura | **Homologar a abertura** (decisão desta ata) |

## 2. Efeitos aplicados `[FATO]`
- `ROADMAP.md`: SPEC-008 "ABERTURA HOMOLOGADA; Plan pendente, só por ordem de Andraus; não é baseline" (seção e tabela do §25); "Decisões FECHADAS": `SPEC-008-ABERTURA` (P-1..P-13, CONF-1..5). A linha de "Próximo trabalho autorizado" **não** foi alterada. Texto anterior preservado (INV-07).
- `governance/CATALOGO-OFICIAL.md`: registro desta ata. `governance/rpsa-ledger.json`: entrada desta ata.
- **Nada** alterado em `WORKFLOW.md`, `backlog/RMR-001_Painel_Backlog.md` (as disposições BL-026/043/044/045/046 seguem **propostas**, declaradas no Plan), `CONFLICT-MAP.md` nem em Specs baselined.

## 3. Condições do Plan da SPEC-008 `[FATO]`
- Plan só por **ordem expressa de Andraus**; antes, o **Manager Contract** curto (P-4, recomendação) para homologação conjunta.
- Condições do CONFORME condicional R3: (i) gate determinístico (`validate_spec_sot.py`) a rodar sobre o `plan.md` quando existir; (ii) **J-001/N-001** abertas — o limiar de contexto "conclusivo" fica como parâmetro a preencher, sem número inventado; (iii) escolhas acima registradas.
- Plan com **teto de 2.000 linhas de corpo**, alerta em 1.900 (RULE-ECC-07); acima disso, dividir depois de começar = **nova abertura** (volta a Andraus; o Plan antigo fica congelado).
- A Spec de Tempo tem Plan próprio, **depois** do da SPEC-008; a interface entre as duas entra como requisito `[PROPOSTA]`. A errata de re-apontamento (`ABERTURA.md` §8) cai só no Plan da SPEC-008.
- Dossiê válido até **2027-02-05** (HIGH/CRITICAL: 90 dias a contar de 2026-11-07, ECC-VAL-001).
- Antes de abrir outra Spec: retrospectiva da SPEC-008 (`loop_ledger.py --retro-check SPEC-008`).

## 4. Condições de conformidade (o que esta ata NÃO afirma)
- Homologa a **abertura** (número, nome, peso, fronteira, divisão, quantidade, respostas, disposições propostas); **não** escreve nem aprova Plan, **não** é baseline, **não** altera Spec baselined, **não** edita o `WORKFLOW.md`.
- P-11, P-12, P-13, CONF-1 e CONF-5 tocam texto do `WORKFLOW.md`: ele **não** foi editado e nenhum estado/transição foi criado; só Andraus decide e edita.
- O Revisor não executou o gate (ferramenta indisponível em nuvem; abertura sem `plan.md`). Veracidade das fontes web e possível adulteração de `sources/` são risco residual declarado.
- As respostas de Andraus constam desta ata a partir do chat; o chat não está no repositório.

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 · D-PCC-4. **Nenhuma decisão aberta foi fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] ROADMAP · [x] CATALOGO · [x] RPSA · [ ] merge (assinatura) · [ ] Manager Contract e Plan da SPEC-008 (só por ordem de Andraus) · [ ] retrospectiva da SPEC-008 (ao fechar a Spec)

---

**Andraus** — *decisão em chat, 2026-11-07; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
