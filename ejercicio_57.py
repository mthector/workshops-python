lista1 = []
lista2 = []
lista3 = []


print("Introduce 5 valores para la lista1:")
for i in range(5):
    valor_lista1 = int(input(f"Valor {i + 1}: "))
    lista1.append(valor_lista1)

print("Introduce 5 valores para la lista2:")
for i in range(5):
    valor_lista2 = int(input(f"Valor {i + 1}: "))
    lista2.append(valor_lista2)



lista3 = [lista1[i] + lista2[i] for i in range(5)]



print(f"La lista1 es: {lista1}")
print(f"La lista 2 es: {lista2}")
print(f"La suma de la lista 1 y 2 es: {lista3}")
