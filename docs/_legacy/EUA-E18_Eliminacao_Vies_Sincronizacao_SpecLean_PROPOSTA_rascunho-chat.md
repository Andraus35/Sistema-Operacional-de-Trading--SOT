# EUA-E18 — Eliminação de Viés e Uso Sincronizado da Spec-Lean entre Especificador e Revisor (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E18** (emenda aos agentes `especificador.md` e `revisor.md`) |
| Natureza | Emenda dual — acrescenta mecanismos anti-viés ao Especificador e protocolo simétrico de verificação ao Revisor, sem alterar o fluxo de autoridade nem os baselines de domínio |
| Status epistemológico | **PROPOSTA — não homologada.** Nenhum arquivo do repositório foi alterado. |
| Autoria | Especificador (chat — Andraus/Claude Sonnet 4.6, 2026-09-21) |
| Data | 2026-09-21 |
| Alvo | `.claude/agents/especificador.md` (§7 Autopré-check + novo §7-bis) · `.claude/agents/revisor.md` (§4 interpelação + §5 Passo 5 + novo §5-bis) |
| Fundamento no baseline | **RULE-EPI-01..03** (EUA-E05 — anti-conversão, abstenção produtiva); **RULE-MET-01** (EUA-E14 — não-fabricação, revisabilidade); **CEE-001 §12 4Es** (Eficácia precede Eficiência); **Manual Universal §44/§46** (separação de perspectivas, contestação estruturada — classificados PRÁTICA, não normativos); **atomic-spec D8** (adversarial/negação como profundidade-alvo para CRITICAL) |
| Princípio-guia | **O que o Especificador produz como obrigação, o Revisor verifica como obrigação — na mesma linguagem, com ferramenta simétrica.** Viés de confirmação no Especificador e viés de leniência no Revisor são suprimidos por protocolo estrutural, não por intenção. |

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
O Especificador usa `tlc-spec-lean` (PLAN + CHECKS) para produzir. O Revisor usa GRE-001/HRE-001 para verificar. São frameworks diferentes. O Especificador declara "frozen obligations" via a skill (implicitamente, pelo método), mas o Revisor verifica cada BASpec individualmente — não verifica o conjunto de obrigações como bloco. Com a EUA-E04 (CC-08, Herança/Delta) essa assimetria aprofunda: cada spec passa a declarar herança explícita, mas o Revisor não tem mecanismo para verificar conservação das obrigações herdadas como conjunto.

**Ausência 2 — Verificação de hipótese de falha** `[INFERÊNCIA]`
Nenhum dos dois agentes opera com a pergunta: *"como esta spec poderia estar errada mesmo passando em todos os checks?"* Essa pergunta — equivalente ao D8 adversarial — está presente no método de especificação mas ausente no método de revisão.

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
## 7-bis. Autopré-check Anti-Viés (obrigatório para HIGH e CRITICAL)
[Fonte: RULE-EPI-01..03 / RULE-MET-01 / atomic-spec D8 / Manual Universal §44/§46 — PRÁTICA]

Este bloco é executado DEPOIS do Autopré-check (§7) e ANTES de submeter ao Revisor.
Propósito: identificar o que a spec poderia ter errado, não o que ela declarou certo.

### Bloco A — Pergunta adversarial por BASpec (conceito D8 aplicado à auto-revisão)

Para cada BASpec CRITICAL ou HIGH da entrega, responda:
[ ] "Se esta BASpec estivesse errada, o que seria observável?" — documente o caso de negação.
[ ] "O ENTÃO desta BASpec é verificável por um observador independente?" — se não, reescreva.
[ ] "Existe uma condição em que o QUANDO se satisfaz mas o ENTÃO não deve ocorrer?" — se sim, adicione BASpec de negação.

Se não conseguir responder às três perguntas com âncora de fonte, marque a BASpec como [DECISÃO NECESSÁRIA] — não submeta sem resolução.

### Bloco B — Verificação de viés de confirmação na herança (CC-08)

Quando a spec declara herança (CC-08, EUA-E04):
[ ] Liste explicitamente cada obrigação herdada do canônico pai (ID+versão, RULE-HD-04).
[ ] Para cada obrigação herdada, documente UMA evidência de que ela foi satisfeita nesta spec.
[ ] Verifique que nenhuma obrigação herdada foi silenciosamente removida ou enfraquecida.

Se alguma obrigação herdada não tem evidência de satisfação → achado [DECISÃO NECESSÁRIA].
Este bloco é o substrato que o Revisor usará no Passo 5-bis (§5-bis do revisor.md).

### Bloco C — Verificação epistêmica (RULE-EPI-01..03 / CC-09)

