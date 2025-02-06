import random
from HEAP import HEAP
from PriorityQueue import PriorityQueue

lista_prueba = [random.randint(1,20)]
while len(lista_prueba) < 20:
    lista_check = random.randint(1,20)
    if lista_check not in lista_prueba:
        lista_prueba.append(lista_check) 
print("Lista de numeros aleatorios: ", lista_prueba)
print("Tamaño de la lista:", len(lista_prueba))


prueba_heap = HEAP(len(lista_prueba))

print("Vamos a construir un heap de la lista de numeros aleatorios")
print("Antes del BUILD-MAX-HEAP:", lista_prueba)
max_heap = prueba_heap.buildMaxHeap(lista_prueba)
print("Despues del BUILD-MAX-HEAP:", lista_prueba)
print("HEAP-SORT:", prueba_heap.heap_sort())

input("Ahora probaremos la segunda parte:\n ")




lista_prueba2 = [random.randint(1,20)]
while len(lista_prueba2) < 20:
    lista_check = random.randint(1,20)
    if lista_check not in lista_prueba2:
        lista_prueba2.append(lista_check)
print(lista_prueba2)
prueba_2_heap = PriorityQueue(len(lista_prueba2))

for k in lista_prueba2:
    prueba_2_heap.maxHeapInsert(k)

print("Estado del HEAP despues del MAXHEAPINSERT:", prueba_2_heap.heap.getA())

print("HEAP-MAXIMUM:", prueba_2_heap.heapMaximum())

heap_max_ext = prueba_2_heap.heapExtractMax()
print("Numero extraido del HEAP-EXTRACT-MAX:", heap_max_ext)
print("Nuevo estado del heap:", prueba_2_heap.heap.getA())
print("Insertar numero 21 con MAX-HEAP-INSERT:", prueba_2_heap.maxHeapInsert(21))
print("Estado actual del heap:", prueba_2_heap.heap.getA())