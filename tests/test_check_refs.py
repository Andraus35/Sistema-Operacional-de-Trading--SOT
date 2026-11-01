"""Testes do check_refs.py em repositório sintético — python -m unittest tests/test_check_refs.py"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_refs.py"


class Repo:
    def __init__(self, files):
        self.dir = Path(tempfile.mkdtemp())
        (self.dir / "scripts").mkdir()
        shutil.copy(SCRIPT, self.dir / "scripts" / "check_refs.py")
        for name, body in files.items():
            p = self.dir / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, encoding="utf-8")

    def run(self, *args):
        r = subprocess.run(
            [sys.executable, str(self.dir / "scripts" / "check_refs.py"), *args],
            capture_output=True, text=True, encoding="utf-8", cwd=self.dir,
        )
        return r.returncode, r.stdout

    def close(self):
        shutil.rmtree(self.dir, ignore_errors=True)


BASE = {
    "ROADMAP.md": "### SPEC-001 — Hypothesis\n",
    "backlog/RMR-001_Painel_Backlog.md": "| **BL-001** | x |\n",
    "governance/RULES.md": "RULE-AA-01 vale. INV-07 vale.\n",
}


class CheckRefs(unittest.TestCase):
    def go(self, extra, *args):
        repo = Repo({**BASE, **extra})
        self.addCleanup(repo.close)
        return repo.run(*args), repo

    def test_referencias_validas_passam(self):
        (code, out), _ = self.go({"backlog/x.md": "Ver SPEC-001, BL-001, RULE-AA-01, INV-07."})
        self.assertEqual(code, 0, out)

    def test_artefato_gerado_local_nao_e_caminho_quebrado(self):
        """A2.1: docs/mapa/mapa-projeto.json é gitignored; citá-lo em clone limpo não pode ser ERRO."""
        repo = Repo({**BASE, "governance/viva.md": "Veja `docs/mapa/mapa-projeto.json`.\n",
                     "governance/outra.md": "Veja `docs/mapa/outro-inexistente.json`.\n"})
        try:
            rc, out = repo.run()
            self.assertNotIn("mapa-projeto.json", out)
            self.assertIn("outro-inexistente.json", out)
        finally:
            repo.close()

    def test_placeholder_0nn_com_sufixo_separado_nao_e_regra_sem_definicao(self):
        """RULE-WRV-0nn (família de numeração) não é referência; RULE-WRV-07 inexistente continua sendo achado."""
        repo = Repo({**BASE, "governance/viva.md": "Contagem de `^RULE-WRV-0nn:` e de RULE-WRV-0NN.\n",
                     "governance/outra.md": "Cita RULE-WRV-07 e RULE-WRV-0x.\n"})
        try:
            rc, out = repo.run()
            self.assertNotIn("viva.md", out)
            self.assertIn("RULE-WRV-07", out)
        finally:
            repo.close()

    def test_ledger_gerado_nao_e_caminho_quebrado(self):
        """DHR-LEDGER-GERADO-001: o ledger é gerado e não versionado; citá-lo em doc vivo não pode ser ERRO."""
        repo = Repo({**BASE, "governance/viva.md": "Leia `governance/aprendizado/LEDGER-ACHADOS.md` com --stdout.\n",
                     "governance/outra.md": "Veja `governance/aprendizado/OUTRO-INEXISTENTE.md`.\n"})
        try:
            rc, out = repo.run()
            self.assertNotIn("LEDGER-ACHADOS", out)
            self.assertIn("OUTRO-INEXISTENTE", out)
        finally:
            repo.close()

    def test_bl_inexistente_em_doc_vivo_e_erro(self):
        (code, out), _ = self.go({"backlog/x.md": "Depende de BL-099."})
        self.assertEqual(code, 1)
        self.assertIn("BL sem definição: BL-099", out)

    def test_ata_congelada_nao_falha(self):
        (code, out), _ = self.go({"governance/DHR-X-001_ata.md": "cita BL-099"}, "--info")
        self.assertEqual(code, 0, out)
        self.assertIn("[INFO]", out)

    def test_referencia_prospectiva_e_info(self):
        (code, out), _ = self.go({"backlog/x.md": "SPEC-777 será redigida depois."}, "--info")
        self.assertEqual(code, 0, out)
        self.assertIn("[INFO]", out)

    def test_caminho_com_diretorio_inexistente_e_erro(self):
        (code, out), _ = self.go({"backlog/x.md": "Ver `governance/NAO-EXISTE.md`."})
        self.assertEqual(code, 1)
        self.assertIn("caminho inexistente", out)

    def test_nome_sem_diretorio_e_atalho(self):
        (code, out), _ = self.go({"backlog/x.md": "Ver `RULES.md` e `gerado.json`."})
        self.assertEqual(code, 0, out)

    def test_familia_de_regra_resolve(self):
        (code, out), _ = self.go({"backlog/x.md": "Família RULE-AA."})
        self.assertEqual(code, 0, out)

    def test_bloco_de_codigo_ignorado(self):
        (code, out), _ = self.go({"backlog/x.md": "```\nBL-099\n```\n"})
        self.assertEqual(code, 0, out)

    def test_grafo_exportado(self):
        (code, _), repo = self.go({"backlog/x.md": "Ver SPEC-001 e `governance/RULES.md`."}, "--graph", "g.json")
        g = json.loads((repo.dir / "g.json").read_text(encoding="utf-8"))
        self.assertIn({"from": "backlog/x.md", "to": "governance/RULES.md", "type": "path"}, g["edges"])
        self.assertIn({"from": "backlog/x.md", "to": "SPEC-001", "type": "id"}, g["edges"])

    def test_placeholder_de_id_ignorado(self):
        (code, out), _ = self.go({"backlog/x.md": "Registra INV-GAP-nnn e BL-xxx."})
        self.assertEqual(code, 0, out)

    def test_caminho_de_exemplo_e_info(self):
        (code, out), _ = self.go({"backlog/x.md": "por ex. leia `references/view.md` (e.g. exemplo)."})
        self.assertEqual(code, 0, out)

    def test_eua_futura_anunciada_por_ata_nao_e_erro(self):
        files = {"governance/DHR-EUA-E19a_ata.md": "A EUA-E20 (futura) institui a FASE RISK.",
                 "backlog/x.md": "Efetiva via EUA-E20."}
        (code, out), _ = self.go(files)
        self.assertEqual(code, 0, out)

    def test_numero_de_linha_correto_com_bloco_de_codigo(self):
        (code, out), _ = self.go({"backlog/x.md": "a\n```\nx\ny\n```\nBL-099\n"})
        self.assertEqual(code, 1)
        self.assertIn("backlog/x.md:6 ", out)

    def test_registro_de_achado_sem_lastro_nao_e_erro(self):
        (code, out), _ = self.go({"backlog/x.md": "Citação sem lastro: SPEC-888 removida."})
        self.assertEqual(code, 0, out)

    def test_strict_falha_em_warn(self):
        (code, out), _ = self.go({"backlog/x.md": "Usa RULE-ZZ-99."}, "--strict")
        self.assertEqual(code, 1, out)

    # --- falsos positivos medidos no repositório real (auditoria 2026-10-31, B10) ---
    def test_placeholder_0NN_nao_gera_warn(self):
        (code, out), _ = self.go({"specs/features/SPEC-001/checks.md": "Famílias RULE-CKG-0NN e RULE-KFH-0NN (modelo)."}, "--strict")
        self.assertEqual(code, 0, out)

    def test_caminho_absoluto_fora_do_repo_nao_e_sugerido_como_movido(self):
        files = {"README.md": "x", "specs/a.md": "Veja `/root/.ccr/README.md` no ambiente."}
        (code, out), _ = self.go(files, "--strict")
        self.assertEqual(code, 0, out)

    def test_comando_wc_usa_o_ultimo_argumento(self):
        files = {"specs/features/SPEC-001/plan.md": "x", "specs/features/SPEC-006/plan.md": "x",
                 "specs/features/SPEC-006/checks.md": "Rode `wc -l specs/features/SPEC-006/plan.md`."}
        (code, out), _ = self.go(files, "--strict")
        self.assertEqual(code, 0, out)

    def test_regra_real_sem_definicao_continua_alertando(self):
        (code, out), _ = self.go({"backlog/x.md": "Usa RULE-ZZ-99."}, "--strict")
        self.assertEqual(code, 1, out)

    def test_caminho_relativo_inexistente_continua_erro(self):
        (code, out), _ = self.go({"backlog/x.md": "veja `docs/inexistente.md`."})
        self.assertEqual(code, 1, out)

    # --- testes adversariais do patch (regressão: "/" não pode mascarar caminho do repositório) ---
    def test_adv_caminho_com_barra_inicial_inexistente_no_repo_continua_erro(self):
        (code, out), _ = self.go({"backlog/x.md": "veja `/docs/inexistente.md`."})
        self.assertEqual(code, 1, out)
        self.assertIn("caminho inexistente", out)

    def test_adv_caminho_com_barra_inicial_existente_resolve(self):
        # comportamento já existente antes do patch: "/docs/a.md" resolve para docs/a.md com aviso de caminho desatualizado (nunca ERRO)
        (code, out), _ = self.go({"docs/a.md": "x", "backlog/x.md": "veja `/docs/a.md`."})
        self.assertEqual(code, 0, out)
        self.assertIn("existe em docs/a.md", out)

    def test_adv_comando_cat_com_alvo_inexistente_continua_erro(self):
        (code, out), _ = self.go({"backlog/x.md": "rode `cat docs/inexistente.md`."})
        self.assertEqual(code, 1, out)

    def test_adv_placeholder_so_no_fim_da_regra(self):
        (code, out), _ = self.go({"backlog/x.md": "Usa RULE-ZZ-0NN-01."}, "--strict")
        self.assertEqual(code, 1, out)

    def test_adv_caminho_do_ambiente_em_home_tmp_usr_e_ignorado(self):
        (code, out), _ = self.go({"backlog/x.md": "veja `/home/u/a.md`, `/tmp/b.json`, `/usr/c.md`, `/etc/d.yml`."}, "--strict")
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
