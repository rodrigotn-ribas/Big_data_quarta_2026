import re

texto = "O número de telefone de Raphel é (123) 456-7890."


def procurar_numero(texto):
    padrao = r'\(\d{3}\) \d{3}-\d{4}'
    resultado = re.search(padrao, texto)
    print(resultado)

    if resultado:
        numero_telefone = resultado.group()
        print("Número de telefone encontrado:", numero_telefone)
    else:
        print("Número de telefone não encontrado")

procurar_numero(texto)