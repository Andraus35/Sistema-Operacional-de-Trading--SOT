#!/usr/bin/env python3
"""loop_ledger.py — coleta DETERMINÍSTICA dos achados dos pareceres do Revisor (LOOP-001, DHR-LOOP-001).

Lê `governance/propostas/**/PARECER*.md` e `parecer-revisor-*.md` e gera `governance/aprendizado/LEDGER-ACHADOS.md`:
achados por linha de trabalho (Spec + tipo) e rodada, categoria da taxonomia fixa, recorrência entre rodadas/linhas,
e LACUNAS DE PREVENÇÃO (categoria recorrente sem entrada em `CAUSAS-PREVENCAO.md` ou com prevenção AUSENTE).
Métricas por 4Es (Conformidade, Eficácia, Efetividade, Eficiência; Economicidade = INDETERMINADO, tokens não medidos).

Duas fontes por achado (a estruturada prevalece):
  1. bloco `<!-- ACHADOS-ESTRUTURADOS ... -->` do parecer, linhas `ID|SEV|CATEGORIA|CAUSA|PREVENCAO`;
  2. extração HEURÍSTICA das seções "Média(s)/Crítica(s)/Menor(es)" (marcada `heuristica`).
Saída sem relógio nem aleatoriedade: mesma entrada ⇒ mesmo texto. Detector (ENF-03): não promove, não fecha decisão
(CONS-01), não é Gate; exit 0 ≠ CONFORME ≠ homologação.

Uso:
  python scripts/loop_ledger.py            # (re)gera o ledger
  python scripts/loop_ledger.py --check    # exit 1 se o ledger está desatualizado
  python scripts/loop_ledger.py --stdout   # imprime sem gravar
  python scripts/loop_ledger.py --retro-check SPEC-007   # exit 1 se falta a retrospectiva de fechamento (antes de abrir outra Spec)
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = "governance/aprendizado/LEDGER-ACHADOS.md"
REGISTRY = "governance/aprendizado/CAUSAS-PREVENCAO.md"
RETRO = "governance/aprendizado/RETROSPECTIVAS.md"

# Taxonomia fixa e ORDENADA (a primeira que casa vence). Heurística: não substitui a categoria estruturada do parecer.
TAXONOMIA = [
    ("C01", "contradicao_interna", r"contradi|dois desfechos|dois c[óo]digos|diverge|inconsist|n[ãa]o bate|diz o contr[áa]rio|incoerent"),
    ("C02", "ambiguidade_vocabulario", r"hom[ôo]nim|acep[çc][ãa]o|amb[íi]gu|vocabul[áa]rio|CC-10|SEM-01|r[óo]tulo|nome colide"),
    ("C03", "precondicao_teste", r"pr[ée]-?condi|fixture|inalcan[çc][áa]v|n[ãa]o alcan[çc][áa]v|entrada injet[áa]vel|sem entrada|estado inicial"),
    ("C04", "heranca_rastreabilidade", r"heran[çc]a|RULE-HD|REMOVED|rastre|mapeamento|supress|n[ãa]o disposta|silêncio|sil[êe]ncio"),
    ("C05", "observabilidade_enforcement", r"observabil|detect|EVIDENCE|enforcement|ENF-|falso-?ACEITE|amostr|n[ãa]o represent|n[ãa]o verific[áa]vel"),
    ("C06", "contagem_historico_anexo", r"contagem|hist[óo]ric|anexo|colchete|INV-07|c[óo]pia|truncad|numerad|renumer|editorial|reda[çc][ãa]o|rotulad"),
    ("C07", "citacao_ancora", r"\bl\.\s?\d|linha desatualizad|[âa]ncora|cita[çc][ãa]o|n[ãa]o confere|ponteiro"),
    ("C08", "decisao_aberta_escopo", r"CONS-01|decis[ãa]o aberta|DECIS[ÃA]O NECESS[ÁA]RIA|fecha de fato|escopo|fora do escopo|ordem de Andraus"),
    ("C09", "seguranca_guarda", r"inje[çc][ãa]o|vazament|trava|guarda|envio externo|reenvio|bypass|contorn|permiss"),
    ("C10", "estado_maquina", r"transi[çc][ãa]o|m[áa]quina de estados|\bD5\b|estado"),
]
OUTRA = ("C99", "outros")

SEV_SECAO = [
    (re.compile(r"^#{2,4}\s*Cr[ií]ticas?\b", re.I), "Crítica"),
    (re.compile(r"^#{2,4}\s*M[ée]dias?\b(?!\s+da\s+R\d)", re.I), "Média"),
    (re.compile(r"^#{2,4}\s*Menores?\b", re.I), "Menor"),
]
ID_RE = re.compile(r"(?:^|\*\*|·\s+|-\s+)((?:R\d-)?[MNmn]-\d{1,2}|[Rr]\d-[MNmn]\d{1,2})(?![\w-])")
BLOCO_RE = re.compile(r"<!--\s*ACHADOS-ESTRUTURADOS\s*(.*?)-->", re.S)


def categoria(texto):
    for cod, nome, rx in TAXONOMIA:
        if re.search(rx, texto, re.I):
            return cod, nome
    return OUTRA


def linha_trabalho(path):
    """(chave da linha de trabalho, rodada) a partir do caminho/nome."""
    p = str(path).replace("\\", "/")
    spec = re.search(r"SPEC-?(\d{3})", p, re.I)
    spec = f"SPEC-{spec.group(1)}" if spec else "SPEC-?"
    nome = Path(p).name.upper()
    tipo = "ABERTURA" if "ABERTURA" in nome else ("PLAN" if "PLAN" in nome else "OUTRO")
    r = re.search(r"-R(\d+)-|RODADA(\d+)|-R(\d+)\.", nome)
    rodada = int(next(g for g in r.groups() if g)) if r else 1
    return f"{spec} {tipo}", rodada


def extrair_estruturado(texto):
    achados = []
    for bloco in BLOCO_RE.findall(texto):
        for ln in bloco.strip().splitlines():
            partes = [x.strip() for x in ln.split("|")]
            if len(partes) >= 5 and not partes[0].upper().startswith("ID"):
                sev = {"CRITICA": "Crítica", "MEDIA": "Média", "MENOR": "Menor"}.get(partes[1].upper().replace("É", "E").replace("Í", "I"), partes[1])
                cat = next(((c, n) for c, n, _ in TAXONOMIA if c == partes[2]), OUTRA if partes[2] == "C99" else (partes[2], partes[2]))
                achados.append({"id": partes[0], "sev": sev, "cat": cat, "causa": partes[3], "prev": partes[4], "fonte": "estruturado"})
    return achados


def extrair_heuristico(texto):
    achados, sev, buf = [], None, []

    def fecha():
        if sev and buf:
            sec = "\n".join(buf)
            marcas = [(m.start(1), m.group(1)) for m in ID_RE.finditer(sec)]
            vistos = set()
            for i, (pos, fid) in enumerate(marcas):
                if fid in vistos:
                    continue
                vistos.add(fid)
                fim = marcas[i + 1][0] if i + 1 < len(marcas) else len(sec)
                achados.append({"id": fid, "sev": sev, "cat": categoria(sec[pos:fim]), "causa": "", "prev": "", "fonte": "heuristica"})
    for ln in texto.splitlines():
        if re.match(r"^#{1,4}\s", ln):
            fecha()
            buf = []
            sev = None
            for rx, s in SEV_SECAO:
                if rx.match(ln):
                    sev = s
                    break
            continue
        if sev:
            buf.append(ln)
    fecha()
    return achados


def metadados_rodada(texto):
    """(modo, sha256, tokens) declarados no parecer. Convenção (DHR-DELTA-HASH-001): linha `MODO: delta|integral`,
    `SHA256-ALVO: <64 hex>` e `TOKENS: <n>` no cabeçalho da transcrição. Sem a convenção: modo inferido de 'por delta' nas
    primeiras linhas (marcado '(inferido)'); sha256 ausente = 'ausente'; tokens = 'n/m' (não medido)."""
    m = re.search(r"MODO:\s*(delta|integral)", texto, re.I)
    if m:
        modo = m.group(1).lower()
    elif re.search(r"por delta", "\n".join(texto.splitlines()[:15]), re.I):
        modo = "delta (inferido)"
    else:
        modo = "n/d"
    h = re.search(r"SHA256-ALVO:\s*`?([0-9a-f]{64})", texto, re.I) or re.search(r"sha256[^0-9a-f\n]{0,40}([0-9a-f]{64})", texto, re.I)
    sha = h.group(1)[:12] if h else ("não conferido" if re.search(r"(n[ãa]o conferido|n[ãa]o verific)[^\n]{0,60}sha256|sha256[^\n]{0,40}(n[ãa]o conferido|n[ãa]o verific)", texto, re.I) else "ausente")
    t = re.search(r"TOKENS:\s*([\d.,]+)", texto, re.I)
    return modo, sha, (t.group(1) if t else "n/m")


def coletar(root):
    cands = sorted(set(list((root / "governance").rglob("PARECER*.md")) + list((root / "governance").rglob("parecer-revisor-*.md"))))
    linhas = defaultdict(dict)  # linha -> rodada -> {"arquivo","achados"}
    for f in cands:
        texto = f.read_text(encoding="utf-8", errors="replace")
        chave, rodada = linha_trabalho(f.relative_to(root))
        ach = extrair_estruturado(texto)
        ids = {a["id"] for a in ach}
        ach += [a for a in extrair_heuristico(texto) if a["id"] not in ids]
        modo, sha, tok = metadados_rodada(texto)
        linhas[chave][rodada] = {"arquivo": str(f.relative_to(root)).replace("\\", "/"), "achados": ach, "modo": modo, "sha": sha, "tokens": tok}
    return linhas


def ler_registro(root):
    """categoria -> prevenção ('AUSENTE' ou texto). Linhas `| C0x | ... | prevenção atual | ... |` em CAUSAS-PREVENCAO.md."""
    reg = {}
    p = root / REGISTRY
    if p.exists():
        for ln in p.read_text(encoding="utf-8").splitlines():
            cel = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cel) >= 5 and re.fullmatch(r"C\d{2}", cel[0]):
                reg[cel[0]] = {"causa": cel[2], "prev": cel[3], "gate": cel[4]}
    return reg


def retros_feitas(root):
    """Specs com retrospectiva de fechamento FEITA: linhas `| SPEC-nnn | ... | FEITA |` em RETROSPECTIVAS.md."""
    p = root / RETRO
    feitas = set()
    if p.exists():
        for ln in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*(SPEC-\d{3})\s*\|.*\|\s*FEITA\s*\|\s*$", ln)
            if m:
                feitas.add(m.group(1))
    return feitas


def specs_com_parecer(root):
    return sorted({chave.split()[0] for chave in coletar(root)})


def tamanho_plan(root, spec):
    """Linhas totais e de CORPO (antes do primeiro '## Anexo') do plan.md da Spec; None se ausente. RULE-ECC-07."""
    f = Path(root) / "specs" / "features" / spec / "plan.md"
    if not f.is_file():
        return None
    linhas = f.read_text(encoding="utf-8", errors="replace").splitlines()
    corpo = next((i for i, l in enumerate(linhas) if re.match(r"##\s+Anexo\b", l)), len(linhas))
    return len(linhas), corpo


def gerar(root):
    linhas = coletar(root)
    reg = ler_registro(root)
    out = ["# LEDGER DE ACHADOS DO LOOP DOS CONSTRUTORES — GERADO (não editar à mão)", "",
           "> Gerado por `python scripts/loop_ledger.py` (LOOP-001 / DHR-LOOP-001). **Detector (ENF-03)**: não promove, não fecha decisão aberta, "
           "não é Gate. Fonte: pareceres em `governance/`. Categoria `heuristica` = classificação por palavra-chave; `estruturado` = bloco "
           "`ACHADOS-ESTRUTURADOS` do parecer (prevalece). Causas e prevenções: `" + REGISTRY + "` (manual, append-only).", ""]
    # 1. Arquivos e extração
    out += ["## 1. Pareceres lidos e achados extraídos", "", "| Linha | Rodada | Arquivo | Crítica | Média | Menor |", "|---|---|---|---|---|---|"]
    tot_cat = defaultdict(lambda: defaultdict(set))  # cat -> {"rodadas": set((linha,rodada)), "linhas": set(linha)}
    contagem_cat = defaultdict(int)
    sem_extracao = []
    for linha in sorted(linhas):
        for rod in sorted(linhas[linha]):
            d = linhas[linha][rod]
            c = {"Crítica": 0, "Média": 0, "Menor": 0}
            for a in d["achados"]:
                c[a["sev"]] = c.get(a["sev"], 0) + 1
                cod = a["cat"][0]
                contagem_cat[cod] += 1
                tot_cat[cod]["rodadas"].add((linha, rod))
                tot_cat[cod]["linhas"].add(linha)
            if not d["achados"]:
                sem_extracao.append(d["arquivo"])
            out.append(f"| {linha} | R{rod} | `{d['arquivo']}` | {c['Crítica']} | {c['Média']} | {c['Menor']} |")
    out += ["", "Arquivos sem nenhum achado extraído (formato fora do padrão ou parecer sem achados; **não** é prova de ausência de achados): "
            + (", ".join(f"`{x}`" for x in sem_extracao) if sem_extracao else "nenhum"), ""]
    # 2. Tendência por linha (4Es: Eficácia/Eficiência)
    out += ["## 2. Tendência por linha de trabalho (Médias por rodada) — Eficácia e Eficiência", "",
            "| Linha | Médias por rodada | Rodadas lidas | Última rodada com 0 Média+Crítica |", "|---|---|---|---|"]
    for linha in sorted(linhas):
        seq = []
        for rod in sorted(linhas[linha]):
            ach = linhas[linha][rod]["achados"]
            seq.append(sum(1 for a in ach if a["sev"] in ("Média", "Crítica")))
        zero = [f"R{r}" for r, n in zip(sorted(linhas[linha]), seq) if n == 0 and linhas[linha][r]["achados"] is not None]
        out.append(f"| {linha} | {' → '.join(map(str, seq))} | {len(seq)} | {zero[-1] if zero else '—'} |")
    # 2-bis. Tamanho do alvo (Plans) x rodadas — insumo para calibrar os tetos da RULE-ECC-07 (medida, não regra)
    out += ["", "### 2-bis. Tamanho do Plan x rodadas (instrumentação de Economicidade; RULE-ECC-07)", "",
            "| Linha | Linhas totais | Linhas de corpo | Rodadas | Médias totais | Médias / 100 linhas de corpo | Tokens por rodada |", "|---|---|---|---|---|---|---|"]
    for linha in sorted(linhas):
        partes = linha.split()
        if len(partes) < 2 or partes[1] != "PLAN":
            continue
        t = tamanho_plan(root, partes[0])
        if not t:
            continue
        medias = sum(1 for r in linhas[linha] for a in linhas[linha][r]["achados"] if a["sev"] in ("Média", "Crítica"))
        dens = f"{100 * medias / t[1]:.2f}" if t[1] else "—"
        out.append(f"| {linha} | {t[0]} | {t[1]} | {len(linhas[linha])} | {medias} | {dens} | n/m |")
    out += ["", "### 2-ter. Modo da rodada, hash do alvo e tokens (instrumentação do delta por hash; DHR-DELTA-HASH-001)", "",
            "| Linha | Rodada | Modo | SHA256-ALVO | Tokens |", "|---|---|---|---|---|"]
    n_delta = n_total = n_sha = 0
    for linha in sorted(linhas):
        for rod in sorted(linhas[linha]):
            d = linhas[linha][rod]
            n_total += 1
            n_delta += d["modo"].startswith("delta")
            n_sha += d["sha"] not in ("ausente", "não conferido")
            out.append(f"| {linha} | R{rod} | {d['modo']} | {d['sha']} | {d['tokens']} |")
    out += ["", f"Rodadas por delta: {n_delta}/{n_total} · com SHA256-ALVO declarado: {n_sha}/{n_total}. Convenção no cabeçalho da transcrição: `MODO:`, `SHA256-ALVO:`, `TOKENS:` (tokens só se o ambiente os informar; nunca estimar).", ""]
    out += ["", "Tamanho = estado ATUAL do `plan.md` (não o de cada rodada); tokens por rodada seguem **n/m** (o repositório não os mede — registrar manualmente em `TELEMETRIA-ONDA0.md`).", ""]
    out += ["", "Economicidade (tokens/custo por rodada): **INDETERMINADO** — não medido pelo repositório.", ""]
    # 3. Categorias e recorrência
    out += ["## 3. Categorias, recorrência e prevenção registrada", "",
            "| Cod | Categoria | Achados | Rodadas distintas | Linhas distintas | Recorrente | Prevenção registrada |", "|---|---|---|---|---|---|---|"]
    nomes = {c: n for c, n, _ in TAXONOMIA}
    nomes[OUTRA[0]] = OUTRA[1]
    lacunas = []
    for cod in sorted(contagem_cat):
        rod, lin = len(tot_cat[cod]["rodadas"]), len(tot_cat[cod]["linhas"])
        recorrente = rod >= 2 or lin >= 2
        r = reg.get(cod)
        prev = (r["prev"] if r else "SEM ENTRADA")
        if recorrente and (not r or prev.strip().upper().startswith("AUSENTE")):
            lacunas.append((cod, nomes.get(cod, cod), contagem_cat[cod], rod))
        out.append(f"| {cod} | {nomes.get(cod, cod)} | {contagem_cat[cod]} | {rod} | {lin} | {'SIM' if recorrente else 'não'} | {prev} |")
    out += ["", "## 4. LACUNAS DE PREVENÇÃO (categoria recorrente sem prevenção registrada ou AUSENTE)", ""]
    if lacunas:
        out += ["| Cod | Categoria | Achados | Rodadas | Ação exigida pela regra LOOP-001 |", "|---|---|---|---|---|"]
        for cod, nome, n, rod in sorted(lacunas, key=lambda x: (-x[2], x[0])):
            out.append(f"| {cod} | {nome} | {n} | {rod} | registrar causa-raiz e prevenção proposta em `{REGISTRY}`; gate/processo só por ordem de Andraus |")
    else:
        out.append("Nenhuma.")
    feitas = retros_feitas(root)
    pend = [s for s in specs_com_parecer(root) if s not in feitas]
    out += ["", "## 5. Retrospectivas de fechamento (individual e coletiva) — regra LOOP-001", "",
            "O tratamento de melhoria ocorre ao FIM do trabalho completo de uma Spec e ANTES de abrir outra (ordem de Andraus, 2026-10-24). "
            "Specs com parecer e sem retrospectiva `FEITA` em `" + RETRO + "` (a Spec ainda em curso aparece aqui até fechar; o Orquestrador confere "
            "`--retro-check SPEC-nnn` de cada Spec FECHADA antes de abrir outra): " + (", ".join(pend) if pend else "nenhuma"), ""]
    out += ["## 6. Frase de controle", "",
            "Contagens por palavra-chave são **indicativas**; a fonte de verdade de cada achado é o parecer. Nenhuma decisão aberta é fechada por este arquivo (CONS-01).", ""]
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--retro-check", metavar="SPEC-nnn", help="exit 1 se a Spec não tem retrospectiva de fechamento FEITA (usar antes de abrir outra Spec)")
    ap.add_argument("--root", default=str(ROOT))
    a = ap.parse_args(argv)
    root = Path(a.root)
    if a.retro_check:
        if a.retro_check in retros_feitas(root):
            print(f"Retrospectiva de {a.retro_check}: FEITA.")
            return 0
        print(f"RETROSPECTIVA PENDENTE para {a.retro_check} — faça (individual e coletiva) em {RETRO} antes de abrir outra Spec, ou Andraus dispensa.")
        return 1
    txt = gerar(root)
    if a.stdout:
        print(txt)
        return 0
    dest = root / OUT
    if a.check:
        atual = dest.read_text(encoding="utf-8") if dest.exists() else ""
        if atual != txt:
            print(f"LEDGER DESATUALIZADO — rode: python scripts/loop_ledger.py ({OUT})")
            return 1
        print("Ledger em dia.")
        return 0
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(txt, encoding="utf-8")
    print(f"Ledger gravado: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
