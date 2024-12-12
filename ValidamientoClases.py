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
##BusquedaBinaria
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

from ORDENADOR_AGENDA import ORDENADOR_AGENDA
from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion

objeto = ORDENADOR_AGENDA()
#usuario 1
user1 = Usuario("Juan-Perez", 24567898)
fecha_user1 = Fecha("12", "10", "1980")
user1.setFecha_nacimiento(fecha_user1)
user1.setCiudad_nacimiento("Medellin")
user1.setTel("3003233234")
user1.setEmail("juanperez@edl.edu.co")
direccion_user1 = Direccion()
direccion_user1.setAll("kr74", "4T-35", "Boston", "Medellin", "null", "null")
user1.setDir(direccion_user1)


#usuario 2
user2 = Usuario("Diego-Palacio", 34568910)
fecha_user2 = Fecha("20", "12", "1979")
user2.setFecha_nacimiento(fecha_user2)
user2.setCiudad_nacimiento("Envigado")
user2.setTel("3013234567")
user2.setEmail("diegopalacio@edl.edu.co")
direccion_user2 = Direccion()
direccion_user2.setAll("cll65", "3-29", "Robledo", "Medellin", "Balcones-de-la-Quinta", "405")
user2.setDir(direccion_user2)


#usuario 3
user3 = Usuario("Camila-Jimenez", 2345902)
fecha_user3 = Fecha("15", "09", "1985")
user3.setFecha_nacimiento(fecha_user3)
user3.setCiudad_nacimiento("Cali")
user3.setTel("3003234567")
user3.setEmail("camilajimenez@edl.edu.co" )
direccion_user3 = Direccion()
direccion_user3.setAll("tr45", "4S-73", "Poblado", "Medellin", "null", "null")
user3.setDir(direccion_user3)


#usuario 4
user4 = Usuario("Pedro-Gomez", 1075689)
fecha_user4 = Fecha("20", "02", "1990")
user4.setFecha_nacimiento(fecha_user4)
user4.setCiudad_nacimiento("Popayan")
user4.setTel("3003012323")
user4.setEmail("pedrogomez@edl.edu.co")
direccion_user4 = Direccion()
direccion_user4.setAll("kr23", "8-10", "SanJuan", "Envigado", "Mirador", "503")
user4.setDir(direccion_user4)


#usuario 5
user5 = Usuario("Tatiana-Ramirez", 2345934 )
fecha_user5 = Fecha("15", "11", "1982")
user5.setFecha_nacimiento(fecha_user5)
user5.setCiudad_nacimiento("Medellin")
user5.setTel("3004567890")
user5.setEmail("tatianaramirez@edl.edu.co")
direccion_user5 = Direccion()
direccion_user5.setAll("cll5", "4S-69", "Poblado", "Medellin", "UrbColina", "1023")
user5.setDir(direccion_user5)

#Usuario 6
user6 = Usuario("jessica", 2345434 )
fecha_user6 = Fecha("15", "11", "1982")
user6.setFecha_nacimiento(fecha_user5)
user6.setCiudad_nacimiento("Medellin")
user6.setTel("3004567890")
user6.setEmail("jessica@edl.edu.co")
direccion_user6 = Direccion()
direccion_user6.setAll("cll5", "4S-69", "Poblado", "Medellin", "UrbColina", "1123")
user5.setDir(direccion_user6)

objeto.agregarUsuario(user1)
objeto.agregarUsuario(user2)
objeto.agregarUsuario(user3)
objeto.agregarUsuario(user4)
objeto.agregarUsuario(user5)
objeto.agregarUsuario(user6)

objeto.mostrar()
objeto.ordenar()

print('miremos como ordeno:\n')
objeto.mostrar()
