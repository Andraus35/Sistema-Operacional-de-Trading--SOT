// Testa a trava de fim de turno e o marcador de perguntas a Andraus (scripts/andraus-ask-guard.js, andraus-ask-mark.js)
// e o lembrete de lançamento corrigido (scripts/andraus-ask-reminder.js). Históricos SINTÉTICOS em diretório temporário.
const { spawnSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');
const root = path.join(__dirname, '..');
let fail = 0;

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sot-ask-test-'));
const iso = (ms) => new Date(ms).toISOString();
const T0 = Date.parse('2026-10-01T10:00:00Z');   // no PASSADO: o marcador usa Date.now() e precisa ser mais novo que as entregas simuladas

function run(script, payload, stateDir) {
  return spawnSync('node', [path.join(root, 'scripts', script)], {
    input: payload === undefined ? '' : JSON.stringify(payload),
    env: { ...process.env, SOT_ASK_STATE_DIR: stateDir },
    encoding: 'utf8',
  });
}
function check(name, cond, extra) {
  if (!cond) fail++;
  console.log(`  ${cond ? 'PASS' : 'FAIL'} [${name}]${cond ? '' : ' ' + (extra || '')}`);
}

// --- construtores de histórico (formato real observado: tool_use/tool_result em message.content; entregas em registros de texto)
const launch = (ms, toolId, type) => ({ type: 'assistant', timestamp: iso(ms), message: { content: [{ type: 'tool_use', id: toolId, name: 'Agent', input: { subagent_type: type } }] } });
const launched = (ms, toolId, agentId) => ({ type: 'user', timestamp: iso(ms), message: { content: [{ type: 'tool_result', tool_use_id: toolId, content: `Async agent launched successfully.\nagentId: ${agentId} (internal ID)` }] } });
const handback = (ms, agentId) => ({ type: 'queue-operation', timestamp: iso(ms), content: `<agent-message from="${agentId}">\n[Subagent hand-back] pronto\n</agent-message>` });
const notif = (ms, agentId) => ({ type: 'attachment', timestamp: iso(ms), attachment: { text: `<task-notification><task-id>${agentId}</task-id><status>completed</status></task-notification>` } });
const ask = (ms) => ({ type: 'assistant', timestamp: iso(ms), message: { content: [{ type: 'tool_use', id: 'q' + ms, name: 'AskUserQuestion', input: {} }] } });
const jsonl = (evs) => evs.map((e) => JSON.stringify(e)).join('\n') + '\n';

let n = 0;
function caso(evs, extra = {}) {
  n++;
  const dir = path.join(tmp, 'c' + n); fs.mkdirSync(dir);
  const tp = path.join(dir, 't.jsonl');
  if (evs !== null) fs.writeFileSync(tp, typeof evs === 'string' ? evs : jsonl(evs));
  return { tp, state: path.join(dir, 'state'), sid: 'sess' + n, ...extra };
}
const stop = (c, over = {}) => run('andraus-ask-guard.js', { session_id: c.sid, transcript_path: c.tp, stop_hook_active: false, ...over }, c.state);
const blocked = (r) => { try { return JSON.parse(r.stdout).decision === 'block'; } catch (_) { return false; } };

const base = [launch(T0, 'tu1', 'Especificador SOT'), launched(T0 + 1, 'tu1', 'aaa111bbb222')];

// 1. sem entregas -> libera
let c = caso(base); let r = stop(c);
check('sem entregas libera', r.status === 0 && r.stdout === '', r.stdout);

// 2. entrega (hand-back) depois da última pergunta -> bloqueia, com orientação
c = caso([...base, ask(T0 + 10), handback(T0 + 20, 'aaa111bbb222')]); r = stop(c);
check('entrega depois da pergunta bloqueia', r.status === 0 && blocked(r), r.stdout);
check('motivo manda usar AskUserQuestion, linguagem de trader e recomendação', /AskUserQuestion/.test(r.stdout) && /trader/.test(r.stdout) && /Recomendado/.test(r.stdout));

// 3. notificação de tarefa também conta como entrega
c = caso([...base, notif(T0 + 20, 'aaa111bbb222')]); r = stop(c);
check('notificação de tarefa bloqueia', blocked(r), r.stdout);

// 4. pergunta DEPOIS da entrega -> libera
c = caso([...base, handback(T0 + 20, 'aaa111bbb222'), ask(T0 + 30)]); r = stop(c);
check('pergunta depois da entrega libera', r.status === 0 && r.stdout === '', r.stdout);

// 5. stop_hook_active nunca bloqueia (anti-laço)
c = caso([...base, handback(T0 + 20, 'aaa111bbb222')]); r = stop(c, { stop_hook_active: true });
check('stop_hook_active libera (sem laço)', r.stdout === '', r.stdout);

// 6. agente que não é Especificador/Revisor SOT não cobra
c = caso([launch(T0, 'tu9', 'Explore'), launched(T0 + 1, 'tu9', 'eee999fff000'), handback(T0 + 20, 'eee999fff000')]); r = stop(c);
check('agente não-SOT não cobra', r.stdout === '', r.stdout);

// 7. Revisor SOT cobra e o motivo o nomeia
c = caso([launch(T0, 'tu2', 'Revisor SOT'), launched(T0 + 1, 'tu2', 'rrr111sss222'), handback(T0 + 20, 'rrr111sss222')]); r = stop(c);
check('Revisor SOT cobra e é nomeado', blocked(r) && /Revisor SOT/.test(JSON.parse(r.stdout).reason), r.stdout);

// 8. marcador mais novo que a entrega (histórico atrasado) -> libera
c = caso([...base, handback(T0 + 20, 'aaa111bbb222')]); fs.mkdirSync(c.state, { recursive: true });
let m = run('andraus-ask-mark.js', { session_id: c.sid }, c.state);
check('marcador grava estado', m.status === 0 && fs.readdirSync(c.state).length === 1);
// o marcador usa Date.now() (>> T0 de 2026-10-07 pode ser passado/futuro): força comparação com entrega "antiga" no histórico
r = stop(c);
check('marcador (pergunta feita agora) vence entrega antiga do histórico', r.stdout === '', r.stdout);

// 9. não repete a cobrança pela mesma entrega
c = caso([...base, handback(T0 + 20, 'aaa111bbb222')]);
const r1 = stop(c), r2 = stop(c);
check('1ª vez bloqueia', blocked(r1)); check('2ª vez, mesma entrega, libera (não repete)', r2.stdout === '', r2.stdout);

// 10. entrega NOVA depois de ter cobrado -> cobra de novo
fs.appendFileSync(c.tp, jsonl([handback(T0 + 99999, 'aaa111bbb222')])); const r3 = stop(c);
check('entrega nova volta a cobrar', blocked(r3), r3.stdout);

// 11. fail-open: histórico inexistente, lixo, stdin vazio/JSON inválido
c = caso(null); r = stop(c); check('histórico inexistente libera', r.status === 0 && r.stdout === '');
c = caso('isto não é json\n{"a":\n'); r = stop(c); check('histórico corrompido libera', r.status === 0 && r.stdout === '');
r = run('andraus-ask-guard.js', undefined, path.join(tmp, 'x')); check('stdin vazio libera', r.status === 0 && r.stdout === '');
r = spawnSync('node', [path.join(root, 'scripts', 'andraus-ask-guard.js')], { input: '{quebrado', encoding: 'utf8' }); check('stdin inválido libera', r.status === 0 && r.stdout === '');

// 12. id de agente não lançado nesta sessão (sessão compactada) -> libera (limite documentado)
c = caso([handback(T0 + 20, 'zzz000yyy111')]); r = stop(c); check('id desconhecido libera (fail-open)', r.stdout === '');


// 14. 2ª regra — pergunta em TEXTO sem AskUserQuestion no turno -> bloqueia (1 vez por fala)
const humano = (ms, txt = 'pode seguir') => ({ type: 'user', timestamp: iso(ms), message: { content: txt } });
const fala = (ms, txt) => ({ type: 'assistant', timestamp: iso(ms), message: { content: [{ type: 'text', text: txt }] } });
c = caso([humano(T0), fala(T0 + 5, 'Fiz a ata.\n\nQuer que eu abra o PR agora?')]); r = stop(c);
check('pergunta em texto sem AskUserQuestion bloqueia', blocked(r) && /AskUserQuestion/.test(r.stdout) && /TEXTO/.test(r.stdout), r.stdout);
r = stop(c); check('não repete a cobrança pela mesma fala', r.stdout === '', r.stdout);

// 15. já houve AskUserQuestion depois da mensagem humana -> libera
c = caso([humano(T0), fala(T0 + 5, 'Quer que eu abra o PR?'), ask(T0 + 10)]); r = stop(c);
check('AskUserQuestion no turno libera', r.stdout === '', r.stdout);

// 16. afirmação sem pergunta -> libera
c = caso([humano(T0), fala(T0 + 5, 'PR aberto e conferido. Nada mais a decidir.')]); r = stop(c);
check('texto sem pergunta libera', r.stdout === '', r.stdout);

// 17. AskUserQuestion de turno ANTERIOR não vale para o turno novo
c = caso([humano(T0), ask(T0 + 2), humano(T0 + 10, 'ok, e agora?'), fala(T0 + 20, 'Posso montar o teste?')]); r = stop(c);
check('pergunta de turno anterior não conta', blocked(r), r.stdout);

// 18. mensagem sintética (notificação do sistema) NÃO é Andraus: ask anterior a ela ainda vale
c = caso([humano(T0), ask(T0 + 2), { type: 'user', timestamp: iso(T0 + 10), message: { content: '[SYSTEM NOTIFICATION - NOT USER INPUT] tarefa concluída' } }, fala(T0 + 20, 'Quer que eu siga?')]); r = stop(c);
check('notificação do sistema não reinicia o turno', r.stdout === '', r.stdout);

// 19. last_assistant_message do payload tem precedência sobre o histórico (que é assíncrono)
c = caso([humano(T0), fala(T0 + 5, 'Tudo certo.')]); r = stop(c, { last_assistant_message: 'Você decide: A ou B?' });
check('last_assistant_message do payload é usado', blocked(r), r.stdout);

// 20. stop_hook_active nunca bloqueia (também na 2ª regra)
c = caso([humano(T0), fala(T0 + 5, 'Quer que eu siga?')]); r = stop(c, { stop_hook_active: true });
check('2ª regra respeita stop_hook_active', r.stdout === '', r.stdout);

// 21. relatório com "?" no meio, mas fecha em afirmação -> libera
c = caso([humano(T0), fala(T0 + 5, 'O auditor achou algo? Sim, 9 achados.\n\nRelatório salvo em estresse-local/.')]); r = stop(c);
check('"?" no meio e fecho em afirmação libera', r.stdout === '', r.stdout);

// 13. lembrete de lançamento (B): em segundo plano NÃO diz que chegou entrega
const rem = (input) => spawnSync('node', [path.join(root, 'scripts', 'andraus-ask-reminder.js')], { input: JSON.stringify({ tool_name: 'Agent', tool_input: input }), encoding: 'utf8' });
let o = rem({ subagent_type: 'Especificador SOT', run_in_background: true });
check('lançamento em segundo plano: "AINDA NÃO HÁ ENTREGA"', /AINDA NÃO HÁ ENTREGA/.test(o.stdout) && !/acabou de chegar/.test(o.stdout), o.stdout);
o = rem({ subagent_type: 'Revisor SOT' });
check('padrão (sem run_in_background) também é segundo plano', /AINDA NÃO HÁ ENTREGA/.test(o.stdout), o.stdout);
o = rem({ subagent_type: 'Revisor SOT', run_in_background: false });
check('síncrono mantém "acabou de chegar uma entrega"', /acabou de chegar/.test(o.stdout), o.stdout);
o = rem({ subagent_type: 'Explore' }); check('outro agente não dispara lembrete', o.stdout === '');

fs.rmSync(tmp, { recursive: true, force: true });
console.log(fail ? `\n${fail} falha(s)` : '\nTodos os testes do guard/marcador/lembrete passaram');
process.exit(fail ? 1 : 0);
