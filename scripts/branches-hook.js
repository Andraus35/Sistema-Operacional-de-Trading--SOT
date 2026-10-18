#!/usr/bin/env node
// Hook SessionStart: roda scripts/check_branches.py de forma INFORMATIVA e avisa de ramos remotos órfãos
// (à frente da main e não citados no HANDOFF.md) ou apagáveis. Nunca bloqueia (exit 0 sempre) — DETECTOR, não GATE (ENF-03);
// não apaga ramo nem fecha PR. Falha do script nunca derruba a sessão.
//   node scripts/branches-hook.js session-start

const { spawnSync } = require('child_process');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const CHECK = path.join(__dirname, 'check_branches.py');

try {
  if (process.argv[2] !== 'session-start') {
    console.error('uso: node scripts/branches-hook.js session-start');
    process.exit(0);
  }
  for (const [exe, pre] of [['python', []], ['python3', []], ['py', ['-3']]]) {
    const r = spawnSync(exe, [...pre, CHECK], { cwd: ROOT, encoding: 'utf8', timeout: 25000 });
    if (r.error || r.status === 9009 || /Python was not found|Microsoft Store/i.test(String(r.stderr))) continue;
    const out = String(r.stdout || '');
    const lines = out.split('\n').filter((l) => /^\[(WARN|INFO)\] BR-0[12]/.test(l));
    const warn = lines.filter((l) => l.startsWith('[WARN]'));
    const info = lines.filter((l) => l.startsWith('[INFO]'));
    if (warn.length) console.log('ramos: possíveis ramos órfãos (informativo):\n' + warn.join('\n'));
    if (info.length) console.log(`ramos: ${info.length} ramo(s) remoto(s) já contido(s) na main (apagáveis) — "python scripts/check_branches.py" para a lista.`);
    break;
  }
} catch (_) {
  /* nunca derruba a sessão */
}
process.exit(0);
