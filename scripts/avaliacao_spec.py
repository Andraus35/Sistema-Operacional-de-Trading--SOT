#!/usr/bin/env python3
"""avaliacao_spec.py — avaliação de desempenho de fim de Spec, DETERMINÍSTICA e OBRIGATÓRIA (DHR-AVALIACAO-001).

Ordem de Andraus (2026-11-08): ao fim do ciclo de cada Spec, a avaliação de desempenho chega à análise dele, de forma
determinística, com perguntas automatizadas e recomendações de boas práticas. Este script:
  1. mede o desempenho da Spec a partir dos pareceres do Revisor (via loop_ledger): rodadas, Críticas/Médias/Menores por rodada,
     veredito, modo (delta/integral), tokens (n/m = não medido), % de Menores resolvidos pela classe M, categorias recorrentes e
     sua prevenção, tamanho do Plan (RULE-ECC-07);
  2. escolhe, por regra FIXA do catálogo `governance/aprendizado/BOAS-PRATICAS.json`, quais recomendações e perguntas se aplicam;
  3. grava `governance/aprendizado/AVALIACOES/AVALIACAO-SPEC-nnn.md` (Estado GERADA → RESPONDIDA) com as perguntas prontas para
     AskUserQuestion (lotes de até 4; recomendada em 1º lugar);
  4. barra: `--retro-check` do loop_ledger e a guarda de fim de turno exigem a avaliação RESPONDIDA antes de abrir outra Spec.
"Aprovação final da Spec" = ata `DHR-SPECnnn-*_Ata_Homologacao_Plan*` (ou `_Homologacao_SPEC-nnn`) com Status "HOMOLOGADO … BASELINE".
PROSPECTIVO: só Specs cuja ata de aprovação final tem Data >= CUTOFF (as já homologadas ficam fora).
Mesma entrada => mesma saída (sem relógio nem aleatoriedade). Detector (ENF-03): não decide, não homologa, não aplica proposta, não fecha
decisão aberta (CONS-01); toda recomendação é PROPOSTA que só vira mecanismo por ordem expressa de Andraus.

Uso:
  python scripts/avaliacao_spec.py gerar SPEC-nnn [--write|--stdout]   # gera/mostra a avaliação
  python scripts/avaliacao_spec.py perguntas SPEC-nnn                  # JSON dos lotes de AskUserQuestion
  python scripts/avaliacao_spec.py registrar SPEC-nnn --ata DHR-... --resposta "<citação da decisão de Andraus>"
  python scripts/avaliacao_spec.py --pendentes [--json]                # Specs exigidas sem avaliação RESPONDIDA (exit 1 se houver)
  python scripts/avaliacao_spec.py --ci                                # exit 1 se Spec exigida sem avaliação atual (AUSENTE/DESATUALIZADA)
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import loop_ledger as L  # noqa: E402

ROOT = HERE.parent
CUTOFF = "2026-11-08"  # DHR-AVALIACAO-001: só vale para Spec cuja aprovação final ocorra a partir desta data
AV_DIR = "governance/aprendizado/AVALIACOES"
CATALOGO = "governance/aprendizado/BOAS-PRATICAS.json"
ATA_RE = re.compile(r"^DHR-SPEC(\d{3})-\d{3}_Ata_Homologacao_(?:Plan.*|SPEC-\d{3})\.md$")
OPS = {">=": lambda a, b: a >= b, ">": lambda a, b: a > b, "<=": lambda a, b: a <= b, "<": lambda a, b: a < b, "==": lambda a, b: a == b}
VEREDITO_RE = re.compile(r"(N[ÃA]O CONFORME|CONFORME condicional|CONFORME)", re.I)
FICHA_RE = re.compile(r"<!--\s*FICHA-M\s*(.*?)-->", re.S)
ESTADO_RE = re.compile(r"^\| Estado \| (\w+) \|$", re.M)
DIGEST_RE = re.compile(r"<!--\s*DIGEST:([0-9a-f]{64})\s*-->")


# ---------- aprovação final (prospectiva) ----------
def aprovadas(root):
    """spec -> {"ata","data"} para Specs com ata de aprovação final (Status HOMOLOGADO … BASELINE). Ata mais recente vence."""
    out = {}
    for f in sorted((Path(root) / "governance").glob("DHR-SPEC*_Ata_Homologacao_*.md")):
        m = ATA_RE.match(f.name)
        if not m:
            continue
        txt = f.read_text(encoding="utf-8", errors="replace")
        st = re.search(r"^\|\s*Status\s*\|(.*)$", txt, re.M)
        dt = re.search(r"^\|\s*Data\s*\|\s*(\d{4}-\d{2}-\d{2})", txt, re.M)
        if not st or not dt or "HOMOLOGAD" not in st.group(1).upper() or "BASELINE" not in st.group(1).upper():
            continue
        spec = f"SPEC-{m.group(1)}"
        cand = {"ata": f.name.split("_")[0], "data": dt.group(1)}
        if spec not in out or cand["data"] >= out[spec]["data"]:
            out[spec] = cand
    return out


def exigida(root, spec):
    a = aprovadas(root).get(spec)
    return bool(a and a["data"] >= CUTOFF)


# ---------- métricas ----------
def metricas(root, spec):
    root = Path(root)
    linhas = {k: v for k, v in L.coletar(root).items() if k.split()[0] == spec}
    reg = L.ler_registro(root)
    por_linha, cats = {}, {}
    tot_menor = tot_ficha = sem_tokens = integral_pos_r1 = medias_r1 = 0
    for chave in sorted(linhas):
        rodadas = []
        for rod in sorted(linhas[chave]):
            d = linhas[chave][rod]
            sev = {"Crítica": 0, "Média": 0, "Menor": 0}
            for a in d["achados"]:
                if a["sev"] in sev:
                    sev[a["sev"]] += 1
                cod = a["cat"][0]
                cats.setdefault(cod, set()).add((chave, rod))
            txt = (root / d["arquivo"]).read_text(encoding="utf-8", errors="replace")
            vm = VEREDITO_RE.search(txt.split("## Achados")[0]) or VEREDITO_RE.search(txt)
            ficha = 0
            for b in FICHA_RE.findall(txt):
                try:
                    ficha += len(json.loads(b.strip()).get("achados", []))
                except ValueError:
                    pass
            tot_menor += sev["Menor"]
            tot_ficha += ficha
            if d["tokens"] == "n/m":
                sem_tokens += 1
            if rod > 1 and d["modo"] == "integral":
                integral_pos_r1 += 1
            if rod == min(linhas[chave]):
                medias_r1 = max(medias_r1, sev["Média"])
            rodadas.append({"rodada": rod, "arquivo": d["arquivo"], "critica": sev["Crítica"], "media": sev["Média"], "menor": sev["Menor"],
                            "veredito": vm.group(1).upper() if vm else "n/d", "modo": d["modo"], "tokens": d["tokens"], "ficha_m": ficha})
        por_linha[chave] = rodadas
    recorrentes = sorted(c for c, s in cats.items() if len({r for r in s}) >= 2)
    sem_prev = [c for c in recorrentes if (reg.get(c, {}).get("prev", "AUSENTE").strip().upper().startswith("AUSENTE") or c not in reg)]
    tam = L.tamanho_plan(root, spec)
    return {
        "spec": spec,
        "linhas": por_linha,
        "max_rodadas_linha": max((len(v) for v in por_linha.values()), default=0),
        "rodadas_total": sum(len(v) for v in por_linha.values()),
        "rodadas_integral_apos_r1": integral_pos_r1,
        "rodadas_sem_tokens": sem_tokens,
        "medias_r1_max": medias_r1,
        "menores_total": tot_menor,
        "menores_classe_m": tot_ficha,
        "pct_menores_classe_m": (100 if tot_menor == 0 else int(100 * tot_ficha / tot_menor)),
        "categorias": {c: sorted(f"{k}#R{r}" for k, r in s) for c, s in sorted(cats.items())},
        "categorias_recorrentes": recorrentes,
        "categorias_recorrentes_sem_prevencao": len(sem_prev),
        "categorias_recorrentes_sem_prevencao_lista": sem_prev,
        "plan_linhas_total": tam[0] if tam else 0,
        "plan_corpo_linhas": tam[1] if tam else 0,
        "retrospectiva_feita": spec in L.retros_feitas(root),
    }


# ---------- catálogo, recomendações e perguntas ----------
def carregar_catalogo(root):
    return json.loads((Path(root) / CATALOGO).read_text(encoding="utf-8"))["itens"]


def aplica(item, m):
    g = item["gatilho"]
    if g["tipo"] == "sempre":
        return True
    if g["tipo"] == "metrica":
        return OPS[g["op"]](m.get(g["nome"], 0), g["valor"])
    if g["tipo"] == "categoria":
        return len(m["categorias"].get(g["cod"], [])) >= g["min_rodadas"]
    raise ValueError(g)


def selecionar(root, m):
    itens = [i for i in carregar_catalogo(root) if aplica(i, m)]
    itens.sort(key=lambda i: (i["id"] == "BP-01", i["id"]))  # aceitação (BP-01) por último
    return itens


def lotes(itens):
    qs = [{"question": i["pergunta"], "header": i["cabecalho"][:12], "multiSelect": False,
           "options": [{"label": o["label"], "description": o["description"]} for o in i["opcoes"]], "origem": i["id"]} for i in itens]
    return [qs[i:i + 4] for i in range(0, len(qs), 4)]


def digest(m, itens):
    base = json.dumps({"m": m, "itens": [i["id"] for i in itens], "cutoff": CUTOFF}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(base.encode("utf-8")).hexdigest()


def caminho(root, spec):
    return Path(root) / AV_DIR / f"AVALIACAO-{spec}.md"


def gerar_texto(root, spec, estado="GERADA", resposta="—", ata_reg="—"):
    m = metricas(root, spec)
    itens = selecionar(root, m)
    ap = aprovadas(root).get(spec, {"ata": "—", "data": "—"})
    o = [f"# AVALIAÇÃO DE DESEMPENHO — {spec} (fim de ciclo) — GERADA por `scripts/avaliacao_spec.py` (DHR-AVALIACAO-001)", "",
         "> **Detector (ENF-03)**: números extraídos dos pareceres do Revisor; recomendações do catálogo `" + CATALOGO + "` (PROPOSTAS, nunca aplicadas sozinhas). "
         "Não decide, não homologa, não fecha decisão aberta (CONS-01). Fontes EXTERNAS são referência geral, não verificada nesta sessão.", "",
         "| Campo | Valor |", "|---|---|",
         f"| Spec | {spec} |", f"| Estado | {estado} |",
         f"| Ata de aprovação final | {ap['ata']} ({ap['data']}) |", f"| Resposta de Andraus | {resposta} |", f"| Ata do registro | {ata_reg} |", "",
         "## 1. Desempenho (4Es; Economicidade = INDETERMINADO enquanto tokens n/m)", "",
         "| Linha | Rodada | Crítica | Média | Menor | Veredito | Modo | Tokens | FICHA-M |", "|---|---|---|---|---|---|---|---|---|"]
    for ch, rs in m["linhas"].items():
        for r in rs:
            o.append(f"| {ch} | R{r['rodada']} | {r['critica']} | {r['media']} | {r['menor']} | {r['veredito']} | {r['modo']} | {r['tokens']} | {r['ficha_m']} |")
    o += ["", "| Indicador | Valor |", "|---|---|",
          f"| Rodadas no total / máx. numa linha | {m['rodadas_total']} / {m['max_rodadas_linha']} |",
          f"| Médias na 1ª rodada (máx. entre linhas) | {m['medias_r1_max']} |",
          f"| Rodadas integrais depois da 1ª | {m['rodadas_integral_apos_r1']} |",
          f"| Rodadas sem tokens medidos | {m['rodadas_sem_tokens']} |",
          f"| Menores resolvidos pela classe M | {m['menores_classe_m']} de {m['menores_total']} ({m['pct_menores_classe_m']}%) |",
          f"| Categorias recorrentes (≥2 rodadas) | {', '.join(m['categorias_recorrentes']) or 'nenhuma'} |",
          f"| …delas, sem prevenção registrada | {m['categorias_recorrentes_sem_prevencao']} ({', '.join(m['categorias_recorrentes_sem_prevencao_lista']) or '—'}) |",
          f"| Plan: linhas totais / corpo (alerta 1.900, teto 2.000) | {m['plan_linhas_total']} / {m['plan_corpo_linhas']} |",
          f"| Retrospectiva registrada (`FEITA`) | {'sim' if m['retrospectiva_feita'] else 'não'} |", "",
          "## 2. Recomendações de boas práticas (PROPOSTAS; fontes e 4Es por item)", ""]
    for i in itens:
        o.append(f"- **{i['id']} — {i['titulo']}** ({i['efeito_4Es']}): {i['recomendacao']}")
        for f in i["fontes"]:
            o.append(f"  - fonte {f['tipo']}: {f['ref']}" + (f" — _{f['nota']}_" if f.get("nota") else ""))
    o += ["", "## 3. Perguntas automatizadas para Andraus (AskUserQuestion; recomendada em 1º lugar)", "",
          "```json", json.dumps(lotes(itens), ensure_ascii=False, indent=1), "```", "",
          "## 4. Como fechar", "",
          "1. Apresentar os lotes acima a Andraus por AskUserQuestion (linguagem de trader). 2. Registrar a decisão dele em ata (DHR-…) e rodar "
          "`python scripts/avaliacao_spec.py registrar " + spec + " --ata DHR-… --resposta \"<citação>\"`. 3. Registrar a retrospectiva "
          "(`RETROSPECTIVAS.md`, `FEITA`). Sem isso `loop_ledger.py --retro-check " + spec + "` falha e a próxima Spec não abre (salvo dispensa expressa de Andraus).", "",
          f"<!-- DIGEST:{digest(m, itens)} -->", ""]
    return "\n".join(o)


# ---------- estado ----------
def estado(root, spec):
    """AUSENTE | DESATUALIZADA | GERADA | RESPONDIDA."""
    p = caminho(root, spec)
    if not p.is_file():
        return "AUSENTE"
    txt = p.read_text(encoding="utf-8")
    d = DIGEST_RE.search(txt)
    m = metricas(root, spec)
    if not d or d.group(1) != digest(m, selecionar(root, m)):
        return "DESATUALIZADA"
    e = ESTADO_RE.search(txt)
    if e and e.group(1) == "RESPONDIDA" and "| Resposta de Andraus | —" not in txt and "| Ata do registro | —" not in txt:
        return "RESPONDIDA"
    return "GERADA"


def pendentes(root):
    out = []
    for spec in sorted(aprovadas(root)):
        if exigida(root, spec):
            e = estado(root, spec)
            if e != "RESPONDIDA":
                out.append({"spec": spec, "estado": e, "ata": aprovadas(root)[spec]["ata"]})
    return out


def registrar(root, spec, ata, resposta):
    if estado(root, spec) in ("AUSENTE", "DESATUALIZADA"):
        raise SystemExit(f"{spec}: avaliação {estado(root, spec)} — regere antes (gerar {spec} --write).")
    if not list((Path(root) / "governance").glob(f"{ata}_*.md")):
        raise SystemExit(f"Ata {ata} não existe em governance/ — o registro exige a ata da decisão de Andraus.")
    if not resposta.strip() or resposta.strip() == "—":
        raise SystemExit("Resposta de Andraus vazia.")
    p = caminho(root, spec)
    t = p.read_text(encoding="utf-8")
    t = ESTADO_RE.sub("| Estado | RESPONDIDA |", t)
    t = re.sub(r"^\| Resposta de Andraus \|.*$", "| Resposta de Andraus | " + resposta.replace("|", "/").strip() + " |", t, flags=re.M)
    t = re.sub(r"^\| Ata do registro \|.*$", f"| Ata do registro | {ata} |", t, flags=re.M)
    p.write_text(t, encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", nargs="?", choices=["gerar", "perguntas", "registrar"])
    ap.add_argument("spec", nargs="?")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--pendentes", action="store_true")
    ap.add_argument("--ci", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--ata")
    ap.add_argument("--resposta", default="")
    ap.add_argument("--root", default=str(ROOT))
    a = ap.parse_args(argv)
    root = Path(a.root)
    if a.pendentes or a.ci:
        pend = pendentes(root)
        if a.ci:
            pend = [p for p in pend if p["estado"] in ("AUSENTE", "DESATUALIZADA")]
        if a.json:
            print(json.dumps(pend, ensure_ascii=False))
        else:
            for p in pend:
                print(f"AVALIAÇÃO {p['estado']}: {p['spec']} (aprovação final: {p['ata']}) — rode: python scripts/avaliacao_spec.py gerar {p['spec']} --write")
            if not pend:
                print("Nenhuma avaliação pendente.")
        return 1 if pend else 0
    if not a.cmd or not a.spec:
        ap.error("informe o comando e a Spec (ex.: gerar SPEC-008)")
    if a.cmd == "gerar":
        txt = gerar_texto(root, a.spec)
        if a.write:
            p = caminho(root, a.spec)
            p.parent.mkdir(parents=True, exist_ok=True)
            if p.is_file() and estado(root, a.spec) == "RESPONDIDA":
                print(f"{a.spec}: avaliação já RESPONDIDA e atual — não sobrescrevo.")
                return 0
            p.write_text(txt, encoding="utf-8")
            print(f"Avaliação gravada em {p.relative_to(root)} (Estado GERADA).")
        else:
            print(txt)
        return 0
    if a.cmd == "perguntas":
        m = metricas(root, a.spec)
        print(json.dumps(lotes(selecionar(root, m)), ensure_ascii=False, indent=1))
        return 0
    if a.cmd == "registrar":
        if not a.ata:
            ap.error("registrar exige --ata")
        registrar(root, a.spec, a.ata, a.resposta)
        print(f"{a.spec}: avaliação RESPONDIDA (ata {a.ata}).")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
