# EUA-E18 — Redução de Viés e Uso Sincronizado da Spec-Lean entre Especificador e Revisor (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E18** (emenda aos agentes `especificador.md` e `revisor.md`) |
| Versão | **v3 — formalizada no Claude Code** (Especificador, 2026-09-21). Supersede o rascunho de chat homônimo (raiz) e a v2. A v2 incorporou os achados #1–#5 da leitura factual anterior (ver §0 e §11); esta v3 incorpora o parecer formal **NÃO CONFORME RECUPERÁVEL** do Revisor SOT sobre a v2 — achados M-01/M-02/M-03/m-01/m-02/m-03 (ver §11.2). |
| Natureza | Emenda dual — acrescenta mecanismos de redução de viés ao Especificador e protocolo simétrico de verificação ao Revisor, sem alterar o fluxo de autoridade nem os baselines de domínio |
| Status epistemológico | **HOMOLOGADA — vigência imediata** (DHR-EUA-E18, Andraus, 2026-09-21; Q1–Q7 = Sim; parecer do Revisor CONFORME na v3, após 1º parecer NÃO CONFORME RECUPERÁVEL sobre a v2 — M-01/M-02/M-03/m-01/m-02/m-03, todos tratados). Efeitos registrados em `.claude/agents/especificador.md` (§7-bis), `.claude/agents/revisor.md` (Passo 5-bis), `CATALOGO-OFICIAL.md`, `CONFLICT-MAP.md` (K-MAN-21) e RPSA (`sincronizado-até` → DHR-EUA-E18). *(Filename mantém "_PROPOSTA" por convenção de repositório — o status vigente é este e o do CATÁLOGO/DHR.)* |
| Autoria | Rascunho: Especificador (chat — Andraus/Claude Sonnet 4.6, 2026-09-21). Formalização: Especificador (Claude Code, Sonnet 5, 2026-09-21). |
| Data | 2026-09-21 |
| Alvo | `.claude/agents/especificador.md` (§7 Autopré-check + novo §7-bis) · `.claude/agents/revisor.md` (§4 interpelação + §5 Passo 5 + novo §5-bis) |
| Fundamento no baseline | **RULE-EPI-01..03** (EUA-E05 — anti-conversão, abstenção produtiva); **RULE-MET-01** (EUA-E14 — não-fabricação, revisabilidade); **CEE-001 §12 4Es** (Eficácia precede Eficiência); **Manual Universal §44/§46** (separação de perspectivas, contestação estruturada — classificados PRÁTICA, não normativos); **atomic-spec D8** (adversarial/negação como profundidade-alvo para CRITICAL); **EUA-E17/DHR-EUA-E17** (FASE GOV, SPEC-019 — Contrato de Herança Vertical, ver §0) |
| Princípio-guia | **O que o Especificador produz como obrigação, o Revisor verifica como obrigação — na mesma linguagem, com ferramenta simétrica.** Viés de confirmação no Especificador e viés de leniência no Revisor são **reduzidos** por protocolo estrutural — não eliminados, e não por intenção. |

---

## 0. Declaração de escopo desta emenda (correções #1 e #2, tratadas na v2; ajustadas na v3 — ver M-02) `[PROPOSTA]`

Para eliminar duas imprecisões apontadas na leitura factual anterior, este documento declara explicitamente:

**Correção #2 — título.** O rascunho intitulava-se "Eliminação de Viés". Pedir ao próprio autor que gere seus casos de negação (Bloco A do §7-bis) **reduz**, não elimina, o viés de confirmação — a escolha de quais falhas documentar é ela mesma enviesada; só a verificação independente do Revisor (Passo 5-bis) compensa parcialmente. O título e as referências internas foram corrigidos de "Eliminação" para "Redução" em todo este documento.

**Correção #1 — relação com a EUA-E17/SPEC-019.** O Bloco B do §7-bis (Especificador) e a seção A do Passo 5-bis (Revisor) verificam a **herança obrigação-a-obrigação já declarada por CC-08** (EUA-E04, vigente). Isso **não** antecipa a regra de **conservação-como-conjunto** (Contrato de Herança Vertical macro→micro) que a SPEC-019 irá normatizar quando **redigida e homologada**. Os Blocos B foram reescritos com uma nota de delimitação explícita (§3.1, §4.1) para que não sejam lidos como uma regra de conservação vertical formal antes que ela exista como norma escrita.

> **Correção M-02 (parecer do Revisor sobre a v2):** a v2 descrevia o acréscimo de escopo à SPEC-019 como "condicionado a Q1" / "sujeito a Q1" da EUA-E17 — isso estava **factualmente incorreto**. A EUA-E17 (DHR-EUA-E17 §2, 2026-09-21) já homologou **Q1 = SIM**: o Contrato de Herança Vertical já é **escopo autorizado** da SPEC-019 — decisão de escopo **fechada**, não pendente. O que ainda **não existe** é a **regra escrita** (o conteúdo normativo da conservação-como-conjunto) — essa só surge quando a SPEC-019 for redigida e homologada. A distinção correta é: **escopo já decidido (Q1=SIM) ≠ norma ainda não redigida**. CONS-01 aplica-se ao conteúdo da regra (ainda inexistente), não ao escopo (já decidido) — nenhuma decisão aberta é tratada aqui como fechada, e nenhuma decisão fechada é tratada como pendente. Todas as menções à "Q1 pendente/sujeita a/condicionada" nesta emenda foram corrigidas nesta v3 (§1.3, §3.1, §8, §12).

