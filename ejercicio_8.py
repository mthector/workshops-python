sueldobase = int(input("¿Cual es tu sueldo base?: "))

venta1 = int(input("¿Cuanto facturaste en la primera venta?: "))
venta2 = int(input("¿Cuanto facturaste en la segunda venta?: "))
venta3 = int(input("¿Cuanto facturaste en la tercera venta?: "))

comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10

total_comisiones = comision1 + comision2 + comision3

total_mes = sueldobase + total_comisiones

print(f"Te has llevado {total_comisiones} euros de comison")
print(f"Has ganado este mes {total_mes}, contando las comisiones")
