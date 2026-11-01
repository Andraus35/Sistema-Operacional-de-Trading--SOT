#!/usr/bin/env python3
"""log_ac.py — PROTOTIPO F1 (proposta; nao instalado) do log dos agentes Construtores (AC).
Valida evento contra o esquema (sem dependencias), recusa conteudo/segredo (metadados apenas, master §10/§34),
encadeia por hash (master §35) com anexo atomico + trava (R1/A03) e leitura so da cauda (R1/A02).
LIMITES DECLARADOS: o varredor de segredos e DETECTOR com falsos negativos conhecidos (ENF-03); a cadeia de hash prova
INTEGRIDADE, nao AUTORIA (quem escreve no arquivo pode recalcular a cadeia — a ancora e o git); truncamento do fim so e
detectado se o hash-cabeca esperado for fornecido a verifica(). Nunca decide nada; nao toca hooks nem scripts selados."""
import hashlib, json, os, re, sys, time
from pathlib import Path

try:
    import fcntl
except ImportError:  # Windows: sem trava de arquivo (limite declarado; usar segmento por sessao)
    fcntl = None

def _carrega_schema():
    aqui = Path(__file__).resolve().parent
    for c in (aqui / "evento-ac.schema.json", aqui.parent / "schemas" / "evento-ac.schema.json"):
        if c.exists(): return json.loads(c.read_text(encoding="utf-8"))
    raise FileNotFoundError("evento-ac.schema.json nao encontrado (mesma pasta ou ../schemas)")


SCHEMA = _carrega_schema()
PROIBIDAS = {"prompt", "response", "resposta", "content", "conteudo", "text", "texto", "message", "mensagem", "parecer",
             "transcript_path", "cwd", "scratchpad_dir", "system_prompt", "input", "args", "body", "output", "arguments"}
SEGREDOS = [r"sk-[A-Za-z0-9_-]{16,}", r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}", r"AKIA[0-9A-Z]{12,}",
            r"AIza[0-9A-Za-z_-]{20,}", r"xox[abprs]-[A-Za-z0-9-]{10,}", r"eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{4,}",
            r"(?i)bearer\s+[A-Za-z0-9._~+/=-]{16,}", r"(?i)authorization\s*[:=]\s*(basic|bearer)\s+\S{8,}",
            r"(?i)https?://[^/\s:@]+:[^/\s@]+@", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
            r"(?i)\b(password|passwd|pwd|senha|secret|api[_-]?key|token)\s*[=:]\s*\S{4,}"]
CAMADAS_PUBLICAS = ("L2", "L3")  # versionadas no git: sessao so em hash curto
CAUDA = 65536
LOCK_PRAZO = 1.0  # segundos de espera pela trava (B01): estourou => TimeoutError => WARN, nunca bloqueia o hook
CAMADAS = ("L1", "L2", "L3")
_RE_ATA = r"governance/DHR-[A-Za-z0-9_.-]+\.md"
_RE_SESSAO_HASH = re.compile(r"h:[0-9a-f]{12}")


def raiz_repo():
    """Raiz do repositorio (LOG_AC_RAIZ ou primeiro pai com .git); ancora caminhos relativos (B13)."""
    e = os.environ.get("LOG_AC_RAIZ")
    if e: return Path(e)
    for q in Path(__file__).resolve().parents:
        if (q / ".git").exists(): return q
    return Path.cwd()


def camada_do_caminho(arquivo, camada=None):
    """Camada FORCADA pelo destino (B04): governance/logs/L2/... => L2; governance/logs/L3/... => L3; qualquer outro lugar
    dentro de governance/logs => erro; fora dele => L1 (local). Valor desconhecido ou conflito => ValueError."""
    if camada is not None and camada not in CAMADAS: raise ValueError(f"camada desconhecida: {camada!r}")
    partes = Path(os.path.abspath(str(arquivo))).parts
    der = "L1"
    for i in range(len(partes) - 1):
        if partes[i] == "governance" and partes[i + 1] == "logs":
            sub = partes[i + 2] if len(partes) > i + 3 else None
            if sub not in ("L2", "L3"): raise ValueError("dentro de governance/logs so L2/ ou L3/ (camada versionada)")
            der = sub; break
    if camada is not None and camada != der: raise ValueError(f"camada {camada} conflita com o destino ({der})")
    return der


