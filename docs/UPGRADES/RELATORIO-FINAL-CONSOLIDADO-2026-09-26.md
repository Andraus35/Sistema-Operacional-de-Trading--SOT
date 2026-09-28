# Relatório Final Consolidado — o que foi feito no SOT em 26/09/2026

**Para:** Andraus · **Linguagem:** sem jargão técnico (termos técnicos aparecem só entre parênteses, quando ajudam a localizar o arquivo)
**Status:** documento de acompanhamento — não é norma e não altera nenhuma decisão.

---

## 1. Em poucas linhas

Você pediu, no início, uma auditoria para saber se três ferramentas externas (uma memória para agentes, um compressor de contexto e um gerador de mapa) combinavam com o SOT. A auditoria descobriu que **os "guardas" de proteção que o SOT já tinha estavam desligados na prática**, e que a decisão sobre as ferramentas era outra: **nenhuma delas vale a pena agora**.

A partir daí, o trabalho virou em **quatro frentes**:

1. **Consertar os guardas** que já existiam (e o verificador que reprovava uma Spec já aprovada).
2. **Criar três "fiscais" automáticos** (de referências, de gatilhos do backlog e de mapa).
3. **Criar um mapa do projeto** que os agentes usam para se orientar — e **garantir que ele se atualize sozinho**.
4. **Formalizar tudo no padrão do projeto** (proposta, parecer do Revisor, sua homologação, ata, registros).

Nenhuma regra de trading, nenhuma decisão em aberto e nenhum poder dos agentes foi alterado.

---

## 2. Como ler as classificações

| Etiqueta | O que significa | Confiabilidade |
|---|---|---|
| 🔧 **DETERMINÍSTICA** | Feita por **programa**. Nas mesmas condições, dá **sempre o mesmo resultado**, não depende de o agente "lembrar" ou "interpretar". | Alta e **testável** — foi testada com testes automáticos. |
| 🎲 **PROBABILÍSTICA** | Depende de um **agente de IA ler um texto e decidir segui-lo**. Aumenta a **chance** de o comportamento certo acontecer, **sem garantir**. | Média — vale como orientação, não como garantia. |
| 📋 **DOCUMENTAL** | Registro de governança (atas, catálogo, backlog). **Não muda comportamento sozinho**, mas dá lastro e rastreabilidade. | Não se aplica. |

> Regra de ouro adotada: **onde algo precisava ser garantido, usei mecanismo determinístico**; o texto para agentes (probabilístico) ficou como reforço e explicação, nunca como única defesa.

---

## 3. As alterações, uma a uma

### 🔧 A. Alterações DETERMINÍSTICAS (programas e automações)

