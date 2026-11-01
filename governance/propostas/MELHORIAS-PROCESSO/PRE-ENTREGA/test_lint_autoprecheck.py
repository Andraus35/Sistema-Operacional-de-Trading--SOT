import json, sys, tempfile, unittest, hashlib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_autoprecheck as L

FRASE = "Esta linha de teste tem bem mais de cem caracteres para servir de trecho literal verificável pelo linter do autoprecheck sem ambiguidade."

def montar(tmp, linhas_extra=None, pe_status="OK", plan="# plan\n"):
    root = Path(tmp); sd = root / "specs/features/SPEC-X"; sd.mkdir(parents=True)
    (sd / "plan.md").write_text(plan, encoding="utf-8")
    (root / "doc.md").write_text("linha1\n" + FRASE + "\n", encoding="utf-8")
    pe = {"plan_sha256": hashlib.sha256((sd / "plan.md").read_bytes()).hexdigest(),
          "verificacoes": [{"id": i, "tipo": "bloqueante" if i in ("validate_spec_sot", "check_repo_research", "build_map_check") else "informativo", "status": pe_status}
                           for i in {p for it in L.CAT["itens"] if it["tipo"] == "D" for p in it["pe"]}]}
    linhas = ["| item | estado | evidência |", "|---|---|---|"]
    for it in L.CAT["itens"]:
        if not L.aplica(it, set()):
            linhas.append(f"| {it['id']} | N/A | motivo: fora do contexto {it['aplica']} |")
        elif it["tipo"] == "D":
            linhas.append(f"| {it['id']} | [x] | PE:{','.join(it['pe'])} |")
        else:
            linhas.append(f"| {it['id']} | [x] | doc.md:2 «{FRASE}» |")
    for k, v in (linhas_extra or {}).items():
        linhas = [v if l.startswith(f"| {k} ") else l for l in linhas]
    (sd / "autoprecheck.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    return root, pe

class T(unittest.TestCase):
    def conferir(self, **kw):
        with tempfile.TemporaryDirectory() as d:
            root, pe = montar(d, **kw); return L.conferir("specs/features/SPEC-X", root, set(), pe)
    def test_completo_passa(self):
        self.assertEqual(self.conferir(), [])
    def test_item_ausente(self):
        with tempfile.TemporaryDirectory() as d:
            root, pe = montar(d); f = root / "specs/features/SPEC-X/autoprecheck.md"
            f.write_text("\n".join(l for l in f.read_text(encoding="utf-8").splitlines() if not l.startswith("| AP-01 ")) + "\n", encoding="utf-8")
            self.assertTrue(any("AP-01" in p and "ausente" in p for p in L.conferir("specs/features/SPEC-X", root, set(), pe)))
    def test_item_desmarcado(self):
        self.assertTrue(any("AP-03" in p for p in self.conferir(linhas_extra={"AP-03": "| AP-03 | [ ] | |"})))
    def test_d_sem_evidencia(self):
        self.assertTrue(any("sem evidência" in p for p in self.conferir(linhas_extra={"AP-03": "| AP-03 | [x] | tudo certo |"})))
    def test_atestado_sem_ancora_e_ancora_falsa(self):
        self.assertTrue(any("AP-01" in p and "sem âncora" in p for p in self.conferir(linhas_extra={"AP-01": "| AP-01 | [x] | li o ROADMAP |"})))
        falsa = "| AP-01 | [x] | doc.md:2 «" + FRASE.replace("teste", "TROCADO") + "» |"
        self.assertTrue(any("AP-01" in p and "não consta" in p for p in self.conferir(linhas_extra={"AP-01": falsa})))
    def test_ancora_curta(self):
        self.assertTrue(any("< 100" in p for p in self.conferir(linhas_extra={"AP-01": "| AP-01 | [x] | doc.md:2 «linha curta» |"})))
    def test_bloqueante_vermelho_e_achado_informativo(self):
        self.assertTrue(any("VERMELHO" in p for p in self.conferir(pe_status="RED")))
        with tempfile.TemporaryDirectory() as d:
            root, pe = montar(d)
            for v in pe["verificacoes"]:
                if v["id"] == "check_dimensionamento": v["status"] = "ACHADOS"
            self.assertTrue(any("sem `justificado:`" in p for p in L.conferir("specs/features/SPEC-X", root, set(), pe)))
    def test_plan_mudou_depois_do_pregate(self):
        with tempfile.TemporaryDirectory() as d:
            root, pe = montar(d); (root / "specs/features/SPEC-X/plan.md").write_text("# plan alterado\n", encoding="utf-8")
            self.assertTrue(any("plan_sha256" in p for p in L.conferir("specs/features/SPEC-X", root, set(), pe)))
    def test_na_indevido(self):
        self.assertTrue(any("N/A" in p for p in self.conferir(linhas_extra={"AP-03": "| AP-03 | N/A | motivo: não faz sentido aqui mesmo |"})))
    def test_ausencia_do_arquivo(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertTrue(L.conferir("specs/features/SPEC-X", Path(d), set(), None))
    def test_template_gera_d_marcado_e_atestado_aberto(self):
        _, pe = montar(tempfile.mkdtemp())
        t = L.template("x", set(), pe)
        self.assertIn("| AP-03 | [x] | PE:check_invariants |", t); self.assertIn("| AP-01 | [ ] |", t)
if __name__ == "__main__": unittest.main()
