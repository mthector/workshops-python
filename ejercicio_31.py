numero_a_calcular = int(input("Introduce un número: "))


if numero_a_calcular <= 1:
    resultado = f"{numero_a_calcular} no es un número primo."
else:
    resultado = f"{numero_a_calcular} es un número primo."
    for i in range(2, int(numero_a_calcular**0.5) + 1):
        if numero_a_calcular % i == 0:
            resultado = f"{numero_a_calcular} no es un número primo."
            break

print(resultado)
