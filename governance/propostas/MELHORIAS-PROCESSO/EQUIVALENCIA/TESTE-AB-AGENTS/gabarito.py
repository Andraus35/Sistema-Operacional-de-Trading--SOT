import re,sys,json
# cada item: lista de regexes; TODAS precisam casar (insensível a caixa). "NAO CONSTA" nunca pontua.
K={1:[r"1\s*:\s*3|3\s*:\s*1"],2:[r"70",r"7\s*/\s*9"],3:[r"elliott"],4:[r"\bn[ãa]o\b"],5:[r"\b8\b|oito"],
6:[r"par",r"report"],7:[r"150"],8:[r"validate_spec_sot"],9:[r"check_handoff"],10:[r"check_rpsa"],11:[r"check_doc_sync"],
12:[r"paus"],13:[r"\bdado\b"],14:[r"\b90\b"],15:[r"roadmap"],16:[r"andraus"],17:[r"\bdado\b",r"auditor|issue|achado"]}
def pontuar(txt):
    r={}
    for l in txt.splitlines():
        m=re.match(r"\s*\**Q(\d+)\**\s*:\s*(.*)",l)
        if m: r[int(m.group(1))]=m.group(2)
    ok={}
    for q,pats in K.items():
        a=r.get(q,"")
        ok[q]=bool(a) and "nao consta" not in a.lower() and all(re.search(p,a,re.I) for p in pats)
    return ok,r
if __name__=="__main__":
    ok,r=pontuar(open(sys.argv[1],encoding='utf8').read())
    print(f"{sum(ok.values())}/{len(K)}  falhas:",[q for q,v in ok.items() if not v])
