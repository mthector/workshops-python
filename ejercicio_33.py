sueldo_por_hora = float(input("Introduce la tarifa por hora: "))

total_horas_trabajadas = 0

for dia in range(1, 7):
    horas_dia = float(input(f"Introduce las horas trabajadas en el día {dia}: "))
    total_horas_trabajadas += horas_dia  # Sumar horas al total


sueldo = total_horas_trabajadas * sueldo_por_hora

print(f"\nTotal de horas trabajadas en la semana: {total_horas_trabajadas:.2f} horas")
print(f"Sueldo total a recibir: ${sueldo:.2f}")
