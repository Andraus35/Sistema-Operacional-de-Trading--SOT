import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import aplicar_ficha_m as A  # noqa: E402

BASE = "linha um\nBASpec-X VERIFICADO POR: T01\nlinha tres\nlinha tres repetida\nlinha tres repetida\n"


def ach(id_, antigo, novo, sev="MENOR", **k):
    d = {"id": id_, "sev": sev, "arquivo": "plan.md", "antigo": antigo, "novo": novo, "condicao": "grep novo"}
    d.update(k)
    return d


class AplicarFichaM(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "plan.md").write_text(BASE, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def txt(self):
        return (self.root / "plan.md").read_text(encoding="utf-8")

    def test_aplica_menor_mecanico_por_texto_e_nao_por_linha(self):
        rel, ok, _ = A.aplicar([ach("n-01", "BASpec-X VERIFICADO POR: T01", "BASpec-X VERIFICADO POR: T01; ADV-04(c)", linha=999)], self.root)
        self.assertEqual(rel["aplicados"], ["n-01"])
        self.assertEqual(rel["escalados"], [])
        self.assertIn("T01; ADV-04(c)", self.txt())
        self.assertEqual(len(self.txt().splitlines()), 5)

    def test_media_nunca_e_corrigida(self):
        rel, _, _ = A.aplicar([ach("M-01", "linha um", "linha UM", sev="MEDIA")], self.root)
        self.assertEqual(rel["aplicados"], [])
        self.assertIn("severidade", rel["escalados"][0]["motivo"])
        self.assertEqual(self.txt(), BASE)

    def test_texto_nao_unico_ou_inexistente_escala(self):
        rel, _, _ = A.aplicar([ach("n-02", "linha tres repetida", "linha tres REPETIDA"), ach("n-03", "nao existe", "x")], self.root)
        self.assertEqual({e["id"] for e in rel["escalados"]}, {"n-02", "n-03"})
        self.assertEqual(self.txt(), BASE)

    def test_nao_cria_id_normativo_nem_muda_numero_de_linhas(self):
        rel, _, _ = A.aplicar([ach("n-04", "linha um", "linha um RULE-NOVA-99"), ach("n-05", "linha um", "linha um\nlinha extra")], self.root)
        self.assertEqual({e["id"] for e in rel["escalados"]}, {"n-04", "n-05"})
        self.assertEqual(self.txt(), BASE)

    def test_id_ja_presente_no_arquivo_nao_escala(self):
        """DHR-ROTEAMENTO-007: ID que o arquivo já contém não é 'novo' (antes escalava por engano)."""
        (self.root / "plan.md").write_text(BASE + "ref DHR-ZZ-001 aqui\n", encoding="utf-8")
        rel, _, _ = A.aplicar([ach("n-08", "linha um", "linha um (DHR-ZZ-001)")], self.root)
        self.assertEqual(rel["aplicados"], ["n-08"])

    def test_teto_do_lote_escala_o_excedente(self):
        texto = "\n".join(f"l{i} velha" for i in range(12)) + "\n"
        (self.root / "plan.md").write_text(texto, encoding="utf-8")
        fichas = [ach(f"n-{i:02d}", f"l{i} velha", f"l{i} nova") for i in range(12)]
        rel, ok, _ = A.aplicar(fichas, self.root)
        self.assertEqual(len(rel["aplicados"]), 10)
        self.assertEqual(len(rel["escalados"]), 2)

    def test_dry_nao_grava(self):
        rel, _, _ = A.aplicar([ach("n-01", "linha um", "linha UM")], self.root, dry=True)
        self.assertEqual(rel["previstos"], ["n-01"])
        self.assertEqual(self.txt(), BASE)

    def test_extrai_bloco_ficha_m_do_parecer_e_cli(self):
        parecer = self.root / "parecer.md"
        parecer.write_text("# P\n<!-- FICHA-M\n" + json.dumps({"achados": [ach("n-01", "linha um", "linha UM")]}) + "\n-->\n", encoding="utf-8")
        self.assertEqual(A.main([str(parecer), "--root", str(self.root)]), 0)
        self.assertIn("linha UM", self.txt())

    def test_cli_sem_bloco_nada_faz_e_escala_da_exit_1(self):
        parecer = self.root / "p2.md"
        parecer.write_text("# sem ficha", encoding="utf-8")
        self.assertEqual(A.main([str(parecer), "--root", str(self.root)]), 0)
        j = self.root / "f.json"
        j.write_text(json.dumps({"achados": [ach("M-01", "linha um", "x", sev="MEDIA")]}), encoding="utf-8")
        self.assertEqual(A.main([str(j), "--root", str(self.root)]), 1)

    def test_deterministico(self):
        f = [ach("n-01", "linha um", "linha UM")]
        r1, _, _ = A.aplicar(f, self.root, dry=True)
        r2, _, _ = A.aplicar(f, self.root, dry=True)
        self.assertEqual(json.dumps(r1, sort_keys=True), json.dumps(r2, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
