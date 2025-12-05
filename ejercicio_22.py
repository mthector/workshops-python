import random

numero_adivinar = random.randint(1, 100)
intentos_max = 10
intentos_realizados = 0

print("¡Bienvenido al juego de adivinar el número!")
print("He elegido un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")


while intentos_realizados < intentos_max:
    intento = int(input("Introduce tu número: "))
    intentos_realizados += 1


    if intento < numero_adivinar:
        print("El número a adivinar es mayor. Te quedan", intentos_max - intentos_realizados, "intentos.")
    elif intento > numero_adivinar:
        print("El número a adivinar es menor. Te quedan", intentos_max - intentos_realizados, "intentos.")
    elif intento == numero_adivinar:
        print(f"¡Felicidades! Has adivinado el número {numero_adivinar} en {intentos_realizados} intentos.")
        break;
    else:
        print(f"Has agotado tus intentos. El número era {numero_adivinar}.")
