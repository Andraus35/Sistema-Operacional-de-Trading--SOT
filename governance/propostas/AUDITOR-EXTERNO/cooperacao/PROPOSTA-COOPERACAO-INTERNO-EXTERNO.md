# PROPOSTA — Cooperação entre agentes internos e Auditor Externo (mediada pelo Orquestrador)

**[PROPOSTA — NÃO NORMATIVO / NÃO HOMOLOGADO]**

| Campo | Valor |
|---|---|
| Autor | Especificador Principal SOT (Claude Code, Opus 4.8) |
| Data | 2026-10-06 |
| Base | `DOSSIE-PESQUISA-COOPERACAO.md` (+ `sources/`) · auditoria de entrada `AUDITORIA-ENTRADA-2026-10-06.md` · DHR-AUDITOR-EXTERNO-001..004 · kit reverificado |
| Natureza | Proposta de governança de piloto. Não é Spec, não é RULE, não altera o fluxo de 3 posições nem o piloto sem homologação de Andraus. |
| Decisão | **`[DECISÃO NECESSÁRIA]`** — tudo aqui é insumo ao Orquestrador→Andraus. Eu proponho; Andraus decide. |

> Cobertura `MANIFEST.sha256` (entrada §0 / OPERACAO §7): **cobertos** = `kit/*` e `DIRETIVAS-AO-AUDITOR.md` (+ AGENTE/BRIEFING) — mexer neles exige **regenerar o manifesto + reaprovar na VM** (`sync_auditor.sh --approve <hash>`, DIR-003). **Não cobertos** = `scripts/`, `.github/`, `.gitattributes`, `OPERACAO.md`, `AGENTS.md`, atas DHR-*. Esta é a fronteira que distingue "proposta barata" de "proposta que custa reaprovação na VM".
>
> **Limite do meu mandato nesta tarefa:** não editei (nem edito) `AGENTS.md`, `ROADMAP.md`, `RULES.md`, `atomic-spec.md`, `canon/`, `CATALOGO-OFICIAL.md`, `kit/`, `MANIFEST.sha256`, `DIRETIVAS-AO-AUDITOR.md`, `.github/`, `.claude/` nem atas DHR-*. Onde a proposta recai sobre esses arquivos, **descrevo** a mudança; a edição é ato de quem Andraus designar.

---

## 0. Classificação de complexidade e perfil de profundidade (AGENTS.md §4 — sem elevar em silêncio)

- **Como conjunto**, uma eventual normatização desta cooperação é **HIGH** (toca o fluxo de homologação/consenso, enforcement/ENF-03, segurança de isolamento). Perfil: **standard, D0–D7**. **Não** a classifico como CRITICAL (não é componente analítico nem motor de convicção; não toca invariante de trading).
- **Item a item**, a maioria é **LOW–MEDIUM** (detectores, rótulos, config, geração de lista). Declaro a complexidade por item na tabela de cada proposta.
- **Importante:** se Andraus quiser **normatizar** (não apenas ajustar o piloto), isso vira matéria de abertura própria sob RULE-ECC-01/02 (Dossiê + homologação) — este documento **não** substitui essa abertura.

---

## 1. Veredicto da pesquisa sobre P1..P8 (confirma / refuta / refina)

> Para cada: **o que o estado da arte diz** · problema · evidência (ID) · 4Es (Eficácia>Efetividade>Eficiência>Economicidade) · onde no repo · toca manifesto? · depende de Andraus?

### P1 — Detector do consenso (Detector, não Gate; script em `scripts/`)
- **Estado da arte: CONFIRMA e REFINA.** SRC-HITL-01: use "deterministic logic... as the authoritative signal" e mantenha registro auditável com identidade+timestamp. Um detector que lê o corpo do PR (`Consenso:`/`Auditor=`) e aponta divergência é exatamente o "andaime determinístico" (ENF-03). **Refino:** é **Detector**, nunca Gate — o workflow de merge só AVISA hoje (entrada §3) e deve continuar assim no piloto; quem bloqueia é Andraus.
- **Problema:** a "metade interna" do loop é não-determinística; nada em `scripts/`/CI lê `[AEX]` nem o estado de consenso (entrada §3).
- **Evidência:** SRC-HITL-01 `[EXTERNO]`; ENF-03 `[FATO]`.
- **4Es:** Eficácia alta (fecha um gap de rastreabilidade do loop); Economicidade boa (um script no molde `check_doc_sync.py`). Risco: virar "gate de fato" se alguém o tratar como bloqueante — mitigar com rótulo informativo.
- **Onde:** novo `scripts/check_aex_consensus.py` (**não** coberto pelo manifesto) + o já-existente hook `Stop/SubagentStop` (padrão BL-019). Eu descrevo; não escrevo código (fase spec-first).
- **Toca manifesto?** Não (vive em `scripts/`).
- **Andraus?** Sim — criar script é mudança de processo do piloto. `[DECISÃO NECESSÁRIA]`.

### P2 — Rótulos de disposição `aex-confirmado/parcial/descartado`
- **Estado da arte: CONFIRMA.** SRC-HITL-01 pede "auditable record" da decisão de revisão. Hoje a disposição CONFIRMADO/PARCIAL/DESCARTADO/DUPLICADO existe só como string em `kit/loop_tools.py:93`, sem rótulo/campo/leitor (entrada §3.3).
- **Problema:** a disposição do Revisor sobre cada achado `[AEX]` não é registrada de forma legível por máquina → o "dissenso registrado" (DHR-AUDITOR-EXTERNO-004 §1.6) fica informal.
- **Evidência:** SRC-HITL-01 `[EXTERNO]`; DHR-AUDITOR-EXTERNO-004 §1.6 `[FATO]`.
- **4Es:** Eficácia média-alta; Economicidade alta (3 rótulos GitHub + aplicação pelo Orquestrador). Risco: rótulo aplicado por humano/Orquestrador, não pelo auditor (o auditor é read-only — nunca rotula a própria disposição).
- **Onde:** config de rótulos no GitHub (ato de Andraus) + procedimento em `OPERACAO.md` (**não** coberto). Opcional: leitor no detector P1.
- **Toca manifesto?** Não.
- **Andraus?** Sim (criar rótulos é ato dele, como os 7 atuais). `[DECISÃO NECESSÁRIA]`.

