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
// Limites honestos: ids de agentes lançados antes de uma compactação/retomada da sessão não são reconhecidos (fail-open);
// o histórico é assíncrono — por isso o marcador. É Detector/lembrete (ENF-03): nunca decide, nunca homologa; qualquer
// falha libera o encerramento (fail-open).
//   Registrado em .claude/settings.json → hooks.Stop

const fs = require('fs');
const { stateFile } = require('./andraus-ask-mark.js');

const SOT = /(especificador|revisor)\s*sot/i;

function analisar(transcriptText) {
  const idTipo = {};     // agentId -> subagent_type
  const lancados = {};   // tool_use.id (Agent) -> subagent_type
  let ultimaPergunta = 0;
  const entregas = [];   // { ts, id, tipo }
  for (const linha of transcriptText.split('\n')) {
    if (!linha.trim()) continue;
    let o; try { o = JSON.parse(linha); } catch (_) { continue; }
    const ts = Date.parse(o.timestamp || '') || 0;
    const conteudo = o.message && o.message.content;
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
  return { ultimaPergunta, entregas };
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

if (require.main === module) {
  try {
    let raw = '';
    try { raw = fs.readFileSync(0, 'utf8'); } catch (_) { /* sem stdin */ }
    const payload = raw.trim() ? JSON.parse(raw) : {};
    if (payload.stop_hook_active || !payload.transcript_path || !fs.existsSync(payload.transcript_path)) process.exit(0);
    const { file } = stateFile(payload.session_id);
    let estado = {}; try { estado = JSON.parse(fs.readFileSync(file, 'utf8')); } catch (_) { /* sem estado */ }
    const d = decidir(payload, fs.readFileSync(payload.transcript_path, 'utf8'), estado);
    if (d) {
      estado.blockedForTs = d.maisRecente;
      try { fs.mkdirSync(require('path').dirname(file), { recursive: true }); fs.writeFileSync(file, JSON.stringify(estado)); } catch (_) { /* estado é best-effort */ }
      process.stdout.write(JSON.stringify({ decision: 'block', reason: d.reason }));
    }
  } catch (_) { /* fail-open */ }
  process.exit(0);
}

module.exports = { analisar, decidir };
