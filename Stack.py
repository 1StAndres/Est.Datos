from ListS import ListS

class Stack:
    
    def __init__(self):
        self.data = ListS()
    
    def size(self):
        return self.data.get_size()

    def isEmpty(self):
        return self.size() == 0
    
    def push(self, e):
        self.data.addFirst(e)
    
    def pop(self):
        return self.data.removeFirst()
    
    def top(self):
        if self.isEmpty() == False:
            return self.data.first().get_data()
        else:
            return None

#Prueba       
pila = Stack()
for i in range(2,11,2):
    pila.push(i)
pilaaux = pila
for j in range(pilaaux.size()):
    print(pila.pop())