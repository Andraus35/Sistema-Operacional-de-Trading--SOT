"""Testes do check_rpsa.py — python -m unittest tests/test_rpsa.py

Mesmo molde dos demais testes: fixtures sintéticas em diretório temporário, script chamado via
subprocess com --root. Cobre R1–R5, --register e --write (idempotência).
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_rpsa.py"


def ata(data="2026-10-05"):
    return f"# ata\n\n| Campo | Valor |\n|---|---|\n| Data | {data} |\n"


def agente(stamp, data):
    return (f"---\nname: x\nsincronizado-até: {stamp}   # RPSA comentario\n"
            f"last_sync_catalog_date: {data}\nrequired_sources: []\n---\ncorpo\n")


class Rpsa(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)
        (self.d / "governance").mkdir()
        (self.d / ".claude" / "agents").mkdir(parents=True)
        self.dhr("DHR-BASE-001", "2026-10-01")
        self.dhr("DHR-OLD-001", "2026-09-20")
        self.ledger(entries=[])
        self.agentes("DHR-BASE-001", "2026-10-01")

    def dhr(self, i, data="2026-10-05"):
        (self.d / "governance" / f"{i}_Ata.md").write_text(ata(data), encoding="utf-8")

    def ledger(self, entries, pre=("DHR-OLD-001",), base="DHR-BASE-001"):
        led = {"baseline_stamp": base, "pre_baseline": list(pre), "entries": entries}
        (self.d / "governance" / "rpsa-ledger.json").write_text(json.dumps(led), encoding="utf-8")

    def agentes(self, stamp, data):
        for n in ("especificador", "revisor"):
            (self.d / ".claude" / "agents" / f"{n}.md").write_text(agente(stamp, data), encoding="utf-8")

    def run_(self, *args):
        r = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.d), "--json", *args],
                           capture_output=True, text=True)
        out = r.stdout
        try:
            return r.returncode, json.loads(out[out.index("{"):])
        except Exception:
            return r.returncode, {"raw": out, "err": r.stderr}

    def regras(self, j):
        return sorted({a["regra"] for a in j.get("achados", [])})

    def test_estado_ok(self):
        rc, j = self.run_()
        self.assertEqual((rc, j["ok"]), (0, True))

    def test_r2_dhr_nova_nao_classificada(self):
        self.dhr("DHR-NEW-001", "2026-10-05")
        rc, j = self.run_()
        self.assertEqual(rc, 1)
        self.assertIn("R2", self.regras(j))

    def test_register_alinha_carimbos_e_fica_ok(self):
        self.dhr("DHR-NEW-001", "2026-10-05")
        rc, _ = self.run_("--register", "DHR-NEW-001", "--scope", "sim", "--sync", "fonte-unica", "--motivo", "toca fluxo")
        self.assertEqual(rc, 0)
        txt = (self.d / ".claude" / "agents" / "revisor.md").read_text(encoding="utf-8")
        self.assertIn("sincronizado-até: DHR-NEW-001", txt)
        self.assertIn("last_sync_catalog_date: 2026-10-05", txt)
        self.assertIn("# RPSA comentario", txt)  # preserva o resto da linha
        led = json.loads((self.d / "governance" / "rpsa-ledger.json").read_text(encoding="utf-8"))
        self.assertEqual(led["entries"][0]["data"], "2026-10-05")  # Data lida da própria ata

    def test_fora_de_escopo_nao_move_carimbo(self):
        self.dhr("DHR-NEW-001", "2026-10-05")
        rc, _ = self.run_("--register", "DHR-NEW-001", "--scope", "nao", "--sync", "fonte-unica", "--motivo", "so operacional")
        self.assertEqual(rc, 0)
        txt = (self.d / ".claude" / "agents" / "especificador.md").read_text(encoding="utf-8")
        self.assertIn("sincronizado-até: DHR-BASE-001", txt)

    def test_r3_sync_pendente_e_gate(self):
        self.dhr("DHR-NEW-001", "2026-10-05")
        rc, j = self.run_("--register", "DHR-NEW-001", "--scope", "sim", "--sync", "pendente", "--motivo", "falta propagar")
        self.assertEqual(rc, 1)
        self.assertIn("R3", self.regras(j))

    def test_r4_carimbo_defasado(self):
        self.dhr("DHR-NEW-001", "2026-10-05")
        self.ledger([{"id": "DHR-NEW-001", "data": "2026-10-05", "em_escopo": True, "sync": "fonte-unica", "motivo": "x"}])
        rc, j = self.run_()
        self.assertEqual(rc, 1)
        self.assertEqual(self.regras(j), ["R4", "R5"])

    def test_r5_data_defasada(self):
        self.agentes("DHR-BASE-001", "2026-09-26")
        rc, j = self.run_()
        self.assertEqual((rc, self.regras(j)), (1, ["R5"]))

    def test_r1_ata_ausente_e_data_divergente(self):
        self.ledger([{"id": "DHR-GHOST-001", "data": "2026-10-05", "em_escopo": False, "sync": "fonte-unica", "motivo": "x"}])
        rc, j = self.run_()
        self.assertEqual(rc, 1)
        self.assertIn("R1", self.regras(j))
        self.dhr("DHR-GHOST-001", "2026-10-04")  # ata existe, mas Data diverge do livro-razão
        rc, j = self.run_()
        self.assertTrue(any("Data do livro-razão" in a["msg"] for a in j["achados"]))

    def test_r1_ordem_cronologica_nao_regride(self):
        self.dhr("DHR-A-001", "2026-10-05")
        self.dhr("DHR-B-001", "2026-10-03")
        self.ledger([{"id": "DHR-A-001", "data": "2026-10-05", "em_escopo": False, "sync": "fonte-unica", "motivo": "x"},
                     {"id": "DHR-B-001", "data": "2026-10-03", "em_escopo": False, "sync": "fonte-unica", "motivo": "x"}])
        rc, j = self.run_()
        self.assertTrue(any("regride" in a["msg"] for a in j["achados"]))

    def test_register_recusa_duplicata_motivo_vazio_e_ata_inexistente(self):
        self.dhr("DHR-NEW-001", "2026-10-05")
        a = ("--register", "DHR-NEW-001", "--scope", "sim", "--sync", "fonte-unica")
        self.assertNotEqual(self.run_(*a, "--motivo", " ")[0], 0)  # sem motivo
        self.assertEqual(self.run_(*a, "--motivo", "ok")[0], 0)
        self.assertNotEqual(self.run_(*a, "--motivo", "de novo")[0], 0)  # append-only
        self.assertNotEqual(self.run_("--register", "DHR-NAOEXISTE-9", "--scope", "sim", "--motivo", "x")[0], 0)
        self.assertNotEqual(self.run_("--register", "DHR-OLD-001", "--scope", "sim", "--motivo", "x")[0], 0)  # pre_baseline

    def test_write_e_idempotente(self):
        self.dhr("DHR-NEW-001", "2026-10-05")
        self.ledger([{"id": "DHR-NEW-001", "data": "2026-10-05", "em_escopo": True, "sync": "fonte-unica", "motivo": "x"}])
        r1 = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.d), "--write"], capture_output=True, text=True)
        r2 = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.d), "--write"], capture_output=True, text=True)
        self.assertIn("especificador.md", r1.stdout)
        self.assertIn("nenhuma mudança", r2.stdout)


if __name__ == "__main__":
    unittest.main()
