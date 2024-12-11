from ListS import ListS
import random

# Clase ORDENADOR_LISTA 
class ORDENADOR_LISTA:
    
  def __init__(self):
    self.lista = None
  
  def inicializar(self, n):
    self.lista = ListS() # Inicializa una nueva lista vacía
    for i in range(n):
      numrandom = random.randint(1,100) # Genera un número aleatorio entre 1 y 100
      self.lista.addLast(numrandom)
  
  def ordenar(self):
    if self.lista.first() is None:  # Si la lista está vacía, no hay nada que ordenar
      return    
    # Nodo actual que estamos tratando de ordenar
    temp = self.lista.first()    
    while temp is not None:  
      llave = temp
      j = self.lista.first()    
      while j != llave:  
        if j.get_data() > llave.get_data(): 
            temp_value = llave.get_data()
            llave.set_data(j.get_data())
            j.set_data(temp_value)
        j = j.get_next()    
      temp = temp.get_next()

  def mostrar(self):
    self.lista.print_list()
    