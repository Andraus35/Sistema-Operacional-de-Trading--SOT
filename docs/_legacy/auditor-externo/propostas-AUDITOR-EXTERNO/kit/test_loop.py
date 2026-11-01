#!/usr/bin/env python3
"""test_loop.py — testes offline do loop (loop_tools.py e poll_requests.py). [PROPOSTA — NÃO HOMOLOGADO]
Rodar: python3 test_loop.py   (stdlib; servidor HTTP falso em localhost, sem rede/credencial)."""
import json, os, subprocess, sys, tempfile, threading, unittest
from http.server import BaseHTTPRequestHandler, HTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
SHA = "a" * 40
LT = [sys.executable, os.path.join(HERE, "loop_tools.py")]


def run(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, **kw)


def tmp(content, name="f"):
    p = os.path.join(tempfile.mkdtemp(), name); open(p, "w", encoding="utf-8").write(content); return p


FINDING = {"baseline_commit": SHA, "evidence": [{"path": "AGENTS.md", "line_start": 5, "line_end": 5, "quote": "linha  com   espaços"}],
           "proposal": {"type": "NOTA"}}


class TestLoopTools(unittest.TestCase):
    def test_extract_ok_e_erros(self):
        out = os.path.join(tempfile.mkdtemp(), "o.json")
        ok = tmp("texto\n```json\n" + json.dumps(FINDING) + "\n```\nmais")
        self.assertEqual(run(LT + ["extract", "--body-file", ok, "--out", out]).returncode, 0)
        self.assertEqual(json.load(open(out))["baseline_commit"], SHA)
        for corpo in ("sem bloco", "```json\n{quebrado\n```", "```json\n[1,2]\n```", "x" * 100_001):
            self.assertEqual(run(LT + ["extract", "--body-file", tmp(corpo), "--out", out]).returncode, 1, corpo[:20])

    def test_meta_valida_sha(self):
        self.assertEqual(run(LT + ["meta", "--finding", tmp(json.dumps(FINDING))]).stdout.strip(), SHA)
        ruim = dict(FINDING, baseline_commit="HEAD; rm -rf /")
        self.assertEqual(run(LT + ["meta", "--finding", tmp(json.dumps(ruim))]).returncode, 1)

    def test_fingerprint_estavel_e_sensivel(self):
        f1 = run(LT + ["fingerprint", "--finding", tmp(json.dumps(FINDING))]).stdout.strip()
        f2 = dict(FINDING); f2["evidence"] = [dict(FINDING["evidence"][0], quote="linha com espaços")]  # só espaços diferentes
        self.assertEqual(f1, run(LT + ["fingerprint", "--finding", tmp(json.dumps(f2))]).stdout.strip())
        f3 = dict(FINDING); f3["evidence"] = [dict(FINDING["evidence"][0], line_start=6)]
        self.assertNotEqual(f1, run(LT + ["fingerprint", "--finding", tmp(json.dumps(f3))]).stdout.strip())

    def test_request_body_exclui_mapa_e_tem_marcador(self):
        fl = tmp("specs/features/SPEC-001/plan.md\ndocs/mapa/MAPA-PROJETO.md\n")
        b = run(LT + ["request-body", "--pr", "7", "--sha", SHA, "--files-file", fl, "--round", "1"]).stdout
        self.assertIn(f"<!-- aex-req pr=7 sha={SHA} round=1 kind=auditoria -->", b)
        self.assertIn("specs/features/SPEC-001/plan.md", b); self.assertNotIn("MAPA-PROJETO.md", b)
        self.assertEqual(run(LT + ["request-body", "--pr", "7", "--sha", "xyz", "--files-file", fl, "--round", "1"]).returncode, 1)
        r = run(LT + ["request-body", "--pr", "7", "--sha", SHA, "--files-file", fl, "--round", "2", "--kind", "re-auditoria", "--refs", "12,x,15"]).stdout
        self.assertIn("#12, #15", r); self.assertNotIn("#x", r)

    def test_request_body_manifesto(self):
        fl = os.path.join(tempfile.mkdtemp(), "f.txt"); open(fl, "w").write("AGENTS.md\n"); mf = "d" * 64
        b = run(LT + ["request-body", "--pr", "7", "--sha", SHA, "--files-file", fl, "--round", "1", "--manifest-sha", mf]).stdout
        self.assertIn(f"kind=auditoria manifest={mf} -->", b); self.assertIn(f"`{mf}`", b)
        self.assertEqual(run(LT + ["request-body", "--pr", "7", "--sha", SHA, "--files-file", fl, "--round", "1", "--manifest-sha", "xyz"]).returncode, 1)
        self.assertNotIn("manifest=", run(LT + ["request-body", "--pr", "7", "--sha", SHA, "--files-file", fl, "--round", "1"]).stdout)
    def test_comment_body(self):
        rep = tmp(json.dumps({"pass": False, "finding_id": "AEX-1", "head": SHA, "errors": ["E-QUOTE x"], "warnings": []}))
        c = run(LT + ["comment-body", "--report", rep, "--fp", "abc"]).stdout
        self.assertIn("FAIL", c); self.assertIn("E-QUOTE x", c); self.assertIn("<!-- aex-fp:abc -->", c)
        self.assertIn("DUPLICADO", run(LT + ["comment-body", "--report", rep, "--fp", "abc", "--dup", "9"]).stdout)


