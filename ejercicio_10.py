nota1 = float(input("Ingresa la calificación del primer trimestre: "))
nota2 = float(input("Ingresa la calificación del segundo trimestre: "))
nota3 = float(input("Ingresa la calificación del tercer trimestre: "))

examenfinal = float(input("Ingresa la calificación del examen final: "))

trabajofinal = float(input("Ingresa la calificación del trabajo final: "))

media_trimestral = (nota1 + nota2 + nota3) / 3

notafinal = (media_trimestral * 0.55) + (examenfinal * 0.30) + (trabajofinal * 0.15)
print(f"Tu nota final de la materia de Algoritmos es {notafinal}")