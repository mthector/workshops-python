alumnos = {}

num_alumnos = int(input("Introduce el número de alumnos: "))


for i in range(num_alumnos):
    nombre = input("Introduce el nombre del alumno: ").strip()
    
    if nombre in alumnos:
        print(f"Error: El alumno {nombre} ya existe.")
        continue
    
    notas = []
    
    while True:
        nota = float(input(f"Introduce una nota para {nombre} (número negativo para terminar): "))
        if nota < 0:
            break
        notas.append(nota)
    
    alumnos[nombre] = notas


print("\nLista de alumnos y sus notas medias:")
for nombre, notas in alumnos.items():
    if notas:
        media = sum(notas) / len(notas)
        print(f"{nombre}: {media:.2f}")
    else:
        print(f"{nombre}: No tiene notas registradas.")
