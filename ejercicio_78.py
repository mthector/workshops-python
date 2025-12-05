def convertir_a_segundos(horas, minutos, segundos):
    """Convierte horas, minutos y segundos a segundos."""
    return horas * 3600 + minutos * 60 + segundos

def convertir_a_hms(segundos):
    """Convierte segundos a horas, minutos y segundos."""
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

while True:
    print("\nMenú:")
    print("1. Convertir a segundos")
    print("2. Convertir a horas, minutos y segundos")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")

    if opcion == '1':
        horas = int(input("Introduce las horas: "))
        minutos = int(input("Introduce los minutos: "))
        segundos = int(input("Introduce los segundos: "))
        
        total_segundos = convertir_a_segundos(horas, minutos, segundos)
        print(f"Total en segundos: {total_segundos} segundos.")
    
    elif opcion == '2':
        segundos = int(input("Introduce los segundos: "))
        
        horas, minutos, segundos_restantes = convertir_a_hms(segundos)
        print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
    
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida. Por favor, elige una opción válida.")

