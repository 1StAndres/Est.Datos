from ListS import ListS
from Queue import Queue
from Usuario import Usuario
from Direccion import Direccion
from Fecha import Fecha
from Stack import Stack
class TurnoUsuario :
    def __init__(self):
        self.registro = Queue()
        self.usuarioAtendido = Stack()

    def Resgistrar(self, user):
        self.registro.enqueue(user)

    def atenderSiguiente(self):
        self.registro.first()
        self.usuarioAtendido.push(self.registro.dequeue())

    def toFile(self):
        if self.registro.isEmpty() != True:
            while self.registro.isEmpty() != True:
                Esc_user = self.registro.first()
                Ing_user = self.registro.dequeue()
            #falta hacer uso de stack para volver a crear la cola
                with open("usuariospendientes.txt", "a") as f:
                    f.write(f"{Esc_user}")
        if self.usuarioAtendido.isEmpty() != True:
            while self.usuarioAtendido.isEmpty() != True: 
                tp_user = self.usuarioAtendido.top() 
                pp_user = self.usuarioAtendido.pop()
                #asist_stack = Stack()
                #asist_stack.push(tp_user)   
                with open("usuarioatendidos.txt", "a") as r:
                    r.write(f"{tp_user}")   


#prueba

while True:
    ejemplo_turno = input("Cual ejemplo quieres hacer: 1, 2 o 3(opcion de salir) ")
    if ejemplo_turno == "1":
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
        print("Revisa el txt")
    if ejemplo_turno == "2":
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
        Turno.atenderSiguiente()
        Turno.atenderSiguiente()
        Turno.toFile()
        print("Revisa los txt")
    if ejemplo_turno == "3":
        print("Nos vemos ;)")
        break          
