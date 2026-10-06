# PROPOSTA — Auditor Externo como "revisor de cognição" (pesquisador-revisor híbrido): parecer e opções

**[PROPOSTA — NÃO NORMATIVO / NÃO HOMOLOGADO]**

| Campo | Valor |
|---|---|
| Autor | Especificador Principal SOT (Claude Code, Opus 4.8) |
| Data | 2026-10-06 |
| Base | `DOSSIE-PESQUISA-AUDITOR-HIBRIDO.md` (+ `sources/`) · ata DHR-AUDITOR-EXTERNO-004 §3-ter/§3-bis · kit reverificado |
| Natureza | Verificação de uma intenção de Andraus (ata 004 §3-ter). Não é Spec/RULE; não muda o piloto sem homologação. |
| Decisão | **`[DECISÃO NECESSÁRIA]`** — eu verifico e proponho; Andraus decide (via Orquestrador). |

> Cobertura `MANIFEST.sha256`: `kit/*` e `DIRETIVAS-AO-AUDITOR.md` são **cobertos** (mexê-los = DIR-003 + reaprovação na VM); `scripts/`, `.github/`, `OPERACAO.md` **não**. Não editei nada fora de `cooperacao/`.

---

## 1. PARECER

**VIÁVEL COM CONDIÇÕES** — porém **NÃO na forma ingênua** ("ligar a rede no mesmo agente que hoje faz a auditoria").

Justificativa em uma frase: a ideia tem valor cognitivo real (um revisor que pesquisa estado da arte amplia a Eficácia da especificação), mas **adicionar web ao agente que já lê o repositório e pode ler o token completa a "lethal trifecta"** (`[EXTERNO, SRC-TRIFECTA-01]`) e **a própria pesquisa é um vetor de viés/alucinação** (`[EXTERNO, SRC-JUDGE-01]` referências fabricadas enviesam o juízo; `[EXTERNO, SRC-CITE-01]` 3–13% de URLs alucinadas) — o que colide frontalmente com o princípio de Andraus "não expor o auditor a viés" (ata 004 §3-ter/§3-bis). Logo, o benefício só é capturável **se** a pesquisa for (a) **separada em fase/privilégio** do segredo e da auditoria e (b) **verificada deterministicamente** (o modelo propõe a citação; o código busca a URL e confere a citação literal). Essas duas condições são o que torna a intenção viável sem contradizer o Pacote 2 (anti-viés).

Classificação de complexidade (AGENTS.md §4, sem elevar em silêncio): **HIGH** (D0–D7, standard) — toca segurança, enforcement e o fluxo de homologação. Normatizar o papel exigiria abertura própria sob RULE-ECC-01/02 (fora do meu mandato aqui).

---

## 2. OPÇÕES (cada uma: descrição · risco · 4Es · toca manifesto/DIR/VM? · depende de Andraus?)

