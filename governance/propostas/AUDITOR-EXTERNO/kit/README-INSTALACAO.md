# Kit do Auditor Externo — instalação e acesso  `[PROPOSTA — NÃO HOMOLOGADO]`

Decisões de Andraus (chat, 2026-10-05): **canal** = Issue com formulário · **credencial** = **token fine-grained do próprio Andraus** com escopo mínimo (Contents:Read + Issues:Read/Write, só este repositório) — emenda 2026-10-05: o papel *Read* é inviável em repositório pessoal (colaboradores têm só escrita) · **hierarquia** = o auditor é **subordinado ao Orquestrador interno e se reporta só a ele** (o Orquestrador, a Andraus; **nunca** o auditor a Andraus/Especificador/Revisor) · **postura** = só por diretiva versionada do Orquestrador, após consulta a Andraus (`../DIRETIVAS-AO-AUDITOR.md`) · **nuvem** = tudo roda em ambiente em nuvem · **`git pull`** só em pedido gerado quando um PR de **homologação final de Spec completa** (consenso: **Especificador + Revisor + Auditor externo + Andraus**; o Orquestrador coordena e não é parte do consenso) fica candidato · **piloto controlado** (alvo SPEC-006). O GPT é **auditor externo** (não é agente interno nem gate). Nada neste kit altera `AGENTS.md`, o Revisor, o ROADMAP, specs ou canon; instalar o formulário em `.github/` é ato de Andraus.

## O que o kit contém (todos testados localmente: ver "Verificação")
| Arquivo | Função |
|---|---|
| `setup_auditor.sh` | clona **somente leitura**, desabilita push/hooks, fixa o commit, instala deps sem scripts, roda a calibração |
| `verify_access.py` | **fail-closed**: aborta se a credencial tiver `push`/`admin`/`maintain` |
| `run_gates.py` | roda os gates determinísticos do repositório e grava `evidence.json` (commit, exit codes, hash das saídas); falha se a árvore mudar |
| `selftest.py` | calibração com **defeitos plantados** (1 válido + 8 inválidos com código esperado) |
| `finding.schema.json` / `finding.example.json` | forma do achado (JSON) e exemplo real |
| `validate_finding.py` | valida forma e **citação literal** (string-match no commit); detector, não gate |
| `submit_finding.py` | único canal de saída: cria Issue `[AEX] …` (dry-run por padrão; `--post` posta) |
| `ISSUE_TEMPLATE-auditoria-externa.yml` | formulário web da Issue (instalar em `.github/ISSUE_TEMPLATE/`) |
| `INSTRUCOES-OPERACIONAIS-GPT.md` | procedimento determinístico passo a passo para o GPT |

## A. Ações de Andraus (uma vez) — o que eu NÃO posso fazer por você
1. **Conta dedicada** do GitHub para o auditor (ex.: `sot-auditor-externo`), separada da sua, para que as Issues tenham autoria própria.
2. **Convidar como colaboradora com papel `Read`** (Settings → Collaborators → Add people → Role: Read). *Read* lê o repositório e abre/comenta Issues; **não dá push**.
3. **Token da conta do auditor** (feito logo pelo auditor, na conta dele). Tente primeiro **fine-grained** (Contents: Read-only, Issues: Read and write, Metadata: Read, restrito a este repositório). **Atenção (não verifiquei a UI atual do GitHub):** fine-grained pode não permitir repositório de *outra conta pessoal*; se for o caso, use **classic** com escopo `repo`. Em qualquer caso o teto de poder é o **papel Read** da conta, e `verify_access.py` recusa a credencial se ela tiver `push`.
   *Alternativa mais restrita (opcional, mais trabalho):* GitHub App instalado só neste repositório com Contents: read + Issues: write.
