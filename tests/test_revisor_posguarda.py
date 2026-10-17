"""Testes da guarda pós-Revisor (scripts/revisor_posguarda.py) — DHR-AUDITOR-EXTERNO-018."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import revisor_posguarda as p  # noqa: E402

PLAN = str(ROOT / "specs" / "features" / "SPEC-005" / "plan.md")
AID = "abc1234567890def"


def montar(tmp, tipo="Revisor SOT", final="parecer sem gate"):
    sess = Path(tmp) / "sess.jsonl"
    sess.write_text(json.dumps({"type": "user", "message": {"content": f'[Subagent hand-back] <agent-message from="{AID}"> x'}}) + "\n", encoding="utf-8")
    sub = Path(tmp) / "sess" / "subagents"
    sub.mkdir(parents=True)
    (sub / f"agent-{AID}.meta.json").write_text(json.dumps({"agentType": tipo}), encoding="utf-8")
    linhas = [json.dumps({"type": "user", "message": {"content": f"audite {PLAN}"}}),
              json.dumps({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "SubagentHandback", "input": {"message": final}}]}})]
    (sub / f"agent-{AID}.jsonl").write_text("\n".join(linhas), encoding="utf-8")
    return str(sess)


GATE_FAKE = ({"veredito_D": "PASSOU_D"}, ["VEREDITO D: PASSOU_D (fake)", "  sinais H: 0"])


class PosGuarda(unittest.TestCase):
    def test_revisor_sem_gate_e_bloqueado_uma_vez(self):
        with tempfile.TemporaryDirectory() as t, mock.patch.object(p.g, "rodar_gate", return_value=GATE_FAKE):
            s = montar(t)
            a = p.avaliar_sessao(s, Path(t) / "est")
            self.assertEqual(len(a), 1)
            self.assertTrue(any("G1" in m for m in a[0][1]) and any("G2" in m for m in a[0][1]))
            self.assertEqual(p.avaliar_sessao(s, Path(t) / "est"), [])      # 1 vez por agente

    def test_outro_agente_e_ignorado(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(p.avaliar_sessao(montar(t, tipo="Explore"), Path(t) / "est"), [])

    def test_sem_transcript_libera(self):
        self.assertEqual(p.ids_entregues([]), [])


if __name__ == "__main__":
    unittest.main()
