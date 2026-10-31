#!/usr/bin/env node
// Hook PostToolUse/Agent (BL-036): repassa o evento ao scripts/telemetria_tokens.py (detector; nunca nega).
// Qualquer falha do wrapper = exit 0 (fail-open).
const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');
let input = '';
try { input = fs.readFileSync(0, 'utf8'); } catch (_) { process.exit(0); }
const SCRIPT = path.join(__dirname, 'telemetria_tokens.py');
for (const [exe, pre] of [['python', []], ['python3', []], ['py', ['-3']]]) {
  const r = spawnSync(exe, [...pre, SCRIPT], { input, encoding: 'utf8', cwd: path.join(__dirname, '..'), timeout: 110000 });
  if (r.error || r.status === 9009) continue;
  if (/Python was not found|Microsoft Store/i.test(String(r.stderr))) continue;
  if (r.status === 0 && r.stdout) process.stdout.write(r.stdout);
  process.exit(0);
}
process.exit(0);
