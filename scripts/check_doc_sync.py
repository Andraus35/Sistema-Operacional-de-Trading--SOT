#!/usr/bin/env python3
"""
check_doc_sync.py — detector de drift de sincronização documental (CONS-01 e correlatos).

Somente leitura. Nasce da auditoria profunda de 2026-09-28 (achados de incoerência
recorrentes: decisão fechada ainda listada como aberta em CATALOGO-OFICIAL.md/CIC-001;
RULE citada como normativa antes de ser registrada em RULES.md; Estado de backlog fora
do próprio enum do RMR-001; documento de intake de backlog dessincronizado do painel
vivo). Mesmo molde de scripts/check_refs.py e scripts/backlog_triggers.py: extrai fatos
de fontes objetivas do próprio repositório (nunca de opinião externa) e cruza.

Checagens (Detector ≠ Gate — ENF-03; nunca promove, nunca fecha decisão — CONS-01):
    D1  Decisão ABERTA (ROADMAP "Decisões abertas ativas") citada como FECHADA/resolvida
        em algum documento vivo, sem ter sido fechada por homologação → ERRO.
    D2  Decisão FECHADA (ROADMAP "Decisões FECHADAS") ainda listada como aberta/
        remanescente em documento vivo → ERRO se o documento se autodeclara SSoT/
        inventário de conformidade; WARN nos demais.
    D3  Família RULE-XX citada como já normativa/vigente (Spec homologada, "→ RULES.md",
        "vigência imediata") sem seção própria em governance/RULES.md → ERRO
        (RULE-HG-02: RULE sem registro permanece [PROPOSTA], não vinculante).
    D4  Estado de item do RMR-001 fora do enum que o próprio RMR-001 §2 declara → WARN.
    D5  Documento de intake `backlog/BL-0NN-*.md` com campo Estado divergente do estado
        do mesmo BL-0NN no painel vivo RMR-001 → WARN.

Uso:
    python scripts/check_doc_sync.py               # relatório; exit 1 se houver ERRO
    python scripts/check_doc_sync.py --strict      # WARN também falha
    python scripts/check_doc_sync.py --json        # saída legível por máquina
    python scripts/check_doc_sync.py --root DIR    # raiz alternativa (testes)

Este script NÃO é gate de conformidade (exit 0 ≠ CONFORME ≠ homologação) e não fecha
decisão aberta nem promove item de backlog (CONS-01): apenas aponta candidatos a drift
para revisão humana (Revisor audita achado; Andraus decide encaminhamento — atomic-spec §15).
"""

import argparse
import json
import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Mesmo escopo de exclusão do check_refs.py/map-sync.js — congelados (INV-07) e não-normativos.
EXCLUDE = re.compile(r"(^|/)(node_modules|\.git|UPGRADES|_legacy)(/|$)|harness-eval/runs/|^docs/mapa/")
FROZEN = re.compile(r"(^|/)governance/(DHR-|EUA-|HOD-|MAN-|PP-|PE-)|^docs/")
ID_TOKEN = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b")

# D1/D2 são deliberadamente ESTRITOS (alta precisão > alta cobertura): um detector barulhento
# treina o time a ignorá-lo (o oposto do que scripts/check_refs.py já demonstra funcionar).
# Só dispara em dois padrões de alta confiança:
#   (a) declaração inline "ID — FECHADA"/"ID RESOLVIDA" adjacente (sem tokens entre os dois);
#   (b) tabela/lista sob um CABEÇALHO de registro de decisão ("Open decisions", "Decisões
#       abertas", "Decisões FECHADAS" etc.) — mesmo padrão que o próprio ROADMAP.md usa.
# Não varre prosa livre: evita o falso-positivo de "decisao:J-001 resolvida" (sintaxe de
# gatilho do RMR-001/backlog_triggers.py) ou de "dimensionalidade fechada" na mesma linha
# de um ID não relacionado.
INLINE_CLOSED = re.compile(r"[\s*]{0,3}(?:—|-|:)\s*(?:FECHADA|RESOLVID[AO])\b")
GATILHO_PREFIX = re.compile(r"decisao:\s*$", re.I)
HEADING_OPEN = re.compile(r"open\s+decisions|decis[õo]es?\s+abertas|abertas\s+remanescentes", re.I)
# Basta a palavra "FECHADA(S)"/"closed" aparecer no cabeçalho para ele ser um registro de
# FECHADAS, mesmo que também contenha "Open decisions" (ex.: título legado da tabela em
# CIC-001 §5.3 "Open decisions FECHADAS (registro histórico)") — checada com prioridade.
HEADING_CLOSED = re.compile(r"closed\s+decisions|fechada|resolvid[ao]s?\s+\(registro", re.I)
TABLE_ID_ROW = re.compile(r"^\s*\|\s*\*{0,2}([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\*{0,2}\s*\|")


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def rel(root: Path, p: Path) -> str:
    return p.relative_to(root).as_posix()


