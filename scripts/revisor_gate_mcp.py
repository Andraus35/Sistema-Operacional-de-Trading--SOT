#!/usr/bin/env python3
"""
revisor_gate_mcp.py — FERRAMENTA ESTREITA do Revisor SOT (DHR-AUDITOR-EXTERNO-009, fase F2). Servidor MCP local (stdio).

Expõe UMA ferramenta, `revisor_gate(spec, rapido?)`, que roda o gate fundido (scripts/revisor_gate.py) numa Spec e devolve o
relatório. É o que permite ao Revisor "rodar o gate" SEM Bash e SEM escrita (ENF-03):
  - argumento `spec` validado por padrão fixo ^SPEC-NNN$ (lista de permissão, não sanitização); nada é interpretado por shell;
  - o caminho resolvido tem de ficar DENTRO de specs/features/ (barra symlink e `..`);
  - nenhuma ferramenta de escrita, execução arbitrária ou rede; os detectores chamados são somente leitura;
  - a árvore de trabalho é comparada antes/depois (`git status --porcelain`): se mudar, o resultado vira erro;
  - qualquer coisa fora do padrão é RECUSADA no servidor (a segurança não depende de o modelo se comportar).
Falha fechada: sem este servidor o Revisor não tem a ferramenta e declara "gate não verificado" (parecer no máximo condicional).

Protocolo MCP sobre stdio (JSON-RPC, uma mensagem por linha). Configuração (exemplo, usada na F3 pelo arquivo do Revisor):
  mcpServers: [{ sot-revisor-gate: { type: stdio, command: python, args: [scripts/revisor_gate_mcp.py] } }]
  tools: Read, Grep, Glob, mcp__sot-revisor-gate__revisor_gate        (sem Write, Edit ou Bash)
Variável opcional SOT_REPO (testes): raiz do repositório a servir; padrão = pasta pai de scripts/.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import revisor_gate  # noqa: E402
import gate_manifest  # noqa: E402

REPO = Path(os.environ.get("SOT_REPO") or HERE.parent).resolve()
SPEC = re.compile(r"^SPEC-[0-9]{3}$")
SERVER = {"name": "sot-revisor-gate", "version": "1.0.0"}
TOOL = {
    "name": "revisor_gate",
    "description": ("Gate determinístico (Classe D) do Revisor SOT para UMA Spec: estrutura, baselines, IDs canônicos, valores e ordem, "
                    "referências, sincronização, backlog ATIVADO, RPSA e mapa, mais sinais H (candidatos que o Revisor confirma). "
                    "Somente leitura. Não cobre julgamento de sentido (Classe P). Argumento spec = 'SPEC-NNN'."),
    "inputSchema": {
        "type": "object",
        "properties": {"spec": {"type": "string", "pattern": "^SPEC-[0-9]{3}$"},
                       "rapido": {"type": "boolean", "description": "pula os detectores do repositório inteiro"}},
        "required": ["spec"], "additionalProperties": False,
    },
}


def _erro(texto):
    return {"isError": True, "content": [{"type": "text", "text": texto}]}


def _arvore():
    try:
        p = subprocess.run(["git", "status", "--porcelain"], cwd=REPO, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=60)
        return p.stdout if p.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def formatar(ev):
    linhas = [f"GATE FUNDIDO (Classe D) — {ev['documento']}"]
    for g in ev["gates"]:
        marca = "OK" if g["exit_code"] == 0 else ("RED" if g["bloqueante"] else "AVISO")
        detalhe = g.get("detalhes") or g.get("tail") or []
        linhas.append(f"  {marca} [{g['classe']}{'*' if g['bloqueante'] else ''}] {g['nome']} (exit {g['exit_code']})")
        for d in detalhe[:6]:
            linhas.append(f"      {d}")
    linhas.append(f"SINAIS H (candidatos — o Revisor confirma): {len(ev['sinais_H'])}")
    for s in ev["sinais_H"][:15]:
        linhas.append(f"  {s['ref']} [{s['codigo']}] {s['trecho']}")
    linhas.append(f"VEREDITO D: {ev['veredito_D']}")
    linhas.append("(*) = bloqueante. Classe P (sentido, adversarial, epistêmico) é do Revisor; este relatório não é parecer.")
    return "\n".join(linhas)


def chamar(args):
    if not isinstance(args, dict) or set(args) - {"spec", "rapido"}:
        return _erro("RECUSADO: argumentos devem ser apenas 'spec' (e opcionalmente 'rapido')")
    spec = args.get("spec")
    if not isinstance(spec, str) or not SPEC.match(spec):
        return _erro("RECUSADO: 'spec' fora do padrão SPEC-NNN")
    rapido = args.get("rapido", False)
    if not isinstance(rapido, bool):
        return _erro("RECUSADO: 'rapido' deve ser booleano")
    # Integridade do próprio gate (DHR-AUDITOR-EXTERNO-015): script alterado sem regravar o manifesto = recusa (falha fechada).
    div = gate_manifest.conferir(REPO)
    if div:
        return _erro("RECUSADO: GATE ADULTERADO OU DESATUALIZADO (governance/GATE-MANIFEST.sha256): " + "; ".join(div[:4]))
    base = (REPO / "specs" / "features").resolve()
    plan = (base / spec / "plan.md").resolve()
    if base not in plan.parents or not plan.is_file():
        return _erro(f"RECUSADO: specs/features/{spec}/plan.md não existe dentro de specs/features/")
    antes = _arvore()
    try:
        ev, _reprovado = revisor_gate.rodar(plan, rapido=rapido, root=REPO)
    except Exception as e:                                      # falha fechada: nada de resultado parcial como se fosse ok
        return _erro(f"ERRO do gate ({type(e).__name__}): {e}")
    depois = _arvore()
    if antes is not None and depois is not None and antes != depois:
        return _erro("ERRO: a árvore de trabalho mudou durante o gate (esperado: somente leitura). Resultado descartado.")
    return {"content": [{"type": "text", "text": formatar(ev)}]}


def responder(msg):
    mid, metodo = msg.get("id"), msg.get("method")
    if metodo == "initialize":
        pv = (msg.get("params") or {}).get("protocolVersion", "2024-11-05")
        return {"jsonrpc": "2.0", "id": mid, "result": {"protocolVersion": pv, "capabilities": {"tools": {}}, "serverInfo": SERVER}}
    if metodo == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    if metodo == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": [TOOL]}}
    if metodo == "tools/call":
        p = msg.get("params") or {}
        if p.get("name") != TOOL["name"]:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": "ferramenta desconhecida"}}
        return {"jsonrpc": "2.0", "id": mid, "result": chamar(p.get("arguments"))}
    if mid is None:
        return None                                              # notificação (ex.: notifications/initialized): sem resposta
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": "método não suportado"}}


def main():
    # Windows: a saída padrão usa a codificação antiga do sistema (cp1252) e o relatório tem "≠", "→", "—": sem isto o servidor
    # quebrava ("Connection closed") no caminho feliz. Força UTF-8 e, por segurança extra, emite JSON só em ASCII (\uXXXX).
    for fluxo in (sys.stdin, sys.stdout):
        try:
            fluxo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    for linha in sys.stdin:
        linha = linha.strip()
        if not linha:
            continue
        try:
            msg = json.loads(linha)
        except ValueError:
            continue
        if not isinstance(msg, dict):
            continue
        resp = responder(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=True) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
