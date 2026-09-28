Proposta de seleção e acoplamento de skills de caching ao SOT
1. Objetivo
Selecionar, entre as skills e ferramentas identificadas no benchmark, quais atendem aos requisitos do SOT — Sistema Operacional de Trading — de forma exata, aproximada ou insuficiente, considerando os quatro critérios:
Eficácia: capacidade de produzir o resultado correto, preservando os invariantes comportamentais do SOT.
Efetividade: contribuição real para os objetivos do SOT, incluindo confiabilidade das análises e decisões.
Eficiência: capacidade de reduzir latência, consumo de tokens e esforço operacional.
Economicidade: benefício líquido em relação ao custo de implementação, operação, manutenção e risco.

Nota de conformidade (2026-09-28): ordem corrigida para a hierarquia canônica do SOT — Eficácia > Efetividade > Eficiência > Economicidade (AGENTS.md §6 item 11; governance/RULES.md:239; CEE-001). A versão original desta proposta listava Eficiência antes de Efetividade (achado ACHADO-M1 do parecer de auditoria do Revisor SOT, 2026-09-28, ref. BL-024).
A proposta considera o SOT como um sistema multiagente especializado em análise de mercado, com agentes como Elliott, SMC e ICT, uso de conhecimento especializado, evidências, hipóteses e validação de decisões.
O ponto central é que o SOT não precisa simplesmente de uma skill que aumente o cache hit rate. Precisa de uma capacidade que identifique o que pode ser reutilizado, sob quais condições, com qual risco e com qual benefício demonstrável.

1.1. Agentes contemplados pela proposta
O caching não se destina apenas aos agentes de análise de mercado citados acima. A proposta cobre duas famílias de agentes, com regimes de risco distintos:
A. Agentes cognitivos internos do domínio (runtime do SOT): estrutural, institucional, operacional, manager e de risco. Nestes, o caching manipula evidências, hipóteses e observações regidas por CHM-001/CEM-001 — aplica-se integralmente o risco descrito na seção 6 (item 5 do parecer de auditoria: cache stale servindo resultado de uma hipótese cujo estado já mudou) e a exigência de precondição verificável de estado antes de qualquer HIT.
B. Agentes que constroem e auditam o próprio harness (spec-time): Especificador e Revisor. Nestes, o caching é majoritariamente de prompt/contexto (instruções, arquivos-fonte lidos repetidamente, ex. ROADMAP.md, atomic-spec.md, governance/) durante a produção e auditoria de Specs — não manipula hipóteses de mercado, mas ainda está sujeito a ENF-03 (gate determinístico) e a "sem baseline informal": um cache não pode fazer o Especificador ou o Revisor tratarem uma versão desatualizada de uma Spec, do CATALOGO-OFICIAL.md ou de uma decisão aberta (seção 7 do AGENTS.md) como atual.
A matriz de acoplamento (seção 4) e os critérios de aceitação dos 4Es (seção 6) devem ser avaliados separadamente para A e para B, pois o custo, o risco e o mecanismo de invalidação de cada família são diferentes.