def hash_sessao(sid):
    """Hash curto do session_id para L2/L3 (OWASP: nao versionar o identificador de sessao em claro)."""
    return "h:" + hashlib.sha256(str(sid).encode("utf-8")).hexdigest()[:12]


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
        if len(v) > p.get("maxItems", 10**9): erros.append(f"{nome}: itens demais")
        for i, x in enumerate(v): _valida_prop(f"{nome}[{i}]", x, p["items"], defs, erros)
    if isinstance(v, str):
        if len(v) < p.get("minLength", 0): erros.append(f"{nome}: vazio")
        if len(v) > p.get("maxLength", 10**9): erros.append(f"{nome}: longo demais")
        if "pattern" in p and not re.fullmatch(p["pattern"], v): erros.append(f"{nome}: formato invalido")
    if isinstance(v, dict):
        if isinstance(p.get("additionalProperties"), dict):
            for k, x in v.items(): _valida_prop(f"{nome}.{k}", x, p["additionalProperties"], defs, erros)
        for r in p.get("required", []):
            if r not in v: erros.append(f"{nome}.{r}: ausente")
        if p.get("additionalProperties") is False:
            for k in v:
                if k not in p.get("properties", {}): erros.append(f"{nome}.{k}: campo nao permitido")
        for k, sp in p.get("properties", {}).items():
            if k in v: _valida_prop(f"{nome}.{k}", v[k], sp, defs, erros)


def _segredo(txt):
    return any(re.search(pad, txt) for pad in SEGREDOS)


def _varre(obj, caminho, erros):
    if isinstance(obj, dict):
        for k, v in obj.items():
            ks = str(k)
            if ks.lower() in PROIBIDAS: erros.append(f"{caminho}.{ks}: campo de conteudo proibido (so metadados)")
            if not ks.isascii(): erros.append(f"{caminho}.{ks}: chave nao ASCII (subconjunto JCS)")
            if _segredo(ks): erros.append(f"{caminho}.{ks}: padrao de segredo na chave")
            _varre(v, f"{caminho}.{ks}", erros)
    elif isinstance(obj, list):
        for i, v in enumerate(obj): _varre(v, f"{caminho}[{i}]", erros)
    elif isinstance(obj, str):
        if _segredo(obj): erros.append(f"{caminho}: padrao de segredo detectado")


def valida(ev, camada="L1"):
    """Lista de erros (vazia = ok). `camada` L2/L3 exige session_id em hash curto."""
    erros = []
    if not isinstance(ev, dict): return ["evento nao e objeto"]
    for r in SCHEMA["required"]:
        if r not in ev: erros.append(f"{r}: ausente")
    for k, v in ev.items():
        if k not in SCHEMA["properties"]: erros.append(f"{k}: campo nao permitido")
        else: _valida_prop(k, v, SCHEMA["properties"][k], SCHEMA["definitions"], erros)
    if ev.get("event") == "policy.decision" and (ev.get("decision") is None or not ev.get("policy_id")):
        erros.append("policy.decision exige decision e policy_id")
    if ev.get("event") == "approval.decided" and camada in CAMADAS_PUBLICAS:
        ref = ev.get("input_ref")
        if ev.get("status") == "sem-ata" and not ev.get("task_ref"):
            erros.append("approval.decided 'sem-ata' exige task_ref (onde a decisao foi tomada)")
        if ev.get("status") != "sem-ata" and not (isinstance(ref, dict) and re.fullmatch(_RE_ATA, str(ref.get("path", "")))):
            erros.append("approval.decided em L2/L3 exige input_ref para governance/DHR-*.md ou status 'sem-ata' (a cadeia nao prova autoria; o verify nao confere existencia da ata)")
    if camada in CAMADAS_PUBLICAS and not _RE_SESSAO_HASH.fullmatch(str(ev.get("session_id", ""))):
        erros.append("session_id em claro numa camada versionada (use hash_sessao)")
    _varre(ev, "$", erros)
    return erros


def saneia(ev):
    """Evento minimo: campos de texto livre que dispararam o varredor viram None (ou "[redigido]" se o esquema nao aceita null)
    e entram em `redacted`. Preserva a evidencia do DENY em vez de descarta-la por falso positivo (R1/A04, R2/B08)."""
    e = dict(ev); red = list(e.get("redacted") or [])
    for campo, v in list(e.items()):
        if campo in ("redacted", "hash", "prev_hash") or not isinstance(v, str) or not _segredo(v): continue
        aceita_nulo = "null" in (SCHEMA["properties"].get(campo, {}).get("type") or [])
        e[campo] = None if aceita_nulo else "[redigido]"; red.append(campo)
    if red: e["redacted"] = red[:20]
    return e


