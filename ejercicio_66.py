lista = []

while True:
    print("\n--- Menú ---")
    print("1. Añadir número a la lista")
    print("2. Añadir número en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    print("\n")

    opcion = int(input("Seleccione una opción (1-9): "))

    if opcion == 1:
        numero = int(input("Ingrese un número para añadir a la lista: "))
        lista.append(numero)
        print(f"Número {numero} añadido a la lista.")

    elif opcion == 2:
        posicion = int(input("Ingrese la posición donde quiere añadir el número: "))
        numero = int(input("Ingrese el número a añadir: "))
        if posicion <= len(lista) + 1:
            lista.insert(posicion - 1, numero)
            print(f"Número {numero} añadido en la posición {posicion}.")
        else:
            print("Posición no válida.")

    elif opcion == 3:
        print(f"La lista tiene {len(lista)} elementos.")

    elif opcion == 4:
        if lista:
            ultimo_numero = lista.pop()
            print(f"Número eliminado: {ultimo_numero}")
        else:
            print("La lista está vacía.")

    elif opcion == 5:
        if lista:
            posicion = int(input("Ingrese la posición del número a eliminar: "))
            if posicion <= len(lista):
                eliminado = lista.pop(posicion - 1)
                print(f"Número eliminado: {eliminado}")
            else:
                print("Posición no válida.")
    
    elif opcion == 6:
        numero = int(input("Ingrese un número para contar en la lista: "))
        print(f"El número {numero} aparece {lista.count} veces en la lista.")
    
    elif opcion == 7:
        numero = int(input("Ingrese un número para buscar en la lista: "))
        if numero in lista:
            print(f"El número {numero} se encuentra en la posición {lista.index(numero) +  1}")
        else:
            print(f"El número {numero} no se encuentra en la lista.")

    elif opcion == 8:
        print(f"Esta es la lista que tienes: {lista}")
    
    elif opcion == 9:
        print("Hasta luego!")
        break

    else:
        print("Opción no válida.")