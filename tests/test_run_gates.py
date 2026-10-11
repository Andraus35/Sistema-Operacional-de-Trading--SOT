"""Testes do runner de gates que gera o evidence.json para o Revisor (scripts/run_gates.py) — DHR-AUDITOR-EXTERNO-008 R1."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNNER = ROOT / "scripts" / "run_gates.py"


def git(repo, *a):
    return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True)


def novo_repo(d):
    git(d, "init", "-q")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    (Path(d) / "a.txt").write_text("x")
    git(d, "add", ".")
    git(d, "commit", "-q", "-m", "c")


class TestRunGates(unittest.TestCase):
    def test_arvore_suja_falha(self):
        with tempfile.TemporaryDirectory() as d:
            novo_repo(d)
            (Path(d) / "sujo.txt").write_text("y")
            r = subprocess.run([sys.executable, str(RUNNER), "--repo", d, "--out", str(Path(d) / "e.json")], capture_output=True, text=True)
            self.assertEqual(r.returncode, 2)
            self.assertIn("suja", r.stdout)

    def test_gera_evidence_e_registra_arquivos_sem_gate(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as o:
            novo_repo(d)
            out = Path(o) / "evidence.json"
            r = subprocess.run([sys.executable, str(RUNNER), "--repo", d, "--out", str(out), "--files", "doc.md"], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            ev = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(ev["schema_version"], "1.0")
            self.assertEqual(ev["arquivos_sem_gate_de_estrutura"], ["doc.md"])
            nomes = {g["name"] for g in ev["gates"]}
            self.assertIn("check_invariants", nomes)
            self.assertTrue(all("output_sha256" in g and "exit_code" in g for g in ev["gates"]))

    def test_check_invariants_e_informativo(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import run_gates
        self.assertIn("check_invariants", run_gates.INFORMATIVOS)


if __name__ == "__main__":
    unittest.main()
