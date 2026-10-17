#!/usr/bin/env python3
"""
revisor_posguarda.py — guarda do Revisor do lado do ORQUESTRADOR (hook Stop; DHR-AUDITOR-EXTERNO-018).

Por que existe: o hook SubagentStop da DHR-AUDITOR-EXTERNO-017 DISPARA em nuvem para "Revisor SOT" (sondas de 2026-10-17), mas o
harness não honra o exit 2 quando o subagente entrega por SubagentHandback — o Revisor encerra sem retorno forçado. Aqui o mesmo
critério (G1/G2/G3 de revisor_guard.avaliar) é aplicado quando a ENTREGA chega ao Orquestrador: no Stop, para cada hand-back de um
Revisor ainda não conferido, o código confere o parecer; havendo violação, bloqueia o fim do turno UMA vez por agente e entrega a lista
ao Orquestrador, que devolve ao Revisor (SendMessage) ou roda o gate e anota. Detector ≠ Gate (ENF-03): confere FORMA e EXISTÊNCIA.
Falha do script => libera (fail-open). stop_hook_active => libera (sem laço).
"""
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import revisor_guard as g  # noqa: E402

_ID = re.compile(r'from=\\*"([0-9a-z]{10,})')


def ids_entregues(linhas):
    vistos = []
    for ln in linhas:
        if "Subagent hand-back" in ln:
            for i in _ID.findall(ln):
                if i not in vistos:
                    vistos.append(i)
    return vistos


def parecer_final(path):
    """Texto do último SubagentHandback do transcript do subagente ('' se não houver)."""
    final = ""
    try:
        for ln in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                o = json.loads(ln)
            except ValueError:
                continue
            cont = (o.get("message") or {}).get("content")
            if o.get("type") == "assistant" and isinstance(cont, list):
                for b in cont:
                    if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "SubagentHandback":
                        final = " ".join(g._strs(b.get("input")))
    except OSError:
        pass
    return final


def avaliar_sessao(transcript, estado_dir):
    """-> lista de (agent_id, [mensagens]) ainda não conferidas e com violação."""
    tp = Path(transcript)
    linhas = tp.read_text(encoding="utf-8", errors="replace").splitlines()
    sub = tp.with_suffix("") / "subagents"
    est = Path(estado_dir) / (tp.stem + ".json")
    feitos = set(json.loads(est.read_text())) if est.exists() else set()
    achados = []
    for i in ids_entregues(linhas):
        if i in feitos:
            continue
        meta = sub / f"agent-{i}.meta.json"
        try:
            tipo = json.loads(meta.read_text(encoding="utf-8")).get("agentType", "")
        except (OSError, ValueError):
            continue
        if not re.search(r"revisor", tipo, re.I):
            continue
        feitos.add(i)
        ev = {"agent_type": tipo, "agent_transcript_path": str(sub / f"agent-{i}.jsonl"), "last_assistant_message": parecer_final(sub / f"agent-{i}.jsonl"), "stop_hook_active": False}
        msgs = g.avaliar(ev)
        if msgs:
            achados.append((i, msgs))
    Path(estado_dir).mkdir(parents=True, exist_ok=True)
    est.write_text(json.dumps(sorted(feitos)))
    return achados


def main():
    try:
        ev = json.loads(sys.stdin.read() or "{}")
        if ev.get("stop_hook_active") or not ev.get("transcript_path"):
            return 0
        achados = avaliar_sessao(ev["transcript_path"], Path(tempfile.gettempdir()) / "sot-revisor-posguarda")
    except Exception:
        return 0
    if achados:
        txt = ["GUARDA PÓS-REVISOR (DHR-AUDITOR-EXTERNO-018) — o parecer chegou sem passar pela guarda do Revisor (o hook do subagente não é honrado em nuvem). "
               "Devolva ao Revisor (SendMessage) com a lista abaixo ou rode `python scripts/revisor_gate.py <plan.md>` e anote o resultado antes de levar a Andraus:"]
        for i, msgs in achados:
            txt.append(f"[agente {i}]\n" + "\n".join(msgs))
        print(json.dumps({"decision": "block", "reason": "\n".join(txt)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
