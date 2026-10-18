#!/usr/bin/env python3
"""
roteador_modelos.py — roteador DETERMINÍSTICO de modelo por tarefa (hook PreToolUse/Agent; DHR-ROTEAMENTO-003 + Emenda 1).

Uso:
  (sem argumentos)                         hook PreToolUse/Agent: lê o evento em stdin e emite permissionDecision deny quando a tabela nega.
  classificar <ficha.json>                 agrupa os achados da rodada por classe (M / S1 / S2 / S3 / O) -> JSON em stdout.
  conferir <ficha.json> [--base REF]       classe M: confere que o que mudou no working tree é SÓ o que a ficha lista; exit 1 = ESCALA.

Tabela classe -> executor/modelo (estática e versionada; sem roteador aprendido):
  M   Orquestrador (sem agente)          achado com arquivo:linha + texto antigo -> novo + condição; sem criar regra/campo/mecanismo
  S1  Revisor SOT  -> sonnet             conferência mecânica (citações, banco de regressão)
  S2  Revisor SOT  -> sonnet             auditoria por delta
  S3  Revisor SOT  -> opus               revisão integral de Spec CRITICAL
  O   Especificador SOT -> opus          desenho (regra/BASpec novos, dossiê, mecanismo)

Regras do hook para Especificador SOT / Revisor SOT:
  R-AC1  `effort` por invocação => NEGA (coluna reservada e desligada até o piloto de esforço).
  R-AC2  `model` por invocação só é aceito se a tarefa declara `CLASSE-TAREFA: <classe>` (linha própria no prompt), a classe é
         compatível com o agente e o `model` é IGUAL ao da tabela da classe. Qualquer outra coisa (sem classe, classe inválida/
         ambígua, agente incompatível, modelo diferente) => NEGA; sem `model` vale o frontmatter. FAIL-CLOSED no override.
  R-AC3  `CLASSE-TAREFA: M` enviada a agente => NEGA (o Orquestrador executa a classe M).
  R-AC4  a classe DECLARADA é conferida contra a classe DERIVADA de fatos objetivos do repositório (derivar_classe); divergência
         ou impossibilidade de derivar => NEGA. Entradas na linha própria do prompt: `ALVO: <plan.md>` (Revisor), `BASE: <ref|arquivo>`
         + `PARECER: <arquivo>` (revisão por delta), `FICHA: <json>` (achados). Especificador (abertura de Spec, Plan, errata) => O;
         com FICHA toda M => M (negado). Revisor: FICHA só de `conferencia` => S1; delta aplicável (revisor.md §3-bis.6) => S2;
         integral => S3 se Complexidade CRITICAL, senão S2.
Demais regras (R-GATE, R-N4, R-ALLOW) inalteradas. Detector/regra de forma, não julga o mérito (ENF-03). Falha na leitura do
evento => libera (não há o que conferir); falha dentro da decisão sobre um agente de construção com model/effort => NEGA.
Telemetria mínima (R8): uma linha JSON por invocação em <tmp>/sot-roteador/uso.jsonl (dado de estado, não normativo).
"""
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

AGENTES_CONSTRUCAO_FIXOS = re.compile(r"(especificador|revisor)\s*sot", re.I)
MODELOS_PERMITIDOS = re.compile(r"^(opus|sonnet|haiku|fable|claude-(opus|sonnet|haiku|fable)-[\w.-]+)$", re.I)
BAIXO_CUSTO = re.compile(r"haiku", re.I)
TAREFA_GATE = re.compile(r"\b(gate|revisor_gate|parecer|revis[aã]o|revisar|auditar|auditoria|conformidade|conforme|valida[cç][aã]o de spec)\b", re.I)
TAREFA_SOBERANA = re.compile(r"\b(homolog\w*|fechar decis[aã]o|abrir decis[aã]o|baseline)\b", re.I)

# --- tabela classe -> (agente, modelo) -------------------------------------------------------------------------------
CLASSES = {
    "M": {"agente": None, "modelo": None},
    "S1": {"agente": "revisor", "modelo": "sonnet"},
    "S2": {"agente": "revisor", "modelo": "sonnet"},
    "S3": {"agente": "revisor", "modelo": "opus"},
    "O": {"agente": "especificador", "modelo": "opus"},
}
IDS_VIGENTES = {"opus": "claude-opus-5-5", "sonnet": "claude-sonnet-5-5"}
MARCADOR = re.compile(r"^[ \t]*CLASSE-TAREFA:[ \t]*(\S+)[ \t]*$", re.M)

