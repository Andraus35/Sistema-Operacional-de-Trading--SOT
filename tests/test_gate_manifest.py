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


class TestAgentesDeRevisaoSomenteLeitura(unittest.TestCase):
    """Todo agente de revisão/validação em .claude/agents declara `tools` e nunca inclui Bash/Write/Edit (ENF-03).
    Sem `tools`, o subagente herda todas as ferramentas. (Os dois subagentes de 1ª geração foram aposentados na
    DHR-AUDITOR-EXTERNO-016; um novo revisor com nome parecido cai aqui.)"""
    PROIBIDAS = {"Bash", "Write", "Edit", "MultiEdit", "NotebookEdit", "*"}

    def test_revisores_sem_ferramenta_de_escrita_ou_execucao(self):
        achados = [p for p in (ROOT / ".claude" / "agents").glob("*.md") if re.search(r"revis|review|valid", p.name, re.I)]
        self.assertIn("revisor.md", [p.name for p in achados])
        for p in achados:
            fm = p.read_text(encoding="utf-8").split("---")[1]
            self.assertRegex(fm, r"(?m)^tools:", f"{p.name}: sem `tools` herda todas as ferramentas")
            tools = set(re.findall(r"(?m)^\s+-\s+(\S+)", fm.split("tools:")[1]))
            self.assertFalse(tools & self.PROIBIDAS, p.name)

    def test_subagentes_antigos_aposentados_nao_estao_ativos(self):
        for n in ("sot-spec-reviewer.md", "sot-schema-validator.md"):
            self.assertFalse((ROOT / ".claude" / "agents" / n).exists(), n)
            self.assertTrue((ROOT / "docs" / "_legacy" / "agents" / n).is_file(), n)


if __name__ == "__main__":
    unittest.main()