def list_docs(root: Path):
    out = []
    for p in root.rglob("*.md"):
        if p.is_file():
            r = rel(root, p)
            if not EXCLUDE.search(r):
                out.append(p)
    return sorted(out)


STRIKETHROUGH = re.compile(r"~~.*?~~")


def extract_id_segments(cell: str):
    """Quebra a célula de uma tabela do ROADMAP (·-separado) e devolve {ID: trecho}.

    Só o PRIMEIRO segmento (antes do 1º '·') é tratado como lista simples separada por
    vírgula (ex.: "J-001 (reduzido), G-001, H-001, K-001") — é o formato estrutural das
    duas linhas do ROADMAP. Os demais segmentos (após '·', tipicamente em negrito, um por
    decisão elaborada) só contribuem com o PRIMEIRO ID que citam — para não capturar IDs
    mencionados de passagem na prosa explicativa de outra decisão (ex.: "...→ SPEC-018/K-001)"
    dentro do segmento que fecha L-001 não faz de K-001 uma decisão fechada).
    """
    out = {}
    # ~~ID~~ é a convenção já usada no repositório para marcar item superado in-line (ex.:
    # CATALOGO-OFICIAL.md §6, "~~SPEC-001 está liberada~~ → SPEC-001 HOMOLOGADO") — um ID
    # riscado não conta como "ainda listado".
    cell = STRIKETHROUGH.sub("", cell)
    segments = re.split(r"·", cell)
    for idx, seg in enumerate(segments):
        seg = seg.strip()
        if not seg:
            continue
        seg_clean = seg.strip("*").strip()
        m = ID_TOKEN.search(seg_clean)
        if m:
            out[m.group(0)] = seg
        if idx == 0:
            for m2 in re.finditer(r"\b[A-Z]-\d{3}\b", seg_clean):
                out.setdefault(m2.group(0), seg)
    return out


# Documentos cujo papel declarado é ser registro/inventário de status de decisão — mesmo
# critério que o AGENTS.md usa para "Fonte de verdade de baseline" (§1: CATALOGO-OFICIAL.md).
# D1(b)/D2 (varredura por cabeçalho) só olha para esses arquivos: fora deles, "decisão X" +
# "aberta"/"fechada" na mesma vizinhança é prosa livre, não um registro — tentar generalizar
# para prosa arbitrária troca precisão por cobertura e produz ruído (ver histórico deste
# script: primeira versão, sem este recorte, gerou dezenas de falsos positivos).
REGISTRY_GLOBS = ("governance/CATALOGO-OFICIAL.md", "governance/CIC-*.md")


def is_registry_doc(rel_path: str) -> bool:
    from fnmatch import fnmatch
    return any(fnmatch(rel_path, g) for g in REGISTRY_GLOBS)


def is_heading_line(line: str) -> bool:
    """Só cabeçalho markdown de verdade (## / ### ...). Uma linha de TABELA ou um trecho em
    **negrito** dentro de prosa NÃO conta — foi a fonte de todos os falsos-positivos da
    primeira versão deste script (ex.: uma linha de tabela sobre outro assunto que cita a
    frase "decisões abertas" de passagem abria uma janela de 60 linhas por engano)."""
    return bool(re.match(r"^#{1,4}\s", line))


BULLET_LABEL = re.compile(r"^-\s*\*\*([^*]+)\*\*\s*:?")


