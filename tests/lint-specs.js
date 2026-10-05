#!/usr/bin/env node
// Lints spec files in specs/ (root) and specs/features/*/plan.md for required sections and EARS notation.
// GEN-1_REFERENCE files are skipped (they carry normative_authority: NONE).

const fs = require('fs');
const path = require('path');

const specsDir = path.join(__dirname, '..', 'specs');
let passed = 0;
let failed = 0;
let skipped = 0;

const REQUIRED_SECTIONS = [
  ['## Missão'],
  ['## Escopo'],
  ['## Antiescopo', 'Fora do escopo', 'Non-goals'],
  ['## Comportamento', '## Comportamentos'],
  ['## Critérios'],
];

const EARS_PATTERN = /\*?\*?Quando\*?\*?\s+.+,?\s+o agente DEVE/;

// Required metadata fields for features/*/plan.md (BASpec format)
const PLAN_REQUIRED_FIELDS = ['Status:', 'Complexidade:', 'Profundidade-alvo:'];

function lintRootSpec(filePath, label) {
  const content = fs.readFileSync(filePath, 'utf-8');

  if (content.includes('GEN-1_REFERENCE') || content.includes('normative_authority: NONE')) {
    console.log(`  SKIP [${label}]: GEN-1_REFERENCE — not normative`);
    skipped++;
    return;
  }

  let fileFailed = false;
  for (const alternatives of REQUIRED_SECTIONS) {
    const found = alternatives.some(s => content.includes(s));
    if (!found) {
      console.error(`  FAIL [${label}]: Missing section (one of: "${alternatives.join('", "')}")`);
      fileFailed = true;
    }
  }
  if (!EARS_PATTERN.test(content)) {
    console.error(`  FAIL [${label}]: No EARS notation found (Quando..., o agente DEVE...)`);
    fileFailed = true;
  }
  if (!fileFailed) { console.log(`  PASS [${label}]`); passed++; } else { failed++; }
}

function lintFeaturePlan(filePath, label) {
  const content = fs.readFileSync(filePath, 'utf-8');
  let fileFailed = false;
  for (const field of PLAN_REQUIRED_FIELDS) {
    // Aceita "Campo:" (linha) ou o cabeçalho em tabela "| Campo | valor |" usado nos planos atuais.
    const name = field.replace(/:$/, '');
    const asTableRow = new RegExp('^\\s*\\|\\s*' + name + '\\s*\\|', 'm');
    if (!content.includes(field) && !asTableRow.test(content)) {
      console.error(`  FAIL [${label}]: Missing metadata field "${field}"`);
      fileFailed = true;
    }
  }
  if (!fileFailed) { console.log(`  PASS [${label}]`); passed++; } else { failed++; }
}

function lintFeatureChecks(filePath, label) {
  const content = fs.readFileSync(filePath, 'utf-8');
  // checks.md only needs to exist and have a heading — structural gate is python validate_spec_sot.py
  if (content.trim().length < 10) {
    console.error(`  FAIL [${label}]: checks.md appears empty`);
    failed++;
  } else {
    console.log(`  PASS [${label}]`);
    passed++;
  }
}

// Lint root specs/*.spec.md
const rootFiles = fs.readdirSync(specsDir).filter(f => f.endsWith('.md'));
for (const file of rootFiles) {
  lintRootSpec(path.join(specsDir, file), file);
}

// Lint specs/features/*/plan.md and checks.md recursively (different rules per file type)
const featuresDir = path.join(specsDir, 'features');
if (fs.existsSync(featuresDir)) {
  const featureDirs = fs.readdirSync(featuresDir, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name);

  for (const featureDir of featureDirs) {
    const featurePath = path.join(featuresDir, featureDir);
    const planPath = path.join(featurePath, 'plan.md');
    const checksPath = path.join(featurePath, 'checks.md');
    if (fs.existsSync(planPath)) lintFeaturePlan(planPath, `features/${featureDir}/plan.md`);
    if (fs.existsSync(checksPath)) lintFeatureChecks(checksPath, `features/${featureDir}/checks.md`);
  }
}

const total = passed + failed + skipped;
console.log(`\nResults: ${passed} passed, ${failed} failed, ${skipped} skipped (GEN-1) out of ${total} files`);

if (failed > 0) process.exit(1);
