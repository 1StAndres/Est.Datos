import random

class Ordenador:
    def __init__(self, capacity = "None"):
        self._limit = capacity
        self._A = [random.randint(0, 100) for i in range(self._limit)]
        
    def inicializar(self):
        self._A = [random.randint(0, 100) for j in range (self._limit)]

    def ordenar_burbuja(self):
        A = self._A
        capacity = self._limit

        for i in range(capacity-1):
            for j in range(1, capacity-i):
                if A[j-1] > A[j]:
                    self.intercambiar(j-1, j)
    
    def intercambiar(self,mayor,menor):
        temp1 = self._A[mayor]
        temp2 = self._A[menor]
        self._A[mayor] = temp2
        self._A[menor] = temp1

    def imprimir(self):
        print(self._A)

numeritos = Ordenador(6)
numeritos.imprimir()
numeritos.ordenar_burbuja()
numeritos.imprimir()
