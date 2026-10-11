"""Testes da ferramenta estreita do Revisor (scripts/revisor_gate_mcp.py) — DHR-AUDITOR-EXTERNO-009, fase F2.
O foco é RECUSA: a segurança está no servidor, não no comportamento do modelo."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVER = ROOT / "scripts" / "revisor_gate_mcp.py"


def rpc(msgs, env_extra=None, timeout=240):
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", **(env_extra or {})}
    entrada = "\n".join(json.dumps(m, ensure_ascii=False) for m in msgs) + "\n"
    p = subprocess.run([sys.executable, str(SERVER)], input=entrada, capture_output=True, text=True,
                       encoding="utf-8", env=env, timeout=timeout)
    return [json.loads(l) for l in p.stdout.splitlines() if l.strip()], p


def call(args, rid=2, name="revisor_gate", env_extra=None):
    out, _ = rpc([{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05"}},
                  {"jsonrpc": "2.0", "method": "notifications/initialized"},
                  {"jsonrpc": "2.0", "id": rid, "method": "tools/call", "params": {"name": name, "arguments": args}}], env_extra)
    return next(r for r in out if r.get("id") == rid)


def texto(resp):
    return resp["result"]["content"][0]["text"]


class TestProtocolo(unittest.TestCase):
    def test_initialize_e_lista_com_uma_unica_ferramenta(self):
        out, p = rpc([{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05"}},
                      {"jsonrpc": "2.0", "method": "notifications/initialized"},
                      {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}])
        self.assertEqual(out[0]["result"]["serverInfo"]["name"], "sot-revisor-gate")
        self.assertEqual(len(out), 2)                                           # a notificação não gera resposta
        ferramentas = out[1]["result"]["tools"]
        self.assertEqual([t["name"] for t in ferramentas], ["revisor_gate"])    # nenhuma ferramenta de escrita/execução
        self.assertEqual(p.stderr.strip(), "")

    def test_metodo_desconhecido_e_ferramenta_desconhecida(self):
        out, _ = rpc([{"jsonrpc": "2.0", "id": 1, "method": "resources/list"},
                      {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "Bash", "arguments": {"command": "ls"}}}])
        self.assertEqual(out[0]["error"]["code"], -32601)
        self.assertEqual(out[1]["error"]["code"], -32602)

    def test_lixo_na_entrada_nao_derruba_o_servidor(self):
        out, p = rpc([{"jsonrpc": "2.0", "id": 1, "method": "ping"}])
        self.assertEqual(out[0]["result"], {})


class TestRecusas(unittest.TestCase):
    def assertRecusado(self, args):
        r = call(args)
        self.assertTrue(r["result"].get("isError"), f"deveria recusar: {args!r}")
        self.assertIn("RECUSADO", texto(r), args)

    def test_argumentos_fora_do_padrao(self):
        for spec in ["../x; echo hacked", "SPEC-001; ls", "SPEC-001 && touch pwn", "SPEC-001\nSPEC-002", "$(id)", "`id`",
                     "specs/features/SPEC-001/plan.md", "../../etc/passwd", "SPEC-1", "SPEC-0001", "spec-001", "SPEC-00a",
                     " SPEC-001", "SPEC-001 ", "SPEC-001/../SPEC-002", "SPEC-001\x00", "", "SPEC-"]:
            self.assertRecusado({"spec": spec})

    def test_tipos_errados_e_argumentos_extras(self):
        for args in [{}, {"spec": None}, {"spec": 1}, {"spec": ["SPEC-001"]}, {"spec": {"a": 1}}, None, [], "SPEC-001",
                     {"spec": "SPEC-001", "command": "ls"}, {"spec": "SPEC-001", "rapido": "sim"}, {"spec": "SPEC-001", "path": "/"}]:
            self.assertRecusado(args)

    def test_spec_inexistente(self):
        self.assertRecusado({"spec": "SPEC-999"})

    def test_nenhum_efeito_colateral_de_comando_injetado(self):
        with tempfile.TemporaryDirectory() as d:
            marcador = Path(d) / "pwn"
            for spec in [f"SPEC-001; touch {marcador}", f"SPEC-001 && echo x > {marcador}", f"$(touch {marcador})"]:
                self.assertRecusado({"spec": spec})
            self.assertFalse(marcador.exists())

    def test_symlink_para_fora_de_specs_features_e_barrado(self):
        with tempfile.TemporaryDirectory() as repo, tempfile.TemporaryDirectory() as fora:
            (Path(fora) / "plan.md").write_text("# fora\n", encoding="utf-8")
            feats = Path(repo) / "specs" / "features"
            feats.mkdir(parents=True)
            try:
                os.symlink(fora, feats / "SPEC-001", target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("sem permissão para criar symlink neste ambiente")
            r = call({"spec": "SPEC-001"}, env_extra={"SOT_REPO": repo})
            self.assertTrue(r["result"].get("isError"))
            self.assertIn("RECUSADO", texto(r))


class TestCodificacao(unittest.TestCase):
    """Regressão (achada na F3 com agente de arquivo real): no Windows a saída padrão é cp1252 e o relatório tem '≠', '→', '—';
    o servidor quebrava com 'Connection closed' no caminho feliz. Simula a codificação do sistema e exige sucesso."""

    def test_caminho_feliz_com_saida_padrao_em_cp1252(self):
        r = call({"spec": "SPEC-001", "rapido": True}, env_extra={"PYTHONIOENCODING": "cp1252", "PYTHONUTF8": "0"})
        self.assertFalse(r["result"].get("isError"), r)
        self.assertIn("≠", texto(r))                                            # o caractere que quebrava chega íntegro

    def test_recusa_com_acento_chega_integra_em_cp1252(self):
        r = call({"spec": "SPEC-001 && echo x"}, env_extra={"PYTHONIOENCODING": "cp1252", "PYTHONUTF8": "0"})
        self.assertIn("fora do padrão SPEC-NNN", texto(r))                      # 'ã' sem virar '�'


class TestExecucao(unittest.TestCase):
    def test_spec_real_roda_o_gate_somente_leitura(self):
        antes = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
        r = call({"spec": "SPEC-001", "rapido": True})
        self.assertFalse(r["result"].get("isError"), r)
        t = texto(r)
        self.assertIn("PASSOU_D", t)
        self.assertIn("baselines_na_raiz", t)
        self.assertIn("Classe P", t)                                           # deixa claro que não é parecer
        depois = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
        self.assertEqual(antes, depois)

    def test_modo_completo_inclui_detectores_do_repositorio(self):
        r = call({"spec": "SPEC-001"})
        self.assertFalse(r["result"].get("isError"), r)
        t = texto(r)
        for nome in ["check_refs", "check_doc_sync", "backlog_triggers", "check_rpsa", "build_map_check"]:
            self.assertIn(nome, t)


if __name__ == "__main__":
    unittest.main()