# --- critérios objetivos da classe M ---------------------------------------------------------------------------------
MAX_LINHAS_M = 10
MAX_ARQUIVOS_M = 2
NATUREZA_PARA_CLASSE = {"conferencia": "S1", "auditoria": "S2", "integral": "S3"}
ID_NORMATIVO = re.compile(r"\b(?:RULE|INV|ENF|STRUCT|CKG|WF|DHR|EUA)-[A-Z0-9][A-Z0-9-]*\b")
FLAGS_CRIACAO = ("cria_regra", "cria_campo", "cria_mecanismo")


def familia(modelo):
    """'opus'|'sonnet'|... a partir de alias ou ID; None se for ID completo fora de IDS_VIGENTES."""
    m = str(modelo).strip().lower()
    if m in IDS_VIGENTES:
        return m
    for fam, ident in IDS_VIGENTES.items():
        if m == ident:
            return fam
    return None


def extrair_classe(texto):
    """-> classe única declarada em `CLASSE-TAREFA:`; None se ausente, inválida ou ambígua."""
    achadas = {c.upper() for c in MARCADOR.findall(texto or "")}
    if len(achadas) != 1:
        return None
    c = achadas.pop()
    return c if c in CLASSES else None


def _campo(texto, nome):
    ach = re.findall(rf"^[ \t]*{nome}:[ \t]*(\S.*?)[ \t]*$", texto or "", re.M)
    return ach[0] if len(set(ach)) == 1 else None


def _caminho(valor):
    """Caminho do prompt resolvido dentro do repositório; None se fora dele ou inexistente."""
    p = (Path(ROOT) / valor).resolve()
    try:
        p.relative_to(Path(ROOT).resolve())
    except ValueError:
        return None
    return p if p.is_file() else None


def _complexidade(texto):
    m = re.search(r"Complexidade\W{0,20}\**(LOW|MEDIUM|HIGH|CRITICAL)\b", texto)
    return m.group(1) if m else None


def derivar_classe(agente, prompt):
    """Classe derivada de FATOS objetivos (não da declaração). None = não derivável (=> override negado, fail-closed)."""
    ficha = None
    fv = _campo(prompt, "FICHA")
    if fv:
        fp = _caminho(fv)
        if not fp:
            return None
        ficha = json.loads(fp.read_text(encoding="utf-8")).get("achados") or []
        if not ficha:
            return None
        classes = {classificar_achado(a) for a in ficha}
        if classes == {"M"}:
            return "M"
        if agente == "revisor" and classes == {"S1"}:
            return "S1"
    if agente == "especificador":
        return "O"
    alvo = _caminho(_campo(prompt, "ALVO") or "")
    if not alvo:
        return None
    atual = alvo.read_text(encoding="utf-8", errors="replace")
    compl = _complexidade(atual)
    if not compl:
        return None
    base, parecer = _campo(prompt, "BASE"), _campo(prompt, "PARECER")
    if base and parecer and _caminho(parecer):
        import spec_delta
        base_txt = spec_delta.ler_base(str(_caminho(base) or base), alvo)
        d = spec_delta.delta(base_txt, atual)
        total = max(d["total_base"], d["total_atual"], 1)
        mudou = len(d["adicionados"]) + len(d["removidos"]) + len(d["alterados"])
        if mudou * 2 <= total and _complexidade(base_txt) == compl:  # revisor.md §3-bis.6: > metade alterada ou Complexidade mudou => integral
            return "S2"
    return "S3" if compl == "CRITICAL" else "S2"


