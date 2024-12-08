import requests
class Agenda:
  def __init__(self, capacity):
    self._registro = [None] * capacity
    self.capaity = capacity
    self._no_reg = 0 
  
  def agregar(self, usuario):
    if self._no_reg < self.capacity:
        self._registro[self._no_reg] = usuario
        self._no_reg += 1
        return True
    else:
        print("La agenda está llena.")
        return False

  def buscar(self, id):
    for i in range(self._no_reg):
      if self._registro[i].getId() == id:
        return self._registro[i].getId()
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
          f.write(usuario.__str__()) # falta verificar el metodo (.__str__()) para que coincida como lo necesitemos escribir en el archivo)
          # ejm: (nombre id fechadia fechames fechaaño ciudad telefono email direccioncalle direccionnomenclatura direccionbarrio direccionciudad direccionedificio direccionapto)
          #todo separado solo con espacios sin - ni nada para que coincida con el ejempl_agenda que puso la profe

  def importF(self):
    with open("agenda_ejemplo.txt", "r") as f:
      for linea in f:
        datos = linea.strip().split()
        direccion = Direccion()
        direccion.setAll(datos[8], datos[9], datos[10], datos[11], datos[12], datos[13])
        fecha = Fecha(int(datos[2]), int(datos[3]), int(datos[4]))
        usuario = Usuario(datos[0], int(datos[1]))
        usuario.setAll(datos[0], int(datos[1]), fecha, datos[5], datos[6], datos[7], direccion)
        self.agregar(usuario)

