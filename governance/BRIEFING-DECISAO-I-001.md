# BRIEFING DE DECISÃO — I-001 ("Skills como unidades formais separadas?")

| Campo | Valor |
|---|---|
| Documento | BRIEFING-DECISAO-I-001 |
| Tipo | Brief de decisão (**NÃO-normativo**; NÃO fecha I-001; NÃO abre SPEC-025; NÃO edita ROADMAP/RMR-001; NÃO homologa) |
| Autor | Especificador SOT (souza.merchan@gmail.com — identificação de autoria) |
| Data | 2026-09-28 |
| Objeto | Preparar a decisão de I-001 para Andraus: pergunta exata, opções reais, trade-offs, recomendação técnica etiquetada, impacto de fechar sem abrir SPEC-025, risco de reversão. |
| Decisor | **Andraus** (CONS-01 — decisão aberta só fecha por homologação de Andraus; INV-09) |
| Fontes | `docs/arranque/respostas-questionario-v1.md:316-322`; `ROADMAP.md` §15 (SPEC-025), §21; `reference/camadas/CAMADAS SKILLS.MD` (MC-SKL-001); `backlog/RMR-001_Painel_Backlog.md` BL-016; `AGENTS.md` §6 item 1; `atomic-spec.md` §9, §10.6 (RULE-MECH-01..04 / CLASSE-MECH-001); `governance/AUDITORIA-ADIANTAMENTO-SLOTS-ROADMAP-2026-09-28.md` (Parte 3). |

> **Status epistemológico (TRACE-06).** A pergunta e o histórico de I-001 são **[FATO NORMATIVO]** (verificados nas fontes citadas). As opções e trade-offs são **[INFERÊNCIA]** derivada das fontes. A recomendação da §3 é **[PROPOSTA]**. Nenhuma linha deste documento fecha I-001 nem qualquer outra decisão aberta (CONS-01), abre/renumera slot (INV-07/RULE-ECC-01) ou substitui o `governance/CATALOGO-OFICIAL.md` (INV-09).

> **Restrição inviolável em TODAS as opções (não-negociável — não faz parte da decisão).** A hierarquia analítica **Elliott → Fibonacci → Fractal → SMC → ICT** (CC-01 / AGENTS.md §6 item 1 / INV-01/02) permanece **intocada** em qualquer opção. **ICT não cria hipótese de nenhum tipo.** I-001 decide *como a competência é empacotada e governada*, **nunca** quem cria hipótese nem a ordem de precedência entre escolas. Qualquer opção que altere CC-01 está fora do espaço de decisão. [FATO NORMATIVO]

---

## 1. A pergunta exata e o contexto histórico

**Pergunta literal de I-001** (`docs/arranque/respostas-questionario-v1.md:319`):

> "Skills como unidades formais separadas?"

**Ampliação operacional** (`ROADMAP.md` §15 / SPEC-025): I-001 governa se existe — e com que forma — uma **"Plataforma para todas as Skills"** que fixe, para cada Skill: definição; atomicidade; input/output; pré/pós-condições; ferramentas; conhecimento; RAG; evidência; eventos; Blackboard; testes; adversarial; versionamento; certificação; performance; custo; autonomia; governança. `ROADMAP.md` marca SPEC-025 como a Spec que **"Resolve I-001"**. [FATO NORMATIVO]

**Por que ficou aberta desde o Questionário v1 (2026-09-14).** No Questionário v1, Andraus fechou as decisões então maduras (B-001 = Conviction≠Synthesis; dimensionalidade=8; CHM-001/CEM-001 baselined) e deixou explicitamente I-001 como **"Inalterado — SPEC-025"** (`respostas-questionario-v1.md:319`). Ou seja: a decisão foi **deliberadamente diferida** ao momento em que a Spec da plataforma de Skills seria produzida, porque (a) não estava no caminho crítico da FASE 1–6 (núcleo cognitivo + agentes + síntese) e (b) sua resposta correta depende de saber como os agentes analíticos (SPEC-010..014) realmente se estruturam. Desde então, uma peça nova de contexto entrou:

