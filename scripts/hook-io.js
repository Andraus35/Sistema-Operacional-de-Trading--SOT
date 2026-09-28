// Utilitário compartilhado pelos hooks do Claude Code (PreToolUse/PostToolUse).
//
// Contrato do Claude Code: o payload chega como JSON via STDIN
//   { tool_name, tool_input: { file_path, content | new_string | edits[] } , ... }
// e um hook só BLOQUEIA com exit code 2 (stderr é entregue ao modelo).
// Exit 1 é erro não-bloqueante. Ver docs de hooks do Claude Code.
//
// Compatibilidade: se não houver stdin, cai para a variável HOOK_TOOL_INPUT
// (formato legado usado antes desta correção; payload = o próprio tool_input).

const fs = require('fs');

const BLOCK = 2; // exit code de bloqueio

function readStdin() {
  try {
    return fs.readFileSync(0, 'utf8');
  } catch (_) {
    return '';
  }
}

function readToolInput() {
  const raw = readStdin().trim();
  if (raw) {
    try {
      const payload = JSON.parse(raw);
      return payload.tool_input || payload;
    } catch (_) {
      // JSON inválido no stdin: não bloquear por defeito do canal.
    }
  }
  if (process.env.HOOK_TOOL_INPUT) {
    try {
      return JSON.parse(process.env.HOOK_TOOL_INPUT);
    } catch (_) {
      /* ignora */
    }
  }
  return {};
}

// Normaliza separadores (Windows entrega "specs\\features\\...").
function normalizePath(p) {
  return String(p || '').replace(/\\/g, '/');
}

// Texto novo que a operação introduz: Write.content, Edit.new_string, MultiEdit.edits[].
function newContent(toolInput) {
  const parts = [];
  if (typeof toolInput.content === 'string') parts.push(toolInput.content);
  if (typeof toolInput.new_string === 'string') parts.push(toolInput.new_string);
  if (Array.isArray(toolInput.edits)) {
    for (const e of toolInput.edits) {
      if (e && typeof e.new_string === 'string') parts.push(e.new_string);
    }
  }
  return parts.join('\n');
}

module.exports = { BLOCK, readToolInput, normalizePath, newContent };
