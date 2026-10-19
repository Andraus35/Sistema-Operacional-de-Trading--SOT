# Conflict Map — SOT (Sistema Operacional de Trading)
<!-- Fonte: ENGENHARIA GERAL.pdf Doc05 + Doc07 + ARIA_Plano_Mestre.md | Versão 1.1 -->
<!-- Correções homologadas por Andraus 2026-09-14: Q-004 (R:R 1:3; RULE-ICT-002 corrigida), Q-002 (limiares de convicção = Fase Piloto, recalibráveis). -->

<!-- Emenda 2026-09-20 (DHR-PAP-001-C-Hyg1 / RCH-001 Ciclo #1): seção "Inversões contextuais (GPR-001 §3.6)" HOMOLOGADA por Andraus. Fechou BL-007 e FLAG #5 de BL-005. -->

<!-- Emenda 2026-09-20 (DHR-EUA-E04): registrada colisão de rótulos do HCH-001 (referência externa não-normativa). NÃO adotar do HCH-001: H0–H4; "3Es+Economicidade" (conflita com 4Es CEE-001 §12); L0–L4 (colide com Quality Gates L1–L4 do atomic-spec §7 e com harness-score); M0–M7 (colide com Marcos). Aproveitada apenas a mecânica de herança-por-delta via emenda EUA-E04. [K-MAN-01] -->

<!-- Emenda 2026-09-20 (DHR-MAN-001): registrada colisão de rótulos do CMHP-001 (referência externa não-normativa). NÃO adotar do CMHP-001: L0–L6 (colide com Quality Gates L1–L4 / harness-score L0–L4 / maturidade GPR-001 §11 L0–L5); I-01..I-12 (colide com INV-01..10 / PC-xx / PB-xx / HCH-INV). Aproveitada apenas a mecânica de convergência horizontal via MAN-001. Convergências e conflitos horizontais entre Master Contracts passam a ser governados pelo MAN-001. [K-MAN-02] -->

<!-- Emenda 2026-09-20 (DHR-EUA-E05): registrada colisão de rótulos do MEG-001 (referência externa não-normativa). NÃO adotar do MEG-001: maturidade "Nível 0–6" (colide com Quality Gates L1–L4 / harness-score L0–L4 / maturidade GPR-001 §11 L0–L5); unidade EPI-ID (§100, já coberta por BASpec/Enforcement Contract). Aproveitada apenas a mecânica de verificação epistêmica via EUA-E05 (Epistemic Check no atomic-spec §11: anti-conversão RULE-EPI, estados de gate incl. INDETERMINADO, INV-EPI). Nó N8 (Epistêmico) registrado no MAN-001. [K-MAN-04] -->

<!-- Emenda 2026-09-20 (DHR-EUA-E06): registrado o MSC-001 / Camada Semântica (referência externa não-normativa). NÃO adotar por DUPLICAÇÃO: §53 Não-colapsação (= RULE-EPI-01..03, EUA-E05) — a semântica REFERENCIA RULE-EPI, não recria. Aproveitada só a mecânica de terminologia concorrente por escola + transparência semântica via EUA-E06 (RULE-SEM-01..04, CC-10, registro no GLOSSARIO com FONTE obrigatória). Nó N9 (Semântico) registrado no MAN-001. Interpretações concorrentes de termo por escola (Elliott/SMC/ICT) passam a ser registradas no GLOSSARIO com fonte; sentido decisivo exige declaração de acepção. [K-MAN-05] -->

<!-- Emenda 2026-09-20 (DHR-EUA-E07): registrado o MOC-001 / Camada Ontológica (referência externa não-normativa). NÃO adotar por DUPLICAÇÃO: nome≠entidade (§3/§24 = RULE-SEM/RULE-EPI); relação≠causa (§13–14 = RULE-EPI-02); catálogo genérico de tipos (§5) e maturidade ontológica (§57) = CEM/CHM/SAS. Aproveitada só a distinção observacional/teórico + autoexpansão governada via EUA-E07 (RULE-ONT-01/02, verificada sob CC-09). Construção teórica (order block, liquidez, "pressão compradora") NÃO é promovida a real sem tratamento epistêmico (RULE-EPI). Nó N10 (Ontológico) registrado no MAN-001; substância nos Modelos Canônicos (CCM/CDM/CNM). [K-MAN-06] -->

<!-- Emenda 2026-09-20 (DHR-EUA-E08): registrado o MIQG-001 / Camada de Inquérito (referência externa não-normativa). CONFLITO DE ORDEM: o §87 do MIQG usa "3Es" na ordem Eficácia→Eficiência→Efetividade — REJEITADO; prevalece o 4Es homologado Eficácia→Efetividade→Eficiência→Economicidade (CEE-001 §12). NÃO adotar o catálogo operacional §62–66 (INV-INQ/INQ-S/GATE-INQ) — são sensores de runtime, pertencem ao harness-eval/GEH, não a emenda de spec. Aproveitadas só 3 disciplinas via EUA-E08 (RULE-INQ-01 questão→método; RULE-INQ-02 evidência discriminante — estende PCO-02; RULE-INQ-03 critério de encerramento → INDETERMINADO). Nó N11 (Inquérito) registrado no MAN-001; corrigida a lista §68 que omitia "Inquérito". [K-MAN-07] -->

<!-- Emenda 2026-09-20 (DHR-EUA-E09): registrado o MCC-001 / Camada Causal (referência externa não-normativa). NÃO adotar por DUPLICAÇÃO: §53 Não-confusão (correlação/precedência/previsão/padrão → causa = RULE-EPI-02 / RULE-ONT / AP-02 / RULE-004). DIFERIDOS: observar-vs-intervir e intervenção hipotética (§28/§58) → nó futuro Contrafactuais + specs de backtest/CCM; vocabulário estatístico mediação/moderação/confounder (§17) → CCM-001. Aproveitadas 3 disciplinas via EUA-E09 (RULE-CAU-01 mecanismo obrigatório — estende RULE-EPI-02; RULE-CAU-02 regime de validade — ancora SES-001 §33 e GPR §3.6; RULE-CAU-03 guard pós-hoc — estende AP-10). Asserção causal de SMC/ICT (MCC §43: "liquidez causou reversão", "rompimento causou continuação") = hipótese com mecanismo, não fato. Nó N12 (Causal) no MAN-001. [K-MAN-08] -->

<!-- Emenda 2026-09-20 (DHR-EUA-E10): registrado o MCF-001 / Camada Contrafactual (referência externa não-normativa). NÃO adotar por DUPLICAÇÃO: §20/§57 anti-hindsight (= RULE-CAU-03/AP-10); contrafactual≠fato (= RULE-EPI). DIFERIDOS: qualificação por incerteza/probabilidade (§31/§32) → nós futuros Incerteza/Probabilística; propagação/árvores/simulação (§16–18) → specs de backtest. Aproveitadas 3 disciplinas via EUA-E10 (RULE-CTF-01 baseline+intervenção mínima+anti-hindsight — estende RULE-CAU-03; RULE-CTF-02 condicional+gradação necessária/plausível/possível/especulativa; RULE-CTF-03 contrafactual de invalidação ligado ao invalidador INV-02/Elliott-ICT). Recebe o diferimento da EUA-E09 (§28/§58 observar-vs-intervir). Nó N13 (Contrafactual) no MAN-001. [K-MAN-09] -->

<!-- Emenda 2026-09-20 (DHR-EUA-E11): registrado o MUN-001 / Camada de Incerteza (referência externa não-normativa). NÃO adotar por DUPLICAÇÃO: preservação da incerteza/abstenção/hipóteses concorrentes (= PB-10/INDETERMINADO/PCO); falsa precisão (= RULE-EPI). FRONTEIRA J-001: a emenda NÃO define fórmula/pesos/limiares do Conviction Vector (INV-03/J-001 permanecem ABERTOS). DIFERIDOS: calibração/sensibilidade/incerteza crítica (§10/§36/§37/§38) → Conviction Engine/CCM-001; quantificação probabilística (§31/§58) → nó futuro Probabilística. Aproveitadas 3 disciplinas via EUA-E11 (RULE-UNC-01 localizar/tipificar — estende PB-10; RULE-UNC-02 não-contaminação; RULE-UNC-03 incerteza≠probabilidade). Nó N14 (Incerteza) no MAN-001. [K-MAN-10] -->

<!-- Emenda 2026-09-20 (DHR-EUA-E12): registrado o MPB-001 / Camada Probabilística (referência externa não-normativa). NÃO adotar por DUPLICAÇÃO: possibilidade/probabilidade/certeza/incerteza (= RULE-UNC-03/RULE-EPI/PB-10); falsa precisão (= RULE-EPI). FRONTEIRA J-001 (a mais sensível): a emenda NÃO define fórmula/pesos/limiares/CALIBRAÇÃO/DISTRIBUIÇÃO do Conviction Vector — RULE-PRB-01 exclui explicitamente o Conviction Vector, cujo contrato é o CCM-001 (INV-03/J-001 ABERTOS). DIFERIDOS ao CCM-001/Conviction Engine: calibração (§43/§124), valor esperado/risco/cauda (§25/§52/§53), priors/bayes (§60–63), distribuições (§19/§24); probabilidade≠decisão (§50/§133) → nó Decisional; backtest (§83) → specs. Aproveitadas 2 disciplinas via EUA-E12 (RULE-PRB-01 evento bem-formado evento+condição+horizonte; RULE-PRB-02 não quantificar sem base → ordenação qualitativa/INDETERMINADO). Nó N15 (Probabilística) no MAN-001. [K-MAN-11] -->

<!-- Emenda 2026-09-21 (DHR-EUA-E13): registrado o MDC-001 / Camada Decisional (referência externa não-normativa). NÃO adotar por DUPLICAÇÃO: decisão≠previsão (§27 = RULE-UNC/PB-10/RULE-EPI); decisão≠causalidade (§28 = RULE-CAU); contrafactuais/cenários decisórios (§40/§41 = RULE-CTF); decisão sob incerteza/risco (§18/§19 = RULE-UNC/PB-10/INDETERMINADO); invalidação (§50 = RULE-CTF-03/INV-02); valor/suficiência/parada de informação (§14–17 = RULE-INQ); explicabilidade/rastreabilidade (§55–57 = TRACE-06/RULE-010/PB-05..07); proporcionalidade cognitiva (§44/§45/§71/§85 = GES/D0–D9/4Es/CC-05); possibilidade/probabilidade (§5 = RULE-PRB). FRONTEIRA J-001/CDM-001: a emenda NÃO define função de utilidade/pesos/critérios/ponderação multicritério/robustez/opcionalidade do modelo de decisão — isso é CDM-001 (pendente) + Synthesis Agent (INV-03/J-001 ABERTOS). DIFERIDOS: multicritério (§30–32), utilidade/pesos (§74), robustez/sensibilidade (§20/§21), risco multidimensional (§46), sequencial/opcionalidade (§67/§68/§69) → CDM-001/Synthesis; vieses/metacognição (§58/§59/§60) → nó Metacognição (sem doc); agentes adaptativos/adversarialidade/2ª ordem/externalidades (§36/§37/§38/§39) → Modelos Canônicos + specs de domínio. Aproveitadas 3 disciplinas via EUA-E13 (RULE-DEC-01 decisão≠execução + autoridade — REFORÇA INV-05/P14/B-001, não redefine; RULE-DEC-02 decisão condicional se X→A / ¬X→B / desconhecido→INDETERMINADO; RULE-DEC-03 qualidade do processo ≠ resultado, anti-hindsight — estende RULE-CAU-03/AP-10). Nó N16 (Decisional) no MAN-001 — fecha as camadas §68 com documento (resta só Metacognição). [K-MAN-12] -->

<!-- Emenda 2026-09-21 (DHR-EUA-E14): registrado o MC-001 / Camada Metacognição (referência externa não-normativa). Camada TRANSVERSAL / de 2ª ordem — monitora o funcionamento de N8–N16, não introduz domínio novo (MC-001 §31/§91/§93). NÃO adotar por DUPLICAÇÃO (13): §10/§41 processo≠resultado (=RULE-DEC-03); §45/46/47 hindsight/overfitting (=RULE-CTF/CAU); §27/37 causa≠narrativa (=RULE-CAU-01); §28/56/73 contrafactual-autocrítica/invalidação (=RULE-CTF/INV-02); §29 incerteza (=RULE-UNC); §22/26/25 semântica/ontologia (=RULE-SEM/ONT); §16/58/70 dependência de evidências (=RULE-004); §38/96 valor da informação/parada (=RULE-INQ); §35/77/95 proporcionalidade/recursão (=GES/D0–D9/4Es); §52/53/85 concorrentes/insuficiência (=RULE-007/PCO/INDETERMINADO); §109/79 transparência/invariantes (=TRACE-06/INV-EPI); §30 não-substitui-decisão (=fronteira N16); §64 falsa precisão (=RULE-PRB/EPI). FRONTEIRA J-001/CCM-001: a emenda NÃO define calibração/confiança quantitativa — §65 calibração diferida ao CCM-001 (INV-03/J-001 ABERTOS). DIFERIDOS: deriva/métricas/avaliação adversarial (§74/§99/§100) → harness-eval/GEH; especialização Trading (§66/§102) → SES-001. Aproveitadas 3 disciplinas via EUA-E14 (RULE-MET-01 honestidade/não-fabricação — estende RULE-SY-005/EPI/004; RULE-MET-02 abstenção produtiva/anti-censura — INDETERMINADO deve localizar; RULE-MET-03 autonegação/revisibilidade — estende RULE-007/PCO/CTF-03). Nó N17 (Metacognição, transversal/2ª ordem) no MAN-001 — FECHA todo o §68 (fim do ciclo de camadas). Sensor metacognitivo (dependência/deriva) enxertado no Hygiene RCH-001 (Q5). [K-MAN-13] -->

<!-- Emenda 2026-09-21 (DHR-MC-RAG-001): admitido ao backlog (BL-010, Em espera) o MC-RAG-001 / Master Contract da Camada RAG, classificado como referência externa não-normativa (empresta requisitos a SPEC-007 e vizinhas; NÃO é baseline nem nó). COLISÕES DE RÓTULO registradas: (a) Quality Gates G0–G8 (§13) colidem com Quality Gates L1–L4 (atomic-spec §7) / harness-score L0–L4 — namespace G REJEITADO como gate global (tratar como gates LOCAIS da camada RAG, mesmo padrão K-MAN-01/02); (b) ordem dos 4Es (§1: Eficácia→Eficiência→Efetividade→Economicidade) INVERTIDA vs. ordem canônica CEE-001 §12 (Eficácia→Efetividade→Eficiência→Economicidade) — REJEITADA, prevalece a canônica (mesmo caso K-MAN-07/MIQG); (c) namespaces I-RAG-01..10 (§12) e RAG-P01..P14 (§3) — tratar como invariantes/princípios LOCAIS que REFERENCIAM os canônicos (INV/PC/PB/PCO), não novos globais; (d) RAG-SPEC-018 (Evidence Independence) ancora em RULE-004 + RULE-MET-01, não redefine. FRONTEIRAS CONFORMES (Revisor): J-001 (campo confidence do RAG ≠ Conviction Vector, INV-03 aberto), CC-02 (Evidence Packet/Knowledge Candidate PROJETAM CEM-001/CHM-001, não redefinem), INV-05 (RAG não decide/executa — §2.2/§23), INV-09 (RAG-P13 feedback≠autorização). Tratamentos R-01..R-08 aplicáveis na ATIVAÇÃO (redação de SPEC-007). [K-MAN-14] -->

<!-- Emenda 2026-09-21 (DHR-MC-EXP-001): admitido ao backlog (BL-011, Em espera) o MC-EXP-001 / Master Contract da Camada de Experiência e Memória, classificado como referência externa não-normativa (empresta requisitos a SPEC-004/006/009/018 + CEM/CHM/CCM; NÃO é baseline nem nó). INCONSISTÊNCIA INTERNA normalizada: doc declara "Status: BASELINE" (l.7) e "BASELINE PROPOSTA" (l.1518) — sem efeito normativo (INV-09/PC-08); entra como PROPOSTA/ref. externa. COLISÕES DE RÓTULO: (a) Quality Gates G0–G8 (§52) colidem com Quality Gates L1–L4 / harness-score L0–L4 — namespace G REJEITADO como gate global (gates LOCAIS da camada, padrão K-MAN-14); (b) namespaces I-EXP-01..12 (§51) e EXP-P01..P14 (§5) — tratar como invariantes/princípios LOCAIS que ANCORAM nos canônicos: I-EXP-01/07 (imutabilidade)=RULE-BB-004/INV-07; I-EXP-08 (independência)=RULE-004/RULE-MET-01; I-EXP-09 (memória sem autoridade decisional)=INV-05; EXP-P03 (experiência≠conhecimento)=RULE-EPI; EXP-P04 (resultado≠causa)=RULE-CAU-03; (c) Working Memory §7.6 pertence ao Blackboard/SPEC-004, não a esta camada (memória permanente); (d) dup. EXP-SPEC-021 (Experience Independence) ↔ RAG-SPEC-018 (Evidence Independence, BL-010) — ambos ancoram RULE-004, reconciliar na ativação. FRONTEIRAS CONFORMES (Revisor): CC-02 (Experience Record/Packet PROJETAM CEM-001/CHM-001, não redefinem), J-001 (confidence/performance_metrics = métricas históricas ≠ Conviction Vector 8D, INV-03 aberto), INV-05 (I-EXP-09), INV-07/RULE-BB-004 (imutabilidade histórica REFORÇADA). Fronteira RAG↔Experiência coerente (MC-EXP §35: RAG=recuperação, Experience=conteúdo). Tratamentos R-01..R-07 + X-04 aplicáveis na ATIVAÇÃO (SPEC-006/009). [K-MAN-15] -->

<!-- Emenda 2026-09-21 (DHR-MC-COG-001): admitido ao backlog (BL-012, Em espera) o MC-COG-001 / Master Contract da Camada de Cognição, classificado como referência externa não-normativa (empacota o NÚCLEO COGNITIVO já normativo — N8–N17 + agentes + Synthesis + Conviction; NÃO é baseline nem nó). ~80% do conteúdo já é FATO NORMATIVO (RULE-EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET). Status "Baseline" (l.6) sem efeito (INV-09). COLISÕES: (a) ACHADO CENTRAL — modelo de estados cognitivos §7 (CREATED→ANALYZED→PARTIALLY_VALIDATED→MONITORED→STRENGTHENED→PRINCIPAL / REFUTED / INCONCLUSIVE) CONFLITA com o modelo canônico de hipótese CHM-001/RULE-BB-003 (EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→ARCHIVED) — risco de CC-02; REJEITADO, prevalece CHM-001 (COG-SPEC-004 mapeia para CHM, não cria lifecycle paralelo); (b) Quality Gates G0–G9 (§22) colidem com Quality Gates L1–L4 / harness-score L0–L4 — namespace G rejeitado como gate global (locais); (c) I-COG-01..12 (§21) e COG-P01..P15 (§4) — invariantes/princípios LOCAIS que referenciam N8–N17/INV/PC/PB (I-COG-01=RULE-EPI/TRACE-06; I-COG-06=RULE-CAU-01; I-COG-11=RULE-MET-01/INV-09); (d) §15/§16 calibração/bayes/risco (COG-SPEC-035..039/043) → CCM-001/Conviction (J-001 aberto), não define. FRONTEIRAS CONFORMES (Revisor): J-001 (probabilístico/confidence genéricos ≠ Conviction Vector 8D), INV-05 (COG-SPEC-040 análise≠autoridade decisional), RULE-MET-01/INV-09 (I-COG-11 feedback≠fabricação), RULE-EPI/TRACE-06 (fato≠inferência). MC-COG = hub do trio (§18 Cognition-to-RAG/Experience/Learning/Governance/Skills). Tratamentos R-05/R-01/R-06 + X-01 na ATIVAÇÃO (SPEC-002 homologada/consolidação cognitiva). [K-MAN-16] -->

<!-- Emenda 2026-09-21 (DHR-MC-LRN-001): admitido ao backlog (BL-015, Em espera) o MC-LRN-001 / Master Contract da Camada de Learning (`reference/camadas/CAMADA APRENDIZADO.MD`), classificado como referência externa não-normativa. 5º da família (RAG/EXP/COG/GOV/LRN); é o PROPOSITOR — face inversa do MC-GOV §34: Learning propõe, Governance decide (LRN-P08/P14, I-LRN-12 = INV-09/I-GOV-13/RULE-GMC-005/trio; SEM dupla autoridade). ~grande parte já é FATO NORMATIVO (N8–N17 + INV-07/09 + governança viva). Status "BASELINE"/"BASELINE PROPOSTA" sem efeito (INV-09; X-01). COLISÕES: (a) Quality Gates G0–G10 (§51) vs L1–L4/harness-score L0–L4 — namespace G local; (b) I-LRN-01..15 (§50) e LRN-P01..P14 (§5) LOCAIS ancorados nos canônicos: I-LRN-02 (corr≠causa)=RULE-CAU-01/RULE-EPI-02, I-LRN-11 (não reescreve experiência)=INV-07/RULE-BB-004, I-LRN-12 (sem autoridade Governança)=INV-09; (c) estados §9 (CREATED→…→PROMOTED / SUPPORTED/REFUTED) = ciclo de vida do LEARNING CANDIDATE (objeto distinto) — NÃO conflita com CHM-001 (hipótese) nem com Change Record MC-GOV §13; mapear só na fronteira handoff VALIDATION→GOVERNANCE (X-02; diferente do conflito grave do MC-COG §7). FRONTEIRA J-001/N-001 (R-05): §28/§43 parameter learning/calibration + §41 avaliação estatística NÃO fecham nem calibram o Conviction Vector — pesos por ativo = N-001 (parte de J-001 aberto) → diferido ao CCM-001/Conviction Engine; saída sempre Learning Candidate (proposta). CC-02: Learning Candidate projeta CEM/CHM, não redefine. Delta útil: Learning Candidate schema §8, Experiment Contract §15 (baseline/A-B/backtest/replay/OOS), overfitting/regression §30/§23, parameter drift LRN-SPEC-041..045 → SPEC-018 (L-001) + K-001 + backtest. Tratamentos na ATIVAÇÃO (SPEC-018 em redação / K-001). [K-MAN-18] -->

<!-- Emenda 2026-09-21 (DHR-MC-SKL-001): admitido ao backlog (BL-016, Em espera) o MC-SKL-001 / Master Contract da Camada de Skills (`reference/camadas/CAMADAS SKILLS.MD`), classificado referência externa não-normativa. 6º e último da família (RAG/EXP/COG/GOV/LRN/SKL) — completa o conjunto. Resolve escopo de I-001 (Skills → SPEC-025). ACHADO CENTRAL R-ARCH: §"ponto arquitetural"/§37 propõem Skill≠agente especialista (Elliott/SMC/ICT como competências usadas por um agente), o que INTERSECTA o baseline vigente que os trata como AGENTES (RULE-EW/SM/ICT, hierarquia CC-01/RULE-001/RULE-008). RESOLUÇÃO: redigido como possibilidade ("permite"), não deleta/reescreve agentes; REJEITADO como reenquadramento imediato — prevalecem CC-01/hierarquia/RULE-EW-SM-ICT; decisão DIFERIDA a SPEC-025/I-001 (admissão só como ref. externa não-normativa; não toca a arquitetura agora). Status "MASTER SPECIFICATION"/"MASTER CONTRACT BASELINE" sem efeito (INV-09; X-01). COLISÕES: (a) Quality Gates G0–G13 (§28) vs L1–L4/harness-score L0–L4 — namespace G local; (b) Skill Depth LEVEL 0–5 (§21) vs L0–L4/L1–L4 — namespace LEVEL local; (c) I-SKL-01..20 (§27) e SKL-P01..P24 (§5) LOCAIS ancorados: I-SKL-07 (exp≠regra)=INV-07/RULE-CAU-01/EPI, I-SKL-12 (não substitui cognição)=MC-COG, I-SKL-13/15 (Governança/Learning)=INV-09/I-GOV-13/I-LRN-12. FRONTEIRA J-001 (R-05): SKL-SPEC-044/065 calibração de confiança da Skill NÃO fecha o Conviction Vector 8D (INV-03/J-001 abertos → CCM-001). CC-02: Skill não redefine CEM/CHM/CCM/CDM/CNM. Coerência família §37: Skill usa RAG/COG/EXP/LRN/GOV sem autoridade própria (SKL-P11/P12); Learning propõe/Governança decide (SKL-P14/I-SKL-15). Tratamentos na ATIVAÇÃO (SPEC-025 / I-001). [K-MAN-19] -->

<!-- Emenda 2026-09-21 (DHR-MC-GOV-001): admitido ao backlog (BL-013, Em espera) o MC-GOV-001 / Master Contract da Camada de Governança, classificado como referência externa não-normativa. ACHADO CENTRAL R-06 (dupla autoridade): MC-GOV-001 descreve a governança que o SOT JÁ OPERA — ~80% já é FATO NORMATIVO VIVO (trio Especificador→Revisor→Andraus, GMC-001/RULE-GMC-005, PAP-001, RMR-001, INV-07/INV-09/PC-08, Constitution Check, atas DHR). RESOLUÇÃO: entra SUBORDINADO, escopo = governança de RUNTIME (SPEC-018/019/L-001); NÃO substitui a governança viva de spec-time; Andraus permanece Decisor Final (§46/PC-08). MC-GOV ESPELHA (não recria): I-GOV-02=trio/RULE-GMC-005; I-GOV-03=Revisor≠Andraus; I-GOV-06=INV-09; I-GOV-08=INV-07; §10 fail-safe=ENF-04; I-GOV-13=INV-09/feedback≠autorização; I-GOV-12=liberdade cognitiva. COLISÕES: (a) Quality Gates G0–G11 (§65) colidem com Quality Gates L1–L4 / harness-score L0–L4 — namespace G rejeitado como gate global (locais); (b) I-GOV-01..15 (§64) e GOV-P01..P15 (§5) — invariantes/princípios LOCAIS ancorados nos canônicos vivos; (c) estados de mudança §13 (DRAFT→…→PROMOTED / REJECTED/DEFERRED/ROLLED_BACK/SUPERSEDED/EXPIRED) = Change Record de runtime, mapear sem concorrer com CHM-001 (hipótese) nem RMR-001 (backlog). Status "BASELINE"/"BASELINE PROPOSTA" sem efeito (INV-09). Delta útil = §7 Change Record, §45 Decision Record, §30 Rollback, §34 Learning gov, §43 Exceções → SPEC-018/019. Tratamentos T-01..T-08 na ATIVAÇÃO (SPEC-018/019 em redação / L-001 / evento runtime). [K-MAN-17] -->

<!-- Emenda 2026-09-21 (DHR-EUA-E17): reposicionamento sequencial no ROADMAP — SPEC-019/020/021 antecipadas para uma FASE GOV entre SPEC-001 e SPEC-002; renumeração de Fases 10–17→8–15 (números de Specs inalterados). NENHUMA colisão de rótulo (é mudança de sequência, não de namespace). Acréscimo de escopo à SPEC-019: Contrato de Herança Vertical macro→micro (normativiza GEH-001 §6; regra de conservação + verificação inter-nível; resolve L-001) — este é o elo vertical que falta ao MAN-001 (que é convergência HORIZONTAL, K-MAN-02). SPEC-020 faseada: núcleo constitutivo (correctness/grounding/hallucination/role adherence/context/safety/regression/adversarial) antecipado; dimensões dependentes-de-upstream (RAG faithfulness→SPEC-007; tool correctness→SPEC-038; decision traceability→SPEC-014) DIFERIDAS ao ponto de dependência (não fechadas — CONS-01). Método da FASE GOV = atomic-spec v1.4 (ou v1.5 se homologada antes); independente do piloto EUA-E15. Fronteiras conformes: não toca invariantes, não redefine canônico (CC-02), não fecha decisão aberta. [K-MAN-20] -->

<!-- Emenda 2026-09-21 (DHR-EUA-E18): registrada colisão de rótulos do Manual Universal §44/§46 (referência externa não-normativa). NÃO adotar do Manual Universal: nenhum catálogo operacional próprio — importado apenas o CONCEITO de separação de perspectivas (§44) e contestação estruturada (§46), classificados PRÁTICA (não normativo). Aproveitada a mecânica via §7-bis "Autopré-check de Redução de Viés" (especificador.md) + Passo 5-bis "Verificação Adversarial e de Conservação de Herança" (revisor.md) — simetria de propósito/granularidade entre os dois agentes, obrigatória para HIGH/CRITICAL. Delimitação preservada: o Bloco B/seção A verificam herança OBRIGAÇÃO-A-OBRIGAÇÃO sob CC-08 (EUA-E04) vigente; NÃO antecipam a regra escrita de conservação-como-conjunto (Contrato de Herança Vertical) cujo ESCOPO já foi homologado na SPEC-019 (EUA-E17/DHR-EUA-E17 §2, Q1=SIM) — falta apenas o conteúdo normativo, a redigir quando a SPEC-019 for elaborada; nenhuma decisão fechada tratada como pendente, nenhuma decisão aberta tratada como fechada (CONS-01 bidirecional). [K-MAN-21] -->

<!-- Emenda 2026-09-21 (DHR-EUA-E19): registrada colisão de escopo com CEE-001/RULE-CEE-002/003 (baseline interno, não referência externa). NÃO estender ao Especificador/Revisor SOT (camada meta): o roteamento de modelo por Tipo I–V (RULE-CEE-002) e o InferenceContextEnvelope/cache_control/stable_prefix (RULE-CEE-003) permanecem escopados ao ORYX AGENT/Trilha B (CEE-001 §1), hoje spec-only (não implementado) — comunicação via Blackboard, que o Especificador/Revisor não usam. Aproveitada apenas a MECÂNICA por analogia metodológica: regra NOVA e própria da camada meta — roteamento de modelo por papel (especificador.md=claude-opus-4-8/esforço médio; revisor.md=claude-sonnet-4-6/esforço alto) + extensão do dial GES (RULE-PPQ-001) ao escopo de leitura obrigatória + short-circuit via `sincronizado-até` (RPSA/EUA-E16). Ressalva de plataforma (RULE-MET-01): não há campo de frontmatter de subagente para "reasoning effort" — a política de esforço é orientação de conduta, não configuração; nenhuma capability inexistente foi declarada. Fronteiras conformes: não toca invariantes, não fecha decisão aberta, não relaxa o gate M-02 nem a checagem `ATIVADO` do RMR-001 (ambos permanecem núcleo sempre obrigatório). [K-MAN-22] -->

---

## Conflitos direcionais

| Situação | Elliott | SMC | Fibonacci | Resolução | Autoridade | RULE |
|---|---|---|---|---|---|---|
| Divergência direcional Elliott × SMC | Bullish | Bearish | — | Output = NEUTRO | Elliott (veto) | RULE-SY-001 |
| SMC bullish, Elliott bearish | Bearish | Bullish | — | Output = NEUTRO | Elliott (veto) | RULE-SY-001 |
| Fibonacci invalida contagem Elliott | Hipótese A | — | Contradiz proporções | Elliott recontar + emitir alternativa | Fibonacci informa, Elliott decide | RULE-FB-004 |
| CHoCH contra Elliott | Bullish | CHoCH bearish | — | Registra conflito, não bloqueia, reduz convicção SMC | Synthesis registra | RULE-SM-003 |
| BOS sem CHoCH anterior | Qualquer | BOS isolado | — | SMC não pontua esse BOS (sem mudança de caráter prévia) | RULE-SM-005 | RULE-SM-005 |
| Elliott ambíguo (2 contagens válidas) + SMC bullish | Ambíguo | Bullish | — | Output = AGUARDAR_SETUP (Elliott não resolveu) | Elliott (veto por omissão) | RULE-EW-008 |

---

## Conflitos fractais

| Situação | Grau Superior | Grau Inferior | Resolução | Impacto na Convicção |
|---|---|---|---|---|
| H1 impulsivo contra D1 corretivo | D1 corretivo | H1 impulsivo | Conflito fractal — reduz convicção estrutural. H1 pode ser subestrutural do corretivo D1. | Reduz convicção fractal significativamente |
| M5 vendendo contra início de Onda 3 no D1 | D1 Onda 3 | M5 corretivo | Interpretável como retração ICT para entrada — contexto determina. ICT verifica se é pullback ou reversão. | Sem redução se M5 for retração esperada |
| H4 incompatível com estrutura D1 | D1 | H4 divergente | Conflito fractal — invalidador para Elliott. Recontar obrigatório. | Reduz convicção estrutural drasticamente |
| S1 bearish vs D1 bullish | S1 bearish | D1 bullish | D1 pode ser correção do S1. Elliott verifica se D1 bullish é sub-onda corretiva do S1. | Reduz convicção fractal — alternativa plausível |

---

## Conflitos de timing (ICT)

| Situação | ICT | Resolução | RULE |
|---|---|---|---|
| Setup estrutural válido fora de killzone | Killzone inativa | Execução possível com convicção operacional reduzida (-1 ponto) | RULE-ICT-003 |
| Killzone ativa sem setup estrutural | Killzone ativa | ICT aguarda — sem hipótese estrutural, ICT permanece inativo | RULE-ICT-001 |
| R:R calculado < 1:3 com score 9/9 | — | SEM sinal. Score alto, R:R insuficiente — log interno | RULE-ICT-002 / RULE-006 |
| Stop estrutural excessivamente grande | — | ICT bloqueia execução | RULE-ICT-006 |

---

## Conflitos de convicção

| Situação | Componente | Resolução | RULE |
|---|---|---|---|
| Convicção global 60–70% | Synthesis | Output = AGUARDAR_SETUP | RULE-SY-003 [limiares Fase Piloto — Q-002] |
| Convicção global < 60% | Synthesis | Output = NEUTRO | RULE-SY-003 [limiares Fase Piloto — Q-002] |
| Convicção Elliott alta (>80%) + SMC fraco | Synthesis | Sinal possível — SMC é confirmatório, não bloqueante | RULE-SY-001 |
| Elliott 3/3 + SMC 0/3 + ICT 0/3 (score 3/9) | Synthesis | Output = AGUARDAR_SETUP — threshold mínimo não atingido | RULE-003 |
| Hipótese A e B com diferença < 10% de convicção | Synthesis | NÃO emite sinal — vantagem não significativa | RULE-EW-008 |

---

## Conflitos de qualidade de evidência

| Situação | Resolução | RULE |
|---|---|---|
| BOS + rompimento de estrutura na mesma zona | Contar como UMA evidência (correlacionadas) | RULE-004 |
| OB mitigado apresentado como zona ativa | SMC invalida o layer — OB descartado | RULE-SM-001 |
| Sweep sem retorno ao range | SMC invalida o layer do sweep | RULE-SM-007 |
| Divergência na Onda 3 (momentum alto) | Baixa relevância — esperado em Onda 3 | RULE-SM-006 variante |
| Divergência na Onda 5 | Alta relevância — possível fim de impulso | RULE-SM-006 variante |

---

## Inversões contextuais (GPR-001 §3.6)

**[HOMOLOGADO — Andraus, 2026-09-20 (RCH-001 Ciclo #1)]**

Inversão contextual ocorre quando um princípio normalmente de menor peso passa a dominar em um contexto específico. Não é incoerência — é a regra de inversão que precisa estar especificada. [FONTE: GPR-001 §3.6:267-269]

| # | Contexto | Trigger | Princípio que sobe | Princípio que desce/suprime | Efeito operacional | Referência |
|---|---|---|---|---|---|---|
| 1 | Evento crítico de mercado | Ruptura de hipótese dominante | PCO-01 (hipóteses concorrentes) | PO-01 (economia cognitiva) | Cognitive Scheduler desperta análise completa independente do custo | GPR-001 §3.6:275-277 |
| 2 | Efeito irreversível | Detecção de efeito com nível E3 (crítico + irreversível) | PB-01 (eficácia) via PO-07 (reversibilidade como sinal) | PB-03 (eficiência) | Mais validação, menos economia — fail-closed | GPR-001 §3.6:282-284 |
| 3 | Regime desconhecido | Entrada em regime de mercado não-estabelecido | PS-03 (exploração) + PS-02 (cautela) | — (nenhum suprimido; PC-04 eleva-se a barreira crítica) | PC-04 (piso de convicção) vira barreira de segurança crítica | GPR-001 §3.6:289-291 |

**Notas de integração:**
- Inversão #1 referencia o Cognitive Scheduler (SPEC-008, pendente); a mecânica de ativação será especificada nessa Spec. [INFERÊNCIA]
- Inversão #2 alinha-se à camada de enforcement E3 (atomic-spec.md §10.2) e ENF-04 (fail-closed para efeito crítico irreversível). [FONTE]
- Inversão #3 conecta-se aos limiares de Fase Piloto do Conviction Vector (Q-002: ≥70%, 7/9) e à Salvaguarda de piso de convicção (CEE-001 §11). [FONTE]

---

## Colisões classificadas — Master Contracts diferidos (BL-010/011/012)

<!-- Emenda 2026-09-28 (DHR-BL010-011-012-001): consolidação tabular das colisões já registradas em
     K-MAN-14 (MC-RAG-001/BL-010), K-MAN-15 (MC-EXP-001/BL-011), K-MAN-16 (MC-COG-001/BL-012).
     Classificar ≠ aplicar: tratamentos de aplicação permanecem diferidos à ativação
     (SPEC-004/006/007 e consolidação cognitiva). Nenhuma colisão fecha J-001, redefine
     CEM-001/CHM-001 (CC-02) ou toca INV-05/INV-09. Fonte: governance/CLASSIFICACAO-COLISOES-BL010-011-012.md -->

| Item | ID | Elemento externo | Colide com (SOT) | Prevalece | Decisão | K-MAN |
|---|---|---|---|---|---|---|
| BL-010 | COL-RAG-01 | Quality Gates G0–G8 (§13) | L1–L4 / L0–L4 | SOT | REJEITAR global → gate LOCAL | K-MAN-14 |
| BL-010 | COL-RAG-02 | Ordem 4Es §1 (Efic.→Eficiência→Efetividade) | CEE-001 §12 | SOT | REJEITAR ordem externa | K-MAN-14 |
| BL-010 | COL-RAG-03 | I-RAG-01..10 (§12) / RAG-P01..P14 (§3) | INV/PC/PB | SOT | ADAPTAR como LOCAIS | K-MAN-14 |
| BL-010 | COL-RAG-04 | RAG-SPEC-018 (Evidence Independence) | RULE-004/RULE-MET-01 | SOT | CONFORME (não redefine) | K-MAN-14 |
| BL-011 | COL-EXP-01 | Status "BASELINE"/"BASELINE PROPOSTA" | INV-09/PC-08 | SOT | REJEITAR efeito → PROPOSTA | K-MAN-15 |
| BL-011 | COL-EXP-02 | Quality Gates G0–G8 (§52) | L1–L4 / L0–L4 | SOT | REJEITAR global → gate LOCAL | K-MAN-15 |
| BL-011 | COL-EXP-03 | I-EXP-01..12 (§51) / EXP-P01..P14 (§5) | INV/PC/PB | SOT | ADAPTAR como LOCAIS | K-MAN-15 |
| BL-011 | COL-EXP-04 | Working Memory §7.6 | Blackboard/SPEC-004 | SOT | ADIAR/RELOCAR a SPEC-004 | K-MAN-15 |
| BL-011 | COL-EXP-05 | EXP-SPEC-021 ↔ RAG-SPEC-018 (dup.) | RULE-004 | SOT | ~~ADIAR reconciliação (SPEC-006/009)~~ → **re-apontada à SPEC-007** (Andraus, 2026-10-19, DHR-BENCH-INTEL-001 D8; abertura homologada em DHR-SPEC007-001; o Plan da SPEC-007 deve tratá-la) | K-MAN-15 |
| BL-012 | COL-COG-01 | Estados cognitivos §7 | CHM-001/RULE-BB-003 (CC-02) | CHM-001 | REJEITAR §7 → mapear p/ CHM-001 | K-MAN-16 |
| BL-012 | COL-COG-02 | Quality Gates G0–G9 (§22) | L1–L4 / L0–L4 | SOT | REJEITAR global → gate LOCAL | K-MAN-16 |
| BL-012 | COL-COG-03 | I-COG-01..12 (§21) / COG-P01..P15 (§4) | N8–N17/INV/PC/PB | SOT | ADAPTAR como LOCAIS | K-MAN-16 |
| BL-012 | COL-COG-04 | Calibração/bayes/risco §15/§16 | CCM-001 (J-001 aberto) | SOT | ADIAR ao CCM-001 (não define) | K-MAN-16 |
| BL-012 | COL-COG-05 | Status "Baseline" (l.6) | INV-09 | SOT | REJEITAR efeito → ref. externa | K-MAN-16 |

Fronteiras confirmadas CONFORMES (todos os itens): J-001 permanece aberto (confidence/calibração ≠ Conviction Vector 8D); CC-02 preservado (pacotes externos PROJETAM CEM-001/CHM-001); INV-05 preservado (nenhuma camada decide/executa); INV-09 preservado (feedback/status externo ≠ autoridade/baseline). Homologado por Andraus, DHR-BL010-011-012-001 (parecer do Revisor CONFORME, 2026-09-28).

---

## O que é impossível por definição

```
IMPOSSÍVEL: Sinal COMPRA ou VENDA com convicção global < 70%.   [limiar de Fase Piloto — recalibrável, Q-002]
IMPOSSÍVEL: ICT emitindo setup sem hipótese estrutural aprovada.
IMPOSSÍVEL: SMC sobrepondo ou corrigindo a direção de Elliott.
IMPOSSÍVEL: Fibonacci criando uma contagem de ondas.
IMPOSSÍVEL: Duas evidências causalmente correlacionadas contando como independentes.
IMPOSSÍVEL: Sinal operacional com conflito direcional aberto entre Elliott e SMC.
IMPOSSÍVEL: Sinal operacional com R:R < 1:3.
IMPOSSÍVEL: Sinal operacional sem declaração explícita do invalidador.
IMPOSSÍVEL: Sinal contra o bias do D1.
IMPOSSÍVEL: ICT com score 0/3 em setup considerado válido pelo Synthesis.
```