### P3 — Re-auditoria automática em novo commit com `[AEX]` aberto
- **Estado da arte: CONFIRMA com ressalva.** SRC-HITL-01: parada + escalonamento são necessários; re-rodar sem limite recria o anti-padrão de "stall indefinido" e alimenta o risco de "consenso por cansaço" (Dossiê Q3). **Refino:** re-auditoria só dentro do `MAX_ROUNDS=3` já existente; nunca ilimitada.
- **Problema:** hoje re-auditoria só por `workflow_dispatch` manual (entrada §3.4) — fricção que pode levar a pular a re-verificação.
- **Evidência:** SRC-HITL-01 `[EXTERNO]`; `MAX_ROUNDS` `[FATO: workflow]`.
- **4Es:** Eficácia média; Eficiência boa (menos passo manual). Risco: gatilho automático em `.github/` que eu **não posso editar** (limite) e que consome chamadas do modelo (freio de 6/dia) — tratar com cuidado.
- **Onde:** `.github/workflows/auditor-externo.yml` (**não** coberto pelo manifesto, mas **fora do meu mandato de edição**) — apenas descrevo.
- **Toca manifesto?** Não.
- **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`. **Recomendação:** adiar até o piloto da SPEC-006 exercitar o fluxo manual ao menos uma vez (fechamento por merge nunca foi exercitado — ata 002/003).

### P4 — Piso de veredito por código (P0 válido ⇒ `NAO_OK`)
- **Estado da arte: CONFIRMA fortemente.** SRC-HITL-01: o sinal autoritativo deve ser **determinístico**, com o LLM como insumo re-checado. Hoje o veredito vem cru do modelo (`kit/auditor_bot.py:203,229`), sem cruzamento com os achados (entrada §2-L1): um `OK` com P0 postado passa.
- **Problema:** lacuna L1 — veredito probabilístico aceito sem derivação dos achados validados. Isto é um **desvio de ENF-03** ("o LLM é seu próprio gate" de fato, ainda que consultivo).
- **Evidência:** SRC-HITL-01 `[EXTERNO]`; `auditor_bot.py:203/:229` `[FATO reverificado]`; ENF-03 `[FATO]`.
- **4Es:** **Eficácia alta** (corrige incoerência veredito×achados — prioridade máxima na ordem 4Es). Economicidade boa. Risco baixo.
- **Onde:** `kit/auditor_bot.py` (derivar/sobrepor o veredito a partir da contagem de achados P0/P1 validados) **ou** `kit/validate_finding.py`/novo passo no bot. **COBERTO por `MANIFEST.sha256`.**
- **Toca manifesto?** **SIM** → exige regenerar manifesto + **reaprovar na VM** (DIR-003). Custo operacional real.
- **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`. Ver **PN1** (formulação ampliada e preferível).

### P5 — Fixar modelo/esforço e gravar o modelo real
- **Estado da arte: CONFIRMA parcialmente + impõe honestidade.** SRC-REPRO-01: "pinned model version locks the model snapshot", mas temperatura/seed não garantem determinismo; "sampling determinism is not the same thing as system determinism". **Refino:** pinar **reduz deriva**, não garante reprodutibilidade bit-a-bit.
- **Problema:** `MODEL_LABEL` (`auditor_bot.py:34`) é só rótulo e vai para `author.model` (`:218`); `--ignore-user-config` pode deixar modelo/esforço no padrão do CLI (entrada §1) — procedência fraca.
- **Evidência:** SRC-REPRO-01 `[EXTERNO]`; `auditor_bot.py:34/:218` `[FATO reverificado]`.
- **4Es:** Eficácia média (procedência/auditabilidade); Economicidade boa. Risco: o login por conta ChatGPT pode **não** expor modelo/versão/esforço reais → gravar o que houver e marcar o resto **INDETERMINADO** (não fingir pinagem).
- **Onde:** `kit/auditor_bot.py` + `kit/PROMPT-AUDITOR-CI.md` (pedir ao modelo declarar versão) — **COBERTOS pelo manifesto.**
- **Toca manifesto?** **SIM** → reaprovação na VM.
- **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`. Ver **PN5**.

### P6 — Listas de decisões abertas extraídas do `ROADMAP.md`/`AGENTS.md` e conferidas por `check_doc_sync.py`
- **Estado da arte: CONFIRMA.** SRC-OWASP-01 (instruction/data separation) + a disciplina interna RPSA/`check_doc_sync.py` convergem: a lista de decisões abertas que o externo usa deve ser **gerada da fonte de verdade**, não mantida à mão.
- **Problema REVERIFICADO (achado meu, reforça a entrada §1):** a lista `CLOSED_CLAIM` em `kit/validate_finding.py:26` está **dessincronizada** em dois sentidos — (i) inclui **`I-001`**, que está **FECHADA** (atomic-spec §12, DHR-I001-001; ROADMAP:267) como se ainda fosse aberta (bug: o regex trataria uma citação de I-001-como-fechada como suspeita CONS-01, quando I-001 já está fechada); (ii) **omite `SPEC-045-RUNTIME-001`**, que é a **única omissão de decisão aberta confirmada** aqui (aberta, AGENTS.md §7). **`SPEC-038-DATASRC-001` NÃO é omissão:** ela está **DECIDIDA neste recorte** (DHR-DEC-004 — TradingView como uma das fontes via adapter, risco ToS assumido por Andraus); o **resíduo** é só o provedor de máquina, após o Discovery do MASTER (BL-033) — não é decisão aberta plena, não entra na lista de omissões. Lista mantida à mão deriva.
- **Drift paralelo (achado de sincronização, NÃO decido — para Andraus):** `AGENTS.md:126` lista `I-001` entre as decisões "Ativas", mas `I-001` está **FECHADA** (DHR-I001-001; atomic-spec:379; ROADMAP:267). Registro como drift documental a encaminhar; **não edito `AGENTS.md`** nem re-decido I-001.
- **Evidência:** `validate_finding.py:26` `[FATO reverificado]`; atomic-spec §12 / AGENTS.md §7 `[FATO]`; SRC-OWASP-01 `[EXTERNO]`.
- **4Es:** **Eficácia alta** (evita o auditor tratar decisão errada como aberta/fechada). Economicidade alta (gerar a lista; detector no molde existente).
- **Onde:** `scripts/check_doc_sync.py` (novo detector D-AEX: compara a lista do kit × decisões abertas do ROADMAP/AGENTS — **não** coberto) **e** a própria lista em `kit/validate_finding.py` + `kit/PROMPT-AUDITOR-CI.md` (**COBERTOS**). Misto.
- **Toca manifesto?** **SIM** na parte do kit → reaprovação na VM; a parte `scripts/` não.
- **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`. Ver **PN7** (formulação unificada). **Nota CONS-01:** corrigir a lista **não** fecha nem abre decisão — apenas alinha o detector à verdade vigente; `I-001` já foi fechada por Andraus (DHR-I001-001), `SPEC-045-RUNTIME-001` segue aberta, `SPEC-038-DATASRC-001` está decidida neste recorte com resíduo (BL-033). Nenhuma delas é re-decidida aqui.