| # | O que é, em palavras simples | Comportamento ANTES | Comportamento DEPOIS |
|---|---|---|---|
| **A1** | **Guardas de proteção ao editar** (impedem escrever, nas Specs e regras, frases que violam a Constituição: "ICT pode criar hipótese", "R:R abaixo de 1:3 é aceitável", "SMC corrige Elliott") | **Existiam, mas não funcionavam.** O programa esperava o aviso do Claude Code em um formato que o Claude Code não usa; na prática **nunca via nada** e **nunca bloqueava**. Testei: uma frase claramente proibida passava sem problema. | **Funcionam de verdade**: leem o aviso no formato certo, entendem caminhos do Windows, e **bloqueiam** as três violações. Também **não bloqueiam quando a frase só cita a regra** ("SMC *nunca* corrige Elliott" — texto que já está na Constituição e seria barrado por engano). |
| **A2** | **Conferência da estrutura das Specs** (a regra que impede tratar uma decisão *aberta* como se fosse *fechada*) | A **SPEC-019, já aprovada por você**, **reprovava** nessa conferência: o programa confundia "decisão fechada" (L-001) com "decisão aberta sem aviso". Havia contradição entre o catálogo (aprovada) e o verificador (reprovada). | O verificador **reconhece as decisões fechadas** registradas no ROADMAP. A SPEC-019 passa. **Continua barrando** quem trata uma decisão realmente aberta (como o J-001) como se estivesse fechada. |
| **A3** | **Fiscal de referências** (`check_refs.py`) — confere se tudo que os documentos citam (regras, Specs, atas, arquivos) **de fato existe** | **Ninguém conferia.** Uma citação errada podia ficar meses sem ser notada. | Varre os 148 documentos e classifica em **ERRO** (quebra em documento vivo), **AVISO** e **INFO** (histórico congelado, que não se mexe). **Encontrou um problema real** (a ata "DHR-PRA-001", ver §5). Hoje: **0 erros, 0 avisos**. |
| **A4** | **Fiscal de gatilhos do backlog** (`backlog_triggers.py`, item BL-006) — diz quais itens do backlog "chegaram na hora" | **Manual**: alguém precisava lembrar de reler o painel a cada aprovação. Itens podiam "vencer" sem ninguém ver. | Relatório automático. **Só decide o que dá para provar por fatos** (Spec aprovada, decisão fechada); o que depende de julgamento humano fica marcado como "**verificação manual**". **Nunca promove nada sozinho** — a promoção continua sendo sua. |
| **A5** | **Gerador do mapa do projeto** (`build_map.py`) | Não havia visão geral navegável. O grafo do Understand-Anything, que existia em `UPGRADES/`, tinha **zero ligações entre arquivos** — só listava arquivos. | Gera `docs/mapa/`: **148 documentos e ~1.000 ligações** entre eles, com camadas por pasta, os IDs mais citados (com o documento que os define), a cadeia de Specs (aprovada / em redação / planejada) e documentos que ninguém cita. |
| **A6** | **Atualização automática do mapa** (o que garante o seu pedido: "todos os agentes atualizam o mapa") — ver §4 | Não existia mapa; portanto nada a atualizar. | O mapa **se atualiza sozinho** em quatro momentos: depois de cada edição de documento, ao terminar cada tarefa, ao terminar cada sub-agente e ao abrir uma sessão nova. Se o Python não estiver disponível, **deixa um aviso visível** (arquivo `.stale`) em vez de falhar em silêncio. |
| **A7** | **Barreira final no repositório** (CI e pre-commit) | O CI só validava os esquemas, o lint das Specs e a lista de arquivos. | Passa a rodar também os fiscais. **O do mapa é bloqueante** (se o mapa estiver desatualizado, a entrega não passa); os de referências e gatilhos são **só informativos** (não bloqueiam). |
| **A8** | **Testes automáticos** | 11 testes de esquema + lint. **Nada testava os hooks nem os verificadores.** | **+76 testes novos** (47 de verificadores/mapa/gatilhos, 11 dos guardas, 18 da atualização do mapa). Tudo passa. |
| **A9** | **Atalhos de comando** (`package.json`) | — | `npm run map`, `map:check`, `test:hooks`, `test:py`. |

### 🎲 B. Alterações PROBABILÍSTICAS (texto que os agentes leem)

| # | O que é, em palavras simples | Comportamento ANTES | Comportamento DEPOIS |
|---|---|---|---|
| **B1** | **Regra "atualize o mapa"** escrita para os agentes (AGENTS.md §5 e §8; item no checklist do Especificador; observação do Revisor; regra equivalente para o Cline) | Nenhuma menção ao mapa. | Todo agente é **instruído** a manter o mapa em dia. **Reforço, não garantia**: quem garante é A6/A7. O Revisor (que só lê, não escreve) apenas **observa** se a entrega declara o mapa atualizado. |
| **B2** | **Nota de "orientação rápida"** no AGENTS.md §2 | Agentes buscavam arquivos por conta própria. | Os agentes são **orientados** a consultar o mapa antes de sair procurando — mas ele é **opcional e não-normativo** (em caso de conflito, vale o documento de origem). Fica em `docs/mapa/` e **não na raiz** porque a regra de higiene (HOD-001) só permite ali os documentos de leitura constante. |
| **B3** | **Correção da fonte citada nos agentes** (a "DHR-PRA-001") | Os dois agentes citavam, como base do "contrato de cumprimento", **uma ata que nunca existiu** em nenhum lugar do projeto. | Passam a citar as fontes reais (EUA-E02 v1.2 + tabela ENF do atomic-spec). Você confirmou que não existe ata perdida; o achado foi fechado como "citação sem lastro". |
| **B4** | **Seção de decisões abertas do AGENTS.md (§7)** | Listava a **L-001 como ainda aberta** (embora fechada desde a SPEC-019) e **omitia quatro itens ativos** do ROADMAP. Um agente lendo só o AGENTS.md teria uma visão desatualizada. | L-001 aparece como **fechada** (só na parte de "regras da própria governança"; a parte de "operação em tempo real" continua com a K-001, aberta). Os quatro itens do ROADMAP (SPEC-020-PRINC-001, SPEC-045-RUNTIME-001, RISK-ARR-LOC-001, RISK-CONV-001) passam a constar **como abertos**, com o estado exato do ROADMAP. **Nenhuma decisão foi fechada.** |
| **B5** | **Carimbo de sincronização dos agentes** (`sincronizado-até`, agora "DHR-EUA-E22") | Apontava para a última ata anterior. | Aponta para a ata nova. Esse carimbo é usado pelos agentes para **decidir se precisam reler as atas antigas** — por isso é comportamento influenciado por texto (probabilístico), não por programa. |

