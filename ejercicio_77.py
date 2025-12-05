def Login(usuario, contrasena, intentos):
    if usuario == "usuario1" and contrasena == "asdasd":
        return True, intentos
    else:
        intentos += 1
        return False, intentos


intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Introduce el nombre de usuario: ")
    contrasena = input("Introduce la contraseña: ")

    login_exitoso, intentos = Login(usuario, contrasena, intentos)

    if login_exitoso:
        print("Login exitoso.")
        break
    else:
        print(f"Login fallido. Intento {intentos} de {max_intentos}.")

if intentos == max_intentos:
    print("Has alcanzado el número máximo de intentos.")
