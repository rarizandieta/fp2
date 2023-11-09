from calculadora import Calculadora

class Asociacion:

    def __init__(self, sueldo, porcertaje):
        self.sueldo = sueldo
        self.porcertaje = porcertaje

    def descuentoAsociacion(self):
        calculadora = Calculadora(self.sueldo, self.porcertaje)
        print("descuento asociacion " + str(calculadora.descuentoAsociacion(self.sueldo, self.porcertaje)))
        return calculadora.descuentoAsociacion(self.sueldo, self.porcertaje)

    