Decisão de faseamento (Andraus, 2026-09-28): a abertura formal de Spec cobre, nesta rodada, SOMENTE o Grupo B (Especificador e Revisor, caching de spec-time). O Grupo A (agentes cognitivos internos — estrutural, institucional, operacional, manager, risco) fica deliberadamente adiado para uma fase posterior — não por descuido, mas porque o Grupo A depende de precondições que ainda não existem como Spec (agentes analíticos SPEC-010..014) e carrega o risco mais sério identificado pelo Revisor (ACHADO-M2 — precondição de estado CHM-001 antes de cache HIT). O Grupo B, por lidar com staleness de documentos-fonte do próprio repositório (não com hipóteses de mercado), é tratável de forma independente e com risco menor. BL-024 (backlog/RMR-001) reflete esse faseamento.
2. Escopo da decisão
A seleção deve separar três funções que não são equivalentes:
A. Auditoria de maturidade
Examina o sistema existente, identifica mecanismos de cache, encontra problemas e produz diagnóstico fundamentado em evidências.
B. Implementação e correção
Modifica configurações, prompts, código ou políticas de caching, dentro das permissões autorizadas.
C. Benchmark comportamental e econômico
Verifica se o caching preserva a correção do sistema e se entrega benefícios mensuráveis em relação ao baseline.
A análise recomenda não concentrar essas três funções em uma única skill sem separação de responsabilidades. Uma auditoria pode identificar a oportunidade, mas não deve presumir que a alteração é segura ou economicamente vantajosa.
3. Benchmark comparativo por capacidade
A avaliação abaixo é uma proposta de acoplamento ao SOT, não uma certificação de que os repositórios já atendem integralmente aos seus requisitos.
As classificações significam:
Exata: atende diretamente à capacidade técnica pretendida.
Aproximada: atende parcialmente, exigindo extensão ou integração.
Insuficiente: não demonstra a capacidade necessária para aquela função.
A validar: depende de testes no ambiente real do SOT.
3.1. Skills e ferramentas avaliadas
1. audit-prompt-caching
Auditoria técnica
Repositório: sernote
GitHub — audit-prompt-caching
Capacidade: auditar prompt/prefix cache, telemetria, roteamento, estabilidade de ferramentas, KV cache e economia.
Acoplamento ao SOT
Base documental: auditoria estática, scripts, fixtures e testes; não captura tráfego real automaticamente.

sernote/audit-prompt-caching · GitHub
2. cache-audit
Auditoria Claude Code
Repositório: ussumant
GitHub — cache-audit
Capacidade: revisar seis regras de prompt caching no Claude Code e entregar relatório com problemas e correções.
Base documental: regras de ordenação, injeção de mensagens, estabilidade de ferramentas, troca de modelos, conteúdo dinâmico e segurança de fork.

GitHub
3. prompt-cache-skills
Implementação
Repositório: OnlyTerp
GitHub — prompt-cache-skills
Capacidade: aplicar correções específicas para harnesses e provedores, com etapas de verificação.
Base documental: skills atômicas com alvo, sintoma, correção e verificação. A aplicação deve confirmar os arquivos e o harness de destino antes de alterar o sistema.

GitHub
+1
4. CacheEval
Avaliação de correção
Repositório: BudEcosystem
GitHub — CacheEval
Capacidade: avaliar se o cache decide corretamente entre HIT e MISS, incluindo falsos hits em consultas semelhantes, mas não equivalentes.
Base documental: benchmark de pares de equivalência em dez domínios, com False-Hit Rate como métrica central.

GitHub
5. semantic-cache-bench
Benchmark de desempenho
Repositório: Akshitha024
GitHub — semantic-cache-bench
Capacidade: comparar ausência de cache, LRU e cache semântico em hit rate, custo, latência e evicções.
Base documental: benchmark publicado com 12 mil consultas. Os resultados são específicos à carga e à configuração do projeto.

GitHub
3.2. Capacidade nativa do provedor
Além das skills de repositório, o próprio provedor pode oferecer recursos de caching e diagnóstico.
A documentação da OpenAI descreve prompt caching automático para modelos compatíveis, métricas de tokens reutilizados e, para GPT-5.6 e posteriores, opções de controle de cache e diagnóstico de misses.

