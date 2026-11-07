#!/data/data/com.termux/files/usr/bin/bash
# Limpeza de ramos remotos do SOT, por grupos, com conferencia antes de cada remocao.
# Uso:  bash arquivar-ramos.sh A   # contidos na main (0 commits exclusivos)
#       bash arquivar-ramos.sh B   # so handoff/mapa, handoffs ja arquivados na main
#       bash arquivar-ramos.sh C   # historicos: cria tag arquivo/<nome> e SO ENTAO apaga o ramo
# Nada e apagado sem voce responder "s". Precisa de gh logado como admin (ver proteger-main.sh).
set -euo pipefail
REPO="Andraus35/Sistema-Operacional-de-Trading--SOT"
G="${1:-}"
A="ccr-599f6762-60qbvg claude/amazing-fermat-dnbjtz ccr-60575b67-ffmqlh ccr-f02efedf-w33g38"
B="ccr-3235944c-duo3sl ccr-166207a9-473jhk ccr-1c561451-dsk356"
C="ccr-3a0d581c-6cj4ig ferramentas-estresse spec006-plan ccr-e3c0fb7e-63d2l9 auditor-externo-integracao spec-006-abertura"
case "$G" in A) L="$A";; B) L="$B";; C) L="$C";; *) echo "uso: bash arquivar-ramos.sh A|B|C"; exit 1;; esac
command -v gh >/dev/null || { echo "gh nao instalado"; exit 1; }
gh auth status -h github.com >/dev/null 2>&1 || { echo "faca: gh auth login -h github.com -p https -w -s repo"; exit 1; }

echo "== Grupo $G em $REPO"
for b in $L; do
  if ! sha=$(gh api "repos/$REPO/git/ref/heads/$b" --jq .object.sha 2>/dev/null); then echo "  $b: ja nao existe"; continue; fi
  ahead=$(gh api "repos/$REPO/compare/main...$b" --jq .ahead_by)
  echo "  $b  sha=${sha:0:9}  commits_a_frente_da_main=$ahead"
  if [ "$G" = "A" ] && [ "$ahead" != "0" ]; then echo "  >> PULADO: grupo A exige 0 commits exclusivos"; continue; fi
  printf "  %s este ramo? [s/N] " "$([ "$G" = C ] && echo 'ARQUIVAR (tag) e APAGAR' || echo 'APAGAR')"; read -r R
  [ "$R" = "s" ] || [ "$R" = "S" ] || { echo "  mantido"; continue; }
  if [ "$G" = "C" ]; then
    tag="arquivo/$b"
    gh api --method POST "repos/$REPO/git/refs" -f "ref=refs/tags/$tag" -f "sha=$sha" --jq .ref 2>/dev/null || echo "  (tag $tag ja existia)"
    gh api "repos/$REPO/git/ref/tags/$tag" --jq .object.sha | grep -q "$sha" || { echo "  >> tag nao confere; NAO apago"; continue; }
    echo "  tag $tag = ${sha:0:9} confirmada"
  fi
  gh api --method DELETE "repos/$REPO/git/refs/heads/$b" && echo "  apagado: $b"
done
echo "== Feito. Restantes:"; gh api "repos/$REPO/branches" --paginate --jq '.[].name' | tr '\n' ' '; echo
