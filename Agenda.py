import requests

class Agenda:
  def __init__(self, capacity=int):#capacity = capacidad max de almacenamiento de usuarios
    self._registro = [1]
    self._no_reg = int = 0 #numero de usuarios ingresados

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
      return True # Aviso solo es para continuar con otros metodos por el momento
  
  def toFile(self):
    url = "https://github.com/1StAndres/Est.Datos/blob/main/agenda.txt" 
    response = requests.get(url)
    with open("agenda.txt", "w") as f:
            f.write(self._registro)
toFile()
