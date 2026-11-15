"""Testes da reconciliação de telemetria pelos transcripts dos subagentes (DHR-TELEMETRIA-002)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import telemetria_tokens as T  # noqa: E402


_N = [0]


def linha(role, mid, usage=None, texto="", ts="2026-11-14T10:00:00.000Z", tool_ids=(), agent="a111", sess="S1"):
    m = {"role": role, "id": mid}
    if role == "assistant":
        m["model"] = "claude-opus-5-5"
        m["usage"] = usage or {}
        m["content"] = [{"type": "tool_use", "id": t, "name": "Read"} for t in tool_ids] or [{"type": "text", "text": texto}]
    else:
        m["content"] = [{"type": "text", "text": texto}]
    _N[0] += 1
    return {"agentId": agent, "sessionId": sess, "timestamp": ts, "message": m, "uuid": f"u-{_N[0]}"}   # uuid ÚNICO por linha, como no transcript real


def U(i, o, cc, cr):
    return {"input_tokens": i, "output_tokens": o, "cache_creation_input_tokens": cc, "cache_read_input_tokens": cr}


def monta(base, agent="a111", sess="S1", prompt="CLASSE-TAREFA: S3\nALVO: specs/features/SPEC-123/plan.md\nrevise", tipo="Revisor SOT", finished=True):
    sub = Path(base) / "proj" / sess / "subagents"
    sub.mkdir(parents=True, exist_ok=True)
    linhas = [linha("user", "p0", texto=prompt, ts="2026-11-14T10:00:00.000Z", agent=agent, sess=sess),
              # a MESMA resposta (mesmo id) repetida em 3 linhas: o transcript real faz isso
              linha("assistant", "m1", U(10, 100, 1000, 5000), ts="2026-11-14T10:01:00.000Z", tool_ids=("t1",), agent=agent, sess=sess),
              linha("assistant", "m1", U(10, 100, 1000, 5000), ts="2026-11-14T10:01:00.000Z", tool_ids=("t1",), agent=agent, sess=sess),
              linha("assistant", "m1", U(10, 100, 1000, 5000), ts="2026-11-14T10:01:00.000Z", tool_ids=("t1",), agent=agent, sess=sess),
              linha("assistant", "m2", U(20, 200, 500, 7000), ts="2026-11-14T10:03:00.000Z", tool_ids=("t2", "t3"), agent=agent, sess=sess)]
    arq = sub / f"agent-{agent}.jsonl"
    arq.write_text("\n".join(json.dumps(x) for x in linhas) + "\n", encoding="utf-8")
    arq.with_suffix(".meta.json").write_text(json.dumps({"agentType": tipo, "description": "rev", "model": "opus", "finished": finished}), encoding="utf-8")
    return arq


class TestLerTranscript(unittest.TestCase):
    def test_dedup_por_id_de_resposta(self):
        with tempfile.TemporaryDirectory() as td:
            u = T.ler_transcript(monta(td))
            self.assertEqual(u["mensagens"], 2)                      # 4 linhas de assistant, 2 respostas únicas
            self.assertEqual((u["in"], u["out"]), (30, 300))         # NÃO 50/500 (soma bruta de linhas)
            self.assertEqual((u["cache_create"], u["cache_read"]), (1500, 12000))
            self.assertEqual(u["tool_uses"], 3)
            self.assertEqual(u["duracao_ms"], 180000)
            self.assertEqual(u["janela_ms"], 180000)

    def test_registro_formato_e_total_so_tokens_novos(self):
        with tempfile.TemporaryDirectory() as td:
            r = T.registro_de_transcript(monta(td))
            self.assertEqual((r["agente"], r["model"], r["classe"], r["spec"]), ("Revisor SOT", "opus", "S3", "SPEC-123"))
            self.assertEqual(r["total"], 30 + 300 + 1500)            # in + out + cache criado; cache lido fica à parte
            self.assertEqual(r["fonte"], "transcript")
            self.assertTrue(r["finalizado"])
            self.assertEqual(r["agent_id"], "a111")

    def test_duracao_e_tempo_ativo_nao_a_janela(self):
        with tempfile.TemporaryDirectory() as td:
            arq = monta(td)
            # retomada 2 dias depois: a janela cresce, o tempo ativo NÃO
            extra = linha("assistant", "m9", U(1, 1, 1, 1), ts="2026-11-16T10:00:00.000Z")
            arq.write_text(arq.read_text(encoding="utf-8") + json.dumps(extra) + "\n", encoding="utf-8")
            u = T.ler_transcript(arq)
            self.assertEqual(u["duracao_ms"], 180000)
            self.assertGreaterEqual(u["janela_ms"], 172800000)

    def test_ilegivel_ou_sem_uso_devolve_none(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "agent-x.jsonl"
            p.write_text("lixo\n{}\n", encoding="utf-8")
            self.assertIsNone(T.ler_transcript(p))
            self.assertIsNone(T.ler_transcript(Path(td) / "nao-existe.jsonl"))

    def test_deterministico(self):
        with tempfile.TemporaryDirectory() as td:
            a = monta(td)
            self.assertEqual(T.registro_de_transcript(a), T.registro_de_transcript(a))


class TestReconciliar(unittest.TestCase):
    def test_idempotente_e_atualiza_quando_o_transcript_cresce(self):
        with tempfile.TemporaryDirectory() as td:
            saida = Path(td) / "uso.jsonl"
            monta(td)
            self.assertEqual(T.reconciliar(projetos=Path(td) / "proj", saida=saida), (1, 0))
            self.assertEqual(T.reconciliar(projetos=Path(td) / "proj", saida=saida), (0, 1))    # mesmo tamanho => não relê
            self.assertEqual(len(saida.read_text(encoding="utf-8").splitlines()), 1)
            arq = Path(td) / "proj" / "S1" / "subagents" / "agent-a111.jsonl"
            extra = linha("assistant", "m3", U(1, 1, 1, 1), ts="2026-11-14T10:05:00.000Z")
            arq.write_text(arq.read_text(encoding="utf-8") + json.dumps(extra) + "\n", encoding="utf-8")
            self.assertEqual(T.reconciliar(projetos=Path(td) / "proj", saida=saida), (1, 0))    # cresceu => atualiza
            regs = [json.loads(x) for x in saida.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(regs), 1)                                                      # 1 registro por agente (upsert)
            self.assertEqual(regs[0]["mensagens"], 3)

    def test_versao_antiga_do_registro_e_relida(self):
        with tempfile.TemporaryDirectory() as td:
            saida = Path(td) / "uso.jsonl"
            monta(td)
            T.reconciliar(projetos=Path(td) / "proj", saida=saida)
            r = json.loads(saida.read_text(encoding="utf-8").splitlines()[0])
            r["v"] = 1
            saida.write_text(json.dumps(r) + "\n", encoding="utf-8")
            self.assertEqual(T.reconciliar(projetos=Path(td) / "proj", saida=saida), (1, 0))   # formato antigo => relê

    def test_substitui_stubs_de_lancamento_da_sessao(self):
        with tempfile.TemporaryDirectory() as td:
            saida = Path(td) / "uso.jsonl"
            stub = {"t": 1, "tool": "Agent", "agente": "Revisor SOT", "sessao": "S1", "total": None, "lancamento": True}
            stub_outra = {"t": 1, "tool": "Agent", "agente": "Revisor SOT", "sessao": "OUTRA", "total": None}
            saida.write_text(json.dumps(stub) + "\n" + json.dumps(stub_outra) + "\n", encoding="utf-8")
            monta(td)
            T.reconciliar(projetos=Path(td) / "proj", saida=saida)
            regs = [json.loads(x) for x in saida.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(regs), 2)
            self.assertEqual({r.get("sessao") for r in regs}, {"S1", "OUTRA"})                 # stub de S1 sumiu; o de OUTRA fica
            self.assertEqual([r for r in regs if r.get("sessao") == "S1"][0]["fonte"], "transcript")

    def test_resumo_nao_conta_lancamento_e_mostra_tokens(self):
        regs = [{"tool": "Agent", "agente": "Revisor SOT", "model": "opus", "classe": "S3", "total": None, "lancamento": True},
                {"tool": "Agent", "agente": "Revisor SOT", "model": "opus", "classe": "S3", "total": 1830, "in": 30, "out": 300, "cache_read": 0, "cache_create": 1500, "fonte": "transcript"}]
        g = T.resumo(regs)
        v = g[("Revisor SOT", "opus", "S3")]
        self.assertEqual((v["chamadas"], v["sem_tokens"], v["total"]), (1, 0, 1830))

    def test_hook_subagentstop_reconcilia_o_agente(self):
        with tempfile.TemporaryDirectory() as td:
            saida = Path(td) / "uso.jsonl"
            arq = monta(td)
            T.reconciliar(caminho=arq, saida=saida)
            self.assertEqual(json.loads(saida.read_text(encoding="utf-8").splitlines()[0])["agent_id"], "a111")

    def test_cli_tokens(self):
        with tempfile.TemporaryDirectory() as td:
            saida = Path(td) / "uso.jsonl"
            T.reconciliar(caminho=monta(td), saida=saida)
            old = T.SAIDA
            try:
                T.SAIDA = saida
                self.assertEqual(T.main(["x", "tokens", "a111"]), 0)
                self.assertEqual(T.main(["x", "tokens", "naoexiste"]), 1)
            finally:
                T.SAIDA = old


if __name__ == "__main__":
    unittest.main()
