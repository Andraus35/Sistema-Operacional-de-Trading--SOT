set -e
S=$1; R=$2; rm -rf $S/lg && mkdir -p $S/lg && cd $S/lg && git init -q -b main && git config user.email a@b && git config user.name t
mkdir -p governance/aprendizado governance/propostas/SPEC-048 scripts
cp $R/governance/aprendizado/CAUSAS-PREVENCAO.md $R/governance/aprendizado/RETROSPECTIVAS.md governance/aprendizado/; cp $R/scripts/loop_ledger.py scripts/
PA=$R/governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R3-2026-10-24.md
PB=$R/governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R4-2026-10-25.md
test -f $PA; test -f $PB
echo x > README; git add -A; git commit -qm base
run() { # $1=prefixo $2=ledger-versionado(1/0)
  git checkout -q main; git checkout -qb $1-0 main
  [ "$2" = 0 ] && { echo governance/aprendizado/LEDGER-ACHADOS.md > .gitignore; git add .gitignore; git commit -qm ign; }
  git checkout -qb $1-a $1-0; mkdir -p governance/propostas/SPEC-048; cp $PA governance/propostas/SPEC-048/; python3 scripts/loop_ledger.py >/dev/null; git add -A; git commit -qm a
  git checkout -qb $1-b $1-0; mkdir -p governance/propostas/SPEC-048; cp $PB governance/propostas/SPEC-048/; python3 scripts/loop_ledger.py >/dev/null; git add -A; git commit -qm b
  git checkout -q $1-a; git merge --no-edit $1-b 2>&1 | tail -1
}
echo "A) ledger COMMITADO (modelo atual):"; run A 1; git diff --name-only --diff-filter=U; git merge --abort
echo "B) ledger GERADO, nao versionado:"; run B 0; git status -sb | head -1
python3 scripts/loop_ledger.py --stdout > x1.txt; python3 scripts/loop_ledger.py --stdout > x2.txt; cmp x1 x1.txt >/dev/null 2>&1 || true; cmp x1.txt x2.txt && echo "deterministico: duas geracoes identicas"
echo "achados dos DOIS pareceres no ledger regenerado: $(grep -c 'SPEC-048' x1.txt) linhas citam SPEC-048"
