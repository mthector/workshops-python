nombres = []
edades = []

while True:
    print("--- MENU ---")
    print("1. Agregar un alumno")
    print("2. Mostrar mayores de edad")
    print("3. Mostrar menores de edad")
    print("4. Salir")
    print("\n")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        nombres.append(input("Nombre: "))
        edades.append(int(input("Edad: ")))

    elif opcion == 2:
        for i in range(len(nombres)):
            if edades[i] >= 18:
                print(f"{nombres[i]}, es mayor de edad, tiene {edades[i]} años")

    elif opcion == 3:
        for i in range(len(nombres)):
            if edades[i] < 18:
                print(f"{nombres[i]}, es menor de edad, tiene {edades[i]} años")

    elif opcion == 4:
        print("Gracias por utilizar el programa")
        break

    else:
        print("Opcion invalida, por favor elija una opcion valida")
