import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import detectores_novos as n

PLAN = """### D3.1 — Vocabulário unificado de códigos
| código | dono |
|---|---|
| `WRV_AA_BB` | SPEC-049 |
## Regras
- Quando X falhar, o compilador DEVE recusar com `WRV_AA_BB`.
"""
class T(unittest.TestCase):
    def test_c1a_limpo_e_mutante(self):
        self.assertEqual(n.codigos_sem_definicao(PLAN), [])
        self.assertEqual(len(n.codigos_sem_definicao(PLAN + "- usa `WRV_CC_DD` aqui\n")), 1)
    def test_c1a_enum_de_outra_familia_nao_alarma(self):
        self.assertEqual(n.codigos_sem_definicao(PLAN + "- estado APROVADA_PARA_ENTREGA\n"), [])
    def test_c1b(self):
        self.assertEqual(n.recusa_sem_codigo(PLAN), [])
        self.assertEqual(len(n.recusa_sem_codigo(PLAN + "- Quando Y, o compilador DEVE recusar (fail-closed).\n")), 1)
    def test_c2_renomeacao(self):
        b = "linha com WRV_AA_BB aqui\noutra com WRV_AA_BB\n"; v = "linha com WRV_CC_DD aqui\noutra com WRV_AA_BB\n"
        self.assertEqual(len(n.token_antigo_presente(b, v)), 1)
        self.assertEqual(n.token_antigo_presente(b, "linha com WRV_CC_DD aqui\noutra com WRV_CC_DD\n"), [])
    def test_c2_historico_ignorado(self):
        b = "| 1.0 | 2026-10-31 | WRV_AA_BB |\nx WRV_AA_BB\n"; v = "| 1.1 | 2026-10-31 | WRV_CC_DD |\nx WRV_CC_DD\n"
        self.assertEqual(n.token_antigo_presente(b, v), [])
if __name__ == "__main__": unittest.main()

class TC4(unittest.TestCase):
    PLAN = "- RULE-WRV-001 e RULE-WRV-002; BASpec-WRV-001; ENF-02\n"
    def test_limpo(self):
        self.assertEqual(n.checks_ancorado("| F1 | RULE-WRV-001; ENF-02; RULE-ABC-009 | ✔ |\n", self.PLAN), [])
    def test_id_proprio_inexistente(self):
        self.assertEqual(len(n.checks_ancorado("| F1 | RULE-WRV-099 | ✔ |\n", self.PLAN)), 1)
    def test_sem_marca_nao_conta(self):
        self.assertEqual(n.checks_ancorado("| F1 | RULE-WRV-099 | pendente |\n", self.PLAN), [])
