"""Testes do detector de valores e ordem das regras fixas (scripts/check_invariants.py) — DHR-AUDITOR-EXTERNO-008 R2."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_invariants as ci  # noqa: E402


def cods(linha):
    return {c for c, _, _ in ci.checar_linha(linha)}


class TestDetecta(unittest.TestCase):
    def test_rr(self):
        self.assertIn("INV-RR", cods("the Risk Agent SHALL rejeitar o sinal com R:R inferior a 2.0 (mínimo 1:2)."))
        self.assertIn("INV-RR", cods("| R:R mínimo | 2.5 |"))
        self.assertNotIn("INV-RR", cods("the Risk Agent SHALL rejeitar o sinal com R:R inferior a 3.0 (mínimo 1:3, sem exceção)."))
        self.assertNotIn("INV-RR", cods("| R:R mínimo | 3.0 |"))

    def test_score_e_conviccao(self):
        self.assertIn("INV-SCORE", cods("WHEN a convicção for ≥ 70% e o score for ≥ 5/9, o sinal SHALL ser elegível."))
        self.assertIn("INV-CONVICCAO", cods("WHEN a convicção for ≥ 60% e o score for ≥ 7/9, o sinal SHALL ser elegível."))
        self.assertEqual(cods("WHEN a convicção for ≥ 70% e o score for ≥ 7/9, o sinal SHALL ser elegível."), set())

    def test_dimensoes(self):
        self.assertIn("INV-DIM", cods("O vetor tem 9 dimensões: estrutural, geométrica, fractal, institucional, operacional, temporal, volume, custo."))
        self.assertEqual(cods("O vetor tem 8 dimensões: estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica."), set())

    def test_hierarquia(self):
        self.assertIn("INV-HIER", cods("A hierarquia é inviolável: Elliott → SMC → Fibonacci → Fractal → ICT. São quatro camadas."))
        self.assertEqual(cods("A hierarquia é inviolável: Elliott → Fibonacci → Fractal → SMC → ICT. São cinco camadas."), set())

    def test_estados(self):
        self.assertIn("INV-ESTADO", cods("Existem nove estados canônicos: PROPOSED → VALIDATED → ACTIVE → DOMINANT → SUPERSEDED → REFUTED → ARCHIVED."))
        self.assertEqual(cods("Existem sete estados canônicos: EMERGENT → CANDIDATE → ACTIVE → DOMINANT → SUPERSEDED → REFUTED → ARCHIVED."), set())

    def test_4es(self):
        self.assertIn("INV-4ES", cods("Economicidade > Eficiência > Efetividade > Eficácia > Conformidade. Economicidade nunca fica acima de Eficácia."))
        self.assertEqual(cods("Conformidade > Eficácia > Efetividade > Eficiência > Economicidade."), set())

    def test_dossie(self):
        self.assertIn("INV-DOSSIE", cods("| Validade do Dossiê de Pesquisa (HIGH) | 180 dias |"))
        self.assertEqual(cods("| Validade do Dossiê de Pesquisa (HIGH) | 90 dias |"), set())


class TestNaoDaFalsoAlarme(unittest.TestCase):
    """Casos reais que geraram falso alarme na calibração (10 Specs + canon/governance)."""

    def test_transicoes_proibidas_em_pares(self):
        self.assertEqual(cods("Transições proibidas: DOMINANT->ACTIVE, ACTIVE->CANDIDATE, CANDIDATE->EMERGENT (regressão)."), set())

    def test_conviccao_abaixo_do_piloto_citada_como_exemplo(self):
        self.assertEqual(cods("DADO        convicção global 68% (abaixo do piloto ≥70%)"), set())

    def test_conviccao_de_maturidade_e_bias(self):
        self.assertEqual(cods('DADO        proposta de "aprovar L3 se convicção-de-maturidade ≥ 80%"'), set())
        self.assertEqual(cods("RULE-EW-002: NÃO DEVE emitir bias com convicção < 60%."), set())

    def test_frase_solta_sobre_es(self):
        self.assertEqual(cods("Eficiência sem Eficácia é desperdício disfarçado de economia."), set())

    def test_tabela_de_correcao(self):
        self.assertEqual(cods("| **COR-GPR-002** | `Convicção Estrutural ≥ 60%` | **Convicção ≥ 70%** |"), set())


class TestFontes(unittest.TestCase):
    """Alarme de deriva: as constantes do detector ainda estão no AGENTS.md (fonte única). O detector não é 2ª fonte da verdade."""

    def test_fontes_no_agents(self):
        agents = re.sub(r"\s+", " ", (ROOT / "AGENTS.md").read_text(encoding="utf-8").replace("**", ""))
        for nome, trecho in ci.FONTES_AGENTS.items():
            self.assertIn(trecho, agents, f"AGENTS.md não contém mais o trecho-fonte de '{nome}': {trecho!r}")

    def test_smoke_specs_reais(self):
        self.assertEqual(ci.main([]), 0)   # padrão informativo: nunca falha


if __name__ == "__main__":
    unittest.main()
