"""Regressão da RULE-ECC-06 — python -m unittest tests/test_repo_research.py"""
import sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_repo_research as c  # noqa: E402

CAP = """Repositório: https://github.com/acme/tool
Plataforma: GitHub
Data de acesso: 2026-10-03
Estrelas: {stars}
Licença: {lic}
Último commit: {last}
Arquivado: {arch}
Alertas de segurança graves abertos: {alerts}
Dono: acme (organização)
Veredito de elegibilidade: {ver}
Trecho literal: "x"
"""


def good(**kw):
    d = dict(stars="1200", lic="MIT", last="2026-08-01", arch="não", alerts="0", ver="ELEGÍVEL")
    d.update(kw)
    return CAP.format(**d)


def make(research, caps):
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name) / "SPEC-099"
    (root / "sources").mkdir(parents=True)
    (root / "research.md").write_text(research, encoding="utf-8")
    for i, t in enumerate(caps):
        (root / "sources" / f"REPO-{i}.txt").write_text(t, encoding="utf-8")
    return tmp, root


SEC = "# Dossiê\n## Pesquisa em repositórios\n{body}\n## Outra seção\n"


class RepoResearch(unittest.TestCase):
    def run_case(self, body, caps):
        tmp, root = make(SEC.format(body=body), caps)
        with tmp:
            return c.check_spec_folder(root)

    def test_elegivel_passa(self):
        self.assertTrue(self.run_case("Adaptar https://github.com/acme/tool (ELEGÍVEL).", [good()])[0])

    def test_sem_secao_reprova(self):
        tmp, root = make("# Dossiê\nsem a seção\n", [])
        with tmp:
            self.assertFalse(c.check_spec_folder(root)[0])

    def test_poucas_estrelas_reprova_se_declarado_elegivel(self):
        ok, msg = self.run_case("https://github.com/acme/tool", [good(stars="120")])
        self.assertFalse(ok)
        self.assertIn("diverge da régua", msg)

    def test_nao_elegivel_declarado_ok_mas_exige_frase_de_nenhum(self):
        cap = good(stars="120", ver="NÃO ELEGÍVEL")
        self.assertFalse(self.run_case("Descartado https://github.com/acme/tool", [cap])[0])
        self.assertTrue(self.run_case(
            "Descartado https://github.com/acme/tool. Nenhum repositório elegível.", [cap])[0])

    def test_nao_elegivel_adotado_reprova(self):
        cap = good(stars="120", ver="NÃO ELEGÍVEL")
        ok, _ = self.run_case(
            "Adotar https://github.com/acme/tool\nNenhum repositório elegível.", [cap])
        self.assertFalse(ok)

    def test_licenca_fechada_arquivado_alerta_e_commit_antigo(self):
        for kw in (dict(lic="Proprietary"), dict(arch="sim"), dict(alerts="2"), dict(last="2024-01-01")):
            ok, msg = self.run_case("https://github.com/acme/tool", [good(ver="ELEGÍVEL", **kw)])
            self.assertFalse(ok, kw)

    def test_url_sem_captura_reprova(self):
        self.assertFalse(self.run_case("Adaptar https://gitlab.com/acme/x", [])[0])

    def test_nenhum_elegivel_explicito_sem_urls_passa(self):
        self.assertTrue(self.run_case("Nenhum repositório elegível encontrado (busca em 2026-10-03).", [])[0])

    def test_sem_urls_e_sem_frase_reprova(self):
        self.assertFalse(self.run_case("Pesquisamos bastante.", [])[0])

    def test_grandfathered_nao_e_alcancado(self):
        self.assertIn("SPEC-038", c.GRANDFATHERED)


if __name__ == "__main__":
    unittest.main()
