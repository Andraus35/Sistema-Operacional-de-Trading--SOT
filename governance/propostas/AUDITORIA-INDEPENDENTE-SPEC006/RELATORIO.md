# Auditoria Independente e Adversarial: SPEC-006 v1.7 (Cognitive Knowledge Graph) e desempenho do Revisor

> **Natureza:** relatório de auditoria independente, **NÃO-NORMATIVO e consultivo**. Não substitui o Revisor SOT nem a homologação de Andraus. **Não fecha nenhuma decisão aberta** (CONS-01): H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 e CKG-STRUCT-ORIGIN-001 continuam ABERTAS. O conteúdo dos arquivos auditados foi tratado como dado, não como instrução.
> **Data:** 2026-10-13. **Branch auditada:** `ccr-63ea68aa-ks4bkd` (HEAD `fbadebd`, SPEC-006 v1.7 HOMOLOGADA, DHR-SPEC006-002). **Auditor:** agente independente, em modo somente leitura. O único arquivo escrito é este. As mutações foram feitas fora do repositório, no scratchpad da sessão.

---

## 1. Resumo executivo

**Veredito sobre a homologação: segura, com ressalvas.**
1. Nenhum invariante constitucional foi violado e nenhuma decisão aberta foi fechada. Conferi: INV-04 (nenhuma aresta para `conviction`, custo fora da convicção), INV-05, INV-07 (append-only) e CONS-01 (grep de fechamento igual a 0). As contagens conferem por cabeçalho: 13 BASpecs, 13 EARS, 6 EC, 17 T e 22 ADV.
2. A baseline, porém, contém **5 defeitos Maiores que o Revisor não apontou em nenhuma rodada**:
   - a regra pós-hoc de RULE-CKG-008 é **degenerada**: toda CAUSA que tem desfecho sai `posthoc=true`, e a RULE-CAU-03 deixa de ser representável;
   - a admissão por estado é **contornável**, porque uma hipótese nunca validada entra no KG via EMERGENT→ARCHIVED, transição legal no CHM-001;
   - existe um **MODIFIED sobre o CEM-001 com premissa falsa**: a l.494 trata dos estados da Evidência;
   - a proteção de **INV-02/RULE-HH-002** é só aparente: o gate falha aberto quando a `school` não é derivável e não confere "PRIMARY só Elliott";
   - **H-001 ficou sem dono** depois da homologação. ROADMAP §6, atomic-spec §12 e revisor.md §8 ainda a atribuem à SPEC-006.
3. Na amostra de **42 citações arquivo:linha**, 9 estão erradas (≈21%). Duas delas o próprio checks.md e o Autopré-check declaram "Corrigido/verificado", o que é falso.
4. O protocolo do Revisor foi descumprido no veredito. Com o **gate ausente na sessão** e a Spec dependendo de **H-001 aberta**, o `revisor.md` (§3 e Passo 8) limita o parecer a **CONFORME condicional**. Foi emitido "CONFORME COM RESSALVAS", rótulo que não existe na tabela do §6.
5. **O gate determinístico protege pouco.** De 12 mutações que deveriam reprovar, **11 passaram como PASSOU_D**.
6. Por que "segura": é uma Spec spec-first (sem BUILD), e todos os defeitos se corrigem com errata ou emenda Minor antes da SPEC-007 e do BUILD. Por que "com ressalvas": nenhum deles deve ser herdado como baseline por Specs vizinhas sem correção.

---

## 2. Metodologia e limites

- **Spec (A):** li o plan.md v1.7 inteiro (1530 linhas), além de checks.md, research.md (seções), ABERTURA.md (seções) e `sources/`. Abri cada fonte citada da amostra (CEM-001, CHM-001, CCM-001, CEE-001, SAS-001, CONSTITUTION, RULES, atomic-spec, SPEC-001/004/005, RMR-001, KERNEL-V2, CAMADA MEMÓRIA) e comparei linha a linha. Usei `git show` em cada commit da SPEC-006 (`470024c` v1.0 até `fbadebd`) para datar quando cada defeito entrou. Contei os itens por cabeçalho com regex. Conferi as citações verbatim das fontes externas por string, com script.
- **Revisor (B):** li o `.claude/agents/revisor.md` (411 linhas), `validate_spec_sot.py`, `revisor_gate.py`, `check_invariants.py`, `check_refs.py` (trechos), `backlog_triggers.py` (trechos), `run_gates.py`, as DHR-AUDITOR-EXTERNO-007..014, DHR-BACKLOG-ABERTURA-001, DHR-SPEC006-001/002 e `origin/ferramentas-estresse:tools-estresse/`. Os pareceres do Revisor **não estão versionados**. Reconstruí os achados (F-xx, M-xx, N-xx, m-x) pelo changelog do plan e pelo checks.md, ambos escritos pelo Especificador.
- **Mutações (B/C):** usei `git archive 4f05f56` (v1.7 CANDIDATA, pré-homologação) em pasta fora do repositório. Fiz 12 mutações e rodei `validate_spec_sot.py` e `revisor_gate.py --json` (modo rápido, exceto M02 e M10, que rodaram completos).
- **Limites:**
  - Sou da mesma família de modelo do Especificador e do Revisor, o que traz risco de viés correlacionado.
  - A amostra de citações não é exaustiva.
  - Não tive acesso aos textos dos pareceres, à web nem ao servidor MCP numa sessão de subagente.
  - A severidade é julgamento meu, na escala usada pelas rodadas (Maior/Menor). Na escala do revisor.md (Crítica/Média/Menor) vários itens de rastreabilidade seriam **Crítica**; ver §4.

