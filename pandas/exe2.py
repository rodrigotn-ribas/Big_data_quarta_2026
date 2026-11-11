from pathlib import Path

BASE = Path(__file__).resolve().parent
ARQUIVO = BASE / "data" / "raw" /"vendas.csv"

if not ARQUIVO.exists():
    raise FileNotFoundError(ARQUIVO)

print(ARQUIVO)
