grados = input("Introduce la temperatura en grados Fahrenheit: ")

valor_fahrenheit = float(grados)
valor_celsius = (valor_fahrenheit - 32) * 5 / 9

print(f"{valor_fahrenheit} grados Fahrenheit son {valor_celsius:.2f} grados Celsius.")