# EUA-E19 — Economia de Tokens na Camada Meta (Especificador/Revisor): Roteamento de Modelo e Proporcionalidade de Leitura (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E19** (emenda aos agentes `especificador.md` e `revisor.md`) |
| Versão | **v2 — trata o parecer do Revisor sobre a v1** (Especificador, Claude Code, 2026-09-21): A-01 (afirmação de "Eficácia preservada" no roteamento do Revisor suavizada para reconhecer risco residual não-garantido) e A-02 (checagem de itens `ATIVADO` do RMR-001 movida para o núcleo sempre-obrigatório, §3.1 — não é mais dispensável junto com a leitura integral do painel) tratados; A-03 (citação D-11/D-12 → D-12) corrigido. |
| Natureza | Emenda dual — (a) roteamento de modelo por papel (Especificador vs. Revisor); (b) extensão do dial GES (RULE-PPQ-001) ao **escopo de leitura obrigatória**, hoje fixo independente de complexidade; (c) uso do carimbo `sincronizado-até` (RPSA/EUA-E16) como **short-circuit** de releitura das atas já incorporadas; (d) registro honesto de uma lacuna de plataforma (não há campo de frontmatter para "esforço de raciocínio" por subagente). Não altera CEE-001, RULE-CEE-002/003 (permanecem escopados ao ORYX/Trilha B), o gate M-02, nem o trio de autoridade. |
| Status epistemológico | **HOMOLOGADA — vigência imediata** (DHR-EUA-E19, Andraus, 2026-09-21; Q1–Q6 = Sim; parecer do Revisor CONFORME na v2, após 1º parecer NÃO CONFORME RECUPERÁVEL sobre a v1 — A-01/A-02/A-03, tratados). Origem: auditoria solicitada por Andraus nesta sessão (2026-09-21), não um rascunho de chat externo — foi direto a `governance/`. Efeitos registrados em `.claude/agents/especificador.md`, `.claude/agents/revisor.md`, `CATALOGO-OFICIAL.md`, `CONFLICT-MAP.md` (K-MAN-22) e RPSA (`sincronizado-até` → DHR-EUA-E19). |
| Autoria | Especificador (Claude Code, Sonnet 5, 2026-09-21) |
| Data | 2026-09-21 |
| Alvo | `.claude/agents/especificador.md` (frontmatter `model:` + §3/§4/§7-bis) · `.claude/agents/revisor.md` (frontmatter `model:` + §0/Passo 0/§4.4) |
| Fundamento no baseline | **CEE-001 §12** (Framework 4Es — Economicidade subordinada a Eficácia; cita cache de contexto/reuso de KV-cache **como mecanismo**, não como mandato universal); **RULE-CEE-002/003** (padrão de roteamento por complexidade e de `InferenceContextEnvelope` cacheável — citados **por analogia metodológica**, seu escopo literal é o ORYX AGENT/Trilha B, ainda não implementado — CEE-001 §1); **RULE-PPQ-001** (dial GES, rigor proporcional ao impacto); **RPSA (EUA-E16)** (`sincronizado-até`); **RULE-MET-01** (não-fabricação — motiva a Ressalva de Plataforma no §2) |
| Princípio-guia | **Economicidade nunca sobe acima de Eficácia — mas onde não há trade-off real (leitura redundante, modelo mal-roteado por papel), deixar de economizar também não é neutro: é desperdício disfarçado de rigor.** A camada meta (Especificador/Revisor) nunca teve uma regra própria de roteamento/proporcionalidade — herdou modelo por *bump* de versão (EUA-E16 D-12/Q6), não por decisão de custo×papel. Esta emenda fecha essa lacuna. |

---

## 0. Origem — auditoria (2026-09-21, mesma sessão)

Esta emenda formaliza os achados de uma auditoria solicitada por Andraus sobre mecanismos de economia de tokens no harness. Resumo dos achados (evidência completa no histórico da sessão, ancorada em arquivo):

