# Proposta de Abertura — SPEC-049: WikiRAG Reading View (slot ROADMAP §6, FASE 3)

> **Revisão 3 — correção do parecer R2** (`governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-ABERTURA-R2-2026-10-31.md`, CONFORME condicional: 2 Menores) **+ registro das respostas de Andraus** (chat 2026-10-31, a registrar na ata de homologação — **não** é homologação). Onde mudou: R2-m01 → S1 (iv), S6, S7, C-4, §15 cond. 13; R2-m02 → S5, R-3, §15 cond. 12 e 14; respostas → Status, §1, §3, CC-05, §13.
> *[antes: cabeçalho "Revisão 2 — correção do parecer R1", mantido abaixo como histórico]*
> **Revisão 2 — correção do parecer R1** (`governance/propostas/SPEC-049/PARECER-REVISOR-SPEC049-ABERTURA-R1-2026-10-31.md`, NÃO CONFORME: 1 Média + 8 Menores). Onde mudou: R1-M01 → S1, S6, S7, BASpec 1, CC-10, §7 (H-001), R-5/R-8, §13 C-4, §15 cond. 2; R1-m01 → §3, §13 P-7, §16; R1-m04 → S5, §15 cond. 12; R1-m05 → §1, S9, CC-08; R1-m06 → §4, R-9, §15 cond. 9-11; R1-m07 → §8; R1-m08 → contrato com a SPEC-007 (§2). R1-m02 aplicado pelo Orquestrador no `research.md` (não refeito). Texto superado preservado em linhas `[antes: …]` (INV-07).

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06/07) + DHR-BACKLOG-ABERTURA-001
**Autor:** Especificador Principal SOT (Claude Code, Opus 5.5)
**Data:** 2026-10-31
**Status:** **PROPOSTA DE ABERTURA** — aguarda parecer do Revisor (sobre o processo do Dossiê) e **homologação de Andraus** da definição da Spec. **NÃO** é baseline. O Plan (`plan.md`/`checks.md`) **não** foi escrito e só começa após a homologação desta abertura e por ordem expressa de Andraus. Tudo aqui é `[PROPOSTA]` salvo quando marcado `[FONTE]`. Nenhuma decisão aberta é fechada; nenhum baseline é tocado; nenhuma regra nova é criada (os requisitos descritos só valem se Andraus homologar e o Plan os redigir). **Revisão 3:** Andraus respondeu P-1..P-7 e C-1..C-4 no chat (2026-10-31) — respostas registradas em §13, a lançar na ata de homologação; a **homologação da abertura** segue como ato posterior dele.
**Depende de:** `research.md` (mesmo diretório — ler primeiro: §0 auditoria, §3 comparação, §4 repositórios, §8 escopo/re-apontamento) e `sources/`.
**Autorização:** ordem do Orquestrador por decisão de Andraus (chat, 2026-10-31): "ABRIR a SPEC-049 — WikiRAG Reading View … ETAPA DE ABERTURA". Base: DHR-SPEC048-001 Q-2 e C-2.

> **Em uma frase (para o trader):** a SPEC-007 **carimba** conhecimento e a SPEC-048 é o **balcão de consulta** dos analistas; a SPEC-049 é a **estante de leitura para você**: monta, sem escrever uma palavra, páginas com o que já foi carimbado, cada item com o endereço da fonte, os dois lados de cada contradição lado a lado e o aviso "a revalidar" onde houver — página que se refaz igual a qualquer momento, **não manda em nada** e **nunca** vira fonte para os analistas.

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-049** | **Já decidido** por Andraus (DHR-SPEC048-001 Q-2). `[FONTE]` |
| **Nome** | **"WikiRAG Reading View"** (Visão de Leitura WikiRAG) | **Já decidido** (Q-2). Sentido de "WikiRAG" = Q3 da DHR-SPEC007-001. `[FONTE]` |
| **Complexidade** | **HIGH — decidida por Andraus (P-1, chat 2026-10-31; a registrar na ata)**. Alternativa MEDIUM (proposta do slot, `ROADMAP.md` l.193) **rejeitada por Andraus**. *[antes: "HIGH — recomendada; a confirmar por Andraus (P-1). Alternativa: MEDIUM"]* | O perfil MEDIUM pára em D5 e não tem D7 (BASpec com VERIFICADO POR — atomic-spec l.52). Sem D7, a **trava E3** ("compilação WikiRAG" da INV-KFH-02 — herança `[INFERÊNCIA]`, ver S9) e a **reconstrução** (insumo T21) ficariam sem teste — mais fraco que o insumo, que vinha de Spec CRITICAL. A C-2 avisou: "Peso médio só se sustenta se essa trava continuar valendo do mesmo jeito" (`SPEC-048/ABERTURA.md` l.218). CRITICAL rejeitada: sem efeito sobre a verdade (E1), fora do ciclo, sem modelo (research §8.1). |
| **Profundidade-alvo** | **D0–D7** (standard, AGENTS §4) *[antes: "se HIGH; D0–D5 se MEDIUM"]* | D6 (protocolo do Blackboard) **não aplicável** — a página não vai ao Blackboard; declarado assim no Plan. Casos negativos transferidos (ADV-KFH-11 parte compilação; omissão de um lado) entram como **cenários negativos de D7**, sem suíte D8. |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Mesmo regime das SPEC-006/007/048. |
| **Classe predominante** (orientação, não vinculante — CC-11 por BASpec) | **D** (compilação, reconstrução, citação, lado a lado, exibição) · **C** (trava E3 do compilador) · **H: nenhuma** | Ver §4. Zero Classe H é característica, não lacuna: nenhum modelo é chamado. |

**Natureza:** Spec de **infraestrutura cognitiva de leitura** (Trilha B), agnóstica de escola, **fora do ciclo de trading**. CC-12 **não incide**; RULE-ECC-05 **não incide** (research §9) — condicionado à P-2 (respondida: só pessoas).

**Validade do Dossiê (ECC-VAL-001):** acesso 2026-10-31 → **2027-01-29** (HIGH, 90 dias). *[antes: "2027-01-29 se HIGH ou 2027-02-28 se MEDIUM (120 dias)"]*

---

## 2. Fronteira e escopo

