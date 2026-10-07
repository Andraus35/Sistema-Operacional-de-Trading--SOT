#!/usr/bin/env node
// Lembrete DETERMINÍSTICO ao orquestrador (chat principal) depois que o Especificador SOT
// ou o Revisor SOT entregam: apresentar a Andraus perguntas automatizadas (AskUserQuestion)
// em linguagem NÃO técnica, para trader, com recomendação coerente com o SOT.
//
// Mecanismo: hook PostToolUse com matcher "Agent" (a chamada que delega ao subagente).
// O Claude Code injeta `additionalContext` no contexto do orquestrador — diferente do
// SubagentStop, cujo stdout só aparece na transcrição e cujo exit 2 reabriria o SUBAGENTE.
//
// É Detector/lembrete (ENF-03): nunca bloqueia (exit 0 sempre), nunca decide, nunca
// homologa. Quem decide é Andraus. Qualquer falha do hook é silenciosa (fail-open).
//
//   Registrado em .claude/settings.json → hooks.PostToolUse[matcher="Agent"]

const fs = require('fs');

function readStdin() {
  try { return fs.readFileSync(0, 'utf8'); } catch (_) { return ''; }
}

let payload = {};
try { payload = JSON.parse(readStdin() || '{}'); } catch (_) { process.exit(0); }

const input = payload.tool_input || {};
const agente = String(input.subagent_type || '');
const alvo = /(especificador|revisor)\s*sot/i;
if (!alvo.test(agente)) process.exit(0);

const papel = /revisor/i.test(agente) ? 'Revisor SOT (parecer)' : 'Especificador SOT (entrega)';

// Em segundo plano (padrão do Agent; só run_in_background:false é síncrono) a chamada VOLTA NA HORA, no lançamento — ainda não
// existe entrega. Dizer "acabou de chegar" aí era falso; a cobrança da entrega real é do hook de fim de turno
// (scripts/andraus-ask-guard.js), que enxerga o retorno do agente.
const emSegundoPlano = input.run_in_background !== false;
if (emSegundoPlano) {
  const aviso = [
    `LEMBRETE AO ORQUESTRADOR — ${papel.replace(/ \(.*\)/, '')} ACIONADO em segundo plano; AINDA NÃO HÁ ENTREGA nem parecer. Não pergunte a Andraus agora.`,
    'Quando a entrega/parecer chegar (relatório de retorno ou notificação de tarefa), resuma em 3 a 5 linhas simples e FALE COM ANDRAUS com AskUserQuestion:',
    'linguagem de trader, recomendação em PRIMEIRO lugar marcada "(Recomendado)", nunca decidir/homologar/fechar decisão aberta (CONS-01).',
    'O hook de fim de turno (scripts/andraus-ask-guard.js) bloqueia o encerramento da resposta se houver entrega sem pergunta.'
  ].join('\n');
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: 'PostToolUse', additionalContext: aviso } }));
  process.exit(0);
}

const texto = [
  `LEMBRETE AO ORQUESTRADOR — acabou de chegar uma entrega do ${papel}.`,
  'Antes de seguir adiante, FALE COM ANDRAUS usando AskUserQuestion (perguntas automatizadas):',
  '1. Linguagem NÃO técnica, de trader: sem siglas soltas (explique "Observação", "Evidência", "BASpec" em uma frase simples); diga o que muda na prática para analisar/operar.',
  '2. Resuma o resultado em 3 a 5 linhas simples: o que o agente entregou, se passou (CONFORME/NÃO CONFORME), o que ainda precisa de decisão.',
  '3. Cada pergunta traz a recomendação em PRIMEIRO lugar, marcada "(Recomendado)", coerente e coesa com o SOT: hierarquia Elliott → Fibonacci → Fractal → SMC → ICT; R:R mínimo 1:3; SOT não executa ordem (INV-05); dado de ferramenta é Observação, não Evidência (INV-06); custo nunca entra na convicção (INV-04); baseline só com homologação de Andraus.',
  '4. Nunca decida por Andraus, nunca homologue, nunca feche decisão aberta (CONS-01: J-001, N-001, M-001, H-001, WF-D03, ECC-03-001...). Se a escolha mexer em decisão aberta, diga isso com clareza e ofereça "adiar" como opção.',
  '5. Vale também quando uma decisão importante depender de escolha de Andraus, mesmo sem entrega de agente.'
].join('\n');

process.stdout.write(JSON.stringify({
  hookSpecificOutput: {
    hookEventName: 'PostToolUse',
    additionalContext: texto
  }
}));
process.exit(0);
