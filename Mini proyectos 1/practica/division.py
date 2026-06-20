
class Division:

    def __init__ (self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2


    def resultado(self):

        if self.numero2 == 0:

            return "Error: No se puede dividir por cero"

        resultado = self.numero1 / self.numero2


        return resultado  
    

