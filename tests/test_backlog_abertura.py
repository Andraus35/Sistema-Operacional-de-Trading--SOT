"""Regressão da vinculação de backlog por abertura (DHR-BACKLOG-ABERTURA-001) — python -m unittest tests/test_backlog_abertura.py"""
import sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import backlog_triggers as bt  # noqa: E402
import validate_spec_sot as v  # noqa: E402

RMR = (
    "| **BL-901** | Item solo | X | Y | `spec:SPEC-950 em redação` | A | **Em espera** | F |\n"
    "| **BL-902** | Item composto | X | Y | `spec:SPEC-950 em redação` ∧ `decisao:H-001 resolvida` | A | **Em espera** | F |\n"
    "| **BL-903** | Item de faixa | X | Y | `spec:SPEC-949..951 em redação` ∨ `milestone:M` | A | **Em espera** | F |\n"
    "| **BL-904** | Outra Spec | X | Y | `spec:SPEC-951 em redação` | A | **Em espera** | F |\n"
    "| **BL-905** | Encerrado | X | Y | `spec:SPEC-950 em redação` | A | **Absorvido** | F |\n"
    "| **BL-906** | Só homologada | X | Y | `spec:SPEC-950 homologada` | A | **Em espera** | F |\n"
)
ROADMAP = "| SPEC-950 — Teste | FASE X | **ABERTURA HOMOLOGADA** (Andraus); Plan pendente |\n"


def repo(plan=""):
    d = tempfile.TemporaryDirectory()
    root = Path(d.name)
    (root / "backlog").mkdir()
    (root / "backlog" / "RMR-001_Painel_Backlog.md").write_text(RMR, encoding="utf-8")
    (root / "ROADMAP.md").write_text(ROADMAP, encoding="utf-8")
    spec = root / "specs" / "features" / "SPEC-950"
    spec.mkdir(parents=True)
    (spec / "plan.md").write_text(plan, encoding="utf-8")
    return d, root, spec / "plan.md"


class Abertura(unittest.TestCase):
    def test_escopo_por_regra_e_alcance(self):
        d, root, _ = repo()
        with d:
            f = bt.Facts(root)
            scope = bt.abertura_scope(bt.parse_items(bt.read(root / "backlog" / "RMR-001_Painel_Backlog.md")), "950", f)
            got = {x["id"]: x["alcance"] for x in scope}
        self.assertEqual(got, {"BL-901": "TOTAL", "BL-902": "PARCIAL", "BL-903": "TOTAL"})

    def test_abertura_homologada_nao_e_spec_homologada(self):
        d, root, _ = repo()
        with d:
            self.assertNotIn("950", bt.Facts(root).homolog)

    def test_gate_reprova_sem_disposicao_e_passa_com(self):
        d, root, plan = repo()
        base = "RULE-ECC-01 abertura\n"
        with d:
            ok, msg = v.check_backlog_abertura(base, filepath=plan)
            self.assertFalse(ok)
            for bl in ("BL-901", "BL-902", "BL-903"):
                self.assertIn(bl, msg)
            full = base + "".join(f"- {bl} Disposição: PARCIAL — motivo\n" for bl in ("BL-901", "BL-902", "BL-903"))
            self.assertTrue(v.check_backlog_abertura(full, filepath=plan)[0])
            # disposição sem a palavra-chave não vale
            self.assertFalse(v.check_backlog_abertura(base + "BL-901 BL-902 BL-903 tratados\n", filepath=plan)[0])

    def test_pendentes_lista_so_o_que_falta(self):
        d, root, plan = repo("- BL-901 Disposição: FORA — x\n")
        with d:
            pend = bt.abertura_pendentes(root)
        self.assertEqual(pend, [{"spec": "SPEC-950", "faltam": ["BL-902", "BL-903"]}])


if __name__ == "__main__":
    unittest.main()
