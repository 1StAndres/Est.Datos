#en algun momento del semetre tenia esto avanzado asi que lo monto pero esto es para el lab 4
class Node:

  def __init__(self, data=None):
    self.data = data  # Dato almacenado en el nodo
    self.next = None  # Referencia al siguiente nodo

  def set_data(self, data):
    self.data = data

  def set_next(self, next_node):
    self.next = next_node

  def get_data(self):
    return self.dat

  def get_next(self):
    return self.next