### Dentro do escopo (proposta)
- **S1 Entrada declarada da compilação:** (i) **momento de corte** (tempo de registro do KG — `recorded_at`, SPEC-006 RULE-CKG-004); (ii) **itens carimbados** (SPEC-007 ponto 1) e **marcas** `revalidation_mark`/`contradiction_mark` (ponto 5) lidos **até o corte**, só por consulta read-only (RULE-CKG-011); (iii) **versão da regra de compilação**; (iv) **data de referência da validade** (nome proposto `valid_at`) — instante de **tempo de validade** (valid-time da SPEC-006) contra o qual cada item é julgado vigente ou encerrado. **Premissa `[INFERÊNCIA]` — o item tem janela de validade:** na regra normativa, `valid_from`/`valid_to` são campos de **relação** (RULE-CKG-004, `SPEC-006/plan.md` l.322, l.395-400, l.710); para o nó `learning` (SPEC-007 ponto 1, l.1224) a janela só aparece (1) no esquema lógico de `node_record` ("nós também têm validade — CKG-012", SPEC-006 l.1419-1420, referência), (2) no registro de **invalidação** que gera o estado derivado `INVALIDATED_IN_TIME` (l.718, l.1073) e (3) na extensão local `[PROPOSTA]` da SPEC-007 RULE-KFH-009 a nós e relações (l.683-685); qual dessas sustenta a validade do item fica para o Plan (§15 cond. 13), sem inventar campo; *[antes: "(valid-time, `valid_from`/`valid_to` da RULE-CKG-004)" — campo de relação atribuído ao item (R2-m01)]* é campo **próprio** da entrada, distinto do corte (CC-10). `[PROPOSTA]` Regra: o pedido declara `valid_at`; se não declarar, a regra de compilação o preenche **com o mesmo instante do corte**, **antes** de compilar, e grava esse valor como campo da entrada (no registro de compilação) — nunca lido do relógio. São dois campos com papéis diferentes que podem ter o mesmo valor (confirmação C-4). Candidato não selado **nunca** entra (research §3.1, §3.3).
  *[antes: entrada = (i) corte, (ii) itens/marcas até o corte, (iii) versão da regra — sem referência de tempo para a validade (R1-M01)]*
- **S2 Regra fixa:** agrupamento **só por campos de lista fechada** do item (ex.: ativo, tipo de nó, assunto do vocabulário do sistema); item sem o campo ⇒ grupo "sem classificação" declarado; **ordem total determinística**; modelo de página **sem lógica** (só encaixa campos); texto fixo da regra (rótulos, títulos) faz parte da versão da regra (research §3.7).
- **S3 Nenhum texto novo:** a página contém só (a) campos dos itens carimbados copiados como estão, (b) texto fixo da regra, (c) citações e identificadores. Qualquer outro texto ⇒ página **não emitida** (insumo `WIKI_MODEL_TEXT_FORBIDDEN`) (research §3.4).
- **S4 Citação conferível em cada bloco:** `published_item_ref@version` e a cadeia selo → validação → candidato → unidade → fonte@hash (SPEC-007 ponto 1, D9). Trecho da fonte original: **conforme P-3** (recomendação: não copiar).
- **S5 Contradição lado a lado:** todos os lados de cada `contradiction_mark` no **mesmo bloco**, cada um com citação; **sem** escolha de verdade, **sem** "preferido", **sem** destaque; **ordem neutra e fixa** (ex.: por identificador — nunca por escola, data, número de fontes ou hierarquia analítica); omitir um lado ⇒ não emite, com a granularidade (a)/(b) abaixo (parte transferida da RULE-KFH-016) (research §3.5). **Granularidade** `[PROPOSTA]`: (a) se o compilador deixar de pôr no bloco um lado que **está na entrada** (item carimbado até o corte), **a página inteira não é emitida** — nada de página parcial sem o bloco, que seria omissão silenciosa — e o registro de compilação grava a recusa com o código `CONTRADICTION_SILENT_RESOLUTION_FORBIDDEN` (código vigente da SPEC-007, `plan.md` l.1678, usado por referência, não redefinido — ou código próprio `WRV`, conforme o Plan declarar, §15 cond. 14); (b) se um lado **não está na entrada** (não carimbado até o corte), o bloco é emitido com esse lado declarado "lado não exibível" + motivo + identificador da `contradiction_mark`, e a ocorrência vai ao relatório de saúde como "contradição incompleta" (S7). Cenário negativo de (a) e de (b) no Plan.
- **S6 Tempo e marcas visíveis:** a página diz o **corte** e a **data de referência da validade** (`valid_at`, S1 (iv)); cada bloco mostra a **validade** do item (janela derivada da SPEC-006/007 — premissa `[INFERÊNCIA]` em S1 (iv); §15 cond. 13) *[antes: "(`valid_from`/`valid_to`)" atribuídos ao item (R2-m01)]*, o seu estado **em relação a `valid_at`** — vigente / encerrada / ainda não vigente / validade não informada (sem o campo ⇒ sinal, nunca "atual"; CC-09) — e "a revalidar" quando houver; item com validade encerrada em `valid_at` **nunca** aparece como atual sem sinal (RAG-SPEC-020); a convenção de fronteira (`valid_to = null` ≡ vigente, RULE-CKG-004; inclusão do limite) é fixada no Plan alinhada à SPEC-006; item superado é sinalizado e permanece no histórico — nada apagado (INV-07) (research §3.3).
  *[antes: "item com validade encerrada nunca aparece como atual sem sinal" — sem dizer contra que data (R1-M01)]*
- **S7 Reconstrução:** mesma entrada (S1, os **quatro** campos) ⇒ mesma página, byte a byte (hash); **nenhuma hora do relógio** na página nem no julgamento de validade — os únicos tempos são os da entrada (corte e `valid_at`) e a janela de validade dos itens (derivada, S1 (iv)) *[antes: "os campos de validade dos itens"]*; mesmo corte com `valid_at` diferente = **outra entrada** (página pode diferir, como esperado); **registro de compilação** só-inserção (entrada com os quatro campos — inclusive `valid_at` preenchido por derivação —, versão da regra, hash da entrada e da saída, relatório de saúde: contradição incompleta, validade vencida, página órfã; a página traz o hash da **entrada**, o da **saída** fica só no registro — um hash não pode estar dentro do que mede) (research §3.1, §3.2, §3.6, §3.8).
  *[antes: "o único tempo é o corte"]*
