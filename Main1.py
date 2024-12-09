from Usuario import Usuario
from Agenda import Agenda 
from Fecha import Fecha
from Direccion import Direccion
#iniciar agenda
agenda = Agenda(5)

# usuario 1
user1 = Usuario("Juan-Perez", "24567898")
fecha_user1 = Fecha("12", "10", "1980")
user1.setFecha_nacimiento(fecha_user1)
user1.setCiudad_nacimiento("Medellin")
user1.setTel("3003233234")
user1.setEmail("juanperez@edl.edu.co")
direccion_user1 = Direccion()
direccion_user1.setAll("kr74", "4T-35", "Boston", "Medellin", "null", "null")
user1.setDir(direccion_user1)
print(user1)

#agregar usuario
agenda.agregar(user1)

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
print(user2)

#agregar usuario
agenda.agregar(user2)

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
print(user3)

#agregar usuario
agenda.agregar(user3)

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
print(user4)

#agregar usuario
agenda.agregar(user4)

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
print(user5)

#agregar usuario
agenda.agregar(user5)

agenda.buscar("1075689")#id de Pedro-Gomez retorna en numero donde esta ubicado en el arreglo

agenda.toFile()
