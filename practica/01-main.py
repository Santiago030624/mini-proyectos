
from suma import Suma

from resta import Resta 

from multiplicacion import Multiplicacion

from division import Division

from fastapi import FastAPI


app = FastAPI()

@app.get("/suma/{numero1}/{numero2}")

def sumar(numero1 : float, numero2 : float): # Funcion de suma

    operacion = Suma(numero1, numero2)
    resultado = operacion.resultado()

    return {"resultado": resultado}



@app.get("/resta/{numero1}/{numero2}") # Funcion de resta

def restar_numeros(numero1: float, numero2: float):

    operacion = Resta(numero1, numero2)
    resultado = operacion.resultado()

    return {"resultado" : resultado}



@app.get("/multiplicacion/{numero1}/{numero2}")
        
def multiplicar_numero(numero1: float, numero2 : float): # Funcion de multiplicacion

    operacion = Multiplicacion(numero1, numero2)
    resultado = operacion.resultado()

    return {"resultado" : resultado}


@app.get("/division/{numero1}/{numero2}")

def dividir_numero(numero1: float, numero2: float): # Funcion de divicion

    if numero2 == 0:
        return  "Error: No se puede dividir por cero"

    operacion = Division(numero1, numero2)
    resultado = operacion.resultado()

    return {"resultado" : resultado}