OpenAI API
+1
Isso é relevante porque:
O mecanismo de cache pode já estar ativo sem implementação adicional.
A skill deve primeiro diagnosticar o comportamento real do provedor.
A aplicação de uma correção genérica pode ser desnecessária ou incompatível com o modelo.
O benchmark deve usar métricas reais de consumo e latência, não apenas estimativas estáticas.
A capacidade nativa do provedor não substitui a skill de auditoria. Ela fornece o mecanismo e parte da telemetria; a skill interpreta os dados e recomenda ações.
4. Matriz de acoplamento ao SOT
A matriz abaixo avalia a adequação das ferramentas às necessidades específicas do sistema.
|
Necessidade do SOT
|
Ferramenta candidata
|
Aderência
|
| --- | --- | --- |
|
Auditar prompt caching dos agentes
|
audit-prompt-caching
|
Exata
|
|
Auditar regras específicas do Claude Code
|
cache-audit
|
Exata
|
|
Corrigir caching em harnesses suportados
|
prompt-cache-skills
|
Exata, se houver skill compatível
|
|
Avaliar falsos hits de cache semântico
|
CacheEval
|
Exata para o benchmark
|
|
Comparar latência, hit rate e custo
|
semantic-cache-bench
|
Exata para o cenário experimental
|
|
Verificar validade de hipóteses de mercado
|
Nenhuma das skills isoladamente
|
Insuficiente
|
|
Verificar validade temporal de dados de mercado
|
Harness específico do SOT
|
Insuficiente
|
|
Preservar invariantes de decisão
|
Harness específico do SOT
|
Insuficiente
|
|
Demonstrar benefício econômico no SOT
|
Benchmark integrado
|
A validar
|
A conclusão dessa matriz é que nenhuma das ferramentas analisadas cobre, isoladamente, todo o ciclo de maturidade comportamental do SOT.
O acoplamento exige uma camada própria de critérios de trading, sem reimplementar aquilo que as ferramentas já fazem bem.
5. Proposta de arquitetura recomendada
5.1. Separação de responsabilidades
SOT — Harness comportamental
Define invariantes, validade temporal, regras de decisão e condições de reutilização.
Skill de maturidade de caching
Coordena diagnóstico, avaliação, benchmark e recomendação.
Auditoria técnica
Validação comportamental
Benchmark econômico
Ferramentas especializadas
audit-prompt-caching · cache-audit · prompt-cache-skills · CacheEval · semantic-cache-bench
A skill de maturidade não precisa conter todos os mecanismos. Ela deve selecionar e orquestrar as ferramentas conforme o tipo de cache, o risco e a missão.
5.2. Acoplamento ao ciclo PDCA
|
Etapa
|
Responsabilidade
|
Ferramenta
|
| --- | --- | --- |
|
Plan
|
Diagnosticar e definir critérios
|
audit-prompt-caching
|
|
Do
|
Aplicar correções aprovadas
|
prompt-cache-skills
|
|
Check
|
Avaliar correção e desempenho
|
CacheEval + semantic-cache-bench
|
|
Act
|
Recomendar manter, ajustar ou reverter
|
Skill de maturidade do SOT
|
O cache-audit pode ser usado como verificação complementar quando o alvo for especificamente o Claude Code.
6. Critérios de aceitação dos 4Es
A recomendação é que o SOT não aprove uma política de caching apenas por atingir um nível de economia.
Eficácia
A política deve demonstrar que:
Não reutiliza resultados incompatíveis com a consulta atual.
Respeita contexto, temporalidade e identidade das entidades.
Preserva os invariantes comportamentais do agente.
Não transforma hipóteses anteriores em fatos atuais.
Efetividade
Deve demonstrar:
Preservação da qualidade da análise.
Cumprimento dos objetivos do agente.
Ausência de degradação relevante nas decisões ou recomendações.
Eficiência
Deve demonstrar:
Redução mensurável de latência ou consumo.
Ausência de sobrecarga excessiva de validação.
Melhora em métricas relevantes para o fluxo real do agente.
Economicidade
Deve demonstrar:
Economia líquida, não apenas redução de tokens.
Custos de implementação e manutenção aceitáveis.
Risco residual compatível com a missão.
Benefício superior ao custo de manter o mecanismo.
Critério de bloqueio: qualquer falha crítica de correção, segurança ou validade temporal impede a aprovação, mesmo que os demais indicadores sejam favoráveis.
7. Decisão proposta
Proposta para análise do SOT
Adotar uma arquitetura composta
Não selecionar uma única skill como solução completa. Adotar uma skill de maturidade própria, integrando ferramentas especializadas conforme a necessidade.
Núcleo de auditoria: audit-prompt-caching
Implementação: prompt-cache-skills, somente quando houver correção aplicável ao harness.
Benchmark de correção: CacheEval, adaptado aos riscos de reutilização do SOT.
Benchmark de desempenho: semantic-cache-bench, adaptado à carga real.
Complemento opcional: cache-audit para auditoria específica do Claude Code.
Essa composição atende de forma aproximada ao conjunto dos 4Es e oferece uma base técnica para construir uma capacidade mais completa. A aderência exata aos critérios do SOT só poderá ser confirmada após testes com seus prompts, agentes, dados e fluxos reais.
8. Próxima etapa recomendada
Executar uma análise de acoplamento controlada, sem modificar o SOT:
Inventariar os tipos de cache existentes e os pontos de chamada dos agentes.
Aplicar a auditoria técnica em modo somente leitura.
Identificar oportunidades de cache por classe de conhecimento e validade.
Construir casos de teste de equivalência e invalidação específicos do trading.
Verificar, para cada ferramenta candidata, a necessidade de usá-la em sentido estrito (dependência externa invocada como skill/pacote, mantendo atualização e versionamento pelo repositório de origem) ou de copiar/adaptar sua lógica para replicar internamente no projeto (fork interno mantido pelo SOT, sem dependência externa). A decisão deve registrar o motivo (ex.: estabilidade da API externa, necessidade de customização para invariantes do SOT como CHM-001, risco de descontinuação do repositório de origem) e o custo de manutenção resultante, como insumo do critério de Economicidade (seção 6).
Comparar baseline e política candidata nos 4Es.
Submeter os resultados à homologação humana antes de qualquer implementação.
O entregável dessa etapa deve ser uma matriz de decisão por mecanismo de cache, com evidências, riscos, custo estimado e recomendação de acoplamento.
Síntese: a ferramenta de auditoria identifica onde melhorar; a ferramenta de implementação corrige; o benchmark verifica se a mudança é segura e vantajosa. O SOT precisa governar a decisão de reutilização e a aceitação final.

