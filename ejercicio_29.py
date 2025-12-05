base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    resultado = 1.0
    
    for _ in range(exponente):
        resultado *= base

print(f"{base} elevado a la {exponente} es: {resultado}")
