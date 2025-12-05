cadena = input("Introduce una cadena: ")

contar_cadena = {}

for caracter in cadena:
    if caracter in contar_cadena:
        contar_cadena[caracter] += 1
    else:
        contar_cadena[caracter] = 1

print(contar_cadena)
