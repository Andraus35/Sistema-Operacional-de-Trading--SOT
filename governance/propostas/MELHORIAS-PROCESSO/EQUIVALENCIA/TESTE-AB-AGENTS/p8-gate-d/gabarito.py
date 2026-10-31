import re,sys
K={1:[r"prossig|proced|an[áa]lise sem[âa]ntica|segue|continu|aceit|v[áa]lid",r"passou_d|via gate-d|gate-d"],
2:[r"n[ãa]o verificado|ausente|inv[áa]lid|falha fechada",r"condicional"],
3:[r"n[ãa]o verificado|ausente|falha fechada",r"condicional"],
4:[r"n[ãa]o conforme",r"cr[íi]tica",r"sem an[áa]lise sem[âa]ntica|imediat"],
5:[r"n[ãa]o verificado|ausente|inv[áa]lid|campos|falha fechada",r"condicional"],
6:[r"\bn[ãa]o\b",r"bash|orquestrador|n[ãa]o confirma"],
7:[r"\bn[ãa]o\b",r"devolv|regera|impede|reprovad|orquestrador"],
8:[r"\bn[ãa]o\b",r"devolv|regera|impede|reprovad|orquestrador"]}
def pontuar(t):
    r={}
    for l in t.splitlines():
        m=re.match(r"\s*\**C(\d+)\**\s*:\s*(.*)",l)
        if m: r[int(m.group(1))]=m.group(2)
    return {q:(bool(r.get(q)) and "nao consta" not in r[q].lower() and all(re.search(p,r[q],re.I) for p in pats)) for q,pats in K.items()}
if __name__=="__main__":
    ok=pontuar(open(sys.argv[1],encoding='utf8').read()); print(f"{sum(ok.values())}/{len(K)}  falhas:",[q for q,v in ok.items() if not v])
