
class Usuario:
    def __init__ (self, nombre, apellido, edad, correo ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo

    # Metodo para mostar los datos del Usuario
    def mostrar_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")
        print( "-" * 20)


Usuario1 = Usuario("Santiago", "Mendez", 17, "santiago@gmail.co")

Usuario1.mostrar_usuario() 

# Asignacion de un nuevo Usuario
Usuario2 = Usuario("Maria", "Guzman", 36, "maria@gmail.co")

# Llamada al metodo para mostrar los datos del nuevo Usuario
Usuario2.mostrar_usuario()

Usuario3 = Usuario("Juan", "Perez", 34, "juan@gmail.co")

Usuario3.mostrar_usuario()


# Eredan los atributos de usuario a la clase Addmin, pero no ereda los de mostrar_usuario
class Addmin(Usuario):

    def mostarar_permisos(self):

        print("El usuario fue agregado correcta mente")

    def mostrar_negacion(self):

        print("El usuario no pudo ser agregado")



AdminUsuario3 = Addmin("Juan", "Perez", 34, "juan@gmail.co")

AdminUsuario3.mostrar_usuario()
AdminUsuario3.mostarar_permisos()
AdminUsuario3.mostrar_negacion()
