fruta = input(f"Inserte el nombre de la fruta: ")
cantidad_frutas = float(input(f"Inserta cantidad de frutas vendidas: "))


diccionario = {
    "Manzana" : 0.56,
    "Pera" : 0.80,
    "Platano" : 1.23
}


if fruta not in diccionario:
    print(f"La fruta no existe")
else:
    precio_fruta = diccionario[fruta] * cantidad_frutas
    print(f"El precio de {fruta} de {cantidad_frutas} unidades es de: {precio_fruta:.2f}€")
    opcion = input("Desea volver hacer una operacion? (s/n): ")
    if opcion == "s":
        fruta = input(f"Inserte el nombre de la fruta: ")
        cantidad_frutas = float(input(f"Inserta cantidad de frutas vendidas: "))
        precio_fruta = diccionario[fruta] * cantidad_frutas 
        print(f"El precio de {fruta} de {cantidad_frutas} unidades es de: {precio_fruta:.2f}€")
    elif opcion == "n":
        exit