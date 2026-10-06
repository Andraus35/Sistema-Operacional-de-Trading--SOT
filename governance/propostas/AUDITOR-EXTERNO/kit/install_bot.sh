#!/usr/bin/env bash
# install_bot.sh — instala o bot do Auditor Externo numa VM Linux (ex.: Oracle Cloud Always Free). [PROPOSTA — NÃO HOMOLOGADO]
# Rode como o USUÁRIO que vai rodar o bot (não root), de dentro do clone ~/sot-repo (ver README-INSTALACAO.md).
#   bash install_bot.sh              instala (interativo): token, declaração de escopo, Codex, sync, systemd, 1ª aprovação
#   bash install_bot.sh --print-only mostra os arquivos systemd que seriam criados (não altera nada)
#   bash install_bot.sh --go-live    tira o --dry-run e coloca o bot no ar (só depois de conferir o dry-run)
#   bash install_bot.sh --status     estado do timer e últimas linhas do log
set -euo pipefail
HOME_STATE="$HOME/.sot-audit"; ENVF="$HOME_STATE/env"; REPO_DIR="${SOT_REPO_DIR:-$HOME/sot-repo}"
KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; UNITS="$HOME/.config/systemd/user"
die() { echo "ERRO: $*" >&2; exit 1; }

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
command -v git >/dev/null && command -v python3 >/dev/null && command -v node >/dev/null && command -v npm >/dev/null || die "faltam git/python3/node/npm"
python3 -c 'import sys; sys.exit(0 if sys.version_info>=(3,10) else 1)' || die "python >= 3.10 requerido"
node -e 'process.exit(parseInt(process.versions.node)>=18?0:1)' || die "node >= 18 requerido"
command -v systemctl >/dev/null || die "systemd ausente"
[ -d "$REPO_DIR/.git" ] || die "clone esperado em $REPO_DIR (ver README-INSTALACAO.md)"
[ "$KIT" = "$REPO_DIR/governance/propostas/AUDITOR-EXTERNO/kit" ] || die "rode este script de dentro de $REPO_DIR"

mkdir -p "$HOME_STATE/codex-home"; chmod 700 "$HOME_STATE" "$HOME_STATE/codex-home"
echo "== 1/6 Declaração de escopo do token"
echo "O token deve ser fine-grained, só este repositório: Contents=Read-only, Issues=Read and write, Metadata=Read-only."
echo "A API NÃO prova isso: é uma declaração sua (limite registrado na ata DHR-AUDITOR-EXTERNO-002)."
read -r -p "Digite CONFIRMO se você conferiu esse escopo na tela do GitHub: " C; [ "$C" = "CONFIRMO" ] || die "sem confirmação"
read -rs -p "Cole o token (não aparece na tela): " T; echo; [ -n "$T" ] || die "token vazio"
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
  read -r -p "Cole o hash do manifesto informado pelo Orquestrador: " H
  SOT_AUDIT_STATE="$HOME_STATE" SOT_REPO_DIR="$REPO_DIR" "$HOME_STATE/sync_auditor.sh" --approve "$H"
elif [ "$RC" -ne 0 ]; then die "sync_auditor.sh saiu com $RC"; fi
echo
echo "PRONTO (modo --dry-run: o bot faz tudo, exceto postar e dar ACK)."
echo "Teste agora:  systemctl --user start sot-auditor.service && journalctl --user -u sot-auditor.service -n 60 --no-pager"
echo "Quando o dry-run estiver bom:  bash $KIT/install_bot.sh --go-live"