### P7 — Regras mínimas do Revisor na diretiva do auditor
- **Estado da arte: CONFIRMA parcialmente + REFINA com cautela.** Simetria de critérios entre juízes é desejável (SRC-JUDGE-01 mostra que juízes divergem; critérios comuns reduzem variância). **Mas** SRC-JUDGE-01 também mostra viés de concordância: se o auditor receber **o mesmo** checklist detalhado e for instruído a "espelhar o Revisor", perde-se a independência que é o valor dele (DHR-AUDITOR-EXTERNO-004 §1.4). **Refino:** entregar ao auditor as **regras invariantes/constitucionais** (CC-01..CC-12, invariantes, CONS-01, ENF-03) — que são objetivas — **sem** transformá-lo em cópia do Revisor; preservar a independência de julgamento.
- **Problema:** `kit/PROMPT-AUDITOR-CI.md` + DIR-002 não trazem 5-bis, proporcionalidade, N8–N17, ATIVADO, RPSA, Classe D/H/P/C (entrada §1, grep 0 ocorrências).
- **Evidência:** entrada §1 `[FATO]`; SRC-JUDGE-01 `[EXTERNO]`.
- **4Es:** Eficácia média-alta; Economicidade: **custo real** — mexe em `DIRETIVAS-AO-AUDITOR.md` + `PROMPT-AUDITOR-CI.md` (COBERTOS) ⇒ **DIR-003 + reaprovação na VM** (a própria entrada reconhece isto).
- **Onde:** `DIRETIVAS-AO-AUDITOR.md` (nova **DIR-003**) + `kit/PROMPT-AUDITOR-CI.md`. **COBERTOS.**
- **Toca manifesto?** **SIM** → DIR-003 + reaprovação na VM.
- **Andraus?** Sim (DIR-003 é ato do Orquestrador **após consultar Andraus** — DHR-AUDITOR-EXTERNO-001 §1.2). `[DECISÃO NECESSÁRIA]`.
- **Acoplar com E6 (risco Médio ativo):** a mesma DIR-003 deve declarar a **ordem sequencial** da ata 004 (Especificador → Revisor → Auditor → Andraus). Hoje o protocolo §1 ainda diz "precede ou acompanha o Revisor" (texto não editável — está no manifesto) e o `PROMPT-AUDITOR-CI.md` não cita o protocolo (0 ocorrências); DIR-002 §8 manda a diretiva prevalecer em conflito, mas a ordem sequencial só fica inequívoca quando a DIR-003 a escrever. `[FATO: ERRATA E6]`.

### P8 — `.gitattributes` `eol=lf` para `*.sh`/`*.sha256`
- **Estado da arte: fora do escopo de pesquisa LLM; é higiene de ferramenta.** `[INFERÊNCIA]` boa prática amplamente reconhecida (não requer fonte LLM). CRLF no checkout Windows quebra `sha256sum -c` e scripts `bash`.
- **Problema:** entrada §4-P8 — o manifesto hoje confere 22/22 por blobs no `origin/main`, mas um checkout Windows pode reintroduzir CRLF e quebrar verificação/execução na VM.
- **Evidência:** entrada §4 `[FATO declarado]`; `[INFERÊNCIA]` prática Git.
- **4Es:** Eficácia média (robustez cross-OS); Economicidade altíssima (uma linha de config). Risco: alterar normalização de fim de linha pode, em teoria, mudar blobs/hlikelihood de recalcular o manifesto — avaliar antes. **Recomendo verificar** se afeta os blobs cobertos antes de aplicar.
- **Onde:** `.gitattributes` na raiz (**não** coberto pelo manifesto).
- **Toca manifesto?** Não diretamente; **mas pode afetar os blobs conferidos** → verificar.
- **Andraus?** Sim (mudança em arquivo de raiz). `[DECISÃO NECESSÁRIA]`.

---

## 2. Propostas novas justificadas pela pesquisa (`[PROPOSTA]`)