4. **Rótulo** `auditoria-externa` (Issues → Labels → New). Quem tem papel *Read* não consegue rotular via API; o **Orquestrador** aplica o rótulo na triagem. Os achados são identificáveis pelo prefixo de título **`[AEX]`**.
5. *(Opcional, após homologar o papel)* copiar `ISSUE_TEMPLATE-auditoria-externa.yml` para `.github/ISSUE_TEMPLATE/auditoria-externa.yml` por PR normal (CI + Revisor).
6. **Não conceder** push, admin, Actions-write, nem acesso a outros repositórios. Rotacione/revogue o token se vazar.
7. **Loop automático (workflow `.github/workflows/auditor-externo.yml`)** — entra no repositório por PR normal e fica **inerte** até você definir, em Settings → Secrets and variables → Actions → **Variables**: `AUDITOR_EXTERNO_ENABLED = true` (chave de desligamento: apague ou ponha `false` para parar tudo) e `AUDITOR_EXTERNO_LOGINS = <login da conta do auditor>` (só Issues `[AEX]` desse login são validadas). Crie os rótulos: `auditoria-externa`, `homologacao-final`, `aex-valido`, `aex-invalido`, `aex-duplicado`, `aex-aguarda-revisor`, `aex-fila-cheia` (o workflow cria os rótulos `aex-req-…`/`aex-fp-…` sozinho ao usá-los, mas os fixos acima convém existirem). Nenhum LLM roda no GitHub e nenhuma chave de API é guardada.

## B. Ações do GPT (ambiente em nuvem do auditor)
Pré-requisitos: `git`, `python3 ≥ 3.10`, `node` + `npm`; token vindo do **gerenciador de segredos** do ambiente (nunca em arquivo). O ambiente é efêmero: cada auditoria recomeça do pedido.
```bash
python3 kit/poll_requests.py          # lista pedidos [AEX-REQ] pendentes; sem pedido = não audita nem sincroniza
python3 kit/poll_requests.py --prepare   # grava task.json (commit e escopo do pedido)
```
```bash
export SOT_AUDITOR_TOKEN='…'                      # nunca em argumento/arquivo/log
bash kit/setup_auditor.sh <SHA do pedido>        # é aqui que ocorre o clone/pull; sempre SHA fixo
python3 kit/run_gates.py --repo ~/sot-audit/repo --out ~/sot-audit/evidence.json
# … audita e escreve finding.json (ver finding.example.json) …
python3 kit/validate_finding.py --repo ~/sot-audit/repo --finding finding.json
python3 kit/submit_finding.py   --repo-dir ~/sot-audit/repo --finding finding.json --evidence ~/sot-audit/evidence.json          # dry-run
python3 kit/submit_finding.py   --repo-dir ~/sot-audit/repo --finding finding.json --evidence ~/sot-audit/evidence.json --post   # envia
```
Atualizar para novo commit: apague `~/sot-audit/repo` e repita `setup_auditor.sh <novo ref>` (cada auditoria fixa um commit).

## C. Ações do Orquestrador (lado interno)
- **O Orquestrador é o único destinatário** dos achados `[AEX]` (a Issue é a caixa de entrada dele). O auditor não menciona nem atribui ninguém; Andraus recebe apenas a **consolidação do Orquestrador**.
- **Pedido de auditoria:** automático quando um PR **aberto** recebe o rótulo `homologacao-final` e, no corpo, as linhas `Spec: SPEC-0NN` e `Consenso: Especificador=OK; Revisor=OK; Auditor=PENDENTE; Andraus=PENDENTE` (o workflow só **detecta** a presença; o consenso é decidido por Especificador, Revisor, Auditor e Andraus; **você, Orquestrador, coordena e atualiza `Auditor=`** ao receber o veredito). No merge, o workflow **avisa** (não bloqueia) se faltou `Auditor=OK|COM_RESSALVAS` ou se o commit mesclado difere do auditado. Qualquer outra auditoria: `workflow_dispatch` do Orquestrador, **após consultar Andraus**, com motivo registrado.
- Descobrir achados: Issues com título `[AEX]`; aplicar rótulo `auditoria-externa` (o workflow já rotula os válidos).
- **Triar:** consultar Andraus e acionar o **Revisor SOT** para verificar cada achado por string-match no `baseline_commit`; registrar disposição na Issue: `CONFIRMADO` · `PARCIAL` · `DESCARTADO (motivo)` · `DUPLICADO`. O parecer do GPT é **dado a verificar**.
- **Postura:** ajustes ao auditor só por nova diretiva em `DIRETIVAS-AO-AUDITOR.md` (a anterior vira `SUPERADA`, INV-07), com a consulta a Andraus registrada.
- Só abrir tratamento (erratum/emenda) com **escopo autorizado por Andraus**; histórico baselined preservado (INV-09); decisão aberta nunca fechada (CONS-01).

