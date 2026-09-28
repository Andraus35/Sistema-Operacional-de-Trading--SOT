#!/usr/bin/env node
// Validates that all JSON schema files in schemas/ are valid JSON and have required fields.

const fs = require('fs');
const path = require('path');

const schemasDir = path.join(__dirname, '..', 'schemas');
let passed = 0;
let failed = 0;

function check(condition, message, file) {
  if (!condition) {
    console.error(`  FAIL [${file}]: ${message}`);
    failed++;
    return false;
  }
  return true;
}

const files = fs.readdirSync(schemasDir).filter(f => f.endsWith('.json'));

for (const file of files) {
  const filePath = path.join(schemasDir, file);
  let schema;

  try {
    schema = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  } catch (e) {
    console.error(`  FAIL [${file}]: Invalid JSON — ${e.message}`);
    failed++;
    continue;
  }

  let ok = true;
  ok = check(schema.$schema, 'Missing $schema field', file) && ok;
  ok = check(schema.$id, 'Missing $id field', file) && ok;
  ok = check(schema.title, 'Missing title field', file) && ok;
  ok = check(schema.type === 'object', 'Root type must be "object"', file) && ok;

  // Output schemas must declare a score field
  if (file.includes('.output.')) {
    const hasScore = schema.properties && (
      schema.properties.score !== undefined ||
      schema.properties.score_total !== undefined ||
      schema.properties.ict_score !== undefined ||
      schema.properties.smc_score !== undefined ||
      schema.properties.elliott_score !== undefined ||
      schema.properties.geometric_conviction_pct !== undefined
    );
    ok = check(hasScore, 'Output schema must declare a score property', file) && ok;
  }

  if (ok) {
    console.log(`  PASS [${file}]`);
    passed++;
  }
}

console.log(`\nResults: ${passed} passed, ${failed} failed out of ${files.length} schemas`);

if (failed > 0) process.exit(1);
