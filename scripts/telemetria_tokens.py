#!/usr/bin/env python3
"""
telemetria_tokens.py — telemetria de tokens/custo dos agentes CONSTRUTORES (AC) (BL-036; insumo: governance/propostas/TELEMETRIA-CUSTO/).

Uso:
  (sem argumentos)    hook PostToolUse/Agent: lê o evento em stdin e acrescenta UMA linha JSON a .telemetria/uso-tokens.jsonl.
  custo-beneficio     cruza tokens por Spec (telemetria local) com os achados dos pareceres (loop_ledger): tokens por rodada, por achado e por achado Média/Crítica.
  snapshot            grava governance/aprendizado/TELEMETRIA-TOKENS.md (retrato datado, versionável; o ledger do loop aponta para ele).
  reconciliar [--sessao ID] [--projetos DIR]   (DHR-TELEMETRIA-002) lê o uso REAL dos transcripts dos subagentes (agent-*.jsonl + .meta.json), deduplicado por id de resposta, e grava/atualiza 1 registro por agente em .telemetria/uso-tokens.jsonl (idempotente). É também o que o hook SubagentStop/Stop executa sozinho.
  tokens AGENT_ID       imprime os tokens NOVOS (in+out+cache criado) do agente, para a convenção `TOKENS:` do parecer.
  resumo [--json] [--por-spec]   agrega por agente / modelo / classe-de-tarefa (ou por Spec / agente / classe): chamadas, tokens (in/out/cache), custo EQUIVALENTE API (não é cobrança) e tokens por chamada.

Garantias: DETECTOR (ENF-03) — nunca nega, nunca altera a chamada, falha => exit 0 silencioso. Não grava o texto do prompt nem da resposta
(só metadados). Custo = tokens x tabela versionada governance/telemetria/PRECOS-MODELOS.json; preço ausente => custo INDETERMINADO
(nenhum preço é inventado). Custo NUNCA entra no Conviction Vector (INV-04); só agentes AC (os AT ainda não existem — fase spec-first).
Dado de estado, não normativo; nada aqui homologa, fecha decisão aberta (CONS-01) ou promove item.
"""
import json
import re
import sys
import time
from datetime import datetime
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAIDA = ROOT / ".telemetria" / "uso-tokens.jsonl"
PRECOS = ROOT / "governance" / "telemetria" / "PRECOS-MODELOS.json"
PROJETOS = Path.home() / ".claude" / "projects"
VERSAO_REG = 2   # sobe quando o formato/semântica do registro de transcript muda (força reler transcripts já reconciliados)
OCIOSO_S = 1800   # intervalo entre mensagens acima disto = parado (rate limit, retomada, noite): não conta como tempo de trabalho
CHAVES = {"input_tokens": "in", "output_tokens": "out", "cache_read_input_tokens": "cache_read",
          "cache_creation_input_tokens": "cache_create"}


def _busca(obj, chave, prof=0):
    """Primeiro valor numérico de `chave` em dict/list aninhado (a forma exata de tool_response varia entre versões)."""
    if prof > 6:
        return None
    if isinstance(obj, dict):
        v = obj.get(chave)
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            return v
        for x in obj.values():
            r = _busca(x, chave, prof + 1)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for x in obj:
            r = _busca(x, chave, prof + 1)
            if r is not None:
                return r
    return None


def extrair(ev):
    """Evento PostToolUse -> registro de metadados (sem texto de prompt/resposta)."""
    entrada = ev.get("tool_input") or {}
    resp = ev.get("tool_response")
    prompt = str(entrada.get("prompt") or entrada.get("message") or "")
    classe = re.search(r"^\s*CLASSE-TAREFA:\s*(\w+)", prompt, re.M)
    alvo = re.search(r"^\s*ALVO:\s*(\S+)", prompt, re.M)
    spec = re.search(r"SPEC-\d{3}", (alvo.group(1) if alvo else "") + " " + prompt)
    r = {"t": int(time.time()), "tool": ev.get("tool_name"), "agente": entrada.get("subagent_type") or entrada.get("to"),
         "model": entrada.get("model"), "classe": classe.group(1).upper() if classe else None,
         "spec": spec.group(0) if spec else None, "alvo": alvo.group(1) if alvo else None, "sessao": ev.get("session_id")}
    for k, nome in CHAVES.items():
        r[nome] = _busca(resp, k)
    r["total"] = _busca(resp, "totalTokens")
    r["duracao_ms"] = _busca(resp, "totalDurationMs")
    r["tool_uses"] = _busca(resp, "totalToolUseCount")
    if r["total"] is None:
        parcelas = [r[n] for n in CHAVES.values() if r[n] is not None]
        r["total"] = sum(parcelas) if parcelas else None
    return r


