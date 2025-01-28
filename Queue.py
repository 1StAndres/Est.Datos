from ListS import ListS
class Queue:
    
    def __init__(self):
        self.data = ListS()

    def size(self):
        return self.data.get_size()
    
    def isEmpty(self):
        return self.data.is_empty()
    
    def enqueue(self, item):
        self.data.addLast(item)
    
    def dequeue(self):
        return self.data.removeFirst()
           
    def first(self):
        return self.data.first().get_data()
    
#probando
cola = Queue()
for i in range(2,11,2):
    cola.enqueue(i)
print(cola.dequeue())
