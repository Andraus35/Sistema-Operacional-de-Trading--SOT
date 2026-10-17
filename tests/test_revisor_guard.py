"""Testes da guarda determinística do fim do Revisor (scripts/revisor_guard.py) — DHR-AUDITOR-EXTERNO-017."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import revisor_guard as g  # noqa: E402

PLAN = str(ROOT / "specs" / "features" / "SPEC-005" / "plan.md")


def transcript(tmp, prompt, leituras):
    """JSONL no formato do transcript de subagente: 1ª mensagem do usuário + tool_use de leitura."""
    p = Path(tmp) / "agent.jsonl"
    linhas = [json.dumps({"type": "user", "message": {"role": "user", "content": prompt}})]
    for alvo in leituras:
        linhas.append(json.dumps({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Read", "input": {"file_path": alvo}}]}}))
    p.write_text("\n".join(linhas), encoding="utf-8")
    return str(p)


NUCLEO_ABERTO = ["/x/ROADMAP.md", "/x/atomic-spec.md", "/x/governance/RULES.md", "/x/backlog/RMR-001_Painel_Backlog.md"]
GATE_FAKE = ({"veredito_D": "PASSOU_D"}, ["VEREDITO D: PASSOU_D (fake)", "  sinais H: 0"])


class TestGuarda(unittest.TestCase):
    def evento(self, tmp, leituras, final, **kw):
        return {"agent_type": "Revisor SOT", "agent_transcript_path": transcript(tmp, f"Audite {PLAN}", leituras),
                "last_assistant_message": final, "stop_hook_active": False, **kw}

    def test_ignora_agente_que_nao_e_revisor(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(g.avaliar(self.evento(t, [], "x", agent_type="general-purpose")), [])

    def test_libera_quando_ja_continuou_uma_vez(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(g.avaliar(self.evento(t, [], "x", stop_hook_active=True)), [])

    def test_g1_exige_nucleo_aberto(self):
        with tempfile.TemporaryDirectory() as t, mock.patch.object(g, "rodar_gate", return_value=GATE_FAKE):
            msgs = g.avaliar(self.evento(t, ["/x/atomic-spec.md"], "VEREDITO D: PASSOU_D"))
        txt = " ".join(msgs)
        self.assertIn("G1", txt)
        self.assertIn("ROADMAP.md", txt)
        self.assertIn("RMR-001", txt)
        self.assertNotIn("atomic-spec.md,", txt.split("G1")[1].split(".")[0] + ",")

    def test_g2_injeta_o_gate_quando_o_parecer_diz_nao_verificado(self):
        with tempfile.TemporaryDirectory() as t, mock.patch.object(g, "rodar_gate", return_value=GATE_FAKE):
            msgs = g.avaliar(self.evento(t, NUCLEO_ABERTO, "GATE NÃO VERIFICADO — ferramenta indisponível"))
        self.assertTrue(any(m.startswith("G2") and "PASSOU_D (fake)" in m for m in msgs), msgs)

    def test_g2_nao_dispara_quando_o_parecer_traz_o_veredito_d(self):
        with tempfile.TemporaryDirectory() as t, mock.patch.object(g, "rodar_gate", return_value=GATE_FAKE):
            self.assertEqual(g.avaliar(self.evento(t, NUCLEO_ABERTO, "3. GATE: VEREDITO D: PASSOU_D")), [])

    def test_g3_citacao_valida_passa_e_inventada_falha(self):
        bom = "`atomic-spec.md:116` diz `D5 (estado) + ≥ 3 cenários D7`"
        self.assertEqual(g.conferir_citacoes(bom, []), [])
        ruim = "`atomic-spec.md:274` diz `| ENF-09 | Gates de gaming e inflação de nível |`"
        r = g.conferir_citacoes(ruim, [])
        self.assertEqual(len(r), 1, r)
        self.assertIn("não está no arquivo", r[0])

    def test_g3_linha_alem_do_fim_e_arquivo_inexistente(self):
        r = g.conferir_citacoes("ver atomic-spec.md:99999 e governance/NAO-EXISTE.md:3", [])
        self.assertTrue(any("tem só" in x for x in r), r)
        self.assertTrue(any("arquivo não encontrado" in x for x in r), r)

    def test_g3_trecho_na_linha_errada_e_apontado(self):
        r = g.conferir_citacoes("`atomic-spec.md:5` diz `D5 (estado) + ≥ 3 cenários D7`", [])
        self.assertTrue(any("em outra linha" in x for x in r), r)

    def test_g3_sem_trecho_so_confere_a_linha(self):
        self.assertEqual(g.conferir_citacoes("veja atomic-spec.md:116", []), [])

    def test_hook_como_processo_sai_com_2_e_mensagem(self):
        with tempfile.TemporaryDirectory() as t:
            ev = self.evento(t, [], "`atomic-spec.md:274` diz `| ENF-09 | Gates de gaming e inflação de nível |`")
            p = subprocess.run([sys.executable, str(ROOT / "scripts" / "revisor_guard.py")], input=json.dumps(ev), capture_output=True, text=True, encoding="utf-8", timeout=180)
        self.assertEqual(p.returncode, 2, p.stderr)
        self.assertIn("G1", p.stderr)
        self.assertIn("G3", p.stderr)

    def test_entrada_invalida_nao_derruba(self):
        p = subprocess.run([sys.executable, str(ROOT / "scripts" / "revisor_guard.py")], input="isto não é json", capture_output=True, text=True, timeout=60)
        self.assertEqual(p.returncode, 0)


if __name__ == "__main__":
    unittest.main()
