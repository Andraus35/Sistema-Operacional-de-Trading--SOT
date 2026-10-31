import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import delta_pacote as D  # noqa: E402

BASE = "## A\ntexto a\n\n## B\ntexto b\n"
NOVO = "## A\ntexto a\n\n## B\ntexto b alterado\n\n## C\nnovo\n"


class TestDeltaPacote(unittest.TestCase):
    def test_grava_arquivo_e_devolve_linhas_do_prompt_com_sha256_correto(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            (t / "plan.md").write_text(NOVO, encoding="utf-8")
            (t / "base.md").write_text(BASE, encoding="utf-8")
            arq, texto, prompt = D.montar(str(t / "plan.md"), str(t / "base.md"), t / "out")
            self.assertTrue(arq.is_file())
            esperado = hashlib.sha256(NOVO.encode("utf-8")).hexdigest()
            self.assertIn(f"SHA256-ALVO: {esperado}", prompt)
            self.assertIn(f"SHA256-ALVO: {esperado}", texto)
            self.assertTrue(any(l.startswith("ALVO: ") for l in prompt))
            self.assertTrue(any(l.startswith("BASE: ") for l in prompt))
            self.assertTrue(any(l.startswith("DELTA: ") for l in prompt))

    def test_delta_lista_alterado_e_adicionado(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            (t / "plan.md").write_text(NOVO, encoding="utf-8")
            (t / "base.md").write_text(BASE, encoding="utf-8")
            _, texto, _ = D.montar(str(t / "plan.md"), str(t / "base.md"), t / "o")
            self.assertIn("1 alterados", texto)
            self.assertIn("1 adicionados", texto)
            self.assertIn("1 inalterados", texto)

    def test_hash_muda_quando_o_alvo_muda(self):
        self.assertNotEqual(D.sha(BASE), D.sha(NOVO))


if __name__ == "__main__":
    unittest.main()
