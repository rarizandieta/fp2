
class Persona(object):

    def __init__(self, nombre, edad, sueldo, horasExtra, pagoEnviado, inscrito, porcentaje):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.horasExtra =  horasExtra
        self.pagosEnviado = pagoEnviado  //flag
        self.inscrito = inscrito
        self.porcentaje = porcentaje

    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getSueldo(self):
        return self.sueldo
    
    def getHorasExtra(self):
        return self.horasExtra
    
    def getPagosEnviado(self):
        return self.pagosEnviado
    
    def getInscrito(self):
        return self.inscrito
    
    def getPorcentaje(self):
        return self.porcentaje
    
    def setNombre(self, nombre):    
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setSueldo(self, sueldo):
        self.sueldo = sueldo

    def setHorasExtra(self, horasExtra):
        self.horasExtra = horasExtra

    def setPagosEnviado(self, pagosEnviado):
        self.pagosEnviado = pagosEnviado

    def setInscrito(self, inscrito):
        self.inscrito = inscrito

    def setPorcentaje(self, porcentaje):
        self.porcentaje = porcentaje
    