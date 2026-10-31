# Parecer do Revisor — Proposta de Abertura da SPEC-049 (WikiRAG Reading View) — R1 integral (S2, sonnet) — 2026-10-31

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura). Alvo: `specs/features/SPEC-049/ABERTURA.md` (+ `research.md`, `sources/`).
> MODO: integral
> SHA256-ALVO: 07a942c3e73e0c1a61a666a29a99d2f8b9e55a0fa065bc28cf1f30fd2fc3f779 (valor recebido do Orquestrador; o Revisor não calculou — sem Bash)
> TOKENS: 172341
> **Veredito: NÃO CONFORME (Média)** — 0 Críticas, 1 Média (R1-M01), 8 Menores (R1-m01..R1-m08). Teto, mesmo corrigido: CONFORME condicional (gate não executado dentro da sessão do Revisor; gates rodados pelo Orquestrador = dado de estado).

## 1. Veredito
- O processo do Dossiê está sólido: ECC-02, 04, 06 e 07 conferem. Nenhuma fonte carregada sem captura, nenhuma citação divergente.
- A Média é de conteúdo: a "entrada" da compilação (S1) não fixa a referência de tempo da validade, o que abala a garantia de reconstrução byte a byte (S7).
- Correção curta. Devolver ao Especificador e fazer rodada 2 em delta. A decisão de peso (P-1) é de Andraus; a justificativa é consistente com o perfil de profundidade.

## 2. Alinhamento
Passo 0: ROADMAP l.176-195 (slot SPEC-049 l.192-193, tabela l.523), atomic-spec §15 (l.441-457) e tabela D0-D8 (l.44-53), RULES.md RULE-ECC-06/07 (l.500-534), painel RMR-001. Spec autorizada: SPEC-049 (slot indicativo, abertura ordenada). Interpelação formal não feita (sem canal); o Autopré-check (§16) foi tratado como afirmação a conferir.

