"""Testes do gate fundido do Revisor (scripts/revisor_gate.py) — DHR-AUDITOR-EXTERNO-009, fase F1."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import revisor_gate as rg  # noqa: E402


def cods(linha):
    return {s["codigo"] for s in rg.sinais_h(linha)}


class TestBaselinesEIds(unittest.TestCase):
    def test_baselines_ausentes(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(rg.checar_baselines(d), rg.BASELINES)
            (Path(d) / "governance").mkdir()
            for b in rg.BASELINES:
                (Path(d) / b).write_text("x")
            self.assertEqual(rg.checar_baselines(d), [])

    def test_ids_canonicos(self):
        achados = rg.checar_ids_canonicos("Baselines | CHM-009, CEM-004 e CHM-001")
        self.assertEqual({i for _, i in achados}, {"CHM-009", "CEM-004"})

    def test_ids_abreviados_e_de_regra_nao_acusam(self):
        self.assertEqual(rg.checar_ids_canonicos("ver RULE-CEE-003 e RULE-003/SY-003/CEE-004"), [])


class TestSinaisH(unittest.TestCase):
    def test_detecta(self):
        casos = {
            "H-ORDEM": "O SOT executa a ordem diretamente na corretora depois que o Risk Agent aprova.",
            "H-ICT-HIPOTESE": "O ICT cria sub-hipóteses quando detecta uma killzone.",
            "H-CUSTO-VETOR": "O custo de execução entra com peso de 5% no Conviction Vector.",
            "H-REMOCAO": "hipóteses ARCHIVED são removidas após 30 dias.",
            "H-PARENT-ID": "SMC e Fibonacci criam sub-hipóteses sem necessidade de `parent_id`.",
            "H-EVENTBUS": "O Event Bus é a fonte de verdade do estado, e o Blackboard apenas replica.",
            "H-REGIME-GATE": "O regime de mercado é um gate: regime adverso veta o sinal.",
            "H-SYNTH-SEPARADO": "O Synthesis Agent permanece como agente separado, depois do Conviction Engine.",
            "H-VETOR-1X": "Conviction Vector calculado | uma única vez, ao final da Fase 2",
            "H-REFUTED-SINAL": "Uma hipótese REFUTED pode gerar sinal se o score for ≥ 7/9.",
        }
        for cod, linha in casos.items():
            self.assertIn(cod, cods(linha), cod)

    def test_versoes_corretas_nao_acusam(self):
        corretas = [
            "O SOT não executa ordens; entrega o Signal Package ao Bot Trade Finance.",
            "O ICT não cria hipótese de nenhum tipo.",
            "O custo de execução NUNCA entra no Conviction Vector (CEE-001 §10, Salvaguarda 4).",
            "nada é deletado, e a hipótese refutada segue para ARCHIVED",
            "O Event Bus é uma camada fina de notificação de mudança; o Blackboard guarda o estado.",
            "O regime de mercado é a dimensão temporal; não é gate nem veto.",
            "O Synthesis Agent foi absorvido pelo Manager Agent.",
            "Uma hipótese REFUTED não gera sinal.",
            "SMC e Fibonacci criam sub-hipóteses com `parent_id` apontando para a PRIMARY",
        ]
        for linha in corretas:
            self.assertEqual(cods(linha), set(), linha)

    def test_contexto_adversarial_nao_acusa(self):
        self.assertEqual(cods("### ADV-CF-13 — Regime tratado como gate/veto (viola WF-C04) [Q-A9]"), set())
        self.assertEqual(cods("DADO        Spec-filha do ICT que cria hipótese estrutural"), set())


class TestRodar(unittest.TestCase):
    def test_documento_fora_de_specs_nao_tem_gate_de_estrutura(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "canon").mkdir()
            (Path(d) / "canon" / "CHM-001-x.md").write_text("x")
            (Path(d) / "governance").mkdir()
            for b in rg.BASELINES:
                (Path(d) / b).write_text("x")
            doc = Path(d) / "doc.md"
            doc.write_text("O SOT executa a ordem diretamente na corretora.\nR:R mínimo 2.0\n", encoding="utf-8")
            ev, reprovado = rg.rodar(doc, rapido=True, root=d)
            self.assertFalse(reprovado)                                    # nenhum D bloqueante falhou
            nomes = {g["nome"]: g for g in ev["gates"]}
            self.assertIn("NÃO APLICÁVEL", nomes["validate_spec_sot"]["tail"][0])
            self.assertEqual(nomes["check_invariants"]["exit_code"], 1)    # R:R 2.0 acusado (informativo)
            self.assertEqual([s["codigo"] for s in ev["sinais_H"]], ["H-ORDEM"])
            self.assertIn("ref", ev["sinais_H"][0])

    def test_baseline_ausente_reprova_em_D(self):
        with tempfile.TemporaryDirectory() as d:
            doc = Path(d) / "doc.md"
            doc.write_text("texto\n")
            ev, reprovado = rg.rodar(doc, rapido=True, root=d)
            self.assertTrue(reprovado)
            self.assertIn("REPROVADO_D", ev["veredito_D"])

    def test_spec_real_passa_em_D_e_sem_sinais(self):
        ev, reprovado = rg.rodar(ROOT / "specs" / "features" / "SPEC-001" / "plan.md", rapido=True, root=ROOT)
        self.assertFalse(reprovado, ev["gates"])
        self.assertEqual(ev["sinais_H"], [])

    def test_todas_as_specs_vigentes_sem_falso_alarme(self):
        for plan in sorted((ROOT / "specs" / "features").glob("*/plan.md")):
            ev, reprovado = rg.rodar(plan, rapido=True, root=ROOT)
            self.assertFalse(reprovado, f"{plan}: {[g for g in ev['gates'] if g['exit_code']]}")
            self.assertEqual(ev["sinais_H"], [], f"{plan}: {ev['sinais_H']}")


class TestDetectoresMedicaoSpec006(unittest.TestCase):
    """Detectores D informativos nascidos da medição do Revisor na SPEC-006 (2026-10-12)."""

    def _root(self, d, cem="Campos: Lineage, Status, gate_id", rmr=None):
        r = Path(d)
        (r / "canon").mkdir()
        (r / "canon" / "CEM-001_x.md").write_text(cem, encoding="utf-8")
        (r / "backlog").mkdir()
        (r / "backlog" / "RMR-001_Painel_Backlog.md").write_text(
            rmr or "| **BL-029** | t | Adaptação | a | g | acao | **Em espera** (x) ~~ATIVADO~~ | o |\n"
                   "| **BL-003** | t | Adaptação | a | g | acao | **ATIVADO** (y) | o |\n", encoding="utf-8")
        return r

    def test_campo_inexistente_no_baseline_acusa(self):
        with tempfile.TemporaryDirectory() as d:
            r = self._root(d)
            self.assertEqual(rg.campos_atribuidos_baseline("O `lineage_ref` é do CEM-001 (Cap.5).", r), [(1, "lineage_ref", "CEM-001")])
            self.assertEqual(rg.campos_atribuidos_baseline("O campo `gate_record` atribuído ao CEM-001.", r), [(1, "gate_record", "CEM-001")])

    def test_campo_existente_ou_proposta_nao_acusa(self):
        with tempfile.TemporaryDirectory() as d:
            r = self._root(d, cem="Campos: lineage_ref, Status")
            self.assertEqual(rg.campos_atribuidos_baseline("O `lineage_ref` é do CEM-001.", r), [])
            r2 = self._root(tempfile.mkdtemp())
            self.assertEqual(rg.campos_atribuidos_baseline("[PROPOSTA] `lineage_ref` do CEM-001 é campo local novo.", r2), [])

    def test_estado_backlog_so_em_candidato(self):
        with tempfile.TemporaryDirectory() as d:
            r = self._root(d)
            cand = "| Status | **CANDIDATO — aguarda** |\n- BL-029 permanece `ATIVADO`, independente.\n"
            self.assertEqual(rg.estado_backlog(cand, r), [(2, "BL-029", "ATIVADO", "Em espera")])
            homolog = "| Status | **BASELINE v1.0** |\n- BL-029 permanece `ATIVADO`, independente.\n"
            self.assertEqual(rg.estado_backlog(homolog, r), [])
            ok = "| Status | **CANDIDATO** |\n- BL-029 `Em espera`, independente.\n- BL-003 não promovido a ATIVADO.\n"
            self.assertEqual(rg.estado_backlog(ok, r), [])

    def test_refs_variantes(self):
        self.assertEqual(rg.refs_variantes("Negação: ADV-CKG-06, T04-neg.\n"), [(1, "T04-neg")])
        self.assertEqual(rg.refs_variantes("### T04-neg — definido\nver T04-neg\n"), [])
        self.assertEqual(rg.refs_variantes("T04 e ADV-CKG-06 e EC-CKG-001 normais\n"), [])

class TestContratoSchemas(unittest.TestCase):
    """Absorção do ex-subagente `sot-schema-validator` (DHR-AUDITOR-EXTERNO-016)."""

    def test_schemas_vigentes_cumprem_o_contrato(self):
        self.assertEqual(rg.checar_schemas(), [])

    def test_adulteracao_e_detectada(self):
        import json, shutil, tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as t:
            shutil.copytree(rg.ROOT / "schemas", Path(t) / "schemas")
            f = Path(t) / "schemas" / "synthesis.output.json"
            s = json.loads(f.read_text(encoding="utf-8"))
            s["properties"]["sinal"]["enum"].remove("NEUTRO")
            s["properties"]["score_total"]["maximum"] = 12
            f.write_text(json.dumps(s), encoding="utf-8")
            i = Path(t) / "schemas" / "ict.input.json"
            d = json.loads(i.read_text(encoding="utf-8"))
            d["properties"]["approved_hypothesis"]["type"] = "object"
            i.write_text(json.dumps(d), encoding="utf-8")
            txt = " | ".join(rg.checar_schemas(t))
        self.assertIn("score_total", txt)
        self.assertIn("NEUTRO", txt)
        self.assertIn("approved_hypothesis", txt)

if __name__ == "__main__":
    unittest.main()
