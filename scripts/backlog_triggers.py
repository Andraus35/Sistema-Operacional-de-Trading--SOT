#!/usr/bin/env python3
"""
backlog_triggers.py — BL-006: "o sistema informa" (RMR-001 §4), automatizado.

Somente leitura. Lê o Registro Vivo do RMR-001 (§6), avalia os Gatilhos de Ativação
(§3) contra o estado do repositório e imprime quais itens estão ATIVADOS, quais
tiveram o gatilho DISPARADO sem registro (achado de gate) e quais exigem verificação
manual.

Uso:
    python scripts/backlog_triggers.py               # relatório; exit 1 se houver divergência
    python scripts/backlog_triggers.py --strict      # ATIVADO pendente também falha
    python scripts/backlog_triggers.py --json        # saída legível por máquina
    python scripts/backlog_triggers.py --root DIR    # raiz alternativa (testes)
    python scripts/backlog_triggers.py --abertura SPEC-006   # itens vinculados POR REGRA à abertura da Spec (DHR-BACKLOG-ABERTURA-001)
    python scripts/backlog_triggers.py --abertura-pendentes  # Specs em redação cujo plan.md ainda não declara a disposição de cada item vinculado

Avaliação (tri-estado — nunca finge certeza):
    spec:SPEC-nnn homologada | em redação   → verificável (ROADMAP + specs/features/)
    spec:EUA-Enn homologada                 → verificável (governance/DHR-EUA-Enn*.md)
    decisao:X-nnn resolvida                 → verificável (ROADMAP, linha "Decisões FECHADAS")
    evento: / milestone: / hygiene:         → MANUAL (exige julgamento humano; nunca dispara sozinho)
    ∧ = todas as condições · ∨ = alguma alternativa.
    Faixas "SPEC-010..014" valem para qualquer Spec da faixa.

Vinculação por abertura (DHR-BACKLOG-ABERTURA-001): todo item não encerrado cujo gatilho tem uma
alternativa `spec:SPEC-nnn em redação` fica VINCULADO À SPEC-nnn desde a abertura — sem depender de
promoção de Andraus. Vincular ≠ promover a ATIVADO ≠ absorver: o painel não muda de estado; o vínculo
é declarado no Plan (Disposição: INCORPORADO | PARCIAL | REFERÊNCIA | FORA + motivo) e conferido por
[STRUCT-13] do validate_spec_sot.py.

O script NÃO altera estados, NÃO promove itens e NÃO é gate de conformidade: a promoção
`→ ATIVADO` e `→ Absorvido/Descartado` é homologada por Andraus (RMR-001 §5).
Exit 0 ≠ CONFORME ≠ homologação.
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

TRUE, FALSE, MANUAL = "TRUE", "FALSE", "MANUAL"
STATES = ("Proposto", "Em espera", "ATIVADO", "Absorvido", "Descartado", "Diferido")


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


class Facts:
    """Fatos objetivos do repositório usados para avaliar gatilhos."""

    def __init__(self, root: Path):
        self.root = root
        road = read(root / "ROADMAP.md")
        self.homolog, self.drafting, self.closed_decisions = set(), set(), set()

        for line in road.split("\n"):
            m = re.match(r"^(?:#{2,4}\s*|\|\s*)\**SPEC-(\d{3})\b", line)
            # "ABERTURA HOMOLOGADA" (Dossiê/escopo) ≠ Spec homologada (baseline): só conta a Spec
            # homologada quando o HOMOLOGAD não é de abertura (DHR-BACKLOG-ABERTURA-001).
            if m and re.search(r"HOMOLOGAD", re.sub(r"ABERTURA\s+HOMOLOGAD\w*", "", line, flags=re.I)):
                self.homolog.add(m.group(1))
            if re.match(r"\|\s*Decisões FECHADAS\s*\|", line):
                for seg in line.split("·"):  # só o 1º ID de cada segmento é decisão fechada
                    d = re.search(r"\b([A-Z]-\d{3})\b", seg)
                    if d:
                        self.closed_decisions.add(d.group(1))

        feats = root / "specs" / "features"
        if feats.exists():
            for d in feats.iterdir():
                m = re.match(r"SPEC-(\d{3})$", d.name)
                if not m:
                    continue
                self.drafting.add(m.group(1))  # diretório existe = redação iniciada
                plan = read(d / "plan.md")
                head = "\n".join(plan.split("\n")[:12])
                if re.search(r"Status:.*HOMOLOGAD", re.sub(r"(?i)abertura\s+homologad\w*", "", head)):
                    self.homolog.add(m.group(1))

        self.eua_homolog = set()
        gov = root / "governance"
        if gov.exists():
            for p in gov.glob("DHR-EUA-E*.md"):
                m = re.match(r"DHR-EUA-E(\d{2}[a-z]?)", p.name)
                if m:
                    self.eua_homolog.add(m.group(1))


def eval_cond(cond: str, f: Facts):
    """Retorna (estado, rótulo) para uma condição atômica."""
    c = cond.strip().strip("`").strip()
    m = re.match(r"spec:\s*SPEC-(\d{3})(?:\.\.(\d{3}))?\s+(homologad[ao]|em redação)", c, re.I)
    if m:
        lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
        ids = {f"{n:03d}" for n in range(lo, hi + 1)}
        homolog = m.group(3).lower().startswith("homolog")
        pool = f.homolog if homolog else (f.drafting | f.homolog)
        return (TRUE if ids & pool else FALSE), c
    m = re.match(r"spec:\s*EUA-E(\d{2}[a-z]?)\s+homologad[ao]", c, re.I)
    if m:
        return (TRUE if m.group(1) in f.eua_homolog else FALSE), c
    m = re.match(r"decisao:\s*([A-Z]-\d{3})\s+resolvid[ao]", c, re.I)
    if m:
        return (TRUE if m.group(1) in f.closed_decisions else FALSE), c
    return MANUAL, c  # evento:/milestone:/hygiene:/formato desconhecido


def eval_trigger(text: str, f: Facts):
    """OR de alternativas; cada alternativa é AND de condições. Retorna (estado, [rótulos manuais])."""
    text = text.replace("`", "")
    manual, alt_states = [], []
    for alt in re.split(r"\s*∨\s*", text):
        conds = [eval_cond(c, f) for c in re.split(r"\s*∧\s*", alt)]
        states = [s for s, _ in conds]
        manual += [lbl for s, lbl in conds if s == MANUAL]
        if FALSE in states:
            alt_states.append(FALSE)
        elif MANUAL in states:
            alt_states.append(MANUAL)
        else:
            alt_states.append(TRUE)
    if TRUE in alt_states:
        return TRUE, []
    if MANUAL in alt_states:
        return MANUAL, manual
    return FALSE, []


def parse_items(rmr_text: str):
    items = []
    for line in rmr_text.split("\n"):
        m = re.match(r"^\|\s*\*\*(BL-\d{3})\*\*\s*\|", line)
        if not m:
            continue
        cells = line.split("|")
        if len(cells) < 10:
            continue
        estado_raw = re.sub(r"[*`]", "", cells[-3]).strip()
        estado = next((s for s in STATES if estado_raw.lower().startswith(s.lower())), "?")
        items.append({
            "id": m.group(1),
            "titulo": cells[2].strip(),
            "gatilho": cells[5].strip(),
            "estado": estado,
            "linha": line,
        })
    return items


def slot_state(spec_id: str, f: "Facts") -> str:
    """Estado do slot de Spec para o mapa de gatilhos (EUA-E21 — slot indicativo por padrão)."""
    if spec_id in f.homolog:
        return "Homologada"
    if spec_id in f.drafting:
        return "Em redação"
    return "Indicativa (não aberta)"


def slot_trigger_map(items, f: "Facts"):
    """
    BL-021 item (2): mapa slot→Spec de cada gatilho `spec:SPEC-nnn ...` contra o estado
    real do slot, com sinalização SUAVE (heurística, não-normativa) de possível
    re-apontamento pendente (RMR-001 §3 / RULE-ECC-01) quando o slot referenciado ainda
    não abriu e a linha do item não menciona re-apontamento/slot mantido.
    Somente leitura — não altera exit code nem promove nada.
    """
    rows = []
    seen = set()
    for it in items:
        for m in re.finditer(r"SPEC-(\d{3})(?:\.\.(\d{3}))?", it["gatilho"]):
            lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
            for n in range(lo, hi + 1):
                spec_id = f"{n:03d}"
                key = (it["id"], spec_id)
                if key in seen:
                    continue
                seen.add(key)
                estado = slot_state(spec_id, f)
                mencionado = bool(re.search(r"re-apontamento|slot mantido|slot alterado", it["linha"], re.I))
                aviso = (estado == "Indicativa (não aberta)" and not mencionado)
                rows.append({
                    "bl": it["id"], "spec": f"SPEC-{spec_id}", "estado_slot": estado,
                    "re_apontamento_mencionado": mencionado, "aviso": aviso,
                })
    return rows


DISPOSICAO_RE = r"Disposi[çc][ãa]o:\s*(INCORPORADO|PARCIAL|REFER[ÊE]NCIA|FORA)"


def abertura_scope(items, spec_nnn: str, f: "Facts"):
    """
    Itens VINCULADOS por regra à abertura de SPEC-nnn: estado não encerrado e alguma
    alternativa (∨) do gatilho contendo `spec:SPEC-nnn em redação` (faixa incluída).
    alcance = TOTAL se a alternativa tem só essa condição (ou as demais já são TRUE);
              PARCIAL se há condição ∧ ainda não satisfeita/manual (o item só se realiza em parte).
    Determinístico; somente leitura.
    """
    n = int(spec_nnn)
    out = []
    for it in items:
        if it["estado"] in ("Absorvido", "Descartado"):
            continue
        text = it["gatilho"].replace("`", "")
        hit, alcance = False, "TOTAL"
        for alt in re.split(r"\s*∨\s*", text):
            conds = re.split(r"\s*∧\s*", alt)
            mine = False
            for c in conds:
                m = re.match(r"\s*spec:\s*SPEC-(\d{3})(?:\.\.(\d{3}))?\s+em redação", c, re.I)
                if m and int(m.group(1)) <= n <= int(m.group(2) or m.group(1)):
                    mine = True
            if mine:
                hit = True
                others = [eval_cond(c, f)[0] for c in conds
                          if not re.match(r"\s*spec:\s*SPEC-\d{3}(?:\.\.\d{3})?\s+em redação", c, re.I)]
                alcance = "TOTAL" if all(s == TRUE for s in others) else "PARCIAL"
                break
        if hit:
            out.append({"id": it["id"], "titulo": it["titulo"], "estado": it["estado"], "alcance": alcance})
    return out


def plan_declara(plan_text: str, bl_id: str) -> bool:
    """True se alguma linha do plan.md cita o BL e traz `Disposição: <valor>` (declaração explícita)."""
    for line in plan_text.split("\n"):
        if bl_id in line and re.search(DISPOSICAO_RE, line, re.I):
            return True
    return False


def abertura_pendentes(root: Path):
    """Specs em redação (não homologadas) cujo plan.md ainda não declara a disposição de cada item vinculado."""
    f = Facts(root)
    items = parse_items(read(root / "backlog" / "RMR-001_Painel_Backlog.md"))
    pend = []
    for nnn in sorted(f.drafting - f.homolog):
        scope = abertura_scope(items, nnn, f)
        plan = read(root / "specs" / "features" / f"SPEC-{nnn}" / "plan.md")
        faltam = [x["id"] for x in scope if not plan_declara(plan, x["id"])]
        if faltam and plan:  # sem plan.md ainda = Spec só em abertura; o gate cobra quando o Plan existir
            pend.append({"spec": f"SPEC-{nnn}", "faltam": faltam})
    return pend


def build_report(root: Path):
    rmr = read(root / "backlog" / "RMR-001_Painel_Backlog.md")
    facts = Facts(root)
    out = {"ativados": [], "disparados_sem_registro": [], "manual": [], "aguardando": [], "encerrados": [], "ilegiveis": []}
    for it in parse_items(rmr):
        if it["estado"] in ("Absorvido", "Descartado"):
            out["encerrados"].append(it["id"])
            continue
        if it["estado"] == "?":
            out["ilegiveis"].append(it["id"])
            continue
        state, manual = eval_trigger(it["gatilho"], facts)
        it["avaliacao"] = state
        if it["estado"] == "ATIVADO":
            out["ativados"].append(it)
        elif state == TRUE:
            out["disparados_sem_registro"].append(it)
        elif state == MANUAL:
            it["condicoes_manuais"] = manual
            out["manual"].append(it)
        else:
            out["aguardando"].append(it)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--abertura", metavar="SPEC-NNN")
    ap.add_argument("--abertura-pendentes", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    if not (root / "backlog" / "RMR-001_Painel_Backlog.md").exists():
        print("ERRO: backlog/RMR-001_Painel_Backlog.md não encontrado.", file=sys.stderr)
        sys.exit(2)

    if args.abertura:
        m = re.match(r"(?:SPEC-)?(\d{3})$", args.abertura.strip(), re.I)
        if not m:
            print("ERRO: use --abertura SPEC-NNN (ex.: SPEC-006).", file=sys.stderr)
            sys.exit(2)
        scope = abertura_scope(parse_items(read(root / "backlog" / "RMR-001_Painel_Backlog.md")), m.group(1), Facts(root))
        if args.json:
            print(json.dumps(scope, ensure_ascii=False, indent=1))
        else:
            print(f"ITENS VINCULADOS À ABERTURA DE SPEC-{m.group(1)} ({len(scope)}) — por regra, sem promoção (DHR-BACKLOG-ABERTURA-001)")
            for x in scope:
                print(f"  - {x['id']} [{x['estado']}] alcance={x['alcance']} — {x['titulo']}")
            print("O Plan deve declarar `Disposição: INCORPORADO|PARCIAL|REFERÊNCIA|FORA` + motivo em cada item ([STRUCT-13]).")
        sys.exit(0)

    if args.abertura_pendentes:
        pend = abertura_pendentes(root)
        if args.json:
            print(json.dumps(pend, ensure_ascii=False, indent=1))
        elif pend:
            for x in pend:
                print(f"ABERTURA-PENDENTE {x['spec']}: plan.md sem Disposição para " + ", ".join(x["faltam"]))
        else:
            print("ABERTURA-PENDENTE: nenhuma")
        sys.exit(0)

    rep = build_report(root)
    div, ativ = rep["disparados_sem_registro"], rep["ativados"]
    facts = Facts(root)
    slot_map = slot_trigger_map(parse_items(read(root / "backlog" / "RMR-001_Painel_Backlog.md")), facts)
    rep["mapa_slots"] = slot_map

    if args.json:
        print(json.dumps(rep, ensure_ascii=False, indent=1))
    else:
        print("=" * 60)
        print("BACKLOG — gatilhos de ativação (BL-006 / RMR-001 §4)")
        print("=" * 60)
        print(f"\nDISPARADOS SEM REGISTRO ({len(div)}) — achado de gate: promover a ATIVADO (Andraus)")
        for it in div:
            print(f"  ! {it['id']} [{it['estado']}] {it['titulo']}")
        print(f"\nATIVADOS ({len(ativ)}) — exigem encaminhamento no gate")
        for it in ativ:
            print(f"  * {it['id']} {it['titulo']}")
        print(f"\nVERIFICAÇÃO MANUAL ({len(rep['manual'])}) — gatilho depende de evento/milestone/hygiene")
        for it in rep["manual"]:
            print(f"  ? {it['id']} [{it['estado']}] {it['titulo']}")
            for c in it["condicoes_manuais"]:
                print(f"      - {c}")
        print(f"\nAGUARDANDO ({len(rep['aguardando'])}): " + ", ".join(i["id"] for i in rep["aguardando"]))
        print(f"ENCERRADOS ({len(rep['encerrados'])}): " + ", ".join(rep["encerrados"]))
        if rep["ilegiveis"]:
            print(f"ESTADO ILEGÍVEL ({len(rep['ilegiveis'])}): " + ", ".join(rep["ilegiveis"]))
        if slot_map:
            print(f"\nMAPA DE GATILHOS spec: → ESTADO DO SLOT ({len(slot_map)}) — BL-021 item 2, informativo, EUA-E21")
            for r in slot_map:
                flag = "  ⚠ possível re-apontamento não mencionado" if r["aviso"] else ""
                print(f"  {r['bl']} → {r['spec']} [{r['estado_slot']}]{flag}")
        print("-" * 60)
        print("Somente leitura: não promove itens. exit 0 ≠ CONFORME ≠ homologação.")

    sys.exit(1 if (div or (args.strict and ativ)) else 0)


if __name__ == "__main__":
    main()
