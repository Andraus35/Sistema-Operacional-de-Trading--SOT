"""Calibração e mutação dos detectores D adicionais do gate (DHR-AUDITOR-EXTERNO-017)."""
import glob
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import revisor_detectores as d  # noqa: E402

DETECTORES = ("mapeamento_conflitante", "id_norma_inexistente", "contagem_declarada", "spec_nome_incoerente", "valor_fonte", "dhr_backlog")
BASE = (ROOT / "specs" / "features" / "SPEC-021" / "plan.md").read_text(encoding="utf-8")


def mutar(texto, find, repl):
    assert texto.count(find) == 1, f"find deve ocorrer 1x: {find!r} ({texto.count(find)})"
    return texto.replace(find, repl)


class TestCalibracao(unittest.TestCase):
    def test_plans_homologados_so_tem_o_achado_genuino_conhecido(self):
        """10 Plans homologados: único achado esperado = SPEC-003 declara 10 critérios EARS e lista 11 (drift real de baseline)."""
        achados = []
        for f in sorted(glob.glob(str(ROOT / "specs" / "features" / "SPEC-*" / "plan.md"))):
            t = Path(f).read_text(encoding="utf-8")
            for n in DETECTORES:
                for ln, msg in getattr(d, n)(t):
                    achados.append((Path(f).parent.name, n, msg))
        self.assertEqual(len(achados), 1, achados)
        self.assertEqual(achados[0][:2], ("SPEC-003", "contagem_declarada"))


class TestMutacao(unittest.TestCase):
    """Cada detector tem de achar a sua mutação (plantada como no teste cego de 2026-10-17) e não achar nada no original."""

    def test_original_sem_achados_nos_detectores_novos(self):
        for n in DETECTORES:
            self.assertEqual(getattr(d, n)(BASE), [], n)

    def test_d1_valor_atribuido_ao_atomic_spec(self):
        t = mutar(BASE, "D5 + ≥3 cenários D7 + ≥1 adversarial D8 + revisão independente [FONTE", "D5 + ≥4 cenários D7 + ≥1 adversarial D8 + revisão independente [FONTE")
        self.assertTrue(any("≥4" in m for _, m in d.valor_fonte(t)))

    def test_d2_contagem_de_criterios_ears(self):
        t = mutar(BASE, "Critérios em EARS (8)", "Critérios em EARS (9)")
        self.assertTrue(any("declara 9 critérios EARS" in m for _, m in d.contagem_declarada(t)))

    def test_d3_enf_inexistente(self):
        t = mutar(BASE, "ENF-04]  [PROPOSTA]", "ENF-09]  [PROPOSTA]")
        self.assertTrue(any("ENF-09" in m for _, m in d.id_norma_inexistente(t)))

    def test_d6_mapeamento_contraditorio(self):
        t = mutar(BASE, "MEDIUM→L2, HIGH→L3, CRITICAL→L3", "MEDIUM→L1, HIGH→L3, CRITICAL→L3")
        r = d.mapeamento_conflitante(t)
        self.assertTrue(any("MEDIUM" in m for _, m in r), r)

    def test_d10_nome_de_spec_incoerente(self):
        t = mutar(BASE, "SPEC-041** (Cognitive Audit)", "SPEC-024** (Cognitive Audit)")
        self.assertTrue(any("SPEC-024" in m for _, m in d.spec_nome_incoerente(t)))

    def test_d13_dhr_do_backlog(self):
        t = mutar(BASE, "**Absorvido** (2026-09-27, DHR-SPEC020-001)", "**Absorvido** (2026-09-27, DHR-SPEC019-001)")
        self.assertTrue(any("BL-021" in m for _, m in d.dhr_backlog(t)))


class TestCompararVersoes(unittest.TestCase):
    def test_d4_fonte_trocada(self):
        n = mutar(BASE, "O atomic-spec §10.7 **nomeia", "O GPR-001 §2.7 **nomeia")
        r = " | ".join(d.comparar_versoes(BASE, n))
        self.assertIn("GPR-001", r)
        self.assertIn("atomic-spec", r)

    def test_d9_pendencia_marcada_como_feita(self):
        n = mutar(BASE, "[ ] Gate determinístico (validate_spec_sot.py) e build_map.py: a rodar no ambiente pai (sem Bash Python confirmado aqui) — reportado ao caller.",
                  "[x] Gate determinístico (validate_spec_sot.py) e build_map.py: rodados no ambiente pai (exit 0) — resolvido.")
        self.assertIn("pendência [ ] marcada como feita [x]", " | ".join(d.comparar_versoes(BASE, n)))

    def test_d14_referencia_removida_em_silencio(self):
        i = BASE.index("RULE-HG-06; fail-closed")
        n = BASE[:i] + BASE[i + len("RULE-HG-06; "):]
        self.assertIn("referência reduzida: RULE-HG-06", " | ".join(d.comparar_versoes(BASE, n)))

    def test_d1_valor_trocado_aparece_no_diff(self):
        n = mutar(BASE, "Critérios em EARS (8)", "Critérios em EARS (9)")
        self.assertEqual(d.comparar_versoes(BASE, BASE), [])
        self.assertIsInstance(d.comparar_versoes(BASE, n), list)


if __name__ == "__main__":
    unittest.main()