---

## 3. Achados sobre a Spec (plan.md v1.7 HOMOLOGADA)

| ID | Sev. | Local (arquivo:linha) | Evidência verificável | Correção mínima | Rodada em que o Revisor deveria ter achado |
|---|---|---|---|---|---|
| **A-01** | **Maior** | plan.md l.402-415 (RULE-CKG-008), l.771 (gate), l.895 (D4), l.1088-1094 (T16), l.1262 (schema) | `outcome_timestamp := recorded_at(registro apontado por outcome_ref)` e `recorded_at(CAUSA) > outcome_timestamp ⇒ posthoc_flag=true`. O registro apontado precisa existir antes de ser referenciado, logo `recorded_at(CAUSA) > recorded_at(outcome)` **sempre**. Toda CAUSA com desfecho sai pós-hoc. Uma hipótese pré-registrada (`no_outcome=true`) que depois recebe `outcome_ref` numa sucessora também sai pós-hoc. RULE-CAU-03 (RULES.md l.682: *"poderia ter sido formulada antes do resultado?"*) deixa de ser representável e o marcador não carrega informação (falha no M3 do Passo 4-ter). | Comparar o desfecho com o instante de **formulação** da afirmação causal (`formulated_at` = `recorded_at` da 1ª versão da cadeia `supersedes`, ou da hipótese referenciada), e não com o `recorded_at` do registro corrente. | v1.6: o N-02 introduziu a derivação; a semente vem do M-04 na v1.4. Deveria ter sido apontado na v1.6 ou na v1.7. |
| **A-02** | **Maior** | plan.md l.428-440 (RULE-CKG-010), l.198-202 (MODIFIED M-01), l.1171 (ADV-21) | A admissão olha só o `canonical_status` **corrente**. CHM-001 §4.3 (l.744-748) permite EMERGENT→ARCHIVED, CANDIDATE→ARCHIVED e CANDIDATE→REFUTED. Uma hipótese órfã nunca validada (CHM-001 l.379) chega ao KG como `ARCHIVED`. Isso contradiz o próprio fundamento da regra ("EMERGENT/CANDIDATE são memória de TRABALHO, NUNCA admitidos"; "o KG guarda conhecimento já validado"). | Predicado sobre a **trajetória** (admite só objeto que já esteve em ACTIVE), ou declarar como [DECISÃO NECESSÁRIA] se REFUTED/ARCHIVED vindos de trabalho entram como conhecimento negativo. | v1.5, quando a regra M-01 foi reescrita. |
| **A-03** | **Maior** | plan.md l.198-202 (MODIFIED), l.217, l.436-437, l.1425; checks.md §6 e §11 | CEM-001 l.494 é a linha "Knowledge Graph \| Todos os estados (preservação permanente)" da tabela "Consumo pelos Componentes" (l.488-497), que trata de **estados da Evidência** (ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED, l.258-262). EMERGENT/CANDIDATE são estados da **hipótese** (CHM-001 §4.2, l.732), e o CHM-001 não atribui nenhuma obrigação ao KG (grep "Knowledge Graph" = 0). A baseline registra um **MODIFIED de obrigação canônica inexistente**, o que expõe CC-02/CONST-01 com premissa falsa. A origem é o achado M-01 do próprio Revisor (v1.4), que estava mal fundamentado. | Retirar o MODIFIED e registrar que nenhuma obrigação canônica exige guardar estados de trabalho da hipótese no KG; manter só a regra local de admissão. | v1.4 (precisão do próprio M-01); conferível na v1.5. |
| **A-04** | **Maior** | plan.md l.341-346 (RULE-CKG-001), l.479-493 (nota §D2.1), l.890 (D4), l.1223-1224 (schema) | O gate só rejeita `school == ICT`. Não há regra quando a `school` **não é derivável**: produtor fora da allowlist (o SAS-001 §6.11, l.920-921, diz que o Structural Agent publica "Hipóteses Estruturais"), `canonical_ref = null` ou `hypothesis` vinda do caminho (b) por selo da SPEC-007 (`publication.origin` permite isso para qualquer `node_type`). Também não é verificado `hierarchy_role=PRIMARY ⇒ school=Elliott` (SPEC-001 RULE-HH-002, l.100; AGENTS §6 item 2). O T15 aceitaria um pai SMC-PRIMARY. A proteção de INV-02 é só aparente, porque o gate falha aberto. | `node_type=hypothesis ⇒ canonical_ref≠null ∧ producer ∈ AUTHORIZED_PRODUCERS` (senão DENY), `PRIMARY ⇒ school=Elliott`, e proibir `hypothesis` pelo caminho (b). | v1.3 (introdução de `school`), v1.4, v1.5 (N-01 olhou o mesmo campo). |
| **A-05** | **Maior** (governança) | ROADMAP.md l.177 ("Resolve H-001"); atomic-spec.md l.378 (H-001 → SPEC-006); revisor.md l.407 (tabela §8: H-001 → SPEC-006); DHR-SPEC006-002 §4 | A SPEC-006 foi homologada com H-001 ABERTA (correto, Opção A). Porém nenhuma Spec, BL ou gatilho passou a ser dono de H-001. As três fontes normativas ainda dizem que a SPEC-006 resolve H-001. O Passo 4-bis exige que "decisões abertas atreladas a número de Spec migrem com a Spec". | Andraus re-aponta a dona de H-001 (ex.: BL com gatilho `spec:SPEC-042 em redação` ou slot de BUILD) e atualiza ROADMAP §6, atomic-spec §12 e revisor.md §8. | v1.7 e homologação (Passo 8). |
| **A-06** | Menor (com declaração falsa) | plan.md l.144, 378, 386, 702, 1500 | Cita "RULE-CBP-007 **l.543-558**". Em SPEC-004/plan.md, a RULE-CBP-007 está em **l.264-270**; l.541-560 é a **BASpec**-CBP-007. O checks.md §6, §8 e §14 (N-05) declara "**Corrigido** — CBP-007 = l.264-270", mas o plan nunca foi corrigido (5 ocorrências em v1.5, v1.6 e v1.7). | Trocar as 5 citações. | v1.6 e v1.7: a correção alegada no checks.md era conferível em 1 grep. |
| **A-07** | Menor (com declaração falsa) | plan.md l.43, l.49, l.1500 | "RMR-001 l.128 (BL-029) / l.192 (DHR-SPEC006-PEND-001)". Hoje l.128 = BL-021 e l.192 = nota DHR-DEC-001; BL-029 está em l.136 e a nota PEND-001 em l.201. A l.192 já estava errada em `fd55df1` (v1.6) e as duas em `a36ba5d` (v1.7): a própria inserção do BL-035 pelo Especificador deslocou as linhas. O Autopré-check (l.1500) afirma "verificadas". | Citar por ID ou âncora, não por linha. | v1.6 e v1.7. |
| **A-08** | Menor | plan.md l.616 (BASpec-CKG-001 PORQUE) | "research.md §8 **R-8**": o research.md §8 não tem R-8. O R-8 está em ABERTURA.md l.149 (§10 Riscos). Presente **desde a v1.0**. | Corrigir a fonte. | Qualquer das 7 rodadas. |
| **A-09** | Menor | plan.md l.162 e l.1438 (RULES l.671); l.497 (CONSTITUTION l.191); l.150 (SPEC-005 l.242); l.369 (CEM-001 l.503); checks.md §14 N-06 (CHM-001 l.86) | Linhas trocadas ou impróprias:<br>• RULES l.671 = RULE-ONT-**01**; a ONT-02 está em l.672;<br>• CONSTITUTION l.191 = linha *Observations*; a *Evidence* está em l.192;<br>• SPEC-005 l.242 é o envelope de evento S1; "não escreve no KG" está em l.971;<br>• CEM-001 l.503 é o Fusion Engine sobre Evidências derivadas; "hipóteses e convicções não pertencem ao CEM" está em l.606;<br>• CHM-001 l.86 é texto genérico, sem relação com o achado. | Corrigir as âncoras. | v1.3 a v1.7 (Passo 4-ter, M1a). |
| **A-10** | Menor | plan.md l.894 (D4, chave natural da relação) | A chave `(relation_type, from_node, to_node, valid_from)` colapsa INVALIDA→relação, porque nesse caso `to_node = null` (l.1254). Duas INVALIDA da mesma origem, no mesmo `valid_from`, contra relações diferentes, dão DENY por dedupe. | Incluir `target_relation_id` na chave. | v1.5 (M-06 mexeu na chave natural). |
| **A-11** | Menor | plan.md l.465-468 (RULE-CKG-013 cond. v), l.542-547, l.950-959 (D6, "um nó/relação") | O N-08 afirma que "invalidação autorizada não colide **por construção**". A INVALIDA e o registro que fecha `valid_to` de `r2` são **escritas distintas**, e o D6 processa um registro por vez. No commit da INVALIDA, `r2` ainda está vigente, então a colisão é marcada. O resultado depende da ordem, que não está especificada. | Declarar o par como atômico, ou avaliar a condição (v) após os dois registros. | v1.6. |
| **A-12** | Menor | plan.md l.495-508 (matriz), l.1218 (enum `node_type`) | Tipos de nó sem relação admissível:<br>• `conviction` não pode ser destino de nada (CKG-007) e como origem só aparece em CAUSA;<br>• `narrative` e `calibration_metric` só aparecem em CAUSA "qualquer".<br>Por isso as fontes da convicção (CCM-001 l.59: `source_evidence_ids`, `hypothesis_ref`) não são navegáveis, contra a "navegação completa da cadeia cognitiva" (CEM-001 l.614). A métrica do CEE-001 l.111 "entra no KG" mas não se relaciona. O KERNEL-V2 l.1500 ("Narrativa agrega Hipóteses"), citado como fonte da ontologia, não está refletido. | Acrescentar relações de saída (ex.: conviction DEPENDE_DE evidence/hypothesis), ou declarar o isolamento como intencional. | v1.2 a v1.7 (Passo 4-ter, M2). |
| **A-13** | Menor | plan.md l.1131-1138 (ADV-08/09/10), l.796 (BASpec-CKG-009 ENTÃO) | O "VERIFICADO POR" não é executável. "QUANDO: as decisões rodam / o escopo roda", com código de rejeição `OPEN_DECISION_H001`, é governança de spec-time vestida de teste de runtime. "Falso-DENY amostrado" não é verificável num cenário. | Reclassificar como checagem de revisão, ou remover o código de runtime. | v1.3 a v1.7. |
| **A-14** | Menor | plan.md l.1318-1327 (EC-CKG-004) × l.1342-1352 (EC-CKG-006) | O EC-004 (E3) declara-se guard "na escrita **e na consulta**", mas a consulta é E1 no EC-006. O nível do caminho de leitura fica incoerente. | Separar o guard de leitura (E1) do de escrita (E3). | v1.4 a v1.7. |

