"""Regressão do gate_extra (auditoria independente SPEC-006) — python -m unittest tests/test_gate_extra.py
Cada teste reproduz uma mutação que passava como PASSOU_D e agora deve ser acusada (e o caso legítimo não)."""
import sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import gate_extra as g  # noqa: E402

STATUS = "| Status | **CANDIDATO** — H-001 permanece ABERTA; WF-D03, ECC-03-001 e CKG-STRUCT-ORIGIN-001 seguem ABERTAS. |\n"


class Citacoes(unittest.TestCase):
    def test_intervalo_fora_do_arquivo(self):  # M05
        self.assertTrue(g.citacoes_arquivo_linha("ver CEM-001 l.9608-9615", ROOT))

    def test_regra_citada_no_bloco_da_basPec_e_nao_na_regra(self):  # A-06
        self.assertTrue(g.citacoes_arquivo_linha("SPEC-004 RULE-CBP-007 l.543-558", ROOT))

    def test_regra_citada_no_intervalo_da_definicao(self):
        self.assertFalse(g.citacoes_arquivo_linha("SPEC-004 RULE-CBP-007 l.264-270", ROOT))

    def test_regra_citada_dentro_do_proprio_bloco(self):
        self.assertFalse(g.citacoes_arquivo_linha("SPEC-004 RULE-CBP-004 l.243-244", ROOT))

    def test_id_de_backlog_fora_do_intervalo(self):  # A-07
        self.assertTrue(g.citacoes_arquivo_linha("RMR-001 l.128 (BL-029)", ROOT))


class Contagens(unittest.TestCase):
    DOC = "\n".join(["### BASpec-X-001 a", "### BASpec-X-002 b", "### EC-X-001 c", "texto"])

    def test_contagem_errada(self):  # M04
        self.assertTrue(g.contagens_declaradas(self.DOC + "\nA Spec tem 3 BASpecs e 1 EC.\n"))

    def test_contagem_certa_e_historico_isento(self):
        t = self.DOC + "\nA Spec tem 2 BASpecs e 1 EC.\n| 1.0 | x | 13 BASpecs; 6 EC |\n"
        self.assertFalse(g.contagens_declaradas(t))

    def test_ec_cog_nao_e_contagem(self):
        self.assertFalse(g.contagens_declaradas(self.DOC + "\nCONSTITUTION l.233 EC-COG-003\n"))


class Enforcement(unittest.TestCase):
    def doc(self, level):
        return "Knowledge Graph\n### EC-CKG-001 — Escrita de nó no KG permanente [E3]\n```\nLEVEL        : " + level + "\n```\n"

    def test_piso_rebaixado(self):  # M09
        self.assertTrue(g.piso_enforcement(self.doc("E1")))

    def test_piso_ok(self):
        self.assertFalse(g.piso_enforcement(self.doc("E3")))


class DecisoesAbertas(unittest.TestCase):
    def test_fechamento_perto_de_aberta_em_outra_oracao(self):  # M01b
        t = STATUS + "H-001 está aberta aqui. Depois: H-001 FECHADA pelo plano.\n"
        self.assertTrue(g.decisoes_abertas_fechadas(t))

    def test_ids_fora_do_padrao_antigo(self):  # M02
        t = STATUS + "WF-D03 FECHADA; CKG-STRUCT-ORIGIN-001 resolvida; ECC-03-001 resolvida.\n"
        self.assertEqual(len(g.decisoes_abertas_fechadas(t)), 3)

    def test_negacao_na_mesma_oracao_passa(self):
        t = STATUS + "Este Plan NÃO fecha H-001; segue aberta.\nH-001 permanece ABERTA, nada foi resolvido.\n"
        self.assertFalse(g.decisoes_abertas_fechadas(t))


class Invariantes(unittest.TestCase):
    def test_custo_no_vetor(self):  # M06
        self.assertTrue(g.invariantes_estritos("Confiança e custo alimentam o Conviction Vector."))

    def test_ict_cria_hipotese_mesmo_citando_inv(self):  # M07b
        self.assertTrue(g.invariantes_estritos("O ICT Specialist cria sub-hipóteses (INV-02 revisto)."))

    def test_negacao_passa(self):
        self.assertFalse(g.invariantes_estritos("O ICT nunca cria hipóteses (INV-02)."))


class Assertivas(unittest.TestCase):
    PLAN = "a regra RULE-CBP-007 l.264-270 fica\nem duas linhas"

    def test_present_e_absent_ok(self):
        c = '| x | **Corrigido** assert-present:"RULE-CBP-007 l.264-270" assert-absent:"l.543-558" |'
        self.assertFalse(g.assertivas_checks(c, self.PLAN))

    def test_absent_falha(self):  # A-06 (declarado corrigido, não aplicado)
        c = '| x | **Corrigido** assert-absent:"l.264-270" |'
        self.assertTrue(g.assertivas_checks(c, self.PLAN))

    def test_present_falha_e_texto_quebrado_em_linha_ok(self):
        c = '| assert-present:"fica em duas linhas" | assert-present:"nada disso" |'
        self.assertEqual(len(g.assertivas_checks(c, self.PLAN)), 1)

    def test_descricao_do_formato_nao_conta(self):
        self.assertFalse(g.assertivas_checks('formato: assert-absent:"..." e assert-present:"..."', self.PLAN))

    def test_corrigido_sem_assertiva(self):
        self.assertTrue(g.corrigidos_sem_assertiva("| a | **Corrigido** — feito |"))


class CamposPorBloco(unittest.TestCase):
    BASE = "### BASpec-X-001 — a\nQUANDO x\nENTÃO y\nPORQUE z\nREFERÊNCIA r\nVERIFICADO POR t\n"

    def test_completo(self):
        self.assertFalse(g.campos_por_bloco(self.BASE))

    def test_basPec_sem_verificado_por_mesmo_havendo_o_campo_em_outro_bloco(self):  # M03
        t = self.BASE.replace("VERIFICADO POR t\n", "") + "### BASpec-X-002 — b\nQUANDO x\nENTÃO y\nPORQUE z\nREFERÊNCIA r\nVERIFICADO POR t\n"
        r = g.campos_por_bloco(t)
        self.assertEqual(len(r), 1)
        self.assertIn("BASpec-X-001", r[0][1])

    def test_ec_sem_level(self):
        self.assertTrue(g.campos_por_bloco("### EC-X-001 — a\nCAPABILITY c\nEFFECT e\nPRECOND p\nPOSTCOND q\n"))


class Candidato(unittest.TestCase):
    def test_status(self):
        self.assertTrue(g._eh_candidato("| Status | **CANDIDATO** — x |"))
        self.assertTrue(g._eh_candidato("| Status | BASELINE v1.7 — ERRATA v1.8 PROPOSTA (aguarda) |"))
        self.assertFalse(g._eh_candidato("| Status | **HOMOLOGADA — BASELINE v1.7** |"))


class Teto(unittest.TestCase):
    def test_gate_fora_da_sessao_do_revisor_limita(self):
        teto, mot = g.teto_de_veredito("SPEC-006", STATUS, ROOT, gate_executado_pelo_revisor=True)
        self.assertEqual(teto, "CONFORME condicional")  # H-001 aberta bloqueia a SPEC-006 (revisor.md §8)
        self.assertTrue(any("H-001" in m for m in mot))

    def test_sem_bloqueio_e_com_gate_no_revisor(self):
        teto, mot = g.teto_de_veredito("SPEC-001", "| Status | x |\n", ROOT, gate_executado_pelo_revisor=True)
        self.assertEqual((teto, mot), ("CONFORME", []))


if __name__ == "__main__":
    unittest.main()
