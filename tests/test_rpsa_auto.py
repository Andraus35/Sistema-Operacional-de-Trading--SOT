"""Testes do rpsa_auto.py (DHR-RPSA-002) — python -m unittest tests/test_rpsa_auto.py

Fixtures sintéticas em diretório temporário; o script é chamado por subprocess com --root (mesmo molde de test_rpsa.py).
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import rpsa_auto  # noqa: E402

SCRIPT = ROOT / "scripts" / "rpsa_auto.py"
MOTIVO = "Altera apenas a operacao do piloto; nao muda checklist, metodo nem regra dos agentes."


def ata(data="2026-10-10", escopo="nao", sync="fonte-unica", motivo=MOTIVO, rows=True):
    base = f"# ata\n\n| Campo | Valor |\n|---|---|\n| Data | {data} |\n"
    if rows:
        base += f"| RPSA-escopo | {escopo} |\n| RPSA-sync | {sync} |\n| RPSA-motivo | {motivo} |\n"
    return base


def agente(stamp, data):
    return (f"---\nname: x\nsincronizado-até: {stamp}   # RPSA comentario\n"
            f"last_sync_catalog_date: {data}\nrequired_sources: []\n---\ncorpo\n")


class Auto(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)
        (self.d / "governance").mkdir()
        (self.d / ".claude" / "agents").mkdir(parents=True)
        self.escreve("DHR-BASE-001", ata("2026-10-01", rows=False))
        led = {"baseline_stamp": "DHR-BASE-001", "pre_baseline": [], "entries": []}
        (self.d / "governance" / "rpsa-ledger.json").write_text(json.dumps(led), encoding="utf-8")
        for n in ("especificador", "revisor"):
            (self.d / ".claude" / "agents" / f"{n}.md").write_text(agente("DHR-BASE-001", "2026-10-01"), encoding="utf-8")

    def escreve(self, dhr, texto):
        (self.d / "governance" / f"{dhr}_Ata.md").write_text(texto, encoding="utf-8")

    def run_(self, changed, apply=False):
        cf = self.d / "changed.txt"
        cf.write_text("\n".join(changed) + "\n", encoding="utf-8")
        args = [sys.executable, str(SCRIPT), "--root", str(self.d), "--changed-file", str(cf)]
        if apply:
            args.append("--apply")
        r = subprocess.run(args, capture_output=True, text=True)
        return r.returncode, json.loads(r.stdout[r.stdout.index("{"):]) if "{" in r.stdout else {"err": r.stderr}

    def ledger(self):
        return json.loads((self.d / "governance" / "rpsa-ledger.json").read_text(encoding="utf-8"))

    def estado(self, j, dhr):
        return next(x for x in j["plano"] if x["dhr"] == dhr)

    # --- parse
    def test_parse_declaracao(self):
        d = rpsa_auto.parse_declaration(ata())
        self.assertEqual((d["escopo"], d["sync"]), ("nao", "fonte-unica"))
        self.assertEqual(rpsa_auto.parse_declaration(ata(rows=False)), {})

    def test_primeira_ocorrencia_vence(self):
        t = ata() + "| RPSA-escopo | sim |\n"
        self.assertEqual(rpsa_auto.parse_declaration(t)["escopo"], "nao")

    # --- registro feliz
    def test_registra_fora_de_escopo(self):
        self.escreve("DHR-NOVA-001", ata())
        rc, j = self.run_(["governance/DHR-NOVA-001_Ata.md", "governance/CATALOGO-OFICIAL.md"], apply=True)
        self.assertEqual((rc, j["registradas"], j["pendentes"]), (0, ["DHR-NOVA-001"], []))
        e = self.ledger()["entries"][0]
        self.assertEqual((e["id"], e["em_escopo"], e["sync"], e["data"]), ("DHR-NOVA-001", False, "fonte-unica", "2026-10-10"))

    def test_em_escopo_fonte_unica_alinha_carimbo(self):
        self.escreve("DHR-NOVA-001", ata(escopo="sim"))
        rc, j = self.run_(["governance/DHR-NOVA-001_Ata.md"], apply=True)
        self.assertEqual(j["registradas"], ["DHR-NOVA-001"])
        txt = (self.d / ".claude" / "agents" / "revisor.md").read_text(encoding="utf-8")
        self.assertIn("sincronizado-até: DHR-NOVA-001", txt)
        self.assertIn("last_sync_catalog_date: 2026-10-10", txt)

    def test_propagado_com_agente_alterado(self):
        self.escreve("DHR-NOVA-001", ata(escopo="sim", sync="propagado"))
        rc, j = self.run_([".claude/agents/revisor.md", "./.claude/agents/especificador.md"], apply=True)
        self.assertEqual(j["registradas"], ["DHR-NOVA-001"])

    def test_so_planeja_sem_apply(self):
        self.escreve("DHR-NOVA-001", ata())
        rc, j = self.run_(["x.md"])
        self.assertEqual(self.estado(j, "DHR-NOVA-001")["estado"], "registrar")
        self.assertEqual(self.ledger()["entries"], [])

    # --- barreiras
    def test_sem_declaracao_nao_registra(self):
        self.escreve("DHR-NOVA-001", ata(rows=False))
        rc, j = self.run_(["x.md"], apply=True)
        self.assertEqual((rc, j["registradas"], j["pendentes"]), (1, [], ["DHR-NOVA-001"]))
        self.assertEqual(self.estado(j, "DHR-NOVA-001")["estado"], "sem-declaracao")
        self.assertEqual(self.ledger()["entries"], [])

    def test_declaracao_invalida(self):
        casos = [dict(escopo="talvez"), dict(sync="outro"), dict(motivo="curto"),
                 dict(escopo="nao", sync="propagado"), dict(escopo="nao", sync="pendente")]
        for i, kw in enumerate(casos):
            with self.subTest(kw=kw):
                for p in (self.d / "governance").glob("DHR-NOVA-*"):
                    p.unlink()
                self.escreve("DHR-NOVA-001", ata(**kw))
                rc, j = self.run_(["x.md"], apply=True)
                self.assertEqual(self.estado(j, "DHR-NOVA-001")["estado"], "declaracao-invalida", kw)
                self.assertEqual(self.ledger()["entries"], [])

    def test_conflito_c1_nao_mas_alterou_metodo_ou_regras(self):
        for arq in ("atomic-spec.md", "governance/RULES.md", "governance/CONSTITUTION.md", "./ATOMIC-SPEC.md"):
            with self.subTest(arq=arq):
                self.escreve("DHR-NOVA-001", ata(escopo="nao"))
                rc, j = self.run_([arq], apply=True)
                self.assertEqual(self.estado(j, "DHR-NOVA-001")["estado"], "conflito", arq)
                self.assertEqual(j["registradas"], [])

    def test_conflito_c3_nao_mas_alterou_agente(self):
        self.escreve("DHR-NOVA-001", ata(escopo="nao"))
        rc, j = self.run_([".claude/agents/revisor.md"], apply=True)
        self.assertEqual(self.estado(j, "DHR-NOVA-001")["estado"], "conflito")

    def test_conflito_c2_propagado_sem_alterar_agente(self):
        self.escreve("DHR-NOVA-001", ata(escopo="sim", sync="propagado"))
        rc, j = self.run_(["governance/CATALOGO-OFICIAL.md"], apply=True)
        self.assertEqual(self.estado(j, "DHR-NOVA-001")["estado"], "conflito")
        self.assertEqual(self.ledger()["entries"], [])

    def test_em_escopo_pendente_registra_e_aciona_gate(self):
        self.escreve("DHR-NOVA-001", ata(escopo="sim", sync="pendente"))
        rc, j = self.run_(["governance/RULES.md"], apply=True)
        self.assertEqual(j["registradas"], ["DHR-NOVA-001"])
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_rpsa.py"), "--root", str(self.d), "--json"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)  # R3: Agent-Sync pendente continua bloqueando a próxima Spec
        self.assertIn("R3", r.stdout)

    # --- ordem, idempotência e append-only
    def test_ordem_cronologica_e_idempotencia(self):
        self.escreve("DHR-B-001", ata("2026-10-12"))
        self.escreve("DHR-A-001", ata("2026-10-11"))
        rc, j = self.run_(["x.md"], apply=True)
        self.assertEqual(j["registradas"], ["DHR-A-001", "DHR-B-001"])
        rc2, j2 = self.run_(["x.md"], apply=True)  # segunda execução: nada pendente, nada muda
        self.assertEqual((rc2, j2["registradas"], j2["plano"]), (0, [], []))
        self.assertEqual([e["id"] for e in self.ledger()["entries"]], ["DHR-A-001", "DHR-B-001"])

    def test_nao_reescreve_entrada_existente(self):
        self.escreve("DHR-NOVA-001", ata(escopo="nao"))
        self.run_(["x.md"], apply=True)
        antes = self.ledger()
        self.escreve("DHR-NOVA-001", ata(escopo="sim", sync="pendente"))  # ata editada depois: ledger não muda
        rc, j = self.run_(["atomic-spec.md"], apply=True)
        self.assertEqual(self.ledger(), antes)
        self.assertEqual(j["plano"], [])

    def test_check_rpsa_fica_ok_depois_de_registrar(self):
        self.escreve("DHR-NOVA-001", ata(escopo="sim"))
        self.run_(["x.md"], apply=True)
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_rpsa.py"), "--root", str(self.d)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_texto_malicioso_na_ata_nao_vira_comando(self):
        evil = "x'; rm -rf / #  \"$(touch /tmp/pwn)\" `id` " + "a" * 30
        self.escreve("DHR-NOVA-001", ata(motivo=evil))
        rc, j = self.run_(["x.md"], apply=True)
        self.assertEqual(j["registradas"], ["DHR-NOVA-001"])  # é só texto no JSON
        self.assertFalse(Path("/tmp/pwn").exists())


if __name__ == "__main__":
    unittest.main()
