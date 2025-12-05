
cadena = input("Inserta una frase ")
letra = input("Inserta la letra que vas a remplazar: ")
letra1 = input("Inserta la letera con la que vas a remplezar: ")


if len(letra) != 1 or len(letra1) != 1:
    print("No pueden ser las mismas letras")
else:
    nueva_frase = cadena.replace(letra, letra1, 1)


    print("La frase remplazada es", nueva_frase)