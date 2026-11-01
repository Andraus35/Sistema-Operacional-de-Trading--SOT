"""telemetria_tokens + log dos Construtores (DHR-LOGS-AC-001, F2): agent.run no esquema; telemetria legada intacta; payload so com nomes de chaves."""
import contextlib, io, json, os, sys, tempfile, unittest
import unittest.mock as m
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import telemetria_tokens as T
import log_ac

EV = {"tool_name": "Agent", "session_id": "s1", "tool_use_id": "tu_1", "hook_event_name": "PostToolUse",
      "tool_input": {"subagent_type": "Revisor SOT", "model": "sonnet", "prompt": "CLASSE-TAREFA: S2\nALVO: SPEC-049/plan.md SEGREDO-NO-PROMPT"},
      "tool_response": {"content": [{"type": "text", "text": "TEXTO-DA-RESPOSTA"}], "totalDurationMs": 1200, "totalTokens": 1000, "totalToolUseCount": 3,
                        "usage": {"input_tokens": 600, "output_tokens": 300, "cache_read_input_tokens": 100, "cache_creation_input_tokens": 0}}}


def rodar(raiz, ev=EV):
    with m.patch.dict(os.environ, {"LOG_AC_RAIZ": str(raiz), "LOG_AC_FALHAS": str(Path(raiz) / "f.log")}), \
            m.patch.object(T, "SAIDA", Path(raiz) / ".telemetria" / "uso-tokens.jsonl"), \
            m.patch("sys.stdin", io.StringIO(json.dumps(ev))), contextlib.redirect_stdout(io.StringIO()):
        return T.hook()


class TelemetriaLog(unittest.TestCase):
    def test_emite_agent_run_valido_sem_texto(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(rodar(d), 0)
            txt = (Path(d) / ".telemetria" / "eventos.jsonl").read_text(); e = json.loads(txt.splitlines()[0])
            self.assertEqual((e["event"], e["session_id"], e["run_id"], e["agent_id"], e["class"], e["task_ref"]), ("agent.run", "s1", "tu_1", "Revisor SOT", "S2", "SPEC-049"))
            self.assertEqual((e["metrics"]["in"], e["metrics"]["total"], e["metrics"]["tool_uses"]), (600, 1000, 3))
            for proibido in ("SEGREDO-NO-PROMPT", "TEXTO-DA-RESPOSTA"): self.assertNotIn(proibido, txt)
            self.assertEqual(log_ac.verifica(Path(d) / ".telemetria" / "eventos.jsonl"), [])
    def test_telemetria_legada_intacta(self):
        with tempfile.TemporaryDirectory() as d:
            rodar(d); leg = json.loads((Path(d) / ".telemetria" / "uso-tokens.jsonl").read_text().splitlines()[0])
            self.assertEqual((leg["agente"], leg["total"]), ("Revisor SOT", 1000))
    def test_falha_do_log_nao_afeta_a_telemetria_legada(self):
        for exc in (ImportError("x"), ValueError("x"), RecursionError()):
            with tempfile.TemporaryDirectory() as d:
                with m.patch.object(T, "_emitir_log", side_effect=exc):
                    self.assertEqual(rodar(d), 0)
                self.assertTrue((Path(d) / ".telemetria" / "uso-tokens.jsonl").read_text().strip())
    def test_forma_do_payload_so_nomes_de_chaves(self):
        with tempfile.TemporaryDirectory() as d:
            rodar(d); txt = (Path(d) / ".telemetria" / "payload-forma.jsonl").read_text(); f = json.loads(txt.splitlines()[0])
            self.assertIn("tool_use_id", f["chaves"]); self.assertIn("usage", f["tool_response"])
            for proibido in ("SEGREDO-NO-PROMPT", "TEXTO-DA-RESPOSTA", "tu_1", "sonnet"): self.assertNotIn(proibido, txt)
    def test_ids_ausentes_usam_fallback(self):
        ev = json.loads(json.dumps(EV)); ev.pop("session_id"); ev.pop("tool_use_id")
        with tempfile.TemporaryDirectory() as d:
            rodar(d, ev); e = json.loads((Path(d) / ".telemetria" / "eventos.jsonl").read_text().splitlines()[0])
            self.assertEqual(e["session_id"], "sem-sessao"); self.assertTrue(e["run_id"].startswith("x:"))
    def test_outras_ferramentas_nao_geram_evento(self):
        with tempfile.TemporaryDirectory() as d:
            rodar(d, {"tool_name": "Bash", "session_id": "s"}); self.assertFalse((Path(d) / ".telemetria" / "eventos.jsonl").exists())

if __name__ == "__main__":
    unittest.main()
