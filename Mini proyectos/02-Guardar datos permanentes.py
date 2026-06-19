
import json

usuario = {}

while True:
  
  print("!Bienvenido al sistema de registro de usuarios¡")

  print("1. Ingresar datos del usuario")
  print("2. Guardar dato del usuario")
  print("3. Mirar datos del usuario")
  print("4. Salir")
  
  opcion = (input("Selecciona una opcion: "))

  if opcion == "1":

     nombre_usuario = input("Ingresa el nombre del usuario: ")
     apellido_usuario = input("Ingresa el apellido del usuario: ")
     edad_usuario = int(input("Ingresa la edad del usuario: "))
     correo_usuario = input("Ingresa el correo  del usuario: ")

     usuario[nombre_usuario.lower()] = {
        "nombre" : nombre_usuario,
        "apellido" : apellido_usuario,
        "edad" : edad_usuario,
        "correo" : correo_usuario
     }

     print("Los datos del usuario se han ingresado correctamente")

  elif opcion == "2":
     #Guarda información en el archivo 
     with open( "datos_usuario.json", "w") as archivo:
        json.dump(usuario, archivo, indent=4)

        print("Los datos del usuario se han guardado correctamente")

  elif opcion == "3":
       # Muestra la informacion antes guardada en el archivo y detecta si la lista esta vacia 
       try:
           with open("datos_usuario.json", "r") as archivo:
             usuario =  json.load(archivo)


             print("\nDatos del usuario:")

           
             for nombre, datos in usuario.items():
                    print(f"Nombre: {datos['nombre']}")
                    print(f"Apellido: {datos['apellido']}")
                    print(f"Edad: {datos['edad']}")
                    print(f"Correo: {datos['correo']}")
                    print( "-" * 20)

       except FileNotFoundError:
          usuario = {}
          print("No se encontraron datos del usuario guardados anterior mente")
    
  elif opcion == "4":
      print("Gracias por usar el sistema de registro de usuarios. !Hasta luego¡")
      break
  else:
      print("Opcion invalida, por favor seleccione una opcion valida")
      


        