## 3. Conferências solicitadas
1. **RULE-ECC-04: CONFORME.** 14 SRC-*.txt abertos; cada citação entre aspas no research §3.1-3.8 idêntica à captura (string). Trechos que sustentam alegação ≥100 caracteres (bordas: SRC-SDE ~104, REPO-DATASETTE ~101, REPO-QUARTZ = 100). URL e data em todos. Benchmark não lido (declarado). Autenticidade das capturas: risco residual (sem web).
2. **RULE-ECC-06: CONFORME.** Seção "Pesquisa em repositórios" (§4) e 6 REPO-*.txt com campos da régua. mkdocs NÃO ELEGÍVEL (último commit 2025-10-20; 376 dias no acesso 2026-10-31; conta confere). Quartz (2026-04-20) dentro dos 12 meses. Alertas de segurança INDETERMINADO registrado como 0 (limite declarado em _LIMITACAO-WEB item 2).
3. **RULE-ECC-07: declarada, plausível com ressalva (m1).** 10 BASpecs (títulos), capacidades e linhas (HIGH ≈1.250, faixa 1.000-1.500; MEDIUM ≈880) declaradas; somas conferem (400+700+150; 380+400+100). Falta derivação de "70 linhas por BASpec" e "400 fixo".
4. **Peso HIGH D0-D7 contra slot MEDIUM D0-D5: consistente.** atomic-spec l.52 coloca D7 só em HIGH/CRITICAL; MEDIUM para em D5. Opções para Andraus, sem elevação silenciosa (AGENTS §4): HIGH, MEDIUM, MEDIUM com D7 seletivo. Tensão a ver (m6): a proposta rejeita CRITICAL porque a página é E1 e mantém trava Classe C/E3; CC-11 trata Classe C em BASpec de risco baixo como violação — o Plan precisará justificar pela ameaça e pela herança do slot.
5. **CONS-01: sem violação.** Decisões abertas listadas como abertas (§10, §13, research §7), inclusive WF-D03 (aberta no WORKFLOW l.112, v2.1) e CKG-STRUCT-ORIGIN-001. P-2, P-3, P-6 são propostas. Agrupamento por escola cai em "INDETERMINADA".
6. **Herança: existe nos arquivos citados.** SPEC-007 plan: INV-KFH-02 l.432-449; Interface pontos 1/2/5 l.1224/1225/1228; RULE-KFH-015 l.2058-2062; EARS 15 l.2098; BASpec-KFH-015 l.2225-2240; T21 l.2365-2371; ADV-KFH-11/25; EC-KFH-009 [E1] l.2461-2471; RULE-KFH-016 l.2064-2068. ERRATUM-REAPONT-001 N-F. SPEC-048: Interface com a SPEC-049 l.1149-1151; `reading_view_ref` l.1267/1439; INV-RET-01 l.421-433. Ressalva (m5): o texto da "compilação WikiRAG" em INV-KFH-02 (l.444-447) está no parágrafo "INTERFACE COM A SPEC-048 [PROPOSTA]"; o corpo vinculante cobre só FORMAÇÃO e F1.
7. **Backlog: coerente.** Nenhum gatilho do painel contém `spec:SPEC-049` (BL-010 l.117, BL-017 l.124, BL-029 l.136, BL-035 l.142, BL-003 l.110, BL-011 l.118). `REFERÊNCIA` é valor válido (validate_spec_sot.py l.456). BL-029 FORA é coerente (a SPEC-048 usou REFERÊNCIA para o mesmo item). BL-003/BL-011 ATIVADO (painel l.200, HANDOFF l.48) prevalece sobre nota antiga l.215. O Revisor não verifica o resultado de `backlog_triggers --abertura`.
8. **"Não é preciso errata": confirmado.** SPEC-048 l.5, 19, 117-131, 147, 176, 318, 333, 375, 507, 1149-1151, nota C-3 da SPEC-007 e N-F já apontam a página à SPEC-049. Sem re-apontamento de gatilho (slot não dividido/fundido/renumerado). A lista de linhas do research §8.3 é incompleta (m7); não muda a conclusão.

## 4. Passos 2-8
- Passo 2 (invariantes): PASS. Nada vai ao Conviction Vector; ordem neutra dos lados da contradição não usa a hierarquia analítica.
- Passo 3 (CC-01..12 preliminar): PASS com ressalva CC-11/Classe C (m6). CC-12 e RULE-ECC-05 "não incidem" (condicionado a P-2). A página não está no pipeline; nenhum WF-xx tocado.
- Passo 4 (rastreabilidade): PASS com m5 e m7.
- Passo 4-bis: Dossiê completo; validade conferida (2026-10-31 + 90 = 2027-01-29 HIGH; + 120 = 2027-02-28 MEDIUM).
- Passos 5, 5-bis, 6: não incidem no Plan; pergunta adversarial aplicada às candidatas 5, 7 e 9 (M01, m3, m4).
- Passo 7 (Enforcement): pisos E1/E3 e fail-closed declarados; faltam ENF-07 (falso-DENY da unidade E3) e justificativa CC-11 (m6).
- Passo 8 (dependências): montante baselined (SPEC-007 v2.3, SPEC-006 v1.7, SPEC-048 v1.4); sem bloqueador. Sem itens carimbados, a página sai vazia com a falta declarada (S11).
- Bloco C: EPI = m5; CAU, DEC, SEM, ONT, INQ, CTF, UNC, PRB, MET verificados sem achados.

## 5. Achados
**R1-M01 (MÉDIA, C01/C02): a referência de tempo da validade não faz parte da entrada.** ABERTURA S6 exige que "item com validade encerrada nunca apareça como atual sem sinal" (compara `valid_to` com uma data de referência). S1/S7 declaram como entrada: corte (`recorded_at`), itens e marcas até o corte, versão da regra. CC-10 define "corte = tempo de registro, ≠ validade". O relógio é proibido (S7). Logo, a data usada para decidir "encerrada" não está na entrada: ou usa o relógio (viola S7) ou usa o corte como data de validade (conflita com CC-10). "Mesma entrada ⇒ mesma página" fica indeterminada para esse sinal. Ação: declarar a data de referência da validade como parte da entrada (campo próprio ou regra de que deriva do corte) e alinhar S1, S6, S7, CC-10 e a condição 2 do §15.