def _forma_payload(ev):
    """B05 (DHR-LOGS-AC-001): so os NOMES das chaves do payload real (nunca valores), para conferir tool_use_id/prompt_id/agent_id/session_id."""
    d = SAIDA.parent / "payload-forma.jsonl"
    if d.exists() and d.stat().st_size > 20000:
        return
    forma = {"t": int(time.time()), "evento": ev.get("hook_event_name"), "tool": ev.get("tool_name"), "chaves": sorted(ev.keys()),
             "tool_input": sorted((ev.get("tool_input") or {}).keys()) if isinstance(ev.get("tool_input"), dict) else None,
             "tool_response": sorted(ev["tool_response"].keys()) if isinstance(ev.get("tool_response"), dict) else type(ev.get("tool_response")).__name__}
    with open(d, "a", encoding="utf-8") as f:
        f.write(json.dumps(forma, ensure_ascii=False) + "\n")


def _emitir_log(ev, reg):
    """DHR-LOGS-AC-001 (F2): agent.run no esquema do log dos Construtores (L1, local). Isolado: falha nunca afeta a telemetria legada."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import log_ac
    def i(v):
        return int(v) if isinstance(v, (int, float)) and not isinstance(v, bool) else None
    e = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "event": "agent.run", "family": "AC", "severity": "INFO",
         "status": "SUCCEEDED", "operation": "agent.run", "agent_id": str(reg.get("agente") or "desconhecido")[:128],
         "model": str(reg["model"])[:128] if reg.get("model") else None, "class": reg.get("classe"), "task_ref": reg.get("spec"),
         "metrics": {"in": i(reg.get("in")), "out": i(reg.get("out")), "cache_read": i(reg.get("cache_read")),
                     "cache_create": i(reg.get("cache_create")), "total": i(reg.get("total")), "duration_ms": i(reg.get("duracao_ms")),
                     "tool_uses": i(reg.get("tool_uses"))}}
    e = log_ac.completa_ids(e, ev)
    log_ac.emite_seguro(log_ac.raiz_repo() / ".telemetria" / "eventos.jsonl", e, "L1")


# ---------------------------------------------------------------------------------------------------------------------------
# DHR-TELEMETRIA-002 — telemetria dos subagentes a partir do TRANSCRIPT (a fonte real do uso).
# Causa da falha anterior: agente em segundo plano só devolve tokens no FIM, como notificação de tarefa (fora de qualquer chamada de
# ferramenta); o PostToolUse/Agent vê só "lançado" => 9 chamadas sem tokens. O transcript do subagente guarda `message.usage` por
# resposta, mas REPETE a mesma resposta em várias linhas (mesmo message.id): somar linhas dobraria/triplicaria o consumo => deduplica por id.
# ---------------------------------------------------------------------------------------------------------------------------
def _epoch(ts):
    try:
        return datetime.fromisoformat(str(ts).replace("Z", "+00:00")).timestamp()
    except (ValueError, TypeError):
        return None


def _texto_msg(m):
    c = m.get("content")
    if isinstance(c, str):
        return c
    return " ".join(b.get("text", "") for b in c if isinstance(b, dict)) if isinstance(c, list) else ""


def ler_transcript(caminho):
    """Uso REAL de um transcript de subagente. Determinístico (mesma entrada => mesma saída). None se ilegível/sem respostas."""
    caminho = Path(caminho)
    uso_por_id = {}
    modelos, usos_ferr = set(), set()
    t0 = t1 = None
    marcas = []
    agent_id = sessao = prompt0 = None
    try:
        linhas = caminho.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None
    for linha in linhas:
        try:
            d = json.loads(linha)
        except ValueError:
            continue
        if not isinstance(d, dict):
            continue
        agent_id = agent_id or d.get("agentId")
        sessao = sessao or d.get("sessionId")
        e = _epoch(d.get("timestamp"))
        if e is not None:
            marcas.append(e)
            t0 = e if t0 is None else min(t0, e)
            t1 = e if t1 is None else max(t1, e)
        m = d.get("message")
        if not isinstance(m, dict):
            continue
        if m.get("role") == "user" and prompt0 is None:
            prompt0 = _texto_msg(m)
        if m.get("role") != "assistant":
            continue
        mid = m.get("id") or d.get("uuid")
        u = m.get("usage") or {}
        uso_por_id[mid] = {n: int(u.get(k) or 0) for k, n in CHAVES.items()}   # mesma resposta repetida => 1 só (a última)
        if m.get("model"):
            modelos.add(m["model"])
        for b in (m.get("content") if isinstance(m.get("content"), list) else []):
            if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("id"):
                usos_ferr.add(b["id"])
    if not uso_por_id:
        return None
    soma = {n: sum(v[n] for v in uso_por_id.values()) for n in CHAVES.values()}
    marcas.sort()
    ativo = sum(b - a for a, b in zip(marcas, marcas[1:]) if b - a <= OCIOSO_S)   # tempo ATIVO: intervalos > 30 min = agente parado/retomado
    return {"agent_id": agent_id, "sessao": sessao, "modelos": sorted(modelos), "mensagens": len(uso_por_id), "tool_uses": len(usos_ferr),
            "duracao_ms": int(ativo * 1000) if marcas else None,
            "janela_ms": int((t1 - t0) * 1000) if t0 is not None and t1 is not None else None, "fim": t1, "prompt0": prompt0 or "", **soma}


def registro_de_transcript(caminho):
    """Registro no mesmo formato de `extrair`, com fonte='transcript'. `total` = tokens NOVOS (in+out+cache criado); o cache lido
    (re-leitura do contexto a cada turno) fica à parte e só entra no custo. None se não houver uso."""
    caminho = Path(caminho)
    u = ler_transcript(caminho)
    if not u:
        return None
    try:
        meta = json.loads(caminho.with_suffix(".meta.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        meta = {}
    prompt = u["prompt0"]
    classe = re.search(r"^\s*CLASSE-TAREFA:\s*(\w+)", prompt, re.M)
    alvo = re.search(r"^\s*ALVO:\s*(\S+)", prompt, re.M)
    spec = re.search(r"SPEC-\d{3}", (alvo.group(1) if alvo else "") + " " + prompt)
    try:
        nbytes = caminho.stat().st_size
    except OSError:
        nbytes = None
    return {"t": int(u["fim"]) if u["fim"] is not None else int(time.time()), "tool": "Agent", "agente": meta.get("agentType"),
            "model": meta.get("model") or (u["modelos"][0] if u["modelos"] else None), "classe": classe.group(1).upper() if classe else None,
            "spec": spec.group(0) if spec else None, "alvo": alvo.group(1) if alvo else None, "sessao": u["sessao"], "agent_id": u["agent_id"],
            "in": u["in"], "out": u["out"], "cache_read": u["cache_read"], "cache_create": u["cache_create"],
            "total": u["in"] + u["out"] + u["cache_create"], "duracao_ms": u["duracao_ms"], "janela_ms": u["janela_ms"], "tool_uses": u["tool_uses"],
            "mensagens": u["mensagens"], "descricao": meta.get("description"), "finalizado": bool(meta.get("finished")),
            "fonte": "transcript", "bytes": nbytes, "v": VERSAO_REG}


def _transcritos(projetos=None, sessao=None, agent_id=None, caminho=None):
    if caminho:
        return [Path(caminho)]
    base = Path(projetos) if projetos else PROJETOS
    slug = str(ROOT).replace("/", "-").replace("\\", "-")
    pasta = base / slug if (base / slug).is_dir() else base
    padrao = f"{sessao}/subagents/agent-*.jsonl" if sessao else "*/subagents/agent-*.jsonl"
    arqs = sorted(pasta.glob(padrao))
    if agent_id:
        arqs = [a for a in arqs if a.name == f"agent-{agent_id}.jsonl"]
    return arqs


def reconciliar(projetos=None, sessao=None, agent_id=None, caminho=None, saida=None):
    """Grava/atualiza 1 registro por subagente (chave agent_id). Idempotente: transcript do mesmo tamanho (`bytes`) não é relido.
    Substitui os 'stubs de lançamento' (chamada Agent/SendMessage sem tokens) das sessões reconciliadas. -> (gravados, ignorados)."""
    saida = Path(saida) if saida else SAIDA
    regs = []
    if saida.exists():
        for linha in saida.read_text(encoding="utf-8").splitlines():
            try:
                regs.append(json.loads(linha))
            except ValueError:
                pass
    existentes = {r.get("agent_id"): r for r in regs if r.get("fonte") == "transcript" and r.get("agent_id")}
    novos, ignorados, sessoes = {}, 0, set()
    for arq in _transcritos(projetos, sessao, agent_id, caminho):
        reg = registro_de_transcript(arq)
        if not reg or not reg.get("agent_id"):
            continue
        ant = existentes.get(reg["agent_id"])
        if ant and ant.get("v") == VERSAO_REG and ant.get("bytes") == reg.get("bytes") and ant.get("finalizado") == reg.get("finalizado"):
            ignorados += 1
            sessoes.add(reg.get("sessao"))
            continue
        novos[reg["agent_id"]] = reg
        sessoes.add(reg.get("sessao"))
    if not novos:
        return 0, ignorados
    out = [r for r in regs if not (r.get("fonte") == "transcript" and r.get("agent_id") in novos)]
    out = [r for r in out if not (r.get("fonte") != "transcript" and r.get("tool") in ("Agent", "Task", "SendMessage")
                                   and r.get("total") is None and r.get("sessao") in sessoes)]
    out += sorted(novos.values(), key=lambda r: (r.get("t") or 0, r.get("agent_id") or ""))
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in out), encoding="utf-8")
    return len(novos), ignorados


def hook():
    try:
        ev = json.loads(sys.stdin.read() or "{}")
        if ev.get("hook_event_name") in ("SubagentStop", "Stop"):
            # DHR-TELEMETRIA-002: o uso real só existe no fim do agente (transcript); reconcilia (idempotente, fail-open).
            try:
                reconciliar(sessao=ev.get("session_id"), agent_id=ev.get("agent_id") if ev.get("hook_event_name") == "SubagentStop" else None,
                            caminho=ev.get("agent_transcript_path") if ev.get("hook_event_name") == "SubagentStop" else None)
            except BaseException:
                pass
            return 0
        if ev.get("tool_name") not in ("Agent", "Task"):
            return 0
        SAIDA.parent.mkdir(parents=True, exist_ok=True)
        reg = extrair(ev)
        if reg.get("total") is None:
            reg["lancamento"] = True   # agente em segundo plano: o uso virá do transcript (reconciliar), não deste evento
        with open(SAIDA, "a", encoding="utf-8") as f:
            f.write(json.dumps(reg, ensure_ascii=False) + "\n")
        for f_ in (_forma_payload, ):
            try: f_(ev)
            except BaseException: pass
        try: _emitir_log(ev, reg)
        except BaseException: pass
    except Exception:
        pass
    return 0


def _preco(modelo):
    try:
        tab = json.loads(PRECOS.read_text(encoding="utf-8")).get("modelos", {})
    except (OSError, ValueError):
        return None
    for nome, p in tab.items():
        if modelo and nome in str(modelo).lower():
            return p
    return None


def custo(reg):
    """USD estimado ou None (INDETERMINADO) se faltar preço para qualquer parcela com tokens."""
    p = _preco(reg.get("model"))
    if not p:
        return None
    mapa = {"in": "input", "out": "output", "cache_read": "cache_read", "cache_create": "cache_create"}
    total = 0.0
    for nome, campo in mapa.items():
        n = reg.get(nome)
        if n:
            if p.get(campo) is None:
                return None
            total += n * p[campo] / 1_000_000
    return total


def resumo(registros, por="agente"):
    grupos = defaultdict(lambda: {"chamadas": 0, "sem_tokens": 0, "total": 0, "in": 0, "out": 0, "cache_read": 0,
                                  "cache_create": 0, "custo": 0.0, "custo_indet": 0})
    for r in registros:
        if r.get("lancamento"):
            continue                      # stub de lançamento (agente em segundo plano): o uso real vem do registro de transcript
        if por == "spec":
            g = grupos[(r.get("spec") or "sem-spec", r.get("agente") or "?", r.get("classe") or "-")]
        else:
            g = grupos[(r.get("agente") or "?", r.get("model") or "frontmatter", r.get("classe") or "-")]
        g["chamadas"] += 1
        if r.get("total") is None:
            g["sem_tokens"] += 1
        g["total"] += r.get("total") or 0
        for n in CHAVES.values():
            g[n] += r.get(n) or 0
        c = custo(r)
        if c is None:
            g["custo_indet"] += 1
        else:
            g["custo"] += c
    return grupos


SNAP = ROOT / "governance" / "aprendizado" / "TELEMETRIA-TOKENS.md"


def snapshot(regs):
    g = resumo(regs)
    out = ["# TELEMETRIA DE TOKENS DOS CONSTRUTORES — retrato (gerado por `python scripts/telemetria_tokens.py snapshot`)", "",
           "> Dado de estado, NÃO normativo (BL-036 / DHR-TELEMETRIA-CUSTO-001). **Detector (ENF-03)**: não bloqueia, não fecha decisão aberta. "
           "Custo fora do Conviction Vector (INV-04). Tokens ≠ qualidade (CEE-001): ler junto de Eficácia, nunca isolado. "
           f"Retrato de {len(regs)} chamada(s) em {time.strftime('%Y-%m-%d', time.gmtime())}; custo = EQUIVALENTE a preço de tabela da API, NÃO cobrança (no plano Pro o custo marginal é zero); preços em `governance/telemetria/PRECOS-MODELOS.json` (null => INDETERMINADO).", "",
           "| Agente | Modelo | Classe | Chamadas | Tokens total | Tokens/chamada | in | out | cache lido | cache criado | Custo equivalente API (USD) |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for (a, m, c), v in sorted(g.items()):
        med = round(v["total"] / v["chamadas"]) if v["chamadas"] else 0
        cu = "INDETERMINADO" if v["custo_indet"] else f"{v['custo']:.4f}"
        out.append(f"| {a} | {m} | {c} | {v['chamadas']} | {v['total']} | {med} | {v['in']} | {v['out']} | {v['cache_read']} | {v['cache_create']} | {cu} |")
    return "\n".join(out) + "\n"


def custo_beneficio(regs, linhas):
    """Cruza tokens por Spec (telemetria) com rodadas/achados (loop_ledger.coletar). Só razões; sem juízo de mérito.
    Spec sem telemetria => tokens 'n/m' (não medido; nunca estimar). Tokens != qualidade (CEE-001): ler junto das severidades."""
    tok = defaultdict(int)
    for r in regs:
        if r.get("spec") and r.get("total") is not None:
            tok[r["spec"]] += r["total"]
    por_spec = defaultdict(lambda: {"rodadas": 0, "Crítica": 0, "Média": 0, "Menor": 0})
    for chave, rodadas in linhas.items():
        spec = chave.split()[0]
        for d in rodadas.values():
            s = por_spec[spec]
            s["rodadas"] += 1
            for a in d["achados"]:
                s[a["sev"]] = s.get(a["sev"], 0) + 1
    linhas_out = []
    for spec in sorted(set(por_spec) | set(tok)):
        s = por_spec.get(spec, {"rodadas": 0, "Crítica": 0, "Média": 0, "Menor": 0})
        n = tok.get(spec)
        graves = s["Crítica"] + s["Média"]
        total = graves + s["Menor"]
        linhas_out.append({"spec": spec, "rodadas": s["rodadas"], "criticas": s["Crítica"], "medias": s["Média"], "menores": s["Menor"],
                           "tokens": n,
                           "tokens_por_rodada": round(n / s["rodadas"]) if n is not None and s["rodadas"] else None,
                           "tokens_por_achado": round(n / total) if n is not None and total else None,
                           "tokens_por_achado_grave": round(n / graves) if n is not None and graves else None})
    return linhas_out


def _ler():
    regs = []
    if SAIDA.exists():
        for linha in SAIDA.read_text(encoding="utf-8").splitlines():
            try:
                regs.append(json.loads(linha))
            except ValueError:
                pass
    return regs


def main(argv):
    if len(argv) < 2:
        return hook()
    if argv[1] == "custo-beneficio":
        sys.path.insert(0, str(ROOT / "scripts"))
        import loop_ledger
        res = custo_beneficio(_ler(), loop_ledger.coletar(ROOT))
        if "--json" in argv:
            print(json.dumps(res, ensure_ascii=False, indent=1))
            return 0
        print("spec | rodadas | crít | méd | men | tokens | tokens/rodada | tokens/achado | tokens/achado grave (Crítica+Média)")
        f = lambda v: "n/m" if v is None else v
        for r in res:
            print(f"{r['spec']} | {r['rodadas']} | {r['criticas']} | {r['medias']} | {r['menores']} | {f(r['tokens'])} | {f(r['tokens_por_rodada'])} | {f(r['tokens_por_achado'])} | {f(r['tokens_por_achado_grave'])}")
        print("LEMBRETE: Detector (ENF-03). n/m = telemetria sem registro da Spec (nunca estimado). Menos tokens por achado NÃO é melhor por si (Eficiência só sobre Eficácia válida, CEE-001); custo fora do Conviction Vector (INV-04).")
        return 0
    if argv[1] == "reconciliar":
        def _arg(nome):
            return argv[argv.index(nome) + 1] if nome in argv and argv.index(nome) + 1 < len(argv) else None
        g, i = reconciliar(projetos=_arg("--projetos"), sessao=_arg("--sessao"))
        print(f"reconciliado: {g} registro(s) gravado(s)/atualizado(s), {i} já em dia (fonte: transcripts dos subagentes).")
        return 0
    if argv[1] == "tokens":
        alvo = argv[2] if len(argv) > 2 else ""
        regs = [r for r in _ler() if r.get("agent_id") == alvo and r.get("fonte") == "transcript"]
        if not regs:
            print("n/m")
            return 1
        print(regs[-1]["total"])
        return 0
    if argv[1] == "snapshot":
        regs = _ler()
        if not regs:
            print("Sem telemetria local (.telemetria/uso-tokens.jsonl): nada a gravar.")
            return 1
        SNAP.write_text(snapshot(regs), encoding="utf-8")
        print(f"gravado {SNAP.relative_to(ROOT)} ({len(regs)} chamada(s))")
        return 0
    if argv[1] != "resumo":
        print(__doc__)
        return 2
    regs = _ler()
    por = "spec" if "--por-spec" in argv else "agente"
    g = resumo(regs, por)
    if "--json" in argv:
        print(json.dumps({"|".join(k): v for k, v in g.items()}, ensure_ascii=False, indent=1))
        return 0
    print(f"Telemetria de tokens (AC) — {len(regs)} chamada(s) em {SAIDA.relative_to(ROOT)}")
    print(("spec | agente | classe" if por == "spec" else "agente | modelo | classe") + " | chamadas | tokens total | tokens/chamada | in | out | cache_r | cache_c | custo equivalente API USD (não é cobrança)")
    for (a, m, c), v in sorted(g.items()):
        med = round(v["total"] / v["chamadas"]) if v["chamadas"] else 0
        cu = "INDETERMINADO" if v["custo_indet"] else f"{v['custo']:.4f}"
        print(f"{a} | {m} | {c} | {v['chamadas']} | {v['total']} | {med} | {v['in']} | {v['out']} | {v['cache_read']} | {v['cache_create']} | {cu}")
        if v["sem_tokens"]:
            print(f"  aviso: {v['sem_tokens']} chamada(s) sem tokens no evento (formato do tool_response não reconhecido)")
    print("LEMBRETE: Detector (ENF-03). Custo = equivalente a preço de API, NÃO cobrança (Pro = assinatura fixa). Fora do Conviction Vector (INV-04). Tokens != qualidade (CEE-001).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