def completa_ids(ev, payload):
    """Ids obrigatorios a partir do payload do hook, com fallback deterministico quando ausentes (B05)."""
    e = dict(ev); pl = payload or {}
    e.setdefault("session_id", str(pl.get("session_id") or "sem-sessao")[:128])
    base = json.dumps([pl.get("tool_name"), (pl.get("tool_input") or {}).get("subagent_type"), (pl.get("tool_input") or {}).get("model"), e.get("ts")], sort_keys=True)
    e.setdefault("run_id", str(pl.get("tool_use_id") or "x:" + hashlib.sha256(base.encode()).hexdigest()[:16])[:128])
    e.setdefault("parent_run_id", pl.get("prompt_id") or None)
    e.setdefault("agent_id", str((pl.get("tool_input") or {}).get("subagent_type") or pl.get("agent_type") or "desconhecido")[:128])
    return e


def _canon(ev):
    return json.dumps({k: v for k, v in ev.items() if k != "hash"}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _linha(ev):
    """Serializa a linha JSON sem separadores Unicode de linha crus (U+0085/2028/2029), que quebrariam leitores por splitlines (B06)."""
    return json.dumps(ev, ensure_ascii=False).replace("\u0085", "\\u0085").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def sela(ev, prev_hash):
    ev = dict(ev); ev["prev_hash"] = prev_hash
    ev["hash"] = hashlib.sha256(_canon(ev).encode("utf-8")).hexdigest()
    return ev


def _ultima_linha(fd):
    """Ultima linha nao vazia lendo so a cauda; a janela cresce ate conter a linha inteira (O(tamanho da ultima linha))."""
    tam = os.fstat(fd).st_size
    if tam == 0: return None
    janela = CAUDA
    while True:
        ini = max(0, tam - janela)
        os.lseek(fd, ini, os.SEEK_SET)
        dados = b""
        while len(dados) < tam - ini:
            bloco = os.read(fd, tam - ini - len(dados))
            if not bloco: break
            dados += bloco
        corpo = dados.rstrip(b"\n \t\r")
        if not corpo: return None
        corte = corpo.rfind(b"\n")
        if corte >= 0 or ini == 0:
            return corpo[corte + 1:].decode("utf-8")
        janela *= 2


def _trava(fd):
    if not fcntl: return
    fim = time.monotonic() + LOCK_PRAZO
    while True:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB); return
        except (BlockingIOError, OSError):
            if time.monotonic() >= fim: raise TimeoutError("trava do arquivo de log ocupada")
            time.sleep(0.01)


def acrescenta(arquivo, ev, camada=None, continua_de=None):
    """Valida, sela e anexa UMA linha de forma atomica (O_APPEND + flock com prazo). A camada e FORCADA pelo destino (B04).
    `continua_de`: hash final do segmento anterior, usado como prev_hash quando o arquivo e novo (B02). Recusa evento invalido (ValueError)."""
    camada = camada_do_caminho(arquivo, camada)
    e = valida(ev, camada)
    if e: raise ValueError("; ".join(e))
    p = Path(arquivo); p.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(p), os.O_RDWR | os.O_APPEND | os.O_CREAT, 0o644)
    try:
        _trava(fd)
        ult = _ultima_linha(fd)
        prev = json.loads(ult).get("hash") if ult else continua_de
        dados = (_linha(sela(ev, prev)) + "\n").encode("utf-8"); sel = json.loads(dados)
        if os.fstat(fd).st_size > 0:
            os.lseek(fd, -1, os.SEEK_END)
            if os.read(fd, 1) != b"\n": dados = b"\n" + dados  # arquivo sem \n final: nao cola a proxima linha
        n = 0
        while n < len(dados): n += os.write(fd, dados[n:])  # escrita curta (B08)
        if camada in CAMADAS_PUBLICAS: os.fsync(fd)  # L1 e descartavel: sem fsync (custo/latencia)
        return sel
    finally:
        try:
            if fcntl: fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def emite_seguro(arquivo, ev, camada=None, canal_warn="arquivo", continua_de=None):
    """Para hooks de POLITICA: NUNCA levanta, NUNCA altera a decisao (A01). Devolve (ok, motivo). Falha => WARN em arquivo
    (padrao canal_warn="arquivo"; "stderr" so em hook sem exit 2; A12). Tenta o evento minimo (`saneia`) antes de desistir."""
    try:
        try:
            return True, acrescenta(arquivo, ev, camada, continua_de)["hash"]
        except ValueError:
            return True, acrescenta(arquivo, saneia(ev), camada, continua_de)["hash"]
    except BaseException as exc:  # noqa: BLE001 — isolamento total do log em relacao a decisao
        msg = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} log_ac WARN: evento nao gravado ({type(exc).__name__})\n"
        try:
            if canal_warn == "stderr": sys.stderr.write(msg)  # NAO usar em hook com exit 2: o stderr vai ao modelo
            elif canal_warn == "arquivo":
                d = Path(os.environ.get("LOG_AC_FALHAS") or (raiz_repo() / ".telemetria" / "log-ac-falhas.log")); d.parent.mkdir(parents=True, exist_ok=True)
                with open(d, "a", encoding="utf-8") as f: f.write(msg)
        except BaseException: pass
        return False, type(exc).__name__


