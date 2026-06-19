# Creacion deusuario con diccionario
usuario = {
    "nombre" : "Sharo",
    "edad" : 16,
    "correo" : "sharo@gmail.com"
}

print(usuario)

# Agregado usuarios por medio de lista

usuarios = {
    "lista_usuarios" : []
}
nombre_usuario = input("Ingrese el nombre del usuario: ")

usuarios_diccionario = {"nombre" : nombre_usuario}
usuarios["lista_usuarios"].append(usuarios_diccionario)

print(usuarios)


