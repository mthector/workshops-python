minutos = int(input("Introduce el numero de minutos: "))

horas = minutos // 60
minutos_res = minutos % 60

print(f"{minutos} minutos son {horas:.2f} horas y {minutos_res} minutos")