from Agenda import Agenda
from Usuario import Usuario
# parte a
agenda1 = Agenda(5)
agenda1.importF()

# parte b
for i in range(5):
    print(str(agenda1.getRegistro()[i]))
    

# parte c
id = input("ingrese el id: ")
agenda1.eliminar(id)

# Parte d
agenda1.toFile()
