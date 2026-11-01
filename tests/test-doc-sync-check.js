// A6.4: doc-sync-check.js só repete o aviso quando o conjunto de achados muda; ERRO aparece sempre.
const { spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path');
let fail = 0;
const ok = (n, c) => { console.log((c ? '  PASS [' : '  FAIL [') + n + ']'); if (!c) fail++; };

function repo(stdout) {
  const d = fs.mkdtempSync(path.join(os.tmpdir(), 'dsc-'));
  fs.mkdirSync(path.join(d, 'scripts')); fs.mkdirSync(path.join(d, '.claude'));
  fs.copyFileSync(path.join(__dirname, '..', 'scripts', 'doc-sync-check.js'), path.join(d, 'scripts', 'doc-sync-check.js'));
  setOut(d, stdout);
  fs.writeFileSync(path.join(d, 'scripts', 'backlog_triggers.py'), 'print("")\n');
  return d;
}
const setOut = (d, s) => fs.writeFileSync(path.join(d, 'scripts', 'check_doc_sync.py'), 'print(' + JSON.stringify(s) + ')\n');
const run = (d, mode = 'session-start') => spawnSync('node', [path.join(d, 'scripts', 'doc-sync-check.js'), mode], { encoding: 'utf8' }).stdout;

let d = repo('[WARN] a.md:1 — x\nERRO=0 WARN=1 INFO=0');
ok('1ª vez com WARN: mostra', /doc-sync: 0 achado/.test(run(d)));
ok('mesmo conjunto de WARN: silencia', run(d) === '');
setOut(d, '[WARN] b.md:2 — y\nERRO=0 WARN=1 INFO=0');
ok('conjunto mudou (mesma contagem): mostra de novo', /doc-sync: 0 achado/.test(run(d)));
setOut(d, '[ERRO] c.md:3 — z\nERRO=1 WARN=0 INFO=0');
ok('ERRO aparece', /doc-sync: 1 achado/.test(run(d)));
ok('ERRO repetido continua aparecendo', /doc-sync: 1 achado/.test(run(d)));
setOut(d, 'ERRO=0 WARN=0 INFO=0');
ok('sem achados: silencioso', run(d) === '');
setOut(d, '[WARN] b.md:2 — y\nERRO=0 WARN=1 INFO=0');
ok('WARN volta depois de limpo: mostra', /doc-sync: 0 achado/.test(run(d)));
fs.rmSync(path.join(d, '.claude'), { recursive: true });
ok('estado ilegível/gravação falha: mostra, nunca esconde', /doc-sync: 0 achado/.test(run(d)));

const s = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '.claude', 'settings.json'), 'utf8'));
const cmds = (ev) => s.hooks[ev].flatMap(g => g.hooks.map(h => h.command));
ok('settings: doc-sync fora de Stop/SubagentStop', !cmds('Stop').concat(cmds('SubagentStop')).some(c => c.includes('doc-sync-check')));
ok('settings: doc-sync continua em SessionStart', cmds('SessionStart').some(c => c.includes('doc-sync-check.js session-start')));
console.log(fail ? 'FALHOU' : 'Todos os testes de doc-sync-check passaram'); process.exit(fail ? 1 : 0);
