
class Calculadora:

    def __init__(self, numero1, numero2, porcentaje):
        self.numero1 = numero1
        self.numero2 = numero2
        self.porcentaje = porcentaje

    def calcularSueldo(self):
        return self.numero1 + self.numero2
    
    def __descuentoIgss(self):
        return self.calcularSueldo() * 0.0483
    
    def  __descuentoIsr(self):
        if self.calcularSueldo() >= 5000:
            return self.calcularSueldo() * 0.05
        else:
            return 0
        
    def calcularDescuentos(self):
        print("total descuento " + str(self.__descuentoIgss() + self.__descuentoIsr()))
        return self.__descuentoIgss() + self.__descuentoIsr()
    
    def descuentoAsociacion(self, sueldo, porcentaje):
        return sueldo * porcentaje
    
    def calcularSueldoNeto(self):
        if self.porcentaje != 0:
            print("sueldo neto con calculo de descueto de asociacion solidarista " + str(self.calcularSueldo() - self.calcularDescuentos() - self.descuentoAsociacion(self.numero1, self.porcentaje)))
            return self.calcularSueldo() - self.calcularDescuentos() - self.descuentoAsociacion(self.numero1, self.porcentaje)
        else: 
            print("sueldo neto sin descuento de asociacion solidarista" + str(self.calcularSueldo() - self.calcularDescuentos()))
            return self.calcularSueldo() - self.calcularDescuentos()
    
    
        