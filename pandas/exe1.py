def limpar_valor_monetario(valor: str) -> float:
    """Converte texto monetário simples para float."""
    limpo = valor.replace("R$", "").replace(".","").replace(",",".")
    return float(limpo.strip())

banco_de_valores = [
    "R$ 1800,324",
    "R$400,1000",
    "R$    80"
]

for valor in banco_de_valores:
    valor_limpo = limpar_valor_monetario(valor)
    print(f"valor: {valor_limpo} tipo: {type(valor_limpo)}")

