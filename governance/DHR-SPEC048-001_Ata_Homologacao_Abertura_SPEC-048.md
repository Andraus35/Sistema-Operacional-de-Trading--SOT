# DHR-SPEC048-001 — Ata de Homologação — Abertura da SPEC-048 (RAG Retrieval & Evidence Packet Harness) e slot da SPEC-049 (WikiRAG Reading View)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Proposta `specs/features/SPEC-048/ABERTURA.md` (Revisão 4) + Dossiê `research.md` + `sources/` · pareceres do Revisor `governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-ABERTURA-R1-2026-10-24.md` (CONFORME condicional, 10 Menores) e `...-R2-2026-10-24.md` (CONFORME condicional, 7 Menores; corrigidos na Revisão 4; gate completo do Orquestrador = PASSOU_D) · `DHR-SPEC007-002` (divisão; D3 número e nome da SPEC-048) · `DHR-SPEC007-003/004/005` |
| Data | 2026-10-24 |
| Status | **ABERTURA HOMOLOGADA** (decisão direta de Andraus em chat, 2026-10-24, por AskUserQuestion: "Homologar a abertura"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **NÃO é baseline** — o Plan ainda não foi escrito e só inicia por ordem de Andraus. **SPEC-049 = slot indicativo, NÃO aberta.** Homologação **CONDICIONADA** (§4). |
| Compatibilidade | Minor (não toca modelo canônico baselined; notas aditivas sem mudar regra) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de abertura de Spec e registro de slot: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-24)
| # | Pergunta | Decisão |
|---|---|---|
| Ordem | Abrir a SPEC-048 | **Dossiê de abertura ordenado** (chat, 2026-10-24, "Abrir a SPEC-048: Dossiê de abertura"); fecha o m-09 do R1 |
| Q-1 | Peso | **Peça crítica: CRITICAL D0–D8**, com teste de ataque completo |
| Q-2 | Uma Spec ou duas | **Separar já a página de leitura (WikiRAG)** numa Spec própria: **SPEC-049 — WikiRAG Reading View** (número e nome decididos por Andraus; escolha **contra** a recomendação do Especificador). A SPEC-048 fica com busca, contagem de fontes independentes, pacote, entrega e conferência de frases (F2) |
| Q-3 | Analista que roda em modelo de fora | **Aceitar o padrão, sem exceção**: todo analista conta como "fora" até Andraus confirmar modelos de casa (P-12); cada analista só recebe trechos de fontes liberadas para envio externo; o resto vem como "falta declarada"; o registro analista↔modelo é criado no detalhamento |
| Q-4 | Rótulo no pacote | **Sim**: cada item diz se é "conhecimento carimbado" ou "só trecho de fonte" |
| Q-5 | Resumo curto junto do pacote | **Existe no desenho, DESLIGADO até Andraus mandar ligar** |
| Q-6 | Gatilho do backlog | **Autorizado o acréscimo aditivo** `∨ spec:SPEC-048 em redação` na coluna de gatilho de BL-017 e BL-010 (gatilho antigo preservado; Estado inalterado; sem promoção) |
| Q-7 | Correção de endereço em Specs aprovadas | **A ata registra a REGRA DE BUSCA** (critério 1: "SPEC-007" junto de retrieval/recuperação/evidence candidate/pacote/RAG faithfulness, em Spec baselined ou errata homologada; critério 2: "SPEC-048" junto de WikiRAG/página de leitura, em Spec baselined ou ata → Spec da página) e a errata, proposta no Plan da SPEC-048, corrige o que a busca achar na hora de ser escrita |
| Q-8 | Conferência com o WORKFLOW | **Conferir com o WORKFLOW sem pesquisar escolas** (RULE-ECC-05 não incide; confronto voluntário; WF-D03 segue ABERTA) |
| C-1 | Corte do insumo do Anexo T entre as duas Specs | **Confirmado**: as partes só da página de leitura (RULE-KFH-015 e cláusulas de 2 regras, EARS 15, BASpec-KFH-015, EC-KFH-009, T21, partes de 2 ADV) vão à SPEC-049; o resto fica na SPEC-048 |
| C-2 | Peso e Classe da SPEC-049 | **Só como proposta** (MEDIUM D0–D5, Classe D) **até a abertura dela**, depois do Dossiê próprio; atenção registrada: ela herda a trava "compilação WikiRAG" (E3 na SPEC-007) |
| C-3 | Correção de endereço | **Autorizada a nota aditiva agora** (sem apagar nada) nos pontos listados em `ABERTURA.md` §12 |

