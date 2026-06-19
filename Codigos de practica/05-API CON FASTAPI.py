#nombre obligatorio del archibo main.py

# El archibo se deve llamar main.py para que se ejecute con el comando (uvicorn main:app --reload) o sino no se ejecutará 

from fastapi import FastAPI

app = FastAPI() # Me permite crear una instancia de la aplicación FastAPI (crea la aplicación backend)

@app.get("/") # Decorador que indica que esta función se ejecutará cuando se realice una solicitud GET a la ruta raíz ("/") (me crea una ruta get)

def inicio():

    return {"mensaje" : "Hola Mundo"}