### Opção A — Auditor em DUAS FASES (pesquisa com rede sem segredos → auditoria offline)
- **Descrição:** Fase 1 "pesquisa": contêiner/usuário **separado**, **sem** o token nem `auth.json`, rede com **egress allowlist** (só domínios de pesquisa), sem acesso de escrita; produz um dossiê de pesquisa com citações. Fase 2 "auditoria": **offline** (como hoje, `--sandbox read-only`, sem rede), consome o dossiê da Fase 1 como **DADO** e audita o commit. As duas fases **nunca** coexistem no mesmo processo (quebra a trifecta: nunca há segredo + conteúdo não confiável + rede juntos).
- **Risco:** injeção indireta na Fase 1 (conteúdo web malicioso) ainda existe, mas **sem segredo e sem repo privado** o dano de exfiltração cai muito (SRC-TRIFECTA-01: faltam os outros dois vértices). Risco residual: a Fase 1 pode trazer citação fabricada para a Fase 2 → exige Opção B acoplada. Complexidade operacional alta na VM de 1 GB.
- **4Es:** Eficácia alta (cognição ampliada com trifecta quebrada); Efetividade média (latência maior, 2 fases); Eficiência baixa-média (2 execuções, custo); Economicidade: pesada (ver H6 — pode estourar timeout/limite). 
- **Toca manifesto/DIR/VM?** SIM — muda `kit/` (novo fluxo), ambiente da VM (novo usuário/contêiner, egress), DIR-003. Reaprovação na VM.
- **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`. **INDETERMINADO:** se a VM comporta (H6).

### Opção B — Fetcher determinístico no bot que verifica as URLs/citações que o modelo propõe
- **Descrição:** o modelo **não** navega; ele apenas **propõe** achados de pesquisa com `url` + `captura_verbatim`. Um **fetcher determinístico** (código do bot, **sem** segredos no ambiente, egress allowlist) busca cada URL e confere que a citação aparece **literalmente** na página; se não resolver ou não casar, o achado de pesquisa é **descartado** (fail-closed). É o ENF-03 aplicado à pesquisa (SRC-HITL-01: código é o sinal autoritativo).
- **Risco:** baixo — o fetcher é código determinístico, não um agente; não segue instruções da página (trata HTML como dado, não executa). Resolve diretamente o risco de citação fabricada (SRC-CITE-01) e reduz o viés de autoridade (SRC-JUDGE-01), porque referência não verificada não entra. Risco residual: SSRF/egress — mitigado por allowlist e por rodar sem segredos.
- **4Es:** Eficácia alta (mata citação fabricada por construção); Efetividade alta; Eficiência boa; Economicidade boa (fetch é barato perto de "deep research").
- **Toca manifesto/DIR/VM?** SIM na parte `kit/` (novo validador/fetcher) — reaprovação; egress exige ajuste de ambiente da VM.
- **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`. **É o complemento recomendado de A e de C.**

### Opção C — Manter auditor OFFLINE + passo separado "verificador de fontes" que confere AO VIVO as fontes do Dossiê do Especificador
- **Descrição:** o auditor continua **offline** (sem rede, como hoje). Cria-se um passo determinístico **à parte** (não é o LLM auditor) que, **ao vivo e sem segredos**, busca as URLs do `sources/` do Dossiê do **Especificador** e confere que a citação verbatim casa a página. **Preenche exatamente a lacuna** que o Revisor SOT declarou nesta sessão ("veracidade das páginas não verificável sem web") — sem dar web ao auditor nem ao Revisor (ENF-03 preservado: é código, não LLM).
- **Risco:** o mais baixo das opções que agregam valor — nenhum LLM ganha rede; o verificador é um fetcher determinístico. Não amplia a "cognição" do auditor (não traz estado da arte novo), mas **fecha a lacuna de verificação de fontes**, que é metade do valor pedido.
- **4Es:** Eficácia alta (fecha lacuna real sem abrir superfície); Efetividade alta; Eficiência alta; Economicidade alta.
- **Toca manifesto/DIR/VM?** Pode viver em `scripts/` (verificador do Dossiê do Especificador, **não** coberto) + egress controlado. Menor custo de manifesto.
- **Andraus?** Sim. `[DECISÃO NECESSÁRIA]`. **Recomendada como primeiro passo** (captura valor com risco mínimo).