class H(BaseHTTPRequestHandler):
    posted = []
    def log_message(self, *a): pass
    def _send(self, obj): b = json.dumps(obj).encode(); self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if "/comments" in self.path:
            n = self.path.split("/issues/")[1].split("/")[0]
            return self._send([{"body": "<!-- aex-ack -->"}] if n == "2" else [])
        body = lambda sha, pr, mf="": f"<!-- aex-req pr={pr} sha={sha} round=1 kind=auditoria{mf} -->\n- Commit: `{sha}`\n- `specs/features/SPEC-001/plan.md`\n- `AGENTS.md`\n"
        bot = {"login": "github-actions[bot]"}
        self._send([{"number": 1, "title": "[AEX-REQ] PR#7", "user": bot, "body": body(SHA, 7, " manifest=" + "a" * 64)},
                    {"number": 2, "title": "[AEX-REQ] PR#8 (já atendido)", "user": bot, "body": body("b" * 40, 8)},
                    {"number": 6, "title": "[AEX-REQ] forjado por outra conta", "user": {"login": "intruso"}, "body": body("c" * 40, 9)},
                    {"number": 3, "title": "outra issue qualquer", "body": "x"},
                    {"number": 4, "title": "[AEX-REQ] sem marcador", "body": "sem marcador"},
                    {"number": 5, "title": "PR", "pull_request": {}, "body": "x"}])
    def do_POST(self):
        n = int(self.headers["Content-Length"]); H.posted.append((self.path, json.loads(self.rfile.read(n)))); self._send({"id": 1})


class TestPoll(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = HTTPServer(("127.0.0.1", 0), H); threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.env = dict(os.environ, SOT_AUDITOR_TOKEN="x", SOT_API_BASE=f"http://127.0.0.1:{cls.srv.server_port}", SOT_REPO_SLUG="o/r")
    @classmethod
    def tearDownClass(cls): cls.srv.shutdown()
    def P(self, *a): return run([sys.executable, os.path.join(HERE, "poll_requests.py"), *a], env=self.env, cwd=tempfile.mkdtemp())
    def test_lista_so_pendentes_com_marcador(self):
        o = self.P().stdout
        self.assertIn("#1 PR#7", o); self.assertNotIn("#2", o); self.assertNotIn("#3", o); self.assertNotIn("#4", o); self.assertNotIn("#5", o)
        self.assertNotIn("#6", o)  # autor não é o bot: ignorado
        self.assertIn("manifesto=aaaaaaaa", o)
    def test_prepare_e_ack(self):
        d = tempfile.mkdtemp(); out = os.path.join(d, "task.json")
        self.assertEqual(self.P("--prepare", "--out", out).returncode, 0)
        t = json.load(open(out)); self.assertEqual((t["issue"], t["sha"], t["files"]), (1, SHA, ["specs/features/SPEC-001/plan.md", "AGENTS.md"]))
        self.assertEqual(t["manifest"], "a" * 64)
        H.posted.clear(); self.assertEqual(self.P("--ack", "1", "--verdict", "COM_RESSALVAS", "--findings", "2", "--discarded", "1").returncode, 0)
        self.assertIn("/issues/1/comments", H.posted[0][0]); self.assertIn("<!-- aex-ack -->", H.posted[0][1]["body"])
        self.assertIn("COM_RESSALVAS", H.posted[0][1]["body"])
        self.assertEqual(self.P("--ack", "1").returncode, 2)  # sem --verdict: recusa
        self.assertEqual(self.P("--ack", "1", "--verdict", "TALVEZ").returncode, 2)  # veredito inválido
    def test_sem_token_falha(self):
        e = dict(self.env); e.pop("SOT_AUDITOR_TOKEN")
        self.assertEqual(run([sys.executable, os.path.join(HERE, "poll_requests.py")], env=e).returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=1)
