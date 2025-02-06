class HEAP:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.A = [None] * capacity

    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def maxHeapyfy(self, i):
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left < self.size and self.A[left] is not None and self.A[left] > self.A[largest]:
            largest = left
        
        if right < self.size and self.A[right] is not None and self.A[right] > self.A[largest]:
            largest = right

        if largest != i:
            temp = self.A[i]
            self.A[i] = self.A[largest]
            self.A[largest] = temp
            self.maxHeapyfy(largest)
        #return self.A    

    def buildMaxHeap(self, B):
        self.A = B[:] + [None] * (self.capacity - len(B))
        self.size = len(B)
        for i in range(self.size // 2 - 1, -1, -1):
            self.maxHeapyfy(i)
        return self.A    

    def heap_sort(self):
        self.buildMaxHeap(self.A)
        for i in range(self.size - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.size -= 1
            self.maxHeapyfy(0)
        return self.A

    def getSize(self):
        return self.size
    
    def setSize(self, size):
        self.size = size
    
    def getA(self):
        return self.A