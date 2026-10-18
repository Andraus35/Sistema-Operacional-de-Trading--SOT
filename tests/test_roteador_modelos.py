"""Testes do roteador determinístico de modelos (scripts/roteador_modelos.py) — DHR-ROTEAMENTO-003 + Emenda 1."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import roteador_modelos as r  # noqa: E402


def d(**k):
    return r.decidir(k)[0]


def cls(c, extra=""):
    return f"Audite o delta.\nCLASSE-TAREFA: {c}\n{extra}"


def plan(compl, n=10, mudar=()):
    """plan.md sintético com n blocos; `mudar` = índices com texto diferente."""
    out = [f"# Plan\nComplexidade: {compl}\n"]
    for i in range(n):
        out.append(f"## Bloco {i}\ntexto {'novo' if i in mudar else 'velho'} {i}\n")
    return "\n".join(out)


class Roteador(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self._root = r.ROOT
        r.ROOT = self.root
        (self.root / "crit.md").write_text(plan("CRITICAL"), encoding="utf-8")
        (self.root / "med.md").write_text(plan("MEDIUM"), encoding="utf-8")
        (self.root / "crit_base.md").write_text(plan("CRITICAL"), encoding="utf-8")
        (self.root / "crit_poucas.md").write_text(plan("CRITICAL", mudar=(1,)), encoding="utf-8")
        (self.root / "crit_muitas.md").write_text(plan("CRITICAL", mudar=range(8)), encoding="utf-8")
        (self.root / "parecer.md").write_text("parecer", encoding="utf-8")
        (self.root / "fm.json").write_text(json.dumps({"achados": [achado()]}), encoding="utf-8")
        (self.root / "fc.json").write_text(json.dumps({"achados": [achado(natureza="conferencia")]}), encoding="utf-8")

    def tearDown(self):
        r.ROOT = self._root
        self.tmp.cleanup()

    def test_classe_derivada_do_alvo(self):
        self.assertEqual(r.derivar_classe("especificador", ""), "O")
        self.assertEqual(r.derivar_classe("revisor", "ALVO: crit.md"), "S3")
        self.assertEqual(r.derivar_classe("revisor", "ALVO: med.md"), "S2")
        self.assertIsNone(r.derivar_classe("revisor", ""))
        self.assertIsNone(r.derivar_classe("revisor", "ALVO: ../fora.md"))
        self.assertIsNone(r.derivar_classe("revisor", "ALVO: nao_existe.md"))

    def test_delta_aplicavel_so_com_base_parecer_e_menos_da_metade(self):
        base = "BASE: crit_base.md\nPARECER: parecer.md"
        self.assertEqual(r.derivar_classe("revisor", "ALVO: crit_poucas.md\n" + base), "S2")
        self.assertEqual(r.derivar_classe("revisor", "ALVO: crit_muitas.md\n" + base), "S3")  # > metade => integral
        self.assertEqual(r.derivar_classe("revisor", "ALVO: crit_poucas.md\nBASE: crit_base.md"), "S3")  # sem parecer anterior
        (self.root / "med_base.md").write_text(plan("MEDIUM"), encoding="utf-8")
        self.assertEqual(r.derivar_classe("revisor", "ALVO: crit_poucas.md\nBASE: med_base.md\nPARECER: parecer.md"), "S3")  # Complexidade mudou

    def test_ficha_define_s1_e_m(self):
        self.assertEqual(r.derivar_classe("revisor", "FICHA: fc.json"), "S1")
        self.assertEqual(r.derivar_classe("especificador", "FICHA: fm.json"), "M")
        self.assertEqual(r.derivar_classe("revisor", "FICHA: fm.json"), "M")

    def test_declaracao_deve_igualar_derivada(self):
        ok = lambda c, ex, m="sonnet": d(subagent_type="Revisor SOT", model=m, prompt=cls(c, ex))
        self.assertEqual(ok("S3", "ALVO: crit.md", "opus"), "permitir")
        self.assertEqual(ok("S2", "ALVO: crit.md"), "negar")          # declarou S2, derivada S3 (rebaixar o Revisor)
        self.assertEqual(ok("S2", "ALVO: med.md"), "permitir")
        self.assertEqual(ok("S3", "ALVO: med.md", "opus"), "negar")   # declarou S3, derivada S2 (gasto indevido)
        self.assertEqual(ok("S2", ""), "negar")                       # sem ALVO: não derivável
        self.assertEqual(ok("S1", "FICHA: fc.json"), "permitir")
        self.assertEqual(ok("S2", "FICHA: fc.json"), "negar")

    def test_abertura_de_spec_e_desenho_e_ficha_mecanica_nao_vai_a_agente(self):
        self.assertEqual(d(subagent_type="Especificador SOT", model="opus", prompt=cls("O")), "permitir")
        self.assertEqual(d(subagent_type="Especificador SOT", prompt=cls("O", "FICHA: fm.json")), "negar")
        self.assertEqual(d(subagent_type="Especificador SOT", model="opus", prompt=cls("O", "FICHA: fm.json")), "negar")

    def test_especificador_e_revisor_sem_parametro(self):
        self.assertEqual(d(subagent_type="Revisor SOT", prompt="audite"), "permitir")
        self.assertEqual(d(subagent_type="Especificador SOT"), "permitir")

    def test_model_sem_classe_negado_fail_closed(self):
        for t in ("Revisor SOT", "Especificador SOT"):
            self.assertEqual(d(subagent_type=t, model="haiku"), "negar")
            self.assertEqual(d(subagent_type=t, model="opus"), "negar")
            self.assertEqual(d(subagent_type=t, model="sonnet", prompt="CLASSE-TAREFA: XX"), "negar")

    def test_effort_sempre_negado(self):
        for t in ("Revisor SOT", "Especificador SOT"):
            self.assertEqual(d(subagent_type=t, effort="low"), "negar")
            self.assertEqual(d(subagent_type=t, effort="low", model="sonnet", prompt=cls("S2", "ALVO: med.md")), "negar")

    def test_model_igual_a_tabela_da_classe_permitido(self):
        self.assertEqual(d(subagent_type="Revisor SOT", model="sonnet", prompt=cls("S1", "FICHA: fc.json")), "permitir")
        self.assertEqual(d(subagent_type="Revisor SOT", model="claude-sonnet-5-5", prompt=cls("S2", "ALVO: med.md")), "permitir")
        self.assertEqual(d(subagent_type="Revisor SOT", model="opus", prompt=cls("S3", "ALVO: crit.md")), "permitir")
        self.assertEqual(d(subagent_type="Especificador SOT", model="opus", prompt=cls("O")), "permitir")

    def test_model_diferente_da_tabela_negado(self):
        self.assertEqual(d(subagent_type="Revisor SOT", model="opus", prompt=cls("S2", "ALVO: med.md")), "negar")
        self.assertEqual(d(subagent_type="Especificador SOT", model="sonnet", prompt=cls("O")), "negar")
        self.assertEqual(d(subagent_type="Revisor SOT", model="claude-sonnet-4-6", prompt=cls("S2", "ALVO: med.md")), "negar")
        self.assertEqual(d(subagent_type="Revisor SOT", model="haiku", prompt=cls("S1", "FICHA: fc.json")), "negar")

    def test_classe_incompativel_com_agente_negada_mesmo_sem_model(self):
        self.assertEqual(d(subagent_type="Revisor SOT", prompt=cls("O")), "negar")
        self.assertEqual(d(subagent_type="Especificador SOT", prompt=cls("S2")), "negar")

    def test_classe_m_nao_vai_a_agente(self):
        self.assertEqual(d(subagent_type="Revisor SOT", prompt=cls("M")), "negar")
        self.assertEqual(d(subagent_type="Especificador SOT", model="opus", prompt=cls("M")), "negar")

    def test_classe_ambigua_ou_invalida(self):
        self.assertIsNone(r.extrair_classe("CLASSE-TAREFA: S1\nCLASSE-TAREFA: O"))
        self.assertIsNone(r.extrair_classe("texto CLASSE-TAREFA: S1 no meio"))
        self.assertEqual(r.extrair_classe("a\nCLASSE-TAREFA: s2\n"), "S2")
        self.assertEqual(d(subagent_type="Revisor SOT", model="sonnet", prompt="CLASSE-TAREFA: S2\nCLASSE-TAREFA: S2\nALVO: med.md"), "permitir")
        self.assertEqual(d(subagent_type="Revisor SOT", model="sonnet", prompt="CLASSE-TAREFA: S1\nCLASSE-TAREFA: S2"), "negar")
        self.assertEqual(d(subagent_type="Revisor SOT", model="sonnet", prompt="CLASSE-TAREFA: S1\nCLASSE-TAREFA: O"), "negar")

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

    def test_falha_interna_com_override_nega(self):
        orig = r._decidir_ac
        r._decidir_ac = lambda *a: (_ for _ in ()).throw(RuntimeError("x"))
        try:
            self.assertEqual(d(subagent_type="Revisor SOT", model="sonnet", prompt=cls("S2")), "negar")
            self.assertEqual(d(subagent_type="Revisor SOT"), "permitir")
        finally:
            r._decidir_ac = orig


def achado(**k):
    base = {"id": "A1", "arquivo": "x.md", "linha": 2, "antigo": "um", "novo": "dois", "condicao": "linha 2 == dois"}
    base.update(k)
    return base


class Classificacao(unittest.TestCase):
    def test_achado_mecanico_e_m(self):
        self.assertEqual(r.classificar_achado(achado()), "M")

    def test_sem_localizacao_ou_condicao_escala_a_o(self):
        for k in ({"linha": None}, {"linha": 0}, {"arquivo": ""}, {"antigo": ""}, {"condicao": ""}, {"novo": "um"}):
            self.assertEqual(r.classificar_achado(achado(**k)), "O", k)

    def test_criar_regra_campo_mecanismo_nao_e_m(self):
        self.assertEqual(r.classificar_achado(achado(cria_mecanismo=True)), "O")
        self.assertEqual(r.classificar_achado(achado(novo="vale RULE-ZZ-99")), "O")
        self.assertEqual(r.classificar_achado(achado(antigo="RULE-ZZ-99", novo="RULE-ZZ-99 ok")), "M")

    def test_natureza_auditoria(self):
        self.assertEqual(r.classificar_achado(achado(natureza="conferencia")), "S1")
        self.assertEqual(r.classificar_achado(achado(natureza="auditoria")), "S2")
        self.assertEqual(r.classificar_achado(achado(natureza="integral")), "S3")

    def test_agrupar_escala_o_que_estoura_o_teto(self):
        grupos = r.agrupar([achado(id=f"A{i}", arquivo=f"f{i % 3}.md") for i in range(3)])
        self.assertEqual(grupos["M"], ["A0", "A1"])
        self.assertEqual(grupos["O"], ["A2"])
        grande = achado(id="G", antigo="\n".join("l" for _ in range(11)), novo="n")
        self.assertEqual(r.agrupar([grande]), {"O": ["G"]})


class Conferir(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "t@t")
        self.git("config", "user.name", "t")
        (self.root / "x.md").write_text("a\num\nc\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "i")

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *a):
        subprocess.run(["git", *a], cwd=self.root, check=True, capture_output=True)

    def ficha(self):
        return {"achados": [achado()]}

    def test_delta_so_nas_linhas_listadas_ok(self):
        (self.root / "x.md").write_text("a\ndois\nc\n", encoding="utf-8")
        self.assertEqual(r.conferir(self.ficha(), root=self.root), [])

    def test_linha_extra_alterada_escala(self):
        (self.root / "x.md").write_text("A\ndois\nc\n", encoding="utf-8")
        self.assertTrue(any("fora da ficha" in p for p in r.conferir(self.ficha(), root=self.root)))

    def test_insercao_escala(self):
        (self.root / "x.md").write_text("a\ndois\nnova\nc\n", encoding="utf-8")
        self.assertTrue(r.conferir(self.ficha(), root=self.root))

    def test_texto_novo_ausente_escala(self):
        (self.root / "x.md").write_text("a\ntres\nc\n", encoding="utf-8")
        self.assertTrue(any("não contém" in p for p in r.conferir(self.ficha(), root=self.root)))

    def test_nada_alterado_escala(self):
        self.assertTrue(r.conferir(self.ficha(), root=self.root))

    def test_ficha_sem_m(self):
        self.assertTrue(r.conferir({"achados": [achado(linha=None)]}, root=self.root))

    def test_cli_classificar(self):
        f = self.root / "f.json"
        f.write_text(json.dumps(self.ficha()), encoding="utf-8")
        out = subprocess.run([sys.executable, str(Path(r.__file__)), "classificar", str(f)], capture_output=True, text=True)
        self.assertEqual(json.loads(out.stdout), {"M": ["A1"]})


if __name__ == "__main__":
    unittest.main()
