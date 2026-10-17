"""Testes do selo de integridade do gate (scripts/gate_manifest.py) e da trava de ferramentas dos subagentes
(DHR-AUDITOR-EXTERNO-015)."""
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import gate_manifest  # noqa: E402


class TestManifesto(unittest.TestCase):
    def test_repositorio_vigente_esta_integro(self):
        self.assertEqual(gate_manifest.conferir(ROOT), [])

    def test_alteracao_ausencia_e_arquivo_fora_sao_detectados(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = Path(tmp)
            (r / "governance").mkdir()
            (r / "scripts").mkdir()
            for a in gate_manifest.ARQUIVOS:
                (r / a).write_text(f"# {a}\n", encoding="utf-8")
            gate_manifest.gravar(r)
            self.assertEqual(gate_manifest.conferir(r), [])
            (r / "scripts/check_refs.py").write_text("# mudou\n", encoding="utf-8")
            self.assertTrue(any("check_refs.py: sha256 difere" in d for d in gate_manifest.conferir(r)))
            (r / "scripts/check_refs.py").unlink()
            self.assertTrue(any("arquivo ausente" in d for d in gate_manifest.conferir(r)))

    def test_fim_de_linha_nao_muda_o_selo(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = Path(tmp)
            (r / "governance").mkdir()
            (r / "scripts").mkdir()
            for a in gate_manifest.ARQUIVOS:
                (r / a).write_bytes(b"a\nb\n")
            gate_manifest.gravar(r)
            (r / "scripts/check_refs.py").write_bytes(b"a\r\nb\r\n")
            self.assertEqual(gate_manifest.conferir(r), [])


class TestSubagentesSomenteLeitura(unittest.TestCase):
    """Subagentes de revisão não podem herdar Bash/Write/Edit (ENF-03): `tools` tem de estar declarado e ser só leitura."""
    PROIBIDAS = {"Bash", "Write", "Edit", "MultiEdit", "NotebookEdit", "*"}

    def _tools(self, nome):
        txt = (ROOT / ".claude" / "agents" / nome).read_text(encoding="utf-8")
        fm = txt.split("---")[1]
        self.assertRegex(fm, r"(?m)^tools:", f"{nome}: sem `tools` herda todas as ferramentas")
        return set(re.findall(r"(?m)^\s+-\s+(\S+)", fm.split("tools:")[1]))

    def test_revisores_sem_ferramenta_de_escrita_ou_execucao(self):
        for nome in ("revisor.md", "sot-spec-reviewer.md", "sot-schema-validator.md"):
            self.assertFalse(self._tools(nome) & self.PROIBIDAS, nome)


if __name__ == "__main__":
    unittest.main()
