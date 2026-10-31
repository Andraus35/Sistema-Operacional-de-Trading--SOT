"""Testes do fato_locais.py (proposta P7; informativo) — python -m unittest tests/test_fato_locais.py"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "fato_locais.py"
sys.path.insert(0, str(SCRIPT.parent))
import fato_locais as fl  # noqa: E402


def run(*args):
    r = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout


class Base(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())

    def arq(self, nome, texto):
        p = self.d / nome
        p.write_text(texto, encoding="utf-8")
        return str(p)


class TestUtilitarios(unittest.TestCase):
    def test_comprimir(self):
        self.assertEqual(fl.comprimir([1, 2, 3, 7, 9, 10]), "1-3, 7, 9-10")
        self.assertEqual(fl.comprimir([]), "")
        self.assertEqual(fl.comprimir([5, 5, 5]), "5")

    def test_expandir(self):
        self.assertEqual(fl.expandir("12, 40-42, 77"), {12, 40, 41, 42, 77})
        self.assertEqual(fl.expandir("12–14"), {12, 13, 14})  # travessão
        self.assertEqual(fl.expandir("lixo, x, 0, 5"), {5})

    def test_expandir_nao_explode_com_intervalo_gigante(self):
        self.assertEqual(fl.expandir("1-99999999"), set())


class TestTabela(Base):
    def test_acha_todas_as_ocorrencias_literais(self):
        p = self.arq("a.md", "RULE-X-01 aqui\nnada\nde novo RULE-X-01\nRULE-X-010 não é o mesmo\n")
        rc, out = run(p, "RULE-X-01")
        self.assertEqual(rc, 0)
        res = fl.tabela([p], ["RULE-X-01"])
        # literal: "RULE-X-010" contém "RULE-X-01" → linha 4 também casa (é literal, sem fronteira de palavra)
        self.assertEqual(res[0]["linhas"], [1, 3, 4])

    def test_regex_com_fronteira(self):
        p = self.arq("a.md", "RULE-X-01\nRULE-X-010\n")
        res = fl.tabela([p], [r"re:RULE-X-01\b"])
        self.assertEqual(res[0]["linhas"], [1])

    def test_caracteres_especiais_sao_literais(self):
        p = self.arq("a.md", "custo 1.900\noutro 1x900\n")
        res = fl.tabela([p], ["1.900"])
        self.assertEqual(res[0]["linhas"], [1])  # ponto literal: NÃO casa "1x900" (casaria se o fato fosse regex)

    def test_varios_arquivos(self):
        a = self.arq("a.md", "X\n")
        b = self.arq("b.md", "nada\nX\n")
        res = fl.tabela([a, b], ["X"])
        self.assertEqual([r["linhas"] for r in res], [[1], [2]])

    def test_fato_ausente_nao_quebra(self):
        p = self.arq("a.md", "abc\n")
        rc, out = run(p, "ZZZ")
        self.assertEqual(rc, 0)
        self.assertIn("—", out)

    def test_arquivo_com_bytes_invalidos(self):
        p = self.d / "a.md"
        p.write_bytes(b"ok FATO\n\xff\xfe quebrado FATO\n")
        res = fl.tabela([str(p)], ["FATO"])
        self.assertEqual(res[0]["linhas"], [1, 2])


class TestConferir(Base):
    def test_lista_correta(self):
        doc = self.arq("d.md", "ID-1 a\nx\nID-1 b\n")
        lista = self.arq("l.md", "| fato | linhas |\n|---|---|\n| `ID-1` | 1, 3 |\n")
        r = fl.conferir(lista, doc)
        self.assertEqual((r[0]["omitidas"], r[0]["sobrando"]), ([], []))

    def test_omissao_e_o_defeito_da_reapont_M_A(self):
        # a lista escrita à mão tem 5 das 10 menções
        doc = self.arq("d.md", "\n".join("ID-1" if i % 1 == 0 else "x" for i in range(10)) + "\n")
        lista = self.arq("l.md", "| fato | linhas |\n|---|---|\n| ID-1 | 1-5 |\n")
        r = fl.conferir(lista, doc)
        self.assertEqual(r[0]["omitidas"], [6, 7, 8, 9, 10])
        self.assertEqual(r[0]["sobrando"], [])

    def test_linha_obsoleta_sobrando(self):
        doc = self.arq("d.md", "ID-1\nx\n")
        lista = self.arq("l.md", "| fato | linhas |\n|---|---|\n| ID-1 | 1, 2 |\n")
        r = fl.conferir(lista, doc)
        self.assertEqual(r[0]["sobrando"], [2])

    def test_cabecalho_e_separador_nao_viram_fato(self):
        doc = self.arq("d.md", "x\n")
        lista = self.arq("l.md", "| Fato | Linhas |\n|:---|---:|\n| ID | 1 |\n")
        self.assertEqual([x["fato"] for x in fl.conferir(lista, doc)], ["ID"])

    def test_lista_vazia_nao_aprova_por_vazio(self):
        doc = self.arq("d.md", "ID-1\n")
        lista = self.arq("l.md", "texto sem tabela\n")
        rc, out = run("--conferir", lista, doc)
        self.assertEqual(rc, 0)
        self.assertIn("nenhuma linha de tabela", out)

    def test_strict_falha_quando_diverge(self):
        doc = self.arq("d.md", "ID-1\nID-1\n")
        lista = self.arq("l.md", "| fato | linhas |\n|---|---|\n| ID-1 | 1 |\n")
        self.assertEqual(run("--conferir", lista, doc)[0], 0)             # informativo por padrão
        self.assertEqual(run("--conferir", lista, doc, "--strict")[0], 1)  # --strict reprova

    def test_strict_passa_quando_confere(self):
        doc = self.arq("d.md", "ID-1\n")
        lista = self.arq("l.md", "| fato | linhas |\n|---|---|\n| ID-1 | 1 |\n")
        self.assertEqual(run("--conferir", lista, doc, "--strict")[0], 0)

    def test_json(self):
        doc = self.arq("d.md", "ID-1\n")
        lista = self.arq("l.md", "| fato | linhas |\n|---|---|\n| ID-1 | 1 |\n")
        rc, out = run("--conferir", lista, doc, "--json")
        self.assertEqual(json.loads(out.split("\nLEMBRETE")[0])[0]["reais"], [1])


class TestBaseGit(unittest.TestCase):
    def test_base_indisponivel_nao_quebra(self):
        d = Path(tempfile.mkdtemp()) / "fora.md"
        d.write_text("FATO\n", encoding="utf-8")
        rc, out = run(str(d), "FATO", "--base", "HEAD")
        self.assertEqual(rc, 0)
        self.assertIn("indisponível", out)

    def test_propagacao_parcial_no_repo_real(self):
        # usa um doc real versionado: README.md em HEAD vs HEAD (nada mudou ⇒ sem parcial)
        rc, out = run("README.md", "SOT", "--base", "HEAD")
        self.assertEqual(rc, 0)
        self.assertNotIn("PROPAGAÇÃO PARCIAL", out)

    def test_parcial_detectada_por_funcao(self):
        # simula: 2 ocorrências, 1 mudou e 1 igual ao base
        import fato_locais as m
        antigo = ["PARAM = 90", "PARAM = 90 (outro lugar)"]
        atual = ["PARAM = 120", "PARAM = 90 (outro lugar)"]
        ant = {a.strip() for a in antigo}
        occ = m.ocorrencias(atual, "PARAM")
        mudou = [n for n in occ if atual[n - 1].strip() not in ant]
        igual = [n for n in occ if atual[n - 1].strip() in ant]
        self.assertEqual((mudou, igual), ([1], [2]))


if __name__ == "__main__":
    unittest.main()