Quando a SPEC-019 for homologada com a regra escrita, este Bloco B é candidato a emenda pontual de alinhamento — registrado aqui como dependência futura de conteúdo normativo, não como decisão de escopo em aberto (CONS-01).

**Não altera:** o restante do diagnóstico (§1), o princípio de simetria (§2), o fluxo de autoridade (Especificador→Revisor→Andraus), a independência estrutural do Revisor, nem os invariantes de domínio.

---

## 1. Diagnóstico — o que existe, o que está fraco, o que está ausente `[INFERÊNCIA]`

### 1.1 O que existe e funciona (preservar integralmente)

A independência estrutural do Revisor é garantida por arquitetura (Write/Edit ausentes, ENF-03) — não é conduta, é impossibilidade física. O gate determinístico (`validate_spec_sot.py`) elimina viés na verificação estrutural antes de qualquer julgamento semântico. O protocolo de interpelação (Revisor §4) inverte o ônus da prova: o Especificador deve provar conformidade, não o Revisor presumir falha. A separação `VERIFY da skill ≠ CONFORME ≠ homologação` está blindada em três lugares.

### 1.2 O que está fraco (melhorar sem redesenhar)

**Fraqueza 1 — Auto-verificação concentrada no autor** `[INFERÊNCIA]`
O Especificador produz `plan.md` (a spec) e `checks.md` (a verificação da spec) — dois artefatos, mesmo agente. A auditoria documenta: *"a skill cobre simultaneamente spec e verificação-de-spec, e o Especificador é quem roda ambos."* O `checks.md` produzido pelo autor tende estruturalmente a verificar o que passou, não o que poderia ter falhado. Isso não é desonestidade — é viés de confirmação inerente à auto-avaliação.

**Fraqueza 2 — Disciplinas cognitivas N8–N17 sem verificação determinística** `[FATO ESTRUTURAL]`
A auditoria documenta: *"RULE-EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET são exigidas no Autopré-check e no Passo 3, mas não têm check determinístico em `validate_spec_sot.py` — dependem do julgamento semântico do Revisor."* Julgamento semântico sob pressão de entrega tende a viés de leniência — aprovar o que é difícil de refutar formalmente.

**Fraqueza 3 — Ausência de etapa adversarial estruturada no Revisor** `[INFERÊNCIA]`
O protocolo de 8 passos do Revisor é inteiramente verificativo: confere o que está declarado. Não há passo equivalente a D8 do método (adversarial/negação) no lado da revisão. O Manual Universal §46 prescreve contestação estruturada para decisões de alto impacto (PRÁTICA — não normativo). Essa etapa está ausente do protocolo do Revisor.

### 1.3 O que está ausente (decidir se é lacuna ou limite aceitável)

**Ausência 1 — Assimetria de método entre Especificador e Revisor** `[FATO ESTRUTURAL]`
O Especificador usa `tlc-spec-lean` (PLAN + CHECKS) para produzir. O Revisor usa GRE-001/HRE-001 para verificar. São frameworks diferentes. O Especificador declara "frozen obligations" via a skill (implicitamente, pelo método), mas o Revisor verifica cada BASpec individualmente — não verifica o conjunto de obrigações como bloco. Com a EUA-E04 (CC-08, Herança/Delta) essa assimetria aprofunda: cada spec passa a declarar herança explícita, mas o Revisor não tem mecanismo para verificar conservação das obrigações herdadas **obrigação-a-obrigação** como as tem hoje.

> **Nota de atualização (2026-09-21, pós-EUA-E17; corrigida na v3 — achado M-02):** a EUA-E17 (DHR-EUA-E17 §2) já homologou **Q1 = SIM** — o Contrato de Herança Vertical (conservação-como-conjunto entre níveis, macro→micro) já é **escopo autorizado** da SPEC-019; essa decisão de escopo está **fechada**, não pendente. O que ainda não existe é a **regra escrita** — ela só surge quando a SPEC-019 for redigida e homologada. Este documento **não** antecipa essa regra ainda inexistente — ver §0, correção #1.

**Ausência 2 — Verificação de hipótese de falha** `[INFERÊNCIA]`
Nenhum dos dois agentes opera com a pergunta: *"como esta spec poderia estar errada mesmo passando em todos os checks?"* Essa pergunta — equivalente ao D8 adversarial — está presente no método de especificação mas ausente no método de revisão.

### 1.4 Base de evidência (nota de status — correção m-01, EUA-E18 v3)

Esta emenda apoia-se, em parte, na auditoria `docs/arranque/AUDITORIA-ESTADO-ATUAL-AGENTES-HARNESS.md`, que é uma **auditoria não-homologada** (documentado ≠ homologado, TRACE-06). Seus achados são usados como `[FATO ESTRUTURAL]`/`[FATO DOCUMENTADO]` de diagnóstico, **não** como norma. A autoridade normativa permanece nos baselines (`especificador.md`, `revisor.md`, `atomic-spec.md`, `GPR-001`).

---

## 2. Princípio da simetria operacional `[PROPOSTA]`

A proposta parte de um princípio único:

> **Cada obrigação que o Especificador declara ter satisfeito, o Revisor verifica ter sido satisfeita — com a mesma granularidade, na mesma linguagem, usando o conceito equivalente da skill no seu papel.**

Isso não significa que os dois agentes usam a mesma ferramenta. Significa que:

