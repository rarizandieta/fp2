from persona import Persona
from nomina import Nomina

class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo, horasExtra, pagoEnviado, inscrito, porcentaje):
        super().__init__(nombre, edad, sueldo, horasExtra, pagoEnviado, inscrito, porcentaje)

    def hacerPago(self):
        if self.getInscrito() == False:
            print("El empleado no esta inscrito a la asociacion")
            nomina = Nomina(self.getSueldo(), self.getHorasExtra(), 0)
        else:            
            nomina = Nomina(self.getSueldo(), self.getHorasExtra(), self.getPorcentaje())
        print("Se le esta realizando el pago al empleado; " + self.getNombre())
        nomina.calcularSueldo()
        self.setPagosEnviado(True)


emp = Empleado("Juan", 25, 5000, 10, False, True, 0.25)
emp.hacerPago()
    