- **S8 Sem autoridade:** identificador próprio **`reading_view_ref`**, tipo **disjunto** de `published_item_ref@version` e `source_id@hash` — aceita o requisito inverso da SPEC-048 (`plan.md` l.1149-1151) com o nome que os testes de lá já usam; a página **nunca** é submetida ao KG nem é fonte (research §3.6).
- **S9 Trava E3 do compilador (herança `[INFERÊNCIA]`):** a herança **não** vem de texto vinculante: o corpo vinculante da INV-KFH-02 cobre só FORMAÇÃO e F1 (`SPEC-007/plan.md` l.432-443); a "compilação WikiRAG" aparece no parágrafo "INTERFACE COM A SPEC-048 [PROPOSTA]" (l.444-447: "estender esta invariante à trilha de consulta é requisito à SPEC-048"). Ancoragem: o slot "herda a trava "compilação WikiRAG" (INV-KFH-02, E3)" (`ROADMAP.md` l.193) e a C-2 da DHR-SPEC048-001 ("ela herda a trava "compilação WikiRAG" (E3 na SPEC-007)", research §0 b). *[antes: "S9 Trava E3 do compilador (herdada):" sem etiqueta (R1-m05)]* Conteúdo: a compilação **não tem capacidade de efeito permanente nem externo** (definições da SPEC-007 INV-KFH-02, não redefinidas); **zero chamada de modelo** (logo, não usa a CIM); únicos efeitos: **emitir a página** (E1) e **gravar o próprio registro** de compilação (research §0 e).
- **S10 Exibição como dado e restrição visível:** texto do item codificado na saída, nunca interpretado como marcação ativa, link executável ou instrução; a página mostra a **restrição de uso mais restritiva** dos itens que contém (P-11); leitura **local** (P-2/P-6) (research §3.7, §3.10).
- **S11 Fail-closed a montante:** sem itens carimbados (linha de montagem parada até a 1ª liberação — DHR-SPEC007-005 §3) ⇒ **página vazia com a falta declarada** — correto, não falha.

### Fora do escopo (Non-goals)
| Item | Motivo | Dono |
|---|---|---|
| Registro de fonte, direitos, formação, F1, validação, selo, marcas, atos de Andraus, CIM | BASELINE — usar, não redefinir (CC-02) | **SPEC-007** |
| Memória permanente, admissão, ontologia, consulta read-only, bitemporal | BASELINE | **SPEC-006** |
| Busca para analistas, pacote, contagem, F2, **regra de consumo** (pacote nunca cita a página) | BASELINE (DHR-SPEC048-002) | **SPEC-048** |
| Página no Blackboard / tipo de objeto | **M-001 ABERTA**; a página não vai ao quadro | SPEC-004 / Andraus |
| Gatilho de recompilação por notificação | por referência, se usado | **SPEC-005** |
| Leitura da página por agente analítico ou Manager | proposta P-2: não consomem | Specs dos agentes (requisito, `[INFERÊNCIA]`) |
| Resumo, síntese ou qualquer texto redigido por modelo na página | vedado (Q3; S3) — mudar isso = **nova abertura** (RULE-ECC-07) | — |
| Enviar a página a outra pessoa ou a modelo de fora | proposta P-6 | Andraus (decisão futura) |
| Motor de renderização, formato, interface gráfica, armazenamento da página | neutralidade tecnológica (RAG-P12) | BUILD |
| Rastreio por etapa; casos de regressão | — | **SPEC-040** / **SPEC-022** |
| Aprender com uso da página; ciclo P12 | **K-001 ABERTA** | **SPEC-018** |
| Convicção, pesos, limiares | **J-001/N-001 ABERTAS**; INV-04 | SPEC-003/CCM-001 |
| Escola de `structure` (campo usado para agrupar) | **CKG-STRUCT-ORIGIN-001 ABERTA** (BL-035) | SPEC-006 / Andraus — aqui ausente ⇒ "INDETERMINADA" |
| Caminho de leitura em runtime dos agentes | **SPEC-045-RUNTIME-001 ABERTA** | SPEC-045 |

### Contrato com as Specs montante (BASELINE)
- **SPEC-007:** a página **cumpre**, por analogia `[INFERÊNCIA]`, os pontos 1, 2 e 5 da Interface (`plan.md` l.1224, l.1225, l.1228), com o texto literal da coluna "Requisito proposto à SPEC-048": ponto 1 — "servir como conhecimento **só** itens carimbados; candidato não selado nunca é conhecimento servível"; ponto 2 — "não servir unidade de fonte com `rights_status` efetivo INDETERMINADO; usar a definição de origem-raiz daqui para contar independência" (a parte de independência não se aplica — a página não conta fontes); ponto 5 — "expor "a revalidar"; servir os dois lados de uma contradição, lado a lado". **Separado do ponto 2:** a **exibição da restrição de uso mais restritiva** (S10) **não** vem do ponto 2; vem da RULE-KFH-001 (restrição efetiva registrada) e da P-11 (derivado herda a restrição, DHR-SPEC007-003/004), declaradas no CC-08. Com P-3 opção (A) (não copiar trecho) o "não servir" literal fica satisfeito por construção; com (B), vale literalmente: trecho de unidade com `rights_status` efetivo INDETERMINADO **não** aparece. *[antes: "só itens carimbados; restrição de uso efetiva respeitada e exibida; …" — paráfrase do ponto 2 (R1-m08)]* Ponto 3 (CIM) **não se aplica** — zero chamada de modelo. Ponto 4: não lê nem grava atos além do que a restrição de uso efetiva já traz. **Não** emite selo, não muta candidato, não grava marca nem ato.
- **SPEC-006:** só consulta read-only; nada submetido ao KG.
- **SPEC-048:** nenhuma interface em tempo de execução; esta Spec **entrega** o identificador disjunto `reading_view_ref` que o gate D de lá recusa.

---

## 3. Quantidade e dimensionamento (RULE-ECC-07)

**Spec única** — um contrato só (itens carimbados no corte → página + registro de compilação); tudo muda junto. Sem divisão.

**BASpecs candidatas (só títulos; numeração no Plan, prefixo `WRV` proposto):**
1. Entrada da compilação: corte, itens carimbados e marcas lidos só-leitura até o corte, versão da regra, data de referência da validade (`valid_at`; derivação declarada se ausente)
2. Regra fixa: agrupamento por campos de lista fechada, ordem total determinística, modelo de página sem lógica
3. Nenhum texto novo na compilação
4. Citação conferível em cada bloco (e trecho de fonte conforme P-3)
5. Contradição lado a lado, ordem neutra, sem escolha nem destaque
6. Tempo e marcas visíveis; item superado sinalizado, nunca apagado
7. Reconstrução: mesma entrada ⇒ mesma página; sem hora do relógio; registro de compilação só-inserção
8. Identificador `reading_view_ref` disjunto; página não citável e nunca submetida ao KG
9. Compilador sem capacidade de efeito (trava E3 herdada; zero modelo)
10. Exibição como dado; restrição de uso visível; leitura local; página vazia com falta declarada

**Capacidades do ROADMAP cobertas** (`ROADMAP.md` l.193 + Q3): visão de leitura por regra fixa (BASpecs 1-2); a partir de itens carimbados da SPEC-007 (1); sem autoridade própria (8); refeita a qualquer momento (7); trava "compilação WikiRAG" E3 (9); contradições lado a lado (5 — C-1); a página nunca é citada (8, lado da página; o lado do pacote é da SPEC-048).

**Linhas previstas do corpo normativo do Plan** `[INFERÊNCIA]` — derivação mostrada (R1-m01).