class Facts:
    def __init__(self, root: Path):
        self.root = root
        road = read(root / "ROADMAP.md")
        self.decisions_open = {}
        self.decisions_closed = {}
        for line in road.split("\n"):
            if re.match(r"\|\s*Decisões abertas ativas\s*\|", line):
                cell = line.split("|")[2] if line.count("|") >= 3 else line
                self.decisions_open.update(extract_id_segments(cell))
            if re.match(r"\|\s*Decisões FECHADAS\s*\|", line):
                cell = line.split("|")[2] if line.count("|") >= 3 else line
                self.decisions_closed.update(extract_id_segments(cell))

        # Famílias RULE com seção própria em RULES.md (heading "(RULE-XX)" + ao menos
        # uma linha de definição "RULE-XX-NN:").
        rules_text = read(root / "governance" / "RULES.md")
        self.rule_families_defined = set()
        for m in re.finditer(r"^#{2,3}.*\(RULE-([A-Z]+)\)", rules_text, re.M):
            self.rule_families_defined.add(m.group(1))
        for m in re.finditer(r"\bRULE-([A-Z]+)-\d+\s*:", rules_text):
            self.rule_families_defined.add(m.group(1))

        # RMR-001 §2 — enum canônico de Estado, extraído do próprio texto ("Proposto → Em
        # espera → ATIVADO → Absorvido" · "ou Descartado", etc.) — nunca hardcoded aqui.
        rmr_path = root / "backlog" / "RMR-001_Painel_Backlog.md"
        self.rmr_text = read(rmr_path)
        self.rmr_states = set()
        m = re.search(r"Proposto\s*(?:→|->).{0,120}", self.rmr_text)
        if m:
            self.rmr_states |= set(re.findall(r"\b(Proposto|Em espera|ATIVADO|Absorvido|Descartado)\b", m.group(0)))
        # aceita variações "ou Descartado" fora da seta principal, buscando na mesma seção (§2)
        sec2 = re.search(r"##\s*2[.\s].*?(?=\n##\s*3[.\s]|\Z)", self.rmr_text, re.S)
        if sec2:
            self.rmr_states |= set(re.findall(r"\b(Proposto|Em espera|ATIVADO|Absorvido|Descartado)\b", sec2.group(0)))
        if not self.rmr_states:
            self.rmr_states = {"Proposto", "Em espera", "ATIVADO", "Absorvido", "Descartado"}

        # Estado de cada item no painel vivo (linha de tabela "| **BL-0NN** | ... |")
        self.rmr_rows = []  # (bl_id, estado_raw, line_no)
        for i, line in enumerate(self.rmr_text.split("\n"), 1):
            mm = re.match(r"^\|\s*\*\*(BL-\d{3})\*\*\s*\|", line)
            if not mm:
                continue
            cells = line.split("|")
            if len(cells) < 10:
                continue
            estado_raw = re.sub(r"[*`]", "", cells[-3]).strip()
            self.rmr_rows.append((mm.group(1), estado_raw, i))
        self.rmr_state_by_id = {bl: st for bl, st, _ in self.rmr_rows}

        # Specs homologadas — mesma lógica de backlog_triggers.py (ROADMAP + header do plan.md)
        self.spec_homolog = set()
        for line in road.split("\n"):
            m = re.match(r"^(?:#{2,4}\s*|\|\s*)\**SPEC-(\d{3})\b", line)
            if m and re.search(r"HOMOLOGAD", line):
                self.spec_homolog.add(m.group(1))
        feats = root / "specs" / "features"
        if feats.exists():
            for d in feats.iterdir():
                m = re.match(r"SPEC-(\d{3})$", d.name)
                if not m:
                    continue
                head = "\n".join(read(d / "plan.md").split("\n")[:15])
                if re.search(r"Status:.*HOMOLOGAD", head):
                    self.spec_homolog.add(m.group(1))


def _ids_in_heading_window(lines, start_idx, max_span=60):
    """A partir de uma linha de cabeçalho (índice start_idx, 0-based), coleta IDs em linhas
    de tabela (TABLE_ID_ROW) ou em listas ·/vírgula na mesma linha, até a próxima linha de
    cabeçalho de nível igual/maior ou até max_span linhas depois."""
    ids = {}
    heading_level = len(re.match(r"^(#*)", lines[start_idx]).group(1))
    for j in range(start_idx, min(start_idx + max_span, len(lines))):
        line = lines[j]
        if j > start_idx:
            m = re.match(r"^(#+)\s", line)
            if m and (heading_level == 0 or len(m.group(1)) <= max(heading_level, 1)):
                break
        m2 = TABLE_ID_ROW.match(STRIKETHROUGH.sub("", line))
        if m2:
            ids.setdefault(m2.group(1), j + 1)
        else:
            ids.update({k: j + 1 for k in extract_id_segments(line) if k not in ids})
    return ids


