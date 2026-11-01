#!/usr/bin/env python3
"""pre_entrega.py — pré-gate unificado antes do Revisor (PROPOSTA; não instalado; ver PROPOSTA-PRE-ENTREGA-2026-11-01.md).

Só COMPÕE scripts já selados (nenhuma lógica nova de detecção). Roda pelo Orquestrador/hook — o Especificador não tem Bash.
Saída: pre-entrega.json com sha256 de plan.md/checks.md e, por verificação: tipo (bloqueante|informativo), status, achados.
Bloqueante = o que já é bloqueante no CI (validate_spec_sot, check_repo_research, build_map --check). Detectores = informativos
até Andraus promover (ENF-03). exit 0 ≠ CONFORME ≠ homologação. Somente leitura (escreve só o --out).

Uso: python pre_entrega.py specs/features/SPEC-nnn [--root REPO] [--out pre-entrega.json]
"""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest() if Path(p).exists() else None


def cli(root, nome, tipo, cmd, achados_de=None):
    p = subprocess.run(cmd, cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": __import__("os").environ.get("PATH", "")})
    out = (p.stdout or "") + (p.stderr or "")
    r = {"id": nome, "tipo": tipo, "exit": p.returncode, "status": "OK" if p.returncode == 0 else "RED",
         "output_sha256": hashlib.sha256(out.encode()).hexdigest(), "cauda": out.strip().splitlines()[-3:]}
    return r


def detectores(root, plan_t, checks_t):
    sys.path.insert(0, str(Path(root) / "scripts"))
    import gate_extra as g, revisor_detectores as d
    R = Path(root)
    lote = [("gate_extra.citacoes_arquivo_linha", lambda: g.citacoes_arquivo_linha(plan_t, R)),
            ("gate_extra.contagens_declaradas", lambda: g.contagens_declaradas(plan_t)),
            ("gate_extra.piso_enforcement", lambda: g.piso_enforcement(plan_t)),
            ("gate_extra.decisoes_abertas_fechadas", lambda: g.decisoes_abertas_fechadas(plan_t)),
            ("gate_extra.invariantes_estritos", lambda: g.invariantes_estritos(plan_t)),
            ("gate_extra.assertivas_checks", lambda: g.assertivas_checks(checks_t, plan_t)),
            ("gate_extra.corrigidos_sem_assertiva", lambda: g.corrigidos_sem_assertiva(checks_t)),
            ("revisor_detectores.mapeamento_conflitante", lambda: d.mapeamento_conflitante(plan_t)),
            ("revisor_detectores.id_norma_inexistente", lambda: d.id_norma_inexistente(plan_t, R)),
            ("revisor_detectores.contagem_declarada", lambda: d.contagem_declarada(plan_t)),
            ("revisor_detectores.spec_nome_incoerente", lambda: d.spec_nome_incoerente(plan_t, R)),
            ("revisor_detectores.valor_fonte", lambda: d.valor_fonte(plan_t, R)),
            ("revisor_detectores.dhr_backlog", lambda: d.dhr_backlog(plan_t, R))]
    res = []
    for nome, fn in lote:
        try:
            ach = fn()
            res.append({"id": nome, "tipo": "informativo", "status": "ACHADOS" if ach else "OK",
                        "n_achados": len(ach), "achados": [str(a)[:200] for a in ach[:10]]})
        except Exception as e:  # detector que quebra não pode passar por limpo
            res.append({"id": nome, "tipo": "informativo", "status": "ERRO_DO_DETECTOR", "n_achados": None, "achados": [repr(e)[:200]]})
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("spec_dir"); ap.add_argument("--root", default="."); ap.add_argument("--out", default="pre-entrega.json")
    a = ap.parse_args(argv); root = Path(a.root).resolve(); sd = Path(a.spec_dir)
    plan, checks = root / sd / "plan.md", root / sd / "checks.md"
    if not plan.exists():
        print(f"FAIL: {plan} ausente"); return 2
    py = sys.executable; rel = str(sd).replace("\\", "/")
    v = [cli(root, "validate_spec_sot", "bloqueante", [py, "scripts/validate_spec_sot.py", f"{rel}/plan.md"]),
         cli(root, "check_repo_research", "bloqueante", [py, "scripts/check_repo_research.py", rel]),
         cli(root, "build_map_check", "bloqueante", [py, "scripts/build_map.py", "--check"]),
         cli(root, "check_invariants", "informativo", [py, "scripts/check_invariants.py", f"{rel}/plan.md"]),
         cli(root, "check_dimensionamento", "informativo", [py, "scripts/check_dimensionamento.py"]),
         cli(root, "check_refs", "informativo", [py, "scripts/check_refs.py"]),
         cli(root, "backlog_triggers", "informativo", [py, "scripts/backlog_triggers.py"])]
    v += detectores(root, plan.read_text(encoding="utf-8"), checks.read_text(encoding="utf-8") if checks.exists() else "")
    bloq = [x for x in v if x["tipo"] == "bloqueante" and x["status"] != "OK"]
    ev = {"schema_version": "1.0", "spec_dir": rel, "plan_sha256": sha(plan), "checks_sha256": sha(checks),
          "verificacoes": v, "bloqueantes_vermelhos": [x["id"] for x in bloq],
          "informativos_com_achado": [x["id"] for x in v if x["tipo"] == "informativo" and x["status"] in ("ACHADOS", "RED", "ERRO_DO_DETECTOR")],
          "nota": "exit 0 ≠ CONFORME ≠ homologação (ENF-03). Detectores informativos até ordem de Andraus."}
    Path(a.out).write_text(json.dumps(ev, ensure_ascii=False, indent=2), encoding="utf-8")
    for x in v: print(f"{x['status']:<17} {x['tipo']:<11} {x['id']}")
    print(f"plan_sha256={ev['plan_sha256'][:12]}  bloqueantes vermelhos: {len(bloq)}")
    return 1 if bloq else 0


if __name__ == "__main__":
    sys.exit(main())