[ ] Cada afirmação causal ("X causa Y", "X garante Y") tem mecanismo declarado (RULE-CAU-01).
[ ] Nenhuma hipótese foi tratada como fato (RULE-EPI-01).
[ ] Onde há incerteza material, o estado INDETERMINADO foi usado em vez de forçar PASS/FAIL.
[ ] Nenhuma probabilidade foi declarada sem evento bem-formado (RULE-PRB-01).
[ ] Nenhuma precisão numérica foi declarada sem base (RULE-EPI-02 anti-falsa-precisão).

### Bloco D — Verificação de escopo (RULE-DEC-01 / INV-05)

[ ] A spec produz recomendação/TMP — não executa (INV-05 / RULE-DEC-01).
[ ] Nenhuma BASpec cruza a fronteira SOT→execução downstream.
[ ] Toda dependência de decisão de Andraus está marcada [DECISÃO NECESSÁRIA] e não como fato.
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

[ ] O Especificador preencheu o Bloco A (casos de negação por BASpec)?
    — Se não preencheu para spec HIGH/CRITICAL: achado Médio (não-bloqueante, mas registrado).
    — Se preencheu: verifique se os casos de negação são plausíveis ou apenas formais.
      "Se esta condição negativa existisse, o sistema detectaria?" — se não, achado Médio.

[ ] O Especificador preencheu o Bloco B (evidências de herança)?
    — Se declarou CC-08 mas não preencheu o Bloco B: achado Médio.
    — Se preencheu: verifique UMA evidência por obrigação herdada.
      Para cada obrigação herdada sem evidência de satisfação: achado Crítico
      (obrigação declarada herdada mas não demonstrada = herança silenciosa).

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
[ ] Existe ao menos UMA afirmação causal sem mecanismo declarado?
    — Se sim: achado Médio (RULE-CAU-01).

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
8. **Que preencheu o §7-bis (Autopré-check Anti-Viés)** — para specs HIGH/CRITICAL,
   exija que o Especificador mostre: (a) pelo menos 1 caso de negação por BASpec
   CRITICAL; (b) evidências de herança por obrigação herdada (se CC-08 declarado).
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

---

## 5. O que NÃO muda `[FONTE]`

- O **fluxo de autoridade** (Especificador → Revisor → Andraus) permanece intacto.
- O **gate determinístico** (`validate_spec_sot.py`) não é alterado — este é o gate estrutural; os novos blocos são semânticos.
- Os **8 passos do Revisor** são preservados; o Passo 5-bis é uma inserção entre Passo 5 e Passo 6, não uma substituição.
- O **Autopré-check §7** é preservado integralmente; §7-bis é adição.
- A **independência estrutural** do Revisor (Write/Edit ausentes, ENF-03) não é tocada.
- Os **invariantes de domínio** (INV-01..10, CC-01..CC-10, 4Es, Salvaguardas) não são alterados.
- A **skill tlc-spec-lean** e o **overlay GUS-TLC-001** não são alterados — apenas o uso da skill é estendido para um segundo momento (auto-revisão adversarial) no Especificador.
- As **atas DHR existentes** não são alteradas (INV-07).
- **CONS-01** respeitado: nenhuma decisão aberta (J-001, L-001 etc.) é tratada como fechada.

---

## 6. Mapa de simetria resultante `[PROPOSTA]`

```
ESPECIFICADOR                          REVISOR
─────────────────────────────          ──────────────────────────────
§3 Skill operacional:                  §3/§4 Interpelação:
  Momento 1: PLAN + CHECKS (spec)        Item 8: exige §7-bis preenchido
  Momento 2: §7-bis adversarial
                                       §5-bis Verificação adversarial:
§7-bis Autopré-check Anti-Viés:          Bloco A: verifica casos de negação
  Bloco A: casos de negação              Bloco B: verifica evidências herança
  Bloco B: evidências de herança         Bloco B': adversarial próprio
  Bloco C: verificação epistêmica        Bloco C: N8–N17 anti-leniência
  Bloco D: verificação de escopo
                                       §5 Passo 5: BASpec + Profundidade
                                         (preservado — verifica o que está)
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
- A incorporação ao `atomic-spec.md` (como extensão do D8) é diferida à SPEC-002/v1.5, junto com as demais emendas em piloto.
- **Escopo retroativo:** regime D-DHR-PAP-001-01 — retroativo-como-auditoria para a SPEC-001 (já coberta pelo piloto EUA-E15); prospectivo-obrigatório para SPEC-002+.

---

## 8. Non-goals `[FONTE]`

- Não cria novo agente nem nova ferramenta determinística.
- Não altera o `validate_spec_sot.py` (gate estrutural permanece como está).
- Não fecha nenhuma decisão aberta (CONS-01).
- Não importa o catálogo operacional do Manual Universal §46 — importa apenas o conceito de contestação estruturada, como PRÁTICA classificada.
- Não substitui o julgamento semântico do Revisor — estrutura-o para reduzir leniência.
- Não torna o Revisor adversarial ao Especificador — torna o processo adversarial à entrega. A relação de cooperação (Especificador §2) é preservada.
- Não cria novo Constitution Check — os blocos §7-bis e Passo 5-bis são procedimentos, não itens do CC.

---

## 9. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| **Q1** | Aprovar a adição do **§7-bis (Autopré-check Anti-Viés)** ao `especificador.md`? | **Sim** — elimina viés de confirmação na auto-avaliação sem alterar o fluxo |
| **Q2** | Aprovar a adição do **Passo 5-bis** ao protocolo de revisão do `revisor.md`? | **Sim** — estrutura o julgamento semântico das N8–N17 e cria simetria com o §7-bis |
| **Q3** | Confirmar que os achados do Passo 5-bis são **Críticos apenas para herança não demonstrada e violação INV-05**, e Médios/Menores nos demais casos? | **Sim** — evita que o novo passo vire gate excessivamente restritivo |
| **Q4** | Aceitar a **obrigatoriedade para HIGH/CRITICAL** e opcional para MEDIUM? | **Sim** — proporcional ao risco; dial GES aplicado (PPQ-001 RULE-PPQ-001) |
| **Q5** | Diferir a **incorporação ao atomic-spec.md** ao piloto da v1.5 (junto com EUA-E04..E14)? | **Sim** — consistente com o regime vigente de incorporação diferida |
| **Q6** | Registrar esta emenda no **CATÁLOGO OFICIAL** e acrescentar entrada no **CONFLICT-MAP** (K-MAN-xx — Manual Universal §46 como PRÁTICA, não normativo)? | **Sim** — INV-07 + disciplina de referências externas |

---

## 10. Fluxo de autoridade

```
[feito] Especificador (chat) redige a PROPOSTA (este arquivo)
   ↓