**Base:** ledger §2-bis (`governance/aprendizado/LEDGER-ACHADOS.md` l.63) — SPEC-048: 1.935 linhas de corpo, 12 BASpecs (contadas por cabeçalho `### BASpec-RET-0nn`, `SPEC-048/plan.md` l.808-1078), CRITICAL D0–D8, 4 rodadas de correção. É a Spec irmã mais parecida (mesmo padrão de mapeamento do Anexo T). Decomposição da base por cabeçalhos de seção do próprio `plan.md` da SPEC-048 (contagem de linhas entre cabeçalhos):

| Parte da SPEC-048 (linhas) | Linhas | Comportamento na estimativa |
|---|---|---|
| D2 Regras (l.416-745) + corpos das BASpecs (l.808-1098) + D7 cenários (l.1215-1403) | 330 + 291 + 189 = **810** | **variável por BASpec**: 810 / 12 ≈ **67,5** (HIGH); sem D7: (330 + 291) / 12 ≈ **52** (MEDIUM) |
| Enforcement Contracts (l.1490-1652, 8 ECs) | 163 | **por EC**: ≈ **20** |
| D8 adversarial (l.1404-1478) | 75 | **0** (nem HIGH nem MEDIUM têm D8) |
| Restante (cabeçalho, histórico de rodadas, mapeamento, decisões, CC, Herança/Delta, CC-10, D0/D1, EARS, D3.1, D4–D6, interfaces, métricas/D9, escala E0–E3, erratas propostas, Plan/§7-bis/etiquetagem/perguntas/autopré-check) | 887 | **fixo**, com 2 ajustes `[INFERÊNCIA]`: erratas/propostas (l.1664-1721, 58) → ≈10 (aqui não há errata — §8): **−48**; em MEDIUM, §7-bis (l.1779-1817, 39) não é obrigatório: **−39** |

| Estimativa SPEC-049 (10 BASpecs, 3 ECs) | HIGH D0–D7 | MEDIUM D0–D5 |
|---|---|---|
| Fixo ajustado | 887 − 48 = 839 | 887 − 48 − 39 = 800 |
| Variável | 10 × 67,5 = 675 | 10 × 52 = 520 |
| ECs (emissão E1; trava E3; registro E1) | 3 × 20 = 60 | 3 × 20 = 60 |
| **Total central** | **≈1.570** | **≈1.380** |
| **Faixa** (−10% / sem o ajuste de erratas) | **1.420–1.620** | **1.240–1.430** |
| **Extrapolação proporcional** (1.935 / 12 ≈ 161 por BASpec × 10) | **≈1.610** | — (a base é CRITICAL; superestima MEDIUM) |

**Leitura contra a RULE-ECC-07** (`governance/RULES.md` l.518-530): em **HIGH**, o total central (≈1.570) fica a 98% do limiar de **1.600** (80% do teto), e o topo da faixa (≈1.620) e a extrapolação proporcional (≈1.610) **passam** de 1.600 — por precaução (fail-closed), trato HIGH como **exigindo a confirmação de Andraus** da decomposição antes do Plan (**P-7**). **Andraus escolheu HIGH (P-1) e confirmou um documento só, ciente do encosto no limiar de 1.600 (P-7, chat 2026-10-31; a registrar na ata).** Em **MEDIUM** (rejeitada), toda a faixa fica abaixo de 1.600. Ambas bem abaixo do alerta 1.900 / teto 2.000. **Proposta de decomposição:** Spec **única** — dividir partiria um contrato só (entrada → página + registro), em que tudo muda junto; não há fronteira de contrato interna (RULE-ECC-07: "o que muda junto fica junto"). **Incertezas:** base n=1 decomposta (a SPEC-007, 1.949 linhas de corpo, l.62 do ledger, não foi decomposta); o histórico de rodadas cresce com o número de rodadas (na base, l.29-93 ≈ 65 linhas para 4 rodadas). **Gatilho processual:** mudar escopo ou dividir depois de o Plan começar = nova abertura.
*[antes: fixo ~400/~380 + 10 × 70 / 10 × 40 + ~150/~100 = ≈1.250 (1.000–1.500) / ≈880 (700–1.050), "ambas abaixo de 1.600" — fixo sem derivação (R1-m01)]*

---

## 4. Classe RULE-MECH-01 (CC-11) — orientação por tipo de BASpec

- **Classe D:** entrada (corte e data de referência da validade, com a derivação declarada); agrupamento e ordem; checagem "nenhum texto fora de campos/texto fixo/citações"; citação resolvível; lado a lado e ordem neutra; tempo e marcas; hash e reconstrução; identificador disjunto; codificação na saída; página vazia; registro de compilação.
- **Classe C (E3, fail-closed):** trava do compilador sem capacidade de efeito (insumo: cláusula "compilação WikiRAG" da INV-KFH-02) — falha ⇒ **não compila** e registra. **Justificativa CC-11** `[INFERÊNCIA]` (atomic-spec l.305 trata Classe C em BASpec de risco baixo como violação): o nível E3 **não** mede a página (E1, sem efeito sobre a verdade), e sim a **capacidade que a trava nega** — o compilador lê texto de item que veio, na origem, de fonte externa (pode trazer instrução embutida — research §3.7); se ganhasse capacidade de efeito, o efeito seria **permanente** (escrita ao KG, selo, ato, configuração — as mesmas definições da INV-KFH-02, `SPEC-007/plan.md` l.433-436, cujos caminhos são E3). Risco da ameaça = alto e irreversível ⇒ C/E3 compatível; e é o piso que o slot declara (`ROADMAP.md` l.193). Economicidade: a trava não chama modelo nem acrescenta etapa cara. O Plan redige esta justificativa por BASpec (§15 cond. 10).
- **Classe H: nenhuma.** Se um dia se quiser texto de modelo na página (ex.: resumo), é **nova abertura**.
- **Pisos de nível (D2):** emissão da página **E1** (insumo EC-KFH-009 — visão reconstruível, sem efeito sobre a verdade); registro de compilação **E1**; trava do compilador **E3**. Economicidade nunca rebaixa nível.

**Critério 4Es:** Eficácia primeiro — uma página que escolhesse lado, inventasse texto ou pudesse escrever no KG criaria uma 2ª verdade; por isso tudo é D e a trava é C. Eficiência: compilar sob demanda a partir do registro, sem guardar a página como verdade. Economicidade: zero chamada de modelo.

---

## 5. Princípios de Domínio (RULE-PD-01 / CC-12) — **NÃO incide**
Não é Spec de especialidade de escola. Nenhum `PD-xx`.

---

