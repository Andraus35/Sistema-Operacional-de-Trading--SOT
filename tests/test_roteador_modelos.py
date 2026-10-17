"""Testes do roteador determinístico de modelos (scripts/roteador_modelos.py) — DHR-ROTEAMENTO-003."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import roteador_modelos as r  # noqa: E402


def d(**k):
    return r.decidir(k)[0]


class Roteador(unittest.TestCase):
    def test_especificador_e_revisor_sem_parametro(self):
        self.assertEqual(d(subagent_type="Revisor SOT", prompt="audite"), "permitir")
        self.assertEqual(d(subagent_type="Especificador SOT"), "permitir")

    def test_especificador_e_revisor_com_model_ou_effort_negados(self):
        for t in ("Revisor SOT", "Especificador SOT"):
            self.assertEqual(d(subagent_type=t, model="haiku"), "negar")
            self.assertEqual(d(subagent_type=t, model="opus"), "negar")
            self.assertEqual(d(subagent_type=t, effort="low"), "negar")

    def test_haiku_nunca_como_gate_ou_soberano(self):
        self.assertEqual(d(subagent_type="general-purpose", model="haiku", description="rodar o gate e emitir parecer"), "negar")
        self.assertEqual(d(subagent_type="general-purpose", model="haiku", prompt="homologar a SPEC-006"), "negar")

    def test_tarefa_operacional_em_modelo_barato_permitida(self):
        self.assertEqual(d(subagent_type="Explore", model="haiku", description="listar arquivos de governance"), "permitir")
        self.assertEqual(d(subagent_type="Explore", description="busca ampla"), "permitir")

    def test_modelo_fora_da_tabela_negado(self):
        self.assertEqual(d(subagent_type="Explore", model="gpt-5"), "negar")

    def test_sonnet_em_revisao_por_auxiliar_permitido(self):
        self.assertEqual(d(subagent_type="general-purpose", model="sonnet", description="revisar texto"), "permitir")


if __name__ == "__main__":
    unittest.main()
