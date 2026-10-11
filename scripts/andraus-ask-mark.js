#!/usr/bin/env node
// Marcador DETERMINÍSTICO: registra que o orquestrador FEZ uma pergunta a Andraus (AskUserQuestion).
//
// Por que existe: o hook de fim de turno (scripts/andraus-ask-guard.js) precisa saber se já houve pergunta DEPOIS da
// última entrega de agente, mas o histórico da sessão é escrito de forma assíncrona e pode não ter o turno atual
// (docs de hooks do Claude Code). Este marcador, gravado no momento da chamada, não depende desse atraso.
//
//   Registrado em .claude/settings.json → hooks.PostToolUse[matcher="AskUserQuestion"]
// Estado: <tmp>/sot-ask-state/<session_id>.json  (fora do repositório). Detector/auxiliar (ENF-03): nunca bloqueia, fail-open.

const fs = require('fs');
const os = require('os');
const path = require('path');

function stateFile(sid) {
  const dir = process.env.SOT_ASK_STATE_DIR || path.join(os.tmpdir(), 'sot-ask-state');
  return { dir, file: path.join(dir, String(sid || 'sem-sessao').replace(/[^\w.-]/g, '_') + '.json') };
}

if (require.main === module) {
  try {
    let raw = '';
    try { raw = fs.readFileSync(0, 'utf8'); } catch (_) { /* sem stdin */ }
    const payload = raw.trim() ? JSON.parse(raw) : {};
    const { dir, file } = stateFile(payload.session_id);
    fs.mkdirSync(dir, { recursive: true });
    let st = {};
    try { st = JSON.parse(fs.readFileSync(file, 'utf8')); } catch (_) { /* primeiro uso */ }
    st.lastAskMs = Date.now();
    fs.writeFileSync(file, JSON.stringify(st));
  } catch (_) { /* fail-open */ }
  process.exit(0);
}

module.exports = { stateFile };
