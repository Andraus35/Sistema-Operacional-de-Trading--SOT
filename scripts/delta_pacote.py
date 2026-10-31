#!/usr/bin/env python3
"""
delta_pacote.py — pacote de entrega do delta por hash ao Revisor (DHR-DELTA-HASH-001, proposta 1 e 2).

O Revisor não tem Bash: não calcula sha256 nem roda `spec_delta.py`. Este script faz isso pelo Orquestrador, SEMPRE que há rodada
seguinte, e GRAVA o delta em arquivo ao lado do parecer (rastreável e reutilizável), em vez de deixá-lo só no prompt:

  python scripts/delta_pacote.py specs/features/SPEC-nnn/plan.md --base <commit|arquivo> --out governance/propostas/SPEC-nnn/

Saída: (1) arquivo `DELTA-<alvo>-<base7>-<sha8>.txt` em --out; (2) no stdout, as linhas para colar no prompt do Revisor:
  ALVO: / BASE: / SHA256-ALVO: / DELTA:     (o hook R-AC7 já lê ALVO e BASE; as demais são informativas)

Somente leitura do repositório (escreve apenas o arquivo de delta em --out). Reaproveita spec_delta.py (selado) sem alterá-lo.
Detector ≠ Gate (ENF-03): diz O QUE mudou e o hash do que foi entregue; não julga o sentido nem substitui o parecer.
`SHA256-ALVO` = sha256 do texto UTF-8 do arquivo como lido por spec_delta.py (o mesmo valor de `documento_sha256`).
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import spec_delta  # noqa: E402


def sha(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def montar(alvo, base, out_dir):
    """Devolve (caminho_do_arquivo, texto_do_pacote, linhas_do_prompt). Grava o arquivo."""
    alvo_p = Path(alvo)
    novo = alvo_p.read_text(encoding="utf-8", errors="replace")
    base_txt = spec_delta.ler_base(base, str(alvo_p))
    d = spec_delta.delta(base_txt, novo)
    f = spec_delta.fontes(novo)
    sha_alvo, sha_base = sha(novo), sha(base_txt)
    corpo = [
        f"DELTA {alvo} vs {base}",
        f"SHA256-ALVO: {sha_alvo}",
        f"SHA256-BASE: {sha_base}",
        f"blocos: {len(d['alterados'])} alterados · {len(d['adicionados'])} adicionados · {len(d['removidos'])} removidos · "
        f"{d['inalterados']} inalterados (de {d['total_atual']} atuais; {d['total_base']} na base)",
        "alterados: " + (", ".join(d["alterados"]) or "—"),
        "adicionados: " + (", ".join(d["adicionados"]) or "—"),
        "removidos: " + (", ".join(d["removidos"]) or "—"),
        "fontes citadas (sha256 de 12): " + (json.dumps(f, ensure_ascii=False) if f else "—"),
        "",
        "Auxílio de leitura (Classe D): diz o que mudou, não se está certo. Revisão integral obrigatória nos casos do revisor.md §3-bis item 6.",
    ]
    texto = "\n".join(corpo) + "\n"
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    nome = f"DELTA-{alvo_p.parent.name}-{alvo_p.stem}-{str(base)[:7].replace('/', '_')}-{sha_alvo[:8]}.txt"
    arq = out / nome
    arq.write_text(texto, encoding="utf-8")
    prompt = [f"ALVO: {alvo}", f"BASE: {base}", f"SHA256-ALVO: {sha_alvo}", f"DELTA: {arq.as_posix()}"]
    return arq, texto, prompt


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("alvo")
    ap.add_argument("--base", required=True, help="commit/ref ou arquivo da versão já revisada")
    ap.add_argument("--out", required=True, help="pasta onde gravar o arquivo de delta (ao lado do parecer)")
    a = ap.parse_args(argv)
    arq, _, prompt = montar(a.alvo, a.base, a.out)
    print(f"delta gravado: {arq}")
    print("--- cole no prompt do Revisor ---")
    print("\n".join(prompt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