1. **CEE-001/RULE-CEE-003 já preveem cache** (`stable_prefix`, `cache_control`/TTL, proibição de reenviar estado completo) — mas o escopo declarado do CEE-001 é o **ORYX AGENT** (`canon/CEE-001…md:35`), isto é, a Trilha B (Elliott/Fibonacci/SMC/ICT/Synthesis via Blackboard), hoje em **fase spec-only** (nada implementado). **Não cobre** o Especificador/Revisor.
2. **A "leitura obrigatória" de ambos os agentes é uma lista fixa**, sem gradação por complexidade (`especificador.md §4 item 1`; `revisor.md` Passo 0) — uma spec LOW lê a mesma lista que uma CRITICAL. O dial GES (RULE-PPQ-001) já existe, mas hoje só modula *profundidade de achado*, não *volume de leitura*.
3. **O carimbo `sincronizado-até` (RPSA) não é usado como sinal de dispensa.** Se o último DHR do CATALOGO-OFICIAL é ≤ ao carimbo do próprio agente, o conteúdo das atas EUA-E04..E18 já está, por definição, incorporado ao arquivo do agente — reabri-las de novo em toda revisão é redundante.
4. **O modelo de ambos (`claude-opus-4-8`) foi herdado por atualização de versão** (EUA-E16, D-12/Q6: *"opus-4-5 → modelo vigente"*), não por uma decisão de roteamento por papel/custo análoga à RULE-CEE-002 (que existe só para a Trilha B).
5. **Operacional (fora do texto normativo):** cada invocação via `Agent` é uma conversa nova, sem memória de invocações anteriores — ao pedir um 2º parecer sobre uma versão corrigida do mesmo artefato, spawnar um agente novo perde o cache de prompt da API; continuar o mesmo agente (quando disponível) preserva parte do contexto.

---

## 1. Ressalva de plataforma (RULE-MET-01 — não-fabricação) `[FATO ESTRUTURAL]`

Antes de especificar a mudança: **o frontmatter de subagente do Claude Code (`.claude/agents/*.md`) não tem, na versão vigente, nenhum campo para configurar "esforço de raciocínio" por subagente.** Campos suportados: `name`, `description`, `tools`, `model`, `permissionMode`, `skills`, `memory`, `maxTurns`, `isolation`, `hooks`, `mcpServers`, `background`, `omitClaudeMd` (fonte: documentação oficial de subagentes do Claude Code). Reasoning effort é parâmetro de API, hoje sem exposição no frontmatter de subagente.

**Consequência:** a decisão de Andraus — *"Especificador usa Opus, esforço médio; Revisor usa Sonnet, esforço alto"* — só pode ser **parcialmente** codificada como configuração persistente (`model:`, sim). A parte de **esforço** não pode ser fixada como config do agente hoje; é registrada aqui como **política operacional** (texto normativo no corpo dos dois agentes, instruindo o padrão a seguir) e como orientação para quem invoca (Andraus/Especificador via Claude Code, ao chamar o Revisor pelo `Agent`/`Task` tool). Isto não é um `[DECISÃO NECESSÁRIA]` sem resposta — é um limite de plataforma documentado, não uma lacuna de especificação.

---

## 2. Mudanças propostas — roteamento de modelo (decisão já dada por Andraus)

| Agente | Modelo (frontmatter, persistente) | Esforço (política operacional, não-persistente) | Racional |
|---|---|---|---|
| **Especificador** | `claude-opus-4-8` (mantido) | **Médio** | Produção/síntese normativa exige o modelo mais capaz (Eficácia primeiro), mas o Autopré-check (§7) + §7-bis (EUA-E18) já estruturam a profundidade formalmente — não é preciso esforço bruto máximo a cada turno para obter o mesmo resultado verificável. |
| **Revisor** | `claude-sonnet-4-6` (alterado de `claude-opus-4-8`) | **Alto** | O Revisor é o agente mais lido/invocado por ciclo de revisão (releitura de baselines a cada parecer) — é onde a Economicidade tem mais alavanca. O **objetivo** é compensar o modelo mais econômico com esforço de raciocínio alto; o gate M-02 (Passo 0, eliminatório), os 8 passos e o Passo 5-bis (EUA-E18) continuam obrigatórios **como processo** e não são relaxados por este roteamento. |