9. Classificação preliminar de fontes (pré-Dossiê, RULE-ECC-01/02)

Nota: esta é uma classificação preliminar para instruir o item de backlog BL-024, NÃO o Dossiê de Pesquisa formal exigido por RULE-ECC-02 (governance/RULES.md:434) — este só será produzido, com captura verbatim (RULE-ECC-04, governance/RULES.md:450-461) em `specs/features/SPEC-0NN/sources/`, quando uma Spec de caching for formalmente aberta no ROADMAP. Hoje não existe slot SPEC-0NN de caching, portanto qualquer avaliação abaixo é [PROPOSTA]/[INFERÊNCIA] e não é baseline (AGENTS.md §6 item 10; "sem baseline informal"). O Dossiê formal DEVE ser produzido pelo próprio Especificador (não delegável ao agente raiz — RULE-ECC-02).

Base de evidência: as caracterizações abaixo derivam EXCLUSIVAMENTE do que já está descrito nas seções 3.1 e 4 deste documento. Nenhum detalhe técnico de repositório foi acrescentado por acesso à web nesta preparação. Onde a caracterização exigiria informação não contida no documento, marca-se "[a validar em Dossiê formal]".

9.1. Vocabulário (RULE-ECC-02)
Tipo de fonte: Padrão / Prática / Benchmark / Evidência / Experimento / Opinião.
Recomendação preliminar: adotar / adaptar / rejeitar / adiar.
Ordem dos 4Es aplicada como critério (AGENTS.md §6 item 11; governance/RULES.md:239): Eficácia > Efetividade > Eficiência > Economicidade — Economicidade nunca sobrepõe Eficácia.

9.2. Classificação por ferramenta