- **MC-SKL-001** (`reference/camadas/CAMADAS SKILLS.MD`) foi admitido como **referência externa não-normativa** via **BL-016** (DHR-MC-SKL-001, 2026-09-21; K-MAN-19 registrado). Ele traz um **"Ponto arquitetural" explícito**: *"Skill não deve ser entendida como 'agente especialista'. O agente pode usar uma ou várias Skills"* — permitindo que "Elliott, SMC e ICT sejam competências especializadas, sem obrigar que cada uma seja um 'cérebro independente'". Esse é o **achado R-ARCH**, que o BL-016 **difere expressamente a SPEC-025** e condiciona a **"NÃO tocar hierarquia/CC-01/RULE-EW-SM-ICT vigentes"**. [FATO NORMATIVO — mas MC-SKL-001 é ref. externa, não baseline]
- **CLASSE-MECH-001** (DHR-CLASSE-MECH-001, 2026-09-27; `atomic-spec.md` §10.6) criou a taxonomia **Classe D/H/P/C** por BASpec. Isso dá vocabulário novo — e possivelmente **parte da resposta** — para I-001 (ver §2, Opção C). [FATO NORMATIVO]

**Alavancagem atual (por que Andraus está resolvendo agora).** A auditoria de hoje (`AUDITORIA-ADIANTAMENTO-SLOTS-ROADMAP-2026-09-28.md`, Parte 3) identifica I-001 como a **maior alavanca de largura** da fila: resolvê-la destrava **13 slots** (SPEC-025 + as 12 Skills analíticas SPEC-026..037), e — ao contrário de J-001 — **não depende de backtest**; é uma decisão de arquitetura, em tese tratável por deliberação. [INFERÊNCIA a partir da auditoria]

---

## 2. Opções reais

As três opções abaixo diferem apenas em **como a competência especializada é empacotada e governada** — não em quem raciocina nem na hierarquia. As invariantes CC-01, INV-05 (SOT não executa), INV-06 (Evidência≠Observação), CONST-01 (não redefinir canônico) valem igual em todas.

### Opção A — Skill = unidade formal separada e certificável (plataforma dedicada full-SPEC-025)

**O que é.** A Skill é um artefato de primeira classe, com identidade/versão/escopo próprios, contrato de I/O, certificação, testes e Harness dedicados — exatamente o programa de MC-SKL-001 (§8–§40: identidade, escopo, capacidades, limitações, contratos com RAG/Cognição/Experiência/Learning/Governança, estados DEFINED→…→ARCHIVED, 95 SKL-SPEC, 14 Quality Gates G0–G13, invariantes I-SKL-01..20). SPEC-025 nasce como a plataforma completa.

- **CC-01:** intocada. MC-SKL-001 §"Ponto arquitetural" é explícito que Elliott/SMC/ICT viram **competências que um agente usa**, com a cognição permanecendo integradora — a hierarquia de precedência não muda; o agente estrutural continua criando a hipótese primária, ICT continua sem criar hipótese. [INFERÊNCIA]
- **RULE-MECH-01..04:** compatível e reforçado — cada Skill declara Classe por BASpec (D/H/P/C) normalmente; a plataforma dá lar natural ao GATE DE SAÍDA (ENF-03) e ao BOUNDED LOOP das Classes H/P.
- **13 slots dependentes:** destrava todos — SPEC-025 como plataforma + SPEC-026..037 como instâncias. Máxima largura destravada.
- **Custo:** é a opção mais pesada (95 SKL-SPEC candidatas; risco de sobre-especificar antes de os agentes SPEC-010..014 existirem — a própria auditoria classifica SPEC-025 como Bloco S+R risco MÉDIO, e o ROADMAP §22 proíbe "Skills individuais antes da SPEC-025"). Risco de nascer desalinhada dos agentes reais.

### Opção B — Skill = anotação/rótulo dentro dos agentes existentes (sem plataforma separada)

