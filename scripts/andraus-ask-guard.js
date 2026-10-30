#!/usr/bin/env node
// Trava DETERMINÍSTICA de fim de turno: o orquestrador não encerra a resposta sem perguntar a Andraus (AskUserQuestion)
// quando o Especificador SOT ou o Revisor SOT ENTREGARAM algo desde a última pergunta.
//
// Problema que resolve: o hook andraus-ask-reminder.js (PostToolUse/Agent) dispara no LANÇAMENTO do agente (em segundo
// plano a chamada volta na hora), nunca na ENTREGA — esta chega como mensagem de retorno/notificação de tarefa, sem
// chamada de ferramenta, e agentes retomados por SendMessage nem passam pelo matcher. Aqui o gancho é o evento Stop.
//
// Contrato (docs de hooks do Claude Code): Stop recebe { session_id, transcript_path, stop_hook_active, ... } em stdin;
// `{"decision":"block","reason":"..."}` em stdout impede o encerramento e entrega o motivo ao modelo. `stop_hook_active`
// = já estamos continuando por causa de um Stop hook → NUNCA bloquear de novo (evita laço infinito).
//
// Como detecta:
//   entregas  = registros do histórico com "Subagent hand-back" ou "<task-notification>" cujo id de agente (from="…" /
//               <task-id>…</task-id>) foi lançado nesta sessão com subagent_type Especificador/Revisor SOT.
//   pergunta  = max( último tool_use AskUserQuestion no histórico , marcador do andraus-ask-mark.js ).
//   bloqueia  = há entrega mais nova que a última pergunta E ainda não bloqueamos por essa mesma entrega (1 vez só).
// 2ª regra (DHR-ASK-002, 2026-10-11 — brecha vista na prática): o orquestrador encerrava o turno com uma pergunta ou oferta
// escrita em TEXTO ("Quer que eu…?") em vez de AskUserQuestion, e a 1ª regra só cobre entrega do Especificador/Revisor.
//   pergunta-em-texto = a última fala termina em pergunta/oferta/pedido de decisão E não houve AskUserQuestion depois da
//                       última mensagem HUMANA do turno. Bloqueia 1 vez por fala (mesmo hash) e nunca com stop_hook_active.
// 3ª regra (DHR-MERGE-001, 2026-10-30 — ordem de Andraus: "ser deterministicamente avisado quando já posso mesclar"):
//   pronto-para-mesclar = `python scripts/merge_ready.py --json` devolve PRONTO (PR aberto do ramo atual, mergeable_state clean, cabeça
//                         do PR == HEAD local, árvore limpa, todos os check-runs concluídos com sucesso). Bloqueia 1 vez por commit-cabeça
//                         e manda perguntar a Andraus por AskUserQuestion: "já é possível e seguro mesclar; mesclo ao seu comando".
//                         NUNCA mescla (a mesclagem é ato de Andraus — AGENTS.md §10). Indeterminado/erro de rede => libera (fail-open).
// Limites honestos: ids de agentes lançados antes de uma compactação/retomada da sessão não são reconhecidos (fail-open);
// o histórico é assíncrono — por isso o marcador. É Detector/lembrete (ENF-03): nunca decide, nunca homologa; qualquer
// falha libera o encerramento (fail-open).
//   Registrado em .claude/settings.json → hooks.Stop

const fs = require('fs');
const { stateFile } = require('./andraus-ask-mark.js');

