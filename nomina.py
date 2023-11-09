from calculadora import Calculadora
from banco import Banco
from servidorCorreos import Correos

class Nomina():

    def __init__(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3

    def calcularSueldo(self):
        calculadora = Calculadora(self.valor1, self.valor2, self.valor3)
        self.envioPago(calculadora.calcularSueldoNeto())
        return calculadora.calcularSueldoNeto()
    
    def envioPago(self, pago):
        print("entrando a enviar pago")
        pago = Banco.enviarACH(pago)

        if pago:
            calculadora = Calculadora(self.valor1, self.valor2)
            sueldo = calculadora.calcularSueldoNeto()
            descuento = calculadora.calcularDescuentos()
            correo = Correos(sueldo, descuento)
            correo.enviarCorreo()
            