## 6. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação | Nota |
|---|---|---|
| CC-01 | OK | Agnóstica de escola; não cria hipótese; a hierarquia analítica **não** é usada para ordenar lados de contradição (ordem neutra). |
| CC-02 | **Aplica — foco** | Não redefine CEM/CHM/CCM nem SPEC-006/007/048; consome por referência. |
| CC-03 | OK | Nada da página entra no Conviction Vector (INV-04); J-001/N-001 abertas. |
| CC-04 | OK | Nenhuma Salvaguarda tocada; a página não é sinal. |
| CC-05 | Aplica | HIGH decidido por Andraus (P-1; MEDIUM rejeitada). *[antes: "HIGH proposto (alternativa MEDIUM)"]* |
| CC-06/07 | Diferido ao Plan | Engineering Cards no BUILD. |
| CC-08 | **Aplica — foco** | INHERITS (ID+versão no Plan): SPEC-007 v2.3 (INV-KFH-02 — cláusula "compilação WikiRAG" via nota C-3, herança `[INFERÊNCIA]`: o texto-fonte l.444-447 é parágrafo marcado `[PROPOSTA]` ("requisito à SPEC-048"); âncora `ROADMAP.md` l.193 e C-2 da DHR-SPEC048-001 — ver S9; Interface pontos 1, 2, 5; RULE-KFH-001 restrição efetiva e P-11; RULE-KFH-016 registro da contradição; RULE-KFH-007 selo), SPEC-006 v1.7+erratas (RULE-CKG-004, -010, -011), SPEC-048 v1.4 (requisito inverso; `WIKI_PAGE_CITED_AS_SOURCE`), DHR-SPEC007-001 Q3, RULE-MET-01, INV-07, INV-09. **REMOVED vazio** (proposta). Eixo vertical RULE-HV não se aplica (relação horizontal — research §0 i). |
| CC-09 | **Aplica** | Nenhum número (sem limiar); escola ausente ⇒ INDETERMINADA; "página vazia" é estado válido. |
| CC-10 | **Aplica** | Acepções: **página de leitura** ≠ KG ≠ pacote ≠ Evidência (CEM) ≠ Observação; **"emitir"** a página ≠ **"publicar"** (KG/Blackboard — vocabulário n-06 da SPEC-007); **"texto de modelo"** = texto novo na compilação, ≠ texto já carimbado (C-1); **"corte"** = tempo de registro (`recorded_at`), ≠ validade do item; **"data de referência da validade"** (`valid_at`) = instante de tempo de validade contra o qual se julga vigente/encerrado — campo próprio da entrada, ≠ corte, mesmo quando derivado com o mesmo valor (S1 (iv)). |
| CC-11 | Aplica (§4) | Por BASpec; Classe C/E3 da trava justificada pela ameaça e pelo slot (§4), a redigir no Plan. |
| CC-12 | **NÃO incide** (§5) | — |

---

## 7. Decisões de Andraus que entram nesta Spec — disposição proposta

| Decisão | Fonte | Disposição na SPEC-049 |
|---|---|---|
| **Q3** — versão de leitura do carimbado, regra fixa, refeita a qualquer momento, sem autoridade, nunca citada | DHR-SPEC007-001 | **Incorporar como regra** (S1–S8). Nada a reabrir. |
| **Q-2** — página em Spec própria (número e nome) | DHR-SPEC048-001 | Já aplicado. |
| **C-1** — corte do insumo do Anexo T | DHR-SPEC048-001 | **Incorporar** as partes listadas (research §0 f), reescritas com IDs próprios; nenhum ID `*-KFH-*` reutilizado. |
| **C-2** — peso só como proposta; atenção à trava E3 | DHR-SPEC048-001 | Respondida aqui: trava mantida em E3 (S9) e P-1 (HIGH recomendado). |
| **P-11 / P-12 / P-4b** — derivado herda restrição; "de casa" só com ato; modelo de terceiro = "fora" | DHR-SPEC007-003/004 | **Usar** só para exibir a restrição; a página não envia nada a modelo (P-6). |
| **H-001 FECHADA** — KG só-inserção bitemporal | DHR-H001-001 | **Usar** para o corte (tempo de registro), a data de referência da validade (tempo de validade) e a reconstrução (S1, S6, S7). |

---

## 8. Re-apontamento — errata e gatilhos (só proposta; nada executado)

**Errata de re-apontamento: nenhuma.** O slot mantém número, nome e fronteira; as Specs baselined que citam a página (SPEC-007 l.3 + nota N-F do ERRATUM-REAPONT-001; SPEC-048 — lista completa por Grep do literal `SPEC-049` e de `reading_view_ref` em research §8.3) **já** apontam à SPEC-049. *[antes: lista "SPEC-048 l.5, 19, 123-131, … 1267, 1439, 1463, 1658, 1756, 1762" — incompleta e com linhas deslocadas (R1-m07)]* Condição: se o identificador da página deixar de ser `reading_view_ref`, ou se número/fronteira mudarem, a errata volta a ser necessária.

**Nota aditiva opcional à SPEC-007** (proposta para o Plan, passo à parte, só se Andraus quiser — conflito de redação research §7 item 2/3): "a cláusula 'compilação WikiRAG' da INV-KFH-02 e os pontos 1, 2 e 5 da Interface valem também para a SPEC-049". Sem ela, a herança fica declarada só no CC-08 desta Spec.

**Gatilhos do RMR-001:** nenhum re-apontamento proposto (slot não dividido, fundido nem renumerado). Esperado do `backlog_triggers --abertura SPEC-049`: **nenhum item** (research §8.4, `[INFERÊNCIA]` a confirmar pelo script).

---

## 9. Itens do backlog — disposições PROPOSTAS (declaradas no Plan; o Especificador não promove)

- **BL-010** (MC-RAG-001, `Em espera`, não vinculado por regra) — `Disposição: REFERÊNCIA` *(proposta, voluntária)* — motivo: a página aplica RAG-P08 (contradição explícita), RAG-P10 (temporalidade explícita), RAG-P12 (neutralidade tecnológica) e o critério de aceitação de RAG-SPEC-020; nenhum RAG-SPEC inteiro é absorvido (confirma a `[INFERÊNCIA]` do Dossiê da SPEC-048 §8.3).
- **BL-035** (CKG-STRUCT-ORIGIN-001, não vinculado) — `Disposição: REFERÊNCIA` *(proposta, voluntária)* — motivo: a página agrupa por campo de escola quando existir e **não** infere; ausente ⇒ "INDETERMINADA"; a decisão segue aberta.
- **BL-017** (dimensões B da SPEC-020) — `Disposição: FORA` *(proposta)* — motivo: a página não tem F2 nem resposta a avaliar.
- **BL-029** (`ATIVADO`, não vinculado) — `Disposição: FORA` *(proposta)* — motivo: não há modelo propondo nada; tudo é D.
- **BL-003** e **BL-011** (`ATIVADO` segundo o HANDOFF §9, não vinculados) — não tocados (a página não persiste hipótese/estado nem trata experiência); encerrar é de Andraus.
- **Resultado esperado do `backlog_triggers --abertura SPEC-049`:** nenhum item. Se o script listar algo diferente, prevalece o script e eu reviso as disposições.

