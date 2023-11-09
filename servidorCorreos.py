class Correos:

    def __init__(self, pago, descuentos):
        self.pago = pago
        self.descuentos = descuentos

    def enviarCorreo(self):
        print("Enviando a enviar correo")
        print("Total pagado: " + str(self.pago))
        print("Total descuentos: " + str(self.descuentos))
        print("correo enviado!!!")
        # aca definir implementacion para enviar corroe electronico