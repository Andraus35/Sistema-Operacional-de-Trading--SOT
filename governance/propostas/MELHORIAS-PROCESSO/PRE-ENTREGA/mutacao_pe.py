#!/usr/bin/env python3
"""mutacao_pe.py — P-E: planta defeitos conhecidos num Plan baselined e mede quais detectores os acham (PROPOSTA; informativo).
Uso: python mutacao_pe.py [specs/features/SPEC-049] -> tabela mutação x detector (recall) + falsos alarmes no original."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "scripts")); sys.path.insert(0, str(HERE))
import gate_extra as g, revisor_detectores as r, detectores_novos as n


def todos(plan, checks, base=None, irmaos=None):
    d = {"gate_extra.citacoes": lambda: g.citacoes_arquivo_linha(plan, ROOT), "gate_extra.contagens": lambda: g.contagens_declaradas(plan),
         "gate_extra.decisoes": lambda: g.decisoes_abertas_fechadas(plan), "gate_extra.assertivas": lambda: g.assertivas_checks(checks, plan),
         "gate_extra.sem_assertiva": lambda: g.corrigidos_sem_assertiva(checks), "rev.id_norma": lambda: r.id_norma_inexistente(plan, ROOT),
         "rev.contagem": lambda: r.contagem_declarada(plan), "rev.valor_fonte": lambda: r.valor_fonte(plan, ROOT),
         "NOVO C-1a codigos": lambda: n.codigos_sem_definicao(plan), "NOVO C-1b recusa": lambda: n.recusa_sem_codigo(plan), "NOVO C-4 checks": lambda: n.checks_ancorado(checks, plan)}
    if base is not None:
        d["NOVO C-2 token"] = lambda: n.token_antigo_presente(base, plan, irmaos)
    out = {}
    for k, f in d.items():
        try: out[k] = len(f())
        except Exception as e: out[k] = -1
    return out


def mutantes(plan, checks):
    linhas = plan.splitlines()
    reg = n.regiao_codigos(plan)
    cod = next(c for c in sorted(set(re.findall(r"\bWRV_[A-Z0-9_]+", plan))) if 3 <= plan.count(c) <= 8
               and sum(c in ln for _, ln in reg) == 1)
    iDef = next(i - 1 for i, ln in reg if cod in ln)
    num = re.search(r"\b1\.583\b|\b1\.5\d\d\b", plan)
    m = {}
    m["M1 apaga a linha-definição de um código (usado sem definição)"] = ("\n".join(linhas[:iDef] + linhas[iDef + 1:]), checks, None)
    # M2: um uso do código passa a ter grafia divergente (typo) — o código "novo" não está na tabela
    k = next(i for i, l in enumerate(linhas) if cod in l and i != iDef and not l.lstrip().startswith("|"))
    mut = linhas[:]; mut[k] = mut[k].replace(cod, cod[:-1] + "Z", 1)
    m["M2 um uso do código com grafia divergente"] = ("\n".join(mut), checks, None)
    m["M3 nova recusa fail-closed em EARS sem código"] = (plan + "\n- Quando o registro de capacidades divergir, o compilador DEVE recusar a página (fail-closed).\n", checks, None)
    base = plan
    mp = plan.replace(num.group(0), "9.999", 1) if num else plan
    m["M4 troca um número em 1 local (propagação parcial)"] = (mp, checks, base)
    m["M5 ✔ novo em checks.md citando ID da Spec que não existe"] = (plan, checks + "\n| **F99** Recusa sem código | RULE-WRV-999 | ✔ |\n", None)
    m["M6 ✔ novo em checks.md sem evidência nenhuma (sem ID)"] = (plan, checks + "\n| **F98** Recusa sem código | por leitura | ✔ |\n", None)
    return m


def main():
    sd = Path(sys.argv[1] if len(sys.argv) > 1 else "specs/features/SPEC-049")
    plan = (ROOT / sd / "plan.md").read_text(encoding="utf-8"); checks = (ROOT / sd / "checks.md").read_text(encoding="utf-8")
    irmaos = {f: (ROOT / sd / f).read_text(encoding="utf-8") for f in ("checks.md", "research.md", "ABERTURA.md") if (ROOT / sd / f).exists()}
    orig = todos(plan, checks, plan, irmaos)
    print("FALSOS ALARMES no original baselined (achados por detector):"); [print(f"  {k:<26}{v}") for k, v in orig.items()]
    print("\nMUTAÇÃO (detectores que ACHAM algo a mais que o original):")
    for nome, (p, c, base) in mutantes(plan, checks).items():
        res = todos(p, c, base, irmaos)
        pegou = [k for k, v in res.items() if v > orig[k]]
        print(f"  {'PEGOU ' if pegou else 'ESCAPOU'} {nome}  -> {pegou or '-'}")


if __name__ == "__main__":
    main()
