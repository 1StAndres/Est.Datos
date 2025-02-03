from ListS import ListS
from Queue import Queue
from Usuario import Usuario
from Direccion import Direccion
from Fecha import Fecha
class TurnoUsuario :
    def __init__(self):
        self.registro = Queue()
        #self.usuarioAtendido = stack()

    def Resgistrar(self, user):
        #user = Usuario("juan-perez", "12345678")
        self.registro.enqueue(user)

    def atenderSiguiente(self):
        User_atendido = self.registro.first()
        #self.usuarioAtendido.push(self.registro.dequeue())

    def toFile(self):
        while self.registro.isEmpty() != True:
            Esc_user = self.registro.first()
            Ing_user = self.registro.dequeue()
            #falta hacer uso de stack para volver a crear la cola
            with open("usuariospendientes.txt", "a") as f:
                f.write(f"{Esc_user}")


#prueba
print("Revisa el nuevo txt :)")
user1 = Usuario("jose-rojas", "123451")
user2 = Usuario("juan-perez", "123456")
user3 = Usuario("maria-rojas", "123457")
user4 = Usuario("diana-pinal", "123458")
user5 = Usuario("pedro-jesus", "123459")
Turno = TurnoUsuario()
Turno.Resgistrar(user1)
Turno.Resgistrar(user2)
Turno.Resgistrar(user3)
Turno.Resgistrar(user4)
Turno.Resgistrar(user5)
Turno.toFile()
