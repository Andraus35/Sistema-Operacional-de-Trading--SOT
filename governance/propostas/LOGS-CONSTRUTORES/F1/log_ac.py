#!/usr/bin/env python3
"""log_ac.py — PROTOTIPO F1 (proposta; nao instalado) do log dos agentes Construtores (AC).
Valida evento contra o esquema (sem dependencias), recusa conteudo/segredo (metadados apenas, master §10/§34)
e encadeia por hash (master §35). Detector: nunca decide nada; nao toca hooks nem scripts selados."""
import hashlib, json, re
from pathlib import Path

SCHEMA = json.loads((Path(__file__).with_name("evento-ac.schema.json")).read_text(encoding="utf-8"))
PROIBIDAS = {"prompt", "response", "resposta", "content", "conteudo", "text", "texto", "message", "mensagem", "parecer",
            "transcript_path", "cwd", "scratchpad_dir"}
SEGREDOS = [r"sk-[A-Za-z0-9_-]{16,}", r"gh[pousr]_[A-Za-z0-9]{20,}", r"AKIA[0-9A-Z]{12,}", r"Bearer\s+[A-Za-z0-9._-]{16,}",
            r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"(?i)(password|senha|secret|token)\s*[=:]\s*\S{6,}"]


def _tipo_ok(v, t):
    ts = t if isinstance(t, list) else [t]
    mapa = {"string": str, "number": (int, float), "integer": int, "object": dict, "array": list}
    for x in ts:
        if x == "null" and v is None: return True
        if x in mapa and isinstance(v, mapa[x]) and not (x in ("number", "integer") and isinstance(v, bool)): return True
    return False


def _valida_prop(nome, v, p, defs, erros):
    if "$ref" in p: p = defs[p["$ref"].split("/")[-1]]
    if "const" in p and v != p["const"]: erros.append(f"{nome}: deve ser {p['const']!r}")
    if "enum" in p and v not in p["enum"]: erros.append(f"{nome}: fora do enum ({v!r})")
    if "type" in p and not _tipo_ok(v, p["type"]): erros.append(f"{nome}: tipo invalido"); return
    if isinstance(v, list) and isinstance(p.get("items"), dict):
        for i, x in enumerate(v): _valida_prop(f"{nome}[{i}]", x, p["items"], defs, erros)
    if isinstance(v, str):
        if len(v) < p.get("minLength", 0): erros.append(f"{nome}: vazio")
        if len(v) > p.get("maxLength", 10**9): erros.append(f"{nome}: longo demais")
        if "pattern" in p and not re.search(p["pattern"], v): erros.append(f"{nome}: formato invalido")
    if isinstance(v, dict) and isinstance(p.get("additionalProperties"), dict):
        for k, x in v.items(): _valida_prop(f"{nome}.{k}", x, p["additionalProperties"], defs, erros)
    if isinstance(v, dict) and "required" in p:
        for r in p["required"]:
            if r not in v: erros.append(f"{nome}.{r}: ausente")
        if p.get("additionalProperties") is False:
            for k in v:
                if k not in p.get("properties", {}): erros.append(f"{nome}.{k}: campo nao permitido")
        for k, sp in p.get("properties", {}).items():
            if k in v: _valida_prop(f"{nome}.{k}", v[k], sp, defs, erros)


def _varre(obj, caminho, erros):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if str(k).lower() in PROIBIDAS: erros.append(f"{caminho}.{k}: campo de conteudo proibido (so metadados)")
            _varre(v, f"{caminho}.{k}", erros)
    elif isinstance(obj, list):
        for i, v in enumerate(obj): _varre(v, f"{caminho}[{i}]", erros)
    elif isinstance(obj, str):
        for pad in SEGREDOS:
            if re.search(pad, obj): erros.append(f"{caminho}: padrao de segredo detectado")


def valida(ev):
    """Lista de erros (vazia = ok)."""
    erros = []
    if not isinstance(ev, dict): return ["evento nao e objeto"]
    for r in SCHEMA["required"]:
        if r not in ev: erros.append(f"{r}: ausente")
    for k, v in ev.items():
        if k not in SCHEMA["properties"]: erros.append(f"{k}: campo nao permitido")
        else: _valida_prop(k, v, SCHEMA["properties"][k], SCHEMA["definitions"], erros)
    if ev.get("event") == "policy.decision" and (ev.get("decision") is None or not ev.get("policy_id")):
        erros.append("policy.decision exige decision e policy_id")
    _varre(ev, "$", erros)
    return erros


def _canon(ev):
    return json.dumps({k: v for k, v in ev.items() if k != "hash"}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def sela(ev, prev_hash):
    ev = dict(ev); ev["prev_hash"] = prev_hash
    ev["hash"] = hashlib.sha256(_canon(ev).encode("utf-8")).hexdigest()
    return ev


def acrescenta(arquivo, ev):
    """Valida, sela e anexa uma linha. Recusa evento invalido (ValueError)."""
    e = valida(ev)
    if e: raise ValueError("; ".join(e))
    p = Path(arquivo); prev = None
    if p.exists():
        linhas = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
        if linhas: prev = json.loads(linhas[-1]).get("hash")
    sel = sela(ev, prev)
    with open(p, "a", encoding="utf-8") as f: f.write(json.dumps(sel, ensure_ascii=False) + "\n")
    return sel


def verifica(arquivo):
    """Lista de problemas da cadeia (vazia = integra)."""
    probs, prev = [], None
    for i, l in enumerate(Path(arquivo).read_text(encoding="utf-8").splitlines(), 1):
        if not l.strip(): continue
        try: ev = json.loads(l)
        except ValueError: probs.append(f"linha {i}: JSON invalido"); continue
        if ev.get("prev_hash") != prev: probs.append(f"linha {i}: prev_hash nao confere (remocao/reordenacao)")
        if hashlib.sha256(_canon(ev).encode("utf-8")).hexdigest() != ev.get("hash"): probs.append(f"linha {i}: hash nao confere (edicao)")
        prev = ev.get("hash")
    return probs
