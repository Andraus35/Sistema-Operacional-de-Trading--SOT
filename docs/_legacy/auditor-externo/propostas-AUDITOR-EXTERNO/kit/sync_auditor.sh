#!/usr/bin/env bash
# sync_auditor.sh — atualiza o clone do Auditor Externo do SOT de forma DETERMINÍSTICA.
# INSTALE UMA CÓPIA FORA DO REPOSITÓRIO (~/.sot-audit/sync_auditor.sh): ela é a âncora de confiança e se atualiza sozinha só até aqui.
# Uso: sync_auditor.sh            atualiza e confere; renova a aprovação sozinho SE o pedido [AEX-REQ] criado pelo workflow confirmar o hash
#      sync_auditor.sh --approve <hash do manifesto>   aprovação explícita (1ª instalação ou quando a confirmação automática não existir)
# exit 0 = em dia e aprovado · 2 = bloqueio/erro · 3 = manifesto novo/alterado sem confirmação (precisa --approve)
set -euo pipefail
REMOTE_URL="${SOT_REMOTE_URL:-https://github.com/Andraus35/Sistema-Operacional-de-Trading--SOT.git}"
REPO_DIR="${SOT_REPO_DIR:-/workspace/Sistema-Operacional-de-Trading--SOT}"
STATE_DIR="${SOT_AUDIT_STATE:-$HOME/.sot-audit}"
API="${SOT_API_BASE:-https://api.github.com}"
SLUG="${SOT_REPO_SLUG:-Andraus35/Sistema-Operacional-de-Trading--SOT}"
AEX=governance/propostas/AUDITOR-EXTERNO
die() { echo "BLOQUEADO: $*" >&2; exit 2; }
[ -n "${SOT_AUDITOR_TOKEN:-}" ] || die "SOT_AUDITOR_TOKEN ausente"
mkdir -p "$STATE_DIR"; chmod 700 "$STATE_DIR"
# token só por variáveis de ambiente do git (nunca em argumento nem em log)
export GIT_TERMINAL_PROMPT=0 GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=http.extraHeader
GIT_CONFIG_VALUE_0="Authorization: Basic $(printf 'x-access-token:%s' "$SOT_AUDITOR_TOKEN" | base64 | tr -d '\n')"
export GIT_CONFIG_VALUE_0
[ -d "$REPO_DIR/.git" ] || git clone -q "$REMOTE_URL" "$REPO_DIR" || die "clone falhou"
cd "$REPO_DIR"
[ "$(git remote get-url origin)" = "$REMOTE_URL" ] || die "origin diferente do esperado"
[ -z "$(git status --porcelain)" ] || die "checkout com alterações locais"
git checkout -q main || die "sem branch main"
git fetch -q origin main || die "fetch falhou"
git merge -q --ff-only FETCH_HEAD || die "main local divergiu de origin/main (sem fast-forward)"
(cd "$AEX" && sha256sum -c --quiet MANIFEST.sha256) || die "MANIFEST.sha256 não confere com os arquivos"
CUR=$(cd "$AEX" && sha256sum MANIFEST.sha256 | cut -d' ' -f1)
HEAD_SHA=$(git rev-parse HEAD)
APPROVED_FILE="$STATE_DIR/approved_manifest.sha256"; APPROVED_HEAD="$STATE_DIR/approved_head"
approve() { printf '%s\n' "$CUR" > "$APPROVED_FILE"; printf '%s\n' "$HEAD_SHA" > "$APPROVED_HEAD"; }
if [ "${1:-}" = "--approve" ]; then
  [ "${2:-}" = "$CUR" ] || die "hash informado (${2:-vazio}) difere do manifesto atual ($CUR)"
  approve; echo "APROVADO (explícito): $CUR"
fi
OLD=$( [ -f "$APPROVED_FILE" ] && cat "$APPROVED_FILE" || true )
if [ "$OLD" != "$CUR" ]; then
  # Renovação automática: SÓ se já havia aprovação anterior (a 1ª é sempre explícita) e o pedido [AEX-REQ] mais recente,
  # aberto e criado pelo workflow (github-actions), carrega exatamente este hash de manifesto.
  if [ -n "$OLD" ]; then
    REQ=$(python3 - "$API" "$SLUG" "$CUR" <<'PY'
import json, os, re, sys, urllib.request
api, slug, cur = sys.argv[1:4]
rq = urllib.request.Request(f"{api}/repos/{slug}/issues?state=open&per_page=50&sort=created&direction=desc",
    headers={"Authorization": f"Bearer {os.environ['SOT_AUDITOR_TOKEN']}", "Accept": "application/vnd.github+json", "User-Agent": "sot-sync"})
try: items = json.load(urllib.request.urlopen(rq, timeout=30))
except Exception: sys.exit(0)
for i in items:
    if "pull_request" in i or not i["title"].startswith("[AEX-REQ]"): continue
    if (i.get("user") or {}).get("login") not in ("github-actions[bot]", "github-actions"): continue
    m = re.search(r"<!-- aex-req [^>]*? manifest=([0-9a-f]{64}) -->", i.get("body") or "")
    if m: print(i["number"], m[1]); break
PY
)
    RN=${REQ%% *}; RH=${REQ##* }
    if [ -n "$REQ" ] && [ "$RH" = "$CUR" ]; then
      OH=$( [ -f "$APPROVED_HEAD" ] && cat "$APPROVED_HEAD" || true )
      echo "MANIFESTO RENOVADO automaticamente (confirmado pelo pedido #$RN criado pelo workflow): $OLD -> $CUR"
      [ -n "$OH" ] && echo "Arquivos alterados em $AEX desde a última aprovação:" && git diff --name-only "$OH" "$HEAD_SHA" -- "$AEX" || true
      approve
    fi
  fi
fi
if [ ! -f "$APPROVED_FILE" ] || [ "$(cat "$APPROVED_FILE")" != "$CUR" ]; then
  echo "MANIFESTO NOVO/ALTERADO sem confirmação: $CUR"
  echo "Confira com o hash informado pelo Orquestrador (chat do Andraus) e rode: sync_auditor.sh --approve $CUR"; exit 3
fi
echo "OK head=$(git rev-parse --short HEAD) manifesto=$CUR aprovado"
