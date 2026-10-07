"""Testes do check_sources_verbatim.py — python -m unittest tests/test_check_sources_verbatim.py

Mesmo molde de tests/test_check_doc_sync.py: árvore sintética em diretório temporário, script chamado via subprocess
com --root/--today, saída lida via --json. Cobre M1 (citação existe na captura), M2 (rótulo 'não-capturado') e M8 (data de acesso).
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_sources_verbatim.py"

CAPTURA = (
    "SRC-X-01\nFonte: exemplo\nURL: https://exemplo.org/a\nData de acesso: 2026-10-06\n\n"
    'Trecho literal: "Use deterministic logic as the authoritative signal, with LLM-assisted classification as an optional input '
    'that a deterministic layer re-checks."\n'
)


class SourcesVerbatim(unittest.TestCase):
    def run_check(self, md, sources=None, unit="specs/features/SPEC-099", today="2026-10-10", extra=()):
        d = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        (d / unit / "sources").mkdir(parents=True)
        (d / unit / "research.md").write_text(md, encoding="utf-8")
        for name, body in (sources if sources is not None else {"SRC-X-01.txt": CAPTURA}).items():
            (d / unit / "sources" / name).write_text(body, encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), "--root", str(d), "--today", today, "--json", *extra],
                           capture_output=True, text=True, encoding="utf-8")
        return r.returncode, json.loads(r.stdout)

    def sev(self, rep, s):
        return [a for a in rep["achados"] if a["severidade"] == s]

    def test_citacao_literal_na_captura_passa(self):
        code, rep = self.run_check("Texto «Use deterministic logic as the authoritative signal» fim.\n")
        self.assertEqual(code, 0); self.assertEqual(self.sev(rep, "ERRO"), [])

    def test_citacao_inexistente_e_erro_M1(self):
        code, rep = self.run_check("Texto «LLMs follow instructions in content and more words» fim.\n")
        self.assertEqual(code, 1); self.assertIn("M1", self.sev(rep, "ERRO")[0]["mensagem"])

    def test_elipse_exige_os_dois_lados_literais(self):
        ok = "«Use deterministic logic ... that a deterministic layer re-checks.»\n"
        ruim = "«Use deterministic logic ... this part never existed in the capture.»\n"
        self.assertEqual(self.run_check(ok)[0], 0)
        code, rep = self.run_check(ruim)
        self.assertEqual(code, 1); self.assertEqual(len(self.sev(rep, "ERRO")), 1)

    def test_espacos_e_quebras_de_linha_sao_colapsados(self):
        code, _ = self.run_check("«Use deterministic   logic\nas the authoritative signal»\n")
        self.assertEqual(code, 0)

    def test_citacao_interna_do_repositorio_e_info_nao_erro(self):
        # trecho que existe em OUTRO arquivo do repo (citação interna [FATO]) não é fonte externa: INFO
        d = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, d, True)
        (d / "specs/features/SPEC-099/sources").mkdir(parents=True)
        (d / "specs/features/SPEC-099/sources/SRC-X-01.txt").write_text(CAPTURA, encoding="utf-8")
        (d / "specs/features/SPEC-099/research.md").write_text("Prompt diz «Poucos achados corretos valem mais que muitos duvidosos.»\n", encoding="utf-8")
        (d / "kit.md").write_text("regra 4: Poucos achados corretos valem mais que muitos duvidosos.\n", encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), "--root", str(d), "--today", "2026-10-10", "--json"], capture_output=True, text=True, encoding="utf-8")
        rep = json.loads(r.stdout)
        self.assertEqual(r.returncode, 0); self.assertTrue(any("INTERNA" in a["mensagem"] for a in self.sev(rep, "INFO")))

    def test_trecho_curto_nao_e_conferido(self):
        code, rep = self.run_check("«curto demais»\n")
        self.assertEqual(code, 0); self.assertTrue(any("curto" in a["mensagem"] for a in self.sev(rep, "INFO")))

    def test_aspas_vazias_sao_o_simbolo_nao_uma_citacao(self):
        code, rep = self.run_check("A frase ficou sem « » e virou paráfrase.\n")
        self.assertEqual(code, 0); self.assertEqual(rep["achados"], [])

    def test_M2_rotulo_nao_capturado_colado_a_citacao_e_aviso(self):
        code, rep = self.run_check("[EXTERNO, não-capturado-verbatim] «Use deterministic logic as the authoritative signal»\n")
        self.assertEqual(code, 0); self.assertTrue(any("M2" in a["mensagem"] for a in self.sev(rep, "WARN")))

    def test_M2_rotulo_distante_nao_dispara(self):
        md = "A frase X é [EXTERNO, não-capturado-verbatim] e foi parafraseada, sem aspas, lá atrás neste parágrafo longo de texto. " \
             "Já o trecho capturado é este: «Use deterministic logic as the authoritative signal».\n"
        code, rep = self.run_check(md)
        self.assertEqual(self.sev(rep, "WARN"), [])

    def test_M8_captura_vencida_e_aviso(self):
        code, rep = self.run_check("sem citações\n", today="2027-02-01")   # 2026-10-06 + >90 dias
        self.assertTrue(any("M8" in a["mensagem"] and "dias" in a["mensagem"] for a in self.sev(rep, "WARN")))

    def test_M8_captura_sem_data_e_aviso_mas_nota_com_underscore_e_ignorada(self):
        code, rep = self.run_check("x\n", sources={"SRC-SEM-DATA.txt": "sem data aqui", "_LIMITACAO-WEB.txt": "nota"})
        ws = self.sev(rep, "WARN")
        self.assertEqual(len(ws), 1); self.assertIn("SRC-SEM-DATA", ws[0]["arquivo"])

    def test_M8_spec_anterior_a_regra_vira_info(self):
        code, rep = self.run_check("x\n", sources={"SRC-A.txt": "sem data"}, unit="specs/features/SPEC-002")
        self.assertEqual(self.sev(rep, "WARN"), []); self.assertTrue(any("M8" in a["mensagem"] for a in self.sev(rep, "INFO")))

    def test_strict_faz_warn_reprovar(self):
        code, _ = self.run_check("[EXTERNO, não-capturado-verbatim] «Use deterministic logic as the authoritative signal»\n", extra=("--strict",))
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
