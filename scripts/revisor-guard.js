#!/usr/bin/env node
// Hook SubagentStop do Revisor SOT (DHR-AUDITOR-EXTERNO-017): repassa o evento ao scripts/revisor_guard.py.
// exit 2 + stderr = o Revisor continua e corrige (uma vez); qualquer falha do wrapper = exit 0 (nunca derruba a sessão).
const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');
let input = '';
try { input = fs.readFileSync(0, 'utf8'); } catch (_) { process.exit(0); }
const SCRIPT = path.join(__dirname, 'revisor_guard.py');
for (const [exe, pre] of [['python', []], ['python3', []], ['py', ['-3']]]) {
  const r = spawnSync(exe, [...pre, SCRIPT], { input, encoding: 'utf8', cwd: path.join(__dirname, '..'), timeout: 110000 });
  if (r.error || r.status === 9009) continue;
  if (/Python was not found|Microsoft Store/i.test(String(r.stderr))) continue;
  if (r.status === 2) { process.stderr.write(r.stderr); process.exit(2); }
  process.exit(0);
}
process.exit(0);
