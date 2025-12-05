#!/usr/bin/python3.12

import pdb


alumnos = []


while True:
    print("\nMENÚ DE GESTIÓN DEL ALUMNADO:")
    print("\n1. Ver alumnos")
    print("2. Ver detalle de un alumno")
    print("3. Nuevo alumno")
    print("4. Borrar alumno")
    print("5. Salir")
        
    opcion = input("\nSelecciona una opción: ")
        

    if opcion == '1':
        if not alumnos:
            print("No hay alumnos registrados en el sistema.")
        else:
            print("Alumnos registrados:")
            for alumno in alumnos:
                print(f"DNI: {alumno['dni']}, Nombre: {alumno['nombre']}")

    elif opcion == '2':
        dni = input("Introduce el DNI del alumno: ")
        for alumno in alumnos:
            if alumno['dni'] == dni:
                print(f"DNI: {alumno['dni']}, Nombre: {alumno['nombre']}, Asignaturas: {', '.join(alumno['asignaturas'])}") # .join toma todos los elementos y los une en una cadena separandolos por comas
            else:
                print("El alumno no existe!!")

    elif opcion == '3':
        nombre = input("Introduce el nombre del alumno: ")
        dni = input("Introduce el DNI del alumno: ")
        if any(alumno['dni'] == dni for alumno in alumnos): # any sirve para para verificar si al menos uno de los elementos en un iterable es verdadero, en este caso para comprobar que el DNI exite en la lista de alumnos
            print("El DNI ya está registrado. Introduzca un DNI único.")
        else:
            asignaturas = input("Introduce las asignaturas (separadas por comas): ").split(',')#.split sirve para dividir una cadena de texto en una lista de subcadenas, en este caso las asignaturas separadas por comas
            alumnos.append({'nombre': nombre, 'dni': dni, 'asignaturas': asignaturas})
            print("Alumno añadido correctamente!")

    elif opcion == '4':
        dni = input("Introduce el DNI del alumno a borrar: ")
        for alumno in alumnos:
            if alumno['dni'] == dni:
                alumnos.remove(alumno)
                print("El alumno ha sido borrado con exito!! ")
            else:
                print("Este alumno no existe!. No se ha podido borrar!")
    
    elif opcion == '5':
        print("Gracias por utilizar el sistema de gestión del alumnado.")
        break

    else:
        print("Opcion no válida!!")

