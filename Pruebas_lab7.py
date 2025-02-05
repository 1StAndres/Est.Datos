import random
from HEAP import HEAP

lista_prueba = [random.randint(1,20)]
while len(lista_prueba) < 20:
    lista_check = random.randint(1,20)
    if lista_check not in lista_prueba:
        lista_prueba.append(lista_check) 
print("Lista de numeros aleatorios: ", lista_prueba)
print("Tamaño de la lista:", len(lista_prueba))


prueba_heap = HEAP(20)

print("Vamos a construir un heap de la lista de numeros aleatorios")
print("Antes del BUILD-MAX-HEAP:", lista_prueba)
print("Despues del BUILD-MAX-HEAP:", prueba_heap.buildMaxHeap(lista_prueba))