#!/usr/bin/env python3
"""
telemetria_tokens.py — telemetria de tokens/custo dos agentes CONSTRUTORES (AC) (BL-036; insumo: governance/propostas/TELEMETRIA-CUSTO/).

Uso:
  (sem argumentos)    hook PostToolUse/Agent: lê o evento em stdin e acrescenta UMA linha JSON a .telemetria/uso-tokens.jsonl.
  resumo [--json]     agrega por agente / modelo / classe-de-tarefa: chamadas, tokens (in/out/cache), custo estimado e tokens por chamada.

Garantias: DETECTOR (ENF-03) — nunca nega, nunca altera a chamada, falha => exit 0 silencioso. Não grava o texto do prompt nem da resposta
(só metadados). Custo = tokens x tabela versionada governance/telemetria/PRECOS-MODELOS.json; preço ausente => custo INDETERMINADO
(nenhum preço é inventado). Custo NUNCA entra no Conviction Vector (INV-04); só agentes AC (os AT ainda não existem — fase spec-first).
Dado de estado, não normativo; nada aqui homologa, fecha decisão aberta (CONS-01) ou promove item.
"""
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAIDA = ROOT / ".telemetria" / "uso-tokens.jsonl"
PRECOS = ROOT / "governance" / "telemetria" / "PRECOS-MODELOS.json"
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
    r = {"t": int(time.time()), "tool": ev.get("tool_name"), "agente": entrada.get("subagent_type") or entrada.get("to"),
         "model": entrada.get("model"), "classe": classe.group(1).upper() if classe else None,
         "sessao": ev.get("session_id")}
    for k, nome in CHAVES.items():
        r[nome] = _busca(resp, k)
    r["total"] = _busca(resp, "totalTokens")
    r["duracao_ms"] = _busca(resp, "totalDurationMs")
    r["tool_uses"] = _busca(resp, "totalToolUseCount")
    if r["total"] is None:
        parcelas = [r[n] for n in CHAVES.values() if r[n] is not None]
        r["total"] = sum(parcelas) if parcelas else None
    return r


def hook():
    try:
        ev = json.loads(sys.stdin.read() or "{}")
        if ev.get("tool_name") not in ("Agent", "Task"):
            return 0
        SAIDA.parent.mkdir(parents=True, exist_ok=True)
        with open(SAIDA, "a", encoding="utf-8") as f:
            f.write(json.dumps(extrair(ev), ensure_ascii=False) + "\n")
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


def resumo(registros):
    grupos = defaultdict(lambda: {"chamadas": 0, "sem_tokens": 0, "total": 0, "in": 0, "out": 0, "cache_read": 0,
                                  "cache_create": 0, "custo": 0.0, "custo_indet": 0})
    for r in registros:
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


def main(argv):
    if len(argv) < 2:
        return hook()
    if argv[1] != "resumo":
        print(__doc__)
        return 2
    regs = []
    if SAIDA.exists():
        for linha in SAIDA.read_text(encoding="utf-8").splitlines():
            try:
                regs.append(json.loads(linha))
            except ValueError:
                pass
    g = resumo(regs)
    if "--json" in argv:
        print(json.dumps({"|".join(k): v for k, v in g.items()}, ensure_ascii=False, indent=1))
        return 0
    print(f"Telemetria de tokens (AC) — {len(regs)} chamada(s) em {SAIDA.relative_to(ROOT)}")
    print("agente | modelo | classe | chamadas | tokens total | tokens/chamada | in | out | cache_r | cache_c | custo USD")
    for (a, m, c), v in sorted(g.items()):
        med = round(v["total"] / v["chamadas"]) if v["chamadas"] else 0
        cu = "INDETERMINADO" if v["custo_indet"] else f"{v['custo']:.4f}"
        print(f"{a} | {m} | {c} | {v['chamadas']} | {v['total']} | {med} | {v['in']} | {v['out']} | {v['cache_read']} | {v['cache_create']} | {cu}")
        if v["sem_tokens"]:
            print(f"  aviso: {v['sem_tokens']} chamada(s) sem tokens no evento (formato do tool_response não reconhecido)")
    print("LEMBRETE: Detector (ENF-03). Custo fora do Conviction Vector (INV-04). Tokens != qualidade (CEE-001).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
