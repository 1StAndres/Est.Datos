from Node import Node 

class ListS:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def get_size(self):
    return self.size
  
  def is_empty(self):
    return self.size == 0
  
  def first(self):
    return self.head
  
  def last(self):
    return self.tail
    
  def addFirst(self, datos):
      nuev_nodo = Node(datos)
      
      if self.is_empty():
        self.head = nuev_nodo
        self.tail = nuev_nodo
      
      else:
        nuev_nodo.set_next = self.head
        self.head = nuev_nodo
      
      self.size += 1
  
  def addLast(self, datos):
    nuev_nodo = Node(datos)
    
    if self.is_empty():
      self.head = nuev_nodo
      self.tail = nuev_nodo
    
    else:
      self.tail = nuev_nodo
      self.tail.set_next = nuev_nodo
      
    self.size += 1
  
  def removeFirst(self):
    if self.is_empty():
      return None

    infoEliminada = self.head.get_data()
    self.head = self.head.get_next()

    if self.head is None:  
      self.tail = None
    self.size -= 1
    return infoEliminada
  
  def removeLast(self):
    if self.is_empty():
      return None
    if self.size == 1:
      return self.removeFisrt()
    else:
      nuevaCola = self.last.get_data()
      Anterior = self.head()
      while (Anterior != self.tail):
        Anterior = Anterior.get_next()
    Anterior.set_next() == None
    nuevaCola = Anterior
    self.size -= 1
    return nuevaCola.get_data()