- O Especificador usa a spec-lean para **produzir** obrigações verificáveis e para **questionar adversarialmente** sua própria entrega antes de submeter.
- O Revisor usa o equivalente conceitual da spec-lean (frozen obligations + mutation testing) para **verificar** que as obrigações declaradas são de fato satisfeitas — e não apenas formalmente presentes.

A simetria é de **propósito e granularidade**, não de ferramenta.

---

## 3. Mudanças propostas — Especificador `[PROPOSTA]`

### 3.1 Acréscimo ao §7 Autopré-check — Bloco Anti-Viés (novo bloco §7-bis)

Inserir após o Autopré-check existente (§7) o seguinte bloco obrigatório para specs de complexidade HIGH e CRITICAL:

```
## 7-bis. Autopré-check de Redução de Viés (obrigatório para HIGH e CRITICAL)
[Fonte: RULE-EPI-01..03 / RULE-MET-01 / atomic-spec D8 / Manual Universal §44/§46 — PRÁTICA]

Este bloco é executado DEPOIS do Autopré-check (§7) e ANTES de submeter ao Revisor.
Propósito: identificar o que a spec poderia ter errado, não o que ela declarou certo.
Este bloco REDUZ o viés de confirmação — não o elimina (a escolha de quais falhas
documentar é ela mesma enviesada; a verificação independente do Revisor no
Passo 5-bis é o que compensa parcialmente o que resta).

### Bloco A — Pergunta adversarial por BASpec (conceito D8 aplicado à auto-revisão)

Para cada BASpec CRITICAL ou HIGH da entrega, responda:
[ ] "Se esta BASpec estivesse errada, o que seria observável?" — documente o caso de negação.
[ ] "O ENTÃO desta BASpec é verificável por um observador independente?" — se não, reescreva.
[ ] "Existe uma condição em que o QUANDO se satisfaz mas o ENTÃO não deve ocorrer?" — se sim, adicione BASpec de negação.

Se não conseguir responder às três perguntas com âncora de fonte, marque a BASpec como [DECISÃO NECESSÁRIA] — não submeta sem resolução.

### Bloco B — Verificação de viés de confirmação na herança obrigação-a-obrigação (CC-08)

[Nota de delimitação — correção #1 (EUA-E18 v2) e M-02 (EUA-E18 v3): este bloco
verifica a herança OBRIGAÇÃO-A-OBRIGAÇÃO já declarada por CC-08 (EUA-E04, vigente).
NÃO antecipa a regra ESCRITA de conservação-como-conjunto (Contrato de Herança
Vertical macro→micro) — essa regra ainda não existe como norma; será redigida e
homologada junto da SPEC-019. O escopo de a SPEC-019 tratar esse contrato JÁ FOI
HOMOLOGADO (EUA-E17/DHR-EUA-E17 §2, Q1=SIM) — não é uma decisão pendente; falta o
conteúdo normativo, não a autorização. Quando a SPEC-019 for homologada com a
regra escrita, este bloco é candidato a emenda pontual de alinhamento — registrado
aqui como dependência futura de conteúdo, não como decisão de escopo em aberto
(CONS-01).]

Quando a spec declara herança (CC-08, EUA-E04):
[ ] Liste explicitamente cada obrigação herdada do canônico pai (ID+versão, RULE-HD-04).
[ ] Para cada obrigação herdada, documente UMA evidência de que ela foi satisfeita nesta spec.
[ ] Verifique que nenhuma obrigação herdada foi silenciosamente removida ou enfraquecida
    (RULE-HD-03 — supressão fora de REMOVED = achado Crítico) nem contradita por
    ADDED/MODIFIED (RULE-HD-02).

Se alguma obrigação herdada não tem evidência de satisfação → achado [DECISÃO NECESSÁRIA].
Este bloco é o substrato que o Revisor usará no Passo 5-bis, seção A (§5-bis do revisor.md).

### Bloco C — Verificação epistêmica (RULE-EPI-01..03 / CC-09)

[ ] Cada afirmação causal ("X causa Y", "X garante Y") tem mecanismo declarado
    e é compatível com método causal — correlação não basta (RULE-CAU-01 / RULE-EPI-02).
[ ] Nenhuma hipótese foi tratada como fato (RULE-EPI-01).
[ ] Onde há incerteza material, o estado INDETERMINADO foi usado em vez de forçar PASS/FAIL.
[ ] Nenhuma probabilidade foi declarada sem evento bem-formado (RULE-PRB-01).
[ ] Nenhuma precisão numérica foi declarada sem base (CC-09 — sem falsa precisão).

### Bloco D — reforço de escopo (não é item novo — correção #5, EUA-E18 v2)

[Nota (EUA-E18 v2, correção #5): o rascunho original tinha aqui um Bloco D redundante
com o §7 vigente — "spec produz recomendação/TMP, não executa" e "decisão≠execução"
já estão no Autopré-check §7: a linha "Nenhum invariante congelado violado (§8)"
(cobre INV-05) e o fragmento "decisão≠execução (RULE-DEC)" dentro da linha das
disciplinas N8–N17. Removido como bloco autônomo para não duplicar o gate. Fica
como PONTEIRO: ao preencher o §7-bis, reconfirme os itens correspondentes do §7
(INV-05 / RULE-DEC-01) — não é um novo checklist.]
```

### 3.2 Acréscimo ao §3 — Mapeamento explícito da skill para produção e auto-revisão

Inserir após o mapeamento atual de skill (§3):

