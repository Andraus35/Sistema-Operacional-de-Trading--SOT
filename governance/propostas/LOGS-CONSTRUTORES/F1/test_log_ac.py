import json, os, tempfile, threading, unittest, io, contextlib
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
    def test_metrics_chaves_fechadas(self): self.assertTrue(L.valida(ev(metrics={"cwd": 1})))
    def test_redacted_lista_de_strings(self): self.assertTrue(L.valida(ev(redacted=[1])))
    def test_schema_json_bem_formado(self): self.assertEqual(L.SCHEMA["properties"]["family"]["const"], "AC")

    # --- R1 ---
    def test_r1_a04_chave_com_segredo(self): self.assertTrue(L.valida(ev(redacted=["sk-abcdefghijklmnopqrstuv"])))
    def test_r1_a04_chaves_de_conteudo(self):
        for k in ("system_prompt", "input", "args", "body"): self.assertTrue(L.valida(ev(**{k: "x"})), k)
    def test_r1_a04_path_absoluto_ou_pai(self):
        for pth in ("/home/u/x.md", "../x.md", "C:/x.md", "a/../b.md"):
            self.assertTrue(L.valida(ev(output_ref={"path": pth, "sha256": "a" * 64})), pth)
    def test_r1_a04_campos_com_limite(self):
        self.assertTrue(L.valida(ev(task_ref="x" * 129))); self.assertTrue(L.valida(ev(status="x" * 129)))
    def test_r1_a04_padroes_novos(self):
        for r in ("api_key=abcdef12", "Authorization: Basic dXNlcjpwYXNz", "https://u:pw@host/x", "github_pat_" + "a" * 30,
                  "xoxb-1234567890-abc", "AIza" + "a" * 30, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV", "bearer abcdefghijklmnop1234", "pwd=abcd"):
            self.assertTrue(L.valida(ev(reason=r)), r)
    def test_r1_a04_sem_falso_positivo_comum(self):
        for r in ("tokens: 1234567", "R-AC7: model ausente", "classe M enviada a agente", "senha nao informada"):
            self.assertEqual(L.valida(ev(reason=r)), [], r)
    def test_r1_a04_saneia_preserva_deny(self):
        e = ev(event="policy.decision", decision="deny", policy_id="R-AC7", reason="token=abcdef123", severity="AUDIT")
        self.assertTrue(L.valida(e)); s = L.saneia(e)
        self.assertEqual(L.valida(s), []); self.assertIsNone(s["reason"]); self.assertIn("reason", s["redacted"])
    def test_r1_a05_sessao_em_claro_recusada_em_L2_L3(self):
        for c in ("L2", "L3"): self.assertTrue(L.valida(ev(), c))
        self.assertEqual(L.valida(ev(session_id=L.hash_sessao("s1")), "L2"), [])
        self.assertEqual(L.valida(ev()), [])  # L1 local pode ficar em claro
    def test_r1_a13_newline_final(self):
        self.assertTrue(L.valida(ev(ts="2026-11-01T12:00:00Z\n")))
        self.assertTrue(L.valida(ev(output_ref={"path": "a.md", "sha256": "a" * 64 + "\n"})))
    def test_r1_a13_chave_nao_ascii(self): self.assertTrue(L.valida(ev(redacted=[]) | {"açao": 1}))
    def test_r1_a03_concorrencia_sem_bifurcar(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"; erros = []
            def w(i):
                try:
                    for j in range(15): L.acrescenta(f, ev(run_id=f"r{i}-{j}"))
                except Exception as e: erros.append(e)
            ts = [threading.Thread(target=w, args=(i,)) for i in range(8)]
            [t.start() for t in ts]; [t.join() for t in ts]
            self.assertEqual(erros, []); self.assertEqual(len(f.read_text().splitlines()), 120); self.assertEqual(L.verifica(f), [])
    def test_r1_a03_truncamento_do_fim_com_ancora(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            for i in range(4): s = L.acrescenta(f, ev(run_id=f"r{i}"))
            cabeca = s["hash"]; self.assertEqual(L.verifica(f, cabeca), [])
            ls = f.read_text().splitlines(); f.write_text("\n".join(ls[:-1]) + "\n")
            self.assertEqual(L.verifica(f), [])  # sem ancora: nao detecta (limite declarado)
            self.assertTrue(any("cabeca" in p for p in L.verifica(f, cabeca)))
    def test_r1_a03_remocao_da_cabeca(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            for i in range(3): L.acrescenta(f, ev(run_id=f"r{i}"))
            ls = f.read_text().splitlines(); f.write_text("\n".join(ls[1:]) + "\n")
            self.assertTrue(L.verifica(f))
    def test_r1_a03_segmento_continua_de(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / "a.jsonl", Path(d) / "b.jsonl"
            s = L.acrescenta(a, ev(run_id="r0"))
            fd = os.open(b, os.O_WRONLY | os.O_CREAT); os.close(fd)
            b.write_text(json.dumps(L.sela(ev(run_id="r1"), s["hash"])) + "\n")
            self.assertEqual(L.verifica(b, continua_de=s["hash"]), []); self.assertTrue(L.verifica(b))
    def test_r1_a02_le_so_a_cauda(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            for i in range(3): L.acrescenta(f, ev(run_id=f"r{i}"))
            antigo = L.CAUDA; L.CAUDA = 512
            try:
                for i in range(3, 12): L.acrescenta(f, ev(run_id=f"r{i}"))
            finally: L.CAUDA = antigo
            self.assertEqual(L.verifica(f), [])
    def test_r1_a01_emite_seguro_nunca_levanta(self):
        import unittest.mock as m
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            for exc in (ValueError("x"), KeyError("k"), RecursionError(), OSError("ro"), RuntimeError("r"), json.JSONDecodeError("m", "d", 0)):
                with m.patch.object(L, "acrescenta", side_effect=exc), contextlib.redirect_stderr(io.StringIO()) as err:
                    ok, motivo = L.emite_seguro(f, ev(), canal_warn="stderr")
                self.assertFalse(ok); self.assertIn("WARN", err.getvalue())
    def test_r1_a01_falha_de_os_open_nao_levanta(self):
        import unittest.mock as m
        with tempfile.TemporaryDirectory() as d:
            for exc in (PermissionError("ro"), OSError(28, "disco cheio")):
                with m.patch("os.open", side_effect=exc), contextlib.redirect_stderr(io.StringIO()):
                    ok, _ = L.emite_seguro(Path(d) / "l.jsonl", ev(), canal_warn="stderr")
                self.assertFalse(ok)
    def test_r1_a01_emite_seguro_grava_evento_minimo(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            ok, _ = L.emite_seguro(f, ev(event="policy.decision", decision="deny", policy_id="R-AC7", reason="token=abcdef123"))
            self.assertTrue(ok); self.assertIsNone(json.loads(f.read_text())["reason"])

    # --- R2: itens pendentes apontados pelo Especificador ---
    def test_r2_approval_exige_ata_em_L2(self):
        e = ev(event="approval.decided", session_id=L.hash_sessao("s"), severity="AUDIT", status="DECIDED")
        self.assertTrue(L.valida(e, "L2"))
        self.assertEqual(L.valida(dict(e, input_ref={"path": "governance/DHR-X.md", "sha256": "b" * 64}), "L2"), [])
        self.assertEqual(L.valida(dict(e, status="sem-ata"), "L2"), [])
        self.assertEqual(L.valida(e, "L1"), [])
    def test_r2_ancora_de_linha_prefixo(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"; hs = [L.acrescenta(f, ev(run_id=f"r{i}"))["hash"] for i in range(5)]
            self.assertEqual(L.verifica(f, ancora_linha=(3, hs[2])), [])
            self.assertTrue(L.verifica(f, ancora_linha=(3, hs[1])))
            ls = f.read_text().splitlines(); f.write_text("\n".join(ls[:2]) + "\n")
            self.assertTrue(any("truncamento" in p for p in L.verifica(f, ancora_linha=(3, hs[2]))))
    def test_r2_canal_warn_arquivo_sem_stderr(self):
        import unittest.mock as m
        with tempfile.TemporaryDirectory() as d:
            os.environ["LOG_AC_FALHAS"] = str(Path(d) / "falhas.log")
            try:
                with m.patch.object(L, "acrescenta", side_effect=RuntimeError()), contextlib.redirect_stderr(io.StringIO()) as err:
                    ok, _ = L.emite_seguro(Path(d) / "x.jsonl", ev(), canal_warn="arquivo")
                self.assertFalse(ok); self.assertEqual(err.getvalue(), ""); self.assertIn("WARN", (Path(d) / "falhas.log").read_text())
            finally: del os.environ["LOG_AC_FALHAS"]
    def test_r2_cli_emit_e_verify(self):
        import subprocess, sys as S
        with tempfile.TemporaryDirectory() as d:
            f = str(Path(d) / "l.jsonl"); alvo = str(Path(L.__file__))
            for i in range(2):
                r = subprocess.run([S.executable, "-B", alvo, "emit", f, json.dumps(ev(run_id=f"r{i}"))], capture_output=True, text=True); self.assertEqual(r.returncode, 0)
            r = subprocess.run([S.executable, "-B", alvo, "verify", f], capture_output=True, text=True); self.assertEqual(r.returncode, 0, r.stdout)
            Path(f).write_text(Path(f).read_text().replace("SUCCEEDED", "FAILED"))
            r = subprocess.run([S.executable, "-B", alvo, "verify", f], capture_output=True, text=True); self.assertEqual(r.returncode, 1)
    def test_r2_cli_emit_json_invalido_exit0(self):
        import subprocess, sys as S
        r = subprocess.run([S.executable, "-B", str(Path(L.__file__)), "emit", "x.jsonl", "{nao"], capture_output=True, text=True); self.assertEqual(r.returncode, 0)

    # --- R3: achados B01..B13 do parecer R2 ---
    def test_r3_b01_trava_presa_nao_bloqueia(self):
        import subprocess, sys as S, time
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"; L.acrescenta(f, ev())
            seg = subprocess.Popen([S.executable, "-c", "import fcntl,os,sys,time;fd=os.open(sys.argv[1],os.O_RDWR);fcntl.flock(fd,fcntl.LOCK_EX);print('ok',flush=True);time.sleep(4)", str(f)], stdout=subprocess.PIPE, text=True)
            try:
                self.assertEqual(seg.stdout.readline().strip(), "ok")
                antigo = L.LOCK_PRAZO; L.LOCK_PRAZO = 0.3; t0 = time.monotonic()
                try:
                    with contextlib.redirect_stderr(io.StringIO()): ok, motivo = L.emite_seguro(f, ev(run_id="x"), canal_warn="stderr")
                finally: L.LOCK_PRAZO = antigo
                self.assertFalse(ok); self.assertEqual(motivo, "TimeoutError"); self.assertLess(time.monotonic() - t0, 2.0)
                self.assertEqual(len(f.read_text().splitlines()), 1)
            finally: seg.kill(); seg.wait()
    def test_r3_b04_camada_forcada_pelo_destino(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d) / "governance" / "logs"
            self.assertEqual(L.camada_do_caminho(base / "L2" / "a.jsonl"), "L2")
            self.assertEqual(L.camada_do_caminho(Path(d) / "x.jsonl"), "L1")
            with self.assertRaises(ValueError): L.camada_do_caminho(base / "a.jsonl")          # dentro de logs, fora de L2/L3
            with self.assertRaises(ValueError): L.camada_do_caminho(base / "L2" / "a.jsonl", "L1")  # conflito
            with self.assertRaises(ValueError): L.camada_do_caminho(Path(d) / "x.jsonl", "l2")      # valor desconhecido
            with self.assertRaises(ValueError): L.acrescenta(base / "L2" / "a.jsonl", ev())         # esquecimento: sessao em claro
            self.assertFalse((base / "L2" / "a.jsonl").exists())
            L.acrescenta(base / "L3" / "a.jsonl", ev(session_id=L.hash_sessao("s")))
    def test_r3_b04_cli_camada_invalida_exit0(self):
        import subprocess, sys as S
        with tempfile.TemporaryDirectory() as d:
            env = dict(os.environ, LOG_AC_FALHAS=str(Path(d) / "f.log"))
            for args in (["--camada"], ["--camada", "L9"]):
                r = subprocess.run([S.executable, "-B", str(Path(L.__file__)), "emit", str(Path(d) / "x.jsonl"), json.dumps(ev())] + args, capture_output=True, text=True, env=env)
                self.assertEqual(r.returncode, 0, r.stderr); self.assertFalse((Path(d) / "x.jsonl").exists())
    def test_r3_b06_separadores_unicode_de_linha(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"
            for ch in ("\u0085", "\u2028", "\u2029", "\x0b", "\x1c"):
                L.acrescenta(f, ev(reason=f"a{ch}b"))
            self.assertEqual(L.verifica(f), [])
            self.assertEqual(len([l for l in f.read_bytes().decode().split("\n") if l]), 5)
    def test_r3_b05_fallback_de_ids(self):
        base = {k: v for k, v in BASE.items() if k not in ("session_id", "run_id", "agent_id")}
        e = L.completa_ids(base, {}); self.assertEqual(L.valida(e), [])
        pl = {"session_id": "s9", "tool_use_id": "tu_1", "tool_name": "Agent", "tool_input": {"subagent_type": "revisor"}}
        e = L.completa_ids(base, pl); self.assertEqual((e["session_id"], e["run_id"], e["agent_id"]), ("s9", "tu_1", "revisor"))
        self.assertEqual(L.completa_ids(base, {"tool_name": "Agent"})["run_id"], L.completa_ids(base, {"tool_name": "Agent"})["run_id"])
    def test_r3_b08_saneia_campos_obrigatorios(self):
        e = ev(status="token=abcdef123", task_ref="password=hunter22x")
        self.assertTrue(L.valida(e)); s = L.saneia(e)
        self.assertEqual(L.valida(s), []); self.assertEqual(s["status"], "[redigido]"); self.assertIsNone(s["task_ref"])
        self.assertTrue({"status", "task_ref"} <= set(s["redacted"]))
    def test_r3_b08_cauda_corrompida_nao_grava_e_nao_levanta(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "l.jsonl"; L.acrescenta(f, ev()); f.write_text(f.read_text() + '{"parcial": ')
            antes = f.read_text()
            with contextlib.redirect_stderr(io.StringIO()): ok, _ = L.emite_seguro(f, ev(run_id="n"), canal_warn="stderr")
            self.assertFalse(ok); self.assertEqual(f.read_text(), antes)  # falha fechada: nao encadeia sobre lixo
    def test_r3_b02_semente_continua_de(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / "a.jsonl", Path(d) / "b.jsonl"
            s = L.acrescenta(a, ev(run_id="r0")); L.acrescenta(b, ev(run_id="r1"), continua_de=s["hash"]); L.acrescenta(b, ev(run_id="r2"), continua_de=s["hash"])
            self.assertEqual(L.verifica(b, continua_de=s["hash"]), []); self.assertTrue(L.verifica(b))
    def test_r3_b12_approval_so_ata_governance(self):
        e = ev(event="approval.decided", session_id=L.hash_sessao("s"), severity="AUDIT", status="DECIDED")
        for pth in ("x.md", "docs/DHR-X.md", "governance/outro.md", "governance/DHR-X.txt"):
            self.assertTrue(L.valida(dict(e, input_ref={"path": pth, "sha256": "b" * 64}), "L2"), pth)
        self.assertEqual(L.valida(dict(e, input_ref={"path": "governance/DHR-LOGS-AC-001_Ata.md", "sha256": "b" * 64}), "L2"), [])
    def test_r3_decision_block(self):
        self.assertEqual(L.valida(ev(event="policy.decision", decision="block", policy_id="stop-hook")), [])
    def test_r3_b07_varre_isolado(self):
        for obj in ({"system_prompt": 1}, {"sk-abcdefghijklmnopqrstuv": 1}, {"açao": 1}):
            er = []; L._varre(obj, "$", er); self.assertTrue(er, obj)
    def test_r3_b13_raiz_e_warn_ancorados(self):
        self.assertTrue((L.raiz_repo() / ".git").exists() or os.environ.get("LOG_AC_RAIZ"))

    def test_r4_emit_sem_argumentos_exit0_e_warn_com_data(self):
        import subprocess, sys as S, re
        with tempfile.TemporaryDirectory() as d:
            env = dict(os.environ, LOG_AC_FALHAS=str(Path(d) / "f.log"))
            r = subprocess.run([S.executable, "-B", str(Path(L.__file__)), "emit"], capture_output=True, text=True, env=env)
            self.assertEqual(r.returncode, 0)
            self.assertRegex((Path(d) / "f.log").read_text(), r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z log_ac WARN")
    def test_r4_esquema_tem_id(self): self.assertTrue(L.SCHEMA.get("$id"))

if __name__ == "__main__": unittest.main()
