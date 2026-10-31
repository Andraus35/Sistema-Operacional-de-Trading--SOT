# DHR-SPEC049-001 — Ata de Homologação — Abertura da SPEC-049 (WikiRAG Reading View)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Proposta `specs/features/SPEC-049/ABERTURA.md` (Revisão 3) + Dossiê `research.md` + `sources/` (14 SRC + 6 REPO) · pareceres do Revisor `governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-ABERTURA-R1-2026-10-31.md` (NÃO CONFORME, 1 Média + 8 Menores), `...-R2-...` (CONFORME condicional, 2 Menores, integral) e `...-R3-...` (CONFORME condicional, 1 Menor, por delta); gate completo do Orquestrador = PASSOU_D · `DHR-SPEC048-001` (Q-2, C-1..C-3: origem do slot) · `DHR-SPEC007-001` (Q3) · `DHR-DIMENSIONAMENTO-001` (RULE-ECC-07) · `DHR-DELTA-HASH-001` |
| Data | 2026-10-31 |
| Status | **ABERTURA HOMOLOGADA** (decisão direta de Andraus em chat, 2026-10-31, por AskUserQuestion: "Homologar a abertura"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **NÃO é baseline** — o Plan ainda não foi escrito e só inicia por ordem de Andraus. Homologação **CONDICIONADA** (§3). |
| Compatibilidade | Minor (não toca modelo canônico baselined; nenhuma Spec baselined editada) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de abertura de Spec: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-31)
| # | Pergunta | Decisão |
|---|---|---|
| Ordem | Abrir a SPEC-049 | **Abertura ordenada** (chat, 2026-10-31, "Abrir a SPEC-049") |
| P-1 | Peso | **ALTO: HIGH D0–D7** (D6 N/A), com teste escrito para cada regra, inclusive a trava herdada "compilação WikiRAG" (E3); MEDIUM D0–D5 do slot **rejeitado** |
| P-7 | Tamanho | **Um documento só**; Andraus **confirma o encosto** no limiar de 1.600 linhas da RULE-ECC-07 (estimativa ≈1.570, faixa 1.420–1.620; proporcional ≈1.610) |
| P-2 | Quem lê | **Só pessoas** (Andraus, auditoria); analistas e Manager continuam usando só o pacote da SPEC-048 |
| P-3 | Trecho da fonte original | **Sem copiar trecho** (opção A): mostra o conhecimento carimbado e o endereço da fonte |
| P-4 | Organização | **Campos fixos** já conhecidos do sistema; sem campo ⇒ "sem classificação" (escola ausente ⇒ INDETERMINADA; CKG-STRUCT-ORIGIN-001 segue aberta) |
| P-5 | Guardar ou refazer | **Refeita na hora**, a pedido, para a data escolhida; guarda-se só o registro de montagem (entrada, regra, hash do resultado) |
| P-6 | Mostrar para fora | **Não sai da casa** (distribuição fora do escopo; decisão à parte se um dia for desejada) |
| C-1 | "Texto de modelo" | **Confirmado**: vale para texto **novo** escrito na hora de montar; o texto já carimbado é o que a página mostra |
| C-2 | Identificador | **`reading_view_ref`** (nome que os testes da SPEC-048 já usam) |
| C-3 | Onde mora a trava | **Declarada na SPEC-049** (herança, CC-08 `[INFERÊNCIA]`), **sem** editar a SPEC-007; nota aditiva na SPEC-007 só se Andraus pedir |
| C-4 | Duas datas na página | **Confirmado**: "o que o sistema sabia até" (corte) e "o que estava valendo em" (`valid_at`); se a segunda não for informada, recebe o mesmo instante do corte, anotado no registro de montagem; nunca o relógio |
| Menores | R2-m01/m02 | **Corrigir antes** (feito na Revisão 3, conferido pelo Revisor no R3) |
| Homologação | Abertura | **Homologar a abertura** (decisão desta ata) |

## 2. Efeitos aplicados `[FATO]`
- `ROADMAP.md`: SPEC-049 "ABERTURA HOMOLOGADA; Plan pendente, só por ordem de Andraus; não é baseline" (seção e tabela do §25); "Decisões FECHADAS": `SPEC-049-ABERTURA` (P-1..P-7, C-1..C-4). A linha de "Próximo trabalho autorizado" **não** foi alterada (o próximo autorizado segue sendo o que Andraus ordenar). Texto anterior preservado (INV-07).
- `governance/CATALOGO-OFICIAL.md`: registro desta ata.
- **Nada** alterado em `backlog/RMR-001_Painel_Backlog.md` (nenhum gatilho re-apontado; `backlog_triggers --abertura SPEC-049` = 0 itens), `CONFLICT-MAP.md`, `WORKFLOW.md` nem em Specs baselined.

## 3. Condições do Plan da SPEC-049 `[FATO]`
As condições 1–14 do `ABERTURA.md` §15 (inclui: derivar a janela de validade do item da SPEC-006/007 sem inventar campo — cond. 13; declarar reutilização do código da SPEC-007 ou código próprio `WRV` e de quem é o identificador — cond. 14; ENF-07 para a unidade E3; justificativa CC-11 para Classe C/E3; limitação declarada de R-9; medida do corpo do Plan contra a RULE-ECC-07) **mais**:
- **R3-m01 (Menor do R3):** alinhar a linha "Validade do Dossiê" do cabeçalho do `research.md` (l.10) a "HIGH decidido, validade 2027-01-29" (texto antigo em `[antes:]`) — correção a fazer **junto com** o Plan, antes de qualquer parecer sobre ele.
- Plan em HIGH com **teto de 2.000 linhas de corpo** e alerta em 1.900 (RULE-ECC-07); acima, divisão proposta a Andraus antes de seguir.

## 4. Condições de conformidade (o que esta ata NÃO afirma)
- Homologa a **abertura** (número, nome, peso, fronteira, quantidade, perguntas, disposições propostas); **não** escreve nem aprova Plan, **não** é baseline, **não** altera Spec baselined.
- O Revisor não executou o gate (teto CONFORME condicional); o Orquestrador rodou o gate completo = PASSOU_D. Veracidade das fontes web e a possível adulteração de `sources/` são risco residual declarado; o Benchmark não foi lido. Validade do Dossiê (HIGH, ECC-VAL-001): 90 dias a contar de 2026-10-31 → **2027-01-29**.
- As respostas de Andraus constam desta ata a partir do chat; o chat não está no repositório (observação do Revisor R3).

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 (residual) · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção · forma de confirmar a identidade de Andraus (BUILD). **Nenhuma decisão aberta foi fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] ROADMAP · [x] CATALOGO · [ ] merge (assinatura) · [ ] Plan da SPEC-049 (só por ordem de Andraus) · [ ] retrospectiva da SPEC-049 (LOOP-001 passo 5; ao fechar a Spec)

---

**Andraus** — *decisões em chat, 2026-10-31; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
