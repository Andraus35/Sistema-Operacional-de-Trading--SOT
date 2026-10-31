import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import validate_spec_sot as V  # noqa: E402

CITA = "Esta Spec aplica RULE-MECH-01.\n"


def bloco(cls, campos):
    linhas = [f"    CLASSE      : {cls} (x)"] + [f"    {c}: x" for c in campos]
    return "BASpec-X-001:\n  CLASSE/MECANISMO:\n" + "\n".join(linhas) + "\n  VERIFICADO POR:\n    DADO x\n"


class TestClasseMecanismo(unittest.TestCase):
    def run_chk(self, txt):
        return V.check_classe_mecanismo(txt)[0]

    def test_nao_incide_sem_citar_rule_mech(self):
        self.assertTrue(self.run_chk("sem classe nenhuma"))

    def test_cita_sem_nenhum_bloco_reprova(self):
        self.assertFalse(self.run_chk(CITA + "texto"))

    def test_d_minimo_passa(self):
        self.assertTrue(self.run_chk(CITA + bloco("D", ["MECANISMO", "CRITÉRIO 4Es"])))

    def test_d_sem_criterio_reprova(self):
        self.assertFalse(self.run_chk(CITA + bloco("D", ["MECANISMO"])))

    def test_h_exige_loop_e_gate(self):
        self.assertFalse(self.run_chk(CITA + bloco("H", ["MECANISMO", "CRITÉRIO 4Es", "GATE DE SAÍDA"])))
        self.assertFalse(self.run_chk(CITA + bloco("H", ["MECANISMO", "CRITÉRIO 4Es", "BOUNDED LOOP"])))
        self.assertTrue(self.run_chk(CITA + bloco("H", ["MECANISMO", "CRITÉRIO 4Es", "BOUNDED LOOP", "GATE DE SAÍDA"])))

    def test_p_exige_loop_gate_opcional(self):
        self.assertFalse(self.run_chk(CITA + bloco("P", ["MECANISMO", "CRITÉRIO 4Es"])))
        self.assertTrue(self.run_chk(CITA + bloco("P", ["MECANISMO", "CRITÉRIO 4Es", "BOUNDED LOOP"])))

    def test_c_exige_gate(self):
        self.assertFalse(self.run_chk(CITA + bloco("C", ["MECANISMO", "CRITÉRIO 4Es"])))
        self.assertTrue(self.run_chk(CITA + bloco("C", ["MECANISMO", "CRITÉRIO 4Es", "GATE DE SAÍDA"])))

    def test_campo_do_bloco_vizinho_nao_vaza(self):
        txt = CITA + bloco("H", ["MECANISMO", "CRITÉRIO 4Es"]) + bloco("D", ["MECANISMO", "CRITÉRIO 4Es", "BOUNDED LOOP", "GATE DE SAÍDA"])
        self.assertFalse(self.run_chk(txt))


if __name__ == "__main__":
    unittest.main()
