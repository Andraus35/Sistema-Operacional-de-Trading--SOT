"""Testes do novo_handoff.py (proposta) — python -m unittest test_novo_handoff (nesta pasta)."""
import shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "novo_handoff.py"
H = ("---\nhandoff_id: HO-2026-11-01-157\nprevious: HO-2026-11-01-156\ndata: 2026-11-01\nbranch: x\nbase_commit: aaaaaaa\n---\n"
     "# HANDOFF\n## 1. Frente\nTexto ANTIGO unico.\nrepetido\nrepetido\n")


class T(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        (self.d / "HANDOFF.md").write_text(H, encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def run_(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.d), "--base", "bbbbbbb", "--data", "2026-11-02", *args],
                              capture_output=True, text=True)

    def test_troca_id_previous_data_base_e_arquiva_copia_exata(self):
        r = self.run_()
        self.assertEqual(r.returncode, 0, r.stderr)
        n = (self.d / "HANDOFF.md").read_text(encoding="utf-8")
        self.assertIn("handoff_id: HO-2026-11-02-158", n)
        self.assertIn("previous: HO-2026-11-01-157", n)
        self.assertIn("data: 2026-11-02", n)
        self.assertIn("base_commit: bbbbbbb", n)
        self.assertEqual((self.d / "docs/handoffs/HO-2026-11-01-157.md").read_text(encoding="utf-8"), H)

    def test_ancora_ausente_falha_alto_e_nao_escreve_nada(self):
        r = self.run_("--trocar", "NAO EXISTE=>x")
        self.assertEqual(r.returncode, 2)
        self.assertIn("0x", r.stderr)
        self.assertEqual((self.d / "HANDOFF.md").read_text(encoding="utf-8"), H)
        self.assertFalse((self.d / "docs").exists())

    def test_ancora_repetida_falha_alto(self):
        r = self.run_("--trocar", "repetido=>x")
        self.assertEqual(r.returncode, 2)
        self.assertIn("2x", r.stderr)
        self.assertEqual((self.d / "HANDOFF.md").read_text(encoding="utf-8"), H)

    def test_troca_de_texto_unica_aplica(self):
        r = self.run_("--trocar", "ANTIGO unico=>NOVO unico")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("NOVO unico", (self.d / "HANDOFF.md").read_text(encoding="utf-8"))

    def test_copia_existente_divergente_recusa_e_nao_escreve(self):
        p = self.d / "docs/handoffs/HO-2026-11-01-157.md"
        p.parent.mkdir(parents=True)
        p.write_text("OUTRA CADEIA", encoding="utf-8")
        r = self.run_()
        self.assertEqual(r.returncode, 2)
        self.assertEqual((self.d / "HANDOFF.md").read_text(encoding="utf-8"), H)
        self.assertEqual(p.read_text(encoding="utf-8"), "OUTRA CADEIA")

    def test_ramo_manda_a_copia_para_a_pasta_do_ramo(self):
        p = self.d / "docs/handoffs/HO-2026-11-01-157.md"
        p.parent.mkdir(parents=True)
        p.write_text("OUTRA CADEIA", encoding="utf-8")
        r = self.run_("--ramo", "meu-ramo")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual((self.d / "docs/handoffs/ramo-meu-ramo/HO-2026-11-01-157.md").read_text(encoding="utf-8"), H)
        self.assertEqual(p.read_text(encoding="utf-8"), "OUTRA CADEIA")

    def test_sem_frontmatter_ou_id_invalido_recusa(self):
        (self.d / "HANDOFF.md").write_text("# sem frontmatter\n", encoding="utf-8")
        self.assertEqual(self.run_().returncode, 2)
        (self.d / "HANDOFF.md").write_text("---\nhandoff_id: XYZ\n---\n", encoding="utf-8")
        self.assertEqual(self.run_().returncode, 2)

    def test_numero_preserva_largura(self):
        (self.d / "HANDOFF.md").write_text(H.replace("157", "099"), encoding="utf-8")
        self.assertEqual(self.run_().returncode, 0)
        self.assertIn("handoff_id: HO-2026-11-02-100", (self.d / "HANDOFF.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
