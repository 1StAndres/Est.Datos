from DoubleList import DoubleList
from Usuario import Usuario

class ORDENADOR_AGENDA():
    def __init__(self):
        self.lista = DoubleList()

    def agregarUsuario(self, usuario ):
        self.lista.addLast(usuario)
        return 'Usuario agregado'
    
    def ordenar(self):
        if self.lista.first() is None:  # Si la lista está vacía, no hay nada que ordenar
            return    
    # burbuja
        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.lista.first()
            while actual.getNext() is not None:  # Recorre la lista hasta el penúltimo nodo
                siguiente = actual.getNext()
                if actual.getData().getId() > siguiente.getData().getId():
                    # Intercambia los valores de los nodos
                    temp = actual.getData()
                    actual.setData(siguiente.getData())
                    siguiente.setData(temp)
                    cambiado = True
                actual = siguiente

    def mostrar(self):
        if self.lista.first() is None:
            print("La lista está vacía.")
            return

        # Imprime todos los datos de la lista
        temp = self.lista.first()
        while temp is not None:
            print(temp.getData())
            temp = temp.getNext()
