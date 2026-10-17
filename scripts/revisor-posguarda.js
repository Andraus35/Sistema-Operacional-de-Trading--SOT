#!/usr/bin/env node
// Hook Stop do Orquestrador (DHR-AUDITOR-EXTERNO-018): repassa o evento ao scripts/revisor_posguarda.py (stdout = {"decision":"block",...}).
// Qualquer falha do wrapper = exit 0 (fail-open).
const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');
let input = '';
try { input = fs.readFileSync(0, 'utf8'); } catch (_) { process.exit(0); }
const SCRIPT = path.join(__dirname, 'revisor_posguarda.py');
for (const [exe, pre] of [['python', []], ['python3', []], ['py', ['-3']]]) {
  const r = spawnSync(exe, [...pre, SCRIPT], { input, encoding: 'utf8', cwd: path.join(__dirname, '..'), timeout: 110000 });
  if (r.error || r.status === 9009) continue;
  if (/Python was not found|Microsoft Store/i.test(String(r.stderr))) continue;
  if (r.status === 0 && r.stdout) process.stdout.write(r.stdout);
  process.exit(0);
}
process.exit(0);
