// Testa os hooks contra o contrato real do Claude Code: JSON via stdin, bloqueio = exit 2.
const { spawnSync } = require('child_process');
const path = require('path');
const root = path.join(__dirname, '..');
let fail = 0;
function run(script, payload, env) {
  return spawnSync('node', [path.join(root, 'scripts', script)], {
    input: payload === undefined ? '' : JSON.stringify(payload),
    env: { ...process.env, HOOK_TOOL_INPUT: '', ...env },
    encoding: 'utf8',
  });
}
function expect(name, r, code) {
  const ok = r.status === code;
  if (!ok) fail++;
  console.log(`  ${ok ? 'PASS' : 'FAIL'} [${name}] exit=${r.status} esperado=${code}`);
}
const w = (file_path, content) => ({ tool_name: 'Write', tool_input: { file_path, content } });

expect('violação ICT (stdin, path /)', run('gate-check.js', w('specs/x.spec.md', 'ICT pode criar hipótese')), 2);
expect('violação ICT (path Windows barra invertida)', run('gate-check.js', w('C:\\r\\specs\\features\\S\\plan.md','ICT pode criar hipótese')), 2);
expect('violação SMC em Edit.new_string', run('gate-check.js', { tool_name: 'Edit', tool_input: { file_path: 'governance/RULES.md', new_string: 'SMC sobrepõe Elliott' } }), 2);
expect('violação em MultiEdit', run('gate-check.js', { tool_name: 'MultiEdit', tool_input: { file_path: 'specs/a.md', edits: [{ new_string: 'ICT pode criar' }] } }), 2);
expect('regra enunciada (negação) passa', run('gate-check.js', w('governance/CONSTITUTION.md', 'SMC nunca corrige Elliott')), 0);
expect('fora de escopo passa', run('gate-check.js', w('README.md', 'ICT pode criar hipótese')), 0);
expect('stdin vazio não quebra', run('gate-check.js', undefined), 0);
expect('legado HOOK_TOOL_INPUT ainda bloqueia', run('gate-check.js', undefined, { HOOK_TOOL_INPUT: JSON.stringify({ file_path: 'specs/x.md', content: 'ICT pode criar' }) }), 2);

const fs = require('fs'), os = require('os');
const tmp = path.join(os.tmpdir(), 'sot-hook-test.json');
fs.writeFileSync(tmp, '{ ok: ');
expect('JSON inválido pós-edição → 2', run('post-edit-check.js', w(tmp, '')), 2);
fs.writeFileSync(tmp, '{"ok":true}');
expect('JSON válido → 0', run('post-edit-check.js', w(tmp, '')), 0);
fs.unlinkSync(tmp);
expect('não-JSON ignorado', run('post-edit-check.js', w('a.md', '')), 0);

console.log(fail ? `\n${fail} falha(s)` : '\nTodos os testes de hook passaram');
process.exit(fail ? 1 : 0);