```
**Uso da spec-lean em dois momentos distintos:**

Momento 1 — PRODUÇÃO (PLAN + CHECKS):
  A skill produz o artefato. O PLAN é a Spec. O CHECKS é a verificação estrutural
  da Spec (BASpec/EARS/Enforcement bem-formados). O VERIFY interno é feedback.

Momento 2 — AUTO-REVISÃO ADVERSARIAL (§7-bis):
  Após o CHECKS, antes de submeter ao Revisor, use o conceito de
  "mutation testing" da skill: pergunte "o que mudaria se esta obrigação
  estivesse errada?" para cada BASpec CRITICAL/HIGH.
  Isso não é um novo artefato — é uma pergunta mental documentada no Autopré-check.
  O Revisor saberá que você fez isso (via §7-bis preenchido) e verificará
  se as respostas são plausíveis (Passo 5-bis).
```

---

## 4. Mudanças propostas — Revisor `[PROPOSTA]`

### 4.1 Acréscimo ao §5 — Passo 5-bis (Verificação Adversarial e de Herança)

Inserir como **Passo 5-bis** entre o Passo 5 (BASpec + Profundidade) e o Passo 6 (Qualidade + Economia), obrigatório para HIGH e CRITICAL:

```
### Passo 5-bis — Verificação Adversarial e de Conservação de Herança
(obrigatório para HIGH e CRITICAL — executa após Passo 5)
[Fonte: atomic-spec D8 / EUA-E04 CC-08 / RULE-EPI-01..03 / Manual Universal §46 — PRÁTICA]

**Propósito:** verificar não apenas o que a spec declara ter satisfeito,
mas se as obrigações declaradas resistem a uma hipótese de falha.
Isso é o equivalente do D8 adversarial no lado da revisão.

#### A — Verificação das respostas do §7-bis do Especificador

[Nota de delimitação — correção #1 (EUA-E18 v2) e M-02 (EUA-E18 v3): a verificação
de herança abaixo é OBRIGAÇÃO-A-OBRIGAÇÃO sob CC-08 (EUA-E04, vigente). Não é a
verificação de conservação-como-conjunto (regra ESCRITA) que a SPEC-019 irá
normatizar quando redigida — não reprove uma spec por não satisfazer uma regra
que ainda não existe. O escopo de a SPEC-019 tratar esse contrato já foi
homologado (EUA-E17/DHR-EUA-E17 §2, Q1=SIM) — isso não é uma decisão pendente;
é a REGRA (conteúdo) que ainda não foi redigida.]

[ ] O Especificador preencheu o Bloco A (casos de negação por BASpec)?
    — Se não preencheu para spec HIGH/CRITICAL: achado Médio (não-bloqueante, mas registrado).
    — Se preencheu: verifique se os casos de negação são plausíveis ou apenas formais.
      "Se esta condição negativa existisse, o sistema detectaria?" — se não, achado Médio.

[ ] O Especificador preencheu o Bloco B (evidências de herança obrigação-a-obrigação)?
    — Se declarou CC-08 mas não preencheu o Bloco B: achado Médio.
    — Se preencheu: verifique UMA evidência por obrigação herdada, e que nenhuma
      foi suprimida fora de REMOVED (RULE-HD-03) nem contradita por ADDED/MODIFIED
      (RULE-HD-02). Para cada obrigação herdada sem evidência de satisfação:
      achado Crítico (obrigação declarada herdada mas não demonstrada = herança silenciosa).

#### B — Pergunta adversarial própria do Revisor (independente do §7-bis)

Para no mínimo 2 BASpecs CRITICAL (ou 1 se houver apenas 1):
[ ] "Se o ENTÃO desta BASpec nunca ocorresse, o sistema de verificação detectaria?"
    — Se não detectaria: registrar como achado Menor (gap de observabilidade).
[ ] "Existe uma condição em que o QUANDO se satisfaz mas o comportamento esperado
    seria diferente do declarado?" — se sim e não está coberto: achado Médio.

**Nota de calibração:** este passo não é para reprovar specs corretas por
não serem adversarialmente perfeitas. É para detectar obrigações
declaradas que não resistem à pergunta mais básica: "como saberemos se falhou?"
Achados Menores aqui não bloqueiam — registram para melhoria futura.
Achados Críticos (herança não demonstrada) bloqueiam.

#### C — Verificação epistêmica das disciplinas N8–N17 (anti-leniência)

As RULE-EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET são verificadas semanticamente
(sem gate determinístico disponível). Para evitar leniência por dificuldade de
refutação formal, aplique o seguinte protocolo mínimo:

Para RULE-EPI (anti-conversão hipótese→fato):
[ ] Existe ao menos UMA afirmação na spec que poderia ser interpretada como
    "isso é fato" quando deveria ser "isso é hipótese ou inferência"?
    — Se sim e sem etiqueta TRACE-06 correta: achado Médio.

Para RULE-CAU (mecanismo + regime):
[ ] Existe ao menos UMA afirmação causal sem mecanismo declarado, ou apoiada
    apenas em correlação?
    — Se sim: achado Médio (RULE-CAU-01 / RULE-EPI-02).

Para RULE-DEC (decisão≠execução):
[ ] Alguma BASpec cruza a fronteira SOT→execução? (INV-05 / RULE-DEC-01)
    — Se sim: achado Crítico (invariante).

Para as demais (RULE-SEM/ONT/INQ/CTF/UNC/PRB/MET):
[ ] Registre explicitamente "verificado sem achados" ou "achado [ID] encontrado"
    — não deixe estas disciplinas sem registro no relatório.
    A ausência de registro é o viés de leniência; o registro explícito
    (mesmo que "sem achados") é a proteção contra ele.
```

