# DHR-SPEC007-003 — Ata de Decisão — Respostas de Andraus às perguntas P-1..P-11 do Plan v1.2 da SPEC-007

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-007/plan.md` v1.2 (candidato, NÃO CONFORME), seção "Perguntas a Andraus" · `DHR-SPEC007-002` (divisão; P-7 resolvida por ela) · `DHR-SPEC007-001` (Q8) · pareceres R1-R3 em `governance/propostas/SPEC-007/` |
| Data | 2026-10-24 |
| Status | **DECISÕES DE POLÍTICA REGISTRADAS** (decisões diretas de Andraus em chat, 2026-10-24, por AskUserQuestion; todas na opção recomendada). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **NÃO homologa Plan nem baseline**: as regras só viram texto normativo no Plan reduzido da SPEC-007 / Plan da SPEC-048, depois de Revisor e homologação. |
| Compatibilidade | Minor (não toca modelo canônico baselined; não edita Spec baselined) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Registro de decisões de política de Spec em redação: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-24)
| # | Pergunta | Decisão | ID proposto pelo Plan | Destino |
|---|---|---|---|---|
| P-10 | Como o sistema reconhece uma decisão de Andraus | **Só a identidade confirmada de Andraus grava e aprova** os registros de ato (liberação de fonte, aprovação de lote, troca), até ele decidir delegar; não cria autoridade nova. A forma de confirmar a identidade fica para BUILD | SPEC-007-ACTREC-001 | SPEC-007 |
| P-4a | Quem libera o USO de cada fonte | **Só Andraus, fonte por fonte**; sem liberação a fonte fica registrada e parada. **Não decide o livro (Q7c segue adiada)** | SPEC-007-RIGHTS-001 | SPEC-007 |
| P-4b | Quem libera ENVIAR trechos a serviço de fora e o que é "fora" | **Só Andraus libera, fonte por fonte; o modelo de terceiro contratado pelo sistema conta como "fora"**; sem liberação a fonte não vai para fora, nem por cópia reescrita. Consequência aceita: linha parada até a 1ª liberação | SPEC-007-EXTTX-001 | SPEC-007 |
| P-11 | Derivado de fonte "proibida de sair" | **Fica proibido também** (regra mais restritiva); vale também para o "pode usar" | SPEC-007-DERIVTX-001 | SPEC-007 |
| P-1 | Quem segura a caneta do carimbo (Q8) | **Aprovado como regra** as 4 recomendações: Andraus aprova a lista de quem carimba; conferência de fidelidade por modelo diferente do formador; conferência separada de quem escreve; aprovação pessoal por lote só de definições e regras. **Decide parte de `SPEC-006 plan.md` l.482** (quem mantém a lista de quem grava); a governança do aprender-sozinho (K-001) segue ABERTA | (RULE-KFH-006/007 do Plan) | SPEC-007 |
| P-2 | O que é "alto impacto" | **Definições e regras** exigem visto por lote; o resto passa pela conferência automática; ficha sem classificação conta como alto impacto | (RULE-KFH-007 (v)) | SPEC-007 |
| P-3 | Em que gaveta do caderno entra o conhecimento de fontes | **Gaveta `learning` (aprendizado) por enquanto**, sem criar tipo novo; encaixe é [INFERÊNCIA] aceita por Andraus, sem emenda à ontologia da SPEC-006 | SPEC-007-NODETYPE-001 | SPEC-007 |
| P-8 | Quem autoriza trocar conhecimento já carimbado | **Só Andraus, por lote**; delegação posterior da troca de itens comuns à conferência automática é decisão futura dele | SPEC-007-SUCC-001 | SPEC-007 |
| P-5 | Fidelidade na avaliação geral (SPEC-020) | **Uma emenda por metade**, cada uma na homologação do Plan correspondente (F1 → SPEC-007; F2 → SPEC-048), por ato de Andraus; sem números de corte até calibrar. Nada emendado agora | — | SPEC-007 e SPEC-048 |
| P-6 | Duplicidade herdada da memória de experiência | **Reconciliação aceita**: "fontes repetidas contam como uma" fica aqui para **evidência**; para experiência fica na etapa futura do histórico de operações. **BL-011 segue `ATIVADO`**; encerrá-lo continua sendo só de Andraus | COL-EXP-05 | Spec que ficar com a independência de evidência (definir nos Plans) |
| P-9 | Onde o pacote de evidência é entregue | **Direto ao analista que pediu, só leitura, registrada**, sem ir ao quadro compartilhado; tipo no quadro só por emenda à parte (M-001 segue ABERTA) | SPEC-007-BBTYPE-001 | SPEC-048 |
| P-7 | Tamanho da Spec | **Resolvida pela divisão** (`DHR-SPEC007-002`) | SPEC-007-SPLIT-001 | — |

## 2. Efeitos nos Plans (a aplicar quando houver ordem de Andraus)
- O Plan reduzido da SPEC-007 e o Plan da SPEC-048 passam a tratar estas respostas como **decisões tomadas**; as marcas [DECISÃO NECESSÁRIA] dos IDs acima viram "decidida (DHR-SPEC007-003)". O fail-closed do Plan v1.2 deixa de ser "intervalo" e passa a ser a **regra**: nada vale sem registro de ato de Andraus (ACTREC), então a linha segue parada até a 1ª liberação real.
- As Médias R3-M1..M5 do Revisor **continuam abertas** e devem ser tratadas no Plan reduzido; estas decisões resolvem R3-M3 só na parte de "informar a Andraus" (a tabela de pré-requisitos mínimos ainda deve constar).
- `plan.md` v1.2 **não é editado nesta entrega** (candidato; INV-07).

## 3. Efeitos aplicados `[FATO]`
- `ROADMAP.md` ("Decisões FECHADAS"): segmento com ACTREC-001, RIGHTS-001, EXTTX-001, DERIVTX-001, NODETYPE-001, SUCC-001, BBTYPE-001 (decididas como política) e a parte da l.482 decidida por P-1; texto anterior preservado.
- `governance/CATALOGO-OFICIAL.md`: registro desta ata.
- **Não alterados** (por não terem ordem expressa): `governance/CONFLICT-MAP.md` (COL-EXP-05), `SPEC-006/plan.md` l.482 (baseline; a decisão fica aqui e em errata aditiva a propor), `SPEC-020`, painel RMR-001 (BL-011 inalterado).

## 4. Permanecem ABERTAS (CONS-01)
G-001 · **K-001** (a parte "aprender sozinho"; só a lista de carimbadores foi decidida por P-1) · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · "produtor/gatilho de promoção" (SPEC-006 `plan.md` l.976) · direito de uso do livro (Q7c) · forma de confirmar a identidade de Andraus (BUILD). **Nenhuma outra decisão aberta foi fechada.**

## 5. Registro
- [x] Esta ata · [x] ROADMAP · [x] CATALOGO · [ ] CONFLICT-MAP (sem ordem) · [ ] errata aditiva à SPEC-006 l.482 (a propor) · [ ] merge (assinatura) · [ ] Plan reduzido da SPEC-007 e abertura da SPEC-048 (só por ordem de Andraus)

---

**Andraus** — *decisões em chat, 2026-10-24; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
