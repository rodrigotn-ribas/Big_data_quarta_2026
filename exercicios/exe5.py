#Filter
def f(x):
    return x % 2 != 0 and x % 3 != 0

lista = []

for i in range(2,25):
    lista.append(i)

valores = filter(f, lista)

for v in valores:
    print(v)

#Reduce
from functools import reduce

a = ["Geeks", "for", "Geeks"]

r = reduce(lambda result, current: result + " " + current, a)

print(r)

#Mapper
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

print(list(x))
