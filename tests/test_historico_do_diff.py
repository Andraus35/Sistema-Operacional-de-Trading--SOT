"""Testes do historico_do_diff.py (proposta P14(b)) — python -m unittest tests/test_historico_do_diff.py"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "historico_do_diff.py"
sys.path.insert(0, str(SCRIPT.parent))
import historico_do_diff as h  # noqa: E402

V1 = "# T\n## D2\nRULE-X-001: a regra v1 diz A.\ncontinua.\nRULE-X-002: outra.\n## D3\nfim igual.\n"
V2 = "# T\n## D2\nRULE-X-001: a regra v2 diz B.\ncontinua.\nRULE-X-002: outra.\n## D3\nfim igual.\n"


class TestHist(unittest.TestCase):
    def test_troca_tem_texto_anterior_e_ancora(self):
        ts = h.trechos(V1, V2)
        self.assertEqual(len(ts), 1)
        self.assertEqual(ts[0]["local"], "RULE-X-001")
        self.assertIn("v1 diz A", ts[0]["anterior"])
        self.assertIn("v2 diz B", ts[0]["novo"])

    def test_remocao(self):
        ts = h.trechos(V1, V1.replace("continua.\n", ""))
        self.assertEqual(ts[0]["novo"], "(removido)")
        self.assertIn("continua.", ts[0]["anterior"])

    def test_sem_mudanca_sem_trechos(self):
        self.assertEqual(h.trechos(V1, V1), [])

    def test_so_adicao_nao_gera_linha(self):  # nada anterior a preservar
        self.assertEqual(h.trechos(V1, V1 + "nova linha\n"), [])

    def test_trunca_e_marca(self):
        ts = h.trechos("## A\n" + "x" * 900 + "\n", "## A\ny\n", mx=100)
        self.assertIn("truncado", ts[0]["anterior"])
        self.assertNotIn("truncado", h.trechos("## A\n" + "x" * 900 + "\n", "## A\ny\n", mx=0)[0]["anterior"])

    def test_pipe_escapado(self):
        ts = h.trechos("## A\na | b\n", "## A\nc\n")
        self.assertIn("a \\| b", ts[0]["anterior"])

    def test_cli_com_arquivo_base(self):
        d = Path(tempfile.mkdtemp())
        (d / "v1.md").write_text(V1, encoding="utf-8")
        (d / "plan.md").write_text(V2, encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), str(d / "plan.md"), "--base", str(d / "v1.md"), "--out", str(d / "o.md")],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0)
        self.assertIn("(preencher)", (d / "o.md").read_text(encoding="utf-8"))
        self.assertIn("1 trecho", r.stdout)

    def test_base_ilegivel_falha(self):
        d = Path(tempfile.mkdtemp())
        (d / "plan.md").write_text(V2, encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), str(d / "plan.md"), "--base", "ref-que-nao-existe-xyz"],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