def check_d1_d2(root: Path, docs, facts: Facts, findings):
    """D1: decisão aberta tratada como fechada · D2: decisão fechada tratada como aberta."""
    for p in docs:
        r = rel(root, p)
        if r == "ROADMAP.md" or FROZEN.search(r):
            continue  # ROADMAP = fonte de verdade; atas/propostas congeladas retratam sua própria data (INV-07)
        text = read(p)
        lines = text.split("\n")

        # (a) declaração inline de alta confiança: "ID — FECHADA"/"ID RESOLVIDA" adjacente
        for i, line in enumerate(lines, 1):
            for dec_id in facts.decisions_open:
                idx = line.find(dec_id)
                if idx < 0:
                    continue
                tail = line[idx + len(dec_id):idx + len(dec_id) + 20]
                head = line[max(0, idx - 20):idx]
                if INLINE_CLOSED.match(tail) and not GATILHO_PREFIX.search(head):
                    findings.append((
                        "ERRO", r, i,
                        f"decisão ABERTA '{dec_id}' declarada fechada/resolvida inline — CONS-01: {line.strip()[:140]}"
                    ))

        # (b) tabela sob CABEÇALHO markdown de registro de decisão (ex.: CIC-001 "### 5.1
        # Open decisions") — só em documentos que SÃO o registro (REGISTRY_GLOBS); e só
        # quando a linha é um cabeçalho ATX de verdade (não uma linha de tabela ou uma
        # citação bibliográfica que mencione a frase de passagem).
        # (c) bullet de rótulo único "- **Abertas remanescentes:** A, B, C" (formato do
        # CATALOGO-OFICIAL.md §5) — extrai só da MESMA linha, nunca de uma janela.
        if not is_registry_doc(r):
            continue
        for i, line in enumerate(lines):
            if is_heading_line(line):
                # HEADING_CLOSED tem prioridade: um cabeçalho como "Open decisions FECHADAS
                # (registro histórico)" casa as duas regexes (contém "Open decisions" E
                # "FECHADAS") — é um registro de FECHADAS, não de abertas.
                if HEADING_CLOSED.search(line):
                    for dec_id, ln in _ids_in_heading_window(lines, i).items():
                        if dec_id in facts.decisions_open:
                            findings.append((
                                "ERRO", r, ln,
                                f"decisão ABERTA '{dec_id}' listada sob um registro de 'decisões FECHADAS' — CONS-01"
                            ))
                elif HEADING_OPEN.search(line):
                    for dec_id, ln in _ids_in_heading_window(lines, i).items():
                        if dec_id in facts.decisions_closed:
                            findings.append((
                                "ERRO", r, ln,
                                f"decisão FECHADA '{dec_id}' ainda listada sob um registro de 'decisões abertas'"
                            ))
                continue
            m = BULLET_LABEL.match(line)
            if not m:
                continue
            label = m.group(1)
            rest = line[m.end():]
            if HEADING_OPEN.search(label):
                for dec_id in extract_id_segments(rest):
                    if dec_id in facts.decisions_closed:
                        findings.append((
                            "ERRO", r, i + 1,
                            f"decisão FECHADA '{dec_id}' ainda listada em '{label.strip()}'"
                        ))
            if HEADING_CLOSED.search(label):
                for dec_id in extract_id_segments(rest):
                    if dec_id in facts.decisions_open:
                        findings.append((
                            "ERRO", r, i + 1,
                            f"decisão ABERTA '{dec_id}' listada em '{label.strip()}' — CONS-01"
                        ))


FONTE_BLOCK = re.compile(r"\[Fonte:\s*([^\]]*)\]", re.I)
RULE_TOKEN = re.compile(r"\bRULE-([A-Z]+)-\d+\b")


def check_d3(root: Path, facts: Facts, findings):
    """D3: o próprio RULES.md funda uma regra JÁ NORMATIVA em uma família RULE-xx que não
    tem seção própria registrada nele mesmo (RULE-HG-02: sem registro, permanece [PROPOSTA]
    — não pode fundamentar outra regra como se já fosse FATO NORMATIVO). Sinal de alta
    confiança: olha só para citações `[Fonte: ...]` dentro do documento que é a própria
    fonte de verdade das RULEs — não para menções em prosa de plan.md/checks.md, onde a
    mesma frase pode legitimamente estar marcada [PROPOSTA] (ver SPEC-020/plan.md:155)."""
    rules_path = root / "governance" / "RULES.md"
    if not rules_path.exists():
        return
    text = read(rules_path)
    for i, line in enumerate(text.split("\n"), 1):
        for m in FONTE_BLOCK.finditer(line):
            for m2 in RULE_TOKEN.finditer(m.group(1)):
                fam = m2.group(1)
                if fam not in facts.rule_families_defined:
                    findings.append((
                        "ERRO", "governance/RULES.md", i,
                        f"[Fonte:] cita RULE-{fam}-xx como fundamento de uma regra já normativa, mas "
                        f"RULE-{fam} não tem seção própria registrada neste arquivo — RULE-HG-02: "
                        f"permanece [PROPOSTA], não pode fundamentar outra regra"
                    ))