### 📋 C. Alterações DOCUMENTAIS (registro de governança)

| # | O que é | Antes | Depois |
|---|---|---|---|
| **C1** | **Emenda EUA-E22** + parecer do **Revisor** (CONFORME) + **ata DHR-EUA-E22** com a sua homologação (Q1–Q4 = Sim) | As edições nos agentes existiam **sem lastro formal**. | Ficam **homologadas e rastreáveis** (proposta → parecer → sua decisão → ata). |
| **C2** | **Catálogo Oficial** | Sem o mapa, sem a EUA-E22. | Linha do mapa (como "gerado, não-normativo") e linhas da emenda e da ata. |
| **C3** | **Painel de backlog (RMR-001)** | BL-006 "em espera"; BL-019 não existia. | **BL-006 Absorvido** (o fiscal de gatilhos cumpriu o combinado); **BL-019 criado, ativado e Absorvido** (o mapa). Único item ainda ativo: **BL-008**. |
| **C4** | **Registro de Higiene (RCH-001, Ciclo #3)** | — | Registra os achados e cada decisão sua, em adendos que **só acrescentam** (nada foi apagado ou reescrito). |
| **C5** | **Relatórios em `UPGRADES/`** | Auditorias antigas de plugins. | + relatório de compatibilidade, proposta de registro e este relatório final. |

---

## 4. "Todos os agentes atualizam o mapa" — como isso foi garantido

Sua exigência foi *garanta isso*. Um texto pedindo "por favor atualizem" (probabilístico) **não é garantia**. Por isso foram construídas **cinco camadas**, da mais forte para a mais fraca:

| Camada | Tipo | Quando age | Cobre |
|---|---|---|---|
| 1. **Barreira final** (CI / pre-commit) | 🔧 | Ao entregar/commitar | Qualquer agente ou pessoa, em qualquer ferramenta. **Bloqueia** se o mapa estiver desatualizado. |
| 2. **Atualização após cada edição** | 🔧 | Logo depois de editar um documento | Qualquer agente do Claude Code, inclusive os sub-agentes. |
| 3. **Autocorreção** ao terminar tarefa/sub-agente e ao abrir sessão | 🔧 | Fim de tarefa / início de sessão | O que escapou da camada 2: edições por linha de comando, mover ou apagar arquivos, ou hooks desativados. |
| 4. **Aviso visível** (`.stale`) | 🔧 | Quando não dá para regenerar (ex.: sem Python) | Evita que a falha seja silenciosa. |
| 5. **Regras escritas** | 🎲 | Na leitura dos agentes | Explica o porquê; cobre também o Cline, que não roda os hooks do Claude Code. |

**Prova real:** editei o AGENTS.md e, **10 segundos depois, o mapa foi regravado sozinho**, sem eu rodar nada. Também simulei um computador **sem Python**: o sistema deixou o aviso, não travou o agente, e o CI bloqueou até regenerar.

---

## 5. O caso da "DHR-PRA-001"

- **O que era:** os dois agentes citavam, como fonte do "contrato de cumprimento", uma ata com esse nome.
- **O que se descobriu:** ela **não existe em lugar nenhum** — nem no catálogo, nem em documentos antigos.
- **O que foi feito:** a citação foi trocada pelas fontes reais, **sem criar ata retroativa** (criar uma ata que você nunca homologou seria falsificar histórico). Você confirmou que não há registro externo; o achado foi **fechado como "citação sem lastro"** e registrado no RCH-001.

---

## 6. Sobre as três ferramentas externas (a pergunta original)

| Ferramenta | Para que serve | Veredito | Por quê |
|---|---|---|---|
| **claude-mem** (memória entre sessões) | Lembrar coisas de uma sessão para outra | **Não adotar agora** | Você já tem memória nativa e as **atas** são o histórico oficial. Uma segunda memória criaria duas "verdades" que podem se contradizer. |
| **Headroom** (compressor de contexto) | Reduzir o tamanho do que a IA lê | **Só como piloto isolado, e nunca sobre documentos normativos** | Comprimir com perda pode transformar "decisão aberta" em "fechada" — exatamente o que a regra CONS-01 proíbe. O SOT já economiza por outros meios (EUA-E19). |
| **Understand-Anything** (mapa em grafo) | Mapa do projeto | **Superado pelo mapa próprio** | O grafo dele tinha zero ligações entre arquivos. O mapa novo tem ~1.000 e é **feito sob medida** para as regras do SOT. O arquivo antigo foi **preservado** (nada é deletado). |

---

## 7. O que NÃO mudou (de propósito)

- Nenhuma **regra de trading**: hierarquia Elliott→Fibonacci→Fractal→SMC→ICT, R:R mínimo, limiares de convicção, Conviction Vector, Signal Package.
- Nenhuma **decisão em aberto** foi fechada (J-001 e demais seguem abertas).
- O **Revisor continua sem poder de escrever** (proteção estrutural ENF-03).
- **Modelos e esforço dos agentes** (EUA-E19) intactos.
- **Nada foi apagado.** Só se acrescentou (regra INV-07).
- O **mapa não é norma**: o Catálogo Oficial continua sendo a fonte autoritativa de "onde está o quê".

---

## 8. Limites e riscos que continuam (sem enfeite)

1. **Os guardas de proteção são uma rede de segurança, não um juiz.** Pegam só três tipos de frase; a conformidade real continua vindo do verificador de estrutura e do Revisor.
2. **O bloqueio dos guardas constitucionais foi testado em laboratório** (testes automáticos), **mas não ao vivo** nesta sessão. O que foi provado ao vivo foi a atualização do mapa.
3. **O CI no GitHub não foi executado** — só verifiquei que o arquivo de configuração é válido. A primeira execução real pode revelar ajustes.
4. **Fora do Claude Code** (por exemplo, o Cline ou uma edição manual), os automatismos das camadas 2–3 **não rodam**; ali valem a regra escrita e a barreira final.
5. **Precisa de Python** instalado para regenerar o mapa; sem ele, o aviso aparece e a barreira final bloqueia.
6. **Cada edição de documento leva ~2–5 segundos** a mais (regeneração do mapa). Custo aceito.
7. **O mapa reflete citações em texto** e só lê arquivos `.md`; "documento sem citação" não significa "documento inútil".
8. **Os pareceres do Revisor são de IA** (probabilísticos): um deles apontou um "risco" que na verdade já estava tratado. Conferi por execução e corrigi as contagens na ata.
9. **A exigência do mapa bloqueante no CI** foi a **única exceção** ao princípio "começar sem bloquear". Foi aprovada por você e é reversível em uma linha.

---

## 9. Pendências

| Item | Situação |
|---|---|
| **BL-008** (auditoria retroativa da SPEC-001) | Único item ativo do backlog; **não faz parte deste trabalho**, segue como estava. |
| 9 itens do backlog com gatilho "manual" | Dependem de eventos/marcos que só você declara. Lista com `python scripts/backlog_triggers.py`. |
| Rodar o CI no GitHub pela primeira vez | Recomendado, para confirmar. |
| **Nenhuma pendência bloqueante** | O que você pediu está feito e registrado. |

---

## 10. Onde está cada coisa

**Novos — automações:** `scripts/check_refs.py`, `scripts/backlog_triggers.py`, `scripts/build_map.py`, `scripts/map-sync.js`, `scripts/hook-io.js`
**Novos — testes:** `tests/test-hooks.js`, `tests/test-map-sync.js`, `tests/test_struct10.py`, `tests/test_check_refs.py`, `tests/test_backlog_triggers.py`, `tests/test_build_map.py`
**Novos — o mapa:** `docs/mapa/MAPA-PROJETO.md` (para ler) e `docs/mapa/mapa-projeto.json` (para máquinas)
**Novos — governança:** `governance/EUA-E22_…_PROPOSTA.md`, `governance/DHR-EUA-E22_….md`, `.clinerules/sot-map.md`
**Corrigidos:** `scripts/gate-check.js`, `scripts/post-edit-check.js`, `scripts/validate_spec_sot.py`
**Ajustados:** `.claude/settings.json`, `.github/workflows/ci.yml`, `.pre-commit-config.yaml`, `package.json`, `AGENTS.md`, `especificador.md`, `revisor.md`, `CATALOGO-OFICIAL.md`, `RMR-001`, `RCH-001`
**Relatórios:** `UPGRADES/RELATORIO-COMPATIBILIDADE-PLUGINS-2026-09-26.md`, `UPGRADES/PROPOSTA-REGISTRO-HYGIENE-2026-09-26.md`, este arquivo

**Comandos úteis** (para você ou qualquer agente):
- `python scripts/build_map.py` — regenera o mapa · `--check` — diz se está em dia
- `python scripts/check_refs.py` — confere as referências
- `python scripts/backlog_triggers.py` — mostra o que "chegou na hora" no backlog
