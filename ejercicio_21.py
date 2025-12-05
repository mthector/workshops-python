factorial = int(float(input("Ingrese el numero para calcular su factorial:")))

if factorial == 0:
    print(0)
else:
    for a in range(1, factorial):
        factorial*=a
        
print(f"El factorial del numero es {factorial}")