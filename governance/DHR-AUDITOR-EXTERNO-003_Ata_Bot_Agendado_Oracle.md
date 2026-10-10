# DHR-AUDITOR-EXTERNO-003 — Ata — Bot agendado do Auditor Externo (Codex somente-leitura) em VM Oracle Always Free

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisões de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-06 |
| Status | **ASSINADA por Andraus (chat, 2026-10-06) — ver Adendo.** Registra a decisão de chat e o desenho; o bot foi instalado e testado na VM (ver Adendo), em piloto. Não altera `AGENTS.md`, o Revisor, o ROADMAP nem decisão aberta. |
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

**Erratum aditivo (2026-10-10, achado AEX-20261010-004 — proposto pelo orquestrador; **RATIFICADO por Andraus no chat, 2026-10-10**):** em `SPEC-038-DATASRC-001`, o **recorte "TradingView como uma das fontes, via adapter"** foi **DECIDIDO** por Andraus em `DHR-DEC-004` §1.2 (2026-10-03); permanece **ABERTA** a **escolha do provedor de dados de máquina**, diferida ao Discovery/benchmark do MASTER (BL-033). A lista acima é o registro à data da assinatura; esta nota não fecha a decisão inteira (CONS-01).

## 6. Classificação RPSA `[INFERÊNCIA do orquestrador — a ratificar por Andraus]`
**Ratificada por Andraus (chat, 2026-10-10) — ver `DHR-AUDITOR-EXTERNO-004`; o texto abaixo é o registro à data da assinatura.**
Fora de escopo dos agentes (§4.1): muda a operação do piloto, não checklist, método nem regra. Registrada em `rpsa-ledger.json` como `em_escopo=false`.

## 7. Registro
- [x] Esta ata · [x] `kit/auditor_bot.py`, `kit/PROMPT-AUDITOR-CI.md`, `kit/install_bot.sh`, `kit/sync_auditor.sh`, testes · [x] workflow (`manifest=`, avisos no PR) · [x] `MANIFEST.sha256` · [x] `CATALOGO-OFICIAL.md`, `rpsa-ledger.json`, mapa · [x] **assinatura de Andraus (chat, 2026-10-06; ver Adendo)** · [x] instalação na VM e testes (dry-run e real) — ver Adendo.

## Adendo (2026-10-06, antes da assinatura) — fatos posteriores que SUPERAM itens de §2 e §4 `[FATO]`
- **Execução real (supera "nunca executado de ponta a ponta"):** instalado numa VM Oracle Always Free `VM.Standard.E2.1.Micro` (x86_64, ~1 GB de RAM, swap de 2 GB criado pelo instalador), Ubuntu 24.04, Codex CLI 0.160.1 com login por conta ChatGPT (`--device-auth`). Passaram: unidades systemd e timer, `sync_auditor.sh` com aprovação explícita do manifesto, `codex exec` sem interface, ciclo completo no GitHub (Issues `[AEX]`, validação do workflow, ACK, avisos no PR, campo `manifest=` do pedido).
- **Resultados:** dry-run: 5 achados válidos; 1º ciclo real: 3 postados, 2 descartados (formato do comando de reprodução); 2º ciclo real (após PR #23): **5 postados, 0 descartados**, 5/5 defeitos plantados, sem falso alarme no item limpo. A repetição do login (`token_invalidated`) **não ocorreu** nas execuções feitas — isto não prova que não ocorrerá.
- **Achados do teste que mudaram o desenho:** (1) o sandbox do Codex falhou na VM (`bwrap: loopback: Failed RTM_NEWADDR`) e o modelo respondeu "auditoria não realizada" com zero achados; o bot tratava isso como normal e daria ACK enganoso → corrigido: resposta `INDETERMINADO`/"auditoria não realizada" vira **BLOQUEIO sem ACK** (PR #19). (2) O dry-run gastava tentativas e repetia a chamada → corrigido (PR #19). (3) O validador recusou, corretamente, um achado cujo comando de reprodução tinha `|` entre aspas → o prompt passou a proibir metacaracteres de shell (PR #23); o validador não foi afrouxado.
- **Mudança de ambiente na VM (decisão operacional):** instalado o pacote `bubblewrap` e definido `kernel.apparmor_restrict_unprivileged_userns=0` (persistente em `/etc/sysctl.d/60-sot-userns.conf`), necessário para o sandbox no Ubuntu 24.04. É um afrouxamento de segurança do kernel numa VM dedicada ao bot; registrado como risco residual.
- **§2, "systemd timer (~20 min)" — SUPERADO:** o intervalo padrão passou a **2 min** (PR #30); sem pedido pendente não há chamada ao modelo (só consulta à API).
- **Continuam válidos:** segurança residual (o modelo roda como o mesmo usuário do bot); recuperação de instância ociosa pela Oracle (o timer de 2 min reduz, não elimina, o risco); custo/limite de uso do plano ChatGPT **não medido**; ações com o login de Andraus; escopo do token declarado, não provado; a aprovação do manifesto da VM precisa ser refeita a cada mudança no kit (renovação automática só quando um pedido do workflow carrega o hash novo — tentativa de renovação por `workflow_dispatch` hoje não gerou pedido).
- Nenhuma decisão aberta foi fechada; a classificação RPSA de §6 **não foi ratificada por esta assinatura** (permanece a ratificar).

---

**Andraus** — *assinada por decisão direta em chat, 2026-10-06 ("assinar atas"); registro feito pelo Orquestrador interno a pedido de Andraus.*
