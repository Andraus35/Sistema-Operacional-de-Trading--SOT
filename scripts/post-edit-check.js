#!/usr/bin/env node
// Feedback hook (PostToolUse): after editing a JSON file, validates it is still valid JSON.
// Payload via stdin (ver scripts/hook-io.js). Exit 2 entrega o stderr ao modelo como feedback.

const fs = require('fs');
const { BLOCK, readToolInput, normalizePath } = require('./hook-io');

const toolInput = readToolInput();
const filePath = normalizePath(toolInput.file_path || toolInput.path);

if (!filePath || !filePath.endsWith('.json')) process.exit(0);

try {
  const content = fs.readFileSync(filePath, 'utf-8');
  JSON.parse(content);
  console.log('✓ JSON valid: ' + filePath);
} catch (e) {
  console.error('✗ Invalid JSON after edit: ' + filePath);
  console.error(e.message);
  process.exit(BLOCK);
}

process.exit(0);
