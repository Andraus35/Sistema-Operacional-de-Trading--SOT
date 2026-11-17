"""Testes do ancora_hash.py (proposta P14(a)) — python -m unittest tests/test_ancora_hash.py"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "ancora_hash.py"
sys.path.insert(0, str(SCRIPT.parent))
import ancora_hash as ah  # noqa: E402

PLAN = "# T\n## D2\nRULE-X-001: regra v1 diz A.\n\nRULE-X-002: outra regra.\n## D3\n### BASpec-X-001 — comp\ntexto do BASpec\n### ADV-X-01 — adv\nadv texto\n"


class TestAncora(unittest.TestCase):
    def test_hash_estavel_e_4_hex(self):
        h = ah.hashes(PLAN)
        for k in ("RULE-X-001", "RULE-X-002", "BASpec-X-001", "ADV-X-01"):
            self.assertRegex(h[k], r"^[0-9a-f]{4}$")
        self.assertEqual(h, ah.hashes(PLAN))

    def test_hash_nao_depende_de_posicao(self):  # a razão de ser: linhas mudam, âncora não
        deslocado = "linha nova no topo\n\n" + PLAN
        self.assertEqual(ah.hashes(PLAN)["RULE-X-002"], ah.hashes(deslocado)["RULE-X-002"])

    def test_hash_muda_quando_o_texto_muda(self):  # mutante: hash que ignora o conteúdo
        novo = PLAN.replace("regra v1 diz A", "regra v2 diz B")
        self.assertNotEqual(ah.hashes(PLAN)["RULE-X-001"], ah.hashes(novo)["RULE-X-001"])
        self.assertEqual(ah.hashes(PLAN)["RULE-X-002"], ah.hashes(novo)["RULE-X-002"])

    def test_conferir_ok_defasada_inexistente(self):
        h = ah.hashes(PLAN)
        doc = f"cita RULE-X-001#{h['RULE-X-001']} e RULE-X-002#ffff e RULE-Z-009#abcd e BASpec-X-001#{h['BASpec-X-001']}\n"
        r = {x["id"]: x["estado"] for x in ah.conferir(doc, PLAN)}
        self.assertEqual(r, {"RULE-X-001": "OK", "RULE-X-002": "DEFASADA", "RULE-Z-009": "INEXISTENTE", "BASpec-X-001": "OK"})

    def test_texto_sem_ancora_nao_gera_nada(self):
        self.assertEqual(ah.conferir("cita RULE-X-001 sem hash, e #abcd solto\n", PLAN), [])

    def test_cli(self):
        d = Path(tempfile.mkdtemp())
        (d / "plan.md").write_text(PLAN, encoding="utf-8")
        h = ah.hashes(PLAN)["RULE-X-001"]
        (d / "doc.md").write_text(f"ver RULE-X-001#{h}\n", encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), "hash", str(d / "plan.md"), "RULE-X-001"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.stdout.strip(), f"RULE-X-001#{h}")
        r = subprocess.run([sys.executable, str(SCRIPT), "conferir", str(d / "doc.md"), str(d / "plan.md"), "--strict"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0)
        (d / "doc.md").write_text("ver RULE-X-001#0000\n", encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), "conferir", str(d / "doc.md"), str(d / "plan.md"), "--strict"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 1)
        self.assertIn("DEFASADA", r.stdout)

    def test_id_inexistente_no_hash_falha(self):
        d = Path(tempfile.mkdtemp())
        (d / "plan.md").write_text(PLAN, encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), "hash", str(d / "plan.md"), "RULE-Q-1"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()