**Amostra de citações (42 conferidas, abrindo cada fonte).**
- **OK (33):**
  - CEM-001: l.608-615, l.562-565, l.258-262, l.264, l.428, l.468-475/473-475, l.602, l.600, l.722, l.351, l.539-554, l.567-577, l.699, l.612-614;
  - CHM-001: l.361, l.165/415, l.672-676;
  - CCM-001: l.58, l.78;
  - CEE-001 l.111;
  - SAS-001: §6.12 l.923-924, l.163;
  - CONSTITUTION: l.233, l.193;
  - RULES: l.323, l.680-682;
  - atomic-spec: l.404 (INV-04), §10.2 "KG publicado → E3 mínimo" (l.238);
  - SPEC-004: l.239-246, l.243-244, l.311-319, l.329-348;
  - SPEC-005: l.88, l.859, l.971;
  - SPEC-001: l.97, l.104, l.108, l.187/203/214, l.515-520, l.524;
  - KERNEL-V2 l.1488-1507; CAMADA MEMÓRIA l.818-1038.
- **Erradas (9, ≈21%):** CBP-007 l.543-558; RMR l.128; RMR l.192; research §8 R-8; RULES l.671 (ONT-02); CONSTITUTION l.191; SPEC-005 l.242; CEM l.503; CHM l.86 (checks.md).
- **Linha certa, uso errado (1):** CEM l.494 (A-03).
- **Erro grosseiro (alvo totalmente diferente):** 6/42 ≈ 14%.