**Detalhamento operacional da Opção C (OBS-02):**
- **Quem executa:** um **script independente** (`scripts/`, p. ex. `check_sources_live.py`), **não** o LLM auditor nem o Revisor. Recomendo rodá-lo como **passo de CI informativo** (molde `check_refs.py`/`continue-on-error`) **e/ou** como **passo do Orquestrador sob demanda** — nunca como gate bloqueante por conta própria (ENF-03: Detector, não Gate; quem bloqueia é Andraus).
- **Onde entra no fluxo:** sobre o `sources/` do Dossiê do **Especificador**, na fase de revisão (antes/junto do parecer do Revisor) — **não** atrelado ao pedido `[AEX-REQ]` (o auditor híbrido é outra coisa; a Opção C independe dele). Pode também rodar sob demanda quando o Orquestrador quiser conferir um Dossiê.
- **Custo de manutenção / limites técnicos:** URL rot (links que morrem), sites que **bloqueiam bots** (403/429), páginas **só-JavaScript** (conteúdo não vem no HTML), **redirecionamentos** (como o 308 que SRC-CODEX-01 sofreu), paywalls. O fetcher pode dar **falso-negativo por razão técnica, não semântica**.
- **Como tratar o falso-negativo sem virar "não verificável = reprovado":** o resultado por fonte é **tri-estado**, não binário — `VERIFICADO` (a citação casa a página), `DIVERGENTE` (página acessível mas a citação **não** casa → achado real, candidato a Crítica), `INACESSÍVEL-TÉCNICO` (bloqueio/JS/rot/redirect → **não reprova**; registra o motivo técnico para decisão humana). Só `DIVERGENTE` é sinal de problema; `INACESSÍVEL-TÉCNICO` é declarado como limite, coerente com a honestidade já vigente ("veracidade não atestada"). O estado nunca é decidido pelo script como reprovação — é dado ao Orquestrador/Andraus.

**Transferência de confiança (OBS-03):** com a Opção C, o **Revisor permanece offline (ENF-03)** e passa a **confiar na saída determinística do fetcher** em vez de verificar a web por conta própria — isso **desloca** a confiança do Revisor para o fetcher. Mitigação: a saída do fetcher é um **artefato versionado e auditável** por fonte, contendo **URL + data de acesso + hash do conteúdo baixado + a saída literal** (o trecho que casou/não casou) + o tri-estado. Assim o Revisor confere o resultado **por string-match** (dentro do seu mandato, sem web), do mesmo modo que confere a captura `sources/<ID>.txt` — a confiança vai para um **artefato inspecionável**, não para um processo opaco. Limite honesto: o hash prova o que o fetcher **baixou**, não que a página **não foi adulterada na origem** nem que o fetcher viu a mesma coisa que um humano veria (JS/geo/bot-blocking) — risco residual declarado, não eliminado.

### Opção D — Não mudar (auditor permanece revisor offline, sem pesquisa)
- **Descrição:** manter o desenho vigente; a "cognição" de pesquisa continua sendo responsabilidade do **Especificador** (que já pesquisa sob ECC-02/04/06), e o auditor confere semanticamente.
- **Risco:** nenhum novo; mas **não** atende à intenção de Andraus (ata 004 §3-ter) de um revisor de cognição.
- **4Es:** Economicidade máxima; Eficácia de cognição inalterada.
- **Toca manifesto/DIR/VM?** Não. **Andraus?** É o status quo.

---

## 3. RECOMENDAÇÃO (eu proponho; Andraus decide)

**Sequência recomendada: C → B → (A só se Andraus quiser cognição web plena).**
1. **Opção C primeiro** — fecha a lacuna de verificação de fontes (a que o Revisor não cobre) com risco mínimo e sem dar web a nenhum LLM. Captura metade do valor da intenção.
2. **Opção B em seguida** — se/quando se quiser que o auditor **proponha** pesquisa, verificá-la por fetcher determinístico mata a citação fabricada e o viés de autoridade por construção (coerente com o Pacote 2 anti-viés).
3. **Opção A por último e só com decisão explícita** — cognição web plena no auditor, **obrigatoriamente** em duas fases com separação de usuário/segredo + egress allowlist + Opção B acoplada; condicionada a teste de viabilidade na VM (H6 INDETERMINADO).
- **Rejeito** a forma ingênua (rede no mesmo agente com token acessível) — é a lethal trifecta completa.

