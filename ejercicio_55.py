import random

lista = []

for i in range(10):
    lista.append(random.randint(1, 100))

print("Esta es tu lista aleatoria: ")
print(lista)

lista.sort()

print("Esta es tu lista aleatoria, pero ordenada: ")
print(lista)