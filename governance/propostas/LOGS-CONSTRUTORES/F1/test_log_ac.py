import json, tempfile, unittest
from pathlib import Path
import log_ac as L

BASE = {"ts": "2026-11-01T12:00:00Z", "event": "agent.run", "family": "AC", "session_id": "s1", "run_id": "r1",
        "agent_id": "revisor", "severity": "INFO", "status": "SUCCEEDED", "operation": "agent.run",
        "model": "sonnet", "class": "O", "task_ref": "SPEC-049/plan/R2",
        "metrics": {"in": 10, "out": 5, "total": 15, "duration_ms": 1200, "tool_uses": 3},
        "output_ref": {"path": "governance/propostas/SPEC-049/PARECER.md", "sha256": "a" * 64}}


def ev(**kw):
    d = dict(BASE); d.update(kw); return d


class T(unittest.TestCase):
    def test_valido(self): self.assertEqual(L.valida(BASE), [])
    def test_campo_ausente(self):
        d = ev(); del d["run_id"]; self.assertTrue(L.valida(d))
    def test_campo_extra(self): self.assertTrue(L.valida(ev(foo=1)))
    def test_family_so_AC(self): self.assertTrue(L.valida(ev(family="AT")))
    def test_enum_event(self): self.assertTrue(L.valida(ev(event="x")))
    def test_severidade_enum(self): self.assertTrue(L.valida(ev(severity="DEBUG")))
    def test_conteudo_proibido(self): self.assertTrue(L.valida(ev(metrics={"prompt": 1})))
    def test_texto_proibido_topo_via_schema(self): self.assertTrue(L.valida(ev(prompt="oi")))
    def test_segredo_em_reason(self): self.assertTrue(any("segredo" in e for e in L.valida(ev(reason="uso sk-abcdefghijklmnopqrstu"))))
    def test_segredo_ghp(self): self.assertTrue(L.valida(ev(error="ghp_" + "a" * 30)))
    def test_segredo_senha(self): self.assertTrue(L.valida(ev(reason="password=hunter22")))
    def test_hash_malformado(self): self.assertTrue(L.valida(ev(output_ref={"path": "x", "sha256": "zz"})))
    def test_policy_exige_decision(self): self.assertTrue(L.valida(ev(event="policy.decision")))
    def test_policy_ok(self): self.assertEqual(L.valida(ev(event="policy.decision", decision="deny", policy_id="R-AC7", enforcement_point="hook:roteador", severity="AUDIT")), [])
    def test_ts_formato(self): self.assertTrue(L.valida(ev(ts="ontem")))
    def test_bool_nao_e_numero(self): self.assertTrue(L.valida(ev(metrics={"in": True})))
    def test_reason_longo(self): self.assertTrue(L.valida(ev(reason="x" * 301)))
    def test_cadeia_integra(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            for i in range(3): L.acrescenta(f, ev(run_id=f"r{i}"))
            self.assertEqual(L.verifica(f), [])
    def test_detecta_edicao(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            for i in range(3): L.acrescenta(f, ev(run_id=f"r{i}"))
            ls = f.read_text().splitlines(); o = json.loads(ls[1]); o["status"] = "FAILED"; ls[1] = json.dumps(o)
            f.write_text("\n".join(ls) + "\n"); self.assertTrue(any("edicao" in p for p in L.verifica(f)))
    def test_detecta_remocao(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            for i in range(3): L.acrescenta(f, ev(run_id=f"r{i}"))
            ls = f.read_text().splitlines(); del ls[1]
            f.write_text("\n".join(ls) + "\n"); self.assertTrue(any("prev_hash" in p for p in L.verifica(f)))
    def test_recusa_invalido_sem_gravar(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            with self.assertRaises(ValueError): L.acrescenta(f, ev(family="AT"))
            self.assertFalse(f.exists())
    def test_decision_vocabulario(self):
        self.assertTrue(L.valida(ev(event="policy.decision", decision="DENY", policy_id="x")))
        for d in ("allow", "deny", "ask", "defer"): self.assertEqual(L.valida(ev(event="policy.decision", decision=d, policy_id="x", policy_version="h1", redacted=["prompt"])), [])
    def test_metricas_so_inteiras(self): self.assertTrue(L.valida(ev(metrics={"in": 1.5})))
    def test_caminho_local_proibido(self):
        self.assertTrue(L.valida(ev(metrics={"cwd": 1})))
    def test_redacted_lista_de_strings(self): self.assertTrue(L.valida(ev(redacted=[1])))
    def test_schema_json_bem_formado(self): self.assertEqual(L.SCHEMA["properties"]["family"]["const"], "AC")

if __name__ == "__main__": unittest.main()
