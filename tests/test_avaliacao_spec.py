"""Testes de scripts/avaliacao_spec.py (DHR-AVALIACAO-001): avaliação de desempenho de fim de Spec, determinística e obrigatória."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import avaliacao_spec as A  # noqa: E402
import loop_ledger as L  # noqa: E402

PARECER1 = """# Parecer R1
## Veredito
**NÃO CONFORME.** 1 Média.
MODO: integral
TOKENS: 1000
## Achados
- ok
<!-- ACHADOS-ESTRUTURADOS
R1-M01|MEDIA|C01|contradicao|prev
R1-m01|MENOR|C07|ancora|prev
R1-m02|MENOR|C07|ancora2|prev
-->
<!-- FICHA-M {"achados":[{"id":"R1-m01"}]} -->
"""
PARECER2 = """# Parecer R2
## Veredito
**CONFORME condicional.** 0 Média.
MODO: delta
<!-- ACHADOS-ESTRUTURADOS
R2-m01|MENOR|C01|contradicao|prev
-->
"""
ATA_PLAN = """# DHR-SPEC123-002 — Ata
| Campo | Valor |
|---|---|
| Data | {data} |
| Status | **PLAN v1.0 HOMOLOGADO — BASELINE** (decisão) |
"""
ATA_DECISAO = "# DHR-X-001\n| Data | 2026-11-09 |\n"


def monta(root, data="2026-11-09"):
    root = Path(root)
    (root / "governance" / "propostas" / "SPEC-123").mkdir(parents=True)
    (root / "governance" / "aprendizado").mkdir(parents=True)
    (root / "specs" / "features" / "SPEC-123").mkdir(parents=True)
    (root / "specs" / "features" / "SPEC-123" / "plan.md").write_text("linha\n" * 1950, encoding="utf-8")
    (root / "governance" / "propostas" / "SPEC-123" / "PARECER-REVISOR-SPEC123-PLAN-R1-2026-11-09.md").write_text(PARECER1, encoding="utf-8")
    (root / "governance" / "propostas" / "SPEC-123" / "PARECER-REVISOR-SPEC123-PLAN-R2-2026-11-09.md").write_text(PARECER2, encoding="utf-8")
    (root / "governance" / "DHR-SPEC123-002_Ata_Homologacao_Plan_SPEC-123.md").write_text(ATA_PLAN.format(data=data), encoding="utf-8")
    (root / "governance" / "DHR-X-001_Ata_Decisao.md").write_text(ATA_DECISAO, encoding="utf-8")
    shutil.copy(REPO / A.CATALOGO, root / A.CATALOGO)
    (root / L.REGISTRY).write_text("| C01 | contradicao_interna | causa | AUSENTE | gate | Eficácia | 2026-11-09 |\n"
                                   "| C07 | citacao_ancora | causa | Parcial: Revisor | gate | Eficiência | 2026-11-09 |\n", encoding="utf-8")
    (root / L.RETRO).write_text("| SPEC-123 | x | 2026-11-09 | FEITA |\n", encoding="utf-8")


class TestAprovacaoProspectiva(unittest.TestCase):
    def test_exigida_so_a_partir_do_corte(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td, "2026-11-09")
            self.assertTrue(A.exigida(td, "SPEC-123"))
        with tempfile.TemporaryDirectory() as td:
            monta(td, "2026-11-07")  # anterior ao corte => não exigida (retroatividade proibida)
            self.assertFalse(A.exigida(td, "SPEC-123"))

    def test_ata_de_contrato_ou_abertura_nao_dispara(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            g = Path(td) / "governance"
            (g / "DHR-SPEC123-002_Ata_Homologacao_Plan_SPEC-123.md").unlink()
            (g / "DHR-SPEC123-003_Ata_Homologacao_Manager_Contract_MMC-001.md").write_text(ATA_PLAN.format(data="2026-11-09"), encoding="utf-8")
            (g / "DHR-SPEC123-001_Ata_Homologacao_Abertura_SPEC-123.md").write_text(ATA_PLAN.format(data="2026-11-09"), encoding="utf-8")
            self.assertFalse(A.exigida(td, "SPEC-123"))

    def test_sem_baseline_no_status_nao_conta(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            f = Path(td) / "governance" / "DHR-SPEC123-002_Ata_Homologacao_Plan_SPEC-123.md"
            f.write_text(f.read_text(encoding="utf-8").replace("— BASELINE", ""), encoding="utf-8")
            self.assertFalse(A.exigida(td, "SPEC-123"))

    def test_repositorio_real_nenhuma_spec_antiga_exigida(self):
        for spec in A.aprovadas(REPO):
            self.assertFalse(A.exigida(REPO, spec), spec)


class TestMetricas(unittest.TestCase):
    def test_metricas(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            m = A.metricas(td, "SPEC-123")
            self.assertEqual(m["rodadas_total"], 2)
            self.assertEqual(m["max_rodadas_linha"], 2)
            self.assertEqual(m["medias_r1_max"], 1)
            self.assertEqual(m["menores_total"], 3)
            self.assertEqual(m["menores_classe_m"], 1)
            self.assertEqual(m["pct_menores_classe_m"], 33)
            self.assertEqual(m["rodadas_sem_tokens"], 1)  # R2 sem TOKENS
            self.assertEqual(m["plan_corpo_linhas"], 1950)
            self.assertIn("C01", m["categorias_recorrentes"])
            self.assertEqual(m["categorias_recorrentes_sem_prevencao_lista"], ["C01"])  # C07 tem prevenção parcial
            self.assertEqual(m["linhas"]["SPEC-123 PLAN"][0]["veredito"], "NÃO CONFORME")
            self.assertEqual(m["linhas"]["SPEC-123 PLAN"][1]["veredito"], "CONFORME CONDICIONAL")

    def test_gatilhos_do_catalogo(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            ids = [i["id"] for i in A.selecionar(td, A.metricas(td, "SPEC-123"))]
            self.assertEqual(ids[-1], "BP-01")                      # aceitação por último
            for esperado in ("BP-04", "BP-08", "BP-09", "BP-10"):   # C01 recorrente, prevenção ausente, plan 1950, tokens n/m
                self.assertIn(esperado, ids)
            self.assertNotIn("BP-02", ids)                          # só 2 rodadas
            self.assertNotIn("BP-07", ids)                          # sem C10
            self.assertNotIn("BP-12", ids)                          # 1 Média na R1 (<3)

    def test_lotes_de_ate_4_com_recomendada_primeiro(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            lotes = A.lotes(A.selecionar(td, A.metricas(td, "SPEC-123")))
            self.assertTrue(all(1 <= len(l) <= 4 for l in lotes))
            for lote in lotes:
                for q in lote:
                    self.assertIn("(Recomendado)", q["options"][0]["label"])
                    self.assertEqual(q["multiSelect"], False)
                    self.assertTrue(any("Adiar" in o["label"] for o in q["options"]))

    def test_catalogo_do_repositorio_valido(self):
        itens = A.carregar_catalogo(REPO)
        ids = [i["id"] for i in itens]
        self.assertEqual(len(ids), len(set(ids)))
        for i in itens:
            self.assertIn("(Recomendado)", i["opcoes"][0]["label"], i["id"])
            self.assertTrue(i["fontes"], i["id"])
            self.assertTrue(any(f["tipo"] == "INTERNA" for f in i["fontes"]), i["id"])
            for f in i["fontes"]:
                if f["tipo"] == "EXTERNA":
                    self.assertIn("não verificada", f.get("nota", ""), i["id"])  # web = dado: nunca apresentada como verificada


class TestDeterminismoEEstado(unittest.TestCase):
    def test_mesma_entrada_mesma_saida(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            self.assertEqual(A.gerar_texto(td, "SPEC-123"), A.gerar_texto(td, "SPEC-123"))

    def test_ciclo_ausente_gerada_respondida_desatualizada(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            self.assertEqual(A.estado(td, "SPEC-123"), "AUSENTE")
            self.assertEqual(A.main(["--root", td, "--ci"]), 1)
            self.assertEqual(A.main(["--root", td, "gerar", "SPEC-123", "--write"]), 0)
            self.assertEqual(A.estado(td, "SPEC-123"), "GERADA")
            self.assertEqual(A.main(["--root", td, "--ci"]), 0)          # CI exige só existir e estar atual
            self.assertEqual(A.main(["--root", td, "--pendentes"]), 1)   # mas a resposta de Andraus ainda falta
            with self.assertRaises(SystemExit):                          # registrar exige a ata da decisão
                A.main(["--root", td, "registrar", "SPEC-123", "--ata", "DHR-INEXISTENTE-9", "--resposta", "ok"])
            with self.assertRaises(SystemExit):                          # e resposta não vazia
                A.main(["--root", td, "registrar", "SPEC-123", "--ata", "DHR-X-001", "--resposta", "  "])
            self.assertEqual(A.estado(td, "SPEC-123"), "GERADA")
            self.assertEqual(A.main(["--root", td, "registrar", "SPEC-123", "--ata", "DHR-X-001", "--resposta", "Aceitar e registrar (AskUserQuestion 2026-11-09)"]), 0)
            self.assertEqual(A.estado(td, "SPEC-123"), "RESPONDIDA")
            self.assertEqual(A.main(["--root", td, "--pendentes"]), 0)
            # muda o dado de entrada => avaliação fica DESATUALIZADA (não vale resposta antiga)
            (Path(td) / "governance" / "propostas" / "SPEC-123" / "PARECER-REVISOR-SPEC123-PLAN-R3-2026-11-09.md").write_text(PARECER2, encoding="utf-8")
            self.assertEqual(A.estado(td, "SPEC-123"), "DESATUALIZADA")
            self.assertEqual(A.main(["--root", td, "--ci"]), 1)

    def test_resposta_respondida_nao_e_sobrescrita(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            A.main(["--root", td, "gerar", "SPEC-123", "--write"])
            A.main(["--root", td, "registrar", "SPEC-123", "--ata", "DHR-X-001", "--resposta", "ok"])
            A.main(["--root", td, "gerar", "SPEC-123", "--write"])
            self.assertEqual(A.estado(td, "SPEC-123"), "RESPONDIDA")

    def test_estado_forjado_sem_resposta_nao_vale(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            A.main(["--root", td, "gerar", "SPEC-123", "--write"])
            p = A.caminho(td, "SPEC-123")
            p.write_text(p.read_text(encoding="utf-8").replace("| Estado | GERADA |", "| Estado | RESPONDIDA |"), encoding="utf-8")
            self.assertEqual(A.estado(td, "SPEC-123"), "GERADA")  # Estado RESPONDIDA sem Resposta/Ata não conta

    def test_pendentes_json(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            pend = A.pendentes(td)
            self.assertEqual(pend, [{"spec": "SPEC-123", "estado": "AUSENTE", "ata": "DHR-SPEC123-002"}])


class TestBarraDaProximaSpec(unittest.TestCase):
    def test_retro_check_exige_avaliacao_respondida(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td)
            self.assertEqual(L.main(["--root", td, "--retro-check", "SPEC-123"]), 1)  # retrospectiva FEITA, mas avaliação AUSENTE
            A.main(["--root", td, "gerar", "SPEC-123", "--write"])
            self.assertEqual(L.main(["--root", td, "--retro-check", "SPEC-123"]), 1)  # GERADA ainda não basta
            A.main(["--root", td, "registrar", "SPEC-123", "--ata", "DHR-X-001", "--resposta", "ok"])
            self.assertEqual(L.main(["--root", td, "--retro-check", "SPEC-123"]), 0)

    def test_retro_check_spec_antiga_inalterado(self):
        with tempfile.TemporaryDirectory() as td:
            monta(td, "2026-11-07")
            self.assertEqual(L.main(["--root", td, "--retro-check", "SPEC-123"]), 0)  # retroatividade proibida


if __name__ == "__main__":
    unittest.main()
