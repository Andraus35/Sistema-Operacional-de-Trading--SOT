import json, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import telemetria_tokens as T


class Telemetria(unittest.TestCase):
    EV = {"tool_name": "Agent", "session_id": "s1",
          "tool_input": {"subagent_type": "Revisor SOT", "model": "sonnet", "prompt": "CLASSE-TAREFA: S2\nALVO: x.md SEGREDO"},
          "tool_response": {"content": [{"type": "text", "text": "ok"}], "totalDurationMs": 1200, "totalTokens": 1000, "totalToolUseCount": 3,
                            "usage": {"input_tokens": 600, "output_tokens": 300, "cache_read_input_tokens": 100, "cache_creation_input_tokens": 0}}}

    def test_extrai_metadados_sem_texto(self):
        r = T.extrair(self.EV)
        self.assertEqual((r["agente"], r["model"], r["classe"], r["total"], r["in"], r["out"]), ("Revisor SOT", "sonnet", "S2", 1000, 600, 300))
        self.assertNotIn("SEGREDO", json.dumps(r))

    def test_total_soma_parcelas_se_ausente(self):
        ev = json.loads(json.dumps(self.EV)); del ev["tool_response"]["totalTokens"]
        self.assertEqual(T.extrair(ev)["total"], 1000)

    def test_formato_desconhecido_nao_quebra(self):
        r = T.extrair({"tool_name": "Agent", "tool_input": {}, "tool_response": "texto"})
        self.assertIsNone(r["total"])

    def test_custo_indeterminado_sem_preco(self):
        orig = T._preco
        T._preco = lambda m: {"input": None, "output": None, "cache_read": None, "cache_create": None}
        try:
            self.assertIsNone(T.custo(T.extrair(self.EV)))
        finally:
            T._preco = orig

    def test_custo_com_preco(self):
        orig = T._preco
        T._preco = lambda m: {"input": 3.0, "output": 15.0, "cache_read": 0.3, "cache_create": 3.75}
        try:
            c = T.custo(T.extrair(self.EV))
        finally:
            T._preco = orig
        self.assertAlmostEqual(c, (600 * 3 + 300 * 15 + 100 * 0.3) / 1e6)

    def test_resumo_agrega(self):
        r = T.extrair(self.EV)
        g = T.resumo([r, r])
        v = g[("Revisor SOT", "sonnet", "S2")]
        self.assertEqual((v["chamadas"], v["total"], v["custo_indet"]), (2, 2000, 0))

    def test_spec_e_alvo_extraidos_e_resumo_por_spec(self):
        ev = json.loads(json.dumps(self.EV))
        ev["tool_input"]["prompt"] = "CLASSE-TAREFA: S2\nALVO: specs/features/SPEC-049/plan.md"
        r = T.extrair(ev)
        self.assertEqual((r["spec"], r["alvo"]), ("SPEC-049", "specs/features/SPEC-049/plan.md"))
        v = T.resumo([r, r], por="spec")[("SPEC-049", "Revisor SOT", "S2")]
        self.assertEqual(v["total"], 2000)

    def test_custo_beneficio_cruza_tokens_e_achados(self):
        ev = json.loads(json.dumps(self.EV)); ev["tool_input"]["prompt"] = "CLASSE-TAREFA: S2\nALVO: specs/features/SPEC-049/plan.md"
        regs = [T.extrair(ev), T.extrair(ev)]  # 2000 tokens na SPEC-049
        linhas = {"SPEC-049 PLAN": {1: {"achados": [{"sev": "Média"}, {"sev": "Menor"}]}, 2: {"achados": [{"sev": "Menor"}]}},
                  "SPEC-050 PLAN": {1: {"achados": [{"sev": "Crítica"}]}}}
        r = {x["spec"]: x for x in T.custo_beneficio(regs, linhas)}
        self.assertEqual((r["SPEC-049"]["rodadas"], r["SPEC-049"]["tokens"], r["SPEC-049"]["tokens_por_rodada"]), (2, 2000, 1000))
        self.assertEqual((r["SPEC-049"]["tokens_por_achado"], r["SPEC-049"]["tokens_por_achado_grave"]), (667, 2000))
        self.assertIsNone(r["SPEC-050"]["tokens"])  # sem telemetria => n/m, nunca estimado
        self.assertIsNone(r["SPEC-050"]["tokens_por_achado"])

    def test_snapshot_markdown(self):
        md = T.snapshot([T.extrair(self.EV)])
        self.assertIn("| Revisor SOT | sonnet | S2 | 1 | 1000 |", md)
        self.assertIn("equivalente API", md)
        self.assertNotIn("SEGREDO", md)

    def test_tabela_de_precos_tem_fonte_e_rotulo(self):
        tab = json.loads(T.PRECOS.read_text(encoding="utf-8"))
        self.assertTrue(tab.get("fonte", "").startswith("https://"))
        self.assertIn("NÃO é cobrança", tab["rotulo"])
        for m in tab["modelos"].values():
            self.assertTrue(all(isinstance(m[k], (int, float)) for k in ("input", "output", "cache_read", "cache_create")))

    def test_custo_equivalente_haiku_com_tabela_real(self):
        r = {"model": "haiku", "in": 2, "out": 221, "cache_read": 40828, "cache_create": 535}
        self.assertAlmostEqual(T.custo(r), (2 * 0.10 + 221 * 0.50 + 40828 * 0.01 + 535 * 0.125) / 1e6)


if __name__ == "__main__":
    unittest.main()
