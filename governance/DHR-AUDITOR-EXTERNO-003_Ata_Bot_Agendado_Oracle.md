# DHR-AUDITOR-EXTERNO-003 — Ata — Bot agendado do Auditor Externo (Codex somente-leitura) em VM Oracle Always Free

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisões de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-06 |
| Status | **ATA-PROPOSTA — aguarda assinatura de Andraus.** Registra a decisão de chat e o desenho; **nada está em produção**: o bot só vale depois de merge, instalação e teste em `--dry-run`. Não altera `AGENTS.md`, o Revisor, o ROADMAP nem decisão aberta. |
| Compatibilidade | n/a (operação do piloto de DHR-AUDITOR-EXTERNO-001; nenhuma BASpec, regra ou decisão aberta alterada) |
| Regime | Piloto controlado; aditivo (INV-07). Supera, **apenas para o modo bot**, o item 3 de DIR-002 ("ambiente em nuvem efêmero"): a VM é persistente. DIR-002 segue VIGENTE; eventual DIR-003 é do Orquestrador, após assinatura. |

## 1. Decisões de Andraus `[FATO: chat, 2026-10-06]`
1. Automatizar o atendimento dos pedidos `[AEX-REQ]` com **um bot simples com agendador**, hospedado na **Oracle Cloud (Always Free)**.
2. Automatizar também o lado do Orquestrador: o workflow **comenta no PR** quando um achado é validado e quando o ACK chega, e o Orquestrador configura uma **rotina agendada** (após o bot estar no ar).
3. Autenticação do Codex pela **conta ChatGPT** (sem chave de API). O caminho B (GitHub Action com chave de API) fica como proposta não adotada.

## 2. Desenho `[INFERÊNCIA do orquestrador]`
- systemd timer (~20 min): `sync_auditor.sh` (âncora fora do repositório; exit 0) → `auditor_bot.py`. Sem pedido: não chama o modelo.
- `codex exec --sandbox read-only --ephemeral --ignore-user-config --ignore-rules --cd <commit auditado> -o <saída> -`, **sem `SOT_*`/`GIT_CONFIG*`/`GITHUB_*` no ambiente do modelo**. O modelo devolve só JSON (DADO).
- O bot (código determinístico): preenche campos de máquina, **varre a saída contra o token e o `auth.json` do Codex** e padrões de credencial, valida cada achado (`validate_finding` via `submit_finding`), posta os válidos como Issues `[AEX]` e dá o ACK. Freios: 6 chamadas/dia, 2 tentativas por pedido, 1 pedido por execução, 10 achados por pedido, timeout, nota única por motivo.
- `poll_requests.py` só aceita pedidos cujo autor é `github-actions`; o pedido carrega `manifest=<sha256>` (calculado pelo workflow) e o `sync_auditor.sh` renova a aprovação do manifesto só se o pedido confirmar.
- Correções de procedimento encontradas ao desenhar: `setup_auditor.sh` e `submit_finding.py` chamavam `verify_access.py` sem `--confirmo-escopo` (o fluxo manual também pararia em "INDETERMINADO"); agora `SOT_CONFIRMO_ESCOPO=1` equivale à flag (declaração de Andraus no instalador).

## 3. Evidências `[FATO]`
Testes locais com API, Codex, setup e gates **simulados**: 11 testes do bot (fluxo completo, dry-run, campos de máquina, vazamento barrado, formato inválido, manifesto divergente, limite diário, sem token, pedido forjado) e 9 do kit passam; `sync_auditor.sh` em 7 cenários. Documentação consultada: modo não interativo do Codex CLI; política de instâncias ociosas da Oracle.

## 4. Limites e `[NÃO VERIFICADO]`
- **Nunca executado de ponta a ponta no GitHub, no Codex real nem em VM:** unidades systemd (`systemd-analyze` indisponível aqui), `codex exec` headless com login de conta, estabilidade de execuções repetidas (há relato aberto de `token_invalidated`), efeito real do sandbox read-only (leitura de arquivos e bloqueio de rede), custo/limite de uso do plano.
- **Segurança residual:** o modelo roda como o mesmo usuário do bot e pode LER o arquivo do token e o `auth.json`; mitigado (token fora do ambiente, sem rede, varredura de saída), **não eliminado**. Separar usuário do SO é melhoria futura.
- **Oracle:** instâncias Always Free ociosas podem ser recuperadas (7 dias com CPU, rede e memória < 20%); um bot que acorda a cada 20 min é "ocioso" por definição. Capacidade A1 pode faltar na região.
- Escopo do token declarado, não provado; ações com o login de Andraus; a cadeia de confiança do kit é a aprovação do manifesto (1ª explícita; renovações confirmadas pelo workflow na `main`).
- Os avisos de PR (`achado`, `ack_aviso`) e o campo `manifest=` do pedido nunca rodaram no GitHub.

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**; o papel do auditor segue **piloto**.

## 6. Classificação RPSA `[INFERÊNCIA do orquestrador — a ratificar por Andraus]`
Fora de escopo dos agentes (§4.1): muda a operação do piloto, não checklist, método nem regra. Registrada em `rpsa-ledger.json` como `em_escopo=false`.

## 7. Registro
- [x] Esta ata · [x] `kit/auditor_bot.py`, `kit/PROMPT-AUDITOR-CI.md`, `kit/install_bot.sh`, `kit/sync_auditor.sh`, testes · [x] workflow (`manifest=`, avisos no PR) · [x] `MANIFEST.sha256` · [x] `CATALOGO-OFICIAL.md`, `rpsa-ledger.json`, mapa · [ ] **assinatura de Andraus — pendente** · [ ] instalação na VM e teste em `--dry-run` — atos de Andraus.

---

**Andraus** *(assinatura pendente)*