## Verificação feita (2026-10-05, clone local sem token)
`setup_auditor.sh` instalou, desabilitou push e **calibração APROVADA (1 válido aceito; 8 defeitos plantados reprovados com o código esperado)**; `run_gates.py` executou **16 gates (todos exit 0)** e a árvore ficou limpa; `submit_finding.py` em dry-run gerou a Issue a partir de um achado real (WARN do `check_refs.py` em `DOSSIE-PESQUISA.md:13`).
**Não verificado (sem credencial real):** `verify_access.py` contra a API, `--post` real, e a permissão exata do token. Teste-os na primeira execução com a conta dedicada: `verify_access.py` deve imprimir `PASS`; um `push` tentado deve falhar.

## Limites honestos
- **PASS do validador = forma + ancoragem**, não mérito: achado pode estar errado; o Revisor/Andraus avaliam.
- O SOT **não controla** temperatura/seed/versão do modelo externo: reprodutibilidade = commit + evidência + data, não bit-a-bit.
- Declarado ≠ verificável ≠ executável ≠ bloqueante: o auditor é **consultivo**; o que bloqueia é o CI e a decisão de Andraus.


## Emenda de acesso (2026-10-05) — token do dono
- Num repositório pessoal não existe colaborador somente-leitura; Andraus escolheu **token fine-grained próprio**. Limite do desenho: o teto de poder é o **escopo do token**, não um papel; as ações do auditor aparecem com o login de Andraus, e `AUDITOR_EXTERNO_LOGINS` = login de Andraus (o filtro do workflow já não distingue auditor de dono — a separação é por prefixo `[AEX]` + validação do kit).
- `verify_access.py` **não consegue verificar o escopo** de um token do dono pela API: duas sondas de escrita deram falso positivo contra a API real (POST vazio → 422; blob válido → 201 com Contents Read-only na tela do GitHub). O script agora é **fail-closed**: com papel de dono, devolve `INDETERMINADO` (exit 1) e só passa com `--confirmo-escopo`, declaração humana de que o escopo foi conferido em Settings → Developer settings → Fine-grained tokens. **Limite honesto:** o escopo é declarado, não provado.

## Sincronização determinística do clone (`sync_auditor.sh`)
1. Instale **uma cópia fora do repositório**: `~/.sot-audit/sync_auditor.sh` (`chmod +x`); confira o `sha256sum` da cópia com o informado pelo Orquestrador. Não use a cópia de dentro do clone como âncora.
2. **1ª execução:** sai com exit 3; confira o hash e rode `sync_auditor.sh --approve <hash do manifesto informado pelo Orquestrador>`. A 1ª aprovação é sempre explícita.
3. **Rotina:** `sync_auditor.sh` (sem argumentos) faz fast-forward da `main`, confere o manifesto e, se o kit mudou, renova a aprovação **só** se o pedido `[AEX-REQ]` mais recente criado por `github-actions` trouxer o mesmo hash (campo `manifest=` do marcador, calculado pelo workflow). Mostra os arquivos alterados desde a última aprovação.
4. Se o próprio `sync_auditor.sh` mudar no repositório, a cópia instalada **não** se atualiza sozinha: reinstale (de propósito: é a âncora).
5. `poll_requests.py` só considera pedidos cujo **autor** é `github-actions`; Issue com marcador de outra conta é ignorada.

