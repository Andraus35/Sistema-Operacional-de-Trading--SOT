"""Testes do build_map.py (BL-019) — python -m unittest tests/test_build_map.py"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"

FILES = {
    "ROADMAP.md": "# Roadmap\n### SPEC-001 — X **HOMOLOGADA**\nVer `governance/RULES.md` e SPEC-002.\n",
    "governance/RULES.md": "# Regras\nRULE-AA-01 e INV-07. Cita `canon/CHM-001-x.md`.\n",
    "governance/DHR-EUA-E04_ata.md": "# Ata\nEUA-E04 homologada.\n",
    "governance/EUA-E04_proposta_PROPOSTA.md": "# Proposta\n",
    "canon/CHM-001-x.md": "# Modelo CHM\n",
    "reference/solto.md": "# Solto\nninguém cita\n",
    "backlog/RMR-001_Painel_Backlog.md": "| **BL-001** | t | Ideia | P | `evento:x` | a | Em espera | o |\n",
    "specs/features/SPEC-001/plan.md": "# Plan\nStatus: HOMOLOGADA\nUsa RULE-AA-01, INV-07 e EUA-E04.\n",
}


class BuildMap(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)
        (self.d / "scripts").mkdir()
        for n in ("build_map.py", "check_refs.py", "backlog_triggers.py"):
            shutil.copy(SCRIPTS / n, self.d / "scripts" / n)
        for n, body in FILES.items():
            p = self.d / n
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, encoding="utf-8")

    def run_map(self, *args):
        return subprocess.run([sys.executable, str(self.d / "scripts" / "build_map.py"), "--date", "2026-01-01", *args],
                              capture_output=True, text=True, encoding="utf-8", cwd=self.d)

    def md(self):
        return (self.d / "docs" / "mapa" / "MAPA-PROJETO.md").read_text(encoding="utf-8")

    def js(self):
        return json.loads((self.d / "docs" / "mapa" / "mapa-projeto.json").read_text(encoding="utf-8"))

    def test_gera_md_e_json_nao_normativo(self):
        r = self.run_map()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("NÃO-NORMATIVO", self.md())
        self.assertFalse(self.js()["meta"]["normative"])

    def test_hub_de_id_aponta_definicao(self):
        self.run_map()
        ids = {i["id"]: i for i in self.js()["ids"]}
        self.assertEqual(ids["INV-07"]["defined_in"], "governance/RULES.md")
        self.assertEqual(ids["INV-07"]["cited_by"], 1)

    def test_eua_aponta_ata_homologada_e_nao_proposta(self):
        self.run_map()
        ids = {i["id"]: i for i in self.js()["ids"]}
        self.assertEqual(ids["EUA-E04"]["defined_in"], "governance/DHR-EUA-E04_ata.md")

    def test_orfao_listado_e_citado_por_chave_nao(self):
        self.run_map()
        md = self.md()
        sec = md.split("## 6.")[1].split("## 7.")[0]
        self.assertIn("reference/solto.md", sec)
        self.assertNotIn("CHM-001-x.md", sec)  # citado por caminho em RULES.md

    def test_estado_da_spec(self):
        self.run_map()
        self.assertRegex(self.md(), r"`SPEC-001` \| \*\*Homologada\*\*")

    def test_check_nao_depende_do_json(self):
        """A2.1: o .json é artefato local; --check decide pelo digest do .md versionado."""
        self.run_map()
        (self.d / "docs" / "mapa" / "mapa-projeto.json").unlink()
        self.assertEqual(self.run_map("--check").returncode, 0)
        (self.d / "governance" / "RULES.md").write_text("# Regras\nmudou\n", encoding="utf-8")
        self.assertEqual(self.run_map("--check").returncode, 1)

    def test_aresta_de_caminho_no_json(self):
        self.run_map()
        self.assertIn({"from": "ROADMAP.md", "to": "governance/RULES.md", "type": "path"}, self.js()["edges"])

    def test_digest_estavel_e_check(self):
        self.run_map()
        d1 = self.js()["meta"]["digest"]
        self.run_map()
        self.assertEqual(d1, self.js()["meta"]["digest"])
        self.assertEqual(self.run_map("--check").returncode, 0)

    def test_check_detecta_defasagem(self):
        self.run_map()
        (self.d / "governance" / "RULES.md").write_text("# Regras\nmudou\n", encoding="utf-8")
        self.assertEqual(self.run_map("--check").returncode, 1)

    def test_check_sem_mapa_exit_2(self):
        self.assertEqual(self.run_map("--check").returncode, 2)

    def test_mapa_nao_polui_o_proprio_grafo(self):
        self.run_map()
        self.run_map()
        self.assertFalse(any(d["path"].startswith("docs/mapa/") for d in self.js()["docs"]))


if __name__ == "__main__":
    unittest.main()
