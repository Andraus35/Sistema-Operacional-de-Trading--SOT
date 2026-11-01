"""Roteador + log dos Construtores (DHR-LOGS-AC-001, F2): o log NUNCA altera a decisao; L2 so com deny, sem texto livre, sessao em hash."""
import contextlib, io, json, os, sys, tempfile, unittest
import unittest.mock as m
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import roteador_modelos as r
import log_ac

NEGA = {"tool_name": "Agent", "session_id": "sess-123", "tool_use_id": "tu_9",
        "tool_input": {"subagent_type": "Especificador SOT", "prompt": "faca algo ALVO: segredo sk-abcdefghijklmnopqrstuv"}}
PERMITE = {"tool_name": "Agent", "session_id": "sess-123", "tool_input": {"subagent_type": "Explore", "prompt": "x"}}


def rodar(ev, raiz, **patches):
    out = io.StringIO()
    with m.patch.dict(os.environ, {"LOG_AC_RAIZ": str(raiz), "LOG_AC_FALHAS": str(Path(raiz) / "f.log")}), \
            m.patch.object(r, "registrar"), m.patch.object(r, "ROOT", Path(raiz)), \
            m.patch("sys.stdin", io.StringIO(json.dumps(ev))), contextlib.redirect_stdout(out):
        rc = r.hook()
    return rc, out.getvalue()


class RoteadorLog(unittest.TestCase):
    def test_deny_gera_L1_e_L2_sem_texto_livre(self):
        with tempfile.TemporaryDirectory() as d:
            rc, out = rodar(NEGA, d)
            self.assertEqual(rc, 0); self.assertIn('"permissionDecision": "deny"', out)
            l1 = [json.loads(l) for l in (Path(d) / ".telemetria" / "eventos.jsonl").read_text().splitlines()]
            self.assertEqual((l1[0]["decision"], l1[0]["session_id"], l1[0]["run_id"]), ("deny", "sess-123", "tu_9"))
            l2s = list((Path(d) / "governance" / "logs" / "L2").glob("*.jsonl"))
            self.assertEqual(len(l2s), 1); e2 = json.loads(l2s[0].read_text().splitlines()[0])
            self.assertTrue(e2["session_id"].startswith("h:")); self.assertIsNone(e2["reason"])
            self.assertNotIn("sk-abc", l2s[0].read_text()); self.assertNotIn("sess-123", l2s[0].read_text())
            with m.patch.dict(os.environ, {"LOG_AC_RAIZ": d}):
                self.assertEqual(l2s[0].stem, log_ac.nome_segmento("sess-123"))
            self.assertEqual(log_ac.verifica(l2s[0]), [])
    def test_allow_so_L1(self):
        with tempfile.TemporaryDirectory() as d:
            rc, out = rodar(PERMITE, d)
            self.assertEqual((rc, out), (0, "")); self.assertTrue((Path(d) / ".telemetria" / "eventos.jsonl").exists())
            self.assertFalse((Path(d) / "governance" / "logs").exists())
    def test_decisao_identica_quando_o_log_falha(self):
        for exc in (ImportError("x"), ValueError("x"), RuntimeError("x"), RecursionError(), KeyboardInterrupt()):
            with tempfile.TemporaryDirectory() as d:
                _, ref = rodar(NEGA, d)
            with tempfile.TemporaryDirectory() as d:
                with m.patch.object(log_ac, "emite_seguro", side_effect=exc):
                    rc, out = rodar(NEGA, d)
                self.assertEqual((rc, out), (0, ref), type(exc).__name__)
                self.assertIn("WARN", (Path(d) / ".telemetria" / "log-ac-falhas.log").read_text())
    def test_import_do_log_quebrado_nao_perde_o_deny(self):
        with tempfile.TemporaryDirectory() as d:
            _, ref = rodar(NEGA, d)
        with tempfile.TemporaryDirectory() as d:
            with m.patch.dict(sys.modules, {"log_ac": None}):
                rc, out = rodar(NEGA, d)
            self.assertEqual((rc, out), (0, ref)); self.assertIn("roteador WARN", (Path(d) / ".telemetria" / "log-ac-falhas.log").read_text())
    def test_deny_impresso_antes_do_log(self):
        ordem = []
        with tempfile.TemporaryDirectory() as d:
            real = r._emitir_log
            def espia(*a, **k): ordem.append("log"); return real(*a, **k)
            out = io.StringIO()
            class S(io.StringIO):
                def write(self, s): ordem.append("print") if "permissionDecision" in s else None; return super().write(s)
            with m.patch.object(r, "_emitir_log", espia), m.patch.object(r, "registrar"), m.patch.dict(os.environ, {"LOG_AC_RAIZ": d}), \
                    m.patch.object(r, "ROOT", Path(d)), m.patch("sys.stdin", io.StringIO(json.dumps(NEGA))), contextlib.redirect_stdout(S()):
                r.hook()
        self.assertEqual(ordem, ["print", "log"])
    def test_sem_evento_fora_do_escopo(self):
        with tempfile.TemporaryDirectory() as d:
            rc, out = rodar({"tool_name": "Bash", "session_id": "s"}, d)
            self.assertEqual((rc, out), (0, "")); self.assertFalse((Path(d) / ".telemetria").exists())

if __name__ == "__main__":
    unittest.main()