### 4.2 Atualização do §4 — Acréscimo à interpelação (item 8)

Inserir como item 8 na lista de interpelação do §4:

```
8. **Que preencheu o §7-bis (Autopré-check de Redução de Viés)** — para specs HIGH/CRITICAL,
   exija que o Especificador mostre: (a) pelo menos 1 caso de negação por BASpec
   CRITICAL; (b) evidências de herança obrigação-a-obrigação (se CC-08 declarado).
   Se o §7-bis não foi preenchido, isso é um achado — documente antes de prosseguir.
```

### 4.3 Atualização do §6 — Formato do relatório (seção 5-bis)

Inserir no template do relatório de revisão, após o item `Passo 5`:

```
   Passo 5-bis — Adversarial + Herança:  [PASS/FAIL] — [notas]
     Bloco A (casos de negação):         [verificado / não preenchido / achado]
     Bloco B (evidências de herança):    [verificado / não preenchido / achado]
     Bloco B adversarial próprio:        [BASpec CRITICAL verificadas: N]
     Bloco C (N8–N17 epistêmico):        [EPI: / CAU: / DEC: / restantes: ]
```

### 4.4 Acréscimo ao §6 — Registro de proporcionalidade (correção M-03, EUA-E18 v3)

A v2 propunha, no §7.1 do Especificador, uma checagem qualitativa de proporcionalidade (4Es) ao final das 3 primeiras specs da FASE GOV — mas não a refletia em nenhuma mudança do `revisor.md`, deixando a obrigação sem domicílio no arquivo do agente. Correção: inserir no template do relatório de revisão (§6), como linha adicional após o bloco do Passo 5-bis (§4.3), aplicável apenas ao relatório da 3ª spec sob este protocolo (SPEC-021):

```
   Nota de proporcionalidade (apenas no relatório da 3ª spec da FASE GOV — SPEC-021):
     Achados reais do §7-bis/Passo 5-bis nas 3 specs: [N achados / N blocos preenchidos]
     Avaliação qualitativa: [overhead proporcional / desproporcional] — [justificativa breve]
```

Esta nota é preenchida uma única vez, ao final da FASE GOV, e não se repete nas specs seguintes salvo decisão em contrário de Andraus. Não cria ferramenta determinística nem novo agente (§8) — é um campo textual do relatório já existente.

---

## 5. O que NÃO muda `[FONTE]`

