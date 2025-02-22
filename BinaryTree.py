from NodeT import Node
from Queue import Queue
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def is_root(self, node):
        return node == self.root

    def is_internal(self, node):
        return self.has_left(node) or self.has_right(node)

    def has_left(self, node):
        return node.getLeft() is not None

    def has_right(self, node):
        return node.getRight() is not None
    
    def getRoot(self):
        return self.root
    
    def getLeft(self, node):
        return node.getLeft()
    
    def getRight(self, node):
        return node.getRight()
    
    def depth(self, node):
        if self.is_root(node):
            return 0
        return 1 + self.depth(self.get_parent(node))

    def height(self, node):
        if not self.is_internal(node):
            return 0
        return 1 + max(self.height(self.left(node)), self.height(self.right(node)))
    
    def get_parent(self, node):
        if self.is_root(node):
            return None
        
        q = Queue()
        q.put(self.root)
        
        while not q.empty():
            temp = q.get()
            if temp.getLeft() == node or temp.getRight() == node:
                return temp
            if self.has_left(temp):
                q.put(temp.getLeft())
            if self.has_right(temp):
                q.put(temp.getRight())
        
        return None
    
    def add_root(self, value):
        if self.root is not None:
            raise ValueError("Raiz ya existe")
        self.root = Node(value)
        self.size = 1

    def insert_left(self, node, value):
        if node.getLeft() is not None:
            raise ValueError("Hijo izquierdo ya existes")
        node.setLeft(Node(value))
        self.size += 1

    def insert_right(self, node, value):
        if node.getRight() is not None:
            raise ValueError("Hijo derecho ya existe")
        node.setRight(Node(value))
        self.size += 1

    def remove(self, node):
        parent = self.get_parent(node)
        
        if self.has_left(node) or self.has_right(node):
            child = node.getLeft() if self.has_left(node) else node.getRight()
            if parent:
                if parent.getLeft() == node:
                    parent.setLeft(child)
                else:
                    parent.setRight(child)
            else:
                self.root = child
        else:
            if parent:
                if parent.getLeft() == node:
                    parent.setLeft(None)
                else:
                    parent.setRight(None)
            else:
                self.root = None
        
        self.size -= 1
