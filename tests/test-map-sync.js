// Testa scripts/map-sync.js (garantia de atualização do mapa) em repositório sintético.
const { spawnSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const SRC = path.join(__dirname, '..', 'scripts');
let fail = 0;
const ok = (name, cond) => {
  if (!cond) fail++;
  console.log(`  ${cond ? 'PASS' : 'FAIL'} [${name}]`);
};

function makeRepo() {
  const d = fs.mkdtempSync(path.join(os.tmpdir(), 'sot-mapsync-'));
  fs.mkdirSync(path.join(d, 'scripts'));
  for (const f of ['map-sync.js', 'hook-io.js', 'build_map.py', 'check_refs.py', 'backlog_triggers.py']) {
    fs.copyFileSync(path.join(SRC, f), path.join(d, 'scripts', f));
  }
  fs.mkdirSync(path.join(d, 'governance'));
  fs.mkdirSync(path.join(d, 'backlog'));
  fs.writeFileSync(path.join(d, 'ROADMAP.md'), '# Roadmap\n');
  fs.writeFileSync(path.join(d, 'governance', 'RULES.md'), '# Regras\n');
  fs.writeFileSync(path.join(d, 'backlog', 'RMR-001_Painel_Backlog.md'), '# RMR\n');
  return d;
}

const sync = (d, mode, payload) =>
  spawnSync('node', [path.join(d, 'scripts', 'map-sync.js'), mode], {
    input: payload ? JSON.stringify(payload) : '',
    encoding: 'utf8',
    env: { ...process.env, HOOK_TOOL_INPUT: '' },
  });
const mapJson = (d) => path.join(d, 'docs', 'mapa', 'mapa-projeto.json');
const digest = (d) => JSON.parse(fs.readFileSync(mapJson(d), 'utf8')).meta.digest;
const edit = (file) => ({ tool_name: 'Edit', tool_input: { file_path: file, new_string: 'x' } });

let d = makeRepo();
let r = sync(d, 'post-edit', edit(path.join(d, 'ROADMAP.md')));
ok('post-edit em .md gera o mapa', r.status === 0 && fs.existsSync(mapJson(d)));

const d1 = digest(d);
fs.writeFileSync(path.join(d, 'governance', 'RULES.md'), '# Regras\nmudou\n');
sync(d, 'post-edit', edit(path.join(d, 'governance', 'RULES.md')));
ok('post-edit após mudança atualiza o digest', digest(d) !== d1);

d = makeRepo();
sync(d, 'post-edit', edit(path.join(d, 'scripts', 'map-sync.js')));
ok('post-edit em não-.md é no-op', !fs.existsSync(mapJson(d)));

sync(d, 'post-edit', edit(path.join(d, 'docs', 'mapa', 'MAPA-PROJETO.md')));
ok('post-edit no próprio mapa é no-op (sem laço)', !fs.existsSync(mapJson(d)));

sync(d, 'post-edit', edit(path.join(os.tmpdir(), 'fora.md')));
ok('post-edit fora do repositório é no-op', !fs.existsSync(mapJson(d)));

sync(d, 'post-edit', { tool_name: 'Write', tool_input: { file_path: path.join(d, 'UPGRADES', 'x.md'), content: 'x' } });
ok('post-edit em UPGRADES é no-op (fora do escopo)', !fs.existsSync(mapJson(d)));

r = sync(d, 'stop');
ok('stop com mapa ausente gera o mapa', r.status === 0 && fs.existsSync(mapJson(d)));

const d2 = digest(d);
fs.writeFileSync(path.join(d, 'governance', 'NOVO.md'), '# Novo doc criado via Bash\n');
r = sync(d, 'stop');
ok('stop detecta edição por fora dos hooks e regenera', r.status === 0 && digest(d) !== d2);

const d3 = digest(d);
sync(d, 'stop');
ok('stop com mapa em dia não altera nada', digest(d) === d3);

r = sync(d, 'post-edit');
ok('sem payload não quebra', r.status === 0);

// --- Python indisponível: falha nunca silenciosa (marcador .stale) ---------------------
const stale = (dir) => path.join(dir, 'docs', 'mapa', '.stale');
const noPython = { PATH: path.dirname(process.execPath) };
const syncNoPy = (dir, mode, payload) =>
  spawnSync('node', [path.join(dir, 'scripts', 'map-sync.js'), mode], {
    input: payload ? JSON.stringify(payload) : '',
    encoding: 'utf8',
    env: { ...process.env, ...noPython, HOOK_TOOL_INPUT: '' },
  });
const check = (dir) =>
  spawnSync('python', [path.join(dir, 'scripts', 'build_map.py'), '--check'], { cwd: dir, encoding: 'utf8' });

d = makeRepo();
r = syncNoPy(d, 'post-edit', edit(path.join(d, 'ROADMAP.md')));
ok('sem Python: hook não bloqueia (exit 0)', r.status === 0);
ok('sem Python: grava marcador .stale', fs.existsSync(stale(d)));
ok('sem Python: avisa em stderr', /Python não encontrado/.test(r.stderr));
ok('--check falha enquanto houver .stale', check(d).status === 1);

r = sync(d, 'stop');
ok('com Python de volta: stop regenera e remove .stale', r.status === 0 && !fs.existsSync(stale(d)) && fs.existsSync(mapJson(d)));
ok('--check passa após regenerar', check(d).status === 0);

d = makeRepo();
syncNoPy(d, 'stop');
ok('sem Python: stop também marca defasagem', fs.existsSync(stale(d)));

// --- SessionStart: cura mudanças feitas com hooks desativados / fora do repo -----------
d = makeRepo();
sync(d, 'stop');
const before = digest(d);
fs.writeFileSync(path.join(d, 'governance', 'RULES.md'), '# Regras\neditado sem hooks\n');
r = sync(d, 'session-start');
ok('session-start regenera mudança feita fora dos hooks', r.status === 0 && digest(d) !== before);

console.log(fail ? `\n${fail} falha(s)` : '\nTodos os testes de map-sync passaram');
process.exit(fail ? 1 : 0);
