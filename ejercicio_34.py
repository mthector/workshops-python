coche1 = int(input("Introduce el kilometro del coche 1: "))
coche2 = int(input("Introduce el kilometro del coche 2: "))

distancia_entre_coches = coche2 - coche1

km_encuentro = coche1 + (distancia_entre_coches / 2)

print(f"Los coches se encontrarán en el kilómetro: {km_encuentro}")