def check_d4(root: Path, facts: Facts, findings):
    """D4: Estado de item do RMR-001 fora do enum que o próprio §2 declara."""
    rmr_rel = "backlog/RMR-001_Painel_Backlog.md"
    for bl_id, estado_raw, ln in facts.rmr_rows:
        estado = next((s for s in facts.rmr_states if estado_raw.lower().startswith(s.lower())), None)
        if estado is None:
            findings.append((
                "WARN", rmr_rel, ln,
                f"{bl_id}: Estado '{estado_raw}' fora do enum declarado no próprio RMR-001 §2 "
                f"({', '.join(sorted(facts.rmr_states))})"
            ))


def check_d5(root: Path, facts: Facts, findings):
    """D5: doc de intake backlog/BL-0NN-*.md dessincronizado do painel vivo RMR-001."""
    backlog_dir = root / "backlog"
    if not backlog_dir.exists():
        return
    for p in sorted(backlog_dir.glob("BL-*.md")):
        m = re.match(r"(BL-\d{3})", p.name)
        if not m:
            continue
        bl_id = m.group(1)
        panel_estado = facts.rmr_state_by_id.get(bl_id)
        if panel_estado is None:
            continue
        text = read(p)
        m2 = re.search(r"\*\*Estado\*\*\s*\|?\s*:?\s*[`*]{0,2}([A-Za-zÀ-ÿ ]+)", text)
        if not m2:
            continue
        intake_estado = m2.group(1).strip().rstrip(".")
        norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
        if norm(intake_estado) and not panel_estado.lower().startswith(norm(intake_estado).split(" (")[0]):
            findings.append((
                "WARN", rel(root, p), 0,
                f"{bl_id}: documento de intake declara Estado='{intake_estado}', mas o painel vivo "
                f"RMR-001 já registra '{panel_estado}' — sincronizar o intake"
            ))


def analyze(root: Path):
    docs = list_docs(root)
    facts = Facts(root)
    findings = []
    check_d1_d2(root, docs, facts, findings)
    check_d3(root, facts, findings)
    check_d4(root, facts, findings)
    check_d5(root, facts, findings)
    seen, uniq = set(), []
    for f in findings:
        k = (f[0], f[1], f[2], f[3])
        if k not in seen:
            seen.add(k)
            uniq.append(f)
    return docs, facts, uniq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()
    root = Path(args.root)

    docs, facts, uniq = analyze(root)
    order = {"ERRO": 0, "WARN": 1, "INFO": 2}
    shown = sorted(uniq, key=lambda x: (order[x[0]], x[1], x[2]))
    counts = {"ERRO": 0, "WARN": 0, "INFO": 0}
    for f in uniq:
        counts[f[0]] += 1

    if args.json:
        print(json.dumps({
            "documentos": len(docs),
            "decisoes_abertas": sorted(facts.decisions_open),
            "decisoes_fechadas": sorted(facts.decisions_closed),
            "rule_familias_registradas": sorted(facts.rule_families_defined),
            "achados": [{"severidade": s, "arquivo": f, "linha": ln, "mensagem": msg} for s, f, ln, msg in shown],
            "contagens": counts,
        }, ensure_ascii=False, indent=1))
    else:
        print("=" * 60)
        print("VERIFICADOR DE SINCRONIZAÇÃO DOCUMENTAL — check_doc_sync.py")
        print(f"Documentos: {len(docs)} · decisões abertas: {len(facts.decisions_open)} · "
              f"decisões fechadas: {len(facts.decisions_closed)} · famílias RULE registradas: "
              f"{len(facts.rule_families_defined)}")
        print("=" * 60)
        for sev, f, ln, msg in shown:
            loc = f"{f}:{ln}" if ln else f
            print(f"[{sev}] {loc} — {msg}")
        print("-" * 60)
        print(f"ERRO={counts['ERRO']} WARN={counts['WARN']} INFO={counts['INFO']}")
        print("Somente leitura — Detector (ENF-03): não promove item, não fecha decisão.")
        print("LEMBRETE: gate auxiliar. exit 0 ≠ CONFORME ≠ homologação.")

    fail = counts["ERRO"] > 0 or (args.strict and counts["WARN"] > 0)
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
