#!/usr/bin/env node
// Roda scripts/check_doc_sync.py de forma INFORMATIVA nos hooks Stop/SubagentStop/
// SessionStart — mesma garantia determinística de "não depende de o agente lembrar"
// que scripts/map-sync.js já dá ao mapa do projeto (BL-019), aplicada agora à
// sincronização documental (decisões CONS-01, RULE não registrada, Estado de backlog
// fora do enum, intake dessincronizado do painel vivo).
//
// Nunca bloqueia o agente (exit 0 sempre) — é DETECTOR, não GATE (ENF-03): um achado de
// drift de sincronização exige julgamento humano (Revisor audita, Andraus decide), o
// script python nunca promove nem fecha nada. Only prints a nudge; a promoção a
// bloqueante no CI segue a mesma régua já aplicada a check_refs.py/backlog_triggers.py
// (nunca --strict aqui; período estável antes de qualquer bloqueio).
//
//   node scripts/doc-sync-check.js stop            Stop/SubagentStop
//   node scripts/doc-sync-check.js session-start    SessionStart

const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const ROOT = path.join(__dirname, '..');
const CHECK = path.join(__dirname, 'check_doc_sync.py');
const BACKLOG = path.join(__dirname, 'backlog_triggers.py');

function pythonUnavailable(r) {
  if (r.error) return true;
  if (r.status === 9009) return true;
  return /Python was not found|Microsoft Store|não foi encontrado/i.test(String(r.stderr) + String(r.stdout));
}

function run(script, extra) {
  for (const [exe, pre] of [['python', []], ['python3', []], ['py', ['-3']]]) {
    const r = spawnSync(exe, [...pre, script, ...(extra || [])], { cwd: ROOT, encoding: 'utf8' });
    if (!pythonUnavailable(r)) return r;
  }
  return null;
}

const mode = process.argv[2];
if (mode !== 'stop' && mode !== 'session-start') {
  console.error('uso: node scripts/doc-sync-check.js stop|session-start');
  process.exit(0);
}

const r = run(CHECK);
if (!r) {
  // Python indisponível: silencioso aqui (map-sync.js já sinaliza isso para o mapa;
  // não duplicar o aviso). O backstop continua sendo o CI (setup-python garantido).
  process.exit(0);
}
const m = String(r.stdout || '').match(/ERRO=(\d+) WARN=(\d+)/);
// A6.4: o aviso repetido só reaparece quando o CONJUNTO de achados muda; ERRO > 0 aparece sempre.
// Estado local (gitignored) em .claude/.doc-sync-estado; falha ao ler/gravar = mostra (nunca esconde).
const ESTADO = path.join(ROOT, '.claude', '.doc-sync-estado');
const achados = String(r.stdout || '').split('\n').filter(l => /^\[(ERRO|WARN)\]/.test(l)).join('\n');
const assinatura = require('crypto').createHash('sha256').update((m ? m[0] : '') + '\n' + achados).digest('hex');
let jaVisto = false;
try { jaVisto = fs.readFileSync(ESTADO, 'utf8').trim() === assinatura; } catch (e) { /* mostra */ }
if (m && (Number(m[1]) > 0 || Number(m[2]) > 0)) {
  try { fs.writeFileSync(ESTADO, assinatura + '\n'); } catch (e) { /* mostra mesmo assim */ }
}
if (m && (Number(m[1]) > 0 || (Number(m[2]) > 0 && !jaVisto))) {
  console.log(
    `doc-sync: ${m[1]} achado(s) ERRO, ${m[2]} WARN de sincronização documental — ` +
    'rode "python scripts/check_doc_sync.py" para ver o detalhe (achado de gate; Revisor/Andraus decidem, não este hook).'
  );
}

// Vinculação de backlog por abertura (DHR-BACKLOG-ABERTURA-001): Spec em redação cujo plan.md
// ainda não declara a Disposição de cada item vinculado por regra. Informativo (o GATE é o
// [STRUCT-13] do validate_spec_sot.py); nunca bloqueia nem promove.
const b = run(BACKLOG, ['--abertura-pendentes']);
if (b) {
  const lines = String(b.stdout || '').split('\n').filter(l => l.startsWith('ABERTURA-PENDENTE SPEC-'));
  if (lines.length) {
    console.log('backlog-abertura: ' + lines.join(' | ') + ' — declare "Disposição: INCORPORADO|PARCIAL|REFERÊNCIA|FORA" no plan.md ' +
      '(rode "python scripts/backlog_triggers.py --abertura SPEC-NNN"; o gate é o [STRUCT-13]).');
  }
}
process.exit(0);
