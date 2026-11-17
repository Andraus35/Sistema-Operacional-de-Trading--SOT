"""Testes do cenario_precondicao.py (proposta P17(b)) — python -m unittest tests/test_cenario_precondicao.py"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "cenario_precondicao.py"
sys.path.insert(0, str(SCRIPT.parent))
import cenario_precondicao as cp  # noqa: E402

FIX = "## Fixture M0 (base)\n- **E1**: publicação. **S1**: setup. **A1**: alarme.\n\n"
OK = FIX + "## D7\n### Cenário-X-T01 — feliz\n```\nDADO        M0\nQUANDO      E1\nENTÃO       ok\n```\n"


class TestCenario(unittest.TestCase):
    def test_limpo(self):
        r = cp.verificar(OK)
        self.assertEqual(r["achados"], [])
        self.assertEqual(r["cenarios"], 1)
        self.assertEqual(r["fixtures"], ["A1", "E1", "M0", "S1"])

    def test_a_sem_dado(self):  # mutante: cenário sem pré-condição
        r = cp.verificar(FIX + "### Cenário-X-T02 — sem dado\n```\nQUANDO E1\n```\n")
        self.assertEqual([x["verif"] for x in r["achados"]], ["a"])

    def test_c_fixture_nao_declarada(self):  # mutante: nome que ninguém declara
        r = cp.verificar(OK.replace("DADO        M0", "DADO        M0 exceto H9"))
        self.assertTrue(any(x["verif"] == "c" and "H9" in x["msg"] for x in r["achados"]))

    def test_c_nome_definido_no_proprio_dado_ok(self):
        r = cp.verificar(OK.replace("DADO        M0", "DADO        M0; H9 = hipótese refutada"))
        self.assertFalse(any(x["verif"] == "c" for x in r["achados"]))

    def test_referencias_a_cenario_e_linha_nao_acusam(self):
        r = cp.verificar(OK.replace("DADO        M0", "DADO        M0 depois do T01; ciclo parado em F09"))
        self.assertEqual(r["achados"], [])

    def test_d_sem_secao_fixture(self):
        r = cp.verificar("### Cenário-X-T01 — a\n```\nDADO  Z3\nQUANDO  x\n```\n")
        self.assertEqual([x["verif"] for x in r["achados"]], ["d"])  # (c) não dispara sem seção Fixture

    def test_dado_multilinha(self):
        r = cp.verificar(FIX + "### Cenário-X-T03 — m\n```\nDADO        M0, exceto:\n            (a) S1 trocado por H9\nQUANDO      E1\n```\n")
        self.assertTrue(any("H9" in x["msg"] for x in r["achados"]))

    def test_cli_strict(self):
        d = Path(tempfile.mkdtemp())
        p = d / "plan.md"
        p.write_text(FIX + "### Cenário-X-T02 — sem dado\n```\nQUANDO E1\n```\n", encoding="utf-8")
        r0 = subprocess.run([sys.executable, str(SCRIPT), str(p)], capture_output=True, text=True, encoding="utf-8")
        r1 = subprocess.run([sys.executable, str(SCRIPT), str(p), "--strict"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual((r0.returncode, r1.returncode), (0, 1))

    def test_plan_real_da_spec_008_sem_achado_a(self):
        p = Path(__file__).resolve().parent.parent / "specs/features/SPEC-008/plan.md"
        if p.exists():
            r = cp.verificar(p.read_text(encoding="utf-8"))
            self.assertEqual(r["cenarios"], 23)
            self.assertFalse(any(x["verif"] == "a" for x in r["achados"]))


if __name__ == "__main__":
    unittest.main()
