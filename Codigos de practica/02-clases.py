

# Definicion de la clase Usuario
class Usuario:
    def __init__ (self, nombre, apellido, edad, correo ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo

    # Metodo para mostar los datos del Usuario
    def mostrar_Usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")
        print( "-" * 20)


Usuario1 = Usuario("Santiago", "Mendez", 17, "santiago@gmail.co")

Usuario1.mostrar_Usuario() 

# Asignacion de un nuevo Usuario
Usuario2 = Usuario("Maria", "Guzman", 36, "maria@gmail.co")

# Llamada al metodo para mostrar los datos del nuevo Usuario
Usuario2.mostrar_Usuario()

Usuario3 = Usuario("Juan", "Perez", 34, "juan@gmail.co")

Usuario3.mostrar_Usuario()

