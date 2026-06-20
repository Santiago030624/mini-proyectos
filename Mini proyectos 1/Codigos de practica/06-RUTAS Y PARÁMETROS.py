from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def inicio():

    return {"mensaje" : "Iniciando API"}


# me crea otra ruta get con el decorador @app.get y la ruta /saludo

@app.get("/saludo") # El nombre de (@app.get) es el mismo que se deve agregar a la ruta para que se ejecute la función saludo() cuando se acceda a la ruta /saludo|


# El nombre nombre de la función no es importante, pero debe ser diferente a la función inicio() para evitar conflictos

def saludo(): # me crea una función saludo que se ejecutará cuando se realice una solicitud GET a la ruta /saludo

    return {"mensaje" : "Hola bienvenido a la API"} # me devuelve un mensaje de bienvenida a la API cuando se accede a la ruta /saludo


@app.get("/saludo/{nombre}") # me crea otra ruta get con el decorador @app.get y la ruta /saludo/{nombre} donde {nombre} es un parámetro de ruta

def ingreso_nombre_usuario(nombre: str):
 
    return {"Nombre de usuario" : nombre}


#  Suma de dos números utilizando parámetros de ruta

@app.get("/suma/{numero1}/{numero2}") # me crea otra ruta get con el decorador @app.get y la ruta /suma/{numero1}/{numero2} donde {numero1} y {numero2} son parámetros de ruta

def suma(numero1: int, numero2: int):

    resultado = numero1 + numero2

    return {"resultado" : resultado}

