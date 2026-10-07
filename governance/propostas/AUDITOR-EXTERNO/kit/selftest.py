#!/usr/bin/env python3
"""selftest.py — calibração do kit com DEFEITOS PLANTADOS (known-answer test).

[PROPOSTA — NÃO HOMOLOGADO] Gera achados sintéticos no HEAD do clone e confirma que o validador PASSA o
válido e REPROVA cada defeito plantado com o código esperado. Rode após instalar: se falhar, NÃO audite.
Uso: python selftest.py --repo <clone>
"""
import argparse, copy, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", required=True); a = ap.parse_args()
    head = subprocess.run(["git", "-C", a.repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    # âncora real e estável: primeira linha longa de AGENTS.md
    lines = subprocess.run(["git", "-C", a.repo, "show", f"{head}:AGENTS.md"], capture_output=True, text=True).stdout.split("\n")
    n = next(i for i, l in enumerate(lines, 1) if len(l.strip()) >= 40)
    dtxt = subprocess.run(["git", "-C", a.repo, "show", f"{head}:governance/propostas/AUDITOR-EXTERNO/DIRETIVAS-AO-AUDITOR.md"],
                          capture_output=True, text=True).stdout
    vig = re.findall(r"^## (DIR-\d{3})\s*\n+Status:\s*VIGENTE", dtxt, re.M)[-1]
    base = {"schema_version": "1.0", "id": "AEX-20260101-001", "severity": "P2", "type": "drift", "rule_source": "INV-09", "impact": "sintético", "what_does_not_change": "tudo",
            "title": "achado sintético de calibração", "claim": "Teste de calibração do validador.",
            "baseline_commit": head, "directive_version": vig,
            "evidence": [{"path": "AGENTS.md", "line_start": n, "line_end": n, "quote": lines[n - 1].strip()[:60]}],
            "proposal": {"type": "NOTA", "text": "Sem mudança.", "modifies_baselined_text": False, "touches": []},
            "open_decisions_referenced": [], "treats_open_decision_as_closed": False,
            "status_sip": {"specified": True, "implemented": False, "proven": False},
            "reproduce": [f"git show {head[:8]}:AGENTS.md"], "author": {"model": "selftest", "date": "2026-01-01"}}
    def ed(f): d = copy.deepcopy(base); f(d); return d
    # (o ID inventado do caso PN2 é montado em runtime: o texto inteiro nunca aparece literal no repositório)
    casos = [("VÁLIDO", base, 0, None),
             ("citação inventada", ed(lambda d: d["evidence"][0].update(quote="texto que não existe no arquivo em lugar nenhum")), 1, "E-QUOTE"),
             ("sem evidência", ed(lambda d: d.update(evidence=[])), 1, "E-EVID"),
             ("baseline errado", ed(lambda d: d.update(baseline_commit="0" * 40)), 1, "E-BASELINE"),
             ("edição direta de texto baselined", ed(lambda d: d["proposal"].update(type="NOTA", modifies_baselined_text=True)), 1, "E-INV09"),
             ("toca canon/", ed(lambda d: d["proposal"].update(touches=["canon/CHM-001-canonical-hypothesis-model.md"])), 1, "E-CONST01"),
             ("decisão aberta tratada como fechada", ed(lambda d: d.update(treats_open_decision_as_closed=True)), 1, "E-CONS01"),
             ("comando de reprodução com escrita", ed(lambda d: d.update(reproduce=["rm -rf x"])), 1, "E-REPRO"),
             ("diretiva de postura não vigente", ed(lambda d: d.update(directive_version="DIR-999")), 1, "E-DIRETIVA"),
             ("implementado sem evidência de gate", ed(lambda d: d["status_sip"].update(implemented=True)), 1, "E-SIP"),
             ("regra inventada em rule_source (PN2)", ed(lambda d: d.update(rule_source="RULE-" + "INEXISTENTE" + "-" + "00")), 1, "E-RULESRC"),
             ("rule_source em texto livre, sem ID (liberdade cognitiva)", ed(lambda d: d.update(rule_source="princípio de coerência entre nota e achados")), 0, None)]
    ok = True
    for nome, d, esperado, cod in casos:
        p = os.path.join(tempfile.mkdtemp(), "f.json"); json.dump(d, open(p, "w"))
        r = subprocess.run([sys.executable, os.path.join(HERE, "validate_finding.py"), "--repo", a.repo, "--finding", p],
                           capture_output=True, text=True)
        bom = r.returncode == esperado and (cod is None or cod in r.stdout)
        ok &= bom; print(("OK  " if bom else "ERRO"), nome, f"(exit {r.returncode}, esperado {esperado}{', '+cod if cod else ''})")
    print("CALIBRAÇÃO " + ("APROVADA" if ok else "REPROVADA — não audite com este kit")); return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