## 2. Efeitos aplicados `[FATO]`
- `ROADMAP.md`: SPEC-048 "ABERTURA HOMOLOGADA; Plan pendente, só por ordem de Andraus; não é baseline" (linha de "Próximo trabalho autorizado" não alterada — o próximo autorizado segue sendo o que Andraus ordenar); **SPEC-049 registrada como slot indicativo, NÃO aberta** (seção e tabela do §25); notas aditivas nas l.189/l.517 (página de leitura → SPEC-049); "Decisões FECHADAS": `SPEC-048-ABERTURA` (Q-1..Q-8, C-1..C-3). Texto anterior preservado.
- `governance/CATALOGO-OFICIAL.md`: registro desta ata.
- `backlog/RMR-001_Painel_Backlog.md`: BL-017 e BL-010 — acréscimo aditivo `∨ spec:SPEC-048 em redação` na **coluna de gatilho**; Estado **inalterado** (`Em espera`); sem promoção.
- Notas aditivas (C-3, sem mudar regra): `specs/features/SPEC-007/plan.md` (bloco no cabeçalho cobrindo as menções l.63, 64, 71, 308, 319, 359, 443, 711, 1731, 1801 e o título do Anexo T) e `governance/DHR-SPEC007-002_*` (tabela §3). Não alterados: `CONFLICT-MAP.md`, `WORKFLOW.md`, demais Specs baselined (a errata completa é do Plan da SPEC-048).

## 3. Condições do Plan da SPEC-048 `[FATO]` (ABERTURA §15)
Transcrever literal o ponto 3 da Interface (m-03); dispor explicitamente SPEC-004 RULE-CBP-002/004/005 e RULE-BB-001 por causa da P-9 (m-04; silêncio = herança não demonstrada = Crítica); método amostral de falso-ACEITE do juiz F2 (m-08); coordenar a errata com a metade F1 da emenda à SPEC-020 (m-10); declarar `Disposição:` de BL-017 e BL-010 (m-02); registrar a lacuna analista↔modelo (m-05); errata por critério de busca (m-01); não especificar a página de leitura além da regra de consumo.

## 4. Condições de conformidade (o que esta ata NÃO afirma)
- Homologa a **abertura** (número, nome, peso, fronteira, quantidade, perguntas, disposições propostas); **não** escreve nem aprova Plan, **não** abre a SPEC-049, **não** aplica errata nem emenda a Spec baselined (só nota aditiva autorizada em C-3).
- O Revisor não executou o gate (teto CONFORME condicional); o Orquestrador rodou o gate completo = PASSOU_D. 7+ citações do Benchmark não conferidas (clone ausente). Veracidade das fontes web é risco residual declarado no Dossiê. Validade do Dossiê até 2027-01-22.

## 5. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção · direito de uso do livro (Q7c) · forma de confirmar a identidade de Andraus (BUILD). **Nenhuma decisão aberta foi fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] ROADMAP · [x] CATALOGO · [x] RMR-001 (BL-017/BL-010, gatilho aditivo) · [x] notas aditivas (SPEC-007 plan, DHR-SPEC007-002) · [ ] merge (assinatura) · [ ] Dossiê e abertura da SPEC-049 (só por ordem de Andraus) · [ ] Plan da SPEC-048 (só por ordem de Andraus)

---

**Andraus** — *decisões em chat, 2026-10-24; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
