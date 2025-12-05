#OPCION 1
cadena_principal = input("Inserte una palabra de la cadena principal: ")

subcadena = input("Inserte la palabra de la subcadena: ")

if cadena_principal.startswith(subcadena):
    print("La cadena principal empieza con la subcadena")
else:
    print("La cadena principal no empieza por la subcadena")


#OPCION 2
cadena_principal = input("Inserte una palabra de la cadena principal: ")

subcadena = input("Inserte la palabra de la subcadena: ")

if cadena_principal[:len(subcadena)] == subcadena:
    print("La cadena principal empieza con la subcadena")
else:
    print("La cadena principal no empieza por la subcadena")