---

## 10. Dependências e decisões abertas (CONS-01 — não fechar)

**Montante homologado (construir sobre):** SPEC-007 v2.3 (DHR-SPEC007-005), SPEC-006 v1.7 + erratas v1.11/v1.12/v1.13, SPEC-048 v1.4 (DHR-SPEC048-002), SPEC-002 (proveniência, por referência). Nenhum bloqueador a montante aberto **para a abertura**. **Fail-closed herdado:** sem liberações de Andraus na SPEC-007, toda página sai vazia com a falta declarada.

**Abertas que esta Spec toca e não fecha:** **CKG-STRUCT-ORIGIN-001** (escola para agrupar), **SPEC-045-RUNTIME-001** (só para afirmar que a página não é caminho de leitura dos agentes — P-2), **M-001** (a página não vai ao Blackboard), **C-001** (granularidade de EARS multi-condição — afeta só a redação), **K-001** (nenhum aprendizado aqui). **Não tocadas:** J-001, G-001, N-001, ECC-03-001, WORKFLOW-SOT-001 (WF-D03), produtor/gatilho de promoção, forma de confirmar a identidade de Andraus (BUILD).

---

## 11. Riscos (com contenção)

- **R-1 Página vira 2ª verdade** — sem autoridade; `reading_view_ref` disjunto; nunca submetida ao KG; recusada pelo pacote (SPEC-048).
- **R-2 Texto inventado na compilação** — S3 (D): só campos, texto fixo e citações; senão não emite.
- **R-3 Página escolhe lado de uma contradição** — S5: todos os lados, ordem neutra, sem destaque; omitir lado que está na entrada ⇒ página inteira não sai; lado ausente da entrada ⇒ "lado não exibível" (S5 (a)/(b)). *[antes: "omitir ⇒ não emite"]*
- **R-4 Ordem ou agrupamento insinuando preferência** — regra fixa por campos de lista fechada; ordem por identificador; hierarquia analítica não usada.
- **R-5 Página não reconstruível** (hora do relógio, ordem instável, data de validade implícita) — S7: só os tempos da entrada (corte e `valid_at`); ordem total; hash. *[antes: "corte como único tempo"]*
- **R-6 Compilador ganha capacidade de efeito** — S9 (C, E3, fail-closed): zero modelo, zero escrita fora do próprio registro.
- **R-7 Texto do item executado como marcação ou instrução** — S10: codificação na saída.
- **R-8 Conhecimento vencido mostrado como atual** — S6: validade julgada contra `valid_at` (S1 (iv)) e "a revalidar" visíveis.
- **R-9 Agente lê a página por porta lateral** — P-2: só leitura humana; requisito às Specs dos agentes (`[INFERÊNCIA]`). **Limitação declarada:** a SPEC-049 **não tem** gate nem detector próprio que impeça um agente de ler a página — ela não controla os consumidores. Contenção existente: `reading_view_ref` disjunto + recusa no gate D do pacote (SPEC-048 `WIKI_PAGE_CITED_AS_SOURCE`), que impede a página de virar **citação**, mas **não** impede leitura. Risco residual registrado; contenção completa depende das Specs dos agentes e da SPEC-045-RUNTIME-001 (ABERTA). Ver §15 cond. 11.
- **R-10 Trecho não liberado ou restrito exposto** — P-3 (não copiar trecho) e restrição mais restritiva visível; P-6 (não sai da casa).
- **R-11 Invadir SPEC-007/006/048** — Non-goals e contrato.
- **R-12 Peso subestimado** — P-1 (HIGH recomendado).

---

## 12. Edições a documentos de governança — NÃO executadas

O Especificador **não** edita ROADMAP, CATALOGO, RMR-001, CONFLICT-MAP, WORKFLOW, atas, AGENTS.md, agentes, canon nem Specs baselined. Após a homologação, cabe ao Orquestrador/Andraus: registrar a abertura na ata e no ROADMAP (seção SPEC-049 l.192-193 e tabela l.523 — "ABERTURA HOMOLOGADA; Plan pendente"; peso decidido na P-1); registrar as respostas P-1..P-7 e as confirmações C-1..C-4 na ata; CATALOGO-OFICIAL (registro da ata). **Nada a editar** no RMR-001 (nenhum gatilho re-apontado) nem no CONFLICT-MAP. A nota aditiva opcional à SPEC-007 (§8) só se Andraus pedir, em passo à parte.

**Comandos a rodar (não tenho Bash — para o Orquestrador):**
- `python scripts/backlog_triggers.py --abertura SPEC-049` (esperado: nenhum item — §8/§9)
- `python scripts/check_repo_research.py specs/features/SPEC-049` e `--all` (RULE-ECC-06 — esperado OK: 5 elegíveis, 1 não elegível com veredito coerente)
- `python scripts/build_map.py` e `python scripts/build_map.py --check` (BL-019)
- `python scripts/check_refs.py` · `python scripts/check_doc_sync.py` · `python scripts/check_invariants.py specs/features/SPEC-049/ABERTURA.md` (informativos)

---

## 13. Perguntas a Andraus (linguagem simples)

> **Revisão 3:** todas RESPONDIDAS por Andraus no chat (2026-10-31). As respostas abaixo são registro para a ata de homologação — **não** são a homologação da abertura, que é ato posterior dele. Texto original das perguntas mantido.

1. **P-1 (peso).** *Recomendação: tratar a estante de leitura como peça de peso **alto** (HIGH), com teste para cada regra.* Ela não mexe em dinheiro nem roda no ciclo, mas carrega uma trava de nível máximo herdada da linha de montagem ("quem monta a página não pode causar efeito nenhum"). No peso **médio** (o que estava proposto), as regras não ganham teste escrito — essa trava ficaria sem prova. **Prefere alto (recomendado), médio, ou médio com teste só nessa trava e na "página refeita igual"?**
   > *Nota técnica:* HIGH D0–D7 (D6 N/A) × MEDIUM D0–D5 × MEDIUM + D7 seletivo homologado; ≈1.570 × ≈1.380 linhas (derivação §3) *[antes: ≈1.250 × ≈880]*; §1, §3; research §8.1. Se escolher HIGH, ver também P-7.
   > **RESPONDIDA por Andraus (chat 2026-10-31):** peso **ALTO** — HIGH D0–D7. MEDIUM (e MEDIUM + D7 seletivo) rejeitadas.
