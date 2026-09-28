"""Testes do backlog_triggers.py (BL-006) — python -m unittest tests/test_backlog_triggers.py"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "backlog_triggers.py"

HEAD = "| ID | Título | Tipo | Afeta | Gatilho | Ação | Estado | Origem |\n|---|---|---|---|---|---|---|---|\n"


def row(bl, gatilho, estado="Em espera"):
    return f"| **{bl}** | Titulo {bl} | Ideia | Proc | {gatilho} | Acao | {estado} | src |\n"


ROADMAP = (
    "| SPEC-001 — Hypothesis | **HOMOLOGADA — BASELINE** (Andraus) |\n"
    "| Decisões FECHADAS | B-001 (x) · **L-001 — FECHADA (y; runtime → SPEC-018/K-001)** |\n"
)


class Trig(unittest.TestCase):
    def report(self, rows, roadmap=ROADMAP, extra=None, *args):
        d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        (d / "backlog").mkdir()
        (d / "backlog" / "RMR-001_Painel_Backlog.md").write_text(HEAD + rows, encoding="utf-8")
        (d / "ROADMAP.md").write_text(roadmap, encoding="utf-8")
        for name, body in (extra or {}).items():
            p = d / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), "--root", str(d), "--json", *args],
                           capture_output=True, text=True, encoding="utf-8")
        return r.returncode, json.loads(r.stdout) if r.stdout.strip().startswith("{") else r.stdout

    def ids(self, rep, key):
        return [i["id"] if isinstance(i, dict) else i for i in rep[key]]

    def test_spec_homologada_dispara_e_reprova(self):
        code, rep = self.report(row("BL-001", "`spec:SPEC-001 homologada`"))
        self.assertEqual(code, 1)
        self.assertEqual(self.ids(rep, "disparados_sem_registro"), ["BL-001"])

    def test_spec_nao_homologada_aguarda(self):
        code, rep = self.report(row("BL-001", "`spec:SPEC-002 homologada`"))
        self.assertEqual(code, 0)
        self.assertEqual(self.ids(rep, "aguardando"), ["BL-001"])

    def test_em_redacao_por_diretorio_de_feature(self):
        code, rep = self.report(row("BL-001", "`spec:SPEC-004 em redação`"),
                                extra={"specs/features/SPEC-004/plan.md": "Status: rascunho\n"})
        self.assertEqual(code, 1)

    def test_faixa_de_specs(self):
        code, rep = self.report(row("BL-001", "`spec:SPEC-010..014 em redação`"),
                                extra={"specs/features/SPEC-012/plan.md": "x"})
        self.assertEqual(self.ids(rep, "disparados_sem_registro"), ["BL-001"])

    def test_decisao_fechada_no_roadmap(self):
        _, rep = self.report(row("BL-001", "`decisao:L-001 resolvida`"))
        self.assertEqual(self.ids(rep, "disparados_sem_registro"), ["BL-001"])

    def test_id_citado_como_referencia_no_roadmap_nao_e_fechado(self):
        _, rep = self.report(row("BL-001", "`decisao:K-001 resolvida`"))
        self.assertEqual(self.ids(rep, "aguardando"), ["BL-001"])

    def test_eua_homologada_por_ata(self):
        _, rep = self.report(row("BL-001", "`spec:EUA-E19a homologada`"),
                             extra={"governance/DHR-EUA-E19a_ata.md": "x"})
        self.assertEqual(self.ids(rep, "disparados_sem_registro"), ["BL-001"])

    def test_and_com_condicao_manual_nao_dispara(self):
        code, rep = self.report(row("BL-001", "`spec:SPEC-001 homologada` ∧ `milestone:FASE 6 concluída`"))
        self.assertEqual(code, 0)
        self.assertEqual(self.ids(rep, "manual"), ["BL-001"])

    def test_or_verdadeiro_prevalece_sobre_manual(self):
        code, rep = self.report(row("BL-001", "`spec:SPEC-001 homologada` ∨ `evento:algo`"))
        self.assertEqual(code, 1)

    def test_and_com_falso_e_manual_e_falso(self):
        _, rep = self.report(row("BL-001", "`spec:SPEC-002 homologada` ∧ `evento:algo`"))
        self.assertEqual(self.ids(rep, "aguardando"), ["BL-001"])

    def test_evento_e_sempre_manual(self):
        code, rep = self.report(row("BL-001", "`evento:qualquer coisa`") + row("BL-002", "`hygiene:próximo ciclo`"))
        self.assertEqual(code, 0)
        self.assertEqual(sorted(self.ids(rep, "manual")), ["BL-001", "BL-002"])

    def test_ativado_listado_e_strict_falha(self):
        rows = row("BL-001", "`evento:x`", "**ATIVADO** (Andraus)")
        code, rep = self.report(rows)
        self.assertEqual(code, 0)
        self.assertEqual(self.ids(rep, "ativados"), ["BL-001"])
        code, _ = self.report(rows, ROADMAP, None, "--strict")
        self.assertEqual(code, 1)

    def test_encerrados_ignorados(self):
        code, rep = self.report(row("BL-001", "`spec:SPEC-001 homologada`", "**Absorvido** (x)"))
        self.assertEqual(code, 0)
        self.assertEqual(self.ids(rep, "encerrados"), ["BL-001"])

    def test_diferido_tratado_como_espera(self):
        code, _ = self.report(row("BL-001", "`spec:SPEC-001 homologada`", "**Diferido para SPEC-018**"))
        self.assertEqual(code, 1)

    def test_sem_rmr_exit_2(self):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        r = subprocess.run([sys.executable, str(SCRIPT), "--root", d], capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)


if __name__ == "__main__":
    unittest.main()
