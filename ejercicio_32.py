ahorros = 0
ahorros_mes = []

for mes in range (1,13):
    cantidad_a_depositar = float(input("Introduce la cantidad ahorrada de este mes: "))
    ahorros += cantidad_a_depositar
    ahorros_mes.append(ahorros)

    print(f"Total ahorrados hasta el mes {mes}: {ahorros:.2f}€")

print(f"Total ahorra en el año es de: {ahorros:.2f}€")