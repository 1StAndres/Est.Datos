from Node import Node
from ListS import ListS
from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion


#crea lista enlazada
lista = ListS()
#ingresa valores pares del 1 al 20
i = 2
while (i <= 20):
    lista.addLast(i)
    i = i + 2
lista.print_list()  

#elimina el numero 20 que esta en la ultima posicion
print("\ndato eliminado:", lista.removeLast())

#elimina el numero 10 de la lista
temp = lista.head
while (temp != None and temp.get_data() != 10):
    anterior = temp
    temp = temp.get_next()#termina siendo 10
if temp != None:
    anterior.set_next(temp.get_next())
    temp.set_next(None)
    lista.size -= 1
#muestra como quedo la lista despues de eliminar 10 y 20    
lista.print_list()

#Nueva lista para enunciado B
listaUsers = ListS()

#usuario 1
user1 = Usuario("Juan-Perez", "24567898")
fecha_user1 = Fecha("12", "10", "1980")
user1.setFecha_nacimiento(fecha_user1)
user1.setCiudad_nacimiento("Medellin")
user1.setTel("3003233234")
user1.setEmail("juanperez@edl.edu.co")
direccion_user1 = Direccion()
direccion_user1.setAll("kr74", "4T-35", "Boston", "Medellin", "null", "null")
user1.setDir(direccion_user1)
listaUsers.addFirst(user1)
#print('\n',user1)

#usuario 2
user2 = Usuario("Diego-Palacio", "34568910")
fecha_user2 = Fecha("20", "12", "1979")
user2.setFecha_nacimiento(fecha_user2)
user2.setCiudad_nacimiento("Envigado")
user2.setTel("3013234567")
user2.setEmail("diegopalacio@edl.edu.co")
direccion_user2 = Direccion()
direccion_user2.setAll("cll65", "3-29", "Robledo", "Medellin", "Balcones-de-la-Quinta", "405")
user2.setDir(direccion_user2)
listaUsers.addLast(user2)
#print(user2)

#usuario 3
user3 = Usuario("Camila-Jimenez", "2345902")
fecha_user3 = Fecha("15", "09", "1985")
user3.setFecha_nacimiento(fecha_user3)
user3.setCiudad_nacimiento("Cali")
user3.setTel("3003234567")
user3.setEmail("camilajimenez@edl.edu.co" )
direccion_user3 = Direccion()
direccion_user3.setAll("tr45", "4S-73", "Poblado", "Medellin", "null", "null")
user3.setDir(direccion_user3)
listaUsers.addLast(user3)
#print(user3)

#usuario 4
user4 = Usuario("Pedro-Gomez", "1075689")
fecha_user4 = Fecha("20", "02", "1990")
user4.setFecha_nacimiento(fecha_user4)
user4.setCiudad_nacimiento("Popayan")
user4.setTel("3003012323")
user4.setEmail("pedrogomez@edl.edu.co")
direccion_user4 = Direccion()
direccion_user4.setAll("kr23", "8-10", "SanJuan", "Envigado", "Mirador", "503")
user4.setDir(direccion_user4)
listaUsers.addLast(user4)
#print(user4)

#usuario 5
user5 = Usuario("Tatiana-Ramirez", "2345934" )
fecha_user5 = Fecha("15", "11", "1982")
user5.setFecha_nacimiento(fecha_user5)
user5.setCiudad_nacimiento("Medellin")
user5.setTel("3004567890")
user5.setEmail("tatianaramirez@edl.edu.co")
direccion_user5 = Direccion()
direccion_user5.setAll("cll5", "4S-69", "Poblado", "Medellin", "UrbColina", "1023")
user5.setDir(direccion_user5)
listaUsers.addLast(user5)
#print(user5)

print('\n')
listaUsers.print_list()


#usuario 6 por consola
print('Hola, ingresa la siguiente informacion: ')
nombre = input('Nombre: ')
id = input('identificacion: ')
user6= Usuario(nombre, id)#crea usuario

dd = input('dia de nacimiento: ')
mm = input('mes de nacimiento: ')
aa = input('año de nacimiento: ')
user_fecha = Fecha(int(dd), int(mm), int(aa))
user6.setFecha_nacimiento(user_fecha)#fecha

ciudad_nacimiento = input('Ciudad de nacimiento: ')
user6.setCiudad_nacimiento(ciudad_nacimiento)#ciudad de nacimiento

tel = input('Telefono: ')
user6.setTel(tel)#telefono

email = input('Email: ')
user6.setEmail(email)#Email

print('Direccion: ')
user6_direccion = Direccion()
cal = input('Calle: ')
user6_direccion.setCalle(cal)

nom = input('Nomenclatura: ')
user6_direccion.setNomenclatura(nom)

bar = input('Barrio: ')
user6_direccion.setBarrio(bar)

ciu = input('ciudad: ')
user6_direccion.setCiudad(ciu)

edi = input('Edificio: ')
user6_direccion.setEdificio(edi)

apa = input('Apartamento: ')
user6_direccion.setApto(apa)
user6.setDir(user6_direccion)#direccion

#agrega a la principio de la lista al usuario 6
listaUsers.addFirst(user6)

#usuario 7 por consola
print('Hola, ingresa la siguiente informacion: ')
nombre = input('Nombre: ')
id = input('identificacion: ')
user7= Usuario(nombre, id)#crea usuario

dd = input('dia de nacimiento: ')
mm = input('mes de nacimiento: ')
aa = input('año de nacimiento: ')
user_fecha = Fecha(int(dd), int(mm), int(aa))
user7.setFecha_nacimiento(user_fecha)#fecha

ciudad_nacimiento = input('Ciudad de nacimiento: ')
user7.setCiudad_nacimiento(ciudad_nacimiento)#ciudad de nacimiento

tel = input('Telefono: ')
user7.setTel(tel)#telefono

email = input('Email: ')
user7.setEmail(email)#Email

print('Direccion: ')
user7_direccion = Direccion()
cal = input('Calle: ')
user7_direccion.setCalle(cal)

nom = input('Nomenclatura: ')
user7_direccion.setNomenclatura(nom)

bar = input('Barrio: ')
user7_direccion.setBarrio(bar)

ciu = input('ciudad: ')
user7_direccion.setCiudad(ciu)

edi = input('Edificio: ')
user7_direccion.setEdificio(edi)

apa = input('Apartamento: ')
user7_direccion.setApto(apa)
user7.setDir(user7_direccion)#direccion

#agrega el usuario 7 al final de la lista
listaUsers.addLast(user7)

#imprime nuevamente la lista con los nuevos usuarios
listaUsers.print_list()
