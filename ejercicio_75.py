def EscribirCentrado(texto):
    ancho = 80
    longitud_texto = len(texto)
    espacios = (ancho - longitud_texto) // 2
    
    print(' ' * espacios + texto)
    print(' ' * espacios + '=' * longitud_texto)


EscribirCentrado(input("Inserte cadena de texto!: "))
