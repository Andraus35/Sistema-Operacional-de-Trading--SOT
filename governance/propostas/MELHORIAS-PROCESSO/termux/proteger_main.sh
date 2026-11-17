#!/data/data/com.termux/files/usr/bin/bash
# proteger_main.sh — confere e (se você mandar) liga a proteção da branch `main` (H4/H-PROTECAO; NÃO é mecanismo do harness).
# Feito para o Termux, mas roda em qualquer bash com `gh` e `jq`. Por padrão só LÊ e mostra o que faria (dry-run).
#
#   bash proteger_main.sh              # confere a proteção atual e mostra o payload (não altera nada)
#   bash proteger_main.sh --aplicar    # pede confirmação digitada (SIM) e então aplica
#   REPO=dono/repo BRANCH=main CODEOWNERS=1 bash proteger_main.sh
#
# O que liga: CI obrigatório ("Validate SOT Harness", branch em dia), PR obrigatório, e (CODEOWNERS=1) revisão de Code Owners.
# ATENÇÃO (leia antes de --aplicar): com "Require review from Code Owners", todo PR que mexe em arquivo selado
# (CODEOWNERS: gate do Revisor, check_refs, GATE-MANIFEST, .claude/agents/) precisa de aprovação de OUTRA pessoa ou de bypass de admin.
# Os PRs desta sessão são abertos pela SUA conta (Andraus35); o GitHub não deixa o autor aprovar o próprio PR. Por isso o script
# deixa enforce_admins=false: você (admin) ainda mescla com "Merge without waiting for requirements". Se preferir NÃO exigir
# Code Owners, use CODEOWNERS=0 (só CI + PR obrigatórios). Nunca force-push nem exclusão da main são permitidos pelo payload.
set -euo pipefail

REPO="${REPO:-Andraus35/Sistema-Operacional-de-Trading--SOT}"
BRANCH="${BRANCH:-main}"
CODEOWNERS="${CODEOWNERS:-1}"
CHECK="${CHECK:-Validate SOT Harness}"
APLICAR=0
[ "${1:-}" = "--aplicar" ] && APLICAR=1

command -v gh >/dev/null || { echo "Falta o gh. No Termux: pkg install gh"; exit 1; }
command -v jq >/dev/null || { echo "Falta o jq. No Termux: pkg install jq"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "gh não autenticado. Rode: gh auth login (escopo repo)"; exit 1; }

echo "== Repositório: $REPO · branch: $BRANCH"
echo "== Proteção ATUAL (leitura):"
if gh api "repos/$REPO/branches/$BRANCH/protection" >/tmp/prot_atual.json 2>/tmp/prot_err.txt; then
  jq '{checks: .required_status_checks.contexts, strict: .required_status_checks.strict,
       pr_reviews: (.required_pull_request_reviews // "NÃO exigido"),
       code_owners: (.required_pull_request_reviews.require_code_owner_reviews // false),
       enforce_admins: .enforce_admins.enabled, force_push: .allow_force_pushes.enabled, delete: .allow_deletions.enabled}' /tmp/prot_atual.json
else
  echo "Sem proteção (ou sem permissão): $(head -c 200 /tmp/prot_err.txt)"
fi

if [ "$CODEOWNERS" = "1" ]; then CO=true; else CO=false; fi
PAYLOAD=$(jq -n --arg chk "$CHECK" --argjson co "$CO" '{
  required_status_checks: {strict: true, contexts: [$chk]},
  enforce_admins: false,
  required_pull_request_reviews: {required_approving_review_count: 0, require_code_owner_reviews: $co, dismiss_stale_reviews: false},
  restrictions: null,
  allow_force_pushes: false,
  allow_deletions: false,
  required_linear_history: false,
  required_conversation_resolution: false}')

echo; echo "== Payload que seria aplicado (CODEOWNERS=$CODEOWNERS):"; echo "$PAYLOAD" | jq .

if [ "$APLICAR" -ne 1 ]; then
  echo; echo "Dry-run: nada foi alterado. Para aplicar: bash $0 --aplicar"; exit 0
fi

echo; read -r -p "Digite SIM para aplicar esta proteção em $REPO@$BRANCH: " R
[ "$R" = "SIM" ] || { echo "Cancelado."; exit 0; }
echo "$PAYLOAD" | gh api -X PUT "repos/$REPO/branches/$BRANCH/protection" --input - >/dev/null
echo "Aplicado. Conferindo:"
gh api "repos/$REPO/branches/$BRANCH/protection" | jq '{checks: .required_status_checks.contexts, code_owners: .required_pull_request_reviews.require_code_owner_reviews, enforce_admins: .enforce_admins.enabled}'
echo "Para desfazer: gh api -X DELETE repos/$REPO/branches/$BRANCH/protection"
