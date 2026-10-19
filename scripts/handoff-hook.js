#!/usr/bin/env node
// Hooks do HANDOFF.md (PCC-001, Fase 2). Mesma garantia "não depende de o agente lembrar"
// de scripts/doc-sync-check.js, aplicada à continuidade entre sessões.
//
//   node scripts/handoff-hook.js session-start   injeta o cabeçalho do handoff (+ cabeçalho do anexo de tarefa, se houver) + achados do detector
//   node scripts/handoff-hook.js stop            lembra de reescrever o handoff se houver defasagem (HO-03)
//
// Nunca bloqueia (exit 0 sempre) — DETECTOR, não GATE (ENF-03). Não escreve o handoff,
// não fecha decisão aberta (CONS-01). Falha do script nunca derruba a sessão.

const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const CHECK = path.join(__dirname, 'check_handoff.py');
const HANDOFF = path.join(ROOT, 'HANDOFF.md');

function pythonUnavailable(r) {
  if (r.error) return true;
  if (r.status === 9009) return true;
  return /Python was not found|Microsoft Store|não foi encontrado/i.test(String(r.stderr) + String(r.stdout));
}

function runCheck() {
  for (const [exe, pre] of [['python', []], ['python3', []], ['py', ['-3']]]) {
    const r = spawnSync(exe, [...pre, CHECK], { cwd: ROOT, encoding: 'utf8' });
    if (!pythonUnavailable(r)) return r;
  }
  return null;
}

function findings(r) {
  return String(r.stdout || '').split('\n').filter((l) => /^\[(ERRO|WARN)\] HO-/.test(l));
}

const mode = process.argv[2];
if (mode !== 'stop' && mode !== 'session-start') {
  console.error('uso: node scripts/handoff-hook.js stop|session-start');
  process.exit(0);
}

try {
  const r = runCheck();
  const found = r ? findings(r) : [];
  if (mode === 'session-start') {
    if (!fs.existsSync(HANDOFF)) {
      console.log('handoff: HANDOFF.md ausente — pare e reporte a Andraus (AGENTS.md §11).');
    } else {
      const head = fs.readFileSync(HANDOFF, 'utf8').split('\n').slice(0, 11).join('\n');
      console.log('handoff: leia HANDOFF.md e execute "Reverificar ao vivo" antes de agir (AGENTS.md §11). Cabeçalho vigente:\n' + head);
      // Anexo de tarefa (DHR-PCC-003): extensão do handoff; no máximo um ATIVO, citado pelo campo `anexo:`.
      const m = /^anexo:\s*(\S+)\s*$/m.exec(fs.readFileSync(HANDOFF, 'utf8').split('\n').slice(0, 14).join('\n'));
      if (m && !/^(null|nenhum)$/i.test(m[1])) {
        const ap = path.join(ROOT, m[1]);
        if (fs.existsSync(ap)) {
          const ah = fs.readFileSync(ap, 'utf8').split('\n').slice(0, 12).join('\n');
          console.log('handoff: ANEXO DE TAREFA ativo (' + m[1] + ') — leia-o depois do handoff; só ponteiros, nada vale sem conferir a fonte:\n' + ah);
        } else {
          console.log('handoff: o campo `anexo:` aponta para arquivo inexistente (' + m[1] + ') — HO-11.');
        }
      }
    }
    if (found.length) console.log('handoff: achados do detector (PCC-001):\n' + found.join('\n'));
  } else {
    if (found.some((l) => /HO-03|HO-04|HO-01|HO-11|HO-12/.test(l))) {
      console.log(
        'handoff: defasado/incompleto — antes de encerrar, reescreva o HANDOFF.md (novo handoff_id, base_commit, ' +
        'arquivar o anterior em docs/handoffs/) e empurre ao ramo (AGENTS.md §11). Detalhe: python scripts/check_handoff.py'
      );
    }
  }
} catch (_) {
  /* nunca derruba a sessão */
}
process.exit(0);
