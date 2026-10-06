#!/usr/bin/env bash
# install_bot.sh — instala o bot do Auditor Externo numa VM Linux (ex.: Oracle Cloud Always Free). [PROPOSTA — NÃO HOMOLOGADO]
# Rode como o USUÁRIO que vai rodar o bot (não root). UM COMANDO (ver README-INSTALACAO.md): baixa este script, clona o repositório
# sozinho e instala tudo; você só digita o token, CONFIRMO e o código do login do Codex.
#   bash install_bot.sh [--approve-hash H]  instala (interativo): token, escopo, clone, Codex, sync, systemd, 1ª aprovação
#   bash install_bot.sh --print-only mostra os arquivos systemd que seriam criados (não altera nada)
#   bash install_bot.sh --go-live    tira o --dry-run e coloca o bot no ar (só depois de conferir o dry-run)
#   bash install_bot.sh --status     estado do timer e últimas linhas do log
set -euo pipefail
HOME_STATE="$HOME/.sot-audit"; ENVF="$HOME_STATE/env"; REPO_DIR="${SOT_REPO_DIR:-$HOME/sot-repo}"
REMOTE_URL="${SOT_REMOTE_URL:-https://github.com/Andraus35/Sistema-Operacional-de-Trading--SOT.git}"
KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; UNITS="$HOME/.config/systemd/user"
die() { echo "ERRO: $*" >&2; exit 1; }

# memória: com menos de ~2,5 GB (RAM + swap) cria um swap de 2 GB (VM AMD de 1 GB); SOT_SWAP_PRINT_ONLY=1 só mostra o plano (testes)
ensure_swap() {
  local mem swap
  mem=$(awk '/^MemTotal:/{print $2}' "${SOT_MEMINFO:-/proc/meminfo}"); swap=$(awk '/^SwapTotal:/{print $2}' "${SOT_MEMINFO:-/proc/meminfo}")
  if [ $((mem + swap)) -ge 2621440 ]; then echo "memória ok: $((mem/1024)) MB RAM + $((swap/1024)) MB swap"; return 0; fi
  echo "AVISO: pouca memória ($((mem/1024)) MB RAM + $((swap/1024)) MB swap). Plano: swap de 2 GB em /swapfile."
  if [ "${SOT_SWAP_PRINT_ONLY:-}" = "1" ]; then echo "(print-only) fallocate -l 2G /swapfile; chmod 600; mkswap; swapon; linha no /etc/fstab"; return 0; fi
  if ! sudo -n true 2>/dev/null; then echo "AVISO: sem sudo sem senha. Crie o swap à mão (README-INSTALACAO.md) e rode de novo."; return 0; fi
  if [ ! -f /swapfile ]; then sudo sh -c 'fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile >/dev/null'; fi
  sudo swapon /swapfile 2>/dev/null || true
  grep -q '^/swapfile ' /etc/fstab || echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab >/dev/null
}

