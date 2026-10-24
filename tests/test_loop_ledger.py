import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import loop_ledger as L  # noqa: E402

PARECER_A = """# Parecer
## Médias da R1
- **M-01** resolvido
## Média
- **R2-M1** contradição entre RULE-X e a BASpec (dois desfechos).
## Menores
m-01 âncora l.12 desatualizada · m-02 homônimo do campo x.
"""
PARECER_B = """# Parecer
## Médias
- **N-01** dois códigos para a mesma condição, contradição interna.
## Menores
- **n-02** pré-condição da fixture não declarada.
<!-- ACHADOS-ESTRUTURADOS
ID|SEV|CATEGORIA|CAUSA|PREVENCAO
X-01|MEDIA|C05|sem campo de registro|G-B
-->
"""


def monta(root):
    d = root / "governance" / "propostas" / "SPEC-123"
    d.mkdir(parents=True)
    (d / "PARECER-REVISOR-SPEC123-PLAN-R1-2026-01-01.md").write_text(PARECER_A, encoding="utf-8")
    (d / "PARECER-REVISOR-SPEC123-PLAN-R2-2026-01-02.md").write_text(PARECER_B, encoding="utf-8")


class TestLoopLedger(unittest.TestCase):
    def test_extracao_heuristica_ignora_status_de_rodada_anterior(self):
        ach = L.extrair_heuristico(PARECER_A)
        ids = {(a["id"], a["sev"]) for a in ach}
        self.assertIn(("R2-M1", "Média"), ids)
        self.assertNotIn(("M-01", "Média"), ids)  # seção "Médias da R1" é status, não achado novo
        self.assertIn(("m-01", "Menor"), ids)
        self.assertIn(("m-02", "Menor"), ids)

    def test_categoria_por_palavra_chave(self):
        self.assertEqual(L.categoria("contradição entre duas regras")[0], "C01")
        self.assertEqual(L.categoria("campo homônimo")[0], "C02")
        self.assertEqual(L.categoria("coisa nenhuma")[0], "C99")

    def test_estruturado_prevalece_e_e_marcado(self):
        ach = L.extrair_estruturado(PARECER_B)
        self.assertEqual(len(ach), 1)
        self.assertEqual((ach[0]["id"], ach[0]["sev"], ach[0]["cat"][0], ach[0]["fonte"]), ("X-01", "Média", "C05", "estruturado"))

    def test_linha_de_trabalho_e_rodada(self):
        self.assertEqual(L.linha_trabalho("governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R4-2026-10-24.md"), ("SPEC-007 PLAN", 4))
        self.assertEqual(L.linha_trabalho("governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-ABERTURA-R2-x.md"), ("SPEC-048 ABERTURA", 2))

    def test_gerar_e_deterministico_e_aponta_lacuna(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            monta(root)
            a, b = L.gerar(root), L.gerar(root)
            self.assertEqual(a, b)  # mesma entrada => mesmo texto (sem relógio)
            self.assertIn("SPEC-123 PLAN", a)
            self.assertIn("1 → 2", a)  # Médias por rodada (R1: R2-M1; R2: N-01 heurístico + X-01 estruturado)
            self.assertIn("LACUNAS DE PREVENÇÃO", a)
            self.assertIn("| C01 |", a)  # C01 aparece nas duas rodadas e sem registro => lacuna

    def test_registro_com_prevencao_remove_a_lacuna(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            monta(root)
            (root / "governance" / "aprendizado").mkdir(parents=True)
            (root / L.REGISTRY).write_text(
                "| Cod | Categoria | Causa | Prevenção atual | Gate | 4Es | Reg |\n|---|---|---|---|---|---|---|\n"
                "| C01 | contradicao_interna | x | Gate G-B ativo | G-B | Eficácia | 2026 |\n", encoding="utf-8")
            txt = L.gerar(root)
            lacunas = txt.split("## 4.")[1].split("## 5.")[0]
            self.assertNotIn("| C01 |", lacunas)

    def test_check_detecta_desatualizado(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            monta(root)
            self.assertEqual(L.main(["--root", td, "--check"]), 1)
            self.assertEqual(L.main(["--root", td]), 0)
            self.assertEqual(L.main(["--root", td, "--check"]), 0)


if __name__ == "__main__":
    unittest.main()


class TestRetrospectiva(unittest.TestCase):
    def test_retro_check_exige_feita(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            monta(root)
            self.assertEqual(L.main(["--root", td, "--retro-check", "SPEC-123"]), 1)
            (root / "governance" / "aprendizado").mkdir(parents=True)
            (root / L.RETRO).write_text("| SPEC-123 | x | 2026-01-01 | PENDENTE |\n", encoding="utf-8")
            self.assertEqual(L.main(["--root", td, "--retro-check", "SPEC-123"]), 1)
            (root / L.RETRO).write_text("| SPEC-123 | x | 2026-01-01 | FEITA |\n", encoding="utf-8")
            self.assertEqual(L.main(["--root", td, "--retro-check", "SPEC-123"]), 0)

    def test_ledger_lista_specs_sem_retrospectiva(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            monta(root)
            self.assertIn("SPEC-123", L.gerar(root).split("## 5.")[1].split("## 6.")[0])
