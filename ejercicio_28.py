print("Introduce un intervalo. ")
print("Introudcirás números y mostrará informacion variada")

limite_inferior = int(input("introduce el limite inferior del Intervalo: "))
limite_superior = int(input("introduce el limite superior del Intervalo: "))

while limite_inferior > limite_superior:
    print("El limite inferior no puedo ser mas grande que el limite superior")
    limite_inferior = int(input("introduce el limite inferior del Intervalo: "))
    limite_superior = int(input("introduce el limite superior del Intervalo: "))

numero = ""
lista_numeros = []
suma = 0
fuera = 0
numeros_iguales = []

while numero != 0:
    numero = int(input("Introduce numeros (0 para salir): "))
    lista_numeros.append(numero)

for i in lista_numeros:
    if limite_inferior < i < limite_superior:
        suma += i
    else:
        fuera += 1
    
    if i == limite_inferior or i == limite_superior:
        numeros_iguales.append(numero)

print(f"La suma de los numeros dentro del intervalo es {suma}")
print(f"Los numero fuera del intevalo son {fuera}")
print(f"Numero iguales a los limites de los intervalos {numeros_iguales}")