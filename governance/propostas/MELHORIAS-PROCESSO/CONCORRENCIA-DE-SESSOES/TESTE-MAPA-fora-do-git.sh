S=$1; R=$2; rm -rf $S/mp $S/mpc; cd $R && git worktree prune
git worktree add -q $S/mp -b teste-mapa-fora origin/main && cd $S/mp
G="git -c user.email=a@b -c user.name=t"
echo docs/mapa/MAPA-PROJETO.md >> .gitignore; git rm -q --cached docs/mapa/MAPA-PROJETO.md; $G add -A; $G commit -qm "mapa fora do git"
git clone -q --no-hardlinks $S/mp $S/mpc 2>&1 | tail -1; cd $S/mpc; git checkout -q teste-mapa-fora
echo "1) clone novo, sem mapa: --check rc=$(python3 scripts/build_map.py --check >/dev/null 2>&1; echo $?) (esperado 2: ausente)"
python3 scripts/build_map.py >/dev/null 2>&1; echo "2) apos gerar (passo de CI/hook): --check rc=$(python3 scripts/build_map.py --check >/dev/null 2>&1; echo $?) (esperado 0)"
echo "3) mapa nao aparece no git status: [$(git status --short docs/mapa)]"
echo "4) gate_manifest: $(python3 scripts/gate_manifest.py --check | tail -1)"
echo "5) testes que usam o mapa:"; python3 -m unittest tests.test_pre_entrega tests.test_gate_manifest tests.test_revisor_gate_mcp 2>&1 | tail -3
echo "6) dois ramos com .md novos diferentes mesclam sem tocar o mapa:"
for s in a b; do git checkout -q -b m$s teste-mapa-fora; echo "# $s" > docs/doc-$s.md; python3 scripts/build_map.py >/dev/null 2>&1; $G add -A; $G commit -qm $s; done; git checkout -q ma; $G merge --no-edit mb 2>&1 | tail -1
echo FIM
