"""Delta por hash + evidência amarrada à versão — python -m unittest tests/test_spec_delta.py"""
import json, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import spec_delta as sd  # noqa: E402
import revisor_gate as rg  # noqa: E402

BASE = """# SPEC-X
| Status | v1 |

### BASpec-X-001 — a
QUANDO x
ENTÃO y

### BASpec-X-002 — b
QUANDO p
ENTÃO q

```
RULE-X-001: regra um
   continua aqui

RULE-X-002: regra dois
```
"""


class Delta(unittest.TestCase):
    def test_sem_mudanca_tudo_inalterado(self):
        d = sd.delta(BASE, BASE)
        self.assertEqual((d["alterados"], d["adicionados"], d["removidos"]), ([], [], []))

    def test_espacos_nao_contam(self):
        self.assertEqual(sd.delta(BASE, BASE.replace("QUANDO x", "QUANDO   x"))["alterados"], [])

    def test_so_o_bloco_mudado_aparece(self):
        d = sd.delta(BASE, BASE.replace("ENTÃO y", "ENTÃO y2"))
        self.assertEqual(d["alterados"], ["BASpec-X-001"])

    def test_regra_dentro_de_bloco_cercado_tem_granularidade_propria(self):
        d = sd.delta(BASE, BASE.replace("regra dois", "regra DOIS mudou"))
        self.assertIn("def:RULE-X-002", d["alterados"])
        self.assertNotIn("def:RULE-X-001", d["alterados"])

    def test_adicionado_e_removido(self):
        novo = BASE.replace("### BASpec-X-002 — b", "### BASpec-X-003 — b")
        d = sd.delta(BASE, novo)
        self.assertEqual((d["adicionados"], d["removidos"]), (["BASpec-X-003"], ["BASpec-X-002"]))


class Evidencia(unittest.TestCase):
    def test_evidencia_vale_e_fica_velha(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            doc = root / "doc.md"
            doc.write_text("um\n", encoding="utf-8")
            import hashlib
            ev = {"documento": "doc.md", "documento_sha256": hashlib.sha256("um\n".encode()).hexdigest()}
            f = root / "ev.json"
            f.write_text(json.dumps(ev), encoding="utf-8")
            self.assertEqual(rg.verificar_evidencia(f, root)[0], 0)
            doc.write_text("dois\n", encoding="utf-8")
            cod, msg = rg.verificar_evidencia(f, root)
            self.assertEqual(cod, 1)
            self.assertIn("VELHA", msg)

    def test_evidencia_sem_hash_nao_e_verificavel(self):
        with tempfile.TemporaryDirectory() as t:
            f = Path(t) / "ev.json"
            f.write_text(json.dumps({"documento": "x.md"}), encoding="utf-8")
            self.assertEqual(rg.verificar_evidencia(f, Path(t))[0], 2)


if __name__ == "__main__":
    unittest.main()