**Economia de reaprovação do manifesto (responde H5) — com CONTRATO DE INATIVAÇÃO explícito (M-01):** **antes de congelar o esquema do achado** nos Pacotes 1–3, **reservar campos opcionais de pesquisa** no schema do achado (`url`, `data_de_acesso`, `captura_verbatim`, `nivel_de_evidencia`, `relevancia`, tipo de achado `pesquisa`) — **inertes** até Andraus ativar o papel. **Mas reservar NÃO pode significar "o validador aceita em silêncio":** se o schema declarar os campos como opcionais e o validador os aceitar sem checagem, o modelo pode preencher `captura_verbatim`/`url` com texto qualquer (inclusive URL alucinada) e o validador deixa passar — criando **aparência de evidência web-verificada sem verificação alguma**. O contrato de inativação tem de ser **fail-closed**: enquanto o papel de pesquisa estiver INATIVO, campos de pesquisa **não podem** aparecer num achado válido.

Opções do contrato:
- **(a)** `additionalProperties: false` no schema **+** o tipo de achado `pesquisa` como **único** que habilita os campos, e esse tipo é **rejeitado** enquanto o papel não estiver ativado por diretiva.
- **(b)** o validador emite **ERRO** (não só aviso) se qualquer campo de pesquisa aparecer com o papel inativo.
- **(c)** **não** reservar agora — proposta separada quando a ativação for decidida (custo: **nova reaprovação do manifesto/VM**).

**Recomendo (a)+(b) combinadas (defesa em profundidade):** (a) fecha a **forma** (schema não aceita campo inesperado/tipo não ativado), (b) fecha o **comportamento** (validador falha, não avisa). O custo marginal é baixo se feito **junto da rodada já planejada dos Pacotes 1–3** (toca `kit/finding.schema.json` + `kit/validate_finding.py` = COBERTOS → uma reaprovação), e evita a 2ª reaprovação de (c). **4Es:** Eficácia alta (impede evidência-fantasma por construção); Economicidade boa (uma rodada em vez de duas). **Quem ATIVA o papel de pesquisa = Andraus, por diretiva versionada (DIR)** — o flag de ativação é lido pelo validador; **reservar ≠ ativar**. `[DECISÃO NECESSÁRIA]`.

**Condições inegociáveis se qualquer pesquisa for adotada (simetria com o Especificador — H4):**
- Regras do Especificador aplicam-se ao auditor: RULE-ECC-02/04/06, DHR-PROV-WEB-001 §2.1, TRACE-06 (documentado≠homologado). Web = dado; nada vira baseline; achado externo ≠ fato SOT.
- Toda citação de pesquisa só entra **verificada por código** (Opção B): URL resolve + citação literal casa (≥100 chars) + classificada + nível de evidência; senão, descartada (fail-closed). Interage com PN2 (que confere norma interna) de forma complementar.
- Capturas verbatim **não** vão para o corpo da Issue (limite ~100 KB) — vão para arquivo/`sources/` no clone, citadas por referência.
- Papel inalterado (ENF-03): consultivo, não é gate, responde ao Orquestrador; "total liberdade de cognição" = liberdade de investigar/apontar, **não** de decidir/homologar; veredito segue derivado deterministicamente (PN1).
- Pré-requisito de segurança do Pacote 2 (PN6 isolamento de usuário de SO) torna-se **bloqueante** antes de qualquer rede: enquanto o modelo puder ler o token/`auth.json`, nenhuma fase com rede deve existir no mesmo usuário.

---

## 3-bis. H7 — Subagentes e skills "sem restrições, visando o gate determinístico"

