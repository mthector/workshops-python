suma = 0
contador = 0

print("Introduce números (introduce 0 para terminar):")

while True:
    numero = float(input())
    if numero == 0:
        break
    suma += numero
    contador += 1 

if contador > 0:
    media = suma / contador 
    print(f"Suma: {suma}")
    print(f"Media: {media}")
else:
    print("No se han introducido números.")