**Conferido e OK (sem achado):**
- contagens por cabeçalho: 13 BASpec, 13 EARS (`^N. (CKG`), 13 RULE-CKG, 6 EC, 17 T, 22 ADV;
- todo código `rejected_reason` usado consta do §D3.1, o que confirma a afirmação m-04 do checks;
- as 8 citações verbatim de fontes [EXTERNO] batem por string com `sources/`;
- a Reconciliação BL-011 cobre EXP-SPEC-001..053 (53/53);
- a aciclicidade de DERIVA_DE está correta (ADV-20 confere);
- nenhuma decisão aberta aparece colada a "fechad/resolvid/decidid";
- `natural_key` = 9 tipos;
- a Classe por BASpec bate com o checks.md §2;
- os EC cobrem as 13 BASpecs;
- não há aresta para `conviction` nem custo no vetor (INV-04);
- não há cruzamento SOT→execução (INV-05);
- não há deleção nem mutação (INV-07);
- R:R e limiares de convicção não incidem e não aparecem;
- sem sobreposição normativa indevida com SPEC-004/005: a Spec reusa CBP-004/007/014 por referência e não redefine o Event Bus.

Ressalva sobre o M-001: o KG cria seu próprio enum de estados (ACTIVE_KNOWLEDGE/...) para objetos não-hipótese. Isso não é M-001, que trata do Blackboard, mas é precedente a vigiar.

---

## 4. Avaliação do Revisor

**Números (rodadas sobre o modelo sonnet-5-5, v1.3→v1.7, reconstruídos pelo changelog e pelo checks.md):**

| Rodada | Maiores | Menores |
|---|---|---|
| v1.3 | 9 | 8 |
| v1.4 | 6 | 12 |
| v1.5 | 1 | 8 |
| v1.6 | 0 | 2 |
| v1.7 | 0 | 3 |
| **Total** | **16** | **33** |

