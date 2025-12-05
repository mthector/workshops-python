numero_a_calcular = int(input(f"Inserte un numero al diccionario para calcular el cuadrado: "))

diccionario = {}

for valores in range(1,numero_a_calcular + 1):
    valor_al_cuadrado = valores ** 2
    diccionario[valores] = valor_al_cuadrado

print(f"Los cuadrados de tu diccionarios son : {diccionario}")
