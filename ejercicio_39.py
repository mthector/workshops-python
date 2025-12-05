def mostrar_menu():
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Salir")

while True:
    mostrar_menu()

    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == "1":
        print("Has seleccionado la Opción 1.")
    elif opcion == "2":
        print("Has seleccionado la Opción 2.")
    elif opcion == "3":
        print("Has seleccionado la Opción 3.")
    elif opcion == "4":
        print("Has seleccionado la Opción 4.")
    elif opcion == "5":
        print("Saliendo del programa. ¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")
    
    print() 
