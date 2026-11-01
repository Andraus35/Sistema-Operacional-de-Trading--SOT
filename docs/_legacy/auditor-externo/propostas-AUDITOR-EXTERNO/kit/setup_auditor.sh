#!/usr/bin/env bash
# setup_auditor.sh — instala o ambiente SOMENTE-LEITURA do Auditor Externo. [PROPOSTA — NÃO HOMOLOGADO]
# Uso: SOT_AUDITOR_TOKEN=... bash setup_auditor.sh [<ref>]     (ref padrão: main; use SHA para auditoria reprodutível)
# Teste local sem token: SOT_REPO_URL=file:///caminho/clone bash setup_auditor.sh
set -euo pipefail
REPO_URL="${SOT_REPO_URL:-https://github.com/Andraus35/Sistema-Operacional-de-Trading--SOT.git}"
HOME_DIR="${SOT_AUDIT_HOME:-$HOME/sot-audit}"
REF="${1:-main}"
KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
command -v git >/dev/null || { echo "git ausente"; exit 1; }
command -v python3 >/dev/null || { echo "python3 ausente"; exit 1; }
command -v node >/dev/null && command -v npm >/dev/null || { echo "node/npm ausentes (necessários para npm test/lint)"; exit 1; }
python3 - <<'PY' || { echo "python >= 3.10 requerido"; exit 1; }
import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)
PY
mkdir -p "$HOME_DIR"; cd "$HOME_DIR"
if [[ "$REPO_URL" == https://github.com/* ]]; then
  : "${SOT_AUDITOR_TOKEN:?defina SOT_AUDITOR_TOKEN (fine-grained, Contents:read + Issues:read/write, só este repositório)}"
  AUTH=$(printf 'x-access-token:%s' "$SOT_AUDITOR_TOKEN" | base64 | tr -d '\n')
  GIT=(git -c "http.extraHeader=Authorization: Basic $AUTH")   # token só em memória; não vai para .git/config
  python3 "$KIT/verify_access.py"                              # fail-closed: aborta se token tiver push/admin
else
  GIT=(git)
fi
[[ -d repo/.git ]] || "${GIT[@]}" clone --quiet "$REPO_URL" repo
cd repo
git remote set-url --push origin DISABLED_NO_PUSH            # push impossível por construção local
git config core.hooksPath /dev/null                          # nenhum hook do repositório é executado
git config advice.detachedHead false
"${GIT[@]}" fetch --quiet origin
SHA="$(git rev-parse --verify --quiet "origin/$REF^{commit}" || git rev-parse --verify --quiet "$REF^{commit}" || true)"
[[ -n "$SHA" ]] || { echo "ref '$REF' não encontrada (use main ou um SHA completo)"; exit 1; }
git checkout --quiet --detach "$SHA"
[[ -z "$(git status --porcelain)" ]] || { echo "árvore suja"; exit 1; }
npm ci --ignore-scripts --silent                             # sem scripts de ciclo de vida (superfície de ataque)
echo "OK  commit auditado: $(git rev-parse HEAD)"
echo "OK  push desabilitado: $(git remote get-url --push origin)"
python3 "$KIT/selftest.py" --repo "$HOME_DIR/repo"           # calibração com defeitos plantados
echo "Próximo: python3 $KIT/run_gates.py --repo $HOME_DIR/repo --out $HOME_DIR/evidence.json"
