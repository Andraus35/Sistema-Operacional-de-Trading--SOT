"""Testes do check_handoff.py — python -m unittest tests/test_check_handoff.py

Mesmo molde de tests/test_check_doc_sync.py: repositório git sintético em diretório
temporário, script chamado via subprocess com --root, saída lida via --json.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_handoff.py"

SECTIONS = "\n".join(f"## {i}. Seção {i}\nx" for i in range(1, 12))
ROADMAP = ("| Próximo trabalho autorizado | **SPEC-006** — x |\n"
           "| Decisões abertas ativas | J-001 (reduzido), G-001 |\n"
           "| Decisões FECHADAS | B-001 (x) |\n")


def doc(hid="HO-1", prev="null", base="BASE", spec="SPEC-006", extra=""):
    return (f"---\nhandoff_id: {hid}\nprevious: {prev}\ndata: 2026-10-17\nbranch: b\nbase_commit: {base}\n"
            f"spec_autorizada: {spec}\nfase: spec-first\nautor: Orquestrador\n---\n# H\n{SECTIONS}\n{extra}\n")


class Handoff(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)
        self.git("init", "-q")
        self.git("config", "user.email", "t@t")
        self.git("config", "user.name", "t")
        (self.d / "ROADMAP.md").write_text(ROADMAP, encoding="utf-8")
        (self.d / "governance").mkdir()
        (self.d / "governance" / "DHR-OK-001_Ata.md").write_text("x", encoding="utf-8")
        (self.d / "docs" / "handoffs").mkdir(parents=True)

    def git(self, *a):
        return subprocess.run(["git", "-C", str(self.d), *a], capture_output=True, text=True, check=True).stdout.strip()

    def commit(self, msg="c"):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", msg)
        return self.git("rev-parse", "--short", "HEAD")

    def write(self, text):
        (self.d / "HANDOFF.md").write_text(text, encoding="utf-8")

    def run_check(self, *args):
        r = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.d), "--json", *args],
                           capture_output=True, text=True, encoding="utf-8")
        rep = json.loads(r.stdout)
        return r.returncode, rep, {(a["severidade"], a["id"]) for a in rep["achados"]}

    def first(self, **kw):
        base = self.commit("base")
        self.write(doc(base=base, **kw))
        self.commit("handoff 1")
        return base

    def test_handoff_valido_sem_achados(self):
        self.first()
        code, _, ach = self.run_check()
        self.assertEqual(code, 0)
        self.assertEqual(ach, set())

    def test_ausente_e_erro(self):
        self.commit("x")
        code, _, ach = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn(("ERRO", "HO-01"), ach)

    def test_secao_e_campo_ausentes(self):
        self.write("---\nhandoff_id: H\n---\n## 1. a\n")
        self.commit("x")
        _, rep, ach = self.run_check()
        self.assertIn(("ERRO", "HO-01"), ach)

    def test_base_commit_inexistente(self):
        self.commit("x")
        self.write(doc(base="deadbee"))
        self.commit("h")
        _, _, ach = self.run_check()
        self.assertIn(("ERRO", "HO-02"), ach)

    def test_staleness_arquivo_mudou_sem_novo_handoff(self):
        self.first()
        (self.d / "algo.md").write_text("novo", encoding="utf-8")
        self.commit("mudou")
        code, _, ach = self.run_check()
        self.assertIn(("WARN", "HO-03"), ach)
        self.assertEqual(code, 0)
        code, _, _ = self.run_check("--strict")
        self.assertEqual(code, 1)

    def test_commit_rpsa_e_mapa_nao_contam_como_staleness(self):
        self.first()
        (self.d / "governance" / "DHR-OK-001_Ata.md").write_text("y", encoding="utf-8")
        self.commit("RPSA: registra a classificação")
        (self.d / "docs" / "mapa").mkdir(parents=True)
        (self.d / "docs" / "mapa" / "m.md").write_text("m", encoding="utf-8")
        self.commit("mapa")
        _, _, ach = self.run_check()
        self.assertNotIn(("WARN", "HO-03"), ach)

    def test_cadeia_valida_e_arquivo_identico(self):
        self.first()
        old = (self.d / "HANDOFF.md").read_text(encoding="utf-8")
        (self.d / "docs" / "handoffs" / "HO-1.md").write_text(old, encoding="utf-8")
        self.write(doc(hid="HO-2", prev="HO-1", base=self.git("rev-parse", "--short", "HEAD")))
        _, _, ach = self.run_check()  # reescrito, ainda não commitado
        self.assertNotIn(("ERRO", "HO-04"), ach)
        self.commit("handoff 2")
        _, _, ach = self.run_check()
        self.assertNotIn(("ERRO", "HO-04"), ach)

    def test_cadeia_arquivo_adulterado_ou_ausente(self):
        self.first()
        self.write(doc(hid="HO-2", prev="HO-1", base=self.git("rev-parse", "--short", "HEAD")))
        _, _, ach = self.run_check()
        self.assertIn(("ERRO", "HO-04"), ach)  # não arquivado
        (self.d / "docs" / "handoffs" / "HO-1.md").write_text("adulterado", encoding="utf-8")
        _, _, ach = self.run_check()
        self.assertIn(("ERRO", "HO-04"), ach)  # difere

    def test_mais_de_150_linhas(self):
        self.commit("x")
        self.write(doc(base=self.git("rev-parse", "--short", "HEAD"), extra="\n".join("l" for _ in range(160))))
        self.commit("h")
        _, _, ach = self.run_check()
        self.assertIn(("WARN", "HO-05"), ach)

    def test_dhr_inexistente_e_decisao_aberta_como_fechada(self):
        self.commit("x")
        self.write(doc(base=self.git("rev-parse", "--short", "HEAD"),
                       extra="Ver DHR-FAKE-999.\nJ-001 FECHADA por engano.\nG-001 segue ABERTA e não decidida.\nDHR-OK-001 existe."))
        self.commit("h")
        _, rep, ach = self.run_check()
        msgs = [a["mensagem"] for a in rep["achados"]]
        self.assertTrue(any("DHR-FAKE-999" in m for m in msgs))
        self.assertTrue(any("J-001" in m for m in msgs))
        self.assertFalse(any("G-001" in m for m in msgs))
        self.assertFalse(any("DHR-OK-001" in m for m in msgs))

    def test_spec_autorizada_diverge_do_roadmap(self):
        self.first(spec="SPEC-009")
        _, _, ach = self.run_check()
        self.assertIn(("WARN", "HO-07"), ach)

    def test_segredo(self):
        self.commit("x")
        self.write(doc(base=self.git("rev-parse", "--short", "HEAD"), extra="token: abcd1234efgh5678"))
        self.commit("h")
        code, _, ach = self.run_check()
        self.assertIn(("ERRO", "HO-08"), ach)
        self.assertEqual(code, 1)

    def test_homologacao_sem_dhr(self):
        self.commit("x")
        self.write(doc(base=self.git("rev-parse", "--short", "HEAD"),
                       extra="A SPEC-006 foi homologada hoje.\nA SPEC-005 foi homologada (DHR-OK-001).\nPlan não está homologado ainda — pendente."))
        self.commit("h")
        _, rep, ach = self.run_check()
        warns = [a for a in rep["achados"] if a["id"] == "HO-09"]
        self.assertEqual(len(warns), 1)


    def test_ho10_prazo_vencido_aparece_e_futuro_nao(self):
        self.first(extra="- Assinar o registro [PRAZO: 2026-10-24]\n- Outra coisa [PRAZO: 2026-12-31]\n- Data ruim [PRAZO: 2026-13-45]")
        _, rep, _ = self.run_check("--hoje", "2026-10-25")
        msgs = [a["mensagem"] for a in rep["achados"] if a["id"] == "HO-10"]
        self.assertTrue(any("2026-10-24" in m and "Assinar o registro" in m for m in msgs))
        self.assertFalse(any("2026-12-31" in m for m in msgs))
        self.assertTrue(any("data inválida" in m for m in msgs))
        _, rep, _ = self.run_check("--hoje", "2026-10-23")
        self.assertFalse(any("2026-10-24" in a["mensagem"] for a in rep["achados"] if a["id"] == "HO-10"))

    # ---- anexo de tarefa (DHR-PCC-003): HO-11..HO-15 ----------------------------------------------------------------
    def anexo(self, nome="BRIEFING-X.md", status="ATIVO", extra="", faltando=(), base="HEAD"):
        d = self.d / "governance" / "propostas" / "T"
        d.mkdir(parents=True, exist_ok=True)
        fm = {"tipo": "anexo-de-tarefa", "anexo_id": "AT-1", "tarefa": "Plan X", "serve_handoff": "HO-1",
              "base_commit": base, "status": status}
        head = "\n".join(f"{k}: {v}" for k, v in fm.items() if k not in faltando)
        (d / nome).write_text(f"---\n{head}\n---\n# Anexo\n- ponteiro por ID\n{extra}\n", encoding="utf-8")
        return f"governance/propostas/T/{nome}"

    def com_anexo(self, caminho, **kw):
        base = self.commit("base")
        extra = kw.pop("extra", "")
        self.write(doc(base=base, **kw).replace("autor: Orquestrador", f"autor: Orquestrador\nanexo: {caminho}") if caminho else doc(base=base, **kw))
        self.commit("handoff")
        return base

    def test_sem_anexo_nada_muda(self):
        self.first()
        _, _, ach = self.run_check()
        self.assertFalse({a for a in ach if a[1] in ("HO-11", "HO-12", "HO-13", "HO-14", "HO-15")})

    def test_anexo_valido_citado_sem_achados(self):
        c = self.anexo()
        self.com_anexo(c)
        code, _, ach = self.run_check()
        self.assertEqual(code, 0)
        self.assertEqual(ach, set())

    def test_ho11_anexo_inexistente_e_frontmatter_incompleto(self):
        self.com_anexo("governance/propostas/T/NAO-EXISTE.md")
        code, _, ach = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn(("ERRO", "HO-11"), ach)
        c = self.anexo(faltando=("tarefa",))
        self.com_anexo(c)
        _, rep, ach = self.run_check()
        self.assertTrue(any("tarefa" in a["mensagem"] for a in rep["achados"] if a["id"] == "HO-11"))
        c = self.anexo(status="TALVEZ")
        self.com_anexo(c)
        _, rep, _ = self.run_check()
        self.assertTrue(any("fora de ATIVO|CONSUMIDO" in a["mensagem"] for a in rep["achados"] if a["id"] == "HO-11"))

    def test_ho12_orfao_e_mais_de_um_ativo_e_consumido_citado(self):
        self.anexo("A.md")
        self.com_anexo(None)
        _, _, ach = self.run_check()
        self.assertIn(("WARN", "HO-12"), ach)          # ATIVO sem citação
        c1 = self.anexo("B.md")
        self.com_anexo(c1)
        _, rep, _ = self.run_check()
        self.assertTrue(any("máximo 1" in a["mensagem"] for a in rep["achados"] if a["id"] == "HO-12"))
        (self.d / "governance" / "propostas" / "T" / "A.md").unlink()
        c2 = self.anexo("B.md", status="CONSUMIDO")
        self.com_anexo(c2)
        _, rep, _ = self.run_check()
        self.assertTrue(any("CONSUMIDO" in a["mensagem"] for a in rep["achados"] if a["id"] == "HO-12"))

    def test_ho13_anexo_grande(self):
        c = self.anexo(extra="\n".join(f"- linha {i}" for i in range(90)))
        self.com_anexo(c)
        _, _, ach = self.run_check()
        self.assertIn(("WARN", "HO-13"), ach)

    def test_ho14_dhr_inexistente_decisao_aberta_e_segredo(self):
        c = self.anexo(extra="Ver DHR-FANTASMA-009.\nG-001 FECHADA.\ntoken: abcdef123456789")
        self.com_anexo(c)
        code, rep, ach = self.run_check()
        self.assertEqual(code, 1)
        msgs = " ".join(a["mensagem"] for a in rep["achados"] if a["id"] == "HO-14")
        self.assertIn("DHR-FANTASMA-009", msgs)
        self.assertIn("G-001", msgs)
        self.assertIn("segredo", msgs)

    def test_ho15_copia_de_linha_longa_da_fonte(self):
        longa = "A decisao X foi tomada por Andraus em chat com todas as condicoes descritas aqui para teste de copia literal de linha longa"
        (self.d / "governance" / "DHR-OK-001_Ata.md").write_text(longa + "\n", encoding="utf-8")
        c = self.anexo(extra=longa)
        self.com_anexo(c)
        _, rep, ach = self.run_check()
        self.assertIn(("WARN", "HO-15"), ach)
        self.assertTrue(any("DHR-OK-001_Ata.md" in a["mensagem"] for a in rep["achados"] if a["id"] == "HO-15"))


if __name__ == "__main__":
    unittest.main()
