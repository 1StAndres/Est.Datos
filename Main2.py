from Agenda import Agenda
from Usuario import Usuario
# parte a
agenda1 = Agenda(5)
agenda1.importF()

# parte b
for i in range(5):
    print(agenda1._registro[i].__str__())

# parte c
id = input("ingrese el id: ")
agenda1.eliminar(id)

# Parte d
agenda1.toFile()
