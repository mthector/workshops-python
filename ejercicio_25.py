while True:
    caracter = input("Introduce un carácter (o un espacio para terminar): ")

    if caracter == " ":
        print("Has elegido salir del juego!!")
        break


    if caracter.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")
