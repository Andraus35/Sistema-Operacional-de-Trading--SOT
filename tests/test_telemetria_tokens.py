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
        self.assertIsNone(T.custo(T.extrair(self.EV)))

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
        self.assertEqual((v["chamadas"], v["total"], v["custo_indet"]), (2, 2000, 2))

    def test_tabela_de_precos_nao_inventa(self):
        tab = json.loads(T.PRECOS.read_text(encoding="utf-8"))
        self.assertTrue(all(v is None for m in tab["modelos"].values() for v in m.values()) or tab.get("fonte"))


if __name__ == "__main__":
    unittest.main()