### PN1 — Veredito do auditor = função determinística dos achados validados (amplia P4)
- **Problema:** L1 (entrada §2) — o veredito cru do modelo não é cruzado com os achados. Um `OK` com P0 válido, ou `NAO_OK` sem nenhum achado, passa hoje.
- **Proposta:** o veredito consultivo entregue ao Orquestrador deve ser **derivado por código** dos achados **validados** (ex.: existe P0 válido ⇒ `NAO_OK`; só P2 ⇒ `COM_RESSALVAS`; nenhum ⇒ `OK`). O veredito do modelo vira **mais um campo de dado**, comparado ao derivado; divergência entre eles é ela própria um sinal a registrar. Mantém o auditor consultivo (não é gate — ENF-03).
- **Evidência:** SRC-HITL-01 `[EXTERNO]` ("deterministic logic as the authoritative signal... LLM-assisted classification... that a deterministic layer re-checks"); ENF-03 `[FATO]`.
- **4Es:** Eficácia máxima; Economicidade boa.
- **Onde:** `kit/auditor_bot.py` (**COBERTO** → reaprovação na VM). **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

### PN2 — Conferir existência de `rule_source` (fecha L2)
- **Problema:** L2 — `validate_finding.py:62` só exige `rule_source` string não vazia; o protocolo §5.1 exige que a **regra exista**.
- **Proposta:** conferência determinística de que o `rule_source` citado existe no repo, no molde de `scripts/check_refs.py` (índice de IDs RULE-/INV-/CC-/ENF-/§). Ancora o achado à norma real; reduz alucinação de regra (quote-then-verify).
- **Evidência:** `validate_finding.py:62` `[FATO reverificado]`; protocolo §5.1 `[FATO]`; SRC-OWASP-01/SRC-CSMAD-01 `[EXTERNO]` (verificador determinístico no loop).
- **4Es:** Eficácia alta; Economicidade boa (reusar a lógica do `check_refs.py`).
- **Onde:** `kit/validate_finding.py` (**COBERTO** → reaprovação na VM). **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

### PN3 — Documentar e preservar o desenho sequencial-cego e a heterogeneidade de modelo como mitigação de viés (não mudar — registrar o porquê)
- **Problema:** o valor de rodar o auditor **sem ver o parecer do Revisor** e de usar **modelo de fornecedor diferente** não está justificado por evidência no dossiê de piloto.
- **Proposta:** registrar (em `OPERACAO.md`, **não** coberto) que estas duas escolhas são mitigação **baseada em evidência** de (a) viés de posição/ancoragem e (b) auto-preferência — e portanto **não** devem ser relaxadas (ex.: não "mostrar o parecer do Revisor para acelerar"). É um **invariante de conduta do piloto**, não código.
- **Evidência:** SRC-JUDGE-01 `[EXTERNO]` (auto-preferência + viés de posição); DHR-AUDITOR-EXTERNO-004 §1.4 `[FATO]`.
- **4Es:** Eficácia alta (protege a independência, que é a razão de existir do auditor); Economicidade altíssima (texto).
- **Onde:** `OPERACAO.md` (**não** coberto). **Andraus?** Decisão de registro; recomendo sim. `[DECISÃO NECESSÁRIA]`.

### PN4 — Calibração repetida (N execuções) e amostra maior
- **Problema (corrigido pela ERRATA E2):** a medição existente foi dry-run + **dois ciclos reais com correção de prompt entre eles** (ciclo 2 = 5/5 plantados), **só** contra defeitos plantados. Não é "3/5 de recall" no ciclo 1 (os 2 descartados falharam na **forma** do comando de reprodução, não por recall) — mas também **não** é garantia de confiabilidade: sistema não-determinístico não se mede com poucas corridas, e um ciclo dependeu de ajuste de prompt.
- **Proposta:** antes de confiar no piloto (SPEC-006), rodar o conjunto de calibração (protocolo §8, C-1..C-7) **N vezes** e reportar recall/precisão/falso-positivo **com média e variância**; ampliar o conjunto além dos 5 plantados (ex.: medir contra um gabarito conhecido como SPEC-001 v1.2 — opção já citada em DHR-AUDITOR-EXTERNO-001 §2, não decidida).
- **Evidência:** SRC-JUDGE-01 `[EXTERNO]` (vieses sistemáticos de juiz LLM exigem medição) — alegação carregada; SRC-REPRO-01 `[EXTERNO]` (não-determinismo de sistema: resultado varia entre corridas, logo poucas corridas não medem); atas 002/003 Adendo + ERRATA E2 `[FATO]`. *(A prática de "N-rollout / média+variância" é citada como `[EXTERNO, não-capturado-verbatim]` no Dossiê Q6 — não é alegação carregada; o peso recai sobre SRC-JUDGE-01 + SRC-REPRO-01.)*
- **4Es:** Eficácia alta (confiabilidade antes de usar em Spec real); Eficiência: custa chamadas do modelo (freio 6/dia) → planejar.
- **Onde:** procedimento em `OPERACAO.md` + `kit/selftest.py`/`TESTE-PILOTO-001.md` (selftest no kit é **COBERTO**; descrição em OPERACAO não). **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

### PN5 — Registrar o modelo real + contexto de reprodutibilidade honesto (amplia P5)
- **Proposta:** o cabeçalho de cada auditoria registra commit auditado + última DHR + diretiva vigente + **modelo/versão reais quando expostos pelo CLI**, e **INDETERMINADO** quando não — nunca um rótulo que finja pinagem. Reprodutibilidade declarada como "por contexto fixado", não bit-a-bit (protocolo §6 já diz isso; PN5 o torna um requisito de campo, não só prosa).
- **Evidência:** SRC-REPRO-01 `[EXTERNO]`; `auditor_bot.py:34/:218` `[FATO]`; RULE-MET-01 `[FATO]`.
- **4Es:** Eficácia média; Economicidade boa. **Onde:** `kit/auditor_bot.py` + `PROMPT-AUDITOR-CI.md` (**COBERTOS**). **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