# pré-requisitos sem cloud-init: se faltar git/python3/node/npm/curl, instala via apt com sudo sem senha (VM nova); SOT_PREREQ_PRINT_ONLY=1 só mostra o plano
ensure_prereqs() {
  local falta=()
  for c in git python3 node npm curl; do command -v "$c" >/dev/null 2>&1 || falta+=("$c"); done
  if [ ${#falta[@]} -eq 0 ]; then echo "pré-requisitos ok (git, python3, node, npm, curl)"; return 0; fi
  echo "Faltam: ${falta[*]}. Plano: sudo apt-get install -y git python3 nodejs npm curl ca-certificates; sudo loginctl enable-linger $USER"
  [ "${SOT_PREREQ_PRINT_ONLY:-}" = "1" ] && return 0
  command -v apt-get >/dev/null 2>&1 || die "sem apt-get: instale ${falta[*]} manualmente"
  sudo -n true 2>/dev/null || die "sem sudo sem senha: rode 'sudo apt-get install -y git python3 nodejs npm curl ca-certificates' e tente de novo"
  sudo -n apt-get update -qq && sudo -n DEBIAN_FRONTEND=noninteractive apt-get install -y -qq git python3 nodejs npm curl ca-certificates
  sudo -n loginctl enable-linger "$USER" 2>/dev/null || true
}

service_unit() { cat <<EOF
[Unit]
Description=SOT Auditor Externo (bot determinístico, piloto)
[Service]
Type=oneshot
EnvironmentFile=$ENVF
Environment=PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin
Environment=SOT_REPO_DIR=$REPO_DIR
Environment=SOT_AUDIT_STATE=$HOME_STATE
Environment=SOT_AUDIT_HOME=$HOME/sot-audit
TimeoutStartSec=3600
ExecStart=/bin/bash -c '$HOME_STATE/sync_auditor.sh && exec /usr/bin/python3 $REPO_DIR/governance/propostas/AUDITOR-EXTERNO/kit/auditor_bot.py \$\$SOT_BOT_ARGS'
EOF
}
timer_unit() { cat <<EOF
[Unit]
Description=Agenda do SOT Auditor Externo (a cada 20 min)
[Timer]
OnBootSec=5min
OnUnitActiveSec=20min
RandomizedDelaySec=60
[Install]
WantedBy=timers.target
EOF
}

APPROVE_HASH=""
while [ $# -gt 0 ]; do case "$1" in --approve-hash) APPROVE_HASH="${2:-}"; [ -n "$APPROVE_HASH" ] || die "--approve-hash exige o hash"; shift 2 ;; *) break ;; esac; done
case "${1:-}" in
  --print-only) echo "### $UNITS/sot-auditor.service"; service_unit; echo; echo "### $UNITS/sot-auditor.timer"; timer_unit; exit 0 ;;
  --status) systemctl --user list-timers sot-auditor.timer --no-pager || true
            echo "--- SOT_BOT_ARGS atual: $(grep '^SOT_BOT_ARGS=' "$ENVF" 2>/dev/null || echo 'n/d')"
            journalctl --user -u sot-auditor.service -n 40 --no-pager || true; exit 0 ;;
  --go-live) [ -f "$ENVF" ] || die "instale primeiro (bash install_bot.sh)"
             sed -i 's/^SOT_BOT_ARGS=.*/SOT_BOT_ARGS=/' "$ENVF"; systemctl --user restart sot-auditor.timer
             echo "NO AR: o bot agora posta achados e dá ACK. Pausar: systemctl --user stop sot-auditor.timer"; exit 0 ;;
  "") ;;
  *) die "opção desconhecida: $1" ;;
esac

[ "$(id -u)" -ne 0 ] || die "não rode como root"
ensure_prereqs
command -v git >/dev/null && command -v python3 >/dev/null && command -v node >/dev/null && command -v npm >/dev/null || die "faltam git/python3/node/npm"
python3 -c 'import sys; sys.exit(0 if sys.version_info>=(3,10) else 1)' || die "python >= 3.10 requerido"
node -e 'process.exit(parseInt(process.versions.node)>=18?0:1)' || die "node >= 18 requerido"
command -v systemctl >/dev/null || die "systemd ausente"
ensure_swap

# token: lido UMA vez (ou herdado da re-execução via SOT_BOOT_TOKEN); nunca em argumento nem na URL do clone
T="${SOT_BOOT_TOKEN:-}"; unset SOT_BOOT_TOKEN
if [ -z "$T" ]; then read -rs -p "Cole o token (não aparece na tela): " T; echo; fi
[ -n "$T" ] || die "token vazio"
if [ ! -d "$REPO_DIR/.git" ]; then
  echo "== clonando o repositório em $REPO_DIR (token só em memória)"
  git -c "http.extraHeader=Authorization: Basic $(printf 'x-access-token:%s' "$T" | base64 | tr -d '\n')" clone -q "$REMOTE_URL" "$REPO_DIR" || die "clone falhou (token/escopo/rede?)"
