from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion
class Agenda:
  def __init__(self, capacity):
    self._registro = [None] * capacity
    self.capacity = capacity
    self._no_reg = 0 
  
  def agregar(self, u):
    if self._no_reg < self.capacity:
        if  self.buscar(u.getId()) == -1:  #si hay algún error con agregar puede ser por esta línea que verifica si el usuario ya está en la agenda
            self._registro[self._no_reg] = u
            self._no_reg += 1
            print("El usuario nuevo se agregó correctamente")
            return True
        else:
          print("No es posible agregar nuevamente el usuario")
          return False
    else:
        print("La agenda está llena.")
        return False

  def buscar(self, id):
    for i in range(self._no_reg):
      if self._registro[i].getId() == id:
        return i
    return -1
  
  def eliminar(self, id):
    eliminar_user = self.buscar(id)
    if eliminar_user == -1:
      return False
    else:
      self._registro.pop(eliminar_user)
      self._registro.append(None)
      self._no_reg -= 1
      return True
  
  def toFile(self):
    with open("agenda.txt", "w") as f:
      for usuario in self._registro:
        if usuario is not None:
          f.write(usuario.__str__())

  def importF(self):
    with open("ejemplo_agenda.txt", "r") as f:
      for linea in f:
        datos = linea.strip().split()
        direccion = Direccion()
        direccion.setAll(datos[8], datos[9], datos[10], datos[11], datos[12], datos[13])
        fecha = Fecha(int(datos[2]), int(datos[3]), int(datos[4]))
        usuario = Usuario(datos[0], int(datos[1]))
        usuario.setAll(datos[0], int(datos[1]), fecha, datos[5], datos[6], datos[7], direccion)
        self.agregar(usuario)