const SOT = /(especificador|revisor)\s*sot/i;
// mensagens injetadas pelo sistema/hooks/agentes (role user, mas NÃO são Andraus)
const SINTETICA = /^\s*(<system-reminder|\[SYSTEM NOTIFICATION|Stop hook feedback|<agent-message|<task-notification|<ci-monitor-event|Another Claude session|\[Subagent|<command-)/i;
// pergunta/oferta/pedido de decisão ao final da fala
const OFERTA = /(quer que eu|posso (seguir|fazer|montar|preparar|come[cç]ar|abrir|aplicar|rodar)|voc[eê] (decide|prefere|quer|aprova|autoriza)|me diga|decis[aã]o (sua|de andraus)|confirma\b|aprova\b|autoriza\b)/i;

function ehPerguntaEmTexto(texto) {
  const fim = String(texto || '').trim().split('\n').filter((l) => l.trim()).slice(-3).join('\n');
  const ultima = fim.split('\n').slice(-1)[0] || '';
  return /\?\s*[*_`)"”]*\s*$/.test(fim) || OFERTA.test(ultima);
}

function analisar(transcriptText) {
  const idTipo = {};     // agentId -> subagent_type
  const lancados = {};   // tool_use.id (Agent) -> subagent_type
  let ultimaPergunta = 0;
  let ultimoHumano = 0;  // última mensagem de Andraus (não sintética) — separa "este turno" do anterior
  let ultimaFala = '';   // texto da última fala do assistente
  const entregas = [];   // { ts, id, tipo }
  for (const linha of transcriptText.split('\n')) {
    if (!linha.trim()) continue;
    let o; try { o = JSON.parse(linha); } catch (_) { continue; }
    const ts = Date.parse(o.timestamp || '') || 0;
    const conteudo = o.message && o.message.content;
    if (o.type === 'user' && conteudo !== undefined) {
      const txt = typeof conteudo === 'string' ? conteudo
        : (Array.isArray(conteudo) && !conteudo.some((b) => b && b.type === 'tool_result')
          ? conteudo.filter((b) => b && b.type === 'text').map((b) => b.text).join('\n') : '');
      if (txt.trim() && !SINTETICA.test(txt)) ultimoHumano = Math.max(ultimoHumano, ts);
    }
    if (o.type === 'assistant' && Array.isArray(conteudo)) {
      const t = conteudo.filter((b) => b && b.type === 'text').map((b) => b.text).join('\n').trim();
      if (t) ultimaFala = t;
    }
    if (Array.isArray(conteudo)) {
      for (const b of conteudo) {
        if (!b || typeof b !== 'object') continue;
        if (b.type === 'tool_use' && b.name === 'Agent' && b.input) lancados[b.id] = String(b.input.subagent_type || '');
        if (b.type === 'tool_use' && b.name === 'AskUserQuestion') ultimaPergunta = Math.max(ultimaPergunta, ts);
        if (b.type === 'tool_result' && lancados[b.tool_use_id] !== undefined) {
          const txt = typeof b.content === 'string' ? b.content : JSON.stringify(b.content || '');
          const m = /agentId:\s*([0-9a-z]+)/i.exec(txt);
          if (m) idTipo[m[1]] = lancados[b.tool_use_id];
        }
      }
    }
    if (linha.includes('Subagent hand-back') || linha.includes('<task-notification>')) {
      const ids = new Set();
      for (const m of linha.matchAll(/from=\\?"([0-9a-z]{8,})\\?"/g)) ids.add(m[1]);
      for (const m of linha.matchAll(/<task-id>([0-9a-z]{8,})<\/task-id>/g)) ids.add(m[1]);
      for (const id of ids) if (idTipo[id] && SOT.test(idTipo[id])) entregas.push({ ts, id, tipo: idTipo[id] });
    }
  }
  return { ultimaPergunta, ultimoHumano, ultimaFala, entregas };
}

function decidir(payload, transcriptText, estado) {
  if (payload.stop_hook_active) return null;
  const { ultimaPergunta, entregas } = analisar(transcriptText);
  const ultimaAsk = Math.max(ultimaPergunta, estado.lastAskMs || 0);
  const novas = entregas.filter((e) => e.ts > ultimaAsk);
  if (!novas.length) return null;
  const maisRecente = Math.max(...novas.map((e) => e.ts));
  if (estado.blockedForTs && estado.blockedForTs >= maisRecente) return null;   // já cobrei por esta entrega
  const quem = [...new Set(novas.map((e) => (/revisor/i.test(e.tipo) ? 'Revisor SOT (parecer)' : 'Especificador SOT (entrega)')))].join(' e ');
  return {
    maisRecente,
    reason: [
      `FIM DE TURNO BLOQUEADO (regra de Andraus) — chegou entrega de ${quem} desde a sua última pergunta a Andraus.`,
      'Antes de encerrar, FALE COM ANDRAUS usando AskUserQuestion:',
      '1. Linguagem NÃO técnica, de trader (sem siglas soltas; diga o que muda na prática).',
      '2. Resuma em 3 a 5 linhas simples: o que foi entregue, se passou (CONFORME/NÃO CONFORME), o que falta decidir.',
      '3. Cada pergunta com a recomendação em PRIMEIRO lugar, marcada "(Recomendado)", coerente com o SOT (hierarquia Elliott → Fibonacci → Fractal → SMC → ICT; R:R mínimo 1:3; SOT não executa ordem; custo fora da convicção; baseline só com homologação de Andraus).',
      '4. Nunca decida por Andraus, nunca homologue, nunca feche decisão aberta (CONS-01); se tocar decisão aberta, diga e ofereça "adiar".',
      'Se REALMENTE não houver decisão que dependa de Andraus, diga isso em uma frase e encerre: este bloqueio não se repete para a mesma entrega.',
    ].join('\n'),
  };
}

function decidirPergunta(payload, transcriptText, estado) {
  if (payload.stop_hook_active) return null;
  const { ultimaPergunta, ultimoHumano, ultimaFala } = analisar(transcriptText);
  const texto = (typeof payload.last_assistant_message === 'string' && payload.last_assistant_message.trim())
    ? payload.last_assistant_message : ultimaFala;
  if (!ehPerguntaEmTexto(texto)) return null;
  const ultimaAsk = Math.max(ultimaPergunta, estado.lastAskMs || 0);
  if (ultimaAsk > ultimoHumano) return null;                      // já perguntou por AskUserQuestion neste turno
  const hash = require('crypto').createHash('sha1').update(String(texto).trim().slice(-500)).digest('hex');
  if (estado.blockedTextHash === hash) return null;               // já cobrei por esta fala (1 vez só)
  return {
    hash,
    reason: [
      'FIM DE TURNO BLOQUEADO (regra de Andraus) — a sua resposta termina com uma pergunta/oferta/pedido de decisão escrita em TEXTO.',
      'Decisão que depende de Andraus vai por AskUserQuestion, não por texto. Reenvie agora:',
      '1. Resuma em 3 a 5 linhas simples (linguagem de trader, sem siglas soltas) o que já foi feito e o que falta decidir.',
      '2. Chame AskUserQuestion com a recomendação em PRIMEIRO lugar, marcada "(Recomendado)", coerente com o SOT (R:R mínimo 1:3; SOT não executa ordem; custo fora da convicção; baseline só com homologação de Andraus).',
      '3. Nunca decida por Andraus nem feche decisão aberta (CONS-01); se tocar decisão aberta, ofereça "adiar".',
      'Se a pergunta era RETÓRICA e não há decisão de Andraus, reescreva a resposta sem pergunta e encerre: este bloqueio não se repete para a mesma fala.',
    ].join('\n'),
  };
}

function consultarMerge() {
  // Chama o detector Python (REST via gh). Falha/timeout => null (fail-open).
  const { spawnSync } = require('child_process');
  for (const [exe, pre] of [['python', []], ['python3', []], ['py', ['-3']]]) {
    const r = spawnSync(exe, [...pre, require('path').join(__dirname, 'merge_ready.py'), '--json'], { encoding: 'utf8', timeout: 25000, cwd: require('path').join(__dirname, '..') });
    if (r.error || r.status === 9009) continue;
    try { return JSON.parse(r.stdout); } catch (_) { return null; }
  }
  return null;
}

function decidirMerge(payload, info, estado) {
  if (payload.stop_hook_active) return null;
  if (!info || info.estado !== 'PRONTO' || !info.extra) return null;
  const chave = `${info.extra.numero}@${info.extra.cabeca || ''}`;
  if (!info.extra.cabeca) return null;                                             // sem cabeça não há chave de deduplicação: não avisa
  if (estado.mergeNotified === chave) return null;                                 // já avisei por esta cabeça
  const donos = (info.extra.arquivos_de_andraus || []);
  return {
    merge: chave,
    reason: [
      `AVISO DETERMINÍSTICO (regra de Andraus) — JÁ É POSSÍVEL E SEGURO MESCLAR: PR #${info.extra.numero} (${info.extra.titulo}) ${info.extra.url}`,
      'Verificado por código: PR aberto, sem conflito, estado "clean", cabeça igual ao HEAD local, árvore limpa e todos os checks concluídos com sucesso.',
      donos.length ? `Atenção: o PR toca arquivos reservados a Andraus pelo CODEOWNERS (${donos.slice(0, 6).join(', ')}${donos.length > 6 ? ', …' : ''}) — a aprovação é dele.` : 'Nenhum arquivo reservado ao CODEOWNERS no PR.',
      'Antes de encerrar, FALE COM ANDRAUS usando AskUserQuestion (linguagem de trader, 3 a 5 linhas): diga que já é possível e seguro mesclar e que você mescla ao comando dele.',
      'Opções: "Mesclar agora (Recomendado)" · "Esperar mais trabalho antes de mesclar" · "Adiar". NÃO mescle sem a resposta dele (AGENTS.md §10); nunca feche decisão aberta (CONS-01).',
      'Este aviso não se repete para o mesmo commit-cabeça do PR.',
    ].join('\n'),
  };
}

if (require.main === module) {
  try {
    let raw = '';
    try { raw = fs.readFileSync(0, 'utf8'); } catch (_) { /* sem stdin */ }
    const payload = raw.trim() ? JSON.parse(raw) : {};
    if (payload.stop_hook_active || !payload.transcript_path || !fs.existsSync(payload.transcript_path)) process.exit(0);
    const { file } = stateFile(payload.session_id);
    let estado = {}; try { estado = JSON.parse(fs.readFileSync(file, 'utf8')); } catch (_) { /* sem estado */ }
    const texto = fs.readFileSync(payload.transcript_path, 'utf8');
    let d = decidir(payload, texto, estado) || decidirPergunta(payload, texto, estado);
    if (!d && !payload.stop_hook_active) d = decidirMerge(payload, consultarMerge(), estado);
    if (d) {
      if (d.merge) estado.mergeNotified = d.merge;
      if (d.maisRecente) estado.blockedForTs = d.maisRecente;
      if (d.hash) estado.blockedTextHash = d.hash;
      try { fs.mkdirSync(require('path').dirname(file), { recursive: true }); fs.writeFileSync(file, JSON.stringify(estado)); } catch (_) { /* estado é best-effort */ }
      process.stdout.write(JSON.stringify({ decision: 'block', reason: d.reason }));
    }
  } catch (_) { /* fail-open */ }
  process.exit(0);
}

module.exports = { analisar, decidir, decidirPergunta, decidirMerge, ehPerguntaEmTexto };
