import re,sys
# TODAS as regexes de cada item precisam casar (insensível a caixa). "NAO CONSTA" nunca pontua.
K={1:[r"\bn[ãa]o\b",r"1\s*:\s*3|r:r|retorno"],
2:[r"neutro"],
3:[r"orquestrador",r"ficha|aplicar_ficha_m|classe m"],
4:[r"especificador"],
5:[r"\bn[ãa]o\b|expir|vencid|venceu|120",r"120|n[ãa]o"],
6:[r"\bdado\b|ignor|n[ãa]o.{0,25}(instru|obedec|execut|segu)"],
7:[r"\bn[ãa]o\b",r"andraus|ata"],
8:[r"build_map",r"--check|check"],
9:[r"\bn[ãa]o\b|exced|acima|150"],
10:[r"\bn[ãa]o\b",r"custo|inv-04|salvaguarda|cee"],
11:[r"\bn[ãa]o\b",r"andraus|expres"],
12:[r"roadmap"]}
def pontuar(txt):
    r={}
    for l in txt.splitlines():
        m=re.match(r"\s*\**S(\d+)\**\s*:\s*(.*)",l)
        if m: r[int(m.group(1))]=m.group(2)
    ok={q:(bool(r.get(q)) and "nao consta" not in r[q].lower() and all(re.search(p,r[q],re.I) for p in pats)) for q,pats in K.items()}
    return ok
if __name__=="__main__":
    ok=pontuar(open(sys.argv[1],encoding='utf8').read())
    print(f"{sum(ok.values())}/{len(K)}  falhas:",[q for q,v in ok.items() if not v])
