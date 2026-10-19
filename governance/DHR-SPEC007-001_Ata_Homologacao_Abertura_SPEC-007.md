# DHR-SPEC007-001 — Ata de Homologação — Abertura da SPEC-007 (RAG / WikiRAG / Knowledge Formation Harness)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Proposta `specs/features/SPEC-007/ABERTURA.md` + Dossiê `research.md` + `sources/`. Pareceres do Revisor: 1ª rodada **NÃO CONFORME** (3 Médias, de texto) → corrigido → 2ª rodada **CONFORME condicional** (9 Menores) → corrigido → 3ª rodada **CONFORME condicional** (7 Menores, "pode seguir a Andraus") — `governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-ABERTURA-2026-10-19.md`, `…-R2-…`, `…-R3-…`. Benchmark: `DHR-BENCH-INTEL-001` |
| Data | 2026-10-19 |
| Status | **ABERTURA HOMOLOGADA** (decisão direta de Andraus em chat, 2026-10-19, por AskUserQuestion: "Homologar a abertura agora"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **NÃO é baseline** — o Plan ainda não foi escrito e só inicia por ordem de Andraus. **Homologação CONDICIONADA** (§3). |
| Compatibilidade | Minor (não toca modelo canônico baselined nem fecha decisão aberta) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de abertura de Spec: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-19)
| # | Pergunta de abertura | Decisão |
|---|---|---|
| Q1 | Número, nome e peso | **Mantidos**: SPEC-007, "RAG / WikiRAG / Knowledge Formation Harness", **CRITICAL D0–D8** |
| Q2 | Uma Spec ou duas | **Uma Spec** (Opção B), com cláusula de divisão registrada como reserva; "memória de curto prazo" → SPEC-043, "detector de invenção geral" → SPEC-044, "aprender com o uso" → SPEC-018 |
| Q3 | O que é "WikiRAG" | **Versão de leitura** do que já foi carimbado, **montada por regra fixa** (Classe D), refeita a qualquer momento, **sem autoridade própria**; o pacote de evidência **cita só itens carimbados e fontes originais, nunca a página** |
| Q4 | Dono do carimbo | A SPEC-007 define o carimbo do conhecimento **formado a partir de fontes**; a promoção de hipóteses/evidências do próprio sistema fica com a **SPEC-018** (escolhe *quem* cuida, **não** *como*; decide parte do item "produtor/gatilho de promoção" da SPEC-006 `plan.md` l.976; K-001 segue aberta) |
| Q5 | Fidelidade (pendência da SPEC-020) | Duas partes — (1) o conhecimento formado não inventa o que a fonte não diz; (2) cada frase entregue tem apoio no trecho citado; checagens automáticas primeiro, juízo de modelo com conferência depois; **sem números de corte** até calibrar |
| Q6 | Material antigo em `rag/` | **Inalterado** (nada apagado nem alterado); tratado como material de leitura que precisa passar pela linha de montagem e receber carimbo; documentos que citam `rag/` e as 5 Specs GEN-1 ficam como estão |
| Q7(a)(b) | Licença do paralelo | Só **ideias de controle reescritas**, sem copiar texto/código; **citações curtas de auditoria (≈100–150 caracteres) aceitas**; **cópia literal só por decisão de Andraus** (licença/atribuição) |
| Q7(c) | O livro *Evidence-Based Technical Analysis* (obra de terceiro) | **ADIADA.** O livro **não entra como fonte** até Andraus decidir (autorização do titular dos direitos × uso privado; envio a provedor externo × só local). Outros livros e fontes serão acrescentados em momento oportuno |
| Q8 | Autoridade do carimbo | Aceito o **pacote como recomendação para detalhar no Plan**: 8.1 Andraus aprova a lista de quem pode carimbar; 8.2 fidelidade por regra fixa primeiro e, quando houver juízo, por **modelo diferente** do que formou (mesmo modelo em outro contexto **não** conta); 8.3 conferência em ponto separado de quem escreve; 8.4 aprovação pessoal por lote só para conhecimento de alto impacto; o carimbo carrega código (hash) do material + emissor autenticado + referência ao registro da conferência. **Não fecha** K-001 nem "quem mantém a lista de escritores em runtime" (SPEC-006 `plan.md` l.482) |
| BL-011 | Resíduo COL-EXP-05 | Re-apontado à SPEC-007 (`DHR-BENCH-INTEL-001` D8); BL-011 segue `ATIVADO`; `Absorvido` é só de Andraus |

## 2. Efeitos aplicados `[FATO]`
- `ROADMAP.md`: SPEC-007 passa a "abertura HOMOLOGADA; Plan pendente" (linha de "Próximo trabalho autorizado" e tabela do §25); texto anterior preservado.
- `governance/CATALOGO-OFICIAL.md`: registro desta ata.
- `governance/CONFLICT-MAP.md` (linha do COL-EXP-05): "ADIAR reconciliação (SPEC-006/009)" → re-apontado à SPEC-007 (`DHR-BENCH-INTEL-001` D8), texto anterior preservado.
- `backlog/RMR-001_Painel_Backlog.md`: BL-010, BL-017 e BL-035 seguem `Em espera` (vinculados à abertura por regra, **sem promoção**; a Disposição de cada um é declarada no Plan — `[STRUCT-13]`); BL-011 segue `ATIVADO`.

## 3. Condição de conformidade (o que esta homologação NÃO afirma)
Os pareceres são **CONFORME condicional**: o gate de código foi rodado pelo Orquestrador, não pelo Revisor; 7 Menores da 3ª rodada (R3-01..R3-07) seguem como **notas obrigatórias para o Plan** (alinhar a nota da Q-8 com "sim decide parte de `plan.md:482`"; separar "já normativo" de "em aberto" em `ABERTURA.md:33/:121` e `research.md:251`; precisão do exemplo de citações; "SPEC-018" em linguagem de trader; colchetes INV-07 com reticências; `[PROPOSTA]` na entrega do Plan sobre COL-EXP-05; requisito (i) anti-injeção como "não vira efeito"). Fontes externas do Dossiê: veracidade não atestada (sem web). A veracidade dos números dos repositórios vem de páginas públicas (a API do GitHub devolveu 403).

## 4. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · "produtor/gatilho de promoção" (SPEC-006 `plan.md` l.976; encaminhado à SPEC-018, não decidido) · direito de uso do livro (Q7c). **Nenhuma decisão aberta foi fechada por esta ata.**

## 5. Registro
- [x] Esta ata · [x] ROADMAP · [x] CATALOGO · [x] CONFLICT-MAP · [x] RMR-001 · [ ] merge (assinatura) · [ ] Plan da SPEC-007 (só por ordem de Andraus)

---

**Andraus** — *decisão em chat, 2026-10-19; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