### PN6 — Isolamento de segredo por usuário de SO (reforço de Q5, não é prompt)
- **Problema:** o modelo roda como o mesmo usuário do bot e pode ler o token/`auth.json` (ata 003 §4). Nenhuma regra de prompt resolve isto.
- **Proposta:** registrar como **melhoria de segurança priorizada** (não bloqueante do piloto, mas pré-requisito de qualquer saída de piloto): separar o usuário de SO do modelo vs. do bot; manter token fora do ambiente do modelo (já feito) e a varredura/redação de saída (já feita). SRC-OWASP-01 "least privilege" é o princípio; a camada é SO, não LLM.
- **Evidência:** SRC-OWASP-01 `[EXTERNO]`; ata 003 §4 `[FATO]`.
- **4Es:** Eficácia (segurança) alta; Economicidade: custo de engenharia de VM. **Onde:** VM/instalador `kit/install_bot.sh` (**COBERTO**) + nota em `OPERACAO.md`. **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

### PN7 — Sincronização do "kit de regras" do externo equivalente ao RPSA (unifica P6+P7; responde Q7)
- **Problema:** o conjunto de regras/decisões entregue ao externo vive fora do RPSA e deriva (ver P6 reverificado). Não há fonte externa dedicada (Q7 = `[INFERÊNCIA]` por analogia interna).
- **Proposta:** tratar o material entregue ao auditor (`PROMPT-AUDITOR-CI.md` + listas do validador) como **artefato sincronizável**: (a) gerar as listas de decisões abertas/fechadas a partir do ROADMAP/AGENTS; (b) um detector (`check_doc_sync.py` ou `check_rpsa.py`) acusa divergência entre o kit e a verdade vigente; (c) carimbo tipo `sincronizado-até` no kit. É o RPSA aplicado ao externo.
- **Evidência:** `[INFERÊNCIA]` (analogia RPSA/`check_doc_sync.py`, `[FATO]`); SRC-OWASP-01 `[EXTERNO]` (instruction/data separation). **Limite:** nenhuma fonte `[EXTERNO]` dedicada — **INDETERMINADO** quanto a padrão externo nomeado.
- **4Es:** Eficácia alta (elimina deriva estrutural); Economicidade: parte em `scripts/` (barata), parte no kit (**COBERTO** → reaprovação).
- **Onde:** `scripts/` (detector, não coberto) + `kit/` (**COBERTO**). **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

### PN8 (menor) — Alinhar o piso de citação literal
- **Observação reverificada:** `validate_finding.py:19` exige `MIN_QUOTE = 20` caracteres na citação do achado, enquanto a disciplina de captura verbatim do SOT (RULE-ECC-04) usa **≥100**. Contextos diferentes (o achado cita linha de commit, verificável por string-match; a fonte `[EXTERNO]` cita página web). Não é defeito, mas **considerar** elevar o mínimo do achado reduz achados ancorados em trechos curtos/ambíguos. **Menor**, não bloqueante.
- **Evidência:** `validate_finding.py:19` `[FATO reverificado]`; RULE-ECC-04 `[FATO]`.
- **Onde:** `kit/validate_finding.py` (**COBERTO**). **Andraus?** Sim, se adotado. `[DECISÃO NECESSÁRIA]`.

### PN9 — Controle **técnico** da independência (não só procedural) — ERRATA E1
- **Problema:** a independência "o auditor não vê o parecer do Revisor" é **regra decidida**, mas a garantia é **apenas procedural** (ata 004 §3, `[NÃO VERIFICADO]`): basta o parecer do Revisor estar em algum arquivo do commit auditado para a independência quebrar silenciosamente. Como o viés de concordância (SRC-JUDGE-01) é exatamente o que o desenho combate, depender de disciplina humana é frágil.
- **Proposta (opções, Andraus escolhe):** (a) convenção de caminho — o parecer do Revisor nunca reside no repositório auditado (fica em canal/Issue separado), e um **detector** verifica que o commit auditado **não contém** arquivo de parecer do Revisor antes de liberar o pedido `[AEX-REQ]`; (b) o pedido ao auditor aponta um **subconjunto/árvore** que exclui qualquer parecer; (c) no mínimo, elevar E1 a **item de checklist do Orquestrador** registrado por máquina (não só prosa). (a) é o mais próximo de controle técnico sem dar escrita ao auditor.
- **Evidência:** ERRATA E1 `[FATO]`; SRC-JUDGE-01 `[EXTERNO]`; ata 004 §3 `[FATO]`.
- **4Es:** **Eficácia alta** (protege a premissa central do desenho). Economicidade boa (detector em `scripts/`, molde `check_doc_sync.py`).
- **Onde:** `scripts/` (detector — **não** coberto) + `OPERACAO.md`. **Toca manifesto?** Não. **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

### PN10 — Rodar `backlog_triggers.py` no `run_gates.py` (fecha ERRATA E4)
- **Problema REVERIFICADO:** o gate `ATIVADO` do RMR-001 é declarado **nunca dispensado** (`AGENTS.md` §5), mas `backlog_triggers.py` está em `INFORMATIVOS` (`kit/run_gates.py:10`) e **não** é executado — ausente da lista `gates` (linhas 30–36). O `evidence.json` do auditor não cobre `ATIVADO`.
- **Proposta:** incluir `("backlog_triggers", [py, "scripts/backlog_triggers.py"])` na lista `gates` (como informativo, coerente com o CI). O auditor passa a citar o estado dos gatilhos como evidência — sem virar gate (ENF-03; segue informativo).
- **Evidência:** `run_gates.py:10` vs linhas 30–36 `[FATO reverificado]`; `AGENTS.md` §5 `[FATO]`.
- **4Es:** Eficácia alta (fecha gap de cobertura de um gate não-dispensável); Economicidade altíssima (uma linha).
- **Onde:** `kit/run_gates.py` (**COBERTO** → reaprovação na VM). **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