**Parecer sobre H7: VIÁVEL COM CONDIÇÕES, sob o modelo "liberdade por dentro, gate na fronteira".** O modelo proposto por Andraus é **compatível com ENF-03** e com SRC-HITL-01 (código = sinal autoritativo; LLM/subagentes = insumo re-checado) — desde que a "liberdade por dentro" seja **cognitiva**, nunca de **privilégio**. A decomposição em subagentes e o uso de skills não mudam o papel consultivo nem o veredito determinístico (PN1); agravam, porém, custo/tempo (VM ~1 GB), vazamento de segredo (cada subagente pode ler o token — ata 003 §4) e viés compartilhado (todos Codex). **Goodhart (H7d):** como o gate mede **forma/ancoragem, não mérito**, "visar o gate" não garante acerto — o Revisor semântico independente + Andraus continuam sendo o teste de mérito; o gate é **necessário, não suficiente**.

### Quadro "o que é LIVRE / o que é FIXO" do auditor híbrido
| Dimensão | LIVRE (liberdade por dentro) | FIXO (gate/fronteira — inegociável) |
|---|---|---|
| Decomposição | Quebrar o trabalho em subagentes; paralelizar; escolher a ordem | Nº de chamadas/tempo/memória dentro do orçamento da VM (6/dia, 1800 s, ~1 GB); registro por subagente (rastreabilidade) |
| Skills | Usar skills para raciocinar/organizar | Procedência da skill; cobertura por `MANIFEST.sha256`; skill não confiável = vetor de injeção (não "sem restrições" de proveniência) |
| Cognição | Como pensa, investiga, estrutura o raciocínio | Não decide, não homologa, não é gate (ENF-03); veredito derivado por código (PN1) |
| Citação | Que evidências busca | Citação literal verificável (≥ limiar), `rule_source` existe (PN2), fonte de pesquisa verificada por fetcher (Opção B) |
| Segurança | — (não há liberdade aqui) | Sandbox read-only, **sem rede**, **sem segredo** para TODOS os subagentes; nenhum subagente abre rede nem lê `~/.codex`/token |
| Saída | Forma e conteúdo do rascunho | Passa por `validate_finding.py` + esquema + comandos de reprodução somente-leitura + manifesto na fronteira |

**Condição-chave (reverificada):** o bot roda `codex exec --ignore-user-config --ignore-rules` (ata 003 §2). Se as skills são user-config (`~/.codex/skills`), essas flags **provavelmente as desligam** — há **conflito** entre "usar skills sem restrições" e as flags de blindagem atuais, e `~/.codex` é o diretório de segredo que o PROMPT regra 2 proíbe ler. **INDETERMINADO** (doc oficial/teste). Opção de desenho: se skills forem adotadas, elas teriam de ser **empacotadas no kit sob o manifesto** (procedência controlada), não puxadas do `~/.codex` do usuário — senão a blindagem e a liberdade colidem. `[DECISÃO NECESSÁRIA]`.

**Impacto nos Pacotes:** reforça PN1 (fronteira determinística), PN6 (isolamento de SO — agora mais crítico), PN17 (heterogeneidade vs viés compartilhado) e a **reserva de campos no schema** (congelar uma vez). Ortogonal à web: vale mesmo offline.

---

## 4. 5 pontos de honestidade (RULE-MET-01)
- A pesquisa web **aumenta** a cognição **e** o risco de viés/alucinação ao mesmo tempo; só vale com verificação determinística acoplada.
- A lacuna que o híbrido cobriria (verificar fontes ao vivo) é real e é **melhor resolvida por código** (Opção C/B) do que por um LLM com web.
- H3 (modos de rede do Codex), H6 (a VM comporta?) e H7 (suporte oficial a subagentes/skills no exec; efeito de `--ignore-user-config` sobre skills) estão **INDETERMINADOS** — não afirmo viabilidade técnica sem teste/captura; as fontes de subagentes/skills que achei são **comunitárias não-oficiais** e não foram capturadas verbatim.
- Nenhuma decisão aberta foi fechada; nada vira baseline; não editei kit/atas/AGENTS.
- Tudo é `[PROPOSTA]`/`[DECISÃO NECESSÁRIA]`: **eu verifiquei e proponho; Andraus decide.**
