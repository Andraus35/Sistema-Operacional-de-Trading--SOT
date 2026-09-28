#!/usr/bin/env node
// Mantém o mapa do projeto (docs/mapa/, BL-019) sincronizado — garantia determinística,
// que não depende de o agente lembrar. Nunca bloqueia o agente (exit 0); o backstop é o CI (--check).
//
//   node scripts/map-sync.js post-edit      PostToolUse (Write|Edit|MultiEdit): se o arquivo editado
//                                           é um .md do escopo do mapa, regenera o mapa.
//   node scripts/map-sync.js stop           Stop/SubagentStop: se o mapa está desatualizado
//                                           (inclui edições via Bash/rename/delete), regenera.
//   node scripts/map-sync.js session-start  SessionStart: mesma verificação ao abrir a sessão — pega
//                                           mudanças feitas com hooks desativados, por outra
//                                           ferramenta ou fora deste repositório.
//
// Se o Python não está disponível (ou a geração falha), grava o marcador docs/mapa/.stale:
// o defasamento fica VISÍVEL e `build_map.py --check` (CI/pre-commit) passa a falhar até
// alguém regenerar. Assim a falha nunca é silenciosa.

const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const { readToolInput, normalizePath } = require('./hook-io');

const ROOT = path.join(__dirname, '..');
const BUILD = path.join(__dirname, 'build_map.py');
const MAP_DIR = path.join(ROOT, 'docs', 'mapa');
const STALE = path.join(MAP_DIR, '.stale');
// Mesmo escopo do scripts/check_refs.py (EXCLUDE) — arquivos fora dele não afetam o mapa.
const EXCLUDED = /(^|\/)(node_modules|\.git|UPGRADES|_legacy)(\/|$)|harness-eval\/runs\/|^docs\/mapa\//;

// "Python indisponível" inclui o stub da Microsoft Store no Windows (existe, mas não executa).
function pythonUnavailable(r) {
  if (r.error) return true;
  if (r.status === 9009) return true;
  return /Python was not found|Microsoft Store|não foi encontrado/i.test(String(r.stderr) + String(r.stdout));
}

function runBuild(args) {
  for (const [exe, pre] of [['python', []], ['python3', []], ['py', ['-3']]]) {
    const r = spawnSync(exe, [...pre, BUILD, ...args], { cwd: ROOT, encoding: 'utf8' });
    if (!pythonUnavailable(r)) return r;
  }
  return null;
}

function markStale(reason) {
  try {
    fs.mkdirSync(MAP_DIR, { recursive: true });
    fs.writeFileSync(
      STALE,
      'Mapa DEFASADO: ' + reason + '\nRegenerar: python scripts/build_map.py (remove este marcador).\n'
    );
  } catch (e) {
    console.error('map-sync: não foi possível gravar o marcador .stale: ' + e.message);
  }
}

function regenerate(reason) {
  const r = runBuild([]);
  if (!r) {
    markStale('Python não encontrado (' + reason + ')');
    console.error('map-sync: Python não encontrado — mapa marcado como DEFASADO (docs/mapa/.stale); o CI/pre-commit falham até regenerar.');
    return;
  }
  if (r.status !== 0) {
    markStale('falha ao gerar (' + reason + ')');
    console.error('map-sync: falha ao gerar o mapa (' + reason + '); marcado como DEFASADO:\n' + (r.stderr || r.stdout));
    return;
  }
  console.log('map-sync: mapa atualizado (' + reason + ').');
}

function checkAndHeal() {
  const r = runBuild(['--check']);
  if (!r) {
    markStale('Python não encontrado (verificação de fim/início de sessão)');
    console.error('map-sync: Python não encontrado — não foi possível verificar o mapa; marcado como DEFASADO por segurança.');
  } else if (r.status !== 0) {
    regenerate(r.status === 2 ? 'mapa ausente' : 'mapa desatualizado');
  }
}

const mode = process.argv[2];

if (mode === 'post-edit') {
  const input = readToolInput();
  if (!input.file_path && !input.path) process.exit(0);
  const abs = path.resolve(ROOT, String(input.file_path || input.path));
  const rel = normalizePath(path.relative(ROOT, abs));
  if (rel.startsWith('..') || !/\.md$/i.test(rel) || EXCLUDED.test(rel)) process.exit(0);
  regenerate(rel);
} else if (mode === 'stop' || mode === 'session-start') {
  checkAndHeal();
} else {
  console.error('uso: node scripts/map-sync.js post-edit|stop|session-start');
}

process.exit(0);