def _decidir_ac(tipo, entrada):
    modelo, esforco = entrada.get("model"), entrada.get("effort")
    agente = "especificador" if re.search(r"especificador", tipo, re.I) else "revisor"
    classe = extrair_classe(str(entrada.get("prompt") or ""))
    if esforco:
        return "negar", (f"R-AC1: '{tipo}': `effort` por invocação é proibido (coluna reservada e desligada até o piloto de esforço; "
                         "DHR-ROTEAMENTO-003 Emenda 1).")
    prompt = str(entrada.get("prompt") or "")
    derivada = None
    if classe or modelo or _campo(prompt, "FICHA"):
        try:
            derivada = derivar_classe(agente, prompt)
        except Exception:
            derivada = None
    if classe == "M" or derivada == "M":
        return "negar", "R-AC3: classe M é executada pelo Orquestrador (ficha de correção); não é enviada a agente."
    if classe and CLASSES[classe]["agente"] != agente:
        return "negar", f"R-AC2: classe {classe} não é do agente '{tipo}' (tabela: {CLASSES[classe]['agente']})."
    if not modelo:
        return "permitir", "R-AC: modelo do frontmatter"
    if classe is None:
        return "negar", (f"R-AC2: `model={modelo}` exige `CLASSE-TAREFA: <classe>` válida e única no prompt "
                         "(fail-closed: sem classe vale o frontmatter).")
    if derivada is None:
        return "negar", ("R-AC4: classe não derivável de fatos do repositório (ALVO/BASE/PARECER/FICHA ausentes ou ilegíveis); "
                         "override negado, vale o frontmatter.")
    if derivada != classe:
        return "negar", f"R-AC4: classe declarada {classe} diverge da derivada {derivada} (fatos do repositório); declare {derivada}."
    esperado = CLASSES[classe]["modelo"]
    if familia(modelo) != esperado:
        return "negar", f"R-AC2: classe {classe} usa '{esperado}' (tabela); recebido `model={modelo}`."
    return "permitir", f"R-AC2: classe {classe} -> {esperado} (igual à tabela)"


def decidir(entrada):
    """-> (decisao, motivo) com decisao em {'permitir','negar'}."""
    tipo = str(entrada.get("subagent_type") or "")
    modelo = entrada.get("model")
    texto = " ".join(str(entrada.get(k) or "") for k in ("description", "prompt"))
    if AGENTES_CONSTRUCAO_FIXOS.search(tipo):
        try:
            return _decidir_ac(tipo, entrada)
        except Exception:  # fail-closed no override
            if modelo or entrada.get("effort"):
                return "negar", "R-AC2: classificação falhou; override negado (vale o frontmatter)."
            return "permitir", "R-AC: sem parâmetro de modelo"
    if not modelo:
        return "permitir", "herda o modelo da sessão"
    if not MODELOS_PERMITIDOS.match(str(modelo)):
        return "negar", f"R-ALLOW: modelo '{modelo}' fora da tabela permitida (opus|sonnet|haiku|fable|claude-*)."
    if BAIXO_CUSTO.search(str(modelo)) and TAREFA_GATE.search(texto):
        return "negar", "R-GATE: tarefa de gate/revisão/parecer não pode rodar em Haiku (ENF-03; MRM R4). Use código (revisor_gate) ou o Revisor titular."
    if BAIXO_CUSTO.search(str(modelo)) and TAREFA_SOBERANA.search(texto):
        return "negar", "R-N4: tarefa soberana (homologação/decisão/baseline) não é delegável a modelo de baixo custo."
    return "permitir", "dentro da tabela"


# --- classificação de achados (rotina do Orquestrador) ---------------------------------------------------------------
def _linhas(a):
    return max(1, len(str(a.get("antigo") or "").splitlines()))


def _cria_algo(a):
    if any(a.get(f) for f in FLAGS_CRIACAO):
        return True
    novos = set(ID_NORMATIVO.findall(str(a.get("novo") or ""))) - set(ID_NORMATIVO.findall(str(a.get("antigo") or "")))
    return bool(novos)


def _mecanico(a):
    """Critérios objetivos da classe M para UM achado (sem juízo)."""
    return (
        isinstance(a.get("arquivo"), str) and a["arquivo"].strip() != ""
        and isinstance(a.get("linha"), int) and not isinstance(a.get("linha"), bool) and a["linha"] > 0
        and isinstance(a.get("antigo"), str) and a["antigo"] != ""
        and isinstance(a.get("novo"), str) and a["novo"] != a.get("antigo")
        and isinstance(a.get("condicao"), str) and a["condicao"].strip() != ""
        and not _cria_algo(a)
    )


def classificar_achado(a):
    nat = a.get("natureza")
    if nat in NATUREZA_PARA_CLASSE:
        return NATUREZA_PARA_CLASSE[nat]
    return "M" if _mecanico(a) else "O"


def agrupar(achados):
    """Agrupa por classe. Achado M que estoura o teto do lote (linhas/arquivos) é escalado a O."""
    grupos = {c: [] for c in CLASSES}
    linhas, arquivos = 0, set()
    for a in achados:
        c = classificar_achado(a)
        if c == "M":
            if linhas + _linhas(a) > MAX_LINHAS_M or len(arquivos | {a["arquivo"]}) > MAX_ARQUIVOS_M:
                c = "O"
            else:
                linhas += _linhas(a)
                arquivos.add(a["arquivo"])
        grupos[c].append(a.get("id", a))
    return {c: v for c, v in grupos.items() if v}


