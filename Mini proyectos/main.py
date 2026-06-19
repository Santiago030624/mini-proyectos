import fastapi 

from pydantic import BaseModel

from fastapi import status

from fastapi import HTTPException


lista_usuarios = []

class Usuarios(BaseModel):
    nombre: str
    edad: int
    correo: str
    telefono: str

app = fastapi.FastAPI()


# Me permite crear usuarios nuevos, con su nombre, edad, correo y numero de telefono
@app.post("/usuario",
        status_code=status.HTTP_201_CREATED,
        summary = "Crear un nuevo usuario",
        description = "Este endpoin permitira crear un nuebo usuario procesando su nombre, edad, correo y  numero de telefono."
        )

def crear_usuario(usuario: Usuarios):

    lista_usuarios.append(usuario)

    return {
        "mensaje" : "Usuario creado exitosamente", 
        "usuario": usuario
    }


# Me permite ver la lista de los usuarios creados
@app.get("/usuario")

def listar_usuarios():
    if lista_usuarios:

        return lista_usuarios
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No se encontraron usuarios"
    )


# me permite buscar un usuario
@app.get("/usuario/{nombre}")

def obtener_usuario(nombre: str):

    for usuario in lista_usuarios:
        if usuario.nombre.lower() == nombre.lower():
            return usuario
        
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Usuario no encontrado"
    )



# Me permte actualizar la informacion del usuario
@app.put("/usuario/{nombre}")

def actualizar_usuario(nombre: str, datos: Usuarios):

    for i, usuario in enumerate(lista_usuarios):
        
        if usuario.nombre.lower() == nombre.lower():
            lista_usuarios[i] = datos
            
            return {
                "mensaje" : "Usuario actualizado exitosamente",
                "usuario" : datos
            }
        
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Usuario no encontrado"
    )


# Me permite eliminar un usuario por su nombre
@app.delete("/usuario/{nombre}")

def eliminar_usuario(nombre: str):

    for usuario in lista_usuarios:

        if usuario.nombre.lower() == nombre.lower():
            lista_usuarios.remove(usuario)
            return {"mensaje" : "Usuario eliminado exitosamente"}
        
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Usuario no encontrado"
    )



# Me permite saludar a un usuario por su nombre
@app.get("/saludar")
def saludar(nombre: str):

    return {"mensaje" : f"Hola {nombre}, bienvenido a FastAPI!"}


# Me permite verificar si un usuario es mayor o menor de edad por su nombre
@app.get("/usuario/{nombre}/edad")

def mayor_o_menor_de_edad(nombre: str):

    for usuario in lista_usuarios:

        if usuario.nombre.lower() == nombre.lower():

            if usuario.edad >= 18:

                return {"nombre": usuario.nombre,
                        "estado": "Mayor de edad"}
            
            else:

                return {
                    "nombre" : usuario.nombre,
                    "estado" : "Es menor de edad"
                }
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Usuario no encontrado"
    )


# Me permite listar los usuarios mayores de edad
@app.get("/usuario/mayores_de_edad")
def listar_mayores_de_edad():

    lista_mayores = []

    for usuarios in lista_usuarios:
    
        if usuarios.edad >= 18:

            lista_mayores.append(usuarios)

    if lista_mayores:
    
        return lista_mayores

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No se encontraron usuarios mayores de edad"
    )


# Me permite listar los usuarios menores de edad
@app.get("/usuario/menor_de_edad")
def lista_menos_de_edad():

    lista_menores = []

    for usuarios in lista_usuarios:

        if usuarios.edad < 18:

            lista_menores.append(usuarios)

    if lista_menores:

        return lista_menores
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No se encontraron usuarios menores de edad"
    )


# Me permite contar la cantidadde usuarios creados en la lista de usuarios
@app.get("/usuario/contar_usuarios")
def contar_usuarios():

    cantidad_usuarios = len(lista_usuarios)

    return {"cantidad_usuarios" : cantidad_usuarios}


# Me sirve para sacar el promedio de edaes de los usuarios 
@app.get("/usuario/promedio_edades")
def promedio_edades():

    if not lista_usuarios:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No se encontraron usuarios registrados"
        )

    suma_edades = sum(usuario.edad for usuario in lista_usuarios)

    promedio = suma_edades / len(lista_usuarios)

    return {"promedio_edades" : promedio}


@app.get("/usuario/mayor_edad")
def usuario_mayor_edad():

    if not lista_usuarios:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No se encontraron usuarios resgistrados"
        )
    
    usuario_mayor = lista_usuarios[0]

    for usuario in lista_usuarios:

        if usuario.edad > usuario_mayor.edad:
            usuario_mayor = usuario

    return {"usuario" : usuario,
            "edad" : usuario_mayor.edad}