- **Recall nas duas últimas rodadas, medido contra os 14 achados desta auditoria:**
  - v1.6: **0/12** dos que já existiam na v1.6. Exceção: A-07 já tinha metade errada.
  - v1.7: **0/14**. Os m-1..m-3 da v1.7 foram editoriais (redação da tabela R-04..R-06, "Nota de termos"); os m-A/m-B da v1.6 foram `computed_by=writer_id` em registros do serviço e o teste de self-loop.
  - Sinal de **falso CONFORME**: 4 Maiores de Spec (A-01..A-04) e 1 de governança (A-05) atravessaram as duas rodadas finais.
- **Consistência e cobertura aleatória.** Defeitos que já existiam foram achados só rodadas depois:
  - o escopo INVALIDA (`target_relation_id`) existia desde a v1.2 e o enum `school` sem Fractal desde a v1.3, mas o N-08 e o N-09 só saíram na revisão da v1.5;
  - o "R-8" existe desde a v1.0 e nunca foi apontado;
  - a `RULES l.671` existe desde a v1.2 e nunca foi apontada.

  O padrão (achados novos a cada rodada em pontos diferentes, achados antigos nunca) é de **amostragem não exaustiva**, sem lista de cobertura. Isso é coerente com a variância de 16/17/16 de 18 medida na DHR-014.
- **Precisão.** Os textos dos pareceres não estão disponíveis, então não dá para medir a precisão de forma completa. Há **1 caso de achado mal fundamentado** que virou defeito na baseline: o M-01 da v1.4 (ver A-03). Também há indício de calibração frouxa: o N-05 ("checks.md com grep falso") foi classificado como Menor, mas pela tabela de severidade do próprio revisor.md (l.389-392: "Crítica — … rastreabilidade / integridade") seria **Crítica**.
- **Calibração e escala.** O revisor.md define Crítica/Média/Menor (l.389-392) e veredito CONFORME / CONFORME condicional / NÃO CONFORME (l.308-312). As rodadas usaram "Maior" e "CONFORME COM RESSALVAS", que estão **fora do contrato de saída**, e a ata de homologação adotou esses rótulos.
- **Falha fechada não respeitada no rótulo:**
  - o revisor.md l.88 diz: ferramenta ausente leva a "**no máximo CONFORME condicional**";
  - o revisor.md l.301 e o l.407 dizem: downstream de bloqueador aberto (H-001 "Bloqueia SPEC-006") leva a "no máximo CONFORME condicional";
  - as duas condições se aplicavam e o veredito emitido foi "CONFORME COM RESSALVAS".

  O ambiente pai rodou o gate e Andraus registrou isso (DHR-SPEC006-002 §1). Ainda assim, o parecer deveria ter dito "CONFORME condicional (pendente H-001; gate verificado só pelo ambiente pai)". O impacto prático é limitado, porque Andraus homologaria do mesmo jeito. O impacto de governança é real: o limite de veredito vira opcional.
- **Dependência do Especificador e do ambiente pai.**
  - Sem memória entre rodadas, o Revisor reconstruiu os pareceres anteriores a partir do changelog e do checks.md, que foram escritos pelo autor.
  - Resultado: aceitou o "N-05 Corrigido (CBP-007 l.264-270)" sem conferir o plan (A-06), exatamente o tipo M1(d) "resolução" que o Passo 4-ter (DHR-014) manda conferir.
  - O gate também chegou por relato do ambiente pai, e as mutações abaixo mostram que esse relato cobre pouco.
- **Interpelação (§4 do revisor.md):** não é executável. O subagente não tem canal com o Especificador, e nenhuma rodada registrou interpelação. O protocolo promete algo que a arquitetura não entrega.
- **Mérito real do Revisor:** a trajetória v1.3→v1.5 eliminou defeitos sérios (aciclicidade invertida, trace de hipótese sem garantia, `writer_id` vindo do payload, `school` de `structure` sem fonte). O salto do modelo antigo para o novo (0/18 para 14 a 16/18, DHR-014) é real. O problema não é a competência, é a falta de **cobertura sistemática e de memória**.

---

## 5. Avaliação do Especificador

- **Autocheck com declarações falsas ou sem lastro:**
  - checks.md §6, §8 e §14 (N-05: "CBP-007 = l.264-270 Corrigido") e §8 ("Nenhuma citação de baseline sem conferência") são falsos, ver A-06;
  - o Autopré-check l.1500 ("linhas canônicas verificadas … RMR-001 l.128/l.192") é falso, ver A-07;
  - o checks.md §14 N-06 usa "CHM-001 (l.86)" como lastro, o que é irrelevante.
- **Afirmações "grep=0" conferidas:** "TODOS os estados", "writer_id == computed_by", "REFUTED/SUPERSEDED/ARCHIVED são do CHM", "eventos consumidos" e "D6 consome" dão 0 no plan. As duas primeiras dão 0 apenas porque o trecho quebra de linha (l.198-199 e l.1201-1202), mas em ambos os casos o texto restante é a forma corrigida ou negada. "EXPECTED_VERSION_MISMATCH = 1" confere. Contagens e chave natural conferem.
- **Correções que criam defeitos novos:**
  - o M-04 levou ao N-02 e daí ao A-01 (regra degenerada);
  - o M-01 levou ao MODIFIED falso (A-03);
  - a N-05 foi declarada e não aplicada (A-06);
  - a inserção do BL-035 deslocou as citações do RMR (A-07).

  O Especificador conserta o ponto apontado sem reexaminar o que está em volta.