2. **P-2 (quem lê).** *Recomendação: a página é **só para pessoas** (você, auditoria). Os analistas-robô e o Manager continuam usando só o balcão de consulta (SPEC-048), que tem as travas de envio e de conferência de frases.* **Confirma?**
   > *Nota técnica:* research §3.9; se não, reavaliar RULE-ECC-05 e SPEC-045-RUNTIME-001 antes do Plan.
   > **RESPONDIDA por Andraus (chat 2026-10-31):** recomendação aceita — página **só para pessoas**. (SPEC-045-RUNTIME-001 segue ABERTA; esta resposta só tira a página desse caminho.)
3. **P-3 (trecho da fonte original).** *Recomendação: a página mostra o conhecimento carimbado e o **endereço** da fonte, **sem copiar** trecho do texto original.* Assim nada que não passou pelo carimbo aparece na estante, e a questão de direito de uso do texto original não entra aqui. Alternativa: copiar o trecho só quando a fonte estiver liberada. **Qual prefere?**
   > *Nota técnica:* opções (A)/(B) em research §3.10.
   > **RESPONDIDA por Andraus (chat 2026-10-31):** recomendação aceita — opção **(A)**, sem trecho copiado da fonte original.
4. **P-4 (organização das páginas).** *Recomendação: organizar por campos fixos que o sistema já conhece (ativo, tipo, assunto da lista do sistema); o que não tiver o campo vai para "sem classificação", nunca para um grupo adivinhado.* **Confirma?**
   > *Nota técnica:* research §3.7; escola ausente ⇒ "INDETERMINADA" (CKG-STRUCT-ORIGIN-001 segue aberta).
   > **RESPONDIDA por Andraus (chat 2026-10-31):** recomendação aceita — campos fixos, com grupo "sem classificação".
5. **P-5 (guardar ou refazer).** *Recomendação: a página é **refeita na hora**, a pedido, para a data que você escolher (a data do "que o sistema sabia" e, se quiser, outra data para julgar o que estava valendo — C-4); o sistema guarda só o registro de cada montagem (o que entrou, qual regra, a "impressão digital" do resultado), que prova que ela sai igual.* Alternativa: guardar também uma cópia de cada página. **Qual prefere?**
   > *Nota técnica:* research §3.2; armazenamento = BUILD; o comportamento (reconstrução por hash) vale nas duas.
   > **RESPONDIDA por Andraus (chat 2026-10-31):** recomendação aceita — página **refeita na hora**, com registro de cada montagem.
6. **P-6 (mostrar para fora).** *Recomendação: por enquanto a página **não sai da casa** — não é enviada a outra pessoa nem a modelo de empresa terceira; se quiser isso no futuro, decidimos à parte.* **Confirma?**
   > *Nota técnica:* a trava de envio da SPEC-007 rege chamada de modelo, não distribuição a pessoas; research §3.10 e §7 item 6.
   > **RESPONDIDA por Andraus (chat 2026-10-31):** recomendação aceita — a página **não sai da casa**; envio para fora, se um dia quiser, é decisão à parte.
7. **P-7 (tamanho do documento — só se escolher peso alto na P-1).** *Recomendação: manter a estante como **um documento só**.* Pela conta feita com a SPEC-048 como base, o plano no peso alto deve ter cerca de **1.570 linhas** (entre 1.420 e 1.620); a conta mais simples (proporcional) dá **cerca de 1.610**. A regra de tamanho pede que **você confirme** a divisão sempre que a estimativa passar de **1.600** linhas — estamos encostados nesse limite, por isso pergunto. Dividir partiria uma coisa que muda junta (o que entra → a página + o registro da montagem). **Confirma um documento só, ou prefere que eu proponha uma divisão?**
   > *Nota técnica:* RULE-ECC-07 (`governance/RULES.md` l.526-527: "Estimativa acima de 80% do teto (1.600) exige confirmação da decomposição por Andraus antes do Plan"); derivação em §3; no peso médio (≈1.380) a confirmação não é exigida.
   > **RESPONDIDA por Andraus (chat 2026-10-31):** **um documento só**; Andraus confirma o encosto no limiar de 1.600 da RULE-ECC-07. O Plan mede o corpo e declara a medida (§15 cond. 8); o teto de 2.000 segue valendo.

**Confirmações (na homologação):**
- **C-1 — o que é "texto de modelo".** O conhecimento carimbado foi escrito por um modelo na linha de montagem e depois conferido e carimbado. *Recomendação: a regra "texto de modelo não entra na página" vale para **texto novo** escrito na hora de montar a página; o texto **já carimbado** é exatamente o que a página mostra.* **Confirma?** (research §3.4) → **CONFIRMADA por Andraus (chat 2026-10-31):** texto de modelo = só texto novo.
- **C-2 — nome do identificador.** *Recomendação: usar `reading_view_ref`, o nome que os testes da SPEC-048 já usam — evita corrigir a SPEC-048.* **Confirma?** (research §3.6) → **CONFIRMADA por Andraus (chat 2026-10-31):** `reading_view_ref`.
- **C-3 — onde mora a trava.** *Recomendação: a trava "compilação WikiRAG" fica declarada nesta Spec (herança, CC-08), sem editar a SPEC-007; nota aditiva na SPEC-007 só se você quiser.* **Confirma?** (§8) → **CONFIRMADA por Andraus (chat 2026-10-31):** trava declarada nesta Spec via CC-08, sem editar a SPEC-007.
- **C-4 — duas datas na página.** Cada conhecimento carimbado tem um período em que vale (de quando até quando) — *nota técnica:* isto é `[INFERÊNCIA]`; de onde vem esse período no item fica para o Plan (S1 (iv), §15 cond. 13). *[antes: afirmado sem etiqueta (R2-m01)]* Para a página avisar "isto já não vale", ela precisa de uma data para comparar — e essa data não pode vir do relógio, senão a página não sairia igual ao ser refeita. *Recomendação: a página leva **duas datas escritas**: (1) "o que o sistema sabia até" (o corte) e (2) "o que estava valendo em" (data de referência da validade). Se você não informar a segunda, ela recebe **a mesma data da primeira**, e isso fica anotado no registro da montagem.* **Confirma?** (S1 (iv), S6, S7; research §3.1, §3.3) → **CONFIRMADA por Andraus (chat 2026-10-31):** duas datas na página — corte e `valid_at`.

> Nenhuma decisão aberta é fechada (CONS-01): J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção e a forma de confirmar a identidade de Andraus seguem abertas.

---

## 14. Próximo passo
`research.md` + `sources/` + esta Proposta seguem para **parecer do Revisor** sobre o processo do Dossiê (RULE-ECC-02/04/06/07; não incidência de ECC-05 e CC-12; disposições propostas; conflitos registrados; ausência de citação nova do Benchmark) e, depois, **homologação de Andraus** (P-1..P-7, C-1..C-4, fronteira e Classe orientativa) *[antes: "P-1..P-6, C-1..C-3"]* — **antes** de qualquer `plan.md`/`checks.md`, que só começam por ordem expressa dele.

