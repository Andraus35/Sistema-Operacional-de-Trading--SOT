#!/usr/bin/env python3
"""Testes do auditor_bot.py: API do GitHub, Codex, setup e gates SIMULADOS (nada de rede real). python -m unittest test_bot.py"""
import json, os, subprocess, sys, tempfile, threading, unittest
from http.server import BaseHTTPRequestHandler, HTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
BOT = os.path.join(HERE, "auditor_bot.py")
TOKEN = "ghp_" + "A1b2C3d4E5f6G7h8I9j0" + "KLMN"   # token falso, só para o teste de vazamento
SLUG = "o/r"


class Api(BaseHTTPRequestHandler):
    issues, comments, created = [], [], []
    def log_message(self, *a): pass
    def _send(self, obj, code=200):
        b = json.dumps(obj).encode(); self.send_response(code); self.send_header("Content-Type", "application/json"); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.startswith(f"/repos/{SLUG}/issues") and "/comments" in self.path: return self._send([])
        if self.path.startswith(f"/repos/{SLUG}/issues"): return self._send(Api.issues)
        if self.path == f"/repos/{SLUG}":
            return self._send({"full_name": SLUG, "private": True, "has_issues": True,
                               "permissions": {"pull": True, "push": True, "admin": True, "maintain": True, "triage": True}})
        self._send({}, 404)
    def do_POST(self):
        n = int(self.headers["Content-Length"]); d = json.loads(self.rfile.read(n))
        if self.path.endswith("/comments"): Api.comments.append((self.path, d["body"])); return self._send({"id": 1})
        Api.created.append(d); self._send({"html_url": "http://x/1", "number": 99})


def git(repo, *a): return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, check=True).stdout.strip()


class TestBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = HTTPServer(("127.0.0.1", 0), Api); threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
    @classmethod
    def tearDownClass(cls): cls.srv.shutdown()

    def setUp(self):
        Api.issues, Api.comments, Api.created = [], [], []
        self.d = tempfile.mkdtemp(); self.state = os.path.join(self.d, "state"); self.work = os.path.join(self.d, "work")
        repo = os.path.join(self.work, "repo"); os.makedirs(os.path.join(repo, "governance/propostas/AUDITOR-EXTERNO"))
        open(os.path.join(repo, "AGENTS.md"), "w", encoding="utf-8").write("# AGENTS\nHierarquia inviolável: Elliott → Fibonacci → Fractal → SMC → ICT\n")
        open(os.path.join(repo, "governance/propostas/AUDITOR-EXTERNO/DIRETIVAS-AO-AUDITOR.md"), "w", encoding="utf-8").write("## DIR-002\nStatus: VIGENTE\n")
        git(repo, "init", "-q"); git(repo, "-c", "user.email=t@t", "-c", "user.name=t", "add", "-A")
        git(repo, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "x"); self.sha = git(repo, "rev-parse", "HEAD")
        self.repo = repo
        # setup falso: não faz nada (o clone de teste já está no commit)
        self.setup = os.path.join(self.d, "setup.py"); open(self.setup, "w").write("import sys; sys.exit(0)\n")
        self.gates = os.path.join(self.d, "gates.py")
        open(self.gates, "w").write("import json,sys,subprocess\nout=sys.argv[sys.argv.index('--out')+1]; repo=sys.argv[sys.argv.index('--repo')+1]\n"
            "h=subprocess.run(['git','-C',repo,'rev-parse','HEAD'],capture_output=True,text=True).stdout.strip()\njson.dump({'repo_commit':h,'gates':[]},open(out,'w'))\n")
        # codex falso: registra args/ambiente e devolve o conteúdo de out.txt em -o
        self.codex = os.path.join(self.d, "codex.py"); self.out = os.path.join(self.d, "out.txt"); self.clog = os.path.join(self.d, "codex.log")
        open(self.codex, "w").write("import json,os,sys\nargs=sys.argv[1:]; prompt=sys.stdin.read()\n"
            f"json.dump({{'args':args,'has_token':'SOT_AUDITOR_TOKEN' in os.environ,'has_git_cfg':any(k.startswith('GIT_CONFIG') for k in os.environ),'prompt_has_sha':'{self.sha}' in prompt}},open({self.clog!r},'w'))\n"
            f"o=args[args.index('-o')+1]; open(o,'w').write(open({self.out!r}).read())\n")
        os.makedirs(os.path.join(self.state, "codex-home"), exist_ok=True)
        json.dump({"tokens": {"refresh_token": "RT-" + "z" * 30}}, open(os.path.join(self.state, "codex-home", "auth.json"), "w"))
        self.env = dict(os.environ, SOT_AUDITOR_TOKEN=TOKEN, SOT_API_BASE=f"http://127.0.0.1:{self.srv.server_port}", SOT_REPO_SLUG=SLUG,
                        SOT_AUDIT_STATE=self.state, SOT_AUDIT_HOME=self.work, SOT_CONFIRMO_ESCOPO="1",
                        SOT_CODEX_CMD=f"{sys.executable} {self.codex}", SOT_SETUP_CMD=f"{sys.executable} {self.setup}",
                        SOT_GATES_CMD=f"{sys.executable} {self.gates}")

    def req_issue(self, number=1, manifest=""):
        mf = f" manifest={manifest}" if manifest else ""
        Api.issues = [{"number": number, "title": "[AEX-REQ] x", "user": {"login": "github-actions[bot]"},
                       "body": f"<!-- aex-req pr=7 sha={self.sha} round=1 kind=auditoria{mf} -->\n- `AGENTS.md`\n"}]

    def run_bot(self, *a): return subprocess.run([sys.executable, BOT, *a], env=self.env, capture_output=True, text=True, cwd=self.d)
    def acks(self): return [b for _, b in Api.comments if "<!-- aex-ack -->" in b]

    def saida(self, achados, veredito="COM_RESSALVAS"):
        open(self.out, "w", encoding="utf-8").write("Segue:\n```json\n" + json.dumps({"veredito": veredito, "achados": achados}, ensure_ascii=False) + "\n```\n")

    def bom(self, quote="Hierarquia inviolável: Elliott → Fibonacci"):
        return {"severity": "P2", "type": "editorial", "title": "t", "claim": "c", "rule_source": "AGENTS.md §6",
                "evidence": [{"path": "AGENTS.md", "line_start": 2, "line_end": 2, "quote": quote}],
                "proposal": {"type": "NOTA", "text": "n", "modifies_baselined_text": False, "touches": []},
                "impact": "i", "what_does_not_change": "w", "open_decisions_referenced": [], "treats_open_decision_as_closed": False,
                "status_sip": {"specified": True, "implemented": False, "proven": False}, "reproduce": ["git grep -n Hierarquia -- AGENTS.md"]}

    def test_sem_pedido_nao_chama_o_modelo(self):
        r = self.run_bot(); self.assertEqual(r.returncode, 0); self.assertIn("Sem pedidos pendentes", r.stdout)
        self.assertFalse(os.path.exists(self.clog))

    def test_fluxo_completo_posta_valido_descarta_invalido_e_da_ack(self):
        self.req_issue(); self.saida([self.bom(), self.bom(quote="citação inventada que não existe no arquivo")])
        r = self.run_bot(); self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(len(Api.created), 1)                        # só o achado válido foi postado
        self.assertTrue(Api.created[0]["title"].startswith("[AEX] AEX-"))
        ack = self.acks(); self.assertEqual(len(ack), 1)
        self.assertIn("COM_RESSALVAS", ack[0]); self.assertIn("postados: 1", ack[0]); self.assertIn("descartados na autoverificação: 1", ack[0])
        c = json.load(open(self.clog))
        self.assertFalse(c["has_token"]); self.assertFalse(c["has_git_cfg"]); self.assertTrue(c["prompt_has_sha"])
        for flag in ("exec", "--sandbox", "read-only", "--ephemeral", "-o", "-"): self.assertIn(flag, c["args"])
        self.assertEqual(c["args"][c["args"].index("--sandbox") + 1], "read-only")
        self.assertNotIn(TOKEN, json.dumps(Api.created) + json.dumps(Api.comments))

    def test_dry_run_nao_posta_nem_da_ack(self):
        self.req_issue(); self.saida([self.bom()])
        r = self.run_bot("--dry-run"); self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(Api.created, []); self.assertEqual(self.acks(), [])

    def test_campos_de_maquina_sao_do_bot(self):
        self.req_issue(); f = self.bom(); f.update({"baseline_commit": "0" * 40, "directive_version": "DIR-999", "id": "AEX-19990101-001"})
        self.saida([f]); self.assertEqual(self.run_bot().returncode, 0)
        body = Api.created[0]["body"]; self.assertIn(self.sha, body); self.assertNotIn("DIR-999", body); self.assertIn("DIR-002", body)

    def test_vazamento_de_segredo_na_saida_e_barrado(self):
        self.req_issue(); f = self.bom(); f["claim"] = "achei isto: " + TOKEN
        self.saida([f]); r = self.run_bot(); self.assertEqual(r.returncode, 2)
        self.assertEqual(Api.created, []); self.assertEqual(self.acks(), [])
        notas = [b for _, b in Api.comments]; self.assertEqual(len(notas), 1); self.assertIn("segurança", notas[0]); self.assertNotIn(TOKEN, notas[0])
        # vazamento do auth.json do próprio Codex também
        Api.comments.clear(); os.remove(os.path.join(self.state, "notified.json")); os.remove(os.path.join(self.state, "attempts.json"))
        f["claim"] = "RT-" + "z" * 30; self.saida([f]); self.assertEqual(self.run_bot().returncode, 2); self.assertEqual(Api.created, [])

    def test_formato_invalido_gera_nota_unica_e_para_apos_tentativas(self):
        self.req_issue(); open(self.out, "w").write("sem bloco json")
        self.assertEqual(self.run_bot().returncode, 2); self.assertEqual(self.run_bot().returncode, 2)
        r = self.run_bot(); self.assertEqual(r.returncode, 2); self.assertIn("Tentativas esgotadas", r.stdout)
        self.assertEqual(Api.created, []); self.assertEqual(self.acks(), [])
        self.assertEqual(len([b for _, b in Api.comments if "não seguiu o formato" in b]), 1)   # nota não repete
        self.assertEqual(len([b for _, b in Api.comments if "tentativas esgotadas" in b]), 1)

    def test_manifesto_do_pedido_diferente_do_aprovado_e_ignorado(self):
        open(os.path.join(self.state, "approved_manifest.sha256"), "w").write("a" * 64 + "\n")
        self.req_issue(manifest="b" * 64); self.saida([self.bom()])
        r = self.run_bot(); self.assertEqual(r.returncode, 2); self.assertFalse(os.path.exists(self.clog)); self.assertEqual(Api.created, [])

    def test_manifesto_igual_prossegue(self):
        open(os.path.join(self.state, "approved_manifest.sha256"), "w").write("a" * 64 + "\n")
        self.req_issue(manifest="a" * 64); self.saida([], "OK")
        self.assertEqual(self.run_bot().returncode, 0); self.assertIn("OK", self.acks()[0])

    def test_limite_diario_de_chamadas(self):
        self.req_issue(); self.saida([], "OK"); self.env["SOT_BOT_MAX_RUNS"] = "1"
        # 1ª chamada consome o limite mas o pedido segue pendente (API simulada não registra ACK)
        self.assertEqual(self.run_bot().returncode, 0); os.remove(self.clog)
        r = self.run_bot(); self.assertEqual(r.returncode, 0); self.assertIn("Limite diário", r.stdout); self.assertFalse(os.path.exists(self.clog))

    def test_sem_token_bloqueia(self):
        self.env.pop("SOT_AUDITOR_TOKEN"); self.req_issue(); self.assertEqual(self.run_bot().returncode, 2)

    def test_pedido_forjado_por_outra_conta_e_ignorado(self):
        self.req_issue(); Api.issues[0]["user"]["login"] = "intruso"; self.saida([self.bom()])
        r = self.run_bot(); self.assertIn("Sem pedidos pendentes", r.stdout); self.assertFalse(os.path.exists(self.clog))


if __name__ == "__main__":
    unittest.main(verbosity=1)