**Ressalva honesta sobre risco residual (correção A-01, parecer do Revisor):** a afirmação acima não pode ser lida como "Eficácia garantida". Apenas a redução de capacidade do modelo (`claude-opus-4-8` → `claude-sonnet-4-6`) é **persistente e garantida** (config de frontmatter); a compensação ("esforço alto") é **política operacional, não-garantível por config** (§1 — não há campo de frontmatter para isso). Processo preservado (8 passos + Passo 5-bis continuam obrigatórios) **não é o mesmo** que qualidade de julgamento semântico preservada — um modelo mais econômico rodando o mesmo checklist pode, em tese, deixar passar uma violação sutil que o modelo anterior capturaria. A emenda aceita esse risco residual conscientemente (é uma troca custo↔capacidade, não uma correção sem custo) e o registra aqui para que Andraus decida Q1 com o trade-off explícito à vista — não como um ganho sem contrapartida.

Este roteamento é, para a camada meta, o equivalente metodológico do que a RULE-CEE-002 faz para a Trilha B (roteamento por papel/complexidade) — **sem estender a RULE-CEE-002 em si**, que continua escopada ao ORYX AGENT (CEE-001 §1). É uma regra **nova**, própria da camada meta, motivada pela mesma hierarquia 4Es.

---

## 3. Mudanças propostas — proporcionalidade de leitura (extensão do dial GES)

### 3.1 Núcleo sempre obrigatório (não-negociável, qualquer complexidade)

`ROADMAP.md` · `atomic-spec.md` · `governance/RULES.md` — preserva integralmente o gate M-02 (regra eliminatória; nenhuma complexidade dispensa isto). **Inclui também a checagem de itens `ATIVADO` do `backlog/RMR-001_Painel_Backlog.md`** (correção A-02, parecer do Revisor): isso é gate (passo 11-bis do ROADMAP §23), não leitura de baseline — um item `ATIVADO` pendente é achado de gate independentemente da complexidade, e por isso não pode ser dispensado junto com a leitura integral do painel. A checagem é rápida (procurar `ATIVADO` no arquivo ou no índice do CATALOGO), distinta de ler o painel inteiro.

### 3.2 Lista completa — obrigatória para HIGH/CRITICAL; opcional para MEDIUM; dispensável para LOW

`governance/CONFLICT-MAP.md` · `governance/MAN-001_…md` · `governance/CATALOGO-OFICIAL.md` · **leitura integral** de `backlog/RMR-001_Painel_Backlog.md` (além da checagem de `ATIVADO`, que é núcleo — §3.1) · atas `EUA-E04..E18` individuais.

Para **LOW/MEDIUM** sem ambiguidade declarada, a leitura do núcleo (§3.1, incl. checagem de `ATIVADO`) + `CATALOGO-OFICIAL.md` (índice, arquivo pequeno) é suficiente — o Especificador/Revisor só abre o restante se o índice, o núcleo, ou algum item `ATIVADO` indicarem necessidade (ex.: a spec toca herança CC-08 → abre a ata EUA-E04; toca complexidade HIGH/CRITICAL → lista completa por definição).

### 3.3 Short-circuit via RPSA (`sincronizado-até`)

Antes de reabrir as atas `EUA-E04..E18` individualmente: comparar o carimbo `sincronizado-até` do próprio agente com a última linha de DHR registrada em `CATALOGO-OFICIAL.md`. Se **não houver DHR mais recente** que o carimbo, as atas já homologadas até esse ponto estão, por definição da RPSA, **incorporadas ao conteúdo do próprio arquivo do agente** — dispensa reabri-las individualmente. Só reabrir a(s) ata(s) específica(s) se houver DHR novo desde o último sync (nesse caso, o Gate de Sincronização da RPSA já teria sinalizado isso antes de qualquer trabalho).

