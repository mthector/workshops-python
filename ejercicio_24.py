cantidad = int(input("¿Cuantos numero vas a introducir?: "))

mayor_que_0 = 0
menor_que_0 = 0
igual_que_0 = 0

for i in range(cantidad):
    numeros = float(input(f"Introduce el numero {i + 1}: "))

if numeros > 0:
    mayor_que_0 +=1
elif numeros < 0:
    menor_que_0 +=1
else:
    igual_que_0 +=1

print(f"Numeros mayores que 0: {mayor_que_0}")
print(f"Numeros menores que 0: {menor_que_0}")
print(f"Numeros iguales que 0: {igual_que_0}")

