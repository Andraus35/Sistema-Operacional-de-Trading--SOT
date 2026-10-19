// Testa scripts/handoff-hook.js: nunca bloqueia (exit 0) e imprime o lembrete esperado.
const { spawnSync } = require('child_process');
const path = require('path');
const root = path.join(__dirname, '..');
let fail = 0;
function run(mode) {
  return spawnSync('node', [path.join(root, 'scripts', 'handoff-hook.js'), mode], { cwd: root, encoding: 'utf8' });
}
function expect(name, ok) {
  if (!ok) fail++;
  console.log(`  ${ok ? 'PASS' : 'FAIL'} [${name}]`);
}
const s = run('session-start');
expect('session-start exit 0', s.status === 0);
expect('session-start injeta o cabeçalho do handoff', /handoff_id:/.test(s.stdout));
const hasAnexo = /^anexo:\s*(?!null|nenhum)\S+/mi.test(require('fs').readFileSync(path.join(root, 'HANDOFF.md'), 'utf8').split('\n').slice(0, 14).join('\n'));
expect('session-start mostra o anexo de tarefa quando o handoff o cita', !hasAnexo || /ANEXO DE TAREFA ativo/.test(s.stdout));
const t = run('stop');
expect('stop exit 0 (nunca bloqueia)', t.status === 0);
expect('modo inválido não quebra', run('xyz').status === 0);
console.log(fail ? `\n${fail} falha(s)` : '\nTodos os testes do handoff-hook passaram');
process.exit(fail ? 1 : 0);
