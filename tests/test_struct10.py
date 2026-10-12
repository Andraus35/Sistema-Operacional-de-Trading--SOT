"""Regressão do STRUCT-10 (CONS-01) — python -m unittest tests/test_struct10.py"""
import sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import validate_spec_sot as v  # noqa: E402

ROADMAP = "| Decisões FECHADAS | B-001 (x) · **L-001 — FECHADA (y; runtime → SPEC-018/K-001)** |\n"


def run(content, roadmap=ROADMAP):
    with tempfile.TemporaryDirectory() as d:
        r = Path(d) / "ROADMAP.md"
        r.write_text(roadmap, encoding="utf-8")
        return v.check_cons01(content, roadmap=r)


class Struct10(unittest.TestCase):
    def test_id_fechado_no_roadmap_pode_ser_citado(self):
        self.assertTrue(run("Resolve L-001, que ficou estável no plano.")[0])

    def test_id_citado_como_fechado_pelo_roadmap_nao_contamina_K001(self):
        # K-001 só aparece como referência dentro do segmento de L-001: NÃO é fechado
        ok, _ = run("K-001 está fechada.")
        self.assertFalse(ok)

    def test_referencia_solta_a_id_declarado_pendente_passa(self):
        txt = "J-001 em aberto.\n" + ("x" * 500) + "\nrespeita J-001/CC-02 aqui."
        self.assertTrue(run(txt)[0])

    def test_id_aberto_afirmado_fechado_reprova(self):
        txt = "J-001 em aberto.\n" + ("x" * 500) + "\nJ-001 fechada e homologada."
        self.assertFalse(run(txt)[0])

    def test_id_nunca_declarado_pendente_reprova(self):
        self.assertFalse(run("Os limiares de J-001 valem 0.7.")[0])

    def test_id_com_marca_local_passa(self):
        self.assertTrue(run("J-001 pendente de Andraus.")[0])

    def test_sem_roadmap_id_fechado_nao_isenta(self):
        self.assertFalse(run("L-001 citado sem status.", roadmap="")[0])


class Struct10Negacao(unittest.TestCase):
    """Negação/condicional adjacente a 'fechada' NÃO é afirmação de fechamento (achado da medição SPEC-006)."""

    BASE = "J-001 em aberto.\n" + ("x" * 500) + "\n"

    def test_nao_fechada_passa(self):
        self.assertTrue(run(self.BASE + "J-001 não fechada ainda.")[0])

    def test_antes_de_fechada_passa(self):
        self.assertTrue(run(self.BASE + "alcance limitado antes de J-001 fechada.")[0])

    def test_enquanto_resolvida_passa(self):
        self.assertTrue(run(self.BASE + "vale enquanto J-001 resolvida não vier.")[0])

    def test_afirmacao_positiva_continua_reprovando(self):
        self.assertFalse(run(self.BASE + "J-001 fechada e aprovada.")[0])
        self.assertFalse(run(self.BASE + "J-001 está fechada.")[0])
        self.assertFalse(run(self.BASE + "J-001 foi resolvida em chat.")[0])


if __name__ == "__main__":
    unittest.main()
