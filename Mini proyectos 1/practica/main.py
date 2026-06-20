from fastapi import FastAPI

from pydantic import BaseModel

from fastapi import status

from fastapi import HTTPException

app = FastAPI()

guardar_usuario = []

class Usuario(BaseModel):
    nombre: str
    edad: int
    correo : str
    telefono: int

class Mensaje(BaseModel):
    mensaje: str



# Endpoint para recibir un mensaje
@app.post("/mensaje")

def recibir_mensaje(mensaje: Mensaje):

    return {
    "mensaje recibido" : mensaje.mensaje
    }


# Crear un nuevo usuario
@app.post("/usuarios",
        status_code=status.HTTP_201_CREATED,
        summary="Crear un nuevo usuario",
        description="Este endpoint permite crear un nuevo usuario proporcionando su nombre, edad, correo y teléfono."
        )

def crear_usuario(usuario: Usuario):

    guardar_usuario.append(usuario)
    
    return {
        "mensaje": "Usuario creado exitosamente",
            "usuario": usuario
            }


# Listar todos los usuarios
@app.get("/usuarios")
def lista_usuarios():

    if not guardar_usuario:

        return guardar_usuario
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "No se encontraron usuarios"
    )



# Buscar un usuario por su nombre
@app.get("/usuario/{nombre}")
def buscar_usuario(nombre: str):

    for usuario in guardar_usuario:
    
        if usuario.nombre.lower() == nombre.lower():
            return usuario
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Usuario no encontrado"
    )




# Eliminar un usuario por su nombre
@app.delete("/usuario/{nombre}")
def eliminar_usuario(nombre: str):

    for usuario in guardar_usuario:
    
        if usuario.nombre.lower() == nombre.lower():
            
            guardar_usuario.remove(usuario)
            
            return {"mensaje": "El usuario fue eliminado exitosamente"}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Usuario no encontrado"
    )


# Actualizar un usuario por su nombre
@app.put("/usuario/{nombre}")
def actualizar_usuario(nombre: str, datos: Usuario):

    for i, usuario in enumerate(guardar_usuario):
    
        if usuario.nombre.lower() == nombre.lower():
        
            guardar_usuario[i] = datos
        
            return{"mensaje": "Usuario actualizado exitosamente",}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Usuario no encontrado"
    )




@app.get("/saludar")
def saludar(nombre: str):

    return {"mensaje": f"Hola, {nombre}!"}


