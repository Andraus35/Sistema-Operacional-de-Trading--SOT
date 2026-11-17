"""Testes do fsm_check.py (proposta P16; informativo) — python -m unittest tests/test_fsm_check.py"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "fsm_check.py"
sys.path.insert(0, str(SCRIPT.parent))
import fsm_check as fc  # noqa: E402

TAB = """## D5 — Estado
| ID | Estado | Evento | Guarda (D) | Próximo | Ação | Código (`entry_type`/code) | Dono |
|---|---|---|---|---|---|---|---|
| F01 | — | `CYCLE_REQUEST` | ok | `A` | despacha | `MDC_OPENED` | X |
| F02 | `A` | `PUB_OK` | — | `B` | — | `MDC_B` | X |
| F03 | `B` | `STOP_COMMAND` | — | ENC | — | `MDC_STOP` | X |
| F04 | `A` | `DISPATCH_PUBLISH_FAILED` | — | (sem transição) | — | `MDC_FAIL` | X |
"""
CEN = """### Cenário-T01 — feliz
```
QUANDO PUB_OK
VERIFICAÇÃO code == "MDC_B"; fsm_row F02
```
### ADV-01 — x
```
VERIFICAÇÃO fsm_row: F03
```
"""


def msgs(texto, **kw):
    return [x for x in fc.verificar(texto, **kw)["achados"]]


class TestFsm(unittest.TestCase):
    def test_limpo_so_tem_iv(self):
        a = msgs(TAB + CEN)
        self.assertEqual([x["verif"] for x in a if x["verif"] != "iv"], [])

    def test_i_linha_inexistente(self):  # mutante: cenário cita F99
        a = msgs(TAB + CEN.replace("F02", "F99"))
        self.assertTrue(any(x["verif"] == "i" and "F99" in x["msg"] for x in a))

    def test_i_codigo_sem_linha(self):  # mutante: código inventado
        a = msgs(TAB + CEN.replace("MDC_B", "MDC_NOVO"))
        self.assertTrue(any(x["verif"] == "i" and "MDC_NOVO" in x["msg"] for x in a))

    def test_i_codigo_declarado_fora_nao_acusa(self):
        a = msgs(TAB + "\nTexto: o código MDC_NOVO é declarado na regra.\n" + CEN.replace("MDC_B", "MDC_NOVO"))
        self.assertFalse(any("MDC_NOVO" in x["msg"] for x in a))

    def test_i_evento_fora_da_tabela(self):
        a = msgs(TAB + CEN.replace("PUB_OK", "TIMER_FIRED"))
        self.assertTrue(any(x["verif"] == "i" and "TIMER_FIRED" in x["msg"] for x in a))

    def test_ii_estado_inalcancavel(self):  # mutante: linha com origem que ninguém alcança
        t = TAB + "| F05 | `Z` | `X_EVT` | — | `B` | — | `MDC_Z` | X |\n| F06 | `B` | `OUTRO` | — | `Z` | — | `MDC_Z2` | X |\n"
        # Z é alcançável via F06 (B→Z) ⇒ sem achado
        self.assertFalse(any(x["verif"] == "ii" for x in msgs(t)))
        t2 = TAB + "| F05 | `Z` | `X_EVT` | — | `B` | — | `MDC_Z` | X |\n| F06 | `W` | `OUTRO` | — | `Z` | — | `MDC_Z2` | X |\n"
        self.assertTrue(any(x["verif"] == "ii" and "`Z`" in x["msg"] for x in msgs(t2)))

    def test_ii_aciclico(self):
        t = TAB + "| F05 | `B` | `VOLTA` | — | `A` | — | `MDC_V` | X |\n"
        self.assertFalse(any("ciclo" in x["msg"] for x in msgs(t)))
        self.assertTrue(any("ciclo" in x["msg"] for x in msgs(t, aciclico=True)))

    def test_iii_efeito_sem_linha_de_falha(self):
        sem = TAB.replace("`DISPATCH_PUBLISH_FAILED`", "`OUTRO_EVT`")
        a = msgs(sem, efeitos={"despacha": "DISPATCH_PUBLISH_FAILED"})
        self.assertTrue(any(x["verif"] == "iii" for x in a))
        self.assertFalse(any(x["verif"] == "iii" for x in msgs(TAB, efeitos={"despacha": "DISPATCH_PUBLISH_FAILED"})))

    def test_iv_linha_nunca_citada(self):
        a = msgs(TAB + CEN)
        self.assertTrue(any(x["verif"] == "iv" and "F04" in x["msg"] for x in a))
        self.assertFalse(any(x["verif"] == "iv" and "F02" in x["msg"] for x in a))

    def test_sem_tabela(self):
        r = fc.verificar("# nada\n")
        self.assertEqual(r["tabela_linhas"], 0)
        self.assertEqual(r["achados"][0]["verif"], "tabela")

    def test_cli_strict_e_informativo(self):
        d = Path(tempfile.mkdtemp())
        p = d / "plan.md"
        p.write_text(TAB + CEN.replace("F02", "F99"), encoding="utf-8")
        r0 = subprocess.run([sys.executable, str(SCRIPT), str(p)], capture_output=True, text=True, encoding="utf-8")
        r1 = subprocess.run([sys.executable, str(SCRIPT), str(p), "--strict"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r0.returncode, 0)
        self.assertEqual(r1.returncode, 1)

    def test_plan_real_da_spec_008_roda(self):
        p = Path(__file__).resolve().parent.parent / "specs/features/SPEC-008/plan.md"
        if p.exists():
            r = fc.verificar(p.read_text(encoding="utf-8"))
            self.assertGreater(r["tabela_linhas"], 30)
            self.assertEqual([x for x in r["achados"] if x["verif"] in ("i", "ii")], [])


if __name__ == "__main__":
    unittest.main()
