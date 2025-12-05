# Precios de los artículos
precios = []
for i in range(5):
    precio = float(input(f"Dime el precio del articulo {i + 1}: "))
    precios.append(precio)

# Cantidades vendidas por sucursal
ventas_sucursales = []
for sucursal in range(4):
    ventas_sucursal = []
    for articulo in range(5):
        cantidad = int(input(f"Dime la cantidad de articulos {articulo + 1} vendidos en la sucursal {sucursal + 1}: "))
        ventas_sucursal.append(cantidad)
    ventas_sucursales.append(ventas_sucursal)

# Cantidades totales de cada artículo
print("Cantidades totales de cada artículo:")
for i in range(5):
    total = 0
    for ventas_sucursal in ventas_sucursales:
        total += ventas_sucursal[i]
    print(f"Articulo {i + 1}: {total}")

# Cantidad de artículos en la sucursal 2
print(f"\nCantidad de artículos en la sucursal 2: {sum(ventas_sucursales[1])}")

# Cantidad del artículo 3 en la sucursal 1
print(f"Cantidad del artículo 3 en la sucursal 1: {ventas_sucursales[0][2]}")

# Recaudación total de cada sucursal
print("\nRecaudación total de cada sucursal:")
for i in range(4):
    recaudacion = 0
    for j in range(5):
        recaudacion += precios[j] * ventas_sucursales[i][j]
    print(f"Sucursal {i + 1}: {recaudacion}")

# Recaudación total de la empresa
recaudacion_total = 0
for ventas_sucursal in ventas_sucursales:
    for i in range(5):
        recaudacion_total += precios[i] * ventas_sucursal[i]
print(f"\nRecaudación total de la empresa: {recaudacion_total}")

# Sucursal de mayor recaudación
mayor_recaudacion = 0
sucursal_mayor_recaudacion = 0
for i in range(4):
    recaudacion = 0
    for j in range(5):
        recaudacion += precios[j] * ventas_sucursales[i][j]
    if recaudacion > mayor_recaudacion:
        mayor_recaudacion = recaudacion
        sucursal_mayor_recaudacion = i + 1
print(f"Sucursal de mayor recaudación: {sucursal_mayor_recaudacion}")