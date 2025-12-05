meses_años = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

insert_mes = int(input("Inserta un numero de mes(1-12): "))

if 1  <= insert_mes <= 12:
    nombre_meses = meses_años[insert_mes - 1]
    dias_meses = dias_meses[insert_mes - 1]
    print(f"El mes {nombre_meses} tiene {dias_meses} días.")
else:
    print("El mes no existe")