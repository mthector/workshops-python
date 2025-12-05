notas = []

for lista_notas in range(5):
    introduce_nota = float(input(f"Ingrese nota {lista_notas + 1} (entre el 0 y el 10): "))
    if 0 <= introduce_nota <= 10:
        notas.append(introduce_nota)
    else:
        print("La nota tiene que estar entre el 0 y el 10")

nota_media = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)


print("\nLa nota media es un: ", nota_media)
print("\nLa nota más alta es un: ", nota_maxima)
print("\nLa nota más baja es un: ", nota_minima)