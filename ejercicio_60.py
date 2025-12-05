tabla = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

numero_columnas = len(tabla[0]) #CALCULAMOS EL NUMERO DE COLUMNAS
sumas_columas = [0] * numero_columnas #INICIALIZAMOS LA VARIABLE DE LA SUMA DESDE LA POSICION 0 POR LAS COLUMNAS DE LAS TABLAS

for filas in tabla:
    for i in range(numero_columnas):
      sumas_columas[i] += filas[i]
print(f"La suma de las columnas son: {sumas_columas}")