Andraus valida o diagnóstico e leva ao Claude Code
   ↓
Especificador (Claude Code) formaliza as mudanças nos arquivos dos agentes
   ↓
Revisor SOT emite parecer (CONFORME / NÃO CONFORME)
   contra: especificador.md vigente · revisor.md vigente · atomic-spec.md ·
           RULE-EPI/MET/DEC · CEE-001 §12 · GRE-001/HRE-001 · CONS-01
   ↓
Andraus homologa (decide Q1–Q6)
   ↓
Controlador atualiza CATÁLOGO OFICIAL · CONFLICT-MAP (K-MAN-xx) · RMR-001 (passo 11-bis)
   ↓
Próxima spec (SPEC-002+) é produzida já com §7-bis obrigatório
   e revisada já com Passo 5-bis obrigatório
```

---

## 11. Evidências de suporte (âncoras documentais)

| Afirmação | Evidência | Tipo |
|---|---|---|
| Auto-verificação concentrada no autor | `AUDITORIA-ESTADO-ATUAL §7 item 6`: *"o Especificador é quem roda ambos [spec + verificação-de-spec]"* | `[INFERÊNCIA]` |
| N8–N17 sem check determinístico | `AUDITORIA-ESTADO-ATUAL §13`: *"dependem do julgamento semântico do Revisor"* | `[FATO ESTRUTURAL]` |
| Revisor não usa tlc-spec-lean | `AUDITORIA-ESTADO-ATUAL §7 item 2`: *"Quem deveria usá-la: o Especificador. O Revisor não a usa."* | `[FATO DOCUMENTADO]` |
| Mutations/adversarial da skill não confirmados | `AUDITORIA-ESTADO-ATUAL §7 item 10`: *"[NÃO DETERMINADO]"* | `[NÃO DETERMINADO]` |
| D8 adversarial presente no método | `atomic-spec.md §2`: profundidade D8 = adversarial/negação para CRITICAL | `[FATO DOCUMENTADO]` |
| Contestação estruturada para alto impacto | `Manual Universal §46` — classificado **PRÁTICA** (não normativo) | `[PRÁTICA]` |
| Separação de perspectivas em multiagente | `Manual Universal §44` — classificado **PRÁTICA** (não normativo) | `[PRÁTICA]` |
| CC-08 declarado sem verificação de conservação | `AUDITORIA-ESTADO-ATUAL §12/Q14`: *"não há contrato de herança vertical"* | `[FATO ESTRUTURAL]` |
| Achados de N8–N17 dependem de julgamento | `AUDITORIA-ESTADO-ATUAL §13`: *"obrigações do método sem verificação determinística"* | `[FATO ESTRUTURAL]` |

---

*PROPOSTA não-homologada. Nenhum arquivo do repositório foi alterado. Autoridade literal permanece: `.claude/agents/especificador.md` (PEP-001 v1.2) e `.claude/agents/revisor.md` (PRE-001 v1.1) vigentes. Para homologação: Especificador (Claude Code) deve formalizar as mudanças nos arquivos dos agentes, submetê-las ao Revisor e obter consenso de Andraus (GMC-001 Cap.5).*
