"""merge_ready.py (DHR-MERGE-001): critérios determinísticos de 'pronto para mesclar' — função pura + coleta com API simulada."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import merge_ready as M  # noqa: E402

PR = {"number": 7, "draft": False, "mergeable_state": "clean", "head_sha": "abc", "html_url": "u", "title": "t"}
OK = {"name": "CI", "status": "completed", "conclusion": "success"}


def info(**k):
    base = {"pr": dict(PR), "head_local": "abc", "sujo": False, "checks": [dict(OK)], "arquivos": ["a.md"], "donos": []}
    base.update(k)
    return base


class Avaliar(unittest.TestCase):
    def test_pronto(self):
        e, mot, extra = M.avaliar(info())
        self.assertEqual((e, mot), ("PRONTO", []))
        self.assertEqual(extra["cabeca"], "abc")

    def test_sem_pr(self):
        self.assertEqual(M.avaliar(info(pr=None))[0], "NAO_PRONTO")

    def test_cada_criterio_reprova(self):
        casos = [
            info(pr={**PR, "draft": True}), info(pr={**PR, "mergeable_state": "dirty"}), info(pr={**PR, "mergeable_state": "blocked"}),
            info(head_local="zzz"), info(sujo=True), info(checks=[]),
            info(checks=[{"name": "CI", "status": "in_progress", "conclusion": None}]),
            info(checks=[dict(OK), {"name": "x", "status": "completed", "conclusion": "failure"}]),
        ]
        for c in casos:
            self.assertEqual(M.avaliar(c)[0], "NAO_PRONTO", c)

    def test_neutral_e_skipped_contam_como_ok(self):
        c = [dict(OK), {"name": "n", "status": "completed", "conclusion": "neutral"}, {"name": "s", "status": "completed", "conclusion": "skipped"}]
        self.assertEqual(M.avaliar(info(checks=c))[0], "PRONTO")

    def test_arquivos_de_andraus_sao_informativos(self):
        e, _, extra = M.avaliar(info(arquivos=["scripts/roteador_modelos.py", "x.md"], donos=["scripts/roteador_modelos.py"]))
        self.assertEqual(e, "PRONTO")
        self.assertEqual(extra["arquivos_de_andraus"], ["scripts/roteador_modelos.py"])


class Coleta(unittest.TestCase):
    def runner(self, status=""):
        saidas = {"--abbrev-ref": "meu-ramo", "get-url": "https://github.com/o/r", "status": status}

        def run(args, cwd=None, timeout=20):
            if "--abbrev-ref" in args:
                return 0, saidas["--abbrev-ref"], ""
            if "get-url" in args:
                return 0, saidas["get-url"], ""
            if args[:2] == ["git", "rev-parse"]:
                return 0, "abc", ""
            return 0, saidas["status"], ""
        return run

    def test_coleta_monta_o_estado(self):
        chamadas = []

        def api(path, timeout=20):
            chamadas.append(path)
            if "check-runs" in path:
                return {"check_runs": [dict(OK)]}
            if path.endswith("/files?per_page=100"):
                return [{"filename": "a.md"}]
            if "pulls?state=open" in path:
                return [{"number": 7}]
            return {"number": 7, "draft": False, "mergeable_state": "clean", "head": {"sha": "abc"}, "base": {"ref": "main"}, "html_url": "u", "title": "t"}
        i = M.coletar(Path(M.ROOT), api=api, runner=self.runner())
        self.assertEqual(M.avaliar(i)[0], "PRONTO")
        self.assertIn("repos/o/r/pulls?state=open&head=o:meu-ramo&per_page=5", chamadas)

    def test_sem_pr_aberto(self):
        i = M.coletar(Path(M.ROOT), api=lambda p, timeout=20: [], runner=self.runner())
        self.assertIsNone(i["pr"])

    def test_arvore_suja(self):
        i = M.coletar(Path(M.ROOT), api=lambda p, timeout=20: [], runner=self.runner(" M x"))
        self.assertTrue(i["sujo"])

    def test_slug(self):
        self.assertEqual(M.repo_slug("https://github.com/Andraus35/Sistema.git"), "Andraus35/Sistema")
        self.assertEqual(M.repo_slug("git@github.com:o/r.git"), "o/r")
        self.assertIsNone(M.repo_slug(""))

    def test_erro_de_api_e_indeterminado_exit_2(self):
        orig = M.coletar
        M.coletar = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("rede"))
        try:
            self.assertEqual(M.main(["--json"]), 2)
        finally:
            M.coletar = orig


if __name__ == "__main__":
    unittest.main()
