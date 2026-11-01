import json, os, subprocess, sys, tempfile, unittest, shutil
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SCRIPT = ROOT / "scripts" / "pre_entrega.py"

def run(spec, out):
    return subprocess.run([sys.executable, "-B", str(SCRIPT), spec, "--root", str(ROOT), "--out", str(out)], capture_output=True, text=True)

class T(unittest.TestCase):
    def test_baseline_limpa_e_hash(self):
        with tempfile.TemporaryDirectory() as d:
            r = run("specs/features/SPEC-049", Path(d) / "o.json")
            ev = json.loads((Path(d) / "o.json").read_text())
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertEqual(ev["bloqueantes_vermelhos"], [])
            import hashlib
            self.assertEqual(ev["plan_sha256"], hashlib.sha256((ROOT / "specs/features/SPEC-049/plan.md").read_bytes()).hexdigest())
            self.assertGreaterEqual(len(ev["verificacoes"]), 20)
    def test_spec_inexistente_falha(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(run("specs/features/SPEC-999", Path(d) / "o.json").returncode, 2)
    def test_plan_quebrado_fica_vermelho(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d) / "repo"; shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__"))
            p = root / "specs/features/SPEC-049/plan.md"; p.write_text("# vazio\n", encoding="utf-8")
            r = subprocess.run([sys.executable, "-B", str(SCRIPT), "specs/features/SPEC-049", "--root", str(root), "--out", str(Path(d) / "o.json")], capture_output=True, text=True)
            self.assertEqual(r.returncode, 1); self.assertIn("validate_spec_sot", json.loads((Path(d) / "o.json").read_text())["bloqueantes_vermelhos"])
if __name__ == "__main__": unittest.main()
