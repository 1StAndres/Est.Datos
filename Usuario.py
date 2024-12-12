from Fecha import Fecha
from Direccion import Direccion

class Usuario:
  def __init__(self, nombre = "None", id = "None"): 
    self._nombre = nombre
    self._id = id
    self._fecha_nacimiento = "None"
    self._ciudad_nacimiento = "None"
    self._tel = "None"
    self._email = "None"
    self._dir = "None"

  def setNombre(self, nombre):
    self._nombre = nombre
  def setId(self, id):
    self._id = id
  def setFecha_nacimiento(self, fecha_nacimiento):
    self._fecha_nacimiento = fecha_nacimiento
  def setCiudad_nacimiento(self, ciudad_nacimiento):
    self._ciudad_nacimiento = ciudad_nacimiento
  def setTel(self, tel):
    self._tel = tel
  def setEmail(self, email):
    self._email = email
  def setDir(self, dir):
    self._dir = dir

  def setAll(self, n, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
    self.n = n
    self.id = id
    self.fecha_nacimiento = fecha_nacimiento
    self.ciudad_nacimiento = ciudad_nacimiento
    self.tel = tel
    self.email = email
    self.dir = dir

  def getNombre(self):
    return self._nombre
  def getId(self):
    return self._id
  def getFecha_nacimiento(self):
    return self._fecha_nacimiento
  def getCiudad_nacimiento(self):
    return self._ciudad_nacimiento
  def getTel(self):
    return self._tel
  def getEmail(self):
    return self._email
  def getDir(self):
    return self._dir
  def toString(self):
    return

  def __str__(self):
    fecha_nacimiento_str = str(self._fecha_nacimiento.getDia()) + " " + str(self._fecha_nacimiento.getMes()) + " " + str(self._fecha_nacimiento.getA())
    return self._nombre + " " + self._id + " " + fecha_nacimiento_str + " " +  self._ciudad_nacimiento + " " +  self._tel + " " + self._email + " " +  str(self._dir) + "\n"
