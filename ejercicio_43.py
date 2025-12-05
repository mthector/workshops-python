#OPCIÓN 1

cadena = input("Elige una palabra para contar sus letras: ")

letra = input("Elige una letra que quieres contar de la palabra anterior: ")

print(cadena.count(letra))


#OPCIÓN 2
cadena = input("Elige una palabra para contar sus letras: ")

letra = input("Elige una letra que quieres contar de la palabra anterior: ")

contador = 0
iterador = 0
while iterador < len(cadena):
    if cadena[iterador] == letra:
        contador+=1
    iterador+=1

print(f"La cadena {cadena} contiene {contador} veces la letra {letra}")
