#!/usr/bin/env node
// Gate hook (PreToolUse): checks that spec edits don't violate constitutional constraints.
// Bloqueia com exit 2 (contrato Claude Code) se detectar violação. Payload via stdin
// (ver scripts/hook-io.js). Rede de segurança — o gate autoritativo continua sendo
// validate_spec_sot.py + Revisor.

const { BLOCK, readToolInput, normalizePath, newContent } = require('./hook-io');

const toolInput = readToolInput();
const filePath = normalizePath(toolInput.file_path || toolInput.path);

if (!filePath) process.exit(0);

// Only check spec and rule files
const isSpec =
  /(^|\/)specs\//.test(filePath) || /(^|\/)(RULES|CONSTITUTION)\.md$/.test(filePath);
if (!isSpec) process.exit(0);

const content = newContent(toolInput);
if (!content) process.exit(0);

// Uma linha que ENUNCIA a regra ("SMC nunca corrige Elliott", "ICT não pode criar")
// não é violação — ignora linhas com negação/proibição.
const NEGATION = /\b(n[ãa]o|nunca|jamais|sem|nenhum[a]?|proibid[oa]|vedad[oa]|inv[ií]ol[aá]vel)\b/i;

function violates(regex) {
  return content.split('\n').some((line) => regex.test(line) && !NEGATION.test(line));
}

const violations = [];

// Check 1: No spec should contain "ICT pode criar hipótese" or similar
if (violates(/ICT.*pode.*criar/i)) {
  violations.push('CONSTITUTIONAL VIOLATION: ICT cannot create hypotheses (ICT INACTIVE rule)');
}

// Check 2: No spec should allow R:R below the minimum 1:3 (risk:reward) — Q-004
if (violates(/R:R\s*<\s*[012]([.:]\d+)?\s*(pode|pode ser aceito|permitido|ok)/i)) {
  violations.push('CONSTITUTIONAL VIOLATION: R:R below 1:3 (risk:reward) is never acceptable');
}

// Check 3: SMC should not override Elliott
if (violates(/SMC.*sobrepõe.*Elliott|SMC.*corrige.*Elliott/i)) {
  violations.push('CONSTITUTIONAL VIOLATION: SMC cannot override Elliott — hierarchy is inviolable');
}

if (violations.length > 0) {
  console.error('SOT Gate Check FAILED:');
  violations.forEach((v) => console.error('  ✗ ' + v));
  process.exit(BLOCK);
}

process.exit(0);
