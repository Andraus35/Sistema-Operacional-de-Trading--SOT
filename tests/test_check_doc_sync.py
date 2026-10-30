"""Testes do check_doc_sync.py — python -m unittest tests/test_check_doc_sync.py

Mesmo molde de tests/test_backlog_triggers.py: fixtures sintéticas em diretório
temporário, script chamado via subprocess com --root, saída lida via --json.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_doc_sync.py"

ROADMAP_BASE = (
    "| Decisões abertas ativas | J-001 (reduzido), G-001, K-001 · **SPEC-045-RUNTIME-001** (nota) |\n"
    "| Decisões FECHADAS | B-001 (Conviction≠Synthesis) · **L-001 — FECHADA (SPEC-019 homologada, "
    "2026-09-22): governança spec-time resolvida; runtime ≠ resíduo de L-001 → SPEC-018/K-001)** |\n"
)

RMR_HEAD = "| ID | Título | Tipo | Afeta | Gatilho | Ação | Estado | Origem |\n|---|---|---|---|---|---|---|---|\n"


class DocSync(unittest.TestCase):
    def run_check(self, files, roadmap=ROADMAP_BASE, *args):
        d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        (d / "ROADMAP.md").write_text(roadmap, encoding="utf-8")
        for name, body in files.items():
            p = d / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, encoding="utf-8")
        r = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(d), "--json", *args],
            capture_output=True, text=True, encoding="utf-8",
        )
        out = json.loads(r.stdout) if r.stdout.strip().startswith("{") else {"raw": r.stdout, "err": r.stderr}
        return r.returncode, out

    def msgs(self, rep):
        return [a["mensagem"] for a in rep["achados"]]

    # --- K-001 não deve "contaminar" o fechamento de L-001 (bug corrigido: extract_id_segments) ---
    def test_id_mencionado_na_prosa_de_outra_decisao_nao_conta_como_fechado(self):
        code, rep = self.run_check({})
        self.assertNotIn("K-001", rep["decisoes_fechadas"])
        self.assertIn("L-001", rep["decisoes_fechadas"])
        self.assertIn("K-001", rep["decisoes_abertas"])

    # --- D1/D2: só dispara em documentos de registro (CATALOGO-OFICIAL/CIC-*), não em prosa livre ---
    def test_d2_dispara_em_catalogo_oficial(self):
        catalogo = (
            "## 5. Decisões\n"
            "### Open decisions\n"
            "| **L-001** | texto qualquer |\n"
            "### 6. Fechadas\n"
        )
        code, rep = self.run_check({"governance/CATALOGO-OFICIAL.md": catalogo})
        self.assertEqual(code, 1)
        self.assertTrue(any("FECHADA 'L-001'" in m for m in self.msgs(rep)))

    def test_d2_id_riscado_nao_dispara(self):
        # Convenção já usada no repo (CATALOGO-OFICIAL.md §6): ~~ID~~ marca item superado inline.
        catalogo = "## 5. Decisões\n- **Abertas remanescentes:** J-001, ~~L-001~~ -> FECHADA, C-001.\n"
        code, rep = self.run_check({"governance/CATALOGO-OFICIAL.md": catalogo})
        self.assertEqual(code, 0)
        self.assertEqual(self.msgs(rep), [])

    def test_d2_nao_dispara_em_prosa_livre_fora_do_registro(self):
        agents = "## 7. Decisões abertas\nAtivas: J-001, K-001.\nFechadas: B-001, L-001 (ver ROADMAP).\n"
        code, rep = self.run_check({"AGENTS.md": agents})
        self.assertEqual(code, 0)
        self.assertEqual(self.msgs(rep), [])

    def test_d1_declaracao_inline_de_decisao_aberta_como_fechada(self):
        doc = "Nota: **K-001 — FECHADA** por engano nesta ata.\n"
        code, rep = self.run_check({"governance/QUALQUER-ATA-EDITAVEL.md": doc})
        self.assertEqual(code, 1)
        self.assertTrue(any("ABERTA 'K-001' declarada fechada" in m for m in self.msgs(rep)))

    def test_d1_id_aberto_nao_casa_dentro_de_id_maior(self):
        """DHR-DOCSYNC-003: 'K-001' não casa dentro de 'SPEC-020-K-001'; o ID inteiro continua casando."""
        doc = "Nota: **SPEC-020-K-001 — FECHADA** (outra decisão).\n"
        code, rep = self.run_check({"governance/QUALQUER-ATA-EDITAVEL.md": doc})
        self.assertFalse(any("ABERTA 'K-001'" in m for m in self.msgs(rep)))
        doc2 = "Antes SPEC-020-K-001 ok; depois **K-001 — FECHADA** de verdade.\n"
        code, rep = self.run_check({"governance/QUALQUER-ATA-EDITAVEL.md": doc2})
        self.assertEqual(code, 1)
        self.assertTrue(any("ABERTA 'K-001' declarada fechada" in m for m in self.msgs(rep)))

    # --- D3: RULE citada em [Fonte:] do RULES.md sem seção própria ---
    def test_d3_rule_sem_secao_propria(self):
        rules = "## Regras de Governança do Harness (RULE-HG)\nRULE-HG-01: texto.\n\n" \
                "RULE-HG-02: outra regra [Fonte: RULE-ZZ-01; ROADMAP]\n"
        code, rep = self.run_check({"governance/RULES.md": rules})
        self.assertEqual(code, 1)
        self.assertTrue(any("RULE-ZZ" in m for m in self.msgs(rep)))
        self.assertIn("HG", rep["rule_familias_registradas"])

    def test_d3_nao_dispara_para_familia_registrada(self):
        rules = "## Regras de Governança do Harness (RULE-HG)\nRULE-HG-01: texto [Fonte: RULE-HG-01]\n"
        code, rep = self.run_check({"governance/RULES.md": rules})
        self.assertEqual(code, 0)

    # --- D4: Estado do RMR-001 fora do enum que o próprio §2 declara ---
    def test_d4_estado_fora_do_enum(self):
        rmr = ("## 2. Ciclo de vida\nProposto → Em espera → ATIVADO → Absorvido (ou Descartado).\n\n"
               "## 3. Gatilhos\n" + RMR_HEAD +
               "| **BL-001** | X | Ideia | Y | g | a | Diferido para SPEC-018 | src |\n")
        code, rep = self.run_check({"backlog/RMR-001_Painel_Backlog.md": rmr})
        self.assertEqual(code, 0)  # D4 é WARN, não falha sem --strict
        self.assertTrue(any("fora do enum" in m for m in self.msgs(rep)))
        code2, _ = self.run_check({"backlog/RMR-001_Painel_Backlog.md": rmr}, ROADMAP_BASE, "--strict")
        self.assertEqual(code2, 1)

    def test_d4_estado_no_enum_nao_dispara(self):
        rmr = ("## 2. Ciclo de vida\nProposto → Em espera → ATIVADO → Absorvido (ou Descartado).\n\n"
               "## 3. Gatilhos\n" + RMR_HEAD +
               "| **BL-001** | X | Ideia | Y | g | a | Em espera | src |\n")
        code, rep = self.run_check({"backlog/RMR-001_Painel_Backlog.md": rmr})
        self.assertEqual(code, 0)
        self.assertEqual(self.msgs(rep), [])

    # --- D5: intake dessincronizado do painel vivo ---
    def test_d5_intake_dessincronizado(self):
        rmr = RMR_HEAD + "| **BL-002** | X | Ideia | Y | g | a | Em espera | src |\n"
        intake = "# BL-002\n\n| **Estado** | `Proposto` |\n"
        code, rep = self.run_check({
            "backlog/RMR-001_Painel_Backlog.md": rmr,
            "backlog/BL-002-exemplo-backlog.md": intake,
        })
        self.assertTrue(any("BL-002" in m and "dessincronizado" not in m and "declara Estado" in m for m in self.msgs(rep)))

    def test_d5_intake_sincronizado_nao_dispara(self):
        rmr = RMR_HEAD + "| **BL-002** | X | Ideia | Y | g | a | Em espera | src |\n"
        intake = "# BL-002\n\n| **Estado** | `Em espera` |\n"
        code, rep = self.run_check({
            "backlog/RMR-001_Painel_Backlog.md": rmr,
            "backlog/BL-002-exemplo-backlog.md": intake,
        })
        self.assertEqual(self.msgs(rep), [])

    # --- D6: coerência das citações ao WORKFLOW.md ---
    WF = (
        "| **Versão vigente** | **1.1** |\n"
        "| **WF-02** | passo |\n"
        "| **WF-D01** | Killzone | ... | **ABERTA** |\n"
        "| **WF-D09** | antigo | [REVOGADO em v1.1] |\n"
    )

    def test_d6_id_inexistente_e_erro(self):
        code, rep = self.run_check({"WORKFLOW.md": self.WF, "specs/features/SPEC-9/plan.md": "ver WF-02 e WF-07\n"})
        self.assertEqual(code, 1)
        self.assertTrue(any("WF-07" in m and "inexistente" in m for m in self.msgs(rep)))
        self.assertFalse(any("WF-02" in m for m in self.msgs(rep)))

    def test_d6_decisao_aberta_declarada_fechada_e_erro(self):
        code, rep = self.run_check({"WORKFLOW.md": self.WF, "specs/features/SPEC-9/plan.md": "WF-D01 — FECHADA\n"})
        self.assertEqual(code, 1)
        self.assertTrue(any("WF-D01" in m and "CONS-01" in m for m in self.msgs(rep)))

    def test_d6_revogado_e_versao_divergente_sao_warn(self):
        code, rep = self.run_check({"WORKFLOW.md": self.WF, "specs/features/SPEC-9/plan.md": "WF-D09; conforme WORKFLOW.md v1.0\n"})
        self.assertEqual(code, 0)
        ms = self.msgs(rep)
        self.assertTrue(any("REVOGADO" in m for m in ms))
        self.assertTrue(any("vigente é 1.1" in m for m in ms))

    def test_d6_sem_workflow_md_nao_dispara(self):
        code, rep = self.run_check({"specs/features/SPEC-9/plan.md": "WF-77\n"})
        self.assertFalse(any("WF-77" in m for m in self.msgs(rep)))


if __name__ == "__main__":
    unittest.main()