fi
KIT_REPO="$REPO_DIR/governance/propostas/AUDITOR-EXTERNO/kit"
if ! cmp -s "$0" "$KIT_REPO/install_bot.sh"; then   # a cópia baixada difere da do clone: segue com a do clone
  echo "== usando o instalador do clone"; ARGS=(); [ -n "$APPROVE_HASH" ] && ARGS=(--approve-hash "$APPROVE_HASH")
  SOT_BOOT_TOKEN="$T" exec bash "$KIT_REPO/install_bot.sh" "${ARGS[@]}" "$@"
fi
KIT="$KIT_REPO"

mkdir -p "$HOME_STATE/codex-home"; chmod 700 "$HOME_STATE" "$HOME_STATE/codex-home"
echo "== 1/6 Declaração de escopo do token"
echo "O token deve ser fine-grained, só este repositório: Contents=Read-only, Issues=Read and write, Metadata=Read-only."
echo "A API NÃO prova isso: é uma declaração sua (limite registrado na ata DHR-AUDITOR-EXTERNO-002)."
read -r -p "Digite CONFIRMO se você conferiu esse escopo na tela do GitHub: " C; [ "$C" = "CONFIRMO" ] || die "sem confirmação"
umask 077; printf 'SOT_AUDITOR_TOKEN=%s\nSOT_CONFIRMO_ESCOPO=1\nSOT_BOT_ARGS=--dry-run\n' "$T" > "$ENVF"; unset T; chmod 600 "$ENVF"

echo "== 2/6 Codex CLI (npm, sem root)"
npm config set prefix "$HOME/.npm-global"; export PATH="$HOME/.npm-global/bin:$PATH"
npm i -g @openai/codex >/dev/null; codex --version
echo "== 3/6 Login do Codex com a conta ChatGPT (abre um código para você digitar no navegador)"
CODEX_HOME="$HOME_STATE/codex-home" codex login --device-auth
echo "== 4/6 Âncora de confiança fora do repositório"
install -m 700 "$KIT/sync_auditor.sh" "$HOME_STATE/sync_auditor.sh"
echo "sha256 da cópia instalada: $(sha256sum "$HOME_STATE/sync_auditor.sh" | cut -d' ' -f1)  (compare com o informado pelo Orquestrador)"
echo "== 5/6 systemd (usuário) + timer de 20 min, INICIANDO em --dry-run"
mkdir -p "$UNITS"; service_unit > "$UNITS/sot-auditor.service"; timer_unit > "$UNITS/sot-auditor.timer"
systemctl --user daemon-reload; systemctl --user enable --now sot-auditor.timer
loginctl enable-linger "$USER" 2>/dev/null || echo "AVISO: rode 'sudo loginctl enable-linger $USER' para o timer continuar sem sessão aberta."
echo "== 6/6 Primeira aprovação (explícita)"
set +e; set -a; . "$ENVF"; set +a; SOT_AUDIT_STATE="$HOME_STATE" SOT_REPO_DIR="$REPO_DIR" "$HOME_STATE/sync_auditor.sh"; RC=$?; set -e
if [ "$RC" -eq 3 ]; then
  H="$APPROVE_HASH"; [ -n "$H" ] || read -r -p "Cole o hash do manifesto informado pelo Orquestrador: " H
  SOT_AUDIT_STATE="$HOME_STATE" SOT_REPO_DIR="$REPO_DIR" "$HOME_STATE/sync_auditor.sh" --approve "$H"
elif [ "$RC" -ne 0 ]; then die "sync_auditor.sh saiu com $RC"; fi
echo
echo "PRONTO (modo --dry-run: o bot faz tudo, exceto postar e dar ACK)."
echo "Teste agora:  systemctl --user start sot-auditor.service && journalctl --user -u sot-auditor.service -n 60 --no-pager"
echo "Quando o dry-run estiver bom:  bash $KIT/install_bot.sh --go-live"
