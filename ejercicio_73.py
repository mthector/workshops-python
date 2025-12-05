
agenda = {}


while True:
    print("\n--- Agenda ---")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    print("----------------")
    
    opcion = input("Seleccione una opción: ")

#OPCION MODIFICICAR
    if opcion == '1':
        nombre = input("Ingrese el nombre: ")
        if nombre in agenda:
            print(f"El teléfono de {nombre} es: {agenda[nombre]}")
            modificar = input("¿Desea modificarlo? (s/n): ")
            if modificar.lower() == 's':
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                agenda[nombre] = nuevo_telefono
                print("Teléfono modificado.")
        else:
            telefono = input("Este nombre no existe. Ingrese el teléfono: ")
            agenda[nombre] = telefono
            print("Contacto añadido.")

#OPCION BUSCAR
    elif opcion == '2':
        cadena = input("Ingrese la cadena de caracteres: ")
        print("Contactos que comienzan con:", cadena)
        for nombre in agenda:
            if nombre.startswith(cadena):
                print(f"{nombre}: {agenda[nombre]}")

#OPCION BORRAR
    elif opcion == '3':
        nombre = input("Ingrese el nombre a borrar: ")
        if nombre in agenda:
            confirmar = input(f"¿Está seguro de que desea borrar a {nombre}? (s/n): ")
            if confirmar.lower() == 's':
                del agenda[nombre]
                print("Contacto borrado.")
        else:
            print("El contacto no existe.")

#OPCION LISTAR
    elif opcion == '4':
        if not agenda:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")

#OPCION SALIR
    elif opcion == '5':
        print("Saliendo de la agenda.")
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")
