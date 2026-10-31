import subprocess, sys, tempfile, unittest
from pathlib import Path
SC = Path(__file__).parent / "equiv_conservacao.py"

def run(orig, enx, mor):
    d = Path(tempfile.mkdtemp())
    for n, t in (("o.md", orig), ("e.md", enx), ("m.md", mor)):
        (d / n).write_text(t, encoding="utf-8")
    r = subprocess.run([sys.executable, str(SC), d / "o.md", d / "e.md", d / "m.md"], capture_output=True, text=True)
    return r.returncode, r.stdout

ORIG = "# T\nR:R mínimo 1:3 sem exceção.\nConvicção >= 70% e score >= 7/9.\n| a | b |\n"

class T(unittest.TestCase):
    def test_mover_para_morto_conserva(self):
        self.assertEqual(run(ORIG, "# T\nver arquivo morto\n| a | b |\n", "R:R mínimo 1:3 sem exceção.\nConvicção >= 70% e score >= 7/9.\n")[0], 0)
    def test_espacos_e_crlf_nao_contam(self):
        self.assertEqual(run(ORIG, "# T\r\nR:R   mínimo 1:3 sem exceção.\r\nConvicção >= 70% e score >= 7/9.\r\n| a | b |\r\n", "")[0], 0)
    def test_linha_apagada_reprova(self):
        c, o = run(ORIG, "# T\n| a | b |\n", "R:R mínimo 1:3 sem exceção.\n")
        self.assertEqual(c, 1); self.assertIn("score", o)
    def test_valor_alterado_reprova_e_aponta_parecida(self):
        c, o = run(ORIG, "# T\nR:R mínimo 1:2 sem exceção.\nConvicção >= 70% e score >= 7/9.\n| a | b |\n", "")
        self.assertEqual(c, 1); self.assertIn("parecida", o); self.assertIn("1:2", o)
    def test_linha_duplicada_exige_duas_copias(self):
        self.assertEqual(run("x\nx\n", "x\n", "")[0], 1)
        self.assertEqual(run("x\nx\n", "x\n", "x\n")[0], 0)
    def test_linhas_novas_sao_permitidas(self):
        self.assertEqual(run("x\n", "x\nponteiro novo\n", "")[0], 0)
    def test_celula_longa_truncada_reprova(self):
        longa = "| " + "a" * 5000 + " |\n"
        self.assertEqual(run(longa, "| " + "a" * 100 + " |\n", "")[0], 1)
        self.assertEqual(run(longa, "| resumo |\n", longa)[0], 0)
    def test_arquivo_vazio_nao_conserva_nada(self):
        self.assertEqual(run(ORIG, "", "")[0], 1)

if __name__ == "__main__":
    unittest.main()
