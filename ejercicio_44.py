cadena = input("Introduce una frase (separada por espacios): ")

palabras = 1

for i in cadena:
    if i == " ":
        palabras = palabras + 1

print(f"La frase que has insertado tienes {len(cadena)} letras: ")

print(f"La frase que has insertado tienes {(palabras)} palabras: ")