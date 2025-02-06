from HEAP import HEAP

class PriorityQueue:

    def __init__(self, capacity):
        self.heap = HEAP(capacity)
    
    def maxHeapInsert(self, k):
        self.heap.setSize(self.heap.getSize() + 1)
        i = self.heap.getSize() - 1 #agregue -1
        A = self.heap.getA()
        A[i] = k
        while i>0 and A[self.heap.parent(i)] < A[i]:
            temp = A[self.heap.parent(i)]
            A[self.heap.parent(i)] = A[i]
            A[i] = temp
            i = self.heap.parent(i)

    def heapExtractMax(self):
        A = self.heap.getA()
        max = A[0]
        A[0] = A[self.heap.getSize() - 1] #No sé si va con -1 si hay problemas con las posiciones puede ser esto
        self.heap.setSize(self.heap.getSize() - 1)
        self.heap.maxHeapyfy(0)
        return max
    
    def heapMaximum(self):
        A = self.heap.getA()
        return A[0]