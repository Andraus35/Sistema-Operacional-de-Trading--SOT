"""Teste (PROPOSTA A9; não instalado): os arquivos de agente não podem repetir fatos que o repositório já corrigiu.
Cada regra cita a autoridade que a tornou defasada. Limite: pega só deriva CONHECIDA (lista fechada), não deriva nova.
Uso: python -m unittest governance/propostas/MELHORIAS-PROCESSO/A9/test_agentes_sem_fatos_defasados.py  (ROOT = repositório)."""
import re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AGENTES = [".claude/agents/especificador.md", ".claude/agents/revisor.md"]
# (regex, autoridade, o que está certo)
DEFASADOS = [
    (r"SOT não executa ordem[^\n]*produz (?:o )?(?:Trading Mission Package|TMP)\b", "AGENTS.md §6.9 / EUA-E19a", "o produto é o Signal Package; o TMP é artefato interno"),
    (r"CCM-001[^\n]*pendente de reda[çc][ãa]o", "AGENTS.md §6.12 / DHR-SPEC003-001", "CCM-001 está BASELINED desde 2026-10-02"),
    (r"conforme AGENTS\.md §3\b", "AGENTS.md §4", "profiles de profundidade estão no §4"),
    (r"CC-01\.\.CC-10\b", "atomic-spec §10.5 (CC-11/CC-12)", "o Constitution Check vai até CC-12"),
    (r"trava SPEC-003", "DHR-SPEC003-001", "SPEC-003 já foi homologada; J-001 segue aberta"),
]

class T(unittest.TestCase):
    def test_sem_fatos_defasados(self):
        achados = []
        for a in AGENTES:
            for n, ln in enumerate((ROOT / a).read_text(encoding="utf-8").splitlines(), 1):
                for rx, auth, certo in DEFASADOS:
                    if re.search(rx, ln):
                        achados.append(f"{a}:{n}: fato defasado ({auth}: {certo}) — {ln.strip()[:90]}")
        self.assertEqual(achados, [], "\n".join(achados))

    def test_regras_detectam_o_defeito(self):   # o detector não pode ficar mudo (mutação)
        amostras = ["- SOT não executa ordem — produz TMP.", "CCM-001 **pendente de redação** (SPEC-003)", "(D0–D8 conforme AGENTS.md §3)", "CC-01..CC-10 (atomic-spec", "trava SPEC-003)"]
        for rx_t, am in zip(DEFASADOS, amostras):
            self.assertTrue(re.search(rx_t[0], am), rx_t[0])

if __name__ == "__main__":
    unittest.main()
