lista = []

while True:
    numero = int(input("Ingresa numeros (Ingresa un numero negativo para parar): "))
    if numero < 0:
        break

    lista.append(numero)

print(f"La lista de numeros es {lista}")