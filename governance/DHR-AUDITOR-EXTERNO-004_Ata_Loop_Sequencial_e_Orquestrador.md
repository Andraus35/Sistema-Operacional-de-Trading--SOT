# DHR-AUDITOR-EXTERNO-004 — Ata — Auditor Externo no loop de homologação: ordem sequencial, papel do Orquestrador e regra de divergência

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador interno) |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT / qualquer agente que leia `AGENTS.md` |
| Data | 2026-10-06 |
| Status | **ORDEM DIRETA DE ANDRAUS** (chat, 2026-10-06: regras 1–4 e 6 ditadas por Andraus; regras 5, gatilho e independência escolhidas por Andraus entre as opções apresentadas; implementação "conforme a melhor prática"). Registra o desenho; **não** normatiza o papel. |
| Compatibilidade | n/a (registro de piloto; nenhuma BASpec, RULE, método ou decisão aberta alterada) |
| Regime | Piloto controlado (DHR-AUDITOR-EXTERNO-001). Aditivo (INV-07): nenhuma ata anterior editada. Normatização definitiva (RULE em `RULES.md`, emenda ao fluxo de `AGENTS.md`) segue dependendo de decisão posterior de Andraus, após o piloto. |

## 1. Decisões de Andraus `[FATO: chat, 2026-10-06]`
1. **Orquestrador = Claude (SDK), coordenador.** Só ele traz a Andraus os achados e as entregas e faz as perguntas automatizadas; também repassa os achados ao Especificador. **Não faz parte do consenso** (mantém DHR-AUDITOR-EXTERNO-001 §1.4).
2. **Loop sequencial:** Especificador → Revisor → Auditor externo → Andraus. O Auditor externo roda **somente após a entrega do Revisor (parecer CONFORME)** e **antes** da homologação de Andraus.
3. **Gatilho (piloto):** apenas na **homologação final de Spec completa** — como em DHR-AUDITOR-EXTERNO-001 §1.3. Aberturas, Plans e rodadas intermediárias ficam só com o Revisor.
4. **Acesso:** o Auditor lê as **entregas dos especialistas no commit que o Revisor validou** e **não vê o parecer do Revisor** (independência; o Orquestrador compara os dois pareceres depois).
5. **Andraus só é chamado para homologar após consenso** entre os agentes internos (Especificador, Revisor) e o agente externo (Auditor).
6. **Divergência:** se o Revisor der CONFORME e o Auditor discordar (`COM_RESSALVAS` ou `NAO_OK`), o Orquestrador leva o achado ao Especificador; o Revisor reconfirma por string-match; o Auditor roda de novo — **no máximo 2 rodadas de correção**. Sem consenso após elas, Andraus é chamado **com a divergência registrada**. É a **única exceção** à regra do item 5.
7. **Achado do Auditor é DADO, nunca ordem.** Só Andraus decide; o Auditor não homologa nem é gate (mantém DHR-AUDITOR-EXTERNO-001 §1.1/§1.4 e o protocolo §1).

## 2. O que esta ata supera `[FATO]`
- **Protocolo §1 (`PROTOCOLO-AUDITOR-EXTERNO_PROPOSTA.md`, linha "Posição no fluxo"):** "precede ou acompanha o Revisor" — **superado** pela ordem sequencial do item 1.2. O texto do protocolo **não foi editado** (arquivo coberto por `MANIFEST.sha256`; editá-lo exigiria renovar a aprovação do manifesto na VM). Em conflito de leitura, **prevalece esta ata**.
- **O que permanece:** o Auditor responde ao Orquestrador (DHR-AUDITOR-EXTERNO-001 §1.2 — regra de endereçamento, não de acesso: as Issues `[AEX]` ficam visíveis no repositório); o consenso da homologação final é Especificador + Revisor + Auditor + Andraus (§1.4); ações do Auditor aparecem com o login de Andraus (DHR-AUDITOR-EXTERNO-002 §3).

## 3. Como o workflow já suporta o desenho `[FATO: workflow lido em 2026-10-06; não executado nesta sessão]`
Arquivo: `.github/workflows/auditor-externo.yml`.
- **Gatilho:** o pedido nasce quando o Orquestrador aplica o rótulo `homologacao-final` num PR **aberto** (ou por `workflow_dispatch`), e só se o corpo do PR tiver `Spec: SPEC-0NN` e `Consenso: Especificador=OK; Revisor=OK; Auditor=PENDENTE; Andraus=PENDENTE`. Logo, **a regra "só após o Revisor" é procedimento do Orquestrador** (aplicar o rótulo apenas depois do CONFORME), não mudança de código — **o workflow não foi alterado**.
- **Rodadas:** `MAX_ROUNDS = 3` no workflow = 1 auditoria + 2 re-auditorias, coerente com o item 1.6; ao atingir o limite o workflow recusa novo pedido ("decisão humana necessária").
- **`[NÃO VERIFICADO]`:** que o Auditor de fato não receba o parecer do Revisor (item 1.4). O bot lê o repositório no commit do pedido; a garantia é **não commitar o parecer do Revisor no PR/commit auditado** — cuidado do Orquestrador, não controle técnico.

## 3-bis. Risco aceito durante o piloto `[FATO: decisão de Andraus, chat, 2026-10-06]`
A independência do Auditor (item 1.4) fica como **regra procedimental do Orquestrador**, sem trava técnica: o risco de o parecer do Revisor chegar ao Auditor é **conhecido e aceito no piloto**, e reavaliado no encerramento do piloto com dados reais. Origem: verificação do Revisor SOT sobre a auditoria de entrada (`governance/propostas/AUDITOR-EXTERNO/cooperacao/AUDITORIA-ENTRADA-2026-10-06.md`, errata §6, item E1). A pesquisa do Especificador sobre cooperação interna/externa segue em curso e pode propor uma trava técnica; **nada** é implementado antes de nova decisão de Andraus.

