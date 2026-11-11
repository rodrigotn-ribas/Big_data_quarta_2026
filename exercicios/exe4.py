def f(x):
    return x % 2 != 0 and x % 3 != 0

lista = []

for i in range(2,25):
    lista.append(i)

valores = filter(f, lista)

for v in valores:
    print(v)