def verifica(arquivo, cabeca_esperada=None, continua_de=None, ancora_linha=None):
    """Lista de problemas da cadeia (vazia = integra). `cabeca_esperada`: hash final ancorado no git (detecta truncamento do fim).
    `ancora_linha`=(N, hash): o hash da linha N (1-based, so linhas nao vazias) deve ser o ancorado — vale para segmento que continua crescendo.
    `continua_de`: hash final do segmento anterior (a 1a linha deve encadear nele); sem isso a 1a linha tem prev_hash nulo."""
    probs, prev, ult, n = [], continua_de, None, 0
    try: texto = Path(arquivo).read_bytes().decode("utf-8")
    except UnicodeDecodeError: return ["arquivo nao e UTF-8 valido"]
    for i, l in enumerate(texto.split("\n"), 1):
        if not l.strip(): continue
        n += 1
        try: ev = json.loads(l)
        except ValueError: probs.append(f"linha {i}: JSON invalido"); continue
        if not isinstance(ev, dict): probs.append(f"linha {i}: nao e objeto JSON"); continue
        if ev.get("prev_hash") != prev: probs.append(f"linha {i}: prev_hash nao confere (remocao/reordenacao)")
        if hashlib.sha256(_canon(ev).encode("utf-8")).hexdigest() != ev.get("hash"): probs.append(f"linha {i}: hash nao confere (edicao)")
        prev = ult = ev.get("hash")
        if ancora_linha and n == ancora_linha[0] and ult != ancora_linha[1]: probs.append(f"linha {i}: hash nao confere com a ancora da linha {n}")
    if ancora_linha and n < ancora_linha[0]: probs.append("segmento mais curto que a linha ancorada (truncamento)")
    if cabeca_esperada is not None and ult != cabeca_esperada:
        probs.append("hash-cabeca nao confere com a ancora (truncamento/acrescimo nao ancorado)")
    return probs


def main(argv):
    """CLI: `emit <arquivo> '<json>' [--camada L1|L2|L3] [--continua-de H]` | `verify <arquivo> [--cabeca H] [--continua-de H] [--ancora N:H]`.
    emit: exit 0 SEMPRE (fail-open; WARN em arquivo). verify: 1 se houver problema."""
    def opt(n):
        if n not in argv: return None
        i = argv.index(n)
        return argv[i + 1] if i + 1 < len(argv) else ""
    if len(argv) >= 2 and argv[1] == "emit" and len(argv) < 4:
        emite_seguro(os.devnull, {"x": 1}, canal_warn="arquivo")  # argumentos ausentes: so registra o WARN, exit 0
        return 0
    if len(argv) >= 4 and argv[1] == "emit":
        try: ev = json.loads(argv[3])
        except ValueError: ev = None
        if ev is None or opt("--camada") == "" or opt("--continua-de") == "":
            emite_seguro(argv[2], {"x": 1}, canal_warn="arquivo")  # evento invalido => so registra o WARN
            return 0
        emite_seguro(argv[2], ev, opt("--camada"), canal_warn="arquivo", continua_de=opt("--continua-de"))
        return 0
    if len(argv) >= 3 and argv[1] == "verify":
        anc = opt("--ancora")
        try: anc = (int(anc.split(":")[0]), anc.split(":")[1]) if anc else None
        except (ValueError, IndexError): print("PROBLEMA: --ancora deve ser N:HASH"); return 2
        probs = verifica(argv[2], opt("--cabeca"), opt("--continua-de"), anc)
        for pr in probs: print("PROBLEMA:", pr)
        print("cadeia integra" if not probs else f"{len(probs)} problema(s)")
        return 1 if probs else 0
    print(main.__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
