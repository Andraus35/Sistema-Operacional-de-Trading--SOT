"""Testes do detector de ramos órfãos (scripts/check_branches.py) — informativo."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_branches as c  # noqa: E402


class Ramos(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.g("init", "-q", "-b", "main")
        self.g("config", "user.email", "t@t")
        self.g("config", "user.name", "t")
        self.commit("m0")

    def tearDown(self):
        self.tmp.cleanup()

    def g(self, *a):
        subprocess.run(["git", *a], cwd=self.root, check=True, capture_output=True)

    def commit(self, msg):
        (self.root / f"{msg}.txt").write_text(msg, encoding="utf-8")
        self.g("add", ".")
        self.g("commit", "-qm", msg)

    def ref(self, nome, sha="HEAD"):
        self.g("update-ref", f"refs/remotes/origin/{nome}", sha)

    def test_sem_origin_main_so_avisa(self):
        achados, aviso = c.analisar(self.root, "")
        self.assertEqual(achados, [])
        self.assertIn("indisponível", aviso)

    def test_contido_e_orfao_e_citado(self):
        self.ref("main")
        self.ref("contido")
        self.g("checkout", "-q", "-b", "frente")
        self.commit("f1")
        self.ref("orfao", "HEAD")
        self.ref("citado", "HEAD")
        self.g("checkout", "-q", "main")
        achados, aviso = c.analisar(self.root, "ramo citado em andamento")
        self.assertIsNone(aviso)
        ids = {(n, i, m.split(" ")[0]) for n, i, m in achados}
        self.assertIn(("INFO", "BR-02", "contido"), ids)
        self.assertIn(("WARN", "BR-01", "orfao"), ids)
        self.assertNotIn(("WARN", "BR-01", "citado"), ids)

    def test_ramo_atual_e_main_ignorados(self):
        self.ref("main")
        self.g("checkout", "-q", "-b", "atual")
        self.commit("a1")
        self.ref("atual", "HEAD")
        achados, _ = c.analisar(self.root, "")
        self.assertEqual(achados, [])


if __name__ == "__main__":
    unittest.main()
