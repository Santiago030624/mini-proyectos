
usuarios = {}

while True:
    print("!Bienvenido al sistema de usuarios¡")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Buscar usuario por nombre")
    print("4. salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del usuario: ")
        edad = int(input("Ingresa la edad del usuario: "))
        correo = input("Ingresa el correo del usuario: ")

        usuarios[nombre.lower()] = {
            "nombre" : nombre,
            "edad" : edad,
            "correo" : correo
        }
     
        print("\nUsuario agregado con éxito")
    elif opcion == "2":
        if usuarios:
            print("\nLista de usuarios")
            for nombre, datos in usuarios.items():
                print(f"Nombre: {nombre}, Edad: {datos['edad']}, correo: {datos['correo']}")
        
        else:
            print("\nNo hay usuarios registrados")

    elif opcion == "3":
        nombre_buscar = input("Ingresa el nombre del usuario a buscar: ").lower()

        if nombre_buscar in usuarios:
            datos_usuario = usuarios[nombre_buscar]
            print(f"Nombre: {nombre_buscar}, Edad: {datos_usuario['edad']}, Correo: {datos_usuario['correo']}")
        
        else:
            print("\nUsuario no encontrado")

    elif opcion == "4":
        print("\nSaliendo del sistema de usuarios. !Hasta luego¡")
        break

    else:
        print("\nOpción no valida. Por favor, seleccione un numero del 1 al 4.")


