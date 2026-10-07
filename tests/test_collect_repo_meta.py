"""Testes do collect_repo_meta.py — python -m unittest tests/test_collect_repo_meta.py

Servidor HTTP falso em localhost (nenhuma rede real). Garante: (a) campos objetivos e campo-fonte; (b) alertas = INDETERMINADO (nunca 0);
(c) NENHUMA credencial é enviada, mesmo com token no ambiente; (d) privado/inexistente/GitLab/rede => exit 2 sem inventar nada;
(e) não sobrescreve captura existente (INV-07).
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "collect_repo_meta.py"
REPO_OK = {"full_name": "acme/widget", "html_url": "https://github.com/acme/widget", "stargazers_count": 1234,
           "license": {"spdx_id": "Apache-2.0"}, "pushed_at": "2026-10-05T04:18:38Z", "archived": False,
           "owner": {"login": "acme", "type": "Organization"}, "description": "A widget for  agents,\nbuilt for production."}


class Api(BaseHTTPRequestHandler):
    seen_headers = []
    payloads = {}

    def log_message(self, *a): pass

    def do_GET(self):
        Api.seen_headers.append({k.lower(): v for k, v in self.headers.items()})
        body = Api.payloads.get(self.path)
        if body is None:
            self.send_response(404); self.end_headers(); return
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps(body).encode())


class CollectRepoMeta(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = HTTPServer(("127.0.0.1", 0), Api)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.srv.server_port}"

    @classmethod
    def tearDownClass(cls): cls.srv.shutdown()

    def setUp(self):
        Api.seen_headers = []; Api.payloads = {"/repos/acme/widget": dict(REPO_OK)}

    def run_script(self, *args, env=None):
        e = dict(os.environ, PYTHONUTF8="1"); e.update(env or {})
        return subprocess.run([sys.executable, str(SCRIPT), *args, "--api-base", self.base, "--today", "2026-10-06"],
                              capture_output=True, text=True, encoding="utf-8", env=e)

    def test_gera_rascunho_com_campos_e_campo_fonte(self):
        r = self.run_script("acme/widget"); self.assertEqual(r.returncode, 0, r.stderr)
        o = r.stdout
        for esperado in ("Repositório: https://github.com/acme/widget", "Plataforma: GitHub", "Data de acesso: 2026-10-06",
                         "Estrelas: 1234   (campo stargazers_count)", "Licença: Apache-2.0   (campo license.spdx_id)",
                         "Último commit: 2026-10-05", "pushed_at = 2026-10-05T04:18:38Z", "Arquivado: não   (campo archived)",
                         "Dono: acme (Organization — identificável)"):
            self.assertIn(esperado, o)
        self.assertIn('"A widget for agents, built for production."', o)        # description com espaços colapsados

    def test_alertas_sao_indeterminado_nunca_zero(self):
        o = self.run_script("acme/widget").stdout
        linha = next(l for l in o.splitlines() if l.startswith("Alertas de segurança graves abertos"))
        self.assertIn("INDETERMINADO", linha); self.assertNotRegex(linha, r":\s*0\b")

    def test_veredito_fica_pendente_e_ha_pre_avaliacao_mecanica(self):
        o = self.run_script("acme/widget").stdout
        self.assertIn("Veredito de elegibilidade: PENDENTE", o); self.assertNotIn("ELEGÍVEL", o.split("Veredito de elegibilidade:")[1].splitlines()[0])
        self.assertIn("estrelas 1234 >= 300", o); self.assertIn("licença Apache-2.0 na lista de abertas", o)

    def test_capture_sai_incompleta_para_o_gate_de_regua_ate_decisao_de_andraus(self):
        # fail-closed: o campo de alertas não é numérico, então check_repo_research.py a trata como incompleta
        sys.path.insert(0, str(SCRIPT.parent))
        import check_repo_research as crr
        meta = crr.parse_capture(self.run_script("acme/widget").stdout)
        ok, why = crr.evaluate(meta)
        self.assertFalse(ok); self.assertTrue(any("alertas" in w for w in why))

    def test_nunca_envia_credencial_mesmo_com_token_no_ambiente(self):
        self.run_script("acme/widget", env={"GITHUB_TOKEN": "ghp_" + "x" * 30, "GH_TOKEN": "ghp_" + "y" * 30, "SOT_AUDITOR_TOKEN": "ghp_" + "z" * 30})
        self.assertTrue(Api.seen_headers)
        for h in Api.seen_headers: self.assertNotIn("authorization", h)

    def test_aceita_url_completa(self):
        self.assertEqual(self.run_script("https://github.com/acme/widget").returncode, 0)

    def test_privado_ou_inexistente_e_indeterminado_sem_inventar(self):
        r = self.run_script("acme/nao-existe"); self.assertEqual(r.returncode, 2)
        self.assertIn("INDETERMINADO", r.stderr); self.assertEqual(r.stdout.strip(), "")

    def test_gitlab_fora_do_escopo(self):
        r = self.run_script("https://gitlab.com/acme/widget"); self.assertEqual(r.returncode, 2); self.assertIn("GitLab", r.stderr)

    def test_repo_arquivado_e_licenca_fora_da_lista_aparecem_na_pre_avaliacao(self):
        Api.payloads["/repos/acme/widget"] = dict(REPO_OK, archived=True, license={"spdx_id": "NOASSERTION"}, stargazers_count=10)
        o = self.run_script("acme/widget").stdout
        self.assertIn("Arquivado: sim", o); self.assertIn("FORA da lista", o); self.assertIn("estrelas 10 < 300", o)

    def test_nao_sobrescreve_captura_existente(self):
        d = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, d, True)
        out = d / "sources" / "REPO-x.txt"
        self.assertEqual(self.run_script("acme/widget", "--out", str(out)).returncode, 0); self.assertTrue(out.exists())
        antes = out.read_text(encoding="utf-8")
        r = self.run_script("acme/widget", "--out", str(out)); self.assertEqual(r.returncode, 2); self.assertIn("já existe", r.stderr)
        self.assertEqual(out.read_text(encoding="utf-8"), antes)

    def test_sem_description_nao_inventa_trecho(self):
        Api.payloads["/repos/acme/widget"] = dict(REPO_OK, description=None)
        o = self.run_script("acme/widget").stdout
        self.assertIn("Trecho literal: INDETERMINADO", o)


if __name__ == "__main__":
    unittest.main()