**Isto não dispensa nunca:** o núcleo (§3.1), nem a própria consulta ao `CATALOGO-OFICIAL.md` (é o arquivo que permite fazer a comparação).

---

## 4. Nota operacional — continuidade de agente em re-pareceres (fora do texto dos agentes)

Quando o mesmo artefato é resubmetido para um novo parecer após correção (ex.: v2 → v3 de uma emenda), **preferir continuar o mesmo agente** (mecanismo de continuação disponível ao orquestrador, quando prático) em vez de instanciar um agente novo — preserva parte do contexto/cache já pago na primeira leitura. Isto é orientação de uso de quem invoca (Especificador/Andraus via Claude Code), não pode ser codificado dentro de `especificador.md`/`revisor.md` (a decisão de como invocar é externa ao agente). Registrada aqui para constar no processo (ver `RMR-001` — não é item de backlog, é nota de procedimento).

---

## 5. O que NÃO muda `[FONTE]`

- **CEE-001, RULE-CEE-002, RULE-CEE-003** não são alterados — permanecem escopados ao ORYX AGENT/Trilha B (spec-only, não implementado). Esta emenda **não estende** essas regras à camada meta; cria uma regra nova, análoga, para a camada meta.
- O **gate M-02** (confirmar acesso ao `RULES.md` vigente) permanece **eliminatório e obrigatório para toda complexidade**, sem excepcionalidade.
- Os **8 passos do Revisor + Passo 5-bis (EUA-E18)** não são relaxados. A economia é de *volume de leitura de baseline*, não de *rigor de verificação*.
- O **fluxo de autoridade** (Especificador → Revisor → Andraus) e a **independência estrutural do Revisor** (ENF-03) não são tocados.
- **CONS-01:** nenhuma decisão aberta é fechada por esta emenda.
- **RULE-MET-01 (não-fabricação):** nenhum campo de frontmatter inexistente é declarado como existente (ver §1).

---

## 6. Non-goals `[FONTE]`

- Não implementa `InferenceContextEnvelope` (RULE-CEE-003) para a camada meta — isso pertence à Trilha B, quando implementada.
- Não cria campo de frontmatter novo nem propõe extensão ao schema de subagente do Claude Code (fora do controle deste repositório).
- Não altera o modelo do Especificador (permanece `claude-opus-4-8`).
- Não fecha J-001/L-001 nem qualquer outra decisão aberta.
- Não torna o Passo 0/M-02 opcional para nenhuma complexidade.

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| **Q1** | Alterar `model:` do `revisor.md` de `claude-opus-4-8` para `claude-sonnet-4-6`? | **Sim** — já instruído por Andraus nesta sessão |
| **Q2** | Manter `model:` do `especificador.md` em `claude-opus-4-8`? | **Sim** — já instruído por Andraus nesta sessão |
| **Q3** | Registrar "esforço médio/alto" como política operacional no corpo dos agentes (não como config persistente, dada a Ressalva de Plataforma §1)? | **Sim** — única forma honesta de refletir a decisão sem fabricar capability |
| **Q4** | Aprovar a extensão do dial GES ao escopo de leitura (núcleo sempre obrigatório; lista completa HIGH/CRITICAL; reduzida LOW/MEDIUM)? | **Sim** — coerente com RULE-PPQ-001 já vigente |
| **Q5** | Aprovar o short-circuit de releitura das atas via `sincronizado-até` vs. último DHR do `CATALOGO-OFICIAL`? | **Sim** — não reduz garantia (RPSA já certifica atualidade) |
| **Q6** | Registrar no CATÁLOGO OFICIAL e no CONFLICT-MAP (K-MAN-22 — CEE-001/RULE-CEE-002/003 citadas por analogia, não estendidas)? | **Sim** — INV-07 + disciplina de referências |

