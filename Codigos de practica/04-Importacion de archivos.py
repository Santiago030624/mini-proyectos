
# Archivo"usuario.py"

class Usuario:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def mostrar_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")


# Archivo "main.py"

#from usuario import Usuario # from me ayuda a importar una clase específica de un módulo personalizado para utilizarla en otro archivo. En este caso, se importa la clase Usuario del módulo usuario, lo que permite crear instancias de la clase Usuario y acceder a sus métodos y atributos utilizando la sintaxis Usuario().

usuario1 = Usuario("Santiago", 17, "santiago@gmail.com")

usuario1.mostrar_usuario()


#Archivo "admin.py" con importacion de paquete personalizado

#from usuario import Usuario # from me ayuda a importar una clase específica de un módulo personalizado para utilizarla en otro archivo. En este caso, se importa la clase Usuario del módulo usuario, lo que permite crear instancias de la clase Usuario y acceder a sus métodos y atributos utilizando la sintaxis Usuario().

class Admin(Usuario):

    def mostrar_permiso(self):
        print("El permiso fue agregado correctamente")

    def mostrar_negacion(self):
        print("El permiso fue denegado")

admin1 = Admin("Sharo", 16, "sharo@gmail.com")
admin1.mostrar_negacion()
admin1.mostrar_permiso()