**O que é.** "Skill" permanece um **conceito documental/organizacional** — um rótulo de competência dentro de um agente — sem plataforma formal, sem certificação, sem contrato de I/O próprio. Não há unidade arquitetural "Skill" independente do agente.

- **CC-01:** intocada (trivialmente — nada muda na estrutura de agentes).
- **RULE-MECH-01..04:** a Classe continua sendo declarada por BASpec **do agente**; não há objeto Skill separado a classificar. Consistente, porém perde a granularidade de certificar competências isoladas.
- **13 slots dependentes:** **esvazia** SPEC-025 (vira, no máximo, uma convenção de nomenclatura) e **descaracteriza** SPEC-026..037 como Specs de Skill independentes — as competências seriam absorvidas dentro das SPEC-010..014 (agentes). Efeito: a "largura" não é destravada como fila de Skills; é reabsorvida na fila de agentes. Pode ser legítimo (menos componentes — respeita ROADMAP §24/§16 "não criar Skills só para aumentar contagem"), mas **contraria o achado R-ARCH de MC-SKL-001** (que separa Skill de agente) e reduz contestabilidade cruzada (SKL-P09/multi-skill).
- **Custo:** o mais barato agora; maior risco de reconciliação depois se o sistema precisar de competências reutilizáveis entre agentes (ex.: Fibonacci usado por Elliott e por SMC) ou de certificação/versionamento independente de uma competência.

### Opção C — Híbrido por Classe (D/H/P/C): formalizar como Skill separada só onde há competência atômica e reutilizável

