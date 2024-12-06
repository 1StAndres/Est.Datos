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
          f.write(usuario.__str__()) # falta verificar el metodo (.__str__()) para que coincida como lo necesitemos escribir en el archivo

  def importF(self): # en trabajo
    with open("agenda.txt", "r") as f:
      for line in f:
        data = line.strip().split()