### PN11 — Protocolo estruturado do auditor equivalente aos passos do Revisor (ERRATA E7)
- **Problema:** o auditor tem prompt de conduta, mas **sem passos eliminatórios ordenados** como o Revisor (Passo 0→8, 4-bis, 5-bis) — pode concluir `OK` sem percorrer o equivalente. E o carimbo de sincronização do auditor (protocolo §6) é **texto livre**, não um campo comparável por máquina como o `sincronizado-até`/`check_rpsa.py` do Revisor.
- **Proposta:** (a) a DIR-003 (ou o `PROMPT-AUDITOR-CI.md`) define um **roteiro mínimo ordenado** que o auditor deve declarar ter percorrido (invariantes → CONS-01/CONST-01 → ancoragem literal → enforcement), espelhando o essencial dos passos do Revisor **sem** copiar seu checklist completo (preservar independência — ver P7/PN3); (b) o parecer traz um **carimbo estruturado** (campos de máquina) comparável por um detector, não prosa. Combina com PN7.
- **Evidência:** ERRATA E7 `[FATO]`; revisor.md §5 (passos) `[FATO]`; SRC-JUDGE-01 `[EXTERNO]` (critérios comuns reduzem variância, mas sem anular independência).
- **4Es:** Eficácia média-alta (reduz "OK por omissão de passo"); Economicidade: parte prompt/diretiva (**COBERTO**), parte detector (`scripts/`, não coberto).
- **Onde:** `DIRETIVAS-AO-AUDITOR.md`/`kit/PROMPT-AUDITOR-CI.md` (**COBERTOS**) + `scripts/`. **Toca manifesto?** SIM na parte do kit. **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`.

---

## 2-bis. Modelo de ameaça de viés (requisito de Andraus, 2026-10-06): canais de exposição × mitigações

> Andraus: *"a ideia também é não expor o auditor externo a viés de qualquer tipo que possa prejudicar a auditoria externa."* Evidência dos tipos de viés (posição, autopreferência, bandwagon, autoridade, verbosidade, sicofância) está no Dossiê §7, com captura verbatim. Andraus **já decidiu** manter, para o canal específico "parecer do Revisor", a **regra procedimental do Orquestrador** no piloto (ata 004 §3-bis). **Achado novo:** os canais (1)–(3) abaixo **vazam o veredito/estado SEM depender dessa disciplina** — são estruturais do clone/leitura, não do cuidado do Orquestrador. Proponho opções; **não decido**.

### Canais de exposição (reverificados por leitura; `[FATO]` salvo nota)
| # | Canal | Âncora reverificada | Viés que induz |
|---|---|---|---|
| 1 | **Clone completo com histórico** — o bot clona sem `--depth` e o sandbox permite `git show`/`git grep` | `kit/setup_auditor.sh:25` (`clone` sem `--depth`), `:30` (`fetch`), `:33` (`checkout --detach`); `kit/PROMPT-AUDITOR-CI.md:21` (permite `git show`, `git grep`). Mensagens de commit com "CONFORME"/"homolog" no `origin/main`: **`[FATO: verificado pelo Orquestrador; não reverificável por mim sem Bash]`** (ex. citado: "…Revisor CONFORME, nao homologada") | ancoragem/autoridade/bandwagon: lê o veredito do Revisor pelo histórico mesmo sem ninguém commitar o parecer |
| 2 | **Leitura obrigatória do `CATALOGO-OFICIAL.md`** | `PROMPT-AUDITOR-CI.md:21` (leitura obrigatória); `CATALOGO-OFICIAL.md` tem **13** ocorrências de "CONFORME" (reverificado por mim) e pode registrar a Spec em auditoria | autoridade/ancoragem no estado de homologação |
| 3 | **Artefatos de Specs anteriores/da Spec auditada** com "Revisor … CONFORME"/"parecer do Revisor" | reverifiquei: **29** arquivos sob `specs/features/` contêm esse texto (ex.: `SPEC-006/ABERTURA.md` — a própria Spec-alvo do piloto) | ancoragem: o veredito aparece dentro do próprio escopo lido |
| 4 | **Pedido de re-auditoria carrega os achados anteriores e a rodada** | `kit/loop_tools.py:62` ("Achados em tratamento (Issues): #refs"), `:66` ("rodada N/3") | confirmação: ancora o auditor nos achados que ele mesmo fez |
| 5 | **Linguagem indutora no prompt/diretiva** | `PROMPT-AUDITOR-CI.md:9` «Poucos achados corretos valem mais que muitos duvidosos.» (empurra recall p/ baixo); `DIRETIVAS-AO-AUDITOR.md:30` (DIR-002 §5) «Você integra o consenso, de forma consultiva.» (pressão de autoridade/consenso) | verbosidade-inversa (sub-reporte) / autoridade / sicofância |
| 6 | **Autoavaliações dentro da própria entrega auditada** (status "homologada"/"CONFORME" no texto da Spec) | irredutível (o auditor precisa ler a entrega) | ancoragem — declarado como limite, não eliminável |

### Tensão central a registrar (barreira de informação)
`[INFERÊNCIA]` Há **conflito direto** entre o que o auditor **PRECISA** ler (AGENTS, ROADMAP, atomic-spec, RULES, RMR-001, WORKFLOW — `PROMPT-AUDITOR-CI.md:21`) e o que **NÃO** deveria ver (veredito do Revisor, estado de consenso/homologação, histórico de commits). Hoje a leitura obrigatória e o clone completo **carregam ambos juntos**. Qualquer mitigação tem de **separar** as duas classes sem tirar do auditor a base normativa — e isso é não-trivial porque o `CATALOGO-OFICIAL.md` (base normativa) **também** carrega "CONFORME". Fonte de apoio: SRC-HITL-01 (sinal autoritativo determinístico; não expor o avaliador ao mesmo conteúdo que contamina) e SRC-OWASP-01 (separar/denotar conteúdo não confiável).

### Mitigações propostas (cada uma: problema · evidência · 4Es · arquivo-alvo · manifesto/DIR-003 · Andraus)

**PN12 — Snapshot "clean-room" sem `.git`.** Problema: canal 1 (histórico de commits vaza veredito). Proposta: o pedido entrega ao modelo uma **árvore sem histórico** — `git archive` do SHA, ou `clone --depth 1` seguido de remoção de `.git`, e o prompt **não** autoriza `git log`/`git show` (hoje autoriza em `:21`). Evidência: SRC-OWASP-01/SRC-HITL-01 `[EXTERNO]`; `setup_auditor.sh:25` + `PROMPT-AUDITOR-CI.md:21` `[FATO]`. 4Es: Eficácia alta (fecha o maior vazamento estrutural); Economicidade boa. Arquivo-alvo: `kit/setup_auditor.sh` + `kit/PROMPT-AUDITOR-CI.md` (**COBERTOS** → DIR-003/reaprovação na VM). Andraus? Sim. `[DECISÃO NECESSÁRIA]`.

**PN13 — Barreira de informação explícita (lista do que ocultar × do que mostrar).** Problema: canais 2–3 (veredito dentro da leitura obrigatória e dos artefatos). Proposta (opções, Andraus escolhe): (a) entregar ao auditor uma **visão filtrada** do `CATALOGO-OFICIAL.md` e dos artefatos (redigir linhas de veredito antes de expor — redação feita por código determinístico, não pelo auditor); (b) um **detector** que acusa, no commit do pedido, presença de "Revisor … CONFORME"/"parecer"/estado de homologação nos arquivos do escopo, para o Orquestrador decidir filtrar; (c) aceitar o canal como risco residual declarado quando a filtragem custar a base normativa. **Tensão declarada:** filtrar o `CATALOGO-OFICIAL.md` sem remover sua função normativa é difícil — pode exigir uma **projeção normativa sem vereditos**. Evidência: SRC-HITL-01/SRC-OWASP-01 `[EXTERNO]`; `PROMPT-AUDITOR-CI.md:21` + 13/29 ocorrências `[FATO]`. 4Es: Eficácia alta, Economicidade média (filtragem custa engenharia). Arquivo-alvo: `scripts/` (detector, não coberto) + possivelmente `kit/` (filtro — COBERTO). Andraus? Sim. `[DECISÃO NECESSÁRIA]`.

**PN14 — Re-auditoria cega + verificação de correção em passe separado.** Problema: canal 4 (viés de confirmação nos próprios achados). Proposta: na re-auditoria, **não** enviar "Achados em tratamento (#refs)" ao modelo; a verificação de que um achado anterior foi corrigido é feita em **passe determinístico separado** (o commit novo ainda casa a citação literal do achado antigo?), não pedindo ao modelo para "reconfirmar". Evidência: SRC-JUDGE-01 (bandwagon/posição) + SRC-SYCO-01 `[EXTERNO]`; `loop_tools.py:62` `[FATO]`. 4Es: Eficácia alta; Economicidade boa. Arquivo-alvo: `kit/loop_tools.py` (**COBERTO** → reaprovação). Andraus? Sim. `[DECISÃO NECESSÁRIA]`.

**PN15 — Neutralizar linguagem indutora do prompt/diretiva.** Problema: canal 5. Proposta: reescrever `PROMPT-AUDITOR-CI.md:9` para separar **precisão** de **recall** sem empurrar para baixo o número de achados (ex.: "cada achado precisa de citação checável; não omita um achado ancorado por medo de errar"); e qualificar a frase da DIR-002 §5 para que "integra o consenso" não vire pressão de concordar (o auditor contribui com juízo **independente**, não com adesão). Evidência: SRC-SYCO-01 (sicofância) + SRC-JUDGE-01 (bandwagon/autoridade) `[EXTERNO]`; `PROMPT-AUDITOR-CI.md:9` + `DIRETIVAS-AO-AUDITOR.md:30` `[FATO]`. 4Es: Eficácia média-alta; Economicidade altíssima (texto). Arquivo-alvo: `kit/PROMPT-AUDITOR-CI.md` + `DIRETIVAS-AO-AUDITOR.md` (**COBERTOS** → DIR-003/reaprovação). Andraus? Sim. `[DECISÃO NECESSÁRIA]`.

**PN16 — Teste de viés A/B como calibração.** Problema: não sabemos *quanto* cada canal enviesa este auditor. Proposta: rodar o conjunto de defeitos plantados **duas vezes** — uma com pistas de veredito ("Revisor=CONFORME" visível) e outra sem — e medir se recall/precisão/severidade mudam. Diferença material = o canal importa e deve ser mitigado; diferença nula (em N execuções) = evidência de robustez. Combina com PN4 (N execuções). Evidência: SRC-JUDGE-01 `[EXTERNO]` (vieses exigem medição); ata 002/003 `[FATO]`. 4Es: Eficácia alta (mede antes de confiar); Eficiência: custa chamadas (freio 6/dia). Arquivo-alvo: `kit/selftest.py`/`TESTE-PILOTO` (**COBERTO**) + `OPERACAO.md`. Andraus? Sim. `[DECISÃO NECESSÁRIA]`.

**PN17 — Manter heterogeneidade de modelo (não relaxar).** Problema: autopreferência (SRC-JUDGE-01) cresce se o auditor for do mesmo modelo que produziu a entrega. Proposta: registrar como **invariante de conduta do piloto** que o auditor externo use modelo de **fornecedor diferente** dos agentes Claude; não "unificar por conveniência". Evidência: SRC-JUDGE-01 `[EXTERNO]`. 4Es: Eficácia alta; Economicidade altíssima (texto). Arquivo-alvo: `OPERACAO.md` (**não** coberto). Andraus? Decisão de registro. `[DECISÃO NECESSÁRIA]`. (Complementa PN3.)

**PN18 — Randomização/dupla ordem de leitura do escopo.** Problema: viés de posição/ordem (SRC-JUDGE-01) — a ordem em que os arquivos do escopo chegam pode enviesar. Proposta: quando o escopo tem múltiplos arquivos, apresentá-los em **ordem aleatória** (ou auditar em duas ordens e comparar estabilidade — liga-se a PN4/PN16). Evidência: SRC-JUDGE-01 `[EXTERNO]` (posição). 4Es: Eficácia média; Economicidade boa. Arquivo-alvo: `kit/loop_tools.py` (montagem de `{{FILES}}`) + `kit/PROMPT-AUDITOR-CI.md` (**COBERTOS**). Andraus? Sim. `[DECISÃO NECESSÁRIA]`.

> **Limite honesto (RULE-MET-01):** estas mitigações **reduzem**, não eliminam, o viés — o canal 6 (autoavaliação dentro da própria entrega) é irredutível, e o A/B (PN16) mede, não corrige. A barreira de informação (PN12/PN13) é a de maior efeito, mas colide com a necessidade de base normativa (tensão declarada). Nada aqui decide; tudo é `[PROPOSTA]`/`[DECISÃO NECESSÁRIA]`.

---

## 3. Síntese de priorização (recomendação — Andraus decide)

| Ordem (4Es) | Item | Por quê primeiro | Custo manifesto/VM |
|---|---|---|---|
| 1 | **PN1 (+P4)** | corrige incoerência veredito×achados = ENF-03 (Eficácia) | SIM |
| 2 | **PN10** | o gate `ATIVADO` do RMR-001 não roda no bot (ERRATA E4) — uma linha | SIM (kit) |
| 3 | **PN9 + PN12/PN13** | independência: canal "parecer" é só procedural (ERRATA E1) **e** os canais 1–3 (§2-bis) vazam veredito pelo clone/leitura sem depender de disciplina — barreira de informação / clean-room (requisito de Andraus 2026-10-06) | PN12/PN13-kit SIM; detectores NÃO |
| 4 | **P6+PN7** | elimina deriva da lista de decisões (erro vivo: I-001 fechada listada; SPEC-045 omitida; ERRATA E5) | parcial |
| 5 | **PN2** | regra citada precisa existir (anti-alucinação) | SIM |
| 6 | **P1+P2** | rastreabilidade do consenso/dissenso (barato, em `scripts/`) | NÃO |
| 7 | **PN3** | preservar independência (texto; protege o valor do auditor) | NÃO |
| 8 | **PN4+P5+PN5** | medir e dar procedência antes de confiar no piloto | SIM (kit) |
| 9 | **PN11 + P7 (DIR-003)** | protocolo estruturado do auditor + ordem sequencial (ERRATA E6/E7), sem copiar o Revisor | SIM (DIR-003+VM) |
| 10 | **PN6** | isolamento de SO antes de sair do piloto | SIM (kit/VM) |
| 11 | **P3, P8, PN8** | adiáveis / higiene / menor | varia |

> **Recomendação de sequência operacional:** começar pelos itens **sem custo de manifesto/VM** (P1, P2, PN3, PN9) e pelos de **maior Eficácia** que justifiquem uma única rodada de reaprovação do manifesto (PN1, PN2, PN10, PN7-kit, P6-kit, P5/PN5) **agrupada** — reaprovar o manifesto na VM uma vez para um lote, não a cada item (Economicidade). **Nada disto deve começar antes do fechamento do ciclo da SPEC-006** (gatilho do piloto — DHR-AUDITOR-EXTERNO-001 §2; SPEC-006 ainda **não aberta**).
>
> **Risco cumulativo de lote (m-03):** agrupar várias mudanças de kit numa única reaprovação **economiza** reaprovações, mas **aumenta a superfície de revisão de um só golpe** — o `MANIFEST.sha256` só atesta integridade de bytes, não corretude; um lote grande torna mais difícil para quem revisa (e para a aprovação do hash por Andraus fora do repo) avaliar cada mudança. Há, portanto, um **trade-off Eficiência × Eficácia**: lotes menores e temáticos (ex.: um lote "coerência de veredito" = PN1+PN2+PN10; outro "procedência/calibração" = P5+PN5+PN4) são preferíveis a um único lote monolítico. Decisão de granularidade do lote = Andraus. `[DECISÃO NECESSÁRIA]`.

---

## 4. CONS-01, invariantes e fronteiras (autodeclaração)
- Nenhuma decisão aberta foi fechada ou tratada como invariante: J-001, N-001, M-001, H-001, G-001, K-001, C-001, WF-D03, ECC-03-001, **SPEC-045-RUNTIME-001** seguem **ABERTAS**.
- `SPEC-038-DATASRC-001`: **DECIDIDA neste recorte** (DHR-DEC-004 — TradingView como uma das fontes via adapter, risco ToS assumido por Andraus); **resíduo** = provedor de máquina só após o Discovery do MASTER (BL-033). Não a trato como totalmente aberta nem como totalmente fechada; **não** a re-decido.
- `I-001` é **FECHADA** por Andraus (DHR-I001-001) — cito o fato apenas para apontar a deriva da lista `CLOSED_CLAIM` (e o drift de `AGENTS.md:126`, que a lista como Ativa); **não** reabro nem re-decido nada; o drift do `AGENTS.md` é achado de sincronização para Andraus.
- O auditor externo permanece **piloto, consultivo, não-gate, não-agente-interno** (DHR-AUDITOR-EXTERNO-001..004). Nada aqui o promove.
- Fase spec-first respeitada: descrevi mudanças, **não** escrevi código de implementação.
- Tudo é `[PROPOSTA]`/`[DECISÃO NECESSÁRIA]`: **eu proponho, Andraus decide (via Orquestrador).**