**O que é.** Skills existem como unidade formal separada **seletivamente** — pelo critério já previsto no ROADMAP §16 ("cada Skill só criada quando houver responsabilidade realmente atômica e independente") e agora com o vocabulário de CLASSE-MECH-001. Candidatos naturais a Skill formal: competências **Classe D** (determinísticas — ex.: cálculo de retração/extensão Fibonacci, detecção de FVG/Order Block por regra) e competências atômicas reutilizáveis entre agentes. Competências fortemente interpretativas/**Classe P** (julgamento estrutural Elliott, narrativa institucional) permanecem como **comportamento interno do agente**, não empacotadas como Skill certificável isolada.

- **CC-01:** intocada — Elliott/SMC/ICT como escolas e a precedência não mudam; o híbrido só decide o *empacotamento* de sub-competências, não a hierarquia. [INFERÊNCIA]
- **RULE-MECH-01..04:** é a opção que **melhor se acopla** à taxonomia. `atomic-spec.md` §10.6 já observa que "um domínio só-Classe-D não gera `PD-xx` de julgamento semântico" — sinalizando que Classe D e julgamento qualitativo são naturezas distintas. Uma Skill Classe D é, por definição, uma unidade determinística com GATE DE SAÍDA verificável — candidata ideal a Skill formal certificável; uma Classe P (LLM+julgamento) é mais difícil de "certificar" isoladamente e cabe melhor dentro do agente. **Parte da resposta a I-001 já está parcialmente pré-configurada por CLASSE-MECH-001.** [INFERÊNCIA — não é decisão; Andraus confirma]
- **13 slots dependentes:** destrava SPEC-025 (como plataforma **enxuta**, aplicável às Skills que qualifiquem) + o subconjunto de SPEC-026..037 que corresponda a competências realmente atômicas/reutilizáveis; as demais competências ficam dentro dos agentes (FASE 5). Largura destravada **parcial e proporcional** (respeita 4Es/Economicidade e ROADMAP §24).
- **Custo:** intermediário. Exige um critério de corte explícito (qual competência vira Skill formal) — o que é justamente o núcleo de SPEC-025. Menor risco de sobre-especificação que A; maior aderência ao R-ARCH e à Economicidade que B.

---

## 3. Recomendação técnica

**[PROPOSTA] — Opção C (Híbrido por Classe), como direção arquitetural**, deixando o *critério de corte* e a *extensão da plataforma* para a abertura da SPEC-025. **A escolha final é de Andraus (CONS-01).**

**[INFERÊNCIA] Justificativa:**
1. É a única opção que se alinha simultaneamente a (a) o achado **R-ARCH** de MC-SKL-001 (Skill≠agente; competências reutilizáveis) e (b) o princípio **4Es/Economicidade** do ROADMAP §24/§16 (não criar Skills só para contagem) — sem cair no extremo pesado (A) nem no extremo que descaracteriza a fila de Skills (B).
2. **CLASSE-MECH-001 já oferece o eixo de corte** (D determinística/certificável → candidata a Skill formal; P interpretativa → comportamento interno do agente). Isso reduz o arbítrio da decisão e a torna verificável — decidir I-001 como "híbrido governado por Classe" reaproveita norma já homologada em vez de criar critério novo. [INFERÊNCIA]
3. Preserva CC-01 de forma idêntica às outras opções (não é diferenciador) e mantém a contestabilidade cruzada (SKL-P09/multi-skill) onde ela agrega valor, sem forçá-la onde não agrega.

**Ressalva de conformidade (honestidade — RULE-MET-01):** esta é uma recomendação de *direção*, não um fechamento. O critério exato de corte D-vs-resto, a extensão da plataforma e a reconciliação das SKL-SPEC-001..095 exigem o **Dossiê de Pesquisa de abertura da SPEC-025** (RULE-ECC-01/02) — que só ocorre quando SPEC-025 for autorizada. Andraus pode fechar I-001 na direção C sem que isso pré-determine esse detalhe.

---

## 4. Impacto de fechar I-001 SEM abrir SPEC-025 ainda

**Fechar I-001 não obriga abrir SPEC-025 imediatamente, e não a antecipa no caminho crítico.** [INFERÊNCIA a partir de RULE-ECC-01, ROADMAP §25/§25-bis]

- **SPEC-002 permanece o próximo trabalho autorizado** (`ROADMAP.md` §25) — I-001 não está no caminho crítico da FASE 1–6; fechá-la não desloca a ordem regular. A auditoria de hoje protege isso explicitamente ("Ordem protegida... SPEC-002 é o próximo passo regular").
- **O que fechar I-001 libera:** conforme a auditoria (Parte 1, SPEC-025; Parte 3), resolver I-001 faz o *sliver S* de SPEC-025 (o template/plataforma de Skill-spec) **subir de "MÉDIO bloqueado" a candidato BAIXO de adiantamento parcial**. Ou seja: com I-001 fechada, torna-se possível produzir — como **linha paralela modelo SPEC-046** (`ROADMAP.md` §25-bis, faculdade de RULE-ECC-01 item 5) — o **Dossiê de Pesquisa + proposta de abertura** da SPEC-025 (ou do seu núcleo S de plataforma) **antes do gatilho nominal da FASE 10**, sem bloquear SPEC-002. As 12 Skills SPEC-026..037 (Bloco R) continuam dependendo dos agentes SPEC-010..014 e **não** são adiantáveis, mesmo com I-001 fechada.
- **Não é preciso abrir a SPEC-025 completa primeiro** para colher o valor de fechar I-001: o valor imediato é *desbloqueio* (remover a decisão que hoje anula os critérios C-AT1/C-AT2 de adiantamento — auditoria Parte 1/SPEC-025) e *estabilização do objeto* (dar às futuras SPEC-026..037 uma definição estável de "o que é uma Skill"). A abertura formal da SPEC-025 continua sujeita ao passo 1-bis do §23 (Dossiê + homologação) quando Andraus quiser.
- **Registro de gatilho (não executar aqui):** BL-016 tem gatilho `spec:SPEC-025 em redação ∨ decisao:I-001 resolvida` (`RMR-001` linha BL-016). **Fechar I-001 dispara a 2ª condição desse gatilho** — o que, pelo passo 11-bis do §23, exigiria tratamento/encaminhamento de BL-016 por Andraus (ativação do MC-SKL-001 como fonte de requisitos). Este briefing apenas sinaliza; não movimenta o RMR-001.

---

## 5. Risco de reversão (decidir agora vs. esperar SPEC-025)

**Pergunta:** se Andraus fechar uma opção agora e a SPEC-025 (quando aberta) revelar que ela não funciona bem na prática, qual o custo de reverter?

- **Baixo risco de reversão para a direção (Opção C) — moderado para A ou B.** [INFERÊNCIA]
  - Fechar I-001 como **direção C (híbrido governado por Classe)** é uma decisão de *princípio arquitetural*, não de detalhe. Ela é compatível com praticamente qualquer refinamento posterior (o corte D-vs-resto pode ser ajustado dentro de C sem reverter a direção). Reverter *dentro* de C custa uma emenda de critério na SPEC-025, não um redesenho.
  - **Opção A** tem maior custo de reversão: se a plataforma completa (95 SKL-SPEC) for especificada e os agentes SPEC-010..014 revelarem que a granularidade estava errada, muitos SKL-SPEC precisam ser refeitos (embora INV-07 preserve tudo por versionamento monotônico — nada é deletado, mas há retrabalho).
  - **Opção B** tem custo de reversão assimétrico: se depois for preciso extrair competências reutilizáveis, é preciso *criar* a plataforma que se decidiu não ter — reabrindo I-001 na prática.
- **Salvaguardas que baixam o custo de reverter, independentemente da opção:**
  - **INV-07 (versionamento monotônico):** nenhuma decisão refutada é deletada — reversão é registrada como supersessão, com trilha de auditoria. Reverter nunca destrói histórico.
  - **RULE-ECC-01/EUA-E21:** os slots são **indicativos** até a abertura; a direção fixada por I-001 não congela número/quantidade/fronteira das Skills — a abertura da SPEC-025 ainda pode dividir/fundir/redefinir sob Dossiê homologado.
  - **CLASSE-MECH-001 prospectivo:** não retroage sobre Specs homologadas; se o critério de corte por Classe se mostrar imperfeito, ele é ajustável por emenda pontual sem tocar SPEC-001/019/020/021.
- **Fator que aumenta a segurança de decidir agora:** I-001 **não depende de dados de mercado/backtest** (diferente de J-001). Toda a evidência necessária para a *direção* já está no repositório (MC-SKL-001 R-ARCH + CLASSE-MECH-001). O que a SPEC-025 acrescenta é *detalhe de implementação da plataforma*, não a resposta à pergunta de princípio. [INFERÊNCIA]
- **Recomendação de prudência [PROPOSTA]:** fechar I-001 na **direção** (C) agora é seguro e alavanca alta; fechar o **detalhe** da plataforma agora (Opção A completa) é o que carrega risco de reversão — esse detalhe deve ficar para a abertura da SPEC-025 sob Dossiê.

---

## Notas de conformidade

- Documento **[PROPOSTA]/brief**: **não fecha I-001, não abre SPEC-025, não edita ROADMAP/RMR-001, não homologa, não renumera slot** (CONS-01, INV-07, INV-09, RULE-ECC-01). SPEC-002 permanece o próximo trabalho autorizado, inalterado.
- CC-01 (hierarquia Elliott→Fibonacci→Fractal→SMC→ICT) é tratada como **restrição inviolável em todas as opções** — nunca objeto da decisão.
- MC-SKL-001 é **referência externa não-normativa** (BL-016, DHR-MC-SKL-001) — citado como fonte de requisitos/achado R-ARCH, nunca como baseline.
- Fechar I-001 dispara a 2ª condição do gatilho de BL-016 (`decisao:I-001 resolvida`) — encaminhamento (passo 11-bis do §23) é de Andraus; este briefing apenas sinaliza.
- Nenhuma fonte `[EXTERNO]`/web foi usada; todas as âncoras são documentos internos do repositório (RULE-ECC-04 não incide).

---

*Brief de decisão I-001 — Especificador SOT, 2026-09-28. NÃO-normativo (INV-09). Insumo para deliberação de Andraus. Homologação/encaminhamento: Andraus.*
