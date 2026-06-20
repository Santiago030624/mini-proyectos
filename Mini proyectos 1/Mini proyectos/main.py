from fastapi import FastAPI

from pydantic import BaseModel

from fastapi import status

from fastapi import HTTPException


lista_usuarios = []

class Usuarios(BaseModel):
    nombre: str
    edad: int
    correo: str
    telefono: str

app = FastAPI()


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


# Me sirve para ayar la edad mas alta de un usuario 
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

    return {"usuario" : usuario_mayor.nombre,
            "edad" : usuario_mayor.edad}



# Me sirve para sacar la persona mayor 
@app.get("/usuario/menor_edad")
def usuario_menor_edad():

# Me verifica si la lista esta vacia
    if not lista_usuarios:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No se encontraron usuarios registrados"
        )


    usuario_menor = lista_usuarios[0]

    for usuario in lista_usuarios:

        if usuario.edad < usuario_menor.edad:
            usuario_menor = usuario

    return {"usuario" : usuario_menor.nombre,
            "edad" : usuario_menor.edad}


@app.get("/usuario/etadisticas_edades")
def estadistica_edades():

    if not lista_usuarios:
        raise HTTPException(
            Status_code = status.HTTP_404_NOT_FOUND,
            detail = "No se encontraron usuarios"
        )

# Conteo de usuarios
    contar_usuarios = len(lista_usuarios)

# Suma de edades
    suma_edades = sum(usuario.edad for usuario in lista_usuarios)

# Saca el promedio de las edades
    promedio_edades = suma_edades / contar_usuarios




# Lista almacenadoras de edad mas alta y mas baja
    usuario_mayor_edad = lista_usuarios[0]

    usuario_menor_edad = lista_usuarios[0]
    
    # Recorre la lista "lista_usuarios"
    for usuario in lista_usuarios:

        # Filtrado de edad mas alta 
        if usuario.edad > usuario_mayor_edad.edad:
            usuario_mayor_edad = usuario
        
        # Filtrado de edad mas baja
        if usuario.edad < usuario_menor_edad.edad:
            usuario_menor_edad = usuario


# Variables almacenadoras de la cantidad de personas que son mayores y menores de edad
    usuarios_mayores = 0

    usuarios_menores = 0

    usuarios_18_30 = 0

# Recorre la lista "lista_usuarios" para hacer el filtrado de los mayores y menores de edad
    for usuario in lista_usuarios:

        if usuario.edad >= 18 :
            usuarios_mayores += 1

        if usuario.edad < 18:
            usuarios_menores += 1

        if 18 >= usuario.edad <= 30:
            usuarios_18_30 += 1



# En cuentra el nombre mas largo
    nombre_mas_largo = lista_usuarios[0]

    for usuario in lista_usuarios:

        if len(usuario.nombre) > len(nombre_mas_largo.nombre):
            nombre_mas_largo = usuario

    
# En cuentra el nombre mas corto
    nombre_mas_corto = lista_usuarios[0]

    for usuario in lista_usuarios:

        if len(usuario.nombre) < len(nombre_mas_corto.nombre):
            nombre_mas_corto = usuario

# Meda el promedio de los caracteres de los nombres
    suma_nombres = sum(len(usuario.nombre) for usuario in lista_usuarios)

    promedio_nombres = suma_nombres / contar_usuarios



# Encuentra el correo mas largo
    correo_mas_largo = lista_usuarios[0]

    for usuario in lista_usuarios:

        if len(usuario.correo) > len(correo_mas_largo.correo):
            correo_mas_largo = usuario



# Encuentra el correo mas corto
    correo_mas_corto = lista_usuarios[0]

    for usuario in lista_usuarios:
        if len(usuario.correo) < len(correo_mas_corto.correo):
            correo_mas_corto = usuario


# Meda el promedio de los caracteres de los correos
    sumar_correos = sum(len(usuario.correo) for usuario in lista_usuarios)

    promedio_correos = sumar_correos / contar_usuarios


# Da el porcentaje de los mayores de edad
    porcentaje_mayor = (usuarios_mayores / contar_usuarios) * 100 



# Da el procentaje de los menores de edad
    porcentaje_menores = (usuarios_menores / contar_usuarios) * 100



# Da la diferencia de edad entre el usuario mayor y el menor
    diferencia_edad = usuario_mayor_edad.edad - usuario_menor_edad.edad

    return {
        "cantidad_usuarios" : contar_usuarios,
        "promedio_edades" : promedio_edades,
        "usuario_mayor" : usuario_mayor_edad.nombre,
        "edad_maxima" : usuario_mayor_edad.edad,
        "usuario_menor" : usuario_menor_edad.nombre,
        "edad_minima" : usuario_menor_edad.edad,
        "usuarios_mayores_18" : usuarios_mayores,
        "usuarios_menores_18" : usuarios_menores,
        "usuarios_entre_18_y_30" : usuarios_18_30,
        "total_suma_edades" : suma_edades,
        "nombre_mas_largo" : nombre_mas_largo.nombre,
        "nombre_mas_corto" : nombre_mas_corto.nombre,
        "promedio_caracteres_nombres" : promedio_nombres,
        "correo_mas_largo" : correo_mas_largo.correo,
        "correo_mas_corto" : correo_mas_corto.correo,
        "promedio_caracteres_correos" : promedio_correos,
        "porcentaje_mayor_edad" : f"{porcentaje_mayor}%",
        "porcentaje_menores_edad" : f"{porcentaje_menores}%",
        "diferencia_de_edades" : diferencia_edad
    }

