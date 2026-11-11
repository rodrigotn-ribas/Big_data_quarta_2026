import sys

for linha in sys.stidn:
    regiao, _, valor = linha.strip().split(",")
    print(f"{regiao}\t{float(valor)}")