1. audit-prompt-caching (sernote) [EXTERNO]
- Tipo de fonte: Prática (ferramenta de auditoria estática, com scripts, fixtures e testes; seção 3.1).
- Recomendação preliminar: adaptar. [PROPOSTA]
- Justificativa (4Es): serve à Eficácia como núcleo de diagnóstico (identifica onde há reutilização e telemetria antes de qualquer HIT), mas o documento registra que é auditoria estática e "não captura tráfego real automaticamente" — logo precisa ser adaptada/estendida ao runtime do SOT (famílias A e B da seção 1.1) para ter Efetividade. Não é adoção direta.

2. cache-audit (ussumant) [EXTERNO]
- Tipo de fonte: Prática (revisão de seis regras de prompt caching específicas do Claude Code, com relatório; seção 3.1).
- Recomendação preliminar: adiar. [PROPOSTA]
- Justificativa (4Es): o próprio documento a posiciona como "complemento opcional" e "verificação complementar quando o alvo for especificamente o Claude Code" (seções 5.2 e 7). Sua contribuição à Eficácia/Efetividade é condicionada a esse alvo restrito, então seu acoplamento pode aguardar a definição de escopo da Spec de caching.

3. prompt-cache-skills (OnlyTerp) [EXTERNO]
- Tipo de fonte: Prática (skills atômicas de implementação/correção, com alvo, sintoma, correção e verificação; seção 3.1).
- Recomendação preliminar: adaptar. [PROPOSTA]
- Justificativa (4Es): atua na fase "Do" (aplicar correções — seção 5.2), o que toca diretamente a Eficácia e os invariantes comportamentais; o documento condiciona seu uso a "somente quando houver correção aplicável ao harness" e exige confirmar arquivos/harness de destino antes de alterar. É adaptação sob salvaguarda, não adoção genérica. Grau de compatibilidade com o harness do SOT [a validar em Dossiê formal].

4. CacheEval (BudEcosystem) [EXTERNO]
- Tipo de fonte: Benchmark (pares de equivalência em dez domínios, métrica central False-Hit Rate; seção 3.1).
- Recomendação preliminar: adaptar. [PROPOSTA]
- Justificativa (4Es): mede diretamente a Eficácia — falsos hits em consultas semelhantes mas não equivalentes, exatamente o risco descrito na seção 6 (cache stale servindo resultado de hipótese cujo estado mudou). O documento pede que seja "adaptado aos riscos de reutilização do SOT" (seção 7), incluindo temporalidade e CHM-001/CEM-001. Alto valor, mas requer adaptação do conjunto de equivalência ao trading.

5. semantic-cache-bench (Akshitha024) [EXTERNO]
- Tipo de fonte: Benchmark (comparação sem-cache / LRU / cache semântico em hit rate, custo, latência e evicções; benchmark publicado com 12 mil consultas; seção 3.1).
- Recomendação preliminar: adaptar. [PROPOSTA]
- Justificativa (4Es): endereça sobretudo Eficiência e Economicidade (latência, custo, hit rate). O documento adverte que "os resultados são específicos à carga e à configuração do projeto" e pede adaptação "à carga real" (seção 7) — portanto seus números não transferem sem re-execução no ambiente SOT, e nunca podem aprovar uma política sozinhos (Eficácia/Efetividade precedem — seção 6, critério de bloqueio).

9.3. Observações de fronteira
- Nenhuma das cinco ferramentas, isoladamente, cobre validade de hipóteses de mercado, validade temporal ou preservação de invariantes de decisão (matriz da seção 4: "Insuficiente") — essa camada é do harness próprio do SOT e não é objeto de adoção externa.
- A capacidade nativa do provedor (seção 3.2) é [EXTERNO] e não classificada como ferramenta candidata aqui; permanece [a validar em Dossiê formal] quanto a diagnóstico do comportamento real de cache.
- Conversão desta nota preliminar em decisão vinculante depende de: (i) abertura formal de uma Spec de caching no ROADMAP; (ii) Dossiê de Pesquisa RULE-ECC-01/02 pelo Especificador; (iii) captura verbatim RULE-ECC-04; (iv) homologação de Andraus. Até lá: [DECISÃO NECESSÁRIA] quanto a adotar/adaptar em definitivo.