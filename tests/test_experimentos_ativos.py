"""Testes de scripts/experimentos_ativos.py (DHR-PROCESSO-EXPERIMENTOS-001): experimento aprovado entra nos pedidos por código, não por lembrança."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import experimentos_ativos as E  # noqa: E402

HASH = "a" * 64
MARC = "EXPERIMENTO: P10-REGRA-DE-PARADA"
REG = {"registro": "x", "versao": "1.0", "experimentos": [{
    "id": "P10-REGRA-DE-PARADA", "descricao": "regras do P10", "ata": "DHR-EXPERIMENTO-PARADA-001", "estado": "ativo",
    "escopo": {"tipo": "spec", "specs": ["SPEC-123"]}, "teto_rodadas_revisao": 3, "hash_a_partir_da_rodada": 2,
    "escalado_por_andraus": False, "marcador": MARC}]}


def monta(root, rodadas=0, reg=None, plan=True):
    root = Path(root)
    (root / "governance" / "propostas" / "SPEC-123").mkdir(parents=True)
    (root / "governance" / "aprendizado").mkdir(parents=True)
    (root / E.REGISTRO).write_text(json.dumps(reg or REG), encoding="utf-8")
    for r in range(1, rodadas + 1):
        (root / "governance" / "propostas" / "SPEC-123" / f"PARECER-REVISOR-SPEC123-PLAN-R{r}-2026-11-14.md").write_text(
            "# Parecer\n<!-- ACHADOS-ESTRUTURADOS\nR1-m01|MENOR|C01|x|y\n-->\n", encoding="utf-8")
    if plan:
        (root / "specs" / "features" / "SPEC-123").mkdir(parents=True)
        (root / "specs" / "features" / "SPEC-123" / "plan.md").write_text("x\n", encoding="utf-8")


def rev(extra="", marc=True, spec="SPEC-123"):
    p = f"CLASSE-TAREFA: S3\nALVO: specs/features/{spec}/plan.md\n" + (MARC + "\n" if marc else "") + extra + "\nRevise o Plan.\n"
    return {"subagent_type": "Revisor SOT", "model": "opus", "prompt": p}


def esp(marc=True, spec="SPEC-123"):
    p = "CLASSE-TAREFA: O\n" + (MARC + "\n" if marc else "") + f"Escreva o Plan da {spec}.\n"
    return {"subagent_type": "Especificador SOT", "model": "opus", "prompt": p}


class TestFalhaOriginal(unittest.TestCase):
    def test_plan_no_escopo_sem_clausula_e_negado(self):
        """A falha real: o Plan abriu e o pedido saiu sem o experimento aprovado."""
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            self.assertIn("EXPERIMENTO: P10-REGRA-DE-PARADA", E.decidir(esp(marc=False), td))
            self.assertIn("regras do P10", E.decidir(esp(marc=False), td))       # a negação traz o texto a colar
            self.assertIsNone(E.decidir(esp(marc=True), td))

    def test_revisor_sem_clausula_negado_com_clausula_liberado(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            self.assertIsNotNone(E.decidir(rev(marc=False), td))
            self.assertIsNone(E.decidir(rev(marc=True), td))                     # rodada 1: sem hash exigido

    def test_sendmessage_tambem_e_coberto(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            msg = {"to": "a111", "message": "CLASSE-TAREFA: O\nCorrija o Plan da SPEC-123 (plan.md).\n"}
            self.assertIsNotNone(E.decidir(msg, td))
            msg["message"] = "CLASSE-TAREFA: O\n" + MARC + "\nCorrija o Plan da SPEC-123 (plan.md).\n"
            self.assertIsNone(E.decidir(msg, td))

    def test_fora_do_escopo_nao_interfere(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            self.assertIsNone(E.decidir(esp(marc=False, spec="SPEC-999"), td))           # outra Spec
            self.assertIsNone(E.decidir({"subagent_type": "Explore", "prompt": "Plan da SPEC-123"}, td))   # não é agente construtor
            self.assertIsNone(E.decidir({"subagent_type": "Especificador SOT", "prompt": "CLASSE-TAREFA: O\nPesquise SPEC-123 sem plano"}, td))  # não é pedido sobre o Plan

    def test_experimento_encerrado_nao_exige(self):
        with tempfile.TemporaryDirectory() as td:
            reg = copy.deepcopy(REG)
            reg["experimentos"][0]["estado"] = "encerrado"
            monta(td, reg=reg)
            self.assertIsNone(E.decidir(esp(marc=False), td))


class TestTetoEHash(unittest.TestCase):
    def test_teto_de_rodadas_por_codigo(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td, rodadas=2)
            self.assertIsNone(E.decidir(rev(f"SHA256-ALVO: {HASH}"), td))                # seria a rodada 3 (= teto)
        with tempfile.TemporaryDirectory() as td:
            monta(td, rodadas=3)
            motivo = E.decidir(rev(f"SHA256-ALVO: {HASH}"), td)                          # seria a rodada 4 > teto 3
            self.assertIn("TETO de 3 rodadas", motivo)
            self.assertIn("escalar a Andraus", motivo)

    def test_escalado_por_andraus_libera_rodada_extra(self):
        with tempfile.TemporaryDirectory() as td:
            reg = copy.deepcopy(REG)
            reg["experimentos"][0]["escalado_por_andraus"] = True
            monta(td, rodadas=3, reg=reg)
            self.assertIsNone(E.decidir(rev(f"SHA256-ALVO: {HASH}"), td))

    def test_teto_nao_vale_para_o_especificador(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td, rodadas=3)
            self.assertIsNone(E.decidir(esp(), td))                                      # corrigir depois da R3 é permitido

    def test_hash_obrigatorio_da_rodada_2_em_diante(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td, rodadas=1)                                                         # seria a rodada 2
            self.assertIn("SHA256-ALVO", E.decidir(rev(), td))
            self.assertIn("SHA256-ALVO", E.decidir(rev("SHA256-ALVO: curto"), td))       # hash inválido não vale
            self.assertIsNone(E.decidir(rev(f"SHA256-ALVO: {HASH}"), td))
        with tempfile.TemporaryDirectory() as td:
            monta(td, rodadas=0)                                                         # rodada 1: não exige
            self.assertIsNone(E.decidir(rev(), td))


class TestProximoPlanECi(unittest.TestCase):
    REGP = {"registro": "x", "versao": "1.0", "experimentos": [{
        "id": "P10-REGRA-DE-PARADA", "descricao": "d", "ata": "DHR-X-001", "estado": "ativo",
        "escopo": {"tipo": "proximo-plan", "apos": "2026-10-31"}, "marcador": MARC}]}

    def test_ci_falha_com_plan_em_redacao_e_experimento_nao_vinculado(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td, rodadas=1, reg=self.REGP)
            probs = E.ci(td)
            self.assertTrue(any("sem `vinculado_a`" in p for p in probs), probs)
            reg = copy.deepcopy(self.REGP)
            reg["experimentos"][0]["vinculado_a"] = "SPEC-123"
            (Path(td) / E.REGISTRO).write_text(json.dumps(reg), encoding="utf-8")
            self.assertEqual(E.ci(td), [])

    def test_ci_ok_sem_plan_em_redacao(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td, rodadas=0, reg=self.REGP, plan=False)
            self.assertEqual(E.ci(td), [])

    def test_proximo_plan_exige_clausula_no_primeiro_plan(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td, rodadas=0, reg=self.REGP, plan=False)
            self.assertIsNotNone(E.decidir(esp(marc=False), td))                         # Spec sem plan.md = Plan a abrir
            self.assertIsNone(E.decidir(esp(marc=True), td))


class TestRegistro(unittest.TestCase):
    def test_registro_do_repositorio_e_valido_e_o_ci_passa(self):
        self.assertEqual(E.validar(E.ler_registro(REPO)), [])
        self.assertEqual(E.ci(REPO), [])

    def test_validar_pega_defeitos(self):
        bad = copy.deepcopy(REG)
        bad["experimentos"][0]["marcador"] = "EXPERIMENTO: OUTRO"
        bad["experimentos"].append({"id": "X", "estado": "ativo"})
        probs = E.validar(bad)
        self.assertTrue(any("marcador" in p for p in probs))
        self.assertTrue(any("campos ausentes" in p for p in probs))

    def test_fail_open_sem_registro(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "governance").mkdir()
            self.assertIsNone(E.decidir(esp(marc=False), td))


if __name__ == "__main__":
    unittest.main()