# --- conferência do delta da classe M ---------------------------------------------------------------------------------
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def _hunks(arquivo, base, root):
    r = subprocess.run(["git", "diff", "-U0", base, "--", arquivo], cwd=root, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip() or "git diff falhou")
    out = []
    for ln in r.stdout.splitlines():
        m = HUNK.match(ln)
        if m:
            out.append((int(m.group(1)), int(m.group(2) if m.group(2) is not None else 1),
                        int(m.group(3)), int(m.group(4) if m.group(4) is not None else 1)))
    return out


def conferir(ficha, base="HEAD", root=ROOT):
    """-> lista de divergências (vazia = ok). Qualquer divergência => ESCALA (o Orquestrador não improvisa)."""
    root = Path(root)
    achados = [a for a in ficha.get("achados", []) if classificar_achado(a) == "M"]
    problemas = []
    if not achados:
        return ["ficha sem achado de classe M"]
    if len({a["arquivo"] for a in achados}) > MAX_ARQUIVOS_M or sum(_linhas(a) for a in achados) > MAX_LINHAS_M:
        problemas.append("lote M acima do teto (linhas/arquivos): escalar")
    permitido = {}
    for a in achados:
        arq, ini = a["arquivo"], a["linha"]
        permitido.setdefault(arq, set()).update(range(ini, ini + _linhas(a)))
        try:
            texto = (root / arq).read_text(encoding="utf-8").splitlines()
        except OSError as e:
            problemas.append(f"{a.get('id', '?')}: {arq} ilegível ({e})")
            continue
        novo = a["novo"].splitlines()
        trecho = texto[ini - 1:ini - 1 + len(novo)]
        if trecho != novo:
            problemas.append(f"{a.get('id', '?')}: {arq}:{ini} não contém o texto novo prescrito")
    for arq, linhas in permitido.items():
        try:
            hunks = _hunks(arq, base, root)
        except Exception as e:
            problemas.append(f"{arq}: diff indisponível ({e})")
            continue
        tocadas = set()
        for ini, n_old, _, n_new in hunks:
            if n_old != n_new or n_old == 0:
                problemas.append(f"{arq}:{ini}: inserção/remoção de linhas fora da substituição prescrita")
                continue
            tocadas.update(range(ini, ini + n_old))
        fora = sorted(tocadas - linhas)
        if fora:
            problemas.append(f"{arq}: linhas alteradas fora da ficha: {fora[:10]}")
        parados = sorted(linhas - tocadas)
        if parados:
            problemas.append(f"{arq}: linhas da ficha não alteradas: {parados[:10]}")
    return problemas


# --- entrada/saída ----------------------------------------------------------------------------------------------------
def registrar(entrada, decisao, motivo):
    try:
        d = Path(tempfile.gettempdir()) / "sot-roteador"
        d.mkdir(parents=True, exist_ok=True)
        with open(d / "uso.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"t": int(time.time()), "tipo": entrada.get("subagent_type"), "model": entrada.get("model"),
                                "effort": entrada.get("effort"), "decisao": decisao, "motivo": motivo}, ensure_ascii=False) + "\n")
    except OSError:
        pass


def hook():
    try:
        ev = json.loads(sys.stdin.read() or "{}")
        if ev.get("tool_name") not in (None, "Agent", "Task"):
            return 0
        entrada = ev.get("tool_input") or {}
        decisao, motivo = decidir(entrada)
        registrar(entrada, decisao, motivo)
    except Exception:
        return 0
    if decisao == "negar":
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                 "permissionDecisionReason": "ROTEADOR DE MODELOS (DHR-ROTEAMENTO-003) — " + motivo}}, ensure_ascii=False))
    return 0


def main(argv):
    if len(argv) < 2:
        return hook()
    cmd = argv[1]
    if cmd not in ("classificar", "conferir") or len(argv) < 3:
        print(__doc__)
        return 2
    ficha = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
    if cmd == "classificar":
        print(json.dumps(agrupar(ficha.get("achados", [])), ensure_ascii=False, indent=1))
        return 0
    base = argv[argv.index("--base") + 1] if "--base" in argv else "HEAD"
    problemas = conferir(ficha, base)
    for p in problemas:
        print("ESCALA:", p)
    if not problemas:
        print("OK: o delta mostra só as linhas listadas na ficha (classe M).")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
