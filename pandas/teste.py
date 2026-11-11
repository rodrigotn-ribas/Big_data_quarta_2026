regiao = ["RJ", "SP", "RJ","MG", "ES", "SP"]
estado = []
for r in regiao:
    r = r.lower()
    estado.append(r)

print(estado)


preco = [150.00, 80.00, 1200.00, 150.00, 220.00, 80.00]
qtd = [2,3,1,4,2,1]
valor = []

valor.append(lambda d: d[preco] * d[qtd])
print(valor)

for i in range(5):
    v = preco[i] * qtd[i]
    valor.append(v)
valor = [new_list in new_itemfor]

print(valor)