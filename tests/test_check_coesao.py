"""Testes do check_coesao.py — python -m unittest tests/test_check_coesao.py

Repositório sintético em diretório temporário (sem git: as checagens que dependem de origin/main são
puladas), script chamado via subprocess com --root e saída lida via --json. Cada checagem tem um caso
que dispara e um que não dispara.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_coesao.py"


class Coesao(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)
        for sub in ("scripts", "tests", "governance", ".claude/agents", ".claude/skills", ".github/workflows"):
            (self.d / sub).mkdir(parents=True, exist_ok=True)

    def w(self, rel, text=""):
        p = self.d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def run_it(self):
        r = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.d), "--json"],
                           capture_output=True, text=True, encoding="utf-8")
        return json.loads(r.stdout), r.returncode

    def ids(self, level=None):
        out, _ = self.run_it()
        return [(f["id"], f["onde"]) for f in out["achados"] if level in (None, f["nivel"])]

    # COE-01 -------------------------------------------------------------
    def test_hook_sem_script(self):
        self.w(".claude/settings.json", '{"hooks":{"Stop":[{"hooks":[{"command":"node scripts/sumiu.js"}]}]}}')
        self.assertIn(("COE-01", "settings.json/pre-commit"), self.ids("ERRO"))

    def test_script_sem_uso_e_script_usado(self):
        self.w("scripts/orfao.py", "print(1)")
        self.w("scripts/usado.py", "print(2)")
        self.w("tests/test_usado.py", "import usado  # scripts/usado.py")
        achados = self.ids("WARN")
        self.assertIn(("COE-01", "scripts/orfao.py"), achados)
        self.assertNotIn(("COE-01", "scripts/usado.py"), achados)

    # COE-02 -------------------------------------------------------------
    def test_teste_fora_do_ci(self):
        self.w("tests/test_a.py")
        self.w("tests/test_b.py")
        self.w(".github/workflows/ci.yml", "run: python -m unittest tests/test_a.py\n")
        achados = self.ids("ERRO")
        self.assertIn(("COE-02", "tests/test_b.py"), achados)
        self.assertNotIn(("COE-02", "tests/test_a.py"), achados)

    def test_discover_cobre_python_e_npm_run_cobre_js(self):
        self.w("tests/test_a.py")
        self.w("tests/test-hook.js")
        self.w("package.json", '{"scripts":{"test:hooks":"node tests/test-hook.js"}}')
        self.w(".github/workflows/ci.yml", "run: python -m unittest discover -s tests\nrun: npm run test:hooks\n")
        self.assertEqual([x for x in self.ids() if x[0] == "COE-02"], [])

    # COE-03 -------------------------------------------------------------
    def test_precommit_noop(self):
        self.w("scripts/g.js", "const {readToolInput}=require('./hook-io');")
        self.w(".pre-commit-config.yaml", "entry: node scripts/g.js\n")
        self.assertIn(("COE-03", ".pre-commit-config.yaml"), self.ids("WARN"))

    # COE-04 -------------------------------------------------------------
    def test_ata_inexistente(self):
        self.w("governance/DHR-REAL-001_Ata.md")
        self.w("scripts/x.py", "# DHR-REAL-001 ok; DHR-FANTASMA-002 não existe")
        achados = [f for f in self.run_it()[0]["achados"] if f["id"] == "COE-04"]
        self.assertEqual([f["msg"].split()[0] for f in achados], ["DHR-FANTASMA-002"])

    # COE-05 -------------------------------------------------------------
    def test_caixa_do_arquivo(self):
        self.w("ROADMAP.md")
        self.w(".claude/agents/a.md", "---\ntools:\n  - Read\n---\nLeia roadmap.md e ROADMAP.md")
        achados = [f for f in self.run_it()[0]["achados"] if f["id"] == "COE-05"]
        self.assertEqual(len(achados), 1)
        self.assertIn("roadmap.md", achados[0]["msg"])

    # COE-06 -------------------------------------------------------------
    def test_tabela_do_agents_x_frontmatter(self):
        self.w("AGENTS.md", "| `.claude/agents/r.md` | Audita | Read · Grep |\n")
        self.w(".claude/agents/r.md", "---\nname: R\ntools:\n  - Read\n  - Grep\n  - WebFetch\n  - mcp__x__y\n---\n")
        msgs = [f["msg"] for f in self.run_it()[0]["achados"] if f["id"] == "COE-06"]
        self.assertTrue(msgs and "WebFetch" in msgs[0] and "mcp__x__y" in msgs[0])

    def test_tabela_igual_ao_frontmatter(self):
        self.w("AGENTS.md", "| `.claude/agents/r.md` | Audita | Read · Grep |\n")
        self.w(".claude/agents/r.md", "---\ntools:\n  - Read\n  - Grep\n---\n")
        self.assertEqual([x for x in self.ids() if x[0] == "COE-06"], [])

    # COE-07 -------------------------------------------------------------
    def test_selo_sem_dono(self):
        self.w("governance/GATE-MANIFEST.sha256", "abc  scripts/a.py\nabc  scripts/b.py\n")
        self.w(".github/CODEOWNERS", "/scripts/a.py @x\n")
        achados = [f["msg"] for f in self.run_it()[0]["achados"] if f["id"] == "COE-07"]
        self.assertEqual(len(achados), 1)
        self.assertIn("scripts/b.py", achados[0])

    # COE-08 -------------------------------------------------------------
    def test_skill_solta_e_pasta_sem_skill_md(self):
        self.w(".claude/skills/solta.md")
        self.w(".claude/skills/boa/SKILL.md")
        self.w(".claude/skills/ruim/leia.md")
        achados = self.ids("WARN")
        self.assertIn(("COE-08", ".claude/skills/solta.md"), achados)
        self.assertIn(("COE-08", ".claude/skills/ruim"), achados)
        self.assertNotIn(("COE-08", ".claude/skills/boa"), achados)

    # COE-09 -------------------------------------------------------------
    def test_config_ociosa(self):
        self.w(".eslintrc.json", "{}")
        self.w("package.json", '{"scripts":{}}')
        self.assertIn(("COE-09", ".eslintrc.json"), self.ids("INFO"))
        self.w("package.json", '{"scripts":{"lint":"eslint ."}}')
        self.assertNotIn(("COE-09", ".eslintrc.json"), self.ids("INFO"))

    # COE-10 -------------------------------------------------------------
    def test_workflow_inerte_descrito_como_ativo(self):
        self.w(".github/workflows/aud.yml", "# INERTE até Andraus ligar\nname: Auditor externo (loop)\n")
        self.w("AGENTS.md", "## 9. Auditor Externo\nCanal de auditoria ativo.\n")
        self.assertIn(("COE-10", ".github/workflows/aud.yml"), self.ids("WARN"))
        self.w("AGENTS.md", "## 9. Auditor Externo\nCanal de auditoria — PAUSADO.\n")
        self.assertNotIn(("COE-10", ".github/workflows/aud.yml"), self.ids("WARN"))

    # COE-13 -------------------------------------------------------------
    def test_readme_declara_spec_autorizada(self):
        self.w("README.md", "Próximo trabalho autorizado: **SPEC-001**\n")
        self.assertTrue(any(i == "COE-13" for i, _ in self.ids("WARN")))
        self.w("README.md", "Spec autorizada: ver ROADMAP.md\n")
        self.assertFalse(any(i == "COE-13" for i, _ in self.ids("WARN")))

    # Contrato -------------------------------------------------------------
    def test_exit_code_e_strict(self):
        self.w("README.md", "x\n")
        _, rc = self.run_it()
        self.assertEqual(rc, 0)
        self.w("tests/test_b.py")
        _, rc = self.run_it()
        self.assertEqual(rc, 1)          # COE-02 é ERRO

    def test_matriz(self):
        self.w("scripts/a.py", "x")
        r = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.d), "--matriz"],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertIn("| a.py |", r.stdout)

    def test_repositorio_real_nao_quebra(self):
        r = subprocess.run([sys.executable, str(SCRIPT), "--json"], capture_output=True, text=True, encoding="utf-8")
        self.assertIn("contagem", json.loads(r.stdout))


if __name__ == "__main__":
    unittest.main()
