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

    def ordenar_seleccion(self):
        A = self._A
        capacity = self._limit
        
        for i in range(capacity-1):
            minIndex = i
            for j in range(i+1,capacity):
                if A[j] < A[minIndex]:
                    minIndex = j
            self.intercambiar(i, minIndex)

    def ordenar_insercion(self):
        A = self._A
        capacity = self._limit

        for i in range(1, capacity):
            temp = A[i]
            j = i
            while j>0 and A[j-1]>temp:
                A[j] = A[j-1]
                j -= 1
            A[j] = temp

    ####
    def ordenar_mergeSort(self):
        self._mergeSort(0, self._limit - 1)

    def _mergeSort(self, p, r):
        if p < r:
           q = (p + r) // 2   
           self._mergeSort(p, q) 
           self._mergeSort(q + 1, r)
           self._merge(p, q, r)

    def _merge(self, p, q, r):
        left = self._A[p:q+1] 
        right = self._A[q+1:r+1]  
        i = j = 0
        k = p

        while i < len(left) and j < len(right):
            if left[i] <= right[j]: 
                self._A[k] = left[i]   
                i += 1
            else:
                self._A[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            self._A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            self._A[k] = right[j]
            j += 1
            k += 1
    
    def mostrar(self):
        print(self._A)
    
    def busqueda_binaria(self, x):
        return self._busquedaBinaria(0, self._limit-1, x)
    
    def _busquedaBinaria(self, iLeft, iRight, x):
        if iLeft > iRight:
            return -1
        mid = (iLeft + iRight)//2
        if x < self._A[mid]:
            return self._busquedaBinaria(iLeft, mid - 1, x)
        elif x > self._A[mid]:
            return self._busquedaBinaria(mid + 1, iRight, x)
        else:
            return mid