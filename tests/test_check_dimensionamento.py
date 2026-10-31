import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_dimensionamento as C  # noqa: E402


def plan(root, spec, corpo, anexo=0):
    d = root / "specs" / "features" / spec
    d.mkdir(parents=True)
    (d / "plan.md").write_text("linha\n" * corpo + ("## Anexo R\n" + "x\n" * anexo if anexo else ""), encoding="utf-8")


class TestDimensionamento(unittest.TestCase):
    def test_classificacao_prospectiva_desde_spec_049(self):
        self.assertEqual(C.classificar(2500, 48)[0], "INFO")   # anterior: só histórico
        self.assertEqual(C.classificar(2100, 49)[0], "WARN")   # acima do teto
        self.assertEqual(C.classificar(1950, 49)[0], "WARN")   # acima do alerta
        self.assertEqual(C.classificar(1700, 49)[0], "INFO")   # pede confirmação
        self.assertEqual(C.classificar(1500, 49)[0], "OK")

    def test_anexos_nao_contam_no_corpo(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            plan(root, "SPEC-049", 1500, anexo=3000)
            nivel, txt = C.checar_planos(root)[0][0], C.checar_planos(root)[0][2]
            self.assertEqual(nivel, "OK")
            self.assertIn("1500", txt)

    def test_hash_ausente_em_rodada_por_delta_apos_a_vigencia(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            d = root / "governance" / "propostas" / "SPEC-049"
            d.mkdir(parents=True)
            (d / "PARECER-REVISOR-SPEC049-PLAN-R2-2026-11-02.md").write_text("# R2 por delta\n", encoding="utf-8")
            (d / "PARECER-REVISOR-SPEC049-PLAN-R3-2026-11-03.md").write_text("MODO: delta\nSHA256-ALVO: " + "a" * 64 + "\n", encoding="utf-8")
            (d / "PARECER-REVISOR-SPEC049-PLAN-R2-2026-10-31.md").write_text("# R2 por delta\n", encoding="utf-8")  # anterior à regra
            achados = C.checar_hash(root)
            self.assertEqual(len(achados), 1)
            self.assertIn("R2-2026-11-02", achados[0][1])


if __name__ == "__main__":
    unittest.main()
