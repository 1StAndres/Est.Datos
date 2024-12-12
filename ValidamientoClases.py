from ORDENADOR_LISTA import ORDENADOR_LISTA
from Ordenador import Ordenador
#Apartado A
new = Ordenador(10)
##burbuja
new.inicializar()
new.mostrar()
new.ordenar_burbuja()
new.mostrar()
##selección
new.inicializar()
new.mostrar()
new.ordenar_seleccion()
new.mostrar()
##inserción
new.inicializar()
new.mostrar()
new.ordenar_insercion()
new.mostrar()
##MergeSort
new.inicializar()
new.mostrar()
new.ordenar_mergeSort()
new.mostrar()

busqueda = new.busqueda_binaria(int(input("Introduzca el número que desea buscar: ")))
if busqueda == -1:
    print("El elemento no se encontró en el arreglo")
else:
    print("El elemento se encuentra en la posición: " + str(busqueda))
#Apartado B
ordenando = ORDENADOR_LISTA()
ordenando.inicializar(12)
ordenando.ordenar()
ordenando.mostrar()
print("\n")
#Apartado C