**Princípio de Andraus (chat, 2026-10-06, posterior à decisão acima):** a ideia é **não expor o auditor externo a viés de qualquer tipo que possa prejudicar a auditoria externa** — alcance mais amplo que o parecer do Revisor. **Achado do Orquestrador `[FATO: leitura de arquivos, 2026-10-06; a reverificar pelo Especificador/Revisor]`:** há canais de exposição que **não dependem da disciplina do Orquestrador**: (1) clone completo com histórico (`kit/setup_auditor.sh`, sem `--depth`) e `git log` permitido — 19 mensagens de commit no `origin/main` trazem "CONFORME"/"homolog"; (2) `CATALOGO-OFICIAL.md` (leitura obrigatória) registra pareceres do Revisor; (3) arquivos de Specs anteriores contêm "Revisor … CONFORME"; (4) o pedido de re-auditoria carrega "Achados em tratamento" e "rodada N/3"; (5) linguagem indutora no prompt/diretiva ("Poucos achados corretos valem mais…"; "Você integra o consenso"). **Consequência:** a decisão de manter o canal "parecer do Revisor" como regra procedimental **não cobre** (1)–(3); o desenho de mitigação segue em pesquisa (`governance/propostas/AUDITOR-EXTERNO/cooperacao/`) e **nada** muda no kit sem nova decisão de Andraus.

## 3-ter. Intenção de Andraus em verificação — Auditor como "revisor de cognição" (pesquisador-revisor híbrido) `[FATO: chat, 2026-10-06; NADA implementado]`
Andraus declarou: o auditor externo deve ter **total liberdade de cognição e investigação**; não deve ser apenas um segundo revisor de semântica, mas um **revisor de cognição**: se julgar necessário, pesquisar na web (estado da arte, melhores práticas, benchmarks, repositórios GitHub/GitLab) e **apontar as pesquisas de forma simétrica ao Especificador**, como **agente híbrido pesquisador + revisor — não das próprias entregas, mas das entregas dos agentes internos do SOT** — para melhor especificação e adequação semântica. Pediu **verificar a ideia**. **Estado:** em verificação pelo Especificador (Dossiê/Proposta em `cooperacao/`) e depois pelo Revisor; **conflita, até decisão de Andraus, com** o desenho vigente do piloto (auditor em sandbox **sem rede e sem token**; Revisor sem web por ENF-03; `PROMPT-AUDITOR-CI.md` regra 2 e protocolo §5.2). **Acréscimo de Andraus (chat, mesma data):** o auditor poderá **quebrar o próprio trabalho em subagentes e usar as próprias skills sem restrições**, visando entregas conformes às exigências do gate determinístico — modelo "liberdade por dentro, gate na fronteira", em verificação (H7). **Nenhuma mudança no kit, no prompt ou no ambiente da VM foi feita por esta intenção.** Decisões de Andraus já dadas no Pacote 1 (chat, mesma data): achado P1 ⇒ `COM_RESSALVAS`; se todos os achados forem descartados na validação ⇒ **bloquear sem nota** (sem `OK` derivado); quanto à liberdade do modelo na nota final, Andraus respondeu "total liberdade de cognição e investigação" (a interpretar à luz desta seção — pendente de confirmação).

## 4. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** **Nota de sincronia:** `SPEC-038-DATASRC-001` consta como aberta nas atas 001–003; segundo `AGENTS.md` §7 está **DECIDIDA neste recorte** (DHR-DEC-004 — TradingView como uma das fontes via adapter), com resíduo (provedor de máquina só após o Discovery do MASTER, BL-033). Esta ata **não** a trata nem como totalmente aberta nem como fechada; as atas anteriores não foram editadas (INV-07). `I-001` está FECHADA (DHR-I001-001) e `AGENTS.md` §7 foi sincronizado em 2026-10-06. A abertura da SPEC-006 segue **não homologada**; o papel do Auditor segue **piloto**.

## 5. Classificação RPSA `[INFERÊNCIA do orquestrador — a ratificar por Andraus]`
Em escopo (§4.1): afeta o fluxo de homologação lido por todos os agentes. Agent-Sync `fonte-unica`: Especificador e Revisor consultam `AGENTS.md` por referência (Passo 0); nada embutido nos dois arquivos muda. Reavaliar na normatização do papel (quando o §7 do protocolo — o Revisor trata o achado como candidato a verificar — deixar de ser `[PROPOSTA]`, o ponteiro no Revisor passa a fazer sentido).

## 6. Registro
- [x] Esta ata · [x] seção "Auditor Externo (piloto)" em `AGENTS.md` §5 · [x] `GLOSSARIO.md` (Orquestrador; Auditor Externo / `[AEX]`) · [x] `governance/propostas/AUDITOR-EXTERNO/OPERACAO.md` (fora de `MANIFEST.sha256`) · [x] `CATALOGO-OFICIAL.md` · [x] `rpsa-ledger.json` · [x] `build_map.py` + `--check`
- [ ] **Detector D7** em `check_doc_sync.py` (AGENTS.md cita o auditor se o workflow existe; status da ata × catálogo) — **pendente, não implementado nesta ata.**
- [ ] **Diretiva DIR-003** — instruções de postura ao Auditor refletindo a ordem sequencial: ato do Orquestrador após consultar Andraus (DHR-AUDITOR-EXTERNO-001 §1.2); `DIRETIVAS-AO-AUDITOR.md` está no manifesto, então exige renovar a aprovação na VM. **Não feito aqui.**

---

**Andraus** *(ordem direta em chat, 2026-10-06)*