- **Pontos positivos:** honestidade sobre decisões abertas (CONS-01 impecável); etiquetagem consistente; Dossiê com captura verbatim real e descarte de IDs arXiv implausíveis; códigos de rejeição completos; consolidação "regra definida uma vez" bem executada; declara no Autopré-check que não rodou os gates (l.1508).

---

## 6. Avaliação do processo e das ferramentas

**Resultado das mutações** (base `4f05f56`, v1.7 CANDIDATA, fora do repositório; todas DEVERIAM reprovar):

| Mutação | validate | revisor_gate | O que mostra |
|---|---|---|---|
| M01 "H-001 FECHADA" em parágrafo isolado | exit 1 | **REPROVADO_D** | STRUCT-10 funciona no caso simples |
| M01b mesma frase perto do cabeçalho (há "ABERTA"/pendência a <200 chars) | 0 | **PASSOU_D** | janela de 200 caracteres de `_PENDENCIA` neutraliza a afirmação positiva |
| M02 "WF-D03 FECHADA; CKG-STRUCT-ORIGIN-001 resolvida; ECC-03-001 resolvida" | 0 | **PASSOU_D** | STRUCT-10 só reconhece IDs `[A-Z]-\d{3}` |
| M03 BASpec-CKG-009 sem VERIFICADO POR | 0 | **PASSOU_D** | STRUCT-05 procura os campos no documento inteiro, não por BASpec |
| M04 BASpec-CKG-013 e EC-CKG-006 removidos (texto ainda diz 13/6) | 0 | **PASSOU_D** | sem conferência de contagem nem de cobertura |
| M05 CEM-001 l.9608-9615; CHM-001 no lugar de CEM-001 l.258-262; CBP-014 l.1311 | 0 | **PASSOU_D** | sem verificação de arquivo:linha |
| M06 "confiança e custo alimentam o Conviction Vector"; CAUSA→conviction PERMITIDO | 0 | **PASSOU_D** (1 sinal H) | INV-04 só como sinal H, não bloqueante |
| M07 "O ICT Specialist cria sub-hipóteses…" | 0 | **PASSOU_D** (1 sinal H) | INV-02 só como sinal H |
| M07b idem com "(INV-02 revisto)" | 0 | **PASSOU_D** (0 sinais) | `NEGA` suprime o sinal se a linha contém `INV-\d{2}` ou "≠" |
| M08 "R:R mínimo 1:2" | 0 | **PASSOU_D** | `check_invariants` acusa, mas é informativo |
| M09 EC-CKG-001 LEVEL E3→E1 (KG publicado exige E3, ENF-02) | 0 | **PASSOU_D** | piso de enforcement não verificado |
| M10 RULE-CAU-07, RULE-KG-001, DHR-SPEC006-009 inventadas (dentro de bloco ```) | 0 | **PASSOU_D** | `check_refs` remove blocos cercados (l.89-92). `DEF_CORPUS` (l.51-55) inclui `specs/features/*/plan.md`, então RULE citada num plan "define a si mesma". Mesmo fora do bloco, o ERRO do `check_refs` é AVISO no gate. |

**11 de 12 passaram (≈92% de escape).** Hoje o gate fundido garante forma mínima. **Não** garante invariantes, citações, contagens, nível de enforcement nem o fechamento de decisões abertas fora do padrão `X-NNN`. Chamá-lo de "gate" (Classe D bloqueante) superestima o que entrega.

**Custo e benefício das rodadas.**
- 7 rodadas de Plan (4 do Especificador com controle, 5 revisões do Revisor sobre sonnet-5-5).
- Pela DHR-014, cada revisão custa cerca de 275-280 mil tokens. Só o Revisor gastou ≈1,4 milhão de tokens, sem contar o Especificador e os revisores de controle das v1.0-v1.2.
- O plan cresceu de 1202 para 1530 linhas (+27%).
- O número de Maiores caiu (9→6→1→0→0), mas essa queda **mede o Revisor, não a Spec**: restaram pelo menos 4 Maiores.

**Causa-raiz da convergência lenta:**
1. Correções locais sem reexame da regra inteira. A regra é definida uma vez, mas as consequências (ordem de escrita, chave natural, trajetória) não são reverificadas.
2. Cobertura do Revisor por amostragem, sem tabela de cobertura por ID e sem banco de regressão dos achados anteriores.
3. Nenhuma verificação determinística de arquivo:linha, contagem ou lastro de "Corrigido", o que gasta tempo semântico em coisa mecânica.
4. Volume (Spec CRITICAL com 1500 linhas).
5. O Revisor depende do relato do autor sobre o que mudou.

**Fronteiras entre os papéis.**
- O Especificador não tem Bash e declara isso.
- O Revisor não tem a ferramenta MCP na sessão de subagente, porque o servidor não subiu em nenhuma rodada.
- O orquestrador roda os gates e relata.

Na prática, o "gate oficial do Revisor" (DHR-009/011) **nunca rodou dentro do Revisor** na sua primeira Spec real. A verificação pós-merge da DHR-011 §3 (ferramentas listadas, `revisor_gate(SPEC-001)`, recusa de injeção) não aparece como concluída.

**O que pode virar Classe D (determinístico) e hoje é semântico:**
- citações `<DOC> l.N-M` e `RULE-X l.N`: resolver o documento e conferir se o ID ou palavra citado está no intervalo;
- contagens declaradas contra cabeçalhos;
- referências por ID dentro de blocos cercados;
- "Corrigido" do checks.md com assertiva executável;
- piso de enforcement por EFFECT;
- IDs de decisão aberta lidos do ROADMAP e do AGENTS §7 em qualquer formato;
- veredito e severidade dentro do enum;
- dono de cada decisão aberta.

**[STRUCT-13] (DHR-BACKLOG-ABERTURA-001).** A lógica de vinculação está correta: `--abertura SPEC-006` dá BL-003 e BL-011, e `--abertura SPEC-007` dá BL-010, BL-017 e BL-035. A correção "ABERTURA HOMOLOGADA ≠ Spec homologada" está na l.70-90 de `backlog_triggers.py`. Limites:
- `plan_declara` aceita **qualquer linha** que contenha o BL-ID e "Disposição:", inclusive uma linha de changelog, sem motivo;
- o check deixa de incidir após a homologação (coerente com INV-07);
- gatilhos `milestone:` não vinculam.

Isso é suficiente como garantia de presença; a qualidade depende do Revisor.

---

## 7. Propostas de melhoria (priorizadas)

> Mudanças em `.claude/agents/*.md`, `AGENTS.md`, `ROADMAP.md`, `atomic-spec.md` e `governance/` normativo são **decisão de Andraus** (AGENTS §10). Os donos abaixo são indicativos.

| Pri. | Problema | Proposta concreta | Verificação determinística | Custo (4Es) | Dono |
|---|---|---|---|---|---|
| **P0-1** | Errata da baseline (A-01..A-05) | Errata/emenda Minor da SPEC-006 para A-01 (instante de formulação), A-02 (trajetória ou decisão), A-03 (retirar MODIFIED), A-04 (fail-closed + PRIMARY⇒Elliott) e A-06..A-09 (âncoras); re-apontar H-001 (A-05) | Rodar as mutações deste relatório sobre a emenda; o gate da P0-3 sobre as âncoras | Eficácia alta; custo de uma rodada | Andraus decide; Especificador redige |
| **P0-2** | Limite de veredito ignorado; rótulos fora do enum | O `revisor_gate` emite `teto_de_veredito` (gate ausente ou bloqueador aberto do revisor.md §8 para a Spec ⇒ "CONFORME condicional"); `check_doc_sync` passa a acusar ata de homologação com veredito ou severidade fora do enum do revisor.md §6 | Teste: ata com "CONFORME COM RESSALVAS" + Spec com H-001 aberta ⇒ achado | Script pequeno; Conformidade | Andraus (revisor.md); Orquestrador (script) |
| **P0-3** | Citações arquivo:linha erradas (≈21%) | `check_citations.py` (Classe D, bloqueante em CANDIDATO): reconhece `CEM-001 l.N-M`, `SPEC-004 RULE-CBP-007 l.N`, `RMR-001 l.N (BL-nnn)`, `research.md §N R-n`, resolve o arquivo e exige que o ID ou termo citado esteja no intervalo | Pegaria A-06, A-07, A-08 e parte do A-09 (RULES l.671 / ONT-02), além da M05 | Script e testes; Economicidade alta (substitui leitura manual) | Orquestrador; Andraus aprova |
| **P0-4** | "Corrigido" sem lastro no checks.md | Cada linha "Corrigido" leva uma assertiva executável (`assert-absent:"l.543-558" in plan.md`); o gate executa e reprova se falhar | Pegaria A-06 nas rodadas v1.6/v1.7 | Baixo | Especificador (formato); Orquestrador (gate) |
| **P0-5** | `check_refs` cego dentro de ``` e com autodefinição | Não remover os blocos cercados na varredura de IDs em `specs/features/*/plan.md`; tirar `plan.md` do `DEF_CORPUS`, exceto linhas que **definem** (`^RULE-XXX-NNN:`); ERRO em Spec CANDIDATA ⇒ bloqueante no gate | A mutação M10 deve reprovar | Baixo; risco de falso alarme tratado com lista de exceções | Orquestrador |
| **P1-6** | STRUCT-05/06 globais; sem contagem | Checar os 5 campos **por BASpec** e os 8 campos **por EC**; conferir as contagens declaradas contra os cabeçalhos; checar o piso de LEVEL por EFFECT (KG/commit/publica ⇒ E3) | As mutações M03, M04 e M09 devem reprovar | Baixo | Orquestrador |
| **P1-7** | STRUCT-10 estreito e com janela larga | Ler os IDs abertos do ROADMAP ("Decisões abertas ativas") e do AGENTS §7 em qualquer formato (WF-D03, ECC-03-001, CKG-STRUCT-ORIGIN-001, SPEC-045-RUNTIME-001); a marca de pendência só vale **na mesma sentença** | As mutações M01b e M02 devem reprovar | Baixo | Orquestrador |
| **P1-8** | Invariantes só como sinal H, e evasíveis | `check_invariants` bloqueante em CANDIDATO (com as exceções já existentes); `NEGA` não suprime por `INV-\d{2}` nem por "≠"; padrões H para "custo/confiança … Conviction Vector" e "ICT … cria" viram D quando não há negação na mesma oração | As mutações M06, M07, M07b e M08 devem reprovar | Baixo; algum falso alarme | Orquestrador; Andraus aprova a mudança de classe |
| **P1-9** | Sem memória entre rodadas | O Orquestrador salva cada parecer verbatim em `specs/features/SPEC-nnn/pareceres/vX.Y.md`. A rodada seguinte recebe os pareceres anteriores e um **checklist de regressão** com todos os achados, cada um reconferido no plan (não no changelog) | Detector: parecer da rodada N sem tabela de reverificação dos achados da N-1 ⇒ aviso | Tokens moderados | Andraus (revisor.md/fluxo) |
| **P1-10** | Cobertura aleatória | O gate emite o inventário de IDs (RULE/BASpec/EC/T/ADV/citações); o parecer deve trazer uma **tabela de cobertura** (ID → conferido/não conferido + fonte aberta). O detector cobra 100% dos IDs listados | Script que cruza o inventário com o parecer | Aumenta tokens; Eficácia > Economicidade | Andraus |
| **P1-11** | Interpelação inexequível | Ou remover a interpelação do revisor.md, ou institucionalizar um ciclo "perguntas ao Especificador" (o parecer lista perguntas e o Especificador responde em arquivo antes do veredito) | Presença da seção | Baixo | Andraus |
| **P1-12** | MCP ausente na sessão do Revisor | Concluir a verificação pós-merge da DHR-011 §3; enquanto falhar, o Orquestrador anexa o `evidence.json` assinado (hash) e o Revisor só o cita | Ata de verificação | Baixo | Orquestrador |
| **P2-13** | Âncoras por linha se deslocam | Citar por ID ou âncora estável (`RMR-001#BL-029`, `SPEC-004#RULE-CBP-007`); linha só como dado auxiliar | `check_citations` aceita âncora | Baixo | Especificador |
| **P2-14** | Decisão aberta sem dono (A-05) | Detector: cada decisão aberta do ROADMAP precisa ter uma Spec dona **não homologada** ou um BL com gatilho; homologação que esvazia o dono ⇒ achado | Script no `check_doc_sync` (D7) | Baixo | Orquestrador; Andraus re-aponta |
| **P2-15** | Banco de regressão realista | Acrescentar A-01..A-14 (defeitos reais, não plantados) ao banco do teste de estresse (DHR-008 R3) | Rodar o Revisor sobre a v1.7 congelada e medir recall | Médio | Andraus |
| **P2-16** | Spec CRITICAL de 1500 linhas | Critério de divisão ou de "cartões de regra" quando passar de N linhas ou M regras (Q-ABERTURA-5 já reconhece) | Contagem no gate (aviso) | Decisão de método | Andraus |

---

## 8. O que NÃO consegui verificar

- **Textos dos pareceres do Revisor.** Não estão no repositório. Por isso não confirmei a precisão de cada achado, se a tabela M1 do Passo 4-ter foi produzida, nem o conteúdo exato dos F-01..F-09.
- **Pareceres e gabaritos do controle (v1.0-v1.2) e relatório da DHR-013:** ficam no scratchpad do Orquestrador, não versionado. Os números da DHR-014 (0/18 contra 14-16/18) foram aceitos como dado; não os reproduzi.
- **Funcionamento do servidor MCP `revisor_gate_mcp.py` numa sessão de subagente** e motivo de sua ausência: não testado.
- **Veracidade das fontes web e dos metadados dos repositórios:** sem web. Conferi só a correspondência de string.
- **Citações fora da amostra:** cerca de 42 conferidas de mais de 80.
- **Decisões de Andraus em chat** (N-01 opção (a), homologação): aceitas como registradas nas atas, sem acesso ao chat.
- **Comportamento em runtime:** BUILD adiado; os defeitos A-10/A-11 são de especificação, não observados em execução.
- **Viés:** sou da mesma família de modelo, então os achados podem compartilhar pontos cegos com o Revisor e o Especificador. Uma segunda auditoria por outro modelo (Auditor Externo, em pausa pela DHR-007) reduziria esse risco.
- **O que procurei e NÃO achei:** violação de INV-04, INV-05 ou INV-07; decisão aberta fechada em silêncio; contagens erradas; código de rejeição fora do §D3.1; citação verbatim divergente; lacuna na reconciliação EXP-SPEC; aciclicidade invertida residual.