---

## 8. Fluxo de autoridade

```
[feito] Auditoria (Claude Code, nesta sessão) — achados #1–#5 (§0)
   ↓
[feito] Especificador (Claude Code) formaliza a v1 em governance/
   ↓
[feito] Revisor SOT emite 1º parecer formal sobre a v1 →
        NÃO CONFORME RECUPERÁVEL (A-01/A-02 Médios; A-03 Menor)
   ↓
[feito] Especificador (Claude Code) formaliza a v2 tratando A-01/A-02/A-03
   ↓
[feito] Revisor SOT re-emite parecer sobre a v2 →
        **CONFORME** (2 observações Menores, não-bloqueantes)
   ↓
[feito] Andraus homologa (decide Q1–Q6) → **SIM** para todas (DHR-EUA-E19, 2026-09-21)
   ↓
[feito] Especificador (Claude Code) aplica as mudanças a
   `.claude/agents/especificador.md` e `.claude/agents/revisor.md`
   ↓
[feito] Controlador atualiza CATÁLOGO OFICIAL · CONFLICT-MAP (K-MAN-22) · RMR-001
   ↓
[feito] RPSA (EUA-E16): re-sincronizados especificador.md / revisor.md
   (carimbo `sincronizado-até` → DHR-EUA-E19)
```

---

## 9. Evidências de suporte (âncoras documentais)

| Afirmação | Evidência | Tipo |
|---|---|---|
| CEE-001 escopado ao ORYX AGENT | `canon/CEE-001-cognitive-economy-efficiency-v2.0.md:35` | `[FATO DOCUMENTADO]` |
| RULE-CEE-003 exige cache/TTL/stable_prefix | `governance/RULES.md:243-248` | `[FATO DOCUMENTADO]` |
| RULE-CEE-002 roteia modelo por Tipo I–V (Trilha B) | `governance/RULES.md:237-241` | `[FATO DOCUMENTADO]` |
| CEE-001 §12 cita "cache de contexto"/"reuso de KV-cache" como Economicidade | `canon/CEE-001…md:338` | `[FATO DOCUMENTADO]` |
| Modelo dos agentes bump por versão, não por roteamento | `governance/EUA-E16_Sincronizacao_Agentes_PROPOSTA.md:39,124,169` (D-12, Q6) | `[FATO DOCUMENTADO]` |
| Gate M-02 (RULES.md sempre obrigatório) | `.claude/agents/revisor.md` Passo 0; ocorrências em `EUA-E13/E14/E15/E16/HOD-001` | `[FATO DOCUMENTADO]` |
| Frontmatter de subagente não suporta reasoning effort | Documentação oficial de subagentes do Claude Code (consulta desta sessão) | `[FATO DOCUMENTADO]` |
| Dial GES já vigente para rigor (não para leitura) | `governance/RULES.md:333-338` (RULE-PPQ-001) | `[FATO DOCUMENTADO]` |
| RPSA / `sincronizado-até` | `DHR-EUA-E16` | `[FATO DOCUMENTADO]` |
| Último K-MAN antes desta emenda = K-MAN-21 | `governance/CONFLICT-MAP.md` (linha K-MAN-21, DHR-EUA-E18) | `[FATO DOCUMENTADO]` |

---

*HOMOLOGADA — v2, DHR-EUA-E19 (Andraus, 2026-09-21). Reside em `governance/` (Mapa de Pastas: emendas EUA-E* → `governance/`). Efeitos aplicados a `.claude/agents/especificador.md` e `.claude/agents/revisor.md` — ver DHR-EUA-E19 §4 para o detalhe de cada edição. CATÁLOGO OFICIAL, CONFLICT-MAP (K-MAN-22) e RMR-001 (passo 11-bis) atualizados; RPSA re-sincronizou os agentes.*
