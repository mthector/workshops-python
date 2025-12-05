def EsMultiplo(a, b):
    return a % b == 0

numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

if EsMultiplo(numero1, numero2):
    print(f"{numero1} es múltiplo de {numero2}.")
elif EsMultiplo(numero2, numero1):
    print(f"{numero2} es múltiplo de {numero1}.")
else:
    print("Ninguno de los números es múltiplo del otro.")