---

## 15. Condições propostas ao Plan (só valem se a abertura for homologada)

| # | Condição | Origem |
|---|---|---|
| 1 | Reescrever o insumo do corte C-1 com IDs próprios (`WRV`), tabela de origem item a item; nenhum ID `*-KFH-*` reutilizado. | research §0 f; padrão SPEC-048 |
| 2 | Declarar a **entrada** da compilação com **quatro** campos (corte + itens/marcas até o corte + versão da regra + data de referência da validade `valid_at`, com a regra de derivação "ausente ⇒ mesmo instante do corte, gravado na entrada"), a proibição de hora do relógio na página **e no julgamento de validade**, e cenário D7 "mesmo corte, `valid_at` diferente ⇒ entradas diferentes". *[antes: "corte + itens/marcas até o corte + versão da regra"]* | research §3.1, §3.3; S1, S6, S7 |
| 3 | Dispor, no CC-08 (§7-bis Bloco B se HIGH), a cláusula "compilação WikiRAG" da INV-KFH-02 e os pontos 1, 2, 5 da Interface da SPEC-007, um a um, com evidência. | research §7 itens 2-3 |
| 4 | Fixar a acepção de "texto de modelo" (C-1) e o vocabulário "emitir" ≠ "publicar" (CC-10). | research §3.4 |
| 5 | Ordem neutra e fixa dos lados de contradição, declarada como regra D, com cenário negativo de omissão. | research §3.5 |
| 6 | Identificador `reading_view_ref` disjunto, conferido contra `SPEC-048/plan.md` l.1103/l.1267/l.1439. | research §3.6 |
| 7 | Não especificar consumo da página por agentes, resumo por modelo nem envio para fora (Non-goals), salvo decisão diferente de Andraus em P-2/P-6. | P-2, P-6 |
| 8 | Medir o corpo do Plan contra a estimativa (§3) e declarar a medida (RULE-ECC-07); se HIGH, só começar após a resposta à P-7. | RULE-ECC-07; P-7 |
| 9 | **ENF-07:** a unidade E3 (trava do compilador) declara o método de **falso-DENY** — compilação legítima recusada pela trava —, amostral, com limiar = gap aberto (sem número inventado). | atomic-spec l.273 (ENF-07); parecer R1-m06 (a) |
| 10 | **CC-11:** justificar, na BASpec da trava, Classe C/E3 pela ameaça (capacidade de efeito permanente negada) e pelo piso do slot, não pelo nível da página (E1). | §4; atomic-spec l.292/l.305 |
| 11 | **Limitação R-9:** declarar que a SPEC-049 não tem gate/detector contra leitura por agente; contenção = `reading_view_ref` + gate D da SPEC-048 + requisito `[INFERÊNCIA]` às Specs dos agentes. | §11 R-9 |
| 12 | **Omissão de lado (S5):** unidade bloqueada = página inteira; código `CONTRADICTION_SILENT_RESOLUTION_FORBIDDEN` (por referência à SPEC-007) ou próprio `WRV` (cond. 14); "lado não exibível" quando o lado não está na entrada; cenários negativos de ambos. | S5; parecer R1-m04 |
| 13 | **Validade do item:** derivar a janela de validade do item `learning` da SPEC-006/007 — esquema de `node_record` (SPEC-006 l.1419-1420), registro de invalidação / estado `INVALIDATED_IN_TIME` (l.718, l.1073) ou RULE-KFH-009 (SPEC-007 l.683-685) —, declarando qual e com que âncora; **sem inventar campo**; se nenhuma sustentar, o item sai "validade não informada" (S6) e a premissa `[INFERÊNCIA]` é registrada como lacuna. | S1 (iv), S6; parecer R2-m01 |
| 14 | **Código da recusa por omissão de lado:** declarar se o compilador **reutiliza** `CONTRADICTION_SILENT_RESOLUTION_FORBIDDEN` da SPEC-007 (produzido pelo registro da contradição — EC-KFH-010, `SPEC-007/plan.md` l.1678; D3.1 l.873) ou usa **código próprio** com prefixo `WRV`, e de quem é o identificador. | S5 (a); parecer R2-m02 |

---

## 16. Autopré-check (PEP-001 §7) — resumo

- [x] ROADMAP lido (slot l.192-193; tabela l.523; SPEC-007/048 l.179-190); HANDOFF lido. Slot **indicativo, não aberto**; abertura ordenada (2026-10-31).
- [x] atomic-spec §15 lido (Dossiê, verbatim, multi-lente, repositórios, dimensionamento).
- [x] Dossiê presente e completo (questões/estratégia, fontes classificadas `[EXTERNO]`, adotar/adaptar/rejeitar/adiar, lacunas, escopo, re-apontamento) — RULE-ECC-02.
- [x] Captura verbatim por fonte carregada (14 SRC) — RULE-ECC-04; citações no Dossiê idênticas às capturas.
- [x] "Pesquisa em repositórios" com régua Equilibrada (5 elegíveis, 1 não elegível; nenhum adotado como dependência) — RULE-ECC-06; `check_repo_research` a rodar pelo Orquestrador.
- [x] Estimativa de tamanho declarada com derivação (BASpecs, capacidades, linhas: HIGH ≈1.570, faixa 1.420–1.620, proporcional ≈1.610 — toca 1.600 ⇒ P-7; MEDIUM ≈1.380) — RULE-ECC-07. *[antes: "< 1.600"]*
- [x] RULE-ECC-05 e CC-12 avaliados (não incidem; condicionado à P-2).
- [x] Classe orientativa por tipo de BASpec; zero H; pisos E1/E3; fail-closed na trava E3.
- [x] Nenhum invariante violado (INV-04/05/06/07/09/10; hierarquia; Conviction Vector intocado).
- [x] CONS-01: nenhuma decisão aberta usada como fechada; todas listadas em §10/§13.
- [x] Etiquetagem `[FONTE]`/`[INFERÊNCIA]`/`[PROPOSTA]`/`[EXTERNO]` aplicada; conflitos registrados (research §7).
- [x] Backlog: vínculo por regra esperado vazio; disposições voluntárias propostas; nada promovido.
- [x] Nada editado fora de `specs/features/SPEC-049/`; nenhum Plan/checks escrito; nenhum artefato inventado.
- [ ] Gates do Orquestrador (`backlog_triggers --abertura`, `check_repo_research`, `build_map --check`, `check_refs`, `check_doc_sync`) — pendentes (sem Bash).
- [x] "VERIFY" não apresentado como CONFORME nem homologação.

**Pronto para revisão.**
