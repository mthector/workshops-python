numero_inferior = int(input("Introduce el primer número (inferior): "))
numero_superior = int(input("Introduce el segundo número (superior): "))

if numero_inferior > numero_superior:
    print("El primer número debe ser menor o igual que el segundo número.")
else:
    print(f"Números pares entre {numero_inferior} y {numero_superior}:")
    

for numero in range(numero_inferior, numero_superior + 1):
    if numero % 2 == 0:
        print(numero)