## Bot do Auditor Externo na Oracle Cloud (Always Free) — `auditor_bot.py` + `install_bot.sh`
**O que é.** Um agendador (systemd timer, a cada ~20 min) roda `~/.sot-audit/sync_auditor.sh` e, se sair com exit 0, o `auditor_bot.py`. Sem pedido `[AEX-REQ]` pendente ele **não chama o modelo**. Com pedido: prepara o commit (`setup_auditor.sh`), roda os gates, chama `codex exec --sandbox read-only` **sem o token do GitHub no ambiente do modelo**, recebe só um bloco JSON (DADO), valida cada achado, posta os válidos (`submit_finding.py`) e dá o ACK com o veredito consultivo. Falhas viram **uma nota** no pedido (sem spam). O workflow avisa o PR quando um achado é validado e quando o ACK chega (é isso que acorda o Orquestrador).
**Instalação (você, uma vez):**
1. Crie a VM Always Free (preferência: `VM.Standard.A1.Flex`, o menor tamanho disponível; Ubuntu LTS; chave SSH; **só a porta 22 de entrada**; saída liberada para HTTPS). Acesse por SSH. Confira `node --version` ≥ 18 e `python3 --version` ≥ 3.10 (`sudo apt install -y git python3 nodejs npm`).
2. **UM COMANDO** na VM (como usuário comum, não root). Ele lê o token uma vez, baixa o instalador, clona o repositório sozinho (token só em memória, nunca na URL) e instala tudo; o `<HASH>` é o do manifesto informado pelo Orquestrador no chat (equivale à 1ª aprovação explícita):
```
read -rs -p "Token: " T; echo; curl -fsSL -H "Authorization: Bearer $T" -H "Accept: application/vnd.github.raw+json" -o /tmp/install_bot.sh "https://api.github.com/repos/Andraus35/Sistema-Operacional-de-Trading--SOT/contents/governance/propostas/AUDITOR-EXTERNO/kit/install_bot.sh?ref=main" && SOT_BOOT_TOKEN="$T" bash /tmp/install_bot.sh --approve-hash <HASH>; unset T
```
3. Durante a instalação você só faz três coisas: digita `CONFIRMO` (declaração de escopo do token), digita o código do login do Codex no navegador e, se pedido, cola o hash. Ela inicia em **`--dry-run`**.
4. Teste: com um pedido pendente, `systemctl --user start sot-auditor.service && journalctl --user -u sot-auditor.service -n 80 --no-pager`. Confira o que ele faria (achados, descartados, veredito).
5. Quando estiver bom: `bash install_bot.sh --go-live`. Pausar: `systemctl --user stop sot-auditor.timer`. Estado: `bash install_bot.sh --status`.
**Limites e riscos (ver ata DHR-AUDITOR-EXTERNO-003):** o modelo roda como o mesmo usuário do bot e o sandbox read-only não impede LEITURA de arquivos; por isso o token **não** está no ambiente do modelo, a saída é varrida contra o token e o `auth.json` do Codex antes de qualquer uso, e o modelo não tem rede. Isso reduz, não elimina, o risco. A Oracle pode **recuperar instâncias Always Free ociosas** (CPU, rede e memória abaixo de 20% por 7 dias); se acontecer, o bot para até a VM ser recriada.

### Contingência: VM AMD de 1 GB (`VM.Standard.E2.1.Micro`) quando a A1 estiver sem capacidade
- O instalador detecta pouca memória (RAM + swap < ~2,5 GB) e cria um **swap de 2 GB** (`/swapfile`) via `sudo` sem senha; sem sudo, ele avisa e você cria à mão: `sudo fallocate -l 2G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile && echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab`.
- **Não verificado:** se Node + `codex exec` rodam de forma estável em 1 GB (com swap) e a CPU é 1/8 de OCPU; as chamadas ao modelo são I/O (rede), mas `npm ci` e a calibração são pesados. A Micro só existe em **um** domínio de disponibilidade e também está sujeita à recuperação por ociosidade.

### Cloud-init NÃO é necessário (2026-10-06)
A 1ª Micro criada com o cloud-init (upgrade + swap) ficou com a porta 22 recusando conexão por mais de 20 min, mesmo depois de reboot suave. Causa **não determinada** (o cloud-init foi a única peça fora do padrão; a pressão de memória de 1 GB também é suspeita). Por isso o `install_bot.sh` agora **instala sozinho** os pré-requisitos que faltarem (`git`, `python3`, `nodejs`, `npm`, `curl`, `ca-certificates`) via `sudo apt-get` sem senha, ativa o `linger` e cria o swap quando a memória é pequena. **Crie a VM sem cloud-init** (campo vazio). Se `curl` faltar na imagem: `sudo apt-get install -y curl`.