- O **fluxo de autoridade** (Especificador → Revisor → Andraus) permanece intacto.
- O **gate determinístico** (`validate_spec_sot.py`) não é alterado — este é o gate estrutural; os novos blocos são semânticos.
- Os **8 passos do Revisor** são preservados; o Passo 5-bis é uma inserção entre Passo 5 e Passo 6, não uma substituição.
- O **Autopré-check §7** é preservado integralmente; §7-bis é adição, não duplicação (ver correção #5, §3.1 Bloco D).
- A **independência estrutural** do Revisor (Write/Edit ausentes, ENF-03) não é tocada.
- Os **invariantes de domínio** (INV-01..10, CC-01..CC-10, 4Es, Salvaguardas) não são alterados.
- A **skill tlc-spec-lean** e o **overlay GUS-TLC-001** não são alterados — apenas o uso da skill é estendido para um segundo momento (auto-revisão adversarial) no Especificador.
- As **atas DHR existentes** não são alteradas (INV-07).
- **CONS-01** respeitado: nenhuma decisão aberta (J-001, L-001 etc.) é tratada como fechada.
- **Não antecipa a regra escrita** do Contrato de Herança Vertical da SPEC-019 (EUA-E17) — o Bloco B (Especificador) e a seção A do Passo 5-bis (Revisor) verificam apenas herança obrigação-a-obrigação já vigente via CC-08. O **escopo** de a SPEC-019 tratar esse contrato já está homologado (EUA-E17/DHR-EUA-E17 §2, Q1=SIM); é a **regra em si** que ainda não foi redigida (ver §0, correção #1, e M-02 §11.2).

---

## 6. Mapa de simetria resultante `[PROPOSTA]`

```
ESPECIFICADOR                          REVISOR
─────────────────────────────          ──────────────────────────────
§3 Skill operacional:                  §3/§4 Interpelação:
  Momento 1: PLAN + CHECKS (spec)        Item 8: exige §7-bis preenchido
  Momento 2: §7-bis adversarial
                                       §5-bis Verificação adversarial:
§7-bis Autopré-check de Redução          Bloco A: verifica casos de negação
de Viés:                                 Bloco B: verifica evidências herança
  Bloco A: casos de negação              (obrigação-a-obrigação, CC-08)
  Bloco B: evidências de herança         Bloco B': adversarial próprio
  (obrigação-a-obrigação, CC-08)         Bloco C: N8–N17 anti-leniência
  Bloco C: verificação epistêmica
  Bloco D: ponteiro para §7            §5 Passo 5: BASpec + Profundidade
  (não é checklist novo)                 (preservado — verifica o que está)
                                       §5-bis: (novo — verifica o que resiste)

PRODUTO: spec com casos de negação     PRODUTO: relatório com achados de
documentados + herança evidenciada     resistência + N8–N17 registradas
```

A simetria é: **o Especificador documenta a hipótese de falha; o Revisor verifica se a hipótese de falha é plausível.**

---

## 7. Escopo e diferimento `[PROPOSTA]`

- Esta emenda altera apenas os arquivos de agentes (`.claude/agents/especificador.md` e `.claude/agents/revisor.md`).
- Os novos blocos (§7-bis do Especificador, Passo 5-bis do Revisor) são **obrigatórios para HIGH e CRITICAL**, **recomendados mas não bloqueantes para MEDIUM**, **não aplicáveis para LOW**.
- Os achados do Passo 5-bis são **Críticos apenas para herança não demonstrada** (CC-08 declarado sem evidência) e para violação de RULE-DEC-01 (INV-05). Todos os demais achados do Passo 5-bis são Médios ou Menores — registram sem bloquear.
- A incorporação ao `atomic-spec.md` (como extensão do D8) é diferida ao **piloto vigente** — auditoria retroativa da SPEC-001 (EUA-E15, regime auditoria-não-reescrita) — rumo à v1.5, junto com as demais emendas em piloto. *(Correção m-03, EUA-E18 v3: a v2 referenciava "SPEC-002/v1.5", desalinhado com a redesignação do piloto pela EUA-E15.)*
- **Escopo retroativo:** regime D-DHR-PAP-001-01 — retroativo-como-auditoria para a SPEC-001 (já coberta pelo piloto EUA-E15); prospectivo-obrigatório para SPEC-002+ e, por reposicionamento da EUA-E17, para **SPEC-019/020/021 (FASE GOV)**.

### 7.1 Nota de proporcionalidade — 4Es/Efetividade (correção #3, EUA-E18 v2)

O rascunho original não endereçava o custo do §7-bis (4 blocos) + Passo 5-bis (3 blocos) em toda spec HIGH/CRITICAL. Esse overhead recai **imediatamente sobre a SPEC-019/020/021** — o próximo trabalho autorizado pela EUA-E17, todas HIGH/CRITICAL. Tratamento:

- CEE-001 §12 (4Es: Eficácia precede Eficiência) autoriza o custo **na primeira aplicação** — reduzir viés é Eficácia; o overhead é Eficiência, subordinada.
- Para que o overhead não vire regra permanente não-examinada, esta emenda recomenda uma **checagem qualitativa de proporcionalidade** ao final da FASE GOV (após SPEC-019, SPEC-020-núcleo-A e SPEC-021 — as três primeiras specs sob o protocolo): o Revisor registra, no relatório da terceira spec, se os achados do §7-bis/Passo 5-bis justificaram o tempo gasto (achados reais capturados vs. blocos preenchidos sem achado). Essa checagem **não cria novo agente nem ferramenta determinística** (§8) — é uma nota qualitativa no relatório existente, sujeita à leitura de Andraus. O texto a inserir no `revisor.md` para que esta obrigação tenha domicílio normativo está em **§4.4** (correção M-03, EUA-E18 v3).
- Se a checagem indicar desproporção, a correção é por emenda pontual a este documento — não por desvio informal do protocolo.

---

## 8. Non-goals `[FONTE]`

- Não cria novo agente nem nova ferramenta determinística.
- Não altera o `validate_spec_sot.py` (gate estrutural permanece como está).
- Não fecha nenhuma decisão aberta (CONS-01) — nem trata como pendente uma decisão já fechada: a Q1 da EUA-E17 (escopo do Contrato de Herança Vertical na SPEC-019) já foi homologada como SIM (DHR-EUA-E17 §2); o que permanece aberto é apenas o **conteúdo** da regra escrita, a redigir quando a SPEC-019 for elaborada. *(Correção M-02, EUA-E18 v3.)*
- Não importa o catálogo operacional do Manual Universal §46 — importa apenas o conceito de contestação estruturada, como PRÁTICA classificada.
- Não substitui o julgamento semântico do Revisor — estrutura-o para reduzir leniência.
- Não torna o Revisor adversarial ao Especificador — torna o processo adversarial à entrega. A relação de cooperação (Especificador §2) é preservada.
- Não cria novo Constitution Check — os blocos §7-bis e Passo 5-bis são procedimentos, não itens do CC.
- Não introduz instrumento automático de medição de custo/latência — a proporcionalidade (§7.1) é observada qualitativamente no relatório do Revisor, não por métrica determinística.

---

## 9. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| **Q1** | Aprovar a adição do **§7-bis (Autopré-check de Redução de Viés)** ao `especificador.md`? | **Sim** — reduz viés de confirmação na auto-avaliação sem alterar o fluxo |
| **Q2** | Aprovar a adição do **Passo 5-bis** ao protocolo de revisão do `revisor.md`? | **Sim** — estrutura o julgamento semântico das N8–N17 e cria simetria com o §7-bis |
| **Q3** | Confirmar que os achados do Passo 5-bis são **Críticos apenas para herança não demonstrada e violação INV-05**, e Médios/Menores nos demais casos? | **Sim** — evita que o novo passo vire gate excessivamente restritivo |
| **Q4** | Aceitar a **obrigatoriedade para HIGH/CRITICAL** e opcional para MEDIUM? | **Sim** — proporcional ao risco; dial GES aplicado (PPQ-001 RULE-PPQ-001) |
| **Q5** | Diferir a **incorporação ao atomic-spec.md** ao piloto da v1.5 (junto com EUA-E04..E14)? | **Sim** — consistente com o regime vigente de incorporação diferida |
| **Q6** | Registrar esta emenda no **CATÁLOGO OFICIAL** e acrescentar entrada no **CONFLICT-MAP** (K-MAN-21 — Manual Universal §46 como PRÁTICA, não normativo)? | **Sim** — INV-07 + disciplina de referências externas |
| **Q7** *(correção #3, texto em §7.1 + §4.4)* | Confirmar a **checagem qualitativa de proporcionalidade** (Especificador §7.1 / Revisor §4.4) ao final das 3 primeiras specs da FASE GOV, sem criar instrumento novo? | **Sim** — mitigação mínima ao custo, sem violar Non-goals |

---

## 10. Fluxo de autoridade

```
[feito] Especificador (chat) redige a PROPOSTA (rascunho, raiz) — 2026-09-21
   ↓
[feito] Leitura factual informal (chat) identifica achados #1–#5
        (autocrítica do Especificador — NÃO é parecer formal do Revisor SOT)
   ↓
[feito] Especificador (Claude Code) formaliza a v2 em governance/ tratando os achados #1–#5
   ↓
[feito] Revisor SOT emite o PRIMEIRO parecer formal sobre a v2 →
        NÃO CONFORME RECUPERÁVEL (M-01/M-02/M-03; m-01/m-02/m-03)
   ↓
[feito] Especificador (Claude Code) formaliza a v3 tratando M-01/M-02/M-03/m-01/m-02/m-03
   ↓
[feito] Revisor SOT re-emite parecer sobre a v3 →
        **CONFORME** (zero Críticos, zero Médios; 2 Menores editoriais — já
        corrigidos: rótulos residuais "v2" no §0, granularidade da citação
        de "decisão≠execução" no Bloco D)
   ↓
[feito] Andraus homologa (decide Q1–Q7) → **SIM** para todas (DHR-EUA-E18, 2026-09-21)
   ↓
[feito] Especificador (Claude Code) aplica as mudanças homologadas a
   `.claude/agents/especificador.md` (§3 dois-momentos + §7-bis) e
   `.claude/agents/revisor.md` (§4 item 8 + Passo 5-bis + §6 template)
   ↓
[feito] Controlador atualiza CATÁLOGO OFICIAL · CONFLICT-MAP (K-MAN-21) · RMR-001 (passo 11-bis)
   ↓
[feito] RPSA (EUA-E16): re-sincronizados especificador.md / revisor.md
   (carimbo `sincronizado-até` → DHR-EUA-E18)
   ↓
Próxima spec (SPEC-019, FASE GOV) é produzida já com §7-bis obrigatório
   e revisada já com Passo 5-bis obrigatório
```

---

## 11. Registro de tratamento dos achados (rastreabilidade)

### 11.1 Achados da leitura factual anterior (autocrítica, tratados na v2)

| Achado | Severidade | Tratamento |
|---|---|---|
| **#1** — Bloco B antecipa a regra de herança vertical que a SPEC-019 (EUA-E17) vai definir | Médio | **Tratado na v2** — §0 declara a delimitação; Bloco B (§3.1) e seção A do Passo 5-bis (§4.1) reescritos como verificação obrigação-a-obrigação sob CC-08 vigente, com nota explícita de que não antecipam a conservação-como-conjunto da SPEC-019; §5 e §10 reforçam a delimitação. |
| **#2** — título "Eliminação de Viés" excede o mecanismo (reduz, não elimina) | Menor | **Tratado na v2** — título corrigido para "Redução de Viés"; linguagem interna ("suprimidos" → "reduzidos... não eliminados") corrigida no cabeçalho, no §7-bis e no item 8 do §4.2. |
| **#3** — custo/latência (4Es) não endereçado; recai sobre SPEC-019/020/021 | Médio | **Tratado na v2** — novo §7.1 (Nota de proporcionalidade) com checagem qualitativa ao final das 3 primeiras specs da FASE GOV; formalizado como Q7 (§9); sem criar instrumento novo (respeita Non-goals). |
| **#4** — RPSA não previsto para esta emenda | Menor | **Tratado na v2** — §10 (fluxo de autoridade) inclui explicitamente o passo RPSA (EUA-E16), com bump de `sincronizado-até` → DHR-EUA-E18. |
| **#5** — localização na raiz; Bloco D redundante com §7 vigente | Menores | **Tratado na v2** — este documento reside em `governance/` (ver §13); Bloco D (§3.1) convertido de checklist autônomo em ponteiro de reforço para os itens já existentes no §7 (`Nenhum invariante congelado violado (§8)` e `decisão≠execução (RULE-DEC)`), eliminando a duplicação. |

### 11.2 Achados do primeiro parecer formal do Revisor SOT (sobre a v2, tratados na v3)

| Achado | Severidade | Tratamento nesta v3 |
|---|---|---|
| **M-01** — Bloco C atribuía a falsa precisão à RULE-EPI-02 (que na verdade rege causalidade/correlação, EUA-E05) | Médio | **Tratado** — §3.1 Bloco C: linha de falsa precisão reancorada em CC-09; RULE-EPI-02 movida para a linha causal junto de RULE-CAU-01. Espelhado no Passo 5-bis §4.1 seção C (Revisor). |
| **M-02** — tratava a Q1 da EUA-E17 (escopo do Contrato de Herança Vertical na SPEC-019) como pendente, quando já foi homologada como SIM (DHR-EUA-E17 §2) — misrepresentação de decisão fechada | Médio | **Tratado** — corrigido em §0, §1.3 (nota de atualização), §3.1 (Bloco B), §4.1 (seção A), §8 (Non-goals) e §12 (evidências): a distinção passa a ser "escopo já decidido (Q1=SIM) ≠ regra ainda não redigida", nunca "decisão pendente". |
| **M-03** — a checagem de proporcionalidade (§7.1) não tinha correspondência nas mudanças do `revisor.md` (§4) — obrigação sem domicílio no arquivo-alvo | Médio | **Tratado** — novo §4.4 com o texto exato a inserir no template do relatório (§6 do revisor.md); §7.1 e Q7 (§9) atualizados para referenciar §4.4. |
| **m-01** — ausência do disclaimer "documentado ≠ homologado" para a auditoria não-homologada usada como diagnóstico | Menor | **Tratado** — novo §1.4 (Base de evidência / nota de status), espelhando o §1.2 da EUA-E17. |
| **m-02** — check de "remoção/enfraquecimento silencioso" no Bloco B sem ancorar RULE-HD-02/HD-03 | Menor | **Tratado** — Bloco B (§3.1) e seção A do Passo 5-bis (§4.1) passam a citar RULE-HD-02 (ADDED/MODIFIED não contradiz o herdado) e RULE-HD-03 (supressão fora de REMOVED = achado Crítico). |
| **m-03** — referência ao piloto de incorporação ("SPEC-002/v1.5") desalinhada com a redesignação pela EUA-E15 | Menor | **Tratado** — §7 atualizado para "piloto vigente — auditoria retroativa da SPEC-001 (EUA-E15)". |

---

## 12. Evidências de suporte (âncoras documentais)

| Afirmação | Evidência | Tipo |
|---|---|---|
| Auto-verificação concentrada no autor | `AUDITORIA-ESTADO-ATUAL §7 item 6`: *"o Especificador é quem roda ambos [spec + verificação-de-spec]"* | `[INFERÊNCIA]` |
| N8–N17 sem check determinístico | `AUDITORIA-ESTADO-ATUAL §13`: *"dependem do julgamento semântico do Revisor"* | `[FATO ESTRUTURAL]` |
| Revisor não usa tlc-spec-lean | `AUDITORIA-ESTADO-ATUAL §7 item 2`: *"Quem deveria usá-la: o Especificador. O Revisor não a usa."* | `[FATO DOCUMENTADO]` |
| Mutations/adversarial da skill não confirmados | `AUDITORIA-ESTADO-ATUAL §7 item 10`: *"[NÃO DETERMINADO]"* | `[NÃO DETERMINADO]` |
| D8 adversarial presente no método | `atomic-spec.md §2`: profundidade D8 = adversarial/negação para CRITICAL | `[FATO DOCUMENTADO]` |
| Contestação estruturada para alto impacto | `Manual Universal §46` — classificado **PRÁTICA** (não normativo) | `[PRÁTICA]` |
| Separação de perspectivas em multiagente | `Manual Universal §44` — classificado **PRÁTICA** (não normativo) | `[PRÁTICA]` |
| CC-08 declarado sem verificação de conservação-como-conjunto | `AUDITORIA-ESTADO-ATUAL §12/Q14`: *"não há contrato de herança vertical"* | `[FATO ESTRUTURAL]` |
| Contrato de Herança Vertical já é escopo homologado da SPEC-019 (Q1=SIM) — falta apenas a regra escrita | `DHR-EUA-E17 §2` (2026-09-21) — Q1–Q6 = Sim | `[FATO DOCUMENTADO]` |
| Achados de N8–N17 dependem de julgamento | `AUDITORIA-ESTADO-ATUAL §13`: *"obrigações do método sem verificação determinística"* | `[FATO ESTRUTURAL]` |
| RPSA exige re-sync dos agentes | `DHR-EUA-E16` (RPSA) | `[FATO DOCUMENTADO]` |
| Último K-MAN registrado antes desta emenda = K-MAN-20 | `governance/CONFLICT-MAP.md` (linha do K-MAN-20, DHR-EUA-E17) | `[FATO DOCUMENTADO]` |

---

## 13. Encaminhamento do rascunho da raiz (RPIR / HOD-001)

O rascunho de chat `EUA-E18_Eliminacao_Vies_Sincronizacao_SpecLean_PROPOSTA.md` na **raiz** é intake tratado por esta formalização. Conforme RPIR (HOD-001): "raiz = intake; tratado → pasta ou excluído; arquivar por padrão". Tratamento aplicado (mesmo padrão da EUA-E17): **movido para `docs/_legacy/` com sufixo `_rascunho-chat.md`** — histórico preservado, nunca deletado (INV-07). **Este arquivo (v3, `governance/`) passa a ser a versão de referência da EUA-E18.**

---

*HOMOLOGADA — v3, DHR-EUA-E18 (Andraus, 2026-09-21). Reside em `governance/` (Mapa de Pastas: emendas EUA-E* → `governance/`). Efeitos aplicados a `.claude/agents/especificador.md` (§7-bis) e `.claude/agents/revisor.md` (Passo 5-bis) — ver DHR-EUA-E18 §4 para o detalhe de cada edição. CATÁLOGO OFICIAL, CONFLICT-MAP (K-MAN-21) e RMR-001 (passo 11-bis) atualizados; RPSA re-sincronizou os agentes.*