**R1-m01 (MENOR, C06):** derivação da estimativa de linhas não mostrada. Escalar a base SPEC-048 (1.935 linhas, 12 BASpecs, ≈161/BASpec) a 10 BASpecs dá ≈1.610 > 1.600 (80% do teto) e exigiria confirmação de decomposição por Andraus. "70 linhas por BASpec / 400 fixo" sem origem (n=2 Plans, ambos CRITICAL); o limite superior declarado (1.500) está a 94% de 1.600. Ação: mostrar a derivação e dizer a Andraus que a extrapolação proporcional toca o limiar.

**R1-m02 (MENOR, C01), mecânico:** research.md l.201 diz "≈850 em MEDIUM"; ABERTURA §3 diz ≈880 (faixa 700-1.050). Ver FICHA-M.

**R1-m03 (MENOR, C01):** research §3.1 (l.92) diz que a página traz "o hash da entrada e da saída" (circular); §3.6 e S7 põem o hash da saída só no registro de compilação. Ação: alinhar §3.1 a §3.6/S7.

**R1-m04 (MENOR, C02):** S5 diz que omitir um lado ⇒ "não emite"; S7 lista "contradição incompleta" no relatório de saúde (página sai com aviso?). Falta fixar a granularidade (página ou bloco) e o código de recusa; cenário negativo no Plan.

**R1-m05 (MENOR, C04/EPI):** S9 e CC-08 chamam a trava de "herdada" sem etiqueta; o texto-fonte (SPEC-007 l.444-447) é parágrafo marcado [PROPOSTA] ("requisito à SPEC-048"). Research §0/§7.2 já dizem [INFERÊNCIA]. Ação: marcar S9/CC-08 como [INFERÊNCIA] ancorada em ROADMAP l.193 e C-2, citando l.444-447.

**R1-m06 (MENOR, C05):** condições ao Plan (§15) incompletas: (a) ENF-07 (falso-DENY da unidade E3); (b) justificativa CC-11 para Classe C/E3 (§1 diz E1, sem efeito sobre a verdade); (c) R-9 ("agente lê a página por porta lateral") com contenção só por requisito às Specs dos agentes [INFERÊNCIA], sem gate/detector na SPEC-049. Ação: incluir no §15 ou declarar a limitação.

**R1-m07 (MENOR, C07):** research §8.3 lista linhas da SPEC-048 "que apontam à SPEC-049"; faltam l.9, 96, 206, 507, 1731 e outras; "1267" é o `reading_view_ref` (menção a SPEC-049 em 1268); l.1439 tem `reading_view_ref` e não "SPEC-049". Ação: declarar a lista ilustrativa ou ajustar.

**R1-m08 (MENOR, C07):** ABERTURA §2 atribui ao ponto 2 da Interface "restrição de uso efetiva respeitada e exibida"; o texto literal (SPEC-007 l.1225) é "não servir unidade de fonte com rights_status efetivo INDETERMINADO; usar origem-raiz". A restrição mais restritiva exibida vem de RULE-KFH-001/P-11 (CC-08). Com P-3 opção A não há conflito; com B vale o "não servir" literal. Ação: citar o ponto 2 literalmente e separar o que vem de RULE-KFH-001/P-11.

<!-- ACHADOS-ESTRUTURADOS
ID|SEV|CATEGORIA|CAUSA|PREVENCAO
R1-M01|MEDIA|C01|Referência de tempo da validade ausente da entrada (S1) enquanto S6 exige sinal de validade encerrada e S7 proíbe relógio; CC-10 distingue corte de validade|Em abertura de Spec com reconstrução determinística, listar todas as referências temporais usadas por qualquer regra de exibição como campos da entrada
R1-m01|MENOR|C06|Estimativa de linhas sem derivação; extrapolação proporcional da base SPEC-048 (161/BASpec) chega a ~1.610 > 1.600|Declarar a derivação (base, fator) na estimativa RULE-ECC-07 e comparar com o limiar de 80%
R1-m02|MENOR|C06|research.md l.201 diz ≈850 em MEDIUM; ABERTURA §3 diz ≈880|Conferir números repetidos entre ABERTURA e research antes da entrega
R1-m03|MENOR|C01|research §3.1 diz que a página traz o hash da saída (circular); §3.6 e S7 põem no registro|Revisar o Dossiê contra o texto final da ABERTURA após qualquer mudança de desenho
R1-m04|MENOR|C02|Granularidade do não-emite (página ou bloco) e relação com relatório de saúde não definida|Em regra fail-closed declarar a unidade bloqueada e o código de recusa
R1-m05|MENOR|C04|S9 e CC-08 chamam a trava de herdada sem etiqueta; texto-fonte é parágrafo marcado PROPOSTA|Etiquetar herança que depende de texto PROPOSTA como INFERENCIA com âncora na decisão de Andraus
R1-m06|MENOR|C05|Condições ao Plan sem ENF-07, sem justificativa CC-11 para Classe C/E3 e sem mecanismo para R-9|Checar condições do Plan contra ENF-01..08 e CC-11 na abertura
R1-m07|MENOR|C07|Lista de linhas da SPEC-048 em research §8.3 incompleta e com uma linha deslocada (1267 vs 1268)|Declarar listas de busca como ilustrativas ou gerá-las por grep
R1-m08|MENOR|C07|Paráfrase do ponto 2 da Interface SPEC-007 não literal em ABERTURA §2|Citar pontos de interface por texto literal
-->

<!-- FICHA-M {"achados":[{"id":"R1-m02","sev":"MENOR","arquivo":"specs/features/SPEC-049/research.md","antigo":"≈850 em MEDIUM","novo":"≈880 em MEDIUM","condicao":"ABERTURA.md §3 (tabela, linha Total estimado) declara ≈880 (faixa 700–1.050); texto antigo ocorre uma única vez no research.md (l.201)"}]} -->

## 6. Cobertura
| Bloco | Situação |
|---|---|
| ABERTURA §1-§2 | conferido; M01, m5, m8 |
| ABERTURA §3 | conferido; m1, m2 |
| ABERTURA §4-§6 | conferido; m6 |
| ABERTURA §7-§9 | conferido; itens 7 e 8 |
| ABERTURA §10-§16 | conferido; CONS-01 sem achados |
| research §0-§3 + 14 capturas SRC | conferido; ECC-04 OK; m3 |
| research §4 + 6 REPO + _LIMITACAO | conferido; ECC-06 OK |
| research §5 (Benchmark) | linha B10 conferida em SPEC-007/research.md l.163 (ordem de grandeza); veracidade não verificável |
| research §6-§9 | conferido |

## 7. Não pude verificar
Resultado de qualquer gate (`revisor_gate`, `backlog_triggers`, `check_repo_research`, `check_refs`, `check_doc_sync`, `check_invariants`, `check_dimensionamento`, `build_map`) · SHA256 do alvo e do research.md (sem Bash) · veracidade das páginas web e números dos repositórios · adulteração de `sources/` · estado git/commit · se a SPEC-048 tem exatamente 12 BASpecs · interpelação formal ao Especificador.

## 8. Encaminhamento
Devolver ao Especificador (classe O) para M01 e os Menores m1 e m3 a m8. O Orquestrador aplica a ficha m2 por `aplicar_ficha_m.py`. Depois, rodada 2 em delta com amostra anti-leniência. As perguntas P-1 a P-6 e C-1 a C-3 seguem a Andraus só após CONFORME. Nada decidido por Andraus.
